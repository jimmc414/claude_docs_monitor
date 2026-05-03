---
name: check-docs
description: Run Claude docs monitor — fetch all pages, detect changes, generate reports and digest
allowed-tools: Bash, Read
argument-hint: [--quiet] [--report DIR] [--poll SEC]
---

# Check Claude Docs

Run the Claude Code documentation change monitor. Fetches all doc pages, compares against previous snapshots, displays a change summary with unified diffs, updates local `.md` files, generates HTML/Markdown reports (both per-run and cumulative history), and automatically runs an AI digest if changes are detected.

## Usage

```
/check-docs
/check-docs --quiet
/check-docs --report ~/my-reports
```

## Instructions

This skill is self-contained. The monitor script lives at `~/.claude/lib/claude_docs_monitor.py` and stores its data at `~/.local/share/claude-docs-monitor/data-claude/`.

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

### Step 3: Run the monitor with automatic digest

The `--digest` flag makes the script automatically run the AI digest if any changes are detected.

```bash
cd ~/.local/share/claude-docs-monitor && python ~/.claude/lib/claude_docs_monitor.py check --digest --report ~/.local/share/claude-docs-monitor/data-claude $ARGUMENTS
```

### Step 4: Copy outputs to project directory

After the monitor finishes, copy all output files to the project working directory:

```bash
mkdir -p /mnt/c/python/claude_docs_monitor/data-claude
cp -r ~/.local/share/claude-docs-monitor/data-claude/* /mnt/c/python/claude_docs_monitor/data-claude/
```

This ensures `data-claude/pages/`, `data-claude/report.md`, `data-claude/report.html`, etc. are always up to date in the project directory.

### Step 5: Summarize

After the command completes, read `/mnt/c/python/claude_docs_monitor/data-claude/report.md` (first 30 lines) and present a brief summary to the user highlighting:
- Number of changed/added/removed pages
- Which specific pages changed (if any)
- Any errors encountered

If no changes were detected, just say so concisely.
