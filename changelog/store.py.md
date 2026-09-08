# CHANGELOG -- store.py  (notes rolled out of the file's header)

Moved out of `store.py` on 2026-09-08 (build ui): every CHANGE NOTE dated before 2026-09-01 -- 61 entries, VERBATIM, in the order they sat in the file (newest first). The 5 notes from 2026-09-01 on stay at the top of `store.py` itself, and new notes keep going there. Nothing below was edited; grep this file for a build letter or a date. When the header is rolled out again, the newer block is added ABOVE this one.

```text
#   2026-08-31  BUILD rd -- THE MAIN ROAD MOVES THE STAR. The scripted lane grades in
#               code and never emits [[mark]], so today_streak moved neither up nor down
#               there (measured, then watched live). NEW bump_today_streak(): the mirror
#               of rc's reset_today_streak -- same atomic _bump_stats upsert, qz's own
#               today_of=(1,1) clean-mark arm, NO counters touched (scripted problems
#               stay out of problems_practiced/accuracy, per record_drill's standing
#               reasoning). main.py's /api/script/answer calls bump/reset from the
#               engine's own verdict and carries the fresh pair in its response.
#   2026-08-31  BUILD rc -- THE STAR FALLS WHEN THE CHILD SLIPS. Jim's ruling: a miss is
#               ANY WRONG TAP -- the first wrong answer resets the today-streak to 0 even
#               if the child recovers on the re-ask. Until now only a FINISHED problem
#               moved the streak ([[mark]] -> record_practice), so a wrong tap inside a
#               still-going problem left the star standing. NEW reset_today_streak():
#               one thin wrapper over the SAME atomic _bump_stats upsert (today_of=(0,1)
#               is qz's own any-miss-resets arm), touching NO counters -- problems,
#               accuracy and the day streak are untouched; only the today-streak falls.
#               Returns the fresh pair read back from the write, record_practice-style.
#   2026-08-31  BUILD qz -- A STREAK A CHILD CAN SEE TODAY. Jim: a prominent bar on the
#               dashboard AND the classroom page showing (1) the day streak (already
#               tracked) and (2) problems answered correctly IN A ROW TODAY -- a
#               motivator to keep coming back, distinct from the day streak (which only
#               counts showing up) and from lifetime accuracy (which barely moves in one
#               sitting). `student_stats` gains `today_streak` / `today_streak_day`,
#               migrated additively (existing rows read 0 until first touched). Lives on
#               the SAME clock as the day streak (STREAK_TZ, California Pacific, build
#               hn's ruling) so "today" means the same thing for both numbers. Driven
#               ONLY by record_practice's per-problem [[mark]] events -- deliberately NOT
#               folded into record_check's batch unit-check scores, because "4 of 6 on a
#               check" is not a meaningful "in a row" event. One atomic upsert per mark,
#               same CASE-over-stored-date shape _bump_stats already uses for the day
#               streak: a clean mark (correct == attempted) on the same stored day adds
#               to the streak; a clean mark on a NEW day restarts the streak at that
#               mark's count (yesterday's number does not carry over); any mark with a
#               miss (correct < attempted) resets it to 0, mid-lesson, immediately. Read
#               back through get_mastery()'s stats dict, which already reaches both pages
#               (dashboard.html via /api/topics, session.html via /api/session, newly
#               widened here to carry stats too) -- so a value stored on an OLD day still
#               reads back honestly as 0 without a write, the same way the day streak
#               already had to be read-guarded for a student who has not visited today.
#   2026-08-27  BUILD op -- THE AUTHORED LANE COUNTS ITSELF. usage_stats gains
#               script_turns / ms_script_median (kind="script" rows -- scripted-
#               lesson turns, no model on the clock) and script_ai_turns (brain
#               rows with mode="script" -- the lane's bounded interventions).
#               The Phase-3 pilot's claim is "authored beats are instant"; now
#               the admin card can show it next to the live lane's median.
#   2026-08-26  BUILD ol -- THE 16-CHARACTER TRAP. "critic-unresolved" is 17 chars;
#               verify_status is String(16), so every shipped-critic reply was
#               stored as "critic-unresolve" and (mw)'s counter key never matched
#               -- 14 rows read "Uncounted verdicts" while the Shipped tile said
#               "0 live critic". usage_stats now normalizes the truncated
#               spelling on read (history included; no migration).
#   2026-08-25  BUILD nq -- THE OWNER'S FLAG. Jim, watching geometry live, caught
#               the tutor saying "piece" for "angle" and asked: "It would be great if
#               I could point this out while in the app and have it fix it itself."
#               This is the storage half: table `flags` -- one row per sentence Jim
#               flags from a tutor bubble (page, course, student code, the quoted
#               sentence, his note, resolved flag). OWNER-ONLY by Jim's ruling
#               2026-08-25: "I only want it when I'm online. I don't want the parents
#               or teachers to see it." -- so writes arrive only through an
#               admin-key-gated route; nothing here is readable by student/parent/
#               teacher surfaces. Brand-new table -> create_all builds it, no
#               migration, nothing existing touched. Helpers: add_flag / list_flags /
#               resolve_flag, all never-raise in the read path like their siblings.
#   2026-08-24  BUILD na -- BUILD COST AND SERVE COST ARE DIFFERENT QUESTIONS.
#               usage_stats reported tts_chars_generated as one number, so the ~30,000
#               lines of the course rendered ONCE to audio were indistinguishable from
#               a line a child asked to hear today. /admin divided the sum by one
#               week of engaged hours and printed "$610.76 per student-hour".
#               Adds TTS_BUILD_MODES -- the ONE definition of "this row was course
#               construction" -- and six additive keys (tts_chars_build/_serve,
#               tts_chars_cached_build/_serve, tts_requests_build/_serve).
#               ⚠️ THE THREE ORIGINAL TOTALS ARE UNCHANGED and still mean build+serve,
#               so every existing caller reads exactly what it read before.
#               ⭐ ANYTHING NOT NAMED AS BUILD COUNTS AS SERVE, including rows written
#               before `mode` existed (they carry ""). Understating what teaching
#               costs is how you misprice a product; overstating it only makes you
#               cautious. PART 3do fails the battery if main.py grows a render pass
#               this tuple does not name.
#   2026-08-24  BUILD mw -- THE VERDICT NOBODY COUNTED. usage_stats had keys for
#               every referee verdict except "critic-unresolved", which tutor.py has
#               emitted since build iv. Unknown statuses were added to verify_none,
#               so a reply that a referee OBJECTED to and that shipped anyway was
#               reported as a reply nobody had checked -- the opposite fact. Adds the
#               key, and unknown verdicts now land in a LOUD verify_unknown bucket
#               (with the offending names) instead of quietly reading as "unchecked".
#   2026-08-24  BUILD mt -- PRACTICE IS COUNTED, AND STILL IS NOT MASTERY. Jim:
#               "is there a way they can track how much practice problems they've
#               done, how they've done on their practice problems AS APART FROM the
#               regular course so we can encourage them to practice."
#               His parent scenario IS the design brief -- "go practice your
#               multiplication tables for twenty minutes a day all week long" -- so
#               the grain is (student, lesson, DAY) and the child can SHOW the week.
#               NEW: table drill_daily, record_drill(), drill_stats().
#               ⚠️ ITS OWN TABLE, NOT A COLUMN ON student_stats. "Apart from the
#               regular course" was the request, and a blended number can never be
#               un-blended later.
#               ⚠️ IT DOES NOT TOUCH MASTERY. Jim's ruling of 2026-08-23 stands:
#               drill is practice, quizzes are for mastery. Nothing here writes
#               unit_checks or topic_progress, and PART 3dm proves it on a real DB.
#               ⚠️ BUT IT DOES KEEP THE STREAK. _bump_stats with no counters writes
#               last_active and the streak and nothing else. A child who practised
#               every day this week HAS worked every day this week, and a streak
#               that ignored it would call them lazy for doing what they were asked.
#   2026-08-24  BUILD mq -- THE COST EPOCH. Jim: "since we have restructured how
#               things are run, we should zero out our current cost measurement so it
#               is measuring cost based on how we do it now."
#               ⚠️ "ZERO OUT" DELIBERATELY DOES NOT MEAN DELETE. The obvious reading
#               is "empty the usage log", which would destroy the only record of what
#               this app has ever cost in exchange for a tidier panel. An epoch moves
#               the LEFT EDGE of the window instead: set_cost_epoch() writes ONE
#               timestamp, usage_stats() gained an optional `since`, and every row
#               stays exactly where it is. The 7- and 30-day panels are untouched.
#               ⚠️ AND THE PURGE NOW EXEMPTS IT. The epoch rides system_events, which
#               is deleted at 90 days -- so without the exemption Jim's measurement
#               era would evaporate one quiet night and every figure would snap back
#               to all-of-history with nothing on screen saying so.
#               NEW: student_minutes_since() -- the DENOMINATOR for cost per
#               student-hour, measured on the DAY WORKED and never on updated_at,
#               which moves whenever a row is touched and would migrate a nudged
#               yesterday-row into the wrong window.
#   2026-08-20  BUILD jr -- CONSISTENCY MEMORY. Jim, watching a live Basic Math lesson:
#               "since that's OVER NINE, carry" and, four turns later in the SAME lesson,
#               "since that's TEN OR MORE, carry". Mathematically identical; two
#               different rules to a seven-year-old. NEW table `student_phrasings`
#               (code, course, concept -> phrasing) plus remember_phrasing() and
#               get_phrasings(). FIRST PHRASING WINS AND NEVER CHANGES -- the words the
#               child actually learned are the ones that must keep coming back --
#               enforced race-safely by read/insert/read, so two overlapping turns
#               cannot fork a student's vocabulary. Brand-new table: create_all builds
#               it, no migration, nothing existing touched.
#   2026-08-20  BUILD jq -- WHAT THE TURN WRITES. jm/jp measured that 77% of a
#               16-second turn is the model serially generating ~875 output tokens;
#               this says which 875. usage_log gains out_chars / out_spoken_chars /
#               out_tags (additive, same migration), measured on the ACCEPTED draft so
#               a discarded one cannot skew the split, and usage_stats reports
#               sized_turns + the averages + out_spoken_share. Characters rather than
#               tokens on purpose: the API reports tokens for the whole turn INCLUDING
#               retries, so only the text actually in hand can be split honestly.
#   2026-08-20  BUILD jp -- THE SECOND OPINION BECOMES VISIBLE. LIVE_CRITIC is set in
#               production with LIVE_CRITIC_MODEL=claude-opus-5, so a whole extra model
#               reads every accepted draft -- and it was invisible in BOTH directions:
#               its seconds landed in jm's "referees and our own work" bucket (ms_model
#               wrapped the teaching call only), and its tokens were never counted at
#               all, because every figure on the cost card filters kind == "brain" and a
#               critic row is kind == "critic". NEW: usage_log.ms_critic (additive, same
#               migration), log_usage takes it, _timing_summary reports ms_critic_avg /
#               ms_critic_share (tolerating 3-wide rows so PART 3cp's fixtures still
#               work), and usage_stats aggregates the critic's own calls and tokens.
#   2026-08-20  BUILD jm -- THE TURN CLOCK. `usage_log` gains ms_total / ms_model /
#               ms_retry (additive migration _migrate_usage_log_timing, default 0 =
#               "never timed"), log_usage accepts them, and usage_stats reports
#               timed_turns + avg/median/p90/max plus the model and retry averages and
#               ms_retry_share. Jim's objective this week was "a responsive accurate
#               application above cost", and the only measurement of turn time that had
#               ever existed was Jim counting seconds. ms_retry makes Lever 1 of the
#               responsiveness proposal -- referee retries -- an actual number.
#               Percentiles are computed in PYTHON by the new pure _timing_summary()
#               over the newest TIMING_SAMPLE (5,000) rows: SQLite and Postgres disagree
#               about percentile SQL, and a latency figure that means two different
#               things on two databases is worse than none. The cap is REPORTED
#               (ms_sampled vs timed_turns), never silent.
#   2026-08-18  BUILD il -- THE TODAY BAR'S WORKED TICKS. today_goals grows Jim's
#               "honest work-time counts" notion: done entries may now be "3w"
#               (a WORKED tick, earned by engaged minutes) beside plain "3"
#               (COMPLETED). get_today_goals returns the new "worked" list; old
#               plain-int rows parse unchanged; save_today_goals(worked=[...])
#               merges with completed-outranks-worked (a finish upgrades the tick,
#               time never downgrades it). Same column, no migration.
#   2026-08-18  BUILD ik -- THE TOUR IS A RECORDED FACT. Jim's live catch: tour ->
#               placement -> return, and the whole introduction played again,
#               because "toured" was INFERRED from lesson history and the tour
#               writes none. NEW tours_seen table (code + tgroup "elem"/"typing" +
#               seen_at) with record_tour_seen()/tour_seen(); joins
#               _STUDENT_CODE_TABLES on day one (a reset student is a new student
#               and gets the introduction again). main.py records it when
#               __tour_done__/__tour_done_declined__ arrives and ORs it into the
#               /api/session "toured" flag.
#   2026-08-18  BUILD hv -- ONE STORAGE BACKEND, LOUDLY (Phase 5, review Class E).
#               (1) NEW degraded(): True when DATABASE_URL is SET but unreachable --
#               the state that used to silently fork every write onto un-backed-up
#               files; main.py now gates the teaching lanes on it (status() reports
#               it too). (2) NEW deletions ledger (table + record_deletion):
#               delete_parent_cascade and reset_student_data write one row per
#               deliberate erasure. (3) import_all: token tables (parent_tokens,
#               parent_resets, teacher_tokens, teacher_resets) are WITHHELD from
#               every restore -- a revoked credential stays revoked -- and the
#               deletions ledger is RE-APPLIED after the restore for deletions
#               NEWER than the snapshot (older ones are skipped on purpose: the
#               snapshot's data is legitimately post-deletion). Proved end-to-end
#               by PART 3bm on a real database.
#   2026-08-18  BUILD hn -- THE STREAK LIVES ON CALIFORNIA TIME (Jim's ruling on THE
#               THREE CLOCKS, 2026-08-18: "use California Pacific Time"). The streak's
#               day boundary was the SERVER-UTC day, so a student practicing at 8pm in
#               California was already "tomorrow" to the streak -- practice every
#               evening and the streak could still break. NEW _streak_now()/
#               _streak_today(): the streak's "today" and "yesterday" are computed in
#               STREAK_TZ (env, default America/Los_Angeles) and fed to _bump_stats'
#               same atomic SQL CASE -- the arithmetic is unchanged, only the calendar
#               the day-strings come from moved. zoneinfo + the tzdata package (added
#               to requirements so Windows dev boxes have the IANA database too);
#               if the zone cannot load, it falls back to UTC LOUDLY (one boot print)
#               -- the old behaviour, never a crash. Hours tiles stay student-local,
#               backups stay server-local; the CLOCKS note below records the decision.
#   2026-08-17  BUILD hl -- THE SMALL CUTS OF PHASE 3 (this file: two of the three).
#               (1) THE STREAK IS ATOMIC. NEW _bump_stats(code, problems, correct,
#               attempted, checks) -- ONE dialect-native upsert that bumps the
#               student_stats counters AND advances the streak in the same statement,
#               via a SQL CASE over ISO date strings (same day -> keep, yesterday ->
#               +1, gap -> reset to 1). Replaces the _get_stats_row/_touch_streak/
#               _save_stats read-then-write trio in record_check, record_sprint and
#               record_practice -- the last remaining lost-update race in the store
#               (deliberately deferred in hi; now closed the same way as the rest).
#               The trio itself is retired. Also added "THE THREE CLOCKS, DOCUMENTED"
#               -- the app has three day-boundaries (student-local for hours,
#               server-UTC for the streak, server-local for backups); which one a
#               streak SHOULD use is a product decision recorded there for Jim, not
#               silently changed here.
#               (2) A QUIZ HAS ONE IDENTITY. record_topic_quiz now claims an existing
#               row by (code, course, unit, topic_idx) BEFORE upserting: if the model
#               rephrases a topic name ("Adding Fractions" vs "Fraction Addition"),
#               the slug changes but the (unit, topic_idx) coordinate doesn't -- the
#               old code minted a second row and the student's best/taken history
#               split across ghosts. Now the existing row's key is reused, so
#               rephrasing HEALS instead of forking; no key migration, existing data
#               preserved, topic_idx 0 (unknown) keeps the old slug behaviour.
#               Proved (temp SQLite): rephrase -> ONE row, best=max, taken summed;
#               180/180 threaded practice marks exact with streak correct; streak +1
#               on consecutive days and reset after a gap. ruletests PART 3bc
#               re-proves all of it on every push.
#   2026-08-17  BUILD hk -- NO EXCHANGE CAN BE LOST. NEW update_history(code, course,
#               fn, cap): the chat path's only history writer, a COMPARE-AND-SWAP
#               transform. The old shape -- read blob, run a multi-second model call,
#               write the whole blob back -- was last-writer-wins with a race window
#               the width of the model's latency; a double-submit or second tab
#               silently deleted a full exchange. CAS chosen over a row lock ON
#               EVIDENCE: the first version used SELECT..FOR UPDATE and was correct on
#               Postgres but SILENTLY WRONG on SQLite (pysqlite's legacy isolation
#               begins the transaction at the first WRITE, so the read ran outside it
#               -- the hammer lost 200 of 240 appends with ZERO errors). CAS has no
#               dialect trap: UPDATE..WHERE history = exactly-what-we-read, loop on
#               rowcount 0. fn must be pure (it may run again on retry). The insert
#               race (two first turns for a brand-new student) retries into the CAS
#               path. Exhausting retries RAISES -- dropping an exchange silently is
#               the disease, not an acceptable fallback. Proved: 240/240 threaded
#               appends, pairs adjacent; ruletests PART 3bb re-proves on every push.
#   2026-08-17  BUILD hi -- THE COUNTERS ARE ATOMIC (Phase 3 of the full-app review,
#               "one owner per fact"). The store's universal write pattern was
#               SELECT-in-Python-then-upsert -- a lost-update race whose worst case
#               was ACADEMIC: two overlapping check submissions could write a stale
#               max and make best_pct GO DOWN, silently un-mastering a unit and
#               re-locking the Final Exam while topic_progress still said "mastered"
#               (confidently wrong together, the unit-rail class in the gradebook).
#               _upsert gained exprs= -- column -> (seed, build_fn) evaluated INSIDE
#               the native ON CONFLICT, identical on Postgres and SQLite (bests use
#               CASE, not GREATEST, because SQLite has no two-arg GREATEST). Five
#               sites converted: record_minutes (+n), record_check (taken/correct/
#               attempted counters + never-regress best), record_topic_quiz (count +
#               best), record_topic (touches + keep-deeper-status via CASE on
#               STATUS_RANK), _set_unit_status (upgrade-only, atomically). Reporting
#               fields ("improved", attempt number) still use a read and are
#               best-effort under concurrency BY DESIGN -- they flavour one
#               congratulation line; the STORED data no longer depends on any read.
#               DELIBERATELY DEFERRED: student_stats streaks (_get_stats_row/
#               _save_stats) stay read-then-write -- the streak's day arithmetic
#               belongs with the one-activity-clock work (Phase 3, later build), and
#               its stakes are a display number, not mastery.
#               PROVED on a real database: 200 threaded calls -> zero errors, minutes
#               and counts EXACT, best = true max, deepest status kept, and the
#               un-mastering interleave reconstructed and shown impossible.
#               ruletests PART 3az re-proves a scaled version on every push.
#   2026-08-17  BUILD ha -- EYES: THE system_events TABLE. Phase 1 of the full-app
#               review. The review's meta-finding: fail-open was applied ~19 times with
#               print-only reporting, so a crashed referee, a dead heartbeat and a healthy
#               system all looked identical -- which is exactly why "5 of 6 audit causes
#               were a check that failed to fire". New table system_events + record_event
#               (never raises, no-ops when the DB is off), event_stats (kind->name->count
#               for /admin and the night watch), recent_events (the telemetry card's
#               list), last_event_at (powers /health's heartbeat/backup/nightwatch AGES),
#               purge_system_events (rides the heartbeat purge pass, default 90 days).
#               Tally only: short details, never conversation text, never secrets.
#   2026-08-17  BUILD gz -- THE WORST VERIFY STATUS IS NO LONGER INVISIBLE. usage_stats()
#               groups usage_log.verify_status into verify_* keys, but any status not in
#               its init dict fell into verify_none -- and the statuses that fell were
#               "prose-unresolved" (a reply that SHIPPED to a student carrying a known,
#               unresolved referee finding -- the single most important number on the
#               dashboard) and "empty" (the model returned nothing twice). Both were
#               indistinguishable from ordinary untagged turns. Found by the 2026-08-17
#               full-app review ("the app cannot see its own failures" class). They are
#               now their own keys; admin.html counts prose-unresolved among checked and
#               caught turns.
#   2026-08-13  BUILD fa -- TEACHER ACCOUNTS (security finding F2). NEW tables `teachers`,
#               `teacher_tokens` and `teacher_resets`, deliberately MIRRORING the parent
#               tables rather than reusing them: a parent row carries Stripe and
#               subscription state that has nothing to do with a teacher, and the parent
#               path is live with paying customers. Same shape, same token discipline,
#               separate blast radius. NEW nullable `classes.teacher_id` (the real OWNER)
#               via the same additive, self-healing migration used for teacher_code and
#               parent_id -- existing classes keep every row with teacher_id NULL, which
#               means UNOWNED and claimable, never lost. NEW claim_class() and
#               adopt_classes_by_teacher_code(): both do their ownership test and their
#               write in ONE transaction with `teacher_id IS NULL` in the WHERE clause, so
#               two teachers racing for the same class cannot both win and a legacy
#               teacher code can never outrank a real password by taking an owned class.
#   2026-08-11  BUILD ea -- THE PACING STEER (Four-Lens homeschool item 3). New table
#               steers (ONE standing plan per student: course + unit) + set_steer/
#               get_steer/clear_steer. Reset family AND the dy code-move both cover it
#               via _STUDENT_CODE_TABLES. Applied in main.py's chat handler; shown and
#               controlled on /family.
#   2026-08-11  BUILD dy -- PARENT CHILD-MANAGEMENT (Four-Lens parent item 2): NEW
#               rename_student() (accounts row only), change_student_code() (a leaked
#               login code is a leaked key -- every per-student row moves to the fresh
#               code in ONE transaction, because the code is the join key everywhere;
#               the old code dies the moment it commits), and attach_student() (claim
#               an UNOWNED account by its code; an account owned by another parent is
#               never transferable here -- returns 'owned' so the endpoint can refuse).
#               Remove needed nothing new: reset_student_data() already cascades the
#               accounts row with everything else.
#   2026-08-11  BUILD dt -- MISSED-PROBLEM MEMORY (Four-Lens student item 1, the data
#               foundation). NEW table quiz_misses (one row per missed quiz/check/final
#               question: the question as asked + the student's exact wrong answer,
#               reported by the tutor per rule 55) + record_misses() (re-clamped
#               lengths, <= 25 per event, swept to the newest 200 rows per student on
#               every write) + get_misses() (newest first, course-filterable). Joins
#               _STUDENT_CODE_TABLES on day one; export/backup picks it up
#               automatically because export_all() walks _tables.
#   2026-08-11  BUILD dj -- BACKUPS (Jim: "if Render falters, do we have sufficient
#               backup so that we could recreate everything right away?"). The code is
#               safe on GitHub and the voice cache is recreatable for ~$20 -- the
#               DATABASE is the one thing that was not recreatable at all. Two new
#               functions, deliberately symmetrical and deliberately dialect-agnostic
#               (they go through SQLAlchemy, so a snapshot taken from Postgres restores
#               into Postgres OR SQLite, which is also how the round-trip is tested):
#                 export_all()  -> one JSON-serializable snapshot of EVERY table this
#                                  file owns, dates as ISO strings, with row counts.
#                 import_all(payload, wipe=True) -> restores a snapshot inside ONE
#                                  transaction: wipe a table, insert its rows, next
#                                  table; any failure rolls the WHOLE restore back, so
#                                  a half-restored database cannot exist. Unknown
#                                  tables in old snapshots are skipped with a note;
#                                  unknown columns are dropped row-by-row (a snapshot
#                                  from an older build restores into a newer schema).
#               NEVER exposed as a write endpoint -- restore runs only from the
#               offline restore_backup.py with an explicit flag. main.py writes the
#               nightly snapshot; /admin gains a download button; RECOVERY.md is the
#               runbook.
#   2026-08-11  BUILD dd -- FLUENCY SPRINTS: new table `sprints` (one row per completed
#               sprint), record_sprint() and get_sprint_history(). Counts are CLAMPED
#               (correct <= attempted <= 30) so the dashboards this will feed stay
#               honest, and `personal_best` compares only with THIS student's own
#               history (rule 42). Joins _STUDENT_CODE_TABLES on day one -- a Start
#               Fresh that left sprint rows behind would hand the reset student a
#               personal best they never set. Recording a sprint touches no mastery, no
#               status, no unlock -- sprints never gate, and PART 3n enforces it.
#   2026-08-10  BUILD cu -- record_check() now also reports the UNIT's state, not only
#               this attempt's. "mastered" has always meant "THIS attempt cleared 90%",
#               which is right for the celebration and wrong for the student's nerve: a
#               retake that goes badly returned mastered=False even though best_pct still
#               held the unit and the unit status is never un-set. Added, additively:
#               unit_mastered (best_pct >= PASS_PCT), improved, and attempt.
#               Jim asked for a review-and-retake path for a unit passed but not mastered;
#               the storage layer has always kept the BEST score, so every retake was
#               already safe -- nobody had ever been told, and fear of losing a good score
#               is the commonest reason a student refuses to try again. Rule 50(e) now
#               says it out loud, and this is that promise being true in the data.
#   2026-08-10  BUILD cn -- SCALE. Jim: "suppose we have ten thousand people using this
#               app simultaneously. It needs to be able to handle that."
#               (1) CONNECTION POOL sized on purpose. SQLAlchemy's default is five
#                   connections plus ten overflow -- fifteen, total, for a service whose
#                   sync endpoints each want one from a FastAPI threadpool. Now
#                   DB_POOL_SIZE / DB_MAX_OVERFLOW (10 + 20 by default), with
#                   pool_recycle=1800 so a managed Postgres cannot hand us a socket it
#                   quietly closed overnight, and pool_timeout so a spike queues instead
#                   of hanging forever.
#               (2) purge_usage_log(days) -- the usage log is one row per model call and
#                   per TTS request and NOTHING ever removed one. At ten thousand
#                   students that is millions of rows a month, in the same database the
#                   lessons run on. main.py calls this once a day off the heartbeat that
#                   already exists. Counts only; no student text was ever in there.
#   2026-08-09  SCORING IS FLOORED, NOT ROUNDED (build ch, audit #2 item 9). Every
#               score here used round(100 * correct / total) and then compared THAT to
#               the pass mark, so a rounded-up percentage could carry a student over a
#               bar they had not cleared -- and the rounded value was also what got
#               STORED as best_pct, which is what the mastery bars and the printable
#               record read. New score_pct() does it in integer arithmetic, floored, and
#               record_check / record_topic_quiz / record_final_exam all use it.
#               NOTHING A STUDENT HAS ALREADY EARNED CHANGES: at our real question counts
#               (3-5 topic quiz, 4-6 unit quiz, 18 final) there is no score where
#               rounding and flooring disagree -- verified exhaustively, and ruletests.py
#               re-verifies it for every total from 1 to 40. But "the progress bars are
#               honest" should not rest on a coincidence in the question counts, and a
#               future 20-question exam would have broken it silently.
#   2026-08-09  TODAY'S GOALS (build cg, Jim: "there's only two of the three tracking
#               bars across the top. I don't know where the third one is, and I don't
#               know why it keeps disappearing"). NEW TABLE `today_goals`
#               (code, course, day) holding the goal items and which are finished, so the
#               TODAY bar survives a reload the way UNIT and COURSE already do -- they
#               are rebuilt from mastery data, and TODAY had no server side at all.
#               get_today_goals() / save_today_goals(): ticks MERGE (a later turn can
#               never un-tick an earned win), a genuinely new plan resets them, and
#               out-of-range marks are dropped. Scoped per day, so yesterday's goals are
#               never shown as today's. Brand-new table -> create_all builds it; no
#               migration. JOINS _STUDENT_CODE_TABLES on day one (standing rule).
#               NOTE for the next person: read that table with t.c["items"], never
#               t.c.items -- SQLAlchemy's ColumnCollection already has an .items()
#               method, so attribute access hands back the METHOD and the query dies
#               with "may not be passed as a SQL expression". Caught on the first dry run.
#   2026-08-09  FOUNDATION MEMORY (build ce, Jim: "if a student is returning, nothing
#               tells him which scripts that student has heard, so a loyal student can
#               re-hear it. We need to fix it"). NEW TABLE `foundations_heard`
#               (code, course, term) with first_heard, last_heard and a `refreshers`
#               count, plus get_foundations_heard() and record_foundation_heard().
#               Brand-new table -> create_all builds it; no migration; nothing else
#               touched. The FIRST hearing keeps its date forever and every later
#               delivery counts as a refresher, which is the honest signal that a term
#               did not stick -- worth surfacing on the parent dashboard later.
#               It JOINS _STUDENT_CODE_TABLES on day one (standing rule): a "Start
#               Fresh" that left these rows behind would hand the reset student a tutor
#               who still believes he already explained fractions to them.
#               Both accessors swallow their own errors: a memory lookup must never be
#               able to break a lesson.
#   2026-08-07  STUDENT RESET + BETA-DELETE SAFETY (build bc). (1) delete_beta_cascade now
#               verifies the pass EXISTS before wiping anything (a mistyped/pilot code used
#               to get its data erased, then a "no pass" error). (2) NEW reset_student_data
#               (code) -- wipes every per-student row for ONE code (pilot personas like
#               0000, demo codes) so it can be reused as brand new; the code keeps working.
#   2026-08-07  BETA DELETE (build bb, Jim: revoke wasn't enough). NEW delete_beta_cascade()
#               -- removes the beta_codes row AND every per-student row under that code, one
#               transaction. ALSO: final_exams joined _STUDENT_CODE_TABLES, so parent resets
#               and beta deletes wipe exam rows too (the table was added earlier today).
#   2026-08-07  LOOK-IT-UP LIBRARY (Jim: the searchable reference database). NEW table
#               `library_articles` (topic_key+band pk): title, body (safe-HTML), source
#               ('generated' -- curated seeds live in library.py, not here), hits counter,
#               created_at. New functions: get_library_article(key, band),
#               save_library_article(), list_library_titles(band) (for fuzzy matching),
#               bump_library_hits(). Articles are written ONCE by the model on a missed
#               search and served from here forever after. Brand-new table -> create_all
#               builds it; no migration; nothing else touched. Additive only.
#   2026-08-07  FINAL EXAM (Jim: a real course final, gated on mastering all nine units).
#               NEW table `final_exams` (code+course pk): exams_taken, best_pct, last_pct,
#               correct, attempted, passed_at (set ONCE, the first time the score reaches
#               PASS_PCT=90 -- the date the course was conquered; 2026-08-07 later the same
#               day: the diploma was REMOVED (accreditation optics) and the date now simply
#               backs the 🏅 Course Champion award), updated_at. New
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
```

I did no harm and this file is not truncated.
