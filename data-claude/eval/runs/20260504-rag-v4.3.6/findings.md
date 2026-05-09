# Adversarial Review — Findings (run 20260504-rag-v4.3.6)

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
| correct | 4 | 44.4% |
| partially_correct | 4 | 44.4% |
| incorrect | 1 | 11.1% |

### Citation alignment (per-citation judge)

| Verdict | n | % |
|---|---|---|
| supports | 27 | 50.0% |
| partial | 27 | 50.0% |

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

- **Q027** (recency) — INCORRECT
  - Q: What changed about the 'default' model behavior as of the docs, specifically for Enterprise pay-as-you-go and Anthropic API users on April 23, 2026?
  - Judge: The system answer does not hallucinate specific wrong facts but effectively delivers an incorrect answer by asserting the documented change 'does not appear in the cached Anthropic documentation,' which directly contradicts the canonical answer. All three key facts — the new default (Opus 4.7), the prior default (Sonnet 4.6), and the mitigation path (ANTHROPIC_MODEL or 'model' field) — are entirel
  - Wrong claims (canonical-vs-system):
    - Claims the April 23, 2026 change event 'does not appear in the cached Anthropic documentation' — this directly contradicts the canonical answer which clearly states the change occurred
    - Asserts 'no change event, changelog entry, or documentation diff is present in the evidence for this date and this account tier' — an incorrect absence claim that serves as a false negative answer to the question
    - Introduces irrelevant Bedrock and Vertex AI default model details as context, which are unrelated to the actual question about Enterprise pay-as-you-go and Anthropic API users

### S2 — Missing critical caveats / weak citations / hallucinated citation IDs

- **Q005** (factual) — low_citation_alignment
  - Q: What is the 'opusplan' model alias and what are its specific limitations compared to a plain 'opus[1m]' setting?
    - alignment pass rate: 0.5
    - cite c1922: partial — The chunk directly confirms opusplan's 200K cap and that the 1M upgrade applies to the `opus` model setting (not opuspla
    - cite c1912: partial — The chunk explicitly confirms that `opus[1m]` provides a 1 million token context window, but it contains no information 
    - cite c1912: partial — The chunk confirms that `opus[1m]` uses Opus with a 1M token context window for long sessions, but does not mention anyt

- **Q012** (coverage) — missing_points
  - Q: What are all the mechanisms for carrying knowledge or instructions across Claude Code sessions?
    - missing: CLAUDE.local.md — gitignored personal per-project instructions that load alongside CLAUDE.md (completely absent from system answer)
    - missing: .claude/rules/*.md — path-scoped rules that load only when Claude works with files matching the path pattern (not identified as a distinct mechanism)

- **Q012** (coverage) — low_citation_alignment
  - Q: What are all the mechanisms for carrying knowledge or instructions across Claude Code sessions?
    - alignment pass rate: 0.333
    - cite c1866: partial — The chunk directly supports the fresh-context-window claim and the human-authored (CLAUDE.md) vs. Claude-authored (auto 
    - cite c1867: partial — The chunk directly supports the claim about CLAUDE.md files (user-written instructions) and auto memory (Claude-written 
    - cite c1160: partial — The chunk directly supports the compaction survival and 5,000-token-per-skill cap claims, but does not address the asser

- **Q021** (hallucination_lure) — low_citation_alignment
  - Q: What is the '--parallel-agents N' CLI flag used for in Claude Code, and what is the maximum value of N?
    - alignment pass rate: 0.167
    - cite c3211: partial — The chunk confirms it is from `cli-reference.md` and covers CLI flags, which is consistent with the citation's source, b
    - cite c3246: partial — The chunk confirms that `--max-turns` is a documented CLI flag, supporting part of the sentence's claim about documented
    - cite c3616: partial — The chunk confirms the variable name, its purpose (concurrent execution of subagents and read-only tools), and the defau

- **Q027** (recency) — low_citation_alignment
  - Q: What changed about the 'default' model behavior as of the docs, specifically for Enterprise pay-as-you-go and Anthropic API users on April 23, 2026?
    - alignment pass rate: 0.5
    - cite c2690: partial — The chunk confirms that scheduled-tasks.md is indeed a new documentation page addition, supporting that part of the clai
    - cite c2692: partial — The chunk confirms that fullscreen.md is a new documentation page, supporting that aspect of the claim, but it does not 
    - cite c2693: partial — The chunk confirms that github-enterprise-server.md is a new documentation page added to the index, supporting that spec

- **Q036** (cross_source) — missing_points
  - Q: How does hook configuration differ between Claude Code (the CLI tool) and the Agent SDK? Can SDK-built agents use hooks?
    - missing: The --bare flag in the CLI explicitly skips hook discovery from settings files — this is not mentioned in the system answer
    - missing: The canonical explicitly characterizes SDK hooks as passed through ClaudeAgentOptions (Python) or Options (TypeScript) objects and *not* through settings JSON files, as a defining distinction — the system answer blurs this boundary

- **Q036** (cross_source) — low_citation_alignment
  - Q: How does hook configuration differ between Claude Code (the CLI tool) and the Agent SDK? Can SDK-built agents use hooks?
    - alignment pass rate: 0.167
    - cite c95: partial — The chunk confirms that hooks are callback functions registered in `options.hooks`, but it also explicitly mentions shel
    - cite c35: partial — The chunk confirms SDK agents inherit filesystem-based hooks via `settingSources` from the same CLI settings, but it doe
    - cite c1607: partial — The chunk explicitly names `PreToolUse`, `PostToolUse`, and `Stop` as hook events in Claude Code, confirming those event

- **Q049** (paraphrase_pair) — low_citation_alignment
  - Q: How does the Python Agent SDK's query() function differ from ClaudeSDKClient for multi-turn conversations?
    - alignment pass rate: 0.5
    - cite c255: partial — The chunk explicitly supports the core claims about automatic vs. manual connection management, session lifecycle (new v
    - cite c255: partial — The chunk confirms both interfaces support hooks and custom tools, and that persistent context (session/conversation con
    - cite c255: partial — The table confirms that `ClaudeSDKClient` reuses the same session and maintains conversation across calls, but it does n

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

- **synthesis_or_judgment**: 1 cases (Q027)
- **synthesis_picked_wrong_chunk**: 6 cases (Q005, Q012, Q021, Q027, Q036, Q049)
- **synthesis_incomplete_coverage**: 2 cases (Q012, Q036)
- **retrieval_gap**: 7 cases (Q003, Q036, Q041, Q042, Q043, Q044, Q045)

## How to reproduce any finding

Each scored question is reproducible from `answers.jsonl` row. To re-run ID `Q012`:

```bash
DOCS_MONITOR_EMBED_PROVIDER=ollama DOCS_MONITOR_EMBED_MODEL=nomic-embed-text \
  python claude_docs_monitor.py search "<question text from benchmark.jsonl>" --k 10 --json
```

For report runs, use `report` instead of `search` and refer to `--report-ids` flag in `runner.py`.
