# Setup Impact Report — 2026-06-10

Window: 30d | Events analyzed: 272 (30 high / 146 medium / 96 low) across runs 2026-05-21 and 2026-05-28 | Docs snapshot: 2026-05-28

Profile sources: `~/.claude/settings.json`, `~/.claude/rules/agent-sdk-max-oauth.md`, `~/.claude/CLAUDE.md`, `~/.claude/lib/*` (8 scripts), `~/.claude/commands/` (35 skills), project `.mcp.json` + `.claude/settings.local.json`.

## Action needed

1. **`CLAUDE_CODE_EFFORT_LEVEL=max` blocks ultracode.** Your settings.json env pins effort to `max`, and the env var "takes precedence over `/effort` and the `effortLevel` setting" (env-vars.md). Ultracode is session-only and set via `/effort ultracode` (settings.md) — which your pin overrides. Confirmed live: today's `/effort` printed "CLAUDE_CODE_EFFORT_LEVEL=max overrides effort this session". **Do:** remove the env pin (or switch to the `effortLevel: "xhigh"` setting, which `/effort` can override) so ultracode becomes reachable.

2. **`CLAUDE_CODE_ENABLE_TASKS: "true"` is a no-op.** As of v2.1.142 Task tools are the default in all modes; the flag only does something when set to `0` to revert to `TodoWrite` (env-vars.md, tools-reference.md). **Do:** delete the line from settings.json env.

3. **`CLAUDE_CODE_WORKFLOWS=1` is vestigial.** Workflows are GA and default-on; the current docs only define the opt-out (`CLAUDE_CODE_DISABLE_WORKFLOWS` / `disableWorkflows`, env-vars.md + settings.md + workflows.md). The bare `CLAUDE_CODE_WORKFLOWS` flag no longer appears anywhere in the cached pages. **Do:** delete the line from settings.json env.

4. **`/model` now saves your selection as the default.** Inverted in v2.1.153: Enter persists; `s` switches for the session only; the old `d`-to-persist keybinding was removed (commands.md, model-config.md, keybindings.md). This bit you today — your first `/model` press silently saved Opus 4.8 (1M) as the default before you corrected it to Fable 5. **Do:** use `s` in the picker for session-only switches.

5. **Stale model IDs in your SDK tooling — fixed during this run.** Per the maintenance note in `rules/agent-sdk-max-oauth.md`:
   - `llm_backend.py` alias map: repo had `opus → claude-opus-4-7` (Opus 4.8 is the new default, model-config.md); the `~/.claude/lib/` copy was three generations stale (`claude-sonnet-4-20250514` era). Repo updated to `claude-opus-4-8` and re-synced to lib.
   - `~/.claude/commands/new-agent-sdk-app.md` template defaulted generated apps to `claude-sonnet-4-20250514` (≈13 months old) and listed Opus 4.5/Haiku 4 in its models table. Updated to `claude-sonnet-4-6` / `claude-opus-4-8` / `claude-haiku-4-5-20251001`.

## Directly affects you

- **`voiceEnabled` is a documented legacy alias** — "Legacy alias for `voice.enabled`. Prefer the `voice` object" (settings.md). Your settings.json carries both `voice: {enabled, mode}` and `voiceEnabled: true`. Safe cleanup: drop `voiceEnabled`.
- **Fast mode on Opus 4.6 is deprecated** (~30 days after Opus 4.8 launch) and Opus 4.8 fast mode costs $10/$50 MTok vs $30/$150 (fast-mode.md). You toggled `/fast` in past sessions; prefer Opus 4.8 when fast.
- **`/simplify` → `/code-review`** (skills.md, commands.md): `/simplify` survives as an alias for `/code-review --fix`, but new muscle memory should target `/code-review`.
- **`defaultMode: "auto"` placement rule** (settings.md, v2.1.142): now ignored in project/local settings, honored only in `~/.claude/settings.json` — yours is already user-level, so you're compliant, but don't move it.

## Likely relevant

- **MCP startup is non-blocking by default** (env-vars.md, v2.1.142): the project's `docs-monitor` MCP tools may not be ready on a session's very first turn. If that ever matters, mark the server `alwaysLoad: true` or set `MCP_CONNECTION_NONBLOCKING=0`.
- **Python Agent SDK churn for your `new-agent-sdk-app` projects**: `query()` now supports continuation (`continue_conversation`/`resume`); Python SDK sandbox defaults to running *unsandboxed* on failure, unlike TypeScript (agent-sdk/python.md). The TypeScript `env`-replaces-environment breaking change does not affect your template — it deletes `ANTHROPIC_API_KEY` from `process.env` rather than passing an `env` option.
- **Four settings keys are absent from the current docs**: `skipAutoPermissionPrompt`, `remoteControlAtStartup`, `agentPushNotifEnabled`, `gitAttribution`. They may be internal/undocumented or stale; `gitAttribution: false` in particular looks like a duplicate of the documented `includeCoAuthoredBy: false` you already set. Worth pruning experimentally.
- **`extraKnownMarketplaces` may be redundant**: you register `claude-code-plugins → github anthropics/claude-code`, but the docs now describe two built-in public marketplaces (`claude-plugins-official`, `claude-community`) and your plugins already resolve via `@claude-plugins-official` (plugins.md, discover-plugins.md).
- **Project `.claude/settings.local.json` carries dead allowlist entries** referencing `reindex`/`search` CLI commands and Voyage AI domains from the rolled-back RAG experiment — harmless, but prunable.

## Worth adopting

- **`/usage` per-skill/subagent/MCP breakdown and `/usage-credits`** (costs.md) — you run heavy multi-agent sessions on Max; `/extra-usage` was renamed.
- **Status line upgrades** (statusline.md): your custom `statusline-command.sh` can now use `COLUMNS`/`LINES` for width-aware layout (v2.1.153) and new `pr.number`/`pr.url`/`pr.review_state` + `workspace.repo` fields.
- **`disallowed-tools` skill frontmatter + `/reload-skills`** (skills.md, v2.1.152) — applicable across your 35 custom skills to scope tool access while a skill is active.
- **Per-server `timeout` field in `.mcp.json`** (mcp.md) — available for the docs-monitor server.
- **New pages worth a read given your setup**: workflows.md (you pre-adopted via flag), sandbox-environments.md, security-guidance.md, large-codebases.md, prompt-caching.md (note: effort level is now part of the cache key — mid-session effort changes invalidate the cache, which interacts with finding #1).
- **Fable 5**: you're running `claude-fable-5`, but the cached docs don't document it and your rules file's working-models list doesn't include it. Once you've confirmed it works via the Agent SDK with Max OAuth, add it to `rules/agent-sdk-max-oauth.md`.

## Checked and clean

- `alwaysThinkingEnabled`, `showThinkingSummaries`, `showClearContextOnPlanAccept`, `includeCoAuthoredBy`, `teammateMode`, `skipDangerousModePermissionPrompt`, `statusLine`, `enabledPlugins` — all documented-current (settings.md and related pages).
- `CLAUDE_CODE_MAX_OUTPUT_TOKENS`, `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` — still documented (env-vars.md; agent teams remains flag-gated).
- `--dangerously-skip-permissions` root/sudo block (sandboxing.md) — you run as a non-root WSL user; not affected.
- Monitor's `claude -p` surface: `--output-format json`, `--json-schema`, `--max-turns` all still in cli-reference.md.
- Monitor's `CLAUDECODE` strip for nested invocation: unaffected by the change that now sets `CLAUDECODE` in hook/status-line commands; `statusline-command.sh` doesn't reference it.
- `rules/agent-sdk-max-oauth.md` model list (`claude-sonnet-4-6`, `claude-opus-4-8`, `claude-haiku-4-5-20251001`) — current per the cached docs.
- Global `CLAUDE.md` uses no `@import`s — the import-depth reduction (5 → 4 hops, memory.md) doesn't apply.
- Max OAuth flow: the `CLAUDE_CODE_SIMPLE` bare-mode OAuth removal doesn't apply (you don't use bare mode); no `forceLoginMethod` managed settings in play.

> Docs last updated: 2026-05-28 13:14 (local) — run /check-docs first if this is stale.
