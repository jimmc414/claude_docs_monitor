"""
Phase C scorer — Validator + Oracle (LLM-as-judge).

Scoring pipeline:
  1. Static metrics (no LLM): Recall@k, page_overlap, hallucination_short_circuit
  2. Citation alignment per [^cN]: fetch chunk text, ask LLM "does it entail the sentence?"
  3. Factual correctness: ask LLM to compare answer vs canonical
  4. Coverage gap: ask LLM to list canonical points absent from answer
  5. Per-question composite verdict + severity tag

Outputs scores.jsonl + summary.json.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
EVAL_DIR = REPO / "data-claude" / "eval"
INDEX_DB = REPO / "data-claude" / "index.db"
sys.path.insert(0, str(REPO))

# Strip API key so SDK uses Max OAuth
os.environ.pop("ANTHROPIC_API_KEY", None)

from llm_backend import call_claude  # type: ignore


def get_chunk(chunk_id: int) -> dict | None:
    conn = sqlite3.connect(INDEX_DB)
    conn.row_factory = sqlite3.Row
    row = conn.execute(
        "SELECT id, source_type, source_id, heading_path, content, line_start, line_end "
        "FROM doc_chunks WHERE id=?", (chunk_id,)
    ).fetchone()
    conn.close()
    return dict(row) if row else None


def parse_citations(md: str) -> list[tuple[int, str]]:
    """Return list of (chunk_id, cited_sentence).

    Citations like `[^cN]` typically follow a sentence-ending punctuation:
    "Sentence text. [^c123][^c456] Next sentence." The cited sentence is the
    one ending just before the citation cluster — NOT the gap between cluster
    and following sentence. Algorithm:
      1. Get window of text before the citation.
      2. Strip trailing whitespace + adjacent citation tags so we land at the
         end of the sentence that owns this citation.
      3. Walk back to the previous sentence boundary (. ! ? \\n) to find the
         start of that sentence.
    """
    out = []
    pattern = re.compile(r"\[\^c(\d+)\]")
    for m in pattern.finditer(md):
        cid = int(m.group(1))
        start = m.start()
        ctx_start = max(0, start - 800)
        ctx = md[ctx_start:start]
        # strip any trailing citations + whitespace + punctuation gap so we land at the sentence end
        ctx_stripped = re.sub(r"(\[\^c\d+\][\s,;]*)+\s*$", "", ctx).rstrip()
        if not ctx_stripped:
            # fallback: use last 200 chars before citation
            sentence_raw = ctx[-200:]
        else:
            # find the previous sentence boundary (the one ending the prior sentence,
            # not the one ending this sentence); ctx_stripped already ends at "." (or similar)
            # so we want the SECOND-to-last terminator
            # Search positions of all terminators
            positions = []
            for sep in (". ", "! ", "? ", "\n"):
                idx = ctx_stripped.rfind(sep)
                if idx >= 0:
                    positions.append(idx + len(sep) - 1)  # position of the space
            # ctx_stripped's final char might be '.', '!', '?' — if so, ignore it as a boundary
            terminators = [p for p in positions if p < len(ctx_stripped) - 1]
            sent_start = (max(terminators) + 1) if terminators else 0
            sentence_raw = ctx_stripped[sent_start:]
        # strip any embedded citations and normalize whitespace
        sentence_clean = pattern.sub("", sentence_raw).strip()
        sentence_clean = re.sub(r"\s+", " ", sentence_clean)
        out.append((cid, sentence_clean))
    return out


def static_recall_at_k(expected_pages: list[str], hits: list[dict], k: int = 10) -> dict:
    """Recall@k over expected source pages."""
    if not expected_pages:
        return {"recall_at_k": None, "k": k}
    retrieved = [h.get("source_id") for h in hits[:k]]
    expected_set = set(expected_pages)
    retrieved_set = set(retrieved)
    hits_in = expected_set & retrieved_set
    return {
        "recall_at_k": round(len(hits_in) / len(expected_set), 3),
        "k": k,
        "expected": sorted(expected_set),
        "retrieved": retrieved,
        "missing": sorted(expected_set - retrieved_set),
    }


def hallucination_short_circuit(answer_text: str) -> dict:
    """For lure questions, check if answer contains 'does not exist' phrase."""
    al = answer_text.lower() if answer_text else ""
    refusal_signals = [
        "does not exist", "doesn't exist", "no documentation", "not documented",
        "no such", "not found in", "cannot find", "not available", "i don't see",
        "i don't find", "no mention", "no reference", "not present",
        "could not find", "couldn't find", "no information",
        "does not appear in", "is not part of the documented",
        "does not appear to exist",
    ]
    return {
        "refused": any(sig in al for sig in refusal_signals),
        "matched_signal": next((sig for sig in refusal_signals if sig in al), None),
    }


def llm_judge_citation(sentence: str, chunk: dict, model: str = "sonnet") -> dict:
    """Does the chunk content support the sentence? Returns {verdict, reasoning}."""
    prompt = f"""You are auditing a research report for citation accuracy. The report contains this sentence with a citation:

SENTENCE: {sentence}

The citation points to this evidence chunk (from `{chunk['source_id']}`):
---
{chunk['content'][:3000]}
---

Question: Does the chunk content directly support the factual claim(s) in the sentence?

Respond ONLY with valid JSON in this exact shape:
{{"verdict": "supports|partial|contradicts|unrelated", "reasoning": "one short sentence"}}

- "supports": chunk explicitly entails the claim
- "partial": chunk relates but doesn't fully entail (e.g., mentions topic but not the specific detail)
- "contradicts": chunk says the opposite
- "unrelated": chunk is about a different topic"""

    schema_str = json.dumps({
        "type": "object",
        "properties": {
            "verdict": {"type": "string", "enum": ["supports", "partial", "contradicts", "unrelated"]},
            "reasoning": {"type": "string"},
        },
        "required": ["verdict", "reasoning"],
    })
    try:
        result = call_claude(prompt=prompt, model=model, json_schema=schema_str)
        try:
            return json.loads(result)
        except json.JSONDecodeError:
            m = re.search(r"\{.*\}", result, re.DOTALL)
            return json.loads(m.group(0)) if m else {"verdict": "judge_parse_error", "reasoning": result[:200]}
    except Exception as e:
        return {"verdict": "judge_error", "reasoning": str(e)[:200]}


def llm_judge_correctness(question: str, expected_answer: str, system_answer: str, model: str = "sonnet") -> dict:
    """Compare system answer to canonical."""
    prompt = f"""You are an expert reviewer comparing a RAG system's answer to a canonical reference answer.

QUESTION: {question}

CANONICAL ANSWER (ground truth):
{expected_answer}

SYSTEM ANSWER:
{system_answer[:4000]}

Score the system answer on factual correctness AND coverage versus the canonical answer:

Respond ONLY with valid JSON:
{{"correctness": "correct|partially_correct|incorrect|hallucinated", "missing_points": ["point1", "point2"], "extra_or_wrong": ["..."], "reasoning": "one short paragraph"}}

- "correct": fully aligned, no false claims, all major points present
- "partially_correct": main thrust correct but missing critical points or has minor errors
- "incorrect": main claim wrong or contradicts canonical
- "hallucinated": invents specific facts (function names, flags, behaviors) not in canonical

`missing_points` lists canonical-answer points absent from system answer.
`extra_or_wrong` lists claims in system answer that are wrong, unsupported, or invented."""

    schema_str = json.dumps({
        "type": "object",
        "properties": {
            "correctness": {"type": "string", "enum": ["correct", "partially_correct", "incorrect", "hallucinated"]},
            "missing_points": {"type": "array", "items": {"type": "string"}},
            "extra_or_wrong": {"type": "array", "items": {"type": "string"}},
            "reasoning": {"type": "string"},
        },
        "required": ["correctness", "reasoning"],
    })
    try:
        result = call_claude(prompt=prompt, model=model, json_schema=schema_str)
        try:
            return json.loads(result)
        except json.JSONDecodeError:
            m = re.search(r"\{.*\}", result, re.DOTALL)
            return json.loads(m.group(0)) if m else {"correctness": "judge_parse_error", "reasoning": result[:200]}
    except Exception as e:
        return {"correctness": "judge_error", "reasoning": str(e)[:200]}


def score_one(item: dict, answer_row: dict, model: str = "sonnet", judge_max_cites: int = 6) -> dict:
    """Score a single (question, answer) pair across all metrics."""
    scores = {
        "id": item["id"],
        "dimension": item.get("dimension"),
        "difficulty": item.get("difficulty"),
        "question": item["question"],
    }

    # Static metrics on search results
    search = answer_row.get("search") or {}
    if search.get("ok") and search.get("hits"):
        scores["search_recall_at_10"] = static_recall_at_k(item.get("expected_pages", []), search["hits"], k=10)
        scores["search_recall_at_5"] = static_recall_at_k(item.get("expected_pages", []), search["hits"], k=5)
        scores["search_top1_page"] = search["hits"][0].get("source_id") if search["hits"] else None
    else:
        scores["search_error"] = search.get("error") or search.get("stderr_tail", "")[:200]

    # Report metrics
    report = answer_row.get("report") or {}
    if report.get("ok") and report.get("report_md_text"):
        md_text = report["report_md_text"]
        report_data = report.get("report_json_data") or {}
        evidence_chunks = report_data.get("evidence", [])
        evidence_by_id = {e["chunk_id"]: e for e in evidence_chunks}

        # parse citations
        citations = parse_citations(md_text)
        scores["report_n_citations"] = len(citations)
        scores["report_n_unique_chunks_cited"] = len(set(c[0] for c in citations))
        scores["report_evidence_count"] = len(evidence_chunks)

        # check for hallucinated chunk_ids
        hallucinated = [cid for cid, _ in citations if cid not in evidence_by_id]
        scores["report_hallucinated_citations"] = list(set(hallucinated))[:5]

        # citation alignment - sample up to N citations to score
        valid_citations = [(cid, sent) for cid, sent in citations if cid in evidence_by_id]
        sampled = valid_citations[:judge_max_cites]
        align_judgements = []
        for cid, sent in sampled:
            chunk = evidence_by_id[cid]
            # Use the chunk content from the report's evidence (already has 'quote') OR fetch fresh from index
            chunk_for_judge = {
                "source_id": chunk.get("source_id"),
                "content": chunk.get("quote") or chunk.get("content") or "",
            }
            j = llm_judge_citation(sent, chunk_for_judge, model=model)
            align_judgements.append({"chunk_id": cid, "verdict": j.get("verdict"), "reasoning": j.get("reasoning"), "sentence": sent[:150]})
        scores["citation_alignment"] = align_judgements
        scores["citation_alignment_pass_rate"] = round(
            sum(1 for j in align_judgements if j.get("verdict") == "supports") / len(align_judgements), 3
        ) if align_judgements else None

        # factual correctness
        if item.get("expected_answer"):
            corr = llm_judge_correctness(item["question"], item["expected_answer"], md_text, model=model)
            scores["correctness"] = corr

        # hallucination short-circuit for lures
        if item.get("dimension") == "hallucination_lure":
            scores["lure_short_circuit"] = hallucination_short_circuit(md_text)

    elif report.get("error"):
        scores["report_error"] = report.get("error")
    elif report and not report.get("ok"):
        scores["report_error"] = (report.get("stderr_tail") or "")[:300]

    return scores


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run_id")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--ids", default="", help="comma-separated Q-IDs to score")
    ap.add_argument("--model", default="sonnet")
    args = ap.parse_args()

    bench_path = EVAL_DIR / "benchmark.jsonl"
    items = {}
    for line in bench_path.read_text().splitlines():
        if line.strip():
            it = json.loads(line)
            items[it["id"]] = it

    run_dir = EVAL_DIR / "runs" / args.run_id
    # Merge from both files: answers.jsonl (search) and reports.jsonl (reports)
    answers: dict[str, dict] = {}
    for fname in ("answers.jsonl", "reports.jsonl"):
        path = run_dir / fname
        if not path.exists():
            continue
        for line in path.read_text().splitlines():
            if line.strip():
                r = json.loads(line)
                qid = r["id"]
                if qid not in answers:
                    answers[qid] = r
                else:
                    # merge: prefer non-null fields from later rows
                    for k, v in r.items():
                        if v is not None:
                            answers[qid][k] = v
    if not answers:
        print(f"no answer rows found in {run_dir}", file=sys.stderr); sys.exit(1)

    targets = list(items.keys())
    if args.ids:
        targets = [t.strip() for t in args.ids.split(",") if t.strip()]
    if args.limit:
        targets = targets[: args.limit]

    out_path = run_dir / "scores.jsonl"
    n = len(targets)
    print(f"scoring {n} questions, output -> {out_path}", file=sys.stderr)
    with open(out_path, "a") as f:
        for i, qid in enumerate(targets, 1):
            if qid not in items:
                print(f"[{i}/{n}] {qid}: NOT IN BENCHMARK", file=sys.stderr); continue
            if qid not in answers:
                print(f"[{i}/{n}] {qid}: NO ANSWER ROW", file=sys.stderr); continue
            print(f"[{i}/{n}] {qid} ({items[qid].get('dimension')})", file=sys.stderr)
            scores = score_one(items[qid], answers[qid], model=args.model)
            f.write(json.dumps(scores) + "\n"); f.flush()

    print(f"\ndone. scoring written to {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
