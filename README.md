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

### LLM backend (for `digest` and `backfill`)

The `digest` and `backfill` commands call Claude. They route through a tiered backend dispatcher and pick the first available of:

| Backend | When it's used | Install |
|---------|----------------|---------|
| `sdk`   | Preferred — lighter and faster than CLI | `pip install -r requirements-sdk.txt` |
| `cli`   | Fallback — works without optional deps | install [Claude Code](https://docs.anthropic.com/en/docs/claude-code) |
| `api`   | Opt-in only — activates when `ANTHROPIC_API_KEY` is set | `pip install -r requirements-api.txt` and `export ANTHROPIC_API_KEY=…` |

Without `ANTHROPIC_API_KEY`, the `api` tier is never chosen — no API spend can occur. Both `sdk` and `cli` authenticate via Max OAuth (`~/.claude/.credentials.json`). The dispatcher strips `ANTHROPIC_API_KEY` from the environment before invoking `sdk` or `cli` so OAuth is honored even if the key happens to be set.

Force a backend explicitly:
```
python claude_docs_monitor.py digest --backend sdk
python claude_docs_monitor.py digest --backend cli
python claude_docs_monitor.py digest --backend api
```

`--verbose` (or `DOCS_MONITOR_VERBOSE=1`) prints which backend is in use:
```
[llm_backend] backend resolved: sdk
[llm_backend] call: backend=sdk model=sonnet schema=no
```

## Usage

```
python claude_docs_monitor.py                      # fetch, diff, update local files
python claude_docs_monitor.py check --quiet        # summary table only
python claude_docs_monitor.py check --poll 3600    # re-check every hour
python claude_docs_monitor.py check --save-diffs out/
python claude_docs_monitor.py check --dump ~/docs         # dump pages to custom dir instead of data/pages/
python claude_docs_monitor.py check --report ~/reports    # write reports to custom dir
python claude_docs_monitor.py check --include-html       # include HTML-noise diffs (suppressed by default)
python claude_docs_monitor.py history              # browse snapshot history
python claude_docs_monitor.py diff URL             # diff last two snapshots of a page
python claude_docs_monitor.py urls                 # list all tracked URLs
python claude_docs_monitor.py rebuild-history      # regenerate history files from all stored snapshots
python claude_docs_monitor.py dump ~/review        # export .md files from DB (no network)
python claude_docs_monitor.py digest              # AI-analyze latest diffs into a change digest
python claude_docs_monitor.py digest --model opus # use a different model
python claude_docs_monitor.py digest --gh-issue   # also create GitHub issues for breaking changes
python claude_docs_monitor.py query breaking       # query all breaking changes
python claude_docs_monitor.py query --since 7d     # changes in the last 7 days
python claude_docs_monitor.py query "hooks" --severity high  # keyword search with severity filter
python claude_docs_monitor.py query --json | jq .  # machine-readable output
python claude_docs_monitor.py backfill             # classify historical changes with AI
python claude_docs_monitor.py backfill --dry-run   # preview what would be classified
```

Running with no arguments defaults to `check`.

## Codex Variant

A parallel OpenAI Codex monitor is included as `codex_docs_monitor.py`.

- Source index: `https://developers.openai.com/codex/llms.txt`
- Default data directory: `data-codex/` (separate from Claude artifacts)
- Command surface: mirrors the existing CLI (`check`, `digest`, `query`, `backfill`, etc.)
- Local page filenames are path-preserving (e.g. `app__commands.md`, `ide__commands.md`)

Quick start:

```bash
python codex_docs_monitor.py check
python codex_docs_monitor.py digest
python codex_docs_monitor.py query --since 7d
```

AI behavior in the Codex variant:

- Uses OpenAI Responses API with OAuth token from `~/.codex/auth.json`
- Falls back to `codex exec` automatically if direct API auth/call fails

See `CODEX_DOCS_MONITOR.md` for full command reference.

## Cross-Tool Full-Corpus Comparison

A full documentation-set comparator is included as `compare_docs_features.py`.
It evaluates all cached pages for Claude, Gemini, and Codex (not just recent diffs), then scores and ranks the three tools using a fixed 100-point rubric.

```bash
python compare_docs_features.py
python compare_docs_features.py --strict-rubric
python compare_docs_features.py --output-dir data-analysis/compare-docs
```

Default outputs:

- `data-analysis/compare-docs/report.md` (detailed analysis report)
- `data-analysis/compare-docs/report.json` (structured feature/score matrix)
- `data-analysis/compare-docs/latest_scores.csv` (quick rank export)

Rubric definition and scoring rules are versioned in `DOCS_COMPARISON_RUBRIC.md`.

### Codex skill: compare docs

A project-local Codex skill is included at `.codex/skills/compare-docs/`.
Use it in Codex as:

```text
$compare-docs
```

The skill runs the full-corpus analyzer and returns an executive ranking summary, while writing the detailed artifacts to `data-analysis/compare-docs/`.

### Claude Code slash command

A standalone `/check-docs` slash command is included. It runs the monitor and summarizes the results directly in your Claude Code session — no need to clone the repo first.

**Install:**

```bash
cp .claude/commands/check-docs.md ~/.claude/commands/
cp .claude/commands/digest.md ~/.claude/commands/
cp .claude/commands/query-docs.md ~/.claude/commands/
cp claude_docs_monitor.py ~/.claude/lib/
```

The skills store data at `~/.local/share/claude-docs-monitor/` and auto-install `httpx` if needed. After installing, just type `/check-docs` in any Claude Code session. When changes are detected, it automatically generates an AI digest and stores structured change events.

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

### Change intelligence

Every `digest` run now also classifies each change with AI and stores the result permanently in SQLite. Each change event gets a category (`feature`, `breaking`, `deprecation`, `clarification`, `flag_change`, `bugfix`), severity (`high`, `medium`, `low`), a one-line summary, details, action items, and keyword tags. This data accumulates over time and is queryable.

The `query` command searches the accumulated intelligence:

```
python claude_docs_monitor.py query breaking                     # all breaking changes ever
python claude_docs_monitor.py query --since 7d                   # everything in the last 7 days
python claude_docs_monitor.py query --severity high              # all high-severity events
python claude_docs_monitor.py query "hooks"                      # keyword search across summaries, details, tags
python claude_docs_monitor.py query --page hooks.md              # all events for a specific page
python claude_docs_monitor.py query --category feature --since 30d  # new features in last month
python claude_docs_monitor.py query --json | jq '.events[]'     # pipe to jq for processing
```

A `/query-docs` slash command is included. It runs the query and presents results directly in your Claude Code session.

**Install:**

```bash
cp .claude/commands/query-docs.md ~/.claude/commands/
```

The `backfill` command populates the change intelligence database from existing snapshot history, so you don't lose the value of past runs:

```
python claude_docs_monitor.py backfill --dry-run   # preview what would be classified
python claude_docs_monitor.py backfill             # classify all historical changes
```

### Hybrid retrieval and agentic reports (RAG layer)

`claude_docs_monitor` ships with an optional retrieval layer that turns the cached docs and change history into a queryable knowledge base. Three new commands:

```bash
python claude_docs_monitor.py reindex                            # build chunk + embedding index
python claude_docs_monitor.py search "how do I block dangerous tools"   # hybrid BM25+dense semantic search
python claude_docs_monitor.py report  "what changed about hooks last month"  # agentic RAG report
```

Architecture (M1-M5):
- **M1: `embedding_cache.py`** — persistent SQLite cache of embeddings, keyed by `(content_hash, model)`. Hash-keyed so re-running reindex is a no-op when content hasn't changed; survives DB drops.
- **M2: `doc_index.py`** — chunks pages at H1/H2/H3 boundaries (with code-fence awareness), one whole-page chunk plus per-section chunks, FTS5 mirror for BM25, optional LLM-generated 1-3 sentence summaries embedded separately for "answer-language" matching.
- **M3: `retriever.py`** — runs BM25 (FTS5), dense cosine on raw vectors, dense cosine on summary vectors, fuses with Reciprocal Rank Fusion (k=60), and optionally reranks with Claude.
- **M4: `report_builder.py`** — agentic loop using the Claude Agent SDK: PLAN → RETRIEVE → REASON & GAP-FILL (with in-process MCP tools) → SYNTHESIZE → SELF-CRITIQUE.
- **M5: surfaces** — three new CLI subcommands, six new MCP tools (`hybrid_search`, `change_search`, `find_similar`, `get_chunk`, `build_report`, `list_reports`, `get_saved_report`), and a new `/report` skill. `/ask-docs` and `/query-docs` upgrade to use hybrid search when MCP is available, with grep fallback.

#### Setup

```bash
pip install -r requirements-rag.txt          # numpy
ollama pull nomic-embed-text                 # local, free, default-friendly
# OR install voyageai: pip install voyageai && export VOYAGE_API_KEY=...
# OR install openai:   pip install openai && export OPENAI_API_KEY=...
```

#### Embedding providers

| Provider | Model (default) | Dims | Cost / 1M tokens | When |
|---|---|---|---|---|
| `voyage` | `voyage-3` | 1024 | $0.06 | Default; Anthropic-aligned |
| `voyage` | `voyage-3-large` | 2048 | $0.18 | Highest quality |
| `openai` | `text-embedding-3-large` | 3072 | $0.13 | Familiar baseline |
| `ollama` | `nomic-embed-text` | 768 | free | Local, no network |

Pick the provider via `--provider`, the env var `DOCS_MONITOR_EMBED_PROVIDER`, or the config file at `~/.config/claude_docs_monitor/embedding.json`.

#### Workflow

```bash
# One-time: build the index (auto-incremental on subsequent /check-docs runs)
python claude_docs_monitor.py reindex --provider ollama --skip-summaries

# Search — hybrid by default, with optional rerank
python claude_docs_monitor.py search "how do I prevent dangerous tool use"
python claude_docs_monitor.py search "PreToolUse" --source page --no-rerank
python claude_docs_monitor.py search "execution order" --source change_event --since 30d

# Report — agentic RAG with inline citations
python claude_docs_monitor.py report  "what changed about hooks in the last 30 days"
python claude_docs_monitor.py report  "compare subagents and skills" --scope docs
```

After the first `reindex`, every subsequent `check` run automatically reindexes only the changed pages. Pass `--no-reindex` to skip.

#### Cost

- Initial embed of corpus (~125 pages × ~5 chunks × 2 representations × ~500 tokens): ~625K tokens
  - Voyage-3: **~$0.04**
  - OpenAI 3-large: **~$0.08**
  - Ollama: **free**
- Initial summary generation (~625 chunks via Sonnet): **<$1** (free via Max OAuth + SDK)
- Per `/check-docs` incremental update: **<$0.005** (Voyage); free on Ollama
- Per `/report` invocation: **$0.50–$3.00** API equivalent depending on depth (effectively free via Max OAuth + SDK on Max 20x)
- Per `/ask-docs` query: **<$0.001** + Claude rerank tokens

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

Read-only metadata lookups (always available):

| Tool | Description | Parameters |
|------|-------------|------------|
| `query_changes` | Exact-filter search of AI-classified change events | `keyword?`, `category?`, `severity?`, `page?`, `since?`, `until?`, `limit?` |
| `get_page_snapshots` | Snapshot history for a page or overview of all tracked URLs | `url?`, `limit?` |
| `get_diff` | Unified diff between the two most recent snapshots | `url` (required) |
| `search_pages` | LIKE-based full-text search of latest cached pages (kept for backward compat) | `keyword`, `limit?` |

Hybrid retrieval and agentic-report tools (require `reindex` to have built `data-claude/index.db`):

| Tool | Description | Parameters |
|------|-------------|------------|
| `hybrid_search` | BM25 ⊕ dense ⊕ rerank semantic search across pages and change events | `query`, `source_type?`, `category?`, `severity?`, `page?`, `since?`, `until?`, `k?`, `rerank?` |
| `change_search` | Same as hybrid_search but locked to `source_type='change_event'` | `query`, `since?`, `until?`, `category?`, `severity?`, `page?`, `k?` |
| `find_similar` | Find chunks most similar to a given chunk_id (cosine) | `chunk_id`, `k?` |
| `get_chunk` | Fetch a chunk's full content and metadata | `chunk_id` |
| `build_report` | Run the agentic RAG report builder | `question`, `scope?`, `since?`, `until?`, `model?`, `max_turns?` |
| `list_reports` | List previously generated reports | (none) |
| `get_saved_report` | Read a previously generated report by slug | `slug` |

### Resources

| URI | Returns |
|-----|---------|
| `docs://pages/{name}` | Latest cached content for a doc page (e.g. `docs://pages/hooks.md`) |
| `docs://digest` | Latest AI-generated change digest |
| `docs://report` | Latest check report (summary + diffs) |

### Example queries (in an MCP client)

Once configured, you can ask your MCP client things like:

- "Use query_changes to find all breaking changes"
- "Use search_pages to find mentions of permissions"
- "Use get_diff to show the latest diff for hooks.md"
- "Read the docs://digest resource to see the latest change analysis"

### Configuration

The server reads the SQLite database at `~/.local/share/claude-docs-monitor/data/snapshots.db` by default. Override with the `DOCS_MONITOR_DB` environment variable.

## Reports

Every `check` run generates four report files in `data/` (override with `--report DIR`):

- **`report.html`** / **`report.md`** — latest run only, overwritten each time
- **`history.html`** / **`history.md`** — cumulative log, appended each run with a separator between entries

Reports include a summary table (changed/added/removed/errors) and per-page unified diffs showing the exact text that was added, removed, or modified — the actual wording changes, not just a flag that something changed. The HTML versions are self-contained with inline CSS and syntax-highlighted diffs (green for additions, red for removals). First run produces a "pages snapshotted" baseline.


## What gets stored

```
data/
  snapshots.db    # SQLite: full history of every fetch + change intelligence
  pages/          # latest .md files, updated every run
  report.html     # self-contained HTML report (latest run)
  report.md       # Markdown report (latest run)
  history.html    # cumulative HTML report (appended each run)
  history.md      # cumulative Markdown report (appended each run)
  digest.html     # AI-generated change digest (latest run)
  digest.md       # AI-generated change digest (latest run)
```

Three tables: `index_snapshots` (the llms.txt file itself), `page_snapshots` (one row per fetch per URL), and `change_events` (AI-classified change metadata). All append-only — every fetch and classification is stored permanently. The `change_events` table accumulates structured intelligence over time: category, severity, summary, details, action items, and keyword tags for each change. You can query this data via the `query` command or directly in SQLite.

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
