# Codex Docs Monitor History

## 2026-03-07 04:18:08 UTC

**First run: 68 pages snapshotted.**

- https://developers.openai.com/codex/llms-full.txt
- https://developers.openai.com/codex/agent-approvals-security.md
- https://developers.openai.com/codex/app.md
- https://developers.openai.com/codex/app/automations.md
- https://developers.openai.com/codex/app/commands.md
- https://developers.openai.com/codex/app/features.md
- https://developers.openai.com/codex/app/settings.md
- https://developers.openai.com/codex/app/local-environments.md
- https://developers.openai.com/codex/app/review.md
- https://developers.openai.com/codex/app/troubleshooting.md
- https://developers.openai.com/codex/app/windows.md
- https://developers.openai.com/codex/app/worktrees.md
- https://developers.openai.com/codex/app-server.md
- https://developers.openai.com/codex/auth.md
- https://developers.openai.com/codex/cli.md
- https://developers.openai.com/codex/cli/features.md
- https://developers.openai.com/codex/cli/reference.md
- https://developers.openai.com/codex/cli/slash-commands.md
- https://developers.openai.com/codex/cloud.md
- https://developers.openai.com/codex/cloud/internet-access.md
- https://developers.openai.com/codex/cloud/environments.md
- https://developers.openai.com/codex/community/codex-for-oss.md
- https://developers.openai.com/codex/concepts/customization.md
- https://developers.openai.com/codex/concepts/cyber-safety.md
- https://developers.openai.com/codex/concepts/multi-agents.md
- https://developers.openai.com/codex/concepts/sandboxing.md
- https://developers.openai.com/codex/config-advanced.md
- https://developers.openai.com/codex/config-basic.md
- https://developers.openai.com/codex/config-reference.md
- https://developers.openai.com/codex/config-sample.md
- https://developers.openai.com/codex/custom-prompts.md
- https://developers.openai.com/codex/enterprise/admin-setup.md
- https://developers.openai.com/codex/enterprise/governance.md
- https://developers.openai.com/codex/enterprise/managed-configuration.md
- https://developers.openai.com/codex/explore.md
- https://developers.openai.com/codex/feature-maturity.md
- https://developers.openai.com/codex/github-action.md
- https://developers.openai.com/codex/guides/build-ai-native-engineering-team.md
- https://developers.openai.com/codex/guides/agents-md.md
- https://developers.openai.com/codex/guides/agents-sdk.md
- https://developers.openai.com/codex/ide.md
- https://developers.openai.com/codex/ide/commands.md
- https://developers.openai.com/codex/ide/features.md
- https://developers.openai.com/codex/ide/settings.md
- https://developers.openai.com/codex/ide/slash-commands.md
- https://developers.openai.com/codex/integrations/github.md
- https://developers.openai.com/codex/integrations/linear.md
- https://developers.openai.com/codex/integrations/slack.md
- https://developers.openai.com/codex/mcp.md
- https://developers.openai.com/codex/models.md
- https://developers.openai.com/codex/multi-agent.md
- https://developers.openai.com/codex/noninteractive.md
- https://developers.openai.com/codex/open-source.md
- https://developers.openai.com/codex/overview.md
- https://developers.openai.com/codex/pricing.md
- https://developers.openai.com/codex/prompting.md
- https://developers.openai.com/codex/quickstart.md
- https://developers.openai.com/codex/rules.md
- https://developers.openai.com/codex/sdk.md
- https://developers.openai.com/codex/security.md
- https://developers.openai.com/codex/security/setup.md
- https://developers.openai.com/codex/security/faq.md
- https://developers.openai.com/codex/security/threat-model.md
- https://developers.openai.com/codex/skills.md
- https://developers.openai.com/codex/speed.md
- https://developers.openai.com/codex/videos.md
- https://developers.openai.com/codex/windows.md
- https://developers.openai.com/codex/workflows.md

---

## 2026-05-10 19:58:44 UTC

| Metric | Count |
|--------|------:|
| Changed | 44 |
| Added | 13 |
| Removed | 3 |
| Errors | 0 |

### Added Pages

- https://developers.openai.com/codex/app/browser.md
- https://developers.openai.com/codex/app/chrome-extension.md
- https://developers.openai.com/codex/app/computer-use.md
- https://developers.openai.com/codex/concepts/subagents.md
- https://developers.openai.com/codex/hooks.md
- https://developers.openai.com/codex/learn/best-practices.md
- https://developers.openai.com/codex/memories.md
- https://developers.openai.com/codex/memories/chronicle.md
- https://developers.openai.com/codex/migrate.md
- https://developers.openai.com/codex/plugins.md
- https://developers.openai.com/codex/plugins/build.md
- https://developers.openai.com/codex/remote-connections.md
- https://developers.openai.com/codex/subagents.md

### Removed Pages

- https://developers.openai.com/codex/concepts/multi-agents.md
- https://developers.openai.com/codex/explore.md
- https://developers.openai.com/codex/multi-agent.md

### Diffs

#### https://developers.openai.com/codex/llms-full.txt

```diff
--- a/https://developers.openai.com/codex/llms-full.txt
+++ b/https://developers.openai.com/codex/llms-full.txt
@@ -15,7 +15,8 @@
 By default, the agent runs with network access turned off. Locally, Codex uses an OS-enforced sandbox that limits what it can touch (typically to the current workspace), plus an approval policy that controls when it must stop and ask you before acting.
 
 For a high-level explanation of how sandboxing works across the Codex app, IDE
-extension, and CLI, see [Sandboxing](https://developers.openai.com/codex/concepts/sandboxing).
+extension, and CLI, see [sandboxing](https://developers.openai.com/codex/concepts/sandboxing).
+For a broader enterprise security overview, see the [Codex security white paper](https://trust.openai.com/?itemUid=382f924d-54f3-43a8-a9df-c39e6c959958&source=click).
 
 ## Sandbox and approvals
 
@@ -29,7 +30,7 @@
 - **Codex cloud**: Runs in isolated OpenAI-managed containers, preventing access to your host system or unrelated data. Uses a two-phase runtime model: setup runs before the agent phase and can access the network to install specified dependencies, then the agent phase runs offline by default unless you enable internet access for that environment. Secrets configured for cloud environments are available only during setup and are removed before the agent phase starts.
 - **Codex CLI / IDE extension**: OS-level mechanisms enforce sandbox policies. Defaults include no network access and write permissions limited to the active workspace. You can configure the sandbox, approval policy, and network settings based on your risk tolerance.
 
-In the `Auto` preset (for example, `--full-auto`), Codex can read files, make edits, and run commands in the working directory automatically.
+In the `Auto` preset (for example, `--sandbox workspace-write --ask-for-approval on-request`), Codex can read files, make edits, and run commands in the working directory automatically.
 
 Codex asks for approval to edit files outside the workspace or to run commands that require network access. If you want to chat or plan without making changes, switch to `read-only` mode with the `/permissions` command.
 
@@ -76,6 +77,26 @@
 - `<writable_root>/.codex` is protected as read-only when it exists as a directory.
 - Protection is recursive, so everything under those paths is read-only.
 
+### Deny reads with filesystem profiles
+
+Named permission profiles can also deny reads for exact paths or glob patterns.
+This is useful when a workspace should stay writable but specific sensitive
+files, such as local environment files, must stay unreadable:
+
+```toml
+default_permissions = "workspace"
+
+[permissions.workspace.filesystem]
+":project_roots" = { "." = "write", "**/*.env" = "none" }
+glob_scan_max_depth = 3
+```
+
+Use `"none"` for paths or globs that Codex shouldn't read. The sandbox policy
+evaluates globs for local macOS and Linux command execution. On platforms that
+pre-expand glob matches before the sandbox starts, set `glob_scan_max_depth` for
+unbounded `**` patterns, or list explicit depths such as `*.env`, `*/*.env`, and
+`*/*/*.env`.
+
 ### Run without approval prompts
 
 You can disable approval prompts with `--ask-for-approval never` or `-a never` (shorthand).
@@ -84,19 +105,62 @@
 
 If you need Codex to read files, make edits, and run commands with network access without approval prompts, use `--sandbox danger-full-access` (or the `--dangerously-bypass-approvals-and-sandbox` flag). Use caution before doing so.
 
-For a middle ground, `approval_policy = { reject = { ... } }` lets you auto-reject specific approval prompt categories (sandbox escalation, execpolicy-rule prompts, or MCP elicitations) while keeping other prompts interactive.
+For a middle ground, `approval_policy = { granular = { ... } }` lets you keep specific approval prompt categories interactive while automatically rejecting others. The granular policy covers sandbox approvals, execpolicy-rule prompts, MCP prompts, `request_permissions` prompts, and skill-script approvals.
+
+### Automatic approval reviews
+
+By default, approval requests route to you:
+
+```toml
+approvals_reviewer = "user"
+```
+
+Automatic approval reviews apply when approvals are interactive, such as
+`approval_policy = "on-request"` or a granular approval policy. Set
+`approvals_reviewer = "auto_review"` to route eligible approval requests
+through a reviewer agent before Codex runs the request:
+
+```toml
+approval_policy = "on-request"
+approvals_reviewer = "auto_review"
+```
+
+The reviewer evaluates only actions that already need approval, such as sandbox
+escalations, network requests, `request_permissions` prompts, or side-effecting
+app and MCP tool calls. Actions that stay inside the sandbox continue without an
+extra review step.
+
+The reviewer policy checks for data exfiltration, credential probing, persistent
+security weakening, and destructive actions. Low-risk and medium-risk actions
+can proceed when policy allows them. The policy denies critical-risk actions.
+High-risk actions require enough user authorization and no matching deny rule.
+Timeouts, parse failures, and review errors fail closed.
+
+The [default reviewer policy](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md)
+is in the open-source Codex repository. Enterprises can replace its
+tenant-specific section with `guardian_policy_config` in managed requirements.
+Local `[auto_review].policy` text is also supported, but managed requirements
+take precedence. For setup details, see
+[Managed configuration](https://developers.openai.com/codex/enterprise/managed-configuration#configure-automatic-review-policy).
+
+In the Codex app, these reviews appear as automatic review items with a status such
+as Reviewing, Approved, Denied, Stopped, or Timed out. They can also include a
+risk level for the reviewed request.
+
+Automatic review uses extra model calls, so it can add to Codex usage. Admins
+can constrain it with `allowed_approvals_reviewers`.
 
 ### Common sandbox and approval combinations
 
-| Intent                                                            | Flags                                                          | Effect                                                                                                                                           |
-| ----------------------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
-| Auto (preset)                                                     | _no flags needed_ or `--full-auto`                             | Codex can read files, make edits, and run commands in the workspace. Codex requires approval to edit outside the workspace or to access network. |
-| Safe read-only browsing                                           | `--sandbox read-only --ask-for-approval on-request`            | Codex can read files and answer questions. Codex requires approval to make edits, run commands, or access network.                               |
-| Read-only non-interactive (CI)                                    | `--sandbox read-only --ask-for-approval never`                 | Codex can only read files; never asks for approval.                                                                                              |
-| Automatically edit but ask for approval to run untrusted commands | `--sandbox workspace-write --ask-for-approval untrusted`       | Codex can read and edit files but asks for approval before running untrusted commands.                                                           |
-| Dangerous full access                                             | `--dangerously-bypass-approvals-and-sandbox` (alias: `--yolo`) | No sandbox; no approvals _(not recommended)_                                                                               |
-
-`--full-auto` is a convenience alias for `--sandbox workspace-write --ask-for-approval on-request`.
+| Intent                                                            | Flags                                                                          | Effect                                                                                                                                           |
+| ----------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
+| Auto (preset)                                                     | _no flags needed_ or `--sandbox workspace-write --ask-for-approval on-request` | Codex can read files, make edits, and run commands in the workspace. Codex requires approval to edit outside the workspace or to access network. |
+| Safe read-only browsing                                           | `--sandbox read-only --ask-for-approval on-request`                            | Codex can read files and answer questions. Codex requires approval to make edits, run commands, or access network.                               |
+| Read-only non-interactive (CI)                                    | `--sandbox read-only --ask-for-approval never`                                 | Codex can only read files; never asks for approval.                                                                                              |
+| Automatically edit but ask for approval to run untrusted commands | `--sandbox workspace-write --ask-for-approval untrusted`                       | Codex can read and edit files but asks for approval before running untrusted commands.                                                           |
+| Dangerous full access                                             | `--dangerously-bypass-approvals-and-sandbox` (alias: `--yolo`)                 | No sandbox; no approvals _(not recommended)_                                                                               |
+
+For non-interactive runs, use `codex exec --sandbox workspace-write`; Codex keeps older `codex exec --full-auto` invocations as a deprecated compatibility path and prints a warning.
 
 With `--ask-for-approval untrusted`, Codex runs only known-safe read operations automatically. Commands that can mutate state or trigger external execution paths (for example, destructive Git operations or Git output/config-override flags) require approval.
 
@@ -114,8 +178,14 @@
 [sandbox_workspace_write]
 network_access = true
 
-# Optional: granular approval prompt auto-rejection
-# approval_policy = { reject = { sandbox_approval = true, rules = false, mcp_elicitations = false } }
+# Optional: granular approval policy
+# approval_policy = { granular = {
+#   sandbox_approval = true,
+#   rules = true,
+#   mcp_elicitations = true,
+#   request_permissions = false,
+#   skill_approval = false
+# } }
 ```
 
 You can also save presets as profiles, then select them with `codex --profile <name>`:
@@ -136,9 +206,11 @@
 
 ```bash
 # macOS
-codex sandbox macos [--full-auto] [--log-denials] [COMMAND]...
+codex sandbox macos [--permissions-profile <name>] [--log-denials] [COMMAND]...
 # Linux
-codex sandbox linux [--full-auto] [COMMAND]...
+codex sandbox linux [--permissions-profile <name>] [COMMAND]...
+# Windows
+codex sandbox windows [--permissions-profile <name>] [COMMAND]...
 ```
 
 The `sandbox` command is also available as `codex debug`, and the platform helpers have aliases (for example `codex sandbox seatbelt` and `codex sandbox landlock`).
@@ -148,10 +220,10 @@
 Codex enforces the sandbox differently depending on your OS:
 
 - **macOS** uses Seatbelt policies and runs commands using `sandbox-exec` with a profile (`-p`) that corresponds to the `--sandbox` mode you selected. When restricted read access enables platform defaults, Codex appends a curated macOS platform policy (instead of broadly allowing `/System`) to preserve common tool compatibility.
-- **Linux** uses `Landlock` plus `seccomp` by default. You can opt into the alternative Linux sandbox pipeline with `features.use_linux_sandbox_bwrap = true` (or `-c use_linux_sandbox_bwrap=true`). In managed proxy mode, the bwrap pipeline routes egress through a proxy-only bridge and fails closed if it cannot build valid loopback proxy routes; landlock-only flows do not use that bridge behavior.
-- **Windows** uses the Linux sandbox implementation when running in [Windows Subsystem for Linux (WSL)](https://developers.openai.com/codex/windows#windows-subsystem-for-linux). When running natively on Windows, Codex uses a [Windows sandbox](https://developers.openai.com/codex/windows#windows-sandbox) implementation.
-
-If you use the Codex IDE extension on Windows, it supports WSL directly. Set the following in your VS Code settings to keep the agent inside WSL whenever it's available:
+- **Linux** uses `bwrap` plus `seccomp` by default.
+- **Windows** uses the Linux sandbox implementation when running in [Windows Subsystem for Linux 2 (WSL2)](https://developers.openai.com/codex/windows#windows-subsystem-for-linux). WSL1 was supported through Codex `0.114`; starting in `0.115`, the Linux sandbox moved to `bwrap`, so WSL1 is no longer supported. When running natively on Windows, Codex uses a [Windows sandbox](https://developers.openai.com/codex/windows#windows-sandbox) implementation.
+
+If you use the Codex IDE extension on Windows, it supports WSL2 directly. Set the following in your VS Code settings to keep the agent inside WSL2 whenever it's available:
 
 ```json
 {
@@ -166,13 +238,61 @@
 ```toml
 [windows]
 sandbox = "unelevated" # or "elevated"
+# sandbox_private_desktop = true  # default; set false only for compatibility
 ```
 
 See the [Windows setup guide](https://developers.openai.com/codex/windows#windows-sandbox) for details.
 
-When you run Linux in a containerized environment such as Docker, the sandbox may not work if the host or container configuration doesn't support the required `Landlock` and `seccomp` features.
+When you run Linux in a containerized environment such as Docker, the sandbox may not work if the host or container configuration blocks the namespace, setuid `bwrap`, or `seccomp` operations that Codex needs.
 
 In that case, configure your Docker container to provide the isolation you need, then run `codex` with `--sandbox danger-full-access` (or the `--dangerously-bypass-approvals-and-sandbox` flag) inside the container.
+
+### Run Codex in Dev Containers
+
+If your host cannot run the Linux sandbox directly, or if your organization already standardizes on containerized development, run Codex with Dev Containers and let Docker provide the outer isolation boundary. This works with Visual Studio Code Dev Containers and compatible tools.
+
+Use the [Codex secure devcontainer example](https://github.com/openai/codex/tree/main/.devcontainer) as a reference implementation. The example installs Codex, common development tools, `bubblewrap`, and firewall-based outbound controls.
+
+Devcontainers provide substantial protection, but they do not prevent every
+  attack. If you run Codex with `--sandbox danger-full-access` or
+  `--dangerously-bypass-approvals-and-sandbox` inside the container, a malicious
+  project can exfiltrate anything available inside the devcontainer, including
+  Codex credentials. Use this pattern only with trusted repositories, and
+  monitor Codex activity as you would in any other elevated environment.
+
+The reference implementation includes:
+
+- an Ubuntu 24.04 base image with Codex and common development tools installed;
+- an allowlist-driven firewall profile for outbound access;
+- VS Code settings and extension recommendations for reopening the workspace in a container;
+- persistent mounts for command history and Codex configuration;
+- `bubblewrap`, so Codex can still use its Linux sandbox when the container grants the needed capabilities.
+
+To try it:
+
+1. Install Visual Studio Code and the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
+2. Copy the Codex example `.devcontainer` setup into your repository, or start from the Codex repository directly.
+3. In VS Code, run **Dev Containers: Open Folder in Container...** and select `.devcontainer/devcontainer.secure.json`.
+4. After the container starts, open a terminal and run `codex`.
+
+You can also start the container from the CLI:
+
+```bash
+devcontainer up --workspace-folder . --config .devcontainer/devcontainer.secure.json
+```
+
+The example has three main pieces:
+
+- `.devcontainer/devcontainer.secure.json` controls container settings, capabilities, mounts, environment variables, and VS Code extensions.
+- `.devcontainer/Dockerfile.secure` defines the Ubuntu-based image and installed tools.
+- `.devcontainer/init-firewall.sh` applies the outbound network policy.
+
+The reference firewall is intentionally a starting point. If you depend on domain allowlisting for isolation, implement DNS rebinding and DNS refresh protections that fit your environment, such as TTL-aware refreshes or a DNS-aware firewall.
+
+Inside the container, choose one of these modes:
+
+- Keep Codex's Linux sandbox enabled if the Dev Container profile grants the capabilities needed for `bwrap` to create the inner sandbox.
+- If the container is your intended security boundary, run Codex with `--sandbox danger-full-access` inside the container so Codex does not try to create a second sandbox layer.
 
 ## Version control
 
@@ -268,13 +388,16 @@
 
 ## Getting started
 
-The Codex app is available on macOS (Apple Silicon).
+The Codex app is available on macOS and Windows.
+
+Most Codex app features are available on both platforms. Platform-specific
+exceptions are noted in the relevant docs.
 
 
 
 1. Download and install the Codex app
 
-    Download the Codex app for Windows or macOS.
+    Download the Codex app for macOS or Windows. Choose the Intel build if you're using an Intel-based Mac.
 
     <div class="text-sm">
       [Get notified for Linux](https://openai.com/form/codex-app/)
@@ -301,7 +424,8 @@
    <ExampleGallery>
      </ExampleGallery>
 
-   If you need more inspiration, check out the [explore section](https://developers.openai.com/codex/explore).
+   If you need more inspiration, explore [Codex use cases](https://developers.openai.com/codex/use-cases).
+   If you're new to Codex, read the [best practices guide](https://developers.openai.com/codex/learn/best-practices).
 
 
 
@@ -315,65 +439,93 @@
 
 ### Multitask across projects
 
-Run multiple tasks in parallel and switch quickly between them.
-
-  </BentoContent>
-  <BentoContent href="/codex/app/features#built-in-git-tools">
-
-### Built-in Git tools
-
-Review diffs, comment inline, stage or revert chunks, and commit without leaving the app.
+Run project threads side by side and switch between them quickly.
 
   </BentoContent>
   <BentoContent href="/codex/app/worktrees">
 
-### Worktrees for parallel tasks
-
-Isolate changes of multiple Codex threads using built-in Git worktree support.
+### Worktrees
+
+Keep parallel code changes isolated with built-in Git worktree support.
+
+  </BentoContent>
+  <BentoContent href="/codex/app/computer-use">
+
+### Computer use
+
+Let Codex use macOS apps for GUI tasks, browser flows, and native app testing.
+
+  </BentoContent>
+  <BentoContent href="/codex/app/review">
+
+### Review and ship changes
+
+Inspect diffs, address PR feedback, stage files, commit, and push.
+
+  </BentoContent>
+  <BentoContent href="/codex/app/features#integrated-terminal">
+
+### Terminal and actions
+
+Run commands in each thread and launch repeatable project actions.
+
+  </BentoContent>
+  <BentoContent href="/codex/app/browser">
+
+### In-app browser
+
+Open rendered pages, leave comments, or let Codex operate local browser flows.
+
+  </BentoContent>
+  <BentoContent href="/codex/app/chrome-extension">
+
+### Chrome extension
+
+Add the Chrome plugin so Codex can use Chrome for signed-in browser tasks while you manage website approvals.
+
+  </BentoContent>
+  <BentoContent href="/codex/app/features#image-generation">
+
+### Image generation
+
+Generate or edit images in a thread while you work on the surrounding code and assets.
+
+  </BentoContent>
+  <BentoContent href="/codex/app/automations">
+
+### Automations
+
+Schedule recurring tasks, or wake up the same thread for ongoing checks.
 
   </BentoContent>
   <BentoContent href="/codex/app/features#skills-support">
 
-### Skills support
-
-Give your Codex agent additional capabilities and reuse skills across App, CLI, and IDE Extension.
+### Skills
+
+Reuse instructions and workflows across the app, CLI, and IDE Extension.
 
   </BentoContent>
-  <BentoContent href="/codex/app/automations">
-
-### Automations
-
-Pair skills with automations to automate recurring tasks in the background. Codex adds findings to the inbox, or automatically archives runs if there's nothing to report.
+  <BentoContent href="/codex/app/features#richer-outputs-and-artifacts">
+
+### Sidebar and artifacts
+
+Follow plans, sources, task summaries, and generated file previews.
 
   </BentoContent>
-  <BentoContent href="/codex/app/features#integrated-terminal">
-
-### Built-in terminal
-
-Open a terminal per thread to test your changes, run dev servers, scripts, and custom commands.
-
-  </BentoContent>
-  <BentoContent href="/codex/app/local-environments">
-
-### Local environments
-
-Define worktree setup scripts and common project actions for easy access.
+  <BentoContent href="/codex/plugins">
+
+### Plugins
+
+Connect apps, skills, and MCP servers to extend what Codex can do.
 
   </BentoContent>
   <BentoContent href="/codex/app/features#sync-with-the-ide-extension">
 
-### Sync with the IDE extension
+### IDE Extension sync
 
 Share Auto Context and active threads across app and IDE sessions.
 
   </BentoContent>
-  <BentoContent href="/codex/app/features#mcp-support">
-
-### MCP support
-
-Connect your Codex agent to additional services using MCP.
-
-  </BentoContent>
 
 
 
@@ -391,52 +543,116 @@
 
 Automate recurring tasks in the background. Codex adds findings to the inbox, or automatically archives the task if there's nothing to report. You can combine automations with [skills](https://developers.openai.com/codex/skills) for more complex tasks.
 
-Automations run locally in the Codex app. The app needs to be running, and the
-selected project needs to be available on disk.
-
-In Git repositories, each automation run starts in a new
-[worktree](https://developers.openai.com/codex/app/worktrees) so it doesn't interfere with your main
-checkout. In non-version-controlled projects, automations run directly in the
+For project-scoped automations, the app needs to be running, and the selected
+project needs to be available on disk.
+
+In Git repositories, you can choose whether an automation runs in your local
+project or on a new [worktree](https://developers.openai.com/codex/app/worktrees). Both options run in the
+background. Worktrees keep automation changes separate from unfinished local
+work, while running in your local project can modify files you are still
+working on. In non-version-controlled projects, automations run directly in the
 project directory.
 
+You can also leave the model and reasoning effort on their default settings, or
+choose them explicitly if you want more control over how the automation runs.
+
 </div>
 
 </div>
 
 ## Managing tasks
 
-All automations and their runs can be found in the automations pane inside your Codex app sidebar.
+Find all automations and their runs in the automations pane inside your Codex app sidebar.
 
 The "Triage" section acts as your inbox. Automation runs with findings show up there, and you can filter your inbox to show all automation runs or only unread ones.
 
-When an automation runs in a Git repository, Codex uses a dedicated background [worktree](https://developers.openai.com/codex/app/features#worktree-support). In non-version-controlled projects, automations run directly in the project directory. Consider using Git to enable running on background worktrees. You can have the same automation run on multiple projects.
+Standalone automations start fresh runs on a schedule and report results in
+Triage. Use them when each run should be independent or when one automation
+should run across one or more projects. If you need a custom cadence, choose a
+custom schedule and enter cron syntax.
+
+For Git repositories, each automation can run either in your local project or
+on a dedicated background [worktree](https://developers.openai.com/codex/app/features#worktree-support). Use
+worktrees when you want to isolate automation changes from unfinished local
+work. Use local mode when you want the automation to work directly in your main
+checkout, keeping in mind that it can change files you are actively editing.
+In non-version-controlled projects, automations run directly in the project
+directory. You can have the same automation run on more than one project.
 
 Automations use your default sandbox settings. In read-only mode, tool calls fail if they require modifying files, network access, or working with apps on your computer. With full access enabled, background automations carry elevated risk. You can adjust sandbox settings in [Settings](https://developers.openai.com/codex/app/settings) and selectively allowlist commands with [rules](https://developers.openai.com/codex/rules).
 
-To keep automations maintainable and shareable across teams, you can use [skills](https://developers.openai.com/codex/skills) to define the action and provide tools and context to Codex. You can explicitly trigger a skill as part of an automation by using `$skill-name` inside your automation.
-
-## Testing automations safely
+Automations can use the same plugins and skills available to Codex. To keep
+automations maintainable and shareable across teams, use [skills](https://developers.openai.com/codex/skills)
+to define the action and provide tools and context. You can explicitly trigger a
+skill as part of an automation by using `$skill-name` inside your automation.
+
+## Ask Codex to create or update automations
+
+You can create and update automations from a regular Codex thread. Describe the
+task, the schedule, and whether the automation should stay attached to the
+current thread or start fresh runs. Codex can draft the automation prompt, choose
+the right automation type, and update it when the scope or cadence changes.
+
+For example, ask Codex to remind you in this thread while a deployment finishes,
+or ask it to create a standalone automation that checks a project on a recurring
+schedule.
+
+Skills can also create or update automations. For example, a skill for
+babysitting a pull request could set up a recurring automation that checks the
+PR status with the GitHub plugin and fixes new review feedback.
+
+## Thread automations
+
+Thread automations are heartbeat-style recurring wake-up calls attached to the
+current thread. Use them when you want Codex to keep returning to the same
+conversation on a schedule.
+
+Use a thread automation when the scheduled work should preserve the thread's
+context instead of starting from a new prompt each time.
+
+Thread automations can use minute-based intervals for active follow-up loops,
+or daily and weekly schedules when you need a check-in at a specific time.
+
+Thread automations are useful for:
+
+- checking a long-running command until it finishes
+- polling Slack, GitHub, or another connected source when the results should
+  stay in the same thread
+- reminding Codex to continue a review loop at a fixed cadence
+- running a skill-driven workflow that uses plugins, such as checking PR status
+  and addressing new feedback
+- keeping a chat focused on an ongoing research or triage task
+
+Use a standalone or project automation when each run should be independent,
+when it should run across more than one project, or when findings should appear
+as separate automation runs in Triage.
+
+When you create a thread automation, make the prompt durable. It should
+describe what Codex should do each time the thread wakes up, how to decide
+whether there is anything important to report, and when to stop or ask you for
+input.
+
+## Test automations
 
 Before you schedule an automation, test the prompt manually in a regular thread
 first. This helps you confirm:
 
 - The prompt is clear and scoped correctly.
-- The selected model and tools behave as expected.
+- The selected or default model, reasoning effort, and tools behave as expected.
 - The resulting diff is reviewable.
 
-When you start scheduling runs, review the first few outputs closely and adjust
-the prompt or cadence as needed.
+When you start scheduling runs, review the first few outputs and adjust the
+prompt or cadence as needed.
 
 ## Worktree cleanup for automations
 
-For Git repositories, automations run in worktrees. Frequent schedules can
-create many worktrees over time. Archive automation runs you no longer need,
-and avoid pinning runs unless you intend to keep their worktrees.
+If you choose worktrees for Git repositories, frequent schedules can create
+many worktrees over time. Archive automation runs you no longer need, and avoid
+pinning runs unless you intend to keep their worktrees.
 
 ## Permissions and security model
 
-Automations are designed to run unattended and use your default sandbox
-settings.
+Automations run unattended and use your default sandbox settings.
 
 - If your sandbox mode is **read-only**, tool calls fail if they require
   modifying files, accessing network, or working with apps on your computer.
@@ -446,7 +662,7 @@
   on your computer. You can selectively allowlist commands to run outside the
   sandbox using [rules](https://developers.openai.com/codex/rules).
 - If your sandbox mode is **full access**, background automations carry
-  elevated risk, as Codex may modify files, run commands, and access network
+  elevated risk, as Codex may change files, run commands, and access network
   without asking. Consider updating sandbox settings to workspace write, and
   using [rules](https://developers.openai.com/codex/rules) to selectively define which commands the agent
   can run with full access.
@@ -457,7 +673,7 @@
 [Admin-enforced requirements (`requirements.toml`)](https://developers.openai.com/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml).
 
 Automations use `approval_policy = "never"` when your organization policy
-allows it. If `approval_policy = "never"` is disallowed by admin requirements,
+allows it. If admin requirements disallow `approval_policy = "never"`,
 automations fall back to the approval behavior of your selected mode.
 
 ## Examples
@@ -603,7 +819,7 @@
 
 You can also explicitly invoke skills by typing `$` in the thread composer. See [Skills](https://developers.openai.com/codex/skills).
 
-Enabled skills also appear in the slash command list (for example, `/imagegen`).
+Enabled skills also appear in the slash command list.
 
 ### Available slash commands
 
@@ -615,6 +831,24 @@
 | `/review`     | Start code review mode to review uncommitted changes or compare against a base branch. |
 | `/status`     | Show the thread ID, context usage, and rate limits.                                    |
 
+## Deeplinks
+
+The Codex app registers the `codex://` URL scheme so links can open specific parts of the app directly.
+
+| Deeplink                      | Opens                                         | Supported query parameters               |
+| ----------------------------- | --------------------------------------------- | ---------------------------------------- |
+| `codex://settings`            | Settings.                                     | None.                                    |
+| `codex://skills`              | Skills.                                       | None.                                    |
+| `codex://automations`         | Inbox in automation create mode.              | None.                                    |
+| `codex://threads/<thread-id>` | A local thread. `<thread-id>` must be a UUID. | None.                                    |
+| `codex://new`                 | A new thread.                                 | Optional: `prompt`, `originUrl`, `path`. |
+
+For new-thread deeplinks:
+
+- `prompt` sets the initial composer text.
+- `path` must be an absolute path to a local directory and, when valid, makes that directory the active workspace for the new thread.
+- `originUrl` tries to match one of your current workspace roots by Git remote URL. If both `path` and `originUrl` are present, Codex resolves `path` first.
+
 ## See also
 
 - [Features](https://developers.openai.com/codex/app/features)
@@ -626,6 +860,9 @@
 
 The Codex app is a focused desktop experience for working on Codex threads in parallel,
 with built-in worktree support, automations, and Git functionality.
+
+Most Codex app features are available on both macOS and Windows.
+The sections below note platform-specific exceptions.
 
 ---
 
@@ -671,7 +908,8 @@
 
 You can also combine skills with [automations](https://developers.openai.com/codex/app/automations) to perform routine tasks
 such as evaluating errors in your telemetry and submitting fixes or creating reports on recent
-codebase changes.
+codebase changes. For ongoing work that should stay in one thread, use a
+[thread automation](https://developers.openai.com/codex/app/automations#thread-automations).
 
 </div>
 
@@ -749,7 +987,9 @@
 pressing <kbd>Cmd</kbd>+<kbd>J</kbd>.
 
 Use the terminal to validate changes, run scripts, and perform Git operations
-without leaving the app.
+without leaving the app. Codex can also read the current terminal output, so
+it can check the status of a running development server or refer back to a
+failed build while it works with you.
 
 Common tasks include:
 
@@ -812,6 +1052,78 @@
 
 </section>
 
+<section class="feature-grid">
+
+<div>
+
+## In-app browser
+
+Use the [in-app browser](https://developers.openai.com/codex/app/browser) to preview, review, and comment on
+local development servers, file-backed previews, and public pages that don't
+require sign-in while you iterate on a web app.
+
+The in-app browser doesn't support authentication flows, signed-in pages, your
+regular browser profile, cookies, extensions, or existing tabs.
+
+Use browser comments to mark specific elements or areas on a page, then ask
+Codex to address that feedback.
+
+When you want Codex to operate the page directly, use
+[browser use](https://developers.openai.com/codex/app/browser#browser-use) for local development servers and
+file-backed pages. You can manage the Browser plugin, allowed websites, and
+blocked websites from settings.
+
+</div>
+
+</section>
+
+<section class="feature-grid inverse">
+
+<div>
+
+## Computer use
+
+[Computer use](https://developers.openai.com/codex/app/computer-use) helps Codex operate a macOS app by
+seeing, clicking, and typing. This is useful for testing desktop apps, checking
+browser or simulator flows, working with data sources that aren't available as
+plugins, changing app settings, and reproducing GUI-only bugs.
+
+Because computer use can affect app and system state outside your project
+workspace, keep tasks narrow and review permission prompts before continuing.
+
+The feature isn't available in the European Economic Area, the United Kingdom, or
+Switzerland at launch.
+
+</div>
+
+</section>
+
+<section class="feature-grid">
+
+<div>
+
+<a id="richer-outputs-and-artifacts"></a>
+<a id="task-sidebar"></a>
+<a id="artifact-viewer"></a>
+
+## Work with non-code artifacts
+
+When a task produces non-code artifacts, the sidebar can preview PDF files,
+spreadsheets, documents, and presentations. Give Codex the source data, expected
+file type, structure, and review criteria you care about.
+
+For spreadsheets and presentations, describe the sheets, columns, charts, slide
+sections, and checks that matter. Ask Codex to explain where it saved the output
+and how it checked the result.
+
+Use the task sidebar to follow what Codex is doing while a thread runs. It can
+surface the agent's plan, sources, generated artifacts, and task summary so you
+can steer the work, inspect generated files, and decide what needs another pass.
+
+</div>
+
+</section>
+
 ---
 
 ## Sync with the IDE extension
@@ -828,6 +1140,18 @@
 If you're unsure whether the app includes context, toggle it off and ask the
 same question again to compare results.
 
+## Thread automations
+
+Automations can also attach to a single thread. These thread automations are
+recurring wake-up calls that preserve the thread's context so Codex can check
+on long-running work, poll a source for new information, or continue a follow-up
+loop. Use them for heartbeat-style automations that should keep returning to the
+same conversation on a schedule.
+
+Use a thread automation when the next run depends on the current conversation.
+Use a standalone or project [automation](https://developers.openai.com/codex/app/automations) when you want
+Codex to start a fresh recurring task for one or more projects.
+
 ## Approvals and sandboxing
 
 Your approval and sandbox settings constrain Codex actions.
@@ -846,7 +1170,12 @@
 opening separate projects or using worktrees rather than asking Codex to roam
 outside the project root.
 
-For a high-level overview, see [Sandboxing](https://developers.openai.com/codex/concepts/sandboxing). For
+If [automatic review](https://developers.openai.com/codex/agent-approvals-security#automatic-approval-reviews)
+is available in your workspace, you can choose it from the permissions selector.
+It keeps the same sandbox boundary but routes eligible approval requests through
+the configured review policy instead of waiting for you.
+
+For a high-level overview, see [sandboxing](https://developers.openai.com/codex/concepts/sandboxing). For
 configuration details, see the
 [agent approvals & security documentation](https://developers.openai.com/codex/agent-approvals-security).
 
@@ -859,12 +1188,22 @@
 
 ## Web search
 
-Codex ships with a first-party web search tool. For local tasks in the Codex IDE Extension, Codex
+Codex ships with a first-party web search tool. For local tasks in the Codex app, Codex
 enables web search by default and serves results from a web search cache. If you configure your
 sandbox for [full access](https://developers.openai.com/codex/agent-approvals-security), web search defaults to live results. See
 [Config basics](https://developers.openai.com/codex/config-basic) to disable web search or switch to live results that fetch the
 most recent data.
 
+## Image generation
+
+Ask Codex to generate or edit images directly in a thread. This is useful for UI assets, banners, backgrounds, illustrations, sprite sheets, and placeholders you want to create alongside code. Add a reference image when you want Codex to transform or extend an existing asset.
+
+You can ask in natural language or explicitly invoke the image generation skill by including `$imagegen` in your prompt.
+
+Built-in image generation uses `gpt-image-2`, counts toward your general Codex usage limits, and uses included limits 3-5x faster on average than similar turns without image generation, depending on image quality and size. For details, see [Pricing](https://developers.openai.com/codex/pricing#image-generation-usage-limits). For prompting tips and model details, see the [image generation guide](https://developers.openai.com/api/docs/guides/image-generation).
+
+For larger batches of image generation, set `OPENAI_API_KEY` in your environment variables and ask Codex to generate images through the API so API pricing applies instead.
+
 ## Image input
 
 You can drag and drop images into the prompt composer to include them as context. Hold down `Shift`
@@ -873,6 +1212,25 @@
 You can also ask Codex to view images on your system. By giving Codex tools to take screenshots of
 the app you are working on, Codex can verify the work it's doing.
 
+<a id="projectless-threads"></a>
+
+## Chats
+
+Chats are threads you can start when the task doesn't need a specific project
+folder or Git repository. Use them for research, triage, planning,
+plugin-heavy workflows, and other conversations where Codex should use connected
+tools instead of editing a codebase.
+
+Chats use a Codex-managed `threads` directory under your Codex home as their
+working location. By default, that location is `~/.codex/threads`.
+
+## Memories
+
+[Memories](https://developers.openai.com/codex/memories), where available, let Codex carry useful context
+from past tasks into future threads. They're most useful for stable preferences,
+project conventions, recurring work patterns, and known pitfalls that would
+otherwise need to repeat.
+
 ## Notifications
 
 By default, the Codex app sends notifications when a task completes or needs approval while the app
@@ -890,6 +1248,9 @@
 
 - [Settings](https://developers.openai.com/codex/app/settings)
 - [Automations](https://developers.openai.com/codex/app/automations)
+- [In-app browser](https://developers.openai.com/codex/app/browser)
+- [Computer use](https://developers.openai.com/codex/app/computer-use)
+- [Review pane](https://developers.openai.com/codex/app/review)
 - [Local environments](https://developers.openai.com/codex/app/local-environments)
 - [Worktrees](https://developers.openai.com/codex/app/worktrees)
 
@@ -906,11 +1267,6 @@
 Choose where files open and how much command output appears in threads. You can also
 require <kbd>Cmd</kbd>+<kbd>Enter</kbd> for multiline prompts or prevent sleep while a
 thread runs.
-
-## Appearance
-
-Pick a theme, decide whether the window is solid, and adjust UI or code fonts. Font
-choices apply across the app, including the diff review panel and terminal.
 
 ## Notifications
 
@@ -924,6 +1280,45 @@
 options. See [Codex security](https://developers.openai.com/codex/agent-approvals-security) and
 [config basics](https://developers.openai.com/codex/config-basic) for more detail.
 
+## Appearance
+
+In **Settings**, you can change the Codex app appearance by choosing a base theme,
+adjusting accent, background, and foreground colors, and changing the UI and code
+fonts. You can also share your custom theme with friends.
+
+### Codex pets
+
+<div class="grid gap-5 md:grid-cols-[minmax(0,1fr)_minmax(15rem,50%)] md:items-start xl:grid-cols-[minmax(0,1fr)_minmax(16rem,30%)]">
+  <div>
+    Codex pets are optional animated companions for the app. In **Settings**,
+    go to **Appearance** and choose **Pets** to select a built-in pet or
+    refresh custom pets from your local Codex home. Type `/pet` in the
+    composer, use **Wake Pet** or **Tuck Away Pet** in **Settings > Appearance**, or
+    press <kbd>Cmd+K</kbd> or <kbd>Ctrl+K</kbd> and run the same commands to
+    toggle the floating overlay.
+
+    The overlay keeps active Codex work visible while you use other apps. It
+    shows the active thread, reflects whether Codex is running, waiting for
+    input, or ready for review, and pairs that state with a short progress
+    prompt so you can glance at what changed without reopening the thread.
+
+  </div>
+
+  </div>
+
+To create your own pet, install the `hatch-pet` skill:
+
+```text
+$skill-installer hatch-pet
+```
+
+Reload skills from the command menu. Press <kbd>Cmd+K</kbd> or <kbd>Ctrl+K</kbd>,
+choose **Force Reload Skills**, then ask the skill to create a pet:
+
+```text
+$hatch-pet create a new pet inspired by my recent projects
+```
+
 ## Git
 
 Use Git settings to standardize branch naming and choose whether Codex uses force
@@ -937,6 +1332,24 @@
 also apply to the Codex CLI and IDE extension because the MCP configuration lives in
 `config.toml`. See the [Model Context Protocol docs](https://developers.openai.com/codex/mcp) for details.
 
+## Browser use
+
+Use these settings to install or enable the bundled Browser plugin, set up the
+[Codex Chrome extension](https://developers.openai.com/codex/app/chrome-extension), and manage allowlisted
+and blocklisted websites. Codex asks before using a website unless you've
+allowlisted it. Removing a site from the blocklist lets Codex ask again before
+using it in the browser.
+
+See [In-app browser](https://developers.openai.com/codex/app/browser) for browser preview, comment, and
+browser use workflows.
+
+## Computer Use
+
+On macOS, check your Computer Use settings to review desktop-app access and related
+preferences after setup. To revoke system-level access, update Screen Recording
+or Accessibility permissions in macOS Privacy & Security settings. The feature
+isn't available in the EEA, the United Kingdom, or Switzerland at launch.
+
 ## Personalization
 
 Choose **Friendly**, **Pragmatic**, or **None** as your default personality. Use
@@ -945,10 +1358,399 @@
 You can also add your own custom instructions. Editing custom instructions updates your
 [personal instructions in `AGENTS.md`](https://developers.openai.com/codex/guides/agents-md).
 
+## Context-aware suggestions
+
+Use context-aware suggestions to surface follow-ups and tasks you may want to resume when you
+start or return to Codex.
+
+## Memories
+
+Enable Memories, where available, to let Codex carry useful context from past
+threads into future work. See [Memories](https://developers.openai.com/codex/memories) for setup, storage,
+and per-thread controls.
+
 ## Archived threads
 
 The **Archived threads** section lists archived chats with dates and project
 context. Use **Unarchive** to restore a thread.
+
+---
+
+# Codex Chrome extension
+
+The Codex Chrome extension lets Codex use Chrome for browser tasks that need
+your signed-in browser state. Use it when Codex needs to read or act on sites
+such as LinkedIn, Salesforce, Gmail, or internal tools.
+
+For local development servers, file-backed previews, and public pages that do
+not require sign-in, use the [in-app browser](https://developers.openai.com/codex/app/browser) first. The
+in-app browser keeps preview and verification work inside Codex without using
+your Chrome profile.
+
+Codex can also switch between tools as a task requires, using plugins when a
+dedicated integration is available, Chrome when it needs logged-in browser
+context, and the in-app browser for localhost.
+
+<div className="not-prose my-4">
+  </div>
+
+## Set up Chrome from Plugins
+
+Set up the extension from Codex:
+
+1. Open Codex and go to **Plugins**.
+2. Add the **Chrome** plugin.
+3. Follow the setup flow. It guides you through installing or connecting the
+   Chrome extension and approving Chrome's permission prompts.
+4. Open Chrome and confirm the Codex extension shows **Connected**.
+
+After the plugin setup is complete, start a new Codex thread. Codex can suggest
+Chrome when a task needs a signed-in website. You can also invoke it directly in
+a prompt:
+
+```text
+@Chrome open Salesforce and update the account from these call notes.
+```
+
+If Chrome isn't already open, Codex can open it. Chrome browser tasks run in
+Chrome tab groups so the work for a thread stays grouped together.
+
+## Control website access
+
+By default, Codex asks before it interacts with each new website. Codex bases
+the prompt on the website host, such as `example.com`.
+
+When Codex asks to use a website, you can choose the option that matches the
+task and your risk tolerance:
+
+- Allow the website for the current chat.
+- Always allow the host so Codex can use that website again without asking.
+- Decline the website.
+
+### Manage the allowlist and blocklist
+
+In Computer Use settings, you can manage an allowlist and blocklist for
+domains. The allowlist contains domains Codex can use without asking again. The
+blocklist contains domains Codex shouldn't use.
+
+Removing a domain from the allowlist means Codex asks again before using it.
+Removing a domain from the blocklist means Codex can ask again instead of
+treating the domain as blocked.
+
+#### Always allow browser content If you turn on always allow browser content, Codex no longer asks for
+confirmation before using websites.
+
+#### Browser history Browser history can include sensitive telemetry, internal URLs, search terms,
+and activity from Chrome sessions on signed-in devices. If you allow Codex to
+access browser history, relevant history entries can become part of the context
+Codex uses for the task. Malicious or misleading page content can increase the
+risk that Codex copies this data somewhere unintended.
+
+Codex asks when it wants to use browser history. Codex scopes history access to
+the request, and history doesn't have an always-allow option.
+
+## Data and security
+
+### Chrome extension permissions
+
+Chrome asks you to accept extension permissions when you install the extension.
+The permission prompt may include:
+
+- Access the page debugger
+- Read and change all your data on all websites
+- Read and change your browsing history on all your signed-in devices
+- Display notifications
+- Read and change your bookmarks
+- Manage your downloads
+- Communicate with cooperating native applications
+- View and manage your tab groups
+
+These Chrome permissions make the extension capable of operating browser
+workflows. Codex still uses its own confirmations, settings, allowlists, and
+blocklists before using websites or browser history during a task.
+
+### Memories
+
+Browser use follows your Codex Memories setting. If Memories is on, Codex can
+use relevant saved memories while working in Chrome. If Memories is off, browser
+use doesn't use memories.
+
+### What OpenAI stores from browsing
+
+OpenAI doesn't store a separate complete record of your Chrome actions from the
+extension. OpenAI stores browser activity only when it becomes part of the Codex
+context, such as text Codex reads from a page, screenshots, tool calls,
+summaries, messages, or other content included in the thread.
+
+Your ChatGPT and Codex data controls apply to content processed in context.
+Avoid sending secrets or highly sensitive data through browser tasks unless
+they're required and you are present to review each prompt.
+
+## Troubleshooting
+
+If Codex can't connect to Chrome, first confirm the website Codex is trying to
+access isn't in the blocklist in Settings. If the website isn't blocked, work
+through these checks:
+
+1. Open the Codex extension from the Chrome toolbar or Chrome's extensions
+   menu. Make sure it shows **Connected**. If it shows disconnected or mentions
+   a missing native host, remove and re-add the Chrome plugin from **Plugins**
+   in Codex, then follow the setup flow again.
+2. In Codex, open **Plugins** and confirm that the Chrome plugin is on. If the
+   plugin is off, turn it on and try the task again.
+3. Make sure you are using the same Chrome profile where the Codex extension is
+   installed. If you use more than one Chrome profile, install and enable the
+   extension in the active profile.
+4. Start a new Codex thread and try the Chrome task again. This can clear a
+   thread-specific connection state.
+5. Restart Chrome and Codex, then try again. If the extension still doesn't
+   connect, uninstall the Codex Chrome extension, remove and re-add the Chrome
+   plugin from **Plugins**, and follow the setup flow again.
+6. If the extension shows **Connected** but Codex still can't use Chrome, run
+   `/feedback` in the Codex app and include the thread ID when you contact
+   support.
+
+### Upload Files
+
+If a Chrome task needs to upload a file from your computer, allow the Codex
+extension to access file URLs in Chrome:
+
+1. In Chrome, open the extensions icon in the toolbar, then click **Manage
+   Extensions**.
+2. On the Codex extension card, click **Details**.
+3. Turn on **Allow access to file URLs**.
+
+After you change the setting, start the Chrome task again.
+
+---
+
+# Computer Use
+
+In the Codex app, computer use is currently available on macOS, except in the
+  European Economic Area, the United Kingdom, and Switzerland at launch. Install
+  the Computer Use plugin, then grant Screen Recording and Accessibility
+  permissions when macOS prompts you.
+
+With computer use, Codex can see and operate graphical user interfaces on macOS.
+Use it for tasks where command-line tools or structured integrations aren't
+enough, such as checking a desktop app, using a browser, changing app settings,
+working with a data source that isn't available as a plugin, or reproducing a
+bug that only happens in a graphical user interface.
+
+Because computer use can affect app and system state outside your project
+workspace, use it for scoped tasks and review permission prompts before
+continuing.
+
+## Set up computer use
+
+In Codex settings, open **Computer Use** and click **Install** to install the
+Computer Use plugin before you ask Codex to operate desktop apps. When macOS
+prompts for access, grant Screen Recording and Accessibility permissions if you
+want Codex to see and interact with the target app.
+
+To use computer use, grant:
+
+- **Screen Recording** permission so Codex can see the target app.
+- **Accessibility** permission so Codex can click, type, and navigate.
+
+## When to use computer use
+
+Choose computer use when the task depends on a graphical user interface that's
+hard to verify through files or command output alone.
+
+Good fits include:
+
+- Testing a macOS app, an iOS simulator flow, or another desktop app that Codex
+  is building.
+- Performing a task that requires your web browser.
+- Reproducing a bug that only appears in a graphical interface.
+- Changing app settings that require clicking through a UI.
+- Inspecting information in an app or data source that isn't available through a
+  plugin.
+- Running a scoped task in the background while you keep working elsewhere.
+- Executing a workflow that spans more than one app.
+
+For web apps you are building locally, use the
+[in-app browser](https://developers.openai.com/codex/app/browser) first.
+
+## Start a computer use task
+
+Mention `@Computer` or `@AppName` in your prompt, or ask Codex to use
+computer use. Describe the exact app, window, or flow Codex should operate.
+
+```text
+Open the app with computer use, reproduce the onboarding bug, and fix the
+smallest code path that causes it. After each change, run the same UI flow
+again.
+```
+
+```text
+Open @Chrome and verify the checkout page still works after the latest changes.
+```
+
+If the target app exposes a dedicated plugin or MCP server, prefer that
+structured integration for data access and repeatable operations. Choose
+computer use when Codex needs to inspect or operate the app visually.
+
+## Permissions and approvals
+
+The macOS system permissions for computer use are separate from app approvals in
+Codex. The macOS permissions let Codex see and operate apps. App approvals
+determine which apps you allow Codex to use. File reads, file edits, and shell
+commands still follow the sandbox and approval settings for the thread.
+
+With computer use, Codex can see and take action only in the apps you allow.
+During a task, Codex asks for your permission before it can use an app on your
+computer. You can choose **Always allow** so Codex can use that app in the future
+without asking again. You can remove apps from the **Always allow** list in the
+**Computer Use** section of Codex settings.
+
+Codex may also ask for permission before taking sensitive or disruptive actions.
+
+If Codex can't see or control an app, open **System Settings > Privacy &
+Security** and check **Screen Recording** and **Accessibility** for the Codex
+app.
+
+## Safety guidance
+
+With computer use, Codex can view screen content, take screenshots, and interact
+with windows, menus, keyboard input, and clipboard state in the target app.
+Treat visible app content, browser pages, screenshots, and files opened in the
+target app as context Codex may process while the task runs.
+
+Keep tasks narrow and stay present for sensitive flows:
+
+- Give Codex one clear target app or flow at a time.
+- You can stop the task or take over your computer at any time.
+- Keep sensitive apps closed unless they're required for the task.
+- Avoid tasks that require secrets unless you're present and can approve each
+  step.
+- Review app permission prompts before allowing Codex to use an app.
+- Use **Always allow** only for apps you trust Codex to use automatically in
+  future tasks.
+- Stay present for account, security, privacy, network, payment, or
+  credential-related settings.
+- Cancel the task if Codex starts interacting with the wrong window.
+
+If Codex uses your browser, it can interact with pages where you're already
+signed in. Review website actions as if you were taking them yourself: web pages
+can contain malicious or misleading content, and sites may treat approved clicks,
+form submissions, and signed-in actions as coming from your account. To keep
+using your browser while Codex works, ask Codex to use a different browser.
+
+The feature can't automate terminal apps or Codex itself, since automating them
+could bypass Codex security policies. It also can't authenticate as an
+administrator or approve security and privacy permission prompts on your
+computer.
+
+File edits and shell commands still follow Codex approval and sandbox settings
+where applicable. Changes made through desktop apps may not appear in the review
+pane until they're saved to disk and tracked by the project. Your ChatGPT data
+controls apply to content processed through Codex, including screenshots taken
+by computer use.
+
+---
+
+# In-app browser
+
+The in-app browser gives you and Codex a shared view of rendered web pages
+inside a thread. Use it when you're building or debugging a web app and want to
+preview pages and attach visual comments.
+
+Use it for local development servers, file-backed previews, and public pages
+that don't require sign-in. For anything that depends on login state or browser
+extensions, use your regular browser or the
+[Codex Chrome extension](https://developers.openai.com/codex/app/chrome-extension).
+
+Open the in-app browser from the toolbar, by clicking a URL, by navigating
+manually in the browser, or by pressing <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>B</kbd>
+(<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>B</kbd> on Windows).
+
+The in-app browser does not support authentication flows, signed-in pages,
+  your regular browser profile, cookies, extensions, or existing tabs. Use it
+  for pages Codex can open without logging in.
+
+Treat page content as untrusted context. Don't paste secrets into browser flows.
+
+## Browser use
+
+Browser use lets Codex operate the in-app browser directly. Use it for local
+development servers and file-backed previews when Codex needs to click, type,
+inspect rendered state, take screenshots, or verify a fix in the page.
+
+To use it, install and enable the Browser plugin. Then ask Codex to use the
+browser in your task, or reference it directly with `@Browser`. The app keeps
+browser use inside the in-app browser and lets you manage allowed and blocked
+websites from settings.
+
+Example:
+
+```text
+Use the browser to open http://localhost:3000/settings, reproduce the layout
+bug, and fix only the overflowing controls.
+```
+
+Codex asks before using a website unless you've allowed it. Removing a site from
+the allowed list means Codex asks again before using it; removing a site from the
+blocked list means Codex can ask again instead of treating it as blocked.
+
+For signed-in websites in Chrome, see
+[Codex Chrome extension](https://developers.openai.com/codex/app/chrome-extension).
+
+## Preview a page
+
+1. Start your app's development server in the [integrated terminal](https://developers.openai.com/codex/app/features#integrated-terminal) or with a [local environment action](https://developers.openai.com/codex/app/local-environments#actions).
+2. Open an unauthenticated local route, file-backed page, or public page by
+   clicking a URL or navigating manually in the browser.
+3. Review the rendered state alongside the code diff.
+4. Leave browser comments on the elements or areas that need changes.
+5. Ask Codex to address the comments and keep the scope narrow.
+
+Example feedback:
+
+```text
+I left comments on the pricing page in the in-app browser. Address the mobile
+layout issues and keep the card structure unchanged.
+```
+
+## Comment on the page
+
+When a bug is visible only in the rendered page, use browser comments to give
+Codex precise feedback on the page.
+
+- Turn on comment mode, select an element or area, and submit a comment.
+- In comment mode, hold <kbd>Shift</kbd> and click to select an area.
+- Hold <kbd>Cmd</kbd> while clicking to send a comment immediately.
+
+After you leave comments, send a message in the thread asking Codex to address
+them. Comments are most useful when Codex needs to make a precise visual change.
+
+Good feedback is specific:
+
+```text
+This button overflows on mobile. Keep the label on one line if it fits,
+otherwise wrap it without changing the card height.
+```
+
+```text
+This tooltip covers the data point under the cursor. Reposition the tooltip so
+it stays inside the chart bounds.
+```
+
+## Keep browser tasks scoped
+
+The in-app browser is for review and iteration. Keep each browser task small
+enough to review in one pass.
+
+- Name the page, route, or local URL.
+- Name the visual state you care about, such as loading, empty, error, or
+  success.
+- Leave comments on the exact elements or areas that need changes.
+- Review the updated route after Codex changes the code.
+- Ask Codex to start or check the dev server before it uses the browser.
+
+For repository changes, use the [review pane](https://developers.openai.com/codex/app/review) to inspect the
+changes and leave comments.
 
 ---
 
@@ -1045,12 +1847,12 @@
 2. Hover the line you want to comment on.
 3. Click the **+** button that appears.
 4. Write your feedback and submit it.
-5. Once you are done with all your feedback, send a message back to the thread.
-
-Because the comment is anchored to a line, Codex can usually respond more
-precisely than with a general instruction.
-
-Inline comments are treated as review guidance. After leaving comments, send a
+5. After you finish leaving feedback, send a message back to the thread.
+
+Because comments are line-specific, Codex can respond more precisely than with a
+general instruction.
+
+Codex treats inline comments as review guidance. After leaving comments, send a
 follow-up message that makes your intent explicit, for example “Address the
 inline comments and keep the scope minimal.”
 
@@ -1059,12 +1861,35 @@
 If you use `/review` to run a code review, comments will show up directly
 inline in the review pane.
 
+## Pull request reviews
+
+When Codex has GitHub access for your repository and the current project is on
+the pull request branch, the Codex app can help you work through pull request
+feedback without leaving the app. The sidebar shows pull request context and
+feedback from reviewers, and the review pane shows comments alongside the diff
+so you can ask Codex to address issues in the same thread.
+
+Install the GitHub CLI (`gh`) and authenticate it with `gh auth login` so Codex
+can load pull request context, review comments, and changed files. If `gh` is
+missing or unauthenticated, pull request details may not appear in the sidebar
+or review pane.
+
+Use this flow when you want to keep the full fix loop in one place:
+
+1. Open the review pane on the pull request branch.
+2. Review the pull request context, comments, and changed files.
+3. Ask Codex to fix the specific comments you want handled.
+4. Inspect the resulting diff in the review pane.
+5. Stage, commit, and push the changes to the PR branch when you are ready.
+
+For GitHub-triggered reviews, see [Use Codex in GitHub](https://developers.openai.com/codex/integrations/github).
+
 ## Staging and reverting files
 
 The review pane includes Git actions so you can shape the diff before you
 commit.
 
-You can stage, unstage, or revert changes at multiple levels:
+You can stage, unstage, or revert changes at these levels:
 
 - **Entire diff**: use the action buttons in the review header (for example,
   "Stage all" or "Revert all")
@@ -1074,7 +1899,7 @@
 Use staging when you want to accept part of the work, and revert when you want
 to discard it.
 
-### Partially staged states
+### Staged and unstaged states
 
 Git can represent both staged and unstaged changes in the same file. When that
 happens, it can look like the pane is showing “the same file twice” across
@@ -1223,16 +2048,18 @@
 
 # Windows
 
-The [Codex app for Windows](https://apps.microsoft.com/detail/9plm9xgg6vks?hl=en-US&gl=US) gives you one interface for
+The [Codex app for Windows](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi) gives you one interface for
 working across projects, running parallel agent threads, and reviewing results.
+The Windows app supports core workflows such as worktrees, automations, Git
+functionality, the in-app browser, artifact previews, plugins, and skills.
 It runs natively on Windows using PowerShell and the
 [Windows sandbox](https://developers.openai.com/codex/windows#windows-sandbox), or you can configure it to
-run in [Windows Subsystem for Linux (WSL)](#windows-subsystem-for-linux-wsl).
+run in [Windows Subsystem for Linux 2 (WSL2)](#windows-subsystem-for-linux-wsl).
 
 ## Download and update the Codex app
 
 Download the Codex app from the
-[Microsoft Store](https://apps.microsoft.com/detail/9plm9xgg6vks?hl=en-US&gl=US).
+[Microsoft Store](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi).
 
 Then follow the [quickstart](https://developers.openai.com/codex/quickstart?setup=app) to get started.
 
@@ -1248,6 +2075,18 @@
 ```powershell
 winget install Codex -s msstore
 ```
+
+## Native sandbox
+
+The Codex app on Windows supports a native [Windows sandbox](https://developers.openai.com/codex/windows#windows-sandbox) when the agent runs in PowerShell, and uses Linux sandboxing when you run the agent in [Windows Subsystem for Linux 2 (WSL2)](#windows-subsystem-for-linux-wsl). To apply sandbox protections in either mode, set sandbox permissions to **Default permissions** in the Composer before sending messages to Codex.
+
+Running Codex in full access mode means Codex is not limited to your project
+  directory and might perform unintentional destructive actions that can lead to
+  data loss. Keep sandbox boundaries in place and use [rules](https://developers.openai.com/codex/rules) for
+  targeted exceptions, or set your [approval policy to
+  never](https://developers.openai.com/codex/agent-approvals-security#run-without-approval-prompts) to have
+  Codex attempt to solve problems without asking for escalated permissions,
+  based on your [approval and security setup](https://developers.openai.com/codex/agent-approvals-security).
 
 ## Customize for your dev setup
 
@@ -1292,7 +2131,7 @@
 
 By default, the Codex app uses the Windows-native agent. That means the agent
 runs commands in PowerShell. The app can still work with projects that live in
-Windows Subsystem for Linux (WSL) by using the `wsl` CLI when needed.
+Windows Subsystem for Linux 2 (WSL2) by using the `wsl` CLI when needed.
 
 If you want to add a project from the WSL filesystem, click **Add new project**
 or press <kbd>Ctrl</kbd>+<kbd>O</kbd>, then type `\\wsl$\` into the File
@@ -1304,10 +2143,13 @@
 `/mnt/<drive>/...`. This setup is more reliable than opening projects
 directly from the WSL filesystem.
 
-If you want the agent itself to run in WSL, open **[Settings](codex://settings)**,
+If you want the agent itself to run in WSL2, open **[Settings](codex://settings)**,
 switch the agent from Windows native to WSL, and **restart the app**. The
 change doesn't take effect until you restart. Your projects should remain in
 place after restart.
+
+WSL1 was supported through Codex `0.114`. Starting in Codex `0.115`, the Linux
+sandbox moved to `bubblewrap`, so WSL1 is no longer supported.
 
 You configure the integrated terminal independently from the agent. See
 [Customize for your dev setup](#customize-for-your-dev-setup) for the
@@ -1400,7 +2242,7 @@
 `%USERPROFILE%\.codex`.
 
 If you also run the Codex CLI inside WSL, the CLI uses the Linux home
-directory by default, so it does not automatically share configuration, cached
+directory by default, so it doesn't automatically share configuration, cached
 auth, or session history with the Windows app.
 
 To share them, use one of these approaches:
@@ -1422,15 +2264,15 @@
 
 ### Git isn't detected for projects opened from `\\wsl$`
 
-For now, if you want to use the Windows-native agent with a project that is
-also accessible from WSL, the most reliable workaround is to store the project
+For now, if you want to use the Windows-native agent with a project also
+accessible from WSL, the most reliable workaround is to store the project
 on the native Windows drive and access it in WSL through `/mnt/<drive>/...`.
 
-### Cmder is not listed in the open dialog
-
-If Cmder is installed but doesn't show in Codex's open dialog, add it to the
-Windows Start Menu: right-click Cmder and choose **Add to Start**, then restart
-Codex or reboot.
+### `Cmder` isn't listed in the open dialog
+
+If `Cmder` is installed but doesn't show in Codex's open dialog, add it to the
+Windows Start Menu: right-click `Cmder` and choose **Add to Start**, then
+restart Codex or reboot.
 
 ---
 
@@ -1625,7 +2467,26 @@
 Supported transports:
 
 - `stdio` (`--listen stdio://`, default): newline-delimited JSON (JSONL).
-- `websocket` (`--listen ws://IP:PORT`, experimental): one JSON-RPC message per WebSocket text frame.
+- `websocket` (`--listen ws://IP:PORT`, experimental and unsupported): one JSON-RPC message per WebSocket text frame.
+- `off` (`--listen off`): don't expose a local transport.
+
+When you run with `--listen ws://IP:PORT`, the same listener also serves basic HTTP health probes:
+
+- `GET /readyz` returns `200 OK` once the listener accepts new connections.
+- `GET /healthz` returns `200 OK` when the request doesn't include an `Origin` header.
+- Requests with an `Origin` header are rejected with `403 Forbidden`.
+
+WebSocket transport is experimental and unsupported. Loopback listeners such as `ws://127.0.0.1:PORT` are appropriate for localhost and SSH port-forwarding workflows. Non-loopback WebSocket listeners currently allow unauthenticated connections by default during rollout, so configure WebSocket auth before exposing one remotely.
+
+Supported WebSocket auth flags:
+
+- `--ws-auth capability-token --ws-token-file /absolute/path`
+- `--ws-auth capability-token --ws-token-sha256 HEX`
+- `--ws-auth signed-bearer-token --ws-shared-secret-file /absolute/path`
+
+For signed bearer tokens, you can also set `--ws-issuer`, `--ws-audience`, and `--ws-max-clock-skew-seconds`. Clients present the credential as `Authorization: Bearer <token>` during the WebSocket handshake, and app-server enforces auth before JSON-RPC `initialize`.
+
+Prefer `--ws-token-file` over passing raw bearer tokens on the command line. Use `--ws-token-sha256` only when the client keeps the raw high-entropy token in a separate local secret store; the hash is only a verifier, and clients still need the original token.
 
 In WebSocket mode, app-server uses bounded queues. When request ingress is full, the server rejects new requests with JSON-RPC error code `-32001` and message `"Server overloaded; retry later."` Clients should retry with an exponentially increasing delay and jitter.
 
@@ -1634,7 +2495,7 @@
 Requests include `method`, `params`, and `id`:
 
 ```json
-{ "method": "thread/start", "id": 10, "params": { "model": "gpt-5.1-codex" } }
+{ "method": "thread/start", "id": 10, "params": { "model": "gpt-5.4" } }
 ```
 
 Responses echo the `id` with either `result` or `error`:
@@ -1712,7 +2573,7 @@
   },
 });
 send({ method: "initialized", params: {} });
-send({ method: "thread/start", id: 1, params: { model: "gpt-5.1-codex" } });
+send({ method: "thread/start", id: 1, params: { model: "gpt-5.4" } });
 ```
 
 ## Core primitives
@@ -1736,7 +2597,7 @@
 
 Clients must send a single `initialize` request per transport connection before invoking any other method on that connection, then acknowledge with an `initialized` notification. Requests sent before initialization receive a `Not initialized` error, and repeated `initialize` calls on the same connection return `Already initialized`.
 
-The server returns the user agent string it will present to upstream services. Set `clientInfo` to identify your integration.
+The server returns the user agent string it will present to upstream services plus `platformFamily` and `platformOs` values that describe the runtime target. Set `clientInfo` to identify your integration.
 
 `initialize.params.capabilities` also supports per-connection notification opt-out via `optOutNotificationMethods`, which is a list of exact method names to suppress for that connection. Matching is exact (no wildcards/prefixes). Unknown method names are accepted and ignored.
 
@@ -1772,10 +2633,7 @@
     },
     "capabilities": {
       "experimentalApi": true,
-      "optOutNotificationMethods": [
-        "codex/event/session_configured",
-        "item/agentMessage/delta"
-      ]
+      "optOutNotificationMethods": ["thread/started", "item/agentMessage/delta"]
     }
   }
 }
@@ -1815,37 +2673,71 @@
 - `thread/resume` - reopen an existing thread by id so later `turn/start` calls append to it.
 - `thread/fork` - fork a thread into a new thread id by copying stored history; emits `thread/started` for the new thread.
 - `thread/read` - read a stored thread by id without resuming it; set `includeTurns` to return full turn history. Returned `thread` objects include runtime `status`.
-- `thread/list` - page through stored thread logs; supports cursor-based pagination plus `modelProviders`, `sourceKinds`, `archived`, and `cwd` filters. Returned `thread` objects include runtime `status`.
+- `thread/list` - page through stored thread logs; supports cursor-based pagination plus `modelProviders`, `sourceKinds`, `archived`, `cwd`, and `searchTerm` filters. Returned `thread` objects include runtime `status`.
+- `thread/turns/list` - page through a stored thread's turn history without resuming it.
 - `thread/loaded/list` - list the thread ids currently loaded in memory.
+- `thread/name/set` - set or update a thread's user-facing name for a loaded thread or a persisted rollout; emits `thread/name/updated`.
+- `thread/goal/set` - set the goal for a loaded thread (experimental; requires `capabilities.experimentalApi`); emits `thread/goal/updated`.
+- `thread/goal/get` - read the current goal for a loaded thread (experimental; requires `capabilities.experimentalApi`).
+- `thread/goal/clear` - clear the goal for a loaded thread (experimental; requires `capabilities.experimentalApi`); emits `thread/goal/cleared`.
+- `thread/metadata/update` - patch SQLite-backed stored thread metadata; currently supports persisted `gitInfo`.
 - `thread/archive` - move a thread's log file into the archived directory; returns `{}` on success and emits `thread/archived`.
-- `thread/unsubscribe` - unsubscribe this connection from thread turn/item events. If this was the last subscriber, the server unloads the thread and emits `thread/closed`.
+- `thread/unsubscribe` - unsubscribe this connection from thread turn/item events. If this was the last subscriber, the server unloads the thread after a no-subscriber inactivity grace period and emits `thread/closed`.
 - `thread/unarchive` - restore an archived thread rollout back into the active sessions directory; returns the restored `thread` and emits `thread/unarchived`.
 - `thread/status/changed` - notification emitted when a loaded thread's runtime `status` changes.
 - `thread/compact/start` - trigger conversation history compaction for a thread; returns `{}` immediately while progress streams via `turn/*` and `item/*` notifications.
+- `thread/shellCommand` - run a user-initiated shell command against a thread. This runs outside the sandbox with full access and doesn't inherit the thread sandbox policy.
+- `thread/backgroundTerminals/clean` - stop all running background terminals for a thread (experimental; requires `capabilities.experimentalApi`).
 - `thread/rollback` - drop the last N turns from the in-memory context and persist a rollback marker; returns the updated `thread`.
 - `turn/start` - add user input to a thread and begin Codex generation; responds with the initial `turn` and streams events. For `collaborationMode`, `settings.developer_instructions: null` means "use built-in instructions for the selected mode."
+- `thread/inject_items` - append raw Responses API items to a loaded thread's model-visible history without starting a user turn.
 - `turn/steer` - append user input to the active in-flight turn for a thread; returns the accepted `turnId`.
 - `turn/interrupt` - request cancellation of an in-flight turn; success is `{}` and the turn ends with `status: "interrupted"`.
 - `review/start` - kick off the Codex reviewer for a thread; emits `enteredReviewMode` and `exitedReviewMode` items.
 - `command/exec` - run a single command under the server sandbox without starting a thread/turn.
+- `command/exec/write` - write `stdin` bytes to a running `command/exec` session or close `stdin`.
+- `command/exec/resize` - resize a running PTY-backed `command/exec` session.
+- `command/exec/terminate` - stop a running `command/exec` session.
+- `command/exec/outputDelta` (notify) - emitted for base64-encoded stdout/stderr chunks from a streaming `command/exec` session.
 - `model/list` - list available models (set `includeHidden: true` to include entries with `hidden: true`) with effort options, optional `upgrade`, and `inputModalities`.
+- `modelProvider/capabilities/read` - read provider capability bounds for model/provider combinations (experimental; requires `capabilities.experimentalApi`).
 - `experimentalFeature/list` - list feature flags with lifecycle stage metadata and cursor pagination.
+- `experimentalFeature/enablement/set` - patch in-memory runtime enablement for supported feature keys such as `apps` and `plugins`.
 - `collaborationMode/list` - list collaboration mode presets (experimental, no pagination).
 - `skills/list` - list skills for one or more `cwd` values (supports `forceReload` and optional `perCwdExtraUserRoots`).
+- `skills/changed` (notify) - emitted when watched local skill files change.
+- `marketplace/add` - add a remote plugin marketplace and persist it into the user's marketplace config.
+- `marketplace/upgrade` - refresh a configured Git marketplace, or all configured Git marketplaces when you omit the marketplace name.
+- `plugin/list` - list discovered plugin marketplaces and plugin state, including install/auth policy metadata, marketplace load errors, featured plugin ids, and local, Git, or remote plugin source metadata.
+- `plugin/read` - read one plugin by marketplace path or remote marketplace name and plugin name, including bundled skills, apps, and MCP server names when those details are available.
+- `plugin/install` - install a plugin from a marketplace path or remote marketplace name.
+- `plugin/uninstall` - uninstall an installed plugin.
 - `app/list` - list available apps (connectors) with pagination plus accessibility/enabled metadata.
 - `skills/config/write` - enable or disable skills by path.
 - `mcpServer/oauth/login` - start an OAuth login for a configured MCP server; returns an authorization URL and emits `mcpServer/oauthLogin/completed` on completion.
 - `tool/requestUserInput` - prompt the user with 1-3 short questions for a tool call (experimental); questions can set `isOther` for a free-form option.
 - `config/mcpServer/reload` - reload MCP server configuration from disk and queue a refresh for loaded threads.
-- `mcpServerStatus/list` - list MCP servers, tools, resources, and auth status (cursor + limit pagination).
+- `mcpServerStatus/list` - list MCP servers, tools, resources, and auth status (cursor + limit pagination). Use `detail: "full"` for full data or `detail: "toolsAndAuthOnly"` to omit resources.
+- `mcpServer/resource/read` - read a single MCP resource through an initialized MCP server.
+- `mcpServer/tool/call` - call a tool on a thread's configured MCP server.
+- `mcpServer/startupStatus/updated` (notify) - emitted when a configured MCP server's startup status changes for a loaded thread.
 - `windowsSandbox/setupStart` - start Windows sandbox setup for `elevated` or `unelevated` mode; returns quickly and later emits `windowsSandbox/setupCompleted`.
 - `feedback/upload` - submit a feedback report (classification + optional reason/logs + conversation id, plus optional `extraLogFiles` attachments).
 - `config/read` - fetch the effective configuration on disk after resolving configuration layering.
-- `externalAgentConfig/detect` - detect migratable external-agent artifacts with `includeHome` and optional `cwds`; each detected item includes `cwd` (`null` for home).
-- `externalAgentConfig/import` - apply selected external-agent migration items by passing explicit `migrationItems` with `cwd` (`null` for home).
+- `externalAgentConfig/detect` - detect external-agent artifacts that can be migrated with `includeHome` and optional `cwds`; each detected item includes `cwd` (`null` for home).
+- `externalAgentConfig/import` - apply selected external-agent migration items by passing explicit `migrationItems` with `cwd` (`null` for home). Supported item types include config, skills, `AGENTS.md`, plugins, MCP server config, subagents, hooks, commands, and sessions; plugin imports emit `externalAgentConfig/import/completed`.
 - `config/value/write` - write a single configuration key/value to the user's `config.toml` on disk.
 - `config/batchWrite` - apply configuration edits atomically to the user's `config.toml` on disk.
 - `configRequirements/read` - fetch requirements from `requirements.toml` and/or MDM, including allow-lists, pinned `featureRequirements`, and residency/network requirements (or `null` if you haven't set any up).
+- `fs/readFile`, `fs/writeFile`, `fs/createDirectory`, `fs/getMetadata`, `fs/readDirectory`, `fs/remove`, `fs/copy`, `fs/watch`, `fs/unwatch`, and `fs/changed` (notify) - operate on absolute filesystem paths through the app-server v2 filesystem API.
+
+Plugin summaries include a `source` union. Local plugins return
+`{ "type": "local", "path": ... }`, Git-backed marketplace entries return
+`{ "type": "git", "url": ..., "path": ..., "refName": ..., "sha": ... }`,
+and remote catalog entries return `{ "type": "remote" }`. For remote-only
+catalog entries, `PluginMarketplaceEntry.path` can be `null`; pass
+`remoteMarketplaceName` instead of `marketplacePath` when reading or installing
+those plugins.
 
 ## Models
 
@@ -1914,13 +2806,16 @@
 ## Threads
 
 - `thread/read` reads a stored thread without subscribing to it; set `includeTurns` to include turns.
-- `thread/list` supports cursor pagination plus `modelProviders`, `sourceKinds`, `archived`, and `cwd` filtering.
+- `thread/turns/list` pages through a stored thread's turn history without resuming it.
+- `thread/list` supports cursor pagination plus `modelProviders`, `sourceKinds`, `archived`, `cwd`, and `searchTerm` filtering.
 - `thread/loaded/list` returns the thread IDs currently in memory.
 - `thread/archive` moves the thread's persisted JSONL log into the archived directory.
-- `thread/unsubscribe` unsubscribes the current connection from a loaded thread and can trigger `thread/closed`.
+- `thread/metadata/update` patches stored thread metadata, currently including persisted `gitInfo`.
+- `thread/unsubscribe` unsubscribes the current connection from a loaded thread and can trigger `thread/closed` after an inactivity grace period.
 - `thread/unarchive` restores an archived thread rollout back into the active sessions directory.
 - `thread/compact/start` triggers compaction and returns `{}` immediately.
 - `thread/rollback` drops the last N turns from the in-memory context and records a rollback marker in the thread's persisted JSONL log.
+- `thread/inject_items` appends raw Responses API items to a loaded thread's model-visible history without starting a user turn.
 
 ### Start or resume a thread
 
@@ -1928,7 +2823,7 @@
 
 ```json
 { "method": "thread/start", "id": 10, "params": {
-  "model": "gpt-5.1-codex",
+  "model": "gpt-5.4",
   "cwd": "/Users/me/project",
   "approvalPolicy": "never",
   "sandbox": "workspaceWrite",
@@ -1991,6 +2886,23 @@
 
 Unlike `thread/resume`, `thread/read` doesn't load the thread into memory or emit `thread/started`.
 
+### List thread turns
+
+Use `thread/turns/list` to page a stored thread's turn history without resuming it. Results default to newest-first so clients can fetch older turns with `nextCursor`. The response also includes `backwardsCursor`; pass it as `cursor` with `sortDirection: "asc"` to fetch turns newer than the first item from the earlier page.
+
+```json
+{ "method": "thread/turns/list", "id": 20, "params": {
+  "threadId": "thr_123",
+  "limit": 50,
+  "sortDirection": "desc"
+} }
+{ "id": 20, "result": {
+  "data": [],
+  "nextCursor": "older-turns-cursor-or-null",
+  "backwardsCursor": "newer-turns-cursor-or-null"
+} }
+```
+
 ### List threads (with pagination & filters)
 
 `thread/list` lets you render a history UI. Results default to newest-first by `createdAt`. Filters apply before pagination. Pass any combination of:
@@ -2002,6 +2914,7 @@
 - `sourceKinds` - restrict results to specific thread sources. When omitted or `[]`, the server defaults to interactive sources only: `cli` and `vscode`.
 - `archived` - when `true`, list archived threads only. When `false` or omitted, list non-archived threads (default).
 - `cwd` - restrict results to threads whose session current working directory exactly matches this path.
+- `searchTerm` - search stored thread summaries and metadata before pagination.
 
 `sourceKinds` accepts the following values:
 
@@ -2035,6 +2948,23 @@
 
 When `nextCursor` is `null`, you have reached the final page.
 
+### Update stored thread metadata
+
+Use `thread/metadata/update` to patch stored thread metadata without resuming the thread. Today this supports persisted `gitInfo`; omitted fields are left unchanged, and explicit `null` clears a stored value.
+
+```json
+{ "method": "thread/metadata/update", "id": 21, "params": {
+  "threadId": "thr_123",
+  "gitInfo": { "branch": "feature/sidebar-pr" }
+} }
+{ "id": 21, "result": {
+  "thread": {
+    "id": "thr_123",
+    "gitInfo": { "sha": null, "branch": "feature/sidebar-pr", "originUrl": null }
+  }
+} }
+```
+
 ### Track thread status changes
 
 `thread/status/changed` is emitted whenever a loaded thread's runtime status changes. The payload includes `threadId` and the new `status`.
@@ -2063,14 +2993,19 @@
 `thread/unsubscribe` removes the current connection's subscription to a thread. The response status is one of:
 
 - `unsubscribed` when the connection was subscribed and is now removed.
-- `notSubscribed` when the connection was not subscribed to that thread.
-- `notLoaded` when the thread is not loaded.
-
-If this was the last subscriber, the server unloads the thread and emits a `thread/status/changed` transition to `notLoaded` plus `thread/closed`.
+- `notSubscribed` when the connection wasn't subscribed to that thread.
+- `notLoaded` when the thread isn't loaded.
+
+If this was the last subscriber, the server keeps the thread loaded until it has no subscribers and no thread activity for 30 minutes. When the grace period expires, app-server unloads the thread and emits a `thread/status/changed` transition to `notLoaded` plus `thread/closed`.
 
 ```json
 { "method": "thread/unsubscribe", "id": 22, "params": { "threadId": "thr_123" } }
 { "id": 22, "result": { "status": "unsubscribed" } }
+```
+
+If the thread later expires:
+
+```json
 { "method": "thread/status/changed", "params": {
     "threadId": "thr_123",
     "status": { "type": "notLoaded" }
@@ -2111,13 +3046,35 @@
 { "id": 25, "result": {} }
 ```
 
+### Run a thread shell command
+
+Use `thread/shellCommand` for user-initiated shell commands that belong to a thread. The request returns immediately with `{}` while progress streams through standard `turn/*` and `item/*` notifications.
+
+This API runs outside the sandbox with full access and doesn't inherit the thread sandbox policy. Clients should expose it only for explicit user-initiated commands.
+
+If the thread already has an active turn, the command runs as an auxiliary action on that turn and its formatted output is injected into the turn's message stream. If the thread is idle, app-server starts a standalone turn for the shell command.
+
+```json
+{ "method": "thread/shellCommand", "id": 26, "params": { "threadId": "thr_b", "command": "git status --short" } }
+{ "id": 26, "result": {} }
+```
+
+### Clean background terminals
+
+Use `thread/backgroundTerminals/clean` to stop all running background terminals associated with a thread. This method is experimental and requires `capabilities.experimentalApi = true`.
+
+```json
+{ "method": "thread/backgroundTerminals/clean", "id": 27, "params": { "threadId": "thr_b" } }
+{ "id": 27, "result": {} }
+```
+
 ### Roll back recent turns
 
 Use `thread/rollback` to remove the last `numTurns` entries from the in-memory context and persist a rollback marker in the rollout log. The returned `thread` includes `turns` populated after the rollback.
 
 ```json
-{ "method": "thread/rollback", "id": 26, "params": { "threadId": "thr_b", "numTurns": 1 } }
-{ "id": 26, "result": { "thread": { "id": "thr_b", "name": "Bug bash notes", "ephemeral": false } } }
+{ "method": "thread/rollback", "id": 28, "params": { "threadId": "thr_b", "numTurns": 1 } }
+{ "id": 28, "result": { "thread": { "id": "thr_b", "name": "Bug bash notes", "ephemeral": false } } }
 ```
 
 ## Turns
@@ -2183,7 +3140,7 @@
     "writableRoots": ["/Users/me/project"],
     "networkAccess": true
   },
-  "model": "gpt-5.1-codex",
+  "model": "gpt-5.4",
   "effort": "medium",
   "summary": "concise",
   "personality": "friendly",
@@ -2195,6 +3152,24 @@
   }
 } }
 { "id": 30, "result": { "turn": { "id": "turn_456", "status": "inProgress", "items": [], "error": null } } }
+```
+
+### Inject items into a thread
+
+Use `thread/inject_items` to append prebuilt Responses API items to a loaded thread's prompt history without starting a user turn. These items are persisted to the rollout and included in subsequent model requests.
+
+```json
+{ "method": "thread/inject_items", "id": 31, "params": {
+  "threadId": "thr_123",
+  "items": [
+    {
+      "type": "message",
+      "role": "assistant",
+      "content": [{ "type": "output_text", "text": "Previously computed context." }]
+    }
+  ]
+} }
+{ "id": 31, "result": {} }
 ```
 
 ### Steer an active turn
@@ -2326,6 +3301,8 @@
 - The server rejects empty `command` arrays.
 - `sandboxPolicy` accepts the same shape used by `turn/start` (for example, `dangerFullAccess`, `readOnly`, `workspaceWrite`, `externalSandbox`).
 - When omitted, `timeoutMs` falls back to the server default.
+- Set `tty: true` for PTY-backed sessions, and use `processId` when you plan to follow up with `command/exec/write`, `command/exec/resize`, or `command/exec/terminate`.
+- Set `streamStdoutStderr: true` to receive `command/exec/outputDelta` notifications while the command is running.
 
 ### Read admin requirements (`configRequirements/read`)
 
@@ -2376,6 +3353,28 @@
 - `elevated` - run the elevated Windows sandbox setup path.
 - `unelevated` - run the legacy setup/preflight path.
 
+## Filesystem
+
+The v2 filesystem APIs operate on absolute paths. Use `fs/watch` when a client needs to invalidate UI state after a file or directory changes.
+
+```json
+{ "method": "fs/watch", "id": 54, "params": {
+  "watchId": "0195ec6b-1d6f-7c2e-8c7a-56f2c4a8b9d1",
+  "path": "/Users/me/project/.git/HEAD"
+} }
+{ "id": 54, "result": { "path": "/Users/me/project/.git/HEAD" } }
+{ "method": "fs/changed", "params": {
+  "watchId": "0195ec6b-1d6f-7c2e-8c7a-56f2c4a8b9d1",
+  "changedPaths": ["/Users/me/project/.git/HEAD"]
+} }
+{ "method": "fs/unwatch", "id": 55, "params": {
+  "watchId": "0195ec6b-1d6f-7c2e-8c7a-56f2c4a8b9d1"
+} }
+{ "id": 55, "result": {} }
+```
+
+Watching a file emits `fs/changed` for that file path, including updates delivered by replace or rename operations.
+
 ## Events
 
 Event notifications are the server-initiated stream for thread lifecycles, turn lifecycles, and the items within them. After you start or resume a thread, keep reading the active transport stream for `thread/started`, `thread/archived`, `thread/unarchived`, `thread/closed`, `thread/status/changed`, `turn/*`, `item/*`, and `serverRequest/resolved` notifications.
@@ -2386,7 +3385,7 @@
 
 - Exact-match only: `item/agentMessage/delta` suppresses only that method.
 - Unknown method names are ignored.
-- Applies to both legacy (`codex/event/*`) and v2 (`thread/*`, `turn/*`, `item/*`, etc.) notifications.
+- Applies to the current `thread/*`, `turn/*`, `item/*`, and related v2 notifications.
 - Doesn't apply to requests, responses, or errors.
 
 ### Fuzzy file search events (experimental)
@@ -2597,6 +3596,8 @@
 } }
 ```
 
+The server also emits `skills/changed` notifications when watched local skill files change. Treat this as an invalidation signal and rerun `skills/list` with your current params when needed.
+
 To enable or disable a skill by path:
 
 ```json
@@ -2763,7 +3764,7 @@
 
 ### Detect and import external agent config
 
-Use `externalAgentConfig/detect` to discover migratable external-agent artifacts, then pass the selected entries to `externalAgentConfig/import`.
+Use `externalAgentConfig/detect` to discover external-agent artifacts that can be migrated, then pass the selected entries to `externalAgentConfig/import`.
 
 Detection example:
 
@@ -2803,32 +3804,46 @@
 { "id": 64, "result": {} }
 ```
 
-Supported `itemType` values are `AGENTS_MD`, `CONFIG`, `SKILLS`, and `MCP_SERVER_CONFIG`. Detection returns only items that still have work to do. For example, AGENTS migration is skipped when `AGENTS.md` already exists and is non-empty, and skill imports do not overwrite existing skill directories.
+When a request includes plugin imports, the server emits `externalAgentConfig/import/completed` after the import finishes. This notification may arrive immediately after the response or after background remote imports complete.
+
+Supported `itemType` values are `AGENTS_MD`, `CONFIG`, `SKILLS`, `PLUGINS`,
+and `MCP_SERVER_CONFIG`. For `PLUGINS` items, `details.plugins` lists each
+`marketplaceName` and the `pluginNames` Codex can try to migrate. Detection
+returns only items that still have work to do. For example, Codex skips AGENTS
+migration when `AGENTS.md` already exists and is non-empty, and skill imports
+don't overwrite existing skill directories.
+
+When detecting plugins from `.claude/settings.json`, Codex reads configured
+marketplace sources from `extraKnownMarketplaces`. If `enabledPlugins` contains
+plugins from `claude-plugins-official` but the marketplace source is missing,
+Codex infers `anthropics/claude-plugins-official` as the source.
 
 ## Auth endpoints
 
-The JSON-RPC auth/account surface exposes request/response methods plus server-initiated notifications (no `id`). Use these to determine auth state, start or cancel logins, logout, and inspect ChatGPT rate limits.
+The JSON-RPC auth/account surface exposes request/response methods plus server-initiated notifications (no `id`). Use these to determine auth state, start or cancel logins, logout, inspect ChatGPT rate limits, and notify workspace owners about depleted credits or usage limits.
 
 ### Authentication modes
 
-Codex supports three authentication modes. `account/updated.authMode` shows the active mode, and `account/read` also reports it.
-
-- **API key (`apikey`)** - the caller supplies an OpenAI API key and Codex stores it for API requests.
-- **ChatGPT managed (`chatgpt`)** - Codex owns the ChatGPT OAuth flow, persists tokens, and refreshes them automatically.
-- **ChatGPT external tokens (`chatgptAuthTokens`)** - a host app supplies `idToken` and `accessToken` directly. Codex stores these tokens in memory, and the host app must refresh them when asked.
+Codex supports these authentication modes. `account/updated.authMode` shows the active mode and includes the current ChatGPT `planType` when available. `account/read` also reports account and plan details.
+
+- **API key (`apikey`)** - the caller supplies an OpenAI API key with `type: "apiKey"`, and Codex stores it for API requests.
+- **ChatGPT managed (`chatgpt`)** - Codex owns the ChatGPT OAuth flow, persists tokens, and refreshes them automatically. Start with `type: "chatgpt"` for the browser flow or `type: "chatgptDeviceCode"` for the device-code flow.
+- **ChatGPT external tokens (`chatgptAuthTokens`)** - experimental and intended for host apps that already own the user's ChatGPT auth lifecycle. The host app supplies an `accessToken`, `chatgptAccountId`, and optional `chatgptPlanType` directly, and must refresh the token when asked.
 
 ### API overview
 
 - `account/read` - fetch current account info; optionally refresh tokens.
-- `account/login/start` - begin login (`apiKey`, `chatgpt`, or `chatgptAuthTokens`).
+- `account/login/start` - begin login (`apiKey`, `chatgpt`, `chatgptDeviceCode`, or experimental `chatgptAuthTokens`).
 - `account/login/completed` (notify) - emitted when a login attempt finishes (success or error).
-- `account/login/cancel` - cancel a pending ChatGPT login by `loginId`.
+- `account/login/cancel` - cancel a pending managed ChatGPT login by `loginId`.
 - `account/logout` - sign out; triggers `account/updated`.
-- `account/updated` (notify) - emitted whenever auth mode changes (`authMode`: `apikey`, `chatgpt`, `chatgptAuthTokens`, or `null`).
+- `account/updated` (notify) - emitted whenever auth mode changes (`authMode`: `apikey`, `chatgpt`, `chatgptAuthTokens`, or `null`) and includes `planType` when available.
 - `account/chatgptAuthTokens/refresh` (server request) - request fresh externally managed ChatGPT tokens after an authorization error.
 - `account/rateLimits/read` - fetch ChatGPT rate limits.
 - `account/rateLimits/updated` (notify) - emitted whenever a user's ChatGPT rate limits change.
+- `account/sendAddCreditsNudgeEmail` - ask ChatGPT to email a workspace owner about depleted credits or a reached usage limit.
 - `mcpServer/oauthLogin/completed` (notify) - emitted after a `mcpServer/oauth/login` flow finishes; payload includes `{ name, success, error? }`.
+- `mcpServer/startupStatus/updated` (notify) - emitted when a configured MCP server's startup status changes for a loaded thread; payload includes `{ name, status, error }`.
 
 ### 1) Check auth state
 
@@ -2902,7 +3917,10 @@
    ```
 
    ```json
-   { "method": "account/updated", "params": { "authMode": "apikey" } }
+   {
+     "method": "account/updated",
+     "params": { "authMode": "apikey", "planType": null }
+   }
    ```
 
 ### 3) Log in with ChatGPT (browser flow)
@@ -2935,12 +3953,58 @@
    ```
 
    ```json
-   { "method": "account/updated", "params": { "authMode": "chatgpt" } }
+   {
+     "method": "account/updated",
+     "params": { "authMode": "chatgpt", "planType": "plus" }
+   }
    ```
 
-### 3b) Log in with externally managed ChatGPT tokens (`chatgptAuthTokens`)
-
-Use this mode when a host application owns the user's ChatGPT auth lifecycle and supplies tokens directly.
+### 3b) Log in with ChatGPT (device-code flow)
+
+Use this flow when your client owns the sign-in ceremony or when a browser callback is brittle.
+
+1. Start:
+
+   ```json
+   {
+     "method": "account/login/start",
+     "id": 4,
+     "params": { "type": "chatgptDeviceCode" }
+   }
+   ```
+
+   ```json
+   {
+     "id": 4,
+     "result": {
+       "type": "chatgptDeviceCode",
+       "loginId": "<uuid>",
+       "verificationUrl": "https://auth.openai.com/codex/device",
+       "userCode": "ABCD-1234"
+     }
+   }
+   ```
+
+2. Show `verificationUrl` and `userCode` to the user; the frontend owns the UX.
+3. Wait for notifications:
+
+   ```json
+   {
+     "method": "account/login/completed",
+     "params": { "loginId": "<uuid>", "success": true, "error": null }
+   }
+   ```
+
+   ```json
+   {
+     "method": "account/updated",
+     "params": { "authMode": "chatgpt", "planType": "plus" }
+   }
+   ```
+
+### 3c) Log in with externally managed ChatGPT tokens (`chatgptAuthTokens`)
+
+Use this experimental mode only when a host application owns the user's ChatGPT auth lifecycle and supplies tokens directly. Clients must set `capabilities.experimentalApi = true` during `initialize` before using this login type.
 
 1. Send:
 
@@ -2950,8 +4014,9 @@
      "id": 7,
      "params": {
        "type": "chatgptAuthTokens",
-       "idToken": "<jwt>",
-       "accessToken": "<jwt>"
+       "accessToken": "<jwt>",
+       "chatgptAccountId": "org-123",
+       "chatgptPlanType": "business"
      }
    }
    ```
@@ -2974,7 +4039,7 @@
    ```json
    {
      "method": "account/updated",
-     "params": { "authMode": "chatgptAuthTokens" }
+     "params": { "authMode": "chatgptAuthTokens", "planType": "business" }
    }
    ```
 
@@ -2986,7 +4051,7 @@
   "id": 8,
   "params": { "reason": "unauthorized", "previousAccountId": "org-123" }
 }
-{ "id": 8, "result": { "idToken": "<jwt>", "accessToken": "<jwt>" } }
+{ "id": 8, "result": { "accessToken": "<jwt>", "chatgptAccountId": "org-123", "chatgptPlanType": "business" } }
 ```
 
 The server retries the original request after a successful refresh response. Requests time out after about 10 seconds.
@@ -3003,7 +4068,7 @@
 ```json
 { "method": "account/logout", "id": 5 }
 { "id": 5, "result": {} }
-{ "method": "account/updated", "params": { "authMode": null } }
+{ "method": "account/updated", "params": { "authMode": null, "planType": null } }
 ```
 
 ### 6) Rate limits (ChatGPT)
@@ -3015,20 +4080,23 @@
     "limitId": "codex",
     "limitName": null,
     "primary": { "usedPercent": 25, "windowDurationMins": 15, "resetsAt": 1730947200 },
-    "secondary": null
+    "secondary": null,
+    "rateLimitReachedType": null
   },
   "rateLimitsByLimitId": {
     "codex": {
       "limitId": "codex",
       "limitName": null,
       "primary": { "usedPercent": 25, "windowDurationMins": 15, "resetsAt": 1730947200 },
-      "secondary": null
+      "secondary": null,
+      "rateLimitReachedType": null
     },
     "codex_other": {
       "limitId": "codex_other",
       "limitName": "codex_other",
       "primary": { "usedPercent": 42, "windowDurationMins": 60, "resetsAt": 1730950800 },
-      "secondary": null
+      "secondary": null,
+      "rateLimitReachedType": null
     }
   }
 } }
@@ -3049,6 +4117,20 @@
 - `usedPercent` is current usage within the quota window.
 - `windowDurationMins` is the quota window length.
 - `resetsAt` is a Unix timestamp (seconds) for the next reset.
+- `planType` is included when the backend returns the ChatGPT plan associated with a bucket.
+- `credits` is included when the backend returns remaining workspace credit details.
+- `rateLimitReachedType` identifies the backend-classified limit state when one has been reached.
+
+### 7) Notify a workspace owner about a limit
+
+Use `account/sendAddCreditsNudgeEmail` to ask ChatGPT to email a workspace owner when credits are depleted or a usage limit has been reached.
+
+```json
+{ "method": "account/sendAddCreditsNudgeEmail", "id": 7, "params": { "creditType": "credits" } }
+{ "id": 7, "result": { "status": "sent" } }
+```
+
+Use `creditType: "credits"` when workspace credits are depleted, or `creditType: "usage_limit"` when the workspace usage limit has been reached. If the owner was already notified recently, the response status is `cooldown_active`.
 
 ---
 
@@ -3080,7 +4162,11 @@
 
 OpenAI bills API key usage through your OpenAI Platform account at standard API rates. See the [API pricing page](https://openai.com/api/pricing/).
 
-Recommendation is to use API key authentication for programmatic Codex CLI workflows (for example CI/CD jobs). Do not expose Codex execution in untrusted or publicly triggerable environments.
+Features that rely on ChatGPT credits, such as [fast mode](https://developers.openai.com/codex/speed), are
+available only when you sign in with ChatGPT. If you sign in with an API key,
+Codex uses standard API pricing instead.
+
+Recommendation is to use API key authentication for programmatic Codex CLI workflows (for example CI/CD jobs). Don't expose Codex execution in untrusted or public environments.
 
 ## Secure your Codex cloud account
 
@@ -3140,6 +4226,25 @@
 If the active credentials don't match the configured restrictions, Codex logs the user out and exits.
 
 These settings are commonly applied via managed configuration rather than per-user setup. See [Managed configuration](https://developers.openai.com/codex/enterprise/managed-configuration).
+
+## Login diagnostics
+
+Direct `codex login` runs write a dedicated `codex-login.log` file under
+your configured log directory. Use it when you need to debug browser-login or
+device-code failures, or when support asks for login-specific logs.
+
+## Custom CA bundles
+
+If your network uses a corporate TLS proxy or private root CA, set
+`CODEX_CA_CERTIFICATE` to a PEM bundle before logging in. When
+`CODEX_CA_CERTIFICATE` is unset, Codex falls back to `SSL_CERT_FILE`. The same
+custom CA settings apply to login, normal HTTPS requests, and secure websocket
+connections.
+
+```shell
+export CODEX_CA_CERTIFICATE=/path/to/corporate-root-ca.pem
+codex login
+```
 
 ## Login on headless devices
 
@@ -3228,15 +4333,18 @@
 Codex CLI is OpenAI's coding agent that you can run locally from your terminal. It can read, change, and run code on your machine in the selected directory.
 It's [open source](https://github.com/openai/codex) and built in Rust for speed and efficiency.
 
-Codex is included with ChatGPT Plus, Pro, Business, Edu, and Enterprise plans. Learn more about [what's included](https://developers.openai.com/codex/pricing).
+ChatGPT Plus, Pro, Business, Edu, and Enterprise plans include Codex. Learn more about [what's included](https://developers.openai.com/codex/pricing).
 
 <br />
 
 ## CLI setup
 
-The Codex CLI is available on macOS and Linux. Windows support is
-  experimental. For the best Windows experience, use Codex in a WSL workspace
-  and follow our <a href="/codex/windows">Windows setup guide</a>.
+The Codex CLI is available on macOS, Windows, and Linux. On Windows, run Codex
+  natively in PowerShell with the Windows sandbox, or use WSL2 when you need a
+  Linux-native environment. For setup details, see the{" "}
+  <a href="/codex/windows">Windows setup guide</a>.
+
+If you're new to Codex, read the [best practices guide](https://developers.openai.com/codex/learn/best-practices).
 
 ---
 
@@ -3265,6 +4373,13 @@
 Attach screenshots or design specs so Codex reads them alongside your prompt.
 
   </BentoContent>
+  <BentoContent href="/codex/cli/features#image-generation">
+
+### Image generation
+
+Generate or edit images directly in the CLI, and attach references when you want Codex to iterate on an existing asset.
+
+  </BentoContent>
 
   <BentoContent href="/codex/cli/features#running-local-code-review">
 
@@ -3274,11 +4389,11 @@
 
   </BentoContent>
 
-  <BentoContent href="/codex/multi-agent">
-
-### Use multi-agent
-
-Enable experimental multi-agent collaboration and parallelize complex tasks.
+  <BentoContent href="/codex/subagents">
+
+### Use subagents
+
+Use subagents to parallelize complex tasks.
 
   </BentoContent>
 
@@ -3298,7 +4413,7 @@
 
   </BentoContent>
 
-  <BentoContent href="/codex/sdk#using-codex-cli-programmatically">
+  <BentoContent href="/codex/noninteractive">
 
 ### Scripting Codex
 
@@ -3345,10 +4460,12 @@
 
 - Send prompts, code snippets, or screenshots (see [image inputs](#image-inputs)) directly into the composer.
 - Watch Codex explain its plan before making a change, and approve or reject steps inline.
-- Read syntax-highlighted markdown code blocks and diffs in the TUI, then use `/theme` to preview and save a preferred color theme.
+- Read syntax-highlighted markdown code blocks and diffs in the TUI, then use `/theme` to preview and save a preferred theme.
 - Use `/clear` to wipe the terminal and start a fresh chat, or press <kbd>Ctrl</kbd>+<kbd>L</kbd> to clear the screen without starting a new conversation.
-- Use `/copy` to copy the latest completed Codex output. If a turn is still running, Codex copies the most recent finished output instead of in-progress text.
+- Use `/copy` or press <kbd>Ctrl</kbd>+<kbd>O</kbd> to copy the latest completed Codex output. If a turn is still running, Codex copies the most recent finished output instead of in-progress text.
+- Press <kbd>Tab</kbd> while Codex is running to queue follow-up text, slash commands, or `!` shell commands for the next turn.
 - Navigate draft history in the composer with <kbd>Up</kbd>/<kbd>Down</kbd>; Codex restores prior draft text and image placeholders.
+- Press <kbd>Ctrl</kbd>+<kbd>R</kbd> to search prompt history from the composer, then press <kbd>Enter</kbd> to accept a match or <kbd>Esc</kbd> to cancel.
 - Press <kbd>Ctrl</kbd>+<kbd>C</kbd> or use `/exit` to close the interactive session when you're done.
 
 ## Resuming conversations
@@ -3369,14 +4486,78 @@
 
 Each resumed run keeps the original transcript, plan history, and approvals, so Codex can use prior context while you supply new instructions. Override the working directory with `--cd` or add extra roots with `--add-dir` if you need to steer the environment before resuming.
 
+## Connect the TUI to a remote app server
+
+Remote TUI mode lets you run the Codex app server on one machine and use the Codex terminal UI from another machine. This is useful when the code, credentials, or execution environment live on a remote host, but you want the local interactive TUI experience.
+
+Start the app server on the machine that should own the workspace and run commands:
+
+```bash
+codex app-server --listen ws://127.0.0.1:4500
+```
+
+Then connect from the machine running the TUI:
+
+```bash
+codex --remote ws://127.0.0.1:4500
+```
+
+For access from another machine, bind the app server to a reachable interface, for example:
+
+```bash
+codex app-server --listen ws://0.0.0.0:4500
+```
+
+`--remote` accepts explicit `ws://host:port` and `wss://host:port` addresses only. For plain WebSocket connections, prefer local-host addresses or SSH port forwarding. If you expose the listener beyond the local host, configure authentication before real remote use and put authenticated non-local connections behind TLS.
+
+Codex supports these WebSocket authentication modes for remote TUI connections:
+
+- **No WebSocket auth**: Best for local-host listeners or SSH port-forwarded connections. Codex can start non-local listeners without auth, but logs a warning and the startup banner reminds you to configure auth before real remote use.
+- **Capability token**: Store a shared token in a file on the app-server host, start the server with `--ws-auth capability-token --ws-token-file /abs/path/to/token`, then set the same token in an environment variable on the TUI host and pass `--remote-auth-token-env <ENV_VAR>`.
+- **Signed bearer token**: Store an HMAC shared secret in a file on the app-server host, start the server with `--ws-auth signed-bearer-token --ws-shared-secret-file /abs/path/to/secret`, and have the TUI send a signed JWT bearer token through `--remote-auth-token-env <ENV_VAR>`. The shared secret must be at least 32 bytes. Signed tokens use HS256 and must include `exp`; Codex also validates `nbf`, `iss`, and `aud` when those claims or server options are present.
+
+To create a capability token on the app-server host, generate a random token file with permissions that only your user can read:
+
+```bash
+TOKEN_FILE="$HOME/.codex/codex-app-server-token"
+install -d -m 700 "$(dirname "$TOKEN_FILE")"
+openssl rand -base64 32 > "$TOKEN_FILE"
+chmod 600 "$TOKEN_FILE"
+```
+
+Treat the token file like a password, and regenerate it if it leaks.
+
+Then start the app server with that token file. For example, with a capability token behind a TLS proxy:
+
+```bash
+# Remote host
+TOKEN_FILE="$HOME/.codex/codex-app-server-token"
+codex app-server \
+  --listen ws://0.0.0.0:4500 \
+  --ws-auth capability-token \
+  --ws-token-file "$TOKEN_FILE"
+
+# TUI host
+export CODEX_REMOTE_AUTH_TOKEN="$(ssh devbox 'cat ~/.codex/codex-app-server-token')"
+codex --remote wss://codex-devbox.example.com:4500 \
+  --remote-auth-token-env CODEX_REMOTE_AUTH_TOKEN
+```
+
+The TUI sends remote auth tokens as `Authorization: Bearer <token>` during the WebSocket handshake. Codex only sends those tokens over `wss://` URLs or `ws://` URLs whose host is `localhost`, `127.0.0.1`, or `::1`, so put non-local remote listeners behind TLS if clients need to authenticate over the network.
+
 ## Models and reasoning
 
-For most tasks in Codex, `gpt-5.4` is the recommended model. It brings the industry-leading coding capabilities of `gpt-5.3-codex` to OpenAI's flagship frontier model, combining frontier coding performance with stronger reasoning, native computer use, and broader professional workflows. For extra fast tasks, ChatGPT Pro subscribers have access to the GPT-5.3-Codex-Spark model in research preview.
+For most tasks in Codex, `gpt-5.5` is the recommended model when it is
+available. It is OpenAI's newest frontier model for complex coding, computer
+use, knowledge work, and research workflows, with stronger planning, tool use,
+and follow-through on multi-step tasks. If `gpt-5.5` is not yet available,
+continue using `gpt-5.4`. For extra fast tasks, ChatGPT Pro subscribers have
+access to the GPT-5.3-Codex-Spark model in research preview.
 
 Switch models mid-session with the `/model` command, or specify one when launching the CLI.
 
 ```bash
-codex --model gpt-5.4
+codex --model gpt-5.5
 ```
 
 [Learn more about the models available in Codex](https://developers.openai.com/codex/models).
@@ -3393,9 +4574,13 @@
 
 `codex features enable <feature>` and `codex features disable <feature>` write to `~/.codex/config.toml`. If you launch Codex with `--profile`, Codex stores the change in that profile rather than the root configuration.
 
-## Multi-agents (experimental)
-
-Use Codex multi-agent workflows to parallelize larger tasks. For setup, role configuration (`[agents]` in `config.toml`), and examples, see [Multi-agents](https://developers.openai.com/codex/multi-agent).
+## Subagents
+
+Use Codex subagent workflows to parallelize larger tasks. For setup, role configuration (`[agents]` in `config.toml`), and examples, see [Subagents](https://developers.openai.com/codex/subagents).
+
+Codex only spawns subagents when you explicitly ask it to. Because each
+subagent does its own model and tool work, subagent workflows consume more
+tokens than comparable single-agent runs.
 
 ## Image inputs
 
@@ -3410,6 +4595,16 @@
 ```
 
 Codex accepts common formats such as PNG and JPEG. Use comma-separated filenames for two or more images, and combine them with text instructions to add context.
+
+## Image generation
+
+Ask Codex to generate or edit images directly in the CLI. This works well for assets such as icons, banners, illustrations, sprite sheets, and placeholder art. If you want Codex to transform or extend an existing asset, attach a reference image with your prompt.
+
+You can ask in natural language or explicitly invoke the image generation skill by including `$imagegen` in your prompt.
+
+Built-in image generation uses `gpt-image-2`, counts toward your general Codex usage limits, and uses included limits 3-5x faster on average than similar turns without image generation, depending on image quality and size. For details, see [Pricing](https://developers.openai.com/codex/pricing#image-generation-usage-limits). For prompting tips and model details, see the [image generation guide](https://developers.openai.com/api/docs/guides/image-generation).
+
+For larger batches of image generation, set `OPENAI_API_KEY` in your environment variables and ask Codex to generate images through the API so API pricing applies instead.
 
 ## Syntax highlighting and themes
 
@@ -3499,7 +4694,7 @@
 
 ## Slash commands
 
-Slash commands give you quick access to specialized workflows like `/review`, `/fork`, or your own reusable prompts. Codex ships with a curated set of built-ins, and you can create custom ones for team-specific tasks or personal shortcuts.
+Slash commands give you quick access to specialized workflows like `/review`, `/fork`, `/side`, or your own reusable prompts. Codex ships with a curated set of built-ins, and you can create custom ones for team-specific tasks or personal shortcuts.
 
 See the [slash commands guide](https://developers.openai.com/codex/guides/slash-commands) to browse the catalog of built-ins, learn how to author custom commands, and understand where they live on disk.
 
@@ -3518,7 +4713,7 @@
 ## Tips and shortcuts
 
 - Type `@` in the composer to open a fuzzy file search over the workspace root; press <kbd>Tab</kbd> or <kbd>Enter</kbd> to drop the highlighted path into your message.
-- Press <kbd>Enter</kbd> while Codex is running to inject new instructions into the current turn, or press <kbd>Tab</kbd> to queue a follow-up prompt for the next turn.
+- Press <kbd>Enter</kbd> while Codex is running to inject new instructions into the current turn, or press <kbd>Tab</kbd> to queue follow-up input for the next turn. Queued input can be a normal prompt, a slash command such as `/review`, or a `!` shell command. Codex parses queued slash commands when they run.
 - Prefix a line with `!` to run a local shell command (for example, `!ls`). Codex treats the output like a user-provided command result and still applies your approval and sandbox settings.
 - Tap <kbd>Esc</kbd> twice while the composer is empty to edit your previous user message. Continue pressing <kbd>Esc</kbd> to walk further back in the transcript, then hit <kbd>Enter</kbd> to fork from that point.
 - Launch Codex from any directory using `codex --cd <path>` to set the working root without running `cd` first. The active path appears in the TUI header.
@@ -3546,7 +4741,7 @@
     key: "--model, -m",
     type: "string",
     description:
-      "Override the model set in configuration (for example `gpt-5-codex`).",
+      "Override the model set in configuration (for example `gpt-5.4`).",
   },
   {
     key: "--oss",
@@ -3572,13 +4767,6 @@
     type: "untrusted | on-request | never",
     description:
       "Control when Codex pauses for human approval before running a command. `on-failure` is deprecated; prefer `on-request` for interactive runs or `never` for non-interactive runs.",
-  },
-  {
-    key: "--full-auto",
-    type: "boolean",
-    defaultValue: "false",
-    description:
-      "Shortcut for low-friction local work: sets `--ask-for-approval on-request` and `--sandbox workspace-write`.",
   },
   {
     key: "--dangerously-bypass-approvals-and-sandbox, --yolo",
@@ -3614,6 +4802,18 @@
       "Disable alternate screen mode for the TUI (overrides `tui.alternate_screen` for this run).",
   },
   {
+    key: "--remote",
+    type: "ws://host:port | wss://host:port",
+    description:
+      "Connect the interactive TUI to a remote app-server WebSocket endpoint. Supported for `codex`, `codex resume`, and `codex fork`; other subcommands reject remote mode.",
+  },
+  {
+    key: "--remote-auth-token-env",
+    type: "ENV_VAR",
+    description:
+      "Read a bearer token from this environment variable and send it when connecting with `--remote`. Requires `--remote`; tokens are only sent over `wss://` URLs or `ws://` URLs whose host is `localhost`, `127.0.0.1`, or `::1`.",
+  },
+  {
     key: "--enable",
     type: "feature",
     description:
@@ -3653,7 +4853,7 @@
     href: "/codex/cli/reference#codex-app",
     type: "stable",
     description:
-      "Launch the Codex desktop app on macOS, optionally opening a specific workspace path.",
+      "Launch the Codex desktop app on macOS or Windows. On macOS, Codex can open a workspace path; on Windows, Codex prints the path to open.",
   },
   {
     key: "codex debug app-server send-message-v2",
@@ -3661,6 +4861,13 @@
     type: "experimental",
     description:
       "Debug app-server by sending a single V2 message through the built-in test client.",
+  },
+  {
+    key: "codex debug models",
+    href: "/codex/cli/reference#codex-debug-models",
+    type: "experimental",
+    description:
+      "Print the raw model catalog Codex sees, including an option to inspect only the bundled catalog.",
   },
   {
     key: "codex apply",
@@ -3725,6 +4932,13 @@
       "Manage Model Context Protocol servers (list, add, remove, authenticate).",
   },
   {
+    key: "codex plugin marketplace",
+    href: "/codex/cli/reference#codex-plugin-marketplace",
+    type: "experimental",
+    description:
+      "Add, upgrade, or remove plugin marketplaces from Git or local sources.",
+  },
+  {
     key: "codex mcp-server",
     href: "/codex/cli/reference#codex-mcp-server",
     type: "experimental",
@@ -3750,7 +4964,14 @@
     href: "/codex/cli/reference#codex-sandbox",
     type: "experimental",
     description:
-      "Run arbitrary commands inside Codex-provided macOS seatbelt or Linux sandboxes (Landlock by default, optional bubblewrap pipeline).",
+      "Run arbitrary commands inside Codex-provided macOS, Linux, or Windows sandboxes.",
+  },
+  {
+    key: "codex update",
+    href: "/codex/cli/reference#codex-update",
+    type: "stable",
+    description:
+      "Check for and apply a Codex CLI update when the installed release supports self-update.",
   },
 ];
 
@@ -3795,7 +5016,7 @@
     type: "boolean",
     defaultValue: "false",
     description:
-      "Apply the low-friction automation preset (`workspace-write` sandbox and `on-request` approvals).",
+      "Deprecated compatibility flag. Prefer `--sandbox workspace-write`; Codex prints a warning when this flag is used.",
   },
   {
     key: "--dangerously-bypass-approvals-and-sandbox, --yolo",
@@ -3821,6 +5042,20 @@
     type: "boolean",
     defaultValue: "false",
     description: "Run without persisting session rollout files to disk.",
+  },
+  {
+    key: "--ignore-user-config",
+    type: "boolean",
+    defaultValue: "false",
+    description:
+      "Do not load `$CODEX_HOME/config.toml`. Authentication still uses `CODEX_HOME`.",
+  },
+  {
+    key: "--ignore-rules",
+    type: "boolean",
+    defaultValue: "false",
+    description:
+      "Do not load user or project execpolicy `.rules` files for this run.",
   },
   {
     key: "--output-schema",
@@ -3867,7 +5102,44 @@
     type: "stdio:// | ws://IP:PORT",
     defaultValue: "stdio://",
     description:
-      "Transport listener URL. `ws://` is experimental and intended for development/testing.",
+      "Transport listener URL. Use `ws://IP:PORT` to expose a WebSocket endpoint for remote clients.",
+  },
+  {
+    key: "--ws-auth",
+    type: "capability-token | signed-bearer-token",
+    description:
+      "Authentication mode for app-server WebSocket clients. If omitted, WebSocket auth is disabled; non-local listeners warn during startup.",
+  },
+  {
+    key: "--ws-token-file",
+    type: "absolute path",
+    description:
+      "File containing the shared capability token. Required with `--ws-auth capability-token`.",
+  },
+  {
+    key: "--ws-shared-secret-file",
+    type: "absolute path",
+    description:
+      "File containing the HMAC shared secret used to validate signed JWT bearer tokens. Required with `--ws-auth signed-bearer-token`.",
+  },
+  {
+    key: "--ws-issuer",
+    type: "string",
+    description:
+      "Expected `iss` claim for signed bearer tokens. Requires `--ws-auth signed-bearer-token`.",
+  },
+  {
+    key: "--ws-audience",
+    type: "string",
+    description:
+      "Expected `aud` claim for signed bearer tokens. Requires `--ws-auth signed-bearer-token`.",
+  },
+  {
+    key: "--ws-max-clock-skew-seconds",
+    type: "number",
+    defaultValue: "30",
+    description:
+      "Clock skew allowance when validating signed bearer token `exp` and `nbf` claims. Requires `--ws-auth signed-bearer-token`.",
   },
 ];
 
@@ -3877,13 +5149,13 @@
     type: "path",
     defaultValue: ".",
     description:
-      "Workspace path to open in Codex Desktop (`codex app` is available on macOS only).",
+      "Workspace path for Codex Desktop. On macOS, Codex opens this path; on Windows, Codex prints the path.",
   },
   {
     key: "--download-url",
     type: "url",
     description:
-      "Advanced override for the Codex desktop DMG download URL used during install.",
+      "Advanced override for the Codex desktop installer URL used during install.",
   },
 ];
 
@@ -3893,6 +5165,16 @@
     type: "string",
     description:
       "Message text sent to app-server through the built-in V2 test-client flow.",
+  },
+];
+
+export const debugModelsOptions = [
+  {
+    key: "--bundled",
+    type: "boolean",
+    defaultValue: "false",
+    description:
+      "Skip refresh and print only the model catalog bundled with the current Codex binary.",
   },
 ];
 
@@ -4050,11 +5332,36 @@
 
 export const sandboxMacOptions = [
   {
-    key: "--full-auto",
+    key: "--permissions-profile",
+    type: "NAME",
+    description:
+      "Apply a named permissions profile from the active configuration stack.",
+  },
+  {
+    key: "--cd, -C",
+    type: "DIR",
+    description:
+      "Working directory used for profile resolution and command execution. Requires `--permissions-profile`.",
+  },
+  {
+    key: "--include-managed-config",
     type: "boolean",
     defaultValue: "false",
     description:
-      "Grant write access to the current workspace and `/tmp` without approvals.",
+      "Include managed requirements while resolving an explicit permissions profile. Requires `--permissions-profile`.",
+  },
+  {
+    key: "--allow-unix-socket",
+    type: "path",
+    description:
+      "Allow the sandboxed command to bind or connect Unix sockets rooted at this path. Repeat to allow multiple paths.",
+  },
+  {
+    key: "--log-denials",
+    type: "boolean",
+    defaultValue: "false",
+    description:
+      "Capture macOS sandbox denials with `log stream` while the command runs and print them after exit.",
   },
   {
     key: "--config, -c",
@@ -4072,11 +5379,23 @@
 
 export const sandboxLinuxOptions = [
   {
-    key: "--full-auto",
+    key: "--permissions-profile",
+    type: "NAME",
+    description:
+      "Apply a named permissions profile from the active configuration stack.",
+  },
+  {
+    key: "--cd, -C",
+    type: "DIR",
+    description:
+      "Working directory used for profile resolution and command execution. Requires `--permissions-profile`.",
+  },
+  {
+    key: "--include-managed-config",
     type: "boolean",
     defaultValue: "false",
     description:
-      "Grant write access to the current workspace and `/tmp` inside the Landlock sandbox.",
+      "Include managed requirements while resolving an explicit permissions profile. Requires `--permissions-profile`.",
   },
   {
     key: "--config, -c",
@@ -4089,6 +5408,40 @@
     type: "var-args",
     description:
       "Command to execute under Landlock + seccomp. Provide the executable after `--`.",
+  },
+];
+
+export const sandboxWindowsOptions = [
+  {
+    key: "--permissions-profile",
+    type: "NAME",
+    description:
+      "Apply a named permissions profile from the active configuration stack.",
+  },
+  {
+    key: "--cd, -C",
+    type: "DIR",
+    description:
+      "Working directory used for profile resolution and command execution. Requires `--permissions-profile`.",
+  },
+  {
+    key: "--include-managed-config",
+    type: "boolean",
+    defaultValue: "false",
+    description:
+      "Include managed requirements while resolving an explicit permissions profile. Requires `--permissions-profile`.",
+  },
+  {
+    key: "--config, -c",
+    type: "key=value",
+    description:
+      "Configuration overrides applied before launching the sandbox (repeatable).",
+  },
+  {
+    key: "COMMAND...",
+    type: "var-args",
+    description:
+      "Command to execute under the native Windows sandbox. Provide the executable after `--`.",
   },
 ];
 
@@ -4211,6 +5564,24 @@
   },
 ];
 
+export const marketplaceCommands = [
+  {
+    key: "add <source>",
+    type: "[--ref REF] [--sparse PATH]",
+    description:
+      "Install a plugin marketplace from GitHub shorthand, a Git URL, an SSH URL, or a local marketplace root directory. `--sparse` is supported only for Git sources and can be repeated.",
+  },
+  {
+    key: "upgrade [marketplace-name]",
+    description:
+      "Refresh one configured Git marketplace, or all configured Git marketplaces when no name is provided.",
+  },
+  {
+    key: "remove <marketplace-name>",
+    description: "Remove a configured plugin marketplace.",
+  },
+];
+
 ## How to read this reference
 
 This page catalogs every documented Codex CLI command and flag. Use the interactive tables to search by key or description. Each section indicates whether the option is stable or experimental and calls out risky combinations.
@@ -4235,19 +5606,23 @@
 
 ### `codex` (interactive)
 
-Running `codex` with no subcommand launches the interactive terminal UI (TUI). The agent accepts the global flags above plus image attachments. Web search defaults to cached mode; use `--search` to switch to live browsing and `--full-auto` to let Codex run most commands without prompts.
+Running `codex` with no subcommand launches the interactive terminal UI (TUI). The agent accepts the global flags above plus image attachments. Web search defaults to cached mode; use `--search` to switch to live browsing. For low-friction local work, use `--sandbox workspace-write --ask-for-approval on-request`.
+
+Use `--remote ws://host:port` or `--remote wss://host:port` to connect the TUI to an app server started with `codex app-server --listen ws://IP:PORT`. Add `--remote-auth-token-env <ENV_VAR>` when the server requires a bearer token for WebSocket authentication. See [Codex CLI features](https://developers.openai.com/codex/cli/features#connect-the-tui-to-a-remote-app-server) for setup examples and authentication guidance.
 
 ### `codex app-server`
 
 Launch the Codex app server locally. This is primarily for development and debugging and may change without notice.
 
-`codex app-server --listen stdio://` keeps the default JSONL-over-stdio behavior. `--listen ws://IP:PORT` enables WebSocket transport (experimental). If you generate schemas for client bindings, add `--experimental` to include gated fields and methods.
+`codex app-server --listen stdio://` keeps the default JSONL-over-stdio behavior. `--listen ws://IP:PORT` enables WebSocket transport for app-server clients. The server accepts `ws://` listen URLs; use TLS termination or a secure proxy when clients connect with `wss://`. If you generate schemas for client bindings, add `--experimental` to include gated fields and methods.
 
 ### `codex app`
 
-Launch Codex Desktop from the terminal on macOS and optionally open a specific workspace path.
-
-`codex app` installs/opens the desktop app on macOS, then opens the provided workspace path. This subcommand is macOS-only.
+Launch Codex Desktop from the terminal on macOS or Windows. On macOS, Codex can open a specific workspace path; on Windows, Codex prints the path to open.
+
+`codex app` opens an installed Codex Desktop app, or starts the installer when
+the app is missing. On macOS, Codex opens the provided workspace path; on
+Windows, it prints the path to open after installation.
 
 ### `codex debug app-server send-message-v2`
 
@@ -4255,6 +5630,12 @@
 
 This debug flow initializes with `experimentalApi: true`, starts a thread, sends a turn, and streams server notifications. Use it to reproduce and inspect app-server protocol behavior locally.
 
+### `codex debug models`
+
+Print the raw model catalog Codex sees as JSON.
+
+Use `--bundled` when you want to inspect only the catalog bundled with the current binary, without refreshing from the remote models endpoint.
+
 ### `codex apply`
 
 Apply the most recent diff from a Codex cloud task to your local repository. You must authenticate and have access to the task.
@@ -4309,6 +5690,15 @@
 
 OAuth actions (`login`, `logout`) only work with streamable HTTP servers (and only when the server supports OAuth).
 
+### `codex plugin marketplace`
+
+Manage plugin marketplace sources that Codex can browse and install from.
+
+`codex plugin marketplace add` accepts GitHub shorthand such as `owner/repo` or
+`owner/repo@ref`, HTTP or HTTPS Git URLs, SSH Git URLs, and local marketplace
+root directories. Use `--ref` to pin a Git ref, and repeat `--sparse PATH` to
+use a sparse checkout for Git-backed marketplace repositories.
+
 ### `codex mcp-server`
 
 Run Codex as an MCP server over stdio so that other tools can connect. This command inherits global configuration overrides and exits when the downstream client closes the connection.
@@ -4329,9 +5719,15 @@
 
 #### Linux Landlock
 
+#### Windows
+
+### `codex update`
+
+Check for and apply a Codex CLI update when the installed release supports self-update. Debug builds print a message telling you to install a release build instead.
+
 ## Flag combinations and safety tips
 
-- Set `--full-auto` for unattended local work, but avoid combining it with `--dangerously-bypass-approvals-and-sandbox` unless you are inside a dedicated sandbox VM.
+- Use `--sandbox workspace-write` for unattended local work that can stay inside the workspace, and avoid `--dangerously-bypass-approvals-and-sandbox` unless you are inside a dedicated sandbox VM.
 - When you need to grant Codex write access to more directories, prefer `--add-dir` rather than forcing `--sandbox danger-full-access`.
 - Pair `--json` with `--output-last-message` in CI to capture machine-readable progress and a final natural-language summary.
 
@@ -4354,43 +5750,55 @@
 This guide shows you how to:
 
 - Find the right built-in slash command for a task
-- Steer an active session with commands like `/model`, `/personality`,
-  `/permissions`, `/experimental`, `/agent`, and `/status`
+- Steer an active session with commands like `/model`, `/fast`,
+  `/personality`, `/permissions`, `/agent`, and `/status`
 
 ## Built-in slash commands
 
 Codex ships with the following commands. Open the slash popup and start typing
 the command name to filter the list.
 
-| Command                                                                         | Purpose                                                         | When to use it                                                                                            |
-| ------------------------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
-| [`/permissions`](#update-permissions-with-permissions)                          | Set what Codex can do without asking first.                     | Relax or tighten approval requirements mid-session, such as switching between Auto and Read Only.         |
-| [`/sandbox-add-read-dir`](#grant-sandbox-read-access-with-sandbox-add-read-dir) | Grant sandbox read access to an extra directory (Windows only). | Unblock commands that need to read an absolute directory path outside the current readable roots.         |
-| [`/agent`](#switch-agent-threads-with-agent)                                    | Switch the active agent thread.                                 | Inspect or continue work in a spawned sub-agent thread.                                                   |
-| [`/apps`](#browse-apps-with-apps)                                               | Browse apps (connectors) and insert them into your prompt.      | Attach an app as `$app-slug` before asking Codex to use it.                                               |
-| [`/clear`](#clear-the-terminal-and-start-a-new-chat-with-clear)                 | Clear the terminal and start a fresh chat.                      | Reset the visible UI and conversation together when you want a clean slate.                               |
-| [`/compact`](#keep-transcripts-lean-with-compact)                               | Summarize the visible conversation to free tokens.              | Use after long runs so Codex retains key points without blowing the context window.                       |
-| [`/copy`](#copy-the-latest-response-with-copy)                                  | Copy the latest completed Codex output.                         | Grab the latest finished response or plan text without manually selecting it.                             |
-| [`/diff`](#review-changes-with-diff)                                            | Show the Git diff, including files Git isn't tracking yet.      | Review Codex's edits before you commit or run tests.                                                      |
-| [`/exit`](#exit-the-cli-with-quit-or-exit)                                      | Exit the CLI (same as `/quit`).                                 | Alternative spelling; both commands exit the session.                                                     |
-| [`/experimental`](#toggle-experimental-features-with-experimental)              | Toggle experimental features.                                   | Enable optional features such as sub-agents from the CLI.                                                 |
-| [`/feedback`](#send-feedback-with-feedback)                                     | Send logs to the Codex maintainers.                             | Report issues or share diagnostics with support.                                                          |
-| [`/init`](#generate-agentsmd-with-init)                                         | Generate an `AGENTS.md` scaffold in the current directory.      | Capture persistent instructions for the repository or subdirectory you're working in.                     |
-| [`/logout`](#sign-out-with-logout)                                              | Sign out of Codex.                                              | Clear local credentials when using a shared machine.                                                      |
-| [`/mcp`](#list-mcp-tools-with-mcp)                                              | List configured Model Context Protocol (MCP) tools.             | Check which external tools Codex can call during the session.                                             |
-| [`/mention`](#highlight-files-with-mention)                                     | Attach a file to the conversation.                              | Point Codex at specific files or folders you want it to inspect next.                                     |
-| [`/model`](#set-the-active-model-with-model)                                    | Choose the active model (and reasoning effort, when available). | Switch between general-purpose models (`gpt-4.1-mini`) and deeper reasoning models before running a task. |
-| [`/plan`](#switch-to-plan-mode-with-plan)                                       | Switch to plan mode and optionally send a prompt.               | Ask Codex to propose an execution plan before implementation work starts.                                 |
-| [`/personality`](#set-a-communication-style-with-personality)                   | Choose a communication style for responses.                     | Make Codex more concise, more explanatory, or more collaborative without changing your instructions.      |
-| [`/ps`](#check-background-terminals-with-ps)                                    | Show experimental background terminals and their recent output. | Check long-running commands without leaving the main transcript.                                          |
-| [`/fork`](#fork-the-current-conversation-with-fork)                             | Fork the current conversation into a new thread.                | Branch the active session to explore a new approach without losing the current transcript.                |
-| [`/resume`](#resume-a-saved-conversation-with-resume)                           | Resume a saved conversation from your session list.             | Continue work from a previous CLI session without starting over.                                          |
-| [`/new`](#start-a-new-conversation-with-new)                                    | Start a new conversation inside the same CLI session.           | Reset the chat context without leaving the CLI when you want a fresh prompt in the same repo.             |
-| [`/quit`](#exit-the-cli-with-quit-or-exit)                                      | Exit the CLI.                                                   | Leave the session immediately.                                                                            |
-| [`/review`](#ask-for-a-working-tree-review-with-review)                         | Ask Codex to review your working tree.                          | Run after Codex completes work or when you want a second set of eyes on local changes.                    |
-| [`/status`](#inspect-the-session-with-status)                                   | Display session configuration and token usage.                  | Confirm the active model, approval policy, writable roots, and remaining context capacity.                |
-| [`/debug-config`](#inspect-config-layers-with-debug-config)                     | Print config layer and requirements diagnostics.                | Debug precedence and policy requirements, including experimental network constraints.                     |
-| [`/statusline`](#configure-footer-items-with-statusline)                        | Configure TUI status-line fields interactively.                 | Pick and reorder footer items (model/context/limits/git/tokens/session) and persist in config.toml.       |
+When a task is already running, you can type a slash command and press `Tab` to
+queue it for the next turn. Codex parses queued slash commands when they run, so
+command menus and errors appear after the current turn finishes. Slash
+completion still works before you queue the command.
+
+| Command                                                                         | Purpose                                                         | When to use it                                                                                             |
+| ------------------------------------------------------------------------------- | --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
+| [`/permissions`](#update-permissions-with-permissions)                          | Set what Codex can do without asking first.                     | Relax or tighten approval requirements mid-session, such as switching between Auto and Read Only.          |
+| [`/sandbox-add-read-dir`](#grant-sandbox-read-access-with-sandbox-add-read-dir) | Grant sandbox read access to an extra directory (Windows only). | Unblock commands that need to read an absolute directory path outside the current readable roots.          |
+| [`/agent`](#switch-agent-threads-with-agent)                                    | Switch the active agent thread.                                 | Inspect or continue work in a spawned subagent thread.                                                     |
+| [`/apps`](#browse-apps-with-apps)                                               | Browse apps (connectors) and insert them into your prompt.      | Attach an app as `$app-slug` before asking Codex to use it.                                                |
+| [`/plugins`](#browse-plugins-with-plugins)                                      | Browse installed and discoverable plugins.                      | Inspect plugin tools, install suggested plugins, or manage plugin availability.                            |
+| [`/clear`](#clear-the-terminal-and-start-a-new-chat-with-clear)                 | Clear the terminal and start a fresh chat.                      | Reset the visible UI and conversation together when you want a fresh start.                                |
+| [`/compact`](#keep-transcripts-lean-with-compact)                               | Summarize the visible conversation to free tokens.              | Use after long runs so Codex retains key points without blowing the context window.                        |
+| [`/copy`](#copy-the-latest-response-with-copy)                                  | Copy the latest completed Codex output.                         | Grab the latest finished response or plan text without manually selecting it. You can also press `Ctrl+O`. |
+| [`/diff`](#review-changes-with-diff)                                            | Show the Git diff, including files Git isn't tracking yet.      | Review Codex's edits before you commit or run tests.                                                       |
+| [`/exit`](#exit-the-cli-with-quit-or-exit)                                      | Exit the CLI (same as `/quit`).                                 | Alternative spelling; both commands exit the session.                                                      |
+| [`/experimental`](#toggle-experimental-features-with-experimental)              | Toggle experimental features.                                   | Enable optional features such as subagents from the CLI.                                                   |
+| [`/feedback`](#send-feedback-with-feedback)                                     | Send logs to the Codex maintainers.                             | Report issues or share diagnostics with support.                                                           |
+| [`/init`](#generate-agentsmd-with-init)                                         | Generate an `AGENTS.md` scaffold in the current directory.      | Capture persistent instructions for the repository or subdirectory you're working in.                      |
+| [`/logout`](#sign-out-with-logout)                                              | Sign out of Codex.                                              | Clear local credentials when using a shared machine.                                                       |
+| [`/mcp`](#list-mcp-tools-with-mcp)                                              | List configured Model Context Protocol (MCP) tools.             | Check which external tools Codex can call during the session; add `verbose` for server details.            |
+| [`/mention`](#highlight-files-with-mention)                                     | Attach a file to the conversation.                              | Point Codex at specific files or folders you want it to inspect next.                                      |
+| [`/model`](#set-the-active-model-with-model)                                    | Choose the active model (and reasoning effort, when available). | Switch between general-purpose models (`gpt-4.1-mini`) and deeper reasoning models before running a task.  |
+| [`/fast`](#toggle-fast-mode-with-fast)                                          | Toggle Fast mode for supported models.                          | Turn Fast mode on or off, or check whether the current thread is using it.                                 |
+| [`/plan`](#switch-to-plan-mode-with-plan)                                       | Switch to plan mode and optionally send a prompt.               | Ask Codex to propose an execution plan before implementation work starts.                                  |
+| [`/goal`](#set-or-view-an-experimental-task-goal-with-goal)                     | Set or view an experimental goal for a long-running task.       | Give Codex a persistent target to track while a larger task runs. Requires `features.goals`.               |
+| [`/personality`](#set-a-communication-style-with-personality)                   | Choose a communication style for responses.                     | Make Codex more concise, more explanatory, or more collaborative without changing your instructions.       |
+| [`/ps`](#check-background-terminals-with-ps)                                    | Show experimental background terminals and their recent output. | Check long-running commands without leaving the main transcript.                                           |
+| [`/stop`](#stop-background-terminals-with-stop)                                 | Stop all background terminals.                                  | Cancel background terminal work started by the current session.                                            |
+| [`/fork`](#fork-the-current-conversation-with-fork)                             | Fork the current conversation into a new thread.                | Branch the active session to explore a new approach without losing the current transcript.                 |
+| [`/side`](#start-a-side-conversation-with-side)                                 | Start an ephemeral side conversation.                           | Ask a focused follow-up without disrupting the main thread's transcript.                                   |
+| [`/resume`](#resume-a-saved-conversation-with-resume)                           | Resume a saved conversation from your session list.             | Continue work from a previous CLI session without starting over.                                           |
+| [`/new`](#start-a-new-conversation-with-new)                                    | Start a new conversation inside the same CLI session.           | Reset the chat context without leaving the CLI when you want a fresh prompt in the same repo.              |
+| [`/quit`](#exit-the-cli-with-quit-or-exit)                                      | Exit the CLI.                                                   | Leave the session immediately.                                                                             |
+| [`/review`](#ask-for-a-working-tree-review-with-review)                         | Ask Codex to review your working tree.                          | Run after Codex completes work or when you want a second set of eyes on local changes.                     |
+| [`/status`](#inspect-the-session-with-status)                                   | Display session configuration and token usage.                  | Confirm the active model, approval policy, writable roots, and remaining context capacity.                 |
+| [`/debug-config`](#inspect-config-layers-with-debug-config)                     | Print config layer and requirements diagnostics.                | Debug precedence and policy requirements, including experimental network constraints.                      |
+| [`/statusline`](#configure-footer-items-with-statusline)                        | Configure TUI status-line fields interactively.                 | Pick and reorder footer items (model/context/limits/git/tokens/session) and persist in config.toml.        |
+| [`/title`](#configure-terminal-title-items-with-title)                          | Configure terminal window or tab title fields interactively.    | Pick and reorder title items such as project, status, thread, branch, model, and task progress.            |
+| [`/keymap`](#remap-tui-shortcuts-with-keymap)                                   | Remap TUI keyboard shortcuts.                                   | Inspect and persist custom shortcut bindings in `config.toml`.                                             |
 
 `/quit` and `/exit` both exit the CLI. Use them only after you have saved or
 committed any important work.
@@ -4408,6 +5816,13 @@
 3. Choose a model such as `gpt-4.1-mini` or `gpt-4.1` from the popup.
 
 Expected: Codex confirms the new model in the transcript. Run `/status` to verify the change.
+
+### Toggle Fast mode with `/fast`
+
+1. Type `/fast on`, `/fast off`, or `/fast status`.
+2. If you want the setting to persist, confirm the update when Codex offers to save it.
+
+Expected: Codex reports whether Fast mode is on or off for the current thread. In the TUI footer, you can also show a Fast mode status-line item with `/statusline`.
 
 ### Set a communication style with `/personality`
 
@@ -4436,10 +5851,20 @@
 
 While a task is already running, `/plan` is temporarily unavailable.
 
+### Set an experimental goal with `/goal`
+
+`/goal` is experimental and only available when `features.goals` is enabled. To enable it, open `/experimental` or add `goals = true` under `[features]` in `config.toml`.
+
+1. Type `/goal <objective>` to set the goal, for example `/goal Finish the migration and keep tests green`.
+2. Type `/goal` to view the current goal.
+3. Use `/goal pause`, `/goal resume`, or `/goal clear` to pause, resume, or remove it.
+
+Expected: Codex keeps the goal attached to the active thread while work continues.
+
 ### Toggle experimental features with `/experimental`
 
 1. Type `/experimental` and press Enter.
-2. Toggle the features you want (for example, **Multi-agents**), then restart Codex.
+2. Toggle the features you want (for example, Apps or Smart Approvals), then restart Codex if the prompt asks you to.
 
 Expected: Codex saves your feature choices to config and applies them on restart.
 
@@ -4474,6 +5899,9 @@
 the in-progress response. The command is unavailable before the first completed
 Codex output and immediately after a rollback.
 
+You can also press <kbd>Ctrl</kbd>+<kbd>O</kbd> from the main TUI to copy the
+latest completed response without opening the slash command menu.
+
 ### Grant sandbox read access with `/sandbox-add-read-dir`
 
 This command is available only when running the CLI natively on Windows.
@@ -4516,6 +5944,29 @@
 limits, git branch, token counters, session id, current directory/project root,
 and Codex version.
 
+### Configure terminal title items with `/title`
+
+1. Type `/title`.
+2. Use the picker to toggle and reorder items, then confirm.
+
+Expected: The terminal window or tab title updates immediately and persists to
+`tui.terminal_title` in `config.toml`.
+
+Available title items include app name, project, spinner, status, thread, git
+branch, model, and task progress.
+
+### Remap TUI shortcuts with `/keymap`
+
+Use `/keymap` to inspect, update, and persist keyboard shortcut bindings for the TUI.
+
+1. Type `/keymap`.
+2. Pick the shortcut context and action you want to change.
+3. Enter the new binding or remove the existing one.
+
+Expected: Codex updates the active keymap and writes the custom binding to `tui.keymap` in `config.toml`.
+
+Key bindings use names such as `ctrl-a`, `shift-enter`, and `page-down`. Context-specific bindings override `tui.keymap.global`; an empty binding list unbinds the action.
+
 ### Check background terminals with `/ps`
 
 1. Type `/ps`.
@@ -4526,6 +5977,14 @@
 
 Background terminals appear when `unified_exec` is in use; otherwise, the list may be empty.
 
+### Stop background terminals with `/stop`
+
+1. Type `/stop`.
+2. Confirm if Codex asks before stopping the listed terminals.
+
+Expected: Codex stops all background terminals for the current session. `/clean`
+is still available as an alias for `/stop`.
+
 ### Keep transcripts lean with `/compact`
 
 1. After a long exchange, type `/compact`.
@@ -4556,7 +6015,7 @@
 Expected: Codex starts a fresh conversation in the same CLI session, so you
 can switch tasks without leaving your terminal.
 
-Unlike `/clear`, `/new` does not clear the current terminal view first.
+Unlike `/clear`, `/new` doesn't clear the current terminal view first.
 
 ### Resume a saved conversation with `/resume`
 
@@ -4577,6 +6036,18 @@
 If you need to fork a saved session instead of the current one, run
 `codex fork` in your terminal to open the session picker.
 
+### Start a side conversation with `/side`
+
+Use `/side` to start an ephemeral fork from the current conversation without switching away from the main task.
+
+1. Type `/side` to open a side conversation.
+2. Optionally add inline text, for example `/side Check whether this plan has an obvious risk`.
+3. Return to the parent thread after the focused detour finishes.
+
+Expected: Codex opens a side conversation whose transcript is separate from the parent thread. While you are in side mode, the TUI continues to show parent-thread status so you can see whether the main task is still running.
+
+`/side` is unavailable inside another side conversation and during review mode.
+
 ### Generate `AGENTS.md` with `/init`
 
 1. Run `/init` in the directory where you want Codex to look for persistent instructions.
@@ -4601,6 +6072,8 @@
 
 Expected: You see the configured Model Context Protocol (MCP) tools Codex can call in this session.
 
+Use `/mcp verbose` to include detailed server diagnostics. If you pass anything other than `verbose`, Codex shows the command usage.
+
 ### Browse apps with `/apps`
 
 1. Type `/apps`.
@@ -4608,6 +6081,15 @@
 
 Expected: Codex inserts the app mention into the composer as `$app-slug`, so
 you can immediately ask Codex to use it.
+
+### Browse plugins with `/plugins`
+
+1. Type `/plugins`.
+2. Choose a marketplace tab, then pick a plugin to inspect its capabilities or available actions.
+
+Expected: Codex opens the plugin browser so you can review installed plugins,
+discoverable plugins that your configuration allows, and installed plugin state.
+Press <kbd>Space</kbd> on an installed plugin to toggle its enabled state.
 
 ### Switch agent threads with `/agent`
 
@@ -4961,11 +6443,14 @@
 In Codex, customization comes from a few layers that work together:
 
 - **Project guidance (`AGENTS.md`)** for persistent instructions
+- **[Memories](https://developers.openai.com/codex/memories)** for useful context learned from prior work
 - **Skills** for reusable workflows and domain expertise
 - **[MCP](https://developers.openai.com/codex/mcp)** for access to external tools and shared systems
-- **[Multi-agents](https://developers.openai.com/codex/concepts/multi-agents)** for delegating work to specialized sub-agents
-
-These are complementary, not competing. `AGENTS.md` shapes behavior, skills package repeatable processes, and [MCP](https://developers.openai.com/codex/mcp) connects Codex to systems outside the local workspace.
+- **[Subagents](https://developers.openai.com/codex/concepts/subagents)** for delegating work to specialized subagents
+
+These are complementary, not competing. `AGENTS.md` shapes behavior, memories
+carry local context forward, skills package repeatable processes, and
+[MCP](https://developers.openai.com/codex/mcp) connects Codex to systems outside the local workspace.
 
 ## AGENTS Guidance
 
@@ -4975,7 +6460,7 @@
 
 - Build and test commands
 - Review expectations
-- Repo-specific conventions
+- repo-specific conventions
 - Directory-specific instructions
 
 When the agent makes incorrect assumptions about your codebase, correct them in `AGENTS.md` and ask the agent to update `AGENTS.md` so the fix persists. Treat it as a feedback loop.
@@ -5003,6 +6488,12 @@
 Skills are often the best fit for reusable workflows because they support richer instructions, scripts, and references while staying reusable across tasks.
 Skills are loaded and visible to the agent (at least their metadata), so Codex can discover and choose them implicitly. This keeps rich workflows available without bloating context up front.
 
+Use skill folders to author and iterate on workflows locally. If a plugin
+already exists for the workflow, install it first to reuse a proven setup. When
+you want to distribute your own workflow across teams or bundle it with app
+integrations, package it as a [plugin](https://developers.openai.com/codex/plugins/build). Skills remain the
+authoring format; plugins are the installable distribution unit.
+
 A skill is typically a `SKILL.md` file plus optional scripts, references, and assets.
 
 The skill directory can include a `scripts/` folder with CLI scripts that Codex invokes as part of the workflow (for example, seed data or run validations). When the workflow needs external systems (issue trackers, design tools, docs servers), pair the skill with [MCP](https://developers.openai.com/codex/mcp).
@@ -5029,10 +6520,10 @@
 
 Skills can be global (in your user directory, for you as a developer) or repo-specific (checked into `.agents/skills`, for your team). Put repo skills in `.agents/skills` when the workflow applies to that project; use your user directory for skills you want across all repos.
 
-| Layer  | Global                 | Repo                                    |
-| :----- | :--------------------- | :-------------------------------------- |
-| AGENTS | `~/.codex/AGENTS.md`   | `AGENTS.md` in repo root or nested dirs |
-| Skills | `$HOME/.agents/skills` | `.agents/skills` in repo                |
+| Layer  | Global                 | Repo                                           |
+| :----- | :--------------------- | :--------------------------------------------- |
+| AGENTS | `~/.codex/AGENTS.md`   | `AGENTS.md` in repo root or nested directories |
+| Skills | `$HOME/.agents/skills` | `.agents/skills` in repo                       |
 
 Codex uses progressive disclosure for skills:
 
@@ -5047,11 +6538,11 @@
 ## MCP
 
 MCP (Model Context Protocol) is the standard way to connect Codex to external tools and context providers.
-It's especially useful for remotely hosted systems such as Figma, Linear, Jira, GitHub, or internal knowledge services your team depends on.
+It's especially useful for remotely hosted systems such as Figma, Linear, GitHub, or internal knowledge services your team depends on.
 
 Use MCP when Codex needs capabilities that live outside the local repo, such as issue trackers, design tools, browsers, or shared documentation systems.
 
-A useful mental model:
+One way to think about it:
 
 - **Host**: Codex
 - **Client**: the MCP connection inside Codex
@@ -5071,11 +6562,11 @@
 
 [Model Context Protocol](https://developers.openai.com/codex/mcp)
 
-## Multi-agents
-
-You can create different agents with different roles and prompt them to use tools differently. For example, one agent might run specific testing commands and configurations, while another has MCP servers that fetch production logs for debugging. Each sub-agent stays focused and uses the right tools for its job.
-
-[Multi-agents concepts](https://developers.openai.com/codex/concepts/multi-agents)
+## Subagents
+
+You can create different agents with different roles and prompt them to use tools differently. For example, one agent might run specific testing commands and configurations, while another has MCP servers that fetch production logs for debugging. Each subagent stays focused and uses the right tools for its job.
+
+[Subagent concepts](https://developers.openai.com/codex/concepts/subagents)
 
 ## Skills + MCP together
 
@@ -5087,9 +6578,9 @@
 Build in this order:
 
 1. [Custom instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md) so Codex follows your repo conventions. Add pre-commit hooks and linters to enforce those rules.
-2. [Skills](https://developers.openai.com/codex/skills) so you never have the same conversation twice. Skills can include a `scripts/` directory with CLI scripts or pair with [MCP](https://developers.openai.com/codex/mcp) for external systems.
-3. [MCP](https://developers.openai.com/codex/mcp) when workflows need external systems (Linear, JIRA, docs servers, design tools).
-4. [Multi-agents](https://developers.openai.com/codex/multi-agent) when you're ready to delegate noisy or specialized tasks to sub-agents.
+2. Install a [plugin](https://developers.openai.com/codex/plugins) when a reusable workflow already exists. Otherwise, create a [skill](https://developers.openai.com/codex/skills) and package it as a plugin when you want to share it.
+3. [MCP](https://developers.openai.com/codex/mcp) when workflows need external systems (Linear, GitHub, docs servers, design tools).
+4. [Subagents](https://developers.openai.com/codex/subagents) when you're ready to delegate noisy or specialized tasks to subagents.
 
 ---
 
@@ -5136,65 +6627,9 @@
 
 ---
 
-# Multi-agents
-
-Codex can run multi-agent workflows by spawning specialized agents in parallel and collecting their results in one response.
-
-This page explains the core concepts and tradeoffs. For setup, agent configuration, and examples, see [Multi-agents](https://developers.openai.com/codex/multi-agent).
-
-## Why multi-agent workflows help
-
-Even with large context windows, models have limits. If you flood the main conversation (where you're defining requirements, constraints, and decisions) with noisy intermediate output such as exploration notes, test logs, stack traces, and command output, the session can become less reliable over time.
-
-This is often described as:
-
-- **Context pollution**: useful information gets buried under noisy intermediate output.
-- **Context rot**: performance degrades as the conversation fills up with less relevant details.
-
-For background, see Chroma's writeup on [context rot](https://research.trychroma.com/context-rot).
-
-Multi-agent workflows help by moving noisy work off the main thread:
-
-- Keep the **main agent** focused on requirements, decisions, and final outputs.
-- Run specialized **sub-agents** in parallel for exploration, tests, or log analysis.
-- Return **summaries** from sub-agents instead of raw intermediate output.
-
-As a starting point, use parallel agents for tasks that mostly read (exploration, tests, triage, and summarization). Be more careful with parallel write-heavy workflows, because multiple agents editing code at once can create conflicts and increase coordination overhead.
-
-## Core terms
-
-Codex uses a few related terms in multi-agent workflows:
-
-- **Multi-agent**: A workflow where Codex runs multiple agents in parallel and combines their results.
-- **Sub-agent**: A delegated agent that Codex starts to handle a specific task.
-- **Agent thread**: The CLI thread for an agent, which you can inspect and switch between with `/agent`.
-
-## Choosing models and reasoning
-
-Different agents benefit from different model and reasoning settings.
-
-`gpt-5.3-codex-spark` is available in research preview for ChatGPT Pro
-  subscribers. See [Models](https://developers.openai.com/codex/models) for current availability. If you're
-  using Codex via the API, use GPT-5.2-Codex today.
-
-### Model choice
-
-- **`gpt-5.3-codex`**: Use for agents that need stronger reasoning, such as code review, security analysis, multi-step implementation, or tasks with ambiguous requirements. The main agent and agents that propose or apply edits usually fit here.
-- **`gpt-5.3-codex-spark`**: Use for agents that prioritize speed over depth, such as exploration, read-heavy scans, or quick summarization tasks. Spark works well for parallel workers that return distilled results to the main agent.
-
-### Reasoning effort (`model_reasoning_effort`)
-
-- **`high`**: Use when an agent needs to trace complex logic, validate assumptions, or work through edge cases (for example, reviewer or security-focused agents).
-- **`medium`**: A balanced default for most agents.
-- **`low`**: Use when the task is straightforward and speed matters most.
-
-Higher reasoning effort increases response time and token usage, but it can improve quality for complex work. For details, see [Models](https://developers.openai.com/codex/models), [Config basics](https://developers.openai.com/codex/config-basic), and [Configuration Reference](https://developers.openai.com/codex/config-reference).
-
----
-
-# Sandboxing
-
-Sandboxing is the boundary that lets Codex act autonomously without giving it
+# Sandbox
+
+The sandbox is the boundary that lets Codex act autonomously without giving it
 unrestricted access to your machine. When Codex runs local commands in the
 **Codex app**, **IDE extension**, or **CLI**, those commands run inside a
 constrained environment instead of running with full access by default.
@@ -5215,20 +6650,97 @@
 those commands inherit the same sandbox boundaries.
 
 Codex uses platform-native enforcement on each OS. The implementation differs
-between macOS, Linux, WSL, and native Windows, but the idea is the same across
+between macOS, Linux, WSL2, and native Windows, but the idea is the same across
 surfaces: give the agent a bounded place to work so routine tasks can run
 autonomously inside clear limits.
 
 ## Why it matters
 
-Sandboxing reduces approval fatigue. Instead of asking you to confirm every
+The sandbox reduces approval fatigue. Instead of asking you to confirm every
 low-risk command, Codex can read files, make edits, and run routine project
 commands within the boundary you already approved.
 
-It also gives you a clearer trust model for agentic work. You are not just
+It also gives you a clearer trust model for agentic work. You aren't just
 trusting the agent's intentions; you are trusting that the agent is operating
 inside enforced limits. That makes it easier to let Codex work independently
 while still knowing when it will stop and ask for help.
+
+## Getting started
+
+Codex applies sandboxing automatically when you use the default permissions
+mode.
+
+### Prerequisites
+
+On **macOS**, sandboxing works out of the box using the built-in Seatbelt
+framework.
+
+On **Windows**, Codex uses the native [Windows
+sandbox](https://developers.openai.com/codex/windows#windows-sandbox) when you run in PowerShell and the
+Linux sandbox implementation when you run in WSL2.
+
+On **Linux and WSL2**, install `bubblewrap` with your package manager first:
+
+
+
+<div slot="ubuntu-debian">
+
+```bash
+sudo apt install bubblewrap
+```
+
+  </div>
+
+  <div slot="fedora">
+
+```bash
+sudo dnf install bubblewrap
+```
+
+  </div>
+
+
+
+Codex uses the first `bwrap` executable it finds on `PATH`. If no `bwrap`
+executable is available, Codex falls back to a bundled helper, but that helper
+requires support for unprivileged user namespace creation. Installing the
+distribution package that provides `bwrap` keeps this setup reliable.
+
+Codex surfaces a startup warning when `bwrap` is missing or when the helper
+can't create the needed user namespace. On distributions that restrict this
+AppArmor setting, prefer loading the `bwrap` AppArmor profile so `bwrap` can
+keep working without disabling the restriction globally.
+
+**Ubuntu AppArmor note:** On Ubuntu 25.04, installing `bubblewrap` from
+  Ubuntu's package repository should work without extra AppArmor setup. The
+  `bwrap-userns-restrict` profile ships in the `apparmor` package at
+  `/etc/apparmor.d/bwrap-userns-restrict`.
+
+On Ubuntu 24.04, Codex may still warn that it can't create the needed user
+namespace after `bubblewrap` is installed. Copy and load the extra profile:
+
+```bash
+sudo apt update
+sudo apt install apparmor-profiles apparmor-utils
+sudo install -m 0644 \
+  /usr/share/apparmor/extra-profiles/bwrap-userns-restrict \
+  /etc/apparmor.d/bwrap-userns-restrict
+sudo apparmor_parser -r /etc/apparmor.d/bwrap-userns-restrict
+```
+
+`apparmor_parser -r` loads the profile into the kernel without a reboot. You
+can also reload all AppArmor profiles:
+
+```bash
+sudo systemctl reload apparmor.service
+```
+
+If that profile is unavailable or does not resolve the issue, you can disable
+the AppArmor unprivileged user namespace restriction with:
+
+```bash
+sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0
+```
 
 ## How you control it
 
@@ -5261,7 +6773,7 @@
 
 At a high level, the common sandbox modes are:
 
-- `read-only`: Codex can inspect files, but it cannot edit files or run
+- `read-only`: Codex can inspect files, but it can't edit files or run
   commands without approval.
 - `workspace-write`: Codex can read files, edit within the workspace, and run
   routine local commands inside that boundary. This is the default low-friction
@@ -5272,21 +6784,31 @@
 
 The common approval policies are:
 
-- `untrusted`: Codex asks before running commands that are not in its trusted
+- `untrusted`: Codex asks before running commands that aren't in its trusted
   set.
 - `on-request`: Codex works inside the sandbox by default and asks when it
   needs to go beyond that boundary.
-- `never`: Codex does not stop for approval prompts.
+- `never`: Codex doesn't stop for approval prompts.
 
 Full access means using `sandbox_mode = "danger-full-access"` together with
-`approval_policy = "never"`. By contrast, `--full-auto` is the lower-risk local
-automation preset: `sandbox_mode = "workspace-write"` and
-`approval_policy = "on-request"`.
+`approval_policy = "never"`. By contrast, the lower-risk local automation
+preset is `sandbox_mode = "workspace-write"` together with
+`approval_policy = "on-request"`, or the matching CLI flags
+`--sandbox workspace-write --ask-for-approval on-request`.
 
 If you need Codex to work across more than one directory, writable roots let
 you extend the places it can modify without removing the sandbox entirely. If
 you need a broader or narrower trust boundary, adjust the default sandbox mode
-and approval policy instead of relying on ad hoc exceptions.
+and approval policy instead of relying on one-off exceptions.
+
+For reusable permission sets, set `default_permissions` to a named profile and
+define `[permissions.<name>.filesystem]` or `[permissions.<name>.network]`.
+Managed network profiles use map tables such as
+`[permissions.<name>.network.domains]` and
+`[permissions.<name>.network.unix_sockets]` for domain and socket rules.
+Filesystem profiles can also deny reads for exact paths or glob patterns by
+setting matching entries to `"none"`; use this to keep files such as local
+secrets unreadable without turning off workspace writes.
 
 When a workflow needs a specific exception, use [rules](https://developers.openai.com/codex/rules). Rules
 let you allow, prompt, or forbid command prefixes outside the sandbox, which is
@@ -5295,6 +6817,12 @@
 [Codex app features](https://developers.openai.com/codex/app/features#approvals-and-sandboxing), and for the
 IDE-specific settings entry points, see [Codex IDE extension settings](https://developers.openai.com/codex/ide/settings).
 
+Automatic review, when available, doesn't change the sandbox boundary. It
+reviews approval requests, such as sandbox escalations or network access, while
+actions already allowed inside the sandbox run without extra review. See
+[Automatic approval reviews](https://developers.openai.com/codex/agent-approvals-security#automatic-approval-reviews)
+for the policy behavior.
+
 Platform details live in the platform-specific docs. For native Windows setup,
 behavior, and troubleshooting, see [Windows](https://developers.openai.com/codex/windows). For admin
 requirements and organization-level constraints on sandboxing and approvals, see
@@ -5302,11 +6830,106 @@
 
 ---
 
+# Subagents
+
+Codex can run subagent workflows by spawning specialized agents in parallel so
+they can explore, tackle, or analyze work concurrently.
+
+This page explains the core concepts and tradeoffs. For setup, agent configuration, and examples, see [Subagents](https://developers.openai.com/codex/subagents).
+
+## Why subagent workflows help
+
+Even with large context windows, models have limits. If you flood the main conversation (where you're defining requirements, constraints, and decisions) with noisy intermediate output such as exploration notes, test logs, stack traces, and command output, the session can become less reliable over time.
+
+This is often described as:
+
+- **Context pollution**: useful information gets buried under noisy intermediate output.
+- **Context rot**: performance degrades as the conversation fills up with less relevant details.
+
+For background, see the Chroma writeup on [context rot](https://research.trychroma.com/context-rot).
+
+Subagent workflows help by moving noisy work off the main thread:
+
+- Keep the **main agent** focused on requirements, decisions, and final outputs.
+- Run specialized **subagents** in parallel for exploration, tests, or log analysis.
+- Return **summaries** from subagents instead of raw intermediate output.
+
+They can also save time when the work can run independently in parallel, and
+they make larger-shaped tasks more tractable by breaking them into bounded
+pieces. For example, Codex can split analysis of a multi-million-token
+document into smaller problems and return distilled takeaways to the main
+thread.
+
+As a starting point, use parallel agents for read-heavy tasks such as
+exploration, tests, triage, and summarization. Be more careful with parallel
+write-heavy workflows, because agents editing code at once can create
+conflicts and increase coordination overhead.
+
+## Core terms
+
+Codex uses a few related terms in subagent workflows:
+
+- **Subagent workflow**: A workflow where Codex runs parallel agents and combines their results.
+- **Subagent**: A delegated agent that Codex starts to handle a specific task.
+- **Agent thread**: The CLI thread for an agent, which you can inspect and switch between with `/agent`.
+
+## Triggering subagent workflows
+
+Codex doesn't spawn subagents automatically, and it should only use subagents when you
+explicitly ask for subagents or parallel agent work.
+
+In practice, manual triggering means using direct instructions such as
+"spawn two agents," "delegate this work in parallel," or "use one agent per
+point." Subagent workflows consume more tokens than comparable single-agent runs
+because each subagent does its own model and tool work.
+
+A good subagent prompt should explain how to divide the work, whether Codex
+should wait for all agents before continuing, and what summary or output to
+return.
+
+```text
+Review this branch with parallel subagents. Spawn one subagent for security risks, one for test gaps, and one for maintainability. Wait for all three, then summarize the findings by category with file references.
+```
+
+## Choosing models and reasoning
+
+Different agents need different model and reasoning settings.
+
+If you don't pin a model or `model_reasoning_effort`, Codex can choose a setup
+that balances intelligence, speed, and price for the task. It may favor
+`gpt-5.4-mini` for fast scans or a higher-effort `gpt-5.5` configuration for
+more demanding reasoning when that model is available. When you want finer
+control, steer that choice in your prompt or set `model` and
+`model_reasoning_effort` directly in the agent file.
+
+For most tasks in Codex, start with `gpt-5.5` when it is available. Continue
+  using `gpt-5.4` during the rollout if `gpt-5.5` is not yet available. Use
+  `gpt-5.4-mini` when you want a faster, lower-cost option for lighter subagent
+  work. If you have ChatGPT Pro and want near-instant text-only iteration,
+  `gpt-5.3-codex-spark` remains available in research preview.
+
+### Model choice
+
+- **`gpt-5.5`**: Start here for demanding agents when it is available. It is strongest for ambiguous, multi-step work that needs planning, tool use, validation, and follow-through across a larger context.
+- **`gpt-5.4`**: Use this when `gpt-5.5` is not yet available or when a workflow is pinned to GPT-5.4. It combines strong coding, reasoning, tool use, and broader workflows.
+- **`gpt-5.4-mini`**: Use for agents that favor speed and efficiency over depth, such as exploration, read-heavy scans, large-file review, or processing supporting documents. It works well for parallel workers that return distilled results to the main agent.
+- **`gpt-5.3-codex-spark`**: If you have ChatGPT Pro, use this research preview model for near-instant, text-only iteration when latency matters more than broader capability.
+
+### Reasoning effort (`model_reasoning_effort`)
+
+- **`high`**: Use when an agent needs to trace complex logic, check assumptions, or work through edge cases (for example, reviewer or security-focused agents).
+- **`medium`**: A balanced default for most agents.
+- **`low`**: Use when the task is straightforward and speed matters most.
+
+Higher reasoning effort increases response time and token usage, but it can improve quality for complex work. For details, see [Models](https://developers.openai.com/codex/models), [Config basics](https://developers.openai.com/codex/config-basic), and [Configuration Reference](https://developers.openai.com/codex/config-reference).
+
+---
+
 # Advanced Configuration
 
 Use these options when you need more control over providers, policies, and integrations. For a quick start, see [Config basics](https://developers.openai.com/codex/config-basic).
 
-For background on project guidance, reusable capabilities, custom slash commands, multi-agent workflows, and integrations, see [Customization](https://developers.openai.com/codex/concepts/customization). For configuration keys, see [Configuration Reference](https://developers.openai.com/codex/config-reference).
+For background on project guidance, reusable capabilities, custom slash commands, subagent workflows, and integrations, see [Customization](https://developers.openai.com/codex/concepts/customization). For configuration keys, see [Configuration Reference](https://developers.openai.com/codex/config-reference).
 
 ## Profiles
 
@@ -5319,7 +6942,7 @@
 Define profiles under `[profiles.<name>]` in `config.toml`, then run `codex --profile <name>`:
 
 ```toml
-model = "gpt-5-codex"
+model = "gpt-5.4"
 approval_policy = "on-request"
 model_catalog_json = "/Users/me/.codex/model-catalogs/default.json"
 
@@ -5378,24 +7001,64 @@
 
 For shared defaults, rules, and skills checked into repos or system paths, see [Team Config](https://developers.openai.com/codex/enterprise/admin-setup#team-config).
 
-If you just need to point the built-in OpenAI provider at an LLM proxy, router, or data-residency enabled project, set environment variable `OPENAI_BASE_URL` instead of defining a new provider. This overrides the default OpenAI endpoint without a `config.toml` change.
-
-```shell
-export OPENAI_BASE_URL="https://api.openai.com/v1"
-codex
+If you just need to point the built-in OpenAI provider at an LLM proxy, router, or data-residency enabled project, set `openai_base_url` in `config.toml` instead of defining a new provider. This changes the base URL for the built-in `openai` provider without requiring a separate `model_providers.<id>` entry.
+
+```toml
+openai_base_url = "https://us.api.openai.com/v1"
 ```
 
 ## Project config files (`.codex/config.toml`)
 
 In addition to your user config, Codex reads project-scoped overrides from `.codex/config.toml` files inside your repo. Codex walks from the project root to your current working directory and loads every `.codex/config.toml` it finds. If multiple files define the same key, the closest file to your working directory wins.
 
-For security, Codex loads project-scoped config files only when the project is trusted. If the project is untrusted, Codex ignores `.codex/config.toml` files in the project.
-
-Relative paths inside a project config (for example, `experimental_instructions_file`) are resolved relative to the `.codex/` folder that contains the `config.toml`.
+For security, Codex loads project-scoped config files only when the project is trusted. If the project is untrusted, Codex ignores project `.codex/` layers, including `.codex/config.toml`, project-local hooks, and project-local rules. User and system layers remain separate and still load.
+
+Relative paths inside a project config (for example, `model_instructions_file`) are resolved relative to the `.codex/` folder that contains the `config.toml`.
+
+## Hooks (experimental)
+
+Codex can also load lifecycle hooks from either `hooks.json` files or inline
+`[hooks]` tables in `config.toml` files that sit next to active config layers.
+
+In practice, the two most useful locations are:
+
+- `~/.codex/hooks.json`
+- `~/.codex/config.toml`
+- `<repo>/.codex/hooks.json`
+- `<repo>/.codex/config.toml`
+
+Project-local hooks load only when the project `.codex/` layer is trusted.
+User-level hooks remain independent of project trust.
+
+Turn hooks on with:
+
+```toml
+[features]
+codex_hooks = true
+```
+
+Inline TOML hooks use the same event structure as `hooks.json`:
+
+```toml
+[[hooks.PreToolUse]]
+matcher = "^Bash$"
+
+[[hooks.PreToolUse.hooks]]
+type = "command"
+command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py"'
+timeout = 30
+statusMessage = "Checking Bash command"
+```
+
+If a single layer contains both `hooks.json` and inline `[hooks]`, Codex loads
+both and warns. Prefer one representation per layer.
+
+For the current event list, input fields, output behavior, and limitations, see
+[Hooks](https://developers.openai.com/codex/hooks).
 
 ## Agent roles (`[agents]` in `config.toml`)
 
-For multi-agent role configuration (`[agents]` in `config.toml`), see [Multi-agents](https://developers.openai.com/codex/multi-agent).
+For subagent role configuration (`[agents]` in `config.toml`), see [Subagents](https://developers.openai.com/codex/subagents).
 
 ## Project root detection
 
@@ -5412,12 +7075,12 @@
 
 ## Custom model providers
 
-A model provider defines how Codex connects to a model (base URL, wire API, and optional HTTP headers).
+A model provider defines how Codex connects to a model (base URL, wire API, authentication, and optional HTTP headers). Custom providers can't reuse the reserved built-in provider IDs: `openai`, `ollama`, and `lmstudio`.
 
 Define additional providers and point `model_provider` at them:
 
 ```toml
-model = "gpt-5.1"
+model = "gpt-5.4"
 model_provider = "proxy"
 
 [model_providers.proxy]
@@ -5425,7 +7088,7 @@
 base_url = "http://proxy.example.com"
 env_key = "OPENAI_API_KEY"
 
-[model_providers.ollama]
+[model_providers.local_ollama]
 name = "Ollama"
 base_url = "http://localhost:11434/v1"
 
@@ -5442,6 +7105,41 @@
 http_headers = { "X-Example-Header" = "example-value" }
 env_http_headers = { "X-Example-Features" = "EXAMPLE_FEATURES" }
 ```
+
+Use command-backed authentication when a provider needs Codex to fetch bearer tokens from an external credential helper:
+
+```toml
+[model_providers.proxy]
+name = "OpenAI using LLM proxy"
+base_url = "https://proxy.example.com/v1"
+wire_api = "responses"
+
+[model_providers.proxy.auth]
+command = "/usr/local/bin/fetch-codex-token"
+args = ["--audience", "codex"]
+timeout_ms = 5000
+refresh_interval_ms = 300000
+```
+
+The auth command receives no `stdin` and must print the token to stdout. Codex trims surrounding whitespace, treats an empty token as an error, and refreshes proactively at `refresh_interval_ms`; set `refresh_interval_ms = 0` to refresh only after an authentication retry. Don't combine `[model_providers.<id>.auth]` with `env_key`, `experimental_bearer_token`, or `requires_openai_auth`.
+
+### Amazon Bedrock provider
+
+Codex includes a built-in `amazon-bedrock` model provider. Set it directly as
+`model_provider`; unlike custom providers, this built-in provider supports only
+the nested AWS profile and region overrides.
+
+```toml
+model_provider = "amazon-bedrock"
+model = "<bedrock-model-id>"
+
+[model_providers.amazon-bedrock.aws]
+profile = "default"
+region = "eu-central-1"
+```
+
+If you omit `profile`, Codex uses the standard AWS credential chain. Set
+`region` to the supported Bedrock region that should handle requests.
 
 ## OSS mode (local providers)
 
@@ -5461,12 +7159,12 @@
 env_key = "AZURE_OPENAI_API_KEY"
 query_params = { api-version = "2025-04-01-preview" }
 wire_api = "responses"
-
-[model_providers.openai]
 request_max_retries = 4
 stream_max_retries = 10
 stream_idle_timeout_ms = 300000
 ```
+
+To change the base URL for the built-in OpenAI provider, use `openai_base_url`; don't create `[model_providers.openai]`, because you can't override built-in provider IDs.
 
 ## ChatGPT customers using data residency
 
@@ -5494,21 +7192,73 @@
 
 Pick approval strictness (affects when Codex pauses) and sandbox level (affects file/network access).
 
-For operational details that are easy to miss while editing `config.toml`, see [Common sandbox and approval combinations](https://developers.openai.com/codex/agent-approvals-security#common-sandbox-and-approval-combinations), [Protected paths in writable roots](https://developers.openai.com/codex/agent-approvals-security#protected-paths-in-writable-roots), and [Network access](https://developers.openai.com/codex/agent-approvals-security#network-access).
-
-You can also use a granular reject policy (`approval_policy = { reject = { ... } }`) to auto-reject only selected prompt categories, such as sandbox approvals, `execpolicy` rule prompts, or MCP input requests (`mcp_elicitations`), while keeping other prompts interactive.
+For operational details to keep in mind while editing `config.toml`, see [Common sandbox and approval combinations](https://developers.openai.com/codex/agent-approvals-security#common-sandbox-and-approval-combinations), [Protected paths in writable roots](https://developers.openai.com/codex/agent-approvals-security#protected-paths-in-writable-roots), and [Network access](https://developers.openai.com/codex/agent-approvals-security#network-access).
+
+You can also use a granular approval policy (`approval_policy = { granular = { ... } }`) to allow or auto-reject individual prompt categories. This is useful when you want normal interactive approvals for some cases but want others, such as `request_permissions` or skill-script prompts, to fail closed automatically.
+
+Set `approvals_reviewer = "auto_review"` to route eligible interactive approval
+requests through automatic review. This changes the reviewer, not the sandbox
+boundary.
+
+Use `[auto_review].policy` for local reviewer policy instructions. Managed
+`guardian_policy_config` takes precedence.
 
 ```toml
-approval_policy = "untrusted"   # Other options: on-request, never, or { reject = { ... } }
+approval_policy = "untrusted"   # Other options: on-request, never, or { granular = { ... } }
+approvals_reviewer = "user"     # Or "auto_review" for automatic review
 sandbox_mode = "workspace-write"
 allow_login_shell = false       # Optional hardening: disallow login shells for shell tools
+
+# Example granular approval policy:
+# approval_policy = { granular = {
+#   sandbox_approval = true,
+#   rules = true,
+#   mcp_elicitations = true,
+#   request_permissions = false,
+#   skill_approval = false
+# } }
 
 [sandbox_workspace_write]
 exclude_tmpdir_env_var = false  # Allow $TMPDIR
 exclude_slash_tmp = false       # Allow /tmp
 writable_roots = ["/Users/YOU/.pyenv/shims"]
 network_access = false          # Opt in to outbound network
-```
+
+[auto_review]
+policy = """
+Use your organization's automatic review policy.
+"""
+```
+
+### Named permission profiles
+
+Set `default_permissions` to reuse a sandbox profile by name. Codex includes
+the built-in profiles `:read-only`, `:workspace`, and `:danger-no-sandbox`:
+
+```toml
+default_permissions = ":workspace"
+```
+
+For custom profiles, point `default_permissions` at a name you define under
+`[permissions.<name>]`:
+
+```toml
+default_permissions = "workspace"
+
+[permissions.workspace.filesystem]
+":project_roots" = { "." = "write", "**/*.env" = "none" }
+glob_scan_max_depth = 3
+
+[permissions.workspace.network]
+enabled = true
+mode = "limited"
+
+[permissions.workspace.network.domains]
+"api.openai.com" = "allow"
+```
+
+Use built-in names with a leading colon. Custom names don't use a leading
+colon and must have matching `permissions` tables.
 
 Need the complete key list (including profile-scoped overrides and requirements constraints)? See [Configuration Reference](https://developers.openai.com/codex/config-reference) and [Managed configuration](https://developers.openai.com/codex/enterprise/managed-configuration).
 
@@ -5630,35 +7380,140 @@
 
 #### Metrics catalog
 
-Each metric includes the required fields plus the default context fields above. Every metric is prefixed by `codex.`.
+Each metric includes the required fields plus the default context fields above. Metric names below omit the `codex.` prefix.
+Most metric names are centralized in `codex-rs/otel/src/metrics/names.rs`; feature-specific metrics emitted outside that file are included here too.
 If a metric includes the `tool` field, it reflects the internal tool used (for example, `apply_patch` or `shell`) and doesn't contain the actual shell command or patch `codex` is trying to apply.
 
-| Metric                                   | Type      | Fields             | Description                                                                                                                   |
-| ---------------------------------------- | --------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
-| `feature.state`                          | counter   | `feature`, `value` | Feature values that differ from defaults (emit one row per non-default).                                                      |
-| `thread.started`                         | counter   | `is_git`           | New thread created.                                                                                                           |
-| `thread.fork`                            | counter   |                    | New thread created by forking an existing thread.                                                                             |
-| `thread.rename`                          | counter   |                    | Thread renamed.                                                                                                               |
-| `task.compact`                           | counter   | `type`             | Number of compactions per type (`remote` or `local`), including manual and auto.                                              |
-| `task.user_shell`                        | counter   |                    | Number of user shell actions (`!` in the TUI for example).                                                                    |
-| `task.review`                            | counter   |                    | Number of reviews triggered.                                                                                                  |
-| `task.undo`                              | counter   |                    | Number of undo actions triggered.                                                                                             |
-| `approval.requested`                     | counter   | `tool`, `approved` | Tool approval request result (`approved`, `approved_with_amendment`, `approved_for_session`, `denied`, `abort`).              |
-| `conversation.turn.count`                | counter   |                    | User/assistant turns per thread, recorded at the end of the thread.                                                           |
-| `turn.e2e_duration_ms`                   | histogram |                    | End-to-end time for a full turn.                                                                                              |
-| `mcp.call`                               | counter   | `status`           | MCP tool invocation result (`ok` or error string).                                                                            |
-| `model_warning`                          | counter   |                    | Warning sent to the model.                                                                                                    |
-| `tool.call`                              | counter   | `tool`, `success`  | Tool invocation result (`success`: `true` or `false`).                                                                        |
-| `tool.call.duration_ms`                  | histogram | `tool`, `success`  | Tool execution time.                                                                                                          |
-| `remote_models.fetch_update.duration_ms` | histogram |                    | Time to fetch remote model definitions.                                                                                       |
-| `remote_models.load_cache.duration_ms`   | histogram |                    | Time to load the remote model cache.                                                                                          |
-| `shell_snapshot`                         | counter   | `success`          | Whether taking a shell snapshot succeeded.                                                                                    |
-| `shell_snapshot.duration_ms`             | histogram | `success`          | Time to take a shell snapshot.                                                                                                |
-| `db.init`                                | counter   | `status`           | State DB initialization outcomes (`opened`, `created`, `open_error`, `init_error`).                                           |
-| `db.backfill`                            | counter   | `status`           | Initial state DB backfill results (`upserted`, `failed`).                                                                     |
-| `db.backfill.duration_ms`                | histogram | `status`           | Duration of the initial state DB backfill, tagged with `success`, `failed`, or `partial_failure`.                             |
-| `db.error`                               | counter   | `stage`            | Errors during state DB operations (for example, `extract_metadata_from_rollout`, `backfill_sessions`, `apply_rollout_items`). |
-| `db.compare_error`                       | counter   | `stage`, `reason`  | State DB discrepancies detected during reconciliation.                                                                        |
+#### Runtime and model transport
+
+| Metric                                          | Type      | Fields               | Description                                                  |
+| ----------------------------------------------- | --------- | -------------------- | ------------------------------------------------------------ |
+| `api_request`                                   | counter   | `status`, `success`  | API request count by HTTP status and success/failure.        |
+| `api_request.duration_ms`                       | histogram | `status`, `success`  | API request duration in milliseconds.                        |
+| `sse_event`                                     | counter   | `kind`, `success`    | SSE event count by event kind and success/failure.           |
+| `sse_event.duration_ms`                         | histogram | `kind`, `success`    | SSE event processing duration in milliseconds.               |
+| `websocket.request`                             | counter   | `success`            | WebSocket request count by success/failure.                  |
+| `websocket.request.duration_ms`                 | histogram | `success`            | WebSocket request duration in milliseconds.                  |
+| `websocket.event`                               | counter   | `kind`, `success`    | WebSocket message/event count by type and success/failure.   |
+| `websocket.event.duration_ms`                   | histogram | `kind`, `success`    | WebSocket message/event processing duration in milliseconds. |
+| `responses_api_overhead.duration_ms`            | histogram |                      | Responses API overhead timing from websocket responses.      |
+| `responses_api_inference_time.duration_ms`      | histogram |                      | Responses API inference timing from websocket responses.     |
+| `responses_api_engine_iapi_ttft.duration_ms`    | histogram |                      | Responses API engine IAPI time-to-first-token timing.        |
+| `responses_api_engine_service_ttft.duration_ms` | histogram |                      | Responses API engine service time-to-first-token timing.     |
+| `responses_api_engine_iapi_tbt.duration_ms`     | histogram |                      | Responses API engine IAPI time-between-token timing.         |
+| `responses_api_engine_service_tbt.duration_ms`  | histogram |                      | Responses API engine service time-between-token timing.      |
+| `transport.fallback_to_http`                    | counter   | `from_wire_api`      | WebSocket-to-HTTP fallback count.                            |
+| `remote_models.fetch_update.duration_ms`        | histogram |                      | Time to fetch remote model definitions.                      |
+| `remote_models.load_cache.duration_ms`          | histogram |                      | Time to load the remote model cache.                         |
+| `startup_prewarm.duration_ms`                   | histogram | `status`             | Startup prewarm duration by outcome.                         |
+| `startup_prewarm.age_at_first_turn_ms`          | histogram | `status`             | Startup prewarm age when the first real turn resolves it.    |
+| `cloud_requirements.fetch.duration_ms`          | histogram |                      | Workspace-managed cloud requirements fetch duration.         |
+| `cloud_requirements.fetch_attempt`              | counter   | See note             | Workspace-managed cloud requirements fetch attempts.         |
+| `cloud_requirements.fetch_final`                | counter   | See note             | Final workspace-managed cloud requirements fetch outcome.    |
+| `cloud_requirements.load`                       | counter   | `trigger`, `outcome` | Workspace-managed cloud requirements load outcome.           |
+
+The `cloud_requirements.fetch_attempt` metric includes `trigger`, `attempt`, `outcome`, and `status_code` fields. The `cloud_requirements.fetch_final` metric includes `trigger`, `outcome`, `reason`, `attempt_count`, and `status_code` fields.
+
+#### Turn and tool activity
+
+| Metric                                 | Type      | Fields                                                                    | Description                                                                                                      |
+| -------------------------------------- | --------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
+| `turn.e2e_duration_ms`                 | histogram |                                                                           | End-to-end time for a full turn.                                                                                 |
+| `turn.ttft.duration_ms`                | histogram |                                                                           | Time to first token for a turn.                                                                                  |
+| `turn.ttfm.duration_ms`                | histogram |                                                                           | Time to first model output item for a turn.                                                                      |
+| `turn.network_proxy`                   | counter   | `active`, `tmp_mem_enabled`                                               | Whether the managed network proxy was active for the turn.                                                       |
+| `turn.memory`                          | counter   | `read_allowed`, `feature_enabled`, `config_use_memories`, `has_citations` | Per-turn memory read availability and memory citation usage.                                                     |
+| `turn.tool.call`                       | histogram | `tmp_mem_enabled`                                                         | Number of tool calls in the turn.                                                                                |
+| `turn.token_usage`                     | histogram | `token_type`, `tmp_mem_enabled`                                           | Per-turn token usage by token type (`total`, `input`, `cached_input`, `output`, or `reasoning_output`).          |
+| `tool.call`                            | counter   | `tool`, `success`                                                         | Tool invocation count by tool name and success/failure.                                                          |
+| `tool.call.duration_ms`                | histogram | `tool`, `success`                                                         | Tool execution duration in milliseconds by tool name and outcome.                                                |
+| `tool.unified_exec`                    | counter   | `tty`                                                                     | Unified exec tool calls by TTY mode.                                                                             |
+| `approval.requested`                   | counter   | `tool`, `approved`                                                        | Tool approval request result (`approved`, `approved_with_amendment`, `approved_for_session`, `denied`, `abort`). |
+| `mcp.call`                             | counter   | See note                                                                  | MCP tool invocation result.                                                                                      |
+| `mcp.call.duration_ms`                 | histogram | See note                                                                  | MCP tool invocation duration.                                                                                    |
+| `mcp.tools.list.duration_ms`           | histogram | `cache`                                                                   | MCP tool-list duration, including cache hit/miss state.                                                          |
+| `mcp.tools.fetch_uncached.duration_ms` | histogram |                                                                           | Duration of uncached MCP tool fetches.                                                                           |
+| `mcp.tools.cache_write.duration_ms`    | histogram |                                                                           | Duration of Codex Apps MCP tool-cache writes.                                                                    |
+| `hooks.run`                            | counter   | `hook_name`, `source`, `status`                                           | Hook run count by hook name, source, and status.                                                                 |
+| `hooks.run.duration_ms`                | histogram | `hook_name`, `source`, `status`                                           | Hook run duration in milliseconds.                                                                               |
+
+The `mcp.call` and `mcp.call.duration_ms` metrics include `status`; normal tool-call emissions also include `tool`, plus `connector_id` and `connector_name` when available. Blocked Codex Apps MCP calls may emit `mcp.call` with only `status`.
+
+#### Threads, tasks, and features
+
+| Metric                            | Type      | Fields                | Description                                                                      |
+| --------------------------------- | --------- | --------------------- | -------------------------------------------------------------------------------- |
+| `feature.state`                   | counter   | `feature`, `value`    | Feature values that differ from defaults (emit one row per non-default).         |
+| `status_line`                     | counter   |                       | Session started with a configured status line.                                   |
+| `model_warning`                   | counter   |                       | Warning sent to the model.                                                       |
+| `thread.started`                  | counter   | `is_git`              | New thread created, tagged by whether the working directory is in a Git repo.    |
+| `conversation.turn.count`         | counter   |                       | User/assistant turns per thread, recorded at the end of the thread.              |
+| `thread.fork`                     | counter   | `source`              | New thread created by forking an existing thread.                                |
+| `thread.rename`                   | counter   |                       | Thread renamed.                                                                  |
+| `thread.side`                     | counter   | `source`              | Side conversation created.                                                       |
+| `thread.skills.enabled_total`     | histogram |                       | Number of skills enabled for a new thread.                                       |
+| `thread.skills.kept_total`        | histogram |                       | Number of enabled skills kept after prompt rendering.                            |
+| `thread.skills.truncated`         | histogram |                       | Whether skill rendering truncated the enabled skills list (`1` or `0`).          |
+| `task.compact`                    | counter   | `type`                | Number of compactions per type (`remote` or `local`), including manual and auto. |
+| `task.review`                     | counter   |                       | Number of reviews triggered.                                                     |
+| `task.undo`                       | counter   |                       | Number of undo actions triggered.                                                |
+| `task.user_shell`                 | counter   |                       | Number of user shell actions (`!` in the TUI for example).                       |
+| `shell_snapshot`                  | counter   | See note              | Whether taking a shell snapshot succeeded.                                       |
+| `shell_snapshot.duration_ms`      | histogram | `success`             | Time to take a shell snapshot.                                                   |
+| `skill.injected`                  | counter   | `status`, `skill`     | Skill injection outcomes by skill.                                               |
+| `plugins.startup_sync`            | counter   | `transport`, `status` | Curated plugin startup sync attempts.                                            |
+| `plugins.startup_sync.final`      | counter   | `transport`, `status` | Final curated plugin startup sync outcome.                                       |
+| `multi_agent.spawn`               | counter   | `role`                | Agent spawns by role.                                                            |
+| `multi_agent.resume`              | counter   |                       | Agent resumes.                                                                   |
+| `multi_agent.nickname_pool_reset` | counter   |                       | Agent nickname pool resets.                                                      |
+
+The `shell_snapshot` metric includes `success` and, on failures, `failure_reason`.
+
+#### Memory and local state
+
+| Metric                         | Type      | Fields                    | Description                                               |
+| ------------------------------ | --------- | ------------------------- | --------------------------------------------------------- |
+| `memory.phase1`                | counter   | `status`                  | Memory phase 1 job counts by status.                      |
+| `memory.phase1.e2e_ms`         | histogram |                           | End-to-end duration for memory phase 1.                   |
+| `memory.phase1.output`         | counter   |                           | Memory phase 1 outputs written.                           |
+| `memory.phase1.token_usage`    | histogram | `token_type`              | Memory phase 1 token usage by token type.                 |
+| `memory.phase2`                | counter   | `status`                  | Memory phase 2 job counts by status.                      |
+| `memory.phase2.e2e_ms`         | histogram |                           | End-to-end duration for memory phase 2.                   |
+| `memory.phase2.input`          | counter   |                           | Memory phase 2 input count.                               |
+| `memory.phase2.token_usage`    | histogram | `token_type`              | Memory phase 2 token usage by token type.                 |
+| `memories.usage`               | counter   | `kind`, `tool`, `success` | Memory usage by kind, tool, and success/failure.          |
+| `external_agent_config.detect` | counter   | See note                  | External agent config detections by migration item type.  |
+| `external_agent_config.import` | counter   | See note                  | External agent config imports by migration item type.     |
+| `db.backfill`                  | counter   | `status`                  | Initial state DB backfill results (`upserted`, `failed`). |
+| `db.backfill.duration_ms`      | histogram | `status`                  | Duration of the initial state DB backfill.                |
+| `db.error`                     | counter   | `stage`                   | Errors during state DB operations.                        |
+
+The `external_agent_config.detect` and `external_agent_config.import` metrics include `migration_type`; skills migrations also include `skills_count`.
+
+#### Windows sandbox
+
+| Metric                                           | Type      | Fields                                    | Description                                           |
+| ------------------------------------------------ | --------- | ----------------------------------------- | ----------------------------------------------------- |
+| `windows_sandbox.setup_success`                  | counter   | `originator`, `mode`                      | Windows sandbox setup successes.                      |
+| `windows_sandbox.setup_failure`                  | counter   | `originator`, `mode`                      | Windows sandbox setup failures.                       |
+| `windows_sandbox.setup_duration_ms`              | histogram | `result`, `originator`, `mode`            | Windows sandbox setup duration.                       |
+| `windows_sandbox.elevated_setup_success`         | counter   |                                           | Elevated Windows sandbox setup successes.             |
+| `windows_sandbox.elevated_setup_failure`         | counter   | See note                                  | Elevated Windows sandbox setup failures.              |
+| `windows_sandbox.elevated_setup_canceled`        | counter   | See note                                  | Canceled elevated Windows sandbox setup attempts.     |
+| `windows_sandbox.elevated_setup_duration_ms`     | histogram | `result`                                  | Elevated Windows sandbox setup duration.              |
+| `windows_sandbox.elevated_prompt_shown`          | counter   |                                           | Elevated sandbox setup prompt shown.                  |
+| `windows_sandbox.elevated_prompt_accept`         | counter   |                                           | Elevated sandbox setup prompt accepted.               |
+| `windows_sandbox.elevated_prompt_use_legacy`     | counter   |                                           | User chose legacy sandbox from the elevated prompt.   |
+| `windows_sandbox.elevated_prompt_quit`           | counter   |                                           | User quit from the elevated prompt.                   |
+| `windows_sandbox.fallback_prompt_shown`          | counter   |                                           | Fallback sandbox prompt shown.                        |
+| `windows_sandbox.fallback_retry_elevated`        | counter   |                                           | User retried elevated setup from the fallback prompt. |
+| `windows_sandbox.fallback_use_legacy`            | counter   |                                           | User chose legacy sandbox from the fallback prompt.   |
+| `windows_sandbox.fallback_prompt_quit`           | counter   |                                           | User quit from the fallback prompt.                   |
+| `windows_sandbox.legacy_setup_preflight_failed`  | counter   | See note                                  | Legacy Windows sandbox setup preflight failure.       |
+| `windows_sandbox.setup_elevated_sandbox_command` | counter   |                                           | Elevated sandbox setup command invoked.               |
+| `windows_sandbox.createprocessasuserw_failed`    | counter   | `error_code`, `path_kind`, `exe`, `level` | Windows `CreateProcessAsUserW` failures.              |
+
+The elevated setup failure metrics include `code` and `message` when Windows setup failure details are available, and may include `originator` when emitted from the shared setup path. The `windows_sandbox.legacy_setup_preflight_failed` metric includes `originator` when emitted from the shared setup path, but fallback-prompt preflight failures may not include any fields.
 
 ### Feedback controls
 
@@ -5736,6 +7591,8 @@
 - `notify` runs an external program (good for webhooks, desktop notifiers, CI hooks).
 - `tui.notifications` is built in to the TUI and can optionally filter by event type (for example, `agent-turn-complete` and `approval-requested`).
 - `tui.notification_method` controls how the TUI emits terminal notifications (`auto`, `osc9`, or `bel`).
+- `tui.notification_condition` controls whether TUI notifications fire only when
+  the terminal is `unfocused` or `always`.
 
 In `auto` mode, Codex prefers OSC 9 notifications (a terminal escape sequence some terminals interpret as a desktop notification) and falls back to BEL (`\x07`) otherwise.
 
@@ -5782,6 +7639,8 @@
 
 - `tui.notifications`: enable/disable notifications (or restrict to specific types)
 - `tui.notification_method`: choose `auto`, `osc9`, or `bel` for terminal notifications
+- `tui.notification_condition`: choose `unfocused` or `always` for when
+  notifications fire
 - `tui.animations`: enable/disable ASCII animations and shimmer effects
 - `tui.alternate_screen`: control alternate screen usage (set to `never` to keep terminal scrollback)
 - `tui.show_tooltips`: show or hide onboarding tooltips on the welcome screen
@@ -5794,7 +7653,7 @@
 
 # Config basics
 
-Codex reads configuration details from more than one location. Your personal defaults live in `~/.codex/config.toml`, and you can add project overrides with `.codex/config.toml` files. For security, Codex loads project config files only when you trust the project.
+Codex reads configuration details from more than one location. Your personal defaults live in `~/.codex/config.toml`, and you can add project overrides with `.codex/config.toml` files. For security, Codex loads project `.codex/` layers only when you trust the project.
 
 ## Codex configuration file
 
@@ -5821,7 +7680,7 @@
 
 Use that precedence to set shared defaults at the top level and keep profiles focused on the values that differ.
 
-If you mark a project as untrusted, Codex skips project-scoped `.codex/` layers (including `.codex/config.toml`) and falls back to user, system, and built-in defaults.
+If you mark a project as untrusted, Codex skips project-scoped `.codex/` layers, including project-local config, hooks, and rules. User and system config still load, including user/global hooks and rules.
 
 For one-off overrides via `-c`/`--config` (including TOML quoting rules), see [Advanced Config](https://developers.openai.com/codex/config-advanced#one-off-overrides-from-the-cli).
 
@@ -5840,7 +7699,7 @@
 Choose the model Codex uses by default in the CLI and IDE.
 
 ```toml
-model = "gpt-5.4"
+model = "gpt-5.5"
 ```
 
 #### Approval prompts
@@ -5862,6 +7721,16 @@
 ```
 
 For mode-by-mode behavior (including protected `.git`/`.codex` paths and network defaults), see [Sandbox and approvals](https://developers.openai.com/codex/agent-approvals-security#sandbox-and-approvals), [Protected paths in writable roots](https://developers.openai.com/codex/agent-approvals-security#protected-paths-in-writable-roots), and [Network access](https://developers.openai.com/codex/agent-approvals-security#network-access).
+
+#### Permission profiles
+
+Use a named permission profile when you want one reusable filesystem or network policy across sessions:
+
+```toml
+default_permissions = ":workspace"
+```
+
+Built-in profiles include `:read-only`, `:workspace`, and `:danger-no-sandbox`. For custom filesystem or network rules, define `[permissions.<name>]` tables and set `default_permissions` to that name.
 
 #### Windows sandbox mode
 
@@ -5905,6 +7774,18 @@
 
 You can override this later in an active session with `/personality` or per thread/turn when using the app-server APIs.
 
+#### TUI keymap
+
+Customize terminal shortcuts under `tui.keymap`. Context-specific bindings override `tui.keymap.global`, and an empty list unbinds the action.
+
+```toml
+[tui.keymap.global]
+open_transcript = "ctrl-t"
+
+[tui.keymap.composer]
+submit = ["enter", "ctrl-m"]
+```
+
 #### Command environment
 
 Control which environment variables Codex forwards to spawned commands.
@@ -5939,32 +7820,29 @@
 
 ### Supported features
 
-| Key                       | Default | Maturity     | Description                                                                                        |
-| ------------------------- | :-----: | ------------ | -------------------------------------------------------------------------------------------------- |
-| `apply_patch_freeform`    |  false  | Experimental | Include the freeform `apply_patch` tool                                                            |
-| `apps`                    |  false  | Experimental | Enable ChatGPT Apps/connectors support                                                             |
-| `apps_mcp_gateway`        |  false  | Experimental | Route Apps MCP calls through `https://api.openai.com/v1/connectors/mcp/` instead of legacy routing |
-| `collaboration_modes`     |  true   | Stable       | Enable collaboration modes such as plan mode                                                       |
-| `multi_agent`             |  false  | Experimental | Enable multi-agent collaboration tools                                                             |
-| `personality`             |  true   | Stable       | Enable personality selection controls                                                              |
-| `remote_models`           |  false  | Experimental | Refresh remote model list before showing readiness                                                 |
-| `runtime_metrics`         |  false  | Experimental | Show runtime metrics summaries in TUI turn separators                                              |
-| `request_rule`            |  true   | Stable       | Enable Smart approvals (`prefix_rule` suggestions)                                                 |
-| `search_tool`             |  false  | Experimental | Enable `search_tool_bm25` so Codex discovers Apps MCP tools via search before tool calls           |
-| `shell_snapshot`          |  false  | Beta         | Snapshot your shell environment to speed up repeated commands                                      |
-| `shell_tool`              |  true   | Stable       | Enable the default `shell` tool                                                                    |
-| `use_linux_sandbox_bwrap` |  false  | Experimental | Use the bubblewrap-based Linux sandbox pipeline                                                    |
-| `unified_exec`            |  false  | Beta         | Use the unified PTY-backed exec tool                                                               |
-| `undo`                    |  true   | Stable       | Enable undo via per-turn git ghost snapshots                                                       |
-| `web_search`              |  true   | Deprecated   | Legacy toggle; prefer the top-level `web_search` setting                                           |
-| `web_search_cached`       |  true   | Deprecated   | Legacy toggle that maps to `web_search = "cached"` when unset                                      |
-| `web_search_request`      |  true   | Deprecated   | Legacy toggle that maps to `web_search = "live"` when unset                                        |
+| Key                  |        Default        | Maturity     | Description                                                                              |
+| -------------------- | :-------------------: | ------------ | ---------------------------------------------------------------------------------------- |
+| `apps`               |         false         | Experimental | Enable ChatGPT Apps/connectors support                                                   |
+| `codex_hooks`        |         true          | Stable       | Enable lifecycle hooks from `hooks.json` or inline `[hooks]`. See [Hooks](https://developers.openai.com/codex/hooks). |
+| `fast_mode`          |         true          | Stable       | Enable Fast mode selection and the `service_tier = "fast"` path                          |
+| `memories`           |         false         | Stable       | Enable [Memories](https://developers.openai.com/codex/memories)                                                       |
+| `multi_agent`        |         true          | Stable       | Enable subagent collaboration tools                                                      |
+| `personality`        |         true          | Stable       | Enable personality selection controls                                                    |
+| `shell_snapshot`     |         true          | Stable       | Snapshot your shell environment to speed up repeated commands                            |
+| `shell_tool`         |         true          | Stable       | Enable the default `shell` tool                                                          |
+| `unified_exec`       | `true` except Windows | Stable       | Use the unified PTY-backed exec tool                                                     |
+| `undo`               |         false         | Stable       | Enable undo via per-turn git ghost snapshots                                             |
+| `web_search`         |         true          | Deprecated   | Legacy toggle; prefer the top-level `web_search` setting                                 |
+| `web_search_cached`  |         false         | Deprecated   | Legacy toggle that maps to `web_search = "cached"` when unset                            |
+| `web_search_request` |         false         | Deprecated   | Legacy toggle that maps to `web_search = "live"` when unset                              |
 
 The Maturity column uses feature maturity labels such as Experimental, Beta,
   and Stable. See [Feature Maturity](https://developers.openai.com/codex/feature-maturity) for how to
   interpret these labels.
 
 Omit feature keys to keep their defaults.
+
+For the current lifecycle hooks MVP, see [Hooks](https://developers.openai.com/codex/hooks).
 
 ### Enabling features
 
@@ -5990,7 +7868,7 @@
     {
       key: "model",
       type: "string",
-      description: "Model to use (e.g., `gpt-5-codex`).",
+      description: "Model to use (e.g., `gpt-5.5`).",
     },
     {
       key: "review_model",
@@ -6004,6 +7882,12 @@
       description: "Provider id from `model_providers` (default: `openai`).",
     },
     {
+      key: "openai_base_url",
+      type: "string",
+      description:
+        "Base URL override for the built-in `openai` model provider.",
+    },
+    {
       key: "model_context_window",
       type: "number",
       description: "Context window tokens available to the active model.",
@@ -6028,27 +7912,51 @@
     },
     {
       key: "approval_policy",
-      type: "untrusted | on-request | never | { reject = { sandbox_approval = bool, rules = bool, mcp_elicitations = bool } }",
-      description:
-        "Controls when Codex pauses for approval before executing commands. You can also use `approval_policy = { reject = { ... } }` to auto-reject specific prompt categories while keeping other prompts interactive. `on-failure` is deprecated; use `on-request` for interactive runs or `never` for non-interactive runs.",
-    },
-    {
-      key: "approval_policy.reject.sandbox_approval",
+      type: "untrusted | on-request | never | { granular = { sandbox_approval = bool, rules = bool, mcp_elicitations = bool, request_permissions = bool, skill_approval = bool } }",
+      description:
+        "Controls when Codex pauses for approval before executing commands. You can also use `approval_policy = { granular = { ... } }` to allow or auto-reject specific prompt categories while keeping other prompts interactive. `on-failure` is deprecated; use `on-request` for interactive runs or `never` for non-interactive runs.",
+    },
+    {
+      key: "approval_policy.granular.sandbox_approval",
       type: "boolean",
       description:
-        "When `true`, sandbox escalation approval prompts are auto-rejected.",
-    },
-    {
-      key: "approval_policy.reject.rules",
+        "When `true`, sandbox escalation approval prompts are allowed to surface.",
+    },
+    {
+      key: "approval_policy.granular.rules",
       type: "boolean",
       description:
-        "When `true`, approvals triggered by execpolicy `prompt` rules are auto-rejected.",
-    },
-    {
-      key: "approval_policy.reject.mcp_elicitations",
+        "When `true`, approvals triggered by execpolicy `prompt` rules are allowed to surface.",
+    },
+    {
+      key: "approval_policy.granular.mcp_elicitations",
       type: "boolean",
       description:
-        "When `true`, MCP elicitation prompts are auto-rejected instead of shown to the user.",
+        "When `true`, MCP elicitation prompts are allowed to surface instead of being auto-rejected.",
+    },
+    {
+      key: "approval_policy.granular.request_permissions",
+      type: "boolean",
+      description:
+        "When `true`, prompts from the `request_permissions` tool are allowed to surface.",
+    },
+    {
+      key: "approval_policy.granular.skill_approval",
+      type: "boolean",
+      description:
+        "When `true`, skill-script approval prompts are allowed to surface.",
+    },
+    {
+      key: "approvals_reviewer",
+      type: "user | auto_review",
+      description:
+        "Who reviews eligible approval prompts under `on-request` or granular approval policies. Defaults to `user`; `auto_review` uses the reviewer subagent. This setting doesn't change sandboxing or review actions already allowed inside the sandbox.",
+    },
+    {
+      key: "auto_review.policy",
+      type: "string",
+      description:
+        "Local Markdown policy instructions for automatic review. Managed `guardian_policy_config` takes precedence. Blank values are ignored.",
     },
     {
       key: "allow_login_shell",
@@ -6093,6 +8001,12 @@
         "Windows-only native sandbox mode when running Codex natively on Windows.",
     },
     {
+      key: "windows.sandbox_private_desktop",
+      type: "boolean",
+      description:
+        "Run the final sandboxed child process on a private desktop by default on native Windows. Set `false` only for compatibility with the older `Winsta0\\\\Default` behavior.",
+    },
+    {
       key: "notify",
       type: "array<string>",
       description:
@@ -6109,6 +8023,12 @@
       type: "boolean",
       description:
         "Enable feedback submission via `/feedback` across Codex surfaces (default: true).",
+    },
+    {
+      key: "analytics.enabled",
+      type: "boolean",
+      description:
+        "Enable or disable analytics for this machine/profile. When unset, the client default applies.",
     },
     {
       key: "instructions",
@@ -6140,6 +8060,12 @@
       description: "Inline override for the history compaction prompt.",
     },
     {
+      key: "commit_attribution",
+      type: "string",
+      description:
+        "Override the commit co-author trailer text. Set an empty string to disable automatic attribution.",
+    },
+    {
       key: "model_instructions_file",
       type: "string (path)",
       description:
@@ -6150,6 +8076,11 @@
       type: "none | friendly | pragmatic",
       description:
         "Default communication style for models that advertise `supportsPersonality`; can be overridden per thread/turn or via `/personality`.",
+    },
+    {
+      key: "service_tier",
+      type: "flex | fast",
+      description: "Preferred service tier for new turns.",
     },
     {
       key: "experimental_compact_prompt_file",
@@ -6232,15 +8163,38 @@
       description: "Per-tool approval behavior override for a single app tool.",
     },
     {
+      key: "tool_suggest.discoverables",
+      type: "array<table>",
+      description:
+        'Allow tool suggestions for additional discoverable connectors or plugins. Each entry uses `type = "connector"` or `"plugin"` and an `id`.',
+    },
+    {
+      key: "tool_suggest.disabled_tools",
+      type: "array<table>",
+      description:
+        'Disable suggestions for specific discoverable connectors or plugins. Each entry uses `type = "connector"` or `"plugin"` and an `id`.',
+    },
+    {
       key: "features.apps",
       type: "boolean",
       description: "Enable ChatGPT Apps/connectors support (experimental).",
     },
     {
-      key: "features.apps_mcp_gateway",
+      key: "features.codex_hooks",
       type: "boolean",
       description:
-        "Route Apps MCP calls through the OpenAI connectors MCP gateway (`https://api.openai.com/v1/connectors/mcp/`) instead of legacy routing (experimental).",
+        "Enable lifecycle hooks loaded from `hooks.json` or inline `[hooks]` config.",
+    },
+    {
+      key: "hooks",
+      type: "table",
+      description:
+        "Lifecycle hooks configured inline in `config.toml`. Uses the same event schema as `hooks.json`; see the Hooks guide for examples and supported events.",
+    },
+    {
+      key: "features.memories",
+      type: "boolean",
+      description: "Enable [Memories](https://developers.openai.com/codex/memories) (off by default).",
     },
     {
       key: "mcp_servers.<id>.command",
@@ -6259,9 +8213,9 @@
     },
     {
       key: "mcp_servers.<id>.env_vars",
-      type: "array<string>",
-      description:
-        "Additional environment variables to whitelist for an MCP stdio server.",
+      type: 'array<string | { name = string, source = "local" | "remote" }>',
+      description:
+        'Additional environment variables to whitelist for an MCP stdio server. String entries default to `source = "local"`; use `source = "remote"` only with executor-backed remote stdio.',
     },
     {
       key: "mcp_servers.<id>.cwd",
@@ -6330,10 +8284,28 @@
         "Deny list applied after `enabled_tools` for the MCP server.",
     },
     {
+      key: "mcp_servers.<id>.scopes",
+      type: "array<string>",
+      description:
+        "OAuth scopes to request when authenticating to that MCP server.",
+    },
+    {
+      key: "mcp_servers.<id>.oauth_resource",
+      type: "string",
+      description:
+        "Optional RFC 8707 OAuth resource parameter to include during MCP login.",
+    },
+    {
+      key: "mcp_servers.<id>.experimental_environment",
+      type: "local | remote",
+      description:
+        "Experimental placement for an MCP server. `remote` starts stdio servers through a remote executor environment; streamable HTTP remote placement is not implemented.",
+    },
+    {
       key: "agents.max_threads",
       type: "number",
       description:
-        "Maximum number of agent threads that can be open concurrently.",
+        "Maximum number of agent threads that can be open concurrently. Defaults to `6` when unset.",
     },
     {
       key: "agents.max_depth",
@@ -6360,26 +8332,97 @@
         "Path to a TOML config layer for that role; relative paths resolve from the config file that declares the role.",
     },
     {
+      key: "agents.<name>.nickname_candidates",
+      type: "array<string>",
+      description:
+        "Optional pool of display nicknames for spawned agents in that role.",
+    },
+    {
+      key: "memories.generate_memories",
+      type: "boolean",
+      description:
+        "When `false`, newly created threads are not stored as memory-generation inputs. Defaults to `true`.",
+    },
+    {
+      key: "memories.use_memories",
+      type: "boolean",
+      description:
+        "When `false`, Codex skips injecting existing memories into future sessions. Defaults to `true`.",
+    },
+    {
+      key: "memories.disable_on_external_context",
+      type: "boolean",
+      description:
+        "When `true`, threads that use external context such as MCP tool calls, web search, or tool search are kept out of memory generation. Defaults to `false`. Legacy alias: `memories.no_memories_if_mcp_or_web_search`.",
+    },
+    {
+      key: "memories.max_raw_memories_for_consolidation",
+      type: "number",
+      description:
+        "Maximum recent raw memories retained for global consolidation. Defaults to `256` and is capped at `4096`.",
+    },
+    {
+      key: "memories.max_unused_days",
+      type: "number",
+      description:
+        "Maximum days since a memory was last used before it becomes ineligible for consolidation. Defaults to `30` and is clamped to `0`-`365`.",
+    },
+    {
+      key: "memories.max_rollout_age_days",
+      type: "number",
+      description:
+        "Maximum age of threads considered for memory generation. Defaults to `30` and is clamped to `0`-`90`.",
+    },
+    {
+      key: "memories.max_rollouts_per_startup",
+      type: "number",
+      description:
+        "Maximum rollout candidates processed per startup pass. Defaults to `16` and is capped at `128`.",
+    },
+    {
+      key: "memories.min_rollout_idle_hours",
+      type: "number",
+      description:
+        "Minimum idle time before a thread is considered for memory generation. Defaults to `6` and is clamped to `1`-`48`.",
+    },
+    {
+      key: "memories.min_rate_limit_remaining_percent",
+      type: "number",
+      description:
+        "Minimum remaining percentage required in Codex rate-limit windows before memory generation starts. Defaults to `25` and is clamped to `0`-`100`.",
+    },
+    {
+      key: "memories.extract_model",
+      type: "string",
+      description: "Optional model override for per-thread memory extraction.",
+    },
+    {
+      key: "memories.consolidation_model",
+      type: "string",
+      description: "Optional model override for global memory consolidation.",
+    },
+    {
       key: "features.unified_exec",
       type: "boolean",
-      description: "Use the unified PTY-backed exec tool (beta).",
+      description:
+        "Use the unified PTY-backed exec tool (stable; enabled by default except on Windows).",
     },
     {
       key: "features.shell_snapshot",
       type: "boolean",
       description:
-        "Snapshot shell environment to speed up repeated commands (beta).",
-    },
-    {
-      key: "features.apply_patch_freeform",
+        "Snapshot shell environment to speed up repeated commands (stable; on by default).",
+    },
+    {
+      key: "features.undo",
       type: "boolean",
-      description: "Expose the freeform `apply_patch` tool (experimental).",
+      description: "Enable undo support (stable; off by default).",
     },
     {
       key: "features.multi_agent",
       type: "boolean",
       description:
-        "Enable multi-agent collaboration tools (`spawn_agent`, `send_input`, `resume_agent`, `wait`, `close_agent`, and `spawn_agents_on_csv`) (experimental; off by default).",
+        "Enable multi-agent collaboration tools (`spawn_agent`, `send_input`, `resume_agent`, `wait_agent`, and `close_agent`) (stable; on by default).",
     },
     {
       key: "features.personality",
@@ -6412,57 +8455,40 @@
         "Enable the default `shell` tool for running commands (stable; on by default).",
     },
     {
-      key: "features.request_rule",
+      key: "features.enable_request_compression",
       type: "boolean",
       description:
-        "Enable Smart approvals (`prefix_rule` suggestions on escalation requests; stable; on by default).",
-    },
-    {
-      key: "features.search_tool",
+        "Compress streaming request bodies with zstd when supported (stable; on by default).",
+    },
+    {
+      key: "features.skill_mcp_dependency_install",
       type: "boolean",
       description:
-        "Enable `search_tool_bm25` for Apps tool discovery before invoking app MCP tools (experimental).",
-    },
-    {
-      key: "features.collaboration_modes",
+        "Allow prompting and installing missing MCP dependencies for skills (stable; on by default).",
+    },
+    {
+      key: "features.fast_mode",
       type: "boolean",
       description:
-        "Enable collaboration modes such as plan mode (stable; on by default).",
-    },
-    {
-      key: "features.use_linux_sandbox_bwrap",
+        'Enable Fast mode selection and the `service_tier = "fast"` path (stable; on by default).',
+    },
+    {
+      key: "features.prevent_idle_sleep",
       type: "boolean",
       description:
-        "Use the bubblewrap-based Linux sandbox pipeline (experimental; off by default).",
-    },
-    {
-      key: "features.remote_models",
-      type: "boolean",
-      description:
-        "Refresh remote model list before showing readiness (experimental).",
-    },
-    {
-      key: "features.runtime_metrics",
-      type: "boolean",
-      description:
-        "Show runtime metrics summary in TUI turn separators (experimental).",
-    },
-    {
-      key: "features.powershell_utf8",
-      type: "boolean",
-      description: "Force PowerShell UTF-8 output (defaults to true).",
-    },
-    {
-      key: "features.child_agents_md",
-      type: "boolean",
-      description:
-        "Append AGENTS.md scope/precedence guidance even when no AGENTS.md is present (experimental).",
+        "Prevent the machine from sleeping while a turn is actively running (experimental; off by default).",
     },
     {
       key: "suppress_unstable_features_warning",
       type: "boolean",
       description:
         "Suppress the warning that appears when under-development feature flags are enabled.",
+    },
+    {
+      key: "model_providers.<id>",
+      type: "table",
+      description:
+        "Custom provider definition. Built-in provider IDs (`openai`, `ollama`, and `lmstudio`) are reserved and cannot be overridden.",
     },
     {
       key: "model_providers.<id>.name",
@@ -6498,9 +8524,9 @@
     },
     {
       key: "model_providers.<id>.wire_api",
-      type: "chat | responses",
-      description:
-        "Protocol used by the provider (defaults to `chat` if omitted).",
+      type: "responses",
+      description:
+        "Protocol used by the provider. `responses` is the only supported value, and it is the default when omitted.",
     },
     {
       key: "model_providers.<id>.query_params",
@@ -6536,12 +8562,69 @@
         "Idle timeout for SSE streams in milliseconds (default: 300000).",
     },
     {
+      key: "model_providers.<id>.supports_websockets",
+      type: "boolean",
+      description:
+        "Whether that provider supports the Responses API WebSocket transport.",
+    },
+    {
+      key: "model_providers.<id>.auth",
+      type: "table",
+      description:
+        "Command-backed bearer token configuration for a custom provider. Do not combine with `env_key`, `experimental_bearer_token`, or `requires_openai_auth`.",
+    },
+    {
+      key: "model_providers.<id>.auth.command",
+      type: "string",
+      description:
+        "Command to run when Codex needs a bearer token. The command must print the token to stdout.",
+    },
+    {
+      key: "model_providers.<id>.auth.args",
+      type: "array<string>",
+      description: "Arguments passed to the token command.",
+    },
+    {
+      key: "model_providers.<id>.auth.timeout_ms",
+      type: "number",
+      description:
+        "Maximum token command runtime in milliseconds (default: 5000).",
+    },
+    {
+      key: "model_providers.<id>.auth.refresh_interval_ms",
+      type: "number",
+      description:
+        "How often Codex proactively refreshes the token in milliseconds (default: 300000). Set to `0` to refresh only after an authentication retry.",
+    },
+    {
+      key: "model_providers.<id>.auth.cwd",
+      type: "string (path)",
+      description: "Working directory for the token command.",
+    },
+    {
+      key: "model_providers.amazon-bedrock.aws.profile",
+      type: "string",
+      description:
+        "AWS profile name used by the built-in `amazon-bedrock` provider.",
+    },
+    {
+      key: "model_providers.amazon-bedrock.aws.region",
+      type: "string",
+      description: "AWS region used by the built-in `amazon-bedrock` provider.",
+    },
+    {
       key: "model_reasoning_effort",
       type: "minimal | low | medium | high | xhigh",
       description:
         "Adjust reasoning effort for supported models (Responses API only; `xhigh` is model-dependent).",
     },
     {
+      key: "plan_mode_reasoning_effort",
+      type: "none | minimal | low | medium | high | xhigh",
+      description:
+        "Plan-mode-specific reasoning override. When unset, Plan mode uses its built-in preset default.",
+    },
+    {
       key: "model_reasoning_summary",
       type: "auto | concise | detailed | none",
       description:
@@ -6551,7 +8634,7 @@
       key: "model_verbosity",
       type: "low | medium | high",
       description:
-        "Control GPT-5 Responses API verbosity (defaults to `medium`).",
+        "Optional GPT-5 Responses API verbosity override; when unset, the selected model/preset default is used.",
     },
     {
       key: "model_supports_reasoning_summaries",
@@ -6623,10 +8706,14 @@
         "Profile-scoped overrides for any of the supported configuration keys.",
     },
     {
-      key: "profiles.<name>.include_apply_patch_tool",
-      type: "boolean",
-      description:
-        "Legacy name for enabling freeform apply_patch; prefer `[features].apply_patch_freeform`.",
+      key: "profiles.<name>.service_tier",
+      type: "flex | fast",
+      description: "Profile-scoped service tier preference for new turns.",
+    },
+    {
+      key: "profiles.<name>.plan_mode_reasoning_effort",
+      type: "none | minimal | low | medium | high | xhigh",
+      description: "Profile-scoped Plan-mode reasoning override.",
     },
     {
       key: "profiles.<name>.web_search",
@@ -6647,16 +8734,16 @@
         "Profile-scoped model catalog JSON path override (applied on startup only; overrides the top-level `model_catalog_json` for that profile).",
     },
     {
+      key: "profiles.<name>.model_instructions_file",
+      type: "string (path)",
+      description:
+        "Profile-scoped replacement for the built-in instruction file.",
+    },
+    {
       key: "profiles.<name>.experimental_use_unified_exec_tool",
       type: "boolean",
       description:
         "Legacy name for enabling unified exec; prefer `[features].unified_exec`.",
-    },
-    {
-      key: "profiles.<name>.experimental_use_freeform_apply_patch",
-      type: "boolean",
-      description:
-        "Legacy name for enabling freeform apply_patch; prefer `[features].apply_patch_freeform`.",
     },
     {
       key: "profiles.<name>.oss_provider",
@@ -6664,6 +8751,21 @@
       description: "Profile-scoped OSS provider for `--oss` sessions.",
     },
     {
+      key: "profiles.<name>.tools_view_image",
+      type: "boolean",
+      description: "Enable or disable the `view_image` tool in that profile.",
+    },
+    {
+      key: "profiles.<name>.analytics.enabled",
+      type: "boolean",
+      description: "Profile-scoped analytics enablement override.",
+    },
+    {
+      key: "profiles.<name>.windows.sandbox",
+      type: "unelevated | elevated",
+      description: "Profile-scoped Windows sandbox mode override.",
+    },
+    {
       key: "history.persistence",
       type: "save-all | none",
       description:
@@ -6710,6 +8812,12 @@
       type: "none | otlp-http | otlp-grpc",
       description:
         "Select the OpenTelemetry trace exporter and provide any endpoint metadata.",
+    },
+    {
+      key: "otel.metrics_exporter",
+      type: "none | statsig | otlp-http | otlp-grpc",
+      description:
+        "Select the OpenTelemetry metrics exporter (defaults to `statsig`).",
     },
     {
       key: "otel.log_user_prompt",
@@ -6793,7 +8901,13 @@
       key: "tui.notification_method",
       type: "auto | osc9 | bel",
       description:
-        "Notification method for unfocused terminal notifications (default: auto).",
+        "Notification method for terminal notifications (default: auto).",
+    },
+    {
+      key: "tui.notification_condition",
+      type: "unfocused | always",
+      description:
+        "Control whether TUI notifications fire only when the terminal is unfocused or regardless of focus. Defaults to `unfocused`.",
     },
     {
       key: "tui.animations",
@@ -6818,6 +8932,35 @@
       type: "array<string> | null",
       description:
         "Ordered list of TUI footer status-line item identifiers. `null` disables the status line.",
+    },
+    {
+      key: "tui.terminal_title",
+      type: "array<string> | null",
+      description:
+        'Ordered list of terminal window/tab title item identifiers. Defaults to `["spinner", "project"]`; `null` disables title updates.',
+    },
+    {
+      key: "tui.theme",
+      type: "string",
+      description:
+        "Syntax-highlighting theme override (kebab-case theme name).",
+    },
+    {
+      key: "tui.keymap.<context>.<action>",
+      type: "string | array<string>",
+      description:
+        "Keyboard shortcut binding for a TUI action. Supported contexts include `global`, `chat`, `composer`, `editor`, `pager`, `list`, and `approval`; context-specific bindings override `tui.keymap.global`.",
+    },
+    {
+      key: "tui.keymap.<context>.<action> = []",
+      type: "empty array",
+      description:
+        "Unbind the action in that keymap context. Key names use normalized strings such as `ctrl-a`, `shift-enter`, or `page-down`.",
+    },
+    {
+      key: "tui.model_availability_nux.<model>",
+      type: "integer",
+      description: "Internal startup-tooltip state keyed by model slug.",
     },
     {
       key: "hide_agent_reasoning",
@@ -6876,22 +9019,15 @@
         "Legacy name for enabling unified exec; prefer `[features].unified_exec` or `codex --enable unified_exec`.",
     },
     {
-      key: "experimental_use_freeform_apply_patch",
+      key: "tools.web_search",
+      type: 'boolean | { context_size = "low|medium|high", allowed_domains = [string], location = { country, region, city, timezone } }',
+      description:
+        "Optional web search tool configuration. The legacy boolean form is still accepted, but the object form lets you set search context size, allowed domains, and approximate user location.",
+    },
+    {
+      key: "tools.view_image",
       type: "boolean",
-      description:
-        "Legacy name for enabling freeform apply_patch; prefer `[features].apply_patch_freeform` or `codex --enable apply_patch_freeform`.",
-    },
-    {
-      key: "include_apply_patch_tool",
-      type: "boolean",
-      description:
-        "Legacy name for enabling freeform apply_patch; prefer `[features].apply_patch_freeform`.",
-    },
-    {
-      key: "tools.web_search",
-      type: "boolean",
-      description:
-        "Deprecated legacy toggle for web search; prefer the top-level `web_search` setting.",
+      description: "Enable the local-image attachment tool `view_image`.",
     },
     {
       key: "web_search",
@@ -6900,10 +9036,108 @@
         'Web search mode (default: `"cached"`; cached uses an OpenAI-maintained index and does not fetch live pages; if you use `--yolo` or another full access sandbox setting, it defaults to `"live"`). Use `"live"` to fetch the most recent data from the web, or `"disabled"` to remove the tool.',
     },
     {
+      key: "default_permissions",
+      type: "string",
+      description:
+        "Name of the default permissions profile to apply to sandboxed tool calls. Built-ins are `:read-only`, `:workspace`, and `:danger-no-sandbox`; custom profile names require matching `[permissions.<name>]` tables.",
+    },
+    {
+      key: "permissions.<name>.filesystem",
+      type: "table",
+      description:
+        "Named filesystem permission profile. Each key is an absolute path or special token such as `:minimal` or `:project_roots`.",
+    },
+    {
+      key: "permissions.<name>.filesystem.glob_scan_max_depth",
+      type: "number",
+      description:
+        "Maximum depth for expanding deny-read glob patterns on platforms that snapshot matches before sandbox startup. Must be at least `1` when set.",
+    },
+    {
+      key: "permissions.<name>.filesystem.<path-or-glob>",
+      type: '"read" | "write" | "none" | table',
+      description:
+        'Grant direct access for a path, glob pattern, or special token, or scope nested entries under that root. Use `"none"` to deny reads for matching paths.',
+    },
+    {
+      key: 'permissions.<name>.filesystem.":project_roots".<subpath-or-glob>',
+      type: '"read" | "write" | "none"',
+      description:
+        'Scoped filesystem access relative to the detected project roots. Use `"."` for the root itself; glob subpaths such as `"**/*.env"` can deny reads with `"none"`.',
+    },
+    {
+      key: "permissions.<name>.network.enabled",
+      type: "boolean",
+      description: "Enable network access for this named permissions profile.",
+    },
+    {
+      key: "permissions.<name>.network.proxy_url",
+      type: "string",
+      description:
+        "HTTP proxy endpoint used when this permissions profile enables the managed network proxy.",
+    },
+    {
+      key: "permissions.<name>.network.enable_socks5",
+      type: "boolean",
+      description:
+        "Expose a SOCKS5 listener when this permissions profile enables the managed network proxy.",
+    },
+    {
+      key: "permissions.<name>.network.socks_url",
+      type: "string",
+      description: "SOCKS5 proxy endpoint used by this permissions profile.",
+    },
+    {
+      key: "permissions.<name>.network.enable_socks5_udp",
+      type: "boolean",
+      description: "Allow UDP over the SOCKS5 listener when enabled.",
+    },
+    {
+      key: "permissions.<name>.network.allow_upstream_proxy",
+      type: "boolean",
+      description:
+        "Allow the managed proxy to chain to another upstream proxy.",
+    },
+    {
+      key: "permissions.<name>.network.dangerously_allow_non_loopback_proxy",
+      type: "boolean",
+      description:
+        "Permit non-loopback bind addresses for the managed proxy listener.",
+    },
+    {
+      key: "permissions.<name>.network.dangerously_allow_all_unix_sockets",
+      type: "boolean",
+      description:
+        "Allow the proxy to use arbitrary Unix sockets instead of the default restricted set.",
+    },
+    {
+      key: "permissions.<name>.network.mode",
+      type: "limited | full",
+      description: "Network proxy mode used for subprocess traffic.",
+    },
+    {
+      key: "permissions.<name>.network.domains",
+      type: "map<string, allow | deny>",
+      description:
+        "Domain rules for the managed proxy. Use domain names or wildcard patterns as keys, with `allow` or `deny` values.",
+    },
+    {
+      key: "permissions.<name>.network.unix_sockets",
+      type: "map<string, allow | none>",
+      description:
+        "Unix socket rules for the managed proxy. Use socket paths as keys, with `allow` or `none` values.",
+    },
+    {
+      key: "permissions.<name>.network.allow_local_binding",
+      type: "boolean",
+      description:
+        "Permit local bind/listen operations through the managed proxy.",
+    },
+    {
       key: "projects.<path>.trust_level",
       type: "string",
       description:
-        'Mark a project or worktree as trusted or untrusted (`"trusted"` | `"untrusted"`). Untrusted projects skip project-scoped `.codex/` layers.',
+        'Mark a project or worktree as trusted or untrusted (`"trusted"` | `"untrusted"`). Untrusted projects skip project-scoped `.codex/` layers, including project-local config, hooks, and rules.',
     },
     {
       key: "notice.hide_full_access_warning",
@@ -6977,7 +9211,19 @@
       key: "allowed_approval_policies",
       type: "array<string>",
       description:
-        "Allowed values for `approval_policy` (for example `untrusted`, `on-request`, `never`, and `reject`).",
+        "Allowed values for `approval_policy` (for example `untrusted`, `on-request`, `never`, and `granular`).",
+    },
+    {
+      key: "allowed_approvals_reviewers",
+      type: "array<string>",
+      description:
+        "Allowed values for `approvals_reviewer`, such as `user` and `auto_review`.",
+    },
+    {
+      key: "guardian_policy_config",
+      type: "string",
+      description:
+        "Managed Markdown policy instructions for automatic review. This takes precedence over local `[auto_review].policy`. Blank values are ignored.",
     },
     {
       key: "allowed_sandbox_modes",
@@ -6985,6 +9231,24 @@
       description: "Allowed values for `sandbox_mode`.",
     },
     {
+      key: "remote_sandbox_config",
+      type: "array<table>",
+      description:
+        "Host-specific sandbox requirements. The first entry whose `hostname_patterns` match the resolved host name overrides top-level `allowed_sandbox_modes` for that requirements source. Host-specific entries currently override sandbox modes only.",
+    },
+    {
+      key: "remote_sandbox_config[].hostname_patterns",
+      type: "array<string>",
+      description:
+        "Case-insensitive host name patterns. Supports `*` for any sequence of characters and `?` for one character.",
+    },
+    {
+      key: "remote_sandbox_config[].allowed_sandbox_modes",
+      type: "array<string>",
+      description:
+        "Allowed sandbox modes to apply when this host-specific entry matches.",
+    },
+    {
       key: "allowed_web_search_modes",
       type: "array<string>",
       description:
@@ -7001,6 +9265,60 @@
       type: "boolean",
       description:
         "Require a specific canonical feature key to stay enabled or disabled.",
+    },
+    {
+      key: "features.in_app_browser",
+      type: "boolean",
+      description:
+        "Set to `false` in `requirements.toml` to disable the in-app browser pane.",
+    },
+    {
+      key: "features.browser_use",
+      type: "boolean",
+      description:
+        "Set to `false` in `requirements.toml` to disable Browser Use and Browser Agent availability.",
+    },
+    {
+      key: "features.computer_use",
+      type: "boolean",
+      description:
+        "Set to `false` in `requirements.toml` to disable Computer Use availability and related install or enablement flows.",
+    },
+    {
+      key: "hooks",
+      type: "table",
+      description:
+        "Admin-enforced managed lifecycle hooks. Requires a managed hook directory and uses the same event schema as inline `[hooks]` in `config.toml`.",
+    },
+    {
+      key: "hooks.managed_dir",
+      type: "string (absolute path)",
+      description:
+        "Directory containing managed hook scripts on macOS and Linux. Codex validates that it is absolute and exists before loading managed hooks.",
+    },
+    {
+      key: "hooks.windows_managed_dir",
+      type: "string (absolute path)",
+      description:
+        "Directory containing managed hook scripts on Windows. Codex validates that it is absolute and exists before loading managed hooks.",
+    },
+    {
+      key: "hooks.<Event>",
+      type: "array<table>",
+      description:
+        "Matcher groups for a hook event such as `PreToolUse`, `PostToolUse`, `PermissionRequest`, `SessionStart`, `UserPromptSubmit`, or `Stop`.",
+    },
+    {
+      key: "hooks.<Event>[].hooks",
+      type: "array<table>",
+      description:
+        "Hook handlers for a matcher group. Command hooks are currently supported; prompt and agent hook handlers are parsed but skipped.",
+    },
+    {
+      key: "permissions.filesystem.deny_read",
+      type: "array<string>",
+      description:
+        "Admin-enforced filesystem read denials. Entries can be paths or glob patterns, and users cannot weaken them with local config.",
     },
     {
       key: "mcp_servers",
@@ -7089,7 +9407,7 @@
 ```toml
 # Codex example configuration (config.toml)
 #
-# This file lists all keys Codex reads from config.toml, along with default
+# This file lists the main keys Codex reads from config.toml, along with default
 # behaviors, recommended examples, and concise explanations. Adjust as needed.
 #
 # Notes
@@ -7101,15 +9419,14 @@
 # Core Model Selection
 ################################################################################
 
-# Primary model used by Codex. Recommended example for most users: "gpt-5.4".
-model = "gpt-5.4"
-
-# Default communication style for supported models. Default: "friendly".
-# Allowed values: none | friendly | pragmatic
-# personality = "friendly"
+# Primary model used by Codex. Recommended example for most users: "gpt-5.5".
+model = "gpt-5.5"
+
+# Communication style for supported models. Allowed values: none | friendly | pragmatic
+# personality = "pragmatic"
 
 # Optional model override for /review. Default: unset (uses current session model).
-# review_model = "gpt-5.4"
+# review_model = "gpt-5.5"
 
 # Provider id selected from [model_providers]. Default: "openai".
 model_provider = "openai"
@@ -7117,11 +9434,13 @@
 # Default OSS provider for --oss sessions. When unset, Codex prompts. Default: unset.
 # oss_provider = "ollama"
 
-# Optional manual model metadata. When unset, Codex auto-detects from model.
-# Uncomment to force values.
+# Preferred service tier. `fast` is honored only when enabled in [features].
+# service_tier = "flex"  # fast | flex
+
+# Optional manual model metadata. When unset, Codex uses model or preset defaults.
 # model_context_window = 128000       # tokens; default: auto for model
-# model_auto_compact_token_limit = 0  # tokens; unset uses model defaults
-# tool_output_token_limit = 10000     # tokens stored per tool output
+# model_auto_compact_token_limit = 64000  # tokens; unset uses model defaults
+# tool_output_token_limit = 12000     # tokens stored per tool output
 # model_catalog_json = "/absolute/path/to/models.json" # optional startup-only model catalog override
 # background_terminal_max_timeout = 300000 # ms; max empty write_stdin poll window (default 5m)
 # log_dir = "/absolute/path/to/codex-logs" # directory for Codex logs; default: "$CODEX_HOME/log"
@@ -7131,16 +9450,19 @@
 # Reasoning & Verbosity (Responses API capable models)
 ################################################################################
 
-# Reasoning effort: minimal | low | medium | high | xhigh (default: medium; `xhigh` availability is model-dependent)
-model_reasoning_effort = "medium"
-
-# Reasoning summary: auto | concise | detailed | none (default: auto)
+# Reasoning effort: minimal | low | medium | high | xhigh
+# model_reasoning_effort = "medium"
+
+# Optional override used when Codex runs in plan mode: none | minimal | low | medium | high | xhigh
+# plan_mode_reasoning_effort = "high"
+
+# Reasoning summary: auto | concise | detailed | none
 # model_reasoning_summary = "auto"
 
-# Text verbosity for GPT-5 family (Responses API): low | medium | high (default: medium)
+# Text verbosity for GPT-5 family (Responses API): low | medium | high
 # model_verbosity = "medium"
 
-# Force enable or disable reasoning summaries for current model
+# Force enable or disable reasoning summaries for current model.
 # model_supports_reasoning_summaries = true
 
 ################################################################################
@@ -7150,32 +9472,24 @@
 # Additional user instructions are injected before AGENTS.md. Default: unset.
 # developer_instructions = ""
 
-# (Ignored) Optional legacy base instructions override (prefer AGENTS.md). Default: unset.
-# instructions = ""
-
 # Inline override for the history compaction prompt. Default: unset.
 # compact_prompt = ""
 
+# Override the default commit co-author trailer. Set to "" to disable it.
+# commit_attribution = "Jane Doe <jane@example.com>"
+
 # Override built-in base instructions with a file path. Default: unset.
 # model_instructions_file = "/absolute/or/relative/path/to/instructions.txt"
 
-# Migration note: experimental_instructions_file was renamed to model_instructions_file (deprecated).
-
 # Load the compact prompt override from a file. Default: unset.
 # experimental_compact_prompt_file = "/absolute/or/relative/path/to/compact_prompt.txt"
-
-# Legacy name for apply_patch_freeform. Default: false
-include_apply_patch_tool = false
-
 
 ################################################################################
 # Notifications
 ################################################################################
 
 # External notifier program (argv array). When unset: disabled.
-# Example: notify = ["notify-send", "Codex"]
-notify = [ ]
-
+# notify = ["notify-send", "Codex"]
 
 ################################################################################
 # Approval & Sandbox
@@ -7185,10 +9499,19 @@
 # - untrusted: only known-safe read-only commands auto-run; others prompt
 # - on-request: model decides when to ask (default)
 # - never: never prompt (risky)
-# - { reject = { ... } }: auto-reject selected prompt categories
+# - { granular = { ... } }: allow or auto-reject selected prompt categories
 approval_policy = "on-request"
-# Example granular auto-reject policy:
-# approval_policy = { reject = { sandbox_approval = true, rules = false, mcp_elicitations = false } }
+# Who reviews eligible approval prompts: user (default) | auto_review
+# approvals_reviewer = "user"
+
+# Example granular policy:
+# approval_policy = { granular = {
+#   sandbox_approval = true,
+#   rules = true,
+#   mcp_elicitations = true,
+#   request_permissions = false,
+#   skill_approval = false
+# } }
 
 # Allow login-shell semantics for shell-based tools when they request `login = true`.
 # Default: true. Set false to force non-login shells and reject explicit login-shell requests.
@@ -7199,10 +9522,18 @@
 # - workspace-write
 # - danger-full-access (no sandbox; extremely risky)
 sandbox_mode = "read-only"
-
-[windows]
-# Native Windows sandbox mode (Windows only): unelevated | elevated
-sandbox = "unelevated"
+# Named permissions profile to apply by default. Built-ins:
+# :read-only | :workspace | :danger-no-sandbox
+# Use a custom name such as "workspace" only when you also define [permissions.workspace].
+# default_permissions = ":workspace"
+
+# Example filesystem profile. Use `"none"` to deny reads for exact paths or
+# glob patterns. On platforms that need pre-expanded glob matches, set
+# glob_scan_max_depth when using unbounded patterns such as `**`.
+# [permissions.workspace.filesystem]
+# glob_scan_max_depth = 3
+# ":project_roots" = { "." = "write", "**/*.env" = "none" }
+# "/absolute/path/to/secrets" = "none"
 
 ################################################################################
 # Authentication & Login
@@ -7211,11 +9542,14 @@
 # Where to persist CLI login credentials: file (default) | keyring | auto
 cli_auth_credentials_store = "file"
 
-# Base URL for ChatGPT auth flow (not OpenAI API). Default:
+# Base URL for ChatGPT auth flow (not OpenAI API).
 chatgpt_base_url = "https://chatgpt.com/backend-api/"
 
+# Optional base URL override for the built-in OpenAI provider.
+# openai_base_url = "https://us.api.openai.com/v1"
+
 # Restrict ChatGPT login to a specific workspace id. Default: unset.
-# forced_chatgpt_workspace_id = ""
+# forced_chatgpt_workspace_id = "00000000-0000-0000-0000-000000000000"
 
 # Force login mechanism when Codex would normally auto-select. Default: unset.
 # Allowed values: chatgpt | api
@@ -7223,10 +9557,8 @@
 
 # Preferred store for MCP OAuth credentials: auto (default) | file | keyring
 mcp_oauth_credentials_store = "auto"
-
 # Optional fixed port for MCP OAuth callback: 1-65535. Default: unset.
 # mcp_oauth_callback_port = 4321
-
 # Optional redirect URI override for MCP OAuth login (for example, remote devbox ingress).
 # Custom callback paths are supported. `mcp_oauth_callback_port` still controls the listener port.
 # mcp_oauth_callback_url = "https://devbox.example.internal/callback"
@@ -7280,18 +9612,17 @@
 # If you use --yolo or another full access sandbox setting, web search defaults to live.
 web_search = "cached"
 
-################################################################################
-# Profiles (named presets)
-################################################################################
-
 # Active profile name. When unset, no profile is applied.
 # profile = "default"
+
+# Suppress the warning shown when under-development feature flags are enabled.
+# suppress_unstable_features_warning = true
 
 ################################################################################
 # Agents (multi-agent roles and limits)
 ################################################################################
 
-# [agents]
+[agents]
 # Maximum concurrently open agent threads. Default: 6
 # max_threads = 6
 # Maximum nested spawn depth. Root session starts at depth 0. Default: 1
@@ -7300,8 +9631,9 @@
 # job_max_runtime_seconds = 1800
 
 # [agents.reviewer]
-# description = "Find security, correctness, and test risks in code."
+# description = "Find correctness, security, and test risks in code."
 # config_file = "./agents/reviewer.toml"  # relative to the config.toml that defines it
+# nickname_candidates = ["Athena", "Ada"]
 
 ################################################################################
 # Skills (per-skill overrides)
@@ -7311,15 +9643,6 @@
 [[skills.config]]
 # path = "/path/to/skill/SKILL.md"
 # enabled = false
-
-################################################################################
-# Experimental toggles (legacy; prefer [features])
-################################################################################
-
-experimental_use_unified_exec_tool = false
-
-# Include apply_patch via freeform editing path (affects default tool set). Default: false
-experimental_use_freeform_apply_patch = false
 
 ################################################################################
 # Sandbox settings (tables)
@@ -7343,8 +9666,8 @@
 [shell_environment_policy]
 # inherit: all (default) | core | none
 inherit = "all"
-# Skip default excludes for names containing KEY/SECRET/TOKEN (case-insensitive). Default: true
-ignore_default_excludes = true
+# Skip default excludes for names containing KEY/SECRET/TOKEN (case-insensitive). Default: false
+ignore_default_excludes = false
 # Case-insensitive glob patterns to remove (e.g., "AWS_*", "AZURE_*"). Default: []
 exclude = []
 # Explicit key/value overrides (always win). Default: {}
@@ -7355,6 +9678,32 @@
 experimental_use_profile = false
 
 ################################################################################
+# Managed network proxy settings
+################################################################################
+
+# Set `default_permissions = "workspace"` before enabling this profile.
+# [permissions.workspace.network]
+# enabled = true
+# proxy_url = "http://127.0.0.1:43128"
+# admin_url = "http://127.0.0.1:43129"
+# enable_socks5 = false
+# socks_url = "http://127.0.0.1:43130"
+# enable_socks5_udp = false
+# allow_upstream_proxy = false
+# dangerously_allow_non_loopback_proxy = false
+# dangerously_allow_non_loopback_admin = false
+# dangerously_allow_all_unix_sockets = false
+# mode = "limited"                           # limited | full
+# allow_local_binding = false
+#
+# [permissions.workspace.network.domains]
+# "api.openai.com" = "allow"
+# "example.com" = "deny"
+#
+# [permissions.workspace.network.unix_sockets]
+# "/var/run/docker.sock" = "allow"
+
+################################################################################
 # History (table)
 ################################################################################
 
@@ -7362,7 +9711,7 @@
 # save-all (default) | none
 persistence = "save-all"
 # Maximum bytes for history file; oldest entries are trimmed when exceeded. Example: 5242880
-# max_bytes = 0
+# max_bytes = 5242880
 
 ################################################################################
 # UI, Notifications, and Misc (tables)
@@ -7376,6 +9725,9 @@
 # Notification mechanism for terminal alerts: auto | osc9 | bel. Default: "auto"
 # notification_method = "auto"
 
+# When notifications fire: unfocused (default) | always
+# notification_condition = "unfocused"
+
 # Enables welcome/status/spinner animations. Default: true
 animations = true
 
@@ -7390,9 +9742,32 @@
 # Set to [] to hide the footer.
 # status_line = ["model", "context-remaining", "git-branch"]
 
+# Ordered list of terminal window/tab title item IDs. When unset, Codex uses:
+# ["spinner", "project"]. Set to [] to clear the title.
+# Available IDs include app-name, project, spinner, status, thread, git-branch, model,
+# and task-progress.
+# terminal_title = ["spinner", "project"]
+
 # Syntax-highlighting theme (kebab-case). Use /theme in the TUI to preview and save.
 # You can also add custom .tmTheme files under $CODEX_HOME/themes.
 # theme = "catppuccin-mocha"
+
+# Custom key bindings. Context-specific bindings override [tui.keymap.global].
+# Use [] to unbind an action.
+# [tui.keymap.global]
+# open_transcript = "ctrl-t"
+# open_external_editor = []
+#
+# [tui.keymap.composer]
+# submit = ["enter", "ctrl-m"]
+
+# Internal tooltip state keyed by model slug. Usually managed by Codex.
+# [tui.model_availability_nux]
+# "gpt-5.4" = 1
+
+# Enable or disable analytics for this machine. When unset, Codex uses its default behavior.
+[analytics]
+enabled = true
 
 # Control whether users can submit feedback from `/feedback`. Default: true
 [feedback]
@@ -7405,10 +9780,7 @@
 # hide_rate_limit_model_nudge = true
 # hide_gpt5_1_migration_prompt = true
 # "hide_gpt-5.1-codex-max_migration_prompt" = true
-# model_migrations = { "gpt-4.1" = "gpt-5.1" }
-
-# Suppress the warning shown when under-development feature flags are enabled.
-# suppress_unstable_features_warning = true
+# model_migrations = { "gpt-5.3-codex" = "gpt-5.4" }
 
 ################################################################################
 # Centralized Feature Flags (preferred)
@@ -7418,22 +9790,39 @@
 # Leave this table empty to accept defaults. Set explicit booleans to opt in/out.
 # shell_tool = true
 # apps = false
-# apps_mcp_gateway = false
-# web_search_cached = false
-# web_search_request = false
-# unified_exec = false
-# shell_snapshot = false
-# apply_patch_freeform = false
-# multi_agent = false
-# search_tool = false
+# codex_hooks = false
+# unified_exec = true
+# shell_snapshot = true
+# multi_agent = true
 # personality = true
-# request_rule = true
-# collaboration_modes = true
-# use_linux_sandbox_bwrap = false
-# remote_models = false
-# runtime_metrics = false
-# powershell_utf8 = true
-# child_agents_md = false
+# fast_mode = true
+# enable_request_compression = true
+# skill_mcp_dependency_install = true
+# prevent_idle_sleep = false
+
+################################################################################
+# Memories (table)
+################################################################################
+
+# Enable memories with [features].memories, then tune memory behavior here.
+# [memories]
+# generate_memories = true
+# use_memories = true
+# disable_on_external_context = false # legacy alias: no_memories_if_mcp_or_web_search
+
+################################################################################
+# Lifecycle hooks can be configured here inline or in a sibling hooks.json.
+################################################################################
+
+# [hooks]
+# [[hooks.PreToolUse]]
+# matcher = "^Bash$"
+#
+# [[hooks.PreToolUse.hooks]]
+# type = "command"
+# command = 'python3 "/absolute/path/to/pre_tool_use_policy.py"'
+# timeout = 30
+# statusMessage = "Checking Bash command"
 
 ################################################################################
 # Define MCP servers under this table. Leave empty to disable.
@@ -7448,13 +9837,17 @@
 # command = "docs-server"                 # required
 # args = ["--port", "4000"]               # optional
 # env = { "API_KEY" = "value" }           # optional key/value pairs copied as-is
-# env_vars = ["ANOTHER_SECRET"]            # optional: forward these from the parent env
+# env_vars = ["ANOTHER_SECRET"]            # optional: forward local parent env vars
+# env_vars = ["LOCAL_TOKEN", { name = "REMOTE_TOKEN", source = "remote" }]
 # cwd = "/path/to/server"                 # optional working directory override
+# experimental_environment = "remote"      # experimental: run stdio via a remote executor
 # startup_timeout_sec = 10.0               # optional; default 10.0 seconds
 # # startup_timeout_ms = 10000              # optional alias for startup timeout (milliseconds)
 # tool_timeout_sec = 60.0                  # optional; default 60.0 seconds
 # enabled_tools = ["search", "summarize"]  # optional allow-list
 # disabled_tools = ["slow-tool"]           # optional deny-list (applied after allow-list)
+# scopes = ["read:docs"]                   # optional OAuth scopes
+# oauth_resource = "https://docs.example.com/" # optional OAuth resource
 
 # --- Example: Streamable HTTP transport ---
 # [mcp_servers.github]
@@ -7467,69 +9860,70 @@
 # startup_timeout_sec = 10.0                   # optional
 # tool_timeout_sec = 60.0                      # optional
 # enabled_tools = ["list_issues"]             # optional allow-list
+# disabled_tools = ["delete_issue"]           # optional deny-list
+# scopes = ["repo"]                           # optional OAuth scopes
 
 ################################################################################
 # Model Providers
 ################################################################################
 
 # Built-ins include:
-# - openai (Responses API; requires login or OPENAI_API_KEY via auth flow)
-# - oss (Chat Completions API; defaults to http://localhost:11434/v1)
+# - openai
+# - ollama
+# - lmstudio
+# - amazon-bedrock
+# These IDs are reserved. Use a different ID for custom providers.
 
 [model_providers]
+
+# --- Example: built-in Amazon Bedrock provider options ---
+# model_provider = "amazon-bedrock"
+# model = "<bedrock-model-id>"
+# [model_providers.amazon-bedrock.aws]
+# profile = "default"
+# region = "eu-central-1"
 
 # --- Example: OpenAI data residency with explicit base URL or headers ---
 # [model_providers.openaidr]
 # name = "OpenAI Data Residency"
 # base_url = "https://us.api.openai.com/v1"        # example with 'us' domain prefix
-# wire_api = "responses"                           # "responses" | "chat" (default varies)
-# # requires_openai_auth = true                    # built-in OpenAI defaults to true
+# wire_api = "responses"                           # only supported value
+# # requires_openai_auth = true                    # use only for providers backed by OpenAI auth
 # # request_max_retries = 4                        # default 4; max 100
-# # stream_max_retries = 5                         # default 5;  max 100
+# # stream_max_retries = 5                         # default 5; max 100
 # # stream_idle_timeout_ms = 300000                # default 300_000 (5m)
+# # supports_websockets = true                     # optional
 # # experimental_bearer_token = "sk-example"       # optional dev-only direct bearer token
 # # http_headers = { "X-Example" = "value" }
 # # env_http_headers = { "OpenAI-Organization" = "OPENAI_ORGANIZATION", "OpenAI-Project" = "OPENAI_PROJECT" }
 
-# --- Example: Azure (Chat/Responses depending on endpoint) ---
+# --- Example: Azure/OpenAI-compatible provider ---
 # [model_providers.azure]
 # name = "Azure"
 # base_url = "https://YOUR_PROJECT_NAME.openai.azure.com/openai"
-# wire_api = "responses"                          # or "chat" per endpoint
+# wire_api = "responses"
 # query_params = { api-version = "2025-04-01-preview" }
 # env_key = "AZURE_OPENAI_API_KEY"
-# # env_key_instructions = "Set AZURE_OPENAI_API_KEY in your environment"
+# env_key_instructions = "Set AZURE_OPENAI_API_KEY in your environment"
+# # supports_websockets = false
+
+# --- Example: command-backed bearer token auth ---
+# [model_providers.proxy]
+# name = "OpenAI using LLM proxy"
+# base_url = "https://proxy.example.com/v1"
+# wire_api = "responses"
+#
+# [model_providers.proxy.auth]
+# command = "/usr/local/bin/fetch-codex-token"
+# args = ["--audience", "codex"]
+# timeout_ms = 5000
+# refresh_interval_ms = 300000
 
 # --- Example: Local OSS (e.g., Ollama-compatible) ---
-# [model_providers.ollama]
+# [model_providers.local_ollama]
 # name = "Ollama"
 # base_url = "http://localhost:11434/v1"
-# wire_api = "chat"
-
-################################################################################
-# Profiles (named presets)
-################################################################################
-
-[profiles]
-
-# [profiles.default]
-# model = "gpt-5.4"
-# model_provider = "openai"
-# approval_policy = "on-request"
-# sandbox_mode = "read-only"
-# oss_provider = "ollama"
-# model_reasoning_effort = "medium"
-# model_reasoning_summary = "auto"
-# model_verbosity = "medium"
-# personality = "friendly" # or "pragmatic" or "none"
-# chatgpt_base_url = "https://chatgpt.com/backend-api/"
-# model_catalog_json = "./models.json"
-# experimental_compact_prompt_file = "./compact_prompt.txt"
-# include_apply_patch_tool = false
-# experimental_use_unified_exec_tool = false
-# experimental_use_freeform_apply_patch = false
-# tools.web_search = false             # deprecated legacy alias; prefer top-level `web_search`
-# features = { unified_exec = false }
+# wire_api = "responses"
 
 ################################################################################
 # Apps / Connectors
@@ -7553,14 +9947,57 @@
 # enabled = false
 # approval_mode = "approve"
 
+# Optional tool suggestion allowlist for connectors or plugins Codex can offer to install.
+# [tool_suggest]
+# discoverables = [
+#   { type = "connector", id = "gmail" },
+#   { type = "plugin", id = "figma@openai-curated" },
+# ]
+# disabled_tools = [
+#   { type = "plugin", id = "slack@openai-curated" },
+#   { type = "connector", id = "connector_googlecalendar" },
+# ]
+
+################################################################################
+# Profiles (named presets)
+################################################################################
+
+[profiles]
+
+# [profiles.default]
+# model = "gpt-5.4"
+# model_provider = "openai"
+# approval_policy = "on-request"
+# sandbox_mode = "read-only"
+# service_tier = "flex"
+# oss_provider = "ollama"
+# model_reasoning_effort = "medium"
+# plan_mode_reasoning_effort = "high"
+# model_reasoning_summary = "auto"
+# model_verbosity = "medium"
+# personality = "pragmatic" # or "friendly" or "none"
+# chatgpt_base_url = "https://chatgpt.com/backend-api/"
+# model_catalog_json = "./models.json"
+# model_instructions_file = "/absolute/or/relative/path/to/instructions.txt"
+# experimental_compact_prompt_file = "./compact_prompt.txt"
+# tools_view_image = true
+# features = { unified_exec = false }
+
 ################################################################################
 # Projects (trust levels)
 ################################################################################
 
+[projects]
 # Mark specific worktrees as trusted or untrusted.
-[projects]
 # [projects."/absolute/path/to/project"]
 # trust_level = "trusted"  # or "untrusted"
+
+################################################################################
+# Tools
+################################################################################
+
+[tools]
+# view_image = true
 
 ################################################################################
 # OpenTelemetry (OTEL) - disabled by default
@@ -7575,6 +10012,8 @@
 exporter = "none"
 # Trace exporter: none (default) | otlp-http | otlp-grpc
 trace_exporter = "none"
+# Metrics exporter: none | statsig | otlp-http | otlp-grpc
+metrics_exporter = "statsig"
 
 # Example OTLP/HTTP exporter configuration
 # [otel.exporter."otlp-http"]
@@ -7584,38 +10023,24 @@
 # [otel.exporter."otlp-http".headers]
 # "x-otlp-api-key" = "${OTLP_TOKEN}"
 
-# Example OTLP/gRPC exporter configuration
-# [otel.exporter."otlp-grpc"]
-# endpoint = "https://otel.example.com:4317",
-# headers = { "x-otlp-meta" = "abc123" }
-
-# Example OTLP exporter with mutual TLS
-# [otel.exporter."otlp-http"]
-# endpoint = "https://otel.example.com/v1/logs"
-# protocol = "binary"
-
-# [otel.exporter."otlp-http".headers]
-# "x-otlp-api-key" = "${OTLP_TOKEN}"
-
 # [otel.exporter."otlp-http".tls]
 # ca-certificate = "certs/otel-ca.pem"
 # client-certificate = "/etc/codex/certs/client.pem"
 # client-private-key = "/etc/codex/certs/client-key.pem"
-```
+
+# Example OTLP/gRPC trace exporter configuration
+# [otel.trace_exporter."otlp-grpc"]
+# endpoint = "https://otel.example.com:4317"
+# headers = { "x-otlp-meta" = "abc123" }
 
 ################################################################################
-
 # Windows
-
 ################################################################################
 
 [windows]
-
-# Native Windows sandbox mode (Windows only). The example below uses the
-
-# recommended elevated mode.
-
-sandbox = "elevated"
+# Native Windows sandbox mode (Windows only): unelevated | elevated
+sandbox = "unelevated"
+```
 
 ---
 
@@ -7684,58 +10109,61 @@
 
 # Admin Setup
 
+<div class="max-w-1xl mx-auto">
+  <img src="https://developers.openai.com/images/codex/codex_enterprise_admin.png"
+    alt="Codex enterprise admin toggle"
+    class="block w-full mx-auto rounded-lg"
+  />
+</div>
+
+
+
 This guide is for ChatGPT Enterprise admins who want to set up Codex for their workspace.
 
-Use this page as the step-by-step rollout guide. It focuses on setup order and decision points. For detailed policy, configuration, and monitoring details, use the linked pages: [Authentication](https://developers.openai.com/codex/auth), [Agent approvals & security](https://developers.openai.com/codex/agent-approvals-security), [Managed configuration](https://developers.openai.com/codex/enterprise/managed-configuration), and [Governance](https://developers.openai.com/codex/enterprise/governance).
+Use this page as the step-by-step rollout guide. For detailed policy, configuration, and monitoring details, use the linked pages: [Authentication](https://developers.openai.com/codex/auth), [Agent approvals & security](https://developers.openai.com/codex/agent-approvals-security), [Managed configuration](https://developers.openai.com/codex/enterprise/managed-configuration), and [Governance](https://developers.openai.com/codex/enterprise/governance).
 
 ## Enterprise-grade security and privacy
 
 Codex supports ChatGPT Enterprise security features, including:
 
 - No training on enterprise data
-- Zero data retention for the App, CLI, and IDE (code remains in developer environment)
+- Zero data retention for the App, CLI, and IDE (code stays in the developer environment)
 - Residency and retention that follow ChatGPT Enterprise policies
 - Granular user access controls
 - Data encryption at rest (AES-256) and in transit (TLS 1.2+)
+- Audit logging via the ChatGPT Compliance API
 
 For security controls and runtime protections, see [Agent approvals & security](https://developers.openai.com/codex/agent-approvals-security). Refer to [Zero Data Retention (ZDR)](https://platform.openai.com/docs/guides/your-data#zero-data-retention) for more details.
-
-## Local vs. cloud setup
-
-Codex operates in two environments: local and cloud.
-
-1. **Codex local** includes the Codex app, CLI, and IDE extension. The agent runs on the developer's computer in a sandbox.
-2. **Codex cloud** includes hosted Codex features (including Codex cloud, iOS, Code Review, and tasks created by the [Slack integration](https://developers.openai.com/codex/integrations/slack) or [Linear integration](https://developers.openai.com/codex/integrations/linear)). The agent runs remotely in a hosted container with your codebase.
+For a broader enterprise security overview, see the [Codex security white paper](https://trust.openai.com/?itemUid=382f924d-54f3-43a8-a9df-c39e6c959958&source=click).
+
+## Pre-requisites: Determine owners and rollout strategy
+
+During your rollout, team members may support different aspects of integrating Codex into your organization. Ensure you have the following owners:
+
+- **ChatGPT Enterprise workspace owner:** required to configure Codex settings in your workspace.
+- **Security owner:** determines agent permissions settings for Codex.
+- **Analytics owner:** integrates analytics and compliance APIs into your data pipelines.
+
+Decide which Codex surfaces you will use:
+
+- **Codex local:** includes the Codex app, CLI, and IDE extension. The agent runs on the developer's computer in a sandbox.
+- **Codex cloud:** includes hosted Codex features (including Codex cloud, iOS, Code Review, and tasks created by the [Slack integration](https://developers.openai.com/codex/integrations/slack) or [Linear integration](https://developers.openai.com/codex/integrations/linear)). The agent runs remotely in a hosted container with your codebase.
+- **Both:** use local + cloud together.
 
 You can enable local, cloud, or both, and control access with workspace settings and role-based access control (RBAC).
 
-## Step 0: Owners and rollout decision
-
-Ensure you have the following owners:
-
-- Workspace owner with access to ChatGPT Enterprise
-- IT management owner for managed configuration
-- Governance owner for analytics / compliance review
-
-A rollout decision:
-
-- Codex local only (Codex app, CLI, and IDE extension)
-- Codex cloud only (Codex web, GitHub code review)
-- Both local + cloud
-
-Review [authentication](https://developers.openai.com/codex/auth) before rollout:
-
-- Codex local supports ChatGPT sign-in or API keys. Confirm MFA/SSO requirements and any managed login restrictions in authentication
-- Codex cloud requires ChatGPT sign-in
-
-## Step 1: Enable workspace toggles
-
-Turn on only the Codex features you plan to roll out in this phase.
+## Step 1: Enable Codex in your workspace
+
+You configure access to Codex in ChatGPT Enterprise workspace settings.
 
 Go to [Workspace Settings > Settings and Permissions](https://chatgpt.com/admin/settings).
 
 ### Codex local
 
+Codex local is enabled by default for new ChatGPT Enterprise workspaces. If
+  you are not a ChatGPT workspace owner, you can test whether you have access by
+  [installing Codex](https://developers.openai.com/codex/quickstart) and logging in with your work email.
+
 Turn on **Allow members to use Codex Local**.
 
 This enables use of the Codex app, CLI, and IDE extension for allowed users.
@@ -7744,7 +10172,7 @@
 
 #### Enable device code authentication for Codex CLI
 
-Allow developers to sign in with device codes when using Codex CLI in a non-interactive environment. More details in [authentication](https://developers.openai.com/codex/auth/).
+Allow developers to sign in with a device code when using Codex CLI in a non-interactive environment (for example, a remote development box). More details are in [authentication](https://developers.openai.com/codex/auth/).
 
 <div class="max-w-1xl mx-auto py-1">
   <img src="https://developers.openai.com/images/codex/enterprise/local-toggle-config.png"
@@ -7771,12 +10199,6 @@
 
 Note that it may take up to 10 minutes for Codex to appear in ChatGPT.
 
-#### Allow members to administer Codex
-
-Allows users to view overall Codex [workspace analytics](https://chatgpt.com/codex/settings/analytics), access [cloud-managed requirements](https://chatgpt.com/codex/settings/managed-configs), and manage Cloud environments (edit and delete).
-
-Codex cloud not required.
-
 #### Enable Codex Slack app to post answers on task completion
 
 Codex posts its full answer back to Slack when the task completes. Otherwise, Codex posts only a link to the task.
@@ -7787,7 +10209,7 @@
 
 By default, Codex cloud agents have no internet access during runtime to help protect against security and safety risks like prompt injection.
 
-This setting enables users to use an allowlist for common software dependency domains, add more domains and trusted sites, and specify allowed HTTP methods.
+This setting lets users use an allowlist for common software dependency domains, add domains and trusted sites, and specify allowed HTTP methods.
 
 For security implications of internet access and runtime controls, see [Agent approvals & security](https://developers.openai.com/codex/agent-approvals-security).
 
@@ -7800,39 +10222,131 @@
 
 ## Step 2: Set up custom roles (RBAC)
 
-Use RBAC to control which users or groups can access Codex local and Codex cloud.
+Use RBAC to control granular permissions for access Codex local and Codex cloud.
+
+<div class="max-w-1xl mx-auto">
+  <img src="https://developers.openai.com/images/codex/enterprise/rbac_custom_roles.png"
+    alt="Codex cloud toggle"
+    class="block w-full mx-auto rounded-lg"
+  />
+</div>
 
 ### What RBAC lets you do
 
 Workspace Owners can use RBAC in ChatGPT admin settings to:
 
-- Set a default role for users who are not assigned any custom role
+- Set a default role for users who aren't assigned any custom role
 - Create custom roles with granular permissions
-- Assign one or more custom roles to Groups (including SCIM-synced groups)
+- Assign one or more custom roles to Groups
+- Automatically sync users into Groups via SCIM
 - Manage roles centrally from the Custom Roles tab
 
-Users can inherit multiple roles, and permissions resolve to the maximum allowed across those roles.
-
-### Important behavior to plan for
-
-Users in any custom role group do not use the workspace default permissions.
-
-If you are gradually rolling out Codex, one suggestion is to have a "Codex Users" group and a second "Codex Admin" group that has the "Allow members to administer Codex" toggle enabled.
-
-For RBAC setup details and the full permission model, see the [OpenAI RBAC Help Center article](https://help.openai.com/en/articles/11750701-rbac).
-
-## Step 3: Configure Codex local managed settings
-
-For Codex local, set an admin-approved baseline for local behavior before broader rollout.
-
-### Use managed configuration for two different goals
-
-- **Requirements** (`requirements.toml`): Admin-enforced constraints users cannot override
-- **Managed defaults** (`managed_config.toml`): Starting values applied when Codex launches
-
-### Team Config
+Users can inherit more than one role, and permissions resolve to the most permissive (least restrictive) access across those roles.
+
+### Create a Codex Admin group
+
+Set up a dedicated "Codex Admin" group rather than granting Codex administration to a broad audience.
+
+The **Allow members to administer Codex** toggle grants the Codex Admin role. Codex Admins can:
+
+- View Codex [workspace analytics](https://chatgpt.com/codex/settings/analytics)
+- Open the Codex [Policies page](https://chatgpt.com/codex/settings/policies) to manage cloud-managed `requirements.toml` policies
+- Assign those managed policies to user groups or configure a default fallback policy
+- Manage Codex cloud environments, including editing and deleting environments
+
+Use this role for the small set of admins who own Codex rollout, policy management, and governance. It's not required for general Codex users. You don't need Codex cloud to enable this toggle.
+
+Recommended rollout pattern:
+
+- Create a "Codex Users" group for people who should use Codex
+- Create a separate "Codex Admin" group for the smaller set of people who should manage Codex settings and policies
+- Assign the custom role with **Allow members to administer Codex** enabled only to the "Codex Admin" group
+- Keep membership in the "Codex Admin" group limited to workspace owners or designated platform, IT, and governance operators
+- If you use SCIM, back the "Codex Admin" group with your identity provider so membership changes are auditable and centrally managed
+
+This separation makes it easier to roll out Codex while keeping analytics, environment management, and policy deployment limited to trusted admins. For RBAC setup details and the full permission model, see the [OpenAI RBAC Help Center article](https://help.openai.com/en/articles/11750701-rbac).
+
+## Step 3: Configure Codex local requirements
+
+Codex Admins can deploy admin-enforced `requirements.toml` policies from the Codex [Policies page](https://chatgpt.com/codex/settings/policies).
+
+Use this page when you want to apply different local Codex constraints to different groups without distributing device-level files first. The managed policy uses the same `requirements.toml` format described in [Managed configuration](https://developers.openai.com/codex/enterprise/managed-configuration), so you can define allowed approval policies, sandbox modes, web search behavior, MCP server allowlists, feature pins, and restrictive command rules. To disable Browser Use, the in-app browser, or Computer Use, see [Pin feature flags](https://developers.openai.com/codex/enterprise/managed-configuration#pin-feature-flags).
+
+<div class="max-w-1xl mx-auto py-1">
+  <img src="https://developers.openai.com/images/codex/enterprise/policies_and_configurations_page.png"
+    alt="Codex policies and configurations page"
+    class="block w-full mx-auto rounded-lg"
+  />
+</div>
+
+Recommended setup:
+
+1. Create a baseline policy for most users, then create stricter or more permissive variants only where needed.
+2. Assign each managed policy to a specific user group, and configure a default fallback policy for everyone else.
+3. Order group rules with care. If a user matches more than one group-specific rule, the first matching rule applies.
+4. Treat each policy as a complete profile for that group. Codex doesn't fill missing fields from later matching group rules.
+
+These cloud-managed policies apply across Codex local surfaces when users sign in with ChatGPT, including the Codex app, CLI, and IDE extension.
+
+### Example requirements.toml policies
+
+Use cloud-managed `requirements.toml` policies to enforce the guardrails you want for each group. The snippets below are examples you can adapt, not required settings.
+
+<div class="max-w-1xl mx-auto py-1">
+  <img src="https://developers.openai.com/images/codex/enterprise/example_policy.png"
+    alt="Example managed requirements policy"
+    class="block w-full mx-auto rounded-lg"
+  />
+</div>
+
+Example: limit web search, sandbox mode, and approvals for a standard local rollout:
+
+```toml
+allowed_web_search_modes = ["disabled", "cached"]
+allowed_sandbox_modes = ["workspace-write"]
+allowed_approval_policies = ["on-request"]
+```
+
+Example: disable Browser Use, the in-app browser, and Computer Use:
+
+```toml
+[features]
+browser_use = false
+in_app_browser = false
+computer_use = false
+```
+
+Example: add a restrictive command rule when you want admins to block or gate specific commands:
+
+```toml
+[rules]
+prefix_rules = [
+  { pattern = [{ token = "git" }, { any_of = ["push", "commit"] }], decision = "prompt", justification = "Require review before mutating remote history." },
+]
+```
+
+You can use either example on its own or combine them in a single managed policy for a group. For exact keys, precedence, and more examples, see [Managed configuration](https://developers.openai.com/codex/enterprise/managed-configuration) and [Agent approvals & security](https://developers.openai.com/codex/agent-approvals-security).
+
+### Checking user policies
+
+Use the policy lookup tools at the end of the workflow to confirm which managed policy applies to a user. You can check policy assignment by group or by entering a user email.
+
+<div class="max-w-1xl mx-auto py-1">
+  <img src="https://developers.openai.com/images/codex/enterprise/policy_lookup.png"
+    alt="Policy lookup by group or user email"
+    class="block w-full mx-auto rounded-lg"
+  />
+</div>
+
+If you plan to restrict login method or workspace for local clients, see the admin-managed authentication restrictions in [Authentication](https://developers.openai.com/codex/auth).
+
+## Step 4: Standardize local configuration with Team Config
 
 Teams who want to standardize Codex across an organization can use Team Config to share defaults, rules, and skills without duplicating setup on every local configuration.
+
+You can check Team Config settings into the repository under the `.codex` directory. Codex automatically picks up Team Config settings when a user opens that repository.
+
+Start with Team Config for your highest-traffic repositories so teams get consistent behavior in the places they use Codex most.
 
 | Type                                 | Path          | Use it to                                                                    |
 | ------------------------------------ | ------------- | ---------------------------------------------------------------------------- |
@@ -7842,39 +10356,29 @@
 
 For locations and precedence, see [Config basics](https://developers.openai.com/codex/config-basic#configuration-precedence).
 
-### Recommended first decisions for local rollout
-
-Define a baseline for your pilot:
-
-- Approval policy posture
-- Sandbox mode posture
-- Web search posture
-- MCP / connectors policy
-- Local logging and telemetry posture
-
-For exact keys, precedence, MDM deployment, and examples, see [Managed configuration](https://developers.openai.com/codex/enterprise/managed-configuration) and [Agent approvals & security](https://developers.openai.com/codex/agent-approvals-security).
-
-If you plan to restrict login method or workspace for local clients, see the admin-managed authentication restrictions in [Authentication](https://developers.openai.com/codex/auth).
-
-## Step 4: Configure Codex cloud usage (if enabled)
-
-This step covers repository and environment setup after the Codex cloud workspace toggle is enabled.
+## Step 5: Configure Codex cloud usage (if enabled)
+
+This step covers repository and environment setup after you enable the Codex cloud workspace toggle.
 
 ### Connect Codex cloud to repositories
 
 1. Navigate to [Codex](https://chatgpt.com/codex) and select **Get started**
 2. Select **Connect to GitHub** to install the ChatGPT GitHub Connector if you haven't already connected GitHub to ChatGPT
-3. Install or authorize the ChatGPT GitHub Connector
+3. Install or connect the ChatGPT GitHub Connector
 4. Choose an installation target for the ChatGPT Connector (typically your main organization)
 5. Allow the repositories you want to connect to Codex
 
+For GitHub Enterprise Managed Users (EMU), an organization owner must install
+  the Codex GitHub App for the organization before users can connect
+  repositories in Codex cloud.
+
 For more, see [Cloud environments](https://developers.openai.com/codex/cloud/environments).
 
 Codex uses short-lived, least-privilege GitHub App installation tokens for each operation and respects the user's existing GitHub repository permissions and branch protection rules.
 
-### Configure IP addresses (as needed)
-
-Configure connector / IP allow lists if required by your network policy with these [egress IP ranges](https://openai.com/chatgpt-agents.json).
+### Configure IP addresses
+
+If your GitHub organization controls the IP addresses that apps use to connect, make sure to include these [egress IP ranges](https://openai.com/chatgpt-agents.json).
 
 These IP ranges can change. Consider checking them automatically and updating your allow list based on the latest values.
 
@@ -7882,30 +10386,163 @@
 
 To allow Codex to perform code reviews on GitHub, go to [Settings → Code review](https://chatgpt.com/codex/settings/code-review).
 
-Code review can be configured at the repository level. Users can also enable auto review for their PRs and choose when Codex automatically triggers a review. More details on [GitHub](https://developers.openai.com/codex/integrations/github) integration page.
-
-Additional integration docs for [Slack](https://developers.openai.com/codex/integrations/slack), [GitHub](https://developers.openai.com/codex/integrations/github), and [Linear](https://developers.openai.com/codex/integrations/linear).
-
-## Step 5: Set up governance and observability
-
-Codex gives enterprise teams several options for visibility into adoption and impact. Set up governance early so your team can monitor adoption, investigate issues, and support compliance workflows.
+You can configure code review at the repository level. Users can also enable auto review for their PRs and choose when Codex automatically triggers a review. More details are on the [GitHub integration page](https://developers.openai.com/codex/integrations/github).
+
+Use the overview page to confirm your workspace has code review turned on and to see the available review controls.
+
+<div class="max-w-1xl mx-auto py-1">
+  <img src="https://developers.openai.com/images/codex/enterprise/code_review_settings_overview.png"
+    alt="Code review settings overview"
+    class="block w-full mx-auto rounded-lg"
+  />
+</div>
+
+<div class="grid grid-cols-1 gap-4 py-1 md:grid-cols-2">
+  <div class="max-w-1xl mx-auto">
+    <p>
+      Use the auto review settings to decide whether Codex should review pull
+      requests automatically for connected repositories.
+    </p>
+    <img src="https://developers.openai.com/images/codex/enterprise/auto_code_review_settings.png"
+      alt="Automatic code review settings"
+      class="block w-full mx-auto rounded-lg"
+    />
+  </div>
+  <div class="max-w-1xl mx-auto">
+    <p>
+      Use review triggers to control which pull request events should start a
+      Codex review.
+    </p>
+    <img src="https://developers.openai.com/images/codex/enterprise/review_triggers.png"
+      alt="Code review trigger settings"
+      class="block w-full mx-auto rounded-lg"
+    />
+  </div>
+</div>
+
+### Configure Codex security
+
+Codex Security helps engineering and security teams find, confirm, and remediate likely vulnerabilities in connected GitHub repositories.
+
+At a high level, Codex Security:
+
+- scans connected repositories commit by commit
+- ranks likely findings and confirms them when possible
+- shows structured findings with evidence, criticality, and suggested remediation
+- lets teams refine a repository threat model to improve prioritization and review quality
+
+For setup, scan creation, findings review, and threat model guidance, see [Codex Security setup](https://developers.openai.com/codex/security/setup). For a product overview, see [Codex Security](https://developers.openai.com/codex/security).
+
+Integration docs are also available for [Slack](https://developers.openai.com/codex/integrations/slack), [GitHub](https://developers.openai.com/codex/integrations/github), and [Linear](https://developers.openai.com/codex/integrations/linear).
+
+## Step 6: Set up governance and observability
+
+Codex gives enterprise teams options for visibility into adoption and impact. Set up governance early so your team can track adoption, investigate issues, and support compliance workflows.
 
 ### Codex governance typically uses
 
 - Analytics Dashboard for quick, self-serve visibility
-- Analytics API for programmatic reporting and BI integration
+- Analytics API for programmatic reporting and business intelligence integration
 - Compliance API for audit and investigation workflows
 
-### Recommended minimum setup
+### Recommended baseline setup
 
 - Assign an owner for adoption reporting
 - Assign an owner for audit and compliance review
 - Define a review cadence
 - Decide what success looks like
 
-For details and examples, see [Governance](https://developers.openai.com/codex/enterprise/governance).
-
-## Step 6: Confirm and validate setup
+### Analytics API setup steps
+
+To set up the Analytics API key:
+
+1. Sign in to the [OpenAI API Platform Portal](https://platform.openai.com) as an owner or admin, and select the correct organization.
+2. Go to the [API keys page](https://platform.openai.com/settings/organization/api-keys).
+3. Create a new secret key dedicated to Codex Analytics, and give it a descriptive name such as Codex Analytics API.
+4. Select the appropriate project for your organization. If you only have one project, the default project is fine.
+5. Set the key permissions to Read only, since this API only retrieves analytics data.
+6. Copy the key value and store it securely, because you can only view it once.
+7. Email support@openai.com to have that key scoped to `codex.enterprise.analytics.read` only. Wait for OpenAI to confirm your API key has Codex Analytics API access.
+
+<div class="not-prose max-w-md mx-auto py-1">
+  <img src="https://developers.openai.com/images/codex/codex_analytics_key.png"
+    alt="Codex analytics key creation"
+    class="block w-full mx-auto rounded-lg"
+  />
+</div>
+
+To use the Analytics API key:
+
+1. Find your `workspace_id` in the [ChatGPT Admin console](https://chatgpt.com/admin) under Workspace details.
+2. Call the Analytics API at `https://api.chatgpt.com/v1/analytics/codex` using your Platform API key, and include your `workspace_id` in the path.
+3. Choose the endpoint you want to query:
+
+- /workspaces/`{workspace_id}`/usage
+- /workspaces/`{workspace_id}`/code_reviews
+- /workspaces/`{workspace_id}`/code_review_responses
+
+4. Set a reporting date range with `start_time` and `end_time` if needed.
+5. Retrieve the next page of results with `next_page` if the response spans more than one page.
+
+Example curl command to retrieve workspace usage:
+
+```bash
+curl -H "Authorization: Bearer YOUR_PLATFORM_API_KEY" \
+  "https://api.chatgpt.com/v1/analytics/codex/workspaces/WORKSPACE_ID/usage"
+```
+
+For more details on the Analytics API, see [Analytics API](https://developers.openai.com/codex/enterprise/governance#analytics-api).
+
+### Compliance API setup steps
+
+To set up the Compliance API key:
+
+1. Sign in to the [OpenAI API Platform Portal](https://platform.openai.com) as an owner or admin, and select the correct organization.
+2. Go to the [API keys page](https://platform.openai.com/settings/organization/api-keys).
+3. Create a new secret key dedicated to Compliance API and select the appropriate project for your organization. If you only have one project, the default project is fine.
+4. Choose All permissions.
+5. Copy the key value and store it securely, because you can only view it once.
+6. Send an email to support@openai.com with:
+
+- the last 4 digits of the API key
+- the key name
+- the created-by name
+- the scope needed: `read`, `delete`, or both
+
+7. Wait for OpenAI to confirm your API key has Compliance API access.
+
+To use the Compliance API key:
+
+1. Find your `workspace_id` in the [ChatGPT Admin console](https://chatgpt.com/admin) under Workspace details.
+2. Use the Compliance API at `https://api.chatgpt.com/v1/`
+3. Pass your Compliance API key in the Authorization header as a Bearer token.
+4. For Codex-related compliance data, use these endpoints:
+
+- /compliance/workspaces/`{workspace_id}`/logs
+- /compliance/workspaces/`{workspace_id}`/logs/`{log_file_id}`
+- /compliance/workspaces/`{workspace_id}`/codex_tasks
+- /compliance/workspaces/`{workspace_id}`/codex_environments
+
+5. For most Codex compliance integrations, start with the logs endpoint and request Codex event types such as CODEX_LOG or CODEX_SECURITY_LOG.
+6. Use /logs to list available Codex compliance log files, then /logs/`{log_file_id}` to download a specific file.
+
+Example curl command to list compliance log files:
+
+```bash
+curl -L -H "Authorization: Bearer YOUR_COMPLIANCE_API_KEY" \
+  "https://api.chatgpt.com/v1/compliance/workspaces/WORKSPACE_ID/logs?event_type=CODEX_LOG&after=2026-03-01T00:00:00Z"
+```
+
+Example curl command to list Codex tasks:
+
+```bash
+curl -H "Authorization: Bearer YOUR_COMPLIANCE_API_KEY" \
+  "https://api.chatgpt.com/v1/compliance/workspaces/WORKSPACE_ID/codex_tasks"
+```
+
+For more details on the Compliance API, see [Compliance API](https://developers.openai.com/codex/enterprise/governance#compliance-api).
+
+## Step 7: Confirm and verify setup
 
 ### What to verify
 
@@ -7913,12 +10550,12 @@
 - (If enabled) Users can sign in to Codex cloud (ChatGPT sign-in required)
 - MFA and SSO requirements match your enterprise security policy
 - RBAC and workspace toggles produce the expected access behavior
-- Managed configuration is applied for users
+- Managed configuration applies for users
 - Governance data is visible for admins
 
 For authentication options and enterprise login restrictions, see [Authentication](https://developers.openai.com/codex/auth).
 
-Once your team is confident with setup, you can confidently roll Codex out to additional teams and organizations.
+Once your team is confident with setup, you can roll Codex out to more teams and organizations.
 
 ---
 
@@ -7939,69 +10576,75 @@
 ## Analytics Dashboard
 
 <div class="max-w-1xl mx-auto">
-  <img src="https://developers.openai.com/images/codex/enterprise/analytics.png"
+  <img src="https://developers.openai.com/images/codex/enterprise/analytics-dashboard.png"
     alt="Codex analytics dashboard"
-    class="block w-full mx-auto rounded-lg"
+    class="block w-full mx-auto rounded-lg !border-0"
   />
 </div>
 
-### Dashboards
-
-The [analytics dashboard](https://chatgpt.com/codex/settings/analytics) allows ChatGPT workspace administrators to track feature adoption.
-
-Codex provides the following dashboards:
-
-- Daily users by product (CLI, IDE, cloud, Code Review)
-- Daily code review users
-- Daily code reviews
-- Code reviews by priority level
-- Daily code reviews by feedback sentiment
-- Daily cloud tasks
-- Daily cloud users
-- Daily VS Code extension users
-- Daily CLI users
+### Dashboard views
+
+The [analytics dashboard](https://chatgpt.com/codex/cloud/settings/analytics#usage) allows ChatGPT workspace administrators and analytics viewers to track Codex adoption, usage, and Code Review feedback. Usage data can lag by up to 12 hours.
+
+Codex provides date-range controls for daily and weekly views. Key charts include:
+
+- Active users by product surface, including CLI, IDE extension, cloud, desktop, and Code Review
+- Workspace and personal usage breakdowns, including credit and token usage by product surface
+- Product activity for threads and turns by client
+- User ranking table, with filters for client and sort options such as credits, threads, turns, text tokens, and current streak
+- Code Review activity, including PRs reviewed, issues by priority, comments, replies, reactions, and feedback sentiment
+- Skill invocations and agent identity usage when your workspace has those features
 
 ### Data export
 
 Administrators can also export Codex analytics data in CSV or JSON format. Codex provides the following export options:
 
-- Code review users and reviews (Daily unique users and total reviews completed in Code Review)
-- Code review findings and feedback (Daily counts of comments, reactions, replies, and priority-level findings)
-- cloud users and tasks (daily unique cloud users and tasks completed)
-- CLI and VS Code users (Daily unique users for the Codex CLI and VS Code extension)
-- Sessions and messages per user (Daily session starts and user message counts for each Codex user across surfaces)
+- Workspace usage, including daily active users, threads, turns, and credits by surface
+- Usage per user, including daily threads, turns, and credits across surfaces, with optional email addresses when allowed
+- Code Review details, including daily comments, reactions, replies, and priority-level findings
 
 ## Analytics API
 
-Use the [Analytics API](https://chatgpt.com/codex/settings/apireference) when you want to automate reporting, build internal dashboards, or join Codex metrics with your existing engineering data.
+Use the [Analytics API](https://chatgpt.com/codex/cloud/settings/apireference) when you want to automate reporting, build internal dashboards, or join Codex metrics with your existing engineering data.
 
 ### What it measures
 
-The Analytics API provides daily, time-series metrics for a workspace, with optional per-user breakdowns and per-client usage.
+The enterprise Analytics API returns daily or weekly UTC buckets for a workspace. It supports workspace-level and per-user usage, per-client breakdowns, Code Review throughput, Code Review comment priority, and user engagement with Code Review comments.
 
 ### Endpoints
 
-#### Daily usage and adoption
-
-- Daily totals for threads, turns, and credits
-- Breakdown by client surface
-- Optional per-user reporting for adoption and power-user analysis
+The base URL is `https://api.chatgpt.com/v1/analytics/codex`. All endpoints return paginated `page` objects with `has_more` and `next_page`.
+
+Use `start_time` for the inclusive Unix timestamp at the beginning of the reporting window, `end_time` for the exclusive Unix timestamp at the end of the reporting window, `group_by` for `day` or `week` buckets, `limit` for page size, and `page` to continue from a previous response. Requests can look back up to 90 days.
+
+#### Usage
+
+`GET /workspaces/{workspace_id}/usage`
+
+- Returns totals for threads, turns, credits, and per-client usage in daily or weekly buckets.
+- Omit `group` to return per-user rows.
+- Set `group=workspace` to return workspace-wide rows.
+- Includes text input, cached input, and output token fields.
 
 #### Code review activity
 
-- Pull request reviews completed by Codex
-- Total comments generated by Codex
-- Severity breakdown of comments
+`GET /workspaces/{workspace_id}/code_reviews`
+
+- Returns pull request reviews completed by Codex.
+- Returns total comments generated by Codex.
+- Breaks comments down by P0, P1, and P2 priority.
 
 #### User engagement with code review
 
-- Replies to Codex comments
-- Reactions, including upvotes and downvotes
-- Engagement breakdowns for how teams respond to Codex feedback
+`GET /workspaces/{workspace_id}/code_review_responses`
+
+- Returns replies and reactions to Codex comments.
+- Breaks reactions down into positive, negative, and other reactions.
+- Counts comments that received reactions, replies, or either form of engagement.
 
 ### How it works
 
-Analytics is daily and time-windowed. Results are time-ordered and returned in pages with cursor-based pagination. You can query by workspace and optionally group by user or aggregate at the workspace level.
+Analytics uses time windows and supports day or week grouping. Results are time-ordered and returned in pages with cursor-based pagination. Use an API key scoped to `codex.enterprise.analytics.read`.
 
 ### Common use cases
 
@@ -8069,21 +10712,21 @@
 
 ## Admin-enforced requirements (requirements.toml)
 
-Requirements constrain security-sensitive settings (approval policy, sandbox mode, web search mode, and optionally which MCP servers can be enabled). When resolving configuration (for example from `config.toml`, profiles, or CLI config overrides), if a value conflicts with an enforced requirement, Codex falls back to a requirements-compatible value and notifies the user. If an `mcp_servers` allowlist is configured, Codex enables an MCP server only when both its name and identity match an approved entry; otherwise, Codex disables it.
-
-Requirements can also be used to constrain [feature flags](https://developers.openai.com/codex/config-basic/#feature-flags) via the `[features]` table in `requirements.toml`. Note features are generally not security-sensitive, but enterprises have the option of pinning values, if desired. Omitted keys remain unconstrained.
+Requirements constrain security-sensitive settings (approval policy, approvals reviewer, automatic review policy, sandbox mode, web search mode, managed hooks, and optionally which MCP servers users can enable). When resolving configuration (for example from `config.toml`, profiles, or CLI config overrides), if a value conflicts with an enforced rule, Codex falls back to a compatible value and notifies the user. If you configure an `mcp_servers` allowlist, Codex enables an MCP server only when both its name and identity match an approved entry; otherwise, Codex disables it.
+
+Requirements can also constrain [feature flags](https://developers.openai.com/codex/config-basic/#feature-flags) via the `[features]` table in `requirements.toml`. Note that features aren't always security-sensitive, but enterprises can pin values if desired. Omitted keys remain unconstrained.
 
 For the exact key list, see the [`requirements.toml` section in Configuration Reference](https://developers.openai.com/codex/config-reference#requirementstoml).
 
 ### Locations and precedence
 
-Requirements layers are applied in this order (earlier wins per field):
+Codex applies requirements layers in this order (earlier wins per field):
 
 1. Cloud-managed requirements (ChatGPT Business or Enterprise)
 2. macOS managed preferences (MDM) via `com.openai.codex:requirements_toml_base64`
-3. System `requirements.toml` (`/etc/codex/requirements.toml` on Unix systems, including Linux/macOS)
-
-Across layers, requirements are merged per field: if an earlier layer sets a field (including an empty list), later layers do not override that field, but lower layers can still fill fields that remain unset.
+3. System `requirements.toml` (`/etc/codex/requirements.toml` on Unix systems, including Linux/macOS, or `%ProgramData%\OpenAI\Codex\requirements.toml` on Windows)
+
+Across layers, Codex merges requirements per field: if an earlier layer sets a field (including an empty list), later layers don't override that field, but lower layers can still fill fields that remain unset.
 
 For backwards compatibility, Codex also interprets legacy `managed_config.toml` fields `approval_policy` and `sandbox_mode` as requirements (allowing only that single value).
 
@@ -8115,15 +10758,15 @@
 
 Admins can configure different managed requirements for different user groups, and also set a default fallback requirements policy.
 
-If a user matches multiple group-specific rules, the first matching rule applies. Codex does not fill unset requirement fields from later matching group rules.
-
-For example, if the first matching group rule sets only `allowed_sandbox_modes = ["read-only"]` and a later matching group rule sets `allowed_approval_policies = ["on-request"]`, Codex applies only the first matching group rule and does not fill `allowed_approval_policies` from the later rule.
+If a user matches more than one group-specific rule, the first matching rule applies. Codex doesn't fill unset fields from later matching group rules.
+
+For example, if the first matching group rule sets only `allowed_sandbox_modes = ["read-only"]` and a later matching group rule sets `allowed_approval_policies = ["on-request"]`, Codex applies only the first matching group rule and doesn't fill `allowed_approval_policies` from the later rule.
 
 #### How Codex applies cloud-managed requirements locally
 
-When a user starts Codex and signs in with ChatGPT on a Business or Enterprise plan, Codex applies managed requirements on a best-effort basis. Codex first checks for a valid, unexpired local managed requirements cache entry and uses it if available. If the cache is missing, expired, invalid, or does not match the current auth identity, Codex attempts to fetch managed requirements from the service (with retries) and writes a new signed cache entry on success. If no valid cached entry is available and the fetch fails or times out, Codex continues without the managed requirements layer.
-
-After cache resolution, managed requirements are enforced as part of the normal requirements layering described above.
+When a user starts Codex and signs in with ChatGPT on a Business or Enterprise plan, Codex applies managed requirements on a best-effort basis. Codex first checks for a valid, unexpired local managed requirements cache entry and uses it if available. If the cache is missing, expired, corrupted, or doesn't match the current auth identity, Codex attempts to fetch managed requirements from the service (with retries) and writes a new signed cache entry on success. If no valid cached entry is available and the fetch fails or times out, Codex continues without the managed requirements layer.
+
+After cache resolution, Codex enforces managed requirements as part of the normal requirements layering described above.
 
 ### Example requirements.toml
 
@@ -8134,24 +10777,146 @@
 allowed_sandbox_modes = ["read-only", "workspace-write"]
 ```
 
+### Override sandbox requirements by host
+
+Use `[[remote_sandbox_config]]` when one managed policy should apply different
+sandbox requirements on different hosts. For example, you can keep a stricter
+default for laptops while allowing workspace writes on matching devboxes or CI
+runners. Host-specific entries currently override `allowed_sandbox_modes` only:
+
+```toml
+allowed_sandbox_modes = ["read-only"]
+
+[[remote_sandbox_config]]
+hostname_patterns = ["*.devbox.example.com", "runner-??.ci.example.com"]
+allowed_sandbox_modes = ["read-only", "workspace-write"]
+```
+
+Codex compares each `hostname_patterns` entry against the best-effort resolved
+host name. It prefers the fully qualified domain name when available and falls
+back to the local host name. Matching is case-insensitive; `*` matches any
+sequence of characters, and `?` matches one character.
+
+The first matching `[[remote_sandbox_config]]` entry wins within the same
+requirements source. If no entry matches, Codex keeps the top-level
+`allowed_sandbox_modes`. Hostname matching is for policy selection only; don't
+treat it as authenticated device proof.
+
 You can also constrain web search mode:
 
 ```toml
 allowed_web_search_modes = ["cached"] # "disabled" remains implicitly allowed
 ```
 
-`allowed_web_search_modes = []` effectively allows only `"disabled"`.
+`allowed_web_search_modes = []` allows only `"disabled"`.
 For example, `allowed_web_search_modes = ["cached"]` prevents live web search even in `danger-full-access` sessions.
 
-You can also pin [feature flags](https://developers.openai.com/codex/config-basic/#feature-flags):
+### Pin feature flags
+
+You can also pin [feature flags](https://developers.openai.com/codex/config-basic/#feature-flags) for users
+receiving a managed `requirements.toml`:
 
 ```toml
 [features]
 personality = true
 unified_exec = false
-```
-
-Use the canonical feature keys from `config.toml`'s `[features]` table. Codex normalizes the effective feature set to satisfy these pins and rejects conflicting writes to `config.toml` or profile-scoped feature settings.
+
+# Disable specific Codex feature surfaces when needed.
+browser_use = false
+in_app_browser = false
+computer_use = false
+```
+
+Use the canonical feature keys from `config.toml`'s `[features]` table. Codex normalizes the resulting feature set to meet these pins and rejects conflicting writes to `config.toml` or profile-scoped feature settings.
+
+<a id="disable-codex-feature-surfaces"></a>
+
+- `in_app_browser = false` disables the in-app browser pane.
+- `browser_use = false` disables Browser Use and Browser Agent availability.
+- `computer_use = false` disables Computer Use availability and related
+  install or enablement flows.
+
+If omitted, these features are allowed by policy, subject to normal client,
+platform, and rollout availability.
+
+### Configure automatic review policy
+
+Use `allowed_approvals_reviewers` to require or allow automatic review. Set it
+to `["auto_review"]` to require automatic review, or include `"user"` when users
+can choose manual approval.
+
+Set `guardian_policy_config` to replace the tenant-specific section of the
+automatic review policy. Codex still uses the built-in reviewer template and
+output contract. Managed `guardian_policy_config` takes precedence over local
+`[auto_review].policy`.
+
+```toml
+allowed_approval_policies = ["on-request"]
+allowed_approvals_reviewers = ["auto_review"]
+
+guardian_policy_config = """
+## Environment Profile
+- Trusted internal destinations include github.com/my-org, artifacts.example.com,
+  and internal CI systems.
+
+## Tenant Risk Taxonomy and Allow/Deny Rules
+- Treat uploads to unapproved third-party file-sharing services as high risk.
+- Deny actions that expose credentials or private source code to untrusted
+  destinations.
+"""
+```
+
+### Enforce deny-read requirements
+
+Admins can deny reads for exact paths or glob patterns with
+`[permissions.filesystem]`. Users can't weaken these requirements with local
+configuration.
+
+```toml
+[permissions.filesystem]
+deny_read = [
+  "/Users/alice/.ssh",
+  "./private/**/*.txt",
+]
+```
+
+When deny-read requirements are present, Codex constrains local sandbox mode to
+`read-only` or `workspace-write` so Codex can enforce them. On native
+Windows, managed `deny_read` applies to direct file tools; shell subprocess
+reads don't use this sandbox rule.
+
+### Enforce managed hooks from requirements
+
+Admins can also define managed lifecycle hooks directly in `requirements.toml`.
+Use `[hooks]` for the hook configuration itself, and point `managed_dir` at the
+directory where your MDM or endpoint-management tooling installs the referenced
+scripts.
+
+```toml
+[features]
+codex_hooks = true
+
+[hooks]
+managed_dir = "/enterprise/hooks"
+windows_managed_dir = 'C:\enterprise\hooks'
+
+[[hooks.PreToolUse]]
+matcher = "^Bash$"
+
+[[hooks.PreToolUse.hooks]]
+type = "command"
+command = "python3 /enterprise/hooks/pre_tool_use_policy.py"
+timeout = 30
+statusMessage = "Checking managed Bash command"
+```
+
+Notes:
+
+- Codex enforces the hook configuration from `requirements.toml`, but it does
+  not distribute the scripts in `managed_dir`.
+- Deliver those scripts separately with your MDM or device-management solution.
+- Managed hook commands should reference absolute script paths under the
+  configured managed directory.
 
 ### Enforce command rules from requirements
 
@@ -8252,22 +11017,6 @@
 - Keep `network_access = false` unless your security review allows a collector or domains required by your workflows.
 - Use managed configuration to pin OTel settings (exporter, environment), but keep `log_user_prompt = false` unless your policy explicitly allows storing prompt contents.
 - Periodically audit diffs between local `config.toml` and managed policy to catch drift; managed layers should win over local flags and files.
-
----
-
-# Explore
-
-## Get started
-
-
-
-## Use skills
-
-
-
-## Create automations
-
-Automate recurring tasks. Codex adds findings to the inbox and archives runs with nothing to report.
 
 ---
 
@@ -8370,7 +11119,7 @@
 Fine-tune how Codex runs by setting the action inputs that map to `codex exec` options:
 
 - `prompt` or `prompt-file` (choose one): Inline instructions or a repository path to Markdown or text with your task. Consider storing prompts in `.github/codex/prompts/`.
-- `codex-args`: Extra CLI flags. Provide a JSON array (for example `["--full-auto"]`) or a shell string (`--full-auto --sandbox danger-full-access`) to allow edits, streaming, or MCP configuration.
+- `codex-args`: Extra CLI flags. Provide a JSON array (for example `["--json"]`) or a shell string (`--sandbox workspace-write --json`) to allow edits, streaming, or MCP configuration.
 - `model` and `effort`: Pick the Codex agent configuration you want; leave empty for defaults.
 - `sandbox`: Match the sandbox mode (`workspace-write`, `read-only`, `danger-full-access`) to the permissions Codex needs during the run.
 - `output-file`: Save the final Codex message to disk so later steps can upload or diff it.
@@ -8804,7 +11553,7 @@
 
 # Running Codex as an MCP server
 
-You can run Codex as an MCP server and connect it from other MCP clients (for example, an agent built with the [OpenAI Agents SDK](https://openai.github.io/openai-agents-js/guides/mcp/)).
+You can run Codex as an MCP server and connect it from other MCP clients (for example, an agent built with the [OpenAI Agents SDK MCP integration](https://developers.openai.com/api/docs/guides/agents/integrations-observability#mcp)).
 
 To start Codex as an MCP server, you can use the following command:
 
@@ -9213,6 +11962,562 @@
 
 ---
 
+# Hooks
+
+Hooks are an extensibility framework for Codex. They allow
+you to inject your own scripts into the agentic loop, enabling features such as:
+
+- Send the conversation to a custom logging/analytics engine
+- Scan your team's prompts to block accidentally pasting API keys
+- Summarize conversations to create persistent memories automatically
+- Run a custom validation check when a conversation turn stops, enforcing standards
+- Customize prompting when in a certain directory
+
+Hooks are behind a feature flag in `config.toml`:
+
+```toml
+[features]
+codex_hooks = true
+```
+
+Runtime behavior to keep in mind:
+
+- Matching hooks from multiple files all run.
+- Multiple matching command hooks for the same event are launched concurrently,
+  so one hook cannot prevent another matching hook from starting.
+- `PreToolUse`, `PermissionRequest`, `PostToolUse`, `UserPromptSubmit`, and
+  `Stop` run at turn scope.
+
+## Where Codex looks for hooks
+
+Codex discovers hooks next to active config layers in either of these forms:
+
+- `hooks.json`
+- inline `[hooks]` tables inside `config.toml`
+
+Installed plugins can also bundle lifecycle config through their plugin
+manifest or a default `hooks/hooks.json` file. See [Build
+plugins](https://developers.openai.com/codex/plugins/build#bundled-mcp-servers-and-lifecycle-config) for the
+plugin packaging rules.
+
+In practice, the four most useful locations are:
+
+- `~/.codex/hooks.json`
+- `~/.codex/config.toml`
+- `<repo>/.codex/hooks.json`
+- `<repo>/.codex/config.toml`
+
+If more than one hook source exists, Codex loads all matching hooks.
+Higher-precedence config layers do not replace lower-precedence hooks.
+If a single layer contains both `hooks.json` and inline `[hooks]`, Codex
+merges them and warns at startup. Prefer one representation per layer.
+
+Project-local hooks load only when the project `.codex/` layer is trusted. In
+untrusted projects, Codex still loads user and system hooks from their own
+active config layers.
+
+## Config shape
+
+Hooks are organized in three levels:
+
+- A hook event such as `PreToolUse`, `PostToolUse`, or `Stop`
+- A matcher group that decides when that event matches
+- One or more hook handlers that run when the matcher group matches
+
+```json
+{
+  "hooks": {
+    "SessionStart": [
+      {
+        "matcher": "startup|resume",
+        "hooks": [
+          {
+            "type": "command",
+            "command": "python3 ~/.codex/hooks/session_start.py",
+            "statusMessage": "Loading session notes"
+          }
+        ]
+      }
+    ],
+    "PreToolUse": [
+      {
+        "matcher": "Bash",
+        "hooks": [
+          {
+            "type": "command",
+            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py\"",
+            "statusMessage": "Checking Bash command"
+          }
+        ]
+      }
+    ],
+    "PermissionRequest": [
+      {
+        "matcher": "Bash",
+        "hooks": [
+          {
+            "type": "command",
+            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/permission_request.py\"",
+            "statusMessage": "Checking approval request"
+          }
+        ]
+      }
+    ],
+    "PostToolUse": [
+      {
+        "matcher": "Bash",
+        "hooks": [
+          {
+            "type": "command",
+            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/post_tool_use_review.py\"",
+            "statusMessage": "Reviewing Bash output"
+          }
+        ]
+      }
+    ],
+    "UserPromptSubmit": [
+      {
+        "hooks": [
+          {
+            "type": "command",
+            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/user_prompt_submit_data_flywheel.py\""
+          }
+        ]
+      }
+    ],
+    "Stop": [
+      {
+        "hooks": [
+          {
+            "type": "command",
+            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/stop_continue.py\"",
+            "timeout": 30
+          }
+        ]
+      }
+    ]
+  }
+}
+```
+
+Notes:
+
+- `timeout` is in seconds.
+- If `timeout` is omitted, Codex uses `600` seconds.
+- `statusMessage` is optional.
+- Commands run with the session `cwd` as their working directory.
+- For repo-local hooks, prefer resolving from the git root instead of using a
+  relative path such as `.codex/hooks/...`. Codex may be started from a
+  subdirectory, and a git-root-based path keeps the hook location stable.
+
+Equivalent inline TOML in `config.toml`:
+
+```toml
+[features]
+codex_hooks = true
+
+[[hooks.PreToolUse]]
+matcher = "^Bash$"
+
+[[hooks.PreToolUse.hooks]]
+type = "command"
+command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py"'
+timeout = 30
+statusMessage = "Checking Bash command"
+
+[[hooks.PostToolUse]]
+matcher = "^Bash$"
+
+[[hooks.PostToolUse.hooks]]
+type = "command"
+command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/post_tool_use_review.py"'
+timeout = 30
+statusMessage = "Reviewing Bash output"
+```
+
+## Managed hooks from `requirements.toml`
+
+Enterprise-managed requirements can also define hooks inline under `[hooks]`.
+This is useful when admins want to enforce the hook configuration while
+delivering the actual scripts through MDM or another device-management system.
+
+```toml
+[features]
+codex_hooks = true
+
+[hooks]
+managed_dir = "/enterprise/hooks"
+windows_managed_dir = 'C:\enterprise\hooks'
+
+[[hooks.PreToolUse]]
+matcher = "^Bash$"
+
+[[hooks.PreToolUse.hooks]]
+type = "command"
+command = "python3 /enterprise/hooks/pre_tool_use_policy.py"
+timeout = 30
+statusMessage = "Checking managed Bash command"
+```
+
+Notes for managed hooks:
+
+- `managed_dir` is used on macOS and Linux.
+- `windows_managed_dir` is used on Windows.
+- Codex does not distribute the scripts in `managed_dir`; your enterprise
+  tooling must install and update them separately.
+- Managed hook commands should use absolute script paths under the configured
+  managed directory.
+
+## Matcher patterns
+
+The `matcher` field is a regex string that filters when hooks fire. Use `"*"`,
+`""`, or omit `matcher` entirely to match every occurrence of a supported
+event.
+
+Only some current Codex events honor `matcher`:
+
+| Event               | What `matcher` filters | Notes                                                        |
+| ------------------- | ---------------------- | ------------------------------------------------------------ |
+| `PermissionRequest` | tool name              | Support includes `Bash`, `apply_patch`\*, and MCP tool names |
+| `PostToolUse`       | tool name              | Support includes `Bash`, `apply_patch`\*, and MCP tool names |
+| `PreToolUse`        | tool name              | Support includes `Bash`, `apply_patch`\*, and MCP tool names |
+| `SessionStart`      | start source           | Current runtime values are `startup`, `resume`, and `clear`  |
+| `UserPromptSubmit`  | not supported          | Any configured `matcher` is ignored for this event           |
+| `Stop`              | not supported          | Any configured `matcher` is ignored for this event           |
+
+\*For `apply_patch`, matchers can also use `Edit` or `Write`.
+
+Examples:
+
+- `Bash`
+- `^apply_patch$`
+- `Edit|Write`
+- `mcp__filesystem__read_file`
+- `mcp__filesystem__.*`
+- `startup|resume|clear`
+
+## Common input fields
+
+Every command hook receives one JSON object on `stdin`.
+
+These are the shared fields you will usually use:
+
+| Field             | Type             | Meaning                                     |
+| ----------------- | ---------------- | ------------------------------------------- |
+| `session_id`      | `string`         | Current session or thread id.               |
+| `transcript_path` | `string \| null` | Path to the session transcript file, if any |
+| `cwd`             | `string`         | Working directory for the session           |
+| `hook_event_name` | `string`         | Current hook event name                     |
+| `model`           | `string`         | Active model slug                           |
+
+Turn-scoped hooks list `turn_id` in their event-specific tables.
+
+If you need the full wire format, see [Schemas](#schemas).
+
+## Common output fields
+
+`SessionStart`, `UserPromptSubmit`, and `Stop` support these shared JSON
+fields:
+
+```json
+{
+  "continue": true,
+  "stopReason": "optional",
+  "systemMessage": "optional",
+  "suppressOutput": false
+}
+```
+
+| Field            | Effect                                          |
+| ---------------- | ----------------------------------------------- |
+| `continue`       | If `false`, marks that hook run as stopped      |
+| `stopReason`     | Recorded as the reason for stopping             |
+| `systemMessage`  | Surfaced as a warning in the UI or event stream |
+| `suppressOutput` | Parsed today but not yet implemented            |
+
+Exit `0` with no output is treated as success and Codex continues.
+
+`PreToolUse` and `PermissionRequest` support `systemMessage`, but `continue`,
+`stopReason`, and `suppressOutput` aren't currently supported for those events.
+
+`PostToolUse` supports `systemMessage`, `continue: false`, and `stopReason`.
+`suppressOutput` is parsed but not currently supported for that event.
+
+## Hooks
+
+### SessionStart
+
+`matcher` is applied to `source` for this event.
+
+Fields in addition to [Common input fields](#common-input-fields):
+
+| Field    | Type     | Meaning                                        |
+| -------- | -------- | ---------------------------------------------- |
+| `source` | `string` | How the session started: `startup` or `resume` |
+
+Plain text on `stdout` is added as extra developer context.
+
+JSON on `stdout` supports [Common output fields](#common-output-fields) and this
+hook-specific shape:
+
+```json
+{
+  "hookSpecificOutput": {
+    "hookEventName": "SessionStart",
+    "additionalContext": "Load the workspace conventions before editing."
+  }
+}
+```
+
+That `additionalContext` text is added as extra developer context.
+
+### PreToolUse
+
+`PreToolUse` can intercept Bash, file edits performed through `apply_patch`,
+and MCP tool calls. It is still a guardrail rather than a complete enforcement
+boundary because Codex can often perform equivalent work through another
+supported tool path.
+
+This doesn't intercept all shell calls yet, only the simple ones. The newer
+  `unified_exec` mechanism allows richer streaming stdin/stdout handling of
+  shell, but interception is incomplete. Similarly, this doesn't intercept
+  `WebSearch` or other non-shell, non-MCP tool calls.
+
+`matcher` is applied to `tool_name` and matcher aliases. For file edits through
+`apply_patch`, matchers can use `apply_patch`, `Edit`, or `Write`; hook input
+still reports `tool_name: "apply_patch"`.
+
+Fields in addition to [Common input fields](#common-input-fields):
+
+| Field         | Type         | Meaning                                                                                                   |
+| ------------- | ------------ | --------------------------------------------------------------------------------------------------------- |
+| `turn_id`     | `string`     | Codex-specific extension. Active Codex turn id                                                            |
+| `tool_name`   | `string`     | Canonical hook tool name, such as `Bash`, `apply_patch`, or an MCP name like `mcp__fs__read`              |
+| `tool_use_id` | `string`     | Tool-call id for this invocation                                                                          |
+| `tool_input`  | `JSON value` | Tool-specific input. `Bash` and `apply_patch` use `tool_input.command` while MCP tools send all the args. |
+
+Plain text on `stdout` is ignored.
+
+JSON on `stdout` can use `systemMessage` and can block a Bash command with this
+hook-specific shape:
+
+```json
+{
+  "hookSpecificOutput": {
+    "hookEventName": "PreToolUse",
+    "permissionDecision": "deny",
+    "permissionDecisionReason": "Destructive command blocked by hook."
+  }
+}
+```
+
+Codex also accepts this older block shape:
+
+```json
+{
+  "decision": "block",
+  "reason": "Destructive command blocked by hook."
+}
+```
+
+You can also use exit code `2` and write the blocking reason to `stderr`.
+
+`permissionDecision: "allow"` and `"ask"`, legacy `decision: "approve"`,
+`updatedInput`, `additionalContext`, `continue: false`, `stopReason`, and
+`suppressOutput` are parsed but not supported yet, so they fail open.
+
+### PermissionRequest
+
+`PermissionRequest` runs when Codex is about to ask for approval, such as a
+shell escalation or managed-network approval. It can allow the request, deny
+the request, or decline to decide and let the normal approval prompt continue.
+It doesn't run for commands that don't need approval.
+
+`matcher` is applied to `tool_name` and matcher aliases. Current canonical
+values include `Bash`, `apply_patch`, and MCP tool names such as
+`mcp__server__tool`; `apply_patch` also matches `Edit` and `Write`.
+
+Fields in addition to [Common input fields](#common-input-fields):
+
+| Field                    | Type             | Meaning                                                                                                   |
+| ------------------------ | ---------------- | --------------------------------------------------------------------------------------------------------- |
+| `turn_id`                | `string`         | Codex-specific extension. Active Codex turn id                                                            |
+| `tool_name`              | `string`         | Canonical hook tool name, such as `Bash`, `apply_patch`, or an MCP name like `mcp__fs__read`              |
+| `tool_input`             | `JSON value`     | Tool-specific input. `Bash` and `apply_patch` use `tool_input.command` while MCP tools send all the args. |
+| `tool_input.description` | `string \| null` | Human-readable approval reason, when Codex has one                                                        |
+
+Plain text on `stdout` is ignored.
+
+To approve the request, return:
+
+```json
+{
+  "hookSpecificOutput": {
+    "hookEventName": "PermissionRequest",
+    "decision": {
+      "behavior": "allow"
+    }
+  }
+}
+```
+
+To deny the request, return:
+
+```json
+{
+  "hookSpecificOutput": {
+    "hookEventName": "PermissionRequest",
+    "decision": {
+      "behavior": "deny",
+      "message": "Blocked by repository policy."
+    }
+  }
+}
+```
+
+If multiple matching hooks return decisions, any `deny` wins. Otherwise, an
+`allow` lets the request proceed without surfacing the approval prompt. If no
+matching hook decides, Codex uses the normal approval flow.
+
+Don't return `updatedInput`, `updatedPermissions`, or `interrupt` for
+`PermissionRequest`; those fields are reserved for future behavior and fail
+closed today.
+
+### PostToolUse
+
+`PostToolUse` runs after supported tools produce output, including Bash,
+`apply_patch`, and MCP tool calls. For Bash, it also runs after commands that
+exit with a non-zero status. It can't undo side effects from the tool that
+already ran.
+
+This doesn't intercept all shell calls yet, only the simple ones. The newer
+  `unified_exec` mechanism allows richer streaming stdin/stdout handling of
+  shell, but interception is incomplete. Similarly, this doesn't intercept
+  `WebSearch` or other non-shell, non-MCP tool calls.
+
+`matcher` is applied to `tool_name` and matcher aliases. For file edits through
+`apply_patch`, matchers can use `apply_patch`, `Edit`, or `Write`; hook input
+still reports `tool_name: "apply_patch"`.
+
+Fields in addition to [Common input fields](#common-input-fields):
+
+| Field           | Type         | Meaning                                                                                                   |
+| --------------- | ------------ | --------------------------------------------------------------------------------------------------------- |
+| `turn_id`       | `string`     | Codex-specific extension. Active Codex turn id                                                            |
+| `tool_name`     | `string`     | Canonical hook tool name, such as `Bash`, `apply_patch`, or an MCP name like `mcp__fs__read`              |
+| `tool_use_id`   | `string`     | Tool-call id for this invocation                                                                          |
+| `tool_input`    | `JSON value` | Tool-specific input. `Bash` and `apply_patch` use `tool_input.command` while MCP tools send all the args. |
+| `tool_response` | `JSON value` | Tool-specific output. For MCP tools, this is the MCP call result.                                         |
+
+Plain text on `stdout` is ignored.
+
+JSON on `stdout` can use `systemMessage` and this hook-specific shape:
+
+```json
+{
+  "decision": "block",
+  "reason": "The Bash output needs review before continuing.",
+  "hookSpecificOutput": {
+    "hookEventName": "PostToolUse",
+    "additionalContext": "The command updated generated files."
+  }
+}
+```
+
+That `additionalContext` text is added as extra developer context.
+
+For this event, `decision: "block"` doesn't undo the completed Bash command.
+Instead, Codex records the feedback, replaces the tool result with that
+feedback, and continues the model from the hook-provided message.
+
+You can also use exit code `2` and write the feedback reason to `stderr`.
+
+To stop normal processing of the original tool result after the command has
+already run, return `continue: false`. Codex will replace the tool result with
+your feedback or stop text and continue from there.
+
+`updatedMCPToolOutput` and `suppressOutput` are parsed but not supported yet,
+so they fail open.
+
+### UserPromptSubmit
+
+`matcher` isn't currently used for this event.
+
+Fields in addition to [Common input fields](#common-input-fields):
+
+| Field     | Type     | Meaning                                        |
+| --------- | -------- | ---------------------------------------------- |
+| `turn_id` | `string` | Codex-specific extension. Active Codex turn id |
+| `prompt`  | `string` | User prompt that's about to be sent            |
+
+Plain text on `stdout` is added as extra developer context.
+
+JSON on `stdout` supports [Common output fields](#common-output-fields) and
+this hook-specific shape:
+
+```json
+{
+  "hookSpecificOutput": {
+    "hookEventName": "UserPromptSubmit",
+    "additionalContext": "Ask for a clearer reproduction before editing files."
+  }
+}
+```
+
+That `additionalContext` text is added as extra developer context.
+
+To block the prompt, return:
+
+```json
+{
+  "decision": "block",
+  "reason": "Ask for confirmation before doing that."
+}
+```
+
+You can also use exit code `2` and write the blocking reason to `stderr`.
+
+### Stop
+
+`matcher` isn't currently used for this event.
+
+Fields in addition to [Common input fields](#common-input-fields):
+
+| Field                    | Type             | Meaning                                           |
+| ------------------------ | ---------------- | ------------------------------------------------- |
+| `turn_id`                | `string`         | Codex-specific extension. Active Codex turn id    |
+| `stop_hook_active`       | `boolean`        | Whether this turn was already continued by `Stop` |
+| `last_assistant_message` | `string \| null` | Latest assistant message text, if available       |
+
+`Stop` expects JSON on `stdout` when it exits `0`. Plain text output is invalid
+for this event.
+
+JSON on `stdout` supports [Common output fields](#common-output-fields). To keep
+Codex going, return:
+
+```json
+{
+  "decision": "block",
+  "reason": "Run one more pass over the failing tests."
+}
+```
+
+You can also use exit code `2` and write the continuation reason to `stderr`.
+
+For this event, `decision: "block"` doesn't reject the turn. Instead, it tells
+Codex to continue and automatically creates a new continuation prompt that acts
+as a new user prompt, using your `reason` as that prompt text.
+
+If any matching `Stop` hook returns `continue: false`, that takes precedence
+over continuation decisions from other matching `Stop` hooks.
+
+## Schemas
+
+If you need the exact current wire format, see the generated schemas in the
+[Codex GitHub repository](https://github.com/openai/codex/tree/main/codex-rs/hooks/schema/generated).
+
+---
+
 # Codex IDE extension
 
 Codex is OpenAI's coding agent that can read, edit, and run code. It helps you build faster, squash bugs, and understand unfamiliar code. With the Codex VS Code extension, you can use Codex side by side in your IDE or delegate tasks to Codex Cloud.
@@ -9233,11 +12538,13 @@
 - [Download for Visual Studio Code Insiders](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt)
 - [Download for JetBrains IDEs](#jetbrains-ide-integration)
 
-The Codex VS Code extension is available on macOS and Linux. Windows support
-  is experimental. For the best Windows experience, use Codex in a WSL workspace
-  and follow our <a href="/codex/windows">Windows setup guide</a>.
-
-After you install it, you'll find the extension in your left sidebar next to your other extensions.
+Codex IDE integrations for VS Code-compatible editors and JetBrains IDEs are
+  available on macOS, Windows, and Linux. On Windows, run Codex natively with
+  the Windows sandbox, or use WSL2 when you need a Linux-native environment. For
+  setup details, see the <a href="/codex/windows">Windows setup guide</a>.
+
+After you install it, you'll find Codex in your editor sidebar.
+In VS Code, Codex opens in the right sidebar by default.
 If you're using VS Code, restart the editor if you don't see Codex right away.
 
 If you're using Cursor, the activity bar displays horizontally by default. Collapsed items can hide Codex, so you can pin it and reorganize the order of the extensions.
@@ -9255,9 +12562,11 @@
 
 ### Move Codex to the right sidebar <a id="right-sidebar"></a>
 
-In VS Code, you can drag the Codex icon to the right of your editor to move it to the right sidebar.
-
-In some IDEs, like Cursor, you may need to temporarily change the activity bar orientation first:
+In VS Code, Codex appears in the right sidebar automatically.
+If you prefer it in the primary (left) sidebar, drag the Codex icon back to the left activity bar.
+
+In VS Code forks like Cursor, you may need to move Codex to the right sidebar manually.
+To do that, you may need to temporarily change the activity bar orientation first:
 
 1. Open your editor settings and search for `activity bar` (in Workbench settings).
 2. Change the orientation to `vertical`.
@@ -9268,6 +12577,7 @@
 Now drag the Codex icon to the right sidebar (for example, next to your Cursor chat). Codex appears as another tab in the sidebar.
 
 After you move it, reset the activity bar orientation to `horizontal` to restore the default behavior.
+If you change your mind later, you can drag Codex back to the primary (left) sidebar at any time.
 
 ### Sign in
 
@@ -9284,6 +12594,7 @@
 To see all available commands and bind them as keyboard shortcuts, select the settings icon in the Codex chat and select **Keyboard shortcuts**.
 You can also refer to the [Codex IDE extension commands](https://developers.openai.com/codex/ide/commands) page.
 For a list of supported slash commands, see [Codex IDE extension slash commands](https://developers.openai.com/codex/ide/slash-commands).
+If you're new to Codex, read the [best practices guide](https://developers.openai.com/codex/learn/best-practices).
 
 ---
 
@@ -9310,6 +12621,14 @@
 ### Adjust reasoning effort
 
 Choose `low`, `medium`, or `high` to trade off speed and depth based on the task.
+
+  </BentoContent>
+
+  <BentoContent href="/codex/ide/features#image-generation">
+
+### Image generation
+
+Generate or edit images without leaving your editor, and use reference assets when you need iteration.
 
   </BentoContent>
 
@@ -9415,7 +12734,7 @@
 
 ## Adjust reasoning effort
 
-You can adjust reasoning effort to control how long Codex thinks before responding. Higher effort can help on complex tasks, but responses take longer. Higher effort also uses more tokens and can consume your rate limits faster (especially with GPT-5-Codex).
+You can adjust reasoning effort to control how long Codex thinks before responding. Higher effort can help on complex tasks, but responses take longer. Higher effort also uses more tokens and can consume your rate limits faster, especially with higher-capability models.
 
 Use the same model switcher shown above, and choose `low`, `medium`, or `high` for each model. Start with `medium`, and only switch to `high` when you need more depth.
 
@@ -9478,6 +12797,16 @@
 
 Hold down `Shift` while dropping an image. VS Code otherwise prevents extensions from accepting a drop.
 
+## Image generation
+
+Ask Codex to generate or edit images without leaving your editor. This is useful for UI assets, layouts, illustrations, sprite sheets, and quick placeholders while you work. Add a reference image to the prompt when you want Codex to transform or extend an existing asset.
+
+You can ask in natural language or explicitly invoke the image generation skill by including `$imagegen` in your prompt.
+
+Built-in image generation uses `gpt-image-2`, counts toward your general Codex usage limits, and uses included limits 3-5x faster on average than similar turns without image generation, depending on image quality and size. For details, see [Pricing](https://developers.openai.com/codex/pricing#image-generation-usage-limits). For prompting tips and model details, see the [image generation guide](https://developers.openai.com/api/docs/guides/image-generation).
+
+For larger batches of image generation, set `OPENAI_API_KEY` in your environment variables and ask Codex to generate images through the API so API pricing applies instead.
+
 ## See also
 
 - [Codex IDE extension settings](https://developers.openai.com/codex/ide/settings)
@@ -9498,15 +12827,19 @@
 
 The Codex IDE extension uses the Codex CLI. Configure some behavior, such as the default model, approvals, and sandbox settings, in the shared `~/.codex/config.toml` file instead of in editor settings. See [Config basics](https://developers.openai.com/codex/config-basic).
 
+The extension also honors VS Code's built-in chat font settings for Codex conversation surfaces.
+
 ## Settings reference
 
-| Setting                                      | Description                                                                                                                                                                                                                                                          |
-| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
-| `chatgpt.cliExecutable`                      | Development only: Path to the Codex CLI executable. You don't need to set this unless you're actively developing the Codex CLI. If you set this manually, parts of the extension might not work as expected.                                                         |
-| `chatgpt.commentCodeLensEnabled`             | Show CodeLens above to-do comments so you can complete them with Codex.                                                                                                                                                                                              |
-| `chatgpt.localeOverride`                     | Preferred language for the Codex UI. Leave empty to detect automatically.                                                                                                                                                                                            |
-| `chatgpt.openOnStartup`                      | Focus the Codex sidebar when the extension finishes starting.                                                                                                                                                                                                        |
-| `chatgpt.runCodexInWindowsSubsystemForLinux` | Windows only: Run Codex in WSL when Windows Subsystem for Linux (WSL) is available. Recommended for improved sandbox security and better performance. Codex agent mode on Windows currently requires WSL. Changing this setting reloads VS Code to apply the change. |
+| Setting                                      | Description                                                                                                                                                                                                                                                                                                           |
+| -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
+| `chat.fontSize`                              | Controls chat text in the Codex sidebar, including conversation content and the composer.                                                                                                                                                                                                                             |
+| `chat.editor.fontSize`                       | Controls code-rendered content in Codex conversations, including code snippets and diffs.                                                                                                                                                                                                                             |
+| `chatgpt.cliExecutable`                      | Development only: Path to the Codex CLI executable. You don't need to set this unless you're actively developing the Codex CLI. If you set this manually, parts of the extension might not work as expected.                                                                                                          |
+| `chatgpt.commentCodeLensEnabled`             | Show CodeLens above to-do comments so you can complete them with Codex.                                                                                                                                                                                                                                               |
+| `chatgpt.localeOverride`                     | Preferred language for the Codex UI. Leave empty to detect automatically.                                                                                                                                                                                                                                             |
+| `chatgpt.openOnStartup`                      | Focus the Codex sidebar when the extension finishes starting.                                                                                                                                                                                                                                                         |
+| `chatgpt.runCodexInWindowsSubsystemForLinux` | Windows only: Run Codex in WSL when Windows Subsystem for Linux (WSL) is available. Use this when your repositories and tooling live in WSL2 or when you need Linux-native tooling. Otherwise, Codex can run natively on Windows with the Windows sandbox. Changing this setting reloads VS Code to apply the change. |
 
 ---
 
@@ -9534,16 +12867,27 @@
 
 ---
 
-# Use Codex in GitHub
-
-Use Codex to review pull requests without leaving GitHub. Add a pull request comment with `@codex review`, and Codex replies with a standard GitHub code review.
+# Codex code review in GitHub
+
+Use Codex code review to get another high-signal review pass on GitHub pull
+requests. Codex reviews the pull request diff, follows your repository guidance,
+and posts a standard GitHub code review focused on serious issues.
 
 <br />
 
-## Set up code review
+## Before you start
+
+Make sure you have:
+
+- [Codex cloud](https://developers.openai.com/codex/cloud) set up for the repository you want to review.
+- Access to [Codex code review settings](https://chatgpt.com/codex/settings/code-review).
+- An `AGENTS.md` file if you want Codex to follow repository-specific review guidance.
+
+## Set up Codex code review
 
 1. Set up [Codex cloud](https://developers.openai.com/codex/cloud).
-2. Go to [Codex settings](https://chatgpt.com/codex/settings/code-review) and turn on **Code review** for your repository.
+2. Go to [Codex settings](https://chatgpt.com/codex/settings/code-review).
+3. Turn on **Code review** for your repository.
 
 <div class="not-prose max-w-3xl mr-auto">
   <img src="https://developers.openai.com/images/codex/code-review/code-review-settings.png"
@@ -9553,7 +12897,7 @@
 </div>
 <br />
 
-## Request a review
+## Request a Codex review
 
 1. In a pull request comment, mention `@codex review`.
 2. Wait for Codex to react (👀) and post a review.
@@ -9566,7 +12910,9 @@
 </div>
 <br />
 
-Codex posts a review on the pull request, just like a teammate would.
+Codex posts a review on the pull request, just like a teammate would. In
+GitHub, Codex flags only P0 and P1 issues so review comments stay focused on
+high-priority risks.
 
 <div class="not-prose max-w-3xl mr-auto">
   <img src="https://developers.openai.com/images/codex/code-review/review-example.png"
@@ -9578,7 +12924,10 @@
 
 ## Enable automatic reviews
 
-If you want Codex to review every pull request automatically, turn on **Automatic reviews** in [Codex settings](https://chatgpt.com/codex/settings/code-review). Codex will post a review whenever a new PR is opened for review, without needing an `@codex review` comment.
+If you want Codex to review every pull request automatically, turn on
+**Automatic reviews** in [Codex settings](https://chatgpt.com/codex/settings/code-review).
+Codex will post a review whenever someone opens a new PR for review, without
+needing an `@codex review` comment.
 
 ## Customize what Codex reviews
 
@@ -9595,11 +12944,24 @@
 
 Codex applies guidance from the closest `AGENTS.md` to each changed file. You can place more specific instructions deeper in the tree when particular packages need extra scrutiny.
 
-For a one-off focus, add it to your pull request comment, for example:
+For a one-off focus, add it to your pull request comment:
 
 `@codex review for security regressions`
 
-In GitHub, Codex flags only P0 and P1 issues. If you want Codex to flag typos in documentation, add guidance in `AGENTS.md` (for example, “Treat typos in docs as P1.”).
+If you want Codex to flag typos in documentation, add guidance in `AGENTS.md`
+(for example, “Treat typos in docs as P1.”).
+
+## Act on review findings
+
+After Codex posts a review, you can ask it to fix issues in the same pull
+request by leaving another comment:
+
+```md
+@codex fix the P1 issue
+```
+
+Codex starts a cloud task with the pull request as context and can push a fix
+back to the branch when it has permission to do so.
 
 ## Give Codex other tasks
 
@@ -9608,6 +12970,16 @@
 ```md
 @codex fix the CI failures
 ```
+
+## Troubleshoot code review
+
+If Codex doesn't react or post a review:
+
+- Confirm you turned on **Code review** for the repository in [Codex settings](https://chatgpt.com/codex/settings/code-review).
+- Confirm the pull request belongs to a repository with [Codex cloud](https://developers.openai.com/codex/cloud) set up.
+- Use the exact trigger `@codex review` in a pull request comment.
+- For automatic reviews, check that you turned on **Automatic reviews** and that
+  the pull request event matches your review trigger settings.
 
 ---
 
@@ -9799,6 +13171,232 @@
 
 ---
 
+# Best practices
+
+If you’re new to Codex or coding agents in general, this guide will help you get better results faster. It covers the core habits that make Codex more effective across the [CLI](https://developers.openai.com/codex/cli), [IDE extension](https://developers.openai.com/codex/ide), and the [Codex app](https://developers.openai.com/codex/app), from prompting and planning to validation, MCP, skills, and automations.
+
+Codex works best when you treat it less like a one-off assistant and more like a teammate you configure and improve over time.
+
+A useful way to think about this: start with the right task context, use `AGENTS.md` for durable guidance, configure Codex to match your workflow, connect external systems with MCP, turn repeated work into skills, and automate stable workflows.
+
+## Strong first use: Context and prompts
+
+Codex is already strong enough to be useful even when your prompt isn't perfect. You can often hand it a hard problem with minimal setup and still get a strong result. Clear [prompting](https://developers.openai.com/codex/prompting) isn't required to get value, but it does make results more reliable, especially in larger codebases or higher-stakes tasks.
+
+If you work in a large or complex repository, the biggest unlock is giving Codex the right task context and a clear structure for what you want done.
+
+A good default is to include four things in your prompt:
+
+- **Goal:** What are you trying to change or build?
+- **Context:** Which files, folders, docs, examples, or errors matter for this task? You can @ mention certain files as context.
+- **Constraints:** What standards, architecture, safety requirements, or conventions should Codex follow?
+- **Done when:** What should be true before the task is complete, such as tests passing, behavior changing, or a bug no longer reproducing?
+
+This helps Codex stay scoped, make fewer assumptions, and produce work that's easier to review.
+
+Choose a reasoning level based on how hard the task is and test what works best for your workflow. Different users and tasks work best with different settings.
+
+- Low for faster, well-scoped tasks
+- Medium or High for more complex changes or debugging
+- Extra High for long, agentic, reasoning-heavy tasks
+
+To provide context faster, try using speech dictation inside the Codex app to
+  dictate what you want Codex to do rather than typing it.
+
+## Plan first for difficult tasks
+
+If the task is complex, ambiguous, or hard to describe well, ask Codex to plan before it starts coding.
+
+A few approaches work well:
+
+**Use Plan mode:** For most users, this is the easiest and most effective option. Plan mode lets Codex gather context, ask clarifying questions, and build a stronger plan before implementation. Toggle with `/plan` or <kbd>Shift</kbd>+<kbd>Tab</kbd>.
+
+**Ask Codex to interview you:** If you have a rough idea of what you want but aren't sure how to describe it well, ask Codex to question you first. Tell it to challenge your assumptions and turn the fuzzy idea into something concrete before writing code.
+
+**Use a PLANS.md template:** For more advanced workflows, you can configure Codex to follow a `PLANS.md` or execution-plan template for longer-running or multi-step work. For more detail, see the [execution plans guide](https://developers.openai.com/cookbook/articles/codex_exec_plans).
+
+## Make guidance reusable with `AGENTS.md`
+
+Once a prompting pattern works, the next step is to stop repeating it manually. That's where [AGENTS.md](https://developers.openai.com/codex/guides/agents-md) comes in.
+
+Think of `AGENTS.md` as an open-format README for agents. It loads into context automatically and is the best place to encode how you and your team want Codex to work in a repository.
+
+A good `AGENTS.md` covers:
+
+- repo layout and important directories
+- How to run the project
+- Build, test, and lint commands
+- Engineering conventions and PR expectations
+- Constraints and do-not rules
+- What done means and how to verify work
+
+The `/init` slash command in the CLI is the quick-start command to scaffold a starter `AGENTS.md` in the current directory. It's a great starting point, but you should edit the result to match how your team actually builds, tests, reviews, and ships code.
+
+You can create `AGENTS.md` files at different levels: a global `AGENTS.md` for personal defaults that sits in `~/.codex`, a repo-level file for shared standards, and more specific files in subdirectories for local rules. If there’s a more specific file closer to your current directory, that guidance wins.
+
+Keep it practical. A short, accurate `AGENTS.md` is more useful than a long file full of vague rules. Start with the basics, then add new rules only after you notice repeated mistakes.
+
+If `AGENTS.md` starts getting too large, keep the main file concise and reference task-specific markdown files for things like planning, code review, or architecture.
+
+When Codex makes the same mistake twice, ask it for a retrospective and update
+  `AGENTS.md`. Guidance stays practical and based on real friction.
+
+## Configure Codex for consistency
+
+Configuration is one of the main ways to make Codex behave more consistently across sessions and surfaces. For example, you can set defaults for model choice, reasoning effort, sandbox mode, approval policy, profiles, and MCP setup.
+
+A good starting pattern is:
+
+- Keep personal defaults in `~/.codex/config.toml` (Settings → Configuration → Open config.toml from the Codex app)
+- Keep repo-specific behavior in `.codex/config.toml`
+- Use command-line overrides only for one-off situations (if you use the CLI)
+
+[`config.toml`](https://developers.openai.com/codex/config-basic) is where you define durable preferences such as MCP servers, profiles, multi-agent setup, and feature flags. You can edit it directly or ask Codex to update it for you.
+
+Codex ships with operating level sandboxing and has two key knobs that you can control. Approval mode determines when Codex asks for your permission to run a command and sandbox mode determines if Codex can read or write in the directory and what files the agent can access.
+
+If you're new to coding agents, start with the default permissions. Keep approval and sandboxing tight by default, then loosen permissions only for trusted repos or specific workflows once the need is clear.
+
+Note that the CLI, IDE, and Codex app all share the same configuration layers. Learn more on the [sample configuration](https://developers.openai.com/codex/config-sample) page.
+
+Configure Codex for your real environment early. Many quality issues are
+  really setup issues, like the wrong working directory, missing write access,
+  wrong model defaults, or missing tools and connectors.
+
+## Improve reliability with testing and review
+
+Don't stop at asking Codex to make a change. Ask it to create tests when needed, run the relevant checks, confirm the result, and review the work before you accept it.
+
+Codex can do this loop for you, but only if it knows what “good” looks like. That guidance can come from either the prompt or `AGENTS.md`.
+
+That can include:
+
+- Writing or updating tests for the change
+- Running the right test suites
+- Checking lint, formatting, or type checks
+- Confirming the final behavior matches the request
+- Reviewing the diff for bugs, regressions, or risky patterns
+
+Toggle the diff panel in the Codex app to directly [review
+  changes](https://developers.openai.com/codex/app/review) locally. Click on a specific row to provide
+  feedback that gets fed as context to the next Codex turn.
+
+A useful option here is the slash command `/review`, which gives you a few ways to review code:
+
+- Review against a base branch for PR-style review
+- Review uncommitted changes
+- Review a commit
+- Use custom review instructions
+
+If you and your team have a `code_review.md` file and reference it from `AGENTS.md`, Codex can follow that guidance during review as well. This is a strong pattern for teams that want review behavior to stay consistent across repositories and contributors.
+
+Codex shouldn't just generate code. With the right instructions, it can also help **test it, check it, and review it**.
+
+If you use GitHub Cloud, you can set up Codex to run [code reviews for your PRs](https://developers.openai.com/codex/integrations/github). At OpenAI, Codex reviews 100% of PRs. You can enable automatic reviews or have Codex reactively review when you @Codex.
+
+## Use MCPs for external context
+
+Use MCPs when the context Codex needs lives outside the repo. It lets Codex connect to the tools and systems you already use, so you don't have to keep copying and pasting live information into prompts.
+
+[Model Context Protocol](https://developers.openai.com/codex/mcp), or MCP, is an open standard for connecting Codex to external tools and systems.
+
+Use MCP when:
+
+- The needed context lives outside the repo
+- The data changes frequently
+- You want Codex to use a tool rather than rely on pasted instructions
+- You need a repeatable integration across users or projects
+
+Codex supports both STDIO and Streamable HTTP servers with OAuth.
+
+In the Codex App, head to Settings → MCP servers to see custom and recommended servers. Often, Codex can help you install the needed servers. All you need to do is ask. You can also use the `codex mcp add` command in the CLI to add your custom servers with a name, URL, and other details.
+
+Add tools only when they unlock a real workflow. Do not start by wiring in
+  every tool you use. Start with one or two tools that clearly remove a manual
+  loop you already do often, then expand from there.
+
+## Turn repeatable work into skills
+
+Once a workflow becomes repeatable, stop relying on long prompts or repeated back-and-forth. Use a [Skill](https://developers.openai.com/codex/skills) to package the instructions in a SKILL.md file, context, and supporting logic Codex should apply consistently. Skills work across the CLI, IDE extension, and Codex app.
+
+Keep each skill scoped to one job. Start with 2 to 3 concrete use cases, define clear inputs and outputs, and write the description so it says what the skill does and when to use it. Include the kinds of trigger phrases a user would actually say.
+
+Don't try to cover every edge case up front. Start with one representative task, get it working well, then turn that workflow into a skill and improve from there. Include scripts or extra assets only when they improve reliability.
+
+A good rule of thumb: if you keep reusing the same prompt or correcting the same workflow, it should probably become a skill.
+
+Skills are especially useful for recurring jobs like:
+
+- Log triage
+- Release note drafting
+- PR review against a checklist
+- Migration planning
+- Telemetry or incident summaries
+- Standard debugging flows
+
+The `$skill-creator` skill is the best place to start to scaffold the first version of a skill. Keep the first version local while you iterate. When it's ready to share broadly, package it as a [plugin](https://developers.openai.com/codex/plugins/build). One of the most important parts of a skill is the description. It should say what the skill does and when to use it.
+
+Personal skills are stored in `$HOME/.agents/skills`, and shared team skills
+  can be checked into `.agents/skills` inside a repository. This is especially
+  helpful for onboarding new teammates.
+
+## Use automations for repeated work
+
+Once a workflow is stable, you can schedule Codex to run it in the background for you. In the Codex app, [automations](https://developers.openai.com/codex/app/automations) let you choose the project, prompt, cadence, and execution environment for a recurring task.
+
+Once a task becomes repetitive for you, you can create an automation in the Automations tab on the Codex app. You can choose which project it runs in, the prompt it runs (you can invoke skills), and the cadence it will run. You can also choose whether the automation runs in a dedicated git worktree or in your local environment. Learn more about [git worktrees](https://developers.openai.com/codex/app/worktrees).
+
+Good candidates include:
+
+- Summarizing recent commits
+- Scanning for likely bugs
+- Drafting release notes
+- Checking CI failures
+- Producing standup summaries
+- Running repeatable analysis workflows on a schedule
+
+A useful rule is that skills define the method, automations define the schedule. If a workflow still needs a lot of steering, turn it into a skill first. Once it's predictable, automation becomes a force multiplier.
+
+Use automations for reflection and maintenance, not just execution. Review
+  recent sessions, summarize repeated friction, and improve prompts,
+  instructions, or workflow setup over time.
+
+## Organize long-running work with session controls
+
+Codex sessions aren't just chat history. They're working threads that accumulate context, decisions, and actions over time, so managing them well has a big impact on quality.
+
+The Codex app UI makes thread management easiest because you can pin threads and create worktrees. If you are using the CLI, these [slash commands](https://developers.openai.com/codex/cli/slash-commands) are especially useful:
+
+- `/experimental` to toggle experimental features and add to your `config.toml`
+- `/resume` to resume a saved conversation
+- `/fork` to create a new thread while preserving the original transcript
+- `/compact` when the thread is getting long and you want a summarized version of earlier context. Note that Codex does automatically compact conversations for you
+- `/agent` when you are running parallel agents and want to switch between the active agent thread
+- `/theme` to choose a syntax highlighting theme
+- `/apps` to use ChatGPT apps directly in Codex
+- `/status` to inspect the current session state
+
+Keep one thread per coherent unit of work. If the work is still part of the same problem, staying in the same thread is often better because it preserves the reasoning trail. Fork only when the work truly branches.
+
+Use Codex’s [subagent](https://developers.openai.com/codex/concepts/subagents) workflows to offload bounded
+  work from the main thread. Keep the main agent focused on the core problem,
+  and use subagents for tasks like exploration, tests, or triage.
+
+## Common mistakes
+
+A few common mistakes to avoid when first using Codex:
+
+- Overloading the prompt with durable rules instead of moving them into `AGENTS.md` or a skill
+- Not letting the agent see its work by not giving details on how to best run build and test commands
+- Skipping planning on multi-step and complex tasks
+- Giving Codex full permission to your computer before you understand the workflow
+- Running live threads on the same files without using git worktrees
+- Turning a recurring task into an automation before it's reliable manually
+- Treating Codex like something you have to watch step by step instead of using it in parallel with your own work
+- Using one thread per project instead of one thread per task. This leads to bloated context and worse results over time
+
+---
+
 # Model Context Protocol
 
 Model Context Protocol (MCP) connects models to tools and context. Use it to give Codex access to third-party documentation, or to let it interact with developer tools like your browser or Figma.
@@ -9859,6 +13457,18 @@
 - `env` (optional): Environment variables to set for the server.
 - `env_vars` (optional): Environment variables to allow and forward.
 - `cwd` (optional): Working directory to start the server from.
+- `experimental_environment` (optional): Set to `remote` to start the stdio
+  server through a remote executor environment when one is available.
+
+`env_vars` can contain plain variable names or objects with a source:
+
+```toml
+env_vars = ["LOCAL_TOKEN", { name = "REMOTE_TOKEN", source = "remote" }]
+```
+
+String entries and `source = "local"` read from Codex's local environment.
+`source = "remote"` reads from the remote executor environment and requires
+remote MCP stdio.
 
 #### Streamable HTTP servers
 
@@ -9878,7 +13488,11 @@
 
 If your OAuth provider requires a fixed callback port, set the top-level `mcp_oauth_callback_port` in `config.toml`. If unset, Codex binds to an ephemeral port.
 
-If your MCP OAuth flow must use a specific callback URL (for example, a remote devbox ingress URL or a custom callback path), set `mcp_oauth_callback_url`. Codex uses this value as the OAuth `redirect_uri` while still using `mcp_oauth_callback_port` for the callback listener port. Local callback URLs (for example `localhost`) bind on loopback; non-local callback URLs bind on `0.0.0.0` so the callback can reach the host.
+If your MCP OAuth flow must use a specific callback URL (for example, a remote Devbox ingress URL or a custom callback path), set `mcp_oauth_callback_url`. Codex uses this value as the OAuth `redirect_uri` while still using `mcp_oauth_callback_port` for the callback listener port. Local callback URLs (for example `localhost`) bind on the local interface; non-local callback URLs bind on `0.0.0.0` so the callback can reach the host.
+
+If the MCP server advertises `scopes_supported`, Codex prefers those
+server-advertised scopes during OAuth login. Otherwise, Codex falls back to the
+scopes configured in `config.toml`.
 
 #### config.toml examples
 
@@ -9886,6 +13500,7 @@
 [mcp_servers.context7]
 command = "npx"
 args = ["-y", "@upstash/context7-mcp"]
+env_vars = ["LOCAL_TOKEN"]
 
 [mcp_servers.context7.env]
 MY_ENV_VAR = "MY_ENV_VALUE"
@@ -9918,7 +13533,7 @@
 
 The list of MCP servers keeps growing. Here are a few common ones:
 
-- [OpenAI Docs MCP](https://developers.openai.com/resources/docs-mcp): Search and read OpenAI developer docs.
+- [OpenAI Docs MCP](https://developers.openai.com/learn/docs-mcp): Search and read OpenAI developer docs.
 - [Context7](https://github.com/upstash/context7): Connect to up-to-date developer documentation.
 - Figma [Local](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/) and [Remote](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/): Access your Figma designs.
 - [Playwright](https://www.npmjs.com/package/@playwright/mcp): Control and inspect a browser using Playwright.
@@ -9928,6 +13543,381 @@
 
 ---
 
+# Memories
+
+Memories are off by default and aren't available in the European Economic
+  Area, the United Kingdom, or Switzerland at launch. Enable them in Codex
+  settings, or set `memories = true` in the `[features]` table in
+  `~/.codex/config.toml`.
+
+Memories let Codex carry useful context from earlier threads into future work.
+After you enable memories, Codex can remember stable preferences, recurring
+workflows, tech stacks, project conventions, and known pitfalls so you don't
+need to repeat the same context in every thread.
+
+Keep required team guidance in `AGENTS.md` or checked-in documentation. Treat
+memories as a helpful local recall layer, not as the only source for rules that
+must always apply.
+
+[Chronicle](https://developers.openai.com/codex/memories/chronicle) helps Codex recover recent working
+context from your screen to build up memory.
+
+## Enable memories
+
+In the Codex app, enable Memories in settings.
+
+For config-based setup, add the feature flag to `config.toml`:
+
+```toml
+[features]
+memories = true
+```
+
+See [Config basics](https://developers.openai.com/codex/config-basic) for where Codex stores user-level
+configuration and how Codex loads `~/.codex/config.toml`.
+
+## How memories work
+
+After you enable memories, Codex can turn useful context from eligible prior
+threads into local memory files. Codex skips active or short-lived sessions,
+redacts secrets from generated memory fields, and updates memories in the
+background instead of immediately at the end of every thread.
+
+Memories may not update right away when a thread ends. Codex waits until a
+thread has been idle long enough to avoid summarizing work that's still in
+progress.
+
+Memory generation can also skip a background pass when your Codex rate-limit
+remaining percentage is below the configured threshold, so Codex doesn't spend
+quota when you're near a limit.
+
+## Memory storage
+
+Codex stores memories under your Codex home directory. By default, that's
+`~/.codex`. See [Config and state locations](https://developers.openai.com/codex/config-advanced#config-and-state-locations)
+for how Codex uses `CODEX_HOME`.
+
+The main memory files live under `~/.codex/memories/` and include summaries,
+durable entries, recent inputs, and supporting evidence from prior threads.
+
+Treat these files as generated state. You can inspect them when troubleshooting
+or before sharing your Codex home directory, but don't rely on editing them by
+hand as your primary control surface.
+
+## Control memories per thread
+
+In the Codex app and Codex TUI, use `/memories` to control memory behavior for
+the current thread. Thread-level choices let you decide whether the current
+thread can use existing memories and whether Codex can use the thread to
+generate future memories.
+
+Thread-level choices don't change your global memory settings.
+
+## Configuration
+
+Enable memories in the Codex app settings, or set `memories = true` in the
+`[features]` section of `config.toml`.
+
+For config file locations and the full list of memory-related settings, see the
+[configuration reference](https://developers.openai.com/codex/config-reference).
+
+Common memory-specific settings include:
+
+- `memories.generate_memories`: controls whether newly created threads can be
+  stored as memory-generation inputs.
+- `memories.use_memories`: controls whether Codex injects existing memories into
+  future sessions.
+- `memories.disable_on_external_context`: when `true`, keeps threads that used
+  external context such as MCP tool calls, web search, or tool search out of
+  memory generation. The older `memories.no_memories_if_mcp_or_web_search` key
+  is still accepted as an alias.
+- `memories.min_rate_limit_remaining_percent`: controls the minimum remaining
+  Codex rate-limit percentage required before memory generation starts.
+- `memories.extract_model`: overrides the model used for per-thread memory
+  extraction.
+- `memories.consolidation_model`: overrides the model used for global memory
+  consolidation.
+
+## Review memories
+
+Don't store secrets in memories. Codex redacts secrets from generated memory
+fields, but you should still review memory files before sharing your Codex home
+directory or generated memory artifacts.
+
+---
+
+# Chronicle
+
+Chronicle is in an **opt-in research preview**. It is only available for
+  ChatGPT Pro subscribers on macOS, and is not yet available in the EU, UK and
+  Switzerland. Please review the [Privacy and Security](#privacy-and-security)
+  section for details and to understand the current risks before enabling.
+
+Chronicle augments Codex memories with context from your screen. When you prompt
+Codex, those memories can help it understand what you’ve been working on with
+less need for you to restate context.
+
+Chronicle is available as an opt-in research preview in the Codex app on macOS.
+It requires macOS Screen Recording and Accessibility permissions. Before
+enabling, be aware that Chronicle uses rate limits quickly, increases risk of
+prompt injection, and stores memories unencrypted on your device.
+
+## How Chronicle helps
+
+We’ve designed Chronicle to reduce the amount of context you have to restate
+when you work with Codex. By using recent screen context to improve memory
+building, Chronicle can help Codex understand what you’re referring to, identify
+the right source to use, and pick up on the tools and workflows you rely on.
+
+<section class="feature-grid mt-4">
+
+<div>
+
+### Use what’s on screen
+
+With Chronicle Codex can understand what you are currently looking at, saving
+you time and context switching.
+
+</div>
+
+</section>
+
+<section class="feature-grid inverse">
+
+<div>
+
+### Fill in missing context
+
+No need to carefully craft your context and start from zero. Chronicle lets
+Codex fill in the gaps in your context.
+
+</div>
+
+</section>
+
+<section class="feature-grid">
+
+<div>
+
+### Remember tools and workflows
+
+No need to explain to Codex which tools to use to perform your work. Codex
+learns as you work to save you time in the long run.
+
+</div>
+
+</section>
+
+In these cases, Codex uses Chronicle to provide additional context. When another
+source is better for the job, such as reading the specific file, Slack thread,
+Google Doc, dashboard, or pull request, Codex uses Chronicle to identify the
+source and then use that source directly.
+
+## Enable Chronicle
+
+1. Open Settings in the Codex app.
+2. Go to **Personalization** and make sure **Memories** is enabled.
+3. Turn on **Chronicle** below the Memories setting.
+4. Review the consent dialog and choose **Continue**.
+5. Grant macOS Screen Recording and Accessibility permissions when prompted.
+6. When setup completes, choose **Try it out** or start a new thread.
+
+If macOS reports that Screen Recording or Accessibility permission is denied,
+open System Settings &gt; Privacy & Security &gt; Screen Recording or
+Accessibility and enable Codex. If a permission is restricted by macOS or your
+organization, Chronicle will start after the restriction is removed and Codex
+receives the required permission.
+
+## Pause or disable Chronicle at any time
+
+You control when Chronicle generates memories using screen context. Use the
+Codex menu bar icon to choose **Pause Chronicle** or **Resume Chronicle**. Pause
+Chronicle before meetings or when viewing sensitive content that you do not want
+Codex to use as context. To disable Chronicle, return to **Settings &gt;
+Personalization &gt; Memories** and turn off **Chronicle**.
+
+You can also control whether memories are used in a given thread. [Learn
+more](https://developers.openai.com/codex/memories#control-memories-per-thread).
+
+## Rate limits
+
+Chronicle works by running sandboxed agents in the background to generate
+memories from captured screen images. These agents currently consume rate limits
+quickly.
+
+## Privacy and security
+
+Chronicle uses screen captures, which can include sensitive information visible
+on your screen. It does not have access to your microphone or system audio.
+Don’t use Chronicle to record meetings or communications with others without
+their consent. Pause Chronicle when viewing content you do not want remembered
+in memories.
+
+### Where does Chronicle store my data?
+
+Screen captures are ephemeral and will only be saved temporarily on your
+computer. Temporary screen capture files may appear under
+`$TMPDIR/chronicle/screen_recording/` while Chronicle is running. Screen captures
+that are older than 6 hours will be deleted while Chronicle is running.
+
+The memories that Chronicle generates are just like other Codex memories:
+unencrypted markdown files that you can read and modify if needed. You can also
+ask Codex to search them. If you want to have Codex forget something you can
+delete the respective file inside the folder or selectively edit the markdown
+files to remove the information you’d like to remove. You should not manually
+add new information. The generated Chronicle memories are stored locally on your
+computer under `$CODEX_HOME/memories_extensions/chronicle/` (typically
+`~/.codex/memories_extensions/chronicle`).
+
+<div className="not-prose my-4">
+  </div>
+
+### What data gets shared with OpenAI?
+
+Chronicle captures screen context locally, then periodically uses Codex to
+summarize recent activity into memories. To generate those memories, Chronicle
+starts an ephemeral Codex session with access to this screen context. That
+session may process selected screenshot frames, OCR text extracted from
+screenshots, timing information, and local file paths for the relevant time
+window.
+
+Screen captures used for memory generation are stored temporarily on your device. They are processed on our
+servers to generate memories, which are then stored locally on device. We do not
+store the screenshots on our servers after processing unless required by law,
+and do not use them for training.
+
+The generated memories are Markdown files stored locally under
+`$CODEX_HOME/memories_extensions/chronicle/`. When Codex uses memories in a
+future session, relevant memory contents may be included as context for that
+session, and may be used to improve our models if allowed in your ChatGPT
+settings. [Learn more](https://help.openai.com/en/articles/7730893-data-controls-faq).
+
+## Prompt injection risk
+
+Using Chronicle increases risk to prompt injection attacks from screen content.
+For instance, if you browse a site with malicious agent instructions, Codex may
+follow those instructions.
+
+## Troubleshooting
+
+### How do I enable Chronicle?
+
+If you do not see the Chronicle setting, make sure you are using a Codex app
+build that includes Chronicle and that you have Memories enabled inside Settings
+&gt; Personalization.
+
+Chronicle is currently only available for ChatGPT Pro subscribers on macOS.
+Chronicle is not available in the EU, UK and Switzerland.
+
+If setup does not complete:
+
+1. Confirm that Codex has Screen Recording and Accessibility permissions.
+2. Quit and reopen the Codex app.
+3. Open **Settings > Personalization** and check the Chronicle status.
+
+### Which model is used for generating the Chronicle memories?
+
+Chronicle uses the same model as your other [Memories](https://developers.openai.com/codex/memories). If you
+did not configure a specific model it uses your default Codex model. To choose a
+specific model, update the `consolidation_model` in your
+[configuration](https://developers.openai.com/codex/config-basic).
+
+```toml
+[memories]
+consolidation_model = "gpt-5.4-mini"
+```
+
+---
+
+# Migrate to Codex
+
+Use the import flow to bring your instructions, configuration, skills, MCP
+servers, hooks, subagents, and recent sessions from another agent into Codex.
+Codex migrates the parts it can handle directly and can open a follow-up thread
+to help migrate anything that remains.
+
+<div class="not-prose my-6 max-w-4xl">
+  </div>
+
+## Start the migration
+
+
+
+1. Open **Settings** in the Codex app.
+2. On the **General** page, find **Import other agent setup**.
+3. Select **Import** or **Import again**.
+4. Review what Codex found, choose what to bring over, then select **Import**.
+5. After the import finishes, select **View imported files** if you want to inspect the result.
+
+
+
+## How migration works
+
+Codex checks both your user-level setup and the current project. User-level
+setup comes from files on your machine; project-level setup comes from files in
+the repository you have open.
+
+When you import, Codex:
+
+1. Detects the setup it can find.
+2. Imports the selected items it can migrate directly.
+3. Checks again after the import finishes.
+4. Offers to continue the migration in a new thread if anything still needs
+   follow-up work.
+
+## What Codex can import
+
+| Detected setup                        | Codex destination                      |
+| ------------------------------------- | -------------------------------------- |
+| Instruction files                     | [`AGENTS.md`](https://developers.openai.com/codex/guides/agents-md) |
+| `settings.json`                       | [`config.toml`](https://developers.openai.com/codex/config-basic)   |
+| Skills                                | [Codex skills](https://developers.openai.com/codex/skills)          |
+| Recent sessions from the last 30 days | Codex threads and projects             |
+| MCP server configuration              | [Codex MCP configuration](https://developers.openai.com/codex/mcp)  |
+| Hooks                                 | [Codex hooks](https://developers.openai.com/codex/hooks)            |
+| Slash commands                        | [Codex skills](https://developers.openai.com/codex/skills)          |
+| Subagents                             | [Codex agents](https://developers.openai.com/codex/subagents)       |
+
+## Finish remaining setup in a new thread
+
+Some detected setup does not have a clean one-to-one mapping into Codex. For
+those items, Codex can open a new thread with the
+[`migrate-to-codex`](https://github.com/openai/skills/tree/main/skills/.curated/migrate-to-codex)
+skill to help finish the migration.
+
+When that happens, Codex shows the remaining setup and offers **Continue in
+Codex**.
+
+<div class="not-prose my-6 max-w-4xl">
+  </div>
+
+If you continue, Codex opens a new thread with the remaining work already filled
+in. The thread keeps user-level setup separate from project-level setup so you
+can see where each remaining item belongs.
+
+<div class="not-prose my-6 max-w-4xl">
+  </div>
+
+## What to review after import
+
+Review any migrated setup before you rely on it, especially:
+
+- Tool restrictions or permissions in imported skills and agents.
+- MCP server settings that use custom authentication, headers, environment
+  variables, or transports.
+- Hooks whose behavior may differ in Codex.
+- Plugins, marketplaces, or other remaining setup that needs manual follow-up.
+- Prompt templates or command-style prompts that depend on arguments, shell
+  interpolation, or file-path placeholders.
+
+## After you switch
+
+Once the import finishes, open one of your migrated projects and continue from
+there. If you are new to Codex, see the [quickstart](https://developers.openai.com/codex/quickstart) for the
+rest of the setup flow.
+
+---
+
 # Codex Models
 
 ## Recommended models
@@ -9935,11 +13925,15 @@
 <div class="not-prose grid gap-6 md:grid-cols-2 xl:grid-cols-3">
   </div>
 
-For most tasks in Codex, start with `gpt-5.4`. It combines strong coding,
-  reasoning, native computer use, and broader professional workflows in one
-  model. The `gpt-5.3-codex-spark` model is available in research preview for
-  ChatGPT Pro subscribers and is optimized for near-instant, real-time coding
-  iteration.
+For most tasks in Codex, start with `gpt-5.5` when it appears in your model
+  picker. It is strongest for complex coding, computer use, knowledge work, and
+  research workflows. GPT-5.5 is currently available in Codex when you sign in
+  with ChatGPT; it isn't available with API-key authentication. During the
+  rollout, continue using `gpt-5.4` if `gpt-5.5` is not yet available. Use
+  `gpt-5.4-mini` when you want a faster, lower-cost option for lighter coding
+  tasks or subagents. The `gpt-5.3-codex-spark` model is available in research
+  preview for ChatGPT Pro subscribers and is optimized for near-instant,
+  real-time coding iteration.
 
 ## Alternative models
 
@@ -9948,7 +13942,7 @@
 
 ## Other models
 
-Codex works best with the models listed above.
+When you sign in with ChatGPT, Codex works best with the models listed above.
 
 You can also point Codex at any model and provider that supports either the [Chat Completions](https://platform.openai.com/docs/api-reference/chat) or [Responses APIs](https://platform.openai.com/docs/api-reference/responses) to fit your specific use case.
 
@@ -9962,8 +13956,10 @@
 The Codex CLI and IDE extension use the same `config.toml` [configuration file](https://developers.openai.com/codex/config-basic). To specify a model, add a `model` entry to your configuration file. If you don't specify a model, the Codex app, CLI, or IDE Extension defaults to a recommended model.
 
 ```toml
-model = "gpt-5.4"
-```
+model = "gpt-5.5"
+```
+
+If `gpt-5.5` isn't available in your account yet, use `gpt-5.4`.
 
 ### Choosing a different local model temporarily
 
@@ -9972,326 +13968,12 @@
 To start a new Codex CLI thread with a specific model or to specify the model for `codex exec` you can use the `--model`/`-m` flag:
 
 ```bash
-codex -m gpt-5.4
+codex -m gpt-5.5
 ```
 
 ### Choosing your model for cloud tasks
 
 Currently, you can't change the default model for Codex cloud tasks.
-
----
-
-# Multi-agents
-
-Codex can run multi-agent workflows by spawning specialized agents in parallel and then collecting their results in one response. This can be particularly helpful for complex tasks that are highly parallel, such as codebase exploration or implementing a multi-step feature plan.
-
-With multi-agent workflows you can also define your own set of agents with different model configurations and instructions depending on the agent.
-
-For the concepts and tradeoffs behind multi-agent workflows (including context pollution/context rot and model-selection guidance), see [Multi-agents concepts](https://developers.openai.com/codex/concepts/multi-agents).
-
-## Enable multi-agent
-
-Multi-agent workflows are currently experimental and need to be explicitly enabled.
-
-You can enable this feature from the CLI with `/experimental`. Enable
-**Multi-agents**, then restart Codex.
-
-Multi-agent activity is currently surfaced in the CLI. Visibility in other
-  surfaces (the Codex app and IDE Extension) is coming soon.
-
-You can also add the [`multi_agent` feature flag](https://developers.openai.com/codex/config-basic#feature-flags) directly to your configuration file (`~/.codex/config.toml`):
-
-```toml
-[features]
-multi_agent = true
-```
-
-## Typical workflow
-
-Codex handles orchestration across agents, including spawning new sub-agents, routing follow-up instructions, waiting for results, and closing agent threads.
-
-When many agents are running, Codex waits until all requested results are available, then returns a consolidated response.
-
-Codex will automatically decide when to spawn a new agent or you can explicitly ask it to do so.
-
-For long-running commands or polling workflows, Codex can also use the built-in `monitor` role, which is tuned for waiting and repeated status checks.
-
-To see it in action, try the following prompt on your project:
-
-```text
-I would like to review the following points on the current PR (this branch vs main). Spawn one agent per point, wait for all of them, and summarize the result for each point.
-1. Security issue
-2. Code quality
-3. Bugs
-4. Race
-5. Test flakiness
-6. Maintainability of the code
-```
-
-## Managing sub-agents
-
-- Use `/agent` in the CLI to switch between active agent threads and inspect the ongoing thread.
-- Ask Codex directly to steer a running sub-agent, stop it, or close completed agent threads.
-- The `wait` tool supports long polling windows for monitoring workflows (up to 1 hour per call).
-
-## Process CSV batches with sub-agents
-
-Use `spawn_agents_on_csv` when you have many similar tasks that can be expressed as one row per work item. Codex reads the CSV, spawns one worker sub-agent per row, waits for the full batch to finish, and exports the combined results to CSV.
-
-This works well for repeated audits such as:
-
-- reviewing one file, package, or service per row
-- checking a list of incidents, PRs, or migration targets
-- generating structured summaries for many similar inputs
-
-The tool accepts:
-
-- `csv_path` for the source CSV
-- `instruction` for the worker prompt template, using `{column_name}` placeholders
-- `id_column` when you want stable item ids from a specific column
-- `output_schema` when each worker should return a JSON object with a fixed shape
-- `output_csv_path`, `max_concurrency`, and `max_runtime_seconds` for job control
-
-Each worker must call `report_agent_job_result` exactly once. If a worker exits without reporting a result, that row is marked as failed in the exported CSV.
-
-Example prompt:
-
-```text
-Create /tmp/components.csv with columns path,owner and one row per frontend component.
-
-Then call spawn_agents_on_csv with:
-- csv_path: /tmp/components.csv
-- id_column: path
-- instruction: "Review {path} owned by {owner}. Return JSON with keys path, risk, summary, and follow_up via report_agent_job_result."
-- output_csv_path: /tmp/components-review.csv
-- output_schema: an object with required string fields path, risk, summary, and follow_up
-```
-
-When you run this through `codex exec`, Codex shows a single-line progress update on `stderr` while the batch is running. The exported CSV includes the original row data plus metadata such as `job_id`, `item_id`, `status`, `last_error`, and `result_json`.
-
-Related runtime settings:
-
-- `agents.max_threads` caps how many agent threads can stay open concurrently.
-- `agents.job_max_runtime_seconds` sets the default per-worker timeout for CSV fan-out jobs. A per-call `max_runtime_seconds` override takes precedence.
-- `sqlite_home` controls where Codex stores the SQLite-backed state used for agent jobs and their exported results.
-
-## Approvals and sandbox controls
-
-Sub-agents inherit your current sandbox policy.
-
-In interactive CLI sessions, approval requests can surface from inactive agent
-threads even while you are looking at the main thread. The approval overlay
-shows the source thread label, and you can press `o` to open that thread before
-you approve, reject, or answer the request.
-
-In non-interactive flows, or whenever a run cannot surface a fresh approval,
-an action that needs new approval fails and the error is surfaced back to the
-parent workflow.
-
-Codex also reapplies the parent turn's live runtime overrides when it spawns a
-child. That includes sandbox and approval choices you set interactively during
-the session, such as `/approvals` changes or `--yolo`, even if the selected
-agent role loads a config file with different defaults.
-
-You can also override the sandbox configuration for individual [agent roles](#agent-roles) such as explicitly marking an agent to work in read-only mode.
-
-## Agent roles
-
-You configure agent roles in the `[agents]` section of your [configuration](https://developers.openai.com/codex/config-basic#configuration-precedence).
-
-Agent roles can be defined either in your local configuration (typically `~/.codex/config.toml`) or shared in a project-specific `.codex/config.toml`.
-
-Each role can provide guidance (`description`) for when Codex should use this agent, and optionally load a
-role-specific config file (`config_file`) when Codex spawns an agent with that role.
-
-Codex ships with built-in roles:
-
-- `default`: general-purpose fallback role.
-- `worker`: execution-focused role for implementation and fixes.
-- `explorer`: read-heavy codebase exploration role.
-- `monitor`: long-running command/task monitoring role (optimized for waiting/polling).
-
-Each agent role can override your default configuration. Common settings to override for an agent role are:
-
-- `model` and `model_reasoning_effort` to select a specific model for your agent role
-- `sandbox_mode` to mark an agent as `read-only`
-- `developer_instructions` to give the agent role additional instructions without relying on the parent agent for passing them
-
-### Schema
-
-| Field                            | Type          | Required | Purpose                                                                       |
-| -------------------------------- | ------------- | :------: | ----------------------------------------------------------------------------- |
-| `agents.max_threads`             | number        |    No    | Maximum number of concurrently open agent threads.                            |
-| `agents.max_depth`               | number        |    No    | Maximum nesting depth for spawned agent threads (root session starts at 0).   |
-| `agents.job_max_runtime_seconds` | number        |    No    | Default timeout per worker for `spawn_agents_on_csv` jobs.                    |
-| `[agents.<name>]`                | table         |    No    | Declares a role. `<name>` is used as the `agent_type` when spawning an agent. |
-| `agents.<name>.description`      | string        |    No    | Human-facing role guidance shown to Codex when it decides which role to use.  |
-| `agents.<name>.config_file`      | string (path) |    No    | Path to a TOML config layer applied to spawned agents for that role.          |
-
-**Notes:**
-
-- Unknown fields in `[agents.<name>]` are rejected.
-- `agents.max_depth` defaults to `1`, which allows a direct child agent to spawn but prevents deeper nesting.
-- `agents.job_max_runtime_seconds` is optional. When you leave it unset, `spawn_agents_on_csv` falls back to its per-call default timeout of 1800 seconds per worker.
-- Relative `config_file` paths are resolved relative to the `config.toml` file that defines the role.
-- `agents.<name>.config_file` is validated at config load time and must point to an existing file.
-- If a role name matches a built-in role (for example, `explorer`), your user-defined role takes precedence.
-- If Codex can't load a role config file, agent spawns can fail until you fix the file.
-- Any configuration not set by the agent role will be inherited from the parent session.
-
-### Example agent roles
-
-The best role definitions are narrow and opinionated. Give each role one clear job, a tool surface that matches that job, and instructions that keep it from drifting into adjacent work.
-
-#### Example 1: PR review team
-
-This pattern splits review into three focused roles:
-
-- `explorer` maps the codebase and gathers evidence.
-- `reviewer` looks for correctness, security, and test risks.
-- `docs_researcher` checks framework or API documentation through a dedicated MCP server.
-
-Project config (`.codex/config.toml`):
-
-```toml
-[agents]
-max_threads = 6
-max_depth = 1
-
-[agents.explorer]
-description = "Read-only codebase explorer for gathering evidence before changes are proposed."
-config_file = "agents/explorer.toml"
-
-[agents.reviewer]
-description = "PR reviewer focused on correctness, security, and missing tests."
-config_file = "agents/reviewer.toml"
-
-[agents.docs_researcher]
-description = "Documentation specialist that uses the docs MCP server to verify APIs and framework behavior."
-config_file = "agents/docs-researcher.toml"
-```
-
-`agents/explorer.toml`:
-
-```toml
-model = "gpt-5.3-codex-spark"
-model_reasoning_effort = "medium"
-sandbox_mode = "read-only"
-developer_instructions = """
-Stay in exploration mode.
-Trace the real execution path, cite files and symbols, and avoid proposing fixes unless the parent agent asks for them.
-Prefer fast search and targeted file reads over broad scans.
-"""
-```
-
-`agents/reviewer.toml`:
-
-```toml
-model = "gpt-5.3-codex"
-model_reasoning_effort = "high"
-sandbox_mode = "read-only"
-developer_instructions = """
-Review code like an owner.
-Prioritize correctness, security, behavior regressions, and missing test coverage.
-Lead with concrete findings, include reproduction steps when possible, and avoid style-only comments unless they hide a real bug.
-"""
-```
-
-`agents/docs-researcher.toml`:
-
-```toml
-model = "gpt-5.3-codex-spark"
-model_reasoning_effort = "medium"
-sandbox_mode = "read-only"
-developer_instructions = """
-Use the docs MCP server to confirm APIs, options, and version-specific behavior.
-Return concise answers with links or exact references when available.
-Do not make code changes.
-"""
-
-[mcp_servers.openaiDeveloperDocs]
-url = "https://developers.openai.com/mcp"
-```
-
-This setup works well for prompts like:
-
-```text
-Review this branch against main. Have explorer map the affected code paths, reviewer find real risks, and docs_researcher verify the framework APIs that the patch relies on.
-```
-
-#### Example 2: frontend integration debugging team
-
-This pattern is useful for UI regressions, flaky browser flows, or integration bugs that cross application code and the running product.
-
-Project config (`.codex/config.toml`):
-
-```toml
-[agents]
-max_threads = 6
-max_depth = 1
-
-[agents.explorer]
-description = "Read-only codebase explorer for locating the relevant frontend and backend code paths."
-config_file = "agents/explorer.toml"
-
-[agents.browser_debugger]
-description = "UI debugger that uses browser tooling to reproduce issues and capture evidence."
-config_file = "agents/browser-debugger.toml"
-
-[agents.worker]
-description = "Implementation-focused agent for small, targeted fixes after the issue is understood."
-config_file = "agents/worker.toml"
-```
-
-`agents/explorer.toml`:
-
-```toml
-model = "gpt-5.3-codex-spark"
-model_reasoning_effort = "medium"
-sandbox_mode = "read-only"
-developer_instructions = """
-Map the code that owns the failing UI flow.
-Identify entry points, state transitions, and likely files before the worker starts editing.
-"""
-```
-
-`agents/browser-debugger.toml`:
-
-```toml
-model = "gpt-5.3-codex"
-model_reasoning_effort = "high"
-sandbox_mode = "workspace-write"
-developer_instructions = """
-Reproduce the issue in the browser, capture exact steps, and report what the UI actually does.
-Use browser tooling for screenshots, console output, and network evidence.
-Do not edit application code.
-"""
-
-[mcp_servers.chrome_devtools]
-url = "http://localhost:3000/mcp"
-startup_timeout_sec = 20
-```
-
-`agents/worker.toml`:
-
-```toml
-model = "gpt-5.3-codex"
-model_reasoning_effort = "medium"
-developer_instructions = """
-Own the fix once the issue is reproduced.
-Make the smallest defensible change, keep unrelated files untouched, and validate only the behavior you changed.
-"""
-
-[[skills.config]]
-path = "/Users/me/.agents/skills/docs-editor/SKILL.md"
-enabled = false
-```
-
-This setup works well for prompts like:
-
-```text
-Investigate why the settings modal fails to save. Have browser_debugger reproduce it, explorer trace the responsible code path, and worker implement the smallest fix once the failure mode is clear.
-```
 
 ---
 
@@ -10308,6 +13990,7 @@
 
 - Run as part of a pipeline (CI, pre-merge checks, scheduled jobs).
 - Produce output you can pipe into other tools (for example, to generate release notes or summaries).
+- Fit naturally into CLI workflows that chain command output into Codex and pass Codex output to other tools.
 - Run with explicit, pre-set sandbox and approval settings.
 
 ## Basic usage
@@ -10330,14 +14013,30 @@
 codex exec --ephemeral "triage this repository and suggest next steps"
 ```
 
+If stdin is piped and you also provide a prompt argument, Codex treats the prompt as the instruction and the piped content as additional context.
+
+This makes it easy to generate input with one command and hand it directly to Codex:
+
+```bash
+curl -s https://jsonplaceholder.typicode.com/comments \
+  | codex exec "format the top 20 items into a markdown table" \
+  > table.md
+```
+
+For more advanced stdin piping patterns, see [Advanced stdin piping](#advanced-stdin-piping).
+
 ## Permissions and safety
 
 By default, `codex exec` runs in a read-only sandbox. In automation, set the least permissions needed for the workflow:
 
-- Allow edits: `codex exec --full-auto "<task>"`
+- Allow edits: `codex exec --sandbox workspace-write "<task>"`
 - Allow broader access: `codex exec --sandbox danger-full-access "<task>"`
 
 Use `danger-full-access` only in a controlled environment (for example, an isolated CI runner or container).
+
+Codex keeps `codex exec --full-auto` as a deprecated compatibility flag and prints a warning. Prefer the explicit `--sandbox workspace-write` flag in new scripts.
+
+Use `--ignore-user-config` when you need a run that doesn't load `$CODEX_HOME/config.toml`, and `--ignore-rules` when you need to skip user and project execpolicy `.rules` files for a controlled automation environment.
 
 If you configure an enabled MCP server with `required = true` and it fails to initialize, `codex exec` exits with an error instead of continuing without that server.
 
@@ -10360,7 +14059,7 @@
 {"type":"turn.started"}
 {"type":"item.started","item":{"id":"item_1","type":"command_execution","command":"bash -lc ls","status":"in_progress"}}
 {"type":"item.completed","item":{"id":"item_3","type":"agent_message","text":"Repo contains docs, sdk, and examples directories."}}
-{"type":"turn.completed","usage":{"input_tokens":24763,"cached_input_tokens":24448,"output_tokens":122}}
+{"type":"turn.completed","usage":{"input_tokens":24763,"cached_input_tokens":24448,"output_tokens":122,"reasoning_output_tokens":0}}
 ```
 
 If you only need the final message, write it to a file with `-o <path>`/`--output-last-message <path>`. This writes the final message to the file and still prints it to `stdout` (see [`codex exec`](https://developers.openai.com/codex/cli/reference#codex-exec) for details).
@@ -10516,7 +14215,7 @@
 
       - name: Run Codex
         run: |
-          codex exec --full-auto --sandbox workspace-write \
+          codex exec --sandbox workspace-write \
             "Read the repository, run the test suite, identify the minimal change needed to make all tests pass, implement only that change, and stop. Do not refactor unrelated files."
 
       - name: Verify tests
@@ -10535,13 +14234,82 @@
 
 If you want to avoid installing the CLI yourself, you can run `codex exec` through the [Codex GitHub Action](https://developers.openai.com/codex/github-action) and pass the prompt as an input.
 
+## Advanced stdin piping
+
+When another command produces input for Codex, choose the stdin pattern based on where the instruction should come from. Use prompt-plus-stdin when you already know the instruction and want to pass piped output as context. Use `codex exec -` when stdin should become the full prompt.
+
+### Use prompt-plus-stdin
+
+Prompt-plus-stdin is useful when another command already produces the data you want Codex to inspect. In this mode, you write the instruction yourself and pipe in the output as context, which makes it a natural fit for CLI workflows built around command output, logs, and generated data.
+
+```bash
+npm test 2>&1 \
+  | codex exec "summarize the failing tests and propose the smallest likely fix" \
+  | tee test-summary.md
+```
+
+
+
+### Summarize logs
+
+```bash
+tail -n 200 app.log \
+  | codex exec "identify the likely root cause, cite the most important errors, and suggest the next three debugging steps" \
+  > log-triage.md
+```
+
+### Inspect TLS or HTTP issues
+
+```bash
+curl -vv https://api.example.com/health 2>&1 \
+  | codex exec "explain the TLS or HTTP failure and suggest the most likely fix" \
+  > tls-debug.md
+```
+
+### Prepare a Slack-ready update
+
+```bash
+gh run view 123456 --log \
+  | codex exec "write a concise Slack-ready update on the CI failure, including the likely cause and next step" \
+  | pbcopy
+```
+
+### Draft a pull request comment from CI logs
+
+```bash
+gh run view 123456 --log \
+  | codex exec "summarize the failure in 5 bullets for the pull request thread" \
+  | gh pr comment 789 --body-file -
+```
+
+
+
+### Use `codex exec -` when stdin is the prompt
+
+If you omit the prompt argument, Codex reads the prompt from stdin. Use `codex exec -` when you want to force that behavior explicitly.
+
+The `-` sentinel is useful when another command or script is generating the entire prompt dynamically. This is a good fit when you store prompts in files, assemble prompts with shell scripts, or combine live command output with instructions before handing the whole prompt to Codex.
+
+```bash
+cat prompt.txt | codex exec -
+```
+
+```bash
+printf "Summarize this error log in 3 bullets:\n\n%s\n" "$(tail -n 200 app.log)" \
+  | codex exec -
+```
+
+```bash
+generate_prompt.sh | codex exec - --json > result.jsonl
+```
+
 ---
 
 # Open Source
 
 OpenAI develops key parts of Codex in the open. That work lives on GitHub so you can follow progress, report issues, and contribute improvements.
 
-If you maintain a widely used open-source project or want to nominate maintainers stewarding important projects, you can also [apply to the Codex open source program](https://developers.openai.com/codex/community/codex-for-oss) for API credits, ChatGPT Pro with Codex, and selective access to Codex Security.
+If you maintain a widely used open-source project or want to nominate maintainers stewarding important projects, you can also [apply to the Codex for OSS program](https://developers.openai.com/community/codex-for-oss) for API credits, ChatGPT Pro with Codex, and selective access to Codex Security.
 
 ## Open-source components
 
@@ -10593,120 +14361,1057 @@
 
 ---
 
+# Plugins
+
+## Overview
+
+Plugins bundle skills, app integrations, and MCP servers into reusable
+workflows for Codex.
+
+Extend what Codex can do, for example:
+
+- Install the Gmail plugin to let Codex read and manage Gmail.
+- Install the Google Drive plugin to work across Drive, Docs, Sheets, and
+  Slides.
+- Install the Slack plugin to summarize channels or draft replies.
+
+A plugin can contain:
+
+- **Skills:** reusable instructions for specific kinds of work. Codex can load
+  them when needed so it follows the right steps and uses the right references
+  or helper scripts for a task.
+- **Apps:** connections to tools like GitHub, Slack, or Google Drive, so
+  Codex can read information from those tools and take actions in them.
+- **MCP servers:** services that give Codex access to additional tools or
+  shared information, often from systems outside your local project.
+
+More plugin capabilities are coming soon.
+
+## Use and install plugins
+
+### Plugin Directory in the Codex app
+
+Open **Plugins** in the Codex app to browse and install curated plugins.
+
+### Plugin directory in the CLI
+
+In Codex CLI, run the following command to open the plugins list:
+
+```text
+codex
+/plugins
+```
+
+The CLI plugin browser groups plugins by marketplace. Use the marketplace tabs
+to switch sources, open a plugin to inspect details, install or uninstall
+marketplace entries, and press <kbd>Space</kbd> on an installed plugin to toggle
+its enabled state.
+
+### Install and use a plugin
+
+Once you open the plugin directory:
+
+
+
+1. Search or browse for a plugin, then open its details.
+2. Select the install button. In the app, select the plus button or
+   **Add to Codex**. In the CLI, select `Install plugin`.
+3. If the plugin needs an external app, connect it when prompted. Some plugins
+   ask you to authenticate during install. Others wait until the first time you
+   use them.
+4. After installation, start a new thread and ask Codex to use the plugin.
+
+
+
+After you install a plugin, you can use it directly in the prompt window:
+
+<div class="not-prose mt-4 grid gap-4 md:grid-cols-2">
+  <div class="rounded-xl border border-subtle bg-surface px-5 py-4">
+    <p class="text-sm font-semibold text-default">Describe the task directly</p>
+    <p class="mt-2 text-sm text-secondary">
+      Ask for the outcome you want, such as "Summarize unread Gmail threads
+      from today" or "Pull the latest launch notes from Google Drive."
+    </p>
+    <p class="mt-3 text-sm text-secondary">
+      Use this when you want Codex to choose the right installed tools for the
+      task.
+    </p>
+  </div>
+
+  <div class="rounded-xl border border-subtle bg-surface px-5 py-4">
+    <p class="text-sm font-semibold text-default">Choose a specific plugin</p>
+    <p class="mt-2 text-sm text-secondary">
+      Type <code>@</code> to invoke the plugin or one of its bundled skills
+      explicitly.
+    </p>
+    <p class="mt-3 text-sm text-secondary">
+      Use this when you want to be specific about which plugin or skill Codex
+      should use. See <a href="/codex/app/commands">Codex app commands</a> and{" "}
+      <a href="/codex/skills">Skills</a>.
+    </p>
+  </div>
+</div>
+
+### How permissions and data sharing work
+
+Installing a plugin makes its workflows available in Codex, but your existing
+[approval settings](https://developers.openai.com/codex/agent-approvals-security) still apply. Any
+connected external services remain subject to their own authentication,
+privacy, and data-sharing policies.
+
+- Bundled skills are available as soon as you install the plugin.
+- If a plugin includes apps, Codex may prompt you to install or sign in to
+  those apps in ChatGPT during setup or the first time you use them.
+- If a plugin includes MCP servers, they may require additional setup or
+  authentication before you can use them.
+- When Codex sends data through a bundled app, that app's terms and privacy
+  policy apply.
+
+### Remove or turn off a plugin
+
+To remove a plugin, reopen it from the plugin browser and select
+**Uninstall plugin**.
+
+Uninstalling a plugin removes the plugin bundle from Codex, but bundled apps
+stay installed until you manage them in ChatGPT.
+
+If you want to keep a plugin installed but turn it off, set its entry in
+`~/.codex/config.toml` to `enabled = false`, then restart Codex:
+
+```toml
+[plugins."gmail@openai-curated"]
+enabled = false
+```
+
+## Build your own plugin
+
+If you want to create, test, or distribute your own plugin, see
+[Build plugins](https://developers.openai.com/codex/plugins/build). That page covers local scaffolding,
+manual marketplace setup, plugin manifests, and packaging guidance.
+
+---
+
+# Build plugins
+
+This page is for plugin authors. If you want to browse, install, and use
+plugins in Codex, see [Plugins](https://developers.openai.com/codex/plugins). If you are still iterating on
+one repo or one personal workflow, start with a local skill. Build a plugin
+when you want to share that workflow across teams, bundle app integrations or
+MCP config, or publish a stable package.
+
+## Create a plugin with `$plugin-creator`
+
+For the fastest setup, use the built-in `$plugin-creator` skill.
+
+It scaffolds the required `.codex-plugin/plugin.json` manifest and can also
+generate a local marketplace entry for testing. If you already have a plugin
+folder, you can still use `$plugin-creator` to wire it into a local
+marketplace.
+
+### Build your own curated plugin list
+
+A marketplace is a JSON catalog of plugins. `$plugin-creator` can generate one
+for a single plugin, and you can keep adding entries to that same marketplace
+to build your own curated list for a repo, team, or personal workflow.
+
+In Codex, each marketplace appears as a selectable source in the plugin
+directory. Use `$REPO_ROOT/.agents/plugins/marketplace.json` for a repo-scoped
+list or `~/.agents/plugins/marketplace.json` for a personal list. Add one
+entry per plugin under `plugins[]`, point each `source.path` at the plugin
+folder with a `./`-prefixed path relative to the marketplace root, and set
+`interface.displayName` to the label you want Codex to show in the marketplace
+picker. Then restart Codex. After that, open the plugin directory, choose your
+marketplace, and browse or install the plugins in that curated list.
+
+You don't need a separate marketplace per plugin. One marketplace can expose a
+single plugin while you are testing, then grow into a larger curated catalog as
+you add more plugins.
+
+### Add a marketplace from the CLI
+
+Use `codex plugin marketplace add` when you want Codex to install and track a
+marketplace source for you instead of editing `config.toml` by hand.
+
+```bash
+codex plugin marketplace add owner/repo
+codex plugin marketplace add owner/repo --ref main
+codex plugin marketplace add https://github.com/example/plugins.git --sparse .agents/plugins
+codex plugin marketplace add ./local-marketplace-root
+```
+
+Marketplace sources can be GitHub shorthand (`owner/repo` or
+`owner/repo@ref`), HTTP or HTTPS Git URLs, SSH Git URLs, or local marketplace root
+directories. Use `--ref` to pin a Git ref, and repeat `--sparse PATH` to use a
+sparse checkout for Git-backed marketplace repos. `--sparse` is valid only for
+Git marketplace sources.
+
+To refresh or remove configured marketplaces:
+
+```bash
+codex plugin marketplace upgrade
+codex plugin marketplace upgrade marketplace-name
+codex plugin marketplace remove marketplace-name
+```
+
+### Create a plugin manually
+
+Start with a minimal plugin that packages one skill.
+
+1. Create a plugin folder with a manifest at `.codex-plugin/plugin.json`.
+
+```bash
+mkdir -p my-first-plugin/.codex-plugin
+```
+
+`my-first-plugin/.codex-plugin/plugin.json`
+
+```json
+{
+  "name": "my-first-plugin",
+  "version": "1.0.0",
+  "description": "Reusable greeting workflow",
+  "skills": "./skills/"
+}
+```
+
+Use a stable plugin `name` in kebab-case. Codex uses it as the plugin
+identifier and component namespace.
+
+2. Add a skill under `skills/<skill-name>/SKILL.md`.
+
+```bash
+mkdir -p my-first-plugin/skills/hello
+```
+
+`my-first-plugin/skills/hello/SKILL.md`
+
+```md
+---
+name: hello
+description: Greet the user with a friendly message.
+---
+
+Greet the user warmly and ask how you can help.
+```
+
+3. Add the plugin to a marketplace. Use `$plugin-creator` to generate one, or
+   follow [Build your own curated plugin list](#build-your-own-curated-plugin-list)
+   to wire the plugin into Codex manually.
+
+From there, you can add MCP config, app integrations, or marketplace metadata
+as needed.
+
+### Install a local plugin manually
+
+Use a repo marketplace or a personal marketplace, depending on who should be
+able to access the plugin or curated list.
+
+
+
+<div slot="workspace">
+    Add a marketplace file at `$REPO_ROOT/.agents/plugins/marketplace.json`
+    and store your plugins under `$REPO_ROOT/plugins/`.
+
+    **Repo marketplace example**
+
+    Step 1: Copy the plugin folder into `$REPO_ROOT/plugins/my-plugin`.
+
+```bash
+mkdir -p ./plugins
+cp -R /absolute/path/to/my-plugin ./plugins/my-plugin
+```
+
+    Step 2: Add or update `$REPO_ROOT/.agents/plugins/marketplace.json` so
+    that `source.path` points to that plugin directory with a `./`-prefixed
+    relative path:
+
+```json
+{
+  "name": "local-repo",
+  "plugins": [
+    {
+      "name": "my-plugin",
+      "source": {
+        "source": "local",
+        "path": "./plugins/my-plugin"
+      },
+      "policy": {
+        "installation": "AVAILABLE",
+        "authentication": "ON_INSTALL"
+      },
+      "category": "Productivity"
+    }
+  ]
+}
+```
+
+    Step 3: Restart Codex and verify that the plugin appears.
+
+  </div>
+
+  <div slot="global">
+    Add a marketplace file at `~/.agents/plugins/marketplace.json` and store
+    your plugins under `~/.codex/plugins/`.
+
+    **Personal marketplace example**
+
+    Step 1: Copy the plugin folder into `~/.codex/plugins/my-plugin`.
+
+```bash
+mkdir -p ~/.codex/plugins
+cp -R /absolute/path/to/my-plugin ~/.codex/plugins/my-plugin
+```
+
+    Step 2: Add or update `~/.agents/plugins/marketplace.json` so that the
+    plugin entry's `source.path` points to that directory.
+
+    Step 3: Restart Codex and verify that the plugin appears.
+
+  </div>
+
+
+
+The marketplace file points to the plugin location, so those directories are
+examples rather than fixed requirements. Codex resolves `source.path` relative
+to the marketplace root, not relative to the `.agents/plugins/` folder. See
+[Marketplace metadata](#marketplace-metadata) for the file format.
+
+After you change the plugin, update the plugin directory that your marketplace
+entry points to and restart Codex so the local install picks up the new files.
+
+### Marketplace metadata
+
+If you maintain a repo marketplace, define it in
+`$REPO_ROOT/.agents/plugins/marketplace.json`. For a personal marketplace, use
+`~/.agents/plugins/marketplace.json`. A marketplace file controls plugin
+ordering and install policies in Codex-facing catalogs. It can represent one
+plugin while you are testing or a curated list of plugins that you want Codex
+to show together under one marketplace name. Before you add a plugin to a
+marketplace, make sure its `version`, publisher metadata, and install-surface
+copy are ready for other developers to see.
+
+```json
+{
+  "name": "local-example-plugins",
+  "interface": {
+    "displayName": "Local Example Plugins"
+  },
+  "plugins": [
+    {
+      "name": "my-plugin",
+      "source": {
+        "source": "local",
+        "path": "./plugins/my-plugin"
+      },
+      "policy": {
+        "installation": "AVAILABLE",
+        "authentication": "ON_INSTALL"
+      },
+      "category": "Productivity"
+    },
+    {
+      "name": "research-helper",
+      "source": {
+        "source": "local",
+        "path": "./plugins/research-helper"
+      },
+      "policy": {
+        "installation": "AVAILABLE",
+        "authentication": "ON_INSTALL"
+      },
+      "category": "Productivity"
+    }
+  ]
+}
+```
+
+- Use top-level `name` to identify the marketplace.
+- Use `interface.displayName` for the marketplace title shown in Codex.
+- Add one object per plugin under `plugins` to build a curated list that Codex
+  shows under that marketplace title.
+- Point each plugin entry's `source.path` at the plugin directory you want
+  Codex to load. For repo installs, that often lives under `./plugins/`. For
+  personal installs, a common pattern is `./.codex/plugins/<plugin-name>`.
+- Keep `source.path` relative to the marketplace root, start it with `./`, and
+  keep it inside that root.
+- For local entries, `source` can also be a plain string path such as
+  `"./plugins/my-plugin"`.
+- Always include `policy.installation`, `policy.authentication`, and
+  `category` on each plugin entry.
+- Use `policy.installation` values such as `AVAILABLE`,
+  `INSTALLED_BY_DEFAULT`, or `NOT_AVAILABLE`.
+- Use `policy.authentication` to decide whether auth happens on install or
+  first use.
+
+The marketplace controls where Codex loads the plugin from. A local
+`source.path` can point somewhere else if your plugin lives outside those
+example directories. A marketplace file can live in the repo where you are
+developing the plugin or in a separate marketplace repo, and one marketplace
+file can point to one plugin or many.
+
+Marketplace entries can also point at Git-backed plugin sources. Use
+`"source": "url"` when the plugin lives at the repository root, or
+`"source": "git-subdir"` when the plugin lives in a subdirectory:
+
+```json
+{
+  "name": "remote-helper",
+  "source": {
+    "source": "git-subdir",
+    "url": "https://github.com/example/codex-plugins.git",
+    "path": "./plugins/remote-helper",
+    "ref": "main"
+  },
+  "policy": {
+    "installation": "AVAILABLE",
+    "authentication": "ON_INSTALL"
+  },
+  "category": "Productivity"
+}
+```
+
+Git-backed entries may use `ref` or `sha` selectors. If Codex can't resolve a
+marketplace entry's source, it skips that plugin entry instead of failing the
+whole marketplace.
+
+### How Codex uses marketplaces
+
+A plugin marketplace is a JSON catalog of plugins that Codex can read and
+install.
+
+Codex can read marketplace files from:
+
+- the curated marketplace that powers the official Plugin Directory
+- a repo marketplace at `$REPO_ROOT/.agents/plugins/marketplace.json`
+- a Claude-style marketplace at `$REPO_ROOT/.claude-plugin/marketplace.json`
+- a personal marketplace at `~/.agents/plugins/marketplace.json`
+
+You can install any plugin exposed through a marketplace. Codex installs
+plugins into
+`~/.codex/plugins/cache/$MARKETPLACE_NAME/$PLUGIN_NAME/$VERSION/`. For local
+plugins, `$VERSION` is `local`, and Codex loads the installed copy from that
+cache path rather than directly from the marketplace entry.
+
+You can enable or disable each plugin individually. Codex stores each plugin's
+on or off state in `~/.codex/config.toml`.
+
+## Package and distribute plugins
+
+### Plugin structure
+
+Every plugin has a manifest at `.codex-plugin/plugin.json`. It can also include
+a `skills/` directory, an `.app.json` file that points at one or more apps or
+connectors, an `.mcp.json` file that configures MCP servers, lifecycle config,
+and assets used to present the plugin across supported surfaces.
+
+Only `plugin.json` belongs in `.codex-plugin/`. Keep `skills/`, `assets/`,
+`.mcp.json`, `.app.json`, and lifecycle config files at the plugin root.
+
+Published plugins typically use a richer manifest than the minimal example that
+appears in quick-start scaffolds. The manifest has three jobs:
+
+- Identify the plugin.
+- Point to bundled components such as skills, apps, or MCP servers.
+- Provide install-surface metadata such as descriptions, icons, and legal
+  links.
+
+Here's a complete manifest example:
+
+```json
+{
+  "name": "my-plugin",
+  "version": "0.1.0",
+  "description": "Bundle reusable skills and app integrations.",
+  "author": {
+    "name": "Your team",
+    "email": "team@example.com",
+    "url": "https://example.com"
+  },
+  "homepage": "https://example.com/plugins/my-plugin",
+  "repository": "https://github.com/example/my-plugin",
+  "license": "MIT",
+  "keywords": ["research", "crm"],
+  "skills": "./skills/",
+  "mcpServers": "./.mcp.json",
+  "apps": "./.app.json",
+  "hooks": "./hooks/hooks.json",
+  "interface": {
+    "displayName": "My Plugin",
+    "shortDescription": "Reusable skills and apps",
+    "longDescription": "Distribute skills and app integrations together.",
+    "developerName": "Your team",
+    "category": "Productivity",
+    "capabilities": ["Read", "Write"],
+    "websiteURL": "https://example.com",
+    "privacyPolicyURL": "https://example.com/privacy",
+    "termsOfServiceURL": "https://example.com/terms",
+    "defaultPrompt": [
+      "Use My Plugin to summarize new CRM notes.",
+      "Use My Plugin to triage new customer follow-ups."
+    ],
+    "brandColor": "#10A37F",
+    "composerIcon": "./assets/icon.png",
+    "logo": "./assets/logo.png",
+    "screenshots": ["./assets/screenshot-1.png"]
+  }
+}
+```
+
+`.codex-plugin/plugin.json` is the required entry point. The other manifest
+fields are optional, but published plugins commonly use them.
+
+### Manifest fields
+
+Use the top-level fields to define package metadata and point to bundled
+components:
+
+- `name`, `version`, and `description` identify the plugin.
+- `author`, `homepage`, `repository`, `license`, and `keywords` provide
+  publisher and discovery metadata.
+- `skills`, `mcpServers`, `apps`, and `hooks` point to bundled components
+  relative to the plugin root.
+- `interface` controls how install surfaces present the plugin.
+
+Use the `interface` object for install-surface metadata:
+
+- `displayName`, `shortDescription`, and `longDescription` control the title
+  and descriptive copy.
+- `developerName`, `category`, and `capabilities` add publisher and capability
+  metadata.
+- `websiteURL`, `privacyPolicyURL`, and `termsOfServiceURL` provide external
+  links.
+- `defaultPrompt`, `brandColor`, `composerIcon`, `logo`, and `screenshots`
+  control starter prompts and visual presentation.
+
+### Path rules
+
+- Keep manifest paths relative to the plugin root and start them with `./`.
+- Store visual assets such as `composerIcon`, `logo`, and `screenshots` under
+  `./assets/` when possible.
+- Use `skills` for bundled skill folders, `apps` for `.app.json`,
+  `mcpServers` for `.mcp.json`, and `hooks` for lifecycle config.
+- If you omit `hooks` and the plugin includes `./hooks/hooks.json`, Codex loads
+  that default lifecycle config automatically.
+
+### Bundled MCP servers and lifecycle config
+
+`mcpServers` can point to an `.mcp.json` file that contains either a direct
+server map or a wrapped `mcp_servers` object.
+
+Direct server map:
+
+```json
+{
+  "docs": {
+    "command": "docs-mcp",
+    "args": ["--stdio"]
+  }
+}
+```
+
+Wrapped server map:
+
+```json
+{
+  "mcp_servers": {
+    "docs": {
+      "command": "docs-mcp",
+      "args": ["--stdio"]
+    }
+  }
+}
+```
+
+`hooks` can point to one lifecycle JSON file, an array of lifecycle JSON files,
+an inline lifecycle object, or an array of inline lifecycle objects. File paths
+must follow the same `./`-prefixed plugin-root path rules as other manifest
+paths. If you omit the manifest field, Codex still checks `./hooks/hooks.json`.
+
+### Publish official public plugins
+
+Adding plugins to the official Plugin Directory is coming soon.
+
+Self-serve plugin publishing and management are coming soon.
+
+---
+
 # Codex Pricing
 
-For a limited time, **try Codex for free in ChatGPT Free and Go**, or enjoy
-  **2x Codex rate limits** with Plus, Pro, Business and Enterprise
-  subscriptions.
-
-<div class="codex-pricing-grid">
-  
-
-- Codex on the web, in the CLI, in the IDE extension, and on iOS
-    - Cloud-based integrations like automatic code review and Slack integration
-    - The latest models, including GPT-5.4 and GPT-5.3-Codex
-    - GPT-5.1-Codex-Mini for up to 4x higher usage limits for local messages
-    - Flexibly extend usage with [ChatGPT credits](#credits-overview)
-    - Other [ChatGPT features](https://chatgpt.com/pricing) as part of the Plus plan
-
-
-  
-
-- Priority request processing
-    - Access to GPT-5.3-Codex-Spark (research preview), a fast Codex model for day-to-day coding tasks
-    - 6x higher usage limits for local and cloud tasks
-    - 10x more cloud-based code reviews
-    - Other [ChatGPT features](https://chatgpt.com/pricing) as part of the Pro plan
-
-
-</div>
-
-<div class="mt-8 codex-pricing-grid">
-  
-
-- Larger virtual machines to run cloud tasks faster
-    - Flexibly extend usage with [ChatGPT credits](#credits-overview)
-    - A secure, dedicated workspace with essential admin controls, SAML SSO, and MFA
-    - No training on your business data by default. [Learn more](https://openai.com/business-data/)
-    - Other [ChatGPT features](https://chatgpt.com/pricing) as part of the Business plan
-
-
-  
-
-- Priority request processing
-    - Enterprise-level security and controls, including SCIM, EKM, user analytics, domain verification, and role-based access control ([RBAC](https://help.openai.com/en/articles/11750701-rbac))
-    - Audit logs and usage monitoring via the [Compliance API](https://chatgpt.com/admin/api-reference#tag/Codex-Tasks)
-    - Data retention and data residency controls
-    - Other [ChatGPT features](https://chatgpt.com/pricing) as part of the Enterprise plan
-
-
-</div>
-
-<div class="mt-8 mb-10 codex-pricing-grid">
-  
-
-- Codex in the CLI, SDK, or IDE extension
-    - No cloud-based features (GitHub code review, Slack, etc.)
-    - Delayed access to new models like GPT-5.3-Codex and GPT-5.3-Codex-Spark
-    - Pay only for the tokens Codex uses, based on [API pricing](https://platform.openai.com/docs/pricing)
-
-
-</div>
+<h2 class="sr-only">Pricing options</h2>
+
+
+
+<div data-content-switcher-pane data-value="individual">
+    <div class="codex-pricing-grid">
+      <PricingCard
+        name="Plus"
+        subtitle="Power a few focused coding sessions each week."
+        price="$20"
+        interval="/month"
+        ctaLabel="Get Plus"
+        ctaHref="https://chatgpt.com/explore/plus?utm_internal_source=openai_developers_codex"
+      >
+        - Codex on the web, in the CLI, in the IDE extension, and on iOS
+        - Cloud-based integrations like automatic code review and Slack
+          integration
+        - The latest models, including GPT-5.5, GPT-5.4, and GPT-5.3-Codex
+        - GPT-5.4-mini for higher usage limits on routine local messages
+        - Flexibly extend usage with [ChatGPT credits](#credits-overview)
+        - Other [ChatGPT features](https://chatgpt.com/pricing) as part of the
+          Plus plan
+      </PricingCard>
+      <PricingCard
+        name="Pro"
+        subtitle="Choose 5x or 20x higher rate limits than Plus."
+        priceEyebrow="From"
+        price="$100"
+        interval="/month"
+        ctaLabel="Get Pro"
+        ctaHref="https://chatgpt.com/explore/pro?utm_internal_source=openai_developers_codex"
+        highlight="Everything in Plus and:"
+        footnoteLabel="*Learn more about limits and promos on both tiers."
+        footnoteHref="https://help.openai.com/en/articles/9793128-about-chatgpt-pro-plans"
+      >
+        **Double your normal Codex usage on the $100/month tier until May 31, 2026.**
+
+        - Access to GPT-5.3-Codex-Spark (research preview), a fast Codex model
+          for day-to-day coding tasks
+        - ~~5x~~ 10x or 20x more Codex usage than Plus*
+        - Other [ChatGPT features](https://chatgpt.com/pricing) as part of the
+          Pro plan
+      </PricingCard>
+      <PricingCard
+        name="API Key"
+        subtitle="Great for automation in shared environments like CI."
+        price=""
+        interval=""
+        ctaLabel="Learn more"
+        ctaHref="/codex/auth"
+        highlight=""
+      >
+        - Codex in the CLI, SDK, or IDE extension
+        - No cloud-based features (GitHub code review, Slack, etc.)
+        - Delayed access to new models like GPT-5.3-Codex and
+          GPT-5.3-Codex-Spark
+        - Pay only for the tokens Codex uses, based on [API
+          pricing](https://platform.openai.com/docs/pricing)
+      </PricingCard>
+    </div>
+
+  </div>
+
+  <div data-content-switcher-pane data-value="business-enterprise" hidden>
+    <div class="codex-pricing-grid">
+      <PricingCard
+        name="Business"
+        subtitle="Bring Codex into your startup or growing business."
+        price="Pay as you go"
+        interval=""
+        ctaLabel="Get Business"
+        ctaHref="https://chatgpt.com/codex/team/start"
+        highlight="Everything in Plus and:"
+      >
+        - Assign standard or usage-based Codex seats based on your team's needs.
+          [Learn
+          more](https://help.openai.com/en/articles/8792828-what-is-chatgpt-business)
+        - Larger virtual machines to run cloud tasks faster
+        - Flexibly extend usage with [ChatGPT credits](#credits-overview)
+        - A secure, dedicated workspace with essential admin controls, SAML SSO,
+          and MFA
+        - No training on your business data by default. [Learn
+          more](https://openai.com/business-data/)
+        - Other [ChatGPT features](https://chatgpt.com/pricing) as part of the
+          Business plan
+      </PricingCard>
+      <PricingCard
+        name="Enterprise & Edu"
+        subtitle="Unlock Codex for your entire organization with enterprise-grade functionality."
+        interval=""
+        ctaLabel="Contact sales"
+        ctaHref="https://chatgpt.com/contact-sales?utm_internal_source=openai_developers_codex"
+        highlight="Everything in Business and:"
+      >
+        - Priority request processing
+        - Enterprise-level security and controls, including SCIM, EKM, user
+          analytics, domain verification, and role-based access control
+          ([RBAC](https://help.openai.com/en/articles/11750701-rbac))
+        - Audit logs and usage monitoring via the [Compliance
+          API](https://chatgpt.com/admin/api-reference#tag/Codex-Tasks)
+        - Data retention and data residency controls
+        - Other [ChatGPT features](https://chatgpt.com/pricing) as part of the
+          Enterprise plan
+      </PricingCard>
+    </div>
+
+    <div class="mt-8 mb-10 codex-pricing-grid">
+      <PricingCard
+        class="codex-pricing-card--span-two"
+        name="API Key"
+        subtitle="Great for automation in shared environments like CI."
+        price=""
+        interval=""
+        ctaLabel="Learn more"
+        ctaHref="/codex/auth"
+        highlight=""
+      >
+        - Codex in the CLI, SDK, or IDE extension
+        - No cloud-based features (GitHub code review, Slack, etc.)
+        - Delayed access to new models like GPT-5.3-Codex and
+          GPT-5.3-Codex-Spark
+        - Pay only for the tokens Codex uses, based on [API
+          pricing](https://platform.openai.com/docs/pricing)
+      </PricingCard>
+    </div>
+
+  </div>
+
+
 
 ## Frequently asked questions
 
 ### What are the usage limits for my plan?
 
-The number of Codex messages you can send depends on the model used, size and complexity of your coding tasks and whether you run them locally or in the cloud. Small scripts or routine functions may consume only a fraction of your allowance, while larger codebases, long-running tasks, or extended sessions that require Codex to hold more context will use significantly more per message.
+The number of Codex messages you can send depends on the model used, size and
+complexity of your coding tasks and whether you run them locally or in the
+cloud. Small scripts or routine functions may consume only a fraction of your
+allowance, while larger codebases, long-running tasks, or extended sessions that
+require Codex to hold more context will use significantly more per message.
+
+GPT-5.5 uses significantly fewer tokens to achieve results comparable to
+GPT-5.4. Its Codex setup runs faster and delivers higher-quality results for
+most users. These efficiency gains support generous usage limits despite
+GPT-5.5 being a significantly more capable model.
 
 <div id="usage-limits">
   
 
-<div data-content-switcher-pane data-value="gpt-5-4">
-      <div class="hidden">GPT-5.4</div>
+<div data-content-switcher-pane data-value="plus">
+      <div class="hidden">Plus</div>
 
       <table>
         <thead>
           <tr>
             <th scope="col"></th>
             <th scope="col" style="text-align:center">
-              Local Messages[\*](#shared-limits) / 5h
+              Local Messages[\*](#shared-limits-plus) / 5h
             </th>
             <th scope="col" style="text-align:center">
-              Cloud Tasks[\*](#shared-limits) / 5h
+              Cloud Tasks[\*](#shared-limits-plus) / 5h
             </th>
             <th scope="col" style="text-align:center">
-              Code Reviews / week
+              Code Reviews / 5h
             </th>
           </tr>
         </thead>
         <tbody>
           <tr>
-            <td>ChatGPT Plus</td>
-            <td style="text-align:center">33-168</td>
+            <td>GPT-5.5</td>
+            <td style="text-align:center">15-80</td>
             <td style="text-align:center">Not available</td>
             <td style="text-align:center">Not available</td>
           </tr>
           <tr>
-            <td>ChatGPT Pro</td>
-            <td style="text-align:center">223-1120</td>
+            <td>GPT-5.4</td>
+            <td style="text-align:center">20-100</td>
             <td style="text-align:center">Not available</td>
             <td style="text-align:center">Not available</td>
           </tr>
           <tr>
-            <td>ChatGPT Business</td>
-            <td style="text-align:center">33-168</td>
+            <td>GPT-5.4-mini</td>
+            <td style="text-align:center">60-350</td>
             <td style="text-align:center">Not available</td>
             <td style="text-align:center">Not available</td>
           </tr>
           <tr>
-            <td>ChatGPT Enterprise &amp; Edu</td>
-            <td colspan="3" style="text-align:center">
-              No fixed limits — usage scales with [credits](#credits-overview)
+            <td>GPT-5.3-Codex</td>
+            <td style="text-align:center">30-150</td>
+            <td style="text-align:center">10-60</td>
+            <td style="text-align:center">20-50</td>
+          </tr>
+        </tbody>
+        <tfoot>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              <a id="shared-limits-plus" class="footnote">
+                *The usage limits for local messages and cloud tasks share a
+                **five-hour window**. Additional weekly limits may apply.
+              </a>
             </td>
           </tr>
           <tr>
-            <td>API Key</td>
+            <td colspan="4" style="text-align:center">
+              For Enterprise/Edu users, there are no fixed rate limits - usage
+              scales with [credits](#credits-overview)
+            </td>
+          </tr>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              Enterprise and Edu plans without flexible pricing have the same
+              per-seat usage limits as Plus for most features
+            </td>
+          </tr>
+        </tfoot>
+      </table>
+    </div>
+    <div data-content-switcher-pane data-value="pro" hidden>
+      <div class="hidden">Pro 5x</div>
+
+      <table>
+        <thead>
+          <tr>
+            <th scope="col"></th>
+            <th scope="col" style="text-align:center">
+              Local Messages[\*](#shared-limits-pro) / 5h
+            </th>
+            <th scope="col" style="text-align:center">
+              Cloud Tasks[\*](#shared-limits-pro) / 5h
+            </th>
+            <th scope="col" style="text-align:center">
+              Code Reviews / 5h
+            </th>
+          </tr>
+        </thead>
+        <tbody>
+          <tr>
+            <td>GPT-5.5</td>
+            <td style="text-align:center">80-400</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+          </tr>
+          <tr>
+            <td>GPT-5.4</td>
+            <td style="text-align:center">100-500</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+          </tr>
+          <tr>
+            <td>GPT-5.4-mini</td>
+            <td style="text-align:center">300-1750</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+          </tr>
+          <tr>
+            <td>GPT-5.3-Codex</td>
+            <td style="text-align:center">150-750</td>
+            <td style="text-align:center">50-300</td>
+            <td style="text-align:center">100-250</td>
+          </tr>
+        </tbody>
+        <tfoot>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              <a id="shared-limits-pro" class="footnote">
+                *The usage limits for local messages and cloud tasks share a
+                **five-hour window**. Additional weekly limits may apply.
+              </a>
+            </td>
+          </tr>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              Pro $100 gets 2x the usage shown above until May 31, 2026.
+            </td>
+          </tr>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              For Enterprise/Edu users, there are no fixed rate limits - usage
+              scales with [credits](#credits-overview)
+            </td>
+          </tr>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              Enterprise and Edu plans without flexible pricing have the same
+              per-seat usage limits as Plus for most features
+            </td>
+          </tr>
+        </tfoot>
+      </table>
+    </div>
+    <div data-content-switcher-pane data-value="pro-20x" hidden>
+      <div class="hidden">Pro 20x</div>
+
+      <table>
+        <thead>
+          <tr>
+            <th scope="col"></th>
+            <th scope="col" style="text-align:center">
+              Local Messages[\*](#shared-limits-pro-20x) / 5h
+            </th>
+            <th scope="col" style="text-align:center">
+              Cloud Tasks[\*](#shared-limits-pro-20x) / 5h
+            </th>
+            <th scope="col" style="text-align:center">
+              Code Reviews / 5h
+            </th>
+          </tr>
+        </thead>
+        <tbody>
+          <tr>
+            <td>GPT-5.5</td>
+            <td style="text-align:center">300-1600</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+          </tr>
+          <tr>
+            <td>GPT-5.4</td>
+            <td style="text-align:center">400-2000</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+          </tr>
+          <tr>
+            <td>GPT-5.4-mini</td>
+            <td style="text-align:center">1200-7000</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+          </tr>
+          <tr>
+            <td>GPT-5.3-Codex</td>
+            <td style="text-align:center">600-3000</td>
+            <td style="text-align:center">200-1200</td>
+            <td style="text-align:center">400-1000</td>
+          </tr>
+        </tbody>
+        <tfoot>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              <a id="shared-limits-pro-20x" class="footnote">
+                *The usage limits for local messages and cloud tasks share a
+                **five-hour window**. Additional weekly limits may apply.
+              </a>
+            </td>
+          </tr>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              Pro $200 gets a boost on the usage shown above until May 31,
+              2026. [Learn
+              more](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-plans).
+            </td>
+          </tr>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              For Enterprise/Edu users, there are no fixed rate limits - usage
+              scales with [credits](#credits-overview)
+            </td>
+          </tr>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              Enterprise and Edu plans without flexible pricing have the same
+              per-seat usage limits as Plus for most features
+            </td>
+          </tr>
+        </tfoot>
+      </table>
+    </div>
+    <div data-content-switcher-pane data-value="business" hidden>
+      <div class="hidden">Business</div>
+
+      <table>
+        <thead>
+          <tr>
+            <th scope="col"></th>
+            <th scope="col" style="text-align:center">
+              Local Messages[\*](#shared-limits-business) / 5h
+            </th>
+            <th scope="col" style="text-align:center">
+              Cloud Tasks[\*](#shared-limits-business) / 5h
+            </th>
+            <th scope="col" style="text-align:center">
+              Code Reviews / 5h
+            </th>
+          </tr>
+        </thead>
+        <tbody>
+          <tr>
+            <td>GPT-5.5</td>
+            <td style="text-align:center">15-80</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+          </tr>
+          <tr>
+            <td>GPT-5.4</td>
+            <td style="text-align:center">20-100</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+          </tr>
+          <tr>
+            <td>GPT-5.4-mini</td>
+            <td style="text-align:center">60-350</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+          </tr>
+          <tr>
+            <td>GPT-5.3-Codex</td>
+            <td style="text-align:center">30-150</td>
+            <td style="text-align:center">10-60</td>
+            <td style="text-align:center">20-50</td>
+          </tr>
+        </tbody>
+        <tfoot>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              <a id="shared-limits-business" class="footnote">
+                *The usage limits for local messages and cloud tasks share a
+                **five-hour window**. Additional weekly limits may apply.
+              </a>
+            </td>
+          </tr>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              For Enterprise/Edu users, there are no fixed rate limits - usage
+              scales with [credits](#credits-overview)
+            </td>
+          </tr>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              Enterprise and Edu plans without flexible pricing have the same
+              per-seat usage limits as Plus for most features
+            </td>
+          </tr>
+        </tfoot>
+      </table>
+    </div>
+    <div data-content-switcher-pane data-value="api-key" hidden>
+      <div class="hidden">API Key</div>
+
+      <table>
+        <thead>
+          <tr>
+            <th scope="col"></th>
+            <th scope="col" style="text-align:center">
+              Local Messages[\*](#shared-limits-api-key) / 5h
+            </th>
+            <th scope="col" style="text-align:center">
+              Cloud Tasks[\*](#shared-limits-api-key) / 5h
+            </th>
+            <th scope="col" style="text-align:center">
+              Code Reviews / 5h
+            </th>
+          </tr>
+        </thead>
+        <tbody>
+          <tr>
+            <td>GPT-5.5</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+          </tr>
+          <tr>
+            <td>GPT-5.4</td>
+            <td style="text-align:center">
+              [Usage-based](https://platform.openai.com/docs/pricing)
+            </td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+          </tr>
+          <tr>
+            <td>GPT-5.4-mini</td>
+            <td style="text-align:center">
+              [Usage-based](https://platform.openai.com/docs/pricing)
+            </td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+          </tr>
+          <tr>
+            <td>GPT-5.3-Codex</td>
             <td style="text-align:center">
               [Usage-based](https://platform.openai.com/docs/pricing)
             </td>
@@ -10714,272 +15419,321 @@
             <td style="text-align:center">Not available</td>
           </tr>
         </tbody>
+        <tfoot>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              <a id="shared-limits-api-key" class="footnote">
+                *The usage limits for local messages and cloud tasks share a
+                **five-hour window**. Additional weekly limits may apply.
+              </a>
+            </td>
+          </tr>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              For Enterprise/Edu users, there are no fixed rate limits - usage
+              scales with [credits](#credits-overview)
+            </td>
+          </tr>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              Enterprise and Edu plans without flexible pricing have the same
+              per-seat usage limits as Plus for most features
+            </td>
+          </tr>
+        </tfoot>
       </table>
     </div>
-    <div data-content-switcher-pane data-value="gpt-5-3-codex" hidden>
-      <div class="hidden">GPT-5.3-Codex</div>
-
+
+
+</div>
+
+Codex usage limits are shared with other agentic features once pricing for
+those features is effective. This currently includes [ChatGPT for
+Excel](https://help.openai.com/articles/20001063) on Plus and Pro.
+
+Speed configurations increase credit consumption for all applicable models, so
+they also use included limits faster. Fast mode consumes credits at a higher
+rate for supported models. See [Speed](https://developers.openai.com/codex/speed) for supported models and
+rates. Image generations also use included limits ~3-5x faster on average,
+depending on image quality and size. GPT-5.3-Codex-Spark is in research preview
+for ChatGPT Pro users only, and isn't available in the API at launch. Because it
+runs on specialized low-latency hardware, usage is governed by a separate usage
+limit that may adjust based on demand.
+
+### What happens when you hit usage limits?
+
+ChatGPT Plus and Pro users who reach their usage limit can purchase additional
+credits to continue working without needing to upgrade their existing plan.
+
+Business, Edu, and Enterprise plans with [flexible
+pricing](https://help.openai.com/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans)
+can purchase additional workspace credits to continue using Codex.
+
+If you are approaching usage limits, you can also switch to a smaller model to
+make your usage limits last longer.
+
+All users may also run extra local tasks using an API key, with usage charged at
+[standard API rates](https://platform.openai.com/docs/pricing).
+
+<a id="image-generation-usage-limits"></a>
+
+### How does image generation count toward usage limits?
+
+Image generation counts toward the same general Codex usage limits as local
+messages and cloud tasks. Image generations use included limits 3-5x faster on
+average than similar turns without image generation, depending on
+image quality and size. After you reach your included limits, image generation
+also draws from [credits](#credits-overview).
+
+Image generation isn't available on the Free plan. When you use Codex with an
+API key, API pricing applies to image generation instead of included ChatGPT
+usage limits.
+
+### What's the current Codex usage promo on Pro?
+
+We’re currently offering extra Codex usage on both Pro tiers.
+
+For **Pro $100**, to celebrate the launch, you’ll get **2x Codex usage through May 31, 2026**. That means 10x usage instead of the standard 5x.
+
+**For Pro $200**, as a thank you to our most loyal customers, we’re carrying forward the benefits of our earlier 2x promo, which means Pro $200 now includes 20x Plus on an ongoing basis. In addition, we’re continuing to honor the higher 5-hour Codex limits for a limited time, so those remain at 25x Plus through May 31, 2026 instead of the standard 20x Plus.
+
+### Where can I see my current usage limits?
+
+You can find your current limits in the [Codex usage
+dashboard](https://chatgpt.com/codex/settings/usage). If you want to see your
+remaining limits during an active Codex CLI session, you can use `/status`.
+
+### How do credits work?
+
+Credits let you continue using Codex after you reach your included usage
+limits. Usage draws down from your available credits based on the models and
+features you use, allowing you to extend work without interruption.
+
+As of April 2nd, we're moving pricing to API token-based rates. Credits remain
+the core pricing unit that customers purchase and consume, but usage is based
+on tokens consumed, calculated as credits per million input tokens, cached
+input tokens and output tokens your workspace consumes. Read about tokens
+[here](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them).
+
+This format replaces average per-message estimates for your plan with a direct
+mapping between token usage and credits. It's most useful when you want a
+clearer view of how input, cached input, and output affect credit consumption.
+
+Under this model, actual credit usage depends on the mix of input, cached input,
+and output tokens in each task. The new rate card is displayed in the table
+below, and is currently applicable to **new and existing Business customers,
+and new Enterprise customers**.
+
+**New and existing customers on all other plan types** should continue to use
+the previous message based rate card, until we migrate you to the new rates in
+the upcoming weeks.
+
+Select your appropriate plan type in the table below to see rates.
+
+<div id="credits-overview">
+  
+
+<div data-content-switcher-pane data-value="business-enterprise-new">
+      <div class="hidden">Business & New Enterprise Customers</div>
+      <table>
+        <thead>
+          <tr>
+            <th scope="col">Credits per 1M tokens</th>
+            <th scope="col" style="text-align:center">
+              Input Tokens
+            </th>
+            <th scope="col" style="text-align:center">
+              Cached input tokens
+            </th>
+            <th scope="col" style="text-align:center">
+              Output Tokens
+            </th>
+          </tr>
+        </thead>
+        <tbody>
+          <tr>
+            <td>GPT-5.5</td>
+            <td style="text-align:center">125 credits</td>
+            <td style="text-align:center">12.50 credits</td>
+            <td style="text-align:center">750 credits</td>
+          </tr>
+          <tr>
+            <td>GPT-5.4</td>
+            <td style="text-align:center">62.50 credits</td>
+            <td style="text-align:center">6.250 credits</td>
+            <td style="text-align:center">375 credits</td>
+          </tr>
+          <tr>
+            <td>GPT-5.4-mini</td>
+            <td style="text-align:center">18.75 credits</td>
+            <td style="text-align:center">1.875 credits</td>
+            <td style="text-align:center">113 credits</td>
+          </tr>
+          <tr>
+            <td>GPT-5.3-Codex</td>
+            <td style="text-align:center">43.75 credits</td>
+            <td style="text-align:center">4.375 credits</td>
+            <td style="text-align:center">350 credits</td>
+          </tr>
+          <tr>
+            <td>GPT-5.2</td>
+            <td style="text-align:center">43.75 credits</td>
+            <td style="text-align:center">4.375 credits</td>
+            <td style="text-align:center">350 credits</td>
+          </tr>
+          <tr>
+            <td>GPT-5.3-Codex-Spark</td>
+            <td colspan="3" style="text-align:center">
+              research preview
+            </td>
+          </tr>
+          <tr>
+            <td>GPT-Image-2 (image)</td>
+            <td style="text-align:center">200 credits</td>
+            <td style="text-align:center">50 credits</td>
+            <td style="text-align:center">750 credits</td>
+          </tr>
+          <tr>
+            <td>GPT-Image-2 (text)</td>
+            <td style="text-align:center">125 credits</td>
+            <td style="text-align:center">31.25 credits</td>
+            <td style="text-align:center">250 credits</td>
+          </tr>
+        </tbody>
+        <tfoot>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              Fast mode consumes credits at a higher rate for supported models.
+              See <a href="/codex/speed">Speed</a> for rates.
+            </td>
+          </tr>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              Cloud tasks and code review run on GPT-5.3-Codex.
+            </td>
+          </tr>
+        </tfoot>
+      </table>
+    </div>
+    <div
+      data-content-switcher-pane
+      data-value="plus-pro-enterprise-edu-legacy"
+      hidden
+    >
+      <div class="hidden">Plus, Pro, Existing Enterprise/Edu and New Edu</div>
       <table>
         <thead>
           <tr>
             <th scope="col"></th>
             <th scope="col" style="text-align:center">
-              Local Messages[\*](#shared-limits) / 5h
+              Unit
             </th>
             <th scope="col" style="text-align:center">
-              Cloud Tasks[\*](#shared-limits) / 5h
+              GPT-5.5
             </th>
             <th scope="col" style="text-align:center">
-              Code Reviews / week
-            </th>
-          </tr>
-        </thead>
-        <tbody>
-          <tr>
-            <td>ChatGPT Plus</td>
-            <td style="text-align:center">45-225</td>
-            <td style="text-align:center">10-60</td>
-            <td style="text-align:center">10-25</td>
-          </tr>
-          <tr>
-            <td>ChatGPT Pro</td>
-            <td style="text-align:center">300-1500</td>
-            <td style="text-align:center">50-400</td>
-            <td style="text-align:center">100-250</td>
-          </tr>
-          <tr>
-            <td>ChatGPT Business</td>
-            <td style="text-align:center">45-225</td>
-            <td style="text-align:center">10-60</td>
-            <td style="text-align:center">10-25</td>
-          </tr>
-          <tr>
-            <td>ChatGPT Enterprise &amp; Edu</td>
-            <td colspan="3" style="text-align:center">
-              No fixed limits — usage scales with [credits](#credits-overview)
-            </td>
-          </tr>
-          <tr>
-            <td>API Key</td>
-            <td style="text-align:center">
-              [Usage-based](https://platform.openai.com/docs/pricing)
-            </td>
-            <td style="text-align:center">Not available</td>
-            <td style="text-align:center">Not available</td>
-          </tr>
-        </tbody>
-      </table>
-    </div>
-    <div data-content-switcher-pane data-value="gpt-5-1-codex-mini" hidden>
-      <div class="hidden">GPT-5.1-Codex-Mini</div>
-
-      <table>
-        <thead>
-          <tr>
-            <th scope="col"></th>
-            <th scope="col" style="text-align:center">
-              Local Messages[\*](#shared-limits) / 5h
+              GPT-5.4
             </th>
             <th scope="col" style="text-align:center">
-              Cloud Tasks[\*](#shared-limits) / 5h
+              GPT-5.3-Codex
             </th>
             <th scope="col" style="text-align:center">
-              Code Reviews / week
+              GPT-5.4-mini
             </th>
-          </tr>
-        </thead>
-        <tbody>
-          <tr>
-            <td>ChatGPT Plus</td>
-            <td style="text-align:center">180-900</td>
-            <td style="text-align:center">Not available</td>
-            <td style="text-align:center">Not available</td>
-          </tr>
-          <tr>
-            <td>ChatGPT Pro</td>
-            <td style="text-align:center">1200-6000</td>
-            <td style="text-align:center">Not available</td>
-            <td style="text-align:center">Not available</td>
-          </tr>
-          <tr>
-            <td>ChatGPT Business</td>
-            <td style="text-align:center">180-900</td>
-            <td style="text-align:center">Not available</td>
-            <td style="text-align:center">Not available</td>
-          </tr>
-          <tr>
-            <td>ChatGPT Enterprise &amp; Edu</td>
-            <td style="text-align:center">
-              Local usage scales with [credits](#credits-overview)
-            </td>
-            <td style="text-align:center">Not available</td>
-            <td style="text-align:center">Not available</td>
-          </tr>
-          <tr>
-            <td>API Key</td>
-            <td style="text-align:center">
-              [Usage-based](https://platform.openai.com/docs/pricing)
-            </td>
-            <td style="text-align:center">Not available</td>
-            <td style="text-align:center">Not available</td>
-          </tr>
-        </tbody>
-      </table>
-    </div>
-
-
-</div>
-
-<a id="shared-limits" class="footnote">
-  *The usage limits for local messages and cloud tasks share a **five-hour
-  window**. Additional weekly limits may apply.
-</a>
-
-Speed configurations increase credit consumption for all applicable models, so
-they also use included limits faster. Details can be found
-[here](https://developers.openai.com/codex/speed).
-
-Enterprise and Edu plans without flexible pricing have the same per-seat usage limits as Plus for most features.
-
-GPT-5.3-Codex-Spark is in research preview for ChatGPT Pro users only, and isn't available in the API at launch. Because it runs on specialized low-latency hardware, usage is governed by a separate usage limit that may adjust based on demand.
-
-### What happens when you hit usage limits?
-
-ChatGPT Plus and Pro users who reach their usage limit can purchase additional credits to continue working without needing to upgrade their existing plan.
-
-Business, Edu, and Enterprise plans with [flexible pricing](https://help.openai.com/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans) can purchase additional workspace credits to continue using Codex.
-
-If you are approaching usage limits, you can also switch to the GPT-5.1-Codex-Mini model to make your usage limits last longer.
-
-All users may also run extra local tasks using an API key, with usage charged at [standard API rates](https://platform.openai.com/docs/pricing).
-
-### Where can I see my current usage limits?
-
-You can find your current limits in the [Codex usage dashboard](https://chatgpt.com/codex/settings/usage). If you want to see your remaining limits during an active Codex CLI session, you can use `/status`.
-
-### How do credits work?
-
-Credits let you continue using Codex after you reach your included usage limits. Usage draws down from your available credits based on the models and features you use, allowing you to extend work without interruption.
-
-Credit cost per message varies based on the model used, the task size and complexity, and the reasoning required. The table shows average credit costs. Average rates may evolve over time as new capabilities are introduced.
-
-<div id="credits-overview">
-  
-
-<div data-content-switcher-pane data-value="gpt-5-4">
-      <div class="hidden">GPT-5.4</div>
-
-      <table>
-        <thead>
-          <tr>
-            <th scope="col"></th>
-            <th scope="col" style="text-align:center">Unit</th>
-            <th scope="col" style="text-align:center">Average credit cost</th>
           </tr>
         </thead>
         <tbody>
           <tr>
             <td>Local Tasks</td>
             <td style="text-align:center">1 message</td>
+            <td style="text-align:center">\~14 credits</td>
             <td style="text-align:center">\~7 credits</td>
+            <td style="text-align:center">\~5 credits</td>
+            <td style="text-align:center">\~2 credits</td>
           </tr>
           <tr>
             <td>Cloud Tasks</td>
             <td style="text-align:center">1 message</td>
-            <td style="text-align:center">\~34 credits</td>
-          </tr>
-          <tr>
-            <td>Code Review</td>
-            <td style="text-align:center">1 pull request</td>
-            <td style="text-align:center">\~34 credits</td>
-          </tr>
-        </tbody>
-      </table>
-    </div>
-    <div data-content-switcher-pane data-value="gpt-5-3-codex" hidden>
-      <div class="hidden">GPT-5.3-Codex</div>
-
-      <table>
-        <thead>
-          <tr>
-            <th scope="col"></th>
-            <th scope="col" style="text-align:center">Unit</th>
-            <th scope="col" style="text-align:center">Average credit cost</th>
-          </tr>
-        </thead>
-        <tbody>
-          <tr>
-            <td>Local Tasks</td>
-            <td style="text-align:center">1 message</td>
-            <td style="text-align:center">\~5 credits</td>
-          </tr>
-          <tr>
-            <td>Cloud Tasks</td>
-            <td style="text-align:center">1 message</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
             <td style="text-align:center">\~25 credits</td>
-          </tr>
-          <tr>
-            <td>Code Review</td>
-            <td style="text-align:center">1 pull request</td>
-            <td style="text-align:center">\~25 credits</td>
-          </tr>
-        </tbody>
-      </table>
-    </div>
-    <div data-content-switcher-pane data-value="gpt-5-1-codex-mini" hidden>
-      <div class="hidden">GPT-5.1-Codex-Mini</div>
-
-      <table>
-        <thead>
-          <tr>
-            <th scope="col"></th>
-            <th scope="col" style="text-align:center">Unit</th>
-            <th scope="col" style="text-align:center">Average credit cost</th>
-          </tr>
-        </thead>
-        <tbody>
-          <tr>
-            <td>Local Tasks</td>
-            <td style="text-align:center">1 message</td>
-            <td style="text-align:center">\~1 credit</td>
-          </tr>
-          <tr>
-            <td>Cloud Tasks</td>
-            <td style="text-align:center">1 message</td>
             <td style="text-align:center">Not available</td>
           </tr>
           <tr>
             <td>Code Review</td>
             <td style="text-align:center">1 pull request</td>
             <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">\~25 credits</td>
+            <td style="text-align:center">Not available</td>
+          </tr>
+          <tr>
+            <td>Image generation</td>
+            <td style="text-align:center">1 image (1024px &times; 1024px)</td>
+            <td colspan="4" style="text-align:center">
+              \~5-6 credits
+            </td>
+          </tr>
+          <tr>
+            <td>Image generation</td>
+            <td style="text-align:center">1 image (1024px &times; 1536px)</td>
+            <td colspan="4" style="text-align:center">
+              \~7-8 credits
+            </td>
           </tr>
         </tbody>
+        <tfoot>
+          <tr>
+            <td colspan="6" style="text-align:center">
+              Fast mode consumes credits at a higher rate for supported models.
+              See <a href="/codex/speed">Speed</a> for rates.
+            </td>
+          </tr>
+          <tr>
+            <td colspan="6" style="text-align:center">
+              These averages also apply to GPT-5.2.
+            </td>
+          </tr>
+        </tfoot>
       </table>
     </div>
 
 
 </div>
 
-These averages also apply to legacy GPT-5.2, GPT-5.2-Codex, GPT-5.1, GPT-5.1-Codex-Max, GPT-5, GPT-5-Codex, and GPT-5-Codex-Mini.
-
 Speed configurations will increase credit consumption for all models that apply.
-Details can be found [here](https://developers.openai.com/codex/speed).
-
-[Learn more about credits in ChatGPT Plus and Pro.](https://help.openai.com/en/articles/12642688-using-credits-for-flexible-usage-in-chatgpt-freegopluspro-sora)  
-[Learn more about credits in ChatGPT Business, Enterprise, and Edu.](https://help.openai.com/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans)
+Fast mode consumes credits at a higher rate for supported models. See
+[Speed](https://developers.openai.com/codex/speed) for supported models and rates.
+
+[Learn more about credits in ChatGPT Plus and
+Pro.](https://help.openai.com/en/articles/12642688)
+
+[Learn more about credits in ChatGPT Business, Enterprise, and
+Edu.](https://help.openai.com/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans)
 
 ### What counts as Code Review usage?
 
-Code Review usage applies only when Codex runs reviews through GitHub—for example, when you tag `@Codex` for review in a pull request or enable automatic reviews on your repository. Reviews run locally or outside of GitHub count toward your general usage limits.
+Code Review usage applies only when Codex runs reviews through GitHub—for
+example, when you tag `@Codex` for review in a pull request or enable automatic
+reviews on your repository. Reviews run locally or outside of GitHub count
+toward your general usage limits.
 
 ### What can I do to make my usage limits last longer?
 
-The usage limits and credits above are average rates. You can try the following tips to maximize your limits:
-
-- **Control the size of your prompts.** Be precise with the instructions you give Codex, but remove unnecessary context.
-- **Reduce the size of your AGENTS.md.** If you work on a larger project, you can control how much context you inject through AGENTS.md files by [nesting them within your repository](https://developers.openai.com/codex/guides/agents-md#layer-project-instructions).
-- **Limit the number of MCP servers you use.** Every [MCP](https://developers.openai.com/codex/mcp) you add to Codex adds more context to your messages and uses more of your limit. Disable MCP servers when you don’t need them.
-- **Switch to GPT-5.1-Codex-Mini for routine tasks.** Using the mini model should extend your usage limits by roughly 4x.
+The usage limits and credits above are average rates. You can try the following
+tips to maximize your limits:
+
+- **Control the size of your prompts.** Be precise with the instructions you
+  give Codex, but remove unnecessary context.
+- **Reduce the size of your AGENTS.md.** If you work on a larger project, you
+  can control how much context you inject through AGENTS.md files by [nesting
+  them within your repository](https://developers.openai.com/codex/guides/agents-md#layer-project-instructions).
+- **Limit the number of MCP servers you use.** Every [MCP](https://developers.openai.com/codex/mcp) you add
+  to Codex adds more context to your messages and uses more of your limit.
+  Disable MCP servers when you don’t need them.
+- **Switch to a smaller model for routine tasks.** Using GPT-5.4 or
+  GPT-5.4-mini can extend your local-message usage limits, depending on the
+  model you switch from.
 
 ---
 
@@ -10999,7 +15753,7 @@
 Add a new command-line option `--json` that outputs JSON.
 ```
 
-When you submit a prompt, Codex works in a loop: it calls the model and then performs any actions (file reads, file edits, tool calls, and so on) indicated by the model output. This process ends when the task is complete or you cancel it.
+When you submit a prompt, Codex works in a loop: it calls the model and then performs the actions indicated by the model output, such as file reads, file edits, and tool calls. This process ends when the task is complete or you cancel it.
 
 As with ChatGPT, Codex is only as effective as the instructions you give it. Here are some tips we find helpful when prompting Codex:
 
@@ -11019,6 +15773,14 @@
 - **Local threads** run on your machine. Codex can read and edit your files and run commands, so you can see what changes and use your existing tools. To reduce the risk of unwanted changes outside your workspace, local threads run in a [sandbox](https://developers.openai.com/codex/agent-approvals-security).
 - **Cloud threads** run in an isolated [environment](https://developers.openai.com/codex/cloud/environments). Codex clones your repository and checks out the branch it's working on. Cloud threads are useful when you want to run work in parallel or delegate tasks from another device. To use cloud threads with your repo, push your code to GitHub first. You can also [delegate tasks from your local machine](https://developers.openai.com/codex/ide/cloud-tasks), which includes your current working state.
 
+In the Codex app, you can also start a chat without choosing a project. Chats
+aren't tied to a saved repository or project folder. Use them for research,
+planning, connected-tool workflows, or other work where Codex shouldn't start
+from a codebase. Chats use a Codex-managed `threads` directory under your Codex
+home as their working location. By default, that location is `~/.codex/threads`.
+To change the base location for this state, set `CODEX_HOME`; see
+[Config and state locations](https://developers.openai.com/codex/config-advanced#config-and-state-locations).
+
 ## Context
 
 When you submit a prompt, include context that Codex can use, such as references to relevant files and images. The Codex IDE extension automatically includes the list of open files and the selected text range as context.
@@ -11031,13 +15793,9 @@
 
 # Quickstart
 
-ChatGPT Plus, Pro, Business, Edu, and Enterprise plans include Codex. Using Codex with your ChatGPT subscription gives you access to the latest Codex models and features.
+Every ChatGPT plan includes Codex.
 
 You can also use Codex with API credits by signing in with an OpenAI API key.
-
-For a limited time, **try Codex for free in ChatGPT Free and Go**, or enjoy
-  **2x Codex rate limits** with Plus, Pro, Business and Enterprise
-  subscriptions.
 
 ## Setup
 
@@ -11048,10 +15806,11 @@
 (() => {
   const platform =
     (navigator.userAgentData?.platform || navigator.platform || "").toLowerCase();
-  const isMac =
+  const isDesktopAppPlatform =
     platform.includes("mac") ||
-    /macintosh|mac os x/i.test(navigator.userAgent || "");
-  if (!isMac) return;
+    platform.includes("win") ||
+    /macintosh|mac os x|windows|win64|win32/i.test(navigator.userAgent || "");
+  if (!isDesktopAppPlatform) return;
 
   const shouldPreferApp = () => {
     try {
@@ -11073,12 +15832,15 @@
 
 
 <div slot="app">
-The Codex app is available on macOS (Apple Silicon).
+The Codex app is available on macOS and Windows.
+
+Most Codex app features are available on both platforms. Platform-specific
+exceptions are noted in the relevant docs.
 
 <WorkflowSteps variant="headings">
 1. Download and install the Codex app
 
-    Download the Codex app for Windows or macOS.
+    Download the Codex app for macOS or Windows. Choose the Intel build if you're using an Intel-based Mac.
 
     <div class="text-sm">
       [Get notified for Linux](https://openai.com/form/codex-app/)
@@ -11094,7 +15856,7 @@
 
    Choose a project folder that you want Codex to work in.
 
-If you used the Codex app, CLI, or IDE Extension before you'll see past projects that you worked on.
+    If you used the Codex app, CLI, or IDE Extension before you'll see past projects that you worked on.
 
 4. Send your first message
 
@@ -11105,9 +15867,10 @@
    <ExampleGallery>
      </ExampleGallery>
 
-   If you need more inspiration, check out the [explore section](https://developers.openai.com/codex/explore).
-
-    </WorkflowSteps>
+   If you need more inspiration, explore [Codex use cases](https://developers.openai.com/codex/use-cases).
+   If you're new to Codex, read the [best practices guide](https://developers.openai.com/codex/learn/best-practices).
+
+</WorkflowSteps>
 
 
   </div>
@@ -11141,6 +15904,7 @@
 4. Use Git checkpoints
 
     Codex can modify your codebase, so consider creating Git checkpoints before and after each task so you can easily revert changes if needed.
+    If you're new to Codex, read the [best practices guide](https://developers.openai.com/codex/learn/best-practices).
     
     </WorkflowSteps>
 
@@ -11179,6 +15943,7 @@
 4. Use Git checkpoints
 
     Codex can modify your codebase, so consider creating Git checkpoints before and after each task so you can easily revert changes if needed.
+    If you're new to Codex, read the [best practices guide](https://developers.openai.com/codex/learn/best-practices).
 </WorkflowSteps>
 
     </div>
@@ -11217,8 +15982,111 @@
 
   </div>
 
+
+
+<div class="h-6" aria-hidden="true"></div>
+
+## Next steps
+
+[
+
+<span slot="icon">
+      </span>
+    Use the Codex app to work with your local projects.
+
+](https://developers.openai.com/codex/app)
+
+[
+
+<span slot="icon">
+      </span>
+    Move supported instruction files, MCP server configuration, skills, and
+    subagents into Codex.
+
+](https://developers.openai.com/codex/migrate)
+
 ---
 
+# Remote connections
+
+SSH remote connections are currently in alpha. To enable them today, set
+  `remote_connections = true` in the `[features]` table in
+  `~/.codex/config.toml`. Availability, setup flows, and supported environments
+  may change as the feature improves.
+
+Remote connections let Codex work with projects that live on another
+SSH-accessible machine. Use them when the codebase, credentials, services, or
+build environment you need are available on that host instead of your local
+machine.
+
+Keep the remote host configured with the same security expectations you use for
+normal SSH access: trusted keys, least-privilege accounts, and no
+unauthenticated public listeners.
+
+## Codex app
+
+In the Codex app, add remote projects from an SSH host and run threads against
+the remote filesystem and shell.
+
+
+
+1. Add the host to your SSH config so Codex can auto-discover it.
+
+   ```text
+   Host devbox
+     HostName devbox.example.com
+     User you
+     IdentityFile ~/.ssh/id_ed25519
+   ```
+
+   Codex reads concrete host aliases from `~/.ssh/config`, resolves them with
+   OpenSSH, and ignores pattern-only hosts.
+
+2. Confirm you can SSH to the host from the machine running the Codex app.
+
+   ```bash
+   ssh devbox
+   ```
+
+3. Install and authenticate Codex on the remote host.
+
+   The app starts the remote Codex app server through SSH, using the remote
+   user's login shell. Make sure the `codex` command is available on the
+   remote host's `PATH` in that shell.
+
+4. In the Codex app, open **Settings > Connections**, add or enable the SSH host,
+   then choose a remote project folder.
+
+
+
+If remote connections don't appear yet, enable the alpha feature flag in
+`~/.codex/config.toml`:
+
+```toml
+[features]
+remote_connections = true
+```
+
+Remote project threads run commands, read files, and write changes on the
+remote host.
+
+## Authentication and network exposure
+
+Use SSH port forwarding with local-host WebSocket listeners. Don't expose an
+unauthenticated app-server listener on a shared or public network.
+
+If you need to reach a remote machine outside your current network, use a VPN or
+mesh networking tool such as Tailscale instead of exposing the app server
+directly to the internet.
+
+## See also
+
+- [Codex app settings](https://developers.openai.com/codex/app/settings)
+- [Command line options](https://developers.openai.com/codex/cli/reference)
+- [Authentication](https://developers.openai.com/codex/auth)
+
+---
+
 # Rules
 
 Use rules to control which commands Codex can run outside the sandbox.
@@ -11227,7 +16095,7 @@
 
 ## Create a rules file
 
-1. Create a `.rules` file under `./codex/rules/` (for example, `~/.codex/rules/default.rules`).
+1. Create a `.rules` file under a `rules/` folder next to an active config layer (for example, `~/.codex/rules/default.rules`).
 2. Add a rule. This example prompts before allowing `gh pr view` to run outside the sandbox.
 
    ```python
@@ -11258,7 +16126,9 @@
 
 3. Restart Codex.
 
-Codex scans `rules/` under every [Team Config](https://developers.openai.com/codex/enterprise/admin-setup#team-config) location at startup. When you add a command to the allow list in the TUI, Codex writes to the user layer at `~/.codex/rules/default.rules` so future runs can skip the prompt.
+Codex scans `rules/` under every active config layer at startup, including [Team Config](https://developers.openai.com/codex/enterprise/admin-setup#team-config) locations and the user layer at `~/.codex/rules/`. Project-local rules under `<repo>/.codex/rules/` load only when the project `.codex/` layer is trusted.
+
+When you add a command to the allow list in the TUI, Codex writes to the user layer at `~/.codex/rules/default.rules` so future runs can skip the prompt.
 
 When Smart approvals are enabled (the default), Codex may propose a
 `prefix_rule` for you during escalation requests. Review the suggested prefix
@@ -11366,7 +16236,7 @@
 
 ## TypeScript library
 
-The TypeScript library provides a way to control Codex from within your application that is more comprehensive and flexible than non-interactive mode.
+The TypeScript library provides a way to control Codex from within your application that's more comprehensive and flexible than non-interactive mode.
 
 Use the library server-side; it requires Node.js 18 or later.
 
@@ -11413,6 +16283,54 @@
 
 For more details, check out the [TypeScript repo](https://github.com/openai/codex/tree/main/sdk/typescript).
 
+## Python library
+
+The Python SDK is experimental and controls the local Codex app-server over JSON-RPC. It requires Python 3.10 or later and a local checkout of the open-source Codex repo.
+
+### Installation
+
+From the Codex repo root, install the SDK in editable mode:
+
+```bash
+cd sdk/python
+python -m pip install -e .
+```
+
+For manual local SDK usage, pass `AppServerConfig(codex_bin=...)` to point at a local `codex` binary, or use the repo examples and notebook bootstrap.
+
+### Usage
+
+Start Codex, create a thread, and run a prompt:
+
+```python
+from codex_app_server import Codex
+
+with Codex() as codex:
+    thread = codex.thread_start(model="gpt-5.4")
+    result = thread.run("Make a plan to diagnose and fix the CI failures")
+    print(result.final_response)
+```
+
+Use `AsyncCodex` when your application is already asynchronous:
+
+```python
+import asyncio
+
+from codex_app_server import AsyncCodex
+
+
+async def main() -> None:
+    async with AsyncCodex() as codex:
+        thread = await codex.thread_start(model="gpt-5.4")
+        result = await thread.run("Implement the plan")
+        print(result.final_response)
+
+
+asyncio.run(main())
+```
+
+For more details, check out the [Python repo](https://github.com/openai/codex/tree/main/sdk/python).
+
 ---
 
 # Codex Security
@@ -11443,7 +16361,7 @@
 
 ## Access and prerequisites
 
-Codex Security works with connected GitHub repositories through Codex cloud. OpenAI manages access. If you need access or a repository isn't visible, contact your OpenAI account team and confirm the repository is available through your Codex cloud workspace.
+Codex Security works with connected GitHub repositories through Codex Web. OpenAI manages access. If you need access or a repository isn't visible, contact your OpenAI account team and confirm the repository is available through your Codex Web workspace.
 
 ## Related docs
 
@@ -11713,11 +16631,17 @@
 
 # Agent Skills
 
-Use agent skills to extend Codex with task-specific capabilities. A skill packages instructions, resources, and optional scripts so Codex can follow a workflow reliably. You can share skills across teams or with the community. Skills build on the [open agent skills standard](https://agentskills.io).
+Use agent skills to extend Codex with task-specific capabilities. A skill packages instructions, resources, and optional scripts so Codex can follow a workflow reliably. Skills build on the [open agent skills standard](https://agentskills.io).
+
+Skills are the authoring format for reusable workflows. Plugins are the installable distribution unit for reusable skills and apps in Codex. Use skills to design the workflow itself, then package it as a [plugin](https://developers.openai.com/codex/plugins/build) when you want other developers to install it.
 
 Skills are available in the Codex CLI, IDE extension, and Codex app.
 
-Skills use **progressive disclosure** to manage context efficiently: Codex starts with each skill's metadata (`name`, `description`, file path, and optional metadata from `agents/openai.yaml`). Codex loads the full `SKILL.md` instructions only when it decides to use a skill.
+Skills use **progressive disclosure** to manage context efficiently: Codex starts with each skill's name, description, and file path. Codex loads the full `SKILL.md` instructions only when it decides to use a skill.
+
+Codex includes an initial list of available skills in context so it can choose the right skill for a task. To avoid crowding out the rest of the prompt, this list is capped at roughly 2% of the model’s context window, or 8,000 characters when the context window is unknown. If many skills are installed, Codex shortens skill descriptions first. For very large skill sets, some skills may be omitted from the initial list, and Codex will show a warning.
+
+This budget applies only to the initial skills list. When Codex selects a skill, it still reads the full SKILL.md instructions for that skill.
 
 A skill is a directory with a `SKILL.md` file plus optional scripts and references. The `SKILL.md` file must include `name` and `description`.
 
@@ -11728,7 +16652,7 @@
 1. **Explicit invocation:** Include the skill directly in your prompt. In CLI/IDE, run `/skills` or type `$` to mention a skill.
 2. **Implicit invocation:** Codex can choose a skill when your task matches the skill `description`.
 
-Because implicit matching depends on `description`, write descriptions with clear scope and boundaries.
+Because implicit matching depends on `description`, write concise descriptions with clear scope and boundaries. Front-load the key use case and trigger words so Codex can still match the skill if descriptions are shortened.
 
 ## Create a skill
 
@@ -11768,15 +16692,35 @@
 
 Codex supports symlinked skill folders and follows the symlink target when scanning these locations.
 
-## Install skills
-
-To install skills beyond the built-ins, use `$skill-installer`. For example, to install the `$linear` skill:
+These locations are for authoring and local discovery. When you want to
+distribute reusable skills beyond a single repo, or optionally bundle them with
+app integrations, use [plugins](https://developers.openai.com/codex/plugins/build).
+
+## Distribute skills with plugins
+
+Direct skill folders are best for local authoring and repo-scoped workflows. If
+you want to distribute a reusable skill, bundle two or more skills together, or
+ship a skill alongside an app integration, package them as a
+[plugin](https://developers.openai.com/codex/plugins/build).
+
+Plugins can include one or more skills. They can also optionally bundle app
+mappings, MCP server configuration, and presentation assets in a single
+package.
+
+## Install curated skills for local use
+
+To add curated skills beyond the built-ins for your own local Codex setup, use `$skill-installer`. For example, to install the `$linear` skill:
 
 ```bash
 $skill-installer linear
 ```
 
-You can also prompt the installer to download skills from other repositories. Codex detects newly installed skills automatically; if one doesn't appear, restart Codex.
+You can also prompt the installer to download skills from other repositories.
+Codex detects newly installed skills automatically; if one doesn't appear,
+restart Codex.
+
+Use this for local setup and experimentation. For reusable distribution of your
+own skills, prefer plugins.
 
 ## Enable or disable skills
 
@@ -11835,18 +16779,369 @@
 Codex offers the ability to increase the speed of the model for increased
 credit consumption.
 
-Fast mode is currently supported on GPT-5.4. When enabled, speed is increased
-by 1.5x and credits are consumed at a 2x rate.
-
-Enable it by typing `/fast`. It is available in Codex IDE Extensions, Codex
-CLI, and the Codex app.
+Fast mode increases supported model speed by 1.5x and consumes credits at a
+higher rate than Standard mode. It currently supports GPT-5.5 and GPT-5.4,
+consuming credits at 2.5x the Standard rate for GPT-5.5 and 2x the Standard
+rate for GPT-5.4.
+
+Use `/fast on`, `/fast off`, or `/fast status` in the CLI to change or inspect
+the current setting. You can also persist the default with `service_tier =
+"fast"` plus `[features].fast_mode = true` in `config.toml`. Fast mode is
+available in the Codex IDE extension, Codex CLI, and the Codex app when you
+sign in with ChatGPT. With an API key, Codex uses standard API pricing instead
+and you can't use Fast mode credits.
 
 ## Codex-Spark
 
-GPT-5.3-Codex-Spark is a separate fast, less-capable Codex model optimized for near-instant, real-time coding iteration. Unlike fast mode, which speeds up GPT-5.4 at a higher credit rate,
-Codex-Spark is its own model choice and has its own usage limits.
+GPT-5.3-Codex-Spark is a separate fast, less-capable Codex model optimized for
+near-instant, real-time coding iteration. Unlike fast mode, which speeds up a
+supported model at a higher credit rate, Codex-Spark is its own model choice
+and has its own usage limits.
 
 During research preview Codex-Spark is only available for ChatGPT Pro subscribers.
+
+---
+
+# Subagents
+
+Codex can run subagent workflows by spawning specialized agents in parallel and then collecting their results in one response. This can be particularly helpful for complex tasks that are highly parallel, such as codebase exploration or implementing a multi-step feature plan.
+
+With subagent workflows, you can also define your own custom agents with different model configurations and instructions depending on the task.
+
+For the concepts and tradeoffs behind subagent workflows, including context pollution, context rot, and model-selection guidance, see [Subagent concepts](https://developers.openai.com/codex/concepts/subagents).
+
+## Availability
+
+Current Codex releases enable subagent workflows by default.
+
+Subagent activity is currently surfaced in the Codex app and CLI. Visibility
+  in the IDE Extension is coming soon.
+
+Codex only spawns subagents when you explicitly ask it to. Because each
+subagent does its own model and tool work, subagent workflows consume more
+tokens than comparable single-agent runs.
+
+## Typical workflow
+
+Codex handles orchestration across agents, including spawning new subagents,
+routing follow-up instructions, waiting for results, and closing agent
+threads.
+
+When many agents are running, Codex waits until all requested results are
+available, then returns a consolidated response.
+
+Codex only spawns a new agent when you explicitly ask it to do so.
+
+To see it in action, try the following prompt on your project:
+
+```text
+I would like to review the following points on the current PR (this branch vs main). Spawn one agent per point, wait for all of them, and summarize the result for each point.
+1. Security issue
+2. Code quality
+3. Bugs
+4. Race
+5. Test flakiness
+6. Maintainability of the code
+```
+
+## Managing subagents
+
+- Use `/agent` in the CLI to switch between active agent threads and inspect the ongoing thread.
+- Ask Codex directly to steer a running subagent, stop it, or close completed agent threads.
+
+## Approvals and sandbox controls
+
+Subagents inherit your current sandbox policy.
+
+In interactive CLI sessions, approval requests can surface from inactive agent
+threads even while you are looking at the main thread. The approval overlay
+shows the source thread label, and you can press `o` to open that thread before
+you approve, reject, or answer the request.
+
+In non-interactive flows, or whenever a run can't surface a fresh approval, an
+action that needs new approval fails and Codex surfaces the error back to the
+parent workflow.
+
+Codex also reapplies the parent turn's live runtime overrides when it spawns a
+child. That includes sandbox and approval choices you set interactively during
+the session, such as `/approvals` changes or `--yolo`, even if the selected
+custom agent file sets different defaults.
+
+You can also override the sandbox configuration for individual [custom agents](#custom-agents), such as explicitly marking one to work in read-only mode.
+
+## Custom agents
+
+Codex ships with built-in agents:
+
+- `default`: general-purpose fallback agent.
+- `worker`: execution-focused agent for implementation and fixes.
+- `explorer`: read-heavy codebase exploration agent.
+
+To define your own custom agents, add standalone TOML files under
+`~/.codex/agents/` for personal agents or `.codex/agents/` for project-scoped
+agents.
+
+Each file defines one custom agent. Codex loads these files as configuration
+layers for spawned sessions, so custom agents can override the same settings as
+a normal Codex session config. That can feel heavier than a dedicated agent
+manifest, and the format may evolve as authoring and sharing mature.
+
+Every standalone custom agent file must define:
+
+- `name`
+- `description`
+- `developer_instructions`
+
+Optional fields such as `nickname_candidates`, `model`,
+`model_reasoning_effort`, `sandbox_mode`, `mcp_servers`, and `skills.config`
+inherit from the parent session when you omit them.
+
+### Global settings
+
+Global subagent settings still live under `[agents]` in your [configuration](https://developers.openai.com/codex/config-basic#configuration-precedence).
+
+| Field                            | Type   | Required | Purpose                                                    |
+| -------------------------------- | ------ | :------: | ---------------------------------------------------------- |
+| `agents.max_threads`             | number |    No    | Concurrent open agent thread cap.                          |
+| `agents.max_depth`               | number |    No    | Spawned agent nesting depth (root session starts at 0).    |
+| `agents.job_max_runtime_seconds` | number |    No    | Default timeout per worker for `spawn_agents_on_csv` jobs. |
+
+**Notes:**
+
+- `agents.max_threads` defaults to `6` when you leave it unset.
+- `agents.max_depth` defaults to `1`, which allows a direct child agent to spawn but prevents deeper nesting. Keep the default unless you specifically need recursive delegation. Raising this value can turn broad delegation instructions into repeated fan-out, which increases token usage, latency, and local resource consumption. `agents.max_threads` still caps concurrent open threads, but it doesn't remove the cost and predictability risks of deeper recursion.
+- `agents.job_max_runtime_seconds` is optional. When you leave it unset, `spawn_agents_on_csv` falls back to its per-call default timeout of 1800 seconds per worker.
+- If a custom agent name matches a built-in agent such as `explorer`, your custom agent takes precedence.
+
+### Custom agent file schema
+
+| Field                    | Type     | Required | Purpose                                                         |
+| ------------------------ | -------- | :------: | --------------------------------------------------------------- |
+| `name`                   | string   |   Yes    | Agent name Codex uses when spawning or referring to this agent. |
+| `description`            | string   |   Yes    | Human-facing guidance for when Codex should use this agent.     |
+| `developer_instructions` | string   |   Yes    | Core instructions that define the agent's behavior.             |
+| `nickname_candidates`    | string[] |    No    | Optional pool of display nicknames for spawned agents.          |
+
+You can also include other supported `config.toml` keys in a custom agent file, such as `model`, `model_reasoning_effort`, `sandbox_mode`, `mcp_servers`, and `skills.config`.
+
+Codex identifies the custom agent by its `name` field. Matching the filename to
+the agent name is the simplest convention, but the `name` field is the source
+of truth.
+
+### Display nicknames
+
+Use `nickname_candidates` when you want Codex to assign more readable display
+names to spawned agents. This is especially helpful when you run many
+instances of the same custom agent and want the UI to show distinct labels
+instead of repeating the same agent name.
+
+Nicknames are presentation-only. Codex still identifies and spawns the agent by
+its `name`.
+
+Nickname candidates must be a non-empty list of unique names. Each nickname can
+use ASCII letters, digits, spaces, hyphens, and underscores.
+
+Example:
+
+```toml
+name = "reviewer"
+description = "PR reviewer focused on correctness, security, and missing tests."
+developer_instructions = """
+Review code like an owner.
+Prioritize correctness, security, behavior regressions, and missing test coverage.
+"""
+nickname_candidates = ["Atlas", "Delta", "Echo"]
+```
+
+In practice, the Codex app and CLI can show the nicknames where agent activity
+appears, while the underlying agent type stays
+`reviewer`.
+
+### Example custom agents
+
+The best custom agents are narrow and opinionated. Give each one clear job, a
+tool surface that matches that job, and instructions that keep it from
+drifting into adjacent work.
+
+#### Example 1: PR review
+
+This pattern splits review across three focused custom agents:
+
+- `pr_explorer` maps the codebase and gathers evidence.
+- `reviewer` looks for correctness, security, and test risks.
+- `docs_researcher` checks framework or API documentation through a dedicated MCP server.
+
+Project config (`.codex/config.toml`):
+
+```toml
+[agents]
+max_threads = 6
+max_depth = 1
+```
+
+`.codex/agents/pr-explorer.toml`:
+
+```toml
+name = "pr_explorer"
+description = "Read-only codebase explorer for gathering evidence before changes are proposed."
+model = "gpt-5.3-codex-spark"
+model_reasoning_effort = "medium"
+sandbox_mode = "read-only"
+developer_instructions = """
+Stay in exploration mode.
+Trace the real execution path, cite files and symbols, and avoid proposing fixes unless the parent agent asks for them.
+Prefer fast search and targeted file reads over broad scans.
+"""
+```
+
+`.codex/agents/reviewer.toml`:
+
+```toml
+name = "reviewer"
+description = "PR reviewer focused on correctness, security, and missing tests."
+model = "gpt-5.4"
+model_reasoning_effort = "high"
+sandbox_mode = "read-only"
+developer_instructions = """
+Review code like an owner.
+Prioritize correctness, security, behavior regressions, and missing test coverage.
+Lead with concrete findings, include reproduction steps when possible, and avoid style-only comments unless they hide a real bug.
+"""
+```
+
+`.codex/agents/docs-researcher.toml`:
+
+```toml
+name = "docs_researcher"
+description = "Documentation specialist that uses the docs MCP server to verify APIs and framework behavior."
+model = "gpt-5.4-mini"
+model_reasoning_effort = "medium"
+sandbox_mode = "read-only"
+developer_instructions = """
+Use the docs MCP server to confirm APIs, options, and version-specific behavior.
+Return concise answers with links or exact references when available.
+Do not make code changes.
+"""
+
+[mcp_servers.openaiDeveloperDocs]
+url = "https://developers.openai.com/mcp"
+```
+
+This setup works well for prompts like:
+
+```text
+Review this branch against main. Have pr_explorer map the affected code paths, reviewer find real risks, and docs_researcher verify the framework APIs that the patch relies on.
+```
+
+## Process CSV batches with subagents (experimental)
+
+This workflow is experimental and may change as subagent support evolves.
+Use `spawn_agents_on_csv` when you have many similar tasks that map to one row per work item. Codex reads the CSV, spawns one worker subagent per row, waits for the full batch to finish, and exports the combined results to CSV.
+
+This works well for repeated audits such as:
+
+- reviewing one file, package, or service per row
+- checking a list of incidents, PRs, or migration targets
+- generating structured summaries for many similar inputs
+
+The tool accepts:
+
+- `csv_path` for the source CSV
+- `instruction` for the worker prompt template, using `{column_name}` placeholders
+- `id_column` when you want stable item ids from a specific column
+- `output_schema` when each worker should return a JSON object with a fixed shape
+- `output_csv_path`, `max_concurrency`, and `max_runtime_seconds` for job control
+
+Each worker must call `report_agent_job_result` exactly once. If a worker exits without reporting a result, Codex marks that row with an error in the exported CSV.
+
+Example prompt:
+
+```text
+Create /tmp/components.csv with columns path,owner and one row per frontend component.
+
+Then call spawn_agents_on_csv with:
+- csv_path: /tmp/components.csv
+- id_column: path
+- instruction: "Review {path} owned by {owner}. Return JSON with keys path, risk, summary, and follow_up via report_agent_job_result."
+- output_csv_path: /tmp/components-review.csv
+- output_schema: an object with required string fields path, risk, summary, and follow_up
+```
+
+When you run this through `codex exec`, Codex shows a single-line progress update on `stderr` while the batch is running. The exported CSV includes the original row data plus metadata such as `job_id`, `item_id`, `status`, `last_error`, and `result_json`.
+
+Related runtime settings:
+
+- `agents.max_threads` caps how many agent threads can stay open concurrently.
+- `agents.job_max_runtime_seconds` sets the default per-worker timeout for CSV fan-out jobs. A per-call `max_runtime_seconds` override takes precedence.
+- `sqlite_home` controls where Codex stores the SQLite-backed state used for agent jobs and their exported results.
+
+#### Example 2: Frontend integration debugging
+
+This pattern is useful for UI regressions, flaky browser flows, or integration bugs that cross application code and the running product.
+
+Project config (`.codex/config.toml`):
+
+```toml
+[agents]
+max_threads = 6
+max_depth = 1
+```
+
+`.codex/agents/code-mapper.toml`:
+
+```toml
+name = "code_mapper"
+description = "Read-only codebase explorer for locating the relevant frontend and backend code paths."
+model = "gpt-5.4-mini"
+model_reasoning_effort = "medium"
+sandbox_mode = "read-only"
+developer_instructions = """
+Map the code that owns the failing UI flow.
+Identify entry points, state transitions, and likely files before the worker starts editing.
+"""
+```
+
+`.codex/agents/browser-debugger.toml`:
+
+```toml
+name = "browser_debugger"
+description = "UI debugger that uses browser tooling to reproduce issues and capture evidence."
+model = "gpt-5.4"
+model_reasoning_effort = "high"
+sandbox_mode = "workspace-write"
+developer_instructions = """
+Reproduce the issue in the browser, capture exact steps, and report what the UI actually does.
+Use browser tooling for screenshots, console output, and network evidence.
+Do not edit application code.
+"""
+
+[mcp_servers.chrome_devtools]
+url = "http://localhost:3000/mcp"
+startup_timeout_sec = 20
+```
+
+`.codex/agents/ui-fixer.toml`:
+
+```toml
+name = "ui_fixer"
+description = "Implementation-focused agent for small, targeted fixes after the issue is understood."
+model = "gpt-5.3-codex-spark"
+model_reasoning_effort = "medium"
+developer_instructions = """
+Own the fix once the issue is reproduced.
+Make the smallest defensible change, keep unrelated files untouched, and validate only the behavior you changed.
+"""
+
+[[skills.config]]
+path = "/Users/me/.agents/skills/docs-editor/SKILL.md"
+enabled = false
+```
+
+This setup works well for prompts like:
+
+```text
+Investigate why the settings modal fails to save. Have browser_debugger reproduce it, code_mapper trace the responsible code path, and ui_fixer implement the smallest fix once the failure mode is clear.
+```
 
 ---
 
@@ -11859,29 +17154,81 @@
 
 # Windows
 
-The easiest way to use Codex on Windows is to use the [Codex app](https://developers.openai.com/codex/app/windows). You can also [set up the IDE extension](https://developers.openai.com/codex/ide) or [install the CLI](https://developers.openai.com/codex/cli) and run it from PowerShell.
+Use Codex on Windows with the native [Codex app](https://developers.openai.com/codex/app/windows), the
+[CLI](https://developers.openai.com/codex/cli), or the [IDE extension](https://developers.openai.com/codex/ide).
+
+The Codex app on Windows supports core workflows such as parallel agent threads,
+worktrees, automations, Git functionality, the in-app browser, artifact previews,
+plugins, and skills.
 
 <div class="mb-8">
   </div>
 
-When you run Codex natively on Windows, agent mode uses a [Windows sandbox](#windows-sandbox) to block filesystem writes outside the working folder and prevent network access without your explicit approval. [Learn more below](#windows-sandbox).
-
-If you prefer to have Codex use [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install) (WSL2), [read the instructions](#windows-subsystem-for-linux) below.
+Depending on the surface and your setup, Codex can run on Windows in three
+practical ways:
+
+- natively on Windows with the stronger `elevated` sandbox,
+- natively on Windows with the fallback `unelevated` sandbox,
+- or inside [Windows Subsystem for Linux 2](https://learn.microsoft.com/en-us/windows/wsl/install) (WSL2), which uses the Linux sandbox implementation.
 
 ## Windows sandbox
 
-Native Windows sandbox support includes two modes that you can configure in `config.toml`:
+When you run Codex natively on Windows, agent mode uses a Windows sandbox to
+block filesystem writes outside the working folder and prevent network access
+without your explicit approval.
+
+Native Windows sandbox support includes two modes that you can configure in
+`config.toml`:
 
 ```toml
 [windows]
-sandbox = "unelevated" # or "elevated"
-```
-
-How `elevated` mode works:
-
-- Uses a Restricted Token approach with filesystem ACLs to limit which files the sandbox can write to.
-- Runs commands as a dedicated Windows Sandbox User.
-- Limits network access by installing Windows Firewall rules.
+sandbox = "elevated" # or "unelevated"
+```
+
+`elevated` is the preferred native Windows sandbox. It uses dedicated
+lower-privilege sandbox users, filesystem permission boundaries, firewall
+rules, and local policy changes needed for commands that run in the sandbox.
+
+`unelevated` is the fallback native Windows sandbox. It runs commands with a
+restricted Windows token derived from your current user, applies ACL-based
+filesystem boundaries, and uses environment-level offline controls instead of
+the dedicated offline-user firewall rule. It's weaker than `elevated`, but it
+is still useful when administrator-approved setup is blocked by local or
+enterprise policy.
+
+If both modes are available, use `elevated`. If the default native sandbox
+doesn't work in your environment, use `unelevated` as a fallback while you
+troubleshoot the setup.
+
+By default, both sandbox modes also use a private desktop for stronger UI
+isolation. Set `windows.sandbox_private_desktop = false` only if you need the
+older `Winsta0\\Default` behavior for compatibility.
+
+### Sandbox permissions
+
+Running Codex in full access mode means Codex is not limited to your project
+  directory and might perform unintentional destructive actions that can lead to
+  data loss. For safer automation, keep sandbox boundaries in place and use
+  [rules](https://developers.openai.com/codex/rules) for specific exceptions, or set your [approval policy to
+  never](https://developers.openai.com/codex/agent-approvals-security#run-without-approval-prompts) to have
+  Codex attempt to solve problems without asking for escalated permissions,
+  based on your [approval and security setup](https://developers.openai.com/codex/agent-approvals-security).
+
+### Windows version matrix
+
+| Windows version                  | Support level   | Notes                                                                                                                                                                                 |
+| -------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
+| Windows 11                       | Recommended     | Best baseline for Codex on Windows. Use this if you are standardizing an enterprise deployment.                                                                                       |
+| Recent, fully updated Windows 10 | Best effort     | Can work, but is less reliable than Windows 11. For Windows 10, Codex depends on modern console support, including ConPTY. In practice, Windows 10 version 1809 or newer is required. |
+| Older Windows 10 builds          | Not recommended | More likely to miss required console components such as ConPTY and more likely to fail in enterprise setups.                                                                          |
+
+Additional environment assumptions:
+
+- `winget` should be available. If it's missing, update Windows or install
+  the Windows Package Manager before setting up Codex.
+- The recommended native sandbox depends on administrator-approved setup.
+- Some enterprise-managed devices block the required setup steps even when the
+  OS version itself is acceptable.
 
 ### Grant sandbox read access
 
@@ -11893,7 +17240,19 @@
 
 The path must be an existing absolute directory. After the command succeeds, later commands that run in the sandbox can read that directory during the current session.
 
+Use the native Windows sandbox by default. The native Windows sandbox offers the best performance and highest speeds while keeping the same security. Choose WSL2 when you
+need a Linux-native environment on Windows, when your workflow already lives in
+WSL2, or when neither native Windows sandbox mode meets your needs.
+
 ## Windows Subsystem for Linux
+
+If you choose WSL2, Codex runs inside the Linux environment instead of using the
+native Windows sandbox. This is useful if you need Linux-native tooling on
+Windows, if your repositories and developer workflow already live in WSL2, or
+if neither native Windows sandbox mode works for your environment.
+
+WSL1 was supported through Codex `0.114`. Starting in Codex `0.115`, the Linux
+sandbox moved to `bubblewrap`, so WSL1 is no longer supported.
 
 ### Launch VS Code from inside WSL
 
@@ -11929,6 +17288,10 @@
 If you don't see "WSL: ..." in the status bar, press `Ctrl+Shift+P`, pick
   `WSL: Reopen Folder in WSL`, and keep your repository under `/home/...` (not
   `C:\`) for best performance.
+
+If the Windows app or project picker does not show your WSL repository, type
+  <code>\\wsl$</code> into the file picker or Explorer, then navigate to your
+  distro's home directory.
 
 ### Use Codex CLI with WSL
 
@@ -11969,7 +17332,132 @@
 
 ## Troubleshooting and FAQ
 
-#### Installed extension, but it's unresponsive
+If you are troubleshooting a managed Windows machine, start with the native
+sandbox mode, Windows version, and any policy error shown by Codex. Most native
+Windows support issues come from sandbox setup, logon rights, or filesystem
+permissions rather than from the editor itself.
+
+My native sandbox setup failed
+
+If Codex cannot complete the `elevated` sandbox setup, the most common causes
+are:
+
+- the Windows UAC or administrator prompt was declined,
+- the machine does not allow local user or group creation,
+- the machine does not allow firewall rule changes,
+- the machine blocks the logon rights needed by the sandbox users,
+- or another enterprise policy blocks part of the setup flow.
+
+What to try:
+
+1. Try the `elevated` sandbox setup again and approve the administrator prompt
+   if your environment allows it.
+2. If your company laptop blocks this, ask your IT team whether the machine
+   allows administrator-approved setup for local user/group creation, firewall
+   configuration, and the required sandbox-user logon rights.
+3. If the default setup still fails, use the `unelevated` sandbox so you can
+   continue working while the issue is investigated.
+
+Codex switched me to the unelevated sandbox
+
+This means Codex could not finish the stronger `elevated` sandbox setup on your
+machine.
+
+- Codex can still run in a sandboxed mode.
+- It still applies ACL-based filesystem boundaries, but it does not use the
+  separate sandbox-user boundary from `elevated` and has weaker network
+  isolation.
+- This is a useful fallback, but not the preferred long-term enterprise
+  configuration.
+
+If you are on a managed enterprise laptop, the best long-term fix is usually to
+get the `elevated` sandbox working with help from your IT team.
+
+I see Windows error 1385
+
+If sandboxed commands fail with error `1385`, Windows is denying the logon type
+the sandbox user needs in order to start the command.
+
+In practice, this usually means Codex created the sandbox users successfully,
+but Windows policy is still preventing those users from launching sandboxed
+commands.
+
+What to do:
+
+1. Ask your IT team whether the device policy grants the required logon rights
+   to the Codex-created sandbox users.
+2. Compare group policy or OU differences if the issue affects only some
+   machines or teams.
+3. If you need to keep working immediately, use the `unelevated` sandbox while
+   the policy issue is investigated.
+4. Send `CODEX_HOME/.sandbox/sandbox.log` along with your Windows version and a
+   short description of the failure.
+
+Codex warns that some folders are writable by Everyone
+
+Codex may warn that some folders are writable by `Everyone`.
+
+If you see this warning, Windows permissions on those folders are too broad for
+the sandbox to fully protect them.
+
+What to do:
+
+1. Review the folders Codex lists in the warning.
+2. Remove `Everyone` write access from those folders if that is appropriate in
+   your environment.
+3. Restart Codex or re-run the sandbox setup after those permissions are
+   corrected.
+
+If you are not sure how to change those permissions, ask your IT team for help.
+
+Sandboxed commands cannot reach the network
+
+Some Codex tasks are intentionally run without outbound network access,
+depending on the permissions mode in use.
+
+If a task fails because it cannot reach the network:
+
+1. Check whether the task was supposed to run with network disabled.
+2. If you expected network access, restart Codex and try again.
+3. If the issue keeps happening, collect the sandbox log so the team can check
+   whether the machine is in a partial or broken sandbox state.
+
+Sandboxing worked before and then stopped
+
+This can happen after:
+
+- moving a repo or workspace,
+- changing machine permissions,
+- changing Windows policies,
+- or other system configuration changes.
+
+What to try:
+
+1. Restart Codex.
+2. Try the `elevated` sandbox setup again.
+3. If that does not fix it, use the `unelevated` sandbox as a temporary
+   fallback.
+4. Collect the sandbox log for review.
+
+I need to send diagnostics to OpenAI
+
+If you still have problems, send:
+
+- `CODEX_HOME/.sandbox/sandbox.log`
+
+It is also helpful to include:
+
+- a short description of what you were trying to do,
+- whether the `elevated` sandbox failed or the `unelevated` sandbox was used,
+- any error message shown in the app,
+- whether you saw `1385` or another Windows or PowerShell error,
+- and whether you are on Windows 11 or Windows 10.
+
+Do not send:
+
+- the contents of `CODEX_HOME/.sandbox-secrets/`
+
+The IDE extension is installed but unresponsive
 
 Your system may be missing C++ development tools, which some native dependencies require:
 
@@ -11979,7 +17467,7 @@
 
 Then fully restart VS Code after installation.
 
-#### If it feels slow on large repositories
+Large repositories feel slow in WSL
 
 - Make sure you're not working under <code>/mnt/c</code>. Move the repository to WSL (for example, <code>~/code/...</code>).
 - Increase memory and CPU for WSL if needed; update WSL to the latest version:
@@ -11988,7 +17476,7 @@
   wsl --shutdown
   ```
 
-#### VS Code in WSL can't find `codex`
+VS Code in WSL cannot find codex
 
 Verify the binary exists and is on PATH inside WSL:
 

```
#### https://developers.openai.com/codex/agent-approvals-security.md

```diff
--- a/https://developers.openai.com/codex/agent-approvals-security.md
+++ b/https://developers.openai.com/codex/agent-approvals-security.md
@@ -9,7 +9,8 @@
 By default, the agent runs with network access turned off. Locally, Codex uses an OS-enforced sandbox that limits what it can touch (typically to the current workspace), plus an approval policy that controls when it must stop and ask you before acting.
 
 For a high-level explanation of how sandboxing works across the Codex app, IDE
-extension, and CLI, see [Sandboxing](https://developers.openai.com/codex/concepts/sandboxing).
+extension, and CLI, see [sandboxing](https://developers.openai.com/codex/concepts/sandboxing).
+For a broader enterprise security overview, see the [Codex security white paper](https://trust.openai.com/?itemUid=382f924d-54f3-43a8-a9df-c39e6c959958&source=click).
 
 ## Sandbox and approvals
 
@@ -23,7 +24,7 @@
 - **Codex cloud**: Runs in isolated OpenAI-managed containers, preventing access to your host system or unrelated data. Uses a two-phase runtime model: setup runs before the agent phase and can access the network to install specified dependencies, then the agent phase runs offline by default unless you enable internet access for that environment. Secrets configured for cloud environments are available only during setup and are removed before the agent phase starts.
 - **Codex CLI / IDE extension**: OS-level mechanisms enforce sandbox policies. Defaults include no network access and write permissions limited to the active workspace. You can configure the sandbox, approval policy, and network settings based on your risk tolerance.
 
-In the `Auto` preset (for example, `--full-auto`), Codex can read files, make edits, and run commands in the working directory automatically.
+In the `Auto` preset (for example, `--sandbox workspace-write --ask-for-approval on-request`), Codex can read files, make edits, and run commands in the working directory automatically.
 
 Codex asks for approval to edit files outside the workspace or to run commands that require network access. If you want to chat or plan without making changes, switch to `read-only` mode with the `/permissions` command.
 
@@ -72,6 +73,26 @@
 - `<writable_root>/.codex` is protected as read-only when it exists as a directory.
 - Protection is recursive, so everything under those paths is read-only.
 
+### Deny reads with filesystem profiles
+
+Named permission profiles can also deny reads for exact paths or glob patterns.
+This is useful when a workspace should stay writable but specific sensitive
+files, such as local environment files, must stay unreadable:
+
+```toml
+default_permissions = "workspace"
+
+[permissions.workspace.filesystem]
+":project_roots" = { "." = "write", "**/*.env" = "none" }
+glob_scan_max_depth = 3
+```
+
+Use `"none"` for paths or globs that Codex shouldn't read. The sandbox policy
+evaluates globs for local macOS and Linux command execution. On platforms that
+pre-expand glob matches before the sandbox starts, set `glob_scan_max_depth` for
+unbounded `**` patterns, or list explicit depths such as `*.env`, `*/*.env`, and
+`*/*/*.env`.
+
 ### Run without approval prompts
 
 You can disable approval prompts with `--ask-for-approval never` or `-a never` (shorthand).
@@ -80,19 +101,62 @@
 
 If you need Codex to read files, make edits, and run commands with network access without approval prompts, use `--sandbox danger-full-access` (or the `--dangerously-bypass-approvals-and-sandbox` flag). Use caution before doing so.
 
-For a middle ground, `approval_policy = { reject = { ... } }` lets you auto-reject specific approval prompt categories (sandbox escalation, execpolicy-rule prompts, or MCP elicitations) while keeping other prompts interactive.
+For a middle ground, `approval_policy = { granular = { ... } }` lets you keep specific approval prompt categories interactive while automatically rejecting others. The granular policy covers sandbox approvals, execpolicy-rule prompts, MCP prompts, `request_permissions` prompts, and skill-script approvals.
+
+### Automatic approval reviews
+
+By default, approval requests route to you:
+
+```toml
+approvals_reviewer = "user"
+```
+
+Automatic approval reviews apply when approvals are interactive, such as
+`approval_policy = "on-request"` or a granular approval policy. Set
+`approvals_reviewer = "auto_review"` to route eligible approval requests
+through a reviewer agent before Codex runs the request:
+
+```toml
+approval_policy = "on-request"
+approvals_reviewer = "auto_review"
+```
+
+The reviewer evaluates only actions that already need approval, such as sandbox
+escalations, network requests, `request_permissions` prompts, or side-effecting
+app and MCP tool calls. Actions that stay inside the sandbox continue without an
+extra review step.
+
+The reviewer policy checks for data exfiltration, credential probing, persistent
+security weakening, and destructive actions. Low-risk and medium-risk actions
+can proceed when policy allows them. The policy denies critical-risk actions.
+High-risk actions require enough user authorization and no matching deny rule.
+Timeouts, parse failures, and review errors fail closed.
+
+The [default reviewer policy](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md)
+is in the open-source Codex repository. Enterprises can replace its
+tenant-specific section with `guardian_policy_config` in managed requirements.
+Local `[auto_review].policy` text is also supported, but managed requirements
+take precedence. For setup details, see
+[Managed configuration](https://developers.openai.com/codex/enterprise/managed-configuration#configure-automatic-review-policy).
+
+In the Codex app, these reviews appear as automatic review items with a status such
+as Reviewing, Approved, Denied, Stopped, or Timed out. They can also include a
+risk level for the reviewed request.
+
+Automatic review uses extra model calls, so it can add to Codex usage. Admins
+can constrain it with `allowed_approvals_reviewers`.
 
 ### Common sandbox and approval combinations
 
-| Intent                                                            | Flags                                                          | Effect                                                                                                                                           |
-| ----------------------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
-| Auto (preset)                                                     | _no flags needed_ or `--full-auto`                             | Codex can read files, make edits, and run commands in the workspace. Codex requires approval to edit outside the workspace or to access network. |
-| Safe read-only browsing                                           | `--sandbox read-only --ask-for-approval on-request`            | Codex can read files and answer questions. Codex requires approval to make edits, run commands, or access network.                               |
-| Read-only non-interactive (CI)                                    | `--sandbox read-only --ask-for-approval never`                 | Codex can only read files; never asks for approval.                                                                                              |
-| Automatically edit but ask for approval to run untrusted commands | `--sandbox workspace-write --ask-for-approval untrusted`       | Codex can read and edit files but asks for approval before running untrusted commands.                                                           |
-| Dangerous full access                                             | `--dangerously-bypass-approvals-and-sandbox` (alias: `--yolo`) | <ElevatedRiskBadge /> No sandbox; no approvals _(not recommended)_                                                                               |
-
-`--full-auto` is a convenience alias for `--sandbox workspace-write --ask-for-approval on-request`.
+| Intent                                                            | Flags                                                                          | Effect                                                                                                                                           |
+| ----------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
+| Auto (preset)                                                     | _no flags needed_ or `--sandbox workspace-write --ask-for-approval on-request` | Codex can read files, make edits, and run commands in the workspace. Codex requires approval to edit outside the workspace or to access network. |
+| Safe read-only browsing                                           | `--sandbox read-only --ask-for-approval on-request`                            | Codex can read files and answer questions. Codex requires approval to make edits, run commands, or access network.                               |
+| Read-only non-interactive (CI)                                    | `--sandbox read-only --ask-for-approval never`                                 | Codex can only read files; never asks for approval.                                                                                              |
+| Automatically edit but ask for approval to run untrusted commands | `--sandbox workspace-write --ask-for-approval untrusted`                       | Codex can read and edit files but asks for approval before running untrusted commands.                                                           |
+| Dangerous full access                                             | `--dangerously-bypass-approvals-and-sandbox` (alias: `--yolo`)                 | <ElevatedRiskBadge /> No sandbox; no approvals _(not recommended)_                                                                               |
+
+For non-interactive runs, use `codex exec --sandbox workspace-write`; Codex keeps older `codex exec --full-auto` invocations as a deprecated compatibility path and prints a warning.
 
 With `--ask-for-approval untrusted`, Codex runs only known-safe read operations automatically. Commands that can mutate state or trigger external execution paths (for example, destructive Git operations or Git output/config-override flags) require approval.
 
@@ -110,8 +174,14 @@
 [sandbox_workspace_write]
 network_access = true
 
-# Optional: granular approval prompt auto-rejection
-# approval_policy = { reject = { sandbox_approval = true, rules = false, mcp_elicitations = false } }
+# Optional: granular approval policy
+# approval_policy = { granular = {
+#   sandbox_approval = true,
+#   rules = true,
+#   mcp_elicitations = true,
+#   request_permissions = false,
+#   skill_approval = false
+# } }
 ```
 
 You can also save presets as profiles, then select them with `codex --profile <name>`:
@@ -132,9 +202,11 @@
 
 ```bash
 # macOS
-codex sandbox macos [--full-auto] [--log-denials] [COMMAND]...
+codex sandbox macos [--permissions-profile <name>] [--log-denials] [COMMAND]...
 # Linux
-codex sandbox linux [--full-auto] [COMMAND]...
+codex sandbox linux [--permissions-profile <name>] [COMMAND]...
+# Windows
+codex sandbox windows [--permissions-profile <name>] [COMMAND]...
 ```
 
 The `sandbox` command is also available as `codex debug`, and the platform helpers have aliases (for example `codex sandbox seatbelt` and `codex sandbox landlock`).
@@ -144,10 +216,10 @@
 Codex enforces the sandbox differently depending on your OS:
 
 - **macOS** uses Seatbelt policies and runs commands using `sandbox-exec` with a profile (`-p`) that corresponds to the `--sandbox` mode you selected. When restricted read access enables platform defaults, Codex appends a curated macOS platform policy (instead of broadly allowing `/System`) to preserve common tool compatibility.
-- **Linux** uses `Landlock` plus `seccomp` by default. You can opt into the alternative Linux sandbox pipeline with `features.use_linux_sandbox_bwrap = true` (or `-c use_linux_sandbox_bwrap=true`). In managed proxy mode, the bwrap pipeline routes egress through a proxy-only bridge and fails closed if it cannot build valid loopback proxy routes; landlock-only flows do not use that bridge behavior.
-- **Windows** uses the Linux sandbox implementation when running in [Windows Subsystem for Linux (WSL)](https://developers.openai.com/codex/windows#windows-subsystem-for-linux). When running natively on Windows, Codex uses a [Windows sandbox](https://developers.openai.com/codex/windows#windows-sandbox) implementation.
-
-If you use the Codex IDE extension on Windows, it supports WSL directly. Set the following in your VS Code settings to keep the agent inside WSL whenever it's available:
+- **Linux** uses `bwrap` plus `seccomp` by default.
+- **Windows** uses the Linux sandbox implementation when running in [Windows Subsystem for Linux 2 (WSL2)](https://developers.openai.com/codex/windows#windows-subsystem-for-linux). WSL1 was supported through Codex `0.114`; starting in `0.115`, the Linux sandbox moved to `bwrap`, so WSL1 is no longer supported. When running natively on Windows, Codex uses a [Windows sandbox](https://developers.openai.com/codex/windows#windows-sandbox) implementation.
+
+If you use the Codex IDE extension on Windows, it supports WSL2 directly. Set the following in your VS Code settings to keep the agent inside WSL2 whenever it's available:
 
 ```json
 {
@@ -162,13 +234,61 @@
 ```toml
 [windows]
 sandbox = "unelevated" # or "elevated"
+# sandbox_private_desktop = true  # default; set false only for compatibility
 ```
 
 See the [Windows setup guide](https://developers.openai.com/codex/windows#windows-sandbox) for details.
 
-When you run Linux in a containerized environment such as Docker, the sandbox may not work if the host or container configuration doesn't support the required `Landlock` and `seccomp` features.
+When you run Linux in a containerized environment such as Docker, the sandbox may not work if the host or container configuration blocks the namespace, setuid `bwrap`, or `seccomp` operations that Codex needs.
 
 In that case, configure your Docker container to provide the isolation you need, then run `codex` with `--sandbox danger-full-access` (or the `--dangerously-bypass-approvals-and-sandbox` flag) inside the container.
+
+### Run Codex in Dev Containers
+
+If your host cannot run the Linux sandbox directly, or if your organization already standardizes on containerized development, run Codex with Dev Containers and let Docker provide the outer isolation boundary. This works with Visual Studio Code Dev Containers and compatible tools.
+
+Use the [Codex secure devcontainer example](https://github.com/openai/codex/tree/main/.devcontainer) as a reference implementation. The example installs Codex, common development tools, `bubblewrap`, and firewall-based outbound controls.
+
+Devcontainers provide substantial protection, but they do not prevent every
+  attack. If you run Codex with `--sandbox danger-full-access` or
+  `--dangerously-bypass-approvals-and-sandbox` inside the container, a malicious
+  project can exfiltrate anything available inside the devcontainer, including
+  Codex credentials. Use this pattern only with trusted repositories, and
+  monitor Codex activity as you would in any other elevated environment.
+
+The reference implementation includes:
+
+- an Ubuntu 24.04 base image with Codex and common development tools installed;
+- an allowlist-driven firewall profile for outbound access;
+- VS Code settings and extension recommendations for reopening the workspace in a container;
+- persistent mounts for command history and Codex configuration;
+- `bubblewrap`, so Codex can still use its Linux sandbox when the container grants the needed capabilities.
+
+To try it:
+
+1. Install Visual Studio Code and the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
+2. Copy the Codex example `.devcontainer` setup into your repository, or start from the Codex repository directly.
+3. In VS Code, run **Dev Containers: Open Folder in Container...** and select `.devcontainer/devcontainer.secure.json`.
+4. After the container starts, open a terminal and run `codex`.
+
+You can also start the container from the CLI:
+
+```bash
+devcontainer up --workspace-folder . --config .devcontainer/devcontainer.secure.json
+```
+
+The example has three main pieces:
+
+- `.devcontainer/devcontainer.secure.json` controls container settings, capabilities, mounts, environment variables, and VS Code extensions.
+- `.devcontainer/Dockerfile.secure` defines the Ubuntu-based image and installed tools.
+- `.devcontainer/init-firewall.sh` applies the outbound network policy.
+
+The reference firewall is intentionally a starting point. If you depend on domain allowlisting for isolation, implement DNS rebinding and DNS refresh protections that fit your environment, such as TTL-aware refreshes or a DNS-aware firewall.
+
+Inside the container, choose one of these modes:
+
+- Keep Codex's Linux sandbox enabled if the Dev Container profile grants the capabilities needed for `bwrap` to create the inner sandbox.
+- If the container is your intended security boundary, run Codex with `--sandbox danger-full-access` inside the container so Codex does not try to create a second sandbox layer.
 
 ## Version control
 

```
#### https://developers.openai.com/codex/app.md

```diff
--- a/https://developers.openai.com/codex/app.md
+++ b/https://developers.openai.com/codex/app.md
@@ -24,12 +24,15 @@
 
 ## Getting started
 
-The Codex app is available on macOS (Apple Silicon).
+The Codex app is available on macOS and Windows.
+
+Most Codex app features are available on both platforms. Platform-specific
+exceptions are noted in the relevant docs.
 
 <WorkflowSteps variant="headings">
 1. Download and install the Codex app
 
-    Download the Codex app for Windows or macOS.
+    Download the Codex app for macOS or Windows. Choose the Intel build if you're using an Intel-based Mac.
 
     <CodexAppDownloadCta client:load className="mb-4" />
 
@@ -113,7 +116,8 @@
      />
    </ExampleGallery>
 
-   If you need more inspiration, check out the [explore section](https://developers.openai.com/codex/explore).
+   If you need more inspiration, explore [Codex use cases](https://developers.openai.com/codex/use-cases).
+   If you're new to Codex, read the [best practices guide](https://developers.openai.com/codex/learn/best-practices).
 
 </WorkflowSteps>
 
@@ -126,65 +130,93 @@
 
 ### Multitask across projects
 
-Run multiple tasks in parallel and switch quickly between them.
-
-  </BentoContent>
-  <BentoContent href="/codex/app/features#built-in-git-tools">
-
-### Built-in Git tools
-
-Review diffs, comment inline, stage or revert chunks, and commit without leaving the app.
+Run project threads side by side and switch between them quickly.
 
   </BentoContent>
   <BentoContent href="/codex/app/worktrees">
 
-### Worktrees for parallel tasks
-
-Isolate changes of multiple Codex threads using built-in Git worktree support.
+### Worktrees
+
+Keep parallel code changes isolated with built-in Git worktree support.
+
+  </BentoContent>
+  <BentoContent href="/codex/app/computer-use">
+
+### Computer use
+
+Let Codex use macOS apps for GUI tasks, browser flows, and native app testing.
+
+  </BentoContent>
+  <BentoContent href="/codex/app/review">
+
+### Review and ship changes
+
+Inspect diffs, address PR feedback, stage files, commit, and push.
+
+  </BentoContent>
+  <BentoContent href="/codex/app/features#integrated-terminal">
+
+### Terminal and actions
+
+Run commands in each thread and launch repeatable project actions.
+
+  </BentoContent>
+  <BentoContent href="/codex/app/browser">
+
+### In-app browser
+
+Open rendered pages, leave comments, or let Codex operate local browser flows.
+
+  </BentoContent>
+  <BentoContent href="/codex/app/chrome-extension">
+
+### Chrome extension
+
+Add the Chrome plugin so Codex can use Chrome for signed-in browser tasks while you manage website approvals.
+
+  </BentoContent>
+  <BentoContent href="/codex/app/features#image-generation">
+
+### Image generation
+
+Generate or edit images in a thread while you work on the surrounding code and assets.
+
+  </BentoContent>
+  <BentoContent href="/codex/app/automations">
+
+### Automations
+
+Schedule recurring tasks, or wake up the same thread for ongoing checks.
 
   </BentoContent>
   <BentoContent href="/codex/app/features#skills-support">
 
-### Skills support
-
-Give your Codex agent additional capabilities and reuse skills across App, CLI, and IDE Extension.
-
-  </BentoContent>
-  <BentoContent href="/codex/app/automations">
-
-### Automations
-
-Pair skills with automations to automate recurring tasks in the background. Codex adds findings to the inbox, or automatically archives runs if there's nothing to report.
-
-  </BentoContent>
-  <BentoContent href="/codex/app/features#integrated-terminal">
-
-### Built-in terminal
-
-Open a terminal per thread to test your changes, run dev servers, scripts, and custom commands.
-
-  </BentoContent>
-  <BentoContent href="/codex/app/local-environments">
-
-### Local environments
-
-Define worktree setup scripts and common project actions for easy access.
+### Skills
+
+Reuse instructions and workflows across the app, CLI, and IDE Extension.
+
+  </BentoContent>
+  <BentoContent href="/codex/app/features#richer-outputs-and-artifacts">
+
+### Sidebar and artifacts
+
+Follow plans, sources, task summaries, and generated file previews.
+
+  </BentoContent>
+  <BentoContent href="/codex/plugins">
+
+### Plugins
+
+Connect apps, skills, and MCP servers to extend what Codex can do.
 
   </BentoContent>
   <BentoContent href="/codex/app/features#sync-with-the-ide-extension">
 
-### Sync with the IDE extension
+### IDE Extension sync
 
 Share Auto Context and active threads across app and IDE sessions.
 
   </BentoContent>
-  <BentoContent href="/codex/app/features#mcp-support">
-
-### MCP support
-
-Connect your Codex agent to additional services using MCP.
-
-  </BentoContent>
 </BentoContainer>
 
 ---

```
#### https://developers.openai.com/codex/app/automations.md

```diff
--- a/https://developers.openai.com/codex/app/automations.md
+++ b/https://developers.openai.com/codex/app/automations.md
@@ -6,20 +6,25 @@
 
 Automate recurring tasks in the background. Codex adds findings to the inbox, or automatically archives the task if there's nothing to report. You can combine automations with [skills](https://developers.openai.com/codex/skills) for more complex tasks.
 
-Automations run locally in the Codex app. The app needs to be running, and the
-selected project needs to be available on disk.
-
-In Git repositories, each automation run starts in a new
-[worktree](https://developers.openai.com/codex/app/worktrees) so it doesn't interfere with your main
-checkout. In non-version-controlled projects, automations run directly in the
+For project-scoped automations, the app needs to be running, and the selected
+project needs to be available on disk.
+
+In Git repositories, you can choose whether an automation runs in your local
+project or on a new [worktree](https://developers.openai.com/codex/app/worktrees). Both options run in the
+background. Worktrees keep automation changes separate from unfinished local
+work, while running in your local project can modify files you are still
+working on. In non-version-controlled projects, automations run directly in the
 project directory.
+
+You can also leave the model and reasoning effort on their default settings, or
+choose them explicitly if you want more control over how the automation runs.
 
 </div>
 
 <CodexScreenshot
   alt="Automation creation form with schedule and prompt fields"
-  lightSrc="/images/codex/app/create-automation-light.webp"
-  darkSrc="/images/codex/app/create-automation-dark.webp"
+  lightSrc="/images/codex/app/codex-automations-light.webp"
+  darkSrc="/images/codex/app/codex-automations-dark.webp"
   maxHeight="400px"
 />
 
@@ -27,38 +32,97 @@
 
 ## Managing tasks
 
-All automations and their runs can be found in the automations pane inside your Codex app sidebar.
+Find all automations and their runs in the automations pane inside your Codex app sidebar.
 
 The "Triage" section acts as your inbox. Automation runs with findings show up there, and you can filter your inbox to show all automation runs or only unread ones.
 
-When an automation runs in a Git repository, Codex uses a dedicated background [worktree](https://developers.openai.com/codex/app/features#worktree-support). In non-version-controlled projects, automations run directly in the project directory. Consider using Git to enable running on background worktrees. You can have the same automation run on multiple projects.
+Standalone automations start fresh runs on a schedule and report results in
+Triage. Use them when each run should be independent or when one automation
+should run across one or more projects. If you need a custom cadence, choose a
+custom schedule and enter cron syntax.
+
+For Git repositories, each automation can run either in your local project or
+on a dedicated background [worktree](https://developers.openai.com/codex/app/features#worktree-support). Use
+worktrees when you want to isolate automation changes from unfinished local
+work. Use local mode when you want the automation to work directly in your main
+checkout, keeping in mind that it can change files you are actively editing.
+In non-version-controlled projects, automations run directly in the project
+directory. You can have the same automation run on more than one project.
 
 Automations use your default sandbox settings. In read-only mode, tool calls fail if they require modifying files, network access, or working with apps on your computer. With full access enabled, background automations carry elevated risk. You can adjust sandbox settings in [Settings](https://developers.openai.com/codex/app/settings) and selectively allowlist commands with [rules](https://developers.openai.com/codex/rules).
 
-To keep automations maintainable and shareable across teams, you can use [skills](https://developers.openai.com/codex/skills) to define the action and provide tools and context to Codex. You can explicitly trigger a skill as part of an automation by using `$skill-name` inside your automation.
-
-## Testing automations safely
+Automations can use the same plugins and skills available to Codex. To keep
+automations maintainable and shareable across teams, use [skills](https://developers.openai.com/codex/skills)
+to define the action and provide tools and context. You can explicitly trigger a
+skill as part of an automation by using `$skill-name` inside your automation.
+
+## Ask Codex to create or update automations
+
+You can create and update automations from a regular Codex thread. Describe the
+task, the schedule, and whether the automation should stay attached to the
+current thread or start fresh runs. Codex can draft the automation prompt, choose
+the right automation type, and update it when the scope or cadence changes.
+
+For example, ask Codex to remind you in this thread while a deployment finishes,
+or ask it to create a standalone automation that checks a project on a recurring
+schedule.
+
+Skills can also create or update automations. For example, a skill for
+babysitting a pull request could set up a recurring automation that checks the
+PR status with the GitHub plugin and fixes new review feedback.
+
+## Thread automations
+
+Thread automations are heartbeat-style recurring wake-up calls attached to the
+current thread. Use them when you want Codex to keep returning to the same
+conversation on a schedule.
+
+Use a thread automation when the scheduled work should preserve the thread's
+context instead of starting from a new prompt each time.
+
+Thread automations can use minute-based intervals for active follow-up loops,
+or daily and weekly schedules when you need a check-in at a specific time.
+
+Thread automations are useful for:
+
+- checking a long-running command until it finishes
+- polling Slack, GitHub, or another connected source when the results should
+  stay in the same thread
+- reminding Codex to continue a review loop at a fixed cadence
+- running a skill-driven workflow that uses plugins, such as checking PR status
+  and addressing new feedback
+- keeping a chat focused on an ongoing research or triage task
+
+Use a standalone or project automation when each run should be independent,
+when it should run across more than one project, or when findings should appear
+as separate automation runs in Triage.
+
+When you create a thread automation, make the prompt durable. It should
+describe what Codex should do each time the thread wakes up, how to decide
+whether there is anything important to report, and when to stop or ask you for
+input.
+
+## Test automations
 
 Before you schedule an automation, test the prompt manually in a regular thread
 first. This helps you confirm:
 
 - The prompt is clear and scoped correctly.
-- The selected model and tools behave as expected.
+- The selected or default model, reasoning effort, and tools behave as expected.
 - The resulting diff is reviewable.
 
-When you start scheduling runs, review the first few outputs closely and adjust
-the prompt or cadence as needed.
+When you start scheduling runs, review the first few outputs and adjust the
+prompt or cadence as needed.
 
 ## Worktree cleanup for automations
 
-For Git repositories, automations run in worktrees. Frequent schedules can
-create many worktrees over time. Archive automation runs you no longer need,
-and avoid pinning runs unless you intend to keep their worktrees.
+If you choose worktrees for Git repositories, frequent schedules can create
+many worktrees over time. Archive automation runs you no longer need, and avoid
+pinning runs unless you intend to keep their worktrees.
 
 ## Permissions and security model
 
-Automations are designed to run unattended and use your default sandbox
-settings.
+Automations run unattended and use your default sandbox settings.
 
 - If your sandbox mode is **read-only**, tool calls fail if they require
   modifying files, accessing network, or working with apps on your computer.
@@ -68,7 +132,7 @@
   on your computer. You can selectively allowlist commands to run outside the
   sandbox using [rules](https://developers.openai.com/codex/rules).
 - If your sandbox mode is **full access**, background automations carry
-  elevated risk, as Codex may modify files, run commands, and access network
+  elevated risk, as Codex may change files, run commands, and access network
   without asking. Consider updating sandbox settings to workspace write, and
   using [rules](https://developers.openai.com/codex/rules) to selectively define which commands the agent
   can run with full access.
@@ -79,7 +143,7 @@
 [Admin-enforced requirements (`requirements.toml`)](https://developers.openai.com/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml).
 
 Automations use `approval_policy = "never"` when your organization policy
-allows it. If `approval_policy = "never"` is disallowed by admin requirements,
+allows it. If admin requirements disallow `approval_policy = "never"`,
 automations fall back to the approval behavior of your selected mode.
 
 ## Examples

```
#### https://developers.openai.com/codex/app/commands.md

```diff
--- a/https://developers.openai.com/codex/app/commands.md
+++ b/https://developers.openai.com/codex/app/commands.md
@@ -36,7 +36,7 @@
 
 You can also explicitly invoke skills by typing `$` in the thread composer. See [Skills](https://developers.openai.com/codex/skills).
 
-Enabled skills also appear in the slash command list (for example, `/imagegen`).
+Enabled skills also appear in the slash command list.
 
 ### Available slash commands
 
@@ -48,6 +48,24 @@
 | `/review`     | Start code review mode to review uncommitted changes or compare against a base branch. |
 | `/status`     | Show the thread ID, context usage, and rate limits.                                    |
 
+## Deeplinks
+
+The Codex app registers the `codex://` URL scheme so links can open specific parts of the app directly.
+
+| Deeplink                      | Opens                                         | Supported query parameters               |
+| ----------------------------- | --------------------------------------------- | ---------------------------------------- |
+| `codex://settings`            | Settings.                                     | None.                                    |
+| `codex://skills`              | Skills.                                       | None.                                    |
+| `codex://automations`         | Inbox in automation create mode.              | None.                                    |
+| `codex://threads/<thread-id>` | A local thread. `<thread-id>` must be a UUID. | None.                                    |
+| `codex://new`                 | A new thread.                                 | Optional: `prompt`, `originUrl`, `path`. |
+
+For new-thread deeplinks:
+
+- `prompt` sets the initial composer text.
+- `path` must be an absolute path to a local directory and, when valid, makes that directory the active workspace for the new thread.
+- `originUrl` tries to match one of your current workspace roots by Git remote URL. If both `path` and `originUrl` are present, Codex resolves `path` first.
+
 ## See also
 
 - [Features](https://developers.openai.com/codex/app/features)

```
#### https://developers.openai.com/codex/app/features.md

```diff
--- a/https://developers.openai.com/codex/app/features.md
+++ b/https://developers.openai.com/codex/app/features.md
@@ -2,6 +2,9 @@
 
 The Codex app is a focused desktop experience for working on Codex threads in parallel,
 with built-in worktree support, automations, and Git functionality.
+
+Most Codex app features are available on both macOS and Windows.
+The sections below note platform-specific exceptions.
 
 <YouTubeEmbed
   title="Introducing the Codex app"
@@ -67,7 +70,8 @@
 
 You can also combine skills with [automations](https://developers.openai.com/codex/app/automations) to perform routine tasks
 such as evaluating errors in your telemetry and submitting fixes or creating reports on recent
-codebase changes.
+codebase changes. For ongoing work that should stay in one thread, use a
+[thread automation](https://developers.openai.com/codex/app/automations#thread-automations).
 
 </div>
 
@@ -173,7 +177,9 @@
 pressing <kbd>Cmd</kbd>+<kbd>J</kbd>.
 
 Use the terminal to validate changes, run scripts, and perform Git operations
-without leaving the app.
+without leaving the app. Codex can also read the current terminal output, so
+it can check the status of a running development server or refer back to a
+failed build while it works with you.
 
 Common tasks include:
 
@@ -264,6 +270,102 @@
 
 </section>
 
+<section class="feature-grid">
+
+<div>
+
+## In-app browser
+
+Use the [in-app browser](https://developers.openai.com/codex/app/browser) to preview, review, and comment on
+local development servers, file-backed previews, and public pages that don't
+require sign-in while you iterate on a web app.
+
+The in-app browser doesn't support authentication flows, signed-in pages, your
+regular browser profile, cookies, extensions, or existing tabs.
+
+Use browser comments to mark specific elements or areas on a page, then ask
+Codex to address that feedback.
+
+When you want Codex to operate the page directly, use
+[browser use](https://developers.openai.com/codex/app/browser#browser-use) for local development servers and
+file-backed pages. You can manage the Browser plugin, allowed websites, and
+blocked websites from settings.
+
+</div>
+
+<CodexScreenshot
+  alt="Codex app showing a browser comment on a local web app preview"
+  lightSrc="/images/codex/app/in-app-browser-light.webp"
+  darkSrc="/images/codex/app/in-app-browser-dark.webp"
+  maxHeight="400px"
+  variant="no-wallpaper"
+/>
+
+</section>
+
+<section class="feature-grid inverse">
+
+<div>
+
+## Computer use
+
+[Computer use](https://developers.openai.com/codex/app/computer-use) helps Codex operate a macOS app by
+seeing, clicking, and typing. This is useful for testing desktop apps, checking
+browser or simulator flows, working with data sources that aren't available as
+plugins, changing app settings, and reproducing GUI-only bugs.
+
+Because computer use can affect app and system state outside your project
+workspace, keep tasks narrow and review permission prompts before continuing.
+
+The feature isn't available in the European Economic Area, the United Kingdom, or
+Switzerland at launch.
+
+</div>
+
+<CodexScreenshot
+  alt="Codex app asking for permission to use Calculator with computer use"
+  lightSrc="/images/codex/app/computer-use-approval-light.webp"
+  darkSrc="/images/codex/app/computer-use-approval-dark.webp"
+  maxHeight="400px"
+  variant="no-wallpaper"
+/>
+
+</section>
+
+<section class="feature-grid">
+
+<div>
+
+<a id="richer-outputs-and-artifacts"></a>
+<a id="task-sidebar"></a>
+<a id="artifact-viewer"></a>
+
+## Work with non-code artifacts
+
+When a task produces non-code artifacts, the sidebar can preview PDF files,
+spreadsheets, documents, and presentations. Give Codex the source data, expected
+file type, structure, and review criteria you care about.
+
+For spreadsheets and presentations, describe the sheets, columns, charts, slide
+sections, and checks that matter. Ask Codex to explain where it saved the output
+and how it checked the result.
+
+Use the task sidebar to follow what Codex is doing while a thread runs. It can
+surface the agent's plan, sources, generated artifacts, and task summary so you
+can steer the work, inspect generated files, and decide what needs another pass.
+
+</div>
+
+<CodexScreenshot
+  alt="Codex app showing a generated presentation in the artifact viewer"
+  lightSrc="/images/codex/app/artifact-viewer-light.webp"
+  darkSrc="/images/codex/app/artifact-viewer-dark.webp"
+  maxHeight="420px"
+  variant="no-wallpaper"
+/>
+
+</section>
+
 ---
 
 ## Sync with the IDE extension
@@ -280,6 +382,18 @@
 If you're unsure whether the app includes context, toggle it off and ask the
 same question again to compare results.
 
+## Thread automations
+
+Automations can also attach to a single thread. These thread automations are
+recurring wake-up calls that preserve the thread's context so Codex can check
+on long-running work, poll a source for new information, or continue a follow-up
+loop. Use them for heartbeat-style automations that should keep returning to the
+same conversation on a schedule.
+
+Use a thread automation when the next run depends on the current conversation.
+Use a standalone or project [automation](https://developers.openai.com/codex/app/automations) when you want
+Codex to start a fresh recurring task for one or more projects.
+
 ## Approvals and sandboxing
 
 Your approval and sandbox settings constrain Codex actions.
@@ -298,7 +412,12 @@
 opening separate projects or using worktrees rather than asking Codex to roam
 outside the project root.
 
-For a high-level overview, see [Sandboxing](https://developers.openai.com/codex/concepts/sandboxing). For
+If [automatic review](https://developers.openai.com/codex/agent-approvals-security#automatic-approval-reviews)
+is available in your workspace, you can choose it from the permissions selector.
+It keeps the same sandbox boundary but routes eligible approval requests through
+the configured review policy instead of waiting for you.
+
+For a high-level overview, see [sandboxing](https://developers.openai.com/codex/concepts/sandboxing). For
 configuration details, see the
 [agent approvals & security documentation](https://developers.openai.com/codex/agent-approvals-security).
 
@@ -311,12 +430,22 @@
 
 ## Web search
 
-Codex ships with a first-party web search tool. For local tasks in the Codex IDE Extension, Codex
+Codex ships with a first-party web search tool. For local tasks in the Codex app, Codex
 enables web search by default and serves results from a web search cache. If you configure your
 sandbox for [full access](https://developers.openai.com/codex/agent-approvals-security), web search defaults to live results. See
 [Config basics](https://developers.openai.com/codex/config-basic) to disable web search or switch to live results that fetch the
 most recent data.
 
+## Image generation
+
+Ask Codex to generate or edit images directly in a thread. This is useful for UI assets, banners, backgrounds, illustrations, sprite sheets, and placeholders you want to create alongside code. Add a reference image when you want Codex to transform or extend an existing asset.
+
+You can ask in natural language or explicitly invoke the image generation skill by including `$imagegen` in your prompt.
+
+Built-in image generation uses `gpt-image-2`, counts toward your general Codex usage limits, and uses included limits 3-5x faster on average than similar turns without image generation, depending on image quality and size. For details, see [Pricing](https://developers.openai.com/codex/pricing#image-generation-usage-limits). For prompting tips and model details, see the [image generation guide](https://developers.openai.com/api/docs/guides/image-generation).
+
+For larger batches of image generation, set `OPENAI_API_KEY` in your environment variables and ask Codex to generate images through the API so API pricing applies instead.
+
 ## Image input
 
 You can drag and drop images into the prompt composer to include them as context. Hold down `Shift`
@@ -325,6 +454,25 @@
 You can also ask Codex to view images on your system. By giving Codex tools to take screenshots of
 the app you are working on, Codex can verify the work it's doing.
 
+<a id="projectless-threads"></a>
+
+## Chats
+
+Chats are threads you can start when the task doesn't need a specific project
+folder or Git repository. Use them for research, triage, planning,
+plugin-heavy workflows, and other conversations where Codex should use connected
+tools instead of editing a codebase.
+
+Chats use a Codex-managed `threads` directory under your Codex home as their
+working location. By default, that location is `~/.codex/threads`.
+
+## Memories
+
+[Memories](https://developers.openai.com/codex/memories), where available, let Codex carry useful context
+from past tasks into future threads. They're most useful for stable preferences,
+project conventions, recurring work patterns, and known pitfalls that would
+otherwise need to repeat.
+
 ## Notifications
 
 By default, the Codex app sends notifications when a task completes or needs approval while the app
@@ -342,5 +490,8 @@
 
 - [Settings](https://developers.openai.com/codex/app/settings)
 - [Automations](https://developers.openai.com/codex/app/automations)
+- [In-app browser](https://developers.openai.com/codex/app/browser)
+- [Computer use](https://developers.openai.com/codex/app/computer-use)
+- [Review pane](https://developers.openai.com/codex/app/review)
 - [Local environments](https://developers.openai.com/codex/app/local-environments)
 - [Worktrees](https://developers.openai.com/codex/app/worktrees)
```
#### https://developers.openai.com/codex/app/settings.md

```diff
--- a/https://developers.openai.com/codex/app/settings.md
+++ b/https://developers.openai.com/codex/app/settings.md
@@ -10,11 +10,6 @@
 require <kbd>Cmd</kbd>+<kbd>Enter</kbd> for multiline prompts or prevent sleep while a
 thread runs.
 
-## Appearance
-
-Pick a theme, decide whether the window is solid, and adjust UI or code fonts. Font
-choices apply across the app, including the diff review panel and terminal.
-
 ## Notifications
 
 Choose when turn completion notifications appear, and whether the app should prompt for
@@ -26,6 +21,54 @@
 Use the in-app controls for common settings, or edit `config.toml` for advanced
 options. See [Codex security](https://developers.openai.com/codex/agent-approvals-security) and
 [config basics](https://developers.openai.com/codex/config-basic) for more detail.
+
+## Appearance
+
+In **Settings**, you can change the Codex app appearance by choosing a base theme,
+adjusting accent, background, and foreground colors, and changing the UI and code
+fonts. You can also share your custom theme with friends.
+
+<CodexScreenshot
+  alt="Codex app Appearance settings showing theme selection, color controls, and font options"
+  lightSrc="/images/codex/app/theme-selection-light.webp"
+  darkSrc="/images/codex/app/theme-selection-dark.webp"
+  maxHeight="720px"
+  class="mb-8"
+/>
+
+### Codex pets
+
+<div class="grid gap-5 md:grid-cols-[minmax(0,1fr)_minmax(15rem,50%)] md:items-start xl:grid-cols-[minmax(0,1fr)_minmax(16rem,30%)]">
+  <div>
+    Codex pets are optional animated companions for the app. In **Settings**,
+    go to **Appearance** and choose **Pets** to select a built-in pet or
+    refresh custom pets from your local Codex home. Type `/pet` in the
+    composer, use **Wake Pet** or **Tuck Away Pet** in **Settings > Appearance**, or
+    press <kbd>Cmd+K</kbd> or <kbd>Ctrl+K</kbd> and run the same commands to
+    toggle the floating overlay.
+
+    The overlay keeps active Codex work visible while you use other apps. It
+    shows the active thread, reflects whether Codex is running, waiting for
+    input, or ready for review, and pairs that state with a short progress
+    prompt so you can glance at what changed without reopening the thread.
+
+  </div>
+
+  <CodexPetsDemo client:load />
+</div>
+
+To create your own pet, install the `hatch-pet` skill:
+
+```text
+$skill-installer hatch-pet
+```
+
+Reload skills from the command menu. Press <kbd>Cmd+K</kbd> or <kbd>Ctrl+K</kbd>,
+choose **Force Reload Skills**, then ask the skill to create a pet:
+
+```text
+$hatch-pet create a new pet inspired by my recent projects
+```
 
 ## Git
 
@@ -40,6 +83,24 @@
 also apply to the Codex CLI and IDE extension because the MCP configuration lives in
 `config.toml`. See the [Model Context Protocol docs](https://developers.openai.com/codex/mcp) for details.
 
+## Browser use
+
+Use these settings to install or enable the bundled Browser plugin, set up the
+[Codex Chrome extension](https://developers.openai.com/codex/app/chrome-extension), and manage allowlisted
+and blocklisted websites. Codex asks before using a website unless you've
+allowlisted it. Removing a site from the blocklist lets Codex ask again before
+using it in the browser.
+
+See [In-app browser](https://developers.openai.com/codex/app/browser) for browser preview, comment, and
+browser use workflows.
+
+## Computer Use
+
+On macOS, check your Computer Use settings to review desktop-app access and related
+preferences after setup. To revoke system-level access, update Screen Recording
+or Accessibility permissions in macOS Privacy & Security settings. The feature
+isn't available in the EEA, the United Kingdom, or Switzerland at launch.
+
 ## Personalization
 
 Choose **Friendly**, **Pragmatic**, or **None** as your default personality. Use
@@ -48,6 +109,17 @@
 You can also add your own custom instructions. Editing custom instructions updates your
 [personal instructions in `AGENTS.md`](https://developers.openai.com/codex/guides/agents-md).
 
+## Context-aware suggestions
+
+Use context-aware suggestions to surface follow-ups and tasks you may want to resume when you
+start or return to Codex.
+
+## Memories
+
+Enable Memories, where available, to let Codex carry useful context from past
+threads into future work. See [Memories](https://developers.openai.com/codex/memories) for setup, storage,
+and per-thread controls.
+
 ## Archived threads
 
 The **Archived threads** section lists archived chats with dates and project

```
#### https://developers.openai.com/codex/app/review.md

```diff
--- a/https://developers.openai.com/codex/app/review.md
+++ b/https://developers.openai.com/codex/app/review.md
@@ -41,12 +41,12 @@
 2. Hover the line you want to comment on.
 3. Click the **+** button that appears.
 4. Write your feedback and submit it.
-5. Once you are done with all your feedback, send a message back to the thread.
+5. After you finish leaving feedback, send a message back to the thread.
 
-Because the comment is anchored to a line, Codex can usually respond more
-precisely than with a general instruction.
+Because comments are line-specific, Codex can respond more precisely than with a
+general instruction.
 
-Inline comments are treated as review guidance. After leaving comments, send a
+Codex treats inline comments as review guidance. After leaving comments, send a
 follow-up message that makes your intent explicit, for example “Address the
 inline comments and keep the scope minimal.”
 
@@ -62,12 +62,35 @@
   maxHeight="400px"
 />
 
+## Pull request reviews
+
+When Codex has GitHub access for your repository and the current project is on
+the pull request branch, the Codex app can help you work through pull request
+feedback without leaving the app. The sidebar shows pull request context and
+feedback from reviewers, and the review pane shows comments alongside the diff
+so you can ask Codex to address issues in the same thread.
+
+Install the GitHub CLI (`gh`) and authenticate it with `gh auth login` so Codex
+can load pull request context, review comments, and changed files. If `gh` is
+missing or unauthenticated, pull request details may not appear in the sidebar
+or review pane.
+
+Use this flow when you want to keep the full fix loop in one place:
+
+1. Open the review pane on the pull request branch.
+2. Review the pull request context, comments, and changed files.
+3. Ask Codex to fix the specific comments you want handled.
+4. Inspect the resulting diff in the review pane.
+5. Stage, commit, and push the changes to the PR branch when you are ready.
+
+For GitHub-triggered reviews, see [Use Codex in GitHub](https://developers.openai.com/codex/integrations/github).
+
 ## Staging and reverting files
 
 The review pane includes Git actions so you can shape the diff before you
 commit.
 
-You can stage, unstage, or revert changes at multiple levels:
+You can stage, unstage, or revert changes at these levels:
 
 - **Entire diff**: use the action buttons in the review header (for example,
   "Stage all" or "Revert all")
@@ -77,7 +100,7 @@
 Use staging when you want to accept part of the work, and revert when you want
 to discard it.
 
-### Partially staged states
+### Staged and unstaged states
 
 Git can represent both staged and unstaged changes in the same file. When that
 happens, it can look like the pane is showing “the same file twice” across

```
#### https://developers.openai.com/codex/app/windows.md

```diff
--- a/https://developers.openai.com/codex/app/windows.md
+++ b/https://developers.openai.com/codex/app/windows.md
@@ -1,10 +1,12 @@
 # Windows
 
-The [Codex app for Windows](https://apps.microsoft.com/detail/9plm9xgg6vks?hl=en-US&gl=US) gives you one interface for
+The [Codex app for Windows](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi) gives you one interface for
 working across projects, running parallel agent threads, and reviewing results.
+The Windows app supports core workflows such as worktrees, automations, Git
+functionality, the in-app browser, artifact previews, plugins, and skills.
 It runs natively on Windows using PowerShell and the
 [Windows sandbox](https://developers.openai.com/codex/windows#windows-sandbox), or you can configure it to
-run in [Windows Subsystem for Linux (WSL)](#windows-subsystem-for-linux-wsl).
+run in [Windows Subsystem for Linux 2 (WSL2)](#windows-subsystem-for-linux-wsl).
 
 <CodexScreenshot
   alt="Codex app for Windows showing a project sidebar, active thread, and review pane"
@@ -17,7 +19,7 @@
 ## Download and update the Codex app
 
 Download the Codex app from the
-[Microsoft Store](https://apps.microsoft.com/detail/9plm9xgg6vks?hl=en-US&gl=US).
+[Microsoft Store](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi).
 
 Then follow the [quickstart](https://developers.openai.com/codex/quickstart?setup=app) to get started.
 
@@ -33,6 +35,18 @@
 ```powershell
 winget install Codex -s msstore
 ```
+
+## Native sandbox
+
+The Codex app on Windows supports a native [Windows sandbox](https://developers.openai.com/codex/windows#windows-sandbox) when the agent runs in PowerShell, and uses Linux sandboxing when you run the agent in [Windows Subsystem for Linux 2 (WSL2)](#windows-subsystem-for-linux-wsl). To apply sandbox protections in either mode, set sandbox permissions to **Default permissions** in the Composer before sending messages to Codex.
+
+Running Codex in full access mode means Codex is not limited to your project
+  directory and might perform unintentional destructive actions that can lead to
+  data loss. Keep sandbox boundaries in place and use [rules](https://developers.openai.com/codex/rules) for
+  targeted exceptions, or set your [approval policy to
+  never](https://developers.openai.com/codex/agent-approvals-security#run-without-approval-prompts) to have
+  Codex attempt to solve problems without asking for escalated permissions,
+  based on your [approval and security setup](https://developers.openai.com/codex/agent-approvals-security).
 
 ## Customize for your dev setup
 
@@ -93,7 +107,7 @@
 
 By default, the Codex app uses the Windows-native agent. That means the agent
 runs commands in PowerShell. The app can still work with projects that live in
-Windows Subsystem for Linux (WSL) by using the `wsl` CLI when needed.
+Windows Subsystem for Linux 2 (WSL2) by using the `wsl` CLI when needed.
 
 If you want to add a project from the WSL filesystem, click **Add new project**
 or press <kbd>Ctrl</kbd>+<kbd>O</kbd>, then type `\\wsl$\` into the File
@@ -105,10 +119,13 @@
 `/mnt/<drive>/...`. This setup is more reliable than opening projects
 directly from the WSL filesystem.
 
-If you want the agent itself to run in WSL, open **[Settings](codex://settings)**,
+If you want the agent itself to run in WSL2, open **[Settings](codex://settings)**,
 switch the agent from Windows native to WSL, and **restart the app**. The
 change doesn't take effect until you restart. Your projects should remain in
 place after restart.
+
+WSL1 was supported through Codex `0.114`. Starting in Codex `0.115`, the Linux
+sandbox moved to `bubblewrap`, so WSL1 is no longer supported.
 
 <CodexScreenshot
   alt="Codex app settings showing the agent selector with Windows native and WSL options"
@@ -210,7 +227,7 @@
 `%USERPROFILE%\.codex`.
 
 If you also run the Codex CLI inside WSL, the CLI uses the Linux home
-directory by default, so it does not automatically share configuration, cached
+directory by default, so it doesn't automatically share configuration, cached
 auth, or session history with the Windows app.
 
 To share them, use one of these approaches:
@@ -232,12 +249,12 @@
 
 ### Git isn't detected for projects opened from `\\wsl$`
 
-For now, if you want to use the Windows-native agent with a project that is
-also accessible from WSL, the most reliable workaround is to store the project
+For now, if you want to use the Windows-native agent with a project also
+accessible from WSL, the most reliable workaround is to store the project
 on the native Windows drive and access it in WSL through `/mnt/<drive>/...`.
 
-### Cmder is not listed in the open dialog
-
-If Cmder is installed but doesn't show in Codex's open dialog, add it to the
-Windows Start Menu: right-click Cmder and choose **Add to Start**, then restart
-Codex or reboot.+### `Cmder` isn't listed in the open dialog
+
+If `Cmder` is installed but doesn't show in Codex's open dialog, add it to the
+Windows Start Menu: right-click `Cmder` and choose **Add to Start**, then
+restart Codex or reboot.
```
#### https://developers.openai.com/codex/app-server.md

```diff
--- a/https://developers.openai.com/codex/app-server.md
+++ b/https://developers.openai.com/codex/app-server.md
@@ -12,7 +12,26 @@
 Supported transports:
 
 - `stdio` (`--listen stdio://`, default): newline-delimited JSON (JSONL).
-- `websocket` (`--listen ws://IP:PORT`, experimental): one JSON-RPC message per WebSocket text frame.
+- `websocket` (`--listen ws://IP:PORT`, experimental and unsupported): one JSON-RPC message per WebSocket text frame.
+- `off` (`--listen off`): don't expose a local transport.
+
+When you run with `--listen ws://IP:PORT`, the same listener also serves basic HTTP health probes:
+
+- `GET /readyz` returns `200 OK` once the listener accepts new connections.
+- `GET /healthz` returns `200 OK` when the request doesn't include an `Origin` header.
+- Requests with an `Origin` header are rejected with `403 Forbidden`.
+
+WebSocket transport is experimental and unsupported. Loopback listeners such as `ws://127.0.0.1:PORT` are appropriate for localhost and SSH port-forwarding workflows. Non-loopback WebSocket listeners currently allow unauthenticated connections by default during rollout, so configure WebSocket auth before exposing one remotely.
+
+Supported WebSocket auth flags:
+
+- `--ws-auth capability-token --ws-token-file /absolute/path`
+- `--ws-auth capability-token --ws-token-sha256 HEX`
+- `--ws-auth signed-bearer-token --ws-shared-secret-file /absolute/path`
+
+For signed bearer tokens, you can also set `--ws-issuer`, `--ws-audience`, and `--ws-max-clock-skew-seconds`. Clients present the credential as `Authorization: Bearer <token>` during the WebSocket handshake, and app-server enforces auth before JSON-RPC `initialize`.
+
+Prefer `--ws-token-file` over passing raw bearer tokens on the command line. Use `--ws-token-sha256` only when the client keeps the raw high-entropy token in a separate local secret store; the hash is only a verifier, and clients still need the original token.
 
 In WebSocket mode, app-server uses bounded queues. When request ingress is full, the server rejects new requests with JSON-RPC error code `-32001` and message `"Server overloaded; retry later."` Clients should retry with an exponentially increasing delay and jitter.
 
@@ -21,7 +40,7 @@
 Requests include `method`, `params`, and `id`:
 
 ```json
-{ "method": "thread/start", "id": 10, "params": { "model": "gpt-5.1-codex" } }
+{ "method": "thread/start", "id": 10, "params": { "model": "gpt-5.4" } }
 ```
 
 Responses echo the `id` with either `result` or `error`:
@@ -99,7 +118,7 @@
   },
 });
 send({ method: "initialized", params: {} });
-send({ method: "thread/start", id: 1, params: { model: "gpt-5.1-codex" } });
+send({ method: "thread/start", id: 1, params: { model: "gpt-5.4" } });
 ```
 
 ## Core primitives
@@ -123,7 +142,7 @@
 
 Clients must send a single `initialize` request per transport connection before invoking any other method on that connection, then acknowledge with an `initialized` notification. Requests sent before initialization receive a `Not initialized` error, and repeated `initialize` calls on the same connection return `Already initialized`.
 
-The server returns the user agent string it will present to upstream services. Set `clientInfo` to identify your integration.
+The server returns the user agent string it will present to upstream services plus `platformFamily` and `platformOs` values that describe the runtime target. Set `clientInfo` to identify your integration.
 
 `initialize.params.capabilities` also supports per-connection notification opt-out via `optOutNotificationMethods`, which is a list of exact method names to suppress for that connection. Matching is exact (no wildcards/prefixes). Unknown method names are accepted and ignored.
 
@@ -159,10 +178,7 @@
     },
     "capabilities": {
       "experimentalApi": true,
-      "optOutNotificationMethods": [
-        "codex/event/session_configured",
-        "item/agentMessage/delta"
-      ]
+      "optOutNotificationMethods": ["thread/started", "item/agentMessage/delta"]
     }
   }
 }
@@ -202,37 +218,71 @@
 - `thread/resume` - reopen an existing thread by id so later `turn/start` calls append to it.
 - `thread/fork` - fork a thread into a new thread id by copying stored history; emits `thread/started` for the new thread.
 - `thread/read` - read a stored thread by id without resuming it; set `includeTurns` to return full turn history. Returned `thread` objects include runtime `status`.
-- `thread/list` - page through stored thread logs; supports cursor-based pagination plus `modelProviders`, `sourceKinds`, `archived`, and `cwd` filters. Returned `thread` objects include runtime `status`.
+- `thread/list` - page through stored thread logs; supports cursor-based pagination plus `modelProviders`, `sourceKinds`, `archived`, `cwd`, and `searchTerm` filters. Returned `thread` objects include runtime `status`.
+- `thread/turns/list` - page through a stored thread's turn history without resuming it.
 - `thread/loaded/list` - list the thread ids currently loaded in memory.
+- `thread/name/set` - set or update a thread's user-facing name for a loaded thread or a persisted rollout; emits `thread/name/updated`.
+- `thread/goal/set` - set the goal for a loaded thread (experimental; requires `capabilities.experimentalApi`); emits `thread/goal/updated`.
+- `thread/goal/get` - read the current goal for a loaded thread (experimental; requires `capabilities.experimentalApi`).
+- `thread/goal/clear` - clear the goal for a loaded thread (experimental; requires `capabilities.experimentalApi`); emits `thread/goal/cleared`.
+- `thread/metadata/update` - patch SQLite-backed stored thread metadata; currently supports persisted `gitInfo`.
 - `thread/archive` - move a thread's log file into the archived directory; returns `{}` on success and emits `thread/archived`.
-- `thread/unsubscribe` - unsubscribe this connection from thread turn/item events. If this was the last subscriber, the server unloads the thread and emits `thread/closed`.
+- `thread/unsubscribe` - unsubscribe this connection from thread turn/item events. If this was the last subscriber, the server unloads the thread after a no-subscriber inactivity grace period and emits `thread/closed`.
 - `thread/unarchive` - restore an archived thread rollout back into the active sessions directory; returns the restored `thread` and emits `thread/unarchived`.
 - `thread/status/changed` - notification emitted when a loaded thread's runtime `status` changes.
 - `thread/compact/start` - trigger conversation history compaction for a thread; returns `{}` immediately while progress streams via `turn/*` and `item/*` notifications.
+- `thread/shellCommand` - run a user-initiated shell command against a thread. This runs outside the sandbox with full access and doesn't inherit the thread sandbox policy.
+- `thread/backgroundTerminals/clean` - stop all running background terminals for a thread (experimental; requires `capabilities.experimentalApi`).
 - `thread/rollback` - drop the last N turns from the in-memory context and persist a rollback marker; returns the updated `thread`.
 - `turn/start` - add user input to a thread and begin Codex generation; responds with the initial `turn` and streams events. For `collaborationMode`, `settings.developer_instructions: null` means "use built-in instructions for the selected mode."
+- `thread/inject_items` - append raw Responses API items to a loaded thread's model-visible history without starting a user turn.
 - `turn/steer` - append user input to the active in-flight turn for a thread; returns the accepted `turnId`.
 - `turn/interrupt` - request cancellation of an in-flight turn; success is `{}` and the turn ends with `status: "interrupted"`.
 - `review/start` - kick off the Codex reviewer for a thread; emits `enteredReviewMode` and `exitedReviewMode` items.
 - `command/exec` - run a single command under the server sandbox without starting a thread/turn.
+- `command/exec/write` - write `stdin` bytes to a running `command/exec` session or close `stdin`.
+- `command/exec/resize` - resize a running PTY-backed `command/exec` session.
+- `command/exec/terminate` - stop a running `command/exec` session.
+- `command/exec/outputDelta` (notify) - emitted for base64-encoded stdout/stderr chunks from a streaming `command/exec` session.
 - `model/list` - list available models (set `includeHidden: true` to include entries with `hidden: true`) with effort options, optional `upgrade`, and `inputModalities`.
+- `modelProvider/capabilities/read` - read provider capability bounds for model/provider combinations (experimental; requires `capabilities.experimentalApi`).
 - `experimentalFeature/list` - list feature flags with lifecycle stage metadata and cursor pagination.
+- `experimentalFeature/enablement/set` - patch in-memory runtime enablement for supported feature keys such as `apps` and `plugins`.
 - `collaborationMode/list` - list collaboration mode presets (experimental, no pagination).
 - `skills/list` - list skills for one or more `cwd` values (supports `forceReload` and optional `perCwdExtraUserRoots`).
+- `skills/changed` (notify) - emitted when watched local skill files change.
+- `marketplace/add` - add a remote plugin marketplace and persist it into the user's marketplace config.
+- `marketplace/upgrade` - refresh a configured Git marketplace, or all configured Git marketplaces when you omit the marketplace name.
+- `plugin/list` - list discovered plugin marketplaces and plugin state, including install/auth policy metadata, marketplace load errors, featured plugin ids, and local, Git, or remote plugin source metadata.
+- `plugin/read` - read one plugin by marketplace path or remote marketplace name and plugin name, including bundled skills, apps, and MCP server names when those details are available.
+- `plugin/install` - install a plugin from a marketplace path or remote marketplace name.
+- `plugin/uninstall` - uninstall an installed plugin.
 - `app/list` - list available apps (connectors) with pagination plus accessibility/enabled metadata.
 - `skills/config/write` - enable or disable skills by path.
 - `mcpServer/oauth/login` - start an OAuth login for a configured MCP server; returns an authorization URL and emits `mcpServer/oauthLogin/completed` on completion.
 - `tool/requestUserInput` - prompt the user with 1-3 short questions for a tool call (experimental); questions can set `isOther` for a free-form option.
 - `config/mcpServer/reload` - reload MCP server configuration from disk and queue a refresh for loaded threads.
-- `mcpServerStatus/list` - list MCP servers, tools, resources, and auth status (cursor + limit pagination).
+- `mcpServerStatus/list` - list MCP servers, tools, resources, and auth status (cursor + limit pagination). Use `detail: "full"` for full data or `detail: "toolsAndAuthOnly"` to omit resources.
+- `mcpServer/resource/read` - read a single MCP resource through an initialized MCP server.
+- `mcpServer/tool/call` - call a tool on a thread's configured MCP server.
+- `mcpServer/startupStatus/updated` (notify) - emitted when a configured MCP server's startup status changes for a loaded thread.
 - `windowsSandbox/setupStart` - start Windows sandbox setup for `elevated` or `unelevated` mode; returns quickly and later emits `windowsSandbox/setupCompleted`.
 - `feedback/upload` - submit a feedback report (classification + optional reason/logs + conversation id, plus optional `extraLogFiles` attachments).
 - `config/read` - fetch the effective configuration on disk after resolving configuration layering.
-- `externalAgentConfig/detect` - detect migratable external-agent artifacts with `includeHome` and optional `cwds`; each detected item includes `cwd` (`null` for home).
-- `externalAgentConfig/import` - apply selected external-agent migration items by passing explicit `migrationItems` with `cwd` (`null` for home).
+- `externalAgentConfig/detect` - detect external-agent artifacts that can be migrated with `includeHome` and optional `cwds`; each detected item includes `cwd` (`null` for home).
+- `externalAgentConfig/import` - apply selected external-agent migration items by passing explicit `migrationItems` with `cwd` (`null` for home). Supported item types include config, skills, `AGENTS.md`, plugins, MCP server config, subagents, hooks, commands, and sessions; plugin imports emit `externalAgentConfig/import/completed`.
 - `config/value/write` - write a single configuration key/value to the user's `config.toml` on disk.
 - `config/batchWrite` - apply configuration edits atomically to the user's `config.toml` on disk.
 - `configRequirements/read` - fetch requirements from `requirements.toml` and/or MDM, including allow-lists, pinned `featureRequirements`, and residency/network requirements (or `null` if you haven't set any up).
+- `fs/readFile`, `fs/writeFile`, `fs/createDirectory`, `fs/getMetadata`, `fs/readDirectory`, `fs/remove`, `fs/copy`, `fs/watch`, `fs/unwatch`, and `fs/changed` (notify) - operate on absolute filesystem paths through the app-server v2 filesystem API.
+
+Plugin summaries include a `source` union. Local plugins return
+`{ "type": "local", "path": ... }`, Git-backed marketplace entries return
+`{ "type": "git", "url": ..., "path": ..., "refName": ..., "sha": ... }`,
+and remote catalog entries return `{ "type": "remote" }`. For remote-only
+catalog entries, `PluginMarketplaceEntry.path` can be `null`; pass
+`remoteMarketplaceName` instead of `marketplacePath` when reading or installing
+those plugins.
 
 ## Models
 
@@ -301,13 +351,16 @@
 ## Threads
 
 - `thread/read` reads a stored thread without subscribing to it; set `includeTurns` to include turns.
-- `thread/list` supports cursor pagination plus `modelProviders`, `sourceKinds`, `archived`, and `cwd` filtering.
+- `thread/turns/list` pages through a stored thread's turn history without resuming it.
+- `thread/list` supports cursor pagination plus `modelProviders`, `sourceKinds`, `archived`, `cwd`, and `searchTerm` filtering.
 - `thread/loaded/list` returns the thread IDs currently in memory.
 - `thread/archive` moves the thread's persisted JSONL log into the archived directory.
-- `thread/unsubscribe` unsubscribes the current connection from a loaded thread and can trigger `thread/closed`.
+- `thread/metadata/update` patches stored thread metadata, currently including persisted `gitInfo`.
+- `thread/unsubscribe` unsubscribes the current connection from a loaded thread and can trigger `thread/closed` after an inactivity grace period.
 - `thread/unarchive` restores an archived thread rollout back into the active sessions directory.
 - `thread/compact/start` triggers compaction and returns `{}` immediately.
 - `thread/rollback` drops the last N turns from the in-memory context and records a rollback marker in the thread's persisted JSONL log.
+- `thread/inject_items` appends raw Responses API items to a loaded thread's model-visible history without starting a user turn.
 
 ### Start or resume a thread
 
@@ -315,7 +368,7 @@
 
 ```json
 { "method": "thread/start", "id": 10, "params": {
-  "model": "gpt-5.1-codex",
+  "model": "gpt-5.4",
   "cwd": "/Users/me/project",
   "approvalPolicy": "never",
   "sandbox": "workspaceWrite",
@@ -378,6 +431,23 @@
 
 Unlike `thread/resume`, `thread/read` doesn't load the thread into memory or emit `thread/started`.
 
+### List thread turns
+
+Use `thread/turns/list` to page a stored thread's turn history without resuming it. Results default to newest-first so clients can fetch older turns with `nextCursor`. The response also includes `backwardsCursor`; pass it as `cursor` with `sortDirection: "asc"` to fetch turns newer than the first item from the earlier page.
+
+```json
+{ "method": "thread/turns/list", "id": 20, "params": {
+  "threadId": "thr_123",
+  "limit": 50,
+  "sortDirection": "desc"
+} }
+{ "id": 20, "result": {
+  "data": [],
+  "nextCursor": "older-turns-cursor-or-null",
+  "backwardsCursor": "newer-turns-cursor-or-null"
+} }
+```
+
 ### List threads (with pagination & filters)
 
 `thread/list` lets you render a history UI. Results default to newest-first by `createdAt`. Filters apply before pagination. Pass any combination of:
@@ -389,6 +459,7 @@
 - `sourceKinds` - restrict results to specific thread sources. When omitted or `[]`, the server defaults to interactive sources only: `cli` and `vscode`.
 - `archived` - when `true`, list archived threads only. When `false` or omitted, list non-archived threads (default).
 - `cwd` - restrict results to threads whose session current working directory exactly matches this path.
+- `searchTerm` - search stored thread summaries and metadata before pagination.
 
 `sourceKinds` accepts the following values:
 
@@ -422,6 +493,23 @@
 
 When `nextCursor` is `null`, you have reached the final page.
 
+### Update stored thread metadata
+
+Use `thread/metadata/update` to patch stored thread metadata without resuming the thread. Today this supports persisted `gitInfo`; omitted fields are left unchanged, and explicit `null` clears a stored value.
+
+```json
+{ "method": "thread/metadata/update", "id": 21, "params": {
+  "threadId": "thr_123",
+  "gitInfo": { "branch": "feature/sidebar-pr" }
+} }
+{ "id": 21, "result": {
+  "thread": {
+    "id": "thr_123",
+    "gitInfo": { "sha": null, "branch": "feature/sidebar-pr", "originUrl": null }
+  }
+} }
+```
+
 ### Track thread status changes
 
 `thread/status/changed` is emitted whenever a loaded thread's runtime status changes. The payload includes `threadId` and the new `status`.
@@ -450,14 +538,19 @@
 `thread/unsubscribe` removes the current connection's subscription to a thread. The response status is one of:
 
 - `unsubscribed` when the connection was subscribed and is now removed.
-- `notSubscribed` when the connection was not subscribed to that thread.
-- `notLoaded` when the thread is not loaded.
-
-If this was the last subscriber, the server unloads the thread and emits a `thread/status/changed` transition to `notLoaded` plus `thread/closed`.
+- `notSubscribed` when the connection wasn't subscribed to that thread.
+- `notLoaded` when the thread isn't loaded.
+
+If this was the last subscriber, the server keeps the thread loaded until it has no subscribers and no thread activity for 30 minutes. When the grace period expires, app-server unloads the thread and emits a `thread/status/changed` transition to `notLoaded` plus `thread/closed`.
 
 ```json
 { "method": "thread/unsubscribe", "id": 22, "params": { "threadId": "thr_123" } }
 { "id": 22, "result": { "status": "unsubscribed" } }
+```
+
+If the thread later expires:
+
+```json
 { "method": "thread/status/changed", "params": {
     "threadId": "thr_123",
     "status": { "type": "notLoaded" }
@@ -498,13 +591,35 @@
 { "id": 25, "result": {} }
 ```
 
+### Run a thread shell command
+
+Use `thread/shellCommand` for user-initiated shell commands that belong to a thread. The request returns immediately with `{}` while progress streams through standard `turn/*` and `item/*` notifications.
+
+This API runs outside the sandbox with full access and doesn't inherit the thread sandbox policy. Clients should expose it only for explicit user-initiated commands.
+
+If the thread already has an active turn, the command runs as an auxiliary action on that turn and its formatted output is injected into the turn's message stream. If the thread is idle, app-server starts a standalone turn for the shell command.
+
+```json
+{ "method": "thread/shellCommand", "id": 26, "params": { "threadId": "thr_b", "command": "git status --short" } }
+{ "id": 26, "result": {} }
+```
+
+### Clean background terminals
+
+Use `thread/backgroundTerminals/clean` to stop all running background terminals associated with a thread. This method is experimental and requires `capabilities.experimentalApi = true`.
+
+```json
+{ "method": "thread/backgroundTerminals/clean", "id": 27, "params": { "threadId": "thr_b" } }
+{ "id": 27, "result": {} }
+```
+
 ### Roll back recent turns
 
 Use `thread/rollback` to remove the last `numTurns` entries from the in-memory context and persist a rollback marker in the rollout log. The returned `thread` includes `turns` populated after the rollback.
 
 ```json
-{ "method": "thread/rollback", "id": 26, "params": { "threadId": "thr_b", "numTurns": 1 } }
-{ "id": 26, "result": { "thread": { "id": "thr_b", "name": "Bug bash notes", "ephemeral": false } } }
+{ "method": "thread/rollback", "id": 28, "params": { "threadId": "thr_b", "numTurns": 1 } }
+{ "id": 28, "result": { "thread": { "id": "thr_b", "name": "Bug bash notes", "ephemeral": false } } }
 ```
 
 ## Turns
@@ -570,7 +685,7 @@
     "writableRoots": ["/Users/me/project"],
     "networkAccess": true
   },
-  "model": "gpt-5.1-codex",
+  "model": "gpt-5.4",
   "effort": "medium",
   "summary": "concise",
   "personality": "friendly",
@@ -582,6 +697,24 @@
   }
 } }
 { "id": 30, "result": { "turn": { "id": "turn_456", "status": "inProgress", "items": [], "error": null } } }
+```
+
+### Inject items into a thread
+
+Use `thread/inject_items` to append prebuilt Responses API items to a loaded thread's prompt history without starting a user turn. These items are persisted to the rollout and included in subsequent model requests.
+
+```json
+{ "method": "thread/inject_items", "id": 31, "params": {
+  "threadId": "thr_123",
+  "items": [
+    {
+      "type": "message",
+      "role": "assistant",
+      "content": [{ "type": "output_text", "text": "Previously computed context." }]
+    }
+  ]
+} }
+{ "id": 31, "result": {} }
 ```
 
 ### Steer an active turn
@@ -713,6 +846,8 @@
 - The server rejects empty `command` arrays.
 - `sandboxPolicy` accepts the same shape used by `turn/start` (for example, `dangerFullAccess`, `readOnly`, `workspaceWrite`, `externalSandbox`).
 - When omitted, `timeoutMs` falls back to the server default.
+- Set `tty: true` for PTY-backed sessions, and use `processId` when you plan to follow up with `command/exec/write`, `command/exec/resize`, or `command/exec/terminate`.
+- Set `streamStdoutStderr: true` to receive `command/exec/outputDelta` notifications while the command is running.
 
 ### Read admin requirements (`configRequirements/read`)
 
@@ -763,6 +898,28 @@
 - `elevated` - run the elevated Windows sandbox setup path.
 - `unelevated` - run the legacy setup/preflight path.
 
+## Filesystem
+
+The v2 filesystem APIs operate on absolute paths. Use `fs/watch` when a client needs to invalidate UI state after a file or directory changes.
+
+```json
+{ "method": "fs/watch", "id": 54, "params": {
+  "watchId": "0195ec6b-1d6f-7c2e-8c7a-56f2c4a8b9d1",
+  "path": "/Users/me/project/.git/HEAD"
+} }
+{ "id": 54, "result": { "path": "/Users/me/project/.git/HEAD" } }
+{ "method": "fs/changed", "params": {
+  "watchId": "0195ec6b-1d6f-7c2e-8c7a-56f2c4a8b9d1",
+  "changedPaths": ["/Users/me/project/.git/HEAD"]
+} }
+{ "method": "fs/unwatch", "id": 55, "params": {
+  "watchId": "0195ec6b-1d6f-7c2e-8c7a-56f2c4a8b9d1"
+} }
+{ "id": 55, "result": {} }
+```
+
+Watching a file emits `fs/changed` for that file path, including updates delivered by replace or rename operations.
+
 ## Events
 
 Event notifications are the server-initiated stream for thread lifecycles, turn lifecycles, and the items within them. After you start or resume a thread, keep reading the active transport stream for `thread/started`, `thread/archived`, `thread/unarchived`, `thread/closed`, `thread/status/changed`, `turn/*`, `item/*`, and `serverRequest/resolved` notifications.
@@ -773,7 +930,7 @@
 
 - Exact-match only: `item/agentMessage/delta` suppresses only that method.
 - Unknown method names are ignored.
-- Applies to both legacy (`codex/event/*`) and v2 (`thread/*`, `turn/*`, `item/*`, etc.) notifications.
+- Applies to the current `thread/*`, `turn/*`, `item/*`, and related v2 notifications.
 - Doesn't apply to requests, responses, or errors.
 
 ### Fuzzy file search events (experimental)
@@ -984,6 +1141,8 @@
 } }
 ```
 
+The server also emits `skills/changed` notifications when watched local skill files change. Treat this as an invalidation signal and rerun `skills/list` with your current params when needed.
+
 To enable or disable a skill by path:
 
 ```json
@@ -1150,7 +1309,7 @@
 
 ### Detect and import external agent config
 
-Use `externalAgentConfig/detect` to discover migratable external-agent artifacts, then pass the selected entries to `externalAgentConfig/import`.
+Use `externalAgentConfig/detect` to discover external-agent artifacts that can be migrated, then pass the selected entries to `externalAgentConfig/import`.
 
 Detection example:
 
@@ -1190,32 +1349,46 @@
 { "id": 64, "result": {} }
 ```
 
-Supported `itemType` values are `AGENTS_MD`, `CONFIG`, `SKILLS`, and `MCP_SERVER_CONFIG`. Detection returns only items that still have work to do. For example, AGENTS migration is skipped when `AGENTS.md` already exists and is non-empty, and skill imports do not overwrite existing skill directories.
+When a request includes plugin imports, the server emits `externalAgentConfig/import/completed` after the import finishes. This notification may arrive immediately after the response or after background remote imports complete.
+
+Supported `itemType` values are `AGENTS_MD`, `CONFIG`, `SKILLS`, `PLUGINS`,
+and `MCP_SERVER_CONFIG`. For `PLUGINS` items, `details.plugins` lists each
+`marketplaceName` and the `pluginNames` Codex can try to migrate. Detection
+returns only items that still have work to do. For example, Codex skips AGENTS
+migration when `AGENTS.md` already exists and is non-empty, and skill imports
+don't overwrite existing skill directories.
+
+When detecting plugins from `.claude/settings.json`, Codex reads configured
+marketplace sources from `extraKnownMarketplaces`. If `enabledPlugins` contains
+plugins from `claude-plugins-official` but the marketplace source is missing,
+Codex infers `anthropics/claude-plugins-official` as the source.
 
 ## Auth endpoints
 
-The JSON-RPC auth/account surface exposes request/response methods plus server-initiated notifications (no `id`). Use these to determine auth state, start or cancel logins, logout, and inspect ChatGPT rate limits.
+The JSON-RPC auth/account surface exposes request/response methods plus server-initiated notifications (no `id`). Use these to determine auth state, start or cancel logins, logout, inspect ChatGPT rate limits, and notify workspace owners about depleted credits or usage limits.
 
 ### Authentication modes
 
-Codex supports three authentication modes. `account/updated.authMode` shows the active mode, and `account/read` also reports it.
-
-- **API key (`apikey`)** - the caller supplies an OpenAI API key and Codex stores it for API requests.
-- **ChatGPT managed (`chatgpt`)** - Codex owns the ChatGPT OAuth flow, persists tokens, and refreshes them automatically.
-- **ChatGPT external tokens (`chatgptAuthTokens`)** - a host app supplies `idToken` and `accessToken` directly. Codex stores these tokens in memory, and the host app must refresh them when asked.
+Codex supports these authentication modes. `account/updated.authMode` shows the active mode and includes the current ChatGPT `planType` when available. `account/read` also reports account and plan details.
+
+- **API key (`apikey`)** - the caller supplies an OpenAI API key with `type: "apiKey"`, and Codex stores it for API requests.
+- **ChatGPT managed (`chatgpt`)** - Codex owns the ChatGPT OAuth flow, persists tokens, and refreshes them automatically. Start with `type: "chatgpt"` for the browser flow or `type: "chatgptDeviceCode"` for the device-code flow.
+- **ChatGPT external tokens (`chatgptAuthTokens`)** - experimental and intended for host apps that already own the user's ChatGPT auth lifecycle. The host app supplies an `accessToken`, `chatgptAccountId`, and optional `chatgptPlanType` directly, and must refresh the token when asked.
 
 ### API overview
 
 - `account/read` - fetch current account info; optionally refresh tokens.
-- `account/login/start` - begin login (`apiKey`, `chatgpt`, or `chatgptAuthTokens`).
+- `account/login/start` - begin login (`apiKey`, `chatgpt`, `chatgptDeviceCode`, or experimental `chatgptAuthTokens`).
 - `account/login/completed` (notify) - emitted when a login attempt finishes (success or error).
-- `account/login/cancel` - cancel a pending ChatGPT login by `loginId`.
+- `account/login/cancel` - cancel a pending managed ChatGPT login by `loginId`.
 - `account/logout` - sign out; triggers `account/updated`.
-- `account/updated` (notify) - emitted whenever auth mode changes (`authMode`: `apikey`, `chatgpt`, `chatgptAuthTokens`, or `null`).
+- `account/updated` (notify) - emitted whenever auth mode changes (`authMode`: `apikey`, `chatgpt`, `chatgptAuthTokens`, or `null`) and includes `planType` when available.
 - `account/chatgptAuthTokens/refresh` (server request) - request fresh externally managed ChatGPT tokens after an authorization error.
 - `account/rateLimits/read` - fetch ChatGPT rate limits.
 - `account/rateLimits/updated` (notify) - emitted whenever a user's ChatGPT rate limits change.
+- `account/sendAddCreditsNudgeEmail` - ask ChatGPT to email a workspace owner about depleted credits or a reached usage limit.
 - `mcpServer/oauthLogin/completed` (notify) - emitted after a `mcpServer/oauth/login` flow finishes; payload includes `{ name, success, error? }`.
+- `mcpServer/startupStatus/updated` (notify) - emitted when a configured MCP server's startup status changes for a loaded thread; payload includes `{ name, status, error }`.
 
 ### 1) Check auth state
 
@@ -1289,7 +1462,10 @@
    ```
 
    ```json
-   { "method": "account/updated", "params": { "authMode": "apikey" } }
+   {
+     "method": "account/updated",
+     "params": { "authMode": "apikey", "planType": null }
+   }
    ```
 
 ### 3) Log in with ChatGPT (browser flow)
@@ -1322,12 +1498,58 @@
    ```
 
    ```json
-   { "method": "account/updated", "params": { "authMode": "chatgpt" } }
+   {
+     "method": "account/updated",
+     "params": { "authMode": "chatgpt", "planType": "plus" }
+   }
    ```
 
-### 3b) Log in with externally managed ChatGPT tokens (`chatgptAuthTokens`)
-
-Use this mode when a host application owns the user's ChatGPT auth lifecycle and supplies tokens directly.
+### 3b) Log in with ChatGPT (device-code flow)
+
+Use this flow when your client owns the sign-in ceremony or when a browser callback is brittle.
+
+1. Start:
+
+   ```json
+   {
+     "method": "account/login/start",
+     "id": 4,
+     "params": { "type": "chatgptDeviceCode" }
+   }
+   ```
+
+   ```json
+   {
+     "id": 4,
+     "result": {
+       "type": "chatgptDeviceCode",
+       "loginId": "<uuid>",
+       "verificationUrl": "https://auth.openai.com/codex/device",
+       "userCode": "ABCD-1234"
+     }
+   }
+   ```
+
+2. Show `verificationUrl` and `userCode` to the user; the frontend owns the UX.
+3. Wait for notifications:
+
+   ```json
+   {
+     "method": "account/login/completed",
+     "params": { "loginId": "<uuid>", "success": true, "error": null }
+   }
+   ```
+
+   ```json
+   {
+     "method": "account/updated",
+     "params": { "authMode": "chatgpt", "planType": "plus" }
+   }
+   ```
+
+### 3c) Log in with externally managed ChatGPT tokens (`chatgptAuthTokens`)
+
+Use this experimental mode only when a host application owns the user's ChatGPT auth lifecycle and supplies tokens directly. Clients must set `capabilities.experimentalApi = true` during `initialize` before using this login type.
 
 1. Send:
 
@@ -1337,8 +1559,9 @@
      "id": 7,
      "params": {
        "type": "chatgptAuthTokens",
-       "idToken": "<jwt>",
-       "accessToken": "<jwt>"
+       "accessToken": "<jwt>",
+       "chatgptAccountId": "org-123",
+       "chatgptPlanType": "business"
      }
    }
    ```
@@ -1361,7 +1584,7 @@
    ```json
    {
      "method": "account/updated",
-     "params": { "authMode": "chatgptAuthTokens" }
+     "params": { "authMode": "chatgptAuthTokens", "planType": "business" }
    }
    ```
 
@@ -1373,7 +1596,7 @@
   "id": 8,
   "params": { "reason": "unauthorized", "previousAccountId": "org-123" }
 }
-{ "id": 8, "result": { "idToken": "<jwt>", "accessToken": "<jwt>" } }
+{ "id": 8, "result": { "accessToken": "<jwt>", "chatgptAccountId": "org-123", "chatgptPlanType": "business" } }
 ```
 
 The server retries the original request after a successful refresh response. Requests time out after about 10 seconds.
@@ -1390,7 +1613,7 @@
 ```json
 { "method": "account/logout", "id": 5 }
 { "id": 5, "result": {} }
-{ "method": "account/updated", "params": { "authMode": null } }
+{ "method": "account/updated", "params": { "authMode": null, "planType": null } }
 ```
 
 ### 6) Rate limits (ChatGPT)
@@ -1402,20 +1625,23 @@
     "limitId": "codex",
     "limitName": null,
     "primary": { "usedPercent": 25, "windowDurationMins": 15, "resetsAt": 1730947200 },
-    "secondary": null
+    "secondary": null,
+    "rateLimitReachedType": null
   },
   "rateLimitsByLimitId": {
     "codex": {
       "limitId": "codex",
       "limitName": null,
       "primary": { "usedPercent": 25, "windowDurationMins": 15, "resetsAt": 1730947200 },
-      "secondary": null
+      "secondary": null,
+      "rateLimitReachedType": null
     },
     "codex_other": {
       "limitId": "codex_other",
       "limitName": "codex_other",
       "primary": { "usedPercent": 42, "windowDurationMins": 60, "resetsAt": 1730950800 },
-      "secondary": null
+      "secondary": null,
+      "rateLimitReachedType": null
     }
   }
 } }
@@ -1435,4 +1661,18 @@
 - `limitName` is an optional user-facing label for the bucket.
 - `usedPercent` is current usage within the quota window.
 - `windowDurationMins` is the quota window length.
-- `resetsAt` is a Unix timestamp (seconds) for the next reset.+- `resetsAt` is a Unix timestamp (seconds) for the next reset.
+- `planType` is included when the backend returns the ChatGPT plan associated with a bucket.
+- `credits` is included when the backend returns remaining workspace credit details.
+- `rateLimitReachedType` identifies the backend-classified limit state when one has been reached.
+
+### 7) Notify a workspace owner about a limit
+
+Use `account/sendAddCreditsNudgeEmail` to ask ChatGPT to email a workspace owner when credits are depleted or a usage limit has been reached.
+
+```json
+{ "method": "account/sendAddCreditsNudgeEmail", "id": 7, "params": { "creditType": "credits" } }
+{ "id": 7, "result": { "status": "sent" } }
+```
+
+Use `creditType: "credits"` when workspace credits are depleted, or `creditType: "usage_limit"` when the workspace usage limit has been reached. If the owner was already notified recently, the response status is `cooldown_active`.
```
#### https://developers.openai.com/codex/auth.md

```diff
--- a/https://developers.openai.com/codex/auth.md
+++ b/https://developers.openai.com/codex/auth.md
@@ -26,7 +26,11 @@
 
 OpenAI bills API key usage through your OpenAI Platform account at standard API rates. See the [API pricing page](https://openai.com/api/pricing/).
 
-Recommendation is to use API key authentication for programmatic Codex CLI workflows (for example CI/CD jobs). Do not expose Codex execution in untrusted or publicly triggerable environments.
+Features that rely on ChatGPT credits, such as [fast mode](https://developers.openai.com/codex/speed), are
+available only when you sign in with ChatGPT. If you sign in with an API key,
+Codex uses standard API pricing instead.
+
+Recommendation is to use API key authentication for programmatic Codex CLI workflows (for example CI/CD jobs). Don't expose Codex execution in untrusted or public environments.
 
 ## Secure your Codex cloud account
 
@@ -86,6 +90,25 @@
 If the active credentials don't match the configured restrictions, Codex logs the user out and exits.
 
 These settings are commonly applied via managed configuration rather than per-user setup. See [Managed configuration](https://developers.openai.com/codex/enterprise/managed-configuration).
+
+## Login diagnostics
+
+Direct `codex login` runs write a dedicated `codex-login.log` file under
+your configured log directory. Use it when you need to debug browser-login or
+device-code failures, or when support asks for login-specific logs.
+
+## Custom CA bundles
+
+If your network uses a corporate TLS proxy or private root CA, set
+`CODEX_CA_CERTIFICATE` to a PEM bundle before logging in. When
+`CODEX_CA_CERTIFICATE` is unset, Codex falls back to `SSL_CERT_FILE`. The same
+custom CA settings apply to login, normal HTTPS requests, and secure websocket
+connections.
+
+```shell
+export CODEX_CA_CERTIFICATE=/path/to/corporate-root-ca.pem
+codex login
+```
 
 ## Login on headless devices
 

```
#### https://developers.openai.com/codex/cli.md

```diff
--- a/https://developers.openai.com/codex/cli.md
+++ b/https://developers.openai.com/codex/cli.md
@@ -3,7 +3,7 @@
 Codex CLI is OpenAI's coding agent that you can run locally from your terminal. It can read, change, and run code on your machine in the selected directory.
 It's [open source](https://github.com/openai/codex) and built in Rust for speed and efficiency.
 
-Codex is included with ChatGPT Plus, Pro, Business, Edu, and Enterprise plans. Learn more about [what's included](https://developers.openai.com/codex/pricing).
+ChatGPT Plus, Pro, Business, Edu, and Enterprise plans include Codex. Learn more about [what's included](https://developers.openai.com/codex/pricing).
 
 <YouTubeEmbed
   title="Codex CLI overview"
@@ -16,9 +16,12 @@
 
 <CliSetupSteps client:load />
 
-The Codex CLI is available on macOS and Linux. Windows support is
-  experimental. For the best Windows experience, use Codex in a WSL workspace
-  and follow our <a href="/codex/windows">Windows setup guide</a>.
+The Codex CLI is available on macOS, Windows, and Linux. On Windows, run Codex
+  natively in PowerShell with the Windows sandbox, or use WSL2 when you need a
+  Linux-native environment. For setup details, see the{" "}
+  <a href="/codex/windows">Windows setup guide</a>.
+
+If you're new to Codex, read the [best practices guide](https://developers.openai.com/codex/learn/best-practices).
 
 ---
 
@@ -46,6 +49,13 @@
 Attach screenshots or design specs so Codex reads them alongside your prompt.
 
   </BentoContent>
+  <BentoContent href="/codex/cli/features#image-generation">
+
+### Image generation
+
+Generate or edit images directly in the CLI, and attach references when you want Codex to iterate on an existing asset.
+
+  </BentoContent>
 
   <BentoContent href="/codex/cli/features#running-local-code-review">
 
@@ -55,11 +65,11 @@
 
   </BentoContent>
 
-  <BentoContent href="/codex/multi-agent">
+  <BentoContent href="/codex/subagents">
 
-### Use multi-agent
+### Use subagents
 
-Enable experimental multi-agent collaboration and parallelize complex tasks.
+Use subagents to parallelize complex tasks.
 
   </BentoContent>
 
@@ -79,7 +89,7 @@
 
   </BentoContent>
 
-  <BentoContent href="/codex/sdk#using-codex-cli-programmatically">
+  <BentoContent href="/codex/noninteractive">
 
 ### Scripting Codex
 

```
#### https://developers.openai.com/codex/cli/features.md

```diff
--- a/https://developers.openai.com/codex/cli/features.md
+++ b/https://developers.openai.com/codex/cli/features.md
@@ -20,10 +20,12 @@
 
 - Send prompts, code snippets, or screenshots (see [image inputs](#image-inputs)) directly into the composer.
 - Watch Codex explain its plan before making a change, and approve or reject steps inline.
-- Read syntax-highlighted markdown code blocks and diffs in the TUI, then use `/theme` to preview and save a preferred color theme.
+- Read syntax-highlighted markdown code blocks and diffs in the TUI, then use `/theme` to preview and save a preferred theme.
 - Use `/clear` to wipe the terminal and start a fresh chat, or press <kbd>Ctrl</kbd>+<kbd>L</kbd> to clear the screen without starting a new conversation.
-- Use `/copy` to copy the latest completed Codex output. If a turn is still running, Codex copies the most recent finished output instead of in-progress text.
+- Use `/copy` or press <kbd>Ctrl</kbd>+<kbd>O</kbd> to copy the latest completed Codex output. If a turn is still running, Codex copies the most recent finished output instead of in-progress text.
+- Press <kbd>Tab</kbd> while Codex is running to queue follow-up text, slash commands, or `!` shell commands for the next turn.
 - Navigate draft history in the composer with <kbd>Up</kbd>/<kbd>Down</kbd>; Codex restores prior draft text and image placeholders.
+- Press <kbd>Ctrl</kbd>+<kbd>R</kbd> to search prompt history from the composer, then press <kbd>Enter</kbd> to accept a match or <kbd>Esc</kbd> to cancel.
 - Press <kbd>Ctrl</kbd>+<kbd>C</kbd> or use `/exit` to close the interactive session when you're done.
 
 ## Resuming conversations
@@ -44,14 +46,78 @@
 
 Each resumed run keeps the original transcript, plan history, and approvals, so Codex can use prior context while you supply new instructions. Override the working directory with `--cd` or add extra roots with `--add-dir` if you need to steer the environment before resuming.
 
+## Connect the TUI to a remote app server
+
+Remote TUI mode lets you run the Codex app server on one machine and use the Codex terminal UI from another machine. This is useful when the code, credentials, or execution environment live on a remote host, but you want the local interactive TUI experience.
+
+Start the app server on the machine that should own the workspace and run commands:
+
+```bash
+codex app-server --listen ws://127.0.0.1:4500
+```
+
+Then connect from the machine running the TUI:
+
+```bash
+codex --remote ws://127.0.0.1:4500
+```
+
+For access from another machine, bind the app server to a reachable interface, for example:
+
+```bash
+codex app-server --listen ws://0.0.0.0:4500
+```
+
+`--remote` accepts explicit `ws://host:port` and `wss://host:port` addresses only. For plain WebSocket connections, prefer local-host addresses or SSH port forwarding. If you expose the listener beyond the local host, configure authentication before real remote use and put authenticated non-local connections behind TLS.
+
+Codex supports these WebSocket authentication modes for remote TUI connections:
+
+- **No WebSocket auth**: Best for local-host listeners or SSH port-forwarded connections. Codex can start non-local listeners without auth, but logs a warning and the startup banner reminds you to configure auth before real remote use.
+- **Capability token**: Store a shared token in a file on the app-server host, start the server with `--ws-auth capability-token --ws-token-file /abs/path/to/token`, then set the same token in an environment variable on the TUI host and pass `--remote-auth-token-env <ENV_VAR>`.
+- **Signed bearer token**: Store an HMAC shared secret in a file on the app-server host, start the server with `--ws-auth signed-bearer-token --ws-shared-secret-file /abs/path/to/secret`, and have the TUI send a signed JWT bearer token through `--remote-auth-token-env <ENV_VAR>`. The shared secret must be at least 32 bytes. Signed tokens use HS256 and must include `exp`; Codex also validates `nbf`, `iss`, and `aud` when those claims or server options are present.
+
+To create a capability token on the app-server host, generate a random token file with permissions that only your user can read:
+
+```bash
+TOKEN_FILE="$HOME/.codex/codex-app-server-token"
+install -d -m 700 "$(dirname "$TOKEN_FILE")"
+openssl rand -base64 32 > "$TOKEN_FILE"
+chmod 600 "$TOKEN_FILE"
+```
+
+Treat the token file like a password, and regenerate it if it leaks.
+
+Then start the app server with that token file. For example, with a capability token behind a TLS proxy:
+
+```bash
+# Remote host
+TOKEN_FILE="$HOME/.codex/codex-app-server-token"
+codex app-server \
+  --listen ws://0.0.0.0:4500 \
+  --ws-auth capability-token \
+  --ws-token-file "$TOKEN_FILE"
+
+# TUI host
+export CODEX_REMOTE_AUTH_TOKEN="$(ssh devbox 'cat ~/.codex/codex-app-server-token')"
+codex --remote wss://codex-devbox.example.com:4500 \
+  --remote-auth-token-env CODEX_REMOTE_AUTH_TOKEN
+```
+
+The TUI sends remote auth tokens as `Authorization: Bearer <token>` during the WebSocket handshake. Codex only sends those tokens over `wss://` URLs or `ws://` URLs whose host is `localhost`, `127.0.0.1`, or `::1`, so put non-local remote listeners behind TLS if clients need to authenticate over the network.
+
 ## Models and reasoning
 
-For most tasks in Codex, `gpt-5.4` is the recommended model. It brings the industry-leading coding capabilities of `gpt-5.3-codex` to OpenAI's flagship frontier model, combining frontier coding performance with stronger reasoning, native computer use, and broader professional workflows. For extra fast tasks, ChatGPT Pro subscribers have access to the GPT-5.3-Codex-Spark model in research preview.
+For most tasks in Codex, `gpt-5.5` is the recommended model when it is
+available. It is OpenAI's newest frontier model for complex coding, computer
+use, knowledge work, and research workflows, with stronger planning, tool use,
+and follow-through on multi-step tasks. If `gpt-5.5` is not yet available,
+continue using `gpt-5.4`. For extra fast tasks, ChatGPT Pro subscribers have
+access to the GPT-5.3-Codex-Spark model in research preview.
 
 Switch models mid-session with the `/model` command, or specify one when launching the CLI.
 
 ```bash
-codex --model gpt-5.4
+codex --model gpt-5.5
 ```
 
 [Learn more about the models available in Codex](https://developers.openai.com/codex/models).
@@ -68,9 +134,13 @@
 
 `codex features enable <feature>` and `codex features disable <feature>` write to `~/.codex/config.toml`. If you launch Codex with `--profile`, Codex stores the change in that profile rather than the root configuration.
 
-## Multi-agents (experimental)
-
-Use Codex multi-agent workflows to parallelize larger tasks. For setup, role configuration (`[agents]` in `config.toml`), and examples, see [Multi-agents](https://developers.openai.com/codex/multi-agent).
+## Subagents
+
+Use Codex subagent workflows to parallelize larger tasks. For setup, role configuration (`[agents]` in `config.toml`), and examples, see [Subagents](https://developers.openai.com/codex/subagents).
+
+Codex only spawns subagents when you explicitly ask it to. Because each
+subagent does its own model and tool work, subagent workflows consume more
+tokens than comparable single-agent runs.
 
 ## Image inputs
 
@@ -85,6 +155,16 @@
 ```
 
 Codex accepts common formats such as PNG and JPEG. Use comma-separated filenames for two or more images, and combine them with text instructions to add context.
+
+## Image generation
+
+Ask Codex to generate or edit images directly in the CLI. This works well for assets such as icons, banners, illustrations, sprite sheets, and placeholder art. If you want Codex to transform or extend an existing asset, attach a reference image with your prompt.
+
+You can ask in natural language or explicitly invoke the image generation skill by including `$imagegen` in your prompt.
+
+Built-in image generation uses `gpt-image-2`, counts toward your general Codex usage limits, and uses included limits 3-5x faster on average than similar turns without image generation, depending on image quality and size. For details, see [Pricing](https://developers.openai.com/codex/pricing#image-generation-usage-limits). For prompting tips and model details, see the [image generation guide](https://developers.openai.com/api/docs/guides/image-generation).
+
+For larger batches of image generation, set `OPENAI_API_KEY` in your environment variables and ask Codex to generate images through the API so API pricing applies instead.
 
 ## Syntax highlighting and themes
 
@@ -174,7 +254,7 @@
 
 ## Slash commands
 
-Slash commands give you quick access to specialized workflows like `/review`, `/fork`, or your own reusable prompts. Codex ships with a curated set of built-ins, and you can create custom ones for team-specific tasks or personal shortcuts.
+Slash commands give you quick access to specialized workflows like `/review`, `/fork`, `/side`, or your own reusable prompts. Codex ships with a curated set of built-ins, and you can create custom ones for team-specific tasks or personal shortcuts.
 
 See the [slash commands guide](https://developers.openai.com/codex/guides/slash-commands) to browse the catalog of built-ins, learn how to author custom commands, and understand where they live on disk.
 
@@ -193,7 +273,7 @@
 ## Tips and shortcuts
 
 - Type `@` in the composer to open a fuzzy file search over the workspace root; press <kbd>Tab</kbd> or <kbd>Enter</kbd> to drop the highlighted path into your message.
-- Press <kbd>Enter</kbd> while Codex is running to inject new instructions into the current turn, or press <kbd>Tab</kbd> to queue a follow-up prompt for the next turn.
+- Press <kbd>Enter</kbd> while Codex is running to inject new instructions into the current turn, or press <kbd>Tab</kbd> to queue follow-up input for the next turn. Queued input can be a normal prompt, a slash command such as `/review`, or a `!` shell command. Codex parses queued slash commands when they run.
 - Prefix a line with `!` to run a local shell command (for example, `!ls`). Codex treats the output like a user-provided command result and still applies your approval and sandbox settings.
 - Tap <kbd>Esc</kbd> twice while the composer is empty to edit your previous user message. Continue pressing <kbd>Esc</kbd> to walk further back in the transcript, then hit <kbd>Enter</kbd> to fork from that point.
 - Launch Codex from any directory using `codex --cd <path>` to set the working root without running `cd` first. The active path appears in the TUI header.

```
#### https://developers.openai.com/codex/cli/reference.md

```diff
--- a/https://developers.openai.com/codex/cli/reference.md
+++ b/https://developers.openai.com/codex/cli/reference.md
@@ -17,7 +17,7 @@
     key: "--model, -m",
     type: "string",
     description:
-      "Override the model set in configuration (for example `gpt-5-codex`).",
+      "Override the model set in configuration (for example `gpt-5.4`).",
   },
   {
     key: "--oss",
@@ -45,13 +45,6 @@
       "Control when Codex pauses for human approval before running a command. `on-failure` is deprecated; prefer `on-request` for interactive runs or `never` for non-interactive runs.",
   },
   {
-    key: "--full-auto",
-    type: "boolean",
-    defaultValue: "false",
-    description:
-      "Shortcut for low-friction local work: sets `--ask-for-approval on-request` and `--sandbox workspace-write`.",
-  },
-  {
     key: "--dangerously-bypass-approvals-and-sandbox, --yolo",
     type: "boolean",
     defaultValue: "false",
@@ -83,6 +76,18 @@
     defaultValue: "false",
     description:
       "Disable alternate screen mode for the TUI (overrides `tui.alternate_screen` for this run).",
+  },
+  {
+    key: "--remote",
+    type: "ws://host:port | wss://host:port",
+    description:
+      "Connect the interactive TUI to a remote app-server WebSocket endpoint. Supported for `codex`, `codex resume`, and `codex fork`; other subcommands reject remote mode.",
+  },
+  {
+    key: "--remote-auth-token-env",
+    type: "ENV_VAR",
+    description:
+      "Read a bearer token from this environment variable and send it when connecting with `--remote`. Requires `--remote`; tokens are only sent over `wss://` URLs or `ws://` URLs whose host is `localhost`, `127.0.0.1`, or `::1`.",
   },
   {
     key: "--enable",
@@ -124,7 +129,7 @@
     href: "/codex/cli/reference#codex-app",
     type: "stable",
     description:
-      "Launch the Codex desktop app on macOS, optionally opening a specific workspace path.",
+      "Launch the Codex desktop app on macOS or Windows. On macOS, Codex can open a workspace path; on Windows, Codex prints the path to open.",
   },
   {
     key: "codex debug app-server send-message-v2",
@@ -132,6 +137,13 @@
     type: "experimental",
     description:
       "Debug app-server by sending a single V2 message through the built-in test client.",
+  },
+  {
+    key: "codex debug models",
+    href: "/codex/cli/reference#codex-debug-models",
+    type: "experimental",
+    description:
+      "Print the raw model catalog Codex sees, including an option to inspect only the bundled catalog.",
   },
   {
     key: "codex apply",
@@ -196,6 +208,13 @@
       "Manage Model Context Protocol servers (list, add, remove, authenticate).",
   },
   {
+    key: "codex plugin marketplace",
+    href: "/codex/cli/reference#codex-plugin-marketplace",
+    type: "experimental",
+    description:
+      "Add, upgrade, or remove plugin marketplaces from Git or local sources.",
+  },
+  {
     key: "codex mcp-server",
     href: "/codex/cli/reference#codex-mcp-server",
     type: "experimental",
@@ -221,7 +240,14 @@
     href: "/codex/cli/reference#codex-sandbox",
     type: "experimental",
     description:
-      "Run arbitrary commands inside Codex-provided macOS seatbelt or Linux sandboxes (Landlock by default, optional bubblewrap pipeline).",
+      "Run arbitrary commands inside Codex-provided macOS, Linux, or Windows sandboxes.",
+  },
+  {
+    key: "codex update",
+    href: "/codex/cli/reference#codex-update",
+    type: "stable",
+    description:
+      "Check for and apply a Codex CLI update when the installed release supports self-update.",
   },
 ];
 
@@ -266,7 +292,7 @@
     type: "boolean",
     defaultValue: "false",
     description:
-      "Apply the low-friction automation preset (`workspace-write` sandbox and `on-request` approvals).",
+      "Deprecated compatibility flag. Prefer `--sandbox workspace-write`; Codex prints a warning when this flag is used.",
   },
   {
     key: "--dangerously-bypass-approvals-and-sandbox, --yolo",
@@ -292,6 +318,20 @@
     type: "boolean",
     defaultValue: "false",
     description: "Run without persisting session rollout files to disk.",
+  },
+  {
+    key: "--ignore-user-config",
+    type: "boolean",
+    defaultValue: "false",
+    description:
+      "Do not load `$CODEX_HOME/config.toml`. Authentication still uses `CODEX_HOME`.",
+  },
+  {
+    key: "--ignore-rules",
+    type: "boolean",
+    defaultValue: "false",
+    description:
+      "Do not load user or project execpolicy `.rules` files for this run.",
   },
   {
     key: "--output-schema",
@@ -338,7 +378,44 @@
     type: "stdio:// | ws://IP:PORT",
     defaultValue: "stdio://",
     description:
-      "Transport listener URL. `ws://` is experimental and intended for development/testing.",
+      "Transport listener URL. Use `ws://IP:PORT` to expose a WebSocket endpoint for remote clients.",
+  },
+  {
+    key: "--ws-auth",
+    type: "capability-token | signed-bearer-token",
+    description:
+      "Authentication mode for app-server WebSocket clients. If omitted, WebSocket auth is disabled; non-local listeners warn during startup.",
+  },
+  {
+    key: "--ws-token-file",
+    type: "absolute path",
+    description:
+      "File containing the shared capability token. Required with `--ws-auth capability-token`.",
+  },
+  {
+    key: "--ws-shared-secret-file",
+    type: "absolute path",
+    description:
+      "File containing the HMAC shared secret used to validate signed JWT bearer tokens. Required with `--ws-auth signed-bearer-token`.",
+  },
+  {
+    key: "--ws-issuer",
+    type: "string",
+    description:
+      "Expected `iss` claim for signed bearer tokens. Requires `--ws-auth signed-bearer-token`.",
+  },
+  {
+    key: "--ws-audience",
+    type: "string",
+    description:
+      "Expected `aud` claim for signed bearer tokens. Requires `--ws-auth signed-bearer-token`.",
+  },
+  {
+    key: "--ws-max-clock-skew-seconds",
+    type: "number",
+    defaultValue: "30",
+    description:
+      "Clock skew allowance when validating signed bearer token `exp` and `nbf` claims. Requires `--ws-auth signed-bearer-token`.",
   },
 ];
 
@@ -348,13 +425,13 @@
     type: "path",
     defaultValue: ".",
     description:
-      "Workspace path to open in Codex Desktop (`codex app` is available on macOS only).",
+      "Workspace path for Codex Desktop. On macOS, Codex opens this path; on Windows, Codex prints the path.",
   },
   {
     key: "--download-url",
     type: "url",
     description:
-      "Advanced override for the Codex desktop DMG download URL used during install.",
+      "Advanced override for the Codex desktop installer URL used during install.",
   },
 ];
 
@@ -364,6 +441,16 @@
     type: "string",
     description:
       "Message text sent to app-server through the built-in V2 test-client flow.",
+  },
+];
+
+export const debugModelsOptions = [
+  {
+    key: "--bundled",
+    type: "boolean",
+    defaultValue: "false",
+    description:
+      "Skip refresh and print only the model catalog bundled with the current Codex binary.",
   },
 ];
 
@@ -521,11 +608,36 @@
 
 export const sandboxMacOptions = [
   {
-    key: "--full-auto",
-    type: "boolean",
-    defaultValue: "false",
-    description:
-      "Grant write access to the current workspace and `/tmp` without approvals.",
+    key: "--permissions-profile",
+    type: "NAME",
+    description:
+      "Apply a named permissions profile from the active configuration stack.",
+  },
+  {
+    key: "--cd, -C",
+    type: "DIR",
+    description:
+      "Working directory used for profile resolution and command execution. Requires `--permissions-profile`.",
+  },
+  {
+    key: "--include-managed-config",
+    type: "boolean",
+    defaultValue: "false",
+    description:
+      "Include managed requirements while resolving an explicit permissions profile. Requires `--permissions-profile`.",
+  },
+  {
+    key: "--allow-unix-socket",
+    type: "path",
+    description:
+      "Allow the sandboxed command to bind or connect Unix sockets rooted at this path. Repeat to allow multiple paths.",
+  },
+  {
+    key: "--log-denials",
+    type: "boolean",
+    defaultValue: "false",
+    description:
+      "Capture macOS sandbox denials with `log stream` while the command runs and print them after exit.",
   },
   {
     key: "--config, -c",
@@ -543,11 +655,23 @@
 
 export const sandboxLinuxOptions = [
   {
-    key: "--full-auto",
-    type: "boolean",
-    defaultValue: "false",
-    description:
-      "Grant write access to the current workspace and `/tmp` inside the Landlock sandbox.",
+    key: "--permissions-profile",
+    type: "NAME",
+    description:
+      "Apply a named permissions profile from the active configuration stack.",
+  },
+  {
+    key: "--cd, -C",
+    type: "DIR",
+    description:
+      "Working directory used for profile resolution and command execution. Requires `--permissions-profile`.",
+  },
+  {
+    key: "--include-managed-config",
+    type: "boolean",
+    defaultValue: "false",
+    description:
+      "Include managed requirements while resolving an explicit permissions profile. Requires `--permissions-profile`.",
   },
   {
     key: "--config, -c",
@@ -560,6 +684,40 @@
     type: "var-args",
     description:
       "Command to execute under Landlock + seccomp. Provide the executable after `--`.",
+  },
+];
+
+export const sandboxWindowsOptions = [
+  {
+    key: "--permissions-profile",
+    type: "NAME",
+    description:
+      "Apply a named permissions profile from the active configuration stack.",
+  },
+  {
+    key: "--cd, -C",
+    type: "DIR",
+    description:
+      "Working directory used for profile resolution and command execution. Requires `--permissions-profile`.",
+  },
+  {
+    key: "--include-managed-config",
+    type: "boolean",
+    defaultValue: "false",
+    description:
+      "Include managed requirements while resolving an explicit permissions profile. Requires `--permissions-profile`.",
+  },
+  {
+    key: "--config, -c",
+    type: "key=value",
+    description:
+      "Configuration overrides applied before launching the sandbox (repeatable).",
+  },
+  {
+    key: "COMMAND...",
+    type: "var-args",
+    description:
+      "Command to execute under the native Windows sandbox. Provide the executable after `--`.",
   },
 ];
 
@@ -679,6 +837,24 @@
     type: "ENV_VAR",
     description:
       "Environment variable whose value is sent as a bearer token when connecting to a streamable HTTP server.",
+  },
+];
+
+export const marketplaceCommands = [
+  {
+    key: "add <source>",
+    type: "[--ref REF] [--sparse PATH]",
+    description:
+      "Install a plugin marketplace from GitHub shorthand, a Git URL, an SSH URL, or a local marketplace root directory. `--sparse` is supported only for Git sources and can be repeated.",
+  },
+  {
+    key: "upgrade [marketplace-name]",
+    description:
+      "Refresh one configured Git marketplace, or all configured Git marketplaces when no name is provided.",
+  },
+  {
+    key: "remove <marketplace-name>",
+    description: "Remove a configured plugin marketplace.",
   },
 ];
 
@@ -715,7 +891,9 @@
 
 ### `codex` (interactive)
 
-Running `codex` with no subcommand launches the interactive terminal UI (TUI). The agent accepts the global flags above plus image attachments. Web search defaults to cached mode; use `--search` to switch to live browsing and `--full-auto` to let Codex run most commands without prompts.
+Running `codex` with no subcommand launches the interactive terminal UI (TUI). The agent accepts the global flags above plus image attachments. Web search defaults to cached mode; use `--search` to switch to live browsing. For low-friction local work, use `--sandbox workspace-write --ask-for-approval on-request`.
+
+Use `--remote ws://host:port` or `--remote wss://host:port` to connect the TUI to an app server started with `codex app-server --listen ws://IP:PORT`. Add `--remote-auth-token-env <ENV_VAR>` when the server requires a bearer token for WebSocket authentication. See [Codex CLI features](https://developers.openai.com/codex/cli/features#connect-the-tui-to-a-remote-app-server) for setup examples and authentication guidance.
 
 ### `codex app-server`
 
@@ -723,15 +901,17 @@
 
 <ConfigTable client:load options={appServerOptions} />
 
-`codex app-server --listen stdio://` keeps the default JSONL-over-stdio behavior. `--listen ws://IP:PORT` enables WebSocket transport (experimental). If you generate schemas for client bindings, add `--experimental` to include gated fields and methods.
+`codex app-server --listen stdio://` keeps the default JSONL-over-stdio behavior. `--listen ws://IP:PORT` enables WebSocket transport for app-server clients. The server accepts `ws://` listen URLs; use TLS termination or a secure proxy when clients connect with `wss://`. If you generate schemas for client bindings, add `--experimental` to include gated fields and methods.
 
 ### `codex app`
 
-Launch Codex Desktop from the terminal on macOS and optionally open a specific workspace path.
+Launch Codex Desktop from the terminal on macOS or Windows. On macOS, Codex can open a specific workspace path; on Windows, Codex prints the path to open.
 
 <ConfigTable client:load options={appOptions} />
 
-`codex app` installs/opens the desktop app on macOS, then opens the provided workspace path. This subcommand is macOS-only.
+`codex app` opens an installed Codex Desktop app, or starts the installer when
+the app is missing. On macOS, Codex opens the provided workspace path; on
+Windows, it prints the path to open after installation.
 
 ### `codex debug app-server send-message-v2`
 
@@ -741,6 +921,14 @@
 
 This debug flow initializes with `experimentalApi: true`, starts a thread, sends a turn, and streams server notifications. Use it to reproduce and inspect app-server protocol behavior locally.
 
+### `codex debug models`
+
+Print the raw model catalog Codex sees as JSON.
+
+<ConfigTable client:load options={debugModelsOptions} />
+
+Use `--bundled` when you want to inspect only the catalog bundled with the current binary, without refreshing from the remote models endpoint.
+
 ### `codex apply`
 
 Apply the most recent diff from a Codex cloud task to your local repository. You must authenticate and have access to the task.
@@ -817,6 +1005,17 @@
 
 OAuth actions (`login`, `logout`) only work with streamable HTTP servers (and only when the server supports OAuth).
 
+### `codex plugin marketplace`
+
+Manage plugin marketplace sources that Codex can browse and install from.
+
+<ConfigTable client:load options={marketplaceCommands} />
+
+`codex plugin marketplace add` accepts GitHub shorthand such as `owner/repo` or
+`owner/repo@ref`, HTTP or HTTPS Git URLs, SSH Git URLs, and local marketplace
+root directories. Use `--ref` to pin a Git ref, and repeat `--sparse PATH` to
+use a sparse checkout for Git-backed marketplace repositories.
+
 ### `codex mcp-server`
 
 Run Codex as an MCP server over stdio so that other tools can connect. This command inherits global configuration overrides and exits when the downstream client closes the connection.
@@ -845,9 +1044,17 @@
 
 <ConfigTable client:load options={sandboxLinuxOptions} />
 
+#### Windows
+
+<ConfigTable client:load options={sandboxWindowsOptions} />
+
+### `codex update`
+
+Check for and apply a Codex CLI update when the installed release supports self-update. Debug builds print a message telling you to install a release build instead.
+
 ## Flag combinations and safety tips
 
-- Set `--full-auto` for unattended local work, but avoid combining it with `--dangerously-bypass-approvals-and-sandbox` unless you are inside a dedicated sandbox VM.
+- Use `--sandbox workspace-write` for unattended local work that can stay inside the workspace, and avoid `--dangerously-bypass-approvals-and-sandbox` unless you are inside a dedicated sandbox VM.
 - When you need to grant Codex write access to more directories, prefer `--add-dir` rather than forcing `--sandbox danger-full-access`.
 - Pair `--json` with `--output-last-message` in CI to capture machine-readable progress and a final natural-language summary.
 

```
#### https://developers.openai.com/codex/cli/slash-commands.md

```diff
--- a/https://developers.openai.com/codex/cli/slash-commands.md
+++ b/https://developers.openai.com/codex/cli/slash-commands.md
@@ -8,43 +8,55 @@
 This guide shows you how to:
 
 - Find the right built-in slash command for a task
-- Steer an active session with commands like `/model`, `/personality`,
-  `/permissions`, `/experimental`, `/agent`, and `/status`
+- Steer an active session with commands like `/model`, `/fast`,
+  `/personality`, `/permissions`, `/agent`, and `/status`
 
 ## Built-in slash commands
 
 Codex ships with the following commands. Open the slash popup and start typing
 the command name to filter the list.
 
-| Command                                                                         | Purpose                                                         | When to use it                                                                                            |
-| ------------------------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
-| [`/permissions`](#update-permissions-with-permissions)                          | Set what Codex can do without asking first.                     | Relax or tighten approval requirements mid-session, such as switching between Auto and Read Only.         |
-| [`/sandbox-add-read-dir`](#grant-sandbox-read-access-with-sandbox-add-read-dir) | Grant sandbox read access to an extra directory (Windows only). | Unblock commands that need to read an absolute directory path outside the current readable roots.         |
-| [`/agent`](#switch-agent-threads-with-agent)                                    | Switch the active agent thread.                                 | Inspect or continue work in a spawned sub-agent thread.                                                   |
-| [`/apps`](#browse-apps-with-apps)                                               | Browse apps (connectors) and insert them into your prompt.      | Attach an app as `$app-slug` before asking Codex to use it.                                               |
-| [`/clear`](#clear-the-terminal-and-start-a-new-chat-with-clear)                 | Clear the terminal and start a fresh chat.                      | Reset the visible UI and conversation together when you want a clean slate.                               |
-| [`/compact`](#keep-transcripts-lean-with-compact)                               | Summarize the visible conversation to free tokens.              | Use after long runs so Codex retains key points without blowing the context window.                       |
-| [`/copy`](#copy-the-latest-response-with-copy)                                  | Copy the latest completed Codex output.                         | Grab the latest finished response or plan text without manually selecting it.                             |
-| [`/diff`](#review-changes-with-diff)                                            | Show the Git diff, including files Git isn't tracking yet.      | Review Codex's edits before you commit or run tests.                                                      |
-| [`/exit`](#exit-the-cli-with-quit-or-exit)                                      | Exit the CLI (same as `/quit`).                                 | Alternative spelling; both commands exit the session.                                                     |
-| [`/experimental`](#toggle-experimental-features-with-experimental)              | Toggle experimental features.                                   | Enable optional features such as sub-agents from the CLI.                                                 |
-| [`/feedback`](#send-feedback-with-feedback)                                     | Send logs to the Codex maintainers.                             | Report issues or share diagnostics with support.                                                          |
-| [`/init`](#generate-agentsmd-with-init)                                         | Generate an `AGENTS.md` scaffold in the current directory.      | Capture persistent instructions for the repository or subdirectory you're working in.                     |
-| [`/logout`](#sign-out-with-logout)                                              | Sign out of Codex.                                              | Clear local credentials when using a shared machine.                                                      |
-| [`/mcp`](#list-mcp-tools-with-mcp)                                              | List configured Model Context Protocol (MCP) tools.             | Check which external tools Codex can call during the session.                                             |
-| [`/mention`](#highlight-files-with-mention)                                     | Attach a file to the conversation.                              | Point Codex at specific files or folders you want it to inspect next.                                     |
-| [`/model`](#set-the-active-model-with-model)                                    | Choose the active model (and reasoning effort, when available). | Switch between general-purpose models (`gpt-4.1-mini`) and deeper reasoning models before running a task. |
-| [`/plan`](#switch-to-plan-mode-with-plan)                                       | Switch to plan mode and optionally send a prompt.               | Ask Codex to propose an execution plan before implementation work starts.                                 |
-| [`/personality`](#set-a-communication-style-with-personality)                   | Choose a communication style for responses.                     | Make Codex more concise, more explanatory, or more collaborative without changing your instructions.      |
-| [`/ps`](#check-background-terminals-with-ps)                                    | Show experimental background terminals and their recent output. | Check long-running commands without leaving the main transcript.                                          |
-| [`/fork`](#fork-the-current-conversation-with-fork)                             | Fork the current conversation into a new thread.                | Branch the active session to explore a new approach without losing the current transcript.                |
-| [`/resume`](#resume-a-saved-conversation-with-resume)                           | Resume a saved conversation from your session list.             | Continue work from a previous CLI session without starting over.                                          |
-| [`/new`](#start-a-new-conversation-with-new)                                    | Start a new conversation inside the same CLI session.           | Reset the chat context without leaving the CLI when you want a fresh prompt in the same repo.             |
-| [`/quit`](#exit-the-cli-with-quit-or-exit)                                      | Exit the CLI.                                                   | Leave the session immediately.                                                                            |
-| [`/review`](#ask-for-a-working-tree-review-with-review)                         | Ask Codex to review your working tree.                          | Run after Codex completes work or when you want a second set of eyes on local changes.                    |
-| [`/status`](#inspect-the-session-with-status)                                   | Display session configuration and token usage.                  | Confirm the active model, approval policy, writable roots, and remaining context capacity.                |
-| [`/debug-config`](#inspect-config-layers-with-debug-config)                     | Print config layer and requirements diagnostics.                | Debug precedence and policy requirements, including experimental network constraints.                     |
-| [`/statusline`](#configure-footer-items-with-statusline)                        | Configure TUI status-line fields interactively.                 | Pick and reorder footer items (model/context/limits/git/tokens/session) and persist in config.toml.       |
+When a task is already running, you can type a slash command and press `Tab` to
+queue it for the next turn. Codex parses queued slash commands when they run, so
+command menus and errors appear after the current turn finishes. Slash
+completion still works before you queue the command.
+
+| Command                                                                         | Purpose                                                         | When to use it                                                                                             |
+| ------------------------------------------------------------------------------- | --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
+| [`/permissions`](#update-permissions-with-permissions)                          | Set what Codex can do without asking first.                     | Relax or tighten approval requirements mid-session, such as switching between Auto and Read Only.          |
+| [`/sandbox-add-read-dir`](#grant-sandbox-read-access-with-sandbox-add-read-dir) | Grant sandbox read access to an extra directory (Windows only). | Unblock commands that need to read an absolute directory path outside the current readable roots.          |
+| [`/agent`](#switch-agent-threads-with-agent)                                    | Switch the active agent thread.                                 | Inspect or continue work in a spawned subagent thread.                                                     |
+| [`/apps`](#browse-apps-with-apps)                                               | Browse apps (connectors) and insert them into your prompt.      | Attach an app as `$app-slug` before asking Codex to use it.                                                |
+| [`/plugins`](#browse-plugins-with-plugins)                                      | Browse installed and discoverable plugins.                      | Inspect plugin tools, install suggested plugins, or manage plugin availability.                            |
+| [`/clear`](#clear-the-terminal-and-start-a-new-chat-with-clear)                 | Clear the terminal and start a fresh chat.                      | Reset the visible UI and conversation together when you want a fresh start.                                |
+| [`/compact`](#keep-transcripts-lean-with-compact)                               | Summarize the visible conversation to free tokens.              | Use after long runs so Codex retains key points without blowing the context window.                        |
+| [`/copy`](#copy-the-latest-response-with-copy)                                  | Copy the latest completed Codex output.                         | Grab the latest finished response or plan text without manually selecting it. You can also press `Ctrl+O`. |
+| [`/diff`](#review-changes-with-diff)                                            | Show the Git diff, including files Git isn't tracking yet.      | Review Codex's edits before you commit or run tests.                                                       |
+| [`/exit`](#exit-the-cli-with-quit-or-exit)                                      | Exit the CLI (same as `/quit`).                                 | Alternative spelling; both commands exit the session.                                                      |
+| [`/experimental`](#toggle-experimental-features-with-experimental)              | Toggle experimental features.                                   | Enable optional features such as subagents from the CLI.                                                   |
+| [`/feedback`](#send-feedback-with-feedback)                                     | Send logs to the Codex maintainers.                             | Report issues or share diagnostics with support.                                                           |
+| [`/init`](#generate-agentsmd-with-init)                                         | Generate an `AGENTS.md` scaffold in the current directory.      | Capture persistent instructions for the repository or subdirectory you're working in.                      |
+| [`/logout`](#sign-out-with-logout)                                              | Sign out of Codex.                                              | Clear local credentials when using a shared machine.                                                       |
+| [`/mcp`](#list-mcp-tools-with-mcp)                                              | List configured Model Context Protocol (MCP) tools.             | Check which external tools Codex can call during the session; add `verbose` for server details.            |
+| [`/mention`](#highlight-files-with-mention)                                     | Attach a file to the conversation.                              | Point Codex at specific files or folders you want it to inspect next.                                      |
+| [`/model`](#set-the-active-model-with-model)                                    | Choose the active model (and reasoning effort, when available). | Switch between general-purpose models (`gpt-4.1-mini`) and deeper reasoning models before running a task.  |
+| [`/fast`](#toggle-fast-mode-with-fast)                                          | Toggle Fast mode for supported models.                          | Turn Fast mode on or off, or check whether the current thread is using it.                                 |
+| [`/plan`](#switch-to-plan-mode-with-plan)                                       | Switch to plan mode and optionally send a prompt.               | Ask Codex to propose an execution plan before implementation work starts.                                  |
+| [`/goal`](#set-or-view-an-experimental-task-goal-with-goal)                     | Set or view an experimental goal for a long-running task.       | Give Codex a persistent target to track while a larger task runs. Requires `features.goals`.               |
+| [`/personality`](#set-a-communication-style-with-personality)                   | Choose a communication style for responses.                     | Make Codex more concise, more explanatory, or more collaborative without changing your instructions.       |
+| [`/ps`](#check-background-terminals-with-ps)                                    | Show experimental background terminals and their recent output. | Check long-running commands without leaving the main transcript.                                           |
+| [`/stop`](#stop-background-terminals-with-stop)                                 | Stop all background terminals.                                  | Cancel background terminal work started by the current session.                                            |
+| [`/fork`](#fork-the-current-conversation-with-fork)                             | Fork the current conversation into a new thread.                | Branch the active session to explore a new approach without losing the current transcript.                 |
+| [`/side`](#start-a-side-conversation-with-side)                                 | Start an ephemeral side conversation.                           | Ask a focused follow-up without disrupting the main thread's transcript.                                   |
+| [`/resume`](#resume-a-saved-conversation-with-resume)                           | Resume a saved conversation from your session list.             | Continue work from a previous CLI session without starting over.                                           |
+| [`/new`](#start-a-new-conversation-with-new)                                    | Start a new conversation inside the same CLI session.           | Reset the chat context without leaving the CLI when you want a fresh prompt in the same repo.              |
+| [`/quit`](#exit-the-cli-with-quit-or-exit)                                      | Exit the CLI.                                                   | Leave the session immediately.                                                                             |
+| [`/review`](#ask-for-a-working-tree-review-with-review)                         | Ask Codex to review your working tree.                          | Run after Codex completes work or when you want a second set of eyes on local changes.                     |
+| [`/status`](#inspect-the-session-with-status)                                   | Display session configuration and token usage.                  | Confirm the active model, approval policy, writable roots, and remaining context capacity.                 |
+| [`/debug-config`](#inspect-config-layers-with-debug-config)                     | Print config layer and requirements diagnostics.                | Debug precedence and policy requirements, including experimental network constraints.                      |
+| [`/statusline`](#configure-footer-items-with-statusline)                        | Configure TUI status-line fields interactively.                 | Pick and reorder footer items (model/context/limits/git/tokens/session) and persist in config.toml.        |
+| [`/title`](#configure-terminal-title-items-with-title)                          | Configure terminal window or tab title fields interactively.    | Pick and reorder title items such as project, status, thread, branch, model, and task progress.            |
+| [`/keymap`](#remap-tui-shortcuts-with-keymap)                                   | Remap TUI keyboard shortcuts.                                   | Inspect and persist custom shortcut bindings in `config.toml`.                                             |
 
 `/quit` and `/exit` both exit the CLI. Use them only after you have saved or
 committed any important work.
@@ -62,6 +74,13 @@
 3. Choose a model such as `gpt-4.1-mini` or `gpt-4.1` from the popup.
 
 Expected: Codex confirms the new model in the transcript. Run `/status` to verify the change.
+
+### Toggle Fast mode with `/fast`
+
+1. Type `/fast on`, `/fast off`, or `/fast status`.
+2. If you want the setting to persist, confirm the update when Codex offers to save it.
+
+Expected: Codex reports whether Fast mode is on or off for the current thread. In the TUI footer, you can also show a Fast mode status-line item with `/statusline`.
 
 ### Set a communication style with `/personality`
 
@@ -90,10 +109,20 @@
 
 While a task is already running, `/plan` is temporarily unavailable.
 
+### Set an experimental goal with `/goal`
+
+`/goal` is experimental and only available when `features.goals` is enabled. To enable it, open `/experimental` or add `goals = true` under `[features]` in `config.toml`.
+
+1. Type `/goal <objective>` to set the goal, for example `/goal Finish the migration and keep tests green`.
+2. Type `/goal` to view the current goal.
+3. Use `/goal pause`, `/goal resume`, or `/goal clear` to pause, resume, or remove it.
+
+Expected: Codex keeps the goal attached to the active thread while work continues.
+
 ### Toggle experimental features with `/experimental`
 
 1. Type `/experimental` and press Enter.
-2. Toggle the features you want (for example, **Multi-agents**), then restart Codex.
+2. Toggle the features you want (for example, Apps or Smart Approvals), then restart Codex if the prompt asks you to.
 
 Expected: Codex saves your feature choices to config and applies them on restart.
 
@@ -128,6 +157,9 @@
 the in-progress response. The command is unavailable before the first completed
 Codex output and immediately after a rollback.
 
+You can also press <kbd>Ctrl</kbd>+<kbd>O</kbd> from the main TUI to copy the
+latest completed response without opening the slash command menu.
+
 ### Grant sandbox read access with `/sandbox-add-read-dir`
 
 This command is available only when running the CLI natively on Windows.
@@ -170,6 +202,29 @@
 limits, git branch, token counters, session id, current directory/project root,
 and Codex version.
 
+### Configure terminal title items with `/title`
+
+1. Type `/title`.
+2. Use the picker to toggle and reorder items, then confirm.
+
+Expected: The terminal window or tab title updates immediately and persists to
+`tui.terminal_title` in `config.toml`.
+
+Available title items include app name, project, spinner, status, thread, git
+branch, model, and task progress.
+
+### Remap TUI shortcuts with `/keymap`
+
+Use `/keymap` to inspect, update, and persist keyboard shortcut bindings for the TUI.
+
+1. Type `/keymap`.
+2. Pick the shortcut context and action you want to change.
+3. Enter the new binding or remove the existing one.
+
+Expected: Codex updates the active keymap and writes the custom binding to `tui.keymap` in `config.toml`.
+
+Key bindings use names such as `ctrl-a`, `shift-enter`, and `page-down`. Context-specific bindings override `tui.keymap.global`; an empty binding list unbinds the action.
+
 ### Check background terminals with `/ps`
 
 1. Type `/ps`.
@@ -180,6 +235,14 @@
 
 Background terminals appear when `unified_exec` is in use; otherwise, the list may be empty.
 
+### Stop background terminals with `/stop`
+
+1. Type `/stop`.
+2. Confirm if Codex asks before stopping the listed terminals.
+
+Expected: Codex stops all background terminals for the current session. `/clean`
+is still available as an alias for `/stop`.
+
 ### Keep transcripts lean with `/compact`
 
 1. After a long exchange, type `/compact`.
@@ -210,7 +273,7 @@
 Expected: Codex starts a fresh conversation in the same CLI session, so you
 can switch tasks without leaving your terminal.
 
-Unlike `/clear`, `/new` does not clear the current terminal view first.
+Unlike `/clear`, `/new` doesn't clear the current terminal view first.
 
 ### Resume a saved conversation with `/resume`
 
@@ -231,6 +294,18 @@
 If you need to fork a saved session instead of the current one, run
 `codex fork` in your terminal to open the session picker.
 
+### Start a side conversation with `/side`
+
+Use `/side` to start an ephemeral fork from the current conversation without switching away from the main task.
+
+1. Type `/side` to open a side conversation.
+2. Optionally add inline text, for example `/side Check whether this plan has an obvious risk`.
+3. Return to the parent thread after the focused detour finishes.
+
+Expected: Codex opens a side conversation whose transcript is separate from the parent thread. While you are in side mode, the TUI continues to show parent-thread status so you can see whether the main task is still running.
+
+`/side` is unavailable inside another side conversation and during review mode.
+
 ### Generate `AGENTS.md` with `/init`
 
 1. Run `/init` in the directory where you want Codex to look for persistent instructions.
@@ -255,6 +330,8 @@
 
 Expected: You see the configured Model Context Protocol (MCP) tools Codex can call in this session.
 
+Use `/mcp verbose` to include detailed server diagnostics. If you pass anything other than `verbose`, Codex shows the command usage.
+
 ### Browse apps with `/apps`
 
 1. Type `/apps`.
@@ -263,6 +340,15 @@
 Expected: Codex inserts the app mention into the composer as `$app-slug`, so
 you can immediately ask Codex to use it.
 
+### Browse plugins with `/plugins`
+
+1. Type `/plugins`.
+2. Choose a marketplace tab, then pick a plugin to inspect its capabilities or available actions.
+
+Expected: Codex opens the plugin browser so you can review installed plugins,
+discoverable plugins that your configuration allows, and installed plugin state.
+Press <kbd>Space</kbd> on an installed plugin to toggle its enabled state.
+
 ### Switch agent threads with `/agent`
 
 1. Type `/agent` and press Enter.

```
#### https://developers.openai.com/codex/concepts/customization.md

```diff
--- a/https://developers.openai.com/codex/concepts/customization.md
+++ b/https://developers.openai.com/codex/concepts/customization.md
@@ -5,11 +5,14 @@
 In Codex, customization comes from a few layers that work together:
 
 - **Project guidance (`AGENTS.md`)** for persistent instructions
+- **[Memories](https://developers.openai.com/codex/memories)** for useful context learned from prior work
 - **Skills** for reusable workflows and domain expertise
 - **[MCP](https://developers.openai.com/codex/mcp)** for access to external tools and shared systems
-- **[Multi-agents](https://developers.openai.com/codex/concepts/multi-agents)** for delegating work to specialized sub-agents
+- **[Subagents](https://developers.openai.com/codex/concepts/subagents)** for delegating work to specialized subagents
 
-These are complementary, not competing. `AGENTS.md` shapes behavior, skills package repeatable processes, and [MCP](https://developers.openai.com/codex/mcp) connects Codex to systems outside the local workspace.
+These are complementary, not competing. `AGENTS.md` shapes behavior, memories
+carry local context forward, skills package repeatable processes, and
+[MCP](https://developers.openai.com/codex/mcp) connects Codex to systems outside the local workspace.
 
 ## AGENTS Guidance
 
@@ -19,7 +22,7 @@
 
 - Build and test commands
 - Review expectations
-- Repo-specific conventions
+- repo-specific conventions
 - Directory-specific instructions
 
 When the agent makes incorrect assumptions about your codebase, correct them in `AGENTS.md` and ask the agent to update `AGENTS.md` so the fix persists. Treat it as a feedback loop.
@@ -53,7 +56,7 @@
       name: "repo-root/",
       open: true,
       children: [
-        { name: "AGENTS.md", comment: "Repo-specific (for your team)" },
+        { name: "AGENTS.md", comment: "repo-specific (for your team)" },
       ],
     },
   ]}
@@ -66,6 +69,12 @@
 Skills give Codex reusable capabilities for repeatable workflows.
 Skills are often the best fit for reusable workflows because they support richer instructions, scripts, and references while staying reusable across tasks.
 Skills are loaded and visible to the agent (at least their metadata), so Codex can discover and choose them implicitly. This keeps rich workflows available without bloating context up front.
+
+Use skill folders to author and iterate on workflows locally. If a plugin
+already exists for the workflow, install it first to reuse a proven setup. When
+you want to distribute your own workflow across teams or bundle it with app
+integrations, package it as a [plugin](https://developers.openai.com/codex/plugins/build). Skills remain the
+authoring format; plugins are the installable distribution unit.
 
 A skill is typically a `SKILL.md` file plus optional scripts, references, and assets.
 
@@ -109,10 +118,10 @@
 
 Skills can be global (in your user directory, for you as a developer) or repo-specific (checked into `.agents/skills`, for your team). Put repo skills in `.agents/skills` when the workflow applies to that project; use your user directory for skills you want across all repos.
 
-| Layer  | Global                 | Repo                                    |
-| :----- | :--------------------- | :-------------------------------------- |
-| AGENTS | `~/.codex/AGENTS.md`   | `AGENTS.md` in repo root or nested dirs |
-| Skills | `$HOME/.agents/skills` | `.agents/skills` in repo                |
+| Layer  | Global                 | Repo                                           |
+| :----- | :--------------------- | :--------------------------------------------- |
+| AGENTS | `~/.codex/AGENTS.md`   | `AGENTS.md` in repo root or nested directories |
+| Skills | `$HOME/.agents/skills` | `.agents/skills` in repo                       |
 
 Codex uses progressive disclosure for skills:
 
@@ -127,11 +136,11 @@
 ## MCP
 
 MCP (Model Context Protocol) is the standard way to connect Codex to external tools and context providers.
-It's especially useful for remotely hosted systems such as Figma, Linear, Jira, GitHub, or internal knowledge services your team depends on.
+It's especially useful for remotely hosted systems such as Figma, Linear, GitHub, or internal knowledge services your team depends on.
 
 Use MCP when Codex needs capabilities that live outside the local repo, such as issue trackers, design tools, browsers, or shared documentation systems.
 
-A useful mental model:
+One way to think about it:
 
 - **Host**: Codex
 - **Client**: the MCP connection inside Codex
@@ -151,11 +160,11 @@
 
 [Model Context Protocol](https://developers.openai.com/codex/mcp)
 
-## Multi-agents
+## Subagents
 
-You can create different agents with different roles and prompt them to use tools differently. For example, one agent might run specific testing commands and configurations, while another has MCP servers that fetch production logs for debugging. Each sub-agent stays focused and uses the right tools for its job.
+You can create different agents with different roles and prompt them to use tools differently. For example, one agent might run specific testing commands and configurations, while another has MCP servers that fetch production logs for debugging. Each subagent stays focused and uses the right tools for its job.
 
-[Multi-agents concepts](https://developers.openai.com/codex/concepts/multi-agents)
+[Subagent concepts](https://developers.openai.com/codex/concepts/subagents)
 
 ## Skills + MCP together
 
@@ -167,6 +176,6 @@
 Build in this order:
 
 1. [Custom instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md) so Codex follows your repo conventions. Add pre-commit hooks and linters to enforce those rules.
-2. [Skills](https://developers.openai.com/codex/skills) so you never have the same conversation twice. Skills can include a `scripts/` directory with CLI scripts or pair with [MCP](https://developers.openai.com/codex/mcp) for external systems.
-3. [MCP](https://developers.openai.com/codex/mcp) when workflows need external systems (Linear, JIRA, docs servers, design tools).
-4. [Multi-agents](https://developers.openai.com/codex/multi-agent) when you're ready to delegate noisy or specialized tasks to sub-agents.+2. Install a [plugin](https://developers.openai.com/codex/plugins) when a reusable workflow already exists. Otherwise, create a [skill](https://developers.openai.com/codex/skills) and package it as a plugin when you want to share it.
+3. [MCP](https://developers.openai.com/codex/mcp) when workflows need external systems (Linear, GitHub, docs servers, design tools).
+4. [Subagents](https://developers.openai.com/codex/subagents) when you're ready to delegate noisy or specialized tasks to subagents.
```
#### https://developers.openai.com/codex/concepts/sandboxing.md

```diff
--- a/https://developers.openai.com/codex/concepts/sandboxing.md
+++ b/https://developers.openai.com/codex/concepts/sandboxing.md
@@ -1,6 +1,6 @@
-# Sandboxing
-
-Sandboxing is the boundary that lets Codex act autonomously without giving it
+# Sandbox
+
+The sandbox is the boundary that lets Codex act autonomously without giving it
 unrestricted access to your machine. When Codex runs local commands in the
 **Codex app**, **IDE extension**, or **CLI**, those commands run inside a
 constrained environment instead of running with full access by default.
@@ -21,20 +21,102 @@
 those commands inherit the same sandbox boundaries.
 
 Codex uses platform-native enforcement on each OS. The implementation differs
-between macOS, Linux, WSL, and native Windows, but the idea is the same across
+between macOS, Linux, WSL2, and native Windows, but the idea is the same across
 surfaces: give the agent a bounded place to work so routine tasks can run
 autonomously inside clear limits.
 
 ## Why it matters
 
-Sandboxing reduces approval fatigue. Instead of asking you to confirm every
+The sandbox reduces approval fatigue. Instead of asking you to confirm every
 low-risk command, Codex can read files, make edits, and run routine project
 commands within the boundary you already approved.
 
-It also gives you a clearer trust model for agentic work. You are not just
+It also gives you a clearer trust model for agentic work. You aren't just
 trusting the agent's intentions; you are trusting that the agent is operating
 inside enforced limits. That makes it easier to let Codex work independently
 while still knowing when it will stop and ask for help.
+
+## Getting started
+
+Codex applies sandboxing automatically when you use the default permissions
+mode.
+
+### Prerequisites
+
+On **macOS**, sandboxing works out of the box using the built-in Seatbelt
+framework.
+
+On **Windows**, Codex uses the native [Windows
+sandbox](https://developers.openai.com/codex/windows#windows-sandbox) when you run in PowerShell and the
+Linux sandbox implementation when you run in WSL2.
+
+On **Linux and WSL2**, install `bubblewrap` with your package manager first:
+
+<Tabs
+  id="codex-sandboxing-prerequisites"
+  param="sandbox-os"
+  tabs={[
+    { id: "ubuntu-debian", label: "Ubuntu/Debian" },
+    { id: "fedora", label: "Fedora" },
+  ]}
+>
+  <div slot="ubuntu-debian">
+
+```bash
+sudo apt install bubblewrap
+```
+
+  </div>
+
+  <div slot="fedora">
+
+```bash
+sudo dnf install bubblewrap
+```
+
+  </div>
+</Tabs>
+
+Codex uses the first `bwrap` executable it finds on `PATH`. If no `bwrap`
+executable is available, Codex falls back to a bundled helper, but that helper
+requires support for unprivileged user namespace creation. Installing the
+distribution package that provides `bwrap` keeps this setup reliable.
+
+Codex surfaces a startup warning when `bwrap` is missing or when the helper
+can't create the needed user namespace. On distributions that restrict this
+AppArmor setting, prefer loading the `bwrap` AppArmor profile so `bwrap` can
+keep working without disabling the restriction globally.
+
+**Ubuntu AppArmor note:** On Ubuntu 25.04, installing `bubblewrap` from
+  Ubuntu's package repository should work without extra AppArmor setup. The
+  `bwrap-userns-restrict` profile ships in the `apparmor` package at
+  `/etc/apparmor.d/bwrap-userns-restrict`.
+
+On Ubuntu 24.04, Codex may still warn that it can't create the needed user
+namespace after `bubblewrap` is installed. Copy and load the extra profile:
+
+```bash
+sudo apt update
+sudo apt install apparmor-profiles apparmor-utils
+sudo install -m 0644 \
+  /usr/share/apparmor/extra-profiles/bwrap-userns-restrict \
+  /etc/apparmor.d/bwrap-userns-restrict
+sudo apparmor_parser -r /etc/apparmor.d/bwrap-userns-restrict
+```
+
+`apparmor_parser -r` loads the profile into the kernel without a reboot. You
+can also reload all AppArmor profiles:
+
+```bash
+sudo systemctl reload apparmor.service
+```
+
+If that profile is unavailable or does not resolve the issue, you can disable
+the AppArmor unprivileged user namespace restriction with:
+
+```bash
+sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0
+```
 
 ## How you control it
 
@@ -67,7 +149,7 @@
 
 At a high level, the common sandbox modes are:
 
-- `read-only`: Codex can inspect files, but it cannot edit files or run
+- `read-only`: Codex can inspect files, but it can't edit files or run
   commands without approval.
 - `workspace-write`: Codex can read files, edit within the workspace, and run
   routine local commands inside that boundary. This is the default low-friction
@@ -78,21 +160,31 @@
 
 The common approval policies are:
 
-- `untrusted`: Codex asks before running commands that are not in its trusted
+- `untrusted`: Codex asks before running commands that aren't in its trusted
   set.
 - `on-request`: Codex works inside the sandbox by default and asks when it
   needs to go beyond that boundary.
-- `never`: Codex does not stop for approval prompts.
+- `never`: Codex doesn't stop for approval prompts.
 
 Full access means using `sandbox_mode = "danger-full-access"` together with
-`approval_policy = "never"`. By contrast, `--full-auto` is the lower-risk local
-automation preset: `sandbox_mode = "workspace-write"` and
-`approval_policy = "on-request"`.
+`approval_policy = "never"`. By contrast, the lower-risk local automation
+preset is `sandbox_mode = "workspace-write"` together with
+`approval_policy = "on-request"`, or the matching CLI flags
+`--sandbox workspace-write --ask-for-approval on-request`.
 
 If you need Codex to work across more than one directory, writable roots let
 you extend the places it can modify without removing the sandbox entirely. If
 you need a broader or narrower trust boundary, adjust the default sandbox mode
-and approval policy instead of relying on ad hoc exceptions.
+and approval policy instead of relying on one-off exceptions.
+
+For reusable permission sets, set `default_permissions` to a named profile and
+define `[permissions.<name>.filesystem]` or `[permissions.<name>.network]`.
+Managed network profiles use map tables such as
+`[permissions.<name>.network.domains]` and
+`[permissions.<name>.network.unix_sockets]` for domain and socket rules.
+Filesystem profiles can also deny reads for exact paths or glob patterns by
+setting matching entries to `"none"`; use this to keep files such as local
+secrets unreadable without turning off workspace writes.
 
 When a workflow needs a specific exception, use [rules](https://developers.openai.com/codex/rules). Rules
 let you allow, prompt, or forbid command prefixes outside the sandbox, which is
@@ -101,6 +193,12 @@
 [Codex app features](https://developers.openai.com/codex/app/features#approvals-and-sandboxing), and for the
 IDE-specific settings entry points, see [Codex IDE extension settings](https://developers.openai.com/codex/ide/settings).
 
+Automatic review, when available, doesn't change the sandbox boundary. It
+reviews approval requests, such as sandbox escalations or network access, while
+actions already allowed inside the sandbox run without extra review. See
+[Automatic approval reviews](https://developers.openai.com/codex/agent-approvals-security#automatic-approval-reviews)
+for the policy behavior.
+
 Platform details live in the platform-specific docs. For native Windows setup,
 behavior, and troubleshooting, see [Windows](https://developers.openai.com/codex/windows). For admin
 requirements and organization-level constraints on sandboxing and approvals, see

```
#### https://developers.openai.com/codex/config-advanced.md

```diff
--- a/https://developers.openai.com/codex/config-advanced.md
+++ b/https://developers.openai.com/codex/config-advanced.md
@@ -2,7 +2,7 @@
 
 Use these options when you need more control over providers, policies, and integrations. For a quick start, see [Config basics](https://developers.openai.com/codex/config-basic).
 
-For background on project guidance, reusable capabilities, custom slash commands, multi-agent workflows, and integrations, see [Customization](https://developers.openai.com/codex/concepts/customization). For configuration keys, see [Configuration Reference](https://developers.openai.com/codex/config-reference).
+For background on project guidance, reusable capabilities, custom slash commands, subagent workflows, and integrations, see [Customization](https://developers.openai.com/codex/concepts/customization). For configuration keys, see [Configuration Reference](https://developers.openai.com/codex/config-reference).
 
 ## Profiles
 
@@ -15,7 +15,7 @@
 Define profiles under `[profiles.<name>]` in `config.toml`, then run `codex --profile <name>`:
 
 ```toml
-model = "gpt-5-codex"
+model = "gpt-5.4"
 approval_policy = "on-request"
 model_catalog_json = "/Users/me/.codex/model-catalogs/default.json"
 
@@ -74,24 +74,64 @@
 
 For shared defaults, rules, and skills checked into repos or system paths, see [Team Config](https://developers.openai.com/codex/enterprise/admin-setup#team-config).
 
-If you just need to point the built-in OpenAI provider at an LLM proxy, router, or data-residency enabled project, set environment variable `OPENAI_BASE_URL` instead of defining a new provider. This overrides the default OpenAI endpoint without a `config.toml` change.
-
-```shell
-export OPENAI_BASE_URL="https://api.openai.com/v1"
-codex
+If you just need to point the built-in OpenAI provider at an LLM proxy, router, or data-residency enabled project, set `openai_base_url` in `config.toml` instead of defining a new provider. This changes the base URL for the built-in `openai` provider without requiring a separate `model_providers.<id>` entry.
+
+```toml
+openai_base_url = "https://us.api.openai.com/v1"
 ```
 
 ## Project config files (`.codex/config.toml`)
 
 In addition to your user config, Codex reads project-scoped overrides from `.codex/config.toml` files inside your repo. Codex walks from the project root to your current working directory and loads every `.codex/config.toml` it finds. If multiple files define the same key, the closest file to your working directory wins.
 
-For security, Codex loads project-scoped config files only when the project is trusted. If the project is untrusted, Codex ignores `.codex/config.toml` files in the project.
-
-Relative paths inside a project config (for example, `experimental_instructions_file`) are resolved relative to the `.codex/` folder that contains the `config.toml`.
+For security, Codex loads project-scoped config files only when the project is trusted. If the project is untrusted, Codex ignores project `.codex/` layers, including `.codex/config.toml`, project-local hooks, and project-local rules. User and system layers remain separate and still load.
+
+Relative paths inside a project config (for example, `model_instructions_file`) are resolved relative to the `.codex/` folder that contains the `config.toml`.
+
+## Hooks (experimental)
+
+Codex can also load lifecycle hooks from either `hooks.json` files or inline
+`[hooks]` tables in `config.toml` files that sit next to active config layers.
+
+In practice, the two most useful locations are:
+
+- `~/.codex/hooks.json`
+- `~/.codex/config.toml`
+- `<repo>/.codex/hooks.json`
+- `<repo>/.codex/config.toml`
+
+Project-local hooks load only when the project `.codex/` layer is trusted.
+User-level hooks remain independent of project trust.
+
+Turn hooks on with:
+
+```toml
+[features]
+codex_hooks = true
+```
+
+Inline TOML hooks use the same event structure as `hooks.json`:
+
+```toml
+[[hooks.PreToolUse]]
+matcher = "^Bash$"
+
+[[hooks.PreToolUse.hooks]]
+type = "command"
+command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py"'
+timeout = 30
+statusMessage = "Checking Bash command"
+```
+
+If a single layer contains both `hooks.json` and inline `[hooks]`, Codex loads
+both and warns. Prefer one representation per layer.
+
+For the current event list, input fields, output behavior, and limitations, see
+[Hooks](https://developers.openai.com/codex/hooks).
 
 ## Agent roles (`[agents]` in `config.toml`)
 
-For multi-agent role configuration (`[agents]` in `config.toml`), see [Multi-agents](https://developers.openai.com/codex/multi-agent).
+For subagent role configuration (`[agents]` in `config.toml`), see [Subagents](https://developers.openai.com/codex/subagents).
 
 ## Project root detection
 
@@ -108,12 +148,12 @@
 
 ## Custom model providers
 
-A model provider defines how Codex connects to a model (base URL, wire API, and optional HTTP headers).
+A model provider defines how Codex connects to a model (base URL, wire API, authentication, and optional HTTP headers). Custom providers can't reuse the reserved built-in provider IDs: `openai`, `ollama`, and `lmstudio`.
 
 Define additional providers and point `model_provider` at them:
 
 ```toml
-model = "gpt-5.1"
+model = "gpt-5.4"
 model_provider = "proxy"
 
 [model_providers.proxy]
@@ -121,7 +161,7 @@
 base_url = "http://proxy.example.com"
 env_key = "OPENAI_API_KEY"
 
-[model_providers.ollama]
+[model_providers.local_ollama]
 name = "Ollama"
 base_url = "http://localhost:11434/v1"
 
@@ -138,6 +178,41 @@
 http_headers = { "X-Example-Header" = "example-value" }
 env_http_headers = { "X-Example-Features" = "EXAMPLE_FEATURES" }
 ```
+
+Use command-backed authentication when a provider needs Codex to fetch bearer tokens from an external credential helper:
+
+```toml
+[model_providers.proxy]
+name = "OpenAI using LLM proxy"
+base_url = "https://proxy.example.com/v1"
+wire_api = "responses"
+
+[model_providers.proxy.auth]
+command = "/usr/local/bin/fetch-codex-token"
+args = ["--audience", "codex"]
+timeout_ms = 5000
+refresh_interval_ms = 300000
+```
+
+The auth command receives no `stdin` and must print the token to stdout. Codex trims surrounding whitespace, treats an empty token as an error, and refreshes proactively at `refresh_interval_ms`; set `refresh_interval_ms = 0` to refresh only after an authentication retry. Don't combine `[model_providers.<id>.auth]` with `env_key`, `experimental_bearer_token`, or `requires_openai_auth`.
+
+### Amazon Bedrock provider
+
+Codex includes a built-in `amazon-bedrock` model provider. Set it directly as
+`model_provider`; unlike custom providers, this built-in provider supports only
+the nested AWS profile and region overrides.
+
+```toml
+model_provider = "amazon-bedrock"
+model = "<bedrock-model-id>"
+
+[model_providers.amazon-bedrock.aws]
+profile = "default"
+region = "eu-central-1"
+```
+
+If you omit `profile`, Codex uses the standard AWS credential chain. Set
+`region` to the supported Bedrock region that should handle requests.
 
 ## OSS mode (local providers)
 
@@ -157,12 +232,12 @@
 env_key = "AZURE_OPENAI_API_KEY"
 query_params = { api-version = "2025-04-01-preview" }
 wire_api = "responses"
-
-[model_providers.openai]
 request_max_retries = 4
 stream_max_retries = 10
 stream_idle_timeout_ms = 300000
 ```
+
+To change the base URL for the built-in OpenAI provider, use `openai_base_url`; don't create `[model_providers.openai]`, because you can't override built-in provider IDs.
 
 ## ChatGPT customers using data residency
 
@@ -190,21 +265,73 @@
 
 Pick approval strictness (affects when Codex pauses) and sandbox level (affects file/network access).
 
-For operational details that are easy to miss while editing `config.toml`, see [Common sandbox and approval combinations](https://developers.openai.com/codex/agent-approvals-security#common-sandbox-and-approval-combinations), [Protected paths in writable roots](https://developers.openai.com/codex/agent-approvals-security#protected-paths-in-writable-roots), and [Network access](https://developers.openai.com/codex/agent-approvals-security#network-access).
-
-You can also use a granular reject policy (`approval_policy = { reject = { ... } }`) to auto-reject only selected prompt categories, such as sandbox approvals, `execpolicy` rule prompts, or MCP input requests (`mcp_elicitations`), while keeping other prompts interactive.
-
-```toml
-approval_policy = "untrusted"   # Other options: on-request, never, or { reject = { ... } }
+For operational details to keep in mind while editing `config.toml`, see [Common sandbox and approval combinations](https://developers.openai.com/codex/agent-approvals-security#common-sandbox-and-approval-combinations), [Protected paths in writable roots](https://developers.openai.com/codex/agent-approvals-security#protected-paths-in-writable-roots), and [Network access](https://developers.openai.com/codex/agent-approvals-security#network-access).
+
+You can also use a granular approval policy (`approval_policy = { granular = { ... } }`) to allow or auto-reject individual prompt categories. This is useful when you want normal interactive approvals for some cases but want others, such as `request_permissions` or skill-script prompts, to fail closed automatically.
+
+Set `approvals_reviewer = "auto_review"` to route eligible interactive approval
+requests through automatic review. This changes the reviewer, not the sandbox
+boundary.
+
+Use `[auto_review].policy` for local reviewer policy instructions. Managed
+`guardian_policy_config` takes precedence.
+
+```toml
+approval_policy = "untrusted"   # Other options: on-request, never, or { granular = { ... } }
+approvals_reviewer = "user"     # Or "auto_review" for automatic review
 sandbox_mode = "workspace-write"
 allow_login_shell = false       # Optional hardening: disallow login shells for shell tools
+
+# Example granular approval policy:
+# approval_policy = { granular = {
+#   sandbox_approval = true,
+#   rules = true,
+#   mcp_elicitations = true,
+#   request_permissions = false,
+#   skill_approval = false
+# } }
 
 [sandbox_workspace_write]
 exclude_tmpdir_env_var = false  # Allow $TMPDIR
 exclude_slash_tmp = false       # Allow /tmp
 writable_roots = ["/Users/YOU/.pyenv/shims"]
 network_access = false          # Opt in to outbound network
-```
+
+[auto_review]
+policy = """
+Use your organization's automatic review policy.
+"""
+```
+
+### Named permission profiles
+
+Set `default_permissions` to reuse a sandbox profile by name. Codex includes
+the built-in profiles `:read-only`, `:workspace`, and `:danger-no-sandbox`:
+
+```toml
+default_permissions = ":workspace"
+```
+
+For custom profiles, point `default_permissions` at a name you define under
+`[permissions.<name>]`:
+
+```toml
+default_permissions = "workspace"
+
+[permissions.workspace.filesystem]
+":project_roots" = { "." = "write", "**/*.env" = "none" }
+glob_scan_max_depth = 3
+
+[permissions.workspace.network]
+enabled = true
+mode = "limited"
+
+[permissions.workspace.network.domains]
+"api.openai.com" = "allow"
+```
+
+Use built-in names with a leading colon. Custom names don't use a leading
+colon and must have matching `permissions` tables.
 
 Need the complete key list (including profile-scoped overrides and requirements constraints)? See [Configuration Reference](https://developers.openai.com/codex/config-reference) and [Managed configuration](https://developers.openai.com/codex/enterprise/managed-configuration).
 
@@ -326,35 +453,140 @@
 
 #### Metrics catalog
 
-Each metric includes the required fields plus the default context fields above. Every metric is prefixed by `codex.`.
+Each metric includes the required fields plus the default context fields above. Metric names below omit the `codex.` prefix.
+Most metric names are centralized in `codex-rs/otel/src/metrics/names.rs`; feature-specific metrics emitted outside that file are included here too.
 If a metric includes the `tool` field, it reflects the internal tool used (for example, `apply_patch` or `shell`) and doesn't contain the actual shell command or patch `codex` is trying to apply.
 
-| Metric                                   | Type      | Fields             | Description                                                                                                                   |
-| ---------------------------------------- | --------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
-| `feature.state`                          | counter   | `feature`, `value` | Feature values that differ from defaults (emit one row per non-default).                                                      |
-| `thread.started`                         | counter   | `is_git`           | New thread created.                                                                                                           |
-| `thread.fork`                            | counter   |                    | New thread created by forking an existing thread.                                                                             |
-| `thread.rename`                          | counter   |                    | Thread renamed.                                                                                                               |
-| `task.compact`                           | counter   | `type`             | Number of compactions per type (`remote` or `local`), including manual and auto.                                              |
-| `task.user_shell`                        | counter   |                    | Number of user shell actions (`!` in the TUI for example).                                                                    |
-| `task.review`                            | counter   |                    | Number of reviews triggered.                                                                                                  |
-| `task.undo`                              | counter   |                    | Number of undo actions triggered.                                                                                             |
-| `approval.requested`                     | counter   | `tool`, `approved` | Tool approval request result (`approved`, `approved_with_amendment`, `approved_for_session`, `denied`, `abort`).              |
-| `conversation.turn.count`                | counter   |                    | User/assistant turns per thread, recorded at the end of the thread.                                                           |
-| `turn.e2e_duration_ms`                   | histogram |                    | End-to-end time for a full turn.                                                                                              |
-| `mcp.call`                               | counter   | `status`           | MCP tool invocation result (`ok` or error string).                                                                            |
-| `model_warning`                          | counter   |                    | Warning sent to the model.                                                                                                    |
-| `tool.call`                              | counter   | `tool`, `success`  | Tool invocation result (`success`: `true` or `false`).                                                                        |
-| `tool.call.duration_ms`                  | histogram | `tool`, `success`  | Tool execution time.                                                                                                          |
-| `remote_models.fetch_update.duration_ms` | histogram |                    | Time to fetch remote model definitions.                                                                                       |
-| `remote_models.load_cache.duration_ms`   | histogram |                    | Time to load the remote model cache.                                                                                          |
-| `shell_snapshot`                         | counter   | `success`          | Whether taking a shell snapshot succeeded.                                                                                    |
-| `shell_snapshot.duration_ms`             | histogram | `success`          | Time to take a shell snapshot.                                                                                                |
-| `db.init`                                | counter   | `status`           | State DB initialization outcomes (`opened`, `created`, `open_error`, `init_error`).                                           |
-| `db.backfill`                            | counter   | `status`           | Initial state DB backfill results (`upserted`, `failed`).                                                                     |
-| `db.backfill.duration_ms`                | histogram | `status`           | Duration of the initial state DB backfill, tagged with `success`, `failed`, or `partial_failure`.                             |
-| `db.error`                               | counter   | `stage`            | Errors during state DB operations (for example, `extract_metadata_from_rollout`, `backfill_sessions`, `apply_rollout_items`). |
-| `db.compare_error`                       | counter   | `stage`, `reason`  | State DB discrepancies detected during reconciliation.                                                                        |
+#### Runtime and model transport
+
+| Metric                                          | Type      | Fields               | Description                                                  |
+| ----------------------------------------------- | --------- | -------------------- | ------------------------------------------------------------ |
+| `api_request`                                   | counter   | `status`, `success`  | API request count by HTTP status and success/failure.        |
+| `api_request.duration_ms`                       | histogram | `status`, `success`  | API request duration in milliseconds.                        |
+| `sse_event`                                     | counter   | `kind`, `success`    | SSE event count by event kind and success/failure.           |
+| `sse_event.duration_ms`                         | histogram | `kind`, `success`    | SSE event processing duration in milliseconds.               |
+| `websocket.request`                             | counter   | `success`            | WebSocket request count by success/failure.                  |
+| `websocket.request.duration_ms`                 | histogram | `success`            | WebSocket request duration in milliseconds.                  |
+| `websocket.event`                               | counter   | `kind`, `success`    | WebSocket message/event count by type and success/failure.   |
+| `websocket.event.duration_ms`                   | histogram | `kind`, `success`    | WebSocket message/event processing duration in milliseconds. |
+| `responses_api_overhead.duration_ms`            | histogram |                      | Responses API overhead timing from websocket responses.      |
+| `responses_api_inference_time.duration_ms`      | histogram |                      | Responses API inference timing from websocket responses.     |
+| `responses_api_engine_iapi_ttft.duration_ms`    | histogram |                      | Responses API engine IAPI time-to-first-token timing.        |
+| `responses_api_engine_service_ttft.duration_ms` | histogram |                      | Responses API engine service time-to-first-token timing.     |
+| `responses_api_engine_iapi_tbt.duration_ms`     | histogram |                      | Responses API engine IAPI time-between-token timing.         |
+| `responses_api_engine_service_tbt.duration_ms`  | histogram |                      | Responses API engine service time-between-token timing.      |
+| `transport.fallback_to_http`                    | counter   | `from_wire_api`      | WebSocket-to-HTTP fallback count.                            |
+| `remote_models.fetch_update.duration_ms`        | histogram |                      | Time to fetch remote model definitions.                      |
+| `remote_models.load_cache.duration_ms`          | histogram |                      | Time to load the remote model cache.                         |
+| `startup_prewarm.duration_ms`                   | histogram | `status`             | Startup prewarm duration by outcome.                         |
+| `startup_prewarm.age_at_first_turn_ms`          | histogram | `status`             | Startup prewarm age when the first real turn resolves it.    |
+| `cloud_requirements.fetch.duration_ms`          | histogram |                      | Workspace-managed cloud requirements fetch duration.         |
+| `cloud_requirements.fetch_attempt`              | counter   | See note             | Workspace-managed cloud requirements fetch attempts.         |
+| `cloud_requirements.fetch_final`                | counter   | See note             | Final workspace-managed cloud requirements fetch outcome.    |
+| `cloud_requirements.load`                       | counter   | `trigger`, `outcome` | Workspace-managed cloud requirements load outcome.           |
+
+The `cloud_requirements.fetch_attempt` metric includes `trigger`, `attempt`, `outcome`, and `status_code` fields. The `cloud_requirements.fetch_final` metric includes `trigger`, `outcome`, `reason`, `attempt_count`, and `status_code` fields.
+
+#### Turn and tool activity
+
+| Metric                                 | Type      | Fields                                                                    | Description                                                                                                      |
+| -------------------------------------- | --------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
+| `turn.e2e_duration_ms`                 | histogram |                                                                           | End-to-end time for a full turn.                                                                                 |
+| `turn.ttft.duration_ms`                | histogram |                                                                           | Time to first token for a turn.                                                                                  |
+| `turn.ttfm.duration_ms`                | histogram |                                                                           | Time to first model output item for a turn.                                                                      |
+| `turn.network_proxy`                   | counter   | `active`, `tmp_mem_enabled`                                               | Whether the managed network proxy was active for the turn.                                                       |
+| `turn.memory`                          | counter   | `read_allowed`, `feature_enabled`, `config_use_memories`, `has_citations` | Per-turn memory read availability and memory citation usage.                                                     |
+| `turn.tool.call`                       | histogram | `tmp_mem_enabled`                                                         | Number of tool calls in the turn.                                                                                |
+| `turn.token_usage`                     | histogram | `token_type`, `tmp_mem_enabled`                                           | Per-turn token usage by token type (`total`, `input`, `cached_input`, `output`, or `reasoning_output`).          |
+| `tool.call`                            | counter   | `tool`, `success`                                                         | Tool invocation count by tool name and success/failure.                                                          |
+| `tool.call.duration_ms`                | histogram | `tool`, `success`                                                         | Tool execution duration in milliseconds by tool name and outcome.                                                |
+| `tool.unified_exec`                    | counter   | `tty`                                                                     | Unified exec tool calls by TTY mode.                                                                             |
+| `approval.requested`                   | counter   | `tool`, `approved`                                                        | Tool approval request result (`approved`, `approved_with_amendment`, `approved_for_session`, `denied`, `abort`). |
+| `mcp.call`                             | counter   | See note                                                                  | MCP tool invocation result.                                                                                      |
+| `mcp.call.duration_ms`                 | histogram | See note                                                                  | MCP tool invocation duration.                                                                                    |
+| `mcp.tools.list.duration_ms`           | histogram | `cache`                                                                   | MCP tool-list duration, including cache hit/miss state.                                                          |
+| `mcp.tools.fetch_uncached.duration_ms` | histogram |                                                                           | Duration of uncached MCP tool fetches.                                                                           |
+| `mcp.tools.cache_write.duration_ms`    | histogram |                                                                           | Duration of Codex Apps MCP tool-cache writes.                                                                    |
+| `hooks.run`                            | counter   | `hook_name`, `source`, `status`                                           | Hook run count by hook name, source, and status.                                                                 |
+| `hooks.run.duration_ms`                | histogram | `hook_name`, `source`, `status`                                           | Hook run duration in milliseconds.                                                                               |
+
+The `mcp.call` and `mcp.call.duration_ms` metrics include `status`; normal tool-call emissions also include `tool`, plus `connector_id` and `connector_name` when available. Blocked Codex Apps MCP calls may emit `mcp.call` with only `status`.
+
+#### Threads, tasks, and features
+
+| Metric                            | Type      | Fields                | Description                                                                      |
+| --------------------------------- | --------- | --------------------- | -------------------------------------------------------------------------------- |
+| `feature.state`                   | counter   | `feature`, `value`    | Feature values that differ from defaults (emit one row per non-default).         |
+| `status_line`                     | counter   |                       | Session started with a configured status line.                                   |
+| `model_warning`                   | counter   |                       | Warning sent to the model.                                                       |
+| `thread.started`                  | counter   | `is_git`              | New thread created, tagged by whether the working directory is in a Git repo.    |
+| `conversation.turn.count`         | counter   |                       | User/assistant turns per thread, recorded at the end of the thread.              |
+| `thread.fork`                     | counter   | `source`              | New thread created by forking an existing thread.                                |
+| `thread.rename`                   | counter   |                       | Thread renamed.                                                                  |
+| `thread.side`                     | counter   | `source`              | Side conversation created.                                                       |
+| `thread.skills.enabled_total`     | histogram |                       | Number of skills enabled for a new thread.                                       |
+| `thread.skills.kept_total`        | histogram |                       | Number of enabled skills kept after prompt rendering.                            |
+| `thread.skills.truncated`         | histogram |                       | Whether skill rendering truncated the enabled skills list (`1` or `0`).          |
+| `task.compact`                    | counter   | `type`                | Number of compactions per type (`remote` or `local`), including manual and auto. |
+| `task.review`                     | counter   |                       | Number of reviews triggered.                                                     |
+| `task.undo`                       | counter   |                       | Number of undo actions triggered.                                                |
+| `task.user_shell`                 | counter   |                       | Number of user shell actions (`!` in the TUI for example).                       |
+| `shell_snapshot`                  | counter   | See note              | Whether taking a shell snapshot succeeded.                                       |
+| `shell_snapshot.duration_ms`      | histogram | `success`             | Time to take a shell snapshot.                                                   |
+| `skill.injected`                  | counter   | `status`, `skill`     | Skill injection outcomes by skill.                                               |
+| `plugins.startup_sync`            | counter   | `transport`, `status` | Curated plugin startup sync attempts.                                            |
+| `plugins.startup_sync.final`      | counter   | `transport`, `status` | Final curated plugin startup sync outcome.                                       |
+| `multi_agent.spawn`               | counter   | `role`                | Agent spawns by role.                                                            |
+| `multi_agent.resume`              | counter   |                       | Agent resumes.                                                                   |
+| `multi_agent.nickname_pool_reset` | counter   |                       | Agent nickname pool resets.                                                      |
+
+The `shell_snapshot` metric includes `success` and, on failures, `failure_reason`.
+
+#### Memory and local state
+
+| Metric                         | Type      | Fields                    | Description                                               |
+| ------------------------------ | --------- | ------------------------- | --------------------------------------------------------- |
+| `memory.phase1`                | counter   | `status`                  | Memory phase 1 job counts by status.                      |
+| `memory.phase1.e2e_ms`         | histogram |                           | End-to-end duration for memory phase 1.                   |
+| `memory.phase1.output`         | counter   |                           | Memory phase 1 outputs written.                           |
+| `memory.phase1.token_usage`    | histogram | `token_type`              | Memory phase 1 token usage by token type.                 |
+| `memory.phase2`                | counter   | `status`                  | Memory phase 2 job counts by status.                      |
+| `memory.phase2.e2e_ms`         | histogram |                           | End-to-end duration for memory phase 2.                   |
+| `memory.phase2.input`          | counter   |                           | Memory phase 2 input count.                               |
+| `memory.phase2.token_usage`    | histogram | `token_type`              | Memory phase 2 token usage by token type.                 |
+| `memories.usage`               | counter   | `kind`, `tool`, `success` | Memory usage by kind, tool, and success/failure.          |
+| `external_agent_config.detect` | counter   | See note                  | External agent config detections by migration item type.  |
+| `external_agent_config.import` | counter   | See note                  | External agent config imports by migration item type.     |
+| `db.backfill`                  | counter   | `status`                  | Initial state DB backfill results (`upserted`, `failed`). |
+| `db.backfill.duration_ms`      | histogram | `status`                  | Duration of the initial state DB backfill.                |
+| `db.error`                     | counter   | `stage`                   | Errors during state DB operations.                        |
+
+The `external_agent_config.detect` and `external_agent_config.import` metrics include `migration_type`; skills migrations also include `skills_count`.
+
+#### Windows sandbox
+
+| Metric                                           | Type      | Fields                                    | Description                                           |
+| ------------------------------------------------ | --------- | ----------------------------------------- | ----------------------------------------------------- |
+| `windows_sandbox.setup_success`                  | counter   | `originator`, `mode`                      | Windows sandbox setup successes.                      |
+| `windows_sandbox.setup_failure`                  | counter   | `originator`, `mode`                      | Windows sandbox setup failures.                       |
+| `windows_sandbox.setup_duration_ms`              | histogram | `result`, `originator`, `mode`            | Windows sandbox setup duration.                       |
+| `windows_sandbox.elevated_setup_success`         | counter   |                                           | Elevated Windows sandbox setup successes.             |
+| `windows_sandbox.elevated_setup_failure`         | counter   | See note                                  | Elevated Windows sandbox setup failures.              |
+| `windows_sandbox.elevated_setup_canceled`        | counter   | See note                                  | Canceled elevated Windows sandbox setup attempts.     |
+| `windows_sandbox.elevated_setup_duration_ms`     | histogram | `result`                                  | Elevated Windows sandbox setup duration.              |
+| `windows_sandbox.elevated_prompt_shown`          | counter   |                                           | Elevated sandbox setup prompt shown.                  |
+| `windows_sandbox.elevated_prompt_accept`         | counter   |                                           | Elevated sandbox setup prompt accepted.               |
+| `windows_sandbox.elevated_prompt_use_legacy`     | counter   |                                           | User chose legacy sandbox from the elevated prompt.   |
+| `windows_sandbox.elevated_prompt_quit`           | counter   |                                           | User quit from the elevated prompt.                   |
+| `windows_sandbox.fallback_prompt_shown`          | counter   |                                           | Fallback sandbox prompt shown.                        |
+| `windows_sandbox.fallback_retry_elevated`        | counter   |                                           | User retried elevated setup from the fallback prompt. |
+| `windows_sandbox.fallback_use_legacy`            | counter   |                                           | User chose legacy sandbox from the fallback prompt.   |
+| `windows_sandbox.fallback_prompt_quit`           | counter   |                                           | User quit from the fallback prompt.                   |
+| `windows_sandbox.legacy_setup_preflight_failed`  | counter   | See note                                  | Legacy Windows sandbox setup preflight failure.       |
+| `windows_sandbox.setup_elevated_sandbox_command` | counter   |                                           | Elevated sandbox setup command invoked.               |
+| `windows_sandbox.createprocessasuserw_failed`    | counter   | `error_code`, `path_kind`, `exe`, `level` | Windows `CreateProcessAsUserW` failures.              |
+
+The elevated setup failure metrics include `code` and `message` when Windows setup failure details are available, and may include `originator` when emitted from the shared setup path. The `windows_sandbox.legacy_setup_preflight_failed` metric includes `originator` when emitted from the shared setup path, but fallback-prompt preflight failures may not include any fields.
 
 ### Feedback controls
 
@@ -432,6 +664,8 @@
 - `notify` runs an external program (good for webhooks, desktop notifiers, CI hooks).
 - `tui.notifications` is built in to the TUI and can optionally filter by event type (for example, `agent-turn-complete` and `approval-requested`).
 - `tui.notification_method` controls how the TUI emits terminal notifications (`auto`, `osc9`, or `bel`).
+- `tui.notification_condition` controls whether TUI notifications fire only when
+  the terminal is `unfocused` or `always`.
 
 In `auto` mode, Codex prefers OSC 9 notifications (a terminal escape sequence some terminals interpret as a desktop notification) and falls back to BEL (`\x07`) otherwise.
 
@@ -478,6 +712,8 @@
 
 - `tui.notifications`: enable/disable notifications (or restrict to specific types)
 - `tui.notification_method`: choose `auto`, `osc9`, or `bel` for terminal notifications
+- `tui.notification_condition`: choose `unfocused` or `always` for when
+  notifications fire
 - `tui.animations`: enable/disable ASCII animations and shimmer effects
 - `tui.alternate_screen`: control alternate screen usage (set to `never` to keep terminal scrollback)
 - `tui.show_tooltips`: show or hide onboarding tooltips on the welcome screen

```
#### https://developers.openai.com/codex/config-basic.md

```diff
--- a/https://developers.openai.com/codex/config-basic.md
+++ b/https://developers.openai.com/codex/config-basic.md
@@ -1,6 +1,6 @@
 # Config basics
 
-Codex reads configuration details from more than one location. Your personal defaults live in `~/.codex/config.toml`, and you can add project overrides with `.codex/config.toml` files. For security, Codex loads project config files only when you trust the project.
+Codex reads configuration details from more than one location. Your personal defaults live in `~/.codex/config.toml`, and you can add project overrides with `.codex/config.toml` files. For security, Codex loads project `.codex/` layers only when you trust the project.
 
 ## Codex configuration file
 
@@ -27,7 +27,7 @@
 
 Use that precedence to set shared defaults at the top level and keep profiles focused on the values that differ.
 
-If you mark a project as untrusted, Codex skips project-scoped `.codex/` layers (including `.codex/config.toml`) and falls back to user, system, and built-in defaults.
+If you mark a project as untrusted, Codex skips project-scoped `.codex/` layers, including project-local config, hooks, and rules. User and system config still load, including user/global hooks and rules.
 
 For one-off overrides via `-c`/`--config` (including TOML quoting rules), see [Advanced Config](https://developers.openai.com/codex/config-advanced#one-off-overrides-from-the-cli).
 
@@ -46,7 +46,7 @@
 Choose the model Codex uses by default in the CLI and IDE.
 
 ```toml
-model = "gpt-5.4"
+model = "gpt-5.5"
 ```
 
 #### Approval prompts
@@ -68,6 +68,16 @@
 ```
 
 For mode-by-mode behavior (including protected `.git`/`.codex` paths and network defaults), see [Sandbox and approvals](https://developers.openai.com/codex/agent-approvals-security#sandbox-and-approvals), [Protected paths in writable roots](https://developers.openai.com/codex/agent-approvals-security#protected-paths-in-writable-roots), and [Network access](https://developers.openai.com/codex/agent-approvals-security#network-access).
+
+#### Permission profiles
+
+Use a named permission profile when you want one reusable filesystem or network policy across sessions:
+
+```toml
+default_permissions = ":workspace"
+```
+
+Built-in profiles include `:read-only`, `:workspace`, and `:danger-no-sandbox`. For custom filesystem or network rules, define `[permissions.<name>]` tables and set `default_permissions` to that name.
 
 #### Windows sandbox mode
 
@@ -111,6 +121,18 @@
 
 You can override this later in an active session with `/personality` or per thread/turn when using the app-server APIs.
 
+#### TUI keymap
+
+Customize terminal shortcuts under `tui.keymap`. Context-specific bindings override `tui.keymap.global`, and an empty list unbinds the action.
+
+```toml
+[tui.keymap.global]
+open_transcript = "ctrl-t"
+
+[tui.keymap.composer]
+submit = ["enter", "ctrl-m"]
+```
+
 #### Command environment
 
 Control which environment variables Codex forwards to spawned commands.
@@ -145,26 +167,21 @@
 
 ### Supported features
 
-| Key                       | Default | Maturity     | Description                                                                                        |
-| ------------------------- | :-----: | ------------ | -------------------------------------------------------------------------------------------------- |
-| `apply_patch_freeform`    |  false  | Experimental | Include the freeform `apply_patch` tool                                                            |
-| `apps`                    |  false  | Experimental | Enable ChatGPT Apps/connectors support                                                             |
-| `apps_mcp_gateway`        |  false  | Experimental | Route Apps MCP calls through `https://api.openai.com/v1/connectors/mcp/` instead of legacy routing |
-| `collaboration_modes`     |  true   | Stable       | Enable collaboration modes such as plan mode                                                       |
-| `multi_agent`             |  false  | Experimental | Enable multi-agent collaboration tools                                                             |
-| `personality`             |  true   | Stable       | Enable personality selection controls                                                              |
-| `remote_models`           |  false  | Experimental | Refresh remote model list before showing readiness                                                 |
-| `runtime_metrics`         |  false  | Experimental | Show runtime metrics summaries in TUI turn separators                                              |
-| `request_rule`            |  true   | Stable       | Enable Smart approvals (`prefix_rule` suggestions)                                                 |
-| `search_tool`             |  false  | Experimental | Enable `search_tool_bm25` so Codex discovers Apps MCP tools via search before tool calls           |
-| `shell_snapshot`          |  false  | Beta         | Snapshot your shell environment to speed up repeated commands                                      |
-| `shell_tool`              |  true   | Stable       | Enable the default `shell` tool                                                                    |
-| `use_linux_sandbox_bwrap` |  false  | Experimental | Use the bubblewrap-based Linux sandbox pipeline                                                    |
-| `unified_exec`            |  false  | Beta         | Use the unified PTY-backed exec tool                                                               |
-| `undo`                    |  true   | Stable       | Enable undo via per-turn git ghost snapshots                                                       |
-| `web_search`              |  true   | Deprecated   | Legacy toggle; prefer the top-level `web_search` setting                                           |
-| `web_search_cached`       |  true   | Deprecated   | Legacy toggle that maps to `web_search = "cached"` when unset                                      |
-| `web_search_request`      |  true   | Deprecated   | Legacy toggle that maps to `web_search = "live"` when unset                                        |
+| Key                  |        Default        | Maturity     | Description                                                                              |
+| -------------------- | :-------------------: | ------------ | ---------------------------------------------------------------------------------------- |
+| `apps`               |         false         | Experimental | Enable ChatGPT Apps/connectors support                                                   |
+| `codex_hooks`        |         true          | Stable       | Enable lifecycle hooks from `hooks.json` or inline `[hooks]`. See [Hooks](https://developers.openai.com/codex/hooks). |
+| `fast_mode`          |         true          | Stable       | Enable Fast mode selection and the `service_tier = "fast"` path                          |
+| `memories`           |         false         | Stable       | Enable [Memories](https://developers.openai.com/codex/memories)                                                       |
+| `multi_agent`        |         true          | Stable       | Enable subagent collaboration tools                                                      |
+| `personality`        |         true          | Stable       | Enable personality selection controls                                                    |
+| `shell_snapshot`     |         true          | Stable       | Snapshot your shell environment to speed up repeated commands                            |
+| `shell_tool`         |         true          | Stable       | Enable the default `shell` tool                                                          |
+| `unified_exec`       | `true` except Windows | Stable       | Use the unified PTY-backed exec tool                                                     |
+| `undo`               |         false         | Stable       | Enable undo via per-turn git ghost snapshots                                             |
+| `web_search`         |         true          | Deprecated   | Legacy toggle; prefer the top-level `web_search` setting                                 |
+| `web_search_cached`  |         false         | Deprecated   | Legacy toggle that maps to `web_search = "cached"` when unset                            |
+| `web_search_request` |         false         | Deprecated   | Legacy toggle that maps to `web_search = "live"` when unset                              |
 
 The Maturity column uses feature maturity labels such as Experimental, Beta,
   and Stable. See [Feature Maturity](https://developers.openai.com/codex/feature-maturity) for how to
@@ -172,6 +189,8 @@
 
 Omit feature keys to keep their defaults.
 
+For the current lifecycle hooks MVP, see [Hooks](https://developers.openai.com/codex/hooks).
+
 ### Enabling features
 
 - In `config.toml`, add `feature_name = true` under `[features]`.

```
#### https://developers.openai.com/codex/config-reference.md

```diff
--- a/https://developers.openai.com/codex/config-reference.md
+++ b/https://developers.openai.com/codex/config-reference.md
@@ -13,7 +13,7 @@
     {
       key: "model",
       type: "string",
-      description: "Model to use (e.g., `gpt-5-codex`).",
+      description: "Model to use (e.g., `gpt-5.5`).",
     },
     {
       key: "review_model",
@@ -25,6 +25,12 @@
       key: "model_provider",
       type: "string",
       description: "Provider id from `model_providers` (default: `openai`).",
+    },
+    {
+      key: "openai_base_url",
+      type: "string",
+      description:
+        "Base URL override for the built-in `openai` model provider.",
     },
     {
       key: "model_context_window",
@@ -51,27 +57,51 @@
     },
     {
       key: "approval_policy",
-      type: "untrusted | on-request | never | { reject = { sandbox_approval = bool, rules = bool, mcp_elicitations = bool } }",
-      description:
-        "Controls when Codex pauses for approval before executing commands. You can also use `approval_policy = { reject = { ... } }` to auto-reject specific prompt categories while keeping other prompts interactive. `on-failure` is deprecated; use `on-request` for interactive runs or `never` for non-interactive runs.",
-    },
-    {
-      key: "approval_policy.reject.sandbox_approval",
-      type: "boolean",
-      description:
-        "When `true`, sandbox escalation approval prompts are auto-rejected.",
-    },
-    {
-      key: "approval_policy.reject.rules",
-      type: "boolean",
-      description:
-        "When `true`, approvals triggered by execpolicy `prompt` rules are auto-rejected.",
-    },
-    {
-      key: "approval_policy.reject.mcp_elicitations",
-      type: "boolean",
-      description:
-        "When `true`, MCP elicitation prompts are auto-rejected instead of shown to the user.",
+      type: "untrusted | on-request | never | { granular = { sandbox_approval = bool, rules = bool, mcp_elicitations = bool, request_permissions = bool, skill_approval = bool } }",
+      description:
+        "Controls when Codex pauses for approval before executing commands. You can also use `approval_policy = { granular = { ... } }` to allow or auto-reject specific prompt categories while keeping other prompts interactive. `on-failure` is deprecated; use `on-request` for interactive runs or `never` for non-interactive runs.",
+    },
+    {
+      key: "approval_policy.granular.sandbox_approval",
+      type: "boolean",
+      description:
+        "When `true`, sandbox escalation approval prompts are allowed to surface.",
+    },
+    {
+      key: "approval_policy.granular.rules",
+      type: "boolean",
+      description:
+        "When `true`, approvals triggered by execpolicy `prompt` rules are allowed to surface.",
+    },
+    {
+      key: "approval_policy.granular.mcp_elicitations",
+      type: "boolean",
+      description:
+        "When `true`, MCP elicitation prompts are allowed to surface instead of being auto-rejected.",
+    },
+    {
+      key: "approval_policy.granular.request_permissions",
+      type: "boolean",
+      description:
+        "When `true`, prompts from the `request_permissions` tool are allowed to surface.",
+    },
+    {
+      key: "approval_policy.granular.skill_approval",
+      type: "boolean",
+      description:
+        "When `true`, skill-script approval prompts are allowed to surface.",
+    },
+    {
+      key: "approvals_reviewer",
+      type: "user | auto_review",
+      description:
+        "Who reviews eligible approval prompts under `on-request` or granular approval policies. Defaults to `user`; `auto_review` uses the reviewer subagent. This setting doesn't change sandboxing or review actions already allowed inside the sandbox.",
+    },
+    {
+      key: "auto_review.policy",
+      type: "string",
+      description:
+        "Local Markdown policy instructions for automatic review. Managed `guardian_policy_config` takes precedence. Blank values are ignored.",
     },
     {
       key: "allow_login_shell",
@@ -116,6 +146,12 @@
         "Windows-only native sandbox mode when running Codex natively on Windows.",
     },
     {
+      key: "windows.sandbox_private_desktop",
+      type: "boolean",
+      description:
+        "Run the final sandboxed child process on a private desktop by default on native Windows. Set `false` only for compatibility with the older `Winsta0\\\\Default` behavior.",
+    },
+    {
       key: "notify",
       type: "array<string>",
       description:
@@ -132,6 +168,12 @@
       type: "boolean",
       description:
         "Enable feedback submission via `/feedback` across Codex surfaces (default: true).",
+    },
+    {
+      key: "analytics.enabled",
+      type: "boolean",
+      description:
+        "Enable or disable analytics for this machine/profile. When unset, the client default applies.",
     },
     {
       key: "instructions",
@@ -163,6 +205,12 @@
       description: "Inline override for the history compaction prompt.",
     },
     {
+      key: "commit_attribution",
+      type: "string",
+      description:
+        "Override the commit co-author trailer text. Set an empty string to disable automatic attribution.",
+    },
+    {
       key: "model_instructions_file",
       type: "string (path)",
       description:
@@ -173,6 +221,11 @@
       type: "none | friendly | pragmatic",
       description:
         "Default communication style for models that advertise `supportsPersonality`; can be overridden per thread/turn or via `/personality`.",
+    },
+    {
+      key: "service_tier",
+      type: "flex | fast",
+      description: "Preferred service tier for new turns.",
     },
     {
       key: "experimental_compact_prompt_file",
@@ -255,15 +308,38 @@
       description: "Per-tool approval behavior override for a single app tool.",
     },
     {
+      key: "tool_suggest.discoverables",
+      type: "array<table>",
+      description:
+        'Allow tool suggestions for additional discoverable connectors or plugins. Each entry uses `type = "connector"` or `"plugin"` and an `id`.',
+    },
+    {
+      key: "tool_suggest.disabled_tools",
+      type: "array<table>",
+      description:
+        'Disable suggestions for specific discoverable connectors or plugins. Each entry uses `type = "connector"` or `"plugin"` and an `id`.',
+    },
+    {
       key: "features.apps",
       type: "boolean",
       description: "Enable ChatGPT Apps/connectors support (experimental).",
     },
     {
-      key: "features.apps_mcp_gateway",
-      type: "boolean",
-      description:
-        "Route Apps MCP calls through the OpenAI connectors MCP gateway (`https://api.openai.com/v1/connectors/mcp/`) instead of legacy routing (experimental).",
+      key: "features.codex_hooks",
+      type: "boolean",
+      description:
+        "Enable lifecycle hooks loaded from `hooks.json` or inline `[hooks]` config.",
+    },
+    {
+      key: "hooks",
+      type: "table",
+      description:
+        "Lifecycle hooks configured inline in `config.toml`. Uses the same event schema as `hooks.json`; see the Hooks guide for examples and supported events.",
+    },
+    {
+      key: "features.memories",
+      type: "boolean",
+      description: "Enable [Memories](https://developers.openai.com/codex/memories) (off by default).",
     },
     {
       key: "mcp_servers.<id>.command",
@@ -282,9 +358,9 @@
     },
     {
       key: "mcp_servers.<id>.env_vars",
-      type: "array<string>",
-      description:
-        "Additional environment variables to whitelist for an MCP stdio server.",
+      type: 'array<string | { name = string, source = "local" | "remote" }>',
+      description:
+        'Additional environment variables to whitelist for an MCP stdio server. String entries default to `source = "local"`; use `source = "remote"` only with executor-backed remote stdio.',
     },
     {
       key: "mcp_servers.<id>.cwd",
@@ -353,10 +429,28 @@
         "Deny list applied after `enabled_tools` for the MCP server.",
     },
     {
+      key: "mcp_servers.<id>.scopes",
+      type: "array<string>",
+      description:
+        "OAuth scopes to request when authenticating to that MCP server.",
+    },
+    {
+      key: "mcp_servers.<id>.oauth_resource",
+      type: "string",
+      description:
+        "Optional RFC 8707 OAuth resource parameter to include during MCP login.",
+    },
+    {
+      key: "mcp_servers.<id>.experimental_environment",
+      type: "local | remote",
+      description:
+        "Experimental placement for an MCP server. `remote` starts stdio servers through a remote executor environment; streamable HTTP remote placement is not implemented.",
+    },
+    {
       key: "agents.max_threads",
       type: "number",
       description:
-        "Maximum number of agent threads that can be open concurrently.",
+        "Maximum number of agent threads that can be open concurrently. Defaults to `6` when unset.",
     },
     {
       key: "agents.max_depth",
@@ -383,26 +477,97 @@
         "Path to a TOML config layer for that role; relative paths resolve from the config file that declares the role.",
     },
     {
+      key: "agents.<name>.nickname_candidates",
+      type: "array<string>",
+      description:
+        "Optional pool of display nicknames for spawned agents in that role.",
+    },
+    {
+      key: "memories.generate_memories",
+      type: "boolean",
+      description:
+        "When `false`, newly created threads are not stored as memory-generation inputs. Defaults to `true`.",
+    },
+    {
+      key: "memories.use_memories",
+      type: "boolean",
+      description:
+        "When `false`, Codex skips injecting existing memories into future sessions. Defaults to `true`.",
+    },
+    {
+      key: "memories.disable_on_external_context",
+      type: "boolean",
+      description:
+        "When `true`, threads that use external context such as MCP tool calls, web search, or tool search are kept out of memory generation. Defaults to `false`. Legacy alias: `memories.no_memories_if_mcp_or_web_search`.",
+    },
+    {
+      key: "memories.max_raw_memories_for_consolidation",
+      type: "number",
+      description:
+        "Maximum recent raw memories retained for global consolidation. Defaults to `256` and is capped at `4096`.",
+    },
+    {
+      key: "memories.max_unused_days",
+      type: "number",
+      description:
+        "Maximum days since a memory was last used before it becomes ineligible for consolidation. Defaults to `30` and is clamped to `0`-`365`.",
+    },
+    {
+      key: "memories.max_rollout_age_days",
+      type: "number",
+      description:
+        "Maximum age of threads considered for memory generation. Defaults to `30` and is clamped to `0`-`90`.",
+    },
+    {
+      key: "memories.max_rollouts_per_startup",
+      type: "number",
+      description:
+        "Maximum rollout candidates processed per startup pass. Defaults to `16` and is capped at `128`.",
+    },
+    {
+      key: "memories.min_rollout_idle_hours",
+      type: "number",
+      description:
+        "Minimum idle time before a thread is considered for memory generation. Defaults to `6` and is clamped to `1`-`48`.",
+    },
+    {
+      key: "memories.min_rate_limit_remaining_percent",
+      type: "number",
+      description:
+        "Minimum remaining percentage required in Codex rate-limit windows before memory generation starts. Defaults to `25` and is clamped to `0`-`100`.",
+    },
+    {
+      key: "memories.extract_model",
+      type: "string",
+      description: "Optional model override for per-thread memory extraction.",
+    },
+    {
+      key: "memories.consolidation_model",
+      type: "string",
+      description: "Optional model override for global memory consolidation.",
+    },
+    {
       key: "features.unified_exec",
       type: "boolean",
-      description: "Use the unified PTY-backed exec tool (beta).",
+      description:
+        "Use the unified PTY-backed exec tool (stable; enabled by default except on Windows).",
     },
     {
       key: "features.shell_snapshot",
       type: "boolean",
       description:
-        "Snapshot shell environment to speed up repeated commands (beta).",
-    },
-    {
-      key: "features.apply_patch_freeform",
-      type: "boolean",
-      description: "Expose the freeform `apply_patch` tool (experimental).",
+        "Snapshot shell environment to speed up repeated commands (stable; on by default).",
+    },
+    {
+      key: "features.undo",
+      type: "boolean",
+      description: "Enable undo support (stable; off by default).",
     },
     {
       key: "features.multi_agent",
       type: "boolean",
       description:
-        "Enable multi-agent collaboration tools (`spawn_agent`, `send_input`, `resume_agent`, `wait`, `close_agent`, and `spawn_agents_on_csv`) (experimental; off by default).",
+        "Enable multi-agent collaboration tools (`spawn_agent`, `send_input`, `resume_agent`, `wait_agent`, and `close_agent`) (stable; on by default).",
     },
     {
       key: "features.personality",
@@ -435,51 +600,28 @@
         "Enable the default `shell` tool for running commands (stable; on by default).",
     },
     {
-      key: "features.request_rule",
-      type: "boolean",
-      description:
-        "Enable Smart approvals (`prefix_rule` suggestions on escalation requests; stable; on by default).",
-    },
-    {
-      key: "features.search_tool",
-      type: "boolean",
-      description:
-        "Enable `search_tool_bm25` for Apps tool discovery before invoking app MCP tools (experimental).",
-    },
-    {
-      key: "features.collaboration_modes",
-      type: "boolean",
-      description:
-        "Enable collaboration modes such as plan mode (stable; on by default).",
-    },
-    {
-      key: "features.use_linux_sandbox_bwrap",
-      type: "boolean",
-      description:
-        "Use the bubblewrap-based Linux sandbox pipeline (experimental; off by default).",
-    },
-    {
-      key: "features.remote_models",
-      type: "boolean",
-      description:
-        "Refresh remote model list before showing readiness (experimental).",
-    },
-    {
-      key: "features.runtime_metrics",
-      type: "boolean",
-      description:
-        "Show runtime metrics summary in TUI turn separators (experimental).",
-    },
-    {
-      key: "features.powershell_utf8",
-      type: "boolean",
-      description: "Force PowerShell UTF-8 output (defaults to true).",
-    },
-    {
-      key: "features.child_agents_md",
-      type: "boolean",
-      description:
-        "Append AGENTS.md scope/precedence guidance even when no AGENTS.md is present (experimental).",
+      key: "features.enable_request_compression",
+      type: "boolean",
+      description:
+        "Compress streaming request bodies with zstd when supported (stable; on by default).",
+    },
+    {
+      key: "features.skill_mcp_dependency_install",
+      type: "boolean",
+      description:
+        "Allow prompting and installing missing MCP dependencies for skills (stable; on by default).",
+    },
+    {
+      key: "features.fast_mode",
+      type: "boolean",
+      description:
+        'Enable Fast mode selection and the `service_tier = "fast"` path (stable; on by default).',
+    },
+    {
+      key: "features.prevent_idle_sleep",
+      type: "boolean",
+      description:
+        "Prevent the machine from sleeping while a turn is actively running (experimental; off by default).",
     },
     {
       key: "suppress_unstable_features_warning",
@@ -488,6 +630,12 @@
         "Suppress the warning that appears when under-development feature flags are enabled.",
     },
     {
+      key: "model_providers.<id>",
+      type: "table",
+      description:
+        "Custom provider definition. Built-in provider IDs (`openai`, `ollama`, and `lmstudio`) are reserved and cannot be overridden.",
+    },
+    {
       key: "model_providers.<id>.name",
       type: "string",
       description: "Display name for a custom model provider.",
@@ -521,9 +669,9 @@
     },
     {
       key: "model_providers.<id>.wire_api",
-      type: "chat | responses",
-      description:
-        "Protocol used by the provider (defaults to `chat` if omitted).",
+      type: "responses",
+      description:
+        "Protocol used by the provider. `responses` is the only supported value, and it is the default when omitted.",
     },
     {
       key: "model_providers.<id>.query_params",
@@ -559,12 +707,69 @@
         "Idle timeout for SSE streams in milliseconds (default: 300000).",
     },
     {
+      key: "model_providers.<id>.supports_websockets",
+      type: "boolean",
+      description:
+        "Whether that provider supports the Responses API WebSocket transport.",
+    },
+    {
+      key: "model_providers.<id>.auth",
+      type: "table",
+      description:
+        "Command-backed bearer token configuration for a custom provider. Do not combine with `env_key`, `experimental_bearer_token`, or `requires_openai_auth`.",
+    },
+    {
+      key: "model_providers.<id>.auth.command",
+      type: "string",
+      description:
+        "Command to run when Codex needs a bearer token. The command must print the token to stdout.",
+    },
+    {
+      key: "model_providers.<id>.auth.args",
+      type: "array<string>",
+      description: "Arguments passed to the token command.",
+    },
+    {
+      key: "model_providers.<id>.auth.timeout_ms",
+      type: "number",
+      description:
+        "Maximum token command runtime in milliseconds (default: 5000).",
+    },
+    {
+      key: "model_providers.<id>.auth.refresh_interval_ms",
+      type: "number",
+      description:
+        "How often Codex proactively refreshes the token in milliseconds (default: 300000). Set to `0` to refresh only after an authentication retry.",
+    },
+    {
+      key: "model_providers.<id>.auth.cwd",
+      type: "string (path)",
+      description: "Working directory for the token command.",
+    },
+    {
+      key: "model_providers.amazon-bedrock.aws.profile",
+      type: "string",
+      description:
+        "AWS profile name used by the built-in `amazon-bedrock` provider.",
+    },
+    {
+      key: "model_providers.amazon-bedrock.aws.region",
+      type: "string",
+      description: "AWS region used by the built-in `amazon-bedrock` provider.",
+    },
+    {
       key: "model_reasoning_effort",
       type: "minimal | low | medium | high | xhigh",
       description:
         "Adjust reasoning effort for supported models (Responses API only; `xhigh` is model-dependent).",
     },
     {
+      key: "plan_mode_reasoning_effort",
+      type: "none | minimal | low | medium | high | xhigh",
+      description:
+        "Plan-mode-specific reasoning override. When unset, Plan mode uses its built-in preset default.",
+    },
+    {
       key: "model_reasoning_summary",
       type: "auto | concise | detailed | none",
       description:
@@ -574,7 +779,7 @@
       key: "model_verbosity",
       type: "low | medium | high",
       description:
-        "Control GPT-5 Responses API verbosity (defaults to `medium`).",
+        "Optional GPT-5 Responses API verbosity override; when unset, the selected model/preset default is used.",
     },
     {
       key: "model_supports_reasoning_summaries",
@@ -646,10 +851,14 @@
         "Profile-scoped overrides for any of the supported configuration keys.",
     },
     {
-      key: "profiles.<name>.include_apply_patch_tool",
-      type: "boolean",
-      description:
-        "Legacy name for enabling freeform apply_patch; prefer `[features].apply_patch_freeform`.",
+      key: "profiles.<name>.service_tier",
+      type: "flex | fast",
+      description: "Profile-scoped service tier preference for new turns.",
+    },
+    {
+      key: "profiles.<name>.plan_mode_reasoning_effort",
+      type: "none | minimal | low | medium | high | xhigh",
+      description: "Profile-scoped Plan-mode reasoning override.",
     },
     {
       key: "profiles.<name>.web_search",
@@ -670,16 +879,16 @@
         "Profile-scoped model catalog JSON path override (applied on startup only; overrides the top-level `model_catalog_json` for that profile).",
     },
     {
+      key: "profiles.<name>.model_instructions_file",
+      type: "string (path)",
+      description:
+        "Profile-scoped replacement for the built-in instruction file.",
+    },
+    {
       key: "profiles.<name>.experimental_use_unified_exec_tool",
       type: "boolean",
       description:
         "Legacy name for enabling unified exec; prefer `[features].unified_exec`.",
-    },
-    {
-      key: "profiles.<name>.experimental_use_freeform_apply_patch",
-      type: "boolean",
-      description:
-        "Legacy name for enabling freeform apply_patch; prefer `[features].apply_patch_freeform`.",
     },
     {
       key: "profiles.<name>.oss_provider",
@@ -687,6 +896,21 @@
       description: "Profile-scoped OSS provider for `--oss` sessions.",
     },
     {
+      key: "profiles.<name>.tools_view_image",
+      type: "boolean",
+      description: "Enable or disable the `view_image` tool in that profile.",
+    },
+    {
+      key: "profiles.<name>.analytics.enabled",
+      type: "boolean",
+      description: "Profile-scoped analytics enablement override.",
+    },
+    {
+      key: "profiles.<name>.windows.sandbox",
+      type: "unelevated | elevated",
+      description: "Profile-scoped Windows sandbox mode override.",
+    },
+    {
       key: "history.persistence",
       type: "save-all | none",
       description:
@@ -733,6 +957,12 @@
       type: "none | otlp-http | otlp-grpc",
       description:
         "Select the OpenTelemetry trace exporter and provide any endpoint metadata.",
+    },
+    {
+      key: "otel.metrics_exporter",
+      type: "none | statsig | otlp-http | otlp-grpc",
+      description:
+        "Select the OpenTelemetry metrics exporter (defaults to `statsig`).",
     },
     {
       key: "otel.log_user_prompt",
@@ -816,7 +1046,13 @@
       key: "tui.notification_method",
       type: "auto | osc9 | bel",
       description:
-        "Notification method for unfocused terminal notifications (default: auto).",
+        "Notification method for terminal notifications (default: auto).",
+    },
+    {
+      key: "tui.notification_condition",
+      type: "unfocused | always",
+      description:
+        "Control whether TUI notifications fire only when the terminal is unfocused or regardless of focus. Defaults to `unfocused`.",
     },
     {
       key: "tui.animations",
@@ -841,6 +1077,35 @@
       type: "array<string> | null",
       description:
         "Ordered list of TUI footer status-line item identifiers. `null` disables the status line.",
+    },
+    {
+      key: "tui.terminal_title",
+      type: "array<string> | null",
+      description:
+        'Ordered list of terminal window/tab title item identifiers. Defaults to `["spinner", "project"]`; `null` disables title updates.',
+    },
+    {
+      key: "tui.theme",
+      type: "string",
+      description:
+        "Syntax-highlighting theme override (kebab-case theme name).",
+    },
+    {
+      key: "tui.keymap.<context>.<action>",
+      type: "string | array<string>",
+      description:
+        "Keyboard shortcut binding for a TUI action. Supported contexts include `global`, `chat`, `composer`, `editor`, `pager`, `list`, and `approval`; context-specific bindings override `tui.keymap.global`.",
+    },
+    {
+      key: "tui.keymap.<context>.<action> = []",
+      type: "empty array",
+      description:
+        "Unbind the action in that keymap context. Key names use normalized strings such as `ctrl-a`, `shift-enter`, or `page-down`.",
+    },
+    {
+      key: "tui.model_availability_nux.<model>",
+      type: "integer",
+      description: "Internal startup-tooltip state keyed by model slug.",
     },
     {
       key: "hide_agent_reasoning",
@@ -899,22 +1164,15 @@
         "Legacy name for enabling unified exec; prefer `[features].unified_exec` or `codex --enable unified_exec`.",
     },
     {
-      key: "experimental_use_freeform_apply_patch",
-      type: "boolean",
-      description:
-        "Legacy name for enabling freeform apply_patch; prefer `[features].apply_patch_freeform` or `codex --enable apply_patch_freeform`.",
-    },
-    {
-      key: "include_apply_patch_tool",
-      type: "boolean",
-      description:
-        "Legacy name for enabling freeform apply_patch; prefer `[features].apply_patch_freeform`.",
-    },
-    {
       key: "tools.web_search",
-      type: "boolean",
-      description:
-        "Deprecated legacy toggle for web search; prefer the top-level `web_search` setting.",
+      type: 'boolean | { context_size = "low|medium|high", allowed_domains = [string], location = { country, region, city, timezone } }',
+      description:
+        "Optional web search tool configuration. The legacy boolean form is still accepted, but the object form lets you set search context size, allowed domains, and approximate user location.",
+    },
+    {
+      key: "tools.view_image",
+      type: "boolean",
+      description: "Enable the local-image attachment tool `view_image`.",
     },
     {
       key: "web_search",
@@ -923,10 +1181,108 @@
         'Web search mode (default: `"cached"`; cached uses an OpenAI-maintained index and does not fetch live pages; if you use `--yolo` or another full access sandbox setting, it defaults to `"live"`). Use `"live"` to fetch the most recent data from the web, or `"disabled"` to remove the tool.',
     },
     {
+      key: "default_permissions",
+      type: "string",
+      description:
+        "Name of the default permissions profile to apply to sandboxed tool calls. Built-ins are `:read-only`, `:workspace`, and `:danger-no-sandbox`; custom profile names require matching `[permissions.<name>]` tables.",
+    },
+    {
+      key: "permissions.<name>.filesystem",
+      type: "table",
+      description:
+        "Named filesystem permission profile. Each key is an absolute path or special token such as `:minimal` or `:project_roots`.",
+    },
+    {
+      key: "permissions.<name>.filesystem.glob_scan_max_depth",
+      type: "number",
+      description:
+        "Maximum depth for expanding deny-read glob patterns on platforms that snapshot matches before sandbox startup. Must be at least `1` when set.",
+    },
+    {
+      key: "permissions.<name>.filesystem.<path-or-glob>",
+      type: '"read" | "write" | "none" | table',
+      description:
+        'Grant direct access for a path, glob pattern, or special token, or scope nested entries under that root. Use `"none"` to deny reads for matching paths.',
+    },
+    {
+      key: 'permissions.<name>.filesystem.":project_roots".<subpath-or-glob>',
+      type: '"read" | "write" | "none"',
+      description:
+        'Scoped filesystem access relative to the detected project roots. Use `"."` for the root itself; glob subpaths such as `"**/*.env"` can deny reads with `"none"`.',
+    },
+    {
+      key: "permissions.<name>.network.enabled",
+      type: "boolean",
+      description: "Enable network access for this named permissions profile.",
+    },
+    {
+      key: "permissions.<name>.network.proxy_url",
+      type: "string",
+      description:
+        "HTTP proxy endpoint used when this permissions profile enables the managed network proxy.",
+    },
+    {
+      key: "permissions.<name>.network.enable_socks5",
+      type: "boolean",
+      description:
+        "Expose a SOCKS5 listener when this permissions profile enables the managed network proxy.",
+    },
+    {
+      key: "permissions.<name>.network.socks_url",
+      type: "string",
+      description: "SOCKS5 proxy endpoint used by this permissions profile.",
+    },
+    {
+      key: "permissions.<name>.network.enable_socks5_udp",
+      type: "boolean",
+      description: "Allow UDP over the SOCKS5 listener when enabled.",
+    },
+    {
+      key: "permissions.<name>.network.allow_upstream_proxy",
+      type: "boolean",
+      description:
+        "Allow the managed proxy to chain to another upstream proxy.",
+    },
+    {
+      key: "permissions.<name>.network.dangerously_allow_non_loopback_proxy",
+      type: "boolean",
+      description:
+        "Permit non-loopback bind addresses for the managed proxy listener.",
+    },
+    {
+      key: "permissions.<name>.network.dangerously_allow_all_unix_sockets",
+      type: "boolean",
+      description:
+        "Allow the proxy to use arbitrary Unix sockets instead of the default restricted set.",
+    },
+    {
+      key: "permissions.<name>.network.mode",
+      type: "limited | full",
+      description: "Network proxy mode used for subprocess traffic.",
+    },
+    {
+      key: "permissions.<name>.network.domains",
+      type: "map<string, allow | deny>",
+      description:
+        "Domain rules for the managed proxy. Use domain names or wildcard patterns as keys, with `allow` or `deny` values.",
+    },
+    {
+      key: "permissions.<name>.network.unix_sockets",
+      type: "map<string, allow | none>",
+      description:
+        "Unix socket rules for the managed proxy. Use socket paths as keys, with `allow` or `none` values.",
+    },
+    {
+      key: "permissions.<name>.network.allow_local_binding",
+      type: "boolean",
+      description:
+        "Permit local bind/listen operations through the managed proxy.",
+    },
+    {
       key: "projects.<path>.trust_level",
       type: "string",
       description:
-        'Mark a project or worktree as trusted or untrusted (`"trusted"` | `"untrusted"`). Untrusted projects skip project-scoped `.codex/` layers.',
+        'Mark a project or worktree as trusted or untrusted (`"trusted"` | `"untrusted"`). Untrusted projects skip project-scoped `.codex/` layers, including project-local config, hooks, and rules.',
     },
     {
       key: "notice.hide_full_access_warning",
@@ -1000,12 +1356,42 @@
       key: "allowed_approval_policies",
       type: "array<string>",
       description:
-        "Allowed values for `approval_policy` (for example `untrusted`, `on-request`, `never`, and `reject`).",
+        "Allowed values for `approval_policy` (for example `untrusted`, `on-request`, `never`, and `granular`).",
+    },
+    {
+      key: "allowed_approvals_reviewers",
+      type: "array<string>",
+      description:
+        "Allowed values for `approvals_reviewer`, such as `user` and `auto_review`.",
+    },
+    {
+      key: "guardian_policy_config",
+      type: "string",
+      description:
+        "Managed Markdown policy instructions for automatic review. This takes precedence over local `[auto_review].policy`. Blank values are ignored.",
     },
     {
       key: "allowed_sandbox_modes",
       type: "array<string>",
       description: "Allowed values for `sandbox_mode`.",
+    },
+    {
+      key: "remote_sandbox_config",
+      type: "array<table>",
+      description:
+        "Host-specific sandbox requirements. The first entry whose `hostname_patterns` match the resolved host name overrides top-level `allowed_sandbox_modes` for that requirements source. Host-specific entries currently override sandbox modes only.",
+    },
+    {
+      key: "remote_sandbox_config[].hostname_patterns",
+      type: "array<string>",
+      description:
+        "Case-insensitive host name patterns. Supports `*` for any sequence of characters and `?` for one character.",
+    },
+    {
+      key: "remote_sandbox_config[].allowed_sandbox_modes",
+      type: "array<string>",
+      description:
+        "Allowed sandbox modes to apply when this host-specific entry matches.",
     },
     {
       key: "allowed_web_search_modes",
@@ -1024,6 +1410,60 @@
       type: "boolean",
       description:
         "Require a specific canonical feature key to stay enabled or disabled.",
+    },
+    {
+      key: "features.in_app_browser",
+      type: "boolean",
+      description:
+        "Set to `false` in `requirements.toml` to disable the in-app browser pane.",
+    },
+    {
+      key: "features.browser_use",
+      type: "boolean",
+      description:
+        "Set to `false` in `requirements.toml` to disable Browser Use and Browser Agent availability.",
+    },
+    {
+      key: "features.computer_use",
+      type: "boolean",
+      description:
+        "Set to `false` in `requirements.toml` to disable Computer Use availability and related install or enablement flows.",
+    },
+    {
+      key: "hooks",
+      type: "table",
+      description:
+        "Admin-enforced managed lifecycle hooks. Requires a managed hook directory and uses the same event schema as inline `[hooks]` in `config.toml`.",
+    },
+    {
+      key: "hooks.managed_dir",
+      type: "string (absolute path)",
+      description:
+        "Directory containing managed hook scripts on macOS and Linux. Codex validates that it is absolute and exists before loading managed hooks.",
+    },
+    {
+      key: "hooks.windows_managed_dir",
+      type: "string (absolute path)",
+      description:
+        "Directory containing managed hook scripts on Windows. Codex validates that it is absolute and exists before loading managed hooks.",
+    },
+    {
+      key: "hooks.<Event>",
+      type: "array<table>",
+      description:
+        "Matcher groups for a hook event such as `PreToolUse`, `PostToolUse`, `PermissionRequest`, `SessionStart`, `UserPromptSubmit`, or `Stop`.",
+    },
+    {
+      key: "hooks.<Event>[].hooks",
+      type: "array<table>",
+      description:
+        "Hook handlers for a matcher group. Command hooks are currently supported; prompt and agent hook handlers are parsed but skipped.",
+    },
+    {
+      key: "permissions.filesystem.deny_read",
+      type: "array<string>",
+      description:
+        "Admin-enforced filesystem read denials. Entries can be paths or glob patterns, and users cannot weaken them with local config.",
     },
     {
       key: "mcp_servers",

```
#### https://developers.openai.com/codex/config-sample.md

```diff
--- a/https://developers.openai.com/codex/config-sample.md
+++ b/https://developers.openai.com/codex/config-sample.md
@@ -15,7 +15,7 @@
 ```toml
 # Codex example configuration (config.toml)
 #
-# This file lists all keys Codex reads from config.toml, along with default
+# This file lists the main keys Codex reads from config.toml, along with default
 # behaviors, recommended examples, and concise explanations. Adjust as needed.
 #
 # Notes
@@ -27,15 +27,14 @@
 # Core Model Selection
 ################################################################################
 
-# Primary model used by Codex. Recommended example for most users: "gpt-5.4".
-model = "gpt-5.4"
-
-# Default communication style for supported models. Default: "friendly".
-# Allowed values: none | friendly | pragmatic
-# personality = "friendly"
+# Primary model used by Codex. Recommended example for most users: "gpt-5.5".
+model = "gpt-5.5"
+
+# Communication style for supported models. Allowed values: none | friendly | pragmatic
+# personality = "pragmatic"
 
 # Optional model override for /review. Default: unset (uses current session model).
-# review_model = "gpt-5.4"
+# review_model = "gpt-5.5"
 
 # Provider id selected from [model_providers]. Default: "openai".
 model_provider = "openai"
@@ -43,11 +42,13 @@
 # Default OSS provider for --oss sessions. When unset, Codex prompts. Default: unset.
 # oss_provider = "ollama"
 
-# Optional manual model metadata. When unset, Codex auto-detects from model.
-# Uncomment to force values.
+# Preferred service tier. `fast` is honored only when enabled in [features].
+# service_tier = "flex"  # fast | flex
+
+# Optional manual model metadata. When unset, Codex uses model or preset defaults.
 # model_context_window = 128000       # tokens; default: auto for model
-# model_auto_compact_token_limit = 0  # tokens; unset uses model defaults
-# tool_output_token_limit = 10000     # tokens stored per tool output
+# model_auto_compact_token_limit = 64000  # tokens; unset uses model defaults
+# tool_output_token_limit = 12000     # tokens stored per tool output
 # model_catalog_json = "/absolute/path/to/models.json" # optional startup-only model catalog override
 # background_terminal_max_timeout = 300000 # ms; max empty write_stdin poll window (default 5m)
 # log_dir = "/absolute/path/to/codex-logs" # directory for Codex logs; default: "$CODEX_HOME/log"
@@ -57,16 +58,19 @@
 # Reasoning & Verbosity (Responses API capable models)
 ################################################################################
 
-# Reasoning effort: minimal | low | medium | high | xhigh (default: medium; `xhigh` availability is model-dependent)
-model_reasoning_effort = "medium"
-
-# Reasoning summary: auto | concise | detailed | none (default: auto)
+# Reasoning effort: minimal | low | medium | high | xhigh
+# model_reasoning_effort = "medium"
+
+# Optional override used when Codex runs in plan mode: none | minimal | low | medium | high | xhigh
+# plan_mode_reasoning_effort = "high"
+
+# Reasoning summary: auto | concise | detailed | none
 # model_reasoning_summary = "auto"
 
-# Text verbosity for GPT-5 family (Responses API): low | medium | high (default: medium)
+# Text verbosity for GPT-5 family (Responses API): low | medium | high
 # model_verbosity = "medium"
 
-# Force enable or disable reasoning summaries for current model
+# Force enable or disable reasoning summaries for current model.
 # model_supports_reasoning_summaries = true
 
 ################################################################################
@@ -76,32 +80,24 @@
 # Additional user instructions are injected before AGENTS.md. Default: unset.
 # developer_instructions = ""
 
-# (Ignored) Optional legacy base instructions override (prefer AGENTS.md). Default: unset.
-# instructions = ""
-
 # Inline override for the history compaction prompt. Default: unset.
 # compact_prompt = ""
 
+# Override the default commit co-author trailer. Set to "" to disable it.
+# commit_attribution = "Jane Doe <jane@example.com>"
+
 # Override built-in base instructions with a file path. Default: unset.
 # model_instructions_file = "/absolute/or/relative/path/to/instructions.txt"
 
-# Migration note: experimental_instructions_file was renamed to model_instructions_file (deprecated).
-
 # Load the compact prompt override from a file. Default: unset.
 # experimental_compact_prompt_file = "/absolute/or/relative/path/to/compact_prompt.txt"
 
-# Legacy name for apply_patch_freeform. Default: false
-include_apply_patch_tool = false
-
-
 ################################################################################
 # Notifications
 ################################################################################
 
 # External notifier program (argv array). When unset: disabled.
-# Example: notify = ["notify-send", "Codex"]
-notify = [ ]
-
+# notify = ["notify-send", "Codex"]
 
 ################################################################################
 # Approval & Sandbox
@@ -111,10 +107,19 @@
 # - untrusted: only known-safe read-only commands auto-run; others prompt
 # - on-request: model decides when to ask (default)
 # - never: never prompt (risky)
-# - { reject = { ... } }: auto-reject selected prompt categories
+# - { granular = { ... } }: allow or auto-reject selected prompt categories
 approval_policy = "on-request"
-# Example granular auto-reject policy:
-# approval_policy = { reject = { sandbox_approval = true, rules = false, mcp_elicitations = false } }
+# Who reviews eligible approval prompts: user (default) | auto_review
+# approvals_reviewer = "user"
+
+# Example granular policy:
+# approval_policy = { granular = {
+#   sandbox_approval = true,
+#   rules = true,
+#   mcp_elicitations = true,
+#   request_permissions = false,
+#   skill_approval = false
+# } }
 
 # Allow login-shell semantics for shell-based tools when they request `login = true`.
 # Default: true. Set false to force non-login shells and reject explicit login-shell requests.
@@ -125,10 +130,18 @@
 # - workspace-write
 # - danger-full-access (no sandbox; extremely risky)
 sandbox_mode = "read-only"
-
-[windows]
-# Native Windows sandbox mode (Windows only): unelevated | elevated
-sandbox = "unelevated"
+# Named permissions profile to apply by default. Built-ins:
+# :read-only | :workspace | :danger-no-sandbox
+# Use a custom name such as "workspace" only when you also define [permissions.workspace].
+# default_permissions = ":workspace"
+
+# Example filesystem profile. Use `"none"` to deny reads for exact paths or
+# glob patterns. On platforms that need pre-expanded glob matches, set
+# glob_scan_max_depth when using unbounded patterns such as `**`.
+# [permissions.workspace.filesystem]
+# glob_scan_max_depth = 3
+# ":project_roots" = { "." = "write", "**/*.env" = "none" }
+# "/absolute/path/to/secrets" = "none"
 
 ################################################################################
 # Authentication & Login
@@ -137,11 +150,14 @@
 # Where to persist CLI login credentials: file (default) | keyring | auto
 cli_auth_credentials_store = "file"
 
-# Base URL for ChatGPT auth flow (not OpenAI API). Default:
+# Base URL for ChatGPT auth flow (not OpenAI API).
 chatgpt_base_url = "https://chatgpt.com/backend-api/"
 
+# Optional base URL override for the built-in OpenAI provider.
+# openai_base_url = "https://us.api.openai.com/v1"
+
 # Restrict ChatGPT login to a specific workspace id. Default: unset.
-# forced_chatgpt_workspace_id = ""
+# forced_chatgpt_workspace_id = "00000000-0000-0000-0000-000000000000"
 
 # Force login mechanism when Codex would normally auto-select. Default: unset.
 # Allowed values: chatgpt | api
@@ -149,10 +165,8 @@
 
 # Preferred store for MCP OAuth credentials: auto (default) | file | keyring
 mcp_oauth_credentials_store = "auto"
-
 # Optional fixed port for MCP OAuth callback: 1-65535. Default: unset.
 # mcp_oauth_callback_port = 4321
-
 # Optional redirect URI override for MCP OAuth login (for example, remote devbox ingress).
 # Custom callback paths are supported. `mcp_oauth_callback_port` still controls the listener port.
 # mcp_oauth_callback_url = "https://devbox.example.internal/callback"
@@ -206,18 +220,17 @@
 # If you use --yolo or another full access sandbox setting, web search defaults to live.
 web_search = "cached"
 
-################################################################################
-# Profiles (named presets)
-################################################################################
-
 # Active profile name. When unset, no profile is applied.
 # profile = "default"
 
+# Suppress the warning shown when under-development feature flags are enabled.
+# suppress_unstable_features_warning = true
+
 ################################################################################
 # Agents (multi-agent roles and limits)
 ################################################################################
 
-# [agents]
+[agents]
 # Maximum concurrently open agent threads. Default: 6
 # max_threads = 6
 # Maximum nested spawn depth. Root session starts at depth 0. Default: 1
@@ -226,8 +239,9 @@
 # job_max_runtime_seconds = 1800
 
 # [agents.reviewer]
-# description = "Find security, correctness, and test risks in code."
+# description = "Find correctness, security, and test risks in code."
 # config_file = "./agents/reviewer.toml"  # relative to the config.toml that defines it
+# nickname_candidates = ["Athena", "Ada"]
 
 ################################################################################
 # Skills (per-skill overrides)
@@ -237,15 +251,6 @@
 [[skills.config]]
 # path = "/path/to/skill/SKILL.md"
 # enabled = false
-
-################################################################################
-# Experimental toggles (legacy; prefer [features])
-################################################################################
-
-experimental_use_unified_exec_tool = false
-
-# Include apply_patch via freeform editing path (affects default tool set). Default: false
-experimental_use_freeform_apply_patch = false
 
 ################################################################################
 # Sandbox settings (tables)
@@ -269,8 +274,8 @@
 [shell_environment_policy]
 # inherit: all (default) | core | none
 inherit = "all"
-# Skip default excludes for names containing KEY/SECRET/TOKEN (case-insensitive). Default: true
-ignore_default_excludes = true
+# Skip default excludes for names containing KEY/SECRET/TOKEN (case-insensitive). Default: false
+ignore_default_excludes = false
 # Case-insensitive glob patterns to remove (e.g., "AWS_*", "AZURE_*"). Default: []
 exclude = []
 # Explicit key/value overrides (always win). Default: {}
@@ -281,6 +286,32 @@
 experimental_use_profile = false
 
 ################################################################################
+# Managed network proxy settings
+################################################################################
+
+# Set `default_permissions = "workspace"` before enabling this profile.
+# [permissions.workspace.network]
+# enabled = true
+# proxy_url = "http://127.0.0.1:43128"
+# admin_url = "http://127.0.0.1:43129"
+# enable_socks5 = false
+# socks_url = "http://127.0.0.1:43130"
+# enable_socks5_udp = false
+# allow_upstream_proxy = false
+# dangerously_allow_non_loopback_proxy = false
+# dangerously_allow_non_loopback_admin = false
+# dangerously_allow_all_unix_sockets = false
+# mode = "limited"                           # limited | full
+# allow_local_binding = false
+#
+# [permissions.workspace.network.domains]
+# "api.openai.com" = "allow"
+# "example.com" = "deny"
+#
+# [permissions.workspace.network.unix_sockets]
+# "/var/run/docker.sock" = "allow"
+
+################################################################################
 # History (table)
 ################################################################################
 
@@ -288,7 +319,7 @@
 # save-all (default) | none
 persistence = "save-all"
 # Maximum bytes for history file; oldest entries are trimmed when exceeded. Example: 5242880
-# max_bytes = 0
+# max_bytes = 5242880
 
 ################################################################################
 # UI, Notifications, and Misc (tables)
@@ -302,6 +333,9 @@
 # Notification mechanism for terminal alerts: auto | osc9 | bel. Default: "auto"
 # notification_method = "auto"
 
+# When notifications fire: unfocused (default) | always
+# notification_condition = "unfocused"
+
 # Enables welcome/status/spinner animations. Default: true
 animations = true
 
@@ -316,9 +350,32 @@
 # Set to [] to hide the footer.
 # status_line = ["model", "context-remaining", "git-branch"]
 
+# Ordered list of terminal window/tab title item IDs. When unset, Codex uses:
+# ["spinner", "project"]. Set to [] to clear the title.
+# Available IDs include app-name, project, spinner, status, thread, git-branch, model,
+# and task-progress.
+# terminal_title = ["spinner", "project"]
+
 # Syntax-highlighting theme (kebab-case). Use /theme in the TUI to preview and save.
 # You can also add custom .tmTheme files under $CODEX_HOME/themes.
 # theme = "catppuccin-mocha"
+
+# Custom key bindings. Context-specific bindings override [tui.keymap.global].
+# Use [] to unbind an action.
+# [tui.keymap.global]
+# open_transcript = "ctrl-t"
+# open_external_editor = []
+#
+# [tui.keymap.composer]
+# submit = ["enter", "ctrl-m"]
+
+# Internal tooltip state keyed by model slug. Usually managed by Codex.
+# [tui.model_availability_nux]
+# "gpt-5.4" = 1
+
+# Enable or disable analytics for this machine. When unset, Codex uses its default behavior.
+[analytics]
+enabled = true
 
 # Control whether users can submit feedback from `/feedback`. Default: true
 [feedback]
@@ -331,10 +388,7 @@
 # hide_rate_limit_model_nudge = true
 # hide_gpt5_1_migration_prompt = true
 # "hide_gpt-5.1-codex-max_migration_prompt" = true
-# model_migrations = { "gpt-4.1" = "gpt-5.1" }
-
-# Suppress the warning shown when under-development feature flags are enabled.
-# suppress_unstable_features_warning = true
+# model_migrations = { "gpt-5.3-codex" = "gpt-5.4" }
 
 ################################################################################
 # Centralized Feature Flags (preferred)
@@ -344,22 +398,39 @@
 # Leave this table empty to accept defaults. Set explicit booleans to opt in/out.
 # shell_tool = true
 # apps = false
-# apps_mcp_gateway = false
-# web_search_cached = false
-# web_search_request = false
-# unified_exec = false
-# shell_snapshot = false
-# apply_patch_freeform = false
-# multi_agent = false
-# search_tool = false
+# codex_hooks = false
+# unified_exec = true
+# shell_snapshot = true
+# multi_agent = true
 # personality = true
-# request_rule = true
-# collaboration_modes = true
-# use_linux_sandbox_bwrap = false
-# remote_models = false
-# runtime_metrics = false
-# powershell_utf8 = true
-# child_agents_md = false
+# fast_mode = true
+# enable_request_compression = true
+# skill_mcp_dependency_install = true
+# prevent_idle_sleep = false
+
+################################################################################
+# Memories (table)
+################################################################################
+
+# Enable memories with [features].memories, then tune memory behavior here.
+# [memories]
+# generate_memories = true
+# use_memories = true
+# disable_on_external_context = false # legacy alias: no_memories_if_mcp_or_web_search
+
+################################################################################
+# Lifecycle hooks can be configured here inline or in a sibling hooks.json.
+################################################################################
+
+# [hooks]
+# [[hooks.PreToolUse]]
+# matcher = "^Bash$"
+#
+# [[hooks.PreToolUse.hooks]]
+# type = "command"
+# command = 'python3 "/absolute/path/to/pre_tool_use_policy.py"'
+# timeout = 30
+# statusMessage = "Checking Bash command"
 
 ################################################################################
 # Define MCP servers under this table. Leave empty to disable.
@@ -374,13 +445,17 @@
 # command = "docs-server"                 # required
 # args = ["--port", "4000"]               # optional
 # env = { "API_KEY" = "value" }           # optional key/value pairs copied as-is
-# env_vars = ["ANOTHER_SECRET"]            # optional: forward these from the parent env
+# env_vars = ["ANOTHER_SECRET"]            # optional: forward local parent env vars
+# env_vars = ["LOCAL_TOKEN", { name = "REMOTE_TOKEN", source = "remote" }]
 # cwd = "/path/to/server"                 # optional working directory override
+# experimental_environment = "remote"      # experimental: run stdio via a remote executor
 # startup_timeout_sec = 10.0               # optional; default 10.0 seconds
 # # startup_timeout_ms = 10000              # optional alias for startup timeout (milliseconds)
 # tool_timeout_sec = 60.0                  # optional; default 60.0 seconds
 # enabled_tools = ["search", "summarize"]  # optional allow-list
 # disabled_tools = ["slow-tool"]           # optional deny-list (applied after allow-list)
+# scopes = ["read:docs"]                   # optional OAuth scopes
+# oauth_resource = "https://docs.example.com/" # optional OAuth resource
 
 # --- Example: Streamable HTTP transport ---
 # [mcp_servers.github]
@@ -393,69 +468,70 @@
 # startup_timeout_sec = 10.0                   # optional
 # tool_timeout_sec = 60.0                      # optional
 # enabled_tools = ["list_issues"]             # optional allow-list
+# disabled_tools = ["delete_issue"]           # optional deny-list
+# scopes = ["repo"]                           # optional OAuth scopes
 
 ################################################################################
 # Model Providers
 ################################################################################
 
 # Built-ins include:
-# - openai (Responses API; requires login or OPENAI_API_KEY via auth flow)
-# - oss (Chat Completions API; defaults to http://localhost:11434/v1)
+# - openai
+# - ollama
+# - lmstudio
+# - amazon-bedrock
+# These IDs are reserved. Use a different ID for custom providers.
 
 [model_providers]
+
+# --- Example: built-in Amazon Bedrock provider options ---
+# model_provider = "amazon-bedrock"
+# model = "<bedrock-model-id>"
+# [model_providers.amazon-bedrock.aws]
+# profile = "default"
+# region = "eu-central-1"
 
 # --- Example: OpenAI data residency with explicit base URL or headers ---
 # [model_providers.openaidr]
 # name = "OpenAI Data Residency"
 # base_url = "https://us.api.openai.com/v1"        # example with 'us' domain prefix
-# wire_api = "responses"                           # "responses" | "chat" (default varies)
-# # requires_openai_auth = true                    # built-in OpenAI defaults to true
+# wire_api = "responses"                           # only supported value
+# # requires_openai_auth = true                    # use only for providers backed by OpenAI auth
 # # request_max_retries = 4                        # default 4; max 100
-# # stream_max_retries = 5                         # default 5;  max 100
+# # stream_max_retries = 5                         # default 5; max 100
 # # stream_idle_timeout_ms = 300000                # default 300_000 (5m)
+# # supports_websockets = true                     # optional
 # # experimental_bearer_token = "sk-example"       # optional dev-only direct bearer token
 # # http_headers = { "X-Example" = "value" }
 # # env_http_headers = { "OpenAI-Organization" = "OPENAI_ORGANIZATION", "OpenAI-Project" = "OPENAI_PROJECT" }
 
-# --- Example: Azure (Chat/Responses depending on endpoint) ---
+# --- Example: Azure/OpenAI-compatible provider ---
 # [model_providers.azure]
 # name = "Azure"
 # base_url = "https://YOUR_PROJECT_NAME.openai.azure.com/openai"
-# wire_api = "responses"                          # or "chat" per endpoint
+# wire_api = "responses"
 # query_params = { api-version = "2025-04-01-preview" }
 # env_key = "AZURE_OPENAI_API_KEY"
-# # env_key_instructions = "Set AZURE_OPENAI_API_KEY in your environment"
+# env_key_instructions = "Set AZURE_OPENAI_API_KEY in your environment"
+# # supports_websockets = false
+
+# --- Example: command-backed bearer token auth ---
+# [model_providers.proxy]
+# name = "OpenAI using LLM proxy"
+# base_url = "https://proxy.example.com/v1"
+# wire_api = "responses"
+#
+# [model_providers.proxy.auth]
+# command = "/usr/local/bin/fetch-codex-token"
+# args = ["--audience", "codex"]
+# timeout_ms = 5000
+# refresh_interval_ms = 300000
 
 # --- Example: Local OSS (e.g., Ollama-compatible) ---
-# [model_providers.ollama]
+# [model_providers.local_ollama]
 # name = "Ollama"
 # base_url = "http://localhost:11434/v1"
-# wire_api = "chat"
-
-################################################################################
-# Profiles (named presets)
-################################################################################
-
-[profiles]
-
-# [profiles.default]
-# model = "gpt-5.4"
-# model_provider = "openai"
-# approval_policy = "on-request"
-# sandbox_mode = "read-only"
-# oss_provider = "ollama"
-# model_reasoning_effort = "medium"
-# model_reasoning_summary = "auto"
-# model_verbosity = "medium"
-# personality = "friendly" # or "pragmatic" or "none"
-# chatgpt_base_url = "https://chatgpt.com/backend-api/"
-# model_catalog_json = "./models.json"
-# experimental_compact_prompt_file = "./compact_prompt.txt"
-# include_apply_patch_tool = false
-# experimental_use_unified_exec_tool = false
-# experimental_use_freeform_apply_patch = false
-# tools.web_search = false             # deprecated legacy alias; prefer top-level `web_search`
-# features = { unified_exec = false }
+# wire_api = "responses"
 
 ################################################################################
 # Apps / Connectors
@@ -479,14 +555,57 @@
 # enabled = false
 # approval_mode = "approve"
 
+# Optional tool suggestion allowlist for connectors or plugins Codex can offer to install.
+# [tool_suggest]
+# discoverables = [
+#   { type = "connector", id = "gmail" },
+#   { type = "plugin", id = "figma@openai-curated" },
+# ]
+# disabled_tools = [
+#   { type = "plugin", id = "slack@openai-curated" },
+#   { type = "connector", id = "connector_googlecalendar" },
+# ]
+
+################################################################################
+# Profiles (named presets)
+################################################################################
+
+[profiles]
+
+# [profiles.default]
+# model = "gpt-5.4"
+# model_provider = "openai"
+# approval_policy = "on-request"
+# sandbox_mode = "read-only"
+# service_tier = "flex"
+# oss_provider = "ollama"
+# model_reasoning_effort = "medium"
+# plan_mode_reasoning_effort = "high"
+# model_reasoning_summary = "auto"
+# model_verbosity = "medium"
+# personality = "pragmatic" # or "friendly" or "none"
+# chatgpt_base_url = "https://chatgpt.com/backend-api/"
+# model_catalog_json = "./models.json"
+# model_instructions_file = "/absolute/or/relative/path/to/instructions.txt"
+# experimental_compact_prompt_file = "./compact_prompt.txt"
+# tools_view_image = true
+# features = { unified_exec = false }
+
 ################################################################################
 # Projects (trust levels)
 ################################################################################
 
+[projects]
 # Mark specific worktrees as trusted or untrusted.
-[projects]
 # [projects."/absolute/path/to/project"]
 # trust_level = "trusted"  # or "untrusted"
+
+################################################################################
+# Tools
+################################################################################
+
+[tools]
+# view_image = true
 
 ################################################################################
 # OpenTelemetry (OTEL) - disabled by default
@@ -501,6 +620,8 @@
 exporter = "none"
 # Trace exporter: none (default) | otlp-http | otlp-grpc
 trace_exporter = "none"
+# Metrics exporter: none | statsig | otlp-http | otlp-grpc
+metrics_exporter = "statsig"
 
 # Example OTLP/HTTP exporter configuration
 # [otel.exporter."otlp-http"]
@@ -510,35 +631,21 @@
 # [otel.exporter."otlp-http".headers]
 # "x-otlp-api-key" = "${OTLP_TOKEN}"
 
-# Example OTLP/gRPC exporter configuration
-# [otel.exporter."otlp-grpc"]
-# endpoint = "https://otel.example.com:4317",
-# headers = { "x-otlp-meta" = "abc123" }
-
-# Example OTLP exporter with mutual TLS
-# [otel.exporter."otlp-http"]
-# endpoint = "https://otel.example.com/v1/logs"
-# protocol = "binary"
-
-# [otel.exporter."otlp-http".headers]
-# "x-otlp-api-key" = "${OTLP_TOKEN}"
-
 # [otel.exporter."otlp-http".tls]
 # ca-certificate = "certs/otel-ca.pem"
 # client-certificate = "/etc/codex/certs/client.pem"
 # client-private-key = "/etc/codex/certs/client-key.pem"
-```
-
-################################################################################
-
+
+# Example OTLP/gRPC trace exporter configuration
+# [otel.trace_exporter."otlp-grpc"]
+# endpoint = "https://otel.example.com:4317"
+# headers = { "x-otlp-meta" = "abc123" }
+
+################################################################################
 # Windows
-
 ################################################################################
 
 [windows]
-
-# Native Windows sandbox mode (Windows only). The example below uses the
-
-# recommended elevated mode.
-
-sandbox = "elevated"+# Native Windows sandbox mode (Windows only): unelevated | elevated
+sandbox = "unelevated"
+```
```
#### https://developers.openai.com/codex/enterprise/admin-setup.md

```diff
--- a/https://developers.openai.com/codex/enterprise/admin-setup.md
+++ b/https://developers.openai.com/codex/enterprise/admin-setup.md
@@ -1,57 +1,60 @@
 # Admin Setup
 
+<div class="max-w-1xl mx-auto">
+  <img src="https://developers.openai.com/images/codex/codex_enterprise_admin.png"
+    alt="Codex enterprise admin toggle"
+    class="block w-full mx-auto rounded-lg"
+  />
+</div>
+
+
+
 This guide is for ChatGPT Enterprise admins who want to set up Codex for their workspace.
 
-Use this page as the step-by-step rollout guide. It focuses on setup order and decision points. For detailed policy, configuration, and monitoring details, use the linked pages: [Authentication](https://developers.openai.com/codex/auth), [Agent approvals & security](https://developers.openai.com/codex/agent-approvals-security), [Managed configuration](https://developers.openai.com/codex/enterprise/managed-configuration), and [Governance](https://developers.openai.com/codex/enterprise/governance).
+Use this page as the step-by-step rollout guide. For detailed policy, configuration, and monitoring details, use the linked pages: [Authentication](https://developers.openai.com/codex/auth), [Agent approvals & security](https://developers.openai.com/codex/agent-approvals-security), [Managed configuration](https://developers.openai.com/codex/enterprise/managed-configuration), and [Governance](https://developers.openai.com/codex/enterprise/governance).
 
 ## Enterprise-grade security and privacy
 
 Codex supports ChatGPT Enterprise security features, including:
 
 - No training on enterprise data
-- Zero data retention for the App, CLI, and IDE (code remains in developer environment)
+- Zero data retention for the App, CLI, and IDE (code stays in the developer environment)
 - Residency and retention that follow ChatGPT Enterprise policies
 - Granular user access controls
 - Data encryption at rest (AES-256) and in transit (TLS 1.2+)
+- Audit logging via the ChatGPT Compliance API
 
 For security controls and runtime protections, see [Agent approvals & security](https://developers.openai.com/codex/agent-approvals-security). Refer to [Zero Data Retention (ZDR)](https://platform.openai.com/docs/guides/your-data#zero-data-retention) for more details.
-
-## Local vs. cloud setup
-
-Codex operates in two environments: local and cloud.
-
-1. **Codex local** includes the Codex app, CLI, and IDE extension. The agent runs on the developer's computer in a sandbox.
-2. **Codex cloud** includes hosted Codex features (including Codex cloud, iOS, Code Review, and tasks created by the [Slack integration](https://developers.openai.com/codex/integrations/slack) or [Linear integration](https://developers.openai.com/codex/integrations/linear)). The agent runs remotely in a hosted container with your codebase.
+For a broader enterprise security overview, see the [Codex security white paper](https://trust.openai.com/?itemUid=382f924d-54f3-43a8-a9df-c39e6c959958&source=click).
+
+## Pre-requisites: Determine owners and rollout strategy
+
+During your rollout, team members may support different aspects of integrating Codex into your organization. Ensure you have the following owners:
+
+- **ChatGPT Enterprise workspace owner:** required to configure Codex settings in your workspace.
+- **Security owner:** determines agent permissions settings for Codex.
+- **Analytics owner:** integrates analytics and compliance APIs into your data pipelines.
+
+Decide which Codex surfaces you will use:
+
+- **Codex local:** includes the Codex app, CLI, and IDE extension. The agent runs on the developer's computer in a sandbox.
+- **Codex cloud:** includes hosted Codex features (including Codex cloud, iOS, Code Review, and tasks created by the [Slack integration](https://developers.openai.com/codex/integrations/slack) or [Linear integration](https://developers.openai.com/codex/integrations/linear)). The agent runs remotely in a hosted container with your codebase.
+- **Both:** use local + cloud together.
 
 You can enable local, cloud, or both, and control access with workspace settings and role-based access control (RBAC).
 
-## Step 0: Owners and rollout decision
-
-Ensure you have the following owners:
-
-- Workspace owner with access to ChatGPT Enterprise
-- IT management owner for managed configuration
-- Governance owner for analytics / compliance review
-
-A rollout decision:
-
-- Codex local only (Codex app, CLI, and IDE extension)
-- Codex cloud only (Codex web, GitHub code review)
-- Both local + cloud
-
-Review [authentication](https://developers.openai.com/codex/auth) before rollout:
-
-- Codex local supports ChatGPT sign-in or API keys. Confirm MFA/SSO requirements and any managed login restrictions in authentication
-- Codex cloud requires ChatGPT sign-in
-
-## Step 1: Enable workspace toggles
-
-Turn on only the Codex features you plan to roll out in this phase.
+## Step 1: Enable Codex in your workspace
+
+You configure access to Codex in ChatGPT Enterprise workspace settings.
 
 Go to [Workspace Settings > Settings and Permissions](https://chatgpt.com/admin/settings).
 
 ### Codex local
 
+Codex local is enabled by default for new ChatGPT Enterprise workspaces. If
+  you are not a ChatGPT workspace owner, you can test whether you have access by
+  [installing Codex](https://developers.openai.com/codex/quickstart) and logging in with your work email.
+
 Turn on **Allow members to use Codex Local**.
 
 This enables use of the Codex app, CLI, and IDE extension for allowed users.
@@ -60,7 +63,7 @@
 
 #### Enable device code authentication for Codex CLI
 
-Allow developers to sign in with device codes when using Codex CLI in a non-interactive environment. More details in [authentication](https://developers.openai.com/codex/auth/).
+Allow developers to sign in with a device code when using Codex CLI in a non-interactive environment (for example, a remote development box). More details are in [authentication](https://developers.openai.com/codex/auth/).
 
 <div class="max-w-1xl mx-auto py-1">
   <img src="https://developers.openai.com/images/codex/enterprise/local-toggle-config.png"
@@ -87,12 +90,6 @@
 
 Note that it may take up to 10 minutes for Codex to appear in ChatGPT.
 
-#### Allow members to administer Codex
-
-Allows users to view overall Codex [workspace analytics](https://chatgpt.com/codex/settings/analytics), access [cloud-managed requirements](https://chatgpt.com/codex/settings/managed-configs), and manage Cloud environments (edit and delete).
-
-Codex cloud not required.
-
 #### Enable Codex Slack app to post answers on task completion
 
 Codex posts its full answer back to Slack when the task completes. Otherwise, Codex posts only a link to the task.
@@ -103,7 +100,7 @@
 
 By default, Codex cloud agents have no internet access during runtime to help protect against security and safety risks like prompt injection.
 
-This setting enables users to use an allowlist for common software dependency domains, add more domains and trusted sites, and specify allowed HTTP methods.
+This setting lets users use an allowlist for common software dependency domains, add domains and trusted sites, and specify allowed HTTP methods.
 
 For security implications of internet access and runtime controls, see [Agent approvals & security](https://developers.openai.com/codex/agent-approvals-security).
 
@@ -116,39 +113,131 @@
 
 ## Step 2: Set up custom roles (RBAC)
 
-Use RBAC to control which users or groups can access Codex local and Codex cloud.
+Use RBAC to control granular permissions for access Codex local and Codex cloud.
+
+<div class="max-w-1xl mx-auto">
+  <img src="https://developers.openai.com/images/codex/enterprise/rbac_custom_roles.png"
+    alt="Codex cloud toggle"
+    class="block w-full mx-auto rounded-lg"
+  />
+</div>
 
 ### What RBAC lets you do
 
 Workspace Owners can use RBAC in ChatGPT admin settings to:
 
-- Set a default role for users who are not assigned any custom role
+- Set a default role for users who aren't assigned any custom role
 - Create custom roles with granular permissions
-- Assign one or more custom roles to Groups (including SCIM-synced groups)
+- Assign one or more custom roles to Groups
+- Automatically sync users into Groups via SCIM
 - Manage roles centrally from the Custom Roles tab
 
-Users can inherit multiple roles, and permissions resolve to the maximum allowed across those roles.
-
-### Important behavior to plan for
-
-Users in any custom role group do not use the workspace default permissions.
-
-If you are gradually rolling out Codex, one suggestion is to have a "Codex Users" group and a second "Codex Admin" group that has the "Allow members to administer Codex" toggle enabled.
-
-For RBAC setup details and the full permission model, see the [OpenAI RBAC Help Center article](https://help.openai.com/en/articles/11750701-rbac).
-
-## Step 3: Configure Codex local managed settings
-
-For Codex local, set an admin-approved baseline for local behavior before broader rollout.
-
-### Use managed configuration for two different goals
-
-- **Requirements** (`requirements.toml`): Admin-enforced constraints users cannot override
-- **Managed defaults** (`managed_config.toml`): Starting values applied when Codex launches
-
-### Team Config
+Users can inherit more than one role, and permissions resolve to the most permissive (least restrictive) access across those roles.
+
+### Create a Codex Admin group
+
+Set up a dedicated "Codex Admin" group rather than granting Codex administration to a broad audience.
+
+The **Allow members to administer Codex** toggle grants the Codex Admin role. Codex Admins can:
+
+- View Codex [workspace analytics](https://chatgpt.com/codex/settings/analytics)
+- Open the Codex [Policies page](https://chatgpt.com/codex/settings/policies) to manage cloud-managed `requirements.toml` policies
+- Assign those managed policies to user groups or configure a default fallback policy
+- Manage Codex cloud environments, including editing and deleting environments
+
+Use this role for the small set of admins who own Codex rollout, policy management, and governance. It's not required for general Codex users. You don't need Codex cloud to enable this toggle.
+
+Recommended rollout pattern:
+
+- Create a "Codex Users" group for people who should use Codex
+- Create a separate "Codex Admin" group for the smaller set of people who should manage Codex settings and policies
+- Assign the custom role with **Allow members to administer Codex** enabled only to the "Codex Admin" group
+- Keep membership in the "Codex Admin" group limited to workspace owners or designated platform, IT, and governance operators
+- If you use SCIM, back the "Codex Admin" group with your identity provider so membership changes are auditable and centrally managed
+
+This separation makes it easier to roll out Codex while keeping analytics, environment management, and policy deployment limited to trusted admins. For RBAC setup details and the full permission model, see the [OpenAI RBAC Help Center article](https://help.openai.com/en/articles/11750701-rbac).
+
+## Step 3: Configure Codex local requirements
+
+Codex Admins can deploy admin-enforced `requirements.toml` policies from the Codex [Policies page](https://chatgpt.com/codex/settings/policies).
+
+Use this page when you want to apply different local Codex constraints to different groups without distributing device-level files first. The managed policy uses the same `requirements.toml` format described in [Managed configuration](https://developers.openai.com/codex/enterprise/managed-configuration), so you can define allowed approval policies, sandbox modes, web search behavior, MCP server allowlists, feature pins, and restrictive command rules. To disable Browser Use, the in-app browser, or Computer Use, see [Pin feature flags](https://developers.openai.com/codex/enterprise/managed-configuration#pin-feature-flags).
+
+<div class="max-w-1xl mx-auto py-1">
+  <img src="https://developers.openai.com/images/codex/enterprise/policies_and_configurations_page.png"
+    alt="Codex policies and configurations page"
+    class="block w-full mx-auto rounded-lg"
+  />
+</div>
+
+Recommended setup:
+
+1. Create a baseline policy for most users, then create stricter or more permissive variants only where needed.
+2. Assign each managed policy to a specific user group, and configure a default fallback policy for everyone else.
+3. Order group rules with care. If a user matches more than one group-specific rule, the first matching rule applies.
+4. Treat each policy as a complete profile for that group. Codex doesn't fill missing fields from later matching group rules.
+
+These cloud-managed policies apply across Codex local surfaces when users sign in with ChatGPT, including the Codex app, CLI, and IDE extension.
+
+### Example requirements.toml policies
+
+Use cloud-managed `requirements.toml` policies to enforce the guardrails you want for each group. The snippets below are examples you can adapt, not required settings.
+
+<div class="max-w-1xl mx-auto py-1">
+  <img src="https://developers.openai.com/images/codex/enterprise/example_policy.png"
+    alt="Example managed requirements policy"
+    class="block w-full mx-auto rounded-lg"
+  />
+</div>
+
+Example: limit web search, sandbox mode, and approvals for a standard local rollout:
+
+```toml
+allowed_web_search_modes = ["disabled", "cached"]
+allowed_sandbox_modes = ["workspace-write"]
+allowed_approval_policies = ["on-request"]
+```
+
+Example: disable Browser Use, the in-app browser, and Computer Use:
+
+```toml
+[features]
+browser_use = false
+in_app_browser = false
+computer_use = false
+```
+
+Example: add a restrictive command rule when you want admins to block or gate specific commands:
+
+```toml
+[rules]
+prefix_rules = [
+  { pattern = [{ token = "git" }, { any_of = ["push", "commit"] }], decision = "prompt", justification = "Require review before mutating remote history." },
+]
+```
+
+You can use either example on its own or combine them in a single managed policy for a group. For exact keys, precedence, and more examples, see [Managed configuration](https://developers.openai.com/codex/enterprise/managed-configuration) and [Agent approvals & security](https://developers.openai.com/codex/agent-approvals-security).
+
+### Checking user policies
+
+Use the policy lookup tools at the end of the workflow to confirm which managed policy applies to a user. You can check policy assignment by group or by entering a user email.
+
+<div class="max-w-1xl mx-auto py-1">
+  <img src="https://developers.openai.com/images/codex/enterprise/policy_lookup.png"
+    alt="Policy lookup by group or user email"
+    class="block w-full mx-auto rounded-lg"
+  />
+</div>
+
+If you plan to restrict login method or workspace for local clients, see the admin-managed authentication restrictions in [Authentication](https://developers.openai.com/codex/auth).
+
+## Step 4: Standardize local configuration with Team Config
 
 Teams who want to standardize Codex across an organization can use Team Config to share defaults, rules, and skills without duplicating setup on every local configuration.
+
+You can check Team Config settings into the repository under the `.codex` directory. Codex automatically picks up Team Config settings when a user opens that repository.
+
+Start with Team Config for your highest-traffic repositories so teams get consistent behavior in the places they use Codex most.
 
 | Type                                 | Path          | Use it to                                                                    |
 | ------------------------------------ | ------------- | ---------------------------------------------------------------------------- |
@@ -158,39 +247,29 @@
 
 For locations and precedence, see [Config basics](https://developers.openai.com/codex/config-basic#configuration-precedence).
 
-### Recommended first decisions for local rollout
-
-Define a baseline for your pilot:
-
-- Approval policy posture
-- Sandbox mode posture
-- Web search posture
-- MCP / connectors policy
-- Local logging and telemetry posture
-
-For exact keys, precedence, MDM deployment, and examples, see [Managed configuration](https://developers.openai.com/codex/enterprise/managed-configuration) and [Agent approvals & security](https://developers.openai.com/codex/agent-approvals-security).
-
-If you plan to restrict login method or workspace for local clients, see the admin-managed authentication restrictions in [Authentication](https://developers.openai.com/codex/auth).
-
-## Step 4: Configure Codex cloud usage (if enabled)
-
-This step covers repository and environment setup after the Codex cloud workspace toggle is enabled.
+## Step 5: Configure Codex cloud usage (if enabled)
+
+This step covers repository and environment setup after you enable the Codex cloud workspace toggle.
 
 ### Connect Codex cloud to repositories
 
 1. Navigate to [Codex](https://chatgpt.com/codex) and select **Get started**
 2. Select **Connect to GitHub** to install the ChatGPT GitHub Connector if you haven't already connected GitHub to ChatGPT
-3. Install or authorize the ChatGPT GitHub Connector
+3. Install or connect the ChatGPT GitHub Connector
 4. Choose an installation target for the ChatGPT Connector (typically your main organization)
 5. Allow the repositories you want to connect to Codex
 
+For GitHub Enterprise Managed Users (EMU), an organization owner must install
+  the Codex GitHub App for the organization before users can connect
+  repositories in Codex cloud.
+
 For more, see [Cloud environments](https://developers.openai.com/codex/cloud/environments).
 
 Codex uses short-lived, least-privilege GitHub App installation tokens for each operation and respects the user's existing GitHub repository permissions and branch protection rules.
 
-### Configure IP addresses (as needed)
-
-Configure connector / IP allow lists if required by your network policy with these [egress IP ranges](https://openai.com/chatgpt-agents.json).
+### Configure IP addresses
+
+If your GitHub organization controls the IP addresses that apps use to connect, make sure to include these [egress IP ranges](https://openai.com/chatgpt-agents.json).
 
 These IP ranges can change. Consider checking them automatically and updating your allow list based on the latest values.
 
@@ -198,30 +277,163 @@
 
 To allow Codex to perform code reviews on GitHub, go to [Settings → Code review](https://chatgpt.com/codex/settings/code-review).
 
-Code review can be configured at the repository level. Users can also enable auto review for their PRs and choose when Codex automatically triggers a review. More details on [GitHub](https://developers.openai.com/codex/integrations/github) integration page.
-
-Additional integration docs for [Slack](https://developers.openai.com/codex/integrations/slack), [GitHub](https://developers.openai.com/codex/integrations/github), and [Linear](https://developers.openai.com/codex/integrations/linear).
-
-## Step 5: Set up governance and observability
-
-Codex gives enterprise teams several options for visibility into adoption and impact. Set up governance early so your team can monitor adoption, investigate issues, and support compliance workflows.
+You can configure code review at the repository level. Users can also enable auto review for their PRs and choose when Codex automatically triggers a review. More details are on the [GitHub integration page](https://developers.openai.com/codex/integrations/github).
+
+Use the overview page to confirm your workspace has code review turned on and to see the available review controls.
+
+<div class="max-w-1xl mx-auto py-1">
+  <img src="https://developers.openai.com/images/codex/enterprise/code_review_settings_overview.png"
+    alt="Code review settings overview"
+    class="block w-full mx-auto rounded-lg"
+  />
+</div>
+
+<div class="grid grid-cols-1 gap-4 py-1 md:grid-cols-2">
+  <div class="max-w-1xl mx-auto">
+    <p>
+      Use the auto review settings to decide whether Codex should review pull
+      requests automatically for connected repositories.
+    </p>
+    <img src="https://developers.openai.com/images/codex/enterprise/auto_code_review_settings.png"
+      alt="Automatic code review settings"
+      class="block w-full mx-auto rounded-lg"
+    />
+  </div>
+  <div class="max-w-1xl mx-auto">
+    <p>
+      Use review triggers to control which pull request events should start a
+      Codex review.
+    </p>
+    <img src="https://developers.openai.com/images/codex/enterprise/review_triggers.png"
+      alt="Code review trigger settings"
+      class="block w-full mx-auto rounded-lg"
+    />
+  </div>
+</div>
+
+### Configure Codex security
+
+Codex Security helps engineering and security teams find, confirm, and remediate likely vulnerabilities in connected GitHub repositories.
+
+At a high level, Codex Security:
+
+- scans connected repositories commit by commit
+- ranks likely findings and confirms them when possible
+- shows structured findings with evidence, criticality, and suggested remediation
+- lets teams refine a repository threat model to improve prioritization and review quality
+
+For setup, scan creation, findings review, and threat model guidance, see [Codex Security setup](https://developers.openai.com/codex/security/setup). For a product overview, see [Codex Security](https://developers.openai.com/codex/security).
+
+Integration docs are also available for [Slack](https://developers.openai.com/codex/integrations/slack), [GitHub](https://developers.openai.com/codex/integrations/github), and [Linear](https://developers.openai.com/codex/integrations/linear).
+
+## Step 6: Set up governance and observability
+
+Codex gives enterprise teams options for visibility into adoption and impact. Set up governance early so your team can track adoption, investigate issues, and support compliance workflows.
 
 ### Codex governance typically uses
 
 - Analytics Dashboard for quick, self-serve visibility
-- Analytics API for programmatic reporting and BI integration
+- Analytics API for programmatic reporting and business intelligence integration
 - Compliance API for audit and investigation workflows
 
-### Recommended minimum setup
+### Recommended baseline setup
 
 - Assign an owner for adoption reporting
 - Assign an owner for audit and compliance review
 - Define a review cadence
 - Decide what success looks like
 
-For details and examples, see [Governance](https://developers.openai.com/codex/enterprise/governance).
-
-## Step 6: Confirm and validate setup
+### Analytics API setup steps
+
+To set up the Analytics API key:
+
+1. Sign in to the [OpenAI API Platform Portal](https://platform.openai.com) as an owner or admin, and select the correct organization.
+2. Go to the [API keys page](https://platform.openai.com/settings/organization/api-keys).
+3. Create a new secret key dedicated to Codex Analytics, and give it a descriptive name such as Codex Analytics API.
+4. Select the appropriate project for your organization. If you only have one project, the default project is fine.
+5. Set the key permissions to Read only, since this API only retrieves analytics data.
+6. Copy the key value and store it securely, because you can only view it once.
+7. Email support@openai.com to have that key scoped to `codex.enterprise.analytics.read` only. Wait for OpenAI to confirm your API key has Codex Analytics API access.
+
+<div class="not-prose max-w-md mx-auto py-1">
+  <img src="https://developers.openai.com/images/codex/codex_analytics_key.png"
+    alt="Codex analytics key creation"
+    class="block w-full mx-auto rounded-lg"
+  />
+</div>
+
+To use the Analytics API key:
+
+1. Find your `workspace_id` in the [ChatGPT Admin console](https://chatgpt.com/admin) under Workspace details.
+2. Call the Analytics API at `https://api.chatgpt.com/v1/analytics/codex` using your Platform API key, and include your `workspace_id` in the path.
+3. Choose the endpoint you want to query:
+
+- /workspaces/`{workspace_id}`/usage
+- /workspaces/`{workspace_id}`/code_reviews
+- /workspaces/`{workspace_id}`/code_review_responses
+
+4. Set a reporting date range with `start_time` and `end_time` if needed.
+5. Retrieve the next page of results with `next_page` if the response spans more than one page.
+
+Example curl command to retrieve workspace usage:
+
+```bash
+curl -H "Authorization: Bearer YOUR_PLATFORM_API_KEY" \
+  "https://api.chatgpt.com/v1/analytics/codex/workspaces/WORKSPACE_ID/usage"
+```
+
+For more details on the Analytics API, see [Analytics API](https://developers.openai.com/codex/enterprise/governance#analytics-api).
+
+### Compliance API setup steps
+
+To set up the Compliance API key:
+
+1. Sign in to the [OpenAI API Platform Portal](https://platform.openai.com) as an owner or admin, and select the correct organization.
+2. Go to the [API keys page](https://platform.openai.com/settings/organization/api-keys).
+3. Create a new secret key dedicated to Compliance API and select the appropriate project for your organization. If you only have one project, the default project is fine.
+4. Choose All permissions.
+5. Copy the key value and store it securely, because you can only view it once.
+6. Send an email to support@openai.com with:
+
+- the last 4 digits of the API key
+- the key name
+- the created-by name
+- the scope needed: `read`, `delete`, or both
+
+7. Wait for OpenAI to confirm your API key has Compliance API access.
+
+To use the Compliance API key:
+
+1. Find your `workspace_id` in the [ChatGPT Admin console](https://chatgpt.com/admin) under Workspace details.
+2. Use the Compliance API at `https://api.chatgpt.com/v1/`
+3. Pass your Compliance API key in the Authorization header as a Bearer token.
+4. For Codex-related compliance data, use these endpoints:
+
+- /compliance/workspaces/`{workspace_id}`/logs
+- /compliance/workspaces/`{workspace_id}`/logs/`{log_file_id}`
+- /compliance/workspaces/`{workspace_id}`/codex_tasks
+- /compliance/workspaces/`{workspace_id}`/codex_environments
+
+5. For most Codex compliance integrations, start with the logs endpoint and request Codex event types such as CODEX_LOG or CODEX_SECURITY_LOG.
+6. Use /logs to list available Codex compliance log files, then /logs/`{log_file_id}` to download a specific file.
+
+Example curl command to list compliance log files:
+
+```bash
+curl -L -H "Authorization: Bearer YOUR_COMPLIANCE_API_KEY" \
+  "https://api.chatgpt.com/v1/compliance/workspaces/WORKSPACE_ID/logs?event_type=CODEX_LOG&after=2026-03-01T00:00:00Z"
+```
+
+Example curl command to list Codex tasks:
+
+```bash
+curl -H "Authorization: Bearer YOUR_COMPLIANCE_API_KEY" \
+  "https://api.chatgpt.com/v1/compliance/workspaces/WORKSPACE_ID/codex_tasks"
+```
+
+For more details on the Compliance API, see [Compliance API](https://developers.openai.com/codex/enterprise/governance#compliance-api).
+
+## Step 7: Confirm and verify setup
 
 ### What to verify
 
@@ -229,9 +441,9 @@
 - (If enabled) Users can sign in to Codex cloud (ChatGPT sign-in required)
 - MFA and SSO requirements match your enterprise security policy
 - RBAC and workspace toggles produce the expected access behavior
-- Managed configuration is applied for users
+- Managed configuration applies for users
 - Governance data is visible for admins
 
 For authentication options and enterprise login restrictions, see [Authentication](https://developers.openai.com/codex/auth).
 
-Once your team is confident with setup, you can confidently roll Codex out to additional teams and organizations.+Once your team is confident with setup, you can roll Codex out to more teams and organizations.
```
#### https://developers.openai.com/codex/enterprise/governance.md

```diff
--- a/https://developers.openai.com/codex/enterprise/governance.md
+++ b/https://developers.openai.com/codex/enterprise/governance.md
@@ -15,69 +15,75 @@
 ## Analytics Dashboard
 
 <div class="max-w-1xl mx-auto">
-  <img src="https://developers.openai.com/images/codex/enterprise/analytics.png"
+  <img src="https://developers.openai.com/images/codex/enterprise/analytics-dashboard.png"
     alt="Codex analytics dashboard"
-    class="block w-full mx-auto rounded-lg"
+    class="block w-full mx-auto rounded-lg !border-0"
   />
 </div>
 
-### Dashboards
+### Dashboard views
 
-The [analytics dashboard](https://chatgpt.com/codex/settings/analytics) allows ChatGPT workspace administrators to track feature adoption.
+The [analytics dashboard](https://chatgpt.com/codex/cloud/settings/analytics#usage) allows ChatGPT workspace administrators and analytics viewers to track Codex adoption, usage, and Code Review feedback. Usage data can lag by up to 12 hours.
 
-Codex provides the following dashboards:
+Codex provides date-range controls for daily and weekly views. Key charts include:
 
-- Daily users by product (CLI, IDE, cloud, Code Review)
-- Daily code review users
-- Daily code reviews
-- Code reviews by priority level
-- Daily code reviews by feedback sentiment
-- Daily cloud tasks
-- Daily cloud users
-- Daily VS Code extension users
-- Daily CLI users
+- Active users by product surface, including CLI, IDE extension, cloud, desktop, and Code Review
+- Workspace and personal usage breakdowns, including credit and token usage by product surface
+- Product activity for threads and turns by client
+- User ranking table, with filters for client and sort options such as credits, threads, turns, text tokens, and current streak
+- Code Review activity, including PRs reviewed, issues by priority, comments, replies, reactions, and feedback sentiment
+- Skill invocations and agent identity usage when your workspace has those features
 
 ### Data export
 
 Administrators can also export Codex analytics data in CSV or JSON format. Codex provides the following export options:
 
-- Code review users and reviews (Daily unique users and total reviews completed in Code Review)
-- Code review findings and feedback (Daily counts of comments, reactions, replies, and priority-level findings)
-- cloud users and tasks (daily unique cloud users and tasks completed)
-- CLI and VS Code users (Daily unique users for the Codex CLI and VS Code extension)
-- Sessions and messages per user (Daily session starts and user message counts for each Codex user across surfaces)
+- Workspace usage, including daily active users, threads, turns, and credits by surface
+- Usage per user, including daily threads, turns, and credits across surfaces, with optional email addresses when allowed
+- Code Review details, including daily comments, reactions, replies, and priority-level findings
 
 ## Analytics API
 
-Use the [Analytics API](https://chatgpt.com/codex/settings/apireference) when you want to automate reporting, build internal dashboards, or join Codex metrics with your existing engineering data.
+Use the [Analytics API](https://chatgpt.com/codex/cloud/settings/apireference) when you want to automate reporting, build internal dashboards, or join Codex metrics with your existing engineering data.
 
 ### What it measures
 
-The Analytics API provides daily, time-series metrics for a workspace, with optional per-user breakdowns and per-client usage.
+The enterprise Analytics API returns daily or weekly UTC buckets for a workspace. It supports workspace-level and per-user usage, per-client breakdowns, Code Review throughput, Code Review comment priority, and user engagement with Code Review comments.
 
 ### Endpoints
 
-#### Daily usage and adoption
+The base URL is `https://api.chatgpt.com/v1/analytics/codex`. All endpoints return paginated `page` objects with `has_more` and `next_page`.
 
-- Daily totals for threads, turns, and credits
-- Breakdown by client surface
-- Optional per-user reporting for adoption and power-user analysis
+Use `start_time` for the inclusive Unix timestamp at the beginning of the reporting window, `end_time` for the exclusive Unix timestamp at the end of the reporting window, `group_by` for `day` or `week` buckets, `limit` for page size, and `page` to continue from a previous response. Requests can look back up to 90 days.
+
+#### Usage
+
+`GET /workspaces/{workspace_id}/usage`
+
+- Returns totals for threads, turns, credits, and per-client usage in daily or weekly buckets.
+- Omit `group` to return per-user rows.
+- Set `group=workspace` to return workspace-wide rows.
+- Includes text input, cached input, and output token fields.
 
 #### Code review activity
 
-- Pull request reviews completed by Codex
-- Total comments generated by Codex
-- Severity breakdown of comments
+`GET /workspaces/{workspace_id}/code_reviews`
+
+- Returns pull request reviews completed by Codex.
+- Returns total comments generated by Codex.
+- Breaks comments down by P0, P1, and P2 priority.
 
 #### User engagement with code review
 
-- Replies to Codex comments
-- Reactions, including upvotes and downvotes
-- Engagement breakdowns for how teams respond to Codex feedback
+`GET /workspaces/{workspace_id}/code_review_responses`
+
+- Returns replies and reactions to Codex comments.
+- Breaks reactions down into positive, negative, and other reactions.
+- Counts comments that received reactions, replies, or either form of engagement.
 
 ### How it works
 
-Analytics is daily and time-windowed. Results are time-ordered and returned in pages with cursor-based pagination. You can query by workspace and optionally group by user or aggregate at the workspace level.
+Analytics uses time windows and supports day or week grouping. Results are time-ordered and returned in pages with cursor-based pagination. Use an API key scoped to `codex.enterprise.analytics.read`.
 
 ### Common use cases
 

```
#### https://developers.openai.com/codex/enterprise/managed-configuration.md

```diff
--- a/https://developers.openai.com/codex/enterprise/managed-configuration.md
+++ b/https://developers.openai.com/codex/enterprise/managed-configuration.md
@@ -7,21 +7,21 @@
 
 ## Admin-enforced requirements (requirements.toml)
 
-Requirements constrain security-sensitive settings (approval policy, sandbox mode, web search mode, and optionally which MCP servers can be enabled). When resolving configuration (for example from `config.toml`, profiles, or CLI config overrides), if a value conflicts with an enforced requirement, Codex falls back to a requirements-compatible value and notifies the user. If an `mcp_servers` allowlist is configured, Codex enables an MCP server only when both its name and identity match an approved entry; otherwise, Codex disables it.
-
-Requirements can also be used to constrain [feature flags](https://developers.openai.com/codex/config-basic/#feature-flags) via the `[features]` table in `requirements.toml`. Note features are generally not security-sensitive, but enterprises have the option of pinning values, if desired. Omitted keys remain unconstrained.
+Requirements constrain security-sensitive settings (approval policy, approvals reviewer, automatic review policy, sandbox mode, web search mode, managed hooks, and optionally which MCP servers users can enable). When resolving configuration (for example from `config.toml`, profiles, or CLI config overrides), if a value conflicts with an enforced rule, Codex falls back to a compatible value and notifies the user. If you configure an `mcp_servers` allowlist, Codex enables an MCP server only when both its name and identity match an approved entry; otherwise, Codex disables it.
+
+Requirements can also constrain [feature flags](https://developers.openai.com/codex/config-basic/#feature-flags) via the `[features]` table in `requirements.toml`. Note that features aren't always security-sensitive, but enterprises can pin values if desired. Omitted keys remain unconstrained.
 
 For the exact key list, see the [`requirements.toml` section in Configuration Reference](https://developers.openai.com/codex/config-reference#requirementstoml).
 
 ### Locations and precedence
 
-Requirements layers are applied in this order (earlier wins per field):
+Codex applies requirements layers in this order (earlier wins per field):
 
 1. Cloud-managed requirements (ChatGPT Business or Enterprise)
 2. macOS managed preferences (MDM) via `com.openai.codex:requirements_toml_base64`
-3. System `requirements.toml` (`/etc/codex/requirements.toml` on Unix systems, including Linux/macOS)
-
-Across layers, requirements are merged per field: if an earlier layer sets a field (including an empty list), later layers do not override that field, but lower layers can still fill fields that remain unset.
+3. System `requirements.toml` (`/etc/codex/requirements.toml` on Unix systems, including Linux/macOS, or `%ProgramData%\OpenAI\Codex\requirements.toml` on Windows)
+
+Across layers, Codex merges requirements per field: if an earlier layer sets a field (including an empty list), later layers don't override that field, but lower layers can still fill fields that remain unset.
 
 For backwards compatibility, Codex also interprets legacy `managed_config.toml` fields `approval_policy` and `sandbox_mode` as requirements (allowing only that single value).
 
@@ -53,15 +53,15 @@
 
 Admins can configure different managed requirements for different user groups, and also set a default fallback requirements policy.
 
-If a user matches multiple group-specific rules, the first matching rule applies. Codex does not fill unset requirement fields from later matching group rules.
-
-For example, if the first matching group rule sets only `allowed_sandbox_modes = ["read-only"]` and a later matching group rule sets `allowed_approval_policies = ["on-request"]`, Codex applies only the first matching group rule and does not fill `allowed_approval_policies` from the later rule.
+If a user matches more than one group-specific rule, the first matching rule applies. Codex doesn't fill unset fields from later matching group rules.
+
+For example, if the first matching group rule sets only `allowed_sandbox_modes = ["read-only"]` and a later matching group rule sets `allowed_approval_policies = ["on-request"]`, Codex applies only the first matching group rule and doesn't fill `allowed_approval_policies` from the later rule.
 
 #### How Codex applies cloud-managed requirements locally
 
-When a user starts Codex and signs in with ChatGPT on a Business or Enterprise plan, Codex applies managed requirements on a best-effort basis. Codex first checks for a valid, unexpired local managed requirements cache entry and uses it if available. If the cache is missing, expired, invalid, or does not match the current auth identity, Codex attempts to fetch managed requirements from the service (with retries) and writes a new signed cache entry on success. If no valid cached entry is available and the fetch fails or times out, Codex continues without the managed requirements layer.
-
-After cache resolution, managed requirements are enforced as part of the normal requirements layering described above.
+When a user starts Codex and signs in with ChatGPT on a Business or Enterprise plan, Codex applies managed requirements on a best-effort basis. Codex first checks for a valid, unexpired local managed requirements cache entry and uses it if available. If the cache is missing, expired, corrupted, or doesn't match the current auth identity, Codex attempts to fetch managed requirements from the service (with retries) and writes a new signed cache entry on success. If no valid cached entry is available and the fetch fails or times out, Codex continues without the managed requirements layer.
+
+After cache resolution, Codex enforces managed requirements as part of the normal requirements layering described above.
 
 ### Example requirements.toml
 
@@ -72,24 +72,146 @@
 allowed_sandbox_modes = ["read-only", "workspace-write"]
 ```
 
+### Override sandbox requirements by host
+
+Use `[[remote_sandbox_config]]` when one managed policy should apply different
+sandbox requirements on different hosts. For example, you can keep a stricter
+default for laptops while allowing workspace writes on matching devboxes or CI
+runners. Host-specific entries currently override `allowed_sandbox_modes` only:
+
+```toml
+allowed_sandbox_modes = ["read-only"]
+
+[[remote_sandbox_config]]
+hostname_patterns = ["*.devbox.example.com", "runner-??.ci.example.com"]
+allowed_sandbox_modes = ["read-only", "workspace-write"]
+```
+
+Codex compares each `hostname_patterns` entry against the best-effort resolved
+host name. It prefers the fully qualified domain name when available and falls
+back to the local host name. Matching is case-insensitive; `*` matches any
+sequence of characters, and `?` matches one character.
+
+The first matching `[[remote_sandbox_config]]` entry wins within the same
+requirements source. If no entry matches, Codex keeps the top-level
+`allowed_sandbox_modes`. Hostname matching is for policy selection only; don't
+treat it as authenticated device proof.
+
 You can also constrain web search mode:
 
 ```toml
 allowed_web_search_modes = ["cached"] # "disabled" remains implicitly allowed
 ```
 
-`allowed_web_search_modes = []` effectively allows only `"disabled"`.
+`allowed_web_search_modes = []` allows only `"disabled"`.
 For example, `allowed_web_search_modes = ["cached"]` prevents live web search even in `danger-full-access` sessions.
 
-You can also pin [feature flags](https://developers.openai.com/codex/config-basic/#feature-flags):
+### Pin feature flags
+
+You can also pin [feature flags](https://developers.openai.com/codex/config-basic/#feature-flags) for users
+receiving a managed `requirements.toml`:
 
 ```toml
 [features]
 personality = true
 unified_exec = false
-```
-
-Use the canonical feature keys from `config.toml`'s `[features]` table. Codex normalizes the effective feature set to satisfy these pins and rejects conflicting writes to `config.toml` or profile-scoped feature settings.
+
+# Disable specific Codex feature surfaces when needed.
+browser_use = false
+in_app_browser = false
+computer_use = false
+```
+
+Use the canonical feature keys from `config.toml`'s `[features]` table. Codex normalizes the resulting feature set to meet these pins and rejects conflicting writes to `config.toml` or profile-scoped feature settings.
+
+<a id="disable-codex-feature-surfaces"></a>
+
+- `in_app_browser = false` disables the in-app browser pane.
+- `browser_use = false` disables Browser Use and Browser Agent availability.
+- `computer_use = false` disables Computer Use availability and related
+  install or enablement flows.
+
+If omitted, these features are allowed by policy, subject to normal client,
+platform, and rollout availability.
+
+### Configure automatic review policy
+
+Use `allowed_approvals_reviewers` to require or allow automatic review. Set it
+to `["auto_review"]` to require automatic review, or include `"user"` when users
+can choose manual approval.
+
+Set `guardian_policy_config` to replace the tenant-specific section of the
+automatic review policy. Codex still uses the built-in reviewer template and
+output contract. Managed `guardian_policy_config` takes precedence over local
+`[auto_review].policy`.
+
+```toml
+allowed_approval_policies = ["on-request"]
+allowed_approvals_reviewers = ["auto_review"]
+
+guardian_policy_config = """
+## Environment Profile
+- Trusted internal destinations include github.com/my-org, artifacts.example.com,
+  and internal CI systems.
+
+## Tenant Risk Taxonomy and Allow/Deny Rules
+- Treat uploads to unapproved third-party file-sharing services as high risk.
+- Deny actions that expose credentials or private source code to untrusted
+  destinations.
+"""
+```
+
+### Enforce deny-read requirements
+
+Admins can deny reads for exact paths or glob patterns with
+`[permissions.filesystem]`. Users can't weaken these requirements with local
+configuration.
+
+```toml
+[permissions.filesystem]
+deny_read = [
+  "/Users/alice/.ssh",
+  "./private/**/*.txt",
+]
+```
+
+When deny-read requirements are present, Codex constrains local sandbox mode to
+`read-only` or `workspace-write` so Codex can enforce them. On native
+Windows, managed `deny_read` applies to direct file tools; shell subprocess
+reads don't use this sandbox rule.
+
+### Enforce managed hooks from requirements
+
+Admins can also define managed lifecycle hooks directly in `requirements.toml`.
+Use `[hooks]` for the hook configuration itself, and point `managed_dir` at the
+directory where your MDM or endpoint-management tooling installs the referenced
+scripts.
+
+```toml
+[features]
+codex_hooks = true
+
+[hooks]
+managed_dir = "/enterprise/hooks"
+windows_managed_dir = 'C:\enterprise\hooks'
+
+[[hooks.PreToolUse]]
+matcher = "^Bash$"
+
+[[hooks.PreToolUse.hooks]]
+type = "command"
+command = "python3 /enterprise/hooks/pre_tool_use_policy.py"
+timeout = 30
+statusMessage = "Checking managed Bash command"
+```
+
+Notes:
+
+- Codex enforces the hook configuration from `requirements.toml`, but it does
+  not distribute the scripts in `managed_dir`.
+- Deliver those scripts separately with your MDM or device-management solution.
+- Managed hook commands should reference absolute script paths under the
+  configured managed directory.
 
 ### Enforce command rules from requirements
 

```
#### https://developers.openai.com/codex/github-action.md

```diff
--- a/https://developers.openai.com/codex/github-action.md
+++ b/https://developers.openai.com/codex/github-action.md
@@ -84,7 +84,7 @@
 Fine-tune how Codex runs by setting the action inputs that map to `codex exec` options:
 
 - `prompt` or `prompt-file` (choose one): Inline instructions or a repository path to Markdown or text with your task. Consider storing prompts in `.github/codex/prompts/`.
-- `codex-args`: Extra CLI flags. Provide a JSON array (for example `["--full-auto"]`) or a shell string (`--full-auto --sandbox danger-full-access`) to allow edits, streaming, or MCP configuration.
+- `codex-args`: Extra CLI flags. Provide a JSON array (for example `["--json"]`) or a shell string (`--sandbox workspace-write --json`) to allow edits, streaming, or MCP configuration.
 - `model` and `effort`: Pick the Codex agent configuration you want; leave empty for defaults.
 - `sandbox`: Match the sandbox mode (`workspace-write`, `read-only`, `danger-full-access`) to the permissions Codex needs during the run.
 - `output-file`: Save the final Codex message to disk so later steps can upload or diff it.

```
#### https://developers.openai.com/codex/guides/agents-sdk.md

```diff
--- a/https://developers.openai.com/codex/guides/agents-sdk.md
+++ b/https://developers.openai.com/codex/guides/agents-sdk.md
@@ -2,7 +2,7 @@
 
 # Running Codex as an MCP server
 
-You can run Codex as an MCP server and connect it from other MCP clients (for example, an agent built with the [OpenAI Agents SDK](https://openai.github.io/openai-agents-js/guides/mcp/)).
+You can run Codex as an MCP server and connect it from other MCP clients (for example, an agent built with the [OpenAI Agents SDK MCP integration](https://developers.openai.com/api/docs/guides/agents/integrations-observability#mcp)).
 
 To start Codex as an MCP server, you can use the following command:
 

```
#### https://developers.openai.com/codex/ide.md

```diff
--- a/https://developers.openai.com/codex/ide.md
+++ b/https://developers.openai.com/codex/ide.md
@@ -23,11 +23,13 @@
 - [Download for Visual Studio Code Insiders](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt)
 - [Download for JetBrains IDEs](#jetbrains-ide-integration)
 
-The Codex VS Code extension is available on macOS and Linux. Windows support
-  is experimental. For the best Windows experience, use Codex in a WSL workspace
-  and follow our <a href="/codex/windows">Windows setup guide</a>.
+Codex IDE integrations for VS Code-compatible editors and JetBrains IDEs are
+  available on macOS, Windows, and Linux. On Windows, run Codex natively with
+  the Windows sandbox, or use WSL2 when you need a Linux-native environment. For
+  setup details, see the <a href="/codex/windows">Windows setup guide</a>.
 
-After you install it, you'll find the extension in your left sidebar next to your other extensions.
+After you install it, you'll find Codex in your editor sidebar.
+In VS Code, Codex opens in the right sidebar by default.
 If you're using VS Code, restart the editor if you don't see Codex right away.
 
 If you're using Cursor, the activity bar displays horizontally by default. Collapsed items can hide Codex, so you can pin it and reorganize the order of the extensions.
@@ -51,9 +53,11 @@
 
 ### Move Codex to the right sidebar <a id="right-sidebar"></a>
 
-In VS Code, you can drag the Codex icon to the right of your editor to move it to the right sidebar.
+In VS Code, Codex appears in the right sidebar automatically.
+If you prefer it in the primary (left) sidebar, drag the Codex icon back to the left activity bar.
 
-In some IDEs, like Cursor, you may need to temporarily change the activity bar orientation first:
+In VS Code forks like Cursor, you may need to move Codex to the right sidebar manually.
+To do that, you may need to temporarily change the activity bar orientation first:
 
 1. Open your editor settings and search for `activity bar` (in Workbench settings).
 2. Change the orientation to `vertical`.
@@ -64,6 +68,7 @@
 Now drag the Codex icon to the right sidebar (for example, next to your Cursor chat). Codex appears as another tab in the sidebar.
 
 After you move it, reset the activity bar orientation to `horizontal` to restore the default behavior.
+If you change your mind later, you can drag Codex back to the primary (left) sidebar at any time.
 
 ### Sign in
 
@@ -80,6 +85,7 @@
 To see all available commands and bind them as keyboard shortcuts, select the settings icon in the Codex chat and select **Keyboard shortcuts**.
 You can also refer to the [Codex IDE extension commands](https://developers.openai.com/codex/ide/commands) page.
 For a list of supported slash commands, see [Codex IDE extension slash commands](https://developers.openai.com/codex/ide/slash-commands).
+If you're new to Codex, read the [best practices guide](https://developers.openai.com/codex/learn/best-practices).
 
 ---
 
@@ -105,6 +111,14 @@
 ### Adjust reasoning effort
 
 Choose `low`, `medium`, or `high` to trade off speed and depth based on the task.
+
+  </BentoContent>
+
+  <BentoContent href="/codex/ide/features#image-generation">
+
+### Image generation
+
+Generate or edit images without leaving your editor, and use reference assets when you need iteration.
 
   </BentoContent>
 

```
#### https://developers.openai.com/codex/ide/features.md

```diff
--- a/https://developers.openai.com/codex/ide/features.md
+++ b/https://developers.openai.com/codex/ide/features.md
@@ -25,7 +25,7 @@
 
 ## Adjust reasoning effort
 
-You can adjust reasoning effort to control how long Codex thinks before responding. Higher effort can help on complex tasks, but responses take longer. Higher effort also uses more tokens and can consume your rate limits faster (especially with GPT-5-Codex).
+You can adjust reasoning effort to control how long Codex thinks before responding. Higher effort can help on complex tasks, but responses take longer. Higher effort also uses more tokens and can consume your rate limits faster, especially with higher-capability models.
 
 Use the same model switcher shown above, and choose `low`, `medium`, or `high` for each model. Start with `medium`, and only switch to `high` when you need more depth.
 
@@ -88,6 +88,16 @@
 
 Hold down `Shift` while dropping an image. VS Code otherwise prevents extensions from accepting a drop.
 
+## Image generation
+
+Ask Codex to generate or edit images without leaving your editor. This is useful for UI assets, layouts, illustrations, sprite sheets, and quick placeholders while you work. Add a reference image to the prompt when you want Codex to transform or extend an existing asset.
+
+You can ask in natural language or explicitly invoke the image generation skill by including `$imagegen` in your prompt.
+
+Built-in image generation uses `gpt-image-2`, counts toward your general Codex usage limits, and uses included limits 3-5x faster on average than similar turns without image generation, depending on image quality and size. For details, see [Pricing](https://developers.openai.com/codex/pricing#image-generation-usage-limits). For prompting tips and model details, see the [image generation guide](https://developers.openai.com/api/docs/guides/image-generation).
+
+For larger batches of image generation, set `OPENAI_API_KEY` in your environment variables and ask Codex to generate images through the API so API pricing applies instead.
+
 ## See also
 
 - [Codex IDE extension settings](https://developers.openai.com/codex/ide/settings)
```
#### https://developers.openai.com/codex/ide/settings.md

```diff
--- a/https://developers.openai.com/codex/ide/settings.md
+++ b/https://developers.openai.com/codex/ide/settings.md
@@ -12,12 +12,16 @@
 
 The Codex IDE extension uses the Codex CLI. Configure some behavior, such as the default model, approvals, and sandbox settings, in the shared `~/.codex/config.toml` file instead of in editor settings. See [Config basics](https://developers.openai.com/codex/config-basic).
 
+The extension also honors VS Code's built-in chat font settings for Codex conversation surfaces.
+
 ## Settings reference
 
-| Setting                                      | Description                                                                                                                                                                                                                                                          |
-| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
-| `chatgpt.cliExecutable`                      | Development only: Path to the Codex CLI executable. You don't need to set this unless you're actively developing the Codex CLI. If you set this manually, parts of the extension might not work as expected.                                                         |
-| `chatgpt.commentCodeLensEnabled`             | Show CodeLens above to-do comments so you can complete them with Codex.                                                                                                                                                                                              |
-| `chatgpt.localeOverride`                     | Preferred language for the Codex UI. Leave empty to detect automatically.                                                                                                                                                                                            |
-| `chatgpt.openOnStartup`                      | Focus the Codex sidebar when the extension finishes starting.                                                                                                                                                                                                        |
-| `chatgpt.runCodexInWindowsSubsystemForLinux` | Windows only: Run Codex in WSL when Windows Subsystem for Linux (WSL) is available. Recommended for improved sandbox security and better performance. Codex agent mode on Windows currently requires WSL. Changing this setting reloads VS Code to apply the change. |+| Setting                                      | Description                                                                                                                                                                                                                                                                                                           |
+| -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
+| `chat.fontSize`                              | Controls chat text in the Codex sidebar, including conversation content and the composer.                                                                                                                                                                                                                             |
+| `chat.editor.fontSize`                       | Controls code-rendered content in Codex conversations, including code snippets and diffs.                                                                                                                                                                                                                             |
+| `chatgpt.cliExecutable`                      | Development only: Path to the Codex CLI executable. You don't need to set this unless you're actively developing the Codex CLI. If you set this manually, parts of the extension might not work as expected.                                                                                                          |
+| `chatgpt.commentCodeLensEnabled`             | Show CodeLens above to-do comments so you can complete them with Codex.                                                                                                                                                                                                                                               |
+| `chatgpt.localeOverride`                     | Preferred language for the Codex UI. Leave empty to detect automatically.                                                                                                                                                                                                                                             |
+| `chatgpt.openOnStartup`                      | Focus the Codex sidebar when the extension finishes starting.                                                                                                                                                                                                                                                         |
+| `chatgpt.runCodexInWindowsSubsystemForLinux` | Windows only: Run Codex in WSL when Windows Subsystem for Linux (WSL) is available. Use this when your repositories and tooling live in WSL2 or when you need Linux-native tooling. Otherwise, Codex can run natively on Windows with the Windows sandbox. Changing this setting reloads VS Code to apply the change. |
```
#### https://developers.openai.com/codex/integrations/github.md

```diff
--- a/https://developers.openai.com/codex/integrations/github.md
+++ b/https://developers.openai.com/codex/integrations/github.md
@@ -1,6 +1,8 @@
-# Use Codex in GitHub
+# Codex code review in GitHub
 
-Use Codex to review pull requests without leaving GitHub. Add a pull request comment with `@codex review`, and Codex replies with a standard GitHub code review.
+Use Codex code review to get another high-signal review pass on GitHub pull
+requests. Codex reviews the pull request diff, follows your repository guidance,
+and posts a standard GitHub code review focused on serious issues.
 
 <YouTubeEmbed
   title="Codex code review walkthrough"
@@ -9,10 +11,19 @@
 />
 <br />
 
-## Set up code review
+## Before you start
+
+Make sure you have:
+
+- [Codex cloud](https://developers.openai.com/codex/cloud) set up for the repository you want to review.
+- Access to [Codex code review settings](https://chatgpt.com/codex/settings/code-review).
+- An `AGENTS.md` file if you want Codex to follow repository-specific review guidance.
+
+## Set up Codex code review
 
 1. Set up [Codex cloud](https://developers.openai.com/codex/cloud).
-2. Go to [Codex settings](https://chatgpt.com/codex/settings/code-review) and turn on **Code review** for your repository.
+2. Go to [Codex settings](https://chatgpt.com/codex/settings/code-review).
+3. Turn on **Code review** for your repository.
 
 <div class="not-prose max-w-3xl mr-auto">
   <img src="https://developers.openai.com/images/codex/code-review/code-review-settings.png"
@@ -22,7 +33,7 @@
 </div>
 <br />
 
-## Request a review
+## Request a Codex review
 
 1. In a pull request comment, mention `@codex review`.
 2. Wait for Codex to react (👀) and post a review.
@@ -35,7 +46,9 @@
 </div>
 <br />
 
-Codex posts a review on the pull request, just like a teammate would.
+Codex posts a review on the pull request, just like a teammate would. In
+GitHub, Codex flags only P0 and P1 issues so review comments stay focused on
+high-priority risks.
 
 <div class="not-prose max-w-3xl mr-auto">
   <img src="https://developers.openai.com/images/codex/code-review/review-example.png"
@@ -47,7 +60,10 @@
 
 ## Enable automatic reviews
 
-If you want Codex to review every pull request automatically, turn on **Automatic reviews** in [Codex settings](https://chatgpt.com/codex/settings/code-review). Codex will post a review whenever a new PR is opened for review, without needing an `@codex review` comment.
+If you want Codex to review every pull request automatically, turn on
+**Automatic reviews** in [Codex settings](https://chatgpt.com/codex/settings/code-review).
+Codex will post a review whenever someone opens a new PR for review, without
+needing an `@codex review` comment.
 
 ## Customize what Codex reviews
 
@@ -64,11 +80,24 @@
 
 Codex applies guidance from the closest `AGENTS.md` to each changed file. You can place more specific instructions deeper in the tree when particular packages need extra scrutiny.
 
-For a one-off focus, add it to your pull request comment, for example:
+For a one-off focus, add it to your pull request comment:
 
 `@codex review for security regressions`
 
-In GitHub, Codex flags only P0 and P1 issues. If you want Codex to flag typos in documentation, add guidance in `AGENTS.md` (for example, “Treat typos in docs as P1.”).
+If you want Codex to flag typos in documentation, add guidance in `AGENTS.md`
+(for example, “Treat typos in docs as P1.”).
+
+## Act on review findings
+
+After Codex posts a review, you can ask it to fix issues in the same pull
+request by leaving another comment:
+
+```md
+@codex fix the P1 issue
+```
+
+Codex starts a cloud task with the pull request as context and can push a fix
+back to the branch when it has permission to do so.
 
 ## Give Codex other tasks
 
@@ -76,4 +105,14 @@
 
 ```md
 @codex fix the CI failures
-```+```
+
+## Troubleshoot code review
+
+If Codex doesn't react or post a review:
+
+- Confirm you turned on **Code review** for the repository in [Codex settings](https://chatgpt.com/codex/settings/code-review).
+- Confirm the pull request belongs to a repository with [Codex cloud](https://developers.openai.com/codex/cloud) set up.
+- Use the exact trigger `@codex review` in a pull request comment.
+- For automatic reviews, check that you turned on **Automatic reviews** and that
+  the pull request event matches your review trigger settings.
```
#### https://developers.openai.com/codex/mcp.md

```diff
--- a/https://developers.openai.com/codex/mcp.md
+++ b/https://developers.openai.com/codex/mcp.md
@@ -58,6 +58,18 @@
 - `env` (optional): Environment variables to set for the server.
 - `env_vars` (optional): Environment variables to allow and forward.
 - `cwd` (optional): Working directory to start the server from.
+- `experimental_environment` (optional): Set to `remote` to start the stdio
+  server through a remote executor environment when one is available.
+
+`env_vars` can contain plain variable names or objects with a source:
+
+```toml
+env_vars = ["LOCAL_TOKEN", { name = "REMOTE_TOKEN", source = "remote" }]
+```
+
+String entries and `source = "local"` read from Codex's local environment.
+`source = "remote"` reads from the remote executor environment and requires
+remote MCP stdio.
 
 #### Streamable HTTP servers
 
@@ -77,7 +89,11 @@
 
 If your OAuth provider requires a fixed callback port, set the top-level `mcp_oauth_callback_port` in `config.toml`. If unset, Codex binds to an ephemeral port.
 
-If your MCP OAuth flow must use a specific callback URL (for example, a remote devbox ingress URL or a custom callback path), set `mcp_oauth_callback_url`. Codex uses this value as the OAuth `redirect_uri` while still using `mcp_oauth_callback_port` for the callback listener port. Local callback URLs (for example `localhost`) bind on loopback; non-local callback URLs bind on `0.0.0.0` so the callback can reach the host.
+If your MCP OAuth flow must use a specific callback URL (for example, a remote Devbox ingress URL or a custom callback path), set `mcp_oauth_callback_url`. Codex uses this value as the OAuth `redirect_uri` while still using `mcp_oauth_callback_port` for the callback listener port. Local callback URLs (for example `localhost`) bind on the local interface; non-local callback URLs bind on `0.0.0.0` so the callback can reach the host.
+
+If the MCP server advertises `scopes_supported`, Codex prefers those
+server-advertised scopes during OAuth login. Otherwise, Codex falls back to the
+scopes configured in `config.toml`.
 
 #### config.toml examples
 
@@ -85,6 +101,7 @@
 [mcp_servers.context7]
 command = "npx"
 args = ["-y", "@upstash/context7-mcp"]
+env_vars = ["LOCAL_TOKEN"]
 
 [mcp_servers.context7.env]
 MY_ENV_VAR = "MY_ENV_VALUE"
@@ -117,7 +134,7 @@
 
 The list of MCP servers keeps growing. Here are a few common ones:
 
-- [OpenAI Docs MCP](https://developers.openai.com/resources/docs-mcp): Search and read OpenAI developer docs.
+- [OpenAI Docs MCP](https://developers.openai.com/learn/docs-mcp): Search and read OpenAI developer docs.
 - [Context7](https://github.com/upstash/context7): Connect to up-to-date developer documentation.
 - Figma [Local](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/) and [Remote](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/): Access your Figma designs.
 - [Playwright](https://www.npmjs.com/package/@playwright/mcp): Control and inspect a browser using Playwright.

```
#### https://developers.openai.com/codex/models.md

```diff
--- a/https://developers.openai.com/codex/models.md
+++ b/https://developers.openai.com/codex/models.md
@@ -5,10 +5,10 @@
 <div class="not-prose grid gap-6 md:grid-cols-2 xl:grid-cols-3">
   <ModelDetails
     client:load
-    name="gpt-5.4"
-    slug="gpt-5.4"
-    wallpaperUrl="/images/api/models/gpt-5.4.jpg"
-    description="Flagship frontier model for professional work that brings the industry-leading coding capabilities of GPT-5.3-Codex together with stronger reasoning, tool use, and agentic workflows."
+    name="gpt-5.5"
+    slug="gpt-5.5"
+    wallpaperUrl="/images/api/models/gpt-5.5.jpg"
+    description="OpenAI's newest frontier model for complex coding, computer use, knowledge work, and research workflows in Codex."
     data={{
       features: [
         {
@@ -37,10 +37,86 @@
           value: false,
         },
         { title: "ChatGPT Credits", value: true },
-        { title: "API Access", value: true },
+        { title: "API Access", value: false },
       ],
     }}
   />
+
+<ModelDetails
+  client:load
+  name="gpt-5.4"
+  slug="gpt-5.4"
+  wallpaperUrl="/images/api/models/gpt-5.4.jpg"
+  description="Flagship frontier model for professional work that brings the industry-leading coding capabilities of GPT-5.3-Codex together with stronger reasoning, tool use, and agentic workflows."
+  data={{
+    features: [
+      {
+        title: "Capability",
+        value: "",
+        icons: [
+          "openai.SparklesFilled",
+          "openai.SparklesFilled",
+          "openai.SparklesFilled",
+          "openai.SparklesFilled",
+          "openai.SparklesFilled",
+        ],
+      },
+      {
+        title: "Speed",
+        value: "",
+        icons: ["openai.Flash", "openai.Flash", "openai.Flash"],
+      },
+      {
+        title: "Codex CLI & SDK",
+        value: true,
+      },
+      { title: "Codex app & IDE extension", value: true },
+      {
+        title: "Codex Cloud",
+        value: false,
+      },
+      { title: "ChatGPT Credits", value: true },
+      { title: "API Access", value: true },
+    ],
+  }}
+/>
+
+<ModelDetails
+  client:load
+  name="gpt-5.4-mini"
+  slug="gpt-5.4-mini"
+  wallpaperUrl="/images/api/models/gpt-5-mini.jpg"
+  description="Fast, efficient mini model for responsive coding tasks and subagents."
+  data={{
+    features: [
+      {
+        title: "Capability",
+        value: "",
+        icons: [
+          "openai.SparklesFilled",
+          "openai.SparklesFilled",
+          "openai.SparklesFilled",
+        ],
+      },
+      {
+        title: "Speed",
+        value: "",
+        icons: ["openai.Flash", "openai.Flash", "openai.Flash", "openai.Flash"],
+      },
+      {
+        title: "Codex CLI & SDK",
+        value: true,
+      },
+      { title: "Codex app & IDE extension", value: true },
+      {
+        title: "Codex Cloud",
+        value: false,
+      },
+      { title: "ChatGPT Credits", value: true },
+      { title: "API Access", value: true },
+    ],
+  }}
+/>
 
 <ModelDetails
   client:load
@@ -126,59 +202,24 @@
 
 </div>
 
-For most tasks in Codex, start with `gpt-5.4`. It combines strong coding,
-  reasoning, native computer use, and broader professional workflows in one
-  model. The `gpt-5.3-codex-spark` model is available in research preview for
-  ChatGPT Pro subscribers and is optimized for near-instant, real-time coding
-  iteration.
+For most tasks in Codex, start with `gpt-5.5` when it appears in your model
+  picker. It is strongest for complex coding, computer use, knowledge work, and
+  research workflows. GPT-5.5 is currently available in Codex when you sign in
+  with ChatGPT; it isn't available with API-key authentication. During the
+  rollout, continue using `gpt-5.4` if `gpt-5.5` is not yet available. Use
+  `gpt-5.4-mini` when you want a faster, lower-cost option for lighter coding
+  tasks or subagents. The `gpt-5.3-codex-spark` model is available in research
+  preview for ChatGPT Pro subscribers and is optimized for near-instant,
+  real-time coding iteration.
 
 ## Alternative models
 
 <div class="not-prose grid gap-4 md:grid-cols-2 xl:grid-cols-3">
-<ModelDetails
-  client:load
-  name="gpt-5.2-codex"
-  slug="gpt-5.2-codex"
-  wallpaperUrl="/images/codex/gpt-5.2-codex.png"
-  description="Advanced coding model for real-world engineering. Succeeded by GPT-5.3-Codex."
-  collapsible
-  data={{
-    features: [
-      {
-        title: "Capability",
-        value: "",
-        icons: [
-          "openai.SparklesFilled",
-          "openai.SparklesFilled",
-          "openai.SparklesFilled",
-          "openai.SparklesFilled",
-        ],
-      },
-      {
-        title: "Speed",
-        value: "",
-        icons: ["openai.Flash", "openai.Flash", "openai.Flash"],
-      },
-      {
-        title: "Codex CLI & SDK",
-        value: true,
-      },
-      { title: "Codex app & IDE extension", value: true },
-      {
-        title: "Codex Cloud",
-        value: true,
-      },
-      { title: "ChatGPT Credits", value: true },
-      { title: "API Access", value: true },
-    ],
-  }}
-/>
-
 <ModelDetails
   client:load
   name="gpt-5.2"
   slug="gpt-5.2"
-  description="Previous general-purpose model for coding and agentic tasks across industries and domains. Succeeded by GPT-5.4."
+  description="Previous general-purpose model for coding and agentic tasks, including hard debugging tasks that benefit from deeper deliberation."
   collapsible
   data={{
     features: [
@@ -212,222 +253,11 @@
   }}
 />
 
-<ModelDetails
-  client:load
-  name="gpt-5.1-codex-max"
-  slug="gpt-5.1-codex-max"
-  description="Optimized for long-horizon, agentic coding tasks in Codex."
-  collapsible
-  data={{
-    features: [
-      {
-        title: "Capability",
-        value: "",
-        icons: [
-          "openai.SparklesFilled",
-          "openai.SparklesFilled",
-          "openai.SparklesFilled",
-        ],
-      },
-      {
-        title: "Speed",
-        value: "",
-        icons: ["openai.Flash", "openai.Flash", "openai.Flash"],
-      },
-      {
-        title: "Codex CLI & SDK",
-        value: true,
-      },
-      { title: "Codex app & IDE extension", value: true },
-      {
-        title: "Codex Cloud",
-        value: false,
-      },
-      { title: "ChatGPT Credits", value: true },
-      { title: "API Access", value: true },
-    ],
-  }}
-/>
-
-<ModelDetails
-  client:load
-  name="gpt-5.1"
-  description="Great for coding and agentic tasks across domains. Succeeded by GPT-5.2."
-  slug="gpt-5.1"
-  collapsible
-  data={{
-    features: [
-      {
-        title: "Capability",
-        value: "",
-        icons: [
-          "openai.SparklesFilled",
-          "openai.SparklesFilled",
-          "openai.SparklesFilled",
-        ],
-      },
-      {
-        title: "Speed",
-        value: "",
-        icons: ["openai.Flash", "openai.Flash", "openai.Flash"],
-      },
-      {
-        title: "Codex CLI & SDK",
-        value: true,
-      },
-      { title: "Codex app & IDE extension", value: true },
-      {
-        title: "Codex Cloud",
-        value: false,
-      },
-      { title: "ChatGPT Credits", value: true },
-      { title: "API Access", value: true },
-    ],
-  }}
-/>
-<ModelDetails
-  client:load
-  name="gpt-5.1-codex"
-  slug="gpt-5.1-codex"
-  description="Optimized for long-running, agentic coding tasks in Codex. Succeeded by GPT-5.1-Codex-Max."
-  collapsible
-  data={{
-    features: [
-      {
-        title: "Capability",
-        value: "",
-        icons: [
-          "openai.SparklesFilled",
-          "openai.SparklesFilled",
-          "openai.SparklesFilled",
-        ],
-      },
-      {
-        title: "Speed",
-        value: "",
-        icons: ["openai.Flash", "openai.Flash", "openai.Flash"],
-      },
-      {
-        title: "Codex CLI & SDK",
-        value: true,
-      },
-      { title: "Codex app & IDE extension", value: true },
-      {
-        title: "Codex Cloud",
-        value: true,
-      },
-      { title: "ChatGPT Credits", value: true },
-      { title: "API Access", value: true },
-    ],
-  }}
-/>
-<ModelDetails
-  client:load
-  name="gpt-5-codex"
-  slug="gpt-5-codex"
-  description="Version of GPT-5 tuned for long-running, agentic coding tasks. Succeeded by GPT-5.1-Codex."
-  collapsible
-  data={{
-    features: [
-      {
-        title: "Capability",
-        value: "",
-        icons: [
-          "openai.SparklesFilled",
-          "openai.SparklesFilled",
-          "openai.SparklesFilled",
-        ],
-      },
-      {
-        title: "Speed",
-        value: "",
-        icons: ["openai.Flash", "openai.Flash", "openai.Flash"],
-      },
-      {
-        title: "Codex CLI & SDK",
-        value: true,
-      },
-      { title: "Codex app & IDE extension", value: true },
-      {
-        title: "Codex Cloud",
-        value: false,
-      },
-      { title: "ChatGPT Credits", value: true },
-      { title: "API Access", value: true },
-    ],
-  }}
-/>
-
-    <ModelDetails
-      client:load
-      name="gpt-5-codex-mini"
-      slug="gpt-5-codex"
-      description="Smaller, more cost-effective version of GPT-5-Codex. Succeeded by GPT-5.1-Codex-Mini."
-      collapsible
-      data={{
-        features: [
-          {
-            title: "Capability",
-            value: "",
-            icons: [
-              "openai.SparklesFilled",
-              "openai.SparklesFilled",
-            ],
-          },
-          { title: "Speed", value: "", icons: ["openai.Flash", "openai.Flash", "openai.Flash", "openai.Flash"] },
-          {
-            title: "Codex CLI & SDK",
-            value: true,
-          },
-          { title: "Codex app & IDE extension", value: true },
-          {
-            title: "Codex Cloud",
-            value: false,
-          },
-          { title: "ChatGPT Credits", value: true },
-          { title: "API Access", value: false },
-        ],
-      }}
-    />
-
-    <ModelDetails
-      client:load
-      name="gpt-5"
-      slug="gpt-5"
-      description="Reasoning model for coding and agentic tasks across domains. Succeeded by GPT-5.1."
-      collapsible
-      data={{
-        features: [
-          {
-            title: "Capability",
-            value: "",
-            icons: [
-              "openai.SparklesFilled",
-              "openai.SparklesFilled",
-              "openai.SparklesFilled",
-            ],
-          },
-          { title: "Speed", value: "", icons: ["openai.Flash", "openai.Flash", "openai.Flash"] },
-          {
-            title: "Codex CLI & SDK",
-            value: true,
-          },
-          { title: "Codex app & IDE extension", value: true },
-          {
-            title: "Codex Cloud",
-            value: false,
-          },
-          { title: "ChatGPT Credits", value: true },
-          { title: "API Access", value: true },
-        ],
-      }}
-    />
-
   </div>
 
 ## Other models
 
-Codex works best with the models listed above.
+When you sign in with ChatGPT, Codex works best with the models listed above.
 
 You can also point Codex at any model and provider that supports either the [Chat Completions](https://platform.openai.com/docs/api-reference/chat) or [Responses APIs](https://platform.openai.com/docs/api-reference/responses) to fit your specific use case.
 
@@ -441,9 +271,11 @@
 The Codex CLI and IDE extension use the same `config.toml` [configuration file](https://developers.openai.com/codex/config-basic). To specify a model, add a `model` entry to your configuration file. If you don't specify a model, the Codex app, CLI, or IDE Extension defaults to a recommended model.
 
 ```toml
-model = "gpt-5.4"
+model = "gpt-5.5"
 ```
 
+If `gpt-5.5` isn't available in your account yet, use `gpt-5.4`.
+
 ### Choosing a different local model temporarily
 
 In the Codex CLI, you can use the `/model` command during an active thread to change the model. In the IDE extension, you can use the model selector below the input box to choose your model.
@@ -451,7 +283,7 @@
 To start a new Codex CLI thread with a specific model or to specify the model for `codex exec` you can use the `--model`/`-m` flag:
 
 ```bash
-codex -m gpt-5.4
+codex -m gpt-5.5
 ```
 
 ### Choosing your model for cloud tasks

```
#### https://developers.openai.com/codex/noninteractive.md

```diff
--- a/https://developers.openai.com/codex/noninteractive.md
+++ b/https://developers.openai.com/codex/noninteractive.md
@@ -11,6 +11,7 @@
 
 - Run as part of a pipeline (CI, pre-merge checks, scheduled jobs).
 - Produce output you can pipe into other tools (for example, to generate release notes or summaries).
+- Fit naturally into CLI workflows that chain command output into Codex and pass Codex output to other tools.
 - Run with explicit, pre-set sandbox and approval settings.
 
 ## Basic usage
@@ -33,14 +34,30 @@
 codex exec --ephemeral "triage this repository and suggest next steps"
 ```
 
+If stdin is piped and you also provide a prompt argument, Codex treats the prompt as the instruction and the piped content as additional context.
+
+This makes it easy to generate input with one command and hand it directly to Codex:
+
+```bash
+curl -s https://jsonplaceholder.typicode.com/comments \
+  | codex exec "format the top 20 items into a markdown table" \
+  > table.md
+```
+
+For more advanced stdin piping patterns, see [Advanced stdin piping](#advanced-stdin-piping).
+
 ## Permissions and safety
 
 By default, `codex exec` runs in a read-only sandbox. In automation, set the least permissions needed for the workflow:
 
-- Allow edits: `codex exec --full-auto "<task>"`
+- Allow edits: `codex exec --sandbox workspace-write "<task>"`
 - Allow broader access: `codex exec --sandbox danger-full-access "<task>"`
 
 Use `danger-full-access` only in a controlled environment (for example, an isolated CI runner or container).
+
+Codex keeps `codex exec --full-auto` as a deprecated compatibility flag and prints a warning. Prefer the explicit `--sandbox workspace-write` flag in new scripts.
+
+Use `--ignore-user-config` when you need a run that doesn't load `$CODEX_HOME/config.toml`, and `--ignore-rules` when you need to skip user and project execpolicy `.rules` files for a controlled automation environment.
 
 If you configure an enabled MCP server with `required = true` and it fails to initialize, `codex exec` exits with an error instead of continuing without that server.
 
@@ -63,7 +80,7 @@
 {"type":"turn.started"}
 {"type":"item.started","item":{"id":"item_1","type":"command_execution","command":"bash -lc ls","status":"in_progress"}}
 {"type":"item.completed","item":{"id":"item_3","type":"agent_message","text":"Repo contains docs, sdk, and examples directories."}}
-{"type":"turn.completed","usage":{"input_tokens":24763,"cached_input_tokens":24448,"output_tokens":122}}
+{"type":"turn.completed","usage":{"input_tokens":24763,"cached_input_tokens":24448,"output_tokens":122,"reasoning_output_tokens":0}}
 ```
 
 If you only need the final message, write it to a file with `-o <path>`/`--output-last-message <path>`. This writes the final message to the file and still prints it to `stdout` (see [`codex exec`](https://developers.openai.com/codex/cli/reference#codex-exec) for details).
@@ -218,7 +235,7 @@
 
       - name: Run Codex
         run: |
-          codex exec --full-auto --sandbox workspace-write \
+          codex exec --sandbox workspace-write \
             "Read the repository, run the test suite, identify the minimal change needed to make all tests pass, implement only that change, and stop. Do not refactor unrelated files."
 
       - name: Verify tests
@@ -235,4 +252,73 @@
 
 #### Alternative: Use the Codex GitHub Action
 
-If you want to avoid installing the CLI yourself, you can run `codex exec` through the [Codex GitHub Action](https://developers.openai.com/codex/github-action) and pass the prompt as an input.+If you want to avoid installing the CLI yourself, you can run `codex exec` through the [Codex GitHub Action](https://developers.openai.com/codex/github-action) and pass the prompt as an input.
+
+## Advanced stdin piping
+
+When another command produces input for Codex, choose the stdin pattern based on where the instruction should come from. Use prompt-plus-stdin when you already know the instruction and want to pass piped output as context. Use `codex exec -` when stdin should become the full prompt.
+
+### Use prompt-plus-stdin
+
+Prompt-plus-stdin is useful when another command already produces the data you want Codex to inspect. In this mode, you write the instruction yourself and pipe in the output as context, which makes it a natural fit for CLI workflows built around command output, logs, and generated data.
+
+```bash
+npm test 2>&1 \
+  | codex exec "summarize the failing tests and propose the smallest likely fix" \
+  | tee test-summary.md
+```
+
+<ToggleSection title="More prompt-plus-stdin examples">
+
+### Summarize logs
+
+```bash
+tail -n 200 app.log \
+  | codex exec "identify the likely root cause, cite the most important errors, and suggest the next three debugging steps" \
+  > log-triage.md
+```
+
+### Inspect TLS or HTTP issues
+
+```bash
+curl -vv https://api.example.com/health 2>&1 \
+  | codex exec "explain the TLS or HTTP failure and suggest the most likely fix" \
+  > tls-debug.md
+```
+
+### Prepare a Slack-ready update
+
+```bash
+gh run view 123456 --log \
+  | codex exec "write a concise Slack-ready update on the CI failure, including the likely cause and next step" \
+  | pbcopy
+```
+
+### Draft a pull request comment from CI logs
+
+```bash
+gh run view 123456 --log \
+  | codex exec "summarize the failure in 5 bullets for the pull request thread" \
+  | gh pr comment 789 --body-file -
+```
+
+</ToggleSection>
+
+### Use `codex exec -` when stdin is the prompt
+
+If you omit the prompt argument, Codex reads the prompt from stdin. Use `codex exec -` when you want to force that behavior explicitly.
+
+The `-` sentinel is useful when another command or script is generating the entire prompt dynamically. This is a good fit when you store prompts in files, assemble prompts with shell scripts, or combine live command output with instructions before handing the whole prompt to Codex.
+
+```bash
+cat prompt.txt | codex exec -
+```
+
+```bash
+printf "Summarize this error log in 3 bullets:\n\n%s\n" "$(tail -n 200 app.log)" \
+  | codex exec -
+```
+
+```bash
+generate_prompt.sh | codex exec - --json > result.jsonl
+```
```
#### https://developers.openai.com/codex/open-source.md

```diff
--- a/https://developers.openai.com/codex/open-source.md
+++ b/https://developers.openai.com/codex/open-source.md
@@ -2,7 +2,7 @@
 
 OpenAI develops key parts of Codex in the open. That work lives on GitHub so you can follow progress, report issues, and contribute improvements.
 
-If you maintain a widely used open-source project or want to nominate maintainers stewarding important projects, you can also [apply to the Codex open source program](https://developers.openai.com/codex/community/codex-for-oss) for API credits, ChatGPT Pro with Codex, and selective access to Codex Security.
+If you maintain a widely used open-source project or want to nominate maintainers stewarding important projects, you can also [apply to the Codex for OSS program](https://developers.openai.com/community/codex-for-oss) for API credits, ChatGPT Pro with Codex, and selective access to Codex Security.
 
 ## Open-source components
 

```
#### https://developers.openai.com/codex/overview.md

```diff
--- a/https://developers.openai.com/codex/overview.md
+++ b/https://developers.openai.com/codex/overview.md
@@ -43,27 +43,27 @@
     backgroundImage="/images/codex/codex-wallpaper-3.webp"
   />
   <LinkCard
-    title="Explore"
-    href="/codex/explore"
-    description="Get inspirations on what you can build with Codex."
+    title="Explore use cases"
+    href="/codex/use-cases"
+    description="Get inspiration on what you can build with Codex."
     variant="image"
     ctaLabel="Learn more"
     backgroundImage="/images/codex/codex-wallpaper-1.webp"
   />
   <LinkCard
     title="Community"
-    href="/codex/community/meetups"
-    description="Explore Codex Ambassadors and upcoming community meetups by location."
+    href="/community"
+    description="Read community posts, explore meetups, and connect with Codex builders."
     variant="image"
     ctaLabel="See community"
     backgroundImage="/images/codex/codex-wallpaper-2.webp"
   />
   <LinkCard
-    title="Codex for OSS"
-    href="/codex/community/codex-for-oss"
+    title="Codex for Open Source"
+    href="/community/codex-for-oss"
     description="Apply or nominate maintainers for API credits, ChatGPT Pro with Codex, and selective Codex Security access."
     variant="image"
     ctaLabel="Learn more"
-    backgroundImage="/images/codex/codex_code_review.webp"
+    backgroundImage="/images/codex/codex_bg.webp"
   />
 </div>
```
#### https://developers.openai.com/codex/pricing.md

```diff
--- a/https://developers.openai.com/codex/pricing.md
+++ b/https://developers.openai.com/codex/pricing.md
@@ -1,283 +1,532 @@
 # Codex Pricing
 
-For a limited time, **try Codex for free in ChatGPT Free and Go**, or enjoy
-  **2x Codex rate limits** with Plus, Pro, Business and Enterprise
-  subscriptions.
-
-<div class="codex-pricing-grid">
-  <PricingCard
-    name="Plus"
-    subtitle="Power a few focused coding sessions each week."
-    price="$20"
-    interval="/month"
-    ctaLabel="Get Plus"
-    ctaHref="https://chatgpt.com/explore/plus?utm_internal_source=openai_developers_codex"
-  >
-
-    - Codex on the web, in the CLI, in the IDE extension, and on iOS
-    - Cloud-based integrations like automatic code review and Slack integration
-    - The latest models, including GPT-5.4 and GPT-5.3-Codex
-    - GPT-5.1-Codex-Mini for up to 4x higher usage limits for local messages
-    - Flexibly extend usage with [ChatGPT credits](#credits-overview)
-    - Other [ChatGPT features](https://chatgpt.com/pricing) as part of the Plus plan
-
-  </PricingCard>
-  <PricingCard
-    name="Pro"
-    subtitle="Rely on Codex for daily full-time development."
-    price="$200"
-    interval="/month"
-    ctaLabel="Get Pro"
-    ctaHref="https://chatgpt.com/explore/pro?utm_internal_source=openai_developers_codex"
-    highlight="Everything in Plus and:"
-  >
-
-    - Priority request processing
-    - Access to GPT-5.3-Codex-Spark (research preview), a fast Codex model for day-to-day coding tasks
-    - 6x higher usage limits for local and cloud tasks
-    - 10x more cloud-based code reviews
-    - Other [ChatGPT features](https://chatgpt.com/pricing) as part of the Pro plan
-
-  </PricingCard>
-</div>
-
-<div class="mt-8 codex-pricing-grid">
-  <PricingCard
-    name="Business"
-    subtitle="Bring Codex into your startup or growing business."
-    price="$30"
-    interval="/user/month"
-    ctaLabel="Try for free"
-    ctaHref="https://chatgpt.com/team-sign-up?utm_internal_source=openai_developers_codex"
-    highlight="Everything in Plus and:"
-  >
-
-    - Larger virtual machines to run cloud tasks faster
-    - Flexibly extend usage with [ChatGPT credits](#credits-overview)
-    - A secure, dedicated workspace with essential admin controls, SAML SSO, and MFA
-    - No training on your business data by default. [Learn more](https://openai.com/business-data/)
-    - Other [ChatGPT features](https://chatgpt.com/pricing) as part of the Business plan
-
-  </PricingCard>
-  <PricingCard
-    name="Enterprise & Edu"
-    subtitle="Unlock Codex for your entire organization with enterprise-grade functionality."
-    interval=""
-    ctaLabel="Contact sales"
-    ctaHref="https://chatgpt.com/contact-sales?utm_internal_source=openai_developers_codex"
-    highlight="Everything in Business and:"
-  >
-
-    - Priority request processing
-    - Enterprise-level security and controls, including SCIM, EKM, user analytics, domain verification, and role-based access control ([RBAC](https://help.openai.com/en/articles/11750701-rbac))
-    - Audit logs and usage monitoring via the [Compliance API](https://chatgpt.com/admin/api-reference#tag/Codex-Tasks)
-    - Data retention and data residency controls
-    - Other [ChatGPT features](https://chatgpt.com/pricing) as part of the Enterprise plan
-
-  </PricingCard>
-</div>
-
-<div class="mt-8 mb-10 codex-pricing-grid">
-  <PricingCard
-    class="codex-pricing-card--span-two"
-    name="API Key"
-    subtitle="Great for automation in shared environments like CI."
-    price=""
-    interval=""
-    ctaLabel="Learn more"
-    ctaHref="/codex/auth"
-    highlight=""
-  >
-
-    - Codex in the CLI, SDK, or IDE extension
-    - No cloud-based features (GitHub code review, Slack, etc.)
-    - Delayed access to new models like GPT-5.3-Codex and GPT-5.3-Codex-Spark
-    - Pay only for the tokens Codex uses, based on [API pricing](https://platform.openai.com/docs/pricing)
-
-  </PricingCard>
-</div>
+<h2 class="sr-only">Pricing options</h2>
+
+<ContentSwitcher
+  id="codex-pricing-plans"
+  initialValue="individual"
+  options={[
+    {
+      label: "Individual",
+      value: "individual",
+    },
+    {
+      label: "Business / Enterprise",
+      value: "business-enterprise",
+    },
+  ]}
+>
+  <div data-content-switcher-pane data-value="individual">
+    <div class="codex-pricing-grid">
+      <PricingCard
+        name="Free"
+        subtitle="Explore Codex capabilities on quick coding tasks."
+        price="$0"
+        interval="/month"
+        ctaLabel="Get Free"
+        ctaHref="https://chatgpt.com/plans/free/"
+      />
+      <PricingCard
+        name="Go"
+        subtitle="Use Codex for lightweight coding tasks."
+        price="$8"
+        interval="/month"
+        ctaLabel="Get Go"
+        ctaHref="https://chatgpt.com/plans/go"
+      />
+      <PricingCard
+        name="Plus"
+        subtitle="Power a few focused coding sessions each week."
+        price="$20"
+        interval="/month"
+        ctaLabel="Get Plus"
+        ctaHref="https://chatgpt.com/explore/plus?utm_internal_source=openai_developers_codex"
+      >
+        - Codex on the web, in the CLI, in the IDE extension, and on iOS
+        - Cloud-based integrations like automatic code review and Slack
+          integration
+        - The latest models, including GPT-5.5, GPT-5.4, and GPT-5.3-Codex
+        - GPT-5.4-mini for higher usage limits on routine local messages
+        - Flexibly extend usage with [ChatGPT credits](#credits-overview)
+        - Other [ChatGPT features](https://chatgpt.com/pricing) as part of the
+          Plus plan
+      </PricingCard>
+      <PricingCard
+        name="Pro"
+        subtitle="Choose 5x or 20x higher rate limits than Plus."
+        priceEyebrow="From"
+        price="$100"
+        interval="/month"
+        ctaLabel="Get Pro"
+        ctaHref="https://chatgpt.com/explore/pro?utm_internal_source=openai_developers_codex"
+        highlight="Everything in Plus and:"
+        footnoteLabel="*Learn more about limits and promos on both tiers."
+        footnoteHref="https://help.openai.com/en/articles/9793128-about-chatgpt-pro-plans"
+      >
+        **Double your normal Codex usage on the $100/month tier until May 31, 2026.**
+
+        - Access to GPT-5.3-Codex-Spark (research preview), a fast Codex model
+          for day-to-day coding tasks
+        - ~~5x~~ 10x or 20x more Codex usage than Plus*
+        - Other [ChatGPT features](https://chatgpt.com/pricing) as part of the
+          Pro plan
+      </PricingCard>
+      <PricingCard
+        name="API Key"
+        subtitle="Great for automation in shared environments like CI."
+        price=""
+        interval=""
+        ctaLabel="Learn more"
+        ctaHref="/codex/auth"
+        highlight=""
+      >
+        - Codex in the CLI, SDK, or IDE extension
+        - No cloud-based features (GitHub code review, Slack, etc.)
+        - Delayed access to new models like GPT-5.3-Codex and
+          GPT-5.3-Codex-Spark
+        - Pay only for the tokens Codex uses, based on [API
+          pricing](https://platform.openai.com/docs/pricing)
+      </PricingCard>
+    </div>
+
+  </div>
+
+  <div data-content-switcher-pane data-value="business-enterprise" hidden>
+    <div class="codex-pricing-grid">
+      <PricingCard
+        name="Business"
+        subtitle="Bring Codex into your startup or growing business."
+        price="Pay as you go"
+        interval=""
+        ctaLabel="Get Business"
+        ctaHref="https://chatgpt.com/codex/team/start"
+        highlight="Everything in Plus and:"
+      >
+        - Assign standard or usage-based Codex seats based on your team's needs.
+          [Learn
+          more](https://help.openai.com/en/articles/8792828-what-is-chatgpt-business)
+        - Larger virtual machines to run cloud tasks faster
+        - Flexibly extend usage with [ChatGPT credits](#credits-overview)
+        - A secure, dedicated workspace with essential admin controls, SAML SSO,
+          and MFA
+        - No training on your business data by default. [Learn
+          more](https://openai.com/business-data/)
+        - Other [ChatGPT features](https://chatgpt.com/pricing) as part of the
+          Business plan
+      </PricingCard>
+      <PricingCard
+        name="Enterprise & Edu"
+        subtitle="Unlock Codex for your entire organization with enterprise-grade functionality."
+        interval=""
+        ctaLabel="Contact sales"
+        ctaHref="https://chatgpt.com/contact-sales?utm_internal_source=openai_developers_codex"
+        highlight="Everything in Business and:"
+      >
+        - Priority request processing
+        - Enterprise-level security and controls, including SCIM, EKM, user
+          analytics, domain verification, and role-based access control
+          ([RBAC](https://help.openai.com/en/articles/11750701-rbac))
+        - Audit logs and usage monitoring via the [Compliance
+          API](https://chatgpt.com/admin/api-reference#tag/Codex-Tasks)
+        - Data retention and data residency controls
+        - Other [ChatGPT features](https://chatgpt.com/pricing) as part of the
+          Enterprise plan
+      </PricingCard>
+    </div>
+
+    <div class="mt-8 mb-10 codex-pricing-grid">
+      <PricingCard
+        class="codex-pricing-card--span-two"
+        name="API Key"
+        subtitle="Great for automation in shared environments like CI."
+        price=""
+        interval=""
+        ctaLabel="Learn more"
+        ctaHref="/codex/auth"
+        highlight=""
+      >
+        - Codex in the CLI, SDK, or IDE extension
+        - No cloud-based features (GitHub code review, Slack, etc.)
+        - Delayed access to new models like GPT-5.3-Codex and
+          GPT-5.3-Codex-Spark
+        - Pay only for the tokens Codex uses, based on [API
+          pricing](https://platform.openai.com/docs/pricing)
+      </PricingCard>
+    </div>
+
+  </div>
+</ContentSwitcher>
 
 ## Frequently asked questions
 
 ### What are the usage limits for my plan?
 
-The number of Codex messages you can send depends on the model used, size and complexity of your coding tasks and whether you run them locally or in the cloud. Small scripts or routine functions may consume only a fraction of your allowance, while larger codebases, long-running tasks, or extended sessions that require Codex to hold more context will use significantly more per message.
+The number of Codex messages you can send depends on the model used, size and
+complexity of your coding tasks and whether you run them locally or in the
+cloud. Small scripts or routine functions may consume only a fraction of your
+allowance, while larger codebases, long-running tasks, or extended sessions that
+require Codex to hold more context will use significantly more per message.
+
+GPT-5.5 uses significantly fewer tokens to achieve results comparable to
+GPT-5.4. Its Codex setup runs faster and delivers higher-quality results for
+most users. These efficiency gains support generous usage limits despite
+GPT-5.5 being a significantly more capable model.
 
 <div id="usage-limits">
   <ContentSwitcher
     id="codex-usage-limits"
-    initialValue="gpt-5-3-codex"
+    initialValue="plus"
     align="right"
     options={[
       {
-        label: "GPT-5.4",
-        value: "gpt-5-4",
+        label: "Plus",
+        value: "plus",
       },
       {
-        label: "GPT-5.3-Codex",
-        value: "gpt-5-3-codex",
+        label: "Pro 5x",
+        value: "pro",
       },
       {
-        label: "GPT-5.1-Codex-Mini",
-        value: "gpt-5-1-codex-mini",
+        label: "Pro 20x",
+        value: "pro-20x",
+      },
+      {
+        label: "Business",
+        value: "business",
+      },
+      {
+        label: "API Key",
+        value: "api-key",
       },
     ]}
   >
-    <div data-content-switcher-pane data-value="gpt-5-4">
-      <div class="hidden">GPT-5.4</div>
+    <div data-content-switcher-pane data-value="plus">
+      <div class="hidden">Plus</div>
 
       <table>
         <thead>
           <tr>
             <th scope="col"></th>
             <th scope="col" style="text-align:center">
-              Local Messages[\*](#shared-limits) / 5h
-            </th>
-            <th scope="col" style="text-align:center">
-              Cloud Tasks[\*](#shared-limits) / 5h
-            </th>
-            <th scope="col" style="text-align:center">
-              Code Reviews / week
+              Local Messages[\*](#shared-limits-plus) / 5h
+            </th>
+            <th scope="col" style="text-align:center">
+              Cloud Tasks[\*](#shared-limits-plus) / 5h
+            </th>
+            <th scope="col" style="text-align:center">
+              Code Reviews / 5h
             </th>
           </tr>
         </thead>
         <tbody>
           <tr>
-            <td>ChatGPT Plus</td>
-            <td style="text-align:center">33-168</td>
-            <td style="text-align:center">Not available</td>
-            <td style="text-align:center">Not available</td>
-          </tr>
-          <tr>
-            <td>ChatGPT Pro</td>
-            <td style="text-align:center">223-1120</td>
-            <td style="text-align:center">Not available</td>
-            <td style="text-align:center">Not available</td>
-          </tr>
-          <tr>
-            <td>ChatGPT Business</td>
-            <td style="text-align:center">33-168</td>
-            <td style="text-align:center">Not available</td>
-            <td style="text-align:center">Not available</td>
-          </tr>
-          <tr>
-            <td>ChatGPT Enterprise &amp; Edu</td>
-            <td colspan="3" style="text-align:center">
-              No fixed limits — usage scales with [credits](#credits-overview)
-            </td>
-          </tr>
-          <tr>
-            <td>API Key</td>
+            <td>GPT-5.5</td>
+            <td style="text-align:center">15-80</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+          </tr>
+          <tr>
+            <td>GPT-5.4</td>
+            <td style="text-align:center">20-100</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+          </tr>
+          <tr>
+            <td>GPT-5.4-mini</td>
+            <td style="text-align:center">60-350</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+          </tr>
+          <tr>
+            <td>GPT-5.3-Codex</td>
+            <td style="text-align:center">30-150</td>
+            <td style="text-align:center">10-60</td>
+            <td style="text-align:center">20-50</td>
+          </tr>
+        </tbody>
+        <tfoot>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              <a id="shared-limits-plus" class="footnote">
+                *The usage limits for local messages and cloud tasks share a
+                **five-hour window**. Additional weekly limits may apply.
+              </a>
+            </td>
+          </tr>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              For Enterprise/Edu users, there are no fixed rate limits - usage
+              scales with [credits](#credits-overview)
+            </td>
+          </tr>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              Enterprise and Edu plans without flexible pricing have the same
+              per-seat usage limits as Plus for most features
+            </td>
+          </tr>
+        </tfoot>
+      </table>
+    </div>
+    <div data-content-switcher-pane data-value="pro" hidden>
+      <div class="hidden">Pro 5x</div>
+
+      <table>
+        <thead>
+          <tr>
+            <th scope="col"></th>
+            <th scope="col" style="text-align:center">
+              Local Messages[\*](#shared-limits-pro) / 5h
+            </th>
+            <th scope="col" style="text-align:center">
+              Cloud Tasks[\*](#shared-limits-pro) / 5h
+            </th>
+            <th scope="col" style="text-align:center">
+              Code Reviews / 5h
+            </th>
+          </tr>
+        </thead>
+        <tbody>
+          <tr>
+            <td>GPT-5.5</td>
+            <td style="text-align:center">80-400</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+          </tr>
+          <tr>
+            <td>GPT-5.4</td>
+            <td style="text-align:center">100-500</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+          </tr>
+          <tr>
+            <td>GPT-5.4-mini</td>
+            <td style="text-align:center">300-1750</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+          </tr>
+          <tr>
+            <td>GPT-5.3-Codex</td>
+            <td style="text-align:center">150-750</td>
+            <td style="text-align:center">50-300</td>
+            <td style="text-align:center">100-250</td>
+          </tr>
+        </tbody>
+        <tfoot>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              <a id="shared-limits-pro" class="footnote">
+                *The usage limits for local messages and cloud tasks share a
+                **five-hour window**. Additional weekly limits may apply.
+              </a>
+            </td>
+          </tr>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              Pro $100 gets 2x the usage shown above until May 31, 2026.
+            </td>
+          </tr>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              For Enterprise/Edu users, there are no fixed rate limits - usage
+              scales with [credits](#credits-overview)
+            </td>
+          </tr>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              Enterprise and Edu plans without flexible pricing have the same
+              per-seat usage limits as Plus for most features
+            </td>
+          </tr>
+        </tfoot>
+      </table>
+    </div>
+    <div data-content-switcher-pane data-value="pro-20x" hidden>
+      <div class="hidden">Pro 20x</div>
+
+      <table>
+        <thead>
+          <tr>
+            <th scope="col"></th>
+            <th scope="col" style="text-align:center">
+              Local Messages[\*](#shared-limits-pro-20x) / 5h
+            </th>
+            <th scope="col" style="text-align:center">
+              Cloud Tasks[\*](#shared-limits-pro-20x) / 5h
+            </th>
+            <th scope="col" style="text-align:center">
+              Code Reviews / 5h
+            </th>
+          </tr>
+        </thead>
+        <tbody>
+          <tr>
+            <td>GPT-5.5</td>
+            <td style="text-align:center">300-1600</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+          </tr>
+          <tr>
+            <td>GPT-5.4</td>
+            <td style="text-align:center">400-2000</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+          </tr>
+          <tr>
+            <td>GPT-5.4-mini</td>
+            <td style="text-align:center">1200-7000</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+          </tr>
+          <tr>
+            <td>GPT-5.3-Codex</td>
+            <td style="text-align:center">600-3000</td>
+            <td style="text-align:center">200-1200</td>
+            <td style="text-align:center">400-1000</td>
+          </tr>
+        </tbody>
+        <tfoot>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              <a id="shared-limits-pro-20x" class="footnote">
+                *The usage limits for local messages and cloud tasks share a
+                **five-hour window**. Additional weekly limits may apply.
+              </a>
+            </td>
+          </tr>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              Pro $200 gets a boost on the usage shown above until May 31,
+              2026. [Learn
+              more](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-plans).
+            </td>
+          </tr>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              For Enterprise/Edu users, there are no fixed rate limits - usage
+              scales with [credits](#credits-overview)
+            </td>
+          </tr>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              Enterprise and Edu plans without flexible pricing have the same
+              per-seat usage limits as Plus for most features
+            </td>
+          </tr>
+        </tfoot>
+      </table>
+    </div>
+    <div data-content-switcher-pane data-value="business" hidden>
+      <div class="hidden">Business</div>
+
+      <table>
+        <thead>
+          <tr>
+            <th scope="col"></th>
+            <th scope="col" style="text-align:center">
+              Local Messages[\*](#shared-limits-business) / 5h
+            </th>
+            <th scope="col" style="text-align:center">
+              Cloud Tasks[\*](#shared-limits-business) / 5h
+            </th>
+            <th scope="col" style="text-align:center">
+              Code Reviews / 5h
+            </th>
+          </tr>
+        </thead>
+        <tbody>
+          <tr>
+            <td>GPT-5.5</td>
+            <td style="text-align:center">15-80</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+          </tr>
+          <tr>
+            <td>GPT-5.4</td>
+            <td style="text-align:center">20-100</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+          </tr>
+          <tr>
+            <td>GPT-5.4-mini</td>
+            <td style="text-align:center">60-350</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+          </tr>
+          <tr>
+            <td>GPT-5.3-Codex</td>
+            <td style="text-align:center">30-150</td>
+            <td style="text-align:center">10-60</td>
+            <td style="text-align:center">20-50</td>
+          </tr>
+        </tbody>
+        <tfoot>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              <a id="shared-limits-business" class="footnote">
+                *The usage limits for local messages and cloud tasks share a
+                **five-hour window**. Additional weekly limits may apply.
+              </a>
+            </td>
+          </tr>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              For Enterprise/Edu users, there are no fixed rate limits - usage
+              scales with [credits](#credits-overview)
+            </td>
+          </tr>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              Enterprise and Edu plans without flexible pricing have the same
+              per-seat usage limits as Plus for most features
+            </td>
+          </tr>
+        </tfoot>
+      </table>
+    </div>
+    <div data-content-switcher-pane data-value="api-key" hidden>
+      <div class="hidden">API Key</div>
+
+      <table>
+        <thead>
+          <tr>
+            <th scope="col"></th>
+            <th scope="col" style="text-align:center">
+              Local Messages[\*](#shared-limits-api-key) / 5h
+            </th>
+            <th scope="col" style="text-align:center">
+              Cloud Tasks[\*](#shared-limits-api-key) / 5h
+            </th>
+            <th scope="col" style="text-align:center">
+              Code Reviews / 5h
+            </th>
+          </tr>
+        </thead>
+        <tbody>
+          <tr>
+            <td>GPT-5.5</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+          </tr>
+          <tr>
+            <td>GPT-5.4</td>
             <td style="text-align:center">
               [Usage-based](https://platform.openai.com/docs/pricing)
             </td>
             <td style="text-align:center">Not available</td>
             <td style="text-align:center">Not available</td>
           </tr>
-        </tbody>
-      </table>
-    </div>
-    <div data-content-switcher-pane data-value="gpt-5-3-codex" hidden>
-      <div class="hidden">GPT-5.3-Codex</div>
-
-      <table>
-        <thead>
-          <tr>
-            <th scope="col"></th>
-            <th scope="col" style="text-align:center">
-              Local Messages[\*](#shared-limits) / 5h
-            </th>
-            <th scope="col" style="text-align:center">
-              Cloud Tasks[\*](#shared-limits) / 5h
-            </th>
-            <th scope="col" style="text-align:center">
-              Code Reviews / week
-            </th>
-          </tr>
-        </thead>
-        <tbody>
-          <tr>
-            <td>ChatGPT Plus</td>
-            <td style="text-align:center">45-225</td>
-            <td style="text-align:center">10-60</td>
-            <td style="text-align:center">10-25</td>
-          </tr>
-          <tr>
-            <td>ChatGPT Pro</td>
-            <td style="text-align:center">300-1500</td>
-            <td style="text-align:center">50-400</td>
-            <td style="text-align:center">100-250</td>
-          </tr>
-          <tr>
-            <td>ChatGPT Business</td>
-            <td style="text-align:center">45-225</td>
-            <td style="text-align:center">10-60</td>
-            <td style="text-align:center">10-25</td>
-          </tr>
-          <tr>
-            <td>ChatGPT Enterprise &amp; Edu</td>
-            <td colspan="3" style="text-align:center">
-              No fixed limits — usage scales with [credits](#credits-overview)
-            </td>
-          </tr>
-          <tr>
-            <td>API Key</td>
+          <tr>
+            <td>GPT-5.4-mini</td>
             <td style="text-align:center">
               [Usage-based](https://platform.openai.com/docs/pricing)
             </td>
             <td style="text-align:center">Not available</td>
             <td style="text-align:center">Not available</td>
           </tr>
-        </tbody>
-      </table>
-    </div>
-    <div data-content-switcher-pane data-value="gpt-5-1-codex-mini" hidden>
-      <div class="hidden">GPT-5.1-Codex-Mini</div>
-
-      <table>
-        <thead>
-          <tr>
-            <th scope="col"></th>
-            <th scope="col" style="text-align:center">
-              Local Messages[\*](#shared-limits) / 5h
-            </th>
-            <th scope="col" style="text-align:center">
-              Cloud Tasks[\*](#shared-limits) / 5h
-            </th>
-            <th scope="col" style="text-align:center">
-              Code Reviews / week
-            </th>
-          </tr>
-        </thead>
-        <tbody>
-          <tr>
-            <td>ChatGPT Plus</td>
-            <td style="text-align:center">180-900</td>
-            <td style="text-align:center">Not available</td>
-            <td style="text-align:center">Not available</td>
-          </tr>
-          <tr>
-            <td>ChatGPT Pro</td>
-            <td style="text-align:center">1200-6000</td>
-            <td style="text-align:center">Not available</td>
-            <td style="text-align:center">Not available</td>
-          </tr>
-          <tr>
-            <td>ChatGPT Business</td>
-            <td style="text-align:center">180-900</td>
-            <td style="text-align:center">Not available</td>
-            <td style="text-align:center">Not available</td>
-          </tr>
-          <tr>
-            <td>ChatGPT Enterprise &amp; Edu</td>
-            <td style="text-align:center">
-              Local usage scales with [credits](#credits-overview)
-            </td>
-            <td style="text-align:center">Not available</td>
-            <td style="text-align:center">Not available</td>
-          </tr>
-          <tr>
-            <td>API Key</td>
+          <tr>
+            <td>GPT-5.3-Codex</td>
             <td style="text-align:center">
               [Usage-based](https://platform.openai.com/docs/pricing)
             </td>
@@ -285,176 +534,330 @@
             <td style="text-align:center">Not available</td>
           </tr>
         </tbody>
+        <tfoot>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              <a id="shared-limits-api-key" class="footnote">
+                *The usage limits for local messages and cloud tasks share a
+                **five-hour window**. Additional weekly limits may apply.
+              </a>
+            </td>
+          </tr>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              For Enterprise/Edu users, there are no fixed rate limits - usage
+              scales with [credits](#credits-overview)
+            </td>
+          </tr>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              Enterprise and Edu plans without flexible pricing have the same
+              per-seat usage limits as Plus for most features
+            </td>
+          </tr>
+        </tfoot>
       </table>
     </div>
 
   </ContentSwitcher>
 </div>
 
-<a id="shared-limits" class="footnote">
-  *The usage limits for local messages and cloud tasks share a **five-hour
-  window**. Additional weekly limits may apply.
-</a>
+Codex usage limits are shared with other agentic features once pricing for
+those features is effective. This currently includes [ChatGPT for
+Excel](https://help.openai.com/articles/20001063) on Plus and Pro.
 
 Speed configurations increase credit consumption for all applicable models, so
-they also use included limits faster. Details can be found
-[here](https://developers.openai.com/codex/speed).
-
-Enterprise and Edu plans without flexible pricing have the same per-seat usage limits as Plus for most features.
-
-GPT-5.3-Codex-Spark is in research preview for ChatGPT Pro users only, and isn't available in the API at launch. Because it runs on specialized low-latency hardware, usage is governed by a separate usage limit that may adjust based on demand.
+they also use included limits faster. Fast mode consumes credits at a higher
+rate for supported models. See [Speed](https://developers.openai.com/codex/speed) for supported models and
+rates. Image generations also use included limits ~3-5x faster on average,
+depending on image quality and size. GPT-5.3-Codex-Spark is in research preview
+for ChatGPT Pro users only, and isn't available in the API at launch. Because it
+runs on specialized low-latency hardware, usage is governed by a separate usage
+limit that may adjust based on demand.
 
 ### What happens when you hit usage limits?
 
-ChatGPT Plus and Pro users who reach their usage limit can purchase additional credits to continue working without needing to upgrade their existing plan.
-
-Business, Edu, and Enterprise plans with [flexible pricing](https://help.openai.com/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans) can purchase additional workspace credits to continue using Codex.
-
-If you are approaching usage limits, you can also switch to the GPT-5.1-Codex-Mini model to make your usage limits last longer.
-
-All users may also run extra local tasks using an API key, with usage charged at [standard API rates](https://platform.openai.com/docs/pricing).
+ChatGPT Plus and Pro users who reach their usage limit can purchase additional
+credits to continue working without needing to upgrade their existing plan.
+
+Business, Edu, and Enterprise plans with [flexible
+pricing](https://help.openai.com/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans)
+can purchase additional workspace credits to continue using Codex.
+
+If you are approaching usage limits, you can also switch to a smaller model to
+make your usage limits last longer.
+
+All users may also run extra local tasks using an API key, with usage charged at
+[standard API rates](https://platform.openai.com/docs/pricing).
+
+<a id="image-generation-usage-limits"></a>
+
+### How does image generation count toward usage limits?
+
+Image generation counts toward the same general Codex usage limits as local
+messages and cloud tasks. Image generations use included limits 3-5x faster on
+average than similar turns without image generation, depending on
+image quality and size. After you reach your included limits, image generation
+also draws from [credits](#credits-overview).
+
+Image generation isn't available on the Free plan. When you use Codex with an
+API key, API pricing applies to image generation instead of included ChatGPT
+usage limits.
+
+### What's the current Codex usage promo on Pro?
+
+We’re currently offering extra Codex usage on both Pro tiers.
+
+For **Pro $100**, to celebrate the launch, you’ll get **2x Codex usage through May 31, 2026**. That means 10x usage instead of the standard 5x.
+
+**For Pro $200**, as a thank you to our most loyal customers, we’re carrying forward the benefits of our earlier 2x promo, which means Pro $200 now includes 20x Plus on an ongoing basis. In addition, we’re continuing to honor the higher 5-hour Codex limits for a limited time, so those remain at 25x Plus through May 31, 2026 instead of the standard 20x Plus.
 
 ### Where can I see my current usage limits?
 
-You can find your current limits in the [Codex usage dashboard](https://chatgpt.com/codex/settings/usage). If you want to see your remaining limits during an active Codex CLI session, you can use `/status`.
+You can find your current limits in the [Codex usage
+dashboard](https://chatgpt.com/codex/settings/usage). If you want to see your
+remaining limits during an active Codex CLI session, you can use `/status`.
 
 ### How do credits work?
 
-Credits let you continue using Codex after you reach your included usage limits. Usage draws down from your available credits based on the models and features you use, allowing you to extend work without interruption.
-
-Credit cost per message varies based on the model used, the task size and complexity, and the reasoning required. The table shows average credit costs. Average rates may evolve over time as new capabilities are introduced.
+Credits let you continue using Codex after you reach your included usage
+limits. Usage draws down from your available credits based on the models and
+features you use, allowing you to extend work without interruption.
+
+As of April 2nd, we're moving pricing to API token-based rates. Credits remain
+the core pricing unit that customers purchase and consume, but usage is based
+on tokens consumed, calculated as credits per million input tokens, cached
+input tokens and output tokens your workspace consumes. Read about tokens
+[here](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them).
+
+This format replaces average per-message estimates for your plan with a direct
+mapping between token usage and credits. It's most useful when you want a
+clearer view of how input, cached input, and output affect credit consumption.
+
+Under this model, actual credit usage depends on the mix of input, cached input,
+and output tokens in each task. The new rate card is displayed in the table
+below, and is currently applicable to **new and existing Business customers,
+and new Enterprise customers**.
+
+**New and existing customers on all other plan types** should continue to use
+the previous message based rate card, until we migrate you to the new rates in
+the upcoming weeks.
+
+Select your appropriate plan type in the table below to see rates.
 
 <div id="credits-overview">
   <ContentSwitcher
     id="codex-credit-costs"
-    initialValue="gpt-5-3-codex"
+    initialValue="business-enterprise-new"
     align="right"
     options={[
       {
-        label: "GPT-5.4",
-        value: "gpt-5-4",
+        label: "Business & New Enterprise Customers",
+        value: "business-enterprise-new",
       },
       {
-        label: "GPT-5.3-Codex",
-        value: "gpt-5-3-codex",
-      },
-      {
-        label: "GPT-5.1-Codex-Mini",
-        value: "gpt-5-1-codex-mini",
+        label: "Plus, Pro, Existing Enterprise/Edu and New Edu",
+        value: "plus-pro-enterprise-edu-legacy",
       },
     ]}
   >
-    <div data-content-switcher-pane data-value="gpt-5-4">
-      <div class="hidden">GPT-5.4</div>
-
+    <div data-content-switcher-pane data-value="business-enterprise-new">
+      <div class="hidden">Business & New Enterprise Customers</div>
       <table>
         <thead>
           <tr>
-            <th scope="col"></th>
-            <th scope="col" style="text-align:center">Unit</th>
-            <th scope="col" style="text-align:center">Average credit cost</th>
+            <th scope="col">Credits per 1M tokens</th>
+            <th scope="col" style="text-align:center">
+              Input Tokens
+            </th>
+            <th scope="col" style="text-align:center">
+              Cached input tokens
+            </th>
+            <th scope="col" style="text-align:center">
+              Output Tokens
+            </th>
           </tr>
         </thead>
         <tbody>
           <tr>
+            <td>GPT-5.5</td>
+            <td style="text-align:center">125 credits</td>
+            <td style="text-align:center">12.50 credits</td>
+            <td style="text-align:center">750 credits</td>
+          </tr>
+          <tr>
+            <td>GPT-5.4</td>
+            <td style="text-align:center">62.50 credits</td>
+            <td style="text-align:center">6.250 credits</td>
+            <td style="text-align:center">375 credits</td>
+          </tr>
+          <tr>
+            <td>GPT-5.4-mini</td>
+            <td style="text-align:center">18.75 credits</td>
+            <td style="text-align:center">1.875 credits</td>
+            <td style="text-align:center">113 credits</td>
+          </tr>
+          <tr>
+            <td>GPT-5.3-Codex</td>
+            <td style="text-align:center">43.75 credits</td>
+            <td style="text-align:center">4.375 credits</td>
+            <td style="text-align:center">350 credits</td>
+          </tr>
+          <tr>
+            <td>GPT-5.2</td>
+            <td style="text-align:center">43.75 credits</td>
+            <td style="text-align:center">4.375 credits</td>
+            <td style="text-align:center">350 credits</td>
+          </tr>
+          <tr>
+            <td>GPT-5.3-Codex-Spark</td>
+            <td colspan="3" style="text-align:center">
+              research preview
+            </td>
+          </tr>
+          <tr>
+            <td>GPT-Image-2 (image)</td>
+            <td style="text-align:center">200 credits</td>
+            <td style="text-align:center">50 credits</td>
+            <td style="text-align:center">750 credits</td>
+          </tr>
+          <tr>
+            <td>GPT-Image-2 (text)</td>
+            <td style="text-align:center">125 credits</td>
+            <td style="text-align:center">31.25 credits</td>
+            <td style="text-align:center">250 credits</td>
+          </tr>
+        </tbody>
+        <tfoot>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              Fast mode consumes credits at a higher rate for supported models.
+              See <a href="/codex/speed">Speed</a> for rates.
+            </td>
+          </tr>
+          <tr>
+            <td colspan="4" style="text-align:center">
+              Cloud tasks and code review run on GPT-5.3-Codex.
+            </td>
+          </tr>
+        </tfoot>
+      </table>
+    </div>
+    <div
+      data-content-switcher-pane
+      data-value="plus-pro-enterprise-edu-legacy"
+      hidden
+    >
+      <div class="hidden">Plus, Pro, Existing Enterprise/Edu and New Edu</div>
+      <table>
+        <thead>
+          <tr>
+            <th scope="col"></th>
+            <th scope="col" style="text-align:center">
+              Unit
+            </th>
+            <th scope="col" style="text-align:center">
+              GPT-5.5
+            </th>
+            <th scope="col" style="text-align:center">
+              GPT-5.4
+            </th>
+            <th scope="col" style="text-align:center">
+              GPT-5.3-Codex
+            </th>
+            <th scope="col" style="text-align:center">
+              GPT-5.4-mini
+            </th>
+          </tr>
+        </thead>
+        <tbody>
+          <tr>
             <td>Local Tasks</td>
             <td style="text-align:center">1 message</td>
+            <td style="text-align:center">\~14 credits</td>
             <td style="text-align:center">\~7 credits</td>
+            <td style="text-align:center">\~5 credits</td>
+            <td style="text-align:center">\~2 credits</td>
           </tr>
           <tr>
             <td>Cloud Tasks</td>
             <td style="text-align:center">1 message</td>
-            <td style="text-align:center">\~34 credits</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">\~25 credits</td>
+            <td style="text-align:center">Not available</td>
           </tr>
           <tr>
             <td>Code Review</td>
             <td style="text-align:center">1 pull request</td>
-            <td style="text-align:center">\~34 credits</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">Not available</td>
+            <td style="text-align:center">\~25 credits</td>
+            <td style="text-align:center">Not available</td>
+          </tr>
+          <tr>
+            <td>Image generation</td>
+            <td style="text-align:center">1 image (1024px &times; 1024px)</td>
+            <td colspan="4" style="text-align:center">
+              \~5-6 credits
+            </td>
+          </tr>
+          <tr>
+            <td>Image generation</td>
+            <td style="text-align:center">1 image (1024px &times; 1536px)</td>
+            <td colspan="4" style="text-align:center">
+              \~7-8 credits
+            </td>
           </tr>
         </tbody>
+        <tfoot>
+          <tr>
+            <td colspan="6" style="text-align:center">
+              Fast mode consumes credits at a higher rate for supported models.
+              See <a href="/codex/speed">Speed</a> for rates.
+            </td>
+          </tr>
+          <tr>
+            <td colspan="6" style="text-align:center">
+              These averages also apply to GPT-5.2.
+            </td>
+          </tr>
+        </tfoot>
       </table>
     </div>
-    <div data-content-switcher-pane data-value="gpt-5-3-codex" hidden>
-      <div class="hidden">GPT-5.3-Codex</div>
-
-      <table>
-        <thead>
-          <tr>
-            <th scope="col"></th>
-            <th scope="col" style="text-align:center">Unit</th>
-            <th scope="col" style="text-align:center">Average credit cost</th>
-          </tr>
-        </thead>
-        <tbody>
-          <tr>
-            <td>Local Tasks</td>
-            <td style="text-align:center">1 message</td>
-            <td style="text-align:center">\~5 credits</td>
-          </tr>
-          <tr>
-            <td>Cloud Tasks</td>
-            <td style="text-align:center">1 message</td>
-            <td style="text-align:center">\~25 credits</td>
-          </tr>
-          <tr>
-            <td>Code Review</td>
-            <td style="text-align:center">1 pull request</td>
-            <td style="text-align:center">\~25 credits</td>
-          </tr>
-        </tbody>
-      </table>
-    </div>
-    <div data-content-switcher-pane data-value="gpt-5-1-codex-mini" hidden>
-      <div class="hidden">GPT-5.1-Codex-Mini</div>
-
-      <table>
-        <thead>
-          <tr>
-            <th scope="col"></th>
-            <th scope="col" style="text-align:center">Unit</th>
-            <th scope="col" style="text-align:center">Average credit cost</th>
-          </tr>
-        </thead>
-        <tbody>
-          <tr>
-            <td>Local Tasks</td>
-            <td style="text-align:center">1 message</td>
-            <td style="text-align:center">\~1 credit</td>
-          </tr>
-          <tr>
-            <td>Cloud Tasks</td>
-            <td style="text-align:center">1 message</td>
-            <td style="text-align:center">Not available</td>
-          </tr>
-          <tr>
-            <td>Code Review</td>
-            <td style="text-align:center">1 pull request</td>
-            <td style="text-align:center">Not available</td>
-          </tr>
-        </tbody>
-      </table>
-    </div>
-
   </ContentSwitcher>
 </div>
 
-These averages also apply to legacy GPT-5.2, GPT-5.2-Codex, GPT-5.1, GPT-5.1-Codex-Max, GPT-5, GPT-5-Codex, and GPT-5-Codex-Mini.
-
 Speed configurations will increase credit consumption for all models that apply.
-Details can be found [here](https://developers.openai.com/codex/speed).
-
-[Learn more about credits in ChatGPT Plus and Pro.](https://help.openai.com/en/articles/12642688-using-credits-for-flexible-usage-in-chatgpt-freegopluspro-sora)  
-[Learn more about credits in ChatGPT Business, Enterprise, and Edu.](https://help.openai.com/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans)
+Fast mode consumes credits at a higher rate for supported models. See
+[Speed](https://developers.openai.com/codex/speed) for supported models and rates.
+
+[Learn more about credits in ChatGPT Plus and
+Pro.](https://help.openai.com/en/articles/12642688)
+
+[Learn more about credits in ChatGPT Business, Enterprise, and
+Edu.](https://help.openai.com/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans)
 
 ### What counts as Code Review usage?
 
-Code Review usage applies only when Codex runs reviews through GitHub—for example, when you tag `@Codex` for review in a pull request or enable automatic reviews on your repository. Reviews run locally or outside of GitHub count toward your general usage limits.
+Code Review usage applies only when Codex runs reviews through GitHub—for
+example, when you tag `@Codex` for review in a pull request or enable automatic
+reviews on your repository. Reviews run locally or outside of GitHub count
+toward your general usage limits.
 
 ### What can I do to make my usage limits last longer?
 
-The usage limits and credits above are average rates. You can try the following tips to maximize your limits:
-
-- **Control the size of your prompts.** Be precise with the instructions you give Codex, but remove unnecessary context.
-- **Reduce the size of your AGENTS.md.** If you work on a larger project, you can control how much context you inject through AGENTS.md files by [nesting them within your repository](https://developers.openai.com/codex/guides/agents-md#layer-project-instructions).
-- **Limit the number of MCP servers you use.** Every [MCP](https://developers.openai.com/codex/mcp) you add to Codex adds more context to your messages and uses more of your limit. Disable MCP servers when you don’t need them.
-- **Switch to GPT-5.1-Codex-Mini for routine tasks.** Using the mini model should extend your usage limits by roughly 4x.+The usage limits and credits above are average rates. You can try the following
+tips to maximize your limits:
+
+- **Control the size of your prompts.** Be precise with the instructions you
+  give Codex, but remove unnecessary context.
+- **Reduce the size of your AGENTS.md.** If you work on a larger project, you
+  can control how much context you inject through AGENTS.md files by [nesting
+  them within your repository](https://developers.openai.com/codex/guides/agents-md#layer-project-instructions).
+- **Limit the number of MCP servers you use.** Every [MCP](https://developers.openai.com/codex/mcp) you add
+  to Codex adds more context to your messages and uses more of your limit.
+  Disable MCP servers when you don’t need them.
+- **Switch to a smaller model for routine tasks.** Using GPT-5.4 or
+  GPT-5.4-mini can extend your local-message usage limits, depending on the
+  model you switch from.
```
#### https://developers.openai.com/codex/prompting.md

```diff
--- a/https://developers.openai.com/codex/prompting.md
+++ b/https://developers.openai.com/codex/prompting.md
@@ -14,7 +14,7 @@
 Add a new command-line option `--json` that outputs JSON.
 ```
 
-When you submit a prompt, Codex works in a loop: it calls the model and then performs any actions (file reads, file edits, tool calls, and so on) indicated by the model output. This process ends when the task is complete or you cancel it.
+When you submit a prompt, Codex works in a loop: it calls the model and then performs the actions indicated by the model output, such as file reads, file edits, and tool calls. This process ends when the task is complete or you cancel it.
 
 As with ChatGPT, Codex is only as effective as the instructions you give it. Here are some tips we find helpful when prompting Codex:
 
@@ -34,6 +34,14 @@
 - **Local threads** run on your machine. Codex can read and edit your files and run commands, so you can see what changes and use your existing tools. To reduce the risk of unwanted changes outside your workspace, local threads run in a [sandbox](https://developers.openai.com/codex/agent-approvals-security).
 - **Cloud threads** run in an isolated [environment](https://developers.openai.com/codex/cloud/environments). Codex clones your repository and checks out the branch it's working on. Cloud threads are useful when you want to run work in parallel or delegate tasks from another device. To use cloud threads with your repo, push your code to GitHub first. You can also [delegate tasks from your local machine](https://developers.openai.com/codex/ide/cloud-tasks), which includes your current working state.
 
+In the Codex app, you can also start a chat without choosing a project. Chats
+aren't tied to a saved repository or project folder. Use them for research,
+planning, connected-tool workflows, or other work where Codex shouldn't start
+from a codebase. Chats use a Codex-managed `threads` directory under your Codex
+home as their working location. By default, that location is `~/.codex/threads`.
+To change the base location for this state, set `CODEX_HOME`; see
+[Config and state locations](https://developers.openai.com/codex/config-advanced#config-and-state-locations).
+
 ## Context
 
 When you submit a prompt, include context that Codex can use, such as references to relevant files and images. The Codex IDE extension automatically includes the list of open files and the selected text range as context.

```
#### https://developers.openai.com/codex/quickstart.md

```diff
--- a/https://developers.openai.com/codex/quickstart.md
+++ b/https://developers.openai.com/codex/quickstart.md
@@ -1,12 +1,8 @@
 # Quickstart
 
-ChatGPT Plus, Pro, Business, Edu, and Enterprise plans include Codex. Using Codex with your ChatGPT subscription gives you access to the latest Codex models and features.
+Every ChatGPT plan includes Codex.
 
 You can also use Codex with API credits by signing in with an OpenAI API key.
-
-For a limited time, **try Codex for free in ChatGPT Free and Go**, or enjoy
-  **2x Codex rate limits** with Plus, Pro, Business and Enterprise
-  subscriptions.
 
 ## Setup
 
@@ -17,10 +13,11 @@
 (() => {
   const platform =
     (navigator.userAgentData?.platform || navigator.platform || "").toLowerCase();
-  const isMac =
+  const isDesktopAppPlatform =
     platform.includes("mac") ||
-    /macintosh|mac os x/i.test(navigator.userAgent || "");
-  if (!isMac) return;
+    platform.includes("win") ||
+    /macintosh|mac os x|windows|win64|win32/i.test(navigator.userAgent || "");
+  if (!isDesktopAppPlatform) return;
 
   const shouldPreferApp = () => {
     try {
@@ -58,12 +55,15 @@
   ]}
 >
   <div slot="app">
-The Codex app is available on macOS (Apple Silicon).
+The Codex app is available on macOS and Windows.
+
+Most Codex app features are available on both platforms. Platform-specific
+exceptions are noted in the relevant docs.
 
 <WorkflowSteps variant="headings">
 1. Download and install the Codex app
 
-    Download the Codex app for Windows or macOS.
+    Download the Codex app for macOS or Windows. Choose the Intel build if you're using an Intel-based Mac.
 
     <CodexAppDownloadCta client:load className="mb-4" />
 
@@ -81,7 +81,7 @@
 
    Choose a project folder that you want Codex to work in.
 
-If you used the Codex app, CLI, or IDE Extension before you'll see past projects that you worked on.
+    If you used the Codex app, CLI, or IDE Extension before you'll see past projects that you worked on.
 
 4. Send your first message
 
@@ -147,9 +147,9 @@
      />
    </ExampleGallery>
 
-   If you need more inspiration, check out the [explore section](https://developers.openai.com/codex/explore).
-
-    <CtaPillLink href="/codex/app" label="Learn more about the Codex app" class="mt-8" />
+   If you need more inspiration, explore [Codex use cases](https://developers.openai.com/codex/use-cases).
+   If you're new to Codex, read the [best practices guide](https://developers.openai.com/codex/learn/best-practices).
+
 </WorkflowSteps>
 
 
@@ -239,6 +239,7 @@
 4. Use Git checkpoints
 
     Codex can modify your codebase, so consider creating Git checkpoints before and after each task so you can easily revert changes if needed.
+    If you're new to Codex, read the [best practices guide](https://developers.openai.com/codex/learn/best-practices).
     
     <CtaPillLink href="/codex/ide" label="Learn more about the Codex IDE extension" class="mt-8" />
 </WorkflowSteps>
@@ -333,6 +334,7 @@
 4. Use Git checkpoints
 
     Codex can modify your codebase, so consider creating Git checkpoints before and after each task so you can easily revert changes if needed.
+    If you're new to Codex, read the [best practices guide](https://developers.openai.com/codex/learn/best-practices).
 </WorkflowSteps>
 
     <CtaPillLink href="/codex/cli" label="Learn more about the Codex CLI" class="mt-8" />
@@ -421,4 +423,23 @@
 </WorkflowSteps>
 
   </div>
-</Tabs>+</Tabs>
+
+<div class="h-6" aria-hidden="true"></div>
+
+## Next steps
+
+[<IconItem title="Learn more about the Codex app" className="mt-2">
+    <span slot="icon">
+      <OpenBook />
+    </span>
+    Use the Codex app to work with your local projects.
+  </IconItem>](https://developers.openai.com/codex/app)
+
+[<IconItem title="Migrate to Codex" className="mt-2">
+    <span slot="icon">
+      <CompareArrows />
+    </span>
+    Move supported instruction files, MCP server configuration, skills, and
+    subagents into Codex.
+  </IconItem>](https://developers.openai.com/codex/migrate)
```
#### https://developers.openai.com/codex/rules.md

```diff
--- a/https://developers.openai.com/codex/rules.md
+++ b/https://developers.openai.com/codex/rules.md
@@ -6,7 +6,7 @@
 
 ## Create a rules file
 
-1. Create a `.rules` file under `./codex/rules/` (for example, `~/.codex/rules/default.rules`).
+1. Create a `.rules` file under a `rules/` folder next to an active config layer (for example, `~/.codex/rules/default.rules`).
 2. Add a rule. This example prompts before allowing `gh pr view` to run outside the sandbox.
 
    ```python
@@ -37,7 +37,9 @@
 
 3. Restart Codex.
 
-Codex scans `rules/` under every [Team Config](https://developers.openai.com/codex/enterprise/admin-setup#team-config) location at startup. When you add a command to the allow list in the TUI, Codex writes to the user layer at `~/.codex/rules/default.rules` so future runs can skip the prompt.
+Codex scans `rules/` under every active config layer at startup, including [Team Config](https://developers.openai.com/codex/enterprise/admin-setup#team-config) locations and the user layer at `~/.codex/rules/`. Project-local rules under `<repo>/.codex/rules/` load only when the project `.codex/` layer is trusted.
+
+When you add a command to the allow list in the TUI, Codex writes to the user layer at `~/.codex/rules/default.rules` so future runs can skip the prompt.
 
 When Smart approvals are enabled (the default), Codex may propose a
 `prefix_rule` for you during escalation requests. Review the suggested prefix

```
#### https://developers.openai.com/codex/sdk.md

```diff
--- a/https://developers.openai.com/codex/sdk.md
+++ b/https://developers.openai.com/codex/sdk.md
@@ -11,7 +11,7 @@
 
 ## TypeScript library
 
-The TypeScript library provides a way to control Codex from within your application that is more comprehensive and flexible than non-interactive mode.
+The TypeScript library provides a way to control Codex from within your application that's more comprehensive and flexible than non-interactive mode.
 
 Use the library server-side; it requires Node.js 18 or later.
 
@@ -56,4 +56,52 @@
 console.log(result2);
 ```
 
-For more details, check out the [TypeScript repo](https://github.com/openai/codex/tree/main/sdk/typescript).+For more details, check out the [TypeScript repo](https://github.com/openai/codex/tree/main/sdk/typescript).
+
+## Python library
+
+The Python SDK is experimental and controls the local Codex app-server over JSON-RPC. It requires Python 3.10 or later and a local checkout of the open-source Codex repo.
+
+### Installation
+
+From the Codex repo root, install the SDK in editable mode:
+
+```bash
+cd sdk/python
+python -m pip install -e .
+```
+
+For manual local SDK usage, pass `AppServerConfig(codex_bin=...)` to point at a local `codex` binary, or use the repo examples and notebook bootstrap.
+
+### Usage
+
+Start Codex, create a thread, and run a prompt:
+
+```python
+from codex_app_server import Codex
+
+with Codex() as codex:
+    thread = codex.thread_start(model="gpt-5.4")
+    result = thread.run("Make a plan to diagnose and fix the CI failures")
+    print(result.final_response)
+```
+
+Use `AsyncCodex` when your application is already asynchronous:
+
+```python
+import asyncio
+
+from codex_app_server import AsyncCodex
+
+
+async def main() -> None:
+    async with AsyncCodex() as codex:
+        thread = await codex.thread_start(model="gpt-5.4")
+        result = await thread.run("Implement the plan")
+        print(result.final_response)
+
+
+asyncio.run(main())
+```
+
+For more details, check out the [Python repo](https://github.com/openai/codex/tree/main/sdk/python).
```
#### https://developers.openai.com/codex/security.md

```diff
--- a/https://developers.openai.com/codex/security.md
+++ b/https://developers.openai.com/codex/security.md
@@ -26,7 +26,7 @@
 
 ## Access and prerequisites
 
-Codex Security works with connected GitHub repositories through Codex cloud. OpenAI manages access. If you need access or a repository isn't visible, contact your OpenAI account team and confirm the repository is available through your Codex cloud workspace.
+Codex Security works with connected GitHub repositories through Codex Web. OpenAI manages access. If you need access or a repository isn't visible, contact your OpenAI account team and confirm the repository is available through your Codex Web workspace.
 
 ## Related docs
 

```
#### https://developers.openai.com/codex/skills.md

```diff
--- a/https://developers.openai.com/codex/skills.md
+++ b/https://developers.openai.com/codex/skills.md
@@ -1,10 +1,16 @@
 # Agent Skills
 
-Use agent skills to extend Codex with task-specific capabilities. A skill packages instructions, resources, and optional scripts so Codex can follow a workflow reliably. You can share skills across teams or with the community. Skills build on the [open agent skills standard](https://agentskills.io).
+Use agent skills to extend Codex with task-specific capabilities. A skill packages instructions, resources, and optional scripts so Codex can follow a workflow reliably. Skills build on the [open agent skills standard](https://agentskills.io).
+
+Skills are the authoring format for reusable workflows. Plugins are the installable distribution unit for reusable skills and apps in Codex. Use skills to design the workflow itself, then package it as a [plugin](https://developers.openai.com/codex/plugins/build) when you want other developers to install it.
 
 Skills are available in the Codex CLI, IDE extension, and Codex app.
 
-Skills use **progressive disclosure** to manage context efficiently: Codex starts with each skill's metadata (`name`, `description`, file path, and optional metadata from `agents/openai.yaml`). Codex loads the full `SKILL.md` instructions only when it decides to use a skill.
+Skills use **progressive disclosure** to manage context efficiently: Codex starts with each skill's name, description, and file path. Codex loads the full `SKILL.md` instructions only when it decides to use a skill.
+
+Codex includes an initial list of available skills in context so it can choose the right skill for a task. To avoid crowding out the rest of the prompt, this list is capped at roughly 2% of the model’s context window, or 8,000 characters when the context window is unknown. If many skills are installed, Codex shortens skill descriptions first. For very large skill sets, some skills may be omitted from the initial list, and Codex will show a warning.
+
+This budget applies only to the initial skills list. When Codex selects a skill, it still reads the full SKILL.md instructions for that skill.
 
 A skill is a directory with a `SKILL.md` file plus optional scripts and references. The `SKILL.md` file must include `name` and `description`.
 
@@ -54,7 +60,7 @@
 1. **Explicit invocation:** Include the skill directly in your prompt. In CLI/IDE, run `/skills` or type `$` to mention a skill.
 2. **Implicit invocation:** Codex can choose a skill when your task matches the skill `description`.
 
-Because implicit matching depends on `description`, write descriptions with clear scope and boundaries.
+Because implicit matching depends on `description`, write concise descriptions with clear scope and boundaries. Front-load the key use case and trigger words so Codex can still match the skill if descriptions are shortened.
 
 ## Create a skill
 
@@ -94,15 +100,35 @@
 
 Codex supports symlinked skill folders and follows the symlink target when scanning these locations.
 
-## Install skills
+These locations are for authoring and local discovery. When you want to
+distribute reusable skills beyond a single repo, or optionally bundle them with
+app integrations, use [plugins](https://developers.openai.com/codex/plugins/build).
 
-To install skills beyond the built-ins, use `$skill-installer`. For example, to install the `$linear` skill:
+## Distribute skills with plugins
+
+Direct skill folders are best for local authoring and repo-scoped workflows. If
+you want to distribute a reusable skill, bundle two or more skills together, or
+ship a skill alongside an app integration, package them as a
+[plugin](https://developers.openai.com/codex/plugins/build).
+
+Plugins can include one or more skills. They can also optionally bundle app
+mappings, MCP server configuration, and presentation assets in a single
+package.
+
+## Install curated skills for local use
+
+To add curated skills beyond the built-ins for your own local Codex setup, use `$skill-installer`. For example, to install the `$linear` skill:
 
 ```bash
 $skill-installer linear
 ```
 
-You can also prompt the installer to download skills from other repositories. Codex detects newly installed skills automatically; if one doesn't appear, restart Codex.
+You can also prompt the installer to download skills from other repositories.
+Codex detects newly installed skills automatically; if one doesn't appear,
+restart Codex.
+
+Use this for local setup and experimentation. For reusable distribution of your
+own skills, prefer plugins.
 
 ## Enable or disable skills
 

```
#### https://developers.openai.com/codex/speed.md

```diff
--- a/https://developers.openai.com/codex/speed.md
+++ b/https://developers.openai.com/codex/speed.md
@@ -5,11 +5,17 @@
 Codex offers the ability to increase the speed of the model for increased
 credit consumption.
 
-Fast mode is currently supported on GPT-5.4. When enabled, speed is increased
-by 1.5x and credits are consumed at a 2x rate.
+Fast mode increases supported model speed by 1.5x and consumes credits at a
+higher rate than Standard mode. It currently supports GPT-5.5 and GPT-5.4,
+consuming credits at 2.5x the Standard rate for GPT-5.5 and 2x the Standard
+rate for GPT-5.4.
 
-Enable it by typing `/fast`. It is available in Codex IDE Extensions, Codex
-CLI, and the Codex app.
+Use `/fast on`, `/fast off`, or `/fast status` in the CLI to change or inspect
+the current setting. You can also persist the default with `service_tier =
+"fast"` plus `[features].fast_mode = true` in `config.toml`. Fast mode is
+available in the Codex IDE extension, Codex CLI, and the Codex app when you
+sign in with ChatGPT. With an API key, Codex uses standard API pricing instead
+and you can't use Fast mode credits.
 
 <VideoPlayer
   src="/videos/codex/fast-mode-demo.mp4"
@@ -18,7 +24,9 @@
 
 ## Codex-Spark
 
-GPT-5.3-Codex-Spark is a separate fast, less-capable Codex model optimized for near-instant, real-time coding iteration. Unlike fast mode, which speeds up GPT-5.4 at a higher credit rate,
-Codex-Spark is its own model choice and has its own usage limits.
+GPT-5.3-Codex-Spark is a separate fast, less-capable Codex model optimized for
+near-instant, real-time coding iteration. Unlike fast mode, which speeds up a
+supported model at a higher credit rate, Codex-Spark is its own model choice
+and has its own usage limits.
 
 During research preview Codex-Spark is only available for ChatGPT Pro subscribers.
```
#### https://developers.openai.com/codex/windows.md

```diff
--- a/https://developers.openai.com/codex/windows.md
+++ b/https://developers.openai.com/codex/windows.md
@@ -1,6 +1,11 @@
 # Windows
 
-The easiest way to use Codex on Windows is to use the [Codex app](https://developers.openai.com/codex/app/windows). You can also [set up the IDE extension](https://developers.openai.com/codex/ide) or [install the CLI](https://developers.openai.com/codex/cli) and run it from PowerShell.
+Use Codex on Windows with the native [Codex app](https://developers.openai.com/codex/app/windows), the
+[CLI](https://developers.openai.com/codex/cli), or the [IDE extension](https://developers.openai.com/codex/ide).
+
+The Codex app on Windows supports core workflows such as parallel agent threads,
+worktrees, automations, Git functionality, the in-app browser, artifact previews,
+plugins, and skills.
 
 <div class="mb-8">
   <CodexCallout
@@ -11,24 +16,71 @@
   />
 </div>
 
-When you run Codex natively on Windows, agent mode uses a [Windows sandbox](#windows-sandbox) to block filesystem writes outside the working folder and prevent network access without your explicit approval. [Learn more below](#windows-sandbox).
-
-If you prefer to have Codex use [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install) (WSL2), [read the instructions](#windows-subsystem-for-linux) below.
+Depending on the surface and your setup, Codex can run on Windows in three
+practical ways:
+
+- natively on Windows with the stronger `elevated` sandbox,
+- natively on Windows with the fallback `unelevated` sandbox,
+- or inside [Windows Subsystem for Linux 2](https://learn.microsoft.com/en-us/windows/wsl/install) (WSL2), which uses the Linux sandbox implementation.
 
 ## Windows sandbox
 
-Native Windows sandbox support includes two modes that you can configure in `config.toml`:
+When you run Codex natively on Windows, agent mode uses a Windows sandbox to
+block filesystem writes outside the working folder and prevent network access
+without your explicit approval.
+
+Native Windows sandbox support includes two modes that you can configure in
+`config.toml`:
 
 ```toml
 [windows]
-sandbox = "unelevated" # or "elevated"
-```
-
-How `elevated` mode works:
-
-- Uses a Restricted Token approach with filesystem ACLs to limit which files the sandbox can write to.
-- Runs commands as a dedicated Windows Sandbox User.
-- Limits network access by installing Windows Firewall rules.
+sandbox = "elevated" # or "unelevated"
+```
+
+`elevated` is the preferred native Windows sandbox. It uses dedicated
+lower-privilege sandbox users, filesystem permission boundaries, firewall
+rules, and local policy changes needed for commands that run in the sandbox.
+
+`unelevated` is the fallback native Windows sandbox. It runs commands with a
+restricted Windows token derived from your current user, applies ACL-based
+filesystem boundaries, and uses environment-level offline controls instead of
+the dedicated offline-user firewall rule. It's weaker than `elevated`, but it
+is still useful when administrator-approved setup is blocked by local or
+enterprise policy.
+
+If both modes are available, use `elevated`. If the default native sandbox
+doesn't work in your environment, use `unelevated` as a fallback while you
+troubleshoot the setup.
+
+By default, both sandbox modes also use a private desktop for stronger UI
+isolation. Set `windows.sandbox_private_desktop = false` only if you need the
+older `Winsta0\\Default` behavior for compatibility.
+
+### Sandbox permissions
+
+Running Codex in full access mode means Codex is not limited to your project
+  directory and might perform unintentional destructive actions that can lead to
+  data loss. For safer automation, keep sandbox boundaries in place and use
+  [rules](https://developers.openai.com/codex/rules) for specific exceptions, or set your [approval policy to
+  never](https://developers.openai.com/codex/agent-approvals-security#run-without-approval-prompts) to have
+  Codex attempt to solve problems without asking for escalated permissions,
+  based on your [approval and security setup](https://developers.openai.com/codex/agent-approvals-security).
+
+### Windows version matrix
+
+| Windows version                  | Support level   | Notes                                                                                                                                                                                 |
+| -------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
+| Windows 11                       | Recommended     | Best baseline for Codex on Windows. Use this if you are standardizing an enterprise deployment.                                                                                       |
+| Recent, fully updated Windows 10 | Best effort     | Can work, but is less reliable than Windows 11. For Windows 10, Codex depends on modern console support, including ConPTY. In practice, Windows 10 version 1809 or newer is required. |
+| Older Windows 10 builds          | Not recommended | More likely to miss required console components such as ConPTY and more likely to fail in enterprise setups.                                                                          |
+
+Additional environment assumptions:
+
+- `winget` should be available. If it's missing, update Windows or install
+  the Windows Package Manager before setting up Codex.
+- The recommended native sandbox depends on administrator-approved setup.
+- Some enterprise-managed devices block the required setup steps even when the
+  OS version itself is acceptable.
 
 ### Grant sandbox read access
 
@@ -40,7 +92,19 @@
 
 The path must be an existing absolute directory. After the command succeeds, later commands that run in the sandbox can read that directory during the current session.
 
+Use the native Windows sandbox by default. The native Windows sandbox offers the best performance and highest speeds while keeping the same security. Choose WSL2 when you
+need a Linux-native environment on Windows, when your workflow already lives in
+WSL2, or when neither native Windows sandbox mode meets your needs.
+
 ## Windows Subsystem for Linux
+
+If you choose WSL2, Codex runs inside the Linux environment instead of using the
+native Windows sandbox. This is useful if you need Linux-native tooling on
+Windows, if your repositories and developer workflow already live in WSL2, or
+if neither native Windows sandbox mode works for your environment.
+
+WSL1 was supported through Codex `0.114`. Starting in Codex `0.115`, the Linux
+sandbox moved to `bubblewrap`, so WSL1 is no longer supported.
 
 ### Launch VS Code from inside WSL
 
@@ -76,6 +140,10 @@
 If you don't see "WSL: ..." in the status bar, press `Ctrl+Shift+P`, pick
   `WSL: Reopen Folder in WSL`, and keep your repository under `/home/...` (not
   `C:\`) for best performance.
+
+If the Windows app or project picker does not show your WSL repository, type
+  <code>\\wsl$</code> into the file picker or Explorer, then navigate to your
+  distro's home directory.
 
 ### Use Codex CLI with WSL
 
@@ -116,7 +184,132 @@
 
 ## Troubleshooting and FAQ
 
-#### Installed extension, but it's unresponsive
+If you are troubleshooting a managed Windows machine, start with the native
+sandbox mode, Windows version, and any policy error shown by Codex. Most native
+Windows support issues come from sandbox setup, logon rights, or filesystem
+permissions rather than from the editor itself.
+
+My native sandbox setup failed
+
+If Codex cannot complete the `elevated` sandbox setup, the most common causes
+are:
+
+- the Windows UAC or administrator prompt was declined,
+- the machine does not allow local user or group creation,
+- the machine does not allow firewall rule changes,
+- the machine blocks the logon rights needed by the sandbox users,
+- or another enterprise policy blocks part of the setup flow.
+
+What to try:
+
+1. Try the `elevated` sandbox setup again and approve the administrator prompt
+   if your environment allows it.
+2. If your company laptop blocks this, ask your IT team whether the machine
+   allows administrator-approved setup for local user/group creation, firewall
+   configuration, and the required sandbox-user logon rights.
+3. If the default setup still fails, use the `unelevated` sandbox so you can
+   continue working while the issue is investigated.
+
+Codex switched me to the unelevated sandbox
+
+This means Codex could not finish the stronger `elevated` sandbox setup on your
+machine.
+
+- Codex can still run in a sandboxed mode.
+- It still applies ACL-based filesystem boundaries, but it does not use the
+  separate sandbox-user boundary from `elevated` and has weaker network
+  isolation.
+- This is a useful fallback, but not the preferred long-term enterprise
+  configuration.
+
+If you are on a managed enterprise laptop, the best long-term fix is usually to
+get the `elevated` sandbox working with help from your IT team.
+
+I see Windows error 1385
+
+If sandboxed commands fail with error `1385`, Windows is denying the logon type
+the sandbox user needs in order to start the command.
+
+In practice, this usually means Codex created the sandbox users successfully,
+but Windows policy is still preventing those users from launching sandboxed
+commands.
+
+What to do:
+
+1. Ask your IT team whether the device policy grants the required logon rights
+   to the Codex-created sandbox users.
+2. Compare group policy or OU differences if the issue affects only some
+   machines or teams.
+3. If you need to keep working immediately, use the `unelevated` sandbox while
+   the policy issue is investigated.
+4. Send `CODEX_HOME/.sandbox/sandbox.log` along with your Windows version and a
+   short description of the failure.
+
+Codex warns that some folders are writable by Everyone
+
+Codex may warn that some folders are writable by `Everyone`.
+
+If you see this warning, Windows permissions on those folders are too broad for
+the sandbox to fully protect them.
+
+What to do:
+
+1. Review the folders Codex lists in the warning.
+2. Remove `Everyone` write access from those folders if that is appropriate in
+   your environment.
+3. Restart Codex or re-run the sandbox setup after those permissions are
+   corrected.
+
+If you are not sure how to change those permissions, ask your IT team for help.
+
+Sandboxed commands cannot reach the network
+
+Some Codex tasks are intentionally run without outbound network access,
+depending on the permissions mode in use.
+
+If a task fails because it cannot reach the network:
+
+1. Check whether the task was supposed to run with network disabled.
+2. If you expected network access, restart Codex and try again.
+3. If the issue keeps happening, collect the sandbox log so the team can check
+   whether the machine is in a partial or broken sandbox state.
+
+Sandboxing worked before and then stopped
+
+This can happen after:
+
+- moving a repo or workspace,
+- changing machine permissions,
+- changing Windows policies,
+- or other system configuration changes.
+
+What to try:
+
+1. Restart Codex.
+2. Try the `elevated` sandbox setup again.
+3. If that does not fix it, use the `unelevated` sandbox as a temporary
+   fallback.
+4. Collect the sandbox log for review.
+
+I need to send diagnostics to OpenAI
+
+If you still have problems, send:
+
+- `CODEX_HOME/.sandbox/sandbox.log`
+
+It is also helpful to include:
+
+- a short description of what you were trying to do,
+- whether the `elevated` sandbox failed or the `unelevated` sandbox was used,
+- any error message shown in the app,
+- whether you saw `1385` or another Windows or PowerShell error,
+- and whether you are on Windows 11 or Windows 10.
+
+Do not send:
+
+- the contents of `CODEX_HOME/.sandbox-secrets/`
+
+The IDE extension is installed but unresponsive
 
 Your system may be missing C++ development tools, which some native dependencies require:
 
@@ -126,7 +319,7 @@
 
 Then fully restart VS Code after installation.
 
-#### If it feels slow on large repositories
+Large repositories feel slow in WSL
 
 - Make sure you're not working under <code>/mnt/c</code>. Move the repository to WSL (for example, <code>~/code/...</code>).
 - Increase memory and CPU for WSL if needed; update WSL to the latest version:
@@ -135,7 +328,7 @@
   wsl --shutdown
   ```
 
-#### VS Code in WSL can't find `codex`
+VS Code in WSL cannot find codex
 
 Verify the binary exists and is on PATH inside WSL:
 

```

---

## 2026-05-10 19:58:46 UTC

| Metric | Count |
|--------|------:|
| Changed | 0 |
| Added | 0 |
| Removed | 0 |
| Errors | 0 |

---

## 2026-05-10 20:01:41 UTC

| Metric | Count |
|--------|------:|
| Changed | 0 |
| Added | 0 |
| Removed | 0 |
| Errors | 0 |

---

## 2026-05-10 20:03:31 UTC

| Metric | Count |
|--------|------:|
| Changed | 0 |
| Added | 0 |
| Removed | 0 |
| Errors | 0 |
