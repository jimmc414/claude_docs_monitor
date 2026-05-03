---
description: Answer questions about Claude Code or the Agent SDK using cached documentation (hybrid retrieval)
allowed-tools: Bash, Read, Grep, Glob, mcp__docs-monitor__hybrid_search, mcp__docs-monitor__get_chunk
argument-hint: [question about Claude Code or Agent SDK]
---

# Ask Docs

Answer a question about Claude Code or the Agent SDK using the locally cached documentation. Uses hybrid retrieval (BM25 + dense + LLM rerank) when the docs-monitor MCP server is available; falls back to grep otherwise.

**User question:** $ARGUMENTS

## Instructions

### Step 1: Check freshness

Run this to get the last-modified time of the cached docs:

```bash
stat -c '%y' data-claude/pages/*.md data-claude/pages/**/*.md 2>/dev/null | sort -r | head -1
```

Note this timestamp — you will include it at the end of your answer.

### Step 2: Try hybrid search via MCP

If the `mcp__docs-monitor__hybrid_search` tool is available, prefer it over Grep. Hybrid search combines BM25 keyword matching, dense semantic similarity, and an LLM rerank pass — it surfaces docs that match the *intent* of the question, not just exact keywords.

Call it like:

```
mcp__docs-monitor__hybrid_search(query="<the user's question verbatim>", source_type="page", k=8, rerank=true)
```

Source-type guidance:
- `source_type="page"` for "how do I X?" / "what is Y?" — stable docs.
- `source_type="change_event"` for "what changed about X?" / "is X new?" — change history.
- `source_type=null` (omit) if you're unsure or the question spans both.

If MCP is **unavailable** (no `mcp__docs-monitor__*` tools listed), fall back to Step 2b:

#### Step 2b: Fallback grep

Use the Grep tool to search `data-claude/pages/*.md` (Claude Code docs) or `data-claude/pages/agent-sdk/*.md` (Agent SDK). Pick the right scope:
- "SDK", "ClaudeSDKClient", "query()", "agent loop", "custom tools" → `data-claude/pages/agent-sdk/`
- CLI usage, slash commands, settings, hooks → `data-claude/pages/`
- Unclear → both.

Use `output_mode: "files_with_matches"` first; search 2-4 keyword variations.

### Step 3: Read top chunks

If you used hybrid_search: each hit has a `chunk_id`. For the top 2-3 most-relevant hits, call `mcp__docs-monitor__get_chunk(chunk_id=N)` to get the full chunk content.

If you used grep: read the top 2-5 matching files.

Be selective — there are 100+ pages. Don't read them all.

### Step 4: Answer the question

Synthesize a clear, direct answer. Rules:

- **Answer from the docs only.** If the docs don't cover something, say so.
- **Cite your sources.** After each key fact, cite using the chunk's `heading_path` and (if available) line numbers: `(hooks.md > Hook Events § PreToolUse, L42-58)` or just `(hooks.md)` for grep fallback.
- **Quote sparingly.** Short inline quotes for important details; no large blocks.
- **Be concise.** Match answer complexity to question complexity.
- **Structure for readability.** Headers/bullets for multi-part answers; plain prose otherwise.

### Step 5: Add freshness note

End your answer with:

> Docs last updated: {timestamp from Step 1}

## If no arguments provided

If `$ARGUMENTS` is empty, ask the user what they'd like to know. Examples:

- "How do hooks work?"
- "What are the sandboxing options?"
- "How do I configure MCP servers?"
- "How do I use structured outputs in the Agent SDK?"
- "What's the difference between query() and ClaudeSDKClient?"
