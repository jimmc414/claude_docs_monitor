# Documentation Feature Comparison Rubric

Rubric Version: 1.0

This rubric scores the *entire cached documentation corpus* for Claude, Gemini, and Codex from a user + power-user perspective.

## Scoring Model

- Total score: **100 points**
- Feature scoring levels:
  - **Explicit evidence**: 100% of feature points
  - **Strong implied evidence**: 60% of feature points
  - **No evidence**: 0% of feature points
- Evidence sources:
  - Page filenames in `data-*/pages/*.md`
  - Page content text across the full corpus
- Tie-break order:
  1. Power-User Workflow Depth
  2. Security and Governance
  3. Automation and Integrations

## Categories and Weights

| Category | Weight |
|---|---:|
| Core Onboarding and Command Surface | 15 |
| Power-User Workflow Depth | 20 |
| Automation and Integrations | 18 |
| Extensibility and Customization | 15 |
| Security and Governance | 17 |
| Enterprise and Operations | 10 |
| Documentation Reliability | 5 |

## Feature Checklist by Category

### 1) Core Onboarding and Command Surface (15)

- Onboarding, installation, and first-run setup (4)
- CLI command/reference depth (4)
- Workflow playbooks, examples, and guides (4)
- Troubleshooting and FAQ coverage (3)

### 2) Power-User Workflow Depth (20)

- Planning, delegation, and multi-agent orchestration (5)
- Memory, session state, and long-running continuity (5)
- Code review and PR/MR execution workflows (5)
- Headless and non-interactive operation modes (5)

### 3) Automation and Integrations (18)

- CI/CD and scheduled automation (6)
- Service integrations and partner ecosystem (6)
- MCP and external tooling connectivity (6)

### 4) Extensibility and Customization (15)

- Skills, plugins, and extension ecosystem (5)
- Custom prompts, command macros, and rule files (5)
- Deep configuration, model controls, and keybindings (5)

### 5) Security and Governance (17)

- Permission models and sandbox controls (6)
- Security, safety, and threat-model depth (6)
- Governance, compliance, and policy guidance (5)

### 6) Enterprise and Operations (10)

- Enterprise admin setup and managed controls (4)
- Pricing, quota, and cost transparency (3)
- Telemetry, analytics, and monitoring (3)

### 7) Documentation Reliability (5)

Reliability is computed from corpus integrity signals:

- URL-to-filename collisions (penalty)
- Missing expected files after URL mapping (penalty)
- Staleness for very old caches (penalty)

A tool with no reliability penalties receives full 5 points.

## Scope Rules

- Evaluate **tool documentation only** (Claude, Gemini, Codex docs corpora).
- Exclude docs-monitor internals from scoring.
- Evaluate the full cached corpus, not recent diffs.
- Use explicit evidence first; implied evidence is only used when explicit evidence is absent.

## Output Contract

Each run should emit:

- `report.md`: human-readable ranking, rationale, matrix, benefits/drawbacks
- `report.json`: structured scoring/evidence output
- `latest_scores.csv`: compact rank/score export

All outputs should include the rubric version so future runs remain comparable.
