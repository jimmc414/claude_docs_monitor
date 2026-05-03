"""Unified retrievable index for the docs-monitor RAG layer.

Chunks pages and change_events into a single ``doc_chunks`` table, keeps an
FTS5 mirror for BM25, and stores per-chunk LLM summaries for retrieval-time
multi-representation lookup.

One unified index serves ``/ask-docs`` (page chunks), ``/query-docs`` (event
chunks), and future wiki/KG (their chunks). Filter by ``source_type`` to slice.

Schema notes:

  * ``content_hash`` is sha256(content) — joins to ``embedding_cache.embeddings``.
  * ``summary_hash`` is sha256(summary) — caches summary embeddings independently
    so a summary regen reuses the embedding if it happens to produce identical text.
  * ``UNIQUE(source_type, source_id, chunk_type, heading_path)`` lets us upsert
    on reindex without duplicates.

Page chunking algorithm: split at H1/H2/H3 boundaries, store one chunk per
section plus one whole-page chunk. The ``heading_path`` breadcrumb (e.g.
``hooks.md > Hook Events > PreToolUse``) makes citations precise and is also
indexed by FTS5 for additional BM25 signal.

Change-event chunking: one chunk per ``change_events`` row. Content is the
concatenation of summary + details + diff_text (NULLs skipped). Existing
``change_events`` data has many NULL classifications — we degrade gracefully
by falling back to ``diff_text``.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sqlite3
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator

from embedding_cache import EmbeddingCache

# Headings up to H3 are chunk boundaries. Deeper headings stay inside their
# parent chunk (avoids over-fragmenting).
_HEADING_RE = re.compile(r"^(#{1,3})\s+(.+?)\s*$")

# Max tokens (approx) per chunk before we force a split. ~1500 tokens ≈ 6000 chars.
# H1/H2/H3 boundaries are usually shorter than this; this catches outliers.
_MAX_CHUNK_CHARS = 6000

SUMMARY_PROMPT = (
    "You are summarizing a documentation chunk for a retrieval system. "
    "Write 1-3 plain sentences that describe what this chunk explains and the "
    "key concepts/identifiers it contains. The summary will be embedded and "
    "matched against user questions like 'how do I X?', so use answer-language "
    "vocabulary. Do not start with 'This chunk' or 'This section'. Output the "
    "summary text only — no markdown, no preamble, no quotes."
)


def _vprint(msg: str) -> None:
    if os.environ.get("DOCS_MONITOR_INDEX_VERBOSE") == "1":
        print(f"[doc_index] {msg}", file=sys.stderr)


def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _utcnow() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


@dataclass
class Chunk:
    id: int | None = None
    source_type: str = ""        # 'page' | 'change_event' | 'wiki_synthesis' | 'kg_entity'
    source_id: str = ""          # page filename, change_events.id, etc.
    parent_id: str | None = None
    chunk_type: str = ""         # 'whole' | 'section' | 'event' | 'entity'
    heading_path: str = ""
    content: str = ""
    content_hash: str = ""
    summary: str | None = None
    summary_hash: str | None = None
    metadata: dict = field(default_factory=dict)
    url: str | None = None
    line_start: int | None = None
    line_end: int | None = None
    indexed_at: str = ""

    @classmethod
    def from_row(cls, row: sqlite3.Row) -> "Chunk":
        meta = {}
        if row["metadata_json"]:
            try:
                meta = json.loads(row["metadata_json"])
            except (json.JSONDecodeError, TypeError):
                meta = {}
        return cls(
            id=row["id"],
            source_type=row["source_type"],
            source_id=row["source_id"],
            parent_id=row["parent_id"],
            chunk_type=row["chunk_type"],
            heading_path=row["heading_path"] or "",
            content=row["content"],
            content_hash=row["content_hash"],
            summary=row["summary"],
            summary_hash=row["summary_hash"],
            metadata=meta,
            url=row["url"],
            line_start=row["line_start"],
            line_end=row["line_end"],
            indexed_at=row["indexed_at"],
        )


# ── Chunking ────────────────────────────────────────────────────────────────

def _strip_frontmatter(text: str) -> tuple[str, int]:
    """Strip leading blockquote frontmatter ("> ..." lines). Returns (stripped, lines_dropped)."""
    lines = text.splitlines()
    drop = 0
    for line in lines:
        if line.startswith(">") or line.strip() == "":
            drop += 1
        else:
            break
    return "\n".join(lines[drop:]), drop


def chunk_markdown(text: str, source_id: str) -> list[dict]:
    """Split markdown into section chunks at H1/H2/H3 boundaries.

    Returns a list of dicts with keys:
      heading_path, content, line_start, line_end, chunk_type
    """
    text, dropped = _strip_frontmatter(text)
    lines = text.splitlines()

    # Find heading positions. Each heading marks the *start* of a new chunk.
    # Skip lines inside fenced code blocks (``` ... ```) so code comments
    # like `# script.sh` don't split sections.
    boundaries: list[tuple[int, int, str]] = []  # (line_index, level, title)
    in_fence = False
    fence_marker: str | None = None
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = None
            continue
        if in_fence:
            continue
        m = _HEADING_RE.match(line)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            boundaries.append((i, level, title))

    chunks: list[dict] = []

    # Track heading stack for breadcrumb. Keyed by level.
    stack: dict[int, str] = {}

    if not boundaries:
        # No headings: one whole-document chunk
        content = "\n".join(lines).strip()
        if content:
            chunks.append({
                "heading_path": source_id,
                "content": content,
                "line_start": 1 + dropped,
                "line_end": len(lines) + dropped,
                "chunk_type": "section",
            })
        return chunks

    # Preamble: any content before the first heading
    if boundaries[0][0] > 0:
        preamble = "\n".join(lines[: boundaries[0][0]]).strip()
        if preamble:
            chunks.append({
                "heading_path": f"{source_id} > (preamble)",
                "content": preamble,
                "line_start": 1 + dropped,
                "line_end": boundaries[0][0] + dropped,
                "chunk_type": "section",
            })

    # Walk boundaries, build sections
    for idx, (start, level, title) in enumerate(boundaries):
        end = boundaries[idx + 1][0] if idx + 1 < len(boundaries) else len(lines)
        # Update heading stack — drop any deeper levels
        for k in list(stack.keys()):
            if k >= level:
                stack.pop(k)
        stack[level] = title
        path_parts = [source_id] + [stack[k] for k in sorted(stack.keys())]
        heading_path = " > ".join(path_parts)

        section_text = "\n".join(lines[start:end]).strip()
        if not section_text:
            continue

        # If a section is huge, split on paragraph breaks
        if len(section_text) > _MAX_CHUNK_CHARS:
            for sub_start, sub_text in _split_long_section(section_text):
                chunks.append({
                    "heading_path": heading_path,
                    "content": sub_text,
                    "line_start": start + sub_start + 1 + dropped,
                    "line_end": start + sub_start + sub_text.count("\n") + 1 + dropped,
                    "chunk_type": "section",
                })
        else:
            chunks.append({
                "heading_path": heading_path,
                "content": section_text,
                "line_start": start + 1 + dropped,
                "line_end": end + dropped,
                "chunk_type": "section",
            })

    return chunks


def _split_long_section(text: str) -> Iterator[tuple[int, str]]:
    """Split a long section on paragraph breaks. Yields (start_line_offset, sub_text)."""
    paras = text.split("\n\n")
    buf: list[str] = []
    buf_chars = 0
    line_offset = 0
    sub_start = 0
    for para in paras:
        para_chars = len(para) + 2
        if buf_chars + para_chars > _MAX_CHUNK_CHARS and buf:
            sub_text = "\n\n".join(buf).strip()
            if sub_text:
                yield (sub_start, sub_text)
            sub_start = line_offset
            buf = [para]
            buf_chars = para_chars
        else:
            buf.append(para)
            buf_chars += para_chars
        line_offset += para.count("\n") + 2
    if buf:
        sub_text = "\n\n".join(buf).strip()
        if sub_text:
            yield (sub_start, sub_text)


# ── DocIndex ────────────────────────────────────────────────────────────────


class DocIndex:
    """SQLite + FTS5 chunk index. Composes with EmbeddingCache for vectors."""

    def __init__(self, db_path: Path, embedder: EmbeddingCache | None = None):
        self.db_path = Path(db_path)
        self.embedder = embedder
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(str(self.db_path))
        self._conn.row_factory = sqlite3.Row
        self._init_schema()

    def _init_schema(self) -> None:
        self._conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS doc_chunks (
                id            INTEGER PRIMARY KEY AUTOINCREMENT,
                source_type   TEXT NOT NULL,
                source_id     TEXT NOT NULL,
                parent_id     TEXT,
                chunk_type    TEXT NOT NULL,
                heading_path  TEXT,
                chunk_idx     INTEGER NOT NULL DEFAULT 0,
                content       TEXT NOT NULL,
                content_hash  TEXT NOT NULL,
                summary       TEXT,
                summary_hash  TEXT,
                metadata_json TEXT,
                url           TEXT,
                line_start    INTEGER,
                line_end      INTEGER,
                indexed_at    TEXT NOT NULL,
                UNIQUE (source_type, source_id, chunk_idx)
            );
            CREATE INDEX IF NOT EXISTS idx_chunks_source
                ON doc_chunks(source_type, source_id);
            CREATE INDEX IF NOT EXISTS idx_chunks_hash
                ON doc_chunks(content_hash);
            CREATE INDEX IF NOT EXISTS idx_chunks_summary_hash
                ON doc_chunks(summary_hash);

            CREATE VIRTUAL TABLE IF NOT EXISTS doc_chunks_fts USING fts5(
                content, summary, heading_path,
                content='doc_chunks', content_rowid='id',
                tokenize='porter unicode61'
            );

            CREATE TRIGGER IF NOT EXISTS doc_chunks_ai AFTER INSERT ON doc_chunks BEGIN
                INSERT INTO doc_chunks_fts(rowid, content, summary, heading_path)
                VALUES (new.id, new.content, COALESCE(new.summary, ''), COALESCE(new.heading_path, ''));
            END;
            CREATE TRIGGER IF NOT EXISTS doc_chunks_ad AFTER DELETE ON doc_chunks BEGIN
                INSERT INTO doc_chunks_fts(doc_chunks_fts, rowid, content, summary, heading_path)
                VALUES ('delete', old.id, old.content, COALESCE(old.summary, ''), COALESCE(old.heading_path, ''));
            END;
            CREATE TRIGGER IF NOT EXISTS doc_chunks_au AFTER UPDATE ON doc_chunks BEGIN
                INSERT INTO doc_chunks_fts(doc_chunks_fts, rowid, content, summary, heading_path)
                VALUES ('delete', old.id, old.content, COALESCE(old.summary, ''), COALESCE(old.heading_path, ''));
                INSERT INTO doc_chunks_fts(rowid, content, summary, heading_path)
                VALUES (new.id, new.content, COALESCE(new.summary, ''), COALESCE(new.heading_path, ''));
            END;
            """
        )
        self._conn.commit()

    def close(self) -> None:
        try:
            self._conn.close()
        except Exception:
            pass

    # ── Reindex ─────────────────────────────────────────────────────────────

    def reindex_pages(
        self,
        pages_dir: Path,
        regenerate_summaries: bool = False,
        only_changed: bool = False,
    ) -> dict:
        """Walk pages_dir/**/*.md and (re)index.

        ``only_changed`` skips files whose latest chunk's content_hash already
        matches the file content's hash — used by the auto-incremental hook
        in ``cmd_check`` to avoid full reindex on every run.
        """
        pages_dir = Path(pages_dir)
        if not pages_dir.exists():
            raise FileNotFoundError(f"pages_dir not found: {pages_dir}")

        files = sorted(pages_dir.rglob("*.md"))
        stats = {"files": 0, "chunks_inserted": 0, "chunks_updated": 0, "files_skipped": 0}

        for fpath in files:
            rel = str(fpath.relative_to(pages_dir))
            text = fpath.read_text(encoding="utf-8", errors="replace")

            if only_changed and self._page_unchanged(rel, text):
                stats["files_skipped"] += 1
                continue

            stats["files"] += 1
            chunks = self._build_page_chunks(rel, text)
            inserted, updated = self._upsert_chunks("page", rel, chunks)
            stats["chunks_inserted"] += inserted
            stats["chunks_updated"] += updated

        # Generate summaries for chunks missing them
        if self.embedder:
            self._generate_summaries(force=regenerate_summaries)
            self._embed_outstanding()

        return stats

    def reindex_change_events(self, snapshots_db: Path) -> dict:
        """Pull change_events from the docs snapshots DB and chunk each row."""
        snapshots_db = Path(snapshots_db)
        if not snapshots_db.exists():
            return {"events": 0, "chunks_inserted": 0, "chunks_updated": 0}

        ext = sqlite3.connect(str(snapshots_db))
        ext.row_factory = sqlite3.Row
        try:
            rows = ext.execute(
                "SELECT * FROM change_events ORDER BY id"
            ).fetchall()
        except sqlite3.Error:
            ext.close()
            return {"events": 0, "chunks_inserted": 0, "chunks_updated": 0}
        ext.close()

        stats = {"events": len(rows), "chunks_inserted": 0, "chunks_updated": 0}
        for row in rows:
            chunks = self._build_event_chunks(row)
            inserted, updated = self._upsert_chunks(
                "change_event", str(row["id"]), chunks
            )
            stats["chunks_inserted"] += inserted
            stats["chunks_updated"] += updated

        if self.embedder:
            self._generate_summaries(force=False)
            self._embed_outstanding()

        return stats

    def reindex_all(
        self,
        pages_dir: Path | None = None,
        snapshots_db: Path | None = None,
        regenerate_summaries: bool = False,
    ) -> dict:
        """Convenience: reindex both pages and change_events."""
        results = {}
        if pages_dir:
            results["pages"] = self.reindex_pages(
                pages_dir, regenerate_summaries=regenerate_summaries
            )
        if snapshots_db:
            results["change_events"] = self.reindex_change_events(snapshots_db)
        return results

    # ── Reads ───────────────────────────────────────────────────────────────

    def get_chunk(self, chunk_id: int) -> Chunk | None:
        row = self._conn.execute(
            "SELECT * FROM doc_chunks WHERE id = ?", (chunk_id,)
        ).fetchone()
        return Chunk.from_row(row) if row else None

    def get_chunks_by_source(
        self, source_type: str, source_id: str
    ) -> list[Chunk]:
        rows = self._conn.execute(
            "SELECT * FROM doc_chunks WHERE source_type = ? AND source_id = ? "
            "ORDER BY line_start, id",
            (source_type, source_id),
        ).fetchall()
        return [Chunk.from_row(r) for r in rows]

    def all_chunks(self, source_type: str | None = None) -> Iterator[Chunk]:
        q = "SELECT * FROM doc_chunks"
        params: tuple = ()
        if source_type:
            q += " WHERE source_type = ?"
            params = (source_type,)
        for row in self._conn.execute(q, params):
            yield Chunk.from_row(row)

    def stats(self) -> dict:
        rows = self._conn.execute(
            "SELECT source_type, COUNT(*) as n FROM doc_chunks GROUP BY source_type"
        ).fetchall()
        by_type = {r["source_type"]: r["n"] for r in rows}
        total = sum(by_type.values())
        n_with_summary = self._conn.execute(
            "SELECT COUNT(*) FROM doc_chunks WHERE summary IS NOT NULL"
        ).fetchone()[0]
        return {
            "total_chunks": total,
            "by_source_type": by_type,
            "chunks_with_summary": n_with_summary,
        }

    # FTS5 search interface for retriever.py
    def fts_search(
        self,
        query: str,
        limit: int = 50,
        source_type: str | list[str] | None = None,
    ) -> list[tuple[int, float]]:
        """Run BM25 search via FTS5. Returns [(chunk_id, bm25_score), ...].

        Lower BM25 score = better match (FTS5 convention: ranks via -bm25()).
        We negate so higher = better, matching cosine convention.
        """
        # Sanitize query: strip FTS5 syntax chars that would parse-error
        clean = re.sub(r'[^\w\s\-\*]', ' ', query).strip()
        if not clean:
            return []

        sql = (
            "SELECT c.id, bm25(doc_chunks_fts) as score "
            "FROM doc_chunks_fts "
            "JOIN doc_chunks c ON c.id = doc_chunks_fts.rowid "
            "WHERE doc_chunks_fts MATCH ? "
        )
        params: list = [clean]
        if source_type:
            if isinstance(source_type, str):
                sql += "AND c.source_type = ? "
                params.append(source_type)
            else:
                placeholders = ",".join("?" * len(source_type))
                sql += f"AND c.source_type IN ({placeholders}) "
                params.extend(source_type)
        sql += "ORDER BY score LIMIT ?"
        params.append(limit)

        try:
            rows = self._conn.execute(sql, params).fetchall()
        except sqlite3.OperationalError as e:
            # Malformed FTS query — return empty rather than crash
            _vprint(f"FTS5 query failed: {e!r}")
            return []
        # Negate so higher = better
        return [(int(r["id"]), -float(r["score"])) for r in rows]

    def filter_chunk_ids(
        self,
        source_type: str | list[str] | None = None,
        category: str | list[str] | None = None,
        severity: str | list[str] | None = None,
        page: str | None = None,
        since: str | None = None,
        until: str | None = None,
        tags: list[str] | None = None,
    ) -> set[int]:
        """Return the set of chunk IDs matching the given metadata filters.

        For metadata stored in metadata_json, we use SQLite's json_extract.
        """
        clauses = []
        params: list = []
        if source_type:
            if isinstance(source_type, str):
                clauses.append("source_type = ?")
                params.append(source_type)
            else:
                placeholders = ",".join("?" * len(source_type))
                clauses.append(f"source_type IN ({placeholders})")
                params.extend(source_type)
        if category:
            if isinstance(category, str):
                clauses.append("json_extract(metadata_json, '$.category') = ?")
                params.append(category)
            else:
                placeholders = ",".join("?" * len(category))
                clauses.append(
                    f"json_extract(metadata_json, '$.category') IN ({placeholders})"
                )
                params.extend(category)
        if severity:
            if isinstance(severity, str):
                clauses.append("json_extract(metadata_json, '$.severity') = ?")
                params.append(severity)
            else:
                placeholders = ",".join("?" * len(severity))
                clauses.append(
                    f"json_extract(metadata_json, '$.severity') IN ({placeholders})"
                )
                params.extend(severity)
        if page:
            clauses.append(
                "(source_id LIKE ? OR json_extract(metadata_json, '$.page_name') LIKE ?)"
            )
            params.extend([f"%{page}%", f"%{page}%"])
        if since:
            clauses.append(
                "COALESCE(json_extract(metadata_json, '$.run_timestamp'), indexed_at) >= ?"
            )
            params.append(since)
        if until:
            clauses.append(
                "COALESCE(json_extract(metadata_json, '$.run_timestamp'), indexed_at) <= ?"
            )
            params.append(until)
        if tags:
            for t in tags:
                clauses.append("metadata_json LIKE ?")
                params.append(f'%"{t}"%')

        sql = "SELECT id FROM doc_chunks"
        if clauses:
            sql += " WHERE " + " AND ".join(clauses)
        rows = self._conn.execute(sql, params).fetchall()
        return {int(r["id"]) for r in rows}

    # ── Internals ───────────────────────────────────────────────────────────

    def _page_unchanged(self, rel_path: str, text: str) -> bool:
        """Cheap check: does the existing 'whole' chunk's content_hash match?"""
        whole_hash = _sha256(text.strip())
        row = self._conn.execute(
            "SELECT content_hash FROM doc_chunks "
            "WHERE source_type='page' AND source_id=? AND chunk_type='whole'",
            (rel_path,),
        ).fetchone()
        return row is not None and row["content_hash"] == whole_hash

    def _build_page_chunks(self, rel_path: str, text: str) -> list[dict]:
        """Build a list of chunk-dicts (sections + whole-page) for a page."""
        sections = chunk_markdown(text, rel_path)
        whole = {
            "heading_path": rel_path,
            "content": text.strip(),
            "line_start": 1,
            "line_end": text.count("\n") + 1,
            "chunk_type": "whole",
        }
        out = [whole] + sections
        return out

    def _build_event_chunks(self, row: sqlite3.Row) -> list[dict]:
        """One chunk per change_event. Falls back to diff_text if metadata is NULL."""
        parts: list[str] = []
        if row["summary"]:
            parts.append(f"Summary: {row['summary']}")
        if row["details"]:
            parts.append(f"Details: {row['details']}")
        if row["action_required"]:
            parts.append(f"Action: {row['action_required']}")
        if row["diff_text"]:
            parts.append(f"Diff:\n{row['diff_text']}")

        content = "\n\n".join(parts).strip()
        if not content:
            return []

        # Heading path encodes context for FTS5 matching
        page_name = row["page_name"] or "unknown.md"
        ts = row["run_timestamp"] or row["created_at"] or ""
        category = row["category"] or "unclassified"
        heading_path = f"change_event[{row['id']}] > {page_name} > {category} ({ts})"

        tags: list[str] = []
        if row["tags_json"]:
            try:
                tags = json.loads(row["tags_json"]) or []
            except (json.JSONDecodeError, TypeError):
                pass

        meta = {
            "category": row["category"],
            "severity": row["severity"],
            "run_timestamp": row["run_timestamp"],
            "page_name": page_name,
            "tags": tags,
            "action_required": row["action_required"],
            "gh_issue_url": row["gh_issue_url"],
            "event_type": row["event_type"],
        }

        return [{
            "heading_path": heading_path,
            "content": content,
            "line_start": None,
            "line_end": None,
            "chunk_type": "event",
            "metadata": meta,
            "url": row["url"],
        }]

    def _upsert_chunks(
        self,
        source_type: str,
        source_id: str,
        chunks: list[dict],
    ) -> tuple[int, int]:
        """Insert or update chunks for a single source. Returns (inserted, updated).

        Strategy: position-based upsert. Each new chunk has a chunk_idx (0..N-1)
        within the source. Existing chunks at higher positions are dropped.
        Chunks at the same position are content-hash compared — if unchanged, the
        existing summary is preserved (no LLM re-call needed).
        """
        now = _utcnow()
        inserted = updated = 0

        existing = self._conn.execute(
            "SELECT id, chunk_idx, content_hash FROM doc_chunks "
            "WHERE source_type = ? AND source_id = ? ORDER BY chunk_idx",
            (source_type, source_id),
        ).fetchall()
        existing_by_idx = {r["chunk_idx"]: r for r in existing}

        # Drop chunks that exist at positions beyond the new chunk count
        for idx, row in existing_by_idx.items():
            if idx >= len(chunks):
                self._conn.execute("DELETE FROM doc_chunks WHERE id = ?", (row["id"],))

        for chunk_idx, c in enumerate(chunks):
            content = c["content"]
            content_hash = _sha256(content)
            metadata_json = json.dumps(c.get("metadata", {})) if c.get("metadata") else None
            existing_row = existing_by_idx.get(chunk_idx)

            if existing_row is None:
                self._conn.execute(
                    "INSERT INTO doc_chunks "
                    "(source_type, source_id, parent_id, chunk_type, heading_path, "
                    " chunk_idx, content, content_hash, summary, summary_hash, "
                    " metadata_json, url, line_start, line_end, indexed_at) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (
                        source_type, source_id, None, c["chunk_type"], c["heading_path"],
                        chunk_idx, content, content_hash, None, None, metadata_json,
                        c.get("url"), c.get("line_start"), c.get("line_end"), now,
                    ),
                )
                inserted += 1
            elif existing_row["content_hash"] != content_hash:
                self._conn.execute(
                    "UPDATE doc_chunks SET chunk_type = ?, heading_path = ?, "
                    "content = ?, content_hash = ?, summary = NULL, summary_hash = NULL, "
                    "metadata_json = ?, url = ?, line_start = ?, line_end = ?, "
                    "indexed_at = ? WHERE id = ?",
                    (
                        c["chunk_type"], c["heading_path"], content, content_hash,
                        metadata_json, c.get("url"), c.get("line_start"),
                        c.get("line_end"), now, existing_row["id"],
                    ),
                )
                updated += 1
            else:
                self._conn.execute(
                    "UPDATE doc_chunks SET chunk_type = ?, heading_path = ?, "
                    "metadata_json = ?, url = ?, line_start = ?, line_end = ? "
                    "WHERE id = ?",
                    (c["chunk_type"], c["heading_path"], metadata_json,
                     c.get("url"), c.get("line_start"), c.get("line_end"),
                     existing_row["id"]),
                )

        self._conn.commit()
        return inserted, updated

    def _generate_summaries(self, force: bool = False, batch_size: int = 10) -> int:
        """Generate LLM summaries for chunks lacking them. Returns # generated."""
        from llm_backend import call_claude  # lazy import: avoid circular load

        sql = "SELECT id, content, heading_path FROM doc_chunks WHERE summary IS NULL"
        if force:
            sql = "SELECT id, content, heading_path FROM doc_chunks"
        rows = self._conn.execute(sql).fetchall()
        if not rows:
            return 0

        _vprint(f"generating summaries for {len(rows)} chunks (batch_size={batch_size})")
        generated = 0

        # Process in small batches; each call summarizes a batch's worth
        for i in range(0, len(rows), batch_size):
            batch = rows[i : i + batch_size]
            for r in batch:
                # Cap content length to avoid huge prompts; first 4000 chars suffices
                content = r["content"][:4000]
                heading = r["heading_path"] or ""
                user_msg = (
                    f"Heading path: {heading}\n\n"
                    f"Content:\n{content}\n\n"
                    f"Output: 1-3 sentences."
                )
                try:
                    summary = call_claude(
                        prompt=SUMMARY_PROMPT,
                        stdin=user_msg,
                        model="sonnet",
                        max_tokens=300,
                        timeout=60,
                    ).strip()
                except Exception as e:
                    _vprint(f"summary failed for chunk {r['id']}: {e!r}")
                    continue
                if not summary:
                    continue
                summary_hash = _sha256(summary)
                self._conn.execute(
                    "UPDATE doc_chunks SET summary = ?, summary_hash = ? WHERE id = ?",
                    (summary, summary_hash, r["id"]),
                )
                generated += 1
            self._conn.commit()
            _vprint(f"summaries: {generated}/{len(rows)} done")

        return generated

    def _embed_outstanding(self) -> tuple[int, int]:
        """Embed any chunk content_hash and summary_hash not yet in the cache.

        Returns (content_embedded, summary_embedded). Cache hits are no-ops.
        """
        if not self.embedder:
            return 0, 0

        rows = self._conn.execute(
            "SELECT content, summary FROM doc_chunks"
        ).fetchall()
        contents = [r["content"] for r in rows]
        summaries = [r["summary"] for r in rows if r["summary"]]

        if contents:
            self.embedder.embed(contents)
        if summaries:
            self.embedder.embed(summaries)

        return len(contents), len(summaries)


__all__ = ["DocIndex", "Chunk", "chunk_markdown"]
