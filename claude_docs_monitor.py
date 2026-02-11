#!/usr/bin/env python3
"""Claude Code Documentation Change Monitor.

Polls all pages from code.claude.com/docs/, stores snapshots in SQLite,
and produces unified diffs when content changes.
"""

import argparse
import asyncio
import hashlib
import json
import re
import sqlite3
import sys
import time
from datetime import datetime, timezone
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

    # Step 4: Display report
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
  %(prog)s urls                         list all 56 tracked URLs with status
  %(prog)s dump                         export latest snapshots to data/pages/
  %(prog)s dump ~/review                export to a custom directory""",
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

    # dump
    dump_p = sub.add_parser(
        "dump",
        help="Export latest page snapshots as .md files (from DB, no network)",
    )
    dump_p.add_argument(
        "dir", nargs="?", default="data/pages",
        help="Output directory (default: data/pages)",
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
    elif args.command == "dump":
        cmd_dump(args)


if __name__ == "__main__":
    main()
