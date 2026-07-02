# Codex Docs Change Digest

*Generated: 2026-05-10 20:14 UTC*

### Executive Summary
Codex documentation expanded materially across the app, Windows, and extensibility surface. The May 10 refresh added 13 pages, removed 3 older pages, and rewrote key guidance around sandboxing, plugins, remote connections, memories, and subagents.

### New Features
- In-app browser docs now cover shared rendered-page preview, page comments, and Browser plugin driven browser use for local and public pages ([browser](https://developers.openai.com/codex/app/browser.md))
- Computer Use is now documented as a macOS GUI automation workflow with Screen Recording, Accessibility, and per-app approvals ([computer-use](https://developers.openai.com/codex/app/computer-use.md))
- Subagents now have first-class docs for built-in agents, custom agents, thread management, and concurrency/depth settings ([subagents](https://developers.openai.com/codex/subagents.md))
- Plugins are now documented as the installable distribution unit for skills, apps, and MCP servers, with separate authoring guidance for marketplaces and packaging ([plugins](https://developers.openai.com/codex/plugins.md))
- Memories are now documented as a feature with thread-level controls, storage details, and generation settings ([memories](https://developers.openai.com/codex/memories.md))
- Chronicle is now documented as an opt-in research preview that augments memories from screen context on macOS ([chronicle](https://developers.openai.com/codex/memories/chronicle.md))
- SSH remote connections are now documented as an alpha Codex app feature for remote project execution ([remote-connections](https://developers.openai.com/codex/remote-connections.md))
- Codex now documents an import flow for bringing setup, sessions, skills, hooks, MCP servers, and subagents from another agent into Codex ([migrate](https://developers.openai.com/codex/migrate.md))

### Breaking Changes
- Older multi-agent docs were removed in favor of the new subagent documentation, so bookmarks and internal links targeting `multi-agent` or `concepts/multi-agents` now need replacement ([subagents](https://developers.openai.com/codex/subagents.md))
- The CLI reference no longer presents `--full-auto` as the primary path for edit-capable runs; the explicit replacement is `--sandbox workspace-write --ask-for-approval on-request` ([cli-reference](https://developers.openai.com/codex/cli/reference.md))
- Windows guidance now states that WSL1 is unsupported starting in Codex `0.115`, which matters for older Windows automation setups ([windows](https://developers.openai.com/codex/windows.md))

### Deprecations
- `codex exec --full-auto` is now documented as a deprecated compatibility flag; new automation should switch to explicit sandbox flags ([noninteractive](https://developers.openai.com/codex/noninteractive.md))
- `on-failure` remains documented as deprecated for approval behavior, with `on-request` or `never` preferred depending on interactivity ([cli-reference](https://developers.openai.com/codex/cli/reference.md))

### Flag & API Changes
- The CLI reference adds `--remote` and `--remote-auth-token-env` for connecting the interactive TUI to a remote app-server endpoint ([cli-reference](https://developers.openai.com/codex/cli/reference.md))
- Sandboxing docs add deny-read filesystem profiles, granular approval policies, and automatic approval review via `approvals_reviewer = "auto_review"` ([sandboxing](https://developers.openai.com/codex/concepts/sandboxing.md))
- MCP docs add `experimental_environment = "remote"` and remote-sourced `env_vars` entries for stdio servers that run in remote executor environments ([mcp](https://developers.openai.com/codex/mcp.md))
- Auth docs add `CODEX_CA_CERTIFICATE`, a dedicated `codex-login.log`, and clearer billing guidance for ChatGPT sign-in versus API-key usage ([auth](https://developers.openai.com/codex/auth.md))

### Notable Clarifications
- Quickstart now states that every ChatGPT plan includes Codex, and the Codex app is available on both macOS and Windows ([quickstart](https://developers.openai.com/codex/quickstart.md))
- IDE docs now treat Windows as a supported Codex IDE platform and clarify that VS Code opens Codex in the right sidebar by default ([ide](https://developers.openai.com/codex/ide.md))
- Skills docs now spell out the initial skill-list context budget and position plugins as the distribution layer for reusable skills ([skills](https://developers.openai.com/codex/skills.md))

### Action Items
- [ ] Replace internal references and scripts that still use `--full-auto`, `codex/explore`, or legacy multi-agent URLs ([noninteractive](https://developers.openai.com/codex/noninteractive.md))
- [ ] Review whether new browser, computer-use, memories, and Chronicle capabilities need policy guardrails before broad internal adoption ([computer-use](https://developers.openai.com/codex/app/computer-use.md))
- [ ] If you operate Windows, remote, or remote-MCP workflows, review the new sandbox and remote-environment settings before updating local defaults ([windows](https://developers.openai.com/codex/windows.md))
