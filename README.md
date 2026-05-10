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
9. Classifies each change with AI (category, severity, summary) and stores structured events permanently
10. Accumulated change intelligence is queryable by category, severity, page, keyword, or date range

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
python claude_docs_monitor.py                                # fetch, diff, update local files
python claude_docs_monitor.py check --quiet                  # summary table only
python claude_docs_monitor.py check --poll 3600              # re-check every hour
python claude_docs_monitor.py check --save-diffs out/
python claude_docs_monitor.py check --dump ~/docs            # dump pages to custom dir instead of data-claude/pages/
python claude_docs_monitor.py check --report ~/reports       # write reports to custom dir
python claude_docs_monitor.py check --include-html           # include HTML-noise diffs (suppressed by default)
python claude_docs_monitor.py history                        # browse snapshot history
python claude_docs_monitor.py diff URL                       # diff last two snapshots of a page
python claude_docs_monitor.py urls                           # list all tracked URLs
python claude_docs_monitor.py rebuild-history                # regenerate history files from all stored snapshots
python claude_docs_monitor.py dump ~/review                  # export .md files from DB (no network)
python claude_docs_monitor.py digest                         # AI-analyze latest diffs into a change digest
python claude_docs_monitor.py digest --model opus            # use a different model
python claude_docs_monitor.py digest --gh-issue              # also create GitHub issues for breaking changes
python claude_docs_monitor.py query breaking                 # query all breaking changes
python claude_docs_monitor.py query --since 7d               # changes in the last 7 days
python claude_docs_monitor.py query "hooks" --severity high  # keyword search with severity filter
python claude_docs_monitor.py query --json | jq .            # machine-readable output
python claude_docs_monitor.py backfill                       # classify historical changes with AI
python claude_docs_monitor.py backfill --dry-run             # preview what would be classified
```

Running with no arguments defaults to `check`.

All output (snapshots, pages, reports, digest, history) lives under `data-claude/` in the working directory.

### Claude Code slash commands

The repo ships five project-level slash commands in `.claude/commands/`:

| Command | Purpose |
|---|---|
| `/check-docs` | Fetch all doc pages, diff against snapshot, update reports |
| `/digest` | Feed latest diffs to `claude -p` and write an actionable digest |
| `/query-docs` | Query the change intelligence database |
| `/ask-docs` | Answer questions by searching cached pages with grep + read |
| `/ask-docs-bare` | Identical to `/ask-docs`. Exists as a runner-target alias to bypass user-global skill shadowing in eval harnesses |

These are project-scoped — they activate automatically when you open this repo in Claude Code. The `/check-docs` skill calls `~/.claude/lib/claude_docs_monitor.py` against the project's working directory, so output lands in `data-claude/` where `/ask-docs` can read it.

**Install** (the script — skills are picked up from `.claude/commands/` automatically):

```bash
mkdir -p ~/.claude/lib
cp claude_docs_monitor.py ~/.claude/lib/
```

First run fetches everything and stores a baseline. No diffs are shown. Second run onward reports changes. When changes are detected, `/check-docs` automatically generates an AI digest and stores structured change events.

### Ask docs

`/ask-docs` answers questions about Claude Code by searching the locally cached documentation pages (in `data-claude/pages/`), citing sources and noting cache freshness:

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

Run `check` first to generate a report, then `digest` to analyze it. The digest writes `data-claude/digest.md` and `data-claude/digest.html`.

The `/check-docs` skill automatically runs the digest when changes are detected, so you don't need to invoke it separately during a normal check.

Requires the `claude` CLI to be installed and authenticated (Max OAuth via `~/.claude/.credentials.json`), or the Agent SDK installed, or `ANTHROPIC_API_KEY` set. The dispatcher in `llm_backend.py` resolves these in order: SDK → CLI → API.

### Change intelligence

Every `digest` run also classifies each change with AI and stores the result permanently in SQLite. Each change event gets a category (`feature`, `breaking`, `deprecation`, `clarification`, `flag_change`, `bugfix`), severity (`high`, `medium`, `low`), a one-line summary, details, action items, and keyword tags. This data accumulates over time and is queryable.

The `query` command searches the accumulated intelligence:

```
python claude_docs_monitor.py query breaking                        # all breaking changes ever
python claude_docs_monitor.py query --since 7d                      # everything in the last 7 days
python claude_docs_monitor.py query --severity high                 # all high-severity events
python claude_docs_monitor.py query "hooks"                         # keyword search across summaries, details, tags
python claude_docs_monitor.py query --page hooks.md                 # all events for a specific page
python claude_docs_monitor.py query --category feature --since 30d  # new features in last month
python claude_docs_monitor.py query --json | jq '.events[]'         # pipe to jq for processing
```

The `backfill` command populates the change intelligence database from existing snapshot history, so you don't lose the value of past runs:

```
python claude_docs_monitor.py backfill --dry-run   # preview what would be classified
python claude_docs_monitor.py backfill             # classify all historical changes
```

### GitHub issues for breaking changes

The `digest` command can automatically create GitHub issues for breaking changes:

```
python claude_docs_monitor.py digest --gh-issue
python claude_docs_monitor.py digest --gh-issue --gh-repo owner/repo
```

Each breaking change gets an issue with the summary, details, action items, and tags. Requires the `gh` CLI to be authenticated.

## MCP Server (optional)

An optional MCP server (`mcp_server.py`) exposes the documentation intelligence database as tools and resources to any MCP client (Claude Code, Cursor, custom agents).

The MCP server is **read-only** — it queries the SQLite database but never writes to it. You still need the CLI (or slash commands) to fetch docs (`check`), generate digests (`digest`), and classify changes (`backfill`). The typical workflow is:

1. **Populate data** via CLI: `python claude_docs_monitor.py check` then `digest`
2. **Query data** via MCP tools — or via CLI `query` command, slash commands, or direct SQL

The MCP server is purely additive. Everything works without it.

### Setup

```bash
pip install mcp                          # or: pip install -r requirements-mcp.txt
claude mcp add docs-monitor -- python /path/to/mcp_server.py
```

Or use the project-scoped `.mcp.json` (already included — works automatically when opening this project in Claude Code).

### Tools

| Tool | Description | Parameters |
|------|-------------|------------|
| `query_changes` | Search AI-classified change events | `keyword?`, `category?`, `severity?`, `page?`, `since?`, `until?`, `limit?` |
| `get_page_snapshots` | Snapshot history for a page or overview of all tracked URLs | `url?`, `limit?` |
| `get_diff` | Unified diff between the two most recent snapshots | `url` (required) |
| `search_pages` | Full-text search across latest cached doc pages | `keyword` (required), `limit?` |

### Resources

| URI | Returns |
|-----|---------|
| `docs://pages/{name}` | Latest cached content for a doc page (e.g. `docs://pages/hooks.md`) |
| `docs://digest` | Latest AI-generated change digest |
| `docs://report` | Latest check report (summary + diffs) |

### Configuration

The server reads the SQLite database at `data-claude/snapshots.db` (relative to the project working directory) by default, falling back to `~/.local/share/claude-docs-monitor/data-claude/snapshots.db` if the local one is absent. Override with the `DOCS_MONITOR_DB` environment variable.

## Reports

Every `check` run generates four report files in `data-claude/` (override with `--report DIR`):

- **`report.html`** / **`report.md`** — latest run only, overwritten each time
- **`history.html`** / **`history.md`** — cumulative log, appended each run with a separator between entries

Reports include a summary table (changed/added/removed/errors) and per-page unified diffs showing the exact text that was added, removed, or modified — the actual wording changes, not just a flag that something changed. The HTML versions are self-contained with inline CSS and syntax-highlighted diffs (green for additions, red for removals). First run produces a "pages snapshotted" baseline.

## What gets stored

```
data-claude/
  snapshots.db    # SQLite: full history of every fetch + change intelligence
  pages/          # latest .md files, updated every run
  report.html     # self-contained HTML report (latest run)
  report.md       # Markdown report (latest run)
  history.html    # cumulative HTML report (appended each run)
  history.md      # cumulative Markdown report (appended each run)
  digest.html     # AI-generated change digest (latest run)
  digest.md       # AI-generated change digest (latest run)
```

Three tables: `index_snapshots` (the llms.txt file itself), `page_snapshots` (one row per fetch per URL), and `change_events` (AI-classified change metadata). All append-only — every fetch and classification is stored permanently. The `change_events` table accumulates structured intelligence over time: category, severity, summary, details, action items, and keyword tags for each change. Query this data via the `query` command or directly in SQLite.

The `history.html` and `history.md` files grow over time, accumulating every run's summary and diffs into a single scrollable document. This gives you a complete, human-readable changelog of all documentation changes without needing to query the database.

## Project structure

```
claude_docs_monitor/
├── claude_docs_monitor.py         # main CLI: fetch, diff, classify, report
├── llm_backend.py                 # tiered SDK/CLI/API dispatcher
├── mcp_server.py                  # optional read-only MCP server
├── .claude/commands/              # project-level slash commands
│   ├── ask-docs.md
│   ├── ask-docs-bare.md
│   ├── check-docs.md
│   ├── digest.md
│   └── query-docs.md
├── .mcp.json                      # MCP server registration
├── data-claude/                   # output directory (created on first run)
│   ├── snapshots.db
│   ├── pages/
│   ├── eval/                      # benchmark harness for ask-docs evaluation
│   └── ...
├── investigation-archive/         # markdown notes from RAG-vs-bare experiments
├── requirements.txt
└── requirements-mcp.txt
```

## Design decisions

- **httpx async + HTTP/2**: connection multiplexing on a single host, all URLs in roughly 12 round trips.
- **SQLite**: zero-config, queryable, works everywhere. Better than a folder of timestamped files when you have 50+ pages and want to ask questions about history.
- **SHA-256 before diffing**: hash comparison is O(1). Only compute expensive diffs when something actually changed.
- **difflib.unified_diff**: standard library. Produces normal unified diffs that work with any tool that reads them.
- **Bare grep-and-read for `/ask-docs`**: a hybrid RAG stack (BM25 + dense + rerank) was tested against the bare grep approach on a 9-question hard subset. Both landed in the same 1–4/9 strict-pass band. The bare version ships with vastly less code, so the RAG layer was rolled back. See `investigation-archive/` for the experimental record.

## Limitations

- Some pages (notably the changelog) embed dynamic content like CSRF tokens and request IDs that cause false-positive diffs on every run. These diffs are suppressed by default — use `--include-html` to see them.
- The tool fetches rendered markdown from the docs site. If the site serves different content based on headers or cookies, you'll get whatever an unauthenticated `httpx` client gets.
- No notification system. Pipe it into whatever you already use.

## License

Do whatever you want with it.
