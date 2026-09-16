# CHANGELOG -- lessonscripts.py  (notes rolled out of the file's header)

Moved out of `lessonscripts.py` on 2026-09-16 (build wp): every CHANGE NOTE dated before 2026-09-10 -- 46 entries, VERBATIM, in the order they sat in the file (newest first). The 20 notes from 2026-09-10 on stay at the top of `lessonscripts.py` itself, and new notes keep going there. Nothing below was edited; grep this file for a build letter or a date. When the header is rolled out again, the newer block is added ABOVE this one.

```text
#   2026-09-08  OLDER NOTES (before 2026-09-01) live in
#               changelog/lessonscripts.py.md -- moved out on 2026-09-08 (build ui)
#               VERBATIM, 70 entries; 39 stay here. Keep adding new notes HERE, newest at
#               top; roll them out again (notes_rollout.py) when this header passes ~100
#               KB.
#   2026-09-09  BUILD uv -- THE LESSON HAS A VISIBLE FINISH LINE, AND THE ORIENTATION
#               CARD CARRIES THE RECORD. Two board-only repairs from Jim's 2026-09-09
#               ruling ("wherever we can, we want to have graphics to support what we are
#               saying"). NOT ONE SPOKEN WORD CHANGES in either, so no new voice line
#               exists in this build and NO PREWARM IS NEEDED.
#               (a) _end_board / _card_text, read by _end: every lesson now ends on a
#                   card -- "Lesson done" (Jim's own word; his 2026-09-07 ruling reserves
#                   "mastered" for the 90% Unit Quiz) or "Where we got to" for a
#                   still-learning end -- carrying the topic and how many problems were
#                   answered. A student who answered none is not handed a zero to look
#                   at. boardaudit.py measured what the silent ending cost: 68 endings
#                   across Entry-Level and Diffeq where a child answers the last question
#                   and then hears 40-70 words with nothing new drawn, and ALL 23
#                   stretches in the whole course that ran past referee 85's ceiling were
#                   lesson endings. The worst run in the course: 69 words -> 53.
#               (b) lesson_orientation(lesson, prev_done, last=None) + _last_time_item:
#                   the orientation card now says what they did LAST TIME, WHEN, and HOW
#                   IT WENT, from the record main.py prepares (_orientation_last). The
#                   two SPOKEN variants are deliberately untouched -- they are
#                   pre-rendered clips, and a per-student sentence would turn the second
#                   beat of every lesson into a live text-to-speech call, a bill and a
#                   wait on the one beat that has to land instantly. The board holds a
#                   score better than the ear does. last=None returns byte-for-byte what
#                   us shipped, and an absent or impossible field drops that part of the
#                   line rather than guessing (rule 0).
#   2026-09-09  BUILD us -- ORIENT, THEN ONE IDEA PER BEAT WITH A CHECK (the shape Jim
#               chose, 2026-09-08). Three pure helpers, the engine's walk untouched:
#               lesson_orientation(lesson, prev_done) -> (spoken, card) -- "Before this
#               came <prev>, and you finished it. Today: <topic>. First the idea, then a
#               picture, then the method -- then your turn." (the record's word) or the
#               "Today:" form; prev_lesson(lesson) from COURSE_ORDER; beat_of(lesson,
#               spoken) -> why/picture/teach/worked/practice_intro/explain/recap/"".
#               LINE_CHECK ("Got it?"), CHECK_CHOICES and READY_CHOICES are the page's
#               check and ready gate, byte-identical in session.html. Both orientation
#               forms join every lesson's audio closure (the battery's ceiling 24,000 ->
#               24,500); LINE_CHECK is a STANDALONE line. Run the prewarm after the push.
#   2026-09-09  BUILD ur -- THE WRONG ANSWER IS ANSWERED AT ONCE. Two fixed lines join the
#               audio closure: LINE_THINKING ("Give me a moment to work this one out with
#               you.") and LINE_THINKING_MORE ("Still working on it -- one more moment."),
#               spoken by session.html while a deferred re-teach is still coming (byte-
#               identical there). They are STANDALONE_LINES -- the lane's, not any
#               lesson's closure (three calculus closures sit 25 chars under the 24,000
#               ceiling). Nothing else in this file changed. Run the prewarm.
#   2026-09-08  BUILD uq -- THE PROBLEM IS ALWAYS ON THE BOARD (Jim's corrections queue).
#               * PRACTICE_INTRO_BOARD: the practice intro ("Now it's your turn...") carries
#                 a card now; it spoke over a scrolled-away board (flag 22:02).
#               * _fcmp_board: the two rules FIRST, then the machines, then f(g(c)) = ?
#                 (flag 21:57 "visuals backwards"); _fcmp_worked writes each machine's
#                 line beside it (flag 21:59).
#               * absc: INTEGERS, not "whole numbers" (false for the negatives); the
#                 question, the board, the walk-back and the praise count DOTS on the
#                 number line one side at a time (_absc_dots), not bars (flag 21:40).
#               * PRAISE_PREFIXES: "Nice counting!" -> "Nice work!" (flag 22:05: it praised
#                 a composition). New closure text: run the script-prewarm after the push.
#   2026-09-08  BUILD up -- A NEW MACHINE, STILL CALLED f. Jim's 2026-09-08 ruling (rule
#               28: one letter names one function, all conversation) reaches the practice
#               sets, which give f a fresh rule every problem. The four function ops now
#               open by retiring the name out loud: fnot and fback "A new machine, still
#               called f.", fm2 "Two new machines in a row.", fcmp "Two new machines, still
#               called f and g." -- rule 28's own escape clause, applied uniformly. Nothing
#               else in the ops changed (answers, boards, choices, checks, praise).
#   2026-09-08  BUILD uj -- ONE FILE PER COURSE. THIS FILE IS THE ENGINE NOW. The 360
#               authored lessons -- 25,500 lines, 61% of this file -- moved to lessons/
#               (entry.py, basic.py, prealgebra.py, algebra1.py, geometry.py, algebra2.py,
#               precalc.py, probstat.py, calculus.py, diffeq.py), each course its own
#               pure-data file with its unit lists, their build notes and its slice of
#               COURSE_ORDER; lessons/__init__.py joins them in course order. This file
#               does `from lessons import LESSONS, COURSE_ORDER` where the lists used to
#               be and then exactly what it always did (the disagreement check, the
#               reorder, LESSON_BY_ID, PILOT_LESSON). The split script proved the data
#               deep-equal (types included) and every moved line present; PART 3kf pins
#               it. 41,846 lines -> 16,280. Nothing the engine does changed. A new
#               lesson goes in lessons/<course>.py -- see that file's note.
#   2026-09-07  BUILD ub -- CALCULUS UNITS 7-9 TO THE SHAPE (12 lessons). Jim: "continue
#               with updating the courses as far as how we're taught." ⭐ CALCULUS 36/36.
#               THIS FILE:
#                 * Unit 7 (the integral): the area under the graph SHADED on the ask
#                   with "?" written in it ([[graph shade="lo..hi" label="?"]], new in
#                   math-figures.js) and the area written on the walk-back -- the
#                   rectangle under a steady speed, the triangle under the ramp y = x,
#                   the strip under 2x from one end to the other; the hump whose area is
#                   GIVEN (h + h/2 sin over one whole period, so the label is honest)
#                   and the flat line it flattens to on the walk-back;
#                 * Unit 8 (uses): the strip between two humps (between="1"); the
#                   trapezium under a climbing speed and its halfway line on the
#                   walk-back; the flow rectangle asked, the AMOUNT line from the start
#                   on the walk-back; the cylinder ([[solid kind="cylinder"]]) a
#                   rectangle sweeps out;
#                 * Unit 9 (differential equations): the amount line falling from the
#                   start, its end point on the walk-back; the two rates as bars, the
#                   net line on the walk-back; the rate line against the amount, the
#                   point on the walk-back; the rate line falling to zero, the crossing
#                   on the walk-back.
#               LEGENDS: "speed = 7 m/s" as a legend name fired the one-thought-per-line
#               referee (an equation with a trailing unit) on 24 asks and walk-backs --
#               "a steady 7 metres a second" and "6 litres a minute running in" now.
#               THREE closures crossed the 24,000-character audio ceiling (defi 24,126,
#               revo 25,361, pgrw 24,650): each praise says the arithmetic once and
#               keeps the one idea its walk-back does not say. Trap lines kept in every
#               lesson; "one idea wearing two hats" and "measures the CHANGE, never the
#               amount" kept in their teaches. ENGINE: OP_EXT defi/triz/ftc/avgv/btwn/
#               trap/accu/revo/dfeq/mixr/pgrw/eqbm gain "worked" (_defi_* ... _eqbm_*)
#               and picture boards. The six PART 3fs fixed fragments survive in each
#               lesson's second worked pair.
#   2026-09-07  BUILD ua -- CALCULUS UNITS 4-6 TO THE SHAPE (12 lessons). Jim: "continue
#               with updating the courses as far as how we're taught." CALCULUS 24/36.
#               THIS FILE:
#                 * Unit 4 (derivatives at work): the speed line ALONE on the ask (no
#                   height, no crossing), the height and the crossing on the walk-back;
#                   area against side with the point, the tangent there on the
#                   walk-back; the valley alone, its flat bottom on the walk-back; the
#                   speed line, one step up it on the walk-back;
#                 * Unit 5 (optimisation): the fence shared four ways as a TAPE with
#                   every part blank, the square walked round ([[rectangle
#                   show="perimeter"]]) on the walk-back; the square on a metre grid
#                   asked ([[rectangle show="area" ask="1"]]), counted on the
#                   walk-back; the hump of every split, its peak on the walk-back; the
#                   cubic whose bend changes, the line x = a/3 on the walk-back;
#                 * Unit 6 (antiderivatives): the power rule run backwards as a
#                   MACHINE (÷ 2, then ÷ the new exponent) with output "?", filled and
#                   the function written on the walk-back; two parallel curves with
#                   the lower one's point, both points on the walk-back; one member of
#                   the family with its start, its height further on on the walk-back.
#               RULE 15 IN THE ASK ITSELF, live: the one-point lesson wrote "y = 19 at
#               x = 0 · y at x = 4 = ?" on every one of its twelve asks -- a chain of
#               equals ending in "= ?" -- and writes "at x = 4 · y = ?" now. The
#               acceleration ask's "differentiate again → ?" is "acceleration = ?".
#               The halves lesson's teach splits 30 (20 was a bank ask); the related
#               rates teach grows a side of 15 (10 at 2 was a bank ask); "the total"
#               (canon "in all") and "makes" (canon "equals") are gone from the audio.
#               The related-rates praise says the arithmetic once (its closure was
#               24,652 characters, over the 24,000 audio ceiling; 19,612 now). ENGINE:
#               OP_EXT vsol/mrat/crit/acce/optr/maxa/sumx/infl/anti/antp/plusc/init gain
#               "worked" (_vsol_* ... _init_*) and picture boards; maxa's check keeps
#               the fence at 80 or less (the grid draws sides to 20; 88 wanted 22).
#               The eight PART 3fs fixed fragments survive in each lesson's second
#               worked pair. FIGURES: math-figures.js keeps a five-digit y label whole.
#   2026-09-07  BUILD tz -- CALCULUS UNITS 1-3 TO THE SHAPE (12 lessons). Jim: "continue
#               with updating the courses as far as how we're taught." CALCULUS 12/36.
#               THIS FILE:
#                 * Unit 1 (limits): f and g closing on the same x on one GRAPH with the
#                   hole drawn (hole= on the first curve, names="f; g"), the product
#                   withheld, walked back as the product curve closing on it; the
#                   fraction flattening with NO line on the ask, the line y = a/b drawn
#                   on the walk-back; two shelves with the open and closed dots at the
#                   border (piecewise func="a for x<6; b for x>=6"), the leap marked on
#                   the walk-back; the sloping piece climbing to a border the flat piece
#                   misses, the flat piece raised to meet it on the walk-back;
#                 * Unit 2 (the derivative): y = x squared with the point alone on the
#                   ask, the tangent line on the walk-back; the power rule as a MACHINE
#                   (the exponent goes in, rule "x the front number", output "?"), the
#                   machine filled and the new power written on the walk-back; a line
#                   alone on the ask, two steps marked on the walk-back; the derivative
#                   as a machine fed an x, the curve with the point on the ask and the
#                   tangent on the walk-back;
#                 * Unit 3 (the rules): x times (x + a) with the point, the slope rule
#                   as its OWN step, the tangent on the walk-back; the chain rule as a
#                   machine (the power goes in, rule "x the inside's derivative"); the
#                   chain rule at a point, the tangent on the walk-back; a plain number
#                   underneath as a two-stage machine ("x 2, then / b").
#               LEGENDS: every single-curve graph carries names= now -- the legend used
#               to print the raw expression ("y=(36*x^2)/(3*x^2 + 3)"), and reads
#               "y = 36x² / (3x² + 3)" instead (40 graphs across asks, walk-backs, beats).
#               PENDING LINES: two boards wrote a chain of equals ending in "= ?" and
#               are two steps now ("slope = 2x + 6" then "at x = 5 · slope = ?"); two
#               piecewise boards wrote an arrow after an equals sign and use the colon
#               form ("x < 6: y = 2 · x ≥ 6: y = 14"). The cnst lesson said "makes"
#               (canon is "equals"). Trap lines kept in every lesson. ENGINE: OP_EXT
#               llaw/linf/jump/cfix/derv/pwrc/cnst/evat/prod/chan/chev/quot gain
#               "worked" (_llaw_* ... _quot_*) and picture boards. Demonstrated numbers
#               kept out of the banks: the power rule teaches 6x^3 (a bank ask was
#               3x^6), the chain rule (5x + 3)^6 and (4x + 7)^2. The eight PART 3fs
#               fixed fragments survive in each lesson's second worked pair.
#   2026-09-07  BUILD ty -- PROBSTAT UNITS 7-9 TO THE SHAPE (12 lessons). Jim: "continue
#               with updating the courses as far as how we're taught." ⭐ PROBSTAT 36/36.
#               THIS FILE:
#                 * Unit 7 (expected value): the two known chances on the HUNDRED SQUARE
#                   with large as the white cells (asked), the three prizes as BARS that
#                   fill the hundred (walked back); the paying plays shaded on the hundred
#                   square, walked back as two PILES of tokens as bars; the wins shaded on
#                   the hundred square, walked back as the pot MACHINE (÷ the wins); what
#                   you pay beside what comes back as bars, walked back as a TAPE of back
#                   and gone;
#                 * Unit 8 (the normal curve): the middle band on the BELL ([[normal]] on
#                   the ask -- the answer is a headcount, not on its axis), walked back on
#                   the hundred square; the mean and the value as two dots on a NUMBER
#                   LINE with no hops on the ask (a hop prints its jump, and counting the
#                   hops IS the answer), the hops of one deviation on the walk-back; ONE
#                   hop shown on the ask and two walked; the top sliver of the bell on the
#                   ask, the three parts of the group as a tape on the walk-back;
#                 * Unit 9 (confidence): the estimate as a dot with the margin's reach on
#                   the ask, the step down as a hop on the walk-back; the two halves of the
#                   doubt as a tape with total="?" on the ask and the width on the
#                   walk-back; the estimate, the ceiling and the claim as three dots, the
#                   gap as a hop on the walk-back; the three percents as bars on the ask,
#                   the people machine on the walk-back.
#               RULE 42 IN THE ASK ITSELF, live: two asks said "how many students" (n68,
#               npop) -- the comparison shape (tn's law) -- and are "how many of the whole
#               group / the whole school" now; their praise counts no students. THREE ops
#               wrote a QUESTION inside a step ("how many students = ?", "how many
#               deviations above = ?" -- 36 baseline presweep hits) and write statements
#               now ("the middle band holds ?", "deviations above the mean = ?"). Trap
#               lines kept in every lesson. ENGINE: OP_EXT pdis/evwa/fair/hedg/n68/zsco/
#               zval/ntal/cint/cwid/inci/npop gain "worked" (_pdis_* ... _npop_*) and
#               picture boards. Demonstrated numbers kept out of the banks: the tails
#               lesson teaches a group of 800 (400 was a bank ask). The nine PART 3ft
#               ps_fixed fragments survive in each lesson's second worked pair.
#   2026-09-06  BUILD tt -- PROBSTAT UNITS 4-6 TO THE SHAPE (12 lessons). Jim:
#               "Continue with the probability and statistics."
#               THIS FILE:
#                 * Unit 4 (sampling): the school as bars and the sample as a TAPE cut
#                   the same way (asked with both parts blank); the surveys back and
#                   silent as a tape, walked back on the hundred square as a percent;
#                   the asked and the never-asked as a tape with the second part blank;
#                   the people MACHINE (rule x 4) with its output blank, walked back as
#                   now beside four times;
#                 * Unit 5 (probability): the bag as bars, the chance on the hundred
#                   square; the three piles captioned (12 asks drew bars with none,
#                   rule 41) and joined on a tape; two PIES with one slice each for two
#                   chances, walked back as the ARRAY of days by buses (the array prints
#                   its product -- walk-back only); the spinner as a pie with its winners
#                   shaded, walked back as the TREE of paths (it prints every leaf's
#                   product -- walk-back only);
#                 * Unit 6 (conditional): the four groups as bars, walked back as the
#                   TWO-WAY table (it prints the row totals -- walk-back only); the
#                   girls' share on the hundred square; the school beside the group as
#                   bars; the bag as a tape before and after a marble is kept.
#               RULE 42 IN THE ASK ITSELF, live: the undercoverage ask said "How many
#               students never had a chance to be asked?" -- "how many students" is the
#               comparison shape (tn's law) -- and its praise counted "students it could
#               never reach". The ask asks about "the whole school" now; the praise
#               counts "the ones it could never reach". One pending line was a question
#               inside a step ("how many winners?") -- a statement now. Trap lines kept
#               in every lesson. ENGINE: OP_EXT strf/resp/bias/merr/ppct/por/pand/ptre/
#               cbse/ccnt/indp/wout gain "worked" (_strf_* ... _wout_*) and boards.
#               Demonstrated numbers kept out of the banks and pairs: the margin lesson
#               teaches 60 -> 240 -> 960 (100 -> 400 was a bank ask); the AND lesson
#               teaches one in 5 times one in 3 (4 times 3 was the (3, 4) bank ask);
#               the GIVEN lesson counts 7 plus 5 girls (6 plus 4 was the (6, 4, 13)
#               bank ask); independence predicts 45 percent (30 was a bank ask).
#   2026-09-06  BUILD ts -- THE LESSON INTRODUCES ITSELF. Jim, back after a day away:
#               "Welcome back -- let's pick up where you left off", then a Pre-Algebra
#               why beat with no unit, no lesson, no name -- "I have no idea what it is
#               referring to. I thought we fixed this." (the 22:16 "no introduction"
#               flag, back in the shape's costume: the old teach openers named the
#               unit, the why beat opens on the why). ENGINE: lesson_intro(lesson)
#               makes one spoken line and one board card -- "Pre-Algebra, Unit 1:
#               Number Sense and Order of Operations. Lesson 1 of 4: Order of
#               operations." on a [[write]] card -- and step()'s begin speaks it
#               BEFORE the why, for every lesson in every course, fresh start and
#               return alike; audio_lines() carries it (360 new closure lines --
#               prewarm). Pure: it reads the lesson and curriculum.py's titles.
#   2026-09-06  BUILD tr -- PROBSTAT UNITS 1-3 TO THE SHAPE (12 lessons). Jim: "go".
#               THIS FILE:
#                 * Unit 1 (exploring data): the dot plot, the dot plot with its line,
#                   the histogram and the stray dot -- every ask captioned (96 asks in
#                   these three units drew a figure with no caption, rule 41), walked
#                   back with the stack, the count, the sum and the stray named;
#                 * Unit 2 (describing distributions): the even list as a dot plot,
#                   walked back as the two middles on the number line with the halfway
#                   mark (mid=); the box plot; the four numbers as a dot plot, walked
#                   back as their four distances as bars; the hundred square as a
#                   percent, walked back as beaten beside ahead;
#                 * Unit 3 (scatterplots): the scatter cloud captioned; the slope as a
#                   rate MACHINE, walked back as the line climbing with the point
#                   marked; predicted beside actual as bars, walked back as one hop on
#                   the number line; the dots as a tape with the below part blank.
#               RULE 42 IN THE ASKS THEMSELVES, live: the mode ask said "the most
#               children" and the percentile ask "40 other students" -- the comparison
#               shape. The mode ask now asks for "the number that happened most often";
#               the percentile ask is a swimmer racing "40 others" (third person;
#               "percentile" is exempt in probstat, "other students" never was). Two
#               pending lines were questions inside a step ("how many players?", "how
#               many scores in all?") and one more ("how many beaten = ?") -- all
#               statements now. Trap lines kept in every lesson. ENGINE: OP_EXT dotm/
#               dcnt/htot/farv/medv/iqrw/madv/pctl/spnt/sslp/resd/sblw gain "worked"
#               (_dotm_* ... _sblw_*) and boards. Demonstrated numbers kept out of the
#               banks and pairs: the mode teach stacks over 14 (every mode 5..13, 15,
#               17, 18 is an ask); the even-list teach and worked pairs land on 7, 14
#               and 10 (the old 9, 12 and 19 were asks); the scatter teach reads a
#               cloud of its own (the old cloud WAS the slope-3 ask at 8 hours).
#   2026-09-06  BUILD tq -- PRECALC UNITS 7-9 TO THE SHAPE (12 lessons). Jim: "go".
#               PRECALC IS 36/36. THIS FILE:
#                 * Unit 7 (conics, parametrics): the circle with its radius marked "?"
#                   ([[circle r="?"]]) and the circle with its middle unnamed
#                   ([[circle center="?"]]) on the asks -- the [[conic]] grid would let
#                   the answer be counted, so it draws the walk-backs (cx= cy= at the
#                   true middle); the ellipse's two reaches as a tape, both blank; the
#                   ball's path with its t = 1 point, walked back as the vector at time t;
#                 * Unit 8 (series): the pattern's machine on the ask (writing the terms
#                   would do the adding), the terms as bars in the walk-back; the sigma
#                   recipe machine, its terms as bars; the crowd as a one-row array,
#                   line-ups beside teams as bars; the first three bounces as bars, walked
#                   back as hops that each cover half of what is left. The sigma pending
#                   line reads "k from 1 to 7" (the old "k = 1 → 7" was an arrow after an
#                   equals, 12 asks, live);
#                 * Unit 9 (limits): the line that never breaks; the machine that jams at
#                   the hole on the ask (the curve's hole sits at the answer), the line
#                   with its hole (hole=) in the walk-back; the step with its two shelves
#                   (piecewise func=), the pending line "x < 6: y = 11 · x ≥ 6: y = 19"
#                   (the old arrows after equals, 12 asks, live); the window on the curve
#                   (lines="x=2; x=10"), walked back as the line through the two ends.
#               Trap lines kept in every lesson. ENGINE: OP_EXT crad/cctr/elax/parm/gsum/
#               sigm/pasc/gser/lsub/lhol/lsid/avgr gain "worked" (_crad_* ... _avgr_*)
#               and boards. Demonstrated numbers kept out of the banks and pairs: every
#               radius 2..12 and every center 2..12 is an ask, so the radius teach un-
#               squares 225 (15) and the center teach and worked pairs sit at 15, 14, 13.
#   2026-09-06  BUILD tp -- PRECALC UNITS 4-6 TO THE SHAPE (12 lessons). Jim: "go".
#               THIS FILE:
#                 * Unit 4 (trig functions): a half turn beside the angle as bars, walked
#                   back as the half turns laid end to end (tape to ten, number-line hops
#                   past it); the arrow wound backwards on the circle with its values
#                   hidden, walked back as the same arrow named forwards; the flat line
#                   split at the arrow with the gap blank ([[angle deg="180" split=]]),
#                   walked back with both pieces; the plain sine beside the fast one on
#                   an axis in DEGREES ([[graph names=]]), walked back with the first
#                   repeat marked (lines="x=");
#                 * Unit 5 (identities): the hundred square with sine squared shaded
#                   ([[hundredgrid eq=]]) -- and the ask now SAYS "of the 100" (the old
#                   "cos² = ?/100" was a board problem the spoken words never read, rule
#                   44, 12 asks, live); the right triangle with its second sharp corner
#                   blank; the mirror stays picture-free on the ask (the pointed arrow is
#                   the answer) and walks back with the arrow and its values; the wave
#                   through its turns with the level line, the pending line a statement
#                   (the old "how many times?" was a question inside a step, 12 asks,
#                   live), walked back with the touches marked (points=);
#                 * Unit 6 (applications): the HONEST SAS triangle ([[triangle sas=]],
#                   new in geo-figures.js -- the schematic layout drew 150 looking sharp,
#                   which is why the old ask had words only); the ramp and the arrow's
#                   triangle captioned (rule 41: 24 asks drew a figure with no caption);
#                   THE COMPASS ([[unitcircle bearing= turn=]], new in math-figures.js)
#                   with the turn arc's far end unnamed, walked back at the new bearing;
#                   the arrow walked back as [[vector]] (it prints the length).
#               Trap lines kept in every lesson. ENGINE: OP_EXT rad1/nspn/refq/wper/
#               pyid/cofn/negf/sols/arsn/ramp/brng/vmag gain "worked" (_rad1_* ...
#               _vmag_*) and, where a picture withholds the answer, boards. Demonstrated
#               numbers kept out of the banks and pairs: the mirror lesson's bank asks
#               (90, sine) and (180, cosine) were the teach's own demonstrations -- they
#               are (360, sine) and (630, cosine) now; the crossings teach counts three
#               turns (every one- and two-turn combination is an ask).
#   2026-09-06  BUILD to -- PRECALC UNITS 1-3 TO THE SHAPE (12 lessons). Jim: "go".
#               THIS FILE:
#                 * Unit 1 (functions): two MACHINES in a row on the ask, g first with
#                   its output blank and f fed from it, both answered in the walk-back;
#                   the old point on the grid, walked back with where it landed; the
#                   root's doorway walked back as the curve of √(x − a) starting at the
#                   door (no picture on the ask: the curve starts at the answer); the
#                   border at 5 on the number line with x marked, walked back with the
#                   side named -- and the ask's pending line is "x = c · y = ?" (the old
#                   "x = c → ?" put an arrow after an equals, 12 asks, live);
#                 * Unit 2 (polynomials): the minus parade walked back as the ARRAY in
#                   two rows, the odd one left over (extra="1"; the pairing is the
#                   answer, so walk-back only); the plug-in machine with its output blank;
#                   the four rooms with the corner blank ([[areamodel ask="1"]] -- the
#                   end number is the corner room); the bottom walked back as the curve
#                   flying off at each zero (yrange=; the poles are the answer, so
#                   walk-back only);
#                 * Unit 3 (logs and exponentials): the log beside the log of the power
#                   as bars; the log machine run backwards with its input blank, walked
#                   back as the layers stacked and the machine answered; the tank halving
#                   day by day and the pile doubling year by year on the bars.
#               Trap lines kept in every lesson. ⚠️ no figure asks in these three units
#               before this build (no captions to miss) -- the pieces pending line was
#               the live find. ENGINE: OP_EXT fcmp/fshf/fdom/fpie/negp/remt/vprd/vasy/
#               logp/lsol/hcnt/cmpd gain "worked" (_fcmp_* ... _cmpd_*) and, where a
#               picture withholds the answer, boards. Demonstrated numbers kept out of
#               the banks and pairs (every old teach and pair already was).
#   2026-09-06  BUILD tn -- ALGEBRA 2 UNITS 7-9 TO THE SHAPE (12 lessons). THE COURSE IS
#               36/36. THIS FILE:
#                 * Unit 7 (patterns): the first three terms as BARS, walked back with
#                   every term to the asked one (the ride, the leaps); 1 up to n on the
#                   number line, walked back as the STAIRCASE RECTANGLE ([[rectangle
#                   half="1"]] -- half of n rows of n + 1 is the sum; bars past 19); the
#                   rule as a MACHINE with its output blank, walked back run twice;
#                 * Unit 8 (the unit circle): the height and across asks stay
#                   picture-free -- the renderer strips the spins and points the arrow,
#                   which IS the answer -- and their pending lines are statements (the
#                   old "where does the arrow point?" was a question inside a step, 24
#                   asks); walked back with the arrow pointed; the spin ask draws the
#                   arrow with its coordinates hidden ([[unitcircle values="0"]], new
#                   this build in math-figures.js) and walks back with the SAME arrow
#                   after the full turn; the wave walked back with its crest line;
#                 * Unit 9 (statistics): the five scores as bars with the mean beside
#                   them; shirts by pants as an array, then the hats; the plays as a pie
#                   with the paying ones shaded, walked back as wins-of-tokens on the
#                   array; the sample beside the school as bars.
#               Trap lines kept in every lesson. ⚠️ 12 graph asks drew with no caption
#               (rule 41), and the sample ask's spoken question -- "how many students in
#               the school" -- was rule 42's shape (the comparison referee, 12 asks; it
#               says "how many of the whole school" now). ENGINE: OP_EXT anth/gnth/gaus/
#               reca/sinp/cosp/spin/ampl/wavg/cnt3/expv/samp gain "worked" (_anth_* ...
#               _samp_*) and boards; _COMPASS names the four directions. Demonstrated
#               numbers kept out of the banks and pairs (the old times-again pair walked
#               (4, 2, 5) against the pair ask (4, 2, 4); the old pair-the-ends pair
#               walked 1 to 6, a bank ask; the old height teach walked 270 and 450 and
#               the across teach 810, all bank asks -- the height teaches on 90 and 630,
#               the across on 0 and 450, the pairs on 540/1260 and 720/1260; the old
#               stretched-wave teach drew 4·sin x, a bank ask, so it draws 20·sin x; the
#               old heavier-mean pair repeated the teach and walks (9, 4) now).
#   2026-09-06  BUILD tm -- ALGEBRA 2 UNITS 4-6 TO THE SHAPE (12 lessons). Jim: "go".
#               THIS FILE:
#                 * Unit 4 (division moves in): the sharing curve captioned, walked back
#                   with the point marked; the MACHINE run backwards -- input "?", output
#                   given -- and answered in the walk-back; the forbidden x asked on the
#                   jammed machine (no curve on the ask: the pole sits at the answer),
#                   walked back with the curve FLYING OFF at that x (yrange=); the
#                   survivor's curve walked back with the level line drawn (lines="y=a"
#                   beside func=);
#                 * Unit 5 (roots): the two roots' square walked back as the array (to
#                   10), the rectangle (to 20) or bars beyond -- walk-back only, its side
#                   is the answer; the one-half power walked back as the root beside the
#                   halving trap on the bars; the rooting machine with its input blank;
#                   the number between two squares ON THE NUMBER LINE, walked back with
#                   the hop to the nearer square;
#                 * Unit 6 (decay and logs): the sample fading day by day on the bars;
#                   the power machine with its exponent blank, walked back as the layers
#                   stacked; the two stacks of doublings joined; the number between two
#                   powers as three bars.
#               Trap lines kept in every lesson. ⚠️ 24 graph asks drew with no caption
#               (rule 41); under them, the logs-add pending line "a × b = ab · log ab =
#               ?" read as a × b by the unanswerable-choices referee (6 asks -- now two
#               lines), and the survivor's "which part survives? y → ?" was a question
#               inside a step (12 asks). ENGINE: OP_EXT rdiv/rsol/excl/rasy/rmul/rpow/rsq/
#               rbet/hlfl/logb/logm/lbet gain "worked" (_rdiv_* ... _lbet_*) and, where a
#               picture withholds the answer, boards; _sq_figure(k, total, cap) picks the
#               square's figure by its side. Demonstrated numbers kept out of the banks
#               and pairs (the old hidden-exponent pairs walked 2^?=8 and 10^?=1000 --
#               both pair asks -- so they walk 5^?=125 and 10^?=10,000; the old logs-add
#               pair walked 4 and 8, a bank ask, so it walks 2 and 64).
#   2026-09-06  BUILD tl -- ALGEBRA 2 UNITS 1-3 TO THE SHAPE (12 lessons). Jim: "go".
#               THIS FILE:
#                 * Unit 1 (absolute value, two clues, three): the two spots on the
#                   number line captioned, walked back with the steps between them hopped
#                   (hops=); the fence on the line, walked back as negatives, zero and
#                   positives on the BARS; the two shopping trips as TAPES (apple |
#                   apple | apple | banana | banana), walked back with the pair of apples
#                   left standing; the three clues as bars, walked back beside "everyone
#                   once" -- and the sys3 ask gains the pending line x + y + z = ? (the
#                   board-answers-the-question referee: the clues stood completed with
#                   no line ending in "?");
#                 * Unit 2 (the vertex, the roots, the test number, i): the curve
#                   captioned and walked back with the vertex marked (points=); the
#                   crossings marked; the test number walked back as two bars (a² against
#                   4b) beside the curve -- no picture on the ask, a curve would count its
#                   own crossings; x² = −a walked back as the square on the ARRAY (past a
#                   side of 10, the rectangle -- its side is the answer, so walk-back
#                   only), and the ask's pending line is its own line, "x = ? · i" (rule
#                   44: the old "i² = −1 · x = ? · i" carried a number the ask never
#                   spoke);
#                 * Unit 3 (polynomials): the two piles of x's as bars, joined in the
#                   walk-back; the degree beside its turns (no curve on the ask -- it
#                   would show them); the cubic with its three crossings marked; the
#                   MACHINE with its door blank, answered in the walk-back.
#               Trap lines kept in every lesson. ⚠️ 60 figure asks drew with no caption
#               (rule 41: graph 36, numberline 24). ENGINE: OP_EXT absv/absc/el2/sys3/vtx2/
#               rsum/disc/imag/pdeg/turnc/rsum3/pval gain "worked" (_absv_* ... _pval_*)
#               and, where a picture withholds the answer, boards. Demonstrated numbers
#               kept out of the banks and pairs (the old inside-the-distance teach used 3
#               -- a pair ask -- so it teaches on 5; the old wiggle-count why walked
#               degree 3 to two turns -- the same -- so it walks degree 4 to three).
#   2026-09-06  BUILD tk -- GEOMETRY UNITS 7-9 TO THE SHAPE (12 lessons). THE COURSE IS
#               36/36. THIS FILE:
#                 * Unit 7 (the grid): the up-and-down segment captioned and walked back
#                   with its steps counted; the slant walked back with the RIGHT TRIANGLE
#                   drawn under it on the grid and beside it as a [[righttriangle]]; the
#                   midpoint marked on the walk-back; the three corners captioned (the
#                   fourth never drawn) and the box closed in the walk-back;
#                 * Unit 8 (area and volume): the parallelogram DRAWN with its true height
#                   as a dashed line ([[polygon kind="parallelogram"]], new this build in
#                   geo-figures.js) and walked back pushed straight into a rectangle; the
#                   two rooms as two rectangles; the cube ([[solid kind="cube"]]) walked
#                   back as six faces on the bars; the box with every edge timesed;
#                 * Unit 9 (chance and counting): the bag as bars, walked back as the
#                   whole bag on a pie; rain against all the chances, walked back beside
#                   no rain; the outfit grid as an ARRAY (the area model would print the
#                   product); the two-way table captioned and read at the crossing.
#               Trap lines kept in every lesson. ⚠️ every figure ask in the three units
#               drew with no caption (rule 41, 72 asks: graph, twoway, bars), and the
#               two-rooms ask's pending line carried the room areas the ask never spoke
#               (rule 44, 12 asks -- now "a × b + c × b = ?"). ENGINE: OP_EXT vseg/dist/
#               mid2/corn/para/lshp/surf/svol/poft/notp/outc/twop gain boards and "worked"
#               (_vseg_* ... _twop_*). Demonstrated numbers kept out of the banks and
#               pairs (the old straight-up teach used (4, 2)-(4, 7) -- a bank ask -- so
#               the lesson now teaches on (1, 3)-(1, 8)). "students", never "children",
#               in the new prose.
#   2026-09-06  BUILD tj -- GEOMETRY UNITS 4-6 TO THE SHAPE (12 lessons). Jim: "go".
#               THIS FILE:
#                 * Unit 4 (similar shapes): the small triangle ABC beside its enlarged
#                   copy DEF with the asked side blank (sides="a,,"), walked back with
#                   every side filled; the factor asked on the bars (small beside big);
#                   the matching side on the two triangles; the area surprise on the
#                   rectangle of squares ([[rectangle w=b h=b]]);
#                 * Unit 5 (the right triangle): the hypotenuse asked on the triangle with
#                   the two legs written and the long side blank, walked back on the
#                   RIGHT TRIANGLE with adjacent/opposite/hypotenuse named; the missing
#                   leg the same way round; the tangent on the captioned right triangle
#                   (adjacent along the floor, opposite up the wall); the opposite side
#                   from the tangent;
#                 * Unit 6 (circles): the rest of the circle asked on the plain circle
#                   and walked back as the two arcs on a PIE ([[pie data=]] -- "the arc
#                   a° | the rest (360 - a)°"); the inscribed angle asked on the plain
#                   circle (inscribed= is a giveaway there: the renderer prints the
#                   answer) and walked back with the angle drawn on the rim; the arc
#                   asked with the angle drawn (inscribed="2a" labels the GIVEN);
#                   the arc length on the pie of equal parts, one shaded.
#               Trap lines kept in every lesson. ⚠️ every figure ask in the three units
#               drew with no caption (rule 41, 107 asks: triangle, righttriangle, bars,
#               rectangle, circle, pie). TUTOR.PY (this build): referee 68 (the second
#               triangle) read ABC beside DEF as one triangle redrawn -- it now reads the
#               v= names, so a second, differently named triangle is a second triangle.
#               ENGINE: OP_EXT scal/sfac/mside/sare/pyth/leg/tang/topp/cent/insc/iarc/
#               alen gain boards and "worked" (_scal_* ... _alen_*). Demonstrated numbers
#               kept out of the banks and pairs. Reason options that worked the
#               arithmetic aloud ("25 plus 144 is 169") reworded -- the spoken-math
#               referee sweeps the joined options.
#   2026-09-06  BUILD ti -- GEOMETRY UNITS 1-3 TO THE SHAPE (12 lessons). Jim: "start in
#               on the geometry." THIS FILE:
#                 * Unit 1 (angles, the circle, the midpoint): the square corner split and
#                   walked back with both pieces labelled; two lines crossed as the X with
#                   the twin labelled ([[angle cross=]]) and walked back on the straight
#                   line the neighbours share; the circle with its radius, walked back with
#                   the DIAMETER drawn edge to edge ([[circle d=]], new this build in
#                   geo-figures.js); the midpoint on the number line with the halfway mark;
#                 * Unit 2 (the three moves) on the GRID: the point captioned, then the
#                   point and where it landed (a slide, a flip across the mirror on x = 0,
#                   a half turn to the opposite spot); turn symmetry on the pie (past
#                   twelve parts, a written line);
#                 * Unit 3 (triangles): ABC beside its copy DEF (congruent); the ticked
#                   triangle with its base angles and the top blank, then all three; two
#                   angles with the third corner opened out; the apex with the base angles
#                   blank. Trap lines kept in every lesson.
#               ⚠️ every figure ask in the three units drew with no caption (rule 41, 138
#               asks: triangle, graph, angle, numberline, circle, pie). The geometry
#               vocabulary referee: an angle is never a "piece". Every lesson: why,
#               picture, teach, pairs, walk-back, reason, recap. ENGINE: OP_EXT comp/vert/
#               circ/mid/tran/refl/htrn/rota/cong/isos/extr/chas gain boards and "worked"
#               (_comp_* ... _chas_*). Demonstrated numbers kept out of the banks (the old
#               rota teach used 4 and 5 parts and the old isos teach 50 -- all asks; rota's
#               twelve divisors of 360 leave only 6 and 12 free, so the lesson teaches on
#               those two).
#   2026-09-06  BUILD th -- ALGEBRA 1 UNITS 7-9 TO THE SHAPE (12 lessons). THE COURSE IS
#               36/36. THIS FILE:
#                 * Unit 7 (the four rooms) on the AREA MODEL with two new ask modes
#                   (math-figures.js, this build): the four rooms asked with the MIDDLE
#                   rooms blank and the corner given ([[areamodel ask="x"]]); factoring
#                   and the common factor asked with one SIDE hidden and the sum left
#                   whole (ask="side"); the difference of squares asked with the corner
#                   blank and the middles showing, so the cancelling is seen;
#                 * Unit 8 (curves) on the GRID: the curve with a vertical line at the
#                   asked x; the bowl with one ground point marked and the other asked;
#                   the lowest point asked and then marked; the falling ball marked at
#                   its launch and its landing;
#                 * Unit 9 (the three middles): the mean as a pile shared into hidden
#                   parts on the TAPE; the median and the odd-one-out on the DOTPLOT,
#                   captioned; the range as two bars, then the stretch on the NUMBER
#                   LINE. Trap lines kept in every lesson.
#               ⚠️ every graph, dotplot and bar-chart ask in the three units drew with
#               no caption (rule 41, 72 asks); underneath, the vtx and outl asks ended on
#               lines the spoken question never read ("... bottoms out at 0 — lowest y =
#               ?", "mean = 13 · median = ?") -- split into a plain line and "lowest y =
#               ?" / "median = ?". Every lesson: why, picture, teach, pairs, walk-back,
#               reason, recap. ENGINE: OP_EXT foil/fnum/gcfx/dsq/sqy/roots/vtx/hitg/mean/
#               medn/rnge/outl gain boards and "worked" (_foil_* ... _outl_*).
#               Demonstrated numbers kept out of the banks (the old fnum teach worked
#               (x + 2)(x + 3), the old gcfx pair 8x + 6, the old mean pairs 28-in-4 and
#               54-in-6, the old medn pairs, the old outl pair 6-and-26: all bank or pair
#               problems). hitg's every square from 9 to 196 is a bank ask; its teach
#               keeps 25 (teachaudit reads the tuple, and the beat opens on 25, not 5).
#   2026-09-06  BUILD tg -- ALGEBRA 1 UNITS 4-6 TO THE SHAPE (12 lessons). THIS FILE:
#                 * Unit 4 (lines) on the GRID: reading the line asks with a vertical line
#                   at the given x ("climb from x = 6 up to the line") and walks back with
#                   the point marked; the climb asks with the two points and walks back
#                   with the line drawn through them; the start asks the left wall and
#                   marks (0, b); start-and-climb marks the point reached;
#                 * Unit 5 (two rules): where-two-rules-agree asks on TWO LINES with the
#                   crossing ringed but unlabelled ([[graph cross="ask"]], new this build
#                   in math-figures.js -- the auto-label used to print the answer);
#                   swapping-in, sum-and-difference and the eraser as BARS (two x's and
#                   the a against b; bigger as smaller-and-more; the two trips side by
#                   side, the difference one pencil);
#                 * Unit 6 (powers): the x's written out as a bar and counted (joining
#                   adds); b copies of x^a as a bar (copying times); a digit on the
#                   PLACE-VALUE CHART moved up a places (times ten to a power); the
#                   doubling pond as BARS one day short, then to the end. Trap lines kept.
#               ⚠️ every graph ask in the three units drew with no caption (rule 41, 58
#               asks), and the sys2 ask ended on "2x = 8 → x = ?" -- a line the spoken
#               question never read AND an arrow after an equals sign; it is "2x + a = b"
#               then "x = ?" now. Every lesson: why, picture, teach, pairs, walk-back,
#               reason, recap. ENGINE: OP_EXT lny/slp/yint/lin2/sys1/sys2/sumd/elim/exadd/
#               exmul/sci/dbl gain boards and "worked" (_lny_* ... _dbl_*, _line_spec).
#               Demonstrated numbers kept out of the banks (the old lny teach worked
#               y = x + 2 at x = 3 and the old sci teach 3 × 10², both bank problems; the
#               old dbl pair worked 2 pads for 4 days, a bank problem).
#   2026-09-06  BUILD tf -- ALGEBRA 1 UNITS 1-3 TO THE SHAPE (12 lessons). Jim: "start on
#               algebra." THIS FILE:
#                 * Unit 1 (expressions) as BARS: bx + c is b copies of x then the c (the
#                   plus waits its turn); x + cy is one x then c copies of y (each letter
#                   its own number); ax + by + cx is the bar in the order written, the x
#                   pieces counted past the y, then collected as two proportional parts;
#                   a(x − b) on the AREA MODEL asked with the taken-away room blank
#                   ([[areamodel ask="1"]] now keeps the sign: "= 4x - ?");
#                 * Unit 2 (equations) on the BALANCE: x + a = b drawn level, a off both
#                   sides, x alone against the answer, put back to check; ax = b as a
#                   copies of x on the pan and as a bar shared; ax + b = c as the scale
#                   after each undo (last on, first off); x + a < b on the number line
#                   with the OPEN circle and the shaded ray, the biggest whole number
#                   marked in the walk-back;
#                 * Unit 3 (functions) on the MACHINE: the rule run in order with its
#                   two steps written; f(b) with the output blank; two machines nose to
#                   tail, the second's output blank; the input blank and found by undoing
#                   the rule, then run forwards to check. Trap lines kept in every lesson.
#               ⚠️ every machine and number-line ask in the three units drew with no
#               caption (rule 41); every ask carries one now. Every lesson: why, picture,
#               teach, pairs, walk-back, reason, recap. ENGINE: OP_EXT ev2/evxy/cl2/dstm/
#               un1/un2/un3/ineq/fm1/fnot/fm2/fback gain boards and "worked" (_ev2_* ...
#               _fback_*, _cl2_tape). Demonstrated numbers kept out of the banks (the old
#               dstm pair worked 3(x − 4), a bank problem).
#   2026-09-06  BUILD te -- PREALGEBRA UNITS 7-9 TO THE SHAPE (12 lessons). THIS FILE:
#                 * Unit 7 (percent) on the TAPE: the number cut into ten equal parts --
#                   ten percent is one part -- and the taken parts marked (any percent);
#                   the share as a bar beside the HUNDRED GRID holding the same share
#                   out of 100 (what percent); the ten parts found from the part
#                   (finding the whole); the price and the change as one bar, put on or
#                   taken off (a price up or down);
#                 * Unit 8 (measurement, geometry): one bar part per big unit with the
#                   small units in each (changing units); the RECTANGLE ROUND THE
#                   TRIANGLE with its diagonal drawn and half filled ([[rectangle
#                   half="1"]], new this build in math-figures.js) -- a right triangle
#                   is half a rectangle, seen; the straight line split with both pieces
#                   labelled; the triangle with its three angles;
#                 * Unit 9 (the first letters): x + b as a bar of x and b, x swapped for
#                   its number (a letter holds a number); bx as b COPIES of x side by
#                   side (a number against a letter); ax + bx as one bar counted
#                   (collecting); the AREA MODEL asked with the number room blank
#                   ([[areamodel ask="1"]], new this build) and read filled (the times
#                   reaches both). Trap lines kept in every lesson.
#               ⚠️ the pcn/pwh/tri/tri3 asks ended on a line the spoken question never
#               read ("3 × 3 = ?", "100% = 4 × 10 = ?", "24 ÷ 2 = ?", "180° − 110° = ?")
#               -- rule 44 hits the old sweep never saw because rule 41 (no caption)
#               fired first; the pending line now carries the numbers the ask speaks
#               ("30% of 30 = ?", "12 is 30% of ?", "6 × 4 ÷ 2 = ?", "180° − (50° +
#               60°) = ?"). The dst ask used to print the answer (12) in the area
#               model's number room. Every lesson: why, picture, teach, pairs,
#               walk-back, reason, recap. ENGINE: OP_EXT pcn/asp/pwh/pup/cnv/tri/sla/
#               tri3/evx/mlx/clt/dst gain boards and "worked" (_pcn_* ... _dst_*,
#               _ten_tape, _clt_tape, _CNV_UNITS). Demonstrated numbers kept out of the
#               banks (the old pup teach worked 40 up 10%, a bank problem; tri now
#               teaches 8 by 3, mlx x=9, dst 4(x + 3)).
#   2026-09-06  BUILD td -- PREALGEBRA UNITS 4-6 TO THE SHAPE (12 lessons). THIS FILE:
#                 * Unit 4 (fractions) on the TAPE (a fraction of a number: the whole cut
#                   into the bottom's parts, the top's parts taken; parts in a whole) and
#                   the FRACTION LINE (dividing by a fraction as HOPS of the fraction --
#                   the measurement picture -- with the flip-and-times ladder when the
#                   hops would be too many; fractions bigger than one hopped a whole at a
#                   time with the left-over drawn);
#                 * Unit 5 (decimals) on the HUNDRED GRID (hundredths: rows are tenths),
#                   the place-value chart's new TENTHS column (times by ten moves the
#                   digits across it), the tenths line with hops, and the array of
#                   tenths shared out;
#                 * Unit 6 (ratio) as TWO TAPES (the batch and the batches, both sides
#                   timesed), sharing then groups on the array (a rate), TWO PIES cut
#                   two ways (a proportion; the ladder when the pie would need more than
#                   twelve parts), the tape cut into the counted parts (sharing in a
#                   ratio). Trap lines kept (rat, prop).
#               ⚠️ the old dbf asks wrote the FLIPPED form under the question -- the
#               method, given away -- and "c ÷ a/b" is read by the choices referee as
#               (c ÷ a)/b; a divisor fraction is written in parentheses now. Every lesson:
#               why, picture, teach, pairs, walk-back, reason, recap. ENGINE: OP_EXT
#               nuf/uic/dbf/imp/hun/x10/dth/dsh/rat/rte/prop/shr gain boards and "worked"
#               (_nuf_* ... _shr_*, _dbf_hops). Demonstrated numbers kept out of the
#               banks (nuf 2/5 of 10, uic sixths-in-2, dbf 4÷2/3, imp 7/3, hun 0.45 and
#               0.5, dth 0.5×5, rte 18-in-3-for-5 were all bank problems).
#   2026-09-05  BUILD tc -- PREALGEBRA UNITS 1-3 TO THE SHAPE (12 lessons). Jim: "leave
#               basic aside from now and go to prealgebra." THIS FILE:
#                 * Unit 1 (order of operations) on the LADDER -- [[solve]] marching the
#                   moves down the board ("times first", "then add"); a square number on
#                   the area model, a cube as a BLOCK OF CUBES ([[solid]]) -- the course's
#                   first honest picture of a to-the-power-3;
#                 * Unit 2 (factors) on RECTANGLES -- the factor pairs written and one
#                   drawn (array, or the area model when wide); the smallest-factor hunt
#                   as the tries in order, the first fit ticked; primes on the ladder
#                   ("pull out 2"); the biggest factor as the smallest one's partner;
#                 * Unit 3 (integers) on the NUMBER LINE with the move drawn as HOPS.
#                   ⚠️ the cbz/addneg asks used to mark the LANDING POINT -- the answer
#                   drawn on the question; they mark the START now (subneg too), and
#                   the walk-back hops. Times with a negative is b hops of a from zero.
#               Every lesson: why, picture, teach, pairs, walk-back, reason, recap; the
#               trap line kept (bfac). ENGINE: OP_EXT tba/parf/expn/exo/nfac/spf/npf/bfac/
#               mulneg gain "worked"; cbz/addneg/subneg gain boards and "worked"
#               (_tba_worked ... _mulneg_worked; _factor_pairs, _pair_board, _npf_ladder,
#               _int_range, _neg). validate: a negative answer may be named "negative 4".
#   2026-09-05  BUILD tb -- ENTRY UNIT 1 TO THE SHAPE (the youngest students). Counting
#               to 10 and past ten on the STARS counted one at a time; before-and-after
#               and which-is-bigger on the NUMBER LINE (one hop up / back; the later
#               number is bigger). Each lesson: why, picture, teach, pairs, recap.
#               Ruling ⑤ keeps the quick praise for counting and comparing (no
#               walk-back); NO reason question in this unit -- its options are text a
#               student learning to count cannot read yet (open ruling). ENGINE: "big"
#               asks draw the two numbers on the line (the comparing method IS the
#               picture). Nothing else changed.
#   2026-09-05  BUILD ta -- the `intervene` step carries "board": the ask's board as it
#               was drawn (pending["board"], board_for as the fallback), so the model
#               that steps in is told exactly what the student is looking at (flag
#               22:31). Nothing else in the engine changed.
#   2026-09-05  BUILD sz -- THE TIMES TABLE IS A PASS, NOT A STREAK. Jim's flag 22:40 and
#               his rulings ⑥ ⑦: 1-9 times 1-9, complete on ONE clean pass, a slip
#               restarts it. ENGINE: "mastery": "table" (TABLE_MAX / TABLE_SIZE /
#               TABLE_MAX_MISSES settings); start(lesson, seed=None) seeds the shuffle;
#               table_facts(), _table_order/_board/_miss/_begin/_ask/_praise_index;
#               step(): pair-1 -> phase "table", a right fact earns praise and the
#               next fact (no walk-back inside the pass), the 81st earns the reason
#               question; a slip draws the fact's array counted down the rows, says
#               LINE_TABLE_RESTART and deals a fresh shuffle; the fifth slip in a
#               sitting says LINE_TABLE_REST and ends warmly. _ask() takes a board
#               override and REMEMBERS the board in pending (a re-ask keeps the
#               counter). "*" gains _mul_choices (neighbouring FACTS as distractors).
#               audio_lines: the 81 facts asked/re-asked, one praise each, the slip
#               lines, the two standing lines. validate #11: the table lesson's
#               promises. LESSON: basic-u2-times-tables says "mastery": "table"; its
#               practice intro and advance line say the pass, never "three in a row".
#   2026-09-05  BUILD sy -- BASIC UNIT 9 TO THE SHAPE (measuring) -- AND WITH IT THE WHOLE
#               BASIC COURSE, 36 LESSONS. THIS FILE: perimeter and area on the new
#               RECTANGLE on a unit grid (the walk around traced; the squares inside
#               filled); quarter turns on the CIRCLE cut into four; volume as one
#               layer (an array) times the layers, beside the box ([[solid]]). ENGINE:
#               OP_EXT peri / area / ang / angq / vol gain boards and "worked".
#   2026-09-05  BUILD sx -- BASIC UNIT 8 TO THE SHAPE (percent). THIS FILE: what-percent
#               on the HUNDREDTHS SQUARE in percent mode (the part asked as a pie or a
#               bar); percent-of as the SHARING picture (50 percent is one of two equal
#               parts); percent-off on the TAPE (the discount and what you pay, side by
#               side under the price); what-one-costs as the dollars shared over the
#               apples. Both trap lines kept. ENGINE: OP_EXT wpc / pc / poff / rate gain
#               boards and "worked".
#   2026-09-05  BUILD sw -- BASIC UNIT 7 TO THE SHAPE (decimals and money). THIS FILE:
#               tenths on the 0-to-1 line (it already speaks in tenths); hundredths and
#               tenths-meeting-hundredths on the new HUNDREDTHS SQUARE ([[hundredgrid]]
#               -- a tenth is a full row); dimes and pennies on the PLACE-VALUE CHART
#               (dimes are tens). The tenths-and-hundredths trap line kept. ENGINE:
#               OP_EXT dt / dh / m / t2h gain boards and "worked".
#   2026-09-05  BUILD sv -- BASIC UNIT 6 TO THE SHAPE (adding and taking away fractions).
#               THIS FILE: all four lessons on the FRACTION LINE -- same bottom: start at
#               the first fraction and hop by the second (back, for taking away);
#               different bottoms: the first fraction found on the FINER line, then the
#               hop. The unlike-bottoms trap line kept. ENGINE: OP_EXT fa / fs / fu / fus
#               gain boards (the line with the start marked, the hop withheld) and
#               "worked" (the hops drawn); _fl helper.
#   2026-09-05  BUILD su -- BASIC UNIT 5 TO THE SHAPE (fractions). THIS FILE:
#                 * fractions-on-the-number-line on the FRACTION LINE ([[numberline
#                   denom=]] -- ticks and hops labelled in fourths), the hops drawn;
#                 * fraction-of-a-group on the ARRAY shared into equal parts;
#                 * equivalent-fractions and simplest-form on TWO PIES holding the same
#                   amount cut two ways; the simplest-form trap line kept.
#               ENGINE: OP_EXT nl / nlw / of / eqf / simp gain boards and "worked"
#               (_nl_*, _nlw_*, _of_*, _eqf_*, _simp_*; _frac_line helper). A pie
#               holds at most 12 parts, so simplest-form asks with a bigger bottom
#               are bare and their walk-back draws the simplified pie only.
#   2026-09-05  BUILD st -- BASIC UNIT 4 TO THE SHAPE (factors and multiples). THIS FILE:
#                 * missing-factors on the ARRAY: b boxes, a dots -- the sharing question
#                   in disguise -- then the boxes filled;
#                 * factor-pairs as a RECTANGLE (rows of dots when small, the area model's
#                   one cell with its sides labelled when big); the trap line kept;
#                 * greatest-common-factor on the VENN: the two factor lists, the overlap
#                   holding what they share;
#                 * least-common-multiple on TWO NUMBER LINES: count-by hops on each, the
#                   first shared landing marked.
#               ENGINE: OP_EXT mf / fpr gain a board and a "worked" (_mf_*, _fpr_*); gcf
#               gains _gcf_worked (the Venn); lcm gains _lcm_board (two bare count-by
#               lines) and _lcm_worked (the hops). _factors(n) helper.
#   2026-09-05  BUILD ss -- BASIC UNIT 3 TO THE SHAPE (the dividing unit). THIS FILE:
#                 * what-dividing-means on the ARRAY read the other way -- the dots to
#                   share and the empty boxes (the sharing question as a picture), then
#                   the boxes filled;
#                 * left-overs on the array with extra= (the red dots that did not fit);
#                 * divide-two-digit on the AREA MODEL backwards (tens and ones shared);
#                 * story-problems with BOTH pictures side by side -- groups put
#                   together (times) and a pile shared out (divided by).
#               ENGINE: OP_EXT "/" gains _div_board / _div_worked (sharing picture while
#               small -- a <= 45, quotient <= 9; the area model for a split two-digit
#               number); "rem" gains _rem_board / _rem_worked; a STORY problem's array
#               reads the story (b groups of a) -- _mul_rows_cols.
#   2026-09-05  BUILD sr -- BASIC UNIT 2 TO THE SHAPE (the multiplying unit). THIS FILE:
#                 * what-multiplying-means on the ARRAY in equal-groups view;
#                 * times-tables on the array (the ask stays bare -- recall, not
#                   counting; every worked beat and walk-back draws it);
#                 * multiply-two-digit on the AREA MODEL split into tens and ones;
#                 * times-by-ten on the PLACE-VALUE CHART (which grew a Thousands
#                   column) -- the digits are seen moving up a column.
#               ENGINE: OP_EXT "*" gains _mul_board (the array on the ask only while
#               both numbers are 5 or under -- the meaning lesson) and _mul_worked
#               (array, or the area model for a two-digit number); "mtz" gains a chart
#               ask board and _mtz_worked. The "Here is the trap" line in times-by-ten
#               is kept verbatim (se: a wider ruling is Jim's).
#   2026-09-05  BUILD sq -- BASIC UNIT 1 TO THE SHAPE. Jim, after running sp's rounding
#               prototype: "This is exactly what I want. I would like all lessons to be
#               taught this clearly and demonstrated this way using graphic." His
#               rollout choice: Basic Unit 1, then the rest of Basic. THIS FILE:
#                 * basic-u1-place-value-to-1000 rewritten to the shape on the new
#                   [[placevalue]] chart (flats / rods / cubes, math-figures.js);
#                 * basic-u1-rounding-hundreds rewritten on the number line, one
#                   place over (_r100_line / _r100_walkback);
#                 * basic-u1-multi-digit-review rewritten on the stacked COLUMN, the
#                   carry drawn above (carries=) and the regrouping drawn over the
#                   struck digits (borrows=, new in board.js); the old "terrible" teach
#                   line is gone -- the rule is read off the two columns.
#               ENGINE: BASE_WORKED gives the base ops (+, -, t) walk-back pictures --
#               _col_add / _col_sub narrate the column from the ones up; tens-and-ones
#               draws the chart -- and _worked_for consults it after OP_EXT. OP_EXT pv
#               and r100 gain "worked"; their ask boards draw the chart (digits hidden)
#               and the number line (no hop). board_for: a problem with TWO two-digit
#               numbers is asked on [[column]] at every level (Jim's 22:35/22:36 flags:
#               carrying and regrouping were taught over a flat line) -- four lessons.
#   2026-09-05  BUILD sp -- THE LESSON LEARNS TO TEACH. Jim, after a live run through
#               Entry and Basic: "there is not so much emphasis on teaching as there is
#               on giving problems ... just saying something once doesn't mean that it
#               has been learned ... are we really in the business here of teaching, or
#               are we just trying to create a teaching app?" His choice: shape first,
#               prototype on rounding. THE SHAPE (claude/Design_What_A_Lesson_Is): seven
#               beats -- Why, Picture, Teach, Show, Try (with the WALK-BACK after a right
#               answer), Say it (a REASON question, graded in code), Come back (the
#               RECAP). Every one is an OPTIONAL lesson field, so the other 359 lessons
#               play byte-for-byte as before:
#                 "why"      [(spoken, board)...]  what the skill is FOR, before any rule
#                 "picture"  [(spoken, board)...]  the representation, drawn BEFORE the rule;
#                                                  replayed when the reason question misses
#                 "show_work_on_correct": True     after every right answer the board shows
#                                                  the work (OP_EXT[op]["worked"]) -- ruling ⑤
#                 "explain"  {spoken, choices, answer, board}  asked ONCE, after the streak;
#                                                  right -> mastered; a miss replays the
#                                                  picture and asks again; two misses end
#                                                  warmly as still-learning (the warm choice)
#                 "recap"    [(spoken, board)...]  the rule and the why, said again before
#                                                  EVERY end line
#               The reason ask is an `ask` with reason=True, problem=None, tap_only=True
#               and TEXT choices; main.py grades the tapped label in code (never the
#               model). OP_EXT r10 gains "worked" (the number line with the hop) and its
#               ask board now draws the number line -- Jim: "a number line anytime we talk
#               about rounding". basic-u1-rounding-tens is rewritten to the shape (the
#               prototype he will run). validate() and audio_lines() cover every new
#               field, so the closure and the canon hold. PART 3il pins it both ways.
#   2026-09-04  BUILD sn -- THE WARM CHOICE. Jim's ruling ③ (2026-09-04): at a still-
#               learning lesson end the student picks -- "go on to the next lesson, or
#               review this a bit more to get it solid?" -- instead of the page handing
#               the seam to the live tutor. LINE_STILL_LEARNING_CHOICE, his words
#               verbatim, joins STANDALONE_LINES beside rj's LINE_NEW_TOPIC so it is
#               pre-rendered. The engine's end steps are untouched: main.py's
#               _script_clean adds the pointer, session.html renders the two buttons.
#   2026-09-02  BUILD se -- JIM'S FLAG on the entry count-on lesson: "Drop the term
#               'trap' and everything after it." The teach line now ends on the
#               count ("...Fourteen stars."). Its clip re-renders from the new text
#               on first play. The 40-odd "Here is the trap" lines in OTHER courses
#               are the house pattern and are deliberately untouched -- a wider
#               ruling is Jim's to make.
#   2026-09-01  BUILD rj -- THE SEAM IS ANNOUNCED. Jim, after watching ri live: the class
#               "stopped after 3 in a row then thought for a bit and then acted as if we
#               had been working on subtraction. This is strange." What he saw: a mastered
#               scripted lesson hands the class to the LIVE tutor (__script_done__), which
#               picked the next topic (one-less -- reads as subtraction) with no
#               announcement; the "thought for a bit" was the model call. His ruling
#               (asked): ANNOUNCE IT, THEN CONTINUE. One new course-level line,
#               LINE_NEW_TOPIC, joins STANDALONE_LINES (pre-rendered like Abrabot's
#               introduction; held to the same canon by PART 3di): session.html speaks it
#               after a MASTERED end, and main.py now turns __script_done__ into a system
#               note telling the live tutor to NAME the new topic first and put it on the
#               board. Words only in this file -- one new spoken line, one prewarm render.
#   2026-09-01  BUILD ri -- THREE IN A ROW MEANS MOVE ON. Jim's live catch (session,
#               'Count the stars'): "I gave three correct answers and it gave me a
#               4th question." Every lesson PROMISES "Three right answers in a row
#               and we're done" (practice_intro, 49 copies) but the advance gate
#               also demanded done >= MIN_PROBLEMS (4), so a perfect child was
#               asked a 4th problem the words never warned about. Jim's ruling:
#               "The three in a row is what it specifically states to demonstrate
#               that we're ready to move on to the next stage." So the CODE now
#               matches the WORDS: the gate is streak >= ADVANCE_STREAK alone, and
#               MIN_PROBLEMS (the 2026-08-20 research ruling's DI-firming floor)
#               is REMOVED -- Jim's ruling supersedes it. A child who misses still
#               does more than three (the miss resets the streak), and MAX_PROBLEMS
#               still caps every path. No spoken line changed -- NO TTS RE-RENDERS.
```

---

Moved out of `lessonscripts.py` on 2026-09-08 (build ui): every CHANGE NOTE dated before 2026-09-01 -- 70 entries, VERBATIM, in the order they sat in the file (newest first). The 39 notes from 2026-09-01 on stay at the top of `lessonscripts.py` itself, and new notes keep going there. Nothing below was edited; grep this file for a build letter or a date. When the header is rolled out again, the newer block is added ABOVE this one.

```text
#   2026-08-30  BUILD qt -- THE COUNTING LESSONS ACTUALLY COUNT. Build qs taught the board
#               to count along ([[objects ... count="1"]]: the things land one at a time,
#               each taking its own ✓ and number, paced to his voice) and nothing in the
#               canon used it yet -- only the AI intervention asked for it. Every authored
#               card that draws countable things was read (33 of them, by the battery's own
#               walker) and 11 were counted here: the ones where Mr. Cadabra counts the
#               drawing HIMSELF, out loud, while he models.
#               ⚠️ THE ONES DELIBERATELY LEFT PLAIN, so the next pass does not "finish the
#               job" and undo the thinking:
#                 * every COUNT-ON card ("count on from seven: eight, nine...") -- ticking
#                   every star from 1 teaches the exact habit counting-on exists to replace,
#                   so the picture would be arguing with the lesson;
#                 * every TAKE-AWAY card -- they carry take=, which the count-along refuses;
#                   you do not count UP to a struck-out star;
#                 * anything over a dozen things (counting-past-ten's 13, 14 and 16, and
#                   add-past-ten's 13 and 15) -- the renderer refuses past OBJ_COUNT_MAX, and
#                   a tag that asks for something the renderer will not do is a lie in the
#                   source even though it draws correctly;
#                 * the multiplication card (the apples are GROUPS, so 1..6 under them would
#                   be counting the wrong thing), the geometry POINT card (its caption already
#                   names them A, B and C) and the subtracting card (its picture is about what
#                   is taken, not what is counted up).
#               BOARD LINES ONLY -- not one spoken line changed, so NO TTS CLIP RE-RENDERS.
#   2026-08-29  BUILD qc -- THE BARS ARE ON THE BOARD. Jim's screenshot of the Algebra
#               II opener (alg2-u1-how-far-from-zero, teach[0]): the words say "here are
#               two straight bars around a number" and the board showed only the number
#               line. |4| = 4 and |−4| = 4 now lead the board. Spoken line untouched --
#               no new audio key. PART 3gh.
#   2026-08-28  BUILD pv -- A HYPHEN MARKED A RIGHT ANSWER WRONG. Jim said "sixty-one
#               degrees" to a Geometry angle question (90 - 29); the recogniser wrote
#               "Si-61 degrees" and read_answer returned NEGATIVE 61, so a correct
#               child was told "Not quite" and dropped into an AI intervention that
#               then taught adding zero with its tags printed as text. ONE CHARACTER,
#               THREE VISIBLE FAILURES. _RA_NUMERAL's sign now requires that the
#               character before it is not a LETTER. Digits still count ("3-5" keeps
#               its old reading) -- the defect is a word prefix and the fix is no
#               wider than the defect. See ruletests PART 3fz.
#   2026-08-28  BUILD pp -- THE LAST TWO COURSES. THE WHOLE CURRICULUM IS READ.
#               Jim: "Finish the last twenty percent now." Probability & Statistics
#               and Differential Equations, all 72 lessons, line by line. With these
#               two, EVERY ONE OF THE 360 AUTHORED LESSONS in all ten courses has
#               been read for sense by a human-shaped pass, not just validated.
#               ⭐ NEITHER COURSE HAS A SINGLE PROSE DEFECT. No broken sentence, no
#               false statement, no leaked shorthand -- four courses running now.
#               FORTY-EIGHT changes, all one shape: a worked example that stated its
#               answer without doing the operation. 22 in Prob & Stat, 26 in Diffeq.
#               ⚠️ DIFFEQ IS THE ONLY COURSE WHERE THE *FIRST* EXAMPLE WAS ALSO BARE.
#               Build pi's finding was about the second example ("One more together"),
#               because in the other nine courses the first one -- "Here is one more,
#               done for you" -- reliably showed its working. Diffeq breaks that: six
#               of its FIRST examples collapsed to the answer too ("A slope of 14 at
#               x equals 4: the nullcline sits at 56"). They are fixed here, and the
#               asymmetry is recorded rather than assumed away.
#               ⚠️ AND A DETECTOR WAS CUT, under the canon sweep law. An operation-word
#               regex run over all 360 second examples returned 39 hits and nearly
#               every one was a FALSE POSITIVE -- because in Entry, counting aloud IS
#               the working ("One, two, three, four, five, six. Six stars."), and in
#               Algebra II so is a doubling chain ("56 to 28 to 14"). The defect
#               cannot be found by machine; it was found by reading, and that is why
#               the read had to happen at all. See ruletests PART 3ft.
#   2026-08-28  BUILD po -- CALCULUS, READ FOR SENSE. All 36 lessons read line by
#               line. ⭐ ITS PROSE IS CLEAN -- the second course running with no broken
#               sentence, no false statement, no leaked shorthand. And it teaches the
#               subject the way a good teacher does: the Fundamental Theorem arrives
#               as "areas and antiderivatives are one idea wearing two hats"; the
#               chain rule's omission is named as "the commonest mistake in all of
#               Calculus"; accumulation is settled in one line -- "an integral
#               measures the CHANGE, never the amount"; and the last lesson of the
#               course is "a quiet one", asking a rate where it stops.
#               TWENTY-TWO changes, every one build pl's shape: a second worked
#               example stating the answer without doing the operation.
#               ⚠️ AND THE COUNT ITSELF IS THE FINDING. 22 in Calculus and 16 in
#               Pre-Calculus, against 4 in Algebra One. The defect gets MORE common
#               as the mathematics gets harder, and the reason is visible in the
#               lines: an upper-course operation is a one-liner ("162 over 18 is 9",
#               "half of 56"), so an author writing at speed states the result and
#               moves on -- where a multi-step Basic method forces the working onto
#               the page whether the author meant to write it or not. The courses
#               that need the working shown most are the ones least likely to have it.
#   2026-08-28  BUILD pn -- PRE-CALCULUS, READ FOR SENSE. All 36 lessons read line by
#               line. ⭐ ITS PROSE IS CLEAN -- not one broken sentence in the whole
#               course, the first course where that is true. And it is the best-built
#               course in the product for a different reason: it keeps its promises
#               ACROSS units and across years. Algebra Two was told the roots' product
#               "would be famous later"; Vieta's lesson opens "Later is now." The
#               doorway lesson answers division's forbidden x with its opposite --
#               "zero under a root is WELCOME." The last lesson shrinks a window
#               toward a point, reaches 8, and says "that limit is called the
#               derivative, and Calculus starts exactly there." A curriculum that
#               remembers what it said is rarer than one that says it well.
#               SIXTEEN changes, every one of them build pl's shape: a second worked
#               example that states the answer without doing the operation. No prose
#               defects, no leaks, no false statements.
#   2026-08-28  BUILD pm -- ALGEBRA TWO, READ FOR SENSE. All 36 lessons read line by
#               line -- the course whose absolute-value beat started this whole
#               thread. ⭐ IT READS WELL NOW. pe's rewrite of lesson one landed, and
#               the rest of the course was never the problem: Gauss put his slate
#               down in seconds; expected value is "not a promise, a center of
#               gravity"; the fencepost error returns as "the fencepost from the grid
#               unit, wearing a new coat". Ten changes in 36 lessons.
#               ⚠️ ONE WAS A NEW KIND OF DEFECT, AND THE ONLY ONE OF ITS KIND IN THE
#               WHOLE CURRICULUM: INTERNAL SHORTHAND SPOKEN TO A CHILD. The roots
#               lesson said "stopping there is pyth's old stopped-at-the-square
#               slip." "pyth" is THIS CODEBASE'S ABBREVIATION for the Pythagoras op.
#               It is not a word. A student hearing it has been handed a filename.
#               A sweep of all 360 lessons for op codes and build letters spoken as
#               English found exactly this one -- the other four hits were ordinary
#               possessives ("the leg's square", "the area's rate") that happen to
#               collide with op names. Isolated, and now gone.
#               The other nine are build pl's shape: a second worked example that
#               states the answer without ever doing the operation.
#   2026-08-28  BUILD pl -- GEOMETRY, READ FOR SENSE. All 36 lessons read line by
#               line. ⭐ THE COURSE IS EXCELLENT, and what carries it is that every
#               unit's trap is a MISTAKE SOMEONE ACTUALLY MAKES, named out loud: 180
#               leaping to mind inside a 90-degree corner because the straight-line
#               lesson came first; a fence with six posts and five rails; the slanted
#               side of a parallelogram that is longer than its height, so grabbing
#               it "always looks generous"; and volume punished by "the course's own
#               history" -- times the factor once is the LENGTH habit, twice is the
#               AREA habit. Seven changes in 36 lessons, all of one shape.
#               ⚠️ THE SHAPE, sharper here than anywhere: the FIRST worked example
#               states the OPERATION and the second states only the ANSWER.
#                   W1  "The arc measures 56 degrees, so the inscribed angle is
#                        56 divided by 2 — 28 degrees."
#                   W2  "An arc of 110: the inscribed angle is 55 degrees."
#               Halving IS the lesson. Doubling the radius IS the lesson. Dividing by
#               the adjacent IS the lesson. Only two of the seven were short enough
#               for build pi's word-count sweep to catch -- the other five state a
#               correct answer at a normal length and simply never do the arithmetic
#               in front of the child. A sweep cannot see that; reading it can.
#   2026-08-28  BUILD pk -- ALGEBRA ONE, READ FOR SENSE. All 36 lessons read line by
#               line. ⭐ IT IS AS GOOD AS PRE-ALGEBRA AND POSSIBLY BETTER, and the
#               teaching pictures are the reason: an equation is a BALANCE SCALE and
#               equals means level; two undos come off in SOCKS-AND-SHOES order; a
#               function is a MACHINE with a door in and a door out; a product is a
#               rectangle of ROOMS, and "middles add, corner times" is the whole
#               danger of the unit said in four words. FOUR changes in 36 lessons.
#               ⚠️ ONE WAS A BEAT THAT SAID THE SAME THING TWICE. The range lesson
#               opened: "The mean and the median both tell you where the data SITS.
#               How far it reaches is its spread, and the range measures exactly
#               that. The range tells you something else entirely: how far it
#               stretches." The second sentence announces a contrast the first one
#               already made, so a listener is told twice that spread is not
#               position and never told it cleanly once. Cut to one.
#               The other three are build pi's rule again -- second worked examples
#               that had stopped showing their method.
#               AND THE FRAGMENT pj FLAGGED IS FIXED: pc-u4-the-half-turn-language
#               said "One more together. 2700 degrees: 15 pi." Dividing by 180 to
#               count the half turns IS that lesson's method, and the one example a
#               child works through alongside the teacher skipped it.
#   2026-08-28  BUILD pj -- PRE-ALGEBRA, READ FOR SENSE. All 35 lessons that predate
#               this session read line by line. ⭐ IT IS THE STRONGEST COURSE IN THE
#               PRODUCT and the finding is worth recording as praise, not as a thin
#               build: its traps are named out loud ("if you had gone left to right
#               you would have said 20, and 20 is wrong"), its checks are honest
#               ("if the two shares do not put back together, something went wrong"),
#               and its pictures are concrete (the rectangle round a right triangle,
#               the two rooms the times has to reach). SEVEN changes across five
#               lessons, and only three of them were sentences:
#                 - "More digits does NOT mean bigger" -- a plural subject with a
#                   singular verb, in the beat that teaches decimal comparison.
#                 - "small parts fit in many times" -- not English. The idea is that
#                   small pieces go into a whole many times over, which is exactly
#                   why dividing by a fraction GROWS the answer.
#                 - the 180-degree fact, the most useful sentence in the course,
#                   delivered with TWO dash clauses in one breath, the second
#                   dangling off "180 degrees". Split in two.
#               The other four are build pi's rule applied to the course pi did not
#               reach: three second worked examples that had stopped showing their
#               working, and "a decimal point number", which is not a thing.
#               ⚠️ AND RULE 14 CAUGHT THE FIX. Renaming "a decimal point number" to
#               "a decimal number" deleted the lesson's only utterance of its own
#               declared sign. It now reads "a number with a decimal point in it" --
#               better English AND the sign said out loud. Second time this session
#               that rule 14 has caught prose being tidied past a promise.
#   2026-08-28  BUILD pi -- THE SECOND EXAMPLE TEACHES TOO. Basic read line by line,
#               all 29 lessons that predate this session. The course is SOUND -- its
#               sentences are short and its methods are clear -- but it carries one
#               systematic defect Entry does not: the pair of worked examples is
#               lopsided. "Here is one more, done for you" shows its working; "One
#               more together" often collapsed to the bare answer. A worked example
#               that shows no work is not a worked example, it is the answer with a
#               friendly opening -- and it lands at exactly the moment the child is
#               meant to be working alongside.
#               ⚠️ THE WORST OF THE ELEVEN WAS NOT BARE, IT WAS A FRAGMENT:
#               "One more together. 31 times 3. 90 plus 3 — 93." The 90 arrives from
#               nowhere. Splitting 31 into 30 and 1 IS the method of that lesson, and
#               the one example a child works alongside skipped it.
#               TWELVE fixed (my first pass found eleven and the battery found the
#               twelfth -- what-dividing-means), in the lessons where the method is
#               the point: two-digit
#               multiplying and dividing, left-overs, greatest common factor, a
#               fraction of a group, equivalent fractions, dimes, percent, what one
#               costs, perimeter and area. Left alone on purpose: times tables (a
#               recall domain, where "eight times six equals 48" IS the working) and
#               the same-bottom fraction lessons, where the count is visible in the
#               numbers themselves.
#   2026-08-28  BUILD ph -- THE LAST EIGHT. THE CURRICULUM IS WHOLE. Basic was short
#               seven lessons and Pre-Algebra one; all eight are written, so every one
#               of the TEN courses is now nine units of four -- 360 authored lessons,
#               and no topic anywhere drops a child onto the live lane for want of a
#               script. New: times by ten and a hundred, factor pairs, simplest form,
#               taking away fractions with different bottoms, tenths and hundredths
#               together, what percent is it, percent off a price, and the biggest
#               factor below the number.
#               ⭐ TWO THINGS THE VALIDATOR FOUND THAT I WOULD NOT HAVE:
#               (1) "fus" (unlike-bottom take away) had a pool of SIX -- below the
#               seven-problem bank floor before a single ask was set aside. Letting
#               the number taken away vary is the same lesson and gives 24.
#               (2) 50 PERCENT OFF IS DEGENERATE. At half price the saving and the
#               price you pay are the SAME number, so percent-off's whole distractor
#               -- answering the saving instead of the price -- collapses into the
#               right answer. It failed on six problems and half price left the op.
#   2026-08-28  BUILD pg -- ENTRY FILLS ITS UNITS. Jim: "go and create the authored
#               lessons as well." Entry-Level Math had 20 lessons where nine units of
#               four is 36, so SIXTEEN topics dropped a five-year-old out of the
#               authored lane and onto the live one -- seconds per sentence, for the
#               children least able to wait. All sixteen are written: counting past
#               ten, which is bigger, doubles, adding three numbers, the missing part,
#               hundreds-tens-and-ones, ten more, what a digit is worth, adding
#               three-digit numbers, crossing a hundred, two- and three-digit take
#               away, checking by adding back, dimes, quarters, making change.
#               14 new ops; place value reuses "pv" and dimes reuse "m", both already
#               proved in Basic. Each lesson sits where it is TAUGHT, not at the end
#               of the course order.
#               ⭐ THE VALIDATOR WROTE HALF OF THIS BUILD. It rejected the first cut
#               18 times and every rejection was right: banks that did not ramp,
#               worked-pair asks that duplicated a bank problem (the pool for counting
#               past ten is exactly eleven-to-twenty, so the bank had to give two
#               back), "altogether" where the canon is "in all", "makes" where it is
#               "equals", and "cents" where rule 14 wanted the word "cent" said once.
#               None of those would have been caught by reading it over.
#   2026-08-27  BUILD pf -- THE FIRST COURSE, READ FOR SENSE. Jim: "Start at the
#               beginning." All 20 Entry lessons read line by line. THE HONEST RESULT
#               IS THAT ENTRY IS IN GOOD SHAPE -- it was authored earliest and most
#               carefully, its sentences are short and concrete, and only EIGHT lines
#               across six lessons needed anything. That is the finding, not a
#               disappointment: the prose rot Jim hit is in the upper courses, where
#               beats were written dense to fit a lot of idea into 80 words.
#               ⭐ ONE OF THE EIGHT WAS A FALSE STATEMENT, not a style problem:
#               entry-u8-how-much-longer said "17 take away 9 equals 8 cubes longer".
#               17 take away 9 equals 8. It does not equal "8 cubes longer". The
#               lesson's OWN first beat gets it right ("equals 9, so the pencil is 9
#               cubes longer") and the three lines after it had dropped the "so", so
#               a child was being read an equation that is not true, three times.
#               And entry-u9-sides-and-corners said "A triangle has 3 of each, and
#               that is true for every flat shape" -- which reads as "every flat shape
#               has 3 of each". It now says the counts MATCH, which is what was meant.
#               The other six: two sentences that made the ACTION the object ("
#               Mathematicians write putting together with a special sign"), a minute
#               hand that "passes" five minutes instead of stepping them, and an
#               "out loud" dangling off the end of a clock line.
#   2026-08-27  BUILD pe -- THE SENTENCES MAKE SENSE. Jim, on a live Algebra II
#               lesson: "the text itself is as if someone is teaching math in a
#               non-native language." He was right, and he also stopped me chasing
#               the wrong cause: I had found that the canon forces "take away" on all
#               336 lessons (a five-year-old's words governing Differential
#               Equations) and proposed swapping 3,220 lines to "minus". His ruling:
#               "Takeaway or minus, those were just as well. It's just when you put it
#               in the whole context of those sentences, it just didn't make sense."
#               The vocabulary was never the defect. The WRITING was.
#               WHAT SHIPPED:
#                 - alg2-u1-how-far-from-zero rewritten line by line with him, twice
#                   (he rejected my first trap beat: "saying that the negative sign
#                   only tells you which way you went is really confusing").
#                 - 171 stray spaces before punctuation closed, and 11 before "?".
#                 - 22 spoken sentences over 34 words split; 2 nominalizations fixed.
#                 - rule 14 REPAIRED: it demanded a literal f" {sym} ", so authors had
#                   been padding "terms , and" to satisfy it. Closing the spaces broke
#                   70 lessons at once, which is how the dependency surfaced. It now
#                   matches on word boundaries.
#                 - two new authoring rules (5b) that survived a canon sweep against
#                   all 1,989 cards; a third ("stacked dashes/colons", 390 hits) was
#                   CUT for false positives, the same way ox's arm was.
#   2026-08-27  BUILD ou -- ANSWER FREELY. read_answer() turns what a child TYPED
#               or SAID into the integer this engine grades: pure code, no model,
#               no network, refusing rather than guessing (a fraction, a spoken
#               decimal, or garbage is a refusal with an authored line, never a
#               rounded number that could grade a wrong answer correct). Two new
#               lines -- LINE_WHOLE and LINE_UNSURE -- join STANDALONE_LINES so
#               every spoken refusal stays inside the audio closure and is free
#               forever. The number-word table lives in numwords.py now, shared
#               with tutor.py's referees (one copy, tags.py's precedent).
#   2026-08-27  BUILD oo -- THE GIVEAWAYS ARE CLOSED (the ms hand-tail). All 41
#               remaining hits where a demo answers a problem its own lesson
#               asks: 5 problems renumbered under ms's ranking law (same answer,
#               then same difficulty -- basic-u9-perimeter kept its 16); 26 bank
#               entries removed across 18 lessons where the domain offered no
#               legal replacement (every bank stays >= 7; every removal
#               re-validated in place); alg2-u8-the-height's ask rotated
#               90 -> 180 (the one un-demoed angle in a fully-enumerated
#               domain); basic-u3's jar story renumbered 3x4 -> 2x5 WITH its
#               sentence -- a story's words and numbers move together.
#               WARNING -- one ask sentence changed (the jar story): one line to
#               re-render; it falls back to the browser voice until then.
#               Allowlist (PART 3ev pins it exactly): basic-u9-quarter-turns
#               (a four-fact recall domain -- re-asking a demonstrated fact is
#               recall, not a giveaway) and entry-u3-story-problems (a false
#               positive the audit's own doc anticipates).
#   2026-08-27  BUILD on -- THE CANON HELD TO ITS OWN STANDARD (Phase 1 of the
#               plan Jim approved: "take another look at those lesson plans in
#               conjunction with what is being written on the whiteboard").
#               Every authored card now passes the full 54-referee live-reply
#               sweep (PART 3eu pins it at zero). In this file: 132 board lines
#               of the shape "A = B -> C" split into one-claim-per-line rows
#               (rule 15; bare second rows got their honest math -- "root 25 = 5",
#               "log = 3", "three prime factors" -- never a naked number);
#               249 figures gained captions (rule 41), each written from its
#               own tag and lesson (the clock hours, "base 6, height 4", "the
#               ends, 2 and 10 -- where is the middle?"); five questions moved
#               out of equation rows into captions; geo-u1's corner picture and
#               diffeq-u1's dash point are now DRAWN where the words promised
#               them; "Look at the picture" says "board" where only rows exist.
#               WARNING -- FIVE SPOKEN LINES CHANGED (audio re-render needed):
#               geo-u1-two-make-a-corner t1/w0/w1 piece->angle (three lines),
#               pc-u4-the-half-turn-language "360 pieces" -> "360 thin slices",
#               and pre-u9-the-times-reaches-both t2 "picture" -> "board".
#               Until re-rendered those lines fall back to the browser voice.
#   2026-08-24  BUILD ms -- 71 GIVEAWAYS CLOSED, AND NOT ONE WORD OF TEACHING
#               REWRITTEN. teachaudit.py (mr) found 113 places where a teach beat or
#               a worked example works a problem the SAME lesson later asks -- the
#               tutor reads the answer aloud minutes before asking the question, and
#               "mastered" stops meaning the child can do it.
#               ⭐ THE FIX IS WHICH PROBLEM IS ASKED, NOT WHAT MR. CADABRA SAYS. The
#               teaching prose is hand-authored and read aloud by a human ear; the
#               bank is data. So 71 PROBLEMS were swapped and every teach beat and
#               worked example is untouched, to the byte. 113 direct+reverse hits ->
#               41, across 51 lessons.
#               ⚠️ EVERY REPLACEMENT KEEPS THE ORIGINAL'S ANSWER AND DIFFICULTY.
#               The first pass enumerated candidates from 1 upward and took the first
#               legal one, which quietly turned "x plus 3 equals 10" into "x plus 2
#               equals 4" -- across 87 swaps that is a course-wide difficulty
#               regression dressed up as a bug fix. Candidates are now RANKED by
#               distance from what the author chose: same difficulty key, then same
#               answer, then same magnitudes.
#               ⚠️ AND THE PROBE TESTS THE BANK IN PLACE. The first pass validated a
#               SORTED candidate bank while writing the swap into the author's
#               original slot -- six lessons briefly shipped a broken ramp. The probe
#               now validates exactly what the file will contain.
#               ⚠️ STORY PROBLEMS ARE NEVER MACHINE-SWAPPED. Their sentence is
#               authored per problem; changing the numbers under it would leave the
#               words describing something else.
#               NOT FIXED, ON PURPOSE (23 lessons, 35 hits): tiny problem domains
#               (basic-u9-quarter-turns has eight problems in total), banks built by
#               comprehension rather than written out, and story problems. Those need
#               a hand and a read-aloud, not a script. teachaudit.py names them.
#   2026-08-24  BUILD mr -- "1 PENNIES". 224 SPOKEN LINES FIXED, 12 LESSONS.
#               ⚠️ FOUND BY AN AUDIT LOOKING FOR SOMETHING ELSE. The new teach-beat
#               giveaway audit printed a bank question verbatim and it read "How many
#               cents is 3 nickels and 1 pennies?". A sweep of the whole closure then
#               found 224 spoken lines with the same defect -- "1 sixths", "1
#               hundreds", "1 stars", "1 hops", "1 ten and 1 ones" -- EVERY ONE of
#               them in Entry-Level or Basic Math, the courses for the youngest
#               children, and every one already rendered in Mr. Cadabra's real voice.
#               ⚠️ WHY NOTHING CAUGHT IT. Grammar is not arithmetic. No bound, ramp,
#               closure, vocabulary or notation rule is broken by "1 pennies", so
#               validate() passed it 436 times. The read-aloud habit catches this
#               class, and a habit is not a test -- PART 3dl is now the test.
#               ⚠️ _FRACWORD HAD BOTH FORMS ALL ALONG. Every caller simply took [1].
#               New helpers: _irr() (penny/pennies -- an "s" cannot do it) and _fw()
#               (the fraction word agreeing with its count, read from the table).
#               Ops touched: cnt, dt, fa, fs, fu, m, nick, nl, pv, vol, and the core
#               +/-/t paths in spoken_for() and praise_for().
#               ⚠️ THESE LINES ARE NEW CACHE KEYS -- about $2.70 to re-render, and
#               the 224 old clips become orphans the evictor will collect.
#   2026-08-24  BUILD mp -- ⭐⭐ THE CURRICULUM IS COMPLETE. ENTRY-LEVEL UNIT 9.
#               332 lessons -> 336, 5 new ops (sid, cor, pat, grp, eqs).
#               With this unit EVERY unit of ALL TEN COURSES has scripted lessons,
#               Entry-Level Math through Differential Equations. Entry-Level was the
#               last course not covering its own units, and nothing said so -- the
#               hole was found by a spreadsheet on 2026-08-24, not by a test. There
#               is now a test: PART 3cv reads the units from curriculum.py and fails
#               on any unit anywhere with no lessons.
#               U9 -- Shapes, Patterns & Groups. sid/cor are counting, and the two
#               together ARE the lesson: a shape has as many corners as sides, so a
#               child who notices never counts twice. pat is counting on by a fixed
#               step -- the skip counting U7 and U8 already built. grp and eqs are
#               the honest precursors to multiplying and dividing.
#               ⚠️ THE GROUP LESSONS NEVER SAY "TIMES", and a pin holds it. Basic
#               Math Unit 2 is where multiplying is taught and named; a child should
#               meet the IDEA -- equal groups counted up, a pile dealt out fairly --
#               before the word and the symbol arrive.
#               ⚠️ eqs NEVER LEAVES A REMAINDER; its check refuses one. Left-overs
#               are basic-u3-left-overs' lesson. Met here, before fair sharing is
#               solid, they teach a child that sharing sometimes just fails.
#               ⚠️ THE TRIANGLE AND SQUARE ARE RESERVED in the shapes lesson -- both
#               teach beats work the triangle, both worked examples the square, so
#               neither is ever asked in EITHER direction. workedaudit.py cannot see
#               that: sides and corners are two ops, so it compares two tuples and
#               finds nothing. Pinned by shape instead.
#   2026-08-24  BUILD mo -- ENTRY-LEVEL UNIT 8 EXISTS. 328 lessons -> 332, 4 new ops
#               (hrl, min5, min5q, dwd, cube -- five counting min5's reverse).
#               ⚠️ FOUND BY THE SPREADSHEET, NOT BY A TEST. Jim asked for problems
#               per unit; the count showed Entry-Level Units 8 and 9 with NO scripted
#               lessons at all -- in the course where the youngest children start,
#               and the only course in the curriculum not covering its own units.
#               Every other course runs four lessons in each of nine units.
#               U8 -- Time, Calendar & Measurement, and every lesson is a shape the
#               child has already met, which is the whole design: a six-year-old
#               meeting the clock should not also be meeting new arithmetic. "Later
#               on the clock" is counting on (U2/U3) along a number line. "Minutes
#               past the hour" counts by five exactly as U7 counts nickels. "Weeks
#               and days" is U7's coin shape with sevens instead of fives. "How much
#               longer" is taking away (U3) with a ruler drawn under it.
#               ⚠️ THE CLOCK DOES NOT WRAP, and hrl's check enforces it. "11 o'clock
#               plus 3 hours is 2 o'clock" is modular arithmetic; this unit never
#               teaches the twelve-hour circle it would need, so it may not ask it.
#               ⚠️ min5 NEEDED ITS REVERSE (min5q) -- a clock has only ELEVEN
#               positions, which is not enough for a bank plus pairs. ang/angq hit
#               exactly this wall in kd. It is also better teaching: one direction
#               only is a memorised list, not a clock.
#               ⚠️ AND SO THE MINUTES BANK IS TEN, NOT TWELVE. The lesson also
#               DEMONSTRATES four positions (two teach beats, two worked examples),
#               so those four are reserved -- shown, never asked. Filling the bank
#               would have meant asking a child a question Mr. Cadabra answered out
#               loud two minutes earlier. Pinned by position, in both directions,
#               because workedaudit.py compares problem TUPLES and cannot see that
#               "the hand points to 4" and "20 minutes past" are one fact.
#               NEW PUBLIC NAME: difficulty_key -- see its note above validate().
#   2026-08-24  BUILD mn -- THE HANDOFF'S OWN TWO LINES JOIN THE CLOSURE.
#               Jim tested the drill handoff with the fully rendered course and HEARD
#               THE SEAM: Mr. Cadabra flew in and his first words came out in the
#               BROWSER voice, then his real voice "came back" for the re-teach. The
#               cause was a deliberate mj decision: his hello ("Let's look at this
#               one together.") and goodbye ("You have got this. Back to you,
#               Abrabot.") were left OUT of the closure as "not authored closure
#               text". Wrong call, honestly made -- the two lines are exactly as
#               authored as the introduction, they never vary, and they cost under
#               two cents to render once. They are standalone speech (no lesson owns
#               them), so they now live here beside ABRABOT_INTRO as
#               CADABRA_HANDOFF_HELLO / CADABRA_HANDOFF_BYE, and main.py's handoff
#               READS them from here rather than defining its own copies -- ONE
#               owner, the same argument as mk. PART 3di validates them like all
#               standalone speech (both pass the canon, the cap, and the character
#               set unchanged), and pins that main.py does not fork them.
#               ⚠️ AFTER DEPLOY THEY ARE 2 UNRENDERED LINES (72 chars, ~$0.02):
#               one press of ② in /admin renders them; until then the drill lane's
#               cache-only gate quietly 204s them to the browser voice -- the exact
#               behavior Jim heard, never a charge.
#   2026-08-23  BUILD mk -- THE CLOSURE GREW A SECOND KIND OF LINE, AND ONE OWNER.
#               Phase 5 of Abrabot: Mr. Cadabra introduces him, in four authored
#               lines. They are the first speech that belongs to the COURSE rather
#               than to any lesson, so audio_lines(lesson) could never find them.
#               ⚠️ THE REAL RISK WAS NOT THE LINES, IT WAS THE SIX COPIES. main.py
#               built "the closure" in SIX places -- prewarm, dry-run, clip audit,
#               model split, eviction guard, byte estimator -- each as its own
#               comprehension over audio_lines(). A line those six disagree about is
#               a line that gets rendered but not protected (evicted, then re-billed),
#               or protected but never rendered (silence in production). So
#               course_audio_lines() is now the single answer and all six ask it.
#               ⚠️ AND THE NEW LINES ARE OUTSIDE validate()'s REACH, because
#               validate() takes a lesson. PART 3di holds them to the same speech
#               rules instead -- the VOCABULARY canon, the beat word cap, no notation.
#               The first draft of line four said a problem "gives you trouble";
#               "gives you" is a banned synonym for "equals" and the sweep caught it
#               before it was ever spoken, which is the whole argument for the pin.
#   2026-08-23  BUILD md -- ⭐⭐ THE CURRICULUM IS COMPLETE. DIFFEQ UNIT 9
#               (Nonlinear Systems & Stability). 324 lessons -> 328, 317 ops
#               (lnrz, prey, cycl, chao). THIRTEEN COURSES, NINE UNITS EACH
#               WHERE THE CURRICULUM CALLS FOR IT, AND THE ARC THAT OPENED
#               WITH COUNTING CLOSES HERE.
#               U9 -- almost nothing in the world is linear, and Unit 8's
#               neat straight-line systems look like a special case until
#               you see the rescue: zoom in far enough on any curve and it
#               becomes its own tangent, so close to an equilibrium every
#               curved law behaves like a straight one. Then the most famous
#               nonlinear system there is -- rabbits and foxes, where the
#               eating depends on BOTH numbers at once and neither is steady
#               on its own. Then what such a system does that no linear one
#               can: it circles, for ever, with the foxes always peaking a
#               quarter of a cycle behind the rabbits.
#               And then the last lesson in the course, which is deliberately
#               the strangest: two forecasts start almost the same, the gap
#               multiplies every day, and after a week it is out of sight.
#               Nothing random, nothing unknown, the equation exact -- and
#               still no forecast. A child who has come the whole way from
#               counting to here finishes by learning where prediction stops.
#               ⚠️ ONE CATCH WORTH THE WHOLE READ-ALOUD HABIT. lnrz's first
#               draft let its two numbers float free, so it cheerfully said
#               "the law 6 take away P squared has its equilibrium at P
#               equals 6" -- which is false; the equilibrium is the square
#               root of the constant. The check now requires a == b*b, so
#               the story cannot contradict its own algebra. Also caught:
#               two rule-14 symbols that only appeared in the plural or not
#               at all, one teach beat walking its own bank tuple (cycl),
#               two lessons over the closure pin, and chao saying the gap
#               "doubled its way out of sight" when in most of its bank it
#               triples or quintuples.
#   2026-08-23  BUILD mc -- DIFFEQ UNITS 7 AND 8: TURN IT INTO ALGEBRA, AND
#               FOLLOW TWO THINGS AT ONCE. 316 lessons -> 324, 313 ops
#               (lder, lalg, lshf, lfin + sysx, nucl, detm, eign).
#               U7 -- the Laplace transform, taught as what it actually is:
#               a way to solve a differential equation by turning it into
#               something that is not one. The derivative rule (a derivative
#               becomes a MULTIPLICATION, which is the whole reason it
#               works), the plain algebra left behind, the shift rule and
#               what a pole means (right of zero it grows, left of zero it
#               dies), and the final-value theorem -- where a thing settles,
#               read straight off the transform with no inverting at all.
#               U8 -- Unit 1's slope field one dimension up: two quantities
#               changing together, each watching the other. Reading the
#               system at a point, the nullclines where one arrow goes flat
#               (and their crossing, which is an equilibrium), the
#               determinant that classifies the whole picture, and the pair
#               of eigenvalues that decide it.
#               ⚠️ U8 WAS DELIBERATELY KEPT OFF b² − 4c. U5's char already
#               computes that discriminant and Algebra II's disc computes it
#               too; a third pass would have been the same subtraction in a
#               new hat. So U8 runs on the trace and the DETERMINANT
#               instead, and the classification is what those numbers mean.
#               Catches: two rule-14 misses where the symbol appeared only
#               hyphenated ("x-nullcline" is not " nullcline "); one teach
#               beat walking its own bank tuple (eign); "the total" and
#               "altogether" both written into ops and caught by the sweep;
#               and one read-aloud fix worth keeping -- lfin said "Y is 96
#               over s, times s plus 8", which spoken aloud is (96/s)(s+8),
#               the wrong expression. The board had it right and the speech
#               did not. It now names which parts are underneath.
#   2026-08-23  BUILD mb -- DIFFEQ UNITS 5 AND 6: ONE NUMBER DECIDES, AND
#               NOW SOMEBODY IS PUSHING. 308 lessons -> 316, 305 ops (char,
#               cdmp, natf, oscf + part, trns, reso, damp).
#               U5 -- second-order equations describe everything that swings,
#               and each hides a quadratic. Algebra II's discriminant comes
#               back, but now its SIGN is a physical case: above zero the
#               door closes without a wobble. Exactly zero is critical
#               damping, the knife-edge every door closer is built to sit
#               on. Strip the damping and the spring rocks at its natural
#               frequency for ever. Put a little back and -- the surprise --
#               the rocking gets SLOWER, not just smaller.
#               U6 -- a steady push settles at a steady height (guess the
#               shape, let the equation fix the size); the transient is
#               whatever the start is not explained by, which is why a
#               spring forgets how it was let go; a push at the object's own
#               frequency has nothing left to divide by and grows without
#               stopping; and damping is the only thing standing between
#               resonance and ruin.
#               ⚠️ THE b=0 TRAP, THIRD BUILD RUNNING -- AND THIS TIME IT WAS
#               CAUGHT AND MISSED IN THE SAME BUILD. natf got its speaks
#               override at authoring; cdmp, written twenty minutes later,
#               did not. Its bank then HALF passed, because a=10 and a=20
#               carry a "0" of their own. Both ops now carry the comment.
#               Also: reso's second tap was the gap itself, which sat at 3
#               beside an answer of 47 -- the small-end wasted tap for the
#               fifth build running; it became "divided by the driver
#               instead of the gap", which scales. Four teach beats walked
#               their own bank tuples (cdmp, natf, oscf, damp) -- the
#               teach-beat audit earns its place every single build now.
#               And two read-aloud catches the validator cannot see: reso
#               said the swing "has no size at all -- it just grows", which
#               contradicts itself; and cdmp first demoed a middle number of
#               4, the one value where a squared over 4 is 4 as well, so the
#               rule looked like "copy it down" -- revo's degenerate-demo
#               lesson, learned again.
#   2026-08-23  BUILD ma -- DIFFEQ UNITS 3 AND 4: KNOWING THE SHAPE WITHOUT
#               SOLVING, AND WALKING IT WHEN YOU CANNOT. 300 lessons -> 308,
#               297 ops (logi, carr, fast, away + eulr, estp, rk4, evls).
#               U3 -- qualitative analysis, which is the art of refusing to
#               solve. The logistic rate read straight off the law (and
#               dying at BOTH ends), the non-obvious place growth peaks
#               (halfway, not near the top -- a crowd gets in its own way),
#               how big that peak is, and the other kind of equilibrium:
#               one that pushes away instead of pulling in, which is why a
#               pencil will not stand on its point.
#               U4 -- Euler commits to the slope it read at the START of a
#               step and always lands low on a curve that bends up; its
#               error follows the step size exactly, which is a poor
#               bargain; fourth-order Runge-Kutta divides its error by
#               SIXTEEN where Euler manages two; and the fine print, which
#               is that accuracy is paid for in slope evaluations.
#               ⚠️ THE b=0 TRAP LANDED AGAIN. rk4 is a b=0 op and the
#               default rule-44 check demands the digit "0" in speech that
#               never says zero -- so a=80 and a=160 PASSED by accident
#               while a=32 failed, which is the nastiest shape this bug
#               takes. Every handoff since lw has named it and it still
#               got through. It is now commented at the op itself.
#               Three more caught at authoring, all read-aloud only: the
#               wasted tap at the SMALL end (lz's discovery) hit three ops
#               at once -- away, estp and evls each had a constant of 2 to 12
#               sitting beside answers over 140; a ceiling of 24 fish with a
#               growth constant of 12 gave a peak rate of 72 fish a year in
#               a pond that holds 24, so the constant is now capped at a
#               quarter of the ceiling; and carr had "its fastest -growing
#               size" -- a space inserted purely to satisfy rule 14, which
#               the symbol's other appearance already covered.
#   2026-08-23  BUILD lz -- ⭐ DIFFERENTIAL EQUATIONS OPENS, THE THIRTEENTH
#               AND LAST COURSE. UNITS 1 AND 2: THE EQUATION AS A PICTURE,
#               AND THE FIRST TWO METHODS THAT SOLVE ONE. 292 lessons ->
#               300, 289 ops (slpf, slpq, isoc, fldc + sepv, sepr, newt,
#               conc). New helper _isqrt -- a whole square root, or 0 when
#               the number is not a perfect square; sepr needs it and a
#               lambda cannot say "and only if it comes out whole".
#               U1 -- classification named in passing (first order, second)
#               and then the idea that makes the subject visible: the
#               equation hands you a SLOPE at every point, so draw a dash
#               there. Change the law and every dash swings. Read the field
#               backwards and the equal dashes line up on an isocline. Then
#               walk it: joining the dashes is not a picture of a solution,
#               it IS one.
#               U2 -- separate the two letters and integrate each side; do
#               it again where the y sits underneath and the answer arrives
#               as a square root, which breaks the straight-line guess for
#               good; then the two first-order LINEAR equations the world
#               is full of -- a cooling cup and a tank of brine.
#               ⚠️ FOUR CATCHES, AND THREE OF THEM ARE THE SAME LESSON. The
#               enormous-distractor check (lx, ly) fired twice more: slpf's
#               first draft timesed the coordinates and reached 2,750
#               against an answer of 105. And the DUAL of it, which is new:
#               slpf's bank had a and b nearly equal all the way up, so the
#               "taken away" tap SHRANK to 5 beside an answer of 105 --
#               equally dismissible. A tap is wasted at either extreme, so
#               the bank now scales its gap with the answer. Third, slpq's
#               "squaring skipped" tap was a take away b, which goes
#               NEGATIVE wherever y sits above x; the choices floor caught
#               it. Fourth, and this one only a read-aloud finds: newt's
#               bank opened with "coffee at 20 degrees in a room at 10",
#               which is not coffee, it is a cold cup. Coffee now starts at
#               40. Its cooling constant was also INVERTED at authoring --
#               1 degree a minute per c degrees of gap, not c degrees per
#               degree -- because the first wording had a 30-degree gap
#               cooling at 60 degrees a minute.
#   2026-08-23  BUILD ly -- ⭐ CALCULUS COMPLETE. UNITS 8 AND 9: WHAT AREA
#               CAN MEASURE, AND AN EQUATION ABOUT A RATE. 284 lessons ->
#               292, 281 ops (btwn, trap, accu, revo + dfeq, mixr, pgrw,
#               eqbm). THE TWELFTH COURSE IS DONE; only Differential
#               Equations remains.
#               U8 -- once area is a measurement it measures anything: the
#               strip caught between two curves (top take away bottom), the
#               trapezium under a speed that climbs (average the two ends,
#               then hold it for the time), an integral that ADDS ON to what
#               was already in the tank -- an integral measures the CHANGE,
#               never the amount -- and a flat rectangle spun into a
#               cylinder, where squaring the radius is what turns an area
#               into a solid.
#               U9 -- the closing unit, and the one that reframes the whole
#               course: an equation can describe a RATE instead of an
#               amount, and integration is what turns it back. A constant
#               rate (the draining tank), two rates pulling against each
#               other (find the NET rate first, then let the clock work on
#               it), a rate that depends on the amount itself -- the
#               equation behind every exponential -- and equilibrium, the
#               amount at which all change stops.
#               ⚠️ TWO CATCHES, BOTH ABOUT WHAT THE CHILD ACTUALLY SEES.
#               (1) The max_value rule only INSPECTS a and b, but its label
#               promises "every number a child sees". The wrong taps are
#               numbers a child sees too, and four of these eight lessons
#               had a tap outside the stated bound. Bounds are now set from
#               max(a, b, answer, every tap). (2) eqbm's "timesed" tap
#               reached 1,323 against an answer of 27 -- the same defect lx
#               found in antp. A distractor nobody would ever touch is a
#               wasted tap, so it became the constant answered as though it
#               were the population, which is a mistake children make.
#               Two builds running, the enormous-distractor check has earned
#               its place in the pipeline.
#   2026-08-23  BUILD lx -- CALCULUS UNITS 6 AND 7: THE RULE RUN BACKWARDS,
#               AND THE AREA THAT MEANS SOMETHING. 276 lessons -> 284, 273
#               ops (anti, antp, plusc, init + defi, triz, ftc, avgv).
#               U6 -- every unit up to here asked for a derivative; this one
#               asks the question backwards. The power rule reversed (halve,
#               do not double), the same reversal at any power (raise the
#               exponent, then DIVIDE by it), the discovery that going
#               backwards never lands on one function but on a whole FAMILY
#               a constant apart, and the one known point that picks a single
#               member out of that family.
#               U7 -- the area under a graph is a real measurement: a
#               rectangle of steady speed IS a distance, a triangle of steady
#               acceleration is the same idea halved, the Fundamental Theorem
#               ties that area back to the antiderivatives of U6 (end take
#               away start), and the average value flattens the area out
#               again into a single height.
#               ⚠️ THREE AUTHORING CATCHES WORTH KEEPING. (1) max_value
#               bounds every number a child SEES, not just the answer -- anti,
#               antp and avgv all validated their answers happily and failed
#               on their givens (a=48, b=72, a=154). Set the bound from
#               max(a, b, answer), not from the answer alone. (2) A TEACH
#               beat that walks a worked example must not walk a BANK tuple:
#               anti demoed 6x, antp demoed 12x cubed and triz demoed 6
#               seconds, and all three numbers sat in their own banks. The
#               worked-example audit only reads pairs[]; teach beats need the
#               same check by hand. (3) antp's "timesed instead of divided"
#               tap reached 396 against an answer of 11 -- a distractor no
#               child would ever touch is a wasted tap, so it became the
#               front number handed back UNDIVIDED, which is the error they
#               actually make.
#   2026-08-23  BUILD lw -- CALCULUS UNITS 4 AND 5: THE DERIVATIVE AS A TOOL,
#               AND FINDING THE BEST. 268 lessons -> 276, 265 ops (vsol,
#               mrat, crit, acce + optr, maxa, sumx, infl).
#               U4 -- a derivative is an equation and can be SOLVED (from a
#               speed back to the moment it happens), one rate drives another
#               (a square's area speeds up while its side grows steadily --
#               the chain rule doing real work), a curve can only turn where
#               its slope is zero, and differentiating TWICE reaches
#               acceleration, which for a falling stone is the constant
#               called gravity.
#               U5 -- the best answer sits where the slope is zero: the oldest
#               optimisation there is (a fixed fence wants a SQUARE), the
#               area that wins, the same truth stripped to plain numbers
#               (equal halves beat every other split), and the SECOND
#               derivative finding where the bend changes rather than where
#               the slope does -- with the halving habit named as the tap.
#               Four surfaces were too small to fill a bank and had their
#               ranges widened at authoring (maxa 11 tuples, sumx 8, infl 10,
#               vsol 11) -- the enumerate-first habit catches this before a
#               single lesson is written. ⚠️ AND THE OLD RULE-44 TRAP BIT
#               THREE TIMES AT ONCE: crit, optr and infl are all b=0 ops, so
#               the default speaks check demanded the digit "0" in speech
#               that never says zero. Every b=0 op needs its own speaks
#               override; it is the single most repeated defect in the build
#               history.
#   2026-08-23  BUILD lv -- CALCULUS UNITS 2 AND 3: THE SLOPE AT A POINT, AND
#               THE RULES FOR BUILT-UP FUNCTIONS. 260 lessons -> 268, 257 ops
#               (derv, pwrc, cnst, evat + prod, chan, chev, quot).
#               U2 -- pc-u9's avgr shrank the window and named the limit;
#               here it becomes a NUMBER (on x squared the slope at a point
#               is twice that point, and the height is the tap), then the
#               POWER RULE that skips the shrinking entirely (exponent times
#               the front number -- adding is not a rule anything obeys),
#               then a line's one constant slope (the lifting number is the
#               tap), then the derivative as a MACHINE you feed x's to (the
#               height and the un-fed front number are both taps).
#               U3 -- the product rule checked against expanding first, so
#               the child can SEE it agree; the chain rule, whose whole point
#               is that the inside's derivative comes out too (forgetting it
#               is named in the lesson as the commonest mistake in Calculus);
#               the chain rule then evaluated at a point; and the reassurance
#               that a plain NUMBER underneath needs no quotient rule at all.
#               Three lessons came in over the 20,000-char closure pin and
#               were trimmed at authoring -- derv's spoken had grown a whole
#               paragraph of setup. Checking cost before the battery is now
#               reflex, and it is catching one or two lessons every build.
#   2026-08-23  BUILD lu -- ⭐ PROBABILITY & STATISTICS COMPLETE (U9 Sampling
#               & Inference) and ⭐ CALCULUS OPENS (U1 Limits & Continuity).
#               252 lessons -> 260, 249 ops (cint, cwid, inci, npop + llaw,
#               linf, jump, cfix). Prob & Stats finishes as the ELEVENTH
#               course: nine units, 36 lessons, the sixth 36-lesson course in
#               a row. Calculus is the twelfth.
#               ⭐ JIM RAISED TTS_CACHE_MAX_MB TO 4000 (2026-08-23), which
#               covers the finished course (~3,800 MB projected) with room.
#               U9 -- A SAMPLE ANSWERS WITH A RANGE, NEVER A POINT. Unit 4
#               built the sample; this reports it honestly: the low end (the
#               high end is the tap), the width of the whole range (the
#               margin counts twice -- elax's un-square-and-double, in
#               statistics clothes), whether somebody's claim can survive
#               inside it (measure from the EDGE, not the middle -- measuring
#               from the estimate pretends it is exact), and the range
#               carried back onto real people (take the low end FIRST, then
#               count).
#               CALCULUS U1 -- Pre-Calc met the limit; Calculus puts it to
#               work. Limits pass straight through arithmetic (the permission
#               every later rule rests on), they survive out at infinity
#               where matched powers cancel and only the ratio of the leading
#               numbers is left, a break has a measurable SIZE, and a curve
#               can be MENDED -- walk the slope up to the border and match
#               it, which is continuity as a repair job.
#               Two catches of the collides-with-a-constant class (lq's
#               lesson), both now forbidden by check() rather than by care:
#               jump's added-heights tap could equal the border 6 that its
#               own sentence names, and cfix's flat value could equal the
#               border, putting one number in two roles in one sentence.
#               The auto-picker needed better KEYS this time, not just a
#               variety rule: five ops ramped on a parameter that let the
#               ANSWER repeat (cint gave the same answer five times running),
#               so cint, inci, npop and jump now key on what the lesson
#               actually measures.
#   2026-08-23  BUILD lt -- PROB & STATS UNITS 7 AND 8: WHAT ONE PLAY IS
#               WORTH, AND THE CURVE THAT FITS THE WORLD. 244 lessons -> 252,
#               241 ops (pdis, evwa, fair, hedg + n68, zsco, zval, ntal).
#               ⭐ [[normal]] WALKED -- THE LAST UNUSED RENDERER IN THE APP.
#               It labels the axis at every standard deviation from minus
#               three to plus three, which prints zval's answer outright and
#               lets a child count ticks for zsco, so it is TEACH-ONLY
#               throughout the unit. Every figure renderer the app owns has
#               now carried at least one lesson; only conic type="hyperbola"
#               (a variant, not a renderer) is still unused.
#               UNIT 7 -- alg2-u9's expv counted the payout of a RUN of
#               plays; this unit builds the idea properly. A distribution's
#               chances must fill the hundred (something happens every time).
#               Expected value is the payoffs WEIGHTED by how often they come
#               -- and the plain average of the two prizes, the classic slip,
#               is only right when both come up equally often. Fairness is
#               that idea run backwards: spread the whole stake over just the
#               wins, which is why a rare prize must be a big one. And the
#               gap between what you pay and what comes back is the house
#               edge -- invisible in one play, perfectly reliable over
#               hundreds.
#               UNIT 8 -- one curve fits so much of the world, and it comes
#               with a ruler: how many sit in the crowded middle (68 percent,
#               turned into actual children), how far out a value really is
#               once measured in standard deviations rather than raw units
#               (the raw gap is the tap), which value sits two deviations out
#               (starting FROM the mean is the tap), and how few people live
#               in the tails -- the 5 percent split evenly between two ends,
#               so counting both is the tap.
#               Validator caught six wordings ("makes" x3, "remain",
#               "remaining", "altogether"). Closure cost was checked BEFORE
#               the battery (lr's lesson, now standing practice): three U7
#               lessons came in at or over the 20,000-char pin and their
#               praise was trimmed at authoring. The auto-picked banks needed
#               a VARIETY rule this time -- keying on one parameter made four
#               banks march monotonously (hedg gave the same answer ten times
#               running), so the picker now rotates the shape it has not used
#               recently.
#   2026-08-23  BUILD ls -- PROB & STATS UNITS 5 AND 6: PUTTING A NUMBER ON A
#               CHANCE, AND THE WORD THAT SHRINKS THE WORLD. 236 lessons ->
#               244, 233 ops (ppct, por, pand, ptre + cbse, ccnt, indp, wout).
#               ⭐ [[tree]] WALKED -- it prints every leaf's product, so it
#               lives in teach beats only; ptre's ask boards carry the givens
#               in words. Only [[normal]] and conic type="hyperbola" remain
#               unused anywhere in the course.
#               UNIT 5 -- geo-u9 COUNTED chances ("a out of b"); this unit
#               MEASURES them on the 0-to-100 scale, then meets the two ways
#               chances join, taught as a deliberate PAIR where each is the
#               other's trap: OR adds (timesing counts pairs of marbles, not
#               marbles) and AND times (adding makes a chance commoner, which
#               cannot be right when you demand both). It closes by counting
#               winning PATHS through two stages -- the AND rule drawn.
#               UNIT 6 -- the word GIVEN throws away everyone it does not
#               mention: first WHAT YOU DIVIDE BY (the whole class is the tap
#               that ignores the conditioning), then the rate inside the
#               shrunken world, then what INDEPENDENT actually claims -- that
#               the group's rate IS the overall rate, so the MEASURED rate is
#               the wrong answer to "what would independence predict" -- and
#               last the draw that changes the bag behind it.
#               Read-aloud caught two beyond the usual: (1) por's praise said
#               timesing "would give more winners than there are marbles",
#               which is FALSE at the smallest problem (2 red, 3 blue, 2
#               green: 6 is not more than 7) -- a praise that argues from
#               size must hold at every tuple in the bank, so it now names
#               what the product actually counts, PAIRS; (2) indp's stories
#               claimed a percent of a group of students without checking the
#               percent landed on whole children -- 55 percent of 35
#               left-handers is 19.25 of them. check() now enforces
#               (b * c) % 100 == 0: no fraction of a child.
#               Closure cost checked BEFORE the battery this time (lr's
#               lesson): indp and pand both came in over the 20,000-char pin
#               and were trimmed at authoring, not after a failed run.
#   2026-08-23  BUILD lr -- PROB & STATS UNITS 3 AND 4: TWO NUMBERS AT ONCE,
#               AND THE ASKING. 228 lessons -> 236, 225 ops (spnt, sslp, resd,
#               sblw + strf, resp, bias, merr). New helpers _scat_points /
#               _scat_at / _scat_next build the six-dot cloud.
#               ⭐ [[scatter]] WALKED -- the last of the plot renderers except
#               tree and normal. It prints the fit equation when fit="true",
#               so it appears with the fit ONLY in teach beats; ask boards
#               either show the bare cloud (reading a dot IS the skill) or no
#               figure at all.
#               UNIT 3 -- TWO MEASUREMENTS AT ONCE: reading one dot without
#               mixing the axes (answering the x is the classic), the fit
#               line's slope USED as a rate over several steps (alg1's slp
#               measured the climb; here the climb means points per hour), the
#               RESIDUAL as the gap between predicted and actual, and the fact
#               that the line runs THROUGH the cloud so both sides hold dots.
#               UNIT 4 -- THE ANSWER IS ONLY AS GOOD AS THE ASKING. alg2-u9's
#               samp scaled a sample up to a school; this unit asks whether it
#               deserved to be scaled: a stratified sample that keeps the
#               group's own mix (half-and-half is the lazy tap), the response
#               rate as a warning light, the people a survey could never reach
#               (undercoverage, the heart of bias), and the price of accuracy
#               -- FOUR times the people to halve the margin, where doubling
#               is the honest-looking wrong answer.
#               Design-time greps again earned their keep: a planned "scale
#               the sample up" op WAS alg2-u9's samp outright, and alg1 owns
#               lny/slp/yint, so the slope lesson had to become a rate
#               application rather than a second reading of a climb.
#               ⭐ READ-ALOUD FOUND A SHARPER FORM OF lp's RULE: three worked
#               examples solved a problem sitting in their own lesson's BANK
#               (not merely the ask beside them) -- spnt twice and merr once.
#               The rule is now: a worked example must not answer ANY problem
#               in its lesson. A scripted sweep for this (numbers opening with
#               a problem's tuple, then its answer) finds 45 older lessons
#               with the same shape -- logged for a dedicated cleanup build,
#               NOT touched here.
#   2026-08-23  BUILD lq -- ⭐ PROBABILITY & STATISTICS OPENS, THE TENTH COURSE
#               (U1 Exploring Data; U2 Describing Distributions). 220 lessons
#               -> 228, 217 ops (dotm, dcnt, htot, farv + medv, iqrw, madv,
#               pctl). New list helpers _dotmode/_dotcut/_histvals/_farlist/
#               _evenlist/_madlist build the plotted data from p.
#               ⭐ THE STATISTICS RENDERER SHELF COMES OFF THE WALL: [[histogram]]
#               and [[boxplot]] used for the first time since they were
#               written. Both PRINT their numbers (histogram labels every
#               bar's count; boxplot prints all five) -- so the lessons are
#               built so that READING is the given and the arithmetic is the
#               skill: add the printed bars, subtract the printed box edges
#               (alg1-u9 rnge's precedent, where the board showed smallest
#               and biggest and asked for the range). Still unused: tree,
#               scatter, normal -- they belong to later units of this course.
#               UNIT 1 -- BEFORE YOU COMPUTE, LOOK. Algebra One computed mean,
#               median and range from lists; this unit reads a PICTURE: the
#               mode as the value under the tallest stack (the count of dots
#               standing on it is the classic wrong tap), a slice of the plot
#               counted with one dot standing exactly ON the line ("more than
#               8" excludes 8 -- the off-by-one tap), a histogram's bars added
#               up, and SPOTTING an outlier (alg1's outl showed what one DOES
#               to a mean; this teaches how to see it first).
#               UNIT 2 -- NOW PUT NUMBERS ON THE SHAPE: the median when there
#               is no single middle (alg1's medn is odd-only by check), the
#               box plot's box as the middle half (whisker-to-whisker is the
#               tap), the average distance from the mean -- standard deviation
#               in child clothes, four numbers placed b and 3b either side so
#               the answer is exactly 2b -- and the percentile, read as a
#               percent of the group rather than a headcount.
#               Op-name collisions caught by grep before authoring: "outl" is
#               alg1's outlier op (-> farv) and a planned "new mean after an
#               outlier joins" lesson WOULD HAVE REPEATED alg1-u9 outright
#               (-> replaced with percentiles). Compile check caught the
#               f-string quoting slip again (dcnt's board, ll's lesson).
#               Read-aloud caught FIVE: a worked example landing on the SAME
#               answer AND the same arithmetic as the ask beside it (lp's new
#               checklist line, earning its place on its first outing); three
#               worked examples describing a picture their board did not show;
#               an all-equal-bars histogram making "the tallest bar" a
#               meaningless phrase; "1 either side of the pair"; and -- the
#               real one -- "a class of 20" counting the CHILD among the 20,
#               so 2 beaten plus 18 above came to 20 people in a class that
#               also contained the reader. Now "20 other students".
#   2026-08-22  BUILD lp -- ⭐ PRE-CALC COMPLETE (U8 Sequences, Series & the
#               Binomial Theorem; U9 Introduction to Limits). 212 lessons ->
#               220, 209 ops (gsum, sigm, pasc, gser + lsub, lhol, lsid,
#               avgr). Pre-Calc finishes as the NINTH course: nine units, 36
#               lessons, the fifth 36-lesson course in a row.
#               New module helpers _fact / _npr / _ncr (a lambda cannot
#               express the loops readably -- _prime_factors' precedent).
#               UNIT 8 -- ADD THE WHOLE PATTERN UP, not just its last term:
#               the finite geometric sum (the last-term tap is the classic,
#               the never-grew tap is the arithmetic habit), sigma read as an
#               INSTRUCTION (gaus's bare sum now carrying a multiplier --
#               dropping it is one slip, answering the last term the other),
#               choosing when ORDER DOES NOT MATTER (cnt3 grown up: count the
#               line-ups, then divide the orders away), and -- the hinge --
#               an INFINITE halving sum that still settles, on twice the
#               first piece.
#               UNIT 9, LIMITS -- one question: where was it HEADED? The
#               friendly limit (walk the value in), THE HOLE (undefined at
#               the point, plain everywhere around it -- the case limits were
#               invented for), two sides that disagree (fpie's piecewise, met
#               again -- and the limit is never the middle), and the average
#               rate of change over a shrinking window, which is the
#               derivative, handed forward to Calculus by name.
#               Read-aloud caught THREE, one of them the worst kind yet:
#               lsid's two WORKED EXAMPLES WERE THEIR OWN ASKS, number for
#               number -- the answer served aloud immediately before the
#               question. The validator cannot see it (workeds are prose, not
#               tuples). NEW CHECKLIST LINE: compare every worked example's
#               numbers against its own ask. Also caught: sigm's workeds were
#               its asks with a and b transposed (a near miss of the same
#               defect), and a y-value of 6 in lsid colliding with the
#               border's own 6 ("y is 6 when x is below 6") -- now excluded
#               by check.
#   2026-08-22  BUILD lo -- PRE-CALC UNITS 6 AND 7: THE WORK CLOTHES AND THE
#               EQUATION. 204 lessons -> 212, 201 ops (arsn, ramp, brng, vmag
#               + crad, cctr, elax, parm).
#               UNIT 6, APPLICATIONS OF TRIGONOMETRY -- trigonometry puts on
#               work clothes: area from two sides and the angle between them
#               (sin 90 = 1 halves the product, sin 30 = sin 150 quarters it
#               -- and the 150 case PAYS OFF ln's reference angle), a ramp's
#               climb as half its length, a ship's bearing wrapped past 360
#               (ln's coterminal rule, at sea), and an arrow's length from its
#               two steps -- Geometry's Pythagoras in vector clothes, bounded
#               above by the corner walk and below by the biggest step.
#               UNIT 7, CONIC SECTIONS & PARAMETRIC EQUATIONS -- a shape's
#               EQUATION hands over its measurements: un-square the circle's
#               right-hand number for the radius, read the center out of the
#               take-aways (the sign points opposite -- vtx2's and fdom's rule
#               in its third home), un-square AND DOUBLE for an ellipse's
#               width, and tie both coordinates to time so the curve becomes a
#               path (the speed-mistaken-for-distance tap is the new one).
#               ⭐ TWO SHELVED RENDERERS WALKED: [[vector]] (vmag's teach) and
#               [[conic]] (crad's and elax's teach). BOTH ARE TEACH-ONLY BY
#               RULE: [[vector]] prints |v| -- vmag's exact answer -- and
#               [[conic]] draws on a labeled grid a child could measure an
#               ellipse's width off. Only [[hyperbola]]-style conic types and
#               the statistics shelf now remain unused.
#               Read-aloud pass caught SIX: "half of half of" (unspeakable),
#               "the turn made backwards" (names the wrong noun), a trailing
#               possessive ("not 2 seconds'"), two guided asks sharing 144,
#               a worked example reading "take away 9 ... equals 9", and --
#               the real one -- arsn's ask FIGURE drawing a 150-degree angle
#               that looks sharp while the praise calls that triangle wide
#               (the le/topp class: speech arguing with the picture). The ask
#               board is now words; the teach keeps the figure at 90 degrees,
#               where the drawing tells the truth.
#   2026-08-22  BUILD ln -- PRE-CALC UNITS 4 AND 5: THE LANGUAGE AND THE MIRROR.
#               196 lessons -> 204, 193 ops (rad1, nspn, refq, wper + pyid,
#               cofn, negf, sols). NOTE: the period op is "wper", not "peri" --
#               "peri" was already the Basic Math perimeter op (checked before
#               authoring; always grep planned op names first).
#               UNIT 4, TRIGONOMETRIC FUNCTIONS -- the circle gets a NEW
#               LANGUAGE and a map, deepening alg2-u8's compass points:
#               radians counted in half turns (180 = 1 pi; the quarter-turn
#               double and the degrees-copied taps), negative angles named
#               forwards by adding a full turn (spin's backwards mirror; the
#               dropped-minus and half-turn taps), reference angles in the
#               second quarter (hug the FLAT line -- the measured-from-the-top
#               tap; 135 excluded where the taps would collide), and the
#               period of sin(ax) (divide 360 -- the times-360 flip and the
#               plain-360 habit).
#               UNIT 5, ANALYTIC TRIGONOMETRY -- what is ALWAYS true:
#               sin^2 + cos^2 splits one whole into hundredths (50 excluded --
#               the copy tap would collide), cofunction partners across 90
#               (45 excluded -- its own partner), even/odd on the circle (the
#               mirror flips height, never across -- lm's minus parade paid
#               forward; all answers spoken as words, never printed minus),
#               and counting solutions per sweep (skip the start, keep the
#               finish; the one-per-quarter tap says 4).
#               Read-aloud pass found NOTHING to fix -- second build running
#               (raw-givens + the design-time canon sweep now catch the
#               defect classes at authoring time).
#   2026-08-22  BUILD lm -- PRE-CALC UNITS 2 AND 3: THE SHORTCUT AND THE LAYERS.
#               188 lessons -> 196, 185 ops (negp, remt, vprd, vasy + logp,
#               lsol, hcnt, cmpd).
#               UNIT 2, POLYNOMIAL & RATIONAL FUNCTIONS -- a polynomial tells
#               you everything WITHOUT long division: (-1)^n read by parity
#               (the minus parade, cancelled two at a time), the Remainder
#               Theorem as the plug-in shortcut (the theorem's NAME lives on
#               the board only -- "remainder" contains the banned "remain",
#               so the speech says "left over" throughout, canon-clean by
#               construction), Vieta's product paying off lh's planted
#               promise ("the product -- famous later"; the sum tap is the
#               mirror), and forbidden x's COUNTED from a factored bottom
#               (repeated factors share one zero -- count zeros, not
#               factors).
#               UNIT 3, EXPONENTIAL & LOGARITHMIC FUNCTIONS -- logs and
#               exponentials un-do each other: the power rule (the exponent
#               comes down front; powering the log is the trap), solving
#               log ? = b by stacking the base (the a-times-b single-times
#               trap), halvings counted BACKWARDS (hcnt is lj's hlfl read
#               the other way -- the ratio-not-count trap), and money that
#               doubles (count the doublings from the years FIRST; steady
#               adding stalls where doubling pulls away).
#               All eight ask boards raw-givens at authoring time. Read-aloud
#               pass caught one edge-grammar defect: negp's "the pairs
#               cancel" with power 2 or 3 has exactly ONE pair -- now
#               "cancel two at a time", parity-safe at every power.
#   2026-08-22  BUILD ll -- ⭐ ALGEBRA II COMPLETE (U9 Statistics & Probability)
#               and ⭐ PRE-CALC OPENS (U1 Functions & Their Graphs). 188 lessons,
#               177 ops (wavg, cnt3, expv, samp + fcmp, fshf, fdom, fpie).
#               Algebra II finishes as the EIGHTH course: nine units, 36 lessons,
#               the fourth 36-lesson course in a row.
#               U9 goes past alg1-u9 and geo-u9: the WEIGHTED mean (the
#               unweighted-average-of-two-numbers slip is the classic), the
#               counting principle grown a third slot, expected value in child
#               clothes ("count the paying plays, then times"), and sampling --
#               "ask a few, learn about everyone", with the sample-copied and
#               half-guess taps, and the word ABOUT taught as part of the answer.
#               PRE-CALC U1 grows alg1-u3's machines up: composition in f(g(x))
#               notation (INSIDE FIRST -- the order flip is the trap), the
#               graph-slides rule (f(x − a) slides RIGHT -- vtx2's opposite-sign
#               lesson generalized to every function), the domain as a doorway
#               (with the taught CONTRAST: the root's edge is welcome, division's
#               forbidden x was not), and piecewise functions (find where x
#               lives, run THAT rule only -- the wrong-branch value is the tap).
#               All eight ask boards are raw-givens by design -- the lj rule
#               applied at authoring time, and for once the read-aloud pass found
#               nothing to fix.
#   2026-08-22  BUILD lk -- ALGEBRA II UNITS 7 AND 8: THE RIDE AND THE CIRCLE.
#               172 lessons -> 180, 169 ops (anth, gnth, gaus, reca + sinp, cosp,
#               spin, ampl).
#               UNIT 7, SEQUENCES & SERIES -- a pattern is a rule you can RIDE:
#               the arithmetic closed form (the OFF-BY-ONE is the trap -- term c
#               stands c-1 steps from the start, "the fencepost in a new coat"),
#               the geometric one (the adding habit again), Gauss's pairing trick
#               -- where the teach tells the schoolboy story but WITHHOLDS 5050,
#               so ask2 (n=100) lets the child BE Gauss -- and walking a
#               recursive rule as the contrast that shows what closed forms buy.
#               UNIT 8, TRIGONOMETRIC FUNCTIONS -- the circle of size one: sine
#               is the HEIGHT of the arrow's tip, cosine the ACROSS, read at the
#               compass points where both are exactly 1, 0 or negative 1 (the
#               whole-number surface; the four base angles ARE the world, so the
#               teach shows them -- the turnc precedent -- and the spun angles
#               past 360 are the fresh practice, which quietly drills coterminal
#               stripping twelve times per lesson). Then the spin that changes
#               nothing, and amplitude on a real [[graph]] sine wave (compile
#               supports sin() -- checked first).
#               ⭐ [[unitcircle]] draws its first scripted lessons -- teach and
#               worked boards ONLY: it prints cos and sin at the bottom, the
#               answers (the righttriangle/inscribed rule, fourth instance). With
#               it, EVERY non-statistics renderer on July's shelf has now been
#               walked by a scripted lesson.
#               Caught out loud: sinp/cosp praise opened lowercase after the
#               praise prefix in the no-spin branch ("That's it! the arrow...")
#               -- conditional praise templates must re-check capitalization in
#               EVERY branch. Validator caught one "makes" (reca teach).
#   2026-08-22  BUILD lj -- ALGEBRA II UNITS 5 AND 6: THE ROOT AND THE HIDDEN
#               EXPONENT. 164 lessons -> 172, 161 ops (rmul, rpow, rsq, rbet +
#               hlfl, logb, logm, lbet).
#               UNIT 5, RADICALS & RATIONAL EXPONENTS -- the root is a power in
#               disguise, and NEVER A HALVING: that one misconception is the
#               standing wrong tap in three of the four lessons (half of a in
#               rpow, double-as-the-undo in rsq, a-half in rbet). Roots times
#               under one roof (wrong taps: stopped-at-the-square and the famous
#               illegal add-under-roots), the one-half power unmasked, the
#               radical equation undone, estimation between the squares.
#               UNIT 6, EXPONENTIAL & LOGARITHMIC FUNCTIONS -- decay mirrors the
#               doubling pond (the LINEAR FALLER is the wrong tap, exactly as the
#               linear thinker was in kz), then the logarithm met as a question
#               ("the base raised to WHAT equals this?"), its product rule as the
#               third rung of the powers-add family (exadd -> pdeg -> logm), and
#               estimation between the powers -- rbet's twin, on purpose.
#               THE RAW-GIVENS RULE BIT TWICE MORE in the read-aloud pass: rpow's
#               board translated the fraction power into a root, and rmul's board
#               did the under-one-roof combine -- both exactly the decisions
#               their distractors test. Both boards now show raw givens only.
#               The rule is now three-time-confirmed (para, rasy, rpow/rmul):
#               WHEN THE SKILL IS CHOOSING OR TRANSFORMING THE GIVENS, THE BOARD
#               SHOWS ONLY THE GIVENS. Validator caught "makes" (rmul teach) and
#               a rule-14 miss ("logarithm" spoken only in plural/short forms in
#               lbet's teach).
#   2026-08-22  BUILD li -- ALGEBRA II UNITS 3 AND 4: THE DEGREE AND THE DIVIDE.
#               156 lessons -> 164, 153 ops (pdeg, turnc, rsum3, pval + rdiv,
#               rsol, excl, rasy).
#               UNIT 3, POLYNOMIAL FUNCTIONS -- what the DEGREE promises: it adds
#               under times (kz's power rule grown up; wrong taps are the
#               multiplied degrees and addition's keep-the-bigger rule), it caps
#               the wiggles at one fewer (the parabola habit "curves turn once"
#               is the other tap), a cubic's three crossings answer together
#               (rsum's ladder + the forgot-the-third trap), and evaluating a
#               cubic brings back the oldest exponent misconception -- x³ read as
#               3-times-x -- one storey taller, alongside the dropped minus.
#               UNIT 4, RATIONAL EXPRESSIONS & FUNCTIONS -- division becomes a
#               function: y = a/x met and read backwards (the deliberate pair;
#               the wrong taps are the other operations wearing masks), the one
#               FORBIDDEN x (where the BOTTOM dies -- vtx2's sign flip and the
#               x=0 habit as taps; NO graph on those asks, the asymptote would
#               sit at the answer), and the far horizon: (ax+b)/x hides a
#               survivor, where ZERO -- the plain-a/x answer -- is the deliberate
#               trap, and the board shows the UNSPLIT form (splitting is the
#               skill; the first draft split it on the board -- the para/lg
#               rule caught again in the read-aloud pass).
#               The validator caught one word: "altogether" in rsol's teach
#               (canon "in all") -- swapped for "entirely".
#   2026-08-22  BUILD lh -- ⭐ ALGEBRA II OPENS, the seventh course. Units 1 and 2.
#               148 lessons -> 156, 145 ops (absv, absc, el2, sys3 + vtx2, rsum,
#               disc, imag).
#               UNIT 1, FOUNDATIONS & SYSTEMS -- sharpened tools: absolute value
#               as DISTANCE read both directions (the value, then counting inside
#               it -- where zero always sneaks in unseen), then systems grown past
#               alg1-u5: elimination where the vanishing leaves a PAIR that still
#               needs sharing ("vanish, then share"), and three friends weighed
#               two at a time (add the clues, halve -- everyone was there twice).
#               UNIT 2, QUADRATIC FUNCTIONS & COMPLEX NUMBERS -- the quadratic
#               tells its secrets without being solved: vertex form says WHERE it
#               turns (deliberately paired with alg1-vtx's how-LOW question; the
#               sign trap −a and the wrong-question trap b are the taps), the two
#               roots answer together (the product waits as Vieta's other
#               number), the discriminant counts crossings by its SIGN alone
#               (answers 0/1/2 -- the course's first judgment ask, min_value 0),
#               and the unit ends with a door opening: i arrives, x² = −a, where
#               the wrong taps are the forgotten root and the minus dragged onto
#               the coefficient ("the i carries the minus").
#               CAUGHT READING THE OUTPUT ALOUD: absc's praise said "1 negatives,
#               1 positives" on the gentlest ask -- praise templates must stay
#               grammatical at count 1 ("{n} on each side" now). A NEW defect
#               class for the checklist: read the SMALLEST problem's praise, not
#               just first/last bank items.
#   2026-08-22  BUILD lg -- GEOMETRY UNITS 8 AND 9. ⭐ GEOMETRY IS COMPLETE: nine
#               units, 36 lessons, the same shape as Algebra I. 140 lessons -> 148,
#               137 ops (para, lshp, surf, svol + poft, notp, outc, twop).
#               UNIT 8, AREA, SURFACE AREA & VOLUME -- past Basic U9 and pre-u8,
#               not over them: the height that is NOT the slant (and the ask board
#               states the FORMULA, never the picked numbers -- choosing height
#               over slant IS the skill, caught in the read-aloud pass), the
#               composite floor (areas add, lengths never do), the cube's six
#               faces (the open-box slip: 4 walls, no lid), and the capstone that
#               finishes U4's scaling story: length pays the factor once, area
#               twice, VOLUME THREE TIMES -- with both wrong taps drawn from the
#               course's own history (the length habit and the area habit).
#               UNIT 9, PROBABILITY -- chance in child numbers, counts out of a
#               whole, never fractions: the whole bag is the out-of (the
#               odds-vs-probability slip "3 out of 2" is the standing wrong tap),
#               the complement shares the whole, choices TIMES up (not add), and
#               the two-way table closes the course read like an address -- row,
#               then column, the box where they cross.
#               RENDERER RULINGS (read first, as always): [[tree]] prints every
#               leaf product -- a giveaway machine on asks, so it STAYS ON THE
#               SHELF for the Probability & Statistics course; [[areamodel]]
#               prints its expanded product (teach boards only -- it draws the
#               outfit grid in how-many-ways' teach); [[twoway]] auto-computes all
#               totals, so the table ask is a CELL, the cong pattern. ⭐ twoway
#               draws for a scripted lesson for the first time.
#   2026-08-22  BUILD lf -- GEOMETRY UNITS 6 AND 7: THE RIM AND THE GRID. Two units
#               in one build. 132 lessons -> 140, 129 ops (cent, insc, iarc, alen +
#               vseg, dist, mid2, corn).
#               UNIT 6, CIRCLES -- the whole is 360, planted against the
#               straight-line habit (180 leaps to mind after three units of
#               triangles; it is the standing wrong tap). The inscribed-angle rule
#               is read BOTH directions in the isos/chas pair pattern, and arc
#               length closes the unit as one equal part of the distance around,
#               drawn on the shaded pie. ⭐ [[circle inscribed=]] (July's shelf)
#               draws its first scripted lessons -- and, like righttriangle in le,
#               READING THE RENDERER FIRST set the rule: it labels the vertex angle
#               at HALF the arc, so it carries teach/worked boards and the
#               angle-to-arc asks (where the label is the given) but never an
#               arc-to-angle ask (where the label would be the answer).
#               UNIT 7, COORDINATE GEOMETRY -- geometry moves onto the grid for
#               good: lengths along a grid line (the FENCEPOST trap: steps, never
#               dots -- "a fence with six posts has five rails"), the straight
#               distance as U5's Pythagoras under a slant (the wrong tap is the
#               TAXICAB walk, across plus up), U1's midpoint grown into two
#               dimensions, and the rectangle's fourth corner as the closer. The
#               wrong-coordinate error (a y handed back for an x) runs through the
#               whole unit, exactly as it ran through U2's moves.
#               The validator caught ONE word this build: the fourth-corner teach
#               said a corner "never borrows its x" -- "borrow" is banned (canon
#               "regroup"), and the regrouping canon polices geometry prose it was
#               never aimed at. One wording, one rule, everywhere -- working as
#               designed.
#   2026-08-22  BUILD le -- GEOMETRY UNITS 4 AND 5: THE SCALE AND THE CLIMB. Two
#               units in one build. 124 lessons -> 132, 121 ops (scal, sfac, mside,
#               sare + pyth, leg, tang, topp).
#               UNIT 4, SIMILARITY & DILATIONS -- one thread, four lessons: a scale
#               factor is a TIMES, never an ADD. The additive error ("3 grew by 3,
#               so 5 becomes 8") is the best-documented misconception in all of
#               similarity, and it stands as a distractor in EVERY lesson of the
#               unit -- as a+k in scal, as the difference in sfac and tang, as
#               b + a(k-1) in mside (its natural habitat), as a+k again in sare and
#               topp. The closer is the k² area surprise ("length pays the factor
#               once -- area pays it twice").
#               UNIT 5, RIGHT TRIANGLES & TRIGONOMETRY -- Pythagoras FORWARD and
#               BACKWARDS on named whole-number triples (wrong taps: adding the
#               legs = walking around the corner; stopping at the SQUARE of the
#               answer), then the tangent met as U4's ratio living inside one
#               triangle and as alg1-u4's "climb" renamed -- read both directions
#               in the isos/chas pair pattern.
#               ⭐ [[righttriangle]] (July's shelf) draws its first scripted
#               lessons -- and reading the renderer first set the rule: it ALWAYS
#               labels the hypotenuse (computed if not given), so it may carry
#               teach/worked boards and TANGENT asks, but never a Pythagorean ask
#               (it would print the answer). Those asks use [[triangle right=]].
#               CAUGHT READING THE OUTPUT ALOUD (the validator passed first try,
#               again): topp's ask said "the marked angle" over a [[triangle]]
#               board that draws NO mark -- speech may never claim a mark the
#               figure lacks (Jim's 2026-08-01 live catch, the split-ray lesson;
#               tang keeps "marked" because righttriangle really draws the θ arc).
#               And sfac's ask re-glossed "similar" in every problem (kw's
#               scaffold rule) -- givens only now.
#   2026-08-22  BUILD ld -- GEOMETRY UNITS 2 AND 3: THE SHAPE MOVES, THEN THE PROOFS
#               BEGIN. Two units in one build. 116 lessons -> 124, 113 ops (tran,
#               refl, htrn, rota + cong, isos, extr, chas).
#               UNIT 2, TRANSFORMATIONS & SYMMETRY -- the three moves, each owning
#               ONE coordinate rule: a slide changes one number by ADDING, a flip
#               changes ONE sign, a half turn changes BOTH. Every wrong tap in the
#               unit is the right rule aimed at the wrong coordinate, the wrong
#               direction, or the wrong number of signs -- and the closing lesson
#               (turn symmetry, 360 shared by the equal parts) has a wrong tap of
#               180, the half-turn habit, which the previous lesson just installed
#               ON PURPOSE: the two lessons argue with each other the way kz's
#               exponent pair does. [[graph points=]] carries the moving point; ask
#               boards never draw the image point (the kz/la giveaway class).
#               rota's surface is ky-tiny: the divisors of 360 between 3 and 24 are
#               EXACTLY twelve -- two pair-asks plus a ten-problem bank, no slack.
#               UNIT 3, CONGRUENCE & TRIANGLE PROOFS -- congruent means every
#               matching part is equal, and the LETTERS, not the picture, say which
#               parts match ("the copy may be turned or flipped -- Unit 2 taught you
#               exactly those moves"). Then the isosceles pair read BOTH directions
#               (base->apex, then apex->base with the order-slip distractor 90 - a),
#               and the exterior angle taught as the course's first little proof:
#               two owned facts chained, then the shortcut named. [[triangle
#               ticks=]] finally draws the equal-side marks it was built for in
#               July. First-pass authoring findings worth keeping: negative answers
#               must be SPOKEN as words in praise ("negative 3", never "-3" -- the
#               pre-u3 integer ops set the convention and the first draft broke it),
#               and two asks were trimmed for kw's scaffold-never-fades rule ("its
#               two base angles are equal too" restated the isosceles rule in every
#               problem; givens only now).
#   2026-08-22  BUILD lc -- ALGEBRA I COMPLETE, AND GEOMETRY OPENS. Two units in one
#               build. 108 lessons -> 116, 105 ops (mean, medn, rnge, outl + comp,
#               vert, circ, mid). ⭐ ALGEBRA I IS FINISHED: nine units, 36 lessons.
#               ⭐ GEOMETRY IS THE TENTH COURSE.
#               ALGEBRA I U9, DATA & STATISTICS -- and the LAST renderers on July's
#               shelf: [[dotplot]] and [[bars]] had never been drawn by a scripted
#               lesson. Every lesson puts the DATA on the board and asks a question
#               the picture can answer, which is the argument for teaching statistics
#               with a plot instead of a formula.
#               THE UNIT BUILDS TO ONE IDEA: mean and median are not interchangeable.
#               Three lessons lay the tools; the fourth walks one unusual number into
#               the room -- four children with 5 pencils, a fifth with 45 -- and the
#               mean jumps to 13 while the median stands at 5. "Not one child in that
#               room has 13 pencils." Every misleading statistic a child will ever
#               meet lives in that gap, and the wrong tap IS the mean.
#               GEOMETRY U1, FOUNDATIONS & CONSTRUCTIONS -- vocabulary laid with
#               FIGURES, not definitions: complementary angles on [[angle deg="90"
#               split=]], the crossing X on [[angle deg="180" split=]], radius and
#               diameter on [[circle]], the midpoint on [[numberline]]. The unit's
#               thread is pairs that add to a fixed total or relate by two, and EVERY
#               wrong tap is the other total (180 where 90 belongs -- and the teach
#               says out loud that 180 sticks because U8 taught it first) or the
#               other direction (halving where doubling belongs).
#               THE VALIDATOR CAUGHT SEVEN, one of them subtle and worth keeping:
#               "the total" is banned speech (canon "in all"), and it is also the
#               natural statistics word -- so the WORDING moved, not the rule. A child
#               who has heard "in all" since Entry keeps hearing it in Algebra I. Also
#               caught: "subtraction" contains the banned "subtract"; "makes"; and
#               rule 14 on spread, cross, degrees and halfway, each appearing only
#               against punctuation.
#   2026-08-22  BUILD la -- ALGEBRA I UNITS 7 AND 8, ONE BUILD (Jim: "do twice as
#               much as you have been doing between pushes"). 100 lessons -> 108,
#               97 ops (foil, fnum, gcfx, dsq + sqy, roots, vtx, hitg).
#               UNIT 7, POLYNOMIALS & FACTORING: the area model comes back and RUNS
#               BACKWARDS. (x + a)(x + b) is FOUR rooms -- middles ADD, corner TIMES,
#               and mixing those two jobs is the unit's recurring wrong tap.
#               Factoring is the same picture read the other way, a detective game
#               with two clues (adds to the x count AND timeses to the corner --
#               "a number that fits only one clue is an impostor"). gcfx demands
#               gcd(a, b) = 1 via a new _gcd helper: the pulled-out factor must be
#               the WHOLE common factor, or the factored form is a lie. dsq is the
#               vanishing middle -- the first identity that feels like a magic trick
#               and is just two rooms cancelling; a >= 3 because at 2 the square
#               collides with the double.
#               UNIT 8, QUADRATIC FUNCTIONS: the curve arrives, built on three
#               feelings: SQUARING IS NOT DOUBLING (sqy requires x >= 3 and its
#               teach names the trap's cause -- at 2 the two agree, and that
#               coincidence is what plants the habit); a product of zero means a
#               factor is zero (roots: "nobody asked for 3 + 5 or 3 x 5" -- the
#               wrong taps do arithmetic on the roots); a square is never negative,
#               so the curve has a FLOOR (vtx); and the ball comes down (hitg),
#               where the square root is met as the answer to "what number squared
#               equals 25" before it is ever a symbol -- and the wrong tap of 2a is
#               the child reaching for halving, "which undoes doubling, not
#               squaring".
#               CAUGHT READING THE BOARDS: vtx originally wrote "lowest y = 0 + 2 =
#               ?" -- the answer wearing a hat, the same giveaway class as kz's pond
#               sequence. The board now shows the rule and the floor, never the sum.
#   2026-08-22  BUILD kz -- ALGEBRA I UNIT 6: EXPONENTS & EXPONENTIAL FUNCTIONS.
#               ⭐ THE COURSE REACHES 100 LESSONS. 96 -> 100, 89 ops (exadd, exmul,
#               sci, dbl added). Prealgebra U1 taught what a power IS; this unit
#               teaches how powers BEHAVE.
#               Lessons 1 and 2 are a deliberate PAIR: the product rule (x³ · x² --
#               joining piles, powers ADD) and the power of a power ((x³)² -- copying
#               a pile, powers TIMES) are each other's classic confusion, taught
#               back-to-back, each offering the other's rule as its wrong tap. The
#               closing beat gives the one question that separates them: "am I
#               JOINING two piles, or COPYING a whole pile?"
#               Lesson 3 is scientific notation in child clothes (b × 10^a; the wrong
#               tap is the times-not-power reading, 3 × 10² tapped as 60). Lesson 4
#               is THE FIRST EXPONENTIAL GROWTH: the doubling pond, whose wrong tap
#               is the LINEAR THINKER'S answer (up by 2 a day) -- the board draws the
#               run-away sequence so the child watches doubling pull away from
#               walking. dbl requires at least 3 days: below that, doubling and
#               times-2-times-days agree and the error cannot be shown.
#               NEW module helper _sup(n) -- real superscripts for board text; expn
#               hard-coded ² and ³ because its powers stop at 3, Algebra I's do not.
#               CAUGHT READING THE BOARDS OUT LOUD: dbl's sequence originally ran ALL
#               THE WAY to the answer ("2 → 4 → 8 → 16" asking for 16). It now stops
#               one day short and ends on "?" -- a board that answers its own ask
#               teaches tapping, not doubling.
#   2026-08-22  BUILD ky -- ALGEBRA I UNIT 5: SYSTEMS OF EQUATIONS. 92 lessons -> 96,
#               85 ops (sys1, sys2, sumd, elim added). TWO RULES TRUE AT ONCE, opened
#               by [[graph]] drawing TWO LINES CROSSING (lines= splits on ";") -- the
#               crossing point is the answer standing on the board before anyone
#               computes it. Then the three classical moves in their plainest
#               clothes: SUBSTITUTION as "swap y for what it equals" (two letters
#               become one), the sum-and-difference puzzle (add the clues and the
#               smaller number cancels itself away), and ELIMINATION as two shopping
#               trips -- take one buy away from the other and the eraser VANISHES.
#               ONE DISTRACTOR RUNS THROUGH THE WHOLE UNIT: the value of the OTHER
#               unknown. In sys1 it is the y where the lines cross, in sys2 it is y
#               again, in elim it is the eraser's price. A system holds two answers,
#               and tapping the wrong one is the system-specific mistake -- offered
#               every time, and the teach beats name it every time.
#               AUTHORING NOTE WORTH KEEPING: sys1's constraint surface is genuinely
#               small -- with single-digit a there are only SIX distinct valid
#               problems, fewer than one bank. Its check now allows a up to 14 and
#               says why. The bank verifier caught ten bad picks before insertion
#               (sumd at a = 2b where the halving error IS the answer; elim at
#               3b = 2a where the eraser's price collides with it; sys2 at b = 3a
#               where stopping-at-2x collides with y) -- every one is now excluded
#               by the op's own check, not by hand-care.
#               The validator caught "makes" in sys1's ask ("what x makes both
#               rules...") and rule 14 demanded " cents " spoken standalone.
#   2026-08-22  BUILD kx -- ALGEBRA I UNIT 4: LINEAR FUNCTIONS & GRAPHS. 88 lessons
#               -> 92, 81 ops (lny, slp, yint, lin2 added).
#               ⭐ [[graph]] DRAWS ITS FIRST SCRIPTED LINE -- the real function
#               grapher, used by the generated lane since July and never by a
#               scripted lesson (the shelf: areamodel kt, angle-split ks, balance kv,
#               machine kw, grapher kx). A line is taught as THE MACHINE'S WHOLE
#               TABLE OF ANSWERS DRAWN AT ONCE -- every point an input standing under
#               its output -- so the unit sits directly on U3 rather than beside it.
#               The ladder: read one point off a line (wrong tap: the swapped
#               partner, answering y with the x you were given); SLOPE from two
#               points, before any formula, as "the climb per step" (wrong taps: the
#               heights -- where y landed and where it started -- versus how far it
#               MOVED); the starting height at x = 0, where 2 × 0 makes the times
#               part VANISH (wrong tap: the slope -- the other number in the rule);
#               and start-plus-climb answering any x, where y = ax + b is a sentence
#               ("start at b, climb a per step") before it is a formula (wrong tap:
#               the height one step LEFT -- the off-by-one graph-reading error).
#               Rule 14 forced "line" to be spoken as a standalone word -- it only
#               appeared against punctuation -- same punctuation-spacing fix as
#               "terms" in kt and "the term" in km.
#   2026-08-22  BUILD kw -- ALGEBRA I UNIT 3: FUNCTIONS & NOTATION. 84 lessons -> 88,
#               77 ops (fm1, fnot, fm2, fback added).
#               ⭐ [[machine]] GETS ITS FIRST SCRIPTED USE -- the last renderer on
#               July's figure shelf to be picked up (areamodel kt, angle-split ks,
#               balance kv). A function is taught as a MACHINE: door in, rule, door
#               out. The renderer prints "f(4) = 9" under the flow, so lesson 1 lets
#               the child STARE at the notation for a whole lesson before lesson 2
#               ever asks them to read it -- the shorthand arrives as a caption for
#               something familiar, not as a new thing.
#               THE NOTATION ERROR THE UNIT DEFUSES: f(3) read as f times 3. The
#               misreading is not stupid -- parentheses have meant times since the
#               distributive lesson, and the same marks suddenly mean "feed the
#               machine". The f-of-x lesson says that conflict OUT LOUD ("same marks,
#               different job") and offers the times-reading as the wrong tap on
#               every problem.
#               The rest of the ladder: two machines in a row (the first's output is
#               the second's input; wrong tap = the other order -- composition
#               without the word), and running the machine BACKWARDS (f of WHAT
#               equals 10 -- "an equation in machine clothes", tying straight back to
#               U2's balance; wrong tap = feeding the machine its own output).
#               fm2's asks open with "Two machines in a row." deliberately -- that is
#               scene-setting like rat's recipe, not rule re-teaching like the evxy
#               and mlx scaffolds that were trimmed; the distinction is recorded here
#               so a future sweep does not "fix" it.
#   2026-08-22  BUILD kv -- ALGEBRA I UNIT 2: LINEAR EQUATIONS & INEQUALITIES.
#               80 lessons -> 84, 73 ops (un1, un2, un3, ineq added). SOLVING BEGINS.
#               Unit 1 always handed the child what x was holding; from here the
#               EQUATION holds it, and the child gets it back by undoing -- the same
#               move off both sides.
#               ⭐ [[balance]] GETS ITS FIRST SCRIPTED USE -- the balance-scale
#               renderer, in the codebase since July, same story as [[areamodel]]
#               (kt) and [[angle split=]] (ks). An equation IS a balance; "take the
#               same off both sides or the scale tips" is the whole logic of solving,
#               drawn instead of asserted. Equals is taught as LEVEL.
#               The ladder: undo a plus, undo a times (a DIFFERENT undo -- choosing
#               which is the single biggest decision a solver makes, so it gets its
#               own lesson and its own wrong tap: 3x = 12 answered 9, the wrong-undo
#               error), two steps back in reverse order (socks before shoes -- the 3
#               went on last so it comes off first; the wrong tap is stopping at
#               "2x = 8" and calling 8 the answer, the same stop-at-step-one error as
#               rte/pcn/tri3), and LESS THAN, where the tap answer is the biggest
#               whole number allowed -- an inequality's answer is a crowd, a tap can
#               hold one number, and the wrong tap is the boundary itself (x < 7
#               answered 7), which is THE inequality misconception.
#               The validator caught "makes" twice in one teach beat ("plus 4 makes
#               11", "the picture that makes it honest") -- the first was the exact
#               habit the ban exists for; both reworded rather than the ban weakened.
#   2026-08-22  BUILD ku -- ALGEBRA I OPENS: UNIT 1, FOUNDATIONS & EXPRESSIONS.
#               76 lessons -> 80, 69 ops (ev2, evxy, cl2, dstm added). The course key
#               is "algebra1", matching curriculum.COURSES, whose own unit list names
#               this unit -- the lessons follow Jim's declared curriculum, not an
#               invented one.
#               Prealgebra U9 planted four seeds one at a time; this unit makes them
#               WORK TOGETHER: two-step evaluation (order of operations meets a letter
#               -- the add-first error b(a+c) is the wrong tap), a second letter
#               (proving x was never special; each letter keeps its own number),
#               collecting the x's PAST A Y (the first algebra done blind -- neither
#               letter's value is ever given -- with "9 of what?" as the
#               grab-everything error), and distributing over a take away, where the
#               invisible times carries a minus with it, drawn as an [[areamodel]]
#               with a NEGATIVE room (the renderer parses cols="x,-3" and prints the
#               expanded sum with the minus carried through).
#               Caught while reading the rendered asks out loud: evxy's ask opened
#               "Two letters now." in every one of twelve problems -- the same
#               scaffold-never-fades defect mlx had in build kt. The teach beats
#               introduce y; the ask just asks.
#   2026-08-21  BUILD kt -- PREALGEBRA UNIT 9: VARIABLES & EXPRESSIONS. THE COURSE'S
#               LAST UNIT. 72 lessons -> 76, 65 ops (evx, mlx, clt, dst added).
#               PREALGEBRA IS COMPLETE: nine units, 35 lessons (Unit 2 has three), entry ladder to the
#               doorway of algebra.
#               The order is the order the idea grows: a letter HOLDS a number (evx),
#               a number written against a letter means TIMES (mlx -- the one piece of
#               notation a child must simply be told, because nothing about it looks
#               like what it means), like terms collect by COUNTING (clt -- three x's
#               plus two x's are five x's, like apples), and a times DISTRIBUTES over
#               a parenthesis (dst).
#               ⭐ dst DRAWS THE DISTRIBUTIVE PROPERTY as an area model: a rectangle
#               4 tall and (x + 3) wide, cut into a 4x room and a 12 room, expanded
#               sum printed underneath -- using [[areamodel]], the algebra-tile
#               renderer in the registry since July and (exactly like [[angle split=]]
#               before build ks) never used by a scripted lesson until now. The child
#               is not handed the rule; the child is shown the two rooms. The teach
#               beat ties it back to rule one of prealgebra: parentheses SAY do the
#               inside first, but an x inside will not collapse -- so the times has to
#               reach in, and it reaches BOTH rooms.
#               The distractors are the unit's real errors: CONCATENATION (x holds 5,
#               "x + 3" tapped as 53 -- the documented universal first misreading of
#               substitution), 3x read as 3 plus x, counts timesed instead of added
#               (3x + 2x tapped as 6x), and the times never reaching the number
#               (4(x + 3) tapped as "plus 3").
#               Caught this build: (1) clt's neighbour distractor lands exactly on its
#               times-them distractor at 2x + 3x (both 6) -- its check now demands
#               three distinct options, the same repair shr and prop needed in kp.
#               (2) mlx's ask originally re-explained the invisible-times shorthand in
#               EVERY problem; a scaffold repeated in all twelve asks is a scaffold
#               that never fades, and fading it is what practice is for. The teach
#               beats own the explanation now.
#   2026-08-21  BUILD ks -- PREALGEBRA UNIT 8: MEASUREMENT & GEOMETRY BASICS.
#               68 lessons -> 72, 61 ops (cnv, tri, sla, tri3 added).
#               ⭐ THE FIRST SCRIPTED LESSONS THAT DRAW A REAL FIGURE. Basic Math's
#               geometry unit -- perimeter, area, quarter turns, volume -- draws NO
#               pictures at all: every board in it is a [[step]] line. Geometry is the
#               one subject where the picture IS the argument, and geo-figures.js has
#               carried [[triangle]] and [[angle]] since July. Three of these four
#               lessons put a figure up, and the straight-line lesson uses
#               [[angle deg="180" split="130" caption="a straight line split — 130° and the rest"]] -- a tag built on 2026-08-01 for
#               exactly that sentence, after Jim's beta run caught the tutor SAYING
#               "a ray splits it into two smaller angles" over a figure with no ray,
#               and never once used by a scripted lesson until now.
#               The ladder: change a unit (Unit 5's place value wearing a coat), halve
#               a rectangle to get a triangle, then the two facts every later geometry
#               course leans on -- a straight line is 180 degrees, and so are the three
#               angles of ANY triangle. That last lesson is the first in the whole
#               course whose answer comes from a rule about all triangles rather than
#               from counting something.
#               Distractors, all of them real errors: the wrong power of ten (cnv --
#               a child who knows a zero goes on and not how many), the rectangle
#               un-halved (tri), a full turn's 360 in place of a straight line's 180
#               (sla), and the two angles you were GIVEN added up (tri3 -- doing step
#               one and tapping it).
#               tri3 draws the right-angle square when one of its given angles is 90.
#               These figures are schematic by design, but a right angle drawn as a
#               lazy corner with "90°" written beside it is schematic in the one way
#               that teaches the wrong thing.
#   2026-08-21  BUILD kr -- PREALGEBRA UNIT 7: PERCENTS. 64 lessons -> 68, 57 ops
#               (pcn, asp, pwh, pup added). Basic Math's percent lesson only ever asks
#               for 10, 25 or 50 percent and answers them with a FRACTION SHORTCUT --
#               half, a fourth, a tenth. The shortcut is fine and it is also a dead
#               end: it says nothing at all about 30 percent or 70 percent. This unit
#               replaces it with one method that never runs out -- find ten percent,
#               then count how many tens you need -- and then runs that method in all
#               four directions a percent question can face: forwards (pcn), as a
#               reading of one number against another (asp, which is Unit 6's
#               proportion with 100 on the bottom), BACKWARDS from a part to the whole
#               (pwh, the direction children reverse), and finally up and down on a
#               price (pup).
#               THE ERROR THE LAST LESSON EXISTS FOR is moving a price by the PERCENT
#               NUMBER instead of by that percent OF the price -- 40 dollars up 10
#               percent read as 50 dollars, because 40 and 10 are two numbers and
#               adding them is the thing a child already knows how to do. It is the
#               wrong tap on every problem in that bank.
#               Two defects the validator could NOT see, found by reading the rendered
#               boards and options out loud:
#                 - pup drew the ten-percent step TWICE whenever the percent was ten
#                   ("10% of 40 = 4" then "10% = 4"), which teaches a child that the
#                   second step is empty. It is now drawn only when it says something
#                   new.
#                 - pwh's forward-error distractor rounds DOWN. At "6 is 20 percent of
#                   what?" it came out as 1, and 1 is not an answer any child arrives
#                   at -- it is a stub. The check now demands every wrong option be a
#                   real wrong answer, and the one bank item that relied on the stub
#                   was replaced.
#   2026-08-21  BUILD kp -- PREALGEBRA UNIT 6: RATIOS, RATES & PROPORTIONS.
#               60 lessons -> 64, 53 ops (rat, rte, prop, shr added). Basic Math's
#               "one costs" already finds a unit PRICE; these four are the family
#               around it, in the order the ideas depend on each other: keeping a
#               ratio's shape when both sides grow, scaling a rate over time (the same
#               move with a unit step in the middle), writing it as an equation with a
#               hole in it, and SPLITTING an amount in a ratio -- the genuinely
#               different one, because there the total is given and the parts have to
#               be counted before anything is shared. The unit is aimed at ONE error:
#               adding instead of timesing (2 to 3 grown to 4 read as "4 to 5"), and
#               three of the four lessons offer exactly that as their wrong tap.
#               THE VALIDATOR CO-AUTHORED AGAIN, and every catch is recorded here
#               because each one is a rule worth keeping: "makes" is banned speech
#               (canon is "equals") so the machine now FILLS bottles rather than making
#               them; "gives you" and "is the same as" were caught in teach prose; rule
#               14 demanded "per hour" and "proportion" be said out loud; and a share of
#               ONE part turned out to be the same number as the size of one part, so
#               shr's check now requires THREE DIFFERENT tap options and the 1-to-3
#               problem left the bank (it still teaches in the worked example, which is
#               prose, not a tap). prop got the same distinctness demand when two of its
#               distractors collided on 7.
#               ALSO CATCHING UP ON RULE 8, which builds kk through ko wrote as inline
#               section comments but never entered here:
#                 kk (2026-08-21) Prealgebra U1, Number Sense & Order of Operations --
#                     41 -> 45 lessons; ops tba, parf, expn, exo.
#                 km (2026-08-21) Prealgebra U3, Integers -- the first answers below
#                     zero; ops cbz, addneg, subneg, mulneg. A lesson may now declare
#                     min_value, because "every answer is at least 1" stopped being true
#                     the day negatives arrived; the option regex learned to see a minus
#                     sign. U2 (Factors, Multiples & Primes; nfac, spf, npf) shipped
#                     alongside it.  45 -> 52 lessons.
#                 kn (2026-08-21) Prealgebra U4, Fractions -- past Basic's unit
#                     fractions; ops nuf, uic, dbf, imp.  52 -> 56 lessons.
#                 ko (2026-08-21) Prealgebra U5, Decimals -- past Basic's naming, to
#                     PLACE; ops hun, x10, dth, dsh.  56 -> 60 lessons.
#   2026-08-21  BUILD kd -- THE CONTENT SWEEP + LESSONS THAT FLOW. Jim: "my priority
#               right now is to get the app up and running ... I wanna see it all up
#               and running, and then I can troubleshoot it from there." (Reviews,
#               quizzes, exams and depth-maintenance are DEFERRED to a design
#               conversation once content is complete -- his ruling, recorded.)
#               TEN new lessons close the audit's remaining named gaps: Entry U1
#               counting (a concrete-only op where the child COUNTS the stars -- the
#               spoken ask deliberately never says the number, with a speaks()
#               override documenting why), numbers before/after, counting coins
#               (nickels), story problems for Entry (add/take-away) and Basic
#               (multiply/divide) -- via a NEW per-problem "story" field: a problem
#               may carry its own spoken sentence, and every validator rule (digits
#               spoken, canon vocabulary, word caps via closure) applies to it
#               automatically -- plus hundredths, adding fractions with DIFFERENT
#               bottoms, least common multiple, angles as quarter turns, and volume.
#               41 lessons. Entry still lacks Time and Shapes units (no clock/shape
#               renderer on the pilot page yet -- recorded, not hidden).
#   2026-08-21  BUILD kc -- THE RE-CUT (Jim's ruling on the Eureka audit,
#               Eureka_Audit_Of_The_Scripted_Course_2026-08-21.md). The audit's
#               headline: my first eight lessons -- single-digit adding through
#               regrouping -- were ENTRY-LEVEL MATH content by Jim's own curriculum,
#               filed under Basic because Basic U1's title ("Place Value &
#               Whole-Number Operations") reads the same at every grade band. MOVED:
#               all eight to course "entry", units 2-6, ids renamed entry-*. Basic
#               gets its REAL Unit 1 -- place value to 1,000, rounding to tens and
#               hundreds, and an interleaved multi-digit review (interleaving is the
#               evidence-based practice; the review lesson carries mixed_review=True
#               and the ramp check deliberately does not apply). PLUS the audit's two
#               biggest holes: multi-digit multiplication and division (Eureka G4-M3,
#               43 days, the largest module in grades 3-5 -- previously ZERO lessons)
#               and fractions ON THE NUMBER LINE (Eureka G3-M5's core idea: a
#               fraction IS a number with a place, previously taught only as portions
#               of groups). New ops: pv (hundreds/tens/ones), r10/r100 (rounding,
#               with their OWN distractors -- +-10/+-100, because +-1 distractors
#               would make rounding trivially guessable), nl/nlw (number-line hops).
#               OP_EXT entries may now declare a "choices" function.
#   2026-08-21  BUILD jz -- THE COURSE CROSSES ALL NINE UNITS. Jim: "keep working ...
#               I wanna get through the whole basic math course." SEVENTEEN new
#               lessons spanning units 1-9 (regrouping, multiplication, division,
#               remainders, missing factors, GCF, unit fractions, equivalent
#               fractions, same-bottom fraction add/take-away, tenths, money,
#               percent, unit price, perimeter, area), built on a NEW data-driven
#               OP_EXT registry: each op declares its answer function, spoken/board/
#               praise templates, difficulty key, per-problem constraint, and (when
#               digits are spoken as words) its own rule-44 check. The original
#               +/−/t ops are untouched. Problems may now carry an optional third
#               number c (fractions need one); it joins the dedup key and the
#               choices rotation. ALSO FIXED: jy accidentally placed carrying BEFORE
#               two-digit-no-carry in the course order -- an explicit COURSE_ORDER
#               now owns the sequence and the module refuses to import if any lesson
#               is missing from it or listed twice. New canon vocabulary: "regroup"
#               (bans "borrow"), "too small" (jr's live catch), "times" (bans
#               "multiplied by"). Depth note, honest: units 2-9 open at survey depth
#               (about two lessons each); the factory deepens any unit on demand.
#   2026-08-21  BUILD jy -- CARRYING COMES HOME. Lesson 7, "Adding with carrying" --
#               the lesson build jr's whole consistency-memory fight was about. On
#               2026-08-20 Jim caught the live tutor teaching the SAME rule two ways
#               four turns apart ("over nine" ... "ten or more"), and jr pinned the
#               first phrasing per student at runtime. Here the fix becomes
#               structural: "over nine" is now CANON VOCABULARY -- "ten or more",
#               "more than nine" and "bigger than nine" are BANNED from every
#               lesson's closure by the validator, and the intervention prompt hands
#               the AI the same words. A child on the scripted path can no longer
#               hear the carrying rule in two costumes, because the second costume
#               cannot pass the build. New validator branch "carry": every bank
#               problem MUST carry in the ones (else the lesson teaches its idea on
#               examples that never use it) and must NOT overflow the tens.
#   2026-08-21  BUILD jx -- JIM'S SECOND WORDING RULING + LESSONS FIVE AND SIX.
#               Jim, on jw's names: "What I meant to say is we're going to be adding
#               or subtracting SINGLE-DIGIT numbers -- numbers one through nine.
#               That's how I would say it." Lessons are now named by their INPUTS,
#               the way a person says it: "Adding single-digit numbers", "Taking away
#               single-digit numbers", "...past ten", "...from bigger numbers" -- and
#               the validator grew a_max/b_max so the bank PROVABLY matches the name
#               (L2's 10−6 and L4's 20−10 were quietly violating it; both replaced).
#               NEW LESSONS: 5. "Tens and ones" (teen numbers as one ten and some
#               ones -- a new op "t", answer = 10a+b, so the answer key stays
#               computed) and 6. "Adding two-digit numbers" (no carrying -- and the
#               validator ENFORCES no-carry on every bank problem, so a carrying
#               problem cannot sneak into the lesson that promises none). Lessons may
#               now declare their own representation levels: lesson 6 is
#               abstract-only, because dropping a struggling child to counting 37
#               stars one at a time would be the opposite of help.
#   2026-08-21  BUILD jw -- THE FIRST FOUR LESSONS (the course takes shape). Jim's
#               playtest verdict on the pilot: "very, very impressive. I think it's
#               what we want" -- and his wording ruling: say it PLAINLY. "Adding
#               within 10" is curriculum-speak; the goal chip now says "Adding
#               numbers up to 10" and the teach script says out loud what the bound
#               actually is: "every answer will be ten or smaller."
#               GENERALIZED: problems carry an op ("+" or "-"), renderers and praise
#               are op-aware, each lesson declares its symbols, its bound, its
#               difficulty key and its own advance line. NEW LESSONS (each authored
#               to the 2026-08-20 research settings, each with its own closure):
#                 1. Adding numbers up to 10        (reworded per Jim)
#                 2. Taking away -- numbers up to 10 (the minus sign, "are left")
#                 3. Adding numbers up to 20        (counting on from the bigger)
#                 4. Taking away -- numbers up to 20 (counting back)
#               PILOT_LESSON remains LESSONS[0] so every existing pin and endpoint
#               default still resolves. The engine itself is UNCHANGED in behavior:
#               same settings, same intervene contract, same closure property.
#   2026-08-20  NEW FILE (build js -- THE PILOT). Jim's ruling of 2026-08-20
#               (Ruling_Scripted_First_And_The_Settings_2026-08-20.md): every lesson is
#               pre-authored, pre-verified, and pre-voiced up to the moment a child
#               responds; the AI steps in only when the child leaves the script; CODE,
#               not the model, returns the child to the script. Why: the day's
#               measurements -- ~$50/student/month against a $29 price, 11.5s median
#               turn, 42.4% verified right first try, 25 known-bad replies shipped in a
#               week -- are all costs of GENERATING teaching at runtime. A script
#               verified once is right forever, retries never, and speaks from cached
#               audio at zero marginal cost.
#
#               THIS FILE IS DELIBERATELY PURE. No model, no network, no store, no
#               clock: lesson data + a state-machine engine + a validator. Everything
#               here can therefore be verified exhaustively by ruletests PART 3cv, and
#               a verified script stays verified.
#
#               THE SETTINGS ARE THE RESEARCH DOC'S, NOT OPINIONS (citations there):
#               advance on 3 consecutive unaided correct, minimum 4, cap 10; worked
#               examples then example-problem pairs; error path = scripted "let's look
#               together" -> AI Model-Lead-Test -> engine-issued same-form retest;
#               second intervention on a skill drops a representation level (abstract ->
#               pictorial -> concrete); failing at concrete ends warmly and marks the
#               topic "learning"; a garbled answer gets ONE scripted re-ask, then
#               tap-only -- never an AI call for a mishearing.
#
#               ⭐ THE CLOSURE PROPERTY (the reason pre-rendered voice can be TOTAL):
#               every spoken string this engine can ever emit is enumerable in advance
#               by audio_lines(). PART 3cv drives every scenario the engine supports
#               and asserts each emitted spoken line is in that closure. If a future
#               edit adds a line the closure misses, the battery fails -- so the voice
#               cache can never be surprised at runtime.
```

I did no harm and this file is not truncated.
