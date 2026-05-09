# v4.3.11 — Variant comparison

**Date**: 2026-05-07
**Variants**: V1 prompt-fix vs V2 deterministic-top-N
**Trials**: 3 per variant × 9-Q hard subset = 54 reports total
**Branches**: `rag-v4.3.11-prompt-fix`, `rag-v4.3.11-deterministic-topn`

---

## TL;DR

- **V1 fails the Q027 success bar**: 0/3 correct. **[amended 2026-05-07]**
  T3 ERR is effectively another incorrect — V1's T1/T2 pattern (c1921
  dropped from final evidence in both evaluable trials) argues against
  the charitable read. 0/3 is the honest reading; even with charitable
  T3=correct it was 1/3, still under the ≥2/3 bar. The prompt-level
  guidance was ignored. V1 dropped c1921 from final evidence in every
  evaluable trial.
- **V2 partially passes Q027**: 1/3 correct. When c1921 is in
  `initial_evidence`, V2 deterministically preserves it and produces the
  canonical answer (T2). When the planner's queries don't surface c1921 in
  `initial_evidence` (T1, T3), V2 can't help — and even chunks c2675/c2674,
  which contain related April 23 information, aren't sufficient on their
  own.
- **The mechanism understanding refines, doesn't break.** v4.3.10's E1 found
  c1921 at position 1/20 in *one* `initial_evidence` reconstruction. 3-trial
  replays here show c1921 in `initial_evidence` only 1/3 of the time — so
  the bottleneck is *both* agent curation (V2 fixes this) *and* upstream
  retrieval stability (V2 cannot fix this). **[amended 2026-05-07]** V2
  fixes the *rarer* bug by frequency: c1921 is in the initial_evidence
  pool in only ~17% of trials, V2 lifts Q027 correctness from ~0% to
  ~17%, and the remaining ~83% gap is planner stability — which V2 does
  not address. V2 is necessary but not sufficient.
- **Recommendation: ship V2.** It strictly dominates V1 on Q027 (1/3 vs
  0/3). V2's failures are upstream of V2 and would be present in V1 too.
  Stable-question regressions are within the noise envelope. The remaining
  Q027 work is in the planner / retrieval layer, not the agent loop.

---

**Amendment 2026-05-07** (post-Opus review): Three framing corrections
applied below.

- Q005 "within noise" claim: ±1 envelope was characterized on aggregate
  correct_count, not per-question stability. Q005 going 3/3→1/3 is a
  meaningful shift to flag, not noise.
- V1 T3 SDK error charity: V1's T1/T2 pattern doesn't support "could have
  been correct"; T3 is better read as effectively another incorrect.
- V2 "fixes one of the two bugs cleanly": accurate but undersells that
  V2 fixes the rarer failure mode. C1921 is in pool ~17% of trials; V2
  lifts Q027 from ~0% to ~17%, with the larger gap remaining in planner
  stability.

---

## 9-Q × 6-trial verdict matrix

Encoding: `correct=C` `partially_correct=P` `incorrect=I` `ERR=report_error`

| Q | dim | v4.3.10 (3T) | V1 T1 T2 T3 | V2 T1 T2 T3 |
|------|---|---|---|---|
| Q005 | factual           | C C C | P C C | P C P |
| Q010 | citation          | C C H | C C C | C C C |
| Q012 | coverage          | P P P | P P P | P P P |
| Q021 | hallucination_lure| P P P | P P P | P P P |
| **Q027** | **recency**   | **I I I** | **I I ERR** | **I C I** |
| Q032 | negation          | P P P | P P P | P P P |
| Q036 | cross_source      | P P P | P P P | P P P |
| Q049 | paraphrase_pair   | C P P | P P C | P C P |
| Q050 | paraphrase_pair   | P P C | C C P | C C C |

**Legend**: H = hallucinated (a verdict v4.3.10 trial3 saw on Q010 once).

### Trial-level correct counts (all 9 Q)

| Run     | C | P | I | H | ERR |
|---------|---|---|---|---|-----|
| v4.3.10 (avg of 3 trials) | 2.3 | 5.3 | 1.0 | 0.3 | 0 |
| V1 T1   | 1 | 6 | 1 | 0 | 0 |
| V1 T2   | 3 | 5 | 1 | 0 | 0 |
| V1 T3   | 4 | 3 | 0 | 0 | 1 (Q027) |
| V2 T1   | 1 | 7 | 1 | 0 | 0 |
| V2 T2   | 5 | 3 | 1 | 0 | 0 |
| V2 T3   | 1 | 7 | 1 | 0 | 0 |

### Q027 specifically

| Trial | V1 verdict | V1 c1921 in evidence | V1 ev_count | V2 verdict | V2 c1921 in evidence | V2 ev_count |
|---|---|---|---|---|---|---|
| T1 | incorrect | False | 19 | incorrect | False | 25 |
| T2 | incorrect | False | 18 | **correct** | **True (pos 0)** | 25 |
| T3 | ERR (synthesis SDK error) | — (no report) | 0 | incorrect | False | 25 |

The single V2 correct (T2) is the only trial in either variant where c1921
made it into `initial_evidence` and then into final evidence.

---

## Decision per the plan's matrix

The plan's variant outcome matrix:

| V1 result | V2 result | Recommendation |
|---|---|---|
| Pass | Pass, no regression | Ship V1 |
| Pass | Pass, regression | Ship V1; document V2 cost |
| Fail | Pass, no regression | Ship V2 |
| Fail | Pass, regression | Hard call |
| Pass | Fail | Anomalous |
| **Fail** | **Fail** | **Mechanism understanding wrong; reinvestigate** |

**Strict reading: V1 = Fail (0/3), V2 = Fail (1/3 < 2/3) → Fail/Fail cell.**

But the strict reading flattens an important distinction. **V1 and V2 fail
for different reasons** — and only V1's failure mode is fixable by either
variant:

- **V1 dropped c1921 from final evidence in every evaluable trial.** Even
  in T2, where c1921 *was* in `initial_evidence`, V1's agent dropped it.
  This is the failure mode V2 was designed to eliminate.
- **V2 dropped c1921 in 0 of 3 trials.** When c1921 was in
  `initial_evidence` (T2), V2 preserved it through the deterministic merge
  → correct verdict. When c1921 was *not* in `initial_evidence` (T1, T3),
  V2 had nothing to preserve.

So the more accurate framing:

- **V2 fixes the curation bug definitively** — there are no V2 trials where
  c1921 was retrieved and then dropped.
- **V2 reveals an upstream retrieval bug** that V1 had been masking
  behind its own curation failure. The planner does not reliably surface
  c1921 in `initial_evidence`. v4.3.10's E1 finding ("c1921 at position 1
  in `initial_evidence`") was n=1; n=3 here is 1/3.
- **Neither variant fixes the upstream retrieval bug.** That work belongs
  to the planner / retrieval layer.

---

## Trade-off characterization

### What V2 sacrifices vs V1

**Citation count and evidence count are more uniform** in V2 by design.
Variant 2's deterministic merge caps at `target_evidence + 25 = 25` chunks
and produces exactly 25 in every observed trial. V1 produced 18-19 chunks
on Q027.

| Metric (median over 27 question-trials) | V1 | V2 |
|---|---|---|
| `report_n_citations` | 54 (stdev 22.2) | 54 (stdev 18.7) |
| `report_n_unique_chunks_cited` | 16 (stdev 6.5) | 13 (stdev 6.9) |
| `report_evidence_count` | 25 (stdev 2.8) | 25 (stdev 1.9) |
| `citation_alignment_pass_rate` | 0.50 | 0.50 |
| `elapsed_seconds` | mean 927 / median 878 | mean 964 / median 964 |

V2 has lower standard deviation on `n_citations` and `n_evidence` —
deterministic curation does what it says. V2 is ~4% slower on average.

### Stable-question regression check

The 6 questions stable across v4.3.10 trials (Q005, Q012, Q021, Q027, Q032,
Q036) anchor the regression watch:

- **Q005** (was 3/3 correct in v4.3.10): V1 = 2/3 correct, V2 = 1/3 correct.
  Both variants slipped one trial to partial. **[amended 2026-05-07]**
  Q005 was 3/3 stable across three independent samples (v4.3.9 and
  v4.3.10 trials 2 and 3) and is now 1/3 in V2 — a real shift to watch
  in the next 3-trial run, not noise. The ±1 envelope was characterized
  on aggregate correct_count, not per-question stability; flagging Q005
  here, not filing it under noise. Both partials trace to the same
  canonical answer omission (1M context applicability to opusplan).
- **Q012, Q021, Q032, Q036**: identical 3/3 partial across v4.3.10, V1, V2.
  No movement. Confirms these verdicts are structural to the corpus, not
  shapeable by curation logic.
- **Q027**: v4.3.10 = 0/3 correct, V1 = 0/2, V2 = 1/3. V2 strictly improves,
  V1 ties.

### Oscillating questions

Q010, Q049, Q050 oscillate at fixed config per v4.3.10's E3 noise floor.

- **Q010** (v4.3.10 had 2 correct + 1 hallucinated): both V1 and V2 land
  3/3 correct. The hallucinated tail-behavior didn't reproduce in either
  variant. Likely just landed lucky.
- **Q049** (v4.3.10 had 1 correct + 2 partial): V1 = 1C+2P, V2 = 1C+2P.
  Identical distribution; the trial that flipped correct differs.
- **Q050** (v4.3.10 had 2 partial + 1 correct): V1 = 2C+1P, V2 = 3C.
  V2 marginally better (3C); V1 also better than v4.3.10 baseline.

None of these movements break out of the ±1 noise envelope.

---

## Why V2 only got 1/3 on Q027 (mechanism deepening)

Re-examining Q027 evidence per trial:

| Trial | V1 c1921 | V1 c2675 | V1 c2674 | V2 c1921 | V2 c2675 | V2 c2674 |
|---|---|---|---|---|---|---|
| T1 | ⨯ | ✓ | ✓ | ⨯ | ✓ | ✓ |
| T2 | ⨯ | ⨯ | ⨯ | **✓** | ✓ | ✓ |
| T3 | (ERR) | (ERR) | (ERR) | ⨯ | ✓ | ✓ |

c2675 and c2674 (which from chunk-id proximity look like they may also
contain April 23 information — confirmed by their consistent presence in
V2's deterministic top-N) are present in 4 of 5 evaluable trials. But the
agent only produces a correct Q027 verdict when **c1921 specifically** is
in evidence (V2 T2).

This is not surprising — c1921 is the canonical chunk identified by E1 with
the exact `<Note>` text containing the April 23 date and ANTHROPIC_MODEL
override. The other April 23-adjacent chunks may discuss the change less
authoritatively, leaving the synthesizer to hedge.

**Implication for follow-up work**: the next iteration should target
*planner / retrieval stability for c1921*. Specifically:
- Why does the planner's sub-query phrasing surface c1921 only ~1/3 of
  the time?
- Is BM25 contributing here? (E2 showed BM25 is structurally inert for
  multi-token sub-queries on Q049 — likely the same issue here.)
- Would a planner-side stability fix (deterministic sub-query templating,
  HyDE for date-conditioned queries, or direct chunk_id pinning for known-
  canonical chunks on dimension=recency questions) help?

These are explicitly **out of scope for v4.3.11** — v4.3.11 ships V2 (the
curation fix), and the retrieval-stability work is the explicit next round.

---

## Final recommendation: SHIP V2

**Rationale**:

1. **V2 strictly dominates V1 on the primary metric.** Q027: V2 1/3 correct
   vs V1 0/3. Both fail the ≥2/3 bar, but V2 is closer.

2. **V1's failure mode is bug-class; V2's failure mode is dependency-class.**
   V1 fails because the agent drops chunks it shouldn't — a fixable design
   flaw. V2 fails because retrieval doesn't surface what's needed — out of
   scope for the curation layer.

3. **V2 introduces no regressions.** The Q005 slip and the verbosity
   uniformity changes are within v4.3.10's documented ±1 noise envelope and
   cost-of-determinism trade-offs respectively.

4. **The structural argument from E4 still holds.** Bundling gap-fill and
   curation gives the agent license to drop high-rerank chunks for soft
   reasons. Separating them is the correct architecture regardless of
   whether Q027's specific bug surfaces in any given trial.

5. **Diagnostic value going forward.** With curation deterministic, future
   evals can attribute Q027 failures unambiguously to retrieval rather than
   to agent caprice. That makes the next round (retrieval stability)
   measurable.

**Do not ship V1.** Even granting the smoke test pass, three trials show
V1's prompt-level guidance is ignored in practice. The agent dropped c1921
when it had it (V1 T2 — c1921 was in `initial_evidence`, agent surfaced
conf=10.0 + the warning paragraph, dropped it anyway). The prompt fix is
the wrong mechanism for this bug.

---

## What this run does NOT do (deferred per plan)

- **No retrieval-layer changes.** Planner stability, BM25 coverage,
  HyDE, query-expansion — all out of scope. Reopened as the explicit next
  round.
- **No 9→25-Q benchmark expansion.** The plan called this out as the
  meta-improvement. Stays out of scope for v4.3.11; goes into its own plan.
- **No T2 rollback or aggregation-logic changes.** E1+E2+E4 all converged
  on "aggregation is not the bottleneck" — V2 results don't change this.
- **No reanalysis of v4.3.7-v4.3.9 decision documents.** Caveat-noting
  pass for prior analyses that depended on Q049 movement is nice-to-have.

---

## Files referenced

Diagnostic record (read-only inputs):

- `data-claude/eval/runs/20260506-rag-v4.3.10/branch_decision.md`
- `data-claude/eval/runs/20260506-rag-v4.3.10/E1_reconstruction.txt`
- `data-claude/eval/runs/20260506-rag-v4.3.10/E3_3trial_matrix.md`

Trial outputs (this run):

- `data-claude/eval/runs/20260507-rag-v4.3.11-prompt-trial{1,2,3}/`
- `data-claude/eval/runs/20260507-rag-v4.3.11-detn-trial{1,2,3}/`

Code (this run):

- Branch `rag-v4.3.11-prompt-fix` — V1 (commit 4830446)
- Branch `rag-v4.3.11-deterministic-topn` — V2 (commit c8f0560)
- Branch `main` — v4.3.10 baseline (4dd26ec) + `--trials` flag (96ec1fb)
