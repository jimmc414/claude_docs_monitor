---
description: Run Claude docs monitor — fetch all pages, detect changes, generate reports
allowed-tools: Bash, Read
---

# Check Claude Docs

Run the Claude Code documentation change monitor. Fetches all 56 doc pages, compares against previous snapshots, displays a change summary with unified diffs, updates local `.md` files, and generates HTML/Markdown reports (both per-run and cumulative history).

## What it does

1. Runs `python claude_docs_monitor.py` from the project directory
2. Shows the terminal output (summary table + diffs)
3. Reads and summarizes the generated `data/report.md` for a quick overview

## Usage

```
/check-docs
/check-docs --quiet
/check-docs --report ~/my-reports
```

## Instructions

Run the following command from the project root at `/mnt/c/python/claude_docs`:

```bash
python /mnt/c/python/claude_docs/claude_docs_monitor.py $ARGUMENTS
```

After the command completes, read `/mnt/c/python/claude_docs/data/report.md` (first 30 lines) and present a brief summary to the user highlighting:
- Number of changed/added/removed pages
- Which specific pages changed (if any)
- Any errors encountered

If no changes were detected, just say so concisely.
