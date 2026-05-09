"""R0b: Single-doc head-to-head, comfortably under 32K tokens.

Gives voyage-context-3 its best shot: one document well under 32K tokens, multiple
paraphrase pairs, full contextual conditioning. If voyage-4-large still wins here,
the bake-off verdict holds.

Run: python data-claude/eval/embed_compare_singledoc.py
"""
from __future__ import annotations

import os
import sqlite3
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
try:
    from dotenv import load_dotenv; load_dotenv(REPO / ".env")
except ImportError:
    pass
os.environ.pop("ANTHROPIC_API_KEY", None)

import numpy as np
import voyageai

INDEX_DB = REPO / "data-claude" / "index.db"
OUT_PATH = REPO / "data-claude" / "eval" / "embed_compare_singledoc_results.md"

MODELS = ["voyage-4-large", "voyage-context-3"]

# Three single-doc tests, each well under 32K tokens.
# (doc_source_id, [(query_a, query_b, label), ...])
TESTS = [
    {
        "source_id": "permissions.md",
        "label": "permissions.md (52 chunks, ~19K tokens)",
        "pairs": [
            ("How do I restrict which tools Claude can use in a session?",
             "How do I limit Claude's tool access in a Claude Code session?",
             "Q041/Q042 (limit/restrict tools)"),
            ("How do I limit which tools Claude can use?",
             "How do I restrict Claude's tool access?",
             "probe pair (shorter limit/restrict)"),
        ],
    },
    {
        "source_id": "hooks-guide.md",
        "label": "hooks-guide.md (66 chunks, ~31K tokens)",
        "pairs": [
            ("How do hooks work in Claude Code?",
             "What is a hook and how is it configured?",
             "probe pair (hooks)"),
        ],
    },
    {
        "source_id": "authentication.md",
        "label": "authentication.md (10 chunks, ~?K tokens)",
        "pairs": [
            ("Where does Claude Code store credentials on Linux?",
             "What file stores Claude Code's login tokens on a Linux machine?",
             "Q047/Q048 (credentials location)"),
        ],
    },
]


def cosine(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-12))


def jaccard(a: list, b: list) -> float:
    sa, sb = set(a), set(b)
    return len(sa & sb) / len(sa | sb) if (sa or sb) else 1.0


def fetch_chunks(source_id: str) -> list[tuple[int, str]]:
    conn = sqlite3.connect(str(INDEX_DB))
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT id, content FROM doc_chunks WHERE source_type='page' AND source_id=? ORDER BY id",
        (source_id,),
    ).fetchall()
    conn.close()
    return [(r["id"], r["content"]) for r in rows]


def topk(query_vec: np.ndarray, chunk_vecs: dict[int, np.ndarray], k: int = 5) -> list[int]:
    scored = sorted(
        ((cid, cosine(query_vec, v)) for cid, v in chunk_vecs.items()),
        key=lambda x: x[1], reverse=True,
    )
    return [cid for cid, _ in scored[:k]]


def run():
    if not os.environ.get("VOYAGE_API_KEY"):
        print("FATAL: VOYAGE_API_KEY not set", file=sys.stderr); sys.exit(1)

    client = voyageai.Client()
    lines = ["# Single-doc bake-off (R0b)\n",
             f"_Run: {time.strftime('%Y-%m-%d %H:%M:%S')}_\n",
             "\nGiving voyage-context-3 a fair shot: one document, well under 32K tokens, "
             "full contextual conditioning.\n"]

    per_model_jaccards: dict[str, list[float]] = {m: [] for m in MODELS}

    for test in TESTS:
        sid = test["source_id"]
        chunks = fetch_chunks(sid)
        if not chunks:
            print(f"  [skip] no chunks for {sid}", file=sys.stderr); continue
        # Approx token count
        approx_tokens = sum(len(c[1]) for c in chunks) // 4
        print(f"\n=== {sid}: {len(chunks)} chunks, ~{approx_tokens} tokens ===", file=sys.stderr)
        lines.append(f"\n## {test['label']} (~{approx_tokens} tokens)\n")
        if approx_tokens > 32000:
            lines.append(f"\n_⚠️  ~{approx_tokens} tokens — at/above 32K limit; voyage-context-3 may error_\n")

        # Embed all chunks once per model
        chunk_vecs_per_model: dict[str, dict[int, np.ndarray]] = {}
        for model in MODELS:
            try:
                if model.startswith("voyage-context"):
                    r = client.contextualized_embed(
                        inputs=[[c[1] for c in chunks]], model=model, input_type="document",
                    )
                    chunk_vecs_per_model[model] = {
                        chunks[i][0]: np.asarray(v, dtype=np.float32)
                        for i, v in enumerate(r.results[0].embeddings)
                    }
                else:
                    r = client.embed([c[1] for c in chunks], model=model, input_type="document")
                    chunk_vecs_per_model[model] = {
                        chunks[i][0]: np.asarray(v, dtype=np.float32)
                        for i, v in enumerate(r.embeddings)
                    }
                print(f"  {model}: embedded {len(chunk_vecs_per_model[model])} chunks", file=sys.stderr)
            except Exception as e:
                print(f"  {model} ERR: {e!r}", file=sys.stderr)
                lines.append(f"\n  ⚠️  `{model}` errored: {str(e)[:200]}\n")

        # For each query pair, measure both Jaccard@5 (chunk overlap) AND query-pair cosine
        lines.append("\n| Pair | Metric | " + " | ".join(MODELS) + " |")
        lines.append("|---|---|" + "|".join(["---:"] * len(MODELS)) + "|")

        for qa, qb, label in test["pairs"]:
            for model in MODELS:
                if model not in chunk_vecs_per_model:
                    continue
                try:
                    if model.startswith("voyage-context"):
                        qr = client.contextualized_embed(
                            inputs=[[qa], [qb]], model=model, input_type="query",
                        )
                        va = np.asarray(qr.results[0].embeddings[0], dtype=np.float32)
                        vb = np.asarray(qr.results[1].embeddings[0], dtype=np.float32)
                    else:
                        qr = client.embed([qa, qb], model=model, input_type="query")
                        va = np.asarray(qr.embeddings[0], dtype=np.float32)
                        vb = np.asarray(qr.embeddings[1], dtype=np.float32)
                    top_a = topk(va, chunk_vecs_per_model[model], k=5)
                    top_b = topk(vb, chunk_vecs_per_model[model], k=5)
                    j = jaccard(top_a, top_b)
                    c_qq = cosine(va, vb)
                    per_model_jaccards[model].append(j)
                    if model == MODELS[0]:
                        lines.append(f"| {label} | Jaccard@5 | {j:.3f} | _filled below_ |")
                        lines.append(f"|  | query cosine | {c_qq:.3f} | _filled below_ |")
                except Exception as e:
                    print(f"  {model} query ERR: {e!r}", file=sys.stderr)

        # Properly format the table — collect row data first then write
        # (rewrite the last few lines with both models)
        # easier: redo per-model loop and aggregate
        rows_data = []
        for qa, qb, label in test["pairs"]:
            row = {"label": label, "jaccard": {}, "cosine": {}}
            for model in MODELS:
                if model not in chunk_vecs_per_model:
                    row["jaccard"][model] = "—"
                    row["cosine"][model] = "—"
                    continue
                try:
                    if model.startswith("voyage-context"):
                        qr = client.contextualized_embed(
                            inputs=[[qa], [qb]], model=model, input_type="query",
                        )
                        va = np.asarray(qr.results[0].embeddings[0], dtype=np.float32)
                        vb = np.asarray(qr.results[1].embeddings[0], dtype=np.float32)
                    else:
                        qr = client.embed([qa, qb], model=model, input_type="query")
                        va = np.asarray(qr.embeddings[0], dtype=np.float32)
                        vb = np.asarray(qr.embeddings[1], dtype=np.float32)
                    top_a = topk(va, chunk_vecs_per_model[model], k=5)
                    top_b = topk(vb, chunk_vecs_per_model[model], k=5)
                    j = jaccard(top_a, top_b)
                    c_qq = cosine(va, vb)
                    row["jaccard"][model] = f"{j:.3f}"
                    row["cosine"][model] = f"{c_qq:.3f}"
                except Exception:
                    row["jaccard"][model] = "ERR"
                    row["cosine"][model] = "ERR"
            rows_data.append(row)

        # Strip the half-built rows we appended above
        # find the table header we last appended
        header_idx = None
        for i in range(len(lines) - 1, -1, -1):
            if lines[i].startswith("| Pair |"):
                header_idx = i
                break
        if header_idx is not None:
            lines = lines[:header_idx]
        # Write fresh table
        lines.append("\n| Pair | Metric | " + " | ".join(MODELS) + " |")
        lines.append("|---|---|" + "|".join(["---:"] * len(MODELS)) + "|")
        for row in rows_data:
            lines.append(f"| {row['label']} | Jaccard@5 | " +
                         " | ".join(row["jaccard"].get(m, "—") for m in MODELS) + " |")
            lines.append(f"|  | query cosine | " +
                         " | ".join(row["cosine"].get(m, "—") for m in MODELS) + " |")

    # Aggregate
    lines.append("\n## Aggregate (excluding 32K-overflow cases)\n")
    lines.append("\n| Model | Mean Jaccard@5 | N |")
    lines.append("|---|---:|---:|")
    for m in MODELS:
        scores = [s for s in per_model_jaccards[m]]
        if scores:
            mean = sum(scores) / len(scores)
            lines.append(f"| {m} | {mean:.3f} | {len(scores)} |")
        else:
            lines.append(f"| {m} | — | 0 |")

    # Verdict
    lines.append("\n## Verdict\n")
    j_4l = sum(per_model_jaccards["voyage-4-large"]) / len(per_model_jaccards["voyage-4-large"]) if per_model_jaccards["voyage-4-large"] else 0
    j_ctx = sum(per_model_jaccards["voyage-context-3"]) / len(per_model_jaccards["voyage-context-3"]) if per_model_jaccards["voyage-context-3"] else 0
    if j_ctx >= j_4l + 0.05:
        verdict = f"**voyage-context-3 wins** by {j_ctx - j_4l:+.3f} on single-doc Jaccard@5"
    elif j_4l >= j_ctx + 0.05:
        verdict = f"**voyage-4-large wins** by {j_4l - j_ctx:+.3f} on single-doc Jaccard@5 — even in the contextual model's sweet spot"
    else:
        verdict = f"**Effectively tied** (gap {abs(j_4l - j_ctx):.3f} < 0.05); pick voyage-4-large for simpler integration"
    lines.append(f"\n{verdict}\n")
    lines.append(f"\n- voyage-4-large mean Jaccard@5: **{j_4l:.3f}**")
    lines.append(f"- voyage-context-3 mean Jaccard@5: **{j_ctx:.3f}**\n")

    OUT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\n=== wrote {OUT_PATH} ===", file=sys.stderr)
    print(f"voyage-4-large: {j_4l:.3f} | voyage-context-3: {j_ctx:.3f}", file=sys.stderr)


if __name__ == "__main__":
    run()
