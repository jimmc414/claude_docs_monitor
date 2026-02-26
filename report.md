# Claude Docs Monitor Report

*Generated: 2026-02-26 20:46:59 UTC*

| Metric | Count |
|--------|------:|
| Changed | 37 |
| Added | 1 |
| Removed | 0 |
| Errors | 0 |

## Added Pages

- https://code.claude.com/docs/en/remote-control.md

## Diffs

### https://code.claude.com/docs/en/agent-teams.md

```diff
--- a/https://code.claude.com/docs/en/agent-teams.md
+++ b/https://code.claude.com/docs/en/agent-teams.md
@@ -70,7 +70,7 @@
 
 This example works well because the three roles are independent and can explore the problem without waiting on each other:
 
-```
+```text  theme={null}
 I'm designing a CLI tool that helps developers track TODO comments across
 their codebase. Create an agent team to explore this from different angles: one
 teammate on UX, one on technical architecture, one playing devil's advocate.
@@ -120,7 +120,7 @@
 
 Claude decides the number of teammates to spawn based on your task, or you can specify exactly what you want:
 
-```
+```text  theme={null}
 Create a team with 4 teammates to refactor these modules in parallel.
 Use Sonnet for each teammate.
 ```
@@ -129,7 +129,7 @@
 
 For complex or risky tasks, you can require teammates to plan before implementing. The teammate works in read-only plan mode until the lead approves their approach:
 
-```
+```text  theme={null}
 Spawn an architect teammate to refactor the authentication module.
 Require plan approval before they make any changes.
 ```
@@ -160,7 +160,7 @@
 
 To gracefully end a teammate's session:
 
-```
+```text  theme={null}
 Ask the researcher teammate to shut down
 ```
 
@@ -170,7 +170,7 @@
 
 When you're done, ask the lead to clean up:
 
-```
+```text  theme={null}
 Clean up the team
 ```
 
@@ -253,7 +253,7 @@
 
 A single reviewer tends to gravitate toward one type of issue at a time. Splitting review criteria into independent domains means security, performance, and test coverage all get thorough attention simultaneously. The prompt assigns each teammate a distinct lens so they don't overlap:
 
-```
+```text  theme={null}
 Create an agent team to review PR #142. Spawn three reviewers:
 - One focused on security implications
 - One checking performance impact
@@ -267,7 +267,7 @@
 
 When the root cause is unclear, a single agent tends to find one plausible explanation and stop looking. The prompt fights this by making teammates explicitly adversarial: each one's job is not only to investigate its own theory but to challenge the others'.
 
-```
+```text  theme={null}
 Users report the app exits after one message instead of staying connected.
 Spawn 5 agent teammates to investigate different hypotheses. Have them talk to
 each other to try to disprove each other's theories, like a scientific
@@ -284,13 +284,27 @@
 
 Teammates load project context automatically, including CLAUDE.md, MCP servers, and skills, but they don't inherit the lead's conversation history. See [Context and communication](#context-and-communication) for details. Include task-specific details in the spawn prompt:
 
-```
+```text  theme={null}
 Spawn a security reviewer teammate with the prompt: "Review the authentication module
 at src/auth/ for security vulnerabilities. Focus on token handling, session
 management, and input validation. The app uses JWT tokens stored in
 httpOnly cookies. Report any issues with severity ratings."
 ```
 
+### Choose an appropriate team size
+
+There's no hard limit on the number of teammates, but practical constraints apply:
+
+* **Token costs scale linearly**: each teammate has its own context window and consumes tokens independently. See [agent team token costs](/en/costs#agent-team-token-costs) for details.
+* **Coordination overhead increases**: more teammates means more communication, task coordination, and potential for conflicts
+* **Diminishing returns**: beyond a certain point, additional teammates don't speed up work proportionally
+
+Start with 3-5 teammates for most workflows. This balances parallel work with manageable coordination. The examples in this guide use 3-5 teammates because that range works well across different task types.
+
+Having 5-6 [tasks](/en/agent-teams#architecture) per teammate keeps everyone productive without excessive context switching. If you have 15 independent tasks, 3 teammates is a good starting point.
+
+Scale up only when the work genuinely benefits from having teammates work simultaneously. Three focused teammates often outperform five scattered ones.
+
 ### Size tasks appropriately
 
 * **Too small**: coordination overhead exceeds the benefit
@@ -305,7 +319,7 @@
 
 Sometimes the lead starts implementing tasks itself instead of waiting for teammates. If you notice this:
 
-```
+```text  theme={null}
 Wait for your teammates to complete their tasks before proceeding
 ```
 

```
### https://code.claude.com/docs/en/common-workflows.md

```diff
--- a/https://code.claude.com/docs/en/common-workflows.md
+++ b/https://code.claude.com/docs/en/common-workflows.md
@@ -644,27 +644,31 @@
 
 When working on multiple tasks at once, you need each Claude session to have its own copy of the codebase so changes don't collide. Git worktrees solve this by creating separate working directories that each have their own files and branch, while sharing the same repository history and remote connections. This means you can have Claude working on a feature in one worktree while fixing a bug in another, without either session interfering with the other.
 
-Use the `--worktree` flag to create an isolated worktree and start Claude in it. The value you pass becomes the worktree directory name and branch name:
+Use the `--worktree` (`-w`) flag to create an isolated worktree and start Claude in it. The value you pass becomes the worktree directory name and branch name:
 
 ```bash  theme={null}
 # Start Claude in a worktree named "feature-auth"
 # Creates .claude/worktrees/feature-auth/ with a new branch
-claude -w feature-auth
+claude --worktree feature-auth
 
 # Start another session in a separate worktree
-claude -w bugfix-123
+claude --worktree bugfix-123
 ```
 
 If you omit the name, Claude generates a random one automatically:
 
 ```bash  theme={null}
 # Auto-generates a name like "bright-running-fox"
-claude -w
+claude --worktree
 ```
 
 Worktrees are created at `<repo>/.claude/worktrees/<name>` and branch from the default remote branch. The worktree branch is named `worktree-<name>`.
 
 You can also ask Claude to "work in a worktree" or "start a worktree" during a session, and it will create one automatically.
+
+### Subagent worktrees
+
+Subagents can also use worktree isolation to work in parallel without conflicts. Ask Claude to "use worktrees for your agents" or configure it in a [custom subagent](/en/sub-agents#supported-frontmatter-fields) by adding `isolation: worktree` to the agent's frontmatter. Each subagent gets its own worktree that is automatically cleaned up when the subagent finishes without changes.
 
 ### Worktree cleanup
 
@@ -703,6 +707,10 @@
 <Tip>
   Remember to initialize your development environment in each new worktree according to your project's setup. Depending on your stack, this might include running dependency installation (`npm install`, `yarn`), setting up virtual environments, or following your project's standard setup process.
 </Tip>
+
+### Non-git version control
+
+Worktree isolation works with git by default. For other version control systems like SVN, Perforce, or Mercurial, configure [WorktreeCreate and WorktreeRemove hooks](/en/hooks#worktreecreate) to provide custom worktree creation and cleanup logic. When configured, these hooks replace the default git behavior when you use `--worktree`.
 
 For automated coordination of parallel sessions with shared tasks and messaging, see [agent teams](/en/agent-teams).
 

```
### https://code.claude.com/docs/en/plugins-reference.md

```diff
--- a/https://code.claude.com/docs/en/plugins-reference.md
+++ b/https://code.claude.com/docs/en/plugins-reference.md
@@ -26,7 +26,7 @@
 
 **Skill structure**:
 
-```
+```text  theme={null}
 skills/
 ├── pdf-processor/
 │   ├── SKILL.md
@@ -250,12 +250,12 @@
 
 When you install a plugin, you choose a **scope** that determines where the plugin is available and who else can use it:
 
-| Scope     | Settings file                 | Use case                                                 |
-| :-------- | :---------------------------- | :------------------------------------------------------- |
-| `user`    | `~/.claude/settings.json`     | Personal plugins available across all projects (default) |
-| `project` | `.claude/settings.json`       | Team plugins shared via version control                  |
-| `local`   | `.claude/settings.local.json` | Project-specific plugins, gitignored                     |
-| `managed` | `managed-settings.json`       | Managed plugins (read-only, update only)                 |
+| Scope     | Settings file                                   | Use case                                                 |
+| :-------- | :---------------------------------------------- | :------------------------------------------------------- |
+| `user`    | `~/.claude/settings.json`                       | Personal plugins available across all projects (default) |
+| `project` | `.claude/settings.json`                         | Team plugins shared via version control                  |
+| `local`   | `.claude/settings.local.json`                   | Project-specific plugins, gitignored                     |
+| `managed` | [Managed settings](/en/settings#settings-files) | Managed plugins (read-only, update only)                 |
 
 Plugins use the same scope system as other Claude Code configurations. For installation instructions and scope flags, see [Install plugins](/en/discover-plugins#install-plugins). For a complete explanation of scopes, see [Configuration scopes](/en/settings#configuration-scopes).
 
@@ -408,7 +408,7 @@
 
 A complete plugin follows this structure:
 
-```
+```text  theme={null}
 enterprise-plugin/
 ├── .claude-plugin/           # Metadata directory (optional)
 │   └── plugin.json             # plugin manifest
@@ -650,7 +650,7 @@
 
 **Correct structure**: Components must be at the plugin root, not inside `.claude-plugin/`. Only `plugin.json` belongs in `.claude-plugin/`.
 
-```
+```text  theme={null}
 my-plugin/
 ├── .claude-plugin/
 │   └── plugin.json      ← Only manifest here

```
### https://code.claude.com/docs/en/hooks.md

```diff
--- a/https://code.claude.com/docs/en/hooks.md
+++ b/https://code.claude.com/docs/en/hooks.md
@@ -18,29 +18,31 @@
 
 <div style={{maxWidth: "500px", margin: "0 auto"}}>
   <Frame>
-    <img src="https://mintcdn.com/claude-code/xcAz1d2i2To-I_QJ/images/hooks-lifecycle.svg?fit=max&auto=format&n=xcAz1d2i2To-I_QJ&q=85&s=783a0db47dd59602418763e037056d49" alt="Hook lifecycle diagram showing the sequence of hooks from SessionStart through the agentic loop to SessionEnd" data-og-width="520" width="520" data-og-height="960" height="960" data-path="images/hooks-lifecycle.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/claude-code/xcAz1d2i2To-I_QJ/images/hooks-lifecycle.svg?w=280&fit=max&auto=format&n=xcAz1d2i2To-I_QJ&q=85&s=1fd947ad1c8fc4fcfbe85c8b4b7b528b 280w, https://mintcdn.com/claude-code/xcAz1d2i2To-I_QJ/images/hooks-lifecycle.svg?w=560&fit=max&auto=format&n=xcAz1d2i2To-I_QJ&q=85&s=794ba776ed6126344835c206f587c9dd 560w, https://mintcdn.com/claude-code/xcAz1d2i2To-I_QJ/images/hooks-lifecycle.svg?w=840&fit=max&auto=format&n=xcAz1d2i2To-I_QJ&q=85&s=d137272c869dd6f9315ec35f99338289 840w, https://mintcdn.com/claude-code/xcAz1d2i2To-I_QJ/images/hooks-lifecycle.svg?w=1100&fit=max&auto=format&n=xcAz1d2i2To-I_QJ&q=85&s=531c5f866a6fd56adf94ecfa156ac96a 1100w, https://mintcdn.com/claude-code/xcAz1d2i2To-I_QJ/images/hooks-lifecycle.svg?w=1650&fit=max&auto=format&n=xcAz1d2i2To-I_QJ&q=85&s=dc81c6d273cd26cd7f9a191ddcb92592 1650w, https://mintcdn.com/claude-code/xcAz1d2i2To-I_QJ/images/hooks-lifecycle.svg?w=2500&fit=max&auto=format&n=xcAz1d2i2To-I_QJ&q=85&s=8f29af9b4145e517655a8bdf7a9987c5 2500w" />
+    <img src="https://mintcdn.com/claude-code/rsuu-ovdPNos9Dnn/images/hooks-lifecycle.svg?fit=max&auto=format&n=rsuu-ovdPNos9Dnn&q=85&s=ce5f1225339bbccdfbb52e99205db912" alt="Hook lifecycle diagram showing the sequence of hooks from SessionStart through the agentic loop to SessionEnd, with WorktreeCreate and WorktreeRemove as standalone setup and teardown events" data-og-width="520" width="520" data-og-height="1020" height="1020" data-path="images/hooks-lifecycle.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/claude-code/rsuu-ovdPNos9Dnn/images/hooks-lifecycle.svg?w=280&fit=max&auto=format&n=rsuu-ovdPNos9Dnn&q=85&s=7c7143c65492c1beb6bc66f5d206ba15 280w, https://mintcdn.com/claude-code/rsuu-ovdPNos9Dnn/images/hooks-lifecycle.svg?w=560&fit=max&auto=format&n=rsuu-ovdPNos9Dnn&q=85&s=dafaebf8f789f94edbf6bd66853c69df 560w, https://mintcdn.com/claude-code/rsuu-ovdPNos9Dnn/images/hooks-lifecycle.svg?w=840&fit=max&auto=format&n=rsuu-ovdPNos9Dnn&q=85&s=2caa51d2d95596f1f80b92e3f5f534fa 840w, https://mintcdn.com/claude-code/rsuu-ovdPNos9Dnn/images/hooks-lifecycle.svg?w=1100&fit=max&auto=format&n=rsuu-ovdPNos9Dnn&q=85&s=614def559f34f9b0c1dec93739d96b64 1100w, https://mintcdn.com/claude-code/rsuu-ovdPNos9Dnn/images/hooks-lifecycle.svg?w=1650&fit=max&auto=format&n=rsuu-ovdPNos9Dnn&q=85&s=ca45b85fdd8b2da81c69d12c453230cb 1650w, https://mintcdn.com/claude-code/rsuu-ovdPNos9Dnn/images/hooks-lifecycle.svg?w=2500&fit=max&auto=format&n=rsuu-ovdPNos9Dnn&q=85&s=7fd92d6b9713493f59962c9f295c9d2f 2500w" />
   </Frame>
 </div>
 
 The table below summarizes when each event fires. The [Hook events](#hook-events) section documents the full input schema and decision control options for each one.
 
-| Event                | When it fires                                                      |
-| :------------------- | :----------------------------------------------------------------- |
-| `SessionStart`       | When a session begins or resumes                                   |
-| `UserPromptSubmit`   | When you submit a prompt, before Claude processes it               |
-| `PreToolUse`         | Before a tool call executes. Can block it                          |
-| `PermissionRequest`  | When a permission dialog appears                                   |
-| `PostToolUse`        | After a tool call succeeds                                         |
-| `PostToolUseFailure` | After a tool call fails                                            |
-| `Notification`       | When Claude Code sends a notification                              |
-| `SubagentStart`      | When a subagent is spawned                                         |
-| `SubagentStop`       | When a subagent finishes                                           |
-| `Stop`               | When Claude finishes responding                                    |
-| `TeammateIdle`       | When an [agent team](/en/agent-teams) teammate is about to go idle |
-| `TaskCompleted`      | When a task is being marked as completed                           |
-| `ConfigChange`       | When a configuration file changes during a session                 |
-| `PreCompact`         | Before context compaction                                          |
-| `SessionEnd`         | When a session terminates                                          |
+| Event                | When it fires                                                                                               |
+| :------------------- | :---------------------------------------------------------------------------------------------------------- |
+| `SessionStart`       | When a session begins or resumes                                                                            |
+| `UserPromptSubmit`   | When you submit a prompt, before Claude processes it                                                        |
+| `PreToolUse`         | Before a tool call executes. Can block it                                                                   |
+| `PermissionRequest`  | When a permission dialog appears                                                                            |
+| `PostToolUse`        | After a tool call succeeds                                                                                  |
+| `PostToolUseFailure` | After a tool call fails                                                                                     |
+| `Notification`       | When Claude Code sends a notification                                                                       |
+| `SubagentStart`      | When a subagent is spawned                                                                                  |
+| `SubagentStop`       | When a subagent finishes                                                                                    |
+| `Stop`               | When Claude finishes responding                                                                             |
+| `TeammateIdle`       | When an [agent team](/en/agent-teams) teammate is about to go idle                                          |
+| `TaskCompleted`      | When a task is being marked as completed                                                                    |
+| `ConfigChange`       | When a configuration file changes during a session                                                          |
+| `WorktreeCreate`     | When a worktree is being created via `--worktree` or `isolation: "worktree"`. Replaces default git behavior |
+| `WorktreeRemove`     | When a worktree is being removed, either at session exit or when a subagent finishes                        |
+| `PreCompact`         | Before context compaction                                                                                   |
+| `SessionEnd`         | When a session terminates                                                                                   |
 
 ### How a hook resolves
 
@@ -159,17 +161,17 @@
 
 The `matcher` field is a regex string that filters when hooks fire. Use `"*"`, `""`, or omit `matcher` entirely to match all occurrences. Each event type matches on a different field:
 
-| Event                                                                  | What the matcher filters  | Example matcher values                                                             |
-| :--------------------------------------------------------------------- | :------------------------ | :--------------------------------------------------------------------------------- |
-| `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest` | tool name                 | `Bash`, `Edit\|Write`, `mcp__.*`                                                   |
-| `SessionStart`                                                         | how the session started   | `startup`, `resume`, `clear`, `compact`                                            |
-| `SessionEnd`                                                           | why the session ended     | `clear`, `logout`, `prompt_input_exit`, `bypass_permissions_disabled`, `other`     |
-| `Notification`                                                         | notification type         | `permission_prompt`, `idle_prompt`, `auth_success`, `elicitation_dialog`           |
-| `SubagentStart`                                                        | agent type                | `Bash`, `Explore`, `Plan`, or custom agent names                                   |
-| `PreCompact`                                                           | what triggered compaction | `manual`, `auto`                                                                   |
-| `SubagentStop`                                                         | agent type                | same values as `SubagentStart`                                                     |
-| `ConfigChange`                                                         | configuration source      | `user_settings`, `project_settings`, `local_settings`, `policy_settings`, `skills` |
-| `UserPromptSubmit`, `Stop`, `TeammateIdle`, `TaskCompleted`            | no matcher support        | always fires on every occurrence                                                   |
+| Event                                                                                           | What the matcher filters  | Example matcher values                                                             |
+| :---------------------------------------------------------------------------------------------- | :------------------------ | :--------------------------------------------------------------------------------- |
+| `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`                          | tool name                 | `Bash`, `Edit\|Write`, `mcp__.*`                                                   |
+| `SessionStart`                                                                                  | how the session started   | `startup`, `resume`, `clear`, `compact`                                            |
+| `SessionEnd`                                                                                    | why the session ended     | `clear`, `logout`, `prompt_input_exit`, `bypass_permissions_disabled`, `other`     |
+| `Notification`                                                                                  | notification type         | `permission_prompt`, `idle_prompt`, `auth_success`, `elicitation_dialog`           |
+| `SubagentStart`                                                                                 | agent type                | `Bash`, `Explore`, `Plan`, or custom agent names                                   |
+| `PreCompact`                                                                                    | what triggered compaction | `manual`, `auto`                                                                   |
+| `SubagentStop`                                                                                  | agent type                | same values as `SubagentStart`                                                     |
+| `ConfigChange`                                                                                  | configuration source      | `user_settings`, `project_settings`, `local_settings`, `policy_settings`, `skills` |
+| `UserPromptSubmit`, `Stop`, `TeammateIdle`, `TaskCompleted`, `WorktreeCreate`, `WorktreeRemove` | no matcher support        | always fires on every occurrence                                                   |
 
 The matcher is a regex, so `Edit|Write` matches either tool and `Notebook.*` matches any tool starting with Notebook. The matcher runs against a field from the [JSON input](#hook-input-and-output) that Claude Code sends to your hook on stdin. For tool events, that field is `tool_name`. Each [hook event](#hook-events) section lists the full set of matcher values and the input schema for that event.
 
@@ -193,7 +195,7 @@
 }
 ```
 
-`UserPromptSubmit` and `Stop` don't support matchers and always fire on every occurrence. If you add a `matcher` field to these events, it is silently ignored.
+`UserPromptSubmit`, `Stop`, `TeammateIdle`, `TaskCompleted`, `WorktreeCreate`, and `WorktreeRemove` don't support matchers and always fire on every occurrence. If you add a `matcher` field to these events, it is silently ignored.
 
 #### Match MCP tools
 
@@ -463,6 +465,8 @@
 | `SessionStart`       | No         | Shows stderr to user only                                                     |
 | `SessionEnd`         | No         | Shows stderr to user only                                                     |
 | `PreCompact`         | No         | Shows stderr to user only                                                     |
+| `WorktreeCreate`     | Yes        | Any non-zero exit code causes worktree creation to fail                       |
+| `WorktreeRemove`     | No         | Failures are logged in debug mode only                                        |
 
 ### JSON output
 
@@ -497,18 +501,20 @@
 
 Not every event supports blocking or controlling behavior through JSON. The events that do each use a different set of fields to express that decision. Use this table as a quick reference before writing a hook:
 
-| Events                                                                              | Decision pattern     | Key fields                                                        |
-| :---------------------------------------------------------------------------------- | :------------------- | :---------------------------------------------------------------- |
-| UserPromptSubmit, PostToolUse, PostToolUseFailure, Stop, SubagentStop, ConfigChange | Top-level `decision` | `decision: "block"`, `reason`                                     |
-| TeammateIdle, TaskCompleted                                                         | Exit code only       | Exit code 2 blocks the action, stderr is fed back as feedback     |
-| PreToolUse                                                                          | `hookSpecificOutput` | `permissionDecision` (allow/deny/ask), `permissionDecisionReason` |
-| PermissionRequest                                                                   | `hookSpecificOutput` | `decision.behavior` (allow/deny)                                  |
+| Events                                                                              | Decision pattern     | Key fields                                                                  |
+| :---------------------------------------------------------------------------------- | :------------------- | :-------------------------------------------------------------------------- |
+| UserPromptSubmit, PostToolUse, PostToolUseFailure, Stop, SubagentStop, ConfigChange | Top-level `decision` | `decision: "block"`, `reason`                                               |
+| TeammateIdle, TaskCompleted                                                         | Exit code only       | Exit code 2 blocks the action, stderr is fed back as feedback               |
+| PreToolUse                                                                          | `hookSpecificOutput` | `permissionDecision` (allow/deny/ask), `permissionDecisionReason`           |
+| PermissionRequest                                                                   | `hookSpecificOutput` | `decision.behavior` (allow/deny)                                            |
+| WorktreeCreate                                                                      | stdout path          | Hook prints absolute path to created worktree. Non-zero exit fails creation |
+| WorktreeRemove, Notification, SessionEnd, PreCompact                                | None                 | No decision control. Used for side effects like logging or cleanup          |
 
 Here are examples of each pattern in action:
 
 <Tabs>
   <Tab title="Top-level decision">
-    Used by `UserPromptSubmit`, `PostToolUse`, `PostToolUseFailure`, `Stop`, and `SubagentStop`. The only value is `"block"`. To allow the action to proceed, omit `decision` from your JSON, or exit 0 without any JSON at all:
+    Used by `UserPromptSubmit`, `PostToolUse`, `PostToolUseFailure`, `Stop`, `SubagentStop`, and `ConfigChange`. The only value is `"block"`. To allow the action to proceed, omit `decision` from your JSON, or exit 0 without any JSON at all:
 
     ```json  theme={null}
     {
@@ -1308,6 +1314,92 @@
 
 `policy_settings` changes cannot be blocked. Hooks still fire for `policy_settings` sources, so you can use them for audit logging, but any blocking decision is ignored. This ensures enterprise-managed settings always take effect.
 
+### WorktreeCreate
+
+When you run `claude --worktree` or a [subagent uses `isolation: "worktree"`](/en/sub-agents#choose-the-subagent-scope), Claude Code creates an isolated working copy using `git worktree`. If you configure a WorktreeCreate hook, it replaces the default git behavior, letting you use a different version control system like SVN, Perforce, or Mercurial.
+
+The hook must print the absolute path to the created worktree directory on stdout. Claude Code uses this path as the working directory for the isolated session.
+
+This example creates an SVN working copy and prints the path for Claude Code to use. Replace the repository URL with your own:
+
+```json  theme={null}
+{
+  "hooks": {
+    "WorktreeCreate": [
+      {
+        "hooks": [
+          {
+            "type": "command",
+            "command": "bash -c 'NAME=$(jq -r .name); DIR=\"$HOME/.claude/worktrees/$NAME\"; svn checkout https://svn.example.com/repo/trunk \"$DIR\" >&2 && echo \"$DIR\"'"
+          }
+        ]
+      }
+    ]
+  }
+}
+```
+
+The hook reads the worktree `name` from the JSON input on stdin, checks out a fresh copy into a new directory, and prints the directory path. The `echo` on the last line is what Claude Code reads as the worktree path. Redirect any other output to stderr so it doesn't interfere with the path.
+
+#### WorktreeCreate input
+
+In addition to the [common input fields](#common-input-fields), WorktreeCreate hooks receive the `name` field. This is a slug identifier for the new worktree, either specified by the user or auto-generated (for example, `bold-oak-a3f2`).
+
+```json  theme={null}
+{
+  "session_id": "abc123",
+  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
+  "cwd": "/Users/...",
+  "hook_event_name": "WorktreeCreate",
+  "name": "feature-auth"
+}
+```
+
+#### WorktreeCreate output
+
+The hook must print the absolute path to the created worktree directory on stdout. If the hook fails or produces no output, worktree creation fails with an error.
+
+WorktreeCreate hooks do not use the standard allow/block decision model. Instead, the hook's success or failure determines the outcome. Only `type: "command"` hooks are supported.
+
+### WorktreeRemove
+
+The cleanup counterpart to [WorktreeCreate](#worktreecreate). This hook fires when a worktree is being removed, either when you exit a `--worktree` session and choose to remove it, or when a subagent with `isolation: "worktree"` finishes. For git-based worktrees, Claude handles cleanup automatically with `git worktree remove`. If you configured a WorktreeCreate hook for a non-git version control system, pair it with a WorktreeRemove hook to handle cleanup. Without one, the worktree directory is left on disk.
+
+Claude Code passes the path that WorktreeCreate printed on stdout as `worktree_path` in the hook input. This example reads that path and removes the directory:
+
+```json  theme={null}
+{
+  "hooks": {
+    "WorktreeRemove": [
+      {
+        "hooks": [
+          {
+            "type": "command",
+            "command": "bash -c 'jq -r .worktree_path | xargs rm -rf'"
+          }
+        ]
+      }
+    ]
+  }
+}
+```
+
+#### WorktreeRemove input
+
+In addition to the [common input fields](#common-input-fields), WorktreeRemove hooks receive the `worktree_path` field, which is the absolute path to the worktree being removed.
+
+```json  theme={null}
+{
+  "session_id": "abc123",
+  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
+  "cwd": "/Users/...",
+  "hook_event_name": "WorktreeRemove",
+  "worktree_path": "/Users/.../my-project/.claude/worktrees/feature-auth"
+}
+```
+
+WorktreeRemove hooks have no decision control. They cannot block worktree removal but can perform cleanup tasks like removing version control state or archiving changes. Hook failures are logged in debug mode only. Only `type: "command"` hooks are supported.
+
 ### PreCompact
 
 Runs before Claude Code is about to run a compact operation.
@@ -1369,7 +1461,30 @@
 
 ## Prompt-based hooks
 
-In addition to Bash command hooks (`type: "command"`), Claude Code supports prompt-based hooks (`type: "prompt"`) that use an LLM to evaluate whether to allow or block an action. Prompt-based hooks work with the following events: `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`, `UserPromptSubmit`, `Stop`, `SubagentStop`, and `TaskCompleted`. `TeammateIdle` does not support prompt-based or agent-based hooks.
+In addition to Bash command hooks (`type: "command"`), Claude Code supports prompt-based hooks (`type: "prompt"`) that use an LLM to evaluate whether to allow or block an action, and agent hooks (`type: "agent"`) that spawn an agentic verifier with tool access. Not all events support every hook type.
+
+Events that support all three hook types (`command`, `prompt`, and `agent`):
+
+* `PermissionRequest`
+* `PostToolUse`
+* `PostToolUseFailure`
+* `PreToolUse`
+* `Stop`
+* `SubagentStop`
+* `TaskCompleted`
+* `UserPromptSubmit`
+
+Events that only support `type: "command"` hooks:
+
+* `ConfigChange`
+* `Notification`
+* `PreCompact`
+* `SessionEnd`
+* `SessionStart`
+* `SubagentStart`
+* `TeammateIdle`
+* `WorktreeCreate`
+* `WorktreeRemove`
 
 ### How prompt-based hooks work
 
@@ -1616,7 +1731,7 @@
 
 Run `claude --debug` to see hook execution details, including which hooks matched, their exit codes, and output. Toggle verbose mode with `Ctrl+O` to see hook progress in the transcript.
 
-```
+```text  theme={null}
 [DEBUG] Executing hooks for PostToolUse:Write
 [DEBUG] Getting matching hook commands for PostToolUse with query: Write
 [DEBUG] Found 1 hook matchers in settings

```
### https://code.claude.com/docs/en/setup.md

```diff
--- a/https://code.claude.com/docs/en/setup.md
+++ b/https://code.claude.com/docs/en/setup.md
@@ -2,29 +2,38 @@
 > Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
 > Use this file to discover all available pages before exploring further.
 
-# Set up Claude Code
-
-> Install, authenticate, and start using Claude Code on your development machine.
+# Advanced setup
+
+> System requirements, platform-specific installation, version management, and uninstallation for Claude Code.
+
+This page covers system requirements, platform-specific installation details, updates, and uninstallation. For a guided walkthrough of your first session, see the [quickstart](/en/quickstart). If you've never used a terminal before, see the [terminal guide](/en/terminal-guide).
 
 ## System requirements
 
-* **Operating System**:
+Claude Code runs on the following platforms and configurations:
+
+* **Operating system**:
   * macOS 13.0+
-  * Windows 10 1809+ or Windows Server 2019+ ([see setup notes](#platform-specific-setup))
+  * Windows 10 1809+ or Windows Server 2019+
   * Ubuntu 20.04+
   * Debian 10+
-  * Alpine Linux 3.19+ ([additional dependencies required](#platform-specific-setup))
+  * Alpine Linux 3.19+
 * **Hardware**: 4 GB+ RAM
-* **Network**: Internet connection required (see [network configuration](/en/network-config#network-access-requirements))
-* **Shell**: Works best in Bash or Zsh
+* **Network**: internet connection required. See [network configuration](/en/network-config#network-access-requirements).
+* **Shell**: Bash, Zsh, PowerShell, or CMD. On Windows, [Git for Windows](https://git-scm.com/downloads/win) is required.
 * **Location**: [Anthropic supported countries](https://www.anthropic.com/supported-countries)
 
 ### Additional dependencies
 
-* **ripgrep**: Usually included with Claude Code. If search fails, see [search troubleshooting](/en/troubleshooting#search-and-discovery-issues).
-* **[Node.js 18+](https://nodejs.org/en/download)**: Only required for [deprecated npm installation](#npm-installation-deprecated)
-
-## Installation
+* **ripgrep**: usually included with Claude Code. If search fails, see [search troubleshooting](/en/troubleshooting#search-and-discovery-issues).
+
+## Install Claude Code
+
+<Tip>
+  Prefer a graphical interface? The [Desktop app](/en/desktop-quickstart) lets you use Claude Code without the terminal. Download it for [macOS](https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect?utm_source=claude_code\&utm_medium=docs) or [Windows](https://claude.ai/api/desktop/win32/x64/exe/latest/redirect?utm_source=claude_code\&utm_medium=docs).
+
+  New to the terminal? See the [terminal guide](/en/terminal-guide) for step-by-step instructions.
+</Tip>
 
 To install Claude Code, use one of the following methods:
 
@@ -47,6 +56,8 @@
     ```batch  theme={null}
     curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
     ```
+
+    **Windows requires [Git for Windows](https://git-scm.com/downloads/win).** Install it first if you don't have it.
 
     <Info>
       Native installations automatically update in the background to keep you on the latest version.
@@ -54,7 +65,7 @@
   </Tab>
 
   <Tab title="Homebrew">
-    ```sh  theme={null}
+    ```bash  theme={null}
     brew install --cask claude-code
     ```
 
@@ -74,176 +85,98 @@
   </Tab>
 </Tabs>
 
-After the installation process completes, navigate to your project and start Claude Code:
-
-```bash  theme={null}
-cd your-awesome-project
+After installation completes, open a terminal in the project you want to work in and start Claude Code:
+
+```bash  theme={null}
 claude
 ```
 
-If you encounter any issues during installation, consult the [troubleshooting guide](/en/troubleshooting).
-
-<Tip>
-  Run `claude doctor` after installation to check your installation type and version.
-</Tip>
-
-### Platform-specific setup
-
-**Windows**: Run Claude Code natively (requires [Git Bash](https://git-scm.com/downloads/win)) or inside WSL. Both WSL 1 and WSL 2 are supported, but WSL 1 has limited support and does not support features like Bash tool sandboxing.
-
-**Alpine Linux and other musl/uClibc-based distributions**:
+If you encounter any issues during installation, see the [troubleshooting guide](/en/troubleshooting).
+
+### Set up on Windows
+
+Claude Code on Windows requires [Git for Windows](https://git-scm.com/downloads/win) or WSL. You can launch `claude` from PowerShell, CMD, or Git Bash. Claude Code uses Git Bash internally to run commands. You do not need to run PowerShell as Administrator.
+
+**Option 1: Native Windows with Git Bash**
+
+Install [Git for Windows](https://git-scm.com/downloads/win), then run the install command from PowerShell or CMD.
+
+If Claude Code can't find your Git Bash installation, set the path in your [settings.json file](/en/settings):
+
+```json  theme={null}
+{
+  "env": {
+    "CLAUDE_CODE_GIT_BASH_PATH": "C:\\Program Files\\Git\\bin\\bash.exe"
+  }
+}
+```
+
+**Option 2: WSL**
+
+Both WSL 1 and WSL 2 are supported. WSL 2 supports [sandboxing](/en/sandboxing) for enhanced security. WSL 1 does not support sandboxing.
+
+### Alpine Linux and musl-based distributions
 
 The native installer on Alpine and other musl/uClibc-based distributions requires `libgcc`, `libstdc++`, and `ripgrep`. Install these using your distribution's package manager, then set `USE_BUILTIN_RIPGREP=0`.
 
-On Alpine:
+This example installs the required packages on Alpine:
 
 ```bash  theme={null}
 apk add libgcc libstdc++ ripgrep
 ```
 
-### Authentication
-
-#### For individuals
-
-1. **Claude Pro or Max plan** (recommended): Subscribe to Claude's [Pro or Max plan](https://claude.ai/pricing) for a unified subscription that includes both Claude Code and Claude on the web. Manage your account in one place and log in with your Claude.ai account.
-2. **Claude Console**: Connect through the [Claude Console](https://console.anthropic.com) and complete the OAuth process. Requires active billing in the Anthropic Console. A "Claude Code" workspace is automatically created for usage tracking and cost management. You can't create API keys for the Claude Code workspace; it's dedicated exclusively for Claude Code usage.
-
-#### For teams and organizations
-
-1. **Claude for Teams or Enterprise** (recommended): Subscribe to [Claude for Teams](https://claude.com/pricing#team-&-enterprise) or [Claude for Enterprise](https://anthropic.com/contact-sales) for centralized billing, team management, and access to both Claude Code and Claude on the web. Team members log in with their Claude.ai accounts.
-2. **Claude Console with team billing**: Set up a shared [Claude Console](https://console.anthropic.com) organization with team billing. Invite team members and assign roles for usage tracking.
-3. **Cloud providers**: Configure Claude Code to use [Amazon Bedrock, Google Vertex AI, or Microsoft Foundry](/en/third-party-integrations) for deployments with your existing cloud infrastructure.
-
-### Install a specific version
-
-The native installer accepts either a specific version number or a release channel (`latest` or `stable`). The channel you choose at install time becomes your default for auto-updates. See [Configure release channel](#configure-release-channel) for more information.
-
-To install the latest version (default):
-
-<Tabs>
-  <Tab title="macOS, Linux, WSL">
-    ```bash  theme={null}
-    curl -fsSL https://claude.ai/install.sh | bash
-    ```
-  </Tab>
-
-  <Tab title="Windows PowerShell">
-    ```powershell  theme={null}
-    irm https://claude.ai/install.ps1 | iex
-    ```
-  </Tab>
-
-  <Tab title="Windows CMD">
-    ```batch  theme={null}
-    curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
-    ```
-  </Tab>
-</Tabs>
-
-To install the stable version:
-
-<Tabs>
-  <Tab title="macOS, Linux, WSL">
-    ```bash  theme={null}
-    curl -fsSL https://claude.ai/install.sh | bash -s stable
-    ```
-  </Tab>
-
-  <Tab title="Windows PowerShell">
-    ```powershell  theme={null}
-    & ([scriptblock]::Create((irm https://claude.ai/install.ps1))) stable
-    ```
-  </Tab>
-
-  <Tab title="Windows CMD">
-    ```batch  theme={null}
-    curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd stable && del install.cmd
-    ```
-  </Tab>
-</Tabs>
-
-To install a specific version number:
-
-<Tabs>
-  <Tab title="macOS, Linux, WSL">
-    ```bash  theme={null}
-    curl -fsSL https://claude.ai/install.sh | bash -s 1.0.58
-    ```
-  </Tab>
-
-  <Tab title="Windows PowerShell">
-    ```powershell  theme={null}
-    & ([scriptblock]::Create((irm https://claude.ai/install.ps1))) 1.0.58
-    ```
-  </Tab>
-
-  <Tab title="Windows CMD">
-    ```batch  theme={null}
-    curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd 1.0.58 && del install.cmd
-    ```
-  </Tab>
-</Tabs>
-
-### Binary integrity and code signing
-
-* SHA256 checksums for all platforms are published in the release manifests, currently located at `https://storage.googleapis.com/claude-code-dist-86c565f3-f756-42ad-8dfa-d59b1c096819/claude-code-releases/{VERSION}/manifest.json` (example: replace `{VERSION}` with `2.0.30`)
-* Signed binaries are distributed for the following platforms:
-  * macOS: Signed by "Anthropic PBC" and notarized by Apple
-  * Windows: Signed by "Anthropic, PBC"
-
-## NPM installation (deprecated)
-
-NPM installation is deprecated. Use the [native installation](#installation) method when possible. To migrate an existing npm installation to native, run `claude install`.
-
-**Global npm installation**
-
-```sh  theme={null}
-npm install -g @anthropic-ai/claude-code
-```
-
-<Warning>
-  Do NOT use `sudo npm install -g` as this can lead to permission issues and security risks.
-  If you encounter permission errors, see [troubleshooting permission errors](/en/troubleshooting#command-not-found-claude-or-permission-errors) for recommended solutions.
-</Warning>
-
-## Windows setup
-
-**Option 1: Claude Code within WSL**
-
-* Both WSL 1 and WSL 2 are supported
-* WSL 2 supports [sandboxing](/en/sandboxing) for enhanced security. WSL 1 does not support sandboxing.
-
-**Option 2: Claude Code on native Windows with Git Bash**
-
-* Requires [Git for Windows](https://git-scm.com/downloads/win)
-* For portable Git installations, specify the path to your `bash.exe`:
-  ```powershell  theme={null}
-  $env:CLAUDE_CODE_GIT_BASH_PATH="C:\Program Files\Git\bin\bash.exe"
-  ```
+Then set `USE_BUILTIN_RIPGREP` to `0` in your [settings.json file](/en/settings#environment-variables):
+
+```json  theme={null}
+{
+  "env": {
+    "USE_BUILTIN_RIPGREP": "0"
+  }
+}
+```
+
+## Verify your installation
+
+After installing, confirm Claude Code is working:
+
+```bash  theme={null}
+claude --version
+```
+
+For a more detailed check of your installation and configuration, run [`claude doctor`](/en/troubleshooting#get-more-help):
+
+```bash  theme={null}
+claude doctor
+```
+
+## Authenticate
+
+Claude Code requires a Pro, Max, Teams, Enterprise, or Console account. The free Claude.ai plan does not include Claude Code access. You can also use Claude Code with a third-party API provider like [Amazon Bedrock](/en/amazon-bedrock), [Google Vertex AI](/en/google-vertex-ai), or [Microsoft Foundry](/en/microsoft-foundry).
+
+After installing, log in by running `claude` and following the browser prompts. See [Authentication](/en/authentication) for all account types and team setup options.
 
 ## Update Claude Code
 
-### Auto updates
-
-Claude Code automatically keeps itself up to date to ensure you have the latest features and security fixes.
-
-* **Update checks**: Performed on startup and periodically while running
-* **Update process**: Downloads and installs automatically in the background
-* **Notifications**: You'll see a notification when updates are installed
-* **Applying updates**: Updates take effect the next time you start Claude Code
+Native installations automatically update in the background. You can [configure the release channel](#configure-release-channel) to control whether you receive updates immediately or on a delayed stable schedule, or [disable auto-updates](#disable-auto-updates) entirely. Homebrew and WinGet installations require manual updates.
+
+### Auto-updates
+
+Claude Code checks for updates on startup and periodically while running. Updates download and install in the background, then take effect the next time you start Claude Code.
 
 <Note>
   Homebrew and WinGet installations do not auto-update. Use `brew upgrade claude-code` or `winget upgrade Anthropic.ClaudeCode` to update manually.
 
   **Known issue:** Claude Code may notify you of updates before the new version is available in these package managers. If an upgrade fails, wait and try again later.
+
+  Homebrew keeps old versions on disk after upgrades. Run `brew cleanup claude-code` periodically to reclaim disk space.
 </Note>
 
 ### Configure release channel
 
-Configure which release channel Claude Code follows for both auto-updates and `claude update` with the `autoUpdatesChannel` setting:
-
-* `"latest"` (default): Receive new features as soon as they're released
-* `"stable"`: Use a version that is typically about one week old, skipping releases with major regressions
+Control which release channel Claude Code follows for auto-updates and `claude update` with the `autoUpdatesChannel` setting:
+
+* `"latest"`, the default: receive new features as soon as they're released
+* `"stable"`: use a version that is typically about one week old, skipping releases with major regressions
 
 Configure this via `/config` → **Auto-update channel**, or add it to your [settings.json file](/en/settings):
 
@@ -257,66 +190,186 @@
 
 ### Disable auto-updates
 
-Set the `DISABLE_AUTOUPDATER` environment variable in your shell or [settings.json file](/en/settings):
-
-```bash  theme={null}
-export DISABLE_AUTOUPDATER=1
+Set `DISABLE_AUTOUPDATER` to `"1"` in the `env` key of your [settings.json file](/en/settings#environment-variables):
+
+```json  theme={null}
+{
+  "env": {
+    "DISABLE_AUTOUPDATER": "1"
+  }
+}
 ```
 
 ### Update manually
 
+To apply an update immediately without waiting for the next background check, run:
+
 ```bash  theme={null}
 claude update
 ```
 
+## Advanced installation options
+
+These options are for version pinning, migrating from npm, and verifying binary integrity.
+
+### Install a specific version
+
+The native installer accepts either a specific version number or a release channel (`latest` or `stable`). The channel you choose at install time becomes your default for auto-updates. See [configure release channel](#configure-release-channel) for more information.
+
+To install the latest version (default):
+
+<Tabs>
+  <Tab title="macOS, Linux, WSL">
+    ```bash  theme={null}
+    curl -fsSL https://claude.ai/install.sh | bash
+    ```
+  </Tab>
+
+  <Tab title="Windows PowerShell">
+    ```powershell  theme={null}
+    irm https://claude.ai/install.ps1 | iex
+    ```
+  </Tab>
+
+  <Tab title="Windows CMD">
+    ```batch  theme={null}
+    curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
+    ```
+  </Tab>
+</Tabs>
+
+To install the stable version:
+
+<Tabs>
+  <Tab title="macOS, Linux, WSL">
+    ```bash  theme={null}
+    curl -fsSL https://claude.ai/install.sh | bash -s stable
+    ```
+  </Tab>
+
+  <Tab title="Windows PowerShell">
+    ```powershell  theme={null}
+    & ([scriptblock]::Create((irm https://claude.ai/install.ps1))) stable
+    ```
+  </Tab>
+
+  <Tab title="Windows CMD">
+    ```batch  theme={null}
+    curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd stable && del install.cmd
+    ```
+  </Tab>
+</Tabs>
+
+To install a specific version number:
+
+<Tabs>
+  <Tab title="macOS, Linux, WSL">
+    ```bash  theme={null}
+    curl -fsSL https://claude.ai/install.sh | bash -s 1.0.58
+    ```
+  </Tab>
+
+  <Tab title="Windows PowerShell">
+    ```powershell  theme={null}
+    & ([scriptblock]::Create((irm https://claude.ai/install.ps1))) 1.0.58
+    ```
+  </Tab>
+
+  <Tab title="Windows CMD">
+    ```batch  theme={null}
+    curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd 1.0.58 && del install.cmd
+    ```
+  </Tab>
+</Tabs>
+
+### Deprecated npm installation
+
+npm installation is deprecated. The native installer is faster, requires no dependencies, and auto-updates in the background. Use the [native installation](#install-claude-code) method when possible.
+
+#### Migrate from npm to native
+
+If you previously installed Claude Code with npm, switch to the native installer:
+
+```bash  theme={null}
+# Install the native binary
+curl -fsSL https://claude.ai/install.sh | bash
+
+# Remove the old npm installation
+npm uninstall -g @anthropic-ai/claude-code
+```
+
+You can also run `claude install` from an existing npm installation to install the native binary alongside it, then remove the npm version.
+
+#### Install with npm
+
+If you need npm installation for compatibility reasons, you must have [Node.js 18+](https://nodejs.org/en/download) installed. Install the package globally:
+
+```bash  theme={null}
+npm install -g @anthropic-ai/claude-code
+```
+
+<Warning>
+  Do NOT use `sudo npm install -g` as this can lead to permission issues and security risks. If you encounter permission errors, see [troubleshooting permission errors](/en/troubleshooting#permission-errors-during-installation).
+</Warning>
+
+### Binary integrity and code signing
+
+You can verify the integrity of Claude Code binaries using SHA256 checksums and code signatures.
+
+* SHA256 checksums for all platforms are published in the release manifests at `https://storage.googleapis.com/claude-code-dist-86c565f3-f756-42ad-8dfa-d59b1c096819/claude-code-releases/{VERSION}/manifest.json`. Replace `{VERSION}` with a version number such as `2.0.30`.
+* Signed binaries are distributed for the following platforms:
+  * **macOS**: signed by "Anthropic PBC" and notarized by Apple
+  * **Windows**: signed by "Anthropic, PBC"
+
 ## Uninstall Claude Code
 
-If you need to uninstall Claude Code, follow the instructions for your installation method.
+To remove Claude Code, follow the instructions for your installation method.
 
 ### Native installation
 
 Remove the Claude Code binary and version files:
 
-**macOS, Linux, WSL:**
-
-```bash  theme={null}
-rm -f ~/.local/bin/claude
-rm -rf ~/.local/share/claude
-```
-
-**Windows PowerShell:**
-
-```powershell  theme={null}
-Remove-Item -Path "$env:USERPROFILE\.local\bin\claude.exe" -Force
-Remove-Item -Path "$env:USERPROFILE\.local\share\claude" -Recurse -Force
-```
-
-**Windows CMD:**
-
-```batch  theme={null}
-del "%USERPROFILE%\.local\bin\claude.exe"
-rmdir /s /q "%USERPROFILE%\.local\share\claude"
-```
+<Tabs>
+  <Tab title="macOS, Linux, WSL">
+    ```bash  theme={null}
+    rm -f ~/.local/bin/claude
+    rm -rf ~/.local/share/claude
+    ```
+  </Tab>
+
+  <Tab title="Windows PowerShell">
+    ```powershell  theme={null}
+    Remove-Item -Path "$env:USERPROFILE\.local\bin\claude.exe" -Force
+    Remove-Item -Path "$env:USERPROFILE\.local\share\claude" -Recurse -Force
+    ```
+  </Tab>
+</Tabs>
 
 ### Homebrew installation
 
+Remove the Homebrew cask:
+
 ```bash  theme={null}
 brew uninstall --cask claude-code
 ```
 
 ### WinGet installation
+
+Remove the WinGet package:
 
 ```powershell  theme={null}
 winget uninstall Anthropic.ClaudeCode
 ```
 
-### NPM installation
+### npm
+
+Remove the global npm package:
 
 ```bash  theme={null}
 npm uninstall -g @anthropic-ai/claude-code
 ```
 
-### Clean up configuration files (optional)
+### Remove configuration files
 
 <Warning>
   Removing configuration files will delete all your settings, allowed tools, MCP server configurations, and session history.
@@ -324,38 +377,28 @@
 
 To remove Claude Code settings and cached data:
 
-**macOS, Linux, WSL:**
-
-```bash  theme={null}
-# Remove user settings and state
-rm -rf ~/.claude
-rm ~/.claude.json
-
-# Remove project-specific settings (run from your project directory)
-rm -rf .claude
-rm -f .mcp.json
-```
-
-**Windows PowerShell:**
-
-```powershell  theme={null}
-# Remove user settings and state
-Remove-Item -Path "$env:USERPROFILE\.claude" -Recurse -Force
-Remove-Item -Path "$env:USERPROFILE\.claude.json" -Force
-
-# Remove project-specific settings (run from your project directory)
-Remove-Item -Path ".claude" -Recurse -Force
-Remove-Item -Path ".mcp.json" -Force
-```
-
-**Windows CMD:**
-
-```batch  theme={null}
-REM Remove user settings and state
-rmdir /s /q "%USERPROFILE%\.claude"
-del "%USERPROFILE%\.claude.json"
-
-REM Remove project-specific settings (run from your project directory)
-rmdir /s /q ".claude"
-del ".mcp.json"
-```
+<Tabs>
+  <Tab title="macOS, Linux, WSL">
+    ```bash  theme={null}
+    # Remove user settings and state
+    rm -rf ~/.claude
+    rm ~/.claude.json
+
+    # Remove project-specific settings (run from your project directory)
+    rm -rf .claude
+    rm -f .mcp.json
+    ```
+  </Tab>
+
+  <Tab title="Windows PowerShell">
+    ```powershell  theme={null}
+    # Remove user settings and state
+    Remove-Item -Path "$env:USERPROFILE\.claude" -Recurse -Force
+    Remove-Item -Path "$env:USERPROFILE\.claude.json" -Force
+
+    # Remove project-specific settings (run from your project directory)
+    Remove-Item -Path ".claude" -Recurse -Force
+    Remove-Item -Path ".mcp.json" -Force
+    ```
+  </Tab>
+</Tabs>

```
### https://code.claude.com/docs/en/quickstart.md

```diff
--- a/https://code.claude.com/docs/en/quickstart.md
+++ b/https://code.claude.com/docs/en/quickstart.md
@@ -6,13 +6,14 @@
 
 > Welcome to Claude Code!
 
-This quickstart guide will have you using AI-powered coding assistance in just a few minutes. By the end, you'll understand how to use Claude Code for common development tasks.
+This quickstart guide will have you using AI-powered coding assistance in a few minutes. By the end, you'll understand how to use Claude Code for common development tasks.
 
 ## Before you begin
 
 Make sure you have:
 
 * A terminal or command prompt open
+  * If you've never used the terminal before, check out the [terminal guide](/en/terminal-guide)
 * A code project to work with
 * A [Claude subscription](https://claude.com/pricing) (Pro, Max, Teams, or Enterprise), [Claude Console](https://console.anthropic.com/) account, or access through a [supported cloud provider](/en/third-party-integrations)
 
@@ -28,21 +29,23 @@
   <Tab title="Native Install (Recommended)">
     **macOS, Linux, WSL:**
 
-    ```bash  theme={null}
+    ```bash theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null}
     curl -fsSL https://claude.ai/install.sh | bash
     ```
 
     **Windows PowerShell:**
 
-    ```powershell  theme={null}
+    ```powershell theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null}
     irm https://claude.ai/install.ps1 | iex
     ```
 
     **Windows CMD:**
 
-    ```batch  theme={null}
+    ```batch theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null}
     curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
     ```
+
+    **Windows requires [Git for Windows](https://git-scm.com/downloads/win).** Install it first if you don't have it.
 
     <Info>
       Native installations automatically update in the background to keep you on the latest version.
@@ -50,7 +53,7 @@
   </Tab>
 
   <Tab title="Homebrew">
-    ```sh  theme={null}
+    ```bash theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null}
     brew install --cask claude-code
     ```
 
@@ -60,7 +63,7 @@
   </Tab>
 
   <Tab title="WinGet">
-    ```powershell  theme={null}
+    ```powershell theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null}
     winget install Anthropic.ClaudeCode
     ```
 
@@ -111,47 +114,47 @@
 
 Let's start with understanding your codebase. Try one of these commands:
 
-```
+```text  theme={null}
 what does this project do?
 ```
 
 Claude will analyze your files and provide a summary. You can also ask more specific questions:
 
-```
+```text  theme={null}
 what technologies does this project use?
 ```
 
-```
+```text  theme={null}
 where is the main entry point?
 ```
 
-```
+```text  theme={null}
 explain the folder structure
 ```
 
 You can also ask Claude about its own capabilities:
 
-```
+```text  theme={null}
 what can Claude Code do?
 ```
 
-```
+```text  theme={null}
 how do I create custom skills in Claude Code?
 ```
 
-```
+```text  theme={null}
 can Claude Code work with Docker?
 ```
 
 <Note>
-  Claude Code reads your files as needed - you don't have to manually add context. Claude also has access to its own documentation and can answer questions about its features and capabilities.
+  Claude Code reads your project files as needed. You don't have to manually add context.
 </Note>
 
 ## Step 5: Make your first code change
 
 Now let's make Claude Code do some actual coding. Try a simple task:
 
-```
+```text  theme={null}
 add a hello world function to the main file
 ```
 
@@ -170,25 +173,25 @@
 
 Claude Code makes Git operations conversational:
 
-```
+```text  theme={null}
 what files have I changed?
 ```
 
-```
+```text  theme={null}
 commit my changes with a descriptive message
 ```
 
 You can also prompt for more complex Git operations:
 
-```
+```text  theme={null}
 create a new branch called feature/quickstart
 ```
 
-```
+```text  theme={null}
 show me the last 5 commits
 ```
 
-```
+```text  theme={null}
 help me resolve merge conflicts
 ```
 
@@ -198,13 +201,13 @@
 
 Describe what you want in natural language:
 
-```
+```text  theme={null}
 add input validation to the user registration form
 ```
 
 Or fix existing issues:
 
-```
+```text  theme={null}
 there's a bug where users can submit empty forms - fix it
 ```
 
@@ -221,30 +224,30 @@
 
 **Refactor code**
 
-```
+```text  theme={null}
 refactor the authentication module to use async/await instead of callbacks
 ```
 
 **Write tests**
 
-```
+```text  theme={null}
 write unit tests for the calculator functions
 ```
 
 **Update documentation**
 
-```
+```text  theme={null}
 update the README with installation instructions
 ```
 
 **Code review**
 
-```
+```text  theme={null}
 review my changes and suggest improvements
 ```
 
 <Tip>
-  **Remember**: Claude Code is your AI pair programmer. Talk to it like you would a helpful colleague - describe what you want to achieve, and it will help you get there.
+  Talk to Claude like you would a helpful colleague. Describe what you want to achieve, and it will help you get there.
 </Tip>
 
 ## Essential commands
@@ -279,7 +282,7 @@
   <Accordion title="Use step-by-step instructions">
     Break complex tasks into steps:
 
-    ```
+    ```text  theme={null}
     1. create a new database table for user profiles
     2. create an API endpoint to get and update user profiles
     3. build a webpage that allows users to see and edit their information
@@ -289,11 +292,11 @@
   <Accordion title="Let Claude explore first">
     Before making changes, let Claude understand your code:
 
-    ```
+    ```text  theme={null}
     analyze the database schema
     ```
 
-    ```
+    ```text  theme={null}
     build a dashboard showing products that are most frequently returned by our UK customers
     ```
   </Accordion>

```
### https://code.claude.com/docs/en/costs.md

```diff
--- a/https://code.claude.com/docs/en/costs.md
+++ b/https://code.claude.com/docs/en/costs.md
@@ -22,7 +22,7 @@
 
 The `/cost` command provides detailed token usage statistics for your current session:
 
-```
+```text  theme={null}
 Total cost:            $0.55
 Total duration (API):  6m 19.7s
 Total duration (wall): 6h 33m 10.2s

```
### https://code.claude.com/docs/en/hooks-guide.md

```diff
--- a/https://code.claude.com/docs/en/hooks-guide.md
+++ b/https://code.claude.com/docs/en/hooks-guide.md
@@ -36,7 +36,7 @@
       <Tab title="macOS">
         Uses [`osascript`](https://ss64.com/mac/osascript.html) to trigger a native macOS notification through AppleScript:
 
-        ```
+        ```bash  theme={null}
         osascript -e 'display notification "Claude Code needs your attention" with title "Claude Code"'
         ```
       </Tab>
@@ -44,7 +44,7 @@
       <Tab title="Linux">
         Uses `notify-send`, which is pre-installed on most Linux desktops with a notification daemon:
 
-        ```
+        ```bash  theme={null}
         notify-send 'Claude Code' 'Claude Code needs your attention'
         ```
       </Tab>
@@ -52,7 +52,7 @@
       <Tab title="Windows (PowerShell)">
         Uses PowerShell to show a native message box through .NET's Windows Forms:
 
-        ```
+        ```powershell  theme={null}
         powershell.exe -Command "[System.Reflection.Assembly]::LoadWithPartialName('System.Windows.Forms'); [System.Windows.Forms.MessageBox]::Show('Claude Code needs your attention', 'Claude Code')"
         ```
       </Tab>
@@ -293,23 +293,25 @@
 
 Hook events fire at specific lifecycle points in Claude Code. When an event fires, all matching hooks run in parallel, and identical hook commands are automatically deduplicated. The table below shows each event and when it triggers:
 
-| Event                | When it fires                                                      |
-| :------------------- | :----------------------------------------------------------------- |
-| `SessionStart`       | When a session begins or resumes                                   |
-| `UserPromptSubmit`   | When you submit a prompt, before Claude processes it               |
-| `PreToolUse`         | Before a tool call executes. Can block it                          |
-| `PermissionRequest`  | When a permission dialog appears                                   |
-| `PostToolUse`        | After a tool call succeeds                                         |
-| `PostToolUseFailure` | After a tool call fails                                            |
-| `Notification`       | When Claude Code sends a notification                              |
-| `SubagentStart`      | When a subagent is spawned                                         |
-| `SubagentStop`       | When a subagent finishes                                           |
-| `Stop`               | When Claude finishes responding                                    |
-| `TeammateIdle`       | When an [agent team](/en/agent-teams) teammate is about to go idle |
-| `TaskCompleted`      | When a task is being marked as completed                           |
-| `ConfigChange`       | When a configuration file changes during a session                 |
-| `PreCompact`         | Before context compaction                                          |
-| `SessionEnd`         | When a session terminates                                          |
+| Event                | When it fires                                                                                               |
+| :------------------- | :---------------------------------------------------------------------------------------------------------- |
+| `SessionStart`       | When a session begins or resumes                                                                            |
+| `UserPromptSubmit`   | When you submit a prompt, before Claude processes it                                                        |
+| `PreToolUse`         | Before a tool call executes. Can block it                                                                   |
+| `PermissionRequest`  | When a permission dialog appears                                                                            |
+| `PostToolUse`        | After a tool call succeeds                                                                                  |
+| `PostToolUseFailure` | After a tool call fails                                                                                     |
+| `Notification`       | When Claude Code sends a notification                                                                       |
+| `SubagentStart`      | When a subagent is spawned                                                                                  |
+| `SubagentStop`       | When a subagent finishes                                                                                    |
+| `Stop`               | When Claude finishes responding                                                                             |
+| `TeammateIdle`       | When an [agent team](/en/agent-teams) teammate is about to go idle                                          |
+| `TaskCompleted`      | When a task is being marked as completed                                                                    |
+| `ConfigChange`       | When a configuration file changes during a session                                                          |
+| `WorktreeCreate`     | When a worktree is being created via `--worktree` or `isolation: "worktree"`. Replaces default git behavior |
+| `WorktreeRemove`     | When a worktree is being removed, either at session exit or when a subagent finishes                        |
+| `PreCompact`         | Before context compaction                                                                                   |
+| `SessionEnd`         | When a session terminates                                                                                   |
 
 Each hook has a `type` that determines how it runs. Most hooks use `"type": "command"`, which runs a shell command. Two other options use a Claude model to make decisions: `"type": "prompt"` for single-turn evaluation and `"type": "agent"` for multi-turn verification with tool access. See [Prompt-based hooks](#prompt-based-hooks) and [Agent-based hooks](#agent-based-hooks) for details.
 
@@ -333,7 +335,7 @@
 }
 ```
 
-Your script can parse that JSON and act on any of those fields. `UserPromptSubmit` hooks get the `prompt` text instead, `SessionStart` hooks get the `source` (startup, resume, compact), and so on. See [Common input fields](/en/hooks#common-input-fields) in the reference for shared fields, and each event's section for event-specific schemas.
+Your script can parse that JSON and act on any of those fields. `UserPromptSubmit` hooks get the `prompt` text instead, `SessionStart` hooks get the `source` (startup, resume, clear, compact), and so on. See [Common input fields](/en/hooks#common-input-fields) in the reference for shared fields, and each event's section for event-specific schemas.
 
 #### Hook output
 
@@ -411,16 +413,17 @@
 
 Each event type matches on a specific field. Matchers support exact strings and regex patterns:
 
-| Event                                                                  | What the matcher filters  | Example matcher values                                                         |
-| :--------------------------------------------------------------------- | :------------------------ | :----------------------------------------------------------------------------- |
-| `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest` | tool name                 | `Bash`, `Edit\|Write`, `mcp__.*`                                               |
-| `SessionStart`                                                         | how the session started   | `startup`, `resume`, `clear`, `compact`                                        |
-| `SessionEnd`                                                           | why the session ended     | `clear`, `logout`, `prompt_input_exit`, `bypass_permissions_disabled`, `other` |
-| `Notification`                                                         | notification type         | `permission_prompt`, `idle_prompt`, `auth_success`, `elicitation_dialog`       |
-| `SubagentStart`                                                        | agent type                | `Bash`, `Explore`, `Plan`, or custom agent names                               |
-| `PreCompact`                                                           | what triggered compaction | `manual`, `auto`                                                               |
-| `UserPromptSubmit`, `Stop`, `TeammateIdle`, `TaskCompleted`            | no matcher support        | always fires on every occurrence                                               |
-| `SubagentStop`                                                         | agent type                | same values as `SubagentStart`                                                 |
+| Event                                                                                           | What the matcher filters  | Example matcher values                                                             |
+| :---------------------------------------------------------------------------------------------- | :------------------------ | :--------------------------------------------------------------------------------- |
+| `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`                          | tool name                 | `Bash`, `Edit\|Write`, `mcp__.*`                                                   |
+| `SessionStart`                                                                                  | how the session started   | `startup`, `resume`, `clear`, `compact`                                            |
+| `SessionEnd`                                                                                    | why the session ended     | `clear`, `logout`, `prompt_input_exit`, `bypass_permissions_disabled`, `other`     |
+| `Notification`                                                                                  | notification type         | `permission_prompt`, `idle_prompt`, `auth_success`, `elicitation_dialog`           |
+| `SubagentStart`                                                                                 | agent type                | `Bash`, `Explore`, `Plan`, or custom agent names                                   |
+| `PreCompact`                                                                                    | what triggered compaction | `manual`, `auto`                                                                   |
+| `SubagentStop`                                                                                  | agent type                | same values as `SubagentStart`                                                     |
+| `ConfigChange`                                                                                  | configuration source      | `user_settings`, `project_settings`, `local_settings`, `policy_settings`, `skills` |
+| `UserPromptSubmit`, `Stop`, `TeammateIdle`, `TaskCompleted`, `WorktreeCreate`, `WorktreeRemove` | no matcher support        | always fires on every occurrence                                                   |
 
 A few more examples showing matchers on different event types:
 
@@ -634,7 +637,7 @@
 
 When Claude Code runs a hook, it spawns a shell that sources your profile (`~/.zshrc` or `~/.bashrc`). If your profile contains unconditional `echo` statements, that output gets prepended to your hook's JSON:
 
-```
+```text  theme={null}
 Shell ready on arm64
 {"decision": "block", "reason": "Not allowed"}
 ```

```
### https://code.claude.com/docs/en/troubleshooting.md

```diff
--- a/https://code.claude.com/docs/en/troubleshooting.md
+++ b/https://code.claude.com/docs/en/troubleshooting.md
@@ -6,20 +6,536 @@
 
 > Discover solutions to common issues with Claude Code installation and usage.
 
+## Troubleshoot installation issues
+
+<Tip>
+  If you'd rather skip the terminal entirely, the [Claude Code Desktop app](/en/desktop-quickstart) lets you install and use Claude Code through a graphical interface. Download it for [macOS](https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect?utm_source=claude_code\&utm_medium=docs) or [Windows](https://claude.ai/api/desktop/win32/x64/exe/latest/redirect?utm_source=claude_code\&utm_medium=docs) and start coding without any command-line setup.
+</Tip>
+
+Find the error message or symptom you're seeing:
+
+| What you see                                                | Solution                                                                                                                |
+| :---------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- |
+| `command not found: claude` or `'claude' is not recognized` | [Fix your PATH](#command-not-found-claude-after-installation)                                                           |
+| `syntax error near unexpected token '<'`                    | [Install script returns HTML](#install-script-returns-html-instead-of-a-shell-script)                                   |
+| `curl: (56) Failure writing output to destination`          | [Download script first, then run it](#curl-56-failure-writing-output-to-destination)                                    |
+| `Killed` during install on Linux                            | [Add swap space for low-memory servers](#install-killed-on-low-memory-linux-servers)                                    |
+| `TLS connect error` or `SSL/TLS secure channel`             | [Update CA certificates](#tls-or-ssl-connection-errors)                                                                 |
+| `Failed to fetch version` or can't reach download server    | [Check network and proxy settings](#check-network-connectivity)                                                         |
+| `irm is not recognized` or `&& is not valid`                | [Use the right command for your shell](#windows-irm-or--not-recognized)                                                 |
+| `Claude Code on Windows requires git-bash`                  | [Install or configure Git Bash](#windows-claude-code-on-windows-requires-git-bash)                                      |
+| `Error loading shared library`                              | [Wrong binary variant for your system](#linux-wrong-binary-variant-installed-muslglibc-mismatch)                        |
+| `Illegal instruction` on Linux                              | [Architecture mismatch](#illegal-instruction-on-linux)                                                                  |
+| `dyld: cannot load` or `Abort trap` on macOS                | [Binary incompatibility](#dyld-cannot-load-on-macos)                                                                    |
+| `Invoke-Expression: Missing argument in parameter list`     | [Install script returns HTML](#install-script-returns-html-instead-of-a-shell-script)                                   |
+| `App unavailable in region`                                 | Claude Code is not available in your country. See [supported countries](https://www.anthropic.com/supported-countries). |
+| `unable to get local issuer certificate`                    | [Configure corporate CA certificates](#tls-or-ssl-connection-errors)                                                    |
+| `OAuth error` or `403 Forbidden`                            | [Fix authentication](#authentication-issues)                                                                            |
+
+If your issue isn't listed, work through these diagnostic steps.
+
+## Debug installation problems
+
+### Check network connectivity
+
+The installer downloads from `storage.googleapis.com`. Verify you can reach it:
+
+```bash  theme={null}
+curl -sI https://storage.googleapis.com
+```
+
+If this fails, your network may be blocking the connection. Common causes:
+
+* Corporate firewalls or proxies blocking Google Cloud Storage
+* Regional network restrictions: try a VPN or alternative network
+* TLS/SSL issues: update your system's CA certificates, or check if `HTTPS_PROXY` is configured
+
+If you're behind a corporate proxy, set `HTTPS_PROXY` and `HTTP_PROXY` to your proxy's address before installing. Ask your IT team for the proxy URL if you don't know it, or check your browser's proxy settings.
+
+This example sets both proxy variables, then runs the installer through your proxy:
+
+```bash  theme={null}
+export HTTP_PROXY=http://proxy.example.com:8080
+export HTTPS_PROXY=http://proxy.example.com:8080
+curl -fsSL https://claude.ai/install.sh | bash
+```
+
+### Verify your PATH
+
+If installation succeeded but you get a `command not found` or `not recognized` error when running `claude`, the install directory isn't in your PATH. Your shell searches for programs in directories listed in PATH, and the installer places `claude` at `~/.local/bin/claude` on macOS/Linux or `%USERPROFILE%\.local\bin\claude.exe` on Windows.
+
+Check if the install directory is in your PATH by listing your PATH entries and filtering for `local/bin`:
+
+<Tabs>
+  <Tab title="macOS/Linux">
+    ```bash  theme={null}
+    echo $PATH | tr ':' '\n' | grep local/bin
+    ```
+
+    If there's no output, the directory is missing. Add it to your shell configuration:
+
+    ```bash  theme={null}
+    # Zsh (macOS default)
+    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
+    source ~/.zshrc
+
+    # Bash (Linux default)
+    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
+    source ~/.bashrc
+    ```
+
+    Alternatively, close and reopen your terminal.
+
+    Verify the fix worked:
+
+    ```bash  theme={null}
+    claude --version
+    ```
+  </Tab>
+
+  <Tab title="Windows PowerShell">
+    ```powershell  theme={null}
+    $env:PATH -split ';' | Select-String 'local\\bin'
+    ```
+
+    If there's no output, add the install directory to your User PATH:
+
+    ```powershell  theme={null}
+    $currentPath = [Environment]::GetEnvironmentVariable('PATH', 'User')
+    [Environment]::SetEnvironmentVariable('PATH', "$currentPath;$env:USERPROFILE\.local\bin", 'User')
+    ```
+
+    Restart your terminal for the change to take effect.
+
+    Verify the fix worked:
+
+    ```powershell  theme={null}
+    claude --version
+    ```
+  </Tab>
+
+  <Tab title="Windows CMD">
+    ```batch  theme={null}
+    echo %PATH% | findstr /i "local\bin"
+    ```
+
+    If there's no output, open System Settings, go to Environment Variables, and add `%USERPROFILE%\.local\bin` to your User PATH variable. Restart your terminal.
+
+    Verify the fix worked:
+
+    ```batch  theme={null}
+    claude --version
+    ```
+  </Tab>
+</Tabs>
+
+### Check for conflicting installations
+
+Multiple Claude Code installations can cause version mismatches or unexpected behavior. Check what's installed:
+
+<Tabs>
+  <Tab title="macOS/Linux">
+    List all `claude` binaries found in your PATH:
+
+    ```bash  theme={null}
+    which -a claude
+    ```
+
+    Check whether the native installer and npm versions are present:
+
+    ```bash  theme={null}
+    ls -la ~/.local/bin/claude
+    ```
+
+    ```bash  theme={null}
+    ls -la ~/.claude/local/
+    ```
+
+    ```bash  theme={null}
+    npm -g ls @anthropic-ai/claude-code 2>/dev/null
+    ```
+  </Tab>
+
+  <Tab title="Windows PowerShell">
+    ```powershell  theme={null}
+    where.exe claude
+    Test-Path "$env:LOCALAPPDATA\Claude Code\claude.exe"
+    ```
+  </Tab>
+</Tabs>
+
+If you find multiple installations, keep only one. The native install at `~/.local/bin/claude` is recommended. Remove any extra installations:
+
+Uninstall an npm global install:
+
+```bash  theme={null}
+npm uninstall -g @anthropic-ai/claude-code
+```
+
+Remove a Homebrew install on macOS:
+
+```bash  theme={null}
+brew uninstall --cask claude-code
+```
+
+### Check directory permissions
+
+The installer needs write access to `~/.local/bin/` and `~/.claude/`. If installation fails with permission errors, check whether these directories are writable:
+
+```bash  theme={null}
+test -w ~/.local/bin && echo "writable" || echo "not writable"
+test -w ~/.claude && echo "writable" || echo "not writable"
+```
+
+If either directory isn't writable, create the install directory and set your user as the owner:
+
+```bash  theme={null}
+sudo mkdir -p ~/.local/bin
+sudo chown -R $(whoami) ~/.local
+```
+
+### Verify the binary works
+
+If `claude` is installed but crashes or hangs on startup, run these checks to narrow down the cause.
+
+Confirm the binary exists and is executable:
+
+```bash  theme={null}
+ls -la $(which claude)
+```
+
+On Linux, check for missing shared libraries. If `ldd` shows missing libraries, you may need to install system packages. On Alpine Linux and other musl-based distributions, see [Alpine Linux setup](/en/setup#alpine-linux-and-musl-based-distributions).
+
+```bash  theme={null}
+ldd $(which claude) | grep "not found"
+```
+
+Run a quick sanity check that the binary can execute:
+
+```bash  theme={null}
+claude --version
+```
+
 ## Common installation issues
 
+These are the most frequently encountered installation problems and their solutions.
+
+### Install script returns HTML instead of a shell script
+
+When running the install command, you may see one of these errors:
+
+```
+bash: line 1: syntax error near unexpected token `<'
+bash: line 1: `<!DOCTYPE html>'
+```
+
+On PowerShell, the same problem appears as:
+
+```
+Invoke-Expression: Missing argument in parameter list.
+```
+
+This means the install URL returned an HTML page instead of the install script. If the HTML page says "App unavailable in region," Claude Code is not available in your country. See [supported countries](https://www.anthropic.com/supported-countries).
+
+Otherwise, this can happen due to network issues, regional routing, or a temporary service disruption.
+
+**Solutions:**
+
+1. **Use an alternative install method**:
+
+   On macOS or Linux, install via Homebrew:
+
+   ```bash  theme={null}
+   brew install --cask claude-code
+   ```
+
+   On Windows, install via WinGet:
+
+   ```powershell  theme={null}
+   winget install Anthropic.ClaudeCode
+   ```
+
+2. **Retry after a few minutes**: the issue is often temporary. Wait and try the original command again.
+
+### `command not found: claude` after installation
+
+The install finished but `claude` doesn't work. The exact error varies by platform:
+
+| Platform    | Error message                                                          |
+| :---------- | :--------------------------------------------------------------------- |
+| macOS       | `zsh: command not found: claude`                                       |
+| Linux       | `bash: claude: command not found`                                      |
+| Windows CMD | `'claude' is not recognized as an internal or external command`        |
+| PowerShell  | `claude : The term 'claude' is not recognized as the name of a cmdlet` |
+
+This means the install directory isn't in your shell's search path. See [Verify your PATH](#verify-your-path) for the fix on each platform.
+
+### `curl: (56) Failure writing output to destination`
+
+The `curl ... | bash` command downloads the script and passes it directly to Bash for execution using a pipe (`|`). This error means the connection broke before the script finished downloading. Common causes include network interruptions, the download being blocked mid-stream, or system resource limits.
+
+**Solutions:**
+
+1. **Check network stability**: Claude Code binaries are hosted on Google Cloud Storage. Test that you can reach it:
+   ```bash  theme={null}
+   curl -fsSL https://storage.googleapis.com -o /dev/null
+   ```
+   If the command completes silently, your connection is fine and the issue is likely intermittent. Retry the install command. If you see an error, your network may be blocking the download.
+
+2. **Try an alternative install method**:
+
+   On macOS or Linux:
+
+   ```bash  theme={null}
+   brew install --cask claude-code
+   ```
+
+   On Windows:
+
+   ```powershell  theme={null}
+   winget install Anthropic.ClaudeCode
+   ```
+
+### TLS or SSL connection errors
+
+Errors like `curl: (35) TLS connect error`, `schannel: next InitializeSecurityContext failed`, or PowerShell's `Could not establish trust relationship for the SSL/TLS secure channel` indicate TLS handshake failures.
+
+**Solutions:**
+
+1. **Update your system CA certificates**:
+
+   On Ubuntu/Debian:
+
+   ```bash  theme={null}
+   sudo apt-get update && sudo apt-get install ca-certificates
+   ```
+
+   On macOS via Homebrew:
+
+   ```bash  theme={null}
+   brew install ca-certificates
+   ```
+
+2. **On Windows, enable TLS 1.2** in PowerShell before running the installer:
+   ```powershell  theme={null}
+   [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
+   irm https://claude.ai/install.ps1 | iex
+   ```
+
+3. **Check for proxy or firewall interference**: corporate proxies that perform TLS inspection can cause these errors, including `unable to get local issuer certificate`. Set `NODE_EXTRA_CA_CERTS` to your corporate CA certificate bundle:
+   ```bash  theme={null}
+   export NODE_EXTRA_CA_CERTS=/path/to/corporate-ca.pem
+   ```
+   Ask your IT team for the certificate file if you don't have it. You can also try on a direct connection to confirm the proxy is the cause.
+
+### `Failed to fetch version from storage.googleapis.com`
+
+The installer couldn't reach the download server. This typically means `storage.googleapis.com` is blocked on your network.
+
+**Solutions:**
+
+1. **Test connectivity directly**:
+   ```bash  theme={null}
+   curl -sI https://storage.googleapis.com
+   ```
+
+2. **If behind a proxy**, set `HTTPS_PROXY` so the installer can route through it. See [proxy configuration](/en/network-config#proxy-configuration) for details.
+   ```bash  theme={null}
+   export HTTPS_PROXY=http://proxy.example.com:8080
+   curl -fsSL https://claude.ai/install.sh | bash
+   ```
+
+3. **If on a restricted network**, try a different network or VPN, or use an alternative install method:
+
+   On macOS or Linux:
+
+   ```bash  theme={null}
+   brew install --cask claude-code
+   ```
+
+   On Windows:
+
+   ```powershell  theme={null}
+   winget install Anthropic.ClaudeCode
+   ```
+
+### Windows: `irm` or `&&` not recognized
+
+If you see `'irm' is not recognized` or `The token '&&' is not valid`, you're running the wrong command for your shell.
+
+* **`irm` not recognized**: you're in CMD, not PowerShell. You have two options:
+
+  Open PowerShell by searching for "PowerShell" in the Start menu, then run the original install command:
+
+  ```powershell  theme={null}
+  irm https://claude.ai/install.ps1 | iex
+  ```
+
+  Or stay in CMD and use the CMD installer instead:
+
+  ```batch  theme={null}
+  curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
+  ```
+
+* **`&&` not valid**: you're in PowerShell but ran the CMD installer command. Use the PowerShell installer:
+  ```powershell  theme={null}
+  irm https://claude.ai/install.ps1 | iex
+  ```
+
+### Install killed on low-memory Linux servers
+
+If you see `Killed` during installation on a VPS or cloud instance:
+
+```
+Setting up Claude Code...
+Installing Claude Code native build latest...
+bash: line 142: 34803 Killed    "$binary_path" install ${TARGET:+"$TARGET"}
+```
+
+The Linux OOM killer terminated the process because the system ran out of memory. Claude Code requires at least 4 GB of available RAM.
+
+**Solutions:**
+
+1. **Add swap space** if your server has limited RAM. Swap uses disk space as overflow memory, letting the install complete even with low physical RAM.
+
+   Create a 2 GB swap file and enable it:
+
+   ```bash  theme={null}
+   sudo fallocate -l 2G /swapfile
+   sudo chmod 600 /swapfile
+   sudo mkswap /swapfile
+   sudo swapon /swapfile
+   ```
+
+   Then retry the installation:
+
+   ```bash  theme={null}
+   curl -fsSL https://claude.ai/install.sh | bash
+   ```
+
+2. **Close other processes** to free memory before installing.
+
+3. **Use a larger instance** if possible. Claude Code requires at least 4 GB of RAM.
+
+### Install hangs in Docker
+
+When installing Claude Code in a Docker container, installing as root into `/` can cause hangs.
+
+**Solutions:**
+
+1. **Set a working directory** before running the installer. When run from `/`, the installer scans the entire filesystem, which causes excessive memory usage. Setting `WORKDIR` limits the scan to a small directory:
+   ```dockerfile  theme={null}
+   WORKDIR /tmp
+   RUN curl -fsSL https://claude.ai/install.sh | bash
+   ```
+
+2. **Increase Docker memory limits** if using Docker Desktop:
+   ```bash  theme={null}
+   docker build --memory=4g .
+   ```
+
+### Windows: Claude Desktop overrides `claude` CLI command
+
+If you installed an older version of Claude Desktop, it may register a `Claude.exe` in the `WindowsApps` directory that takes PATH priority over Claude Code CLI. Running `claude` opens the Desktop app instead of the CLI.
+
+Update Claude Desktop to the latest version to fix this issue.
+
+### Windows: "Claude Code on Windows requires git-bash"
+
+Claude Code on native Windows needs [Git for Windows](https://git-scm.com/downloads/win), which includes Git Bash.
+
+**If Git is not installed**, download and install it from [git-scm.com/downloads/win](https://git-scm.com/downloads/win). During setup, select "Add to PATH." Restart your terminal after installing.
+
+**If Git is already installed** but Claude Code still can't find it, set the path in your [settings.json file](/en/settings):
+
+```json  theme={null}
+{
+  "env": {
+    "CLAUDE_CODE_GIT_BASH_PATH": "C:\\Program Files\\Git\\bin\\bash.exe"
+  }
+}
+```
+
+If your Git is installed somewhere else, find the path by running `where.exe git` in PowerShell and use the `bin\bash.exe` path from that directory.
+
+### Linux: wrong binary variant installed (musl/glibc mismatch)
+
+If you see errors about missing shared libraries like `libstdc++.so.6` or `libgcc_s.so.1` after installation, the installer may have downloaded the wrong binary variant for your system.
+
+```
+Error loading shared library libstdc++.so.6: No such file or directory
+```
+
+This can happen on glibc-based systems that have musl cross-compilation packages installed, causing the installer to misdetect the system as musl.
+
+**Solutions:**
+
+1. **Check which libc your system uses**:
+   ```bash  theme={null}
+   ldd /bin/ls | head -1
+   ```
+   If it shows `linux-vdso.so` or references to `/lib/x86_64-linux-gnu/`, you're on glibc. If it shows `musl`, you're on musl.
+
+2. **If you're on glibc but got the musl binary**, remove the installation and reinstall. You can also manually download the correct binary from the GCS bucket at `https://storage.googleapis.com/claude-code-dist-86c565f3-f756-42ad-8dfa-d59b1c096819/claude-code-releases/{VERSION}/manifest.json`. File a [GitHub issue](https://github.com/anthropics/claude-code/issues) with the output of `ldd /bin/ls` and `ls /lib/libc.musl*`.
+
+3. **If you're actually on musl** (Alpine Linux), install the required packages:
+   ```bash  theme={null}
+   apk add libgcc libstdc++ ripgrep
+   ```
+
+### `Illegal instruction` on Linux
+
+If the installer prints `Illegal instruction` instead of the OOM `Killed` message, the downloaded binary doesn't match your CPU architecture. This commonly happens on ARM servers that receive an x86 binary, or on older CPUs that lack required instruction sets.
+
+```
+bash: line 142: 2238232 Illegal instruction    "$binary_path" install ${TARGET:+"$TARGET"}
+```
+
+**Solutions:**
+
+1. **Verify your architecture**:
+   ```bash  theme={null}
+   uname -m
+   ```
+   `x86_64` means 64-bit Intel/AMD, `aarch64` means ARM64. If the binary doesn't match, [file a GitHub issue](https://github.com/anthropics/claude-code/issues) with the output.
+
+2. **Try an alternative install method** while the architecture issue is resolved:
+   ```bash  theme={null}
+   brew install --cask claude-code
+   ```
+
+### `dyld: cannot load` on macOS
+
+If you see `dyld: cannot load` or `Abort trap: 6` during installation, the binary is incompatible with your macOS version or hardware.
+
+```
+dyld: cannot load 'claude-2.1.42-darwin-x64' (load command 0x80000034 is unknown)
+Abort trap: 6
+```
+
+**Solutions:**
+
+1. **Check your macOS version**: Claude Code requires macOS 13.0 or later. Open the Apple menu and select About This Mac to check your version.
+
+2. **Update macOS** if you're on an older version. The binary uses load commands that older macOS versions don't support.
+
+3. **Try Homebrew** as an alternative install method:
+   ```bash  theme={null}
+   brew install --cask claude-code
+   ```
+
 ### Windows installation issues: errors in WSL
 
 You might encounter the following issues in WSL:
 
-**OS/platform detection issues**: If you receive an error during installation, WSL may be using Windows `npm`. Try:
+**OS/platform detection issues**: if you receive an error during installation, WSL may be using Windows `npm`. Try:
 
 * Run `npm config set os linux` before installation
-* Install with `npm install -g @anthropic-ai/claude-code --force --no-os-check` (Do NOT use `sudo`)
-
-**Node not found errors**: If you see `exec: node: not found` when running `claude`, your WSL environment may be using a Windows installation of Node.js. You can confirm this with `which npm` and `which node`, which should point to Linux paths starting with `/usr/` rather than `/mnt/c/`. To fix this, try installing Node via your Linux distribution's package manager or via [`nvm`](https://github.com/nvm-sh/nvm).
-
-**nvm version conflicts**: If you have nvm installed in both WSL and Windows, you may experience version conflicts when switching Node versions in WSL. This happens because WSL imports the Windows PATH by default, causing Windows nvm/npm to take priority over the WSL installation.
+* Install with `npm install -g @anthropic-ai/claude-code --force --no-os-check`. Do not use `sudo`.
+
+**Node not found errors**: if you see `exec: node: not found` when running `claude`, your WSL environment may be using a Windows installation of Node.js. You can confirm this with `which npm` and `which node`, which should point to Linux paths starting with `/usr/` rather than `/mnt/c/`. To fix this, try installing Node via your Linux distribution's package manager or via [`nvm`](https://github.com/nvm-sh/nvm).
+
+**nvm version conflicts**: if you have nvm installed in both WSL and Windows, you may experience version conflicts when switching Node versions in WSL. This happens because WSL imports the Windows PATH by default, causing Windows nvm/npm to take priority over the WSL installation.
 
 You can identify this issue by:
 
@@ -54,7 +570,7 @@
 ```
 
 <Warning>
-  Avoid disabling Windows PATH importing (`appendWindowsPath = false`) as this breaks the ability to call Windows executables from WSL. Similarly, avoid uninstalling Node.js from Windows if you use it for Windows development.
+  Avoid disabling Windows PATH importing via `appendWindowsPath = false` as this breaks the ability to call Windows executables from WSL. Similarly, avoid uninstalling Node.js from Windows if you use it for Windows development.
 </Warning>
 
 ### WSL2 sandbox setup
@@ -77,92 +593,19 @@
 
 WSL1 does not support sandboxing. If you see "Sandboxing requires WSL2", you need to upgrade to WSL2 or run Claude Code without sandboxing.
 
-### Linux and Mac installation issues: permission or command not found errors
-
-When installing Claude Code with npm, `PATH` problems may prevent access to `claude`.
-You may also encounter permission errors if your npm global prefix is not user writable (for example, `/usr`, or `/usr/local`).
-
-#### Recommended solution: Native Claude Code installation
-
-Claude Code has a native installation that doesn't depend on npm or Node.js.
-
-Use the following command to run the native installer.
-
-**macOS, Linux, WSL:**
-
-```bash  theme={null}
-# Install stable version (default)
+### Permission errors during installation
+
+If the native installer fails with permission errors, the target directory may not be writable. See [Check directory permissions](#check-directory-permissions).
+
+If you previously installed with npm and are hitting npm-specific permission errors, switch to the native installer:
+
+```bash  theme={null}
 curl -fsSL https://claude.ai/install.sh | bash
-
-# Install latest version
-curl -fsSL https://claude.ai/install.sh | bash -s latest
-
-# Install specific version number
-curl -fsSL https://claude.ai/install.sh | bash -s 1.0.58
-```
-
-**Windows PowerShell:**
-
-```powershell  theme={null}
-# Install stable version (default)
-irm https://claude.ai/install.ps1 | iex
-
-# Install latest version
-& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) latest
-
-# Install specific version number
-& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) 1.0.58
-
-```
-
-This command installs the appropriate build of Claude Code for your operating system and architecture and adds a symlink to the installation at `~/.local/bin/claude` (or `%USERPROFILE%\.local\bin\claude.exe` on Windows).
-
-<Tip>
-  Make sure that you have the installation directory in your system PATH.
-</Tip>
-
-### Windows: "Claude Code on Windows requires git-bash"
-
-Claude Code on native Windows requires [Git for Windows](https://git-scm.com/downloads/win) which includes Git Bash. If Git is installed but not detected:
-
-1. Set the path explicitly in PowerShell before running Claude:
-   ```powershell  theme={null}
-   $env:CLAUDE_CODE_GIT_BASH_PATH="C:\Program Files\Git\bin\bash.exe"
-   ```
-
-2. Or add it to your system environment variables permanently through System Properties → Environment Variables.
-
-If Git is installed in a non-standard location, adjust the path accordingly.
-
-### Windows: "installMethod is native, but claude command not found"
-
-If you see this error after installation, the `claude` command isn't in your PATH. Add it manually:
-
-<Steps>
-  <Step title="Open Environment Variables">
-    Press `Win + R`, type `sysdm.cpl`, and press Enter. Click **Advanced** → **Environment Variables**.
-  </Step>
-
-  <Step title="Edit User PATH">
-    Under "User variables", select **Path** and click **Edit**. Click **New** and add:
-
-    ```
-    %USERPROFILE%\.local\bin
-    ```
-  </Step>
-
-  <Step title="Restart your terminal">
-    Close and reopen PowerShell or CMD for changes to take effect.
-  </Step>
-</Steps>
-
-Verify installation:
-
-```bash  theme={null}
-claude doctor # Check installation health
 ```
 
 ## Permissions and authentication
+
+These sections address login failures, token issues, and permission prompt behavior.
 
 ### Repeated permission prompts
 
@@ -179,36 +622,56 @@
 
 If the browser doesn't open automatically during login, press `c` to copy the OAuth URL to your clipboard, then paste it into your browser manually.
 
-If problems persist, try:
-
-```bash  theme={null}
-rm -rf ~/.config/claude-code/auth.json
+### OAuth error: Invalid code
+
+If you see `OAuth error: Invalid code. Please make sure the full code was copied`, the login code expired or was truncated during copy-paste.
+
+**Solutions:**
+
+* Press Enter to retry and complete the login quickly after the browser opens
+* Type `c` to copy the full URL if the browser doesn't open automatically
+* If using a remote/SSH session, the browser may open on the wrong machine. Copy the URL displayed in the terminal and open it in your local browser instead.
+
+### 403 Forbidden after login
+
+If you see `API Error: 403 {"error":{"type":"forbidden","message":"Request not allowed"}}` after logging in:
+
+* **Claude Pro/Max users**: verify your subscription is active at [claude.ai/settings](https://claude.ai/settings)
+* **Console users**: confirm your account has the "Claude Code" or "Developer" role assigned by your admin
+* **Behind a proxy**: corporate proxies can interfere with API requests. See [network configuration](/en/network-config) for proxy setup.
+
+### OAuth login fails in WSL2
+
+Browser-based login in WSL2 may fail if WSL can't open your Windows browser. Set the `BROWSER` environment variable:
+
+```bash  theme={null}
+export BROWSER="/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"
 claude
 ```
 
-This removes your stored authentication information and forces a clean login.
+Or copy the URL manually: when the login prompt appears, press `c` to copy the OAuth URL, then paste it into your Windows browser.
+
+### "Not logged in" or token expired
+
+If Claude Code prompts you to log in again after a session, your OAuth token may have expired.
+
+Run `/login` to re-authenticate. If this happens frequently, check that your system clock is accurate, as token validation depends on correct timestamps.
 
 ## Configuration file locations
 
 Claude Code stores configuration in several locations:
 
-| File                          | Purpose                                                  |
-| :---------------------------- | :------------------------------------------------------- |
-| `~/.claude/settings.json`     | User settings (permissions, hooks, model overrides)      |
-| `.claude/settings.json`       | Project settings (checked into source control)           |
-| `.claude/settings.local.json` | Local project settings (not committed)                   |
-| `~/.claude.json`              | Global state (theme, OAuth, MCP servers)                 |
-| `.mcp.json`                   | Project MCP servers (checked into source control)        |
-| `managed-settings.json`       | [Managed settings](/en/settings#settings-files)          |
-| `managed-mcp.json`            | [Managed MCP servers](/en/mcp#managed-mcp-configuration) |
+| File                          | Purpose                                                                                                |
+| :---------------------------- | :----------------------------------------------------------------------------------------------------- |
+| `~/.claude/settings.json`     | User settings (permissions, hooks, model overrides)                                                    |
+| `.claude/settings.json`       | Project settings (checked into source control)                                                         |
+| `.claude/settings.local.json` | Local project settings (not committed)                                                                 |
+| `~/.claude.json`              | Global state (theme, OAuth, MCP servers)                                                               |
+| `.mcp.json`                   | Project MCP servers (checked into source control)                                                      |
+| `managed-mcp.json`            | [Managed MCP servers](/en/mcp#managed-mcp-configuration)                                               |
+| Managed settings              | [Managed settings](/en/settings#settings-files) (server-managed, MDM/OS-level policies, or file-based) |
 
 On Windows, `~` refers to your user home directory, such as `C:\Users\YourName`.
-
-**Managed file locations:**
-
-* macOS: `/Library/Application Support/ClaudeCode/`
-* Linux/WSL: `/etc/claude-code/`
-* Windows: `C:\Program Files\ClaudeCode\`
 
 For details on configuring these files, see [Settings](/en/settings) and [MCP](/en/mcp).
 
@@ -232,6 +695,8 @@
 
 ## Performance and stability
 
+These sections cover issues related to resource usage, responsiveness, and search behavior.
+
 ### High CPU or memory usage
 
 Claude Code is designed to work with most development environments, but may consume significant resources when processing large codebases. If you're experiencing performance issues:
@@ -272,7 +737,7 @@
 
 ### Slow or incomplete search results on WSL
 
-Disk read performance penalties when [working across file systems on WSL](https://learn.microsoft.com/en-us/windows/wsl/filesystems) may result in fewer-than-expected matches (but not a complete lack of search functionality) when using Claude Code on WSL.
+Disk read performance penalties when [working across file systems on WSL](https://learn.microsoft.com/en-us/windows/wsl/filesystems) may result in fewer-than-expected matches when using Claude Code on WSL. Search still functions, but returns fewer results than on a native filesystem.
 
 <Note>
   `/doctor` will show Search as OK in this case.
@@ -280,14 +745,16 @@
 
 **Solutions:**
 
-1. **Submit more specific searches**: Reduce the number of files searched by specifying directories or file types: "Search for JWT validation logic in the auth-service package" or "Find use of md5 hash in JS files".
-
-2. **Move project to Linux filesystem**: If possible, ensure your project is located on the Linux filesystem (`/home/`) rather than the Windows filesystem (`/mnt/c/`).
-
-3. **Use native Windows instead**: Consider running Claude Code natively on Windows instead of through WSL, for better file system performance.
+1. **Submit more specific searches**: reduce the number of files searched by specifying directories or file types: "Search for JWT validation logic in the auth-service package" or "Find use of md5 hash in JS files".
+
+2. **Move project to Linux filesystem**: if possible, ensure your project is located on the Linux filesystem (`/home/`) rather than the Windows filesystem (`/mnt/c/`).
+
+3. **Use native Windows instead**: consider running Claude Code natively on Windows instead of through WSL, for better file system performance.
 
 ## IDE integration issues
 
+If Claude Code does not connect to your IDE or behaves unexpectedly within an IDE terminal, try the solutions below.
+
 ### JetBrains IDE not detected on WSL2
 
 If you're using Claude Code on WSL2 with JetBrains IDEs and getting "No available IDEs detected" errors, this is likely due to WSL2's networking configuration or Windows Firewall blocking the connection.
@@ -301,14 +768,14 @@
 1. Find your WSL2 IP address:
    ```bash  theme={null}
    wsl hostname -I
-   # Example output: 172.21.123.456
+   # Example output: 172.21.123.45
    ```
 
 2. Open PowerShell as Administrator and create a firewall rule:
    ```powershell  theme={null}
    New-NetFirewallRule -DisplayName "Allow WSL2 Internal Traffic" -Direction Inbound -Protocol TCP -Action Allow -RemoteAddress 172.21.0.0/16 -LocalAddress 172.21.0.0/16
    ```
-   (Adjust the IP range based on your WSL2 subnet from step 1)
+   Adjust the IP range based on your WSL2 subnet from step 1.
 
 3. Restart both your IDE and Claude Code
 
@@ -327,19 +794,19 @@
   These networking issues only affect WSL2. WSL1 uses the host's network directly and doesn't require these configurations.
 </Note>
 
-For additional JetBrains configuration tips, see our [JetBrains IDE guide](/en/jetbrains#plugin-settings).
-
-### Reporting Windows IDE integration issues (both native and WSL)
+For additional JetBrains configuration tips, see the [JetBrains IDE guide](/en/jetbrains#plugin-settings).
+
+### Report Windows IDE integration issues
 
 If you're experiencing IDE integration problems on Windows, [create an issue](https://github.com/anthropics/claude-code/issues) with the following information:
 
 * Environment type: native Windows (Git Bash) or WSL1/WSL2
-* WSL networking mode (if applicable): NAT or mirrored
+* WSL networking mode, if applicable: NAT or mirrored
 * IDE name and version
 * Claude Code extension/plugin version
 * Shell type: Bash, Zsh, PowerShell, etc.
 
-### Escape key not working in JetBrains (IntelliJ, PyCharm, etc.) terminals
+### Escape key not working in JetBrains IDE terminals
 
 If you're using Claude Code in JetBrains terminals and the `Esc` key doesn't interrupt the agent as expected, this is likely due to a keybinding clash with JetBrains' default shortcuts.
 
@@ -366,7 +833,7 @@
 function example() {
   return "hello";
 }
-```
+```text
 ````
 
 Instead of properly tagged blocks like:
@@ -376,16 +843,16 @@
 function example() {
   return "hello";
 }
-```
+```text
 ````
 
 **Solutions:**
 
-1. **Ask Claude to add language tags**: Request "Add appropriate language tags to all code blocks in this markdown file."
-
-2. **Use post-processing hooks**: Set up automatic formatting hooks to detect and add missing language tags. See [Auto-format code after edits](/en/hooks-guide#auto-format-code-after-edits) for an example of a PostToolUse formatting hook.
-
-3. **Manual verification**: After generating markdown files, review them for proper code block formatting and request corrections if needed.
+1. **Ask Claude to add language tags**: request "Add appropriate language tags to all code blocks in this markdown file."
+
+2. **Use post-processing hooks**: set up automatic formatting hooks to detect and add missing language tags. See [Auto-format code after edits](/en/hooks-guide#auto-format-code-after-edits) for an example of a PostToolUse formatting hook.
+
+3. **Manual verification**: after generating markdown files, review them for proper code block formatting and request corrections if needed.
 
 ### Inconsistent spacing and formatting
 
@@ -393,21 +860,21 @@
 
 **Solutions:**
 
-1. **Request formatting corrections**: Ask Claude to "Fix spacing and formatting issues in this markdown file."
-
-2. **Use formatting tools**: Set up hooks to run markdown formatters like `prettier` or custom formatting scripts on generated markdown files.
-
-3. **Specify formatting preferences**: Include formatting requirements in your prompts or project [memory](/en/memory) files.
-
-### Best practices for markdown generation
+1. **Request formatting corrections**: ask Claude to "Fix spacing and formatting issues in this markdown file."
+
+2. **Use formatting tools**: set up hooks to run markdown formatters like `prettier` or custom formatting scripts on generated markdown files.
+
+3. **Specify formatting preferences**: include formatting requirements in your prompts or project [memory](/en/memory) files.
+
+### Reduce markdown formatting issues
 
 To minimize formatting issues:
 
-* **Be explicit in requests**: Ask for "properly formatted markdown with language-tagged code blocks"
-* **Use project conventions**: Document your preferred markdown style in [`CLAUDE.md`](/en/memory)
-* **Set up validation hooks**: Use post-processing hooks to automatically verify and fix common formatting issues
-
-## Getting more help
+* **Be explicit in requests**: ask for "properly formatted markdown with language-tagged code blocks"
+* **Use project conventions**: document your preferred markdown style in [`CLAUDE.md`](/en/memory)
+* **Set up validation hooks**: use post-processing hooks to automatically verify and fix common formatting issues
+
+## Get more help
 
 If you're experiencing issues not covered here:
 

```
### https://code.claude.com/docs/en/best-practices.md

```diff
--- a/https://code.claude.com/docs/en/best-practices.md
+++ b/https://code.claude.com/docs/en/best-practices.md
@@ -148,7 +148,7 @@
   Run `/init` to generate a starter CLAUDE.md file based on your current project structure, then refine over time.
 </Tip>
 
-CLAUDE.md is a special file that Claude reads at the start of every conversation. Include Bash commands, code style, and workflow rules. This gives Claude persistent context **it can't infer from code alone**.
+CLAUDE.md is a special file that Claude reads at the start of every conversation. Include Bash commands, code style, and workflow rules. This gives Claude persistent context it can't infer from code alone.
 
 The `/init` command analyzes your codebase to detect build systems, test frameworks, and code patterns, giving you a solid foundation to refine.
 
@@ -194,9 +194,9 @@
 
 You can place CLAUDE.md files in several locations:
 
-* **Home folder (`~/.claude/CLAUDE.md`)**: Applies to all Claude sessions
-* **Project root (`./CLAUDE.md`)**: Check into git to share with your team, or name it `CLAUDE.local.md` and `.gitignore` it
-* **Parent directories**: Useful for monorepos where both `root/CLAUDE.md` and `root/foo/CLAUDE.md` are pulled in automatically
+* **Home folder (`~/.claude/CLAUDE.md`)**: applies to all Claude sessions
+* **Project root (`./CLAUDE.md`)**: check into git to share with your team, or name it `CLAUDE.local.md` and `.gitignore` it
+* **Parent directories**: useful for monorepos where both `root/CLAUDE.md` and `root/foo/CLAUDE.md` are pulled in automatically
 * **Child directories**: Claude pulls in child CLAUDE.md files on demand when working with files in those directories
 
 ### Configure permissions
@@ -207,8 +207,8 @@
 
 By default, Claude Code requests permission for actions that might modify your system: file writes, Bash commands, MCP tools, etc. This is safe but tedious. After the tenth approval you're not really reviewing anymore, you're just clicking through. There are two ways to reduce these interruptions:
 
-* **Permission allowlists**: Permit specific tools you know are safe (like `npm run lint` or `git commit`)
-* **Sandboxing**: Enable OS-level isolation that restricts filesystem and network access, allowing Claude to work more freely within defined boundaries
+* **Permission allowlists**: permit specific tools you know are safe (like `npm run lint` or `git commit`)
+* **Sandboxing**: enable OS-level isolation that restricts filesystem and network access, allowing Claude to work more freely within defined boundaries
 
 Alternatively, use `--dangerously-skip-permissions` to bypass all permission checks for contained workflows like fixing lint errors or generating boilerplate.
 
@@ -216,7 +216,7 @@
   Letting Claude run arbitrary commands can result in data loss, system corruption, or data exfiltration via prompt injection. Only use `--dangerously-skip-permissions` in a sandbox without internet access.
 </Warning>
 
-Read more about [configuring permissions](/en/settings) and [enabling sandboxing](/en/sandboxing#sandboxing).
+Read more about [configuring permissions](/en/permissions) and [enabling sandboxing](/en/sandboxing).
 
 ### Use CLI tools
 
@@ -356,7 +356,7 @@
 
 Claude asks about things you might not have considered yet, including technical implementation, UI/UX, edge cases, and tradeoffs.
 
-```
+```text  theme={null}
 I want to build [brief description]. Interview me in detail using the AskUserQuestion tool.
 
 Ask about technical implementation, UI/UX, edge cases, concerns, and tradeoffs. Don't ask obvious questions, dig into the hard parts I might not have considered.
@@ -380,10 +380,10 @@
 
 The best results come from tight feedback loops. Though Claude occasionally solves problems perfectly on the first attempt, correcting it quickly generally produces better solutions faster.
 
-* **`Esc`**: Stop Claude mid-action with the `Esc` key. Context is preserved, so you can redirect.
-* **`Esc + Esc` or `/rewind`**: Press `Esc` twice or run `/rewind` to open the rewind menu and restore previous conversation and code state, or summarize from a selected message.
-* **`"Undo that"`**: Have Claude revert its changes.
-* **`/clear`**: Reset context between unrelated tasks. Long sessions with irrelevant context can reduce performance.
+* **`Esc`**: stop Claude mid-action with the `Esc` key. Context is preserved, so you can redirect.
+* **`Esc + Esc` or `/rewind`**: press `Esc` twice or run `/rewind` to open the rewind menu and restore previous conversation and code state, or summarize from a selected message.
+* **`"Undo that"`**: have Claude revert its changes.
+* **`/clear`**: reset context between unrelated tasks. Long sessions with irrelevant context can reduce performance.
 
 If you've corrected Claude more than twice on the same issue in one session, the context is cluttered with failed approaches. Run `/clear` and start fresh with a more specific prompt that incorporates what you learned. A clean session with a better prompt almost always outperforms a long session with accumulated corrections.
 
@@ -411,7 +411,7 @@
 
 Since context is your fundamental constraint, subagents are one of the most powerful tools available. When Claude researches a codebase it reads lots of files, all of which consume your context. Subagents run in separate context windows and report back summaries:
 
-```
+```text  theme={null}
 Use subagents to investigate how our authentication system handles token
 refresh, and whether we have any existing OAuth utilities I should reuse.
 ```
@@ -420,7 +420,7 @@
 
 You can also use subagents for verification after Claude implements something:
 
-```
+```text  theme={null}
 use a subagent to review this code for edge cases
 ```
 
@@ -444,30 +444,30 @@
   Run `claude --continue` to pick up where you left off, or `--resume` to choose from recent sessions.
 </Tip>
 
-Claude Code saves conversations locally. When a task spans multiple sessions (you start a feature, get interrupted, come back the next day) you don't have to re-explain the context:
+Claude Code saves conversations locally. When a task spans multiple sessions, you don't have to re-explain the context:
 
 ```bash  theme={null}
 claude --continue    # Resume the most recent conversation
 claude --resume      # Select from recent conversations
 ```
 
-Use `/rename` to give sessions descriptive names (`"oauth-migration"`, `"debugging-memory-leak"`) so you can find them later. Treat sessions like branches. Different workstreams can have separate, persistent contexts.
+Use `/rename` to give sessions descriptive names like `"oauth-migration"` or `"debugging-memory-leak"` so you can find them later. Treat sessions like branches: different workstreams can have separate, persistent contexts.
 
 ***
 
 ## Automate and scale
 
-Once you're effective with one Claude, multiply your output with parallel sessions, headless mode, and fan-out patterns.
+Once you're effective with one Claude, multiply your output with parallel sessions, non-interactive mode, and fan-out patterns.
 
 Everything so far assumes one human, one Claude, and one conversation. But Claude Code scales horizontally. The techniques in this section show how you can get more done.
 
-### Run headless mode
+### Run non-interactive mode
 
 <Tip>
   Use `claude -p "prompt"` in CI, pre-commit hooks, or scripts. Add `--output-format stream-json` for streaming JSON output.
 </Tip>
 
-With `claude -p "your prompt"`, you can run Claude headlessly, without an interactive session. Headless mode is how you integrate Claude into CI pipelines, pre-commit hooks, or any automated workflow. The output formats (plain text, JSON, streaming JSON) let you parse results programmatically.
+With `claude -p "your prompt"`, you can run Claude non-interactively, without a session. Non-interactive mode is how you integrate Claude into CI pipelines, pre-commit hooks, or any automated workflow. The output formats let you parse results programmatically: plain text, JSON, or streaming JSON.
 
 ```bash  theme={null}
 # One-off queries
@@ -539,7 +539,7 @@
 
 Use `--verbose` for debugging during development, and turn it off in production.
 
-### Safe Autonomous Mode
+### Safe autonomous mode
 
 Use `claude --dangerously-skip-permissions` to bypass all permission checks and let Claude work uninterrupted. This works well for workflows like fixing lint errors or generating boilerplate code.
 
@@ -580,20 +580,7 @@
 
 ## Related resources
 
-<CardGroup cols={2}>
-  <Card title="How Claude Code works" icon="gear" href="/en/how-claude-code-works">
-    Understand the agentic loop, tools, and context management
-  </Card>
-
-  <Card title="Extend Claude Code" icon="puzzle-piece" href="/en/features-overview">
-    Choose between skills, hooks, MCP, subagents, and plugins
-  </Card>
-
-  <Card title="Common workflows" icon="list-check" href="/en/common-workflows">
-    Step-by-step recipes for debugging, testing, PRs, and more
-  </Card>
-
-  <Card title="CLAUDE.md" icon="file-lines" href="/en/memory">
-    Store project conventions and persistent context
-  </Card>
-</CardGroup>
+* [How Claude Code works](/en/how-claude-code-works): the agentic loop, tools, and context management
+* [Extend Claude Code](/en/features-overview): skills, hooks, MCP, subagents, and plugins
+* [Common workflows](/en/common-workflows): step-by-step recipes for debugging, testing, PRs, and more
+* [CLAUDE.md](/en/memory): store project conventions and persistent context

```
### https://code.claude.com/docs/en/skills.md

```diff
--- a/https://code.claude.com/docs/en/skills.md
+++ b/https://code.claude.com/docs/en/skills.md
@@ -58,13 +58,13 @@
 
     **Let Claude invoke it automatically** by asking something that matches the description:
 
-    ```
+    ```text  theme={null}
     How does this code work?
     ```
 
     **Or invoke it directly** with the skill name:
 
-    ```
+    ```text  theme={null}
     /explain-code src/auth/login.ts
     ```
 
@@ -76,12 +76,12 @@
 
 Where you store a skill determines who can use it:
 
-| Location   | Path                                                     | Applies to                     |
-| :--------- | :------------------------------------------------------- | :----------------------------- |
-| Enterprise | See [managed settings](/en/permissions#managed-settings) | All users in your organization |
-| Personal   | `~/.claude/skills/<skill-name>/SKILL.md`                 | All your projects              |
-| Project    | `.claude/skills/<skill-name>/SKILL.md`                   | This project only              |
-| Plugin     | `<plugin>/skills/<skill-name>/SKILL.md`                  | Where plugin is enabled        |
+| Location   | Path                                                | Applies to                     |
+| :--------- | :-------------------------------------------------- | :----------------------------- |
+| Enterprise | See [managed settings](/en/settings#settings-files) | All users in your organization |
+| Personal   | `~/.claude/skills/<skill-name>/SKILL.md`            | All your projects              |
+| Project    | `.claude/skills/<skill-name>/SKILL.md`              | This project only              |
+| Plugin     | `<plugin>/skills/<skill-name>/SKILL.md`             | Where plugin is enabled        |
 
 When skills share the same name across levels, higher-priority locations win: enterprise > personal > project. Plugin skills use a `plugin-name:skill-name` namespace, so they cannot conflict with other levels. If you have files in `.claude/commands/`, those work the same way, but if a skill and a command share the same name, the skill takes precedence.
 
@@ -91,7 +91,7 @@
 
 Each skill is a directory with `SKILL.md` as the entrypoint:
 
-```
+```text  theme={null}
 my-skill/
 ├── SKILL.md           # Main instructions (required)
 ├── template.md        # Template for Claude to fill in
@@ -213,7 +213,7 @@
 
 Skills can include multiple files in their directory. This keeps `SKILL.md` focused on the essentials while letting Claude access detailed reference material only when needed. Large reference docs, API specifications, or example collections don't need to load into context every time the skill runs.
 
-```
+```text  theme={null}
 my-skill/
 ├── SKILL.md (required - overview and navigation)
 ├── reference.md (detailed API docs - loaded when needed)
@@ -423,14 +423,14 @@
 
 **Disable all skills** by denying the Skill tool in `/permissions`:
 
-```
+```text  theme={null}
 # Add to deny rules:
 Skill
 ```
 
 **Allow or deny specific skills** using [permission rules](/en/permissions):
 
-```
+```text  theme={null}
 # Allow only specific skills
 Skill(commit)
 Skill(review-pr *)
@@ -453,7 +453,7 @@
 
 * **Project skills**: Commit `.claude/skills/` to version control
 * **Plugins**: Create a `skills/` directory in your [plugin](/en/plugins)
-* **Managed**: Deploy organization-wide through [managed settings](/en/permissions#managed-settings)
+* **Managed**: Deploy organization-wide through [managed settings](/en/settings#settings-files)
 
 ### Generate visual output
 
@@ -486,7 +486,7 @@
 
 ```bash
 python ~/.claude/skills/codebase-visualizer/scripts/visualize.py .
-```
+```text
 
 This creates `codebase-map.html` in the current directory and opens it in your default browser.
 

```
### https://code.claude.com/docs/en/data-usage.md

```diff
--- a/https://code.claude.com/docs/en/data-usage.md
+++ b/https://code.claude.com/docs/en/data-usage.md
@@ -51,7 +51,7 @@
 
 ## Data access
 
-For all first party users, you can learn more about what data is logged for [local Claude Code](#local-claude-code-data-flow-and-dependencies) and [remote Claude Code](#cloud-execution-data-flow-and-dependencies). Note for remote Claude Code, Claude accesses the repository where you initiate your Claude Code session. Claude does not access repositories that you have connected but have not started a session in.
+For all first party users, you can learn more about what data is logged for [local Claude Code](#local-claude-code-data-flow-and-dependencies) and [remote Claude Code](#cloud-execution-data-flow-and-dependencies). [Remote Control](/en/remote-control) sessions follow the local data flow since all execution happens on your machine. Note for remote Claude Code, Claude accesses the repository where you initiate your Claude Code session. Claude does not access repositories that you have connected but have not started a session in.
 
 ## Local Claude Code: Data flow and dependencies
 

```
### https://code.claude.com/docs/en/authentication.md

```diff
--- a/https://code.claude.com/docs/en/authentication.md
+++ b/https://code.claude.com/docs/en/authentication.md
@@ -4,13 +4,32 @@
 
 # Authentication
 
-> Learn how to configure user authentication and credential management for Claude Code in your organization.
+> Log in to Claude Code and configure authentication for individuals, teams, and organizations.
 
-## Authentication methods
+Claude Code supports multiple authentication methods depending on your setup. Individual users can log in with a Claude.ai account, while teams can use Claude for Teams or Enterprise, the Claude Console, or a cloud provider like Amazon Bedrock, Google Vertex AI, or Microsoft Foundry.
 
-Setting up Claude Code requires access to Anthropic models. For teams, you can set up Claude Code access in one of these ways:
+## Log in to Claude Code
 
-* [Claude for Teams or Enterprise](#claude-for-teams-or-enterprise) (recommended)
+After [installing Claude Code](/en/setup#install-claude-code), run `claude` in your terminal. On first launch, Claude Code opens a browser window for you to log in.
+
+If the browser doesn't open automatically, press `c` to copy the login URL to your clipboard, then paste it into your browser.
+
+You can authenticate with any of these account types:
+
+* **Claude Pro or Max subscription**: log in with your Claude.ai account. Subscribe at [claude.com/pricing](https://claude.com/pricing).
+* **Claude for Teams or Enterprise**: log in with the Claude.ai account your team admin invited you to.
+* **Claude Console**: log in with your Console credentials. Your admin must have [invited you](#claude-console-authentication) first.
+* **Cloud providers**: if your organization uses [Amazon Bedrock](/en/amazon-bedrock), [Google Vertex AI](/en/google-vertex-ai), or [Microsoft Foundry](/en/microsoft-foundry), set the required environment variables before running `claude`. No browser login is needed.
+
+To log out and re-authenticate, type `/logout` at the Claude Code prompt.
+
+If you're having trouble logging in, see [authentication troubleshooting](/en/troubleshooting#authentication-issues).
+
+## Set up team authentication
+
+For teams and organizations, you can configure Claude Code access in one of these ways:
+
+* [Claude for Teams or Enterprise](#claude-for-teams-or-enterprise), recommended for most teams
 * [Claude Console](#claude-console-authentication)
 * [Amazon Bedrock](/en/amazon-bedrock)
 * [Google Vertex AI](/en/google-vertex-ai)
@@ -49,7 +68,7 @@
   <Step title="Add users">
     You can add users through either method:
 
-    * Bulk invite users from within the Console (Console -> Settings -> Members -> Invite)
+    * Bulk invite users from within the Console: Settings -> Members -> Invite
     * [Set up SSO](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso)
   </Step>
 
@@ -65,14 +84,14 @@
 
     * Accept the Console invite
     * [Check system requirements](/en/setup#system-requirements)
-    * [Install Claude Code](/en/setup#installation)
+    * [Install Claude Code](/en/setup#install-claude-code)
     * Log in with Console account credentials
   </Step>
 </Steps>
 
 ### Cloud provider authentication
 
-For teams using Amazon Bedrock, Google Vertex AI, or Microsoft Azure:
+For teams using Amazon Bedrock, Google Vertex AI, or Microsoft Foundry:
 
 <Steps>
   <Step title="Follow provider setup">
@@ -84,7 +103,7 @@
   </Step>
 
   <Step title="Install Claude Code">
-    Users can [install Claude Code](/en/setup#installation).
+    Users can [install Claude Code](/en/setup#install-claude-code).
   </Step>
 </Steps>
 
@@ -92,13 +111,7 @@
 
 Claude Code securely manages your authentication credentials:
 
-* **Storage location**: on macOS, API keys, OAuth tokens, and other credentials are stored in the encrypted macOS Keychain.
+* **Storage location**: on macOS, credentials are stored in the encrypted macOS Keychain.
 * **Supported authentication types**: Claude.ai credentials, Claude API credentials, Azure Auth, Bedrock Auth, and Vertex Auth.
 * **Custom credential scripts**: the [`apiKeyHelper`](/en/settings#available-settings) setting can be configured to run a shell script that returns an API key.
 * **Refresh intervals**: by default, `apiKeyHelper` is called after 5 minutes or on HTTP 401 response. Set `CLAUDE_CODE_API_KEY_HELPER_TTL_MS` environment variable for custom refresh intervals.
-
-## See also
-
-* [Permissions](/en/permissions): configure what Claude Code can access and do
-* [Settings](/en/settings): complete configuration reference
-* [Security](/en/security): security safeguards and best practices

```
### https://code.claude.com/docs/en/how-claude-code-works.md

```diff
--- a/https://code.claude.com/docs/en/how-claude-code-works.md
+++ b/https://code.claude.com/docs/en/how-claude-code-works.md
@@ -34,7 +34,7 @@
 
 Tools are what make Claude Code agentic. Without tools, Claude can only respond with text. With tools, Claude can act: read your code, edit files, run commands, search the web, and interact with external services. Each tool use returns information that feeds back into the loop, informing Claude's next decision.
 
-The built-in tools generally fall into four categories, each representing a different kind of agency.
+The built-in tools generally fall into five categories, each representing a different kind of agency.
 
 | Category              | What Claude can do                                                                                                                                            |
 | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
@@ -61,8 +61,6 @@
 
 ## What Claude can access
 
-This guide focuses on the terminal. Claude Code also runs in [VS Code, JetBrains IDEs, and other environments](/en/ide-integrations).
-
 When you run `claude` in a directory, Claude Code gains access to:
 
 * **Your project.** Files in your directory and subdirectories, plus files elsewhere with your permission.
@@ -73,6 +71,24 @@
 
 Because Claude sees your whole project, it can work across it. When you ask Claude to "fix the authentication bug," it searches for relevant files, reads multiple files to understand context, makes coordinated edits across them, runs tests to verify the fix, and commits the changes if you ask. This is different from inline code assistants that only see the current file.
 
+## Environments and interfaces
+
+The agentic loop, tools, and capabilities described above are the same everywhere you use Claude Code. What changes is where the code executes and how you interact with it.
+
+### Execution environments
+
+Claude Code runs in three environments, each with different tradeoffs for where your code executes.
+
+| Environment        | Where code runs                         | Use case                                                   |
+| ------------------ | --------------------------------------- | ---------------------------------------------------------- |
+| **Local**          | Your machine                            | Default. Full access to your files, tools, and environment |
+| **Cloud**          | Anthropic-managed VMs                   | Offload tasks, work on repos you don't have locally        |
+| **Remote Control** | Your machine, controlled from a browser | Use the web UI while keeping everything local              |
+
+### Interfaces
+
+You can access Claude Code through the terminal, the [desktop app](/en/desktop), [IDE extensions](/en/ide-integrations), [claude.ai/code](https://claude.ai/code), [Remote Control](/en/remote-control), [Slack](/en/slack), and [CI/CD pipelines](/en/github-actions). The interface determines how you see and interact with Claude, but the underlying agentic loop is identical. See [Use Claude Code everywhere](/en/overview#use-claude-code-everywhere) for the full list.
+
 ## Work with sessions
 
 Claude Code saves your conversation locally as you work. Each message, tool use, and result is stored, which enables [rewinding](#undo-changes-with-checkpoints), [resuming, and forking](#resume-or-fork-sessions) sessions. Before Claude makes code changes, it also snapshots the affected files so you can revert if needed.

```
### https://code.claude.com/docs/en/github-actions.md

```diff
--- a/https://code.claude.com/docs/en/github-actions.md
+++ b/https://code.claude.com/docs/en/github-actions.md
@@ -200,7 +200,7 @@
 
 In issue or PR comments:
 
-```
+```text  theme={null}
 @claude implement this feature based on the issue description
 @claude how should I implement user authentication for this endpoint?
 @claude fix the TypeError in the user dashboard component

```
### https://code.claude.com/docs/en/memory.md

```diff
--- a/https://code.claude.com/docs/en/memory.md
+++ b/https://code.claude.com/docs/en/memory.md
@@ -37,7 +37,7 @@
 Auto memory is a persistent directory where Claude records learnings, patterns, and insights as it works. Unlike CLAUDE.md files that contain instructions you write for Claude, auto memory contains notes Claude writes for itself based on what it discovers during sessions.
 
 <Note>
-  Auto memory is being rolled out gradually. If you aren't seeing auto memory, you can opt in by setting `CLAUDE_CODE_DISABLE_AUTO_MEMORY=0` in your environment.
+  Auto memory is enabled by default. To toggle it on or off, use `/memory` and select the auto-memory toggle.
 </Note>
 
 ### What Claude remembers
@@ -73,11 +73,27 @@
 
 ### Manage auto memory
 
-Auto memory files are markdown files you can edit at any time. Use `/memory` to open the file selector, which includes your auto memory entrypoint alongside your CLAUDE.md files.
+Auto memory files are markdown files you can edit at any time. Use `/memory` to open the file selector, which includes your auto memory entrypoint alongside your CLAUDE.md files. The `/memory` selector also includes an auto-memory toggle to turn the feature on or off.
 
 To ask Claude to save something specific, tell it directly: "remember that we use pnpm, not npm" or "save to memory that the API tests require a local Redis instance".
 
-When neither variable is set, auto memory follows the gradual rollout. The variable name uses double-negative logic: `DISABLE=0` means "don't disable" and forces auto memory on.
+You can also control auto memory through settings or environment variables.
+
+Disable auto memory for all projects by adding `autoMemoryEnabled` to your user settings:
+
+```json  theme={null}
+// ~/.claude/settings.json
+{ "autoMemoryEnabled": false }
+```
+
+Disable auto memory for a single project by adding `autoMemoryEnabled` to the project settings:
+
+```json  theme={null}
+// .claude/settings.json
+{ "autoMemoryEnabled": false }
+```
+
+Override all other settings with the `CLAUDE_CODE_DISABLE_AUTO_MEMORY` environment variable. This takes precedence over both the `/memory` toggle and `settings.json`, making it useful for CI or managed environments:
 
 ```bash  theme={null}
 export CLAUDE_CODE_DISABLE_AUTO_MEMORY=1  # Force off

```
### https://code.claude.com/docs/en/vs-code.md

```diff
--- a/https://code.claude.com/docs/en/vs-code.md
+++ b/https://code.claude.com/docs/en/vs-code.md
@@ -14,6 +14,8 @@
 
 ## Prerequisites
 
+Before installing, make sure you have:
+
 * VS Code 1.98.0 or higher
 * An Anthropic account (you'll sign in when you first open the extension). If you're using a third-party provider like Amazon Bedrock or Google Vertex AI, see [Use third-party providers](#use-third-party-providers) instead.
 
@@ -47,7 +49,7 @@
     Other ways to open Claude Code:
 
     * **Command Palette**: `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux), type "Claude Code", and select an option like "Open in New Tab"
-    * **Status Bar**: Click **✱ Claude Code** in the bottom-right corner of the window. This works even when no file is open.
+    * **Status Bar**: click **✱ Claude Code** in the bottom-right corner of the window. This works even when no file is open.
 
     When you first open the panel, a **Learn Claude Code** checklist appears. Work through each item by clicking **Show me**, or dismiss it with the X. To reopen it later, uncheck **Hide Onboarding** in VS Code settings under Extensions → Claude Code.
 
@@ -81,17 +83,17 @@
 
 The prompt box supports several features:
 
-* **Permission modes**: Click the mode indicator at the bottom of the prompt box to switch modes. In normal mode, Claude asks permission before each action. In Plan mode, Claude describes what it will do and waits for approval before making changes. In auto-accept mode, Claude makes edits without asking. Set the default in VS Code settings under `claudeCode.initialPermissionMode`.
-* **Command menu**: Click `/` or type `/` to open the command menu. Options include attaching files, switching models, toggling extended thinking, and viewing plan usage (`/usage`). The Customize section provides access to MCP servers, hooks, memory, permissions, and plugins. Items with a terminal icon open in the integrated terminal.
-* **Context indicator**: The prompt box shows how much of Claude's context window you're using. Claude automatically compacts when needed, or you can run `/compact` manually.
-* **Extended thinking**: Lets Claude spend more time reasoning through complex problems. Toggle it on via the command menu (`/`). See [Extended thinking](/en/common-workflows#use-extended-thinking-thinking-mode) for details.
-* **Multi-line input**: Press `Shift+Enter` to add a new line without sending. This also works in the "Other" free-text input of question dialogs.
+* **Permission modes**: click the mode indicator at the bottom of the prompt box to switch modes. In normal mode, Claude asks permission before each action. In Plan mode, Claude describes what it will do and waits for approval before making changes. In auto-accept mode, Claude makes edits without asking. Set the default in VS Code settings under `claudeCode.initialPermissionMode`.
+* **Command menu**: click `/` or type `/` to open the command menu. Options include attaching files, switching models, toggling extended thinking, and viewing plan usage (`/usage`). The Customize section provides access to MCP servers, hooks, memory, permissions, and plugins. Items with a terminal icon open in the integrated terminal.
+* **Context indicator**: the prompt box shows how much of Claude's context window you're using. Claude automatically compacts when needed, or you can run `/compact` manually.
+* **Extended thinking**: lets Claude spend more time reasoning through complex problems. Toggle it on via the command menu (`/`). See [Extended thinking](/en/common-workflows#use-extended-thinking-thinking-mode) for details.
+* **Multi-line input**: press `Shift+Enter` to add a new line without sending. This also works in the "Other" free-text input of question dialogs.
 
 ### Reference files and folders
 
 Use @-mentions to give Claude context about specific files or folders. When you type `@` followed by a file or folder name, Claude reads that content and can answer questions about it or make changes to it. Claude Code supports fuzzy matching, so you can type partial names to find what you need:
 
-```
+```text  theme={null}
 > Explain the logic in @auth (fuzzy matches auth.js, AuthService.ts, etc.)
 > What's in @src/components/ (include a trailing slash for folders)
 ```
@@ -136,9 +138,9 @@
 
 You can drag the Claude panel to reposition it anywhere in VS Code. Grab the panel's tab or title bar and drag it to:
 
-* **Secondary sidebar**: The right side of the window. Keeps Claude visible while you code.
-* **Primary sidebar**: The left sidebar with icons for Explorer, Search, etc.
-* **Editor area**: Opens Claude as a tab alongside your files. Useful for side tasks.
+* **Secondary sidebar**: the right side of the window. Keeps Claude visible while you code.
+* **Primary sidebar**: the left sidebar with icons for Explorer, Search, etc.
+* **Editor area**: opens Claude as a tab alongside your files. Useful for side tasks.
 
 <Tip>
   Use the sidebar for your main Claude session and open additional tabs for side tasks. Claude remembers your preferred location. Note that the Spark icon only appears in the Activity Bar when the Claude panel is docked to the left. Since Claude defaults to the right side, use the Editor Toolbar icon to open Claude.
@@ -173,9 +175,9 @@
 
 When you install a plugin, choose the installation scope:
 
-* **Install for you**: Available in all your projects (user scope)
-* **Install for this project**: Shared with project collaborators (project scope)
-* **Install locally**: Only for you, only in this repository (local scope)
+* **Install for you**: available in all your projects (user scope)
+* **Install for this project**: shared with project collaborators (project scope)
+* **Install locally**: only for you, only in this repository (local scope)
 
 ### Manage marketplaces
 
@@ -235,8 +237,8 @@
 
 The extension has two types of settings:
 
-* **Extension settings** in VS Code: Control the extension's behavior within VS Code. Open with `Cmd+,` (Mac) or `Ctrl+,` (Windows/Linux), then go to Extensions → Claude Code. You can also type `/` and select **General Config** to open settings.
-* **Claude Code settings** in `~/.claude/settings.json`: Shared between the extension and CLI. Use for allowed commands, environment variables, hooks, and MCP servers. See [Settings](/en/settings) for details.
+* **Extension settings** in VS Code: control the extension's behavior within VS Code. Open with `Cmd+,` (Mac) or `Ctrl+,` (Windows/Linux), then go to Extensions → Claude Code. You can also type `/` and select **General Config** to open settings.
+* **Claude Code settings** in `~/.claude/settings.json`: shared between the extension and CLI. Use for allowed commands, environment variables, hooks, and MCP servers. See [Settings](/en/settings) for details.
 
 <Tip>
   Add `"$schema": "https://json.schemastore.org/claude-code-settings.json"` to your `settings.json` to get autocomplete and inline validation for all available settings directly in VS Code.
@@ -320,7 +322,7 @@
 
 Claude can stage changes, write commit messages, and create pull requests based on your work:
 
-```
+```text  theme={null}
 > commit my changes with a descriptive message
 > create a pr for this feature
 > summarize the changes I've made to the auth module
@@ -330,10 +332,10 @@
 
 ### Use git worktrees for parallel tasks
 
-Use the `--worktree` flag to start Claude in an isolated worktree with its own files and branch:
+Use the `--worktree` (`-w`) flag to start Claude in an isolated worktree with its own files and branch:
 
 ```bash  theme={null}
-claude -w feature-auth
+claude --worktree feature-auth
 ```
 
 Each worktree maintains independent file state while sharing git history. This prevents Claude instances from interfering with each other when working on different tasks. For more details, see [Run parallel sessions with Git worktrees](/en/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees).

```
### https://code.claude.com/docs/en/sandboxing.md

```diff
--- a/https://code.claude.com/docs/en/sandboxing.md
+++ b/https://code.claude.com/docs/en/sandboxing.md
@@ -89,7 +89,7 @@
 
 You can enable sandboxing by running the `/sandbox` command:
 
-```
+```text  theme={null}
 > /sandbox
 ```
 

```
### https://code.claude.com/docs/en/desktop.md

```diff
--- a/https://code.claude.com/docs/en/desktop.md
+++ b/https://code.claude.com/docs/en/desktop.md
@@ -369,9 +369,9 @@
 
 Managed settings override project and user settings and apply when Desktop spawns CLI sessions. You can set these keys in your organization's [managed settings](/en/settings#settings-precedence) file or push them remotely through the admin console.
 
-| Key                            | Description                                                                                                                     |
-| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
-| `disableBypassPermissionsMode` | set to `"disable"` to prevent users from enabling Bypass permissions mode. See [permissions](/en/permissions#managed-settings). |
+| Key                            | Description                                                                                                                               |
+| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
+| `disableBypassPermissionsMode` | set to `"disable"` to prevent users from enabling Bypass permissions mode. See [managed settings](/en/permissions#managed-only-settings). |
 
 For the complete list of managed-only settings including `allowManagedPermissionRulesOnly` and `allowManagedHooksOnly`, see [managed-only settings](/en/permissions#managed-only-settings).
 
@@ -463,6 +463,8 @@
 
 ### What's not available in Desktop
 
+The following features are only available in the CLI or VS Code extension:
+
 * **Third-party providers**: Desktop connects to Anthropic's API directly. Use the [CLI](/en/quickstart) with Bedrock, Vertex, or Foundry instead.
 * **Linux**: the desktop app is available on macOS and Windows only.
 * **Inline code suggestions**: Desktop does not provide autocomplete-style suggestions. It works through conversational prompts and explicit code changes.

```
### https://code.claude.com/docs/en/gitlab-ci-cd.md

```diff
--- a/https://code.claude.com/docs/en/gitlab-ci-cd.md
+++ b/https://code.claude.com/docs/en/gitlab-ci-cd.md
@@ -126,7 +126,7 @@
 
 In an issue comment:
 
-```
+```text  theme={null}
 @claude implement this feature based on the issue description
 ```
 
@@ -136,7 +136,7 @@
 
 In an MR discussion:
 
-```
+```text  theme={null}
 @claude suggest a concrete approach to cache the results of this API call
 ```
 
@@ -146,7 +146,7 @@
 
 In an issue or MR comment:
 
-```
+```text  theme={null}
 @claude fix the TypeError in the user dashboard component
 ```
 

```
### https://code.claude.com/docs/en/overview.md

```diff
--- a/https://code.claude.com/docs/en/overview.md
+++ b/https://code.claude.com/docs/en/overview.md
@@ -22,21 +22,23 @@
       <Tab title="Native Install (Recommended)">
         **macOS, Linux, WSL:**
 
-        ```bash theme={null} theme={null}
+        ```bash  theme={null}
         curl -fsSL https://claude.ai/install.sh | bash
         ```
 
         **Windows PowerShell:**
 
-        ```powershell theme={null} theme={null}
+        ```powershell  theme={null}
         irm https://claude.ai/install.ps1 | iex
         ```
 
         **Windows CMD:**
 
-        ```batch theme={null} theme={null}
+        ```batch  theme={null}
         curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
         ```
+
+        **Windows requires [Git for Windows](https://git-scm.com/downloads/win).** Install it first if you don't have it.
 
         <Info>
           Native installations automatically update in the background to keep you on the latest version.
@@ -44,7 +46,7 @@
       </Tab>
 
       <Tab title="Homebrew">
-        ```sh theme={null} theme={null}
+        ```bash  theme={null}
         brew install --cask claude-code
         ```
 
@@ -54,7 +56,7 @@
       </Tab>
 
       <Tab title="WinGet">
-        ```powershell theme={null} theme={null}
+        ```powershell  theme={null}
         winget install Anthropic.ClaudeCode
         ```
 
@@ -187,6 +189,7 @@
   <Accordion title="Work from anywhere" icon="globe">
     Sessions aren't tied to a single surface. Move work between environments as your context changes:
 
+    * Step away from your desk and keep working from your phone or any browser with [Remote Control](/en/remote-control)
     * Kick off a long-running task on the [web](/en/claude-code-on-the-web) or [iOS app](https://apps.apple.com/app/claude-by-anthropic/id6473753684), then pull it into your terminal with `/teleport`
     * Hand off a terminal session to the [Desktop app](/en/desktop) with `/desktop` for visual diff review
     * Route tasks from team chat: mention `@Claude` in [Slack](/en/slack) with a bug report and get a pull request back
@@ -199,13 +202,14 @@
 
 Beyond the [Terminal](/en/quickstart), [VS Code](/en/vs-code), [JetBrains](/en/jetbrains), [Desktop](/en/desktop), and [Web](/en/claude-code-on-the-web) environments above, Claude Code integrates with CI/CD, chat, and browser workflows:
 
-| I want to...                                  | Best option                                                                                                        |
-| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
-| Start a task locally, continue on mobile      | [Web](/en/claude-code-on-the-web) or [Claude iOS app](https://apps.apple.com/app/claude-by-anthropic/id6473753684) |
-| Automate PR reviews and issue triage          | [GitHub Actions](/en/github-actions) or [GitLab CI/CD](/en/gitlab-ci-cd)                                           |
-| Route bug reports from Slack to pull requests | [Slack](/en/slack)                                                                                                 |
-| Debug live web applications                   | [Chrome](/en/chrome)                                                                                               |
-| Build custom agents for your own workflows    | [Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview)                                                |
+| I want to...                                             | Best option                                                                                                        |
+| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
+| Continue a local session from my phone or another device | [Remote Control](/en/remote-control)                                                                               |
+| Start a task locally, continue on mobile                 | [Web](/en/claude-code-on-the-web) or [Claude iOS app](https://apps.apple.com/app/claude-by-anthropic/id6473753684) |
+| Automate PR reviews and issue triage                     | [GitHub Actions](/en/github-actions) or [GitLab CI/CD](/en/gitlab-ci-cd)                                           |
+| Route bug reports from Slack to pull requests            | [Slack](/en/slack)                                                                                                 |
+| Debug live web applications                              | [Chrome](/en/chrome)                                                                                               |
+| Build custom agents for your own workflows               | [Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview)                                                |
 
 ## Next steps
 

```
### https://code.claude.com/docs/en/interactive-mode.md

```diff
--- a/https://code.claude.com/docs/en/interactive-mode.md
+++ b/https://code.claude.com/docs/en/interactive-mode.md
@@ -13,9 +13,9 @@
 
   **macOS users**: Option/Alt key shortcuts (`Alt+B`, `Alt+F`, `Alt+Y`, `Alt+M`, `Alt+P`) require configuring Option as Meta in your terminal:
 
-  * **iTerm2**: Settings → Profiles → Keys → Set Left/Right Option key to "Esc+"
-  * **Terminal.app**: Settings → Profiles → Keyboard → Check "Use Option as Meta Key"
-  * **VS Code**: Settings → Profiles → Keys → Set Left/Right Option key to "Esc+"
+  * **iTerm2**: settings → Profiles → Keys → set Left/Right Option key to "Esc+"
+  * **Terminal.app**: settings → Profiles → Keyboard → check "Use Option as Meta Key"
+  * **VS Code**: settings → Profiles → Keys → set Left/Right Option key to "Esc+"
 
   See [Terminal configuration](/en/terminal-config) for details.
 </Note>
@@ -108,13 +108,13 @@
 | `/model`                  | Select or change the AI model. With Opus 4.6, use left/right arrows to [adjust effort level](/en/model-config#adjust-effort-level). The change takes effect immediately without waiting for the current response to finish |
 | `/permissions`            | View or update [permissions](/en/permissions#manage-permissions)                                                                                                                                                           |
 | `/plan`                   | Enter plan mode directly from the prompt                                                                                                                                                                                   |
-| `/rename <name>`          | Rename the current session for easier identification                                                                                                                                                                       |
+| `/rename [name]`          | Rename the current session. Without a name, generates one from conversation history (requires at least one message in the conversation context).                                                                           |
 | `/resume [session]`       | Resume a conversation by ID or name, or open the session picker                                                                                                                                                            |
 | `/rewind`                 | Rewind the conversation and/or code, or summarize from a selected message                                                                                                                                                  |
 | `/stats`                  | Visualize daily usage, session history, streaks, and model preferences                                                                                                                                                     |
 | `/status`                 | Open the Settings interface (Status tab) showing version, model, account, and connectivity                                                                                                                                 |
 | `/statusline`             | Set up Claude Code's status line UI                                                                                                                                                                                        |
-| `/copy`                   | Copy the last assistant response to clipboard                                                                                                                                                                              |
+| `/copy`                   | Copy the last response to clipboard. When code blocks are present, shows an interactive picker to select individual code blocks or the full response                                                                       |
 | `/tasks`                  | List and manage background tasks                                                                                                                                                                                           |
 | `/teleport`               | Resume a remote session from claude.ai (subscribers only)                                                                                                                                                                  |
 | `/desktop`                | Hand off the current CLI session to the Claude Code Desktop app (macOS and Windows only)                                                                                                                                   |
@@ -204,18 +204,18 @@
 
 Claude Code maintains command history for the current session:
 
-* History is stored per working directory
-* Cleared with `/clear` command
+* Input history is stored per working directory
+* Input history resets when you run `/clear` to start a new session. The previous session's conversation is preserved and can be resumed.
 * Use Up/Down arrows to navigate (see keyboard shortcuts above)
-* **Note**: History expansion (`!`) is disabled by default
+* **Note**: history expansion (`!`) is disabled by default
 
 ### Reverse search with Ctrl+R
 
 Press `Ctrl+R` to interactively search through your command history:
 
-1. **Start search**: Press `Ctrl+R` to activate reverse history search
-2. **Type query**: Enter text to search for in previous commands - the search term will be highlighted in matching results
-3. **Navigate matches**: Press `Ctrl+R` again to cycle through older matches
+1. **Start search**: press `Ctrl+R` to activate reverse history search
+2. **Type query**: enter text to search for in previous commands. The search term is highlighted in matching results
+3. **Navigate matches**: press `Ctrl+R` again to cycle through older matches
 4. **Accept match**:
    * Press `Tab` or `Esc` to accept the current match and continue editing
    * Press `Enter` to accept and execute the command immediately
@@ -223,7 +223,7 @@
    * Press `Ctrl+C` to cancel and restore your original input
    * Press `Backspace` on empty search to cancel
 
-The search displays matching commands with the search term highlighted, making it easy to find and reuse previous inputs.
+The search displays matching commands with the search term highlighted, so you can find and reuse previous inputs.
 
 ## Background bash commands
 

```
### https://code.claude.com/docs/en/statusline.md

```diff
--- a/https://code.claude.com/docs/en/statusline.md
+++ b/https://code.claude.com/docs/en/statusline.md
@@ -31,7 +31,7 @@
 
 The `/statusline` command accepts natural language instructions describing what you want displayed. Claude Code generates a script file in `~/.claude/` and updates your settings automatically:
 
-```
+```text  theme={null}
 /statusline show model name and context percentage with a progress bar
 ```
 

```
### https://code.claude.com/docs/en/plugins.md

```diff
--- a/https://code.claude.com/docs/en/plugins.md
+++ b/https://code.claude.com/docs/en/plugins.md
@@ -205,7 +205,7 @@
 
 Add a `skills/` directory at your plugin root with Skill folders containing `SKILL.md` files:
 
-```
+```text  theme={null}
 my-plugin/
 ├── .claude-plugin/
 │   └── plugin.json

```
### https://code.claude.com/docs/en/security.md

```diff
--- a/https://code.claude.com/docs/en/security.md
+++ b/https://code.claude.com/docs/en/security.md
@@ -106,6 +106,8 @@
 
 For more details on cloud execution, see [Claude Code on the web](/en/claude-code-on-the-web).
 
+[Remote Control](/en/remote-control) sessions work differently: the web interface connects to a Claude Code process running on your local machine. All code execution and file access stays local, and the same data that flows during any local Claude Code session travels through the Anthropic API over TLS. No cloud VMs or sandboxing are involved. The connection uses multiple short-lived, narrowly scoped credentials, each limited to a specific purpose and expiring independently, to limit the blast radius of any single compromised credential.
+
 ## Security best practices
 
 ### Working with sensitive code
@@ -117,7 +119,7 @@
 
 ### Team security
 
-* Use [managed settings](/en/permissions#managed-settings) to enforce organizational standards
+* Use [managed settings](/en/settings#settings-files) to enforce organizational standards
 * Share approved permission configurations through version control
 * Train team members on security best practices
 * Monitor Claude Code usage through [OpenTelemetry metrics](/en/monitoring-usage)

```
### https://code.claude.com/docs/en/claude-code-on-the-web.md

```diff
--- a/https://code.claude.com/docs/en/claude-code-on-the-web.md
+++ b/https://code.claude.com/docs/en/claude-code-on-the-web.md
@@ -20,9 +20,9 @@
 * **Repositories not on your local machine**: Work on code you don't have checked out locally
 * **Backend changes**: Where Claude Code can write tests and then write code to pass those tests
 
-Claude Code is also available on the Claude iOS app for kicking off tasks on the go and monitoring work in progress.
-
-You can move between local and remote development: [send tasks from your terminal to run on the web](#from-terminal-to-web) with the `&` prefix, or [teleport web sessions back to your terminal](#from-web-to-terminal) to continue locally.
+Claude Code is also available on the Claude app for [iOS](https://apps.apple.com/us/app/claude-by-anthropic/id6473753684) and [Android](https://play.google.com/store/apps/details?id=com.anthropic.claude) for kicking off tasks on the go and monitoring work in progress.
+
+You can [kick off new tasks on the web from your terminal](#from-terminal-to-web) with `--remote`, or [teleport web sessions back to your terminal](#from-web-to-terminal) to continue locally. To use the web interface while running Claude Code on your own machine instead of cloud infrastructure, see [Remote Control](/en/remote-control).
 
 ## Who can use Claude Code on the web?
 
@@ -69,50 +69,44 @@
 
 ## Moving tasks between web and terminal
 
-You can start tasks on the web and continue them in your terminal, or send tasks from your terminal to run on the web. Web sessions persist even if you close your laptop, and you can monitor them from anywhere including the Claude iOS app.
+You can start new tasks on the web from your terminal, or pull web sessions into your terminal to continue locally. Web sessions persist even if you close your laptop, and you can monitor them from anywhere including the Claude mobile app.
 
 <Note>
-  Session handoff is one-way: you can pull web sessions into your terminal, but you can't push an existing terminal session to the web. The [`&` prefix](#from-terminal-to-web) creates a *new* web session with your current conversation context.
+  Session handoff is one-way: you can pull web sessions into your terminal, but you can't push an existing terminal session to the web. The `--remote` flag creates a *new* web session for your current repository.
 </Note>
 
 ### From terminal to web
 
-Start a message with `&` inside Claude Code to send a task to run on the web:
-
-```
-& Fix the authentication bug in src/auth/login.ts
-```
-
-This creates a new web session on claude.ai with your current conversation context. The task runs in the cloud while you continue working locally. Use `/tasks` to check progress, or open the session on claude.ai or the Claude iOS app to interact directly. From there you can steer Claude, provide feedback, or answer questions just like any other conversation.
-
-You can also start a web session directly from the command line:
+Start a web session from the command line with the `--remote` flag:
 
 ```bash  theme={null}
 claude --remote "Fix the authentication bug in src/auth/login.ts"
 ```
 
-#### Tips for background tasks
-
-**Plan locally, execute remotely**: For complex tasks, start Claude in plan mode to collaborate on the approach before sending work to the web:
+This creates a new web session on claude.ai. The task runs in the cloud while you continue working locally. Use `/tasks` to check progress, or open the session on claude.ai or the Claude mobile app to interact directly. From there you can steer Claude, provide feedback, or answer questions just like any other conversation.
+
+#### Tips for remote tasks
+
+**Plan locally, execute remotely**: For complex tasks, start Claude in plan mode to collaborate on the approach, then send work to the web:
 
 ```bash  theme={null}
 claude --permission-mode plan
 ```
 
-In plan mode, Claude can only read files and explore the codebase. Once you're satisfied with the plan, send it to the web for autonomous execution:
-
+In plan mode, Claude can only read files and explore the codebase. Once you're satisfied with the plan, start a remote session for autonomous execution:
+
+```bash  theme={null}
+claude --remote "Execute the migration plan in docs/migration-plan.md"
 ```
-& Execute the migration plan we discussed
-```
 
 This pattern gives you control over the strategy while letting Claude execute autonomously in the cloud.
 
-**Run tasks in parallel**: Each `&` command creates its own web session that runs independently. You can kick off multiple tasks and they'll all run simultaneously in separate sessions:
-
-```
-& Fix the flaky test in auth.spec.ts
-& Update the API documentation
-& Refactor the logger to use structured output
+**Run tasks in parallel**: Each `--remote` command creates its own web session that runs independently. You can kick off multiple tasks and they'll all run simultaneously in separate sessions:
+
+```bash  theme={null}
+claude --remote "Fix the flaky test in auth.spec.ts"
+claude --remote "Update the API documentation"
+claude --remote "Refactor the logger to use structured output"
 ```
 
 Monitor all sessions with `/tasks`. When a session completes, you can create a PR from the web interface or [teleport](#from-web-to-terminal) the session to your terminal to continue working.
@@ -232,12 +226,12 @@
 
 **To update an existing environment:** Select the current environment, to the right of the environment name, and select the settings button. This will open a dialog where you can update the environment name, network access, and environment variables.
 
-**To select your default environment from the terminal:** If you have multiple environments configured, run `/remote-env` to choose which one to use when starting web sessions from your terminal with `&` or `--remote`. With a single environment, this command shows your current configuration.
+**To select your default environment from the terminal:** If you have multiple environments configured, run `/remote-env` to choose which one to use when starting web sessions from your terminal with `--remote`. With a single environment, this command shows your current configuration.
 
 <Note>
   Environment variables must be specified as key-value pairs, in [`.env` format](https://www.dotenv.org/). For example:
 
-  ```
+  ```text  theme={null}
   API_KEY=your_api_key
   DEBUG=true
   ```

```
### https://code.claude.com/docs/en/permissions.md

```diff
--- a/https://code.claude.com/docs/en/permissions.md
+++ b/https://code.claude.com/docs/en/permissions.md
@@ -135,20 +135,20 @@
 
 Read and Edit rules both follow the [gitignore](https://git-scm.com/docs/gitignore) specification with four distinct pattern types:
 
-| Pattern            | Meaning                                | Example                          | Matches                            |
-| ------------------ | -------------------------------------- | -------------------------------- | ---------------------------------- |
-| `//path`           | **Absolute** path from filesystem root | `Read(//Users/alice/secrets/**)` | `/Users/alice/secrets/**`          |
-| `~/path`           | Path from **home** directory           | `Read(~/Documents/*.pdf)`        | `/Users/alice/Documents/*.pdf`     |
-| `/path`            | Path **relative to settings file**     | `Edit(/src/**/*.ts)`             | `<settings file path>/src/**/*.ts` |
-| `path` or `./path` | Path **relative to current directory** | `Read(*.env)`                    | `<cwd>/*.env`                      |
+| Pattern            | Meaning                                | Example                          | Matches                        |
+| ------------------ | -------------------------------------- | -------------------------------- | ------------------------------ |
+| `//path`           | **Absolute** path from filesystem root | `Read(//Users/alice/secrets/**)` | `/Users/alice/secrets/**`      |
+| `~/path`           | Path from **home** directory           | `Read(~/Documents/*.pdf)`        | `/Users/alice/Documents/*.pdf` |
+| `/path`            | Path **relative to project root**      | `Edit(/src/**/*.ts)`             | `<project root>/src/**/*.ts`   |
+| `path` or `./path` | Path **relative to current directory** | `Read(*.env)`                    | `<cwd>/*.env`                  |
 
 <Warning>
-  A pattern like `/Users/alice/file` is NOT an absolute path. It's relative to your settings file. Use `//Users/alice/file` for absolute paths.
+  A pattern like `/Users/alice/file` is NOT an absolute path. It's relative to the project root. Use `//Users/alice/file` for absolute paths.
 </Warning>
 
 Examples:
 
-* `Edit(/docs/**)`: edits in `<project>/docs/` (NOT `/docs/`)
+* `Edit(/docs/**)`: edits in `<project>/docs/` (NOT `/docs/` and NOT `<project>/.claude/docs/`)
 * `Read(~/.zshrc)`: reads your home directory's `.zshrc`
 * `Edit(//tmp/scratch.txt)`: edits the absolute path `/tmp/scratch.txt`
 * `Read(src/**)`: reads from `<current-directory>/src/`
@@ -215,28 +215,22 @@
 
 ## Managed settings
 
-For organizations that need centralized control over Claude Code configuration, administrators can deploy `managed-settings.json` files to system directories. These policy files follow the same format as regular settings files and cannot be overridden by user or project settings. For organizations without device management infrastructure, [server-managed settings](/en/server-managed-settings) provide an alternative that delivers configurations from Anthropic's servers.
-
-**Managed settings file locations**:
-
-* **macOS**: `/Library/Application Support/ClaudeCode/managed-settings.json`
-* **Linux and WSL**: `/etc/claude-code/managed-settings.json`
-* **Windows**: `C:\Program Files\ClaudeCode\managed-settings.json`
-
-<Note>
-  These are system-wide paths (not user home directories like `~/Library/...`) that require administrator privileges. They are designed to be deployed by IT administrators.
-</Note>
+For organizations that need centralized control over Claude Code configuration, administrators can deploy managed settings that cannot be overridden by user or project settings. These policy settings follow the same format as regular settings files and can be delivered through MDM/OS-level policies, managed settings files, or [server-managed settings](/en/server-managed-settings). See [settings files](/en/settings#settings-files) for delivery mechanisms and file locations.
 
 ### Managed-only settings
 
 Some settings are only effective in managed settings:
 
-| Setting                           | Description                                                                                                                                        |
-| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
-| `disableBypassPermissionsMode`    | Set to `"disable"` to prevent `bypassPermissions` mode and the `--dangerously-skip-permissions` flag                                               |
-| `allowManagedPermissionRulesOnly` | When `true`, prevents user and project settings from defining `allow`, `ask`, or `deny` permission rules. Only rules in managed settings apply     |
-| `allowManagedHooksOnly`           | When `true`, prevents loading of user, project, and plugin hooks. Only managed hooks and SDK hooks are allowed                                     |
-| `strictKnownMarketplaces`         | Controls which plugin marketplaces users can add. See [managed marketplace restrictions](/en/plugin-marketplaces#managed-marketplace-restrictions) |
+| Setting                                   | Description                                                                                                                                                                                                            |
+| :---------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
+| `disableBypassPermissionsMode`            | Set to `"disable"` to prevent `bypassPermissions` mode and the `--dangerously-skip-permissions` flag                                                                                                                   |
+| `allowManagedPermissionRulesOnly`         | When `true`, prevents user and project settings from defining `allow`, `ask`, or `deny` permission rules. Only rules in managed settings apply                                                                         |
+| `allowManagedHooksOnly`                   | When `true`, prevents loading of user, project, and plugin hooks. Only managed hooks and SDK hooks are allowed                                                                                                         |
+| `allowManagedMcpServersOnly`              | When `true`, only `allowedMcpServers` from managed settings are respected. `deniedMcpServers` still merges from all sources. See [Managed MCP configuration](/en/mcp#managed-mcp-configuration)                        |
+| `blockedMarketplaces`                     | Blocklist of marketplace sources. Blocked sources are checked before downloading, so they never touch the filesystem. See [managed marketplace restrictions](/en/plugin-marketplaces#managed-marketplace-restrictions) |
+| `sandbox.network.allowManagedDomainsOnly` | When `true`, only `allowedDomains` and `WebFetch(domain:...)` allow rules from managed settings are respected. Denied domains still merge from all sources                                                             |
+| `strictKnownMarketplaces`                 | Controls which plugin marketplaces users can add. See [managed marketplace restrictions](/en/plugin-marketplaces#managed-marketplace-restrictions)                                                                     |
+| `allow_remote_sessions`                   | When `true`, allows users to start [Remote Control](/en/remote-control) and [web sessions](/en/claude-code-on-the-web). Defaults to `true`. Set to `false` to prevent remote session access                            |
 
 ## Settings precedence
 

```
### https://code.claude.com/docs/en/sub-agents.md

```diff
--- a/https://code.claude.com/docs/en/sub-agents.md
+++ b/https://code.claude.com/docs/en/sub-agents.md
@@ -84,7 +84,7 @@
   <Step title="Open the subagents interface">
     In Claude Code, run:
 
-    ```
+    ```text  theme={null}
     /agents
     ```
   </Step>
@@ -96,7 +96,7 @@
   <Step title="Generate with Claude">
     Select **Generate with Claude**. When prompted, describe the subagent:
 
-    ```
+    ```text  theme={null}
     A code improvement agent that scans files and suggests improvements
     for readability, performance, and best practices. It should explain
     each issue, show the current code, and provide an improved version.
@@ -120,7 +120,7 @@
   <Step title="Save and try it out">
     Save the subagent. It's available immediately (no restart needed). Try it:
 
-    ```
+    ```text  theme={null}
     Use the code-improver agent to suggest improvements in this project
     ```
 
@@ -145,6 +145,8 @@
 * See which subagents are active when duplicates exist
 
 This is the recommended way to create and manage subagents. For manual creation or automation, you can also add subagent files directly.
+
+To list all configured subagents from the command line without starting an interactive session, run `claude agents`. This shows agents grouped by source and indicates which are overridden by higher-priority definitions.
 
 ### Choose the subagent scope
 
@@ -496,7 +498,7 @@
 
 You can also request a specific subagent explicitly:
 
-```
+```text  theme={null}
 Use the test-runner subagent to fix failing tests
 Have the code-reviewer subagent look at my recent changes
 ```
@@ -506,7 +508,7 @@
 Subagents can run in the foreground (blocking) or background (concurrent):
 
 * **Foreground subagents** block the main conversation until complete. Permission prompts and clarifying questions (like [`AskUserQuestion`](/en/settings#tools-available-to-claude)) are passed through to you.
-* **Background subagents** run concurrently while you continue working. Before launching, Claude Code prompts for any tool permissions the subagent will need, ensuring it has the necessary approvals upfront. Once running, the subagent inherits these permissions and auto-denies anything not pre-approved. If a background subagent needs to ask clarifying questions, that tool call fails but the subagent continues. MCP tools are not available in background subagents.
+* **Background subagents** run concurrently while you continue working. Before launching, Claude Code prompts for any tool permissions the subagent will need, ensuring it has the necessary approvals upfront. Once running, the subagent inherits these permissions and auto-denies anything not pre-approved. If a background subagent needs to ask clarifying questions, that tool call fails but the subagent continues.
 
 If a background subagent fails due to missing permissions, you can [resume it](#resume-subagents) in the foreground to retry with interactive prompts.
 
@@ -523,7 +525,7 @@
 
 One of the most effective uses for subagents is isolating operations that produce large amounts of output. Running tests, fetching documentation, or processing log files can consume significant context. By delegating these to a subagent, the verbose output stays in the subagent's context while only the relevant summary returns to your main conversation.
 
-```
+```text  theme={null}
 Use a subagent to run the test suite and report only the failing tests with their error messages
 ```
 
@@ -531,7 +533,7 @@
 
 For independent investigations, spawn multiple subagents to work simultaneously:
 
-```
+```text  theme={null}
 Research the authentication, database, and API modules in parallel using separate subagents
 ```
 
@@ -547,7 +549,7 @@
 
 For multi-step workflows, ask Claude to use subagents in sequence. Each subagent completes its task and returns results to Claude, which then passes relevant context to the next subagent.
 
-```
+```text  theme={null}
 Use the code-reviewer subagent to find performance issues, then use the optimizer subagent to fix them
 ```
 
@@ -582,7 +584,7 @@
 
 When a subagent completes, Claude receives its agent ID. To resume a subagent, ask Claude to continue the previous work:
 
-```
+```text  theme={null}
 Use the code-reviewer subagent to review the authentication module
 [Agent completes]
 

```
### https://code.claude.com/docs/en/server-managed-settings.md

```diff
--- a/https://code.claude.com/docs/en/server-managed-settings.md
+++ b/https://code.claude.com/docs/en/server-managed-settings.md
@@ -24,12 +24,12 @@
 
 ## Choose between server-managed and endpoint-managed settings
 
-Claude Code supports two approaches for centralized configuration. Server-managed settings deliver configuration from Anthropic's servers. [Endpoint-managed settings](/en/permissions#managed-settings) deploy a `managed-settings.json` file to system directories via MDM (mobile device management).
+Claude Code supports two approaches for centralized configuration. Server-managed settings deliver configuration from Anthropic's servers. [Endpoint-managed settings](/en/settings#settings-files) are deployed directly to devices through native OS policies (macOS managed preferences, Windows registry) or managed settings files.
 
-| Approach                                                          | Best for                                                 | Security model                                                     |
-| :---------------------------------------------------------------- | :------------------------------------------------------- | :----------------------------------------------------------------- |
-| **Server-managed settings**                                       | Organizations without MDM, or users on unmanaged devices | Settings delivered from Anthropic's servers at authentication time |
-| **[Endpoint-managed settings](/en/permissions#managed-settings)** | Organizations with MDM or endpoint management            | Settings deployed to protected system directories by IT            |
+| Approach                                                     | Best for                                                 | Security model                                                                                            |
+| :----------------------------------------------------------- | :------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- |
+| **Server-managed settings**                                  | Organizations without MDM, or users on unmanaged devices | Settings delivered from Anthropic's servers at authentication time                                        |
+| **[Endpoint-managed settings](/en/settings#settings-files)** | Organizations with MDM or endpoint management            | Settings deployed to devices via MDM configuration profiles, registry policies, or managed settings files |
 
 If your devices are enrolled in an MDM or endpoint management solution, endpoint-managed settings provide stronger security guarantees because the settings file can be protected from user modification at the OS level.
 
@@ -89,7 +89,7 @@
 
 ### Settings precedence
 
-Server-managed settings and [endpoint-managed settings](/en/permissions#managed-settings) both occupy the highest tier in the Claude Code [settings hierarchy](/en/settings#settings-precedence), and user or project settings cannot override them. When both are present, server-managed settings take precedence and the local `managed-settings.json` file is not used.
+Server-managed settings and [endpoint-managed settings](/en/settings#settings-files) both occupy the highest tier in the Claude Code [settings hierarchy](/en/settings#settings-precedence), and user or project settings cannot override them. When both are present, server-managed settings take precedence and endpoint-managed settings are not used.
 
 ### Fetch and caching behavior
 
@@ -152,13 +152,13 @@
 
 To detect runtime configuration changes, use [`ConfigChange` hooks](/en/hooks#configchange) to log modifications or block unauthorized changes before they take effect.
 
-For stronger enforcement guarantees, use [endpoint-managed settings](/en/permissions#managed-settings) on devices enrolled in an MDM solution.
+For stronger enforcement guarantees, use [endpoint-managed settings](/en/settings#settings-files) on devices enrolled in an MDM solution.
 
 ## See also
 
 Related pages for managing Claude Code configuration:
 
 * [Settings](/en/settings): complete configuration reference including all available settings
-* [Endpoint-managed settings](/en/permissions#managed-settings): file-based managed settings deployed by IT
+* [Endpoint-managed settings](/en/settings#settings-files): managed settings deployed to devices by IT
 * [Authentication](/en/authentication): set up user access to Claude Code
 * [Security](/en/security): security safeguards and best practices

```
### https://code.claude.com/docs/en/settings.md

```diff
--- a/https://code.claude.com/docs/en/settings.md
+++ b/https://code.claude.com/docs/en/settings.md
@@ -14,12 +14,12 @@
 
 ### Available scopes
 
-| Scope       | Location                             | Who it affects                       | Shared with team?      |
-| :---------- | :----------------------------------- | :----------------------------------- | :--------------------- |
-| **Managed** | System-level `managed-settings.json` | All users on the machine             | Yes (deployed by IT)   |
-| **User**    | `~/.claude/` directory               | You, across all projects             | No                     |
-| **Project** | `.claude/` in repository             | All collaborators on this repository | Yes (committed to git) |
-| **Local**   | `.claude/*.local.*` files            | You, in this repository only         | No (gitignored)        |
+| Scope       | Location                                                                           | Who it affects                       | Shared with team?      |
+| :---------- | :--------------------------------------------------------------------------------- | :----------------------------------- | :--------------------- |
+| **Managed** | Server-managed settings, plist / registry, or system-level `managed-settings.json` | All users on the machine             | Yes (deployed by IT)   |
+| **User**    | `~/.claude/` directory                                                             | You, across all projects             | No                     |
+| **Project** | `.claude/` in repository                                                           | All collaborators on this repository | Yes (committed to git) |
+| **Local**   | `.claude/*.local.*` files                                                          | You, in this repository only         | No (gitignored)        |
 
 ### When to use each scope
 
@@ -83,17 +83,19 @@
 * **Project settings** are saved in your project directory:
   * `.claude/settings.json` for settings that are checked into source control and shared with your team
   * `.claude/settings.local.json` for settings that are not checked in, useful for personal preferences and experimentation. Claude Code will configure git to ignore `.claude/settings.local.json` when it is created.
-* **Managed settings**: For organizations that need centralized control, Claude Code supports `managed-settings.json` and `managed-mcp.json` files that can be deployed to system directories:
-
-  * macOS: `/Library/Application Support/ClaudeCode/`
-  * Linux and WSL: `/etc/claude-code/`
-  * Windows: `C:\Program Files\ClaudeCode\`
-
-  <Note>
-    These are system-wide paths (not user home directories like `~/Library/...`) that require administrator privileges. They are designed to be deployed by IT administrators.
-  </Note>
-
-  See [Managed settings](/en/permissions#managed-settings) and [Managed MCP configuration](/en/mcp#managed-mcp-configuration) for details. For organizations without device management infrastructure, see [server-managed settings](/en/server-managed-settings).
+* **Managed settings**: For organizations that need centralized control, Claude Code supports multiple delivery mechanisms for managed settings. All use the same JSON format and cannot be overridden by user or project settings:
+
+  * **Server-managed settings**: delivered from Anthropic's servers via the Claude.ai admin console. See [server-managed settings](/en/server-managed-settings).
+  * **MDM/OS-level policies**: delivered through native device management on macOS and Windows:
+    * macOS: `com.anthropic.claudecode` managed preferences domain (deployed via configuration profiles in Jamf, Kandji, or other MDM tools)
+    * Windows: `HKLM\SOFTWARE\Policies\ClaudeCode` registry key with a `Settings` value (REG\_SZ or REG\_EXPAND\_SZ) containing JSON (deployed via Group Policy or Intune)
+    * Windows (user-level): `HKCU\SOFTWARE\Policies\ClaudeCode` (lowest policy priority, only used when no admin-level source exists)
+  * **File-based**: `managed-settings.json` and `managed-mcp.json` deployed to system directories:
+    * macOS: `/Library/Application Support/ClaudeCode/`
+    * Linux and WSL: `/etc/claude-code/`
+    * Windows: `C:\Program Files\ClaudeCode\`
+
+  See [managed settings](/en/permissions#managed-only-settings) and [Managed MCP configuration](/en/mcp#managed-mcp-configuration) for details.
 
   <Note>
     Managed deployments can also restrict **plugin marketplace additions** using
@@ -139,47 +141,49 @@
 
 `settings.json` supports a number of options:
 
-| Key                               | Description                                                                                                                                                                                                                                                                     | Example                                                                 |
-| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------- |
-| `apiKeyHelper`                    | Custom script, to be executed in `/bin/sh`, to generate an auth value. This value will be sent as `X-Api-Key` and `Authorization: Bearer` headers for model requests                                                                                                            | `/bin/generate_temp_api_key.sh`                                         |
-| `cleanupPeriodDays`               | Sessions inactive for longer than this period are deleted at startup. Setting to `0` immediately deletes all sessions. (default: 30 days)                                                                                                                                       | `20`                                                                    |
-| `companyAnnouncements`            | Announcement to display to users at startup. If multiple announcements are provided, they will be cycled through at random.                                                                                                                                                     | `["Welcome to Acme Corp! Review our code guidelines at docs.acme.com"]` |
-| `env`                             | Environment variables that will be applied to every session                                                                                                                                                                                                                     | `{"FOO": "bar"}`                                                        |
-| `attribution`                     | Customize attribution for git commits and pull requests. See [Attribution settings](#attribution-settings)                                                                                                                                                                      | `{"commit": "🤖 Generated with Claude Code", "pr": ""}`                 |
-| `includeCoAuthoredBy`             | **Deprecated**: Use `attribution` instead. Whether to include the `co-authored-by Claude` byline in git commits and pull requests (default: `true`)                                                                                                                             | `false`                                                                 |
-| `permissions`                     | See table below for structure of permissions.                                                                                                                                                                                                                                   |                                                                         |
-| `hooks`                           | Configure custom commands to run at lifecycle events. See [hooks documentation](/en/hooks) for format                                                                                                                                                                           | See [hooks](/en/hooks)                                                  |
-| `disableAllHooks`                 | Disable all [hooks](/en/hooks) and any custom [status line](/en/statusline)                                                                                                                                                                                                     | `true`                                                                  |
-| `allowManagedHooksOnly`           | (Managed settings only) Prevent loading of user, project, and plugin hooks. Only allows managed hooks and SDK hooks. See [Hook configuration](#hook-configuration)                                                                                                              | `true`                                                                  |
-| `allowManagedPermissionRulesOnly` | (Managed settings only) Prevent user and project settings from defining `allow`, `ask`, or `deny` permission rules. Only rules in managed settings apply. See [Managed-only settings](/en/permissions#managed-only-settings)                                                    | `true`                                                                  |
-| `model`                           | Override the default model to use for Claude Code                                                                                                                                                                                                                               | `"claude-sonnet-4-6"`                                                   |
-| `availableModels`                 | Restrict which models users can select via `/model`, `--model`, Config tool, or `ANTHROPIC_MODEL`. Does not affect the Default option. See [Restrict model selection](/en/model-config#restrict-model-selection)                                                                | `["sonnet", "haiku"]`                                                   |
-| `otelHeadersHelper`               | Script to generate dynamic OpenTelemetry headers. Runs at startup and periodically (see [Dynamic headers](/en/monitoring-usage#dynamic-headers))                                                                                                                                | `/bin/generate_otel_headers.sh`                                         |
-| `statusLine`                      | Configure a custom status line to display context. See [`statusLine` documentation](/en/statusline)                                                                                                                                                                             | `{"type": "command", "command": "~/.claude/statusline.sh"}`             |
-| `fileSuggestion`                  | Configure a custom script for `@` file autocomplete. See [File suggestion settings](#file-suggestion-settings)                                                                                                                                                                  | `{"type": "command", "command": "~/.claude/file-suggestion.sh"}`        |
-| `respectGitignore`                | Control whether the `@` file picker respects `.gitignore` patterns. When `true` (default), files matching `.gitignore` patterns are excluded from suggestions                                                                                                                   | `false`                                                                 |
-| `outputStyle`                     | Configure an output style to adjust the system prompt. See [output styles documentation](/en/output-styles)                                                                                                                                                                     | `"Explanatory"`                                                         |
-| `forceLoginMethod`                | Use `claudeai` to restrict login to Claude.ai accounts, `console` to restrict login to Claude Console (API usage billing) accounts                                                                                                                                              | `claudeai`                                                              |
-| `forceLoginOrgUUID`               | Specify the UUID of an organization to automatically select it during login, bypassing the organization selection step. Requires `forceLoginMethod` to be set                                                                                                                   | `"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"`                                |
-| `enableAllProjectMcpServers`      | Automatically approve all MCP servers defined in project `.mcp.json` files                                                                                                                                                                                                      | `true`                                                                  |
-| `enabledMcpjsonServers`           | List of specific MCP servers from `.mcp.json` files to approve                                                                                                                                                                                                                  | `["memory", "github"]`                                                  |
-| `disabledMcpjsonServers`          | List of specific MCP servers from `.mcp.json` files to reject                                                                                                                                                                                                                   | `["filesystem"]`                                                        |
-| `allowedMcpServers`               | When set in managed-settings.json, allowlist of MCP servers users can configure. Undefined = no restrictions, empty array = lockdown. Applies to all scopes. Denylist takes precedence. See [Managed MCP configuration](/en/mcp#managed-mcp-configuration)                      | `[{ "serverName": "github" }]`                                          |
-| `deniedMcpServers`                | When set in managed-settings.json, denylist of MCP servers that are explicitly blocked. Applies to all scopes including managed servers. Denylist takes precedence over allowlist. See [Managed MCP configuration](/en/mcp#managed-mcp-configuration)                           | `[{ "serverName": "filesystem" }]`                                      |
-| `strictKnownMarketplaces`         | When set in managed-settings.json, allowlist of plugin marketplaces users can add. Undefined = no restrictions, empty array = lockdown. Applies to marketplace additions only. See [Managed marketplace restrictions](/en/plugin-marketplaces#managed-marketplace-restrictions) | `[{ "source": "github", "repo": "acme-corp/plugins" }]`                 |
-| `awsAuthRefresh`                  | Custom script that modifies the `.aws` directory (see [advanced credential configuration](/en/amazon-bedrock#advanced-credential-configuration))                                                                                                                                | `aws sso login --profile myprofile`                                     |
-| `awsCredentialExport`             | Custom script that outputs JSON with AWS credentials (see [advanced credential configuration](/en/amazon-bedrock#advanced-credential-configuration))                                                                                                                            | `/bin/generate_aws_grant.sh`                                            |
-| `alwaysThinkingEnabled`           | Enable [extended thinking](/en/common-workflows#use-extended-thinking-thinking-mode) by default for all sessions. Typically configured via the `/config` command rather than editing directly                                                                                   | `true`                                                                  |
-| `plansDirectory`                  | Customize where plan files are stored. Path is relative to project root. Default: `~/.claude/plans`                                                                                                                                                                             | `"./plans"`                                                             |
-| `showTurnDuration`                | Show turn duration messages after responses (e.g., "Cooked for 1m 6s"). Set to `false` to hide these messages                                                                                                                                                                   | `true`                                                                  |
-| `spinnerVerbs`                    | Customize the action verbs shown in the spinner and turn duration messages. Set `mode` to `"replace"` to use only your verbs, or `"append"` to add them to the defaults                                                                                                         | `{"mode": "append", "verbs": ["Pondering", "Crafting"]}`                |
-| `language`                        | Configure Claude's preferred response language (e.g., `"japanese"`, `"spanish"`, `"french"`). Claude will respond in this language by default                                                                                                                                   | `"japanese"`                                                            |
-| `autoUpdatesChannel`              | Release channel to follow for updates. Use `"stable"` for a version that is typically about one week old and skips versions with major regressions, or `"latest"` (default) for the most recent release                                                                         | `"stable"`                                                              |
-| `spinnerTipsEnabled`              | Show tips in the spinner while Claude is working. Set to `false` to disable tips (default: `true`)                                                                                                                                                                              | `false`                                                                 |
-| `spinnerTipsOverride`             | Override spinner tips with custom strings. `tips`: array of tip strings. `excludeDefault`: if `true`, only show custom tips; if `false` or absent, custom tips are merged with built-in tips                                                                                    | `{ "excludeDefault": true, "tips": ["Use our internal tool X"] }`       |
-| `terminalProgressBarEnabled`      | Enable the terminal progress bar that shows progress in supported terminals like Windows Terminal and iTerm2 (default: `true`)                                                                                                                                                  | `false`                                                                 |
-| `prefersReducedMotion`            | Reduce or disable UI animations (spinners, shimmer, flash effects) for accessibility                                                                                                                                                                                            | `true`                                                                  |
-| `teammateMode`                    | How [agent team](/en/agent-teams) teammates display: `auto` (picks split panes in tmux or iTerm2, in-process otherwise), `in-process`, or `tmux`. See [set up agent teams](/en/agent-teams#set-up-agent-teams)                                                                  | `"in-process"`                                                          |
+| Key                               | Description                                                                                                                                                                                                                                                                               | Example                                                                 |
+| :-------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------- |
+| `apiKeyHelper`                    | Custom script, to be executed in `/bin/sh`, to generate an auth value. This value will be sent as `X-Api-Key` and `Authorization: Bearer` headers for model requests                                                                                                                      | `/bin/generate_temp_api_key.sh`                                         |
+| `cleanupPeriodDays`               | Sessions inactive for longer than this period are deleted at startup. Setting to `0` immediately deletes all sessions. (default: 30 days)                                                                                                                                                 | `20`                                                                    |
+| `companyAnnouncements`            | Announcement to display to users at startup. If multiple announcements are provided, they will be cycled through at random.                                                                                                                                                               | `["Welcome to Acme Corp! Review our code guidelines at docs.acme.com"]` |
+| `env`                             | Environment variables that will be applied to every session                                                                                                                                                                                                                               | `{"FOO": "bar"}`                                                        |
+| `attribution`                     | Customize attribution for git commits and pull requests. See [Attribution settings](#attribution-settings)                                                                                                                                                                                | `{"commit": "🤖 Generated with Claude Code", "pr": ""}`                 |
+| `includeCoAuthoredBy`             | **Deprecated**: Use `attribution` instead. Whether to include the `co-authored-by Claude` byline in git commits and pull requests (default: `true`)                                                                                                                                       | `false`                                                                 |
+| `permissions`                     | See table below for structure of permissions.                                                                                                                                                                                                                                             |                                                                         |
+| `hooks`                           | Configure custom commands to run at lifecycle events. See [hooks documentation](/en/hooks) for format                                                                                                                                                                                     | See [hooks](/en/hooks)                                                  |
+| `disableAllHooks`                 | Disable all [hooks](/en/hooks) and any custom [status line](/en/statusline)                                                                                                                                                                                                               | `true`                                                                  |
+| `allowManagedHooksOnly`           | (Managed settings only) Prevent loading of user, project, and plugin hooks. Only allows managed hooks and SDK hooks. See [Hook configuration](#hook-configuration)                                                                                                                        | `true`                                                                  |
+| `allowManagedPermissionRulesOnly` | (Managed settings only) Prevent user and project settings from defining `allow`, `ask`, or `deny` permission rules. Only rules in managed settings apply. See [Managed-only settings](/en/permissions#managed-only-settings)                                                              | `true`                                                                  |
+| `allowManagedMcpServersOnly`      | (Managed settings only) Only `allowedMcpServers` from managed settings are respected. `deniedMcpServers` still merges from all sources. Users can still add MCP servers, but only the admin-defined allowlist applies. See [Managed MCP configuration](/en/mcp#managed-mcp-configuration) | `true`                                                                  |
+| `model`                           | Override the default model to use for Claude Code                                                                                                                                                                                                                                         | `"claude-sonnet-4-6"`                                                   |
+| `availableModels`                 | Restrict which models users can select via `/model`, `--model`, Config tool, or `ANTHROPIC_MODEL`. Does not affect the Default option. See [Restrict model selection](/en/model-config#restrict-model-selection)                                                                          | `["sonnet", "haiku"]`                                                   |
+| `otelHeadersHelper`               | Script to generate dynamic OpenTelemetry headers. Runs at startup and periodically (see [Dynamic headers](/en/monitoring-usage#dynamic-headers))                                                                                                                                          | `/bin/generate_otel_headers.sh`                                         |
+| `statusLine`                      | Configure a custom status line to display context. See [`statusLine` documentation](/en/statusline)                                                                                                                                                                                       | `{"type": "command", "command": "~/.claude/statusline.sh"}`             |
+| `fileSuggestion`                  | Configure a custom script for `@` file autocomplete. See [File suggestion settings](#file-suggestion-settings)                                                                                                                                                                            | `{"type": "command", "command": "~/.claude/file-suggestion.sh"}`        |
+| `respectGitignore`                | Control whether the `@` file picker respects `.gitignore` patterns. When `true` (default), files matching `.gitignore` patterns are excluded from suggestions                                                                                                                             | `false`                                                                 |
+| `outputStyle`                     | Configure an output style to adjust the system prompt. See [output styles documentation](/en/output-styles)                                                                                                                                                                               | `"Explanatory"`                                                         |
+| `forceLoginMethod`                | Use `claudeai` to restrict login to Claude.ai accounts, `console` to restrict login to Claude Console (API usage billing) accounts                                                                                                                                                        | `claudeai`                                                              |
+| `forceLoginOrgUUID`               | Specify the UUID of an organization to automatically select it during login, bypassing the organization selection step. Requires `forceLoginMethod` to be set                                                                                                                             | `"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"`                                |
+| `enableAllProjectMcpServers`      | Automatically approve all MCP servers defined in project `.mcp.json` files                                                                                                                                                                                                                | `true`                                                                  |
+| `enabledMcpjsonServers`           | List of specific MCP servers from `.mcp.json` files to approve                                                                                                                                                                                                                            | `["memory", "github"]`                                                  |
+| `disabledMcpjsonServers`          | List of specific MCP servers from `.mcp.json` files to reject                                                                                                                                                                                                                             | `["filesystem"]`                                                        |
+| `allowedMcpServers`               | When set in managed-settings.json, allowlist of MCP servers users can configure. Undefined = no restrictions, empty array = lockdown. Applies to all scopes. Denylist takes precedence. See [Managed MCP configuration](/en/mcp#managed-mcp-configuration)                                | `[{ "serverName": "github" }]`                                          |
+| `deniedMcpServers`                | When set in managed-settings.json, denylist of MCP servers that are explicitly blocked. Applies to all scopes including managed servers. Denylist takes precedence over allowlist. See [Managed MCP configuration](/en/mcp#managed-mcp-configuration)                                     | `[{ "serverName": "filesystem" }]`                                      |
+| `strictKnownMarketplaces`         | When set in managed-settings.json, allowlist of plugin marketplaces users can add. Undefined = no restrictions, empty array = lockdown. Applies to marketplace additions only. See [Managed marketplace restrictions](/en/plugin-marketplaces#managed-marketplace-restrictions)           | `[{ "source": "github", "repo": "acme-corp/plugins" }]`                 |
+| `blockedMarketplaces`             | (Managed settings only) Blocklist of marketplace sources. Blocked sources are checked before downloading, so they never touch the filesystem. See [Managed marketplace restrictions](/en/plugin-marketplaces#managed-marketplace-restrictions)                                            | `[{ "source": "github", "repo": "untrusted/plugins" }]`                 |
+| `awsAuthRefresh`                  | Custom script that modifies the `.aws` directory (see [advanced credential configuration](/en/amazon-bedrock#advanced-credential-configuration))                                                                                                                                          | `aws sso login --profile myprofile`                                     |
+| `awsCredentialExport`             | Custom script that outputs JSON with AWS credentials (see [advanced credential configuration](/en/amazon-bedrock#advanced-credential-configuration))                                                                                                                                      | `/bin/generate_aws_grant.sh`                                            |
+| `alwaysThinkingEnabled`           | Enable [extended thinking](/en/common-workflows#use-extended-thinking-thinking-mode) by default for all sessions. Typically configured via the `/config` command rather than editing directly                                                                                             | `true`                                                                  |
+| `plansDirectory`                  | Customize where plan files are stored. Path is relative to project root. Default: `~/.claude/plans`                                                                                                                                                                                       | `"./plans"`                                                             |
+| `showTurnDuration`                | Show turn duration messages after responses (e.g., "Cooked for 1m 6s"). Set to `false` to hide these messages                                                                                                                                                                             | `true`                                                                  |
+| `spinnerVerbs`                    | Customize the action verbs shown in the spinner and turn duration messages. Set `mode` to `"replace"` to use only your verbs, or `"append"` to add them to the defaults                                                                                                                   | `{"mode": "append", "verbs": ["Pondering", "Crafting"]}`                |
+| `language`                        | Configure Claude's preferred response language (e.g., `"japanese"`, `"spanish"`, `"french"`). Claude will respond in this language by default                                                                                                                                             | `"japanese"`                                                            |
+| `autoUpdatesChannel`              | Release channel to follow for updates. Use `"stable"` for a version that is typically about one week old and skips versions with major regressions, or `"latest"` (default) for the most recent release                                                                                   | `"stable"`                                                              |
+| `spinnerTipsEnabled`              | Show tips in the spinner while Claude is working. Set to `false` to disable tips (default: `true`)                                                                                                                                                                                        | `false`                                                                 |
+| `spinnerTipsOverride`             | Override spinner tips with custom strings. `tips`: array of tip strings. `excludeDefault`: if `true`, only show custom tips; if `false` or absent, custom tips are merged with built-in tips                                                                                              | `{ "excludeDefault": true, "tips": ["Use our internal tool X"] }`       |
+| `terminalProgressBarEnabled`      | Enable the terminal progress bar that shows progress in supported terminals like Windows Terminal and iTerm2 (default: `true`)                                                                                                                                                            | `false`                                                                 |
+| `prefersReducedMotion`            | Reduce or disable UI animations (spinners, shimmer, flash effects) for accessibility                                                                                                                                                                                                      | `true`                                                                  |
+| `teammateMode`                    | How [agent team](/en/agent-teams) teammates display: `auto` (picks split panes in tmux or iTerm2, in-process otherwise), `in-process`, or `tmux`. See [set up agent teams](/en/agent-teams#set-up-agent-teams)                                                                            | `"in-process"`                                                          |
 
 ### Permission settings
 
@@ -190,7 +194,7 @@
 | `deny`                         | Array of permission rules to deny tool use. Use this to exclude sensitive files from Claude Code access. See [Permission rule syntax](#permission-rule-syntax) and [Bash permission limitations](/en/permissions#tool-specific-permission-rules) | `[ "WebFetch", "Bash(curl *)", "Read(./.env)", "Read(./secrets/**)" ]` |
 | `additionalDirectories`        | Additional [working directories](/en/permissions#working-directories) that Claude has access to                                                                                                                                                  | `[ "../docs/" ]`                                                       |
 | `defaultMode`                  | Default [permission mode](/en/permissions#permission-modes) when opening Claude Code                                                                                                                                                             | `"acceptEdits"`                                                        |
-| `disableBypassPermissionsMode` | Set to `"disable"` to prevent `bypassPermissions` mode from being activated. This disables the `--dangerously-skip-permissions` command-line flag. See [managed settings](/en/permissions#managed-settings)                                      | `"disable"`                                                            |
+| `disableBypassPermissionsMode` | Set to `"disable"` to prevent `bypassPermissions` mode from being activated. This disables the `--dangerously-skip-permissions` command-line flag. See [managed settings](/en/permissions#managed-only-settings)                                 | `"disable"`                                                            |
 
 ### Permission rule syntax
 
@@ -213,19 +217,20 @@
 
 **Filesystem and network restrictions** are configured via Read, Edit, and WebFetch permission rules, not via these sandbox settings.
 
-| Keys                          | Description                                                                                                                                                                                                                                                                                                                       | Example                         |
-| :---------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------ |
-| `enabled`                     | Enable bash sandboxing (macOS, Linux, and WSL2). Default: false                                                                                                                                                                                                                                                                   | `true`                          |
-| `autoAllowBashIfSandboxed`    | Auto-approve bash commands when sandboxed. Default: true                                                                                                                                                                                                                                                                          | `true`                          |
-| `excludedCommands`            | Commands that should run outside of the sandbox                                                                                                                                                                                                                                                                                   | `["git", "docker"]`             |
-| `allowUnsandboxedCommands`    | Allow commands to run outside the sandbox via the `dangerouslyDisableSandbox` parameter. When set to `false`, the `dangerouslyDisableSandbox` escape hatch is completely disabled and all commands must run sandboxed (or be in `excludedCommands`). Useful for enterprise policies that require strict sandboxing. Default: true | `false`                         |
-| `network.allowUnixSockets`    | Unix socket paths accessible in sandbox (for SSH agents, etc.)                                                                                                                                                                                                                                                                    | `["~/.ssh/agent-socket"]`       |
-| `network.allowAllUnixSockets` | Allow all Unix socket connections in sandbox. Default: false                                                                                                                                                                                                                                                                      | `true`                          |
-| `network.allowLocalBinding`   | Allow binding to localhost ports (macOS only). Default: false                                                                                                                                                                                                                                                                     | `true`                          |
-| `network.allowedDomains`      | Array of domains to allow for outbound network traffic. Supports wildcards (e.g., `*.example.com`).                                                                                                                                                                                                                               | `["github.com", "*.npmjs.org"]` |
-| `network.httpProxyPort`       | HTTP proxy port used if you wish to bring your own proxy. If not specified, Claude will run its own proxy.                                                                                                                                                                                                                        | `8080`                          |
-| `network.socksProxyPort`      | SOCKS5 proxy port used if you wish to bring your own proxy. If not specified, Claude will run its own proxy.                                                                                                                                                                                                                      | `8081`                          |
-| `enableWeakerNestedSandbox`   | Enable weaker sandbox for unprivileged Docker environments (Linux and WSL2 only). **Reduces security.** Default: false                                                                                                                                                                                                            | `true`                          |
+| Keys                              | Description                                                                                                                                                                                                                                                                                                                       | Example                         |
+| :-------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------ |
+| `enabled`                         | Enable bash sandboxing (macOS, Linux, and WSL2). Default: false                                                                                                                                                                                                                                                                   | `true`                          |
+| `autoAllowBashIfSandboxed`        | Auto-approve bash commands when sandboxed. Default: true                                                                                                                                                                                                                                                                          | `true`                          |
+| `excludedCommands`                | Commands that should run outside of the sandbox                                                                                                                                                                                                                                                                                   | `["git", "docker"]`             |
+| `allowUnsandboxedCommands`        | Allow commands to run outside the sandbox via the `dangerouslyDisableSandbox` parameter. When set to `false`, the `dangerouslyDisableSandbox` escape hatch is completely disabled and all commands must run sandboxed (or be in `excludedCommands`). Useful for enterprise policies that require strict sandboxing. Default: true | `false`                         |
+| `network.allowUnixSockets`        | Unix socket paths accessible in sandbox (for SSH agents, etc.)                                                                                                                                                                                                                                                                    | `["~/.ssh/agent-socket"]`       |
+| `network.allowAllUnixSockets`     | Allow all Unix socket connections in sandbox. Default: false                                                                                                                                                                                                                                                                      | `true`                          |
+| `network.allowLocalBinding`       | Allow binding to localhost ports (macOS only). Default: false                                                                                                                                                                                                                                                                     | `true`                          |
+| `network.allowedDomains`          | Array of domains to allow for outbound network traffic. Supports wildcards (e.g., `*.example.com`).                                                                                                                                                                                                                               | `["github.com", "*.npmjs.org"]` |
+| `network.allowManagedDomainsOnly` | (Managed settings only) Only `allowedDomains` and `WebFetch(domain:...)` allow rules from managed settings are respected. Domains from user, project, and local settings are ignored. Denied domains are still respected from all sources. Default: false                                                                         | `true`                          |
+| `network.httpProxyPort`           | HTTP proxy port used if you wish to bring your own proxy. If not specified, Claude will run its own proxy.                                                                                                                                                                                                                        | `8080`                          |
+| `network.socksProxyPort`          | SOCKS5 proxy port used if you wish to bring your own proxy. If not specified, Claude will run its own proxy.                                                                                                                                                                                                                      | `8081`                          |
+| `enableWeakerNestedSandbox`       | Enable weaker sandbox for unprivileged Docker environments (Linux and WSL2 only). **Reduces security.** Default: false                                                                                                                                                                                                            | `true`                          |
 
 **Configuration example:**
 
@@ -273,7 +278,7 @@
 
 **Default commit attribution:**
 
-```
+```text  theme={null}
 🤖 Generated with [Claude Code](https://claude.com/claude-code)
 
    Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
@@ -281,7 +286,7 @@
 
 **Default pull request attribution:**
 
-```
+```text  theme={null}
 🤖 Generated with [Claude Code](https://claude.com/claude-code)
 ```
 
@@ -321,7 +326,7 @@
 
 Output newline-separated file paths to stdout (currently limited to 15):
 
-```
+```text  theme={null}
 src/components/Button.tsx
 src/components/Modal.tsx
 src/components/Form.tsx
@@ -356,9 +361,10 @@
 
 Settings apply in order of precedence. From highest to lowest:
 
-1. **Managed settings** ([`managed-settings.json`](/en/permissions#managed-settings) or [server-managed settings](/en/server-managed-settings))
-   * Policies deployed by IT/DevOps to system directories, or delivered from Anthropic's servers for Claude for Enterprise customers
+1. **Managed settings** ([server-managed](/en/server-managed-settings), [MDM/OS-level policies](#configuration-scopes), or [managed settings](/en/settings#settings-files))
+   * Policies deployed by IT through server delivery, MDM configuration profiles, registry policies, or managed settings files
    * Cannot be overridden by user or project settings
+   * Within the managed tier, precedence is: server-managed > MDM/OS-level policies > `managed-settings.json` > HKCU registry (Windows only). Only one managed source is used; sources do not merge.
 
 2. **Command line arguments**
    * Temporary overrides for a specific session
@@ -375,6 +381,10 @@
 This hierarchy ensures that organizational policies are always enforced while still allowing teams and individuals to customize their experience.
 
 For example, if your user settings allow `Bash(npm run *)` but a project's shared settings deny it, the project setting takes precedence and the command is blocked.
+
+### Verify active settings
+
+Run `/status` inside Claude Code to see which settings sources are active and where they come from. The output shows each configuration layer (managed, user, project) along with its origin, such as `Enterprise managed settings (remote)`, `Enterprise managed settings (plist)`, `Enterprise managed settings (HKLM)`, or `Enterprise managed settings (file)`. If a settings file contains errors, `/status` reports the issue so you can fix it.
 
 ### Key points about the configuration system
 
@@ -505,7 +515,7 @@
 
 #### `strictKnownMarketplaces`
 
-**Managed settings only**: Controls which plugin marketplaces users are allowed to add. This setting can only be configured in [`managed-settings.json`](/en/permissions#managed-settings) and provides administrators with strict control over marketplace sources.
+**Managed settings only**: Controls which plugin marketplaces users are allowed to add. This setting can only be configured in [managed settings](/en/settings#settings-files) and provides administrators with strict control over marketplace sources.
 
 **Managed settings file locations**:
 
@@ -762,40 +772,45 @@
 | `BASH_MAX_TIMEOUT_MS`                          | Maximum timeout the model can set for long-running bash commands                                                                                                                                                                                                                                                                                                                                                                                                                                      |     |
 | `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE`              | Set the percentage of context capacity (1-100) at which auto-compaction triggers. By default, auto-compaction triggers at approximately 95% capacity. Use lower values like `50` to compact earlier. Values above the default threshold have no effect. Applies to both main conversations and subagents. This percentage aligns with the `context_window.used_percentage` field available in [status line](/en/statusline)                                                                           |     |
 | `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR`     | Return to the original working directory after each Bash command                                                                                                                                                                                                                                                                                                                                                                                                                                      |     |
+| `CLAUDE_CODE_ACCOUNT_UUID`                     | Account UUID for the authenticated user. Used by SDK callers to provide account information synchronously, avoiding a race condition where early telemetry events lack account metadata. Requires `CLAUDE_CODE_USER_EMAIL` and `CLAUDE_CODE_ORGANIZATION_UUID` to also be set                                                                                                                                                                                                                         |     |
 | `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD` | Set to `1` to load CLAUDE.md files from directories specified with `--add-dir`. By default, additional directories do not load memory files                                                                                                                                                                                                                                                                                                                                                           | `1` |
-| `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`         | Set to `1` to enable [agent teams](/en/agent-teams). Agent teams are experimental and disabled by default                                                                                                                                                                                                                                                                                                                                                                                             |     |
 | `CLAUDE_CODE_API_KEY_HELPER_TTL_MS`            | Interval in milliseconds at which credentials should be refreshed (when using `apiKeyHelper`)                                                                                                                                                                                                                                                                                                                                                                                                         |     |
 | `CLAUDE_CODE_CLIENT_CERT`                      | Path to client certificate file for mTLS authentication                                                                                                                                                                                                                                                                                                                                                                                                                                               |     |
+| `CLAUDE_CODE_CLIENT_KEY`                       | Path to client private key file for mTLS authentication                                                                                                                                                                                                                                                                                                                                                                                                                                               |     |
 | `CLAUDE_CODE_CLIENT_KEY_PASSPHRASE`            | Passphrase for encrypted CLAUDE\_CODE\_CLIENT\_KEY (optional)                                                                                                                                                                                                                                                                                                                                                                                                                                         |     |
-| `CLAUDE_CODE_CLIENT_KEY`                       | Path to client private key file for mTLS authentication                                                                                                                                                                                                                                                                                                                                                                                                                                               |     |
-| `CLAUDE_CODE_EFFORT_LEVEL`                     | Set the effort level for supported models. Values: `low`, `medium`, `high` (default). Lower effort is faster and cheaper, higher effort provides deeper reasoning. Currently supported with Opus 4.6 only. See [Adjust effort level](/en/model-config#adjust-effort-level)                                                                                                                                                                                                                            |     |
-| `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS`       | Set to `1` to disable Anthropic API-specific `anthropic-beta` headers. Use this if experiencing issues like "Unexpected value(s) for the `anthropic-beta` header" when using an LLM gateway with third-party providers                                                                                                                                                                                                                                                                                |     |
+| `CLAUDE_CODE_DISABLE_1M_CONTEXT`               | Set to `1` to disable [1M context window](/en/model-config#extended-context) support. When set, 1M model variants are unavailable in the model picker. Useful for enterprise environments with compliance requirements                                                                                                                                                                                                                                                                                |     |
 | `CLAUDE_CODE_DISABLE_AUTO_MEMORY`              | Set to `1` to disable [auto memory](/en/memory#auto-memory). Set to `0` to force auto memory on during the gradual rollout. When disabled, Claude does not create or load auto memory files                                                                                                                                                                                                                                                                                                           |     |
 | `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS`         | Set to `1` to disable all background task functionality, including the `run_in_background` parameter on Bash and subagent tools, auto-backgrounding, and the Ctrl+B shortcut                                                                                                                                                                                                                                                                                                                          |     |
+| `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS`       | Set to `1` to disable Anthropic API-specific `anthropic-beta` headers. Use this if experiencing issues like "Unexpected value(s) for the `anthropic-beta` header" when using an LLM gateway with third-party providers                                                                                                                                                                                                                                                                                |     |
 | `CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY`          | Set to `1` to disable the "How is Claude doing?" session quality surveys. Also disabled when using third-party providers or when telemetry is disabled. See [Session quality surveys](/en/data-usage#session-quality-surveys)                                                                                                                                                                                                                                                                         |     |
-| `CLAUDE_CODE_EXIT_AFTER_STOP_DELAY`            | Time in milliseconds to wait after the query loop becomes idle before automatically exiting. Useful for automated workflows and scripts using SDK mode                                                                                                                                                                                                                                                                                                                                                |     |
-| `CLAUDE_CODE_PROXY_RESOLVES_HOSTS`             | Set to `true` to allow the proxy to perform DNS resolution instead of the caller. Opt-in for environments where the proxy should handle hostname resolution                                                                                                                                                                                                                                                                                                                                           |     |
-| `CLAUDE_CODE_TASK_LIST_ID`                     | Share a task list across sessions. Set the same ID in multiple Claude Code instances to coordinate on a shared task list. See [Task list](/en/interactive-mode#task-list)                                                                                                                                                                                                                                                                                                                             |     |
-| `CLAUDE_CODE_TEAM_NAME`                        | Name of the agent team this teammate belongs to. Set automatically on [agent team](/en/agent-teams) members                                                                                                                                                                                                                                                                                                                                                                                           |     |
-| `CLAUDE_CODE_TMPDIR`                           | Override the temp directory used for internal temp files. Claude Code appends `/claude/` to this path. Default: `/tmp` on Unix/macOS, `os.tmpdir()` on Windows                                                                                                                                                                                                                                                                                                                                        |     |
 | `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`     | Equivalent of setting `DISABLE_AUTOUPDATER`, `DISABLE_BUG_COMMAND`, `DISABLE_ERROR_REPORTING`, and `DISABLE_TELEMETRY`                                                                                                                                                                                                                                                                                                                                                                                |     |
 | `CLAUDE_CODE_DISABLE_TERMINAL_TITLE`           | Set to `1` to disable automatic terminal title updates based on conversation context                                                                                                                                                                                                                                                                                                                                                                                                                  |     |
+| `CLAUDE_CODE_EFFORT_LEVEL`                     | Set the effort level for supported models. Values: `low`, `medium`, `high` (default). Lower effort is faster and cheaper, higher effort provides deeper reasoning. Currently supported with Opus 4.6 only. See [Adjust effort level](/en/model-config#adjust-effort-level)                                                                                                                                                                                                                            |     |
 | `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION`         | Set to `false` to disable prompt suggestions (the "Prompt suggestions" toggle in `/config`). These are the grayed-out predictions that appear in your prompt input after Claude responds. See [Prompt suggestions](/en/interactive-mode#prompt-suggestions)                                                                                                                                                                                                                                           |     |
 | `CLAUDE_CODE_ENABLE_TASKS`                     | Set to `false` to temporarily revert to the previous TODO list instead of the task tracking system. Default: `true`. See [Task list](/en/interactive-mode#task-list)                                                                                                                                                                                                                                                                                                                                  |     |
 | `CLAUDE_CODE_ENABLE_TELEMETRY`                 | Set to `1` to enable OpenTelemetry data collection for metrics and logging. Required before configuring OTel exporters. See [Monitoring](/en/monitoring-usage)                                                                                                                                                                                                                                                                                                                                        |     |
+| `CLAUDE_CODE_EXIT_AFTER_STOP_DELAY`            | Time in milliseconds to wait after the query loop becomes idle before automatically exiting. Useful for automated workflows and scripts using SDK mode                                                                                                                                                                                                                                                                                                                                                |     |
+| `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`         | Set to `1` to enable [agent teams](/en/agent-teams). Agent teams are experimental and disabled by default                                                                                                                                                                                                                                                                                                                                                                                             |     |
 | `CLAUDE_CODE_FILE_READ_MAX_OUTPUT_TOKENS`      | Override the default token limit for file reads. Useful when you need to read larger files in full                                                                                                                                                                                                                                                                                                                                                                                                    |     |
 | `CLAUDE_CODE_HIDE_ACCOUNT_INFO`                | Set to `1` to hide your email address and organization name from the Claude Code UI. Useful when streaming or recording                                                                                                                                                                                                                                                                                                                                                                               |     |
 | `CLAUDE_CODE_IDE_SKIP_AUTO_INSTALL`            | Skip auto-installation of IDE extensions                                                                                                                                                                                                                                                                                                                                                                                                                                                              |     |
 | `CLAUDE_CODE_MAX_OUTPUT_TOKENS`                | Set the maximum number of output tokens for most requests. Default: 32,000. Maximum: 64,000. Increasing this value reduces the effective context window available before [auto-compaction](/en/costs#reduce-token-usage) triggers.                                                                                                                                                                                                                                                                    |     |
+| `CLAUDE_CODE_ORGANIZATION_UUID`                | Organization UUID for the authenticated user. Used by SDK callers to provide account information synchronously. Requires `CLAUDE_CODE_ACCOUNT_UUID` and `CLAUDE_CODE_USER_EMAIL` to also be set                                                                                                                                                                                                                                                                                                       |     |
 | `CLAUDE_CODE_OTEL_HEADERS_HELPER_DEBOUNCE_MS`  | Interval for refreshing dynamic OpenTelemetry headers in milliseconds (default: 1740000 / 29 minutes). See [Dynamic headers](/en/monitoring-usage#dynamic-headers)                                                                                                                                                                                                                                                                                                                                    |     |
 | `CLAUDE_CODE_PLAN_MODE_REQUIRED`               | Auto-set to `true` on [agent team](/en/agent-teams) teammates that require plan approval. Read-only: set by Claude Code when spawning teammates. See [require plan approval](/en/agent-teams#require-plan-approval-for-teammates)                                                                                                                                                                                                                                                                     |     |
-| `CLAUDE_CODE_SIMPLE`                           | Set to `1` to run with a minimal system prompt and only the Bash, file read, and file edit tools. Disables MCP tools, attachments, hooks, and CLAUDE.md files                                                                                                                                                                                                                                                                                                                                         |     |
+| `CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS`            | Timeout in milliseconds for git operations when installing or updating plugins (default: 120000). Increase this value for large repositories or slow network connections. See [Git operations time out](/en/plugin-marketplaces#git-operations-time-out)                                                                                                                                                                                                                                              |     |
+| `CLAUDE_CODE_PROXY_RESOLVES_HOSTS`             | Set to `true` to allow the proxy to perform DNS resolution instead of the caller. Opt-in for environments where the proxy should handle hostname resolution                                                                                                                                                                                                                                                                                                                                           |     |
 | `CLAUDE_CODE_SHELL`                            | Override automatic shell detection. Useful when your login shell differs from your preferred working shell (for example, `bash` vs `zsh`)                                                                                                                                                                                                                                                                                                                                                             |     |
 | `CLAUDE_CODE_SHELL_PREFIX`                     | Command prefix to wrap all bash commands (for example, for logging or auditing). Example: `/path/to/logger.sh` will execute `/path/to/logger.sh <command>`                                                                                                                                                                                                                                                                                                                                            |     |
+| `CLAUDE_CODE_SIMPLE`                           | Set to `1` to run with a minimal system prompt and only the Bash, file read, and file edit tools. Disables MCP tools, attachments, hooks, and CLAUDE.md files                                                                                                                                                                                                                                                                                                                                         |     |
 | `CLAUDE_CODE_SKIP_BEDROCK_AUTH`                | Skip AWS authentication for Bedrock (for example, when using an LLM gateway)                                                                                                                                                                                                                                                                                                                                                                                                                          |     |
 | `CLAUDE_CODE_SKIP_FOUNDRY_AUTH`                | Skip Azure authentication for Microsoft Foundry (for example, when using an LLM gateway)                                                                                                                                                                                                                                                                                                                                                                                                              |     |
 | `CLAUDE_CODE_SKIP_VERTEX_AUTH`                 | Skip Google authentication for Vertex (for example, when using an LLM gateway)                                                                                                                                                                                                                                                                                                                                                                                                                        |     |
 | `CLAUDE_CODE_SUBAGENT_MODEL`                   | See [Model configuration](/en/model-config)                                                                                                                                                                                                                                                                                                                                                                                                                                                           |     |
+| `CLAUDE_CODE_TASK_LIST_ID`                     | Share a task list across sessions. Set the same ID in multiple Claude Code instances to coordinate on a shared task list. See [Task list](/en/interactive-mode#task-list)                                                                                                                                                                                                                                                                                                                             |     |
+| `CLAUDE_CODE_TEAM_NAME`                        | Name of the agent team this teammate belongs to. Set automatically on [agent team](/en/agent-teams) members                                                                                                                                                                                                                                                                                                                                                                                           |     |
+| `CLAUDE_CODE_TMPDIR`                           | Override the temp directory used for internal temp files. Claude Code appends `/claude/` to this path. Default: `/tmp` on Unix/macOS, `os.tmpdir()` on Windows                                                                                                                                                                                                                                                                                                                                        |     |
+| `CLAUDE_CODE_USER_EMAIL`                       | Email address for the authenticated user. Used by SDK callers to provide account information synchronously. Requires `CLAUDE_CODE_ACCOUNT_UUID` and `CLAUDE_CODE_ORGANIZATION_UUID` to also be set                                                                                                                                                                                                                                                                                                    |     |
 | `CLAUDE_CODE_USE_BEDROCK`                      | Use [Bedrock](/en/amazon-bedrock)                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |     |
 | `CLAUDE_CODE_USE_FOUNDRY`                      | Use [Microsoft Foundry](/en/microsoft-foundry)                                                                                                                                                                                                                                                                                                                                                                                                                                                        |     |
 | `CLAUDE_CODE_USE_VERTEX`                       | Use [Vertex](/en/google-vertex-ai)                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |     |

```
### https://code.claude.com/docs/en/cli-reference.md

```diff
--- a/https://code.claude.com/docs/en/cli-reference.md
+++ b/https://code.claude.com/docs/en/cli-reference.md
@@ -8,17 +8,24 @@
 
 ## CLI commands
 
-| Command                         | Description                                            | Example                                           |
-| :------------------------------ | :----------------------------------------------------- | :------------------------------------------------ |
-| `claude`                        | Start interactive REPL                                 | `claude`                                          |
-| `claude "query"`                | Start REPL with initial prompt                         | `claude "explain this project"`                   |
-| `claude -p "query"`             | Query via SDK, then exit                               | `claude -p "explain this function"`               |
-| `cat file \| claude -p "query"` | Process piped content                                  | `cat logs.txt \| claude -p "explain"`             |
-| `claude -c`                     | Continue most recent conversation in current directory | `claude -c`                                       |
-| `claude -c -p "query"`          | Continue via SDK                                       | `claude -c -p "Check for type errors"`            |
-| `claude -r "<session>" "query"` | Resume session by ID or name                           | `claude -r "auth-refactor" "Finish this PR"`      |
-| `claude update`                 | Update to latest version                               | `claude update`                                   |
-| `claude mcp`                    | Configure Model Context Protocol (MCP) servers         | See the [Claude Code MCP documentation](/en/mcp). |
+You can start sessions, pipe content, resume conversations, and manage updates with these commands:
+
+| Command                         | Description                                                                                                                                                                            | Example                                            |
+| :------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------- |
+| `claude`                        | Start interactive session                                                                                                                                                              | `claude`                                           |
+| `claude "query"`                | Start interactive session with initial prompt                                                                                                                                          | `claude "explain this project"`                    |
+| `claude -p "query"`             | Query via SDK, then exit                                                                                                                                                               | `claude -p "explain this function"`                |
+| `cat file \| claude -p "query"` | Process piped content                                                                                                                                                                  | `cat logs.txt \| claude -p "explain"`              |
+| `claude -c`                     | Continue most recent conversation in current directory                                                                                                                                 | `claude -c`                                        |
+| `claude -c -p "query"`          | Continue via SDK                                                                                                                                                                       | `claude -c -p "Check for type errors"`             |
+| `claude -r "<session>" "query"` | Resume session by ID or name                                                                                                                                                           | `claude -r "auth-refactor" "Finish this PR"`       |
+| `claude update`                 | Update to latest version                                                                                                                                                               | `claude update`                                    |
+| `claude auth login`             | Sign in to your Anthropic account. Use `--email` to pre-fill your email address and `--sso` to force SSO authentication                                                                | `claude auth login --email user@example.com --sso` |
+| `claude auth logout`            | Log out from your Anthropic account                                                                                                                                                    | `claude auth logout`                               |
+| `claude auth status`            | Show authentication status as JSON. Use `--text` for human-readable output. Exits with code 0 if logged in, 1 if not                                                                   | `claude auth status`                               |
+| `claude agents`                 | List all configured [subagents](/en/sub-agents), grouped by source                                                                                                                     | `claude agents`                                    |
+| `claude mcp`                    | Configure Model Context Protocol (MCP) servers                                                                                                                                         | See the [Claude Code MCP documentation](/en/mcp).  |
+| `claude remote-control`         | Start a [Remote Control session](/en/remote-control) to control Claude Code from Claude.ai or the Claude app while running locally. See [Remote Control](/en/remote-control) for flags | `claude remote-control`                            |
 
 ## CLI flags
 
@@ -63,7 +70,6 @@
 | `--print`, `-p`                        | Print response without interactive mode (see [Agent SDK documentation](https://platform.claude.com/docs/en/agent-sdk/overview) for programmatic usage details)                                            | `claude -p "query"`                                                                                |
 | `--remote`                             | Create a new [web session](/en/claude-code-on-the-web) on claude.ai with the provided task description                                                                                                    | `claude --remote "Fix the login bug"`                                                              |
 | `--resume`, `-r`                       | Resume a specific session by ID or name, or show an interactive picker to choose a session                                                                                                                | `claude --resume auth-refactor`                                                                    |
-| `--worktree`, `-w`                     | Start Claude in an isolated [git worktree](/en/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees) at `<repo>/.claude/worktrees/<name>`. If no name is given, one is auto-generated    | `claude -w feature-auth`                                                                           |
 | `--session-id`                         | Use a specific session ID for the conversation (must be a valid UUID)                                                                                                                                     | `claude --session-id "550e8400-e29b-41d4-a716-446655440000"`                                       |
 | `--setting-sources`                    | Comma-separated list of setting sources to load (`user`, `project`, `local`)                                                                                                                              | `claude --setting-sources user,project`                                                            |
 | `--settings`                           | Path to a settings JSON file or a JSON string to load additional settings from                                                                                                                            | `claude --settings ./settings.json`                                                                |
@@ -75,6 +81,7 @@
 | `--tools`                              | Restrict which built-in tools Claude can use (works in both interactive and print modes). Use `""` to disable all, `"default"` for all, or tool names like `"Bash,Edit,Read"`                             | `claude --tools "Bash,Edit,Read"`                                                                  |
 | `--verbose`                            | Enable verbose logging, shows full turn-by-turn output (helpful for debugging in both print and interactive modes)                                                                                        | `claude --verbose`                                                                                 |
 | `--version`, `-v`                      | Output the version number                                                                                                                                                                                 | `claude -v`                                                                                        |
+| `--worktree`, `-w`                     | Start Claude in an isolated [git worktree](/en/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees) at `<repo>/.claude/worktrees/<name>`. If no name is given, one is auto-generated    | `claude -w feature-auth`                                                                           |
 
 <Tip>
   The `--output-format json` flag is particularly useful for scripting and
@@ -128,22 +135,22 @@
 
 **When to use each:**
 
-* **`--system-prompt`**: Use when you need complete control over Claude's system prompt. This removes all default Claude Code instructions, giving you a blank slate.
+* **`--system-prompt`**: use when you need complete control over Claude's system prompt. This removes all default Claude Code instructions, giving you a blank slate.
   ```bash  theme={null}
   claude --system-prompt "You are a Python expert who only writes type-annotated code"
   ```
 
-* **`--system-prompt-file`**: Use when you want to load a custom prompt from a file, useful for team consistency or version-controlled prompt templates.
+* **`--system-prompt-file`**: use when you want to load a custom prompt from a file, useful for team consistency or version-controlled prompt templates.
   ```bash  theme={null}
   claude -p --system-prompt-file ./prompts/code-review.txt "Review this PR"
   ```
 
-* **`--append-system-prompt`**: Use when you want to add specific instructions while keeping Claude Code's default capabilities intact. This is the safest option for most use cases.
+* **`--append-system-prompt`**: use when you want to add specific instructions while keeping Claude Code's default capabilities intact. This is the safest option for most use cases.
   ```bash  theme={null}
   claude --append-system-prompt "Always use TypeScript and include JSDoc comments"
   ```
 
-* **`--append-system-prompt-file`**: Use when you want to append instructions from a file while keeping Claude Code's defaults. Useful for version-controlled additions.
+* **`--append-system-prompt-file`**: use when you want to append instructions from a file while keeping Claude Code's defaults. Useful for version-controlled additions.
   ```bash  theme={null}
   claude -p --append-system-prompt-file ./prompts/style-rules.txt "Review this PR"
   ```

```
### https://code.claude.com/docs/en/plugin-marketplaces.md

```diff
--- a/https://code.claude.com/docs/en/plugin-marketplaces.md
+++ b/https://code.claude.com/docs/en/plugin-marketplaces.md
@@ -314,6 +314,53 @@
 | `url` | string | Required. Full git repository URL (must end with `.git`)              |
 | `ref` | string | Optional. Git branch or tag (defaults to repository default branch)   |
 | `sha` | string | Optional. Full 40-character git commit SHA to pin to an exact version |
+
+### npm packages
+
+Plugins distributed as npm packages are installed using `npm install`. This works with any package on the public npm registry or a private registry your team hosts.
+
+```json  theme={null}
+{
+  "name": "my-npm-plugin",
+  "source": {
+    "source": "npm",
+    "package": "@acme/claude-plugin"
+  }
+}
+```
+
+To pin to a specific version, add the `version` field:
+
+```json  theme={null}
+{
+  "name": "my-npm-plugin",
+  "source": {
+    "source": "npm",
+    "package": "@acme/claude-plugin",
+    "version": "2.1.0"
+  }
+}
+```
+
+To install from a private or internal registry, add the `registry` field:
+
+```json  theme={null}
+{
+  "name": "my-npm-plugin",
+  "source": {
+    "source": "npm",
+    "package": "@acme/claude-plugin",
+    "version": "^2.0.0",
+    "registry": "https://npm.example.com"
+  }
+}
+```
+
+| Field      | Type   | Description                                                                                  |
+| :--------- | :----- | :------------------------------------------------------------------------------------------- |
+| `package`  | string | Required. Package name or scoped package (for example, `@org/plugin`)                        |
+| `version`  | string | Optional. Version or version range (for example, `2.1.0`, `^2.0.0`, `~1.5.0`)                |
+| `registry` | string | Optional. Custom npm registry URL. Defaults to the system npm registry (typically npmjs.org) |
 
 ### Advanced plugin entries
 
@@ -680,7 +727,6 @@
 
 * `Marketplace has no plugins defined`: add at least one plugin to the `plugins` array
 * `No marketplace description provided`: add `metadata.description` to help users understand your marketplace
-* `Plugin "x" uses npm source which is not yet fully implemented`: use `github` or local path sources instead
 
 ### Plugin installation failures
 
@@ -713,6 +759,18 @@
 * For GitLab, ensure the token has at least `read_repository` scope
 * Verify the token hasn't expired
 
+### Git operations time out
+
+**Symptoms**: Plugin installation or marketplace updates fail with a timeout error like "Git clone timed out after 120s" or "Git pull timed out after 120s".
+
+**Cause**: Claude Code uses a 120-second timeout for all git operations, including cloning plugin repositories and pulling marketplace updates. Large repositories or slow network connections may exceed this limit.
+
+**Solution**: Increase the timeout using the `CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS` environment variable. The value is in milliseconds:
+
+```bash  theme={null}
+export CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS=300000  # 5 minutes
+```
+
 ### Plugins with relative paths fail in URL-based marketplaces
 
 **Symptoms**: Added a marketplace via URL (such as `https://example.com/marketplace.json`), but plugins with relative path sources like `"./plugins/my-plugin"` fail to install with "path not found" errors.

```
### https://code.claude.com/docs/en/keybindings.md

```diff
--- a/https://code.claude.com/docs/en/keybindings.md
+++ b/https://code.claude.com/docs/en/keybindings.md
@@ -292,7 +292,7 @@
 
 For example:
 
-```
+```text  theme={null}
 ctrl+k          Single key with modifier
 shift+tab       Shift + Tab
 meta+p          Command/Meta + P
@@ -309,7 +309,7 @@
 
 Chords are sequences of keystrokes separated by spaces:
 
-```
+```text  theme={null}
 ctrl+k ctrl+s   Press Ctrl+K, release, then Ctrl+S
 ```
 

```
### https://code.claude.com/docs/en/terminal-config.md

```diff
--- a/https://code.claude.com/docs/en/terminal-config.md
+++ b/https://code.claude.com/docs/en/terminal-config.md
@@ -42,22 +42,23 @@
 
 ### Notification setup
 
-Never miss when Claude completes a task with proper notification configuration:
+When Claude finishes working and is waiting for your input, it fires a notification event. You can surface this event as a desktop notification through your terminal or run custom logic with [notification hooks](/en/hooks#notification).
 
-#### iTerm 2 system notifications
+#### Terminal notifications
 
-For iTerm 2 alerts when tasks complete:
+Kitty and Ghostty support desktop notifications without additional configuration. iTerm 2 requires setup:
 
-1. Open iTerm 2 Preferences
-2. Navigate to Profiles → Terminal
-3. Enable "Silence bell" and Filter Alerts → "Send escape sequence-generated alerts"
-4. Set your preferred notification delay
+1. Open iTerm 2 Settings → Profiles → Terminal
+2. Enable "Notification Center Alerts"
+3. Click "Filter Alerts" and check "Send escape sequence-generated alerts"
 
-Note that these notifications are specific to iTerm 2 and not available in the default macOS Terminal.
+If notifications aren't appearing, verify that your terminal app has notification permissions in your OS settings.
 
-#### Custom notification hooks
+Other terminals, including the default macOS Terminal, do not support native notifications. Use [notification hooks](/en/hooks#notification) instead.
 
-For advanced notification handling, you can create [notification hooks](/en/hooks#notification) to run your own logic.
+#### Notification hooks
+
+To add custom behavior when notifications fire, such as playing a sound or sending a message, configure a [notification hook](/en/hooks#notification). Hooks run alongside terminal notifications, not as a replacement.
 
 ### Handling large inputs
 

```
### https://code.claude.com/docs/en/headless.md

```diff
--- a/https://code.claude.com/docs/en/headless.md
+++ b/https://code.claude.com/docs/en/headless.md
@@ -152,20 +152,7 @@
 
 ## Next steps
 
-<CardGroup cols={2}>
-  <Card title="Agent SDK quickstart" icon="play" href="https://platform.claude.com/docs/en/agent-sdk/quickstart">
-    Build your first agent with Python or TypeScript
-  </Card>
-
-  <Card title="CLI reference" icon="terminal" href="/en/cli-reference">
-    Explore all CLI flags and options
-  </Card>
-
-  <Card title="GitHub Actions" icon="github" href="/en/github-actions">
-    Use the Agent SDK in GitHub workflows
-  </Card>
-
-  <Card title="GitLab CI/CD" icon="gitlab" href="/en/gitlab-ci-cd">
-    Use the Agent SDK in GitLab pipelines
-  </Card>
-</CardGroup>
+* [Agent SDK quickstart](https://platform.claude.com/docs/en/agent-sdk/quickstart): build your first agent with Python or TypeScript
+* [CLI reference](/en/cli-reference): all CLI flags and options
+* [GitHub Actions](/en/github-actions): use the Agent SDK in GitHub workflows
+* [GitLab CI/CD](/en/gitlab-ci-cd): use the Agent SDK in GitLab pipelines

```
### https://code.claude.com/docs/en/model-config.md

```diff
--- a/https://code.claude.com/docs/en/model-config.md
+++ b/https://code.claude.com/docs/en/model-config.md
@@ -55,7 +55,7 @@
 
 Example settings file:
 
-```
+```json  theme={null}
 {
     "permissions": {
         ...
@@ -78,12 +78,7 @@
 
 ### Default model behavior
 
-The Default option in the model picker is not affected by `availableModels`. It always remains available and represents the system's runtime default based on the user's subscription tier:
-
-| User type                     | Default model |
-| :---------------------------- | :------------ |
-| Max, Team, or Pro subscribers | Opus 4.6      |
-| Pay-as-you-go (API) users     | Sonnet 4.5    |
+The Default option in the model picker is not affected by `availableModels`. It always remains available and represents the system's runtime default [based on the user's subscription tier](#default-model-setting).
 
 Even with `availableModels: []`, users can still use Claude Code with the Default model for their tier.
 
@@ -94,7 +89,7 @@
 * **availableModels**: restricts what users can switch to
 * **model**: sets the explicit model override, taking precedence over the Default
 
-This example ensures all users run Sonnet 4.5 and can only choose between Sonnet and Haiku:
+This example ensures all users run Sonnet 4.6 and can only choose between Sonnet and Haiku:
 
 ```json  theme={null}
 {
@@ -157,6 +152,8 @@
 
 * **API and pay-as-you-go users**: full access to 1M context
 * **Pro, Max, Teams, and Enterprise subscribers**: available with [extra usage](https://support.claude.com/en/articles/12429409-extra-usage-for-paid-claude-plans) enabled
+
+To disable 1M context entirely, set `CLAUDE_CODE_DISABLE_1M_CONTEXT=1`. This removes 1M model variants from the model picker. See [environment variables](/en/settings#environment-variables).
 
 Selecting a 1M model does not immediately change billing. Your session uses standard rates until it exceeds 200K tokens of context. Beyond 200K tokens, requests are charged at [long-context pricing](https://platform.claude.com/docs/en/about-claude/pricing#long-context-pricing) with dedicated [rate limits](https://platform.claude.com/docs/en/api/rate-limits#long-context-rate-limits). For subscribers, tokens beyond 200K are billed as extra usage rather than through the subscription.
 

```
### https://code.claude.com/docs/en/discover-plugins.md

```diff
--- a/https://code.claude.com/docs/en/discover-plugins.md
+++ b/https://code.claude.com/docs/en/discover-plugins.md
@@ -356,6 +356,21 @@
 
 Team admins can set up automatic marketplace installation for projects by adding marketplace configuration to `.claude/settings.json`. When team members trust the repository folder, Claude Code prompts them to install these marketplaces and plugins.
 
+Add `extraKnownMarketplaces` to your project's `.claude/settings.json`:
+
+```json  theme={null}
+{
+  "extraKnownMarketplaces": {
+    "my-team-tools": {
+      "source": {
+        "source": "github",
+        "repo": "your-org/claude-plugins"
+      }
+    }
+  }
+}
+```
+
 For full configuration options including `extraKnownMarketplaces` and `enabledPlugins`, see [Plugin settings](/en/settings#plugin-settings).
 
 ## Troubleshooting

```
