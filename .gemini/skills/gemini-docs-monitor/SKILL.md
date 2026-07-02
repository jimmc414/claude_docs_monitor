---
name: gemini-docs-monitor
description: Monitor Gemini CLI documentation for changes and answer questions using cached docs. Use when the user wants to check for doc updates or ask questions specifically about Gemini CLI.
---

# Gemini Docs Monitor

This skill allows you to monitor Gemini CLI documentation for changes and answer questions based on the locally cached documentation.

## Commands

### `/check-docs`
Run the Gemini CLI documentation change monitor with automatic AI digest generation.

**Workflow:**
1. Run `./gemini_docs_monitor.py check --digest` in the project root (`/mnt/c/python/claude_docs_monitor/`).
2. Read `data-gemini/report.md` and present a brief summary to the user.
3. If changes were detected, the AI digest will have been automatically generated in `data-gemini/digest.md`. Read and summarize it for the user.

### `/ask-docs <question>`
Answer questions about Gemini CLI using the locally cached documentation in `data-gemini/pages/`.

**Workflow:**
1. **Check freshness**: Run `stat -c '%y' data-gemini/pages/*.md 2>/dev/null | sort -r | head -1`. Note this timestamp for the end of your answer.
2. **Search for relevant pages**: Use `grep_search` on `data-gemini/pages/*.md` for keywords from the user's question. Run multiple searches in parallel if needed.
3. **Read relevant pages**: Read the top 2-5 matching files. Be selective.
4. **Answer the question**: Synthesize a clear answer based *only* on the docs.
   - Cite sources in parentheses, e.g., `(model.md)`.
   - Quote sparingly.
   - Be concise.
5. **Add freshness note**: End with `> Docs last updated: {timestamp}`.

**If no question is provided**: Ask the user what they'd like to know about Gemini CLI. Suggest examples:
- "How do I configure custom commands?"
- "What are Agent Skills?"
- "How does Plan Mode work?"
- "How do I set up an MCP server?"

## Instructions

- **Location**: All scripts and data reside in `/mnt/c/python/claude_docs_monitor/`.
- **Environment**: Ensure `httpx` is available before running the monitor.
- **Data Source**: Always use `data-gemini/pages/` for `/ask-docs`.
