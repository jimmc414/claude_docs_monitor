# v4.3.10 — Branch decision

**Status:** Complete. All four experiments finished.

**Date:** 2026-05-05 (E1/E2/E4 complete) → 2026-05-06 (E3 complete)

---

## What we know now

### E1 — Reconstruction, decisive

`c1921 in initial_evidence top-30 = TRUE.`

Pool of 20 (well below the 30-item slice). c1921 was at **position 1**, with the
maximum rerank confidence (10.0 of 10). Its `relevance_to` was SQ4 ("Are there
different default model tiers or upgrade paths…") — the broadest sub-question.

**Mechanism:** the **agent loop's curation** dropped c1921. The aggregation in
`_initial_retrieve` did its job: it ranked the right chunk first.

This rules out "cross-sub-query aggregation" as the Q027 mechanism. **A2 (force-
include top-K per sub-query) would not help** — c1921 already topped the pool.

### E2 — BM25 vs dense divergence on Q049, narrowed

| Sub-query | BM25 v37 hits | BM25 v39 hits | BM25 Jaccard | Dense Jaccard |
|---|---|---|---|---|
| SQ0 | 2 | 10 | 0.20 | 0.67 |
| SQ1 | 0 | 0 | 0.00 | 0.25 |
| SQ2 | 0 | 0 | 0.00 | 0.25 |
| SQ3 | 0 | 0 | 0.00 | 0.05 |
| SQ4 | 3 | 4 | 0.75 | 0.25 |
| SQ5 | 4 | 0 | 0.00 | 0.18 |
| SQ6 | 0 | 0 | 0.00 | 0.82 |
| **avg** | — | — | **0.14** | **0.35** |

Two findings, neither matching the plan's framing:

1. **BM25 returns no hits in 4/7 sub-queries** (SQ1/2/3/6) and nearly empty
   in SQ0 v37. The FTS5 query has no exact-token match for these multi-token
   phrases. So Q049 is structurally a **dense-only retrieval** for those
   sub-queries; the "BM25 surface-form sensitivity" hypothesis is misframed —
   surface-form matters but only when BM25 returns *anything*.
2. **Dense overlap is highly variable per sub-query** (0.05–0.82). SQ3
   especially is brittle: 0.05 Jaccard, 1 chunk in common. SQ6 is robust:
   0.82 Jaccard, 9 chunks in common. The variance is **per-sub-query intent
   stability**, not a systematic property of dense embeddings.

**Implication:** the v4.3.9 → v4.3.7 ~50% pool divergence on Q049 is
**downstream of dense retrieval on per-sub-query phrasing**, with BM25
contributing essentially nothing for most sub-queries. The leverage points
suggested by the plan (RRF rebalancing, query-expansion/HyDE) might help SQ3-
class brittleness, but the bigger lever is **planner phrasing stability** for
Q049 — same intent, very different per-sub embeddings.

### E4 — Aggregation logic, unchanged recommendation

Recommendation: **don't touch `_initial_retrieve`.** Reasons documented in
`E4_aggregation_critique.md`:

- E1 confirms the function ranked the right chunk first.
- E2 shows pool sizes are structurally small (often < 30 deduped), so the
  global-sort-vs-rank-preserving debate doesn't move outcomes here.
- The leverage that *is* directly motivated by E1 is on the **agent
  presentation layer** (REASON_PROMPT formatting): currently the agent sees
  `<chunk_id>: <heading>` with no confidence score, no relevance_to, no
  source_type. c1921 was scored 10/10 and the agent had no signal to know it.

### E3 — Q027 reproducibly incorrect 3/3

Both trials completed cleanly. Wall: 23:53 UTC May 5 → 06:23 UTC May 6 (~6.5h).

**Q027: incorrect 3/3** — same canonical points missed (April 23, 2026 default
change to Opus 4.7; previous Sonnet 4.6; ANTHROPIC_MODEL override). Same failure
mode in all three runs: agent concludes "no April 23 event in evidence" rather
than acknowledging retrieval gap.

**6 of 9 questions are 3/3 stable.** 3 oscillate:

- Q010: correct → correct → **hallucinated** (trial3 invented `:*` syntax)
- Q049: correct → partial → partial (v4.3.9's correct was the lucky draw)
- Q050: partial → partial → correct (mirror noise)

**Trial-level totals:** v4.3.9 had 3 correct; trials 2/3 had 2 each.
The "correct count" has ±1 noise envelope; v4.3.9 was at the top end.

Full data: `E3_3trial_matrix.md`.

---

## Decision tree, resolved

From the plan:

| E1 outcome | E3 Q027 stability | Implication | Next code-touch |
|---|---|---|---|
| ✅ **c1921 in top-30 (agent curation)** | ✅ **3/3 incorrect** | Agent prompt is the leverage point; A2 wouldn't help | Surface conf+relevance_to in REASON_PROMPT, *or* replace curation with deterministic top-N |

Both axes resolved cleanly. The recommendation is concrete.

---

## Recommended next code-touch

**Smallest-blast-radius fix: surface confidence + relevance_to in the agent prompt.**

Edit `report_builder.py:452-454`:

```python
initial_evidence="\n".join(
    f"  c{e.chunk_id} [conf={e.confidence:.1f} from='{(e.relevance_to or '')[:60]}'] {e.heading_path[:80]}"
    for e in initial_evidence[:30]
),
```

And add a paragraph to REASON_PROMPT (after line 393) that explains the new
fields:

> Each chunk row shows `conf=N.N` (the rerank model's 0–10 relevance score for
> the sub-question that retrieved it) and `from='...'` (which sub-question it
> answers). Be slow to drop chunks scoring 8+ — they passed BM25, dense, and
> rerank gates. If you drop a high-confidence chunk, do it because get_chunk
> showed the content didn't actually answer its sub-question, not because the
> heading looked off-topic.

This is ~8 lines of code change. No aggregation logic change. No new flags.
Risk: agent over-anchors on confidence and keeps low-quality high-conf chunks.
That's tunable; the current under-anchoring is structural.

**Eval impact prediction:** Q027 should flip from 3/3 incorrect to at least
1/3 correct. If it doesn't, the next escalation is to **replace agent
curation with deterministic top-N** — use line 514's fallback as the default,
let the agent only **append** new gap-filled chunks instead of rewriting the
list.

**What NOT to ship:**

- A (filter-fallback ladder): no evidence it's needed. SQ4 (which retrieved
  c1921 #1) didn't have date filters; SQ0–SQ2 did but their results are
  irrelevant since c1921 was already in the pool.
- A2 (force-include top-K per sub-query): E1 confirmed c1921 was already #1.
  This change wouldn't move anything.
- T2 rollback: established correct in isolation; not implicated by E1 or E3.
- Any aggregation-logic change: E1 + E2 + E4 all converge on "aggregation is
  not the bottleneck."

**Eval-methodology note:**

Q049, Q050, Q010 each oscillate 1/3 across replays. The 9-Q subset has ±1
noise on `correct_count`. Future eval comparisons should either average
across 3 trials before declaring a delta, or restrict to the 6 stable
questions for single-trial signal.

---

## What this run did NOT do (per plan)

- No edits to `report_builder.py`
- No A (filter-fallback ladder) implementation
- No A2 (force-include top-K per sub-query) implementation
- No T2 rollback
- No 4th-config experiment
- No SYNTH_PROMPT or ENUMERATION changes

End state: five artifacts in `data-claude/eval/runs/20260506-rag-v4.3.10/`:

- `E1_reconstruction.txt` — Q027 top-30 dump, with c1921 verdict
- `E2_q049_bm25_vs_dense.txt` — per-sub-query Jaccard overlaps
- `E3_3trial_matrix.md` — 3-trial × 9-Q correctness matrix
- `E4_aggregation_critique.md` — design critique
- `branch_decision.md` — this file

Plus E3 trial output in:

- `data-claude/eval/runs/20260506-rag-v4.3.10-trial2/` (reports.jsonl + scores.jsonl)
- `data-claude/eval/runs/20260506-rag-v4.3.10-trial3/` (reports.jsonl + scores.jsonl)

---

## Open follow-up questions

These are surfaced by the experiments but not in scope for this run:

1. **Q049's SQ3 has 0.05 dense Jaccard** between v4.3.7 and v4.3.9. Why is
   that one sub-query so brittle while SQ6 (0.82) is robust? Not a Q027
   question, but worth noting if dense brittleness is a recurring pattern.
2. **BM25 returns 0 for sub-queries with 6+ tokens**. FTS5 isn't doing
   stemming/synonym expansion. Worth checking if the planner's verbosity
   actively hurts BM25.
3. **The agent saw c1921 in v4.3.9 and dropped it.** What text did the agent
   produce around that decision? `stdout_tail` and `stderr_tail` should have
   reasoning traces. Out of scope for v4.3.10 but trivially recoverable.
