"""Run reports on the hard subset, write to reports.jsonl (separate from search answers).

When --trials N (N>1) is passed, run the full SUBSET N times sequentially under
run_ids `{base}-trial1` ... `{base}-trialN`. Trials run sequentially because
data-claude/reports/ is shared and the newest-mtime pickup window (~5s) would
race across parallel runners.
"""
import argparse
import json
import os
import shlex
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
EVAL_DIR = REPO / "data-claude" / "eval"

# Load .env if present (no python-dotenv dep). Lets VOYAGE_API_KEY reach subprocess.
_env_file = REPO / ".env"
if _env_file.exists():
    for _line in _env_file.read_text().splitlines():
        _line = _line.strip()
        if not _line or _line.startswith("#") or "=" not in _line:
            continue
        _k, _, _v = _line.partition("=")
        os.environ.setdefault(_k.strip(), _v.strip().strip('"').strip("'"))

sys.path.insert(0, str(REPO))
from llm_backend import _is_rate_limit  # noqa: E402

ENV = {**os.environ}
ENV.pop("ANTHROPIC_API_KEY", None)

DELAY_S = int(os.environ.get("REPORT_DELAY_S", "60"))
NO_CRITIQUE = os.environ.get("REPORT_NO_CRITIQUE", "0") == "1"

# Selected hard subset across dimensions
SUBSET = ["Q005", "Q010", "Q012", "Q021", "Q027", "Q032", "Q036", "Q049", "Q050"]


def _run_one_trial(run_id: str, items: dict) -> None:
    """Run the full SUBSET under a single run_id, append to reports.jsonl."""
    run_dir = EVAL_DIR / "runs" / run_id
    out_path = run_dir / "reports.jsonl"

    n = len(SUBSET)
    stderr_dir = run_dir / "stderr"
    stderr_dir.mkdir(parents=True, exist_ok=True)
    print(f"running report on {n} questions, output -> {out_path}", file=sys.stderr)

    with open(out_path, "a") as f:
        for i, qid in enumerate(SUBSET, 1):
            if qid not in items:
                print(f"[{i}/{n}] {qid}: NOT IN BENCHMARK", file=sys.stderr); continue
            q = items[qid]["question"]
            print(f"[{i}/{n}] {qid} ({items[qid]['dimension']}) {q[:80]!r}", file=sys.stderr)

            cmd = [
                "python", str(REPO / "claude_docs_monitor.py"), "report", q,
                "--scope", "docs", "--max-turns", "4",
                "--model", "sonnet",
            ]
            if NO_CRITIQUE:
                cmd.append("--no-self-critique")
            t0 = time.time()
            try:
                r = subprocess.run(cmd, capture_output=True, text=True, env=ENV, cwd=str(REPO), timeout=1800)
                elapsed = time.time() - t0
                (stderr_dir / f"{qid}.txt").write_text(r.stderr or "")
                (stderr_dir / f"{qid}.stdout.txt").write_text(r.stdout or "")
                # find newest md/json in reports dir
                reports_dir = REPO / "data-claude" / "reports"
                md = sorted(reports_dir.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
                jsf = sorted(reports_dir.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
                md_p = md[0] if md and md[0].stat().st_mtime > t0 - 5 else None
                jp = jsf[0] if jsf and jsf[0].stat().st_mtime > t0 - 5 else None
                row = {
                    "id": qid,
                    "question": q,
                    "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                    "report": {
                        "ok": r.returncode == 0,
                        "exit_code": r.returncode,
                        "elapsed_s": round(elapsed, 1),
                        "rate_limited": _is_rate_limit(r.stderr) if r.returncode else False,
                        "report_md_path": str(md_p) if md_p else None,
                        "report_json_path": str(jp) if jp else None,
                        "report_md_text": md_p.read_text() if md_p else None,
                        "report_json_data": json.loads(jp.read_text()) if jp else None,
                        "stderr_tail": r.stderr[-4000:] if r.returncode else None,
                        "stderr_path": str(stderr_dir / f"{qid}.txt"),
                        "stdout_tail": r.stdout[-300:],
                        "cmd": shlex.join(cmd),
                    },
                }
            except subprocess.TimeoutExpired:
                row = {"id": qid, "question": q, "report": {"ok": False, "error": "timeout", "elapsed_s": 900}}
            f.write(json.dumps(row) + "\n"); f.flush()
            print(f"  -> ok={row['report'].get('ok')} elapsed={row['report'].get('elapsed_s','?')}s", file=sys.stderr)
            if i < n and DELAY_S > 0:
                print(f"  ... sleeping {DELAY_S}s before next", file=sys.stderr)
                time.sleep(DELAY_S)

    print(f"\ndone. wrote {out_path}", file=sys.stderr)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "run_id",
        nargs="?",
        default="20260503T013441Z",
        help="Base run_id. With --trials >1, becomes prefix and each trial appends -trialN.",
    )
    parser.add_argument(
        "--trials",
        type=int,
        default=1,
        help="Number of trial repetitions of the full SUBSET (default 1 = original behavior).",
    )
    args = parser.parse_args()

    if args.trials < 1:
        parser.error("--trials must be >= 1")

    # Load benchmark once
    items = {}
    for line in (EVAL_DIR / "benchmark.jsonl").read_text().splitlines():
        if line.strip():
            it = json.loads(line)
            items[it["id"]] = it

    if args.trials == 1:
        _run_one_trial(args.run_id, items)
    else:
        for t in range(1, args.trials + 1):
            trial_run_id = f"{args.run_id}-trial{t}"
            print(f"\n=== TRIAL {t}/{args.trials}: {trial_run_id} ===", file=sys.stderr)
            _run_one_trial(trial_run_id, items)


if __name__ == "__main__":
    main()
