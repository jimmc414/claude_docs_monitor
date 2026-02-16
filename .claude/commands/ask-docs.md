---
description: Answer questions about Claude Code using locally cached documentation
allowed-tools: Bash, Read, Grep, Glob
---

# Ask Docs

Answer a question about Claude Code by searching the locally cached documentation pages.

**User question:** $ARGUMENTS

## Instructions

### Step 1: Check freshness

Run this to get the last-modified time of the cached docs:

```bash
stat -c '%y' data/pages/*.md 2>/dev/null | sort -r | head -1
```

Note this timestamp — you will include it at the end of your answer.

### Step 2: Search for relevant pages

Use the Grep tool to search `data/pages/*.md` for keywords extracted from the user's question. Run multiple searches in parallel if the question contains distinct concepts (e.g., "hooks" and "permissions" should be two separate searches).

- Use `output_mode: "files_with_matches"` first to identify which files are relevant
- Search for 2-4 keyword variations (e.g., for "MCP servers" search both "MCP" and "mcp server")
- Also search for closely related terms the docs might use instead

### Step 3: Read the most relevant pages

Read the top 2-5 matching files (the ones that appeared most frequently across your searches, or that most directly match the question). If a question is clearly about a single topic (e.g., "how do hooks work?"), reading 1-2 files may be enough.

Do NOT read all 56 pages. Be selective.

### Step 4: Answer the question

Synthesize a clear, direct answer based on what you read. Follow these rules:

- **Answer from the docs only.** Do not supplement with outside knowledge. If the docs don't cover something, say so.
- **Cite your sources.** After each key fact, note the source file in parentheses, e.g., `(hooks.md)`. Use just the filename, not the full path.
- **Quote sparingly.** Short inline quotes are fine for important details; don't dump large blocks.
- **Be concise.** Match the complexity of your answer to the complexity of the question. A simple question gets a short answer.
- **Structure for readability.** Use headers/bullets for multi-part answers, plain prose for simple ones.

### Step 5: Add freshness note

End your answer with a single line:

> Docs last updated: {timestamp from Step 1}

## If no arguments provided

If `$ARGUMENTS` is empty, ask the user what they'd like to know about Claude Code. Mention a few example queries:

- "How do hooks work?"
- "What are the sandboxing options?"
- "How do I configure MCP servers?"
- "What changed in the latest changelog?"
