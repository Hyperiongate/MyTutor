# =============================================================================
# main.py  --  Math Tutor MVP  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
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


class CheckIn(BaseModel):
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
}


@app.get("/api/awards/{code}")
def awards_state(code: str):
    """The student's trophy case: course trophies, per-course merit-badge counts, and
    effort awards (persisted once earned). Honest {tracking:false} when the DB is off."""
    _student_or_404(code)
    code = code.strip()
    if not store.enabled():
        return {"tracking": False, "trophies": [], "badges": {}, "awards": []}

    trophies, badges = [], {}
    any_check = perfect = bounce = False
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
                                     "pathfinder": placed}[aid]))
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
def time_summary(code: str, days: int = 14):
    """Recent engaged time for the dashboard: per-day totals (newest first) with a
    per-course split. The CLIENT computes 'today' / 'this week' against the days
    it recorded, so the student's local calendar stays authoritative."""
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
    """A fresh, friendly student code (e.g. MAPLE42) that collides with nothing:
    not the pilot codes in students.json, not any existing account."""
    for _ in range(60):
        code = f"{secrets.choice(_CODE_WORDS)}{secrets.randbelow(90) + 10}"
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
def admin_email_test(key: str = "", to: str = ""):
    """Jim's email-pipe diagnostic (admin-key protected): sends ONE real test email
    and returns exactly what happened -- the precise SMTP failure text on error,
    and the active config WITHOUT the password. This is how we debug 'the email
    never arrived' without guessing."""
    _require_admin(key)
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
def admin_digest_test(key: str = "", email: str = "", to: str = ""):
    """Jim's weekly-email diagnostic (admin-key protected): builds a REAL parent's
    digest and returns it as JSON WITHOUT sending. Add &to=an@address to also send
    exactly one copy there for eyeballing. Never marks the parent as sent."""
    _require_admin(key)
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
def beta_list(key: str = ""):
    _require_db()
    _require_admin(key)
    return {"ok": True, "codes": store.list_beta_codes()}


@app.post("/api/beta/revoke")
def beta_revoke(body: BetaRevokeIn):
    _require_db()
    _require_admin(body.key)
    if not store.revoke_beta_code(body.code):
        raise HTTPException(status_code=404, detail="No pass with that code.")
    return {"ok": True, "codes": store.list_beta_codes()}


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
def admin_stats_api(key: str = ""):
    """The numbers behind /admin. Admin-key protected (constant-time compare)."""
    _require_db()
    _require_admin(key)
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
            description="All 8 math courses with Mr. Cadabra — placement to mastery, "
                        "warm voice, math keyboard, honest dashboards.").id
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
    key: str
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
def forum_moderate(body: ForumModIn):
    """Jim's moderation: soft-delete a post or reply. Needs FORUM_MOD_KEY (env)."""
    _require_db()
    mod_key = os.environ.get("FORUM_MOD_KEY", "").strip()
    if not mod_key or not hmac.compare_digest((body.key or "").strip(), mod_key):
        raise HTTPException(status_code=401, detail="Not authorized.")
    if body.kind not in ("post", "reply"):
        raise HTTPException(status_code=400, detail="kind must be 'post' or 'reply'.")
    if not store.delete_forum_item(body.kind, (body.item_id or "").strip()):
        raise HTTPException(status_code=404, detail="Nothing with that id.")
    return {"ok": True}


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


@app.get("/api/records/{code}")
def records_report(code: str, days: int = 90):
    """Everything the printable homeschool records report needs (2026-08-04), in one
    call: the full-range hours log, per-course unit progress (statuses, topic quizzes,
    Unit Quiz best, mastered at 90%), placement titles, and dated awards. Read-only;
    honest {tracking:false} when the DB is off."""
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
        return {"ok": True, "tracking": True, **res}
    except Exception as exc:  # noqa: BLE001
        print(f"[quiz] record_topic_quiz failed: {exc}")
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
APP_BUILD = "2026-08-05aj-hearhim-breathe"


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

    # OPENER: the app auto-sends "__open__" when the student opens the lesson (they did NOT
    # type anything). The OLD app sent a literal "Hi!" that got stored as a student turn, so
    # after a few logins the tutor saw "Hi Hi Hi..." and turned snappish. Fix: never store a
    # fake student greeting, strip any leftover junk ones, generate a warm recap, and save
    # ONLY the tutor's reply so the conversation stays coherent.
    if message in ("__open__", "__tour_done__"):
        after_tour = (message == "__tour_done__")
        junk = ("hi", "hi!", "hi.", "hello", "hey", "__open__", "__tour_done__")
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
        reply = _bold_first_terms(tutor.get_tutor_reply(student_context, history, opener_note, req.course, code=code), history)
        history.append({"role": "assistant", "content": reply})
        session["history"] = history
        save_session(code, session, req.course)
        return {"reply": reply}

    reply = _bold_first_terms(tutor.get_tutor_reply(student_context, history, message, req.course, code=code), history)

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

    reply = _bold_first_terms(tutor.get_practice_reply(student, req.problem, safe_history, message, req.course, code=req.code.strip()), req.history)

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
    reply = _bold_first_terms(tutor.get_topic_reply(student, req.topic, _sanitize_history(req.history), message, req.course, code=req.code.strip()), req.history)

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
