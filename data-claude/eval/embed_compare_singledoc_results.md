# Single-doc bake-off (R0b)

_Run: 2026-05-03 20:56:48_


Giving voyage-context-3 a fair shot: one document, well under 32K tokens, full contextual conditioning.


## permissions.md (52 chunks, ~19K tokens) (~19362 tokens)


| Pair | Metric | voyage-4-large | voyage-context-3 |
|---|---|---:|---:|
| Q041/Q042 (limit/restrict tools) | Jaccard@5 | 0.667 | _filled below_ |
|  | query cosine | 0.909 | _filled below_ |
| probe pair (shorter limit/restrict) | Jaccard@5 | 1.000 | _filled below_ |
|  | query cosine | 0.916 | _filled below_ |

| Pair | Metric | voyage-4-large | voyage-context-3 |
|---|---|---:|---:|
| Q041/Q042 (limit/restrict tools) | Jaccard@5 | 0.667 | 0.667 |
|  | query cosine | 0.909 | 0.871 |
| probe pair (shorter limit/restrict) | Jaccard@5 | 1.000 | 0.429 |
|  | query cosine | 0.916 | 0.887 |

## hooks-guide.md (66 chunks, ~31K tokens) (~30973 tokens)


| Pair | Metric | voyage-4-large | voyage-context-3 |
|---|---|---:|---:|
| probe pair (hooks) | Jaccard@5 | 0.000 | _filled below_ |
|  | query cosine | 0.761 | _filled below_ |

| Pair | Metric | voyage-4-large | voyage-context-3 |
|---|---|---:|---:|
| probe pair (hooks) | Jaccard@5 | 0.000 | 0.111 |
|  | query cosine | 0.761 | 0.722 |

## authentication.md (10 chunks, ~?K tokens) (~5008 tokens)


| Pair | Metric | voyage-4-large | voyage-context-3 |
|---|---|---:|---:|
| Q047/Q048 (credentials location) | Jaccard@5 | 1.000 | _filled below_ |
|  | query cosine | 0.824 | _filled below_ |

| Pair | Metric | voyage-4-large | voyage-context-3 |
|---|---|---:|---:|
| Q047/Q048 (credentials location) | Jaccard@5 | 1.000 | 0.667 |
|  | query cosine | 0.824 | 0.804 |

## Aggregate (excluding 32K-overflow cases)


| Model | Mean Jaccard@5 | N |
|---|---:|---:|
| voyage-4-large | 0.667 | 4 |
| voyage-context-3 | 0.468 | 4 |

## Verdict


**voyage-4-large wins** by +0.198 on single-doc Jaccard@5 — even in the contextual model's sweet spot


- voyage-4-large mean Jaccard@5: **0.667**
- voyage-context-3 mean Jaccard@5: **0.468**

