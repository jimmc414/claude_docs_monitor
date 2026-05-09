# Variant 2 vs Variant 4 — Full Report

Focused, standalone comparison of the two Variant-flavoured Opus 4.7 baselines that were actually run against the 9-Q hard subset: **Variant 2 (`opus_bm25`)** and **Variant 4-alt (`opus_cli_agent`)**, with the BLOCKED original Variant 4 (`opus_whole_corpus`) summarized in Section 3. The 9-system reference is `baselines/opus_comparison.md`; this document is intentionally narrower and meant to be readable on its own.

## 1. Executive summary

- Both variants run Opus 4.7 on Max OAuth and end up at **4/9 strict** (4+5/9 lenient) for opus_bm25 vs **4/9 strict** (4+5/9 lenient) for opus_cli_agent on the 9-Q hard subset.
- They reach the same headline number with very different shapes: opus_bm25 is one LLM call against ~30K tokens of pre-retrieved BM25 chunks; opus_cli_agent is a multi-turn agent loop that pulls files via Glob/Read/Grep tools and reaches up to 1.2M cache_read tokens on a single question.
- Per-question, the variants disagree on three: opus_bm25 wins Q010 (cli_agent's answer invents a `Bash(ls:*)` colon-star variant and adds unsourced line numbers); opus_cli_agent wins Q049 (no invented SDK identifiers); Q012 is the judge_error case re-scored to `partially_correct`.
- The 1M context window is genuinely exercised by opus_cli_agent (Q012 reads 1,199,949 cached tokens across 18 turns) but does **not** translate to higher strict correctness vs simple BM25 retrieval on this benchmark.
- Variant 4 in its **original** form (whole-corpus stuffing) was infrastructure-blocked across all 5 invocation tiers — see Section 3.

## 2. Variant configurations

| Aspect | Variant 2 (opus_bm25) | Variant 4-alt (opus_cli_agent) |
|---|---|---|
| Model ID | `claude-opus-4-7` | `claude-opus-4-7[1m]` |
| Auth | Max OAuth via Agent SDK / CLI tier | Max OAuth via `claude -p` |
| Retrieval | SQLite FTS5 BM25, top-30 chunks pre-loaded | Agent loop: Glob / Read / Grep tools |
| Context per Q | ~30K input tokens | 57K–1.2M cache_read tokens |
| Turns | 1 | 3–18 |
| Tools enabled | none | full Claude Code toolset (`--add-dir <pages>`) |
| Concurrency | 3 | 3 |
| Cost reporting | tiktoken estimate × $/MTok | API-reported `total_cost_usd` per row |
| Source script | `baselines/scripts/opus_bm25_baseline.py` | `baselines/scripts/opus_cli_agent_baseline.py` |

## 3. Why "Variant 4 alt" exists

The original Variant 4 plan was to stuff the entire 736K-token corpus into stdin and let Opus 4.7 answer from a single oversized user message. **All five invocation tiers were blocked** with `Prompt is too long`:

| Tier | Path | Result |
|---|---|---|
| 1 | SDK + model w/ `[1m]` suffix | `Prompt is too long` (18 chars in 4.6s) |
| 2 | SDK + plain Opus 4.7 | `Prompt is too long` (18 chars in 3.3s) |
| 3 | SDK + Opus 4.7 + `ANTHROPIC_BETA=context-1m-2025-08-07` | `Prompt is too long` (18 chars in 3.1s) |
| 4 | CLI `--model claude-opus-4-7[1m]` | exit 1 in 3.6s, empty stderr |
| 5 | CLI `--model claude-opus-4-7` | exit 1 in 3.6s, empty stderr |

Probing tiers 4-5 with `--output-format stream-json --include-partial-messages` surfaced the underlying envelope:

```json
{"type": "result", "subtype": "success", "is_error": true,
 "api_error_status": 400, "duration_ms": 1876, "duration_api_ms": 0,
 "result": "Prompt is too long", "stop_reason": "stop_sequence"}
```

The load-bearing field is **`duration_api_ms: 0`** — the request was rejected client-side by Claude Code before the API was called. The local gate sits at ~200K regardless of the `[1m]` model suffix, the `ANTHROPIC_BETA` env var, or whether the SDK or CLI is invoked. The 1M window the API supports is for accumulated cache content (tool outputs, prior turns), not for a single oversized user message.

**Variant 4-alt sidesteps the gate** by keeping the user message tiny and letting the agent pull the corpus via tools. The `cache_read_input_tokens` figures in Section 8 show this works: a single Q012 invocation accumulates ~1.2M cached tokens of doc content across 18 turns — well past the 200K client-side gate that blocks the whole-corpus path.

Full per-tier evidence: `baselines/outputs/opus_whole_corpus/BLOCKED.md` (2545 chars on disk).

## 4. Headline numbers

| System | correct | partial | incorrect | hallucinated | judge_err | total $ | wall (s) |
|---|---:|---:|---:|---:|---:|---:|---:|
| opus_bm25 | 4 | 5 | 0 | 0 | 0 | $4.33 | 264.5 |
| opus_cli_agent | 4 | 5 | 0 | 0 | 0 | $3.98 | 438.8 |
| opus_whole_corpus | — | — | — | — | — | — | BLOCKED |

`opus_bm25` cost is the tiktoken-estimate × pricing (258,461 in × $15/MTok + 6,073 out × $75/MTok). `opus_cli_agent` cost is the API-reported `total_cost_usd` summed across rows — strictly more accurate because it accounts for the agent's prompt-cache discounts. Wall times are at concurrency=3.

## 5. Per-question matrix

| QID | Question (short) | bm25 | cli_agent |
|---|---|:---:|:---:|
| Q005 | opusplan alias limitations | ✓ | ✓ |
| Q010 | `Bash(ls *)` regex match | ✓ | ~ |
| Q012 | Cross-session knowledge mechanisms | ~ | ~ |
| Q021 | --parallel-agents flag | ~ | ~ |
| Q027 | April 23 default model change | ✓ | ✓ |
| Q032 | bypassPermissions exclusions | ~ | ~ |
| Q036 | CLI vs SDK hooks | ~ | ~ |
| Q049 | query() vs ClaudeSDKClient | ~ | ✓ |
| Q050 | When to choose ClaudeSDKClient | ✓ | ✓ |

Cell legend: ✓ correct, ~ partial, ✗ incorrect, H hallucinated, ?err judge_error.

## 6. Per-question deep dives

### Q005 — What is the 'opusplan' model alias and what are its specific limitations compared to a plain 'opus[1m]' setting?
*dimension: factual; difficulty: hard*

**bm25**: `correct` — The system answer correctly captures every point in the canonical answer: opusplan is a hybrid alias that uses Opus in plan mode and automatically switches to Sonnet for execution; the plan-mode Opus phase is capped at the standard 200K context window; and the automatic 1M upgrade that applies to the plain 'opus' setting does not extend to opusplan. No canonical claim is missing or contradicted. H...[truncated]

bm25 answer (first 300 chars):

```
# The `opusplan` Model Alias

## Definition

`opusplan` is a special model alias described in `model-config.md` (section "Model configuration > Available models > Model aliases") as a "Special mode that uses `opus` during plan mode, then switches to `sonnet` for execution."

The `model-config.md` se...[truncated]
```

**cli_agent**: `correct` — The system answer correctly and completely covers every point in the canonical answer: it accurately describes opusplan as a hybrid mode (opus for plan mode, sonnet for execution), correctly identifies the 200K context window limitation for the Opus planning phase, and correctly states that the automatic 1M upgrade for the 'opus' setting does not extend to 'opusplan'. No canonical points are missi...[truncated]

cli_agent answer (first 300 chars):

```
## `opusplan` model alias

From `model-config.md` § "Available models" (line 34) and § "`opusplan` model setting" (lines 145–157):

- **What it is**: A "Special mode that uses `opus` during plan mode, then switches to `sonnet` for execution."
  - **Plan mode** → uses `opus` for complex reasoning and...[truncated]
```

cli_agent telemetry: turns=5, tool_calls=4, cache_read=101,533, files_read=[model-config.md], cost=$0.31

### Q010 — The Bash permission rule 'Bash(ls *)' — does it match the command 'lsof'? Why or why not?
*dimension: citation; difficulty: hard*

**bm25**: `correct` — The system answer fully aligns with the canonical answer. It correctly states that 'Bash(ls *)' does not match 'lsof' because the space before '*' enforces a word boundary requiring the prefix to be followed by a space or end-of-string. It also correctly contrasts this with 'Bash(ls*)' (no space), which would match both 'ls -la' and 'lsof'. All major points from the canonical answer are present, a...[truncated]

bm25 answer (first 300 chars):

```
**No, `Bash(ls *)` does not match `lsof`.**

According to the documentation, the space before `*` enforces a word boundary, requiring the prefix to be followed by a space or end-of-string. Specifically:

> "When `*` appears at the end with a space before it (like `Bash(ls *)`), it enforces a word bo...[truncated]
```

**cli_agent**: `partially_correct` — The system answer correctly answers the core question (no match), correctly identifies the space-enforced word-boundary mechanism, and correctly notes the contrast with 'Bash(ls*)' matching both 'ls -la' and 'lsof' — covering every major point in the canonical answer. However, it invents specific source citations (a file path and two line numbers) not present in the canonical, and it introduces a...[truncated]

cli_agent answer (first 300 chars):

```
No, `Bash(ls *)` does **not** match `lsof`.

**Why:** The space before `*` enforces a word boundary, requiring the prefix `ls` to be followed by a space or end-of-string. Since `lsof` has no space after `ls`, it doesn't satisfy this boundary constraint.

By contrast, `Bash(ls*)` (no space) would mat...[truncated]
```

cli_agent telemetry: turns=3, tool_calls=2, cache_read=57,491, files_read=[], cost=$0.19

### Q012 — What are all the mechanisms for carrying knowledge or instructions across Claude Code sessions?
*dimension: coverage; difficulty: hard*

**bm25**: `partially_correct` — The system answer correctly identifies all five canonical mechanisms (CLAUDE.md files, auto memory, CLAUDE.local.md, .claude/rules/*.md, and Skills), and CLAUDE.local.md is correctly folded into the CLAUDE.md section as a local/gitignored variant. However, it misses the canonical's nuanced note about session transcripts (present but explicitly not cross-session knowledge injection), omits the auto...[truncated]

bm25 answer (first 300 chars):

```
# Mechanisms for Carrying Knowledge/Instructions Across Claude Code Sessions

According to `memory.md > How Claude remembers your project`, the documentation explicitly states: *"Each Claude Code session begins with a fresh context window. Two mechanisms carry knowledge across sessions"* — namely **...[truncated]
```

**cli_agent**: `partially_correct` — The system answer correctly identifies and elaborates on all five mechanisms the canonical answer treats as primary (CLAUDE.md files, auto memory, CLAUDE.local.md, .claude/rules/*.md, and Skills/SKILL.md), and its factual claims about those mechanisms are accurate and well-sourced. However, it omits the canonical's explicit note about session transcripts in ~/.claude/projects/ (even as a 'not stri...[truncated]

cli_agent answer (first 300 chars):

```
# Mechanisms for carrying knowledge or instructions across Claude Code sessions

The docs are explicit that there are **two primary mechanisms** for carrying knowledge across sessions, plus several related/secondary persistence mechanisms.

## The two primary mechanisms (from `memory.md`)

> "Each C...[truncated]
```

cli_agent telemetry: turns=18, tool_calls=17, cache_read=1,199,949, files_read=[checkpointing.md, claude-directory.md, features-overview.md, how-claude-code-works.md (+6)], cost=$1.22

### Q021 — What is the '--parallel-agents N' CLI flag used for in Claude Code, and what is the maximum value of N?
*dimension: hallucination_lure; difficulty: hard*

**bm25**: `partially_correct` — The system answer correctly identifies that no '--parallel-agents N' CLI flag exists in the documentation and correctly states it cannot find such a flag or a maximum value for it. This aligns with the canonical answer's main thrust. However, the system answer misses several important canonical points: that agent teams are created via natural language, that the --agents flag exists but serves a di...[truncated]

bm25 answer (first 300 chars):

```
Not found in the provided documentation.

The provided chunks do not mention a `--parallel-agents N` CLI flag. The closest related items I can find are:

- `CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY`, an environment variable that controls the "Maximum number of read-only tools and subagents that can exec...[truncated]
```

**cli_agent**: `partially_correct` — The system answer correctly identifies that --parallel-agents does not exist and correctly notes that --agents handles custom subagents via JSON (aligned with canonical). However, it frames its conclusion as merely 'not documented' rather than definitively non-existent, and it omits the canonical's key explanatory point that agent team creation is done through natural language rather than CLI flag...[truncated]

cli_agent answer (first 300 chars):

```
Not found in the provided documentation.

I searched the docs corpus (including `cli-reference.md`, which lists CLI flags from `--add-dir` to `--worktree`) and there is no `--parallel-agents` flag documented for Claude Code. The only related mention is in `glossary.md` § "Worktree isolation" (line 2...[truncated]
```

cli_agent telemetry: turns=9, tool_calls=8, cache_read=181,450, files_read=[cli-reference.md], cost=$0.34

### Q027 — What changed about the 'default' model behavior as of the docs, specifically for Enterprise pay-as-you-go and Anthropic API users on April 23, 2026?
*dimension: recency; difficulty: hard*

**bm25**: `correct` — The system answer covers every major point in the canonical answer: the April 23, 2026 date, the change to Opus 4.7, the affected user groups (Enterprise pay-as-you-go and Anthropic API), the prior default of Sonnet 4.6, and both opt-out mechanisms (ANTHROPIC_MODEL env var and the model field in server-managed settings). The additional context—tier table for other account types, caveats about non-...[truncated]

bm25 answer (first 300 chars):

```
According to the documentation, on April 23, 2026, the default model for **Enterprise pay-as-you-go and Anthropic API users** changed to **Opus 4.7**.

**Source:** `model-config.md` → "Special model behavior" → "`default` model setting" (also restated in the same file's main body at the top of the d...[truncated]
```

**cli_agent**: `correct` — The system answer fully covers all key points from the canonical answer: the date (April 23, 2026), the affected tiers (Enterprise pay-as-you-go and Anthropic API users), the change direction (from Sonnet 4.6 to Opus 4.7), and the mitigation options (ANTHROPIC_MODEL env var or the 'model' field in server-managed settings). The system answer also provides additional useful context (other tiers' def...[truncated]

cli_agent answer (first 300 chars):

```
## Answer

According to `data-claude/pages/model-config.md` (in the section "`default` model setting", under the Note callout at line 142):

> "On April 23, 2026, the default model for Enterprise pay-as-you-go and Anthropic API users will change to **Opus 4.7**. To keep a different default, set `ANT...[truncated]
```

cli_agent telemetry: turns=4, tool_calls=3, cache_read=97,758, files_read=[], cost=$0.24

**Recency / gold-phrase check** (Q027 expects 'April 23, 2026'): bm25 ctx_has_phrase=True, answer_has='April 23'=True; cli_agent ctx_has_phrase=True, answer_has='April 23'=True.

### Q032 — What tools and operations does 'bypassPermissions' mode NOT skip, and under what conditions would you still see a prompt?
*dimension: negation; difficulty: hard*

**bm25**: `partially_correct` — The system answer correctly and prominently covers the circuit-breaker prompt for rm -rf / and rm -rf ~ (the canonical's first and most critical point), but it entirely omits the canonical's third point about administrators disabling bypassPermissions mode via permissions.disableBypassPermissionsMode='disable' in managed settings. The canonical's second point — that writes to .git, .claude, .vscod...[truncated]

bm25 answer (first 300 chars):

```
# What `bypassPermissions` Does NOT Skip

According to the documentation, `bypassPermissions` mode "disables permission prompts and safety checks so tool calls execute immediately" (permission-modes.md > Skip all checks with bypassPermissions mode), but several layers still operate. Here's what is N...[truncated]
```

**cli_agent**: `partially_correct` — The system answer correctly identifies both main canonical prompting carve-outs — the root/home rm circuit breaker and the admin disableBypassPermissionsMode lockout — and attributes them accurately. However, the canonical's second key point (that writes to .git, .claude, .vscode, .idea, and .husky are currently skipped with no prompts, flagged as a security consideration) is only covered obliquel...[truncated]

cli_agent answer (first 300 chars):

```
## What `bypassPermissions` does NOT skip

Based on `permission-modes.md` (§ "Skip all checks with bypassPermissions mode", line 249) and `permissions.md` (line 42):

**Circuit-breaker prompts that still fire:**
- **Removals targeting the filesystem root or home directory**, such as `rm -rf /` and `...[truncated]
```

cli_agent telemetry: turns=6, tool_calls=5, cache_read=144,880, files_read=[permission-modes.md], cost=$0.33

### Q036 — How does hook configuration differ between Claude Code (the CLI tool) and the Agent SDK? Can SDK-built agents use hooks?
*dimension: cross_source; difficulty: hard*

**bm25**: `partially_correct` — The system answer correctly affirms that SDK agents support hooks and that there is a configuration difference between CLI and SDK, which aligns with the canonical's main thrust. However, it directly contradicts the canonical on a critical point: the canonical explicitly states SDK hooks are passed programmatically 'not through settings JSON files,' whereas the system answer asserts the SDK suppor...[truncated]

bm25 answer (first 300 chars):

```
# Hook configuration: Claude Code CLI vs. Agent SDK

## Can SDK-built agents use hooks?

**Yes.** The Agent SDK supports hooks as a first-class feature. Per `agent-sdk/overview.md > Capabilities` (Hooks tab): "Run custom code at key points in the agent lifecycle. SDK hooks use callback functions to...[truncated]
```

**cli_agent**: `partially_correct` — The system answer correctly identifies the two core architectural differences — CLI hooks live in JSON settings files at multiple scopes, SDK hooks are programmatic callbacks in ClaudeAgentOptions/Options — and correctly confirms SDK agents can use hooks and that both support PreToolUse/PostToolUse-style filtering. However, it omits the --bare flag point (a specific canonical fact), and more criti...[truncated]

cli_agent answer (first 300 chars):

```
## How hook configuration differs between Claude Code CLI and the Agent SDK

**Claude Code (CLI) — declarative, in JSON settings files**

Per `hooks.md` ("Configuration" / "Hook locations"), CLI hooks are user-defined **shell commands, HTTP endpoints, MCP tool calls, LLM prompts, or subagents** decl...[truncated]
```

cli_agent telemetry: turns=7, tool_calls=6, cache_read=222,287, files_read=[agent-sdk/hooks.md, hooks.md], cost=$0.52

### Q049 — How does the Python Agent SDK's query() function differ from ClaudeSDKClient for multi-turn conversations?
*dimension: paraphrase_pair; difficulty: hard*

**bm25**: `partially_correct` — The system answer correctly covers every major point in the canonical: query() creates a new session each time vs. ClaudeSDKClient maintaining context, the lack of interrupt support in query(), the shared support for hooks/custom tools/streaming, and the one-off vs. interactive use-case split. However, it then introduces specific flags (`continue_conversation=True`, `resume`) that allow query() to...[truncated]

bm25 answer (first 300 chars):

```
For multi-turn conversations in the Python Agent SDK, `query()` and `ClaudeSDKClient` differ along several dimensions:

## Session continuity

- **`query()`**: Creates a new session each time it is called, performing a single exchange (`agent-sdk/python.md > Choosing between query() and ClaudeSDKCli...[truncated]
```

**cli_agent**: `correct` — The system answer correctly and completely covers every point in the canonical answer: query() starts a fresh session each call with no history, ClaudeSDKClient reuses a session and maintains context, query() lacks interrupt support while ClaudeSDKClient has it, and both support hooks, custom tools, and streaming input, with the right use-case guidance for each. All canonical facts are accurately...[truncated]

cli_agent answer (first 300 chars):

```
# `query()` vs `ClaudeSDKClient` for multi-turn conversations

The Python Agent SDK exposes two primary entry points with **fundamentally different session semantics** for multi-turn use.

## Core difference: session continuity

Per `agent-sdk/python.md` § "Choosing between `query()` and `ClaudeSDKC...[truncated]
```

cli_agent telemetry: turns=10, tool_calls=9, cache_read=360,237, files_read=[agent-sdk/python.md, agent-sdk/streaming-vs-single-mode.md], cost=$0.46

**Hallucination canary check** (substrings from `INVENTED_SDK_METHODS`): bm25 → `none`; cli_agent → `none`.

### Q050 — In the Python Agent SDK, when would I choose ClaudeSDKClient instead of calling query() repeatedly?
*dimension: paraphrase_pair; difficulty: hard*

**bm25**: `correct` — The system answer correctly and fully covers every major point in the canonical answer: query() creates a fresh session each call with no retained history; ClaudeSDKClient reuses the same session and maintains conversation context across turns; query() does not support interrupts while ClaudeSDKClient does; query() is appropriate for one-off independent tasks; ClaudeSDKClient is appropriate for in...[truncated]

bm25 answer (first 300 chars):

```
# When to use `ClaudeSDKClient` vs repeated `query()` calls

Choose `ClaudeSDKClient` whenever you need follow-up turns to share context with prior turns or you need capabilities that `query()` does not support. Calling `query()` repeatedly creates a brand-new session each time, so the agent has no...[truncated]
```

**cli_agent**: `correct` — The system answer correctly and fully covers every point in the canonical answer: query() starts a fresh session each call with no history, ClaudeSDKClient reuses the session for conversation continuity, only ClaudeSDKClient supports interrupts, query() is for one-off/independent tasks while ClaudeSDKClient suits interactive apps and chatbots, and both share hooks/tools/streaming support. All crit...[truncated]

cli_agent answer (first 300 chars):

```
## When to choose `ClaudeSDKClient` over repeated `query()` calls

Based on `agent-sdk/python.md` ("Choosing between `query()` and `ClaudeSDKClient`") and `agent-sdk/streaming-vs-single-mode.md`, the docs treat this as a session/lifecycle question: each `query()` call **creates a new session each ti...[truncated]
```

cli_agent telemetry: turns=6, tool_calls=5, cache_read=241,229, files_read=[agent-sdk/python.md, agent-sdk/streaming-vs-single-mode.md], cost=$0.38

## 7. Cost & efficiency

| Metric | opus_bm25 | opus_cli_agent | Note |
|---|---:|---:|---|
| Strict correct | 4/9 | 4/9 | tied on this subset |
| Lenient (correct + partial) | 9/9 | 9/9 | also tied |
| Total $-cost | $4.33 | $3.98 | cli_agent is API-reported (cache discount); bm25 is token×price estimate |
| $-cost / correct answer | $1.08 | $1.00 | |
| Wall time @ concurrency=3 | 264.5s | 438.8s | bm25 ~1.7× faster |
| Avg input tokens / Q | 28,718 | 289,646 cache_read | different shapes — bm25 prompt size vs cli_agent total cached doc content |

Cost-efficiency on this 9-Q subset is essentially a wash — cli_agent's prompt-cache savings roughly offset its multi-turn token usage. The wall-time gap (1.7×) is the real cost of the agent loop.

## 8. Tool-use telemetry (cli_agent only)

Per-question agent activity. `cache_read` is the load-bearing column for the 1M-context claim — it shows how much doc content was held in the cached prompt across turns.

| QID | turns | tool_calls | cache_read | cost ($) | files_read |
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

**Aggregate**: avg turns/Q = 7.6, avg tool calls/Q = 6.6, total cache_read across the run = 2,606,814 tokens, total API-reported cost = $3.98. 7/9 questions used ≥5 turns. **Q012 alone read 1,199,949 cached tokens across 18 turns and 17 tool calls — direct evidence the 1M context window is exercised on this benchmark, despite the strict-correct tie with opus_bm25's single-call ~30K-token approach.**

## 9. Where they differ

Three questions split the variants. The judge reasoning lines are quoted (truncated to ~400 chars) directly from `scores.jsonl`.

**Q010 (bm25 wins ✓ vs cli_agent ~):** the cli_agent answer covers the core point (no match) but invents detail not in the canonical. Judge reasoning for cli_agent:

> The system answer correctly answers the core question (no match), correctly identifies the space-enforced word-boundary mechanism, and correctly notes the contrast with 'Bash(ls*)' matching both 'ls -la' and 'lsof' — covering every major point in the canonical answer. However, it invents specific source citations (a file path and two line numbers) not present in the canonical, and it introduces a novel claim about a 'Bash(ls:*)' colon-star variant being equivalent, which the canonical answer never mentions and which may be a hallucination. These additions tip the rating from 'correct' to 'part...[truncated]

Mechanism: cli_agent skipped Read on this question — only Grep tool calls — so its answer lacked file-grounded line numbers, then it fabricated some. bm25's answer stuck closer to the retrieved chunk text and avoided the invention.

**Q049 (cli_agent wins ✓ vs bm25 ~) — hallucination canary:** Q049 has historically tripped Sonnet 4.6 V2 trials into inventing SDK methods. Both Opus answers cleared the substring canary (no `.connect(`, `.disconnect(`, etc.). The judge marked cli_agent fully correct, bm25 partial. Judge reasoning for bm25:

> The system answer correctly covers every major point in the canonical: query() creates a new session each time vs. ClaudeSDKClient maintaining context, the lack of interrupt support in query(), the shared support for hooks/custom tools/streaming, and the one-off vs. interactive use-case split. However, it then introduces specific flags (`continue_conversation=True`, `resume`) that allow query() to persist context — a qualification the canonical explicitly excludes by stating 'each invocation starts fresh.' Whether these flags are real SDK features from the RAG corpus or invented, they material...[truncated]

Judge reasoning for cli_agent:

> The system answer correctly and completely covers every point in the canonical answer: query() starts a fresh session each call with no history, ClaudeSDKClient reuses a session and maintains context, query() lacks interrupt support while ClaudeSDKClient has it, and both support hooks, custom tools, and streaming input, with the right use-case guidance for each. All canonical facts are accurately reproduced. However, the system answer also introduces a substantial amount of additional detail — specific method signatures, documentation line numbers, a second multi-turn mechanism (continue_conve...[truncated]

**Q012 (judge_error in cli_agent, then re-scored):** cli_agent's Q012 answer is ~7K tokens (the longest in either run; see `wc -c baselines/outputs/opus_cli_agent/Q012.md`). The Sonnet 4.6 judge errored on the original scoring run — likely an output-token-budget or parse failure on the long answer. Step 1 of this report's plan re-runs only Q012 via `baselines/scripts/rescore_q012.py`. Even with the corrected verdict the strict tally between variants ties, so the measurement-artifact does not move the headline.

## 10. Conclusion / recommendation

On the 9-Q hard subset both Opus 4.7 variants land at 4/9 strict and 9/9 lenient. The 1M context capability of `claude-opus-4-7[1m]` is real and measurably exercised (opus_cli_agent's Q012 reads 1.2M cached tokens) but it does not move the strict score on this benchmark.

Pick by criterion:
- **Simpler / faster:** `opus_bm25` — one LLM call, ~30K context, 1.7× faster wall time.
- **Better hallucination resistance:** `opus_cli_agent` — wins Q049, zero invented SDK identifiers across the run.
- **Cost-efficient at scale:** Sonnet 4.6 + BM25 — out of scope for this report; the 9-system reference `baselines/opus_comparison.md` shows it at ~$0.80 per correct answer vs ~$1 here for either Opus path.

**Caveats**. (1) n=1 per variant on 9 questions; per-question oscillation ~33% in prior multi-trial runs. (2) Sonnet 4.6 is the judge for both Opus answers; some risk of undermarking sophisticated Opus phrasing. (3) The Q012 judge_error is a measurement artifact of long answers, not of variant quality — re-scoring resolves it.
