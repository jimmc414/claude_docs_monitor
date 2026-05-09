"""
Phase F synthesis — produce severity-ranked findings.md from all artifacts.

Reads:
  - benchmark.jsonl
  - runs/{run_id}/answers.jsonl
  - runs/{run_id}/scores.jsonl
  - runs/{run_id}/adversarial_probes.json
  - runs/{run_id}/ux_findings.md  (if present)

Writes:
  - runs/{run_id}/findings.md  — severity-ranked headline report
  - runs/{run_id}/headline_metrics.json  — machine-readable summary
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
EVAL_DIR = REPO / "data-claude" / "eval"


def load_jsonl(p: Path) -> list[dict]:
    if not p.exists():
        return []
    return [json.loads(line) for line in p.read_text().splitlines() if line.strip()]


def avg(xs):
    xs = [x for x in xs if x is not None]
    return round(sum(xs) / len(xs), 3) if xs else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run_id")
    args = ap.parse_args()

    run_dir = EVAL_DIR / "runs" / args.run_id
    bench = {it["id"]: it for it in load_jsonl(EVAL_DIR / "benchmark.jsonl")}
    answers = {a["id"]: a for a in load_jsonl(run_dir / "answers.jsonl")}
    scores = {s["id"]: s for s in load_jsonl(run_dir / "scores.jsonl")}
    probes = []
    pp = run_dir / "adversarial_probes.json"
    if pp.exists():
        probes = json.loads(pp.read_text())
    inj_path = run_dir / "prompt_injection_probe.json"
    injection = json.loads(inj_path.read_text()) if inj_path.exists() else None
    ux_path = run_dir / "ux_findings.md"
    ux = ux_path.read_text() if ux_path.exists() else ""
    bmk_patches_path = EVAL_DIR / "benchmark_patches.md"
    bmk_patches = bmk_patches_path.read_text() if bmk_patches_path.exists() else ""

    # ===== Headline metrics =====
    by_dim_recall = defaultdict(list)
    by_dim_correct = defaultdict(list)
    by_dim_align = defaultdict(list)
    lure_refused = []
    lure_failed = []
    findings_S1 = []
    findings_S2 = []
    findings_S3 = []
    correctness_dist = defaultdict(int)
    align_dist = defaultdict(int)

    for qid, sc in scores.items():
        item = bench.get(qid, {})
        dim = sc.get("dimension") or item.get("dimension") or "unknown"

        if sc.get("search_recall_at_10") and sc["search_recall_at_10"].get("recall_at_k") is not None:
            by_dim_recall[dim].append(sc["search_recall_at_10"]["recall_at_k"])

        if sc.get("citation_alignment_pass_rate") is not None:
            by_dim_align[dim].append(sc["citation_alignment_pass_rate"])
            for j in sc.get("citation_alignment", []):
                align_dist[j.get("verdict", "unknown")] += 1

        if sc.get("correctness"):
            verdict = sc["correctness"].get("correctness")
            correctness_dist[verdict] += 1
            if verdict in ("correct",):
                by_dim_correct[dim].append(1)
            elif verdict == "partially_correct":
                by_dim_correct[dim].append(0.5)
            elif verdict in ("incorrect", "hallucinated"):
                by_dim_correct[dim].append(0)

        if dim == "hallucination_lure" and sc.get("lure_short_circuit"):
            sc_lure = sc["lure_short_circuit"]
            if sc_lure.get("refused"):
                lure_refused.append(qid)
            else:
                lure_failed.append(qid)

        # ===== Severity findings =====
        # S1: factually wrong cited claim (judge says incorrect/hallucinated and cites a chunk)
        if sc.get("correctness", {}).get("correctness") in ("incorrect", "hallucinated"):
            findings_S1.append({
                "id": qid,
                "dim": dim,
                "question": item.get("question") or sc.get("question"),
                "verdict": sc["correctness"].get("correctness"),
                "reasoning": sc["correctness"].get("reasoning", "")[:400],
                "extra_or_wrong": sc["correctness"].get("extra_or_wrong", []),
            })

        # S1 also: citation marked CONTRADICTS — system cited a chunk that contradicts its claim
        contradicting = [j for j in sc.get("citation_alignment", []) if j.get("verdict") == "contradicts"]
        if contradicting:
            findings_S1.append({
                "id": qid,
                "dim": dim,
                "question": item.get("question") or sc.get("question"),
                "verdict": "contradicting_citation",
                "reasoning": f"{len(contradicting)} citations cite chunks that explicitly contradict the surrounding sentence",
                "contradicting_citations": [
                    {"chunk_id": j["chunk_id"], "sentence": j["sentence"][:200], "judge_reason": j["reasoning"][:300]}
                    for j in contradicting[:3]
                ],
                "extra_or_wrong": sc.get("correctness", {}).get("extra_or_wrong", []),
            })

        # S2: missing critical caveat (correctness=partially_correct AND multiple missing_points)
        if (
            sc.get("correctness", {}).get("correctness") == "partially_correct" and
            len(sc.get("correctness", {}).get("missing_points", [])) >= 2
        ):
            findings_S2.append({
                "id": qid,
                "dim": dim,
                "question": item.get("question") or sc.get("question"),
                "missing_points": sc["correctness"]["missing_points"],
            })

        # S2 also: hallucinated chunk_id
        if sc.get("report_hallucinated_citations"):
            findings_S2.append({
                "id": qid,
                "dim": dim,
                "issue": "hallucinated_citation_id",
                "question": item.get("question") or sc.get("question"),
                "fake_chunk_ids": sc["report_hallucinated_citations"],
            })

        # S2 also: low citation alignment
        if sc.get("citation_alignment_pass_rate") is not None and sc["citation_alignment_pass_rate"] < 0.6:
            findings_S2.append({
                "id": qid,
                "dim": dim,
                "issue": "low_citation_alignment",
                "question": item.get("question") or sc.get("question"),
                "pass_rate": sc["citation_alignment_pass_rate"],
                "weak_citations": [j for j in sc.get("citation_alignment", []) if j.get("verdict") != "supports"][:3],
            })

        # S3: low retrieval recall
        if (
            sc.get("search_recall_at_10", {}).get("recall_at_k") is not None and
            sc["search_recall_at_10"]["recall_at_k"] < 0.5 and
            dim != "hallucination_lure"
        ):
            findings_S3.append({
                "id": qid,
                "dim": dim,
                "question": item.get("question") or sc.get("question"),
                "recall@10": sc["search_recall_at_10"]["recall_at_k"],
                "missing_pages": sc["search_recall_at_10"].get("missing", []),
            })

    # ===== Build markdown =====
    lines = []
    lines.append(f"# Adversarial Review — Findings (run {args.run_id})\n")
    lines.append("Brutal-honesty audit of RAG answer quality across 8 dimensions. Generated from " +
                 f"{len(scores)} scored questions, {len(probes)} probes, " +
                 f"{'plus UX track' if ux else 'no UX track'}.\n")

    lines.append("## Headline metrics\n")
    lines.append("### Retrieval recall@10 by dimension\n")
    lines.append("| Dimension | n | mean recall@10 |")
    lines.append("|---|---|---|")
    for dim, xs in sorted(by_dim_recall.items()):
        lines.append(f"| {dim} | {len(xs)} | {avg(xs)} |")
    lines.append("")

    lines.append("### Factual correctness (report subset)\n")
    if correctness_dist:
        total_c = sum(correctness_dist.values())
        lines.append("| Verdict | n | % |")
        lines.append("|---|---|---|")
        for v in ("correct", "partially_correct", "incorrect", "hallucinated", "judge_error", "judge_parse_error"):
            n = correctness_dist.get(v, 0)
            if n:
                lines.append(f"| {v} | {n} | {round(n/total_c*100,1)}% |")
    else:
        lines.append("_No reports were scored. The report subset may have failed to run._")
    lines.append("")

    lines.append("### Citation alignment (per-citation judge)\n")
    if align_dist:
        total_a = sum(align_dist.values())
        lines.append("| Verdict | n | % |")
        lines.append("|---|---|---|")
        for v in ("supports", "partial", "contradicts", "unrelated", "judge_error", "judge_parse_error"):
            n = align_dist.get(v, 0)
            if n:
                lines.append(f"| {v} | {n} | {round(n/total_a*100,1)}% |")
    else:
        lines.append("_No citations were scored. Reports may not have included citations or report subset failed._")
    lines.append("")

    lines.append("### Hallucination resistance (lures)\n")
    n_lures_with_report = len(lure_refused) + len(lure_failed)
    n_lures_total = sum(1 for r in scores.values() if r.get("dimension") == "hallucination_lure")
    if n_lures_with_report:
        lines.append(f"- Lures with full report run: **{n_lures_with_report}** (of {n_lures_total} total lures)")
        lines.append(f"- Correctly refused (said 'doesn't exist'): **{len(lure_refused)}/{n_lures_with_report}**")
        lines.append(f"- Invented an answer instead: **{len(lure_failed)}/{n_lures_with_report}**")
        if lure_failed:
            lines.append(f"  - Invented-answer IDs: {', '.join(lure_failed)}")
        if n_lures_with_report < n_lures_total:
            lines.append(f"- _Note: search-only retrieval cannot diagnose hallucination — needs synthesis layer; "
                         f"{n_lures_total - n_lures_with_report} lures only had search runs and are unmeasured here._")
    else:
        lines.append(f"_No lure had a full `report` run; hallucination resistance is unmeasured. "
                     f"{n_lures_total} lures had search only._")
    lines.append("")

    lines.append("## Benchmark-quality meta-findings (caught before scoring)\n")
    if bmk_patches:
        # extract the section headers from benchmark_patches.md
        for line in bmk_patches.splitlines():
            if line.startswith("## "):
                lines.append(f"- {line.lstrip('#').strip()}")
        lines.append("")
        lines.append("See `eval/benchmark_patches.md` for full reproduction details.\n")
    else:
        lines.append("_No benchmark-quality issues caught._\n")

    lines.append("## Adversarial probes\n")
    if probes:
        lines.append("| Probe | Verdict | Notes |")
        lines.append("|---|---|---|")
        for p in probes:
            verdict_emoji = {"PASS": "PASS", "PARTIAL": "PARTIAL", "WEAK": "WEAK", "FAIL": "FAIL", "SKIP": "SKIP"}.get(p.get("verdict"), p.get("verdict"))
            note_bits = []
            if p["probe"] == "P1_filter_leakage":
                leaked = sum(1 for f in p["findings"] if f.get("status") == "leak")
                note_bits.append(f"{leaked} of {len(p['findings'])} queries leaked")
            elif p["probe"] == "P2_multi_hop_retrieval":
                pass_n = sum(1 for f in p["findings"] if f.get("status") == "pass")
                note_bits.append(f"{pass_n}/{len(p['findings'])} found all expected pages")
            elif p["probe"] == "P4_stale_data_retrieval":
                pass_n = sum(1 for f in p["findings"] if f.get("status") == "pass")
                note_bits.append(f"{pass_n}/{len(p['findings'])} surfaced changed page in top-3")
            elif p["probe"] == "P_paraphrase_stability":
                stable = sum(1 for f in p["findings"] if f.get("status") == "stable")
                note_bits.append(f"{stable}/{len(p['findings'])} pairs stable (jaccard>=0.5)")
            elif p["probe"] == "P_chunk_existence":
                fails = sum(1 for f in p["findings"] if f.get("status") == "fail")
                note_bits.append(f"{fails} reports cite missing chunks" if fails else "all cited chunks exist")
            lines.append(f"| {p['probe']} | {verdict_emoji} | {'; '.join(note_bits)} |")
    if injection:
        v = injection.get('verdict','?')
        notes_bits = []
        if injection.get("trigger_token_in_report") is True:
            notes_bits.append("synthesizer EMITTED trigger token")
        elif injection.get("trigger_token_in_report") is False:
            notes_bits.append("trigger token NOT emitted")
        if injection.get("injected_chunk_in_evidence"):
            notes_bits.append("injected chunk reached synthesizer")
        if injection.get("injection_in_top5"):
            notes_bits.append("injection chunk in retrieval top-5")
        lines.append(f"| P5_prompt_injection | {v} | {'; '.join(notes_bits)} |")
    lines.append("")
    if injection:
        lines.append("### P5 prompt-injection details\n")
        lines.append(f"- Trigger token: `{injection.get('trigger_token')}`")
        lines.append(f"- Injected chunks indexed: {len(injection.get('injected_chunks',[]))}")
        lines.append(f"- Injection appeared in retrieval top-5: {injection.get('injection_in_top5')}")
        lines.append(f"- Synthesizer cited the injected chunk: {injection.get('injected_chunk_in_evidence')}")
        lines.append(f"- Synthesizer emitted the trigger token: **{injection.get('trigger_token_in_report')}**")
        lines.append(f"- Verdict: **{injection.get('verdict')}**")
        lines.append(f"- Reproduce: `python data-claude/eval/prompt_injection_probe.py <run_id>`\n")

    # ===== Paraphrase stability from benchmark pairs =====
    # bench items have paraphrase_of pointing to partner ID
    pairs = []
    for it in bench.values():
        if it.get("dimension") == "paraphrase_pair" and it.get("paraphrase_of"):
            partner = it["paraphrase_of"]
            if partner < it["id"]:  # avoid duplicates
                pairs.append((partner, it["id"]))

    pp_results = []
    if pairs:
        for a, b in pairs:
            ra = answers.get(a, {}).get("search", {}) if a in answers else {}
            rb = answers.get(b, {}).get("search", {}) if b in answers else {}
            ha = ra.get("hits", []) or []
            hb = rb.get("hits", []) or []
            if not ha or not hb:
                continue
            ids_a = {h.get("chunk_id") for h in ha}
            ids_b = {h.get("chunk_id") for h in hb}
            pages_a = {h.get("source_id") for h in ha}
            pages_b = {h.get("source_id") for h in hb}
            cj = len(ids_a & ids_b) / len(ids_a | ids_b) if (ids_a | ids_b) else 0
            pj = len(pages_a & pages_b) / len(pages_a | pages_b) if (pages_a | pages_b) else 0
            pp_results.append({
                "a": a, "b": b,
                "qa": (bench.get(a, {}).get("question") or "")[:80],
                "qb": (bench.get(b, {}).get("question") or "")[:80],
                "chunk_jaccard": round(cj, 3),
                "page_jaccard": round(pj, 3),
                "status": "stable" if cj >= 0.5 else "weak" if pj >= 0.5 else "unstable",
            })

    if pp_results:
        lines.append("### Paraphrase pair stability (benchmark Q041-Q050)\n")
        lines.append("| pair | chunk Jaccard | page Jaccard | status | A | B |")
        lines.append("|---|---|---|---|---|---|")
        for r in pp_results:
            lines.append(f"| {r['a']}+{r['b']} | {r['chunk_jaccard']} | {r['page_jaccard']} | {r['status']} | {r['qa']!r} | {r['qb']!r} |")
        unstable_pairs = [r for r in pp_results if r["status"] == "unstable"]
        if unstable_pairs:
            lines.append(f"\n**{len(unstable_pairs)}/{len(pp_results)} pairs are UNSTABLE** (chunk Jaccard < 0.5 AND page Jaccard < 0.5).")
            lines.append("Real-world implication: the same question phrased two natural ways gives the synthesizer different evidence; answers can diverge.")
        lines.append("")

    lines.append("## Severity-ranked findings\n")

    lines.append("### S1 — Factually wrong cited claims\n")
    if findings_S1:
        for f in findings_S1[:20]:
            lines.append(f"- **{f['id']}** ({f['dim']}) — {f['verdict'].upper()}")
            lines.append(f"  - Q: {f['question']}")
            lines.append(f"  - Judge: {f['reasoning']}")
            for cc in f.get("contradicting_citations", []) or []:
                lines.append(f"  - Cite c{cc['chunk_id']}: '{cc['sentence']}'")
                lines.append(f"    - judge: {cc['judge_reason']}")
            if f.get("extra_or_wrong"):
                lines.append("  - Wrong claims (canonical-vs-system):")
                for w in f["extra_or_wrong"][:3]:
                    lines.append(f"    - {w}")
            lines.append("")
    else:
        lines.append("_None found in scored set._\n")

    lines.append("### S2 — Missing critical caveats / weak citations / hallucinated citation IDs\n")
    if findings_S2:
        for f in findings_S2[:20]:
            issue = f.get("issue", "missing_points")
            lines.append(f"- **{f['id']}** ({f['dim']}) — {issue}")
            lines.append(f"  - Q: {f['question']}")
            if "missing_points" in f and "issue" not in f:
                for mp in f["missing_points"][:4]:
                    lines.append(f"    - missing: {mp}")
            elif issue == "hallucinated_citation_id":
                lines.append(f"    - fake chunk_ids cited: {f['fake_chunk_ids']}")
            elif issue == "low_citation_alignment":
                lines.append(f"    - alignment pass rate: {f['pass_rate']}")
                for w in f.get("weak_citations", [])[:3]:
                    lines.append(f"    - cite c{w.get('chunk_id')}: {w.get('verdict')} — {w.get('reasoning','')[:120]}")
            lines.append("")
    else:
        lines.append("_None._\n")

    lines.append("### S3 — Retrieval recall failures (recall@10 < 0.5)\n")
    if findings_S3:
        for f in findings_S3[:20]:
            lines.append(f"- **{f['id']}** ({f['dim']}) — recall@10 = {f['recall@10']}")
            lines.append(f"  - Q: {f['question']}")
            lines.append(f"  - missing pages: {f['missing_pages']}")
            lines.append("")
    else:
        lines.append("_None — all questions had ≥50% recall@10._\n")

    lines.append("### S4 — UX friction (from new-hire pass)\n")
    if ux:
        lines.append("See attached `ux_findings.md`. Key items:\n")
        for line in ux.splitlines():
            if line.startswith("## ") or line.startswith("### "):
                lines.append(f"- {line.lstrip('#').strip()}")
        lines.append("")
    else:
        lines.append("_UX track not run or output missing._\n")

    # ===== root-cause summary =====
    lines.append("## Root-cause attribution summary\n")
    lines.append("This is a heuristic mapping from observed failure → likely cause. Use as starting point, not final diagnosis.\n")
    causes = defaultdict(list)
    for f in findings_S1:
        causes["synthesis_or_judgment"].append(f["id"])
    for f in findings_S2:
        if f.get("issue") == "hallucinated_citation_id":
            causes["citation_postprocessing"].append(f["id"])
        elif f.get("issue") == "low_citation_alignment":
            causes["synthesis_picked_wrong_chunk"].append(f["id"])
        else:
            causes["synthesis_incomplete_coverage"].append(f["id"])
    for f in findings_S3:
        causes["retrieval_gap"].append(f["id"])
    if causes:
        for cause, ids in causes.items():
            lines.append(f"- **{cause}**: {len(ids)} cases ({', '.join(sorted(set(ids))[:8])}{'…' if len(set(ids))>8 else ''})")

    lines.append("")
    lines.append("## How to reproduce any finding\n")
    lines.append("Each scored question is reproducible from `answers.jsonl` row. To re-run ID `Q012`:\n")
    lines.append("```bash")
    lines.append("DOCS_MONITOR_EMBED_PROVIDER=ollama DOCS_MONITOR_EMBED_MODEL=nomic-embed-text \\")
    lines.append("  python claude_docs_monitor.py search \"<question text from benchmark.jsonl>\" --k 10 --json")
    lines.append("```\n")
    lines.append("For report runs, use `report` instead of `search` and refer to `--report-ids` flag in `runner.py`.\n")

    out_md = run_dir / "findings.md"
    out_md.write_text("\n".join(lines))

    # ===== headline metrics JSON =====
    headline = {
        "run_id": args.run_id,
        "n_scored": len(scores),
        "n_benchmark": len(bench),
        "recall_at_10_by_dim": {d: avg(xs) for d, xs in by_dim_recall.items()},
        "correctness_dist": dict(correctness_dist),
        "alignment_dist": dict(align_dist),
        "lure_refused": len(lure_refused),
        "lure_failed": len(lure_failed),
        "n_S1": len(findings_S1),
        "n_S2": len(findings_S2),
        "n_S3": len(findings_S3),
        "probe_verdicts": {p["probe"]: p.get("verdict") for p in probes},
    }
    (run_dir / "headline_metrics.json").write_text(json.dumps(headline, indent=2))

    print(f"wrote {out_md}")
    print(f"wrote {run_dir / 'headline_metrics.json'}")


if __name__ == "__main__":
    main()
