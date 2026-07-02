# Claude Docs Monitor — AI Agent Reference

## Purpose

Single-file Python tool that monitors Claude Code documentation at `code.claude.com/docs/` for changes. Fetches all pages, stores snapshots in SQLite, computes unified diffs, generates HTML/Markdown reports, produces AI-powered change digests via `claude -p`, and maintains a persistent change intelligence database with structured AI classifications queryable by category, severity, page, keyword, and date range.

## Architecture

### Single-File Design

Everything lives in `claude_docs_monitor.py` (~3500 lines, including a ~1100-line inline `_DASHBOARD_TEMPLATE` HTML/CSS/JS string). No package structure, no setup.py. One required dependency (`httpx[http2]`), three optional (`rich`, `mcp`, `PyYAML`). An optional `mcp_server.py` (~220 lines) provides read-only MCP access to the database.

### Layers (top to bottom)

```
CLI (build_parser, main)
  → Commands (cmd_check, cmd_digest, cmd_history, cmd_diff, cmd_urls, cmd_dump, cmd_rebuild_history, cmd_query, cmd_backfill)
    → Change Intelligence (_run_structured_classification, _create_gh_issues)
    → Report Generation (generate_md_report, generate_html_report, append_*_history)
    → Display (print_summary, print_diffs — Rich or plain text)
    → HTTP (fetch_url, fetch_all — async httpx with semaphore + retry)
    → Database (init_db, store_*, get_*, query_change_events — SQLite append-only)
    → Utilities (sha256, normalize, compute_diff, parse_index, is_html_diff, _parse_relative_date)

MCP Server (mcp_server.py — optional, read-only)
  → Tools (query_changes, get_page_snapshots, get_diff, search_pages)
  → Resources (docs://pages/{name}, docs://digest, docs://report)
  → Imports from claude_docs_monitor (init_db, query_change_events, get_page_history, etc.)
```

### Database Schema

Three tables in `data-claude/snapshots.db`:

**`index_snapshots`** — tracks the llms.txt index itself (append-only):
- `id` INTEGER PK, `fetched_at` TEXT, `content` TEXT, `hash` TEXT, `urls_json` TEXT

**`page_snapshots`** — one row per fetch per URL (append-only):
- `id` INTEGER PK, `url` TEXT, `fetched_at` TEXT, `content` TEXT, `hash` TEXT, `status_code` INTEGER, `duration_ms` REAL, `error` TEXT
- Indexes: `idx_page_url` (url), `idx_page_fetched` (fetched_at)

**`change_events`** — AI-classified change metadata (append-only):
- `id` INTEGER PK, `run_timestamp` TEXT, `url` TEXT, `page_name` TEXT, `event_type` TEXT, `category` TEXT, `severity` TEXT, `summary` TEXT, `details` TEXT, `action_required` TEXT, `tags_json` TEXT, `diff_text` TEXT, `gh_issue_url` TEXT, `created_at` TEXT
- Indexes: `idx_ce_run` (run_timestamp), `idx_ce_url` (url), `idx_ce_category` (category), `idx_ce_severity` (severity)
- Categories: feature, breaking, deprecation, clarification, flag_change, bugfix
- Severity levels: high, medium, low

### Data Flow: `check` command

1. Fetch `INDEX_URL` (llms.txt) → parse URLs → store index snapshot
2. Compare URL set against previous index → detect added/removed pages
3. `fetch_all()`: async HTTP/2, 5 concurrent connections, 3 retries with exponential backoff
4. For each page: SHA-256 hash comparison against last snapshot → compute unified diff if changed
5. Filter HTML noise diffs (>50% HTML tags) unless `--include-html`
6. Store all snapshots → generate reports (md + html + history) → dump pages to disk

### Data Flow: `digest` command

1. Read `data-claude/report.md` → check for changes (| Changed | 0 |)
2. Extract `## Diffs` section to minimize tokens
3. Resolve output mode via `_resolve_output()` (CLI > env > `config.yaml` > `"both"`)
4. **Phase 1 — Structured classification** (always runs): Diffs are split into chunks bounded by `_MAX_DIFFS_PER_CHUNK` (10) and `_MAX_BYTES_PER_CHUNK` (~60 KB) and classified **serially** with `claude -p --output-format json --json-schema`. A failing chunk logs a warning and the run continues; surviving events are merged and stored in `change_events` (skips if already classified for this run; the dashboard and `--gh-issue` step both depend on these events). Empty-URL events are dropped at the insert path.
5. **Phase 2a — Narrative digest** (when `output ∈ {digest, both}`): Reads back the classified events for this run via `_build_narrative_input_from_events()` and pipes that compact per-event metadata (not raw diffs) to `claude -p --output-format text` → write `digest.md` and `digest.html`. **Variant B fallback:** if classification stored zero events, runs map-reduce on raw diff chunks (mini-digest per chunk, then a reduce call) so the user always gets a digest when changes were detected.
6. **Phase 2b — Dashboard** (when `output ∈ {dashboard, both}`): Build payload from `change_events` (joined with `page_snapshots` for diff excerpts) and render `dashboard.html` from the inline `_DASHBOARD_TEMPLATE`
7. **Browser launch** (unless `--no-open` or `auto_open: false`): open each generated HTML in `files_to_open` order with a 150ms gap between
8. **Phase 3 — GitHub issues** (optional, `--gh-issue`): Create issues via `gh` CLI for breaking changes
9. Strip `CLAUDECODE` env var to allow nested invocation

### Key Design Decisions

- **Hash-before-diff**: SHA-256 comparison is O(1); only compute expensive diffs when content changed
- **Status code tracking**: 200→non-200 treated as a change even without content diff
- **HTML noise filter**: `is_html_diff()` counts HTML/JS patterns in changed lines; >50% threshold suppresses the diff
- **First-run detection**: If first URL has no prior snapshot, treat entire run as baseline (no "added" reports)
- **Index tracking**: Stores `urls_json` per run to detect when Anthropic adds/removes doc pages
- **Digest via CLI**: Uses `subprocess.run(["claude", "-p", ...])` not the SDK — works with Max OAuth automatically
- **History reconstruction**: `rebuild-history` walks index snapshots chronologically, uses time windows to group page fetches per run
- **Structured classification via JSON schema**: Uses `claude -p --output-format json --json-schema` for deterministic structured output; graceful fallback if classification fails (text digest still runs)
- **Duplicate guard**: Checks `run_timestamp` before classifying to prevent duplicate events on re-runs
- **Backfill**: Reconstructs historical diffs from snapshot pairs and classifies them retroactively, so the change intelligence database covers the full history

## Commands Reference

| Command | Async | Key Flags |
|---------|-------|-----------|
| `check` (default) | Yes | `--quiet`, `--poll SEC`, `--save-diffs DIR`, `--dump DIR`, `--report DIR`, `--include-html` |
| `digest` | No | `--model ALIAS`, `--report DIR`, `--output {digest,dashboard,both}`, `--no-open`, `--gh-issue`, `--gh-repo OWNER/REPO` |
| `query` | No | `[KEYWORD]`, `--category`, `--severity`, `--page`, `--since`, `--until`, `--limit`, `--json` |
| `backfill` | No | `--model ALIAS`, `--dry-run`, `--include-html` |
| `history` | No | `[URL]` positional |
| `diff` | No | `URL` positional (required) |
| `urls` | No | (none) |
| `dump` | No | `[DIR]` positional (default: data-claude/pages) |
| `rebuild-history` | No | `--report DIR`, `--include-html` |

## MCP Server (mcp_server.py)

Optional read-only MCP server. Requires `mcp>=1.0` (`pip install -r requirements-mcp.txt`).

The MCP server **only reads** the database — it cannot fetch docs, generate digests, or classify changes. Those operations require the CLI (`check`, `digest`, `backfill`) or slash commands (`/check-docs`, `/digest`). The MCP server provides a query interface for data that already exists in the database.

### Tools

| Tool | Wraps | Parameters |
|------|-------|------------|
| `query_changes` | `query_change_events()` | `keyword?`, `category?`, `severity?`, `page?`, `since?`, `until?`, `limit?` |
| `get_page_snapshots` | `get_page_history()` / `get_all_tracked_urls()` | `url?`, `limit?` |
| `get_diff` | `get_two_snapshots()` + `compute_diff()` | `url` (required) |
| `search_pages` | SQL LIKE on latest page content | `keyword` (required), `limit?` |

### Resources

| URI | Returns |
|-----|---------|
| `docs://pages/{name}` | Latest cached page content (e.g. `docs://pages/hooks.md`) |
| `docs://digest` | Contents of `data-claude/digest.md` |
| `docs://report` | Contents of `data-claude/report.md` |

### Configuration

Project-scoped `.mcp.json` auto-registers the server. DB path: `DOCS_MONITOR_DB` env var → `~/.local/share/claude-docs-monitor/data-claude/snapshots.db` → `./data-claude/snapshots.db`.

## Output Files

All written to `data-claude/` (override with `--report DIR`):

| File | Lifecycle | Content |
|------|-----------|---------|
| `snapshots.db` | Append-only, grows each run | Full history of every fetch |
| `pages/*.md` | Overwritten each run | Latest doc pages as markdown |
| `report.md` / `report.html` | Overwritten each run | Summary + diffs for latest run |
| `history.md` / `history.html` | Appended each run | Cumulative changelog |
| `digest.md` / `digest.html` | Overwritten each digest run (output ∈ {digest, both}) | AI-generated change analysis |
| `dashboard.html` | Overwritten each digest run (output ∈ {dashboard, both}) | Interactive single-file event browser, embeds full `change_events` history |
| `impact.md` | Overwritten each `/impact` run | Setup impact report: recent change events scored against the user's local Claude config, plus a config-vs-docs audit |

## Configuration

`digest` reads optional configuration from `data-claude/config.yaml`. Two
keys are honored in v1:

```yaml
# data-claude/config.yaml
output: both        # digest | dashboard | both — which artifact(s) to produce
auto_open: true     # false to suppress browser launches even without --no-open
```

Precedence for `output`: `--output` CLI flag → `DOCS_MONITOR_OUTPUT` env var →
`config.yaml` → built-in default `both`. Invalid values fall through to the
next layer with a printed warning.

`PyYAML` is optional. If absent, a built-in flat `key: value` parser handles
the subset above. A committed `data-claude/config.yaml.example` documents the
schema; the real `config.yaml` is gitignored so each user picks their own.

When `output=both`, `digest.html` and `dashboard.html` both auto-open in the
browser (digest first, dashboard ~150ms later). `--no-open` and
`auto_open: false` suppress every browser launch.

## Skills (Claude Code Slash Commands)

Five skills in `.claude/commands/`:

### `/check-docs`
Runs the full monitor pipeline from the project directory. The script writes natively to `data-claude/`, so there is no copy step. Auto-runs `/digest` if changes detected.

### `/digest`
Standalone AI digest. Reads latest `report.md`, analyzes diffs, writes digest files. Now also stores structured change events in SQLite.

### `/ask-docs`
Q&A against cached doc pages. Uses Grep to search `data-claude/pages/*.md`, reads top matches, synthesizes answer. No network calls.

### `/query-docs`
Query the change intelligence database. Searches accumulated change events by category, severity, page, keyword, or date range.

### `/impact`
Personal impact analysis, callable independently of the monitor pipeline. Builds a profile of the user's actual Claude environment (`~/.claude/settings.json`, rules, lib scripts, plugins, MCP config), then (a) scores recent `change_events` against that profile (direct / likely / none, with citations) and (b) audits the profile's checkable elements — env vars, settings keys, model IDs, `claude` CLI flags used by scripts — against the cached pages for deprecations, conflicts, and unused adjacent capabilities. Pure skill: the session does the reasoning with Grep/Read; no script changes, no DB writes. Writes `data-claude/impact.md`. Optional window argument (`7d`, `30d`, `90d`, `all`; default `30d`).

## Two-Copy Installation Pattern

The script and skills live in two places:

| Location | Purpose |
|----------|---------|
| Repo: `claude_docs_monitor.py`, `.claude/commands/*.md` | Source of truth, version-controlled |
| System: `~/.claude/lib/claude_docs_monitor.py`, `~/.claude/commands/*.md` | Working copies used by skills |
| Data: `~/.local/share/claude-docs-monitor/data-claude/` | Canonical working directory for script I/O |
| Project: `pages/`, `report.*`, `history.*`, `digest.*` | Mirror copied after each run for git tracking |

After modifying the script, sync both copies:
```bash
cp claude_docs_monitor.py ~/.claude/lib/claude_docs_monitor.py
cp .claude/commands/query-docs.md ~/.claude/commands/query-docs.md
```

## Integration Guide

### Installing into another project

Copy five skill files and the script:

```bash
# Skills (into user-global commands)
cp .claude/commands/check-docs.md ~/.claude/commands/
cp .claude/commands/digest.md ~/.claude/commands/
cp .claude/commands/ask-docs.md ~/.claude/commands/
cp .claude/commands/query-docs.md ~/.claude/commands/
cp .claude/commands/impact.md ~/.claude/commands/

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
python ~/.claude/lib/claude_docs_monitor.py query breaking
python ~/.claude/lib/claude_docs_monitor.py query --since 7d --json
python ~/.claude/lib/claude_docs_monitor.py backfill --dry-run
```

### MCP server (alternative to slash commands for querying)

Instead of using `/query-docs` or `/ask-docs` slash commands, you can configure the MCP server for native tool access:

```bash
pip install mcp
claude mcp add docs-monitor -- python /path/to/mcp_server.py
```

Or open the project directory in Claude Code — the `.mcp.json` auto-registers it. The MCP server provides the same query capabilities as the CLI `query`, `history`, `diff`, and `dump` commands but as MCP tools/resources. Write operations (`check`, `digest`, `backfill`) still require the CLI.

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

-- Change events by category
SELECT category, COUNT(*) FROM change_events GROUP BY category;

-- All breaking changes
SELECT run_timestamp, page_name, summary FROM change_events WHERE category = 'breaking';

-- High-severity events in last 30 days
SELECT * FROM change_events WHERE severity = 'high'
AND run_timestamp >= datetime('now', '-30 days');
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
- **Optional**: `mcp>=1.0` (MCP server — see `requirements-mcp.txt`)
- **Optional**: `PyYAML` (richer parsing of `data-claude/config.yaml`; a built-in flat-key parser is used otherwise)
- **For digest**: `claude` CLI installed and authenticated (Max OAuth via `~/.claude/.credentials.json`)
