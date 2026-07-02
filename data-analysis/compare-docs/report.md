# Full Documentation Feature Comparison

*Generated: 2026-03-08 05:14:21 UTC*
*Rubric version: 1.0*

## Corpus Coverage

| Tool | Pages | Newest Page (UTC) | History URLs | Expected Unique Files | Collisions | Reliability |
|------|------:|-------------------|-------------:|----------------------:|-----------:|------------:|
| Claude | 60 | 2026-03-07 03:14:37 | 60 | 60 | 0 | 5.0/5 |
| Gemini | 78 | 2026-03-07 08:47:47 | 82 | 78 | 4 | 3.0/5 |
| Codex | 68 | 2026-03-07 04:50:03 | 68 | 68 | 0 | 5.0/5 |

## Scores and Ranking

| Rank | Tool | Score / 100 |
|------|------|------------:|
| 1 | Claude | 100.00 |
| 2 | Codex | 98.80 |
| 3 | Gemini | 95.60 |

## Category Breakdown

| Category | Weight | Claude | Gemini | Codex |
|----------|-------:|-------:|-------:|------:|
| Core Onboarding and Command Surface | 15 | 15.0 | 15.0 | 15.0 |
| Power-User Workflow Depth | 20 | 20.0 | 20.0 | 20.0 |
| Automation and Integrations | 18 | 18.0 | 15.6 | 18.0 |
| Extensibility and Customization | 15 | 15.0 | 15.0 | 15.0 |
| Security and Governance | 17 | 17.0 | 17.0 | 17.0 |
| Enterprise and Operations | 10 | 10.0 | 10.0 | 8.8 |
| Documentation Reliability | 5 | 5.0 | 3.0 | 5.0 |

## Common Features Across All Three

- Onboarding, installation, and first-run setup
- CLI command/reference depth
- Workflow playbooks, examples, and guides
- Troubleshooting and FAQ coverage
- Planning, delegation, and multi-agent orchestration
- Memory, session state, and long-running continuity
- Code review and PR/MR execution workflows
- Headless and non-interactive operation modes
- CI/CD and scheduled automation
- Service integrations and partner ecosystem
- MCP and external tooling connectivity
- Skills, plugins, and extension ecosystem
- Custom prompts, command macros, and rule files
- Deep configuration, model controls, and keybindings
- Permission models and sandbox controls
- Security, safety, and threat-model depth
- Governance, compliance, and policy guidance
- Enterprise admin setup and managed controls
- Pricing, quota, and cost transparency
- Telemetry, analytics, and monitoring

## Missing or Underrepresented Feature Areas

### Claude
- No major missing feature areas under this rubric.

### Gemini
- Service integrations and partner ecosystem (weight 6; current evidence: implied)

### Codex
- Telemetry, analytics, and monitoring (weight 3; current evidence: implied)

## Tool-Specific Differentiators

### Claude
- Desktop-first IDE/app experience (chrome.md, desktop-quickstart.md, desktop.md, jetbrains.md)
- Plugin marketplace and plugin tooling (discover-plugins.md, plugin-marketplaces.md, plugins-reference.md, plugins.md)
- Cloud provider integration docs (amazon-bedrock.md, google-vertex-ai.md, llm-gateway.md, microsoft-foundry.md)
- Remote control and web surface docs (claude-code-on-the-web.md, remote-control.md)
- Zero-data-retention and analytics detail (analytics.md, monitoring-usage.md, zero-data-retention.md)

### Gemini
- Plan mode and task planning workflows (plan-mode.md, planning.md, task-planning.md)
- Policy engine and trusted folder controls (policy-engine.md, trusted-folders.md)
- Web tooling guidance (web-fetch.md, web-search.md, web-tools.md)
- Extension authoring lifecycle (extensions.md, releasing.md, writing-extensions.md)
- Tooling docs for ask-user/internal-docs (activate-skill.md, ask-user.md, internal-docs.md)

### Codex
- Codex cloud environments and internet policy (cloud.md, cloud__environments.md, cloud__internet-access.md)
- App server and noninteractive execution (app-server.md, noninteractive.md)
- Worktree-centric execution model (app__worktrees.md)
- Threat model and cyber safety depth (concepts__cyber-safety.md, security__threat-model.md)
- Agents.md and Agents SDK guidance (guides__agents-md.md, guides__agents-sdk.md)
- Feature maturity and OSS positioning (community__codex-for-oss.md, feature-maturity.md, open-source.md)

## Benefits and Drawbacks

### Claude
Benefits:
- Strong in Core Onboarding and Command Surface (15.0/15)
- Strong in Power-User Workflow Depth (20.0/20)
- Strong in Automation and Integrations (18.0/18)
- Additional feature: Desktop-first IDE/app experience
- Additional feature: Plugin marketplace and plugin tooling
Drawbacks:

### Gemini
Benefits:
- Strong in Core Onboarding and Command Surface (15.0/15)
- Strong in Power-User Workflow Depth (20.0/20)
- Strong in Extensibility and Customization (15.0/15)
- Additional feature: Plan mode and task planning workflows
- Additional feature: Policy engine and trusted folder controls
Drawbacks:
- Missing or weak feature area: Service integrations and partner ecosystem
- Corpus reliability penalty (3.0/5): URL-to-filename collisions detected: 4

### Codex
Benefits:
- Strong in Core Onboarding and Command Surface (15.0/15)
- Strong in Power-User Workflow Depth (20.0/20)
- Strong in Automation and Integrations (18.0/18)
- Additional feature: Codex cloud environments and internet policy
- Additional feature: App server and noninteractive execution
Drawbacks:

## Detailed Feature Matrix

### Core Onboarding and Command Surface

| Feature | Weight | Claude | Gemini | Codex |
|---------|-------:|--------|--------|-------|
| Onboarding, installation, and first-run setup | 4 | 4.0/4 (explicit; desktop-quickstart.md, features-overview.md, overview.md, quickstart.md) | 4.0/4 (explicit; get-started.md, installation.md, mcp-setup.md) | 4.0/4 (explicit; enterprise__admin-setup.md, overview.md, quickstart.md) |
| CLI command/reference depth | 4 | 4.0/4 (explicit; cli-reference.md, plugins-reference.md) | 4.0/4 (explicit; cli-reference.md, commands.md, custom-commands.md, reference.md) | 4.0/4 (explicit; cli.md, cli__reference.md, cli__slash-commands.md, config-reference.md) |
| Workflow playbooks, examples, and guides | 4 | 4.0/4 (explicit; best-practices.md, common-workflows.md) | 4.0/4 (explicit; best-practices.md, examples.md) | 4.0/4 (explicit; explore.md, workflows.md) |
| Troubleshooting and FAQ coverage | 3 | 3.0/3 (explicit; troubleshooting.md) | 3.0/3 (explicit; faq.md, troubleshooting.md, uninstall.md) | 3.0/3 (explicit; app__troubleshooting.md, security__faq.md) |

### Power-User Workflow Depth

| Feature | Weight | Claude | Gemini | Codex |
|---------|-------:|--------|--------|-------|
| Planning, delegation, and multi-agent orchestration | 5 | 5.0/5 (explicit; agent-teams.md, sub-agents.md) | 5.0/5 (explicit; plan-mode.md, planning.md, subagents.md, task-planning.md) | 5.0/5 (explicit; agent-approvals-security.md, concepts__multi-agents.md, multi-agent.md) |
| Memory, session state, and long-running continuity | 5 | 5.0/5 (explicit; checkpointing.md, memory.md, statusline.md) | 5.0/5 (explicit; checkpointing.md, memory-management.md, memory.md, rewind.md) | 5.0/5 (explicit; app__worktrees.md) |
| Code review and PR/MR execution workflows | 5 | 5.0/5 (explicit; desktop-quickstart.md, desktop.md, github-actions.md, gitlab-ci-cd.md) | 5.0/5 (explicit; issue-and-pr-automation.md, preview.md) | 5.0/5 (explicit; app__review.md, github-action.md) |
| Headless and non-interactive operation modes | 5 | 5.0/5 (explicit; headless.md) | 5.0/5 (explicit; headless.md) | 5.0/5 (explicit; app-server.md, noninteractive.md) |

### Automation and Integrations

| Feature | Weight | Claude | Gemini | Codex |
|---------|-------:|--------|--------|-------|
| CI/CD and scheduled automation | 6 | 6.0/6 (explicit; github-actions.md, gitlab-ci-cd.md, scheduled-tasks.md) | 6.0/6 (explicit; automation.md, issue-and-pr-automation.md) | 6.0/6 (explicit; app__automations.md, github-action.md) |
| Service integrations and partner ecosystem | 6 | 6.0/6 (explicit; amazon-bedrock.md, google-vertex-ai.md, llm-gateway.md, microsoft-foundry.md) | 3.6/6 (implied; authentication.md, best-practices.md, cli-reference.md, commands.md) | 6.0/6 (explicit; integrations__github.md, integrations__linear.md, integrations__slack.md) |
| MCP and external tooling connectivity | 6 | 6.0/6 (explicit; mcp.md) | 6.0/6 (explicit; mcp-server.md, mcp-setup.md) | 6.0/6 (explicit; mcp.md) |

### Extensibility and Customization

| Feature | Weight | Claude | Gemini | Codex |
|---------|-------:|--------|--------|-------|
| Skills, plugins, and extension ecosystem | 5 | 5.0/5 (explicit; discover-plugins.md, plugin-marketplaces.md, plugins-reference.md, plugins.md) | 5.0/5 (explicit; activate-skill.md, creating-skills.md, extensions.md, skills-getting-started.md) | 5.0/5 (explicit; skills.md) |
| Custom prompts, command macros, and rule files | 5 | 5.0/5 (explicit; output-styles.md) | 5.0/5 (explicit; custom-commands.md, gemini-md.md, system-prompt.md) | 5.0/5 (explicit; custom-prompts.md, rules.md) |
| Deep configuration, model controls, and keybindings | 5 | 5.0/5 (explicit; keybindings.md, model-config.md, network-config.md, server-managed-settings.md) | 5.0/5 (explicit; configuration.md, generation-settings.md, model-routing.md, policy-engine.md) | 5.0/5 (explicit; app__settings.md, config-advanced.md, config-basic.md, config-reference.md) |

### Security and Governance

| Feature | Weight | Claude | Gemini | Codex |
|---------|-------:|--------|--------|-------|
| Permission models and sandbox controls | 6 | 6.0/6 (explicit; permissions.md, sandboxing.md) | 6.0/6 (explicit; policy-engine.md, sandbox.md, trusted-folders.md) | 6.0/6 (explicit; agent-approvals-security.md, concepts__sandboxing.md) |
| Security, safety, and threat-model depth | 6 | 6.0/6 (explicit; authentication.md, data-usage.md, security.md, zero-data-retention.md) | 6.0/6 (explicit; authentication.md) | 6.0/6 (explicit; agent-approvals-security.md, auth.md, concepts__cyber-safety.md, security.md) |
| Governance, compliance, and policy guidance | 5 | 5.0/5 (explicit; legal-and-compliance.md, server-managed-settings.md) | 5.0/5 (explicit; enterprise.md, tos-privacy.md) | 5.0/5 (explicit; enterprise__admin-setup.md, enterprise__governance.md, enterprise__managed-configuration.md) |

### Enterprise and Operations

| Feature | Weight | Claude | Gemini | Codex |
|---------|-------:|--------|--------|-------|
| Enterprise admin setup and managed controls | 4 | 4.0/4 (explicit; agent-teams.md, amazon-bedrock.md, google-vertex-ai.md, llm-gateway.md) | 4.0/4 (explicit; enterprise.md) | 4.0/4 (explicit; enterprise__admin-setup.md, enterprise__governance.md, enterprise__managed-configuration.md) |
| Pricing, quota, and cost transparency | 3 | 3.0/3 (explicit; costs.md) | 3.0/3 (explicit; quota-and-pricing.md) | 3.0/3 (explicit; pricing.md) |
| Telemetry, analytics, and monitoring | 3 | 3.0/3 (explicit; analytics.md, monitoring-usage.md) | 3.0/3 (explicit; telemetry.md) | 1.8/3 (implied; agent-approvals-security.md, app-server.md, app.md, app__automations.md) |

## Reliability Notes

### Claude (5.0/5)
- No reliability penalties detected

### Gemini (3.0/5)
- URL-to-filename collisions detected: 4

### Codex (5.0/5)
- No reliability penalties detected

## Scoring Method

- Explicit evidence: full points for a feature
- Strong implied evidence: 60% of feature points
- No evidence: 0 points
- Category weights and thresholds are defined in `DOCS_COMPARISON_RUBRIC.md`
