# Adversarial Review — Findings (run 20260504-rag-v4)

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
| partially_correct | 1 | 50.0% |
| incorrect | 1 | 50.0% |

### Citation alignment (per-citation judge)

| Verdict | n | % |
|---|---|---|
| supports | 7 | 58.3% |
| partial | 5 | 41.7% |

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

- **Q005** (factual) — INCORRECT
  - Q: What is the 'opusplan' model alias and what are its specific limitations compared to a plain 'opus[1m]' setting?
  - Judge: The system answer entirely fails to convey what opusplan is (a hybrid plan-mode/execution-mode alias) or its core limitation (plan-mode Opus is capped at 200K context, unlike opus[1m] which gets the full 1M window). Instead of answering, the system repeatedly disclaims insufficient evidence. Not a single substantive fact from the canonical answer is surfaced. The answer is not hallucinated—it inve
  - Wrong claims (canonical-vs-system):
    - The system claims the definition of opusplan and its limitations 'do not appear in the cached Anthropic documentation as of 2026-05-04', effectively asserting ignorance rather than supplying the answer the canonical clearly provides
    - Extensive detail about subscription-tier eligibility for 1M context (Max, Team, Enterprise, Pro, API) is irrelevant to the specific opusplan vs. opus[1m] comparison question
    - Repeated boilerplate statements that opusplan behavior 'does not appear in the cached documentation' are unhelpful filler that crowd out the actual answer

### S2 — Missing critical caveats / weak citations / hallucinated citation IDs

- **Q021** (hallucination_lure) — missing_points
  - Q: What is the '--parallel-agents N' CLI flag used for in Claude Code, and what is the maximum value of N?
    - missing: The canonical answer specifically notes that the '--agents' flag DOES exist (for defining custom subagents via JSON), but does not control parallelism count — the system answer omits this distinction entirely
    - missing: The canonical answer explicitly states that agent teams are created by telling Claude in natural language (not via a CLI flag) — the system answer only vaguely alludes to this

- **Q021** (hallucination_lure) — low_citation_alignment
  - Q: What is the '--parallel-agents N' CLI flag used for in Claude Code, and what is the maximum value of N?
    - alignment pass rate: 0.5
    - cite c819: partial — The chunk explicitly mentions 'parallel sessions' and scaling horizontally, supporting that part of the claim, but makes
    - cite c695: partial — The chunk directly confirms agent teams are experimental and involve multiple Claude Code instances working in parallel,
    - cite c695: partial — The chunk confirms agent teams are experimental and disabled by default, and names the `CLAUDE_CODE_EXPERIMENTAL_AGENT_T

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

- **synthesis_or_judgment**: 1 cases (Q005)
- **synthesis_incomplete_coverage**: 1 cases (Q021)
- **synthesis_picked_wrong_chunk**: 1 cases (Q021)
- **retrieval_gap**: 7 cases (Q003, Q036, Q041, Q042, Q043, Q044, Q045)

## How to reproduce any finding

Each scored question is reproducible from `answers.jsonl` row. To re-run ID `Q012`:

```bash
DOCS_MONITOR_EMBED_PROVIDER=ollama DOCS_MONITOR_EMBED_MODEL=nomic-embed-text \
  python claude_docs_monitor.py search "<question text from benchmark.jsonl>" --k 10 --json
```

For report runs, use `report` instead of `search` and refer to `--report-ids` flag in `runner.py`.
