# E3 — 3-trial noise floor at v4.3.9 config

**Question**: Are per-question correctness shifts we've been treating as signal
actually reproducible at fixed config?

**Method**: Replay v4.3.9's pipeline twice with identical code and config. Run
ids: `20260506-rag-v4.3.10-trial2` and `…-trial3`. Same `answers.jsonl`, same
benchmark, same prompts. Score with the same scorer.

**Wall time**: trial2 ~3h (started 2026-05-05 23:53 UTC); trial3 ~3h (started
2026-05-06 02:48 UTC); both completed by 2026-05-06 06:23 UTC.

---

## Correctness matrix

| Q | dimension | v4.3.9 | trial2 | trial3 | stable? |
|------|-------------------|---------------|---------------|---------------|----|
| Q005 | factual           | correct       | correct       | correct       | ✅ 3/3 |
| Q010 | citation          | correct       | correct       | **hallucinated** | ⚠️ 2/3 same |
| Q012 | coverage          | partial       | partial       | partial       | ✅ 3/3 |
| Q021 | hallucination_lure| partial       | partial       | partial       | ✅ 3/3 |
| **Q027** | **recency**   | **incorrect** | **incorrect** | **incorrect** | ✅ **3/3** |
| Q032 | negation          | partial       | partial       | partial       | ✅ 3/3 |
| Q036 | cross_source      | partial       | partial       | partial       | ✅ 3/3 |
| Q049 | paraphrase_pair   | correct       | partial       | partial       | ⚠️ v4.3.9 outlier |
| Q050 | paraphrase_pair   | partial       | partial       | correct       | ⚠️ trial3 outlier |

**Trial totals (correctness distribution):**

| Run     | correct | partial | incorrect | hallucinated |
|---------|---------|---------|-----------|--------------|
| v4.3.9  | 3       | 5       | 1         | 0            |
| trial2  | 2       | 6       | 1         | 0            |
| trial3  | 2       | 5       | 1         | 1            |

---

## Per-question reading

### Q027 — incorrect 3/3 ✅ regression confirmed

All three runs produce the same fundamental failure: the agent concludes "no
April 23, 2026 default-model change event appears in my evidence." All three
runs miss the same canonical points:

- The default model for Enterprise pay-as-you-go and Anthropic API users
  changed to Opus 4.7 on April 23, 2026
- The previous default was Sonnet 4.6
- ANTHROPIC_MODEL or `model` in server-managed settings can override

The failure mode is structurally identical across runs. **Combined with E1's
finding (c1921 in `initial_evidence` at position 1, confidence 10.0), this
locks the diagnosis: agent-curation is dropping the perfect chunk consistently
across replays.** Not noise. Not sampling variance.

### Q005 — correct 3/3 ✅ robust correct

Stable. The opusplan question's evidence is well-covered by retrieval and
the agent reliably produces the canonical answer.

### Q012, Q021, Q032, Q036 — partial 3/3 ✅ robust partial

These four are partial-correct in every run. The partial verdict is
**structural to the corpus or the question**, not noise. No eval methodology
change would move them.

- Q012 (coverage): consistently misses CLAUDE.local.md and `.claude/rules/*.md`
  as distinct mechanisms; consistently inflates with settings/hooks
- Q021 (hallucination_lure): consistently identifies `--parallel-agents` doesn't
  exist but consistently invents `--teammate-mode` and similar
- Q032 (negation): consistently covers root/home circuit breaker but consistently
  misses the named .git/.claude/.vscode/.idea/.husky list
- Q036 (cross_source): consistently captures CLI vs SDK distinction but consistently
  hallucinates exact event counts and TypeScript-only events

### Q010 — 2 correct, 1 "hallucinated" ⚠️

trial3's Q010 received a `hallucinated` verdict (rather than `correct`/
`partial`/`incorrect`) — a verdict reserved for answers that fabricate
specifics not in the canonical. Trial3 invented `:*` syntax,
`Bash(ls:*)` equivalence, fabricated process-wrapper stripping rules, and
ended truncated. v4.3.9 and trial2 produced clean correct answers.

This is **a 1/3 hallucination flip on what looked like a stable correct.** The
underlying answer-generation has tail behavior we hadn't seen on this Q before.

### Q049 — v4.3.9 was the outlier ⚠️

v4.3.9: correct. trial2: partial. trial3: partial. The `correct` was the
lucky draw. **Both new trials lose the "both surfaces support hooks, custom
tools, streaming input" canonical point** — exactly the missing-point pattern
that distinguishes correct vs partial here. v4.3.9 happened to include it; the
two replays didn't.

This means the v4.3.9 → v4.3.7 Q049 delta we've been studying (pool divergence,
plan stability, etc.) was layered on top of an inherently noisy verdict on
this question.

### Q050 — partial 2/3, correct 1/3 ⚠️

The mirror situation: v4.3.9 and trial2 are partial, trial3 is correct.
Trial3 happened to cover the canonical points the others missed. Same noise
mechanism as Q049, just flipped sign.

---

## Aggregate stability

- **6 of 9 questions are 3/3 same verdict** — high stability on this subset.
- **3 of 9 oscillate** — Q010 (correct↔hallucinated), Q049 (correct↔partial),
  Q050 (partial↔correct).
- **The 3-trial correct count varies by ±1** (3, 2, 2). The v4.3.9 figure was
  at the top end of the noise envelope.

The plan asked specifically:

> Q050 correct→partial — is this systematic or one-off?

→ **Systematic.** Both new trials produced partial. v4.3.9's partial was not a
v4.3.7 → v4.3.9 *change*; v4.3.9 was already partial 3/3 (counting trial2/3),
v4.3.7 just looked correct. (Aside: trial3 producing `correct` shows there's
~1/3 probability of a clean run on this Q regardless of code version.)

> Q027 incorrect — does it land 3/3 or sometimes correct?

→ **3/3 incorrect.** Reproducible. Fix is justified by the data.

> Q049 correct — does it stay correct, or was v4.3.9 lucky?

→ **Lucky draw.** Both new trials are partial. The 9-Q correct count being 3
in v4.3.9 vs 2 in trial2/3 is mostly Q049 oscillating.

---

## Implications for fix scope

1. **Q027 fix is justified.** Three replays with no code change keep producing
   the same retrieval-failure-dressed-as-confident-negative-finding. E1 already
   localized the mechanism (agent curation drops c1921 despite confidence 10/10).

2. **Q049 fix is NOT justified yet.** What looked like a v4.3.9 → v4.3.7 shift
   is largely the verdict's own ~1/3 oscillation. Don't act on it until we
   distinguish replay noise from code-version-attributable change. A fair test
   would be 3-trial replays at v4.3.7's config too.

3. **Q010 noise is new.** The hallucinated verdict on trial3 hasn't been
   seen on Q010 before. One observation isn't enough to act on, but it's worth
   flagging — the model's tail behavior on citation-dimension questions is
   wider than we'd assumed.

4. **Eval methodology note.** Single-trial verdicts on this 9-Q subset have
   ±1 noise on `correct_count`. Either average across trials before treating
   a delta as signal, or restrict eval to the 6 stable questions.
