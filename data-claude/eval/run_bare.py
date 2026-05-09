#!/usr/bin/env python3
"""
Run the bare pre-RAG /ask-docs skill (as it existed at commit f9f39cc) on
selected benchmark questions, capturing tool-call telemetry from claude -p
stream-json output.

Usage:
  python baseline_bare/scripts/run_bare.py --only Q027              # smoke test
  python baseline_bare/scripts/run_bare.py --only Q005,Q036,Q049    # remainder
  python baseline_bare/scripts/run_bare.py --all                    # all 4
  python baseline_bare/scripts/run_bare.py --all --clean            # truncate output first
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent  # claude_docs_monitor/
BENCHMARK = REPO / "data-claude" / "eval" / "benchmark.jsonl"
OUTPUTS_DIR = REPO / "data-claude" / "eval" / "runs" / "bare"
REPORTS_PATH = OUTPUTS_DIR / "reports.jsonl"

DEFAULT_QIDS = ["Q005", "Q027", "Q036", "Q049"]
MODEL = "claude-opus-4-7"
TIMEOUT_SEC = 300
BASELINE_TAG = "bare-ask-docs-f9f39cc"


def load_benchmark(qids):
    by_id = {}
    for line in BENCHMARK.read_text().splitlines():
        if line.strip():
            it = json.loads(line)
            by_id[it["id"]] = it
    out = []
    for qid in qids:
        if qid in by_id:
            out.append(by_id[qid])
        else:
            print(f"WARN: {qid} not in benchmark", file=sys.stderr)
    return out


def parse_stream_json(stdout):
    """Parse claude -p stream-json output. Dedupe tool_use by id, prefer
    the version with a populated input dict (in case partial deltas arrive
    first under --include-partial-messages)."""
    session_id = None
    tool_use_by_id = {}
    text_chunks = []
    final_text = None
    usage = None
    cost_usd = None
    num_turns = None
    stop_reason = None

    for line in stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        t = ev.get("type")
        if t == "system" and ev.get("subtype") == "init":
            session_id = ev.get("session_id")
        elif t == "assistant":
            msg = ev.get("message") or {}
            for block in (msg.get("content") or []):
                btype = block.get("type")
                if btype == "tool_use":
                    tid = block.get("id") or f"_anon_{len(tool_use_by_id)}"
                    name = block.get("name")
                    inp = block.get("input")
                    existing = tool_use_by_id.get(tid)
                    if existing is None:
                        tool_use_by_id[tid] = {"id": tid, "name": name, "input": inp}
                    else:
                        if name and not existing.get("name"):
                            existing["name"] = name
                        if isinstance(inp, dict) and inp:
                            # Prefer the populated dict over earlier empty/partial
                            existing["input"] = inp
                elif btype == "text":
                    txt = block.get("text")
                    if txt:
                        text_chunks.append(txt)
        elif t == "result":
            if ev.get("subtype") == "success":
                final_text = ev.get("result")
            usage = ev.get("usage")
            cost_usd = ev.get("total_cost_usd")
            num_turns = ev.get("num_turns")
            stop_reason = ev.get("stop_reason")

    if not final_text and text_chunks:
        final_text = "".join(text_chunks)

    return {
        "session_id": session_id,
        "tool_calls": list(tool_use_by_id.values()),
        "final_text": final_text,
        "usage": usage,
        "total_cost_usd": cost_usd,
        "num_turns": num_turns,
        "stop_reason": stop_reason,
    }


def _shorten(obj, limit=2000):
    if obj is None:
        return None
    if isinstance(obj, str):
        return obj if len(obj) <= limit else obj[:limit] + f"...<+{len(obj)-limit}>"
    try:
        s = json.dumps(obj, ensure_ascii=False)
    except (TypeError, ValueError):
        return repr(obj)[:limit]
    if len(s) <= limit:
        return obj
    return s[:limit] + f"...<+{len(s)-limit}>"


def now_z():
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def run_one(qid, question):
    # NOTE: invoke /ask-docs-bare (a project-level alias of the worktree's
    # historical /ask-docs skill, identical body) to bypass shadowing by the
    # user-level ~/.claude/commands/ask-docs.md (which is the new hybrid version
    # and would invoke MCP RAG tools instead of the bare grep/read flow).
    prompt = f"/ask-docs-bare {question}"
    cmd = [
        "claude", "-p",
        "--model", MODEL,
        "--output-format", "stream-json",
        "--include-partial-messages",
        "--verbose",
        "--dangerously-skip-permissions",
        "--", prompt,
    ]
    print(f"[{qid}] starting (timeout={TIMEOUT_SEC}s)", file=sys.stderr)
    t0 = time.time()
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(REPO),
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SEC,
        )
        elapsed = round(time.time() - t0, 2)
    except subprocess.TimeoutExpired as exc:
        elapsed = round(time.time() - t0, 2)
        partial_stderr = (exc.stderr or "") if isinstance(exc.stderr, str) else (exc.stderr or b"").decode("utf-8", "replace")
        print(f"[{qid}] TIMED OUT after {elapsed:.0f}s", file=sys.stderr)
        return {
            "id": qid,
            "question": question,
            "ts": now_z(),
            "report": {
                "ok": False,
                "exit_code": -1,
                "elapsed_s": elapsed,
                "report_md_text": "",
                "report_json_data": {
                    "question": question,
                    "model": MODEL,
                    "evidence": [],
                    "n_tool_calls": 0,
                    "tools_used": [],
                    "tool_call_details": [],
                    "error": "timeout",
                    "baseline": BASELINE_TAG,
                },
                "stderr_tail": partial_stderr[-2000:],
                "cmd": " ".join(cmd),
            },
        }

    parsed = parse_stream_json(proc.stdout)
    final_text = parsed["final_text"] or ""
    tools_used = [tc["name"] for tc in parsed["tool_calls"] if tc.get("name")]
    tool_call_details = [
        {"name": tc.get("name"), "input": _shorten(tc.get("input"))}
        for tc in parsed["tool_calls"]
    ]
    usage = parsed["usage"] or {}
    ok = (proc.returncode == 0) and bool(final_text)
    print(
        f"[{qid}] ok={ok} exit={proc.returncode} elapsed={elapsed}s "
        f"tools={len(parsed['tool_calls'])} answer_len={len(final_text)}",
        file=sys.stderr,
    )

    return {
        "id": qid,
        "question": question,
        "ts": now_z(),
        "report": {
            "ok": ok,
            "exit_code": proc.returncode,
            "elapsed_s": elapsed,
            "report_md_text": final_text,
            "report_json_data": {
                "question": question,
                "model": MODEL,
                "evidence": [],
                "n_tool_calls": len(parsed["tool_calls"]),
                "tools_used": tools_used,
                "tool_call_details": tool_call_details,
                "session_id": parsed["session_id"],
                "input_tokens": usage.get("input_tokens"),
                "output_tokens": usage.get("output_tokens"),
                "cache_read_input_tokens": usage.get("cache_read_input_tokens"),
                "cache_creation_input_tokens": usage.get("cache_creation_input_tokens"),
                "total_cost_usd": parsed["total_cost_usd"],
                "num_turns": parsed["num_turns"],
                "stop_reason": parsed["stop_reason"],
                "baseline": BASELINE_TAG,
            },
            "stderr_tail": (proc.stderr or "")[-2000:],
            "cmd": " ".join(cmd),
        },
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", "--ids", dest="only", default="", help="Comma-separated QIDs (e.g., Q027)")
    ap.add_argument("--all", action="store_true", help=f"Run all default IDs: {','.join(DEFAULT_QIDS)}")
    ap.add_argument("--out", default=str(REPORTS_PATH), help="Output reports.jsonl path")
    ap.add_argument("--clean", action="store_true", help="Truncate output file before writing")
    args = ap.parse_args()

    if args.only:
        qids = [q.strip() for q in args.only.split(",") if q.strip()]
    elif args.all:
        qids = DEFAULT_QIDS
    else:
        print("specify --only QIDs or --all", file=sys.stderr)
        sys.exit(2)

    items = load_benchmark(qids)
    if not items:
        print("no benchmark items matched", file=sys.stderr)
        sys.exit(1)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if args.clean and out_path.exists():
        out_path.unlink()

    with open(out_path, "a") as f:
        for it in items:
            rec = run_one(it["id"], it["question"])
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            f.flush()
    print(f"wrote {len(items)} record(s) -> {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
