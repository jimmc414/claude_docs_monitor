"""E1: Reconstruct Q027's initial_evidence in v4.3.9.

Did c1921 reach the agent's initial_evidence[:30]?
- If yes  -> agent curation is the mechanism
- If no   -> cross-sub-query aggregation is the mechanism
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent.parent.parent
sys.path.insert(0, str(REPO))

from doc_index import DocIndex
from embedding_cache import EmbeddingCache
from retriever import HybridRetriever
from report_builder import _initial_retrieve


def main():
    # 1. Load v4.3.9's actual Q027 plan
    plan = None
    path = REPO / "data-claude/eval/runs/20260505-rag-v4.3.9/reports.jsonl"
    for line in open(path):
        row = json.loads(line)
        if row["id"] == "Q027":
            plan = row["report"]["report_json_data"]["plan"]
            break
    if plan is None:
        raise RuntimeError("Q027 plan not found")

    print(f"Loaded Q027 plan: {len(plan['sub_questions'])} sub-questions, "
          f"{len(plan['search_strategies'])} strategies")

    # 2. Set up retriever (same DBs as the run)
    idx = DocIndex(db_path=REPO / "data-claude/index.db")
    emb = EmbeddingCache(db_path=REPO / "data-claude/embeddings.db")
    retr = HybridRetriever(idx, emb)

    # 3. Reproduce the v4.3.9 run's parameters:
    #    - run launched: claude_docs_monitor.py report Q --scope docs --max-turns 4 --model sonnet
    #    - --scope docs maps to scope=['page'] in cmd_report (claude_docs_monitor.py:2278-2283)
    #    - default since/until = None
    #    - default k_per_sub = 8
    scope = ["page"]
    since = None
    until = None
    k_per_sub = 8

    # 4. Run _initial_retrieve
    initial = _initial_retrieve(plan, retr, scope=scope, since=since, until=until,
                                k_per_sub=k_per_sub)

    # 5. Output
    out_lines = []
    out_lines.append("E1: Reconstruction of v4.3.9 Q027 _initial_retrieve")
    out_lines.append("=" * 72)
    out_lines.append("")
    out_lines.append(f"Plan: 5 sub-questions, 5 strategies")
    out_lines.append(f"Run config: scope=['page'], since=None, until=None, k_per_sub=8, rerank=True")
    out_lines.append("")
    out_lines.append(f"Pool size (deduped, sorted by confidence): {len(initial)}")
    out_lines.append("")
    out_lines.append("--- top-30 ---")
    chunk_ids_top30 = []
    for i, e in enumerate(initial[:30]):
        out_lines.append(
            f"{i+1:2d}. c{e.chunk_id:<5d} src={e.source_type:<13s} conf={e.confidence:.3f} "
            f"{(e.heading_path or '')[:80]}"
        )
        chunk_ids_top30.append(e.chunk_id)
    out_lines.append("")
    out_lines.append("=" * 72)
    has_1921 = 1921 in chunk_ids_top30
    out_lines.append(f"c1921 in top-30: {has_1921}")
    pos_1921 = None
    for i, e in enumerate(initial):
        if e.chunk_id == 1921:
            pos_1921 = i + 1
            break
    if pos_1921:
        out_lines.append(f"c1921 in pool at position: {pos_1921} (of {len(initial)})")
        for e in initial:
            if e.chunk_id == 1921:
                out_lines.append(f"c1921 details: src={e.source_type} conf={e.confidence:.3f} "
                                 f"heading={e.heading_path}")
                out_lines.append(f"c1921 relevance_to: {e.relevance_to}")
                break
    else:
        out_lines.append("c1921 NOT in pool at all (any sub-query)")

    out_lines.append("")
    out_lines.append("Branch outcomes from plan:")
    if has_1921:
        out_lines.append("  -> c1921 in top-30: AGENT CURATION is the mechanism.")
        out_lines.append("     A2 (force-include top-K per sub-query) wouldn't help.")
    else:
        if pos_1921:
            out_lines.append(f"  -> c1921 NOT in top-30 (at pos {pos_1921}): AGGREGATION is the mechanism.")
            out_lines.append("     A2 is the right fix.")
        else:
            out_lines.append("  -> c1921 NOT in pool at all: retrieval-layer issue, not aggregation.")
            out_lines.append("     A2 wouldn't help either; the issue is upstream (BM25/dense/rerank).")

    output = "\n".join(out_lines)
    out_path = REPO / "data-claude/eval/runs/20260506-rag-v4.3.10/E1_reconstruction.txt"
    out_path.write_text(output)
    print(output)
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
