# Claude Docs Change Digest

*Generated: 2026-02-26 20:49 UTC*

### Executive Summary
This release adds non-git VCS support for worktrees via new hooks, a Remote Control feature for controlling local Claude from a browser, and several new managed settings for enterprise control. The `&` prefix for web sessions has been replaced by `claude --remote`, and auto memory is now enabled by default.

### New Features
- **WorktreeCreate/WorktreeRemove hooks**: Replace default git worktree behavior with custom VCS logic (SVN, Perforce, Mercurial)
- **Subagent worktrees**: Subagents support `isolation: worktree` in frontmatter for parallel work without conflicts
- **Remote Control**: `claude remote-control` lets you control a local Claude process from the web UI or mobile app
- **`claude agents` command**: List all configured subagents grouped by source without starting a session
- **`claude auth` subcommands**: `login`, `logout`, and `status` for scripted auth management
- **npm plugin packages**: npm source for plugins is now fully implemented (previously marked "not yet implemented")
- **`autoMemoryEnabled` setting**: Control auto memory per-project or user via `settings.json`; auto memory is now **on by default**
- **MDM/OS-level managed settings**: macOS plist (`com.anthropic.claudecode`) and Windows registry (`HKLM\SOFTWARE\Policies\ClaudeCode`) support for managed settings
- **Agent team size guidance**: 3–5 teammates recommended; new "Choose an appropriate team size" section with cost/coordination tradeoffs
- **`/rename` auto-generates names**: Omit the name argument to generate one from conversation history
- **`/copy` code block picker**: When code blocks are present, shows an interactive picker to copy individual blocks or the full response
- **`CLAUDE_CODE_DISABLE_1M_CONTEXT`**: Env var to disable 1M context window support (for compliance)
- **`CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS`**: Configurable timeout for plugin git operations (default 120s)
- **SDK account env vars**: `CLAUDE_CODE_ACCOUNT_UUID`, `CLAUDE_CODE_USER_EMAIL`, `CLAUDE_CODE_ORGANIZATION_UUID` for SDK callers to avoid telemetry race conditions

### Breaking Changes
- **`&` prefix for web sessions removed**: The `& Fix the bug` in-session syntax is gone. Use `claude --remote "Fix the bug"` from the command line instead. Update any scripts or habits using the `&` prefix.
- **`/path` permissions now relative to project root**: A rule like `Edit(/src/**)` resolves to `<project root>/src/**`, not `<settings file path>/src/**`. Review existing permission rules that use leading `/`.

### Deprecations
- **npm installation**: Continues deprecation. Migrate with `curl -fsSL https://claude.ai/install.sh | bash && npm uninstall -g @anthropic-ai/claude-code`
- **`DISABLE_AUTOUPDATER` shell export**: Documentation now shows the preferred way as `{"env": {"DISABLE_AUTOUPDATER": "1"}}` in `settings.json`

### Flag & API Changes
- **New managed-only settings**: `allowManagedMcpServersOnly`, `blockedMarketplaces`, `sandbox.network.allowManagedDomainsOnly`, `allow_remote_sessions`
- **`--worktree` now primary form**: `-w` still works as alias; docs now show `--worktree` as the canonical flag
- **Background subagents**: MCP tools restriction removed — background subagents can now use MCP tools
- **Managed settings precedence within tier**: server-managed > MDM/OS policies > `managed-settings.json` > HKCU registry; sources do not merge, only one is used

### Notable Clarifications
- **Windows requires Git for Windows**: Now prominently documented across install, quickstart, and overview pages; required for native Windows (not just optional)
- **`/status` shows settings sources**: Reports which managed settings layer is active (`remote`, `plist`, `HKLM`, or `file`)
- **Managed settings precedence**: When server-managed and endpoint-managed are both present, server-managed wins and endpoint-managed is entirely ignored
- **Troubleshooting guide massively expanded**: Now includes a quick-lookup error table and detailed sections for each install error (OOM, TLS, musl/glibc mismatch, Docker hangs, etc.)
- **setup.md retitled "Advanced setup"**: First-run content moved to quickstart; setup page now focused on system requirements, version management, and uninstall
- **Remote Control data flow**: Clarified as local execution — no cloud VMs involved, all data stays on your machine

### Action Items
- [ ] Replace any `& <task>` usage in scripts/habits with `claude --remote "<task>"`
- [ ] Audit permission rules using `/path` patterns — they now resolve to project root, not settings file location
- [ ] If using non-git VCS with worktrees, configure `WorktreeCreate`/`WorktreeRemove` hooks
- [ ] Windows users: ensure Git for Windows is installed before running Claude Code
- [ ] Enterprise admins: review new managed settings (`allowManagedMcpServersOnly`, `blockedMarketplaces`, `allow_remote_sessions`, `sandbox.network.allowManagedDomainsOnly`)
- [ ] If auto memory should be off, add `{"autoMemoryEnabled": false}` to `settings.json` (it's now on by default)
- [ ] Verify Homebrew installs do periodic `brew cleanup claude-code` to reclaim disk space from old versions
