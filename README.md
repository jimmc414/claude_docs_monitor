# claude_docs_monitor

Tracks changes to Claude Code documentation across all pages at `code.claude.com/docs/`. Fetches every page, stores snapshots in SQLite, produces unified diffs when content changes, and maintains a local mirror of the markdown files.

## Why

Claude Code ships documentation updates without a changelog or RSS feed. If you're building on top of it or writing about it, you need to know what changed and when. This tool gives you that.

## How it works

1. Fetches the `llms.txt` index to discover all doc page URLs
2. Fetches all pages concurrently (async HTTP/2, 5 connections, polite backoff)
3. Compares SHA-256 hashes against the last stored snapshot
4. Computes unified diffs for anything that changed
5. Stores everything in SQLite (append-only, full history)
6. Updates a local folder of `.md` files
7. Generates HTML and Markdown reports (per-run snapshots + cumulative history)
8. Optionally feeds diffs to `claude -p` to produce an AI-generated change digest

The index itself is tracked too — if Anthropic adds or removes a doc page, that shows up in the report.

<img width="1065" height="706" alt="image" src="https://github.com/user-attachments/assets/32f56bd4-701c-48ca-acaa-6b1609c47402" />


<img width="974" height="53" alt="image" src="https://github.com/user-attachments/assets/5256c977-1fec-46f0-949e-4bbcd9cac0da" />

<img width="560" height="54" alt="image" src="https://github.com/user-attachments/assets/f5a255fe-2fb4-4da7-b52f-2e33c40dec2a" />

## Setup

```
pip install -r requirements.txt
```

One dependency: `httpx` with HTTP/2 support. `rich` is optional (colored output, progress bars).

## Usage

```
python claude_docs_monitor.py                      # fetch, diff, update local files
python claude_docs_monitor.py check --quiet        # summary table only
python claude_docs_monitor.py check --poll 3600    # re-check every hour
python claude_docs_monitor.py check --save-diffs out/
python claude_docs_monitor.py check --report ~/reports  # write reports to custom dir
python claude_docs_monitor.py check --include-html     # include HTML-noise diffs (suppressed by default)
python claude_docs_monitor.py history              # browse snapshot history
python claude_docs_monitor.py diff URL             # diff last two snapshots of a page
python claude_docs_monitor.py urls                 # list all tracked URLs
python claude_docs_monitor.py rebuild-history      # regenerate history files from all stored snapshots
python claude_docs_monitor.py dump ~/review        # export .md files from DB (no network)
python claude_docs_monitor.py digest              # AI-analyze latest diffs into a change digest
python claude_docs_monitor.py digest --model opus # use a different model
```

Running with no arguments defaults to `check`.

### Claude Code slash command

A standalone `/check-docs` slash command is included. It runs the monitor and summarizes the results directly in your Claude Code session — no need to clone the repo first.

**Install:**

```bash
cp .claude/commands/check-docs.md ~/.claude/commands/
cp .claude/commands/digest.md ~/.claude/commands/
cp claude_docs_monitor.py ~/.claude/lib/
```

The skills store data at `~/.local/share/claude-docs-monitor/` and auto-install `httpx` if needed. After installing, just type `/check-docs` in any Claude Code session. When changes are detected, it automatically generates an AI digest.

First run fetches everything and stores a baseline. No diffs are shown. Second run onward reports changes.

### Ask docs

An `/ask-docs` skill is also included. It answers questions about Claude Code by searching the locally cached documentation pages (stored in `data/pages/`), citing sources and noting cache freshness.

**Install:**

```bash
cp .claude/commands/ask-docs.md ~/.claude/commands/
```

Then ask questions directly in any Claude Code session from this project:

```
/ask-docs how do hooks work?
/ask-docs what are the sandboxing options?
/ask-docs how to configure MCP servers?
```

The skill greps the cached docs for relevant pages, reads the top matches, and synthesizes an answer — no network calls needed. Run `/check-docs` first to ensure the local cache is up to date.

### Digest

The `digest` subcommand feeds raw diffs to `claude -p` and generates an actionable intelligence briefing — executive summary, new features, breaking changes, deprecations, flag changes, and action items. It transforms 1400+ lines of unified diff into "here are the 5 things you need to know."

```
python claude_docs_monitor.py digest
python claude_docs_monitor.py digest --model opus
python claude_docs_monitor.py digest --report ~/reports
```

Run `check` first to generate a report, then `digest` to analyze it. The digest writes `data/digest.md` and `data/digest.html`.

A `/digest` slash command is also included. It runs the digest and presents the results directly in your Claude Code session.

**Install:**

```bash
cp .claude/commands/digest.md ~/.claude/commands/
```

The `/check-docs` skill automatically runs the digest when changes are detected, so you don't need to invoke it separately during a normal check.

Requires the `claude` CLI to be installed and authenticated.

## Reports

Every `check` run generates four report files in `data/` (override with `--report DIR`):

- **`report.html`** / **`report.md`** — latest run only, overwritten each time
- **`history.html`** / **`history.md`** — cumulative log, appended each run with a separator between entries

Reports include a summary table (changed/added/removed/errors) and per-page unified diffs showing the exact text that was added, removed, or modified — the actual wording changes, not just a flag that something changed. The HTML versions are self-contained with inline CSS and syntax-highlighted diffs (green for additions, red for removals). First run produces a "pages snapshotted" baseline.


## What gets stored

```
data/
  snapshots.db    # SQLite: full history of every fetch
  pages/          # latest .md files, updated every run
  report.html     # self-contained HTML report (latest run)
  report.md       # Markdown report (latest run)
  history.html    # cumulative HTML report (appended each run)
  history.md      # cumulative Markdown report (appended each run)
  digest.html     # AI-generated change digest (latest run)
  digest.md       # AI-generated change digest (latest run)
```

Two tables: `index_snapshots` (the llms.txt file itself) and `page_snapshots` (one row per fetch per URL). Append-only — every fetch is stored permanently, so you have a full history of every version of every page. You can query the database directly if you want something the CLI doesn't expose.

The `history.html` and `history.md` files grow over time, accumulating every run's summary and diffs into a single scrollable document. This gives you a complete, human-readable changelog of all documentation changes without needing to query the database.

## Design decisions

- **httpx async + HTTP/2**: Connection multiplexing on a single host. all URLs in roughly 12 round trips.
- **SQLite**: Zero-config, queryable, works everywhere. Better than a folder of timestamped files when you have 50+ pages and want to ask questions about history.
- **SHA-256 before diffing**: Hash comparison is O(1). Only compute expensive diffs when something actually changed.
- **difflib.unified_diff**: Standard library. Produces normal unified diffs that work with any tool that reads them.
- **Single file**: No package structure, no setup.py, no src/ directory. One file, one dependency, run it.

## Limitations

- Some pages (notably the changelog) embed dynamic content like CSRF tokens and request IDs that cause false-positive diffs on every run. These diffs are suppressed by default — use `--include-html` to see them.
- The tool fetches rendered markdown from the docs site. If the site serves different content based on headers or cookies, you'll get whatever an unauthenticated `httpx` client gets.
- No notification system. Pipe it into whatever you already use.

## License

Do whatever you want with it.
