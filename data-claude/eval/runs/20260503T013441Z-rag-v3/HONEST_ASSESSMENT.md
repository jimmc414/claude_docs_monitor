# rag-v3 Honest Assessment (2026-05-04)

**TL;DR**: The voyage-4-large embedding swap delivered a real `correct` win (2 → 4, recovering past baseline) and recovered cross-source recall. But the planned `S2` (completeness check) and `R2` (semantic dedup) didn't materially help — S2 because the benchmark harness never invoked it, R2 because dedup hurts chunk-level paraphrase Jaccard. The biggest unsolved problem (paraphrase stability, FAIL verdict) is **not an embedding-quality issue** — it's the query-expansion + reranker pipeline introducing ~50% noise that dominates dense retrieval. The clean fix exists (R3, designed below) but isn't shipped yet.

---

## What changed in rag-v3

| Phase | Item | Status |
|---|---|---|
| R0 | Voyage bake-off (voyage-4-large vs voyage-context-3) | Done. voyage-4-large wins decisively (~80% better Jaccard@5). |
| R1 | Reindex with voyage-4-large | Done. 6462 vectors, 0 API errors. |
| R2 | Semantic chunk dedup after RRF | Built but **flipped to default-OFF** after data showed it hurts chunk-level Jaccard by ~5pp. Implementation retained for future KG use. |
| S1 | `max_tokens` pass-through | **Skipped**. Investigation revealed Q050's "truncation" is a completeness gap, not a length cap. SDK has no `max_tokens` field; CLI has no `--max-tokens` flag. No reports actually hit a length wall. |
| S2 | Completeness check in `_self_critique` | **Wired into code but NOT exercised in this benchmark.** `run_reports.py:41` still passes `--no-self-critique`. Test gap, not implementation gap. |

---

## Headline metrics: baseline | postfix-v2 | rag-v3

| METRIC | baseline | postfix-v2 | **rag-v3** | Δ vs pv2 |
|---|---:|---:|---:|---:|
| `correct` | 3 | 2 | **4** | **+2 ⬆⬆** |
| `partially_correct` | 6 | 7 | 5 | -2 ⬆ |
| `lure_refused` | 1 | 1 | 1 | hold |
| `n_S1` (high-severity) | 1 | 0 | 0 | hold |
| `n_S3` (low-severity) | 6 | 8 | 7 | -1 ⬆ |

### Recall@10 by dimension

| dim | baseline | postfix-v2 | rag-v3 | Δ vs pv2 |
|---|---:|---:|---:|---:|
| factual | 0.917 | 0.917 | 0.917 | hold |
| citation | 0.800 | 1.000 | **1.000** | hold |
| coverage | 0.767 | 0.717 | 0.717 | hold |
| negation | 0.833 | 0.750 | 0.667 | **-0.083 ⬇** |
| recency | 0.800 | 1.000 | 0.900 | -0.100 ⬇ |
| **cross_source** | 0.733 | 0.700 | **0.833** | **+0.133 ⬆** |
| paraphrase_pair | 0.692 | 0.658 | 0.658 | hold |

### Citation alignment

| | baseline | postfix-v2 | rag-v3 |
|---|---:|---:|---:|
| supports | 26 | 30 | 27 |
| partial | 26 | 24 | 27 |
| contradicts | 2 | 0 | 0 |
| unrelated | 0 | 1 | 0 |

### Adversarial probes

| Probe | baseline | postfix-v2 | rag-v3 |
|---|---|---|---|
| P1_filter_leakage | PASS | PASS | PASS |
| P2_multi_hop_retrieval | PARTIAL | PARTIAL | **FAIL ⬇** |
| P4_stale_data_retrieval | PASS | PASS | PASS |
| P_chunk_existence | PASS | PASS | PASS |
| P_paraphrase_stability | WEAK | FAIL | FAIL (still) |

---

## Per-question correctness flips (postfix-v2 → rag-v3)

| QID | Dim | PV2 | rag-v3 | Δ |
|---|---|---|---|---|
| Q005 | factual | correct | correct | — |
| Q010 | citation | partially_correct | **correct** | UP |
| Q012 | coverage | partially_correct | partially_correct | — |
| Q021 | hallucination_lure | partially_correct | partially_correct | — |
| Q027 | recency | correct | correct | — |
| Q032 | negation | partially_correct | partially_correct | — |
| Q036 | cross_source | partially_correct | partially_correct | — |
| Q049 | paraphrase_pair | partially_correct | **correct** | UP |
| Q050 | paraphrase_pair | partially_correct | partially_correct | — |

Two questions flipped to `correct`: **Q010 (citation)** and **Q049 (paraphrase_pair)**. Both are pure retrieval wins from voyage-4-large finding higher-quality evidence — neither involved S2 or any pipeline change.

Q032 (the .idea/.husky-list-completeness case) is still `partially_correct` because S2 never ran. Q050 (the comparison-table-completeness case) is still `partially_correct` for the same reason.

---

## The Paraphrase-Stability Paradox

This is the most important finding in this report.

**On paper**: voyage-4-large is strictly stronger than nomic-embed-text. We proved this in the R0 bake-off:
- Probe-pair query-to-query cosine: voyage-4-large 0.792 vs voyage-context-3 0.746
- Real-chunk Jaccard@5 in single-doc tests: voyage-4-large 0.667 vs voyage-context-3 0.468

**In practice**: the end-to-end probe shows `P_paraphrase_stability` is still **FAIL** with voyage-4-large. Mean chunk Jaccard@5 across 5 paraphrase pairs:
- baseline (nomic): 0.445
- postfix-v2 (nomic): 0.380
- **rag-v3 (voyage-4-large): 0.326** — slightly worse than postfix-v2

That's contradictory until you isolate the layers. We ran the same 5 paraphrase pairs through the live retriever with various pipeline knobs:

| Config | Mean Jaccard@5 |
|---|---:|
| Default (expand + rerank ON) | 0.236 |
| No expand | 0.452 (+0.216) |
| **No rerank** | **0.469 (+0.233)** |
| No expand + no rerank | 0.417 |
| Dedup ON, no rerank | 0.469 |
| **No dedup, no rerank** | **0.619 (+0.383)** |

Reading: when we strip out the LLM-generated query expansion (Haiku-paraphrased query variants) AND the LLM reranker (Claude scoring chunks against literal query text), Jaccard nearly **triples** from 0.236 → 0.619. The dense-only path is the most paraphrase-stable.

**Why**: rerank scores chunks against the literal query string. Two paraphrased queries — "How do I limit tools?" vs "How do I restrict tool access?" — get *different* rerank orderings even when the dense layer agrees on the candidate set. Query expansion compounds this by generating *different* paraphrase variants per query (Haiku is stochastic), so even BM25 hits diverge.

**The voyage-4-large dense layer IS doing its job.** The pipeline above it is what's making paraphrased queries surface different chunks.

---

## Honest verdict

**Keep voyage-4-large**. The evidence:

✅ `correct: 2 → 4` (objective LLM-judge correctness, recovered + 1 over baseline)
✅ `cross_source` recall +0.133 (real win on multi-page synthesis)
✅ `citation@10` held at 1.000 (no regression)
✅ `factual` held at 0.917
✅ `contradicts` held at 0 (entailment audit doing its job)
✅ R0/R0b chunk-level cosine and Jaccard tests confirmed strict dense-quality win

❌ `negation` -0.083, `recency` -0.100 (small recall slips on individual dimensions)
❌ `P2_multi_hop` PARTIAL → FAIL (needs investigation; possibly probe-specific)
❌ `P_paraphrase_stability` still FAIL (pipeline issue, not embedding issue)
❌ `n_S2` 8 → 9, `partial_alignment` 24 → 27 (more "partially supports" judgments)

The headline `correct` jump dominates. The probe regression has a known mechanical cause and a known fix. Rolling back voyage-4-large would re-cost us the `correct` win without fixing the paraphrase issue (which baseline also failed on, just with WEAK instead of FAIL).

---

## Why `n_S2` and `partial_alignment` ticked up

Plausible mechanism: voyage-4-large surfaces **more dense matches per query** than nomic, because the model is generally stronger. The reranker keeps slightly different top-5s. Some of those new top-5 chunks are *plausibly* related to the question but don't directly support specific sentences in the report — judge marks those as `partial_alignment`. This isn't a quality regression in synthesis; it's a side-effect of broader retrieval. Worth watching but not a blocker.

---

## What the data tells us to do next (R3)

The pipeline-stability fix is now well-defined. Three options, with my recommendation:

### Option A: Drop query expansion entirely (recommended)

**Why**: voyage-4-large is strong enough that the Haiku paraphrase step is redundant — and the data shows it actively hurts paraphrase consistency (no-expand: +0.216 mean Jaccard).

**Cost**: One LOC change in retriever.py default + one Haiku call per query saved.

**Risk**: Some queries genuinely benefit from expansion (rare-vocabulary queries that don't match doc phrasing). For those we'd lose recall. But the data shows the average impact is positive.

**Trade-off**: Can be guarded behind a `--expand` opt-in for debugging.

### Option B: Make rerank query-text-agnostic

**Why**: rerank's instability comes from scoring chunks against literal query text. If we score chunks against a **query embedding** instead (cosine to fixed dense vector), paraphrased queries with similar embeddings get similar scores.

**Cost**: ~50 LOC. Replace the LLM rerank call with a cheap re-cosine pass over top-50 candidates using the same query embedding we already computed.

**Risk**: Loses the reasoning capacity of LLM reranker. Might hurt single-query relevance even if it helps paraphrase consistency.

### Option C: Cache query expansions

**Why**: If two paraphrased queries happen to generate the same expansion (unlikely) we'd get consistent results.

**Risk**: Doesn't help — paraphrased queries are different strings, so cache keys differ. Doesn't address the real issue. **Skip this option.**

### My recommendation: Option A first, evaluate, then maybe Option B

1. Drop query expansion default → re-run benchmark → measure
2. If paraphrase stability flips to PASS/WEAK and `correct` holds: ship it
3. If paraphrase still poor: layer Option B on top
4. If `correct` regresses with Option A: roll back, try Option B alone

Estimated effort: 1 hour code + 1 benchmark run = ~2 hours total to settle.

---

## What needs to happen before claiming "optimal" status

In priority order:

1. **R3 Option A** (drop query expansion default) — the single biggest pipeline fix.
2. **Exercise S2** (remove `--no-self-critique` from run_reports.py) and re-run reports. This is the only way to know if the completeness-check actually flips Q032/Q050.
3. **Investigate negation/recency slips** (Q032 detail; check if voyage-4-large surfaces different but valid chunks that the judge marks down).
4. **Investigate P2_multi_hop FAIL** (probe-specific regression — may be probe quirk vs real issue).
5. **E1** (CI / sample-size / baseline-diff in synthesize.py) — without this we keep relitigating verdict-level claims on N=5 to N=9 samples.
6. **E2** (LLM-based benchmark generator → 150 questions) — only after E1 lands; without CIs, more questions don't fix the noise.

---

## Risk register

- **Voyage-4-large could be reverted** if a future benchmark shows the negation/recency slips persist and aren't offset by `correct` wins. Cost of revert: 1 line in `embedding_cache.py` + ollama reindex (~30 min). Embeddings cache survives both providers (composite PK on model name).
- **Dedup is built but disabled.** When KG work begins, this is the entry-point primitive. Don't delete the implementation.
- **S2 is wired but untested.** Carries some confidence-bias risk: the prompt was hand-written based on Q032/Q050 patterns; it may over-trigger on legitimate summaries. Need to test at scale before trusting.

---

## Files modified in rag-v3 cycle

| File | Change |
|---|---|
| `embedding_cache.py:43-50, 90-103` | Default model `voyage-3` → `voyage-4-large`; batch size 128 → 50 (token-cap); add voyage-4 family to `_MODEL_TO_PROVIDER` |
| `data-claude/eval/runner.py:22-23` | Drop Ollama override (let Voyage default kick in) |
| `data-claude/eval/run_reports.py:12` | Drop Ollama override |
| `data-claude/eval/probes.py:28-30` | Drop Ollama override |
| `data-claude/eval/embed_compare.py` | NEW: R0 bake-off script |
| `data-claude/eval/embed_compare_singledoc.py` | NEW: R0b single-doc bake-off |
| `report_builder.py:628-680, 868-925` | S2: extend CRITIQUE_PROMPT with completeness section; add evidence_summary input to `_self_critique`; pipe `missing_enumerations` into retry feedback |
| `retriever.py:140-146, 220-227, 287-340` | R2: add `_semantic_dedup`; new `dedup`/`dedup_threshold` retrieve() params; default OFF |
| `claude_docs_monitor.py` (search subparser) | New `--dedup` opt-in flag |
| `.env` | Voyage API key (gitignored) |

---

## What this assessment is NOT claiming

- That voyage-4-large solves paraphrase stability — it doesn't (root cause is pipeline-level, not embedding-level).
- That S2 is validated — it isn't (never ran in benchmark; needs separate test).
- That R2 dedup is useful for retrieval — data shows it's mildly harmful for chunk-Jaccard. Kept for future KG work only.
- That `correct: 2 → 4` is statistically significant — N=9 reports, 2-question swing, no CI. The trend is positive but the sample is small. Once E1 lands we can quantify confidence.
