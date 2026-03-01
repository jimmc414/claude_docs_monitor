---
description: Query the change intelligence database for documentation changes
allowed-tools: Bash, Read
argument-hint: [keyword] [--category CAT] [--since DATE] [--severity SEV]
---

# Query Documentation Changes

Search and filter the accumulated change intelligence database for Claude Code documentation changes.

## Instructions

### Step 1: Run the query command

```bash
cd ~/.local/share/claude-docs-monitor && python ~/.claude/lib/claude_docs_monitor.py query $ARGUMENTS
```

### Step 2: Present results

Read the output and present a concise summary to the user. If no results are found, suggest alternative queries.

### Examples

```
/query-docs breaking                       # all breaking changes
/query-docs "hooks"                        # keyword search
/query-docs --since 7d                     # last 7 days
/query-docs --severity high                # high-severity only
/query-docs --category feature --since 30d # new features in last month
/query-docs --page hooks.md                # all events for hooks.md
/query-docs --json                         # machine-readable output
```
