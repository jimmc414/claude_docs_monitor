# Maximizing `/loop` and `/goal` — A Counterintuitive Power Guide

A field guide to using Claude Code's `/loop` and `/goal` for things they were
*not* obviously designed for. Almost everyone uses `/goal` for "build until
done" and `/loop` for "poll the deploy." Those are the brochure uses. This guide
is about the rest.

Every pattern below is built on the *actual* documented mechanics (verified
against the cached `code.claude.com/docs` pages), not folklore. The mechanics
section comes first because the clever uses fall out of understanding the
primitives precisely.

---

## Table of contents

1. [The mechanics that actually matter](#the-mechanics-that-actually-matter)
2. [The reframe that unlocks everything](#the-reframe-that-unlocks-everything)
3. [Exploiting `/goal`'s free judge](#exploiting-goals-free-judge)
4. [Exploiting `/loop`'s persistence + self-editable tape](#exploiting-loops-persistence--self-editable-tape)
5. [The big unlock: compose them (loop = clock, goal = ratchet)](#the-big-unlock-compose-them-loop--clock-goal--ratchet)
6. [Recipes for a docs-monitor repo](#recipes-for-a-docs-monitor-repo)
7. [Guardrails](#guardrails)
8. [Cheat sheet](#cheat-sheet)

---

## The mechanics that actually matter

### `/goal` — stop on *truth*, with a free adversarial judge

- Sets a **completion condition**; after every turn a **separate, small fast
  model** (Haiku by default) decides whether the condition holds. A "no" starts
  another turn automatically; a "yes" clears the goal.
- **The judge reads only the transcript — it does not run tools.** It can only
  be convinced by what Claude has *surfaced in the conversation*. This is the
  single most important and most underused fact about `/goal`.
- The judge returns a short **reason** each turn, and a "no" feeds that reason
  back as steering for the next turn.
- The condition can be up to **4,000 characters** — big enough to hold a real
  acceptance-criteria list.
- Bound a run by writing a turn/time clause *into* the condition, e.g.
  `or stop after 20 turns`.
- Works **headless**: `claude -p "/goal <condition>"` runs the loop to
  completion in one invocation. `Ctrl+C` interrupts it.
- It is a wrapper around a **session-scoped prompt-based Stop hook**. Requires a
  trusted workspace; unavailable when `disableAllHooks` or
  `allowManagedHooksOnly` is set.
- Survives `--resume`/`--continue` (the condition carries over; turn count,
  timer, and token baseline reset).
- Requires Claude Code **v2.1.139+**.

### `/loop` — stop on *exhaustion or never*, with a self-editable tape

- Three modes by what you provide:
  - **Interval + prompt** → fixed cron schedule: `/loop 5m check the deploy`
  - **Prompt only** → Claude **self-paces**, picking a delay of **1 minute to 1
    hour** after each iteration based on what it observed, and prints the delay
    and the reason.
  - **Interval only / nothing** → runs the **built-in maintenance prompt**, or
    your `loop.md` if one exists.
- Can wrap another command as its body:
  `/loop 20m /review-pr 1234`.
- **`loop.md` is re-read fresh every iteration**, so you can edit the loop's own
  instructions while it runs. Lookup order: project `.claude/loop.md` (wins) →
  user `~/.claude/loop.md`. Plain Markdown, truncated past **25,000 bytes**.
- Self-paced mode can **end itself** by simply not scheduling the next wakeup
  once the work is provably done. It may also use the **Monitor tool** to stream
  a background script's output instead of polling.
- Session-scoped; survives `--resume`. **Expires after 7 days.** `Esc` stops a
  loop that's waiting for its next tick.
- Requires Claude Code **v2.1.72+**. Alias: `/proactive`.

> **Provider caveats:** on Bedrock, Vertex AI, and Microsoft Foundry, a
> no-interval prompt runs on a fixed 10-minute schedule, and bare `/loop` /
> `loop.md` behavior differs (it prints usage instead of running the maintenance
> prompt, and `loop.md` isn't read).

---

## The reframe that unlocks everything

These aren't a "keep working" command and a "cron" command. They're two
different **halting oracles** plus two **free superpowers**:

| Primitive | Stops on | Free superpower |
|-----------|----------|-----------------|
| `/goal`   | **truth** (semantic completion) | a **free adversarial judge** that only believes the transcript |
| `/loop`   | **exhaustion or never** (rhythm) | a **free persistent process** with a **self-editable instruction tape** |

Once you see them as a *stopping rule* and a *heartbeat*, you can point them at
anything that needs one — not just coding tasks.

---

## Exploiting `/goal`'s free judge

The judge reads only what you put in the transcript, so it's a **"prove it"
gate** you can weaponize against your own optimism.

### 1. The anti-hallucination / prove-it gate

Phrase the condition as the **evidence that must appear**, not the outcome:

```
/goal the transcript shows all four: (1) a test that reproduces the bug and currently FAILS,
(2) the one-line root cause, (3) the fix, (4) that same test now passing — or stop after 15 turns
```

The judge won't pass on "I fixed it" — it needs the four artifacts visibly in
the conversation. This converts a fuzzy "is it done?" into a mechanical evidence
checklist enforced by a *fresh* model. Highest-leverage counterintuitive use: it
stops the worker from declaring premature victory.

### 2. Invert it into a fuzzer / flaky-test hunter (a tripwire goal)

Goals usually mean "make it good." Flip the sign and make the **failure** the
target:

```
/goal I have run the flaky integration test enough times to actually reproduce its failure
at least once and captured the failing output
```

Now Claude won't stop until it **witnesses the bad event**. Same trick for "keep
probing this endpoint until you get a 500," "keep generating inputs until the
parser crashes." A completion engine repurposed as a reproduction engine.

### 3. The Ulysses pact (a self-restraint device)

The condition can carry constraints that must *not* change. Use it to bind your
future turns against scope creep:

```
/goal auth tests pass AND the diff touches only src/auth AND stays under 150 lines
```

A productivity tool used as a discipline tool — the judge fails you if you
sprawl.

### 4. The spec *is* the halting condition

4,000 chars is enough for a real acceptance-criteria list. Put your spec there,
version it in git, and the spec becomes a **reusable, model-checked oracle** with
no test code written:

```bash
claude -p "/goal $(cat spec-acceptance.md)"   # headless, walk away
```

Re-run it next month and it's a **semantic regression check**: converges in zero
extra turns → still compliant; does work → something drifted. Product
requirements become a living invariant.

### 5. Mine the "reason" channel as a free PM

Every turn the judge hands back *why it's not done yet*. Design the condition
less to terminate and more to **steer** — the reason becomes a turn-by-turn TODO
generator written by a second model. `/goal` as a coach, not a finish line.

---

## Exploiting `/loop`'s persistence + self-editable tape

`loop.md` is re-read every iteration, so it's not config — it's a **mutable
program the loop runs against itself**, and a **shared surface you and Claude
both write to across time**.

### 6. The self-modifying loop (compounding agent)

End your `loop.md` with: *"Append one lesson learned this iteration to the
Lessons section of this file."* Iteration N teaches iteration N+1. The loop stops
being repetitive and starts **learning** — a curriculum that ratchets up on its
own. A polling tool turned into a self-improving one.

### 7. `loop.md` as an async blackboard across sleep/timezones

Leave a self-paced `/loop` running. From your editor, drop new priorities into
`loop.md` whenever they occur to you; Claude picks them up on the next tick and
writes status back. It's a message queue between you-now and Claude-later: you go
to bed, it keeps tending the repo, and you both edit the same standing-orders
file. Asymmetric collaboration across time.

### 8. Evolutionary search (loop as optimizer)

The docs sell `/loop` for polling; its self-paced, self-terminating mode is
actually a general iterative-deepening engine. Use it as a genetic algorithm
where Claude is the mutate+select operator:

```
/loop generate one new variant of the onboarding headline, score it against the rubric in
champions.md, keep the top 5, mutate from the best; stop when 3 rounds yield no improvement
```

`champions.md` is the gene pool / hall of fame. Works for prompts, configs, copy,
query plans — anything with an oracle.

### 9. The smart ambient filter (cron with judgment)

Plain cron does "do X." The value of a `/loop` body is **discrimination**:

```
/loop check the last hour of Sentry errors; surface ONLY ones not already in known-issues.md,
and append genuinely-new ones there
```

It's a noise filter made of judgment — it pings you on novelty, not on schedule.
(In this mode Claude may reach for the **Monitor tool** to stream a background
script instead of re-polling, which is often more responsive and
token-efficient.)

---

## The big unlock: compose them (loop = clock, goal = ratchet)

The pattern almost no one reaches for, and the most powerful. `/loop` is an
eternal process with no notion of "done per item." `/goal` guarantees convergence
but runs once. Nest them and you get an autonomous worker that **picks up work on
a heartbeat AND drives each piece to a *verified* done state** instead of
abandoning it half-finished. Since `/loop` can take a command as its body, it's
one line:

```
/loop 1h /goal the release/next PR has green CI and zero unresolved review threads,
or stop after 12 turns
```

Every hour: re-arm a **bounded, judge-verified** push. The loop is the metronome
(never quits, survives `--resume`); the goal is the ratchet (only locks in real
completion). Outer loop schedules, inner loop drives to setpoint — a
control-systems architecture made of two slash commands.

---

## Recipes for a docs-monitor repo

This project already ships `/check-docs → /digest → /impact`. Wire it into a
standing nervous system.

### A self-paced doc early-warning daemon

Put this in `~/.claude/loop.md`, then just run a bare `/loop`:

```markdown
Run /check-docs. If it reports changes, run /digest, then /impact 7d.
If any change is classified breaking AND /impact says it hits my actual ~/.claude config,
open a GitHub issue. If nothing changed, say so in one line and wait longer.
Append a dated one-liner of what you found to loop-journal.md.
```

Your entire pipeline becomes an always-on colleague that gets quieter when the
docs are quiet (self-pacing) and louder when something actually affects *your*
setup — and it journals its own history (the self-modifying tape, pattern #6).

### Backfill-to-completion with a verified floor

Instead of babysitting `backfill`, let the judge enforce a whole database:

```
/goal every change_event row that has a diff also has a non-null category and severity,
and `query --json` returns zero unclassified rows — or stop after 25 turns
```

The judge reads your `query` output from the transcript and won't release until
the database is genuinely whole.

---

## Guardrails

"Think big" plus autonomy can bite. Keep these in place:

- **Always bound a goal** with `or stop after N turns` / a time clause — an
  unsatisfiable condition grinds (and spends) forever.
- **Auto mode is what makes these unattended.** Turn it on deliberately, and
  lean on the maintenance loop's built-in rule that irreversible actions
  (push/delete) only proceed when the transcript already authorized them.
- **Know the kill switches:** `Esc` stops a waiting loop; `/goal clear` (aliases:
  `stop`, `off`, `reset`, `none`, `cancel`) drops a goal; `/clear` removes both.
- **Watch spend** on long `/goal` runs (`/goal` with no argument shows turns +
  tokens). The Haiku judge is cheap; the worker turns are not.
- **Self-paced loops self-expire at 7 days** — fine for a daemon, but it's not
  permanent infrastructure. For that, use Routines (cloud), Desktop scheduled
  tasks, or GitHub Actions.
- **The judge can't see what you don't surface.** If a condition depends on a
  file or command result, make sure Claude prints it into the transcript, or the
  evaluator will never agree.

---

## Cheat sheet

| You want… | Use | One-liner |
|-----------|-----|-----------|
| Stop only when something is *provably* true | `/goal` prove-it gate | `/goal transcript shows failing test → root cause → fix → passing test, or stop after 15 turns` |
| Reproduce a rare failure | `/goal` tripwire (inverted) | `/goal I've reproduced the flaky failure at least once and captured the output` |
| Enforce scope discipline | `/goal` Ulysses pact | `/goal tests pass AND diff only touches src/auth AND under 150 lines` |
| Build to spec unattended | `/goal` as oracle (headless) | `claude -p "/goal $(cat spec-acceptance.md)"` |
| A loop that learns | self-modifying `loop.md` | end the file with "append one lesson to the Lessons section" |
| Hand off work across time | `loop.md` blackboard | edit `loop.md` from your editor while a bare `/loop` runs |
| Optimize toward a rubric | `/loop` as evolutionary search | `/loop mutate best variant vs champions.md, keep top 5, stop after 3 dry rounds` |
| Alert only on novelty | `/loop` smart filter | `/loop surface only Sentry errors not in known-issues.md; append new ones` |
| Pick up work *and* finish each piece | `/loop` + `/goal` | `/loop 1h /goal release PR is green with no open threads, or stop after 12 turns` |

---

*Built on Claude Code docs for `/goal` (v2.1.139+) and `/loop` / scheduled tasks
(v2.1.72+). Mechanics verified against the cached documentation snapshot in this
repo; the counterintuitive patterns are extrapolations from those mechanics, not
documented features.*
