"""Diagnostic: re-run the 5 paraphrase pairs with expand/rerank toggled.

Compares:
  - default search (expand+rerank ON) — what the standard probe measures
  - dense-only (expand+rerank OFF) — isolates the embedding contribution

Use to determine if voyage-4-large's paraphrase win is being washed out by
pipeline stochasticity (expand=Haiku, rerank=Claude scoring against literal query).
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
try:
    from dotenv import load_dotenv; load_dotenv(REPO / ".env")
except ImportError:
    pass
os.environ.pop("ANTHROPIC_API_KEY", None)

ENV = {**os.environ}
ENV.pop("ANTHROPIC_API_KEY", None)

PAIRS = [
    ("How do I limit which tools Claude can use?",
     "How do I restrict Claude's tool access?"),
    ("How do I configure Claude Code to use AWS Bedrock?",
     "How do I run Claude Code on Bedrock?"),
    ("Where are session settings stored?",
     "What's the location of the settings file?"),
    ("How do hooks work in Claude Code?",
     "What is a hook and how is it configured?"),
    ("How do I create a custom slash command?",
     "How do I add a new slash command?"),
]


def search(query: str, no_expand: bool, no_rerank: bool, k: int = 5) -> list[dict]:
    cmd = ["python", str(REPO / "claude_docs_monitor.py"),
           "search", query, "--k", str(k), "--json"]
    if no_expand: cmd.append("--no-expand")
    if no_rerank: cmd.append("--no-rerank")
    r = subprocess.run(cmd, capture_output=True, text=True, env=ENV, cwd=str(REPO), timeout=120)
    if r.returncode != 0:
        return []
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return []


def jaccard(a: list, b: list) -> float:
    sa, sb = set(a), set(b)
    return len(sa & sb) / len(sa | sb) if (sa or sb) else 1.0


def main():
    print(f"\n{'Pair':<60} | {'Default':>8} | {'NoExp':>8} | {'NoRer':>8} | {'NoBoth':>8}")
    print("-" * 100)
    rows = []
    for qa, qb in PAIRS:
        label = (qa[:30] + "/" + qb[:25])[:60]
        results = []
        for no_expand, no_rerank in [(False, False), (True, False), (False, True), (True, True)]:
            ra = [h["chunk_id"] for h in search(qa, no_expand, no_rerank)]
            rb = [h["chunk_id"] for h in search(qb, no_expand, no_rerank)]
            results.append(jaccard(ra, rb))
        print(f"{label:<60} | {results[0]:>8.3f} | {results[1]:>8.3f} | {results[2]:>8.3f} | {results[3]:>8.3f}")
        rows.append(results)

    means = [sum(c)/len(c) for c in zip(*rows)]
    print("-" * 100)
    print(f"{'MEAN':<60} | {means[0]:>8.3f} | {means[1]:>8.3f} | {means[2]:>8.3f} | {means[3]:>8.3f}")
    print(f"\nLegend: Default=expand+rerank, NoExp=no query expansion, NoRer=no rerank, NoBoth=neither")


if __name__ == "__main__":
    main()
