# Benchmark patches — meta-findings

The adversarial-generator built `benchmark.jsonl` claiming all 10 lures (Q016-Q025) were verified non-existent. Independent verification by grepping the cached pages found **two false negatives** in the lure set:

## P-BMK-1 (S2): Q018 is not a valid lure — `CLAUDE_CODE_MAX_CONTEXT_TOKENS` IS documented

The benchmark labels Q018 `hallucination_lure` with expected answer "does not exist". But the env var is documented in `env-vars.md`:

> `CLAUDE_CODE_MAX_CONTEXT_TOKENS` — Override the context window size Claude Code assumes for the active model. Only takes effect when `DISABLE_COMPACT` is also set. Use this when routing to a model through `ANTHROPIC_BASE_URL` whose context window does not match the built-in size for its name.

It also appears in `changelog.md`. **Action**: reclassified to `factual` (medium) with the documented answer, kept the ID for traceability.

## P-BMK-2 (S3): Q024 mis-classified as lure — answer IS in the docs (as a negation)

The benchmark labels Q024 `hallucination_lure` but the expected_answer correctly says "No. Claude Code explicitly does not support SOCKS proxies." This is a NEGATION question with a documented answer. The generator's report acknowledged this rejection during drafting but the dimension field wasn't updated. **Action**: reclassified to `negation` (medium).

## Why this matters

The user asked for **brutal honesty over flattering numbers**. If the benchmark itself contains errors, scoring is meaningless. Catching this before scoring is exactly the calibration step the plan called for. This finding is reportable as part of the review:

> **Even an LLM agent with strict instructions to grep before writing each lure produced a 2/10 false-positive rate on lure verification.** Implication: any retrospective change-classification step needs ground-truth verification (grep), not just LLM judgment.

## Adjusted dimension counts after patch

| dimension | before | after |
|---|---|---|
| factual | 5 | 6 |
| hallucination_lure | 10 | 8 |
| negation | 5 | 6 |
| (others unchanged) | | |

The 8 remaining lures were re-verified by grep:
- Q016 voice-transcription — verified zero matches
- Q017 /summarize-pr — verified zero matches  
- Q019 plugin sandboxing — TODO re-verify
- Q020 MEMORY_RETENTION_DAYS — verified zero matches
- Q021 --parallel-agents — TODO re-verify
- Q022 thought budget — verified zero matches (the plausible cousin is Anthropic API `thinking.budget_tokens`, distinct)
- Q023 PreFileWrite — verified zero matches
- Q025 GitHubCodeReview — verified zero matches
