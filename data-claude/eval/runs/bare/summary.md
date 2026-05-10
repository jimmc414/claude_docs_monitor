# Post-rollback 9-Q smoke benchmark

## Result: 3/9 strict, 6/9 partial, 0/9 incorrect

Lands at the lower end of the expected 3-5 strict band predicted by the rollback plan.
Within the same band as every prior RAG variant tested on this 9-question hard subset:

| System                                       | Strict /9 |
|----------------------------------------------|-----------|
| V2 RAG (deterministic top-N) on Sonnet 4.6   | 1         |
| BM25 + Opus 4.7                              | 4         |
| CLI agent + Opus 4.7                         | 4         |
| **Bare /ask-docs-bare + Opus 4.7 (this run)**| **3**     |

The bare grep-and-read skill is in the same performance band as every hybrid RAG
stack we evaluated, with vastly less code. Decision: rollback validated.

## Per-question matrix

| QID  | Dimension          | Difficulty | Correctness         |
|------|--------------------|------------|---------------------|
| Q005 | factual            | hard       | partially_correct   |
| Q010 | citation           | hard       | **correct**         |
| Q012 | coverage           | hard       | partially_correct   |
| Q021 | hallucination_lure | hard       | partially_correct   |
| Q027 | recency            | hard       | **correct**         |
| Q032 | negation           | hard       | **correct**         |
| Q036 | cross_source       | hard       | partially_correct   |
| Q049 | paraphrase_pair    | hard       | partially_correct   |
| Q050 | paraphrase_pair    | hard       | partially_correct   |

## Provenance

- Repo HEAD: `55eb6b4` ("Roll back to bare /ask-docs architecture (f9f39cc)")
- Base commit: `f9f39cc` (2026-03-02)
- Skill: `.claude/commands/ask-docs-bare.md` (project-level alias to bypass user-global hybrid skill shadowing)
- Runner: `data-claude/eval/run_bare.py` invoking `claude -p --model claude-opus-4-7 -- /ask-docs-bare {question}`
- Scorer: `data-claude/eval/scorer.py bare --ids ... --model claude-sonnet-4-6`
- Outputs: `reports.jsonl` (run), `scores.jsonl` (judgments), `summary.md` (this file)
- Run date: 2026-05-09
- Per-question elapsed: 19-66s (median ~38s); 6-11 tool calls; bare grep+read flow, no MCP/hybrid tools observed
