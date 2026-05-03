---
description: AI-analyze latest doc changes into an actionable digest
allowed-tools: Bash, Read
argument-hint: [--model MODEL] [--report DIR]
---

# Digest

Run the AI-powered digest on the latest documentation changes.

## Instructions

### Step 1: Run the digest command

```bash
cd ~/.local/share/claude-docs-monitor && python ~/.claude/lib/claude_docs_monitor.py digest --report ~/.local/share/claude-docs-monitor/data-claude $ARGUMENTS
```

### Step 2: Copy outputs to project directory

```bash
mkdir -p /mnt/c/python/claude_docs_monitor/data-claude
cp ~/.local/share/claude-docs-monitor/data-claude/digest.* /mnt/c/python/claude_docs_monitor/data-claude/ 2>/dev/null || true
```

### Step 3: Show the digest

Read `/mnt/c/python/claude_docs_monitor/data-claude/digest.md` and present it to the user.
