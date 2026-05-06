"""Hybrid retriever for the docs-monitor RAG layer.

Pipeline (the "optimal" SOTA path):

  query
    ├──► (optional) query expansion → 3 paraphrases via call_claude()
    ├──► (optional) HyDE → hypothetical answer paragraph via call_claude()
    ├──► embed all variants (cached after first use)
    │
    ├──► BM25 search (FTS5 MATCH on content+summary+heading_path) → top-K_bm25
    ├──► Dense cosine on raw vectors → top-K_dense
    ├──► Dense cosine on summary vectors → top-K_summary
    │
    ├──► Reciprocal Rank Fusion (k=60) → top-50 fused
    ├──► (optional) Cross-encoder rerank → top-K
    └──► Return RetrievalHit[] with provenance

RRF beats weighted fusion on small corpora and is parameter-free. It uses
each retriever's *rank*, not score, so we never need to calibrate BM25
scores against cosine similarities.

Reranker default: Claude (Opus, structured 0-10 score). Slowest but highest
quality and most aligned with the "learn Anthropic" goal. Voyage rerank-2
and local cross-encoder are alternatives.

Filters compose with retrieval — pre-filtered IDs are intersected with
retriever results, so BM25 and dense search still operate on the filtered
subset. SQLite makes this trivially fast on the small corpus.
"""

from __future__ import annotations

import json
import os
import sys
from dataclasses import dataclass, field

import numpy as np

from doc_index import DocIndex, Chunk
from embedding_cache import EmbeddingCache

RRF_K = 60  # standard reciprocal rank fusion constant


def _vprint(msg: str) -> None:
    if os.environ.get("DOCS_MONITOR_RETRIEVAL_VERBOSE") == "1":
        print(f"[retriever] {msg}", file=sys.stderr)


def _canonicalize_query(q: str) -> str:
    return ' '.join(q.lower().strip().rstrip("?.!,;:").split())


@dataclass
class RetrievalHit:
    chunk_id: int
    source_type: str
    source_id: str
    heading_path: str
    content: str
    summary: str | None
    url: str | None
    metadata: dict
    score_bm25: float = 0.0
    score_dense: float = 0.0
    score_summary: float = 0.0
    score_rerank: float | None = None
    rrf_rank: int = 0
    line_start: int | None = None
    line_end: int | None = None

    @classmethod
    def from_chunk(cls, c: Chunk) -> "RetrievalHit":
        return cls(
            chunk_id=c.id or 0,
            source_type=c.source_type,
            source_id=c.source_id,
            heading_path=c.heading_path,
            content=c.content,
            summary=c.summary,
            url=c.url,
            metadata=c.metadata,
            line_start=c.line_start,
            line_end=c.line_end,
        )

    def to_dict(self) -> dict:
        d = {
            "chunk_id": self.chunk_id,
            "source_type": self.source_type,
            "source_id": self.source_id,
            "heading_path": self.heading_path,
            "url": self.url,
            "metadata": self.metadata,
            "line_start": self.line_start,
            "line_end": self.line_end,
            "scores": {
                "bm25": self.score_bm25,
                "dense": self.score_dense,
                "summary": self.score_summary,
                "rerank": self.score_rerank,
            },
            "rrf_rank": self.rrf_rank,
        }
        snippet = self.content[:400]
        if len(self.content) > 400:
            snippet += "..."
        d["snippet"] = snippet
        return d


@dataclass
class _DenseIndex:
    """In-memory dense vector matrix for fast cosine search."""
    chunk_ids: list[int] = field(default_factory=list)
    matrix: np.ndarray | None = None  # (N, dims) float32, L2-normalized
    norm_lookup: dict[int, int] = field(default_factory=dict)  # chunk_id -> row idx


class HybridRetriever:
    """BM25 ⊕ dense ⊕ RRF ⊕ rerank."""

    def __init__(
        self,
        index: DocIndex,
        embedder: EmbeddingCache,
    ):
        self.index = index
        self.embedder = embedder
        self._dense_content: _DenseIndex | None = None
        self._dense_summary: _DenseIndex | None = None

    # ── Public API ──────────────────────────────────────────────────────────

    def retrieve(
        self,
        query: str,
        *,
        source_type: str | list[str] | None = None,
        filters: dict | None = None,
        k: int = 10,
        k_bm25: int = 50,
        k_dense: int = 50,
        expand_query: bool = False,
        use_hyde: bool = False,
        rerank: bool = True,
        rerank_backend: str = "claude",
        # Dedup default OFF: paraphrase-test data showed it hurts chunk-level
        # Jaccard slightly (0.269 → 0.319 with dedup off). Implementation is
        # retained for future KG-node extraction (where collapsing near-duplicate
        # chunks is the right primitive). Opt in via --dedup or dedup=True.
        dedup: bool = False,
        dedup_threshold: float = 0.92,
        max_per_source: int = 3,
    ) -> list[RetrievalHit]:
        """Run the full hybrid retrieval pipeline."""
        if not query.strip():
            return []

        # Build candidate-set filter (chunk_ids matching metadata filters)
        allowed_ids: set[int] | None = None
        if filters or source_type:
            filter_args = dict(filters or {})
            if source_type and "source_type" not in filter_args:
                filter_args["source_type"] = source_type

            if "date" in filter_args:
                d = filter_args.pop("date")
                filter_args.setdefault("since", d)
                filter_args.setdefault("until", d)

            _ALLOWED = {"source_type", "category", "severity", "page", "since", "until", "tags"}
            unknown = [k for k in filter_args if k not in _ALLOWED]
            for k in unknown:
                _vprint(f"dropping unknown filter key {k!r}={filter_args[k]!r}")
                del filter_args[k]

            allowed_ids = self.index.filter_chunk_ids(**filter_args)
            if not allowed_ids:
                _vprint(f"filters yielded zero candidates")
                return []

        # Build query variants (always include the original query)
        variants = [query]
        if expand_query:
            variants.extend(self._expand_query(query))
        if use_hyde:
            hyde_doc = self._hyde(query)
            if hyde_doc:
                variants.append(hyde_doc)

        _vprint(f"query variants: {len(variants)}")

        # Run BM25 across all variants. Fuse by MAX across variants:
        # keep the strongest single-variant score for each chunk, accepting
        # paraphrase stochasticity as the trade-off. Mean-fusion was tried
        # but dampened the strongest evidence — see HONEST_ASSESSMENT for
        # the regression that motivated rolling back.
        bm25_scores: dict[int, float] = {}
        for v in variants:
            for chunk_id, score in self.index.fts_search(
                v, limit=k_bm25, source_type=source_type
            ):
                if allowed_ids is not None and chunk_id not in allowed_ids:
                    continue
                bm25_scores[chunk_id] = max(bm25_scores.get(chunk_id, 0.0), score)

        # Embed query variants once
        query_vectors = self.embedder.embed(variants)

        # Dense search on raw content vectors — max-fuse across variants
        self._ensure_dense(use_summary=False)
        dense_scores: dict[int, float] = {}
        if self._dense_content and self._dense_content.matrix is not None:
            for qv in query_vectors:
                for chunk_id, score in self._cosine_topk(
                    self._dense_content, qv, k_dense, allowed_ids
                ):
                    dense_scores[chunk_id] = max(dense_scores.get(chunk_id, 0.0), score)

        # Dense search on summary vectors (multi-representation) — max-fuse
        self._ensure_dense(use_summary=True)
        summary_scores: dict[int, float] = {}
        if self._dense_summary and self._dense_summary.matrix is not None:
            for qv in query_vectors:
                for chunk_id, score in self._cosine_topk(
                    self._dense_summary, qv, k_dense, allowed_ids
                ):
                    summary_scores[chunk_id] = max(summary_scores.get(chunk_id, 0.0), score)

        _vprint(
            f"candidates: bm25={len(bm25_scores)}, dense={len(dense_scores)}, "
            f"summary={len(summary_scores)}"
        )

        # RRF fusion
        fused = _reciprocal_rank_fusion(
            [bm25_scores, dense_scores, summary_scores], k_rrf=RRF_K
        )
        # Take top 50 for reranking (over-retrieve)
        fused_ids = [cid for cid, _ in fused[:50]]
        if not fused_ids:
            return []

        # Per-source diversity: prevent any single source_id from monopolizing top-K.
        # Preserve RRF order while capping each source to max_per_source. Default 3
        # is a balance: high enough that a deep single-doc query still gets coverage,
        # low enough to force cross-source spread on multi-doc questions like Q036.
        if max_per_source > 0 and max_per_source < len(fused_ids):
            per_source: dict[str, int] = {}
            capped_ids: list[int] = []
            for cid in fused_ids:
                chunk = self.index.get_chunk(cid)
                if not chunk:
                    continue
                sid = chunk.source_id
                if per_source.get(sid, 0) >= max_per_source:
                    continue
                per_source[sid] = per_source.get(sid, 0) + 1
                capped_ids.append(cid)
            fused_ids = capped_ids
            _vprint(f"after diversity cap (≤{max_per_source}/source): {len(fused_ids)}")

        # Semantic dedup: collapse near-duplicate chunks to the highest-RRF
        # representative. Same fact stated in two sections of the corpus
        # shouldn't dilute top-k. Threshold conservative; --no-dedup to skip.
        # (Same primitive will later extract KG nodes.)
        if dedup and len(fused_ids) > 1:
            fused_ids = self._semantic_dedup(fused_ids, threshold=dedup_threshold)
            _vprint(f"after dedup: {len(fused_ids)} candidates "
                    f"(threshold={dedup_threshold})")

        # Materialize hits
        hits: list[RetrievalHit] = []
        for rank, chunk_id in enumerate(fused_ids):
            chunk = self.index.get_chunk(chunk_id)
            if not chunk:
                continue
            hit = RetrievalHit.from_chunk(chunk)
            hit.score_bm25 = bm25_scores.get(chunk_id, 0.0)
            hit.score_dense = dense_scores.get(chunk_id, 0.0)
            hit.score_summary = summary_scores.get(chunk_id, 0.0)
            hit.rrf_rank = rank
            hits.append(hit)

        # Rerank
        if rerank and hits:
            try:
                hits = self._rerank(query, hits, backend=rerank_backend)
            except Exception as e:
                _vprint(f"rerank failed, falling back to RRF order: {e!r}")

        return hits[:k]

    def find_similar(self, chunk_id: int, k: int = 10) -> list[RetrievalHit]:
        """Find chunks most similar to a given chunk (uses its content vector)."""
        chunk = self.index.get_chunk(chunk_id)
        if not chunk:
            return []
        # Use the chunk's existing embedding (cache hit)
        qv = self.embedder.embed_query(chunk.content)
        self._ensure_dense(use_summary=False)
        if not self._dense_content or self._dense_content.matrix is None:
            return []
        results = self._cosine_topk(self._dense_content, qv, k + 1, None)
        # Drop self
        out = []
        for cid, score in results:
            if cid == chunk_id:
                continue
            c = self.index.get_chunk(cid)
            if not c:
                continue
            hit = RetrievalHit.from_chunk(c)
            hit.score_dense = score
            out.append(hit)
            if len(out) >= k:
                break
        return out

    def invalidate_dense_cache(self) -> None:
        """Reset cached vector matrices. Call after reindexing."""
        self._dense_content = None
        self._dense_summary = None

    # ── Semantic dedup ──────────────────────────────────────────────────────

    def _semantic_dedup(
        self, candidate_ids: list[int], threshold: float = 0.92,
    ) -> list[int]:
        """Greedy near-duplicate collapse on a list of chunk_ids.

        Iterates candidates in their input order (RRF-rank order). For each,
        computes cosine vs all already-kept representatives; if max similarity
        exceeds ``threshold``, the candidate is dropped (subsumed by the
        higher-ranked representative). Otherwise it joins the kept set.

        Returns ids in original order, with duplicates removed. If a candidate
        has no cached vector (e.g. embedding cache miss), it passes through
        unchanged — better to keep an unverified chunk than drop it.
        """
        if not candidate_ids:
            return []
        # Pull vectors for all candidates from the dense_content matrix
        self._ensure_dense(use_summary=False)
        if not self._dense_content or self._dense_content.matrix is None:
            return candidate_ids
        idx_of = self._dense_content.norm_lookup
        matrix = self._dense_content.matrix

        kept_ids: list[int] = []
        kept_vecs: list = []  # numpy arrays
        for cid in candidate_ids:
            row = idx_of.get(cid)
            if row is None:
                # No vector cached — pass through (don't risk dropping)
                kept_ids.append(cid)
                continue
            v = matrix[row]
            v_norm = float(np.linalg.norm(v))
            if v_norm < 1e-9:
                kept_ids.append(cid)
                continue
            duplicate = False
            for kv in kept_vecs:
                kv_norm = float(np.linalg.norm(kv))
                if kv_norm < 1e-9:
                    continue
                sim = float(np.dot(v, kv) / (v_norm * kv_norm))
                if sim >= threshold:
                    duplicate = True
                    break
            if not duplicate:
                kept_ids.append(cid)
                kept_vecs.append(v)
        return kept_ids

    # ── Query expansion ─────────────────────────────────────────────────────

    def _expand_query(self, query: str) -> list[str]:
        """Generate 3 paraphrases via call_claude()."""
        from llm_backend import call_claude
        prompt = (
            "Generate 3 paraphrases of the user's question that use different "
            "vocabulary. Each paraphrase should preserve the question's intent "
            "but reword it as a developer might phrase it. Output one paraphrase "
            "per line. No numbering, no preamble, no quotes. If the input is "
            "already very specific (e.g. an exact identifier), output the input "
            "unchanged for the first line and add 2 broader rephrasings."
        )
        try:
            raw = call_claude(
                prompt=prompt, stdin=query, model="haiku",
                max_tokens=200, timeout=20,
            )
        except Exception as e:
            _vprint(f"query expansion failed: {e!r}")
            return []
        out = [line.strip() for line in raw.splitlines() if line.strip()]
        return out[:3]

    def _hyde(self, query: str) -> str | None:
        """HyDE: generate a hypothetical answer paragraph to use as the dense query."""
        from llm_backend import call_claude
        prompt = (
            "Write a 2-3 sentence hypothetical answer to the user's question, "
            "as if you had perfect knowledge from the documentation. Use "
            "vocabulary the documentation likely uses. Be specific and concrete. "
            "No preamble, no caveats — just the hypothetical answer."
        )
        try:
            return call_claude(
                prompt=prompt, stdin=query, model="haiku",
                max_tokens=200, timeout=20,
            ).strip()
        except Exception as e:
            _vprint(f"HyDE failed: {e!r}")
            return None

    # ── Dense search ────────────────────────────────────────────────────────

    def _ensure_dense(self, use_summary: bool) -> None:
        """Lazy-load and cache the dense matrix for content or summary embeddings."""
        attr = "_dense_summary" if use_summary else "_dense_content"
        if getattr(self, attr) is not None:
            return

        rows = self.index._conn.execute(
            "SELECT id, content, summary FROM doc_chunks ORDER BY id"
        ).fetchall()

        chunk_ids: list[int] = []
        texts: list[str] = []
        for r in rows:
            text = (r["summary"] if use_summary else r["content"]) or ""
            if not text.strip():
                continue
            chunk_ids.append(int(r["id"]))
            texts.append(text)

        if not chunk_ids:
            setattr(self, attr, _DenseIndex())
            return

        # All these should be cache hits if reindex+embed was done
        vectors = self.embedder.embed(texts)
        if not vectors:
            setattr(self, attr, _DenseIndex())
            return

        dims = vectors[0].shape[0]
        matrix = np.zeros((len(vectors), dims), dtype=np.float32)
        for i, v in enumerate(vectors):
            if v.shape[0] != dims:
                # Defensive: skip mismatched
                continue
            norm = np.linalg.norm(v)
            if norm > 0:
                matrix[i] = v / norm
            else:
                matrix[i] = v

        idx = _DenseIndex(
            chunk_ids=chunk_ids,
            matrix=matrix,
            norm_lookup={cid: i for i, cid in enumerate(chunk_ids)},
        )
        setattr(self, attr, idx)
        _vprint(
            f"loaded {'summary' if use_summary else 'content'} dense matrix: "
            f"shape={matrix.shape}"
        )

    def _cosine_topk(
        self,
        idx: _DenseIndex,
        query_vec: np.ndarray,
        k: int,
        allowed_ids: set[int] | None,
    ) -> list[tuple[int, float]]:
        """Cosine similarity top-k via matrix multiply on L2-normalized vectors."""
        if idx.matrix is None or len(idx.chunk_ids) == 0:
            return []
        # Normalize query
        q = query_vec.astype(np.float32, copy=False)
        norm = np.linalg.norm(q)
        if norm > 0:
            q = q / norm
        # Dimension mismatch (e.g., model rotation): can't compare
        if q.shape[0] != idx.matrix.shape[1]:
            _vprint(
                f"dim mismatch: query={q.shape[0]} vs index={idx.matrix.shape[1]}"
            )
            return []
        scores = idx.matrix @ q  # shape (N,)
        # If filter, mask out disallowed
        if allowed_ids is not None:
            mask = np.array(
                [cid in allowed_ids for cid in idx.chunk_ids], dtype=bool
            )
            scores = np.where(mask, scores, -np.inf)
        # Top-k via argpartition
        if k >= len(scores):
            top_idx = np.argsort(-scores)
        else:
            part = np.argpartition(-scores, k)[:k]
            top_idx = part[np.argsort(-scores[part])]
        return [
            (idx.chunk_ids[i], float(scores[i]))
            for i in top_idx
            if scores[i] != -np.inf
        ]

    # ── Reranking ───────────────────────────────────────────────────────────

    def _rerank(
        self,
        query: str,
        hits: list[RetrievalHit],
        backend: str = "claude",
    ) -> list[RetrievalHit]:
        if backend == "claude":
            return self._rerank_claude(query, hits)
        if backend == "voyage":
            return self._rerank_voyage(query, hits)
        if backend == "local":
            return self._rerank_local(query, hits)
        raise ValueError(f"Unknown rerank backend: {backend}")

    def _rerank_claude(
        self, query: str, hits: list[RetrievalHit]
    ) -> list[RetrievalHit]:
        """Score each candidate 0-10 via a single batched Claude call."""
        from llm_backend import call_claude

        # Build a numbered candidate list
        items = []
        for i, h in enumerate(hits):
            snippet = h.content[:600]
            items.append(
                f"### Candidate {i}\n"
                f"Heading: {h.heading_path}\n"
                f"Content: {snippet}"
            )
        candidates_block = "\n\n".join(items)

        prompt = (
            "You are a relevance judge. For each candidate, rate how well it "
            "answers the user's question on a 0-10 integer scale "
            "(0 = irrelevant, 5 = somewhat related, 10 = directly answers). "
            "Output ONLY a JSON array of integers, one per candidate, in order. "
            "Example: [8, 3, 0, 10, 5]. No prose, no markdown."
        )
        stdin = f"Question: {_canonicalize_query(query)}\n\nCandidates:\n{candidates_block}"

        raw = call_claude(
            prompt=prompt, stdin=stdin, model="sonnet",
            max_tokens=512, timeout=60,
        )
        # Tolerate markdown fences
        cleaned = raw.strip().lstrip("`").lstrip("json").strip("`").strip()
        # Find the first JSON-array-looking substring
        start = cleaned.find("[")
        end = cleaned.rfind("]")
        if start < 0 or end < start:
            raise RuntimeError(f"reranker returned no JSON array: {raw[:200]!r}")
        try:
            scores = json.loads(cleaned[start : end + 1])
        except json.JSONDecodeError as e:
            raise RuntimeError(f"reranker JSON parse failed: {e}") from e
        if len(scores) != len(hits):
            # Pad/truncate defensively
            scores = (list(scores) + [0] * len(hits))[: len(hits)]

        for h, s in zip(hits, scores):
            try:
                h.score_rerank = float(s)
            except (TypeError, ValueError):
                h.score_rerank = 0.0
        # Sort by rerank score desc, breaking ties by RRF rank (asc)
        return sorted(
            hits,
            key=lambda h: (-(h.score_rerank or 0.0), h.rrf_rank),
        )

    def _rerank_voyage(
        self, query: str, hits: list[RetrievalHit]
    ) -> list[RetrievalHit]:
        try:
            import voyageai  # type: ignore[import-not-found,unused-ignore]
        except ImportError as e:
            raise RuntimeError(
                "Voyage rerank requires `pip install voyageai`."
            ) from e
        key = (
            os.environ.get("VOYAGE_API_KEY")
            or self.embedder.__class__.__module__  # placeholder
        )
        if not key or "module" in str(key):
            key = os.environ.get("VOYAGE_API_KEY")
        if not key:
            raise RuntimeError("VOYAGE_API_KEY not set for Voyage rerank")
        client = voyageai.Client(api_key=key)
        documents = [h.content[:1500] for h in hits]
        result = client.rerank(query=query, documents=documents,
                               model="rerank-2", top_k=len(hits))
        # result.results is a list of {index, relevance_score}
        score_by_idx = {r.index: float(r.relevance_score) for r in result.results}
        for i, h in enumerate(hits):
            h.score_rerank = score_by_idx.get(i, 0.0)
        return sorted(hits, key=lambda h: (-(h.score_rerank or 0.0), h.rrf_rank))

    def _rerank_local(
        self, query: str, hits: list[RetrievalHit]
    ) -> list[RetrievalHit]:
        try:
            from sentence_transformers import CrossEncoder  # type: ignore
        except ImportError as e:
            raise RuntimeError(
                "Local rerank requires `pip install sentence-transformers`."
            ) from e
        model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
        pairs = [(query, h.content[:1500]) for h in hits]
        scores = model.predict(pairs)
        for h, s in zip(hits, scores):
            h.score_rerank = float(s)
        return sorted(hits, key=lambda h: (-(h.score_rerank or 0.0), h.rrf_rank))


# ── Reciprocal Rank Fusion ──────────────────────────────────────────────────


def _reciprocal_rank_fusion(
    rankings: list[dict[int, float]], k_rrf: int = RRF_K
) -> list[tuple[int, float]]:
    """Fuse multiple rankings via RRF: score(d) = Σ 1 / (k + rank_i(d)).

    Each ranking is {chunk_id: score}; we convert to ranks (high score = rank 0).
    Items not in a ranking simply contribute 0 from that source.
    """
    fused: dict[int, float] = {}
    for ranking in rankings:
        if not ranking:
            continue
        sorted_ids = sorted(ranking.keys(), key=lambda c: -ranking[c])
        for rank, cid in enumerate(sorted_ids):
            fused[cid] = fused.get(cid, 0.0) + 1.0 / (k_rrf + rank + 1)
    return sorted(fused.items(), key=lambda x: -x[1])


__all__ = ["HybridRetriever", "RetrievalHit"]
