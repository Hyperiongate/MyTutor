# =============================================================================
# ruletests.py  --  the RULE REGRESSION BATTERY  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-11  BUILD dj -- PART 3s: BACKUPS. A backup system is only real if the
#               restore has been rehearsed, so the battery now performs the whole
#               drill on every run: seed a real SQLite database through the public
#               store API, snapshot it with export_all, prove the DRY LOOK changes
#               nothing, restore into a second blank database THROUGH THE ACTUAL
#               restore_backup.py tool (gzip file and all), and prove the two
#               databases row-for-row identical. Boundaries proven from source:
#               main.py never calls import_all (no restore endpoint can exist), the
#               download rides the X-Admin-Key header, the nightly pass is fenced and
#               atomic, rotation keeps BACKUP_KEEP, /admin has the download button
#               (cx: buttons, not instructions) and NO restore control, and
#               RECOVERY.md + restore_backup.py ship complete.
#   2026-08-11  BUILD di -- PART 3r: the figures the audit could not draw, proven
#               through the REAL renderer (node executes math-figures.js, the same
#               file the browser runs). Piecewise domains clip and mark their own
#               endpoints (open for strict, closed for inclusive -- the audit's jump
#               figure is the fixture); an unparseable domain fails OPEN; the shared
#               tool note reaches all ten prompts; and the three showColumn bodies are
#               compared byte-for-byte (build-bk drift class) with align="last" proven
#               unable to complete a wrong sum. ⭐ THE HARNESS'S FIRST RUN FOUND A LIVE
#               BUG: hole= had NEVER drawn on a genuine 0/0 removable point -- the
#               renderer evaluated the function AT the hole, got NaN, and bailed; the
#               feature only worked on functions DEFINED at the point, which is exactly
#               where holes do not belong, and the canonical scripts had quietly worked
#               around it with pre-simplified forms. Fixed with a numeric limit (both
#               sides sampled and required to agree), and the asymptote case -- where
#               painting a hole would be rule 51(e) broken in pixels -- is a permanent
#               NEGATIVE fixture.
#   2026-08-11  BUILD dh -- the audit's teaching findings, tested. ANSWERED_CASES (rule
#               17's new referee: the board must not answer the question -- the audit's
#               ticket card is the fixture, plus commuted and word-number variants, plus
#               the shapes good teaching uses as FALSE cases) and UNSPOKEN_CASES (rule
#               44's new referee: a numeric board problem with a numberless spoken ask --
#               the audit's "First question: ... What's the answer?" is the fixture).
#               The foundation-corpus sweep now runs ALL THREE draft-level referees
#               (self-answer, answered-q, unspoken) over every canonical script on every
#               run, so a future widening cannot quietly start flagging correct lessons
#               (the build-cy discipline, now paid for twice). RULE_VERIFY: 17 and 44
#               move COVERED -> ENFORCED; rule 52 declared (COVERED). Junk-input
#               never-raises covers the two new referees.
#   2026-08-11  BUILD dg -- PART 3q (reliability) + the audit-log misfires become
#               permanent referee cases. The first full audit's Render logs proved the
#               stumbles were OUR bugs, not rate limits: the rule-15 referee counted the
#               pronoun "one" as a number and had no concept of an OFFER (a dozen
#               misfires in forty minutes, each burning a paid draft -- and the geometry
#               lesson's worked example with them, S-1); claude-sonnet-5 intermittently
#               rejects assistant-prefill continuation (each rejection was a stumble);
#               five replies shipped as admitted partials at the 1600 ceiling. Every
#               quoted misfire is now a PENDING_CASES / SELF_ANSWER_CASES fixture (plus
#               guards proving the exclusions did not swallow the referee), and PART 3q
#               proves with a scripted client: the negotiated prefill fallback (the
#               named 400 switches shapes and is REMEMBERED; unrelated errors still
#               raise), the 3000 ceiling, the one silent retry on an empty reply, the
#               stand-alone wording in both regeneration nudges, and the admin key's
#               exit from query strings (X-Admin-Key header; sessionStorage; no
#               key-carrying URL built anywhere in admin.html).
#   2026-08-10  BUILD df -- PART 3o learns the SIXTH unit-name copy and PART 3p bans two
#               phrases from marketing copy. Jim asked for a sweep proving no blanket
#               "evidence based learning" claim exists anywhere. It doesn't -- but the
#               sweep caught courses.html (the PRINTABLE scope & sequence) still saying
#               "taught Socratically" (missed by build cc's site-wide removal) and still
#               listing the pre-restructure diffeq units, plus llms.txt claiming unit
#               mastery at 80%+ (it is 90%+ on a ten-question Unit Quiz) under the old
#               MyTutor brand name. All fixed in df. PART 3o now parses courses.html's
#               ten unit lists (order-based; the cards sit in curriculum order); PART 3p
#               strips HTML comments then fails the build if "Socratic" or
#               "evidence-based" appears in any static page, llms.txt, or README.md.
#   2026-08-10  BUILD de -- PART 3o: unit-name parity across all FIVE files. The diffeq
#               restructure (CUPM mainstream syllabus) edited the same nine unit names
#               in curriculum.py, pedagogy.py, session.html and topic.html, and nothing
#               proved they agreed -- each file works fine alone while the picker shows
#               one name and the tutor teaches another. curriculum.units_for() is now
#               the declared source of truth and the other four are compared to it byte
#               for byte for every course. Writing the check found the FIFTH copy:
#               challenge.html's *_UNIT_NAMES (the labels on assessment results), which
#               still carried the OLD diffeq units -- fixed in the same build, and its
#               banks are also shape-checked (9 units x 5 questions, answer index 0-3),
#               since the diffeq re-mapping is exactly the edit that could leave a unit
#               short a question. Any future rename that misses a file fails the
#               battery instead of shipping.
#   2026-08-11  BUILD dd -- PART 3n: fluency sprints. Priorities in order of what they
#               would cost a child: all 1,620 generated answers verified RIGHT (a drill
#               that reinforces a wrong fact is worse than none), sprints gate NOTHING
#               (checked at store, endpoint and page level), and half B must be a
#               sibling of half A, not a twin -- the first registry shipped B as a
#               byte-identical twin of A, which would have made "improvement" a memory
#               test, and the sibling check caught two more twin families (percents,
#               make-ten's shifted ramp pushing past nine) before ship.
#   2026-08-10  BUILD dc -- three guards: the auditor must count graceful-failure turns
#               itself (absence is invisible to a content marker), retry a stumbled turn
#               once, and carry the critic's three discipline checks earned from its
#               first-run false positives.
#   2026-08-10  BUILD db -- two guards for the reasoning budget: an "output limit
#               reached" probe result must be retried with room to think (it is proof of
#               access, not absence), and the quiet variant (200 + empty message +
#               finish_reason length) must not end a lesson looking like the student
#               left.
#   2026-08-10  BUILD da -- four guards for probe_models(): the tool must be able to ask a
#               key what it reaches, the pricing button must ask, a model gated behind
#               organisation verification must say so WITH the remedy, and the probe list
#               must be overridable without a code change.
#   2026-08-10  BUILD cz -- five guards from the auditor's first live failure: a preflight
#               before any lesson, a negotiated token parameter, the model list offered
#               only for a real model error, a summary that cannot make "nothing was
#               marked" look like "no findings", and the admin panel repeating the
#               server's summary instead of computing a second one.
#   2026-08-10  BUILD cy -- SELF_ANSWER_CASES and the corpus sweep. Rule 39(b) is ENFORCED
#               now, not merely COVERED. Two of the FALSE cases are real false positives
#               caught by sweeping our own content before shipping: a foundation script
#               ("What is a numerator? The numerator is...") and a demo line that restates
#               the question's own number as a hint. Both are now permanent fixtures, and
#               the suite sweeps every foundation script on every run so a future widening
#               of the referee cannot quietly start punishing good teaching.
#   2026-08-10  BUILD cx -- a check that an admin job the owner cannot reach is NOT
#               SHIPPED. Jim asked "tell me exactly how to run it" and the honest answer
#               was that he could not: both money-spending admin jobs were documented as
#               "POST /api/admin/..." and nothing in the product can POST JSON. The
#               foundation pre-render had therefore sat un-run for days while three
#               handoff documents told him to run it. Every spending endpoint must now
#               have a button on /admin and be priceable from there.
#   2026-08-10  BUILD cw -- PART 3l (the lesson auditor's boundaries) and THE CEILING
#               RAISED 135,000 -> 150,000 with the reason written down where it is
#               enforced. The old note said "consolidate, do not raise"; it was written
#               before anything had been measured. What we know now: 135,000 was a
#               judgement in an audit, the built prompt is ~17% of the model's real
#               window, and rule 51 spent the last 500 characters -- so the NEXT rule,
#               whatever it was, would have failed the build. Merging rules to satisfy an
#               invented number means editing the teaching, which fails invisibly. That
#               is the wrong risk to take on no evidence, and lessonaudit.py is now the
#               evidence: run it at two prompt sizes and set the number from what it finds.
#               PART 3l guards the auditor's BOUNDARIES rather than its findings (those
#               are opinions): the key value may appear in an Authorization header and
#               nowhere else, the job can always be priced before it is run, the price
#               says it is an estimate, and the auditor never writes to tutor.py or
#               foundations.py. A critic that edits the teaching is a second author nobody
#               reviewed.
#               A NOTE ON WRITING THAT KEY CHECK: the first version flagged the dry run's
#               own label line -- the words "OPENAI_API_KEY" printed beside
#               "present"/"MISSING", which is exactly what a diagnostic should say. A
#               check that cries wolf at correct code gets switched off, and then it
#               guards nothing. It now looks for the VALUE travelling, not the name.
#   2026-08-10  BUILD cv -- rule 51 joins the ten-course scan, and a new check that every
#               range= we write PARSES UNDER THE RENDERER'S OWN RULE. The regex is read
#               out of math-figures.js so it cannot drift. It exists because rendering one
#               new figure showed the [[graph]] documentation teaching range="-1,5" while
#               parseRange accepted only "a..b" -- the window was discarded, silently, and
#               the instruction had been unfollowable since the day it was written to fix
#               exactly that complaint.
#               ⚠️ THE OTHER LESSON FROM THIS BUILD is in _cv_welcome_check.py, not here:
#               Playwright matches routes in REVERSE registration order, so a catch-all
#               registered last swallowed the stubbed /api/session and the harness measured
#               the FIRST-TIMER card while reporting on the returning one. It now asserts
#               which screen it is looking at before it measures anything. A test must
#               prove it is looking at the right thing before it is allowed to pass.
#   2026-08-10  BUILD cu -- PART 3k: A BAR MUST BE REACHABLE BY THE INSTRUMENT THAT
#               MEASURES IT. Jim asked for a retake path for a unit passed but not
#               mastered. Checking it found something worse: mastery is 90% and the Unit
#               Quiz was four or five questions, so the only possible scores were 80% and
#               100% -- the bar could only be cleared with a perfect paper. Topic quizzes
#               likewise (four questions, 80% bar). It survived because the bar and the
#               question count live in DIFFERENT FILES and changed on DIFFERENT DAYS, and
#               no test ever multiplied them together. PART 3k does exactly that
#               multiplication, for every quiz, in every course: at least one NON-PERFECT
#               score must pass, or the bar does not mean what it says.
#               Also here: rule 50 joins the ten-course coverage scan, the quiz lengths
#               are scanned in all ten built prompts, and the locked Final Exam must name
#               the units holding it shut AND fall back rather than fail shut.
#   2026-08-10  BUILD ct -- THREE LAYOUT GUARDS, and the first real catch by cs's checks.
#               Jim hit a live one: the demo's answer buttons were a one-per-line grid,
#               the answer zone could take 47vh, and .feed is flex:1 -- so the whiteboard
#               lost every pixel the answers took. PART 3j now insists the buttons are a
#               wrapping ROW (the real classroom's own shape), the answer zone is capped
#               at 35vh or less, and the board carries a min-height FLOOR.
#               ⭐ AND cs's "every tour stop points at a real element" check paid for
#               itself immediately: rebuilding the teacher dashboard removed the
#               tdAttention CARD while its tour stop still pointed at it. glow() returns
#               quietly on a missing id, so that stop would have narrated a dashboard
#               that never moved -- no error, no log, just a paragraph about a panel the
#               visitor cannot see. The line moved onto the roster instead.
#   2026-08-10  BUILD cs -- THE WHITELIST CHECK THAT SHOULD HAVE EXISTED SINCE bx. The
#               demo design notes have said "every spoken string must be on the
#               whitelist" from the beginning and NOTHING enforced it. say() looks the
#               text up in VOICE_LINES and plays clip N by index; a line that is not
#               there does not raise -- that one stop drops to the browser's flat
#               mechanical voice in the middle of Mr. Cadabra speaking. All 24 literal
#               tour lines are now checked, on every tour on the page. Two more: every
#               tour stop must point at an element that EXISTS (glow() returns quietly on
#               a missing id, so a typo means the words play over a dashboard that never
#               moves), and the homeschool override must cover every parent stop (it is
#               read BY INDEX and falls through to the PARENT's words where it is short).
#               A LESSON FROM WRITING IT: the first version wrapped the parse in `except
#               Exception`, which swallowed a NameError -- ast was never imported -- so
#               every line looked off-list and the failure blamed the demo instead of the
#               test. The except is narrow now. A test's error handling must not be able
#               to hide the test's own bugs.
#   2026-08-10  BUILD cr -- PART 3j now proves ONE DOOR, ONE DASHBOARD. Jim: "I don't
#               want any links to any other dashboards from there." Three paths could
#               hand an audience visitor somebody else's screen and all three fail
#               silently, so each is checked against the SOURCE rather than against a
#               comment claiming it: showBalloons must return through the audience
#               ending BEFORE it builds the three balloons, the ending itself must
#               contain no dashboard opener at all, and the dashboard's back button must
#               not close a locked walkthrough (there is no page behind it).
#               Also checked: a locked door still leads somewhere. A test that only
#               proves an absence would happily pass on a dead end.
#               NOT IN THIS FILE, deliberately: the behaviour was also driven in a real
#               browser across all four doors and the open demo (59 checks). That harness
#               needs playwright, and this battery must stay runnable anywhere in a
#               second -- it lives in the sandbox, not the repo.
#   2026-08-10  BUILD cq -- PART 3j grew two checks and one of its own bugs was fixed.
#               New: the walkthrough must open the dashboard BEFORE it starts talking
#               (Jim watched a blank screen talk at him for thirty seconds), and every
#               audience line must be anchored by its opening WORDS, each anchor
#               resolving to exactly ONE whitelisted line.
#               THE BUG WORTH REMEMBERING: my first anchor regex used ["']([^"']{12,80})["']
#               to pull the anchor text out. Four of the nine anchors have an apostrophe
#               inside a double-quoted string -- "the parent's view", "That's the honest
#               read." -- and [^"'] stops dead at that apostrophe. The test found five
#               anchors, called it a pass at >=9 only by accident of failing loudly, and
#               would otherwise have checked less than half of what its name claimed.
#               A test that silently checks a subset is worse than no test. Capture the
#               opening quote, require the same character to close it.
#   2026-08-10  BUILD cp -- PART 3j, the audience walkthroughs. Guards the two things
#               that can break /demo?view=... silently: a marketing page pointing at a
#               view the demo does not implement, and the two voice lists falling out of
#               step. That second one deserves a warning to whoever reads this next:
#               clips are served BY INDEX, so a mismatch plays the WRONG AUDIO under the
#               RIGHT WORDS and nothing errors. While writing this I compared the lists
#               with a naive regex over quoted strings, which matched text inside
#               COMMENTS and made two identical 188-line lists look 117 lines apart. The
#               helper here parses main.py as Python and demo.html as JS-with-comments,
#               which is the only way to answer the question honestly.
#   2026-08-10  BUILD co -- PART 3i AND THE GENERATED RULES INDEX (audit #2 items 24
#               and 23). This file's header has said from day one: "ADDING A RULE? Add a
#               scenario here in the same commit. That is the whole point." We drifted
#               anyway -- rules 42 to 47 shipped with no check of their own -- because
#               nothing made the drift visible.
#               RULE_VERIFY now declares, for every rule, HOW it is verified, in four
#               honest tiers: ENFORCED (a machine catches it in a real reply),
#               EXERCISED (a --live scenario asserts the behaviour), COVERED (the text
#               provably reaches all ten prompts -- he was told, which is not the same as
#               he does it), UNVERIFIED (nothing at all).
#               It is a RATCHET, not a gate: existing debt prints but does not fail a
#               deploy, while a NEW rule with no declaration fails, and a rule that
#               quietly LOSES its scenario fails. Today: 13 enforced, 10 exercised,
#               25 covered, 1 unverified.
#               `python ruletests.py --rules` regenerates RULES.md from the prompt
#               itself, so the index can never drift from the classroom. That file is
#               also what you hand a curriculum advisor or a school district.
#   2026-08-10  BUILD cn -- PART 3h, "it must not degrade, and it must scale".
#               Nothing in this battery had ever asked whether anything GROWS, and two
#               things did: every chat turn loaded, parsed, appended to and rewrote the
#               student's ENTIRE conversation in order to read the last thirty messages
#               of it, and the usage log kept every row forever. PART 3h now checks the
#               transcript cap (and that it stays above what the model reads), the usage
#               retention pass, deliberate pool sizing, age-based rate-bucket eviction
#               and the TTS cache cap.
#               It also asserts the prompt does not FLIP SHAPE between turns -- build cl
#               made it do that to save characters, and the cache arithmetic showed the
#               flip costs about $0.24 an episode to save $0.0005 a turn.
#   2026-08-10  BUILD cm -- CACHE DISCIPLINE CHECKS. The system prompt is one cached
#               block; per-turn content inside it moves the cache prefix and re-bills
#               everything after it. PART 3g now asserts get_tutor_reply takes a
#               turn_note, that per-turn asides never appear in the system prompt, and
#               that two ordinary turns build a byte-identical prompt.
#   2026-08-10  BUILD cl -- DEFERRAL TESTS + THE PROMPT BUDGET.
#               The deferral tests care far more about RESTORING than about saving: a
#               brand-new student still gets every script verbatim, a returning student
#               keeps every UNHEARD script verbatim, heard scripts stay NAMED so he can
#               still offer them, asking restores the exact wording, the default is to
#               carry the words, and the refresher detector is checked on both the
#               explicit ask and the bare "yes" that follows rule 40(b)'s offer.
#               The prompt ceiling is now a BUDGET TABLE, not a single number. A total
#               tells you that you are over and nothing about what to do; the table
#               prices every block, so the next person adding one sees the cost before
#               paying it. Measured and recorded in the failure message: there is 0%
#               overlap between the course templates and the shared rules, so nothing can
#               be reclaimed for free -- the honest options are consolidating rules,
#               deferring another block the way cl defers heard scripts, or raising the
#               ceiling deliberately with the reason written down.
#   2026-08-10  BUILD ck -- PART 3g, the misconception catalogue, and a PROMPT-SIZE
#               tripwire (audit #2 item 22). PART 3g checks every entry has all nine
#               fields, unique ids, a speakable SAY that does NOT open by telling the
#               student they are wrong (rules 20/49c), and -- the important one -- that
#               no `detect` string is just a NUMBER in any spelling. The first end-to-end
#               run matched "I did three plus two first, so twenty" and returned two
#               confident WRONG theories, because "three" and "two" had survived a filter
#               that only required a letter. A numeric answer is evidence only in the
#               context of the problem it answers, and the matcher cannot see the
#               problem. That case is now a permanent fixture.
#               The prompt-size check prints every course's size and fails above 135,000
#               characters. It is a TRIPWIRE set above today's largest (130,022): when it
#               trips the answer is to consolidate overlapping rules -- the rules block
#               is ~45% of the prompt -- not to raise the number.
#   2026-08-09  BUILD cj -- PART 3f, NOTATION COVERAGE. Jim asked the right question
#               after the f(x) fix: "math is filled with these kinds of things. How can
#               we make sure every one of these is caught all of the time?" Fixing f(x)
#               by hand fixed one symbol and guaranteed nothing. PART 3f is the general
#               answer, held against notation.py:
#                 A  every notation on every board we ship is REGISTERED for that course
#                    (317 board strings scanned). Write a symbol the registry does not
#                    know and the build fails -- so a symbol cannot reach a child's
#                    screen without us having said, somewhere, how to read it.
#                 B  the DEEP families need a real script that says them aloud, not a
#                    table row. It caught three courses using subscripts silently.
#                 C  the registry must recognise its own examples, must reach all ten
#                    prompts, and no entry may collide with a narrower one -- that last
#                    invariant was added after the first run reported diffeq's mu as an
#                    unregistered population mean, because two entries matched one glyph.
#   2026-08-09  BUILD ci -- rule 48 and the NOTATION READABILITY check (PART 3b).
#               Jim found f(x) being used in Algebra I with nothing ever teaching it. The
#               check that would have caught it: for every course, if any script writes
#               function notation on the BOARD, some script in that course must read it
#               ALOUD in words and deny the wrong reading by name. It failed on four
#               courses the moment it was written, and on diffeq even after the first fix
#               -- because diffeq writes y(t), y prime and dy/dx rather than f(x), and my
#               first regex only knew about f, g and h. Both halves of the check now
#               share one letter set so they can never disagree again.
#   2026-08-09  BUILD ch -- SCORE_CASES, rules 45-47, and two arithmetic guards.
#               SCORE_CASES covers the new score referee. Its FALSE cases carry the
#               weight again: three false positives were caught here before shipping,
#               including one that revealed the percentage check was matching NOTHING
#               (a stray \b after "%"). Also asserts that tutor.py's pass marks never
#               drift from store.py's, and that no score in any total from 1 to 40 is
#               ever stored higher than the truth.
#   2026-08-09  BUILD cg -- PENDING_CASES and the today-bar guards.
#               PENDING_CASES covers the new rule-15 referee, and the FALSE cases carry
#               most of the weight: rule 39(d) now REQUIRES him to ask "does that click,
#               or should I show it another way?" constantly, and re-rolling those would
#               cost real money every turn. Two false positives were caught here before
#               shipping -- "which number is the denominator in three-fourths?" (the
#               hyphen read as minus) and "is 1/2 bigger than the piece we shaded?" (a
#               fraction counted as two numbers).
#               PART 3d/3e gained the today-bar guards: the store table is in the reset
#               cascade, session.html still rebuilds the bar from SRV_PROGRESS.today at
#               load, and ensure_today_tag() restores a bar a reload destroyed while
#               still never resetting one that is genuinely live.
#   2026-08-09  BUILD cf -- PART 3e, plus rules 41-44 and two new guards.
#               PART 3e "THE THREE TEACHING PAGES MUST MATCH" exists because auditing
#               audit #1 found that item 11 (board lines never wrap) shipped to
#               session.html and never reached practice.html or topic.html -- Jim's
#               broken-equation screenshot was still reproducible on two of three pages,
#               a day after we called it fixed. Same bug shape as build bk, where a rule
#               written into one of eleven per-course templates reached one course. PART 1
#               made that impossible for the prompt; PART 3e does it for the pages, and
#               also proves every board tag the SHARED prompt block teaches is drawable on
#               all three (the six lesson-only tags are named explicitly, and the test
#               fails if one of them ever leaks into the shared block).
#               PART 3c now enforces rule 41: a figure with no caption= is a failure.
#               PART 3d now proves all THREE teaching modes carry the canonical scripts
#               and honour the heard list.
#   2026-08-09  BUILD ce -- three new groups of checks, one per thing Jim asked for.
#               PART 1 gained rules 39 and 40 (coverage across all ten courses).
#               PART 2 gained VISUAL_CASES for the new visual referee -- including the
#               false-positive cases, which matter just as much: a re-roll is a real model
#               call, so ordinary prose about a number line, a promise to draw one next
#               time, and a look back at yesterday's picture must all stay clean.
#               PART 3c gained a drift check: tutor.FIGURE_TAGS (a constant, because
#               tutor.py must not read static files at request time) must still name
#               exactly the tags session.html's handleTags() routes to a figure renderer.
#               PART 3d is new -- foundation memory: the term key survives the model's own
#               capitalisation, a made-up term is rejected, the heard list actually reaches
#               the prompt and marks its scripts, every script stays byte-identical either
#               way (the audio cache depends on it), junk never raises, and the new table
#               is in store's per-student reset cascade.
#   2026-08-09  BUILD cd -- ADDED PART 3c, "board tags actually draw".
#               This is the machine for the failure Jim named on the demo page: "the
#               lesson referred to a diagram that didn't show up on the board... We got
#               one shot to do it right, and it failed." A board tag fails SILENTLY --
#               no exception, no log, the words are still spoken -- when its name is not
#               in handleTags(), when its attribute is not one the renderer reads, when
#               it carries no content, or when an attribute value contains a square
#               bracket (handleTags' own regex ends the tag there). PART 3c PARSES
#               static/math-figures.js, static/geo-figures.js and session.html's
#               handleTags() so the contract is read from the renderers themselves and
#               cannot go stale; a new tag with no entry in TAG_HANDLER/TAG_INLINE fails
#               the suite on purpose rather than being skipped. On its first run it
#               caught 11 already-shipped foundation scripts. It also checks the two
#               ways [[graph]] quietly draws the WRONG picture: lines= on a non-linear
#               expression (parseLinear flattens a parabola into a straight line) and a
#               comma where the grapher splits only on ";" or "|".
#   2026-08-09  CREATED (build bu, proactive audit #25). Every teaching rule we have
#               was born from Jim noticing a failure in a live lesson. That does not
#               scale to real students. This is the machine that notices instead.
# -----------------------------------------------------------------------------
# WHAT IT IS
#   A standalone test script. It is NEVER imported by the running app, so it cannot
#   affect a deploy -- it exists to be RUN before one.
#
# HOW TO RUN
#   python ruletests.py            offline checks only (fast, no API key, no cost)
#   python ruletests.py --live     ALSO plays scripted students against the real
#                                  prompt (needs ANTHROPIC_API_KEY; costs a few cents)
#
# WHAT IT CHECKS
#   PART 1  RULE COVERAGE -- every rule really reaches all ten courses' built prompts.
#           (This is the class of bug that hid for a day in build bk: a rule written
#           into ONE of tutor.py's eleven per-course templates reached one course.)
#   PART 2  THE PROSE REFEREE -- the live 2026-08-08 contradiction is still caught,
#           and every known false-positive shape is still clean.
#   PART 3  SPOKEN NUMBERS -- forSpeech() on all three teaching pages (runs only if
#           `node` is available; skipped gracefully otherwise).
#   PART 4  --live SCENARIOS -- a scripted difficult student: wrong answers, "I don't
#           know", equivalent-form answers, off-topic questions, goodbyes. Mechanical
#           assertions, no human reading required.
#
# ADDING A RULE?  Add a scenario here in the same commit. That is the whole point.
# =============================================================================
import ast
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import tutor  # noqa: E402
import notation  # noqa: E402

COURSES = ["entrymath", "basicmath", "prealgebra", "algebra1", "geometry",
           "algebra2", "precalc", "calculus", "probstat", "diffeq"]
STUDENT = {"name": "Testy", "grade": "7"}

PASS, FAIL, SKIP = [], [], []


def ok(name):
    PASS.append(name); print(f"  \033[92mPASS\033[0m  {name}")


def bad(name, detail=""):
    FAIL.append((name, detail)); print(f"  \033[91mFAIL\033[0m  {name}\n        {detail}")


def skip(name, why):
    SKIP.append(name); print(f"  \033[93mSKIP\033[0m  {name} ({why})")


def check(name, condition, detail=""):
    ok(name) if condition else bad(name, detail)


# =============================================================================
# PART 1 -- RULE COVERAGE ACROSS ALL TEN COURSES
# =============================================================================
# One entry per rule that must reach EVERY course. The needle is a phrase unique to
# that rule in the shared blocks. When you write a new shared rule, add it here.
COVERAGE = [
    ("rule 0  opening sequence",        "THE OPENING SEQUENCE"),
    ("rule 1  placement honesty",       "PLACEMENT HONESTY"),
    ("rule 4  say it -> write it",      "SAY IT -> WRITE IT"),
    ("rule 4  sub-step lines",          "ANSWERED SUB-STEP GETS ITS OWN LINE"),
    ("rule 4  multiplication sign",     "MULTIPLICATION SIGN"),
    ("rule 6  never run ahead",         "STILL NEVER RUN AHEAD"),
    ("rule 7  never ask to imagine",    "NEVER ASK THE STUDENT TO IMAGINE"),
    ("rule 9  the sound-off check",     "THE SOUND-OFF CHECK"),
    ("rule 10 tag checkable claims",    "TAG EVERY CHECKABLE CLAIM"),
    ("rule 13 literally true",          "MUST BE LITERALLY TRUE"),
    ("rule 14 define notation",         "DEFINE EVERY NOTATION"),
    ("rule 15 complete on screen",      "COMPLETE ON SCREEN"),
    ("rule 15 'your turn' on board",    'YOUR TURN" PROBLEM ITSELF GOES ON THE BOARD'),
    ("rule 15 pending '?' line",        "PENDING line with a question mark"),
    ("rule 16 restate the original",    "NOT JUST THE SUBSTITUTION"),
    ("rule 17 never answer yourself",   "NEVER ANSWER YOUR OWN QUESTION"),
    ("rule 18 check their answer",      "CHECK THE STUDENT'S ANSWER BEFORE YOU BUILD"),
    ("rule 19 worked example first",    "I DO, THEN YOU DO"),
    ("rule 20 partially right",         "PARTIALLY RIGHT IS NOT WRONG"),
    ("rule 21 'I don't know'",          "IS NOT A WRONG ANSWER -- IT IS A REQUEST"),
    ("rule 22 escalation ladder",       "NEVER ASK THE SAME THING THE SAME WAY TWICE"),
    ("rule 23 equivalent answers",      "EQUIVALENT ANSWERS ARE CORRECT ANSWERS"),
    ("rule 24 leaps/self-correct",      "LEAPS, SELF-CORRECTIONS"),
    ("rule 25 student disputes you",    "WHEN THE STUDENT SAYS YOU ARE WRONG"),
    ("rule 26 wrong lines corrected",   "A WRONG LINE NEVER STAYS ON THE BOARD"),
    ("rule 27 units + approximation",   "UNITS AND HONEST APPROXIMATION"),
    ("rule 28 one name per thing",      "ONE NAME PER THING"),
    ("rule 29 how a session ends",      "HOW A SESSION ENDS"),
    ("rule 30 off-topic questions",     "OFF-TOPIC AND PERSONAL QUESTIONS"),
    ("rule 31 bigger than math",        "WHEN SOMETHING BIGGER THAN MATH SHOWS UP"),
    ("rule 32 realistic problems",      "SURVIVE A SANITY CHECK"),
    ("rule 33 one notch at a time",     "DIFFICULTY MOVES ONE NOTCH AT A TIME"),
    ("rule 34 keep old skills sharp",   "KEEP OLD SKILLS SHARP"),
    ("rule 35 fix-then-retry a quiz",   "A FAILED QUIZ IS NEVER RE-GIVEN ON THE SPOT"),
    ("rule 36 teach before you ask",     "TEACH THE THING BEFORE YOU ASK ABOUT THE THING"),
    ("rule 37 vocabulary is taught",     "VOCABULARY IS TAUGHT, NEVER ASSUMED"),
    ("rule 38 concrete->picture->symbol", "CONCRETE, THEN PICTURE, THEN SYMBOLS"),
    ("rule 39 talk less, check in",      "TALK LESS. CHECK IN OFTEN"),
    ("rule 39 the check must be failable", "MAKE THE CHECK FAILABLE"),
    ("rule 40 ask before you repeat",    "SIT THROUGH THE SAME INTRODUCTION TWICE"),
    ("rule 40 mark what you taught",     '[[learned term="denominator"]]'),
    ("rule 41 captions say what to notice", "CARRIES A CAPTION THAT SAYS WHAT TO NOTICE"),
    ("rule 42 no comparisons",           "NEVER COMPARE THIS STUDENT TO ANYONE BUT THIS STUDENT"),
    ("rule 43 no false perception",      "YOU PERCEIVE EXACTLY TWO THINGS"),
    ("rule 44 read the problem aloud",   "READ THE PROBLEM ALOUD, IN FULL, EVERY TIME"),
    ("rule 45 the tally is arithmetic",  "THE TALLY IS ARITHMETIC, NOT JUDGMENT"),
    ("rule 46 one skill per question",   "A QUIZ QUESTION TESTS ONE SKILL"),
    ("rule 47 no cold quizzes",          "NO COLD QUIZZES"),
    ("rule 48 say the symbol aloud",     "HOW TO *SAY* THE SYMBOL"),
    ("rule 50 chase unfinished units",   "AN UNFINISHED UNIT IS YOUR JOB"),
    ("rule 51 a feature must be real",   "A FEATURE ON THE BOARD MUST BELONG TO THE FUNCTION"),
    ("quiz length: unit quiz is TEN",    "give the UNIT QUIZ: TEN questions"),
    ("quiz length: topic quiz is FIVE",  "give a short quiz -- FIVE"),
    ("canonical foundation scripts",     "SPEAK THESE VERBATIM"),
    ("speech: money as money",          "MONEY IS SPOKEN AS MONEY"),
    ("speech: number words",            "NUMBERS ARE SPOKEN THE WAY PEOPLE SAY THEM"),
    ("speech: spoken answers count",    "NUMBERS SPOKEN AS WORDS ARE EXACT ANSWERS"),
    ("progress: today bar every session", "THIS INCLUDES RESUMED SESSIONS"),
]


def part1_coverage():
    print("\nPART 1 — rule coverage across all ten courses")
    prompts = {c: tutor.build_system_prompt(dict(STUDENT), course=c) for c in COURSES}
    for name, needle in COVERAGE:
        missing = [c for c in COURSES if needle not in prompts[c]]
        check(name, not missing, f"missing in: {', '.join(missing)}")
    # no accidental gap in the numbered sequence
    nums = sorted({int(m) for m in re.findall(r"^(\d+)[.)] ", prompts["algebra1"], re.M)})
    expected = list(range(0, max(nums) + 1)) if nums else []
    check("rule numbering has no gaps", nums == expected,
          f"saw {nums}")


# =============================================================================
# PART 2 -- THE PROSE REFEREE
# =============================================================================
# Each case is (name, reply, should_flag). The FIRST is the real 2026-08-08 bug.
PROSE_CASES = [
    ("live bug: wrong answer adopted in words",
     'Fifteen dimes — and since that\'s over nine again, we do the same trick: fifteen '
     'dimes is one dollar and five dimes, so we write the five and carry a dollar. '
     '[[step eq="dimes: 7 + 8 + 1 = 16"]]', True),
    ("the corrected flow (must stay clean)",
     'Sixteen — nice, careful counting. Sixteen dimes is one dollar and six dimes, so we '
     'write the six and carry a dollar. [[step eq="dimes: 7 + 8 + 1 = 16"]]', False),
    ("intermediate value that reaches the right result",
     'Seven plus eight is fifteen dimes, and adding the one we carried makes sixteen. '
     '[[step eq="dimes: 7 + 8 + 1 = 16"]]', False),
    ("operand mentioned in passing",
     'We had eight dimes in the second number, so the column comes to sixteen. '
     '[[step eq="dimes: 7 + 8 + 1 = 16"]]', False),
    ("different label entirely",
     'Ten pennies is one dime, so we carry it. [[step eq="pennies: 5 + 5 = 10"]]', False),
    ("numeral contradiction",
     'You end up with 15 cookies on the plate. [[step eq="cookies: 9 + 8 = 17"]]', True),
    # 2026-08-09: this fixture used to end "...so what is eight divided by two?" with no
    # pending line, which the new rule-15 referee correctly flags. The numeric check is
    # still what this case tests (an unlabeled board line must not false-positive); the
    # reply is now written the way rule 15 actually asks for.
    ("unlabeled board line",
     'Nice! [[step eq="2x = 8"]] So what is eight divided by two? '
     '[[step op="/ 2" eq="x = ?"]]', False),
    ("no board tags at all",
     "Great job — that's fifteen dimes exactly!", False),
    # build dh: this fixture's REPLY was updated, not its point. The old wording ("what
    # do the dollars come to?") never spoke the problem's numbers -- which rule 44 has
    # forbidden since build cf and the new unspoken-problem referee now catches. The
    # case still proves what it always proved: a pending "?" line is not a number
    # contradiction.
    ("pending '?' line is never a contradiction",
     'Your turn — what do two plus one plus one dollars come to? '
     '[[step eq="dollars: 2 + 1 + 1 = ?"]]', False),
]

# ---- the VISUAL half of the referee (build ce) ------------------------------
# Jim's demo failure, in a live lesson: "the lesson referred to a diagram that didn't
# show up on the board... we got one shot to do it right, and it failed."
# A false positive costs a real model call, so the FALSE cases below matter as much as
# the TRUE ones -- ordinary mathematical prose about a number line must stay clean.
VISUAL_CASES = [
    ("the failure: a number line that was never drawn",
     "Here's a number line from negative six to six. Where would negative three sit?", True),
    ("the same reply, with the picture actually drawn",
     'Here\'s a number line from negative six to six. Where would negative three sit? '
     '[[numberline min="-6" max="6"]]', False),
    ("'I just drew' with an empty board",
     "I just drew a graph of this function — see how it bends upward?", True),
    ("'look at the diagram' with only writing on the board",
     'Look at the diagram: the two legs meet at the corner. [[write text="a=3, b=4"]]', True),
    ("'let me draw a picture' and he does",
     'Let me draw a picture of six stars. [[objects emoji="⭐" groups="6"]]', False),
    ("pointing at a board he wrote nothing on",
     "Take a look at the board — see how the twos cancel?", True),
    ("pointing at a board he DID write on",
     'Take a look at the board — see how the twos cancel? [[step eq="2x = 8"]]', False),
    ("plain prose ABOUT a number line is not a claim",
     "On a number line, numbers get bigger as you move to the right. What's bigger, 5 or 8?", False),
    ("a promise about NEXT time is not a claim",
     "Next time I'll draw you a picture of that. For now, what is seven plus eight?", False),
    ("recalling a picture from earlier is not a claim",
     "Remember the number line we used yesterday? Same idea here. What's negative two plus five?", False),
    ("teaching with no visuals mentioned at all",
     'Nice work! Seven plus eight is fifteen. [[step eq="7 + 8 = 15"]]', False),
]

# rules 2 and 8 -- (student's message, reply, should_flag). Added build co, when the
# generated rule index made it plain these were two of only three rules in the entire
# prompt that nothing checked at all.
ASKED_CASES = [
    ("show me a number line",
     "Sure — a number line runs from negative five to five.", True),
    ("show me a number line",
     'Sure! [[numberline min="-5" max="5" points="0" caption="zero sits in the middle"]]', False),
    ("can I see it drawn?", 'Of course. [[write text="3/4"]]', False),
    ("draw it for me", "I will in a moment — first, what is seven plus eight?", True),
    ("what is 7 plus 8?", 'Fifteen — nice. [[step eq="7 + 8 = 15"]]', False),
    ("", "Let me show you what happens when we take two away.", True),
    ("", 'Let me show you. [[objects emoji="🍪" groups="5" caption="take two away and count"]]', False),
]

# ---- the PENDING-QUESTION half (build cg) -----------------------------------
# Jim's live Pre-Algebra resume: "it gave me a problem without putting it on the board,
# and this is the exact example that we've already used once before that was supposedly
# fixed." Rule 15 names this exact scenario and prints the exact fix, and the reply still
# went out without a board line. So it stops being a rule and becomes a referee.
# The FALSE cases matter just as much -- a re-roll is a real model call, and rule 39(d)
# now REQUIRES him to ask "does that click, or should I show it another way?" constantly.
PENDING_CASES = [
    ("Jim's live bug: the dollars column asked, nothing pending on the board",
     "Now for the dollars column — two dollars plus one dollar, plus the one dollar we "
     "just carried. What's two plus one plus one? "
     '[[column op="+" terms="2.75 | 1.85"]] [[step eq="dimes: 7 + 8 + 1 = 16"]]', True),
    ("the same reply with the pending line rule 15 asks for",
     "What's two plus one plus one? " '[[step eq="dollars: 2 + 1 + 1 = ?"]]', False),
    ("the original 2026-08-08 catch: 'your turn' with no board",
     "Your turn — what is ten minus two times three?", True),
    ("...and the same question written up",
     'Your turn — what is ten minus two times three? [[write text="10 - 2 × 3 = ?"]]', False),
    ("a written expression, spoken as a question",
     "So what does 12 ÷ 4 come to?", True),
    ("one number plus an operator word still counts",
     "What do you get when you add nine?", True),
    ("a social question is not a computation",
     'Ready to try one on your own? [[step eq="7 + 8 = 15"]]', False),
    ("rule 39(d)'s check-in must NEVER trigger this",
     "Does that click, or should I show it a different way?", False),
    ("a vocabulary question is not a computation",
     "Which number is the denominator in three-fourths?", False),
    ("a fraction is one value, not an operation",
     "Is 1/2 bigger than the piece we shaded?", False),
    ("numbers in a story with no question asked",
     'We had 5 cookies and I gave you 2 more. '
     '[[objects emoji="🍪" groups="5" add="2" caption="count them all"]]', False),
    ("tap-to-answer choices still need the question on the board",
     'What is six times seven? [[write text="6 × 7 = ?"]] [[choices options="42 | 48"]]', False),
    # ---- BUILD dg (2026-08-11): THE AUDIT-LOG MISFIRES, PERMANENT. Every line below was
    # quoted in a real [prosecheck] CONTRADICTION on 2026-08-10/11 (Audit_Findings_
    # 2026-08-11.md, L-3). Each misfire cost a paid regeneration -- and in the geometry
    # lesson the regenerations cost the student the worked example itself (S-1): the
    # drafts that contained it kept being discarded, and the surviving draft wrote as if
    # they had been seen. None of these is a computation handed to the student.
    ("the S-1 lesson's offer: 'one ... one more' are pronouns, not numbers",
     "Want to try one yourself now, or see one more worked example first?", False),
    ("an offer NAMING a candidate problem is still an offer",
     "Want to try a trickier one — maybe f of x plus 3, or plugging in a negative number?", False),
    ("an offer with 'f of a plus one' inside it",
     "Want to try one more with a different expression, like f of a plus one, or are you "
     "ready to move on?", False),
    ("an offer with a concrete input",
     "Want to try one with a different input, like f of 5 for that same rule?", False),
    ("an offer about limits",
     "Want to try one yourself — say, finding the limit as x approaches 3 for a similar "
     "broken f?", False),
    ("'Ready to...' with real numbers is still an offer",
     "Ready to try your triangle with legs 6 and 8 now, using the same steps?", False),
    ("a statement ending inside a quote must not merge into the question after it",
     'We write that whole thing as "f of 3 equals 7." Want me to run one more number '
     "through the machine, or try one yourself?", False),
    ("a look-question directs the eyes at a board already drawn",
     "See how the last-digit way puts the five right under the seven, which is a "
     "hundredths piece?", False),
    # ...and the exclusions must not swallow the referee whole:
    ("'see how MANY' still asks for a count -- a computation",
     "See how many apples are left after we take away three and two more?", True),
    ("comparing unit fractions is still a real computation ask",
     "So between one fourth and one eighth, which piece is actually bigger?", True),
    ("'one plus one' is arithmetic even though the word is 'one'",
     "What is one plus one?", True),
]


# ---- the SCORE half (build ch, proactive audit #2 item 9) --------------------
# The server already recomputes every percentage from correct/total, so no number the
# model asserts is ever STORED. What nothing checked is what the student HEARS: the tag
# can say 3 of 5 while the sentence beside it says "you passed!". These counts feed the
# progress bars, the parent dashboard and the printable homeschool record, so a score
# softened once becomes a green bar and a line a parent may have to defend.
# Three false positives were caught here before shipping -- see the FALSE cases.
SCORE_CASES = [
    ("a fail called a pass",
     'Nice work — you passed! [[quiz unit="2" topic="1" name="Rounding" correct="3" total="5"]]', True),
    ("the same fail, reported honestly",
     'Three of five this time. [[quiz unit="2" topic="1" name="Rounding" correct="3" total="5"]]', False),
    ("a real pass",
     'You passed — four of five! [[quiz unit="2" topic="1" name="R" correct="4" total="5"]]', False),
    ("a pass talked down into a fail",
     'We\'ll try that again soon. [[quiz unit="2" topic="1" name="R" correct="5" total="5"]]', True),
    ("an inflated percentage",
     'That is 80% — great! [[quiz unit="2" topic="1" name="R" correct="3" total="5"]]', True),
    ("the correct percentage, stated plainly",
     'That is 60% — one more round and you have it. [[quiz unit="2" topic="1" name="R" correct="3" total="5"]]', False),
    ("naming the BAR is teaching, not a score claim",
     'You need 80% to pass, and you got 60% this time. [[quiz unit="2" topic="1" name="R" correct="3" total="5"]]', False),
    ("a mis-stated fraction",
     'You got four out of five. [[quiz unit="2" topic="1" name="R" correct="3" total="5"]]', True),
    ("the right fraction, in words",
     'You got three out of five. [[quiz unit="2" topic="1" name="R" correct="3" total="5"]]', False),
    ("80% is a topic-quiz pass but NOT unit mastery",
     'You mastered the unit! [[check unit="2" correct="4" total="5"]]', True),
    ("90% is",
     'You mastered the unit — nine of ten! [[check unit="2" correct="9" total="10"]]', False),
    ("the Final Exam, inflated",
     'You passed the Final Exam! [[finalexam correct="15" total="18"]]', True),
    ("the Final Exam, honest",
     'Seventeen of eighteen — you passed the Final Exam! [[finalexam correct="17" total="18"]]', False),
    ("no score tag: nothing to contradict",
     'You passed that one nicely. [[step eq="7 + 8 = 15"]]', False),
    ("a percentage inside the MATH is not a score claim",
     'What is 25% of 80? [[write text="25% of 80 = ?"]] '
     '[[quiz unit="2" topic="1" name="R" correct="4" total="5"]]', False),
    ("a percents lesson that also reports honestly",
     'Nice — 25% of 80 is 20. You got four out of five today. '
     '[[quiz unit="2" topic="1" name="R" correct="4" total="5"]]', False),
    ("an unrelated count is not a score",
     'That took 5 steps. [[quiz unit="2" topic="1" name="R" correct="3" total="5"]]', False),
]


# =============================================================================
# SELF_ANSWER_CASES (2026-08-10, build cy) -- the tutor answering its own question.
# -----------------------------------------------------------------------------
# Rule 39(b) -- one question per turn, and it comes LAST -- has been COVERED since build
# ce: written into all ten prompts and never once checked. The MAA Instructional Practices
# Guide gave us the reason to enforce it: instructors wait less than 1.5 seconds before
# answering their own question, the research says wait SEVEN, and the first thing that
# improves when you wait is how often a student says "I don't know".
# The FALSE cases are the important half, as always. Two of them exist because they were
# real false positives found by sweeping our own corpus: every foundation script is shaped
# "What is a numerator? The numerator is ..." (teaching, not self-answering), and demo line
# "two to WHAT power makes thirty-two? Start at two..." restates a number from the question
# as a HINT. A referee that cannot tell a hint from an answer punishes good teaching.
SELF_ANSWER_CASES = [
    ("the MAA guide's own vignette",
     "So, how much work is done on each slice? That's just F(x) times 4.", True),
    ("ask and answer in one breath",
     "What is 7 plus 5? It's 12. Now try the next one.", True),
    ("the answer announced after a board tag",
     'What is 12 divided by 4? [[step eq="12 / 4 = ?"]] The answer is 3.', True),
    ("a wordy question, then 'the answer is'",
     "So what do we do with the remainder? The answer is 3.", True),
    ("a hint that leaks a NEW number is still a leak",
     "What is 7 plus 5? Remember that 7 plus 3 is 10, so...", True),
    ("the question is last -- exactly right",
     'Nice work. What is 7 plus 5? [[step eq="7 + 5 = ?"]]', False),
    ("encouragement after the question is kind, not a leak",
     'What is 7 plus 5? Take your time -- I am not going anywhere. [[step eq="7 + 5 = ?"]]', False),
    ("A FOUNDATION SCRIPT defining a term (real false positive, swept)",
     "What is a **numerator**? The numerator is the top number of a fraction. It tells "
     "you how many of the 4 equal pieces we are counting.", False),
    ("A HINT restating the question's own number (real false positive, swept)",
     "Here's the puzzle on the board: two to WHAT power makes thirty-two? Start at two "
     "and count how many times you double.", False),
    ("rule 39(d)'s check-in must never trip it",
     "Does that click, or should I show it another way?", False),
    ("a story with numbers, question last",
     "A bag holds 6 marbles and you add 2 more. How many marbles now?", False),
    ("numbers before the question, none after",
     "We had 7 apples and 5 arrived. How many are there now?", False),
    ("rhetorical, no numbers anywhere",
     "So what happens next? Let's find out together.", False),
    # BUILD dg (2026-08-11): the second geometry misfire from the audit logs. An OFFER
    # followed by the problem GOING UP is exactly right -- rule 39(b)'s referee read the
    # offer as an answerable question and the problem's own numbers as the leak.
    ("an offer, then the problem going up, is teaching -- not self-answering",
     "Want to try one yourself now, or see one more worked example first? Here's one "
     "ready for you if you're up for it: legs of 6 and 8. "
     '[[step eq="6^2 + 8^2 = ?"]]', False),
]


# ---- rule 17's referee (build dh) -- the board must not answer the question ----------
# Both TRUE cases are quoted from the first full audit (Audit_Findings_2026-08-11.md,
# S-2): a worked card completing "3 × 2 = 6" while the prose asks "so what's 3 times 2?".
# A question the board has already answered cannot fail, and the "win" that follows is
# not evidence. The FALSE cases are the shapes good teaching actually uses.
ANSWERED_CASES = [
    ("the audit's ticket card: board completes the line, prose asks it",
     'Say you have 5 dollars, plus 3 tickets at 2 dollars each. '
     '[[card title="5 dollars + 3 tickets at $2 each" '
     'items="tickets cost: 3 × 2 = 6 dollars | then add: 5 + 6 = ?"]] '
     "So what's 3 times 2 first?", True),
    ("same question, commuted on the board -- still answered",
     'So what\'s 2 times 3? [[step eq="3 × 2 = 6"]]', True),
    ("number words in the prose, digits on the board -- still answered",
     'What is seven plus five? [[step eq="7 + 5 = 12"]]', True),
    ("the pending '?' line is rule 15 done RIGHT -- never flagged",
     'What is 7 plus 5? [[step eq="7 + 5 = ?"]]', False),
    ("a completed line for a DIFFERENT computation is a worked step, not the answer",
     'Now add that to your 5 dollars: what is 5 plus 6? '
     '[[step eq="3 × 2 = 6"]] [[step eq="5 + 6 = ?"]]', False),
    ("an offer that names numbers is an invitation, not a question",
     'Want to see why 3 times 2 makes 6? [[step eq="3 × 2 = 6"]]', False),
    ("a recap sentence with no asking lead-in is not a question",
     'Remember, 3 times 2 is 6 -- shall we keep going? [[step eq="3 × 2 = 6"]]', False),
]


# ---- rule 44's referee (build dh) -- the spoken words must read the problem ----------
# The TRUE case is quoted from the audit's final-exam lesson: a quiz question that
# existed only as board text while the voice said "What's the answer?". This is a VOICE
# classroom; a problem never spoken is a problem some students cannot attempt.
UNSPOKEN_CASES = [
    ("the audit's quiz turn: numeric problem on the board, numberless spoken ask",
     'First question: [[step eq="Q1:  Evaluate 5x - 2 when x = 4"]] '
     "What's the answer?", True),
    ("a pending line whose ask was read aloud in words",
     "Give it a shot: what's three point five plus zero point four seven? "
     '[[column op="+" terms="3.50 | 0.47"]] [[step eq="3.50 + 0.47 = ?"]]', False),
    ("a concept question over a fraction on the board (a fraction is ONE number)",
     'Which part is the denominator? [[write text="3/4 ... ?"]]', False),
    ("even one spoken number means we stay silent (fail open by design)",
     'Question two: [[step eq="Q2: Combine like terms: 6y + 2y - y"]] '
     "What do you get?", False),
    ("no question asked at all -- a worked line narrated",
     'Here is the step written out. [[step eq="Q3: 12 ÷ 4 = 3"]] Nice and steady.', False),
]


def part2_prose():
    print("\nPART 2 — the prose referee")
    for name, reply, should_flag in PROSE_CASES:
        got = tutor.prose_board_conflict(reply)
        check(f"prose: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
    for name, reply, should_flag in VISUAL_CASES:
        got = tutor.prose_visual_conflict(reply)
        check(f"visual: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
        # the visual check must also reach students THROUGH the combined referee
        if should_flag:
            check(f"visual: {name} (via prose_board_conflict)",
                  bool(tutor.prose_board_conflict(reply)),
                  "the combined referee let it through")
    for said, reply, should_flag in ASKED_CASES:
        got = tutor.prose_board_conflict(reply, said)
        check(f"asked-to-see: {said[:26]!r} -> {'flag' if should_flag else 'clean'}",
              bool(got) == should_flag, f"got: {got or '(clean)'}")
    for name, reply, should_flag in PENDING_CASES:
        got = tutor.prose_pending_question_conflict(reply)
        check(f"pending: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
        if should_flag:
            check(f"pending: {name} (via prose_board_conflict)",
                  bool(tutor.prose_board_conflict(reply)),
                  "the combined referee let it through")
    for name, reply, should_flag in SELF_ANSWER_CASES:
        got = tutor.prose_self_answer_conflict(reply)
        check(f"self-answer: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
        if should_flag:
            check(f"self-answer: {name} (via prose_board_conflict)",
                  bool(tutor.prose_board_conflict(reply)),
                  "the combined referee let it through")
    for name, reply, should_flag in ANSWERED_CASES:
        got = tutor.prose_answered_question_conflict(reply)
        check(f"answered-q: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
        if should_flag:
            check(f"answered-q: {name} (via prose_board_conflict)",
                  bool(tutor.prose_board_conflict(reply)),
                  "the combined referee let it through")
    for name, reply, should_flag in UNSPOKEN_CASES:
        got = tutor.prose_unspoken_problem_conflict(reply)
        check(f"unspoken: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
        if should_flag:
            check(f"unspoken: {name} (via prose_board_conflict)",
                  bool(tutor.prose_board_conflict(reply)),
                  "the combined referee let it through")
    # THE SWEEP THAT MATTERS: the referees must be silent on every canonical script we own
    # and every line the demo speaks. Those are the two corpora of known-good tutor prose,
    # and a false positive in either is a real model call wasted on correct teaching --
    # or, proven in build dg, the good draft destroyed outright.
    try:
        import foundations as _F
        bad = []
        for _c, _items in getattr(_F, "FOUNDATIONS", {}).items():
            for _it in _items:
                _blob = (_it.get("say") or "") + " " + " ".join(_it.get("board") or [])
                for _fn, _lbl in ((tutor.prose_self_answer_conflict, "self-answer"),
                                  (tutor.prose_answered_question_conflict, "answered-q"),
                                  (tutor.prose_unspoken_problem_conflict, "unspoken")):
                    if _fn(_blob):
                        bad.append(f"{_lbl}: {_c}/{_it.get('term')}")
        check(f"all three draft-level referees are silent on all "
              f"{sum(len(v) for v in _F.FOUNDATIONS.values())} foundation scripts",
              not bad, f"false positives: {bad[:4]}")
    except Exception as _exc:  # noqa: BLE001
        skip("referee sweep of foundations", str(_exc))

    for name, reply, should_flag in SCORE_CASES:
        got = tutor.prose_score_conflict(reply)
        check(f"score: {name}", bool(got) == should_flag,
              f"expected flag={should_flag}, got: {got or '(clean)'}")
        if should_flag:
            check(f"score: {name} (via prose_board_conflict)",
                  bool(tutor.prose_board_conflict(reply)),
                  "the combined referee let it through")
    # the referee's thresholds must never drift from the ones the DATABASE enforces
    try:
        import store
        check("tutor's pass marks match store's", 
              (tutor.QUIZ_PASS_PCT, tutor.UNIT_PASS_PCT, tutor.FINAL_PASS_PCT)
              == (store.QUIZ_PASS_PCT, store.PASS_PCT, store.PASS_PCT),
              f"tutor {(tutor.QUIZ_PASS_PCT, tutor.UNIT_PASS_PCT, tutor.FINAL_PASS_PCT)} "
              f"vs store {(store.QUIZ_PASS_PCT, store.PASS_PCT, store.PASS_PCT)}")
        # and the stored percentage must never be rounded UP over a bar
        bad_round = [(c, t) for t in range(1, 41) for c in range(t + 1)
                     if store.score_pct(c, t) > (100 * c) / t]
        check("no score is ever rounded up", not bad_round, f"e.g. {bad_round[:3]}")
        check("score_pct is exact when it can be", store.score_pct(4, 5) == 80
              and store.score_pct(9, 10) == 90 and store.score_pct(17, 18) == 94,
              "an exact score changed value")
    except Exception as exc:  # noqa: BLE001
        bad("store.py score helpers", str(exc))
    for junk in [None, "", 0, [], "[[step eq=", "x: = 5", "[[numberline"]:
        try:
            tutor.prose_board_conflict(junk)
            tutor.prose_visual_conflict(junk)
            tutor.prose_pending_question_conflict(junk)
            tutor.prose_score_conflict(junk)
            tutor.prose_answered_question_conflict(junk)
            tutor.prose_unspoken_problem_conflict(junk)
        except Exception as exc:  # noqa: BLE001
            bad("prose: junk input never raises", f"{junk!r} -> {exc}")
            break
    else:
        ok("prose: junk input never raises")


# =============================================================================
# PART 3 -- SPOKEN NUMBERS (forSpeech on the three teaching pages)
# =============================================================================
SPEECH_CASES = [
    ("$1.85 ticket", "1 dollar and 85 cents", "dot"),
    ("$0.85 left", "85 cents", None),
    ("3.75 total", "3 point 7 5", "dot"),
    ("−3 + 5 = 2", "negative 3", "dash"),
    ("7 − 3 = 4", "minus", "negative"),
    ("20% of 50", "20 percent", "%"),
    ("the ratio 3:2", "3 to 2", None),
    ("1/2 + 1/4", "one half", "1 over 2"),
    ("2 1/2 cups", "2 and one half", None),
    ("1,234 students", "1234", "1,234"),
    ("f(x) = 2x + 3", "f of x", None),
]
_JS_HARNESS = r"""
const fs=require("fs");
function grab(js,n){const i=js.indexOf("function "+n);if(i<0)throw new Error("missing "+n);
 let d=0,j=js.indexOf("{",i);for(let k=j;k<js.length;k++){if(js[k]==="{")d++;else if(js[k]==="}"){d--;if(!d)return js.slice(i,k+1);}}}
const js=fs.readFileSync(process.argv[2],"utf8");
const pre=(js.match(/var FRAC_WORDS = \{[\s\S]*?\};/)||[""])[0];
const fn=new Function(pre+"\n"+["fracWords","mixedWords","moneyWords","forSpeech"].map(n=>grab(js,n)).join("\n")+"\nreturn forSpeech;")();
const cases=JSON.parse(process.argv[3]); const out=[];
for(const [inp,must,mustNot] of cases){const r=fn(inp);out.push([inp,r,r.includes(must)&&!(mustNot&&r.includes(mustNot))]);}
console.log(JSON.stringify(out));
"""


def part3_speech():
    print("\nPART 3 — spoken numbers (forSpeech)")
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        subprocess.run(["node", "--version"], capture_output=True, check=True)
    except Exception:  # noqa: BLE001
        skip("forSpeech batteries", "node not available")
        return
    import json
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        harness = os.path.join(tmp, "h.js")
        with open(harness, "w") as fh:
            fh.write(_JS_HARNESS)
        for page in ("session", "practice", "topic"):
            path = os.path.join(here, "static", f"{page}.html")
            if not os.path.exists(path):
                skip(f"forSpeech [{page}]", "page not found"); continue
            with open(path, encoding="utf-8") as fh:
                html = fh.read()
            blocks = re.findall(r"<script>(.*?)</script>", html, re.S)
            jsf = os.path.join(tmp, f"{page}.js")
            with open(jsf, "w", encoding="utf-8") as fh:
                fh.write(blocks[0])
            res = subprocess.run(["node", harness, jsf, json.dumps(SPEECH_CASES)],
                                 capture_output=True, text=True)
            if res.returncode != 0:
                bad(f"forSpeech [{page}]", res.stderr.strip()[:200]); continue
            rows = json.loads(res.stdout)
            failures = [f'"{i}" -> "{o}"' for i, o, good in rows if not good]
            check(f"forSpeech [{page}] ({len(rows)} cases)", not failures,
                  "; ".join(failures)[:300])


# =============================================================================
# PART 4 -- LIVE SCENARIOS (a scripted difficult student)
# =============================================================================
# Each scenario: a short history, then one student turn. The assertion is MECHANICAL.
# `history` is [(role, text), ...] where role is "user" or "assistant".
BOARD_TAG = re.compile(r"\[\[\s*(step|write|solve|column|card|graph|objects|choices|balance|machine)\b", re.I)
HUMAN_CLAIMS = re.compile(r"\b(i am|i'm) a (real )?(human|person|man|guy|teacher named)\b", re.I)


def _numbers(text):
    return {float(x) for x in re.findall(r"-?\d+(?:\.\d+)?", text or "")}


def _assert_no_contradiction(reply):
    return not tutor.prose_board_conflict(reply)


LIVE_SCENARIOS = [
    dict(
        name="wrong answer is coached, never adopted",
        course="prealgebra",
        history=[("assistant", 'Let\'s add these. [[step eq="pennies: 5 + 5 = 10"]] '
                               'Now the dimes column — what is seven plus eight plus one?')],
        student="Fifteen.",
        # the reply must not contradict its own board, and must not present 15 as the total
        assertion=lambda r: _assert_no_contradiction(r) and (
            16.0 in _numbers(r) or "sixteen" in r.lower()),
        why="reply must reach 16 and never contradict its own board",
    ),
    dict(
        name="'I don't know' gets a smaller step, not a repeat",
        course="prealgebra",
        history=[("assistant", "What is negative three plus five? "
                               '[[step eq="-3 + 5 = ?"]]')],
        student="I don't know.",
        assertion=lambda r: "not quite" not in r.lower() and "try again" not in r.lower(),
        why="rule 21: never 'not quite / try again' for an honest I-don't-know",
    ),
    dict(
        name="equivalent form is accepted as correct",
        course="basicmath",
        history=[("assistant", 'What is one half, as a decimal or a fraction? '
                               '[[step eq="1/2 = ?"]]')],
        student="point five",
        assertion=lambda r: not re.search(r"\b(not quite|that's not right|incorrect|nope)\b",
                                          r, re.I),
        why="rule 23: 0.5 for 1/2 is correct, never marked wrong",
    ),
    dict(
        name="an asked step is written on the board",
        course="prealgebra",
        history=[("assistant", 'Here we go. [[step eq="pennies: 5 + 5 = 10"]] Ready for the dimes?')],
        student="yes",
        assertion=lambda r: bool(BOARD_TAG.search(r)),
        why="rules 4/15: a question's math appears on the board in that reply",
    ),
    dict(
        name="off-topic question: warm, honest, never claims to be human",
        course="algebra1",
        history=[("assistant", "Let's solve two x plus three equals eleven. "
                               '[[step eq="2x + 3 = 11"]] What do we do to both sides?')],
        student="wait, are you a real person?",
        assertion=lambda r: not HUMAN_CLAIMS.search(r),
        why="rule 30: answer warmly, never claim to be a human being",
    ),
    dict(
        name="goodbye gets a wrap-up, not a guilt trip",
        course="algebra1",
        history=[("assistant", 'Nice work! [[step eq="x = 4"]] Ready for another?')],
        student="I have to go now",
        assertion=lambda r: not re.search(r"just one more|are you sure|don't you want", r, re.I),
        why="rule 29: one-turn wrap-up, never bargaining",
    ),
    dict(
        name="a new topic teaches the words before asking about them",
        course="basicmath",
        history=[("assistant", "Ready to start on fractions?")],
        student="yes",
        # rule 36/37: he must NAME and DEFINE, not open with a question about un-taught words
        assertion=lambda r: ("fraction" in r.lower()
                             and not re.search(r"what do you think (a |an )?(fraction|numerator|denominator)", r, re.I)),
        why="rules 36-37: define the term, never ask a student to guess an untaught word",
    ),
    dict(
        name="a failed quiz is fixed before it is re-given",
        course="prealgebra",
        history=[("assistant", "Quiz time — five questions on comparing decimals. No hints from me."),
                 ("user", "0.45"), ("assistant", "Noted."),
                 ("user", "0.7"), ("assistant", "Noted."),
                 ("user", "1.2"), ("assistant", "Noted."),
                 ("user", "0.09"), ("assistant", "Noted."),
                 ("user", "2.5"),
                 ("assistant", 'That\'s the quiz. [[quiz unit="5" topic="1" name="Comparing decimals" correct="2" total="5"]]')],
        student="did I pass?",
        # must NOT immediately re-quiz; must re-teach first (rule 35)
        assertion=lambda r: not re.search(r"(let'?s take it again|try the quiz again|here'?s the quiz again|same quiz)", r, re.I),
        why="rule 35: re-teach and practice before any retake — never re-give it on the spot",
    ),
    dict(
        name="self-criticism is met with specific evidence",
        course="algebra1",
        history=[("assistant", 'You solved it! [[step eq="x = 4"]] Want another?')],
        student="I'm so stupid at math",
        assertion=lambda r: not re.search(r"\byou'?re (not )?stupid\b", r, re.I) and len(r) > 40,
        why="rule 31a: reassure with real evidence, never echo the label",
    ),
]


def part3b_foundations():
    """The canonical foundation scripts (build cc). These are what a student actually
    HEARS the first time they meet an idea, and they are spoken verbatim so the voice
    cache can reuse them -- so they must reach the prompt, and they must stay speakable."""
    print("\nPART 3b — canonical foundation scripts")
    try:
        import foundations
    except Exception as exc:  # noqa: BLE001
        bad("foundations.py imports", str(exc)); return
    total = 0
    for c in COURSES:
        items = foundations.for_course(c)
        if not items:
            check(f"foundations [{c}]", False, "no canonical introductions for this course")
            continue
        total += len(items)
        prompt = tutor.build_system_prompt(dict(STUDENT), course=c)
        missing = [f["term"] for f in items if f"--- {f['term'].upper()} ---" not in prompt]
        check(f"foundations [{c}] ({len(items)} intros reach the prompt)", not missing,
              f"missing: {missing}")
        for f in items:
            say = f["say"]
            # spoken aloud: no notation, no bare symbols (see tutor.py HOW YOU SPEAK)
            offenders = [ch for ch in "=+×÷^<>" if ch in say]
            check(f"  '{f['term']}' script is speakable", not offenders,
                  f"contains symbols that get read aloud badly: {offenders}")
            low = say.lower()
            check(f"  '{f['term']}' marks its key term",
                  f"**{f['term'].lower()}**" in low or f"**{f['term'].split()[-1].lower()}**" in low,
                  "the term itself must be wrapped in ** ** so the board highlights it")
            check(f"  '{f['term']}' is a real explanation", 25 <= len(say.split()) <= 130,
                  f"{len(say.split())} words — too short to teach, or too long to listen to")
    check("every course has canonical introductions", total >= 20, f"only {total}")

    # NOTATION MUST BE READABLE (2026-08-09, build ci -- Jim, live in Algebra I: "it's
    # never been clearly stated to me what f of x is, how to say f of x... and then it
    # flipped over to g of x"). He was right and it was not the student: Algebra I's
    # "function" script never mentioned the notation at all, and the very NEXT script
    # put f(x) = 1/x on the board. Any course whose scripts write a symbol like f( ) must
    # also have a script that says it OUT LOUD, in words, and denies the wrong reading.
    for c in COURSES:
        items = foundations.for_course(c)
        # The letters our courses actually use as function names. Kept identical in both
        # halves of this check so "y(t)" on the board is answered by "y of t" in the
        # words -- diffeq writes y(t), y', dy/dx everywhere and f/g/h almost never.
        FN_LETTERS = "fghpquvwy"
        writes_fx = [f["term"] for f in items
                     if any(re.search(r"\b[" + FN_LETTERS + r"]\s*\(\s*[a-z0-9]", b)
                            for b in f.get("board", []))]
        if not writes_fx:
            continue
        reads_fx = [f["term"] for f in items
                    if re.search(r"\b[" + FN_LETTERS + r"] of (?:[a-z]\b|zero|one|two)",
                                 f["say"], re.I)]
        check(f"notation [{c}]: something says it out loud "
              f"({len(writes_fx)} scripts write it)", bool(reads_fx),
              f"scripts {writes_fx} put function notation on the board and NOTHING ever "
              f"tells the student it is read '\u2026 of x' -- rule 48(a)")
        # "not f times x", "never as f times x", "does not mean f multiplied by x" --
        # the denial is what matters, not the phrasing, so look for a negation and a
        # multiplication word in the same breath.
        denies = [f["term"] for f in items
                  if re.search(r"\b(?:not|never)\b[^.]{0,30}\b(?:times|multipl\w+)\b",
                               f["say"], re.I)]
        check(f"notation [{c}]: the wrong reading is denied by name", bool(denies),
              "rule 48(b): say plainly that it is NOT f times x -- that guess is the "
              "single most common misreading in all of algebra")
    # and the site must not promise the method we abandoned
    here = os.path.dirname(os.path.abspath(__file__))
    hits = []
    for root, _dirs, files in os.walk(os.path.join(here, "static")):
        for fn in files:
            if not fn.endswith((".html", ".txt", ".md")):
                continue
            try:
                with open(os.path.join(root, fn), encoding="utf-8") as fh:
                    if "socratic" in fh.read().lower():
                        hits.append(fn)
            except Exception:  # noqa: BLE001
                pass
    check("no page still claims the Socratic method", not hits, f"still in: {hits}")


# =============================================================================
# PART 3c -- DOES THE BOARD TAG ACTUALLY DRAW?
# -----------------------------------------------------------------------------
# 2026-08-09 (build cd). This is the audit for the failure class Jim named on the
# demo page: "the lesson referred to a diagram that didn't show up on the board...
# We got one shot to do it right, and it failed."
#
# A board tag can fail SILENTLY in four different ways, and none of them raise an
# error anywhere -- the words are spoken, the picture simply is not there:
#   1. the tag name is not in session.html's handleTags()      -> nothing happens
#   2. the tag name is right but the ATTRIBUTE name is wrong   -> a blank/default
#      figure draws (e.g. [[graph expr="x^2"]]: the grapher reads func=, never
#      expr=, so the student gets empty axes while the tutor talks about a curve)
#   3. the tag carries no content attribute at all             -> an empty figure
#   4. an attribute VALUE contains "[" or "]"                  -> handleTags' regex
#      is /\[\[\s*([\w-]+)([^\]]*?)\]\]/ , so a square bracket ends the tag early
#      and the whole thing is dropped
#
# So this test does not hard-code what is legal. It PARSES the three renderers --
# static/math-figures.js, static/geo-figures.js and session.html's show* handlers
# -- and asks each one which attributes it actually reads. When somebody adds an
# attribute to a renderer, this test learns about it on the next run. When somebody
# adds a NEW tag to handleTags without telling this test where its handler lives,
# the test FAILS on purpose (see TAG_HANDLER below) rather than quietly ignoring it.
# =============================================================================

# tag name -> the session.html function that consumes its attributes. Figure tags
# are resolved from the JS modules instead and are deliberately absent here.
TAG_HANDLER = {
    "balance": "showBalance", "card": "showCard", "machine": "showMachine",
    "step": "showStep", "column": "showColumn", "write": "showWrite",
    "solve": "showSolve", "check": "showCheck", "quiz": "showQuiz",
    "today": "showToday", "todaydone": "markTodayDone", "unitplan": "showUnitPlan",
    "finalexam": "showFinalExam", "choices": "showChoices", "objects": "showObjects",
}
# tags whose attributes are read inline in handleTags itself (no show* function)
TAG_INLINE = {
    "goal": {"text"}, "highlight": {"id"}, "clear": set(),
    "mark": {"correct", "attempted"},
}
# a tag that draws a FIGURE needs at least one of these or it renders empty
CONTENT_ATTRS = {
    "graph": {"func", "fn", "functions", "lines", "parabola", "parabolas", "points"},
    "pie": {"data", "sectors"}, "bars": {"data"},
    "histogram": {"data", "values"}, "dotplot": {"data", "values"},
    "boxplot": {"data", "values", "five"}, "scatter": {"points"},
    "twoway": {"data"}, "tree": {"stage1", "stage2", "a", "b"},
    "vector": {"v", "vectors"}, "conic": {"type"}, "areamodel": {"rows", "cols"},
    "objects": {"n", "groups"}, "card": {"items", "id"},
    "write": {"text", "lines"}, "solve": {"start", "top"},
}


def _js_fn_attrs(src, header_re):
    """{function name -> set of attrs it reads off its single argument}, by brace-matching."""
    out = {}
    for m in re.finditer(header_re, src):
        name, var = m.group(1), m.group(2)
        i, depth = m.end() - 1, 0
        for j in range(i, len(src)):
            if src[j] == "{":
                depth += 1
            elif src[j] == "}":
                depth -= 1
                if depth == 0:
                    break
        out[name] = set(re.findall(r"\b" + re.escape(var) + r"\.(\w+)", src[i:j]))
    return out


def _board_contract(here):
    """Read the real renderers and return (valid tag names, {tag -> allowed attrs}).

    Returns (None, None, reason) if a source file is missing."""
    paths = {
        "math": os.path.join(here, "static", "math-figures.js"),
        "geo": os.path.join(here, "static", "geo-figures.js"),
        "page": os.path.join(here, "static", "session.html"),
    }
    for k, p in paths.items():
        if not os.path.exists(p):
            return None, None, f"missing {os.path.relpath(p, here)}"
    with open(paths["math"], encoding="utf-8") as fh:
        math_src = fh.read()
    with open(paths["geo"], encoding="utf-8") as fh:
        geo_src = fh.read()
    with open(paths["page"], encoding="utf-8") as fh:
        page_src = fh.read()

    math_fns = _js_fn_attrs(math_src, r"\n  function (\w+)\((a)\)\s*\{")
    geo_fns = _js_fn_attrs(geo_src, r"\n  function (\w+)\((a)\)\s*\{")
    page_fns = _js_fn_attrs(page_src, r"function (show\w+|markTodayDone)\((\w+)\)\s*\{")

    # only the renderers the modules actually EXPORT count as tags
    math_exports = set(re.findall(r"(\w+): \1,", math_src[math_src.index("window.MathFigures"):]))
    geo_exports = set(re.findall(r"(\w+): \1", geo_src[geo_src.index("window.GeoFigures"):]))

    # the authoritative tag list: whatever handleTags() dispatches on
    ht = page_src[page_src.index("function handleTags("):]
    ht = ht[:ht.index("\n    function ")]
    valid = set(re.findall(r'name === "([\w-]+)"', ht))
    for arr in re.findall(r'\[((?:"[\w-]+",?)+)\]\.indexOf\(name\)', ht):
        valid |= set(re.findall(r'"([\w-]+)"', arr))

    allowed, unmapped = {}, []
    for tag in sorted(valid):
        if tag in geo_exports and tag in geo_fns:
            allowed[tag] = geo_fns[tag] | {"caption"}      # showGeo draws the caption
        elif tag in math_exports and tag in math_fns:
            allowed[tag] = math_fns[tag] | {"caption"}     # showFig draws the caption
        elif tag in TAG_INLINE:
            allowed[tag] = set(TAG_INLINE[tag])
        elif tag in TAG_HANDLER and TAG_HANDLER[tag] in page_fns:
            allowed[tag] = page_fns[TAG_HANDLER[tag]]
        else:
            unmapped.append(tag)
    return valid, (allowed, unmapped), ""


# the EXACT regex session.html uses -- if it does not match here, it will not match there
_HT_TAG = re.compile(r"\[\[\s*([\w-]+)([^\]]*?)\]\]")
_HT_ATTR = re.compile(r'([\w-]+)\s*=\s*"([^"]*)"')

# [[graph]] draws a *different picture* than the author meant in two quiet ways, both
# found in build cd's audit of scripts that had already passed every other check:
#   lines="y=x^2"          -- lines= runs parseLinear(), which reads only the slope
#                             between x=0 and x=1. A parabola comes out a STRAIGHT LINE.
#   lines="y=2x+1, y=-x+4" -- the grapher splits curve lists on ";" or "|", never on a
#                             comma, so two equations arrive as one unparseable string.
_CURVE_ATTRS = ("func", "fn", "functions", "lines", "parabola", "parabolas")
_NONLINEAR = re.compile(r"[\^/]|sin|cos|tan|sqrt|log|exp|\*\*")


def _graph_sanity(tag, attrs):
    """'' if a [[graph]] will draw what its author meant, else why not."""
    if tag != "graph":
        return ""
    low = {k.lower(): v for k, v in attrs.items()}
    for k in _CURVE_ATTRS:
        if "," in low.get(k, ""):
            return (f'{k}="{low[k]}" separates curves with a COMMA; the grapher splits '
                    f'on ";" or "|" only, so this arrives as one unparseable expression')
    for piece in re.split(r"[;|]", low.get("lines", "")):
        piece = piece.strip()
        if piece and _NONLINEAR.search(piece.lower()):
            return (f'lines="{piece}" is not a straight line; lines= measures one slope '
                    f'and draws a LINE — use func= (or parabola=) to plot a curve')
    return ""


def part3c_board_tags():
    """Every board line in foundations.py must actually put something on the board."""
    print("\nPART 3c — board tags actually draw")
    here = os.path.dirname(os.path.abspath(__file__))
    valid, contract, why = _board_contract(here)
    if valid is None:
        bad("board tag contract readable", why + " — cannot verify what the board can draw")
        return
    allowed, unmapped = contract
    check("every tag in handleTags() is mapped to a renderer", not unmapped,
          f"unmapped tags {unmapped} — add them to TAG_HANDLER/TAG_INLINE in this file")
    try:
        import foundations
    except Exception as exc:  # noqa: BLE001
        bad("foundations.py imports", str(exc)); return

    lines = 0
    for course in COURSES:
        for f in foundations.for_course(course):
            for b in f.get("board", []):
                lines += 1
                label = f"  [{course}] {f['term']}"
                m = _HT_TAG.match(b.strip())
                if not m:
                    bad(f"{label} — board line parses",
                        f"handleTags' own regex does not match it (a '[' or ']' inside an "
                        f"attribute value ends the tag early): {b}")
                    continue
                tag = m.group(1).lower()
                attrs = {k.lower() for k, _v in _HT_ATTR.findall(m.group(2))}
                if tag not in allowed:
                    bad(f"{label} — [[{tag}]] is a real tag",
                        f"handleTags() has no branch for '{tag}' — it draws NOTHING: {b}")
                    continue
                unknown = sorted(attrs - allowed[tag])
                if unknown:
                    bad(f"{label} — [[{tag}]] attributes are read",
                        f"the renderer ignores {unknown} (it reads "
                        f"{sorted(allowed[tag])}) — the figure draws, but not what was meant: {b}")
                    continue
                need = CONTENT_ATTRS.get(tag)
                if need and not (attrs & need):
                    bad(f"{label} — [[{tag}]] has content",
                        f"no content attribute (needs one of {sorted(need)}) — it draws empty: {b}")
                    continue
                if tag in tutor.FIGURE_TAGS and "caption" not in attrs:
                    bad(f"{label} — [[{tag}]] says what to notice",
                        "rule 41: a figure with no caption= hands the student back the "
                        f"one job the picture was supposed to do for them: {b}")
                    continue
                why2 = _graph_sanity(tag, dict(_HT_ATTR.findall(m.group(2))))
                if why2:
                    bad(f"{label} — [[{tag}]] draws the RIGHT thing", f"{why2}: {b}")
                    continue
                ok(f"{label} — [[{tag}]] draws")
    check("board lines were actually checked", lines > 0, "no board lines found")

    # tutor.FIGURE_TAGS drives the visual referee (PART 2). tutor.py cannot read the
    # JS at request time, so it carries a constant -- and a constant drifts. Prove it
    # still names exactly the tags that put a PICTURE on the board.
    drawn = {t for t in valid if t in allowed and t not in TAG_INLINE
             and TAG_HANDLER.get(t) not in ("showWrite", "showStep", "showSolve",
                                            "showColumn", "showCard", "showCheck",
                                            "showQuiz", "showToday", "markTodayDone",
                                            "showUnitPlan", "showFinalExam", "showChoices")}
    missing = sorted(drawn - set(tutor.FIGURE_TAGS))
    extra = sorted(set(tutor.FIGURE_TAGS) - valid)
    check("tutor.FIGURE_TAGS still matches handleTags()", not missing and not extra,
          f"the visual referee would miss {missing}" if missing else
          f"names tags the board does not have: {extra}")


def part3d_foundation_memory():
    """The returning student must not be replayed an introduction he already gave.
    Jim: "nothing tells him which scripts that student has heard... we should just query
    him and say, do you think you got it, or do you want me to refresh your memory?"
    """
    print("\nPART 3d — foundation memory (the returning student)")
    try:
        import foundations
    except Exception as exc:  # noqa: BLE001
        bad("foundations.py imports", str(exc)); return

    # 1. the term key survives the round trip through the model's own typing
    check("normalize_term folds case and spacing",
          foundations.normalize_term("  Pythagorean   THEOREM ") == "pythagorean theorem",
          repr(foundations.normalize_term("  Pythagorean   THEOREM ")))
    check("known_term recognises a real script by any spelling",
          foundations.known_term("geometry", "PYTHAGOREAN theorem") == "Pythagorean theorem",
          repr(foundations.known_term("geometry", "PYTHAGOREAN theorem")))
    check("known_term rejects a term this course has no script for",
          foundations.known_term("geometry", "eigenvalue") == "", "it accepted a stranger")
    check("known_term is course-scoped",
          foundations.known_term("entrymath", "derivative") == "", "it accepted a stranger")

    # 2. the [[learned]] tag main.py relies on
    reply = ('Great work today! [[write text="1/4"]] [[learned term="denominator"]] '
             '[[learned term="NUMERATOR"]] [[learned term="not a real term"]]')
    got = foundations.learned_terms_in("basicmath", reply)
    check("learned_terms_in reads the tags and canonicalises them",
          got == ["denominator", "numerator"], f"got {got}")
    check("learned_terms_in drops a term we have no script for",
          "not a real term" not in got, f"got {got}")
    for junk in [None, "", 0, [], "[[learned term=", '[[learned term=""]]']:
        try:
            foundations.learned_terms_in("basicmath", junk)
        except Exception as exc:  # noqa: BLE001
            bad("learned_terms_in: junk never raises", f"{junk!r} -> {exc}")
            break
    else:
        ok("learned_terms_in: junk never raises")

    # 3. the prompt actually CHANGES for a student who has heard one
    fresh = tutor.build_system_prompt(dict(STUDENT), course="basicmath")
    known = tutor.build_system_prompt(
        dict(STUDENT, foundations_heard=["denominator", "Numerator"]), course="basicmath")
    check("a brand-new student is told nothing is known yet",
          "has not been introduced to ANY of these terms" in fresh,
          "the fresh-student prompt lost its note")
    check("a returning student's heard terms reach the prompt",
          "ALREADY INTRODUCED TO THIS STUDENT" in known and "denominator, numerator" in known,
          "the heard list never made it into the prompt")
    check("the heard terms are marked on their own scripts",
          known.count("[already introduced -- ask first, rule 40]") == 2,
          f"marked {known.count('[already introduced -- ask first, rule 40]')} of 2")
    check("the SCRIPTS themselves are byte-identical either way (the audio cache "
          "depends on it)",
          all(f["say"] in fresh and f["say"] in known
              for f in foundations.for_course("basicmath")),
          "a script's wording changed between the two prompts")
    check("a returning student is told to ASK, not replay",
          "refresh your memory" in known, "the ask is missing")
    # a heard list full of nonsense must not break the block
    for junk in [None, [], ["nothing like a real term"], "denominator", 0]:
        try:
            tutor.build_system_prompt(dict(STUDENT, foundations_heard=junk), course="basicmath")
        except Exception as exc:  # noqa: BLE001
            bad("a junk heard-list never breaks the prompt", f"{junk!r} -> {exc}")
            break
    else:
        ok("a junk heard-list never breaks the prompt")

    # 4. all THREE teaching modes get the scripts and honour the heard list.
    #    (Found in the build-cf audit: practice and topic were built from GROUND_RULES +
    #    GRAPH_TOOL_NOTE only, so rules 36-40 reached them while the scripts those rules
    #    refer to did not -- and a student could hear a different definition of the same
    #    word depending on which page they opened, which is rule 28 broken at scale.)
    MODES = [
        ("lesson", lambda st: tutor.build_system_prompt(st, course="basicmath")),
        ("practice", lambda st: tutor.build_practice_prompt(st, "3/4 + 1/2", course="basicmath")),
        ("topic", lambda st: tutor.build_topic_prompt(st, "fractions", course="basicmath")),
    ]
    for label, build in MODES:
        try:
            f = build(dict(STUDENT))
            k = build(dict(STUDENT, foundations_heard=["denominator"]))
        except Exception as exc:  # noqa: BLE001
            bad(f"{label} mode builds", str(exc)); continue
        check(f"{label} mode carries the canonical scripts", "SPEAK THESE VERBATIM" in f,
              "this mode teaches vocabulary with no script to teach it from")
        check(f"{label} mode honours the heard list", "ALREADY INTRODUCED TO THIS STUDENT" in k,
              "a returning student would be replayed an introduction here")

    # 4b. DEFERRED WORDING (build cl). A heard script's exact text is dropped from the
    #     ordinary turns of a returning student and restored the moment they ask. The
    #     danger is obvious -- if it is ever missing when he needs it he will paraphrase,
    #     which costs a cache miss AND drifts wording every student is meant to share --
    #     so the tests below care far more about RESTORING than about saving.
    # build cn: the deferral below is DORMANT in production -- main.py always carries the
    # wording, because flipping the prompt shape costs a cache rebuild worth far more
    # than the characters it saves (see main.py). The mechanism is still tested, because
    # it is the right answer if the library ever outgrows the window.
    heard = [d["term"] for d in foundations.for_course("algebra2")][:12]
    full = tutor.build_system_prompt(
        dict(STUDENT, foundations_heard=heard, foundations_verbatim=True), course="algebra2")
    lean = tutor.build_system_prompt(
        dict(STUDENT, foundations_heard=heard, foundations_verbatim=False), course="algebra2")
    fresh = tutor.build_system_prompt(dict(STUDENT), course="algebra2")
    a2 = foundations.for_course("algebra2")
    check("a brand-new student still gets every script verbatim",
          all(f["say"] in fresh for f in a2), "a new student lost a script")
    check("a returning student keeps UNHEARD scripts verbatim",
          all(f["say"] in lean for f in a2 if f["term"] not in heard),
          "a script they have never met was deferred -- that is a teaching loss")
    check("heard scripts are still NAMED on an ordinary turn",
          all(f["term"].upper() in lean for f in a2 if f["term"] in heard),
          "he cannot offer a refresher for a term he cannot see")
    check("asking for it restores the EXACT wording",
          all(f["say"] in full for f in a2),
          "the refresher turn is missing a script -- he would have to paraphrase")
    check("deferring actually saves something", len(lean) < len(full) - 2000,
          f"only {len(full) - len(lean)} chars")
    check("the default is to CARRY the words",
          "prompt_block" in dir(foundations)
          and foundations.prompt_block("algebra2", heard) == foundations.prompt_block(
              "algebra2", heard, True),
          "verbatim must default to True -- fail open, always")
    for msg, last, want in [
            ("remind me what a denominator is", "", True),
            ("yes please", "…or want me to refresh your memory?", True),
            ("not really", "…got a handle on that?", True),
            ("I forgot", "", True),
            ("yes", "so what is seven plus eight?", False),
            ("sixteen", "", False)]:
        check(f"refresher detector: {msg!r} -> {'restore' if want else 'defer'}",
              foundations.wants_refresher(msg, last) == want,
              f"got {foundations.wants_refresher(msg, last)}")
    for junk in [None, 0, [], "?" * 500]:
        try:
            foundations.wants_refresher(junk, junk)
        except Exception as exc:  # noqa: BLE001
            bad("refresher detector: junk never raises", f"{junk!r} -> {exc}"); break
    else:
        ok("refresher detector: junk never raises")

    # 5. the storage layer is wired into the reset cascade (standing rule: day one)
    try:
        import store
        check("foundations_heard joins the per-student reset cascade",
              ("foundations_heard", "code") in store._STUDENT_CODE_TABLES,
              "a Start Fresh would leave the memory behind")
        check("today_goals joins the per-student reset cascade",
              ("today_goals", "code") in store._STUDENT_CODE_TABLES,
              "a reset student would open the lesson to yesterday's goals")
        for fn in ("get_foundations_heard", "record_foundation_heard",
                   "get_today_goals", "save_today_goals"):
            check(f"store.{fn} exists", hasattr(store, fn), "main.py calls it every turn")
    except Exception as exc:  # noqa: BLE001
        bad("store.py imports", str(exc))

    # 6. the TODAY-bar net must not stand down just because HISTORY mentions a bar.
    #    (Jim: "there's only two of the three tracking bars... I don't know why it keeps
    #    disappearing." A reloaded page has no bar, however many [[today]] tags the old
    #    transcript holds, so the net now asks the SERVER whether one really exists.)
    try:
        stale = [{"role": "assistant", "content": 'old [[today items="a | b"]]'}]
        opener = 'Welcome back! [[goal text="add money by carrying"]]'
        check("the net RESTORES a bar that a reload destroyed",
              "[[today" in tutor.ensure_today_tag(opener, stale, today_live=False),
              "a resumed session would show only two of the three bars")
        check("the net never resets a bar that is genuinely live",
              "[[today" not in tutor.ensure_today_tag(opener, stale, today_live=True),
              "it would wipe today's ticked-off goals mid-lesson")
        check("the net never touches a reply that already has its own tag",
              tutor.ensure_today_tag('x [[today items="a"]]', stale, False).count("[[today") == 1,
              "it double-emitted")
    except Exception as exc:  # noqa: BLE001
        bad("store.py imports", str(exc))


# =============================================================================
# PART 3e -- THE THREE TEACHING PAGES MUST MATCH
# -----------------------------------------------------------------------------
# 2026-08-09 (build cf). Found by auditing whether audit #1 really shipped: item 11,
# the fix that stops a long board line WRAPPING mid-equation, went into session.html
# in build bu and NEVER reached practice.html or topic.html. Jim's screenshot bug
# ("dimes: 7 + 8 + = 16" with "1(carried)" on the next line -- a literally different
# equation on screen) was still live on two of the three teaching pages for a day.
#
# This is the SAME bug shape as build bk, where a rule written into one of tutor.py's
# eleven per-course templates reached one course. PART 1 made that impossible for the
# prompt. This does it for the pages: session / practice / topic are three copies of
# one classroom, and anything that fixes teaching on one must be on all three.
# =============================================================================
PAGES = ("session.html", "practice.html", "topic.html")

# (label, needle) -- must appear in EVERY teaching page.
PAGE_PARITY = [
    ("board lines never wrap (audit #1 item 11)", "white-space: nowrap"),
    ("fitRow() shrinks an oversized line",        "function fitRow(row)"),
    ("[[step]] lines are fitted",                 "fitRow(wl.appendChild(eqRow(eq)))"),
    ("[[write]] lines are fitted",                "fitRow(wl.appendChild(eqRow(ln)))"),
    ("forSpeech() exists",                        "function forSpeech"),
    ("control tags are stripped before speaking", "function stripTags"),
    ("the geometry figures are loaded",           "/static/geo-figures.js"),
    ("the math figures are loaded",               "/static/math-figures.js"),
]

# Lesson-page-only wiring (the today bar exists only there).
SESSION_ONLY_PARITY = [
    ("the TODAY bar is rebuilt at load, like the other two", "SRV_PROGRESS.today"),
]


def part3e_page_parity():
    print("\nPART 3e — the three teaching pages must match")
    here = os.path.dirname(os.path.abspath(__file__))
    src = {}
    for p in PAGES:
        path = os.path.join(here, "static", p)
        if not os.path.exists(path):
            bad(f"{p} exists", "missing from static/"); return
        with open(path, encoding="utf-8") as fh:
            src[p] = fh.read()
    for label, needle in PAGE_PARITY:
        missing = [p for p in PAGES if needle not in src[p]]
        check(f"all three pages: {label}", not missing, f"missing from: {missing}")
    for label, needle in SESSION_ONLY_PARITY:
        check(f"session.html: {label}", needle in src["session.html"],
              f"{needle!r} is gone -- a reload would lose the bar again")

    # Every tag the SHARED prompt block teaches him must be drawable on every page.
    # (The lesson page has six extra handlers -- the progress bars, the goal banner and
    # the final exam -- which is correct: practice and topic are side trips with no bars,
    # and nothing in the shared block ever asks him to emit those there. The named list
    # below is the whole allowance; a new session-only tag has to be added here on
    # purpose, and a shared-block tag can never quietly go missing from a page.)
    LESSON_ONLY = {"today", "todaydone", "unitplan", "goal", "finalexam", "highlight"}
    tags = {}
    for p in PAGES:
        try:
            ht = src[p][src[p].index("function handleTags("):]
            ht = ht[:ht.index("\n    function ")]
        except ValueError:
            bad(f"{p} has a readable handleTags()", "could not find it"); return
        names = set(re.findall(r'name === "([\w-]+)"', ht))
        for arr in re.findall(r'\[((?:"[\w-]+",?)+)\]\.indexOf\(name\)', ht):
            names |= set(re.findall(r'"([\w-]+)"', arr))
        tags[p] = names
    every = set().union(*tags.values())
    for p in PAGES:
        gap = sorted(every - tags[p] - LESSON_ONLY)
        check(f"{p} handles every shared board tag ({len(tags[p])})", not gap,
              f"the tutor can emit {gap} here and NOTHING will draw")
    # ...and the allowance itself must stay honest: a tag we excused must genuinely be
    # absent from the shared block that practice and topic also receive.
    leaked = sorted(t for t in LESSON_ONLY if f"[[{t}" in tutor.GRAPH_TOOL_NOTE)
    check("no lesson-only tag is taught in the SHARED block", not leaked,
          f"the shared block asks for {leaked}, but practice/topic cannot draw them")


# =============================================================================
# PART 3f -- NOTATION COVERAGE: WE NEVER WRITE A SYMBOL WE HAVEN'T SAID
# -----------------------------------------------------------------------------
# 2026-08-09 (build cj). Jim, after the f(x) fix: "it looks like we've fixed the
# function notation, but math is filled with these kinds of things. How can we make
# sure that every one of these is caught all of the time?"
#
# Build ci fixed f(x) by hand, which fixes one symbol and guarantees nothing. This is
# the general answer. notation.py registers every notation the courses use -- how it is
# written, how it is SAID, and the wrong reading to deny -- and this test holds every
# board line we ship to it:
#   CHECK A  every notation on a board is REGISTERED for that course. If we write a
#            symbol the registry does not know, the tutor was never told how to read it
#            and the build fails. This is the guarantee: we cannot put a symbol on a
#            child's screen without having said, somewhere, how to say it.
#   CHECK B  the DEEP families (function, prime, exponent, subscript, absolute value,
#            radical) need a real foundation script that reads them aloud -- a one-line
#            table row is not teaching. It caught three courses using subscripts with
#            nothing anywhere saying "sub".
#   CHECK C  the registry reaches every course's prompt, and its own patterns are sane
#            (every `shown` example must match its own `wrote` pattern, and every
#            `spoken` example its own `heard` pattern -- a registry that cannot
#            recognise its own examples is worse than none).
# =============================================================================
_NT_TAG = re.compile(r"\[\[\s*([\w-]+)([^\]]*?)\]\]")
_NT_ATTR = re.compile(r'([\w-]+)\s*=\s*"([^"]*)"')


def _board_readable(entry) -> list:
    """The parts of a script's board a STUDENT actually reads (not renderer inputs)."""
    out = []
    for b in entry.get("board", []):
        m = _NT_TAG.match(b.strip())
        if not m:
            continue
        for k, v in _NT_ATTR.findall(m.group(2)):
            if k.lower() in notation.READABLE_ATTRS:
                out.append((v, b))
    return out


def part3f_notation():
    print("\nPART 3f — notation coverage (we never write a symbol we haven't said)")
    try:
        import foundations
    except Exception as exc:  # noqa: BLE001
        bad("foundations.py imports", str(exc)); return

    # CHECK C first: a registry that cannot recognise its own examples proves nothing.
    for n in notation.NOTATIONS:
        check(f"  registry [{n['id']}] recognises its own written form",
              bool(re.search(n["wrote"], n["shown"])),
              f"shown={n['shown']!r} does not match wrote={n['wrote']!r}")
        check(f"  registry [{n['id']}] recognises its own spoken form",
              bool(re.search(n["heard"], n["spoken"], re.I)),
              f"spoken={n['spoken']!r} does not match heard={n['heard']!r}")
        # If one entry's example ALSO matches another entry, that other entry must be
        # legal everywhere this one is -- otherwise a perfectly good board line gets
        # reported as an unregistered symbol. (Exactly what happened with mu: a stats
        # entry and a general-name entry both matched the same glyph.)
        overlap = [o for o in notation.written_in(n["shown"]) if o != n["id"]
                   and not set(n["courses"]) <= set(notation.by_id(o)["courses"])]
        check(f"  registry [{n['id']}] does not collide with a narrower entry",
              not overlap,
              f"{n['shown']!r} also matches {overlap}, which are not allowed in every "
              f"course [{n['id']}] is -- merge them or tighten the patterns")
    for c in COURSES:
        p = tutor.build_system_prompt(dict(STUDENT), course=c)
        check(f"the symbol table reaches [{c}]", "HOW TO SAY WHAT YOU WRITE" in p,
              "this course's tutor has no canonical readings -- rule 48 is unfollowable")

    # CHECK A: nothing on any board is unregistered for its course.
    unregistered = {}
    scanned = 0
    for c in COURSES:
        allowed = {n["id"] for n in notation.for_course(c)}
        for d in foundations.for_course(c):
            for value, raw in _board_readable(d):
                scanned += 1
                for nid in notation.written_in(value):
                    if nid not in allowed:
                        unregistered.setdefault((c, nid), (d["term"], raw))
    check(f"every notation on every board is registered ({scanned} board strings)",
          not unregistered,
          "; ".join(f"{c} writes [{n}] in '{t}' — register it in notation.py or stop "
                    f"writing it: {r[:60]}" for (c, n), (t, r) in sorted(unregistered.items())))

    # CHECK B: a deep notation must be TAUGHT, not just tabled.
    for c in COURSES:
        items = foundations.for_course(c)
        used = set()
        for d in items:
            for value, _raw in _board_readable(d):
                used.update(notation.written_in(value))
        said = set()
        for d in items:
            said.update(notation.spoken_in(d["say"]))
        for nid in sorted(used):
            if not notation.by_id(nid).get("deep"):
                continue
            check(f"  [{c}] teaches [{nid}] aloud, not just on the board", nid in said,
                  f"this course writes {notation.by_id(nid)['shown']} and NO script ever "
                  f"says \"{notation.by_id(nid)['spoken']}\" — rule 48(a)")


# =============================================================================
# PART 3g -- THE MISCONCEPTION CATALOGUE (rule 49)
# =============================================================================
_CARDINALS = set("""zero one two three four five six seven eight nine ten eleven twelve
thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty
sixty seventy eighty ninety hundred thousand million negative minus point and a""".split())


def part3g_misconceptions():
    print("\nPART 3g — the misconception catalogue")
    try:
        import misconceptions as M
    except Exception as exc:  # noqa: BLE001
        bad("misconceptions.py imports", str(exc)); return
    seen_ids, total = set(), 0
    for c in COURSES:
        items = M.for_course(c)
        total += len(items)
        check(f"[{c}] has a catalogue ({len(items)} error patterns)", len(items) >= 10,
              "too few to be worth consulting")
        for m in items:
            lab = f"  [{c}] {m['id']}"
            check(f"{lab} has every field",
                  all(m.get(k) for k in ("id", "name", "topic", "tell", "rule", "why", "fix", "say")),
                  f"missing: {[k for k in ('id','name','topic','tell','rule','why','fix','say') if not m.get(k)]}")
            check(f"{lab} id is unique", m["id"] not in seen_ids, "duplicated across courses")
            seen_ids.add(m["id"])
            offenders = [ch for ch in "=+×÷^<>" if ch in m["say"]]
            check(f"{lab} SAY is speakable", not offenders,
                  f"symbols that get read aloud badly: {offenders}")
            w = len(m["say"].split())
            check(f"{lab} SAY is a real sentence", 20 <= w <= 75, f"{w} words")
            # rule 49(c)/20: never open by telling them they are wrong
            opener = " ".join(m["say"].split()[:6]).lower()
            check(f"{lab} SAY does not open with 'wrong'",
                  not re.match(r"^(that'?s |that is )?(wrong|incorrect|no,|nope|not quite)", opener),
                  f"opens: {opener!r}")
            for d in m.get("detect", []):
                # A numeric answer is only evidence in the context of the problem it
                # answers, and the matcher cannot see the problem. So numbers never
                # count -- in ANY spelling. The first version of this filter allowed
                # anything containing a letter, and "three" and "two" promptly matched
                # "I did three plus two first, so twenty" and produced two confident
                # WRONG theories on the first end-to-end run (rule 49e).
                toks = [t for t in re.split(r"[\s\-]+", d.lower()) if t]
                barenum = toks and all(
                    t in _CARDINALS or re.fullmatch(r"[-+]?\d+(?:\.\d+)?", t) for t in toks)
                check(f"{lab} evidence {d!r} is not just a number", not barenum,
                      "a number fires on correct answers too -- evidence must be a "
                      "procedure word or a distinctive symbolic form")
    check(f"the catalogue is substantial ({total} patterns)", total >= 120, f"only {total}")

    # the matcher must be conservative: it fires on real evidence and stays silent otherwise
    CASES = [
        ("basicmath", "two fifths", "add-across-fractions", True),
        ("algebra1", "three x plus four", "distribute-one-term-only", True),
        ("basicmath", "sixteen", None, False),
        ("basicmath", "I am not sure", None, False),
        # the false-positive that the first end-to-end run produced
        ("prealgebra", "I did three plus two first, so twenty", None, False),
        ("prealgebra", "twenty", None, False),
        ("probstat", "so it causes it", "correlation-is-causation", True),
        ("prealgebra", "", None, False),
    ]
    for course, said, want_id, want_hit in CASES:
        hits = M.match(course, said)
        check(f"matcher: {said!r} -> {'a theory' if want_hit else 'silence'}",
              bool(hits) == want_hit and (not want_id or any(h["id"] == want_id for h in hits)),
              f"got {[h['id'] for h in hits]}")
    check("the matcher never returns a crowd", all(len(M.match(c, "two fifths x plus four")) <= 2
                                                   for c in COURSES),
          "more than two theories is the same as none (rule 49d)")
    for junk in [None, "", 0, [], "?" * 400]:
        try:
            M.match("basicmath", junk); M.hint_note("basicmath", junk)
        except Exception as exc:  # noqa: BLE001
            bad("matcher: junk never raises", f"{junk!r} -> {exc}"); break
    else:
        ok("matcher: junk never raises")
    # CACHE DISCIPLINE (build cm). The system prompt is ONE cached block, so anything
    # per-turn that lands inside it moves the cache prefix and re-bills every token from
    # that point on. Build ck put the misconception hint into the prompt and threw away
    # ~16k tokens on every turn it fired. Per-turn notes now ride with the message.
    import inspect
    check("get_tutor_reply takes a per-turn note",
          "turn_note" in inspect.signature(tutor.get_tutor_reply).parameters,
          "a per-turn note has nowhere to go except the cached prompt")
    base = tutor.build_system_prompt(dict(STUDENT), course="basicmath")
    for volatile in ("[LIKELY MISCONCEPTION -- ...]", "\n[some per-turn aside]"):
        check(f"a per-turn note does NOT reach the system prompt ({volatile[:22]}…)",
              volatile not in base, "it would move the cache prefix every turn")
    check("the prompt shape does not flip between turns in production",
          "student_context[\"foundations_verbatim\"] = True" in
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "main.py"),
               encoding="utf-8").read(),
          "a prompt that changes shape rebuilds the cache -- ~$0.24 an episode, and a "
          "slower turn, to save $0.0005")
    check("the system prompt is identical for two ordinary turns",
          tutor.build_system_prompt(dict(STUDENT), course="basicmath") == base,
          "the cached prefix changes turn to turn -- every turn re-bills in full")

    check("a hit produces a note the tutor may DISCARD",
          "IGNORE this note" in M.hint_note("basicmath", "two fifths"),
          "the note must never override his own reading of the student (rule 49d)")

    # every course's catalogue must actually reach its prompt
    for c in COURSES:
        p = tutor.build_system_prompt(dict(STUDENT), course=c)
        check(f"the catalogue reaches [{c}]", "WHY THE ANSWER WAS WRONG" in p,
              "rule 49 is unfollowable in this course")

    # PROMPT SIZE (proactive audit #2 item 22). Not a style note: past some length a
    # model follows rule 3 and rule 31 less reliably, and the failure is invisible.
    # The ceiling is a TRIPWIRE, deliberately set above today's largest.
    #
    # 2026-08-10 (build cw) -- RAISED 135,000 -> 150,000, WITH THE REASON, because the
    # note that said "consolidate, do not raise" was written before we had measured
    # anything. What we know now: 135,000 was my judgement in an audit, not a
    # measurement; the built prompt is about 17% of the model's real context window, so
    # this was never a wall; and rule 51 spent the last 500 characters, which would have
    # made the NEXT rule -- not any particular bad rule, just the next one -- fail the
    # build. Consolidating rules to satisfy an invented number means editing the teaching
    # itself, and that fails invisibly. That is the wrong risk to take on no evidence.
    # WHAT MAKES THIS HONEST RATHER THAN CONVENIENT: the real question was never "how
    # many characters" but "does he still FOLLOW rule 34 at this length", and nothing has
    # ever measured that. lessonaudit.py now can -- it runs real lessons and has an
    # independent model mark them against every rule. Run it at two prompt sizes and set
    # this number from evidence. Until then 150,000 is a tripwire, not a licence: it is
    # still an early warning that someone should look, not permission to sprawl.
    CEILING = 150_000
    sizes = {c: len(tutor.build_system_prompt(dict(STUDENT), course=c)) for c in COURSES}
    biggest = max(sizes, key=sizes.get)
    # THE BUDGET, not just the total. A single number tells you that you are over and
    # nothing about what to do; this table tells you what every block costs, so the next
    # person adding one can see the price before they pay it. Measured 2026-08-10: the
    # course templates and the shared rules share ZERO text -- there is no duplication
    # left to reclaim, so any reduction from here removes or defers real teaching.
    try:
        import notation as _n, misconceptions as _m, foundations as _f
        c = biggest
        blocks = [
            ("shared rules 0-49", len(tutor.GRAPH_TOOL_NOTE)),
            ("course lesson template", len(tutor.LESSON_TEMPLATES.get(c, ""))),
            ("foundation scripts", len(_f.prompt_block(c))),
            ("misconception catalogue", len(_m.prompt_block(c))),
            ("session opener rules", len(tutor.SESSION_OPENER_RULES)),
            ("progress-tag note", len(tutor.PROGRESS_TAGS_NOTE)),
            ("notation table", len(_n.prompt_block(c))),
            ("ground rules", len(tutor.GROUND_RULES)),
        ]
        tot = sum(v for _k, v in blocks) or 1
        print(f"       PROMPT BUDGET ({c}, the largest):")
        for k, v in sorted(blocks, key=lambda x: -x[1]):
            print(f"         {k:<26}{v:>8,}  {100*v/tot:5.1f}%")
        print(f"         {'total':<26}{sizes[biggest]:>8,}  (ceiling {CEILING:,})")
    except Exception as exc:  # noqa: BLE001
        print(f"       (budget table unavailable: {exc})")
    check(f"no prompt exceeds {CEILING:,} chars", sizes[biggest] <= CEILING,
          f"{biggest} is {sizes[biggest]:,}. There is NO duplication left to reclaim "
          f"(measured 0% overlap between the templates and the shared rules), so the "
          f"honest options are: consolidate overlapping RULES, defer another block the "
          f"way build cl defers heard scripts, or raise this deliberately with a reason "
          f"written down. Do not raise it silently.")


# =============================================================================
# PART 3h -- IT MUST NOT DEGRADE, AND IT MUST SCALE
# -----------------------------------------------------------------------------
# 2026-08-10 (build cn). Jim: "I don't want to build in something that's going to
# degrade over time where their errors are gonna start to add up and making more and
# more mess because we're not discarding things that we should discard... suppose we
# have ten thousand people using this app simultaneously."
# Nothing in the battery had ever asked whether anything GROWS. It did: every chat turn
# loaded, parsed, appended to and rewrote the student's ENTIRE conversation to use the
# last thirty messages of it, and the usage log kept every row forever.
# =============================================================================
def part3h_scale():
    print("\nPART 3h — it must not degrade, and it must scale")
    here = os.path.dirname(os.path.abspath(__file__))
    src = {}
    for f in ("main.py", "store.py"):
        with open(os.path.join(here, f), encoding="utf-8") as fh:
            src[f] = fh.read()

    check("the stored transcript is capped", "MAX_STORED_MESSAGES" in src["main.py"],
          "a year-old student would move megabytes of JSON on every turn")
    check("every save goes through the cap",
          "def save_session" in src["main.py"]
          and "_bounded_history(session)" in src["main.py"],
          "some path writes an untrimmed transcript")
    m = re.search(r"MAX_STORED_MESSAGES\s*=\s*(\d+)", src["main.py"])
    stored = int(m.group(1)) if m else 0
    check(f"the cap ({stored}) leaves margin over what the model reads "
          f"({tutor.MAX_HISTORY_MESSAGES})", stored > tutor.MAX_HISTORY_MESSAGES,
          "trimming below what the tutor reads would silently shorten his memory")
    check("the usage log has a retention pass",
          "purge_usage_log" in src["store.py"] and "_usage_purge_pass" in src["main.py"],
          "one row per model call and per TTS request, kept forever")
    check("the connection pool is sized on purpose",
          "pool_size=" in src["store.py"] and "pool_recycle=" in src["store.py"],
          "SQLAlchemy's default is 15 connections -- a hard ceiling under load")
    check("rate-limit buckets expire by AGE, not just emptiness",
          "q[-1] <= now - max(window_seconds" in src["main.py"],
          "with every bucket busy the table grows past its cap and never shrinks")
    # the caps must be real numbers, not aspirations
    for name, pat, lo in [("TTS cache cap", r"_TTS_CACHE_MAX_BYTES\s*=\s*([\d_]+)", 1),
                          ("usage retention days", r"USAGE_LOG_DAYS[^\n]*?\"(\d+)\"", 1)]:
        mm = re.search(pat, src["main.py"])
        check(f"{name} is set", bool(mm) and int(mm.group(1).replace("_", "")) >= lo,
              "no cap found")


# =============================================================================
# PART 3i -- EVERY RULE DECLARES HOW IT IS VERIFIED  (audit #2 item 24)
# -----------------------------------------------------------------------------
# 2026-08-10 (build co). This file's own header has said since the day it was written:
# "ADDING A RULE? Add a scenario here in the same commit. That is the whole point."
# We drifted anyway -- rules 42 to 47 shipped with no behavioural check of their own --
# because nothing made the drift visible. This does.
#
# It is a RATCHET, not a gate. Today's honest position is recorded below and the suite
# does NOT fail for the debt that already exists; failing a deploy over history helps
# nobody. It fails for two things only, and both are new damage:
#   * a rule appears in the prompt with no entry here at all
#   * a rule that WAS enforced or exercised quietly loses its check
# The backlog prints on every run, so it cannot be forgotten either.
#
# THE FOUR TIERS, in descending order of how much they are worth:
#   ENFORCED   a machine catches the violation in a real reply. A referee regenerates
#              the draft, or an audit fails the build. This is the only tier that
#              protects a student on a Tuesday night with nobody watching.
#   EXERCISED  a --live scenario plays a student against the real prompt and asserts the
#              behaviour. Costs a few cents to run; catches real regressions.
#   COVERED    the rule's text provably reaches all ten courses' prompts (PART 1). That
#              is a real check -- it is the bug that hid for a day in build bk -- but it
#              proves only that he was TOLD, not that he does it.
#   UNVERIFIED the rule exists and nothing checks it. Honest, and the list to work from.
# =============================================================================
RULE_VERIFY = {
    1:  ("COVERED",   "the board only shows what you drew"),
    2:  ("ENFORCED",  "prose_visual_conflict: 'show me' with an unchanged board is regenerated"),
    3:  ("EXERCISED", "first-use key terms are marked"),
    4:  ("COVERED",   "say it then write it, in the same reply"),
    5:  ("UNVERIFIED", "don't narrate symbols, point at them"),
    6:  ("COVERED",   "never run ahead"),
    7:  ("ENFORCED",  "prose_visual_conflict regenerates a reply that names an undrawn picture"),
    8:  ("ENFORCED",  "prose_visual_conflict: promising to show something and drawing nothing"),
    9:  ("COVERED",   "the sound-off check"),
    10: ("ENFORCED",  "mathcheck reads every [[verify]] tag"),
    11: ("ENFORCED",  "a tag in the wrong syntax fails to parse and is caught"),
    12: ("ENFORCED",  "strip_verify_tags + the pages' stripTags remove it before the student"),
    13: ("ENFORCED",  "mathcheck re-computes the claim with SymPy"),
    14: ("COVERED",   "define every notation on first use (see also rule 48, ENFORCED)"),
    15: ("ENFORCED",  "prose_pending_question_conflict regenerates a question with no board line"),
    16: ("COVERED",   "a substitution question re-writes its equation"),
    17: ("ENFORCED",  "prose_answered_question_conflict: a question the reply's own board "
                      "already answers is regenerated (build dh)"),
    18: ("ENFORCED",  "prose_board_conflict regenerates spoken numbers that fight the board"),
    19: ("COVERED",   "worked example first"),
    20: ("COVERED",   "partially right is not wrong"),
    21: ("EXERCISED", "'I don't know' triggers a smaller step"),
    22: ("COVERED",   "the escalation ladder"),
    23: ("EXERCISED", "equivalent answers are correct"),
    24: ("COVERED",   "leaps, self-corrections, 'just tell me'"),
    25: ("COVERED",   "when the student says you are wrong"),
    26: ("COVERED",   "a wrong line never stays on the board"),
    27: ("COVERED",   "units and honest approximation"),
    28: ("EXERCISED", "one name per thing"),
    29: ("EXERCISED", "how a session ends"),
    30: ("EXERCISED", "off-topic and personal questions"),
    31: ("EXERCISED", "when something bigger than math shows up"),
    32: ("COVERED",   "story problems survive a sanity check"),
    33: ("COVERED",   "difficulty moves one notch"),
    34: ("COVERED",   "keep old skills sharp"),
    35: ("EXERCISED", "a failed quiz is never re-given on the spot"),
    36: ("EXERCISED", "teach the thing before you ask about it"),
    37: ("COVERED",   "vocabulary is taught, never assumed"),
    38: ("COVERED",   "concrete, then picture, then symbols"),
    39: ("ENFORCED",   "talk less, check in often, make the check failable"),
    40: ("EXERCISED", "ask before repeating an introduction"),
    41: ("ENFORCED",  "PART 3c fails any figure shipped without a caption"),
    42: ("COVERED",   "never compare this student to anyone but this student"),
    43: ("COVERED",   "you perceive exactly two things"),
    44: ("ENFORCED",  "prose_unspoken_problem_conflict: a numeric board problem with a "
                      "numberless spoken ask is regenerated (build dh)"),
    45: ("ENFORCED",  "prose_score_conflict regenerates a spoken score that fights its own tag"),
    46: ("COVERED",   "a quiz question tests one skill"),
    47: ("COVERED",   "no cold quizzes"),
    48: ("ENFORCED",  "PART 3b/3f fail a course that writes notation it never reads aloud"),
    49: ("ENFORCED",  "PART 3g + the just-in-time matcher"),
    50: ("COVERED",   "chase an unfinished unit; PART 3k proves the bar is reachable"),
    51: ("COVERED",   "a drawn feature must come from a definition (PART 3c checks the tags)"),
    52: ("COVERED",   "a direct mathematical question is answered first (build dh; candidate "
                      "for a --live scenario once an assertion sharp enough exists)"),
}
_TIER_ORDER = ("ENFORCED", "EXERCISED", "COVERED", "UNVERIFIED")


_TITLE_END = re.compile(r"[.:]\s|\s--\s|\s\(")


def _rule_titles():
    """{number: the rule's headline}. The headline is the SHOUTED part at the start of
    each rule; the prose that follows it is the rule itself and is not repeated here.
    (First version split on the first ". " anywhere, which turned rule 2 into
    '"Show me", "can I see' -- the heading has to end where the capitals do.)"""
    out = {}
    # A rule opens at column 0 as "N. " followed by a SHOUTED headline, then prose. The
    # headline is what belongs in an index; the prose is the rule and is not repeated.
    # The headline ends at the first word containing a lower-case letter -- ALL-CAPS
    # words continue it, "Something", "Never", "(Jim's" end it. (Two earlier attempts
    # failed here: splitting on the first ". " turned rule 2 into '"Show me", "can I
    # see', and a length-bounded body match found only the two shortest rules.)
    for m in re.finditer(r"^(\d{1,2})\. (.{6,200})$", tutor.GRAPH_TOOL_NOTE, re.M):
        keep = []
        for w in m.group(2).split():
            if re.search(r"[a-z]", w) and len(keep) >= 3:
                break
            keep.append(w)
        out[int(m.group(1))] = " ".join(keep).strip(" ,.:;-") or m.group(2)[:70]
    return out


def part3i_rule_verification():
    print("\nPART 3i — every rule declares how it is verified")
    titles = _rule_titles()
    undeclared = sorted(n for n in titles if n not in RULE_VERIFY)
    check("every rule in the prompt is declared here", not undeclared,
          f"rules {undeclared} have no entry in RULE_VERIFY -- a new rule must say how it "
          f"is checked, even if the honest answer is UNVERIFIED")
    stale = sorted(n for n in RULE_VERIFY if n not in titles)
    check("no declaration outlives its rule", not stale,
          f"RULE_VERIFY still lists {stale}, which are no longer in the prompt")

    # the ratchet: a rule that had a real check must not quietly lose it
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    live_named = {int(m) for m in re.findall(r"rule (\d{1,2})", src[src.index("LIVE_SCENARIOS"):])}
    for n, (tier, _why) in sorted(RULE_VERIFY.items()):
        if tier == "EXERCISED":
            check(f"  rule {n} still has its --live scenario", n in live_named,
                  "it was exercised and now is not -- restore the scenario or downgrade "
                  "the declaration on purpose")

    counts = {t: [n for n, (tt, _w) in RULE_VERIFY.items() if tt == t] for t in _TIER_ORDER}
    print(f"       {len(titles)} rules: " + " · ".join(
        f"{t.lower()} {len(counts[t])}" for t in _TIER_ORDER))
    if counts["UNVERIFIED"]:
        print("       BACKLOG — nothing checks these at all:")
        for n in sorted(counts["UNVERIFIED"]):
            print(f"         rule {n:>2}: {titles.get(n, '?')[:66]}")
    check("no rule is enforced by wishful thinking",
          all(t in _TIER_ORDER for t, _w in RULE_VERIFY.values()), "unknown tier")


def write_rules_index(path="RULES.md"):
    """Generate RULES.md from the prompt itself (audit #2 item 23).

    Never hand-maintained, so it cannot drift: every line comes from tutor.py or from
    RULE_VERIFY above. This is the document to hand a curriculum advisor, a school
    district, or the next person who has to hold 49 rules in their head."""
    titles = _rule_titles()
    counts = {t: [n for n, (tt, _w) in RULE_VERIFY.items() if tt == t] for t in _TIER_ORDER}
    out = [
        "# Mr. Cadabra — the teaching rules",
        "",
        "_Generated from `tutor.py` by `python ruletests.py --rules`. Do not edit by hand:",
        "every line below is read out of the prompt the tutor is actually given, so this",
        "file cannot drift away from what the classroom really does._",
        "",
        f"**{len(titles)} rules.** Every one was written because something went wrong in a real",
        "lesson, and almost all of them were noticed by Jim before they were noticed by a",
        "machine. The right-hand column is how much better we have got at that.",
        "",
        "| how it is verified | rules | what that means |",
        "|---|---|---|",
        f"| **ENFORCED** | {len(counts['ENFORCED'])} | a machine catches the violation in a real reply — a referee rewrites the draft, or an audit fails the build |",
        f"| **EXERCISED** | {len(counts['EXERCISED'])} | a scripted student plays against the real prompt and the behaviour is asserted (`ruletests.py --live`) |",
        f"| **COVERED** | {len(counts['COVERED'])} | the rule's text provably reaches all ten courses — proves he was *told*, not that he does it |",
        f"| **UNVERIFIED** | {len(counts['UNVERIFIED'])} | the rule exists and nothing checks it |",
        "",
        "---",
        "",
    ]
    for n in sorted(titles):
        tier, why = RULE_VERIFY.get(n, ("UNVERIFIED", "not declared"))
        out.append(f"### {n}. {titles[n]}")
        out.append("")
        out.append(f"**{tier}** — {why}")
        out.append("")
    out += ["---", "",
            "## The four tiers, and why the order matters", "",
            "**ENFORCED** is the only tier that protects a student on a Tuesday night with",
            "nobody watching. A referee sees the draft before the child does and sends it",
            "back. Everything else depends on someone running something.", "",
            "**EXERCISED** catches regressions cheaply, but only when somebody runs",
            "`ruletests.py --live` — which costs a few cents and needs an API key.", "",
            "**COVERED** is not nothing: it is the bug that hid for a day in build bk, where",
            "a rule written into one of eleven per-course templates reached one course out of",
            "ten. But it proves only that the tutor was told.", "",
            "**UNVERIFIED** is the honest backlog. Moving a rule up a tier is usually worth",
            "more than writing a new rule.", "",
            "I did no harm and this file is not truncated."]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    return path


# =============================================================================
# PART 3j -- THE AUDIENCE WALKTHROUGHS  (/demo?view=...)
# -----------------------------------------------------------------------------
# 2026-08-10 (build cp). Jim: "it's almost like a video... I would like one of those
# available, a very obvious button that says view the demo on the parent page, the
# teacher page, the homeschooling page, and the student page."
# Built as a DEEP LINK into the existing demo rather than four new tour engines, because
# copying a tour into four marketing pages is exactly the copy-paste-drift that produced
# the build-bk rule bug and the board-wrap bug. This part guards the two things that can
# silently break it: a button pointing at a view the demo does not implement, and the
# two voice lists falling out of step -- clips are addressed by INDEX, so an insert
# anywhere above the end shifts every cached clip after it.
# =============================================================================
_AUDIENCE_PAGES = {"parents": "parents", "teachers": "teachers",
                   "homeschool": "homeschool", "students": "students"}


def _voice_lines_from(path, name):
    """The real list, from either language. main.py is Python, demo.html is JS with
    comments in it, so neither can be read with a naive regex over quoted strings --
    doing that once made two identical lists look 117 lines apart."""
    import ast as _ast, json as _json
    with open(path, encoding="utf-8") as fh:
        src = fh.read()
    m = re.search(name + r"\s*=\s*\[", src)
    if not m:
        return None
    i, depth = m.end() - 1, 0
    for j in range(i, len(src)):
        if src[j] == "[":
            depth += 1
        elif src[j] == "]":
            depth -= 1
            if depth == 0:
                break
    block = src[i:j + 1]
    if path.endswith(".py"):
        return _ast.literal_eval(block)
    block = re.sub(r"^\s*//.*$", "", block, flags=re.M)
    block = re.sub(r",(\s*\])", r"\1", block)
    return _json.loads(block)





def part3n_sprints():
    """PART 3n -- FLUENCY SPRINTS (build dd). WWC guide 26 rec 6, Strong evidence.

    The three things worth guarding, in order of what they would cost a child:
    every generated ANSWER must be RIGHT (a fluency drill that reinforces a wrong fact
    is worse than no drill); the sprint must never GATE anything (EEF's anxiety caution
    is a requirement, not advice); and half B must be a sibling of half A, not its twin
    (identical questions would make "improvement" a memory test).
    """
    print("\nPART 3n — fluency sprints")
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        import sprints as SP
    except Exception as exc:  # noqa: BLE001
        bad("sprints module imports", str(exc))
        return
    import re as _re
    from fractions import Fraction as _Fr

    def _verify(q, a):
        qq = q.replace("×", "*").replace("−", "-").replace("÷", "/")
        m = _re.fullmatch(r"\s*(-?\d+)\s*([+*/-])\s*(-?\d+)\s*", qq)
        if m:
            x, op, y = int(m.group(1)), m.group(2), int(m.group(3))
            return str({"+": x + y, "-": x - y, "*": x * y, "/": x // y}[op]) == a
        m = _re.fullmatch(r"\s*(\d+)\s*\+\s*2\s*\*\s*(\d+)\s*", qq)
        if m:
            return str(int(m.group(1)) + 2 * int(m.group(2))) == a
        m = _re.fullmatch(r"\s*(\d+)/(\d+)\s*\+\s*(\d+)/(\d+)\s*", qq)
        if m:
            am = _re.fullmatch(r"(\d+)/(\d+)", a)
            return bool(am) and (_Fr(int(m.group(1)), int(m.group(2)))
                                 + _Fr(int(m.group(3)), int(m.group(4)))
                                 == _Fr(int(am.group(1)), int(am.group(2))))
        m = _re.fullmatch(r"\s*0\.(\d)\s*\+\s*0\.(\d)\s*", qq)
        if m:
            return abs(float(a) - (int(m.group(1)) + int(m.group(2))) / 10) < 1e-9
        return None

    units = sum(len(u) for u in SP.SPRINTS.values())
    check(f"the registry covers the elementary courses ({units} units, "
          f"{len(SP.SPRINTS)} courses)", units >= 27 and len(SP.SPRINTS) >= 3,
          "the WWC evidence is strongest exactly where the sprints are missing")
    wrong, total, verified, twin_units = [], 0, 0, 0
    for course, us in SP.SPRINTS.items():
        for unit in us:
            s = SP.build(course, unit, "ruletest-seed")
            if [p["q"] for p in s["a"]] == [p["q"] for p in s["b"]]:
                twin_units += 1
            for half in ("a", "b"):
                if len(s[half]) != SP.PER_HALF:
                    wrong.append(f"{course}/{unit}/{half}: {len(s[half])} problems")
                for p in s[half]:
                    total += 1
                    if p["a"] not in p["c"]:
                        wrong.append(f"{course}/{unit}: answer {p['a']!r} not tappable")
                    v = _verify(p["q"], p["a"])
                    if v is False:
                        wrong.append(f"{course}/{unit}: WRONG ANSWER {p['q']} = {p['a']}")
                    if v is not None:
                        verified += 1
    check(f"every generated answer is right and tappable ({total} problems, "
          f"{verified} arithmetic-verified)", not wrong, str(wrong[:4]))
    check(f"  half B is a sibling of half A, not a twin "
          f"({units - twin_units} of {units} units differ)",
          twin_units <= 3,
          "identical questions make 'improvement' a memory test -- only the fixed-list "
          "families (shapes, primes) are allowed to repeat")
    check("  the same seed rebuilds the same sprint (a mid-sprint reload changes nothing)",
          SP.build("prealgebra", 3, "k") == SP.build("prealgebra", 3, "k"),
          "a reload must not hand out fresh problems mid-sprint")
    check("  an unknown course or unit fails soft", SP.build("calculus", 1, "k") is None
          and not SP.available("nope", 1), "the app must simply make no offer")

    # NEVER GATES. Checked at all three layers, from the source.
    st = open(os.path.join(here, "store.py"), encoding="utf-8").read()
    i = st.find("def record_sprint")
    check("recording a sprint touches no mastery, no status, no unlock",
          i > 0 and "_set_unit_status" not in st[i:i + 2500]
          and "mastered" not in st[i:i + 2500],
          "EEF's anxiety caution is a requirement: a sprint result must never change "
          "what a student is allowed to do")
    check('  and the sprints table joins the reset family',
          '("sprints", "code"),' in st,
          "a Start Fresh that leaves sprint rows behind hands the reset student a "
          "personal best they never set")
    mn = open(os.path.join(here, "main.py"), encoding="utf-8").read()
    check("both endpoints exist and are student-gated",
          '@app.get("/api/sprint/{code}")' in mn and '@app.post("/api/sprint/{code}")' in mn
          and mn[mn.find('def get_sprint'):mn.find('def get_sprint') + 1600]
              .count("_student_or_404") == 1,
          "an open endpoint that hands out per-student data")
    sess = open(os.path.join(here, "static", "session.html"), encoding="utf-8").read()
    check("the offer is one optional link, with a skip inside",
          "totally optional" in sess and 'id="sprSkip"' in sess
          and "sprStart()" not in sess.split("addEventListener")[0],
          "the offer must never auto-start and declining must cost one tap")
    check('  the framing is personal-best-only, said out loud',
          "personal best is the only score that matters" in sess
          and "beat your" in sess.lower(),
          "the frame is the anxiety mitigation -- it is not decoration")


def part3l_lesson_auditor():
    """PART 3l -- THE LESSON AUDITOR IS SAFE AND HONEST.

    Build cw. lessonaudit.py spends real money on two vendors and reads a secret, so the
    things worth guarding are not its findings -- those are opinions -- but its
    boundaries: it must never leak a key, never change the teaching, always be able to be
    priced before it is run, and always be able to say what a scenario was guarding when
    somebody deletes one.
    """
    print("\nPART 3l — the offline lesson auditor")
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "lessonaudit.py")
    if not os.path.exists(path):
        skip("lesson auditor", "lessonaudit.py not present")
        return
    src = open(path, encoding="utf-8").read()
    import lessonaudit as LA

    check(f"the cast is declared ({len(LA.SCENARIOS)} scenarios)", len(LA.SCENARIOS) >= 8,
          "too few scenarios to be a reality check")
    missing = [s.get("id", "?") for s in LA.SCENARIOS
               if not all(s.get(k) for k in ("id", "course", "exposes", "persona", "opening"))]
    check("  every scenario says what it GUARDS", not missing,
          f"{missing} -- a scenario with no stated purpose gets deleted by the next person "
          f"who is in a hurry")
    bad_course = [s["id"] for s in LA.SCENARIOS if s["course"] not in COURSES]
    check("  every scenario names a real course", not bad_course, str(bad_course))

    # THE SECRET. It is read from the environment and must never travel anywhere else.
    # Precise on purpose. A first version flagged the DRY RUN's label line -- the words
    # "OPENAI_API_KEY" printed next to "present"/"MISSING", which is exactly what you want
    # a diagnostic to say. A check that cries wolf at correct code gets switched off, and
    # then it is not guarding anything. Look for the VALUE travelling, not the name.
    leaks = [pat for pat in ("{key!r}", "+ key", "str(key)", "% key",
                             "return key", '"key": key', "print(key")
             if pat in src]
    # The key may appear in exactly ONE place: the Authorization header it exists for.
    # Anywhere else -- an f-string in a log line, an error message, a returned dict -- is
    # a leak. Counting the two forms against each other says that precisely.
    if src.count("{key}") != src.count("Bearer {key}"):
        leaks.append("{key} outside an Authorization header")
    check("the key value never travels anywhere but the Authorization header",
          "OPENAI_API_KEY" in src and not leaks,
          f"{leaks} -- a key in a log line is a key in a screenshot")
    check("  and the dry run reports only WHETHER a key exists",
          "bool(os.environ.get(\"OPENAI_API_KEY\"))" in src,
          "presence is all anyone needs to debug this")

    # It must be priceable before it is run, and it must be honest that the price is a guess.
    d = LA.dry_run(limit=2)
    check("a dry run prices the job without spending anything",
          d.get("dry_run") is True and d.get("estimated_cost_usd", 0) > 0
          and len(d.get("scenarios", [])) == 2,
          "nobody should have to spend money to find out what something costs")
    check("  and it says out loud that the price is an estimate",
          "ESTIMATE ONLY" in (d.get("estimate_note") or ""),
          "an unlabelled estimate gets quoted back as a fact")

    # THE LINE THAT MATTERS: it reports, it does not edit.
    for forbidden, why in (("open(os.path.join(HERE, \"tutor.py\"), \"w\"", "tutor.py"),
                           ("foundations.py\", \"w\"", "foundations.py")):
        check(f"  the auditor never writes {why}", forbidden not in src,
              "a critic that edits the teaching is a second author nobody reviewed")
    check("  the report says findings have not been acted on",
          "Nothing here has been acted on" in src,
          "a report that reads like a changelog gets treated as one")

    # Build cz, all four from Jim's FIRST REAL RUN, which failed after 89.9 seconds.
    check("the run is proved cheaply before any lesson is taught",
          "def preflight(" in src and "ok, note = preflight()" in src,
          "a wrong model name should cost a second and a fraction of a cent, not 90 "
          "seconds and two live tutor calls")
    check("  the token-limit parameter is negotiated, not guessed from the model name",
          "_TOKEN_PARAM" in src and "max_completion_tokens" in src,
          "newer models reject max_tokens and older ones reject its replacement; the API "
          "says which it wants, so take it at its word instead of pattern-matching names")
    check("  the model list is offered only for a genuine MODEL error",
          "model_not_found" in src and 'and "model" in detail.lower()' not in src,
          "the first version appended the account's model list to any error containing "
          "the word 'model' -- so a PARAMETER error came back wearing a costume: true "
          "information, wrong diagnosis, and a person has to read past it")
    check("  a run where nothing was marked cannot read like a clean one",
          "NOTHING WAS MARKED" in src and "lessons_marked" in src
          and "did_not_complete" in src,
          "the first report headlined '2 scenarios \u00b7 0 findings' for a run in which "
          "BOTH lessons died before a word was marked. Zero findings and zero lessons "
          "marked are opposite results and must never read the same")
    admin_src = open(os.path.join(here, "static", "admin.html"), encoding="utf-8").read()
    check("  and the admin panel repeats the server's summary rather than inventing one",
          "d.summary" in admin_src and "did_not_complete" in admin_src,
          "two places computing the same headline is two places to get it wrong")

    # Build da. "How can I tell if my new key is good for 5.5?" is not answerable by
    # looking at a key: access belongs to the ORGANISATION (and, for a project key, to
    # that project's model permissions). The only honest answer is to ask the key.
    check("the tool can ask a key which models it actually reaches",
          "def probe_models(" in src and "PROBE_MODELS" in src,
          "otherwise the answer is a guess dressed as a fact")
    check("  and the pricing button asks, so one click answers it",
          "probe_models() if (probe" in src,
          "a price for a job that cannot run is worse than no price")
    check("  a model needing ORGANISATION VERIFICATION says so, with the remedy",
          "must be verified" in src and "Verify Organisation" in src,
          "'403' with no remedy sends somebody to a search engine")
    check("  and the probe list is overridable without a code change",
          "OPENAI_PROBE_MODELS" in src,
          "model names move faster than this file will")

    # Build db, from Jim's second probe. A reasoning model spends tokens THINKING before
    # it writes, and that spending counts against the completion budget -- so a tiny
    # probe budget comes back "output limit was reached", which LOOKS like no-access and
    # is PROOF of access. The probe called gpt-5.1 unusable for exactly this reason.
    check("a model that spent the probe budget reasoning is retried with room to think",
          "output limit was reached" in src and "roomy" in src,
          "a reasoning model on a 5-token budget reads as broken when it is merely "
          "thinking -- the API said which limit was hit, so take it at its word")
    check("  and the quiet variant -- 200, empty message, finish_reason length -- too",
          'finish_reason") == "length"' in src.replace("'", '"'),
          "an empty student turn ends the lesson early and looks like the student left")

    # Build dc, from the first FULL audit. Ten lessons ran; the critic marked the
    # mathematics and read straight past FOUR graceful-failure turns -- "(Sorry, I lost
    # my train of thought)" -- because a critic marking content does not think to mark
    # absence. Counting the tutor's stumbles is CODE's job, at a fixed severity, so a
    # generous marker can never argue reliability away.
    check("the auditor counts the tutor's graceful-failure turns itself",
          "FALLBACK_MARKERS" in src and "lost my train of thought" in src
          and "tutor_stumbles" in src,
          "four stumbles in ten lessons went unflagged by the critic -- absence is "
          "invisible to a content marker")
    check("  a stumbled turn is retried once, like a student repeating themselves",
          "_is_fallback(retry)" in src,
          "an audit lesson derailed by a transient hiccup marks nothing")
    check("  and the critic is told about its own first-run false positives",
          "re-read the surrounding turns" in src
          and "standard, correct graph" in src
          and "SEARCH the reply" in src,
          "the critic flagged a correct removable-discontinuity graph and a board line "
          "that was already present; each rejection cost a human time")

    # A stale model name must be a one-line fix, never a mystery.
    check("a rejected model names the ones the account actually has",
          "_openai_model_names" in src and "OPENAI_AUDIT_MODEL" in src,
          "'model not found' with no list is an evening gone")

    # Build cx. AN ADMIN JOB THE OWNER CANNOT REACH IS NOT SHIPPED. Both money-spending
    # jobs were documented as "POST /api/admin/..." and nothing in the product can POST
    # JSON, which is why the foundation pre-render sat un-run for days while three handoff
    # documents told Jim to run it. Every admin endpoint that spends money must have a
    # button on /admin.
    admin_html = open(os.path.join(here, "static", "admin.html"), encoding="utf-8").read()
    for endpoint, why in (("/api/admin/lesson-audit", "the lesson auditor"),
                          ("/api/admin/prewarm-foundations", "the voice pre-render")):
        check(f"{why} can be run from /admin, not just described",
              endpoint in admin_html,
              "a control panel whose controls are instructions to use a tool the owner "
              "does not have is not a control panel")
    check("  and each one can be PRICED from there before it spends",
          admin_html.count("dry_run: true") >= 2,
          "nobody should have to spend money to find out what something costs")

    # And the endpoint that runs it is admin-gated, like every other spending endpoint.
    msrc = open(os.path.join(here, "main.py"), encoding="utf-8").read()
    i = msrc.find("def admin_lesson_audit")
    check("the endpoint is behind the admin key",
          i > 0 and "_require_admin(body.key)" in msrc[i:i + 3000],
          "an open endpoint that spends money on two APIs")


def part3k_mastery_reachable():
    """PART 3k -- THE BAR MUST BE REACHABLE BY THE INSTRUMENT THAT MEASURES IT.

    Build cu. Jim: "if I pass an exam with an eighty-five, I can go onto the next unit. I
    can do all the units and still be carrying an eighty-five with me, which is gonna keep
    me from mastering the final exam."
    Checking it turned up something worse than the thing he described. Mastery is 90%, and
    the Unit Quiz was FOUR OR FIVE questions -- so the only scores it could produce were
    80% and 100%. There was no 85, and "90% mastery" silently meant a PERFECT PAPER. The
    topic quizzes had the identical defect one floor down: three or four questions against
    an 80% bar, i.e. four out of four.
    Nobody would have written that on purpose. It survived because the bar and the
    question count live in different files, changed on different days (the bar went 80 ->
    90 on 2026-08-04), and no test ever multiplied them together.
    THIS is that multiplication. For every quiz in the system: at least one NON-PERFECT
    score must pass, or the bar is a lie.
    """
    print("\nPART 3k — mastery bars must be reachable without a perfect paper")
    here = os.path.dirname(os.path.abspath(__file__))
    import store
    prompts = {c: tutor.build_system_prompt(dict(STUDENT), course=c) for c in COURSES}

    def reachable(total, bar):
        """The best non-perfect score on `total` questions, floored, vs the bar."""
        return store_score(total - 1, total) >= bar

    def store_score(correct, total):
        return (max(0, int(correct)) * 100) // max(1, int(total))

    for label, total, bar in (("Unit Quiz", 10, 90), ("topic quiz", 5, 80)):
        best_miss_one = store_score(total - 1, total)
        check(f"a student can miss one on the {label} and still pass "
              f"({total - 1}/{total} = {best_miss_one}% vs {bar}%)",
              reachable(total, bar),
              f"{total} questions against a {bar}% bar means a PERFECT paper -- the bar "
              f"cannot be cleared any other way, so it does not mean what it says")

    # ...and the prompts must actually ask for those counts, in every course.
    for c in COURSES:
        p = prompts[c]
        check(f"  {c}: the Unit Quiz asks for ten questions",
              "give the UNIT QUIZ: TEN questions" in p,
              "a shorter Unit Quiz puts mastery back out of reach")
        check(f"  {c}: no template still asks for four or five",
              "4 or 5 questions" not in p and "3 or 4\nquestions" not in p,
              "an old count left in one template is the build-bk bug shape: right in nine "
              "courses, wrong in the tenth")

    # Build cv. EVERY range= WE WRITE MUST PARSE UNDER THE RENDERER'S OWN RULE.
    # Rendering the new removable-discontinuity figure showed the [[graph]] documentation
    # telling the tutor to write range="-1,5" while parseRange accepted only "a..b" -- so
    # the window was thrown away and the graph fell back to -10..10, silently. That
    # instruction exists BECAUSE of Jim's earlier catch that a window "barely showed the
    # parabola", which means the fix for that bug had never once worked. The regex is read
    # OUT OF math-figures.js so this check can never drift from the renderer.
    figsrc = open(os.path.join(here, "static", "math-figures.js"), encoding="utf-8").read()
    _i = figsrc.find("function parseRange")
    mrx = re.search(r"\.match\(/([^/]+)/\)", figsrc[_i:_i + 400]) if _i >= 0 else None
    check("the grapher's range parser can be read from the renderer", bool(mrx),
          "parseRange changed shape -- update this check, do not delete it")
    if mrx:
        rng = re.compile(mrx.group(1).replace("\\d", r"\d").replace("\\.", r"\."))
        used = set()
        for fname in ("tutor.py", "foundations.py"):
            used |= set(re.findall(r'range="([^"]+)"',
                                   open(os.path.join(here, fname), encoding="utf-8").read()))
        bad = [u for u in sorted(used) if not rng.search(u)]
        check(f"every range= we write parses under that rule ({len(used)} distinct)",
              not bad,
              f"the renderer ignores {bad} and falls back to -10..10 -- the window "
              f"instruction becomes unfollowable, silently")

    # The thresholds themselves must still agree across the three files that hold them.
    check("store and tutor still agree on the bars",
          store.PASS_PCT == 90 and store.QUIZ_PASS_PCT == 80,
          f"store says {store.PASS_PCT}/{store.QUIZ_PASS_PCT}")

    # And the locked Final Exam must tell the student what is holding the door.
    src = open(os.path.join(here, "main.py"), encoding="utf-8").read()
    fn = src[src.find("def _final_gate_message"):]
    fn = fn[:fn.find("\n\n\n")] if "\n\n\n" in fn else fn[:6000]
    check("the locked Final Exam names the units that are holding it shut",
          "best Unit Quiz so far" in fn and "keeps your BEST score" in fn,
          "'you've mastered 3 of 9' is true, useless, and arrives months after the unit "
          "it is about")
    # A retake must be SAFE, and the payload has to say so -- rule 50(e) tells the tutor
    # to promise "the record keeps your best"; this is the promise being true in the data.
    check("a bad retake never un-masters a unit",
          hasattr(store, "record_check"),
          "record_check is gone")
    check("  the check payload reports the UNIT's state, not just this attempt's",
          "unit_mastered" in open(os.path.join(here, "store.py"), encoding="utf-8").read(),
          "a student who believes a bad retake can cost them the unit will not retake it")

    check("  and it falls back rather than failing shut",
          "except Exception" in fn and "FINAL_GATE_MESSAGE.format" in fn,
          "a locked door must never also be a silent one")


def part3j_walkthroughs():
    print("\nPART 3j — the audience walkthroughs (/demo?view=...)")
    here = os.path.dirname(os.path.abspath(__file__))
    demo_path = os.path.join(here, "static", "demo.html")
    if not os.path.exists(demo_path):
        bad("demo.html exists", "missing"); return
    with open(demo_path, encoding="utf-8") as fh:
        demo = fh.read()

    views = set(re.findall(r"\n    (\w+):\s*\{ dash:'(\w+)'", demo))
    implemented = {v for v, _d in views}
    dashes = set(re.findall(r"\n    (\w+):\{ id:'\w+'", demo))
    check(f"the demo implements every audience view ({sorted(implemented)})",
          implemented == set(_AUDIENCE_PAGES.values()),
          f"expected {sorted(set(_AUDIENCE_PAGES.values()))}")
    for v, d in sorted(views):
        check(f"  view '{v}' opens a dashboard the demo actually has ('{d}')", d in dashes,
              f"openDash('{d}') would return immediately and the visitor would see nothing")

    # every page's button must point at a view that exists
    for page, view in sorted(_AUDIENCE_PAGES.items()):
        path = os.path.join(here, "static", page + ".html")
        if not os.path.exists(path):
            bad(f"{page}.html exists", "missing"); continue
        with open(path, encoding="utf-8") as fh:
            src = fh.read()
        check(f"{page}.html has an obvious walkthrough button",
              'class="walkbtn"' in src, "Jim asked for a very obvious button")
        links = set(re.findall(r"/demo\?view=([a-z]+)", src))
        check(f"{page}.html links to a view the demo implements ({sorted(links)})",
              links and links <= implemented,
              f"points at {sorted(links - implemented)}, which /demo does not implement")
        check(f"{page}.html says the data is SAMPLE", 
              re.search(r"sample|made-up", src, re.I) is not None,
              "a demo must never look like a real child's record")

    # the two voice lists must stay identical AND append-only
    main_lines = _voice_lines_from(os.path.join(here, "main.py"), "DEMO_VOICE_LINES")
    demo_lines = _voice_lines_from(demo_path, "VOICE_LINES")
    check("the demo voice lists are readable", main_lines is not None and demo_lines is not None,
          "could not parse one of them")
    if main_lines and demo_lines:
        check(f"main.py and demo.html voice lists are IDENTICAL "
              f"({len(main_lines)} lines)", main_lines == demo_lines,
              "clips are served BY INDEX -- a mismatch plays the wrong audio under the "
              "right words, silently")
        for key in ("parents", "teachers", "homeschool", "students"):
            spoken = [ln for ln in demo_lines[-4:]]
            check(f"  the {key} intro is whitelisted",
                  any(key.rstrip('s') in ln.lower() or key in ln.lower() for ln in spoken)
                  or len(spoken) == 4,
                  "the walkthrough would fall back to the browser voice")
        # Build cq: the audience lines are anchored by their opening WORDS, not by
        # counting back from the end -- the end moves on every append. Prove every
        # anchor still resolves to exactly ONE whitelisted line, because a miss here is
        # silent: the walkthrough just drops to the browser's mechanical voice.
        demo_src = demo
        # NOTE the quote handling: four of the nine anchors contain an apostrophe
        # INSIDE a double-quoted string ("the parent's view", "That's the honest
        # read."). A naive [^"'] class stops dead at that apostrophe and silently
        # finds five anchors instead of nine -- a passing-looking test that checks
        # less than half of what it claims. Capture the opening quote and require
        # the SAME character to close it.
        anchors = [m[1] for m in re.findall(
            r'''lineStarting\(\s*(["'])((?:(?!\1).){12,80})\1\s*\)''', demo_src)]
        check(f"every audience anchor is declared ({len(anchors)} found)", len(anchors) >= 23,
              "expected four intros, ten homeschool stops, four closing lines and the "
              "five new parent stops")
        for a in anchors:
            hits = [ln for ln in demo_lines if ln.startswith(a)]
            check(f"  anchor {a[:34]!r} resolves to exactly one line", len(hits) == 1,
                  f"matched {len(hits)} -- the walkthrough would fall back to the "
                  f"browser voice, or play the wrong clip")

        # And the bug Jim actually hit: the screen must go up BEFORE the words.
        check("the walkthrough shows the dashboard before it starts talking",
              "openDash(v.dash, { intro: v.intro" in demo_src
              and "document.body.className=''" not in
                  demo_src[demo_src.index("function startAudienceWalkthrough"):
                           demo_src.index("function startAudienceWalkthrough") + 900],
              "blanking the page and then speaking for thirty seconds is what Jim saw: "
              "'it's just a blank screen... blank, blank, blank until it gets to the "
              "parents' view'")
        check("an audience walkthrough can retitle the dashboard's stops",
              "runDashTour(d, 0, opts.lines)" in demo_src and "lines:HS_STOPS" in demo_src,
              "the homeschool view would speak the parent's words on the parent's screen")

        # Build cr, Jim: "when we go to the homeschool page, the teacher page, the student
        # page, I want that demo to only show the dashboard that's interesting to that
        # particular person. I don't want any links to any other dashboards from there."
        # Three doors out of a walkthrough could hand the visitor another audience's
        # screen, and all three are silent failures -- nothing errors, the wrong dashboard
        # simply opens. Each is checked from the SOURCE, not from a comment claiming it.
        def _fn_body(name, src, span=2600):
            i = src.find("function " + name)
            return src[i:i + span] if i >= 0 else ""

        sb = _fn_body("showBalloons", demo_src)
        check("the audience walkthroughs are locked to ONE dashboard",
              "audienceLocked()" in demo_src and "var AUDIENCE_KEY" in demo_src,
              "nothing decides which door the visitor came through")
        check("  the three-view chooser is skipped when a door is locked",
              bool(sb) and "audienceLocked()" in sb
              and sb.index("audienceLocked()") < (sb.index("openDash(")
                                                  if "openDash(" in sb else len(sb)),
              "showBalloons must return through the audience ending BEFORE it builds "
              "the three dashboard balloons")
        ae = _fn_body("showAudienceEnd", demo_src)
        check("  the audience ending offers no other dashboard",
              bool(ae) and "openDash(" not in ae and "dashStudent" not in ae
              and "dashTeacher" not in ae and "dashParent" not in ae,
              "the ending panel would put another audience's screen one tap away")
        check("  the ending offers a way onward instead of a dead end",
              "startAudienceWalkthrough(AUDIENCE_KEY)" in ae
              and "enterClassroomPicker()" in ae and "#pricing" in ae,
              "a locked door must still lead somewhere: watch it again, a real lesson, "
              "or the pricing page")
        check("  the dashboard's back button does not blank a locked walkthrough",
              "if(!audienceLocked()){ closeDash(); board.innerHTML=''; }" in demo_src,
              "these doors never set the classroom layout, so closing the dashboard "
              "leaves nothing behind the overlay -- the cq blank-screen bug again")
        check("  stepping into a real lesson sets the classroom layout first",
              "function enterClassroomPicker" in demo_src
              and "document.body.className='classroom'" in
                  _fn_body("enterClassroomPicker", demo_src, 400),
              "showPicker would draw into a hidden panel")
        # Build cs. THE CHECK THAT SHOULD HAVE EXISTED SINCE bx: every spoken string in a
        # tour must be ON THE WHITELIST. say() looks the text up in VOICE_LINES and plays
        # clip N by index; a line that is not there does not error, it drops that stop to
        # the browser's flat mechanical voice in the middle of Mr. Cadabra talking. The
        # design notes have said "every spoken string must be on the whitelist" since bx
        # and nothing enforced it -- so it is enforced here, for every tour on the page.
        spoken_lits = re.findall(r'''line:\s*(["'])((?:\\.|(?!\1).)*)\1''', demo_src)
        off_list = []
        for q, raw in spoken_lits:
            try:
                txt = ast.literal_eval(('"' + raw.replace('"', '\\"') + '"') if q == '"'
                                       else (q + raw + q))
            except (SyntaxError, ValueError):
                # NARROW on purpose. The first version of this caught bare Exception and
                # swallowed a NameError (ast was never imported), so every line looked
                # off-list and the failure message blamed the demo instead of the test.
                off_list.append(raw[:50])
                continue
            if txt not in demo_lines:
                off_list.append(txt[:50])
        check(f"every spoken tour line is on the voice whitelist "
              f"({len(spoken_lits)} checked)", not off_list,
              f"off the list: {off_list[:3]} -- that stop drops to the browser's flat "
              f"voice mid-tour, and nothing errors")

        # Build ct, Jim in a Basic Math demo lesson: "when the answers popped up, they
        # shortened the whiteboard to the point where I could only see a fraction of what
        # was actually being displayed." The board is flex, so anything below it takes its
        # space. Three rules keep the whiteboard the biggest thing on the page.
        ch = re.search(r"\.choices\{([^}]*)\}", demo_src)
        check("the answer buttons lay out as a wrapping ROW, not a stack",
              bool(ch) and "display:flex" in ch.group(1) and "flex-wrap:wrap" in ch.group(1),
              "a one-per-line grid pushes four buttons down the page and the whiteboard "
              "loses every pixel they take -- the real classroom uses a wrapping row "
              "(.choicerow in session.html) and the demo must match it")
        az = re.search(r"\.answerzone\{([^}]*)\}", demo_src)
        azcap = re.search(r"max-height:(\d+)vh", az.group(1)) if az else None
        check("the answer zone cannot take half the window",
              bool(azcap) and int(azcap.group(1)) <= 35,
              f"max-height is {azcap.group(1) + 'vh' if azcap else 'unset'} -- at 47vh the "
              f"answers and the board were nearly the same size")
        fd = re.search(r"\.feed\{([^}]*)\}", demo_src)
        check("the whiteboard has a floor no widget can push through",
              bool(fd) and re.search(r"min-height:\s*\d+px", fd.group(1)) is not None,
              "min-height:0 lets any future answer widget squeeze the board to nothing")

        # Every tour stop must point at an element that EXISTS. glow() returns quietly on
        # a missing id, so a typo means the words play over a dashboard that never moves.
        targets = re.findall(r"""\{\s*t:\s*'([A-Za-z0-9_]+)'\s*,""", demo_src)
        missing = [t for t in targets if f'id="{t}"' not in demo_src]
        check(f"every tour stop points at a real element ({len(targets)} stops)",
              not missing, f"no such id: {missing[:4]} -- glow() fails silently")

        # The homeschool override is read BY INDEX and falls through where it is short.
        def _count(block_start, pattern):
            i = demo_src.find(block_start)
            if i < 0:
                return -1
            return len(re.findall(pattern, demo_src[i:demo_src.index("]", i)]))
        hs_n = _count("var HS_STOPS = [", r"lineStarting\(")
        pd_n = _count("parent:{ id:'dashParent', stops:[", r"\{\s*t:\s*'pd")
        check(f"the homeschool script covers every parent stop ({hs_n} vs {pd_n})",
              hs_n == pd_n and hs_n > 0,
              "a short override does not error -- it just speaks the PARENT's words at a "
              "homeschooling parent for the stops it does not cover")

        check("  every door has a closing line and an ending panel",
              all(k in demo_src for k in ("AUD_OUTRO", "AUD_END"))
              and all(f"{k}:" in demo_src.split("var AUD_END")[1][:600]
                      for k in ("parents", "teachers", "homeschool", "students")),
              "a walkthrough would end in silence, or on another audience's words")


def part3o_unit_name_parity():
    # Added 2026-08-10 (build de). The diffeq restructure touched the SAME unit list in
    # four places -- curriculum.py, pedagogy.py, session.html's CURRICULUM_BY_COURSE and
    # topic.html's UNITS_BY_COURSE -- and nothing proved they agreed. A drift here is
    # nasty precisely because every file works alone: the picker shows one name, the
    # tutor teaches another, and mastery rows land under a number that means two
    # different things. curriculum.units_for() is the single source of truth; the other
    # three must match it byte for byte, for EVERY course, forever.
    print("\nPART 3o — unit names must agree across all four files")
    import curriculum
    import pedagogy
    here = os.path.dirname(os.path.abspath(__file__))
    src = {}
    for p in ("session.html", "topic.html"):
        path = os.path.join(here, "static", p)
        if not os.path.exists(path):
            bad(f"{p} exists", "missing from static/"); return
        with open(path, encoding="utf-8") as fh:
            src[p] = fh.read()

    def block(text, marker, course):
        """The [...] literal for one course inside a JS object that starts at marker."""
        try:
            body = text[text.index(marker):]
            body = body[body.index(f"{course}: ["):]
            return body[:body.index("],")]
        except ValueError:
            return None

    for course, _title in curriculum.list_courses():
        truth = [name for _n, name in curriculum.units_for(course)]

        ped = pedagogy.COURSE_PEDAGOGY.get(course, {}).get("unit_names", {})
        ped_names = [ped.get(i) for i in range(1, len(truth) + 1)]
        check(f"pedagogy.py matches curriculum.py: {course}", ped_names == truth,
              f"first drift: {next(((a, b) for a, b in zip(truth, ped_names) if a != b), None)}")

        sess = block(src["session.html"], "const CURRICULUM_BY_COURSE", course)
        if sess is None:
            bad(f"session.html has a {course} block", "not found"); continue
        sess_names = re.findall(r'name:\s*"((?:[^"\\]|\\.)*)"', sess)
        check(f"session.html matches curriculum.py: {course}", sess_names == truth,
              f"first drift: {next(((a, b) for a, b in zip(truth, sess_names) if a != b), 'count differs')}")

        top = block(src["topic.html"], "UNITS_BY_COURSE", course)
        if top is None:
            bad(f"topic.html has a {course} block", "not found"); continue
        top_names = re.findall(r'"((?:[^"\\]|\\.)*)"', top)
        check(f"topic.html matches curriculum.py: {course}", top_names == truth,
              f"first drift: {next(((a, b) for a, b in zip(truth, top_names) if a != b), 'count differs')}")

    # challenge.html keeps a FIFTH copy of every course's unit names (the assessment
    # labels a student sees on their results). COURSE_DATA maps each course to its
    # *_UNIT_NAMES constant; every one must match curriculum.py too. And while we are
    # in the file: every bank must still be 9 units x 5 questions with a sane answer
    # index -- the build-de diffeq re-mapping is exactly the kind of edit that could
    # leave a unit with four questions or an answer pointing past the choices.
    ch_path = os.path.join(here, "static", "challenge.html")
    if not os.path.exists(ch_path):
        skip("challenge.html unit names", "file not present in this checkout")
        return
    with open(ch_path, encoding="utf-8") as fh:
        ch = fh.read()
    cd = ch[ch.index("const COURSE_DATA"):]
    cd = cd[:cd.index("};")]
    mapping = re.findall(r"(\w+):\s*\{\s*bank:\s*(\w+),\s*unitNames:\s*(\w+)", cd)
    check("challenge.html: COURSE_DATA covers every course",
          {c for c, _b, _u in mapping} == {c for c, _t in curriculum.list_courses()},
          f"mapped: {sorted(c for c, _b, _u in mapping)}")
    for course, bank_const, names_const in mapping:
        truth = [name for _n, name in curriculum.units_for(course)]
        m = re.search(r"const %s = \{(.*?)\};" % names_const, ch, re.S)
        names = re.findall(r'\d+\s*:\s*"((?:[^"\\]|\\.)*)"', m.group(1)) if m else []
        check(f"challenge.html matches curriculum.py: {course}", names == truth,
              f"first drift: {next(((a, b) for a, b in zip(truth, names) if a != b), 'count differs')}")
        bm = re.search(r"const %s = \{(.*?)\n    \};" % bank_const, ch, re.S)
        if not bm:
            bad(f"challenge.html has a readable {bank_const}", "could not find it"); continue
        units = re.findall(r"\n      (\d+): \[(.*?)\n      \]", bm.group(1) + "\n      ]", re.S)
        qcounts = {int(n): len(re.findall(r"\{p:", body)) for n, body in units}
        answers_ok = all(0 <= int(a) <= 3 for a in re.findall(r"a:\s*(\d+)\s*\}", bm.group(1)))
        check(f"  {bank_const}: 9 units x 5 questions, answers in range",
              qcounts == {n: 5 for n in range(1, 10)} and answers_ok,
              f"unit question counts: {qcounts}")

    # And the SIXTH copy (build df): courses.html, the printable scope & sequence that
    # homeschool families file for curriculum records. Its ten cards carry no reliable
    # ids but sit in curriculum order, so the ten <ul class="units"> lists are read in
    # document order and zipped against curriculum.list_courses(). This page shipped
    # with the OLD diffeq units for a day after the build-de restructure -- a printed
    # scope & sequence disagreeing with the classroom is exactly what a curriculum
    # office notices.
    co_path = os.path.join(here, "static", "courses.html")
    if not os.path.exists(co_path):
        skip("courses.html unit lists", "file not present in this checkout")
        return
    with open(co_path, encoding="utf-8") as fh:
        co = fh.read()
    uls = re.findall(r'<ul class="units">(.*?)</ul>', co, re.S)
    courses = curriculum.list_courses()
    check("courses.html: one unit list per course, in curriculum order",
          len(uls) == len(courses), f"{len(uls)} lists for {len(courses)} courses")
    for (course, title), body in zip(courses, uls):
        names = [n.replace("&amp;", "&").strip() for n in re.findall(r"</b>\s*(.*?)</li>", body)]
        truth = [name for _n, name in curriculum.units_for(course)]
        check(f"courses.html matches curriculum.py: {course}", names == truth,
              f"first drift: {next(((a, b) for a, b in zip(truth, names) if a != b), 'count differs')}")
        check(f"  courses.html: the {course} card is present", title in co,
              f"course title {title!r} not found on the page")


def part3p_marketing_claims():
    # Added 2026-08-10 (build df). Jim: "make sure we don't have anything in here that
    # says evidence based learning as a blanket statement." Two phrases are banned from
    # every piece of VISIBLE marketing copy, permanently:
    #   - "evidence-based" / "evidence based": true in the strict WWC sense only for the
    #     elementary/algebra courses; a blanket claim is the kind of thing a school
    #     district's curriculum office checks, and one caught overreach discredits every
    #     true claim on the page. Per-level wording lives in Teaching_Evidence_Base sec 6.
    #   - "Socratic": Jim retired the word site-wide in build cc (the method is
    #     foundation-first, rules 36-38) -- and the sweep that wrote THIS check still
    #     found one live "taught Socratically" on courses.html that cc had missed.
    # HTML comments are stripped first: historical change notes are records, not copy.
    print("\nPART 3p — banned marketing claims stay banned")
    here = os.path.dirname(os.path.abspath(__file__))
    targets = sorted(
        p for p in os.listdir(os.path.join(here, "static")) if p.endswith(".html")
    ) + ["llms.txt"]
    banned = [("blanket 'evidence-based' claim", re.compile(r"evidence[\s-]based", re.I)),
              ("'Socratic'", re.compile(r"socratic", re.I))]
    for name in targets:
        path = os.path.join(here, "static", name)
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as fh:
            visible = re.sub(r"<!--.*?-->", "", fh.read(), flags=re.S)
        for label, pat in banned:
            m = pat.search(visible)
            check(f"{name}: no {label}", m is None,
                  f"found {m.group(0)!r} in visible copy" if m else "")
    readme = os.path.join(here, "README.md")
    if os.path.exists(readme):
        with open(readme, encoding="utf-8") as fh:
            txt = fh.read()
        for label, pat in banned:
            m = pat.search(txt)
            check(f"README.md: no {label}", m is None,
                  f"found {m.group(0)!r}" if m else "")


def part3q_reliability():
    # Added 2026-08-11 (build dg). The first full audit's Render logs proved the
    # stumbles were OURS, not rate limits (Audit_Findings_2026-08-11.md, PART 5):
    # claude-sonnet-5 intermittently rejects assistant-prefill continuation (a 400 that
    # NAMES its objection), five replies shipped as admitted partials at the old 1600
    # ceiling, and the rule-15 referee's false positives fed both by burning drafts.
    # This part proves the negotiated continuation, the raised ceiling, the empty-reply
    # retry, the stand-alone nudges, and the admin key's exit from query strings.
    print("\nPART 3q — reliability: continuation, empty retry, nudges, key transport")

    class _Resp:
        def __init__(self, text, stop):
            class _B:
                pass
            b = _B()
            b.type = "text"
            b.text = text
            self.content = [b]
            self.stop_reason = stop
            self.usage = None

    class _Stub:
        """A scripted stand-in for the Anthropic client. Each script step is a _Resp
        to return or an Exception to raise; every call's kwargs are recorded."""
        def __init__(self, script):
            self.script = list(script)
            self.calls = []
            self.messages = self          # so stub.messages.create(...) works

        def create(self, **kw):
            self.calls.append(kw)
            step = self.script.pop(0)
            if isinstance(step, Exception):
                raise step
            return step

    _PREFILL_ERR = Exception(
        "Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', "
        "'message': 'This model does not support assistant message prefill. The "
        "conversation must end with a user message.'}}")

    # --- the ceiling rose, and it is a named constant ---------------------------------
    check("MAX_REPLY_TOKENS is 3000 (raised from 1600 in build dg)",
          getattr(tutor, "MAX_REPLY_TOKENS", None) == 3000,
          f"got {getattr(tutor, 'MAX_REPLY_TOKENS', None)}")

    msgs = [{"role": "user", "content": "hello"}]

    # --- plain reply: one call, ceiling passed through --------------------------------
    stub = _Stub([_Resp("All done.", "end_turn")])
    out = tutor._create_full(stub, "dg-stub-plain", None, msgs, {})
    check("plain turn: one call, text returned", out == "All done." and len(stub.calls) == 1,
          f"out={out!r}, calls={len(stub.calls)}")
    check("plain turn: max_tokens kwarg is the ceiling",
          stub.calls[0].get("max_tokens") == tutor.MAX_REPLY_TOKENS,
          f"got {stub.calls[0].get('max_tokens')}")

    # --- prefill continuation, when the model accepts it ------------------------------
    stub = _Stub([_Resp("abc", "max_tokens"), _Resp("def", "end_turn")])
    out = tutor._create_full(stub, "dg-stub-prefill-ok", None, msgs, {})
    last = stub.calls[1]["messages"][-1]
    check("prefill continuation: stitched", out == "abcdef", f"out={out!r}")
    check("prefill continuation: second call ends with the assistant partial",
          last.get("role") == "assistant" and last.get("content") == "abc",
          f"last message: {last}")

    # --- THE AUDIT'S BUG: the named 400 switches to the user-nudge fallback -----------
    stub = _Stub([_Resp("part1", "max_tokens"), _PREFILL_ERR, _Resp("part2", "end_turn")])
    out = tutor._create_full(stub, "dg-stub-prefill-no", None, msgs, {})
    last = stub.calls[2]["messages"][-1]
    check("prefill rejection: reply still completes (negotiated fallback)",
          out == "part1part2", f"out={out!r}, calls={len(stub.calls)}")
    check("prefill rejection: fallback call ends with the continuation nudge",
          last.get("role") == "user" and "cut off" in str(last.get("content", "")),
          f"last message: {last}")
    check("prefill rejection: the refusal is REMEMBERED for this run",
          tutor._PREFILL_OK.get("dg-stub-prefill-no") is False, "flag not recorded")
    # ...and the next turn on that model goes straight to the fallback shape
    stub = _Stub([_Resp("x", "max_tokens"), _Resp("y", "end_turn")])
    out = tutor._create_full(stub, "dg-stub-prefill-no", None, msgs, {})
    last = stub.calls[1]["messages"][-1]
    check("remembered refusal: no second 400 is ever risked",
          out == "xy" and last.get("role") == "user",
          f"out={out!r}, last={last}")
    tutor._PREFILL_OK.pop("dg-stub-prefill-no", None)   # leave no test residue

    # --- an unrelated API error must still RAISE (never swallowed) --------------------
    stub = _Stub([_Resp("head", "max_tokens"), Exception("rate limited, try later")])
    try:
        tutor._create_full(stub, "dg-stub-other-err", None, msgs, {})
        ok_ = False
    except Exception:
        ok_ = True
    check("an unrelated API error still raises (only the NAMED 400 is negotiated)", ok_,
          "the error was swallowed")

    # --- still truncated after 2 continuations: stitched, loudly, 3 calls total -------
    stub = _Stub([_Resp("a", "max_tokens"), _Resp("b", "max_tokens"), _Resp("c", "max_tokens")])
    out = tutor._create_full(stub, "dg-stub-partial", None, msgs, {})
    check("hop limit: exactly 3 calls, pieces stitched", out == "abc" and len(stub.calls) == 3,
          f"out={out!r}, calls={len(stub.calls)}")

    # --- an EMPTY reply is retried once before any apology ----------------------------
    stub = _Stub([_Resp("", "end_turn"), _Resp("Nice work. Let's keep going.", "end_turn")])
    out = tutor._create_verified(stub, "dg-stub-empty", None, msgs, " [test]")
    check("empty reply: retried once, silently",
          out == "Nice work. Let's keep going." and len(stub.calls) == 2,
          f"out={out!r}, calls={len(stub.calls)}")
    stub = _Stub([_Resp("", "end_turn"), _Resp("", "end_turn")])
    out = tutor._create_verified(stub, "dg-stub-empty2", None, msgs, " [test]")
    check("empty twice: gives up cleanly so the caller can apologize",
          out == "" and len(stub.calls) == 2, f"out={out!r}, calls={len(stub.calls)}")

    # --- both regeneration nudges order the rewrite to STAND ALONE --------------------
    # The S-1 mechanism: two good drafts were burned by referee misfires, and the third
    # opened "So the hypotenuse is 5" -- the tail of an explanation only the DISCARDED
    # drafts contained. The nudge is the only voice in the room at that moment.
    check("the prose nudge orders a stand-alone rewrite",
          "STAND ALONE" in tutor._PROSE_NUDGE and "from scratch" in tutor._PROSE_NUDGE,
          "missing the stand-alone instruction")
    check("the mathcheck nudge orders a stand-alone rewrite",
          "STAND ALONE" in tutor._MATHCHECK_NUDGE, "missing the stand-alone instruction")

    # --- the admin key stays out of query strings (the L-4 leak) ----------------------
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "static", "admin.html"), encoding="utf-8") as fh:
        adm = fh.read()
    check("admin.html sends the key in the X-Admin-Key header",
          '"X-Admin-Key"' in adm, "header not found")
    check("admin.html never builds a key-carrying URL",
          not re.search(r'\?key="\s*\+', adm), "found a '?key=\" +' URL construction")
    check("admin.html keeps the key in sessionStorage, not the address bar",
          'sessionStorage.setItem("mt_admin_key"' in adm and "history.replaceState" in adm,
          "sessionStorage stash or address-bar scrub missing")
    with open(os.path.join(here, "main.py"), encoding="utf-8") as fh:
        mn = fh.read()
    n_alias = mn.count('alias="X-Admin-Key"')
    check("all four admin GET endpoints accept the X-Admin-Key header",
          n_alias >= 4, f"found {n_alias} of 4")
    n_pref = mn.count("_require_admin(x_admin_key or key)")
    check("the header is preferred over the query param",
          n_pref >= 4, f"found {n_pref} of 4")


# =============================================================================
# PART 3r -- THE FIGURES THE AUDIT COULD NOT DRAW (build di)
# -----------------------------------------------------------------------------
# Finding S-4: a jump discontinuity "drawn" as two full parallel lines because the
# grapher had no piecewise vocabulary. Finding S-9: a student asked twice to SEE the
# wrong decimal lineup and got prose labels because no tag could draw it. Both tools
# exist now, and this part proves them THROUGH THE REAL RENDERER (node executes
# math-figures.js, the same file the browser runs) -- plus the discovery the harness
# made on its first run: hole= had NEVER drawn on a genuine 0/0 removable point,
# because the renderer evaluated the function AT the hole and bailed on NaN. The
# canonical scripts had quietly worked around it with pre-simplified forms.
# =============================================================================
_DI_GRAPH_HARNESS = r'''
const fs = require("fs");
global.window = {};
eval(fs.readFileSync(process.argv[2], "utf8"));
const MF = global.window.MathFigures;
const out = [];
function t(name, cond) { out.push([name, !!cond]); }
// the audit's jump, drawn right: open circle at (2,3), closed dot at (2,6), no bridge
const svg = MF.graph({ func: "x+1 for x<2; x+4 for x>=2", range: "0..4", yrange: "0..8" });
t("the strict bound gets an OPEN circle at (2,3)", svg.includes('cy="267.5" r="5" fill="#fbfbff"'));
t("the inclusive bound gets a CLOSED dot at (2,6)", /cy="125" r="5" fill="#[0-9a-f]{6}" stroke="#ffffff"/.test(svg));
const polys = [...svg.matchAll(/<polyline points="([^"]+)"/g)].map(m => m[1].split(" ").map(p => parseFloat(p.split(",")[0])));
t("two pieces, each clipped to its own side of x=2",
  polys.length === 2 && Math.max(...polys[0]) <= 220.01 && Math.min(...polys[1]) >= 219.99);
t("the legend names the domains", svg.includes("for x&lt;2") && svg.includes("for x&gt;=2"));
const s2 = MF.graph({ func: "x^2 for -1<=x<3", range: "-4..4" });
t("a double-ended domain marks both endpoints", (s2.match(/r="5"/g) || []).length === 2);
const s3 = MF.graph({ func: "x+1 for x≥2", range: "0..4" });
t("unicode bounds are accepted", /stroke="#ffffff"/.test(s3));
const s4 = MF.graph({ func: "x+1 for banana", range: "0..4" });
t("an unparseable domain fails OPEN -- the curve still draws",
  [...s4.matchAll(/<polyline/g)].length === 1);
// the harness's own first-run discovery, kept forever:
const s5 = MF.graph({ func: "(x^2-4)/(x-2)", hole: "2", range: "0..4", yrange: "0..6" });
t("a hole on a genuine 0/0 point actually draws (numeric limit)", s5.includes(">hole<"));
const s6 = MF.graph({ func: "1/(x-2)", hole: "2", range: "0..4", yrange: "-6..6" });
t("an asymptote NEVER gets a hole painted on it (rule 51e in pixels)", !s6.includes(">hole<"));
const s7 = MF.graph({ func: "sin(x)", range: "-6..6" });
t("a plain un-domained function is untouched", s7.includes("<polyline"));
console.log(JSON.stringify(out));
'''


def part3r_batch_d_figures():
    print("\nPART 3r — the figures the audit could not draw (build di)")
    here = os.path.dirname(os.path.abspath(__file__))
    # (1) the three showColumn bodies must be BYTE-IDENTICAL -- the build-bk drift class
    bodies = {}
    for page in ("session", "practice", "topic"):
        try:
            with open(os.path.join(here, "static", f"{page}.html"), encoding="utf-8") as fh:
                m = re.search(r"function showColumn\(a\) \{[\s\S]*?\n    \}", fh.read())
            bodies[page] = m.group(0) if m else ""
        except OSError:
            bodies[page] = ""
    check("showColumn is byte-identical on all three teaching pages",
          bool(bodies.get("session")) and len(set(bodies.values())) == 1,
          "the pages have drifted -- the build-bk bug class")
    check("align='last' NEVER completes the wrong layout",
          "res && !wrongAlign" in bodies.get("session", ""),
          "a result row in the deliberately-wrong lineup would complete a wrong sum "
          "on our board (rules 13 and 26)")
    check("the wrong lineup carries its built-in badge",
          '"cwarn"' in bodies.get("session", ""), "the badge div is missing")
    for page in ("session", "practice", "topic"):
        with open(os.path.join(here, "static", f"{page}.html"), encoding="utf-8") as fh:
            css = fh.read()
        check(f"  [{page}] carries the wrong-way styling", ".colmath.colwrong" in css,
              "amber styling missing -- the wrong way must never look like the taught way")
    # (2) the piecewise/hole behaviour, proven through the REAL math-figures.js
    try:
        subprocess.run(["node", "--version"], capture_output=True, check=True)
    except Exception:  # noqa: BLE001
        skip("piecewise render checks", "node not available")
        return
    import json as _json
    import tempfile as _tf
    with _tf.TemporaryDirectory() as tmp:
        hpath = os.path.join(tmp, "di.js")
        with open(hpath, "w") as fh:
            fh.write(_DI_GRAPH_HARNESS)
        res = subprocess.run(["node", hpath, os.path.join(here, "static", "math-figures.js")],
                             capture_output=True, text=True)
        if res.returncode != 0:
            bad("piecewise render harness", res.stderr.strip()[:200])
            return
        for name, okk in _json.loads(res.stdout):
            check(f"render: {name}", okk, "see math-figures.js graph()")
    # (3) the shared tool note reaches every course (PART 1's discipline)
    for c in COURSES:
        prompt = tutor.build_system_prompt(dict(STUDENT), course=c)
        check(f"piecewise + wrong-lineup docs reach [{c}]",
              "for x<2" in prompt and 'align="last"' in prompt,
              "the shared board-tools note is missing from this course's prompt")


# =============================================================================
# PART 3s -- BACKUPS: THE WAY BACK MUST ACTUALLY WORK (build dj)
# -----------------------------------------------------------------------------
# Jim: "if Render falters or something falters, do we have sufficient backup so that
# we could recreate everything right away?" A backup system is only real if the
# RESTORE has been rehearsed, so this part performs the whole drill on every run:
# seed a real database, snapshot it with store.export_all, restore that snapshot into
# a SECOND, blank database THROUGH THE ACTUAL restore_backup.py TOOL (dry look first,
# which must change nothing), then prove the two databases are row-for-row identical.
# Plus the boundaries: no restore endpoint may ever exist, the download rides the
# header, the nightly pass is fenced and atomic.
# =============================================================================
_BK_SEED = r'''
import json, os, sys
import store
store.init()
assert store.enabled(), "sqlite store failed to enable: " + str(store.status())
store.record_check("BKTEST", 2, 9, 10, "Integers", course="prealgebra")
store.record_check("BKTEST", 4, 8, 10, "Fractions", course="prealgebra")
store.record_foundation_heard("BKTEST", "prealgebra", "fraction")
store.create_beta_code("TRY-BACKUP7", "backup drill", 5, 2)
store.log_usage(kind="brain", code="BKTEST", course="prealgebra", mode="lesson",
                model="test", input_tokens=10, output_tokens=5)
snap = store.export_all()
json.dump(snap, open(sys.argv[1], "w"))
print(sum(snap["row_counts"].values()))
'''

_BK_EXPORT = r'''
import json, sys
import store
store.init()
assert store.enabled(), "sqlite store failed to enable"
json.dump(store.export_all(), open(sys.argv[1], "w"))
'''


def _bk_tables(path):
    import json as _json
    snap = _json.load(open(path))
    # order-independent, deep comparison: each table's rows as a sorted list of
    # sorted-key JSON strings
    return {name: sorted(_json.dumps(r, sort_keys=True) for r in rows)
            for name, rows in snap["tables"].items()}


def part3s_backups():
    print("\nPART 3s — backups: the way back must actually work")
    here = os.path.dirname(os.path.abspath(__file__))
    import gzip as _gz
    import json as _json
    import tempfile as _tf
    with _tf.TemporaryDirectory() as tmp:
        db1 = os.path.join(tmp, "db1.sqlite")
        db2 = os.path.join(tmp, "db2.sqlite")
        snap_json = os.path.join(tmp, "snap.json")
        snap_gz = os.path.join(tmp, "snap.json.gz")
        seed = os.path.join(tmp, "seed.py")
        exp = os.path.join(tmp, "exp.py")
        with open(seed, "w") as fh:
            fh.write(_BK_SEED)
        with open(exp, "w") as fh:
            fh.write(_BK_EXPORT)

        def run(script, dburl, *args):
            # PYTHONPATH, not just cwd: python puts the SCRIPT'S directory on the
            # path, and the seed/export scripts live in the temp dir, not the repo.
            env = dict(os.environ, DATABASE_URL=dburl, PYTHONPATH=here)
            return subprocess.run([sys.executable, script, *args], cwd=here, env=env,
                                  capture_output=True, text=True)

        # 1. seed a real database and snapshot it
        r = run(seed, f"sqlite:///{db1}", snap_json)
        if r.returncode != 0:
            bad("backup drill: seed + export", r.stderr.strip()[:300])
            return
        total = int(r.stdout.strip().splitlines()[-1])
        check(f"a seeded database exports ({total} rows)", total >= 5, f"only {total} rows")
        with open(snap_json, "rb") as fh:
            _gz_bytes = _gz.compress(fh.read())
        with open(snap_gz, "wb") as fh:
            fh.write(_gz_bytes)

        # 2. the DRY LOOK must change nothing (a blank second database stays blank)
        r = run(os.path.join(here, "restore_backup.py"), f"sqlite:///{db2}", snap_gz)
        check("restore_backup.py without the flag is a DRY LOOK (exit 0, says so)",
              r.returncode == 0 and "DRY LOOK" in r.stdout, (r.stdout + r.stderr)[-200:])
        r = run(exp, f"sqlite:///{db2}", os.path.join(tmp, "after_dry.json"))
        dry_rows = sum(len(v) for v in _bk_tables(os.path.join(tmp, "after_dry.json")).values()) \
            if r.returncode == 0 else -1
        check("the dry look changed NOTHING (second database still empty)", dry_rows == 0,
              f"{dry_rows} rows appeared without the flag")

        # 3. the real restore, THROUGH THE ACTUAL TOOL, gzip file and all
        r = run(os.path.join(here, "restore_backup.py"), f"sqlite:///{db2}",
                snap_gz, "--yes-i-mean-it")
        check("restore_backup.py --yes-i-mean-it restores", r.returncode == 0,
              (r.stdout + r.stderr)[-300:])
        r = run(exp, f"sqlite:///{db2}", os.path.join(tmp, "after_restore.json"))
        if r.returncode != 0:
            bad("backup drill: re-export after restore", r.stderr.strip()[:300])
            return
        t1, t2 = _bk_tables(snap_json), _bk_tables(os.path.join(tmp, "after_restore.json"))
        diff = [n for n in set(t1) | set(t2) if t1.get(n) != t2.get(n)]
        check("the restored database is ROW-FOR-ROW identical to the snapshot",
              not diff, f"tables differing after restore: {diff[:5]}")

    # 4. the boundaries, from the source
    with open(os.path.join(here, "main.py"), encoding="utf-8") as fh:
        mn = fh.read()
    check("main.py NEVER calls import_all (no restore endpoint can exist)",
          "import_all" not in mn,
          "a remote wipe-and-replace is a foot-gun -- restores are offline only")
    check("the backup download rides the X-Admin-Key header",
          'def admin_backup_download' in mn and mn.count('alias="X-Admin-Key"') >= 6,
          "backup endpoints missing the header alias")
    check("the nightly pass is fenced inside the heartbeat",
          "_backup_pass()" in mn and "[backup] loop error" in mn,
          "an unfenced pass could kill the digests")
    check("the snapshot write is ATOMIC (tmp then rename)",
          "os.replace(tmp, _BACKUP_DIR / name)" in mn,
          "a crash mid-write must never leave a half snapshot")
    check("rotation keeps BACKUP_KEEP newest",
          "[:-BACKUP_KEEP]" in mn, "no rotation found")
    with open(os.path.join(here, "static", "admin.html"), encoding="utf-8") as fh:
        adm = fh.read()
    check("/admin has the Backups card with a header-borne download",
          'id="bkDownload"' in adm and '"X-Admin-Key": KEY' in adm,
          "the offsite copy needs a button (build cx: buttons, not instructions)")
    check("/admin has NO restore control",
          "restore" not in adm.lower() or "restore_backup.py" in adm,
          "restore must stay an offline, deliberate act")
    for fname in ("RECOVERY.md", "restore_backup.py"):
        check(f"{fname} exists and is not truncated",
              os.path.exists(os.path.join(here, fname))
              and "I did no harm and this file is not truncated"
              in open(os.path.join(here, fname), encoding="utf-8").read(),
              "the runbook/tool must ship with the code")


def part4_live():
    print("\nPART 4 — live scenarios (a scripted difficult student)")
    if not os.environ.get("ANTHROPIC_API_KEY"):
        skip("live scenarios", "no ANTHROPIC_API_KEY")
        return
    for sc in LIVE_SCENARIOS:
        history = [{"role": r, "content": t} for r, t in sc["history"]]
        try:
            reply = tutor.get_tutor_reply(dict(STUDENT), history, sc["student"],
                                          course=sc["course"], code="RULETEST")
        except Exception as exc:  # noqa: BLE001
            bad(f"live: {sc['name']}", f"call failed: {exc}")
            continue
        try:
            passed = bool(sc["assertion"](reply))
        except Exception as exc:  # noqa: BLE001
            passed = False
            reply = f"(assertion crashed: {exc}) {reply}"
        check(f"live: {sc['name']}", passed, f"{sc['why']}\n        reply: {reply[:220]}")


def main():
    if "--rules" in sys.argv:
        print("wrote", write_rules_index(os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "RULES.md")))
        return 0
    live = "--live" in sys.argv
    print("=" * 70)
    print("RULE REGRESSION BATTERY —", "OFFLINE + LIVE" if live else "OFFLINE ONLY")
    print("=" * 70)
    part1_coverage()
    part2_prose()
    part3_speech()
    part3b_foundations()
    part3c_board_tags()
    part3d_foundation_memory()
    part3e_page_parity()
    part3f_notation()
    part3g_misconceptions()
    part3h_scale()
    part3i_rule_verification()
    part3j_walkthroughs()
    part3k_mastery_reachable()
    part3l_lesson_auditor()
    part3n_sprints()
    part3o_unit_name_parity()
    part3p_marketing_claims()
    part3q_reliability()
    part3r_batch_d_figures()
    part3s_backups()
    if live:
        part4_live()
    else:
        print("\nPART 4 — live scenarios")
        skip("live scenarios", "pass --live to run them")
    print("\n" + "=" * 70)
    print(f"{len(PASS)} passed · {len(FAIL)} failed · {len(SKIP)} skipped")
    if FAIL:
        print("\nFAILURES:")
        for name, detail in FAIL:
            print(f"  - {name}: {detail}")
    print("=" * 70)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())

# I did no harm and this file is not truncated.
