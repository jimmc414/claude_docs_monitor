# Claude Docs Monitor Report

*Generated: 2026-02-27 05:33:32 UTC*

| Metric | Count |
|--------|------:|
| Changed | 6 |
| Added | 0 |
| Removed | 0 |
| Errors | 0 |

## Diffs

### https://code.claude.com/docs/en/plugins.md

```diff
--- a/https://code.claude.com/docs/en/plugins.md
+++ b/https://code.claude.com/docs/en/plugins.md
@@ -314,6 +314,13 @@
 
 Once your plugin is in a marketplace, others can install it using the instructions in [Discover and install plugins](/en/discover-plugins).
 
+### Submit your plugin to the official marketplace
+
+To submit a plugin to the official Anthropic marketplace, use one of the in-app submission forms:
+
+* **Claude.ai**: [claude.ai/settings/plugins/submit](https://claude.ai/settings/plugins/submit)
+* **Console**: [platform.claude.com/plugins/submit](https://platform.claude.com/plugins/submit)
+
 <Note>
   For complete technical specifications, debugging techniques, and distribution strategies, see [Plugins reference](/en/plugins-reference).
 </Note>

```
### https://code.claude.com/docs/en/model-config.md

```diff
--- a/https://code.claude.com/docs/en/model-config.md
+++ b/https://code.claude.com/docs/en/model-config.md
@@ -140,6 +140,8 @@
 
 Effort is currently supported on Opus 4.6. The effort slider appears in `/model` when a supported model is selected.
 
+To disable adaptive reasoning on Opus 4.6 and Sonnet 4.6 and revert to the previous fixed thinking budget, set `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1`. When disabled, these models use the fixed budget controlled by `MAX_THINKING_TOKENS`. See [environment variables](/en/settings#environment-variables).
+
 ### Extended context
 
 Opus 4.6 and Sonnet 4.6 support a [1 million token context window](https://platform.claude.com/docs/en/build-with-claude/context-windows#1m-token-context-window) for long sessions with large codebases.

```
### https://code.claude.com/docs/en/settings.md

```diff
--- a/https://code.claude.com/docs/en/settings.md
+++ b/https://code.claude.com/docs/en/settings.md
@@ -779,9 +779,11 @@
 | `CLAUDE_CODE_CLIENT_KEY`                       | Path to client private key file for mTLS authentication                                                                                                                                                                                                                                                                                                                                                                                                                                               |     |
 | `CLAUDE_CODE_CLIENT_KEY_PASSPHRASE`            | Passphrase for encrypted CLAUDE\_CODE\_CLIENT\_KEY (optional)                                                                                                                                                                                                                                                                                                                                                                                                                                         |     |
 | `CLAUDE_CODE_DISABLE_1M_CONTEXT`               | Set to `1` to disable [1M context window](/en/model-config#extended-context) support. When set, 1M model variants are unavailable in the model picker. Useful for enterprise environments with compliance requirements                                                                                                                                                                                                                                                                                |     |
+| `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING`        | Set to `1` to disable [adaptive reasoning](/en/model-config#adjust-effort-level) for Opus 4.6 and Sonnet 4.6. When disabled, these models fall back to the fixed thinking budget controlled by `MAX_THINKING_TOKENS`                                                                                                                                                                                                                                                                                  |     |
 | `CLAUDE_CODE_DISABLE_AUTO_MEMORY`              | Set to `1` to disable [auto memory](/en/memory#auto-memory). Set to `0` to force auto memory on during the gradual rollout. When disabled, Claude does not create or load auto memory files                                                                                                                                                                                                                                                                                                           |     |
 | `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS`         | Set to `1` to disable all background task functionality, including the `run_in_background` parameter on Bash and subagent tools, auto-backgrounding, and the Ctrl+B shortcut                                                                                                                                                                                                                                                                                                                          |     |
 | `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS`       | Set to `1` to disable Anthropic API-specific `anthropic-beta` headers. Use this if experiencing issues like "Unexpected value(s) for the `anthropic-beta` header" when using an LLM gateway with third-party providers                                                                                                                                                                                                                                                                                |     |
+| `CLAUDE_CODE_DISABLE_FAST_MODE`                | Set to `1` to disable [fast mode](/en/fast-mode)                                                                                                                                                                                                                                                                                                                                                                                                                                                      |     |
 | `CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY`          | Set to `1` to disable the "How is Claude doing?" session quality surveys. Also disabled when using third-party providers or when telemetry is disabled. See [Session quality surveys](/en/data-usage#session-quality-surveys)                                                                                                                                                                                                                                                                         |     |
 | `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`     | Equivalent of setting `DISABLE_AUTOUPDATER`, `DISABLE_BUG_COMMAND`, `DISABLE_ERROR_REPORTING`, and `DISABLE_TELEMETRY`                                                                                                                                                                                                                                                                                                                                                                                |     |
 | `CLAUDE_CODE_DISABLE_TERMINAL_TITLE`           | Set to `1` to disable automatic terminal title updates based on conversation context                                                                                                                                                                                                                                                                                                                                                                                                                  |     |

```
### https://code.claude.com/docs/en/discover-plugins.md

```diff
--- a/https://code.claude.com/docs/en/discover-plugins.md
+++ b/https://code.claude.com/docs/en/discover-plugins.md
@@ -37,7 +37,12 @@
 ```
 
 <Note>
-  The official marketplace is maintained by Anthropic. To distribute your own plugins, [create your own marketplace](/en/plugin-marketplaces) and share it with users.
+  The official marketplace is maintained by Anthropic. To submit a plugin to the official marketplace, use one of the in-app submission forms:
+
+  * **Claude.ai**: [claude.ai/settings/plugins/submit](https://claude.ai/settings/plugins/submit)
+  * **Console**: [platform.claude.com/plugins/submit](https://platform.claude.com/plugins/submit)
+
+  To distribute plugins independently, [create your own marketplace](/en/plugin-marketplaces) and share it with users.
 </Note>
 
 The official marketplace includes several categories of plugins:

```
### https://code.claude.com/docs/en/common-workflows.md

```diff
--- a/https://code.claude.com/docs/en/common-workflows.md
+++ b/https://code.claude.com/docs/en/common-workflows.md
@@ -540,7 +540,7 @@
 
 **With other models**, thinking uses a fixed budget of up to 31,999 tokens from your output budget. You can limit this with the [`MAX_THINKING_TOKENS`](/en/settings#environment-variables) environment variable, or disable thinking entirely via `/config` or the `Option+T`/`Alt+T` toggle.
 
-`MAX_THINKING_TOKENS` is ignored when using Opus 4.6, since adaptive reasoning controls thinking depth instead. The one exception: setting `MAX_THINKING_TOKENS=0` still disables thinking entirely on any model.
+`MAX_THINKING_TOKENS` is ignored on Opus 4.6 and Sonnet 4.6, since adaptive reasoning controls thinking depth instead. The one exception: setting `MAX_THINKING_TOKENS=0` still disables thinking entirely on any model. To disable adaptive thinking and revert to the fixed thinking budget, set `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1`. See [environment variables](/en/settings#environment-variables).
 
 <Warning>
   You're charged for all thinking tokens used, even though Claude 4 models show summarized thinking

```
### https://code.claude.com/docs/en/fast-mode.md

```diff
--- a/https://code.claude.com/docs/en/fast-mode.md
+++ b/https://code.claude.com/docs/en/fast-mode.md
@@ -103,6 +103,8 @@
 * **Console** (API customers): [Claude Code preferences](https://platform.claude.com/claude-code/preferences)
 * **Claude AI** (Teams and Enterprise): [Admin Settings > Claude Code](https://claude.ai/admin-settings/claude-code)
 
+Another option to disable fast mode entirely is to set `CLAUDE_CODE_DISABLE_FAST_MODE=1`. See [Environment variables](/en/settings#environment-variables).
+
 ## Handle rate limits
 
 Fast mode has separate rate limits from standard Opus 4.6. When you hit the fast mode rate limit or run out of extra usage credits:

```
