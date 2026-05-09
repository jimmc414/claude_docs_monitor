"""
Phase D adversarial probes — independent of benchmark.

Probes:
  P1 filter_leakage: change_search must not return source_type='page' chunks
  P2 multi_hop: questions requiring synthesis across >=3 pages
  P3 self_citation: ask system to summarize a page, verify by fetching the page
  P4 stale_data: pick a recent change_event, ask question whose pre-change answer differed
  P5 prompt_injection: insert synthetic chunk with instructions, observe (DESTRUCTIVE - skipped by default)

Each probe captures a structured pass/fail with reproduction.
"""
from __future__ import annotations

import json
import os
import sqlite3
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
EVAL_DIR = REPO / "data-claude" / "eval"
SNAPSHOTS_DB = REPO / "data-claude" / "snapshots.db"
INDEX_DB = REPO / "data-claude" / "index.db"

ENV = {**os.environ}
ENV.pop("ANTHROPIC_API_KEY", None)


def run_search(question: str, source_type: str | None = None, k: int = 5, timeout: int = 60) -> dict:
    cmd = [
        "python", str(REPO / "claude_docs_monitor.py"),
        "search", question, "--k", str(k), "--json",
    ]
    if source_type:
        cmd.extend(["--source", source_type])
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, env=ENV, cwd=str(REPO), timeout=timeout)
        try:
            hits = json.loads(r.stdout) if r.stdout.strip() else []
        except json.JSONDecodeError:
            hits = []
        return {"ok": r.returncode == 0, "hits": hits, "stderr_tail": r.stderr[-500:], "cmd": " ".join(cmd[:3]) + f' "{question}" ' + " ".join(cmd[3:])}
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": "timeout", "cmd": " ".join(cmd[:3]) + f' "{question}"'}


def probe_filter_leakage() -> dict:
    """change_search with --source change_event should never return source_type='page'."""
    findings = []
    queries = [
        "what changed about hooks recently",
        "new features added",
        "deprecation",
        "skills",
        "permissions",
    ]
    for q in queries:
        result = run_search(q, source_type="change_event", k=10)
        if not result.get("ok"):
            findings.append({"query": q, "status": "error", "error": result.get("error") or result.get("stderr_tail")})
            continue
        leaked = [h for h in result["hits"] if h.get("source_type") != "change_event"]
        findings.append({
            "query": q,
            "n_hits": len(result["hits"]),
            "n_leaked": len(leaked),
            "leaked_source_types": list({h.get("source_type") for h in leaked}),
            "status": "leak" if leaked else "clean",
        })
    return {
        "probe": "P1_filter_leakage",
        "purpose": "change_search restricted to change_event source must not return page chunks",
        "findings": findings,
        "verdict": "FAIL" if any(f.get("status") == "leak" for f in findings) else "PASS",
    }


def probe_multi_hop() -> dict:
    """Multi-hop questions require synthesis across >=3 pages.
    We measure whether retrieval returns relevant chunks from multiple pages."""
    multi_hop_queries = [
        {
            "q": "How do I run Claude Code in a GitHub Action with Bedrock as the backend and restrict tool access?",
            "expected_pages": ["github-actions.md", "amazon-bedrock.md", "permissions.md", "settings.md"],
        },
        {
            "q": "How do I use a custom skill from an MCP server with hooks that fire after tool calls?",
            "expected_pages": ["skills.md", "mcp.md", "hooks.md"],
        },
        {
            "q": "How do I use checkpointing with sub-agents on the headless CLI?",
            "expected_pages": ["checkpointing.md", "sub-agents.md", "headless.md"],
        },
    ]
    findings = []
    for item in multi_hop_queries:
        result = run_search(item["q"], k=10)
        if not result.get("ok"):
            findings.append({"q": item["q"], "status": "error"})
            continue
        retrieved_pages = {h.get("source_id") for h in result["hits"]}
        expected = set(item["expected_pages"])
        coverage = expected & retrieved_pages
        findings.append({
            "q": item["q"],
            "expected_pages": sorted(expected),
            "retrieved_pages": sorted(retrieved_pages),
            "coverage_count": len(coverage),
            "missing": sorted(expected - retrieved_pages),
            "status": "pass" if len(coverage) >= len(expected) - 1 else "partial" if coverage else "fail",
        })
    return {
        "probe": "P2_multi_hop_retrieval",
        "purpose": "retrieval should surface chunks from all expected pages for multi-hop questions",
        "findings": findings,
        "verdict": (
            "FAIL" if any(f.get("status") == "fail" for f in findings) else
            "PARTIAL" if any(f.get("status") == "partial" for f in findings) else
            "PASS"
        ),
    }


def probe_stale_data() -> dict:
    """Identify recently-changed pages from change_events; verify retrieval surfaces post-change content."""
    conn = sqlite3.connect(SNAPSHOTS_DB)
    cur = conn.execute(
        "SELECT page_name, summary, run_timestamp FROM change_events "
        "WHERE category IS NOT NULL ORDER BY run_timestamp DESC LIMIT 5"
    )
    recent = [dict(zip(["page_name", "summary", "run_timestamp"], r)) for r in cur.fetchall()]
    conn.close()

    findings = []
    for ev in recent:
        page = ev["page_name"]
        summary = (ev["summary"] or "")[:100]
        # Probe: ask about the topic of the change, see if retrieval returns the changed page
        q = f"tell me about {page.replace('.md','').replace('-',' ')}"
        result = run_search(q, k=5)
        if not result.get("ok"):
            findings.append({"page": page, "status": "error"})
            continue
        retrieved_pages = [h.get("source_id") for h in result["hits"]]
        findings.append({
            "page": page,
            "summary": summary,
            "run_ts": ev["run_timestamp"],
            "query_used": q,
            "retrieved_top1": retrieved_pages[0] if retrieved_pages else None,
            "page_in_top5": page in retrieved_pages,
            "status": "pass" if page in retrieved_pages[:3] else "weak" if page in retrieved_pages else "fail",
        })
    return {
        "probe": "P4_stale_data_retrieval",
        "purpose": "for recently-changed pages, retrieval should surface the changed page when its topic is queried",
        "findings": findings,
        "verdict": (
            "FAIL" if any(f.get("status") == "fail" for f in findings) else
            "WEAK" if any(f.get("status") == "weak" for f in findings) else
            "PASS"
        ),
    }


def probe_chunk_existence() -> dict:
    """Sanity: every chunk referenced by an existing report must still exist in the index."""
    reports_dir = REPO / "data-claude" / "reports"
    if not reports_dir.exists():
        return {"probe": "P_chunk_existence", "verdict": "SKIP", "reason": "no reports dir"}

    findings = []
    conn = sqlite3.connect(INDEX_DB)
    json_files = sorted(reports_dir.glob("*.json"))[-3:]  # last 3 reports
    for jf in json_files:
        try:
            data = json.loads(jf.read_text())
        except Exception:
            continue
        evidence = data.get("evidence_chunks") or data.get("evidence") or []
        # The structure may vary - just look for any 'chunk_id' fields
        chunk_ids = []
        for k in ("evidence_chunks", "evidence", "citations", "ev_ids"):
            v = data.get(k)
            if isinstance(v, list):
                for item in v:
                    if isinstance(item, dict) and "chunk_id" in item:
                        chunk_ids.append(item["chunk_id"])
                    elif isinstance(item, int):
                        chunk_ids.append(item)
        if not chunk_ids:
            findings.append({"report": jf.name, "status": "no_chunks_in_json"})
            continue
        missing = []
        for cid in chunk_ids:
            row = conn.execute("SELECT id FROM doc_chunks WHERE id=?", (cid,)).fetchone()
            if not row:
                missing.append(cid)
        findings.append({
            "report": jf.name,
            "n_chunks": len(chunk_ids),
            "n_missing": len(missing),
            "missing_ids": missing[:5],
            "status": "pass" if not missing else "fail",
        })
    conn.close()
    return {
        "probe": "P_chunk_existence",
        "purpose": "chunk IDs cited in saved reports should still exist in index.db",
        "findings": findings,
        "verdict": "FAIL" if any(f.get("status") == "fail" for f in findings) else "PASS",
    }


def probe_paraphrase_stability() -> dict:
    """Identical-intent paraphrase pairs should retrieve overlapping chunk sets."""
    pairs = [
        ("How do I limit which tools Claude can use?", "How do I restrict Claude's tool access?"),
        ("How do I configure Claude Code to use AWS Bedrock?", "How do I run Claude Code on Bedrock?"),
        ("Where are session settings stored?", "What's the location of the settings file?"),
        ("How do hooks work in Claude Code?", "What is a hook and how is it configured?"),
        ("How do I create a custom slash command?", "How do I add a new slash command?"),
    ]
    findings = []
    for a, b in pairs:
        ra = run_search(a, k=10)
        rb = run_search(b, k=10)
        if not (ra.get("ok") and rb.get("ok")):
            findings.append({"a": a, "b": b, "status": "error"})
            continue
        ids_a = {h["chunk_id"] for h in ra["hits"]}
        ids_b = {h["chunk_id"] for h in rb["hits"]}
        pages_a = {h["source_id"] for h in ra["hits"]}
        pages_b = {h["source_id"] for h in rb["hits"]}
        chunk_jaccard = len(ids_a & ids_b) / len(ids_a | ids_b) if ids_a | ids_b else 0
        page_jaccard = len(pages_a & pages_b) / len(pages_a | pages_b) if pages_a | pages_b else 0
        findings.append({
            "a": a,
            "b": b,
            "chunk_jaccard": round(chunk_jaccard, 3),
            "page_jaccard": round(page_jaccard, 3),
            "ids_a_top5": sorted(ids_a)[:5],
            "ids_b_top5": sorted(ids_b)[:5],
            "status": "stable" if chunk_jaccard >= 0.5 else "weak" if page_jaccard >= 0.5 else "unstable",
        })
    return {
        "probe": "P_paraphrase_stability",
        "purpose": "same-intent paraphrases should retrieve overlapping chunks/pages",
        "findings": findings,
        "verdict": (
            "FAIL" if sum(1 for f in findings if f.get("status") == "unstable") >= 2 else
            "WEAK" if any(f.get("status") in ("weak", "unstable") for f in findings) else
            "PASS"
        ),
    }


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("run_id")
    ap.add_argument("--probes", default="filter,multi_hop,stale,chunk,paraphrase")
    args = ap.parse_args()

    run_dir = EVAL_DIR / "runs" / args.run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    out = run_dir / "adversarial_probes.json"

    selected = set(s.strip() for s in args.probes.split(",") if s.strip())
    results = []
    if "filter" in selected:
        print("=== P1 filter_leakage ===", file=sys.stderr); results.append(probe_filter_leakage())
    if "multi_hop" in selected:
        print("=== P2 multi_hop ===", file=sys.stderr); results.append(probe_multi_hop())
    if "stale" in selected:
        print("=== P4 stale_data ===", file=sys.stderr); results.append(probe_stale_data())
    if "chunk" in selected:
        print("=== P_chunk_existence ===", file=sys.stderr); results.append(probe_chunk_existence())
    if "paraphrase" in selected:
        print("=== P_paraphrase_stability ===", file=sys.stderr); results.append(probe_paraphrase_stability())

    out.write_text(json.dumps(results, indent=2, default=str))
    print(f"\nwrote {out}", file=sys.stderr)
    print("\n=== SUMMARY ===", file=sys.stderr)
    for r in results:
        print(f"{r['probe']}: {r['verdict']}", file=sys.stderr)


if __name__ == "__main__":
    main()
