# Adversarial Review — Findings (run 20260505-rag-v4.3.7)

Brutal-honesty audit of RAG answer quality across 8 dimensions. Generated from 50 scored questions, 5 probes, no UX track.

## Headline metrics

### Retrieval recall@10 by dimension

| Dimension | n | mean recall@10 |
|---|---|---|
| citation | 5 | 1.0 |
| coverage | 5 | 0.733 |
| cross_source | 5 | 0.8 |
| factual | 6 | 0.75 |
| negation | 6 | 0.917 |
| paraphrase_pair | 10 | 0.583 |
| recency | 5 | 0.9 |

### Factual correctness (report subset)

| Verdict | n | % |
|---|---|---|
| correct | 3 | 33.3% |
| partially_correct | 5 | 55.6% |
| incorrect | 1 | 11.1% |

### Citation alignment (per-citation judge)

| Verdict | n | % |
|---|---|---|
| supports | 24 | 44.4% |
| partial | 29 | 53.7% |
| contradicts | 1 | 1.9% |

### Hallucination resistance (lures)

- Lures with full report run: **1** (of 8 total lures)
- Correctly refused (said 'doesn't exist'): **1/1**
- Invented an answer instead: **0/1**
- _Note: search-only retrieval cannot diagnose hallucination — needs synthesis layer; 7 lures only had search runs and are unmeasured here._

## Benchmark-quality meta-findings (caught before scoring)

- P-BMK-1 (S2): Q018 is not a valid lure — `CLAUDE_CODE_MAX_CONTEXT_TOKENS` IS documented
- P-BMK-2 (S3): Q024 mis-classified as lure — answer IS in the docs (as a negation)
- Why this matters
- Adjusted dimension counts after patch

See `eval/benchmark_patches.md` for full reproduction details.

## Adversarial probes

| Probe | Verdict | Notes |
|---|---|---|
| P1_filter_leakage | PASS | 0 of 5 queries leaked |
| P2_multi_hop_retrieval | PARTIAL | 2/3 found all expected pages |
| P4_stale_data_retrieval | PASS | 4/4 surfaced changed page in top-3 |
| P_chunk_existence | PASS | all cited chunks exist |
| P_paraphrase_stability | FAIL | 1/5 pairs stable (jaccard>=0.5) |

### Paraphrase pair stability (benchmark Q041-Q050)

| pair | chunk Jaccard | page Jaccard | status | A | B |
|---|---|---|---|---|---|
| Q041+Q042 | 0.333 | 0.5 | weak | 'How do I restrict which tools Claude can use in a session?' | "How do I limit Claude's tool access in a Claude Code session?" |
| Q043+Q044 | 0.25 | 0.417 | unstable | 'What mechanism does Claude Code use to prevent context from growing too large du' | 'How does Claude Code avoid running out of context window during extended coding ' |
| Q045+Q046 | 0.333 | 1.0 | weak | 'How do I make Claude Code run non-interactively in a CI pipeline?' | 'What is the correct way to use Claude Code in a GitHub Actions workflow without ' |
| Q047+Q048 | 0.333 | 0.545 | weak | 'Where does Claude Code store credentials on Linux?' | "What file stores Claude Code's login tokens on a Linux machine?" |
| Q049+Q050 | 0.25 | 0.429 | unstable | "How does the Python Agent SDK's query() function differ from ClaudeSDKClient for" | 'In the Python Agent SDK, when would I choose ClaudeSDKClient instead of calling ' |

**2/5 pairs are UNSTABLE** (chunk Jaccard < 0.5 AND page Jaccard < 0.5).
Real-world implication: the same question phrased two natural ways gives the synthesizer different evidence; answers can diverge.

## Severity-ranked findings

### S1 — Factually wrong cited claims

- **Q021** (hallucination_lure) — CONTRADICTING_CITATION
  - Q: What is the '--parallel-agents N' CLI flag used for in Claude Code, and what is the maximum value of N?
  - Judge: 1 citations cite chunks that explicitly contradict the surrounding sentence
  - Cite c3211: 'Because this flag is absent from the documented CLI surface—including the complete CLI reference page'
    - judge: The chunk explicitly states that `claude --help` does not list every flag, directly undermining the sentence's characterization of the CLI reference page as 'complete' and its implication that absence from that surface is meaningful evidence.
  - Wrong claims (canonical-vs-system):
    - The system answer introduces '--teammate-mode' as a documented CLI flag for multi-session coordination — this specific flag is not mentioned in the canonical answer and may be hallucinated.
    - The system answer cites 'CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY' defaulting to 10 as the closest documented integer bound for parallelism — this specific detail is not in the canonical answer and is unsupported by it.
    - The system answer cites 'CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS' environment variable — not mentioned in the canonical answer.

- **Q027** (recency) — INCORRECT
  - Q: What changed about the 'default' model behavior as of the docs, specifically for Enterprise pay-as-you-go and Anthropic API users on April 23, 2026?
  - Judge: The system answer's central assertion is that no documentation of the April 23, 2026 default-model change exists, which directly contradicts the canonical answer. All three key facts from the canonical answer — the switch to Opus 4.7, the prior default of Sonnet 4.6, and the mitigation options (ANTHROPIC_MODEL or server-managed 'model' field) — are entirely absent. Rather than being partially corr
  - Wrong claims (canonical-vs-system):
    - Claims the April 23, 2026 change 'does not appear in the cached Anthropic documentation' and is 'absent from the evidence' — directly contradicting the canonical answer which documents this change explicitly
    - Extended table of model aliases (best, opus[1m], sonnet[1m], opusplan) and discussion of third-party cloud deployments (Bedrock, Vertex AI, Foundry) are tangential and not supported by the canonical answer

### S2 — Missing critical caveats / weak citations / hallucinated citation IDs

- **Q005** (factual) — low_citation_alignment
  - Q: What is the 'opusplan' model alias and what are its specific limitations compared to a plain 'opus[1m]' setting?
    - alignment pass rate: 0.5
    - cite c1922: partial — The chunk directly supports the 200K restriction on opusplan's Opus phase and its exclusion from the 1M upgrade, and con
    - cite c1913: partial — The chunk confirms opusplan switches between opus (plan mode) and sonnet (execution), but does not support the claim tha
    - cite c1912: partial — The chunk confirms that opus[1m] uses Opus with a 1 million token context window for long sessions, but does not mention

- **Q012** (coverage) — missing_points
  - Q: What are all the mechanisms for carrying knowledge or instructions across Claude Code sessions?
    - missing: CLAUDE.local.md — gitignored personal per-project instructions loaded alongside CLAUDE.md (entirely absent from system answer)
    - missing: .claude/rules/*.md as a distinct named mechanism with path-scoped rules that load only when Claude works with matching files (mentioned only in passing inside the CLAUDE.md section, not treated as a separate mechanism)

- **Q012** (coverage) — low_citation_alignment
  - Q: What are all the mechanisms for carrying knowledge or instructions across Claude Code sessions?
    - alignment pass rate: 0.5
    - cite c1866: partial — The chunk directly confirms sessions start with a fresh context window, but specifies exactly 'Two mechanisms' rather th
    - cite c1160: partial — The chunk directly supports the 'run as code, not context' quote about hooks surviving compaction, but it says nothing a
    - cite c1325: partial — The chunk confirms that settings.json can carry environment variables across sessions, but it does not address the claim

- **Q021** (hallucination_lure) — low_citation_alignment
  - Q: What is the '--parallel-agents N' CLI flag used for in Claude Code, and what is the maximum value of N?
    - alignment pass rate: 0.333
    - cite c3269: partial — The chunk does contain a CLI flags table, which supports that claim, but the sentence is incomplete and provides no spec
    - cite c1035: partial — The chunk confirms this is the CLI reference page and shows some CLI commands/flags, but it only displays a truncated po
    - cite c3211: contradicts — The chunk explicitly states that `claude --help` does not list every flag, directly undermining the sentence's character

- **Q027** (recency) — low_citation_alignment
  - Q: What changed about the 'default' model behavior as of the docs, specifically for Enterprise pay-as-you-go and Anthropic API users on April 23, 2026?
    - alignment pass rate: 0.5
    - cite c1902: partial — The chunk directly supports the quoted phrase about `default` clearing overrides and reverting to the recommended model 
    - cite c2728: partial — The chunk confirms that the default model depends on authentication method and subscription, but it does not mention `de
    - cite c1557: partial — The chunk explicitly supports pinning for Vertex AI deployments to control when users move to a new model, but the sente

- **Q036** (cross_source) — missing_points
  - Q: How does hook configuration differ between Claude Code (the CLI tool) and the Agent SDK? Can SDK-built agents use hooks?
    - missing: The --bare flag explicitly skips hook discovery in the CLI, which is an important behavioral difference not mentioned in the system answer
    - missing: SDK hooks are passed specifically through the ClaudeAgentOptions (Python) or Options (TypeScript) named option objects — the system answer references a generic 'hooks field in agent options' without naming these classes
    - missing: The canonical explicitly contrasts CLI hooks as 'not through settings JSON files' for SDK agents, but the system answer muddies this by claiming SDK agents can load settings.json hooks via settingSources/setting_sources, contradicting or at least complicating the canonical's framing
    - missing: CLI hooks fire based on settings files discovered from the working directory and ~/.claude — the system answer mentions ~/.claude/settings.json but does not explain the discovery mechanism

- **Q036** (cross_source) — low_citation_alignment
  - Q: How does hook configuration differ between Claude Code (the CLI tool) and the Agent SDK? Can SDK-built agents use hooks?
    - alignment pass rate: 0.0
    - cite c1609: partial — The chunk confirms that `SubagentStart`/`SubagentStop` and `PostToolBatch` are real events in Claude Code's hook system,
    - cite c1608: partial — The chunk confirms that CLI hooks are 'user-defined shell commands, HTTP endpoints, or LLM prompts,' supporting that par
    - cite c95: partial — The chunk confirms that SDK hooks are programmatic callback functions and briefly mentions shell command hooks from sett

- **Q049** (paraphrase_pair) — low_citation_alignment
  - Q: How does the Python Agent SDK's query() function differ from ClaudeSDKClient for multi-turn conversations?
    - alignment pass rate: 0.0
    - cite c254: partial — The chunk confirms there are two interaction patterns named `query()` and `ClaudeSDKClient`, but it does not explicitly 
    - cite c420: partial — The chunk directly supports the existence and behavior of the three mechanisms (continue, resume, fork) and that 'contin
    - cite c413: partial — The chunk confirms `query()` for one-shot tasks, `ClaudeSDKClient` for multi-turn, and the existence of `continue`, `res

- **Q050** (paraphrase_pair) — low_citation_alignment
  - Q: In the Python Agent SDK, when would I choose ClaudeSDKClient instead of calling query() repeatedly?
    - alignment pass rate: 0.5
    - cite c266: partial — The chunk directly supports the recommended use cases for `ClaudeSDKClient` (follow-up questions, chat interfaces, conte
    - cite c251: partial — The chunk explicitly confirms that `query()` creates a new session each time and `ClaudeSDKClient` reuses the same sessi
    - cite c422: partial — The chunk explicitly confirms that ClaudeSDKClient handles session IDs internally and continues the same session across 

### S3 — Retrieval recall failures (recall@10 < 0.5)

- **Q003** (factual) — recall@10 = 0.0
  - Q: What are the five permission modes available in Claude Code and what does each do?
  - missing pages: ['permissions.md']

- **Q036** (cross_source) — recall@10 = 0.333
  - Q: How does hook configuration differ between Claude Code (the CLI tool) and the Agent SDK? Can SDK-built agents use hooks?
  - missing pages: ['headless.md', 'hooks.md']

- **Q041** (paraphrase_pair) — recall@10 = 0.333
  - Q: How do I restrict which tools Claude can use in a session?
  - missing pages: ['cli-reference.md', 'sub-agents.md']

- **Q042** (paraphrase_pair) — recall@10 = 0.333
  - Q: How do I limit Claude's tool access in a Claude Code session?
  - missing pages: ['cli-reference.md', 'sub-agents.md']

- **Q043** (paraphrase_pair) — recall@10 = 0.333
  - Q: What mechanism does Claude Code use to prevent context from growing too large during a long session?
  - missing pages: ['best-practices.md', 'checkpointing.md']

- **Q044** (paraphrase_pair) — recall@10 = 0.0
  - Q: How does Claude Code avoid running out of context window during extended coding sessions?
  - missing pages: ['best-practices.md', 'checkpointing.md', 'costs.md']

- **Q045** (paraphrase_pair) — recall@10 = 0.333
  - Q: How do I make Claude Code run non-interactively in a CI pipeline?
  - missing pages: ['authentication.md', 'cli-reference.md']

### S4 — UX friction (from new-hire pass)

_UX track not run or output missing._

## Root-cause attribution summary

This is a heuristic mapping from observed failure → likely cause. Use as starting point, not final diagnosis.

- **synthesis_or_judgment**: 2 cases (Q021, Q027)
- **synthesis_picked_wrong_chunk**: 7 cases (Q005, Q012, Q021, Q027, Q036, Q049, Q050)
- **synthesis_incomplete_coverage**: 2 cases (Q012, Q036)
- **retrieval_gap**: 7 cases (Q003, Q036, Q041, Q042, Q043, Q044, Q045)

## How to reproduce any finding

Each scored question is reproducible from `answers.jsonl` row. To re-run ID `Q012`:

```bash
DOCS_MONITOR_EMBED_PROVIDER=ollama DOCS_MONITOR_EMBED_MODEL=nomic-embed-text \
  python claude_docs_monitor.py search "<question text from benchmark.jsonl>" --k 10 --json
```

For report runs, use `report` instead of `search` and refer to `--report-ids` flag in `runner.py`.
