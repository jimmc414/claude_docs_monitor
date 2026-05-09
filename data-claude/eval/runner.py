"""
Adversarial review runner — Phase B harness.

Reads benchmark.jsonl, runs the system on each question across surfaces,
captures answers + evidence to answers.jsonl. Captures the EXACT cli command
per item for reproducibility.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
EVAL_DIR = REPO / "data-claude" / "eval"
RUNS_DIR = EVAL_DIR / "runs"

ENV = {**os.environ}
# Strip ANTHROPIC_API_KEY so Max OAuth is used
ENV.pop("ANTHROPIC_API_KEY", None)


def run_search(question: str, k: int = 10, timeout: int = 120) -> dict:
    cmd = [
        "python", str(REPO / "claude_docs_monitor.py"),
        "search", question, "--k", str(k), "--json",
    ]
    t0 = time.time()
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True,
            env=ENV, cwd=str(REPO), timeout=timeout,
        )
        elapsed = time.time() - t0
        try:
            hits = json.loads(result.stdout) if result.stdout.strip() else []
        except json.JSONDecodeError as e:
            hits = []
            return {
                "ok": False, "error": f"json_decode: {e}",
                "stderr_tail": result.stderr[-500:],
                "stdout_tail": result.stdout[-500:],
                "elapsed_s": elapsed,
                "cmd": " ".join(cmd[:3]) + f' "{question}" --k {k} --json',
            }
        return {
            "ok": result.returncode == 0,
            "exit_code": result.returncode,
            "hits": hits,
            "elapsed_s": elapsed,
            "stderr_tail": result.stderr[-500:] if result.returncode else None,
            "cmd": " ".join(cmd[:3]) + f' "{question}" --k {k} --json',
        }
    except subprocess.TimeoutExpired:
        return {
            "ok": False, "error": "timeout",
            "elapsed_s": timeout,
            "cmd": " ".join(cmd[:3]) + f' "{question}" --k {k} --json',
        }


def run_report(
    question: str,
    scope: str = "docs",
    max_turns: int = 4,
    timeout: int = 600,
    out_dir: Path | None = None,
) -> dict:
    cmd = [
        "python", str(REPO / "claude_docs_monitor.py"),
        "report", question,
        "--scope", scope,
        "--max-turns", str(max_turns),
        "--no-self-critique",
        "--model", "sonnet",
    ]
    if out_dir:
        cmd.extend(["--report", str(out_dir)])
    t0 = time.time()
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True,
            env=ENV, cwd=str(REPO), timeout=timeout,
        )
        elapsed = time.time() - t0
        # Find the most recent report file
        report_md = None
        report_json = None
        reports_dir = (out_dir or REPO / "data-claude") / "reports"
        if reports_dir.exists():
            md_files = sorted(reports_dir.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
            json_files = sorted(reports_dir.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
            if md_files and md_files[0].stat().st_mtime > t0 - 5:
                report_md = md_files[0]
            if json_files and json_files[0].stat().st_mtime > t0 - 5:
                report_json = json_files[0]

        return {
            "ok": result.returncode == 0,
            "exit_code": result.returncode,
            "report_md_path": str(report_md) if report_md else None,
            "report_json_path": str(report_json) if report_json else None,
            "report_md_text": report_md.read_text() if report_md else None,
            "report_json_data": json.loads(report_json.read_text()) if report_json else None,
            "elapsed_s": elapsed,
            "stderr_tail": result.stderr[-1000:] if result.returncode else None,
            "stdout_tail": result.stdout[-500:],
            "cmd": " ".join(cmd[:3]) + f' "{question}" --scope {scope} --max-turns {max_turns}',
        }
    except subprocess.TimeoutExpired:
        return {
            "ok": False, "error": "timeout",
            "elapsed_s": timeout,
            "cmd": " ".join(cmd[:3]) + f' "{question}"',
        }


def load_benchmark(path: Path) -> list[dict]:
    items = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        items.append(json.loads(line))
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run_id", help="run timestamp e.g. 20260503T013441Z")
    ap.add_argument("--surface", choices=["search", "report", "both"], default="search")
    ap.add_argument("--report-ids", default="", help="comma-separated Q-IDs to run report on")
    ap.add_argument("--limit", type=int, default=0, help="limit total items")
    ap.add_argument("--k", type=int, default=10)
    ap.add_argument("--max-turns", type=int, default=4)
    args = ap.parse_args()

    run_dir = RUNS_DIR / args.run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    bench_path = EVAL_DIR / "benchmark.jsonl"
    if not bench_path.exists():
        print(f"benchmark not found at {bench_path}", file=sys.stderr)
        sys.exit(1)

    items = load_benchmark(bench_path)
    if args.limit:
        items = items[: args.limit]

    out_path = run_dir / "answers.jsonl"
    report_ids = set(s.strip() for s in args.report_ids.split(",") if s.strip())

    n = len(items)
    print(f"running {args.surface} on {n} items, output -> {out_path}", file=sys.stderr)

    with open(out_path, "a") as f:
        for i, item in enumerate(items, 1):
            qid = item["id"]
            q = item["question"]
            print(f"[{i}/{n}] {qid} ({item.get('dimension','?')}/{item.get('difficulty','?')}) {q[:80]!r}", file=sys.stderr)

            row = {"id": qid, "question": q, "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}

            if args.surface in ("search", "both"):
                row["search"] = run_search(q, k=args.k)

            if args.surface in ("report", "both") and (not report_ids or qid in report_ids):
                row["report"] = run_report(q, max_turns=args.max_turns)

            f.write(json.dumps(row) + "\n")
            f.flush()

    print(f"done. wrote {n} rows to {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
