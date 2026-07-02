---
name: ask-docs
description: Answer questions using only locally cached documentation pages from the docs monitor. Use when a user asks how something works in the tracked docs and wants a source-grounded answer without live web fetching.
---

# Ask Docs

Answer a question about OpenAI Codex by searching locally cached documentation pages.

**User question:** Use the user's prompt as the question.

## Instructions

### 1. Check cache freshness

Run this to get the last-modified time of the cached docs:

```bash
stat -c '%y' /mnt/c/python/claude_docs_monitor/data-codex/pages/*.md 2>/dev/null | sort -r | head -1
```

Note this timestamp; include it at the end of the answer.

If no files are found, tell the user to run `$check-docs` first, then stop.

### 2. Search for relevant pages

Use grep searches over `/mnt/c/python/claude_docs_monitor/data-codex/pages/*.md` for keywords extracted from the user's question. Run multiple searches in parallel when the question has distinct concepts.

Guidelines:

- Start with files-only matching to identify relevant pages
- Search 2-4 keyword variations
- Include nearby terminology the docs may use instead

### 3. Read the most relevant pages

Read the top 2-5 matching files (the ones that appear most across searches or most directly match the topic).

Do not read the full corpus unless the question truly requires it.

### 4. Answer the question

Synthesize a clear answer using the cached docs only.

Rules:

- Answer from docs only; do not add external knowledge
- If docs do not cover something, say so explicitly
- Cite source filenames after key facts, e.g. `(overview.md)`
- Quote sparingly (short quotes only)
- Keep the answer concise and readable

### 5. Add freshness line

End with one line:

`Docs last updated: {timestamp from step 1}`

## If no question is provided

Ask what the user wants to know about Codex docs, with examples:

- "How do I use the Codex CLI?"
- "What are the sandboxing and approval options?"
- "How do I configure MCP with Codex?"
- "What changed in the latest docs update?"
