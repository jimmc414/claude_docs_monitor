---
name: check-docs
description: Run the documentation monitor, detect and summarize doc changes, and refresh local artifacts. Use when a user asks to check for docs updates, run a docs diff/report cycle, or generate a current change summary from the monitor output.
---

# Check Docs

Run the Codex docs monitor with the same workflow as the existing `.claude/commands/check-docs.md` command.

## Workflow

### 1. Bootstrap paths

Use these paths:

- Script path: `/mnt/c/python/claude_docs_monitor/codex_docs_monitor.py`
- Working data dir: `~/.local/share/codex-docs-monitor`
- Project mirror dir: `/mnt/c/python/claude_docs_monitor`

Create the data directory if missing:

```bash
mkdir -p ~/.local/share/codex-docs-monitor
```

If the script path is missing, stop and tell the user the script is not installed in the repo.

### 2. Ensure dependency

Install `httpx` only if missing:

```bash
python -c "import httpx" 2>/dev/null || pip install "httpx[http2]>=0.27,<1.0"
```

### 3. Run monitor

Run with provided arguments, but always include `--digest` by default.

Build args so `--digest` is appended only if it is not already present:

```bash
ARGS="$ARGUMENTS"
case " $ARGS " in
  *" --digest "*) ;;
  *) ARGS="$ARGS --digest" ;;
esac
cd ~/.local/share/codex-docs-monitor && python /mnt/c/python/claude_docs_monitor/codex_docs_monitor.py $ARGS
```

If no arguments are provided, this runs default check mode with digest auto-enabled.

### 4. Mirror outputs to project

After completion, copy generated artifacts back into the project directory:

```bash
cp -r ~/.local/share/codex-docs-monitor/data-codex/* /mnt/c/python/claude_docs_monitor/data-codex/
```

Create destination first if needed:

```bash
mkdir -p /mnt/c/python/claude_docs_monitor/data-codex
```

### 5. Digest output handling

`--digest` is always enabled in step 3. The monitor auto-runs digest only when changes are detected.

Mirror digest outputs if present:

```bash
cp ~/.local/share/codex-docs-monitor/data-codex/digest.* /mnt/c/python/claude_docs_monitor/data-codex/ 2>/dev/null || true
```

### 6. Summarize for user

Read `/mnt/c/python/claude_docs_monitor/data-codex/report.md` and provide a concise summary with:

- Number of changed/added/removed pages
- Which pages changed
- Any fetch/errors

If no changes were detected, state that clearly.
