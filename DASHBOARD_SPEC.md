# Living Dashboard for Claude Docs Monitor — Design Spec

## Problem

Claude Docs Monitor accumulates a rich intelligence asset over time in the
`change_events` table: every classified change carries a category
(`feature`/`breaking`/`flag_change`/`clarification`/`deprecation`/`bugfix`),
severity (`high`/`medium`/`low`), summary, action item, and the underlying
diff. After several months of runs this becomes a useful corpus for answering
questions like "what just broke in hooks?", "what's the rate of breaking
changes?", "which pages are churning?", "what do I need to act on this week?".

Today none of that is reachable visually. The pipeline produces:

| Output            | Lifecycle                                       | UX             |
| ----------------- | ----------------------------------------------- | -------------- |
| `report.md/html`  | Overwritten every run; only the latest diff set | Static doc     |
| `digest.md/html`  | Overwritten every run; only the latest LLM analysis | Static doc |
| `history.md/html` | Appended; chronological list of runs            | Wall of text   |
| `snapshots.db`    | Append-only SQLite — the actual moat            | CLI/MCP only   |

The static HTML files are read top-to-bottom. There's no filtering, no
drill-in, no cross-run synthesis, no "what's new since I last looked".
Cross-run intelligence exists only behind `query` (CLI) or the MCP server
(reachable only from inside a Claude conversation). For an everyday human
viewer the UX gap is large.

## Proposal

Add a single-file, self-contained interactive dashboard, written each run by
a new `_generate_dashboard_html()` function. It joins `change_events` with
`page_snapshots` for diff content, embeds the result as a JSON payload, and
ships ~700–900 lines of vanilla JS/HTML/CSS that turn that payload into an
exploratory interface. No build step, no server, no extra dependencies.

`digest.md`/`digest.html` keep their roles as the LLM-curated narrative. The
new file (`dashboard.html`) is what auto-opens in the browser after `check`,
replacing the static `digest.html` as the default landing page. A
`--legacy-digest` flag keeps the old behavior for users who prefer it.

## Visual reference

A working preview rendered from the 2026-05-15 run sits at
`data-claude/dashboard-preview.html`. Open it for the interaction model and
visual density. The spec below describes that artifact in detail and the
gaps between it and the production version.

## Information architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│ HEADER                                                                   │
│  • brand · "latest run: <ts>" · count strip (events/pages/runs/unread)   │
├─────────────────────────────────────────────────────────────────────────┤
│ FILTER RAIL (sticky)                                                     │
│  • Category chips with live counts (breaking, feature, flag, clar.…)     │
│  • Severity chips (high, med, low)                                       │
│  • Toggles: "unread only", "has action"                                  │
│  • Free-text search (focus with /)                                       │
├─────────────────────────────────────────────────────────────────────────┤
│ TIMELINE STRIP                                                           │
│  • Weekly histogram across the full tracked range                        │
│  • Stacked segments by category                                          │
│  • Click a bar → filter to that week (toggle)                            │
├──────────────────────────────────────┬──────────────────────────────────┤
│ MAIN: event feed                     │ SIDE RAIL                        │
│  • Grouped by run timestamp          │  • Pages-by-churn (sortable)     │
│  • Each event = one card             │    name · sparks · lifetime n    │
│  • Severity bar (4px) left edge      │    click → filter feed to page   │
│  • Pills: category + severity        │  • Action items (top 8)          │
│  • Summary + optional "Action" block │    click → opens drawer          │
│  • Click card → opens drawer         │                                  │
│  • Unread dot, "latest" badge        │                                  │
├──────────────────────────────────────┴──────────────────────────────────┤
│ DETAIL DRAWER (right slide-in, 720px max-width, overlay)                 │
│  • Breadcrumb · close (esc)                                              │
│  • Title · category/severity/id pills                                    │
│  • Details (rich)                                                        │
│  • Action required (highlighted)                                         │
│  • Diff excerpt (color-coded unified diff)                               │
│  • Provenance (run ts, page, change_events.id)                           │
└─────────────────────────────────────────────────────────────────────────┘
```

## Interactions

| Trigger                          | Effect                                                              |
| -------------------------------- | ------------------------------------------------------------------- |
| Click category chip              | Toggle that category in the filter set (AND across groups, OR within) |
| Click severity chip              | Toggle severity in the filter set                                   |
| Type in search                   | Live filter on summary/details/page/action (case-insensitive)       |
| Toggle "unread only"             | Hide events already viewed in any prior session                     |
| Toggle "has action"              | Show only events with an `action_required` field                    |
| Click timeline bar               | Filter to that week (re-click clears)                               |
| Click page row                   | Filter feed to that page (re-click clears)                          |
| Click event card                 | Open detail drawer + mark read + write URL hash                     |
| Drawer close button / Esc / backdrop | Close drawer + clear hash                                       |
| Page-sort link                   | Toggle between `changes` / `name` / `recent`                        |

### Keyboard

| Key       | Action                                          |
| --------- | ----------------------------------------------- |
| `/`       | Focus search                                    |
| `j` / `k` | Next / previous event (within current filter)  |
| `x`       | Toggle read status of selected event            |
| `u`       | Toggle "unread only"                            |
| `Esc`     | Close drawer (or blur search if focused)        |

### URL state

- `#event=<id>` opens the drawer for that event on load. Sharing a link to a
  specific change is a one-step copy/paste.
- Filter state is intentionally **not** persisted to the URL. Filters are
  ephemeral; sharing should always land you on the canonical event view, not
  someone else's filter combination.

### Persistent state (localStorage)

- `docsmon.read` — `number[]` of event IDs the user has opened in this
  browser. Drives the "unread" dot and the unread counter.

## Visual design

- **Density first.** Card padding is 10/14px, not 24/32px. The header is one
  row, not a hero. Filter chips are 12px line-height, not 16px.
- **Type system.** Sans for prose (`-apple-system, BlinkMacSystemFont, "Segoe
  UI", Inter, Roboto, sans-serif`). Mono for timestamps, page paths, IDs,
  diff blocks, and small numeric counts (`ui-monospace, "SF Mono",
  "JetBrains Mono", Consolas, monospace`).
- **Color is semantic.** It only communicates:
  - **Severity** — left edge bar on each event card. Red / amber / lime.
  - **Category** — small dot in the chip, soft background pill on the card
    badge. Blue/red/violet/cyan/pink/green for the six categories.
  - **Diff** — green/red bands with bar markers, blue for hunk headers.
- **No gradients, no shadows except the drawer.** The page should feel like
  a tool (think `htop`, `jq`, `gh`), not a marketing page.
- **Light mode only at v1.** Dark mode is straightforward to add (the design
  has only ~20 color tokens) but not gating.

## Data payload

The dashboard is rendered server-side once per run; all data is inlined as a
`PAYLOAD` JSON literal in the HTML. No fetches.

```ts
type Payload = {
  latest_run: string;              // ISO UTC of the most recent run
  runs: Array<{
    ts: string;
    label: string;                 // short "May 15"
    changed: number;
    added: number;
    removed: number;
  }>;
  events: Array<{
    id: number;                    // change_events.id
    run: string;                   // change_events.run_timestamp
    page: string;                  // change_events.page_name
    category: "breaking" | "feature" | "flag_change"
            | "clarification" | "deprecation" | "bugfix";
    severity: "high" | "medium" | "low";
    summary: string;               // one line
    details: string;               // 1-3 paragraphs
    action?: string;               // change_events.action_required
    diff?: string;                 // unified diff excerpt (top 3 hunks max)
  }>;
};
const PAGES_ROLLUP: Array<{
  page: string;
  total: number;                   // lifetime change count
  breakdown: Category[];           // category per change, chronological
}>;
```

**Diff size policy.** Inline up to ~5 KB of diff per event (typically the
first 3 hunks). For events with larger diffs, truncate with a `…` marker
and a link to `data-claude/pages/<page>` for the latest snapshot. This
keeps the dashboard HTML under ~500 KB even with thousands of events.

**Truncation budget.** When the change_events table grows past ~2,000 events,
shift to: latest 90 days inlined in full, older events stored as summary-only
records (no diff). The dashboard adds a "load older diffs" button that fetches
nothing — it just notes the threshold so users know to fall back to CLI
`query` or MCP `get_diff` for archaeology.

## Implementation plan

### Phase 1 — generator

1. New function `_generate_dashboard_html(report_dir: Path)` in
   `claude_docs_monitor.py`.
2. New helper `_collect_dashboard_payload(conn) -> dict` that:
   - reads `change_events` JOIN `page_snapshots` for diffs
   - rolls up `PAGES_ROLLUP` from a `GROUP BY page_name`
   - assembles the `runs` array from `DISTINCT run_timestamp`
3. Embed the HTML template as a triple-quoted string with a single
   `__PAYLOAD__` placeholder; serialize the dict with
   `json.dumps(payload, separators=(",",":"))` and substitute.
4. Write to `<report_dir>/dashboard.html`.
5. In `cmd_digest`, call `_generate_dashboard_html()` after the existing
   `_generate_digest_html()` call. Change `_open_in_browser` target to
   `dashboard.html` unless `--legacy-digest` is passed.

### Phase 2 — backfill quality

The dashboard's value compounds with the size and quality of `change_events`.
Phase 2 tightens the classification step:

- Add `severity_reason` and `affected_versions` to the JSON schema in
  `_run_structured_classification()` so the dashboard can show why something
  is high severity.
- Run `backfill` on the existing history so the dashboard isn't sparse on
  day one. The script already supports this (`python claude_docs_monitor.py
  backfill`); just include it in the rollout checklist.

### Phase 3 — optional power features (post-v1)

- "Compare two runs" mode: pick any two runs, see only events that differ.
- Subscriptions: chip preset saved in localStorage ("I care about hooks +
  mcp + agent-sdk"). Persists across sessions.
- Stability heatmap: by-page churn rate vs. last 30 days. Reveals what's
  "settling down" vs. "still in flux".
- Export filtered view to markdown.

## Non-goals (v1)

- **Mobile.** Two-column layout collapses on narrow viewports, but the
  primary target is desktop. No phone-first design work.
- **Authentication / multi-user.** This is a local single-file artifact.
  "Read state" is per-browser, not per-user.
- **Server-side anything.** Stays a static file. If anything requires a
  server (full-text search across diffs at scale, for example), it's out
  of scope for v1.
- **Replacing `digest.md`.** The LLM narrative remains the canonical
  "what should I read first" artifact. Dashboard is for exploration, not
  curation.

## Acceptance criteria

- [ ] `data-claude/dashboard.html` written on every successful `digest` run.
- [ ] Total HTML size under 500 KB for the first year of accumulated data
      (≈2,000 events with 5 KB diff cap each), under 2 MB through year three.
- [ ] Page loads in under 200 ms on a mid-range laptop, with no network
      requests after initial HTML load.
- [ ] Works in Chrome, Firefox, Safari current and current-1. No build step.
- [ ] All filters compose correctly: e.g. `category=breaking + severity=high
      + page=hooks.md + week=W19` returns exactly the right intersection.
- [ ] Keyboard shortcuts as specified, with `Esc` always reachable.
- [ ] URL hash `#event=<id>` deep-links work on cold load.
- [ ] Empty states for "no events match" and "no events at all" are
      designed (not a blank canvas).
- [ ] No emojis, no gradients, no decorative imagery.

## Open questions

1. **Diff drawer width — fixed 720px or responsive 50/50 split?** Preview
   uses a fixed-width overlay. A 50/50 split lets you keep the feed visible
   while inspecting; the overlay puts the diff front and center. Lean
   overlay for v1 (simpler, more focused).

2. **Should weekly timeline bars be clickable to filter, or only
   hover-to-inspect?** Preview makes them clickable. Risk: easy to filter
   to an empty week by accident. Mitigation: empty bars are visually
   distinct (lighter color, no segments) and the "Clear filters" affordance
   is always visible when any filter is active.

3. **Where does the "Action items" rollup live — sidebar (current) or its
   own first-row module above the feed?** Sidebar keeps it adjacent to the
   feed; a top-row module would be more prominent. Lean sidebar for v1;
   promote to top row if users repeatedly miss it.

4. **Two filter behaviors are possible: "filter narrows the feed" (current)
   vs. "filter brings to top, gray out rest".** Preview narrows. The
   alternative preserves orientation across filter changes. Lean
   narrowing — graying-out is more code and less information-dense.
