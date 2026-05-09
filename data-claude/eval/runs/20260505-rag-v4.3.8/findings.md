# Adversarial Review — Findings (run 20260505-rag-v4.3.8)

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
| correct | 2 | 25.0% |
| partially_correct | 6 | 75.0% |

### Citation alignment (per-citation judge)

| Verdict | n | % |
|---|---|---|
| supports | 22 | 45.8% |
| partial | 24 | 50.0% |
| contradicts | 1 | 2.1% |
| unrelated | 1 | 2.1% |

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

- **Q012** (coverage) — CONTRADICTING_CITATION
  - Q: What are all the mechanisms for carrying knowledge or instructions across Claude Code sessions?
  - Judge: 1 citations cite chunks that explicitly contradict the surrounding sentence
  - Cite c1536: '**Settings files form a four-layer hierarchy** (managed → user → project → local) that persists tool permissions, hooks, MCP configuration, and behavi'
    - judge: The chunk shows the precedence order (highest to lowest) as managed → CLI args → local → project → user, meaning local overrides project which overrides user—the opposite of the sentence's 'managed → user → project → local' ordering; additionally, the chunk describes at least five layers (including 
  - Wrong claims (canonical-vs-system):
    - Auto memory referred to as 'MEMORY.md' — the canonical never names it MEMORY.md; this specific filename appears to be hallucinated or invented
    - Local scope in the CLAUDE.md table is described as controlled by '.claude/settings.local.json' — this conflates a settings file with CLAUDE.local.md, which is factually incorrect per canonical
    - Settings files (four-layer hierarchy) listed as a mechanism for carrying knowledge/instructions across sessions — canonical does not include settings files in this category

### S2 — Missing critical caveats / weak citations / hallucinated citation IDs

- **Q005** (factual) — low_citation_alignment
  - Q: What is the 'opusplan' model alias and what are its specific limitations compared to a plain 'opus[1m]' setting?
    - alignment pass rate: 0.5
    - cite c1913: partial — The chunk confirms opusplan is a model alias that uses opus during plan mode and switches to sonnet for execution, but i
    - cite c1912: partial — The chunk confirms that `opus[1m]` uses Opus with a 1 million token context window, supporting only the final comparativ
    - cite c4177: partial — The chunk confirms that `/model opus[1m]` works as a syntax and that Opus 4.7 and Opus 4.6 support 1M context, but it al

- **Q012** (coverage) — missing_points
  - Q: What are all the mechanisms for carrying knowledge or instructions across Claude Code sessions?
    - missing: CLAUDE.local.md as a distinct, gitignored personal per-project instructions file loaded alongside CLAUDE.md — the canonical treats this as its own mechanism (#3); the system answer conflates 'local scope' with `.claude/settings.local.json` instead
    - missing: .claude/rules/*.md described in canonical as path-scoped rules that load only when Claude works with matching files/paths — system answer mentions rules files but characterizes them only as scoping to 'specific file types', losing the path-matching nuance

- **Q021** (hallucination_lure) — missing_points
  - Q: What is the '--parallel-agents N' CLI flag used for in Claude Code, and what is the maximum value of N?
    - missing: The canonical explicitly notes that '--agents' (not '--parallel-agents') does exist as a CLI flag, and its purpose is to define custom subagents via JSON — the system answer only mentions '--agent' in passing without explaining what it actually does
    - missing: The canonical specifically clarifies that the existing '--agents' flag does NOT control parallelism/concurrency count — the system answer omits this important disambiguation

- **Q021** (hallucination_lure) — low_citation_alignment
  - Q: What is the '--parallel-agents N' CLI flag used for in Claude Code, and what is the maximum value of N?
    - alignment pass rate: 0.333
    - cite c3211: partial — The chunk confirms this is the CLI flags section of the reference where such a flag would appear, and the flag is absent
    - cite c3269: partial — The chunk is from the relevant CLI flags section and notably does not contain `--parallel-agents N`, which is consistent
    - cite c708: partial — The chunk shows that agent count is controlled via natural language prompts, implying no CLI flag is used, but it never 

- **Q032** (negation) — missing_points
  - Q: What tools and operations does 'bypassPermissions' mode NOT skip, and under what conditions would you still see a prompt?
    - missing: The canonical explicitly names the specific protected paths (.git, .claude, .vscode, .idea, .husky) whose writes are skipped (no prompts) even in other modes, framing this as a security consideration — the system answer references 'protected paths' abstractly without naming them.
    - missing: The canonical frames the skipping of writes to those protected paths as a notable *security consideration*, not merely a capability description — the system answer omits this framing.

- **Q032** (negation) — low_citation_alignment
  - Q: What tools and operations does 'bypassPermissions' mode NOT skip, and under what conditions would you still see a prompt?
    - alignment pass rate: 0.167
    - cite c4265: partial — The chunk directly supports the claim about bypassPermissions eliminating most prompts and the circuit-breaker for files
    - cite c3863: partial — The chunk directly supports the claim that `PreToolUse` hooks returning deny survive `bypassPermissions` mode, but it do
    - cite c226: partial — The chunk confirms that deny rules and hooks can block tools even in bypassPermissions mode, but it makes no mention of 

- **Q036** (cross_source) — missing_points
  - Q: How does hook configuration differ between Claude Code (the CLI tool) and the Agent SDK? Can SDK-built agents use hooks?
    - missing: The --bare flag explicitly skips hook discovery in the CLI (important canonical distinction)
    - missing: SDK hooks are specifically configured via ClaudeAgentOptions (Python) or Options (TypeScript) objects — the system answer describes hooks passed to query() instead

- **Q036** (cross_source) — low_citation_alignment
  - Q: How does hook configuration differ between Claude Code (the CLI tool) and the Agent SDK? Can SDK-built agents use hooks?
    - alignment pass rate: 0.167
    - cite c1608: partial — The chunk explicitly supports that hooks are 'shell commands, HTTP endpoints, or LLM prompts,' but does not directly men
    - cite c95: partial — The chunk confirms SDK hooks are callback functions registered via options (passed programmatically to query()) and that
    - cite c332: partial — The chunk explicitly confirms that Python SDK has fewer hook events than TypeScript SDK, but it contains no information 

- **Q049** (paraphrase_pair) — low_citation_alignment
  - Q: How does the Python Agent SDK's query() function differ from ClaudeSDKClient for multi-turn conversations?
    - alignment pass rate: 0.5
    - cite c263: partial — The chunk's table row directly confirms the core conversation-continuity distinction (query() = new session each time, C
    - cite c422: partial — The chunk explicitly supports the claims about `ClaudeSDKClient` tracking session IDs internally and each `client.query(
    - cite c277: partial — The chunk clearly supports that `ClaudeSDKClient` maintains session continuity and retains previous message context acro

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

- **synthesis_or_judgment**: 1 cases (Q012)
- **synthesis_picked_wrong_chunk**: 5 cases (Q005, Q021, Q032, Q036, Q049)
- **synthesis_incomplete_coverage**: 4 cases (Q012, Q021, Q032, Q036)
- **retrieval_gap**: 7 cases (Q003, Q036, Q041, Q042, Q043, Q044, Q045)

## How to reproduce any finding

Each scored question is reproducible from `answers.jsonl` row. To re-run ID `Q012`:

```bash
DOCS_MONITOR_EMBED_PROVIDER=ollama DOCS_MONITOR_EMBED_MODEL=nomic-embed-text \
  python claude_docs_monitor.py search "<question text from benchmark.jsonl>" --k 10 --json
```

For report runs, use `report` instead of `search` and refer to `--report-ids` flag in `runner.py`.
