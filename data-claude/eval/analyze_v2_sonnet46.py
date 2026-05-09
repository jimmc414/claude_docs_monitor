"""Compute decision.md inputs for the v4.3.11 V2-on-Sonnet-4.6 experiment.

Reads scores.jsonl from each trial dir + reports.jsonl, prints:
  - per-Q × 3-trial verdict matrix (V2-Sonnet4.6 vs V2-Sonnet4 vs baselines)
  - strict-correct counts
  - Q027 c1921 in initial_evidence rate (for V2 deterministic, equals final_evidence)
  - per-trial lenient counts

Run from repo root:
    python data-claude/eval/analyze_v2_sonnet46.py 20260507-v2-on-sonnet46
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
RUNS = REPO / "data-claude" / "eval" / "runs"

SUBSET = ["Q005", "Q010", "Q012", "Q021", "Q027", "Q032", "Q036", "Q049", "Q050"]


def load_trial(run_id: str) -> dict[str, dict]:
    """Return {qid: {verdict, c1921_in_evidence, ev_count}}."""
    out: dict[str, dict] = {}
    sp = RUNS / run_id / "scores.jsonl"
    rp = RUNS / run_id / "reports.jsonl"
    scores: dict[str, str] = {}
    if sp.exists():
        for line in sp.read_text().splitlines():
            if not line.strip(): continue
            d = json.loads(line)
            scores[d["id"]] = d.get("correctness", {}).get("correctness", "?")
    rep_data: dict[str, dict] = {}
    if rp.exists():
        for line in rp.read_text().splitlines():
            if not line.strip(): continue
            d = json.loads(line)
            rep_data[d["id"]] = d.get("report", {}).get("report_json_data") or {}
    for qid in SUBSET:
        rj = rep_data.get(qid, {})
        ev = rj.get("evidence", []) or []
        chunk_ids = [e.get("chunk_id") for e in ev]
        out[qid] = {
            "verdict": scores.get(qid, "?"),
            "c1921_in_evidence": 1921 in chunk_ids,
            "ev_count": len(ev),
        }
    return out


def main():
    if len(sys.argv) < 2:
        print("Usage: analyze_v2_sonnet46.py <base-run-id> [num-trials]")
        sys.exit(1)
    base = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 3

    new = [load_trial(f"{base}-trial{i+1}") for i in range(n)]

    # v4.3.11 V2 anchor
    v2_s4 = [load_trial(f"20260507-rag-v4.3.11-detn-trial{i+1}") for i in range(3)]

    # baseline study facts (n=1 each, Sonnet 4.6, from baselines/comparison.md)
    baseline_strict = {
        "ripgrep": {"Q005", "Q027"},  # the 2 strict correct
        "bm25":    {"Q010", "Q027"},
    }
    baseline_q027 = {"ripgrep": "correct", "bm25": "correct"}

    # ── Per-Q matrix ────────────────────────────────────────────────────────
    print("=" * 90)
    print(f"V2-Sonnet4.6 ({base}) vs V2-Sonnet4 (v4.3.11) vs baselines (Sonnet4.6, n=1)")
    print("=" * 90)
    print(f"{'QID':<6} {'New T1':<14} {'New T2':<14} {'New T3':<14} {'V2-S4 Ts':<24} "
          f"{'rg':<6} {'bm':<6} ")
    for qid in SUBSET:
        n_v = [t[qid]["verdict"][:14] for t in new]
        v_old = "/".join(t[qid]["verdict"][:4] for t in v2_s4)
        rg = "C" if qid in baseline_strict["ripgrep"] else "P/I"
        bm = "C" if qid in baseline_strict["bm25"] else "P/I"
        print(f"{qid:<6} {n_v[0]:<14} {n_v[1]:<14} {n_v[2]:<14} {v_old:<24} {rg:<6} {bm:<6}")

    # ── Strict counts ───────────────────────────────────────────────────────
    print()
    new_strict = sum(
        1 for qid in SUBSET if all(new[i][qid]["verdict"] == "correct" for i in range(n))
    )
    v2_s4_strict = sum(
        1 for qid in SUBSET if all(v2_s4[i][qid]["verdict"] == "correct" for i in range(3))
    )
    print(f"V2-Sonnet4.6 strict-correct (3/3 correct): {new_strict}/9")
    print(f"V2-Sonnet4   strict-correct (3/3 correct): {v2_s4_strict}/9")
    print(f"ripgrep      strict-correct (n=1):         2/9")
    print(f"bm25         strict-correct (n=1):         2/9")

    # ── Lenient counts per trial ────────────────────────────────────────────
    print()
    print("Lenient (correct or partially_correct) per trial:")
    for i in range(n):
        lc = sum(1 for qid in SUBSET if new[i][qid]["verdict"] in ("correct", "partially_correct"))
        cor = sum(1 for qid in SUBSET if new[i][qid]["verdict"] == "correct")
        print(f"  V2-Sonnet4.6 T{i+1}: {cor} correct, {lc} correct+partial")

    # ── Q027 deep dive ──────────────────────────────────────────────────────
    print()
    print("=" * 90)
    print("Q027 deep-dive (the diagnostic question)")
    print("=" * 90)
    new_q027_verdicts = [t["Q027"]["verdict"] for t in new]
    new_q027_c1921 = [t["Q027"]["c1921_in_evidence"] for t in new]
    v2_s4_q027_verdicts = [t["Q027"]["verdict"] for t in v2_s4]
    v2_s4_q027_c1921 = [t["Q027"]["c1921_in_evidence"] for t in v2_s4]

    print(f"V2-Sonnet4.6 Q027 verdicts:        {new_q027_verdicts}")
    print(f"V2-Sonnet4.6 Q027 c1921 in evidence: {new_q027_c1921}")
    print(f"  → c1921-in-initial_evidence rate: {sum(new_q027_c1921)}/3 = {sum(new_q027_c1921)/3:.0%}")
    print()
    print(f"V2-Sonnet4   Q027 verdicts:        {v2_s4_q027_verdicts}")
    print(f"V2-Sonnet4   Q027 c1921 in evidence: {v2_s4_q027_c1921}")
    print(f"  → c1921-in-initial_evidence rate: {sum(v2_s4_q027_c1921)}/3 = {sum(v2_s4_q027_c1921)/3:.0%}")
    print()
    print(f"Baselines Q027: ripgrep={baseline_q027['ripgrep']}, bm25={baseline_q027['bm25']}")

    # ── Phase D verdict per rubric ──────────────────────────────────────────
    print()
    print("=" * 90)
    print("Phase D verdict per the plan's rubric:")
    print("  5+ → architecture earns its complexity (build out 25Q + monitor)")
    print("  4   → boundary; look at WHICH questions earn the strict")
    print("  2-3 → architecture ties baselines (consider BM25 pivot)")
    print("  0-1 → architecture loses to baselines (hard pivot)")
    print("=" * 90)
    if new_strict >= 5:
        print(f"VERDICT: {new_strict}/9 → architecture EARNS its complexity")
    elif new_strict == 4:
        print(f"VERDICT: 4/9 → BOUNDARY — examine which questions are correct")
    elif 2 <= new_strict <= 3:
        print(f"VERDICT: {new_strict}/9 → architecture TIES baselines (pivot candidate)")
    else:
        print(f"VERDICT: {new_strict}/9 → architecture LOSES to baselines (hard pivot)")


if __name__ == "__main__":
    main()
