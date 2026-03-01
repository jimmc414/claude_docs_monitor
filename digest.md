# Claude Docs Change Digest

*Generated: 2026-02-27 05:34 UTC*

### Executive Summary
This update expands adaptive reasoning controls to Sonnet 4.6 (previously only Opus 4.6), adds two new environment variables for disabling fast mode and adaptive thinking, and clarifies the official plugin submission process with direct form links.

### New Features
- **Plugin submission forms**: Official Anthropic marketplace now has in-app submission forms at `claude.ai/settings/plugins/submit` and `platform.claude.com/plugins/submit`

### Flag & API Changes
- `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1`: New env var to disable adaptive reasoning on Opus 4.6 and Sonnet 4.6, reverting to fixed `MAX_THINKING_TOKENS` budget
- `CLAUDE_CODE_DISABLE_FAST_MODE=1`: New env var to disable fast mode entirely (alternative to UI-based disabling)

### Notable Clarifications
- `MAX_THINKING_TOKENS` is now documented as ignored on **Sonnet 4.6** in addition to Opus 4.6 (adaptive reasoning controls both); `MAX_THINKING_TOKENS=0` still fully disables thinking on any model
- Plugin distribution docs updated to distinguish between submitting to the official marketplace vs. hosting your own

### Action Items
- [ ] If you rely on `MAX_THINKING_TOKENS` to control thinking depth on Sonnet 4.6, set `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1` to restore that behavior
- [ ] If your enterprise policy requires disabling fast mode, add `CLAUDE_CODE_DISABLE_FAST_MODE=1` to your environment config rather than relying solely on UI settings
- [ ] Plugin authors: use the official submission forms instead of reaching out separately
