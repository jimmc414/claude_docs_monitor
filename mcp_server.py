#!/usr/bin/env python3
"""MCP server for Claude Docs Monitor — read-only access to documentation intelligence.

Exposes the SQLite database (page snapshots, diffs, AI-classified change events)
as MCP tools and resources. All write operations (check, digest, backfill) stay CLI-only.

Usage:
    python mcp_server.py                          # stdio transport (default)
    claude mcp add docs-monitor -- python mcp_server.py
"""

import json
import os
import sqlite3
import sys
from pathlib import Path

from mcp.server.fastmcp import FastMCP

# Add the script directory to sys.path so we can import claude_docs_monitor
_script_dir = Path(__file__).resolve().parent
if str(_script_dir) not in sys.path:
    sys.path.insert(0, str(_script_dir))

from claude_docs_monitor import (
    init_db,
    query_change_events,
    get_page_history,
    get_two_snapshots,
    get_all_tracked_urls,
    compute_diff,
    url_to_filename,
    _parse_relative_date,
)

# Optional RAG layer — only imported on first use to avoid loading
# numpy/embedding deps for users who don't run reindex.
_rag_loaded = False
_doc_index = None
_embedder = None
_retriever = None

# ── Configuration ───────────────────────────────────────────────────────────

# DB path: env var → canonical XDG location → local ./data-claude/
_CANONICAL_DB = Path.home() / ".local/share/claude-docs-monitor/data-claude/snapshots.db"
_LOCAL_DB = Path("data-claude/snapshots.db")

DB_PATH = Path(
    os.environ.get("DOCS_MONITOR_DB")
    or (_CANONICAL_DB if _CANONICAL_DB.exists() else _LOCAL_DB)
)

DATA_DIR = DB_PATH.parent  # digest.md, report.md, pages/ live alongside the DB


def _get_conn() -> sqlite3.Connection:
    """Open a read-only DB connection. Calls init_db() to ensure schema exists."""
    return init_db(DB_PATH)


def _rag_components():
    """Lazy-load and cache (DocIndex, EmbeddingCache, HybridRetriever) tuple.

    Returns (None, None, None) if the index/embedding files don't exist yet
    or the optional deps (numpy, etc.) aren't installed.
    """
    global _rag_loaded, _doc_index, _embedder, _retriever
    if _rag_loaded:
        return _doc_index, _embedder, _retriever
    _rag_loaded = True

    index_db = DATA_DIR / "index.db"
    emb_db = DATA_DIR / "embeddings.db"
    if not index_db.exists():
        return None, None, None

    try:
        from doc_index import DocIndex
        from embedding_cache import EmbeddingCache
        from retriever import HybridRetriever
    except ImportError:
        return None, None, None

    _embedder = EmbeddingCache(emb_db)
    _doc_index = DocIndex(index_db, embedder=_embedder)
    _retriever = HybridRetriever(_doc_index, _embedder)
    return _doc_index, _embedder, _retriever


# ── MCP Server ──────────────────────────────────────────────────────────────

mcp = FastMCP(
    "docs-monitor",
    instructions="Read-only access to Claude Code documentation change intelligence",
)

VALID_CATEGORIES = {"feature", "breaking", "deprecation", "clarification", "flag_change", "bugfix"}


# ── Tools ───────────────────────────────────────────────────────────────────

@mcp.tool()
def query_changes(
    keyword: str | None = None,
    category: str | None = None,
    severity: str | None = None,
    page: str | None = None,
    since: str | None = None,
    until: str | None = None,
    limit: int = 50,
) -> dict:
    """Query AI-classified documentation change events.

    Search the change intelligence database by keyword, category, severity,
    page name, or date range. Returns structured events with summaries,
    details, and action items.

    Categories: feature, breaking, deprecation, clarification, flag_change, bugfix
    Severity: high, medium, low
    Date formats: '7d' (last 7 days), '30d', '2024-01-01', ISO 8601
    """
    # Smart shortcut: if keyword matches a category name, redirect to category filter
    if keyword and keyword.lower() in VALID_CATEGORIES and not category:
        category = keyword.lower()
        keyword = None

    since_parsed = _parse_relative_date(since) if since else None
    until_parsed = _parse_relative_date(until) if until else None

    conn = _get_conn()
    try:
        rows = query_change_events(
            conn,
            category=category,
            severity=severity,
            page_name=page,
            keyword=keyword,
            since=since_parsed,
            until=until_parsed,
            limit=limit,
        )
        events = []
        for r in rows:
            event = dict(r)
            # Deserialize tags from JSON
            if event.get("tags_json"):
                try:
                    event["tags"] = json.loads(event["tags_json"])
                except (json.JSONDecodeError, TypeError):
                    event["tags"] = []
            else:
                event["tags"] = []
            del event["tags_json"]
            events.append(event)
        return {"events": events, "count": len(events)}
    finally:
        conn.close()


@mcp.tool()
def get_page_snapshots(url: str | None = None, limit: int = 20) -> dict:
    """Get snapshot history for documentation pages.

    If url is provided, returns snapshots for that specific page.
    If no url, returns an overview of all tracked URLs with their latest snapshot info.
    """
    conn = _get_conn()
    try:
        if url:
            rows = get_page_history(conn, url=url, limit=limit)
            snapshots = []
            for r in rows:
                snap = dict(r)
                # Don't send full content in listing — too large
                snap.pop("content", None)
                snapshots.append(snap)
            return {"url": url, "snapshots": snapshots, "count": len(snapshots)}
        else:
            tracked = get_all_tracked_urls(conn)
            return {"tracked_urls": tracked, "count": len(tracked)}
    finally:
        conn.close()


@mcp.tool()
def get_diff(url: str) -> dict:
    """Get the unified diff between the two most recent snapshots of a documentation page.

    Returns the diff text showing exactly what changed, along with timestamps.
    Requires the full URL (e.g. 'https://code.claude.com/docs/en/hooks.md').
    """
    conn = _get_conn()
    try:
        newest, previous = get_two_snapshots(conn, url)
        if newest is None:
            return {"error": f"No snapshots found for {url}"}
        if previous is None:
            return {
                "url": url,
                "message": "Only one snapshot exists (baseline). No diff available.",
                "fetched_at": newest["fetched_at"],
            }
        if newest["hash"] == previous["hash"]:
            return {
                "url": url,
                "message": "No changes between the two most recent snapshots.",
                "from": previous["fetched_at"],
                "to": newest["fetched_at"],
            }
        diff_text = compute_diff(previous["content"], newest["content"], url)
        return {
            "url": url,
            "from": previous["fetched_at"],
            "to": newest["fetched_at"],
            "diff": diff_text,
        }
    finally:
        conn.close()


@mcp.tool()
def search_pages(keyword: str, limit: int = 10) -> dict:
    """Search the latest cached documentation pages for a keyword.

    Searches the full text content of all documentation pages and returns
    matching page names with a snippet around the first match.
    """
    conn = _get_conn()
    try:
        # Get latest snapshot per URL, filter by keyword
        rows = conn.execute(
            """
            SELECT p.url, p.content
            FROM page_snapshots p
            INNER JOIN (
                SELECT url, MAX(id) as max_id FROM page_snapshots GROUP BY url
            ) latest ON p.id = latest.max_id
            WHERE p.content LIKE ?
            ORDER BY p.url
            LIMIT ?
            """,
            (f"%{keyword}%", limit),
        ).fetchall()

        matches = []
        for r in rows:
            content = r["content"] or ""
            page_name = url_to_filename(r["url"])

            # Extract snippet around first match
            lower_content = content.lower()
            idx = lower_content.find(keyword.lower())
            if idx >= 0:
                start = max(0, idx - 100)
                end = min(len(content), idx + len(keyword) + 100)
                snippet = content[start:end]
                if start > 0:
                    snippet = "..." + snippet
                if end < len(content):
                    snippet = snippet + "..."
            else:
                snippet = content[:200] + ("..." if len(content) > 200 else "")

            matches.append({
                "url": r["url"],
                "page_name": page_name,
                "snippet": snippet,
            })

        return {"keyword": keyword, "matches": matches, "count": len(matches)}
    finally:
        conn.close()


# ── RAG Tools (M3-M5) ───────────────────────────────────────────────────────


@mcp.tool()
def hybrid_search(
    query: str,
    source_type: str | None = None,
    category: str | None = None,
    severity: str | None = None,
    page: str | None = None,
    since: str | None = None,
    until: str | None = None,
    k: int = 10,
    rerank: bool = True,
) -> dict:
    """Hybrid BM25+dense semantic search with optional Claude rerank.

    Replaces lexical-only `search_pages` for natural-language questions.
    Combines BM25 (FTS5), dense cosine on raw vectors, and dense cosine on
    LLM-summary vectors. Fuses with RRF, then reranks with Claude.

    Args:
        query: Natural-language question or keyword.
        source_type: 'page' | 'change_event' | 'wiki_synthesis' | 'kg_entity' (optional).
        category, severity, page, since, until: Metadata filters.
        k: Number of results (default 10).
        rerank: Apply LLM rerank pass (default True; slower but higher quality).
    """
    _, _, retriever = _rag_components()
    if retriever is None:
        return {"error": "Hybrid retrieval index not built. Run "
                         "`python claude_docs_monitor.py reindex`."}

    filters: dict = {}
    if category:
        filters["category"] = category
    if severity:
        filters["severity"] = severity
    if page:
        filters["page"] = page
    if since:
        filters["since"] = _parse_relative_date(since)
    if until:
        filters["until"] = _parse_relative_date(until)

    hits = retriever.retrieve(
        query,
        source_type=source_type,
        filters=filters or None,
        k=k,
        rerank=rerank,
    )
    return {
        "query": query,
        "count": len(hits),
        "hits": [h.to_dict() for h in hits],
    }


@mcp.tool()
def change_search(
    query: str,
    since: str | None = None,
    until: str | None = None,
    category: str | None = None,
    severity: str | None = None,
    page: str | None = None,
    k: int = 10,
) -> dict:
    """Hybrid search restricted to documentation change events.

    Use this for natural-language questions about *what changed* — e.g.,
    "what changed about hooks recently?". For exact-filter-only queries
    (no keyword), use `query_changes` instead.
    """
    return hybrid_search(
        query=query,
        source_type="change_event",
        category=category,
        severity=severity,
        page=page,
        since=since,
        until=until,
        k=k,
    )


@mcp.tool()
def find_similar(chunk_id: int, k: int = 10) -> dict:
    """Find chunks most similar to a given chunk_id (cosine on content vectors)."""
    _, _, retriever = _rag_components()
    if retriever is None:
        return {"error": "Hybrid retrieval index not built. Run "
                         "`python claude_docs_monitor.py reindex`."}
    hits = retriever.find_similar(chunk_id, k=k)
    return {
        "chunk_id": chunk_id,
        "count": len(hits),
        "similar": [h.to_dict() for h in hits],
    }


@mcp.tool()
def get_chunk(chunk_id: int) -> dict:
    """Fetch a single chunk's full content and metadata by ID."""
    index, _, _ = _rag_components()
    if index is None:
        return {"error": "Hybrid retrieval index not built. Run "
                         "`python claude_docs_monitor.py reindex`."}
    c = index.get_chunk(chunk_id)
    if c is None:
        return {"error": f"chunk_id {chunk_id} not found"}
    return {
        "chunk_id": c.id,
        "source_type": c.source_type,
        "source_id": c.source_id,
        "chunk_type": c.chunk_type,
        "heading_path": c.heading_path,
        "content": c.content,
        "summary": c.summary,
        "url": c.url,
        "metadata": c.metadata,
        "line_start": c.line_start,
        "line_end": c.line_end,
    }


@mcp.tool()
def build_report(
    question: str,
    scope: str = "all",
    since: str | None = None,
    until: str | None = None,
    model: str = "opus",
    max_turns: int = 6,
) -> dict:
    """Build an agentic RAG research report with inline citations.

    Decomposes the question, retrieves evidence, reasons in a tool-equipped
    loop, synthesizes with citations, and self-critiques. Returns paths to
    the markdown report and companion JSON.

    Args:
        question: Your research question.
        scope: 'docs' | 'changes' | 'all' (default 'all').
        since, until: Date filters ('7d', '30d', YYYY-MM-DD).
        model: 'opus' | 'sonnet' | 'haiku' (default 'opus').
        max_turns: Max tool-use turns in the agentic loop (default 6).
    """
    try:
        from report_builder import build_report as _build
    except ImportError as e:
        return {"error": f"report_builder not importable: {e}"}

    scope_map = {
        "docs": ["page"],
        "changes": ["change_event"],
        "all": ["page", "change_event"],
    }
    scope_list = scope_map.get(scope)

    try:
        report = _build(
            question=question,
            scope=scope_list,
            since=since,
            until=until,
            max_loop_turns=max_turns,
            model=model,
            output_dir=DATA_DIR / "reports",
            data_dir=DATA_DIR,
        )
    except Exception as e:
        return {"error": f"report build failed: {type(e).__name__}: {e}"}

    return {
        "question": report.question,
        "markdown_path": str(report.markdown_path),
        "json_path": str(report.json_path),
        "evidence_count": len(report.evidence),
        "loop_turns": report.loop_turns,
        "elapsed_seconds": report.elapsed_seconds,
        "preview": report.markdown[:1500],
    }


@mcp.tool()
def list_reports() -> dict:
    """List all previously generated reports."""
    reports_dir = DATA_DIR / "reports"
    if not reports_dir.exists():
        return {"reports": [], "count": 0}
    items = []
    for md in sorted(reports_dir.glob("*.md")):
        json_path = md.with_suffix(".json")
        items.append({
            "slug": md.stem,
            "markdown_path": str(md),
            "json_path": str(json_path) if json_path.exists() else None,
            "size_bytes": md.stat().st_size,
            "modified_at": md.stat().st_mtime,
        })
    return {"reports": items, "count": len(items)}


@mcp.tool()
def get_saved_report(slug: str) -> dict:
    """Read a previously generated report's markdown by slug."""
    reports_dir = DATA_DIR / "reports"
    md = reports_dir / f"{slug}.md"
    if not md.exists():
        return {"error": f"Report not found: {slug}"}
    return {
        "slug": slug,
        "markdown": md.read_text(encoding="utf-8"),
        "json_path": str(md.with_suffix(".json")) if md.with_suffix(".json").exists() else None,
    }


# ── Resources ───────────────────────────────────────────────────────────────

@mcp.resource("docs://pages/{name}")
def get_page(name: str) -> str:
    """Get the latest cached content of a documentation page by filename.

    Example: docs://pages/hooks.md, docs://pages/best-practices.md
    """
    conn = _get_conn()
    try:
        # Find URL where url_to_filename matches the requested name
        tracked = get_all_tracked_urls(conn)
        target_url = None
        for entry in tracked:
            if url_to_filename(entry["url"]) == name:
                target_url = entry["url"]
                break

        # Fallback: partial match
        if not target_url:
            for entry in tracked:
                if name in url_to_filename(entry["url"]):
                    target_url = entry["url"]
                    break

        if not target_url:
            return f"Page not found: {name}"

        row = conn.execute(
            "SELECT content FROM page_snapshots WHERE url = ? ORDER BY id DESC LIMIT 1",
            (target_url,),
        ).fetchone()
        return row["content"] if row and row["content"] else f"No content for {name}"
    finally:
        conn.close()


@mcp.resource("docs://digest")
def get_digest() -> str:
    """Get the latest AI-generated change digest."""
    digest_path = DATA_DIR / "digest.md"
    if digest_path.exists():
        return digest_path.read_text(encoding="utf-8")
    return "No digest available. Run 'python claude_docs_monitor.py digest' first."


@mcp.resource("docs://report")
def get_report() -> str:
    """Get the latest check report (summary + diffs)."""
    report_path = DATA_DIR / "report.md"
    if report_path.exists():
        return report_path.read_text(encoding="utf-8")
    return "No report available. Run 'python claude_docs_monitor.py check' first."


# ── Entry point ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    mcp.run(transport="stdio")
