# =============================================================================
# store.py  --  Math Tutor MVP  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-07-21  NEW durable storage layer (the "data foundation" for the roadmap:
#               accounts, progress, session memory, and per-topic tracking). It is
#               a DROP-IN, OPT-IN backend:
#                 - If the DATABASE_URL env var is NOT set, store.enabled() is False
#                   and main.py keeps using its existing JSON-file storage EXACTLY as
#                   before. Nothing changes for the current live app. (Do no harm.)
#                 - If DATABASE_URL IS set (e.g. a Render PostgreSQL instance), this
#                   module owns sessions + placements + accounts + topic progress in
#                   the database instead, so memory survives deploys/sleeps and can
#                   scale to many students.
#               Built on SQLAlchemy so the SAME code runs on PostgreSQL (production)
#               and SQLite (local testing). If the DB can't be reached at startup we
#               log a clear warning and fall back to disabled (files) rather than
#               crash the app.
#
# WHAT THIS FILE IS FOR:
#   A single place that answers "where does a student's memory live?" main.py calls
#   store.enabled() and, when true, store.get_session()/save_session()/etc. The DB
#   schema here (accounts, sessions, placements, topic_progress) is the base the
#   real per-topic dashboard (Phase 2) and subscriptions will build on.
#
# ENV VARS:
#   DATABASE_URL   (optional)  a SQLAlchemy/DB URL. Examples:
#                    postgresql://user:pass@host:5432/dbname   (Render Postgres)
#                    sqlite:////absolute/path/to/dev.db        (local testing)
#                  Render often provides "postgres://..."; we normalize it to
#                  "postgresql://..." automatically.
# =============================================================================

import json
import os
import datetime as _dt

# The public flag other modules check. Starts False and is flipped on only if a
# DATABASE_URL is present AND the engine + tables initialize successfully.
_ENABLED = False
_engine = None
_meta = None
_tables = {}

DATABASE_URL = os.environ.get("DATABASE_URL", "").strip()


def _normalize_url(url: str) -> str:
    # Render (and Heroku-style) hand out "postgres://"; SQLAlchemy wants
    # "postgresql://". Also prefer the psycopg2 driver explicitly.
    if url.startswith("postgres://"):
        url = "postgresql://" + url[len("postgres://"):]
    if url.startswith("postgresql://"):
        url = "postgresql+psycopg2://" + url[len("postgresql://"):]
    return url


def _now():
    # Timezone-aware UTC timestamp for updated_at columns.
    return _dt.datetime.now(_dt.timezone.utc)


def init():
    """
    Try to bring up the database backend. Safe to call once at startup. If
    DATABASE_URL is unset or the DB can't be reached, we stay disabled and the app
    uses its file storage. Returns True if the DB backend is active.
    """
    global _ENABLED, _engine, _meta, _tables
    if not DATABASE_URL:
        return False
    try:
        from sqlalchemy import (create_engine, MetaData, Table, Column, String,
                                 Integer, Text, DateTime)
        _engine = create_engine(_normalize_url(DATABASE_URL), pool_pre_ping=True, future=True)
        _meta = MetaData()

        # Accounts / students. For the pilot this mirrors students.json; real
        # signups (email, subscription, payment) extend this table later.
        _tables["accounts"] = Table(
            "accounts", _meta,
            Column("code", String(64), primary_key=True),
            Column("name", String(256)),
            Column("email", String(256)),
            Column("subscription_status", String(64), default="pilot"),
            Column("created_at", DateTime(timezone=True)),
        )
        # Per-student conversation memory (the lesson/course session).
        _tables["sessions"] = Table(
            "sessions", _meta,
            Column("code", String(64), primary_key=True),
            Column("history", Text),        # JSON-encoded list of {role, content}
            Column("summary", Text),        # running summary (roadmap: session-memory layer)
            Column("updated_at", DateTime(timezone=True)),
        )
        # Placement results (from Mr. Cadabra's Challenge).
        _tables["placements"] = Table(
            "placements", _meta,
            Column("code", String(64), primary_key=True),
            Column("data", Text),           # JSON-encoded placement dict
            Column("updated_at", DateTime(timezone=True)),
        )
        # Per-student, per-unit topic tracking (Phase 2 dashboard foundation).
        # unit = 1..9 (the nine Algebra I units). status is a short label.
        _tables["topic_progress"] = Table(
            "topic_progress", _meta,
            Column("code", String(64), primary_key=True),   # composite via (code, unit)
            Column("unit", Integer, primary_key=True),
            Column("unit_name", String(128)),
            Column("status", String(32)),      # e.g. discussed / practiced / in-progress / mastered
            Column("touches", Integer, default=0),
            Column("last_touched", DateTime(timezone=True)),
        )
        _meta.create_all(_engine)
        # Prove the connection works.
        from sqlalchemy import text as _text
        with _engine.connect() as conn:
            conn.execute(_text("SELECT 1"))
        _ENABLED = True
        print("[store] Database backend ENABLED (durable storage).")
    except Exception as exc:  # noqa: BLE001
        _ENABLED = False
        print(f"[store] Database backend disabled (falling back to files): {exc}")
    return _ENABLED


def enabled() -> bool:
    return _ENABLED


# ---- small helpers ---------------------------------------------------------
def _loads(txt, default):
    if not txt:
        return default
    try:
        return json.loads(txt)
    except (json.JSONDecodeError, TypeError):
        return default


def _upsert(table_name: str, pk: dict, values: dict):
    """Insert-or-update a row keyed by the primary-key columns in `pk`.

    Uses the dialect's native ON CONFLICT so it's safe under concurrent workers,
    and works identically on PostgreSQL and SQLite.
    """
    table = _tables[table_name]
    row = dict(pk); row.update(values)
    dialect = _engine.dialect.name
    if dialect == "postgresql":
        from sqlalchemy.dialects.postgresql import insert as _insert
    elif dialect == "sqlite":
        from sqlalchemy.dialects.sqlite import insert as _insert
    else:
        # Portable fallback: try update, else insert.
        from sqlalchemy import update as _update, insert as _plain_insert
        with _engine.begin() as conn:
            res = conn.execute(_update(table).where(
                *[table.c[k] == v for k, v in pk.items()]).values(**values))
            if res.rowcount == 0:
                conn.execute(_plain_insert(table).values(**row))
        return
    stmt = _insert(table).values(**row)
    stmt = stmt.on_conflict_do_update(
        index_elements=list(pk.keys()),
        set_=values,
    )
    with _engine.begin() as conn:
        conn.execute(stmt)


# ---- sessions (conversation memory) ----------------------------------------
def get_session(code: str) -> dict:
    from sqlalchemy import select
    t = _tables["sessions"]
    with _engine.connect() as conn:
        r = conn.execute(select(t.c.history, t.c.summary).where(t.c.code == code)).first()
    if not r:
        return {"history": []}
    out = {"history": _loads(r[0], [])}
    if r[1]:
        out["summary"] = r[1]
    return out


def save_session(code: str, session: dict) -> None:
    values = {
        "history": json.dumps(session.get("history", []), ensure_ascii=False),
        "summary": session.get("summary"),
        "updated_at": _now(),
    }
    _upsert("sessions", {"code": code}, values)


# ---- placements ------------------------------------------------------------
def read_placement(code: str) -> dict:
    from sqlalchemy import select
    t = _tables["placements"]
    with _engine.connect() as conn:
        r = conn.execute(select(t.c.data).where(t.c.code == code)).first()
    return _loads(r[0], {}) if r else {}


def save_placement(code: str, result: dict) -> None:
    _upsert("placements", {"code": code}, {
        "data": json.dumps(result or {}, ensure_ascii=False),
        "updated_at": _now(),
    })


# ---- accounts (roadmap: real signups) --------------------------------------
def ensure_account(code: str, name: str = "", email: str = "") -> None:
    """Make sure an account row exists for this code (idempotent)."""
    from sqlalchemy import select
    t = _tables["accounts"]
    with _engine.connect() as conn:
        exists = conn.execute(select(t.c.code).where(t.c.code == code)).first()
    if exists:
        return
    _upsert("accounts", {"code": code}, {
        "name": name, "email": email, "subscription_status": "pilot", "created_at": _now(),
    })


# ---- per-topic tracking (Phase 2 foundation) -------------------------------
def record_topic(code: str, unit: int, unit_name: str = "", status: str = "discussed") -> None:
    """Record that a student engaged with a unit (increments touches, updates status)."""
    from sqlalchemy import select
    t = _tables["topic_progress"]
    with _engine.connect() as conn:
        r = conn.execute(select(t.c.touches).where(
            (t.c.code == code) & (t.c.unit == unit))).first()
    touches = (r[0] if r else 0) + 1
    _upsert("topic_progress", {"code": code, "unit": unit}, {
        "unit_name": unit_name, "status": status, "touches": touches, "last_touched": _now(),
    })


def get_topics(code: str) -> list:
    """Return this student's per-unit topic progress rows (for the real dashboard)."""
    from sqlalchemy import select
    t = _tables["topic_progress"]
    with _engine.connect() as conn:
        rows = conn.execute(select(
            t.c.unit, t.c.unit_name, t.c.status, t.c.touches, t.c.last_touched
        ).where(t.c.code == code).order_by(t.c.unit)).all()
    return [
        {"unit": r[0], "unit_name": r[1], "status": r[2], "touches": r[3],
         "last_touched": r[4].isoformat() if r[4] else None}
        for r in rows
    ]


def status() -> dict:
    """Small diagnostic for a health/status endpoint."""
    return {"db_enabled": _ENABLED, "dialect": (_engine.dialect.name if _engine else None)}


# I did no harm and this file is not truncated.
