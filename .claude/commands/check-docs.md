---
description: Run Claude docs monitor — fetch all pages, detect changes, generate reports
allowed-tools: Bash, Read
argument-hint: [--quiet] [--report DIR] [--poll SEC]
---

# Check Claude Docs

Run the Claude Code documentation change monitor. Fetches all doc pages, compares against previous snapshots, displays a change summary with unified diffs, updates local `.md` files, and generates HTML/Markdown reports (both per-run and cumulative history).

The script writes natively to `data-claude/` in the project directory, so there's no copy step.

## Usage

```
/check-docs
/check-docs --quiet
/check-docs --report ~/my-reports
```

## Instructions

The monitor script lives at `~/.claude/lib/claude_docs_monitor.py`. The project working directory is `/mnt/c/python/claude_docs_monitor/`. Running from there causes the script to write `pages/`, `report.*`, `history.*`, and `snapshots.db` directly under `data-claude/` in the project — the same place `/ask-docs` reads from.

### Step 1: Bootstrap (only needed once)

If `~/.claude/lib/claude_docs_monitor.py` does not exist, tell the user:
"The monitor script is not installed. Copy it from the repo: `cp claude_docs_monitor.py ~/.claude/lib/`"
Then stop.

### Step 2: Ensure httpx is installed

```bash
python -c "import httpx" 2>/dev/null || pip install "httpx[http2]>=0.27,<1.0"
```

### Step 3: Run the monitor from the project directory

```bash
cd /mnt/c/python/claude_docs_monitor && python ~/.claude/lib/claude_docs_monitor.py check $ARGUMENTS
```

Output lands in `data-claude/pages/`, `data-claude/report.md`, `data-claude/history.md`, `data-claude/snapshots.db`.

### Step 4: Generate AI digest (if changes detected)

Read the first 15 lines of `/mnt/c/python/claude_docs_monitor/data-claude/report.md`. If the report shows any changes (Changed > 0, Added > 0, or Removed > 0), run the AI digest:

```bash
cd /mnt/c/python/claude_docs_monitor && python ~/.claude/lib/claude_docs_monitor.py digest
```

If no changes were detected, skip this step.

### Step 5: Summarize

Read `/mnt/c/python/claude_docs_monitor/data-claude/report.md` (first 30 lines) and present a brief summary to the user highlighting:
- Number of changed/added/removed pages
- Which specific pages changed (if any)
- Any errors encountered

If no changes were detected, just say so concisely.
