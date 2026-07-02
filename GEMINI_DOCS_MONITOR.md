# Gemini Docs Monitor — Command Reference

## What This Is

`gemini_docs_monitor.py` is a parallel monitor for Gemini CLI docs at `https://geminicli.com/`.
It mirrors the Claude monitor workflow:

- Discover pages from `https://geminicli.com/llms.txt`
- Fetch concurrently from GitHub raw sources
- Store append-only snapshots in SQLite
- Compute unified diffs
- Generate run reports + cumulative history
- Build AI digests + structured change events using the `gemini` CLI

## Defaults

- Database and outputs: `data-gemini/`
- Snapshot DB: `data-gemini/snapshots.db`
- Latest pages: `data-gemini/pages/*.md`
- Reports: `data-gemini/report.{md,html}` and `data-gemini/history.{md,html}`
- Digest: `data-gemini/digest.{md,html}`

## Commands

```bash
python gemini_docs_monitor.py                         # default: check
python gemini_docs_monitor.py check --quiet
python gemini_docs_monitor.py check --poll 3600
python gemini_docs_monitor.py check --dump ~/docs
python gemini_docs_monitor.py check --report ~/reports
python gemini_docs_monitor.py check --digest

python gemini_docs_monitor.py history
python gemini_docs_monitor.py history URL
python gemini_docs_monitor.py diff URL
python gemini_docs_monitor.py urls
python gemini_docs_monitor.py dump
python gemini_docs_monitor.py dump ~/review
python gemini_docs_monitor.py rebuild-history

python gemini_docs_monitor.py digest
python gemini_docs_monitor.py digest --model gemini-2.0-flash
python gemini_docs_monitor.py digest --since 7d

python gemini_docs_monitor.py query breaking
python gemini_docs_monitor.py query --since 7d
python gemini_docs_monitor.py query "sandbox" --severity high
python gemini_docs_monitor.py query --json | jq .

python gemini_docs_monitor.py backfill --dry-run
python gemini_docs_monitor.py backfill
```

## AI Features

The `digest` and `backfill` commands use the locally installed `gemini` CLI to perform structured analysis of diffs. It extracts changes into categories (feature, breaking, deprecation, etc.) and assigns severity levels.

Ensure you have the `gemini` CLI installed and authenticated:
```bash
npm install -g @google/gemini-cli
gemini --version
```

## MCP Server

An MCP server (`mcp_server_gemini.py`) exposes the documentation intelligence database.

**Install into Gemini CLI:**
```bash
gemini mcp add docs-monitor -- python /path/to/mcp_server_gemini.py
```

## Notes

- First `check` run creates a baseline (no diffs yet).
- `check --digest` auto-runs digest only when changes are detected.
- `query` reads from `change_events`, which is populated by `digest` and `backfill`.
- Existing `claude_docs_monitor.py` remains unchanged.
