---
name: compare-docs
description: Compare the full cached documentation sets for Claude, Gemini, and Codex using a fixed 100-point rubric, then rank feature coverage with evidence-backed strengths, gaps, and tradeoffs.
---

# Compare Docs

Run a full-corpus analysis of locally cached docs for Claude, Gemini, and Codex.

This is not a recent-diff report. It evaluates the entire `pages/` corpus for each tool.

## Workflow

### 1. Verify local corpora exist

Check for cached pages in all three directories:

- `/mnt/c/python/claude_docs_monitor/data-claude/pages/`
- `/mnt/c/python/claude_docs_monitor/data-gemini/pages/`
- `/mnt/c/python/claude_docs_monitor/data-codex/pages/`

If any corpus is missing or empty, tell the user exactly which one is missing and suggest running its docs check flow first.

### 2. Run the comparison analyzer

Use the project script:

```bash
cd /mnt/c/python/claude_docs_monitor && python compare_docs_features.py $ARGUMENTS
```

Default outputs are written to:

- `data-analysis/compare-docs/report.md`
- `data-analysis/compare-docs/report.json`
- `data-analysis/compare-docs/latest_scores.csv`

### 3. Summarize the results

Read `data-analysis/compare-docs/report.md` and provide an executive summary with:

- Final ranking and scores (out of 100)
- Common feature areas across all tools
- Missing/underrepresented feature areas per tool
- Key differentiators for each tool
- Benefits and drawbacks for each tool
- Any reliability penalties that affected scores

### 4. Reference rubric stability

Mention that the analysis uses the fixed rubric in:

`/mnt/c/python/claude_docs_monitor/DOCS_COMPARISON_RUBRIC.md`

If user asks why a score changed across runs, point to corpus changes or reliability penalties.
