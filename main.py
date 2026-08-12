# =============================================================================
# main.py  --  Math Tutor MVP  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-12  APP_BUILD -> "2026-08-12eg-parents-demo". THE PARENTS DEMO DOOR
#               SPEAKS TO WHAT A PARENT ACTUALLY ASKS (Jim, from a parent-teacher
#               conference: a teacher shows the app -- what does the parent want to
#               know? "Is my child actually learning" and "will she actually want to
#               do this"). THIS FILE: seven lines APPENDED to DEMO_VOICE_LINES
#               (227 -> 234), identical to demo.html's VOICE_LINES -- new parents
#               intro, new words for parent stops 1/2/4/5/8 (conference question ·
#               teaches-never-hands-answers · one-record + the streak nobody can
#               assign · kitchen-table + missed-problems-come-back · trophy case as
#               the will-she-use-it answer), and a new outro carrying the
#               voice-privacy answer. The tour structure is untouched: same ten
#               stops, same panels, same order; HS_STOPS unchanged. Clips render on
#               first play or via the admin pre-render.
#   2026-08-12  APP_BUILD -> "2026-08-12ef-homeschool-pitch". THE CONFERENCE PITCH
#               REWORK of /homeschool (build stamp only in this file; the work lives
#               in static/homeschool.html + new ef guards in ruletests.py). Jim,
#               pitching at a homeschooling conference: same content, new spine --
#               records/filing day FIRST, honest hours as its evidence, the mastery
#               bars named (80/90, never rounds up), a new "You're still the teacher"
#               section (steer + placement + works-with-your-curriculum), a new "The
#               trust questions" section (four calm answers: never a bare answer, the
#               separate math-engine check, voice audio deleted immediately -> links
#               /privacy, something-bigger-than-math -> a trusted adult), and a
#               method line naming the WWC guides. No dollar figure on the page --
#               prices live on /pricing alone. FAQ byte-identical (eb guards).
#   2026-08-12  APP_BUILD -> "2026-08-12ee-teaching-upgrades". THE FIVE TEACHING
#               UPGRADES (prompt lane; claude/Teaching_Evidence_Base_2026-08-10.md).
#               No route or logic changes in THIS file -- the build stamp only. The
#               work lives in: prompts.py (rules 56-60: find-the-error,
#               self-monitoring, two-ways-one-board, right-answer-wrong-method, the
#               board spotlight), the three teaching pages session/practice/topic
#               (the [[highlight]] tag gains id="line" and id="board" -- board work
#               glows while teaching; self-clears; reduced-motion safe), and
#               ruletests.py (new PART 3t; coverage needles; the 150k prompt ceiling
#               raised to 160k per Jim's standing 2026-08-11 decision).
#   2026-08-12  APP_BUILD -> "2026-08-12ed-read-throttle". SECURITY PASS 2 -- finding F1
#               (claude/Security_Review_2026-08-12.md). The GET-by-code reads that return a
#               child's data (session, records, misses, awards, time, topics, assessment,
#               placement, courses, sprints, sprint) were enumerable and UNTHROTTLED -- a
#               short code was the only key. Two-part fix:
#               (A) _read_guard(request, code) now fronts every one of those endpoints. It
#                   applies a generous per-IP raw read cap (READ_IP_LIMIT=600/5min) AND the
#                   real anti-enumeration guard: a per-IP DISTINCT-CODE ceiling
#                   (CODE_PROBE_MAX=50 distinct codes / CODE_PROBE_WINDOW=900s). A family
#                   re-reads its own 1-2 codes forever (never trips); a scraper walking
#                   thousands of DIFFERENT codes is refused after ~50. Self-pruning,
#                   in-process, env-tunable. Pairs with the ec F3 fix (an IP can't be
#                   spoofed, so the cap can't be dodged by rotating addresses).
#               (B) _new_student_code widened 2 -> 4 digits: 50 x 9000 = 450,000 (was
#                   4,500), a ~100x space. Existing 2-digit codes keep working (nothing
#                   validates digit count); only NEW codes are longer. Still one friendly
#                   word + a number for a child to type.
#               Guards: ruletests "BUILD ed" block (every read endpoint calls _read_guard;
#               the generator is 4-digit) + a live SEC2-DRILL (enumeration from one IP
#               hits 429; a fresh IP is unaffected; same-code re-reads never trip; new
#               codes match WORD+4digits). F2 (class lock) remains for the teacher-auth build.
#   2026-08-12  APP_BUILD -> "2026-08-12ec-security-hardening-1". SECURITY PASS 1 of the
#               review in claude/Security_Review_2026-08-12.md (Jim: "make sure our security
#               is robust"). Three low-risk, universal fixes:
#               F3 -- _client_ip no longer trusts the SPOOFABLE leftmost X-Forwarded-For
#                     entry (a visitor could prepend a fake and slip the per-IP brute-force
#                     limits on sign-in / signup / password-reset). It now trusts only the
#                     rightmost TRUSTED_PROXY_HOPS entries (default 1 = the address Render
#                     appended) -- un-spoofable behind our own proxy.
#               F4 -- a new @app.middleware stamps the standard browser-hardening headers on
#                     EVERY response: nosniff, X-Frame-Options SAMEORIGIN, Referrer-Policy,
#                     HSTS, a mic-only Permissions-Policy, and a Content-Security-Policy in
#                     REPORT-ONLY mode (our inline styles/scripts + Plausible mean an
#                     enforcing CSP could blank the site; report-only describes it safely
#                     and can be flipped on later with a nonce refactor).
#               F5 -- /api/transcribe caps the audio it reads at MAX_AUDIO_BYTES (12 MB,
#                     env-tunable) and returns a clean 413 over it, instead of pulling an
#                     unbounded upload into memory. The catch-all except now re-raises
#                     HTTPException so the 413 actually reaches the caller.
#               Nothing else changed. Guards: ruletests PART 3 "BUILD ec" block (source
#               checks + a live TestClient drill proving headers ship and XFF is read from
#               the trusted end). F1 (read-by-code throttle) and F2 (class lock) are the
#               next two builds, per the review's proposed order.
#   2026-08-11  APP_BUILD -> "2026-08-11eb-features-faq". CALM FEATURES PAGE + FOUR
#               AUDIENCE FAQs (Jim: "the features page has too much information... I don't
#               like the icons... just bullet points... consolidate... drop-downs" + "a FAQ
#               section on the bottom of the homeschool, parent, teacher and student pages
#               ... DIFFERENT FAQs"). Static-only build -- nothing in this file changed but
#               the stamp. features.html: one calm column of six <details> drop-downs,
#               features as plain bullets (bold name + one line), NO emoji icons, 30 -> 41
#               features (the eleven shipped since the last rewrite: sprints, refresher,
#               save/resume, retake, tricky-ones x2, steer, child management, phone dock,
#               a11y, /help). students/parents/homeschool/teachers .html each end with an
#               8-question FAQ in that audience's own voice; no question repeats across
#               pages; every answer states only what the product does today. homeschool
#               also lost its phantom "parent code" line (same dq honesty fix as parents).
#               Checks: ruletests PART 3p eb block (icon-free features page, new features
#               present, four disjoint FAQs, parent-code guard extended to homeschool).
#   2026-08-11  APP_BUILD -> "2026-08-11ea-pacing-steer". THE PACING CONTROL (Four-Lens
#               homeschool item 3; the parent-as-teacher design Jim approved 07-28).
#               A parent can now set ONE standing plan per child on /family: "center
#               sessions on Unit N for now." NEW POST /api/parent/student-steer
#               (parent-gated + ownership-checked; unit=0 clears; course defaults to
#               where the child actually works, resolved server-side so no page grows
#               a seventh course list). Applied by _resolve_focus in the chat handler:
#               the child's OWN explicit focus always outranks the plan (rule 50), and
#               the mastery note words it honestly -- "their parent asked", introduced
#               as today's plan, never as the student's request, never a punishment,
#               and the student's agency wins if they ask for something else. The
#               steer shows on /family (overview carries it) until changed or cleared;
#               it survives a dy code regeneration and dies with a reset.
#   2026-08-11  APP_BUILD -> "2026-08-11dz-a11y-and-phones". ACCESSIBILITY + PHONE
#               PASS (Four-Lens student items 5 and 8). Nothing in this file changed
#               but the stamp: on all three teaching pages the transcription readout
#               and your-turn hint are polite aria-live regions, the mic button has a
#               spoken name, the orb is decorative, session's four overlays are real
#               dialogs (welcome focuses its action), and prefers-reduced-motion
#               stills every pulse. PHONES: the board comes FIRST and the left rail
#               becomes a compact bottom DOCK (orb+status row, horizontal nav chips,
#               mic and answer box always in reach). Desktop untouched; all inside
#               the existing 900px media query.
#   2026-08-11  APP_BUILD -> "2026-08-11dy-child-management". FOUR SUPPORT EMAILS
#               BECOME FOUR BUTTONS (Four-Lens parent item 2). New parent-token-gated,
#               ownership-checked endpoints: /api/parent/student-rename ·
#               student-newcode (a leaked login code is a leaked key: fresh code
#               minted, EVERY per-student row moves with it in one transaction via
#               store.change_student_code, old code dies instantly) · student-remove
#               (permanent; the parent must TYPE the child's name back, and the
#               server verifies it -- then the same cascade Start Fresh uses) ·
#               student-attach (claim an UNOWNED code; another family's code returns
#               409 with a support hand-off; shared demo codes refused). Ownership
#               misses return 404, not 403 -- an outsider probing codes learns
#               nothing. family.html grows the ⚙ Manage panel per child + the
#               attach link under Add-a-child.
#   2026-08-11  APP_BUILD -> "2026-08-11dx-assessment-save-resume". THE 45-QUESTION
#               ASSESSMENT SURVIVES A CLOSED TAB (Four-Lens student item 4). Nothing
#               in this file changed but the stamp: challenge.html now saves the run
#               state on the student's device after EVERY answer (the question order
#               is deterministic, so the whole state is four numbers and nine
#               per-unit counts), offers "Pick up where you left off -- question N of
#               45" on the start panel for 48 hours, clears on finish and on a
#               deliberate fresh start, and discards the save if the question bank
#               itself changed between visits. Same-device only, by design.
#   2026-08-11  APP_BUILD -> "2026-08-11dw-refresher-and-three-bars". TWO MORE OF JIM'S
#               LIVE CATCHES. (1) THE GAP-AWARE OPENER: "welcome back, we were looking
#               at this chart, ready to keep going?" is fine after lunch and useless
#               after four days. The opener branch now computes the days since the
#               last session in THIS course (store.get_course_activity, fail-open)
#               and, at 1+ days, orders a REAL refresher: name the unit and topic,
#               say plainly what you were working on and what they'd already nailed,
#               board the key thing, one gentle memory-jog question -- "a friend
#               catching you up, never a test." (2) THREE BARS, ALWAYS: the TODAY bar
#               was routinely missing on resumed sessions -- the tutor announced no
#               goals, ensure_today_tag can only mirror announced goals, and
#               yesterday's stored goals rightly don't rebuild today. Now the server
#               KNOWS when the bar is empty (today_live) and hands the opener a
#               per-turn ORDER to state the 2-3 item plan and emit [[today items]];
#               session.html additionally shows the labeled TODAY placeholder from
#               the first second, so the wall never has fewer than three maps. Both
#               notes are per-turn dynamic text -- zero static prompt cost.
#   2026-08-11  APP_BUILD -> "2026-08-11dv-sprint-buzzer-shield". JIM'S OWN LIVE CATCH:
#               he answered a sprint's last question exactly as the 60 seconds ended;
#               the timer swapped the panel under his click, the click landed on
#               "Start my lesson ▶" (same screen spot as the answer buttons), and the
#               whole A/B celebration vanished before he saw it. Nothing in this file
#               changed but the stamp: session.html's sprShow() gained a shield --
#               any sprint panel swapped in BY THE TIMER (stretch break, results)
#               keeps its buttons inert and dimmed for 1.2 seconds, so a
#               buzzer-beater click can never dismiss the results. Deliberate-tap
#               panels are unshielded. His sprint DATA was never at risk (the POST
#               fires before the panel can be dismissed) -- what vanished was the
#               celebration, which is half the point of the feature.
#   2026-08-11  APP_BUILD -> "2026-08-11du-retake-and-parent-view". TWO DOORS ON TOP OF
#               dt's FOUNDATION. (1) THE RETAKE BUTTON (Four-Lens student item 2): the
#               dashboard's "Unit Quiz best 62% -- let's get it to 90%" line finally
#               has a button. "📝 Retake the Unit Quiz →" opens /session?...&quiz=1;
#               session.html treats it like the Final-Exam door (no tour, no side
#               offers, welcome button says what it does) and sends the NEW
#               "__unit_quiz__" sentinel; this file turns it into marching orders --
#               administer the focus unit's quiz NOW, remind them the record keeps
#               their BEST (rule 50), never make them ask again; warm-up offered only
#               if the notes show unmet topics. (2) THE PARENT'S ANSWER (parent item
#               6, unlocked by dt): the parent box and the Friday email's per-child
#               section both gain the actual missed problems ("Recently tricky" /
#               "Tricky this week"), max 3, with the child's own answers -- absent
#               entirely when there were none.
#   2026-08-11  APP_BUILD -> "2026-08-11dt-missed-problems". THE DATA FOUNDATION
#               (Four-Lens student item 1, NEW RULE 55): until today a 62% Unit Quiz
#               stored ONLY "62%" -- nobody, including the tutor next session, could
#               see WHICH problems were missed. Now: the tutor reports each miss in
#               the tag (missed="question => their answer | ...", rule 55a -- the
#               tutor is the only one who knows what was asked); /api/quiz,
#               /api/check, and /api/final accept the list via _keep_misses (HONESTLY
#               CLAMPED: never more entries than total-correct, <= 25, fail-open so a
#               malformed list never costs the score); store.quiz_misses keeps the
#               newest 200 per student and joins the reset family day one. Surfaced
#               three ways: NEW GET /api/misses/{code} feeds the dashboard's
#               "Tricky ones" card; _mastery_note hands the last 5 back to the tutor
#               with rule 55(b)'s marching orders (revisit exactly ONE, early, as a
#               fresh similar problem -- spaced retrieval, never a re-test); and the
#               parent's "what did she struggle with?" becomes buildable later from
#               the same rows.
#   2026-08-11  APP_BUILD -> "2026-08-11ds-sprints-anytime-help". TWO STUDENT-LENS FIXES
#               (Four-Lens Review items 3 and 6). (1) HELP THAT WORKS FOR A KID: new
#               /help route + static/help.html, a student-first FAQ (sign-in, mic,
#               sound, "I'm confused" is a power move, nothing is lost on refresh) with
#               a grown-ups section (family page, teacher tool, support address as
#               TEXT a kid can show a parent). app-nav.js's Contact pill -- a mailto:
#               dead on school Chromebooks -- is now ❓ Help -> /help on every app
#               page, and challenge.html (the highest-stakes page, which had NO help
#               affordance at all) gains the same link. (2) SPRINTS ON REQUEST: the
#               dashboard sprint card gains "⚡ Run one now" -> /session?...&sprint=1,
#               which starts the sprint directly; before, sprints were startable ONLY
#               from the lesson-open offer, so a student who skipped it had no way
#               back. Card still hidden until a first sprint exists; parent/teacher
#               view never shows the button; no sprint for the unit fails soft.
#   2026-08-11  APP_BUILD -> "2026-08-11dr-elementary-voice". THE YOUNGEST STUDENTS GET
#               A VOICE (Jim: "I think it's okay for the youngest to have a way to talk
#               as well"). Nothing in this file changed but the stamp: session/practice/
#               topic drop canRecord's !IS_ELEM exclusion (entry/basic students -- the
#               ones least able to type -- get the same tap-to-talk mic as everyone
#               else, with the tap answer buttons unchanged beside it), and prompts.py's
#               how-they-answer note tells the tutor they may speak, with EXTRA
#               transcription charity for young readers. The transcribe/speak pipeline
#               is untouched -- it never cared what course the audio came from.
#   2026-08-11  APP_BUILD -> "2026-08-11dq-family-mission-control". THE LINKS-AND-COPY
#               BATCH (Four-Lens Review, order-of-attack item 1 -- Jim: "fix all the
#               things you found that you think you can fix"). /family becomes
#               MISSION CONTROL: NEW GET /api/parent/overview (parent-token gated,
#               one call) gives each child's real minutes this week, active days,
#               units mastered, last-active, and most-worked course; NEW POST
#               /api/parent/weekly-email is the in-product Friday-report toggle
#               (before: the only switch was the tokenized link inside the email).
#               family.html gains per-child stat lines, a Records link (the
#               homeschool page's "one click from your parent view" is finally
#               TRUE), an inline "How are they doing?" narrative per child, and the
#               email toggle. parents.html drops two promises the product doesn't
#               make (there IS no separate read-only parent code -- the parent door
#               takes the child's code; parent accounts are LIVE, not "rolling out")
#               and points at /family. teachers.html finally links to the real
#               /teacher tool. records.html's bare-visit message points at /family.
#               Marketing-copy discipline going forward: copy ships in the same
#               build as the feature it describes.
#   2026-08-11  APP_BUILD -> "2026-08-11dp-sprints-all-courses". FLUENCY SPRINTS REACH
#               EVERY COURSE. The registry (sprints.py) grows from the 3 elementary
#               courses to ALL TEN -- 70 units with a genuine 60-second recall skill
#               (one-step solves, slopes, factor pairs, special angles, the power
#               rule, Laplace facts...); concept units get no sprint ON PURPOSE.
#               Nothing in this file changed but the stamp: the offer, endpoints,
#               store, and dashboard card were built course-agnostic in dd/dm and
#               light up for the new courses on their own. Every computed answer is
#               formula-derived and the battery's oracle now arithmetic-proves the
#               question shapes; every fixed FACT list (trig values, i-powers, the
#               68-95-99.7 rule, derivatives, identities...) is re-derived from
#               mathematics (sympy/erf/complex) on every battery run. Also fixed in
#               sprints.py, found by this build's probe: negative answers had been
#               starved to a SINGLE tap choice by a no-negatives distractor rule
#               meant for the counting courses (live since dd in prealgebra unit 3).
#               Anxiety rules unchanged: never gates, personal-best only.
#   2026-08-11  APP_BUILD -> "2026-08-11do-prompt-split". THE WORDS AND THE MACHINERY
#               NOW LIVE APART. tutor.py (539 KB) was two-thirds prompt TEXT; all of
#               it moved VERBATIM into the NEW prompts.py (353 KB of pure text, no
#               logic -- the battery now enforces that boundary by AST), leaving
#               tutor.py a 190 KB engine. Proven byte-identical: 52 built prompts
#               (every course x lesson/first-meeting/practice/topic + final modes +
#               standalone constants) hashed before and after -- 52 of 52 equal, so
#               NOTHING the model reads changed and no cached audio or behavior can
#               shift. Nothing in this file changed but the stamp; tutor.py re-exports
#               every moved name, so main.py's imports work untouched. From here on:
#               edit the WORDS in prompts.py, the MACHINERY in tutor.py. NEW FILE
#               prompts.py rides this push.
#   2026-08-11  APP_BUILD -> "2026-08-11dn-modkey-header". THE LAST KEY-IN-A-URL
#               RESIDUAL IS CLOSED. Build dg moved the admin key out of query strings
#               (Render logs them in plaintext) but left one documented residual: the
#               forum-moderation unlock was /community?mod=<key>, and the moderate
#               call carried the key in its JSON body from a URL-sourced variable.
#               Now: POST /api/forum/moderate accepts the key in the X-Admin-Key
#               HEADER (preferred) via the same _require_admin() constant-time gate
#               as every other admin call -- the body key stays ACCEPTED (optional,
#               default "") so nothing breaks mid-deploy, but no page we ship sends
#               it any more. community.html reads the key from sessionStorage
#               ("mt_admin_key", the same stash admin.html fills, so mod mode follows
#               Jim from /admin in the same tab); a legacy ?mod= link is honoured
#               ONCE, stashed, and scrubbed from the address bar. admin.html's
#               moderation quick-link is now plain /community. A wrong/rotated key
#               401s -> the page clears the stash and returns to the public view.
#               Zero prompt characters (the dn lane continues while the prompt-size
#               measurement stays postponed).
#   2026-08-11  APP_BUILD -> "2026-08-11dm-sprint-graph". THE DISPLAY HALF OF WWC g26
#               rec 6 ("track AND SHOW progress") -- the sprints table has recorded
#               every one-minute round since build dd and nothing displayed the
#               growth. NEW GET /api/sprints/{code}?course= (student-gated, whole
#               course history oldest-first, personal best; empty when the DB is off
#               -- the card is a bonus, never a 500) feeding dashboard.html's new
#               hidden-until-data "⚡ Your sprint record" card: two bars per sprint
#               (round A pale, round B solid), a green +n over every self-beat.
#               Rule 42 throughout: the only comparison is this student with this
#               student. Chosen over the prompt-budget work ON PURPOSE: Jim postponed
#               the two-size auditor measurement, so today's builds spend ZERO prompt
#               characters (this one) until that measurement runs.
#   2026-08-11  APP_BUILD -> "2026-08-11dl-wwc-rules". The two strongest remaining
#               evidence gaps close as NEW RULES 53 (number-line doctrine) and 54
#               (word-problem types; key-word shortcuts BANNED and machine-enforced).
#               Nothing in this file changed but the stamp -- the work lives in
#               tutor.py and ruletests.py; RULES.md regenerated (54 rules).
#   2026-08-11  APP_BUILD -> "2026-08-11dk-audit-polish". BATCH E -- the audit
#               re-run's six small accuracy fixes. NOTHING in this file changed but
#               the stamp: rule 48(e) say-it-back + rule 52(d) compute-is-not-this-rule
#               + the new board_notation_conflict referee live in tutor.py; the
#               point-on-a-hole guard in static/math-figures.js; the fraction-slash
#               bridge in notation.py; the fixtures in ruletests.py; RULES.md
#               regenerated (rule 27 -> ENFORCED for the percent-sum shape).
#   2026-08-11  APP_BUILD -> "2026-08-11dj-backups". Jim: "if Render falters or
#               something falters, do we have sufficient backup so that we could
#               recreate everything right away?" The honest audit: code = safe on
#               GitHub; voice cache = recreatable for ~$20 (and since 08-11 it
#               survives deploys on the persistent disk); the DATABASE = no way back
#               at all. Now it has three: (1) NIGHTLY SNAPSHOT -- _backup_pass rides
#               the existing 30-minute heartbeat, writes one gzipped JSON snapshot of
#               every table per day to DATA_DIR/backups (the persistent disk),
#               atomically (.tmp then rename), restart-safe (gates on the newest
#               file's mtime, not process memory), rotated (BACKUP_KEEP, default 14);
#               (2) RENDER'S OWN database backups (paid DB plans -- Jim confirms the
#               plan); (3) THE OFFSITE COPY -- GET /api/admin/backup streams a FRESH
#               snapshot as a download (admin key in the X-Admin-Key header, build-dg
#               discipline), wired to a button on /admin's new 🛟 Backups card, plus
#               GET /api/admin/backup/status for the card's nightly report. THERE IS
#               DELIBERATELY NO RESTORE ENDPOINT -- a remote wipe-and-replace is a
#               foot-gun; restores run offline via the new restore_backup.py with an
#               explicit --yes-i-mean-it flag, inside one transaction. The full drill
#               (bad deploy / lost database / Render gone entirely) is RECOVERY.md;
#               render.yaml was refreshed into a truthful recreation recipe (disk,
#               DATA_DIR, all env names). Export/restore themselves live in store.py.
#   2026-08-11  APP_BUILD -> "2026-08-11di-piecewise". BATCH D of the first full audit
#               (Audit_Findings_2026-08-11.md): the board tools the audit proved
#               missing. NOTHING in this file changed but the stamp -- the work lives in
#               static/math-figures.js (piecewise domains via "for", automatic
#               open/closed endpoint circles, and ⭐ a live bug the new harness caught:
#               hole= had NEVER drawn on a genuine 0/0 removable point, fixed with a
#               numeric limit that also refuses to paint a hole on an asymptote), the
#               three teaching pages ([[column align="last"]] -- the deliberately-wrong
#               last-digit lineup for contrast teaching, byte-identical on all three),
#               tutor.py (the shared tool note), and ruletests.py (PART 3r renders the
#               new figures through the real math-figures.js on every run).
#   2026-08-11  APP_BUILD -> "2026-08-11dh-audit-rules". BATCHES B + C of the first full
#               audit (Audit_Findings_2026-08-11.md). NOTHING in this file changed but
#               the stamp -- the work lives in tutor.py (nine rule additions incl. NEW
#               rule 52; two new referees: rules 17 and 44 move COVERED -> ENFORCED),
#               ruletests.py (their fixtures, quoted from the audit; the three-referee
#               foundation sweep), misconceptions.py (denominator-zero-means-hole; the
#               discriminating-counterexample warning on decimal alignment),
#               notation.py (f(a+1) read as "f of the quantity a plus one"), and
#               lessonaudit.py (the final-exam scenario seeds a real mastery picture;
#               critic discipline checks 4 and 5: the board's capital-letter convention,
#               and decided designs are not findings). RULES.md regenerated -- 52 rules,
#               16 enforced.
#   2026-08-11  APP_BUILD -> "2026-08-11dg-reliability". BATCH A: the first full audit's
#               stumbles were OUR bugs, not rate limits (Audit_Findings_2026-08-11.md,
#               PART 5). The teaching-side fixes live in tutor.py (referee false
#               positives, negotiated continuation, ceiling 1600 -> 3000, empty-reply
#               retry, stand-alone regeneration nudges). THIS file's share is SECURITY:
#               the admin key was riding in QUERY STRINGS ("GET /api/admin/stats?key=..."),
#               and query strings are written into Render's request logs in plaintext.
#               The OpenAI key was protected from exactly this in build cw (PART 3l:
#               Authorization header and nowhere else); the admin key now gets the same
#               discipline. The four admin GET endpoints (/api/beta/list,
#               /api/admin/stats, /api/admin/email-test, /api/admin/digest-test) accept
#               the key in an X-Admin-Key HEADER; admin.html sends it that way and never
#               puts the key in a URL again (unlock stores it in sessionStorage; a legacy
#               ?key= bookmark is honoured once, stashed, and scrubbed from the address
#               bar). The query parameter is still ACCEPTED server-side so nothing Jim
#               has saved breaks, but no page we ship generates it any more.
#               ⚠️ AFTER THIS DEPLOYS, JIM ROTATES FORUM_MOD_KEY IN RENDER -- the old
#               value has been logged and must be treated as burned.
#               KNOWN RESIDUAL, queued: /community?mod=<key> (forum moderation) still
#               carries the key in a URL because community.html has no other unlock;
#               admin.html's moderation quick-link keeps working that way until that
#               page's auth is reworked (its own small build). The /beta quick-link is
#               now PLAIN /beta -- the generator lives on /admin itself since 08-04.
#   2026-08-10  APP_BUILD -> "2026-08-10df-honest-copy". HONEST-COPY SWEEP. Jim: "make
#               sure we don't have anything in here that says evidence based learning as
#               a blanket statement." The sweep proved NO such claim exists anywhere on
#               the site -- the only "evidence" wording is "mastery evidence" in the
#               records/portfolio sense, which is honest and stays. But it caught three
#               stale facts, all fixed in df: (1) courses.html (the PRINTABLE scope &
#               sequence) still said the questioning-method word build cc retired, and
#               (2) still listed the pre-restructure diffeq units; (3) llms.txt (the
#               public AI-crawler summary) claimed unit mastery at "80%+" where the real
#               bar is 90%+ on a ten-question Unit Quiz, and still carried the old
#               MyTutor brand name from before the 08-03 rebrand. NO changes in this
#               file beyond the stamp -- the work lives in courses.html, llms.txt and
#               ruletests.py (PART 3o learns courses.html's ten unit lists; NEW PART 3p
#               bans the retired method word and blanket "evidence-based" from every
#               visible page, llms.txt and README, forever).
#   2026-08-10  APP_BUILD -> "2026-08-10de-diffeq-cupm". DIFFEQ RESTRUCTURED TO THE
#               CUPM MAINSTREAM SYLLABUS. Jim: "go with the one that you feel will be
#               most acceptable to most schools." The MAA/CUPM ODE course study (in
#               D:\MyTutor) describes where mainstream college ODE courses have
#               converged: qualitative analysis (equilibria, phase line, stability) and
#               numerical methods (Euler, Runge-Kutta) are core units now; series
#               solutions have largely moved out; systems get real time including the
#               phase plane and a taste of nonlinear dynamics. Our old syllabus was the
#               older formula-methods sequence. New nine: 1 intro/classification/slope
#               fields, 2 separable+linear (exact = one brief topic), 3 qualitative,
#               4 numerical, 5 homogeneous 2nd-order, 6 nonhomogeneous+vibrations+
#               resonance, 7 Laplace, 8 linear systems/phase plane, 9 nonlinear/
#               linearization. No changes in THIS file beyond the stamp -- the work
#               lives in curriculum.py, tutor.py, pedagogy.py, foundations.py (four new
#               scripts: slope field, equilibrium, Euler's method, eigenvalue),
#               session.html, topic.html. NOTE: unit numbers changed meaning. No live
#               students exist; any old diffeq mastery rows describe the OLD units and
#               would mislead -- acceptable only because we are pre-launch.
#   2026-08-11  APP_BUILD -> "2026-08-11dd-fluency-sprints". THE LARGEST EVIDENCE GAP
#               CLOSED: WWC guide 26 recommendation 6 ("regularly include timed
#               activities", STRONG -- named independently by four sources) -- we had
#               nothing. Format studied from the real Eureka G1M1 Teacher Edition and
#               rebuilt with OUR items (their curriculum is (c) Great Minds, not open):
#               two sibling 60-second rounds, pattern-family sequencing, and the only
#               celebrated number is B minus A -- the student against the student
#               (rule 42, which Eureka's design independently arrived at).
#               Jim's calls: offered at lesson start (one optional link on the welcome
#               card), TAP answers (a timed minute must not measure our transcription
#               latency), full A/B with a stretch break.
#               THIS FILE: GET/POST /api/sprint/{code}. Seeded per student-per-day (a
#               mid-sprint reload rebuilds the SAME sprint; tomorrow's is fresh), history
#               and personal best from the new store table, counts re-clamped server-side.
#               ⚠️ SPRINTS NEVER GATE ANYTHING -- ruletests PART 3n proves it at all
#               three layers, and verifies every one of the 1,620 generated answers.
#               NEW FILE sprints.py (27 units across entry/basic/prealgebra); store.py
#               gains the sprints table (JOINS _STUDENT_CODE_TABLES day one);
#               session.html gains the overlay. The teaching prompt is UNTOUCHED -- the
#               offer is deterministic UI, so the prompt budget paid nothing.
#   2026-08-10  APP_BUILD -> "2026-08-10dc-count-the-stumbles". Jim ran the FULL first
#               audit: ten lessons, nine critic findings. Adjudication is in the project
#               (Audit_Findings_2026-08-10.md): most findings were rejected on the quoted
#               evidence -- including the critic calling our removable-discontinuity
#               graph WRONG (the line y=x+2 with the point removed IS the standard graph
#               of (x^2-4)/(x-2); the transcript derived it two lines earlier) and
#               flagging a missing [[step eq="b = sqrt(64) = ?"]] that is plainly there.
#               ⭐ THE REAL FINDING WAS ONE THE CRITIC CANNOT MAKE: the tutor STUMBLED
#               four times in ten lessons -- graceful-failure turns ("Sorry, I lost my
#               train of thought") a real student would have watched. A content marker
#               reads straight past absence, so counting stumbles is now CODE's job:
#               detected, retried once (a student would repeat themselves), counted, and
#               injected into the report as a reliability finding at fixed severity.
#               "Lost my train of thought" = the model returned EMPTY after retries;
#               "having trouble thinking" = the API call itself failed. Jim: the Render
#               logs from 21:45-22:09 UTC name the underlying errors.
#               The critic's system prompt also gained the three discipline checks its
#               first marking run earned: re-read surrounding turns before flagging,
#               search the reply for your own suggested fix, and correct-under-standard-
#               conventions mathematics is never a finding.
#   2026-08-10  APP_BUILD -> "2026-08-10db-room-to-think". Jim's second key probe came
#               back: gpt-5.5 ✓ (the answer he wanted), and gpt-5.1 marked unusable with
#               "max_tokens or model output limit was reached". THAT LINE WAS MY BUG, and
#               it is a false NEGATIVE worth understanding: a reasoning-family model
#               spends tokens THINKING before it writes a word, and that spending counts
#               against max_completion_tokens -- so my 5-token probe left it no room to
#               think, and an error that PROVES access (the request was accepted, billed
#               and answered) read as no-access.
#               Fix, same philosophy as the parameter swap: the API names the limit that
#               was hit, so take it at its word -- retry once with room to think (4x or
#               +3000 tokens), never guessed from the model name. Also handles the QUIET
#               variant: a 200 with an empty message and finish_reason "length", which
#               would otherwise end a lesson looking like the student walked out.
#               This matters beyond the probe: with OPENAI_AUDIT_MODEL=gpt-5.5, the
#               student turns (120-token budget) would have died the same way.
#   2026-08-10  APP_BUILD -> "2026-08-10da-which-models". Jim, holding a new OpenAI key:
#               "how can I tell if it's for chat five point five?"
#               You cannot tell by looking. A key carries no model list; access belongs to
#               the ORGANISATION, and for a project-scoped key to that project's model
#               permissions. The only honest answer is to ASK THE KEY -- so the tool does.
#               NEW probe_models(): one tiny call per candidate model, reporting which this
#               key can actually reach. Folded into the /admin "① Check my key & price it"
#               button, so one click answers the question for a fraction of a cent without
#               teaching a lesson. A model that needs ORGANISATION VERIFICATION now says
#               so AND gives the remedy (Settings > General > Verify Organisation, photo
#               ID and a live selfie, access about 15 minutes after approval) instead of
#               handing back a 403 for somebody to paste into a search engine.
#               The button no longer claims to be "free": it costs a fraction of a cent
#               and says so. A price for a job that cannot run is worse than no price.
#   2026-08-10  APP_BUILD -> "2026-08-10cz-audit-preflight". Jim ran the lesson auditor
#               for the first time and it failed. Four fixes, three of them mine:
#               (1) OpenAI's newer models reject "max_tokens" and want
#               "max_completion_tokens". The parameter is now NEGOTIATED -- try one, and
#               if the API names the other, switch and remember. Not guessed from the
#               model name: names change, and guessing is how you ship a break.
#               (2) ⭐ A PREFLIGHT. His run spent 89.9 SECONDS AND TWO LIVE TUTOR CALLS
#               before discovering a parameter name. One tiny call now proves the key,
#               the model and the parameter first, for a fraction of a cent.
#               (3) The default model was "gpt-5.5", chosen from a press release rather
#               than from his account. His key reaches gpt-4.1 and gpt-4o; the default is
#               now gpt-4.1, still overridden by OPENAI_AUDIT_MODEL.
#               (4) ⚠️ AN HONESTY BUG IN MY OWN REPORT. It headlined "2 scenarios · 0
#               findings" for a run in which BOTH lessons died before a word was marked.
#               Zero findings and zero lessons marked are OPPOSITE RESULTS and must never
#               read the same. The report and the /admin panel now say "NOTHING WAS
#               MARKED", and the panel repeats the server's summary instead of composing
#               its own.
#               One thing that worked exactly as designed: the error named every model his
#               account can reach, so the diagnosis took seconds. It named them for the
#               wrong reason though -- the check fired on any error containing the word
#               "model" -- so that now fires only on a genuine model error.
#   2026-08-10  APP_BUILD -> "2026-08-10cy-wait-time". No code change in this file -- the
#               stamp moves for the FIFTH REFEREE in tutor.py.
#               From the MAA Instructional Practices Guide Jim added to the tutor folder:
#               teachers wait LESS THAN 1.5 SECONDS before answering their own question;
#               the research says wait SEVEN; and the first thing that improves when you
#               wait is HOW OFTEN A STUDENT SAYS "I DON'T KNOW" (Fuller 1985, Tobin 1987).
#               The guide's vignette is an instructor asking eight questions and answering
#               every one himself a second later. We cannot rush our students -- they
#               answer whenever they like -- but we can rush OURSELVES exactly that way.
#               ⭐ NOT A NEW RULE. Rule 39(b) already says one question per turn and it
#               comes LAST; it has been COVERED since build ce -- written into all ten
#               prompts and never checked. Moving a rule UP A TIER is worth more than
#               writing a new one, and it costs no prompt budget. 39 is now ENFORCED.
#               Also: .gitignore now excludes *.pdf. The evidence base in D:\MyTutor is
#               ~104 MB and growing; it belongs beside the code on Jim's machine, not in
#               the GitHub repo or the image Render builds on every deploy.
#   2026-08-10  APP_BUILD -> "2026-08-10cx-buttons-not-instructions". Jim asked "tell me
#               exactly how to run it", and the honest answer was that he could not.
#               BOTH admin jobs -- the new lesson auditor and the foundation pre-render --
#               were documented as "POST /api/admin/... with {key, dry_run:true}", and
#               nothing in the product can POST JSON. That is why the pre-render had sat
#               UN-RUN FOR DAYS while three handoff documents kept telling him to run it.
#               A control panel whose controls are instructions to use a tool the owner
#               does not have is not a control panel.
#               /admin now has both as buttons: price it (free), then run it. The audit
#               walks its cast two lessons at a time and remembers where it got to, so a
#               long job never becomes one long request, and it has a Copy-the-report
#               button because the report's whole purpose is to be handed to someone.
#               THE GENERAL LESSON, worth more than the buttons: a feature is not shipped
#               when the endpoint answers. It is shipped when the person it was built for
#               can reach it. This file's own change notes have been quietly failing that
#               test since build cf.
#   2026-08-10  APP_BUILD -> "2026-08-10cw-lesson-auditor". Jim: "I need to build some
#               sort of effectiveness/reality check so we don't keep having these
#               problems." NEW FILE lessonaudit.py + POST /api/admin/lesson-audit.
#               Two things check quality today and there is a gap between them:
#               ruletests.py checks the CODE and the WORDS OF THE PROMPT and cannot judge
#               teaching, and Jim reads lessons one at a time, which does not scale past
#               Jim. The auditor closes it: student PERSONAS played by OpenAI take real
#               lessons from the real prompt, then OpenAI marks each transcript against
#               the generated rule index as a picky maths teacher. Ten scenarios, each
#               built around a failure class we have actually been bitten by.
#               ⭐ WE CHOSE THIS OVER LIVE PER-TURN REVIEW, and the reason is the point:
#               every defect found this week was a MISSING SPECIFICATION, not a bad day.
#               A live reviewer catches those sometimes and lets them through next
#               Tuesday; a rule plus a test closes them forever, for free -- and live
#               review would roughly double per-turn cost and put a pause in front of a
#               voice tutor, which is the product.
#               NOTHING IN IT CHANGES THE TEACHING. It returns a report a human reads; a
#               wrong critic quietly sanding down good teaching is the exact failure this
#               is meant to prevent. Admin-key gated because it spends on two APIs, runs
#               on Render because that is where the keys are, dry_run prices it for free,
#               limit/offset walk the cast in batches so no request runs long.
#               NEW ENV VARS: OPENAI_API_KEY (required for a real run) and optional
#               OPENAI_AUDIT_MODEL / AUDIT_TURNS. The key is read, never printed, never
#               returned, never logged -- ruletests PART 3l holds that line.
#   2026-08-10  APP_BUILD -> "2026-08-10cv-holes-windows-and-the-fold". No logic change in
#               this file -- the stamp moves for the four fixes below (tutor.py,
#               foundations.py, math-figures.js, session.html, ruletests.py).
#               (1) Jim, reading a live limits lesson: "it doesn't say WHY there is no
#               value at x = 2, and it completely ignores the graph that continues to the
#               right after x = 2." He is right: y = x^2 has no hole at 2, and the lesson
#               painted one on and asserted it. NEW RULE 51 -- a feature on the board must
#               BELONG to the function, and the student must see where it came from -- plus
#               a canonical calculus script for the removable discontinuity built on
#               f(x) = (x^2-4)/(x-2), where the hole is something they watch appear.
#               (2) ⭐ RENDERING THAT SCRIPT FOUND A SILENT ONE: the [[graph]] docs told
#               the tutor to write range="-1,5" while the renderer's parseRange accepted
#               ONLY "a..b" -- so every comma-framed window was discarded and the graph
#               fell back to -10..10. That instruction exists BECAUSE of Jim's earlier
#               catch that a window "barely showed the parabola", so the fix for that bug
#               had never once worked. parseRange now takes "a..b", "a,b" and "a to b",
#               and ruletests reads its regex out of the renderer and checks every range=
#               we write against it.
#               (3) Jim: "the Welcome back page should never require scrolling. I had to
#               scroll down to see what was my option." The returning card was still
#               carrying the first-timer's three how-it-works bullets; the new-student
#               card overflowed too, at every common laptop size.
#   2026-08-10  APP_BUILD -> "2026-08-10cu-mastery-is-reachable". Jim: "if I pass an exam
#               with an eighty-five, I can go onto the next unit. I can do all the units
#               and still be carrying an eighty-five with me, which is gonna keep me from
#               mastering the final exam... there should be the ability to review and
#               retake that quiz so we can get it up to the mastery level."
#               ⭐ WHAT WE FOUND WAS WORSE THAN THE THING HE DESCRIBED. Mastery is 90% and
#               the Unit Quiz was FOUR OR FIVE questions -- so the only scores it could
#               produce were 80% and 100%. There was no 85, and "mastery = 90%" silently
#               meant a PERFECT PAPER. The topic quizzes had the same defect one floor
#               down: three or four questions against an 80% bar, i.e. four out of four.
#               The bar and the question count lived in different files and moved on
#               different days (the bar went 80 -> 90 on 2026-08-04); no test ever
#               multiplied them together. ruletests PART 3k does that now.
#               HIS DECISIONS: Unit Quiz -> TEN questions (90% = miss one and still
#               master), topic quiz -> FIVE (80% = miss one and still pass); a student may
#               still move on with a unit unmastered, but the tutor now CHASES it (new
#               rule 50); and the locked Final Exam names the units holding it shut.
#               THIS FILE: _final_gate_message() replaces the flat "you've mastered 3 of
#               9" -- it names each unit still open, its best Unit Quiz score, offers the
#               review-and-retake, and says plainly that the record keeps their BEST score
#               so a retake can only ever help. Falls back to the old wording if the
#               record cannot be read: a locked door must never also be a silent one.
#               No stored data changes. store.record_check has always kept the best score,
#               so every retake was already safe -- nobody had been told.
#   2026-08-10  APP_BUILD -> "2026-08-10ct-board-and-all-four-views". Two things from Jim,
#               one of them a live defect he hit in a Basic Math demo lesson:
#               (1) "when the answers popped up, they shortened the whiteboard to the
#               point where I could only see a fraction of what was actually being
#               displayed... maybe instead of four answers stacked on top of each other,
#               one row of four, or two rows of two." The answer buttons were a
#               one-per-line grid and the answer zone could take 47vh; the board is flex,
#               so whatever the answers took, the whiteboard lost. THE REAL CLASSROOM
#               ALREADY SOLVED THIS -- session.html lays its tap-to-answer buttons out as
#               a centred wrapping ROW. The demo now matches it. Measured at 1280x800:
#               board 351px -> 435px, answers 193px -> 109px, four buttons on one row.
#               (2) "I'd like to do that same idea for the homeschool, the teacher, and
#               the student." The teacher and student dashboards got the cs treatment.
#               Homeschool needed nothing: it rides the parent dashboard, so it was
#               finished in cs.
#               THIS FILE: sixteen lines APPENDED to DEMO_VOICE_LINES (211 -> 227) --
#               five teacher stops, four student stops, five for the student DOOR (which
#               was describing the visitor in the third person right after greeting them
#               with "this is your dashboard"), and two for the habit charts. Appended,
#               never inserted: clips are served BY INDEX. About 4,000 characters of new
#               audio, roughly a dollar, once.
#   2026-08-10  APP_BUILD -> "2026-08-10cs-full-parent-dashboard". Jim: "the demo is what
#               is selling this product, and the parent is our number one customer... we
#               have this great dashboard for parents. What we've done with this demo is
#               we created a shortened dashboard that doesn't show much at all with a
#               whole lot of words. I want a fully fleshed out parent dashboard, and I
#               want you to give me a tour of that dashboard."
#               He is right, and the demo's OWN design notes already said so: they
#               specify seven sections for the parent view and it shipped with four.
#               /demo's parent dashboard is now a section-for-section mirror of the real
#               /dashboard?view=parent -- honest read, the read-only parent box with the
#               records link, five tiles with the mastery ring, focus areas, nine units
#               with dates AND scores, the learning journey, the status meter, the trophy
#               case, the courses strip, the placement strengths, the honesty footer.
#               The tour went from 5 stops to 10, and homeschool overrides all 10.
#               THIS FILE: ten lines APPENDED to DEMO_VOICE_LINES (201 -> 211), five
#               parent and five homeschool, byte-identical to demo.html's VOICE_LINES.
#               Appended, never inserted -- clips are served BY INDEX. New audio is about
#               2,500 characters, roughly sixty cents, once.
#   2026-08-10  APP_BUILD -> "2026-08-10cr-one-door-one-dashboard". Jim: "when we go to
#               the homeschool page, the teacher page, the student page, I want that demo
#               to only show the dashboard that's interesting to that particular person.
#               I don't want any links to any other dashboards from there."
#               The three-view chooser belongs to the OPEN demo at /demo, where the
#               visitor asked to see all three. A visitor who came through one door is now
#               locked to it: the ending panel, the "Done" button and the dashboard's own
#               back button all lead to that door's own ending, never to another
#               audience's screen. Not a dead end -- the ending offers the walkthrough
#               again, a real lesson, and the pricing page.
#               THIS FILE: four closing lines APPENDED to DEMO_VOICE_LINES (197 -> 201),
#               one per door, byte-identical to demo.html's VOICE_LINES. Appended, never
#               inserted: clips are served BY INDEX. New audio is about 1,300 characters,
#               roughly thirty cents, once.
#   2026-08-10  APP_BUILD -> "2026-08-10cq-homeschool-walkthrough". Jim walked the
#               homeschool door and hit a bug I put there in cp: "it talks for a long
#               time and says this is the page that your child works from. It's just a
#               blank screen. It stays blank, blank, blank, blank until it gets to the
#               parents' view." Two faults, both mine.
#               (1) ORDER. startAudienceWalkthrough blanked the page and THEN spoke a
#               thirty-second intro before opening the dashboard. Nobody should ever be
#               talked at by an empty screen. The screen goes up FIRST now, the first
#               stop glows, and the words come over the top of something to look at.
#               (2) TAILORING. Homeschool borrowed the parent tour verbatim, so a
#               homeschool visitor heard a parent's script. It now has five stop lines of
#               its own -- Monday morning, one adult teaching several grades, no
#               teacher's aide behind you.
#               THIS FILE: five lines APPENDED to DEMO_VOICE_LINES (192 -> 197). Appended,
#               never inserted: clips are addressed BY INDEX, so anything inserted above
#               them would play the wrong audio under the right words, silently. They are
#               byte-identical to demo.html's VOICE_LINES and PART 3j proves it every run.
#   2026-08-10  APP_BUILD -> "2026-08-10cp-audience-walkthroughs". Jim: the demo "is
#               almost like a video... I would like one of those available, a very
#               obvious button that says view the demo on the parent page, the teacher
#               page, the homeschooling page, and the student page."
#               Four doors into ONE demo: /demo?view=parents|teachers|homeschool|students
#               speaks an intro written for that visitor -- naming the features they came
#               for -- and then runs the matching dashboard's existing narrated tour.
#               Deep-linked rather than rebuilt four times, because copying a tour into
#               four marketing pages is the copy-paste-drift that gave us the build-bk
#               rule bug and the board-wrap bug.
#               THIS FILE: four lines APPENDED to DEMO_VOICE_LINES (188 -> 192). They are
#               addressed BY INDEX, so they go on the END and nothing above them moves;
#               they must stay byte-identical to demo.html's VOICE_LINES, and PART 3j now
#               proves it on every run.
#   2026-08-10  APP_BUILD -> "2026-08-10co-rule-index". No code change in this file.
#               Audit #2 items 23 and 24 shipped: every rule now DECLARES how it is
#               verified (ruletests.py PART 3i, a ratchet -- new drift fails, old debt
#               prints), and `python ruletests.py --rules` generates RULES.md from the
#               prompt itself. Generating it exposed that rules 2, 5 and 8 were checked
#               by nothing at all; 2 and 8 are now enforced by the visual referee.
#               ⚠️ RULES.md is a NEW FILE in the repo (generated, but committed so it can
#               be read on GitHub without running anything).
#   2026-08-10  APP_BUILD -> "2026-08-10cn-scale-and-stability". Jim's brief: quality,
#               low latency, no degradation over time, headroom to keep adding teaching
#               code, ten thousand simultaneous students, build under $1,000.
#               ★ THE DEGRADATION HE DESCRIBED WAS REAL AND IT WAS HERE. Every chat turn
#               loaded the student's ENTIRE conversation, parsed it, appended two
#               messages, re-serialised it and wrote it all back -- to use the last 30.
#               A student a year in was moving several megabytes of JSON per turn, and it
#               got worse every week they came back. MAX_STORED_MESSAGES caps it at 60
#               (double what the tutor reads) via _bounded_history on the one path every
#               save goes through. Nothing the tutor uses is lost; progress, mastery,
#               quizzes, hours and awards live in their own tables. It is also the right
#               privacy posture for a child's conversation.
#               ★ USAGE LOG now purged daily off the existing heartbeat (USAGE_LOG_DAYS,
#                 default 180). ★ RATE BUCKETS now expire by AGE -- the old sweep only
#                 dropped already-empty buckets, so with every bucket busy the table grew
#                 past its cap and never came down. ★ DB POOL sized in store.py.
#               ★ REVERSED BUILD cl. Deferring the wording of heard scripts saved ~6,500
#                 characters a turn and cost a cache rebuild on every flip: about $0.24
#                 an episode to save $0.0005 a turn, plus a slower turn each time. The
#                 prompt is now byte-identical for a whole session. A STABLE prompt beats
#                 a smaller one, and at ~34k tokens we are using 17% of the window.
#   2026-08-10  APP_BUILD -> "2026-08-10cm-cache-discipline". Jim asked whether "cost"
#               meant money or performance. Checking the money side found a real defect
#               I had shipped the build before: the misconception hint was appended into
#               the SYSTEM PROMPT, which is one cached block -- so every turn it fired
#               moved the cache prefix and re-billed ~15,000 tokens (plus a cache write)
#               to deliver a ~195-token note. It now travels as turn_note= on the
#               student's own message, where nothing is cached. Same information to the
#               model, better placed, and the system prompt is byte-identical turn to
#               turn again.
#   2026-08-10  APP_BUILD -> "2026-08-10cl-prompt-budget". Jim on the character ceiling:
#               "we broke the files into sub-files... I don't know if that creates
#               problems or an increased chance of errors. I don't want to have that."
#               MEASURED FIRST. Splitting files does not reduce the prompt at all -- a
#               prompt carries ONE course template, so cross-template duplication costs
#               disk (471 KB) and not prompt (130 KB). And the templates overlap the
#               shared rules by 0%, so there is no duplication left to reclaim anywhere.
#               Every reduction from here removes or defers real teaching content, so
#               exactly one was taken, the one rule 40 already made safe: a script the
#               student has HEARD is offered, not replayed, so its wording only belongs
#               in the prompt on the turn they accept the offer. THIS FILE decides that,
#               reading the student's words and -- because the offer is usually answered
#               with a bare "yes" -- the tutor's previous turn as well. Fails OPEN.
#               6,000-8,000 chars off an ordinary returning-student turn, growing as the
#               student learns more. ruletests now prints a per-block PROMPT BUDGET so
#               the next block's cost is visible before it is paid.
#   2026-08-10  APP_BUILD -> "2026-08-10ck-misconceptions". NEW FILE misconceptions.py
#               (148 catalogued wrong RULES; audit #2 item 2 -- the highest-leverage
#               teaching item left). THIS FILE adds the just-in-time half: before the
#               turn, match what the student JUST said against this course's catalogue
#               and, on a hit, hand the tutor the diagnosis AND the remedy in the same
#               note. Always framed as a possibility he may discard -- a matcher that
#               overrode his own reading of a child would be worse than no matcher
#               (rule 49d/e). Conservative by construction: numbers are never evidence
#               in any spelling, matches are on word boundaries, at most two theories.
#               ⚠️ misconceptions.py MUST be committed with this batch.
#   2026-08-09  APP_BUILD -> "2026-08-09cj-notation-registry". No code change in this
#               file. NEW FILE notation.py -- the single source of truth for every
#               symbol the courses use: how it is written, how it is SAID, and the wrong
#               reading to deny. tutor.py feeds it into every prompt; ruletests.py PART
#               3f fails the build if any board line writes a symbol the registry does
#               not know. ⚠️ notation.py MUST be committed with this batch.
#               ⚠️ Re-run POST /api/admin/prewarm-foundations: three new scripts.
#   2026-08-09  APP_BUILD -> "2026-08-09ci-function-notation". No code change in this
#               file. Jim, live in Algebra I: "it's never been clearly stated to me what
#               f of x is, how to say f of x... and then it flipped over to g of x."
#               It was not the student and not a stale deploy -- the teaching was never
#               written. See foundations.py (five new scripts), tutor.py (rule 48) and
#               ruletests.py (the check that would have caught it).
#               ⚠️ AFTER DEPLOYING, RE-RUN POST /api/admin/prewarm-foundations so the five
#               new scripts are rendered before a student meets them (about 63 cents).
#   2026-08-09  APP_BUILD -> "2026-08-09ch-assessment-honesty" (proactive audit #2, the
#               assessment group: items 9, 10 and 11). No endpoint changed shape; the
#               work is in store.py (the arithmetic), tutor.py (rules 45-47 and a fourth
#               referee) and ruletests.py. These three protect the progress bars, which
#               are the product's central promise: every count here becomes a green bar,
#               a parent dashboard line, and a row in a printable homeschool record.
#   2026-08-09  APP_BUILD -> "2026-08-09cg-todaybar-pendingcheck". Jim's live Pre-Algebra
#               resume, two problems, both of which we had "fixed" before.
#               (1) "There's only two of the three tracking bars across the top. I don't
#               know where the third one is, and I don't know why it keeps disappearing."
#               ROOT CAUSE: the UNIT and COURSE bars survive a page load because the
#               SERVER can rebuild them from mastery data (build br did that for UNIT).
#               The TODAY bar never had a server side at all -- it lived only as a
#               [[today items]] tag the model emitted once, held in browser memory. Any
#               reload or resume wiped it, and it could only return if the model happened
#               to emit the tag again, which on a resumed opener it did not. Worse, the
#               ensure_today_tag() net stood DOWN in exactly that case, because it read
#               "a [[today]] exists earlier in history, so a bar is already up" -- true
#               within one sitting, false the moment the page reloads.
#               FIX, same shape as the other two bars: NEW store table `today_goals`
#               (code, course, day) written by _record_today_bar() from the tutor's own
#               [[today items]] / [[todaydone n]] tags, returned by /api/session as
#               progress.today, and rendered by session.html at load. Ticks MERGE, so a
#               later turn can never un-tick an earned win; a new plan resets them; it is
#               scoped per day so yesterday's goals never show as today's. main.py also
#               now tells tutor.py whether a bar genuinely exists (student["today_live"])
#               instead of letting it guess from history.
#               (2) "It gave me a problem without putting it on the board, and this is the
#               exact example that we've already used once before that was supposedly
#               fixed. And I don't understand why it's not fixed." He is right, and the
#               reason matters: rule 15 does not merely forbid this, it names this exact
#               column-addition scenario and prints the exact fix
#               ([[step eq="dollars: 2 + 1 + 1 = ?"]]), and has since build bm. A rule in
#               a prompt is guidance, not a guarantee. So it became a referee --
#               tutor.prose_pending_question_conflict(), the third check in
#               prose_board_conflict(): ask the student to COMPUTE something and emit no
#               pending "?" line, and the draft is thrown away and rewritten. See tutor.py.
#   2026-08-09  APP_BUILD -> "2026-08-09cf-audit1-closure-audit2-start". TWO JOBS.
#               JOB 1 -- Jim: "take a look at Audit One and make sure we've accomplished
#               all of those." Checked all 25 items of the 2026-08-08 audit against the
#               REAL built prompt for all ten courses and the real source, not memory.
#               24 had shipped. ONE HAD NOT, and it was a live bug: item 11, the fix that
#               stops a long board line WRAPPING mid-equation, went into session.html in
#               build bu and NEVER reached practice.html or topic.html. Jim's original
#               screenshot ("dimes: 7 + 8 + = 16" with "1(carried)" on the next line -- a
#               literally different equation on screen) was still reproducible on two of
#               the three teaching pages. Both pages now have the nowrap CSS and fitRow(),
#               and on ALL THREE pages [[write]] lines are fitted too (they never were).
#               A second gap found the same way: practice and topic were built from
#               GROUND_RULES + GRAPH_TOOL_NOTE only, so rules 36-40 reached them while the
#               canonical scripts those rules refer to did not -- a student could hear one
#               definition of "denominator" in the lesson and a different one on the topic
#               page, which is rule 28 broken at platform scale. Both modes now get the
#               foundation block AND the heard-list (this file wires it at both endpoints
#               and records [[learned]] there too).
#               ruletests.py PART 3e now makes the whole class of bug impossible: the
#               three teaching pages are three copies of one classroom and must match.
#               JOB 2 -- audit #2 "do first". NEW: POST /api/admin/prewarm-foundations
#               (item 21). The TTS cache is keyed by TEXT and starts empty, so the FIRST
#               student to reach each of the 173 scripts pays a live render -- seconds of
#               silence on the exact turn that introduces a new idea. We know all 173
#               strings in advance, so that first student should not be a real child.
#               Admin-key gated, idempotent (an already-cached script is skipped free),
#               dry_run prices it without spending, limit renders in batches, atomic
#               writes so a partial clip is never left behind, and one failure never
#               stops the batch. Dry run today: 173 scripts, 82,856 characters.
#               Rules 41-44 are in tutor.py.
#   2026-08-09  APP_BUILD -> "2026-08-09ce-checkin-memory-visualref". Jim, on the three
#               items from proactive audit #2: "we need to have a cap on how long we talk
#               to an eight year old… I think you need to check in with them every now and
#               then" · "nothing tells him which scripts that student has heard, so a loyal
#               student can re-hear it… we should just query him and say, do you think you
#               got it, or do you want me to refresh your memory?" · "you can't say one
#               thing and then have the numbers say something different."
#               THIS FILE carries half of the second item -- FOUNDATION MEMORY:
#                 _foundations_heard(code, course) reads the student's already-heard
#                   canonical terms out of store and puts them on student_context BEFORE
#                   the turn, which is the only way the tutor can ever know: a new
#                   session's history is empty, so the prompt was previously telling him
#                   to skip an introduction he had no way to identify.
#                 _record_learned(code, course, reply) reads the [[learned term="..."]]
#                   tags rule 40(f) asks him to emit and writes them down AFTER the turn.
#                   Parsing and validation live in foundations.learned_terms_in(), so a
#                   tag naming a script we do not have is DROPPED -- a typo must never
#                   retire an introduction a student still needs -- and ruletests.py can
#                   test that filter without booting the app.
#                 The tag is invisible: every page's stripTags() already removes any
#                   [[...]], so no client change was needed and none was made.
#                 foundations is imported DEFENSIVELY here, exactly as in tutor.py.
#               Both chat call sites (the __open__ opener and the normal turn) record.
#               Rules 39 and 40 and the visual referee are in tutor.py; the table and its
#               reset-cascade entry are in store.py.
#   2026-08-09  APP_BUILD -> "2026-08-09cd-foundation-library". No code change in this
#               file -- the build string moves so /health proves the deploy landed.
#               TWO THINGS SHIPPED, both in files main.py only reads through tutor.py:
#               (1) foundations.py grew from 24 canonical foundation scripts to 173 --
#                   every course now has 17 or 18 verbatim introductions instead of 2.
#                   Jim: "I want you to expand that library of saved script... I'd spend
#                   a hundred dollars on it to make it complete." One-time ElevenLabs
#                   render of all 173 is 82,856 characters -- roughly $12 to $25 at
#                   current per-character rates, then free forever, because _tts_cache_path()
#                   in this file keys the audio cache by the TEXT of the line. Verbatim
#                   scripts are the whole reason that cache can ever hit.
#               (2) ruletests.py PART 3c -- "board tags actually draw". Jim's demo
#                   failure ("the lesson referred to a diagram that didn't show up on
#                   the board... we got one shot to do it right, and it failed") has a
#                   root cause that no exception ever reports: a board tag whose NAME or
#                   ATTRIBUTE the renderer does not read draws nothing (or draws the
#                   wrong picture) in total silence. PART 3c parses math-figures.js,
#                   geo-figures.js and session.html's handleTags() and holds every board
#                   line to what those renderers actually read. On its first run it
#                   caught 11 already-shipped scripts: [[graph expr=...]] (the grapher
#                   reads func=, never expr= -- empty axes), [[numberline from/to/mark]]
#                   (it reads min/max/points), [[triangle a/b/c]] and [[righttriangle
#                   a/b/c]] (they read sides/v and adj/opp/hyp), [[vector x/y]] (reads
#                   v="4,3"), lines="y=x^2" (lines= flattens a parabola to a straight
#                   line), a comma used where the grapher needs a semicolon, and two
#                   [[write]] tags whose square brackets ended the tag early in
#                   handleTags' own regex. All fixed; all 57 figures now re-rendered
#                   through the real renderers and confirmed non-empty.
#   2026-08-09  APP_BUILD -> "2026-08-09cc-foundation-first". ★ PEDAGOGY CHANGE (Jim).
#               We described this classroom as SOCRATIC. That was wrong, and Jim caught
#               it from the inside: "there's no foundation built -- when I'm looking at
#               fractions, I'm not getting what is a fraction, what's a denominator,
#               what's a numerator." The evidence agrees: for NOVICES -- nearly every
#               student on a new topic -- fully guided explicit instruction beats
#               discovery, and a student who "discovers" something wrong remembers the
#               wrong version over the correction (Clark/Kirschner/Sweller); a 2026
#               systematic review of Socratic method in mathematics finds it demands
#               heavy teacher expertise, more time, and depends on prior knowledge the
#               student may not have. So:
#               (1) NEW SHARED RULES 36-38 (all ten courses, verified): 36 teach the
#                   thing before you ask about the thing -- name it, name every part,
#                   define it, worked example, check understanding, THEN questions;
#                   37 vocabulary is taught, never assumed; 38 concrete -> picture ->
#                   symbols, with I-do/we-do/you-do and guidance that FADES as the
#                   student gains competence (never before).
#               (2) The per-course templates no longer say "Socratic" -- they say
#                   foundation-first, and rules 36-38 override any older wording.
#               (3) NEW foundations.py -- CANONICAL FOUNDATION SCRIPTS, 24 of them, the
#                   exact words for each course's foundational terms (what a fraction
#                   IS, what a denominator IS, what a variable IS...). Spoken VERBATIM.
#                   This also answers Jim's cost point directly: the TTS cache is keyed
#                   by the TEXT, so a verbatim script is rendered ONCE for the whole
#                   platform and is free for every student after -- teaching MORE now
#                   costs less, not more. Re-wording it is what costs money.
#               (4) EVERY public page swept: no page claims the Socratic method any
#                   more (landing incl. its JSON-LD twin, mission, homeschool, features,
#                   parents, practice, llms.txt, README).
#               ruletests.py grows to 140 checks incl. a new PART 3b that proves each
#               script reaches its course prompt, is speakable, marks its key term, and
#               that no page has crept back to the old claim.
#   2026-08-09  APP_BUILD -> "2026-08-09cb-firstword-quizretry" (Jim's three questions).
#               (1) THE CLIPPED FIRST WORD, PROPERLY. Leading silence only helps if the
#               OUTPUT DEVICE is awake -- Bluetooth speakers, headphones and many laptop
#               codecs power down after a few seconds of quiet and swallow the first
#               200-400ms while they wake, which is exactly "a word or two", and worst
#               "when he comes back from doing something". Two fixes on all three
#               teaching pages: a truly silent WAV now LOOPS in its own element for as
#               long as the lesson is open (paused when the tab is hidden), so the audio
#               route never sleeps; and the lead is now DYNAMIC -- a clip after >2.5s of
#               silence (or the session's first) gets the full ~840ms pad, >0.9s gets
#               ~560ms, back-to-back clips get ~280ms.
#               (2) FAILED QUIZZES: NEW SHARED RULE 35 (all ten courses). A failed quiz
#               is never re-given on the spot. Name the win, diagnose the ONE or TWO
#               skills underneath the misses, re-teach each with a worked example, and
#               require TWO unaided correct problems on that skill BEFORE offering a
#               retake -- with fresh questions, never the same items. A second failure
#               steps BACK to the prerequisite instead of looping. The word "failed" is
#               never used about the student. ruletests.py gains the coverage check and
#               a live scenario.
#               (3) The parent records report was verified working end to end: /records
#               serves the printable page and /api/records/{code} returns the real hours
#               log, per-course unit progress and awards. No change needed.
#   2026-08-09  APP_BUILD -> "2026-08-09ca-demo-voice-recovery" (Jim's live walk-through,
#               two real bugs -- demo.html only; no server logic changed).
#               (1) ⭐ HIS VOICE WAS LOST MID-DEMO. "I got the mechanical voice from the
#               browser rather than our guy's voice." Cause: `serverVoiceOK` was a
#               ONE-WAY LATCH -- the first clip that failed to load switched the ENTIRE
#               rest of the session to the flat browser voice. That is precisely what
#               the first visitor hits after we append lines: a brand-new clip isn't
#               cached, the server has to generate it, and one slow fetch poisoned
#               everything after it. Now every line tries his real voice, a failure is
#               retried once, only THAT line falls back, a stalled clip gives up after
#               6s, and the server voice is re-tried every fifth line even after
#               repeated failures. Verified: one bad clip, then the next lines are back
#               in his voice.
#               (2) ⭐ STRANDED ON THE TEACHER DASHBOARD. "When I finished the teacher's
#               dashboard, it stopped -- it didn't put the three bubbles up again."
#               The bubbles depended on the audio chain completing, so a stalled clip
#               (bug 1) left the visitor with no way forward but the browser's back
#               button. Now THREE independent things bring the bubbles back and any one
#               is enough: the tour finishing, a hard watchdog armed when the dashboard
#               opens (every stop's estimate + 30s), and a "✓ Done — show the three
#               views" button that is visible the whole time a dashboard is open.
#   2026-08-09  APP_BUILD -> "2026-08-09bz-demo-figures-typed-realdash" (Jim, three things
#               from a live walk-through).
#               (1) THE NUMBER LINE WAS INVISIBLE. The figure SVGs carried a viewBox but
#               no WIDTH, and inside the whiteboard's centred flex column an auto-width
#               SVG collapses to a smudge. Figures now take a real width (max 660px) and
#               a 150px minimum height, with a larger caption.
#               (2) THE DEMO NO LONGER SPEAKS. Jim: "let's just drop the speaking part
#               for the demo." A one-shot sales page should not hang on a microphone
#               permission prompt. All 20 lesson lines re-worded for typing (appended
#               154-173; the mic wording at 115-134 is now unused), the mic UI is gone,
#               and POST /api/demo-transcribe is REMOVED (nothing called it, and an
#               unused endpoint that spends ElevenLabs money is a surface we don't need).
#               Typed answers still accept spoken forms ("two", "negative two").
#               (3) THE DASHBOARDS NOW MATCH THE REAL PRODUCT. Asked directly whether
#               they did, the honest answer was no: the teacher view invented a 9x6
#               mastery grid, per-student coaching reasons, a class-level honest read and
#               time charts, and the parent view invented week/September trend sections.
#               None of that exists. Rebuilt from the real screens: the student view is
#               dashboard.html's real tiles (units mastered · accuracy · problems
#               practiced · time this week · day streak) + where-you-are + quiz results +
#               strengthen next + trophy case + my courses; the teacher view is
#               teacher.html's real class manager (open by class code, per-student units
#               mastered/started with a star, needs-attention flags, open a student
#               read-only, add by student code); the parent view is the same dashboard in
#               parent view (How X is doing + the honest read + the same five numbers +
#               strengthen next + the printable record). Tours rewritten to match
#               (appended 174-187; 135-152 now unused).
#   2026-08-09  APP_BUILD -> "2026-08-09by-demo-button-center-bubbles" (Jim, three small
#               things). (1) A highlighted ORANGE "🎬 Try the demo" pill is now the last
#               item in the marketing nav on every page with a .nav-links row, injected
#               by the shared static/site-nav.js (styled in place if a page already had
#               its own /demo link, and suppressed on /demo itself). features.html had a
#               nav row but never loaded the shared script -- fixed. (2) The three
#               dashboard bubbles now appear CENTERED on the screen in an overlay
#               instead of at the bottom of the page. (3) They are offered again at the
#               END OF EVERY DASHBOARD TOUR, not just after the lesson -- with "let me
#               look around on my own" to dismiss them (the dashboard stays open behind)
#               and a floating "👀 Show the three views" button to bring them back.
#               No voice lines added; no server logic changed (stamp bump only).
#   2026-08-09  APP_BUILD -> "2026-08-09bx-demo-nofailure-dashboards". Jim, on the demo:
#               "we got one shot to do it right, and it failed" -- a lesson referred to a
#               diagram that never appeared (precalc said "welcome to the unit circle"
#               with no circle drawn), and most lessons still told the visitor to TYPE
#               after we moved to voice. ALL TEN LESSONS REBUILT deliberately:
#               every visual a line mentions is DRAWN in that same step (new unit-circle
#               and bar-chart figures; the geometry triangle now carries the ASKED
#               angles, 90/35/?, not the taught ones), every ask is voice-worded, and
#               each course teaches a worked example before asking. A new audit
#               (/tmp-style checks, mirrored in the build) walks all 22 steps and fails
#               the build on any unmatched visual reference or any "type it" language;
#               a second walk plays a plausible SPOKEN answer through every course.
#               THE THREE DASHBOARDS ARE NOW FULL (Jim: "extravagant and very, very
#               thorough"): one invented student, Maya Rivera, 7th grade, with a real
#               record -- 4 units mastered with dates and quiz scores, 312 problems,
#               an 11-day streak, 12 awards, the unit-5 topic ladder, an accuracy trend
#               and a minutes-per-day chart, and her next three sessions. The teacher
#               view gains a 6-student roster, a 9x6 mastery grid, per-student
#               "strengthen next" with reasons, a long honest read, and a time-on-task
#               chart. The parent view gains a plain-English read, the week, the arc
#               since September, everything mastered with dates and scores, what's hard
#               right now WITH the plan, awards, and the printable record. Each is
#               toured in SIX spoken stops (was three).
#               DEMO_VOICE_LINES: 39 APPENDED (115-153); 0-114 untouched.
#   2026-08-09  APP_BUILD -> "2026-08-09bw-demo-voice-dashboards" (Jim's three asks).
#               (1) THE DEMO IS ANSWERED BY TALKING. New POST /api/demo-transcribe --
#               same ElevenLabs engine and the same TRANSCRIBE-AND-DELETE guarantee as
#               /api/transcribe (audio lives only in the request, never disk, never
#               stored), but rate limited BY IP (12 per 5 min) because a demo has no
#               student code. demo.html now shows a real microphone button; spoken
#               answers are normalised client-side ("negative two" -> -2, "one half" ->
#               1/2, "fifty-five degrees" -> 55) before matching. Typing remains one tap
#               away and becomes automatic when a browser can't record or the visitor
#               declines the mic. Elementary courses still TAP (that IS their classroom).
#               (2) TEACH FIRST (rule 19 in the demo): every course opens with a taught
#               example -- a drawn NUMBER LINE for negative numbers, a shaded fraction
#               bar, a labelled triangle, a worked equation -- before any question.
#               (3) THREE DASHBOARDS: after the problem, three big balloons offer the
#               STUDENT, TEACHER and PARENT views; each opens full-screen with sample
#               data and Mr. Cadabra tours it in three spoken stops, then the balloons
#               return so every view stays available.
#               DEMO_VOICE_LINES: 20 APPENDED (95-114); 0-94 untouched so cached audio
#               stays valid; both lists verified identical (115 lines).
#   2026-08-09  APP_BUILD -> "2026-08-09bv-fullpage-demo". Jim: "when they click start
#               the demo, I want them to go to a full page view, and go through the
#               complete tour of the page just like we do with a new student."
#               demo.html: the welcome card stays as the front door, but Start now swaps
#               the window to the REAL classroom layout (left rail with Mr. Cadabra +
#               Curriculum / Course assessment / Progress dashboard / Practice a problem
#               / Explore a topic / Final Exam / Look it up, top bar, goal banner, the
#               three bars, the big whiteboard, the answer zone) and he walks ALL TEN
#               STOPS in the real student-tour order (build bf), each spoken with the
#               matching element glowing + a "look here" tag; the Curriculum list opens
#               for its stop and closes again (build bi). Skippable. After the tour it is
#               unchanged from bt (picker -> scripted intro -> one interactive problem ->
#               spoken congratulations). DEMO_VOICE_LINES: 7 APPENDED (88-94, the sidebar
#               stops); 0-87 untouched so cached audio stays valid; lists verified
#               identical (95 lines) and every spoken string is on the whitelist.
#   2026-08-09  APP_BUILD -> "2026-08-09bu-proactive-rules". Jim: "implement the
#               proactive rules as you see fit" (claude/Proactive_Rules_Audit_2026-08-
#               08.md). No main.py logic changes -- stamp bump only. Shipped:
#               (1) tutor.py shared rules 20-34 (answer handling, board-over-time,
#                   session endings, off-topic + a ⚠️ counsel-queued distress rule,
#                   problem quality, spaced review) -- verified in ALL TEN courses;
#               (2) number-speech rules in all eleven "HOW YOU SPEAK" blocks;
#               (3) forSpeech() on session/practice/topic: negative VALUES, percents,
#                   ratios, common + mixed fractions, thousands separators -- and the
#                   board's Unicode minus now reads as "minus" (a pre-existing gap the
#                   new test battery surfaced);
#               (4) board lines never wrap mid-equation: nowrap cells + fitRow() shrinks
#                   an oversized line to fit (the "7 + 8 + = 16 / 1(carried)" break);
#               (5) ⭐ THE PROSE REFEREE in tutor.py -- catches a reply whose SPOKEN
#                   words contradict its own board (the live 2026-08-08 "fifteen dimes"
#                   bug); narrow by design, fails open, silently regenerates;
#               (6) NEW ruletests.py -- the rule regression battery (51 offline checks
#                   + scripted live student scenarios). Not imported by the app.
#   2026-08-09  APP_BUILD -> "2026-08-09bt-classroom-demo". THE DEMO IS THE CLASSROOM
#               (Jim's redesign): /demo now opens as the real learning board (goal
#               banner + the three progress bars in the real palette + whiteboard +
#               Mr. Cadabra), speaks a welcome, gives a GUIDED TOUR of the screen
#               (board -> bars -> Mr. Cadabra, each stop spoken + glowing, skippable),
#               then the ten-course picker; picking a course plays a scripted INTRO
#               line and runs ONE real problem INTERACTIVELY (type or tap, escalating
#               help on misses -- the regular process, not a movie), ending with a
#               spoken "Congratulations" as the TODAY bar lights its first segment.
#               THE MATH KEYPAD GRID IS GONE from the demo (simple answer bar instead).
#               DEMO_VOICE_LINES: 16 lines APPENDED (indices 72-87: welcome, 3 tour
#               stops, picker invite, 10 course intros, congratulations) -- identical
#               append in demo.html; indices 0-71 untouched so cached audio stays valid.
#   2026-08-08  APP_BUILD -> "2026-08-08bs-worked-example-first". tutor.py only: new
#               shared rule 19 -- every NEW topic opens with a complete worked example
#               (tutor works every step + answer on the board, narrating why), THEN the
#               student tries a similar one ("?"-line), with the example left up until
#               their first success. "I do, then you do" (Jim's rule).
#   2026-08-08  APP_BUILD -> "2026-08-08br-resumebars-pendingline". (1) session.html
#               renders the UNIT bar at page load (curriculum + placement + quiz
#               history) -- no longer waits for [[unitplan]]; a resumed session had
#               shown only the course bar. (2) tutor.py: [[today]] required in the
#               first message of EVERY session (resumes included); rule 15 gains the
#               pending-"?"-line device ([[step eq="dollars: 2 + 1 + 1 = ?"]]) so an
#               asked step is ALWAYS on the board without running ahead.
#   2026-08-08  APP_BUILD -> "2026-08-08bq-check-student-answer". tutor.py only: new
#               rule 18 in the shared precision block -- compute the student's numeric
#               answer before accepting it (wrong answer = coaching, never adopted),
#               and spoken numbers must match the board's numbers in the same reply
#               (Jim's screenshot: "fifteen" accepted for 7+8+1 while the board wrote 16).
#   2026-08-08  APP_BUILD -> "2026-08-08bp-money-speech". "$1.85" was voiced "one dot
#               eight five". forSpeech() on all three teaching pages now reads money as
#               dollars-and-cents and plain decimals as "point" spoken digit by digit;
#               tutor.py HOW YOU SPEAK gains the matching rule. Stamp bump only here.
#   2026-08-08  APP_BUILD -> "2026-08-08bo-todaybar-stepline". tutor.py only (stamp bump):
#               (1) TODAY-bar safety net -- ensure_today_tag() mirrors the opener's own
#               goal items into [[today]] when the model skips the tag (deterministic,
#               lesson-only, never resets a live bar); rule 0(c) requires the tag.
#               (2) Rule 4 sharpened: every answered sub-step gets its own board line
#               before any combined line (the "dollars: 2 + 1 = 3" jump-to-answer catch).
#   2026-08-08  APP_BUILD -> "2026-08-08bn-no-truncated-turns". Jim's live freeze (Basic
#               Math first teaching turn showed only "Let", empty board, lesson stalled):
#               the reply hit tutor.py's 1200-token ceiling mid-tag and nothing checked
#               stop_reason. tutor.py's new _create_full() continues a capped reply via
#               assistant prefill and stitches the pieces (up to 2 continuations);
#               ceiling raised to 1600. Covers lesson + practice + topic. No main.py
#               logic changes (build stamp only).
#   2026-08-08  APP_BUILD -> "2026-08-08bm-yourturn-greenbars". (1) Rule 15 sharpened in
#               tutor.py (live catch: "your turn -- what's ten minus two times three?"
#               was asked with the new problem existing only in the spoken words): the
#               problem handed to the student must be WRITTEN on the board ([[step]]/
#               [[write]]) in the same reply it is asked; only its ANSWER stays off.
#               (2) session.html bars in Jim's palette: light-green card, white unfilled
#               segments, black text (replaces bj's dark-gray card).
#   2026-08-08  APP_BUILD -> "2026-08-08bl-firstwords-thinkflag". Static-only build (all
#               changes in session/practice/topic; bump so /health confirms the deploy).
#               (1) FIRST WORDS CLIPPED (Jim, ongoing): every TTS clip now requests
#               lead=1 (~560ms leading silence via the existing /api/speak lead param;
#               the first clip keeps lead=3) AND a suspended Web-Audio context is
#               resumed before playback starts. (2) THINKING FLAG: a red pulsing
#               "Mr. Cadabra is thinking…" badge mid-whiteboard while he thinks; hidden
#               the moment his voice starts.
#   2026-08-07  APP_BUILD -> "2026-08-07bk-times-sign". Jim's screenshot: "3 + 2 X 4"
#               showed the multiplication x styled as a red variable. Fixed both ways:
#               (1) tutor.py board rules now say WRITE × (or ·) for multiplication,
#               never the letter x; (2) styleVarsCore on session/practice/topic renders a
#               lone x between two numbers as a true × sign, unstyled (coefficients like
#               2x and real variables like "3 + x" untouched). No backend logic changes.
#   2026-08-07  APP_BUILD -> "2026-08-07bj-bars-alltour-contrast". Static-only build (all
#               changes in static/session.html; this bump exists so /health confirms the
#               deploy): (1) the today/unit preview bars now show for the WHOLE welcome
#               tour, from the first word (bi showed them only during the "bars" stop --
#               Jim: "they should all show up right at the beginning"); previews are
#               replaced by the real bars when [[today]]/[[unitplan]] render. (2) Bars
#               contrast rework (Jim: "dark gray, not super dark; the spaces in between
#               should be light"): dark-gray card, light unfilled segments, colored fills.
#   2026-08-07  APP_BUILD -> "2026-08-07bi-tour-smallfixes". THREE TOUR TOUCHES (Jim):
#               (1) the curriculum list the tour opens closes again when the tour moves on
#               (it pushed Mr. Cadabra below the fold); (2) the bars tour stop previews the
#               today/unit bars with labeled placeholders (only the course bar exists
#               before the first lesson turn); (3) the three bars sit on a dark card so
#               they stop washing out on the light page. session.html only; bumped.
#   2026-08-07  APP_BUILD -> "2026-08-07bh-original-restated". RULE 16 SHARPENED (Jim's
#               second live catch: the check question wrote the substituted line but spoke
#               of "the original equation on the board" that had scrolled away). The rule
#               now requires re-writing the ORIGINAL equation itself, labeled, above the
#               check line, and bans the phrase "the original equation" unless this reply
#               shows it. tutor.py only; build bumped.
#   2026-08-07  APP_BUILD -> "2026-08-07bg-tour-polish". TOUR POLISH, FINAL ROUND (Jim):
#               (1) the talk button's emoji mic rendered as a gray "dead fly" on Windows --
#               replaced with a drawn SVG microphone on all three teaching pages;
#               (2) "Type instead" link -> a full-size "Type my answer" button (as big as
#               mic/pause), all student-facing strings updated; (3) NEW tour stop explains
#               the three progress bars (today's goals / unit topics + quiz markers + Unit
#               Quiz flag / nine units marching to the Final Exam), glowing #pbars.
#               Static only; build bumped.
#   2026-08-07  APP_BUILD -> "2026-08-07bf-nav-order". SIDEBAR ORDER + ONE-STOP TOUR (Jim):
#               lesson nav now reads Curriculum → Course assessment → Progress dashboard →
#               Practice a problem → Explore a topic (NEW — the lesson page never had the
#               topic link) → Final Exam → 📖 Look it up. The welcome tour covers each item
#               individually in that exact order (practice + assessment are no longer
#               explained in one breath). session.html only; build bumped.
#   2026-08-07  APP_BUILD -> "2026-08-07be-code-entry". CODE BOX FITS EVERY PASS (Jim pasted
#               a pass verbatim -> "not recognized"; separately his TRY-MESA44 test turned
#               out to be MY sandbox test pass, never on live). index.html's #code/#pcode
#               inputs had maxlength=12 -- but 5 of the 50 beta words make 13-char passes
#               (TRY-JUNIPER42 et al), so a verbatim PASTE silently lost the final digit ->
#               "not recognized" ~10%% of the time. maxlength now 20; inputmode=numeric
#               dropped (beta passes have letters; phones showed a digits-only keyboard).
#               Ships together with bd's forgiving login normalizations.
#   2026-08-07  APP_BUILD -> "2026-08-07bd-forgiving-codes". FORGIVING BETA-CODE LOGIN (Jim:
#               generated a pass, typed it in, "not recognized" -- the lookup demanded the
#               exact TRY-XXXX form). /api/login now retries honest normalizations of the
#               typed code (squash spaces, uppercase, add the TRY- prefix, fix a missing
#               dash) and signs in with the first that IS a real pass. "tiger42",
#               "TRY TIGER42", "try-tiger42" all work now. Pilot and parent-student codes
#               are looked up exactly as typed, unchanged. main.py only; build bumped.
#   2026-08-07  APP_BUILD -> "2026-08-07bc-student-reset". WIPE A PILOT/DEMO STUDENT + BETA-
#               DELETE SAFETY (Jim: "I'll be able to wipe 0000, right?" -- he couldn't:
#               0000 is a pilot persona, not a beta pass and not parent-owned, so neither
#               delete path reached it). (1) NEW POST /api/admin/student-reset (admin key,
#               student code): wipes every per-student row for that ONE code via
#               store.reset_student_data; the code keeps working as brand new (account row
#               re-created on login). 404 for unknown codes so typos never silently
#               "succeed". admin.html's Start Fresh card gained a second row for it (same
#               two-click confirm). (2) SAFETY FIX caught in review: /api/beta/delete's
#               cascade now verifies the pass EXISTS before wiping -- previously a
#               mistyped or pilot code would have its student data erased and THEN get a
#               "no pass with that code" error. Nobody hit it; now nobody can.
#   2026-08-07  APP_BUILD -> "2026-08-07bb-beta-delete". DELETE A BETA ACCOUNT (Jim: "I see
#               how to delete a parent's account by email, but I can't delete a beta
#               account" -- true: revoke only DISABLED the code and left every scrap of its
#               student data). NEW POST /api/beta/delete (admin key): removes the pass row
#               AND all data under that code via store.delete_beta_cascade (one
#               transaction). admin.html + beta.html pass tables gained a "delete" button
#               (two-click confirm) next to revoke; revoked rows can now be deleted too, so
#               the list can finally be cleaned. BONUS FIX: final_exams joined the student
#               wipe list, so parent resets also remove exam rows (table was born today).
#   2026-08-07  APP_BUILD -> "2026-08-07ba-start-at-one". UNPLACED STUDENTS START AT UNIT 1
#               (Jim's dashboard catch, confirming a parked question: a brand-new unplaced
#               Demo student was steered to Unit 2 "Addition to 20" with Unit 1 "Counting &
#               Number Sense" never touched). Root cause: chat()'s tracking fallback was a
#               flat "default Unit 2 if unplaced" -- the first turn logged "learning Unit
#               2", the mastery note then told the tutor to FOCUS there, snowball. Now:
#               unplaced activity counts toward the student's FIRST UNMASTERED unit (fresh
#               student = Unit 1); placed students unchanged; focus_unit still overrides.
#               tutor.py rule 1 companion line: no placement + no mastery data = the course
#               path starts at UNIT 1, never assume a fresh student skips ahead.
#               NOTE (same conversation): most of the other dashboard oddities Jim saw were
#               NOT bugs -- the shared demo/test code is a persistent student that remembers
#               every prior test run (AI batteries included). Use admin Start Fresh before
#               serious walk-throughs.
#   2026-08-07  APP_BUILD -> "2026-08-07az-no-self-answer". RULE 17 (Jim's live catch:
#               "five yummy cookies: how many cookies do you see?"). tutor.py's shared
#               rules block gained rule 17 -- a reply that asks a question must never state
#               or hint at its own answer (counting questions never name the count; recaps
#               name the topic, not the pending answer). tutor.py only; build bumped.
#   2026-08-07  APP_BUILD -> "2026-08-07ay-follow-fix2". FOLLOW FIX ROUND 2 (Jim, on the ax
#               build: Basic-Math cookies still hid below the fold). Root cause: the pages'
#               OWN anchor-scroll fired a scroll event the listener mistook for the student
#               scrolling away -> following disabled -> when the tap-to-answer row shrank
#               the transcript, the re-anchor was skipped. New autoScroll flag: only a REAL
#               student scroll releases following. Verified against the exact event
#               sequence in a node simulation. Static only; build bumped.
#   2026-08-07  APP_BUILD -> "2026-08-07ax-follow-turn". TRANSCRIPT FOLLOWS THE TURN (Jim,
#               first Entry-Level lesson: "the whiteboard disappears below and I have to
#               scroll constantly"). All three teaching pages: every new bubble re-engages
#               auto-follow; a tutor turn TALLER than the window anchors the view to the
#               START of the turn (words + board in view) instead of pinning to the bottom
#               (which shoved the bubble off the top); short turns still pin to the bottom.
#               Static only; build bumped for deploy verification.
#   2026-08-07  APP_BUILD -> "2026-08-07aw-pause-chips". PAUSE RESTORED + LIBRARY CHIPS
#               (Jim). (1) The ⏸ Pause button is BACK on all three teaching pages
#               (reverses this morning's removal -- with the tutor talking so much, the
#               student needs a way to stop him mid-sentence): pauses the voice, holds the
#               turn (mic + sends disabled while paused), Resume continues the sentence.
#               (2) 📖 Look it up now opens with CONTEXT CHIPS -- choices drawn from what's
#               being taught right now (the tutor's bolded key terms newest-first, the unit
#               bar's topic ladder, today's goal, the practice problem / explored topic) --
#               plus "✏️ Something else…" which reveals the type-your-own box. Students who
#               don't know what to call a thing can just tap it. Static only; build bumped.
#   2026-08-07  APP_BUILD -> "2026-08-07av-graph-holes". GRAPH HOLES + "SQUARED" (Jim's live
#               catches in Calculus): (1) [[graph]] gained hole="a" (math-figures.js draws
#               an open red-ringed circle on the first curve; tutor.py docs + BOARD HONESTY
#               rule extended: a spoken hole/asymptote/feature must be DRAWN, and the window
#               framed so it's visible with room on both sides). (2) forSpeech() on all
#               three teaching pages converts ² ³ π θ ± ≥ ≤ ≠ ° to spoken words -- the voice
#               was reading "x²" as "x two". Static + prompt only; build bumped.
#   2026-08-07  APP_BUILD -> "2026-08-07au-course-path". RESUME CHOICE + LIBRARY IN THE TOUR
#               (Jim's live catch: he explored a MID-COURSE geometry topic, came back, and
#               "Continue my lesson" resumed the side-trip -- "I don't have a way to get
#               back to the beginning where I want to be").
#               (1) The welcome-back overlay now offers TWO buttons: "▶️ Continue where I
#                   left off" (unchanged) and NEW "🧭 Take me to my course path — Unit N",
#                   where N = the first unmastered unit from the server's mastery data
#                   (falls back to Unit 1 for a fresh course, Unit 9 if all mastered). The
#                   choice sets the focus unit and sends the NEW "__open_fresh__" sentinel:
#                   the opener is told NOT to recap/resume the side work -- welcome briefly,
#                   then the full opening sequence for that unit.
#               (2) The introductory tour gained a stop for the 📖 Look it up button
#                   (library.js injects it before the tour runs), so new students learn the
#                   reference library exists. session.html only + this note; build bumped.
#   2026-08-07  APP_BUILD -> "2026-08-07at-quiet-invite". TWO LIVE CATCHES (Jim's screenshot):
#               (1) QUIET ASSESSMENT INVITATION, PROPERLY THIS TIME. The 08-06 "card shows
#                   alone, silent, opaque" design lived only in session.html and was LOST
#                   when the runaway 08-06 chat rebuilt that file from a stale copy.
#                   Restored + hardened: offerAssessment() no longer speaks/bubbles/status;
#                   #assessInvite backdrop is OPAQUE; and NEW decline sentinels
#                   ("__open_declined__" / "__tour_done_declined__") tell the opener the
#                   card was answered "not right now" -- the tutor is instructed the
#                   question is ASKED AND ANSWERED and must not re-offer it (the old bug:
#                   student clicked no, the spoken welcome asked again).
#               (2) RULE 16 (tutor.py): a substitution/"check it" question must re-write
#                   its full equation on the board in the SAME reply -- Jim's screenshot
#                   showed "plug 4 back into two x plus five equals thirteen" spoken with
#                   only "x = 4" on the board.
#   2026-08-07  APP_BUILD -> "2026-08-07as-lookitup". THE LOOK-IT-UP LIBRARY (Jim: "a
#               searchable database covering all the topics of all the courses" -- a stuck
#               student types e.g. "binomial theorem" or "adding dollars and cents" and a
#               readable bubble opens; the tutor's voice and the chat are never involved).
#               NEW module library.py: 15 curated seed articles (aliases + fuzzy matching,
#               4 reading-level bands from the course id) + a GENERATE-ONCE fallback (one
#               strict-prompted model call for an unmatched topic, scrubbed to a safe HTML
#               subset, saved forever to the NEW store table `library_articles` -- the
#               library fills itself with what students actually ask; off-topic searches
#               refuse cleanly). NEW endpoint GET /api/library?q&course&code (students
#               only; 30 lookups / 6 generations per 5 min). NEW static/library.js: the
#               shared 📖 Look it up button (left nav) + search overlay + article bubble,
#               included on session + practice + topic. DB off -> seeds still work,
#               generated articles serve but don't persist.
#   2026-08-07  APP_BUILD -> "2026-08-07ar-champion". COURSE CHAMPION MEDAL, DIPLOMA REMOVED
#               (Jim: "a diploma implies a California-recognized school, and we are not one").
#               (1) REMOVED the GET /diploma route (the printable Certificate of Completion)
#                   and every diploma link/mention in session.html + tutor.py's final-exam
#                   prompts. Never reintroduce credential-style documents (diploma /
#                   certificate / transcript) without counsel -- they read as accreditation.
#                   (The honest homeschool RECORDS report is unaffected -- it's a log, not a
#                   credential.)
#               (2) ADDED the reward in its place: AWARD_DEFS "champion" (🏅 Course Champion,
#                   "Passed a course Final Exam") -- computed in awards_state from
#                   store.get_final_exam(course).passed per active course, persists like
#                   every award, appears in the dashboard trophy case + the NEW! celebration
#                   + the tutor's 48-hour congratulation note automatically (all generic
#                   AWARD_DEFS plumbing). students.html award catalog updated to match.
#               store.final_exams and its passed_at stamp are unchanged (now simply the date
#               the course was conquered). Exam flow, gate, and bars unchanged.
#   2026-08-07  APP_BUILD -> "2026-08-07aq-progress-finals". PROGRESS BARS + FINAL EXAM (Jim:
#               a nervous student should always SEE where they are; and a real course final).
#               (1) PROGRESS BARS (lesson page): three thin bars under the goal banner --
#                   TODAY (the opener's 2-3 goals; the tutor lights segments with the new
#                   [[today]]/[[todaydone]] tags as the student demonstrates each), UNIT (the
#                   unit's topic ladder from the new [[unitplan]] tag, with a 📝 quiz marker
#                   per topic + the 🏁 Unit Quiz at the end; passed quizzes light from the
#                   existing [[quiz]] tags + server history), COURSE (nine unit segments, gold
#                   when mastered, ending at the 🎓 Final Exam). /api/session now returns a
#                   `progress` object (mastered units, unit-quiz bests, topic quizzes, final
#                   state) so the bars are honest on load, not just live.
#               (2) FINAL EXAM, HARD-GATED (Jim's rule: prep AND exam only for students who
#                   mastered ALL 9 units at 90%). New: _final_exam_state() +
#                   FINAL_GATE_MESSAGE; ChatRequest.final ("prep"|"exam") re-verified
#                   SERVER-SIDE every turn (ineligible -> gate message, no paid call);
#                   tutor.py appends the prep/exam prompt note only after that check.
#                   POST /api/final/{code} records the [[finalexam]] score (gate-checked
#                   again; store.record_final_exam stamps passed_at once at >= 90%).
#                   GET /diploma?code&course -- printable Course Diploma, served only after
#                   a passed final. Prep = optional overview; exam = 18 questions, no hints.
#               New store table final_exams (see store.py). Nothing existing removed.
#   2026-08-07  APP_BUILD -> "2026-08-07ap-opening-order". OPENING SEQUENCE FIXED ORDER (Jim's
#               live check on Pre-Algebra: greeting, warm-up question, and THEN the goals card
#               and numbers -- backwards). tutor.py's SESSION_OPENER_RULES gained rule 0: every
#               course's first message is greeting (course welcome on a first visit) -> today's
#               topic -> today's goal + goals card -> "Ready to get started?" and STOP; the
#               first problem comes next turn, board-first. The 08-03 version of this fix was
#               elementary-only -- now universal. tutor.py only; build bumped for deploy verify.
#   2026-08-07  APP_BUILD -> "2026-08-07ao-voice-everywhere". VOICE-FIRST CLASSROOM (Jim: "back
#               to the conversational back-and-forth between the teacher and the student
#               everywhere"). Mostly a STATIC build (server changes: this note, the build id,
#               a /api/transcribe docstring update, and the Stripe product description):
#               (1) practice.html + topic.html: voice input restored (canRecord is a real
#                   capability check again, matching session.html's 2026-08-06 restore).
#               (2) MIC-HIDING BUG FIXED: math-keyboard.js still force-hid #talkBtn at
#                   DOMContentLoaded (its 2026-07-30 "type-in tier" lines), silently undoing
#                   the 2026-08-06 restore on session.html -- the mic button never actually
#                   appeared. Those lines are removed.
#               (3) 🧮 Math Keyboard RETIRED app-wide (math-keyboard.js now only provides the
#                   Enter ⏎ button + answer-bar layout; keeps its filename so includes don't
#                   404). ⏸ Pause and the Yes/No/I'm confused/Hint quick buttons REMOVED on
#                   all three teaching pages -- the student just SAYS it. KEPT: typing
#                   fallback everywhere, elementary tap-to-answer, 📈 graph tool, Enter ⏎.
#               (4) tutor.py: GRAPH_TOOL_NOTE rewritten (student talks now; transcription
#                   read charitably; no math-keyboard mentions). help-tips.js tips updated.
#               (5) "No microphone, ever" marketing/privacy claims SWEPT site-wide (landing,
#                   features, homeschool, parents, teachers, pricing, mission, privacy,
#                   llms.txt, README): new story = student talks with the tutor; voice is
#                   transcribed to text and the audio is deleted immediately, never stored.
#                   Stripe product description updated (also fixed stale "8 courses" -> ten).
#               NOTE: demo.html + DEMO_VOICE_LINES deliberately UNTOUCHED (the scripted demo
#               still types on its scripted keypad; the voice-line list is append-only).
#               ⚖️ Attorney follow-up: confirm transcribe-and-delete meets the COPPA audio
#               exemption; add voice-in (ElevenLabs Scribe) to the privacy policy + DPA set.
#   2026-08-06  APP_BUILD -> "2026-08-06an-voicein". VOICE INPUT RESTORED (Jim). The tap-to-talk
#               flow (dormant since 2026-08-01's "no microphone" master switch) is back on:
#               session.html's canRecord is a real capability check again (ON for typing courses
#               on browsers that can record; OFF for elementary tap-to-answer + unsupported
#               browsers, which type). The student taps 🎙️ → speaks → the audio posts to the
#               EXISTING /api/transcribe (ElevenLabs Scribe; unchanged, still code-gated + rate-
#               limited + hallucination-scrubbed). "Type instead" stays available everywhere.
#               No server code change beyond a docstring accuracy fix. FOLLOW-UP (Jim): the
#               "no microphone, ever" claims across marketing + privacy pages must be reworked
#               to match — separate task, flagged in the handoff.
#   2026-08-06  APP_BUILD -> "2026-08-06am-homeschoolvideo". Jim's new 77-second homeschool page
#               video embedded under the hero on /homeschool (static/videos/homeschool.mp4 +
#               homeschool-poster.jpg; controls + poster; "Homeschool Video Played" Plausible
#               event on first play — mirrors the teachers video). Frame-checked brand-correct.
#               Static assets + one page; build bumped for deploy verification.
#   2026-08-06  APP_BUILD -> "2026-08-06al-navhome". NAV: "How it works" -> "Home" on all 12
#               marketing pages (Jim: the old first nav item scrolled cold visitors straight
#               past the new hero to the four-steps section; it now opens the TOP of the
#               landing page; marked "here" on the landing page itself). The hero's "See how
#               it works" button still scrolls to #how. Static-only; build bumped for deploy
#               verification.
#   2026-08-05  APP_BUILD -> "2026-08-05ak-tencourses-pulse". LANDING (Jim): (1) the "Hear him
#               teach" button now PULSES (radiating ring, CSS-only, stops on click, off under
#               prefers-reduced-motion) -- "it needs to catch my eye". (2) The courses section
#               was still living in the eight-course era: heading said "middle school through
#               calculus" and Entry-Level Math + Basic Math were missing from the chips. Now
#               "first grade through calculus and beyond" with all TEN courses -- and the same
#               fix in the meta/og/twitter descriptions and JSON-LD blurb. landing.html only.
#   2026-08-05  APP_BUILD -> "2026-08-05aj-hearhim-breathe". TWO LANDING ITEMS (Jim green-lit the
#               remaining design-review quick wins):
#               (1) "🔊 HEAR HIM TEACH" -- a button on the hero whiteboard plays ONE fixed line
#               of Mr. Cadabra's real voice on click (browsers allow audio after a click). The
#               line is APPENDED to DEMO_VOICE_LINES (index 71; identical append in demo.html's
#               VOICE_LINES -- the lists stay in sync, append-only) and served by the existing
#               /api/demo-audio/{i} whitelist + cache; the robot's mouth animates while it
#               plays. Fallbacks: no ElevenLabs key (204) or any error -> the button becomes an
#               honest "Hear him in the demo →" link. No new endpoint; no server change beyond
#               the appended line.
#               (2) BREATHING-ROOM PASS (landing.html): hero lede split into two short
#               paragraphs (same words); the product-screenshots section (#see) moved UP to
#               sit right after "Why families choose" (show, then tell); section padding,
#               heading margins, and line-heights opened up. Copy unchanged throughout.
#   2026-08-05  APP_BUILD -> "2026-08-05ai-heroalign". HERO LESSON RIGOR (Jim: the hero skipped
#               the both-sides step the real classroom shows). static/landing.html only: the
#               hero board now writes the operation row under BOTH sides (   − 1  − 1) before
#               the result line, equals signs column-aligned (white-space:pre), bubbles use the
#               both-sides teaching language. Static no-JS board updated to match. No server
#               change; build bumped for deploy verification.
#   2026-08-05  APP_BUILD -> "2026-08-05ah-herolive". LIVE HERO LESSON (outside design review:
#               "the site tells more than it shows"). static/landing.html only: the hero
#               whiteboard mock now teaches a ~14s scripted mini-lesson on a loop — bubble asks,
#               student reply pill answers, board draws each step, robot face talks/smiles in
#               sync. No video, no new requests; static board preserved for no-JS and
#               prefers-reduced-motion. No server change; build bumped for deploy verification.
#   2026-08-05  APP_BUILD -> "2026-08-05ag-featuresaccordion". FEATURES PAGE: ACCORDION REDESIGN
#               (Jim: "more visible without scrolling so far -- make everything a drop-down and
#               fit it at the top of the page"). static/features.html only: all 30 features are
#               now compact click-to-expand rows (native <details>/<summary>, no JS) in TWO
#               balanced columns (15 rows each side); page height dropped from ~4 screens to
#               under 2, with The Teaching and Proof fully visible on the first screen. All
#               titles + descriptions unchanged from build af. No server change; build bumped
#               for deploy verification.
#   2026-08-05  APP_BUILD -> "2026-08-05af-featuresplus". FEATURES PAGE: SIX MORE CARDS (Jim).
#               static/features.html only -- The Teaching 6->9 (Practice mode / Explore a topic /
#               a tutor who remembers you), Proof 6->9 ("How am I doing?" one click / progress
#               persists across devices / streaks build the habit), and two cards strengthened
#               (assessment card now promises the tailored PLAN; weekly-email card names TIME
#               SPENT). Sections stay multiples of three. No route or server change; build
#               bumped for deploy verification.
#   2026-08-05  APP_BUILD -> "2026-08-05ae-featurespage". FEATURES PAGE LIVE (Jim approved the
#               draft): new static/features.html (six sections x three cards, everything real,
#               DRAFT ribbon removed) served at NEW route GET /features. NAV REORDER on every
#               marketing page (Jim: "homeschool, students, parents, teachers are the four
#               demographics we sell to -- get Courses out from between them, and put Features
#               right after Our mission"): the top-nav link order is now How it works · Our
#               mission · Features · Courses · Homeschool · Students · Parents · Teachers ·
#               Community · Pricing · Contact (page extras like Privacy/FAQ keep their spots at
#               the end; the college-math dropdown still follows Courses -- site-nav.js finds it
#               by href, not position). Routes otherwise unchanged.
#   2026-08-05  APP_BUILD -> "2026-08-05ad-assessinvite". ASSESSMENT INVITATION (Jim: when a
#               student joins a course for the FIRST time, welcome + tour as before, then warmly
#               ENCOURAGE the Course Assessment -- "find your strengths, see where to focus, and
#               I'll build a plan just for you" -- never forced; the 2026-07-28 removal of the
#               forced redirect stands). Static-only change in session.html: a spoken invitation
#               + choice card (take the assessment / start at Unit 1) shown right after the tour
#               for brand-new students, and before the opener for toured students entering a new
#               course; only when the course has no history AND no placement. Declining continues
#               the exact old flow. No server route changed; build bumped for deploy verification.
#   2026-08-05  APP_BUILD -> "2026-08-05ac-opsalerts". OPS ALERTING (pre-launch readiness review:
#               "you should learn about a broken API key from an alert, not from a parent" --
#               the one Tier-2 audit item never built). THREE pieces, all additive:
#               (1) GLOBAL ERROR HANDLER: any unhandled exception on any route now (a) prints to
#               the Render log as before, (b) is recorded to the new store.error_log table, and
#               (c) EMAILS JIM -- throttled to at most one email per error-kind per hour so a
#               crash loop can't flood the inbox. The caller gets a warm JSON 500 instead of a
#               bare stack trace. HTTPExceptions (normal 4xx "please sign in" answers) are NOT
#               errors and don't trip any of this.
#               (2) COST WATCHDOG: the existing 30-min scheduler loop now also checks estimated
#               spend over the trailing 24h (same math as /admin's cost panel) and emails Jim
#               when it crosses COST_ALERT_USD (env, dollars; unset = watchdog off). Throttled
#               to one alert per ~20h. Never guesses: silent unless the price env vars are set.
#               (3) /api/admin/stats now returns errors24 (count) + errors_recent (newest 20),
#               and /admin shows an Errors tile + a recent-errors table when there are any.
#               New env (all optional): ALERT_EMAIL (where alerts go; defaults to SMTP_USER),
#               COST_ALERT_USD (daily-spend alarm threshold), ALERT_THROTTLE_MIN (default 60).
#               Alert emails ride the existing WORKING smtp pipe (_send_email) on a background
#               thread -- an alert can never slow or crash a student's lesson.
#   2026-08-05  APP_BUILD -> "2026-08-05ab-freshreset". ADMIN "START FRESH" (Jim: a button to fully
#               reset ONE parent account by email so he can walk the brand-new-parent signup with
#               his own address, without the site recognizing him). NEW admin-only endpoint
#               POST /api/admin/parent-reset {key, email}: same FORUM_MOD_KEY gate as every other
#               admin tool; looks up the parent by that exact email and, via new
#               store.delete_parent_cascade(), atomically deletes THAT one parent + their children
#               + all per-student/per-parent rows. Touches no other account; never touches the
#               admin key or any env var. 404s (harmlessly) if no account exists for the email.
#               The /admin page gained a gated "Start fresh" card (two-click confirm) that calls
#               this and then clears THIS browser's mt_parent_token so /family opens as a stranger.
#               No existing route/behavior changed -- purely additive.
#   2026-08-04  APP_BUILD -> "2026-08-04aa-demohelp". DEMO ESCALATING HELP (Jim deliberately
#               failed a demo problem repeatedly and only ever got the same "try again" hint —
#               the scripted demo was failing the exact test skeptical parents run: does the
#               tutor ADAPT?). demo.html now escalates: miss 1 = the hint · miss 2 = "let's
#               look at it a different way" + the worked solution revealed on the board ·
#               miss 3 = show the answer warmly, note the real classroom keeps trying new
#               ways until it clicks, and move on. THREE new fixed lines APPENDED to
#               DEMO_VOICE_LINES (kept IDENTICAL to demo.html's VOICE_LINES; appended so
#               existing demo-audio cache indices stay valid).
#   2026-08-04  APP_BUILD -> "2026-08-04z-records". HOMESCHOOL RECORDS PAGE (Jim: the
#               homeschool page promises records -- "do they have a page where they can
#               download the required records?"). Now they do: /records?code=X is a printable
#               report (browser print -> paper or PDF): summary tiles, the honest hours log
#               day-by-day with per-course breakdown over a chosen range (30/90/180/365 days),
#               progress by course (placement, unit statuses, topic quizzes passed, Unit Quiz
#               best, mastered at 90%), and awards with dates. Data: NEW GET
#               /api/records/{code}?days=N (store.get_time_between + the same per-course unit
#               logic as /api/topics). Linked from the dashboard's parent/teacher box and the
#               homeschool page's records section. Honest by design: engaged minutes only,
#               real scores only, and the report itself notes that state rules differ.
#   2026-08-04  APP_BUILD -> "2026-08-04y-quizzes". QUIZZES (Jim): (1) TOPIC QUIZZES -- each
#               unit's topics are now a ladder with a short quiz (3-4 Qs) as the rung between
#               topics; PASSING (80%+, store.QUIZ_PASS_PCT) is how the student earns the next
#               topic. The tutor runs them conversationally and emits a new hidden tag
#               [[quiz unit topic name correct total]]; the pages show a "Quiz" result card and
#               POST the score to the new /api/quiz/{code} (-> store.record_topic_quiz).
#               Gating persists across sessions because _mastery_note now tells the tutor which
#               topic quizzes are passed per unit ("resume at the first unpassed topic; don't
#               re-quiz passed ones"). (2) The end-of-unit check is now called the "UNIT QUIZ"
#               everywhere students and parents see it (tag/API unchanged: [[check]] ->
#               /api/check). Mastery still = 90% (store.PASS_PCT). (3) /api/topics now returns
#               each unit's quiz rows ({name, best_pct, passed}) + quizzes_passed so the
#               dashboard (student AND the parent/teacher read-only views) shows quiz results.
#               (4) STRAY-80 FIXES from the build-w sweep: the in-lesson result card said "Unit
#               mastered!" at 80% on session/practice/topic pages, and teacher.html's heatmap
#               starred at 80 -- all four now use the honest 90. Also fixed practice.html's
#               check POST which omitted `course` (practice checks mis-filed under Algebra I).
#   2026-08-04  APP_BUILD -> "2026-08-04x-weeklymail". THE WEEKLY PARENT EMAIL -- the one
#               feature the site promised ("A weekly report in your inbox... every Friday")
#               that was still unbuilt. Assembled from parts that already existed: the SMTP
#               pipe (_send_email, proven by password resets), the windowed week numbers
#               (NEW store.week_activity), and the SAME parent-voice writing engine as the
#               dashboard's "How are they doing, really?" (tutor.get_assessment, audience
#               "parent" -- exactly what the landing page promised: "the same analytical
#               summary"). HOW IT WORKS: a daemon thread wakes every 30 minutes; in the
#               Friday send window (20:00-23:59 UTC = Friday afternoon/evening US) it sends
#               each due parent (has children, not opted out, nothing sent in the last 3
#               days) one plain-text email: per child, the week's real minutes/days, checks
#               taken (with the honest 90% mastery bar), new awards, streak -- plus the AI
#               summary for the child's most-worked course (skipped gracefully if the AI
#               errors; the numbers still go out). Zero-activity children get a gentle
#               nudge line, never guilt. CAN-SPAM hygiene: every email carries a one-click
#               unsubscribe link (random token, grants ONLY unsubscribe -- new GET
#               /api/parent/weekly-email/unsubscribe, with resubscribe), a reason line, and
#               the support address. Admin: GET /api/admin/digest-test?key=&email= builds a
#               real parent's digest and returns it as JSON WITHOUT sending (add &to= to
#               send one copy for eyeballing). Env: WEEKLY_EMAIL=off disables the scheduler;
#               sends require SMTP_* set (already live). PAGES: parents/homeschool/landing
#               weekly-email copy un-futured ("coming with launch" -> it exists now), and the
#               preview mock's "Mastered ... 84%" corrected to 92% (below the new 90% bar).
#   2026-08-04  APP_BUILD -> "2026-08-04w-mastery90". THREE OF JIM'S CHANGES: (1) MASTERY = 90%
#               now, everywhere -- store.PASS_PCT is the single source (all six hardcoded ">= 80"
#               mastery checks here now read store.PASS_PCT); tutor prompts, dashboard/teacher/
#               admin/students/teachers page texts updated; all screenshots re-shot since the old
#               captions ("80%+") were baked into the pixels. (2) NEW "GRADUATE" honor: finishing
#               a WHOLE course now renders as a 🎓 "Graduate — <Course>" trophy (was the generic
#               🏆 "Course completed" tile) -- computed live from all-9-units-mastered, so it
#               upgrades/downgrades honestly with the new bar. (3) lesson.png re-shot: it still
#               showed the old purple-sphere Mr. Cadabra in the header and speaker spots; the new
#               shot has the official logo header + robot speaker (it is also the og:image
#               everywhere, incl. the parents/teachers pages Jim saw it on).
#   2026-08-04  APP_BUILD -> "2026-08-04v-teachervideo". FIRST PAGE VIDEO (static-only; bump for
#               deploy verification). Jim's teachers video ("Rev A 8.3.26", 69s, 3MB, brand-
#               correct, built from the current screenshots) embedded on /teachers under the
#               hero: poster frame, controls, preload=metadata, playsinline, no autoplay;
#               fires a "Teacher Video Played" Plausible event once on first play. Files:
#               static/videos/teachers.mp4 + teachers-poster.jpg (new static/videos/ folder).
#   2026-08-04  APP_BUILD -> "2026-08-04u-brand". OFFICIAL LOGO (static-only; bump for deploy
#               verification). Jim delivered the brand deck ("Teachers_Video_Deck Rev 2 by SE"):
#               its gradient endpoints are #6C5AE5->#1FB5B0 -- within one shade of the site's
#               existing --purple/--teal, so NO recolor was needed (the deck was built FROM the
#               site palette). Incorporated the genuinely new piece: the logo -- a navy grid of
#               rounded squares with one golden starred tile -- rebuilt as a clean vector
#               (static/brand-mark.svg; colors #15357C/#FFC511 sampled from the deck's pixels),
#               swapped in for the purple orb dot in every nav/footer brand spot (14 pages) and
#               as the favicon. The robot face still represents Mr. Cadabra HIMSELF wherever he
#               speaks (demo speaker, hero mock, classrooms) -- logo = company, robot = him.
#   2026-08-04  APP_BUILD -> "2026-08-04t-mailfunnel". TWO ITEMS (Jim): (1) EMAIL DIAGNOSTICS --
#               his reset email never arrived. Likeliest cause: the account email is
#               jim+test@shift-work.com and forgot-password (by anti-probing design) silently
#               sends nothing for addresses without accounts. To make the pipe debuggable either
#               way: _send_email() now RETURNS the exact failure text instead of just false; a
#               new admin-only GET /api/admin/email-test?key=&to= sends a real test email and
#               reports the precise SMTP error (config shown WITHOUT the password); the forgot
#               endpoint now logs no-account / send-failure outcomes to the server log (never to
#               the caller). (2) PLAUSIBLE FUNNEL GOALS (Measurement plan #2) -- frontend fires
#               five named events (Demo Level Picked / Demo Completed / Parent Signup / Checkout
#               Started / Subscribed) via a tiny mtTrack helper in analytics.js; demo.html +
#               family.html instrumented. Cookieless, no personal data, COPPA-clean. Jim adds
#               the five goals in the Plausible dashboard to see funnel conversion.
#   2026-08-04  APP_BUILD -> "2026-08-04s-heroface". LANDING HERO ROBOT (static-only; bump for
#               deploy verification). The hero whiteboard mock still showed the old purple sphere
#               as Mr. Cadabra; it now draws his real robot face (shared tutor-face.js, gently
#               animated, sphere fallback if the script fails). Hero paragraph also now mentions
#               elementary tap-to-answer alongside typing.
#   2026-08-04  APP_BUILD -> "2026-08-04r-faq". FAQ OVERHAUL on the landing page (static-only;
#               bump for deploy verification). Jim's review caught three stale answers (no
#               Anthropic/Claude mention, "answers by typing" ignoring elementary tap-to-answer,
#               eight courses instead of ten); rewrote those and added four new questions (math
#               verified by a real engine, math-only guardrails, cost incl. family plan, devices).
#               Both the visible FAQ and the JSON-LD FAQPage schema regenerated from one list.
#   2026-08-04  APP_BUILD -> "2026-08-04q-pwreset". PASSWORD RESET + SIGN-IN FIXES (Jim tried
#               to create an account with an email that already had one and the form silently
#               flipped tabs). Backend half: (1) _send_email() -- the app's FIRST outbound
#               email, via the existing Titan mailbox over SMTP; needs env vars in Render:
#               SMTP_HOST=smtp.titan.email, SMTP_PORT=465, SMTP_USER=support@mrcadabra.com,
#               SMTP_PASS=<the mailbox password> (optional SMTP_FROM; APP_BASE_URL defaults to
#               https://mrcadabra.com). Until they are set, forgot-password answers honestly
#               that email isn't wired up and points at support@. This same pipe will later
#               carry the weekly parent email. (2) POST /api/parent/forgot -- ALWAYS answers
#               "sent" whether or not the email has an account (no probing which emails exist);
#               rate-limited per IP and per address; emails a 45-minute single-use link built
#               from a token whose HASH alone is stored. (3) POST /api/parent/reset -- redeems
#               the token, sets the new PBKDF2 hash, and signs the parent out of every device.
#               Frontend half in family.html (409 message no longer swallowed, eyeball,
#               forgot/reset forms).
#   2026-08-04  APP_BUILD -> "2026-08-04p-demoface". DEMO POLISH x3 (Jim; static-only, bump for
#               deploy verification): (1) the demo now shows Mr. Cadabra's ROBOT FACE (same
#               tutor-face.js as every classroom page) instead of a plain sphere -- mouth moves
#               while speaking, teal glow highlights him, happy face on right answers, sphere
#               kept as fallback; (2) the demo math keyboard states it is NOT a calculator;
#               (3) after a wrong check, the next key tapped REPLACES the stale answer
#               (backspace still edits it one character at a time).
#   2026-08-04  APP_BUILD -> "2026-08-04o-familyclarity". FAMILY PAGE CLARITY (static-only; bump
#               for deploy verification). Jim, seeing /family as a new parent: "HARBOR60 -- what
#               IS that? I think it's a password but I don't know for sure." The code chip is now
#               labeled LOGIN CODE - TAP TO COPY; add-a-child says a NICKNAME is fine (real name
#               not needed -- data minimization); the empty state walks the 3 steps in order.
#   2026-08-04  APP_BUILD -> "2026-08-04n-tencourses". PRICING TRUTH PASS (static-only; bump for
#               deploy verification). Jim's screenshot caught the landing pricing section stale:
#               "All 8 courses" (there are TEN since 2026-08-03), the old "ask about multi-student
#               pricing" family card (the real plan: one seat covers 2 kids, 2nd free), and the
#               Free card's "Start free" button sending people to /demo instead of the real free
#               signup at /family. Fixed on landing + the stray "eight"s on pricing (incl.
#               JSON-LD), homeschool, beta, community.
#   2026-08-04  APP_BUILD -> "2026-08-04m-costlog". MEASUREMENT #1 (Jim: "let's get started on
#               the measurement"). Every paid event is now RECORDED (counts only, never text):
#               tutor turns log their real token consumption + verifier verdict (tutor.py does
#               the logging; the four call sites here now pass the student code through), and
#               _tts_stream_response() logs every voice request's character count + whether the
#               audio cache served it free (speak + demo). /api/admin/stats now also returns
#               usage7/usage30 aggregates with estimated DOLLARS -- computed ONLY when the price
#               env vars are set (ANTHROPIC_IN_USD_PER_MTOK, ANTHROPIC_OUT_USD_PER_MTOK,
#               ELEVEN_USD_PER_1K_CHARS in Render); with no prices set it reports raw counts and
#               null dollars -- honest metrics, nothing invented. /admin renders the new section.
#   2026-08-03  APP_BUILD -> "2026-08-03l-shots". PRODUCT-SCREENSHOT REFRESH + two dashboard CSS
#               fixes (all static; bump is for deploy verification). Jim spotted the teachers-page
#               heatmap image cut off at the bottom; an audit of ALL six product screenshots found:
#               lesson.png still said "MyTutor" (it is the og:image for every page AND on the
#               landing/students pages), and dashboard/dashboard-full/parent.png were each clipped
#               mid-content. All five re-captured from the live pages (teacher.png was fixed
#               earlier today). dashboard.html also gained two real fixes the shots exposed: the
#               KPI ring no longer covers the "UNITS MASTERED" label, and the page title no longer
#               breaks mid-word next to the nav pills. landing.html alt text updated to match.
#   2026-08-03  APP_BUILD -> "2026-08-03k-ipad". iPAD/TABLET READINESS PASS -- all changes are in
#               the static pages (no backend code changed; this bump exists so the deploy can be
#               verified at /health). challenge.html + demo.html: audio was silent on iPads (audio
#               must first play INSIDE a tap; challenge awaited a fetch first, demo made a new
#               Audio element per line) -- both now unlock one shared element inside the first tap.
#               practice/topic/session: type-box 16px (stops iPad zoom-on-focus), 100dvh layout
#               (composer can't hide behind Safari's toolbar), 44px quick buttons.
#   2026-08-03  APP_BUILD -> "2026-08-03j-mathverify". THE MATH VERIFIER (Jim's pick): every
#               tutor reply is now re-checked by a real math engine (SymPy) before the student
#               sees it. The work lives in tutor.py (_create_verified + prompt rules 10-12) and
#               the NEW mathcheck.py; sympy was added to requirements.txt. main.py itself needed
#               NO code changes (the three /api/chat|practice|topic endpoints already call
#               tutor.get_*_reply, which now verify internally) -- this is the build bump only.
#   2026-08-03  APP_BUILD -> "2026-08-03i-demolevels". TEN-LEVEL DEMO (Jim): /demo now opens with
#               a level picker (all ten courses, Entry-Level Math -> Differential Equations); each
#               level runs a short scripted sample -- the elementary two answer by TAPPING (like
#               the real elementary classroom), the rest keep the math keyboard. DEMO_VOICE_LINES
#               regenerated FROM THE SAME SOURCE as demo.html's VOICE_LINES (build-verified
#               identical); the original 13 lines are unchanged so their cached audio is reused,
#               and each new line costs ElevenLabs once ever.
#   2026-08-03  APP_BUILD -> "2026-08-03h-boardprimary". BOARD IS THE LESSON (Jim: "words are the
#               backup; overutilize the whiteboard, not underutilize -- at ALL levels"). tutor.py's
#               shared GRAPH_TOOL_NOTE (prepended to EVERY course x lesson/practice/topic) gained
#               rules 7-9: never ask a student to imagine what the toolkit can draw; show CHANGE
#               (before + the change) instead of describing it; and the sound-off check -- every
#               reply must be followable with the audio muted. [[objects]] gained add="n"
#               (⭐⭐⭐⭐⭐ + ⭐) on session/practice/topic. No route changes.
#   2026-08-03  APP_BUILD -> "2026-08-03g-firstwords". THREE playtest fixes (Jim): (1) FIRST-WORDS
#               CLIP: /api/speak gained `lead` (0-4 extra ~280ms silence blocks); pages send lead=3
#               on the FIRST clip of a session, because audio outputs (esp. Bluetooth) close during
#               the thinking wait and eat the head of the first clip -- now they eat silence.
#               (2) OPENING PACING (tutor.py): the elementary opener now does welcome + goal + plan
#               card + a ready-check ONLY -- the first problem waits for the child's reply, board
#               first. (3) NEW [[objects]] board tag (session/practice/topic.html) draws countable
#               emoji rows so the tutor SHOWS five stars instead of asking a child to imagine them.
#   2026-08-03  APP_BUILD -> "2026-08-03f-elemguard". ELEMENTARY GUARDRAILS + ANSWER-BAR ELEM MODE.
#               No logic change in this file: tutor.py gained the "stay inside this course" wall and
#               the board-first-buttons-second rule (playtest: persona notes about algebra made
#               Entry-Level Math teach equations); students.json personas are now COURSE-NEUTRAL so
#               any persona can demo any course; session/practice/topic.html hide the typing gear
#               (Math Keyboard/Graph/"Two ways to answer" + their ? bubbles) for entry/basic and show
#               a tap-friendly hint + placeholder instead. Stamp bump so /health proves the deploy.
#   2026-08-03  APP_BUILD -> "2026-08-03e-elemtour". TOUR PER CLASSROOM TYPE (Jim's playtest: an
#               already-toured demo code got NO welcome/tour in Entry-Level Math and went straight
#               into a problem). The `toured` flag from /api/session is now computed per classroom
#               GROUP: the elementary tap-to-answer courses (entry/basic) count separately from the
#               typing courses, via _tour_group() + a `courses` filter on _has_any_history (DB and
#               JSON paths). So a student's FIRST elementary lesson always gets the full intro --
#               Mr. Cadabra's welcome, the "what math is" opener, the screen tour with the
#               tap-to-answer stop -- even if they toured a typing course before, and vice versa.
#               session.html also gained &tour=1 to force-replay the tour for demos/testing.
#   2026-08-03  APP_BUILD -> "2026-08-03d-cadabra". REBRAND (Jim): the product is now
#               "Mr. Cadabra's Classroom" everywhere a user can see -- all static pages (titles,
#               meta/OG, nav brands, body copy, footers), the beta-pass message, the demo line,
#               the forum fallback author (now just "A parent"), and the Stripe product display
#               name ("Mr. Cadabra's Classroom — Full access"; the finder matches the old
#               "MyTutor Full access" name too and renames it, so no duplicate product is created;
#               the internal price lookup_keys mytutor_monthly/annual are UNCHANGED on purpose --
#               they are invisible IDs and changing them would orphan existing prices).
#               "Hyperion Shift LLC" remains ONLY on /privacy and /terms (legal entity must be
#               named there) and as the invisible legalName in the landing page's structured data.
#               Same deploy: elementary welcome/tour now describe TAP-TO-ANSWER buttons instead of
#               the keyboard (session.html), and the chat pages re-pin the transcript when the
#               choice buttons appear so the tutor's words never slip out of view.
#   2026-08-03  APP_BUILD -> "2026-08-03c-tapanswers". TAP-TO-ANSWER for the elementary courses
#               (Jim: little kids can't type -- give them multiple-choice answers to click). New
#               [[choices]] whiteboard tag rendered by session/practice/topic.html as big tappable
#               answer buttons (+ an automatic "I'm not sure" button); tutor.py's elementary brain
#               and the entry/basic practice/topic scopes now emit it for every question with a
#               specific expected answer. Typing stays as a backup. No changes in this file beyond
#               the stamp -- the tag flows through the existing /api/chat reply path untouched.
#   2026-08-03  APP_BUILD -> "2026-08-03b-elemcourses". ELEMENTARY RESTRUCTURE (Jim): TWO new
#               courses BELOW Pre-Algebra -- ENTRY-LEVEL MATH (grades 1-3) and BASIC MATH (grades
#               4-6) -- each a full peer (9 units, 45-Q assessment, lesson/practice/topic). All the
#               work is in curriculum.py, pedagogy.py, tutor.py and the front-end course maps
#               (challenge/topic/session/home/dashboard/teacher + /courses catalog); main.py itself
#               only bumps the stamp, because course selection is data-driven off curriculum.COURSES
#               (which now includes "entry"/"basic"), so every /session /practice /topic /challenge
#               /dashboard route already accepts them via ?course=. ALSO: a shared static/site-nav.js
#               adds a "College level math" dropdown (Calculus, Differential Equations) to the
#               marketing top nav. No route changes; nothing removed.
#   2026-08-03  APP_BUILD -> "2026-08-03a-adminfamily". TWO features for Jim:
#               (1) FAMILY PLAN -- one paid plan now covers UP TO TWO children. New
#               KIDS_PER_SEAT=2 constant + _seats_for()/_covered_count() helpers; coverage in
#               _student_tier + _parent_payload now uses seats*2 (oldest kids covered first);
#               billing_checkout/billing_cover buy ceil(kids/2) seats so a 2nd child is free
#               and a 3rd child adds a plan (Stripe prorates). Pricing/family copy reworded to
#               "covers up to 2 children" (static/pricing.html, static/family.html). No harm to
#               Stripe checkout/portal/webhook, the free gate, or add-a-child.
#               (2) ADMIN DASHBOARD -- new /admin page (static/admin.html) + GET /api/admin/stats,
#               protected by the existing FORUM_MOD_KEY. One place for live signup/subscription/
#               engagement/beta/forum/health numbers (store.admin_stats(), aggregate counts only --
#               no names/emails/codes), the beta pass generator built in, and quick links.
#   2026-08-02  APP_BUILD -> "2026-08-02a-discovery". AI SEARCH + GOOGLE DISCOVERY (Jim):
#               new routes /robots.txt (welcomes Google + AI crawlers, hides app pages),
#               /sitemap.xml (all 13 public pages), /llms.txt (plain-text product summary
#               for AI assistants) -- files live in static/. Companion change: every public
#               page gained canonical + Open Graph/Twitter tags and schema.org JSON-LD
#               (org/product/FAQ on landing, course list on /courses, offers on /pricing).
#   2026-08-01  APP_BUILD -> "2026-08-01h-boardleads". BOARD LEADS, WORDS FOLLOW (Jim): the
#               tutor was speaking equations and arithmetic checks entirely in words while
#               the whiteboard sat empty. tutor.py's GRAPH_TOOL_NOTE gained rules 4-6: all
#               spoken math must be written on the board in symbols in the same reply, and
#               spoken text points at the board instead of narrating symbols. Prompt-only
#               change; this bump exists so /health proves the new prompt is deployed.
#   2026-08-01  APP_BUILD -> "2026-08-01g-keyterms". DETERMINISTIC first-use key-term bolding
#               (_bold_first_terms + KEY_TERMS, ~60 curated terms): the live audit showed the
#               prompt rule alone misses passing first mentions, so the server now guarantees
#               it on every chat/practice/topic reply -- skipping [[tags]], prior-turn terms,
#               and anything already bolded. Board-honesty rules added to GRAPH_TOOL_NOTE.
#   2026-08-01  APP_BUILD -> "2026-08-01f-terms180". KEY TERMS + STRAIGHT LINES (Jim's beta
#               run, round 2): GROUND_RULES tells the tutor to wrap first-use key terms in
#               **asterisks**; session/practice/topic render them bold red (.kterm). The
#               [[angle]] figure now allows deg=180 (the 175 cap was silently bending the
#               straight lines supplementary-angle lessons describe).
#   2026-08-01  APP_BUILD -> "2026-08-01e-voicefit" (Jim's beta-route test). (1) FIRST-WORD
#               CLIPPING: every TTS clip is now served with ~280ms of leading MP3 silence
#               (matching ElevenLabs' format) so slow audio outputs swallow silence, not the
#               first word. (2) POST-TOUR OPENER: new __tour_done__ sentinel -- after the
#               screen tour, the opener explicitly must NOT re-introduce Mr. Cadabra by name
#               (the tour just did); it bridges straight into the course big idea + goals.
#               (3) tutor.py opener rules: when asking the student to pick from a shown card,
#               SAY WHERE THE LIST IS and repeat 1-2 examples aloud -- no vague 'those'.
#   2026-08-01  APP_BUILD -> "2026-08-01d-howami". NARRATIVE ASSESSMENTS (Jim's long-term
#               vision: tailored, human, honest). GET /api/assessment/{code}?course&audience:
#               gathers ONLY real recorded facts (_assessment_facts: placement, per-unit
#               mastery with real check scores, practice, accuracy, streak, engaged minutes
#               over 14 days, awards, other-course activity) and has tutor.get_assessment()
#               write ONE warm honest paragraph -- student voice or parent voice. 30-min
#               in-memory cache per (code, course, audience) + 8/hr/code rate limit keeps
#               cost tiny. Dashboard gained the "How am I doing?" button (parent view asks
#               "How are they doing, really?"). The same engine will write the weekly
#               emails when those ship.
#   2026-08-01  APP_BUILD -> "2026-08-01c-onetour". (1) ONE SCREEN TOUR PER STUDENT: /api/
#               session returns `toured` = store.has_any_history(code) (any course; JSON
#               fallback scans the sessions file) -- switching courses no longer replays the
#               tour. (2) Math Keyboard sheet gained a 'this isn't a calculator -- it TYPES
#               into your answer' caption + the answer-bar reminder now names the TWO ways
#               to answer (static/math-keyboard.js). (3) Lesson sidebar hint now truthfully
#               says the answer box is at the BOTTOM of the screen.
#   2026-08-01  APP_BUILD -> "2026-08-01b-demofix". DEMO MADE REPRESENTATIVE (Jim's playtest:
#               the demo showed multiple-choice taps, but the real product has NO multiple
#               choice anywhere -- students type with the math keyboard). DEMO_VOICE_LINES
#               updated in lockstep with demo.html's VOICE_LINES: intro + first question are
#               now ONE line (the redundant "Okay, let's go" click is gone) and both concept
#               questions say "type your move". List shrank 14 -> 13 entries; audio for new
#               lines is generated+cached on first play, same as before.
#   2026-08-01  APP_BUILD -> "2026-08-01a-betastamp" (Jim: the live site looked like it takes
#               payment, but Stripe is in test mode -- "we are not taking payment at this
#               time"). NEW _payments_open(): payments count as OPEN only when the Stripe key
#               is a LIVE key (sk_live_...); test/no key = beta mode automatically, no sticker
#               to forget. billing_ready in /api/parent/me now reflects it (the /family page
#               swaps subscribe buttons for an honest beta notice), and checkout/portal/cover
#               all refuse politely with a beta message. Env override PAYMENTS_OPEN=open|closed
#               for deliberate demos. Pricing page gained a visible amber beta stamp.
#   2026-07-31  APP_BUILD -> "2026-07-31q-beta". BETA-TESTER PROGRAM (Jim: "five free logins
#               for approved beta testers... works five times... only stays open an hour or
#               two"). NEW route /beta (public pitch + mailto application; ?admin=<key> shows
#               Jim's pass generator). A beta pass (TRY-XXXX, store.beta_codes) grants FULL
#               access: each /api/login consumes one of its uses (default 5) and opens a timed
#               window (default 2h); sign-ins during an open window ride free (race-guarded);
#               progress is keyed to the pass so testers continue across days. _lookup_student
#               honors a pass only while its window is open; _student_or_404 explains expiry
#               kindly ("sign in again -- N of 5 left" / "pass used up, thanks!") instead of a
#               bare 404, and /api/login returns beta flags so the login page can greet
#               testers with their remaining count. Admin: /api/beta/create|list|revoke,
#               keyed on FORUM_MOD_KEY (constant-time compare). Marketing pages gained a slim
#               gradient BETA RIBBON under the header -> /beta.
#   2026-07-31  APP_BUILD -> "2026-07-31p-community". MISSION PAGE + COMMUNITY FORUM + HEADER v2.
#               (1) NEW route /mission (static mission.html: fun / accessible / complete / taught
#                   right -- every claim on it is something the product really does).
#               (2) NEW route /community + forum API: GET /api/forum/{section} and
#                   /api/forum/post/{id} are PUBLIC reads; POST /api/forum/post|reply require a
#                   signed-in parent token (parents post, students never; author = parent's first
#                   name or "A MyTutor parent"; title<=140, body<=4000; rate-limited 6/10min per
#                   parent + 12/10min per IP). POST /api/forum/moderate (FORUM_MOD_KEY env,
#                   constant-time compare) soft-deletes a post/reply -- hides, never destroys.
#                   Four sections: working / ideas / resources / courses.
#               (3) HEADER v2 on every marketing page + /family: spacious two-row bar (brand +
#                   buttons up top, centered links below) after Jim found the one-row fix still
#                   cramped; nav + footers gained "Our mission" and "Community" links.
#   2026-07-31  APP_BUILD -> "2026-07-31o-taxcode". FIX found in Jim's live sandbox test: new
#               Stripe accounts enable "Managed Payments" by default, which REQUIRES a tax code
#               on every product -- checkout returned "the product tax code is missing". The
#               product is now created with PRODUCT_TAX_CODE (txcd_10000000, "General --
#               Electronically Supplied Services"; override via STRIPE_TAX_CODE env var), and
#               _ensure_product_tax_code() heals the product that was already created without
#               one. An accountant can refine the classification later without a code change.
#   2026-07-31  APP_BUILD -> "2026-07-31n-accounts". REAL PARENT ACCOUNTS + STRIPE BILLING +
#               FREE-PLAN GATE (the payments foundation, built with Jim step by step).
#               (1) ACCOUNTS: POST /api/parent/signup|login|logout, GET /api/parent/me,
#                   POST /api/parent/students. Email + password (PBKDF2-SHA256, 390k iters,
#                   per-account salt, constant-time compare, timing-decoy on unknown emails;
#                   the password itself is NEVER stored or logged). Sign-in issues a 30-day
#                   random token (X-Parent-Token header). Children are FIRST NAMES ONLY and
#                   get friendly codes (MAPLE42-style, collision-checked vs students.json +
#                   accounts). Signup 5/hr/IP, login 20/5min/IP. All parent/billing endpoints
#                   require the database (503 with a clear message otherwise -- accounts must
#                   not live in throwaway JSON). NEW route /family serves the portal page.
#               (2) STUDENT LOOKUP: _lookup_student() -- students.json personas first (pilot,
#                   unchanged forever), then DB accounts with a parent_id. Every existing
#                   endpoint (chat/dashboard/awards/heartbeat/voice) works for family students
#                   with no other change.
#               (3) BILLING (cards NEVER touch this server): POST /api/billing/checkout ->
#                   Stripe-hosted Checkout (monthly $29 / annual $288 per student, quantity =
#                   number of children; prices found-or-created in Stripe by lookup_key so no
#                   dashboard clicking); /api/billing/portal -> Stripe's hosted manage/cancel
#                   page; /api/billing/cover -> prorated quantity bump after adding a child.
#                   POST /api/stripe/webhook (signature-verified via STRIPE_WEBHOOK_SECRET;
#                   payload re-parsed as plain JSON because SDK wrapper shapes drift between
#                   versions) is the ONLY writer of subscription state. Env: STRIPE_SECRET_KEY,
#                   STRIPE_WEBHOOK_SECRET, optional SITE_URL. Without keys: friendly 503s and
#                   the portal shows "payments launching soon" instead of dead buttons.
#               (4) FREE-PLAN GATE (_student_tier/_free_gate in /api/chat, BEFORE the paid
#                   Claude call): free = placement + FIRST mastered unit + unlimited practice/
#                   topic help; after their first mastered unit a free student gets a warm
#                   upgrade note, never an error. Oldest children are covered first, so adding
#                   a child never bumps a paying one to free. Pilot codes are never gated.
#   2026-07-30  APP_BUILD -> "2026-07-30m-parents". NEW route /parents serving the parent trust
#               page (what the child experiences / what the parent sees / privacy promises /
#               3-step start). "For parents" tab added to nav + footer across the marketing site.
#   2026-07-30  APP_BUILD -> "2026-07-30l-rewards". STUDENT REWARD SYSTEM + FOR-STUDENTS PAGE.
#               (1) NEW GET /api/awards/{code}: merit badges (one per mastered unit, per course),
#                   course trophies (all 9 units mastered), and effort awards (AWARD_DEFS: streaks,
#                   engaged-minute milestones, practice volume, Brave Start, Perfect Check, Bounce
#                   Back, Explorer, Pathfinder) -- all computed from data the app already records
#                   honestly. Effort awards PERSIST once earned (new store.awards table), with a
#                   48h "NEW!" window and a "next up" nudge. Design rule: every award names what
#                   the student DID -- process praise, never person praise.
#               (2) TUTOR AWARENESS: /api/chat appends a note when an award was earned in the last
#                   48h so Mr. Cadabra congratulates the effort once, then keeps teaching.
#               (3) Dashboard gained the 🏆 TROPHY CASE (dashboard.html); NEW route /students
#                   serves the student how-to page (lesson flow, tools, the earnable-awards list --
#                   keep its list in sync with AWARD_DEFS).
#   2026-07-30  APP_BUILD -> "2026-07-30k-homeschool". NEW route /homeschool serving the dedicated
#               homeschool marketing page (Jim: "this should scream homeschooling"): parent-view +
#               student-dashboard screenshots, honest engaged-time story, weekly email report
#               (labeled "coming with launch" -- not built yet), records/requirements section.
#               Homeschool tab added to nav + footer across the marketing site; landing hero pill
#               now leads with "Built for homeschool families". New shots: parent.png, timetile.png.
#   2026-07-30  APP_BUILD -> "2026-07-30j-demofix". DEMO SCRIPT FIXES (Jim's playtest): the demo's
#               board no longer reveals "x = 4" before asking the student to type it (the student
#               now computes 8÷2 and the board confirms AFTER, with a check line), and the power-key
#               instructions now give the correct order (2, then xⁿ, then 3 -- the old wording
#               produced "^23"). DEMO_VOICE_LINES updated to the six new/changed lines; MUST stay
#               identical to demo.html's VOICE_LINES.
#   2026-07-30  APP_BUILD -> "2026-07-30i-website". MULTI-PAGE MARKETING SITE + WARM DEMO VOICE
#               (Jim's feedback: one-page anchor nav felt like a one-person company; no product
#               screenshots; demo voice was robotic).
#               (1) NEW routes /courses, /teachers, /pricing serving real pages (courses generated
#                   from curriculum.py; teachers page carries a real product screenshot).
#               (2) NEW GET /api/demo-audio/{idx}: serves ONLY the demo's fixed whitelisted lines
#                   (DEMO_VOICE_LINES -- keep identical to demo.html's VOICE_LINES) in the real
#                   ElevenLabs voice via the shared TTS cache; per-IP rate limited; no arbitrary
#                   text possible, and each line is paid for at most once ever. The speak pipeline
#                   was refactored into _tts_stream_response() (shared; behavior unchanged).
#               (3) static/shots/*.png: real product screenshots (sample data, labeled) used by the
#                   marketing pages.
#   2026-07-30  APP_BUILD -> "2026-07-30h-frontdoor". THE LANDING PAGE IS NOW THE FRONT DOOR
#               (go-live prep for mrcadabra.com): GET / serves landing.html (was the bare code-entry
#               screen), NEW GET /login serves index.html, NEW GET /demo serves demo.html. All 11
#               in-app "kick back to login" redirects across the static pages were retargeted from
#               "/" to "/login" in the same change, and the landing/nav gained a Sign in link -- so
#               a parent hitting the domain sees the marketing site, and students still land on the
#               login form whenever a code is missing/invalid.
#   2026-07-30  APP_BUILD -> "2026-07-30g-timetrack". ENGAGED-TIME TRACKING (parents' "how long did
#               my kid actually work?"). NEW: POST /api/heartbeat (adds one verified minute; requires
#               a valid code; rate limited; server-side MIN_BEAT_GAP_SECONDS stops a tampered client
#               inflating the clock) + GET /api/time/{code} (per-day totals with per-course split;
#               the client computes today/this-week against the student's local calendar). Data in
#               store.py's new time_daily table. Frontend: static/time-tracker.js beats once a minute
#               ONLY while the tab is visible AND the student was active in the last 4 minutes -- an
#               open-but-idle tab counts NOTHING. Dashboard gained a "Time this week" tile. This is
#               also the data spine for the upcoming weekly parent email.
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

import gzip
import hashlib
import hmac
import json
import os
import re
import secrets
import threading
import time
import uuid
from collections import defaultdict, deque
from pathlib import Path

import httpx
from fastapi import FastAPI, File, Header, HTTPException, Request, UploadFile
from fastapi.responses import FileResponse, JSONResponse, Response, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import tutor
import store   # durable DB storage; dormant unless DATABASE_URL is set (see store.py)
import curriculum   # 9 units + classify_unit() for real per-topic tracking
import library  # 2026-08-07: the "Look it up" reference library (seeds + generate-once)
try:
    # 2026-08-10 (build ck): the misconception catalogue, used to recognise a known
    # error pattern in what the student JUST said and hand the tutor the fix for it.
    import misconceptions
except Exception as _exc:  # noqa: BLE001
    misconceptions = None
    print(f"[main] misconceptions.py unavailable ({_exc}) -- diagnosis note disabled")
try:
    # 2026-08-09 (build ce): used ONLY to validate a [[learned term="..."]] tag against
    # the real script names before we write it down. Defensive, exactly like tutor.py's
    # import: a missing or broken foundations.py must never keep the classroom down.
    import foundations
except Exception as _exc:  # noqa: BLE001
    foundations = None
    print(f"[main] foundations.py unavailable ({_exc}) -- foundation memory disabled")

try:
    import sprints
except Exception as _exc:  # noqa: BLE001
    sprints = None
    print(f"[main] sprints.py unavailable ({_exc}) -- fluency sprints disabled")

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


# THE STORED TRANSCRIPT IS BOUNDED (2026-08-10, build cn).
# Jim: "I don't want to build in something that's going to degrade over time where the
# errors are gonna start to add up... because we're not discarding things that we should
# discard." This was that, and it was the biggest one in the app.
# Every chat turn LOADED the entire conversation, parsed it, appended two messages,
# re-serialised it and wrote the whole thing back. The tutor never sees more than the
# last MAX_HISTORY_MESSAGES (30) -- _trim_history throws the rest away immediately -- so
# a student one year in was moving several megabytes of JSON per turn to use 30 messages
# of it. At 10,000 students that is roughly 48 GB of transcript and a turn that gets
# slower every single week.
# We keep a generous margin over what the model reads (60 stored vs 30 sent) so nothing
# the tutor could want is ever missing, and we keep the OLDEST messages when trimming
# is impossible -- no. We keep the NEWEST, which is what a conversation needs.
# It also happens to be the right privacy posture: this is a child's conversation, we
# already delete their audio on the spot, and retaining a transcript forever is a
# liability rather than an asset. Progress, mastery, quizzes, hours and awards all live
# in their own tables and are untouched by this.
MAX_STORED_MESSAGES = 60

# SECURITY (build ec, 2026-08-12 -- finding F5): the largest audio upload /api/transcribe
# will pull into memory. A few seconds of student speech is well under 1 MB; 12 MB is a
# roomy ceiling for a long answer while closing the unbounded-read memory/cost hole.
# Env-tunable (MAX_AUDIO_BYTES) without a code change.
try:
    MAX_AUDIO_BYTES = int(os.environ.get("MAX_AUDIO_BYTES", str(12 * 1024 * 1024)) or (12 * 1024 * 1024))
except (TypeError, ValueError):
    MAX_AUDIO_BYTES = 12 * 1024 * 1024


def _bounded_history(session: dict) -> dict:
    """Return `session` with its transcript capped. Never raises."""
    try:
        h = session.get("history")
        if isinstance(h, list) and len(h) > MAX_STORED_MESSAGES:
            session = dict(session)
            session["history"] = h[-MAX_STORED_MESSAGES:]
    except Exception as exc:  # noqa: BLE001
        print(f"[session] history trim skipped: {exc}")
    return session


def save_session(code: str, session: dict, course: str = "algebra1") -> None:
    session = _bounded_history(session)
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


def _resolve_focus(code: str, course: str, req_unit: int):
    """(focus_unit, steered) for this turn (build ea). Order of authority:
    1. the student's own explicit focus (a dashboard link) -- always wins;
    2. the parent's standing steer for THIS course (set on /family);
    3. none. Fail-open: a store hiccup never costs a turn."""
    if 1 <= int(req_unit or 0) <= 9:
        return int(req_unit), False
    try:
        if store.enabled():
            s = store.get_steer(code)
            if s and s.get("course") == course and 1 <= int(s.get("unit") or 0) <= 9:
                return int(s["unit"]), True
    except Exception as exc:  # noqa: BLE001
        print(f"[steer] resolve failed (ignored): {exc}")
    return 0, False


def _mastery_note(code: str, focus_unit: int = 0, course: str = "algebra1",
                  steered: bool = False) -> str:
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
        if best >= store.PASS_PCT:
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
    # TOPIC QUIZZES (2026-08-04): tell the tutor exactly which mid-unit quizzes are already
    # passed, so gating survives across sessions -- resume each unit's ladder at the first
    # unpassed topic and never re-quiz a passed one.
    try:
        qrows = store.get_topic_quizzes(code, course)
    except Exception as exc:  # noqa: BLE001
        print(f"[mastery-note] get_topic_quizzes failed (ignored): {exc}")
        qrows = []
    if qrows:
        by_unit = {}
        for q in qrows:
            by_unit.setdefault(q["unit"], []).append(q)
        qparts = []
        for n in sorted(by_unit):
            items = []
            for q in by_unit[n]:
                if q["best_pct"] >= store.QUIZ_PASS_PCT:
                    items.append(f"'{q['topic_name']}' PASSED ({q['best_pct']}%)")
                else:
                    items.append(f"'{q['topic_name']}' NOT passed yet (best {q['best_pct']}%)")
            qparts.append(f"Unit {n}: " + "; ".join(items))
        note += (" TOPIC QUIZZES so far -- " + " | ".join(qparts) +
                 ". Resume each unit at its first unpassed topic; do not re-quiz passed topics.")
    # RECENT MISSES (2026-08-11, build dt -- rule 55's spaced-review half). The tutor
    # reported these in quiz tags; now they come back as steering. Capped tight: the
    # note is per-turn prompt weight, and ONE revisited problem is the whole ask.
    try:
        misses = store.get_misses(code, course, limit=5)
    except Exception as exc:  # noqa: BLE001
        print(f"[mastery-note] get_misses failed (ignored): {exc}")
        misses = []
    if misses:
        mm = "; ".join(
            f"\"{m['question'][:80]}\" (they answered \"{m['answer'][:40]}\""
            + (f", Unit {m['unit']}" if m.get("unit") else "") + f", {m['when']})"
            for m in misses)
        note += (" RECENT MISSED PROBLEMS (rule 55): " + mm +
                 ". Early in this session -- after the opener, never as a cold open -- "
                 "revisit exactly ONE of these as a FRESH, slightly different problem "
                 "of the same kind, warmly. One is enough; never re-run a failed quiz.")
    fu = int(focus_unit or 0)
    if 1 <= fu <= 9:
        if steered:
            # build ea: the PARENT set this plan on /family -- the student did not ask.
            note += (f" THE FAMILY PLAN: their parent asked that sessions center on "
                     f"Unit {fu} ({curriculum.unit_name(course, fu)}) for now. Steer "
                     f"there warmly and introduce it as today's plan -- never as "
                     f"something the student requested, and never as a punishment. If "
                     f"the student asks to work on something else, honor rule 50: "
                     f"their agency wins for this session.")
        else:
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
    # 2026-08-07 FINAL EXAM: "" (normal lesson) | "prep" | "exam". The server RE-VERIFIES
    # eligibility (all 9 units mastered) on every turn -- the client is never trusted.
    final: str = ""


class SprintResultIn(BaseModel):
    course: str = "prealgebra"
    unit: int = 1
    skill: str = ""
    a_correct: int = 0
    a_attempted: int = 0
    b_correct: int = 0
    b_attempted: int = 0


class FinalIn(BaseModel):
    correct: int
    total: int
    course: str = "algebra1"
    missed: list = []          # build dt: rule 55's missed problems ride the same POST


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


class HeartbeatRequest(BaseModel):
    code: str
    course: str = "algebra1"   # which course the student is working in right now
    day: str = ""              # the STUDENT'S local calendar day 'YYYY-MM-DD' (validated server-side)


class PlacementIn(BaseModel):
    level: int = 1
    level_title: str = ""
    start_unit: int = 1
    start_unit_name: str = ""
    points: int = 0


class _CheckMissedMixin(BaseModel):
    missed: list = []          # build dt: rule 55's missed problems ride the same POST


class CheckIn(_CheckMissedMixin):
    unit: int                  # which of the 9 units this end-of-unit check covered
    correct: int = 0           # questions the student got right
    total: int = 1             # questions on the check
    course: str = "algebra1"   # which course this check belongs to (so it's filed per-course)


class QuizIn(BaseModel):
    """A mid-unit TOPIC QUIZ result (2026-08-04). Passing (80%+) unlocks the next topic."""
    unit: int                  # which of the 9 units the topic belongs to
    topic: int = 0             # the topic's position in the unit's topic list (1-based; 0 = unknown)
    name: str = ""             # the topic's name as the tutor stated it
    correct: int = 0
    total: int = 1
    course: str = "algebra1"
    missed: list = []          # build dt: [{"q": question, "a": their answer}, ...] from rule 55


def _keep_misses(code: str, course: str, unit: int, topic: int, kind: str,
                 missed, correct: int, total: int) -> None:
    """Store the tag's missed problems (build dt), HONESTLY CLAMPED: never more
    entries than were actually missed (total - correct), never more than 25, and
    always fail-open -- a malformed missed list must never cost the score above it."""
    try:
        if not (store.enabled() and missed):
            return
        room = max(0, min(25, int(total) - int(correct)))
        if not room:
            return
        items = []
        for it in list(missed)[:room]:
            if isinstance(it, dict):
                items.append({"q": it.get("q"), "a": it.get("a")})
        if items:
            store.record_misses(code, course, int(unit or 0), int(topic or 0),
                                kind, items)
    except Exception as exc:  # noqa: BLE001
        print(f"[misses] store failed (ignored): {exc}")


# TEACHER / PARENT CLASSROOM (2026-07-28) -- see the classroom endpoints below.
class ClassIn(BaseModel):
    class_code: str            # short, case-insensitive key the teacher picks (e.g. "MRSB-P3")
    name: str = ""             # friendly label, e.g. "Period 3 Algebra"
    owner_name: str = ""       # teacher/parent display name (optional)
    teacher_code: str = ""     # the teacher's personal sign-in code (optional; e.g. "MRSBAKER")


class ClassStudentIn(BaseModel):
    code: str                  # an EXISTING student code to add to the class


class ParentSignupIn(BaseModel):
    email: str
    password: str
    name: str = ""             # parent's display name (optional)


class ParentLoginIn(BaseModel):
    email: str
    password: str


class ParentTokenIn(BaseModel):
    token: str


class ParentForgotIn(BaseModel):
    email: str


class ParentResetIn(BaseModel):
    token: str
    password: str


class ParentStudentIn(BaseModel):
    token: str
    name: str                  # child's FIRST name only (we ask for nothing more)


class MarkIn(BaseModel):
    correct: int = 1           # was the practice problem right (1) or wrong (0)
    attempted: int = 1         # how many problems this represents (usually 1)
    highest_tier: int = 0
    strengths: list = []


# ---- App -------------------------------------------------------------------
app = FastAPI(title="Math Tutor MVP", version="0.1.0")


# =============================================================================
# SECURITY HEADERS (build ec, 2026-08-12 -- finding F4)
# -----------------------------------------------------------------------------
# One small middleware stamps the standard browser-hardening headers on EVERY
# response (pages, API, static). These are defense-in-depth: alone they ruin
# nothing, but together they stop a whole class of tricks -- clickjacking (our
# site framed inside a fake page), MIME-sniffing, protocol downgrade, and
# referrer leakage.
#
#   X-Content-Type-Options   nosniff -- browser must honor our declared types
#   X-Frame-Options          SAMEORIGIN -- only WE may frame our own pages
#   Referrer-Policy          strict-origin-when-cross-origin -- no path leak off-site
#   Strict-Transport-Security force HTTPS for a year (Render is HTTPS-only already)
#   Permissions-Policy       deny camera/geolocation/payment; MIC stays allowed
#                            (the tutor is voice-first)
#   Content-Security-Policy-Report-Only  -- the ONE header shipped in REPORT-ONLY
#                            mode on purpose. Our pages use inline <style>/<script>
#                            and load Plausible; an enforcing CSP could blank the
#                            site, so we start by DESCRIBING the policy without
#                            blocking, and can flip it to enforcing (and add a
#                            nonce refactor to drop 'unsafe-inline') once proven.
# setdefault() everywhere so a route that sets its own header always wins.
# =============================================================================
_CSP_REPORT_ONLY = (
    "default-src 'self'; "
    "script-src 'self' 'unsafe-inline' https://plausible.io; "
    "style-src 'self' 'unsafe-inline'; "
    "img-src 'self' data:; "
    "font-src 'self' data:; "
    "connect-src 'self' https://plausible.io; "
    "frame-ancestors 'self'; "
    "base-uri 'self'; "
    "form-action 'self'; "
    "object-src 'none'"
)
_SECURITY_HEADERS = {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "SAMEORIGIN",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
    "Permissions-Policy": "camera=(), geolocation=(), payment=(), microphone=(self)",
    "Content-Security-Policy-Report-Only": _CSP_REPORT_ONLY,
}


@app.middleware("http")
async def _security_headers(request: Request, call_next):
    response = await call_next(request)
    for _h, _v in _SECURITY_HEADERS.items():
        response.headers.setdefault(_h, _v)
    return response


def _lookup_student(code: str):
    """Find a student by code, wherever they live (2026-07-31).

    Pilot/persona students come from students.json exactly as before. Students
    created by a signed-up parent live in the database (accounts.parent_id set);
    they are returned in the same shape the rest of the app expects, so every
    endpoint (chat, dashboard, awards, heartbeat, voice) works for them unchanged.
    Returns None when the code is unknown."""
    code = (code or "").strip()
    if not code:
        return None
    student = STUDENTS.get(code)
    if student:
        return student
    if store.enabled():
        acct = store.get_account(code)
        if acct and acct.get("parent_id"):
            return {
                "name": acct.get("name") or "Student",
                "grade": "",
                "progress": "",                      # real progress lives in the DB tables
                "family": True,                       # marks a parent-managed student
                "parent_id": acct["parent_id"],
            }
        # BETA PASS (2026-07-31): valid ONLY while a sign-in window is open. Full
        # access during the window (it's a trial of the real product); when the
        # window lapses, _student_or_404 explains kindly instead of a bare 404.
        bc = store.get_beta_code(code)
        if bc and not bc.get("revoked") and store.beta_window_active(bc):
            return {"name": bc.get("label") or "Beta tester", "grade": "",
                    "progress": "", "beta": True}
    return None


def _beta_404_detail(code: str):
    """A kind, specific message when a KNOWN beta pass can't be used right now."""
    if not store.enabled():
        return None
    bc = store.get_beta_code(code)
    if not bc:
        return None
    if bc.get("revoked"):
        return "This beta pass has been closed. Email support@mrcadabra.com if that seems wrong."
    left = int(bc["uses_allowed"]) - int(bc["uses_used"])
    if left <= 0:
        return ("This beta pass has been used up — thank you for test-driving Mr. Cadabra's Classroom! "
                "We'd love your feedback at support@mrcadabra.com.")
    return (f"Your beta session window has ended. Sign in again with this pass to keep "
            f"going — {left} of {bc['uses_allowed']} sign-ins left.")


def _student_or_404(code: str) -> dict:
    student = _lookup_student(code)
    if not student:
        beta_note = _beta_404_detail((code or "").strip())
        raise HTTPException(status_code=404,
                            detail=beta_note or "That code was not recognized.")
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
        # build cn: the old sweep only dropped buckets that were ALREADY empty, so with
        # ten thousand active students -- every bucket non-empty -- the table could grow
        # past the cap and never come back down. Expire by age instead: a bucket whose
        # newest hit is older than its window is spent, whatever it still holds.
        if len(_RL_BUCKETS) > 5000:
            stale = [k for k, q in _RL_BUCKETS.items()
                     if not q or q[-1] <= now - max(window_seconds, 3600)]
            for k in stale:
                _RL_BUCKETS.pop(k, None)
            if len(_RL_BUCKETS) > 50000:      # pathological: shed the oldest wholesale
                for k in sorted(_RL_BUCKETS, key=lambda k: _RL_BUCKETS[k][-1]
                                if _RL_BUCKETS[k] else 0)[:20000]:
                    _RL_BUCKETS.pop(k, None)
                print("[rate] bucket table shed to 30k keys")
        q = _RL_BUCKETS[key]
        while q and q[0] <= now - window_seconds:
            q.popleft()
        if len(q) >= limit:
            raise HTTPException(status_code=429,
                                detail=f"Too many {what} in a short time — please wait a minute and try again.")
        q.append(now)


# =============================================================================
# READ-BY-CODE ENUMERATION GUARD (build ed, 2026-08-12 -- finding F1)
# -----------------------------------------------------------------------------
# A student's login code is the only key to their data, and the GET-by-code reads
# (session, records, misses, awards, time, topics, assessment, placement, courses,
# sprints, sprint) had NO speed limit -- someone could script guesses across the
# short code space and harvest children's names and progress.
#
# The precise defense: ENUMERATION IS, BY DEFINITION, "many DIFFERENT codes from
# one source." A real family reads its own 1-2 codes over and over; a scraper walks
# thousands. So on top of a generous raw per-IP read cap (blunts hammering/cost), we
# track how many DISTINCT codes each IP has touched in a rolling window and refuse
# once it crosses a ceiling set far above any honest use (a whole co-op reviewed
# from one address is ~30 kids; the ceiling is higher still). Repeatedly reading the
# SAME code -- a real dashboard reloading -- never trips it. Paired with the widened
# code format (_new_student_code) and the F3 IP-spoofing fix, a sweep is infeasible:
# an IP is capped to CODE_PROBE_MAX guesses per window and can't rotate its address.
# All in-process, self-pruning; env-tunable without a code change.
# =============================================================================
try:
    _READ_IP_LIMIT = int(os.environ.get("READ_IP_LIMIT", "600") or 600)
except (TypeError, ValueError):
    _READ_IP_LIMIT = 600
try:
    _CODE_PROBE_MAX = int(os.environ.get("CODE_PROBE_MAX", "50") or 50)
except (TypeError, ValueError):
    _CODE_PROBE_MAX = 50
try:
    _CODE_PROBE_WINDOW = int(os.environ.get("CODE_PROBE_WINDOW", "900") or 900)
except (TypeError, ValueError):
    _CODE_PROBE_WINDOW = 900
_CODE_PROBE_LOCK = threading.Lock()
_CODE_PROBE: dict = defaultdict(dict)      # ip -> {code: last_seen_monotonic}


def _read_guard(request: Request, code: str) -> None:
    """Throttle a read-by-code endpoint against enumeration. Raises 429 when an IP
    exceeds the raw read rate OR touches too many DISTINCT codes in the window."""
    ip = _client_ip(request)
    # (1) raw per-IP read cap -- generous for a browsing family, a wall for a firehose.
    _rate_limit("read:" + ip, limit=_READ_IP_LIMIT, window_seconds=300, what="lookups")
    # (2) distinct-code ceiling -- the actual anti-enumeration guard.
    key = (code or "").strip()
    now = time.monotonic()
    with _CODE_PROBE_LOCK:
        seen = _CODE_PROBE[ip]
        for c in [c for c, t in seen.items() if t <= now - _CODE_PROBE_WINDOW]:
            del seen[c]
        seen[key] = now
        distinct = len(seen)
        if not seen:                                    # never keep an empty inner dict
            _CODE_PROBE.pop(ip, None)
        if len(_CODE_PROBE) > 20000:                    # keep the outer table bounded
            for k in [k for k, d in _CODE_PROBE.items()
                      if not d or max(d.values()) <= now - _CODE_PROBE_WINDOW]:
                _CODE_PROBE.pop(k, None)
    if distinct > _CODE_PROBE_MAX:
        raise HTTPException(status_code=429, detail=(
            "Too many different codes tried from this connection — if you're a "
            "teacher reviewing a class, please wait a minute between students."))


def _client_ip(request: Request) -> str:
    """Caller IP for the per-IP rate limiter, read from the position we actually trust.

    SECURITY (build ec, 2026-08-12 -- finding F3): X-Forwarded-For is built LEFT-to-right
    (client, proxy1, proxy2, ...). A visitor can PREPEND any value they like on the left,
    so the old `.split(",")[0]` (leftmost) was attacker-controlled -- rotating a fake header
    let someone slip the sign-in / signup / password-reset brute-force limits. Our own
    proxy (Render) APPENDS the real peer on the RIGHT, and the client cannot control what we
    append. So we trust only the rightmost `TRUSTED_PROXY_HOPS` entries and take the one just
    inside them. Default 1 hop = "the last entry" = the address Render saw the connection
    from. If ever fronted by an extra trusted proxy (e.g. Cloudflare -> Render), set
    TRUSTED_PROXY_HOPS=2 in the environment; never lower it below the real hop count.
    """
    try:
        hops = int(os.environ.get("TRUSTED_PROXY_HOPS", "1") or 1)
    except (TypeError, ValueError):
        hops = 1
    if hops < 1:
        hops = 1
    fwd = [p.strip() for p in (request.headers.get("x-forwarded-for") or "").split(",") if p.strip()]
    if fwd:
        idx = len(fwd) - hops                 # the entry just inside our trusted proxy hops
        return fwd[idx] if idx >= 0 else fwd[0]
    return request.client.host if request.client else "unknown"


def _require_student(code: str) -> dict:
    """Like _student_or_404 but returns 401 (auth), for the paid voice endpoints."""
    student = _lookup_student(code)
    if not student:
        raise HTTPException(status_code=401, detail="A valid login code is required.")
    return student


@app.get("/")
def home():
    """FRONT DOOR (changed 2026-07-30): the marketing/landing page. A parent visiting
    mrcadabra.com now sees what MyTutor IS, with a Sign in link -- the bare code-entry
    screen used to live here and moved to /login. Every in-app 'kick back to login'
    redirect was retargeted from '/' to '/login' in the same change."""
    return FileResponse(STATIC_DIR / "landing.html")


@app.get("/login")
def login_page():
    """The code-entry screen (was served at '/' until 2026-07-30)."""
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/demo")
def demo_page():
    """The self-contained interactive demo lesson (pretty route for marketing links)."""
    return FileResponse(STATIC_DIR / "demo.html")


@app.get("/homeschool")
def homeschool_page():
    """Marketing: the dedicated homeschool page (parent view, honest hours, records)."""
    return FileResponse(STATIC_DIR / "homeschool.html")


@app.get("/records")
def records_page():
    """The printable homeschool records report (2026-08-04): hours log, mastery, awards."""
    return FileResponse(STATIC_DIR / "records.html")


@app.get("/help")
def help_page():
    """In-app help (2026-08-11, build ds): the student-first FAQ. Every app page's
    ❓ Help button lands here -- the old mailto: link was dead on school Chromebooks."""
    return FileResponse(STATIC_DIR / "help.html")


@app.get("/students")
def students_page():
    """Marketing/help: the student how-to page (lesson flow, tools, earnable awards)."""
    return FileResponse(STATIC_DIR / "students.html")


@app.get("/parents")
def parents_page():
    """Marketing: the parent trust page (child experience, parent view, privacy promises)."""
    return FileResponse(STATIC_DIR / "parents.html")


@app.get("/courses")
def courses_page():
    """Marketing: all eight courses with every unit listed (printable scope & sequence)."""
    return FileResponse(STATIC_DIR / "courses.html")


@app.get("/features")
def features_page():
    """Marketing (2026-08-05): every product feature on one page, grouped in six
    sections of three cards. Everything listed is live in the product today."""
    return FileResponse(STATIC_DIR / "features.html")


@app.get("/teachers")
def teachers_page():
    """Marketing: the classroom/co-op page (heatmap screenshot, features, pilot CTA)."""
    return FileResponse(STATIC_DIR / "teachers.html")


@app.get("/family")
def family_page():
    """The family portal (2026-07-31): parent signup/sign-in, children + their codes,
    plan & billing. The page's own JS talks to /api/parent/* and /api/billing/*."""
    return FileResponse(BASE_DIR / "static" / "family.html")


@app.get("/beta")
def beta_page():
    """Beta-tester program (2026-07-31): public pitch + Jim's ?admin= generator."""
    return FileResponse(BASE_DIR / "static" / "beta.html")


@app.get("/admin")
def admin_page():
    """Jim's central admin dashboard (2026-08-03). A visitor without the key sees
    only a locked 'enter your key' prompt; the real numbers, the beta generator,
    and the quick links appear only after /api/admin/stats verifies the key
    server-side. The admin key never lives in this file."""
    return FileResponse(BASE_DIR / "static" / "admin.html")


@app.get("/mission")
def mission_page():
    """Our mission (2026-07-31): fun, accessible, complete, taught right."""
    return FileResponse(BASE_DIR / "static" / "mission.html")


@app.get("/community")
def community_page():
    """The community forum (2026-07-31): parents post, everyone reads."""
    return FileResponse(BASE_DIR / "static" / "community.html")


@app.get("/pricing")
def pricing_page():
    """Marketing: standalone pricing page."""
    return FileResponse(STATIC_DIR / "pricing.html")


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


# ---- DISCOVERY FILES (2026-08-02: AI search + Google) -----------------------
# Three tiny files that make the site findable. robots.txt welcomes Google AND the
# AI assistants' crawlers (GPTBot/ClaudeBot/PerplexityBot -- they power ChatGPT/
# Claude/Perplexity recommendations) while hiding the sign-in-only app pages.
# sitemap.xml lists every public page for Google Search Console / Bing Webmaster.
# llms.txt is a plain-text product summary the AI crawlers read directly.
@app.get("/robots.txt")
def robots_txt():
    return FileResponse(STATIC_DIR / "robots.txt", media_type="text/plain")


@app.get("/sitemap.xml")
def sitemap_xml():
    return FileResponse(STATIC_DIR / "sitemap.xml", media_type="application/xml")


@app.get("/llms.txt")
def llms_txt():
    return FileResponse(STATIC_DIR / "llms.txt", media_type="text/plain")


# =============================================================================
# STUDENT REWARDS (2026-07-30) -- merit badges, course trophies, effort awards
# -----------------------------------------------------------------------------
# Three kinds of recognition, ALL computed from data the app already records
# honestly (nothing invented, nothing participation-trophy about it):
#   - MERIT BADGES: one per unit mastered (check >= store.PASS_PCT, i.e. 90%), collected per course.
#   - COURSE TROPHIES: all nine units of a course mastered.
#   - EFFORT AWARDS: streaks, engaged minutes, practice volume, courage
#     (first check), growth (Bounce Back: mastered a unit after failing a
#     check on it), range (Explorer/Pathfinder). Awards PERSIST once earned
#     (store.awards) -- a streak medal survives the streak breaking.
# Design rule (matches the tutor's pedagogy): every award names something the
# student DID -- worked, persisted, came back -- never "you're smart."
AWARD_DEFS = {
    # id: (icon, name, description, family, threshold-or-None)
    "streak3":    ("🔥", "Spark",         "Worked 3 days in a row", "streak", 3),
    "streak7":    ("🔥", "Blaze",         "Worked 7 days in a row", "streak", 7),
    "streak30":   ("🔥", "Unstoppable",   "Worked 30 days in a row", "streak", 30),
    "min100":     ("⏱", "Century Club",   "100 minutes of real work", "minutes", 100),
    "min500":     ("⏱", "500 Club",       "500 minutes of real work", "minutes", 500),
    "min1000":    ("⏱", "Scholar",        "1,000 minutes of real work", "minutes", 1000),
    "prac10":     ("✏️", "First Ten",     "Practiced 10 problems", "practice", 10),
    "prac50":     ("✏️", "Workhorse",     "Practiced 50 problems", "practice", 50),
    "prac100":    ("✏️", "Centurion",     "Practiced 100 problems", "practice", 100),
    "firstcheck": ("🎯", "Brave Start",   "Took your first quiz", "one", None),
    "perfect":    ("💯", "Perfect Quiz",  "Scored 100% on a quiz", "one", None),
    "bounceback": ("💪", "Bounce Back",   "Mastered a unit after a tough first Unit Quiz", "one", None),
    "explorer":   ("🧭", "Explorer",      "Worked in two different courses", "one", None),
    "pathfinder": ("🗺️", "Pathfinder",   "Completed a course assessment", "one", None),
    # 2026-08-07 (Jim): the Final Exam's reward lives in the trophy case (the diploma was
    # removed the same day -- it read like an accredited-school credential, which we are not).
    "champion":   ("🏅", "Course Champion", "Passed a course Final Exam", "one", None),
}


@app.get("/api/awards/{code}")
def awards_state(code: str, request: Request):
    """The student's trophy case: course trophies, per-course merit-badge counts, and
    effort awards (persisted once earned). Honest {tracking:false} when the DB is off."""
    _read_guard(request, code)            # F1: throttle read-by-code enumeration
    _student_or_404(code)
    code = code.strip()
    if not store.enabled():
        return {"tracking": False, "trophies": [], "badges": {}, "awards": []}

    trophies, badges = [], {}
    any_check = perfect = bounce = champion = False
    try:
        activity = store.get_course_activity(code)
    except Exception as exc:  # noqa: BLE001
        print(f"[awards] activity failed: {exc}")
        activity = {}
    stats = {}
    for course_id in activity:
        try:
            mastery = store.get_mastery(code, course_id)
        except Exception as exc:  # noqa: BLE001
            print(f"[awards] mastery({course_id}) failed: {exc}")
            continue
        stats = mastery.get("stats") or stats
        checks = mastery.get("checks", {})
        unit_names = dict(curriculum.units_for(course_id))
        mastered_units = []
        for unit, cinfo in checks.items():
            taken = int(cinfo.get("checks_taken") or 0)
            best = int(cinfo.get("best_pct") or 0)
            if taken:
                any_check = True
            if best >= 100:
                perfect = True
            if taken >= 2 and best >= store.PASS_PCT:
                bounce = True
            if best >= store.PASS_PCT:
                mastered_units.append({"unit": unit, "name": unit_names.get(unit, f"Unit {unit}")})
        mastered_units.sort(key=lambda u: u["unit"])
        total_units = len(unit_names) or 9
        badges[course_id] = {"course_title": curriculum.course_title(course_id),
                             "earned": mastered_units, "total": total_units}
        if len(mastered_units) >= total_units:
            trophies.append({"course": course_id, "title": curriculum.course_title(course_id)})
        # 2026-08-07: Course Champion -- passed this course's Final Exam.
        try:
            if (store.get_final_exam(code, course_id) or {}).get("passed"):
                champion = True
        except Exception as exc:  # noqa: BLE001
            print(f"[awards] final({course_id}) failed: {exc}")

    total_minutes = 0
    try:
        total_minutes = sum(r["minutes"] for r in store.get_time(code, days=400))
    except Exception as exc:  # noqa: BLE001
        print(f"[awards] time failed: {exc}")
    streak = int((stats or {}).get("streak_days") or 0)
    practiced = int((stats or {}).get("problems_practiced") or 0)
    placed = any(bool(read_placement(code, cid)) for cid in curriculum.COURSE_ORDER)

    computed = set()
    for aid, (_ic, _nm, _ds, family, threshold) in AWARD_DEFS.items():
        got = ((family == "streak" and streak >= threshold) or
               (family == "minutes" and total_minutes >= threshold) or
               (family == "practice" and practiced >= threshold) or
               (family == "one" and {"firstcheck": any_check, "perfect": perfect,
                                     "bounceback": bounce, "explorer": len(activity) >= 2,
                                     "pathfinder": placed, "champion": champion}[aid]))
        if got:
            computed.add(aid)
    try:
        store.record_awards(code, sorted(computed))
        earned = store.get_awards(code)          # union: persisted awards never un-earn
    except Exception as exc:  # noqa: BLE001
        print(f"[awards] persist failed: {exc}")
        earned = {a: None for a in computed}

    from datetime import datetime, timezone, timedelta
    fresh_cut = datetime.now(timezone.utc) - timedelta(hours=48)
    out = []
    for aid, when in earned.items():
        if aid not in AWARD_DEFS:
            continue
        ic, nm, ds, _f, _t = AWARD_DEFS[aid]
        is_new = False
        try:
            if when:
                dt = datetime.fromisoformat(when)
                if dt.tzinfo is None:            # SQLite returns naive datetimes; treat as UTC
                    dt = dt.replace(tzinfo=timezone.utc)
                is_new = dt >= fresh_cut
        except (ValueError, TypeError):
            pass
        out.append({"id": aid, "icon": ic, "name": nm, "desc": ds,
                    "earned_at": when, "new": is_new})
    order = list(AWARD_DEFS.keys())
    out.sort(key=lambda a: order.index(a["id"]))

    # "Next up" nudges for the tiered families -- the dashboard shows ONE.
    next_up = []
    for family, value, unit_label in (("streak", streak, "day streak"),
                                      ("minutes", total_minutes, "real minutes"),
                                      ("practice", practiced, "problems practiced")):
        tiers = sorted((t, aid) for aid, (_i, _n, _d, f, t) in AWARD_DEFS.items() if f == family)
        for t, aid in tiers:
            if aid not in earned:
                _i, n, _d, _f, _t = AWARD_DEFS[aid]
                next_up.append({"award": n, "icon": _i, "have": value, "need": t, "what": unit_label})
                break
    next_up.sort(key=lambda x: (x["need"] - x["have"]) / max(x["need"], 1))

    return {"tracking": True, "trophies": trophies, "badges": badges,
            "awards": out, "next_up": next_up[:1]}


# -----------------------------------------------------------------------------
# ENGAGED-TIME TRACKING (2026-07-30) -- "how long did my kid actually work?"
# -----------------------------------------------------------------------------
# static/time-tracker.js (on session/practice/topic/challenge) posts a heartbeat
# once a minute ONLY while the tab is visible AND the student did something real
# recently (typed/clicked) -- so leaving the app open does NOT rack up time. The
# server adds its own guard: at most one COUNTED minute per MIN_BEAT_GAP_SECONDS
# per student, so a tampered client can't inflate the clock either.
MIN_BEAT_GAP_SECONDS = 50
_LAST_BEAT: dict = {}
_DAY_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


@app.post("/api/heartbeat")
def heartbeat(req: HeartbeatRequest):
    """Record one verified minute of engaged time. Returns counted=false (never an
    error) when the beat arrives too soon or tracking is off, so pages never break."""
    _student_or_404(req.code)
    code = req.code.strip()
    _rate_limit("beat:" + code, limit=30, window_seconds=600, what="activity pings")
    now = time.monotonic()
    with _RL_LOCK:
        if now - _LAST_BEAT.get(code, -10 ** 9) < MIN_BEAT_GAP_SECONDS:
            return {"ok": True, "counted": False}
        _LAST_BEAT[code] = now
    day = (req.day or "").strip()
    if not _DAY_RE.match(day):
        day = ""   # bad/missing client date -> store.record_minutes falls back to the server's date
    if not store.enabled():
        return {"ok": True, "counted": False, "tracking": False}
    try:
        store.record_minutes(code, (req.course or "algebra1").strip(), day=day, minutes_add=1)
    except Exception as exc:  # noqa: BLE001
        print(f"[time] record_minutes failed: {exc}")
        return {"ok": True, "counted": False}
    return {"ok": True, "counted": True}


@app.get("/api/time/{code}")
def time_summary(code: str, request: Request, days: int = 14):
    """Recent engaged time for the dashboard: per-day totals (newest first) with a
    per-course split. The CLIENT computes 'today' / 'this week' against the days
    it recorded, so the student's local calendar stays authoritative."""
    _read_guard(request, code)            # F1: throttle read-by-code enumeration
    _student_or_404(code)
    code = code.strip()
    if not store.enabled():
        return {"tracking": False, "days": []}
    try:
        rows = store.get_time(code, days=max(1, min(int(days), 60)))
    except Exception as exc:  # noqa: BLE001
        print(f"[time] get_time failed: {exc}")
        return {"tracking": False, "days": []}
    agg: dict = {}
    for r in rows:
        d = agg.setdefault(r["day"], {"day": r["day"], "minutes": 0, "courses": {}})
        d["minutes"] += r["minutes"]
        d["courses"][r["course"]] = d["courses"].get(r["course"], 0) + r["minutes"]
    out = sorted(agg.values(), key=lambda x: x["day"], reverse=True)[:days]
    return {"tracking": True, "days": out}


@app.get("/api/topics/{code}")
def topics_state(code: str, request: Request, course: str = "algebra1"):
    """
    REAL, honest per-topic progress for the dashboard: all of the CHOSEN COURSE's units with
    the student's actual engagement (explored / learning / practiced) or 'not-started'.
    Only meaningful when the database is on (`tracking:true`); otherwise it reports
    tracking is off so the dashboard can say so rather than invent numbers.
    """
    _read_guard(request, code)            # F1: throttle read-by-code enumeration
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

    quiz_rows = {}
    if tracking:
        try:
            for q in store.get_topic_quizzes(code, course):
                quiz_rows.setdefault(q["unit"], []).append({
                    "name": q["topic_name"], "best_pct": q["best_pct"],
                    "passed": q["best_pct"] >= store.QUIZ_PASS_PCT})
        except Exception as exc:  # noqa: BLE001
            print(f"[topics] get_topic_quizzes failed: {exc}")

    checks = mastery.get("checks", {})
    units = []
    for n, name in curriculum.units_for(course):
        r = recorded.get(n)
        c = checks.get(n) or {}
        best = int(c.get("best_pct") or 0)
        uq = quiz_rows.get(n, [])
        units.append({
            "unit": n,
            "name": name,
            "status": (r["status"] if r else "not-started"),
            "touches": (r["touches"] if r else 0),
            "last_touched": (r.get("last_touched") if r else None),
            "best_pct": best,                       # best UNIT QUIZ score (0 if none)
            "checks_taken": int(c.get("checks_taken") or 0),
            "mastered": best >= store.PASS_PCT,
            "quizzes": uq,                          # topic-quiz rows: {name, best_pct, passed}
            "quizzes_passed": len([q for q in uq if q["passed"]]),
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
            "mastered": best >= store.PASS_PCT,
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


# =============================================================================
# PARENT ACCOUNTS (2026-07-31) -- real signups, the payments foundation
# -----------------------------------------------------------------------------
# A parent signs up with email + password, adds children (FIRST names only), and
# each child gets a friendly login code -- the same kind of code the app has
# always used, so nothing about the student experience changes. Passwords are
# never stored or logged: only a salted PBKDF2-SHA256 hash (390k iterations,
# per-account random salt, constant-time comparison). Sign-in hands out a random
# 30-day token; every parent API call presents that token, never the password.
# All of it REQUIRES the database -- an accounts system must not live in
# throwaway JSON files that vanish on redeploy, so without DATABASE_URL these
# endpoints answer 503 with a clear message instead of pretending.
# =============================================================================

_PBKDF2_ITERATIONS = 390_000
_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

# Kid-friendly words for student login codes (short, unambiguous, easy to say
# out loud). A code looks like MAPLE42. ~50 words x 90 numbers = 4500 combos,
# and we re-roll on collision, so exhaustion is not a concern at this scale.
_CODE_WORDS = [
    "MAPLE", "RIVER", "TIGER", "COMET", "EAGLE", "PIANO", "ROCKET", "PANDA",
    "OTTER", "ACORN", "BADGE", "CEDAR", "DELTA", "EMBER", "FALCON", "GECKO",
    "HARBOR", "IGLOO", "JUNIPER", "KOALA", "LANTERN", "MARBLE", "NUTMEG",
    "ORBIT", "PEBBLE", "QUARTZ", "ROBIN", "SIERRA", "TUNDRA", "UMBER",
    "VIOLET", "WALNUT", "YONDER", "ZEPHYR", "ASPEN", "BREEZE", "CANYON",
    "DUNE", "FERN", "GLACIER", "HAZEL", "INDIGO", "JASPER", "KESTREL",
    "LAGOON", "MESA", "NEBULA", "ONYX", "PRAIRIE", "SUMMIT",
]


def _hash_password(password: str) -> str:
    """Salted PBKDF2-SHA256. The stored string carries its own parameters so the
    iteration count can be raised later without breaking old hashes."""
    salt = secrets.token_hex(16)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"),
                             bytes.fromhex(salt), _PBKDF2_ITERATIONS)
    return f"pbkdf2_sha256${_PBKDF2_ITERATIONS}${salt}${dk.hex()}"


def _verify_password(password: str, stored: str) -> bool:
    try:
        algo, iters, salt, want = (stored or "").split("$", 3)
        if algo != "pbkdf2_sha256":
            return False
        dk = hashlib.pbkdf2_hmac("sha256", (password or "").encode("utf-8"),
                                 bytes.fromhex(salt), int(iters))
        return hmac.compare_digest(dk.hex(), want)
    except (ValueError, TypeError):
        return False


def _require_db() -> None:
    if not store.enabled():
        raise HTTPException(status_code=503, detail=(
            "Family accounts need the database, which isn't connected right now. "
            "Please try again shortly or email support@mrcadabra.com."))


def _require_parent(token: str) -> dict:
    """Validate a parent token and return the parent row (sans password hash)."""
    _require_db()
    parent_id = store.get_parent_token((token or "").strip())
    if not parent_id:
        raise HTTPException(status_code=401, detail="Please sign in again.")
    parent = store.get_parent(parent_id)
    if not parent:
        raise HTTPException(status_code=401, detail="Please sign in again.")
    parent.pop("password_hash", None)   # never let the hash near a response
    return parent


def _new_student_code() -> str:
    """A fresh, friendly student code (e.g. MAPLE4821) that collides with nothing:
    not the pilot codes in students.json, not any existing account.

    WIDENED (build ed, 2026-08-12 -- finding F1): the digit block went 2 -> 4 digits,
    so the space is 50 words x 9000 = 450,000 (was 4,500) -- a ~100x jump that makes
    guessing a valid code infeasible even before the read-throttle. Still one short
    word + a number, so it's just as easy for a child to read and type. Existing
    2-digit codes keep working untouched -- nothing validates the digit count; this
    only changes what NEW codes look like."""
    for _ in range(60):
        code = f"{secrets.choice(_CODE_WORDS)}{secrets.randbelow(9000) + 1000}"
        if code in STUDENTS:
            continue
        if store.get_account(code):
            continue
        return code
    return f"STAR{secrets.token_hex(3).upper()}"   # astronomically unlikely fallback


def _issue_token(parent_id: str) -> str:
    token = secrets.token_hex(32)
    store.create_parent_token(token, parent_id, days=30)
    return token


# FAMILY PLAN (2026-08-03): one paid "seat" covers up to this many children, so a
# parent adding a SECOND child pays nothing more; the THIRD child needs a second
# seat, and so on in pairs. Change this one number to change the family policy.
# Oldest children are always covered first (see _student_tier), so buying fewer
# seats never bumps a currently-covered child to Free.
KIDS_PER_SEAT = 2


def _seats_for(n_children: int) -> int:
    """How many paid Stripe seats cover this many children (in pairs, rounded up).
    0 children -> 0 seats, 1 or 2 -> 1 seat, 3 or 4 -> 2 seats, and so on."""
    n = max(0, int(n_children or 0))
    return (n + KIDS_PER_SEAT - 1) // KIDS_PER_SEAT


def _covered_count(seats: int) -> int:
    """How many children `seats` paid seats cover (the inverse of _seats_for)."""
    return max(0, int(seats or 0)) * KIDS_PER_SEAT


def _parent_payload(parent: dict) -> dict:
    """The parent + family picture the /family page renders. One place, so signup,
    login, and refresh all return exactly the same shape."""
    students = store.list_students_for_parent(parent["id"])
    quantity = int(parent.get("sub_quantity") or 0)
    period_end = parent.get("sub_period_end")
    if period_end is not None and getattr(period_end, "tzinfo", None) is None:
        import datetime as _dt2                      # SQLite returns naive datetimes
        period_end = period_end.replace(tzinfo=_dt2.timezone.utc)
    return {
        "ok": True,
        "parent": {"email": parent.get("email"), "name": parent.get("name") or ""},
        "subscription": {
            "status": parent.get("sub_status") or "free",
            "plan": parent.get("sub_plan") or "",
            "quantity": quantity,
            "period_end": period_end.isoformat() if period_end else None,
        },
        "students": [{
            "code": s["code"],
            "name": s.get("name") or "Student",
            "covered": (parent.get("sub_status") == "active"
                        and i < _covered_count(quantity)),
        } for i, s in enumerate(students)],
        "billing_ready": _payments_open(),
    }


def _student_tier(code: str, student: dict) -> str:
    """What level of access does this student have RIGHT NOW?
      'pilot' -- a students.json persona (full access, unchanged forever)
      'full'  -- parent-managed, and the parent's subscription covers them
      'free'  -- parent-managed on the Free plan (placement + first unit + practice)
    Coverage is the parent's live sub_status + paid quantity: the OLDEST students
    are covered first, so adding a new child never bumps a paying child to free."""
    if not student.get("family"):
        return "pilot"
    try:
        parent = store.get_parent(student.get("parent_id") or "")
        if parent and (parent.get("sub_status") or "") == "active":
            quantity = int(parent.get("sub_quantity") or 0)
            kids = store.list_students_for_parent(parent["id"])
            for i, kid in enumerate(kids):
                if kid["code"] == code:
                    return "full" if i < _covered_count(quantity) else "free"
    except Exception as exc:  # noqa: BLE001 -- a billing lookup must never crash a lesson
        print(f"[tier] lookup failed for {code}: {exc}")
    return "free"


def _free_gate(code: str, student: dict, course: str):
    """The Free plan's promise, enforced kindly: one placement + a FIRST unit to
    try + unlimited practice & topic help. Lessons (session mode) stay open until
    the student has MASTERED one unit anywhere; after that, continuing lessons
    needs the Full plan. Returns None (allowed) or a warm message (blocked) --
    and the block happens BEFORE any paid Claude call."""
    if _student_tier(code, student) != "free":
        return None
    try:
        activity = store.get_course_activity(code)
        mastered = sum(int(v.get("units_mastered") or 0) for v in (activity or {}).values())
    except Exception as exc:  # noqa: BLE001
        print(f"[tier] activity lookup failed for {code}: {exc}")
        return None            # if we can't tell, do no harm: let the lesson through
    if mastered < 1:
        return None
    first = (student.get("name") or "there").split()[0]
    return (f"{first}, you did it — you mastered your first unit with me, and that's the whole "
            "free preview! I'd love to keep teaching you. Ask your parent to open the Family "
            "page at mrcadabra.com/family and upgrade your account — then we'll pick up right "
            "here where we left off. (Your Practice and Explore-a-topic tools still work "
            "anytime, free.)")


@app.post("/api/parent/signup")
def parent_signup(body: ParentSignupIn, request: Request):
    """Create a parent account. Free plan, no card, instant."""
    _require_db()
    _rate_limit("psignup:" + _client_ip(request), limit=5, window_seconds=3600,
                what="signup attempts")
    email = (body.email or "").strip().lower()
    if not _EMAIL_RE.match(email):
        raise HTTPException(status_code=400, detail="That doesn't look like an email address.")
    if len(body.password or "") < 8:
        raise HTTPException(status_code=400, detail="Please use a password of at least 8 characters.")
    parent_id = uuid.uuid4().hex
    if not store.create_parent(parent_id, email, body.name, _hash_password(body.password)):
        raise HTTPException(status_code=409, detail=(
            "That email already has an account — use Sign in instead."))
    token = _issue_token(parent_id)
    out = _parent_payload(store.get_parent(parent_id))
    out["token"] = token
    return out


@app.post("/api/parent/login")
def parent_login(body: ParentLoginIn, request: Request):
    _require_db()
    _rate_limit("plogin:" + _client_ip(request), limit=20, window_seconds=300,
                what="sign-in attempts")
    parent = store.get_parent_by_email(body.email)
    # Verify against a real or dummy hash either way, so a wrong email and a wrong
    # password take the same time (no probing which emails have accounts).
    stored = parent["password_hash"] if parent else _hash_password("timing-decoy")
    if not _verify_password(body.password, stored) or not parent:
        raise HTTPException(status_code=401, detail="Email or password didn't match.")
    token = _issue_token(parent["id"])
    out = _parent_payload(parent)
    out["token"] = token
    return out


# -----------------------------------------------------------------------------
# OUTBOUND EMAIL (2026-08-04) -- the app's first sender: password-reset links.
# Uses the EXISTING Titan mailbox over SMTP (no new service, no new cost); the
# same pipe will later carry the weekly parent email. Configure in Render:
#   SMTP_HOST=smtp.titan.email  SMTP_PORT=465
#   SMTP_USER=support@mrcadabra.com  SMTP_PASS=<mailbox password>
#   (optional SMTP_FROM, defaults to SMTP_USER; APP_BASE_URL, defaults below)
# -----------------------------------------------------------------------------
def _smtp_configured() -> bool:
    return bool(os.environ.get("SMTP_HOST") and os.environ.get("SMTP_USER")
                and os.environ.get("SMTP_PASS"))


def _send_email(to_addr: str, subject: str, body: str) -> str:
    """Send one plain-text email. Returns "" on success or the exact failure text
    on error; never raises (a mail hiccup must never 500 an API call). Secrets
    come from env only, and the failure text NEVER includes them."""
    if not _smtp_configured():
        return "SMTP env vars not set (need SMTP_HOST, SMTP_USER, SMTP_PASS)"
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr
    host = os.environ["SMTP_HOST"]
    port = int(os.environ.get("SMTP_PORT", "465") or 465)
    user = os.environ["SMTP_USER"]
    from_addr = os.environ.get("SMTP_FROM", user)
    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = formataddr(("Mr. Cadabra's Classroom", from_addr))
    msg["To"] = to_addr
    try:
        if port == 465:
            with smtplib.SMTP_SSL(host, port, timeout=20) as srv:
                srv.login(user, os.environ["SMTP_PASS"])
                srv.sendmail(from_addr, [to_addr], msg.as_string())
        else:
            with smtplib.SMTP(host, port, timeout=20) as srv:
                srv.starttls()
                srv.login(user, os.environ["SMTP_PASS"])
                srv.sendmail(from_addr, [to_addr], msg.as_string())
        return ""
    except Exception as exc:  # noqa: BLE001
        err = f"{type(exc).__name__}: {exc}"
        print(f"[email] send failed: {err}")
        return err


# =============================================================================
# OPS ALERTING (2026-08-05) -- Jim finds out from an email, not from a parent.
# -----------------------------------------------------------------------------
# _ops_alert() emails Jim about an operational problem, at most once per `kind`
# per throttle window (default 60 min -- a crash loop makes ONE email an hour,
# not a thousand). Sends on a background thread so an alert can never slow a
# student's lesson. The global exception handler below feeds it; so does the
# cost watchdog in the scheduler loop. Env (all optional):
#   ALERT_EMAIL        where alerts go (defaults to SMTP_USER, Jim's inbox)
#   ALERT_THROTTLE_MIN minutes between repeat alerts of the same kind (60)
#   COST_ALERT_USD     trailing-24h est. spend that triggers the cost alarm
# =============================================================================

_ALERT_LAST: dict = {}          # kind -> unix time of last email sent
_ALERT_LOCK = threading.Lock()


def _ops_alert(kind: str, subject: str, body: str,
               throttle_minutes: int | None = None) -> None:
    """Fire-and-forget ops email. Never raises; throttled per `kind`."""
    try:
        mins = (throttle_minutes if throttle_minutes is not None
                else int(os.environ.get("ALERT_THROTTLE_MIN", "60") or 60))
        to_addr = (os.environ.get("ALERT_EMAIL", "").strip()
                   or os.environ.get("SMTP_USER", "").strip())
        if not to_addr or not _smtp_configured():
            print(f"[ops] alert (email not configured) {kind}: {subject}")
            return
        now = time.time()
        with _ALERT_LOCK:
            if len(_ALERT_LAST) > 500:          # bounded memory, always
                _ALERT_LAST.clear()
            if now - _ALERT_LAST.get(kind, 0) < mins * 60:
                return                          # throttled -- already emailed recently
            _ALERT_LAST[kind] = now

        def _go():
            err = _send_email(to_addr, "[Mr. Cadabra ops] " + subject,
                body + "\n\n--\nAutomatic ops alert from mrcadabra.com (build "
                + APP_BUILD + "). Repeats of this alert kind are muted for "
                + str(mins) + " minutes.\nAdmin panel: https://mrcadabra.com/admin")
            if err:
                print(f"[ops] alert email failed ({kind}): {err}")
        threading.Thread(target=_go, daemon=True, name="ops-alert").start()
    except Exception as exc:  # noqa: BLE001 -- the alarm must never be the fire
        print(f"[ops] alert error: {exc}")


@app.exception_handler(Exception)
async def _unhandled_error(request: Request, exc: Exception):
    """Any unhandled crash on any route: log it, record it, email Jim (throttled),
    and answer the caller warmly instead of with a bare stack trace. Normal
    HTTPExceptions (sign-in prompts, validation answers) never come through here."""
    where = f"{request.method} {request.url.path}"
    what = f"{type(exc).__name__}: {exc}"
    print(f"[error] UNHANDLED {where}: {what}")
    try:
        store.record_error(where, what)
    except Exception:  # noqa: BLE001
        pass
    _ops_alert("err:" + type(exc).__name__ + ":" + request.url.path,
               f"Server error on {where}",
               f"An unhandled error just occurred.\n\nWhere: {where}\n"
               f"What:  {what}\n\nRecent errors are listed on /admin.")
    return JSONResponse(status_code=500, content={"detail": (
        "Something went wrong on our side — it's been logged and reported. "
        "Please try again in a moment.")})


def _ops_watch_pass() -> None:
    """Cost watchdog, called by the scheduler loop every 30 minutes. Silent unless
    Jim set COST_ALERT_USD in Render AND the price env vars exist (we never guess
    at dollars). Throttled to roughly one alert per 20 hours."""
    try:
        thr = os.environ.get("COST_ALERT_USD", "").strip()
        if not thr:
            return
        limit = float(thr)
        if limit <= 0:
            return
        u = _usage_with_dollars(1)             # trailing 24h, same math as /admin
        brain, tts = u.get("brain_usd"), u.get("tts_usd")
        if brain is None and tts is None:
            return                              # price env vars not set -- no invented dollars
        total = (brain or 0) + (tts or 0)
        if total >= limit:
            _ops_alert("cost24",
                f"spend in the last 24h is about ${total:.2f} (alarm set at ${limit:.2f})",
                "Estimated spend over the trailing 24 hours crossed your alarm threshold.\n\n"
                f"  Brain (Claude):     ${(brain or 0):.2f}\n"
                f"  Voice (ElevenLabs): ${(tts or 0):.2f}\n"
                f"  Total:              ${total:.2f}   (threshold ${limit:.2f})\n\n"
                "The full cost panel is on /admin. If this is expected growth — "
                "congratulations; raise COST_ALERT_USD in Render. If it isn't, check "
                "/admin for a runaway student or an abuse pattern.",
                throttle_minutes=1200)
    except Exception as exc:  # noqa: BLE001
        print(f"[ops] cost watch error: {exc}")


@app.post("/api/parent/forgot")
def parent_forgot(body: ParentForgotIn, request: Request):
    """Email a password-reset link. SAME answer whether or not the address has an
    account -- nobody gets to probe which emails are signed up. The token is
    single-use, expires in 45 minutes, and only its SHA-256 hash is stored."""
    _require_db()
    _rate_limit("pforgot:" + _client_ip(request), limit=5, window_seconds=3600,
                what="reset requests")
    email = (body.email or "").strip().lower()
    if not _EMAIL_RE.match(email):
        raise HTTPException(status_code=400, detail="That doesn't look like an email address.")
    _rate_limit("pforgot-email:" + email, limit=3, window_seconds=3600,
                what="reset requests")
    if not _smtp_configured():
        # Honest, not leaky: this reveals server config, never account existence.
        return {"ok": True, "sent": False,
                "note": ("Email isn't switched on here yet — write to support@mrcadabra.com "
                         "and we'll reset it for you.")}
    parent = store.get_parent_by_email(email)
    if not parent:
        # Same 200 response as the success path (no probing which emails have
        # accounts) -- but the server log tells Jim why nothing arrived.
        print("[email] forgot: no parent account matches that address -- no email sent")
    if parent:
        raw = secrets.token_urlsafe(32)
        token_hash = hashlib.sha256(raw.encode("utf-8")).hexdigest()
        store.create_parent_reset(token_hash, parent["id"], minutes=45)
        base = os.environ.get("APP_BASE_URL", "https://mrcadabra.com").rstrip("/")
        link = f"{base}/family?reset={raw}"
        send_err = _send_email(email, "Reset your Mr. Cadabra's Classroom password",
            "Hi" + ((" " + parent.get("name")) if parent.get("name") else "") + ",\n\n"
            "Someone asked to reset the password for this Mr. Cadabra's Classroom parent "
            "account. If that was you, open this link and choose a new password:\n\n"
            f"{link}\n\n"
            "The link works once and expires in 45 minutes.\n\n"
            "If you didn't ask for this, you can safely ignore this email — your password "
            "is unchanged and your children's learning is unaffected.\n\n"
            "— Mr. Cadabra's Classroom\nsupport@mrcadabra.com")
        if send_err:
            print(f"[email] forgot: send FAILED for a real account: {send_err}")
    return {"ok": True, "sent": True}


@app.get("/api/admin/email-test")
def admin_email_test(key: str = "", to: str = "",
                     x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    """Jim's email-pipe diagnostic (admin-key protected): sends ONE real test email
    and returns exactly what happened -- the precise SMTP failure text on error,
    and the active config WITHOUT the password. This is how we debug 'the email
    never arrived' without guessing.
    BUILD dg: key accepted in the X-Admin-Key header (preferred); the query param
    stays for a hand-typed URL, but remember it lands in Render's logs when used."""
    _require_admin(x_admin_key or key)
    cfg = {"SMTP_HOST": os.environ.get("SMTP_HOST", "(not set)"),
           "SMTP_PORT": os.environ.get("SMTP_PORT", "(not set -> 465)"),
           "SMTP_USER": os.environ.get("SMTP_USER", "(not set)"),
           "SMTP_FROM": os.environ.get("SMTP_FROM", "(defaults to SMTP_USER)"),
           "SMTP_PASS": "(set)" if os.environ.get("SMTP_PASS") else "(NOT SET)"}
    to = (to or "").strip()
    if not to or not _EMAIL_RE.match(to):
        return {"ok": False, "config": cfg,
                "error": "Add &to=your@email.address to send a test message."}
    err = _send_email(to, "Mr. Cadabra's Classroom — email pipe test",
                      "This is a test of the app's outbound email. If you're reading it, "
                      "the pipe works: password resets and (later) weekly parent emails "
                      "will deliver.\n\n— Mr. Cadabra's Classroom")
    return {"ok": not err, "sent_to": to if not err else None,
            "error": err or None, "config": cfg}


# -----------------------------------------------------------------------------
# WEEKLY PARENT EMAIL (2026-08-04) -- the promised Friday report, assembled from
# existing parts: _send_email (the proven SMTP pipe), store.week_activity (the
# honest windowed numbers), and tutor.get_assessment in parent voice (the same
# engine as the dashboard's "How are they doing, really?").
# -----------------------------------------------------------------------------
_DIGEST_WINDOW_DAYS = 7
_DIGEST_UTC_WEEKDAY = 4          # Friday (site promise: "Every Friday")
_DIGEST_UTC_HOUR_FROM = 20       # 20:00-23:59 UTC = Friday afternoon/evening US


def _app_base() -> str:
    return os.environ.get("APP_BASE_URL", "https://mrcadabra.com").rstrip("/")


def _fmt_minutes(m: int) -> str:
    m = int(m or 0)
    if m < 60:
        return f"{m}m"
    return f"{m // 60}h {m % 60:02d}m"


def _unit_display_name(course: str, unit: int) -> str:
    for i, u in enumerate(curriculum.units_for(course)):
        if isinstance(u, (list, tuple)) and len(u) >= 2:
            if int(u[0]) == int(unit):
                return str(u[1])
        elif i + 1 == int(unit):
            return str(u)
    return f"Unit {unit}"


def _weekly_child_section(student: dict, week: dict) -> str:
    """One child's block of the digest: honest week numbers, template-built
    (deterministic, free). The AI paragraph is added separately by the caller."""
    name = (student.get("name") or "Your student").strip() or "Your student"
    lines = [f"------  {name.upper()}  ------"]
    if week["minutes_total"] <= 0 and not week["checks"] and not week["touched"]:
        lines.append(f"No tutoring sessions this week. {name}'s login code works any "
                     "time -- even ten minutes of practice moves the needle, and "
                     "Mr. Cadabra picks up exactly where they left off.")
        return "\n".join(lines)
    lines.append(f"This week: {_fmt_minutes(week['minutes_total'])} of real work across "
                 f"{week['days_active']} day(s). Idle time never counts.")
    if len(week["minutes_by_course"]) > 1:
        parts = [f"{curriculum.course_title(c)} {_fmt_minutes(m)}"
                 for c, m in sorted(week["minutes_by_course"].items(),
                                    key=lambda kv: -kv[1]) if m > 0]
        if parts:
            lines.append("By course: " + "; ".join(parts) + ".")
    if week["checks"]:
        parts = []
        for c in week["checks"]:
            uname = _unit_display_name(c["course"], c["unit"])
            if c["best_pct"] >= store.PASS_PCT:
                parts.append(f"{uname} -- {c['best_pct']}% (MASTERED, 90%+ bar)")
            else:
                parts.append(f"{uname} -- best so far {c['best_pct']}% (mastery is 90%+)")
        lines.append("Unit checks this week: " + "; ".join(parts) + ".")
    touched_named = [t["unit_name"] for t in week["touched"] if t.get("unit_name")]
    if touched_named:
        seen, uniq = set(), []
        for n in touched_named:
            if n not in seen:
                seen.add(n)
                uniq.append(n)
        lines.append("Worked on: " + ", ".join(uniq[:6]) +
                     ("..." if len(uniq) > 6 else "") + ".")
    if week["award_ids"]:
        names = [f"{AWARD_DEFS[a][0]} {AWARD_DEFS[a][1]}"
                 for a in week["award_ids"] if a in AWARD_DEFS]
        if names:
            lines.append("New awards earned: " + ", ".join(names) + ".")
    # 2026-08-11 (build du, parent lens item 6): the question every parent asks --
    # "what did they struggle with?" -- answered with the ACTUAL problems from this
    # week's quizzes (rule 55's rows). Capped at 3; absent when the week had none.
    try:
        import datetime as _dt
        cutoff = (_dt.date.today() - _dt.timedelta(days=7)).isoformat()
        tricky = [m for m in store.get_misses(student.get("code") or "", limit=15)
                  if (m.get("when") or "") >= cutoff][:3]
    except Exception as exc:  # noqa: BLE001
        print(f"[digest] get_misses failed (ignored): {exc}")
        tricky = []
    if tricky:
        lines.append("Tricky this week (worth five minutes together): " + "; ".join(
            f"\"{m['question']}\" -- they answered \"{m['answer']}\"" for m in tricky)
            + ". Mr. Cadabra brings one of these back himself, gently, next session.")
    return "\n".join(lines)


def _weekly_ai_summary(code: str, student: dict, week: dict) -> str:
    """The parent-voice analytical paragraph for this child's most-worked course
    this week. Returns "" on any problem -- the numbers-only email still goes out."""
    active = {c: m for c, m in week["minutes_by_course"].items() if m > 0}
    if not active:
        return ""
    course = max(active, key=active.get)
    if course not in curriculum.COURSES:
        return ""
    try:
        facts = _assessment_facts(code, student, course)
        facts += (f"\nTHIS SPECIFIC WEEK (the report period): "
                  f"{week['minutes_total']} real working minutes across "
                  f"{week['days_active']} active day(s); "
                  f"{len(week['checks'])} unit check(s) taken; "
                  f"{len(week['award_ids'])} new award(s) earned.")
        text = tutor.get_assessment(facts, "parent", code=code, course=course)
        if not text or text.startswith("("):
            return ""
        return text.strip()
    except Exception as exc:  # noqa: BLE001
        print(f"[digest] AI summary failed for {code}: {exc}")
        return ""


def _build_weekly_digest(parent: dict):
    """(subject, body) for this parent's weekly email, or (None, None) when there
    is nothing to send (no children). Never raises."""
    children = store.list_students_for_parent(parent["id"])
    if not children:
        return None, None
    state = store.ensure_digest_state(parent["id"])
    names = [(c.get("name") or "").strip() or "your student" for c in children]
    if len(names) == 1:
        subject = f"{names[0]}'s week with Mr. Cadabra's Classroom"
    elif len(names) == 2:
        subject = f"{names[0]} & {names[1]}'s week with Mr. Cadabra's Classroom"
    else:
        subject = "Your family's week with Mr. Cadabra's Classroom"
    pname = (parent.get("name") or "").strip()
    blocks = [f"Hi{(' ' + pname) if pname else ''},",
              "Here's the honest weekly report -- real numbers from real work, "
              "never padded."]
    for child in children:
        week = store.week_activity(child["code"], days=_DIGEST_WINDOW_DAYS)
        blocks.append(_weekly_child_section(child, week))
        ai = _weekly_ai_summary(child["code"], child, week)
        if ai:
            blocks.append(ai)
    base = _app_base()
    blocks.append(f"Full dashboard any time: {base}/family")
    blocks.append("Questions? Just reply to this email, or write "
                  "support@mrcadabra.com -- a person reads it.")
    blocks.append("--\nYou're receiving this weekly report because you have a "
                  "Mr. Cadabra's Classroom parent account.\n"
                  f"Unsubscribe (one click): {base}/api/parent/weekly-email/"
                  f"unsubscribe?token={state['optout_token']}\n"
                  "Mr. Cadabra's Classroom · Hyperion Shift LLC")
    return subject, "\n\n".join(blocks)


@app.get("/api/parent/weekly-email/unsubscribe")
def weekly_email_unsubscribe(request: Request, token: str = "", resub: str = ""):
    """One-click unsubscribe from the weekly report (the token grants ONLY this).
    ?resub=1 flips it back on -- the confirmation page offers exactly that."""
    _require_db()
    _rate_limit("unsub:" + _client_ip(request), limit=30, window_seconds=3600,
                what="unsubscribe requests")
    pid = store.parent_id_for_digest_token(token)
    page_top = ("<!doctype html><html><head><meta charset='utf-8'>"
                "<meta name='viewport' content='width=device-width,initial-scale=1'>"
                "<title>Weekly email — Mr. Cadabra's Classroom</title>"
                "<style>body{font-family:system-ui,sans-serif;background:#f7f6ff;"
                "margin:0;display:grid;place-items:center;min-height:100vh}"
                ".card{background:#fff;border:1px solid #e5e2f5;border-radius:14px;"
                "padding:34px 38px;max-width:460px;box-shadow:0 8px 30px rgba(60,50,140,.08)}"
                "h1{font-size:21px;color:#3d3480;margin:0 0 10px}p{color:#555;line-height:1.5}"
                "a{color:#5b5bd6}</style></head><body><div class='card'>")
    page_end = "</div></body></html>"
    if not pid:
        return Response(page_top + "<h1>That link isn't valid</h1>"
                        "<p>It may be from an old email. Nothing was changed. If you "
                        "want to stop the weekly report, use the link in your most "
                        "recent email, or write support@mrcadabra.com.</p>" + page_end,
                        media_type="text/html")
    if (resub or "").strip() == "1":
        store.set_digest_optout(pid, False)
        return Response(page_top + "<h1>Welcome back 👋</h1>"
                        "<p>The weekly report is switched on again. The next one "
                        "arrives Friday.</p>" + page_end, media_type="text/html")
    store.set_digest_optout(pid, True)
    return Response(page_top + "<h1>You're unsubscribed</h1>"
                    "<p>No more weekly report emails. Your account and your "
                    "children's tutoring are completely unaffected, and the same "
                    "numbers are always on your parent dashboard.</p>"
                    f"<p>Changed your mind? <a href='/api/parent/weekly-email/"
                    f"unsubscribe?token={token}&resub=1'>Turn it back on</a>.</p>"
                    + page_end, media_type="text/html")


@app.get("/api/admin/digest-test")
def admin_digest_test(key: str = "", email: str = "", to: str = "",
                      x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    """Jim's weekly-email diagnostic (admin-key protected): builds a REAL parent's
    digest and returns it as JSON WITHOUT sending. Add &to=an@address to also send
    exactly one copy there for eyeballing. Never marks the parent as sent.
    BUILD dg: key accepted in the X-Admin-Key header (preferred); the query param
    stays for a hand-typed URL, but remember it lands in Render's logs when used."""
    _require_admin(x_admin_key or key)
    _require_db()
    email = (email or "").strip().lower()
    if not email:
        return {"ok": False, "error": "Add &email=<parent email> to pick the parent."}
    parent = store.get_parent_by_email(email)
    if not parent:
        return {"ok": False, "error": "No parent account with that email."}
    subject, body = _build_weekly_digest(parent)
    if not subject:
        return {"ok": False, "error": "That parent has no children yet -- nothing to send."}
    sent_to, err = None, None
    to = (to or "").strip()
    if to:
        if not _EMAIL_RE.match(to):
            err = "That &to= address doesn't look like an email."
        else:
            err = _send_email(to, subject, body) or None
            sent_to = to if not err else None
    return {"ok": err is None, "subject": subject, "body": body,
            "sent_to": sent_to, "error": err}


def _weekly_digest_pass(force: bool = False) -> dict:
    """One send pass: every parent who is due gets this week's email. Returns
    counts for the log. `force` ignores the Friday window (admin/testing only --
    the 3-day resend guard still applies)."""
    from datetime import datetime, timezone
    out = {"checked": 0, "sent": 0, "skipped": 0, "failed": 0}
    if not (store.enabled() and _smtp_configured()):
        return out
    now = datetime.now(timezone.utc)
    if not force and not (now.weekday() == _DIGEST_UTC_WEEKDAY
                          and now.hour >= _DIGEST_UTC_HOUR_FROM):
        return out
    for parent in store.list_parents():
        out["checked"] += 1
        try:
            state = store.ensure_digest_state(parent["id"])
            if int(state.get("optout") or 0):
                out["skipped"] += 1
                continue
            last = state.get("last_sent_at")
            if last is not None:
                if hasattr(last, "tzinfo") and last.tzinfo is None:
                    last = last.replace(tzinfo=timezone.utc)
                if (now - last).total_seconds() < 3 * 86400:
                    out["skipped"] += 1
                    continue
            subject, body = _build_weekly_digest(parent)
            if not subject:
                out["skipped"] += 1
                continue
            err = _send_email(parent["email"], subject, body)
            if err:
                out["failed"] += 1
                print(f"[digest] send FAILED for parent {parent['id']}: {err}")
            else:
                store.mark_digest_sent(parent["id"])
                out["sent"] += 1
        except Exception as exc:  # noqa: BLE001
            out["failed"] += 1
            print(f"[digest] pass error for parent {parent.get('id')}: {exc}")
    if out["sent"] or out["failed"]:
        print(f"[digest] pass done: {out}")
    return out


def _digest_loop():
    """Daemon thread: wake every 30 minutes; inside the Friday window, send to
    everyone due. Restart-safe (last_sent_at lives in the database) and duplicate-
    safe (the 3-day guard means one send per parent per window).
    2026-08-05: the same heartbeat now also runs the ops cost watchdog
    (_ops_watch_pass) -- each pass is fenced in its own try so one failing can
    never stop the other."""
    while True:
        time.sleep(1800)          # sleep FIRST: never race the module import at boot
        try:
            _weekly_digest_pass()
        except Exception as exc:  # noqa: BLE001
            print(f"[digest] loop error: {exc}")
        try:
            _ops_watch_pass()
        except Exception as exc:  # noqa: BLE001
            print(f"[ops] watch loop error: {exc}")
        # build cn: the usage log is one row per model call and per TTS request. At
        # 10,000 students that is millions of rows a month, and nothing ever removed
        # one. The cost dashboard only ever looks back weeks, so anything older than
        # USAGE_LOG_DAYS is dead weight in the same database the lessons run on.
        try:
            _usage_purge_pass()
        except Exception as exc:  # noqa: BLE001
            print(f"[usage] purge loop error: {exc}")
        # build dj: the nightly database snapshot rides the same heartbeat, fenced in
        # its own try like everything else here -- a failing backup must never stop
        # the digests, and vice versa. The pass itself decides whether a day has gone
        # by (it reads the newest file on disk, so it is restart-safe).
        try:
            _backup_pass()
        except Exception as exc:  # noqa: BLE001
            print(f"[backup] loop error: {exc}")


USAGE_LOG_DAYS = int(os.environ.get("USAGE_LOG_DAYS", "180") or 180)
_last_usage_purge = [0.0]


# =============================================================================
# NIGHTLY DATABASE SNAPSHOT (2026-08-11, build dj)
# -----------------------------------------------------------------------------
# Jim: "if Render falters or something falters, do we have sufficient backup so that
# we could recreate everything right away?" The honest answer was NO for exactly one
# asset: the database. This writes one gzipped JSON snapshot of every table per day
# to DATA_DIR/backups -- which since the 08-11 infrastructure change is the Render
# PERSISTENT DISK, so snapshots survive deploys. Restart-safe (the gate is the newest
# file's mtime on disk, not process memory), atomic (write .tmp, then rename), and
# rotated (BACKUP_KEEP newest are kept, default 14). Copies leave the machine via the
# /admin download button -- the third copy lives on Jim's own computer. The full
# recovery drill is RECOVERY.md in the repo.
# =============================================================================
BACKUP_KEEP = int(os.environ.get("BACKUP_KEEP", "14") or 14)
_BACKUP_DIR = DATA_DIR / "backups"


def _backup_blob() -> tuple[bytes, dict]:
    """The current database as gzipped JSON bytes, plus the snapshot's row counts."""
    snap = store.export_all()
    blob = gzip.compress(json.dumps(snap, separators=(",", ":")).encode("utf-8"))
    return blob, snap["row_counts"]


def _backup_pass() -> None:
    """Write today's snapshot if a day has passed since the newest one on disk.
    Called from the 30-minute heartbeat; silent and harmless when the DB is off."""
    if not store.enabled() or BACKUP_KEEP <= 0:
        return
    _BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    existing = sorted(_BACKUP_DIR.glob("backup-*.json.gz"))
    if existing:
        newest = max(p.stat().st_mtime for p in existing)
        if time.time() - newest < 24 * 3600 - 300:   # 5-min grace so the slot can't drift
            return
    blob, counts = _backup_blob()
    name = "backup-" + time.strftime("%Y%m%d-%H%M%S", time.gmtime()) + ".json.gz"
    tmp = _BACKUP_DIR / (name + ".tmp")
    tmp.write_bytes(blob)
    os.replace(tmp, _BACKUP_DIR / name)              # atomic: never a half-written snapshot
    print(f"[backup] wrote {name} ({len(counts)} tables, {sum(counts.values())} rows, "
          f"{len(blob):,} bytes)")
    for p in sorted(_BACKUP_DIR.glob("backup-*.json.gz"))[:-BACKUP_KEEP]:
        try:
            p.unlink()
            print(f"[backup] rotated out {p.name}")
        except OSError as exc:
            print(f"[backup] rotation could not remove {p.name}: {exc}")


def _usage_purge_pass() -> None:
    """Drop usage rows older than USAGE_LOG_DAYS. Runs at most once a day, from the
    heartbeat that already exists. Counts only -- no conversation text was ever in
    there. Silent and harmless when the DB is off."""
    if not store.enabled() or USAGE_LOG_DAYS <= 0:
        return
    now = time.monotonic()
    if _last_usage_purge[0] and now - _last_usage_purge[0] < 86400:
        return
    _last_usage_purge[0] = now
    removed = store.purge_usage_log(USAGE_LOG_DAYS)
    if removed:
        print(f"[usage] purged {removed} rows older than {USAGE_LOG_DAYS} days")


_digest_thread_started = False


def _start_digest_thread() -> None:
    global _digest_thread_started
    if _digest_thread_started:
        return
    if os.environ.get("WEEKLY_EMAIL", "on").strip().lower() in ("off", "0", "false", "no"):
        print("[digest] WEEKLY_EMAIL=off -- weekly parent email scheduler disabled")
        return
    _digest_thread_started = True
    threading.Thread(target=_digest_loop, daemon=True, name="weekly-digest").start()


_start_digest_thread()


@app.post("/api/parent/reset")
def parent_reset(body: ParentResetIn, request: Request):
    """Redeem a reset link: set the new password and sign the parent out everywhere."""
    _require_db()
    _rate_limit("preset:" + _client_ip(request), limit=10, window_seconds=3600,
                what="reset attempts")
    if len(body.password or "") < 8:
        raise HTTPException(status_code=400, detail="Please use a password of at least 8 characters.")
    token_hash = hashlib.sha256((body.token or "").encode("utf-8")).hexdigest()
    parent_id = store.consume_parent_reset(token_hash)
    if not parent_id:
        raise HTTPException(status_code=400, detail=(
            "That reset link isn't valid anymore — it may have expired (they last 45 minutes) "
            "or already been used. Request a fresh one from the Sign in page."))
    store.update_parent(parent_id, password_hash=_hash_password(body.password))
    store.delete_parent_tokens_for(parent_id)      # whoever had the old password is out
    return {"ok": True}


@app.post("/api/parent/logout")
def parent_logout(body: ParentTokenIn):
    _require_db()
    store.delete_parent_token((body.token or "").strip())
    return {"ok": True}


@app.get("/api/parent/me")
def parent_me(request: Request):
    """The signed-in parent's family picture. Token comes in the X-Parent-Token header."""
    parent = _require_parent(request.headers.get("x-parent-token", ""))
    return _parent_payload(parent)


@app.post("/api/parent/students")
def parent_add_student(body: ParentStudentIn):
    """Add a child (first name only) and mint their login code."""
    parent = _require_parent(body.token)
    name = (body.name or "").strip()[:40]
    if not name:
        raise HTTPException(status_code=400, detail="Please enter your child's first name.")
    existing = store.list_students_for_parent(parent["id"])
    if len(existing) >= 8:
        raise HTTPException(status_code=400, detail=(
            "That's 8 students on one account — email support@mrcadabra.com and "
            "we'll set your family up properly."))
    code = _new_student_code()
    store.create_student_account(code, name, parent["id"])
    return _parent_payload(parent)


@app.get("/api/parent/overview")
def parent_overview(request: Request):
    """MISSION CONTROL for /family (build dq -- Four-Lens Review, homeschool item 1).
    One parent-token-gated call returns the numbers a parent actually wants next to
    each child's name: real minutes this week (idle never counts), active days, total
    units mastered, last-active date, and the child's most-worked course (so the
    "How are they doing?" button asks about the right one) -- plus the weekly-email
    setting so the page can show the toggle. Every per-child block is wrapped: a
    stats panel is a BONUS and must never break the family page."""
    parent = _require_parent(request.headers.get("x-parent-token", ""))
    import datetime as _dt
    today = _dt.date.today()
    week_ago = (today - _dt.timedelta(days=6)).isoformat()
    titles = dict(curriculum.list_courses())
    kids = []
    for s in store.list_students_for_parent(parent["id"]):
        code = s["code"]
        minutes, days_set, per_course = 0, set(), {}
        try:
            for row in store.get_time_between(code, week_ago, today.isoformat()):
                m = int(row.get("minutes") or 0)
                minutes += m
                if m:
                    days_set.add(row.get("day"))
                    per_course[row["course"]] = per_course.get(row["course"], 0) + m
        except Exception:  # noqa: BLE001
            pass
        mastered, last_active, act = 0, None, {}
        try:
            act = store.get_course_activity(code)
            for a in act.values():
                mastered += int(a.get("units_mastered") or 0)
                la = a.get("last_active")
                if la and (last_active is None or la > last_active):
                    last_active = la
        except Exception:  # noqa: BLE001
            pass
        top = max(per_course, key=per_course.get) if per_course else None
        if not top and act:
            top = max(act, key=lambda c: act[c].get("last_active") or "")
        steer = None
        try:
            s = store.get_steer(code)
            if s and 1 <= int(s.get("unit") or 0) <= 9:
                steer = {"course": s["course"], "unit": s["unit"],
                         "course_title": titles.get(s["course"], s["course"]),
                         "unit_name": curriculum.unit_name(s["course"], s["unit"])}
        except Exception:  # noqa: BLE001
            pass
        kids.append({"code": code, "minutes_week": minutes,
                     "active_days_week": len(days_set), "units_mastered": mastered,
                     "last_active": last_active, "top_course": top,
                     "top_course_title": titles.get(top, ""), "steer": steer})
    state = store.ensure_digest_state(parent["id"])
    return {"ok": True, "students": kids,
            "weekly_email_on": not int(state.get("optout") or 0)}


class WeeklyEmailIn(BaseModel):
    token: str = ""
    on: bool = True


@app.post("/api/parent/weekly-email")
def parent_weekly_email(body: WeeklyEmailIn, request: Request):
    """The IN-PRODUCT toggle for the Friday report (build dq). Before this, the only
    way to stop the weekly email was the tokenized link inside the email itself --
    a setting with no switch. Same store flag the unsubscribe link flips."""
    parent = _require_parent(body.token or request.headers.get("x-parent-token", ""))
    store.set_digest_optout(parent["id"], not bool(body.on))
    return {"ok": True, "on": bool(body.on)}


# =============================================================================
# PARENT CHILD-MANAGEMENT (2026-08-11, build dy -- Four-Lens parent item 2).
# Rename / new code / remove / attach: everything that used to be a support email.
# Every endpoint is parent-token gated AND ownership-checked -- a parent can only
# ever touch their OWN children. Remove additionally demands the child's name typed
# back (a mis-tap must never delete a childhood of progress).
# =============================================================================
class ParentChildIn(BaseModel):
    token: str = ""
    code: str = ""
    name: str = ""             # rename: the new name · remove: the typed confirmation


def _own_student(parent: dict, code: str) -> str:
    """The child must be THIS parent's. 404 (not 403) on a miss: an outsider probing
    codes learns nothing about which codes exist."""
    code = (code or "").strip()
    mine = {s["code"] for s in store.list_students_for_parent(parent["id"])}
    if code not in mine:
        raise HTTPException(status_code=404, detail="That student isn't on your account.")
    return code


class ParentSteerIn(BaseModel):
    token: str = ""
    code: str = ""
    course: str = ""
    unit: int = 0              # 1-9 sets the plan; 0 clears it


@app.post("/api/parent/student-steer")
def parent_student_steer(body: ParentSteerIn, request: Request):
    """The pacing control (build ea): "center their sessions on Unit N for now."
    Applies when the child opens that course without a focus of their own; the
    child's explicit choice always outranks it (rule 50). unit=0 clears the plan."""
    parent = _require_parent(body.token or request.headers.get("x-parent-token", ""))
    code = _own_student(parent, body.code)
    unit = int(body.unit or 0)
    if unit == 0:
        store.clear_steer(code)
        return _parent_payload(store.get_parent(parent["id"]))
    if not (1 <= unit <= 9):
        raise HTTPException(status_code=400, detail="Pick a unit from 1 to 9 (or clear the plan).")
    course = (body.course or "").strip()
    if course not in curriculum.COURSES:
        # default to where the child actually works: most engaged-time course, else
        # most recently active, else algebra1 -- resolved HERE so the page never
        # needs its own course list (unit names live in six files already; no seventh).
        try:
            act = store.get_course_activity(code)
            course = max(act, key=lambda c: act[c].get("last_active") or "") if act else "algebra1"
        except Exception:  # noqa: BLE001
            course = "algebra1"
    store.set_steer(code, course, unit)
    return _parent_payload(store.get_parent(parent["id"]))


@app.post("/api/parent/student-rename")
def parent_student_rename(body: ParentChildIn, request: Request):
    parent = _require_parent(body.token or request.headers.get("x-parent-token", ""))
    code = _own_student(parent, body.code)
    name = (body.name or "").strip()[:40]
    if not name:
        raise HTTPException(status_code=400, detail="Please enter the new name.")
    store.rename_student(code, name)
    return _parent_payload(store.get_parent(parent["id"]))


@app.post("/api/parent/student-newcode")
def parent_student_newcode(body: ParentChildIn, request: Request):
    """A leaked login code is a leaked key. Mint a fresh one; every scrap of the
    child's history moves with it in one transaction; the old code dies instantly."""
    parent = _require_parent(body.token or request.headers.get("x-parent-token", ""))
    code = _own_student(parent, body.code)
    new_code = _new_student_code()
    res = store.change_student_code(code, new_code)
    if not res.get("ok"):
        raise HTTPException(status_code=500, detail="Couldn't change the code — nothing was altered. Try again.")
    out = _parent_payload(store.get_parent(parent["id"]))
    out["new_code"] = new_code
    return out


@app.post("/api/parent/student-remove")
def parent_student_remove(body: ParentChildIn, request: Request):
    """PERMANENT. Deletes the child's account and every per-student row (the same
    cascade Start Fresh uses -- accounts is in the reset family). The parent must
    type the child's name back exactly (case-insensitive) as consent."""
    parent = _require_parent(body.token or request.headers.get("x-parent-token", ""))
    code = _own_student(parent, body.code)
    acct = store.get_account(code) or {}
    want = (acct.get("name") or "").strip().lower()
    typed = (body.name or "").strip().lower()
    if not want or typed != want:
        raise HTTPException(status_code=400, detail=(
            "To remove this student, type their name exactly as it appears — this "
            "permanently deletes their progress."))
    store.reset_student_data(code)
    return _parent_payload(store.get_parent(parent["id"]))


@app.post("/api/parent/student-attach")
def parent_student_attach(body: ParentChildIn, request: Request):
    """Attach an existing UNOWNED student code (an early beta student, a code made
    before the parent signed up). A code owned by another parent is never
    transferable here; pilot demo codes can't be claimed at all."""
    parent = _require_parent(body.token or request.headers.get("x-parent-token", ""))
    _require_db()
    code = (body.code or "").strip().upper()
    if not code:
        raise HTTPException(status_code=400, detail="Please enter the student's login code.")
    if code in STUDENTS:
        raise HTTPException(status_code=400, detail="That's a shared demo code — it can't join a family account.")
    result = store.attach_student(code, parent["id"])
    if result == "missing":
        raise HTTPException(status_code=404, detail="No student found with that code — check it letter by letter.")
    if result == "owned":
        raise HTTPException(status_code=409, detail=(
            "That code already belongs to another family account. If it's yours, "
            "email support@mrcadabra.com and a person will sort it out."))
    return _parent_payload(store.get_parent(parent["id"]))


# =============================================================================
# BETA PASS ADMIN (2026-07-31) -- Jim's generator
# -----------------------------------------------------------------------------
# Keyed on FORUM_MOD_KEY (Jim's one admin key). The /beta page shows a generator
# panel when opened as /beta?admin=<key>; these endpoints back it.
# =============================================================================

class BetaCreateIn(BaseModel):
    key: str
    label: str = ""            # who this pass is for (shows only to Jim)
    uses: int = 5
    hours: int = 2


class BetaRevokeIn(BaseModel):
    key: str
    code: str


def _require_admin(key: str) -> None:
    admin = os.environ.get("FORUM_MOD_KEY", "").strip()
    if not admin or not hmac.compare_digest((key or "").strip(), admin):
        raise HTTPException(status_code=401, detail="Not authorized.")


def _new_beta_code() -> str:
    for _ in range(60):
        code = f"TRY-{secrets.choice(_CODE_WORDS)}{secrets.randbelow(90) + 10}"
        if code in STUDENTS or store.get_account(code) or store.get_beta_code(code):
            continue
        return code
    return f"TRY-{secrets.token_hex(3).upper()}"


@app.post("/api/beta/create")
def beta_create(body: BetaCreateIn):
    _require_db()
    _require_admin(body.key)
    code = _new_beta_code()
    store.create_beta_code(code, body.label, body.uses, body.hours)
    return {"ok": True, "code": code, "codes": store.list_beta_codes()}


@app.get("/api/beta/list")
def beta_list(key: str = "",
              x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    # BUILD dg: the key belongs in the X-Admin-Key HEADER -- query strings are written
    # into Render's request logs in plaintext. The query param stays accepted so old
    # bookmarks keep working, but no page we ship sends it that way any more.
    _require_db()
    _require_admin(x_admin_key or key)
    return {"ok": True, "codes": store.list_beta_codes()}


@app.post("/api/beta/revoke")
def beta_revoke(body: BetaRevokeIn):
    _require_db()
    _require_admin(body.key)
    if not store.revoke_beta_code(body.code):
        raise HTTPException(status_code=404, detail="No pass with that code.")
    return {"ok": True, "codes": store.list_beta_codes()}


@app.post("/api/beta/delete")
def beta_delete(body: BetaRevokeIn):
    """2026-08-07 (build bb, Jim): fully DELETE a beta pass -- the pass row AND every
    scrap of student data recorded under that code (sessions, progress, quizzes, stats,
    time, awards, final exams, account). Revoke only disables the code and leaves the
    data; this is the true 'this tester never happened' button. Admin-key protected."""
    _require_db()
    _require_admin(body.key)
    res = store.delete_beta_cascade(body.code)
    if not res.get("existed"):
        raise HTTPException(status_code=404, detail="No pass with that code.")
    return {"ok": True, "deleted": res.get("deleted") or {}, "codes": store.list_beta_codes()}


# =============================================================================
# ADMIN DASHBOARD (2026-08-03) -- Jim's one-stop status + tools page at /admin.
# Keyed on the SAME FORUM_MOD_KEY as the beta generator and forum moderation.
# Returns only aggregate COUNTS/TOTALS (store.admin_stats()) plus the same facts
# /health shows -- never a child's name, a parent's email, or a login code.
# =============================================================================

def _usage_with_dollars(days: int) -> dict:
    """store.usage_stats(days) plus estimated DOLLARS -- computed ONLY from prices Jim
    sets in Render env vars (nothing invented; dollars stay null until prices exist):
      ANTHROPIC_IN_USD_PER_MTOK   price per MILLION input tokens
      ANTHROPIC_OUT_USD_PER_MTOK  price per MILLION output tokens
      ELEVEN_USD_PER_1K_CHARS     price per 1,000 ElevenLabs characters
    Cache math per Anthropic's published multipliers: cached reads bill at 10% of the
    input price; cache writes at 125%."""
    u = store.usage_stats(days)
    def _price(name):
        try:
            v = os.environ.get(name, "").strip()
            return float(v) if v else None
        except ValueError:
            return None
    pin, pout = _price("ANTHROPIC_IN_USD_PER_MTOK"), _price("ANTHROPIC_OUT_USD_PER_MTOK")
    ptts = _price("ELEVEN_USD_PER_1K_CHARS")
    brain_usd = tts_usd = None
    if pin is not None and pout is not None:
        brain_usd = round((u["input_tokens"] * pin
                           + u["cache_read_tokens"] * pin * 0.10
                           + u["cache_write_tokens"] * pin * 1.25
                           + u["output_tokens"] * pout) / 1_000_000, 2)
    if ptts is not None:
        tts_usd = round(u["tts_chars_generated"] / 1000 * ptts, 2)
    u["brain_usd"] = brain_usd
    u["tts_usd"] = tts_usd
    u["total_usd"] = round(brain_usd + tts_usd, 2) if (brain_usd is not None and tts_usd is not None) else None
    return u


@app.get("/api/admin/stats")
def admin_stats_api(key: str = "",
                    x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    """The numbers behind /admin. Admin-key protected (constant-time compare).
    BUILD dg: key accepted in the X-Admin-Key header (preferred -- query strings land
    in Render's logs); the query param stays for old bookmarks only."""
    _require_db()
    _require_admin(x_admin_key or key)
    return {
        "ok": True,
        "build": APP_BUILD,
        "model": os.environ.get("CLAUDE_MODEL", tutor.DEFAULT_MODEL),
        "payments_open": _payments_open(),
        "storage": store.status(),
        "stats": store.admin_stats(),
        "usage7": _usage_with_dollars(7),
        "usage30": _usage_with_dollars(30),
        # OPS (2026-08-05): unhandled-error visibility for the System section.
        "errors24": store.errors_count(24),
        "errors_recent": store.recent_errors(24, 20),
    }


# =============================================================================
# BACKUP ENDPOINTS (2026-08-11, build dj) -- download and status. READ-ONLY both:
# there is deliberately NO restore endpoint (a remote wipe-and-replace is a foot-gun;
# restores run offline via restore_backup.py with an explicit flag). Key rides in the
# X-Admin-Key header like every admin call since build dg.
# =============================================================================
@app.get("/api/admin/backup/status")
def admin_backup_status(key: str = "",
                        x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    """What the nightly snapshot has been doing: every snapshot on the persistent
    disk, newest first, plus the retention setting. Feeds the /admin Backups card."""
    _require_admin(x_admin_key or key)
    snaps = []
    try:
        for p in sorted(_BACKUP_DIR.glob("backup-*.json.gz"), reverse=True):
            st = p.stat()
            snaps.append({"name": p.name, "bytes": st.st_size,
                          "written_utc": time.strftime("%Y-%m-%d %H:%M UTC",
                                                       time.gmtime(st.st_mtime))})
    except OSError:
        pass
    return {"ok": True, "db": store.enabled(), "keep": BACKUP_KEEP,
            "dir": str(_BACKUP_DIR), "snapshots": snaps}


@app.get("/api/admin/backup")
def admin_backup_download(key: str = "",
                          x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    """A FRESH full snapshot, streamed as a download -- not a file from the disk, so
    what Jim saves is the database as of this click. This is the offsite copy: the
    nightly file protects against deploys and app mistakes; this one protects against
    losing Render itself."""
    _require_admin(x_admin_key or key)
    _require_db()
    blob, counts = _backup_blob()
    fname = "mrcadabra-backup-" + time.strftime("%Y%m%d-%H%M%S", time.gmtime()) + ".json.gz"
    return Response(blob, media_type="application/gzip",
                    headers={"Content-Disposition": f'attachment; filename="{fname}"',
                             "X-Backup-Rows": str(sum(counts.values())),
                             "X-Backup-Tables": str(len(counts))})


# =============================================================================
# ADMIN "START FRESH" (2026-08-05) -- full reset of ONE parent account by email.
# -----------------------------------------------------------------------------
# Jim's testing tool: delete his own parent account so he can re-run the brand-
# new-parent signup with the same email and see the site exactly as a first-time
# visitor would. Admin-key gated (same FORUM_MOD_KEY as every other admin tool),
# scoped to the ONE email passed in. It deletes that parent + their children +
# all their data (store.delete_parent_cascade, atomic); it never touches another
# account, the admin key, or any Render env var.
# =============================================================================

class ParentResetAdminIn(BaseModel):
    key: str
    email: str


class PrewarmAdminIn(BaseModel):
    key: str
    course: str = ""       # blank = every course
    limit: int = 0         # 0 = no cap; otherwise render at most this many this call
    dry_run: bool = False   # count and price it without spending anything


class LessonAuditIn(BaseModel):
    key: str
    limit: int = 2          # scenarios THIS call -- a lesson takes a minute or two
    offset: int = 0         # where to start, so the cast can be walked in batches
    turns: int = 0          # 0 = the file's default
    dry_run: bool = False   # price it and spend nothing


@app.post("/api/admin/lesson-audit")
def admin_lesson_audit(body: LessonAuditIn):
    """Run the OFFLINE LESSON AUDITOR and return its report.

    2026-08-10 (build cw). Jim: "I need to build some sort of effectiveness/reality check
    so we don't keep having these problems."

    Two things check quality today and there is a gap between them: ruletests.py checks
    the CODE and the WORDS OF THE PROMPT and cannot judge teaching, and Jim reads lessons
    one at a time, which does not scale past Jim. This closes that gap: scripted student
    PERSONAS (played by OpenAI) take real lessons from the real prompt, and OpenAI then
    marks each transcript against the generated rule index as a picky maths teacher.

    NOTHING HERE CHANGES THE TEACHING. It returns a report a human reads. A critic can be
    wrong, and a wrong critic quietly sanding down good teaching is exactly the failure
    this is meant to prevent. A real finding becomes a rule AND a test, in one commit.

    It lives behind the admin key because it spends real money on two APIs, and it runs
    HERE rather than on a laptop because this is where the keys are. `dry_run` prices it
    for free. `limit`/`offset` walk the cast in batches so a request never runs long
    enough to time out -- two scenarios a call is comfortable.

    Needs OPENAI_API_KEY in the environment (Render -> Environment). The key is read,
    never printed, never returned, never logged."""
    _require_admin(body.key)
    try:
        import lessonaudit
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=503,
                            detail=f"lessonaudit.py is not available on this deploy: {exc}")
    turns = int(body.turns) or lessonaudit.TURNS
    limit = max(0, int(body.limit)) or None
    if body.dry_run:
        return lessonaudit.dry_run(limit, int(body.offset), turns)
    if not os.environ.get("OPENAI_API_KEY", "").strip():
        raise HTTPException(status_code=503,
                            detail=("No OPENAI_API_KEY on this service. Add it in Render -> "
                                    "Environment and redeploy; it is used only here, only "
                                    "when you call this endpoint."))
    run = lessonaudit.audit(limit, int(body.offset), turns)
    run["report_markdown"] = lessonaudit.report_markdown(run)
    run["next_offset"] = int(body.offset) + run.get("scenarios_run", 0)
    run["remaining"] = max(0, len(lessonaudit.SCENARIOS) - run["next_offset"])
    return run


@app.post("/api/admin/prewarm-foundations")
def admin_prewarm_foundations(body: PrewarmAdminIn):
    """Render every canonical foundation script into the TTS cache, up front.

    2026-08-09 (build cf, proactive audit #2 item 21). The TTS cache is keyed by the
    TEXT of a line and starts empty, so the FIRST student to reach each of the 173
    scripts pays a live ElevenLabs render -- several seconds of silence on the exact
    turn that introduces a brand-new idea to them. Every student after that gets it
    instantly. We know all 173 strings in advance, so there is no reason for that first
    student to be a real child.

    Idempotent and safe to re-run: a script already in the cache is skipped for free, so
    running this after adding scripts renders only the new ones. `dry_run` prices the
    job without spending a cent. `limit` renders in batches if you would rather not do
    it in one request.

    Admin-key protected -- this endpoint spends real ElevenLabs money."""
    _require_admin(body.key)
    if foundations is None:
        raise HTTPException(status_code=503, detail="foundations.py is not available on this deploy.")
    courses = ([body.course.strip()] if body.course.strip()
               else list(getattr(foundations, "FOUNDATIONS", {}).keys()))
    todo = []
    already = 0
    for c in courses:
        for f in foundations.for_course(c):
            say = (f.get("say") or "").strip()
            if not say:
                continue
            try:
                if _tts_cache_path(say).exists() and _tts_cache_path(say).stat().st_size > 0:
                    already += 1
                    continue
            except Exception:  # noqa: BLE001 -- an unreadable cache entry just gets re-rendered
                pass
            todo.append((c, f["term"], say))
    chars = sum(len(s) for _c, _t, s in todo)
    if body.dry_run or not todo:
        return {"ok": True, "dry_run": True, "courses": courses, "already_cached": already,
                "to_render": len(todo), "characters": chars,
                "note": "Nothing was spent. POST again with dry_run=false to render."}
    if not ELEVEN_API_KEY:
        raise HTTPException(status_code=503, detail="ELEVENLABS_API_KEY is not set on this deploy.")
    if body.limit and body.limit > 0:
        todo = todo[:body.limit]

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVEN_VOICE_ID}"
    headers = {"xi-api-key": ELEVEN_API_KEY, "Content-Type": "application/json"}
    rendered, failed, spent = 0, [], 0
    for course, term, say in todo:
        try:
            r = httpx.post(url, headers=headers, timeout=60.0, json={
                "text": say,
                "model_id": ELEVEN_MODEL,
                "output_format": "mp3_44100_128",
                "voice_settings": {"stability": 0.55, "similarity_boost": 0.75,
                                   "use_speaker_boost": True},
            })
            if r.status_code != 200 or not r.content:
                failed.append(f"{course}/{term}: HTTP {r.status_code}")
                continue
            # Same atomic write as the streaming path: a partial file must never be
            # left behind, because a truncated clip would then be served forever.
            path = _tts_cache_path(say)
            _TTS_CACHE_DIR.mkdir(parents=True, exist_ok=True)
            tmp = path.with_suffix(".part")
            tmp.write_bytes(r.content)
            tmp.replace(path)
            rendered += 1
            spent += len(say)
            store.log_usage(kind="tts", code="", mode="prewarm", model=str(ELEVEN_MODEL or ""),
                            tts_chars=len(say), tts_cache_hit=False)
        except Exception as exc:  # noqa: BLE001 -- one bad script must not stop the batch
            failed.append(f"{course}/{term}: {exc}")
    try:
        _evict_tts_cache()
    except Exception as exc:  # noqa: BLE001
        print(f"[prewarm] evict skipped: {exc}")
    print(f"[prewarm] rendered {rendered}, failed {len(failed)}, {spent} characters")
    return {"ok": not failed, "already_cached": already, "rendered": rendered,
            "characters_spent": spent, "failed": failed[:20], "failed_count": len(failed),
            "remaining": max(0, len(todo) - rendered)}


class StudentResetAdminIn(BaseModel):
    key: str
    code: str


@app.post("/api/admin/student-reset")
def admin_student_reset(body: StudentResetAdminIn):
    """2026-08-07 (build bc, Jim): wipe ONE student code's data -- pilot personas
    (0000/1234/...), demo codes, any student -- so the code can be used as brand new.
    The code keeps working (pilot codes live in students.json; the account row is
    re-created on next login). Admin-key protected; 404 for a code that isn't a known
    student, so a typo can never silently 'succeed'."""
    _require_db()
    _require_admin(body.key)
    code = (body.code or "").strip()
    if not _lookup_student(code):
        raise HTTPException(status_code=404, detail=(
            "That code isn't a known student, so nothing was wiped. (Beta passes are "
            "deleted from the pass table instead.)"))
    res = store.reset_student_data(code)
    if not res.get("ok"):
        raise HTTPException(status_code=500, detail="Couldn't complete the wipe — nothing was deleted.")
    removed = sum(int(v or 0) for v in (res.get("deleted") or {}).values())
    return {"ok": True, "code": code, "rows_removed": removed, "deleted": res.get("deleted") or {}}


@app.post("/api/admin/parent-reset")
def admin_parent_reset(body: ParentResetAdminIn):
    """Fully delete ONE parent account (and its children + data) by email, so the
    email is free to sign up from scratch. Admin-key protected. Returns a summary
    of what was removed. 404 (harmless) if no account exists for that email."""
    _require_db()
    _require_admin(body.key)
    email = (body.email or "").strip().lower()
    if not _EMAIL_RE.match(email):
        raise HTTPException(status_code=400, detail="That doesn't look like an email address.")
    parent = store.get_parent_by_email(email)
    if not parent:
        raise HTTPException(status_code=404, detail=(
            f"No account found for {email}, so there's nothing to reset — that email "
            "is already free to sign up fresh."))
    result = store.delete_parent_cascade(parent["id"])
    if not result.get("ok"):
        raise HTTPException(status_code=500, detail=(
            "Couldn't complete the reset — nothing was deleted. Please try again."))
    return {
        "ok": True,
        "email": email,
        "children_removed": len(result.get("student_codes") or []),
        "deleted": result.get("deleted") or {},
    }


# =============================================================================
# BILLING -- Stripe Checkout + Customer Portal + webhook (2026-07-31)
# -----------------------------------------------------------------------------
# Cards never touch this server. "Subscribe" sends the parent to a Stripe-hosted
# Checkout page; "Manage billing" sends them to Stripe's hosted portal (update
# card, switch plan, cancel). Stripe then tells US what happened on the webhook
# below -- and THAT (signature-verified) is the only thing that ever changes a
# parent's subscription status in the database. Prices are found (or created,
# once) in Stripe by lookup key, so Jim never has to click around the Stripe
# dashboard to set up products:
#   mytutor_monthly  $29 / student / month
#   mytutor_annual   $288 / student / year   ($24/mo, as the pricing page says)
# Env (set in Render): STRIPE_SECRET_KEY, STRIPE_WEBHOOK_SECRET. Optional:
# SITE_URL (defaults to https://mrcadabra.com).
# =============================================================================

_PLAN_LOOKUP = {"monthly": "mytutor_monthly", "annual": "mytutor_annual"}
_PLAN_AMOUNTS = {"monthly": 2900, "annual": 28800}     # cents
_PRICE_ID_CACHE: dict = {}
SITE_URL = (os.environ.get("SITE_URL", "").strip() or "https://mrcadabra.com").rstrip("/")

# 2026-07-31: Stripe accounts now enable "Managed Payments" by default, which
# REQUIRES products to carry a tax code (it's how Stripe computes sales tax for
# you). This is Stripe's tax classification for a digital service delivered
# online ("General - Electronically Supplied Services"). If an accountant later
# advises a more specific education classification, change it here (or set the
# STRIPE_TAX_CODE env var) -- existing products are updated automatically.
PRODUCT_TAX_CODE = (os.environ.get("STRIPE_TAX_CODE", "").strip() or "txcd_10000000")
_TAX_CODE_OK: set = set()      # product ids already verified/updated this process


class CheckoutIn(BaseModel):
    token: str
    plan: str = "monthly"      # 'monthly' | 'annual'


def _payments_open() -> bool:
    """Are we ACCEPTING payments? (2026-08-01, Jim: 'we're in beta — not taking
    payment at this time.') Self-managing: payments open automatically when the
    configured Stripe key is a LIVE key (sk_live_...). With a test key or no key,
    the site shows an honest beta notice instead of subscribe buttons, and the
    billing endpoints refuse politely. Env override PAYMENTS_OPEN=open|closed
    forces either state (e.g. 'open' to demo the test-mode checkout on purpose)."""
    override = os.environ.get("PAYMENTS_OPEN", "").strip().lower()
    if override in ("1", "true", "yes", "open"):
        return True
    if override in ("0", "false", "no", "closed"):
        return False
    return os.environ.get("STRIPE_SECRET_KEY", "").strip().startswith("sk_live_")


def _require_payments_open() -> None:
    if not _payments_open():
        raise HTTPException(status_code=503, detail=(
            "We're in our beta period and not taking payments yet. Full access is "
            "currently by beta pass — see mrcadabra.com/beta — or email "
            "support@mrcadabra.com."))


def _stripe():
    """The configured Stripe client module, or a clear 503 when payments are off."""
    key = os.environ.get("STRIPE_SECRET_KEY", "").strip()
    if not key:
        raise HTTPException(status_code=503, detail=(
            "Payments aren't switched on yet — email support@mrcadabra.com."))
    import stripe
    stripe.api_key = key
    return stripe


def _ensure_product_tax_code(stripe, product_id: str) -> None:
    """Make sure the product carries a tax code (required by Stripe's Managed
    Payments, on by default for new accounts). Heals products created before
    this fix existed; checked at most once per product per process."""
    if not product_id or product_id in _TAX_CODE_OK:
        return
    try:
        product = stripe.Product.retrieve(product_id)
        if not getattr(product, "tax_code", None):
            stripe.Product.modify(product_id, tax_code=PRODUCT_TAX_CODE)
            print(f"[billing] set tax_code {PRODUCT_TAX_CODE} on product {product_id}")
        _TAX_CODE_OK.add(product_id)
    except Exception as exc:  # noqa: BLE001 -- let checkout surface the real error
        print(f"[billing] tax-code check failed for {product_id}: {exc}")


def _price_id(stripe, plan: str) -> str:
    """Find (or create, exactly once) the Stripe Price for a plan, by lookup key."""
    lookup = _PLAN_LOOKUP[plan]
    if lookup in _PRICE_ID_CACHE:
        return _PRICE_ID_CACHE[lookup]
    found = stripe.Price.list(lookup_keys=[lookup], active=True, limit=1)
    if found.data:
        # Heal a product made before the tax-code fix (Managed Payments needs it).
        _ensure_product_tax_code(stripe, getattr(found.data[0], "product", None))
        _PRICE_ID_CACHE[lookup] = found.data[0].id
        return found.data[0].id
    # First ever run against this Stripe account: create the product + price.
    product_id = None
    # 2026-08-03 REBRAND: match the old "MyTutor" product too, so an account that already
    # has it reuses (and renames) it instead of creating a duplicate.
    for p in stripe.Product.list(active=True, limit=100).auto_paging_iter():
        if p.name in ("Mr. Cadabra's Classroom — Full access", "MyTutor Full access"):
            product_id = p.id
            if p.name != "Mr. Cadabra's Classroom — Full access":
                try:
                    stripe.Product.modify(product_id, name="Mr. Cadabra's Classroom — Full access")
                except Exception as exc:  # noqa: BLE001 -- a rename must never block checkout
                    print(f"[billing] product rename skipped: {exc}")
            break
    if not product_id:
        product_id = stripe.Product.create(
            name="Mr. Cadabra's Classroom — Full access",
            tax_code=PRODUCT_TAX_CODE,     # required by Managed Payments (default-on)
            description="All ten math courses with Mr. Cadabra — placement to mastery, "
                        "real spoken conversation, honest dashboards.").id
    else:
        _ensure_product_tax_code(stripe, product_id)
    _TAX_CODE_OK.add(product_id)
    price = stripe.Price.create(
        product=product_id, currency="usd", unit_amount=_PLAN_AMOUNTS[plan],
        recurring={"interval": ("month" if plan == "monthly" else "year")},
        lookup_key=lookup, transfer_lookup_key=True)
    _PRICE_ID_CACHE[lookup] = price.id
    return price.id


def _stripe_customer_id(stripe, parent: dict) -> str:
    """This parent's Stripe customer, created on first need and remembered."""
    if parent.get("stripe_customer_id"):
        return parent["stripe_customer_id"]
    customer = stripe.Customer.create(
        email=parent.get("email"), name=parent.get("name") or None,
        metadata={"parent_id": parent["id"]})
    store.update_parent(parent["id"], stripe_customer_id=customer.id)
    return customer.id


@app.post("/api/billing/checkout")
def billing_checkout(body: CheckoutIn):
    """Start a Stripe Checkout for this parent: quantity = their number of students."""
    _require_payments_open()
    parent = _require_parent(body.token)
    plan = (body.plan or "monthly").strip().lower()
    if plan not in _PLAN_LOOKUP:
        raise HTTPException(status_code=400, detail="Plan must be 'monthly' or 'annual'.")
    students = store.list_students_for_parent(parent["id"])
    if not students:
        raise HTTPException(status_code=400, detail=(
            "Add your child first — the subscription covers each student you add."))
    stripe = _stripe()
    try:
        session = stripe.checkout.Session.create(
            mode="subscription",
            customer=_stripe_customer_id(stripe, parent),
            line_items=[{"price": _price_id(stripe, plan),
                         "quantity": _seats_for(len(students))}],
            allow_promotion_codes=True,
            client_reference_id=parent["id"],
            subscription_data={"metadata": {"parent_id": parent["id"]}},
            success_url=SITE_URL + "/family?checkout=success",
            cancel_url=SITE_URL + "/family?checkout=canceled",
        )
    except Exception as exc:  # noqa: BLE001
        print(f"[billing] checkout failed for {parent['id']}: {exc}")
        raise HTTPException(status_code=502, detail=(
            "Stripe couldn't start the checkout — please try again in a minute."))
    return {"ok": True, "url": session.url}


@app.post("/api/billing/portal")
def billing_portal(body: ParentTokenIn):
    """Send the parent to Stripe's hosted portal: update card, switch plan, cancel."""
    _require_payments_open()
    parent = _require_parent(body.token)
    if not parent.get("stripe_customer_id"):
        raise HTTPException(status_code=400, detail="No billing set up yet — subscribe first.")
    stripe = _stripe()
    try:
        session = stripe.billing_portal.Session.create(
            customer=parent["stripe_customer_id"],
            return_url=SITE_URL + "/family")
    except Exception as exc:  # noqa: BLE001
        print(f"[billing] portal failed for {parent['id']}: {exc}")
        raise HTTPException(status_code=502, detail=(
            "Stripe couldn't open the billing page — please try again in a minute."))
    return {"ok": True, "url": session.url}


@app.post("/api/billing/cover")
def billing_cover(body: ParentTokenIn):
    """Parent added a child while subscribed: bump the subscription quantity to
    cover every student (Stripe prorates the difference automatically)."""
    _require_payments_open()
    parent = _require_parent(body.token)
    if (parent.get("sub_status") or "") != "active" or not parent.get("stripe_customer_id"):
        raise HTTPException(status_code=400, detail="No active subscription to update.")
    students = store.list_students_for_parent(parent["id"])
    stripe = _stripe()
    try:
        subs = stripe.Subscription.list(customer=parent["stripe_customer_id"],
                                        status="active", limit=1)
        if not subs.data:
            raise HTTPException(status_code=400, detail="No active subscription found in Stripe.")
        sub = subs.data[0]
        item = sub["items"]["data"][0]
        stripe.Subscription.modify(
            sub.id,
            items=[{"id": item.id, "quantity": _seats_for(len(students))}],
            proration_behavior="create_prorations")
    except HTTPException:
        raise
    except Exception as exc:  # noqa: BLE001
        print(f"[billing] cover failed for {parent['id']}: {exc}")
        raise HTTPException(status_code=502, detail=(
            "Stripe couldn't update the plan — please try again in a minute."))
    # The webhook will confirm, but reflect the new seat count right away too.
    store.update_parent(parent["id"], sub_quantity=_seats_for(len(students)))
    return _parent_payload(store.get_parent(parent["id"]))


def _apply_subscription(sub: dict) -> None:
    """Fold a Stripe subscription object into the parent's row. Called ONLY from
    the signature-verified webhook. Maps Stripe's status vocabulary to ours."""
    customer_id = sub.get("customer") or ""
    parent = store.get_parent_by_customer(customer_id)
    if not parent:
        pid = ((sub.get("metadata") or {}).get("parent_id") or "").strip()
        parent = store.get_parent(pid) if pid else None
        if parent and customer_id:
            store.update_parent(parent["id"], stripe_customer_id=customer_id)
    if not parent:
        print(f"[billing] webhook: no parent for customer {customer_id}")
        return
    s = sub.get("status") or ""
    status = ("active" if s in ("active", "trialing")
              else "past_due" if s in ("past_due",)
              else "canceled" if s in ("canceled", "unpaid", "incomplete_expired")
              else parent.get("sub_status") or "free")   # 'incomplete' etc: no change
    items = ((sub.get("items") or {}).get("data") or [{}])
    quantity = int(items[0].get("quantity") or 0)
    lookup = ((items[0].get("price") or {}).get("lookup_key") or "")
    plan = ("annual" if "annual" in lookup
            else "monthly" if "monthly" in lookup
            else parent.get("sub_plan") or "")
    period_end = None
    ts = sub.get("current_period_end") or items[0].get("current_period_end")
    if ts:
        import datetime as _dt3
        period_end = _dt3.datetime.fromtimestamp(int(ts), tz=_dt3.timezone.utc)
    if status == "canceled":
        quantity = 0
    store.update_parent(parent["id"], sub_status=status, sub_plan=plan,
                        sub_quantity=quantity, sub_period_end=period_end)
    print(f"[billing] {parent['email']}: {status} x{quantity} ({plan})")


@app.post("/api/stripe/webhook")
async def stripe_webhook(request: Request):
    """Stripe's messenger. Signature-verified with STRIPE_WEBHOOK_SECRET -- an
    unsigned or tampered call changes nothing and gets a 400."""
    _require_db()
    secret = os.environ.get("STRIPE_WEBHOOK_SECRET", "").strip()
    if not secret:
        raise HTTPException(status_code=503, detail="Webhook not configured.")
    import stripe
    payload = await request.body()
    sig = request.headers.get("stripe-signature", "")
    try:
        stripe.Webhook.construct_event(payload, sig, secret)   # signature check
    except Exception:  # bad signature or malformed payload
        raise HTTPException(status_code=400, detail="Invalid signature.")
    # Signature verified -- now read the payload as PLAIN dicts (the Stripe SDK's
    # wrapper objects change shape between versions; raw JSON does not).
    try:
        event = json.loads(payload)
    except (json.JSONDecodeError, UnicodeDecodeError):
        raise HTTPException(status_code=400, detail="Invalid payload.")
    etype = event.get("type") or ""
    obj = (event.get("data") or {}).get("object") or {}
    if etype == "checkout.session.completed":
        # Remember which Stripe customer this parent became; the subscription
        # events (below) carry the actual status/quantity.
        pid = (obj.get("client_reference_id") or "").strip()
        cust = obj.get("customer") or ""
        if pid and cust:
            parent = store.get_parent(pid)
            if parent and not parent.get("stripe_customer_id"):
                store.update_parent(pid, stripe_customer_id=cust)
    elif etype in ("customer.subscription.created", "customer.subscription.updated",
                   "customer.subscription.deleted"):
        _apply_subscription(obj)
    return {"received": True}


# =============================================================================
# COMMUNITY FORUM (2026-07-31) -- parents post, everyone reads
# -----------------------------------------------------------------------------
# Four sections: what's working / ideas for improvement / resources for parents /
# course requests. Reading is public. WRITING requires a signed-in parent (the
# accounts built today) -- students never post, and no email or child data ever
# appears: authors show as the parent's first name only, or "A MyTutor parent".
# Moderation: FORUM_MOD_KEY env var + POST /api/forum/moderate soft-deletes
# (hides, never destroys). Writes are rate-limited per parent AND per IP.
# =============================================================================

FORUM_SECTION_TITLES = {
    "working": "What's working for your family",
    "ideas": "Ideas for improvement",
    "resources": "Resources for parents",
    "courses": "Courses you'd like to see",
}


class ForumPostIn(BaseModel):
    token: str
    section: str
    title: str
    body: str = ""


class ForumReplyIn(BaseModel):
    token: str
    post_id: str
    body: str


class ForumModIn(BaseModel):
    key: str = ""              # LEGACY transport (build dn): the page now sends the key
                               # in the X-Admin-Key header; the body field stays accepted
                               # so an old cached page keeps working across the deploy.
    kind: str                  # 'post' | 'reply'
    item_id: str


def _forum_author(parent: dict) -> str:
    first = (parent.get("name") or "").strip().split(" ")[0]
    return first if first else "A parent"


@app.get("/api/forum/{section}")
def forum_list(section: str):
    """Public: the posts in one section, newest first."""
    _require_db()
    if section not in store.FORUM_SECTIONS:
        raise HTTPException(status_code=404, detail="No such section.")
    return {"ok": True, "section": section,
            "title": FORUM_SECTION_TITLES[section],
            "posts": store.list_forum_posts(section)}


@app.get("/api/forum/post/{post_id}")
def forum_post_detail(post_id: str):
    """Public: one post with its replies."""
    _require_db()
    post = store.get_forum_post((post_id or "").strip())
    if not post:
        raise HTTPException(status_code=404, detail="That post isn't here anymore.")
    return {"ok": True, "post": post}


@app.post("/api/forum/post")
def forum_create_post(body: ForumPostIn, request: Request):
    parent = _require_parent(body.token)
    _rate_limit("forum:" + parent["id"], limit=6, window_seconds=600, what="posts")
    _rate_limit("forumip:" + _client_ip(request), limit=12, window_seconds=600, what="posts")
    section = (body.section or "").strip().lower()
    if section not in store.FORUM_SECTIONS:
        raise HTTPException(status_code=400, detail="Please pick a section.")
    title = (body.title or "").strip()[:140]
    text = (body.body or "").strip()[:4000]
    if len(title) < 4:
        raise HTTPException(status_code=400, detail="Please give your post a short title.")
    store.create_forum_post(uuid.uuid4().hex, section, title, text,
                            parent["id"], _forum_author(parent))
    return {"ok": True, "posts": store.list_forum_posts(section)}


@app.post("/api/forum/reply")
def forum_create_reply(body: ForumReplyIn, request: Request):
    parent = _require_parent(body.token)
    _rate_limit("forum:" + parent["id"], limit=6, window_seconds=600, what="posts")
    _rate_limit("forumip:" + _client_ip(request), limit=12, window_seconds=600, what="posts")
    text = (body.body or "").strip()[:4000]
    if len(text) < 2:
        raise HTTPException(status_code=400, detail="Please write a reply first.")
    if not store.create_forum_reply(uuid.uuid4().hex, (body.post_id or "").strip(),
                                    text, parent["id"], _forum_author(parent)):
        raise HTTPException(status_code=404, detail="That post isn't here anymore.")
    return {"ok": True, "post": store.get_forum_post((body.post_id or "").strip())}


@app.post("/api/forum/moderate")
def forum_moderate(body: ForumModIn,
                   x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    """Jim's moderation: soft-delete a post or reply. Needs FORUM_MOD_KEY (env).
    BUILD dn: key accepted in the X-Admin-Key header (preferred -- the old
    /community?mod= link put it in a URL, and query strings land in Render's logs
    in plaintext); the body key stays accepted for a cached pre-dn page only.
    Same _require_admin constant-time gate as every other admin call."""
    _require_db()
    _require_admin(x_admin_key or body.key)
    if body.kind not in ("post", "reply"):
        raise HTTPException(status_code=400, detail="kind must be 'post' or 'reply'.")
    if not store.delete_forum_item(body.kind, (body.item_id or "").strip()):
        raise HTTPException(status_code=404, detail="Nothing with that id.")
    return {"ok": True}


@app.get("/api/courses/{code}")
def student_courses(code: str, request: Request):
    """EVERY course this student has actually worked in, with units mastered/started -- for the
    dashboard's "My courses" strip. Returns courses with REAL activity only, in ladder order, so
    a student sees their whole picture at a glance and can switch with one click. When tracking is
    off it reports that rather than inventing anything."""
    _read_guard(request, code)            # F1: throttle read-by-code enumeration
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


# =============================================================================
# LOOK-IT-UP LIBRARY (2026-08-07, Jim) -- the searchable reference database
# -----------------------------------------------------------------------------
# A stuck student clicks 📖 Look it up, types a topic ("binomial theorem", "adding
# dollars and cents"), and gets a READABLE article in a bubble -- the tutor's voice
# and the chat turn are never involved. Resolution order (see library.py):
#   curated seed -> saved article (exact key) -> fuzzy match across both -> the
#   GENERATE-ONCE fallback (one model call, saved forever, ~2 cents).
# Reading level follows the course's band, so the same search reads gently in
# Basic Math and tersely in Algebra II.
# =============================================================================
@app.get("/api/library")
def library_lookup(q: str = "", course: str = "algebra1", code: str = ""):
    """Serve one reference article for a student's search. Students only; the
    generation path is rate-limited separately (it spends model money)."""
    _student_or_404(code)
    code = code.strip()
    q = (q or "").strip()[:160]
    if len(q) < 2:
        raise HTTPException(status_code=400, detail="Type a topic to look up first.")
    _rate_limit("lib:" + code, limit=30, window_seconds=300, what="lookups")
    band = library.band_for(course if course in curriculum.COURSES else "algebra1")
    key = library.norm_key(q)

    # 1) Curated seed, exact alias.
    seed = library.find_seed(q, band)
    if seed:
        return {"title": seed["title"], "body": library.scrub_html(seed["body"]),
                "source": "library"}
    # 2) Saved article, exact key.
    if store.enabled():
        hit = store.get_library_article(key, band)
        if hit:
            store.bump_library_hits(key, band)
            return {"title": hit["title"], "body": hit["body"], "source": "library"}
    # 3) Fuzzy match across seeds (this band's neighborhood) + saved titles.
    candidates = [s for s in library.SEEDS if library.find_seed(s["title"], band)]
    if store.enabled():
        try:
            candidates = candidates + store.list_library_titles(band)
        except Exception as exc:  # noqa: BLE001
            print(f"[library] title list failed: {exc}")
    pick = library.fuzzy_pick(q, candidates)
    if pick:
        if "body" in pick:      # a seed
            return {"title": pick["title"], "body": library.scrub_html(pick["body"]),
                    "source": "library"}
        hit = store.get_library_article(pick["key"], band) if store.enabled() else {}
        if hit:
            store.bump_library_hits(pick["key"], band)
            return {"title": hit["title"], "body": hit["body"], "source": "library"}
    # 4) Generate once, save forever. Tighter limit -- this path costs money.
    _rate_limit("libgen:" + code, limit=6, window_seconds=300, what="new lookups")
    art = library.generate_article(q, band)
    if not art:
        return {"title": "", "body": "", "source": "none",
                "detail": "I couldn't find that in the library — try different words, "
                          "or ask Mr. Cadabra about it in the lesson."}
    if store.enabled():
        try:
            store.save_library_article(key, band, art["title"], art["body"])
        except Exception as exc:  # noqa: BLE001
            print(f"[library] save failed: {exc}")
    return {"title": art["title"], "body": art["body"], "source": "new"}


# =============================================================================
# FINAL EXAM (2026-08-07, Jim) -- a real course final, HARD-GATED on mastery
# -----------------------------------------------------------------------------
# The rule, in Jim's words: "to take the final exam, they have to have mastered
# everything else in the course ahead of time" -- and the optional 'Prepare for the
# Final Exam' overview is gated exactly the same way. The gate is enforced HERE, on
# the server, on every chat turn and every score post; the page's button state is
# only a courtesy. Mastered = best Unit Quiz >= store.PASS_PCT (90) on all 9 units.
# =============================================================================
FINAL_GATE_MESSAGE = (
    "The Final Exam preparation and the Final Exam are only available to students who "
    "have mastered all the previous units of the course. You've mastered {n} of 9 so far "
    "-- every unit you master gets you one step closer. Keep going; I'll be right here "
    "when you're ready!")


def _final_gate_message(code: str, course: str, state: dict) -> str:
    """The locked-door message, with the door's key attached.

    2026-08-10 (build cu, Jim): "I can do all the units and still be carrying an
    eighty-five with me, which is gonna keep me from mastering the final exam. There needs
    to be some type of option to review and retake that quiz."
    The old message said "you've mastered 3 of 9" and stopped there -- true, useless, and
    arriving months after the unit it is about. A student standing at a locked door needs
    to know WHICH units are holding it shut, how close each one is, and that a retake can
    only ever help them. Units already ATTEMPTED come first and carry their best score,
    because those are the ones a single good session can finish. Falls back to the old
    wording if the record cannot be read -- a locked door must never also be a silent one.
    """
    try:
        names = {}
        for i, u in enumerate(curriculum.units_for(course)):
            if isinstance(u, (list, tuple)) and len(u) >= 2:
                names[int(u[0])] = str(u[1])
            else:
                names[i + 1] = str(u)
        checks = (store.get_mastery(code, course) or {}).get("checks", {}) if store.enabled() else {}
        close, untouched = [], []
        for unit in sorted(names):
            if unit in set(state.get("mastered_units") or []):
                continue
            c = checks.get(unit) or checks.get(str(unit)) or {}
            best = int(c.get("best_pct") or 0)
            if int(c.get("checks_taken") or 0) > 0:
                close.append(f"Unit {unit}, {names[unit]} (best Unit Quiz so far: {best}%)")
            else:
                untouched.append(f"Unit {unit}, {names[unit]}")
        if not close and not untouched:
            return FINAL_GATE_MESSAGE.format(n=state.get("mastered_count", 0))
        msg = ("The Final Exam unlocks when all nine units are mastered -- 90% or better on "
               f"each Unit Quiz. You've mastered {state.get('mastered_count', 0)} of 9.\n\n")
        if close:
            msg += ("These you've already taken a run at, so they're the quickest to finish:\n  - "
                    + "\n  - ".join(close)
                    + "\n\nAny of those we can review together and retake right now -- new questions, "
                      "and the record always keeps your BEST score, so a retake can only ever help "
                      "you. Just say which one.\n\n")
        if untouched:
            msg += "Still to come:\n  - " + "\n  - ".join(untouched) + "\n\n"
        return msg + "Tell me where you'd like to start and I'll get us going."
    except Exception as exc:  # noqa: BLE001
        print(f"[final] gate message fell back: {exc}")
        return FINAL_GATE_MESSAGE.format(n=state.get("mastered_count", 0))


def _final_exam_state(code: str, course: str) -> dict:
    """The student's final-exam picture for a course: which units are mastered, whether
    the exam is unlocked, and any recorded exam result. Honest when the DB is off."""
    mastered = []
    if store.enabled():
        try:
            checks = (store.get_mastery(code, course) or {}).get("checks", {})
            mastered = sorted(int(u) for u, c in checks.items()
                              if int((c or {}).get("best_pct") or 0) >= store.PASS_PCT)
        except Exception as exc:  # noqa: BLE001
            print(f"[final] mastery read failed: {exc}")
    exam = {}
    if store.enabled():
        try:
            exam = store.get_final_exam(code, course) or {}
        except Exception as exc:  # noqa: BLE001
            print(f"[final] exam read failed: {exc}")
    return {
        "mastered_units": mastered,
        "mastered_count": len(mastered),
        "required": 9,
        "eligible": len(mastered) >= 9,
        "exam": exam,
    }


@app.get("/api/sprints/{code}")
def api_sprint_record(code: str, request: Request, course: str = "prealgebra"):
    """The student's whole sprint history for one course, oldest first -- the
    dashboard's '⚡ Your sprint record' card (2026-08-11, build dm). WWC guide 26
    rec. 6 says track progress AND SHOW it; the data has recorded since build dd and
    nothing displayed it. Self-referential only (rule 42): this student's rounds,
    this student's best, nobody else's anything. Empty history -> the card never
    renders (sprints never gate and never nag)."""
    _read_guard(request, code)            # F1: throttle read-by-code enumeration
    _student_or_404(code)
    if not store.enabled():
        return {"ok": True, "history": [], "best_b": 0}
    try:
        rows = store.get_sprint_history(code.strip(), course, unit=None, limit=30)
    except Exception as exc:  # noqa: BLE001 -- the card is a bonus, never a 500
        print(f"[sprint] record read failed: {exc}")
        rows = []
    rows = list(reversed(rows))                      # oldest first, for a growth line
    return {"ok": True, "history": rows,
            "best_b": max([r["b"] for r in rows], default=0)}


@app.get("/api/sprint/{code}")
def get_sprint(code: str, request: Request, course: str = "prealgebra", unit: int = 1):
    """The day's fluency sprint for this student+course+unit, or {available:false}.

    2026-08-11 (build dd). WWC guide 26 recommendation 6 (STRONG): "regularly include
    timed activities... track and monitor progress". Format follows Eureka's Sprints
    (studied, not copied -- see sprints.py's licence note): two sibling halves, the
    celebrated number is B minus A, and the ONLY comparison is with this student's own
    history (rule 42).
    Seeded per student-per-day: a re-request today rebuilds the SAME sprint (a reload
    mid-sprint changes nothing); tomorrow's is fresh. ⚠️ NEVER GATES: nothing anywhere
    reads sprint results as a requirement, and declining is simply not calling this."""
    _read_guard(request, code)            # F1: throttle read-by-code enumeration
    _student_or_404(code)
    code = code.strip()
    if sprints is None or not sprints.available(course, unit):
        return {"available": False}
    import datetime as _dt
    day = _dt.date.today().isoformat()
    built = sprints.build(course, unit, f"{code}|{course}|{unit}|{day}")
    out = {"available": True, "skill": built["skill"], "unit": int(unit),
           "a": built["a"], "b": built["b"], "seconds": 60,
           "history": [], "best_b": 0, "done_today": False}
    if store.enabled():
        try:
            hist = store.get_sprint_history(code, course, unit, limit=8)
            out["history"] = hist
            out["best_b"] = max([h["b"] for h in hist], default=0)
            out["done_today"] = any(h["day"] == day for h in hist)
        except Exception as exc:  # noqa: BLE001
            print(f"[sprint] history read failed: {exc}")
    return out


@app.post("/api/sprint/{code}")
def post_sprint(code: str, body: SprintResultIn):
    """Record a finished sprint. Counts are re-clamped in store.record_sprint (correct
    <= attempted <= 30) so the dashboards this feeds stay honest. Returns the
    celebration facts: improvement, best_b, personal_best -- all self-referential."""
    _student_or_404(code)
    code = code.strip()
    if not store.enabled():
        return {"ok": False, "tracking": False}
    try:
        res = store.record_sprint(code, body.course, int(body.unit), body.skill,
                                  int(body.a_correct), int(body.a_attempted),
                                  int(body.b_correct), int(body.b_attempted))
        return {"ok": True, "tracking": True, **res}
    except Exception as exc:  # noqa: BLE001
        print(f"[sprint] record failed: {exc}")
        return {"ok": False, "tracking": True}


@app.post("/api/final/{code}")
def post_final(code: str, body: FinalIn):
    """Record a FINAL EXAM score ([[finalexam]] tag). Server-side gate: the score only
    records for an eligible student. Same contract style as /api/check."""
    _student_or_404(code)
    code = code.strip()
    if not store.enabled():
        return {"ok": False, "tracking": False}
    try:
        course = body.course if body.course in curriculum.COURSES else "algebra1"
        state = _final_exam_state(code, course)
        if not state["eligible"]:
            return {"ok": False, "tracking": True, "locked": True,
                    "detail": _final_gate_message(code, course, state)}
        res = store.record_final_exam(code, int(body.correct), int(body.total), course)
        _keep_misses(code, course, 0, 0, "final",
                     getattr(body, "missed", []), body.correct, body.total)
        return {"ok": True, "tracking": True, **res}
    except Exception as exc:  # noqa: BLE001
        print(f"[final] record_final_exam failed: {exc}")
        return {"ok": False, "tracking": True}


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
        _keep_misses(code, course, body.unit, 0, "check",
                     body.missed, body.correct, body.total)
        return {"ok": True, "tracking": True, **res}
    except Exception as exc:  # noqa: BLE001
        print(f"[check] record_check failed: {exc}")
        return {"ok": False, "tracking": True}


@app.get("/api/records/{code}")
def records_report(code: str, request: Request, days: int = 90):
    """Everything the printable homeschool records report needs (2026-08-04), in one
    call: the full-range hours log, per-course unit progress (statuses, topic quizzes,
    Unit Quiz best, mastered at 90%), placement titles, and dated awards. Read-only;
    honest {tracking:false} when the DB is off."""
    _read_guard(request, code)            # F1: throttle read-by-code enumeration
    student = _student_or_404(code)
    code = code.strip()
    days = max(7, min(730, int(days or 90)))
    if not store.enabled():
        return {"tracking": False, "name": student.get("name"), "days": days,
                "time": [], "courses": [], "awards": []}
    from datetime import datetime, timezone, timedelta
    today = datetime.now(timezone.utc).date()
    day_from = (today - timedelta(days=days - 1)).isoformat()

    time_rows = store.get_time_between(code, day_from, today.isoformat())
    for r in time_rows:
        r["course_title"] = curriculum.course_title(r["course"]) if r["course"] in curriculum.COURSES else r["course"]

    courses = []
    try:
        activity = store.get_course_activity(code)
    except Exception as exc:  # noqa: BLE001
        print(f"[records] get_course_activity failed: {exc}")
        activity = {}
    for cid in activity:
        if cid not in curriculum.COURSES:
            continue
        try:
            recorded = {r["unit"]: r for r in store.get_topics(code, cid)}
            checks = (store.get_mastery(code, cid) or {}).get("checks", {})
            quiz_rows = {}
            for q in store.get_topic_quizzes(code, cid):
                quiz_rows.setdefault(q["unit"], []).append({
                    "name": q["topic_name"], "best_pct": q["best_pct"],
                    "passed": q["best_pct"] >= store.QUIZ_PASS_PCT})
        except Exception as exc:  # noqa: BLE001
            print(f"[records] course {cid} read failed: {exc}")
            continue
        units = []
        for n, name in curriculum.units_for(cid):
            r = recorded.get(n)
            c = checks.get(n) or {}
            best = int(c.get("best_pct") or 0)
            units.append({"unit": n, "name": name,
                          "status": (r["status"] if r else "not-started"),
                          "best_pct": best, "checks_taken": int(c.get("checks_taken") or 0),
                          "mastered": best >= store.PASS_PCT,
                          "quizzes": quiz_rows.get(n, [])})
        placement = read_placement(code, cid) or {}
        courses.append({"course": cid, "title": curriculum.course_title(cid),
                        "placement": placement.get("level_title") or "",
                        "units": units,
                        "units_mastered": len([u for u in units if u["mastered"]])})
    courses.sort(key=lambda c: -c["units_mastered"])

    awards = []
    try:
        for aid, earned in store.get_awards(code).items():
            if aid in AWARD_DEFS:
                d = AWARD_DEFS[aid]
                awards.append({"icon": d[0], "title": d[1], "desc": d[2], "earned_at": earned})
        awards.sort(key=lambda a: a["earned_at"] or "")
    except Exception as exc:  # noqa: BLE001
        print(f"[records] awards read failed: {exc}")

    return {"tracking": True, "name": student.get("name"), "days": days,
            "time": time_rows, "courses": courses, "awards": awards}


@app.post("/api/quiz/{code}")
def post_quiz(code: str, body: QuizIn):
    """Record a mid-unit TOPIC QUIZ score (2026-08-04). Same contract style as
    /api/check: no-op (tracking:false) when the DB is off; never raises."""
    _student_or_404(code)
    code = code.strip()
    if not store.enabled():
        return {"ok": False, "tracking": False}
    try:
        course = body.course if body.course in curriculum.COURSES else "algebra1"
        res = store.record_topic_quiz(code, int(body.unit), (body.name or "").strip(),
                                      int(body.correct), int(body.total), course,
                                      topic_idx=int(body.topic or 0))
        _keep_misses(code, course, body.unit, body.topic, "quiz",
                     body.missed, body.correct, body.total)
        return {"ok": True, "tracking": True, **res}
    except Exception as exc:  # noqa: BLE001
        print(f"[quiz] record_topic_quiz failed: {exc}")
        return {"ok": False, "tracking": True}


@app.get("/api/misses/{code}")
def get_misses_api(code: str, request: Request, course: str = ""):
    """The student's recent missed problems (build dt) for the dashboard's review
    card: newest first, with unit names attached. Student-gated like every
    per-student read; honest {tracking:false} when the DB is off."""
    _read_guard(request, code)            # F1: throttle read-by-code enumeration
    _student_or_404(code)
    code = code.strip()
    if not store.enabled():
        return {"ok": False, "tracking": False, "misses": []}
    course = course if course in curriculum.COURSES else ""
    try:
        rows = store.get_misses(code, course or None, limit=30)
    except Exception as exc:  # noqa: BLE001
        print(f"[misses] read failed: {exc}")
        rows = []
    for r in rows:
        try:
            r["unit_name"] = (curriculum.unit_name(course or "algebra1", r["unit"])
                              if r.get("unit") else "")
        except Exception:  # noqa: BLE001
            r["unit_name"] = ""
    return {"ok": True, "tracking": True, "misses": rows}


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
def get_placement(code: str, request: Request, course: str = "algebra1"):
    """Return this student's saved placement result for a course (or {})."""
    _read_guard(request, code)            # F1: throttle read-by-code enumeration
    _student_or_404(code)
    return read_placement(code.strip(), course)


# Bump this string whenever the backend changes. It's shown at /health so we can CONFIRM
# Render actually redeployed the new code (if /health still shows an old build, the deploy
# didn't happen -- which would explain why prompt/whiteboard changes aren't taking effect).
APP_BUILD = "2026-08-12eg-parents-demo"


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
    code = req.code.strip()

    # FORGIVING BETA-CODE ENTRY (2026-08-07 build bd, Jim: generated a pass, typed it in,
    # "not recognized"). Passes look like TRY-TIGER42; real people type "tiger42",
    # "TRY TIGER42", or "try-tiger 42". If the code as typed isn't a known pass, retry a
    # few honest normalizations (squash spaces, add the TRY- prefix, fix a missing dash)
    # and use the first that IS one. Pilot 4-digit codes and parent-student codes are
    # looked up with the code exactly as typed, same as always.
    if store.enabled():
        compact = re.sub(r"\s+", "", code).upper()
        for candidate in (code, compact,
                          "TRY-" + compact if not compact.startswith("TRY") else compact,
                          "TRY-" + compact[3:].lstrip("-") if compact.startswith("TRY") else compact):
            if candidate and store.get_beta_code(candidate):
                code = candidate
                break

    # BETA PASS sign-in (2026-07-31): consumes one of its uses and opens a timed
    # window (unless a window is already open, which rides free). The response
    # carries the pass status so the login page can say "3 of 5 sign-ins left".
    if store.enabled() and store.get_beta_code(code):
        status = store.beta_login(code)
        if not status.get("ok"):
            raise HTTPException(status_code=403, detail=_beta_404_detail(code) or
                                "This beta pass can't be used right now.")
        bcode = store.get_beta_code(code)["code"]        # normalized (uppercase)
        session = get_session(bcode)
        placement = read_placement(bcode)
        return {
            "ok": True,
            "code": bcode,
            "name": store.get_beta_code(code).get("label") or "Beta tester",
            "returning": bool(session.get("history")),
            "placed": bool(placement),
            "tutor_name": tutor.TUTOR_NAME,
            "beta": True,
            "beta_uses_left": status.get("uses_left"),
            "beta_window_ends": (status["window_expires_at"].isoformat()
                                  if status.get("window_expires_at") else None),
        }

    student = _student_or_404(req.code)
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
def session_state(code: str, request: Request, course: str = "algebra1"):
    """
    Return the student's info, remembered conversation (for resume), and their
    placement -- ALL scoped to the given course. The hub/session page uses `placed`
    to enforce the flow (a never-placed student with no history is sent to the
    Challenge first) and `history` to decide between a first-time tour and a
    welcome-back recap.
    """
    _read_guard(request, code)            # F1: throttle read-by-code enumeration
    student = _student_or_404(code)
    code = code.strip()
    session = get_session(code, course)
    placement = read_placement(code, course)
    # PROGRESS PICTURE (2026-08-07): everything the lesson page's new bars + final-exam
    # button need, in the call the page already makes. Wrapped: a data hiccup never
    # blocks the lesson from loading.
    progress = {"mastered_units": [], "unit_quiz_best": {}, "topic_quizzes": {},
                "today": {},
                "final": {"eligible": False, "mastered_count": 0, "required": 9, "exam": {}}}
    if store.enabled():
        try:
            checks = (store.get_mastery(code, course) or {}).get("checks", {})
            for u, c in checks.items():
                best = int((c or {}).get("best_pct") or 0)
                progress["unit_quiz_best"][int(u)] = best
                if best >= store.PASS_PCT:
                    progress["mastered_units"].append(int(u))
            progress["mastered_units"].sort()
            for q in store.get_topic_quizzes(code, course):
                progress["topic_quizzes"].setdefault(q["unit"], []).append(
                    {"idx": q["topic_idx"], "name": q["topic_name"],
                     "passed": q["best_pct"] >= store.QUIZ_PASS_PCT})
            # build cg: today's goal bar, so a reload/resume shows all THREE bars.
            progress["today"] = store.get_today_goals(code, course) or {}
            fstate = _final_exam_state(code, course)
            progress["final"] = {"eligible": fstate["eligible"],
                                 "mastered_count": fstate["mastered_count"],
                                 "required": fstate["required"],
                                 "exam": fstate["exam"]}
        except Exception as exc:  # noqa: BLE001
            print(f"[session] progress read failed: {exc}")
    return {
        "name": student.get("name"),
        "tutor_name": tutor.TUTOR_NAME,
        "history": session.get("history", []),
        "placement": placement,
        "placed": bool(placement),
        "progress": progress,
        # 2026-08-01: the screen tour runs ONCE PER STUDENT... 2026-08-03 refinement (Jim's
        # playtest: an already-toured demo code got NO intro in Entry-Level Math): the tour is
        # now once per student PER CLASSROOM TYPE. The elementary classroom (entry/basic,
        # tap-to-answer) is a genuinely different experience from the typing classroom, so
        # history in one group no longer suppresses the other group's first-time tour.
        "toured": _has_any_history(code, _tour_group(course)),
    }


# The two classroom types for tour purposes: elementary (tap-to-answer) vs typing.
_ELEM_COURSES = ("entry", "basic")


def _tour_group(course: str):
    """The set of courses whose history counts as 'has seen this classroom's tour'."""
    if course in _ELEM_COURSES:
        return _ELEM_COURSES
    return tuple(c for c in curriculum.COURSE_ORDER if c not in _ELEM_COURSES)


def _has_any_history(code: str, courses=None) -> bool:
    """True if the student has lesson history (DB or JSON files). `courses` optionally
    limits the check to those course ids (see _tour_group); None = any course."""
    try:
        if store.enabled():
            return store.has_any_history(code, courses)
        allx = _read_all_sessions()
        for key, sess in allx.items():
            if not ((key == code or key.startswith(code + "|")) and (sess or {}).get("history")):
                continue
            if courses:
                # JSON keys are "CODE" (the default course) or "CODE|course".
                kcourse = key.split("|", 1)[1] if "|" in key else curriculum.DEFAULT_COURSE
                if kcourse not in courses:
                    continue
            return True
    except Exception as exc:  # noqa: BLE001 -- worst case: they see the tour again
        print(f"[tour] has_any_history failed for {code}: {exc}")
    return False


# =============================================================================
# NARRATIVE ASSESSMENT (2026-08-01) -- "How am I doing?" / the parent's honest read
# -----------------------------------------------------------------------------
# Gathers ONLY real recorded facts (units, checks, accuracy, streak, engaged
# minutes, awards, placement) and asks the tutor brain for one warm, honest
# paragraph. Cached in memory for 30 minutes per (student, course, audience) so
# repeat taps are free; rate-limited on top. The same engine will write the
# weekly parent/teacher emails when those ship.
# =============================================================================

_ASSESS_CACHE: dict = {}
_ASSESS_TTL_SECONDS = 1800


def _assessment_facts(code: str, student: dict, course: str) -> str:
    """Everything true we know about this student, as compact plain text."""
    title = curriculum.course_title(course)
    lines = [f"Student first name: {student.get('name') or 'Student'}",
             f"Course: {title}"]
    placement = read_placement(code, course)
    if placement:
        lines.append(f"Placement: tested as '{placement.get('level_title','')}' -- "
                     f"recommended start at unit {placement.get('start_unit')} "
                     f"({placement.get('start_unit_name','')})")
    else:
        lines.append("Placement: has not taken the course assessment yet")
    if store.enabled():
        m = store.get_mastery(code, course)
        checks = m.get("checks", {})
        # units_for() yields (unit_number, name) pairs; tolerate bare names too.
        unit_names = {}
        for i, u in enumerate(curriculum.units_for(course)):
            if isinstance(u, (list, tuple)) and len(u) >= 2:
                unit_names[int(u[0])] = str(u[1])
            else:
                unit_names[i + 1] = str(u)
        mastered, working, unchecked = [], [], []
        for u, name in unit_names.items():
            c = checks.get(u)
            if c and int(c.get("best_pct") or 0) >= store.PASS_PCT:
                mastered.append(f"{name} (best check {c['best_pct']}%)")
            elif c and int(c.get("checks_taken") or 0) > 0:
                working.append(f"{name} (best check so far {c['best_pct']}%, "
                               f"{c['checks_taken']} attempt(s))")
        lines.append("Units MASTERED (proved on a scored check): " +
                     ("; ".join(mastered) if mastered else "none yet"))
        lines.append("Units checked but not yet mastered: " +
                     ("; ".join(working) if working else "none"))
        st = m.get("stats", {})
        lines.append(f"Practice: {st.get('problems_practiced') or 0} problems practiced overall; "
                     f"accuracy across checks+practice: "
                     f"{str(st.get('accuracy_pct')) + '%' if st.get('accuracy_pct') is not None else 'no data yet'}; "
                     f"current day streak: {st.get('streak_days') or 0}; "
                     f"last active: {st.get('last_active') or 'no activity recorded'}")
        time_rows = store.get_time(code, days=14)
        total_min = sum(r["minutes"] for r in time_rows)
        days_active = sum(1 for r in time_rows if r["minutes"] > 0)
        lines.append(f"Engaged time, last 14 days: {total_min} real working minutes across "
                     f"{days_active} active day(s) (idle time is never counted)")
        earned = store.get_awards(code)
        names = [AWARD_DEFS[a][1] for a in earned if a in AWARD_DEFS]
        lines.append("Effort awards earned: " + (", ".join(names) if names else "none yet"))
        activity = store.get_course_activity(code)
        others = [curriculum.course_title(c) for c in activity if c != course]
        if others:
            lines.append("Also has activity in: " + ", ".join(others))
    else:
        lines.append("(Progress tracking is offline right now -- only basic info available.)")
    return "\n".join(lines)


@app.get("/api/assessment/{code}")
def assessment(code: str, request: Request, course: str = "algebra1",
               audience: str = "student"):
    """A warm, honest narrative assessment -- student voice or parent voice."""
    _read_guard(request, code)            # F1: throttle read-by-code enumeration
    student = _student_or_404(code)
    code = code.strip()
    audience = "parent" if audience == "parent" else "student"
    if course not in curriculum.COURSES:
        course = "algebra1"
    key = (code, course, audience)
    now = time.monotonic()
    hit = _ASSESS_CACHE.get(key)
    if hit and now - hit[0] < _ASSESS_TTL_SECONDS:
        return {"ok": True, "text": hit[1], "audience": audience, "cached": True}
    # Paid call: modest per-student cap on top of the cache.
    _rate_limit("assess:" + code, limit=8, window_seconds=3600, what="assessment requests")
    facts = _assessment_facts(code, student, course)
    text = tutor.get_assessment(facts, audience, code=code, course=course)
    if not text.startswith("("):                      # don't cache error placeholders
        if len(_ASSESS_CACHE) > 2000:
            _ASSESS_CACHE.clear()
        _ASSESS_CACHE[key] = (now, text)
    return {"ok": True, "text": text, "audience": audience, "cached": False}



# =============================================================================
# FIRST-USE KEY-TERM BOLDING -- deterministic (2026-08-01, from the live audit)
# -----------------------------------------------------------------------------
# The prompt asks the tutor to **bold** a term's first use, and it does so when
# formally DEFINING a term -- but the live audit showed it misses passing first
# mentions ("that's the derivative..."). Style rules deserve a guarantee, not a
# hope (same philosophy as the old board guarantee): the server wraps the first
# occurrence of a curated key term in ** ** itself, skipping [[tags]], skipping
# terms the tutor already used in an earlier turn, and never double-wrapping.
# The pages render **term** bold red; the voice never reads the asterisks.
# =============================================================================

KEY_TERMS = [
    "differential equation", "standard deviation", "line of best fit", "unit circle",
    "pythagorean theorem", "absolute value", "order of operations", "scientific notation",
    "distributive property", "greatest common factor", "least common multiple",
    "rational function", "integrating factor", "complementary", "supplementary",
    "perpendicular", "transversal", "hypotenuse", "congruent", "isosceles", "equilateral",
    "scalene", "circumference", "diameter", "bisect", "polynomial", "coefficient",
    "reciprocal", "numerator", "denominator", "inequality", "proportion", "y-intercept",
    "quadratic", "parabola", "vertex", "exponent", "logarithm", "asymptote", "amplitude",
    "radian", "sine", "cosine", "secant line", "tangent line", "derivative",
    "antiderivative", "integral", "chain rule", "product rule", "quotient rule",
    "separable", "permutation", "combination", "factorial", "probability", "median",
    "quartile", "variance", "histogram", "scatter plot", "box plot", "variable",
]
_TAG_SPLIT_RE = re.compile(r"(\[\[[^\]]*\]\])")


# ===== FOUNDATION MEMORY (2026-08-09, build ce) ==============================
# Jim: "if a student is returning, nothing tells him which scripts that student has
# heard, so a loyal student can re-hear it. We need to fix it... we should just query
# him and say, do you think you got it, or do you want me to refresh your memory?"
#
# Two halves, both here. READ: before the turn, load this student's heard terms out of
# the store and put them on the student record, where tutor.build_system_prompt picks
# them up. WRITE: after the turn, look for [[learned term="..."]] -- the invisible tag
# rule 40(f) asks him to emit whenever he actually delivers an introduction -- and
# record it. The tag parsing and the "is this a real script name?" filter both live in
# foundations.learned_terms_in(), so a mistyped tag can never retire an introduction the
# student still needs -- and ruletests.py can test that filter without booting the app.


# ===== THE TODAY BAR MUST SURVIVE A RELOAD (2026-08-09, build cg) ============
# Jim, on a resumed Pre-Algebra session: "there's only two of the three tracking bars
# across the top. I don't know where the third one is, and I don't know why it keeps
# disappearing."
#
# Why it kept disappearing: the UNIT and COURSE bars are rebuilt by the page at load
# from the server's mastery data (build br did that for the unit bar). The TODAY bar
# never had a server side at all -- it existed only as a [[today items]] tag the model
# emitted once, held in browser memory. Close the tab, resume tomorrow, refresh: gone,
# and it could only come back if the model happened to emit the tag again. The
# ensure_today_tag() net could not help either, because it deliberately stands down
# when an earlier [[today]] exists in history -- true within a session, wrong across a
# page load, where the bar it is protecting no longer exists.
# So we store what the tutor wrote. Same shape as the other two bars: the page renders
# it at load, and a later [[today]] simply replaces it.
_TODAY_TAG_RE = re.compile(r'\[\[\s*today\b[^\]]*?items\s*=\s*"([^"]{1,400})"[^\]]*\]\]', re.I)
_TODAYDONE_TAG_RE = re.compile(r'\[\[\s*todaydone\b[^\]]*?n\s*=\s*"?(\d{1,2})"?[^\]]*\]\]', re.I)


def _record_today_bar(code: str, course: str, reply: str) -> None:
    """Persist this reply's [[today items]] / [[todaydone n]] so the bar survives."""
    try:
        if not store.enabled() or not code or not reply:
            return
        m = _TODAY_TAG_RE.search(reply)
        items = [x.strip() for x in m.group(1).split("|") if x.strip()][:8] if m else []
        done = [int(n) for n in _TODAYDONE_TAG_RE.findall(reply)]
        if items or done:
            store.save_today_goals(code, course, items=items, done=done)
    except Exception as exc:  # noqa: BLE001 -- a bar is never worth failing a turn over
        print(f"[today] recording failed: {exc}")


def _foundations_heard(code: str, course: str) -> list:
    """The canonical terms this student has already been introduced to in this course."""
    try:
        if not store.enabled() or not code:
            return []
        return sorted(store.get_foundations_heard(code, course).keys())
    except Exception as exc:  # noqa: BLE001 -- never break a turn over a memory lookup
        print(f"[foundations] heard-list lookup failed: {exc}")
        return []


def _record_learned(code: str, course: str, reply: str) -> None:
    """Persist every [[learned term="..."]] the tutor emitted in this reply."""
    try:
        if foundations is None or not store.enabled() or not code or not reply:
            return
        for term in foundations.learned_terms_in(course, reply):
            store.record_foundation_heard(code, course, term)
    except Exception as exc:  # noqa: BLE001
        print(f"[foundations] recording failed: {exc}")


def _bold_first_terms(reply: str, history) -> str:
    """Wrap the FIRST use of each key term in **bold** (rendered red by the app).
    Skips [[tags]], terms already used in an earlier tutor turn, and anything the
    model already bolded. Wrapped so a failure can never break a lesson."""
    try:
        if not reply:
            return reply
        # Tag text ([[card ...]] etc.) is NOT spoken prose -- a term that has only
        # ever appeared inside a tag hasn't been "introduced" yet, and terms inside
        # tags are never wrapped. Strip tags before both checks.
        _strip = lambda t: _TAG_SPLIT_RE.sub(" ", str(t))
        prior = " ".join(_strip(m.get("content", "")) for m in (history or [])
                         if m.get("role") == "assistant").lower()
        parts = _TAG_SPLIT_RE.split(reply)
        low = _strip(reply).lower()
        for term in sorted(KEY_TERMS, key=len, reverse=True):
            tl = term.lower()
            if tl not in low or tl in prior or ("**" + tl) in low:
                continue
            pat = re.compile(r"(?<![*\w])(" + re.escape(term) + r"s?)(?![\w*])", re.IGNORECASE)
            for i, seg in enumerate(parts):
                if seg.startswith("[["):
                    continue
                mt = pat.search(seg)
                if mt:
                    parts[i] = seg[:mt.start()] + "**" + mt.group(1) + "**" + seg[mt.end():]
                    break
        return "".join(parts)
    except Exception as exc:  # noqa: BLE001 -- styling must never break a turn
        print(f"[terms] bolding skipped: {exc}")
        return reply


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

    # FREE PLAN GATE (2026-07-31): a free student who has mastered their first unit
    # gets a warm upgrade note instead of a lesson -- checked BEFORE the paid call.
    gate = _free_gate(code, student, req.course)
    if gate:
        return {"reply": gate, "upgrade_required": True}

    # FINAL EXAM MODES (2026-08-07): "prep" or "exam" -- HARD SERVER GATE, re-checked on
    # EVERY turn. An ineligible request gets the gate message with no paid model call;
    # the page's button state is only a courtesy, never the enforcement.
    final_mode = (req.final or "").strip().lower()
    if final_mode not in ("prep", "exam"):
        final_mode = ""
    if final_mode:
        fstate = _final_exam_state(code, req.course)
        if not fstate["eligible"]:
            return {"reply": _final_gate_message(code, req.course, fstate),
                    "final_locked": True}

    session = get_session(code, req.course)
    history = session.get("history", [])

    # Give the tutor the student's remembered progress plus the live history.
    student_context = dict(student)
    if final_mode:
        student_context["final_mode"] = final_mode   # tutor.py appends the matching note
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
    # 2026-08-11 (build ea): the PARENT'S STANDING PLAN. When the student opens this
    # course with no focus of their own, the steer set on /family supplies one. An
    # explicit dashboard link always wins -- the student's own intent outranks the plan.
    focus_unit, steered = _resolve_focus(code, req.course, focus_unit)
    mnote = _mastery_note(code, focus_unit, req.course, steered=steered)
    if mnote:
        student_context["mastery_note"] = mnote
    if 1 <= focus_unit <= 9:
        student_context["focus_unit"] = focus_unit

    # REWARDS AWARENESS (2026-07-30): if the student earned an award in the last 48h, tell the
    # tutor so he can congratulate them ONCE, by name, for what they DID. Wrapped: never breaks a turn.
    try:
        if store.enabled():
            from datetime import datetime, timezone, timedelta
            cut = datetime.now(timezone.utc) - timedelta(hours=48)
            fresh = []
            for aid, when in store.get_awards(code).items():
                if aid not in AWARD_DEFS or not when:
                    continue
                dt = datetime.fromisoformat(when)
                if dt.tzinfo is None:            # SQLite returns naive datetimes; treat as UTC
                    dt = dt.replace(tzinfo=timezone.utc)
                if dt >= cut:
                    _i, nm, ds, _f, _t = AWARD_DEFS[aid]
                    fresh.append(f"{nm} ({ds})")
            if fresh:
                student_context["mastery_note"] = (str(student_context.get("mastery_note", "")) +
                    "\n[AWARDS: this student JUST earned: " + "; ".join(fresh[:3]) +
                    ". If it fits naturally, congratulate them briefly ONCE for the effort it took "
                    "-- then keep teaching. Don't repeat the congratulations every turn.]")
    except Exception as exc:  # noqa: BLE001
        print(f"[awards] tutor note failed: {exc}")

    # LIKELY MISCONCEPTION (2026-08-10, build ck). Rules 20-22 say what to DO about a
    # wrong answer; rule 49 says to work out WHICH RULE produced it first. This is the
    # part the model cannot do from the prompt alone at speed: match what the student
    # just said against the 148 catalogued error patterns for this course and, on a hit,
    # hand him the diagnosis AND the remedy in the same breath.
    # Framed as a possibility he may discard, always. The matcher is conservative --
    # bare numbers were stripped from the evidence at build time, matches are on word
    # boundaries, and at most two theories come back -- but it is still a guess about a
    # child's thinking, and a confident wrong diagnosis is worse than none (rule 49d/e).
    # build cm: this note travels with the TURN, not in the system prompt. Appending it
    # to the prompt (as build ck did) moved the cache prefix and re-billed ~16k tokens
    # on exactly the turns the hint fired. It is per-turn information; it belongs next
    # to the message it is about.
    turn_note = ""
    try:
        if misconceptions is not None and message and not message.startswith("__"):
            turn_note = misconceptions.hint_note(req.course, message)
    except Exception as exc:  # noqa: BLE001 -- a hint is never worth failing a turn over
        print(f"[misconceptions] hint failed: {exc}")
        turn_note = ""

    # FOUNDATION MEMORY (2026-08-09, build ce): which canonical introductions this
    # student has already sat through, so rule 40 can ASK instead of replaying one.
    # This is the ONLY place the tutor can learn it -- a new session's history is empty.
    student_context["foundations_heard"] = _foundations_heard(code, req.course)
    # THE PROMPT IS DELIBERATELY STABLE (2026-08-10, build cn -- reversing build cl).
    # Build cl deferred the wording of already-heard scripts to save ~6,500 characters on
    # an ordinary turn. Then we did the cache arithmetic, and it was the wrong trade:
    #   deferring saves    ~$0.0005 on each ordinary turn
    #   but every flip between the two prompt shapes rebuilds the cached prefix, and
    #   there are two flips per refresher, at ~$0.24
    #   -> it only pays if a student goes 460 turns between refreshers, and rule 40 has
    #      him OFFER one every time a known term comes up.
    # It was also a slower turn each time, which is the thing Jim asked for least of all.
    # So the wording is always carried and the system prompt is byte-identical for the
    # whole of a student's session. A STABLE prompt beats a smaller one: the cache is
    # what makes size cheap, and at ~34k tokens we are using 17% of the context window.
    # The mechanism is left in place (foundations.prompt_block(..., verbatim=False) and
    # wants_refresher) because it becomes the right answer if the library ever grows to
    # where it does not fit, or if the cache lifetime changes. It is dormant, not gone.
    student_context["foundations_verbatim"] = True
    # build cg: does the TODAY bar genuinely exist right now? The net in tutor.py used to
    # infer that from history, which is wrong the moment the page reloads.
    try:
        student_context["today_live"] = bool(store.enabled()
                                             and store.get_today_goals(code, req.course))
    except Exception as exc:  # noqa: BLE001
        print(f"[today] live-check failed: {exc}")
        student_context["today_live"] = False

    # OPENER: the app auto-sends "__open__" when the student opens the lesson (they did NOT
    # type anything). The OLD app sent a literal "Hi!" that got stored as a student turn, so
    # after a few logins the tutor saw "Hi Hi Hi..." and turned snappish. Fix: never store a
    # fake student greeting, strip any leftover junk ones, generate a warm recap, and save
    # ONLY the tutor's reply so the conversation stays coherent.
    if message in ("__open__", "__tour_done__", "__open_declined__", "__tour_done_declined__",
                   "__open_fresh__", "__unit_quiz__"):
        after_tour = message.startswith("__tour_done")
        # 2026-08-07 (build at): "_declined" = the student JUST answered the on-screen
        # assessment-invitation card with "Not right now" -- the tutor must respect it.
        assess_declined = message.endswith("_declined__")
        # 2026-08-07 (build au): "__open_fresh__" = the welcome overlay's "take me to my
        # course path" choice. The student does NOT want to resume the recent side-trip
        # (an explored topic / practice problem); they want their next unmastered unit,
        # which the page sent as the focus unit.
        fresh_start = (message == "__open_fresh__")
        # 2026-08-11 (build du): "__unit_quiz__" = the dashboard's "Retake the Unit
        # Quiz" button. The student came for exactly one thing; deliver exactly that.
        quiz_intent = (message == "__unit_quiz__")
        junk = ("hi", "hi!", "hi.", "hello", "hey", "__open__", "__tour_done__",
                "__open_declined__", "__tour_done_declined__", "__open_fresh__",
                "__unit_quiz__")
        history = [m for m in history if not (
            m.get("role") == "user" and str(m.get("content", "")).strip().lower() in junk)]
        if after_tour:
            # 2026-08-01 (Jim: "after the tour he restates his name as if I just logged in"):
            # the guided screen tour JUST ended, and the tour already introduced Mr. Cadabra
            # by name -- so the lesson opener must not re-introduce him.
            opener_note = (
                "(SYSTEM: The guided SCREEN TOUR just finished — you ALREADY introduced yourself "
                "by name seconds ago, so do NOT say your name again and do NOT re-greet. Flow "
                "straight on from the tour: one enthusiastic bridge sentence, then the one-line "
                "big idea of this course, today's goal + the goals card, and your first question. "
                "The student did NOT type anything; this is NOT an interruption.)")
        else:
            opener_note = (
                "(SYSTEM: The student just OPENED the lesson — they did NOT type anything, and this "
                "is NOT an interruption. If you have met before, warmly greet them back by name and "
                "give a SHORT recap of where you two are and what's next, then invite them to keep "
                "going. If this is your first meeting, begin the first-meeting flow. Do NOT scold "
                "them, do NOT tell them to focus, and do NOT act annoyed.)")
        # 2026-08-11 (build dw, Jim live: "welcome back, we were looking at this chart,
        # ready to keep going?" after DAYS away): the opener now knows the gap. A day
        # or more since the last session in this course -> a real refresher, not a
        # one-liner. Fail-open: no data, no gap note, opener unchanged.
        gap_days = 0
        try:
            if store.enabled():
                la = (store.get_course_activity(code).get(req.course) or {}).get("last_active")
                if la:
                    import datetime as _dt
                    gap_days = max(0, (_dt.date.today()
                                       - _dt.date.fromisoformat(str(la)[:10])).days)
        except Exception as exc:  # noqa: BLE001
            print(f"[opener] gap check failed (ignored): {exc}")
        if gap_days >= 1 and not (after_tour or fresh_start):
            opener_note += (
                f" (ALSO: it has been {gap_days} day{'s' if gap_days != 1 else ''} since "
                "your last session together in this course. Do NOT open with a bare "
                "'ready to keep going?'. Give a REAL refresher first, warmly and briefly "
                "(3-4 sentences): name the unit and topic you two were in, remind them in "
                "plain words what you were working on and what they had already figured "
                "out or nailed (use your notes and the recent conversation), put the key "
                "thing back on the board if it helps, THEN ask one gentle memory-jog "
                "question before moving forward. Memory fades in a few days -- back up a "
                "little; it should feel like a friend catching you up, never a test.)")
        # 2026-08-11 (build dw, Jim live: "it's only showing two bars"): the server KNOWS
        # when the TODAY bar is empty. When it is, the opener's standing instruction to
        # emit [[today items]] becomes a per-turn order it cannot miss.
        if not student_context.get("today_live"):
            opener_note += (
                " (ALSO: the TODAY progress bar at the top of the student's screen is "
                "EMPTY right now. Your FIRST message must state today's short plan (2-3 "
                "items) and emit the matching [[today items=\"...\"]] tag -- resumed "
                "sessions included, every time. No session starts without today's map "
                "on the wall.)")
        if quiz_intent:
            # replaces the generic opener outright -- this door has one purpose
            opener_note = (
                "(SYSTEM: The student clicked 'Retake the Unit Quiz' on their dashboard for "
                "their FOCUS unit -- they came specifically to take that Unit Quiz NOW, and "
                "the app already confirmed the intent. One warm welcome-back sentence, remind "
                "them the record keeps their BEST score so a retake can only help (rule 50), "
                "then administer the FOCUS unit's Unit Quiz per the QUIZZES rules -- the full "
                "quiz, no teaching lesson first, and do NOT make them ask again. Exception: if "
                "your notes show they have genuinely never met some of this unit's topics, say "
                "so plainly and offer a very short warm-up first -- their choice.)")
        if assess_declined:
            opener_note += (
                " (ALSO: the app just showed the Course Assessment invitation card ON SCREEN and "
                "the student chose 'Not right now -- start me at Unit 1.' That question is ASKED "
                "AND ANSWERED. Do NOT mention, offer, or hint at the assessment or placement "
                "again this session -- welcome them warmly and start teaching at Unit 1.)")
        if fresh_start:
            opener_note += (
                " (ALSO: the student clicked 'Take me to my course path' -- they explicitly do "
                "NOT want to pick up the recent side work your notes may mention (an explored "
                "topic or practice problem from another part of the course). Do NOT recap or "
                "resume it. Welcome them back briefly, then run the full opening sequence for "
                "their FOCUS unit (today's topic, the goal + goals card, ready-check) and teach "
                "that unit from where their mastery actually stands.)")
        reply = _bold_first_terms(tutor.get_tutor_reply(student_context, history, opener_note, req.course, code=code), history)
        _record_learned(code, req.course, reply)
        _record_today_bar(code, req.course, reply)
        history.append({"role": "assistant", "content": reply})
        session["history"] = history
        save_session(code, session, req.course)
        return {"reply": reply}

    reply = _bold_first_terms(tutor.get_tutor_reply(student_context, history, message, req.course,
                                                    code=code, turn_note=turn_note), history)
    _record_learned(code, req.course, reply)
    _record_today_bar(code, req.course, reply)

    # Remember this exchange so the tutor recalls it next time.
    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": reply})
    session["history"] = history
    save_session(code, session, req.course)

    # Real tracking: the COURSE now teaches all 9 units starting at the student's
    # placed unit, so course activity counts as "learning" whatever unit they're on.
    # UNPLACED (2026-08-07 build ba, Jim's dashboard catch): count activity toward the
    # FIRST UNMASTERED unit -- a brand-new student's is Unit 1. The old flat default of 2
    # made fresh elementary students SKIP Unit 1 entirely: the first turn logged "learning
    # Unit 2", the mastery note then steered the tutor there, and Counting & Number Sense
    # was never taught.
    course_unit = 1
    try:
        su = int((placement or {}).get("start_unit") or 0)
        if 1 <= su <= 9:
            course_unit = su
        elif store.enabled():
            checks = (store.get_mastery(code, req.course) or {}).get("checks", {})
            for u in range(1, 10):
                if int((checks.get(u) or {}).get("best_pct") or 0) < store.PASS_PCT:
                    course_unit = u
                    break
    except (TypeError, ValueError):
        course_unit = 1
    except Exception as exc:  # noqa: BLE001 -- a tracking miss must never break the turn
        print(f"[track] unplaced-unit lookup failed: {exc}")
        course_unit = 1
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

    # FOUNDATION MEMORY (build cf): practice and topic teach vocabulary too, so they get
    # the same canonical scripts AND the same "already introduced -- ask first" list. A
    # student must not hear one definition of "denominator" in the lesson and a different
    # one on the topic page (rule 28), and a term they met here counts as met.
    student["foundations_heard"] = _foundations_heard(req.code.strip(), req.course)
    reply = _bold_first_terms(tutor.get_practice_reply(student, req.problem, safe_history, message, req.course, code=req.code.strip()), req.history)
    _record_learned(req.code.strip(), req.course, reply)

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
    student["foundations_heard"] = _foundations_heard(req.code.strip(), req.course)
    reply = _bold_first_terms(tutor.get_topic_reply(student, req.topic, _sanitize_history(req.history), message, req.course, code=req.code.strip()), req.history)
    _record_learned(req.code.strip(), req.course, reply)

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
def speak(text: str = "", code: str = "", lead: int = 0):
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

    `lead` (2026-08-03, Jim: "the initial talk almost always misses his first couple of words"):
    extra ~280ms blocks of leading silence, 0-4. The page sends lead=3 (~1.1s total) on the FIRST
    clip of a session -- audio outputs (especially Bluetooth) close during the quiet thinking wait
    and reopen slowly, eating the head of the clip; a longer silent lead means they eat silence.
    Later clips keep the standard single block.
    """
    _require_student(code)
    _rate_limit("speak:" + code.strip(), limit=60, window_seconds=300, what="voice requests")
    text = (text or "").strip()
    if len(text) > MAX_SPEAK_CHARS:
        raise HTTPException(status_code=413, detail="That text is too long to speak.")
    if not text or not ELEVEN_API_KEY:
        return Response(status_code=204)
    return _tts_stream_response(text, lead, code=code.strip(), mode="speak")


# 2026-08-01 (Jim's beta run: "he sometimes drops the first word"): audio output paths
# (especially Bluetooth) take ~100-300ms to open, swallowing the start of playback. We
# prepend ~280ms of REAL MP3 SILENCE (mono 44.1kHz 128k, matching ElevenLabs' format) to
# every served clip, so what gets swallowed is silence -- the first word survives. The
# silence is added at SERVE time only; cached files stay pure voice.
import base64 as _b64
_TTS_LEAD_SILENCE = _b64.b64decode(
    "SUQzBAAAAAAAI1RTU0UAAAAPAAADTGF2ZjYwLjE2LjEwMAAAAAAAAAAAAAAA//uQwAAAAAAAAAAAAAAAAAAAAAAASW5mbwAAAA8AAAAMAAAVOAAnJycnJycnJzs7Ozs7Ozs7Tk5OTk5OTk5iYmJiYmJiYmJ2dnZ2dnZ2domJiYmJiYmJnZ2dnZ2dnZ2dsbGxsbGxsbHExMTExMTExNjY2NjY2NjY2Ozs7Ozs7Ozs//////////8AAAAATGF2YzYwLjMxAAAAAAAAAAAAAAAAJAOEAAAAAAAAFTh99LqRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA//uQxAADwAABpAAAACAAADSAAAAETEFNRTMuMTAwVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVTEFNRTMuMTAwVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//uSxDkDwAABpAAAACAAADSAAAAEVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVUxBTUUzLjEwMFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVf/7ksQ5A8AAAaQAAAAgAAA0gAAABFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVMQU1FMy4xMDBVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVX/+5LEOQPAAAGkAAAAIAAANIAAAARVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVTEFNRTMuMTAwVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//uSxDkDwAABpAAAACAAADSAAAAEVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVUxBTUUzLjEwMFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVf/7ksQ5A8AAAaQAAAAgAAA0gAAABFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVMQU1FMy4xMDBVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVX/+5LEOQPAAAGkAAAAIAAANIAAAARVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVTEFNRTMuMTAwVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//uSxDkDwAABpAAAACAAADSAAAAEVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVUxBTUUzLjEwMFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVf/7ksQ5A8AAAaQAAAAgAAA0gAAABFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVMQU1FMy4xMDBVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVX/+5LEOQPAAAGkAAAAIAAANIAAAARVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVTEFNRTMuMTAwVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//uSxDkDwAABpAAAACAAADSAAAAEVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVUxBTUUzLjEwMFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVf/7ksQ5A8AAAaQAAAAgAAA0gAAABFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVU=")


def _tts_stream_response(text: str, lead: int = 0, code: str = "", mode: str = "speak"):
    """Shared TTS pipeline (used by /api/speak and /api/demo-audio): serve the cached
    render if we have it, otherwise stream from ElevenLabs while caching atomically.
    `lead` = extra leading-silence blocks (0-4) beyond the standard one -- the first clip
    of a session gets more so a sleeping audio output eats silence, not words.
    `code`/`mode` (2026-08-04): attribute this request in the usage log -- character
    count + cache hit/miss only, never the text itself."""
    lead_silence = _TTS_LEAD_SILENCE * (1 + max(0, min(int(lead or 0), 4)))
    # Cache HIT: replay the saved render, no ElevenLabs call.
    cache_path = _tts_cache_path(text)
    cache_hit = False
    try:
        cache_hit = cache_path.exists() and cache_path.stat().st_size > 0
    except Exception as exc:  # noqa: BLE001
        print(f"[speak] cache stat error: {exc}")
    # USAGE LOG (2026-08-04): a miss is about to spend ElevenLabs characters; a hit is free.
    # Fire-and-forget -- log_usage swallows its own errors and no-ops when the DB is off.
    store.log_usage(kind="tts", code=code, mode=mode, model=str(ELEVEN_MODEL or ""),
                    tts_chars=len(text), tts_cache_hit=cache_hit)
    try:
        if cache_hit:
            return Response(content=lead_silence + cache_path.read_bytes(),
                            media_type="audio/mpeg")
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
        yield lead_silence               # leading silence: see note above (never cached)
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


# -----------------------------------------------------------------------------
# DEMO VOICE (2026-07-30) -- the marketing demo speaks with Mr. Cadabra's REAL voice.
# -----------------------------------------------------------------------------
# The interactive demo (static/demo.html) is fully scripted, so its spoken lines are a
# FIXED, finite list. This endpoint serves ONLY those whitelisted lines -- no arbitrary
# text, so it cannot be abused to spend ElevenLabs money beyond ~14 lines that each
# cache after their first render (then replay free, forever). No login code needed
# (it's the public demo); per-IP rate limited. KEEP THIS LIST IDENTICAL to VOICE_LINES
# in static/demo.html -- update both together.
DEMO_VOICE_LINES = [
    "Hi! I'm Mr. Cadabra. Let's solve this one together — two x plus three equals eleven. Our whole goal is to get x all by itself. First move: what should we do to BOTH sides to undo that plus three? Type your move with the keyboard.",
    "Exactly — subtract three from both sides, and the threes cancel on the left.",
    "Not quite — the plus three is being added, so we do the opposite: subtract. Try typing your move again!",
    "Now we've got two x equals eight. Two x means two TIMES x — so what undoes a times two? Type your move.",
    "Nice — divide both sides by two. Notice the board is waiting for YOU — it never gives away the answer.",
    "Careful — two x means two times x, so we undo it with division. Give it another go!",
    "So — eight divided by two. What does x equal? Work it out and type it with the keyboard.",
    "You got it — x equals four! And look: it checks out, two times four plus three really is eleven.",
    "Close — eight divided by two. What number is that? Type it in.",
    "One quick challenge to show off the keyboard. Type two, then tap the x-to-the-n key, then type three — that builds two to the third power.",
    "Beautiful — two to the third, which is eight. You used the power key like a pro.",
    "Order matters: type 2 first, then the xⁿ key, then 3 — that builds 2^3. Try it!",
    "That's it — you just solved a two-step equation and checked it yourself. Great work! That's how Mr. Cadabra's Classroom teaches: one friendly step at a time.",
    "Hi! I'm Mr. Cadabra. Let's count together! Look — I put some stars on the board. Count them with your finger… how many stars do you see? Tap your answer.",
    "Yes! Five stars — you counted every single one.",
    "Almost! Point at each star and count them one at a time — then tap your answer.",
    "Now watch the magic — here comes one more star! How many stars are there now? Tap your answer.",
    "Six! Five stars plus one more makes six. You just did adding!",
    "Count the new star too — five stars, then one more. Tap your answer!",
    "Fractions — the friendly way. The board shows one half plus one fourth. Here's the trick: one half is the same as two fourths. So two fourths plus one more fourth makes how many fourths? Tap your answer.",
    "Three fourths! Once the bottom numbers match, you just add the tops.",
    "Look at the board — two fourths plus one more fourth. Count the fourths and tap again!",
    "Decimals now. Which is bigger — zero point five, or zero point four five? Careful — more digits does not mean bigger! Tap your answer.",
    "Right! Zero point five is five tenths, and zero point four five is only four and a half tenths. You didn't fall for the trap!",
    "Line them up: zero point five zero versus zero point four five. Which has more tenths? Tap again!",
    "Negative numbers — the number one key to algebra. The board shows negative three plus five. Start three below zero and climb up five… where do you land? Type it in.",
    "Two! You climbed from three below zero up to positive two. Negatives hold no fear for you.",
    "Start at three below zero and climb up five steps, one at a time. Where do you land? Type it!",
    "One more: negative four times negative two. Remember the rule — when the two signs match, the answer is positive. Type it in.",
    "Eight! A negative times a negative flips positive. That one rule unlocks half of algebra.",
    "Both signs are negative — a matching pair — so the answer is POSITIVE four times two. Type it!",
    "Every triangle's angles add up to one hundred eighty degrees — always. This one has a ninety and a thirty-five. How big is the mystery angle? Type it in.",
    "Fifty-five degrees! Ninety plus thirty-five is one twenty-five, and one eighty minus that leaves fifty-five.",
    "Add the two angles you know first — ninety plus thirty-five — then subtract from one eighty. Type it!",
    "Now the most famous theorem in math. A right triangle has legs three and four — the board shows Pythagoras at work. What's the long side? Type it in.",
    "Five! The three-four-five triangle — builders have trusted it for four thousand years.",
    "c squared is twenty-five — so c is the number that times itself makes twenty-five. Type it!",
    "Exponentials — where algebra gets powerful. The board asks: two to what power makes thirty-two? Count the doublings. Type the power.",
    "Five! Two, four, eight, sixteen, thirty-two — five doublings. You just did a logarithm without the scary name.",
    "Keep doubling: two, four, eight… count how many steps it takes to reach thirty-two. Type that count!",
    "Now a quadratic, factored and ready: x minus five, times x plus two, equals zero. For the whole thing to be zero, one piece must be zero. What x makes the FIRST piece zero? Type it.",
    "Five! And x equals negative two kills the other piece. Two solutions, no sweat — that's the zero-product property.",
    "Look at the first piece: x minus five. What x makes it exactly zero? Type it!",
    "Welcome to the unit circle — the heart of trigonometry. Half a spin around the circle is pi radians. How many degrees is that? Type it in.",
    "One hundred eighty degrees! Radians are just another ruler for angles — pi is exactly half the circle.",
    "A FULL circle is three hundred sixty degrees, and pi radians is exactly half of it. Type the degrees!",
    "Now the launchpad to calculus: sine of ninety degrees — the very top of the circle. What's its value? Type it in.",
    "One! At the top of the circle you're at full height. Trig is just reading heights and shadows off a circle.",
    "At ninety degrees you're at the very TOP of the unit circle — as high as it gets. That height is… type it!",
    "Statistics time. Three quiz scores on the board: three, five, and ten. The mean is the fair-share average — add them up, split them evenly. What's the mean? Type it in.",
    "Six! Eighteen points split evenly three ways. The mean shares everything out fairly.",
    "Add all three first — three plus five plus ten — then divide by how many scores there are. Type it!",
    "Now the median — the MIDDLE value once they're in order. Same three scores. What's the median? Type it in.",
    "Five! Mean six, median five — two different stories from the same data. That gap is where statistics gets interesting.",
    "Line them up smallest to biggest and take the one sitting in the middle. Type it!",
    "Calculus asks one big question: how fast is something changing? For x cubed, the power rule answers it — bring the three down front, drop the power by one. What's the new power? Type it in.",
    "Two! So the derivative is three x squared — you just took your very first derivative.",
    "The rule says drop the power by ONE. Three minus one is… type it!",
    "Let's use it. The slope of x cubed at x equals two is three times two squared. Work that out — type the slope.",
    "Twelve! At x equals two the curve is climbing twelve units per step. That's calculus — exact speed at an exact instant.",
    "Two squared is four, times three is… type it!",
    "Differential equations describe how things change — and rule one is: classify first. The board shows y double-prime plus y equals zero. The ORDER is the highest derivative in sight. What order is this? Type the number.",
    "Second order — the double-prime is the giveaway. This little equation runs every pendulum and guitar string on Earth.",
    "Count the tick marks on the busiest y — double-prime means the SECOND derivative. Type the order!",
    "One more to classify: y prime equals three y. What order is this one? Type the number.",
    "First order! And it's the equation of growth itself — money, bacteria, radioactive decay. Every model starts with classify.",
    "Just one tick mark on the y — that's the FIRST derivative. Type the order!",
    "And that's how I teach — I talk, the board shows every step, and you do the thinking. Try another level, or come meet me in the real classroom!",
    "Let's look at it a different way — I've put the whole move on the board. Follow it through, then type your answer!",
    "Let's look at it a different way — I've put the whole move on the board. Follow it through, then tap your answer!",
    "No worries — I'll show you this one! The answer is on the board now. In my real classroom I keep trying new ways — smaller steps, new pictures — until it clicks. On we go!",
    # 2026-08-05 (build aj): the landing hero's "Hear him teach" button plays this line.
    # APPENDED (never reorder -- cached audio indices must stay valid; keep identical to
    # demo.html's VOICE_LINES).
    "Hi, I'm Mr. Cadabra! Here's how I teach: I talk you through it in my own voice, the board shows every step, and you do the thinking — I never just hand over the answer. Come try a free lesson, and I'll meet your student right at their level.",
    # APPENDED 2026-08-09 (build bt, classroom-demo redesign): welcome + 3 tour stops +
    # picker invite + 10 course intros + congratulations. NEVER reorder; keep identical
    # to demo.html's VOICE_LINES.
    "Welcome to the demo! This is Mr. Cadabra's Classroom — the very screen your student will learn on. Before we solve anything, let me show you around.",
    "This big space is my whiteboard. Every step of every problem gets drawn right here — the board leads, and my voice follows. Nothing ever happens only in words.",
    "See the bars up top? That's your student's map — today's goals, the current unit with a marker for every quiz, and the whole course marching gold toward the Final Exam. They always know exactly where they are.",
    "And this is me, Mr. Cadabra! In the real classroom we simply talk — your student says their answer out loud and we go back and forth like a real teacher and student. Here in the demo, you'll type or tap your answers instead.",
    "That's the classroom! Ready to try a real problem? Pick your student's level — anywhere from counting stars to differential equations — and I'll teach you the exact way I teach them.",
    "Entry-Level Math — where the adventure begins! We make numbers friendly with pictures you can count. Here's a real one from my classroom.",
    "Basic Math — fractions and decimals, the friendly way. Here's a real one from my classroom.",
    "Pre-Algebra — where negative numbers stop being scary. Here's a real one from my classroom.",
    "Algebra One — the mystery-number hunt! Let's solve a real two-step equation together, exactly like a lesson.",
    "Geometry — shapes, angles, and the most famous theorem in all of math. Here's a real one from my classroom.",
    "Algebra Two — exponents and quadratics, the real power tools. Here's a real one from my classroom.",
    "Trig and Pre-Calc — where everything flows from one beautiful circle. Here's a real one from my classroom.",
    "Probability and Statistics — teaching numbers to tell the truth. Here's a real one from my classroom.",
    "Calculus — the mathematics of change itself. Let's take your very first derivative together.",
    "Differential Equations — the equations that run the physical world. Let's classify one like a pro.",
    "Congratulations — you just worked a real problem, step by step, exactly the way your student will! In the full classroom we talk back and forth by voice, quizzes unlock new topics, and medals land in the trophy case. Come meet me for a free lesson — I'll start right at your student's level.",
    # APPENDED 2026-08-09 (build bv, full-page demo): the seven SIDEBAR tour stops,
    # so the demo walks the screen exactly like a new student's tour.
    "Over here on the left is your Curriculum — everything in the course, laid out in nine units. Your student can open any unit and see exactly what's inside it, so the whole year is never a mystery.",
    "Right below it, the Course Assessment. Whenever they're ready, it finds their strengths and builds a recommended path just for them. It's completely optional, and it's always waiting right there.",
    "Next, the Progress dashboard. That's where they watch themselves win — units mastered, accuracy, streaks, and a trophy case for every award they earn.",
    "Then Practice a problem. When your student is stuck on one specific problem — homework, a worksheet, anything — they bring it here and we work through it together.",
    "Right under it, Explore a topic. Curious about just one thing, like fractions or slope? They open it, name the topic, and we dig into exactly that.",
    "And the Final Exam — the top of the mountain. It unlocks only after all nine units are mastered, and passing it makes them a Course Champion.",
    "Last one on the left: Look it up. Any time they just want to READ about something, they tap it, type the topic, and a page opens right on top of the lesson. Their place is waiting when they close it.",
    # APPENDED 2026-08-09 (build bw): the per-course TEACH step (95-104), the
    # dashboard chooser (105), and the three dashboard tours (106-114).
    "Before we count anything, here's the trick: we touch each one and say the numbers in order. Watch me count these three stars — one… two… three. The last number you say is how many there are. Now you try with a new group!",
    "A fraction is just a number cut into equal pieces. Look at the bar on the board: it's cut into four equal pieces, so each piece is one fourth. Shade two of them and you have two fourths — which is exactly the same amount as one half. Now let's use that.",
    "Here's a number line. Zero sits in the middle, positive numbers run to the right, and negative numbers run to the left. Adding moves you to the right; subtracting moves you left. Watch: start at negative two, climb three steps right, and you land on positive one. Your turn next.",
    "Solving means getting x all by itself, and the one rule is: whatever you do to one side, you do to the other. Watch a quick one — x plus four equals ten. Subtract four from both sides, and x equals six. Now let's do a two-step one together.",
    "Every triangle's three angles add up to one hundred eighty degrees — always, no exceptions. Watch a friendly one: sixty plus sixty plus sixty is one hundred eighty. Now let's find a missing angle.",
    "An exponent just counts how many times you multiply. Two to the third means two times two times two, which is eight — each step doubles what you had. Now let's run that backwards.",
    "The unit circle measures turns two ways. A quarter turn is ninety degrees, and in radians we call that same quarter turn pi over two. Degrees and radians are just two rulers for the same angle. Now let's convert one.",
    "The mean is the fair-share average: add everything up, then split it evenly. Watch — two scores, four and eight. Together that's twelve, split between two people is six each. Now let's do three scores.",
    "The power rule is the first tool in calculus: bring the power down in front, then drop the power by one. Watch — x squared becomes two x. That's it, that's the whole move. Now you try it on a bigger one.",
    "Rule one in differential equations is: classify before you solve. The ORDER is simply the highest derivative in sight — count the tick marks. Watch: y triple-prime has three ticks, so that's third order. Now you classify one.",
    "And that's a real lesson! Now let me show you what the grown-ups see. There are three windows into your student's progress — theirs, a teacher's, and a parent's. Pick whichever one you'd like to look at, and I'll walk you through it.",
    "This is the student's own dashboard — the one they open to watch themselves win. Right up top: units mastered, how accurate they've been, problems practiced, and the day streak they're protecting.",
    "Below that is their course map — nine units, turning gold as each one is mastered, marching toward the Final Exam. It's the same map they see on the bars during a lesson, so their progress is never a mystery.",
    "And this is the trophy case. Every award is earned by real work — exploring a topic, practicing it, learning it, mastering the unit, and the effort medal for sticking with something hard. Nothing here is decoration.",
    "This is the teacher's view — the whole class on one screen. Each student's current unit, their accuracy, when they last worked, and a flag when someone needs a hand today.",
    "This column is the one teachers tell us they use most: what to strengthen next, for each student, in plain words. It comes from what actually went wrong in their lessons, not from a generic level number.",
    "And down here is my honest read on the class — where the group is solid, where several students are wobbling on the same idea, and what I'd teach next. A teacher can use it or overrule it; it's a colleague's opinion, not a verdict.",
    "This is the parent's view, and it answers the only question that really matters: how is my child actually doing? No jargon, no scores to decode — just an honest read in plain English.",
    "Here's the week at a glance — time spent, what they mastered, and what they struggled with. If your child had a rough day, you'll see it here, because a dashboard that only shows good news isn't worth having.",
    "And this button prints the whole record — every unit, every quiz, every hour — for a homeschool portfolio or a school district's file. It's your data; you can take it with you any time.",
    # APPENDED 2026-08-09 (build bx): every lesson rebuilt for VOICE answering and
    # for figures that actually appear (115-134).
    "Your turn. The board shows negative three plus five, and there's your number line right underneath it. Start three steps below zero, climb five steps to the right, and tell me where you land. Tap the microphone and say it out loud.",
    "Not quite — let's walk it together. Put your finger on negative three, then count five hops to the right: negative two, negative one, zero, one… and one more. Tap the mic and say where you land.",
    "Now a real one — it's on the board: two x plus three equals eleven. Our whole goal is to get x all by itself, so the first move is undoing that plus three. What should we do to BOTH sides? Tap the microphone and say your move.",
    "Close — the three is being ADDED, so we undo it with the opposite move. Tap the mic and tell me what to do to both sides.",
    "Look at the board now: two x equals eight. Two x means two TIMES x — so what undoes a times two? Tap the microphone and say your move.",
    "Careful — two x means two times x, so we undo it with division, not subtraction. Tap the mic and try that once more.",
    "Last step. The board says eight divided by two — so what does x equal? Tap the microphone and say the number.",
    "Almost — think of eight split into two equal groups. Tap the mic and say how many are in each group.",
    "Now look at the triangle on the board. Two of its angles are marked for you — ninety degrees and thirty-five degrees — and the third one has a question mark. All three together must add to one hundred eighty. Tap the microphone and tell me that missing angle.",
    "Let's build it up in two moves — first add the two angles you can see, ninety plus thirty-five. Then take that away from one hundred eighty. Tap the mic and say what's left.",
    "Here's the puzzle on the board: two to WHAT power makes thirty-two? Start at two and count how many times you double. Tap the microphone and say the power.",
    "Keep doubling out loud with me — two, four, eight, and so on. Count each step until you reach thirty-two, then tap the mic and say how many steps that took.",
    "Now look at the circle on the board. The arrow sweeps exactly HALF the way around, and half a turn is what we call pi radians. How many degrees is that half turn? Tap the microphone and say it.",
    "Think about the whole circle first — all the way around is three hundred sixty degrees. Our arrow goes exactly half that far. Tap the mic and say the number.",
    "Three quiz scores are on the board — three, five and ten — drawn as bars so you can see their sizes. The mean is the fair share: add them all up, then split the total evenly three ways. Tap the microphone and say the mean.",
    "Let's do it in two moves — first add three, five and ten together. Then split that total into three equal shares. Tap the mic and say what one share is.",
    "Your turn with the power rule. The board shows x CUBED. Bring the three down in front, then drop the power by one — what is the NEW power? Tap the microphone and say it.",
    "Just the second half of the rule: the old power is three, and we drop it by one. Tap the mic and say what that leaves.",
    "Now you classify one. The board shows y double-prime plus y equals zero. The order is simply the highest derivative in sight — count the tick marks on the busiest y. Tap the microphone and say that number.",
    "Look right at the y carrying the most tick marks — two of them means the SECOND derivative. Tap the mic and say that order as a number.",
    # APPENDED 2026-08-09 (build bx): the three FULL dashboard tours, six stops
    # each (135-152), walking a complete invented student's record.
    "This is Maya's own dashboard — the screen your student opens to watch themselves win. Right at the top, the numbers that matter: four units mastered, ninety-one percent accuracy, three hundred twelve problems worked, and an eleven-day streak she is very proud of.",
    "Here's her whole course, all nine units. The gold ones are mastered — she's finished Numbers, Fractions, Ratios and Percents. Unit five is where she's working right now, and the four ahead are still waiting. At the end sits the Final Exam, locked until every unit is gold.",
    "Open the unit she's in and you see the ladder inside it: every topic, every quiz, and the score she earned. Comparing decimals, eighty-eight percent. Adding and subtracting, ninety-two. Multiplying is where she is today, and the Unit Quiz waits at the top.",
    "These two charts are her habits. On the left, accuracy week by week — you can see the dip in week three when percents got hard, and the climb back after we slowed down. On the right, minutes per day this week. Honest pictures, both of them; a dashboard that only shows good news isn't worth having.",
    "And this is the trophy case — twelve awards, every one of them earned. Explored a topic. Practiced it. Learned it. Mastered a whole unit. The Course Champion medal from finishing Basic Math last spring. And the effort medal, which she got for coming back to percents four days in a row until they clicked.",
    "Last, what's coming: the exact next three sessions, so she never wonders what happens tomorrow. And down here, her courses — Basic Math finished and championed, Pre-Algebra in progress, with everything from her old course still on the record.",
    "Now the teacher's view. This is Room Twelve — six students in Pre-Algebra — and the top row is the class at a glance: average accuracy, how many are on track, how many need a hand today, and the hours the class put in this week.",
    "Here's the roster. Every student, the unit they're in, their accuracy, their streak, and when they last worked. Ben hasn't been in for four days and his accuracy is sliding — so he's flagged in red at the top of your attention, not buried on page three.",
    "This grid is the one that saves a teacher a whole planning period. Nine units across, six students down, and every square colored: mastered, in progress, or not started. In one glance you can see that the whole class stalled in the same place — Unit two, fractions.",
    "Then, in plain words, what to strengthen next for each student — and WHY. Not a level number, not a percentile. Ben is stalling on borrowing across a zero. Aiden can't find a common denominator yet. That's what actually went wrong in their lessons this week.",
    "And this is my honest read on the class. Where they're solid, where several of them are wobbling on the very same idea, and what I would teach next if it were my room. A teacher can take it or overrule it — it's a colleague's opinion, never a verdict.",
    "Down at the bottom: what's coming. Who has a Unit Quiz this week, who is close to their Final Exam, and the class time chart so a teacher can see who is quietly doing nothing.",
    "And now the view most parents care about. It opens with the only question that really matters — how is my child actually doing? — answered in plain English, with no jargon and no scores to decode.",
    "Here's her week: four days in, two hours and fifteen minutes, one unit mastered, and the thing she struggled with. We put the hard part right next to the good part on purpose. If your child had a rough week, this page will tell you so.",
    "This is the longer arc — every week since she started in September. Hours, accuracy, units mastered. You can watch her get better, and you can see exactly which week percents nearly beat her.",
    "Everything she has mastered, with the date and the quiz score that proved it. This is the list you'd want if anyone ever asks what your child has actually learned this year.",
    "And this is the part I'd read first: what's hard for her right now, and what we are doing about it. Lining up decimal points when the numbers have different lengths. My plan is smaller numbers and money problems until it feels ordinary — and I'll tell you here when it does.",
    "Finally, the record. Every unit, every quiz, every hour, printable in one click for a homeschool portfolio or a school district file. It's your data and your child's work — you can take it with you any time, and you never have to ask us for it.",
    "Look at the board — two fourths plus one more fourth. Count the shaded pieces and tap again!",
    # APPENDED 2026-08-09 (build bz): the demo drops the microphone -- these are the
    # TYPED versions of the lesson lines (154-173). 115-134 (the mic wording) are
    # now unused but stay in place: indices must never move.
    "Your turn. The board shows negative three plus five, and there's your number line right underneath it. Start three steps below zero, climb five steps to the right, and type where you land.",
    "Not quite — let's walk it together. Put your finger on negative three, then count five hops to the right: negative two, negative one, zero, one… and one more. Type where you land.",
    "Now a real one — it's on the board: two x plus three equals eleven. Our whole goal is to get x all by itself, so the first move is undoing that plus three. What should we do to BOTH sides? Type your move.",
    "Close — the three is being ADDED, so we undo it with the opposite move. Type what you'd do to both sides.",
    "Look at the board now: two x equals eight. Two x means two TIMES x — so what undoes a times two? Type your move.",
    "Careful — two x means two times x, so we undo it with division, not subtraction. Try that once more.",
    "Last step. The board says eight divided by two — so what does x equal? Type the number.",
    "Almost — think of eight split into two equal groups. Type how many are in each group.",
    "Now look at the triangle on the board. Two of its angles are marked for you — ninety degrees and thirty-five degrees — and the third one has a question mark. All three together must add to one hundred eighty. Type that missing angle.",
    "Let's build it up in two moves — first add the two angles you can see, ninety plus thirty-five. Then take that away from one hundred eighty. Type what's left.",
    "Here's the puzzle on the board: two to WHAT power makes thirty-two? Start at two and count how many times you double, then type the power.",
    "Keep doubling with me — two, four, eight, and so on. Count each step until you reach thirty-two, then type how many steps that took.",
    "Now look at the circle on the board. The arrow sweeps exactly HALF the way around, and half a turn is what we call pi radians. How many degrees is that half turn? Type it in.",
    "Think about the whole circle first — all the way around is three hundred sixty degrees. Our arrow goes exactly half that far. Type the number.",
    "Three quiz scores are on the board — three, five and ten — drawn as bars so you can see their sizes. The mean is the fair share: add them all up, then split the total evenly three ways. Type the mean.",
    "Let's do it in two moves — first add three, five and ten together. Then split that total into three equal shares. Type what one share is.",
    "Your turn with the power rule. The board shows x CUBED. Bring the three down in front, then drop the power by one — what is the NEW power? Type it in.",
    "Just the second half of the rule: the old power is three, and we drop it by one. Type what that leaves.",
    "Now you classify one. The board shows y double-prime plus y equals zero. The order is simply the highest derivative in sight — count the tick marks on the busiest y, and type that number.",
    "Look right at the y carrying the most tick marks — two of them means the SECOND derivative. Type that order as a number.",
    # APPENDED 2026-08-09 (build bz): dashboard tours rewritten to describe the REAL
    # product screens (174-187). The earlier tours (135-152) described sections the
    # product does not have and are now unused; indices never move.
    "This is Maya's own dashboard — the real screen your student opens. These five numbers are exactly the ones the product tracks: units mastered, accuracy, problems practiced, time this week, and the day streak she's protecting.",
    "Below it, her course — all nine units. The gold ones are mastered, and mastered here means ninety percent or better on the Unit Quiz with no hints. Unit five is where she's working now, and the Final Exam at the end stays locked until every unit is gold.",
    "Open a unit and you see the quiz results inside it — every topic quiz, the score, and the date. This is the same detail a parent or a teacher sees, because there's only one set of numbers and everybody gets the truth.",
    "Strengthen next is my short list for her: the specific things that actually went wrong in her lessons this week. Not a level, not a percentile — the two habits I'd fix first.",
    "And the trophy case. Explored, practiced, learning, mastered, the effort medal, and the Course Champion medal she earned for finishing Basic Math. Every one of them comes from real work; none of them are participation stickers.",
    "Now the teacher's side. A teacher opens a class with its class code — this is Room Twelve — and every class they run sits in one place.",
    "Here's the class. One row per student, showing how many of the nine units they've mastered, how many they've started, and a star when a unit is finished. Nothing here is guessed; it's the same mastery record the student sees.",
    "The column that matters most is this one: needs attention. A student who has stalled, or whose scores are sliding, gets flagged here so they're the first thing a teacher sees instead of the last thing they find out.",
    "And a teacher can open any student to see their full dashboard, read-only — the same numbers, the same quiz history, the same short list of what to strengthen next. Adding a student is one box: their student code.",
    "And this is the parent's view. It's the same dashboard, opened with a parent's link — but it leads with the question a parent actually has: how is my child really doing, in plain English.",
    "That's my honest read. It names what she's good at, what she's stuck on, and what I'm doing about it. If your child had a hard week, this paragraph will say so — a report that only ever says 'great job' isn't worth reading.",
    "Underneath are the same five numbers her teacher and I see. One record, one set of facts, no separate parent version that quietly rounds things up.",
    "Strengthen next tells you exactly where she is wobbling right now — and because it comes from her actual lessons, it's specific enough to help with at the kitchen table.",
    "And this prints the whole record: every unit, every quiz, every hour, ready for a homeschool portfolio or a school district file. It's your child's work, and you can take it with you any time.",
    # 2026-08-10 (build cp): the four AUDIENCE INTROS for /demo?view=... -- the
    # "view the demo" button on the parents, teachers, homeschool and students pages.
    # APPENDED, never reordered: clips are addressed by INDEX, so an insert anywhere
    # above would silently shift every cached clip after it. Must stay byte-identical
    # to demo.html's VOICE_LINES.
    "Welcome — this is the parent's view of Mr. Cadabra's Classroom, using a made-up student so no real child's record is ever on display. In a moment I'll walk you through the dashboard you'd open: what your child has actually mastered, what they're working on right now, what's hard this week, and the printable record you can take with you. Everything you'll see comes from real work — we never invent a number to make a week look better than it was.",
    "Welcome — this is the teacher's view of Mr. Cadabra's Classroom, built from a made-up class so no real student is ever on display. I'll walk you through the roster, who needs you this week and why, the mastery picture across the whole class, and the time each student actually spent. Every number is earned: mastery means ninety percent or better on a unit quiz with no hints from me.",
    "Welcome — this is the homeschool view of Mr. Cadabra's Classroom, using a made-up student so no real child's record is ever on display. I'll show you the dashboard you'd open each week, and the part homeschool families ask about first: the printable record. Every unit, every quiz, every hour, dated and ready for a portfolio or a district file. It's your child's work and you can take it with you any time.",
    "Hi! This is your dashboard — the screen you'd open every time you come back. I'm using a made-up student called Maya so nobody's real work is on show. I'll walk you through your five numbers, your course map with the gold units you've mastered, what you're working on next, and the trophies you've earned. Everything here is stuff you actually did.",
    # 2026-08-10 (build cq): the HOMESCHOOL stop lines for /demo?view=homeschool.
    # Same screen as the parent view, different audience: a homeschool parent IS the
    # teacher. APPENDED; must stay byte-identical to demo.html's VOICE_LINES.
    "This is the dashboard you'd open on a Monday morning. You are the teacher here, so it leads with the thing you actually need to know before you plan the week: how is this child really doing, in plain English, not a score out of ten.",
    "That's the honest read. It names what she has genuinely got, what she is stuck on, and what Mr. Cadabra is doing about it. If she had a rough week it will say so plainly — a record that only ever says 'great job' is no use to a parent who is also the teacher.",
    "These five numbers are the ones a homeschool week turns on: units mastered, accuracy, problems practised, time on task this week, and the day streak. The hours are measured engaged time, not a timer left running, because in most states the hours are the part you have to be able to stand behind.",
    "Strengthen next is your lesson plan for the week, already written. It comes from her actual work, so it is specific enough to sit down at the kitchen table with — not 'review fractions', but the exact step that is wobbling.",
    "And this is the one homeschool families ask about first. It prints the whole record — every unit, every quiz, every hour, dated — ready for a portfolio, an end-of-year review, or a district file. It is your child's work, and you can take it with you any time, whether or not you stay with us.",
    # 2026-08-10 (build cr): the four AUDIENCE CLOSING lines. Identical to
    # demo.html's VOICE_LINES, APPENDED, never reordered -- clips are served BY
    # INDEX, so an insert above these would play the wrong audio under the right
    # words and nothing would error.
    "And that's the parent's view. Every number on it was earned by a real piece of work — nothing on that screen is a guess, and nothing is rounded up to make a week look better than it was. If you'd like to see what your child actually does in a lesson, I can teach you one right now, at any level from counting to calculus.",
    "And that's the teacher's view. One room, every student, and no guessing about who needs you this week — the flags come from the work itself, not from a survey or a self-report. If you'd like to see what a lesson looks like from the student's side, I can teach you one right now, at any level you choose.",
    "And that's the homeschool view. The week in front of you and the record behind you, both ready whenever you need them, and both built from work your child actually did. If you'd like to see what a lesson looks like, I can teach you one right now, at any level from counting to calculus.",
    "And that's your dashboard! Every gold unit, every trophy, every number on it — you earned all of that yourself. Want to see what a real lesson is like? Pick any level you want and I'll teach you one right now, exactly the way I'd teach you for real.",
    # 2026-08-10 (build cs): FIVE parent stops and FIVE homeschool stops for the
    # rebuilt parent dashboard. The parent tour went from five stops to ten and
    # homeschool overrides all ten BY INDEX. Identical to demo.html, APPENDED.
    "If you only have a minute, this box is the whole dashboard in four lines: what she has mastered, her streak, how accurate she is, and how many problems she has actually done. Underneath it, where to help next — and the link that prints her records.",
    "Here are her nine units. The gold ones are mastered, and every gold unit carries the date she proved it and the score she proved it with. Mastered means ninety percent or better on the Unit Quiz with no hints from me — so a gold unit is evidence, not encouragement.",
    "This is the same nine units drawn as a path, so you can see the shape of her year at a glance: four behind her, decimals under her feet right now, four still ahead. Beside it, the same thing counted up, with the hours she has actually put in since September.",
    "Her trophy case. A Course Champion medal for finishing Basic Math, a badge for every unit she has mastered, and an effort medal she earned for coming back four days running when percents beat her. None of these are participation stickers — every one came from recorded work.",
    "And her courses. She finished Basic Math and moved up, and one subscription covers every course we teach, so she moves on when she is ready rather than when a term ends. Beside it, the strengths her placement check found on the very first day.",
    "If Monday is busy, this box is your whole week in four lines — mastered, streak, accuracy, problems done — and then where to help next. The records link underneath it is the one that matters at filing time.",
    "Here are the nine units, and every mastered one carries a date and a score. That pairing is what turns a checkbox into evidence, which is exactly what an end-of-year review or a portfolio asks you for.",
    "The same nine units as a path, so you can see the whole year at a glance and plan against it. Beside it, the hours — measured engaged time since September, not a timer left running, because in most states the hours are the part you have to be able to stand behind.",
    "The trophy case does a job in a homeschool that is easy to underrate: it is the part your child can show somebody. A medal for finishing a whole course, a badge for every unit mastered, and one for effort — earned the week percents nearly beat her.",
    "And her courses. One subscription covers all ten, so a child who is ahead in one subject and behind in another is not a billing problem — she moves on when she is ready. Beside it, what her placement check found on the very first day.",
    # 2026-08-10 (build ct): five teacher stops, four student stops, and the
    # student door's own second-person script. Identical to demo.html, APPENDED.
    "Three numbers first, and the third one is really a question. Six students, eighteen units mastered between them — and then the unit the class as a whole is struggling with. Here that's Unit 2, fractions, at a seventy-eight percent class average.",
    "This is the heatmap: every student down the side, every unit across the top, and the real score in each box. Read down a column and you find the wall — Unit 2, where Aiden and Ben both stopped. Read across a row and you get one student's whole story in a second.",
    "And this is my honest read on the class. Aiden isn't lazy — he's missing an idea underneath, he's treating a fraction as two separate whole numbers. Ben isn't stuck, he's stopped. And one you didn't ask about: Sofia is being under-served. She's ready for Algebra One now, and keeping her in step with the class is costing her a term.",
    "Strengthen next, one line per student, and every line names the broken rule rather than the wrong answer. Fixing an answer leaves the rule intact, and it fires again next week.",
    "And time on task — engaged time, not a tab left open. It is the fastest way to tell stuck apart from stopped, and those two need opposite responses from you.",
    "This is the part you can ask for any time: how am I doing, in plain words. It's written from your own work — what you're good at, what's hard right now, and what we're going to do about it.",
    "Your nine units drawn as a path, so you can see the whole year at once: four behind you, decimals right where you're standing, and four still ahead. Beside it, the same thing counted up, with every hour you've put in since September.",
    "And your next three sessions, already planned. Finish multiplying decimals, then dividing, then the Unit Five Quiz — ninety percent with no hints and Unit Five turns gold. And I won't offer you that quiz until you've got two right on your own first.",
    "Your courses. You finished Basic Math and moved up, and every course is included — so Algebra One opens the day you are ready for it, not when a term ends.",
    "These five numbers are yours: how many units you've mastered, how accurate you are, how many problems you've done, your time this week, and the day streak you're protecting. Every one of them comes from work you actually did.",
    "Below that is your whole course — all nine units. The gold ones you've mastered, and mastered means ninety percent or better on the Unit Quiz with no hints from me. Unit five is where you are right now, and the Final Exam stays locked until every unit is gold.",
    "Open a unit and you can see every quiz inside it — the score and the date. Your parents and your teacher see exactly this same page, because there is only one set of numbers and everybody gets the truth.",
    "Strengthen next is my short list for you: the specific things that went wrong in your lessons this week. Not a level, not a percentile — the two things I would fix first.",
    "And your trophy case. Explored, practiced, learning, mastered, the effort medal, and the Course Champion medal you earned for finishing Basic Math. Every one of them came from real work — none of them are participation stickers.",
    # 2026-08-10 (build ct): the two habit charts. Identical to demo.html, APPENDED.
    "Two charts here, and they are her habits. On the left, accuracy week by week — the dip is week eight, the week percents beat her, and the climb after it is four days of coming anyway. On the right, minutes a day this week, including the two days she did nothing. Honest pictures, both of them: a dashboard that only ever shows good news isn't worth having.",
    "These two charts are your habits. On the left, how accurate you were week by week — that dip is the week percents beat you, and the climb right after it is you coming back four days running. On the right, your minutes a day this week, days off included. I'd rather show you the truth than a flattering picture.",
    # 2026-08-12 (build eg): SEVEN parent-door lines -- the conference rewrite
    # (intro, stops 1/2/4/5/8, outro). Identical to demo.html, APPENDED.
    "Hello, and come on in — this is the parent's side of Mr. Cadabra's Classroom, shown with a made-up student named Maya so no real child's record is ever on display. Parents bring me the same two questions everywhere: is my child actually learning, and will she actually want to do this? Every panel on this screen answers one of those two — and every number on it comes from real work, because we never invent a good week.",
    "This is the dashboard you'd open at home, and it leads with the question you'd ask me at a parent-teacher conference: how is my child really doing? Not a score out of ten, not a percentile — an answer in plain English, written from the work she actually did.",
    "That's my honest read. It names what she's genuinely got, what she's stuck on, and what I'm doing about it — because I teach: out loud, one step at a time, and I never just hand her the answer. When this paragraph says she owns something, she earned it. And when she has a hard week, it says that too, plainly.",
    "These five numbers are the same five her teacher and I see — one record, one set of facts, nothing rounded up. And the day streak is my favorite of the five, because nobody can assign a streak: it only grows on days she opens the classroom herself, and a child protects a streak she built.",
    "Strengthen next tells you exactly where she's wobbling right now — specific enough to sit down with at the kitchen table. And a problem she misses doesn't just vanish into a percentage: a few days later I bring back a fresh one just like it, so a miss becomes a second chance instead of a quiet gap.",
    "Her trophy case — and this panel is my answer to the question 'will she actually use it?' The badges are earned, never given: a Course Champion medal for finishing Basic Math, a badge for every unit she's mastered, and an effort medal for coming back four days running the week percents beat her. This is why a child opens the classroom without being asked.",
    "And that's the parent's window. One more thing, because careful parents always ask: in a lesson your child talks with me out loud, her speech becomes text, and the audio is deleted right away — never stored — while I stay warmly on the math and nothing else. If you'd like to see how I actually teach, I can give you a real lesson right now, at any level from counting to calculus."
]


@app.get("/api/demo-audio/{idx}")
def demo_audio(idx: int, request: Request):
    """Serve one whitelisted demo line in the tutor's real voice (cached). 204 when the
    ElevenLabs key isn't configured -- the demo falls back to the browser voice."""
    _rate_limit("demoaudio:" + _client_ip(request), limit=60, window_seconds=300,
                what="demo audio requests")
    if idx < 0 or idx >= len(DEMO_VOICE_LINES):
        raise HTTPException(status_code=404, detail="Unknown demo line.")
    if not ELEVEN_API_KEY:
        return Response(status_code=204)
    return _tts_stream_response(DEMO_VOICE_LINES[idx], mode="demo")


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
    this endpoint spends real ElevenLabs money. 2026-08-07: voice input is LIVE on ALL
    THREE teaching pages (session + practice + topic; session got it 2026-08-06) -- the
    tap-to-talk button posts here for the typing courses on capable browsers; elementary
    tap-to-answer courses don't use it. TRANSCRIBE-AND-DELETE: the audio lives only in
    memory in this request, goes to ElevenLabs for transcription, and is discarded when
    the request ends -- never written to disk, never stored, only the text survives.
    """
    _require_student(code)
    _rate_limit("stt:" + code.strip(), limit=20, window_seconds=300, what="voice uploads")
    if not ELEVEN_API_KEY:
        return {"text": "", "error": "no_key"}
    try:
        # SECURITY (build ec, 2026-08-12 -- finding F5): read at most MAX_AUDIO_BYTES + 1
        # so a giant upload can't be pulled whole into memory. A few seconds of student
        # speech is well under a megabyte; the cap (default 12 MB, env-tunable) is roomy
        # for a long answer yet closes the memory/cost hole. Over the cap -> a clean 413.
        content = await audio.read(MAX_AUDIO_BYTES + 1)
        if len(content) > MAX_AUDIO_BYTES:
            raise HTTPException(status_code=413, detail=(
                "That recording is too large — try a shorter answer, "
                "or type it instead."))
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
    except HTTPException:
        # The 413 "too large" refusal (build ec) is a real answer -- it must reach the
        # caller, not be swallowed by the catch-all below that turns errors into "".
        raise
    except Exception as exc:  # noqa: BLE001
        print(f"[transcribe] error: {exc}")
        return {"text": ""}


# NOTE (2026-08-09, build bz): /api/demo-transcribe was removed when the demo dropped
# voice answering (Jim). It lived here, was IP rate limited, and used the same
# transcribe-and-delete path as /api/transcribe -- see git history if the demo ever
# speaks again. Nothing calls it today, and an unused endpoint that spends
# ElevenLabs money is a surface we do not need open.


# Serve the static folder (css/js/images if we add them) under /static.
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


# I did no harm and this file is not truncated.
