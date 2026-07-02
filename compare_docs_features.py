#!/usr/bin/env python3
"""Full-corpus feature comparison for Claude, Gemini, and Codex docs."""

from __future__ import annotations

import argparse
import csv
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

RUBRIC_VERSION = "1.0"
RUBRIC_DOC_PATH = Path("DOCS_COMPARISON_RUBRIC.md")

TOOL_CONFIGS: dict[str, dict[str, Any]] = {
    "claude": {
        "label": "Claude",
        "pages_dir": Path("data-claude/pages"),
        "history_md": Path("data-claude/history.md"),
        "mapper": "claude",
    },
    "gemini": {
        "label": "Gemini",
        "pages_dir": Path("data-gemini/pages"),
        "history_md": Path("data-gemini/history.md"),
        "mapper": "gemini",
    },
    "codex": {
        "label": "Codex",
        "pages_dir": Path("data-codex/pages"),
        "history_md": Path("data-codex/history.md"),
        "mapper": "codex",
    },
}

CATEGORIES: dict[str, dict[str, Any]] = {
    "core_onboarding": {"label": "Core Onboarding and Command Surface", "weight": 15},
    "power_user_depth": {"label": "Power-User Workflow Depth", "weight": 20},
    "automation_integrations": {"label": "Automation and Integrations", "weight": 18},
    "extensibility_customization": {"label": "Extensibility and Customization", "weight": 15},
    "security_governance": {"label": "Security and Governance", "weight": 17},
    "enterprise_operations": {"label": "Enterprise and Operations", "weight": 10},
    "docs_reliability": {"label": "Documentation Reliability", "weight": 5},
}

FEATURES: list[dict[str, Any]] = [
    {
        "id": "onboarding_installation",
        "name": "Onboarding, installation, and first-run setup",
        "category": "core_onboarding",
        "weight": 4,
        "explicit_filename": [r"quickstart", r"get-started", r"installation", r"\bsetup\b", r"overview"],
        "explicit_content": [r"quickstart", r"install", r"getting started", r"first session"],
        "implied_content": [r"prerequisites", r"authenticate", r"requirements"],
    },
    {
        "id": "command_surface_reference",
        "name": "CLI command/reference depth",
        "category": "core_onboarding",
        "weight": 4,
        "explicit_filename": [
            r"cli-reference",
            r"cli__reference",
            r"\bcommands\.md$",
            r"\breference\.md$",
            r"slash-commands",
            r"\bcli\.md$",
        ],
        "explicit_content": [r"command reference", r"slash command", r"usage", r"options"],
        "implied_content": [r"flags?", r"examples?", r"syntax"],
    },
    {
        "id": "workflow_playbooks_examples",
        "name": "Workflow playbooks, examples, and guides",
        "category": "core_onboarding",
        "weight": 4,
        "explicit_filename": [r"common-workflows", r"workflows", r"examples", r"tutorial", r"explore", r"best-practices"],
        "explicit_content": [r"workflow", r"best practices", r"step-by-step", r"guide"],
        "implied_content": [r"example", r"how to", r"recommended"],
    },
    {
        "id": "troubleshooting_basics",
        "name": "Troubleshooting and FAQ coverage",
        "category": "core_onboarding",
        "weight": 3,
        "explicit_filename": [r"troubleshooting", r"faq", r"uninstall"],
        "explicit_content": [r"troubleshoot", r"known issue", r"diagnostic", r"common problems?"],
        "implied_content": [r"error", r"fix", r"recover"],
    },
    {
        "id": "planning_multi_agent",
        "name": "Planning, delegation, and multi-agent orchestration",
        "category": "power_user_depth",
        "weight": 5,
        "explicit_filename": [r"plan-mode", r"planning", r"sub-?agents?", r"multi-agent", r"agent-teams", r"agent-approvals-security"],
        "explicit_content": [r"plan mode", r"subagent", r"multi-agent", r"delegate"],
        "implied_content": [r"parallel", r"orchestr", r"handoff"],
    },
    {
        "id": "memory_session_state",
        "name": "Memory, session state, and long-running continuity",
        "category": "power_user_depth",
        "weight": 5,
        "explicit_filename": [r"\bmemory\b", r"checkpointing", r"session-management", r"rewind", r"worktrees?", r"statusline"],
        "explicit_content": [r"session", r"checkpoint", r"resume", r"memory"],
        "implied_content": [r"state", r"history", r"persist"],
    },
    {
        "id": "review_pr_execution",
        "name": "Code review and PR/MR execution workflows",
        "category": "power_user_depth",
        "weight": 5,
        "explicit_filename": [r"review", r"github-actions?", r"github-action", r"issue-and-pr-automation", r"gitlab", r"remote-control", r"desktop"],
        "explicit_content": [r"pull request", r"code review", r"auto-merge", r"merge request"],
        "implied_content": [r"review", r"approve", r"branch"],
    },
    {
        "id": "headless_noninteractive",
        "name": "Headless and non-interactive operation modes",
        "category": "power_user_depth",
        "weight": 5,
        "explicit_filename": [r"headless", r"noninteractive", r"app-server"],
        "explicit_content": [r"non-?interactive", r"headless", r"stdin", r"json output", r"batch"],
        "implied_content": [r"pipeline", r"automation", r"without ui"],
    },
    {
        "id": "ci_cd_and_scheduled_automation",
        "name": "CI/CD and scheduled automation",
        "category": "automation_integrations",
        "weight": 6,
        "explicit_filename": [r"github-actions?", r"github-action", r"gitlab", r"issue-and-pr-automation", r"scheduled-tasks", r"automations", r"automation"],
        "explicit_content": [r"ci/?cd", r"scheduled", r"cron", r"automation", r"pipeline"],
        "implied_content": [r"trigger", r"job", r"workflow"],
    },
    {
        "id": "ecosystem_service_integrations",
        "name": "Service integrations and partner ecosystem",
        "category": "automation_integrations",
        "weight": 6,
        "explicit_filename": [
            r"integrations",
            r"third-party-integrations",
            r"slack",
            r"linear",
            r"amazon-bedrock",
            r"google-vertex",
            r"microsoft-foundry",
            r"llm-gateway",
        ],
        "explicit_content": [r"integration", r"connector", r"slack", r"linear", r"bedrock", r"vertex", r"foundry"],
        "implied_content": [r"oauth", r"external service", r"third-party"],
    },
    {
        "id": "mcp_tooling_connectivity",
        "name": "MCP and external tooling connectivity",
        "category": "automation_integrations",
        "weight": 6,
        "explicit_filename": [r"\bmcp\b", r"mcp-server", r"mcp-setup"],
        "explicit_content": [r"model context protocol", r"mcp server", r"/mcp"],
        "implied_content": [r"tool server", r"resources", r"tooling"],
    },
    {
        "id": "skills_plugins_extensions",
        "name": "Skills, plugins, and extension ecosystem",
        "category": "extensibility_customization",
        "weight": 5,
        "explicit_filename": [r"\bskills?\b", r"plugins?", r"extensions?", r"creating-skills", r"activate-skill", r"discover-plugins"],
        "explicit_content": [r"skill", r"plugin", r"extension", r"marketplace"],
        "implied_content": [r"custom tool", r"integration package", r"agent capability"],
    },
    {
        "id": "custom_instructions_prompts_rules",
        "name": "Custom prompts, command macros, and rule files",
        "category": "extensibility_customization",
        "weight": 5,
        "explicit_filename": [r"custom-prompts", r"custom-commands", r"\brules\b", r"gemini-md", r"output-styles", r"system-prompt"],
        "explicit_content": [r"custom prompt", r"custom command", r"rule", r"instruction file"],
        "implied_content": [r"persona", r"policy text", r"prompt template"],
    },
    {
        "id": "configuration_model_controls",
        "name": "Deep configuration, model controls, and keybindings",
        "category": "extensibility_customization",
        "weight": 5,
        "explicit_filename": [
            r"settings",
            r"config",
            r"configuration",
            r"keybindings",
            r"model-routing",
            r"generation-settings",
            r"model-config",
            r"trusted-folders",
            r"policy-engine",
        ],
        "explicit_content": [r"configuration", r"settings", r"keybinding", r"model", r"schema"],
        "implied_content": [r"environment variable", r"defaults", r"override"],
    },
    {
        "id": "sandbox_permission_controls",
        "name": "Permission models and sandbox controls",
        "category": "security_governance",
        "weight": 6,
        "explicit_filename": [r"permissions", r"sandbox", r"sandboxing", r"agent-approvals-security", r"trusted-folders", r"policy-engine"],
        "explicit_content": [r"permission", r"sandbox", r"approval", r"allowlist", r"trusted folder"],
        "implied_content": [r"restricted", r"deny", r"enforce"],
    },
    {
        "id": "security_threat_safety",
        "name": "Security, safety, and threat-model depth",
        "category": "security_governance",
        "weight": 6,
        "explicit_filename": [r"security", r"threat-model", r"cyber-safety", r"auth", r"authentication", r"zero-data-retention", r"data-usage"],
        "explicit_content": [r"threat model", r"security", r"cyber", r"authentication", r"safety"],
        "implied_content": [r"risk", r"mitigation", r"vulnerability"],
    },
    {
        "id": "governance_compliance_policy",
        "name": "Governance, compliance, and policy guidance",
        "category": "security_governance",
        "weight": 5,
        "explicit_filename": [r"governance", r"legal-and-compliance", r"tos-privacy", r"managed-configuration", r"server-managed-settings", r"enterprise"],
        "explicit_content": [r"governance", r"compliance", r"terms", r"policy", r"retention"],
        "implied_content": [r"audit", r"regulatory", r"controls"],
    },
    {
        "id": "enterprise_admin_controls",
        "name": "Enterprise admin setup and managed controls",
        "category": "enterprise_operations",
        "weight": 4,
        "explicit_filename": [r"enterprise", r"admin-setup", r"managed-configuration", r"agent-teams", r"llm-gateway", r"microsoft-foundry", r"google-vertex", r"amazon-bedrock"],
        "explicit_content": [r"enterprise", r"organization", r"admin", r"sso", r"managed"],
        "implied_content": [r"owner role", r"rollout", r"workspace"],
    },
    {
        "id": "pricing_quota_cost",
        "name": "Pricing, quota, and cost transparency",
        "category": "enterprise_operations",
        "weight": 3,
        "explicit_filename": [r"pricing", r"quota-and-pricing", r"costs"],
        "explicit_content": [r"pricing", r"quota", r"cost", r"billing", r"spend"],
        "implied_content": [r"usage limit", r"rate limit", r"plan"],
    },
    {
        "id": "telemetry_analytics_monitoring",
        "name": "Telemetry, analytics, and monitoring",
        "category": "enterprise_operations",
        "weight": 3,
        "explicit_filename": [r"telemetry", r"analytics", r"monitoring-usage"],
        "explicit_content": [r"telemetry", r"analytics", r"metrics", r"monitoring", r"opentelemetry"],
        "implied_content": [r"dashboard", r"logs", r"observability"],
    },
]

UNIQUE_SIGNAL_PATTERNS: dict[str, list[dict[str, str]]] = {
    "claude": [
        {"label": "Desktop-first IDE/app experience", "pattern": r"desktop|vs-code|jetbrains|chrome"},
        {"label": "Plugin marketplace and plugin tooling", "pattern": r"plugin|discover-plugins"},
        {"label": "Cloud provider integration docs", "pattern": r"amazon-bedrock|google-vertex|microsoft-foundry|llm-gateway"},
        {"label": "Remote control and web surface docs", "pattern": r"remote-control|claude-code-on-the-web"},
        {"label": "Zero-data-retention and analytics detail", "pattern": r"zero-data-retention|analytics|monitoring-usage"},
    ],
    "gemini": [
        {"label": "Plan mode and task planning workflows", "pattern": r"plan-mode|task-planning|planning"},
        {"label": "Policy engine and trusted folder controls", "pattern": r"policy-engine|trusted-folders"},
        {"label": "Web tooling guidance", "pattern": r"web-search|web-fetch|web-tools"},
        {"label": "Extension authoring lifecycle", "pattern": r"extensions|writing-extensions|releasing"},
        {"label": "Tooling docs for ask-user/internal-docs", "pattern": r"ask-user|internal-docs|activate-skill"},
    ],
    "codex": [
        {"label": "Codex cloud environments and internet policy", "pattern": r"cloud|cloud__environments|cloud__internet-access"},
        {"label": "App server and noninteractive execution", "pattern": r"app-server|noninteractive"},
        {"label": "Worktree-centric execution model", "pattern": r"app__worktrees|worktrees"},
        {"label": "Threat model and cyber safety depth", "pattern": r"security__threat-model|concepts__cyber-safety"},
        {"label": "Agents.md and Agents SDK guidance", "pattern": r"guides__agents-md|guides__agents-sdk"},
        {"label": "Feature maturity and OSS positioning", "pattern": r"feature-maturity|open-source|community__codex-for-oss"},
    ],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compare full documentation feature sets for Claude/Gemini/Codex")
    parser.add_argument(
        "--output-dir",
        default="data-analysis/compare-docs",
        help="Directory for generated artifacts (default: data-analysis/compare-docs)",
    )
    parser.add_argument(
        "--format",
        choices=["md", "json", "both"],
        default="both",
        help="Output format to write (default: both)",
    )
    parser.add_argument(
        "--strict-rubric",
        action="store_true",
        help="Fail if DOCS_COMPARISON_RUBRIC.md does not contain the expected rubric version",
    )
    return parser.parse_args()


def map_url_to_filename_claude(url: str) -> str:
    path = url.split("/docs/en/", 1)[-1] if "/docs/en/" in url else url.rsplit("/", 1)[-1]
    if not path.endswith(".md"):
        path = path.rstrip("/").replace("/", "_") + ".md"
    return path


def map_url_to_filename_gemini(url: str) -> str:
    path = url.rsplit("/", 1)[-1]
    if not path.endswith(".md"):
        path = path.rstrip("/").replace("/", "_") + ".md"
    return path


def map_url_to_filename_codex(url: str) -> str:
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    if path.startswith("codex/"):
        path = path[len("codex/") :]
    if path.startswith("docs/en/"):
        path = path[len("docs/en/") :]

    if not path:
        name = "index"
    elif path.endswith(".md"):
        name = path[:-3]
    else:
        name = path

    name = name.replace("/", "__")
    if parsed.query:
        query = re.sub(r"[^A-Za-z0-9]+", "_", parsed.query).strip("_")
        if query:
            name = f"{name}__q__{query}"

    name = re.sub(r"[^A-Za-z0-9._-]+", "_", name).strip("._")
    if not name:
        name = "page"
    return f"{name}.md"


def get_url_mapper(mapper_name: str):
    if mapper_name == "claude":
        return map_url_to_filename_claude
    if mapper_name == "gemini":
        return map_url_to_filename_gemini
    if mapper_name == "codex":
        return map_url_to_filename_codex
    raise ValueError(f"Unknown mapper: {mapper_name}")


def parse_history_urls(history_path: Path) -> list[str]:
    if not history_path.exists():
        return []
    urls: list[str] = []
    for line in history_path.read_text(encoding="utf-8", errors="ignore").splitlines():
        match = re.match(r"^-\s+(https?://\S+)", line.strip())
        if match:
            urls.append(match.group(1))
    # Preserve order while deduplicating.
    return list(dict.fromkeys(urls))


def load_tool_corpus(tool_key: str, cfg: dict[str, Any]) -> dict[str, Any]:
    pages_dir = cfg["pages_dir"]
    page_paths = sorted(pages_dir.glob("*.md")) if pages_dir.exists() else []

    pages: dict[str, str] = {}
    newest_mtime = None
    for path in page_paths:
        text = path.read_text(encoding="utf-8", errors="ignore")
        pages[path.name] = text.lower()
        mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
        if newest_mtime is None or mtime > newest_mtime:
            newest_mtime = mtime

    history_urls = parse_history_urls(cfg["history_md"])
    mapper = get_url_mapper(cfg["mapper"])
    mapped = [mapper(url) for url in history_urls]
    expected_unique = len(set(mapped))
    collision_count = max(0, len(mapped) - expected_unique)

    return {
        "tool_key": tool_key,
        "label": cfg["label"],
        "pages": pages,
        "page_count": len(pages),
        "newest_mtime": newest_mtime,
        "history_url_count": len(history_urls),
        "expected_unique_files": expected_unique,
        "collision_count": collision_count,
        "missing_expected_files": max(0, expected_unique - len(pages)),
        "extra_files": max(0, len(pages) - expected_unique),
    }


def _match_any(patterns: list[str], text: str) -> bool:
    return any(re.search(pattern, text) for pattern in patterns)


def _find_hits(
    pages: dict[str, str],
    filename_patterns: list[str],
    content_patterns: list[str],
) -> list[str]:
    hits: list[str] = []
    for filename in sorted(pages):
        text = pages[filename]
        if filename_patterns and _match_any(filename_patterns, filename):
            hits.append(filename)
            continue
        if content_patterns and _match_any(content_patterns, text):
            hits.append(filename)
    return hits


def _find_implied_hits(pages: dict[str, str], implied_patterns: list[str]) -> tuple[list[str], int]:
    matched_patterns = 0
    files: set[str] = set()
    for pattern in implied_patterns:
        local_hits = [filename for filename, text in pages.items() if re.search(pattern, text)]
        if local_hits:
            matched_patterns += 1
            files.update(local_hits)
    return sorted(files), matched_patterns


def evaluate_feature(tool: dict[str, Any], feature: dict[str, Any]) -> dict[str, Any]:
    explicit_hits = _find_hits(
        pages=tool["pages"],
        filename_patterns=feature["explicit_filename"],
        content_patterns=[],
    )

    if explicit_hits:
        level = "explicit"
        factor = 1.0
        citations = explicit_hits[:4]
    else:
        implied_patterns = feature["explicit_content"] + feature["implied_content"]
        implied_hits, matched_patterns = _find_implied_hits(tool["pages"], implied_patterns)
        if matched_patterns >= 2 or len(implied_hits) >= 2:
            level = "implied"
            factor = 0.6
            citations = implied_hits[:4]
        else:
            level = "none"
            factor = 0.0
            citations = []

    points = round(feature["weight"] * factor, 2)
    return {
        "level": level,
        "factor": factor,
        "points": points,
        "citations": citations,
    }


def compute_reliability(tool: dict[str, Any], now_utc: datetime) -> dict[str, Any]:
    reasons: list[str] = []
    penalty = 0.0

    if tool["history_url_count"] == 0:
        reasons.append("No history URLs available for coverage checks")
        return {
            "points": 0.0,
            "reasons": reasons,
            "age_days": None,
        }

    if tool["collision_count"] > 0:
        collision_pen = min(2.5, tool["collision_count"] * 0.5)
        penalty += collision_pen
        reasons.append(f"URL-to-filename collisions detected: {tool['collision_count']}")

    if tool["missing_expected_files"] > 0:
        missing_pen = min(1.5, tool["missing_expected_files"] * 0.5)
        penalty += missing_pen
        reasons.append(f"Mapped files missing from pages/: {tool['missing_expected_files']}")

    age_days = None
    newest = tool["newest_mtime"]
    if newest is None:
        penalty += 5.0
        reasons.append("No page files found")
    else:
        age_days = (now_utc - newest).total_seconds() / 86400.0
        if age_days > 21:
            staleness_pen = min(1.0, (age_days - 21) / 14)
            penalty += staleness_pen
            reasons.append(f"Docs are stale ({age_days:.1f} days old)")

    points = round(max(0.0, 5.0 - penalty), 2)
    if not reasons:
        reasons.append("No reliability penalties detected")

    return {
        "points": points,
        "reasons": reasons,
        "age_days": None if age_days is None else round(age_days, 2),
    }


def build_additional_feature_highlights(tools: dict[str, dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    highlights: dict[str, list[dict[str, Any]]] = {tool_key: [] for tool_key in tools}
    for tool_key, signals in UNIQUE_SIGNAL_PATTERNS.items():
        if tool_key not in tools:
            continue
        filenames = sorted(tools[tool_key]["pages"].keys())
        for signal in signals:
            hits = [name for name in filenames if re.search(signal["pattern"], name)]
            if hits:
                highlights[tool_key].append(
                    {
                        "label": signal["label"],
                        "citations": hits[:4],
                    }
                )
    return highlights


def feature_display(feature: dict[str, Any], result: dict[str, Any]) -> str:
    citation_str = ", ".join(result["citations"]) if result["citations"] else "-"
    return f"{result['points']:.1f}/{feature['weight']} ({result['level']}; {citation_str})"


def build_analysis(now_utc: datetime) -> dict[str, Any]:
    tools = {tool_key: load_tool_corpus(tool_key, cfg) for tool_key, cfg in TOOL_CONFIGS.items()}

    category_scores: dict[str, dict[str, float]] = {
        tool_key: {cat: 0.0 for cat in CATEGORIES} for tool_key in tools
    }
    feature_results: dict[str, dict[str, dict[str, Any]]] = {
        feature["id"]: {} for feature in FEATURES
    }

    for feature in FEATURES:
        for tool_key, tool in tools.items():
            result = evaluate_feature(tool, feature)
            feature_results[feature["id"]][tool_key] = result
            category_scores[tool_key][feature["category"]] += result["points"]

    reliability: dict[str, dict[str, Any]] = {}
    for tool_key, tool in tools.items():
        rel = compute_reliability(tool, now_utc)
        reliability[tool_key] = rel
        category_scores[tool_key]["docs_reliability"] = rel["points"]

    totals: dict[str, float] = {
        tool_key: round(sum(cat_scores.values()), 2)
        for tool_key, cat_scores in category_scores.items()
    }

    sorted_tools = sorted(
        totals,
        key=lambda t: (
            totals[t],
            category_scores[t]["power_user_depth"],
            category_scores[t]["security_governance"],
            category_scores[t]["automation_integrations"],
        ),
        reverse=True,
    )

    ranks = {tool_key: idx + 1 for idx, tool_key in enumerate(sorted_tools)}

    # Shared / missing / differentiators
    common_features: list[dict[str, Any]] = []
    missing_features: dict[str, list[dict[str, Any]]] = {tool_key: [] for tool_key in tools}
    differentiators: dict[str, list[dict[str, Any]]] = {tool_key: [] for tool_key in tools}

    for feature in FEATURES:
        fid = feature["id"]
        per_tool = feature_results[fid]
        levels = {tool_key: per_tool[tool_key]["level"] for tool_key in tools}
        points = {tool_key: per_tool[tool_key]["points"] for tool_key in tools}

        if all(level != "none" for level in levels.values()):
            common_features.append(
                {
                    "feature_id": fid,
                    "feature_name": feature["name"],
                    "category": feature["category"],
                }
            )

        for tool_key in tools:
            other_tools = [other for other in tools if other != tool_key]
            others_have_explicit = any(levels[other] == "explicit" for other in other_tools)
            is_underrepresented = levels[tool_key] == "none" or (
                levels[tool_key] == "implied" and others_have_explicit
            )
            if is_underrepresented and any(points[other] > points[tool_key] for other in other_tools):
                missing_features[tool_key].append(
                    {
                        "feature_id": fid,
                        "feature_name": feature["name"],
                        "weight": feature["weight"],
                        "category": feature["category"],
                        "level": levels[tool_key],
                    }
                )

        ordered = sorted(points.items(), key=lambda kv: kv[1], reverse=True)
        top_tool, top_score = ordered[0]
        second_score = ordered[1][1] if len(ordered) > 1 else 0.0
        if top_score >= feature["weight"] * 0.8 and second_score <= feature["weight"] * 0.6:
            differentiators[top_tool].append(
                {
                    "feature_id": fid,
                    "feature_name": feature["name"],
                    "weight": feature["weight"],
                    "category": feature["category"],
                    "score": top_score,
                }
            )

    additional_highlights = build_additional_feature_highlights(tools)

    # Benefits and drawbacks
    benefits_drawbacks: dict[str, dict[str, list[str]]] = {}
    for tool_key in tools:
        cat_pct = []
        for cat_key, cat_info in CATEGORIES.items():
            max_points = cat_info["weight"]
            earned = category_scores[tool_key][cat_key]
            pct = earned / max_points if max_points else 0.0
            cat_pct.append((cat_key, pct, earned, max_points))
        cat_pct.sort(key=lambda item: item[1], reverse=True)

        top_categories = cat_pct[:3]
        weak_categories = [item for item in cat_pct if item[1] < 0.6 and item[0] != "docs_reliability"]

        benefits = [
            f"Strong in {CATEGORIES[cat]['label']} ({earned:.1f}/{max_points})"
            for cat, _pct, earned, max_points in top_categories
        ]

        for diff in sorted(differentiators[tool_key], key=lambda d: (d["weight"], d["score"]), reverse=True)[:3]:
            benefits.append(f"Differentiator: {diff['feature_name']}")
        for highlight in additional_highlights[tool_key][:2]:
            benefits.append(f"Additional feature: {highlight['label']}")

        drawbacks = [
            f"Needs improvement in {CATEGORIES[cat]['label']} ({earned:.1f}/{max_points})"
            for cat, _pct, earned, max_points in weak_categories[:3]
        ]

        high_weight_missing = sorted(
            [f for f in missing_features[tool_key] if f["weight"] >= 5],
            key=lambda item: item["weight"],
            reverse=True,
        )[:3]
        for miss in high_weight_missing:
            drawbacks.append(f"Missing or weak feature area: {miss['feature_name']}")

        if reliability[tool_key]["points"] < 4.0:
            drawbacks.append(
                f"Corpus reliability penalty ({reliability[tool_key]['points']:.1f}/5): "
                + "; ".join(reliability[tool_key]["reasons"])
            )

        benefits_drawbacks[tool_key] = {
            "benefits": benefits,
            "drawbacks": drawbacks,
        }

    return {
        "rubric_version": RUBRIC_VERSION,
        "analysis_timestamp_utc": now_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
        "categories": CATEGORIES,
        "features": FEATURES,
        "tools": tools,
        "feature_results": feature_results,
        "category_scores": {
            tool_key: {cat: round(score, 2) for cat, score in scores.items()}
            for tool_key, scores in category_scores.items()
        },
        "reliability": reliability,
        "totals": totals,
        "ranking": [
            {
                "rank": ranks[tool_key],
                "tool": tool_key,
                "label": tools[tool_key]["label"],
                "score": totals[tool_key],
            }
            for tool_key in sorted_tools
        ],
        "common_features": common_features,
        "missing_features": missing_features,
        "differentiators": differentiators,
        "additional_feature_highlights": additional_highlights,
        "benefits_drawbacks": benefits_drawbacks,
    }


def write_json(output_dir: Path, analysis: dict[str, Any]) -> Path:
    path = output_dir / "report.json"
    path.write_text(
        json.dumps(
            analysis,
            indent=2,
            default=lambda obj: obj.isoformat() if isinstance(obj, datetime) else str(obj),
        ),
        encoding="utf-8",
    )
    return path


def write_csv(output_dir: Path, analysis: dict[str, Any]) -> Path:
    path = output_dir / "latest_scores.csv"
    category_keys = list(CATEGORIES.keys())
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["rank", "tool", "label", "total_score"] + category_keys)
        for row in analysis["ranking"]:
            tool = row["tool"]
            writer.writerow(
                [
                    row["rank"],
                    tool,
                    row["label"],
                    f"{row['score']:.2f}",
                ]
                + [f"{analysis['category_scores'][tool][cat]:.2f}" for cat in category_keys]
            )
    return path


def write_markdown(output_dir: Path, analysis: dict[str, Any]) -> Path:
    path = output_dir / "report.md"
    lines: list[str] = []

    lines.append("# Full Documentation Feature Comparison")
    lines.append("")
    lines.append(f"*Generated: {analysis['analysis_timestamp_utc']}*")
    lines.append(f"*Rubric version: {analysis['rubric_version']}*")
    lines.append("")

    lines.append("## Corpus Coverage")
    lines.append("")
    lines.append("| Tool | Pages | Newest Page (UTC) | History URLs | Expected Unique Files | Collisions | Reliability |")
    lines.append("|------|------:|-------------------|-------------:|----------------------:|-----------:|------------:|")
    for tool_key in TOOL_CONFIGS:
        tool = analysis["tools"][tool_key]
        newest = tool["newest_mtime"].strftime("%Y-%m-%d %H:%M:%S") if tool["newest_mtime"] else "-"
        rel = analysis["reliability"][tool_key]["points"]
        lines.append(
            f"| {tool['label']} | {tool['page_count']} | {newest} | {tool['history_url_count']} | "
            f"{tool['expected_unique_files']} | {tool['collision_count']} | {rel:.1f}/5 |"
        )
    lines.append("")

    lines.append("## Scores and Ranking")
    lines.append("")
    lines.append("| Rank | Tool | Score / 100 |")
    lines.append("|------|------|------------:|")
    for row in analysis["ranking"]:
        lines.append(f"| {row['rank']} | {row['label']} | {row['score']:.2f} |")
    lines.append("")

    lines.append("## Category Breakdown")
    lines.append("")
    lines.append("| Category | Weight | Claude | Gemini | Codex |")
    lines.append("|----------|-------:|-------:|-------:|------:|")
    for cat_key, cat_info in CATEGORIES.items():
        lines.append(
            f"| {cat_info['label']} | {cat_info['weight']} | "
            f"{analysis['category_scores']['claude'][cat_key]:.1f} | "
            f"{analysis['category_scores']['gemini'][cat_key]:.1f} | "
            f"{analysis['category_scores']['codex'][cat_key]:.1f} |"
        )
    lines.append("")

    lines.append("## Common Features Across All Three")
    lines.append("")
    if analysis["common_features"]:
        for item in analysis["common_features"]:
            lines.append(f"- {item['feature_name']}")
    else:
        lines.append("- No feature met the common-coverage threshold.")
    lines.append("")

    lines.append("## Missing or Underrepresented Feature Areas")
    lines.append("")
    for tool_key in TOOL_CONFIGS:
        label = analysis["tools"][tool_key]["label"]
        lines.append(f"### {label}")
        misses = sorted(
            analysis["missing_features"][tool_key],
            key=lambda item: (item["weight"], item["feature_name"]),
            reverse=True,
        )
        if not misses:
            lines.append("- No major missing feature areas under this rubric.")
        else:
            for miss in misses[:8]:
                lines.append(
                    f"- {miss['feature_name']} (weight {miss['weight']}; current evidence: {miss['level']})"
                )
        lines.append("")

    lines.append("## Tool-Specific Differentiators")
    lines.append("")
    for tool_key in TOOL_CONFIGS:
        label = analysis["tools"][tool_key]["label"]
        lines.append(f"### {label}")
        diffs = sorted(
            analysis["differentiators"][tool_key],
            key=lambda item: (item["weight"], item["score"]),
            reverse=True,
        )
        if diffs:
            for diff in diffs:
                lines.append(f"- {diff['feature_name']} ({diff['score']:.1f}/{diff['weight']})")
        extras = analysis["additional_feature_highlights"][tool_key]
        if extras:
            for item in extras:
                citations = ", ".join(item["citations"]) if item["citations"] else "-"
                lines.append(f"- {item['label']} ({citations})")
        if not diffs and not extras:
            lines.append("- No strong differentiators under current thresholds.")
        lines.append("")

    lines.append("## Benefits and Drawbacks")
    lines.append("")
    for tool_key in TOOL_CONFIGS:
        label = analysis["tools"][tool_key]["label"]
        lines.append(f"### {label}")
        lines.append("Benefits:")
        for bullet in analysis["benefits_drawbacks"][tool_key]["benefits"]:
            lines.append(f"- {bullet}")
        lines.append("Drawbacks:")
        for bullet in analysis["benefits_drawbacks"][tool_key]["drawbacks"]:
            lines.append(f"- {bullet}")
        lines.append("")

    lines.append("## Detailed Feature Matrix")
    lines.append("")
    for category_key, cat_info in CATEGORIES.items():
        if category_key == "docs_reliability":
            continue
        lines.append(f"### {cat_info['label']}")
        lines.append("")
        lines.append("| Feature | Weight | Claude | Gemini | Codex |")
        lines.append("|---------|-------:|--------|--------|-------|")
        for feature in FEATURES:
            if feature["category"] != category_key:
                continue
            row = [
                feature["name"],
                str(feature["weight"]),
                feature_display(feature, analysis["feature_results"][feature["id"]]["claude"]),
                feature_display(feature, analysis["feature_results"][feature["id"]]["gemini"]),
                feature_display(feature, analysis["feature_results"][feature["id"]]["codex"]),
            ]
            lines.append(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} |")
        lines.append("")

    lines.append("## Reliability Notes")
    lines.append("")
    for tool_key in TOOL_CONFIGS:
        label = analysis["tools"][tool_key]["label"]
        rel = analysis["reliability"][tool_key]
        lines.append(f"### {label} ({rel['points']:.1f}/5)")
        for reason in rel["reasons"]:
            lines.append(f"- {reason}")
        lines.append("")

    lines.append("## Scoring Method")
    lines.append("")
    lines.append("- Explicit evidence: full points for a feature")
    lines.append("- Strong implied evidence: 60% of feature points")
    lines.append("- No evidence: 0 points")
    lines.append("- Category weights and thresholds are defined in `DOCS_COMPARISON_RUBRIC.md`")
    lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def enforce_rubric(strict: bool) -> None:
    if not strict:
        return
    if not RUBRIC_DOC_PATH.exists():
        raise SystemExit(
            f"--strict-rubric failed: {RUBRIC_DOC_PATH} not found"
        )
    rubric_text = RUBRIC_DOC_PATH.read_text(encoding="utf-8", errors="ignore")
    marker = f"Rubric Version: {RUBRIC_VERSION}"
    if marker not in rubric_text:
        raise SystemExit(
            f"--strict-rubric failed: expected marker '{marker}' in {RUBRIC_DOC_PATH}"
        )


def main() -> int:
    args = parse_args()
    enforce_rubric(args.strict_rubric)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    now_utc = datetime.now(timezone.utc)
    analysis = build_analysis(now_utc)

    written: list[Path] = []
    if args.format in {"json", "both"}:
        written.append(write_json(output_dir, analysis))
        written.append(write_csv(output_dir, analysis))
    if args.format in {"md", "both"}:
        written.append(write_markdown(output_dir, analysis))

    top = analysis["ranking"][0]
    print(
        f"Generated comparison ({analysis['analysis_timestamp_utc']}) - "
        f"#1 {top['label']} at {top['score']:.2f}/100"
    )
    for row in analysis["ranking"]:
        print(f"  {row['rank']}. {row['label']}: {row['score']:.2f}")
    print("Artifacts:")
    for item in written:
        print(f"  - {item}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
