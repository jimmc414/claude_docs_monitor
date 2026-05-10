---
description: AI-analyze latest doc changes into an actionable digest
allowed-tools: Bash, Read
argument-hint: [--model MODEL] [--report DIR]
---

# Digest

Run the AI-powered digest on the latest documentation changes.

The script writes natively to `data-claude/` in the project directory, so there's no copy step.

## Instructions

### Step 1: Run the digest command

```bash
cd /mnt/c/python/claude_docs_monitor && python ~/.claude/lib/claude_docs_monitor.py digest $ARGUMENTS
```

Output lands at `data-claude/digest.md` and `data-claude/digest.html`.

### Step 2: Show the digest

Read `/mnt/c/python/claude_docs_monitor/data-claude/digest.md` and present it to the user.
