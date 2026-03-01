#!/usr/bin/env python3
"""Claude Code Documentation Change Monitor.

Polls all pages from code.claude.com/docs/, stores snapshots in SQLite,
and produces unified diffs when content changes.
"""

import argparse
import asyncio
import hashlib
import json
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from difflib import unified_diff
from pathlib import Path

import httpx

try:
    from rich.console import Console
    from rich.table import Table
    from rich.syntax import Syntax
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
    from rich.panel import Panel
    HAS_RICH = True
except ImportError:
    HAS_RICH = False

INDEX_URL = "https://code.claude.com/docs/llms.txt"
BASE_URL = "https://code.claude.com"
DB_DIR = Path("data")
DB_PATH = DB_DIR / "snapshots.db"
MAX_CONCURRENT = 5
MAX_RETRIES = 3
BACKOFF_BASE = 1  # seconds

console = Console() if HAS_RICH else None


# ── Database Layer ──────────────────────────────────────────────────────────

def init_db(db_path: Path = DB_PATH) -> sqlite3.Connection:
    """Initialize SQLite database with schema."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS index_snapshots (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            fetched_at  TEXT    NOT NULL,
            content     TEXT    NOT NULL,
            hash        TEXT    NOT NULL,
            urls_json   TEXT    NOT NULL
        );
        CREATE TABLE IF NOT EXISTS page_snapshots (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            url         TEXT    NOT NULL,
            fetched_at  TEXT    NOT NULL,
            content     TEXT,
            hash        TEXT,
            status_code INTEGER,
            duration_ms REAL,
            error       TEXT
        );
        CREATE INDEX IF NOT EXISTS idx_page_url ON page_snapshots(url);
        CREATE INDEX IF NOT EXISTS idx_page_fetched ON page_snapshots(fetched_at);

        CREATE TABLE IF NOT EXISTS change_events (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            run_timestamp   TEXT    NOT NULL,
            url             TEXT    NOT NULL,
            page_name       TEXT    NOT NULL,
            event_type      TEXT    NOT NULL,
            category        TEXT,
            severity        TEXT,
            summary         TEXT,
            details         TEXT,
            action_required TEXT,
            tags_json       TEXT,
            diff_text       TEXT,
            gh_issue_url    TEXT,
            created_at      TEXT    NOT NULL
        );
        CREATE INDEX IF NOT EXISTS idx_ce_run ON change_events(run_timestamp);
        CREATE INDEX IF NOT EXISTS idx_ce_url ON change_events(url);
        CREATE INDEX IF NOT EXISTS idx_ce_category ON change_events(category);
        CREATE INDEX IF NOT EXISTS idx_ce_severity ON change_events(severity);
    """)
    return conn


def store_index_snapshot(conn: sqlite3.Connection, content: str, urls: list[str]) -> int:
    """Store an index snapshot and return its id."""
    h = sha256(content)
    now = utcnow()
    cur = conn.execute(
        "INSERT INTO index_snapshots (fetched_at, content, hash, urls_json) VALUES (?, ?, ?, ?)",
        (now, content, h, json.dumps(urls)),
    )
    conn.commit()
    return cur.lastrowid


def get_last_index_snapshot(conn: sqlite3.Connection) -> sqlite3.Row | None:
    """Return the most recent index snapshot, or None."""
    return conn.execute(
        "SELECT * FROM index_snapshots ORDER BY id DESC LIMIT 1"
    ).fetchone()


def store_page_snapshot(conn: sqlite3.Connection, url: str, content: str | None,
                        status_code: int | None, duration_ms: float, error: str | None = None):
    """Append a page snapshot."""
    h = sha256(content) if content else None
    now = utcnow()
    conn.execute(
        "INSERT INTO page_snapshots (url, fetched_at, content, hash, status_code, duration_ms, error) "
        "VALUES (?, ?, ?, ?, ?, ?, ?)",
        (url, now, content, h, status_code, duration_ms, error),
    )


def get_last_page_snapshot(conn: sqlite3.Connection, url: str) -> sqlite3.Row | None:
    """Return the most recent snapshot for a URL."""
    return conn.execute(
        "SELECT * FROM page_snapshots WHERE url = ? ORDER BY id DESC LIMIT 1", (url,)
    ).fetchone()


def get_page_history(conn: sqlite3.Connection, url: str | None = None, limit: int = 50) -> list[sqlite3.Row]:
    """Return snapshot history, optionally filtered by URL."""
    if url:
        return conn.execute(
            "SELECT * FROM page_snapshots WHERE url = ? ORDER BY id DESC LIMIT ?", (url, limit)
        ).fetchall()
    return conn.execute(
        "SELECT url, fetched_at, hash, status_code, error FROM page_snapshots ORDER BY id DESC LIMIT ?",
        (limit,),
    ).fetchall()


def get_two_snapshots(conn: sqlite3.Connection, url: str) -> tuple[sqlite3.Row | None, sqlite3.Row | None]:
    """Return the two most recent snapshots for a URL (newest first)."""
    rows = conn.execute(
        "SELECT * FROM page_snapshots WHERE url = ? ORDER BY id DESC LIMIT 2", (url,)
    ).fetchall()
    if len(rows) == 2:
        return rows[0], rows[1]
    if len(rows) == 1:
        return rows[0], None
    return None, None


def get_all_tracked_urls(conn: sqlite3.Connection) -> list[dict]:
    """Return all tracked URLs with their latest snapshot info."""
    rows = conn.execute("""
        SELECT p.url, p.fetched_at, p.status_code, p.hash, p.error
        FROM page_snapshots p
        INNER JOIN (
            SELECT url, MAX(id) as max_id FROM page_snapshots GROUP BY url
        ) latest ON p.id = latest.max_id
        ORDER BY p.url
    """).fetchall()
    return [dict(r) for r in rows]


def store_change_event(conn: sqlite3.Connection, run_timestamp: str, url: str,
                       event_type: str, diff_text: str | None = None,
                       ai_result: dict | None = None) -> int:
    """Insert a change event row. Returns the row id."""
    page_name = url_to_filename(url)
    now = utcnow()
    category = ai_result.get("category") if ai_result else None
    severity = ai_result.get("severity") if ai_result else None
    summary = ai_result.get("summary") if ai_result else None
    details = ai_result.get("details") if ai_result else None
    action_required = ai_result.get("action_required") if ai_result else None
    tags = ai_result.get("tags") if ai_result else None
    tags_json = json.dumps(tags) if tags else None
    cur = conn.execute(
        "INSERT INTO change_events "
        "(run_timestamp, url, page_name, event_type, category, severity, "
        " summary, details, action_required, tags_json, diff_text, created_at) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (run_timestamp, url, page_name, event_type, category, severity,
         summary, details, action_required, tags_json, diff_text, now),
    )
    return cur.lastrowid


def query_change_events(conn: sqlite3.Connection, *, category: str | None = None,
                        severity: str | None = None, page_name: str | None = None,
                        keyword: str | None = None, since: str | None = None,
                        until: str | None = None, limit: int = 50) -> list[sqlite3.Row]:
    """Flexible query against change_events with optional filters."""
    clauses = []
    params = []
    if category:
        clauses.append("category = ?")
        params.append(category)
    if severity:
        clauses.append("severity = ?")
        params.append(severity)
    if page_name:
        clauses.append("page_name LIKE ?")
        params.append(f"%{page_name}%")
    if keyword:
        clauses.append("(summary LIKE ? OR details LIKE ? OR tags_json LIKE ?)")
        params.extend([f"%{keyword}%"] * 3)
    if since:
        clauses.append("run_timestamp >= ?")
        params.append(since)
    if until:
        clauses.append("run_timestamp <= ?")
        params.append(until)
    where = (" WHERE " + " AND ".join(clauses)) if clauses else ""
    params.append(limit)
    return conn.execute(
        f"SELECT * FROM change_events{where} ORDER BY run_timestamp DESC, id DESC LIMIT ?",
        params,
    ).fetchall()


def update_change_event_issue(conn: sqlite3.Connection, event_id: int, issue_url: str):
    """Set the gh_issue_url on a change event row."""
    conn.execute("UPDATE change_events SET gh_issue_url = ? WHERE id = ?", (issue_url, event_id))


def get_change_events_for_run(conn: sqlite3.Connection, run_timestamp: str) -> list[sqlite3.Row]:
    """Return all change events for a specific run."""
    return conn.execute(
        "SELECT * FROM change_events WHERE run_timestamp = ? ORDER BY id",
        (run_timestamp,),
    ).fetchall()


# ── Utilities ───────────────────────────────────────────────────────────────

def sha256(text: str) -> str:
    """SHA-256 hex digest of normalized text."""
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def utcnow() -> str:
    """ISO 8601 UTC timestamp."""
    return datetime.now(timezone.utc).isoformat()


def normalize(text: str) -> str:
    """Normalize line endings."""
    return text.replace("\r\n", "\n").replace("\r", "\n")


def parse_index(content: str) -> list[str]:
    """Extract markdown page URLs from llms.txt content.

    Format: - [title](url): description
    """
    urls = []
    for line in content.splitlines():
        # Match markdown links: [text](url)
        for match in re.finditer(r'\[([^\]]*)\]\((https?://[^)]+)\)', line):
            urls.append(match.group(2))
    return urls


def is_html_diff(diff_text: str) -> bool:
    """Return True if a diff is predominantly HTML/script noise."""
    changed = [l for l in diff_text.splitlines()
               if l.startswith("+") or l.startswith("-")]
    if len(changed) < 2:
        return False
    html_count = sum(1 for l in changed if re.search(
        r'<(script|meta|link|button|svg|path|div|span|ul|li|form|input|textarea)\b|'
        r'data-(target|action|view|turbo|pjax)|'
        r'class="[A-Z]|'
        r'id="(icon-button|tooltip|item|action-menu|validation|query-builder|custom-)|'
        r'data-csrf|'
        r'content="v2:[0-9a-f]|'
        r'aria-label(led)?=',
        l, re.IGNORECASE))
    return html_count / len(changed) > 0.5


def compute_diff(old_content: str, new_content: str, url: str) -> str:
    """Compute unified diff between two versions."""
    old_lines = normalize(old_content).splitlines(keepends=True)
    new_lines = normalize(new_content).splitlines(keepends=True)
    diff_lines = unified_diff(
        old_lines, new_lines,
        fromfile=f"a/{url}", tofile=f"b/{url}",
        lineterm="\n",
    )
    return "".join(diff_lines)


# ── HTTP Layer ──────────────────────────────────────────────────────────────

async def fetch_url(client: httpx.AsyncClient, url: str, semaphore: asyncio.Semaphore,
                    retries: int = MAX_RETRIES) -> dict:
    """Fetch a URL with retry and backoff. Returns result dict."""
    async with semaphore:
        for attempt in range(retries):
            start = time.monotonic()
            try:
                resp = await client.get(url, follow_redirects=True, timeout=30.0)
                duration_ms = (time.monotonic() - start) * 1000
                return {
                    "url": url,
                    "content": resp.text,
                    "status_code": resp.status_code,
                    "duration_ms": duration_ms,
                    "error": None,
                }
            except (httpx.HTTPError, httpx.TimeoutException) as exc:
                duration_ms = (time.monotonic() - start) * 1000
                if attempt < retries - 1:
                    await asyncio.sleep(BACKOFF_BASE * (2 ** attempt))
                    continue
                return {
                    "url": url,
                    "content": None,
                    "status_code": None,
                    "duration_ms": duration_ms,
                    "error": f"{type(exc).__name__}: {exc}",
                }


async def fetch_all(urls: list[str], show_progress: bool = True) -> list[dict]:
    """Fetch all URLs concurrently with semaphore throttling."""
    semaphore = asyncio.Semaphore(MAX_CONCURRENT)
    async with httpx.AsyncClient(http2=True) as client:
        if show_progress and HAS_RICH:
            results = []
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TextColumn("{task.completed}/{task.total}"),
                console=console,
            ) as progress:
                task = progress.add_task("Fetching pages...", total=len(urls))
                tasks = []
                for url in urls:
                    tasks.append(fetch_url(client, url, semaphore))
                for coro in asyncio.as_completed(tasks):
                    result = await coro
                    results.append(result)
                    progress.advance(task)
            return results
        else:
            tasks = [fetch_url(client, url, semaphore) for url in urls]
            return await asyncio.gather(*tasks)


# ── Display Layer ───────────────────────────────────────────────────────────

def print_plain(msg: str):
    """Print without rich."""
    print(msg)


def print_summary(changes: list[dict], added_urls: list[str], removed_urls: list[str],
                  errors: list[dict], total: int, first_run: bool, quiet: bool):
    """Print summary report."""
    if first_run:
        if HAS_RICH:
            console.print(Panel(
                f"[bold green]First run: {total} pages snapshotted.[/bold green]",
                title="Claude Docs Monitor",
            ))
        else:
            print(f"\n=== First run: {total} pages snapshotted. ===\n")
        return

    # Summary table
    if HAS_RICH:
        table = Table(title="Change Summary")
        table.add_column("Metric", style="bold")
        table.add_column("Count", justify="right")
        table.add_row("Total pages", str(total))
        table.add_row("Changed", f"[yellow]{len(changes)}[/yellow]" if changes else "0")
        table.add_row("Added", f"[green]{len(added_urls)}[/green]" if added_urls else "0")
        table.add_row("Removed", f"[red]{len(removed_urls)}[/red]" if removed_urls else "0")
        table.add_row("Errors", f"[red]{len(errors)}[/red]" if errors else "0")
        console.print(table)
    else:
        print(f"\n--- Change Summary ---")
        print(f"Total pages: {total}")
        print(f"Changed:     {len(changes)}")
        print(f"Added:       {len(added_urls)}")
        print(f"Removed:     {len(removed_urls)}")
        print(f"Errors:      {len(errors)}")

    if added_urls:
        if HAS_RICH:
            console.print("\n[bold green]Added pages:[/bold green]")
            for u in added_urls:
                console.print(f"  + {u}")
        else:
            print("\nAdded pages:")
            for u in added_urls:
                print(f"  + {u}")

    if removed_urls:
        if HAS_RICH:
            console.print("\n[bold red]Removed pages:[/bold red]")
            for u in removed_urls:
                console.print(f"  - {u}")
        else:
            print("\nRemoved pages:")
            for u in removed_urls:
                print(f"  - {u}")

    if errors:
        if HAS_RICH:
            console.print("\n[bold red]Errors:[/bold red]")
            for e in errors:
                console.print(f"  ! {e['url']}: {e['error']}")
        else:
            print("\nErrors:")
            for e in errors:
                print(f"  ! {e['url']}: {e['error']}")


def print_diffs(changes: list[dict], quiet: bool):
    """Print diffs for changed pages."""
    if quiet or not changes:
        return
    for ch in changes:
        diff_text = ch["diff"]
        if not diff_text:
            continue
        if HAS_RICH:
            console.print(f"\n[bold cyan]{'─' * 60}[/bold cyan]")
            console.print(f"[bold]Changed:[/bold] {ch['url']}")
            console.print(Syntax(diff_text, "diff", theme="monokai"))
        else:
            print(f"\n{'─' * 60}")
            print(f"Changed: {ch['url']}")
            print(diff_text)


def generate_md_report(report_data: dict, output_dir: Path):
    """Write a Markdown report to output_dir/report.md."""
    output_dir.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Claude Docs Monitor Report",
        f"\n*Generated: {report_data['timestamp']}*\n",
    ]

    if report_data["first_run"]:
        lines.append(f"**First run: {report_data['total']} pages snapshotted.**\n")
        for url in report_data["urls"]:
            lines.append(f"- {url}")
    else:
        lines.append("| Metric | Count |")
        lines.append("|--------|------:|")
        lines.append(f"| Changed | {len(report_data['changes'])} |")
        lines.append(f"| Added | {len(report_data['added'])} |")
        lines.append(f"| Removed | {len(report_data['removed'])} |")
        lines.append(f"| Errors | {len(report_data['errors'])} |")

        if report_data["added"]:
            lines.append("\n## Added Pages\n")
            for url in report_data["added"]:
                lines.append(f"- {url}")

        if report_data["removed"]:
            lines.append("\n## Removed Pages\n")
            for url in report_data["removed"]:
                lines.append(f"- {url}")

        if report_data["errors"]:
            lines.append("\n## Errors\n")
            for e in report_data["errors"]:
                lines.append(f"- **{e['url']}**: {e['error']}")

        if report_data["changes"]:
            lines.append("\n## Diffs\n")
            for ch in report_data["changes"]:
                lines.append(f"### {ch['url']}\n")
                lines.append("```diff")
                lines.append(ch["diff"])
                lines.append("```")

    (output_dir / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


_HTML_CSS = """\
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
       max-width: 960px; margin: 2rem auto; padding: 0 1rem; color: #24292e; line-height: 1.5; }
h1 { border-bottom: 1px solid #e1e4e8; padding-bottom: .3em; }
h2 { margin-top: 1.5em; border-bottom: 1px solid #eaecef; padding-bottom: .2em; }
h3 { margin-top: 1.2em; }
h4 { margin-top: 1em; }
table { border-collapse: collapse; margin: 1em 0; }
th, td { border: 1px solid #dfe2e5; padding: .4em .8em; text-align: left; }
th { background: #f6f8fa; }
td:last-child { text-align: right; }
ul { padding-left: 1.4em; }
.ts { color: #6a737d; font-size: .85em; }
hr { border: none; border-top: 2px solid #e1e4e8; margin: 2em 0; }
.diff { border: 1px solid #d0d7de; border-radius: 6px; margin: 1em 0; overflow-x: auto; }
.diff-line { font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
             font-size: .85em; padding: 1px 10px; white-space: pre-wrap; word-wrap: break-word;
             border-left: 3px solid transparent; }
.diff-line.add { background: #e6ffec; border-left-color: #2da44e; }
.diff-line.del { background: #ffebe9; border-left-color: #cf222e; }
.diff-line.hunk { background: #ddf4ff; color: #0969da; border-left-color: #54aeff;
                  padding-top: 4px; padding-bottom: 4px; font-weight: 600; }
.diff-line.ctx { background: #ffffff; color: #57606a; }
.diff-header { background: #f6f8fa; padding: 8px 10px; font-family: "SFMono-Regular", Consolas,
               "Liberation Mono", Menlo, monospace; font-size: .85em; font-weight: 600;
               border-bottom: 1px solid #d0d7de; color: #24292e; }"""


def _esc_html(text: str) -> str:
    """HTML-escape special characters."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _render_diff_html(diff_text: str) -> str:
    """Render a unified diff as GitHub-style HTML lines."""
    parts = ['<div class="diff">']
    for line in diff_text.splitlines():
        escaped = _esc_html(line)
        if line.startswith("+++") or line.startswith("---"):
            parts.append(f'<div class="diff-header">{escaped}</div>')
        elif line.startswith("+"):
            parts.append(f'<div class="diff-line add">{escaped}</div>')
        elif line.startswith("-"):
            parts.append(f'<div class="diff-line del">{escaped}</div>')
        elif line.startswith("@@"):
            parts.append(f'<div class="diff-line hunk">{escaped}</div>')
        else:
            parts.append(f'<div class="diff-line ctx">{escaped}</div>')
    parts.append("</div>")
    return "\n".join(parts)


def generate_html_report(report_data: dict, output_dir: Path):
    """Write a self-contained HTML report to output_dir/report.html."""
    output_dir.mkdir(parents=True, exist_ok=True)

    body_parts = [
        "<h1>Claude Docs Monitor Report</h1>",
        f'<p class="ts">{_esc_html(report_data["timestamp"])}</p>',
    ]

    if report_data["first_run"]:
        body_parts.append(f"<p><strong>First run: {report_data['total']} pages snapshotted.</strong></p>")
        body_parts.append("<ul>")
        for url in report_data["urls"]:
            body_parts.append(f"<li>{_esc_html(url)}</li>")
        body_parts.append("</ul>")
    else:
        body_parts.append("<table><tr><th>Metric</th><th>Count</th></tr>")
        body_parts.append(f"<tr><td>Changed</td><td>{len(report_data['changes'])}</td></tr>")
        body_parts.append(f"<tr><td>Added</td><td>{len(report_data['added'])}</td></tr>")
        body_parts.append(f"<tr><td>Removed</td><td>{len(report_data['removed'])}</td></tr>")
        body_parts.append(f"<tr><td>Errors</td><td>{len(report_data['errors'])}</td></tr>")
        body_parts.append("</table>")

        if report_data["added"]:
            body_parts.append("<h2>Added Pages</h2><ul>")
            for url in report_data["added"]:
                body_parts.append(f"<li>{_esc_html(url)}</li>")
            body_parts.append("</ul>")

        if report_data["removed"]:
            body_parts.append("<h2>Removed Pages</h2><ul>")
            for url in report_data["removed"]:
                body_parts.append(f"<li>{_esc_html(url)}</li>")
            body_parts.append("</ul>")

        if report_data["errors"]:
            body_parts.append("<h2>Errors</h2><ul>")
            for e in report_data["errors"]:
                body_parts.append(f"<li><strong>{_esc_html(e['url'])}</strong>: {_esc_html(e['error'])}</li>")
            body_parts.append("</ul>")

        if report_data["changes"]:
            body_parts.append("<h2>Diffs</h2>")
            for ch in report_data["changes"]:
                body_parts.append(f"<h3>{_esc_html(ch['url'])}</h3>")
                body_parts.append(_render_diff_html(ch["diff"]))

    html = (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n"
        f"<title>Claude Docs Monitor Report</title>\n<style>\n{_HTML_CSS}\n</style>\n</head>\n"
        f"<body>\n{''.join(body_parts)}\n</body>\n</html>\n"
    )
    (output_dir / "report.html").write_text(html, encoding="utf-8")


def _build_md_entry(report_data: dict) -> str:
    """Build a single Markdown entry for one check run."""
    lines = [
        f"## {report_data['timestamp']}",
        "",
    ]
    if report_data["first_run"]:
        lines.append(f"**First run: {report_data['total']} pages snapshotted.**\n")
        for url in report_data["urls"]:
            lines.append(f"- {url}")
    else:
        lines.append("| Metric | Count |")
        lines.append("|--------|------:|")
        lines.append(f"| Changed | {len(report_data['changes'])} |")
        lines.append(f"| Added | {len(report_data['added'])} |")
        lines.append(f"| Removed | {len(report_data['removed'])} |")
        lines.append(f"| Errors | {len(report_data['errors'])} |")

        if report_data["added"]:
            lines.append("\n### Added Pages\n")
            for url in report_data["added"]:
                lines.append(f"- {url}")

        if report_data["removed"]:
            lines.append("\n### Removed Pages\n")
            for url in report_data["removed"]:
                lines.append(f"- {url}")

        if report_data["errors"]:
            lines.append("\n### Errors\n")
            for e in report_data["errors"]:
                lines.append(f"- **{e['url']}**: {e['error']}")

        if report_data["changes"]:
            lines.append("\n### Diffs\n")
            for ch in report_data["changes"]:
                lines.append(f"#### {ch['url']}\n")
                lines.append("```diff")
                lines.append(ch["diff"])
                lines.append("```")

    return "\n".join(lines) + "\n"


def _build_html_entry(report_data: dict) -> str:
    """Build HTML fragment for one check run."""
    parts = [
        f'<h2>{_esc_html(report_data["timestamp"])}</h2>',
    ]
    if report_data["first_run"]:
        parts.append(f"<p><strong>First run: {report_data['total']} pages snapshotted.</strong></p>")
        parts.append("<ul>")
        for url in report_data["urls"]:
            parts.append(f"<li>{_esc_html(url)}</li>")
        parts.append("</ul>")
    else:
        parts.append("<table><tr><th>Metric</th><th>Count</th></tr>")
        parts.append(f"<tr><td>Changed</td><td>{len(report_data['changes'])}</td></tr>")
        parts.append(f"<tr><td>Added</td><td>{len(report_data['added'])}</td></tr>")
        parts.append(f"<tr><td>Removed</td><td>{len(report_data['removed'])}</td></tr>")
        parts.append(f"<tr><td>Errors</td><td>{len(report_data['errors'])}</td></tr>")
        parts.append("</table>")

        if report_data["added"]:
            parts.append("<h3>Added Pages</h3><ul>")
            for url in report_data["added"]:
                parts.append(f"<li>{_esc_html(url)}</li>")
            parts.append("</ul>")

        if report_data["removed"]:
            parts.append("<h3>Removed Pages</h3><ul>")
            for url in report_data["removed"]:
                parts.append(f"<li>{_esc_html(url)}</li>")
            parts.append("</ul>")

        if report_data["errors"]:
            parts.append("<h3>Errors</h3><ul>")
            for e in report_data["errors"]:
                parts.append(f"<li><strong>{_esc_html(e['url'])}</strong>: {_esc_html(e['error'])}</li>")
            parts.append("</ul>")

        if report_data["changes"]:
            parts.append("<h3>Diffs</h3>")
            for ch in report_data["changes"]:
                parts.append(f"<h4>{_esc_html(ch['url'])}</h4>")
                parts.append(_render_diff_html(ch["diff"]))

    return "\n".join(parts)


def append_md_history(report_data: dict, output_dir: Path):
    """Append a new entry to output_dir/history.md."""
    output_dir.mkdir(parents=True, exist_ok=True)
    history_path = output_dir / "history.md"
    entry = _build_md_entry(report_data)
    if history_path.exists():
        with open(history_path, "a", encoding="utf-8") as f:
            f.write("\n---\n\n")
            f.write(entry)
    else:
        with open(history_path, "w", encoding="utf-8") as f:
            f.write("# Claude Docs Monitor History\n\n")
            f.write(entry)


def append_html_history(report_data: dict, output_dir: Path):
    """Append a new entry to output_dir/history.html."""
    output_dir.mkdir(parents=True, exist_ok=True)

    entry = _build_html_entry(report_data)
    history_path = output_dir / "history.html"

    if history_path.exists():
        content = history_path.read_text(encoding="utf-8")
        insert_point = content.rfind("</body>")
        if insert_point != -1:
            content = content[:insert_point] + "<hr>" + entry + content[insert_point:]
            history_path.write_text(content, encoding="utf-8")
            return

    # Create new file
    html = (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n"
        f"<title>Claude Docs Monitor History</title>\n<style>\n{_HTML_CSS}\n</style>\n</head>\n"
        f"<body>\n<h1>Claude Docs Monitor History</h1>\n{entry}\n</body>\n</html>\n"
    )
    history_path.write_text(html, encoding="utf-8")


def save_diff_files(changes: list[dict], diff_dir: str):
    """Save .diff files to disk."""
    diff_path = Path(diff_dir)
    diff_path.mkdir(parents=True, exist_ok=True)
    for ch in changes:
        if not ch["diff"]:
            continue
        # Create filename from URL path
        name = ch["url"].replace("https://", "").replace("http://", "")
        name = name.replace("/", "_").replace(".", "_") + ".diff"
        filepath = diff_path / name
        filepath.write_text(ch["diff"], encoding="utf-8")
    if HAS_RICH:
        console.print(f"\n[green]Saved {len(changes)} diff files to {diff_dir}/[/green]")
    else:
        print(f"\nSaved {len(changes)} diff files to {diff_dir}/")


# ── Core Commands ───────────────────────────────────────────────────────────

async def cmd_check(args):
    """Main check command: fetch all pages, detect changes, show diffs."""
    conn = init_db()

    # Step 1: Fetch index
    if HAS_RICH:
        console.print("[bold]Fetching index...[/bold]")
    else:
        print("Fetching index...")

    semaphore = asyncio.Semaphore(MAX_CONCURRENT)
    async with httpx.AsyncClient(http2=True) as client:
        index_result = await fetch_url(client, INDEX_URL, semaphore)

    if index_result["error"] or not index_result["content"]:
        # Fall back to last stored URL list
        last_index = get_last_index_snapshot(conn)
        if last_index:
            urls = json.loads(last_index["urls_json"])
            if HAS_RICH:
                console.print(f"[yellow]Index fetch failed ({index_result['error']}), "
                              f"using cached URL list ({len(urls)} URLs)[/yellow]")
            else:
                print(f"Index fetch failed ({index_result['error']}), "
                      f"using cached URL list ({len(urls)} URLs)")
        else:
            if HAS_RICH:
                console.print(f"[red]Index fetch failed and no cached URLs available. Aborting.[/red]")
            else:
                print("Index fetch failed and no cached URLs available. Aborting.")
            return
    else:
        urls = parse_index(index_result["content"])
        if not urls:
            if HAS_RICH:
                console.print("[red]No URLs found in index. Aborting.[/red]")
            else:
                print("No URLs found in index. Aborting.")
            return

        # Compare against last index
        last_index = get_last_index_snapshot(conn)
        added_urls_index = []
        removed_urls_index = []
        if last_index:
            old_urls = set(json.loads(last_index["urls_json"]))
            new_urls = set(urls)
            added_urls_index = sorted(new_urls - old_urls)
            removed_urls_index = sorted(old_urls - new_urls)

        store_index_snapshot(conn, index_result["content"], urls)

    if HAS_RICH:
        console.print(f"Found [bold]{len(urls)}[/bold] pages to check.")
    else:
        print(f"Found {len(urls)} pages to check.")

    # Determine if first run
    first_run = get_last_page_snapshot(conn, urls[0]) is None if urls else True

    # Step 2: Fetch all pages
    results = await fetch_all(urls, show_progress=not getattr(args, "quiet", False))

    # Step 3: Detect changes
    changes = []
    errors = []
    for result in results:
        url = result["url"]
        if result["error"]:
            errors.append(result)
            store_page_snapshot(conn, url, result["content"], result["status_code"],
                                result["duration_ms"], result["error"])
            continue

        prev = get_last_page_snapshot(conn, url)

        if prev and result["content"]:
            new_hash = sha256(result["content"])
            if prev["hash"] != new_hash:
                diff_text = compute_diff(prev["content"] or "", result["content"], url)
                changes.append({"url": url, "diff": diff_text})
            # Check status code change
            if prev["status_code"] and result["status_code"] != prev["status_code"]:
                if prev["status_code"] == 200 and result["status_code"] != 200:
                    if not any(c["url"] == url for c in changes):
                        changes.append({
                            "url": url,
                            "diff": f"Status changed: {prev['status_code']} → {result['status_code']}",
                        })

        store_page_snapshot(conn, url, result["content"], result["status_code"],
                            result["duration_ms"])

    conn.commit()

    # Step 4: Filter HTML noise unless --include-html
    include_html = getattr(args, "include_html", False)
    if not include_html and changes:
        filtered = []
        skipped = []
        for ch in changes:
            if ch["diff"] and is_html_diff(ch["diff"]):
                skipped.append(ch["url"])
            else:
                filtered.append(ch)
        if skipped:
            if HAS_RICH:
                console.print(f"\n[dim]Suppressed {len(skipped)} HTML-noise diff(s): "
                              f"{', '.join(url.rsplit('/', 1)[-1] for url in skipped)}[/dim]")
                console.print("[dim]Use --include-html to show all diffs[/dim]")
            else:
                print(f"\nSuppressed {len(skipped)} HTML-noise diff(s): "
                      f"{', '.join(url.rsplit('/', 1)[-1] for url in skipped)}")
                print("Use --include-html to show all diffs")
        changes = filtered

    # Step 5: Display report
    added_urls_display = added_urls_index if not first_run else []
    removed_urls_display = removed_urls_index if not first_run else []
    quiet = getattr(args, "quiet", False)

    print_summary(changes, added_urls_display, removed_urls_display, errors, len(urls), first_run, quiet)
    print_diffs(changes, quiet)

    # Save diffs if requested
    if getattr(args, "save_diffs", None) and changes:
        save_diff_files(changes, args.save_diffs)

    # Always dump latest pages to disk
    dump_dir = Path(getattr(args, "dump", None) or "data/pages")
    dump_dir.mkdir(parents=True, exist_ok=True)
    written = 0
    for result in results:
        if result["content"]:
            filename = url_to_filename(result["url"])
            (dump_dir / filename).write_text(result["content"], encoding="utf-8")
            written += 1
    if HAS_RICH:
        console.print(f"[green]Updated {written} pages in {dump_dir}/[/green]")
    else:
        print(f"Updated {written} pages in {dump_dir}/")

    # Step 6: Generate reports
    report_dir = Path(getattr(args, "report", None) or "data")
    report_data = {
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "first_run": first_run,
        "total": len(urls),
        "urls": urls,
        "changes": changes,
        "added": added_urls_display,
        "removed": removed_urls_display,
        "errors": errors,
    }
    generate_md_report(report_data, report_dir)
    generate_html_report(report_data, report_dir)
    append_md_history(report_data, report_dir)
    append_html_history(report_data, report_dir)
    if HAS_RICH:
        console.print(f"[green]Reports written to {report_dir}/ (report + history)[/green]")
    else:
        print(f"Reports written to {report_dir}/ (report + history)")


async def cmd_check_poll(args):
    """Run check in a polling loop."""
    interval = getattr(args, "poll", None)
    if not interval:
        await cmd_check(args)
        return

    while True:
        if HAS_RICH:
            console.print(f"\n[bold]{'═' * 60}[/bold]")
            console.print(f"[bold]Check at {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}[/bold]")
        else:
            print(f"\n{'═' * 60}")
            print(f"Check at {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
        await cmd_check(args)
        if HAS_RICH:
            console.print(f"\n[dim]Next check in {interval} seconds...[/dim]")
        else:
            print(f"\nNext check in {interval} seconds...")
        await asyncio.sleep(interval)


def cmd_history(args):
    """Show change history for a URL or all URLs."""
    conn = init_db()
    url = getattr(args, "url", None)
    rows = get_page_history(conn, url, limit=50)

    if not rows:
        print("No history found.")
        return

    if HAS_RICH:
        table = Table(title=f"History{f' for {url}' if url else ''}")
        table.add_column("URL", max_width=50)
        table.add_column("Fetched At")
        table.add_column("Status", justify="right")
        table.add_column("Hash (first 12)")
        if url:
            table.add_column("Error")
        for row in rows:
            hash_short = row["hash"][:12] if row["hash"] else "—"
            status = str(row["status_code"]) if row["status_code"] else "—"
            cols = [row["url"], row["fetched_at"], status, hash_short]
            if url:
                cols.append(row["error"] or "")
            table.add_row(*cols)
        console.print(table)
    else:
        print(f"\nHistory{f' for {url}' if url else ''}:")
        print(f"{'URL':<50} {'Fetched At':<28} {'Status':>6} {'Hash (12)':>14}")
        print("─" * 100)
        for row in rows:
            hash_short = row["hash"][:12] if row["hash"] else "—"
            status = str(row["status_code"]) if row["status_code"] else "—"
            print(f"{row['url']:<50} {row['fetched_at']:<28} {status:>6} {hash_short:>14}")


def cmd_diff(args):
    """Show diff between two most recent snapshots of a URL."""
    conn = init_db()
    url = args.url

    newest, previous = get_two_snapshots(conn, url)
    if not newest:
        print(f"No snapshots found for {url}")
        return
    if not previous:
        print(f"Only one snapshot found for {url} — no diff available.")
        return

    if newest["hash"] == previous["hash"]:
        print(f"No changes between the two most recent snapshots of {url}")
        return

    diff_text = compute_diff(
        previous["content"] or "", newest["content"] or "", url
    )
    if HAS_RICH:
        console.print(f"\n[bold]Diff for {url}[/bold]")
        console.print(f"[dim]From: {previous['fetched_at']}[/dim]")
        console.print(f"[dim]To:   {newest['fetched_at']}[/dim]\n")
        console.print(Syntax(diff_text, "diff", theme="monokai"))
    else:
        print(f"\nDiff for {url}")
        print(f"From: {previous['fetched_at']}")
        print(f"To:   {newest['fetched_at']}\n")
        print(diff_text)


def url_to_filename(url: str) -> str:
    """Derive a clean .md filename from a doc URL.

    https://code.claude.com/docs/en/best-practices.md → best-practices.md
    """
    path = url.split("/docs/en/", 1)[-1] if "/docs/en/" in url else url.rsplit("/", 1)[-1]
    if not path.endswith(".md"):
        path = path.rstrip("/").replace("/", "_") + ".md"
    return path


def cmd_rebuild_history(args):
    """Rebuild history.html and history.md from all stored snapshots."""
    conn = init_db()
    include_html = getattr(args, "include_html", False)
    output_dir = Path(getattr(args, "report", None) or "data")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Delete existing history files
    for f in ("history.html", "history.md"):
        p = output_dir / f
        if p.exists():
            p.unlink()

    # Get all index snapshots in order — each represents a run
    index_rows = conn.execute(
        "SELECT id, fetched_at, urls_json FROM index_snapshots ORDER BY id"
    ).fetchall()

    if not index_rows:
        print("No snapshots in database. Run 'check' first.")
        return

    # For each consecutive pair of index snapshots, reconstruct what changed
    entries_written = 0
    for run_idx, idx_row in enumerate(index_rows):
        run_time = idx_row["fetched_at"]
        current_urls = json.loads(idx_row["urls_json"])

        # Determine time window: from this index fetch to the next (or far future)
        if run_idx + 1 < len(index_rows):
            next_time = index_rows[run_idx + 1]["fetched_at"]
        else:
            next_time = "9999-12-31T23:59:59+00:00"

        # Get page snapshots for this run (fetched between this index and the next)
        page_rows = conn.execute(
            "SELECT url, content, hash, status_code, error "
            "FROM page_snapshots WHERE fetched_at >= ? AND fetched_at < ? "
            "ORDER BY id",
            (run_time, next_time),
        ).fetchall()

        if not page_rows:
            continue

        # Build a lookup of this run's pages
        run_pages = {}
        for pr in page_rows:
            run_pages[pr["url"]] = dict(pr)

        # First run or subsequent?
        if run_idx == 0:
            timestamp = datetime.fromisoformat(run_time).strftime("%Y-%m-%d %H:%M:%S UTC")
            report_data = {
                "timestamp": timestamp,
                "first_run": True,
                "total": len(current_urls),
                "urls": current_urls,
                "changes": [],
                "added": [],
                "removed": [],
                "errors": [run_pages[u] for u in run_pages if run_pages[u]["error"]],
            }
        else:
            prev_urls = json.loads(index_rows[run_idx - 1]["urls_json"])
            added = sorted(set(current_urls) - set(prev_urls))
            removed = sorted(set(prev_urls) - set(current_urls))

            # Get previous run's page snapshots for comparison
            prev_time = index_rows[run_idx - 1]["fetched_at"]
            prev_page_rows = conn.execute(
                "SELECT url, content, hash FROM page_snapshots "
                "WHERE fetched_at >= ? AND fetched_at < ? ORDER BY id",
                (prev_time, run_time),
            ).fetchall()
            prev_pages = {}
            for pr in prev_page_rows:
                prev_pages[pr["url"]] = dict(pr)

            # Compute diffs
            changes = []
            for url in current_urls:
                cur = run_pages.get(url)
                prev = prev_pages.get(url)
                if cur and prev and cur["hash"] and prev["hash"]:
                    if cur["hash"] != prev["hash"] and cur["content"] and prev["content"]:
                        diff_text = compute_diff(prev["content"], cur["content"], url)
                        changes.append({"url": url, "diff": diff_text})

            errors = [run_pages[u] for u in run_pages if run_pages[u].get("error")]

            # Filter HTML noise unless --include-html
            if not include_html:
                changes = [ch for ch in changes if not (ch["diff"] and is_html_diff(ch["diff"]))]

            timestamp = datetime.fromisoformat(run_time).strftime("%Y-%m-%d %H:%M:%S UTC")
            report_data = {
                "timestamp": timestamp,
                "first_run": False,
                "total": len(current_urls),
                "urls": current_urls,
                "changes": changes,
                "added": added,
                "removed": removed,
                "errors": errors,
            }

        append_md_history(report_data, output_dir)
        append_html_history(report_data, output_dir)
        entries_written += 1

        n_changes = len(report_data["changes"])
        n_added = len(report_data["added"])
        label = "first run" if report_data["first_run"] else f"{n_changes} changes, {n_added} added"
        if HAS_RICH:
            console.print(f"  [dim]Run {entries_written}: {report_data['timestamp']} — {label}[/dim]")
        else:
            print(f"  Run {entries_written}: {report_data['timestamp']} — {label}")

    if HAS_RICH:
        console.print(f"\n[green]Rebuilt history from {entries_written} runs → "
                      f"{output_dir}/history.html and {output_dir}/history.md[/green]")
    else:
        print(f"\nRebuilt history from {entries_written} runs → "
              f"{output_dir}/history.html and {output_dir}/history.md")


def cmd_dump(args):
    """Dump latest snapshot content to .md files in a directory."""
    conn = init_db()
    tracked = get_all_tracked_urls(conn)

    if not tracked:
        print("No snapshots yet. Run 'check' first.")
        return

    out_dir = Path(args.dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    written = 0
    for row in tracked:
        # Get full content from the latest snapshot
        snap = get_last_page_snapshot(conn, row["url"])
        if not snap or not snap["content"]:
            continue
        filename = url_to_filename(row["url"])
        (out_dir / filename).write_text(snap["content"], encoding="utf-8")
        written += 1

    if HAS_RICH:
        console.print(f"[green]Dumped {written} pages to {out_dir}/[/green]")
    else:
        print(f"Dumped {written} pages to {out_dir}/")


# ── AI Digest ─────────────────────────────────────────────────────────────

_DIGEST_INSTRUCTION = """\
Analyze the Claude Code documentation diffs provided on stdin and produce a concise change digest.

Format your response exactly as:

### Executive Summary
2-3 sentences on what changed and why it matters.

### New Features
- Feature name: one-line description

### Breaking Changes
- What changed and what to do about it

### Deprecations
- What's being phased out

### Flag & API Changes
- New/renamed/removed CLI flags or settings

### Notable Clarifications
- Documentation improvements worth knowing about

### Action Items
- [ ] Specific things to update in your workflows

Omit any section that has no items. Be concise — bullet points, not paragraphs."""

_STRUCTURED_DIGEST_INSTRUCTION = """\
Classify each documentation change from the diffs provided on stdin.

For each changed URL, produce a JSON object with:
- url: the full URL that changed
- category: one of "feature", "breaking", "deprecation", "clarification", "flag_change", "bugfix"
- severity: one of "high", "medium", "low"
- summary: one-line description of what changed
- details: 2-3 sentence explanation
- action_required: what the user should do (null if nothing)
- tags: array of keyword tags (e.g. ["hooks", "permissions", "cli"])

Severity guide:
- high: breaking changes, removed features, security-related
- medium: new features, flag changes, deprecations
- low: clarifications, typo fixes, minor rewording

Return a JSON object: {"events": [...]}\
"""

_STRUCTURED_DIGEST_SCHEMA = json.dumps({
    "type": "object",
    "properties": {
        "events": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "url": {"type": "string"},
                    "category": {"type": "string", "enum": [
                        "feature", "breaking", "deprecation",
                        "clarification", "flag_change", "bugfix"]},
                    "severity": {"type": "string", "enum": ["high", "medium", "low"]},
                    "summary": {"type": "string"},
                    "details": {"type": "string"},
                    "action_required": {"type": ["string", "null"]},
                    "tags": {"type": "array", "items": {"type": "string"}}
                },
                "required": ["url", "category", "severity", "summary", "details", "tags"]
            }
        }
    },
    "required": ["events"]
})


def _extract_report_timestamp(report_text: str) -> str | None:
    """Extract the timestamp from a report's *Generated: ...* line."""
    m = re.search(r'\*Generated:\s*(.+?)\*', report_text)
    return m.group(1).strip() if m else None


def _extract_diff_for_url(diffs_text: str, url: str) -> str | None:
    """Extract the diff block for a specific URL from the diffs section."""
    marker = f"### {url}\n"
    idx = diffs_text.find(marker)
    if idx == -1:
        return None
    start = idx + len(marker)
    # Find next ### or end
    next_marker = diffs_text.find("\n### ", start)
    block = diffs_text[start:next_marker] if next_marker != -1 else diffs_text[start:]
    # Strip code fences
    block = block.strip()
    if block.startswith("```diff"):
        block = block[len("```diff"):].strip()
    if block.endswith("```"):
        block = block[:-3].strip()
    return block


def _extract_added_pages(report_text: str) -> list[str]:
    """Parse URLs from ## Added Pages section."""
    m = re.search(r'## Added Pages\s*\n((?:- .+\n?)+)', report_text)
    if not m:
        return []
    return re.findall(r'- (https?://\S+)', m.group(1))


def _extract_removed_pages(report_text: str) -> list[str]:
    """Parse URLs from ## Removed Pages section."""
    m = re.search(r'## Removed Pages\s*\n((?:- .+\n?)+)', report_text)
    if not m:
        return []
    return re.findall(r'- (https?://\S+)', m.group(1))


def _parse_relative_date(date_str: str) -> str:
    """Parse date strings: '7d' → 7 days ago, ISO dates pass through."""
    m = re.match(r'^(\d+)d$', date_str.strip())
    if m:
        days = int(m.group(1))
        dt = datetime.now(timezone.utc) - timedelta(days=days)
        return dt.isoformat()
    # Try ISO or bare date
    if re.match(r'^\d{4}-\d{2}-\d{2}$', date_str.strip()):
        return date_str.strip() + "T00:00:00+00:00"
    return date_str.strip()


def _generate_digest_html(digest_md: str, output_dir: Path):
    """Write a self-contained HTML digest to output_dir/digest.html."""
    output_dir.mkdir(parents=True, exist_ok=True)

    # Convert markdown to simple HTML
    body_lines = []
    in_list = False
    for line in digest_md.splitlines():
        stripped = line.strip()
        if stripped.startswith("### "):
            if in_list:
                body_lines.append("</ul>")
                in_list = False
            body_lines.append(f"<h3>{_esc_html(stripped[4:])}</h3>")
        elif stripped.startswith("## "):
            if in_list:
                body_lines.append("</ul>")
                in_list = False
            body_lines.append(f"<h2>{_esc_html(stripped[3:])}</h2>")
        elif stripped.startswith("- [ ] "):
            if not in_list:
                body_lines.append("<ul>")
                in_list = True
            body_lines.append(f"<li><input type='checkbox' disabled> {_esc_html(stripped[6:])}</li>")
        elif stripped.startswith("- "):
            if not in_list:
                body_lines.append("<ul>")
                in_list = True
            body_lines.append(f"<li>{_esc_html(stripped[2:])}</li>")
        elif stripped:
            if in_list:
                body_lines.append("</ul>")
                in_list = False
            body_lines.append(f"<p>{_esc_html(stripped)}</p>")
    if in_list:
        body_lines.append("</ul>")

    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    html = (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n"
        f"<title>Claude Docs Change Digest</title>\n<style>\n{_HTML_CSS}\n</style>\n</head>\n"
        f"<body>\n<h1>Claude Docs Change Digest</h1>\n"
        f'<p class="ts">{_esc_html(ts)}</p>\n'
        f"{''.join(body_lines)}\n</body>\n</html>\n"
    )
    (output_dir / "digest.html").write_text(html, encoding="utf-8")


def _run_structured_classification(report_text: str, diffs: str, model: str, env: dict,
                                   report_dir: Path) -> list[dict] | None:
    """Run structured JSON classification of changes. Returns list of events or None on failure."""
    run_timestamp = _extract_report_timestamp(report_text) or utcnow()
    conn = init_db(report_dir / "snapshots.db" if (report_dir / "snapshots.db").exists() else DB_PATH)

    # Check for duplicate events
    existing = conn.execute(
        "SELECT COUNT(*) as cnt FROM change_events WHERE run_timestamp = ?", (run_timestamp,)
    ).fetchone()
    if existing and existing["cnt"] > 0:
        if HAS_RICH:
            console.print(f"[dim]Structured classification already exists for {run_timestamp} "
                          f"({existing['cnt']} events) — skipping.[/dim]")
        else:
            print(f"Structured classification already exists for {run_timestamp} "
                  f"({existing['cnt']} events) — skipping.")
        return None

    stdin_text = f"## Diffs to classify:\n\n{diffs}"

    if HAS_RICH:
        console.print("[bold blue]Running structured classification...[/bold blue]")
    else:
        print("Running structured classification...")

    try:
        result = subprocess.run(
            ["claude", "-p", _STRUCTURED_DIGEST_INSTRUCTION, "--model", model,
             "--max-turns", "1", "--output-format", "json",
             "--json-schema", _STRUCTURED_DIGEST_SCHEMA],
            input=stdin_text,
            capture_output=True, text=True, timeout=300, env=env,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError) as exc:
        print(f"Warning: structured classification failed ({exc}). Continuing with text digest.")
        return None

    if result.returncode != 0:
        print(f"Warning: structured classification exited with code {result.returncode}. "
              f"Continuing with text digest.")
        return None

    raw = result.stdout.strip()
    if not raw:
        print("Warning: structured classification returned empty output. Continuing with text digest.")
        return None

    # Parse the JSON — claude CLI may wrap in {"type":"result","result":"..."}
    try:
        parsed = json.loads(raw)
        if isinstance(parsed, dict) and "result" in parsed and isinstance(parsed["result"], str):
            parsed = json.loads(parsed["result"])
        events = parsed.get("events", [])
    except (json.JSONDecodeError, AttributeError) as exc:
        print(f"Warning: failed to parse structured output ({exc}). Continuing with text digest.")
        return None

    # Store each event
    stored = 0
    for ev in events:
        diff_text = _extract_diff_for_url(diffs, ev.get("url", ""))
        store_change_event(conn, run_timestamp, ev.get("url", ""), "changed",
                           diff_text=diff_text, ai_result=ev)
        stored += 1

    # Also store added/removed pages
    for url in _extract_added_pages(report_text):
        store_change_event(conn, run_timestamp, url, "added", ai_result={
            "category": "feature", "severity": "medium",
            "summary": f"New documentation page: {url_to_filename(url)}",
            "details": "A new page was added to the documentation index.",
            "tags": ["new-page"],
        })
        stored += 1
    for url in _extract_removed_pages(report_text):
        store_change_event(conn, run_timestamp, url, "removed", ai_result={
            "category": "breaking", "severity": "high",
            "summary": f"Documentation page removed: {url_to_filename(url)}",
            "details": "A page was removed from the documentation index.",
            "tags": ["removed-page"],
        })
        stored += 1

    conn.commit()
    if HAS_RICH:
        console.print(f"[green]Stored {stored} change events for run {run_timestamp}[/green]")
    else:
        print(f"Stored {stored} change events for run {run_timestamp}")

    return events


def _create_gh_issues(report_text: str, report_dir: Path, gh_repo: str | None = None):
    """Create GitHub issues for breaking changes. Called when --gh-issue is set."""
    if not shutil.which("gh"):
        print("Warning: 'gh' CLI not found — skipping GitHub issue creation.")
        return

    run_timestamp = _extract_report_timestamp(report_text) or utcnow()
    conn = init_db(report_dir / "snapshots.db" if (report_dir / "snapshots.db").exists() else DB_PATH)
    events = get_change_events_for_run(conn, run_timestamp)
    breaking = [e for e in events if e["category"] == "breaking" and not e["gh_issue_url"]]

    if not breaking:
        print("No breaking changes to create issues for.")
        return

    repo_flag = ["--repo", gh_repo] if gh_repo else []
    created = 0
    for ev in breaking:
        title = f"[Claude Docs] Breaking: {ev['summary']}"
        tags = json.loads(ev["tags_json"]) if ev["tags_json"] else []
        body = (
            f"## Breaking Documentation Change\n\n"
            f"**Page:** {ev['url']}\n"
            f"**Severity:** {ev['severity']}\n"
            f"**Detected:** {ev['run_timestamp']}\n\n"
            f"### Details\n\n{ev['details']}\n\n"
        )
        if ev["action_required"]:
            body += f"### Action Required\n\n{ev['action_required']}\n\n"
        if tags:
            body += f"**Tags:** {', '.join(tags)}\n\n"
        body += "*Auto-generated by claude_docs_monitor*"

        try:
            cmd = ["gh", "issue", "create", "--title", title, "--body", body,
                   "--label", "claude-docs,breaking-change"] + repo_flag
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            if res.returncode == 0:
                issue_url = res.stdout.strip()
                update_change_event_issue(conn, ev["id"], issue_url)
                created += 1
                print(f"  Created issue: {issue_url}")
            else:
                print(f"  Warning: failed to create issue for '{ev['summary']}': {res.stderr[:200]}")
        except (subprocess.TimeoutExpired, FileNotFoundError) as exc:
            print(f"  Warning: gh issue create failed ({exc})")

    conn.commit()
    if created:
        print(f"Created {created} GitHub issue(s) for breaking changes.")


def cmd_digest(args):
    """AI-analyze latest diffs into an actionable digest."""
    report_dir = Path(args.report) if args.report else DB_DIR
    report_path = report_dir / "report.md"

    if not report_path.exists():
        print("No report found. Run 'check' first to generate a report.")
        sys.exit(1)

    report_text = report_path.read_text(encoding="utf-8")

    # Check for no changes
    if "| Changed | 0 |" in report_text and "| Added | 0 |" in report_text:
        print("No changes to digest.")
        return

    # Extract diffs section to minimize token usage
    diffs_marker = "\n## Diffs\n"
    if diffs_marker in report_text:
        diffs = report_text[report_text.index(diffs_marker) + len(diffs_marker):]
    else:
        # No diffs section — might be added/removed pages only
        diffs = report_text

    if not diffs.strip():
        print("No diffs found in report.")
        return

    # Check that claude CLI is available
    if not shutil.which("claude"):
        print("Error: 'claude' CLI not found in PATH.")
        print("Install Claude Code: https://docs.anthropic.com/en/docs/claude-code")
        sys.exit(1)

    model = getattr(args, "model", "sonnet")

    # Allow running inside a Claude Code session (nested invocation)
    env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}

    # Phase 1: Structured classification (stores events in DB)
    _run_structured_classification(report_text, diffs, model, env, report_dir)

    # Phase 2: Text digest (existing behavior)
    stdin_text = f"## Diffs to analyze:\n\n{diffs}"

    if HAS_RICH:
        console.print("[bold blue]Generating AI digest...[/bold blue]")
    else:
        print("Generating AI digest...")

    try:
        result = subprocess.run(
            ["claude", "-p", _DIGEST_INSTRUCTION, "--model", model,
             "--max-turns", "1", "--output-format", "text"],
            input=stdin_text,
            capture_output=True, text=True, timeout=300, env=env,
        )
    except subprocess.TimeoutExpired:
        print("Error: claude CLI timed out after 300 seconds.")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: 'claude' CLI not found.")
        sys.exit(1)

    if result.returncode != 0:
        print(f"Error: claude CLI exited with code {result.returncode}")
        if result.stderr:
            print(result.stderr[:500])
        sys.exit(1)

    digest_text = result.stdout.strip()
    if not digest_text:
        print("Error: claude CLI returned empty output.")
        sys.exit(1)

    # Write outputs
    report_dir.mkdir(parents=True, exist_ok=True)
    digest_md_path = report_dir / "digest.md"
    digest_md_path.write_text(
        f"# Claude Docs Change Digest\n\n"
        f"*Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}*\n\n"
        f"{digest_text}\n",
        encoding="utf-8",
    )

    _generate_digest_html(digest_text, report_dir)

    # Print to terminal
    if HAS_RICH:
        console.print()
        console.print(Panel(digest_text, title="Change Digest", border_style="green"))
    else:
        print()
        print("=" * 60)
        print("CHANGE DIGEST")
        print("=" * 60)
        print(digest_text)
        print("=" * 60)

    print(f"\nDigest written to {digest_md_path} and {report_dir / 'digest.html'}")

    # Phase 3: GitHub issue creation (if requested)
    if getattr(args, "gh_issue", False):
        gh_repo = getattr(args, "gh_repo", None)
        _create_gh_issues(report_text, report_dir, gh_repo)


def cmd_query(args):
    """Query the change intelligence database."""
    conn = init_db()
    keyword = getattr(args, "keyword", None)
    category = getattr(args, "category", None)
    severity = getattr(args, "severity", None)
    page = getattr(args, "page", None)
    since = getattr(args, "since", None)
    until_date = getattr(args, "until", None)
    limit = getattr(args, "limit", 50)
    as_json = getattr(args, "json", False)

    # Smart shortcut: if keyword matches a category name, redirect
    known_categories = {"feature", "breaking", "deprecation", "clarification", "flag_change", "bugfix"}
    if keyword and keyword.lower() in known_categories and not category:
        category = keyword.lower()
        keyword = None

    # Parse relative dates
    if since:
        since = _parse_relative_date(since)
    if until_date:
        until_date = _parse_relative_date(until_date)

    rows = query_change_events(conn, category=category, severity=severity,
                               page_name=page, keyword=keyword,
                               since=since, until=until_date, limit=limit)

    if not rows:
        print("No change events found matching your query.")
        return

    if as_json:
        events = []
        for r in rows:
            ev = dict(r)
            if ev.get("tags_json"):
                ev["tags"] = json.loads(ev["tags_json"])
                del ev["tags_json"]
            else:
                ev["tags"] = []
                ev.pop("tags_json", None)
            ev.pop("diff_text", None)
            events.append(ev)
        print(json.dumps({"events": events, "count": len(events)}, indent=2))
        return

    # Display results
    severity_colors = {"high": "red", "medium": "yellow", "low": "green"}
    category_colors = {"breaking": "red", "deprecation": "yellow", "feature": "green",
                       "clarification": "cyan", "flag_change": "magenta", "bugfix": "blue"}

    if HAS_RICH:
        table = Table(title=f"Change Events ({len(rows)} results)")
        table.add_column("Date", style="dim", max_width=20)
        table.add_column("Page", max_width=25)
        table.add_column("Type", max_width=10)
        table.add_column("Cat", max_width=15)
        table.add_column("Sev", max_width=6)
        table.add_column("Summary", max_width=50)
        for r in rows:
            ts = r["run_timestamp"][:19] if r["run_timestamp"] else "—"
            cat = r["category"] or "—"
            sev = r["severity"] or "—"
            cat_color = category_colors.get(cat, "white")
            sev_color = severity_colors.get(sev, "white")
            table.add_row(
                ts,
                r["page_name"] or "—",
                r["event_type"] or "—",
                f"[{cat_color}]{cat}[/{cat_color}]",
                f"[{sev_color}]{sev}[/{sev_color}]",
                r["summary"] or "—",
            )
        console.print(table)

        # Show details for high-severity items
        high = [r for r in rows if r["severity"] == "high"]
        if high:
            console.print(f"\n[bold red]High-severity details:[/bold red]")
            for r in high:
                console.print(f"\n  [bold]{r['summary']}[/bold]")
                if r["details"]:
                    console.print(f"  {r['details']}")
                if r["action_required"]:
                    console.print(f"  [yellow]Action: {r['action_required']}[/yellow]")
    else:
        print(f"\nChange Events ({len(rows)} results):")
        print(f"{'Date':<20} {'Page':<25} {'Type':<10} {'Category':<15} {'Sev':<6} Summary")
        print("─" * 120)
        for r in rows:
            ts = r["run_timestamp"][:19] if r["run_timestamp"] else "—"
            print(f"{ts:<20} {(r['page_name'] or '—'):<25} {(r['event_type'] or '—'):<10} "
                  f"{(r['category'] or '—'):<15} {(r['severity'] or '—'):<6} {r['summary'] or '—'}")

        high = [r for r in rows if r["severity"] == "high"]
        if high:
            print(f"\nHigh-severity details:")
            for r in high:
                print(f"\n  {r['summary']}")
                if r["details"]:
                    print(f"  {r['details']}")
                if r["action_required"]:
                    print(f"  Action: {r['action_required']}")


def cmd_backfill(args):
    """Populate change_events from existing snapshot history."""
    conn = init_db()
    model = getattr(args, "model", "sonnet")
    dry_run = getattr(args, "dry_run", False)
    include_html = getattr(args, "include_html", False)

    # Get all index snapshots in order
    index_rows = conn.execute(
        "SELECT id, fetched_at, urls_json FROM index_snapshots ORDER BY id"
    ).fetchall()

    if not index_rows:
        print("No snapshots in database. Run 'check' first.")
        return

    if not shutil.which("claude") and not dry_run:
        print("Error: 'claude' CLI not found in PATH.")
        sys.exit(1)

    env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}

    runs_to_classify = []
    for run_idx in range(1, len(index_rows)):
        idx_row = index_rows[run_idx]
        run_time = idx_row["fetched_at"]
        current_urls = json.loads(idx_row["urls_json"])

        # Check if already classified
        existing = conn.execute(
            "SELECT COUNT(*) as cnt FROM change_events WHERE run_timestamp = ?",
            (datetime.fromisoformat(run_time).strftime("%Y-%m-%d %H:%M:%S UTC"),)
        ).fetchone()
        if existing and existing["cnt"] > 0:
            continue

        # Determine time window
        prev_time = index_rows[run_idx - 1]["fetched_at"]
        if run_idx + 1 < len(index_rows):
            next_time = index_rows[run_idx + 1]["fetched_at"]
        else:
            next_time = "9999-12-31T23:59:59+00:00"

        prev_urls = json.loads(index_rows[run_idx - 1]["urls_json"])

        # Get page snapshots for both runs
        cur_pages = {}
        for pr in conn.execute(
            "SELECT url, content, hash FROM page_snapshots "
            "WHERE fetched_at >= ? AND fetched_at < ? ORDER BY id",
            (run_time, next_time),
        ).fetchall():
            cur_pages[pr["url"]] = dict(pr)

        prev_pages = {}
        for pr in conn.execute(
            "SELECT url, content, hash FROM page_snapshots "
            "WHERE fetched_at >= ? AND fetched_at < ? ORDER BY id",
            (prev_time, run_time),
        ).fetchall():
            prev_pages[pr["url"]] = dict(pr)

        # Compute diffs
        changes = []
        for url in current_urls:
            cur = cur_pages.get(url)
            prev = prev_pages.get(url)
            if cur and prev and cur["hash"] and prev["hash"]:
                if cur["hash"] != prev["hash"] and cur["content"] and prev["content"]:
                    diff_text = compute_diff(prev["content"], cur["content"], url)
                    if not include_html and is_html_diff(diff_text):
                        continue
                    changes.append({"url": url, "diff": diff_text})

        added = sorted(set(current_urls) - set(prev_urls))
        removed = sorted(set(prev_urls) - set(current_urls))

        if changes or added or removed:
            timestamp = datetime.fromisoformat(run_time).strftime("%Y-%m-%d %H:%M:%S UTC")
            runs_to_classify.append({
                "timestamp": timestamp,
                "changes": changes,
                "added": added,
                "removed": removed,
            })

    if not runs_to_classify:
        print("No unclassified runs found. All runs already have change events.")
        return

    print(f"Found {len(runs_to_classify)} unclassified run(s) with changes.")

    if dry_run:
        for run in runs_to_classify:
            n_ch = len(run["changes"])
            n_add = len(run["added"])
            n_rm = len(run["removed"])
            print(f"  {run['timestamp']}: {n_ch} changes, {n_add} added, {n_rm} removed")
        print("\n(Dry run — no API calls made.)")
        return

    classified = 0
    for run in runs_to_classify:
        # Build diffs text
        diffs_lines = []
        for ch in run["changes"]:
            diffs_lines.append(f"### {ch['url']}\n")
            diffs_lines.append("```diff")
            diffs_lines.append(ch["diff"])
            diffs_lines.append("```\n")
        diffs_text = "\n".join(diffs_lines)

        # Build minimal report text for helpers
        report_text = f"*Generated: {run['timestamp']}*\n"
        if run["added"]:
            report_text += "\n## Added Pages\n\n" + "\n".join(f"- {u}" for u in run["added"]) + "\n"
        if run["removed"]:
            report_text += "\n## Removed Pages\n\n" + "\n".join(f"- {u}" for u in run["removed"]) + "\n"

        if diffs_text.strip():
            stdin_text = f"## Diffs to classify:\n\n{diffs_text}"
            if HAS_RICH:
                console.print(f"[dim]Classifying run {run['timestamp']}...[/dim]")
            else:
                print(f"Classifying run {run['timestamp']}...")

            try:
                result = subprocess.run(
                    ["claude", "-p", _STRUCTURED_DIGEST_INSTRUCTION, "--model", model,
                     "--max-turns", "1", "--output-format", "json",
                     "--json-schema", _STRUCTURED_DIGEST_SCHEMA],
                    input=stdin_text,
                    capture_output=True, text=True, timeout=300, env=env,
                )
                if result.returncode == 0 and result.stdout.strip():
                    parsed = json.loads(result.stdout.strip())
                    if isinstance(parsed, dict) and "result" in parsed and isinstance(parsed["result"], str):
                        parsed = json.loads(parsed["result"])
                    events = parsed.get("events", [])
                    for ev in events:
                        diff_text = _extract_diff_for_url(diffs_text, ev.get("url", ""))
                        store_change_event(conn, run["timestamp"], ev.get("url", ""), "changed",
                                           diff_text=diff_text, ai_result=ev)
                else:
                    print(f"  Warning: classification failed for {run['timestamp']}")
            except (subprocess.TimeoutExpired, json.JSONDecodeError) as exc:
                print(f"  Warning: classification failed for {run['timestamp']}: {exc}")

        # Store added/removed pages
        for url in run["added"]:
            store_change_event(conn, run["timestamp"], url, "added", ai_result={
                "category": "feature", "severity": "medium",
                "summary": f"New documentation page: {url_to_filename(url)}",
                "details": "A new page was added to the documentation index.",
                "tags": ["new-page"],
            })
        for url in run["removed"]:
            store_change_event(conn, run["timestamp"], url, "removed", ai_result={
                "category": "breaking", "severity": "high",
                "summary": f"Documentation page removed: {url_to_filename(url)}",
                "details": "A page was removed from the documentation index.",
                "tags": ["removed-page"],
            })

        conn.commit()
        classified += 1

    if HAS_RICH:
        console.print(f"\n[green]Backfilled {classified} run(s) into change_events table.[/green]")
    else:
        print(f"\nBackfilled {classified} run(s) into change_events table.")


def cmd_urls(args):
    """List all monitored URLs with latest status."""
    conn = init_db()
    tracked = get_all_tracked_urls(conn)

    if not tracked:
        print("No URLs tracked yet. Run 'check' first.")
        return

    if HAS_RICH:
        table = Table(title=f"Tracked URLs ({len(tracked)} pages)")
        table.add_column("#", justify="right", style="dim")
        table.add_column("URL", max_width=60)
        table.add_column("Last Fetched")
        table.add_column("Status", justify="right")
        table.add_column("Hash (first 12)")
        for i, row in enumerate(tracked, 1):
            hash_short = row["hash"][:12] if row["hash"] else "—"
            status = str(row["status_code"]) if row["status_code"] else "—"
            style = "red" if row.get("error") else ""
            table.add_row(str(i), row["url"], row["fetched_at"], status, hash_short, style=style)
        console.print(table)
    else:
        print(f"\nTracked URLs ({len(tracked)} pages):")
        print(f"{'#':>3} {'URL':<60} {'Last Fetched':<28} {'Status':>6} {'Hash (12)':>14}")
        print("─" * 115)
        for i, row in enumerate(tracked, 1):
            hash_short = row["hash"][:12] if row["hash"] else "—"
            status = str(row["status_code"]) if row["status_code"] else "—"
            print(f"{i:>3} {row['url']:<60} {row['fetched_at']:<28} {status:>6} {hash_short:>14}")


# ── CLI ─────────────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="claude_docs_monitor",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Monitor Claude Code documentation (code.claude.com/docs/) for changes.",
        epilog="""examples:
  %(prog)s                              fetch all pages, show diffs, update data/pages/
  %(prog)s check --quiet                summary table only, no inline diffs
  %(prog)s check --save-diffs out/      also write .diff files to out/
  %(prog)s check --dump ~/docs          dump pages to ~/docs instead of data/pages/
  %(prog)s check --poll 3600            re-check every hour
  %(prog)s history                      show recent snapshot history (all pages)
  %(prog)s history URL                  show history for one page
  %(prog)s diff URL                     show diff between last two snapshots of a page
  %(prog)s urls                         list all tracked URLs with status
  %(prog)s rebuild-history               regenerate history files from DB
  %(prog)s dump                         export latest snapshots to data/pages/
  %(prog)s dump ~/review                export to a custom directory
  %(prog)s digest                       AI-analyze latest diffs into an actionable digest
  %(prog)s digest --model opus          use a different model for analysis
  %(prog)s digest --gh-issue            create GitHub issues for breaking changes
  %(prog)s query breaking               show all breaking changes
  %(prog)s query --since 7d             changes in the last 7 days
  %(prog)s query "hooks" --severity high  keyword search with severity filter
  %(prog)s query --json | jq .          machine-readable output
  %(prog)s backfill                     classify historical changes with AI
  %(prog)s backfill --dry-run           preview what would be classified""",
    )
    sub = parser.add_subparsers(dest="command")

    # check
    check_p = sub.add_parser(
        "check",
        help="Fetch all pages, detect changes, show diffs, update local copies (default)",
        description="Fetch every doc page, compare against the previous snapshot, "
                    "display a change summary with unified diffs, and update "
                    "the local .md files in data/pages/.",
    )
    check_p.add_argument(
        "--save-diffs", metavar="DIR",
        help="Write a .diff file per changed page to DIR",
    )
    check_p.add_argument(
        "--poll", type=int, metavar="SEC",
        help="Re-run automatically every SEC seconds",
    )
    check_p.add_argument(
        "--quiet", action="store_true",
        help="Print summary table only, suppress inline diffs",
    )
    check_p.add_argument(
        "--dump", metavar="DIR",
        help="Override page dump directory (default: data/pages)",
    )
    check_p.add_argument(
        "--report", metavar="DIR",
        help="Override report output directory (default: data/)",
    )
    check_p.add_argument(
        "--include-html", action="store_true",
        help="Include diffs that are predominantly HTML/script noise (suppressed by default)",
    )

    # history
    hist_p = sub.add_parser(
        "history",
        help="Show snapshot history for all pages or a specific URL",
    )
    hist_p.add_argument("url", nargs="?", help="Show history for this URL only")

    # diff
    diff_p = sub.add_parser(
        "diff",
        help="Show unified diff between the two most recent snapshots of a URL",
    )
    diff_p.add_argument("url", help="The page URL to diff")

    # urls
    sub.add_parser(
        "urls",
        help="List all monitored URLs with latest fetch status",
    )

    # rebuild-history
    rebuild_p = sub.add_parser(
        "rebuild-history",
        help="Rebuild history.html and history.md from all stored snapshots",
    )
    rebuild_p.add_argument(
        "--report", metavar="DIR",
        help="Override report output directory (default: data/)",
    )
    rebuild_p.add_argument(
        "--include-html", action="store_true",
        help="Include diffs that are predominantly HTML/script noise",
    )

    # dump
    dump_p = sub.add_parser(
        "dump",
        help="Export latest page snapshots as .md files (from DB, no network)",
    )
    dump_p.add_argument(
        "dir", nargs="?", default="data/pages",
        help="Output directory (default: data/pages)",
    )

    # digest
    digest_p = sub.add_parser(
        "digest",
        help="AI-analyze latest diffs into an actionable digest",
    )
    digest_p.add_argument(
        "--report", metavar="DIR",
        help="Report directory (default: data/)",
    )
    digest_p.add_argument(
        "--model", default="sonnet",
        help="Model alias (default: sonnet)",
    )
    digest_p.add_argument(
        "--gh-issue", action="store_true",
        help="Auto-create GitHub issues for breaking changes (requires gh CLI)",
    )
    digest_p.add_argument(
        "--gh-repo", metavar="OWNER/REPO",
        help="Target repository for issues (default: current repo)",
    )

    # query
    query_p = sub.add_parser(
        "query",
        help="Query the change intelligence database",
        description="Search and filter accumulated change events by category, severity, "
                    "page, keyword, or date range.",
    )
    query_p.add_argument(
        "keyword", nargs="?",
        help="Search keyword (or category shortcut: breaking, feature, deprecation, etc.)",
    )
    query_p.add_argument("--category", choices=[
        "feature", "breaking", "deprecation", "clarification", "flag_change", "bugfix"],
        help="Filter by change category",
    )
    query_p.add_argument(
        "--severity", choices=["high", "medium", "low"],
        help="Filter by severity level",
    )
    query_p.add_argument(
        "--page", metavar="NAME",
        help="Filter by page name (partial match, e.g. 'hooks.md')",
    )
    query_p.add_argument(
        "--since", metavar="DATE",
        help="Show events since DATE ('7d' for 7 days ago, or YYYY-MM-DD)",
    )
    query_p.add_argument(
        "--until", metavar="DATE",
        help="Show events until DATE ('7d' for 7 days ago, or YYYY-MM-DD)",
    )
    query_p.add_argument(
        "--limit", type=int, default=50,
        help="Maximum results (default: 50)",
    )
    query_p.add_argument(
        "--json", action="store_true",
        help="Output results as JSON",
    )

    # backfill
    backfill_p = sub.add_parser(
        "backfill",
        help="Populate change_events from existing snapshot history using AI classification",
    )
    backfill_p.add_argument(
        "--model", default="sonnet",
        help="Model alias (default: sonnet)",
    )
    backfill_p.add_argument(
        "--dry-run", action="store_true",
        help="Show what would be classified without making API calls",
    )
    backfill_p.add_argument(
        "--include-html", action="store_true",
        help="Include diffs that are predominantly HTML/script noise",
    )

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    # Default to "check" when no subcommand is given
    if not args.command:
        args.command = "check"
        args.save_diffs = None
        args.poll = None
        args.quiet = False
        args.dump = None
        args.report = None
        args.include_html = False

    if args.command == "check":
        if args.poll:
            asyncio.run(cmd_check_poll(args))
        else:
            asyncio.run(cmd_check(args))
    elif args.command == "history":
        cmd_history(args)
    elif args.command == "diff":
        cmd_diff(args)
    elif args.command == "urls":
        cmd_urls(args)
    elif args.command == "rebuild-history":
        cmd_rebuild_history(args)
    elif args.command == "dump":
        cmd_dump(args)
    elif args.command == "digest":
        cmd_digest(args)
    elif args.command == "query":
        cmd_query(args)
    elif args.command == "backfill":
        cmd_backfill(args)


if __name__ == "__main__":
    main()
