---
description: Cross-reference recent Claude Code doc changes against your actual local setup
allowed-tools: Bash, Read, Grep, Glob, Write
argument-hint: [window: 7d | 30d | 90d | all] (default 30d)
---

# Setup Impact Report

Answer two questions using only locally cached data:

1. **Push:** Which recent Claude Code documentation changes affect *this user's actual setup*?
2. **Pull:** Does the current setup conflict with, lag behind, or miss anything in the *current* docs?

**Window:** $ARGUMENTS — default `30d` if empty. `all` means no date filter.

## Fixed paths

- Project / data: `/mnt/c/python/claude_docs_monitor` — cached pages in `data-claude/pages/*.md`
- Script: `~/.claude/lib/claude_docs_monitor.py`
- Output: `/mnt/c/python/claude_docs_monitor/data-claude/impact.md`

## Step 1: Build the user profile

Gather the user's real configuration (parallel tool calls where possible):

```bash
cat ~/.claude/settings.json
ls ~/.claude/commands/ ~/.claude/rules/ ~/.claude/lib/ 2>/dev/null
cat ~/.claude/rules/*.md 2>/dev/null
```

Also Read `~/.claude/CLAUDE.md`. If the current working directory is a project with its own `.claude/settings.json`, `.mcp.json`, or `CLAUDE.md`, include those too.

Extract the **checkable elements** — concrete strings whose meaning the docs define:

- Env var names from the settings `env` block (e.g. `CLAUDE_CODE_EFFORT_LEVEL`)
- Top-level and nested settings keys (e.g. `teammateMode`, `voice.enabled`, `permissions.defaultMode`)
- Model IDs anywhere in rules or lib scripts: `rg -o -N "claude-(opus|sonnet|haiku|fable)[a-z0-9.-]*" ~/.claude/rules/ ~/.claude/lib/ | sort -u`
- `claude` CLI flags that lib scripts pass to subprocesses (look for `claude -p`, `--output-format`, `--json-schema`, `--max-turns` in `~/.claude/lib/*.py`)
- Enabled plugins and MCP server entries

Skip custom command names — they are user-authored and will not appear in the docs.

## Step 2: Pull recent change events

```bash
cd /mnt/c/python/claude_docs_monitor && python ~/.claude/lib/claude_docs_monitor.py query --since $WINDOW --limit 500 --json
```

(Omit `--since` when the window is `all`.) Each event has `page_name`, `event_type`, `category`, `severity`, `summary`, `details`, `action_required`, `tags`.

## Step 3: Push analysis — which events touch this setup

For every **high** and **medium** event, classify impact against the profile:

- **direct** — the event names a checkable element, a file the user has, or a feature the profile proves they use
- **likely** — adjacent to a demonstrated usage pattern
- **none** — everything else

For **low** events, only scan summaries for literal mentions of checkable elements.

Be strict: "the user uses Claude Code" matches everything and proves nothing. A `direct` or `likely` verdict requires a *specific* hook — a flag they set, a file they have, a subprocess pattern their scripts use. Cite it (`settings.json env block`, `rules/agent-sdk-max-oauth.md`, `lib/claude_docs_monitor.py`).

## Step 4: Pull analysis — audit the profile against current docs

Check each checkable element against the cached pages (these reflect the docs *as of the last check run*):

1. Batch elements into a few alternation greps rather than one grep per element:
   ```bash
   cd /mnt/c/python/claude_docs_monitor && rg -l "ELEM1|ELEM2|ELEM3" data-claude/pages/
   ```
2. For hits, pull context with `rg -n -C 3` and look for deprecation, supersession, renames, or behavior changes around the element.
3. Read `data-claude/pages/settings.md` in full — it is the canonical reference for settings keys and env vars; one full read beats many partial greps. Read other pages selectively (at most ~10 total; prefer `rg -C` excerpts).
4. Compare model IDs found in Step 1 against `changelog.md` / model pages for newer releases.
5. Classify each element: **documented-current** / **deprecated-or-superseded** / **absent-from-docs**. Also flag internal inconsistencies the docs expose (e.g. two settings keys where docs define one canonical form).

Answer from the cached docs only. If an element is not in the docs, report "absent from docs" — do not guess from outside knowledge.

## Step 5: Write the report and summarize

Write `/mnt/c/python/claude_docs_monitor/data-claude/impact.md`:

```markdown
# Setup Impact Report — {YYYY-MM-DD}

Window: {window} | Events analyzed: {N} ({h} high / {m} medium / {l} low) | Docs snapshot: {newest mtime of data-claude/pages/*.md}

## Action needed
{Conflicts and breaking changes that touch this setup. Each: **what** — why it matters here (config citation) — what to do (doc citation).}

## Directly affects you
{Event-driven findings with config + doc citations.}

## Likely relevant
{Adjacent items, one line each.}

## Worth adopting
{Documented capabilities adjacent to existing usage patterns that the profile shows are unused.}

## Checked and clean
{One line per element verified as documented-current — so an empty findings section means "checked, fine", not "didn't check".}
```

Then summarize the top findings conversationally (lead with "Action needed") and end with:

> Docs last updated: {timestamp} — run /check-docs first if this is stale.

## Edge cases

- **No events in the window:** say so, then still run the Step 4 audit — it depends only on the cached pages, not on events.
- **Stale cache:** if the newest page mtime is older than ~2 weeks, recommend running `/check-docs` first, but proceed with the analysis.
