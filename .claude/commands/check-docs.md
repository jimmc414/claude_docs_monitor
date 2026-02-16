---
description: Run Claude docs monitor — fetch all pages, detect changes, generate reports
allowed-tools: Bash, Read
argument-hint: [--quiet] [--report DIR] [--poll SEC]
---

# Check Claude Docs

Run the Claude Code documentation change monitor. Fetches all 56 doc pages, compares against previous snapshots, displays a change summary with unified diffs, updates local `.md` files, and generates HTML/Markdown reports (both per-run and cumulative history).

## What it does

1. Ensures `httpx[http2]` is installed
2. Runs `claude_docs_monitor.py` from `~/.claude/lib/`
3. Shows the terminal output (summary table + diffs)
4. Reads and summarizes the generated report for a quick overview

## Usage

```
/check-docs
/check-docs --quiet
/check-docs --report ~/my-reports
```

## Instructions

This skill is self-contained. The monitor script lives at `~/.claude/lib/claude_docs_monitor.py` and stores its data at `~/.local/share/claude-docs-monitor/`.

### Step 1: Bootstrap (only needed once)

Check if the script and data directory exist. If not, create them:

```bash
mkdir -p ~/.local/share/claude-docs-monitor
```

If `~/.claude/lib/claude_docs_monitor.py` does not exist, tell the user:
"The monitor script is not installed. Copy it from the repo: `cp claude_docs_monitor.py ~/.claude/lib/`"
Then stop.

### Step 2: Ensure httpx is installed

```bash
python -c "import httpx" 2>/dev/null || pip install "httpx[http2]>=0.27,<1.0"
```

### Step 3: Run the monitor

```bash
cd ~/.local/share/claude-docs-monitor && python ~/.claude/lib/claude_docs_monitor.py $ARGUMENTS
```

### Step 4: Summarize

After the command completes, read `~/.local/share/claude-docs-monitor/data/report.md` (first 30 lines) and present a brief summary to the user highlighting:
- Number of changed/added/removed pages
- Which specific pages changed (if any)
- Any errors encountered

If no changes were detected, just say so concisely.
