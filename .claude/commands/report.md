---
description: Build an agentic RAG research report on Claude Code docs and change history with inline citations
allowed-tools: Bash, Read, mcp__docs-monitor__build_report, mcp__docs-monitor__get_saved_report
argument-hint: <question> [--scope docs|changes|all] [--since 30d] [--model opus|sonnet]
---

# Report

Build a research report by decomposing the question, retrieving evidence from the cached docs and change history, reasoning in a tool-equipped loop, synthesizing with inline citations, and self-critiquing.

**User input:** $ARGUMENTS

## Instructions

### Step 1: Parse the question and any flags

Split `$ARGUMENTS` into:
- The question (everything before the first `--` flag, or the whole string if no flags).
- Optional flags:
  - `--scope docs|changes|all` (default `all`)
  - `--since DATE` (e.g., `7d`, `30d`, `2026-04-01`)
  - `--until DATE`
  - `--model opus|sonnet|haiku` (default `opus`)
  - `--max-turns N` (default 6)

### Step 2: Try MCP build_report

If `mcp__docs-monitor__build_report` is available, call it:

```
mcp__docs-monitor__build_report(
  question="<the parsed question>",
  scope="<docs|changes|all>",
  since=<optional>,
  until=<optional>,
  model="<opus|sonnet|haiku>",
  max_turns=<6>
)
```

The tool returns `{markdown_path, json_path, evidence_count, loop_turns, elapsed_seconds, preview}`.

### Step 3: Fallback to CLI

If MCP is unavailable, run:

```bash
cd ~/.local/share/claude-docs-monitor && python ~/.claude/lib/claude_docs_monitor.py report "<question>" --scope <scope> [--since DATE] [--model MODEL]
```

### Step 4: Surface the report

- Tell the user the report's markdown path.
- Read the first ~60 lines of the report and present them inline.
- Note the evidence count, loop turns, and elapsed time.
- Offer to open the full report or surface specific sections.

### Examples

```
/report what changed about hooks in the last 30 days?
/report compare subagents and skills --scope docs
/report which features have been added in the last 60 days? --scope changes --since 60d
/report what is the difference between PreToolUse and PermissionRequest hooks?
```

## If no arguments provided

If `$ARGUMENTS` is empty, ask the user what they'd like a report on. Mention sample prompts:

- "what changed about hooks recently?"
- "compare subagents and skills"
- "which features were added in the last 30 days?"
- "what's the difference between query() and ClaudeSDKClient?"
