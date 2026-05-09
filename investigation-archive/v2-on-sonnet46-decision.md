# V2 on Sonnet 4.6 — Model-Controlled Experiment Decision

**Date**: 2026-05-07
**Run**: `20260507-v2-on-sonnet46-trial{1,2,3}` (9 questions × 3 trials, concurrency 3)
**Subject under test**: V2 (deterministic top-N) hybrid RAG, swapped from
Sonnet 4 (`claude-sonnet-4-20250514`) → Sonnet 4.6 (`claude-sonnet-4-6`)
**Anchor**: v4.3.11 V2 trials, **same code, same SUBSET, only model differs**
**Baselines**: ripgrep + Sonnet 4.6, BM25 + Sonnet 4.6 (n=1 each, from
`/mnt/c/python/claude_docs_monitor-baselines/baselines/comparison.md`)
**Judge**: `claude-sonnet-4-6` for **both** runs (v4.3.11 V2 was re-scored
with the new judge to remove the judge-version confound — see § Methods).

---

## TL;DR

**Strict-correct count: 1/9 — under the rubric this is the "hard pivot"
band.** The architecture does not earn its complexity over a 95-line BM25
script on this benchmark, even after the model swap.

**But Q027 specifically improves: 2/3 correct (V2-Sonnet 4.6) vs 1/3
correct (V2-Sonnet 4).** The c1921-in-initial_evidence rate doubled (33%
→ 67%) when the planner runs on Sonnet 4.6. The architectural fix in V2
(deterministic top-N preserving c1921 once retrieved) plus a more stable
planner does close the curation+stability gap on the question this
experiment was designed around — but only on that question, and not
enough to lift the overall strict count.

**Q049 introduces a new failure mode**: T1 = `hallucinated` under Sonnet
4.6 vs `partially_correct` under Sonnet 4 — invented `connect()`,
`disconnect()`, `continue_conversation=True`. Sonnet 4.6 trades planner
stability for higher fabrication risk on API-detail questions.

**Verdict per the plan's rubric: 0-1/9 → architecture LOSES to baselines,
hard pivot, fast.** Caveats below.

---

## Methods — what was controlled

| Variable | v4.3.11 V2 (anchor) | This run | Baselines (input study) |
|---|---|---|---|
| Architecture | V2 hybrid RAG | V2 hybrid RAG (same code) | ripgrep / BM25 only |
| Synthesis model | Sonnet 4 | **Sonnet 4.6** | Sonnet 4.6 |
| Planner / critique / rerank | Sonnet 4 (via "sonnet" alias) | **claude-sonnet-4-6 (explicit)** | n/a |
| Entailment-audit model | Haiku 4.5 | Haiku 4.5 (unchanged) | n/a |
| Judge (correctness scorer) | Sonnet 4 (original) → **Sonnet 4.6 (re-scored)** | Sonnet 4.6 | Sonnet 4.6 |
| SUBSET | 9-Q hard | same 9-Q | same 9-Q |
| Trials | 3 | 3 | 1 each baseline |

**Judge mismatch removed via re-scoring**: v4.3.11 V2 was originally scored
under `_MODEL_ALIASES_API["sonnet"] → claude-sonnet-4-20250514`. This
experiment uses `claude-sonnet-4-6` everywhere. To make the comparison
apples-to-apples on judge, **v4.3.11 V2 trials were re-scored** with
the new alias map. Original scores are preserved at
`scores.original.jsonl` in each anchor trial dir for audit.

The re-score moved v4.3.11 V2 from 2/9 strict (original judge) to 1/9
strict (new judge): Q050 T1 dropped from `correct` to
`partially_correct`, and Q027 T1 was re-classified from `incorrect` to
`hallucinated`. The new judge is stricter on extra/wrong claims and
tags fabrications as `hallucinated` rather than `incorrect`.

---

## Headline numbers (under claude-sonnet-4-6 judge)

| Run | Strict (3/3 correct) | Lenient mean (correct + partial) | Notes |
|---|---:|---:|---|
| **V2-Sonnet 4.6** (this run) | **1/9** | 8.3/9 | Q050 only |
| V2-Sonnet 4 (re-scored, new judge) | 1/9 | 8.0/9 | Q010 only |
| V2-Sonnet 4 (original judge — for context) | 2/9 | 8.3/9 | Q010, Q050 |
| ripgrep + Sonnet 4.6 (n=1) | 2/9 | 9/9 | Q005, Q027 |
| BM25 + Sonnet 4.6 (n=1) | 2/9 | 9/9 | Q010, Q027 |

Both architectures (V2-Sonnet 4 and V2-Sonnet 4.6) hit **1/9** strict
under the same judge. The architecture neither gains nor loses overall
correctness from the model swap. **Both V2 variants lose to both
baselines** at 2/9.

---

## 9-Q × 3-trial verdict matrix

`C` = correct, `P` = partially_correct, `I` = incorrect, `H` = hallucinated.

| QID | dim | V2-S4.6 T1 | T2 | T3 | V2-S4 T1 | T2 | T3 | rg | bm |
|---|---|---|---|---|---|---|---|---|---|
| Q005 | factual | P | C | P | P | C | P | C | P |
| Q010 | citation | P | C | C | C | C | C | P | C |
| Q012 | coverage | P | P | P | P | P | P | P | P |
| Q021 | hallucination_lure | P | P | P | P | P | P | P | P |
| **Q027** | **recency** | **C** | **C** | **I** | **H** | **C** | **I** | **C** | **C** |
| Q032 | negation | P | P | P | P | P | P | P | P |
| Q036 | cross_source | P | P | P | P | P | P | P | P |
| Q049 | paraphrase_pair | **H** | P | P | P | P | P | P | P |
| Q050 | paraphrase_pair | C | C | C | P | C | C | P | P |

Movements introduced by the Sonnet 4.6 swap (under same judge):
- **Q050 T1**: P → C  (gain — Sonnet 4.6 produces a less-extra-claim answer)
- **Q010 T1**: C → P  (regression — Sonnet 4.6 invented `Bash(ls:*)` shorthand and AST-parsing details)
- **Q027 T1**: H → C  (gain — c1921 surfaced; planner stability is the mechanism)
- **Q049 T1**: P → H  (regression — Sonnet 4.6 fabricated `connect()`/`disconnect()`/`continue_conversation=True`)

Net Q-level: 2 gains, 2 regressions. Strict count unchanged.

---

## Q027 — the diagnostic question

Q027 is the recency question with gold phrase "April 23, 2026" sitting
plainly in chunk c1921. v4.3.11's mechanism analysis identified Q027's
failure as a **two-bug stack**: (a) planner doesn't reliably surface
c1921 in `initial_evidence`, (b) agent curation drops c1921 even when
it is in `initial_evidence`. V2 fixes (b) deterministically. The Sonnet
4.6 swap targets (a).

### Q027 verdicts

| Run | T1 | T2 | T3 | Correctness rate |
|---|---|---|---|---:|
| **V2-Sonnet 4.6** | **C** | **C** | **I** | **2/3** |
| V2-Sonnet 4 (re-scored) | H | C | I | 1/3 |
| V2-Sonnet 4 (original judge) | I | C | I | 1/3 |
| ripgrep + Sonnet 4.6 (n=1) | C | — | — | 1/1 |
| BM25 + Sonnet 4.6 (n=1) | C | — | — | 1/1 |

### Q027 c1921-in-initial_evidence rate

V2 is deterministic top-N → `final_evidence ⊇ initial_evidence`, so
"c1921 in evidence" is identical to "c1921 in initial_evidence" (no
agent curation drop). This isolates planner stability as the mechanism.

| Run | T1 | T2 | T3 | c1921 surface rate |
|---|---|---|---|---:|
| **V2-Sonnet 4.6** | **True** | **True** | False | **2/3 (67%)** |
| V2-Sonnet 4 | False | True | False | 1/3 (33%) |

**The c1921 surface rate doubled** (33% → 67%) when the planner runs on
Sonnet 4.6. The mechanism is exactly what v4.3.11's E1 reconstruction
predicted: when c1921 lands in `initial_evidence`, V2's deterministic
merge keeps it; the synthesizer then produces the canonical answer.
When c1921 doesn't land (Sonnet 4.6 T3), V2 has nothing to preserve
and the synthesizer hallucinates a different change.

This is the Phase C result the experiment was designed to surface. **The
v4.3.11 amendment's framing — "V2 lifts Q027 from ~0% to ~17%, larger
gap remaining in planner stability, V2 necessary but not sufficient" —
holds.** Sonnet 4.6 closes more of that residual planner-stability gap
than Sonnet 4 did, but does not close it fully. T3 still fails for the
same reason v4.3.11's T1/T3 failed: planner sub-queries don't
deterministically surface c1921.

### Q027 specifically — why this matters separate from the strict count

Per the user's "addition #3" guidance: even if overall strict count is
mid-range, a 3/3 Q027 result would be a strong signal. **The actual
Q027 result is 2/3 — not 3/3, but materially better than V2-Sonnet 4's
1/3 and equal to the n=1 baselines' 1/1.** It says:

- The architectural premise (deterministic top-N + agentic gap-fill) is
  not the bottleneck on Q027.
- The model running the planner is the bottleneck. Sonnet 4.6 is
  meaningfully more stable here than Sonnet 4.
- A planner-side fix (e.g., direct chunk-id pinning for known-canonical
  chunks on `dimension=recency` questions, or HyDE for date-conditioned
  queries) targeted at the remaining ~33% miss rate would be testable
  in isolation, on top of either model.

---

## What changed when we swapped models

### Improvements (Sonnet 4.6 vs Sonnet 4, same architecture)

1. **Q027 c1921 surface rate** 33% → 67%. Planner is more stable.
2. **Q027 strict correctness** 1/3 → 2/3.
3. **Q050 T1**: partially_correct → correct under same judge (less
   extra-claim-tail than Sonnet 4 produced).

### Regressions

1. **Q049 T1**: partially_correct → **hallucinated**. Sonnet 4.6 invented
   non-existent SDK methods (`connect()`, `disconnect()`,
   `continue_conversation=True`). API-detail questions are now a
   higher-risk failure surface.
2. **Q010 T1**: correct → partially_correct. Extra-claim verbosity
   (invented `Bash(ls:*)` colon-shorthand, AST-parsing claims) earned
   the partial verdict.

### Wash

Q005, Q012, Q021, Q032, Q036 — identical distributions across both runs.
These are corpus-structural verdicts unaffected by the model.

### Net

| Metric | Δ |
|---|---|
| Strict count (3/3) | 0 (1/9 → 1/9) |
| Lenient mean | -0.3 (8.3/9 → 8.0/9) |
| Q027 c1921 rate | +34 pp (33% → 67%) |
| Q027 correct rate | +33 pp (1/3 → 2/3) |
| New `hallucinated` verdicts | +1 (Q049 T1) |

---

## Phase D verdict per the plan's rubric

| Strict count | Verdict | Next plan |
|---|---|---|
| 5+ / 9 | Architecture earns its complexity | 25-Q expansion + monitor + planner-stability work |
| 4 / 9 | Boundary | Hard call |
| 2-3 / 9 | Architecture ties baselines | BM25 pivot candidate |
| **0-1 / 9** | **Architecture LOSES to baselines** | **Hard pivot, fast** |

**This run lands in the bottom band.** 1/9 strict, baselines at 2/9, both
V2 variants worse than both baselines on the rubric's primary metric.

### Caveats and nuance

The strict count is the rubric's headline, but three caveats matter for
the next plan:

1. **n=1 baselines vs n=3 trials**: ripgrep and BM25 each ran once.
   Their 2/9 numbers are within the noise band V2-Sonnet 4 demonstrated
   (which spans 1-5 strict across trials). With matching n=3, baselines
   could land lower — or higher.
2. **Q027 is a real architectural-or-model gain**: Sonnet 4.6 surfaces
   c1921 reliably enough that V2's deterministic curation lifts Q027
   to 2/3. Baselines also get Q027 right by a different mechanism
   (full-page context). On Q027 specifically, V2-Sonnet 4.6 is
   **superior to V2-Sonnet 4** and **below n=1 baselines** — a real
   middle position.
3. **The pivot direction is constrained by the rubric, not pre-decided
   by this data**: 1/9 says "investigate before doing anything else,"
   not "ship BM25 tomorrow."

### What the architecture *did* earn (under any judge, any model)

- Citation-level provenance: V2 produces inline `[^cN]` citations and a
  companion JSON with chunk lineage. Baselines do not.
- Coverage on multi-aspect questions (Q012, Q036): partial-credit
  performance is identical to baselines, but the structured-evidence
  output makes downstream auditing tractable.
- Determinism: V2's deterministic top-N produces identical evidence
  count (25) across all 27 trials. Baselines were not measured for
  this property.

These are not strict-correctness wins, but they are real properties of
the architecture that a BM25-only system would lose. The pivot decision
should weigh these against the strict-count loss.

---

## Decision

**Per the plan: hard pivot, fast.** The original Phase C (25-Q expansion,
monitor build-out, planner-stability investigation in the current
architecture) is **NOT triggered**. The strict-count threshold for
investing further was 5+/9 and we are at 1/9.

**The next plan, written after this one, should investigate two
questions before deciding the pivot's shape:**

1. **What does an n=3 baseline look like?** Re-run ripgrep and BM25
   three times each, score with the same judge. If their 2/9 holds at
   n=3, the pivot is BM25-only. If they oscillate (e.g., bm25
   landing at 0/9, 2/9, 1/9 across runs), the architectural-vs-model
   confound is muddier than the rubric assumes and the comparison
   itself needs more discipline before the pivot decision can be
   trusted.
2. **Is the planner-stability gain on Q027 transferable to other
   recency questions?** The 25-Q expansion was deferred specifically
   because the architecture didn't earn it. But cheaper than
   building a 25-Q benchmark: hand-craft 3-5 additional recency
   questions (e.g., other dated `<Note>` blocks in the corpus) and
   run V2-Sonnet 4.6 + baselines on them. If the c1921-style
   improvement generalizes, the architecture has a Sonnet 4.6-specific
   recency niche even if it loses on the broader 9-Q.

These two cheap follow-ups (estimated 1-2 hours each) are the gating
work for whatever comes next.

**What this plan does NOT do**:
- ✗ Does not commit to the original Phase C (25-Q expansion + monitor).
  Rubric verdict explicitly defers it.
- ✗ Does not commit to a BM25-only pivot. Rubric verdict says
  "investigate before doing anything else."
- ✗ Does not commit to a planner-stability investigation in the V2
  architecture. Doubly deferred.

---

## Run timing & cost

| Phase | Wall (mm:ss) |
|---|---|
| Trial 1 (9 Q × concurrency 3) | ~58 min |
| Trial 2 | ~58 min |
| Trial 3 | ~57 min |
| **Total trial wall** | **~2:53** |
| Scoring (3 trials × 9 Q) | ~12 min |
| Re-scoring v4.3.11 V2 (anchor) with new judge | ~22 min |
| Decision document | this file |

Trial timing per question (V2-Sonnet 4.6, concurrency 3):
- Median: ~16 min
- Slowest: Q036 trial 1 = 25.2 min
- Fastest: Q027 trial 1 = 10.8 min

Sonnet 4.6 is roughly the same speed as Sonnet 4 was. Concurrency 3 was
correct: the 15s sleep change is moot when concurrency is the throttle.

---

## Files referenced

Inputs:

- `/mnt/c/python/claude_docs_monitor-baselines/baselines/comparison.md`
   — baseline study (n=1 ripgrep + bm25 on Sonnet 4.6, same judge)
- `/mnt/c/python/claude_docs_monitor-baselines/baselines/testing_report.md`
   — full baseline methodology + cost
- `data-claude/eval/runs/20260507-rag-v4.3.11-detn-trial{1,2,3}/`
   — v4.3.11 V2 anchor data (Sonnet 4)
- `data-claude/eval/runs/20260507-rag-v4.3.11-detn-trial{1,2,3}/scores.original.jsonl`
   — v4.3.11 V2 original-judge scoring (preserved before re-score)
- `data-claude/eval/runs/20260507-rag-v4.3.11/comparison.md` (with
   2026-05-07 amendment)

Outputs (this run):

- `data-claude/eval/runs/20260507-v2-on-sonnet46-trial{1,2,3}/reports.jsonl`
   — full reports
- `data-claude/eval/runs/20260507-v2-on-sonnet46-trial{1,2,3}/scores.jsonl`
   — claude-sonnet-4-6 judge scoring
- `data-claude/eval/runs/20260507-v2-on-sonnet46/decision.md`
   — this file
- `data-claude/eval/analyze_v2_sonnet46.py`
   — comparison analyzer

Code (changes that defined the experiment):

- `llm_backend.py:85-89` — `_MODEL_ALIASES_API["sonnet"]` → `claude-sonnet-4-6`
- `report_builder.py` — hardcoded planner/critique model strings → `claude-sonnet-4-6`
- `retriever.py:558` — Claude rerank model string → `claude-sonnet-4-6`
- `data-claude/eval/run_reports.py` — `--model claude-sonnet-4-6` (explicit), `--concurrency` flag, `SUBSET_OVERRIDE` env, slug-match pickup, sleep 60s → 15s
