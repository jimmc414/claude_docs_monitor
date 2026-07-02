---
description: AI-analyze latest doc changes into an actionable digest
allowed-tools: Bash, Read
argument-hint: [--model MODEL] [--report DIR] [--output digest|dashboard|both]
---

# Digest

Run the AI-powered digest on the latest documentation changes.

The script writes natively to `data-claude/` in the project directory, so there's no copy step.

The output mode (`digest` / `dashboard` / `both`) is resolved at runtime in this
precedence order: `--output` CLI flag → `DOCS_MONITOR_OUTPUT` env var →
`data-claude/config.yaml` (`output: ...`) → built-in default `both`.

## Instructions

### Step 1: Run the digest command

```bash
cd /mnt/c/python/claude_docs_monitor && python ~/.claude/lib/claude_docs_monitor.py digest $ARGUMENTS
```

Possible outputs in `data-claude/`:
- `digest.md` + `digest.html` — narrative LLM digest (when output ∈ {digest, both})
- `dashboard.html` — interactive event browser (when output ∈ {dashboard, both})

### Step 2: Show what was produced

After the command completes, list files in `/mnt/c/python/claude_docs_monitor/data-claude/`
and present the user with whichever artifacts were just generated:

- If `digest.md` was modified by this run: read it and present the narrative.
- If `dashboard.html` was modified by this run: tell the user
  "Dashboard is at `data-claude/dashboard.html` (it should also have auto-opened
  in your browser unless you passed `--no-open` or set `auto_open: false` in
  `data-claude/config.yaml`)."
- If both were modified: show the digest narrative first, then mention the
  dashboard as the exploratory companion view.

Use file mtimes to tell which artifacts the current run produced — older
artifacts left over from prior runs should not be presented as if they were
just regenerated.
