# Adversarial Review — Findings (run 20260503T013441Z-postfix-v2)

Brutal-honesty audit of RAG answer quality across 8 dimensions. Generated from 50 scored questions, 5 probes, no UX track.

## Headline metrics

### Retrieval recall@10 by dimension

| Dimension | n | mean recall@10 |
|---|---|---|
| citation | 5 | 1.0 |
| coverage | 5 | 0.717 |
| cross_source | 5 | 0.7 |
| factual | 6 | 0.917 |
| negation | 6 | 0.75 |
| paraphrase_pair | 10 | 0.658 |
| recency | 5 | 1.0 |

### Factual correctness (report subset)

| Verdict | n | % |
|---|---|---|
| correct | 2 | 22.2% |
| partially_correct | 7 | 77.8% |

### Citation alignment (per-citation judge)

| Verdict | n | % |
|---|---|---|
| supports | 30 | 55.6% |
| partial | 24 | 44.4% |

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
| P2_multi_hop_retrieval | PARTIAL | 1/3 found all expected pages |
| P4_stale_data_retrieval | PASS | 4/4 surfaced changed page in top-3 |
| P_chunk_existence | PASS | all cited chunks exist |
| P_paraphrase_stability | FAIL | 1/5 pairs stable (jaccard>=0.5) |

### Paraphrase pair stability (benchmark Q041-Q050)

| pair | chunk Jaccard | page Jaccard | status | A | B |
|---|---|---|---|---|---|
| Q041+Q042 | 0.176 | 0.182 | unstable | 'How do I restrict which tools Claude can use in a session?' | "How do I limit Claude's tool access in a Claude Code session?" |
| Q043+Q044 | 0.429 | 0.667 | weak | 'What mechanism does Claude Code use to prevent context from growing too large du' | 'How does Claude Code avoid running out of context window during extended coding ' |
| Q045+Q046 | 0.0 | 0.0 | unstable | 'How do I make Claude Code run non-interactively in a CI pipeline?' | 'What is the correct way to use Claude Code in a GitHub Actions workflow without ' |
| Q047+Q048 | 0.333 | 0.429 | unstable | 'Where does Claude Code store credentials on Linux?' | "What file stores Claude Code's login tokens on a Linux machine?" |
| Q049+Q050 | 0.667 | 0.5 | stable | "How does the Python Agent SDK's query() function differ from ClaudeSDKClient for" | 'In the Python Agent SDK, when would I choose ClaudeSDKClient instead of calling ' |

**3/5 pairs are UNSTABLE** (chunk Jaccard < 0.5 AND page Jaccard < 0.5).
Real-world implication: the same question phrased two natural ways gives the synthesizer different evidence; answers can diverge.

## Severity-ranked findings

### S1 — Factually wrong cited claims

_None found in scored set._

### S2 — Missing critical caveats / weak citations / hallucinated citation IDs

- **Q012** (coverage) — missing_points
  - Q: What are all the mechanisms for carrying knowledge or instructions across Claude Code sessions?
    - missing: CLAUDE.local.md — the gitignored personal per-project instruction file loaded alongside CLAUDE.md (a distinct, separately named mechanism in the canonical answer)
    - missing: Session transcripts stored in ~/.claude/projects/ — the canonical answer explicitly names these and clarifies they enable conversation resumption but are not cross-session knowledge injection per se

- **Q012** (coverage) — low_citation_alignment
  - Q: What are all the mechanisms for carrying knowledge or instructions across Claude Code sessions?
    - alignment pass rate: 0.333
    - cite c1866: partial — The chunk supports the two primary memory systems (CLAUDE.md as human-written and auto memory as Claude-written), but ma
    - cite c1495: partial — The chunk supports the 'Claude-written counterpart,' per-repository storage, and the 200-lines/25 KB loading limit, but 
    - cite c1536: partial — The chunk fully confirms the five-layer hierarchy and its precedence order, but does not mention tool allow/deny lists, 

- **Q021** (hallucination_lure) — missing_points
  - Q: What is the '--parallel-agents N' CLI flag used for in Claude Code, and what is the maximum value of N?
    - missing: The canonical answer specifically notes that '--agents' flag DOES exist (for defining custom subagents via JSON), but it does not control parallelism count — this distinction is absent from the system answer
    - missing: The canonical answer explicitly states that agent teams are created by telling Claude to create a team in natural language, not via a CLI flag — the system answer only implies this indirectly

- **Q021** (hallucination_lure) — low_citation_alignment
  - Q: What is the '--parallel-agents N' CLI flag used for in Claude Code, and what is the maximum value of N?
    - alignment pass rate: 0.333
    - cite c3211: partial — The chunk confirms this is the CLI flags section of the documentation but does not show the actual flags table content, 
    - cite c3246: partial — The chunk shows only one row of the CLI flags table (`--max-turns`) and does not include `--parallel-agents N`, which is
    - cite c3246: partial — The chunk confirms that `--max-turns` appears in the CLI flags table, but it only shows a single row excerpt, so it cann

- **Q036** (cross_source) — missing_points
  - Q: How does hook configuration differ between Claude Code (the CLI tool) and the Agent SDK? Can SDK-built agents use hooks?
    - missing: The --bare flag explicitly skips hook discovery in the CLI, which is a notable cross-mode behavioral difference
    - missing: Canonical explicitly states SDK hooks are passed 'not through settings JSON files' — the distinction that SDK configuration is purely programmatic is a key point

- **Q036** (cross_source) — low_citation_alignment
  - Q: How does hook configuration differ between Claude Code (the CLI tool) and the Agent SDK? Can SDK-built agents use hooks?
    - alignment pass rate: 0.333
    - cite c1608: partial — The chunk confirms that CLI hooks are 'shell commands, HTTP endpoints, or LLM prompts,' supporting that part of the clai
    - cite c96: partial — The chunk confirms that SDK hooks are callback functions responding to agent events, which partially supports the 'in-pr
    - cite c1514: partial — The chunk confirms that a matcher filters which events fire and a handler (Hook handler) is what runs, supporting that p

- **Q049** (paraphrase_pair) — low_citation_alignment
  - Q: How does the Python Agent SDK's query() function differ from ClaudeSDKClient for multi-turn conversations?
    - alignment pass rate: 0.0
    - cite c268: partial — The chunk directly supports the claims about `query()` creating a new session on every invocation with no memory of prev
    - cite c277: partial — The chunk fully supports the claim about `ClaudeSDKClient` maintaining a persistent session across multiple `query()` ca
    - cite c255: partial — The chunk confirms that `query()` creates a new session each time and `ClaudeSDKClient` reuses/maintains sessions, but i

- **Q050** (paraphrase_pair) — low_citation_alignment
  - Q: In the Python Agent SDK, when would I choose ClaudeSDKClient instead of calling query() repeatedly?
    - alignment pass rate: 0.5
    - cite c257: partial — The chunk confirms that `query()` handles a 'Single exchange' while `ClaudeSDKClient` supports 'Multiple exchanges in sa
    - cite c260: partial — The chunk confirms that interrupts are not supported by query() and are supported by ClaudeSDKClient, but does not speci
    - cite c2835: partial — The chunk explicitly shows `ClaudeSDKClient` has an `.interrupt()` method that halts a task without ending the session, 

### S3 — Retrieval recall failures (recall@10 < 0.5)

- **Q011** (coverage) — recall@10 = 0.25
  - Q: What are all the ways Claude Code can authenticate to Anthropic's API or a provider, covering both individual users and enterprise teams?
  - missing pages: ['amazon-bedrock.md', 'google-vertex-ai.md', 'microsoft-foundry.md']

- **Q014** (coverage) — recall@10 = 0.333
  - Q: What are at least three distinct ways to reduce token usage and costs in Claude Code?
  - missing pages: ['best-practices.md', 'headless.md']

- **Q032** (negation) — recall@10 = 0.0
  - Q: What tools and operations does 'bypassPermissions' mode NOT skip, and under what conditions would you still see a prompt?
  - missing pages: ['permissions.md']

- **Q036** (cross_source) — recall@10 = 0.0
  - Q: How does hook configuration differ between Claude Code (the CLI tool) and the Agent SDK? Can SDK-built agents use hooks?
  - missing pages: ['agent-sdk/python.md', 'headless.md', 'hooks.md']

- **Q041** (paraphrase_pair) — recall@10 = 0.333
  - Q: How do I restrict which tools Claude can use in a session?
  - missing pages: ['cli-reference.md', 'sub-agents.md']

- **Q042** (paraphrase_pair) — recall@10 = 0.333
  - Q: How do I limit Claude's tool access in a Claude Code session?
  - missing pages: ['cli-reference.md', 'sub-agents.md']

- **Q045** (paraphrase_pair) — recall@10 = 0.333
  - Q: How do I make Claude Code run non-interactively in a CI pipeline?
  - missing pages: ['authentication.md', 'cli-reference.md']

- **Q046** (paraphrase_pair) — recall@10 = 0.25
  - Q: What is the correct way to use Claude Code in a GitHub Actions workflow without interactive prompts?
  - missing pages: ['authentication.md', 'cli-reference.md', 'headless.md']

### S4 — UX friction (from new-hire pass)

_UX track not run or output missing._

## Root-cause attribution summary

This is a heuristic mapping from observed failure → likely cause. Use as starting point, not final diagnosis.

- **synthesis_incomplete_coverage**: 3 cases (Q012, Q021, Q036)
- **synthesis_picked_wrong_chunk**: 5 cases (Q012, Q021, Q036, Q049, Q050)
- **retrieval_gap**: 8 cases (Q011, Q014, Q032, Q036, Q041, Q042, Q045, Q046)

## How to reproduce any finding

Each scored question is reproducible from `answers.jsonl` row. To re-run ID `Q012`:

```bash
DOCS_MONITOR_EMBED_PROVIDER=ollama DOCS_MONITOR_EMBED_MODEL=nomic-embed-text \
  python claude_docs_monitor.py search "<question text from benchmark.jsonl>" --k 10 --json
```

For report runs, use `report` instead of `search` and refer to `--report-ids` flag in `runner.py`.
