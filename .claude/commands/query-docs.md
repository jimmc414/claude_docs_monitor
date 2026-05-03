---
description: Query the change intelligence database (semantic + filters) for documentation changes
allowed-tools: Bash, Read, mcp__docs-monitor__change_search, mcp__docs-monitor__query_changes
argument-hint: [question or keyword] [--category CAT] [--since DATE] [--severity SEV]
---

# Query Documentation Changes

Search the accumulated change intelligence database for Claude Code documentation changes.

**User input:** $ARGUMENTS

## Instructions

### Choosing between semantic search and exact filters

- **Natural-language question or keyword** ("what changed about hooks?", "permission updates", "new MCP features") — use **semantic search** via `mcp__docs-monitor__change_search`. It combines BM25, dense semantic search, and LLM rerank, then filters by metadata.
- **Exact filter only** (no keyword, just "all breaking changes" or "everything in last 7 days") — use the **CLI** for the most precise match: `python ~/.claude/lib/claude_docs_monitor.py query $ARGUMENTS`.

### Step 1: Detect intent

Look at `$ARGUMENTS`:
- If it starts with a flag (e.g. `--category breaking`, `--since 7d`) and there's no keyword text → use the CLI path (Step 2a).
- If it contains a keyword or natural-language phrase → use MCP semantic path (Step 2b).
- If MCP tools are unavailable → use the CLI path regardless.

### Step 2a: CLI path (exact filters)

```bash
cd ~/.local/share/claude-docs-monitor && python ~/.claude/lib/claude_docs_monitor.py query $ARGUMENTS
```

Read the output and present a concise summary.

### Step 2b: MCP semantic search

Parse the user's input into:
- A `query` string (the keyword or question).
- Optional filters: `category`, `severity`, `page`, `since`, `until`.

Call:

```
mcp__docs-monitor__change_search(
  query="<the keyword or natural-language phrase>",
  category=<optional>,
  severity=<optional>,
  since=<optional>,
  until=<optional>,
  k=10
)
```

Each hit has `chunk_id`, `heading_path`, `metadata` (category/severity/run_timestamp), `snippet`. Present a concise summary grouped by severity or category.

### Step 3: If empty results

Suggest a broader query (drop filters, try a shorter keyword), or fall back to `mcp__docs-monitor__query_changes` for an exact-filter pass.

### Examples

```
/query-docs breaking                       # all breaking changes (CLI exact filter)
/query-docs "hooks execution order"        # natural-language semantic search
/query-docs "MCP" --since 30d              # keyword + date filter (semantic)
/query-docs --severity high                # exact filter (CLI)
/query-docs --category feature --since 30d # exact filters (CLI)
/query-docs --page hooks.md                # exact filter (CLI)
/query-docs --json                         # machine-readable output (CLI)
```
