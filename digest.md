# Claude Docs Change Digest

*Generated: 2026-03-03 03:46 UTC*

### Executive Summary
This update introduces a significant rework of the memory/CLAUDE.md documentation (now at `/en/memory`), renames the "Task" tool/permission syntax to "Agent" across the board, adds HTTP hooks as a new hook type, and expands sandbox filesystem control with granular path settings. These changes affect permission rules, hook configs, and agent definitions in settings files.

### New Features
- **HTTP hooks** (`type: "http"`): POST hook event data to an HTTP endpoint instead of running a shell command; supports env var interpolation in headers
- **Sandbox filesystem controls**: New `sandbox.filesystem.allowWrite`, `denyWrite`, `denyRead` settings for OS-level subprocess path restrictions (affects `kubectl`, `terraform`, `npm`, etc.)
- **Bundled skills**: `/simplify`, `/batch`, `/debug` now ship with Claude Code out of the box
- **`claudeMdExcludes` setting**: Skip specific CLAUDE.md files by path/glob (useful in monorepos)
- **`fastModePerSessionOptIn` setting**: Admins can require users to re-enable fast mode each session
- **`allowedHttpHookUrls` / `httpHookAllowedEnvVars`**: Settings to restrict HTTP hook targets and env var access
- **Session management on web**: Archive and delete Claude.ai sessions from sidebar
- **VS Code session management**: Hover over sessions to rename or remove them
- **Remote Control on Pro**: Now available on Pro plans (was Max-only)
- **`ENABLE_CLAUDEAI_MCP_SERVERS` env var**: Set to `false` to disable claude.ai MCP servers in Claude Code
- **`/diff` command**: Interactive diff viewer for uncommitted changes and per-turn diffs
- **`/security-review` command**: Analyzes pending branch changes for security vulnerabilities
- **`/pr-comments` and `/review` commands**: GitHub PR integration (requires `gh` CLI)

### Breaking Changes
- **`Task(...)` renamed to `Agent(...)`** in permission rules, agent `tools` fields, and `--disallowedTools` CLI flag. `Task(Explore)` → `Agent(Explore)`. Old `Task(...)` references still work as aliases (v2.1.63+), but update configs to avoid future breakage
- **`Task` tool renamed to `Agent`** in settings tools table and PreToolUse hook matchers — update any hook matchers that reference `Task`

### Deprecations
- `Task(AgentName)` syntax in permissions/agent definitions — still works as alias, migrate to `Agent(AgentName)`

### Flag & API Changes
- New setting: `sandbox.filesystem.allowWrite` / `denyWrite` / `denyRead` — array, merges across settings scopes
- New setting: `fastModePerSessionOptIn: true` — resets fast mode each session
- New setting: `allowedHttpHookUrls` — URL allowlist for HTTP hooks
- New setting: `httpHookAllowedEnvVars` — restrict env vars HTTP hooks can interpolate
- New env var: `ENABLE_CLAUDEAI_MCP_SERVERS=false` — disables claude.ai MCP servers
- Array settings (`sandbox.filesystem.*`, `permissions.allow/deny`, etc.) now explicitly documented as **merged** (concatenated+deduplicated) across settings scopes, not replaced
- Sandbox path prefixes: `//` = absolute, `~/` = home-relative, `/` = settings-file-relative

### Notable Clarifications
- Memory page (`/en/memory`) completely rewritten with troubleshooting section, CLAUDE.md vs auto memory comparison table, and guidance on effective instructions (target **200 lines**, not 500)
- Path-scoped `.claude/rules/` files only load when Claude works with matching files (saves context)
- ZDR (Zero Data Retention) is per-organization — each org must have it enabled separately
- Sandbox restrictions apply to all subprocess commands, not just Claude's file tools
- Auto memory is machine-local; worktrees within the same repo share one auto memory directory
- CLAUDE.md is context, not enforcement — added troubleshooting section for when instructions aren't followed

### Action Items
- [ ] Update any `Task(Explore)`, `Task(my-agent)` references in `settings.json` or `--disallowedTools` to `Agent(Explore)`, `Agent(my-agent)`
- [ ] Update agent `.yaml` frontmatter `tools:` fields from `Task(...)` to `Agent(...)`
- [ ] Update PreToolUse hook matchers that reference `"Task"` to `"Agent"`
- [ ] Review `sandbox.filesystem.allowWrite` for tools like `kubectl`/`terraform` that need to write outside the working directory (replaces using `excludedCommands`)
- [ ] Trim CLAUDE.md files over 200 lines — move content to `.claude/rules/` or skill files
- [ ] If using HTTP hooks, configure `allowedHttpHookUrls` in managed settings for security
- [ ] Enterprise/Team admins: consider `fastModePerSessionOptIn: true` for cost control
