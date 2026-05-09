# UX Findings — new-hire pass

Evaluated: 2026-05-03
Evaluator: New-hire persona (zero prior project knowledge)
Time-boxed to: ~30 min equivalent

---

## TL;DR (3 bullets)

- The README describes a simpler, older version of the tool ("data/" directory, 1 script to install, no mention of the 6 RAG modules) — the actual system is significantly more complex and the README has not kept up.
- The `search` command silently fails with a hard-to-diagnose error the moment you run it without first knowing which embedding provider to pick; there is no "quick start for search" path in the README.
- The `report` command hangs indefinitely with no output and no timeout — a newcomer will kill it and assume it's broken.

---

## What worked

- `query --json` with no date filter: returned structured JSON immediately, zero friction.
- `search` with `DOCS_MONITOR_EMBED_PROVIDER=ollama` and `--no-rerank --no-expand`: returned ranked results that were genuinely relevant in every Q&A scenario tested.
- Error messages for missing required positional args (`search` with no query, `report` with no question): argparse did the right thing, exit code 2, message clear.
- "Index not built. Run: python ... reindex" message when `search` is pointed at a directory with no `index.db`: one of the better error messages in the tool.
- Five out of five realistic Q&A searches returned top-5 results that were directly relevant and actionable.

---

## Onboarding friction (priority-ordered)

### 1. [HIGH] Search crashes immediately with a cryptic module error — no hint at correct fix

**Reproduce with:**
```bash
python claude_docs_monitor.py search "how do I configure hooks"
```

**Error:**
```
RuntimeError: Voyage provider requires `pip install voyageai`. Or switch to --provider ollama (local, no install) or --provider openai.
```

**Problem:** The error message says `--provider ollama` but the `search` command does not have a `--provider` flag. Only `reindex` has `--provider`. The correct fix is to set `DOCS_MONITOR_EMBED_PROVIDER=ollama` as an environment variable, or to have run `reindex --provider ollama` beforehand. Neither is stated in the error.

**Suggested fix:** Error message should read:
```
RuntimeError: Voyage provider requires `pip install voyageai`, OR set DOCS_MONITOR_EMBED_PROVIDER=ollama
to use local embeddings (requires Ollama running with nomic-embed-text pulled), OR reindex with
`python claude_docs_monitor.py reindex --provider ollama`.
```

---

### 2. [HIGH] README install instructions are stale and incomplete

The README "Claude Code slash command" install block copies 3 skill files and 1 script:
```bash
cp .claude/commands/check-docs.md ~/.claude/commands/
cp .claude/commands/digest.md ~/.claude/commands/
cp .claude/commands/query-docs.md ~/.claude/commands/
cp claude_docs_monitor.py ~/.claude/lib/
```

**Missing from this block:**
- `ask-docs.md` (skill exists in repo, not mentioned in install)
- `report.md` (skill exists in repo, not in README install at all)
- `llm_backend.py` (required by main script at runtime)
- `embedding_cache.py` (required for any RAG feature)
- `doc_index.py` (required for reindex/search)
- `retriever.py` (required for search)
- `report_builder.py` (required for report command)

If a user follows the README install exactly, `/ask-docs` and `/report` will silently not exist. Running `search` or `report` from the CLI after install will fail with an ImportError.

CLAUDE.md has the correct full install list. The README does not.

**Suggested fix:** Unify README install section with the CLAUDE.md install block, or link to CLAUDE.md explicitly.

---

### 3. [HIGH] `report` command hangs indefinitely with zero output

**Reproduce with:**
```bash
python claude_docs_monitor.py report "what is a skill" --max-turns 3 --no-self-critique
```

Result: no output, no progress, hangs until killed (confirmed still hanging at 60s wall-clock). Exit code 143 (SIGTERM).

There is no progress indicator, no startup message, no "connecting to SDK..." — nothing. A newcomer will assume it crashed silently.

**Suggested fix:** Print a startup message immediately, e.g.:
```
Building report for: "what is a skill" (max 3 turns, source=all)...
```
Add an explicit `--timeout SEC` flag. Document in README that the agentic loop typically takes 1-3 minutes.

---

### 4. [MEDIUM] README uses "data/" throughout but the actual default directory is "data-claude/"

The README's "What gets stored" section:
```
data/
  snapshots.db
  pages/
  report.html
  ...
```

Actual default (confirmed in source at line 40: `DB_DIR = Path("data-claude")`): `data-claude/`.

README also says the MCP server reads from `~/.local/share/claude-docs-monitor/data/snapshots.db` — the actual path (from `.mcp.json`) is `~/.local/share/claude-docs-monitor/data-claude/snapshots.db`.

This will confuse anyone trying to find output files or configure the MCP server.

---

### 5. [MEDIUM] `search` by default makes 2 LLM API calls with no warning

Default `search` behavior: query expansion (haiku call) + Claude rerank (another haiku call). This is not mentioned in the README. If the SDK is slow or authentication is off, the default search hangs.

`--no-rerank` still makes 1 LLM call (query expansion). Only `--no-rerank --no-expand` is fully LLM-free. There is no README mention of this, and the flags are not described as having this relationship.

**Suggested fix:** README should note: "By default, `search` uses Claude for query expansion and reranking. Use `--no-rerank --no-expand` for a pure BM25+embedding result with no LLM calls."

---

### 6. [MEDIUM] No Python version or prerequisite section anywhere

The README has no mention of:
- Required Python version (script uses f-strings, walrus operator, match/case — needs ≥3.10)
- Whether `check` requires internet access
- Whether Ollama must be running (it's HTTP-based — not a Python package — and the README only says "no install" without saying "Ollama daemon must be running locally on port 11434")

---

### 7. [LOW] `query` command does not support `--report DIR` flag

CLAUDE.md table row for `query` does not list `--report` as a flag, and the `--help` confirms it's absent. But the tool's default DB path is the system path (`~/.local/share/...`), not `data-claude/`. A user cloning the repo and running `query` against a freshly populated local `data-claude/` DB cannot point the query command at it without the `DOCS_MONITOR_DB` env var — which is only mentioned in the MCP server section, not in the query command docs.

---

## Error message audit

| Command | Exit code | Message quality | Recommended improvement |
|---|---|---|---|
| `search` (no query) | 2 | Good — argparse error, names the missing arg | None needed |
| `report` (no question) | 2 | Good — argparse error, names the missing arg | None needed |
| `search "test" --since not-a-date` | 0 | Bad — returns "No results for: test" with no warning that date was invalid | Should warn "Invalid date format 'not-a-date', ignoring --since filter" and return non-zero or at least print a warning |
| `report "test" --model nonsense` | 143 (timeout/hung) | Bad — hangs with no error, no output | Should validate model alias before entering agentic loop; print error and exit 1 |
| `search "hooks"` (no provider set, voyageai not installed) | 1 | Confusing — error says use `--provider ollama` but that flag doesn't exist on `search` | Fix error message to say `DOCS_MONITOR_EMBED_PROVIDER=ollama` or `reindex --provider ollama` |
| `search "hooks"` (no index.db) | 0 | Good — "Index not built. Run: python ... reindex" | Arguably should be exit code 1 |

---

## Q&A realism — 5 attempts

All 5 tested with: `DOCS_MONITOR_EMBED_PROVIDER=ollama python claude_docs_monitor.py search "<Q>" --k 5 --report data-claude/ --no-rerank`

| Question | Top-5 looked relevant? | Could you act on it? |
|---|---|---|
| "how do I set up MCP servers for my Claude Code project" | Yes — hit Installing MCP servers, Add an MCP server (agent-sdk), VS Code MCP setup, MCP troubleshooting, Check MCP servers | Yes — result 1 and 3 give concrete next steps |
| "what permissions does Claude need to edit files outside the project directory" | Yes — hit Working directories, What Claude can access, Permission-based architecture | Yes — result 1 is immediately actionable (`--add-dir`, `/add-dir`, `additionalDirectories`) |
| "how do I create a custom slash command or skill" | Yes — hit Creating Custom Slash Commands, File Locations, Use skills (desktop) | Yes — first result points to markdown files in `.claude/commands/` |
| "how do I use Claude Code in a CI/CD pipeline without interactive prompts" | Yes — hit "Run non-interactive mode" (best-practices) as #1 | Yes — `claude -p "prompt"` is the answer, result 1 says so |
| "memory management how does Claude Code remember things across sessions" | Yes — hit memory.md whole-page chunk, Work with sessions, Auto memory, How it works | Yes — CLAUDE.md files and auto-memory are both explained in top results |

Search quality is good. The tool works well once you clear the setup hurdles.

---

## Documentation gaps (>=3)

- **Gap 1: `ask-docs` and `report` skills not in README install block.** The README lists 3 skills to install but 5 exist. A user following the README gets `/check-docs`, `/digest`, and `/query-docs` only. `/ask-docs` and `/report` are silently missing. The README does describe both skills in prose but never provides install instructions for them.

- **Gap 2: RAG module scripts absent from README install block.** README says `cp claude_docs_monitor.py ~/.claude/lib/`. CLAUDE.md lists 7 Python files that must be copied. The 6 extra modules (`llm_backend.py`, `embedding_cache.py`, `doc_index.py`, `retriever.py`, `report_builder.py`, `mcp_server.py`) are never mentioned in the README install section. Running `/report` or `search` from a README-installed setup will fail with an ImportError.

- **Gap 3: No "quick start" ordered workflow for the RAG features.** The workflow is: (1) `pip install -r requirements.txt`, (2) `check`, (3) `pip install -r requirements-rag.txt`, (4) set up embedding provider, (5) `reindex`, (6) `search`. Steps 3-5 are buried in a mid-page section titled "Hybrid retrieval and agentic reports (RAG layer)" with no explicit "do these in order" callout. A newcomer running `search` before `reindex` gets a cryptic traceback.

- **Gap 4: Ollama prerequisite not stated.** README says Ollama is "local, free, default-friendly" and "HTTP-based — no Python package needed." It does not say that the Ollama server must be running locally, or how to install it, or how to verify it is running (`curl http://localhost:11434`). If Ollama is not running, `search` with `--provider ollama` will fail at the HTTP call with a connection refused error, and the user has no clue that the daemon is the issue.

- **Gap 5: `query` command cannot point to an alternative DB without undocumented env var.** `search`, `reindex`, `report`, `digest` all have `--report DIR`. `query` does not. The only way to point `query` at a non-default DB is `DOCS_MONITOR_DB=/path/to/snapshots.db`. This env var is documented only in the MCP server section, not near the `query` command. A new user who clones the repo, runs `check`, and then runs `query` will hit the system DB (empty on fresh install) and see "No change events found" — no indication that data exists elsewhere.

- **Gap 6: `--since` filter on `query` silently returns nothing when all data is older than the cutoff.** When `query --since 30d` returns zero results because data is 60 days old, the message is "No change events found matching your query." There is no hint that events exist outside the time window, nor a prompt to run `query` without `--since` or with a wider range. This is especially confusing for new users.

---

## Brutal honesty section

**What I would tell a colleague:**

"The core monitoring and search functionality actually works well once you fight through setup. The Q&A retrieval quality is genuinely impressive — it found relevant, actionable results for every realistic question I threw at it. But getting there as a newcomer is painful.

The README describes a significantly simpler, earlier version of the tool. The install section copies 1 script and 3 skills; the real tool needs 7 scripts and 5 skills. The data directory is called `data/` in the README and `data-claude/` in reality. The MCP server DB path in the README is wrong. If you follow the README from scratch, you'll have a broken install and no way to diagnose it from the docs alone.

The `search` command crashes on first run with an error that tells you to use a flag (`--provider`) that doesn't exist on `search`. The `report` command hangs silently for minutes. Both of these will make a newcomer think the tool is broken.

**Would I recommend this tool?** Yes, with a caveat: read CLAUDE.md instead of the README for setup. The CLAUDE.md is accurate and complete. The README is a liability. Fix the README and the newcomer experience goes from 'frustrating' to 'good.'"

