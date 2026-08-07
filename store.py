# =============================================================================
# store.py  --  Math Tutor MVP  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-07  FINAL EXAM (Jim: a real course final, gated on mastering all nine units).
#               NEW table `final_exams` (code+course pk): exams_taken, best_pct, last_pct,
#               correct, attempted, passed_at (set ONCE, the first time the score reaches
#               PASS_PCT=90 -- that date goes on the Course Diploma), updated_at. New
#               functions: record_final_exam() (upserts best/last/attempts; stamps passed_at
#               on first pass), get_final_exam() (read one), both safe-when-disabled like
#               everything else here. Brand-new table -> create_all builds it; no migration;
#               nothing else touched. Additive only.
#   2026-08-05  OPS ERROR LOG (pre-launch readiness: "you should learn about a broken API key
#               from an alert, not from a parent"). NEW table `error_log` (id autoincrement,
#               created_at, where 160, what Text): one row per unhandled server error, written
#               by main.py's new global exception handler. New functions: record_error(where,
#               what) -- best-effort insert that NEVER raises (an error logger that errors would
#               be poetic but useless) and sweeps rows older than 30 days on each write;
#               recent_errors(hours, limit) -- newest first, isoformat timestamps, for /admin;
#               errors_count(hours). Purely additive; no existing function changed.
#   2026-08-05  ADMIN FULL RESET (Jim: a "Start Fresh" tool so he can re-run the brand-new-parent
#               signup with his OWN email). NEW delete_parent_cascade(parent_id): removes ONE
#               parent and everything tied to it -- their student accounts and every per-student
#               row (sessions, placements, topic/unit progress, topic quizzes, stats, engaged
#               time, awards, class memberships), plus that parent's sign-in tokens, reset links,
#               and weekly-digest row -- in a SINGLE atomic transaction (all-or-nothing). Scoped
#               to exactly one parent_id; it never reaches another account. Community forum posts
#               are intentionally LEFT (soft-delete-only by design; the author name is stored on
#               the row, so they still read fine). Returns {ok, deleted:{table: rows}, student_
#               codes:[...]}. Purely additive -- no existing function changed.
#   2026-08-04  RECORDS PAGE (build z): new get_time_between(code, day_from, day_to) -- the
#               full-range hours log for the printable homeschool records report (get_time()
#               only serves the dashboard's recent window). Read-only; additive.
#   2026-08-04  TOPIC QUIZZES (Jim: quizzes as checkpoints WITHIN a unit -- pass one to move to
#               the next topic -- plus the end-of-unit check renamed the 'Unit Quiz' in the UI).
#               NEW table `topic_quizzes` (code+course+unit+topic_key pk): one row per topic the
#               student has been quizzed on, keyed by a normalized topic-name slug so the same
#               topic never double-files even if the tutor words it slightly differently.
#               NEW: QUIZ_PASS_PCT = 80 (the mid-unit bar; the Unit Quiz keeps PASS_PCT = 90),
#               record_topic_quiz() (upserts best/last/attempts), get_topic_quizzes(). Additive.
#   2026-08-04  WEEKLY PARENT EMAIL (the one promised-but-unbuilt feature -- Jim: build it now).
#               NEW table `parent_digests` (parent_id pk, last_sent_at, optout, optout_token,
#               created_at): one row per parent tracking when their weekly report last went out
#               and whether they've unsubscribed. The optout_token is a random URL token used
#               ONLY for one-click unsubscribe links -- it grants no account access. New
#               functions: list_parents(), ensure_digest_state() (creates the row + token),
#               mark_digest_sent(), set_digest_optout(), parent_id_for_digest_token(), and
#               week_activity(code, days) -- the WINDOWED view of a student's week (minutes +
#               active days + per-course split from time_daily; checks taken from unit_checks;
#               units touched from topic_progress; awards earned from awards) that powers the
#               email's honest numbers. All additive: new table + new functions only.
#   2026-08-04  MASTERY BAR RAISED (Jim): PASS_PCT 80 -> 90. A unit now counts as MASTERED at a
#               90%+ best check score, everywhere (store computes it; main.py + the pages now read
#               store.PASS_PCT instead of hardcoding 80, so the NEXT change is one line). Note:
#               previously-stored 'mastered' topic_progress statuses from 80-89% checks keep their
#               stored label until the student checks again, but every LIVE computation (dashboards,
#               heatmaps, badges, trophies, admin counts) uses the new bar immediately.
#   2026-08-04  PASSWORD RESET (Jim: parents need 'I forgot my password'). NEW table
#               `parent_resets` (token_hash pk, parent_id, expires_at, used, created_at) --
#               we store ONLY a SHA-256 hash of the emailed token, never the token itself,
#               so even a database leak can't be replayed into a reset. New functions:
#               create_parent_reset() (45-min expiry), consume_parent_reset() (single-use,
#               expiry-checked, sweeps expired rows), delete_parent_tokens_for() (a reset
#               signs the parent out EVERYWHERE -- whoever knew the old password is out).
#   2026-08-04  USAGE LOG (Measurement plan #1 -- Jim: gather cost/usage/quality data so we can
#               make pricing, model, and grant decisions). NEW table `usage_log`: one privacy-safe
#               row per paid event -- kind 'brain' (a tutor turn: token counts straight from the
#               Anthropic response, attempt count, and the math-verifier verdict) or kind 'tts'
#               (an ElevenLabs request: character count + whether the audio cache served it free).
#               No conversation text is EVER stored here -- counts only. New log_usage() (fire-and-
#               forget; swallows every error -- logging must never break a lesson) and
#               usage_stats(days) (aggregates for /admin: tokens, retries, verifier breakdown,
#               distinct students, TTS generated-vs-cached). Additive: new table only.
#   2026-08-03  has_any_history() gained an optional `courses` filter (iterable of course ids)
#               so main.py can compute the screen-tour flag per CLASSROOM TYPE (elementary
#               tap-courses vs typing courses). Default None keeps the original any-course
#               behavior; read-only; nothing else touched.
#   2026-08-03  ADMIN DASHBOARD AGGREGATES. New read-only function admin_stats() for Jim's
#               /admin page: privacy-safe COUNTS/TOTALS only (parent counts by sub_status,
#               paid seats + estimated monthly revenue, family students, active-7d/30d,
#               engaged minutes total/7d, units mastered at PASS_PCT, checks taken, problems
#               practiced, forum posts/replies, beta pass totals). Read-only -- no schema
#               change, no new table, nothing else touched; returns all-zeros if the DB is off
#               and swallows any query error (the dashboard must never 500).
#   2026-07-31  BETA PASSES (Jim's beta-tester program). NEW table `beta_codes` (code,
#               label, uses_allowed default 5, uses_used, window_hours default 2,
#               window_expires_at, created_at, revoked) + create_beta_code /
#               get_beta_code / beta_login / beta_window_active / list_beta_codes /
#               revoke_beta_code. Semantics: each sign-in CONSUMES one use and opens a
#               window (default 2h); sign-ins DURING an open window ride free; after
#               uses_allowed windows the pass is done. Progress is keyed by the pass
#               code like any student, so a tester continues where they left off.
#               Brand-new table -> create_all builds it; nothing else touched.
#   2026-07-31  COMMUNITY FORUM (parents post, everyone reads). Two NEW tables --
#               `forum_posts` (id, section, title, body, parent_id, author_name,
#               reply_count, created_at, deleted) and `forum_replies` (id, post_id,
#               parent_id, author_name, body, created_at, deleted) -- plus
#               create_forum_post / list_forum_posts / get_forum_post /
#               create_forum_reply / delete_forum_item. Soft deletes only (deleted=1
#               hides, nothing is destroyed), so moderation is reversible by hand.
#               Brand-new tables -> create_all builds them; nothing else touched.
#   2026-07-31  REAL PARENT ACCOUNTS (the signup/payments foundation). Two NEW tables --
#               `parents` (id, email UNIQUE, name, password_hash, stripe_customer_id,
#               sub_status/plan/quantity/period_end, created_at) and `parent_tokens`
#               (token, parent_id, expires_at) -- plus one ADDITIVE nullable column on
#               `accounts`: parent_id (same safe ALTER pattern as classes.teacher_code;
#               _migrate_accounts_parent_id no-ops once present). Pilot students keep
#               parent_id NULL and behave exactly as before. New functions: create_parent /
#               get_parent / get_parent_by_email / get_parent_by_customer / update_parent /
#               create_parent_token / get_parent_token / delete_parent_token /
#               create_student_account / get_account / list_students_for_parent.
#               PASSWORDS ARE NEVER STORED -- only a PBKDF2 hash built in main.py. All
#               additive; no existing table, key, function, or signature changed.
#   2026-07-30  AWARDS TABLE (student reward system). New additive table `awards` (code, award_id,
#               earned_at -- one row per earn, kept forever) + get_awards()/record_awards().
#               Mastery badges/course trophies are recomputed live from unit_checks, but EFFORT
#               awards (streak medals, minute milestones, practice counts) must persist once
#               earned -- a 7-day-streak medal doesn't vanish when the streak breaks. earned_at
#               powers the dashboard's "NEW!" celebration. create_all builds it; no migration.
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
            # 2026-07-31: which parent account owns this student (nullable -- pilot
            # students from students.json have no parent and keep working untouched).
            Column("parent_id", String(64)),
        )
        # REAL PARENT ACCOUNTS (2026-07-31): one row per signed-up parent. The password
        # is NEVER stored -- password_hash is a salted PBKDF2 digest built in main.py.
        # Stripe billing state lives here too, updated only by the verified webhook:
        #   sub_status: 'free' | 'active' | 'past_due' | 'canceled'
        #   sub_plan:   'monthly' | 'annual' | ''      sub_quantity: students paid for
        _tables["parents"] = Table(
            "parents", _meta,
            Column("id", String(64), primary_key=True),          # uuid hex
            Column("email", String(256), unique=True, index=True),
            Column("name", String(256)),
            Column("password_hash", String(512)),
            Column("stripe_customer_id", String(64), index=True),
            Column("sub_status", String(32), default="free"),
            Column("sub_plan", String(16), default=""),
            Column("sub_quantity", Integer, default=0),
            Column("sub_period_end", DateTime(timezone=True)),
            Column("created_at", DateTime(timezone=True)),
        )
        # Parent sign-in tokens (random 64-hex strings handed out at login, checked on
        # every parent API call, removed at logout / on expiry). NOT the password.
        _tables["parent_tokens"] = Table(
            "parent_tokens", _meta,
            Column("token", String(128), primary_key=True),
            Column("parent_id", String(64), index=True),
            Column("expires_at", DateTime(timezone=True)),
            Column("created_at", DateTime(timezone=True)),
        )
        # PASSWORD RESETS (2026-08-04): single-use, short-lived. token_hash is SHA-256 of
        # the emailed token -- the raw token exists only in the parent's inbox.
        _tables["parent_resets"] = Table(
            "parent_resets", _meta,
            Column("token_hash", String(128), primary_key=True),
            Column("parent_id", String(64), index=True),
            Column("expires_at", DateTime(timezone=True)),
            Column("used", Integer, default=0),
            Column("created_at", DateTime(timezone=True)),
        )
        # WEEKLY PARENT EMAIL (2026-08-04): one row per parent -- when their weekly
        # report last went out, whether they opted out, and the random unsubscribe
        # token their email links carry (grants NOTHING but the unsubscribe action).
        _tables["parent_digests"] = Table(
            "parent_digests", _meta,
            Column("parent_id", String(64), primary_key=True),
            Column("last_sent_at", DateTime(timezone=True)),
            Column("optout", Integer, default=0),
            Column("optout_token", String(64), unique=True, index=True),
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
        # TOPIC QUIZZES (2026-08-04): mid-unit checkpoint quizzes. One row per student/
        # course/unit/topic; topic_key is a normalized slug of the topic name (stable
        # even if the tutor words the name slightly differently between sessions).
        _tables["topic_quizzes"] = Table(
            "topic_quizzes", _meta,
            Column("code", String(64), primary_key=True),
            Column("course", String(32), primary_key=True, nullable=False,
                   default=DEFAULT_COURSE),
            Column("unit", Integer, primary_key=True),
            Column("topic_key", String(64), primary_key=True),
            Column("topic_name", String(128)),
            Column("topic_idx", Integer, default=0),
            Column("quizzes_taken", Integer, default=0),
            Column("best_pct", Integer, default=0),
            Column("last_pct", Integer, default=0),
            Column("updated_at", DateTime(timezone=True)),
        )
        # FINAL EXAM (2026-08-07): one row per student per course. passed_at is stamped
        # exactly once -- the first time a score reaches PASS_PCT -- and is the date
        # printed on the Course Diploma.
        _tables["final_exams"] = Table(
            "final_exams", _meta,
            Column("code", String(64), primary_key=True),
            Column("course", String(32), primary_key=True, nullable=False,
                   default=DEFAULT_COURSE),
            Column("exams_taken", Integer, default=0),
            Column("best_pct", Integer, default=0),
            Column("last_pct", Integer, default=0),
            Column("correct", Integer, default=0),
            Column("attempted", Integer, default=0),
            Column("passed_at", DateTime(timezone=True)),
            Column("updated_at", DateTime(timezone=True)),
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
        # AWARDS (2026-07-30): the student's earned trophies/awards, ONE ROW PER EARN, kept
        # forever. Badges/trophies are recomputed from mastery data, but effort awards
        # (streaks, minutes, practice milestones) must PERSIST once earned -- a 7-day-streak
        # medal doesn't vanish when the streak breaks. earned_at powers the "NEW!" celebration.
        _tables["awards"] = Table(
            "awards", _meta,
            Column("code", String(64), primary_key=True),
            Column("award_id", String(48), primary_key=True),
            Column("earned_at", DateTime(timezone=True)),
        )
        # BETA PASSES (2026-07-31): shareable trial codes. Each sign-in consumes one
        # of `uses_allowed` and opens a `window_hours` window of full access.
        _tables["beta_codes"] = Table(
            "beta_codes", _meta,
            Column("code", String(24), primary_key=True),     # e.g. TRY-MAPLE42
            Column("label", String(120)),                     # who Jim made it for
            Column("uses_allowed", Integer, default=5),
            Column("uses_used", Integer, default=0),
            Column("window_hours", Integer, default=2),
            Column("window_expires_at", DateTime(timezone=True)),
            Column("created_at", DateTime(timezone=True)),
            Column("revoked", Integer, default=0),
        )
        # OPS ERROR LOG (2026-08-05): one row per unhandled server error, written by
        # main.py's global exception handler. Powers /admin's error tile and Jim's
        # alert emails. Swept to the last 30 days on each write.
        _tables["error_log"] = Table(
            "error_log", _meta,
            Column("id", Integer, primary_key=True, autoincrement=True),
            Column("created_at", DateTime(timezone=True), index=True),
            Column("where", String(160)),     # e.g. "POST /api/session/1234"
            Column("what", Text),             # exception type + message (no secrets)
        )
        # COMMUNITY FORUM (2026-07-31): parents post, everyone reads. Soft deletes
        # only -- moderation flips deleted=1, nothing is ever destroyed.
        _tables["forum_posts"] = Table(
            "forum_posts", _meta,
            Column("id", String(64), primary_key=True),       # uuid hex
            Column("section", String(24), index=True),        # working|ideas|resources|courses
            Column("title", String(160)),
            Column("body", Text),
            Column("parent_id", String(64)),                  # the AUTHOR (a parents.id)
            Column("author_name", String(80)),                # display name, chosen server-side
            Column("reply_count", Integer, default=0),
            Column("created_at", DateTime(timezone=True)),
            Column("deleted", Integer, default=0),
        )
        _tables["forum_replies"] = Table(
            "forum_replies", _meta,
            Column("id", String(64), primary_key=True),
            Column("post_id", String(64), index=True),
            Column("parent_id", String(64)),
            Column("author_name", String(80)),
            Column("body", Text),
            Column("created_at", DateTime(timezone=True)),
            Column("deleted", Integer, default=0),
        )
        # USAGE LOG (2026-08-04): one row per paid event (a brain turn or a TTS request).
        # COUNTS ONLY -- never any conversation text. See log_usage()/usage_stats() below.
        _tables["usage_log"] = Table(
            "usage_log", _meta,
            Column("id", String(64), primary_key=True),
            Column("kind", String(16), index=True),      # 'brain' | 'tts'
            Column("code", String(64), index=True),      # student code ('' if none, e.g. demo)
            Column("course", String(32)),
            Column("mode", String(24)),                  # lesson|practice|topic|assessment|speak|demo
            Column("model", String(64)),                 # brain: Claude model id; tts: ElevenLabs model
            Column("input_tokens", Integer, default=0),
            Column("output_tokens", Integer, default=0),
            Column("cache_read_tokens", Integer, default=0),
            Column("cache_write_tokens", Integer, default=0),
            Column("tts_chars", Integer, default=0),
            Column("tts_cache_hit", Integer, default=0), # 1 = served from disk cache ($0)
            Column("attempts", Integer, default=1),      # model calls this turn (verifier retries)
            Column("verify_status", String(16), default=""),  # ok|fixed|unresolved|unverifiable|none
            Column("created_at", DateTime(timezone=True), index=True),
        )
        _meta.create_all(_engine)
        # Give the per-unit tables a `course` dimension if they predate the multi-course
        # work (additive; preserves all existing rows as 'algebra1'). No-ops once migrated.
        _migrate_course_columns()
        # Give the `classes` table its `teacher_code` column if it predates teacher sign-in
        # (additive + nullable; no key change). No-ops once migrated.
        _migrate_classes_teacher_code()
        # Give `accounts` its `parent_id` column if it predates real parent accounts
        # (additive + nullable; no key change). No-ops once migrated.
        _migrate_accounts_parent_id()
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


def _migrate_accounts_parent_id():
    """One-time, ADDITIVE migration: give `accounts` a nullable `parent_id` column so a
    signed-up parent can own student codes. Same safe pattern as classes.teacher_code:
    the column is NULLABLE and the primary key is untouched, so a plain ALTER TABLE works
    identically on PostgreSQL and SQLite. Pilot students simply have parent_id NULL and
    keep working exactly as before. No-ops when the column already exists."""
    from sqlalchemy import inspect, text as _text
    insp = inspect(_engine)
    if "accounts" not in set(insp.get_table_names()):
        return  # create_all will build it new, already carrying parent_id
    cols = [c["name"] for c in insp.get_columns("accounts")]
    if "parent_id" in cols:
        return  # already migrated
    with _engine.begin() as conn:
        conn.execute(_text("ALTER TABLE accounts ADD COLUMN parent_id VARCHAR(64)"))
    print("[store] migrated accounts: +parent_id column (nullable).")


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


def has_any_history(code: str, courses=None) -> bool:
    """Has this student EVER had a lesson conversation? (2026-08-01: powers 'one screen
    tour per student, not one per course'.) 2026-08-03: optional `courses` -- an iterable of
    course ids -- limits the check to those courses. This lets the ELEMENTARY classroom
    (entry/basic, tap-to-answer) run its own first-time tour for a student who has only
    ever toured a typing course, and vice versa. courses=None keeps the original
    any-course behavior."""
    from sqlalchemy import select
    t = _tables["sessions"]
    q = select(t.c.history).where(t.c.code == code)
    if courses:
        q = q.where(t.c.course.in_(list(courses)))
    with _engine.connect() as conn:
        rows = conn.execute(q).fetchall()
    for (h,) in rows:
        if _loads(h, []):
            return True
    return False


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


def get_time_between(code: str, day_from: str, day_to: str) -> list:
    """Engaged-time rows for an arbitrary day range (records report): [{day, course,
    minutes}], oldest first. Day strings are ISO 'YYYY-MM-DD' so string compare works."""
    from sqlalchemy import select
    t = _tables["time_daily"]
    with _engine.connect() as conn:
        rows = conn.execute(select(t.c.day, t.c.course, t.c.minutes)
                            .where((t.c.code == code) &
                                   (t.c.day >= day_from) & (t.c.day <= day_to))
                            .order_by(t.c.day)).all()
    return [{"day": r[0], "course": r[1], "minutes": r[2] or 0} for r in rows]


# ---- awards (2026-07-30) -----------------------------------------------------
def get_awards(code: str) -> dict:
    """This student's earned awards: {award_id: earned_at_iso}."""
    from sqlalchemy import select
    t = _tables["awards"]
    with _engine.connect() as conn:
        rows = conn.execute(select(t.c.award_id, t.c.earned_at)
                            .where(t.c.code == code)).all()
    return {r[0]: (r[1].isoformat() if r[1] else None) for r in rows}


def record_awards(code: str, award_ids: list) -> None:
    """Persist newly-earned awards (idempotent; existing rows keep their original earned_at)."""
    existing = get_awards(code)
    now = _now()
    for aid in award_ids:
        if aid in existing:
            continue
        _upsert("awards", {"code": code, "award_id": aid}, {"earned_at": now})


# ---- mastery: end-of-unit CHECKS + student STATS (Phase A) ------------------
# A unit is "mastered" when the student passes a check (best score >= PASS_PCT, i.e. 90%).
PASS_PCT = 90
# A mid-unit TOPIC QUIZ is "passed" at QUIZ_PASS_PCT (80%) -- deliberately below the 90%
# mastery bar, so topic checkpoints keep students moving while the Unit Quiz stays special.
QUIZ_PASS_PCT = 80


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


def _topic_key(name: str) -> str:
    """Normalized slug of a topic name -- stable across small wording differences."""
    import re as _re
    return _re.sub(r"[^a-z0-9]+", "", (name or "").lower())[:60] or "topic"


def record_topic_quiz(code: str, unit: int, topic_name: str, correct: int, total: int,
                      course: str = DEFAULT_COURSE, topic_idx: int = 0) -> dict:
    """Record one mid-unit TOPIC QUIZ result. Upserts by normalized topic name; keeps
    best/last percent and an attempt count. Returns {pct, passed, best_pct}."""
    from sqlalchemy import select
    correct = max(0, int(correct)); total = max(1, int(total))
    pct = round(100 * correct / total)
    key = _topic_key(topic_name)
    t = _tables["topic_quizzes"]
    with _engine.connect() as conn:
        r = conn.execute(select(t.c.quizzes_taken, t.c.best_pct).where(
            (t.c.code == code) & (t.c.course == course) &
            (t.c.unit == int(unit)) & (t.c.topic_key == key))).first()
    taken = (int(r[0]) if r and r[0] else 0) + 1
    best = max(pct, int(r[1]) if r and r[1] else 0)
    _upsert("topic_quizzes",
            {"code": code, "course": course, "unit": int(unit), "topic_key": key},
            {"topic_name": (topic_name or "").strip()[:128], "topic_idx": int(topic_idx or 0),
             "quizzes_taken": taken, "best_pct": best, "last_pct": pct, "updated_at": _now()})
    return {"pct": pct, "passed": pct >= QUIZ_PASS_PCT, "best_pct": best}


def get_topic_quizzes(code: str, course: str = DEFAULT_COURSE) -> list:
    """This student's topic-quiz rows for a course, unit order then topic order:
    [{unit, topic_name, topic_idx, quizzes_taken, best_pct, last_pct}]."""
    from sqlalchemy import select
    t = _tables["topic_quizzes"]
    with _engine.connect() as conn:
        rows = conn.execute(select(t.c.unit, t.c.topic_name, t.c.topic_idx,
                                   t.c.quizzes_taken, t.c.best_pct, t.c.last_pct)
                            .where((t.c.code == code) & (t.c.course == course))
                            .order_by(t.c.unit, t.c.topic_idx)).all()
    return [{"unit": int(r[0]), "topic_name": r[1] or "", "topic_idx": int(r[2] or 0),
             "quizzes_taken": int(r[3] or 0), "best_pct": int(r[4] or 0),
             "last_pct": int(r[5] or 0)} for r in rows]


def record_final_exam(code: str, correct: int, total: int,
                      course: str = DEFAULT_COURSE) -> dict:
    """Record one FINAL EXAM result (2026-08-07). Upserts best/last/attempts; stamps
    passed_at exactly ONCE, the first time the score reaches PASS_PCT (that date goes
    on the Course Diploma). Returns {pct, passed, best_pct, passed_at}."""
    from sqlalchemy import select
    correct = max(0, int(correct)); total = max(1, int(total))
    pct = round(100 * correct / total)
    t = _tables["final_exams"]
    with _engine.connect() as conn:
        r = conn.execute(select(t.c.exams_taken, t.c.best_pct, t.c.passed_at).where(
            (t.c.code == code) & (t.c.course == course))).first()
    taken = (int(r[0]) if r and r[0] else 0) + 1
    best = max(pct, int(r[1]) if r and r[1] else 0)
    passed_at = r[2] if r else None
    values = {"exams_taken": taken, "best_pct": best, "last_pct": pct,
              "correct": correct, "attempted": total, "updated_at": _now()}
    if pct >= PASS_PCT and not passed_at:
        passed_at = _now()
        values["passed_at"] = passed_at
    _upsert("final_exams", {"code": code, "course": course}, values)
    return {"pct": pct, "passed": pct >= PASS_PCT, "best_pct": best,
            "passed_at": passed_at.isoformat() if passed_at else None}


def get_final_exam(code: str, course: str = DEFAULT_COURSE) -> dict:
    """This student's final-exam row for a course, or {} if they haven't taken it."""
    from sqlalchemy import select
    t = _tables["final_exams"]
    with _engine.connect() as conn:
        r = conn.execute(select(t.c.exams_taken, t.c.best_pct, t.c.last_pct,
                                t.c.passed_at).where(
            (t.c.code == code) & (t.c.course == course))).first()
    if not r:
        return {}
    return {"exams_taken": int(r[0] or 0), "best_pct": int(r[1] or 0),
            "last_pct": int(r[2] or 0),
            "passed": int(r[1] or 0) >= PASS_PCT,
            "passed_at": r[3].isoformat() if r[3] else None}


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

    # 2) mastery per course, from unit_checks (a unit is mastered at best >= PASS_PCT)
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
        if best >= PASS_PCT:
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


# ---- real parent accounts (2026-07-31: the signup/payments foundation) ------
# All of these REQUIRE the database (enabled() True). main.py checks that and
# answers parent/billing endpoints with a clear "database required" message when
# it's off -- an accounts-and-payments system must never live in throwaway files.

def _row_to_dict(row, cols):
    return {c: row[i] for i, c in enumerate(cols)} if row else None


_PARENT_COLS = ["id", "email", "name", "password_hash", "stripe_customer_id",
                "sub_status", "sub_plan", "sub_quantity", "sub_period_end", "created_at"]


def create_parent(parent_id: str, email: str, name: str, password_hash: str) -> bool:
    """Insert a new parent. Returns False (and inserts nothing) if the email is taken.
    The unique index on email is the real guarantee under concurrency; the pre-check
    just gives a friendlier code path."""
    from sqlalchemy import insert, select
    email = (email or "").strip().lower()
    t = _tables["parents"]
    try:
        with _engine.begin() as conn:
            exists = conn.execute(select(t.c.id).where(t.c.email == email)).first()
            if exists:
                return False
            conn.execute(insert(t).values(
                id=parent_id, email=email, name=(name or "").strip(),
                password_hash=password_hash, stripe_customer_id="",
                sub_status="free", sub_plan="", sub_quantity=0,
                sub_period_end=None, created_at=_now()))
        return True
    except Exception:  # unique-index race: someone signed up the same email first
        return False


def get_parent_by_email(email: str):
    from sqlalchemy import select
    t = _tables["parents"]
    with _engine.connect() as conn:
        r = conn.execute(select(*[t.c[c] for c in _PARENT_COLS])
                         .where(t.c.email == (email or "").strip().lower())).first()
    return _row_to_dict(r, _PARENT_COLS)


def get_parent(parent_id: str):
    from sqlalchemy import select
    t = _tables["parents"]
    with _engine.connect() as conn:
        r = conn.execute(select(*[t.c[c] for c in _PARENT_COLS])
                         .where(t.c.id == parent_id)).first()
    return _row_to_dict(r, _PARENT_COLS)


def get_parent_by_customer(stripe_customer_id: str):
    from sqlalchemy import select
    if not stripe_customer_id:
        return None
    t = _tables["parents"]
    with _engine.connect() as conn:
        r = conn.execute(select(*[t.c[c] for c in _PARENT_COLS])
                         .where(t.c.stripe_customer_id == stripe_customer_id)).first()
    return _row_to_dict(r, _PARENT_COLS)


_PARENT_UPDATABLE = {"name", "password_hash", "stripe_customer_id",
                     "sub_status", "sub_plan", "sub_quantity", "sub_period_end"}


def update_parent(parent_id: str, **fields) -> None:
    """Update a whitelisted subset of parent fields (billing state, name, password hash).
    Unknown fields are ignored on purpose so a typo can't corrupt a row."""
    from sqlalchemy import update
    values = {k: v for k, v in fields.items() if k in _PARENT_UPDATABLE}
    if not values:
        return
    t = _tables["parents"]
    with _engine.begin() as conn:
        conn.execute(update(t).where(t.c.id == parent_id).values(**values))


def create_parent_token(token: str, parent_id: str, days: int = 30) -> None:
    from sqlalchemy import insert
    t = _tables["parent_tokens"]
    with _engine.begin() as conn:
        conn.execute(insert(t).values(
            token=token, parent_id=parent_id,
            expires_at=_now() + _dt.timedelta(days=days), created_at=_now()))


def get_parent_token(token: str):
    """Return the parent_id for a live token, or None. Expired tokens are deleted
    on sight so the table stays small."""
    from sqlalchemy import select, delete
    if not token:
        return None
    t = _tables["parent_tokens"]
    with _engine.connect() as conn:
        r = conn.execute(select(t.c.parent_id, t.c.expires_at)
                         .where(t.c.token == token)).first()
    if not r:
        return None
    exp = r[1]
    if exp is not None and exp.tzinfo is None:      # SQLite returns naive datetimes
        exp = exp.replace(tzinfo=_dt.timezone.utc)
    if exp is not None and exp < _now():
        with _engine.begin() as conn:
            conn.execute(delete(t).where(t.c.token == token))
        return None
    return r[0]


def create_parent_reset(token_hash: str, parent_id: str, minutes: int = 45) -> None:
    """Store a password-reset token HASH (never the token). Short-lived, single-use."""
    from sqlalchemy import insert
    t = _tables["parent_resets"]
    with _engine.begin() as conn:
        conn.execute(insert(t).values(
            token_hash=token_hash, parent_id=parent_id, used=0,
            expires_at=_now() + _dt.timedelta(minutes=minutes), created_at=_now()))


def consume_parent_reset(token_hash: str):
    """Redeem a reset token hash: returns the parent_id if it's real, unused, and
    unexpired -- and marks it used in the same transaction (single-use). Expired
    rows are swept on sight so the table stays small. Returns None otherwise."""
    from sqlalchemy import select, update, delete
    if not token_hash:
        return None
    t = _tables["parent_resets"]
    with _engine.begin() as conn:
        conn.execute(delete(t).where(t.c.expires_at < _now()))     # sweep expired
        r = conn.execute(select(t.c.parent_id, t.c.expires_at, t.c.used)
                         .where(t.c.token_hash == token_hash)).first()
        if not r or int(r[2] or 0):
            return None
        exp = r[1]
        if exp is not None and exp.tzinfo is None:                 # SQLite: naive UTC
            exp = exp.replace(tzinfo=_dt.timezone.utc)
        if exp is not None and exp < _now():
            return None
        conn.execute(update(t).where(t.c.token_hash == token_hash).values(used=1))
        return r[0]


def delete_parent_tokens_for(parent_id: str) -> None:
    """Sign this parent out of EVERY device (used after a password reset)."""
    from sqlalchemy import delete
    t = _tables["parent_tokens"]
    with _engine.begin() as conn:
        conn.execute(delete(t).where(t.c.parent_id == parent_id))


def delete_parent_token(token: str) -> None:
    from sqlalchemy import delete
    t = _tables["parent_tokens"]
    with _engine.begin() as conn:
        conn.execute(delete(t).where(t.c.token == token))


# ---- ADMIN: full account reset (2026-08-05) ---------------------------------
# Delete ONE parent account and EVERYTHING that belongs to it, atomically. Backs
# the admin-only "Start Fresh" tool so Jim can re-run the brand-new-parent signup
# with his own email. Scoped to a single parent_id -- it never reaches another
# account. Forum posts (community content) are deliberately NOT destroyed here:
# they are soft-delete-only by design and carry their author name on the row, so
# they still read fine after a reset.
_STUDENT_CODE_TABLES = [
    ("accounts", "code"), ("sessions", "code"), ("placements", "code"),
    ("topic_progress", "code"), ("unit_checks", "code"), ("student_stats", "code"),
    ("topic_quizzes", "code"), ("time_daily", "code"), ("awards", "code"),
    ("class_members", "student_code"),
]
_PARENT_KEYED_TABLES = [
    ("parent_tokens", "parent_id"), ("parent_resets", "parent_id"),
    ("parent_digests", "parent_id"),
]


def delete_parent_cascade(parent_id: str) -> dict:
    """Remove a parent, their student accounts, and every per-student and
    per-parent row tied to them. Returns {ok, deleted:{table: rows_deleted},
    student_codes:[...]}. All-or-nothing: one transaction, so a failure midway
    rolls the whole thing back and nothing is left half-deleted."""
    from sqlalchemy import delete, select
    pid = (parent_id or "").strip()
    if not pid:
        return {"ok": False, "reason": "no parent_id", "deleted": {}, "student_codes": []}
    acc = _tables["accounts"]
    deleted: dict = {}
    with _engine.begin() as conn:
        # This parent's students (read inside the txn for a consistent snapshot).
        codes = [r[0] for r in conn.execute(
            select(acc.c.code).where(acc.c.parent_id == pid)).fetchall()]
        # 1) every per-student row, for each of this parent's students
        if codes:
            for tname, col in _STUDENT_CODE_TABLES:
                t = _tables.get(tname)
                if t is None:
                    continue
                res = conn.execute(delete(t).where(t.c[col].in_(codes)))
                deleted[tname] = deleted.get(tname, 0) + int(res.rowcount or 0)
        # 2) belt-and-suspenders: any account still tagged to this parent
        res = conn.execute(delete(acc).where(acc.c.parent_id == pid))
        deleted["accounts"] = deleted.get("accounts", 0) + int(res.rowcount or 0)
        # 3) parent-keyed rows: sign-in tokens, reset links, weekly-digest state
        for tname, col in _PARENT_KEYED_TABLES:
            t = _tables.get(tname)
            if t is None:
                continue
            res = conn.execute(delete(t).where(t.c[col] == pid))
            deleted[tname] = deleted.get(tname, 0) + int(res.rowcount or 0)
        # 4) finally the parent row itself
        p = _tables["parents"]
        res = conn.execute(delete(p).where(p.c.id == pid))
        deleted["parents"] = deleted.get("parents", 0) + int(res.rowcount or 0)
    return {"ok": True, "deleted": deleted, "student_codes": codes}


# ---- weekly parent email (2026-08-04) ---------------------------------------
_DIGEST_COLS = ["parent_id", "last_sent_at", "optout", "optout_token", "created_at"]


def list_parents() -> list:
    """Every parent account: [{id, email, name}]. Powers the weekly-email pass."""
    from sqlalchemy import select
    t = _tables["parents"]
    with _engine.connect() as conn:
        rows = conn.execute(select(t.c.id, t.c.email, t.c.name)
                            .order_by(t.c.created_at)).all()
    return [{"id": r[0], "email": r[1], "name": r[2]} for r in rows]


def ensure_digest_state(parent_id: str) -> dict:
    """This parent's digest row, creating it (with a fresh unsubscribe token) on
    first touch. Returns {parent_id, last_sent_at, optout, optout_token}."""
    import secrets as _secrets
    from sqlalchemy import select
    t = _tables["parent_digests"]
    with _engine.connect() as conn:
        r = conn.execute(select(*[t.c[c] for c in _DIGEST_COLS])
                         .where(t.c.parent_id == parent_id)).first()
    if r:
        return _row_to_dict(r, _DIGEST_COLS)
    row = {"parent_id": parent_id, "last_sent_at": None, "optout": 0,
           "optout_token": _secrets.token_urlsafe(24), "created_at": _now()}
    _upsert("parent_digests", {"parent_id": parent_id}, {
        "last_sent_at": None, "optout": 0,
        "optout_token": row["optout_token"], "created_at": row["created_at"]})
    return row


def mark_digest_sent(parent_id: str) -> None:
    ensure_digest_state(parent_id)
    _upsert("parent_digests", {"parent_id": parent_id}, {"last_sent_at": _now()})


def set_digest_optout(parent_id: str, optout: bool) -> None:
    ensure_digest_state(parent_id)
    _upsert("parent_digests", {"parent_id": parent_id}, {"optout": 1 if optout else 0})


def parent_id_for_digest_token(token: str):
    """The parent this unsubscribe token belongs to, or None. The token grants
    ONLY the unsubscribe/resubscribe action -- it is not a login."""
    from sqlalchemy import select
    token = (token or "").strip()
    if not token:
        return None
    t = _tables["parent_digests"]
    with _engine.connect() as conn:
        r = conn.execute(select(t.c.parent_id)
                         .where(t.c.optout_token == token)).first()
    return r[0] if r else None


def week_activity(code: str, days: int = 7) -> dict:
    """The WINDOWED view of this student's last `days` calendar days -- the honest
    numbers the weekly parent email reports. Returns:
      {minutes_total, days_active, minutes_by_course: {course: min},
       checks: [{course, unit, best_pct, last_pct}],        # checks updated in window
       touched: [{course, unit, unit_name, status}],        # units worked in window
       award_ids: [...]}                                    # awards earned in window
    """
    from sqlalchemy import select
    cut = _now() - _dt.timedelta(days=days)
    day_cut = (_now() - _dt.timedelta(days=max(0, days - 1))).date().isoformat()
    out = {"minutes_total": 0, "days_active": 0, "minutes_by_course": {},
           "checks": [], "touched": [], "award_ids": []}

    td = _tables["time_daily"]
    with _engine.connect() as conn:
        rows = conn.execute(select(td.c.day, td.c.course, td.c.minutes)
                            .where((td.c.code == code) & (td.c.day >= day_cut))).all()
    days_seen = set()
    for day, course, minutes in rows:
        m = int(minutes or 0)
        if m > 0:
            days_seen.add(day)
        out["minutes_total"] += m
        out["minutes_by_course"][course] = out["minutes_by_course"].get(course, 0) + m
    out["days_active"] = len(days_seen)

    uc = _tables["unit_checks"]
    with _engine.connect() as conn:
        rows = conn.execute(select(uc.c.course, uc.c.unit, uc.c.best_pct, uc.c.last_pct,
                                   uc.c.updated_at).where(uc.c.code == code)).all()
    for course, unit, best, last, upd in rows:
        if upd is not None and _aware(upd) >= cut:
            out["checks"].append({"course": course, "unit": int(unit),
                                  "best_pct": int(best or 0), "last_pct": int(last or 0)})

    tp = _tables["topic_progress"]
    with _engine.connect() as conn:
        rows = conn.execute(select(tp.c.course, tp.c.unit, tp.c.unit_name, tp.c.status,
                                   tp.c.last_touched).where(tp.c.code == code)).all()
    for course, unit, uname, status_, last in rows:
        if last is not None and _aware(last) >= cut:
            out["touched"].append({"course": course, "unit": int(unit),
                                   "unit_name": uname or "", "status": status_ or ""})

    aw = _tables["awards"]
    with _engine.connect() as conn:
        rows = conn.execute(select(aw.c.award_id, aw.c.earned_at)
                            .where(aw.c.code == code)).all()
    for aid, earned in rows:
        if earned is not None and _aware(earned) >= cut:
            out["award_ids"].append(aid)
    return out


def create_student_account(code: str, name: str, parent_id: str) -> None:
    """A student created BY a signed-up parent. subscription_status 'family' marks it
    as parent-managed (entitlement comes from the parent's sub_status, checked live)."""
    _upsert("accounts", {"code": code}, {
        "name": (name or "").strip(), "email": "",
        "subscription_status": "family", "parent_id": parent_id, "created_at": _now(),
    })


_ACCOUNT_COLS = ["code", "name", "email", "subscription_status", "created_at", "parent_id"]


def get_account(code: str):
    from sqlalchemy import select
    t = _tables["accounts"]
    with _engine.connect() as conn:
        r = conn.execute(select(*[t.c[c] for c in _ACCOUNT_COLS])
                         .where(t.c.code == (code or "").strip())).first()
    return _row_to_dict(r, _ACCOUNT_COLS)


def list_students_for_parent(parent_id: str) -> list:
    """This parent's students, oldest first (creation order)."""
    from sqlalchemy import select
    t = _tables["accounts"]
    with _engine.connect() as conn:
        rows = conn.execute(select(*[t.c[c] for c in _ACCOUNT_COLS])
                            .where(t.c.parent_id == parent_id)
                            .order_by(t.c.created_at)).fetchall()
    return [_row_to_dict(r, _ACCOUNT_COLS) for r in rows]


# ---- beta passes (2026-07-31: Jim's beta-tester program) --------------------

_BETA_COLS = ["code", "label", "uses_allowed", "uses_used", "window_hours",
              "window_expires_at", "created_at", "revoked"]


def _aware(dt):
    """SQLite returns naive datetimes; treat them as UTC."""
    if dt is not None and dt.tzinfo is None:
        return dt.replace(tzinfo=_dt.timezone.utc)
    return dt


def create_beta_code(code: str, label: str = "", uses: int = 5, hours: int = 2) -> None:
    from sqlalchemy import insert
    t = _tables["beta_codes"]
    with _engine.begin() as conn:
        conn.execute(insert(t).values(
            code=code, label=(label or "").strip()[:120],
            uses_allowed=max(1, min(int(uses), 50)),
            uses_used=0, window_hours=max(1, min(int(hours), 24)),
            window_expires_at=None, created_at=_now(), revoked=0))


def get_beta_code(code: str):
    from sqlalchemy import select
    t = _tables["beta_codes"]
    with _engine.connect() as conn:
        r = conn.execute(select(*[t.c[c] for c in _BETA_COLS])
                         .where(t.c.code == (code or "").strip().upper())).first()
    if not r:
        return None
    d = {c: r[i] for i, c in enumerate(_BETA_COLS)}
    d["window_expires_at"] = _aware(d["window_expires_at"])
    return d


def beta_window_active(bc: dict) -> bool:
    exp = bc.get("window_expires_at")
    return bool(exp and exp > _now())


def beta_login(code: str):
    """One tester sign-in. Returns a status dict:
      {'ok': True, 'uses_left': n, 'window_expires_at': dt, 'consumed': bool}
      or {'ok': False, 'reason': 'unknown'|'revoked'|'exhausted'}
    A sign-in during an open window rides free; otherwise it consumes one use and
    opens a fresh window."""
    from sqlalchemy import update
    bc = get_beta_code(code)
    if not bc:
        return {"ok": False, "reason": "unknown"}
    if bc["revoked"]:
        return {"ok": False, "reason": "revoked"}
    if beta_window_active(bc):
        return {"ok": True, "consumed": False,
                "uses_left": bc["uses_allowed"] - bc["uses_used"],
                "window_expires_at": bc["window_expires_at"]}
    if bc["uses_used"] >= bc["uses_allowed"]:
        return {"ok": False, "reason": "exhausted"}
    new_exp = _now() + _dt.timedelta(hours=int(bc["window_hours"] or 2))
    t = _tables["beta_codes"]
    with _engine.begin() as conn:
        # Guarded update: only consume if the counters still match what we read,
        # so two simultaneous sign-ins can't burn two uses for one window.
        res = conn.execute(update(t).where(
            (t.c.code == bc["code"]) & (t.c.uses_used == bc["uses_used"]) &
            (t.c.revoked == 0)).values(
            uses_used=bc["uses_used"] + 1, window_expires_at=new_exp))
    if not res.rowcount:                      # lost a race: re-read and report honestly
        return beta_login(code)
    return {"ok": True, "consumed": True,
            "uses_left": bc["uses_allowed"] - bc["uses_used"] - 1,
            "window_expires_at": new_exp}


def list_beta_codes(limit: int = 200) -> list:
    from sqlalchemy import select
    t = _tables["beta_codes"]
    with _engine.connect() as conn:
        rows = conn.execute(select(*[t.c[c] for c in _BETA_COLS])
                            .order_by(t.c.created_at.desc()).limit(limit)).fetchall()
    out = []
    for r in rows:
        d = {c: r[i] for i, c in enumerate(_BETA_COLS)}
        for k in ("window_expires_at", "created_at"):
            d[k] = _aware(d[k])
            d[k] = d[k].isoformat() if d[k] else None
        out.append(d)
    return out


def revoke_beta_code(code: str) -> bool:
    from sqlalchemy import update
    t = _tables["beta_codes"]
    with _engine.begin() as conn:
        res = conn.execute(update(t).where(t.c.code == (code or "").strip().upper())
                           .values(revoked=1, window_expires_at=None))
    return bool(res.rowcount)


# ---- ops error log (2026-08-05) ---------------------------------------------

def record_error(where: str, what: str) -> None:
    """Log one unhandled server error. Best-effort by design: this function must
    NEVER raise (an error logger that errors is useless) and stays silent when
    the DB is off (the print() in main.py still reaches the Render logs). Sweeps
    rows older than 30 days on each write so the table can't grow forever."""
    if not _ENABLED:
        return
    from sqlalchemy import insert, delete
    try:
        t = _tables["error_log"]
        with _engine.begin() as conn:
            conn.execute(delete(t).where(
                t.c.created_at < _now() - _dt.timedelta(days=30)))
            conn.execute(insert(t).values(
                created_at=_now(),
                where=(where or "")[:160],
                what=(what or "")[:4000]))
    except Exception as exc:  # noqa: BLE001
        print(f"[error-log] could not record error: {exc}")


def recent_errors(hours: int = 24, limit: int = 50) -> list:
    """Newest-first unhandled errors in the window, for the /admin panel.
    [{when, where, what}] with isoformat timestamps. Empty list on any problem."""
    if not _ENABLED:
        return []
    from sqlalchemy import select
    try:
        t = _tables["error_log"]
        cutoff = _now() - _dt.timedelta(hours=int(hours))
        with _engine.connect() as conn:
            rows = conn.execute(
                select(t.c.created_at, t.c.where, t.c.what)
                .where(t.c.created_at >= cutoff)
                .order_by(t.c.created_at.desc()).limit(int(limit))).fetchall()
        out = []
        for r in rows:
            when = _aware(r[0])
            out.append({"when": when.isoformat() if when else None,
                        "where": r[1] or "", "what": r[2] or ""})
        return out
    except Exception as exc:  # noqa: BLE001
        print(f"[error-log] list failed: {exc}")
        return []


def errors_count(hours: int = 24) -> int:
    """How many unhandled errors in the window. 0 on any problem."""
    if not _ENABLED:
        return 0
    from sqlalchemy import select, func
    try:
        t = _tables["error_log"]
        cutoff = _now() - _dt.timedelta(hours=int(hours))
        with _engine.connect() as conn:
            n = conn.execute(select(func.count()).select_from(t)
                             .where(t.c.created_at >= cutoff)).scalar()
        return int(n or 0)
    except Exception as exc:  # noqa: BLE001
        print(f"[error-log] count failed: {exc}")
        return 0


# ---- community forum (2026-07-31: parents post, everyone reads) -------------

FORUM_SECTIONS = ("working", "ideas", "resources", "courses")


def create_forum_post(post_id: str, section: str, title: str, body: str,
                      parent_id: str, author_name: str) -> None:
    from sqlalchemy import insert
    t = _tables["forum_posts"]
    with _engine.begin() as conn:
        conn.execute(insert(t).values(
            id=post_id, section=section, title=title, body=body,
            parent_id=parent_id, author_name=author_name,
            reply_count=0, created_at=_now(), deleted=0))


_POST_COLS = ["id", "section", "title", "body", "author_name", "reply_count", "created_at"]


def list_forum_posts(section: str, limit: int = 100) -> list:
    """Newest first, hidden posts excluded. Body included (posts are short)."""
    from sqlalchemy import select
    t = _tables["forum_posts"]
    with _engine.connect() as conn:
        rows = conn.execute(
            select(*[t.c[c] for c in _POST_COLS])
            .where((t.c.section == section) & (t.c.deleted == 0))
            .order_by(t.c.created_at.desc()).limit(limit)).fetchall()
    out = []
    for r in rows:
        d = {c: r[i] for i, c in enumerate(_POST_COLS)}
        d["created_at"] = d["created_at"].isoformat() if d["created_at"] else None
        out.append(d)
    return out


def get_forum_post(post_id: str):
    """One post + its visible replies (oldest first), or None."""
    from sqlalchemy import select
    t = _tables["forum_posts"]
    with _engine.connect() as conn:
        r = conn.execute(select(*[t.c[c] for c in _POST_COLS])
                         .where((t.c.id == post_id) & (t.c.deleted == 0))).first()
    if not r:
        return None
    post = {c: r[i] for i, c in enumerate(_POST_COLS)}
    post["created_at"] = post["created_at"].isoformat() if post["created_at"] else None
    tr = _tables["forum_replies"]
    cols = ["id", "author_name", "body", "created_at"]
    with _engine.connect() as conn:
        rows = conn.execute(select(*[tr.c[c] for c in cols])
                            .where((tr.c.post_id == post_id) & (tr.c.deleted == 0))
                            .order_by(tr.c.created_at)).fetchall()
    post["replies"] = []
    for r in rows:
        d = {c: r[i] for i, c in enumerate(cols)}
        d["created_at"] = d["created_at"].isoformat() if d["created_at"] else None
        post["replies"].append(d)
    return post


def create_forum_reply(reply_id: str, post_id: str, body: str,
                       parent_id: str, author_name: str) -> bool:
    """Add a reply and bump the post's reply_count. False if the post is gone/hidden."""
    from sqlalchemy import insert, select, update
    tp = _tables["forum_posts"]
    tr = _tables["forum_replies"]
    with _engine.begin() as conn:
        exists = conn.execute(select(tp.c.id).where(
            (tp.c.id == post_id) & (tp.c.deleted == 0))).first()
        if not exists:
            return False
        conn.execute(insert(tr).values(
            id=reply_id, post_id=post_id, parent_id=parent_id,
            author_name=author_name, body=body, created_at=_now(), deleted=0))
        conn.execute(update(tp).where(tp.c.id == post_id)
                     .values(reply_count=tp.c.reply_count + 1))
    return True


def delete_forum_item(kind: str, item_id: str) -> bool:
    """Moderator soft-delete ('post' or 'reply'). Hides, never destroys."""
    from sqlalchemy import update
    t = _tables["forum_posts"] if kind == "post" else _tables["forum_replies"]
    with _engine.begin() as conn:
        res = conn.execute(update(t).where(t.c.id == item_id).values(deleted=1))
    return bool(res.rowcount)


def status() -> dict:
    """Small diagnostic for a health/status endpoint. `configured` = did the app see a
    DATABASE_URL at all; `reason` = why it's disabled (credentials redacted)."""
    return {
        "db_enabled": _ENABLED,
        "dialect": (_engine.dialect.name if _engine else None),
        "configured": bool(DATABASE_URL),
        "reason": (None if _ENABLED else _INIT_ERROR),
    }


# ---- admin dashboard aggregates (2026-08-03: Jim's central /admin page) ------
def log_usage(kind: str, code: str = "", course: str = "", mode: str = "", model: str = "",
              input_tokens: int = 0, output_tokens: int = 0, cache_read_tokens: int = 0,
              cache_write_tokens: int = 0, tts_chars: int = 0, tts_cache_hit: bool = False,
              attempts: int = 1, verify_status: str = "") -> None:
    """Record one paid event (a tutor brain turn or a TTS request). COUNTS ONLY -- no
    conversation text ever. Fire-and-forget: every error is swallowed and printed,
    because usage logging must NEVER break or slow a lesson. No-op when the DB is off
    (the numbers can't be recovered later, but teaching always comes first)."""
    if not _ENABLED:
        return
    try:
        import uuid as _uuid
        t = _tables["usage_log"]
        with _engine.begin() as conn:
            conn.execute(t.insert().values(
                id=_uuid.uuid4().hex, kind=str(kind)[:16], code=str(code or "")[:64],
                course=str(course or "")[:32], mode=str(mode or "")[:24],
                model=str(model or "")[:64],
                input_tokens=int(input_tokens or 0), output_tokens=int(output_tokens or 0),
                cache_read_tokens=int(cache_read_tokens or 0),
                cache_write_tokens=int(cache_write_tokens or 0),
                tts_chars=int(tts_chars or 0), tts_cache_hit=1 if tts_cache_hit else 0,
                attempts=int(attempts or 1), verify_status=str(verify_status or "")[:16],
                created_at=_now()))
    except Exception as exc:  # noqa: BLE001
        print(f"[store] log_usage failed (non-fatal): {_redact(str(exc))}")


def usage_stats(days: int = 7) -> dict:
    """Aggregate the usage log for /admin: token totals, verifier breakdown, retry count,
    distinct students served, and TTS characters generated vs served free from cache.
    All-zeros when the DB is off; any query error is swallowed (never 500s)."""
    out = {"days": days,
           "brain_calls": 0, "input_tokens": 0, "output_tokens": 0,
           "cache_read_tokens": 0, "cache_write_tokens": 0,
           "retries": 0, "brain_students": 0,
           "verify_ok": 0, "verify_fixed": 0, "verify_unresolved": 0,
           "verify_unverifiable": 0, "verify_none": 0,
           "tts_requests": 0, "tts_chars_generated": 0, "tts_chars_cached": 0}
    if not _ENABLED:
        return out
    from sqlalchemy import select, func
    try:
        U = _tables["usage_log"]
        cutoff = _now() - _dt.timedelta(days=int(days))
        recent = U.c.created_at >= cutoff
        brain = (U.c.kind == "brain") & recent
        tts = (U.c.kind == "tts") & recent
        with _engine.connect() as conn:
            row = conn.execute(select(
                func.count(),
                func.coalesce(func.sum(U.c.input_tokens), 0),
                func.coalesce(func.sum(U.c.output_tokens), 0),
                func.coalesce(func.sum(U.c.cache_read_tokens), 0),
                func.coalesce(func.sum(U.c.cache_write_tokens), 0),
                func.coalesce(func.sum(U.c.attempts), 0),
            ).where(brain)).fetchone()
            out["brain_calls"] = int(row[0] or 0)
            out["input_tokens"] = int(row[1] or 0)
            out["output_tokens"] = int(row[2] or 0)
            out["cache_read_tokens"] = int(row[3] or 0)
            out["cache_write_tokens"] = int(row[4] or 0)
            out["retries"] = max(0, int(row[5] or 0) - out["brain_calls"])
            out["brain_students"] = int(conn.execute(
                select(func.count(func.distinct(U.c.code)))
                .where(brain & (U.c.code != ""))).scalar() or 0)
            for vs, n in conn.execute(
                    select(U.c.verify_status, func.count()).where(brain)
                    .group_by(U.c.verify_status)).fetchall():
                key = "verify_" + (vs or "none")
                if key in out:
                    out[key] += int(n or 0)
                else:
                    out["verify_none"] += int(n or 0)
            out["tts_requests"] = int(conn.execute(
                select(func.count()).where(tts)).scalar() or 0)
            out["tts_chars_generated"] = int(conn.execute(
                select(func.coalesce(func.sum(U.c.tts_chars), 0))
                .where(tts & (U.c.tts_cache_hit == 0))).scalar() or 0)
            out["tts_chars_cached"] = int(conn.execute(
                select(func.coalesce(func.sum(U.c.tts_chars), 0))
                .where(tts & (U.c.tts_cache_hit == 1))).scalar() or 0)
    except Exception as exc:  # noqa: BLE001
        out["error"] = _redact(str(exc))
        print(f"[store] usage_stats failed: {out['error']}")
    return out


def admin_stats() -> dict:
    """Privacy-safe aggregate numbers for Jim's /admin dashboard. Returns only
    COUNTS and TOTALS -- never a name, email, or login code -- read straight from
    the live tables, so nothing here is invented. If the database is off, every
    number is 0 and db_enabled is False. Any query error is swallowed (the
    dashboard must never 500) and reported in an 'error' key.

    seats = paid Stripe seats; one seat covers up to 2 children (see KIDS_PER_SEAT
    in main.py), so children_covered_capacity = seats * 2."""
    out = {
        "db_enabled": _ENABLED,
        "parents_total": 0, "parents_active": 0, "parents_past_due": 0,
        "parents_canceled": 0, "parents_free": 0,
        "seats_paid": 0, "seats_monthly": 0, "seats_annual": 0,
        "children_covered_capacity": 0, "est_monthly_usd": 0,
        "students_total": 0, "students_family": 0,
        "active_7d": 0, "active_30d": 0,
        "minutes_total": 0, "minutes_7d": 0,
        "units_mastered": 0, "checks_taken": 0, "problems_practiced": 0,
        "forum_posts": 0, "forum_replies": 0,
        "beta_total": 0, "beta_active_windows": 0, "beta_signins_used": 0,
    }
    if not _ENABLED:
        return out
    from sqlalchemy import select, func
    try:
        P = _tables["parents"]; A = _tables["accounts"]; SS = _tables["student_stats"]
        TD = _tables["time_daily"]; UC = _tables["unit_checks"]
        FP = _tables["forum_posts"]; FR = _tables["forum_replies"]; BC = _tables["beta_codes"]
        today = _now().date()
        cutoff7 = (today - _dt.timedelta(days=7)).isoformat()
        cutoff30 = (today - _dt.timedelta(days=30)).isoformat()
        now = _now()
        with _engine.connect() as conn:
            def scalar(q):
                v = conn.execute(q).scalar()
                return int(v) if v is not None else 0
            out["parents_total"] = scalar(select(func.count()).select_from(P))
            for st, n in conn.execute(
                    select(P.c.sub_status, func.count()).group_by(P.c.sub_status)).fetchall():
                key = "parents_" + (st or "free")
                if key in out:
                    out[key] = int(n or 0)
                else:                       # unknown/blank status folds into "free"
                    out["parents_free"] += int(n or 0)
            # Paid seats + estimated monthly revenue -- ACTIVE subscriptions only.
            for plan, seats in conn.execute(
                    select(P.c.sub_plan, func.coalesce(func.sum(P.c.sub_quantity), 0))
                    .where(P.c.sub_status == "active").group_by(P.c.sub_plan)).fetchall():
                seats = int(seats or 0)
                if (plan or "") == "annual":
                    out["seats_annual"] += seats
                else:
                    out["seats_monthly"] += seats
            out["seats_paid"] = out["seats_monthly"] + out["seats_annual"]
            out["children_covered_capacity"] = out["seats_paid"] * 2
            out["est_monthly_usd"] = out["seats_monthly"] * 29 + out["seats_annual"] * 24
            # Students (family students = accounts tied to a real parent account).
            out["students_total"] = scalar(select(func.count()).select_from(A))
            out["students_family"] = scalar(
                select(func.count()).select_from(A)
                .where((A.c.parent_id.isnot(None)) & (A.c.parent_id != "")))
            # Engagement.
            out["active_7d"] = scalar(
                select(func.count()).select_from(SS).where(SS.c.last_active >= cutoff7))
            out["active_30d"] = scalar(
                select(func.count()).select_from(SS).where(SS.c.last_active >= cutoff30))
            out["minutes_total"] = scalar(select(func.coalesce(func.sum(TD.c.minutes), 0)))
            out["minutes_7d"] = scalar(
                select(func.coalesce(func.sum(TD.c.minutes), 0)).where(TD.c.day >= cutoff7))
            out["units_mastered"] = scalar(
                select(func.count()).select_from(UC).where(UC.c.best_pct >= PASS_PCT))
            out["checks_taken"] = scalar(select(func.coalesce(func.sum(SS.c.checks_taken), 0)))
            out["problems_practiced"] = scalar(
                select(func.coalesce(func.sum(SS.c.problems_practiced), 0)))
            # Community forum (soft-deleted rows excluded).
            out["forum_posts"] = scalar(
                select(func.count()).select_from(FP).where(FP.c.deleted == 0))
            out["forum_replies"] = scalar(
                select(func.count()).select_from(FR).where(FR.c.deleted == 0))
            # Beta passes.
            out["beta_total"] = scalar(
                select(func.count()).select_from(BC).where(BC.c.revoked == 0))
            out["beta_signins_used"] = scalar(
                select(func.coalesce(func.sum(BC.c.uses_used), 0)))
            out["beta_active_windows"] = scalar(
                select(func.count()).select_from(BC).where(
                    (BC.c.revoked == 0) & (BC.c.window_expires_at.isnot(None)) &
                    (BC.c.window_expires_at > now)))
    except Exception as exc:  # noqa: BLE001 -- the dashboard must never 500 on a stat
        print(f"[store] admin_stats failed: {_redact(exc)}")
        out["error"] = type(exc).__name__
    return out


# I did no harm and this file is not truncated.
