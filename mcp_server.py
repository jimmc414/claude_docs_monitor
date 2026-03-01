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

# ── Configuration ───────────────────────────────────────────────────────────

# DB path: env var → canonical XDG location → local ./data/
_CANONICAL_DB = Path.home() / ".local/share/claude-docs-monitor/data/snapshots.db"
_LOCAL_DB = Path("data/snapshots.db")

DB_PATH = Path(
    os.environ.get("DOCS_MONITOR_DB")
    or (_CANONICAL_DB if _CANONICAL_DB.exists() else _LOCAL_DB)
)

DATA_DIR = DB_PATH.parent  # digest.md, report.md, pages/ live alongside the DB


def _get_conn() -> sqlite3.Connection:
    """Open a read-only DB connection. Calls init_db() to ensure schema exists."""
    return init_db(DB_PATH)


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
