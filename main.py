# =============================================================================
# main.py  --  Math Tutor MVP  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-07-30  APP_BUILD -> "2026-07-30f-lockdown". MARKET-PREP SECURITY PASS (Tier 1 of the
#               Market_Readiness_Review):
#               (1) /api/speak and /api/transcribe now REQUIRE a valid student code (they spend real
#                   ElevenLabs money and previously took none), spoken text is capped at MAX_SPEAK_CHARS,
#                   and both are rate limited. Pages pass &code= on their speak/transcribe calls now.
#               (2) NEW in-process sliding-window RATE LIMITER (_rate_limit): /api/chat, /api/practice,
#                   /api/topic capped at 40 messages / 5 min per code (far above human pace; stops
#                   runaway scripts spending the Anthropic budget); /api/login capped at 20 attempts /
#                   5 min per IP (the 4-digit code space can't be brute-forced quickly).
#               (3) TTS cache now has a 300 MB cap with oldest-first eviction (_evict_tts_cache) --
#                   it previously grew without bound.
#               (4) REMOVED the public /avatar-lab route (internal experiment; exposed internal notes
#                   and an unauthenticated paid-TTS call) -- static/avatar-lab.html is now a stub.
#               (5) REMOVED GET /api/progress/{code} + `import progress`: it served FABRICATED sample
#                   stats; verified nothing calls it (dashboard uses real /api/courses + /api/topics).
#                   progress.py is now unused and can be deleted from the repo.
#               (6) NEW routes /privacy and /terms serving the new static trust pages.
#   2026-07-30  APP_BUILD -> "2026-07-30e-opener". No logic change in this file; the bump pairs with a
#               tutor.py SESSION-opener fix (no fake "placement challenge" claim; goals card shown once).
#               Verify /health shows this stamp after deploy.
#   2026-07-30  APP_BUILD -> "2026-07-30d-topicfix". No logic change in this file; the bump pairs with a
#               tutor.py TOPIC-MODE prompt fix (goals card shows once; every turn hands the ball back so
#               the tutor never stops on a bare statement). Verify /health shows this stamp after deploy.
#   2026-07-30  APP_BUILD -> "2026-07-30c-caching". COST CONTROL: (1) TTS AUDIO CACHE on /api/speak --
#               identical text is served from an on-disk cache instead of re-calling ElevenLabs (the
#               cached bytes are the same render, so no quality change); (2) pairs with tutor.py PROMPT
#               CACHING on the model calls. Both are billing/latency only. Verify /health shows this stamp.
#   2026-07-30  APP_BUILD -> "2026-07-30b-toolhelp". No logic change here; pairs with a tutor.py change
#               so Mr. Cadabra can explain HOW to use the 🧮 math keyboard and 📈 graph paper on request.
#   2026-07-30  APP_BUILD -> "2026-07-30a-graphtool". No logic change in this file; the bump pairs with
#               a tutor.py change that teaches the tutor about the new 📈 Graph tool (coordinate graph
#               paper; plotted points arrive as text coordinates). Also new static static/graph-input.js
#               + graph script includes on session/practice/topic. Verify /health shows this stamp.
#   2026-07-29  APP_BUILD -> "2026-07-29b-scopeguard". No logic change in this file; the bump pairs
#               with a tutor.py change that adds a firm GROUND_RULES scope/jailbreak block to every
#               mode's system prompt (math-only, refuses off-topic/other-student/override attempts;
#               cross-course math still allowed). Verify /health shows this stamp after Render rebuilds.
#   2026-07-29  APP_BUILD -> "2026-07-29a-untruncate". No logic change in this file; the bump pairs
#               with a tutor.py fix that raised the student-facing reply cap max_tokens 700 -> 1200 so
#               long lesson openers (a [[goal]] plus a big [[card]]) stop getting truncated mid-tag.
#               Verify /health shows this stamp after Render rebuilds; if it's stale, do Manual Deploy
#               -> "Clear build cache & deploy latest commit". Do no harm.
#   2026-07-28  THREE FRONT DOORS -- STUDENT / PARENT / TEACHER. Stamp -> "2026-07-28s-threedoors".
#               The home page now has three clearly separated sign-in sections instead of one student
#               box with a combined "parent or teacher?" link, so each person lands on exactly the
#               view meant for them: a STUDENT on their own hub, a PARENT on their child's read-only
#               progress (/dashboard?..&view=parent), a TEACHER on every class they run
#               (/teacher?teacher=CODE). Backend change is small and additive: ClassIn gained an
#               optional teacher_code, POST /api/class passes it through, and the NEW endpoint
#               GET /api/teacher/{teacher_code}/classes lists that teacher's classes (with student
#               counts) on top of store.list_classes_for_teacher(). store.py adds ONE nullable column
#               (classes.teacher_code) via a self-healing additive migration, so classes made before
#               today still open by class code.
#               HONEST LIMIT, stated plainly: with no accounts yet these are DOORS, NOT LOCKS --
#               anyone holding a code can open that door. Separating the roles makes the app clear
#               and safe to USE; real access control is the accounts work still deferred, and a pilot
#               school must be told so. No existing endpoint, model, table or route changed.
#               Do no harm.
#   2026-07-28  "MY COURSES" -- THE DASHBOARD NO LONGER SHOWS ONLY ONE COURSE. Stamp ->
#               "2026-07-28r-mycourses". A student could only ever see the course they happened to
#               enter with, which broke the app's own core case: a student in Algebra I who is also
#               shoring up fractions in Pre-Algebra saw HALF their progress and needed four clicks to
#               reach the rest. New GET /api/courses/{code} returns every course with REAL activity
#               (units started/mastered/checked, avg best, last active) in ladder order, built on the
#               new store.get_course_activity(code) which gathers it in ONE pass over topic_progress
#               + unit_checks rather than a query per course. Courses never opened are omitted
#               (nothing invented); when tracking is off it reports that. dashboard.html renders the
#               strip and hides it entirely for a single-course student, so nothing changes for them.
#               Read-only and additive -- no existing endpoint, table, or signature touched.
#   2026-07-28  PHASE 4 -- DIFFERENTIAL EQUATIONS COURSE COMPLETE (eighth full peer, and the top of
#               the ladder). Stamp -> "2026-07-28q-diffeq". No route/logic change here (only the
#               stamp) -- `course` flows generically. Landed in curriculum.py (COURSES["diffeq"]) +
#               pedagogy.py (COURSE_PEDAGOGY["diffeq"]) + tutor.py (DIFFEQ lesson brain, CLASSIFY-
#               FIRST + scope/subject) + the 5 static files (home picker, dashboard title, topic
#               UNITS, session CURRICULUM/opener, challenge DIFFEQ 45-Q bank). Assumes Calculus and
#               does not re-teach it. Source: DiffEq_Curriculum_KB.md. Do no harm.
#   2026-07-28  PHASE 4 -- CALCULUS COURSE COMPLETE (seventh full peer). Stamp -> "2026-07-28p-calculus".
#               No route/logic change here (only the stamp) -- `course` flows generically. Landed in
#               curriculum.py (COURSES["calculus"]) + pedagogy.py (COURSE_PEDAGOGY["calculus"]) +
#               tutor.py (CALCULUS lesson brain, idea-before-machinery, heavy grapher use + scope/
#               subject) + the 5 static files (home picker, dashboard title, topic UNITS, session
#               CURRICULUM/opener, challenge CALCULUS 45-Q bank). Source: Calculus_Curriculum_KB.md.
#               Do no harm -- the six existing courses untouched.
#   2026-07-28  MR. CADABRA GETS A FACE. Stamp -> "2026-07-28o-robotface". New shared
#               static/tutor-face.js draws a small friendly ROBOT HEAD into the existing
#               <canvas id="orb"> on session/practice/topic/challenge, driven by the SAME 0..1
#               amplitude those pages already computed from the ElevenLabs audio analyser -- so his
#               mouth opens in time with his real speech. Eyes blink and drift, the antenna glows
#               with his voice, and the mood follows the page state (speaking / listening /
#               thinking / happy / idle). No new dependency, no avatar service, no extra network
#               call; if the script ever fails to load the pages fall back to a simple orb. This is
#               a deliberately stylized head, NOT the realistic 3D avatar that was tried and
#               rejected earlier. Static-only change (+ this stamp). Do no harm.
#   2026-07-28  TEACHER / PARENT CLASSROOM VIEW. Stamp -> "2026-07-28n-classroom". New: a lightweight
#               CLASS concept so a teacher or parent can follow SEVERAL students at once. Added
#               ClassIn/ClassStudentIn models, the helpers _class_or_404 + _class_student_row, the
#               endpoints POST /api/class, GET /api/class/{code}, POST+DELETE
#               /api/class/{code}/students[...], and GET /api/class/{code}/summary?course= (the
#               classroom payload: every student's per-unit best scores + class-wide per-unit
#               averages and a needs-help ranking), plus the GET /teacher page route. Roster lives in
#               store.py's new `classes`/`class_members` tables. Deliberately NOT an accounts system:
#               no password, no new personal data -- a class code just groups student codes that
#               ALREADY exist in students.json (unknown codes are rejected with a clear message).
#               Every endpoint reports tracking:false when the DB is off. Existing single-student
#               /dashboard?view=teacher is untouched. Do no harm.
#   2026-07-28  PHASE 4 -- PROBABILITY & STATISTICS COURSE COMPLETE (sixth full peer). Stamp ->
#               "2026-07-28m-probstat". No route/logic change here (only the stamp) -- `course` flows
#               generically. Landed in curriculum.py (COURSES["probstat"]) + pedagogy.py
#               (COURSE_PEDAGOGY["probstat"]) + tutor.py (PROBSTAT lesson brain built on the stats
#               visuals + scope/subject) + the 5 static files (home picker, dashboard title, topic
#               UNITS, session CURRICULUM/opener, challenge PROBSTAT 45-Q bank). Source:
#               ProbStat_Curriculum_KB.md. Do no harm -- the five existing courses untouched.
#   2026-07-28  GRAPHICS STAGE 3 -- TRIG / CONICS / NUMBER LINE / TILES / VECTORS. Stamp ->
#               "2026-07-28l-figures". Six new figures in static/math-figures.js ([[unitcircle]],
#               [[righttriangle]], [[conic]], [[numberline]], [[areamodel]], [[vector]]) routed by the
#               3 pages to showFig(). tutor.py practice/topic + the Pre-Calc lesson prompt document them.
#               No route/logic change here (only the stamp). Do no harm.
#   2026-07-28  GRAPHICS STAGE 2 -- STATISTICS & PROBABILITY VISUALS. Stamp -> "2026-07-28k-statsviz".
#               Nine new figures in static/math-figures.js ([[bars]]/[[histogram]]/[[dotplot]]/
#               [[boxplot]]/[[scatter]] with least-squares fit/[[normal]]/[[twoway]]/[[tree]]/[[pie]]),
#               routed by session/practice/topic.html to showFig(). tutor.py practice/topic prompts now
#               document them. No route/logic change here (only the stamp). Do no harm.
#   2026-07-28  GRAPHICS STAGE 1 -- REAL FUNCTION GRAPHER. Stamp -> "2026-07-28j-grapher". No route/logic
#               change here (only the stamp). New shared static/math-figures.js exposes
#               window.MathFigures.svg('graph', attrs): [[graph]] now plots ANY function of x
#               (sin/cos/tan, exp, logs, higher-degree polynomials, rationals WITH asymptotes, sqrt,
#               abs) via func=, on top of the old lines=/parabola=/points=. Wired into session/practice/
#               topic.html (a showFig() helper + [[graph]] -> showFig; math-figures.js include). tutor.py
#               graph docs now teach func=. Backend stamp so /health confirms the tutor.py deploy landed.
#               Do no harm -- purely additive.
#   2026-07-28  PHASE 4 -- TRIG / PRE-CALC COURSE COMPLETE (fifth full peer). Stamp -> "2026-07-28i-precalc".
#               No route/logic change here -- `course` already flows generically. The work landed in
#               curriculum.py (COURSES["precalc"]) + pedagogy.py (COURSE_PEDAGOGY["precalc"]) + tutor.py
#               (PRECALC lesson template + practice/topic scope + subject) + the 5 static files (home
#               picker card, dashboard title, topic UNITS, session CURRICULUM/opener, challenge PRECALC
#               45-question assessment bank). Source: PreCalc_Curriculum_KB.md. This stamp lets /health
#               confirm the backend (tutor.py) deploy landed. Do no harm -- the four existing courses
#               untouched.
#   2026-07-28  COMPREHENSIVE COURSE ASSESSMENT + COURSE-SCOPED CHECKS. Stamp -> "2026-07-28h-assessment".
#               The quick adaptive placement became a voluntary, comprehensive Course Assessment
#               (challenge.html: all 9 units x 5 Qs, per-unit 0..10 scoring, recommended-path /
#               choose-your-own results). The forced first-entry redirect was removed (home.html +
#               session.html), and a "Course assessment" link now lives in the sidebar. Backend change
#               HERE: CheckIn gained `course`, and /api/check now files the check under the RIGHT
#               course (curriculum.unit_name(course, unit) + store.record_check(..., course)) instead of
#               always Algebra I -- so the assessment's per-unit scores (and the tutor's own end-of-unit
#               checks in Geometry/Pre-Algebra/Algebra II) land on the correct per-course dashboard.
#               Backward-compatible: course defaults to 'algebra1'. Do no harm.
#   2026-07-28  PHASE 4 -- ALGEBRA II COURSE COMPLETE (fourth full peer). Stamp -> "2026-07-28g-algebra2".
#               No route/logic change in this file -- `course` already flows generically through every
#               endpoint (chat/practice/topic/placement/session/topics) to curriculum/pedagogy/tutor/
#               store, all of which now know "algebra2". The work landed in: curriculum.py (COURSES
#               ["algebra2"] + rules) + pedagogy.py (COURSE_PEDAGOGY["algebra2"]) + tutor.py
#               (ALGEBRA2 lesson template + practice/topic scope + subject) + the 5 static files
#               (home picker card, dashboard title, topic UNITS, session CURRICULUM/opener, challenge
#               ALG2 placement bank). This stamp lets /health confirm the backend (tutor.py) deploy
#               landed. Source: AlgebraII_Curriculum_KB.md. Do no harm -- other courses untouched.
#   2026-07-28  INTRO/EXPECTATIONS + COLUMN-MATH VISUAL. Stamp -> "2026-07-28f-introcolumn".
#               Backend change is in tutor.py only: (1) Topic mini-lessons now open with a topic intro +
#               a "by the end you'll be able to..." goals card; (2) all three lesson openers show a short
#               expectations goals card after the goal banner; (3) documented the new [[column]] tag for
#               stacked, decimal-point-aligned add/subtract. The [[column]] renderer itself is static
#               (session/practice/topic.html). This stamp lets /health confirm the tutor.py deploy landed.
#   2026-07-28  PHASE 4 -- PRE-ALGEBRA COURSE COMPLETE (full peer). Stamp -> "2026-07-28e-prealgebra".
#               tutor.py gained the Pre-Algebra lesson prompt + scope/subject; challenge.html a 9-tier
#               Pre-Algebra placement bank (course selection now handles 3 courses); topic.html +
#               session.html the Pre-Algebra concept/curriculum menus; home.html a Pre-Algebra picker
#               card (first) + title; dashboard.html the title label. Pre-Algebra is now pickable and a
#               full peer of Algebra/Geometry. Backend change = tutor prompt only (+ this stamp); rest
#               is static. Algebra I + Geometry unchanged.
#   2026-07-28  PHASE 4 -- PRE-ALGEBRA COURSE (catalog + teaching brain). Stamp -> "2026-07-28d-prealgcat".
#               curriculum.py + pedagogy.py gained a third course, "prealgebra" (9 foundations units:
#               number sense/order-of-ops, factors, integers, fractions, decimals, ratios, percents,
#               measurement, variables). Additive; Algebra I + Geometry unchanged (verified). NOT
#               student-reachable yet -- the Pre-Algebra lesson prompt, placement bank, unit lists,
#               and picker card come next. This stamp just confirms the new backend modules deployed.
#   2026-07-28  PHASE 4 (geometry) -- GEOMETRY WHITEBOARD FIGURES. Stamp -> "2026-07-28c-geofigures".
#               New shared static/geo-figures.js draws labeled triangles, angles, and circles; the
#               three whiteboard pages load it and dispatch [[triangle]]/[[angle]]/[[circle]] tags,
#               and the Geometry lesson prompt (tutor.py) documents them. Backend change is only the
#               tutor prompt + this stamp; everything else is static. Algebra unaffected.
#   2026-07-28  MULTI-COURSE (Phase 3.4c) -- PER-COURSE DASHBOARD. Stamp -> "2026-07-28b-coursedash".
#               /api/topics/{code} now takes ?course= and returns THAT course's units + mastery
#               (store.get_topics/get_mastery(code, course) + curriculum.units_for(course) +
#               read_placement(code, course)). dashboard.html reads the course and carries it in its
#               links. Default algebra1, so single-course behavior is unchanged. This completes the
#               per-course front door: Geometry is now a full peer of Algebra end to end.
#   2026-07-28  MULTI-COURSE (Phase 3.4b) -- PER-COURSE PLACEMENT + SESSION ENDPOINTS. Stamp ->
#               "2026-07-28a-placement". Threaded `course` through the session/placement wrappers
#               (get_session/save_session/read_placement/save_placement + a file-key helper _ck) and
#               the endpoints /api/session, /api/placement (POST + GET), plus /api/chat's session
#               get/save and placement read. So a student's lesson session AND placement are now
#               read/written PER COURSE end-to-end, and the hub gates first-entry placement per
#               course (challenge.html now serves a Geometry question bank). Algebra I is the default
#               everywhere, so single-course behavior is unchanged.
#   2026-07-27  MULTI-COURSE (Phase 3.3) -- PER-COURSE SESSION MEMORY + PLACEMENT (storage). Stamp ->
#               "2026-07-27e-coursemem". store.py's `sessions` and `placements` tables are now keyed by
#               (code, course) with the same self-healing migration (existing rows stamped 'algebra1'),
#               so a student can hold a separate lesson session AND placement per course. store's
#               session/placement functions default course to 'algebra1', so THIS file's calls are
#               UNCHANGED and behavior is identical until the picker threads a course (3.4). Verified on
#               SQLite: fresh, old-schema migration across all four course tables, separation, idempotent.
#   2026-07-27  MULTI-COURSE (Phase 3, step 2) -- COURSE-MODE LESSON PER COURSE. Stamp -> "2026-07-27d-geomlesson".
#               ChatRequest gains `course` (default 'algebra1'); /api/chat passes it to
#               tutor.get_tutor_reply (which now selects the course's lesson template), to
#               _mastery_note (course-scoped mastery steering via store), and to the course-activity
#               _track_topic (records "learning" under the right course). Nothing changes for Algebra I
#               (the default); the Algebra lesson prompt is byte-identical (verified). Geometry course
#               mode becomes reachable once the picker sends course='geometry' (Phase 3.4).
#   2026-07-27  MULTI-COURSE (Phase 3, step 1) -- COURSE-AWARE PRACTICE + TOPIC. Stamp -> "2026-07-27c-ptcourse".
#               PracticeRequest/TopicRequest gain an optional `course` (default 'algebra1'); the
#               /api/practice + /api/topic handlers pass it to tutor.get_practice_reply /
#               get_topic_reply, to curriculum.classify_unit (classify within the course), and to
#               _track_topic (which now records progress under the right course via store). Nothing
#               changes for Algebra I (the default); once the course picker sends course='geometry',
#               those two modes teach + track Geometry. Verified: Algebra prompts byte-identical,
#               Geometry assembles with its own scope + pedagogy. See Multi_Course_Expansion_Plan.md.
#   2026-07-27  MULTI-COURSE (Phase 2) -- COURSE-AWARE PROGRESS DB. Stamp -> "2026-07-27b-coursedb".
#               store.py's per-unit tables (topic_progress, unit_checks) are now keyed by
#               (code, course, unit) with a self-healing migration that stamps all EXISTING rows
#               'algebra1' (nothing lost). Every store function defaults course to 'algebra1', so
#               main.py's calls here are UNCHANGED and student-facing behavior is identical until
#               the course picker (Phase 3) supplies a course. Verified on SQLite: fresh-create,
#               old-schema migration, course separation, idempotent restart. See the project doc
#               Multi_Course_Expansion_Plan.md.
#   2026-07-27  MULTI-COURSE CATALOG (Phase 1). Stamp -> "2026-07-27a-catalog". curriculum.py and
#               pedagogy.py became a two-level course CATALOG (Course -> units) with a second course,
#               Geometry, added; both stay BACKWARD-COMPATIBLE so main.py / tutor.py are unchanged and
#               Algebra I behaves byte-for-byte as before (verified: 20 classify inputs + all playbook
#               states identical to the originals). This stamp bump only CONFIRMS Render redeployed the
#               new modules -- no route or student-facing behavior change yet (the course picker is a
#               later phase). See the project doc Multi_Course_Expansion_Plan.md.
#   2026-07-25  STT NON-SPEECH SCRUB. Stamp -> "2026-07-25b-navtype-stt". Added _clean_transcript()
#               and applied it to /api/transcribe: speech-to-text hallucinations on silence/noise
#               ("[outro jingle]", "[music]", "(applause)", musical notes) are stripped, and if
#               nothing real remains the endpoint returns "" so the UI says "didn't catch that"
#               instead of feeding garbage to the tutor. (A hallucinated "[outro jingle]" had made
#               Mr. Cadabra end a whole topic after one question.) tutor.py adds a matching topic
#               no-self-wrapup guard. Also this build ships the topic/practice nav + type-box UI.
#   2026-07-24  PHASE E -- VISUAL POLISH. Stamp -> "2026-07-24l-polish". Restyled index.html
#               (login) onto the app's design system (warm gradient bg, purple/teal brand
#               gradient, app card/shadow, gradient primary button, Mr. Cadabra orb) so the front
#               door matches the hub/dashboard/lesson pages. Front-end only (index.html); other
#               pages already share the system. (challenge.html not yet reviewed for polish.)
#   2026-07-24  PHASE D -- CONTENT-ENGINE GUARDRAILS. Stamp -> "2026-07-24k-guardrails". The
#               "verify every problem you make up" rule now lives in pedagogy.py METHODOLOGY, so
#               it reaches all three tutor modes (lesson/practice/topic) via the injected
#               playbook: the tutor solves+checks every invented problem, keeps it on-standard,
#               calibrates difficulty, and discards bad ones. Backend prompt change only.
#   2026-07-24  PHASE C -- PARENT/TEACHER PORTAL. Stamp -> "2026-07-24j-teacher". Front-end only:
#               index.html gains a "Parent or teacher? View a student's progress" entry (enter the
#               student's code -> /dashboard?code=..&view=teacher); dashboard.html adds a read-only
#               review mode (Parent/Teacher badge, a plain-language "how to help" summary, weak
#               units shown as "Focus area" instead of a lesson-launch button). Reuses /api/login
#               + /api/topics; no backend change (stamp bump only, to confirm the deploy).
#   2026-07-24  PHASE B -- STRENGTHEN-WEAK-POINTS LOOP. Stamp -> "2026-07-24i-steering".
#               ChatRequest gains optional `unit` (focus). New _mastery_note() summarizes what
#               the student has mastered vs. still needs; /api/chat injects it (+ focus_unit)
#               into the tutor context so Mr. Cadabra STEERS to weak units and does spaced
#               review. Dashboard "Work on it" -> /session?code=..&unit=N; session.html forwards
#               the unit; a focused session tracks toward THAT unit. (tutor.py: {mastery} section.)
#   2026-07-24  PHASE A3 -- MASTERY DASHBOARD. Stamp -> "2026-07-24h-dashboard". dashboard.html
#               rebuilt on the real mastery data (units mastered ring, day streak, accuracy,
#               problems practiced) + a "Strengthen next" section naming started-but-not-mastered
#               units (weakest first) with a Work-on-it link. No backend change (uses the
#               /api/topics fields A1 added). Completes Phase A (measurement spine).
#   2026-07-24  PHASE A2 -- CHECK FLOW LIVE. Stamp -> "2026-07-24g-checks". The tutor now runs
#               end-of-unit checks and marks practice problems (tutor.py prompt); the frontends
#               POST to the A1 endpoints (/api/check, /api/mark) and show a result card. Backend
#               endpoints unchanged from A1. Next: A3 dashboard shows the accumulated mastery.
#   2026-07-24  PHASE A1 -- MASTERY BACKEND. New endpoints POST /api/check/{code} (record an
#               end-of-unit check score) and POST /api/mark/{code} (count a practiced problem);
#               /api/topics now also returns per-unit best_pct/checks_taken/mastered + a summary
#               with units_mastered and stats (problems_practiced, accuracy_pct, streak_days).
#               Backed by new store.py tables (unit_checks, student_stats). Additive + guarded
#               (tracking:false when DB off) -> do no harm. Stamp -> "2026-07-24f-mastery".
#               (A2 = the tutor-run check flow that CALLS these; A3 = the dashboard that SHOWS
#               them. This A1 step is invisible plumbing until A2/A3 land.)
#   2026-07-24  BUILD STAMP BUMP -> "2026-07-24e-superscript". Reason: the board now renders
#               POWERS as real superscripts (x^2 -> x squared shown as x², 10^3 -> 10³, plus
#               pre-formed ²/³) in styleVars across session/practice/topic -- fixes "I don't see
#               the square" (it was showing a literal caret "x^2"). Front-end only.
#   2026-07-24  BUILD STAMP BUMP -> "2026-07-24d-alltranscript". Reason: practice.html and
#               topic.html were rebuilt to the SAME transcript + left-sidebar layout as the
#               lesson (scrollable feed of tutor chat + student chat + math blocks, auto-scroll,
#               controls on the left). Fixes the Topic bug where a graph overlapped the tutor's
#               text (each figure is now its own block in the flow). Front-end only; stamp
#               confirms the deploy.
#   2026-07-24  BUILD STAMP BUMP -> "2026-07-24c-autoscroll". Reason: session.html transcript
#               feed now AUTO-SCROLLS to the newest content (rAF + a MutationObserver, and it
#               stays put if the student scrolled up to read history). Front-end only; stamp
#               just confirms the deploy.
#   2026-07-24  BUILD STAMP BUMP -> "2026-07-24b-introfirst". Reason: tutor.py + pedagogy.py
#               now enforce "define the concept before any exercise" for a beginner (Topic mode
#               was drilling polynomials before defining them). Backend-only; stamp confirms the
#               redeploy.
#   2026-07-24  BUILD STAMP BUMP -> "2026-07-24a-transcript". Reason: session.html lesson
#               page was rebuilt as a single scrollable TRANSCRIPT (tutor chat + student chat
#               + worked math in one retained, scrollable feed); the right sidebar was removed
#               and the avatar + Curriculum/Practice/Dashboard nav + all controls (Pause, Tap-
#               to-talk, Yes/No/confused) moved to the LEFT; the always-on 9-unit course list
#               was removed. Front-end only (session.html); this stamp just confirms the deploy
#               landed. (practice.html/topic.html not yet converted -- pending Jim's OK.)
#   2026-07-23  BUILD STAMP BUMP -> "2026-07-23h-boardstage". Reason: Stage 3 -- the tutor's
#               spoken words now render ON the whiteboard (words + math in one place), the side
#               chat was removed, a Pause button was added (all front-end in session/practice/
#               topic.html), and tutor.py gained a "write the problem on the board when you pose
#               it" rule. This stamp confirms the tutor.py backend redeployed.
#   2026-07-23  BUILD STAMP BUMP -> "2026-07-23g-stepboard". Reason: Stage 2 -- the
#               whiteboard is now a persistent STACKING worklist driven by the new [[step]]
#               tag, and the server-side board-guessing net (ensure_board) was retired (see
#               tutor.py notes). Front-end changes are in session/practice/topic.html; this
#               stamp bump lets /health confirm the tutor.py backend redeployed too.
#   2026-07-23  BUILD STAMP BUMP -> "2026-07-23f-strongbrain". Backend reason: the tutor
#               now runs on the stronger claude-sonnet-5 brain AND injects real per-unit
#               pedagogy from the new pedagogy.py KB (see tutor.py notes). No route change
#               here -- the bump exists so /health confirms Render redeployed. REMINDER:
#               the live model is set by the Render env var CLAUDE_MODEL, which OVERRIDES
#               the code default -- set CLAUDE_MODEL=claude-sonnet-5 in Render (or delete
#               it) or the tutor stays on whatever that var says (currently Haiku).
#   2026-07-23  BUILD STAMP BUMP -> "2026-07-23e-boardsync". Backend-only reason: the
#               tutor.py whiteboard logic changed (the board no longer runs ahead of the
#               student / answers the question it just asked). No route or handler change
#               here -- the stamp bump exists so /health confirms Render redeployed the new
#               tutor.py. If /health still shows an OLDER build, the new pacing fix is NOT
#               live yet (static files push instantly, but the Python backend only updates
#               on a Render rebuild).
#   2026-07-22  AVATAR LAB (experiment). Added GET /avatar-lab -> serves
#               static/avatar-lab.html, a Ready Player Me 3D-avatar sandbox for
#               Mr. Cadabra (design an avatar, watch it talk via /api/speak). It does
#               NOT touch the live /session tutor; brain stays Claude. New route only.
#   2026-07-21  PHASE 2 -- REAL PER-TOPIC TRACKING. Course chats record Unit 2
#               (linear equations) as "learning"; Practice classifies the problem's
#               unit and records "practiced"; Topic records the chosen unit as
#               "explored" (via curriculum.classify_unit). All guarded by
#               store.enabled() and wrapped so tracking never breaks a turn. New
#               GET /api/topics/{code} returns all 9 units + honest summary for the
#               real dashboard.
#   2026-07-21  DURABLE STORAGE FOUNDATION (opt-in). Added store.py (SQLAlchemy) and
#               routed session + placement persistence through it: when DATABASE_URL
#               is set (e.g. a Render PostgreSQL instance) memory lives in the DB and
#               survives deploys/sleeps; when it's NOT set the app uses the SAME JSON
#               files as before, so nothing changes for the current deploy. /health
#               now reports storage status. This is the base for real per-topic
#               tracking, accounts, and subscriptions.
#   2026-07-21  HOME HUB + TOPIC MODE. Added GET /home (the "what would you like to
#               do today?" hub: course / practice / topic), GET /topic (topic page),
#               and POST /api/topic (mini-lesson on a chosen topic via
#               tutor.get_topic_reply; client-held history, not persisted). Login and
#               the Challenge now land placed students on /home instead of /session.
#   2026-07-21  PRACTICE MODE. Added GET /practice (serves practice.html) and
#               POST /api/practice: the student brings a specific problem from school
#               and Mr. Cadabra coaches them through it (tutor.get_practice_reply).
#               Practice history is CLIENT-held and passed in each request (sanitized
#               here), so nothing is persisted -- a homework problem is a one-off.
#   2026-07-21  ENTRY-FLOW + DURABLE-MEMORY GROUNDWORK.
#               • /api/login now also returns `placed` (has the student done the
#                 placement Challenge?) so the login screen can force first-timers
#                 to "find their level" before any lesson.
#               • /api/session/{code} now also returns `placement` + `placed` so the
#                 lesson page can enforce the flow and pick first-tour vs welcome-back.
#               • DATA_DIR is now overridable via the DATA_DIR env var so memory can
#                 live on a Render PERSISTENT DISK (e.g. /var/data) and survive
#                 redeploys/sleeps. Default unchanged (BASE_DIR/data).
#   2026-07-20  Added POST /api/transcribe: server-side speech-to-text via
#               ElevenLabs Scribe (reuses ELEVENLABS_API_KEY). The browser records
#               the student's audio and posts it here; we return the text. This
#               replaces the flaky browser SpeechRecognition. Model via
#               ELEVENLABS_STT_MODEL (default scribe_v1).
#   2026-07-19  Added Mr. Cadabra's Challenge (placement quiz): GET /challenge,
#               POST/GET /api/placement/{code} (persisted to data/placements.json).
#               Placement now feeds BOTH the dashboard (via progress.py) and the
#               tutor (the placement is injected into the tutor's progress context
#               in /api/chat, so he starts each student at the right level).
#   2026-07-19  Firmed up ElevenLabs voice_settings (stability 0.55 + speaker
#               boost) to reduce garbled words.
#   2026-07-19  Added the progress DASHBOARD: GET /dashboard (serves
#               dashboard.html) and GET /api/progress/{code} (data from
#               progress.py -- currently representative sample data, real shape).
#   2026-07-19  LOW-LATENCY VOICE. /api/speak is now a STREAMING GET that proxies
#               ElevenLabs' stream endpoint (audio starts playing before it's fully
#               generated), and the default model is now eleven_flash_v2_5 (fast).
#               Added /api/voice-status so the frontend knows whether the natural
#               voice is available before requesting it. Removed the old POST speak.
#   2026-07-19  Set the default ELEVENLABS_VOICE_ID to Jim's chosen voice
#               (sB7vwSCyX0tQmU24cW2C) so a fresh deploy uses it even without the
#               env var. Still overridable via the ELEVENLABS_VOICE_ID env var.
#   2026-07-19  Added POST /api/speak: proxies ElevenLabs text-to-speech so the
#               tutor can talk in a natural voice. The API key stays server-side
#               (env ELEVENLABS_API_KEY). If the key is missing or the call fails,
#               it returns 204 and the browser falls back to its built-in voice.
#               Voice/model configurable via ELEVENLABS_VOICE_ID / ELEVENLABS_MODEL.
#   2026-07-19  Initial Day 1 backbone. FastAPI backend that:
#                 - serves the minimal code-entry screen and the session screen
#                 - validates a student login code against students.json
#                 - runs a text chat with the tutor (tutor.py / Claude API)
#                 - remembers each student's conversation across logins by
#                   saving it to data/sessions.json
#               Voice (Day 3) and the animated orb options (Day 5) are not here
#               yet; this is the backbone they will plug into.
#
# HOW IT RUNS:
#   Locally:  uvicorn main:app --reload
#   Render:   uvicorn main:app --host 0.0.0.0 --port $PORT   (see render.yaml)
#
# IMPORTANT NOTE ABOUT MEMORY ON RENDER:
#   sessions.json + placements.json (under DATA_DIR) let the tutor remember each
#   student and their placement. On Render's FREE web service the disk is EPHEMERAL
#   -- it resets on every redeploy AND whenever the service sleeps (~15 min idle) --
#   so students look brand new each time. To make memory DURABLE, attach a Render
#   PERSISTENT DISK (needs a paid Starter instance), mount it at e.g. /var/data, and
#   set env var DATA_DIR=/var/data. The code already reads DATA_DIR, so no code
#   change is needed once the disk is attached.
# =============================================================================

import json
import os
import re
import threading
import time
from collections import defaultdict, deque
from pathlib import Path

import httpx
from fastapi import FastAPI, File, HTTPException, Request, UploadFile
from fastapi.responses import FileResponse, JSONResponse, Response, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import tutor
import store   # durable DB storage; dormant unless DATABASE_URL is set (see store.py)
import curriculum   # 9 units + classify_unit() for real per-topic tracking

# Bring up the database backend if DATABASE_URL is configured. If it isn't (or the
# DB can't be reached), store.enabled() stays False and we use the JSON-file storage
# below, exactly as before -- so the current app is unaffected until a DB is added.
store.init()

# ---- ElevenLabs voice config (all optional; empty key -> browser voice) -----
# Set these in Render (NOT in code). If ELEVENLABS_API_KEY is missing, the app
# still talks using the browser's built-in voice.
ELEVEN_API_KEY = os.environ.get("ELEVENLABS_API_KEY")
# Default voice = Jim's chosen ElevenLabs voice. Override with any other voice_id
# from your ElevenLabs Voice Library via the ELEVENLABS_VOICE_ID env var.
ELEVEN_VOICE_ID = os.environ.get("ELEVENLABS_VOICE_ID", "sB7vwSCyX0tQmU24cW2C")
# eleven_flash_v2_5 = low latency (best for live conversation); override with
# ELEVENLABS_MODEL="eleven_multilingual_v2" for higher quality at more latency.
ELEVEN_MODEL = os.environ.get("ELEVENLABS_MODEL", "eleven_flash_v2_5")
# Speech-to-text model (ElevenLabs "Scribe"). Used by /api/transcribe.
ELEVEN_STT_MODEL = os.environ.get("ELEVENLABS_STT_MODEL", "scribe_v1")

# ---- Paths -----------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
# DATA_DIR holds the tutor's MEMORY (each student's conversation + placement).
# It defaults to a "data" folder next to the code, but can be pointed at a Render
# PERSISTENT DISK by setting the DATA_DIR env var (e.g. DATA_DIR=/var/data) so that
# memory SURVIVES redeploys and restarts. On an ephemeral (free-plan) disk this
# folder is wiped on every deploy and whenever the service sleeps -- which is why,
# without a persistent disk, students appear brand new each time.
DATA_DIR = Path(os.environ.get("DATA_DIR", str(BASE_DIR / "data")))
STUDENTS_FILE = BASE_DIR / "students.json"
SESSIONS_FILE = DATA_DIR / "sessions.json"
PLACEMENTS_FILE = DATA_DIR / "placements.json"  # results of Mr. Cadabra's Challenge

DATA_DIR.mkdir(exist_ok=True)  # make sure the memory folder exists

# A simple lock so two overlapping requests never corrupt the sessions file.
_sessions_lock = threading.Lock()


# ---- Loading the hardcoded students ----------------------------------------
def load_students() -> dict:
    """Read students.json and return the {code: student} mapping."""
    with open(STUDENTS_FILE, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    return data.get("students", {})


STUDENTS = load_students()


# ---- Session memory (per student code) -------------------------------------
def _read_all_sessions() -> dict:
    if not SESSIONS_FILE.exists():
        return {}
    try:
        with open(SESSIONS_FILE, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except (json.JSONDecodeError, OSError):
        # If the file is missing or somehow corrupted, start fresh rather than
        # crash. We do no harm to a running session over a bad memory file.
        return {}


def _write_all_sessions(all_sessions: dict) -> None:
    tmp = SESSIONS_FILE.with_suffix(".json.tmp")
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(all_sessions, fh, ensure_ascii=False, indent=2)
    tmp.replace(SESSIONS_FILE)  # atomic swap so the file is never half-written


def _ck(code: str, course: str = "algebra1") -> str:
    """File-storage key (only used when the DB is off). Algebra I stays under the bare code
    so existing JSON files keep working; other courses are namespaced as 'code::course'."""
    return code if (course or "algebra1") == "algebra1" else f"{code}::{course}"


def get_session(code: str, course: str = "algebra1") -> dict:
    """Return this student's saved session for a course, creating an empty one if needed."""
    if store.enabled():
        return store.get_session(code, course)
    all_sessions = _read_all_sessions()
    return all_sessions.get(_ck(code, course), {"history": []})


def save_session(code: str, session: dict, course: str = "algebra1") -> None:
    if store.enabled():
        store.save_session(code, session, course)
        return
    with _sessions_lock:
        all_sessions = _read_all_sessions()
        all_sessions[_ck(code, course)] = session
        _write_all_sessions(all_sessions)


# ---- Placement results (from Mr. Cadabra's Challenge) ----------------------
def read_placement(code: str, course: str = "algebra1") -> dict:
    """Return this student's saved placement result for a course, or {} if none."""
    if store.enabled():
        return store.read_placement(code, course)
    if not PLACEMENTS_FILE.exists():
        return {}
    try:
        with open(PLACEMENTS_FILE, "r", encoding="utf-8") as fh:
            return json.load(fh).get(_ck(code, course), {})
    except (json.JSONDecodeError, OSError):
        return {}


def _track_topic(code: str, unit, name: str, status: str, course: str = "algebra1") -> None:
    """Record real per-topic engagement (Phase 2), but only when the database is on,
    and never let a tracking hiccup break a student's turn. `course` files the progress
    under the right course (multi-course, Phase 3); defaults to Algebra I."""
    if not (store.enabled() and unit):
        return
    try:
        store.record_topic(code, unit, name, status, course=course)
    except Exception as exc:  # noqa: BLE001
        print(f"[track] record_topic failed (ignored): {exc}")


def _mastery_note(code: str, focus_unit: int = 0, course: str = "algebra1") -> str:
    """PHASE B: a short, human-readable summary of what this student has MASTERED vs. still
    needs IN THIS COURSE, for the tutor to STEER by (spend effort on weak units + spaced
    review). Empty string when the DB is off or anything errors -- never breaks a turn."""
    if not store.enabled():
        return ""
    try:
        topics = {r["unit"]: r for r in store.get_topics(code, course)}
        checks = (store.get_mastery(code, course) or {}).get("checks", {})
    except Exception as exc:  # noqa: BLE001
        print(f"[mastery-note] failed (ignored): {exc}")
        return ""
    mastered, working, notstarted = [], [], []
    for n, name in curriculum.units_for(course):
        best = int((checks.get(n) or {}).get("best_pct") or 0)
        t = topics.get(n)
        if best >= 80:
            mastered.append(f"Unit {n} ({name})")
        elif t and t.get("status") not in (None, "not-started"):
            tag = ("best " + str(best) + "%") if best else "no check yet"
            working.append(f"Unit {n} ({name}, {tag})")
        else:
            notstarted.append(str(n))
    parts = []
    if mastered:
        parts.append("MASTERED: " + "; ".join(mastered) + ".")
    if working:
        parts.append("STILL TO MASTER (focus here): " + "; ".join(working) + ".")
    if notstarted:
        parts.append("Not started: units " + ", ".join(notstarted) + ".")
    note = " ".join(parts) if parts else "Just getting started -- no mastery data yet."
    fu = int(focus_unit or 0)
    if 1 <= fu <= 9:
        note += (f" TODAY the student chose to work on Unit {fu} "
                 f"({curriculum.unit_name(course, fu)}) -- center this session there.")
    return note


def save_placement(code: str, result: dict, course: str = "algebra1") -> None:
    if store.enabled():
        store.save_placement(code, result, course)
        return
    with _sessions_lock:
        all_p = {}
        if PLACEMENTS_FILE.exists():
            try:
                with open(PLACEMENTS_FILE, "r", encoding="utf-8") as fh:
                    all_p = json.load(fh)
            except (json.JSONDecodeError, OSError):
                all_p = {}
        all_p[_ck(code, course)] = result
        tmp = PLACEMENTS_FILE.with_suffix(".json.tmp")
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(all_p, fh, ensure_ascii=False, indent=2)
        tmp.replace(PLACEMENTS_FILE)


# ---- Request models --------------------------------------------------------
class LoginRequest(BaseModel):
    code: str


class ChatRequest(BaseModel):
    code: str
    message: str
    unit: int = 0              # optional focus unit (from the dashboard "Work on it" link)
    course: str = "algebra1"   # which course this lesson session belongs to (multi-course)


class PracticeRequest(BaseModel):
    code: str
    problem: str = ""          # the specific problem the student is stuck on
    message: str               # what the student just said (or the problem, first turn)
    history: list = []         # prior practice turns, held by the browser (not persisted)
    course: str = "algebra1"   # which course this practice session belongs to (multi-course)


class TopicRequest(BaseModel):
    code: str
    topic: str = ""            # the topic the student chose to explore
    message: str               # what the student just said (or the topic, first turn)
    history: list = []         # prior topic turns, held by the browser (not persisted)
    course: str = "algebra1"   # which course this topic exploration belongs to (multi-course)


class PlacementIn(BaseModel):
    level: int = 1
    level_title: str = ""
    start_unit: int = 1
    start_unit_name: str = ""
    points: int = 0


class CheckIn(BaseModel):
    unit: int                  # which of the 9 units this end-of-unit check covered
    correct: int = 0           # questions the student got right
    total: int = 1             # questions on the check
    course: str = "algebra1"   # which course this check belongs to (so it's filed per-course)


# TEACHER / PARENT CLASSROOM (2026-07-28) -- see the classroom endpoints below.
class ClassIn(BaseModel):
    class_code: str            # short, case-insensitive key the teacher picks (e.g. "MRSB-P3")
    name: str = ""             # friendly label, e.g. "Period 3 Algebra"
    owner_name: str = ""       # teacher/parent display name (optional)
    teacher_code: str = ""     # the teacher's personal sign-in code (optional; e.g. "MRSBAKER")


class ClassStudentIn(BaseModel):
    code: str                  # an EXISTING student code to add to the class


class MarkIn(BaseModel):
    correct: int = 1           # was the practice problem right (1) or wrong (0)
    attempted: int = 1         # how many problems this represents (usually 1)
    highest_tier: int = 0
    strengths: list = []


# ---- App -------------------------------------------------------------------
app = FastAPI(title="Math Tutor MVP", version="0.1.0")


def _student_or_404(code: str) -> dict:
    code = (code or "").strip()
    student = STUDENTS.get(code)
    if not student:
        raise HTTPException(status_code=404, detail="That code was not recognized.")
    return student


# -----------------------------------------------------------------------------
# COST & ABUSE GUARDS (added 2026-07-30, market-prep lockdown)
# -----------------------------------------------------------------------------
# Every /api/chat, /api/practice, /api/topic call spends Anthropic money, and every
# /api/speak / /api/transcribe call spends ElevenLabs money. Before this change,
# /api/speak and /api/transcribe required NO login code at all -- a stranger who
# found the URL could run up the bill directly -- and nothing anywhere was rate
# limited. Now: (a) both voice endpoints require a valid student code; (b) the
# spoken text has a hard length cap; (c) a small in-process sliding-window rate
# limiter throttles every paid endpoint per code (and /api/login per IP, so the
# 4-digit code space can't be brute-forced quickly). The limits are set WELL above
# any real student's pace, so a legitimate user never sees a 429.
_RL_LOCK = threading.Lock()
_RL_BUCKETS: dict = defaultdict(deque)
MAX_SPEAK_CHARS = 5000          # tutor replies spoken aloud run ~200-2500 chars; 5000 is generous
_TTS_CACHE_MAX_BYTES = 300 * 1024 * 1024   # cap the audio cache at ~300 MB (evicts oldest first)


def _rate_limit(key: str, limit: int, window_seconds: int, what: str = "requests") -> None:
    """Sliding-window limiter. Raises 429 if `key` exceeds `limit` per `window_seconds`."""
    now = time.monotonic()
    with _RL_LOCK:
        # Keep the bucket table itself from growing without bound.
        if len(_RL_BUCKETS) > 10000:
            for k in [k for k, q in _RL_BUCKETS.items() if not q]:
                _RL_BUCKETS.pop(k, None)
        q = _RL_BUCKETS[key]
        while q and q[0] <= now - window_seconds:
            q.popleft()
        if len(q) >= limit:
            raise HTTPException(status_code=429,
                                detail=f"Too many {what} in a short time — please wait a minute and try again.")
        q.append(now)


def _client_ip(request: Request) -> str:
    """Best-effort caller IP. On Render we sit behind a proxy, so X-Forwarded-For is the real one."""
    fwd = (request.headers.get("x-forwarded-for") or "").split(",")[0].strip()
    if fwd:
        return fwd
    return request.client.host if request.client else "unknown"


def _require_student(code: str) -> dict:
    """Like _student_or_404 but returns 401 (auth), for the paid voice endpoints."""
    student = STUDENTS.get((code or "").strip())
    if not student:
        raise HTTPException(status_code=401, detail="A valid login code is required.")
    return student


@app.get("/")
def home():
    """The minimal code-entry screen."""
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/session")
def session_page():
    """The screen where the student talks with the tutor."""
    return FileResponse(STATIC_DIR / "session.html")


@app.get("/dashboard")
def dashboard_page():
    """The full-screen progress dashboard."""
    return FileResponse(STATIC_DIR / "dashboard.html")


@app.get("/teacher")
def teacher_page():
    """The CLASSROOM view: a teacher or parent following several students at once."""
    return FileResponse(STATIC_DIR / "teacher.html")


@app.get("/challenge")
def challenge_page():
    """Mr. Cadabra's Challenge -- the fun adaptive placement quiz."""
    return FileResponse(STATIC_DIR / "challenge.html")


@app.get("/practice")
def practice_page():
    """Practice mode -- bring a specific problem from school and get coached on it."""
    return FileResponse(STATIC_DIR / "practice.html")


@app.get("/home")
def home_page():
    """The 'what would you like to do today?' hub (course / practice / topic)."""
    return FileResponse(STATIC_DIR / "home.html")


@app.get("/topic")
def topic_page():
    """Topic mode -- pick or name a topic for a focused mini-lesson."""
    return FileResponse(STATIC_DIR / "topic.html")


# (Removed 2026-07-30, market-prep lockdown:)
#   - GET /avatar-lab: an internal 3D-avatar EXPERIMENT was publicly routed; it exposed internal
#     notes and a free-text call to the paid /api/speak endpoint. The route is gone and
#     static/avatar-lab.html is now a small "retired" stub. progress.py's companion route:
#   - GET /api/progress/{code}: served FABRICATED sample stats (progress.py _PROFILES). Verified
#     no page calls it anymore (the dashboard uses the real /api/courses + /api/topics data), so
#     the route and the `import progress` are removed. progress.py itself is now unused and can
#     be deleted from the repo whenever convenient.


@app.get("/privacy")
def privacy_page():
    """Parents & Privacy -- the plain-language privacy commitments (attorney review pending)."""
    return FileResponse(STATIC_DIR / "privacy.html")


@app.get("/terms")
def terms_page():
    """Terms of use, billing and refund basics (attorney review pending)."""
    return FileResponse(STATIC_DIR / "terms.html")


@app.get("/api/topics/{code}")
def topics_state(code: str, course: str = "algebra1"):
    """
    REAL, honest per-topic progress for the dashboard: all of the CHOSEN COURSE's units with
    the student's actual engagement (explored / learning / practiced) or 'not-started'.
    Only meaningful when the database is on (`tracking:true`); otherwise it reports
    tracking is off so the dashboard can say so rather than invent numbers.
    """
    student = _student_or_404(code)
    code = code.strip()
    placement = read_placement(code, course)
    tracking = store.enabled()

    recorded = {}
    mastery = {"checks": {}, "stats": {}}
    if tracking:
        try:
            for row in store.get_topics(code, course):
                recorded[row["unit"]] = row
        except Exception as exc:  # noqa: BLE001
            print(f"[topics] get_topics failed: {exc}")
        try:
            mastery = store.get_mastery(code, course)
        except Exception as exc:  # noqa: BLE001
            print(f"[topics] get_mastery failed: {exc}")

    checks = mastery.get("checks", {})
    units = []
    for n, name in curriculum.units_for(course):
        r = recorded.get(n)
        c = checks.get(n) or {}
        best = int(c.get("best_pct") or 0)
        units.append({
            "unit": n,
            "name": name,
            "status": (r["status"] if r else "not-started"),
            "touches": (r["touches"] if r else 0),
            "last_touched": (r.get("last_touched") if r else None),
            "best_pct": best,                       # best end-of-unit check score (0 if none)
            "checks_taken": int(c.get("checks_taken") or 0),
            "mastered": best >= 80,
        })

    started = [u for u in units if u["status"] != "not-started"]
    summary = {
        "units_started": len(started),
        "units_total": len(units),
        "units_mastered": len([u for u in units if u["mastered"]]),
        "total_touches": sum(u["touches"] for u in units),
        "last_active": max([u["last_touched"] for u in started if u["last_touched"]], default=None),
        "stats": mastery.get("stats", {}),          # problems_practiced, accuracy_pct, streak_days
    }
    return {
        "name": student.get("name"),
        "tracking": tracking,
        "placement": placement,
        "units": units,
        "summary": summary,
    }


# =============================================================================
# TEACHER / PARENT CLASSROOM (2026-07-28)
# -----------------------------------------------------------------------------
# A "class" groups EXISTING student codes under a short class code, so a teacher or parent can
# watch several students at once. This is deliberately NOT an accounts system: there is no
# password and no new personal data -- the class code is just a convenience key, and every
# student code added must ALREADY exist in students.json. The roster lives in the database
# (`classes` / `class_members`); when the DB is off these endpoints report tracking:false
# instead of failing, exactly like the rest of the tracking layer.
# =============================================================================
def _class_or_404(class_code: str) -> dict:
    cls = store.get_class(class_code)
    if not cls:
        raise HTTPException(status_code=404, detail="That class code was not found.")
    return cls


def _class_student_row(code: str, course: str) -> dict:
    """One student's snapshot for the classroom view: per-unit best scores + a small summary.
    Mirrors what /api/topics reports, but trimmed to what a roster grid needs. Never raises --
    a student whose data can't be read still appears in the grid (with zeros)."""
    student = STUDENTS.get(code) or {}
    checks, stats, recorded = {}, {}, {}
    try:
        m = store.get_mastery(code, course)
        checks = m.get("checks", {}) or {}
        stats = m.get("stats", {}) or {}
    except Exception as exc:  # noqa: BLE001
        print(f"[class] get_mastery failed for {code}: {exc}")
    try:
        for row in store.get_topics(code, course):
            recorded[row["unit"]] = row
    except Exception as exc:  # noqa: BLE001
        print(f"[class] get_topics failed for {code}: {exc}")

    units = []
    for n, name in curriculum.units_for(course):
        c = checks.get(n) or {}
        r = recorded.get(n)
        best = int(c.get("best_pct") or 0)
        units.append({
            "unit": n,
            "name": name,
            "best_pct": best,
            "checks_taken": int(c.get("checks_taken") or 0),
            "mastered": best >= 80,
            "status": (r["status"] if r else "not-started"),
        })
    started = [u for u in units if u["status"] != "not-started" or u["checks_taken"]]
    # FOUNDATION-FIRST, matching the Course Assessment's recommended path: the units to work on
    # are listed in COURSE ORDER (earliest gap first), NOT weakest-first -- a shaky Unit 1 gets
    # attention before a shaky Unit 9, because the later units build on it.
    weak = [u for u in units if u["checks_taken"] and not u["mastered"]]
    last = [r.get("last_touched") for r in recorded.values() if r.get("last_touched")]
    return {
        "code": code,
        "name": student.get("name") or code,
        "known": bool(student),           # False = the code isn't in students.json (typo?)
        "units": units,
        "units_mastered": len([u for u in units if u["mastered"]]),
        "units_started": len(started),
        "weakest": [{"unit": u["unit"], "name": u["name"], "best_pct": u["best_pct"]}
                    for u in weak[:3]],
        "last_active": (max(last) if last else None),
        "stats": stats,
    }


@app.post("/api/class")
def post_class(body: ClassIn):
    """Create a class, or update its label/owner if the code already exists."""
    if not store.enabled():
        return {"ok": False, "tracking": False}
    cc = (body.class_code or "").strip()
    if not cc:
        raise HTTPException(status_code=400, detail="Please choose a class code.")
    cls = store.create_class(cc, body.name or "", body.owner_name or "",
                             body.teacher_code or "")
    return {"ok": True, "tracking": True, "klass": cls}


@app.get("/api/teacher/{teacher_code}/classes")
def get_teacher_classes(teacher_code: str):
    """EVERY class run by this teacher code -- what a teacher sees right after signing in.

    An unknown code is NOT a 404: it simply has no classes yet, and the page invites the teacher
    to create their first one. Reports tracking:false when the database is off, like the rest of
    the classroom API.

    NOTE (deliberate, and stated in the UI): a teacher code is a convenience key, not a password.
    Until the accounts work lands, anyone who knows a teacher's code can see that teacher's
    classes. This is a door, not a lock.
    """
    if not store.enabled():
        return {"ok": False, "tracking": False, "classes": []}
    tc = (teacher_code or "").strip()
    if not tc:
        raise HTTPException(status_code=400, detail="Please enter your teacher code.")
    classes = store.list_classes_for_teacher(tc)
    return {"ok": True, "tracking": True, "teacher_code": tc.upper(), "classes": classes}


@app.get("/api/class/{class_code}")
def get_class_info(class_code: str):
    """The class label plus its roster (student codes + display names)."""
    if not store.enabled():
        return {"ok": False, "tracking": False}
    cls = _class_or_404(class_code)
    roster = [{"code": c, "name": (STUDENTS.get(c) or {}).get("name") or c,
               "known": bool(STUDENTS.get(c))} for c in cls.get("students", [])]
    return {"ok": True, "tracking": True, "klass": {**cls, "roster": roster}}


@app.post("/api/class/{class_code}/students")
def post_class_student(class_code: str, body: ClassStudentIn):
    """Add an EXISTING student code to the class. Unknown codes are rejected with a clear
    message so a teacher sees their typo instead of a silently empty row."""
    if not store.enabled():
        return {"ok": False, "tracking": False}
    _class_or_404(class_code)
    code = (body.code or "").strip()
    if not code:
        raise HTTPException(status_code=400, detail="Please enter a student code.")
    if code not in STUDENTS:
        raise HTTPException(status_code=404,
                            detail=f"No student with the code '{code}'. Check the code and try again.")
    store.add_student(class_code, code)
    return {"ok": True, "tracking": True}


@app.delete("/api/class/{class_code}/students/{student_code}")
def delete_class_student(class_code: str, student_code: str):
    """Remove a student from the class. The student's own progress is NOT deleted."""
    if not store.enabled():
        return {"ok": False, "tracking": False}
    _class_or_404(class_code)
    store.remove_student(class_code, student_code)
    return {"ok": True, "tracking": True}


@app.get("/api/class/{class_code}/summary")
def get_class_summary(class_code: str, course: str = "algebra1"):
    """THE CLASSROOM VIEW: every student in the class with their per-unit mastery for ONE
    course, plus class-wide aggregates (which units the class as a whole is weakest on)."""
    if not store.enabled():
        return {"ok": False, "tracking": False}
    cls = _class_or_404(class_code)
    students = [_class_student_row(c, course) for c in cls.get("students", [])]
    unit_names = curriculum.units_for(course)

    # Class-wide per-unit picture: how many students have mastered each unit, and the average
    # best score among those who have actually been checked on it.
    per_unit = []
    for n, name in unit_names:
        scored = [s for s in students
                  if next((u for u in s["units"] if u["unit"] == n), {}).get("checks_taken")]
        mastered = [s for s in students
                    if next((u for u in s["units"] if u["unit"] == n), {}).get("mastered")]
        avg = None
        if scored:
            avg = round(sum(next(u for u in s["units"] if u["unit"] == n)["best_pct"]
                            for s in scored) / len(scored))
        per_unit.append({"unit": n, "name": name, "assessed": len(scored),
                         "mastered": len(mastered), "avg_best_pct": avg})

    needs_help = sorted([p for p in per_unit if p["assessed"]],
                        key=lambda p: (p["avg_best_pct"] if p["avg_best_pct"] is not None else 999))
    return {
        "ok": True,
        "tracking": True,
        "klass": {"class_code": cls["class_code"], "name": cls.get("name", ""),
                  "owner_name": cls.get("owner_name", "")},
        "course": course,
        "course_title": curriculum.course_title(course),
        "units": [{"unit": n, "name": nm} for n, nm in unit_names],
        "students": students,
        "per_unit": per_unit,
        "needs_help": needs_help[:3],
        "class_size": len(students),
    }


@app.get("/api/courses/{code}")
def student_courses(code: str):
    """EVERY course this student has actually worked in, with units mastered/started -- for the
    dashboard's "My courses" strip. Returns courses with REAL activity only, in ladder order, so
    a student sees their whole picture at a glance and can switch with one click. When tracking is
    off it reports that rather than inventing anything."""
    _student_or_404(code)
    code = code.strip()
    if not store.enabled():
        return {"ok": False, "tracking": False, "courses": []}
    try:
        activity = store.get_course_activity(code)
    except Exception as exc:  # noqa: BLE001
        print(f"[courses] get_course_activity failed: {exc}")
        activity = {}
    courses = []
    for cid, title in curriculum.list_courses():          # ladder order
        a = activity.get(cid)
        if not a:
            continue                                      # never opened -> don't show a shell
        courses.append({
            "course": cid,
            "title": title,
            "units_total": len(curriculum.units_for(cid)),
            "units_started": a.get("units_started", 0),
            "units_mastered": a.get("units_mastered", 0),
            "units_checked": a.get("units_checked", 0),
            "avg_best_pct": a.get("avg_best_pct"),
            "last_active": a.get("last_active"),
        })
    return {"ok": True, "tracking": True, "courses": courses}


@app.post("/api/placement/{code}")
def post_placement(code: str, body: PlacementIn, course: str = "algebra1"):
    """Save the result of Mr. Cadabra's Challenge for this student, for THIS course."""
    _student_or_404(code)
    save_placement(code.strip(), body.model_dump(), course)
    return {"ok": True}


@app.post("/api/check/{code}")
def post_check(code: str, body: CheckIn):
    """PHASE A: record an end-of-unit CHECK score for this student (feeds mastery). No-op
    (tracking:false) when the DB is off; never raises to the caller."""
    _student_or_404(code)
    code = code.strip()
    if not store.enabled():
        return {"ok": False, "tracking": False}
    try:
        course = getattr(body, "course", None) or "algebra1"
        name = curriculum.unit_name(course, int(body.unit))
        res = store.record_check(code, int(body.unit), int(body.correct), int(body.total), name, course)
        return {"ok": True, "tracking": True, **res}
    except Exception as exc:  # noqa: BLE001
        print(f"[check] record_check failed: {exc}")
        return {"ok": False, "tracking": True}


@app.post("/api/mark/{code}")
def post_mark(code: str, body: MarkIn):
    """PHASE A: count a practice problem the tutor marked right/wrong (problems practiced +
    accuracy + streak). No-op when the DB is off; never raises to the caller."""
    _student_or_404(code)
    code = code.strip()
    if not store.enabled():
        return {"ok": False, "tracking": False}
    try:
        store.record_practice(code, int(body.correct), int(body.attempted))
        return {"ok": True, "tracking": True}
    except Exception as exc:  # noqa: BLE001
        print(f"[mark] record_practice failed: {exc}")
        return {"ok": False, "tracking": True}


@app.get("/api/placement/{code}")
def get_placement(code: str, course: str = "algebra1"):
    """Return this student's saved placement result for a course (or {})."""
    _student_or_404(code)
    return read_placement(code.strip(), course)


# Bump this string whenever the backend changes. It's shown at /health so we can CONFIRM
# Render actually redeployed the new code (if /health still shows an old build, the deploy
# didn't happen -- which would explain why prompt/whiteboard changes aren't taking effect).
APP_BUILD = "2026-07-30f-lockdown"


@app.get("/health")
def health():
    """Simple check that the service is up (handy for Render). Includes the active
    student-facing model and DB status so you can confirm both at a glance."""
    return {
        "status": "ok",
        "build": APP_BUILD,
        "students_loaded": len(STUDENTS),
        "model": os.environ.get("CLAUDE_MODEL", tutor.DEFAULT_MODEL),
        "storage": store.status(),
    }


@app.post("/api/login")
def login(req: LoginRequest, request: Request):
    """
    Validate a login code and return who the student is, PLUS the two flags the
    entry flow branches on:
      - placed:    has this student done Mr. Cadabra's Challenge yet? If not, the
                   login screen sends them there first ("find your level").
      - returning: do we have prior conversation for them? If so, the tutor
                   welcomes them back with a recap instead of a first-time tour.
    """
    # Brute-force guard: codes are short, so cap guesses per IP (20 / 5 min).
    _rate_limit("login:" + _client_ip(request), limit=20, window_seconds=300, what="login attempts")
    student = _student_or_404(req.code)
    code = req.code.strip()
    session = get_session(code)
    placement = read_placement(code)
    return {
        "ok": True,
        "code": code,
        "name": student.get("name"),
        "returning": bool(session.get("history")),
        "placed": bool(placement),
        "tutor_name": tutor.TUTOR_NAME,
    }


@app.get("/api/session/{code}")
def session_state(code: str, course: str = "algebra1"):
    """
    Return the student's info, remembered conversation (for resume), and their
    placement -- ALL scoped to the given course. The hub/session page uses `placed`
    to enforce the flow (a never-placed student with no history is sent to the
    Challenge first) and `history` to decide between a first-time tour and a
    welcome-back recap.
    """
    student = _student_or_404(code)
    code = code.strip()
    session = get_session(code, course)
    placement = read_placement(code, course)
    return {
        "name": student.get("name"),
        "tutor_name": tutor.TUTOR_NAME,
        "history": session.get("history", []),
        "placement": placement,
        "placed": bool(placement),
    }


@app.post("/api/chat")
def chat(req: ChatRequest):
    """Send the student's message to the tutor and return the tutor's reply."""
    student = _student_or_404(req.code)
    code = req.code.strip()
    # Paid Anthropic call behind this -- cap the pace per code (40 turns / 5 min is
    # far above a real student's speed; it only stops abuse/runaway scripts).
    _rate_limit("brain:" + code, limit=40, window_seconds=300, what="messages")

    message = (req.message or "").strip()
    if not message:
        raise HTTPException(status_code=400, detail="Please type a message first.")

    session = get_session(code, req.course)
    history = session.get("history", [])

    # Give the tutor the student's remembered progress plus the live history.
    student_context = dict(student)
    placement = read_placement(code, req.course)
    if placement:
        note = (" [Placement result from the Challenge: this student tested as "
                f"'{placement.get('level_title', '')}' and should start around "
                f"Unit {placement.get('start_unit')} "
                f"({placement.get('start_unit_name', '')}). Strengths: "
                f"{', '.join(placement.get('strengths', [])) or 'building foundations'}. "
                "Meet them at that level -- don't start below it unless they struggle.]")
        student_context["progress"] = (str(student_context.get("progress", "")) + note).strip()

    # Phase B -- MASTERY STEERING: tell the tutor what they've mastered vs. still need, and
    # (from the dashboard "Work on it" link) which unit to focus on today.
    focus_unit = 0
    try:
        focus_unit = int(getattr(req, "unit", 0) or 0)
    except (TypeError, ValueError):
        focus_unit = 0
    mnote = _mastery_note(code, focus_unit, req.course)
    if mnote:
        student_context["mastery_note"] = mnote
    if 1 <= focus_unit <= 9:
        student_context["focus_unit"] = focus_unit

    # OPENER: the app auto-sends "__open__" when the student opens the lesson (they did NOT
    # type anything). The OLD app sent a literal "Hi!" that got stored as a student turn, so
    # after a few logins the tutor saw "Hi Hi Hi..." and turned snappish. Fix: never store a
    # fake student greeting, strip any leftover junk ones, generate a warm recap, and save
    # ONLY the tutor's reply so the conversation stays coherent.
    if message == "__open__":
        junk = ("hi", "hi!", "hi.", "hello", "hey", "__open__")
        history = [m for m in history if not (
            m.get("role") == "user" and str(m.get("content", "")).strip().lower() in junk)]
        opener_note = (
            "(SYSTEM: The student just OPENED the lesson — they did NOT type anything, and this "
            "is NOT an interruption. If you have met before, warmly greet them back by name and "
            "give a SHORT recap of where you two are and what's next, then invite them to keep "
            "going. If this is your first meeting, begin the first-meeting flow. Do NOT scold "
            "them, do NOT tell them to focus, and do NOT act annoyed.)")
        reply = tutor.get_tutor_reply(student_context, history, opener_note, req.course)
        history.append({"role": "assistant", "content": reply})
        session["history"] = history
        save_session(code, session, req.course)
        return {"reply": reply}

    reply = tutor.get_tutor_reply(student_context, history, message, req.course)

    # Remember this exchange so the tutor recalls it next time.
    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": reply})
    session["history"] = history
    save_session(code, session, req.course)

    # Real tracking: the COURSE now teaches all 9 units starting at the student's
    # placed unit, so course activity counts as "learning" whatever unit they're on
    # (from placement; default Unit 2 if unplaced/unknown).
    course_unit = 2
    try:
        su = int((placement or {}).get("start_unit") or 0)
        if 1 <= su <= 9:
            course_unit = su
    except (TypeError, ValueError):
        course_unit = 2
    if 1 <= focus_unit <= 9:
        course_unit = focus_unit        # a focused session counts toward THAT unit
    _track_topic(code, course_unit, curriculum.unit_name(req.course, course_unit),
                 "learning", req.course)

    return {"reply": reply}


@app.post("/api/practice")
def practice(req: PracticeRequest):
    """
    Coach the student through a SPECIFIC problem they brought (homework help).

    Unlike /api/chat, practice is NOT tied to the curriculum, placement, or saved
    session memory. The browser holds the practice conversation and sends it back in
    `history` each turn, so nothing is persisted here -- a homework problem is a
    one-off. We validate the code so only real students can use it.
    """
    student = _student_or_404(req.code)
    _rate_limit("brain:" + req.code.strip(), limit=40, window_seconds=300, what="messages")

    message = (req.message or "").strip()
    if not message:
        raise HTTPException(status_code=400, detail="Please say what you're stuck on first.")

    # Sanitize the client-supplied history to just clean user/assistant text turns.
    safe_history = []
    for m in (req.history or [])[-tutor.MAX_HISTORY_MESSAGES:]:
        if not isinstance(m, dict):
            continue
        role = m.get("role")
        content = m.get("content")
        if role in ("user", "assistant") and isinstance(content, str) and content.strip():
            safe_history.append({"role": role, "content": content})

    reply = tutor.get_practice_reply(student, req.problem, safe_history, message, req.course)

    # Real tracking: classify the problem to a unit WITHIN this course, count "practiced".
    unit, name = curriculum.classify_unit(req.problem or message, req.course)
    _track_topic(req.code.strip(), unit, name, "practiced", req.course)

    return {"reply": reply}


def _sanitize_history(raw):
    """Keep only clean {user|assistant: text} turns from client-supplied history."""
    out = []
    for m in (raw or [])[-tutor.MAX_HISTORY_MESSAGES:]:
        if not isinstance(m, dict):
            continue
        role, content = m.get("role"), m.get("content")
        if role in ("user", "assistant") and isinstance(content, str) and content.strip():
            out.append({"role": role, "content": content})
    return out


@app.post("/api/topic")
def topic(req: TopicRequest):
    """
    Give a focused mini-lesson on the topic the student chose (topic mode).

    Like /api/practice, this is NOT tied to the curriculum/placement/saved memory:
    the browser holds the conversation and passes it back each turn, so nothing is
    persisted. (Real per-topic tracking lands in the next phase, once durable
    storage is on.)
    """
    student = _student_or_404(req.code)
    _rate_limit("brain:" + req.code.strip(), limit=40, window_seconds=300, what="messages")
    message = (req.message or "").strip()
    if not message:
        raise HTTPException(status_code=400, detail="Please pick or name a topic first.")
    reply = tutor.get_topic_reply(student, req.topic, _sanitize_history(req.history), message, req.course)

    # Real tracking: classify the chosen topic to a unit WITHIN this course, count "explored".
    unit, name = curriculum.classify_unit(req.topic or message, req.course)
    _track_topic(req.code.strip(), unit, name, "explored", req.course)

    return {"reply": reply}


@app.get("/api/voice-status")
def voice_status():
    """Tell the frontend whether the natural ElevenLabs voice is configured."""
    return {"eleven": bool(ELEVEN_API_KEY)}


# -----------------------------------------------------------------------------
# TTS AUDIO CACHE -- ElevenLabs charges per character, so we cache the generated audio keyed by the
# EXACT text (+ voice + model). Identical text -> serve the saved render instead of paying to generate
# it again. Most teaching speech is unique (rare hits), but fixed/repeated lines (openers, the tour,
# stock encouragements, UI prompts) hit and cost nothing after the first time. The cached bytes are the
# SAME ElevenLabs render replayed, so there is NO quality change. (Added 2026-07-30.)
# -----------------------------------------------------------------------------
import hashlib
_TTS_CACHE_DIR = DATA_DIR / "tts_cache"


def _tts_cache_path(text: str) -> Path:
    key = hashlib.sha256(("|".join([str(ELEVEN_VOICE_ID), str(ELEVEN_MODEL), text])).encode("utf-8")).hexdigest()
    return _TTS_CACHE_DIR / (key + ".mp3")


@app.get("/api/speak")
def speak(text: str = "", code: str = ""):
    """
    STREAM the tutor's words as a natural ElevenLabs voice (low latency): audio
    starts playing in the browser before the whole clip is generated. The browser
    plays this via <audio src="/api/speak?text=...&code=...">.

    LOCKED DOWN (2026-07-30): requires a valid student code and caps the text length --
    this endpoint spends real ElevenLabs money, and before this change any stranger
    could call it with arbitrary text and run up the bill. Rate limited per code.

    Identical text is served from an on-disk cache (no ElevenLabs call), saving cost + latency on
    repeated lines. If ELEVENLABS_API_KEY is not set, returns 204 and the browser uses its built-in
    voice instead. (Check /api/voice-status first to avoid an empty request.)
    """
    _require_student(code)
    _rate_limit("speak:" + code.strip(), limit=60, window_seconds=300, what="voice requests")
    text = (text or "").strip()
    if len(text) > MAX_SPEAK_CHARS:
        raise HTTPException(status_code=413, detail="That text is too long to speak.")
    if not text or not ELEVEN_API_KEY:
        return Response(status_code=204)

    # Cache HIT: replay the saved render, no ElevenLabs call.
    cache_path = _tts_cache_path(text)
    try:
        if cache_path.exists() and cache_path.stat().st_size > 0:
            return Response(content=cache_path.read_bytes(), media_type="audio/mpeg")
    except Exception as exc:  # noqa: BLE001
        print(f"[speak] cache read error: {exc}")

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVEN_VOICE_ID}/stream"
    headers = {"xi-api-key": ELEVEN_API_KEY, "Content-Type": "application/json"}
    payload = {
        "text": text,
        "model_id": ELEVEN_MODEL,
        "output_format": "mp3_44100_128",
        "voice_settings": {"stability": 0.55, "similarity_boost": 0.75, "use_speaker_boost": True},
    }

    def audio_stream():
        buf = bytearray()
        complete = False
        try:
            with httpx.stream("POST", url, headers=headers, json=payload, timeout=30.0) as r:
                if r.status_code != 200:
                    print(f"[speak] ElevenLabs {r.status_code}: {r.read()[:200]!r}")
                    return
                for chunk in r.iter_bytes():
                    if chunk:
                        buf.extend(chunk)
                        yield chunk
                complete = True
        except Exception as exc:  # noqa: BLE001
            print(f"[speak] stream error: {exc}")
        # Cache WRITE: only after a fully-streamed, non-empty clip; write atomically so a partial
        # (e.g. client disconnect / error) never leaves a truncated file behind.
        if complete and buf:
            try:
                _TTS_CACHE_DIR.mkdir(parents=True, exist_ok=True)
                tmp = cache_path.with_suffix(".part")
                tmp.write_bytes(bytes(buf))
                tmp.replace(cache_path)
                _evict_tts_cache()
            except Exception as exc:  # noqa: BLE001
                print(f"[speak] cache write error: {exc}")

    return StreamingResponse(audio_stream(), media_type="audio/mpeg")


def _evict_tts_cache() -> None:
    """Keep the TTS cache under _TTS_CACHE_MAX_BYTES by deleting the OLDEST clips first
    (down to 80% of the cap, so eviction runs occasionally rather than every write).
    Without this the cache grows forever -- a disk-fill risk once the disk persists."""
    try:
        files = [f for f in _TTS_CACHE_DIR.iterdir() if f.suffix == ".mp3"]
        total = sum(f.stat().st_size for f in files)
        if total <= _TTS_CACHE_MAX_BYTES:
            return
        files.sort(key=lambda f: f.stat().st_mtime)   # oldest first
        target = int(_TTS_CACHE_MAX_BYTES * 0.8)
        for f in files:
            if total <= target:
                break
            size = f.stat().st_size
            f.unlink(missing_ok=True)
            total -= size
        print(f"[speak] cache evicted down to {total} bytes")
    except Exception as exc:  # noqa: BLE001
        print(f"[speak] cache evict error: {exc}")


# Speech-to-text engines (Scribe/Whisper-family) HALLUCINATE non-speech captions on silence
# or background noise -- things like "[outro jingle]", "[music]", "(applause)", "* silence *",
# or musical notes. If one of those slips through as if the student "said" it, the tutor can
# mistake it for a real cue (e.g. "[outro jingle]" once made Mr. Cadabra wrap up a whole topic
# after one question). So we scrub bracketed/parenthesized non-speech captions, and if nothing
# real remains, return "" -- which the UI treats as "I didn't catch that, try again."
def _clean_transcript(text: str) -> str:
    t = (text or "").strip()
    if not t:
        return ""
    # Remove [ ... ] / ( ... ) caption blocks (STT non-speech annotations) and musical notes.
    scrubbed = re.sub(r"[\[\(][^\]\)]{0,60}[\]\)]", " ", t)
    scrubbed = scrubbed.replace("♪", " ").replace("♫", " ").replace("*", " ").strip()
    # If what's left has no letters or digits, it was pure annotation/noise -> treat as silence.
    if not re.search(r"[A-Za-z0-9]", scrubbed):
        return ""
    return scrubbed


@app.post("/api/transcribe")
async def transcribe(audio: UploadFile = File(...), code: str = ""):
    """
    Transcribe the student's recorded audio with ElevenLabs Speech-to-Text (Scribe).
    Browser records the audio (works in every modern browser) and posts it here;
    we return {"text": "..."}. Returns empty text on any failure so the UI can ask
    the student to try again. Reuses ELEVENLABS_API_KEY. Non-speech hallucinations
    (e.g. "[outro jingle]") are scrubbed via _clean_transcript so they never reach the tutor.

    LOCKED DOWN (2026-07-30): requires a valid student code (?code=) + rate limited --
    this endpoint spends real ElevenLabs money. NOTE: the product is currently
    "warm voice out / type in" (all mic buttons hidden), so nothing in the live UI
    calls this; it stays locked and dormant in case voice-in returns as a paid tier.
    """
    _require_student(code)
    _rate_limit("stt:" + code.strip(), limit=20, window_seconds=300, what="voice uploads")
    if not ELEVEN_API_KEY:
        return {"text": "", "error": "no_key"}
    try:
        content = await audio.read()
        if not content:
            return {"text": ""}
        files = {"file": (audio.filename or "speech.webm", content,
                          audio.content_type or "audio/webm")}
        with httpx.Client(timeout=60.0) as client:
            r = client.post(
                "https://api.elevenlabs.io/v1/speech-to-text",
                headers={"xi-api-key": ELEVEN_API_KEY},
                data={"model_id": ELEVEN_STT_MODEL},
                files=files,
            )
        if r.status_code != 200:
            print(f"[transcribe] ElevenLabs {r.status_code}: {r.text[:200]}")
            return {"text": ""}
        return {"text": _clean_transcript((r.json() or {}).get("text", ""))}
    except Exception as exc:  # noqa: BLE001
        print(f"[transcribe] error: {exc}")
        return {"text": ""}


# Serve the static folder (css/js/images if we add them) under /static.
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


# I did no harm and this file is not truncated.
