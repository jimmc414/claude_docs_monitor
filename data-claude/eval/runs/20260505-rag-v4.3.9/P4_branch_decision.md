# P4 Branch Decision — rag-v4.3.9 (T2 on, critique on)

**Run completed**: 2026-05-05 22:41Z, ~2h 56m wall, 9-question subset.
**Configuration**: `REPORT_NO_CRITIQUE` unset (critique on); T2 (date-kwarg normalization) at retriever.py:168; T3 first-pass dump at report_builder.py:1074.
**T2 leak check**: zero `filter_chunk_ids` errors in stderr/. ✅

> **Note (post-Opus-critique revision)**: An earlier version of this document asserted "Q050 is sampling variance" and "T2 is load-bearing via Q049" without testing. Both claims were wrong. Re-tested below. The decision sections were rewritten accordingly.

## Headline correctness (9-question subset)

| Run | correct | partial | incorrect | null |
|---|---|---|---|---|
| v3.5 (gold)              | **5** | 4 | 0 | 0 |
| v4.3.7 (no T2, retry on) | 3 | 5 | 1 | 0 |
| v4.3.8 (T2,  retry off)  | 2 | 6 | 0 | 1 |
| **v4.3.9 (T2,  retry on)** | **3** | 5 | 1 | 0 |

## Per-Q transitions (read across)

| Q | dim | v3.5 | v4.3.7 | v4.3.8 | v4.3.9 |
|---|---|---|---|---|---|
| Q005 | factual    | correct | correct | correct | correct |
| Q010 | citation   | correct | correct | partial | correct |
| Q012 | coverage   | partial | partial | partial | partial |
| Q021 | hallucin.  | partial | partial | partial | partial |
| Q027 | recency    | correct | incorrect | null | incorrect |
| Q032 | negation   | partial | partial | partial | partial |
| Q036 | cross-src  | partial | partial | partial | partial |
| Q049 | paraphrase | correct | partial | correct | correct |
| Q050 | paraphrase | correct | correct | partial | partial |

Q012/Q021/Q032/Q036 are stable partial across all four runs — pre-existing issues, not v4.3.7+ regressions. Removing them, the analysis narrows to **Q010 (recovered), Q027 (broken), Q049 (recovered), Q050 (regressed)**.

## What T2 actually does on this subset

I claimed T2 was "load-bearing" via Q049's recovery. Verified by reading the v4.3.9 plan output for Q049 in reports.jsonl: **all 7 sub-questions have `filters: {}` and no date references in their search queries**. The same is true for v4.3.7. So Q049 cannot have been affected by T2 — there were no date filters for T2 to normalize.

Cross-checking other questions: **v4.3.9's planner emits zero `{"date": ...}` filters across the entire 9-Q subset**, including Q027 (where v4.3.7 had `{"date": "2026-04-23"}` on SQ1 and SQ2 — confirmed in v4.3.7's reports.jsonl). The planner's filter-emission behavior shifted between v4.3.7 and v4.3.9.

**Conclusion on T2**: T2 is correct, leak-free, and necessary if the planner ever emits `{"date": ...}` again. But it is not measurably load-bearing on v4.3.9's actual planner output. Q049's recovery (partial→correct) is unattributed — most likely planner-output sampling variance producing better search queries by chance.

## Q027 deep dive — the regression is at the filter intersection, not the planner OR retrieval alone

I ran the cheap experiment Opus suggested (replay v3.5's plan through v4.3.9's retriever) and found something more nuanced than the critique anticipated.

**Setup**: c1921 is the gold evidence — `model-config.md > default model setting`, listing per-account-type defaults (Max/Team Premium → Opus 4.7; Pro/Team Standard/Enterprise/Anthropic API → Sonnet 4.6; Bedrock/Vertex/Foundry → Sonnet 4.5). Page chunk, no date metadata.

**Result table** (v3.5's queries, varying source/filter restrictions, with v4.3.9's retriever):

| Query (v3.5 SQ#) | source / filters | c1921 rank (raw) | c1921 rank (rerank) |
|---|---|---|---|
| SQ0: "default model behavior change April 23 2026" | `change_event` + `{"date": "2026-04-23"}` | empty (no chunks) | empty |
| SQ0: same query | `None` (no filter) | **1** | **1** |
| SQ1: "default model Enterprise PAYG April 2026" | `change_event` + date | empty | empty |
| SQ1: same query | none | 24 | **1** |
| SQ2: "default model Anthropic API ... change April 2026" | `change_event` + date | empty | empty |
| SQ2: same query | none | **1** | **1** |
| SQ3: "previous default model Claude before April 23 2026" | `page`, no filter | NOT in top 100 | NOT in top 10 |
| SQ4: "new default model Claude April 23 2026 release" | none + date | empty | empty |
| SQ4: same query | none | NOT in top 100 | **1** |

**The regression mechanism**:
- v3.5's planner emitted `source_type='change_event'` + `{"date": "2026-04-23"}` on three of its five sub-questions. c1921 is a page chunk with no date — this filter combination correctly excludes it.
- **Pre-T2**, the `date=` kwarg raised a silent `TypeError` in `filter_chunk_ids()`. The retriever's exception handling (presumably) fell back to an unfiltered search, which **accidentally bypassed source_type='change_event' as well**. With both filters effectively bypassed, c1921 surfaced and v3.5 cited it.
- **Post-T2**, the date kwarg is properly normalized into `since`/`until`. The filter combination now executes as written: source_type='change_event' AND date=2026-04-23 → empty. The accident path is closed; rerank has nothing to rerank.

So Q027's regression is **neither** "planner output drift" (Opus's hypothesis) **nor** "retrieval engine drift" (my earlier hypothesis). It's the planner emitting an over-restrictive filter combination that produces empty results, **with T2 having closed the bug that was incidentally rescuing the search**. The retriever, planner, and T2 are each individually doing the right thing; their composition fails on questions where the planner picks `change_event + date` for a question whose answer lives on a page.

Empirically c1921 is highly retrievable (rerank=1 across multiple paraphrases) **as long as no source_type or date restriction is applied**. The candidate pool is rich. The fix path lies in the composition layer.

## Q050 — Opus's "this is asserted, not demonstrated" was correct

The earlier doc claimed "Q050 is sampling variance." With n=2 (v4.3.7=correct, v4.3.9=partial), this was an unfalsified assertion. I have not run an additional v4.3.9-config trial. I do not know whether Q050 will land correct or partial under the same configuration on a third run.

What I do know from P3c: retry expanded Q050's first-pass with new claims about streaming-mode and TypeScript's `persistSession: false` asymmetry (citing c468 and c413). Whether retry consistently expands Q050 with such claims (a behavior) or only did so in this run (variance) cannot be distinguished from one observation.

## Q010 — the actual evidence for "keep critique on"

v4.3.8 (critique off) had Q010 = partial. v4.3.9 (critique on) has Q010 = correct, T2 held constant. P3c diff shows retry stripped a weakly-anchored c3444 citation about prefix-rule string matching and reorganized the answer. This is one observation that critique-retry helped on at least one question. It is also the *only* unambiguous evidence in this run for keeping critique on.

## Decision

The plan's branch table puts correct=3 in row 2 ("T2 helps but doesn't fully recover; recommend SYNTH_PROMPT/ENUMERATION rollback"). My P3c analysis already argued against the SYNTH rollback. The retrieval experiment now reframes the actual gap:

### What to ship now

**Status: do not ship yet.** Action A (below) is a candidate fix for a known mechanism but has not been tested in the full pipeline. Shipping T2 alone leaves the regression in place. The current state is: T2 is correct in isolation, and a probably-better-but-untested fix for the Q027 composition issue is on deck.

**Persistent decisions** (to keep when something does ship):
- Keep T2 in main. It is correct, leak-free, and prevents a real bug class. Its rollback would re-open the leak that v4.3.7 hit twice on Q027 alone, and an accident path is not a fix path.
- Keep critique on. Evidence is symmetric (Q010 helped, n=1; Q050 hurt, n=1) — not asymmetric as a prior version claimed. Status quo wins on cost in the absence of stronger signal.
- Do not roll back SYNTH_PROMPT or ENUMERATION. Q027 is not synthesis-shaped (the report correctly hedged in both first-pass and final). Q050 is uncharacterized.

### Pre-experiment results (run during this analysis, ~10 min)

#### Action A ladder design — empirically grounded

Tested whether dropping date alone surfaces c1921, or source_type must also drop. Took v3.5's restrictive sub-queries (`source_type='change_event'` + `{"date": "2026-04-23"}`) and walked the ladder:

| Rung | Config | Hit count (per query) | c1921 retrieved? |
|---|---|---|---|
| 0 | original (change_event + date) | 0 | no |
| 1 | drop date, keep source_type=change_event | 4 | no — c1921 is a page chunk, never reachable here |
| 2 | drop both filters | 10 | **yes, rerank rank 1 on 4 of 4 queries** |

For Q027 specifically, **rung 1 is structurally insufficient** because c1921's source_type is `page`, not `change_event`. The fallback must reach rung 2 to surface it.

#### Action A scope — the picture is bigger than just Q027 SQ0/SQ1/SQ2

Tested v4.3.9's actual Q027 sub-queries through the same retriever (not v3.5's). SQ4 — `"Claude default model tier enterprise API pay-as-you-go upgrade"` with `source_type='page'` — already returns **c1921 at rerank rank 1 in rung 0, no fallback needed**. But the actual v4.3.9 run had only 1 model-config.md chunk in its 19-chunk evidence pool (c1905), and c1921 was excluded.

So the Q027 regression has **at least two compounding sources**:
1. **Filter composition** (SQ0/SQ1/SQ2 with `change_event + date` → empty pool). Action A fixes this.
2. **Aggregation/rerank stochasticity** (SQ4 should have surfaced c1921 in its top-10 but didn't make the final 19-chunk evidence pool). Action A does *not* fix this; it lives in `report_builder.py`'s evidence-aggregation logic or in rerank determinism.

The replay was run with `rerank=True, k=10`. If the same call produces different rankings between my replay and v4.3.9's original run, then **rerank is non-deterministic across calls.** This affects every conclusion drawn from one-trial-per-config evals.

#### Action C result — Q049's recovery is plausibly retriever variance

Diffed Q049 chunk evidence pools and citations between v4.3.7 (partial) and v4.3.9 (correct). Plans are semantically near-identical (7 sub-questions, same topics, minor word-order shuffles). Yet:
- Of 25 evidence chunks per run, only ~13 overlap; 12 are unique to each run.
- v4.3.9 cited 25 chunks vs v4.3.7's 18; v4.3.9 added comparison-table chunks (c251–c255 cluster) that match the gold answer's expected enumeration.

Same retriever + nearly-same queries → ~50% different evidence pools → different correctness verdict. Most plausible source: agent-loop curation variance (see Action D below), not rerank.

#### Action D part 1 — rerank IS deterministic; the variance is elsewhere

Re-ran v4.3.9's actual Q027 SQ4 query (`"Claude default model tier enterprise API pay-as-you-go upgrade"`, source=page, rerank=True) **5× with k=10 and 1× with k=8** (the actual run's setting):

| Trial | Top-8 chunk_ids | c1921 rank |
|---|---|---|
| 1 (k=10) | [1921, 1916, 2728, 2675, 8, 9, 778, 2344, 1904, 1167] | 1 |
| 2 (k=10) | [1921, 1916, 4760, 8, 9, 777, 778, 2344, 1904, 2728] | 1 |
| 3 (k=10) | [1921, 1916, 777, 2683, 4760, 8, 9, 778, 2344, 1904] | 1 |
| 4 (k=10) | [1921, 1916, 2728, 4760, 8, 9, 777, 778, 2344, 1904] | 1 |
| 5 (k=10) | [1921, 1916, 4760, 1904, 2675, 1164, 8, 9, 777, 778] | 1 |
| 6 (k=8)  | [1921, 1916, 2728, 8, 9, 778, 1904, 2683] | **1** |

c1921 ranks 1 in 6/6 trials. Rerank is stable at the top of the ranking. So **rerank is not the source of v4.3.9's c1921 exclusion.**

This means SQ4 reliably returns c1921 at rank 1 → c1921 *should have been* in v4.3.9's initial_evidence pool with high confidence. But it wasn't in the final 19-chunk evidence pool. The dropping happened at one of two places:

1. **Cross-sub-query confidence aggregation** (`retrieve_for_plan`, lines 222–280 of report_builder.py): each sub-query's hits are merged by chunk_id, keeping the max-confidence Evidence. Then sorted by confidence descending. The top 30 by confidence are shown to the agent. If c1921 was at rank 1 in SQ4 but had a confidence score lower than 19+ chunks aggregated from SQ0–SQ3, it could be pushed below position 30.

2. **Agentic-loop curation** (lines 449–516 of report_builder.py): the agent is shown `initial_evidence[:30]` and asked to pick the relevant `final_chunk_ids`. If c1921 was in the top 30 but the agent's prose-ranking heuristic didn't find it relevant (e.g., because the question framing emphasizes "Enterprise PAYG and Anthropic API users" — words c1921 doesn't contain — and the agent gravitated toward the cloud-provider chunks that match that surface phrasing), c1921 gets dropped.

Without direct dumps of `initial_evidence[:30]` from v4.3.9's actual run, we can't distinguish 1 from 2 from this artifact alone. **But both are different fix paths from Action A.**

### Action plan (updated after Action D part 1)

**A. Filter-composition fallback ladder in `report_builder.py` (~1.5 hr code + test)** — *necessary but probably not sufficient for Q027*

Implement Opus's staged ladder design: when `hybrid_search(...)` returns 0 chunks for a sub-question, retry first with `filters={}` only, then with `source_type=None, filters={}`. Cost: at most 2 extra retrievals per emptied sub-question, only when needed.

Refinement based on pre-experiment: for Q027, only rung 2 helps — but the ladder still costs nothing extra when rung 1 succeeds. Keep both rungs.

Refinement per Opus: cap the number of sub-queries that get fallback rescue (e.g., at most 2 of N) so a planner that emits 5 over-restrictive filters doesn't drown the pool in 5 widened searches. If the cap is hit, log and proceed with what's there.

**Caveat surfaced by Action D**: even with Action A widening the candidate pool from SQ0/SQ1/SQ2, c1921 may still be dropped at the cross-sub-query confidence aggregation step or by the agent's curation. SQ4 in v4.3.9's actual run reliably retrieved c1921 at rank 1, but c1921 didn't end up in the final 19-chunk evidence pool. **Action A is therefore necessary (it fixes the empty-pool edge case) but probably not sufficient on its own to recover Q027.**

**A2. Force-include top-K chunks per sub-query in `retrieve_for_plan` (~1 hr code + test)** — *new, suggested by Action D*

Currently `retrieve_for_plan` dedupes across sub-queries by max confidence, then sorts by confidence globally. A chunk that was rank 1 in its own sub-query can fall below position 30 in the global pool if other sub-queries returned more chunks with higher confidence. Fix: in addition to global sort, guarantee the top 2-3 chunks from each sub-query are visible to the agent. This costs at most ~5 extra positions in `initial_evidence[:30]`.

Pair with A. Together they ensure: (i) no sub-query is silently empty, and (ii) every sub-query's top results reach the agent.

**B. Two additional v4.3.9-config trials, not just one (~6 hr wall, no code change)**

Originally proposed 1 trial to test the Q050 variance claim. The Q049 evidence-pool diff suggests rerank variance is substantial across the board, so **one extra trial isn't enough — it's pitting one observation against another.** Run 2 trials and treat the 3-trial set as the smallest meaningful sample. Look at Q050, Q049, and Q027 independently:
- If Q050 lands correct in 2 of 3, variance story holds.
- If Q049 lands correct in 2 of 3, real recovery; otherwise also variance.
- If Q027 lands the same way (incorrect) in 3 of 3, Action A is the right next intervention; else variance is dominating Q027 too.

This is more expensive but resolves the broader noise concern, not just one question.

**C. Q049 read-only diff** — done above. Result: plausibly retriever variance under near-identical plans. No further code action recommended; folded into B's broader noise investigation.

**D. (Newly named, not yet scoped) Rerank determinism / aggregation review**

The fact that SQ4 should have surfaced c1921 but didn't in v4.3.9's run points at one of:
- Rerank backend (Claude reranker) is non-deterministic call-to-call
- Aggregation logic in `report_builder.py` drops chunks under some path
- `max_per_source` or dedup is silently filtering

Investigate by: re-running v4.3.9's exact Q027 SQ4 call 5×, see if c1921's rank is stable. Read `report_builder.py`'s evidence-aggregation step and look for filtering. ~1 hr read-only.

**E. (Out of scope for this iteration, named per Opus's request) The Q027 fix space is bigger than Action A**

Three places to address Q027-class issues:
1. **Planner prompt** — teach it not to combine `source_type='change_event'` + `date` filter when the answer might live on a page. Highest leverage but hardest to validate without a structured planner-eval harness.
2. **Retriever fallback** — Action A. Cheapest. Only widens when empty.
3. **Index/data layer** — extend change_event chunks to include forward-looking change announcements that live in `model-config.md` (e.g., add metadata linking c1921 to the April 23 change_event). Most invasive.

Action A is chosen because it is cheapest, most targeted, and reversible. (1) and (3) remain on the table if A is insufficient.

### What this means for the bigger picture

correct=3 vs v3.5's correct=5 is not "shipped and done." Two questions remain unaccounted for plus a newly surfaced concern:
- **Q027**: filter composition + aggregation/rerank stochasticity. A and D address different parts.
- **Q050**: variance vs systematic is unresolved. B addresses.
- **Eval signal noise** (newly elevated): Q049's evidence-pool diff and the SQ4 mystery suggest non-trivial run-to-run variance in the retrieval layer. B addresses by widening the sample; D investigates the source.

If A + B + D collectively don't recover correct ≥ 5, the residual gap is in the persistent partials (Q012/Q021/Q032/Q036), which are out of scope for this branch.

## Out-of-scope (defer)

- SYNTH_PROMPT rollback — not the gap source on this subset.
- ENUMERATION rule rollback — same.
- Retry re-architecture (re-retrieve, not just re-synth) — Q027 first-pass already correctly hedged "no evidence," so retry-re-retrieval wouldn't trigger. Action A (filter fallback in the initial retrieve) is the right place.
- Embedding/paraphrase recall investigation — c1921 is highly retrievable when filters are removed, so the embedding layer is not the bottleneck for Q027. Paraphrase recall@10 dropping (0.65 → 0.583) may be a separate phenomenon worth tracking but is not the v3.5→v4.3.9 correctness regression source.

## Acknowledgments

Opus 4.7's two rounds of critique pushed back on multiple claims and were substantively right:

**Round 1**:
1. "Q050 is sampling variance" — correctly identified as asserted-not-demonstrated. Updated to acknowledge uncertainty; Action B added to test (now expanded to 2 trials).
2. "v4.3.9 ≥ v4.3.8" framing — correct that v3.5 is the load-bearing baseline, not v4.3.8.
3. The meta-suggestion to actually run the cheap retrieval experiment instead of asserting from chunk-count diffs. The experiment was decisive.

**Round 2**:
1. Action A's design — staged ladder (date → source_type) is safer than a one-step zero-filter fallback. Adopted, with the ladder cap (≤ N/2 sub-queries can fall back) Opus suggested.
2. "Q049 unattributed recovery should worry us more" — correct. The Q049 diff (Action C) showed ~50% pool divergence on near-identical plans. Elevated to a first-class concern (Action D) and broadened Action B from 1 trial to 2.
3. Decision framing — "asymmetric uncertainty" was a stretch on n=1/n=1 evidence; updated to "symmetric, status quo wins on cost."
4. Q027 fix space is bigger than Action A — three layers (planner / retriever / data) named explicitly in Action E for completeness, even though A is the chosen path.

**Honest credit accounting**: Opus's Round 1 specific hypothesis (planner dropping a date-mentioning sub-question) was empirically falsified — v4.3.9 has 5 date-mentioning sub-questions, same as v3.5. What Opus contributed was the discipline of running the experiment instead of speculating, and Round 2's calibration corrections. The mechanism (filter-composition + T2 closing an accident path) was found by the experiment, not predicted by either of us.
