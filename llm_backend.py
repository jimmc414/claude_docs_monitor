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
import re
import shutil
import subprocess
import sys
import time
from typing import Optional

_RESOLVED_BACKEND: Optional[str] = None


class RateLimitError(RuntimeError):
    """Raised when the upstream model returns a rate-limit / overloaded signal.

    Distinct from generic RuntimeError so callers (including the dispatcher's
    own retry loop) can backoff transient throttling without retrying real
    bugs like schema parse failures, auth errors, or empty outputs.
    """
    def __init__(self, message: str, retry_after: Optional[float] = None):
        super().__init__(message)
        self.retry_after = retry_after


# Pattern matches the rate-limit / overload signatures we've observed across
# all three backend paths:
#   - Anthropic API: "rate_limit_error", "overloaded_error", HTTP 429/529
#   - claude_agent_sdk: surfaces upstream error text in the Exception message
#   - claude CLI: writes the same to stderr before exiting non-zero
_RATE_LIMIT_PATTERNS = re.compile(
    r"(rate[_ -]?limit|429\b|529\b|overloaded_error|too many requests)",
    re.IGNORECASE,
)

# The SDK's hardcoded placeholder when the inner CLI subprocess dies opaquely
# (exit non-zero with no stderr we can attribute). Observed in v4.2/v4.3 probes:
# the CLI subprocess crashes ~1-2 times per 9-question report run with completely
# empty stderr — likely signal kill / OOM / transient race during init. The
# placeholder string is set at subprocess_cli.py:625-627 in claude_agent_sdk.
# Retrying once or twice consistently recovers; the underlying cause is opaque
# but transient.
_SDK_OPAQUE_FAILURE_PATTERN = re.compile(
    r"Command failed with exit code \d+.*Check stderr output for details",
    re.IGNORECASE | re.DOTALL,
)


def _is_rate_limit(err_text: str) -> bool:
    """True if err_text contains any known rate-limit signature."""
    return bool(_RATE_LIMIT_PATTERNS.search(err_text or ""))


def _is_sdk_opaque_failure(err_text: str) -> bool:
    """True if err_text matches the SDK's hardcoded exit-N + 'Check stderr' placeholder."""
    return bool(_SDK_OPAQUE_FAILURE_PATTERN.search(err_text or ""))

# The API backend needs full model IDs. The CLI and SDK accept aliases
# natively. These IDs are documented as working with Max OAuth in
# ~/.claude/rules/agent-sdk-max-oauth.md and may need refreshing when
# Anthropic releases new models.
_MODEL_ALIASES_API = {
    "sonnet": "claude-sonnet-4-6",
    "opus":   "claude-opus-4-7",
    "haiku":  "claude-haiku-4-5-20251001",
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
        err_msg = f"claude CLI exited with code {result.returncode}: {result.stderr[:500]}"
        if _is_rate_limit(result.stderr):
            raise RateLimitError(err_msg)
        raise RuntimeError(err_msg)
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
    # Uses ``ClaudeSDKClient`` rather than the one-shot ``query()`` helper. The
    # latter has a race where the CLI subprocess exits immediately after sending
    # the prompt, which is fine in isolation but breaks subsequent invocations
    # in the same Python process — observed in v4.3 as the inner CLI dying
    # opaquely (exit 1, empty stderr) on every call AFTER a ClaudeSDKClient has
    # been used. The long-lived client gives the subprocess time to drain.
    # See report_builder.py:425-429 for the original observation in the gap-fill loop.
    from claude_agent_sdk import ClaudeAgentOptions, ClaudeSDKClient  # pyright: ignore[reportMissingImports]

    full_prompt = _combine(prompt, stdin, json_schema)

    saved_key = os.environ.pop("ANTHROPIC_API_KEY", None)
    try:
        options = ClaudeAgentOptions(
            model=model,
            permission_mode="bypassPermissions",
            max_turns=1,
            stderr=lambda line: print(f"[sdk-cli] {line}", file=sys.stderr, flush=True),
        )

        async def _run() -> str:
            chunks: list[str] = []
            final_result: Optional[str] = None
            async with ClaudeSDKClient(options=options) as client:
                await client.query(full_prompt)
                async for msg in client.receive_response():
                    result_attr = getattr(msg, "result", None)
                    if isinstance(result_attr, str) and result_attr:
                        final_result = result_attr
                        continue
                    content = getattr(msg, "content", None)
                    if isinstance(content, list):
                        for block in content:
                            text = getattr(block, "text", None)
                            if isinstance(text, str) and text:
                                chunks.append(text)
            return (final_result or "".join(chunks)).strip()

        try:
            out = _run_sdk_coro(_run(), timeout)
        except Exception as e:
            err_text = f"{e!r} {e!s}"
            if _is_rate_limit(err_text):
                raise RateLimitError(str(e)) from e
            if _is_sdk_opaque_failure(err_text):
                raise RateLimitError(f"transient SDK subprocess failure: {e!s}") from e
            raise
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
    try:
        msg = client.messages.create(
            model=api_model,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": full_prompt}],
        )
    except anthropic.RateLimitError as e:
        retry_after = None
        try:
            ra = e.response.headers.get("retry-after") if getattr(e, "response", None) else None
            retry_after = float(ra) if ra else None
        except (ValueError, TypeError, AttributeError):
            retry_after = None
        raise RateLimitError(str(e), retry_after=retry_after) from e
    except anthropic.APIStatusError as e:
        # 529 overloaded falls under APIStatusError, not RateLimitError
        status = getattr(e, "status_code", None)
        if status in (429, 529) or _is_rate_limit(str(e)):
            raise RateLimitError(str(e)) from e
        raise

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
                env: Optional[dict] = None,
                max_retries: int = 2,
                retry_base_delay: float = 5.0) -> str:
    """Call Claude via the resolved backend, with rate-limit retry.

    Returns the model's textual output. If ``json_schema`` is provided, the
    output is the model's JSON response as a string (the caller parses it).

    Retries up to ``max_retries`` times on ``RateLimitError`` only, with
    exponential backoff (default 5s, 15s, 45s). All other exceptions raise
    immediately on the first attempt — schema parse failures, auth errors,
    and timeouts should NOT be retried.

    Raises RuntimeError or RateLimitError on backend failure. Callers that
    want to gracefully degrade should catch both.
    """
    chosen = resolve_backend(backend)
    if env is None:
        env = dict(os.environ)

    _vprint(f"call: backend={chosen} model={model} schema={'yes' if json_schema else 'no'}")

    def _dispatch() -> str:
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

    last_err: Optional[RateLimitError] = None
    for attempt in range(max_retries + 1):
        try:
            return _dispatch()
        except RateLimitError as e:
            last_err = e
            if attempt >= max_retries:
                break
            delay = e.retry_after if e.retry_after else retry_base_delay * (3 ** attempt)
            kind = "transient-sdk" if "transient SDK" in str(e) else "rate-limit"
            _vprint(
                f"{kind} retry (attempt {attempt + 1}/{max_retries + 1}), "
                f"sleeping {delay:.1f}s: {e!s}"
            )
            time.sleep(delay)
    assert last_err is not None
    raise last_err
