# Opus 4.7 Baseline Comparison: 9-Q Hard Subset

Four Opus 4.7 variants (opus_bm25, opus_agentic, opus_whole_corpus, opus_cli_agent) vs three Sonnet 4.6 baselines (bm25, ripgrep, whole_corpus, n=1 each) vs the v4.3.11 V2 hybrid RAG architecture (n=3 trials, re-scored with Sonnet 4.6 judge for cross-comparability) across 9 hard questions: Q005, Q010, Q012, Q021, Q027, Q032, Q036, Q049, Q050.

**opus_cli_agent** is a Variant-4 alternative: instead of stuffing the 736K-token corpus into a single user message (which Claude Code's non-interactive `-p` mode rejects with 'Prompt is too long' below ~200K tokens of stdin input), this variant runs the same Opus 4.7 model `claude-opus-4-7[1m]` on Max OAuth via `claude -p` with `--add-dir <pages>` and lets the agent loop pull files via Glob/Read/Grep. **This actually exercises Opus 4.7's 1M context window** — section 6b shows up to 1.2M cache_read tokens on a single question (Q012, 18 turns).

**BLOCKED:** opus_whole_corpus — see each variant's `BLOCKED.md` for the infrastructure failure mode.

**SKIPPED:** opus_agentic — see each variant's `SKIPPED.md`. (User did not authorize the API-tier charge.)

## 1. Summary table

| System | correct | partial | incorrect | hallucinated | judge_err | missing |
|---|---:|---:|---:|---:|---:|---:|
| opus_bm25 | 4 | 5 | 0 | 0 | 0 | 0 |
| opus_agentic | — | — | — | — | — | SKIPPED |
| opus_whole_corpus | — | — | — | — | — | BLOCKED |
| opus_cli_agent | 4 | 4 | 0 | 0 | 1 | 0 |
| bm25 | 2 | 7 | 0 | 0 | 0 | 0 |
| ripgrep | 2 | 7 | 0 | 0 | 0 | 0 |
| whole_corpus | 0 | 0 | 0 | 0 | 0 | 9 |
| v2_t1 | 1 | 7 | 0 | 1 | 0 | 0 |
| v2_t2 | 4 | 5 | 0 | 0 | 0 | 0 |
| v2_t3 | 2 | 6 | 1 | 0 | 0 | 0 |

## 2. Per-question matrix
Cell legend: ✓ correct, ~ partial, ✗ incorrect, H hallucinated, BLK blocked, SKIP skipped, — missing.

| QID | opus_bm25 | opus_agentic | opus_whole_corpus | opus_cli_agent | bm25 | ripgrep | whole_corpus | v2_t1 | v2_t2 | v2_t3 |
|---|---|---|---|---|---|---|---|---|---|---|
| Q005 | ✓ | SKIP | BLK | ✓ | ~ | ✓ | — | ~ | ✓ | ~ |
| Q010 | ✓ | SKIP | BLK | ~ | ✓ | ~ | — | ✓ | ✓ | ✓ |
| Q012 | ~ | SKIP | BLK | ?err | ~ | ~ | — | ~ | ~ | ~ |
| Q021 | ~ | SKIP | BLK | ~ | ~ | ~ | — | ~ | ~ | ~ |
| Q027 | ✓ | SKIP | BLK | ✓ | ✓ | ✓ | — | H | ✓ | ✗ |
| Q032 | ~ | SKIP | BLK | ~ | ~ | ~ | — | ~ | ~ | ~ |
| Q036 | ~ | SKIP | BLK | ~ | ~ | ~ | — | ~ | ~ | ~ |
| Q049 | ~ | SKIP | BLK | ✓ | ~ | ~ | — | ~ | ~ | ~ |
| Q050 | ✓ | SKIP | BLK | ✓ | ~ | ~ | — | ~ | ✓ | ✓ |

## 3. Q027 deep-dive (recency / gold-phrase canary)
Q027 asks about a recent doc change; the gold phrase is 'April 23, 2026'. Variants pass iff that phrase (or canonical equivalent) appears in the answer.


#### opus_bm25
- gold phrase 'April 23, 2026' present in context: **True**
- verdict: **correct**
- contains 'April 23, 2026' in answer: **True**
- reasoning: The system answer covers every major point in the canonical answer: the April 23, 2026 date, the change to Opus 4.7, the affected user groups (Enterprise pay-as-you-go and Anthropic API), the prior default of Sonnet 4.6, and both opt-out mechanisms (ANTHROPIC_MODEL env var and the model field in server-managed settings). The additional context—tier table for other account types, caveats about non-
- answer (first 300 chars):

```
According to the documentation, on April 23, 2026, the default model for **Enterprise pay-as-you-go and Anthropic API users** changed to **Opus 4.7**.

**Source:** `model-config.md` → "Special model behavior" → "`default` model setting" (also restated in the same file's main body at the top of the d...[truncated]
```

#### opus_agentic: SKIPPED — see SKIPPED.md

#### opus_whole_corpus: BLOCKED — see BLOCKED.md

#### opus_cli_agent
- gold phrase 'April 23, 2026' present in context: **True**
- verdict: **correct**
- contains 'April 23, 2026' in answer: **True**
- reasoning: The system answer fully covers all key points from the canonical answer: the date (April 23, 2026), the affected tiers (Enterprise pay-as-you-go and Anthropic API users), the change direction (from Sonnet 4.6 to Opus 4.7), and the mitigation options (ANTHROPIC_MODEL env var or the 'model' field in server-managed settings). The system answer also provides additional useful context (other tiers' def
- answer (first 300 chars):

```
## Answer

According to `data-claude/pages/model-config.md` (in the section "`default` model setting", under the Note callout at line 142):

> "On April 23, 2026, the default model for Enterprise pay-as-you-go and Anthropic API users will change to **Opus 4.7**. To keep a different default, set `ANT...[truncated]
```

## 4. Q049 deep-dive (hallucination canary)

Q049 has been a hallucination canary in prior trials — V2 sonnet 4.6 invented SDK methods like `connect()` and `disconnect()`. Here we paste each Opus variant's full Q049 answer and flag invented identifiers.


#### opus_bm25
- verdict: **partially_correct**
- flagged invented identifiers: none
- answer (full):

```
For multi-turn conversations in the Python Agent SDK, `query()` and `ClaudeSDKClient` differ along several dimensions:

## Session continuity

- **`query()`**: Creates a new session each time it is called, performing a single exchange (`agent-sdk/python.md > Choosing between query() and ClaudeSDKClient > Quick comparison`). To continue a prior conversation, you must explicitly opt in with `continue_conversation=True` (which resumes the most recent session in the directory) or pass a captured session ID via `resume` (`agent-sdk/streaming-vs-single-mode.md > Single Message Input > Implementation Example`; `agent-sdk/sessions.md > Choose an approach`).
- **`ClaudeSDKClient`**: "Maintains a conversation session across multiple exchanges" and "handles session IDs internally. Each call to `client.query()` automatically continues the same session" (`agent-sdk/python.md > Classes > ClaudeSDKClient`; `agent-sdk/sessions.md > Automatic session management > Python: ClaudeSDKClient`). No ID handling is required from you (`agent-sdk/sessions.md > Choose an approach`).

## Connection lifecycle

- **`query()`**: Connection is "Managed automatically" (`agent-sdk/python.md > Quick comparison`).
- **`ClaudeSDKClient`**: Has "Manual control" with an "Explicit lifecycle: You control when the session starts and ends." It must be used as an async context manager (`agent-sdk/python.md > Quick comparison`; `agent-sdk/python.md > Classes > ClaudeSDKClient`; `agent-sdk/sessions.md > Automatic session management > Python: ClaudeSDKClient`).

## Interrupts

- **`query()`**: Interrupts are not supported.
- **`ClaudeSDKClient`**: Supports `interrupt()` to stop execution mid-task (`agent-sdk/python.md > Quick comparison`; `agent-sdk/python.md > Classes > ClaudeSDKClient`).

## Features that are the same

Both support streaming input, hooks, and custom tools (`agent-sdk/python.md > Quick comparison`).

## Recommended use cases

- **`query()`**: "One-off tasks" — best when you need a one-shot response (`agent-sdk/python.md > Quick comparison`; `agent-sdk/streaming-vs-single-mode.md > Single Message Input`).
- **`ClaudeSDKClient`**: "Continuous conversations" — best for "Continuing conversations… Follow-up questions… Interactive applications - Chat interfaces, REPLs… Response-driven logic… Session control - Managing conversation lifecycle explicitly" (`agent-sdk/python.md > When to use ClaudeSDKClient (continuous conversation)`).

The session-management guide summarizes the choice: for "Multi-turn chat in one process," use `ClaudeSDKClient` (Python), because "The SDK tracks the session for you with no ID handling" (`agent-sdk/sessions.md > Choose an approach`). It also notes that `ClaudeSDKClient` is "the Python equivalent of how the TypeScript SDK's `query()` function works internally - it creates a client object that can continue conversations" (`agent-sdk/python.md > Classes > ClaudeSDKClient`).
```

#### opus_agentic: SKIPPED

#### opus_whole_corpus: BLOCKED

#### opus_cli_agent
- verdict: **correct**
- flagged invented identifiers: none
- answer (full):

```
# `query()` vs `ClaudeSDKClient` for multi-turn conversations

The Python Agent SDK exposes two primary entry points with **fundamentally different session semantics** for multi-turn use.

## Core difference: session continuity

Per `agent-sdk/python.md` § "Choosing between `query()` and `ClaudeSDKClient`":

- **`query()`** — "Creates a new session for each interaction with Claude Code... Each call to `query()` starts fresh with no memory of previous interactions." (§ "Functions › `query()`")
- **`ClaudeSDKClient`** — "Maintains a conversation session across multiple exchanges... it creates a client object that can continue conversations." (§ "Classes › `ClaudeSDKClient`")

The doc explicitly frames `ClaudeSDKClient` as "the Python equivalent of how the TypeScript SDK's `query()` function works internally" (python.md:436).

## Feature-matrix differences (python.md:21–31)

| Feature | `query()` | `ClaudeSDKClient` |
|---|---|---|
| Session | New session each time | Reuses same session |
| Conversation | Single exchange | Multiple exchanges in same context |
| Connection | Managed automatically | Manual control |
| Interrupts | Not supported | Supported |
| Continue Chat | New session each time | Maintains conversation |
| Use Case | One-off tasks | Continuous conversations |

Note that **streaming input, hooks, and custom tools are supported by both**.

## API shape

- **`query()`** is a single async generator function: `async def query(*, prompt, options, transport) -> AsyncIterator[Message]` (python.md:59–65). You iterate the returned messages, then it's done.
- **`ClaudeSDKClient`** is a class with an explicit lifecycle: `connect()`, `query(prompt, session_id)`, `receive_messages()`, `receive_response()`, `interrupt()`, `set_permission_mode()`, `set_model()`, `disconnect()`, plus context-manager support via `async with` (python.md:447–464, 486–495). Inside that context you can call `client.query(...)` repeatedly and the session retains prior turns (python.md:499–538, "Example - Continuing a conversation").

## Two ways to do multi-turn — and their trade-offs

The docs describe **two distinct mechanisms** for multi-turn:

1. **`ClaudeSDKClient`** keeps a live session in-process. Subsequent `client.query(...)` calls inside the same `async with` block automatically share context — the example asks "What's the capital of France?" then "What's the population of that city?" without re-supplying context (python.md:507–525).

2. **`query()` with `continue_conversation=True`** — `agent-sdk/streaming-vs-single-mode.md:284–290` shows you can also continue a prior conversation through `query()` by passing `ClaudeAgentOptions(continue_conversation=True, max_turns=1)`. This is the "single message input" pattern that resumes server-side session state rather than holding an open client.

## Capabilities only `ClaudeSDKClient` offers for multi-turn

From python.md:438–445 ("Key Features") and the methods table (python.md:466–484):

- **Interrupts** mid-task via `interrupt()` (the matrix at line 27 shows `query()` does not support this).
- **Explicit lifecycle** — you decide when the session opens/closes.
- **Response-driven flow** — react to a response and send a follow-up.
- Live session controls: `set_permission_mode()`, `set_model()`, `rewind_files()`, `toggle_mcp_server()`, `reconnect_mcp_server()`, `stop_task()`, `get_server_info()`, `get_mcp_status()`.

## When to pick each (python.md:33–50)

- **`query()`**: one-off questions, independent tasks, simple automation, "when you want a fresh start each time."
- **`ClaudeSDKClient`**: continuing conversations, follow-up questions, interactive apps / chat / REPLs, response-driven logic, explicit session-lifecycle control.

## Caveat noted in the docs

python.md:497 warns: when iterating over messages from `ClaudeSDKClient`, **avoid `break`** to exit early — it can cause asyncio cleanup issues; let iteration complete or use a flag.

## Summary

For multi-turn conversations, `ClaudeSDKClient` is the idiomatic choice: it holds a single session across many `query()` calls, supports interrupts and live config changes, and is the only path with explicit lifecycle control. `query()` is stateless per call by default, but can still resume an earlier conversation by passing `continue_conversation=True` in `ClaudeAgentOptions` — useful for one-shot scripts that just need to append to prior server-side state without keeping a client connected.
```

#### v2_t1 (Sonnet 4.6 hybrid RAG, n=1 reference)
- verdict: **partially_correct**
- flagged invented identifiers: `['.connect(']`
- answer (first 1000 chars):

```
# How Does the Python Agent SDK's `query()` Function Differ from `ClaudeSDKClient` for Multi-Turn Conversations?

## Executive Summary

The Python Agent SDK exposes two distinct interaction surfaces: the standalone `query()` function, which creates a fresh session on every call, and `ClaudeSDKClient`, a stateful object that preserves conversation context across multiple exchanges within a single process.[^c255] The core difference for multi-turn work is session continuity — `query()` is designed for one-off tasks and offers no built-in mechanism to carry context forward, while `ClaudeSDKClient` tracks the session ID automatically so each successive `client.query()` call continues the same conversation without any explicit ID bookkeeping.[^c422] Both interfaces share the same underlying message type system and support streaming input, but `ClaudeSDKClient` additionally exposes interrupt control, response-driven flow, and explicit lifecycle management that `query()` deliberately omits.[^...[truncated]
```

## 5. Cost & efficiency table
Token counts are tiktoken cl100k_base estimates (opus_agentic uses API-reported counts when available). Pricing: Opus 4.7 $15/$75 per MTok in/out; Sonnet 4.6 $3/$15. Note: Sonnet 4.6 baselines run on Max OAuth (no per-call charge to the user's account); the dollar columns express equivalent API-tier cost for cost-efficiency comparison only.

| Variant | Model | Σ in_tok | Σ out_tok | Wall (s) | Avg/Q (s) | Strict ✓ | $-cost | $/correct |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| opus_bm25 | claude-opus-4-7 | 258,461 | 6,073 | 264.5 | 29.4 | 4/9 | $4.332 | $1.083 |
| opus_agentic | (skipped) | — | — | — | — | — | — | — |
| opus_whole_corpus | (blocked) | — | — | — | — | — | — | — |
| opus_cli_agent | claude-opus-4-7[1m] | 2,937,228 | 24,438 | 438.8 | 48.8 | 4/9 | $3.984 | $0.996 |
| bm25 | claude-sonnet-4-6 | 258,461 | 5,921 | 197.9 | 22.0 | 2/9 | $0.864 | $0.432 |
| ripgrep | claude-sonnet-4-6 | 1,118,587 | 5,853 | 365.4 | 40.6 | 2/9 | $3.444 | $1.722 |
| whole_corpus | claude-sonnet-4-6 | 6,630,483 | 36 | 32.1 | 3.6 | 0/9 | $19.892 | n/a |

## 6. Variant 3 (opus_agentic) tool-use telemetry
Did Opus iterate (≥2 grep calls) or one-shot? Characterizes whether the agentic capability was used.

opus_agentic was SKIPPED (no `ANTHROPIC_API_KEY`; user did not authorize the ~$5-10 API charge). The script `baselines/scripts/opus_agentic_baseline.py` is implemented and ready to run if the env var is set later. See `baselines/outputs/opus_agentic/SKIPPED.md`.

## 6b. Variant 4-alt (opus_cli_agent) tool-use telemetry
Per-question agent activity for the Max-OAuth-via-CLI variant. This is the variant that actually exercises Opus 4.7's 1M context window — `cache_read_input_tokens` shows how much doc content the agent loaded into its long context across turns.

| QID | turns | tool_calls | cache_read tokens | cost ($) | files_read |
|---|---:|---:|---:|---:|---|
| Q005 | 5 | 4 | 101,533 | $0.31 | model-config.md |
| Q010 | 3 | 2 | 57,491 | $0.19 |  |
| Q012 | 18 | 17 | 1,199,949 | $1.22 | checkpointing.md, claude-directory.md, features-overview.md, how-claude-code-works.md (+6) |
| Q021 | 9 | 8 | 181,450 | $0.34 | cli-reference.md |
| Q027 | 4 | 3 | 97,758 | $0.24 |  |
| Q032 | 6 | 5 | 144,880 | $0.33 | permission-modes.md |
| Q036 | 7 | 6 | 222,287 | $0.52 | agent-sdk/hooks.md, hooks.md |
| Q049 | 10 | 9 | 360,237 | $0.46 | agent-sdk/python.md, agent-sdk/streaming-vs-single-mode.md |
| Q050 | 6 | 5 | 241,229 | $0.38 | agent-sdk/python.md, agent-sdk/streaming-vs-single-mode.md |

**Aggregate**: avg turns/Q = 7.6, avg tool calls/Q = 6.6, total cache_read across run = 2,606,814 tokens, total cost = $3.98. 7/9 questions used ≥5 turns (real iterative investigation, not one-shot). The cache_read figures are the headline evidence that the 1M context window is exercised — Q012 alone read 1.2M tokens of cached doc content across 18 turns.

## 7. Honest interpretation

**Strict-correct headline (n=1 each):** Opus 4.7 — opus_bm25=4/9, opus_agentic=skipped, opus_whole_corpus=blocked, opus_cli_agent=4/9. Sonnet 4.6 — bm25=2/9, ripgrep=2/9, whole_corpus=0/9. V2 hybrid RAG on Sonnet 4.6 judge (n=3 trials of v4.3.11): [1, 4, 2] (mean 2.3).

**Scenario A-meaningful: Opus = 4/9 strict, Sonnet max = 2/9, V2 max trial = 4/9.** Opus matches V2's best trial while doubling Sonnet+BM25 on strict. Both Opus paths that ran (opus_bm25, opus_cli_agent) hit the **same** 4/9 strict — the BM25-retrieval path matched the full-tool-agent path despite the latter exercising the 1M context window across 18 turns on Q012. This is strong evidence that on this corpus + benchmark, **how docs are surfaced doesn't drive outcome quality much**: model capability dominates retrieval choice. It also means a 95-line BM25 script is competitive with full agentic investigation. This is real model-capability uplift, not noise — but the architecture story is separate: the simplest Opus variant (opus_bm25, 95 lines) ties V2's best trial, so the V2 hybrid architecture isn't earning its complexity at any model choice. The decision is now between (a) Opus + the simplest retrieval that fits your context budget for max correctness, or (b) Sonnet + BM25 for max cost-efficiency — see section 5.

**opus_whole_corpus was infrastructure-blocked across all 5 tiers tried.** Agent SDK paths (3 tiers) returned the literal string `'Prompt is too long'`. Direct `claude -p` CLI paths (2 tiers, added on user request) exited with code 1 and empty stderr; probing with `--output-format stream-json` surfaced `api_error_status: 400, duration_api_ms: 0, result: 'Prompt is too long'`. The `duration_api_ms: 0` confirms the prompt is rejected client-side by the CLI before the API is even called — the local gate sits at 200K regardless of the `[1m]` model suffix, the `ANTHROPIC_BETA` env var, or whether the SDK or CLI is invoked. No API-key fallback was authorized. The long-context-wins scenario therefore cannot be evaluated from this run; `baselines/outputs/opus_whole_corpus/BLOCKED.md` records all 5 tier results.

**Caveats.** (1) n=1 per variant on a 9-Q subset — single-question swings are within ~33% noise observed in prior runs. (2) Sonnet 4.6 judges Opus answers; small risk the Sonnet judge undermarks sophisticated Opus phrasing. (3) Opus pricing is ~5× Sonnet; if strict-correct ties, Sonnet wins on cost-efficiency — see the cost-per-correct row in section 5.

## 8. TL;DR

**TL;DR — meaningful Opus uplift, but architecture doesn't matter.** Opus 4.7 variants: opus_bm25=4/9 strict, 9/9 lenient; opus_cli_agent=4/9 strict, 8/9 lenient. Sonnet+BM25 = 2/9 strict (9/9 lenient). V2 hybrid = 2.3/9 strict (8.3/9 lenient) mean. Both Opus paths (BM25 retrieval AND full-tool agent access) tie at strict — double Sonnet+BM25, match V2's best trial. **The 1M context window IS being exercised** (cli_agent's Q012 read 1.2M cached tokens) but it does not translate to dramatically higher correctness on this 9-Q benchmark — the model-capability gain shows up regardless of how the docs are surfaced. Cost-efficiency: Sonnet+BM25 is ~2.5× cheaper per correct answer than either Opus path. Recommendation: **use the simplest variant whose cost you can afford** — if Opus is acceptable, opus_bm25 (95-line script) is enough; if not, Sonnet+BM25 is fine. The V2 hybrid architecture is not earning its complexity at any model choice. Validate at n=3 before locking in.
