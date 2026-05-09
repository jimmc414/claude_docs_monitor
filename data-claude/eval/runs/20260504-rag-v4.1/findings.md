# Adversarial Review — Findings (run 20260504-rag-v4.1)

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
| partially_correct | 2 | 66.7% |
| hallucinated | 1 | 33.3% |

### Citation alignment (per-citation judge)

| Verdict | n | % |
|---|---|---|
| supports | 3 | 50.0% |
| partial | 3 | 50.0% |

### Hallucination resistance (lures)

_No lure had a full `report` run; hallucination resistance is unmeasured. 8 lures had search only._

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

- **Q032** (negation) — HALLUCINATED
  - Q: What tools and operations does 'bypassPermissions' mode NOT skip, and under what conditions would you still see a prompt?
  - Judge: The system answer acknowledges it has zero retrieved evidence chunks and admits all claims come from training-data general knowledge. That epistemic honesty aside, the actual content it provides is almost entirely non-overlapping with the canonical answer: every specific canonical point (the rm -rf circuit breaker, the directory-write skip behavior for .git/.claude/.vscode/.idea/.husky, and the di
  - Wrong claims (canonical-vs-system):
    - Claims denylist rules in settings.json are evaluated before and survive the bypass — not mentioned in canonical
    - Claims MCP server-owned confirmations are not bypassed — not mentioned in canonical
    - Claims harness-level safety rails (e.g., force-push to main) still prompt — not mentioned in canonical

### S2 — Missing critical caveats / weak citations / hallucinated citation IDs

- **Q010** (citation) — missing_points
  - Q: The Bash permission rule 'Bash(ls *)' — does it match the command 'lsof'? Why or why not?
    - missing: The canonical answer explicitly states that 'Bash(ls*)' WITHOUT a space WOULD match both 'ls -la' and 'lsof', providing the critical contrast that clarifies the role of the space — this is entirely absent from the system answer
    - missing: The canonical answer frames the space as enforcing a 'word boundary' requiring the prefix to be followed by a space or end-of-string; the system answer conveys a similar idea but never articulates this word-boundary mechanism explicitly

- **Q010** (citation) — low_citation_alignment
  - Q: The Bash permission rule 'Bash(ls *)' — does it match the command 'lsof'? Why or why not?
    - alignment pass rate: 0.5
    - cite c4546: partial — The chunk directly confirms that `Bash(npm run *)` matches commands starting with `npm run`, supporting that specific qu
    - cite c391: partial — The chunk directly confirms that Claude Code parses bash commands into an AST before matching permission rules, but it d
    - cite c2008: partial — The chunk confirms the permission system allows (read-only, no approval) and prompts (bash/file modification require app

- **Q012** (coverage) — missing_points
  - Q: What are all the mechanisms for carrying knowledge or instructions across Claude Code sessions?
    - missing: .claude/rules/*.md — path-scoped rules that load only when Claude works with matching files (completely absent from system answer)
    - missing: Auto memory is stored per working tree and loads first 200 lines or 25KB (specific technical limits not mentioned)
    - missing: Skills are SKILL.md files that load on demand, not slash-command playbooks in .claude/commands/

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

- **synthesis_or_judgment**: 1 cases (Q032)
- **synthesis_incomplete_coverage**: 2 cases (Q010, Q012)
- **synthesis_picked_wrong_chunk**: 1 cases (Q010)
- **retrieval_gap**: 7 cases (Q003, Q036, Q041, Q042, Q043, Q044, Q045)

## How to reproduce any finding

Each scored question is reproducible from `answers.jsonl` row. To re-run ID `Q012`:

```bash
DOCS_MONITOR_EMBED_PROVIDER=ollama DOCS_MONITOR_EMBED_MODEL=nomic-embed-text \
  python claude_docs_monitor.py search "<question text from benchmark.jsonl>" --k 10 --json
```

For report runs, use `report` instead of `search` and refer to `--report-ids` flag in `runner.py`.
