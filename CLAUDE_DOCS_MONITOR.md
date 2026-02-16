# Claude Docs Monitor — Command Reference

## What This Is

Single-file Python tool that monitors all pages of Claude Code documentation at `code.claude.com/docs/` for changes. It fetches every page, stores snapshots in SQLite, computes unified diffs when content changes, and keeps a local folder of `.md` files updated.

## Setup

```bash
cd /path/to/claude_docs
pip install -r requirements.txt   # installs httpx[http2]
```

Required: Python 3.10+, `httpx`. Optional: `rich` (colored output, progress bars, tables).

## Files

| Path | Purpose |
|------|---------|
| `claude_docs_monitor.py` | All logic — run this directly |
| `requirements.txt` | `httpx[http2]>=0.27,<1.0` |
| `data/snapshots.db` | SQLite database (created on first run) |
| `data/pages/*.md` | Latest doc pages as local files (updated every run) |
| `data/report.html` | Self-contained HTML report (overwritten each run) |
| `data/report.md` | Markdown report (overwritten each run) |
| `data/history.html` | Cumulative HTML report (appended each run) |
| `data/history.md` | Cumulative Markdown report (appended each run) |

## Commands

### Default (no arguments) — runs `check`

```bash
python claude_docs_monitor.py
```

Fetches all pages, shows change summary + diffs, updates `data/pages/`.

### check

```bash
python claude_docs_monitor.py check [OPTIONS]
```

| Flag | Effect |
|------|--------|
| `--quiet` | Summary table only, suppress inline diffs |
| `--save-diffs DIR` | Write `.diff` files per changed page to DIR |
| `--dump DIR` | Override local page dump directory (default: `data/pages`) |
| `--report DIR` | Override report output directory (default: `data/`) |
| `--include-html` | Include diffs that are predominantly HTML/script noise (suppressed by default) |
| `--poll SEC` | Re-run every SEC seconds (e.g. `--poll 3600` for hourly) |

First run snapshots all pages as baseline (no diffs). Subsequent runs compare against previous snapshots.

### history

```bash
python claude_docs_monitor.py history              # all pages, last 50 entries
python claude_docs_monitor.py history URL           # one page only
```

Shows snapshot timestamps, HTTP status codes, and content hashes from the database.

### diff

```bash
python claude_docs_monitor.py diff URL
```

Shows unified diff between the two most recent snapshots of a specific URL. URL must be the full URL as tracked (e.g. `https://code.claude.com/docs/en/best-practices.md`).

### urls

```bash
python claude_docs_monitor.py urls
```

Lists all tracked URLs with last fetch time, HTTP status, and content hash.

### dump

```bash
python claude_docs_monitor.py dump                  # to data/pages/
python claude_docs_monitor.py dump /some/other/dir  # custom directory
```

Exports latest snapshots from SQLite as `.md` files. No network calls — reads from database only.

### rebuild-history

```bash
python claude_docs_monitor.py rebuild-history                  # default output to data/
python claude_docs_monitor.py rebuild-history --report ~/out   # custom directory
python claude_docs_monitor.py rebuild-history --include-html   # include HTML noise diffs
```

Regenerates `history.html` and `history.md` from all stored snapshots in the database. Walks through every run chronologically, reconstructs diffs between consecutive snapshots, and writes a complete cumulative history. Useful if history files were deleted or to backfill after upgrading.

## Common Workflows

**Daily check (typical use):**
```bash
python claude_docs_monitor.py
```

**Quick summary without diff noise:**
```bash
python claude_docs_monitor.py check --quiet
```

**Save diffs for later review:**
```bash
python claude_docs_monitor.py check --save-diffs data/diffs
```

**Continuous monitoring:**
```bash
python claude_docs_monitor.py check --poll 21600   # every 6 hours
```

**Review a specific page's recent change:**
```bash
python claude_docs_monitor.py diff https://code.claude.com/docs/en/hooks.md
```

**Read local docs without network:**
```bash
python claude_docs_monitor.py dump ~/claude-docs-review
# then read files in ~/claude-docs-review/
```

## Output Behavior

- **First run:** "First run: N pages snapshotted." No diffs generated.
- **Subsequent runs:** Summary table (changed/added/removed/errors) + unified diffs for changed pages, showing the exact text that was added, removed, or modified line by line.
- **Every run** updates `data/pages/` with latest `.md` files regardless of changes.
- **Every run** generates `report.html` and `report.md` (latest run only, overwritten) plus `history.html` and `history.md` (cumulative, appended). HTML reports are self-contained with inline CSS and syntax-highlighted diffs.

## Data Model

SQLite at `data/snapshots.db` with two tables:

- `index_snapshots` — tracks `llms.txt` itself (detects added/removed doc pages)
- `page_snapshots` — one row per fetch per URL (append-only history)

## Error Handling

- Network failures: 3 retries with exponential backoff (1s, 2s, 4s)
- Index fetch failure: falls back to last cached URL list
- HTTP errors: stored and reported but don't abort the run
