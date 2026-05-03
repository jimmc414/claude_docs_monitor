"""Tiered LLM backend dispatcher for Claude.

Provides a single ``call_claude()`` entry point that routes to one of three
backends:

  * ``sdk`` — claude_agent_sdk (preferred; lightweight, async-friendly)
  * ``cli`` — ``claude -p`` subprocess (fallback; works without optional deps)
  * ``api`` — Anthropic REST API (opt-in via ANTHROPIC_API_KEY)

Resolution order for ``auto``:
    sdk → cli → api

The ``api`` tier is gated on ``ANTHROPIC_API_KEY`` being set. If the env var
is unset, ``auto`` will never resolve to ``api`` and no API spend can occur.

For the ``sdk`` and ``cli`` backends, ``ANTHROPIC_API_KEY`` is stripped from
the environment before invocation so credential discovery falls through to
``~/.claude/.credentials.json`` (Max OAuth). The user-global rule
``~/.claude/rules/agent-sdk-max-oauth.md`` requires this.

Set ``DOCS_MONITOR_VERBOSE=1`` to print the chosen backend to stderr.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from typing import Optional

_RESOLVED_BACKEND: Optional[str] = None

# The API backend needs full model IDs. The CLI and SDK accept aliases
# natively. These IDs are documented as working with Max OAuth in
# ~/.claude/rules/agent-sdk-max-oauth.md and may need refreshing when
# Anthropic releases new models.
_MODEL_ALIASES_API = {
    "sonnet": "claude-sonnet-4-20250514",
    "opus":   "claude-opus-4-5-20251101",
    "haiku":  "claude-haiku-4-5-20250514",
}


def _vprint(msg: str) -> None:
    if os.environ.get("DOCS_MONITOR_VERBOSE") == "1":
        print(f"[llm_backend] {msg}", file=sys.stderr)


def _try_sdk() -> bool:
    try:
        import claude_agent_sdk  # type: ignore[import-not-found,unused-ignore]  # noqa: F401
        return True
    except ImportError:
        return False


def _try_cli() -> bool:
    if not shutil.which("claude"):
        return False
    try:
        result = subprocess.run(
            ["claude", "--version"],
            capture_output=True, text=True, timeout=5,
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
        return False


def _try_api() -> bool:
    """API tier is opt-in: requires ANTHROPIC_API_KEY AND the anthropic package."""
    if not os.environ.get("ANTHROPIC_API_KEY"):
        return False
    try:
        import anthropic  # type: ignore[import-not-found,unused-ignore]  # noqa: F401
        return True
    except ImportError:
        return False


def reset_backend_cache() -> None:
    """Clear the cached backend resolution. Mainly useful in tests."""
    global _RESOLVED_BACKEND
    _RESOLVED_BACKEND = None


def resolve_backend(requested: str = "auto") -> str:
    """Resolve which backend to use.

    ``auto`` order: sdk → cli → api. A forced backend that is unavailable
    raises RuntimeError with installation guidance.
    """
    global _RESOLVED_BACKEND

    if requested != "auto":
        if requested == "sdk" and not _try_sdk():
            raise RuntimeError(
                "Backend 'sdk' requested but claude_agent_sdk is not installed. "
                "Install with: pip install -r requirements-sdk.txt"
            )
        if requested == "cli" and not _try_cli():
            raise RuntimeError(
                "Backend 'cli' requested but `claude` CLI is not on PATH or unhealthy. "
                "Install Claude Code: https://docs.anthropic.com/en/docs/claude-code"
            )
        if requested == "api" and not _try_api():
            raise RuntimeError(
                "Backend 'api' requested but ANTHROPIC_API_KEY is unset or "
                "the `anthropic` package is not installed. "
                "Install with: pip install -r requirements-api.txt and set ANTHROPIC_API_KEY."
            )
        if requested not in {"sdk", "cli", "api"}:
            raise RuntimeError(
                f"Unknown backend '{requested}'. Use one of: auto, sdk, cli, api."
            )
        _vprint(f"backend forced: {requested}")
        return requested

    if _RESOLVED_BACKEND is not None:
        return _RESOLVED_BACKEND

    if _try_sdk():
        _RESOLVED_BACKEND = "sdk"
    elif _try_cli():
        _RESOLVED_BACKEND = "cli"
    elif _try_api():
        _RESOLVED_BACKEND = "api"
    else:
        raise RuntimeError(
            "No LLM backend available. Install one of:\n"
            "  - Claude Agent SDK:  pip install -r requirements-sdk.txt\n"
            "  - Claude CLI:        https://docs.anthropic.com/en/docs/claude-code\n"
            "  - Anthropic API:     pip install -r requirements-api.txt and set ANTHROPIC_API_KEY"
        )
    _vprint(f"backend resolved: {_RESOLVED_BACKEND}")
    return _RESOLVED_BACKEND


def _strip_api_key_env(env: dict) -> dict:
    """Strip ANTHROPIC_API_KEY so SDK/CLI fall through to ~/.claude/.credentials.json."""
    return {k: v for k, v in env.items() if k != "ANTHROPIC_API_KEY"}


def _combine(prompt: str, stdin: str, json_schema: Optional[str]) -> str:
    """Merge prompt + piped content + optional JSON-schema instruction into one user message."""
    parts = [prompt]
    if stdin:
        parts.append(stdin)
    if json_schema:
        parts.append(
            "Respond ONLY with valid JSON matching this schema "
            "(no prose, no markdown fences):\n" + json_schema
        )
    return "\n\n".join(parts)


def _call_via_cli(*, prompt: str, stdin: str, model: str,
                  json_schema: Optional[str], timeout: int, env: dict) -> str:
    cmd = ["claude", "-p", prompt, "--model", model,
           "--max-turns", "1",
           "--output-format", "json" if json_schema else "text"]
    if json_schema:
        cmd += ["--json-schema", json_schema]

    cli_env = _strip_api_key_env(env)
    result = subprocess.run(
        cmd, input=stdin, capture_output=True, text=True,
        timeout=timeout, env=cli_env,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"claude CLI exited with code {result.returncode}: {result.stderr[:500]}"
        )
    raw = result.stdout.strip()
    if not raw:
        raise RuntimeError("claude CLI returned empty output")
    return raw


def _run_sdk_coro(coro, timeout: int):
    """Run an async coroutine to completion, even if a loop is already running."""
    import asyncio

    try:
        asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(asyncio.wait_for(coro, timeout=timeout))

    import concurrent.futures
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
        future = pool.submit(
            lambda: asyncio.run(asyncio.wait_for(coro, timeout=timeout))
        )
        return future.result(timeout=timeout + 10)


def _call_via_sdk(*, prompt: str, stdin: str, model: str,
                  json_schema: Optional[str], timeout: int) -> str:
    from claude_agent_sdk import query, ClaudeAgentOptions  # pyright: ignore[reportMissingImports]

    full_prompt = _combine(prompt, stdin, json_schema)

    saved_key = os.environ.pop("ANTHROPIC_API_KEY", None)
    try:
        options = ClaudeAgentOptions(
            model=model,
            permission_mode="bypassPermissions",
            max_turns=1,
        )

        async def _run() -> str:
            chunks: list[str] = []
            final_result: Optional[str] = None
            async for msg in query(prompt=full_prompt, options=options):
                # ResultMessage.result is the cleanest one-shot output
                result_attr = getattr(msg, "result", None)
                if isinstance(result_attr, str) and result_attr:
                    final_result = result_attr
                    continue
                # AssistantMessage.content is a list[ContentBlock]
                content = getattr(msg, "content", None)
                if isinstance(content, list):
                    for block in content:
                        text = getattr(block, "text", None)
                        if isinstance(text, str) and text:
                            chunks.append(text)
            return (final_result or "".join(chunks)).strip()

        out = _run_sdk_coro(_run(), timeout)
    finally:
        if saved_key is not None:
            os.environ["ANTHROPIC_API_KEY"] = saved_key

    if not out:
        raise RuntimeError("claude_agent_sdk returned empty output")
    return out


def _call_via_api(*, prompt: str, stdin: str, model: str,
                  json_schema: Optional[str], max_tokens: int,
                  timeout: int) -> str:
    import anthropic  # pyright: ignore[reportMissingImports]

    api_model = _MODEL_ALIASES_API.get(model, model)
    full_prompt = _combine(prompt, stdin, json_schema)

    client = anthropic.Anthropic(timeout=float(timeout))
    msg = client.messages.create(
        model=api_model,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": full_prompt}],
    )

    text_parts: list[str] = []
    for block in msg.content:
        text = getattr(block, "text", None)
        if text:
            text_parts.append(text)
    out = "".join(text_parts).strip()
    if not out:
        raise RuntimeError("Anthropic API returned empty output")
    return out


def call_claude(*, prompt: str, stdin: str = "", model: str = "sonnet",
                json_schema: Optional[str] = None, backend: str = "auto",
                max_tokens: int = 4096, timeout: int = 300,
                env: Optional[dict] = None) -> str:
    """Call Claude via the resolved backend.

    Returns the model's textual output. If ``json_schema`` is provided, the
    output is the model's JSON response as a string (the caller parses it).

    Raises RuntimeError on backend failure. The CLI backend may also raise
    ``subprocess.TimeoutExpired`` or ``FileNotFoundError``; callers that want
    to gracefully degrade should catch all three.
    """
    chosen = resolve_backend(backend)
    if env is None:
        env = dict(os.environ)

    _vprint(f"call: backend={chosen} model={model} schema={'yes' if json_schema else 'no'}")

    if chosen == "sdk":
        return _call_via_sdk(prompt=prompt, stdin=stdin, model=model,
                             json_schema=json_schema, timeout=timeout)
    if chosen == "cli":
        return _call_via_cli(prompt=prompt, stdin=stdin, model=model,
                             json_schema=json_schema, timeout=timeout, env=env)
    if chosen == "api":
        return _call_via_api(prompt=prompt, stdin=stdin, model=model,
                             json_schema=json_schema, max_tokens=max_tokens,
                             timeout=timeout)
    raise RuntimeError(f"unknown backend: {chosen}")
