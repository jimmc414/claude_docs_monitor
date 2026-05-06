# E4 — Aggregation-logic close read of `_initial_retrieve`

**Subject:** `report_builder._initial_retrieve()` (lines 214–280)
**Mode:** Design critique. No compute. No code change.
**Authored:** v4.3.10 mechanism-isolation pass.

---

## 1. What the function does today

```python
def _initial_retrieve(plan, retriever, scope, since, until, k_per_sub=8) -> list[Evidence]:
    evidence_by_id: dict[int, Evidence] = {}
    for strategy in plan["search_strategies"]:
        sub_idx = strategy.get("sub_question_index", 0)
        sub_q = plan["sub_questions"][sub_idx]
        search_q = strategy.get("search_query") or sub_q
        sub_source = strategy.get("source_type")
        if sub_source not in ("page", "change_event", None):
            sub_source = None
        filters = dict(strategy.get("filters") or {})
        if since: filters["since"] = since
        if until: filters["until"] = until
        if scope and len(scope) == 1 and not sub_source:
            sub_source = scope[0]
        hits = retriever.retrieve(search_q, source_type=sub_source, filters=filters or None,
                                   k=k_per_sub, rerank=True)
        for h in hits:
            confidence = h.score_rerank if h.score_rerank is not None else max(0.0, 1.0 - h.rrf_rank/50)
            ev = Evidence(chunk_id=h.chunk_id, ..., confidence=float(confidence), ...)
            existing = evidence_by_id.get(h.chunk_id)
            if existing is None or existing.confidence < ev.confidence:
                evidence_by_id[h.chunk_id] = ev
    return sorted(evidence_by_id.values(), key=lambda e: -e.confidence)
```

Behavior in plain words:

1. For each sub-query, run `retriever.retrieve(k=8, rerank=True)`. Each hit carries
   `score_rerank` (0–10 from Claude rerank).
2. Dedupe by `chunk_id`, keeping the **max-confidence** Evidence across sub-queries.
3. Sort the deduped pool by confidence descending.
4. Caller slices `[:30]` for the agent prompt.

The agent then sees, per chunk, only `<chunk_id>: <heading_path[:100]>`. Confidence
scores and which sub-query produced the hit are **not surfaced** to the agent.

---

## 2. Critical observations from E1 + E2

These reframe the design discussion before any "alternative" claim is made.

### Observation 1 — Q027 v4.3.9: the aggregation is NOT the bottleneck

E1 reproduced v4.3.9's run and found:

- Pool size: **20** (well below the 30 the agent sees)
- c1921: **position 1 of 20**, confidence 10.000 (the rerank ceiling)
- c1921's `relevance_to`: SQ4 ("Are there different default model tiers or upgrade
  paths..."), the broadest sub-question — not a tightly focused one
- The agent dropped c1921 anyway. The post-curation evidence (19 chunks) doesn't
  contain it.

The current design surfaced the perfect chunk first. Anything we change in
aggregation-logic is fixing the wrong layer for Q027.

### Observation 2 — The pool is often small

For Q027: pool=20 with `k_per_sub=8 × 5 strategies = 40` upper bound. Dedup pulled
the pool down by ~50%. For Q049 (E2): per-sub-query BM25 returned **0 hits in 4
of 7 sub-queries**. So the "all hits, deduped" pool is much smaller than the
`8×N` upper bound suggests — and definitely not 30.

When the pool is < 30, the slice `[:30]` is the entire pool. There is no rank
selection happening at all; everything reaches the agent. The aggregation
debate matters only when pool size > 30, which on this 9-Q subset it usually
isn't.

### Observation 3 — Confidence is hidden from the agent

Even though `_initial_retrieve` painstakingly resolves rerank scores and sorts
by confidence, the agent prompt strips them:

```
"\n".join(f"  {e.chunk_id}: {e.heading_path[:100]}" for e in initial_evidence[:30])
```

The agent sees no confidence, no relevance_to, no source_type. So the global
sort is a presentation order to the agent, but the agent has no mechanical
signal to favor higher-confidence chunks. It's left to choose by heading alone.
**This is the design flaw most directly implicated by Q027:** the agent
discarded a 10/10 rerank score with no way to know it was 10/10.

---

## 3. Alternatives the plan asked me to evaluate

### Alt A — "Top-K per sub-query, dedupe, no global re-sort" (rank-preserving)

Within each sub-query, keep ranks. Concatenate (sub_q0_rank0, sub_q0_rank1, ...,
sub_q1_rank0, ...). Dedupe by first-occurrence; the merged list interleaves
sub-queries by their per-sub rank.

Pros:
- Guarantees every sub-query gets at least its rank-0 candidate represented at
  the top of the pool, regardless of absolute confidence vs. other sub-queries.
- Robust to one sub-query producing systematically lower rerank scores (if one
  sub-question is broader, its top hit may be 5/10 while a narrow sub-question's
  top hit is 9/10 — current logic buries the broad one's top hit).

Cons:
- Loses comparative quality signal. A sub-query that's a near-duplicate of
  another can't be distinguished.
- Doesn't solve the c1921 case — c1921 was already #1.

**Verdict:** would help cases where a sub-query produces relevant-but-lower-
scoring chunks that get drowned out. Q027 isn't that case.

### Alt B — "Top-K per sub-query, dedupe, global re-sort with sub-query rank as tiebreaker"

Sort primarily by confidence; break ties by per-sub rank (lower is better).

Pros:
- Equal-confidence ties (the rerank score being 0–10 integer-quantized means
  many ties happen — see E1 output: 8.000, 8.000, 8.000, 8.000 at ranks 2–5)
  are broken by which sub-query thought the chunk was most relevant.

Cons:
- Without surfacing the tiebreaker to the agent, this only changes ordering
  inside groups, not what makes the cut.

**Verdict:** marginal improvement on the integer-tie issue (which is real:
rerank scores are integers 0–10). But still doesn't address the Q027 mechanism.

### Alt C — Current logic ("all hits, dedupe, global sort by confidence")

Status quo. Rank-blind across sub-queries.

Pros:
- Simple and predictable. The ordering is purely "best rerank wins".
- For corpora where a sub-question genuinely has the strongest match in absolute
  terms, the strongest match leads.

Cons:
- A sub-question that's slightly narrower or that the rerank model "likes" can
  monopolize the top of the pool. If pool > 30, narrower sub-questions' top hits
  lose the slot to broader sub-questions' second hits.

**Verdict:** what we have. E1 says it's serving Q027 correctly. E2 says the pool
is so small that ordering rarely matters.

---

## 4. The alternative the plan didn't ask about, but that E1 surfaces

**Surface confidence and relevance_to to the agent.** Replace:

```
"  {chunk_id}: {heading_path}"
```

with:

```
"  c{chunk_id} [conf={confidence:.1f} | from-sq={sub_idx}] {heading_path}"
```

This changes nothing in `_initial_retrieve` itself. It changes what the agent
sees. With c1921's score=10.0 visible, the agent has a mechanical reason to
keep it; right now it doesn't.

This isn't an aggregation-logic change — it's a presentation change. But it's
the smallest-blast-radius change directly motivated by E1's finding. It costs:

- ~3 lines in `_reason_and_gap_fill` (the line at 452-453)
- a corresponding nudge in REASON_PROMPT to mention "conf is the rerank score
  (0=worst, 10=best); be slow to drop high-conf chunks"

The risk is that the agent will **over**-anchor on confidence and miss
relevant lower-scoring chunks. That's a tunable problem; under-anchoring (the
current state) is a structural problem.

---

## 5. A second alternative the plan didn't ask about

**Replace agent curation entirely with deterministic top-N.** Set
`final_chunk_ids = [e.chunk_id for e in initial_evidence[:target_evidence]]`
and skip the agent loop's curation step.

This is what `_reason_and_gap_fill` falls back to when JSON parsing fails (line
514). The fallback works.

The justification for the agent loop is "the planner only ran one query per
sub-question, so it almost certainly missed relevant chunks. You MUST call
hybrid_search at least 2-3 times..." — but the **gap-filling** part of the
agent's job is independent from the **curation** part. We could let the agent
gap-fill (call extra `hybrid_search`s) and then **append** new high-scoring
chunks to the deterministic top-N, instead of letting the agent rewrite the
list.

Pros:
- Makes the deterministic ranker authoritative. If rerank says c1921 is 10/10,
  c1921 is in the cite set, full stop.
- Agent still adds value via gap-filling new chunks the planner missed.

Cons:
- Removes the agent's ability to drop low-quality chunks the rerank scored too
  high. (Rare in observed data.)
- Couples the cite list to rerank quality, which is a single-model dependency.

**Verdict:** this is a more invasive change than the presentation tweak, but
it's a much stronger fix to the Q027-class failure. Either way, Q027 doesn't
get fixed by tweaking aggregation.

---

## 6. Recommendation

The plan asked for a recommendation on `_initial_retrieve` aggregation logic.

**Recommendation: leave `_initial_retrieve` alone.**

Justifications:
1. E1 shows the function ranked the answer chunk correctly. Aggregation isn't
   the failure point.
2. E2 shows the pool size is structurally small (often < 30), so the global-
   sort vs rank-preserving debate is mostly academic on this benchmark.
3. The integer-tie issue from rerank scores (0–10 integers) is real but small;
   adding sub-query rank as a tiebreaker is a 3-line change with low risk, low
   benefit, and no clear evidence it would have helped any of the 9 questions
   we've been studying.

**Where leverage actually is:**
- **High-priority, low-blast-radius:** surface `confidence` (and optionally
  `relevance_to`) to the agent in the REASON_PROMPT. Reverses the c1921 dropout
  signal-loss directly.
- **Higher-priority, higher-blast-radius:** replace agent curation with
  deterministic top-N + agent-appended gap-fill. Makes rerank authoritative.

Both depend on the E3 noise-floor result. If Q027 is a 1/3 incorrect (one-time
noise), neither is justified yet. If it's 3/3 incorrect, the surfacing change
should be the first thing tried because it's the smallest one consistent with
E1's mechanism (curation, not aggregation).

---

## 7. Things this critique deliberately does NOT claim

- Does NOT claim the rank-blind global sort is *bad*. It works for this
  benchmark. The c1921 failure is downstream.
- Does NOT recommend implementing A2 (force-include top-K per sub-query).
  E1 confirmed this would have no effect on Q027 — c1921 was already top of
  the pool.
- Does NOT recommend A (filter-fallback ladder). Per the plan, that's a
  retrieval-side fix; this critique is about aggregation logic and curation.
