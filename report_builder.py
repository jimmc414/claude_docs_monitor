"""Agentic RAG report builder for the docs-monitor.

Pipeline (per the plan):

    1. PLAN
       Claude (Opus, max_turns=1): decompose question → 3-7 sub-questions
       + retrieval plan (structured JSON).

    2. RETRIEVE (parallel)
       For each sub-question: HybridRetriever.retrieve(sub_q, scope, filters).
       Collect Evidence[] with chunk provenance.

    3. REASON & GAP-FILL (Agent SDK loop, max_turns=N)
       Claude with custom in-process MCP tools:
         - hybrid_search(query, source_type?, filters?, k?)
         - get_chunk(chunk_id)
         - find_similar(chunk_id)
         - get_diff(url)
       Loop terminates when Claude declares "evidence sufficient".

    4. SYNTHESIZE
       Claude (Opus, generous max_tokens): write the report. Inline citations.

    5. SELF-CRITIQUE
       Claude reviews own report; if gaps, re-loops into step 3 (max 2 retries).

    6. OUTPUT
       Markdown to data-claude/reports/{slug}.md
       Companion JSON: data-claude/reports/{slug}.json with full Evidence[].

Why agentic: a single retrieve-then-write doesn't handle compound questions
("compare X and Y over the last 30 days"). Decomposing → retrieving →
reasoning → re-retrieving → synthesizing → self-critiquing is the documented
pattern Anthropic uses internally for Research mode.

Environment:
  * DOCS_MONITOR_REPORT_VERBOSE=1 — print loop progress to stderr.
"""

from __future__ import annotations

import asyncio
import json
import os
import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from doc_index import DocIndex
from embedding_cache import EmbeddingCache
from llm_backend import call_claude, RateLimitError
from retriever import HybridRetriever


def _vprint(msg: str) -> None:
    if os.environ.get("DOCS_MONITOR_REPORT_VERBOSE") == "1":
        print(f"[report_builder] {msg}", file=sys.stderr)


def _slugify(text: str, max_len: int = 60) -> str:
    s = re.sub(r"[^\w\s-]", "", text.lower()).strip()
    s = re.sub(r"[\s-]+", "-", s)
    return s[:max_len].strip("-")


# ── Data classes ────────────────────────────────────────────────────────────


@dataclass
class Evidence:
    chunk_id: int
    source_type: str
    source_id: str
    heading_path: str
    quote: str            # the chunk content (or excerpt thereof)
    confidence: float     # rerank score if available, else RRF
    relevance_to: str     # which sub-question this answered
    url: str | None = None
    line_start: int | None = None
    line_end: int | None = None
    metadata: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "chunk_id": self.chunk_id,
            "source_type": self.source_type,
            "source_id": self.source_id,
            "heading_path": self.heading_path,
            "quote": self.quote,
            "confidence": self.confidence,
            "relevance_to": self.relevance_to,
            "url": self.url,
            "line_start": self.line_start,
            "line_end": self.line_end,
            "metadata": self.metadata,
        }


@dataclass
class Report:
    question: str
    plan: dict
    evidence: list[Evidence]
    markdown: str
    citations_validated: bool
    elapsed_seconds: float
    loop_turns: int
    markdown_path: Path
    json_path: Path
    critique: dict | None = None
    re_critique: dict | None = None


# ── Step 1: PLAN ────────────────────────────────────────────────────────────


PLAN_PROMPT = """You are decomposing a research question into a retrieval plan.

User question: {question}

Scope: {scope}
Date range: {date_range}

Output a JSON object with this structure (no other text, no markdown fences):
{{
  "sub_questions": [
    "<sub-question 1>",
    "<sub-question 2>",
    ...
  ],
  "search_strategies": [
    {{
      "sub_question_index": 0,
      "search_query": "<retrieval query for sub-question 0>",
      "source_type": "page" | "change_event" | null,
      "filters": {{}}
    }},
    ...
  ]
}}

Rules:
  - 3-7 sub-questions (use fewer for simple questions, more for compound ones).
  - For each sub-question, provide a search_query optimized for retrieval
    (use vocabulary the documentation likely uses).
  - Use source_type='change_event' if the sub-question is about *what
    changed*. Use 'page' for stable docs questions. null = both.
  - Filter by category if asked about specific change types ('breaking',
    'feature', 'deprecation', 'clarification', 'flag_change', 'bugfix').
  - ENUMERATION rule: if the question asks about ALL or EVERY mechanism, or
    asks the user to COMPARE / DIFFER between options ("what are all the ways
    to X", "every mechanism for Y", "compare A and B"), list AT LEAST 5
    candidate sub-topics in `sub_questions`, each one targeting a distinct
    category. It is better to over-search and find no result for a candidate
    than to miss a category entirely. For example, for "all knowledge
    persistence mechanisms" you should enumerate at least: CLAUDE.md,
    auto memory / MEMORY.md, skills, settings.json, hooks, sub-agents,
    transcripts/sessions — each as its own sub-question.
"""


def _plan_question(
    question: str,
    scope: list[str] | None,
    since: str | None,
    until: str | None,
    model: str = "sonnet",
) -> dict:
    """Decompose the question into sub-questions + per-sub retrieval strategies."""
    scope_str = ",".join(scope) if scope else "all"
    date_str = f"{since or 'any'} to {until or 'now'}"
    prompt = PLAN_PROMPT.format(
        question=question, scope=scope_str, date_range=date_str
    )
    raw = call_claude(prompt=prompt, model=model, max_tokens=1500, timeout=120)
    cleaned = raw.strip().lstrip("`").lstrip("json").strip("`").strip()
    start = cleaned.find("{")
    end = cleaned.rfind("}")
    if start < 0 or end < start:
        raise RuntimeError(f"plan JSON parse: no object found in: {raw[:200]!r}")
    try:
        plan = json.loads(cleaned[start : end + 1])
    except json.JSONDecodeError as e:
        raise RuntimeError(f"plan JSON parse failed: {e}\n{raw[:500]}") from e

    if "sub_questions" not in plan or not plan["sub_questions"]:
        # Fall back: treat the whole question as one sub-question
        plan = {
            "sub_questions": [question],
            "search_strategies": [{
                "sub_question_index": 0,
                "search_query": question,
                "source_type": None,
                "filters": {},
            }],
        }
    if "search_strategies" not in plan or not plan["search_strategies"]:
        plan["search_strategies"] = [
            {
                "sub_question_index": i,
                "search_query": q,
                "source_type": None,
                "filters": {},
            }
            for i, q in enumerate(plan["sub_questions"])
        ]
    return plan


# ── Step 2: RETRIEVE (parallel sub-question fan-out) ───────────────────────


def _initial_retrieve(
    plan: dict,
    retriever: HybridRetriever,
    scope: list[str] | None,
    since: str | None,
    until: str | None,
    k_per_sub: int = 8,
) -> list[Evidence]:
    """Run one HybridRetriever.retrieve per sub-question. Dedupe by chunk_id."""
    evidence_by_id: dict[int, Evidence] = {}

    for strategy in plan["search_strategies"]:
        sub_idx = strategy.get("sub_question_index", 0)
        sub_q_list = plan["sub_questions"]
        if sub_idx >= len(sub_q_list):
            continue
        sub_q = sub_q_list[sub_idx]
        search_q = strategy.get("search_query") or sub_q
        sub_source = strategy.get("source_type")
        if sub_source not in ("page", "change_event", None):
            sub_source = None
        # Per-sub filters merged with global since/until
        filters = dict(strategy.get("filters") or {})
        if since and "since" not in filters:
            filters["since"] = since
        if until and "until" not in filters:
            filters["until"] = until

        # If global scope is restrictive, override per-sub source_type
        if scope and len(scope) == 1 and not sub_source:
            sub_source = scope[0]

        try:
            hits = retriever.retrieve(
                search_q,
                source_type=sub_source,
                filters=filters or None,
                k=k_per_sub,
                rerank=True,
            )
        except Exception as e:
            _vprint(f"sub-question {sub_idx} retrieval failed: {e!r}")
            continue

        for h in hits:
            confidence = h.score_rerank if h.score_rerank is not None else (
                # Normalize RRF rank into a 0-1 confidence-ish number
                max(0.0, 1.0 - (h.rrf_rank / 50.0))
            )
            ev = Evidence(
                chunk_id=h.chunk_id,
                source_type=h.source_type,
                source_id=h.source_id,
                heading_path=h.heading_path,
                quote=h.content,
                confidence=float(confidence),
                relevance_to=sub_q,
                url=h.url,
                line_start=h.line_start,
                line_end=h.line_end,
                metadata=h.metadata,
            )
            existing = evidence_by_id.get(h.chunk_id)
            if existing is None or existing.confidence < ev.confidence:
                evidence_by_id[h.chunk_id] = ev

    return sorted(evidence_by_id.values(), key=lambda e: -e.confidence)


# ── Step 3: REASON & GAP-FILL (Agent SDK loop) ──────────────────────────────


def _build_sdk_tools(retriever: HybridRetriever, index: DocIndex):
    """Build in-process MCP tools the agent loop can call.

    Returns the list of SdkMcpTool instances ready for create_sdk_mcp_server.
    """
    from claude_agent_sdk import tool

    @tool(
        "hybrid_search",
        "Hybrid BM25+dense semantic search over docs and change events. "
        "Use this when you need to find more evidence for a sub-question.",
        {
            "query": str,
            "source_type": str,  # 'page' | 'change_event' | 'all'
            "k": int,
        },
    )
    async def _hybrid_search(args: dict) -> dict:
        st = args.get("source_type") or None
        if st == "all":
            st = None
        try:
            hits = retriever.retrieve(
                args["query"],
                source_type=st,
                k=int(args.get("k", 8)),
                rerank=True,
            )
        except Exception as e:
            return {"content": [{"type": "text", "text": f"Error: {e}"}]}
        formatted = json.dumps(
            [
                {
                    "chunk_id": h.chunk_id,
                    "source_type": h.source_type,
                    "heading_path": h.heading_path,
                    "url": h.url,
                    "snippet": h.content[:500],
                    "rerank": h.score_rerank,
                }
                for h in hits
            ],
            indent=2,
        )
        return {"content": [{"type": "text", "text": formatted}]}

    @tool(
        "get_chunk",
        "Fetch the full content of a chunk by chunk_id.",
        {"chunk_id": int},
    )
    async def _get_chunk(args: dict) -> dict:
        c = index.get_chunk(int(args["chunk_id"]))
        if not c:
            return {"content": [{"type": "text", "text": f"chunk_id not found"}]}
        body = (
            f"Source: {c.source_type}/{c.source_id}\n"
            f"Heading: {c.heading_path}\n"
            f"URL: {c.url or '(none)'}\n"
            f"Lines: {c.line_start}-{c.line_end}\n\n"
            f"Content:\n{c.content}"
        )
        return {"content": [{"type": "text", "text": body}]}

    @tool(
        "find_similar",
        "Find chunks most similar to a given chunk_id (broaden the evidence neighborhood).",
        {"chunk_id": int, "k": int},
    )
    async def _find_similar(args: dict) -> dict:
        try:
            hits = retriever.find_similar(
                int(args["chunk_id"]), k=int(args.get("k", 8))
            )
        except Exception as e:
            return {"content": [{"type": "text", "text": f"Error: {e}"}]}
        formatted = json.dumps(
            [
                {
                    "chunk_id": h.chunk_id,
                    "heading_path": h.heading_path,
                    "snippet": h.content[:300],
                    "score": h.score_dense,
                }
                for h in hits
            ],
            indent=2,
        )
        return {"content": [{"type": "text", "text": formatted}]}

    return [_hybrid_search, _get_chunk, _find_similar]


REASON_PROMPT = """You are completing the EVIDENCE-GATHERING phase for a research report.

User question: {question}

Plan:
{plan_json}

Initial evidence retrieved (id: heading):
{initial_evidence}

YOUR JOB: Expand and verify the evidence. Treat the initial list as a STARTING
POINT, not the answer. The planner only ran one query per sub-question, so it
almost certainly missed relevant chunks. You MUST call hybrid_search at least
2-3 times with different angles than the initial plan (synonyms, adjacent
concepts, counter-examples, edge cases) before settling. Use get_chunk to read
full content for snippets that look promising, and find_similar to expand
around the most useful hits.

Tools available:
  - hybrid_search(query, source_type, k): retrieve more chunks
  - get_chunk(chunk_id): read full content of a chunk you saw a snippet of
  - find_similar(chunk_id, k): expand the neighborhood around a useful chunk

When you have actively expanded the evidence and verified the most important
chunks, output a JSON object on the LAST line of your response with the
chunk_ids you want to cite in the final report:
  {{"final_chunk_ids": [123, 456, ...], "reasoning_complete": true}}

Aim for {target_evidence}-25 chunks of evidence. Be selective in what you
finally cite, but thorough in what you explore — a missed source is a worse
outcome than a few extra tool calls.
"""


async def _reason_and_gap_fill(
    question: str,
    plan: dict,
    initial_evidence: list[Evidence],
    retriever: HybridRetriever,
    index: DocIndex,
    model: str,
    max_turns: int,
    target_evidence: int,
) -> tuple[list[int], int]:
    """Agent SDK loop — fills gaps via custom tools. Returns (final_chunk_ids, turns_used).

    Uses ``ClaudeSDKClient`` rather than the one-shot ``query()`` helper because
    the latter exits the CLI subprocess immediately after sending the prompt,
    which races with in-process MCP tool-call ack writes and produces
    ``CLIConnectionError("ProcessTransport is not ready for writing")``. The
    long-lived client keeps the subprocess open across the full tool-use loop.
    """
    from claude_agent_sdk import (
        ClaudeAgentOptions,
        ClaudeSDKClient,
        create_sdk_mcp_server,
    )

    # Strip API key so SDK uses Max OAuth (Max plans don't support custom betas).
    # Also strip CLAUDECODE so the nested SDK invocation isn't confused by the
    # parent CLI session — same trick cmd_digest uses.
    saved_key = os.environ.pop("ANTHROPIC_API_KEY", None)
    saved_cc = os.environ.pop("CLAUDECODE", None)
    use_api_betas = saved_key is not None  # only enable beta features when running on API
    try:
        tools = _build_sdk_tools(retriever, index)
        srv_config = create_sdk_mcp_server(
            name="docs_monitor_retrieval", version="1.0.0", tools=tools
        )

        prompt = REASON_PROMPT.format(
            question=question,
            plan_json=json.dumps(plan, indent=2),
            initial_evidence="\n".join(
                f"  {e.chunk_id}: {e.heading_path[:100]}" for e in initial_evidence[:30]
            ),
            target_evidence=max(8, target_evidence),
        )

        opts_kwargs: dict = dict(
            model=model,
            max_turns=max_turns,
            permission_mode="bypassPermissions",
            mcp_servers={"retrieval": srv_config},
            allowed_tools=[
                "mcp__retrieval__hybrid_search",
                "mcp__retrieval__get_chunk",
                "mcp__retrieval__find_similar",
            ],
            stderr=lambda line: print(f"[reason-cli] {line}", file=sys.stderr, flush=True),
        )
        # The 1M-context beta is only available on API key billing. Max OAuth
        # ignores it (and warns). Skip it on Max OAuth.
        if use_api_betas:
            opts_kwargs["betas"] = ["context-1m-2025-08-07"]

        options = ClaudeAgentOptions(**opts_kwargs)

        chosen_ids: list[int] = []
        all_text_chunks: list[str] = []
        last_text = ""
        turns_used = 0

        async with ClaudeSDKClient(options=options) as client:
            await client.query(prompt)
            async for msg in client.receive_response():
                content = getattr(msg, "content", None)
                if isinstance(content, list):
                    for block in content:
                        text = getattr(block, "text", None)
                        if isinstance(text, str):
                            all_text_chunks.append(text)
                            last_text = text
                        elif hasattr(block, "name") and hasattr(block, "input"):
                            # ToolUseBlock — counts as a tool-use turn
                            turns_used += 1
                result_attr = getattr(msg, "result", None)
                if isinstance(result_attr, str) and result_attr:
                    last_text = result_attr
                    all_text_chunks.append(result_attr)

        # Search every emitted text block for the JSON sentinel — the
        # final-line convention is preferred but not always honored.
        candidates = "\n".join(all_text_chunks).splitlines() + last_text.splitlines()
        for line in reversed(candidates):
            line = line.strip()
            if line.startswith("{") and line.endswith("}") and "final_chunk_ids" in line:
                try:
                    parsed = json.loads(line)
                    chosen_ids = [int(x) for x in parsed.get("final_chunk_ids", [])]
                    if chosen_ids:
                        break
                except (json.JSONDecodeError, ValueError, TypeError):
                    continue
        # If parsing failed, fall back to the initial evidence's chunk_ids
        if not chosen_ids:
            chosen_ids = [e.chunk_id for e in initial_evidence[:target_evidence]]
        return chosen_ids, turns_used
    finally:
        if saved_key is not None:
            os.environ["ANTHROPIC_API_KEY"] = saved_key
        if saved_cc is not None:
            os.environ["CLAUDECODE"] = saved_cc


# ── Step 4: SYNTHESIZE ─────────────────────────────────────────────────────


SYNTH_PROMPT = """Write a markdown research report answering the user's question.

User question: {question}

Plan:
{plan_json}

Evidence (use these as citation sources; cite with [^cN] where N is chunk_id):

{evidence_block}

Format requirements:

# {title}

*Generated: {timestamp} · Model: {model} · Evidence chunks: {n_evidence}*

## Executive Summary
2-4 sentences. Every factual claim cited inline with [^cN].

## Key Findings
1. **{{Finding}}**: {{explanation}} [^cN] [^cM]
2. ...

## Detailed Analysis
### {{sub-question 1}}
{{prose with inline [^cN] citations}}

### {{sub-question 2}}
...

## Sources
[^c123]: brief description of chunk 123
...

CRITICAL RULES:
  - Cite every factual claim with [^cN] where N is the chunk_id (a real id from the evidence).
  - Do NOT make claims that aren't supported by the provided evidence.
  - If the evidence does NOT contain documentation of a claimed feature, flag,
    function, or behavior asked about in the user question, state explicitly:
    "[X] does not appear in the cached Anthropic documentation as of {timestamp}."
    Do NOT speculate that it might be "undocumented", "experimental", "internal",
    or "may exist in newer versions". Treat absent evidence as a hard signal that
    the feature is not part of the documented API surface. A definitive refusal
    is more useful than a hedge.
  - If the retrieved evidence is thin (fewer than 3 chunks scoring above 5.0
    rerank), call this out in the Executive Summary in one sentence so the
    reader knows the answer rests on weak ground.
  - If the evidence is insufficient for a sub-question, say so explicitly
    rather than fabricating an answer.
  - Be concrete: prefer specific identifiers, file names, dates, code
    snippets pulled directly from the evidence.
  - Aim for thorough but tight prose — readers want signal density.
  - The "Sources" section at the bottom should list every cited chunk_id with a 1-line label.
"""


def _synthesize(
    question: str,
    plan: dict,
    evidence: list[Evidence],
    model: str = "opus",
) -> str:
    """Single-shot synthesis call. Returns the full markdown report."""
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    title = question.rstrip("?.").strip().capitalize()

    evidence_lines = []
    for e in evidence:
        loc = ""
        if e.line_start and e.line_end:
            loc = f" [L{e.line_start}-{e.line_end}]"
        evidence_lines.append(
            f"### Chunk {e.chunk_id} ({e.source_type}/{e.source_id}{loc})\n"
            f"Heading: {e.heading_path}\n"
            f"URL: {e.url or '(none)'}\n"
            f"Relevance: {e.relevance_to}\n"
            f"Confidence: {e.confidence:.2f}\n"
            f"Content:\n{e.quote[:2500]}"
        )
    evidence_block = "\n\n".join(evidence_lines)

    prompt = SYNTH_PROMPT.format(
        question=question,
        plan_json=json.dumps(plan, indent=2),
        evidence_block=evidence_block,
        title=title,
        timestamp=timestamp,
        model=model,
        n_evidence=len(evidence),
    )

    raw = call_claude(
        prompt=prompt,
        model=model,
        max_tokens=8000,
        timeout=300,
    )
    return raw.strip()


# ── Step 5: SELF-CRITIQUE ──────────────────────────────────────────────────


CRITIQUE_PROMPT = """Audit a research report for citation quality AND completeness.

Question: {question}

Report:
{report}

Evidence excerpts (the source chunks the report should faithfully reflect):
{evidence_summary}

Audit two dimensions:

A. CITATION QUALITY
  1. Is every factual claim cited with [^cN] (or [^N])?
  2. Are cited chunk_ids in the report's "Sources" section?

B. COMPLETENESS — focus on enumerated content
  1. Scan the evidence above for enumerated lists (markdown lists, tables,
     comma-separated enumerations of >=3 items) that are directly relevant to
     the question.
  2. For each such enumeration, check whether ALL items appear in the report.
  3. Common gaps: directory lists where some entries are dropped (e.g. report
     mentions ".git, .vscode" but evidence has ".git, .claude, .vscode, .idea, .husky");
     comparison tables missing rows; option flag lists with omitted flags.
  4. Do NOT flag stylistic summaries — only flag when the report COULD have
     listed all N items but listed only K<N. Skip if the question explicitly
     asks for "the most important" or "key" items only.

Output a JSON object (no other text):
{{
  "ok": true | false,
  "uncited_claims": ["<verbatim quote of any uncited claim>", ...],
  "missing_sources": [<chunk_ids cited but not in Sources>, ...],
  "missing_enumerations": [
    {{"source_chunk": <chunk_id>, "enumeration": "<short label, e.g. 'protected directory list'>",
      "items_in_evidence": ["item1", "item2", ...],
      "items_in_report": ["item1", ...],
      "missing": ["item3", "item4"]}},
    ...
  ],
  "verdict": "<one-line summary>"
}}

`ok` is false if EITHER citation quality fails OR a `missing_enumerations`
gap has 2+ missing items. Single-item gaps may be intentional summarization.
"""


def _parse_citations_with_sentences(md: str) -> list[tuple[int, str]]:
    """Return list of (chunk_id, cited_sentence) for each [^cN] citation.

    Handles citation clusters like "Sentence text. [^c123][^c456] Next sentence."
    The cited sentence is the one ending just before the citation cluster.
    """
    out = []
    pattern = re.compile(r"\[\^c?(\d+)\]")
    for m in pattern.finditer(md):
        cid = int(m.group(1))
        start = m.start()
        ctx_start = max(0, start - 800)
        ctx = md[ctx_start:start]
        ctx_stripped = re.sub(r"(\[\^c?\d+\][\s,;]*)+\s*$", "", ctx).rstrip()
        if not ctx_stripped:
            sentence_raw = ctx[-200:]
        else:
            positions = []
            for sep in (". ", "! ", "? ", "\n"):
                idx = ctx_stripped.rfind(sep)
                if idx >= 0:
                    positions.append(idx + len(sep) - 1)
            terminators = [p for p in positions if p < len(ctx_stripped) - 1]
            sent_start = (max(terminators) + 1) if terminators else 0
            sentence_raw = ctx_stripped[sent_start:]
        sentence_clean = pattern.sub("", sentence_raw).strip()
        sentence_clean = re.sub(r"\s+", " ", sentence_clean)
        out.append((cid, sentence_clean))
    return out


ENTAILMENT_PROMPT = """You are auditing a single citation in a research report.

Sentence: {sentence}

Cited chunk content:
{chunk_content}

Does the chunk content support (entail) the sentence?

Respond with EXACTLY one of these labels on the first line, then a brief reason:
  supports     — the chunk directly states or clearly implies the claim
  partial      — the chunk is related and partially supports it but is incomplete
  contradicts  — the chunk states something that conflicts with the claim
  unrelated    — the chunk does not address the claim at all

Format:
<label>
<one-line reason>
"""


# Bound the worst-case audit cost. With ~25 citations clustered into ~8
# sentences a typical report stays under this; reports that flood citations
# get truncated audits (un-audited surplus is logged but kept).
MAX_ENTAILMENT_CHECKS = 20


def _entailment_audit(
    report_md: str,
    evidence_by_id: dict[int, "Evidence"],
    index: "DocIndex",
    model: str = "haiku",
    max_checks: int = MAX_ENTAILMENT_CHECKS,
) -> tuple[str, list[dict]]:
    """Per-citation entailment check. Drops contradicting/unrelated citations.

    Returns (revised_markdown, audit_records). Each audit record is a dict with
    keys: chunk_id, sentence, verdict, reason, action_taken.

    Caps actual LLM calls at ``max_checks`` unique (chunk_id, sentence) pairs.
    Surplus pairs are recorded with verdict='skipped' and kept (no rewrite).
    """
    citations = _parse_citations_with_sentences(report_md)
    if not citations:
        return report_md, []

    audit: list[dict] = []
    bad_pairs: set[tuple[int, str]] = set()  # (chunk_id, sentence) to drop

    # Dedupe first so the cap reflects actual API calls, not tokens
    unique_pairs: list[tuple[int, str]] = []
    seen: set[tuple[int, str]] = set()
    for chunk_id, sentence in citations:
        key = (chunk_id, sentence)
        if key in seen:
            continue
        seen.add(key)
        unique_pairs.append((chunk_id, sentence))

    n_checked = 0
    for chunk_id, sentence in unique_pairs:
        if n_checked >= max_checks:
            audit.append({
                "chunk_id": chunk_id,
                "sentence": sentence[:300],
                "verdict": "skipped",
                "reason": f"max_checks={max_checks} budget exhausted",
                "action_taken": "kept",
            })
            continue

        ev = evidence_by_id.get(chunk_id)
        if ev is not None:
            chunk_content = ev.quote
        else:
            c = index.get_chunk(chunk_id)
            chunk_content = c.content if c else ""
        if not chunk_content:
            audit.append({
                "chunk_id": chunk_id,
                "sentence": sentence[:300],
                "verdict": "unknown",
                "reason": "chunk not found",
                "action_taken": "kept",
            })
            continue

        prompt = ENTAILMENT_PROMPT.format(
            sentence=sentence[:1000],
            chunk_content=chunk_content[:3000],
        )
        n_checked += 1
        try:
            raw = call_claude(
                prompt=prompt, model=model, max_tokens=200, timeout=60,
            )
        except Exception as e:
            _vprint(f"entailment audit failed for chunk {chunk_id}: {e!r}")
            audit.append({
                "chunk_id": chunk_id,
                "sentence": sentence[:300],
                "verdict": "error",
                "reason": str(e)[:200],
                "action_taken": "kept",
            })
            continue

        lines = [ln.strip() for ln in raw.strip().splitlines() if ln.strip()]
        verdict = (lines[0] if lines else "").lower().strip(" .:")
        reason = lines[1] if len(lines) > 1 else ""
        for label in ("supports", "partial", "contradicts", "unrelated"):
            if label in verdict:
                verdict = label
                break
        else:
            verdict = "unknown"

        if verdict in ("contradicts", "unrelated"):
            bad_pairs.add((chunk_id, sentence))
            action = "dropped"
        else:
            action = "kept"
        audit.append({
            "chunk_id": chunk_id,
            "sentence": sentence[:300],
            "verdict": verdict,
            "reason": reason[:300],
            "action_taken": action,
        })

    if not bad_pairs:
        return report_md, audit

    # Drop contradicting/unrelated citations from the markdown. We re-walk the
    # citations in order, computing the sentence for each one, and remove the
    # token if it's bad.
    pattern = re.compile(r"\[\^c?(\d+)\]")
    matches = list(pattern.finditer(report_md))
    parsed = _parse_citations_with_sentences(report_md)  # same order as matches
    if len(matches) != len(parsed):
        return report_md, audit  # safety: re-parse mismatch, give up on rewrite
    keep_mask = []
    for (cid, sentence), m in zip(parsed, matches):
        keep_mask.append((cid, sentence) not in bad_pairs)

    out_parts: list[str] = []
    cursor = 0
    for keep, m in zip(keep_mask, matches):
        out_parts.append(report_md[cursor:m.start()])
        if keep:
            out_parts.append(m.group(0))
        cursor = m.end()
    out_parts.append(report_md[cursor:])
    revised = "".join(out_parts)
    # Collapse double-spaces left by removed tokens
    revised = re.sub(r"  +", " ", revised)
    return revised, audit


def _entailment_revise(
    question: str,
    plan: dict,
    evidence: list["Evidence"],
    bad_audit: list[dict],
    model: str = "opus",
) -> str:
    """Strict-citations mode: ask the synthesizer to fix citations rather than drop them."""
    notes = []
    for rec in bad_audit:
        if rec.get("action_taken") != "dropped":
            continue
        notes.append(
            f"  - Chunk {rec['chunk_id']} ({rec['verdict']}): the cited sentence "
            f"\"{rec['sentence'][:150]}\" is not supported by chunk {rec['chunk_id']}. "
            f"Either rewrite the sentence to match the chunk, or drop the citation."
        )
    if not notes:
        return ""
    revise_question = (
        f"{question}\n\nThe previous draft had these citation problems:\n"
        + "\n".join(notes)
        + "\n\nProduce a revised report that fixes these citations."
    )
    return _synthesize(revise_question, plan, evidence, model=model)


def _build_evidence_summary_for_critique(
    evidence: list["Evidence"] | None, max_chars: int = 20000
) -> str:
    """Compact evidence chunks for the critique prompt.

    Includes chunk_id, source_id, and content (truncated). Prioritizes chunks
    most likely to contain enumerations: those with markdown list/table tokens.
    """
    if not evidence:
        return "(no evidence provided to critique — completeness check skipped)"
    # Score each chunk on enumeration-likeness
    def enum_score(text: str) -> int:
        s = 0
        s += text.count("\n- ") + text.count("\n* ")  # bullet lists
        s += text.count("\n| ")                        # tables
        s += min(text.count(", "), 5)                  # inline enumerations (capped)
        return s
    ranked = sorted(evidence, key=lambda e: enum_score(e.quote), reverse=True)
    parts: list[str] = []
    used = 0
    for e in ranked:
        body = e.quote[:1500]
        block = f"[chunk_id={e.chunk_id}, source_id={e.source_id}]\n{body}\n"
        if used + len(block) > max_chars:
            break
        parts.append(block)
        used += len(block)
    return "\n---\n".join(parts) if parts else "(no enumeration-like evidence)"


def _self_critique(
    question: str,
    report_md: str,
    model: str = "sonnet",
    evidence: list["Evidence"] | None = None,
) -> dict:
    evidence_summary = _build_evidence_summary_for_critique(evidence)
    prompt = CRITIQUE_PROMPT.format(
        question=question,
        report=report_md[:30000],
        evidence_summary=evidence_summary,
    )
    try:
        raw = call_claude(prompt=prompt, model=model, max_tokens=2000, timeout=600)
    except RateLimitError as e:
        _vprint(f"critique rate-limited after retries: {e!r}")
        return {"ok": True, "verdict": "critique skipped (rate limit after retries)"}
    except Exception as e:
        _vprint(f"critique failed: {e!r}")
        return {"ok": True, "verdict": "critique skipped (error)"}
    cleaned = raw.strip().lstrip("`").lstrip("json").strip("`").strip()
    start = cleaned.find("{")
    end = cleaned.rfind("}")
    if start < 0 or end < start:
        return {"ok": True, "verdict": "critique parse failed"}
    try:
        return json.loads(cleaned[start : end + 1])
    except json.JSONDecodeError:
        return {"ok": True, "verdict": "critique JSON parse failed"}


# ── Public entry point ─────────────────────────────────────────────────────


def build_report(
    question: str,
    *,
    scope: list[str] | None = None,
    since: str | None = None,
    until: str | None = None,
    max_evidence_chunks: int = 25,
    max_loop_turns: int = 6,
    model: str = "opus",
    do_self_critique: bool = True,
    skip_entailment_audit: bool = False,
    strict_citations: bool = False,
    progress_callback=None,
    output_dir: Path = Path("data-claude/reports"),
    data_dir: Path = Path("data-claude"),
) -> Report:
    """Build a research report end-to-end. Returns the Report object."""
    t0 = time.time()
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    data_dir = Path(data_dir)
    index_db = data_dir / "index.db"
    emb_db = data_dir / "embeddings.db"
    if not index_db.exists():
        raise RuntimeError(
            f"Index not built at {index_db}. Run: "
            f"python claude_docs_monitor.py reindex"
        )

    # Resolve since/until once
    from claude_docs_monitor import _parse_relative_date
    since_iso = _parse_relative_date(since) if since else None
    until_iso = _parse_relative_date(until) if until else None

    embedder = EmbeddingCache(emb_db)
    index = DocIndex(index_db, embedder=embedder)
    retriever = HybridRetriever(index, embedder)

    def _notify(stage: str, info: dict | None = None) -> None:
        if progress_callback is not None:
            try:
                progress_callback(stage, info or {})
            except Exception as e:
                _vprint(f"progress_callback error: {e!r}")

    try:
        # 1. PLAN
        _notify("planning")
        _vprint("step 1: PLAN")
        plan = _plan_question(question, scope, since_iso, until_iso, model="sonnet")
        _vprint(f"plan: {len(plan['sub_questions'])} sub-questions")
        _notify("planned", {"sub_questions": len(plan["sub_questions"])})

        # 2. RETRIEVE
        _notify("retrieving")
        _vprint("step 2: RETRIEVE")
        initial = _initial_retrieve(
            plan, retriever, scope, since_iso, until_iso,
            k_per_sub=8,
        )
        _vprint(f"initial evidence: {len(initial)} chunks")
        _notify("retrieved", {"chunks": len(initial)})

        # 3. REASON & GAP-FILL
        _notify("reasoning")
        _vprint("step 3: REASON & GAP-FILL")
        try:
            chosen_ids, turns_used = asyncio.run(
                _reason_and_gap_fill(
                    question, plan, initial, retriever, index,
                    model=model, max_turns=max_loop_turns,
                    target_evidence=min(max_evidence_chunks, len(initial)) or 8,
                )
            )
        except Exception as e:
            _vprint(f"agentic loop failed, using initial evidence: {e!r}")
            chosen_ids = [e.chunk_id for e in initial[:max_evidence_chunks]]
            turns_used = 0
        _notify("reasoned", {"loop_turns": turns_used})

        # Build final evidence list from chosen ids
        evidence_map = {e.chunk_id: e for e in initial}
        final_evidence: list[Evidence] = []
        for cid in chosen_ids[:max_evidence_chunks]:
            if cid in evidence_map:
                final_evidence.append(evidence_map[cid])
            else:
                # Chunk discovered during the loop — fetch it fresh
                c = index.get_chunk(cid)
                if c:
                    final_evidence.append(Evidence(
                        chunk_id=c.id or 0,
                        source_type=c.source_type,
                        source_id=c.source_id,
                        heading_path=c.heading_path,
                        quote=c.content,
                        confidence=0.5,
                        relevance_to="(discovered during reasoning loop)",
                        url=c.url,
                        line_start=c.line_start,
                        line_end=c.line_end,
                        metadata=c.metadata,
                    ))
        # Always have *some* evidence
        if not final_evidence and initial:
            final_evidence = initial[:max_evidence_chunks]
        _vprint(f"final evidence: {len(final_evidence)} chunks")

        # 4. SYNTHESIZE
        _notify("synthesizing")
        _vprint("step 4: SYNTHESIZE")
        report_md = _synthesize(question, plan, final_evidence, model=model)
        try:
            intermediate_dir = output_dir / "intermediate"
            intermediate_dir.mkdir(parents=True, exist_ok=True)
            fp_slug = _slugify(question) or "report"
            fp_ts = time.strftime("%Y%m%d-%H%M%S")
            (intermediate_dir / f"{fp_ts}-{fp_slug}.first-pass.md").write_text(
                report_md + "\n", encoding="utf-8"
            )
        except Exception as e:
            _vprint(f"first-pass dump failed: {e!r}")
        _notify("synthesized", {"chars": len(report_md)})

        # 5. SELF-CRITIQUE (one retry on failure)
        validated = True
        entailment_audit_records: list[dict] = []
        evidence_by_id = {e.chunk_id: e for e in final_evidence}
        critique: dict | None = None
        re_critique: dict | None = None
        if do_self_critique:
            _notify("critiquing")
            _vprint("step 5: SELF-CRITIQUE")
            critique = _self_critique(
                question, report_md, model="sonnet", evidence=final_evidence,
            )
            validated = bool(critique.get("ok", True))
            if not validated:
                _vprint(f"critique flagged: {critique.get('verdict')}")
                missing_enums = critique.get("missing_enumerations") or []
                enum_feedback = ""
                if missing_enums:
                    enum_lines = []
                    for me in missing_enums[:5]:  # cap to avoid prompt bloat
                        miss_items = me.get("missing", [])
                        if not miss_items:
                            continue
                        enum_lines.append(
                            f"  - In chunk {me.get('source_chunk')}, the "
                            f"\"{me.get('enumeration', 'list')}\" enumeration is missing: "
                            f"{miss_items}. Include all of these in your revision."
                        )
                    if enum_lines:
                        enum_feedback = "\nCompleteness gaps to fix:\n" + "\n".join(enum_lines)
                # Single retry: regenerate with the critique appended
                try:
                    retry_md = _synthesize(
                        f"{question}\n\nCritique to address: {critique.get('verdict', '')}\n"
                        f"Uncited claims to fix: {critique.get('uncited_claims', [])}"
                        f"{enum_feedback}",
                        plan,
                        final_evidence,
                        model=model,
                    )
                    report_md = retry_md
                    re_critique = _self_critique(
                        question, report_md, model="sonnet", evidence=final_evidence,
                    )
                    validated = bool(re_critique.get("ok", True))
                except Exception as e:
                    _vprint(f"retry synthesis failed: {e!r}")

        # 5b. Per-citation entailment audit. Cheap (Haiku), but ~30s wall.
        # Independent of self-critique — validates citations against evidence
        # whether or not the critique pass runs. Opt-out via skip_entailment_audit.
        if not skip_entailment_audit:
            _notify("auditing_citations")
            _vprint("step 5b: ENTAILMENT AUDIT")
            try:
                report_md, entailment_audit_records = _entailment_audit(
                    report_md, evidence_by_id, index, model="haiku",
                )
                dropped = sum(
                    1 for r in entailment_audit_records
                    if r.get("action_taken") == "dropped"
                )
                _vprint(f"entailment audit: {dropped} bad citations / "
                        f"{len(entailment_audit_records)} checked")
                if strict_citations and dropped > 0:
                    _notify("revising_citations", {"bad_citations": dropped})
                    _vprint("step 5c: STRICT REVISE PASS")
                    revised = _entailment_revise(
                        question, plan, final_evidence,
                        entailment_audit_records, model=model,
                    )
                    if revised:
                        report_md = revised
                        # Re-audit the revised report
                        report_md, entailment_audit_records = _entailment_audit(
                            report_md, evidence_by_id, index, model="haiku",
                        )
            except Exception as e:
                _vprint(f"entailment audit failed: {e!r}")

        # 6. OUTPUT
        slug = _slugify(question)
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        slug_with_ts = f"{timestamp}-{slug}" if slug else f"{timestamp}-report"
        md_path = output_dir / f"{slug_with_ts}.md"
        json_path = output_dir / f"{slug_with_ts}.json"

        md_path.write_text(report_md + "\n", encoding="utf-8")
        json_payload = {
            "question": question,
            "plan": plan,
            "evidence": [e.to_dict() for e in final_evidence],
            "loop_turns": turns_used,
            "citations_validated": validated,
            "critique": critique,
            "re_critique": re_critique,
            "entailment_audit": entailment_audit_records,
            "strict_citations": strict_citations,
            "elapsed_seconds": time.time() - t0,
            "model": model,
            "scope": scope,
            "since": since_iso,
            "until": until_iso,
        }
        json_path.write_text(json.dumps(json_payload, indent=2), encoding="utf-8")

        return Report(
            question=question,
            plan=plan,
            evidence=final_evidence,
            markdown=report_md,
            citations_validated=validated,
            elapsed_seconds=time.time() - t0,
            loop_turns=turns_used,
            markdown_path=md_path,
            json_path=json_path,
            critique=critique,
            re_critique=re_critique,
        )
    finally:
        retriever.invalidate_dense_cache()
        index.close()
        embedder.close()


__all__ = ["build_report", "Report", "Evidence"]
