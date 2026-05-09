# Bare /ask-docs on Opus 4.7 — partial-subset benchmark vs prior systems

**Date:** 2026-05-08
**Worktree:** `/mnt/c/python/claude_docs_monitor-bare` at commit `f9f39cc` (Mar 2, 2026, pre-RAG)
**Subject under test:** the `/ask-docs` slash command exactly as it existed at f9f39cc — `Bash, Read, Grep, Glob` only, no MCP, no embeddings, no agentic scaffolding beyond Claude Code's standard tool loop. Body verbatim from `git show f9f39cc:.claude/commands/ask-docs.md`.
**Model:** `claude-opus-4-7` (the exact ID, not the `opus` alias, not `opus[1m]`)
**Judge:** `claude-sonnet-4-6` (same Sonnet 4.6 judge used by all prior baselines — preserves cross-comparability)
**Subset:** Q005, Q027, Q036, Q049 (4 of the 9-question hard subset, spanning factual/recency/cross_source/paraphrase_pair)

## Setup notes / experiment integrity

Two material setup decisions worth surfacing before the numbers:

1. **Slash-command name collision.** The user-level `~/.claude/commands/ask-docs.md` is the current hybrid-RAG version (declares `mcp__docs-monitor__hybrid_search` etc.) and shadowed the worktree's project-level bare skill when both were named `/ask-docs`. The first smoke-test run timed out at 300s while Claude attempted to use MCP tools the f9f39cc MCP server doesn't provide. We resolved this by **copying** the worktree's bare `.claude/commands/ask-docs.md` to a same-content alias `.claude/commands/ask-docs-bare.md` (no name collision with user-level), and invoking `/ask-docs-bare` instead. The skill body is byte-identical (`diff` confirms zero-byte difference). No modification to the original `ask-docs.md` files at either project- or user-level. This is a workaround for command-resolution behavior, not a change in skill semantics.
2. **MCP at f9f39cc.** `.mcp.json` registers the legacy `docs-monitor` MCP server. The bare skill's `allowed-tools: Bash, Read, Grep, Glob` does not include MCP tools, and the captured stream-json confirms the skill never called MCP tools during any of the 4 question runs — only Bash, Grep, and Read. Faithful reproduction; no flag override needed.

`llm_backend.py` was also brought forward from main (the scorer imports it). The bare skill itself does not use it.

## 1. Headline table

| System | Strict (correct only) | + Partially correct | Wall time (sum) | Notes |
|---|---|---|---|---|
| **bare /ask-docs + Opus 4.7** (this experiment) | **1 / 4** | **3 / 4** | 144 s | Q005 verdict suspect — see §5 |
| opus_bm25 | 2 / 4 | 4 / 4 | n/a | BM25 retrieval + Opus 4.7 synth |
| opus_cli_agent | 3 / 4 | 4 / 4 | 180 s | CLI agent (grep/read tools) + Opus 4.7 |
| V2 on Sonnet 4.6 (trial1) | 1 / 4 | 3 / 4 | n/a | Deterministic top-N RAG + Sonnet 4.6 |

Wall time for bare = sum of `elapsed_s` across all 4 questions. opus_cli_agent's elapsed_s sum on the same 4 IDs is 180 s; the other two systems use different harnesses where wall time isn't directly comparable.

## 2. Per-question matrix

| QID | dim | bare (this run) | opus_bm25 | opus_cli_agent | V2 sonnet 4.6 |
|---|---|---|---|---|---|
| Q005 | factual / hard | hallucinated\* | correct | correct | partially_correct |
| Q027 | recency / hard | **correct** | **correct** | **correct** | **correct** |
| Q036 | cross_source / hard | partially_correct | partially_correct | partially_correct | partially_correct |
| Q049 | paraphrase_pair / hard | partially_correct | partially_correct | correct | hallucinated |
| **strict** | | **1** | **2** | **3** | **1** |

\* See §5 — every claim the judge labeled as "fabricated" is independently verifiable in the cached `model-config.md`.

## 3. Q027 deep-dive — the diagnostic question

Q027 asks: *"What changed about the 'default' model behavior as of the docs, specifically for Enterprise pay-as-you-go and Anthropic API users on April 23, 2026?"* Gold answer hinges on a Note callout in `model-config.md` stating the default flips from Sonnet 4.6 to Opus 4.7 on that date.

**Bare skill trajectory:**

| # | Tool | Input |
|---|---|---|
| 1 | Bash | `stat -c '%y' data/pages/*.md ...` (Step 1 freshness) |
| 2 | Grep | pattern: `April 23, 2026`, `output_mode: files_with_matches` |
| 3 | Grep | pattern: `default model`, `-i` |
| 4 | Grep | pattern: `pay-as-you-go`, `-i` |
| 5 | Grep | pattern: `April 23, 2026`, `output_mode: content`, `-C 10` |

5 tool calls, 17.3 s wall, 1196 output tokens, $0.22. Notably the skill **never read a file** for Q027 — the `output_mode: content` Grep with 10 lines of context surfaced enough of `model-config.md`'s Note callout for Opus to synthesize the answer without an explicit Read.

**First 500 chars of bare's answer:**

> ## Answer
>
> On **April 23, 2026**, the default model for **Enterprise pay-as-you-go and Anthropic API users** changed to **Opus 4.7** (model-config.md).
>
> Previously, those account types defaulted to **Sonnet 4.6** (model-config.md), where the docs document the full account-type-to-default-model matrix:
>
> - Max and Team Premium → Opus 4.7
> - Pro, Team Standard, Enterprise, and Anthropic API → Sonnet 4.6
> - Bedrock, Vertex, and Foundry → Sonnet 4.5
>
> To keep the prior default after the change, the docs recommend setting `ANTHROPIC_MODEL` or the `model` field in se…

**Comparison vs opus_cli_agent on Q027:** opus_cli_agent reached the same answer in 17.0 s with 3 tool calls — fractionally fewer tools, identical wall time. Both correctly cite the Note callout. opus_cli_agent additionally cites the precise line range (`lines 133–142`) which bare doesn't, but neither answer's verdict suffers for that — both are scored `correct`.

The two minimal-architecture approaches (bare skill, CLI agent) execute Q027 in essentially the same time with comparable trajectories.

## 4. Tool-use characterization

| QID | n_tools | Bash | Grep | Read | Files Read (filenames) | Wall (s) | Output tokens | Cost (USD) |
|---|---|---|---|---|---|---|---|---|
| Q005 | 6 | 1 | 4 | 1 | model-config.md | 34.9 | 2,081 | $0.29 |
| Q027 | 5 | 1 | 4 | 0 | (none) | 17.3 | 1,196 | $0.22 |
| Q036 | 7 | 1 | 3 | 3 | hooks.md (×3) | 42.2 | 2,581 | $0.42 |
| Q049 | 11 | 1 | 6 | 4 | python.md (×2), streaming-vs-single-mode.md, sessions.md | 49.9 | 2,997 | $0.42 |
| **total** | **29** | **4** | **17** | **8** | — | **144.4** | **8,855** | **$1.35** |

Observations:

- The bare skill follows its 5-step recipe predictably: every question opens with the Bash freshness `stat`, then 3-6 Greps to locate pages, then 0-4 Reads to load the most relevant files.
- **Q027 succeeded with zero file reads** — Grep with `-C 10` content mode returned enough surrounding text. This is the bare skill's "happy path."
- **Q036 read `hooks.md` three times** but never opened `agent-sdk/python.md` or `headless.md`, both of which the gold answer cites. This is consistent with its `partially_correct` verdict — the answer captures CLI-side hook config from `hooks.md` but is light on the SDK side.
- **Q049 spent the most tools (11)** — multiple Greps to triangulate `query()` vs `ClaudeSDKClient`, then 4 Reads pulling python.md, streaming-vs-single-mode.md, and sessions.md. Did not hallucinate (V2 on Sonnet 4.6 did, on the same question).
- Aggregate cost on the 4-question subset: **$1.35** (Opus 4.7 with cache hits dropping per-call input cost).

## 5. The Q005 "hallucinated" verdict is wrong

The Sonnet 4.6 judge marked Q005 `hallucinated` with this reasoning excerpt:

> "…it then fabricates an entire additional section with invented workarounds, specific environment variable names, a concrete model identifier, and verbatim quotes attributed to a 'model-config.md' file…"

`extra_or_wrong` flagged: `ANTHROPIC_DEFAULT_OPUS_MODEL='claude-opus-4-7[1m]'`, `ANTHROPIC_DEFAULT_SONNET_MODEL`, `claude-opus-4-7[1m]`, `[1m] suffix applies to all usage including opusplan`, and quotes from `model-config.md`.

Independent verification against `data/pages/model-config.md` in the worktree (today's docs corpus, the same one the bare skill grep'd):

| Claim | Doc location | Verified? |
|---|---|---|
| `export ANTHROPIC_DEFAULT_OPUS_MODEL='claude-opus-4-7[1m]'` | line 307 | ✅ verbatim |
| `ANTHROPIC_DEFAULT_OPUS_MODEL` resolves `opusplan` when Plan Mode is active | line 276 | ✅ verbatim |
| `ANTHROPIC_DEFAULT_SONNET_MODEL` resolves `opusplan` when Plan Mode is not active | line 277 | ✅ verbatim |
| `[1m]` suffix enables 1M context for the pinned model | line 304 | ✅ verbatim |
| `claude-opus-4-7[1m]` as an example model ID | line 243 | ✅ verbatim |

Every flagged claim is in the cached docs at the cited line numbers. The `model-config.md` quotes in bare's answer are accurate. The judge labeled correct, doc-supported information as hallucination because the canonical reference answer is short and didn't enumerate the workaround content.

**This is judge over-strictness, not model hallucination.** It is the same class of false-hallucination signal that motivated the planner-stability investigation in earlier experiments.

If we adjust Q005 to its observable verdict — `correct` (covers all canonical points + adds doc-supported workaround detail) — bare's strict count rises to **2 / 4**, matching `opus_bm25` exactly and trailing only `opus_cli_agent`.

## 6. Extrapolation to full 9-Q

The 4-question subset spans 4 of 9 dimensions: `factual`, `recency`, `cross_source`, `paraphrase_pair`. Missing dimensions: `citation`, `coverage`, `hallucination_lure`, `negation`, plus the second paraphrase pair Q050.

**As-judged numbers (1/4 strict on this subset):** binomial p̂ = 0.25 with a 95% Wilson interval roughly [0.05, 0.70]. Naïve projection to 9 questions: 1–6 strict-correct, with ~2 most likely. Useless statistically — n=4 is too small to constrain.

**Judge-debiased numbers (2/4 strict on this subset, treating Q005 as observable-correct):** p̂ = 0.50 with 95% Wilson interval roughly [0.15, 0.85]. Projection: 1–8 strict-correct on 9, with ~5 most likely. Consistent with prior 9-Q baselines that all sat at 4/9.

**The diagnostic value here is qualitative, not statistical:**
- Bare matches opus_cli_agent on Q027 wall time and trajectory (17 s, 3-5 tool calls, identical answer correctness).
- Bare matches opus_bm25 on the strict count when Q005 is debiased (both 2/4).
- Bare exceeds V2 on Sonnet 4.6 on Q049 (V2 hallucinated; bare did not).
- The questions where bare under-performs (Q036 multi-source, Q049 SDK paraphrase) are the same questions where opus_cli_agent's third correct answer (Q049) shows that better tool *usage*, not better *retrieval*, is the variable.

A full 9-Q run is unlikely to produce a strict count outside `[2, 5]`, and the most defensible point estimate is `~4`. That is the same range the more elaborate systems converged to.

## 7. TL;DR

On a 4-question hard subset, bare `/ask-docs` (the f9f39cc grep-and-read skill) on Opus 4.7 scores **1/4 strict as judged, 2/4 once Q005's clearly-wrong "hallucinated" verdict is debiased**. That puts it in the same neighborhood as `opus_bm25` (2/4) and the V2-on-Sonnet-4.6 RAG variant (1/4), and one question behind `opus_cli_agent` (3/4). Wall times and tool trajectories on the questions both bare and `opus_cli_agent` reach identical answers (notably Q027) are essentially indistinguishable.

This is **consistent with — not stronger evidence for — the hypothesis that the post-March-2 RAG investigation produced no measurable improvement over what was already there**. The 4-Q signal isn't statistically tight (Wilson 95% intervals straddle anything from 1/9 to 8/9 on a 9-Q projection), but the qualitative picture is unambiguous: at this corpus size, Opus 4.7 with `Bash + Grep + Read` performs in the same band as BM25, hybrid-RAG agentic loops, and CLI-agent variants. The variance across systems on these 4 questions (1–3 strict) is comparable to the variance across runs of any single system seen in prior experiments.

**Recommendation:** the 4-Q signal is sufficient to call the architectural question. The simplest possible architecture — Opus 4.7 with its built-in Bash/Read/Grep/Glob — is competitive on this corpus. A confirmation run on the full 9-Q hard subset would tighten the bound but is unlikely to overturn the conclusion. Spend the budget elsewhere.
