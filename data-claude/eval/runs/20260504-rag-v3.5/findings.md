# Adversarial Review — Findings (run 20260504-rag-v3.5)

Brutal-honesty audit of RAG answer quality across 8 dimensions. Generated from 50 scored questions, 5 probes, no UX track.

## Headline metrics

### Retrieval recall@10 by dimension

| Dimension | n | mean recall@10 |
|---|---|---|
| citation | 5 | 1.0 |
| coverage | 5 | 0.667 |
| cross_source | 5 | 0.8 |
| factual | 6 | 0.917 |
| negation | 6 | 0.833 |
| paraphrase_pair | 10 | 0.65 |
| recency | 5 | 0.9 |

### Factual correctness (report subset)

| Verdict | n | % |
|---|---|---|
| correct | 5 | 55.6% |
| partially_correct | 4 | 44.4% |

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
| Q041+Q042 | 0.25 | 0.75 | weak | 'How do I restrict which tools Claude can use in a session?' | "How do I limit Claude's tool access in a Claude Code session?" |
| Q043+Q044 | 0.25 | 0.364 | unstable | 'What mechanism does Claude Code use to prevent context from growing too large du' | 'How does Claude Code avoid running out of context window during extended coding ' |
| Q045+Q046 | 0.111 | 0.4 | unstable | 'How do I make Claude Code run non-interactively in a CI pipeline?' | 'What is the correct way to use Claude Code in a GitHub Actions workflow without ' |
| Q047+Q048 | 0.429 | 0.333 | unstable | 'Where does Claude Code store credentials on Linux?' | "What file stores Claude Code's login tokens on a Linux machine?" |
| Q049+Q050 | 0.429 | 0.667 | weak | "How does the Python Agent SDK's query() function differ from ClaudeSDKClient for" | 'In the Python Agent SDK, when would I choose ClaudeSDKClient instead of calling ' |

**3/5 pairs are UNSTABLE** (chunk Jaccard < 0.5 AND page Jaccard < 0.5).
Real-world implication: the same question phrased two natural ways gives the synthesizer different evidence; answers can diverge.

## Severity-ranked findings

### S1 — Factually wrong cited claims

_None found in scored set._

### S2 — Missing critical caveats / weak citations / hallucinated citation IDs

- **Q005** (factual) — low_citation_alignment
  - Q: What is the 'opusplan' model alias and what are its specific limitations compared to a plain 'opus[1m]' setting?
    - alignment pass rate: 0.5
    - cite c1922: partial — The chunk directly confirms both the 200K context window claim and that the 1M upgrade does not extend to `opusplan`, bu
    - cite c1912: partial — The chunk confirms that opus[1m] uses Opus with a 1M-token context window for long sessions, but does not explicitly sta
    - cite c1905: partial — The chunk confirms `opus[1m]` uses Opus with a 1M-token context window for long sessions, but never explicitly states th

- **Q012** (coverage) — missing_points
  - Q: What are all the mechanisms for carrying knowledge or instructions across Claude Code sessions?
    - missing: CLAUDE.local.md — a gitignored personal per-project instructions file loaded alongside CLAUDE.md is completely absent from the system answer
    - missing: .claude/rules/*.md is only briefly mentioned in passing under the CLAUDE.md section rather than being identified as a distinct, separately triggered mechanism (path-scoped, loads only when matching files are involved)

- **Q012** (coverage) — low_citation_alignment
  - Q: What are all the mechanisms for carrying knowledge or instructions across Claude Code sessions?
    - alignment pass rate: 0.5
    - cite c1536: partial — The chunk confirms a managed→local→project→user precedence order, but it actually lists five layers (including command-l
    - cite c1609: partial — The chunk directly supports the lifecycle cadences claim (session, per-turn, per tool call), but says nothing about hook
    - cite c1867: partial — The chunk confirms subagents can maintain their own auto memory, but does not explicitly state that this knowledge 'pers

- **Q021** (hallucination_lure) — low_citation_alignment
  - Q: What is the '--parallel-agents N' CLI flag used for in Claude Code, and what is the maximum value of N?
    - alignment pass rate: 0.5
    - cite c3212: partial — The chunk shows the CLI reference table where `--parallel-agents` is indeed absent, supporting that specific claim, but 
    - cite c3269: partial — The chunk directly confirms the flag name, its display-control function, and the three option values (auto, in-process, 
    - cite c3212: partial — The chunk confirms a CLI flags table exists in `cli-reference.md` and shows flags relevant to agents (`--agent`, `--agen

- **Q036** (cross_source) — missing_points
  - Q: How does hook configuration differ between Claude Code (the CLI tool) and the Agent SDK? Can SDK-built agents use hooks?
    - missing: The --bare flag explicitly skips hook discovery in CLI mode — not mentioned at all in the system answer
    - missing: SDK hooks are specifically passed through ClaudeAgentOptions (Python) or Options (TypeScript) objects — the system answer vaguely says 'passed programmatically to query()' which differs from the canonical
    - missing: CLI hook scopes include local, managed, and plugin in addition to user and project — system answer only mentions user and project

- **Q036** (cross_source) — low_citation_alignment
  - Q: How does hook configuration differ between Claude Code (the CLI tool) and the Agent SDK? Can SDK-built agents use hooks?
    - alignment pass rate: 0.5
    - cite c1609: partial — The chunk confirms the lifecycle events (PreToolUse, PostToolUse, Stop, Notification) and mentions JSON on stdin for com
    - cite c95: partial — The chunk confirms SDK hooks are callback functions and mentions PreToolUse/PostToolUse events, but does not mention Sto
    - cite c2760: partial — The chunk explains that settingSources controls which filesystem hooks/settings are loaded (e.g., ["project"] loads .cla

- **Q049** (paraphrase_pair) — low_citation_alignment
  - Q: How does the Python Agent SDK's query() function differ from ClaudeSDKClient for multi-turn conversations?
    - alignment pass rate: 0.167
    - cite c255: partial — The chunk directly supports the core session-behavior claims (query() creates a new session each time, ClaudeSDKClient r
    - cite c268: partial — The chunk directly supports the claims about `query()` being stateless and creating a new session on each call, but cont
    - cite c255: partial — The chunk's comparison table directly supports the session behavior, multi-turn vs. one-shot use cases, and the shared/e

- **Q050** (paraphrase_pair) — low_citation_alignment
  - Q: In the Python Agent SDK, when would I choose ClaudeSDKClient instead of calling query() repeatedly?
    - alignment pass rate: 0.333
    - cite c255: partial — The chunk explicitly supports the interrupt claim (query() ❌, ClaudeSDKClient ✅), but 'explicit lifecycle management' is
    - cite c277: partial — The chunk explicitly lists 'Interrupt support' and 'Explicit lifecycle' as key features of `ClaudeSDKClient`, supporting
    - cite c268: partial — The chunk explicitly supports the claim about `query()` starting fresh with no memory, but contains no information about

### S3 — Retrieval recall failures (recall@10 < 0.5)

- **Q014** (coverage) — recall@10 = 0.333
  - Q: What are at least three distinct ways to reduce token usage and costs in Claude Code?
  - missing pages: ['best-practices.md', 'headless.md']

- **Q036** (cross_source) — recall@10 = 0.0
  - Q: How does hook configuration differ between Claude Code (the CLI tool) and the Agent SDK? Can SDK-built agents use hooks?
  - missing pages: ['agent-sdk/python.md', 'headless.md', 'hooks.md']

- **Q041** (paraphrase_pair) — recall@10 = 0.333
  - Q: How do I restrict which tools Claude can use in a session?
  - missing pages: ['cli-reference.md', 'sub-agents.md']

- **Q042** (paraphrase_pair) — recall@10 = 0.333
  - Q: How do I limit Claude's tool access in a Claude Code session?
  - missing pages: ['cli-reference.md', 'sub-agents.md']

- **Q044** (paraphrase_pair) — recall@10 = 0.333
  - Q: How does Claude Code avoid running out of context window during extended coding sessions?
  - missing pages: ['checkpointing.md', 'costs.md']

- **Q045** (paraphrase_pair) — recall@10 = 0.333
  - Q: How do I make Claude Code run non-interactively in a CI pipeline?
  - missing pages: ['authentication.md', 'cli-reference.md']

### S4 — UX friction (from new-hire pass)

_UX track not run or output missing._

## Root-cause attribution summary

This is a heuristic mapping from observed failure → likely cause. Use as starting point, not final diagnosis.

- **synthesis_picked_wrong_chunk**: 6 cases (Q005, Q012, Q021, Q036, Q049, Q050)
- **synthesis_incomplete_coverage**: 2 cases (Q012, Q036)
- **retrieval_gap**: 6 cases (Q014, Q036, Q041, Q042, Q044, Q045)

## How to reproduce any finding

Each scored question is reproducible from `answers.jsonl` row. To re-run ID `Q012`:

```bash
DOCS_MONITOR_EMBED_PROVIDER=ollama DOCS_MONITOR_EMBED_MODEL=nomic-embed-text \
  python claude_docs_monitor.py search "<question text from benchmark.jsonl>" --k 10 --json
```

For report runs, use `report` instead of `search` and refer to `--report-ids` flag in `runner.py`.
