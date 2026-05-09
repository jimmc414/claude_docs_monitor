# Honest Assessment: F1–F8 Regression Run

**Run**: `20260503T013441Z-postfix-all` (2026-05-03)
**Comparison baseline**: `20260503T013441Z` (2026-05-02)

## TL;DR — What actually moved

| Fix | Status | Evidence |
|---|---|---|
| **F1** Entailment audit | **NOT TESTED** | Both `runner.py` and `run_reports.py` pass `--no-self-critique`, which disables the audit. The `contradicts: 2 → 1` change is retrieval noise, not F1 working. |
| **F2** Refusal language | **WORKING (content); FAILED (metric)** | Q021 says "does not appear in the cached Anthropic documentation as of 2026-05-03" definitively — better than baseline. But `scorer.hallucination_short_circuit` checks for "does not exist" / "no documentation", NOT "does not appear". Result: actual answer is BETTER but `lure_refused` dropped 1 → 0. **Scorer + F2 prompt are out of sync — calibration bug, not real regression.** |
| **F3** Mean fusion | **NET NEGATIVE — RECOMMEND ROLLBACK** | factual 0.917→0.833, recency 0.800→0.600, paraphrase 0.692→0.658, P_paraphrase_stability WEAK→FAIL. Bedrock probe pair dropped 0.818→0.429. Mean fusion is dampening the strong-evidence signal. |
| **F4** Table chunking | **NET POSITIVE w/ side effect** | Q009 (motivating): 0.000→1.000. citation@10: 0.800→1.000. settings.md table_rows retrievable. **But**: 2066 new chunks crowd the index — Q003, Q029, Q032 lost their original `permissions.md`/`settings.md` ranking to other relevant pages. Some of these are arguably better matches (`permission-modes.md` vs `permissions.md` for "five permission modes"); some are real regressions. |
| **F5** Plan enumeration | **WORKING** | Q012 (motivating) now covers all 10 mechanisms (CLAUDE.md, MEMORY.md, Skills, sub-agents, hooks, settings, sessions, transcripts, etc.). Baseline missed Skills. |
| **F6** Provider auto-detect | **WORKING** | Auto-resolved Ollama from cache during all phases. |
| **F7** README parity | **WORKING** | Static change. |
| **F8** Progress hooks | **WORKING** | Stage messages emitted to stderr during reports. |

## Headline metrics diff

| Metric | Baseline | New | Δ |
|---|---|---|---|
| `correctness_dist.correct` | 3 | **4** | +1 ✅ (the most-trustworthy metric) |
| `correctness_dist.partially_correct` | 6 | 5 | -1 |
| `alignment_dist.supports` | 26 | 28 | +2 ✅ |
| `alignment_dist.partial` | 26 | 23 | -3 |
| `alignment_dist.contradicts` | 2 | 1 | -1 ✅ |
| `alignment_dist.unrelated` | 0 | 2 | +2 (new bucket) |
| `lure_refused` | 1 | 0 | -1 ❌ (calibration: F2 phrase not in scorer keywords) |
| `lure_failed` | 0 | 1 | +1 ❌ (same calibration issue) |
| `recall@10 factual` | 0.917 | 0.833 | -0.084 ❌ |
| `recall@10 citation` | 0.800 | **1.000** | +0.200 ✅ (F4 win) |
| `recall@10 coverage` | 0.767 | 0.717 | -0.050 |
| `recall@10 negation` | 0.833 | 0.667 | -0.167 ❌ |
| `recall@10 recency` | 0.800 | 0.600 | -0.200 ❌ |
| `recall@10 cross_source` | 0.733 | 0.700 | -0.033 |
| `recall@10 paraphrase_pair` | 0.692 | 0.658 | -0.034 |
| `n_S2` (severity-2 issues) | 8 | 9 | +1 |
| `n_S3` (severity-3 issues) | 6 | 11 | +5 ❌ |
| `P_paraphrase_stability` | WEAK | FAIL | ❌ |

## Root-cause attribution

The recall drops are NOT all from one fix:

- **F3 mean-fusion is the primary recall offender.** Probe-level evidence: 3 of 5 paraphrase pairs got worse; the Bedrock pair (0.818→0.429) and tools pair (0.538→0.333) are unambiguous. F3 averages chunk scores across stochastic paraphrase variants, dampening the chunk that hits hardest on the strongest variant. This was the exact failure mode the original plan flagged as a possible side effect.
- **F4 table chunking caused a smaller secondary drop** because 2066 new chunks (76% increase in index size) compete with whole/section chunks for top-10 slots. Some of the displaced pages are genuinely less relevant (e.g., `permission-modes.md` outranking `permissions.md` for "five permission modes" is correct), but Q029 (Windows managed settings) and Q030 (model-config) appear to be real recall regressions.

## Recommendations (prioritized)

1. **Roll back F3 (mean-fusion)** OR replace with the "top-2-of-N max" alternative the original plan mentioned. The mean-fusion premise was sound but the empirical result is worse than max. **Evidence: 3 dimensions and 3 of 5 probes regressed.**
2. **Fix the F2 ↔ scorer keyword mismatch.** Either (a) update scorer's `refusal_signals` list (`scorer.py:111-115`) to include "does not appear in", or (b) update F2 prompt to use a phrase already in the scorer list. Option (a) is more honest because "does not appear in" is what the F2 prompt actually instructs the model to say.
3. **Make F1 actually run during eval.** Either remove `--no-self-critique` from `run_reports.py:41` and `runner.py:82` (slower but lets F1 audit fire) OR detach the entailment audit from the self-critique block in `report_builder.py` so it runs unconditionally. F1 is currently untested at all.
4. **F4 collateral**: tune the chunker to either (a) cap table_row chunks per page (e.g., max 50) or (b) lower their FTS5/dense scoring weight so they don't outcompete whole-page chunks on broad queries. Or just accept the trade-off — citation@10 went 0.8→1.0, which is a major win.

## What "good" looked like, with calibration

If we accept that F2's "does not appear" should count as refusal (it is the strictly more honest phrasing) and that F1 wasn't tested:

- `correct: 3 → 4` (a real, hard-to-game gain)
- `citation@10: 0.800 → 1.000` (clear F4 win)
- `Q012 coverage: missing Skills → covers all 10 mechanisms` (clear F5 win)

If we then **revert F3** and re-run, the recall drops on factual/recency/paraphrase should disappear, leaving F4's wins in place.

## What we did NOT measure

- Prompt injection (F-injection probe skipped per plan).
- F1 entailment audit on real reports (eval harness disables it).
- Whether F4's table chunking generalizes to all the table-heavy pages (env-vars.md 217 rows, agent-sdk/typescript.md 162) or just the easy ones.

## Files for review

- `data-claude/eval/runs/20260503T013441Z-postfix-all/headline_metrics.json` — raw metrics
- `data-claude/eval/runs/20260503T013441Z-postfix-all/scores.jsonl` — per-Q scoring
- `data-claude/eval/runs/20260503T013441Z-postfix-all/reports.jsonl` — 9 reports
- `data-claude/eval/runs/20260503T013441Z-postfix-all/findings.md` — synthesis output
