"""Persistent embedding cache for the docs-monitor RAG layer.

Hash-keyed: re-embedding only happens when the *text* changes. Survives
``rebuild-wiki`` and drop-and-rebuild cycles of any consumer index. Composite
PK ``(content_hash, model)`` lets multiple embedding models coexist.

Provider abstraction: three backends, picked at runtime.

  * ``voyage`` — ``voyage-3`` (1024-d), default. Anthropic's partner; best
    Anthropic-alignment for the "learn Anthropic" goal. Up to 128 inputs/call.
  * ``openai`` — ``text-embedding-3-large`` (3072-d). Up to 2048 inputs/call.
  * ``ollama`` — ``nomic-embed-text`` (768-d). Local, free, slower. Requires a
    running Ollama server on ``http://localhost:11434``.

Provider keys read from env (``VOYAGE_API_KEY``, ``OPENAI_API_KEY``) or
``~/.config/claude_docs_monitor/embedding.json``. Ollama needs no key.

Environment overrides:

  * ``DOCS_MONITOR_EMBED_PROVIDER`` — force provider (overrides constructor).
  * ``DOCS_MONITOR_EMBED_MODEL`` — force model.
  * ``DOCS_MONITOR_EMBED_VERBOSE=1`` — log cache hits/misses to stderr.
  * ``OLLAMA_HOST`` — override the Ollama base URL.
"""

from __future__ import annotations

import hashlib
import json
import os
import sqlite3
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np

DEFAULT_PROVIDER = "voyage"

# Provider → (default model, dims, max batch size)
# voyage-4-large is the current best-quality general retrieval model (1024-d,
# 200M-token free tier). Bake-off in data-claude/eval/embed_compare_results.md
# confirmed it beats voyage-context-3 on our corpus by ~20pp on Jaccard@5.
PROVIDER_DEFAULTS: dict[str, tuple[str, int, int]] = {
    # voyage-4-large enforces 120K tokens per batch. With mean chunk ~1500 tokens,
    # a batch of 50 keeps us comfortably under the limit even when chunks run
    # large (~2.5K tokens). Lower than voyage-3's nominal 128 cap but safer.
    "voyage":  ("voyage-4-large", 1024, 50),
    "openai":  ("text-embedding-3-large", 3072, 2048),
    "ollama":  ("nomic-embed-text", 768, 1),  # Ollama embeds one at a time
}

CONFIG_PATH = Path.home() / ".config/claude_docs_monitor/embedding.json"


def _vprint(msg: str) -> None:
    if os.environ.get("DOCS_MONITOR_EMBED_VERBOSE") == "1":
        print(f"[embedding_cache] {msg}", file=sys.stderr)


def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _load_config() -> dict:
    if CONFIG_PATH.exists():
        try:
            return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def _api_key(provider: str) -> str | None:
    env_key = {
        "voyage": "VOYAGE_API_KEY",
        "openai": "OPENAI_API_KEY",
    }.get(provider)
    if env_key and os.environ.get(env_key):
        return os.environ[env_key]
    cfg = _load_config()
    return cfg.get(provider, {}).get("api_key") if isinstance(cfg.get(provider), dict) else None


@dataclass
class EmbedStats:
    cache_hits: int = 0
    cache_misses: int = 0
    provider_calls: int = 0
    api_errors: int = 0


# Map the model names we know to their provider. Used by infer_provider_from_cache().
_MODEL_TO_PROVIDER: dict[str, str] = {
    "voyage-4-large":          "voyage",
    "voyage-4":                "voyage",
    "voyage-4-lite":           "voyage",
    "voyage-context-3":        "voyage",
    "voyage-3":                "voyage",
    "voyage-3-lite":           "voyage",
    "voyage-3-large":          "voyage",
    "voyage-large-2":          "voyage",
    "text-embedding-3-large":  "openai",
    "text-embedding-3-small":  "openai",
    "text-embedding-ada-002":  "openai",
    "nomic-embed-text":        "ollama",
}


def infer_provider_from_cache(db_path: Path) -> tuple[str, str] | None:
    """Inspect an embeddings.db and infer (provider, model) from cached rows.

    Returns the most-rows-cached (provider, model) pair, or None if the cache
    is empty / unreadable / contains no recognized model.
    """
    db_path = Path(db_path)
    if not db_path.exists():
        return None
    try:
        conn = sqlite3.connect(str(db_path))
        rows = conn.execute(
            "SELECT model, COUNT(*) as count FROM embeddings GROUP BY model "
            "ORDER BY count DESC"
        ).fetchall()
        conn.close()
    except sqlite3.Error:
        return None
    for row in rows:
        model = row[0]
        provider = _MODEL_TO_PROVIDER.get(model)
        if provider:
            return (provider, model)
        # Fuzzy match: if model name contains a known prefix
        for known_prefix, prov in (
            ("voyage", "voyage"),
            ("text-embedding", "openai"),
            ("nomic", "ollama"),
        ):
            if known_prefix in model.lower():
                return (prov, model)
    return None


class EmbeddingCache:
    """SQLite-backed embedding cache with provider abstraction.

    Vectors stored as packed float32 BLOBs. Composite PK ``(content_hash,
    model)`` so multiple models coexist. Cache hits skipped; misses sent in a
    single batched provider call (subject to provider batch limits).
    """

    def __init__(
        self,
        db_path: Path,
        provider: str | None = None,
        model: str | None = None,
    ):
        explicit_provider = os.environ.get("DOCS_MONITOR_EMBED_PROVIDER") or provider
        provider = explicit_provider or DEFAULT_PROVIDER
        if provider not in PROVIDER_DEFAULTS:
            raise ValueError(
                f"Unknown provider '{provider}'. "
                f"Valid: {sorted(PROVIDER_DEFAULTS.keys())}"
            )
        # Defensive fallback: if defaulting to voyage but VOYAGE_API_KEY is unset,
        # silently fall back to whatever the cache was indexed with. Prevents the
        # silent "0 initial chunks → empty synthesis" failure mode from v4.3.5
        # batch where queries can't be embedded → semantic search returns nothing.
        # An EXPLICIT provider request (env var or arg) is always honored — the
        # caller knows what they want.
        if explicit_provider is None and provider == "voyage" and not _api_key("voyage"):
            inferred = infer_provider_from_cache(Path(db_path))
            if inferred and inferred[0] != "voyage":
                _vprint(
                    f"VOYAGE_API_KEY missing; falling back to cached provider "
                    f"({inferred[0]}/{inferred[1]}). Set DOCS_MONITOR_EMBED_PROVIDER "
                    f"to override or VOYAGE_API_KEY to use voyage."
                )
                provider, model = inferred[0], inferred[1]
        default_model, default_dims, default_batch = PROVIDER_DEFAULTS[provider]
        model = os.environ.get("DOCS_MONITOR_EMBED_MODEL") or model or default_model

        self.db_path = Path(db_path)
        self.provider = provider
        self.model = model
        self.batch_size = default_batch
        self._dims_hint = default_dims
        self.stats_obj = EmbedStats()

        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(str(self.db_path))
        self._conn.row_factory = sqlite3.Row
        self._conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS embeddings (
                content_hash TEXT NOT NULL,
                model        TEXT NOT NULL,
                vector       BLOB NOT NULL,
                dims         INTEGER NOT NULL,
                created_at   TEXT NOT NULL,
                PRIMARY KEY (content_hash, model)
            );
            CREATE INDEX IF NOT EXISTS idx_emb_model ON embeddings(model);
            """
        )
        self._conn.commit()
        _vprint(f"opened cache at {self.db_path} (provider={self.provider}, model={self.model})")

    # ── Public API ──────────────────────────────────────────────────────────

    def embed(self, texts: list[str]) -> list[np.ndarray]:
        """Embed a batch of texts. Cached items skipped; misses sent to provider.

        Returns vectors in the same order as ``texts``. Empty strings are
        handled — they get a zero vector and are not sent to the provider.
        """
        if not texts:
            return []

        # Compute hashes in input order
        hashes = [_sha256(t) if t else "" for t in texts]

        # Lookup all hashes in one query (batch fetch)
        existing = self._fetch_many(hashes)

        results: list[np.ndarray | None] = [None] * len(texts)
        miss_indices: list[int] = []
        miss_texts: list[str] = []
        miss_hashes: list[str] = []

        for i, h in enumerate(hashes):
            if not h:
                # Empty string → zero vector
                results[i] = np.zeros(self._dims_hint, dtype=np.float32)
                continue
            if h in existing:
                results[i] = existing[h]
                self.stats_obj.cache_hits += 1
            else:
                miss_indices.append(i)
                miss_texts.append(texts[i])
                miss_hashes.append(h)
                self.stats_obj.cache_misses += 1

        if miss_texts:
            _vprint(
                f"embed: {len(miss_texts)} miss / {len(hashes) - len(miss_texts)} hit"
            )
            # Embed and commit per-batch so crashes don't lose work
            now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            for batch_start in range(0, len(miss_texts), self.batch_size):
                batch_texts = miss_texts[batch_start : batch_start + self.batch_size]
                batch_hashes = miss_hashes[batch_start : batch_start + self.batch_size]
                batch_indices = miss_indices[batch_start : batch_start + self.batch_size]
                batch_vectors = self._provider_call(batch_texts)
                if len(batch_vectors) != len(batch_texts):
                    raise RuntimeError(
                        f"Provider returned {len(batch_vectors)} vectors for "
                        f"{len(batch_texts)} inputs"
                    )
                self._store_many(list(zip(batch_hashes, batch_vectors)), now)
                for idx, vec in zip(batch_indices, batch_vectors):
                    results[idx] = vec

        # All slots should be filled
        return [r if r is not None else np.zeros(self._dims_hint, dtype=np.float32)
                for r in results]

    def embed_query(self, text: str) -> np.ndarray:
        """Embed a single query string."""
        out = self.embed([text])
        return out[0]

    def has(self, text: str) -> bool:
        """Check if a single text has a cached embedding."""
        h = _sha256(text)
        row = self._conn.execute(
            "SELECT 1 FROM embeddings WHERE content_hash = ? AND model = ? LIMIT 1",
            (h, self.model),
        ).fetchone()
        return row is not None

    def stats(self) -> dict:
        """Return cache statistics: row counts, total bytes, per-model breakdown."""
        rows = self._conn.execute(
            "SELECT model, COUNT(*) as count, SUM(LENGTH(vector)) as bytes "
            "FROM embeddings GROUP BY model"
        ).fetchall()
        models = {
            r["model"]: {"count": r["count"], "bytes": r["bytes"] or 0}
            for r in rows
        }
        total = self._conn.execute("SELECT COUNT(*) FROM embeddings").fetchone()[0]
        return {
            "total_rows": total,
            "models": models,
            "session": {
                "cache_hits": self.stats_obj.cache_hits,
                "cache_misses": self.stats_obj.cache_misses,
                "provider_calls": self.stats_obj.provider_calls,
                "api_errors": self.stats_obj.api_errors,
            },
            "current_provider": self.provider,
            "current_model": self.model,
        }

    def get_dims(self) -> int:
        """Return embedding dimensionality for the current model.

        Tries the cached row first; falls back to the provider default. Useful
        for retrievers that need to allocate vector arrays before embedding.
        """
        row = self._conn.execute(
            "SELECT dims FROM embeddings WHERE model = ? LIMIT 1", (self.model,)
        ).fetchone()
        if row:
            return int(row["dims"])
        return self._dims_hint

    def close(self) -> None:
        try:
            self._conn.close()
        except Exception:
            pass

    # ── Internals ───────────────────────────────────────────────────────────

    def _fetch_many(self, hashes: Iterable[str]) -> dict[str, np.ndarray]:
        """Bulk-fetch cached vectors for a list of hashes. Empty hashes ignored."""
        unique = list({h for h in hashes if h})
        if not unique:
            return {}
        # SQLite has a default limit of ~999 parameters per statement.
        out: dict[str, np.ndarray] = {}
        chunk = 500
        for i in range(0, len(unique), chunk):
            slice_ = unique[i : i + chunk]
            placeholders = ",".join("?" * len(slice_))
            q = (
                f"SELECT content_hash, vector, dims FROM embeddings "
                f"WHERE model = ? AND content_hash IN ({placeholders})"
            )
            rows = self._conn.execute(q, [self.model, *slice_]).fetchall()
            for r in rows:
                vec = np.frombuffer(r["vector"], dtype=np.float32)
                if vec.shape[0] != r["dims"]:
                    # Defensive: skip malformed rows
                    continue
                out[r["content_hash"]] = vec
        return out

    def _store_many(self, items: list[tuple[str, np.ndarray]], now: str) -> None:
        """Bulk-insert (hash, vector) pairs for the current model."""
        if not items:
            return
        rows = [
            (h, self.model, vec.astype(np.float32).tobytes(), int(vec.shape[0]), now)
            for h, vec in items
        ]
        self._conn.executemany(
            "INSERT OR REPLACE INTO embeddings "
            "(content_hash, model, vector, dims, created_at) VALUES (?, ?, ?, ?, ?)",
            rows,
        )
        self._conn.commit()

    def _provider_call(self, batch: list[str]) -> list[np.ndarray]:
        """One provider API call. Increments stats. Raises on failure."""
        self.stats_obj.provider_calls += 1
        try:
            if self.provider == "voyage":
                return self._call_voyage(batch)
            if self.provider == "openai":
                return self._call_openai(batch)
            if self.provider == "ollama":
                return self._call_ollama(batch)
            raise RuntimeError(f"Unknown provider: {self.provider}")
        except Exception:
            self.stats_obj.api_errors += 1
            raise

    def _call_voyage(self, batch: list[str]) -> list[np.ndarray]:
        try:
            import voyageai  # type: ignore[import-not-found,unused-ignore]
        except ImportError as e:
            raise RuntimeError(
                "Voyage provider requires `pip install voyageai`. "
                "Or switch providers via the DOCS_MONITOR_EMBED_PROVIDER env var: "
                "DOCS_MONITOR_EMBED_PROVIDER=ollama (local, no install) or "
                "DOCS_MONITOR_EMBED_PROVIDER=openai."
            ) from e
        key = _api_key("voyage")
        if not key:
            raise RuntimeError(
                "VOYAGE_API_KEY not set and no key in "
                f"{CONFIG_PATH}. Get one at https://www.voyageai.com/"
            )
        client = voyageai.Client(api_key=key)
        # input_type='document' for indexed content. Queries should pass
        # 'query' separately when calling embed_query() — but we leave that
        # to the retriever for now since the cost difference is negligible.
        result = client.embed(batch, model=self.model, input_type="document")
        return [np.asarray(v, dtype=np.float32) for v in result.embeddings]

    def _call_openai(self, batch: list[str]) -> list[np.ndarray]:
        try:
            from openai import OpenAI  # type: ignore[import-not-found,unused-ignore]
        except ImportError as e:
            raise RuntimeError(
                "OpenAI provider requires `pip install openai`."
            ) from e
        key = _api_key("openai")
        if not key:
            raise RuntimeError("OPENAI_API_KEY not set.")
        client = OpenAI(api_key=key)
        resp = client.embeddings.create(model=self.model, input=batch)
        return [np.asarray(d.embedding, dtype=np.float32) for d in resp.data]

    def _call_ollama(self, batch: list[str]) -> list[np.ndarray]:
        # Ollama's /api/embeddings takes one string at a time. Loop the batch.
        try:
            import httpx
        except ImportError as e:
            raise RuntimeError(
                "Ollama provider requires `pip install httpx`."
            ) from e
        host = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
        url = f"{host.rstrip('/')}/api/embeddings"
        out: list[np.ndarray] = []
        with httpx.Client(timeout=120.0) as client:
            for text in batch:
                resp = client.post(url, json={"model": self.model, "prompt": text})
                if resp.status_code != 200:
                    raise RuntimeError(
                        f"Ollama embeddings request failed "
                        f"({resp.status_code}): {resp.text[:200]}"
                    )
                data = resp.json()
                vec = data.get("embedding")
                if not vec:
                    raise RuntimeError(
                        f"Ollama returned no embedding: keys={list(data.keys())}"
                    )
                out.append(np.asarray(vec, dtype=np.float32))
        return out


__all__ = ["EmbeddingCache", "EmbedStats", "PROVIDER_DEFAULTS"]
