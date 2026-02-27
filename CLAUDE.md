# Claude Docs Monitor — AI Agent Reference

## Purpose

Single-file Python tool that monitors Claude Code documentation at `code.claude.com/docs/` for changes. Fetches all pages, stores snapshots in SQLite, computes unified diffs, generates HTML/Markdown reports, and optionally produces AI-powered change digests via `claude -p`.

## Architecture

### Single-File Design

Everything lives in `claude_docs_monitor.py` (~1450 lines). No package structure, no setup.py. One required dependency (`httpx[http2]`), one optional (`rich`).

### Layers (top to bottom)

```
CLI (build_parser, main)
  → Commands (cmd_check, cmd_digest, cmd_history, cmd_diff, cmd_urls, cmd_dump, cmd_rebuild_history)
    → Report Generation (generate_md_report, generate_html_report, append_*_history)
    → Display (print_summary, print_diffs — Rich or plain text)
    → HTTP (fetch_url, fetch_all — async httpx with semaphore + retry)
    → Database (init_db, store_*, get_* — SQLite append-only)
    → Utilities (sha256, normalize, compute_diff, parse_index, is_html_diff)
```

### Database Schema

Two tables in `data/snapshots.db`, both append-only:

**`index_snapshots`** — tracks the llms.txt index itself:
- `id` INTEGER PK, `fetched_at` TEXT, `content` TEXT, `hash` TEXT, `urls_json` TEXT

**`page_snapshots`** — one row per fetch per URL:
- `id` INTEGER PK, `url` TEXT, `fetched_at` TEXT, `content` TEXT, `hash` TEXT, `status_code` INTEGER, `duration_ms` REAL, `error` TEXT
- Indexes: `idx_page_url` (url), `idx_page_fetched` (fetched_at)

### Data Flow: `check` command

1. Fetch `INDEX_URL` (llms.txt) → parse URLs → store index snapshot
2. Compare URL set against previous index → detect added/removed pages
3. `fetch_all()`: async HTTP/2, 5 concurrent connections, 3 retries with exponential backoff
4. For each page: SHA-256 hash comparison against last snapshot → compute unified diff if changed
5. Filter HTML noise diffs (>50% HTML tags) unless `--include-html`
6. Store all snapshots → generate reports (md + html + history) → dump pages to disk

### Data Flow: `digest` command

1. Read `data/report.md` → check for changes (| Changed | 0 |)
2. Extract `## Diffs` section to minimize tokens
3. Pipe diffs via stdin to: `claude -p INSTRUCTION --model sonnet --max-turns 1 --output-format text`
4. Strip `CLAUDECODE` env var to allow nested invocation
5. Write `digest.md` and `digest.html`

### Key Design Decisions

- **Hash-before-diff**: SHA-256 comparison is O(1); only compute expensive diffs when content changed
- **Status code tracking**: 200→non-200 treated as a change even without content diff
- **HTML noise filter**: `is_html_diff()` counts HTML/JS patterns in changed lines; >50% threshold suppresses the diff
- **First-run detection**: If first URL has no prior snapshot, treat entire run as baseline (no "added" reports)
- **Index tracking**: Stores `urls_json` per run to detect when Anthropic adds/removes doc pages
- **Digest via CLI**: Uses `subprocess.run(["claude", "-p", ...])` not the SDK — works with Max OAuth automatically
- **History reconstruction**: `rebuild-history` walks index snapshots chronologically, uses time windows to group page fetches per run

## Commands Reference

| Command | Async | Key Flags |
|---------|-------|-----------|
| `check` (default) | Yes | `--quiet`, `--poll SEC`, `--save-diffs DIR`, `--dump DIR`, `--report DIR`, `--include-html` |
| `digest` | No | `--model ALIAS`, `--report DIR` |
| `history` | No | `[URL]` positional |
| `diff` | No | `URL` positional (required) |
| `urls` | No | (none) |
| `dump` | No | `[DIR]` positional (default: data/pages) |
| `rebuild-history` | No | `--report DIR`, `--include-html` |

## Output Files

All written to `data/` (override with `--report DIR`):

| File | Lifecycle | Content |
|------|-----------|---------|
| `snapshots.db` | Append-only, grows each run | Full history of every fetch |
| `pages/*.md` | Overwritten each run | Latest doc pages as markdown |
| `report.md` / `report.html` | Overwritten each run | Summary + diffs for latest run |
| `history.md` / `history.html` | Appended each run | Cumulative changelog |
| `digest.md` / `digest.html` | Overwritten each run | AI-generated change analysis |

## Skills (Claude Code Slash Commands)

Three skills in `.claude/commands/`:

### `/check-docs`
Runs the full monitor pipeline. Auto-runs `/digest` if changes detected. Copies all outputs from `~/.local/share/claude-docs-monitor/data/` to the project directory.

### `/digest`
Standalone AI digest. Reads latest `report.md`, analyzes diffs, writes digest files.

### `/ask-docs`
Q&A against cached doc pages. Uses Grep to search `data/pages/*.md`, reads top matches, synthesizes answer. No network calls.

## Two-Copy Installation Pattern

The script and skills live in two places:

| Location | Purpose |
|----------|---------|
| Repo: `claude_docs_monitor.py`, `.claude/commands/*.md` | Source of truth, version-controlled |
| System: `~/.claude/lib/claude_docs_monitor.py`, `~/.claude/commands/*.md` | Working copies used by skills |
| Data: `~/.local/share/claude-docs-monitor/data/` | Canonical working directory for script I/O |
| Project: `pages/`, `report.*`, `history.*`, `digest.*` | Mirror copied after each run for git tracking |

After modifying the script, sync both copies:
```bash
cp claude_docs_monitor.py ~/.claude/lib/claude_docs_monitor.py
```

## Integration Guide

### Installing into another project

Copy three skill files and the script:

```bash
# Skills (into user-global commands)
cp .claude/commands/check-docs.md ~/.claude/commands/
cp .claude/commands/digest.md ~/.claude/commands/
cp .claude/commands/ask-docs.md ~/.claude/commands/

# Script
mkdir -p ~/.claude/lib
cp claude_docs_monitor.py ~/.claude/lib/

# Data directory (auto-created on first run)
mkdir -p ~/.local/share/claude-docs-monitor
```

Then type `/check-docs` in any Claude Code session. First run creates the baseline. Second run onward reports changes.

### Programmatic usage (no skills)

```bash
# Run from any directory
cd ~/.local/share/claude-docs-monitor
python ~/.claude/lib/claude_docs_monitor.py check --quiet
python ~/.claude/lib/claude_docs_monitor.py digest
```

### Adapting for a different docs site

Modify these constants in the script:
- `INDEX_URL`: URL of the page listing all doc URLs (must contain markdown links)
- `BASE_URL`: Base URL for the docs site
- `parse_index()`: Adjust regex if the index format differs

### Querying the database directly

```sql
-- Pages that changed most often
SELECT url, COUNT(*) as changes FROM page_snapshots
GROUP BY url HAVING changes > 1 ORDER BY changes DESC;

-- All snapshots for a specific page
SELECT fetched_at, hash, status_code FROM page_snapshots
WHERE url = 'https://code.claude.com/docs/en/hooks.md' ORDER BY id DESC;

-- When was a page added to the index?
SELECT fetched_at, urls_json FROM index_snapshots ORDER BY id;
```

## Conventions

- All timestamps are ISO 8601 UTC
- Content normalized (CRLF/CR → LF) before hashing or diffing
- `sqlite3.Row` used throughout for dict-like access
- `getattr(args, "key", default)` for safe optional arg access
- `Path.mkdir(parents=True, exist_ok=True)` for all directory creation
- Rich/plain text: every display function checks `if HAS_RICH:` with else fallback
- Report data is a single dict passed to all output functions for consistency

## Dependencies

- **Required**: `httpx[http2]>=0.27,<1.0` (async HTTP/2 client)
- **Optional**: `rich` (colored output, progress bars, tables — gracefully skipped)
- **For digest**: `claude` CLI installed and authenticated (Max OAuth via `~/.claude/.credentials.json`)
