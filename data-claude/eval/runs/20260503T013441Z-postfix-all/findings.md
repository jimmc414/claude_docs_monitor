# Adversarial Review — Findings (run 20260503T013441Z-postfix-all)

Brutal-honesty audit of RAG answer quality across 8 dimensions. Generated from 50 scored questions, 5 probes, no UX track.

## Headline metrics

### Retrieval recall@10 by dimension

| Dimension | n | mean recall@10 |
|---|---|---|
| citation | 5 | 1.0 |
| coverage | 5 | 0.717 |
| cross_source | 5 | 0.7 |
| factual | 6 | 0.833 |
| negation | 6 | 0.667 |
| paraphrase_pair | 10 | 0.658 |
| recency | 5 | 0.6 |

### Factual correctness (report subset)

| Verdict | n | % |
|---|---|---|
| correct | 4 | 44.4% |
| partially_correct | 5 | 55.6% |

### Citation alignment (per-citation judge)

| Verdict | n | % |
|---|---|---|
| supports | 28 | 51.9% |
| partial | 24 | 44.4% |
| contradicts | 1 | 1.9% |
| unrelated | 1 | 1.9% |

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
| P2_multi_hop_retrieval | PARTIAL | 0/3 found all expected pages |
| P4_stale_data_retrieval | PASS | 4/4 surfaced changed page in top-3 |
| P_chunk_existence | PASS | all cited chunks exist |
| P_paraphrase_stability | FAIL | 1/5 pairs stable (jaccard>=0.5) |

### Paraphrase pair stability (benchmark Q041-Q050)

| pair | chunk Jaccard | page Jaccard | status | A | B |
|---|---|---|---|---|---|
| Q041+Q042 | 0.176 | 0.2 | unstable | 'How do I restrict which tools Claude can use in a session?' | "How do I limit Claude's tool access in a Claude Code session?" |
| Q043+Q044 | 0.25 | 0.444 | unstable | 'What mechanism does Claude Code use to prevent context from growing too large du' | 'How does Claude Code avoid running out of context window during extended coding ' |
| Q045+Q046 | 0.053 | 0.167 | unstable | 'How do I make Claude Code run non-interactively in a CI pipeline?' | 'What is the correct way to use Claude Code in a GitHub Actions workflow without ' |
| Q047+Q048 | 0.429 | 0.5 | weak | 'Where does Claude Code store credentials on Linux?' | "What file stores Claude Code's login tokens on a Linux machine?" |
| Q049+Q050 | 0.667 | 1.0 | stable | "How does the Python Agent SDK's query() function differ from ClaudeSDKClient for" | 'In the Python Agent SDK, when would I choose ClaudeSDKClient instead of calling ' |

**3/5 pairs are UNSTABLE** (chunk Jaccard < 0.5 AND page Jaccard < 0.5).
Real-world implication: the same question phrased two natural ways gives the synthesizer different evidence; answers can diverge.

## Severity-ranked findings

### S1 — Factually wrong cited claims

- **Q036** (cross_source) — CONTRADICTING_CITATION
  - Q: How does hook configuration differ between Claude Code (the CLI tool) and the Agent SDK? Can SDK-built agents use hooks?
  - Judge: 1 citations cite chunks that explicitly contradict the surrounding sentence
  - Cite c1641: 'Agent SDK hooks are callback functions passed via `options.hooks` at runtime in Python or TypeScript.'
    - judge: The chunk states hooks are defined in JSON settings files (a configuration-time, file-based mechanism), directly contradicting the sentence's claim that hooks are callback functions passed via `options.hooks` at runtime in Python or TypeScript.
  - Wrong claims (canonical-vs-system):
    - Claim that SDK agents can simultaneously inherit shell-command hooks from settings.json files alongside programmatic callbacks contradicts the canonical, which states SDK hooks are configured 'not through settings JSON files'
    - TypeScript SDK having a superset of events (PostToolBatch, SessionStart, Setup) not in Python or CLI is not mentioned in canonical and may be hallucinated
    - Claim that SDK hooks 'consume no tokens' and run 'outside the context window' is not in the canonical and is an unsupported invention

### S2 — Missing critical caveats / weak citations / hallucinated citation IDs

- **Q005** (factual) — low_citation_alignment
  - Q: What is the 'opusplan' model alias and what are its specific limitations compared to a plain 'opus[1m]' setting?
    - alignment pass rate: 0.5
    - cite c1912: partial — The chunk confirms that `opus[1m]` uses a 1 million token context window, supporting that specific detail, but it says n
    - cite c1912: partial — The chunk confirms `opus[1m]` uses Opus (consistent with the 'single, consistent Opus session' claim) but only describes
    - cite c4177: partial — The chunk confirms that plain `opus[1m]` uses 1M context and that Max/Team/Enterprise plans include 1M for Opus automati

- **Q012** (coverage) — low_citation_alignment
  - Q: What are all the mechanisms for carrying knowledge or instructions across Claude Code sessions?
    - alignment pass rate: 0.5
    - cite c1694: partial — The chunk confirms sessions start with a fresh context window, but only mentions two persistence mechanisms (auto memory
    - cite c1866: partial — The chunk supports the fresh-context-window claim and the descriptions of CLAUDE.md and auto memory as the two primary m
    - cite c1160: partial — The chunk confirms CLAUDE.md, auto memory, hooks, and skills as persistence mechanisms but never mentions 'settings file

- **Q021** (hallucination_lure) — missing_points
  - Q: What is the '--parallel-agents N' CLI flag used for in Claude Code, and what is the maximum value of N?
    - missing: The canonical explicitly notes that the '--agents' flag does exist (for defining custom subagents via JSON), but does not control parallelism count — the system answer omits this distinction entirely
    - missing: The canonical states that agent teams are created by telling Claude to create a team in natural language, not via a CLI flag — the system answer does not mention natural-language team creation as the actual mechanism

- **Q021** (hallucination_lure) — low_citation_alignment
  - Q: What is the '--parallel-agents N' CLI flag used for in Claude Code, and what is the maximum value of N?
    - alignment pass rate: 0.5
    - cite c491: partial — The chunk confirms that multiple subagents can run concurrently (supporting the subagent parallelism claim), but does no
    - cite c3246: partial — The chunk confirms that `--max-turns` appears in the CLI flags table, but it only shows one row and does not provide evi
    - cite c1035: partial — The chunk confirms this is the cli-reference.md file and shows the `-p` flag in the commands table, but it only displays

- **Q032** (negation) — low_citation_alignment
  - Q: What tools and operations does 'bypassPermissions' mode NOT skip, and under what conditions would you still see a prompt?
    - alignment pass rate: 0.0
    - cite c4265: partial — The chunk directly supports claims #1 (filesystem-root/home-directory circuit-breaker) and part of claim #3 (admins can 
    - cite c226: partial — The chunk directly supports the claim about deny rules in settings files and hooks overriding permission modes (includin
    - cite c3863: partial — The chunk directly supports the claim about `PreToolUse` hooks with a `deny` decision overriding any permission mode (in

- **Q036** (cross_source) — missing_points
  - Q: How does hook configuration differ between Claude Code (the CLI tool) and the Agent SDK? Can SDK-built agents use hooks?
    - missing: The --bare flag explicitly skips hook discovery in CLI mode
    - missing: SDK hooks are specifically passed through ClaudeAgentOptions (Python) or Options (TypeScript) named objects
    - missing: CLI hooks fire based on settings files discovered from the working directory and ~/.claude (discovery mechanism detail)

- **Q036** (cross_source) — low_citation_alignment
  - Q: How does hook configuration differ between Claude Code (the CLI tool) and the Agent SDK? Can SDK-built agents use hooks?
    - alignment pass rate: 0.333
    - cite c98: partial — The chunk clearly shows TypeScript is a superset of Python (PostToolBatch, SessionStart, SessionEnd, Setup are TypeScrip
    - cite c95: partial — The chunk discusses hooks and lifecycle events in the agent SDK generally (PreToolUse, PostToolUse, subagent events, etc
    - cite c1641: unrelated — The chunk describes hook configuration structure and terminology in general terms, but makes no mention of TypeScript SD

- **Q049** (paraphrase_pair) — low_citation_alignment
  - Q: How does the Python Agent SDK's query() function differ from ClaudeSDKClient for multi-turn conversations?
    - alignment pass rate: 0.333
    - cite c255: partial — The table directly supports the session behavior and use-case claims (fresh session per call, one-off tasks vs. persiste
    - cite c266: partial — The chunk confirms that ClaudeSDKClient is suited for chat interfaces, REPLs, follow-up questions, and continuing conver
    - cite c421: partial — The chunk confirms that automatic session management exists (supporting the claim about ClaudeSDKClient handling bookkee

- **Q050** (paraphrase_pair) — low_citation_alignment
  - Q: In the Python Agent SDK, when would I choose ClaudeSDKClient instead of calling query() repeatedly?
    - alignment pass rate: 0.5
    - cite c266: partial — The chunk confirms several ClaudeSDKClient use cases cited in the sentence (follow-up questions, conversation continuity
    - cite c260: partial — The chunk confirms that query() does not support interrupts and ClaudeSDKClient does, but it does not mention the specif
    - cite c258: partial — The chunk confirms that `query()` manages connections automatically and `ClaudeSDKClient` requires manual control, but d

### S3 — Retrieval recall failures (recall@10 < 0.5)

- **Q003** (factual) — recall@10 = 0.0
  - Q: What are the five permission modes available in Claude Code and what does each do?
  - missing pages: ['permissions.md']

- **Q011** (coverage) — recall@10 = 0.25
  - Q: What are all the ways Claude Code can authenticate to Anthropic's API or a provider, covering both individual users and enterprise teams?
  - missing pages: ['amazon-bedrock.md', 'google-vertex-ai.md', 'microsoft-foundry.md']

- **Q014** (coverage) — recall@10 = 0.333
  - Q: What are at least three distinct ways to reduce token usage and costs in Claude Code?
  - missing pages: ['best-practices.md', 'headless.md']

- **Q029** (recency) — recall@10 = 0.0
  - Q: What changed about the Windows managed settings path starting with Claude Code v2.1.75?
  - missing pages: ['settings.md']

- **Q030** (recency) — recall@10 = 0.0
  - Q: What version of Claude Code introduced Opus 4.7 support, and what was the error you would see if using an older SDK version?
  - missing pages: ['agent-sdk/overview.md', 'model-config.md']

- **Q032** (negation) — recall@10 = 0.0
  - Q: What tools and operations does 'bypassPermissions' mode NOT skip, and under what conditions would you still see a prompt?
  - missing pages: ['permissions.md']

- **Q036** (cross_source) — recall@10 = 0.0
  - Q: How does hook configuration differ between Claude Code (the CLI tool) and the Agent SDK? Can SDK-built agents use hooks?
  - missing pages: ['agent-sdk/python.md', 'headless.md', 'hooks.md']

- **Q042** (paraphrase_pair) — recall@10 = 0.333
  - Q: How do I limit Claude's tool access in a Claude Code session?
  - missing pages: ['cli-reference.md', 'sub-agents.md']

- **Q044** (paraphrase_pair) — recall@10 = 0.333
  - Q: How does Claude Code avoid running out of context window during extended coding sessions?
  - missing pages: ['checkpointing.md', 'costs.md']

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

- **synthesis_or_judgment**: 1 cases (Q036)
- **synthesis_picked_wrong_chunk**: 7 cases (Q005, Q012, Q021, Q032, Q036, Q049, Q050)
- **synthesis_incomplete_coverage**: 2 cases (Q021, Q036)
- **retrieval_gap**: 11 cases (Q003, Q011, Q014, Q029, Q030, Q032, Q036, Q042…)

## How to reproduce any finding

Each scored question is reproducible from `answers.jsonl` row. To re-run ID `Q012`:

```bash
DOCS_MONITOR_EMBED_PROVIDER=ollama DOCS_MONITOR_EMBED_MODEL=nomic-embed-text \
  python claude_docs_monitor.py search "<question text from benchmark.jsonl>" --k 10 --json
```

For report runs, use `report` instead of `search` and refer to `--report-ids` flag in `runner.py`.
