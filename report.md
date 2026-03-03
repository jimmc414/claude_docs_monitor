# Claude Docs Monitor Report

*Generated: 2026-03-03 03:44:04 UTC*

| Metric | Count |
|--------|------:|
| Changed | 22 |
| Added | 1 |
| Removed | 0 |
| Errors | 0 |

## Added Pages

- https://code.claude.com/docs/en/zero-data-retention.md

## Diffs

### https://code.claude.com/docs/en/how-claude-code-works.md

```diff
--- a/https://code.claude.com/docs/en/how-claude-code-works.md
+++ b/https://code.claude.com/docs/en/how-claude-code-works.md
@@ -61,12 +61,15 @@
 
 ## What Claude can access
 
+This guide focuses on the terminal. Claude Code also runs in [VS Code](/en/vs-code), [JetBrains IDEs](/en/jetbrains), and other environments.
+
 When you run `claude` in a directory, Claude Code gains access to:
 
 * **Your project.** Files in your directory and subdirectories, plus files elsewhere with your permission.
 * **Your terminal.** Any command you could run: build tools, git, package managers, system utilities, scripts. If you can do it from the command line, Claude can too.
 * **Your git state.** Current branch, uncommitted changes, and recent commit history.
 * **Your [CLAUDE.md](/en/memory).** A markdown file where you store project-specific instructions, conventions, and context that Claude should know every session.
+* **[Auto memory](/en/memory#auto-memory).** Learnings Claude saves automatically as you work, like project patterns and your preferences. The first 200 lines of MEMORY.md are loaded at the start of each session.
 * **Extensions you configure.** [MCP servers](/en/mcp) for external services, [skills](/en/skills) for workflows, [subagents](/en/sub-agents) for delegated work, and [Claude in Chrome](/en/chrome) for browser interaction.
 
 Because Claude sees your whole project, it can work across it. When you ask Claude to "fix the authentication bug," it searches for relevant files, reads multiple files to understand context, makes coordinated edits across them, runs tests to verify the fix, and commits the changes if you ask. This is different from inline code assistants that only see the current file.

```
### https://code.claude.com/docs/en/vs-code.md

```diff
--- a/https://code.claude.com/docs/en/vs-code.md
+++ b/https://code.claude.com/docs/en/vs-code.md
@@ -106,7 +106,7 @@
 
 ### Resume past conversations
 
-Click the dropdown at the top of the Claude Code panel to access your conversation history. You can search by keyword or browse by time (Today, Yesterday, Last 7 days, etc.). Click any conversation to resume it with the full message history. For more on resuming sessions, see [Common workflows](/en/common-workflows#resume-previous-conversations).
+Click the dropdown at the top of the Claude Code panel to access your conversation history. You can search by keyword or browse by time (Today, Yesterday, Last 7 days, etc.). Click any conversation to resume it with the full message history. Hover over a session to reveal rename and remove actions: rename to give it a descriptive title, or remove to delete it from the list. For more on resuming sessions, see [Common workflows](/en/common-workflows#resume-previous-conversations).
 
 ### Resume remote sessions from Claude.ai
 

```
### https://code.claude.com/docs/en/memory.md

```diff
--- a/https://code.claude.com/docs/en/memory.md
+++ b/https://code.claude.com/docs/en/memory.md
@@ -2,184 +2,142 @@
 > Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
 > Use this file to discover all available pages before exploring further.
 
-# Manage Claude's memory
-
-> Learn how to manage Claude Code's memory across sessions with different memory locations and best practices.
-
-Claude Code has two kinds of memory that persist across sessions:
-
-* **Auto memory**: Claude automatically saves useful context like project patterns, key commands, and your preferences. This persists across sessions.
-* **CLAUDE.md files**: Markdown files you write and maintain with instructions, rules, and preferences for Claude to follow.
-
-Both are loaded into Claude's context at the start of every session, though auto memory loads only the first 200 lines of its main file.
-
-## Determine memory type
-
-Claude Code offers several memory locations in a hierarchical structure, each serving a different purpose:
-
-| Memory Type                | Location                                                                                                                                                        | Purpose                                             | Use Case Examples                                                    | Shared With                     |
-| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------- |
-| **Managed policy**         | • macOS: `/Library/Application Support/ClaudeCode/CLAUDE.md`<br />• Linux: `/etc/claude-code/CLAUDE.md`<br />• Windows: `C:\Program Files\ClaudeCode\CLAUDE.md` | Organization-wide instructions managed by IT/DevOps | Company coding standards, security policies, compliance requirements | All users in organization       |
-| **Project memory**         | `./CLAUDE.md` or `./.claude/CLAUDE.md`                                                                                                                          | Team-shared instructions for the project            | Project architecture, coding standards, common workflows             | Team members via source control |
-| **Project rules**          | `./.claude/rules/*.md`                                                                                                                                          | Modular, topic-specific project instructions        | Language-specific guidelines, testing conventions, API standards     | Team members via source control |
-| **User memory**            | `~/.claude/CLAUDE.md`                                                                                                                                           | Personal preferences for all projects               | Code styling preferences, personal tooling shortcuts                 | Just you (all projects)         |
-| **Project memory (local)** | `./CLAUDE.local.md`                                                                                                                                             | Personal project-specific preferences               | Your sandbox URLs, preferred test data                               | Just you (current project)      |
-| **Auto memory**            | `~/.claude/projects/<project>/memory/`                                                                                                                          | Claude's automatic notes and learnings              | Project patterns, debugging insights, architecture notes             | Just you (per project)          |
-
-CLAUDE.md files in the directory hierarchy above the working directory are loaded in full at launch. CLAUDE.md files in child directories load on demand when Claude reads files in those directories. Auto memory loads only the first 200 lines of `MEMORY.md`. More specific instructions take precedence over broader ones.
-
-<Note>
-  CLAUDE.local.md files are automatically added to .gitignore, making them ideal for private project-specific preferences that shouldn't be checked into version control.
-</Note>
-
-## Auto memory
-
-Auto memory is a persistent directory where Claude records learnings, patterns, and insights as it works. Unlike CLAUDE.md files that contain instructions you write for Claude, auto memory contains notes Claude writes for itself based on what it discovers during sessions.
-
-<Note>
-  Auto memory is enabled by default. To toggle it on or off, use `/memory` and select the auto-memory toggle.
-</Note>
-
-### What Claude remembers
-
-As Claude works, it may save things like:
-
-* Project patterns: build commands, test conventions, code style preferences
-* Debugging insights: solutions to tricky problems, common error causes
-* Architecture notes: key files, module relationships, important abstractions
-* Your preferences: communication style, workflow habits, tool choices
-
-### Where auto memory is stored
-
-Each project gets its own memory directory at `~/.claude/projects/<project>/memory/`. The `<project>` path is derived from the git repository root, so all subdirectories within the same repo share one auto memory directory. Git worktrees get separate memory directories. Outside a git repo, the working directory is used instead.
-
-The directory contains a `MEMORY.md` entrypoint and optional topic files:
-
-```text  theme={null}
-~/.claude/projects/<project>/memory/
-├── MEMORY.md          # Concise index, loaded into every session
-├── debugging.md       # Detailed notes on debugging patterns
-├── api-conventions.md # API design decisions
-└── ...                # Any other topic files Claude creates
-```
-
-`MEMORY.md` acts as an index of the memory directory. Claude reads and writes files in this directory throughout your session, using `MEMORY.md` to keep track of what's stored where.
-
-### How it works
-
-* The first 200 lines of `MEMORY.md` are loaded into Claude's system prompt at the start of every session. Content beyond 200 lines is not loaded automatically, and Claude is instructed to keep it concise by moving detailed notes into separate topic files.
-* Topic files like `debugging.md` or `patterns.md` are not loaded at startup. Claude reads them on demand using its standard file tools when it needs the information.
-* Claude reads and writes memory files during your session, so you'll see memory updates happen as you work.
-
-### Manage auto memory
-
-Auto memory files are markdown files you can edit at any time. Use `/memory` to open the file selector, which includes your auto memory entrypoint alongside your CLAUDE.md files. The `/memory` selector also includes an auto-memory toggle to turn the feature on or off.
-
-To ask Claude to save something specific, tell it directly: "remember that we use pnpm, not npm" or "save to memory that the API tests require a local Redis instance".
-
-You can also control auto memory through settings or environment variables.
-
-Disable auto memory for all projects by adding `autoMemoryEnabled` to your user settings:
-
-```json  theme={null}
-// ~/.claude/settings.json
-{ "autoMemoryEnabled": false }
-```
-
-Disable auto memory for a single project by adding `autoMemoryEnabled` to the project settings:
-
-```json  theme={null}
-// .claude/settings.json
-{ "autoMemoryEnabled": false }
-```
-
-Override all other settings with the `CLAUDE_CODE_DISABLE_AUTO_MEMORY` environment variable. This takes precedence over both the `/memory` toggle and `settings.json`, making it useful for CI or managed environments:
-
-```bash  theme={null}
-export CLAUDE_CODE_DISABLE_AUTO_MEMORY=1  # Force off
-export CLAUDE_CODE_DISABLE_AUTO_MEMORY=0  # Force on
-```
-
-## CLAUDE.md imports
-
-CLAUDE.md files can import additional files using `@path/to/import` syntax. The following example imports 3 files:
-
-```
+# How Claude remembers your project
+
+> Give Claude persistent instructions with CLAUDE.md files, and let Claude accumulate learnings automatically with auto memory.
+
+Each Claude Code session begins with a fresh context window. Two mechanisms carry knowledge across sessions:
+
+* **CLAUDE.md files**: instructions you write to give Claude persistent context
+* **Auto memory**: notes Claude writes itself based on your corrections and preferences
+
+This page covers how to:
+
+* [Write and organize CLAUDE.md files](#claudemd-files)
+* [Scope rules to specific file types](#organize-rules-with-clauderules) with `.claude/rules/`
+* [Configure auto memory](#auto-memory) so Claude takes notes automatically
+* [Troubleshoot](#troubleshoot-memory-issues) when instructions aren't being followed
+
+## CLAUDE.md vs auto memory
+
+Claude Code has two complementary memory systems. Both are loaded at the start of every conversation. Claude treats them as context, not enforced configuration. The more specific and concise your instructions, the more consistently Claude follows them.
+
+|                      | CLAUDE.md files                                   | Auto memory                                                      |
+| :------------------- | :------------------------------------------------ | :--------------------------------------------------------------- |
+| **Who writes it**    | You                                               | Claude                                                           |
+| **What it contains** | Instructions and rules                            | Learnings and patterns                                           |
+| **Scope**            | Project, user, or org                             | Per working tree                                                 |
+| **Loaded into**      | Every session                                     | Every session (first 200 lines)                                  |
+| **Use for**          | Coding standards, workflows, project architecture | Build commands, debugging insights, preferences Claude discovers |
+
+Use CLAUDE.md files when you want to guide Claude's behavior. Auto memory lets Claude learn from your corrections without manual effort.
+
+Subagents can also maintain their own auto memory. See [subagent configuration](/en/sub-agents#enable-persistent-memory) for details.
+
+## CLAUDE.md files
+
+CLAUDE.md files are markdown files that give Claude persistent instructions for a project, your personal workflow, or your entire organization. You write these files in plain text; Claude reads them at the start of every session.
+
+### Choose where to put CLAUDE.md files
+
+CLAUDE.md files can live in several locations, each with a different scope. More specific locations take precedence over broader ones.
+
+| Scope                    | Location                                                                                                                                                                | Purpose                                                     | Use case examples                                                    | Shared with                     |
+| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------- |
+| **Managed policy**       | • macOS: `/Library/Application Support/ClaudeCode/CLAUDE.md`<br />• Linux and WSL: `/etc/claude-code/CLAUDE.md`<br />• Windows: `C:\Program Files\ClaudeCode\CLAUDE.md` | Organization-wide instructions managed by IT/DevOps         | Company coding standards, security policies, compliance requirements | All users in organization       |
+| **Project instructions** | `./CLAUDE.md` or `./.claude/CLAUDE.md`                                                                                                                                  | Team-shared instructions for the project                    | Project architecture, coding standards, common workflows             | Team members via source control |
+| **User instructions**    | `~/.claude/CLAUDE.md`                                                                                                                                                   | Personal preferences for all projects                       | Code styling preferences, personal tooling shortcuts                 | Just you (all projects)         |
+| **Local instructions**   | `./CLAUDE.local.md`                                                                                                                                                     | Personal project-specific preferences, not checked into git | Your sandbox URLs, preferred test data                               | Just you (current project)      |
+
+CLAUDE.md files in the directory hierarchy above the working directory are loaded in full at launch. CLAUDE.md files in subdirectories load on demand when Claude reads files in those directories. See [How CLAUDE.md files load](#how-claudemd-files-load) for the full resolution order.
+
+For large projects, you can break instructions into topic-specific files using [project rules](#organize-rules-with-clauderules). Rules let you scope instructions to specific file types or subdirectories.
+
+### Set up a project CLAUDE.md
+
+A project CLAUDE.md can be stored in either `./CLAUDE.md` or `./.claude/CLAUDE.md`. Create this file and add instructions that apply to anyone working on the project: build and test commands, coding standards, architectural decisions, naming conventions, and common workflows. These instructions are shared with your team through version control, so focus on project-level standards rather than personal preferences.
+
+<Tip>
+  Run `/init` to generate a starting CLAUDE.md automatically. Claude analyzes your codebase and creates a file with build commands, test instructions, and project conventions it discovers. If a CLAUDE.md already exists, `/init` suggests improvements rather than overwriting it. Refine from there with instructions Claude wouldn't discover on its own.
+</Tip>
+
+### Write effective instructions
+
+CLAUDE.md files are loaded into the context window at the start of every session, consuming tokens alongside your conversation. Because they're context rather than enforced configuration, how you write instructions affects how reliably Claude follows them. Specific, concise, well-structured instructions work best.
+
+**Size**: target under 200 lines per CLAUDE.md file. Longer files consume more context and reduce adherence. If your instructions are growing large, split them using [imports](#import-additional-files) or [`.claude/rules/`](#organize-rules-with-clauderules) files.
+
+**Structure**: use markdown headers and bullets to group related instructions. Claude scans structure the same way readers do: organized sections are easier to follow than dense paragraphs.
+
+**Specificity**: write instructions that are concrete enough to verify. For example:
+
+* "Use 2-space indentation" instead of "Format code properly"
+* "Run `npm test` before committing" instead of "Test your changes"
+* "API handlers live in `src/api/handlers/`" instead of "Keep files organized"
+
+**Consistency**: if two rules contradict each other, Claude may pick one arbitrarily. Review your CLAUDE.md files, nested CLAUDE.md files in subdirectories, and [`.claude/rules/`](#organize-rules-with-clauderules) periodically to remove outdated or conflicting instructions. In monorepos, use [`claudeMdExcludes`](#exclude-specific-claudemd-files) to skip CLAUDE.md files from other teams that aren't relevant to your work.
+
+### Import additional files
+
+CLAUDE.md files can import additional files using `@path/to/import` syntax. Imported files are expanded and loaded into context at launch alongside the CLAUDE.md that references them.
+
+Both relative and absolute paths are allowed. Relative paths resolve relative to the file containing the import, not the working directory. Imported files can recursively import other files, with a maximum depth of five hops.
+
+To pull in a README, package.json, and a workflow guide, reference them with `@` syntax anywhere in your CLAUDE.md:
+
+```text  theme={null}
 See @README for project overview and @package.json for available npm commands for this project.
 
 # Additional Instructions
 - git workflow @docs/git-instructions.md
 ```
 
-Both relative and absolute paths are allowed. Relative paths resolve relative to the file containing the import, not the working directory. For private per-project preferences that shouldn't be checked into version control, prefer `CLAUDE.local.md`: it is automatically loaded and added to `.gitignore`.
+For private per-project preferences that shouldn't be checked into version control, use `CLAUDE.local.md`: it is automatically loaded and added to `.gitignore`.
 
 If you work across multiple git worktrees, `CLAUDE.local.md` only exists in one. Use a home-directory import instead so all worktrees share the same personal instructions:
 
-```
+```text  theme={null}
 # Individual Preferences
 - @~/.claude/my-project-instructions.md
 ```
 
 <Warning>
-  The first time Claude Code encounters external imports in a project, it shows an approval dialog listing the specific files. Approve to load them; decline to skip them. This is a one-time decision per project: once declined, the dialog does not resurface and the imports remain disabled.
+  The first time Claude Code encounters external imports in a project, it shows an approval dialog listing the files. If you decline, the imports stay disabled and the dialog does not appear again.
 </Warning>
 
-To avoid potential collisions, imports are not evaluated inside markdown code spans and code blocks.
-
-```
-This code span will not be treated as an import: `@anthropic-ai/claude-code`
-```
-
-Imported files can recursively import additional files, with a max-depth of 5 hops. You can see what memory files are loaded by running `/memory` command.
-
-## How Claude looks up memories
-
-Claude Code reads memories recursively: starting in the cwd, Claude Code recurses up to (but not including) the root directory */* and reads any CLAUDE.md or CLAUDE.local.md files it finds. This is especially convenient when working in large repositories where you run Claude Code in *foo/bar/*, and have memories in both *foo/CLAUDE.md* and *foo/bar/CLAUDE.md*.
-
-Claude will also discover CLAUDE.md nested in subtrees under your current working directory. Instead of loading them at launch, they are only included when Claude reads files in those subtrees.
-
-### Load memory from additional directories
+For a more structured approach to organizing instructions, see [`.claude/rules/`](#organize-rules-with-clauderules).
+
+### How CLAUDE.md files load
+
+Claude Code reads CLAUDE.md files by walking up the directory tree from your current working directory, checking each directory along the way for CLAUDE.md and CLAUDE.local.md files. This means if you run Claude Code in `foo/bar/`, it loads instructions from both `foo/bar/CLAUDE.md` and `foo/CLAUDE.md`.
+
+Claude also discovers CLAUDE.md files in subdirectories under your current working directory. Instead of loading them at launch, they are included when Claude reads files in those subdirectories.
+
+If you work in a large monorepo where other teams' CLAUDE.md files get picked up, use [`claudeMdExcludes`](#exclude-specific-claudemd-files) to skip them.
+
+#### Load from additional directories
 
 The `--add-dir` flag gives Claude access to additional directories outside your main working directory. By default, CLAUDE.md files from these directories are not loaded.
 
-To also load memory files (CLAUDE.md, .claude/CLAUDE.md, and .claude/rules/\*.md) from additional directories, set the `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD` environment variable:
+To also load CLAUDE.md files from additional directories, including `CLAUDE.md`, `.claude/CLAUDE.md`, and `.claude/rules/*.md`, set the `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD` environment variable:
 
 ```bash  theme={null}
 CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1 claude --add-dir ../shared-config
 ```
 
-## Directly edit memories with `/memory`
-
-Use the `/memory` command during a session to open any memory file in your system editor for more extensive additions or organization.
-
-## Set up project memory
-
-Suppose you want to set up a CLAUDE.md file to store important project information, conventions, and frequently used commands. Project memory can be stored in either `./CLAUDE.md` or `./.claude/CLAUDE.md`.
-
-Bootstrap a CLAUDE.md for your codebase with the following command:
-
-```
-> /init
-```
-
-<Tip>
-  Tips:
-
-  * Include frequently used commands (build, test, lint) to avoid repeated searches
-  * Document code style preferences and naming conventions
-  * Add important architectural patterns specific to your project
-  * CLAUDE.md memories can be used for both instructions shared with your team and for your individual preferences.
-</Tip>
-
-## Modular rules with `.claude/rules/`
-
-For larger projects, you can organize instructions into multiple files using the `.claude/rules/` directory. This allows teams to maintain focused, well-organized rule files instead of one large CLAUDE.md.
-
-### Basic structure
-
-Place markdown files in your project's `.claude/rules/` directory:
-
-```
+### Organize rules with `.claude/rules/`
+
+For larger projects, you can organize instructions into multiple files using the `.claude/rules/` directory. This keeps instructions modular and easier for teams to maintain. Rules can also be [scoped to specific file paths](#path-specific-rules), so they only load into context when Claude works with matching files, reducing noise and saving context space.
+
+<Note>
+  Rules load into context every session or when matching files are opened. For task-specific instructions that don't need to be in context all the time, use [skills](/en/skills) instead, which only load when you invoke them or when Claude determines they're relevant to your prompt.
+</Note>
+
+#### Set up rules
+
+Place markdown files in your project's `.claude/rules/` directory. Each file should cover one topic, with a descriptive filename like `testing.md` or `api-design.md`. All `.md` files are discovered recursively, so you can organize rules into subdirectories like `frontend/` or `backend/`:
+
+```text  theme={null}
 your-project/
 ├── .claude/
 │   ├── CLAUDE.md           # Main project instructions
@@ -189,9 +147,9 @@
 │       └── security.md     # Security requirements
 ```
 
-All `.md` files in `.claude/rules/` are automatically loaded as project memory, with the same priority as `.claude/CLAUDE.md`.
-
-### Path-specific rules
+Rules without [`paths` frontmatter](#path-specific-rules) are loaded at launch with the same priority as `.claude/CLAUDE.md`.
+
+#### Path-specific rules
 
 Rules can be scoped to specific files using YAML frontmatter with the `paths` field. These conditional rules only apply when Claude is working with files matching the specified patterns.
 
@@ -208,11 +166,9 @@
 - Include OpenAPI documentation comments
 ```
 
-Rules without a `paths` field are loaded unconditionally and apply to all files.
-
-### Glob patterns
-
-The `paths` field supports standard glob patterns:
+Rules without a `paths` field are loaded unconditionally and apply to all files. Path-scoped rules trigger when Claude reads files matching the pattern, not on every tool use.
+
+Use glob patterns in the `paths` field to match files by extension, directory, or any combination:
 
 | Pattern                | Matches                                  |
 | ---------------------- | ---------------------------------------- |
@@ -221,67 +177,33 @@
 | `*.md`                 | Markdown files in the project root       |
 | `src/components/*.tsx` | React components in a specific directory |
 
-You can specify multiple patterns:
-
-```markdown  theme={null}
----
-paths:
-  - "src/**/*.ts"
-  - "lib/**/*.ts"
-  - "tests/**/*.test.ts"
----
-```
-
-Brace expansion is supported for matching multiple extensions or directories:
+You can specify multiple patterns and use brace expansion to match multiple extensions in one pattern:
 
 ```markdown  theme={null}
 ---
 paths:
   - "src/**/*.{ts,tsx}"
-  - "{src,lib}/**/*.ts"
+  - "lib/**/*.ts"
+  - "tests/**/*.test.ts"
 ---
-
-# TypeScript/React Rules
-```
-
-This expands `src/**/*.{ts,tsx}` to match both `.ts` and `.tsx` files.
-
-### Subdirectories
-
-Rules can be organized into subdirectories for better structure:
-
-```
-.claude/rules/
-├── frontend/
-│   ├── react.md
-│   └── styles.md
-├── backend/
-│   ├── api.md
-│   └── database.md
-└── general.md
-```
-
-All `.md` files are discovered recursively.
-
-### Symlinks
-
-The `.claude/rules/` directory supports symlinks, allowing you to share common rules across multiple projects:
+```
+
+#### Share rules across projects with symlinks
+
+The `.claude/rules/` directory supports symlinks, so you can maintain a shared set of rules and link them into multiple projects. Symlinks are resolved and loaded normally, and circular symlinks are detected and handled gracefully.
+
+This example links both a shared directory and an individual file:
 
 ```bash  theme={null}
-# Symlink a shared rules directory
 ln -s ~/shared-claude-rules .claude/rules/shared
-
-# Symlink individual rule files
 ln -s ~/company-standards/security.md .claude/rules/security.md
 ```
 
-Symlinks are resolved and their contents are loaded normally. Circular symlinks are detected and handled gracefully.
-
-### User-level rules
-
-You can create personal rules that apply to all your projects in `~/.claude/rules/`:
-
-```
+#### User-level rules
+
+Personal rules in `~/.claude/rules/` apply to every project on your machine. Use them for preferences that aren't project-specific:
+
+```text  theme={null}
 ~/.claude/rules/
 ├── preferences.md    # Your personal coding preferences
 └── workflows.md      # Your preferred workflows
@@ -289,27 +211,131 @@
 
 User-level rules are loaded before project rules, giving project rules higher priority.
 
-<Tip>
-  Best practices for `.claude/rules/`:
-
-  * **Keep rules focused**: Each file should cover one topic (e.g., `testing.md`, `api-design.md`)
-  * **Use descriptive filenames**: The filename should indicate what the rules cover
-  * **Use conditional rules sparingly**: Only add `paths` frontmatter when rules truly apply to specific file types
-  * **Organize with subdirectories**: Group related rules (e.g., `frontend/`, `backend/`)
-</Tip>
-
-## Organization-level memory management
-
-Organizations can deploy centrally managed CLAUDE.md files that apply to all users.
-
-To set up organization-level memory management:
-
-1. Create the managed memory file at the **Managed policy** location shown in the [memory types table above](#determine-memory-type).
-
-2. Deploy via your configuration management system (MDM, Group Policy, Ansible, etc.) to ensure consistent distribution across all developer machines.
-
-## Memory best practices
-
-* **Be specific**: "Use 2-space indentation" is better than "Format code properly".
-* **Use structure to organize**: Format each individual memory as a bullet point and group related memories under descriptive markdown headings.
-* **Review periodically**: Update memories as your project evolves to ensure Claude is always using the most up to date information and context.
+### Manage CLAUDE.md for large teams
+
+For organizations deploying Claude Code across teams, you can centralize instructions and control which CLAUDE.md files are loaded.
+
+#### Deploy organization-wide CLAUDE.md
+
+Organizations can deploy a centrally managed CLAUDE.md that applies to all users on a machine. This file cannot be excluded by individual settings.
+
+<Steps>
+  <Step title="Create the file at the managed policy location">
+    * macOS: `/Library/Application Support/ClaudeCode/CLAUDE.md`
+    * Linux and WSL: `/etc/claude-code/CLAUDE.md`
+    * Windows: `C:\Program Files\ClaudeCode\CLAUDE.md`
+  </Step>
+
+  <Step title="Deploy with your configuration management system">
+    Use MDM, Group Policy, Ansible, or similar tools to distribute the file across developer machines. See [managed settings](/en/permissions#managed-settings) for other organization-wide configuration options.
+  </Step>
+</Steps>
+
+#### Exclude specific CLAUDE.md files
+
+In large monorepos, ancestor CLAUDE.md files may contain instructions that aren't relevant to your work. The `claudeMdExcludes` setting lets you skip specific files by path or glob pattern.
+
+This example excludes a top-level CLAUDE.md and a rules directory from a parent folder. Add it to `.claude/settings.local.json` so the exclusion stays local to your machine:
+
+```json  theme={null}
+{
+  "claudeMdExcludes": [
+    "**/monorepo/CLAUDE.md",
+    "/home/user/monorepo/other-team/.claude/rules/**"
+  ]
+}
+```
+
+Patterns are matched against absolute file paths using glob syntax. You can configure `claudeMdExcludes` at any [settings layer](/en/settings#settings-files): user, project, local, or managed policy. Arrays merge across layers.
+
+Managed policy CLAUDE.md files cannot be excluded. This ensures organization-wide instructions always apply regardless of individual settings.
+
+## Auto memory
+
+Auto memory lets Claude accumulate knowledge across sessions without you writing anything. Claude saves notes for itself as it works: build commands, debugging insights, architecture notes, code style preferences, and workflow habits. Claude doesn't save something every session. It decides what's worth remembering based on whether the information would be useful in a future conversation.
+
+### Enable or disable auto memory
+
+Auto memory is on by default. To toggle it, open `/memory` in a session and use the auto memory toggle, or set `autoMemoryEnabled` in your project settings:
+
+```json  theme={null}
+{
+  "autoMemoryEnabled": false
+}
+```
+
+To disable auto memory via environment variable, set `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`.
+
+### Storage location
+
+Each project gets its own memory directory at `~/.claude/projects/<project>/memory/`. The `<project>` path is derived from the git repository, so all worktrees and subdirectories within the same repo share one auto memory directory. Outside a git repo, the project root is used instead.
+
+The directory contains a `MEMORY.md` entrypoint and optional topic files:
+
+```text  theme={null}
+~/.claude/projects/<project>/memory/
+├── MEMORY.md          # Concise index, loaded into every session
+├── debugging.md       # Detailed notes on debugging patterns
+├── api-conventions.md # API design decisions
+└── ...                # Any other topic files Claude creates
+```
+
+`MEMORY.md` acts as an index of the memory directory. Claude reads and writes files in this directory throughout your session, using `MEMORY.md` to keep track of what's stored where.
+
+Auto memory is machine-local. All worktrees and subdirectories within the same git repository share one auto memory directory. Files are not shared across machines or cloud environments.
+
+### How it works
+
+The first 200 lines of `MEMORY.md` are loaded at the start of every conversation. Content beyond line 200 is not loaded at session start. Claude keeps `MEMORY.md` concise by moving detailed notes into separate topic files.
+
+This 200-line limit applies only to `MEMORY.md`. CLAUDE.md files are loaded in full regardless of length, though shorter files produce better adherence.
+
+Topic files like `debugging.md` or `patterns.md` are not loaded at startup. Claude reads them on demand using its standard file tools when it needs the information.
+
+Claude reads and writes memory files during your session. When you see "Writing memory" or "Recalled memory" in the Claude Code interface, Claude is actively updating or reading from `~/.claude/projects/<project>/memory/`.
+
+### Audit and edit your memory
+
+Auto memory files are plain markdown you can edit or delete at any time. Run [`/memory`](#view-and-edit-with-memory) to browse and open memory files from within a session.
+
+## View and edit with `/memory`
+
+The `/memory` command lists all CLAUDE.md and rules files loaded in your current session, lets you toggle auto memory on or off, and provides a link to open the auto memory folder. Select any file to open it in your editor.
+
+When you ask Claude to remember something, like "always use pnpm, not npm" or "remember that the API tests require a local Redis instance," Claude saves it to auto memory. To add instructions to CLAUDE.md instead, ask Claude directly, like "add this to CLAUDE.md," or edit the file yourself via `/memory`.
+
+## Troubleshoot memory issues
+
+These are the most common issues with CLAUDE.md and auto memory, along with steps to debug them.
+
+### Claude isn't following my CLAUDE.md
+
+CLAUDE.md is context, not enforcement. Claude reads it and tries to follow it, but there's no guarantee of strict compliance, especially for vague or conflicting instructions.
+
+To debug:
+
+* Run `/memory` to verify your CLAUDE.md files are being loaded. If a file isn't listed, Claude can't see it.
+* Check that the relevant CLAUDE.md is in a location that gets loaded for your session (see [Choose where to put CLAUDE.md files](#choose-where-to-put-claudemd-files)).
+* Make instructions more specific. "Use 2-space indentation" works better than "format code nicely."
+* Look for conflicting instructions across CLAUDE.md files. If two files give different guidance for the same behavior, Claude may pick one arbitrarily.
+
+### I don't know what auto memory saved
+
+Run `/memory` and select the auto memory folder to browse what Claude has saved. Everything is plain markdown you can read, edit, or delete.
+
+### My CLAUDE.md is too large
+
+Files over 200 lines consume more context and may reduce adherence. Move detailed content into separate files referenced with `@path` imports (see [Import additional files](#import-additional-files)), or split your instructions across `.claude/rules/` files.
+
+### Instructions seem lost after `/compact`
+
+CLAUDE.md fully survives compaction. After `/compact`, Claude re-reads your CLAUDE.md from disk and re-injects it fresh into the session. If an instruction disappeared after compaction, it was given only in conversation, not written to CLAUDE.md. Add it to CLAUDE.md to make it persist across sessions.
+
+See [Write effective instructions](#write-effective-instructions) for guidance on size, structure, and specificity.
+
+## Related resources
+
+* [Skills](/en/skills): package repeatable workflows that load on demand
+* [Settings](/en/settings): configure Claude Code behavior with settings files
+* [Manage sessions](/en/sessions): manage context, resume conversations, and run parallel sessions
+* [Subagent memory](/en/sub-agents#enable-persistent-memory): let subagents maintain their own auto memory

```
### https://code.claude.com/docs/en/sandboxing.md

```diff
--- a/https://code.claude.com/docs/en/sandboxing.md
+++ b/https://code.claude.com/docs/en/sandboxing.md
@@ -41,6 +41,8 @@
 * **Default read behavior**: Read access to the entire computer, except certain denied directories
 * **Blocked access**: Cannot modify files outside the current working directory without explicit permission
 * **Configurable**: Define custom allowed and denied paths through settings
+
+You can grant write access to additional paths using `sandbox.filesystem.allowWrite` in your settings. These restrictions are enforced at the OS level (Seatbelt on macOS, bubblewrap on Linux), so they apply to all subprocess commands, including tools like `kubectl`, `terraform`, and `npm`, not just Claude's file tools.
 
 ### Network isolation
 
@@ -113,6 +115,36 @@
 
 Customize sandbox behavior through your `settings.json` file. See [Settings](/en/settings#sandbox-settings) for complete configuration reference.
 
+#### Granting subprocess write access to specific paths
+
+By default, sandboxed commands can only write to the current working directory. If subprocess commands like `kubectl`, `terraform`, or `npm` need to write outside the project directory, use `sandbox.filesystem.allowWrite` to grant access to specific paths:
+
+```json  theme={null}
+{
+  "sandbox": {
+    "enabled": true,
+    "filesystem": {
+      "allowWrite": ["~/.kube", "//tmp/build"]
+    }
+  }
+}
+```
+
+These paths are enforced at the OS level, so all commands running inside the sandbox, including their child processes, respect them. This is the recommended approach when a tool needs write access to a specific location, rather than excluding the tool from the sandbox entirely with `excludedCommands`.
+
+When `allowWrite` (or `denyWrite`/`denyRead`) is defined in multiple [settings scopes](/en/settings#settings-precedence), the arrays are **merged**, meaning paths from every scope are combined, not replaced. For example, if managed settings allow writes to `//opt/company-tools` and a user adds `~/.kube` in their personal settings, both paths are included in the final sandbox configuration. This means users and projects can extend the list without duplicating or overriding paths set by higher-priority scopes.
+
+Path prefixes control how paths are resolved:
+
+| Prefix            | Meaning                                     | Example                                |
+| :---------------- | :------------------------------------------ | :------------------------------------- |
+| `//`              | Absolute path from filesystem root          | `//tmp/build` becomes `/tmp/build`     |
+| `~/`              | Relative to home directory                  | `~/.kube` becomes `$HOME/.kube`        |
+| `/`               | Relative to the settings file's directory   | `/build` becomes `$SETTINGS_DIR/build` |
+| `./` or no prefix | Relative path (resolved by sandbox runtime) | `./output`                             |
+
+You can also deny write or read access using `sandbox.filesystem.denyWrite` and `sandbox.filesystem.denyRead`. These are merged with any paths from `Edit(...)` and `Read(...)` permission rules.
+
 <Tip>
   Not all commands are compatible with sandboxing out of the box. Some notes that may help you make the most out of the sandbox:
 
@@ -191,11 +223,15 @@
 * **Permissions** control which tools Claude Code can use and are evaluated before any tool runs. They apply to all tools: Bash, Read, Edit, WebFetch, MCP, and others.
 * **Sandboxing** provides OS-level enforcement that restricts what Bash commands can access at the filesystem and network level. It applies only to Bash commands and their child processes.
 
-Filesystem and network restrictions are configured through permission rules, not sandbox settings:
-
+Filesystem and network restrictions are configured through both sandbox settings and permission rules:
+
+* Use `sandbox.filesystem.allowWrite` to grant subprocess write access to paths outside the working directory
+* Use `sandbox.filesystem.denyWrite` and `sandbox.filesystem.denyRead` to block subprocess access to specific paths
 * Use `Read` and `Edit` deny rules to block access to specific files or directories
 * Use `WebFetch` allow/deny rules to control domain access
 * Use sandbox `allowedDomains` to control which domains Bash commands can reach
+
+Paths from both `sandbox.filesystem` settings and permission rules are merged together into the final sandbox configuration.
 
 This [repository](https://github.com/anthropics/claude-code/tree/main/examples/settings) includes starter settings configurations for common deployment scenarios, including sandbox-specific examples. Use these as starting points and adjust them to fit your needs.
 

```
### https://code.claude.com/docs/en/interactive-mode.md

```diff
--- a/https://code.claude.com/docs/en/interactive-mode.md
+++ b/https://code.claude.com/docs/en/interactive-mode.md
@@ -86,41 +86,73 @@
 
 ## Built-in commands
 
-Built-in commands are shortcuts for common actions. The table below covers commonly used commands but not all available options. Type `/` in Claude Code to see the full list, or type `/` followed by any letters to filter.
-
-To create your own commands you can invoke with `/`, see [skills](/en/skills).
-
-| Command                   | Purpose                                                                                                                                                                                                                    |
-| :------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
-| `/clear`                  | Clear conversation history                                                                                                                                                                                                 |
-| `/compact [instructions]` | Compact conversation with optional focus instructions                                                                                                                                                                      |
-| `/config`                 | Open the Settings interface (Config tab)                                                                                                                                                                                   |
-| `/context`                | Visualize current context usage as a colored grid                                                                                                                                                                          |
-| `/cost`                   | Show token usage statistics. See [cost tracking guide](/en/costs#using-the-cost-command) for subscription-specific details.                                                                                                |
-| `/debug [description]`    | Troubleshoot the current session by reading the session debug log. Optionally describe the issue                                                                                                                           |
-| `/doctor`                 | Checks the health of your Claude Code installation                                                                                                                                                                         |
-| `/exit`                   | Exit the REPL                                                                                                                                                                                                              |
-| `/export [filename]`      | Export the current conversation to a file or clipboard                                                                                                                                                                     |
-| `/help`                   | Get usage help                                                                                                                                                                                                             |
-| `/init`                   | Initialize project with `CLAUDE.md` guide                                                                                                                                                                                  |
-| `/mcp`                    | Manage MCP server connections and OAuth authentication                                                                                                                                                                     |
-| `/memory`                 | Edit `CLAUDE.md` memory files                                                                                                                                                                                              |
-| `/model`                  | Select or change the AI model. With Opus 4.6, use left/right arrows to [adjust effort level](/en/model-config#adjust-effort-level). The change takes effect immediately without waiting for the current response to finish |
-| `/permissions`            | View or update [permissions](/en/permissions#manage-permissions)                                                                                                                                                           |
-| `/plan`                   | Enter plan mode directly from the prompt                                                                                                                                                                                   |
-| `/rename [name]`          | Rename the current session. Without a name, generates one from conversation history (requires at least one message in the conversation context).                                                                           |
-| `/resume [session]`       | Resume a conversation by ID or name, or open the session picker                                                                                                                                                            |
-| `/rewind`                 | Rewind the conversation and/or code, or summarize from a selected message                                                                                                                                                  |
-| `/stats`                  | Visualize daily usage, session history, streaks, and model preferences                                                                                                                                                     |
-| `/status`                 | Open the Settings interface (Status tab) showing version, model, account, and connectivity                                                                                                                                 |
-| `/statusline`             | Set up Claude Code's status line UI                                                                                                                                                                                        |
-| `/copy`                   | Copy the last response to clipboard. When code blocks are present, shows an interactive picker to select individual code blocks or the full response                                                                       |
-| `/tasks`                  | List and manage background tasks                                                                                                                                                                                           |
-| `/teleport`               | Resume a remote session from claude.ai (subscribers only)                                                                                                                                                                  |
-| `/desktop`                | Hand off the current CLI session to the Claude Code Desktop app (macOS and Windows only)                                                                                                                                   |
-| `/theme`                  | Change the color theme                                                                                                                                                                                                     |
-| `/todos`                  | List current TODO items                                                                                                                                                                                                    |
-| `/usage`                  | For subscription plans only: show plan usage limits and rate limit status                                                                                                                                                  |
+Type `/` in Claude Code to see all available commands, or type `/` followed by any letters to filter. Not all commands are visible to every user. Some depend on your platform, plan, or environment. For example, `/desktop` only appears on macOS and Windows, `/upgrade` and `/privacy-settings` are only available on Pro and Max plans, and `/terminal-setup` is hidden when your terminal natively supports its keybindings.
+
+Claude Code also ships with [bundled skills](/en/skills#bundled-skills) like `/simplify`, `/batch`, and `/debug` that appear alongside built-in commands when you type `/`. To create your own commands, see [skills](/en/skills).
+
+In the table below, `<arg>` indicates a required argument and `[arg]` indicates an optional one.
+
+| Command                   | Purpose                                                                                                                                                                                                                                                                                                                                                            |
+| :------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
+| `/add-dir <path>`         | Add a new working directory to the current session                                                                                                                                                                                                                                                                                                                 |
+| `/agents`                 | Manage [agent](/en/sub-agents) configurations                                                                                                                                                                                                                                                                                                                      |
+| `/chrome`                 | Configure [Claude in Chrome](/en/chrome) settings                                                                                                                                                                                                                                                                                                                  |
+| `/clear`                  | Clear conversation history and free up context. Aliases: `/reset`, `/new`                                                                                                                                                                                                                                                                                          |
+| `/compact [instructions]` | Compact conversation with optional focus instructions                                                                                                                                                                                                                                                                                                              |
+| `/config`                 | Open the [Settings](/en/settings) interface (Config tab). Alias: `/settings`                                                                                                                                                                                                                                                                                       |
+| `/context`                | Visualize current context usage as a colored grid                                                                                                                                                                                                                                                                                                                  |
+| `/copy`                   | Copy the last assistant response to clipboard. When code blocks are present, shows an interactive picker to select individual blocks or the full response                                                                                                                                                                                                          |
+| `/cost`                   | Show token usage statistics. See [cost tracking guide](/en/costs#using-the-cost-command) for subscription-specific details                                                                                                                                                                                                                                         |
+| `/desktop`                | Continue the current session in the Claude Code Desktop app. macOS and Windows only. Alias: `/app`                                                                                                                                                                                                                                                                 |
+| `/diff`                   | Open an interactive diff viewer showing uncommitted changes and per-turn diffs. Use left/right arrows to switch between the current git diff and individual Claude turns, and up/down to browse files                                                                                                                                                              |
+| `/doctor`                 | Diagnose and verify your Claude Code installation and settings                                                                                                                                                                                                                                                                                                     |
+| `/exit`                   | Exit the CLI. Alias: `/quit`                                                                                                                                                                                                                                                                                                                                       |
+| `/export [filename]`      | Export the current conversation as plain text. With a filename, writes directly to that file. Without, opens a dialog to copy to clipboard or save to a file                                                                                                                                                                                                       |
+| `/extra-usage`            | Configure extra usage to keep working when rate limits are hit                                                                                                                                                                                                                                                                                                     |
+| `/fast [on\|off]`         | Toggle [fast mode](/en/fast-mode) on or off                                                                                                                                                                                                                                                                                                                        |
+| `/feedback [report]`      | Submit feedback about Claude Code. Alias: `/bug`                                                                                                                                                                                                                                                                                                                   |
+| `/fork [name]`            | Create a fork of the current conversation at this point                                                                                                                                                                                                                                                                                                            |
+| `/help`                   | Show help and available commands                                                                                                                                                                                                                                                                                                                                   |
+| `/hooks`                  | Manage [hook](/en/hooks) configurations for tool events                                                                                                                                                                                                                                                                                                            |
+| `/ide`                    | Manage IDE integrations and show status                                                                                                                                                                                                                                                                                                                            |
+| `/init`                   | Initialize project with `CLAUDE.md` guide                                                                                                                                                                                                                                                                                                                          |
+| `/insights`               | Generate a report analyzing your Claude Code sessions, including project areas, interaction patterns, and friction points                                                                                                                                                                                                                                          |
+| `/install-github-app`     | Set up the [Claude GitHub Actions](/en/github-actions) app for a repository. Walks you through selecting a repo and configuring the integration                                                                                                                                                                                                                    |
+| `/install-slack-app`      | Install the Claude Slack app. Opens a browser to complete the OAuth flow                                                                                                                                                                                                                                                                                           |
+| `/keybindings`            | Open or create your keybindings configuration file                                                                                                                                                                                                                                                                                                                 |
+| `/login`                  | Sign in to your Anthropic account                                                                                                                                                                                                                                                                                                                                  |
+| `/logout`                 | Sign out from your Anthropic account                                                                                                                                                                                                                                                                                                                               |
+| `/mcp`                    | Manage MCP server connections and OAuth authentication                                                                                                                                                                                                                                                                                                             |
+| `/memory`                 | Edit `CLAUDE.md` memory files, enable or disable [auto-memory](/en/memory#auto-memory), and view auto-memory entries                                                                                                                                                                                                                                               |
+| `/mobile`                 | Show QR code to download the Claude mobile app. Aliases: `/ios`, `/android`                                                                                                                                                                                                                                                                                        |
+| `/model [model]`          | Select or change the AI model. For models that support it, use left/right arrows to [adjust effort level](/en/model-config#adjust-effort-level). The change takes effect immediately without waiting for the current response to finish                                                                                                                            |
+| `/output-style [style]`   | Switch between [output styles](/en/output-styles). **Default** is standard behavior, **Explanatory** adds educational insights about implementation choices and codebase patterns, and **Learning** pauses to ask you to write small code pieces for hands-on practice. You can also [create custom output styles](/en/output-styles#create-a-custom-output-style) |
+| `/passes`                 | Share a free week of Claude Code with friends. Only visible if your account is eligible                                                                                                                                                                                                                                                                            |
+| `/permissions`            | View or update [permissions](/en/permissions#manage-permissions). Alias: `/allowed-tools`                                                                                                                                                                                                                                                                          |
+| `/plan`                   | Enter plan mode directly from the prompt                                                                                                                                                                                                                                                                                                                           |
+| `/plugin`                 | Manage Claude Code [plugins](/en/plugins)                                                                                                                                                                                                                                                                                                                          |
+| `/pr-comments [PR]`       | Fetch and display comments from a GitHub pull request. Automatically detects the PR for the current branch, or pass a PR URL or number. Requires the `gh` CLI                                                                                                                                                                                                      |
+| `/privacy-settings`       | View and update your privacy settings. Only available for Pro and Max plan subscribers                                                                                                                                                                                                                                                                             |
+| `/release-notes`          | View the full changelog, with the most recent version closest to your prompt                                                                                                                                                                                                                                                                                       |
+| `/remote-control`         | Make this session available for [remote control](/en/remote-control) from claude.ai. Alias: `/rc`                                                                                                                                                                                                                                                                  |
+| `/remote-env`             | Configure the default remote environment for [teleport sessions](/en/claude-code-on-the-web#teleport-a-web-session-to-your-terminal)                                                                                                                                                                                                                               |
+| `/rename [name]`          | Rename the current session. Without a name, auto-generates one from conversation history                                                                                                                                                                                                                                                                           |
+| `/resume [session]`       | Resume a conversation by ID or name, or open the session picker. Alias: `/continue`                                                                                                                                                                                                                                                                                |
+| `/review`                 | Review a pull request for code quality, correctness, security, and test coverage. Pass a PR number, or omit to list open PRs. Requires the `gh` CLI                                                                                                                                                                                                                |
+| `/rewind`                 | Rewind the conversation and/or code to a previous point, or summarize from a selected message. See [checkpointing](/en/checkpointing). Alias: `/checkpoint`                                                                                                                                                                                                        |
+| `/sandbox`                | Toggle [sandbox mode](/en/sandboxing). Available on supported platforms only                                                                                                                                                                                                                                                                                       |
+| `/security-review`        | Analyze pending changes on the current branch for security vulnerabilities. Reviews the git diff and identifies risks like injection, auth issues, and data exposure                                                                                                                                                                                               |
+| `/skills`                 | List available [skills](/en/skills)                                                                                                                                                                                                                                                                                                                                |
+| `/stats`                  | Visualize daily usage, session history, streaks, and model preferences                                                                                                                                                                                                                                                                                             |
+| `/status`                 | Open the Settings interface (Status tab) showing version, model, account, and connectivity                                                                                                                                                                                                                                                                         |
+| `/statusline`             | Configure Claude Code's [status line](/en/statusline). Describe what you want, or run without arguments to auto-configure from your shell prompt                                                                                                                                                                                                                   |
+| `/stickers`               | Order Claude Code stickers                                                                                                                                                                                                                                                                                                                                         |
+| `/tasks`                  | List and manage background tasks                                                                                                                                                                                                                                                                                                                                   |
+| `/terminal-setup`         | Configure terminal keybindings for Shift+Enter and other shortcuts. Only visible in terminals that need it, like VS Code, Alacritty, or Warp                                                                                                                                                                                                                       |
+| `/theme`                  | Change the color theme. Includes light and dark variants, colorblind-accessible (daltonized) themes, and ANSI themes that use your terminal's color palette                                                                                                                                                                                                        |
+| `/upgrade`                | Open the upgrade page to switch to a higher plan tier                                                                                                                                                                                                                                                                                                              |
+| `/usage`                  | Show plan usage limits and rate limit status                                                                                                                                                                                                                                                                                                                       |
+| `/vim`                    | Toggle between Vim and Normal editing modes                                                                                                                                                                                                                                                                                                                        |
 
 ### MCP prompts
 

```
### https://code.claude.com/docs/en/overview.md

```diff
--- a/https://code.claude.com/docs/en/overview.md
+++ b/https://code.claude.com/docs/en/overview.md
@@ -156,9 +156,9 @@
   </Accordion>
 
   <Accordion title="Customize with instructions, skills, and hooks" icon="sliders">
-    [`CLAUDE.md`](/en/claude-md) is a markdown file you add to your project root that Claude Code reads at the start of every session. Use it to set coding standards, architecture decisions, preferred libraries, and review checklists.
-
-    Create [custom slash commands](/en/skills) to package repeatable workflows your team can share, like `/review-pr` or `/deploy-staging`.
+    [`CLAUDE.md`](/en/memory) is a markdown file you add to your project root that Claude Code reads at the start of every session. Use it to set coding standards, architecture decisions, preferred libraries, and review checklists. Claude also builds [auto memory](/en/memory#auto-memory) as it works, saving learnings like build commands and debugging insights across sessions without you writing anything.
+
+    Create [custom commands](/en/skills) to package repeatable workflows your team can share, like `/review-pr` or `/deploy-staging`.
 
     [Hooks](/en/hooks) let you run shell commands before or after Claude Code actions, like auto-formatting after every file edit or running lint before a commit.
   </Accordion>
@@ -216,7 +216,8 @@
 Once you've installed Claude Code, these guides help you go deeper.
 
 * [Quickstart](/en/quickstart): walk through your first real task, from exploring a codebase to committing a fix
-* Level up with [best practices](/en/best-practices) and [common workflows](/en/common-workflows)
+* [Store instructions and memories](/en/memory): give Claude persistent instructions with CLAUDE.md files and auto memory
+* [Common workflows](/en/common-workflows) and [best practices](/en/best-practices): patterns for getting the most out of Claude Code
 * [Settings](/en/settings): customize Claude Code for your workflow
 * [Troubleshooting](/en/troubleshooting): solutions for common issues
 * [code.claude.com](https://code.claude.com/): demos, pricing, and product details

```
### https://code.claude.com/docs/en/analytics.md

```diff
--- a/https://code.claude.com/docs/en/analytics.md
+++ b/https://code.claude.com/docs/en/analytics.md
@@ -35,7 +35,7 @@
 You need the Owner role to configure analytics settings. A GitHub admin must install the GitHub app.
 
 <Warning>
-  Contribution metrics are not available for organizations with [Zero Data Retention](/en/data-usage#data-retention) enabled. The analytics dashboard will show usage metrics only.
+  Contribution metrics are not available for organizations with [Zero Data Retention](/en/zero-data-retention) enabled. The analytics dashboard will show usage metrics only.
 </Warning>
 
 <Steps>

```
### https://code.claude.com/docs/en/claude-code-on-the-web.md

```diff
--- a/https://code.claude.com/docs/en/claude-code-on-the-web.md
+++ b/https://code.claude.com/docs/en/claude-code-on-the-web.md
@@ -161,6 +161,23 @@
 
 Enable repository access verification and/or withhold your name from your shared
 sessions by going to Settings > Claude Code > Sharing settings.
+
+## Managing sessions
+
+### Archiving sessions
+
+You can archive sessions to keep your session list organized. Archived sessions are hidden from the default session list but can be viewed by filtering for archived sessions.
+
+To archive a session, hover over the session in the sidebar and click the archive icon.
+
+### Deleting sessions
+
+Deleting a session permanently removes the session and its data. This action cannot be undone. You can delete a session in two ways:
+
+* **From the sidebar**: Filter for archived sessions, then hover over the session you want to delete and click the delete icon
+* **From the session menu**: Open a session, click the dropdown next to the session title, and select **Delete**
+
+You will be asked to confirm before a session is deleted.
 
 ## Cloud environment
 

```
### https://code.claude.com/docs/en/permissions.md

```diff
--- a/https://code.claude.com/docs/en/permissions.md
+++ b/https://code.claude.com/docs/en/permissions.md
@@ -167,20 +167,20 @@
 * `mcp__puppeteer__*` wildcard syntax that also matches all tools from the `puppeteer` server
 * `mcp__puppeteer__puppeteer_navigate` matches the `puppeteer_navigate` tool provided by the `puppeteer` server
 
-### Task (subagents)
-
-Use `Task(AgentName)` rules to control which [subagents](/en/sub-agents) Claude can use:
-
-* `Task(Explore)` matches the Explore subagent
-* `Task(Plan)` matches the Plan subagent
-* `Task(my-custom-agent)` matches a custom subagent named `my-custom-agent`
+### Agent (subagents)
+
+Use `Agent(AgentName)` rules to control which [subagents](/en/sub-agents) Claude can use:
+
+* `Agent(Explore)` matches the Explore subagent
+* `Agent(Plan)` matches the Plan subagent
+* `Agent(my-custom-agent)` matches a custom subagent named `my-custom-agent`
 
 Add these rules to the `deny` array in your settings or use the `--disallowedTools` CLI flag to disable specific agents. To disable the Explore agent:
 
 ```json  theme={null}
 {
   "permissions": {
-    "deny": ["Task(Explore)"]
+    "deny": ["Agent(Explore)"]
   }
 }
 ```

```
### https://code.claude.com/docs/en/sub-agents.md

```diff
--- a/https://code.claude.com/docs/en/sub-agents.md
+++ b/https://code.claude.com/docs/en/sub-agents.md
@@ -251,25 +251,27 @@
 
 #### Restrict which subagents can be spawned
 
-When an agent runs as the main thread with `claude --agent`, it can spawn subagents using the Task tool. To restrict which subagent types it can spawn, use `Task(agent_type)` syntax in the `tools` field:
+When an agent runs as the main thread with `claude --agent`, it can spawn subagents using the Agent tool. To restrict which subagent types it can spawn, use `Agent(agent_type)` syntax in the `tools` field.
+
+<Note>In version 2.1.63, the Task tool was renamed to Agent. Existing `Task(...)` references in settings and agent definitions still work as aliases.</Note>
 
 ```yaml  theme={null}
 ---
 name: coordinator
 description: Coordinates work across specialized agents
-tools: Task(worker, researcher), Read, Bash
+tools: Agent(worker, researcher), Read, Bash
 ---
 ```
 
 This is an allowlist: only the `worker` and `researcher` subagents can be spawned. If the agent tries to spawn any other type, the request fails and the agent sees only the allowed types in its prompt. To block specific agents while allowing all others, use [`permissions.deny`](#disable-specific-subagents) instead.
 
-To allow spawning any subagent without restrictions, use `Task` without parentheses:
+To allow spawning any subagent without restrictions, use `Agent` without parentheses:
 
 ```yaml  theme={null}
-tools: Task, Read, Bash
-```
-
-If `Task` is omitted from the `tools` list entirely, the agent cannot spawn any subagents. This restriction only applies to agents running as the main thread with `claude --agent`. Subagents cannot spawn other subagents, so `Task(agent_type)` has no effect in subagent definitions.
+tools: Agent, Read, Bash
+```
+
+If `Agent` is omitted from the `tools` list entirely, the agent cannot spawn any subagents. This restriction only applies to agents running as the main thread with `claude --agent`. Subagents cannot spawn other subagents, so `Agent(agent_type)` has no effect in subagent definitions.
 
 #### Permission modes
 
@@ -396,12 +398,12 @@
 
 #### Disable specific subagents
 
-You can prevent Claude from using specific subagents by adding them to the `deny` array in your [settings](/en/settings#permission-settings). Use the format `Task(subagent-name)` where `subagent-name` matches the subagent's name field.
+You can prevent Claude from using specific subagents by adding them to the `deny` array in your [settings](/en/settings#permission-settings). Use the format `Agent(subagent-name)` where `subagent-name` matches the subagent's name field.
 
 ```json  theme={null}
 {
   "permissions": {
-    "deny": ["Task(Explore)", "Task(my-custom-agent)"]
+    "deny": ["Agent(Explore)", "Agent(my-custom-agent)"]
   }
 }
 ```
@@ -409,7 +411,7 @@
 This works for both built-in and custom subagents. You can also use the `--disallowedTools` CLI flag:
 
 ```bash  theme={null}
-claude --disallowedTools "Task(Explore)"
+claude --disallowedTools "Agent(Explore)"
 ```
 
 See [Permissions documentation](/en/permissions#tool-specific-permission-rules) for more details on permission rules.

```
### https://code.claude.com/docs/en/remote-control.md

```diff
--- a/https://code.claude.com/docs/en/remote-control.md
+++ b/https://code.claude.com/docs/en/remote-control.md
@@ -7,7 +7,7 @@
 > Continue a local Claude Code session from your phone, tablet, or any browser using Remote Control. Works with claude.ai/code and the Claude mobile app.
 
 <Note>
-  Remote Control is available as a research preview on Max plans and will be rolling out to Pro plans soon. It is not available on Team or Enterprise plans.
+  Remote Control is available as a research preview on Max and Pro plans. It is not available on Team or Enterprise plans.
 </Note>
 
 Remote Control connects [claude.ai/code](https://claude.ai/code) or the Claude app for [iOS](https://apps.apple.com/us/app/claude-by-anthropic/id6473753684) and [Android](https://play.google.com/store/apps/details?id=com.anthropic.claude) to a Claude Code session running on your machine. Start a task at your desk, then pick it up from your phone on the couch or a browser on another computer.

```
### https://code.claude.com/docs/en/cli-reference.md

```diff
--- a/https://code.claude.com/docs/en/cli-reference.md
+++ b/https://code.claude.com/docs/en/cli-reference.md
@@ -45,7 +45,7 @@
 | `--continue`, `-c`                     | Load the most recent conversation in the current directory                                                                                                                                                | `claude --continue`                                                                                |
 | `--dangerously-skip-permissions`       | Skip all permission prompts (use with caution)                                                                                                                                                            | `claude --dangerously-skip-permissions`                                                            |
 | `--debug`                              | Enable debug mode with optional category filtering (for example, `"api,hooks"` or `"!statsig,!file"`)                                                                                                     | `claude --debug "api,mcp"`                                                                         |
-| `--disable-slash-commands`             | Disable all skills and slash commands for this session                                                                                                                                                    | `claude --disable-slash-commands`                                                                  |
+| `--disable-slash-commands`             | Disable all skills and commands for this session                                                                                                                                                          | `claude --disable-slash-commands`                                                                  |
 | `--disallowedTools`                    | Tools that are removed from the model's context and cannot be used                                                                                                                                        | `"Bash(git log *)" "Bash(git diff *)" "Edit"`                                                      |
 | `--fallback-model`                     | Enable automatic fallback to specified model when default model is overloaded (print mode only)                                                                                                           | `claude -p --fallback-model sonnet "query"`                                                        |
 | `--fork-session`                       | When resuming, create a new session ID instead of reusing the original (use with `--resume` or `--continue`)                                                                                              | `claude --resume abc123 --fork-session`                                                            |
@@ -92,16 +92,16 @@
 
 The `--agents` flag accepts a JSON object that defines one or more custom subagents. Each subagent requires a unique name (as the key) and a definition object with the following fields:
 
-| Field             | Required | Description                                                                                                                                                                                                        |
-| :---------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
-| `description`     | Yes      | Natural language description of when the subagent should be invoked                                                                                                                                                |
-| `prompt`          | Yes      | The system prompt that guides the subagent's behavior                                                                                                                                                              |
-| `tools`           | No       | Array of specific tools the subagent can use, for example `["Read", "Edit", "Bash"]`. If omitted, inherits all tools. Supports [`Task(agent_type)`](/en/sub-agents#restrict-which-subagents-can-be-spawned) syntax |
-| `disallowedTools` | No       | Array of tool names to explicitly deny for this subagent                                                                                                                                                           |
-| `model`           | No       | Model alias to use: `sonnet`, `opus`, `haiku`, or `inherit`. If omitted, defaults to `inherit`                                                                                                                     |
-| `skills`          | No       | Array of [skill](/en/skills) names to preload into the subagent's context                                                                                                                                          |
-| `mcpServers`      | No       | Array of [MCP servers](/en/mcp) for this subagent. Each entry is a server name string or a `{name: config}` object                                                                                                 |
-| `maxTurns`        | No       | Maximum number of agentic turns before the subagent stops                                                                                                                                                          |
+| Field             | Required | Description                                                                                                                                                                                                         |
+| :---------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
+| `description`     | Yes      | Natural language description of when the subagent should be invoked                                                                                                                                                 |
+| `prompt`          | Yes      | The system prompt that guides the subagent's behavior                                                                                                                                                               |
+| `tools`           | No       | Array of specific tools the subagent can use, for example `["Read", "Edit", "Bash"]`. If omitted, inherits all tools. Supports [`Agent(agent_type)`](/en/sub-agents#restrict-which-subagents-can-be-spawned) syntax |
+| `disallowedTools` | No       | Array of tool names to explicitly deny for this subagent                                                                                                                                                            |
+| `model`           | No       | Model alias to use: `sonnet`, `opus`, `haiku`, or `inherit`. If omitted, defaults to `inherit`                                                                                                                      |
+| `skills`          | No       | Array of [skill](/en/skills) names to preload into the subagent's context                                                                                                                                           |
+| `mcpServers`      | No       | Array of [MCP servers](/en/mcp) for this subagent. Each entry is a server name string or a `{name: config}` object                                                                                                  |
+| `maxTurns`        | No       | Maximum number of agentic turns before the subagent stops                                                                                                                                                           |
 
 Example:
 

```
### https://code.claude.com/docs/en/settings.md

```diff
--- a/https://code.claude.com/docs/en/settings.md
+++ b/https://code.claude.com/docs/en/settings.md
@@ -153,6 +153,8 @@
 | `hooks`                           | Configure custom commands to run at lifecycle events. See [hooks documentation](/en/hooks) for format                                                                                                                                                                                     | See [hooks](/en/hooks)                                                  |
 | `disableAllHooks`                 | Disable all [hooks](/en/hooks) and any custom [status line](/en/statusline)                                                                                                                                                                                                               | `true`                                                                  |
 | `allowManagedHooksOnly`           | (Managed settings only) Prevent loading of user, project, and plugin hooks. Only allows managed hooks and SDK hooks. See [Hook configuration](#hook-configuration)                                                                                                                        | `true`                                                                  |
+| `allowedHttpHookUrls`             | Allowlist of URL patterns that HTTP hooks may target. Supports `*` as a wildcard. When set, hooks with non-matching URLs are blocked. Undefined = no restriction, empty array = block all HTTP hooks. Arrays merge across settings sources. See [Hook configuration](#hook-configuration) | `["https://hooks.example.com/*"]`                                       |
+| `httpHookAllowedEnvVars`          | Allowlist of environment variable names HTTP hooks may interpolate into headers. When set, each hook's effective `allowedEnvVars` is the intersection with this list. Undefined = no restriction. Arrays merge across settings sources. See [Hook configuration](#hook-configuration)     | `["MY_TOKEN", "HOOK_SECRET"]`                                           |
 | `allowManagedPermissionRulesOnly` | (Managed settings only) Prevent user and project settings from defining `allow`, `ask`, or `deny` permission rules. Only rules in managed settings apply. See [Managed-only settings](/en/permissions#managed-only-settings)                                                              | `true`                                                                  |
 | `allowManagedMcpServersOnly`      | (Managed settings only) Only `allowedMcpServers` from managed settings are respected. `deniedMcpServers` still merges from all sources. Users can still add MCP servers, but only the admin-defined allowlist applies. See [Managed MCP configuration](/en/mcp#managed-mcp-configuration) | `true`                                                                  |
 | `model`                           | Override the default model to use for Claude Code                                                                                                                                                                                                                                         | `"claude-sonnet-4-6"`                                                   |
@@ -183,6 +185,7 @@
 | `spinnerTipsOverride`             | Override spinner tips with custom strings. `tips`: array of tip strings. `excludeDefault`: if `true`, only show custom tips; if `false` or absent, custom tips are merged with built-in tips                                                                                              | `{ "excludeDefault": true, "tips": ["Use our internal tool X"] }`       |
 | `terminalProgressBarEnabled`      | Enable the terminal progress bar that shows progress in supported terminals like Windows Terminal and iTerm2 (default: `true`)                                                                                                                                                            | `false`                                                                 |
 | `prefersReducedMotion`            | Reduce or disable UI animations (spinners, shimmer, flash effects) for accessibility                                                                                                                                                                                                      | `true`                                                                  |
+| `fastModePerSessionOptIn`         | When `true`, fast mode does not persist across sessions. Each session starts with fast mode off, requiring users to enable it with `/fast`. The user's fast mode preference is still saved. See [Require per-session opt-in](/en/fast-mode#require-per-session-opt-in)                    | `true`                                                                  |
 | `teammateMode`                    | How [agent team](/en/agent-teams) teammates display: `auto` (picks split panes in tmux or iTerm2, in-process otherwise), `in-process`, or `tmux`. See [set up agent teams](/en/agent-teams#set-up-agent-teams)                                                                            | `"in-process"`                                                          |
 
 ### Permission settings
@@ -209,13 +212,11 @@
 | `Read(./.env)`                 | Matches reading the `.env` file          |
 | `WebFetch(domain:example.com)` | Matches fetch requests to example.com    |
 
-For the complete rule syntax reference, including wildcard behavior, tool-specific patterns for Read, Edit, WebFetch, MCP, and Task rules, and security limitations of Bash patterns, see [Permission rule syntax](/en/permissions#permission-rule-syntax).
+For the complete rule syntax reference, including wildcard behavior, tool-specific patterns for Read, Edit, WebFetch, MCP, and Agent rules, and security limitations of Bash patterns, see [Permission rule syntax](/en/permissions#permission-rule-syntax).
 
 ### Sandbox settings
 
 Configure advanced sandboxing behavior. Sandboxing isolates bash commands from your filesystem and network. See [Sandboxing](/en/sandboxing) for details.
-
-**Filesystem and network restrictions** are configured via Read, Edit, and WebFetch permission rules, not via these sandbox settings.
 
 | Keys                              | Description                                                                                                                                                                                                                                                                                                                       | Example                         |
 | :-------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------ |
@@ -223,6 +224,9 @@
 | `autoAllowBashIfSandboxed`        | Auto-approve bash commands when sandboxed. Default: true                                                                                                                                                                                                                                                                          | `true`                          |
 | `excludedCommands`                | Commands that should run outside of the sandbox                                                                                                                                                                                                                                                                                   | `["git", "docker"]`             |
 | `allowUnsandboxedCommands`        | Allow commands to run outside the sandbox via the `dangerouslyDisableSandbox` parameter. When set to `false`, the `dangerouslyDisableSandbox` escape hatch is completely disabled and all commands must run sandboxed (or be in `excludedCommands`). Useful for enterprise policies that require strict sandboxing. Default: true | `false`                         |
+| `filesystem.allowWrite`           | Additional paths where sandboxed commands can write. Arrays are merged across all settings scopes: user, project, and managed paths are combined, not replaced. Also merged with paths from `Edit(...)` allow permission rules. See [path prefixes](#sandbox-path-prefixes) below.                                                | `["//tmp/build", "~/.kube"]`    |
+| `filesystem.denyWrite`            | Paths where sandboxed commands cannot write. Arrays are merged across all settings scopes. Also merged with paths from `Edit(...)` deny permission rules.                                                                                                                                                                         | `["//etc", "//usr/local/bin"]`  |
+| `filesystem.denyRead`             | Paths where sandboxed commands cannot read. Arrays are merged across all settings scopes. Also merged with paths from `Read(...)` deny permission rules.                                                                                                                                                                          | `["~/.aws/credentials"]`        |
 | `network.allowUnixSockets`        | Unix socket paths accessible in sandbox (for SSH agents, etc.)                                                                                                                                                                                                                                                                    | `["~/.ssh/agent-socket"]`       |
 | `network.allowAllUnixSockets`     | Allow all Unix socket connections in sandbox. Default: false                                                                                                                                                                                                                                                                      | `true`                          |
 | `network.allowLocalBinding`       | Allow binding to localhost ports (macOS only). Default: false                                                                                                                                                                                                                                                                     | `true`                          |
@@ -232,6 +236,17 @@
 | `network.socksProxyPort`          | SOCKS5 proxy port used if you wish to bring your own proxy. If not specified, Claude will run its own proxy.                                                                                                                                                                                                                      | `8081`                          |
 | `enableWeakerNestedSandbox`       | Enable weaker sandbox for unprivileged Docker environments (Linux and WSL2 only). **Reduces security.** Default: false                                                                                                                                                                                                            | `true`                          |
 
+#### Sandbox path prefixes
+
+Paths in `filesystem.allowWrite`, `filesystem.denyWrite`, and `filesystem.denyRead` support these prefixes:
+
+| Prefix            | Meaning                                     | Example                                |
+| :---------------- | :------------------------------------------ | :------------------------------------- |
+| `//`              | Absolute path from filesystem root          | `//tmp/build` becomes `/tmp/build`     |
+| `~/`              | Relative to home directory                  | `~/.kube` becomes `$HOME/.kube`        |
+| `/`               | Relative to the settings file's directory   | `/build` becomes `$SETTINGS_DIR/build` |
+| `./` or no prefix | Relative path (resolved by sandbox runtime) | `./output`                             |
+
 **Configuration example:**
 
 ```json  theme={null}
@@ -240,6 +255,10 @@
     "enabled": true,
     "autoAllowBashIfSandboxed": true,
     "excludedCommands": ["docker"],
+    "filesystem": {
+      "allowWrite": ["//tmp/build", "~/.kube"],
+      "denyRead": ["~/.aws/credentials"]
+    },
     "network": {
       "allowedDomains": ["github.com", "*.npmjs.org", "registry.yarnpkg.com"],
       "allowUnixSockets": [
@@ -247,22 +266,14 @@
       ],
       "allowLocalBinding": true
     }
-  },
-  "permissions": {
-    "deny": [
-      "Read(.envrc)",
-      "Read(~/.aws/**)"
-    ]
   }
 }
 ```
 
-**Filesystem and network restrictions** use standard permission rules:
-
-* Use `Read` deny rules to block Claude from reading specific files or directories
-* Use `Edit` allow rules to let Claude write to directories beyond the current working directory
-* Use `Edit` deny rules to block writes to specific paths
-* Use `WebFetch` allow/deny rules to control which network domains Claude can access
+**Filesystem and network restrictions** can be configured in two ways that are merged together:
+
+* **`sandbox.filesystem` settings** (shown above): Control paths at the OS-level sandbox boundary. These restrictions apply to all subprocess commands (e.g., `kubectl`, `terraform`, `npm`), not just Claude's file tools.
+* **Permission rules**: Use `Edit` allow/deny rules to control Claude's file tool access, `Read` deny rules to block reads, and `WebFetch` allow/deny rules to control network domains. Paths from these rules are also merged into the sandbox configuration.
 
 ### Attribution settings
 
@@ -342,18 +353,30 @@
 
 ### Hook configuration
 
-**Managed settings only**: Controls which hooks are allowed to run. This setting can only be configured in [managed settings](#settings-files) and provides administrators with strict control over hook execution.
+These settings control which hooks are allowed to run and what HTTP hooks can access. The `allowManagedHooksOnly` setting can only be configured in [managed settings](#settings-files). The URL and env var allowlists can be set at any settings level and merge across sources.
 
 **Behavior when `allowManagedHooksOnly` is `true`:**
 
 * Managed hooks and SDK hooks are loaded
 * User hooks, project hooks, and plugin hooks are blocked
 
-**Configuration:**
-
-```json  theme={null}
-{
-  "allowManagedHooksOnly": true
+**Restrict HTTP hook URLs:**
+
+Limit which URLs HTTP hooks can target. Supports `*` as a wildcard for matching. When the array is defined, HTTP hooks targeting non-matching URLs are silently blocked.
+
+```json  theme={null}
+{
+  "allowedHttpHookUrls": ["https://hooks.example.com/*", "http://localhost:*"]
+}
+```
+
+**Restrict HTTP hook environment variables:**
+
+Limit which environment variable names HTTP hooks can interpolate into header values. Each hook's effective `allowedEnvVars` is the intersection of its own list and this setting.
+
+```json  theme={null}
+{
+  "httpHookAllowedEnvVars": ["MY_TOKEN", "HOOK_SECRET"]
 }
 ```
 
@@ -381,6 +404,10 @@
 This hierarchy ensures that organizational policies are always enforced while still allowing teams and individuals to customize their experience.
 
 For example, if your user settings allow `Bash(npm run *)` but a project's shared settings deny it, the project setting takes precedence and the command is blocked.
+
+<Note>
+  **Array settings merge across scopes.** When the same array-valued setting (such as `sandbox.filesystem.allowWrite` or `permissions.allow`) appears in multiple scopes, the arrays are **concatenated and deduplicated**, not replaced. This means lower-priority scopes can add entries without overriding those set by higher-priority scopes, and vice versa. For example, if managed settings set `allowWrite` to `["//opt/company-tools"]` and a user adds `["~/.kube"]`, both paths are included in the final configuration.
+</Note>
 
 ### Verify active settings
 
@@ -828,6 +855,7 @@
 | `DISABLE_PROMPT_CACHING_OPUS`                  | Set to `1` to disable prompt caching for Opus models                                                                                                                                                                                                                                                                                                                                                                                                                                                  |     |
 | `DISABLE_PROMPT_CACHING_SONNET`                | Set to `1` to disable prompt caching for Sonnet models                                                                                                                                                                                                                                                                                                                                                                                                                                                |     |
 | `DISABLE_TELEMETRY`                            | Set to `1` to opt out of Statsig telemetry (note that Statsig events do not include user data like code, file paths, or bash commands)                                                                                                                                                                                                                                                                                                                                                                |     |
+| `ENABLE_CLAUDEAI_MCP_SERVERS`                  | Set to `false` to disable [claude.ai MCP servers](/en/mcp#use-mcp-servers-from-claudeai) in Claude Code. Enabled by default for logged-in users                                                                                                                                                                                                                                                                                                                                                       |     |
 | `ENABLE_TOOL_SEARCH`                           | Controls [MCP tool search](/en/mcp#scale-with-mcp-tool-search). Values: `auto` (default, enables at 10% context), `auto:N` (custom threshold, e.g., `auto:5` for 5%), `true` (always on), `false` (disabled)                                                                                                                                                                                                                                                                                          |     |
 | `FORCE_AUTOUPDATE_PLUGINS`                     | Set to `true` to force plugin auto-updates even when the main auto-updater is disabled via `DISABLE_AUTOUPDATER`                                                                                                                                                                                                                                                                                                                                                                                      |     |
 | `HTTP_PROXY`                                   | Specify HTTP proxy server for network connections                                                                                                                                                                                                                                                                                                                                                                                                                                                     |     |
@@ -866,7 +894,7 @@
 | **NotebookEdit**    | Modifies Jupyter notebook cells                                                                                                                                                                                                                                                                                                                                             | Yes                 |
 | **Read**            | Reads the contents of files                                                                                                                                                                                                                                                                                                                                                 | No                  |
 | **Skill**           | Executes a [skill](/en/skills#control-who-invokes-a-skill) within the main conversation                                                                                                                                                                                                                                                                                     | Yes                 |
-| **Task**            | Runs a sub-agent to handle complex, multi-step tasks                                                                                                                                                                                                                                                                                                                        | No                  |
+| **Agent**           | Runs a sub-agent to handle complex, multi-step tasks                                                                                                                                                                                                                                                                                                                        | No                  |
 | **TaskCreate**      | Creates a new task in the task list                                                                                                                                                                                                                                                                                                                                         | No                  |
 | **TaskGet**         | Retrieves full details for a specific task                                                                                                                                                                                                                                                                                                                                  | No                  |
 | **TaskList**        | Lists all tasks with their current status                                                                                                                                                                                                                                                                                                                                   | No                  |

```
### https://code.claude.com/docs/en/legal-and-compliance.md

```diff
--- a/https://code.claude.com/docs/en/legal-and-compliance.md
+++ b/https://code.claude.com/docs/en/legal-and-compliance.md
@@ -23,7 +23,7 @@
 
 ### Healthcare compliance (BAA)
 
-If a customer has a Business Associate Agreement (BAA) with us, and wants to use Claude Code, the BAA will automatically extend to cover Claude Code if the customer has executed a BAA and has Zero Data Retention (ZDR) activated. The BAA will be applicable to that customer's API traffic flowing through Claude Code.
+If a customer has a Business Associate Agreement (BAA) with us, and wants to use Claude Code, the BAA will automatically extend to cover Claude Code if the customer has executed a BAA and has [Zero Data Retention (ZDR)](/en/zero-data-retention) activated. The BAA will be applicable to that customer's API traffic flowing through Claude Code. ZDR is enabled on a per-organization basis, so each organization must have ZDR enabled separately to be covered under the BAA.
 
 ## Usage policy
 

```
### https://code.claude.com/docs/en/hooks.md

```diff
--- a/https://code.claude.com/docs/en/hooks.md
+++ b/https://code.claude.com/docs/en/hooks.md
@@ -4,17 +4,17 @@
 
 # Hooks reference
 
-> Reference for Claude Code hook events, configuration schema, JSON input/output formats, exit codes, async hooks, prompt hooks, and MCP tool hooks.
+> Reference for Claude Code hook events, configuration schema, JSON input/output formats, exit codes, async hooks, HTTP hooks, prompt hooks, and MCP tool hooks.
 
 <Tip>
   For a quickstart guide with examples, see [Automate workflows with hooks](/en/hooks-guide).
 </Tip>
 
-Hooks are user-defined shell commands or LLM prompts that execute automatically at specific points in Claude Code's lifecycle. Use this reference to look up event schemas, configuration options, JSON input/output formats, and advanced features like async hooks and MCP tool hooks. If you're setting up hooks for the first time, start with the [guide](/en/hooks-guide) instead.
+Hooks are user-defined shell commands, HTTP endpoints, or LLM prompts that execute automatically at specific points in Claude Code's lifecycle. Use this reference to look up event schemas, configuration options, JSON input/output formats, and advanced features like async hooks, HTTP hooks, and MCP tool hooks. If you're setting up hooks for the first time, start with the [guide](/en/hooks-guide) instead.
 
 ## Hook lifecycle
 
-Hooks fire at specific points during a Claude Code session. When an event fires and a matcher matches, Claude Code passes JSON context about the event to your hook handler. For command hooks, this arrives on stdin. Your handler can then inspect the input, take action, and optionally return a decision. Some events fire once per session, while others fire repeatedly inside the agentic loop:
+Hooks fire at specific points during a Claude Code session. When an event fires and a matcher matches, Claude Code passes JSON context about the event to your hook handler. For command hooks, input arrives on stdin. For HTTP hooks, it arrives as the POST request body. Your handler can then inspect the input, take action, and optionally return a decision. Some events fire once per session, while others fire repeatedly inside the agentic loop:
 
 <div style={{maxWidth: "500px", margin: "0 auto"}}>
   <Frame>
@@ -139,7 +139,7 @@
 See [How a hook resolves](#how-a-hook-resolves) above for a complete walkthrough with an annotated example.
 
 <Note>
-  This page uses specific terms for each level: **hook event** for the lifecycle point, **matcher group** for the filter, and **hook handler** for the shell command, prompt, or agent that runs. "Hook" on its own refers to the general feature.
+  This page uses specific terms for each level: **hook event** for the lifecycle point, **matcher group** for the filter, and **hook handler** for the shell command, HTTP endpoint, prompt, or agent that runs. "Hook" on its own refers to the general feature.
 </Note>
 
 ### Hook locations
@@ -243,9 +243,10 @@
 
 ### Hook handler fields
 
-Each object in the inner `hooks` array is a hook handler: the shell command, LLM prompt, or agent that runs when the matcher matches. There are three types:
+Each object in the inner `hooks` array is a hook handler: the shell command, HTTP endpoint, LLM prompt, or agent that runs when the matcher matches. There are four types:
 
 * **[Command hooks](#command-hook-fields)** (`type: "command"`): run a shell command. Your script receives the event's [JSON input](#hook-input-and-output) on stdin and communicates results back through exit codes and stdout.
+* **[HTTP hooks](#http-hook-fields)** (`type: "http"`): send the event's JSON input as an HTTP POST request to a URL. The endpoint communicates results back through the response body using the same [JSON output format](#json-output) as command hooks.
 * **[Prompt hooks](#prompt-and-agent-hook-fields)** (`type: "prompt"`): send a prompt to a Claude model for single-turn evaluation. The model returns a yes/no decision as JSON. See [Prompt-based hooks](#prompt-based-hooks).
 * **[Agent hooks](#prompt-and-agent-hook-fields)** (`type: "agent"`): spawn a subagent that can use tools like Read, Grep, and Glob to verify conditions before returning a decision. See [Agent-based hooks](#agent-based-hooks).
 
@@ -255,7 +256,7 @@
 
 | Field           | Required | Description                                                                                                                                   |
 | :-------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
-| `type`          | yes      | `"command"`, `"prompt"`, or `"agent"`                                                                                                         |
+| `type`          | yes      | `"command"`, `"http"`, `"prompt"`, or `"agent"`                                                                                               |
 | `timeout`       | no       | Seconds before canceling. Defaults: 600 for command, 30 for prompt, 60 for agent                                                              |
 | `statusMessage` | no       | Custom spinner message displayed while the hook runs                                                                                          |
 | `once`          | no       | If `true`, runs only once per session then is removed. Skills only, not agents. See [Hooks in skills and agents](#hooks-in-skills-and-agents) |
@@ -269,6 +270,49 @@
 | `command` | yes      | Shell command to execute                                                                                            |
 | `async`   | no       | If `true`, runs in the background without blocking. See [Run hooks in the background](#run-hooks-in-the-background) |
 
+#### HTTP hook fields
+
+In addition to the [common fields](#common-fields), HTTP hooks accept these fields:
+
+| Field            | Required | Description                                                                                                                                                                                      |
+| :--------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
+| `url`            | yes      | URL to send the POST request to                                                                                                                                                                  |
+| `headers`        | no       | Additional HTTP headers as key-value pairs. Values support environment variable interpolation using `$VAR_NAME` or `${VAR_NAME}` syntax. Only variables listed in `allowedEnvVars` are resolved  |
+| `allowedEnvVars` | no       | List of environment variable names that may be interpolated into header values. References to unlisted variables are replaced with empty strings. Required for any env var interpolation to work |
+
+Claude Code sends the hook's [JSON input](#hook-input-and-output) as the POST request body with `Content-Type: application/json`. The response body uses the same [JSON output format](#json-output) as command hooks.
+
+Error handling differs from command hooks: non-2xx responses, connection failures, and timeouts all produce non-blocking errors that allow execution to continue. To block a tool call or deny a permission, return a 2xx response with a JSON body containing `decision: "block"` or a `hookSpecificOutput` with `permissionDecision: "deny"`.
+
+This example sends `PreToolUse` events to a local validation service, authenticating with a token from the `MY_TOKEN` environment variable:
+
+```json  theme={null}
+{
+  "hooks": {
+    "PreToolUse": [
+      {
+        "matcher": "Bash",
+        "hooks": [
+          {
+            "type": "http",
+            "url": "http://localhost:8080/hooks/pre-tool-use",
+            "timeout": 30,
+            "headers": {
+              "Authorization": "Bearer $MY_TOKEN"
+            },
+            "allowedEnvVars": ["MY_TOKEN"]
+          }
+        ]
+      }
+    ]
+  }
+}
+```
+
+<Note>
+  HTTP hooks must be configured by editing settings JSON directly. The `/hooks` interactive menu only supports adding command hooks.
+</Note>
+
 #### Prompt and agent hook fields
 
 In addition to the [common fields](#common-fields), prompt and agent hooks accept these fields:
@@ -278,7 +322,7 @@
 | `prompt` | yes      | Prompt text to send to the model. Use `$ARGUMENTS` as a placeholder for the hook input JSON |
 | `model`  | no       | Model to use for evaluation. Defaults to a fast model                                       |
 
-All matching hooks run in parallel, and identical handlers are deduplicated automatically. Handlers run in the current directory with Claude Code's environment. The `$CLAUDE_CODE_REMOTE` environment variable is set to `"true"` in remote web environments and not set in the local CLI.
+All matching hooks run in parallel, and identical handlers are deduplicated automatically. Command hooks are deduplicated by command string, and HTTP hooks are deduplicated by URL. Handlers run in the current directory with Claude Code's environment. The `$CLAUDE_CODE_REMOTE` environment variable is set to `"true"` in remote web environments and not set in the local CLI.
 
 ### Reference scripts by path
 
@@ -387,11 +431,11 @@
 
 ## Hook input and output
 
-Hooks receive JSON data via stdin and communicate results through exit codes, stdout, and stderr. This section covers fields and behavior common to all events. Each event's section under [Hook events](#hook-events) includes its specific input schema and decision control options.
+Command hooks receive JSON data via stdin and communicate results through exit codes, stdout, and stderr. HTTP hooks receive the same JSON as the POST request body and communicate results through the HTTP response body. This section covers fields and behavior common to all events. Each event's section under [Hook events](#hook-events) includes its specific input schema and decision control options.
 
 ### Common input fields
 
-All hook events receive these fields via stdin as JSON, in addition to event-specific fields documented in each [hook event](#hook-events) section:
+All hook events receive these fields as JSON, in addition to event-specific fields documented in each [hook event](#hook-events) section. For command hooks, this JSON arrives via stdin. For HTTP hooks, it arrives as the POST request body.
 
 | Field             | Description                                                                                                                                |
 | :---------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
@@ -468,6 +512,18 @@
 | `WorktreeCreate`     | Yes        | Any non-zero exit code causes worktree creation to fail                       |
 | `WorktreeRemove`     | No         | Failures are logged in debug mode only                                        |
 
+### HTTP response handling
+
+HTTP hooks use HTTP status codes and response bodies instead of exit codes and stdout:
+
+* **2xx with an empty body**: success, equivalent to exit code 0 with no output
+* **2xx with a plain text body**: success, the text is added as context
+* **2xx with a JSON body**: success, parsed using the same [JSON output](#json-output) schema as command hooks
+* **Non-2xx status**: non-blocking error, execution continues
+* **Connection failure or timeout**: non-blocking error, execution continues
+
+Unlike command hooks, HTTP hooks cannot signal a blocking error through status codes alone. To block a tool call or deny a permission, return a 2xx response with a JSON body containing the appropriate decision fields.
+
 ### JSON output
 
 Exit codes let you allow or block, but JSON output gives you finer-grained control. Instead of exiting with code 2 to block, exit 0 and print a JSON object to stdout. Claude Code reads specific fields from that JSON to control behavior, including [decision control](#decision-control) for blocking, allowing, or escalating to the user.
@@ -712,7 +768,7 @@
 
 ### PreToolUse
 
-Runs after Claude creates tool parameters and before processing the tool call. Matches on tool name: `Bash`, `Edit`, `Write`, `Read`, `Glob`, `Grep`, `Task`, `WebFetch`, `WebSearch`, and any [MCP tool names](#match-mcp-tools).
+Runs after Claude creates tool parameters and before processing the tool call. Matches on tool name: `Bash`, `Edit`, `Write`, `Read`, `Glob`, `Grep`, `Agent`, `WebFetch`, `WebSearch`, and any [MCP tool names](#match-mcp-tools).
 
 Use [PreToolUse decision control](#pretooluse-decision-control) to allow, deny, or ask for permission to use the tool.
 
@@ -802,7 +858,7 @@
 | `allowed_domains` | array  | `["docs.example.com"]`         | Optional: only include results from these domains |
 | `blocked_domains` | array  | `["spam.example.com"]`         | Optional: exclude results from these domains      |
 
-##### Task
+##### Agent
 
 Spawns a [subagent](/en/sub-agents).
 
@@ -1057,7 +1113,7 @@
 
 ### SubagentStart
 
-Runs when a Claude Code subagent is spawned via the Task tool. Supports matchers to filter by agent type name (built-in agents like `Bash`, `Explore`, `Plan`, or custom agent names from `.claude/agents/`).
+Runs when a Claude Code subagent is spawned via the Agent tool. Supports matchers to filter by agent type name (built-in agents like `Bash`, `Explore`, `Plan`, or custom agent names from `.claude/agents/`).
 
 #### SubagentStart input
 
@@ -1461,9 +1517,9 @@
 
 ## Prompt-based hooks
 
-In addition to Bash command hooks (`type: "command"`), Claude Code supports prompt-based hooks (`type: "prompt"`) that use an LLM to evaluate whether to allow or block an action, and agent hooks (`type: "agent"`) that spawn an agentic verifier with tool access. Not all events support every hook type.
-
-Events that support all three hook types (`command`, `prompt`, and `agent`):
+In addition to command and HTTP hooks, Claude Code supports prompt-based hooks (`type: "prompt"`) that use an LLM to evaluate whether to allow or block an action, and agent hooks (`type: "agent"`) that spawn an agentic verifier with tool access. Not all events support every hook type.
+
+Events that support all four hook types (`command`, `http`, `prompt`, and `agent`):
 
 * `PermissionRequest`
 * `PostToolUse`
@@ -1711,10 +1767,10 @@
 
 ### Disclaimer
 
-Hooks run with your system user's full permissions.
+Command hooks run with your system user's full permissions.
 
 <Warning>
-  Hooks execute shell commands with your full user permissions. They can modify, delete, or access any files your user account can access. Review and test all hook commands before adding them to your configuration.
+  Command hooks execute shell commands with your full user permissions. They can modify, delete, or access any files your user account can access. Review and test all hook commands before adding them to your configuration.
 </Warning>
 
 ### Security best practices

```
### https://code.claude.com/docs/en/fast-mode.md

```diff
--- a/https://code.claude.com/docs/en/fast-mode.md
+++ b/https://code.claude.com/docs/en/fast-mode.md
@@ -21,7 +21,7 @@
 * Available to all Claude Code users on subscription plans (Pro/Max/Team/Enterprise) and Claude Console.
 * For Claude Code users on subscription plans (Pro/Max/Team/Enterprise), fast mode is available via extra usage only and not included in the subscription rate limits.
 
-This page covers how to [toggle fast mode](#toggle-fast-mode), its [cost tradeoff](#understand-the-cost-tradeoff), [when to use it](#decide-when-to-use-fast-mode), [requirements](#requirements), and [rate limit behavior](#handle-rate-limits).
+This page covers how to [toggle fast mode](#toggle-fast-mode), its [cost tradeoff](#understand-the-cost-tradeoff), [when to use it](#decide-when-to-use-fast-mode), [requirements](#requirements), [per-session opt-in](#require-per-session-opt-in), and [rate limit behavior](#handle-rate-limits).
 
 ## Toggle fast mode
 
@@ -30,7 +30,9 @@
 * Type `/fast` and press Tab to toggle on or off
 * Set `"fastMode": true` in your [user settings file](/en/settings)
 
-Fast mode persists across sessions. For the best cost efficiency, enable fast mode at the start of a session rather than switching mid-conversation. See [understand the cost tradeoff](#understand-the-cost-tradeoff) for details.
+By default, fast mode persists across sessions. Administrators can configure fast mode to reset each session. See [require per-session opt-in](#require-per-session-opt-in) for details.
+
+For the best cost efficiency, enable fast mode at the start of a session rather than switching mid-conversation. See [understand the cost tradeoff](#understand-the-cost-tradeoff) for details.
 
 When you enable fast mode:
 
@@ -105,6 +107,18 @@
 
 Another option to disable fast mode entirely is to set `CLAUDE_CODE_DISABLE_FAST_MODE=1`. See [Environment variables](/en/settings#environment-variables).
 
+### Require per-session opt-in
+
+By default, fast mode persists across sessions: if a user enables fast mode, it stays on in future sessions. Administrators on [Teams](https://claude.com/pricing#team-&-enterprise) or [Enterprise](https://anthropic.com/contact-sales) plans can prevent this by setting `fastModePerSessionOptIn` to `true` in [managed settings](/en/settings#settings-files) or [server-managed settings](/en/server-managed-settings). This causes each session to start with fast mode off, requiring users to explicitly enable it with `/fast`.
+
+```json  theme={null}
+{
+  "fastModePerSessionOptIn": true
+}
+```
+
+This is useful for controlling costs in organizations where users run multiple concurrent sessions. Users can still enable fast mode with `/fast` when they need speed, but it resets at the start of each new session. The user's fast mode preference is still saved, so removing this setting restores the default persistent behavior.
+
 ## Handle rate limits
 
 Fast mode has separate rate limits from standard Opus 4.6. When you hit the fast mode rate limit or run out of extra usage credits:

```
### https://code.claude.com/docs/en/quickstart.md

```diff
--- a/https://code.claude.com/docs/en/quickstart.md
+++ b/https://code.claude.com/docs/en/quickstart.md
@@ -29,19 +29,19 @@
   <Tab title="Native Install (Recommended)">
     **macOS, Linux, WSL:**
 
-    ```bash theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null}
+    ```bash  theme={null}
     curl -fsSL https://claude.ai/install.sh | bash
     ```
 
     **Windows PowerShell:**
 
-    ```powershell theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null}
+    ```powershell  theme={null}
     irm https://claude.ai/install.ps1 | iex
     ```
 
     **Windows CMD:**
 
-    ```batch theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null}
+    ```batch  theme={null}
     curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
     ```
 
@@ -53,7 +53,7 @@
   </Tab>
 
   <Tab title="Homebrew">
-    ```bash theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null}
+    ```bash  theme={null}
     brew install --cask claude-code
     ```
 
@@ -63,7 +63,7 @@
   </Tab>
 
   <Tab title="WinGet">
-    ```powershell theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null}
+    ```powershell  theme={null}
     winget install Anthropic.ClaudeCode
     ```
 

```
### https://code.claude.com/docs/en/hooks-guide.md

```diff
--- a/https://code.claude.com/docs/en/hooks-guide.md
+++ b/https://code.claude.com/docs/en/hooks-guide.md
@@ -313,7 +313,11 @@
 | `PreCompact`         | Before context compaction                                                                                   |
 | `SessionEnd`         | When a session terminates                                                                                   |
 
-Each hook has a `type` that determines how it runs. Most hooks use `"type": "command"`, which runs a shell command. Two other options use a Claude model to make decisions: `"type": "prompt"` for single-turn evaluation and `"type": "agent"` for multi-turn verification with tool access. See [Prompt-based hooks](#prompt-based-hooks) and [Agent-based hooks](#agent-based-hooks) for details.
+Each hook has a `type` that determines how it runs. Most hooks use `"type": "command"`, which runs a shell command. Three other types are available:
+
+* `"type": "http"`: POST event data to a URL. See [HTTP hooks](#http-hooks).
+* `"type": "prompt"`: single-turn LLM evaluation. See [Prompt-based hooks](#prompt-based-hooks).
+* `"type": "agent"`: multi-turn verification with tool access. See [Agent-based hooks](#agent-based-hooks).
 
 ### Read input and return output
 
@@ -576,11 +580,50 @@
 
 For full configuration options, see [Agent-based hooks](/en/hooks#agent-based-hooks) in the reference.
 
+## HTTP hooks
+
+Use `type: "http"` hooks to POST event data to an HTTP endpoint instead of running a shell command. The endpoint receives the same JSON that a command hook would receive on stdin, and returns results through the HTTP response body using the same JSON format.
+
+HTTP hooks are useful when you want a web server, cloud function, or external service to handle hook logic: for example, a shared audit service that logs tool use events across a team.
+
+This example posts every tool use to a local logging service:
+
+```json  theme={null}
+{
+  "hooks": {
+    "PostToolUse": [
+      {
+        "hooks": [
+          {
+            "type": "http",
+            "url": "http://localhost:8080/hooks/tool-use",
+            "headers": {
+              "Authorization": "Bearer $MY_TOKEN"
+            },
+            "allowedEnvVars": ["MY_TOKEN"]
+          }
+        ]
+      }
+    ]
+  }
+}
+```
+
+The endpoint should return a JSON response body using the same [output format](/en/hooks#json-output) as command hooks. To block a tool call, return a 2xx response with the appropriate `hookSpecificOutput` fields. HTTP status codes alone cannot block actions.
+
+Header values support environment variable interpolation using `$VAR_NAME` or `${VAR_NAME}` syntax. Only variables listed in the `allowedEnvVars` array are resolved; all other `$VAR` references remain empty.
+
+<Note>
+  HTTP hooks must be configured by editing your settings JSON directly. The `/hooks` interactive menu only supports adding command hooks.
+</Note>
+
+For full configuration options and response handling, see [HTTP hooks](/en/hooks#http-hook-fields) in the reference.
+
 ## Limitations and troubleshooting
 
 ### Limitations
 
-* Hooks communicate through stdout, stderr, and exit codes only. They cannot trigger slash commands or tool calls directly.
+* Command hooks communicate through stdout, stderr, and exit codes only. They cannot trigger commands or tool calls directly. HTTP hooks communicate through the response body instead.
 * Hook timeout is 10 minutes by default, configurable per hook with the `timeout` field (in seconds).
 * `PostToolUse` hooks cannot undo actions since the tool has already executed.
 * `PermissionRequest` hooks do not fire in [non-interactive mode](/en/headless) (`-p`). Use `PreToolUse` hooks for automated permission decisions.

```
### https://code.claude.com/docs/en/features-overview.md

```diff
--- a/https://code.claude.com/docs/en/features-overview.md
+++ b/https://code.claude.com/docs/en/features-overview.md
@@ -26,7 +26,7 @@
 * **[Hooks](/en/hooks)** run outside the loop entirely as deterministic scripts
 * **[Plugins](/en/plugins)** and **[marketplaces](/en/plugin-marketplaces)** package and distribute these features
 
-[Skills](/en/skills) are the most flexible extension. A skill is a markdown file containing knowledge, workflows, or instructions. You can invoke skills with a slash command like `/deploy`, or Claude can load them automatically when relevant. Skills can run in your current conversation or in an isolated context via subagents.
+[Skills](/en/skills) are the most flexible extension. A skill is a markdown file containing knowledge, workflows, or instructions. You can invoke skills with a command like `/deploy`, or Claude can load them automatically when relevant. Skills can run in your current conversation or in an isolated context via subagents.
 
 ## Match features to your goal
 
@@ -81,7 +81,23 @@
 
     **Put it in a skill** if it's reference material Claude needs sometimes (API docs, style guides) or a workflow you trigger with `/<name>` (deploy, review, release).
 
-    **Rule of thumb:** Keep CLAUDE.md under \~500 lines. If it's growing, move reference content to skills.
+    **Rule of thumb:** Keep CLAUDE.md under 200 lines. If it's growing, move reference content to skills or split into [`.claude/rules/`](/en/memory#organize-rules-with-clauderules) files.
+  </Tab>
+
+  <Tab title="CLAUDE.md vs Rules vs Skills">
+    All three store instructions, but they load differently:
+
+    | Aspect       | CLAUDE.md                           | `.claude/rules/`                                   | Skill                                    |
+    | ------------ | ----------------------------------- | -------------------------------------------------- | ---------------------------------------- |
+    | **Loads**    | Every session                       | Every session, or when matching files are opened   | On demand, when invoked or relevant      |
+    | **Scope**    | Whole project                       | Can be scoped to file paths                        | Task-specific                            |
+    | **Best for** | Core conventions and build commands | Language-specific or directory-specific guidelines | Reference material, repeatable workflows |
+
+    **Use CLAUDE.md** for instructions every session needs: build commands, test conventions, project architecture.
+
+    **Use rules** to keep CLAUDE.md focused. Rules with [`paths` frontmatter](/en/memory#path-specific-rules) only load when Claude works with matching files, saving context.
+
+    **Use skills** for content Claude only needs sometimes, like API documentation or a deployment checklist you trigger with `/<name>`.
   </Tab>
 
   <Tab title="Subagent vs Agent team">
@@ -132,7 +148,7 @@
 
 Features can be defined at multiple levels: user-wide, per-project, via plugins, or through managed policies. You can also nest CLAUDE.md files in subdirectories or place skills in specific packages of a monorepo. When the same feature exists at multiple levels, here's how they layer:
 
-* **CLAUDE.md files** are additive: all levels contribute content to Claude's context simultaneously. Files from your working directory and above load at launch; subdirectories load as you work in them. When instructions conflict, Claude uses judgment to reconcile them, with more specific instructions typically taking precedence. See [how Claude looks up memories](/en/memory#how-claude-looks-up-memories).
+* **CLAUDE.md files** are additive: all levels contribute content to Claude's context simultaneously. Files from your working directory and above load at launch; subdirectories load as you work in them. When instructions conflict, Claude uses judgment to reconcile them, with more specific instructions typically taking precedence. See [how CLAUDE.md files load](/en/memory#how-claudemd-files-load).
 * **Skills and subagents** override by name: when the same name exists at multiple levels, one definition wins based on priority (managed > user > project for skills; managed > CLI flag > project > user > plugin for subagents). Plugin skills are [namespaced](/en/plugins#add-skills-to-your-plugin) to avoid conflicts. See [skill discovery](/en/skills#where-skills-live) and [subagent scope](/en/sub-agents#choose-the-subagent-scope).
 * **MCP servers** override by name: local > project > user. See [MCP scope](/en/mcp#scope-hierarchy-and-precedence).
 * **Hooks** merge: all registered hooks fire for their matching events regardless of source. See [hooks](/en/hooks).
@@ -180,13 +196,13 @@
 
     **What loads:** Full content of all CLAUDE.md files (managed, user, and project levels).
 
-    **Inheritance:** Claude reads CLAUDE.md files from your working directory up to the root, and discovers nested ones in subdirectories as it accesses those files. See [How Claude looks up memories](/en/memory#how-claude-looks-up-memories) for details.
+    **Inheritance:** Claude reads CLAUDE.md files from your working directory up to the root, and discovers nested ones in subdirectories as it accesses those files. See [How CLAUDE.md files load](/en/memory#how-claudemd-files-load) for details.
 
     <Tip>Keep CLAUDE.md under \~500 lines. Move reference material to skills, which load on-demand.</Tip>
   </Tab>
 
   <Tab title="Skills">
-    Skills are extra capabilities in Claude's toolkit. They can be reference material (like an API style guide) or invocable workflows you trigger with `/<name>` (like `/deploy`). Some are built-in; you can also create your own. Claude uses skills when appropriate, or you can invoke one directly.
+    Skills are extra capabilities in Claude's toolkit. They can be reference material (like an API style guide) or invocable workflows you trigger with `/<name>` (like `/deploy`). Claude Code ships with [bundled skills](/en/skills#bundled-skills) like `/simplify`, `/batch`, and `/debug` that work out of the box. You can also create your own. Claude uses skills when appropriate, or you can invoke one directly.
 
     **When:** Depends on the skill's configuration. By default, descriptions load at session start and full content loads when used. For user-only skills (`disable-model-invocation: true`), nothing loads until you invoke them.
 

```
### https://code.claude.com/docs/en/skills.md

```diff
--- a/https://code.claude.com/docs/en/skills.md
+++ b/https://code.claude.com/docs/en/skills.md
@@ -4,17 +4,31 @@
 
 # Extend Claude with skills
 
-> Create, manage, and share skills to extend Claude's capabilities in Claude Code. Includes custom slash commands.
+> Create, manage, and share skills to extend Claude's capabilities in Claude Code. Includes custom commands and bundled skills.
 
 Skills extend what Claude can do. Create a `SKILL.md` file with instructions, and Claude adds it to its toolkit. Claude uses skills when relevant, or you can invoke one directly with `/skill-name`.
 
 <Note>
   For built-in commands like `/help` and `/compact`, see [interactive mode](/en/interactive-mode#built-in-commands).
 
-  **Custom slash commands have been merged into skills.** A file at `.claude/commands/review.md` and a skill at `.claude/skills/review/SKILL.md` both create `/review` and work the same way. Your existing `.claude/commands/` files keep working. Skills add optional features: a directory for supporting files, frontmatter to [control whether you or Claude invokes them](#control-who-invokes-a-skill), and the ability for Claude to load them automatically when relevant.
+  **Custom commands have been merged into skills.** A file at `.claude/commands/review.md` and a skill at `.claude/skills/review/SKILL.md` both create `/review` and work the same way. Your existing `.claude/commands/` files keep working. Skills add optional features: a directory for supporting files, frontmatter to [control whether you or Claude invokes them](#control-who-invokes-a-skill), and the ability for Claude to load them automatically when relevant.
 </Note>
 
 Claude Code skills follow the [Agent Skills](https://agentskills.io) open standard, which works across multiple AI tools. Claude Code extends the standard with additional features like [invocation control](#control-who-invokes-a-skill), [subagent execution](#run-skills-in-a-subagent), and [dynamic context injection](#inject-dynamic-context).
+
+## Bundled skills
+
+Bundled skills ship with Claude Code and are available in every session. Unlike [built-in commands](/en/interactive-mode#built-in-commands), which execute fixed logic directly, bundled skills are prompt-based: they give Claude a detailed playbook and let it orchestrate the work using its tools. This means bundled skills can spawn parallel agents, read files, and adapt to your codebase.
+
+You invoke bundled skills the same way as any other skill: type `/` followed by the skill name.
+
+* **`/simplify`**: reviews your recently changed files for code reuse, quality, and efficiency issues, then fixes them. Run it after implementing a feature or bug fix to clean up your work. It spawns three review agents in parallel (code reuse, code quality, efficiency), aggregates their findings, and applies fixes. Pass optional text to focus on specific concerns: `/simplify focus on memory efficiency`.
+
+* **`/batch <instruction>`**: orchestrates large-scale changes across a codebase in parallel. Provide a description of the change and `/batch` researches the codebase, decomposes the work into 5 to 30 independent units, and presents a plan for your approval. Once approved, it spawns one background agent per unit, each in an isolated [git worktree](/en/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees). Each agent implements its unit, runs tests, and opens a pull request. Requires a git repository. Example: `/batch migrate src/ from Solid to React`.
+
+* **`/debug [description]`**: troubleshoots your current Claude Code session by reading the session debug log. Optionally describe the issue to focus the analysis.
+
+Claude Code also includes a bundled developer platform skill that activates automatically when your code imports the Anthropic SDK. You don't need to invoke it manually.
 
 ## Getting started
 
@@ -112,7 +126,7 @@
 Skills defined in `.claude/skills/` within directories added via `--add-dir` are loaded automatically and picked up by live change detection, so you can edit them during a session without restarting.
 
 <Note>
-  CLAUDE.md files from `--add-dir` directories are not loaded by default. To load them, set `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1`. See [Load memory from additional directories](/en/memory#load-memory-from-additional-directories).
+  CLAUDE.md files from `--add-dir` directories are not loaded by default. To load them, set `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1`. See [Load from additional directories](/en/memory#load-from-additional-directories).
 </Note>
 
 ## Configure skills

```
### https://code.claude.com/docs/en/mcp.md

```diff
--- a/https://code.claude.com/docs/en/mcp.md
+++ b/https://code.claude.com/docs/en/mcp.md
@@ -614,7 +614,8 @@
 
   * Authentication tokens are stored securely and refreshed automatically
   * Use "Clear authentication" in the `/mcp` menu to revoke access
-  * If your browser doesn't open automatically, copy the provided URL
+  * If your browser doesn't open automatically, copy the provided URL and open it manually
+  * If the browser redirect fails with a connection error after authenticating, paste the full callback URL from your browser's address bar into the URL prompt that appears in Claude Code
   * OAuth authentication works with HTTP servers
 </Tip>
 
@@ -772,6 +773,12 @@
     Claude.ai servers appear in the list with indicators showing they come from Claude.ai.
   </Step>
 </Steps>
+
+To disable claude.ai MCP servers in Claude Code, set the `ENABLE_CLAUDEAI_MCP_SERVERS` environment variable to `false`:
+
+```bash  theme={null}
+ENABLE_CLAUDEAI_MCP_SERVERS=false claude
+```
 
 ## Use Claude Code as an MCP server
 

```
### https://code.claude.com/docs/en/data-usage.md

```diff
--- a/https://code.claude.com/docs/en/data-usage.md
+++ b/https://code.claude.com/docs/en/data-usage.md
@@ -42,8 +42,10 @@
 **Commercial users (Team, Enterprise, and API)**:
 
 * Standard: 30-day retention period
-* Zero data retention: Available with appropriately configured API keys - Claude Code will not retain chat transcripts on servers
+* [Zero data retention](/en/zero-data-retention): available for Claude Code on Claude for Enterprise. ZDR is enabled on a per-organization basis; each new organization must have ZDR enabled separately by your account team
 * Local caching: Claude Code clients may store sessions locally for up to 30 days to enable session resumption (configurable)
+
+You can delete individual Claude Code on the web sessions at any time. Deleting a session permanently removes the session's event data. For instructions on how to delete sessions, see [Managing sessions](/en/claude-code-on-the-web#managing-sessions).
 
 Learn more about data retention practices in our [Privacy Center](https://privacy.anthropic.com/).
 

```
