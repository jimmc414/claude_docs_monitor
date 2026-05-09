# T9 Branch Decision — v4.3.8 Critique-Retry Ablation

## Headline

| Metric | v3.5 | v4.3.7 | v4.3.8 |
|---|---|---|---|
| correct | 5 | 3 | **2** |
| partially_correct | 4 | 5 | 6 |
| incorrect | 0 | 1 | 0 |
| MISSING (SDK transient) | 0 | 0 | 1 (Q027) |
| 9/9 ok | yes | yes | **8/9** |

**Row 3** of the decision table: `correct < 4 OR < 9/9 ok` → ablation didn't recover.

## Pre-flight fix verification

- **T2 (date kwarg leak):** v4.3.7 had 2 `TypeError: filter_chunk_ids() got an unexpected keyword argument 'date'` in Q027's stderr; v4.3.8 has **0** across all 9 questions. ✅ Plugged.
- **T1, T3, T4:** all wired correctly; subprocess in T7 confirmed spawned with `--no-self-critique`.

## Per-question read

| QID | v3.5 | v4.3.7 | v4.3.8 | Note |
|---|---|---|---|---|
| Q005 | correct | correct | correct | stable |
| Q010 | correct | correct | **partial** | regressed under no-critique |
| Q012 | partial | partial | partial | — |
| Q021 | partial | partial | partial | — |
| Q027 | correct | incorrect | **MISSING** | SDK empty-output crash mid-synth (transient); but T2 unlocked sub-q retrieval (12 chunks vs 8 fallback in v4.3.7) |
| Q032 | partial | partial | partial | — |
| Q036 | partial | partial | partial | — |
| Q049 | correct | partial | **correct** | **T2 recovered it** — date-anchored sub-question retrieval was being silently dropped |
| Q050 | correct | correct | **partial** | regressed under no-critique |

## Interpretation

Three signals, not one:

1. **T2 (date filter) is load-bearing.** Q049 jumped from partial → correct, and Q027's retrieval improved from 8-chunk fallback to 12 chunks before the SDK crash. This refutes the throwaway "affects every run, mostly cosmetic" framing in the plan — for date-anchored sub-questions, T2 was the difference between gold-chunk hit and miss.
2. **Removing critique-retry hurt Q010 and Q050.** Both regressed correct → partial. Looking at scorer notes, both regressions are "added unverified technical specifics" (AST/version claims for Q010; method-name fabrications like `rewind_files`, `stop_task` for Q050). This is consistent with critique-retry's actual job: it forces the model to re-justify each cited claim, suppressing fabricated specifics. **Critique-retry was helping these questions, not just hedging Q027's failures.**
3. **Q027 SDK transient is unrelated.** `claude_agent_sdk returned empty output` mid-synth. Not attributable to the ablation; the retrieval (where T2 lives) succeeded.

The plan's framing — "critique-retry is the dominant cause of v4.3.7 regression vs v3.5" — is **not supported**. With critique-retry removed, correct dropped further (3 → 2). Critique-retry has mixed effects: it can over-hedge (the v4.3.7 Q027 partial-style failure mode the plan inferred) AND it can suppress fabricated specifics (Q010, Q050 in v4.3.8). The "dominant cause" hypothesis was wrong.

## Recommended next action

Skip the row-3-suggested embedding reindex / paraphrase-recall investigation. The recall@10 numbers between v4.3.7 and v4.3.8 are **identical** (answers.jsonl was copied from v4 baseline in T6, so search-side metrics are pinned). The variance is entirely report-side, which means the followups are:

1. **Re-run a critique-on control with T2 applied** (the optional run mentioned at end of Phase 2). This isolates T2's contribution from critique-retry's contribution. Expected outcome: correct ≥ 4 because Q049 recovers AND Q010/Q050 don't regress.
2. **If correct ≥ 4 in that control**, the bug story is: "v4.3.7 regression vs v3.5 was the date-filter leak (T2's bug), not critique-retry." Ship T2; keep critique-retry on.
3. **Defer** the SYNTH/CRITIQUE/retry rework items in the plan's "Out of scope" list — none are indicated by this evidence.

The cheapest decisive next experiment is the critique-on + T2 control run (~2.5 hr wall, no code changes needed since T1-T4 are already in place; just unset `REPORT_NO_CRITIQUE`).
