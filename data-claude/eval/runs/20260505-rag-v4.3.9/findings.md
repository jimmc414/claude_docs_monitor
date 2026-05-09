# Adversarial Review — Findings (run 20260505-rag-v4.3.9)

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
| supports | 23 | 42.6% |
| partial | 31 | 57.4% |

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
  - Judge: The system answer's central finding — that no April 23, 2026 default-model change event appears in its evidence — directly contradicts the canonical answer, which asserts that on that date the default for Enterprise pay-as-you-go and Anthropic API users changed from Sonnet 4.6 to Opus 4.7. The system answer omits every substantive fact in the canonical answer: the new default model (Opus 4.7), the
  - Wrong claims (canonical-vs-system):
    - Claims 'No change event dated April 23, 2026 appears in the cached Anthropic documentation evidence' — directly contradicts the canonical answer which states such a change did occur
    - Presents four unrelated March 2026 documentation-page additions as the only change_event evidence, implying the April 23 event does not exist rather than that the RAG system simply failed to retrieve it

### S2 — Missing critical caveats / weak citations / hallucinated citation IDs

- **Q005** (factual) — low_citation_alignment
  - Q: What is the 'opusplan' model alias and what are its specific limitations compared to a plain 'opus[1m]' setting?
    - alignment pass rate: 0.5
    - cite c1913: partial — The chunk confirms that `opusplan` uses `opus` during plan mode and switches to `sonnet` for execution, but does not men
    - cite c1922: partial — The chunk directly supports all claims about opusplan's hybrid routing behavior and its 200K context ceiling, but it doe
    - cite c1913: partial — The chunk supports that opusplan uses opus in plan mode and switches to sonnet for execution, but the chunk does not use

- **Q012** (coverage) — missing_points
  - Q: What are all the mechanisms for carrying knowledge or instructions across Claude Code sessions?
    - missing: CLAUDE.local.md — gitignored personal per-project instructions loaded alongside CLAUDE.md — is entirely absent from the system answer as a named, distinct mechanism
    - missing: .claude/rules/*.md path-scoped rules are only briefly mentioned as a way to keep root CLAUDE.md concise, not described as a distinct cross-session mechanism that loads only when Claude works with matching files

- **Q012** (coverage) — low_citation_alignment
  - Q: What are all the mechanisms for carrying knowledge or instructions across Claude Code sessions?
    - alignment pass rate: 0.5
    - cite c806: partial — The chunk explicitly confirms that hooks are 'deterministic,' directly supporting that one element of the sentence, but 
    - cite c2364: partial — The chunk supports the 'on-demand skills' element (explicitly stating a skill's body loads only when used), but does not
    - cite c818: partial — The chunk directly supports the 'resumable session transcripts' component by describing `--continue`/`--resume` flags an

- **Q021** (hallucination_lure) — low_citation_alignment
  - Q: What is the '--parallel-agents N' CLI flag used for in Claude Code, and what is the maximum value of N?
    - alignment pass rate: 0.5
    - cite c821: partial — The chunk confirms three of the four parallel mechanisms cited (desktop app, web, agent teams) but does not mention the 
    - cite c695: partial — The chunk confirms that Agent Teams are experimental and enable parallel work across multiple Claude Code instances, but
    - cite c708: partial — The chunk confirms that teammate count can be specified via conversational prompt (e.g., 'Create a team with 4 teammates

- **Q027** (recency) — low_citation_alignment
  - Q: What changed about the 'default' model behavior as of the docs, specifically for Enterprise pay-as-you-go and Anthropic API users on April 23, 2026?
    - alignment pass rate: 0.333
    - cite c1905: partial — The chunk confirms that Bedrock, Vertex, and Foundry resolve aliases to earlier versions (e.g., Opus 4.6, Sonnet 4.5 vs.
    - cite c2690: partial — The chunk confirms it is about a new documentation page being added (consistent with the claim's characterization of chu
    - cite c2691: partial — The chunk confirms that at least one retrieved change_event is about a new documentation page (not a default-model chang

- **Q032** (negation) — low_citation_alignment
  - Q: What tools and operations does 'bypassPermissions' mode NOT skip, and under what conditions would you still see a prompt?
    - alignment pass rate: 0.0
    - cite c4265: partial — The chunk explicitly supports the claims about disabling permission prompts, immediate tool execution, protected-path wr
    - cite c2019: partial — The chunk confirms that bypassPermissions skips all permission prompts and retains a circuit breaker for root/home-direc
    - cite c227: partial — The chunk explicitly confirms that `disallowed_tools` holds unconditionally in every permission mode including `bypassPe

- **Q036** (cross_source) — missing_points
  - Q: How does hook configuration differ between Claude Code (the CLI tool) and the Agent SDK? Can SDK-built agents use hooks?
    - missing: The --bare flag (bare mode) explicitly skips hook discovery in the CLI — this specific behavioral detail is absent from the system answer
    - missing: CLI hooks fire based on settings files discovered from the working directory and ~/.claude — the directory-discovery mechanism is not clearly articulated

- **Q036** (cross_source) — low_citation_alignment
  - Q: How does hook configuration differ between Claude Code (the CLI tool) and the Agent SDK? Can SDK-built agents use hooks?
    - alignment pass rate: 0.333
    - cite c1608: partial — The chunk confirms CLI hooks execute as shell commands, HTTP endpoints, or LLM prompts, supporting that part of the clai
    - cite c95: partial — The chunk confirms that Agent SDK hooks are in-process callback functions passed programmatically via `options.hooks` at
    - cite c1578: partial — The chunk confirms CLI hooks live in settings.json as JSON with a 'command' type handler, but it neither mentions 'http'

- **Q049** (paraphrase_pair) — low_citation_alignment
  - Q: How does the Python Agent SDK's query() function differ from ClaudeSDKClient for multi-turn conversations?
    - alignment pass rate: 0.333
    - cite c251: partial — The chunk explicitly supports that `query()` creates a new session each time and has automatically managed connections, 
    - cite c257: partial — The chunk confirms the core distinction (single exchange vs. multiple exchanges in same context), supporting the isolate
    - cite c422: partial — The chunk explicitly confirms that `ClaudeSDKClient` must be used as an async context manager, but it never mentions exp

- **Q050** (paraphrase_pair) — low_citation_alignment
  - Q: In the Python Agent SDK, when would I choose ClaudeSDKClient instead of calling query() repeatedly?
    - alignment pass rate: 0.333
    - cite c256: partial — The chunk directly confirms that `query()` creates a new session each time and `ClaudeSDKClient` reuses the same session
    - cite c257: partial — The chunk confirms the single-exchange vs. multiple-exchanges distinction between `query()` and `ClaudeSDKClient`, but d
    - cite c251: partial — The chunk directly confirms that `query()` creates a new session each time and `ClaudeSDKClient` reuses the same session

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
- **synthesis_picked_wrong_chunk**: 8 cases (Q005, Q012, Q021, Q027, Q032, Q036, Q049, Q050)
- **synthesis_incomplete_coverage**: 2 cases (Q012, Q036)
- **retrieval_gap**: 7 cases (Q003, Q036, Q041, Q042, Q043, Q044, Q045)

## How to reproduce any finding

Each scored question is reproducible from `answers.jsonl` row. To re-run ID `Q012`:

```bash
DOCS_MONITOR_EMBED_PROVIDER=ollama DOCS_MONITOR_EMBED_MODEL=nomic-embed-text \
  python claude_docs_monitor.py search "<question text from benchmark.jsonl>" --k 10 --json
```

For report runs, use `report` instead of `search` and refer to `--report-ids` flag in `runner.py`.
