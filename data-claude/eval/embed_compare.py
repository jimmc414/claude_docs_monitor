"""R0: Head-to-head embedding model bake-off.

Compares voyage-4-large vs voyage-context-3 on:
  1. Cosine similarity of 5 known-failing paraphrase pairs (synonym bridging)
  2. Real-chunk Jaccard@5 on benchmark paraphrase pairs (end-to-end retrieval)

Decision rule encoded inline at the end. Writes a markdown report.

Run:
  python data-claude/eval/embed_compare.py
"""
from __future__ import annotations

import os
import sqlite3
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent

# Load .env so VOYAGE_API_KEY is available
try:
    from dotenv import load_dotenv
    load_dotenv(REPO / ".env")
except ImportError:
    pass

# Max OAuth: never let Anthropic API key leak in
os.environ.pop("ANTHROPIC_API_KEY", None)

import numpy as np  # noqa: E402
import voyageai  # noqa: E402

INDEX_DB = REPO / "data-claude" / "index.db"
OUT_PATH = REPO / "data-claude" / "eval" / "embed_compare_results.md"

MODELS = ["voyage-4-large", "voyage-context-3"]

# Free-tier throttle: 3 RPM / 10K TPM without payment method.
# Set DOCS_MONITOR_VOYAGE_THROTTLE=1 to enable 22s sleeps between API calls
# and small chunk batches (~30 chunks/call). Disable once payment method added.
THROTTLE = os.environ.get("DOCS_MONITOR_VOYAGE_THROTTLE") == "1"
THROTTLE_SLEEP_S = 22  # 3 RPM = 1 call per 20s; 22 is a small safety margin
THROTTLE_BATCH_CHUNKS = 25  # ~25 chunks * 300 tokens = ~7.5K tokens per call


def _throttle():
    if THROTTLE:
        time.sleep(THROTTLE_SLEEP_S)

# Pairs from probes.py — these are the ones the FAIL verdict was built on
PROBE_PAIRS = [
    ("How do I limit which tools Claude can use?",
     "How do I restrict Claude's tool access?"),
    ("How do I configure Claude Code to use AWS Bedrock?",
     "How do I run Claude Code on Bedrock?"),
    ("Where are session settings stored?",
     "What's the location of the settings file?"),
    ("How do hooks work in Claude Code?",
     "What is a hook and how is it configured?"),
    ("How do I create a custom slash command?",
     "How do I add a new slash command?"),
]

# Benchmark paraphrase pairs (Q041-Q050) with their expected_pages
BENCH_PAIRS = [
    {
        "ids": ("Q041", "Q042"),
        "a": "How do I restrict which tools Claude can use in a session?",
        "b": "How do I limit Claude's tool access in a Claude Code session?",
        "expected_pages": ["cli-reference.md", "permissions.md", "sub-agents.md"],
    },
    {
        "ids": ("Q043", "Q044"),
        "a": "What mechanism does Claude Code use to prevent context from growing too large during a long session?",
        "b": "How does Claude Code avoid running out of context window during extended coding sessions?",
        "expected_pages": ["best-practices.md", "checkpointing.md", "costs.md"],
    },
    {
        "ids": ("Q045", "Q046"),
        "a": "How do I make Claude Code run non-interactively in a CI pipeline?",
        "b": "What is the correct way to use Claude Code in a GitHub Actions workflow without interactive prompts?",
        "expected_pages": ["headless.md", "cli-reference.md", "authentication.md", "github-actions.md"],
    },
    {
        "ids": ("Q047", "Q048"),
        "a": "Where does Claude Code store credentials on Linux?",
        "b": "What file stores Claude Code's login tokens on a Linux machine?",
        "expected_pages": ["authentication.md"],
    },
    {
        "ids": ("Q049", "Q050"),
        "a": "How does the Python Agent SDK's query() function differ from ClaudeSDKClient for multi-turn conversations?",
        "b": "In the Python Agent SDK, when would I choose ClaudeSDKClient instead of calling query() repeatedly?",
        "expected_pages": ["agent-sdk/python.md"],
    },
]


def cosine(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-12))


def fetch_chunks_for_pages(pages: list[str]) -> dict[str, list[tuple[int, str]]]:
    """Return {source_id: [(chunk_id, content), ...]} for chunks whose source_id matches any page.

    The benchmark expected_pages are short forms ('permissions.md'); doc_chunks.source_id
    holds longer forms (e.g. 'permissions' or full URLs). Match by suffix.
    """
    conn = sqlite3.connect(str(INDEX_DB))
    conn.row_factory = sqlite3.Row
    out: dict[str, list[tuple[int, str]]] = {}
    for page in pages:
        # Match source_id ending with page name (with or without .md)
        bare = page.replace(".md", "")
        rows = conn.execute(
            """SELECT id, source_id, content FROM doc_chunks
               WHERE source_type='page'
                 AND (source_id LIKE ? OR source_id LIKE ? OR source_id = ? OR source_id = ?)
               ORDER BY id""",
            (f"%/{page}", f"%/{bare}", page, bare),
        ).fetchall()
        if not rows:
            print(f"  [warn] no chunks for page '{page}'", file=sys.stderr)
            continue
        for r in rows:
            sid = r["source_id"]
            out.setdefault(sid, []).append((r["id"], r["content"]))
    conn.close()
    return out


def embed_flat(client: voyageai.Client, model: str, texts: list[str], input_type: str) -> list[np.ndarray]:
    r = client.embed(texts, model=model, input_type=input_type)
    _throttle()
    return [np.asarray(v, dtype=np.float32) for v in r.embeddings]


def embed_contextual_chunks(
    client: voyageai.Client, model: str, chunks_by_source: dict[str, list[tuple[int, str]]]
) -> dict[int, np.ndarray]:
    """Embed chunks with contextual API. Returns {chunk_id: vector}.

    Each source_id is one document; under throttle mode, send one source per API call.
    """
    out: dict[int, np.ndarray] = {}
    sources = list(chunks_by_source.items())
    if THROTTLE:
        # One source per call to stay under 10K TPM
        for _sid, chunks in sources:
            r = client.contextualized_embed(
                inputs=[[c[1] for c in chunks]], model=model, input_type="document",
            )
            _throttle()
            for chunk_idx, vec in enumerate(r.results[0].embeddings):
                out[chunks[chunk_idx][0]] = np.asarray(vec, dtype=np.float32)
    else:
        inputs = [[c[1] for c in chunks] for _, chunks in sources]
        chunk_ids = [[c[0] for c in chunks] for _, chunks in sources]
        r = client.contextualized_embed(inputs=inputs, model=model, input_type="document")
        for doc_idx, doc_result in enumerate(r.results):
            for chunk_idx, vec in enumerate(doc_result.embeddings):
                out[chunk_ids[doc_idx][chunk_idx]] = np.asarray(vec, dtype=np.float32)
    return out


def embed_flat_chunks(
    client: voyageai.Client, model: str, chunks_by_source: dict[str, list[tuple[int, str]]]
) -> dict[int, np.ndarray]:
    """Embed chunks one-at-a-time (no context). Returns {chunk_id: vector}."""
    flat_ids = []
    flat_texts = []
    for chunks in chunks_by_source.values():
        for cid, content in chunks:
            flat_ids.append(cid)
            flat_texts.append(content)
    # Throttle mode: 25 chunks/call (~7.5K tokens). Otherwise 100/call.
    batch_size = THROTTLE_BATCH_CHUNKS if THROTTLE else 100
    out: dict[int, np.ndarray] = {}
    for i in range(0, len(flat_texts), batch_size):
        batch_texts = flat_texts[i:i+batch_size]
        batch_ids = flat_ids[i:i+batch_size]
        r = client.embed(batch_texts, model=model, input_type="document")
        _throttle()
        for cid, vec in zip(batch_ids, r.embeddings):
            out[cid] = np.asarray(vec, dtype=np.float32)
    return out


def topk_chunk_ids(query_vec: np.ndarray, chunk_vecs: dict[int, np.ndarray], k: int = 5) -> list[int]:
    scored = [(cid, cosine(query_vec, v)) for cid, v in chunk_vecs.items()]
    scored.sort(key=lambda x: x[1], reverse=True)
    return [cid for cid, _ in scored[:k]]


def jaccard(a: list, b: list) -> float:
    sa, sb = set(a), set(b)
    if not sa and not sb:
        return 1.0
    return len(sa & sb) / len(sa | sb)


def run():
    if not INDEX_DB.exists():
        print(f"FATAL: index.db not found at {INDEX_DB}", file=sys.stderr)
        sys.exit(1)

    if not os.environ.get("VOYAGE_API_KEY"):
        print("FATAL: VOYAGE_API_KEY not set (check .env)", file=sys.stderr)
        sys.exit(1)

    client = voyageai.Client()

    report_lines = ["# Embed Model Bake-off (R0)\n"]
    report_lines.append(f"_Run: {time.strftime('%Y-%m-%d %H:%M:%S')}_\n")
    report_lines.append(f"\nComparing: {', '.join(MODELS)}")
    report_lines.append(f"Probe pairs: {len(PROBE_PAIRS)} | Benchmark pairs: {len(BENCH_PAIRS)}\n")

    summary: dict[str, dict[str, float]] = {m: {} for m in MODELS}

    # ── Test 1: Probe-pair cosine ─────────────────────────────────────────────
    print("\n=== Test 1: Probe-pair cosine ===", file=sys.stderr)
    report_lines.append("\n## Test 1 — Probe-pair query-to-query cosine\n")
    report_lines.append("Higher cosine = better synonym bridging by the embedding model itself.\n")
    report_lines.append("\n| Pair | " + " | ".join(MODELS) + " |")
    report_lines.append("|---|" + "|".join(["---:"] * len(MODELS)) + "|")

    cosines_per_model: dict[str, list[float]] = {m: [] for m in MODELS}
    for i, (qa, qb) in enumerate(PROBE_PAIRS, 1):
        row_cells = [f"{i}. {qa[:40]}…/{qb[:30]}…"]
        for model in MODELS:
            print(f"  pair {i} model {model}", file=sys.stderr)
            try:
                if model.startswith("voyage-context"):
                    # contextualized_embed: each query as its own single-chunk doc
                    r = client.contextualized_embed(
                        inputs=[[qa], [qb]], model=model, input_type="query",
                    )
                    va = np.asarray(r.results[0].embeddings[0], dtype=np.float32)
                    vb = np.asarray(r.results[1].embeddings[0], dtype=np.float32)
                else:
                    vecs = embed_flat(client, model, [qa, qb], input_type="query")
                    va, vb = vecs[0], vecs[1]
                c = cosine(va, vb)
                cosines_per_model[model].append(c)
                row_cells.append(f"{c:.3f}")
            except Exception as e:
                row_cells.append(f"ERR: {str(e)[:30]}")
                print(f"    error: {e!r}", file=sys.stderr)
        report_lines.append("| " + " | ".join(row_cells) + " |")

    report_lines.append("")
    means_row = ["**Mean**"]
    for model in MODELS:
        if cosines_per_model[model]:
            mean = sum(cosines_per_model[model]) / len(cosines_per_model[model])
            summary[model]["probe_cosine_mean"] = mean
            means_row.append(f"**{mean:.3f}**")
        else:
            means_row.append("—")
    report_lines.append("| " + " | ".join(means_row) + " |")

    # ── Test 2: Real-chunk Jaccard@5 on benchmark pairs ──────────────────────
    print("\n=== Test 2: Real-chunk Jaccard@5 ===", file=sys.stderr)
    report_lines.append("\n## Test 2 — Real-chunk Jaccard@5 (benchmark pairs)\n")
    report_lines.append("Embed all chunks from each pair's expected_pages, compute top-5 per query half, "
                        "then Jaccard between the two halves' top-5 lists.\n")
    report_lines.append("\n| Pair | " + " | ".join(MODELS) + " |")
    report_lines.append("|---|" + "|".join(["---:"] * len(MODELS)) + "|")

    jaccards_per_model: dict[str, list[float]] = {m: [] for m in MODELS}

    for bench in BENCH_PAIRS:
        print(f"  pair {bench['ids']}", file=sys.stderr)
        chunks_by_source = fetch_chunks_for_pages(bench["expected_pages"])
        if not chunks_by_source:
            print(f"    [skip] no chunks found for {bench['expected_pages']}", file=sys.stderr)
            continue
        n_chunks = sum(len(v) for v in chunks_by_source.values())
        print(f"    {n_chunks} chunks across {len(chunks_by_source)} docs", file=sys.stderr)

        row_cells = [f"{bench['ids'][0]}/{bench['ids'][1]} ({n_chunks}c)"]
        for model in MODELS:
            try:
                if model.startswith("voyage-context"):
                    chunk_vecs = embed_contextual_chunks(client, model, chunks_by_source)
                    qr = client.contextualized_embed(
                        inputs=[[bench["a"]], [bench["b"]]], model=model, input_type="query",
                    )
                    qa = np.asarray(qr.results[0].embeddings[0], dtype=np.float32)
                    qb = np.asarray(qr.results[1].embeddings[0], dtype=np.float32)
                else:
                    chunk_vecs = embed_flat_chunks(client, model, chunks_by_source)
                    qvecs = embed_flat(client, model, [bench["a"], bench["b"]], input_type="query")
                    qa, qb = qvecs[0], qvecs[1]
                top_a = topk_chunk_ids(qa, chunk_vecs, k=5)
                top_b = topk_chunk_ids(qb, chunk_vecs, k=5)
                j = jaccard(top_a, top_b)
                jaccards_per_model[model].append(j)
                row_cells.append(f"{j:.3f}")
            except Exception as e:
                row_cells.append(f"ERR: {str(e)[:30]}")
                print(f"    error ({model}): {e!r}", file=sys.stderr)
        report_lines.append("| " + " | ".join(row_cells) + " |")

    report_lines.append("")
    means_row = ["**Mean Jaccard@5**"]
    for model in MODELS:
        if jaccards_per_model[model]:
            mean = sum(jaccards_per_model[model]) / len(jaccards_per_model[model])
            summary[model]["bench_jaccard5_mean"] = mean
            means_row.append(f"**{mean:.3f}**")
        else:
            means_row.append("—")
    report_lines.append("| " + " | ".join(means_row) + " |")

    # ── Decision rule ────────────────────────────────────────────────────────
    report_lines.append("\n## Decision\n")
    j_large = summary.get("voyage-4-large", {}).get("bench_jaccard5_mean", 0.0)
    j_ctx = summary.get("voyage-context-3", {}).get("bench_jaccard5_mean", 0.0)
    c_large = summary.get("voyage-4-large", {}).get("probe_cosine_mean", 0.0)
    c_ctx = summary.get("voyage-context-3", {}).get("probe_cosine_mean", 0.0)

    report_lines.append(f"- **voyage-4-large**: probe cosine mean **{c_large:.3f}**, bench Jaccard@5 mean **{j_large:.3f}**")
    report_lines.append(f"- **voyage-context-3**: probe cosine mean **{c_ctx:.3f}**, bench Jaccard@5 mean **{j_ctx:.3f}**")
    report_lines.append("")

    # Apply decision rule from plan
    if j_ctx >= j_large + 0.10:
        verdict = ("voyage-context-3", "Wins by ≥0.10 on Jaccard@5 — contextual embedding earns its keep.")
    elif j_large >= 0.65:
        verdict = ("voyage-4-large", "Strong enough on its own; simpler code change wins the tie.")
    else:
        verdict = ("voyage-context-3", "Neither is great, but only contextual has any chance of recovering. Escalate.")
    report_lines.append(f"\n**Decision**: ship `{verdict[0]}` — {verdict[1]}")

    # Token cost summary
    report_lines.append("\n## Cost note\n")
    report_lines.append("Voyage's 200M free tier covers this entire experiment "
                        "(estimated <100K tokens consumed across both models).")

    OUT_PATH.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    print(f"\n=== wrote {OUT_PATH} ===", file=sys.stderr)
    print(f"\nDecision: ship {verdict[0]}", file=sys.stderr)
    return verdict


if __name__ == "__main__":
    run()
