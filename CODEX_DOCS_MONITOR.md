# Codex Docs Monitor — Command Reference

## What This Is

`codex_docs_monitor.py` is a parallel monitor for OpenAI Codex docs at `https://developers.openai.com/codex/`.
It mirrors the Claude monitor workflow:

- Discover pages from `https://developers.openai.com/codex/llms.txt`
- Fetch concurrently
- Store append-only snapshots in SQLite
- Compute unified diffs
- Generate run reports + cumulative history
- Build AI digests + structured change events

## Defaults

- Database and outputs: `data-codex/`
- Snapshot DB: `data-codex/snapshots.db`
- Latest pages: `data-codex/pages/*.md`
- Reports: `data-codex/report.{md,html}` and `data-codex/history.{md,html}`
- Digest: `data-codex/digest.{md,html}`

Page filenames are path-preserving to avoid collisions:

- `https://developers.openai.com/codex/app/commands.md` -> `app__commands.md`
- `https://developers.openai.com/codex/ide/commands.md` -> `ide__commands.md`

## Authentication for AI Features

`digest` and `backfill` use OpenAI OAuth from `~/.codex/auth.json` (reads `tokens.access_token`) for direct Responses API calls.

If that API path fails (auth scope/expiry/etc.), the monitor automatically falls back to `codex exec` using the local Codex login session.

## Commands

```bash
python codex_docs_monitor.py                         # default: check
python codex_docs_monitor.py check --quiet
python codex_docs_monitor.py check --poll 3600
python codex_docs_monitor.py check --dump ~/docs
python codex_docs_monitor.py check --report ~/reports
python codex_docs_monitor.py check --digest

python codex_docs_monitor.py history
python codex_docs_monitor.py history URL
python codex_docs_monitor.py diff URL
python codex_docs_monitor.py urls
python codex_docs_monitor.py dump
python codex_docs_monitor.py dump ~/review
python codex_docs_monitor.py rebuild-history

python codex_docs_monitor.py digest
python codex_docs_monitor.py digest --model gpt-5
python codex_docs_monitor.py digest --since 7d
python codex_docs_monitor.py digest --gh-issue --gh-repo owner/repo

python codex_docs_monitor.py query breaking
python codex_docs_monitor.py query --since 7d
python codex_docs_monitor.py query "sandbox" --severity high
python codex_docs_monitor.py query --json | jq .

python codex_docs_monitor.py backfill --dry-run
python codex_docs_monitor.py backfill
```

## Notes

- First `check` run creates a baseline (no diffs yet).
- `check --digest` auto-runs digest only when changes are detected.
- `query` reads from `change_events`, which is populated by `digest` and `backfill`.
- Existing `claude_docs_monitor.py` remains unchanged.
