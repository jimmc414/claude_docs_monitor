# Embed Model Bake-off (R0)

_Run: 2026-05-03 20:51:10_


Comparing: voyage-4-large, voyage-context-3
Probe pairs: 5 | Benchmark pairs: 5


## Test 1 — Probe-pair query-to-query cosine

Higher cosine = better synonym bridging by the embedding model itself.


| Pair | voyage-4-large | voyage-context-3 |
|---|---:|---:|
| 1. How do I limit which tools Claude can us…/How do I restrict Claude's too… | 0.916 | 0.887 |
| 2. How do I configure Claude Code to use AW…/How do I run Claude Code on Be… | 0.807 | 0.635 |
| 3. Where are session settings stored?…/What's the location of the set… | 0.601 | 0.658 |
| 4. How do hooks work in Claude Code?…/What is a hook and how is it c… | 0.761 | 0.722 |
| 5. How do I create a custom slash command?…/How do I add a new slash comma… | 0.876 | 0.830 |

| **Mean** | **0.792** | **0.746** |

## Test 2 — Real-chunk Jaccard@5 (benchmark pairs)

Embed all chunks from each pair's expected_pages, compute top-5 per query half, then Jaccard between the two halves' top-5 lists.


| Pair | voyage-4-large | voyage-context-3 |
|---|---:|---:|
| Q041/Q042 (202c) | 0.429 | 0.429 |
| Q043/Q044 (74c) | 0.667 | 0.250 |
| Q045/Q046 (171c) | 0.250 | 0.000 |
| Q047/Q048 (10c) | 1.000 | 0.667 |
| Q049/Q050 (141c) | 0.667 | ERR: Request to model 'voyage-conte |

| **Mean Jaccard@5** | **0.602** | **0.336** |

## Decision

- **voyage-4-large**: probe cosine mean **0.792**, bench Jaccard@5 mean **0.602**
- **voyage-context-3**: probe cosine mean **0.746**, bench Jaccard@5 mean **0.336**


**Decision**: ship `voyage-context-3` — Neither is great, but only contextual has any chance of recovering. Escalate.

## Cost note

Voyage's 200M free tier covers this entire experiment (estimated <100K tokens consumed across both models).
