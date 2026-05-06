"""E2: BM25 vs dense top-10 Jaccard overlap on Q049 between v4.3.7 and v4.3.9.

Question: where does the ~50% pool divergence between v4.3.7 and v4.3.9 (near-
identical plans) come from — BM25 surface-form sensitivity, dense embeddings, or
both?
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent.parent.parent
sys.path.insert(0, str(REPO))

from doc_index import DocIndex
from embedding_cache import EmbeddingCache
from retriever import HybridRetriever


def load_q049_plan(run_id: str) -> dict:
    path = REPO / "data-claude/eval/runs" / run_id / "reports.jsonl"
    for line in open(path):
        row = json.loads(line)
        if row["id"] == "Q049":
            return row["report"]["report_json_data"]["plan"]
    raise RuntimeError(f"Q049 not found in {run_id}")


def main():
    plan_v37 = load_q049_plan("20260505-rag-v4.3.7")
    plan_v39 = load_q049_plan("20260505-rag-v4.3.9")

    idx = DocIndex(db_path=REPO / "data-claude/index.db")
    emb = EmbeddingCache(db_path=REPO / "data-claude/embeddings.db")
    retr = HybridRetriever(idx, emb)

    # Pre-load the dense matrix once
    retr._ensure_dense(use_summary=False)

    out_lines = []
    out_lines.append(
        "E2: BM25 vs dense top-10 Jaccard overlap on Q049 (v4.3.7 vs v4.3.9)"
    )
    out_lines.append("=" * 72)
    out_lines.append("")
    out_lines.append("Per sub-query: top-10 chunk_id sets, Jaccard overlap = |A∩B| / |A∪B|")
    out_lines.append("(filter: source_type='page' to match --scope docs)")
    out_lines.append("")

    n = min(len(plan_v37["search_strategies"]), len(plan_v39["search_strategies"]))
    bm25_overlaps = []
    dense_overlaps = []

    for s_v37, s_v39 in zip(plan_v37["search_strategies"], plan_v39["search_strategies"]):
        sub_idx = s_v37.get("sub_question_index", "?")
        q_v37 = s_v37.get("search_query", "")
        q_v39 = s_v39.get("search_query", "")
        if s_v39.get("sub_question_index") != sub_idx:
            out_lines.append(
                f"WARN: sub-index mismatch v37={sub_idx} v39={s_v39.get('sub_question_index')}"
            )

        # BM25 only
        bm25_v37 = [cid for cid, _ in idx.fts_search(q_v37, source_type="page", limit=10)]
        bm25_v39 = [cid for cid, _ in idx.fts_search(q_v39, source_type="page", limit=10)]

        # Dense only on raw content (page-only)
        # Need allowed_ids = chunks with source_type='page'
        page_ids = set(idx.filter_chunk_ids(source_type="page"))
        qv_v37 = retr.embedder.embed_query(q_v37)
        qv_v39 = retr.embedder.embed_query(q_v39)
        dense_v37 = [cid for cid, _ in retr._cosine_topk(retr._dense_content, qv_v37, 10, page_ids)]
        dense_v39 = [cid for cid, _ in retr._cosine_topk(retr._dense_content, qv_v39, 10, page_ids)]

        # Jaccard
        def jaccard(a, b):
            sa, sb = set(a), set(b)
            return len(sa & sb) / max(1, len(sa | sb))

        bm25_j = jaccard(bm25_v37, bm25_v39)
        dense_j = jaccard(dense_v37, dense_v39)
        bm25_overlaps.append(bm25_j)
        dense_overlaps.append(dense_j)

        out_lines.append(f"--- SQ{sub_idx} ---")
        out_lines.append(f"  v37 query: {q_v37}")
        out_lines.append(f"  v39 query: {q_v39}")
        out_lines.append(f"  BM25  v37 top-10: {bm25_v37}")
        out_lines.append(f"  BM25  v39 top-10: {bm25_v39}")
        out_lines.append(f"  BM25  Jaccard: {bm25_j:.2f}  (intersection={sorted(set(bm25_v37) & set(bm25_v39))})")
        out_lines.append(f"  dense v37 top-10: {dense_v37}")
        out_lines.append(f"  dense v39 top-10: {dense_v39}")
        out_lines.append(f"  dense Jaccard: {dense_j:.2f}  (intersection={sorted(set(dense_v37) & set(dense_v39))})")
        out_lines.append("")

    avg_b = sum(bm25_overlaps) / len(bm25_overlaps)
    avg_d = sum(dense_overlaps) / len(dense_overlaps)
    out_lines.append("=" * 72)
    out_lines.append(f"AVERAGE Jaccard (per-SQ mean across {len(bm25_overlaps)} sub-queries):")
    out_lines.append(f"  BM25:  {avg_b:.2f}")
    out_lines.append(f"  dense: {avg_d:.2f}")

    output = "\n".join(out_lines)
    out_path = REPO / "data-claude/eval/runs/20260506-rag-v4.3.10/E2_q049_bm25_vs_dense.txt"
    out_path.write_text(output)
    print(output)
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
