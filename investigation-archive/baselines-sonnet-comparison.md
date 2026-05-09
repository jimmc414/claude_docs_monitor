# Baseline Comparison: RAG vs Trivial Alternatives

Comparison of three minimal baselines (whole_corpus, ripgrep, bm25 — all on Sonnet 4.6) against the v4.3.11 V2 hybrid RAG system (3 trials on Sonnet 4) across 9 hard questions: Q005, Q010, Q012, Q021, Q027, Q032, Q036, Q049, Q050.

## 1. Summary table
| System | correct | partially_correct | incorrect | hallucinated | judge_err | missing |
|---|---:|---:|---:|---:|---:|---:|
| whole_corpus | 0 | 0 | 0 | 0 | 0 | 9 |
| ripgrep | 2 | 7 | 0 | 0 | 0 | 0 |
| bm25 | 2 | 7 | 0 | 0 | 0 | 0 |
| v2_t1 | 2 | 6 | 1 | 0 | 0 | 0 |
| v2_t2 | 5 | 4 | 0 | 0 | 0 | 0 |
| v2_t3 | 2 | 6 | 1 | 0 | 0 | 0 |

## 2. Per-question matrix
Cell legend: ✓ correct, ~ partially_correct, ✗ incorrect, H hallucinated, ?err judge error, — missing.
Note: baseline columns are n=1 each, V2 columns are 3 separate trials (n=3 across them).

| QID | whole_corpus | ripgrep | bm25 | v2_t1 | v2_t2 | v2_t3 |
|---|---|---|---|---|---|---|
| Q005 | — | ✓ | ~ | ~ | ✓ | ~ |
| Q010 | — | ~ | ✓ | ✓ | ✓ | ✓ |
| Q012 | — | ~ | ~ | ~ | ~ | ~ |
| Q021 | — | ~ | ~ | ~ | ~ | ~ |
| Q027 | — | ✓ | ✓ | ✗ | ✓ | ✗ |
| Q032 | — | ~ | ~ | ~ | ~ | ~ |
| Q036 | — | ~ | ~ | ~ | ~ | ~ |
| Q049 | — | ~ | ~ | ~ | ✓ | ~ |
| Q050 | — | ~ | ~ | ✓ | ✓ | ✓ |

## 3. Q027 deep-dive
### Per-baseline (Sonnet 4.6, n=1)

#### whole_corpus
- gold phrase 'April 23, 2026' present in context the LLM saw: **True**
- verdict: **missing**
- reasoning: 
- answer:

```
Prompt is too long
```

#### ripgrep
- gold phrase 'April 23, 2026' present in context the LLM saw: **True**
- verdict: **correct**
- reasoning: The system answer accurately captures all key facts from the canonical answer: the date (April 23, 2026), the affected user tiers (Enterprise pay-as-you-go and Anthropic API users), the new default model (Opus 4.7), the previous default (Sonnet 4.6), and the mitigation options (setting ANTHROPIC_MODEL or the model field in server-managed settings). The system answer also provides additional source
- answer:

```
According to the documentation, on April 23, 2026, **the default model for Enterprise pay-as-you-go and Anthropic API users changed to Opus 4.7**.

This is documented in the **`model-config.md`** file, under the section **"Special model behavior → `default` model setting"**, which contains this note:

> On April 23, 2026, the default model for Enterprise pay-as-you-go and Anthropic API users will change to Opus 4.7. To keep a different default, set `ANTHROPIC_MODEL` or the `model` field in [server-managed settings](/en/server-managed-settings).

Prior to that date (per the same section), Enterprise pay-as-you-go and Anthropic API users defaulted to **Sonnet 4.6**. The note advises users who wish to preserve a different default to explicitly set either the `ANTHROPIC_MODEL` environment variable or the `model` field in server-managed settings.
```

#### bm25
- gold phrase 'April 23, 2026' present in context the LLM saw: **True**
- verdict: **correct**
- reasoning: The system answer correctly identifies all three core points from the canonical answer: the April 23, 2026 date, the new default of Opus 4.7 for Enterprise pay-as-you-go and Anthropic API users, the prior default of Sonnet 4.6, and both mitigation options (ANTHROPIC_MODEL env var and the model field in server-managed settings). The additional details about other account tiers and the logical infer
- answer:

```
According to **`model-config.md` › Model configuration › Special model behavior › `default` model setting**:

> On April 23, 2026, the default model for Enterprise pay-as-you-go and Anthropic API users will change to **Opus 4.7**.

Prior to that date, those account types defaulted to **Sonnet 4.6** (as stated in the same section: *"Pro, Team Standard, Enterprise, and Anthropic API: defaults to Sonnet 4.6"*).

The documentation also notes that if you want to **keep a different default** after this change, you should either:
- Set the `ANTHROPIC_MODEL` environment variable, or
- Set the `model` field in [server-managed settings](https://code.claude.com/docs/en/server-managed-settings)

In other words, this was an automatic upgrade of the default model tier for those users — no action was required to move to Opus 4.7, but action *was* required to stay on Sonnet 4.6 (or any other model) after that date.
```

### v4.3.11 V2 trials (Sonnet 4, n=3)
- **v2_t1** (20260507-rag-v4.3.11-detn-trial1): verdict=**incorrect** — The system answer describes a completely different change (effort level raised from medium to high for Pro/Max subscribers) as the primary event on April 23, 2026, while explicitly asserting that the 'default' alias semantics were unchanged and that no documentation covers Enterprise pay-as-you-go changes on that date. Both of those assertions directly contradict the canonical answer, which states
- **v2_t2** (20260507-rag-v4.3.11-detn-trial2): verdict=**correct** — The system answer correctly identifies all three core facts from the canonical answer: (1) the April 23, 2026 date, (2) the affected account types (Enterprise pay-as-you-go and Anthropic API), (3) the model change from Sonnet 4.6 to Opus 4.7, and (4) the mitigation options (ANTHROPIC_MODEL or model field in server-managed settings). None of these are stated incorrectly. The extra information — sta
- **v2_t3** (20260507-rag-v4.3.11-detn-trial3): verdict=**incorrect** — The system answer's central conclusion is that no April 23, 2026 default-model change for Enterprise pay-as-you-go or Anthropic API users can be found in the retrieved evidence — this directly contradicts the canonical answer, which definitively states that the default changed to Opus 4.7 for exactly those account types on that date. The system answer omits every substantive point in the canonical

## 4. Cost table
| Baseline | Total input tokens | Total output tokens | Total wall time (s) | Avg per-Q wall (s) |
|---|---:|---:|---:|---:|
| whole_corpus | 6,630,483 | 36 | 32.1 | 3.6 |
| ripgrep | 1,118,587 | 5,853 | 365.4 | 40.6 |
| bm25 | 258,461 | 5,921 | 197.9 | 22.0 |

## 5. Honest interpretation
**Whole_corpus failed for technical reasons, not retrieval necessity.** All 9 whole_corpus runs returned 'Prompt is too long' — Sonnet 4.6 default context is 200K, not the 1M the plan assumed (the `context-1m-2025-08-07` beta was retired 2026-04-30 with no GA replacement). This means we cannot directly answer the plan's framing question 'does retrieval beat trivial alternatives?' against full-corpus stuffing. The two baselines that **did** run — ripgrep and bm25 — are the operative comparison.

On strict 'correct' verdicts: whole_corpus=0 (all missing), ripgrep=2, bm25=2, V2 mean=3.0 (n=3). On lenient 'correct + partially_correct': whole_corpus=0, ripgrep=9, bm25=9, V2 mean=8.3. Both ripgrep and bm25 — the two simplest possible retrieval baselines — match V2 on strict correctness and slightly exceed V2's lenient score (9 vs 8.3). The baselines are n=1 each while V2 is n=3, so single-question swings are within noise; but the central tendencies are within ~1 question of each other across all three systems.

**The Q027 result is the cleanest single signal.** Both baselines (n=1 each) got Q027 correct; V2 got it correct on only 1 of 3 trials, with 2/3 trials hallucinating that no such April 23 change exists. On a recency question with the gold phrase plainly present in the retrieved context, V2's planner-stability problems show up clearly while both naive baselines just answer the question. This is consistent with the pattern of the planner-stability investigation that motivated this study.

**Model asymmetry caveat.** The baselines ran on Sonnet 4.6 (`claude-sonnet-4-6`), V2 ran on Sonnet 4 (`claude-sonnet-4-20250514`, deprecated 2026-06-15). The 'newer model' confound cannot be ruled out — perhaps Sonnet 4.6 is simply better at this benchmark and any system using it would tie V2. Either way, the directional read is the same: the current hybrid architecture is not earning its complexity over a 95-line BM25 script on this corpus + benchmark, with this scoring rubric.

**What the data does and doesn't support.** With n=1 per baseline, single-question swings are within noise. The data DOES support: 'whole-corpus stuffing on Sonnet 4.6 default settings is non-viable due to context limits' and 'naive BM25 / naive ripgrep answer-quality is in the same ballpark as V2 on these 9 hard questions'. The data does NOT support: 'X architecture is decisively better than Y'. Use this study to inform the next decision (pivot vs continue vs re-run V2 on newer model), not to declare winners.

## 6. TL;DR
Whole_corpus could not run (context overflow at 736K tokens; Sonnet 4.6 GA = 200K, not 1M as the plan assumed). **Both trivial baselines fall inside V2's own trial-to-trial variance band.** V2 strict trials: [2, 5, 2] (range 2–5, mean 3.0). ripgrep=2, bm25=2 — both at the low end of V2's range, so 'V2 is better' is not supported by this data. On lenient: ripgrep=9, bm25=9, V2 mean=8.3 — baselines slightly exceed V2 here. **Recommendation:** the current architecture is not earning its complexity over a 95-line BM25 script on this benchmark. Consider pivoting to BM25-only or ripgrep-only as the working RAG — and re-run V2 on Sonnet 4.6 to rule out the newer-model confound before committing to a pivot.

Confound: baselines ran on Sonnet 4.6, V2 ran on Sonnet 4 — newer-model wins and simpler-architecture wins are not separable from this data alone.
