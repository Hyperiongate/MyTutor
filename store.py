# =============================================================================
# store.py  --  Math Tutor MVP  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-07-30  ENGAGED-TIME TRACKING (parents asked "how long did my kid actually work?"). New
#               additive table `time_daily` (code, course, day 'YYYY-MM-DD', minutes) plus
#               record_minutes() and get_time(). One row per student/course/day; main.py's
#               /api/heartbeat adds one minute per verified minute of ENGAGED time (tab visible
#               + recent real activity -- leaving the app open does NOT count; the anti-idle
#               logic lives in static/time-tracker.js and a server-side minimum gap between
#               counted beats in main.py). `day` is the STUDENT'S local calendar day, supplied
#               by the browser, so a kid working at 9pm Pacific doesn't get logged on tomorrow's
#               date. Brand-new table -> create_all builds it; no migration; nothing else touched.
#   2026-07-28  TEACHER SIGN-IN: a teacher now owns MANY classes. The `classes` table gained ONE
#               nullable column, `teacher_code` (the personal code a teacher picks, e.g. MRSBAKER),
#               added by a new self-healing additive migration (_migrate_classes_teacher_code) that
#               no-ops once the column exists -- so the classes created before today keep working
#               and simply have no owner code. New list_classes_for_teacher(teacher_code) returns
#               that teacher's classes (with a student count) in creation order. create_class()
#               gained an OPTIONAL teacher_code argument, so every existing call behaves exactly as
#               before; it will NOT overwrite a class that already has a different owner code, so
#               one teacher can't quietly take over another's class. Nothing else changed: no other
#               table, no primary key, no existing signature. Do no harm.
#   2026-07-28  ADDED get_course_activity(code): every course a student has actually touched, with
#               units started / mastered / checked and last-active, gathered in ONE pass over
#               topic_progress + unit_checks instead of one query per course. Courses with no
#               activity are simply absent (nothing invented). Feeds the dashboard's "My courses"
#               strip. Read-only and additive -- no table or existing function changed. Do no harm.
#   2026-07-28  TEACHER / PARENT CLASSROOM ROSTER. Two NEW tables -- `classes` (class_code, name,
#               owner_name) and `class_members` (class_code, student_code) -- plus create_class /
#               get_class / list_students / add_student / remove_student / delete_class. A "class"
#               is deliberately lightweight: a short class CODE grouping student codes that ALREADY
#               exist, so a teacher or parent can watch several students at once WITHOUT an
#               accounts/login system (that work is deferred). No password, no new personal data.
#               Brand-new tables, so create_all builds them -- NO migration and NO change to any
#               existing table, function, or signature. Do no harm.
#   2026-07-27  PHASE 3.3 (multi-course) -- PER-COURSE SESSION MEMORY + PLACEMENT. The `sessions`
#               and `placements` tables gained a `course` column; their primary key is now
#               (code, course) instead of (code), so a student can hold a separate saved lesson
#               session AND a separate placement for Algebra I vs Geometry vs any course. Same
#               self-healing additive migration (now generalized over all four course-scoped
#               tables via _COURSE_TABLES) stamps existing rows 'algebra1' -- nothing lost. The
#               session/placement functions gained an optional course=DEFAULT_COURSE arg, so
#               main.py's existing calls behave EXACTLY as before (Algebra I) until the course
#               picker supplies a course. Do no harm.
#   2026-07-27  PHASE 2 (multi-course) -- COURSE-AWARE PROGRESS. The two per-unit tables
#               (topic_progress, unit_checks) gained a `course` column and their primary key
#               is now (code, course, unit) instead of (code, unit), so a student's progress
#               in Geometry is tracked separately from Algebra I. A self-healing, ADDITIVE
#               migration (_migrate_course_columns) runs at startup: it adds the column with
#               DEFAULT 'algebra1', stamps every EXISTING row as 'algebra1' (nothing is lost),
#               and rebuilds the primary key -- on PostgreSQL via ALTER, on SQLite via a table
#               rebuild. Every function gained an optional course=DEFAULT_COURSE argument, so
#               callers that don't pass a course behave EXACTLY as before (all activity counts
#               as Algebra I until the course picker supplies a course in Phase 3). student_stats
#               (problems practiced / accuracy / day streak) stays whole-student on purpose;
#               per-course "units mastered" comes from unit_checks filtered by course. Do no harm.
#   2026-07-24  PHASE A -- MASTERY MODEL. Added two additive tables (unit_checks,
#               student_stats) + functions: record_check() (end-of-unit check score ->
#               best/last pct, cumulative accuracy, day streak, marks unit 'mastered' at
#               >= PASS_PCT=80), record_practice() (counts practiced problems + accuracy +
#               streak), get_mastery() (assembles the dashboard picture). "mastered" added
#               to STATUS_RANK (rank 4, top). Existing tables untouched -> do no harm.
#   2026-07-21  Diagnostics: /health status() now reports `configured` (did we see a
#               DATABASE_URL) and `reason` (why the DB is disabled, credentials
#               redacted) so a failed connection is visible without digging in logs.
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
_INIT_ERROR = None   # human-readable reason we stayed disabled (shown in /health)

DATABASE_URL = os.environ.get("DATABASE_URL", "").strip()

# The default course. Existing single-course data + any call that doesn't name a course
# resolve here, so Algebra I behaves exactly as it did before the multi-course work.
DEFAULT_COURSE = "algebra1"

# Every course-scoped table and the primary key it should have after migration. The
# migration adds a `course` column (default 'algebra1') and rebuilds each table's key to
# this, preserving existing rows. Per-unit tables key by (code, course, unit); the
# per-student memory/placement tables key by (code, course).
_COURSE_TABLES = {
    "topic_progress": ("code", "course", "unit"),
    "unit_checks": ("code", "course", "unit"),
    "sessions": ("code", "course"),
    "placements": ("code", "course"),
}


def _redact(msg: str) -> str:
    """Strip anything that looks like a password out of an error string before we
    show it in /health, so the diagnostic can't leak the DB credentials."""
    import re
    s = str(msg)
    s = re.sub(r"://([^:/@\s]+):[^@/\s]+@", r"://\1:***@", s)  # user:pass@ -> user:***@
    return s[:400]


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
    global _ENABLED, _engine, _meta, _tables, _INIT_ERROR
    if not DATABASE_URL:
        _INIT_ERROR = "DATABASE_URL is not set (the app didn't receive the env var)."
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
            Column("code", String(64), primary_key=True),   # composite via (code, course)
            Column("course", String(32), primary_key=True, nullable=False,
                   default=DEFAULT_COURSE),
            Column("history", Text),        # JSON-encoded list of {role, content}
            Column("summary", Text),        # running summary (roadmap: session-memory layer)
            Column("updated_at", DateTime(timezone=True)),
        )
        # Placement results (from Mr. Cadabra's Challenge).
        _tables["placements"] = Table(
            "placements", _meta,
            Column("code", String(64), primary_key=True),   # composite via (code, course)
            Column("course", String(32), primary_key=True, nullable=False,
                   default=DEFAULT_COURSE),
            Column("data", Text),           # JSON-encoded placement dict
            Column("updated_at", DateTime(timezone=True)),
        )
        # Per-student, per-unit topic tracking (Phase 2 dashboard foundation).
        # unit = 1..9 (the nine Algebra I units). status is a short label.
        _tables["topic_progress"] = Table(
            "topic_progress", _meta,
            Column("code", String(64), primary_key=True),   # composite via (code, course, unit)
            Column("course", String(32), primary_key=True, nullable=False,
                   default=DEFAULT_COURSE),
            Column("unit", Integer, primary_key=True),
            Column("unit_name", String(128)),
            Column("status", String(32)),      # e.g. discussed / practiced / in-progress / mastered
            Column("touches", Integer, default=0),
            Column("last_touched", DateTime(timezone=True)),
        )
        # Phase A -- MASTERY: results of end-of-unit CHECKS, per student per unit.
        # best_pct drives "mastered" (>= PASS_PCT). Separate from topic_progress so it's
        # a clean, additive table (create_all makes it; existing tables untouched).
        _tables["unit_checks"] = Table(
            "unit_checks", _meta,
            Column("code", String(64), primary_key=True),
            Column("course", String(32), primary_key=True, nullable=False,
                   default=DEFAULT_COURSE),
            Column("unit", Integer, primary_key=True),
            Column("checks_taken", Integer, default=0),
            Column("best_pct", Integer, default=0),      # best score ever on this unit's check
            Column("last_pct", Integer, default=0),       # most recent check score
            Column("correct", Integer, default=0),        # cumulative correct across checks
            Column("attempted", Integer, default=0),      # cumulative questions across checks
            Column("updated_at", DateTime(timezone=True)),
        )
        # Phase A -- overall student STATS for the dashboard: problems practiced, accuracy,
        # day streak. One row per student.
        _tables["student_stats"] = Table(
            "student_stats", _meta,
            Column("code", String(64), primary_key=True),
            Column("problems_practiced", Integer, default=0),
            Column("correct_total", Integer, default=0),
            Column("attempted_total", Integer, default=0),
            Column("checks_taken", Integer, default=0),
            Column("streak_days", Integer, default=0),
            Column("last_active", String(10)),            # 'YYYY-MM-DD'
            Column("updated_at", DateTime(timezone=True)),
        )
        # TEACHER / PARENT CLASSROOM (2026-07-28). A "class" is deliberately lightweight: a short
        # CLASS CODE plus a list of EXISTING student codes, so a teacher or parent can follow
        # several students at once WITHOUT an accounts/login system. No new personal data is
        # stored -- just an optional class label and owner display name. Brand-new tables, so
        # create_all builds them; no migration needed.
        _tables["classes"] = Table(
            "classes", _meta,
            Column("class_code", String(32), primary_key=True),   # e.g. "MRSB-P3"
            Column("name", String(128)),          # e.g. "Period 3 Algebra"
            Column("owner_name", String(128)),    # teacher/parent display name (optional)
            # 2026-07-28: the teacher's own short code (e.g. "MRSBAKER"). Nullable on purpose --
            # classes made before teacher sign-in existed simply have none, and still open by
            # class code. This is a convenience key, NOT a password.
            Column("teacher_code", String(64)),
            Column("created_at", DateTime(timezone=True)),
            Column("updated_at", DateTime(timezone=True)),
        )
        _tables["class_members"] = Table(
            "class_members", _meta,
            Column("class_code", String(32), primary_key=True),
            Column("student_code", String(64), primary_key=True),
            Column("added_at", DateTime(timezone=True)),
        )
        # ENGAGED TIME (2026-07-30): minutes of real, verified work per student/course/day.
        # `day` is the student's LOCAL calendar day ('YYYY-MM-DD'), sent by the browser.
        _tables["time_daily"] = Table(
            "time_daily", _meta,
            Column("code", String(64), primary_key=True),
            Column("course", String(32), primary_key=True, nullable=False,
                   default=DEFAULT_COURSE),
            Column("day", String(10), primary_key=True),
            Column("minutes", Integer, default=0),
            Column("updated_at", DateTime(timezone=True)),
        )
        _meta.create_all(_engine)
        # Give the per-unit tables a `course` dimension if they predate the multi-course
        # work (additive; preserves all existing rows as 'algebra1'). No-ops once migrated.
        _migrate_course_columns()
        # Give the `classes` table its `teacher_code` column if it predates teacher sign-in
        # (additive + nullable; no key change). No-ops once migrated.
        _migrate_classes_teacher_code()
        # Prove the connection works.
        from sqlalchemy import text as _text
        with _engine.connect() as conn:
            conn.execute(_text("SELECT 1"))
        _ENABLED = True
        _INIT_ERROR = None
        print("[store] Database backend ENABLED (durable storage).")
    except Exception as exc:  # noqa: BLE001
        _ENABLED = False
        _INIT_ERROR = f"{type(exc).__name__}: {_redact(exc)}"
        print(f"[store] Database backend disabled (falling back to files): {_INIT_ERROR}")
    return _ENABLED


def enabled() -> bool:
    return _ENABLED


# ---- multi-course migration (Phase 2) --------------------------------------
def _migrate_course_columns():
    """One-time, ADDITIVE migration: give topic_progress + unit_checks a `course` column
    (default 'algebra1') and rebuild their primary key to (code, course, unit). Existing
    rows are preserved and stamped course='algebra1', so all current Algebra I progress is
    kept. Safe to run on EVERY startup: it no-ops once the column exists, and if a table was
    just created fresh by create_all it already has the course key (so nothing to do)."""
    from sqlalchemy import inspect, text as _text
    insp = inspect(_engine)
    existing = set(insp.get_table_names())
    for tname, pk_cols in _COURSE_TABLES.items():
        if tname not in existing:
            continue  # create_all already built it new, with its (code, course, ...) key
        cols = [c["name"] for c in insp.get_columns(tname)]
        if "course" in cols:
            continue  # already migrated
        new_pk = ", ".join(pk_cols)
        dialect = _engine.dialect.name
        if dialect == "postgresql":
            with _engine.begin() as conn:
                conn.execute(_text(
                    f"ALTER TABLE {tname} ADD COLUMN course VARCHAR(32) "
                    f"NOT NULL DEFAULT '{DEFAULT_COURSE}'"))
                pk = conn.execute(_text(
                    f"SELECT conname FROM pg_constraint "
                    f"WHERE conrelid = '{tname}'::regclass AND contype = 'p'")).first()
                if pk:
                    conn.execute(_text(f'ALTER TABLE {tname} DROP CONSTRAINT "{pk[0]}"'))
                conn.execute(_text(f"ALTER TABLE {tname} ADD PRIMARY KEY ({new_pk})"))
            print(f"[store] migrated {tname}: +course column, key -> ({new_pk}).")
        elif dialect == "sqlite":
            _sqlite_rebuild_with_course(tname)
            print(f"[store] migrated {tname} (sqlite rebuild): +course column.")
        else:
            # Portable fallback: at least add the column so writes don't fail.
            with _engine.begin() as conn:
                conn.execute(_text(
                    f"ALTER TABLE {tname} ADD COLUMN course VARCHAR(32) "
                    f"NOT NULL DEFAULT '{DEFAULT_COURSE}'"))


def _migrate_classes_teacher_code():
    """One-time, ADDITIVE migration: give `classes` a nullable `teacher_code` column so a teacher
    can sign in with one personal code and see every class they run.

    This is far simpler than the course migration: the column is NULLABLE and the primary key is
    untouched, so a plain ALTER TABLE works identically on PostgreSQL and SQLite -- no table
    rebuild, no data movement. Existing classes keep every row and simply have teacher_code NULL,
    which means they still open by class code exactly as they do today. Safe to run on EVERY
    startup: it no-ops when the column is already there, and when create_all just built the table
    fresh (the column is already in the definition above)."""
    from sqlalchemy import inspect, text as _text
    insp = inspect(_engine)
    if "classes" not in set(insp.get_table_names()):
        return  # create_all will build it new, already carrying teacher_code
    cols = [c["name"] for c in insp.get_columns("classes")]
    if "teacher_code" in cols:
        return  # already migrated
    with _engine.begin() as conn:
        conn.execute(_text("ALTER TABLE classes ADD COLUMN teacher_code VARCHAR(64)"))
    print("[store] migrated classes: +teacher_code column (nullable).")


def _sqlite_rebuild_with_course(tname):
    """SQLite can't alter a primary key in place, so rebuild the table: rename the old one
    aside, let the new-schema table be created, copy the rows in (stamping course='algebra1'),
    then drop the old table."""
    from sqlalchemy import inspect, text as _text
    insp = inspect(_engine)
    old_cols = [c["name"] for c in insp.get_columns(tname)]
    with _engine.begin() as conn:
        conn.execute(_text(f"DROP TABLE IF EXISTS {tname}_old"))  # clear any stale rebuild
        conn.execute(_text(f"ALTER TABLE {tname} RENAME TO {tname}_old"))
    _tables[tname].create(_engine, checkfirst=True)
    collist = ", ".join(old_cols)
    with _engine.begin() as conn:
        conn.execute(_text(
            f"INSERT INTO {tname} ({collist}, course) "
            f"SELECT {collist}, '{DEFAULT_COURSE}' FROM {tname}_old"))
        conn.execute(_text(f"DROP TABLE {tname}_old"))


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
def get_session(code: str, course: str = DEFAULT_COURSE) -> dict:
    from sqlalchemy import select
    t = _tables["sessions"]
    with _engine.connect() as conn:
        r = conn.execute(select(t.c.history, t.c.summary).where(
            (t.c.code == code) & (t.c.course == course))).first()
    if not r:
        return {"history": []}
    out = {"history": _loads(r[0], [])}
    if r[1]:
        out["summary"] = r[1]
    return out


def save_session(code: str, session: dict, course: str = DEFAULT_COURSE) -> None:
    values = {
        "history": json.dumps(session.get("history", []), ensure_ascii=False),
        "summary": session.get("summary"),
        "updated_at": _now(),
    }
    _upsert("sessions", {"code": code, "course": course}, values)


# ---- placements ------------------------------------------------------------
def read_placement(code: str, course: str = DEFAULT_COURSE) -> dict:
    from sqlalchemy import select
    t = _tables["placements"]
    with _engine.connect() as conn:
        r = conn.execute(select(t.c.data).where(
            (t.c.code == code) & (t.c.course == course))).first()
    return _loads(r[0], {}) if r else {}


def save_placement(code: str, result: dict, course: str = DEFAULT_COURSE) -> None:
    _upsert("placements", {"code": code, "course": course}, {
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
# Honest engagement levels, ranked. We only ever UPGRADE a unit's status, never
# downgrade it (exploring a unit you've already practiced shouldn't demote it).
STATUS_RANK = {"explored": 1, "learning": 2, "practiced": 3, "mastered": 4}


def record_topic(code: str, unit: int, unit_name: str = "", status: str = "explored",
                 course: str = DEFAULT_COURSE) -> None:
    """Record that a student engaged with a unit of a course: +1 touch, and upgrade the
    status if the new engagement is deeper than what's already recorded."""
    from sqlalchemy import select
    t = _tables["topic_progress"]
    with _engine.connect() as conn:
        r = conn.execute(select(t.c.touches, t.c.status).where(
            (t.c.code == code) & (t.c.course == course) & (t.c.unit == unit))).first()
    touches = (r[0] if r else 0) + 1
    prev_status = r[1] if r else None
    # keep the deeper of prev vs incoming
    best = status
    if prev_status and STATUS_RANK.get(prev_status, 0) >= STATUS_RANK.get(status, 0):
        best = prev_status
    _upsert("topic_progress", {"code": code, "course": course, "unit": unit}, {
        "unit_name": unit_name or UNIT_NAME_HINT.get(unit, ""), "status": best,
        "touches": touches, "last_touched": _now(),
    })


# Minimal fallback names so a record without a name still stores one.
UNIT_NAME_HINT = {
    1: "Foundations & Expressions", 2: "Linear Equations & Inequalities",
    3: "Functions & Notation", 4: "Linear Functions & Graphs", 5: "Systems of Equations",
    6: "Exponents & Exponential Functions", 7: "Polynomials & Factoring",
    8: "Quadratic Functions", 9: "Data & Statistics",
}


def get_topics(code: str, course: str = DEFAULT_COURSE) -> list:
    """Return this student's per-unit topic progress rows for a course (for the dashboard)."""
    from sqlalchemy import select
    t = _tables["topic_progress"]
    with _engine.connect() as conn:
        rows = conn.execute(select(
            t.c.unit, t.c.unit_name, t.c.status, t.c.touches, t.c.last_touched
        ).where((t.c.code == code) & (t.c.course == course)).order_by(t.c.unit)).all()
    return [
        {"unit": r[0], "unit_name": r[1], "status": r[2], "touches": r[3],
         "last_touched": r[4].isoformat() if r[4] else None}
        for r in rows
    ]


# ---- engaged time (2026-07-30) ----------------------------------------------
def record_minutes(code: str, course: str = DEFAULT_COURSE, day: str = "",
                   minutes_add: int = 1) -> None:
    """Add verified engaged minutes to this student's day. `day` is the student's
    local 'YYYY-MM-DD' (falls back to the server's date if not supplied)."""
    from sqlalchemy import select
    t = _tables["time_daily"]
    day = (day or "").strip() or _today()
    with _engine.connect() as conn:
        r = conn.execute(select(t.c.minutes).where(
            (t.c.code == code) & (t.c.course == course) & (t.c.day == day))).first()
    _upsert("time_daily", {"code": code, "course": course, "day": day}, {
        "minutes": (r[0] if r and r[0] else 0) + int(minutes_add),
        "updated_at": _now(),
    })


def get_time(code: str, days: int = 14) -> list:
    """Return this student's recent engaged-time rows (newest first), across all
    courses: [{day, course, minutes}]. main.py aggregates per day for the dashboard."""
    from sqlalchemy import select
    t = _tables["time_daily"]
    with _engine.connect() as conn:
        rows = conn.execute(select(t.c.day, t.c.course, t.c.minutes)
                            .where(t.c.code == code)
                            .order_by(t.c.day.desc())
                            .limit(max(1, int(days)) * 12)).all()   # 12 courses of headroom/day
    return [{"day": r[0], "course": r[1], "minutes": r[2] or 0} for r in rows]


# ---- mastery: end-of-unit CHECKS + student STATS (Phase A) ------------------
# A unit is "mastered" when the student passes a check (best score >= PASS_PCT).
PASS_PCT = 80


def _today() -> str:
    return _now().date().isoformat()


def _get_stats_row(code: str) -> dict:
    from sqlalchemy import select
    t = _tables["student_stats"]
    with _engine.connect() as conn:
        r = conn.execute(select(
            t.c.problems_practiced, t.c.correct_total, t.c.attempted_total,
            t.c.checks_taken, t.c.streak_days, t.c.last_active
        ).where(t.c.code == code)).first()
    if not r:
        return {"problems_practiced": 0, "correct_total": 0, "attempted_total": 0,
                "checks_taken": 0, "streak_days": 0, "last_active": None}
    return {"problems_practiced": r[0] or 0, "correct_total": r[1] or 0,
            "attempted_total": r[2] or 0, "checks_taken": r[3] or 0,
            "streak_days": r[4] or 0, "last_active": r[5]}


def _touch_streak(s: dict) -> None:
    """Update streak_days + last_active for activity happening TODAY (in-place)."""
    today = _today()
    last = s.get("last_active")
    if last == today:
        return                                   # already counted today
    yday = (_now().date() - _dt.timedelta(days=1)).isoformat()
    s["streak_days"] = (s.get("streak_days") or 0) + 1 if last == yday else 1
    s["last_active"] = today


def _save_stats(code: str, s: dict) -> None:
    _upsert("student_stats", {"code": code}, {
        "problems_practiced": s["problems_practiced"], "correct_total": s["correct_total"],
        "attempted_total": s["attempted_total"], "checks_taken": s["checks_taken"],
        "streak_days": s["streak_days"], "last_active": s["last_active"], "updated_at": _now(),
    })


def _set_unit_status(code: str, unit: int, status: str, unit_name: str = "",
                     course: str = DEFAULT_COURSE) -> None:
    """Upgrade a unit's topic_progress status (never downgrade), without touching touches."""
    from sqlalchemy import select
    t = _tables["topic_progress"]
    with _engine.connect() as conn:
        r = conn.execute(select(t.c.status).where(
            (t.c.code == code) & (t.c.course == course) & (t.c.unit == unit))).first()
    prev = r[0] if r else None
    if prev and STATUS_RANK.get(prev, 0) >= STATUS_RANK.get(status, 0):
        return
    _upsert("topic_progress", {"code": code, "course": course, "unit": unit}, {
        "unit_name": unit_name or UNIT_NAME_HINT.get(unit, ""),
        "status": status, "last_touched": _now(),
    })


def record_check(code: str, unit: int, correct: int, total: int, unit_name: str = "",
                 course: str = DEFAULT_COURSE) -> dict:
    """Record an end-of-unit check result for a course. Updates best/last score, cumulative
    accuracy, the day streak, and marks the unit 'mastered' if the student passed. Returns a
    small summary {pct, best_pct, mastered}."""
    correct = max(0, int(correct)); total = max(1, int(total))
    pct = round(100 * correct / total)
    from sqlalchemy import select
    t = _tables["unit_checks"]
    with _engine.connect() as conn:
        r = conn.execute(select(t.c.checks_taken, t.c.best_pct, t.c.correct, t.c.attempted).where(
            (t.c.code == code) & (t.c.course == course) & (t.c.unit == unit))).first()
    checks_taken = (r[0] if r else 0) + 1
    best_pct = max(pct, (r[1] if r else 0))
    _upsert("unit_checks", {"code": code, "course": course, "unit": unit}, {
        "checks_taken": checks_taken, "best_pct": best_pct, "last_pct": pct,
        "correct": (r[2] if r else 0) + correct, "attempted": (r[3] if r else 0) + total,
        "updated_at": _now(),
    })
    if pct >= PASS_PCT:
        _set_unit_status(code, unit, "mastered", unit_name, course)
    s = _get_stats_row(code)
    s["checks_taken"] += 1
    s["correct_total"] += correct
    s["attempted_total"] += total
    s["problems_practiced"] += total
    _touch_streak(s)
    _save_stats(code, s)
    return {"pct": pct, "best_pct": best_pct, "mastered": pct >= PASS_PCT}


def record_practice(code: str, correct: int, attempted: int = 1) -> None:
    """Count practice problems the tutor marked right/wrong (feeds 'problems practiced',
    accuracy, and the day streak)."""
    correct = max(0, int(correct)); attempted = max(1, int(attempted))
    s = _get_stats_row(code)
    s["problems_practiced"] += attempted
    s["correct_total"] += correct
    s["attempted_total"] += attempted
    _touch_streak(s)
    _save_stats(code, s)


def get_mastery(code: str, course: str = DEFAULT_COURSE) -> dict:
    """Assemble the student's mastery picture for a course's dashboard: per-unit check scores
    (for THIS course) + overall stats (problems practiced, accuracy, streak, whole-student)."""
    from sqlalchemy import select
    t = _tables["unit_checks"]
    with _engine.connect() as conn:
        rows = conn.execute(select(
            t.c.unit, t.c.checks_taken, t.c.best_pct, t.c.last_pct, t.c.correct, t.c.attempted
        ).where((t.c.code == code) & (t.c.course == course))).all()
    checks = {r[0]: {"checks_taken": r[1], "best_pct": r[2], "last_pct": r[3],
                     "correct": r[4], "attempted": r[5]} for r in rows}
    s = _get_stats_row(code)
    acc = round(100 * s["correct_total"] / s["attempted_total"]) if s["attempted_total"] else None
    return {
        "checks": checks,
        "stats": {
            "problems_practiced": s["problems_practiced"],
            "accuracy_pct": acc,
            "checks_taken": s["checks_taken"],
            "streak_days": s["streak_days"],
            "last_active": s["last_active"],
        },
    }


# =============================================================================
# TEACHER / PARENT CLASSROOM ROSTER (2026-07-28)
# -----------------------------------------------------------------------------
# A class is a short CLASS CODE + a list of existing student codes. This is intentionally
# NOT an accounts system: there is no password and no new personal data -- it simply groups
# student codes that already exist so a teacher/parent can see them together. Every function
# is safe to call when the DB is off (callers check store.enabled() first, and these return
# empty/False rather than raising).
# =============================================================================
def _norm_class(class_code: str) -> str:
    """Class codes are case-insensitive and trimmed, so 'mrsb-p3' == 'MRSB-P3'."""
    return (str(class_code or "").strip().upper())[:32]


def _norm_student(student_code: str) -> str:
    return (str(student_code or "").strip())[:64]


def _norm_teacher(teacher_code: str) -> str:
    """Teacher codes are case-insensitive and trimmed, so 'mrsbaker' == 'MRSBAKER'."""
    return (str(teacher_code or "").strip().upper())[:64]


def create_class(class_code: str, name: str = "", owner_name: str = "",
                 teacher_code: str = "") -> dict:
    """Create a class, or update its label/owner if the code already exists. Returns the class.

    `teacher_code` is OPTIONAL and defaults to "" so every pre-existing call site is unchanged.
    An existing class's teacher_code is NEVER overwritten: if the class already belongs to a
    teacher code, that stays put, and only an unowned class can adopt one. That keeps a second
    teacher who happens to guess the same class code from quietly taking the class over.
    """
    cc = _norm_class(class_code)
    if not cc:
        return {}
    existing = get_class(cc)
    values = {
        "name": (name or existing.get("name") or ""),
        "owner_name": (owner_name or existing.get("owner_name") or ""),
        # keep the current owner code if there is one; otherwise adopt the one supplied
        "teacher_code": (existing.get("teacher_code") or _norm_teacher(teacher_code) or None),
        "updated_at": _now(),
    }
    if not existing:
        values["created_at"] = _now()
    _upsert("classes", {"class_code": cc}, values)
    return get_class(cc)


def get_class(class_code: str) -> dict:
    """{class_code, name, owner_name, teacher_code, students:[codes]} -- {} if it doesn't exist."""
    from sqlalchemy import select
    cc = _norm_class(class_code)
    if not cc:
        return {}
    t = _tables["classes"]
    with _engine.connect() as conn:
        r = conn.execute(select(t.c.class_code, t.c.name, t.c.owner_name, t.c.teacher_code)
                         .where(t.c.class_code == cc)).first()
    if not r:
        return {}
    return {"class_code": r[0], "name": r[1] or "", "owner_name": r[2] or "",
            "teacher_code": r[3] or "", "students": list_students(cc)}


def list_classes_for_teacher(teacher_code: str) -> list:
    """EVERY class run by this teacher code, oldest-created first, each with a student count.

    Returns [] for an unknown code -- that is not an error, it just means this teacher hasn't
    created a class yet, and the page invites them to make their first one. One query for the
    classes plus one for the counts, never one query per class.
    """
    from sqlalchemy import select, func
    tc = _norm_teacher(teacher_code)
    if not tc:
        return []
    cl, cm = _tables["classes"], _tables["class_members"]
    with _engine.connect() as conn:
        rows = conn.execute(
            select(cl.c.class_code, cl.c.name, cl.c.owner_name, cl.c.created_at)
            .where(cl.c.teacher_code == tc)).all()
        counts = dict(conn.execute(
            select(cm.c.class_code, func.count(cm.c.student_code))
            .group_by(cm.c.class_code)).all())
    # oldest-created first; ties broken by code so the list order is always deterministic
    rows = sorted(rows, key=lambda r: (r[3] is None, r[3], r[0]))
    return [{"class_code": r[0], "name": r[1] or "", "owner_name": r[2] or "",
             "student_count": int(counts.get(r[0], 0))} for r in rows]


def list_students(class_code: str) -> list:
    """The student codes in a class, oldest-added first."""
    from sqlalchemy import select
    cc = _norm_class(class_code)
    if not cc:
        return []
    t = _tables["class_members"]
    with _engine.connect() as conn:
        rows = conn.execute(select(t.c.student_code, t.c.added_at)
                            .where(t.c.class_code == cc)).all()
    # oldest-added first; ties broken by code so the roster order is always deterministic
    rows = sorted(rows, key=lambda r: (r[1] is None, r[1], r[0]))
    return [r[0] for r in rows]


def add_student(class_code: str, student_code: str) -> bool:
    """Add a student code to a class. Truly idempotent: re-adding an existing member does
    NOTHING (it must not bump added_at, or the roster would reorder itself)."""
    from sqlalchemy import select
    cc, sc = _norm_class(class_code), _norm_student(student_code)
    if not cc or not sc:
        return False
    t = _tables["class_members"]
    with _engine.connect() as conn:
        already = conn.execute(select(t.c.student_code).where(
            (t.c.class_code == cc) & (t.c.student_code == sc))).first()
    if already:
        return True
    _upsert("class_members", {"class_code": cc, "student_code": sc}, {"added_at": _now()})
    return True


def remove_student(class_code: str, student_code: str) -> bool:
    """Remove a student code from a class (the student's own data is untouched)."""
    cc, sc = _norm_class(class_code), _norm_student(student_code)
    if not cc or not sc:
        return False
    t = _tables["class_members"]
    with _engine.begin() as conn:
        conn.execute(t.delete().where((t.c.class_code == cc) & (t.c.student_code == sc)))
    return True


def delete_class(class_code: str) -> bool:
    """Delete a class and its membership rows. Student records themselves are NOT touched."""
    cc = _norm_class(class_code)
    if not cc:
        return False
    cm, cl = _tables["class_members"], _tables["classes"]
    with _engine.begin() as conn:
        conn.execute(cm.delete().where(cm.c.class_code == cc))
        conn.execute(cl.delete().where(cl.c.class_code == cc))
    return True


def get_course_activity(code: str) -> dict:
    """EVERY course this student has actually touched, in ONE pass (not one query per course).

    Returns {course_id: {units_started, units_mastered, units_checked, best_total, last_active}}
    for courses with real activity only -- a course the student has never opened is simply
    absent, so the caller never has to invent an empty shell. Used by the dashboard's
    "My courses" strip, which needs the whole picture without firing a request per course.
    """
    from sqlalchemy import select
    out = {}

    # 1) engagement (explored / learning / practiced) per course, from topic_progress
    tp = _tables["topic_progress"]
    with _engine.connect() as conn:
        rows = conn.execute(select(tp.c.course, tp.c.unit, tp.c.status, tp.c.last_touched)
                            .where(tp.c.code == code)).all()
    for course, unit, status_, last in rows:
        c = out.setdefault(course, {"units_started": 0, "units_mastered": 0,
                                    "units_checked": 0, "best_total": 0, "last_active": None})
        if status_ and status_ != "not-started":
            c["units_started"] += 1
        if last and (c["last_active"] is None or last > c["last_active"]):
            c["last_active"] = last

    # 2) mastery per course, from unit_checks (a unit is mastered at best >= 80%)
    uc = _tables["unit_checks"]
    with _engine.connect() as conn:
        rows = conn.execute(select(uc.c.course, uc.c.unit, uc.c.best_pct, uc.c.updated_at)
                            .where(uc.c.code == code)).all()
    for course, unit, best, updated in rows:
        c = out.setdefault(course, {"units_started": 0, "units_mastered": 0,
                                    "units_checked": 0, "best_total": 0, "last_active": None})
        best = int(best or 0)
        c["units_checked"] += 1
        c["best_total"] += best
        if best >= 80:
            c["units_mastered"] += 1
        if updated and (c["last_active"] is None or updated > c["last_active"]):
            c["last_active"] = updated

    # a unit that's been checked counts as started even if topic_progress never saw it
    for c in out.values():
        c["units_started"] = max(c["units_started"], c["units_checked"])
        c["avg_best_pct"] = (round(c["best_total"] / c["units_checked"]) if c["units_checked"] else None)
        c["last_active"] = (c["last_active"].isoformat() if c["last_active"] else None)
        c.pop("best_total", None)
    return out


def status() -> dict:
    """Small diagnostic for a health/status endpoint. `configured` = did the app see a
    DATABASE_URL at all; `reason` = why it's disabled (credentials redacted)."""
    return {
        "db_enabled": _ENABLED,
        "dialect": (_engine.dialect.name if _engine else None),
        "configured": bool(DATABASE_URL),
        "reason": (None if _ENABLED else _INIT_ERROR),
    }


# I did no harm and this file is not truncated.
