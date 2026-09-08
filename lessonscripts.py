# =============================================================================
# lessonscripts.py  --  THE SCRIPTED-FIRST ENGINE (the course lives in lessons/)  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-09-08  OLDER NOTES (before 2026-09-01) live in
#               changelog/lessonscripts.py.md -- moved out on 2026-09-08 (build ui)
#               VERBATIM, 70 entries; 39 stay here. Keep adding new notes HERE, newest at
#               top; roll them out again (notes_rollout.py) when this header passes ~100
#               KB.
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
# =============================================================================

import re

# build ou: the shared number-word reader (tutor.py imports the same one).
import numwords as _numw

# ---- THE SETTINGS (from the 2026-08-20 research ruling; change THERE first) -------
ADVANCE_STREAK = 3        # advance on 3 consecutive unaided correct (EDM 2015)
# (ri, 2026-09-01) MIN_PROBLEMS = 4 removed by Jim's ruling: "The three in a row
# is what it specifically states to demonstrate that we're ready to move on to
# the next stage." The words promise three-in-a-row; the code stops demanding a
# fourth. A miss still costs extra problems (the streak resets), so only a
# PERFECT child finishes in exactly three.
MAX_PROBLEMS = 10         # past 10 without a streak, stop -- see drop/end rules
DROP_AFTER_INTERVENTIONS = 2   # 2nd AI intervention on a skill -> easier representation
LEVELS = ("abstract", "pictorial", "concrete")   # drop direction, left to right
# (sz, 2026-09-05) THE TIMES TABLE IS A PASS, NOT A STREAK. Jim, flag 22:40: "being
# able to complete a times table is mandatory to move on ... not just 3 in a row."
# His rulings ⑥ and ⑦ (2026-09-04): ONE through NINE times ONE through NINE -- 81
# facts, ten and above are place value -- and the table is complete on ONE FULL PASS
# WITH NO MISSES, any miss restarting the pass. A lesson that says "mastery": "table"
# practices this way: ADVANCE_STREAK and MAX_PROBLEMS do not apply inside its pass.
# A sitting still has to end: after TABLE_MAX_MISSES slips the student is released
# warmly (still learning, the warm choice), never ground through a sixth restart.
# ⚠️ If the watch shows students stalling here, the fallback Jim named is "every fact
# right once, saved across sessions" -- a small change to _table_* below, not a
# rewrite. Propose it then; do not soften this without a ruling.
TABLE_MAX = 9
TABLE_SIZE = TABLE_MAX * TABLE_MAX     # 81 facts in a pass
TABLE_MAX_MISSES = 5                   # slips in one sitting before the warm end
def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def _spf(n):
    """(ph) The smallest factor of n above 1 -- n itself when n is prime. Used by
    bfac, whose answer is n divided by this."""
    d = 2
    while d * d <= n:
        if n % d == 0:
            return d
        d += 1
    return n


BEAT_WORD_CAP = 80        # rule 19c / build jd: one beat per turn, spoken
# (pe) ...and one SENTENCE inside that beat a listener can hold. 34 is where the
# 336 authored lessons actually sat: 22 sentences were over it, every one of them
# clearer once split, and nothing legitimate was near the line.
SPOKEN_SENTENCE_CAP = 34

# ---- CANON VOCABULARY (build jr's lesson: one rule, one wording) ------------------
# canon phrase -> the synonyms that are BANNED anywhere in any lesson's speech.
# The validator enforces it; the intervention contract hands the canon to the AI.
VOCABULARY = {
    "put together": ("combine", "join together", "add together"),
    "in all": ("altogether", "all together", "the total"),
    "equals": ("makes", "gives you", "is the same as"),
    "take away": ("subtract", "remove"),
    "are left": ("remain", "remaining"),
    # jy: THE CARRYING RULE HAS ONE WORDING -- the exact defect Jim caught live on
    # 2026-08-20 ("over nine" ... then "ten or more", four turns apart), now banned
    # at authoring time across every lesson's closure.
    "over nine": ("ten or more", "more than nine", "bigger than nine"),
    # jz: regrouping's rule has one wording too (jr's other live catch), and so
    # does multiplication's name for itself.
    "regroup": ("borrow",),
    "too small": ("not big enough",),
    "times": ("multiplied by",),
}

# ---- PRAISE (rotated deterministically by problem index; all pre-renderable) ------
PRAISE_PREFIXES = ("That's it!", "You got it!", "Nice work!",       # (uq) "Nice counting!" praised a composition
                   "Exactly right!", "Well done!")

# fixed one-line scripts (every one of these is pre-rendered once)
LINE_WRONG = "Not quite — let's look at it together."
# (uq, 2026-09-08) Jim's flag 22:02: "There is no visual. Only audio." -- the practice
# intro spoke over a board that had scrolled away. It carries this card now.
PRACTICE_INTRO_BOARD = '[[card title="Your turn" items="Three right answers in a row | Tap an answer, say it, or type it | I\'m not sure is always a fair answer"]]'
LINE_REASK = "Let me say that again."
LINE_TAP = "Tap the answer you think is right."
LINE_END_GRACEFUL = ("We did some strong thinking today. We'll practice this again "
                     "next time — Mr. Cadabra is proud of you.")

# ---- build ou (2026-08-27): ANSWER FREELY -- the two lines free answers need ----
# A child may now TYPE or SAY an answer instead of tapping one. Code reads it
# (read_answer below); these are the only two things that can be said back that the
# tap-only lane never needed. Both are in STANDALONE_LINES, so they are rendered
# once into the audio closure and are free forever, like every other spoken line.
# ---- build ov (2026-08-27): THE TOPIC QUIZ ----------------------------------
# A quiz is the ONE time help is held back (the live lane's rule 47, and the
# reason a score means anything). So these lines say right or wrong and nothing
# else: no hint, no re-teach, no second try. THE SCORE IS NEVER SPOKEN -- it is
# drawn on the board as a card -- which keeps the audio closure at seven lines
# instead of one per possible score, and puts the number where a child can look
# at it twice.
# 80% to pass, the same bar store.QUIZ_PASS_PCT applies to every other topic
# quiz in the app. Stated here as a number because this module imports nothing
# with a database in it; PART 3fa pins the two against each other.
QUIZ_PASS_PCT = 80
QUIZ_LEN = 5                 # questions in a topic quiz, when the lesson can field them
QUIZ_MIN = 3                 # fewer than this and the lesson is simply not quizzed
LINE_QUIZ_INTRO = {
    3: ("Quiz time — three questions on this topic, and no hints from me. "
        "Show me what you have got."),
    4: ("Quiz time — four questions on this topic, and no hints from me. "
        "Show me what you have got."),
    5: ("Quiz time — five questions on this topic, and no hints from me. "
        "Show me what you have got."),
}
LINE_QUIZ_RIGHT = "Right."
LINE_QUIZ_WRONG = "Not that one."
LINE_QUIZ_PASS = ("That is a pass — this topic is yours. It is on your dashboard.")
LINE_QUIZ_FAIL = ("Not a pass this time, and that is useful to know. "
                  "We will practise this one again and you can retake it.")

LINE_WHOLE = "That one wants a whole number. Have another go."
LINE_UNSURE = ("Saying you are not sure is a good move. Tap the hand and ask me "
               "anything — or take a guess, and I will help either way.")

# (sp, 2026-09-05) THE REASON QUESTION'S TWO VERDICTS. "Say it" is beat six of the
# shape: after the streak, one question that asks not WHAT the answer was but WHY --
# a student who can pick the reason has learned the idea; one who cannot has learned
# the trick. A miss never fetches the model (there is nothing to re-teach that the
# picture does not say better), so both verdicts are authored and pre-rendered.
LINE_REASON_RIGHT = "That is the reason. Now you really have it."
LINE_REASON_WRONG = "Not that one. Let's look at the picture again."
REASON_TRIES = 2          # the picture replays once; a second miss ends warmly

# (sz, 2026-09-05) THE TIMES-TABLE PASS'S TWO LINES. A slip inside the pass draws the
# fact's picture (authored per fact, _table_miss) and then says this -- warmly, and
# with the rule in it, so the restart is never a surprise. The rest line closes a
# sitting that has slipped TABLE_MAX_MISSES times; it names the number so the words
# and the setting cannot drift apart (the battery pins them equal).
LINE_TABLE_RESTART = ("The table has to be right all the way through, so we start "
                      "again from the beginning. Every fact, one after another — "
                      "here we go.")
LINE_TABLE_REST = (f"{TABLE_MAX_MISSES} facts have slipped today, and that is enough "
                   "for one sitting. The ones we looked at are the ones to practice. "
                   "We will run the table again next time.")


def ans(p):
    """The one place an answer is computed. Problems are DATA (a, b, op) -- a wrong
    answer key cannot exist in this file, because none is ever typed.
    ops: "+" a+b · "-" a-b · "t" tens-and-ones, a tens + b ones = 10a+b."""
    op = p.get("op", "+")
    if op in OP_EXT:
        return OP_EXT[op]["ans"](p)
    if op == "-":
        return p["a"] - p["b"]
    if op == "t":
        return 10 * p["a"] + p["b"]
    return p["a"] + p["b"]


# =============================================================================
# THE LESSONS LIVE IN lessons/ (build uj, 2026-09-08): one file per course, pure data,
# joined in course order by lessons/__init__.py. This file is the ENGINE. The two
# names below are exactly what the 25,500 lines that used to sit here produced.
# =============================================================================
from lessons import LESSONS, COURSE_ORDER
_by_id = {les["id"]: les for les in LESSONS}
if sorted(COURSE_ORDER) != sorted(_by_id):
    raise RuntimeError("COURSE_ORDER and LESSONS disagree: "
                       + str(sorted(set(COURSE_ORDER) ^ set(_by_id))))
LESSONS = [_by_id[i] for i in COURSE_ORDER]

LESSON_BY_ID = {les["id"]: les for les in LESSONS}
PILOT_LESSON = LESSONS[0]   # every js/jt-era pin and endpoint default still resolves


# =============================================================================
# OP_EXT -- the data-driven op registry (build jz). The original three ops
# ("+", "-", "t") stay hand-written below; every newer op is an entry here:
#   ans(p)    the computed answer (never typed -- the founding rule)
#   spoken(p) what the child hears (abstract level; these lessons are abstract-only)
#   board(p)  the board tags
#   praise(p) the echo line after the praise prefix
#   key(p)    the difficulty-ramp key
#   check(p)  (ok, why) -- the per-problem constraint the validator enforces
#   speaks(p, spoken) -- rule-44 override for ops that speak digits as WORDS
# =============================================================================
_NUMWORD = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
            7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
            12: "twelve"}
_FRACWORD = {2: ("half", "halves"), 3: ("third", "thirds"),
             4: ("fourth", "fourths"), 5: ("fifth", "fifths"),
             6: ("sixth", "sixths"), 8: ("eighth", "eighths"),
             10: ("tenth", "tenths"), 12: ("twelfth", "twelfths")}


def _gcd(x, y):
    while y:
        x, y = y, x % y
    return x


_FRAC_BOTTOM = {2: "half", 3: "third", 4: "fourth", 5: "fifth", 6: "sixth",
                7: "seventh", 8: "eighth", 9: "ninth", 10: "tenth", 12: "twelfth"}
_FRAC_TOP = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
             7: "seven", 8: "eight", 9: "nine", 10: "ten"}


def _frac_words(a, b):
    """A fraction said the way a child reads it: (2, 3) -> "two thirds". Basic Math
    only ever spoke UNIT fractions ("one half"), so it had no need to pluralise;
    Prealgebra U4 is where non-unit fractions arrive (build kn)."""
    top = _FRAC_TOP.get(a, str(a))
    bot = _FRAC_BOTTOM.get(b, f"{b}th")
    return f"{top} {bot}" if a == 1 else f"{top} {bot}s"


def _medlist(p):
    """The odd-length list for the median lesson: b is the middle, a either side."""
    n = p["a"]
    return ",".join(str(p["b"] - n + i) for i in range(2 * n + 1))


def _medlist_words(p):
    return ", ".join(str(p["b"] - p["a"] + i) for i in range(2 * p["a"] + 1))


def _dotmode(p):
    """build lq: a dot plot whose tallest stack sits over a, b dots high, with
    small neighbouring stacks so the shape reads like real data."""
    vals = ([p["a"] - 2] + [p["a"] - 1] * 2 + [p["a"]] * p["b"]
            + [p["a"] + 1] * 2 + [p["a"] + 2])
    return ",".join(str(v) for v in vals)


def _dotcut(p):
    """build lq: c dots below the cutoff a, ONE dot sitting exactly on it, and b
    dots above -- so "more than a" has a real edge case standing on the line."""
    below = [p["a"] - 1 - (i % 3) for i in range(p["c"])]
    above = [p["a"] + 1 + (i % 3) for i in range(p["b"])]
    return ",".join(str(v) for v in sorted(below + [p["a"]] + above))


def _histvals(p):
    """build lq: raw values that fall into three well-separated groups, a, b and c
    of them -- however the renderer bins, the printed counts still add to a+b+c."""
    return ",".join(["5"] * p["a"] + ["15"] * p["b"] + ["25"] * p["c"])


def _farlist(p):
    """build lq: a tight cluster around a, and one stray far out at b."""
    vals = [p["a"] - 1, p["a"], p["a"], p["a"] + 1, p["a"] + 1, p["a"] + 2, p["b"]]
    return ",".join(str(v) for v in vals)


def _evenlist(p):
    """build lq: an EVEN-length list (2a numbers) whose two middles are b and b + 2
    -- so the median lands halfway between them, on a whole number."""
    lower = [p["b"] - 2 * (p["a"] - 1 - i) for i in range(p["a"])]
    upper = [p["b"] + 2 + 2 * i for i in range(p["a"])]
    return lower + upper


def _evenlist_words(p):
    return ", ".join(str(v) for v in _evenlist(p))


def _madlist(p):
    """build lq: four numbers sitting b and 3b either side of the mean a -- so the
    average distance comes out to exactly 2b."""
    return [p["a"] - 3 * p["b"], p["a"] - p["b"],
            p["a"] + p["b"], p["a"] + 3 * p["b"]]


def _madlist_words(p):
    return ", ".join(str(v) for v in _madlist(p))


_SCAT_X = (2, 4, 6, 8, 10, 12)
_SCAT_JIT = (0, 2, -1, 1, -2, 0)


def _scat_ys(p):
    """build lr: a rising cloud of six dots -- slope c, a little scatter either
    side of it, so the picture looks like real data instead of a ruler."""
    return [p["c"] * x + 2 + j for x, j in zip(_SCAT_X, _SCAT_JIT)]


def _scat_points(p):
    return ",".join(f"({x},{y})" for x, y in zip(_SCAT_X, _scat_ys(p)))


def _scat_at(p):
    """The y of the dot the question asks about (the child who practiced a hours)."""
    return _scat_ys(p)[_SCAT_X.index(p["a"])]


def _scat_next(p):
    """The y of the dot ONE TO THE RIGHT -- the misread-the-wrong-dot tap."""
    i = _SCAT_X.index(p["a"])
    ys = _scat_ys(p)
    return ys[i + 1] if i + 1 < len(ys) else ys[i - 1]


def _gcd(a, b):
    """math.gcd without the import ceremony (build la -- gcfx's honesty check:
    the pulled-out factor must be the WHOLE common factor)."""
    while b:
        a, b = b, a % b
    return a


_SUPS = {0: "\u2070", 1: "\u00b9", 2: "\u00b2", 3: "\u00b3", 4: "\u2074",
         5: "\u2075", 6: "\u2076", 7: "\u2077", 8: "\u2078", 9: "\u2079"}


def _sup(n):
    """A small exponent as a real superscript, for board text (build kz -- expn
    hard-coded \u00b2 and \u00b3 because its powers stop at 3; Algebra I's do not)."""
    return "".join(_SUPS[int(d)] for d in str(n))


def _prime_factors(n):
    """The primes whose product is n, repeats included: 12 -> [2, 2, 3]. Used by the
    Prealgebra U2 ops (build km); a lambda cannot express the loop readably."""
    out, d, n = [], 2, int(n)
    while d * d <= n:
        while n % d == 0:
            out.append(d)
            n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def _isqrt(n):
    """The whole square root of n, or 0 when n is not a perfect square (build lz).
    DiffEq U2's separable op solves y squared = 2ax + C and has to hand back a
    whole height; a lambda cannot say "and only if it comes out whole"."""
    n = int(n)
    if n < 0:
        return 0
    r = 0
    while (r + 1) * (r + 1) <= n:
        r += 1
    return r if r * r == n else 0


def _fact(n):
    """n factorial -- how many orders n things can stand in. Used by the
    Pre-Calc U8 counting op (build lp)."""
    out = 1
    for i in range(2, int(n) + 1):
        out *= i
    return out


def _npr(n, k):
    """Line-ups: n things, k picked, ORDER counted. n * (n-1) * ... k terms."""
    out = 1
    for i in range(int(k)):
        out *= int(n) - i
    return out


def _ncr(n, k):
    """Teams: n things, k picked, order IGNORED -- the line-ups divided by the
    k! orders each team could have been picked in. Whole by construction."""
    return _npr(n, k) // _fact(k)


# (mp) THE SHAPES ENTRY-LEVEL UNIT 9 CAN NAME, by how many sides they have. The
# side count IS the key, so two shapes cannot share one: "rectangle" and "rhombus"
# are both four-sided and would collide with "square", which is why they are taught
# by Geometry and not counted here.
_SHAPE = {3: "triangle", 4: "square", 5: "pentagon", 6: "hexagon",
          7: "heptagon", 8: "octagon", 10: "decagon"}


def _plural(n, word):
    """(mo) '1 hour', '2 hours' -- said the way a person says it.

    ⚠️ THE VALIDATOR CANNOT SEE THIS. Every check in validate() passed on "What time
    will it be 1 hours later?", because grammar is not arithmetic and no bound, ramp
    or vocabulary rule is broken by it. Four such lines were caught in ONE read-aloud
    pass on build mo -- "1 hours later", "1 weeks and 1 days", "1 cubes long" -- which
    is the whole argument for reading new content out loud before it is rendered in a
    real voice and played to a six-year-old.
    """
    return f"{n} {word}" if n == 1 else f"{n} {word}s"


def _irr(n, one, many):
    """(mr) The same, for words an 's' cannot make plural -- penny/pennies."""
    return f"{n} {one}" if n == 1 else f"{n} {many}"


def _fw(n, bottom):
    """(mr) '1 sixth', '3 sixths' -- the fraction word agreeing with its count.

    ⚠️ _FRACWORD has ALWAYS carried both forms; every caller simply took [1]. That
    is why the course said "1 sixths plus 3 sixths" out loud, in Mr. Cadabra's real
    voice, to seven-year-olds, for months."""
    return f"{n} {_FRACWORD[bottom][0 if n == 1 else 1]}"


# (sp, 2026-09-05) ROUNDING'S PICTURE. One number line per beat: the number sits
# between its two tens, the halfway mark is dashed, and -- once the answer is known --
# the hop to the nearer ten is drawn. The words on every rounding beat are READ OFF
# this picture ("past the halfway mark, closer to 50"); the ones-digit rule is the
# quick way to tell, stated after the picture has shown it, never instead of it.
def _r10_line(a, hop):
    lo = a // 10 * 10
    hi = lo + 10
    near = (a + 5) // 10 * 10
    tag = (f'[[numberline min="{lo}" max="{hi}" mid="{lo + 5}" points="{a}"')
    if hop:
        tag += f' hops="{a},{near}" caption="{a} rounds to {near}"'
    else:
        tag += f' caption="{a} sits between {lo} and {hi}"'
    return tag + "]]"


def _r100_line(a, hop):
    lo = a // 100 * 100
    hi = lo + 100
    near = (a + 50) // 100 * 100
    tag = (f'[[numberline min="{lo}" max="{hi}" mid="{lo + 50}" points="{a}"')
    if hop:
        tag += f' hops="{a},{near}" caption="{a} rounds to {near}"'
    else:
        tag += f' caption="{a} sits between {lo} and {hi}"'
    return tag + "]]"


def _r100_walkback(a):
    lo = a // 100 * 100
    hi = lo + 100
    d = (a // 10) % 10
    near = (a + 50) // 100 * 100
    where = ("below halfway" if d < 5 else
             "right at halfway" if d == 5 else "past halfway")
    way = "down" if d < 5 else "up"
    return (f"Look what you did: {a} sits between {lo} and {hi}. The tens digit "
            f"is {d} — {where} — so it hops {way} to {near}.")


# (sq) THE COLUMN, DRAWN AND READ BACK. The walk-back for adding and taking away
# two-digit numbers: the stacked column with the carry (or the regrouping) shown,
# and the words reading the column from the ones up, the way it is worked on paper.
def _col_add(a, b):
    total = a + b
    ones = a % 10 + b % 10
    if a >= 10 and b >= 10:
        if ones > 9:
            board = (f'[[column terms="{a}|{b}" op="+" carries="1_" result="{total}" '
                     f'caption="{a % 10} + {b % 10} = {ones}: write {ones % 10}, carry one ten"]]')
            spoken = (f"Look what you did: ones first — {a % 10} plus {b % 10} equals "
                      f"{ones}, over nine, so you wrote {ones % 10} and carried one ten. "
                      f"Tens: {a // 10} plus {b // 10} plus the 1 equals {total // 10}. "
                      f"{a} plus {b} equals {total}.")
        else:
            board = (f'[[column terms="{a}|{b}" op="+" result="{total}" '
                     f'caption="ones {a % 10} + {b % 10}, tens {a // 10} + {b // 10}"]]')
            spoken = (f"Look what you did: ones first — {a % 10} plus {b % 10} equals "
                      f"{ones}. Tens: {a // 10} plus {b // 10} equals {total // 10}. "
                      f"{a} plus {b} equals {total}.")
        return (spoken, board)
    board = (f'[[objects emoji="⭐" groups="{a}" add="{b}" caption="{a} + {b} = {total}"]]'
             f'[[step eq="{a} + {b} = {total}"]]')
    return (f"Look what you did: {a} and {b} more — {a} plus {b} equals {total}.", board)


def _col_sub(a, b):
    left = a - b
    if a >= 10 and b >= 10:
        if a % 10 < b % 10:
            board = (f'[[column terms="{a}|{b}" op="−" borrows="{a // 10 - 1}|{a % 10 + 10}" '
                     f'result="{left}" caption="{a % 10} is too small: regroup one ten into ten ones"]]')
            spoken = (f"Look what you did: {a % 10} is too small to take {b % 10} away, so "
                      f"you regrouped — one ten became ten ones. {a % 10 + 10} take away "
                      f"{b % 10} equals {a % 10 + 10 - b % 10}; {a // 10 - 1} take away "
                      f"{b // 10} equals {left // 10}. {a} take away {b} equals {left}.")
        else:
            board = (f'[[column terms="{a}|{b}" op="−" result="{left}" '
                     f'caption="ones {a % 10} − {b % 10}, tens {a // 10} − {b // 10}"]]')
            spoken = (f"Look what you did: ones first — {a % 10} take away {b % 10} equals "
                      f"{a % 10 - b % 10}. Tens: {a // 10} take away {b // 10} equals "
                      f"{left // 10}. {a} take away {b} equals {left}.")
        return (spoken, board)
    board = (f'[[objects emoji="⭐" groups="{a}" take="{b}" caption="{a} − {b} = {left}"]]'
             f'[[step eq="{a} − {b} = {left}"]]')
    return (f"Look what you did: {a}, take {b} away — {left} are left.", board)


def _tens_ones_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: {_plural(a, 'ten')} and {_plural(b, 'one')} — that is "
            f"{10 * a + b}.",
            f'[[placevalue t="{a}" o="{b}" caption="{a} tens and {b} ones = {10 * a + b}"]]')


# (sr, 2026-09-05) MULTIPLYING'S PICTURES. Small facts are an ARRAY (rows of dots
# -- the equal-groups meaning, then the times table read off it); a two-digit
# number times a digit is the AREA MODEL split into tens and ones. The ask draws
# the array only while the lesson is about MEANING (both numbers up to 5, the
# what-multiplying-means bank); a times-table fact is asked bare, because a 9-by-9
# dot grid on the question turns recall into counting. The walk-back always draws.
def _mul_rows_cols(p):
    """(ss) A STORY problem reads "each X holds a; there are b of them" -- b groups
    of a -- so its picture is b rows of a. A bare fact is a rows of b."""
    if p.get("story"):
        return p["b"], p["a"]
    return p["a"], p["b"]


def _mul_board(p):
    a, b = p["a"], p["b"]
    if a <= 5 and b <= 5:
        rows, cols = _mul_rows_cols(p)
        return (f'[[array rows="{rows}" cols="{cols}" view="groups" ask="1" '
                f'caption="{rows} groups of {cols}"]][[step eq="{a} × {b} = ?"]]')
    return f'[[step eq="{a} × {b} = ?"]]'


def _mul_worked(p):
    a, b = p["a"], p["b"]
    if p.get("story") and a <= 9 and b <= 9:
        rows, cols = _mul_rows_cols(p)
        chain = " plus ".join([str(cols)] * rows)
        return (f"Look what you did: {rows} groups of {cols} — {chain} equals {a * b}. "
                f"{a} times {b} equals {a * b}.",
                f'[[array rows="{rows}" cols="{cols}" view="groups" caption="{rows} groups of {cols} = {a * b}"]]')
    if a >= 10 and b <= 9:
        tens, ones = a // 10 * 10, a % 10
        board = (f'[[areamodel rows="{b}" cols="{tens},{ones}" '
                 f'caption="{a} × {b}: {tens} × {b} = {tens * b}, {ones} × {b} = {ones * b}"]]')
        spoken = (f"Look what you did: split {a} into {tens} and {ones}. {tens} times "
                  f"{b} equals {tens * b}; {ones} times {b} equals {ones * b}. "
                  f"{tens * b} plus {ones * b} equals {a * b}.")
        return (spoken, board)
    board = f'[[array rows="{a}" cols="{b}" caption="{a} rows of {b} = {a * b}"]]'
    if a <= 5:
        chain = " plus ".join([str(b)] * a)
        spoken = (f"Look what you did: {a} groups of {b} — {chain} equals {a * b}. "
                  f"{a} times {b} equals {a * b}.")
    else:
        spoken = (f"Look what you did: {a} rows of {b} is {a * b}. {a} times {b} "
                  f"equals {a * b}.")
    return (spoken, board)


def _mul_choices(p):
    """(sz, 2026-09-05) A TIMES QUESTION'S WRONG OPTIONS ARE NEIGHBOURING FACTS, not
    neighbouring numbers. The default distractors are the answer plus and minus one,
    which for 6 times 7 offers 41 | 42 | 43 -- no student who has ever seen a times
    table thinks 6 times 7 is 41, so the buttons tested nothing. The slips a student
    really makes are the facts either side: 6 times 6 is 36, 6 times 8 is 48. Those
    are the options now, for every times question in the course. A first factor of 1
    has no fact below it, so it offers the two above instead."""
    a, b = p["a"], p["b"]
    if b >= 2:
        return [a * (b - 1), a * b, a * (b + 1)]
    return [a * b, a * (b + 1), a * (b + 2)]


def _mtz_worked(p):
    a, b = p["a"], p["b"]
    tens, ones = a // 10, a % 10
    if b == 10:
        moved = (f"the {_plural(ones, 'one')} became {_plural(ones, 'ten')}" if a < 10 else
                 f"the {_plural(tens, 'ten')} became {_plural(tens, 'hundred')} and the "
                 f"{_plural(ones, 'one')} became {_plural(ones, 'ten')}")
        spoken = (f"Look what you did: every digit moved up one place — {moved} — and "
                  f"a zero holds the ones. {a} times 10 equals {a * 10}.")
        cap = f"{a} × 10 = {a * 10}: every digit up one place"
    else:
        moved = (f"the {_plural(ones, 'one')} became {_plural(ones, 'hundred')}" if a < 10 else
                 f"the {_plural(tens, 'ten')} became {_plural(tens, 'thousand')} and the "
                 f"{_plural(ones, 'one')} became {_plural(ones, 'hundred')}")
        spoken = (f"Look what you did: every digit moved up two places — {moved} — and "
                  f"two zeros hold the tens and the ones. {a} times 100 equals {a * 100}.")
        cap = f"{a} × 100 = {a * 100}: every digit up two places"
    return (spoken, f'[[placevalue n="{a * b}" caption="{cap}"]]')


# (ss, 2026-09-05) DIVIDING'S PICTURES -- the array read the other way. A small
# sharing question is ASKED as the dots to share and the empty boxes (total= ask=);
# its walk-back is the groups filled. A two-digit number divided by a digit is the
# AREA MODEL backwards -- split into tens and ones, each piece divided. Left-overs
# draw the full groups and the red dots that did not fit.
def _div_small(a, b):
    return a <= 45 and 2 <= b <= 9 and a // b <= 9


def _div_board(p):
    a, b = p["a"], p["b"]
    if _div_small(a, b):
        return (f'[[array total="{a}" rows="{b}" ask="1" '
                f'caption="share {a} into {b} equal groups"]][[step eq="{a} ÷ {b} = ?"]]')
    return f'[[step eq="{a} ÷ {b} = ?"]]'


def _div_worked(p):
    a, b = p["a"], p["b"]
    q = a // b
    tens, ones = a // 10 * 10, a % 10
    if a >= 20 and not _div_small(a, b) and tens % b == 0 and ones % b == 0 and b <= 9:
        board = (f'[[areamodel rows="{b}" cols="{tens // b},{ones // b}" '
                 f'caption="{a} ÷ {b}: {tens} ÷ {b} = {tens // b}, {ones} ÷ {b} = {ones // b}"]]')
        spoken = (f"Look what you did: split {a} into {tens} and {ones}. {tens} divided by "
                  f"{b} equals {tens // b}; {ones} divided by {b} equals {ones // b}. "
                  f"{tens // b} plus {ones // b} equals {q}.")
        return (spoken, board)
    if b <= 10 and q <= 12:
        board = (f'[[array rows="{b}" cols="{q}" view="groups" eq="{a} ÷ {b} = {q}" '
                 f'caption="{a} shared into {b} equal groups: {q} in each"]]')
        spoken = (f"Look what you did: share {a} into {b} equal groups — {q} in each. "
                  f"{a} divided by {b} equals {q}.")
        return (spoken, board)
    return (f"Look what you did: {a} divided by {b} equals {q}.",
            f'[[step eq="{a} ÷ {b} = {q}"]]')


def _rem_board(p):
    a, b = p["a"], p["b"]
    return (f'[[array total="{a}" rows="{a // b}" ask="1" label="groups of {b}" '
            f'eq="{a} ÷ {b} → left over = ?" '
            f'caption="{a} shared into groups of {b} — what is left over?"]]'
            f'[[step eq="{a} ÷ {b} → left over = ?"]]')


def _rem_worked(p):
    a, b = p["a"], p["b"]
    q, r = a // b, a % b
    board = (f'[[array rows="{q}" cols="{b}" extra="{r}" eq="{a} ÷ {b} = {q} left over {r}" '
             f'caption="{_plural(q, "group")} of {b}, {r} left over"]]')
    spoken = (f"Look what you did: {a} shared into groups of {b} fills "
              f"{_plural(q, 'group')} — {q} times {b} equals {q * b} — and "
              f"{a} take away {q * b} leaves {r}. So {r} {'is' if r == 1 else 'are'} left over.")
    return (spoken, board)


# (st, 2026-09-05) FACTORS AND MULTIPLES' PICTURES. A missing factor is the sharing
# question (b boxes, a dots: b groups of WHAT reach a?) and its walk-back the boxes
# filled. A factor pair is a RECTANGLE: b by q with area a (the area model's one
# cell), or the groups when small. The greatest common factor is the two factor
# lists on a VENN, the overlap holding what they share. The least common multiple
# is two NUMBER LINES, count-by hops on each, the first landing they share marked.
def _factors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def _mf_board(p):
    a, b = p["a"], p["b"]
    if a <= 60 and b <= 10:
        return (f'[[array total="{a}" rows="{b}" ask="1" eq="{b} × ? = {a}" '
                f'caption="{b} groups of what reach {a}?"]][[step eq="{b} × ? = {a}"]]')
    return f'[[step eq="{b} × ? = {a}"]]'


def _mf_worked(p):
    a, b = p["a"], p["b"]
    q = a // b
    if b <= 10 and q <= 12:
        board = (f'[[array rows="{b}" cols="{q}" view="groups" eq="{b} × {q} = {a}" '
                 f'caption="{b} groups of {q} reach {a}"]]')
    else:
        board = f'[[areamodel rows="{b}" cols="{q}" caption="{b} × {q} = {a}"]]'
    return (f"Look what you did: {b} groups of what reach {a}? Share {a} into {b} "
            f"groups — {q} in each. {b} times {q} equals {a}, so the missing factor is {q}.",
            board)


def _fpr_board(p):
    a, b = p["a"], p["b"]
    if a <= 60 and b <= 10:
        return (f'[[array total="{a}" rows="{b}" ask="1" eq="{a} = {b} × ?" '
                f'caption="{a} shared into {b} equal groups"]][[step eq="{a} = {b} × ?"]]')
    return f'[[step eq="{a} = {b} × ?"]]'


def _fpr_worked(p):
    a, b = p["a"], p["b"]
    q = a // b
    if b <= 10 and q <= 12:
        board = (f'[[array rows="{b}" cols="{q}" view="groups" eq="{b} × {q} = {a}" '
                 f'caption="{b} and {q} are a factor pair of {a}"]]')
    else:
        board = f'[[areamodel rows="{b}" cols="{q}" caption="a {b} by {q} rectangle holds {a}"]]'
    return (f"Look what you did: {a} shared into {b} groups is {q}, and {b} times {q} "
            f"comes straight back to {a}. So {b} and {q} are a factor pair of {a}.",
            board)


def _gcf_worked(p):
    a, b = p["a"], p["b"]
    fa, fb = _factors(a), _factors(b)
    both = [d for d in fa if d in fb]
    only_a = [d for d in fa if d not in fb]
    only_b = [d for d in fb if d not in fa]
    g = both[-1]
    j = lambda xs: ", ".join(str(x) for x in xs)
    board = (f'[[venn left="Factors of {a}" right="Factors of {b}" a="{j(only_a)}" '
             f'both="{j(both)}" b="{j(only_b)}" caption="they share {j(both)} — the greatest is {g}"]]')
    return (f"Look what you did: factors of {a}: {j(fa)}. Factors of {b}: {j(fb)}. "
            f"They share {j(both)}, and the greatest of those is {g}.", board)


def _lcm_lines(a, b, hops):
    m = a * b // _gcd(a, b)
    top = m if hops else max(a, b) * 4
    out = ""
    for n in (a, b):
        tag = f'[[numberline min="0" max="{top}"'
        if hops:
            tag += f' hops="{",".join(str(k * n) for k in range(0, m // n + 1))}" points="{m}"'
            tag += f' caption="count by {n} — lands on {m}"]]'
        else:
            tag += f' caption="count by {n}"]]'
        out += tag
    return out


def _lcm_board(p):
    a, b = p["a"], p["b"]
    return _lcm_lines(a, b, hops=False) + f'[[step eq="LCM of {a} and {b} = ?"]]'


def _lcm_worked(p):
    a, b = p["a"], p["b"]
    m = a * b // _gcd(a, b)
    ca = ", ".join(str(k * a) for k in range(1, m // a + 1))
    cb = ", ".join(str(k * b) for k in range(1, m // b + 1))
    return (f"Look what you did: count by {a}: {ca}. Count by {b}: {cb}. The first "
            f"number on both lists is {m} — the least common multiple.",
            _lcm_lines(a, b, hops=True))


# (su, 2026-09-05) FRACTIONS' PICTURES. A fraction on the NUMBER LINE (denom= makes
# the line speak in fourths); a fraction OF a group is the array shared and one
# group taken; equal fractions and simplest form are two PIES holding the same
# amount cut two ways.
def _frac_line(b, hops_to=None, point=None):
    tag = f'[[numberline min="0" max="1" denom="{b}"'
    if hops_to is not None:
        tag += ' hops="' + ",".join(str(round(k / b, 4)) for k in range(0, hops_to + 1)) + '"'
    if point is not None:
        tag += f' points="{round(point / b, 4)}"'
    return tag


def _nl_board(p):
    a, b = p["a"], p["b"]
    return (_frac_line(b) + f' caption="0 to 1 in {b} equal hops — where is {a}/{b}?"]]'
            f'[[step eq="land on {a}/{b} = ? hops"]]')


def _nl_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: the line from 0 to 1 is cut into {b} equal hops, so "
            f"each hop is one {_FRACWORD.get(b, (str(b) + 'th',))[0]}. {_plural(a, 'hop')} "
            f"from 0 land on {a} out of {b}.",
            _frac_line(b, hops_to=a, point=a) + f' caption="{_plural(a, "hop")} land on {a}/{b}"]]')


def _nlw_board(p):
    b = p["b"]
    return (_frac_line(b) + f' caption="0 to 1 in {b} equal hops — how many reach 1?"]]'
            f'[[step eq="reach 1 = ? hops"]]')


def _nlw_worked(p):
    b = p["b"]
    return (f"Look what you did: {b} hops of one {_FRACWORD.get(b, (str(b) + 'th',))[0]} "
            f"each — all {b} together — reach 1 whole. {b} out of {b} equals 1.",
            _frac_line(b, hops_to=b, point=b) + f' caption="all {b} hops reach 1 whole"]]')


def _of_board(p):
    a, b = p["a"], p["b"]
    w = _FRACWORD[b][0]
    return (f'[[array total="{a}" rows="{b}" ask="1" eq="1/{b} of {a} = ?" '
            f'label="{b} equal parts — one part is one {w}" '
            f'caption="share {a} into {b} equal parts"]][[step eq="1/{b} of {a} = ?"]]')


def _of_worked(p):
    a, b = p["a"], p["b"]
    q = a // b
    w = _FRACWORD[b][0]
    return (f"Look what you did: one {w} of {a} — share {a} into {b} equal parts, {q} "
            f"in each part. One part is one {w}. One {w} of {a} equals {q}.",
            f'[[array rows="{b}" cols="{q}" view="groups" eq="1/{b} of {a} = {q}" '
            f'caption="{b} equal parts of {a} — one part is {q}"]]')


def _eqf_board(p):
    b, c = p["b"], p["c"]
    return (f'[[pie parts="{b}" shaded="1" caption="one {_FRACWORD[b][0]}"]]'
            f'[[pie parts="{c}" shaded="0" caption="cut into {c}: how many {_FRACWORD[c][1]} '
            f'is the same amount?"]][[step eq="1/{b} = ?/{c}"]]')


def _eqf_worked(p):
    b, c = p["b"], p["c"]
    k = c // b
    return (f"Look what you did: cut every {_FRACWORD[b][0]} into {_NUMWORD[k]} pieces "
            f"and the whole is in {_FRACWORD[c][1]}. One {_FRACWORD[b][0]} became "
            f"{_NUMWORD[k]} {_FRACWORD[c][1]} — {k} out of {c} — the same amount, cut smaller.",
            f'[[pie parts="{b}" shaded="1" caption="one {_FRACWORD[b][0]}"]]'
            f'[[pie parts="{c}" shaded="{k}" caption="{_NUMWORD[k]} {_FRACWORD[c][1]} — the same amount"]]')


def _simp_board(p):
    a, b = p["a"], p["b"]
    if b <= 12:
        return (f'[[pie parts="{b}" shaded="{a}" caption="{a} out of {b}"]]'
                f'[[step eq="{a}/{b} → ?/…"]]')
    return f'[[step eq="{a}/{b} → ?/…"]]'


def _simp_worked(p):
    a, b = p["a"], p["b"]
    g = _gcd(a, b)
    na, nb = a // g, b // g
    board = ""
    if b <= 12:
        board += f'[[pie parts="{b}" shaded="{a}" caption="{a} out of {b}"]]'
    board += f'[[pie parts="{nb}" shaded="{na}" caption="{na} out of {nb} — the same amount, simplest form"]]'
    return (f"Look what you did: {a} and {b} both share {g}, so divide both by {g}. "
            f"{a} out of {b} is {na} out of {nb} — the same amount, in its simplest form.",
            board)


# (sv, 2026-09-05) ADDING AND TAKING AWAY FRACTIONS' PICTURE: the fraction line.
# Same bottom: hop from the first fraction by the second and read where you land.
# Different bottoms: the first fraction is found on the FINER line (one half is
# four eighths on a line cut into eighths), then the hop. The ask shows the line
# with the starting fraction marked and the hop withheld.
def _fl(c, hops=None, points=None, caption=""):
    tag = f'[[numberline min="0" max="1" denom="{c}"'
    if hops:
        tag += ' hops="' + ",".join(str(round(h / c, 4)) for h in hops) + '"'
    if points:
        tag += ' points="' + ",".join(str(round(pt / c, 4)) for pt in points) + '"'
    return tag + f' caption="{caption}"]]'


def _fa_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (_fl(c, points=[a], caption=f"start at {a}/{c} — hop {b} more {_FRACWORD[c][1]}")
            + f'[[step eq="{a}/{c} + {b}/{c} = ?/{c}"]]')


def _fa_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: the pieces are all {_FRACWORD[c][1]}, so you just "
            f"counted. Start at {_fw(a, c)}, hop {b} more — {a} plus {b} equals {a + b}. "
            f"{_fw(a, c)} plus {_fw(b, c)} equals {_fw(a + b, c)}.",
            _fl(c, hops=[0, a, a + b], points=[a + b],
                caption=f"{a}/{c} + {b}/{c} = {a + b}/{c}"))


def _fs_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (_fl(c, points=[a], caption=f"start at {a}/{c} — hop back {b} {_FRACWORD[c][1]}")
            + f'[[step eq="{a}/{c} − {b}/{c} = ?/{c}"]]')


def _fs_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: the pieces are all {_FRACWORD[c][1]}, so you just "
            f"counted back. Start at {_fw(a, c)}, hop back {b} — {a} take away {b} "
            f"equals {a - b}. {_fw(a, c)} take away {_fw(b, c)} equals {_fw(a - b, c)}.",
            _fl(c, hops=[a, a - b], points=[a - b],
                caption=f"{a}/{c} − {b}/{c} = {a - b}/{c}"))


def _fu_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (_fl(c, points=[c // b], caption=f"one {_FRACWORD[b][0]} on a line cut into "
                                            f"{_FRACWORD[c][1]} — then hop {a} more")
            + f'[[step eq="1/{b} + {a}/{c} = ?/{c}"]]')


def _fu_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    k = c // b
    return (f"Look what you did: on a line cut into {_FRACWORD[c][1]}, one "
            f"{_FRACWORD[b][0]} sits at {_fw(k, c)}. Now both are {_FRACWORD[c][1]}: hop "
            f"{a} more — {k} plus {a} equals {k + a}. One {_FRACWORD[b][0]} plus "
            f"{_fw(a, c)} equals {_fw(k + a, c)}.",
            _fl(c, hops=[0, k, k + a], points=[k + a],
                caption=f"1/{b} = {k}/{c}, then + {a}/{c} = {k + a}/{c}"))


def _fus_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (_fl(c, points=[c // b], caption=f"one {_FRACWORD[b][0]} on a line cut into "
                                            f"{_FRACWORD[c][1]} — then hop back {a}")
            + f'[[step eq="1/{b} − {a}/{c} = ?/{c}"]]')


def _fus_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    k = c // b
    return (f"Look what you did: on a line cut into {_FRACWORD[c][1]}, one "
            f"{_FRACWORD[b][0]} sits at {_fw(k, c)}. Now both are {_FRACWORD[c][1]}: hop "
            f"back {a} — {k} take away {a} equals {k - a}. One {_FRACWORD[b][0]} take "
            f"away {_fw(a, c)} equals {_fw(k - a, c)}.",
            _fl(c, hops=[k, k - a], points=[k - a],
                caption=f"1/{b} = {k}/{c}, then − {a}/{c} = {k - a}/{c}"))


# (sw, 2026-09-05) DECIMALS AND MONEY'S PICTURES. Tenths are hops on the 0-to-1 line
# (which already speaks in tenths); hundredths, and tenths meeting hundredths, are the
# HUNDREDTHS SQUARE; dimes and pennies are the place-value chart -- dimes are tens,
# pennies are ones, which is the whole lesson.
def _dt_board(p):
    a, b = p["a"], p["b"]
    return (f'[[numberline min="0" max="1" points="{a / 10}" '
            f'caption="start at 0.{a} — hop {_fw(b, 10)} more"]][[step eq="0.{a} + 0.{b} = 0.?"]]')


def _dt_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: tenths are tenths, so you counted them. Start at "
            f"0.{a}, hop {b} more tenths — {a} plus {b} equals {a + b}. {_fw(a, 10)} plus "
            f"{_fw(b, 10)} equals {_fw(a + b, 10)}, written 0.{a + b}.",
            f'[[numberline min="0" max="1" hops="0,{a / 10},{(a + b) / 10}" points="{(a + b) / 10}" '
            f'caption="0.{a} + 0.{b} = 0.{a + b}"]]')


def _dh_board(p):
    a, b = p["a"], p["b"]
    return (f'[[hundredgrid shaded="{a}" plus="{b}" ask="1" '
            f'caption="{a} hundredths, then {b} more"]][[step eq="0.{a:02d} + 0.{b:02d} = 0.?"]]')


def _dh_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: hundredths are hundredths, so you counted the cells. "
            f"{a} shaded, then {b} more — {a} plus {b} equals {a + b}. {a} hundredths "
            f"plus {b} hundredths equals {a + b} hundredths, written 0.{a + b:02d}.",
            f'[[hundredgrid shaded="{a}" plus="{b}" caption="0.{a:02d} + 0.{b:02d} = 0.{a + b:02d}"]]')


def _m_board(p):
    a, b = p["a"], p["b"]
    return (f'[[placevalue t="{a}" o="{b}" ask="1" caption="dimes are tens, pennies are ones"]]'
            f'[[step eq="{a} dimes + {b} pennies = ? cents"]]')


def _m_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: dimes are tens and pennies are ones. {_plural(a, 'dime')} "
            f"bring {10 * a} cents, {_irr(b, 'penny', 'pennies')} bring {b} more. {10 * a} "
            f"plus {b} equals {10 * a + b} cents.",
            f'[[placevalue t="{a}" o="{b}" caption="{a} dimes + {b} pennies = {10 * a + b} cents"]]')


def _t2h_board(p):
    a, b = p["a"], p["b"]
    return (f'[[hundredgrid shaded="{10 * a}" plus="{b}" ask="1" '
            f'caption="{_plural(a, "tenth")} — full rows — then {_plural(b, "hundredth")}"]]'
            f'[[step eq="{_plural(a, "tenth")} + {_plural(b, "hundredth")} = ? hundredths"]]')


def _t2h_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: a tenth is a full row of ten hundredths, so "
            f"{_plural(a, 'tenth')} is {10 * a} hundredths — {a} full rows. Then {b} "
            f"more. {10 * a} plus {b} equals {10 * a + b} hundredths.",
            f'[[hundredgrid shaded="{10 * a}" plus="{b}" '
            f'caption="{_plural(a, "tenth")} = {10 * a} hundredths, + {b} = {10 * a + b}"]]')


# (sx, 2026-09-05) PERCENT'S PICTURES. "What percent" lands on the HUNDREDTHS SQUARE
# in percent mode (the part, asked as a pie or a bar). A percent OF a number is the
# sharing picture -- 50 percent is one of two equal parts, 25 one of four, 10 one of
# ten. Percent off is a TAPE: the discount and what you pay, side by side, under the
# price. What one costs is the sharing picture again.
def _wpc_board(p):
    a, b = p["a"], p["b"]
    if b <= 10:
        pic = f'[[pie parts="{b}" shaded="{a}" caption="{a} out of {b}"]]'
    else:
        pic = f'[[tape parts="{a} | {b - a}" total="{b}" caption="{a} out of {b}"]]'
    return pic + f'[[step eq="{a} out of {b} = ? percent"]]'


def _wpc_worked(p):
    a, b = p["a"], p["b"]
    k = 100 // b
    pct = 100 * a // b
    return (f"Look what you did: percent means out of a hundred. {b} times {k} is a "
            f"hundred, so do the same to the top — {a} times {k} is {pct}. {a} out of "
            f"{b} is {pct} percent.",
            f'[[hundredgrid shaded="{pct}" unit="percent" caption="{a} out of {b} = {pct} out of 100 = {pct}%"]]')


def _pc_board(p):
    a, b = p["a"], p["b"]
    parts = 100 // a
    return (f'[[array total="{b}" rows="{parts}" ask="1" eq="{a}% of {b} = ?" '
            f'label="{a}% is one of {parts} equal parts" caption="share {b} into {parts} equal parts"]]'
            f'[[step eq="{a}% of {b} = ?"]]')


def _pc_worked(p):
    a, b = p["a"], p["b"]
    parts = 100 // a
    q = a * b // 100
    name = {2: "one half", 4: "one fourth", 10: "one tenth"}.get(parts, f"one of {parts}")
    return (f"Look what you did: {a} percent is {name}. Share {b} into {parts} equal parts "
            f"and take one — {q}. {a} percent of {b} equals {q}.",
            f'[[array rows="{parts}" cols="{q}" view="groups" eq="{a}% of {b} = {q}" '
            f'caption="{a}% = {name} — one of the {parts} parts is {q}"]]')


def _poff_board(p):
    a, b = p["a"], p["b"]
    return (f'[[tape parts="{b}% off | you pay" total="{a}" '
            f'caption="the price is {a} — the discount is the part you do not pay"]]'
            f'[[step eq="{a} − {b}% of {a} = ?"]]')


def _poff_worked(p):
    a, b = p["a"], p["b"]
    d = a * b // 100
    pay = a - d
    return (f"Look what you did: two steps. The discount first — {b} percent of {a} is "
            f"{d}. Then take it away: {a} take away {d} is {pay}. You pay {pay} dollars; "
            f"the {d} is what you saved.",
            f'[[tape parts="{d} | {pay}" total="{a}" caption="discount {d} — you pay {pay}"]]')


def _rate_board(p):
    a, b = p["a"], p["b"]
    return (f'[[array total="{a}" rows="{b}" ask="1" eq="{a} ÷ {b} = ?" '
            f'label="{b} apples" caption="{a} dollars shared over {b} apples"]]'
            f'[[step eq="{a} ÷ {b} = ?"]]')


def _rate_worked(p):
    a, b = p["a"], p["b"]
    q = a // b
    return (f"Look what you did: {a} dollars shared over {b} apples — {q} each. {a} "
            f"divided by {b} equals {q}. One apple costs {q} dollars.",
            f'[[array rows="{b}" cols="{q}" view="groups" eq="{a} ÷ {b} = {q}" '
            f'caption="each apple costs {q} dollars"]]')


# (sy, 2026-09-05) MEASURING'S PICTURES. Perimeter and area are a RECTANGLE on a unit
# grid -- the walk around it, or the squares inside it. Quarter turns are a circle cut
# into four, the turned quarters shaded. Volume is the box (solid) and one layer as an
# array, times the layers.
def _peri_board(p):
    a, b = p["a"], p["b"]
    return (f'[[rectangle w="{a}" h="{b}" show="perimeter" ask="1" caption="walk all the way around"]]'
            f'[[step eq="{a} + {b} + {a} + {b} = ?"]]')


def _peri_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: you walked all four sides — long, wide, long, wide. "
            f"{a} plus {b} plus {a} plus {b} equals {2 * (a + b)}. The perimeter is "
            f"{2 * (a + b)}.",
            f'[[rectangle w="{a}" h="{b}" show="perimeter" caption="around the outside: {2 * (a + b)}"]]')


def _area_board(p):
    a, b = p["a"], p["b"]
    return (f'[[rectangle w="{a}" h="{b}" show="area" ask="1" caption="count the squares inside"]]'
            f'[[step eq="{a} × {b} = ?"]]')


def _area_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: the inside is {_plural(b, 'row')} of {_plural(a, 'square')}. "
            f"{a} times {b} equals {a * b}. The area is {a * b} squares.",
            f'[[rectangle w="{a}" h="{b}" show="area" caption="{b} rows of {a} = {a * b} squares"]]')


def _ang_board(p):
    a = p["a"]
    return (f'[[pie parts="4" shaded="{a}" caption="{a} quarter turn{"" if a == 1 else "s"} of the circle"]]'
            f'[[step eq="{a} × 90° = ?"]]')


def _ang_worked(p):
    a = p["a"]
    return (f"Look what you did: each quarter of the circle is 90 degrees, and you "
            f"counted {a} of them — {a} times 90 equals {90 * a}. {a} quarter "
            f"turn{'' if a == 1 else 's'} is {90 * a} degrees.",
            f'[[pie parts="4" shaded="{a}" caption="{a} × 90° = {90 * a}°"]]')


def _angq_board(p):
    a = p["a"]
    return (f'[[pie parts="4" shaded="0" caption="each quarter is 90° — how many make {a}°?"]]'
            f'[[step eq="{a}° = ? × 90°"]]')


def _angq_worked(p):
    a = p["a"]
    q = a // 90
    counts = ", ".join(str(90 * k) for k in range(1, q + 1))
    return (f"Look what you did: count by 90 — {counts} — that is {q} "
            f"count{'' if q == 1 else 's'}. {a} degrees is {q} quarter "
            f"turn{'' if q == 1 else 's'}.",
            f'[[pie parts="4" shaded="{q}" caption="{a}° = {q} quarter turn{"" if q == 1 else "s"}"]]')


def _vol_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[solid kind="prism" w="{a}" d="{b}" h="{c}" caption="{a} long, {b} wide, {c} tall"]]'
            f'[[step eq="{a} × {b} × {c} = ?"]]')


def _vol_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    layer = a * b
    return (f"Look what you did: one layer is {a} times {b} — {_plural(layer, 'cube')}. "
            f"There {'is' if c == 1 else 'are'} {_plural(c, 'layer')}. {layer} times {c} "
            f"equals {layer * c} cubes.",
            f'[[array rows="{b}" cols="{a}" caption="one layer: {a} × {b} = {layer} cubes"]]'
            f'[[solid kind="prism" w="{a}" d="{b}" h="{c}" caption="{_plural(c, "layer")}: {layer} × {c} = {layer * c} cubes"]]')


# (tc, 2026-09-05) PREALGEBRA UNIT 1'S PICTURE: THE ORDER OF OPERATIONS MARCHES DOWN THE
# BOARD. [[solve]] draws the starting line and then each move as "what you did" over
# the line it produces -- "times first" over 2 + 12, "then add" over 14 -- so the
# student sees the ORDER as a picture of steps, not a rule in words. A square number is
# a square (the area model); a cube is a cube (the solid), which is the first honest
# picture of a to-the-power-3 the course has had.
def _tba_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: the times first — {b} times {c} equals {b * c}. Then the "
            f"add — {a} plus {b * c} equals {a + b * c}.",
            f'[[solve start="{a} + {b} × {c}" steps="times first : {a} + {b * c} | '
            f'then add : {a + b * c}" caption="{a} + {b} × {c} = {a + b * c}"]]')


def _parf_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    s = a + b
    return (f"Look what you did: inside the parentheses first — {a} plus {b} equals {s}. "
            f"Then the times — {s} times {c} equals {s * c}.",
            f'[[solve start="({a} + {b}) × {c}" steps="inside first : {s} × {c} | '
            f'then times : {s * c}" caption="({a} + {b}) × {c} = {s * c}"]]')


def _expn_worked(p):
    a, b = p["a"], p["b"]
    if b == 2:
        return (f"Look what you did: {a} squared is two {a}s multiplied — {a} times {a} "
                f"equals {a * a}. {a} rows of {a} really do make a square.",
                f'[[areamodel rows="{a}" cols="{a}" caption="{a}² = {a} × {a} = {a * a}"]]')
    return (f"Look what you did: {a} to the power 3 is three {a}s multiplied — {a} times "
            f"{a} times {a} equals {a ** 3}. A {a} by {a} by {a} block of cubes holds "
            f"{a ** 3}.",
            f'[[solid kind="prism" w="{a}" d="{a}" h="{a}" caption="{a}³ = {a} × {a} × {a} = {a ** 3}"]]')


def _exo_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    sq, pr = a * a, b * c
    return (f"Look what you did: the power first — {a} squared equals {sq}. The times next "
            f"— {b} times {c} equals {pr}. The add last — {sq} plus {pr} equals {sq + pr}.",
            f'[[solve start="{a}² + {b} × {c}" steps="power first : {sq} + {b} × {c} | '
            f'times next : {sq} + {pr} | add last : {sq + pr}" caption="{a}² + {b} × {c} = {sq + pr}"]]')


# (tc, 2026-09-05) PREALGEBRA UNIT 2'S PICTURES: a factor pair is a RECTANGLE (the array,
# or the area model when it is wide), the factors of a number are its pairs written out,
# the hunt for the smallest factor is the tries written in order with the one that fits
# ticked, and breaking into primes is the LADDER -- the number split, then split again,
# marching down until only primes are left.
def _factor_pairs(n):
    return [(d, n // d) for d in range(1, int(n ** 0.5) + 1) if n % d == 0]


def _pair_board(a, b, caption):
    """A rectangle for the factor pair a × b: dots when it fits, the area model when wide."""
    if a <= 10 and b <= 12:
        return f'[[array rows="{a}" cols="{b}" caption="{caption}"]]'
    return f'[[areamodel rows="{a}" cols="{b}" caption="{caption}"]]'


def _nfac_worked(p):
    n = p["a"]
    pairs = _factor_pairs(n)
    facs = sorted({x for pr in pairs for x in pr})
    lines = " | ".join(f"{d} × {q}" for d, q in pairs)
    said = ", ".join(f"{d} and {q}" for d, q in pairs)
    j = ", ".join(str(x) for x in facs)
    ex = pairs[len(pairs) // 2]
    return (f"Look what you did: the factor pairs of {n} are {said}. Write every number "
            f"in them once — {j} — and that is {len(facs)} factors.",
            f'[[write lines="{lines}" caption="the factors of {n}: {j} — {len(facs)} of them"]]'
            + _pair_board(ex[0], ex[1], f"{ex[0]} × {ex[1]} = {n}"))


def _spf_worked(p):
    n = p["a"]
    d = _spf(n)
    tries = [t for t in (2, 3, 5, 7) if t < d]
    lines = " | ".join(f"{n} ÷ {t} leaves {n % t} ✗" for t in tries) + (" | " if tries else "") + f"{n} ÷ {d} = {n // d} ✓"
    said = ("" if not tries else " and ".join(f"{t} leaves {n % t} over" for t in tries) + ", so no. ")
    return (f"Look what you did: try the small numbers in order. {said}{d} divides {n} "
            f"exactly — {n} is {d} rows of {n // d}. The smallest factor above 1 is {d}.",
            f'[[write lines="{lines}" caption="the first one that fits is {d}"]]'
            + _pair_board(d, n // d, f"{d} × {n // d} = {n}"))


def _npf_ladder(n):
    """The ladder: each rung pulls out the smallest factor. Returns (rung notes, primes)."""
    rungs, rest, done = [], n, []
    while _spf(rest) != rest:
        d = _spf(rest)
        rest //= d
        done.append(d)
        rungs.append(f"pull out {d} : " + " × ".join(str(x) for x in done + [rest]))
    return rungs, done + [rest]


def _npf_worked(p):
    n = p["a"]
    rungs, primes = _npf_ladder(n)
    chain = " × ".join(str(x) for x in primes)
    return (f"Look what you did: pull out the smallest factor and keep going until only "
            f"primes are left. {n} equals {chain} — {_plural(len(primes), 'prime')}.",
            f'[[solve start="{n}" steps="{" | ".join(rungs)}" caption="{n} = {chain}: {len(primes)} primes"]]')


def _bfac_worked(p):
    n = p["a"]
    d = _spf(n)
    q = n // d
    return (f"Look what you did: the smallest factor of {n} above 1 is {d}. Divide — {n} "
            f"divided by {d} equals {q} — and {q} is the biggest factor below {n}, because "
            f"the smallest factor is always paired with the biggest.",
            f'[[step eq="{n} = {d} × {q}"]]' + _pair_board(d, q, f"smallest {d}, biggest {q}"))


# (tc, 2026-09-05) PREALGEBRA UNIT 3'S PICTURE: THE NUMBER LINE WITH THE MOVE DRAWN AS
# HOPS. The ask marks only where you START (the old boards marked the landing point --
# the answer, drawn on the question); the walk-back draws the hop. Counting back and
# adding a negative hop LEFT past zero; taking away a negative hops RIGHT; times with a
# negative is b hops of a to the left, one after another.
def _int_range(lo, hi):
    lo, hi = min(lo, -5), max(hi, 5)
    return f'min="{lo}" max="{hi}"'


def _neg(n):
    """A negative number the way the board writes it: a real minus sign, never a hyphen."""
    return f"−{-n}" if n < 0 else str(n)


def _cbz_board(p):
    a, b = p["a"], p["b"]
    return (f'[[numberline {_int_range(a - b - 3, a + 3)} points="{a}" caption="start at {a}"]]'
            f'[[step eq="{a} − {b} = ?"]]')


def _cbz_worked(p):
    a, b = p["a"], p["b"]
    r = a - b
    return (f"Look what you did: start at {a} and hop {b} to the left. {a} steps reach "
            f"zero, and {b - a} more carry on past it. You land on negative {b - a}.",
            f'[[numberline {_int_range(r - 3, a + 3)} points="{a}" hops="{a},{r}" caption="{a} − {b} = {_neg(r)}"]]')


def _addneg_board(p):
    a, b = p["a"], p["b"]
    return (f'[[numberline {_int_range(a - b - 3, a + 3)} points="{a}" caption="start at {a}"]]'
            f'[[step eq="{a} + (−{b}) = ?"]]')


def _addneg_worked(p):
    a, b = p["a"], p["b"]
    r = a - b
    return (f"Look what you did: adding negative {b} is a hop of {b} to the left. Start at "
            f"{a}, hop {b} left — {a} steps reach zero, {b - a} more pass it — and you land "
            f"on negative {b - a}.",
            f'[[numberline {_int_range(r - 3, a + 3)} points="{a}" hops="{a},{r}" caption="{a} + (−{b}) = {_neg(r)}"]]')


def _subneg_board(p):
    a, b = p["a"], p["b"]
    return (f'[[numberline {_int_range(-5, a + b + 3)} points="{a}" caption="start at {a}"]]'
            f'[[step eq="{a} − (−{b}) = ?"]]')


def _subneg_worked(p):
    a, b = p["a"], p["b"]
    r = a + b
    return (f"Look what you did: taking away negative {b} is a hop of {b} to the RIGHT. "
            f"Start at {a}, hop {b} right, and you land on {r}. {a} take away negative {b} "
            f"equals {a} plus {b}.",
            f'[[numberline {_int_range(-5, r + 3)} points="{a}" hops="{a},{r}" caption="{a} − (−{b}) = {r}"]]')


def _mulneg_worked(p):
    a, b = p["a"], p["b"]
    r = -(a * b)
    hops = ",".join(str(-a * i) for i in range(0, b + 1))
    return (f"Look what you did: negative {a} times {b} is {b} hops of {a} to the left, "
            f"one after another, starting at zero. {a} times {b} equals {a * b}, and every "
            f"hop went left — so you land on negative {a * b}.",
            f'[[numberline {_int_range(r - 5, 5)} hops="{hops}" caption="(−{a}) × {b} = {_neg(r)}"]]')


# (td, 2026-09-06) PREALGEBRA UNITS 4-6'S PICTURES. Fractions of a number and sharing in
# a ratio on the TAPE (the whole bracketed, cut into equal parts); how-many-parts and
# fractions bigger than one on the FRACTION LINE; dividing by a fraction as HOPS of the
# fraction along the line (the measurement picture), the flip-and-times ladder when
# the hops would be too many; decimals on the HUNDRED GRID, the tenths line and the
# place-value chart's new Tenths column; a rate as sharing then groups (the array);
# a ratio as two tapes, the second scaled; a proportion as two pies cut two ways.
def _nuf_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[tape parts="{" | ".join(["?"] * b)}" total="{c}" '
            f'caption="{c} cut into {b} equal parts — take {a} of them"]]'
            f'[[step eq="{c} ÷ {b} = {c // b}"]][[step eq="{c // b} × {a} = ?"]]')


def _nuf_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    q = c // b
    return (f"Look what you did: cut {c} into {b} equal parts — {c} divided by {b} equals "
            f"{q} in each part. Take {a} of them: {q} times {a} equals {q * a}. "
            f"{_frac_words(a, b).capitalize()} of {c} is {q * a}.",
            f'[[tape parts="{" | ".join([str(q)] * b)}" total="{c}" '
            f'caption="{a} of the {b} parts: {q} × {a} = {q * a}"]]')


def _uic_board(p):
    a, b = p["a"], p["b"]
    word = _FRAC_BOTTOM.get(a, "part")
    return (f'[[tape parts="{" | ".join([str(a) + " " + word + "s"] * b)}" total="{b} wholes" '
            f'caption="each whole holds {a} {word}s — how many in all?"]]'
            f'[[step eq="{b} wholes = {b} × {a} = ?"]]')


def _uic_worked(p):
    a, b = p["a"], p["b"]
    word = _FRAC_BOTTOM.get(a, "part")
    return (f"Look what you did: each whole holds {a} {word}s, and there are {b} wholes. "
            f"{b} times {a} equals {a * b}. There are {a * b} {word}s in {b} wholes.",
            f'[[tape parts="{" | ".join([str(a)] * b)}" total="{b} wholes" '
            f'caption="{b} × {a} = {a * b} {word}s"]]')


def _dbf_hops(c, a, b):
    """The landing points of hops of a/b from 0 up to c, as decimals the line reads
    back in b-ths (the fraction line labels a hop +2/3, not +0.67)."""
    n = c * b // a
    return ",".join(str(round(i * a / b, 4)) for i in range(0, n + 1))


def _dbf_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    if c * b // a <= 8 and c * b <= 30:
        return (f'[[numberline min="0" max="{c}" denom="{b}" points="0" '
                f'caption="how many hops of {a}/{b} reach {c}?"]]'
                f'[[step eq="{c} ÷ ({a}/{b}) = ?"]]')
    # (the old board wrote the flipped form under the question -- the method, given away)
    return f'[[step eq="{c} ÷ ({a}/{b}) = ?"]]'


def _dbf_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    n = c * b // a
    if n <= 8 and c * b <= 30:
        return (f"Look what you did: dividing asks how many {_frac_words(a, b)} fit in {c}. "
                f"Hop by {_frac_words(a, b)} from zero — {n} hops reach {c} exactly. "
                f"{c} divided by {_frac_words(a, b)} equals {n}.",
                f'[[numberline min="0" max="{c}" denom="{b}" hops="{_dbf_hops(c, a, b)}" '
                f'caption="{n} hops of {a}/{b} reach {c}: {c} ÷ ({a}/{b}) = {n}"]]')
    return (f"Look what you did: flip the fraction and times. {c} divided by "
            f"{_frac_words(a, b)} is {c} times {b} over {a}: {c} times {b} equals {c * b}, "
            f"and {c * b} divided by {a} equals {n}.",
            f'[[solve start="{c} ÷ ({a}/{b})" steps="flip and times : {c} × {b}/{a} | '
            f'times the top : {c * b} ÷ {a} | divide : {n}" caption="{c} ÷ ({a}/{b}) = {n}"]]')


def _imp_board(p):
    a, b = p["a"], p["b"]
    top = a // b + 1
    den = f'denom="{b}" ' if top * b <= 30 else ""
    return (f'[[numberline min="0" max="{top}" {den}points="{round(a / b, 2)}" '
            f'caption="{a}/{b} on the line — how many whole ones does it pass?"]]'
            f'[[step eq="{a}/{b} = ? whole ones and some left"]]')


def _imp_worked(p):
    a, b = p["a"], p["b"]
    w, r = a // b, a % b
    hops = ",".join(str(i) for i in range(0, w + 1)) + f",{round(a / b, 2)}"
    word = _FRAC_BOTTOM.get(b, "part")
    return (f"Look what you did: {b} {word}s fill one whole, so hop a whole at a time. "
            f"{w} whole hops use {w * b} {word}s, and {r} {word}{'s' if r != 1 else ''} "
            f"{'are' if r != 1 else 'is'} left over. {a} {word}s is {w} whole ones and "
            f"{r} {word}{'s' if r != 1 else ''}.",
            f'[[numberline min="0" max="{w + 1}" {"denom=" + chr(34) + str(b) + chr(34) + " " if (w + 1) * b <= 30 else ""}hops="{hops}" '
            f'caption="{a}/{b} = {w} whole ones and {r}/{b}"]]')


def _hun_board(p):
    a, b = p["a"], p["b"]
    n = 10 * a + b
    return (f'[[hundredgrid shaded="{n}" ask="1" caption="0.{a}{b} shaded on the hundred grid"]]'
            f'[[step eq="0.{a}{b} = ? hundredths"]]')


def _hun_worked(p):
    a, b = p["a"], p["b"]
    n = 10 * a + b
    more = (f"and {b} more square{'s' if b != 1 else ''} on the next row. {10 * a} plus {b} "
            f"equals {n}." if b else "and no more.")
    return (f"Look what you did: {_plural(a, 'tenth')} {'are' if a != 1 else 'is'} "
            f"{_plural(a, 'full row')} — {10 * a} hundredths — {more} 0 point {a}{b} is {n} "
            f"hundredths.",
            f'[[hundredgrid shaded="{n}" eq="0.{a}{b} = {n} hundredths" '
            f'caption="{a} full rows{" and " + str(b) + " more" if b else ""}: {n} hundredths"]]')


def _x10_board(p):
    a, b = p["a"], p["b"]
    return (f'[[placevalue o="{a}" d="{b}" caption="{a}.{b} on the chart — times 10, every digit moves one place left"]]'
            f'[[step eq="{a}.{b} × 10 = ?"]]')


def _x10_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: times 10 moves every digit one place to the left. The "
            f"{_plural(b, 'tenth')} became {_plural(b, 'one')}, and the {_plural(a, 'one')} "
            f"became {_plural(a, 'ten')}. {a} point {b} times 10 equals {10 * a + b}.",
            f'[[placevalue t="{a}" o="{b}" d="0" caption="{a}.{b} × 10 = {10 * a + b}: every digit one place left"]]')


def _dth_board(p):
    a, b = p["a"], p["b"]
    n = a * b
    top = max(1, (n + 9) // 10)
    if n <= 30:
        pic = (f'[[numberline min="0" max="{top}" denom="10" points="0" '
               f'caption="{b} hops of {a} tenths — where do they land?"]]')
    else:
        pic = (f'[[array rows="{b}" cols="{a}" view="groups" ask="1" label="tenths" '
               f'caption="{b} groups of {a} tenths"]]')
    return pic + f'[[step eq="0.{a} = {a} tenths"]][[step eq="{a} tenths × {b} = ? tenths"]]'


def _dth_worked(p):
    a, b = p["a"], p["b"]
    n = a * b
    top = max(1, (n + 9) // 10)
    hops = ",".join(str(round(i * a / 10, 1)) for i in range(0, b + 1))
    if n <= 30:
        pic = (f'[[numberline min="0" max="{top}" denom="10" hops="{hops}" '
               f'caption="{b} hops of {a} tenths = {n} tenths"]]')
    else:
        pic = (f'[[array rows="{b}" cols="{a}" view="groups" eq="{a} × {b} = {n}" label="tenths" '
               f'caption="{b} groups of {a} tenths = {n} tenths"]]')
    return (f"Look what you did: 0 point {a} is {a} tenths, and {b} lots of {a} tenths are "
            f"{n} tenths. {a} times {b} equals {n}, and the parts stay tenths — {n} tenths.",
            pic)


def _dsh_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    n = 10 * a + b
    q = n // c
    if n <= 60 and q <= 12:
        pic = (f'[[array total="{n}" rows="{c}" ask="1" label="tenths" '
               f'caption="{n} tenths shared into {c} equal groups"]]')
    else:   # too many dots to draw: the tape cut into c parts, the shares hidden
        pic = (f'[[tape parts="{" | ".join(["?"] * c)}" total="{n} tenths" '
               f'caption="{n} tenths shared into {c} equal parts"]]')
    return pic + f'[[step eq="{a}.{b} = {n} tenths"]][[step eq="{n} ÷ {c} = ? tenths"]]'


def _dsh_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    n = 10 * a + b
    q = n // c
    if n <= 60 and q <= 12:
        pic = (f'[[array rows="{c}" cols="{q}" view="groups" eq="{n} ÷ {c} = {q}" label="tenths" '
               f'caption="{n} tenths shared {c} ways: {q} tenths each"]]')
    else:
        pic = (f'[[tape parts="{" | ".join([str(q)] * c)}" total="{n} tenths" '
               f'caption="{n} tenths shared {c} ways: {q} tenths each"]]')
    return (f"Look what you did: {a} point {b} is {n} tenths. Share {n} tenths into {c} equal "
            f"groups — {q} tenths in each. {n} divided by {c} equals {q}, so each share is "
            f"{q} tenths.",
            pic)


def _rat_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[tape parts="{a} | {b}" caption="flour {a} : milk {b} — one batch"]]'
            f'[[step eq="{a} : {b}"]][[step eq="{c} ÷ {a} = {c // a} batches"]]'
            f'[[step eq="{c // a} × {b} = ?"]]')


def _rat_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    k = c // a
    return (f"Look what you did: {c} cups of flour is {k} batches, because {c} divided by "
            f"{a} equals {k}. The milk grows the same way — {k} batches of {b} cups: {k} "
            f"times {b} equals {k * b}. Both sides were timesed by {k}.",
            f'[[tape parts="{a} | {b}" caption="one batch: {a} : {b}"]]'
            f'[[tape parts="{c} | {k * b}" caption="{k} batches: {c} : {k * b} — both sides times {k}"]]')


def _rte_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[array total="{c}" rows="{b}" ask="1" label="hours" '
            f'caption="{c} bottles over {b} hours — how many in one hour?"]]'
            f'[[step eq="{c} ÷ {b} = {c // b} per hour"]][[step eq="{c // b} × {a} = ?"]]')


def _rte_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    r = c // b
    return (f"Look what you did: one hour first — {c} bottles over {b} hours is {r} an hour, "
            f"because {c} divided by {b} equals {r}. Then {a} hours of that: {r} times {a} "
            f"equals {r * a}.",
            f'[[array rows="{b}" cols="{r}" view="groups" eq="{c} ÷ {b} = {r}" label="hours" '
            f'caption="{r} bottles an hour"]]'
            f'[[array rows="{a}" cols="{r}" view="groups" eq="{r} × {a} = {r * a}" label="hours" '
            f'caption="{a} hours: {r * a} bottles"]]')


def _prop_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    if b <= 12 and c <= 12:
        return (f'[[pie parts="{b}" shaded="{a}" caption="{a}/{b}"]]'
                f'[[pie parts="{c}" shaded="0" caption="cut into {c}: how many is the same amount?"]]'
                f'[[step eq="{a}/{b} = ?/{c}"]]')
    return (f'[[step eq="{a}/{b} = ?/{c}"]]'
            f'[[step eq="{b} × ? = {c}"]]')


def _prop_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    n = a * c // b
    if b <= 12 and c <= 12 and c % b == 0:
        k = c // b
        return (f"Look what you did: the bottom was timesed by {k} — {b} times {k} equals {c} "
                f"— so the top is timesed by {k} too: {a} times {k} equals {n}. Both pies hold "
                f"the same amount, cut two ways.",
                f'[[pie parts="{b}" shaded="{a}" caption="{a}/{b}"]]'
                f'[[pie parts="{c}" shaded="{n}" caption="{n}/{c} — the same amount"]]')
    if c % b == 0:
        k = c // b
        return (f"Look what you did: the bottom was timesed by {k} — {b} times {k} equals {c} "
                f"— so the top is timesed by {k} too: {a} times {k} equals {n}.",
                f'[[solve start="{a}/{b} = ?/{c}" steps="the bottom : {b} × {k} = {c} | '
                f'so the top : {a} × {k} = {n}" caption="{a}/{b} = {n}/{c}"]]')
    return (f"Look what you did: {c} is not a whole number of {b}s, so go through 1 — times "
            f"the top by {c} and divide by {b}: {a} times {c} equals {a * c}, and {a * c} "
            f"divided by {b} equals {n}.",
            f'[[solve start="{a}/{b} = ?/{c}" steps="times the top by {c} : {a * c} ÷ {b} | '
            f'divide : {n}" caption="{a}/{b} = {n}/{c}"]]')


def _shr_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    n = a + b
    return (f'[[tape parts="{" | ".join(["?"] * n)}" total="{c}" '
            f'caption="{c} cut into {a} + {b} = {n} equal parts"]]'
            f'[[step eq="{c} ÷ {n} = {c // n} each part"]][[step eq="{c // n} × {a} = ?"]]')


def _shr_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    n = a + b
    q = c // n
    return (f"Look what you did: count the parts first — {a} and {b} are {n} parts. {c} "
            f"divided by {n} equals {q} in each part. The first share is {a} parts: {q} "
            f"times {a} equals {q * a}. And {q * a} plus {q * b} puts the {c} back together.",
            f'[[tape parts="{q * a} | {q * b}" total="{c}" '
            f'caption="{a} parts : {b} parts = {q * a} : {q * b}"]]')


# ---- (te, 2026-09-06) PREALGEBRA UNITS 7-9: percent on the tape, geometry on its own
# figures, the first letters as bars. Every ask draws its question with the answer
# withheld; every walk-back draws the same picture filled in.
def _ten_tape(b, total=None, caption=""):
    """A bar cut into ten equal parts of b/10 -- ten percent each."""
    part = b // 10
    return (f'[[tape parts="{" | ".join([str(part)] * 10)}" total="{total if total is not None else b}" '
            f'caption="{caption}"]]')


def _pcn_board(p):
    a, b = p["a"], p["b"]
    return (f'[[tape parts="{" | ".join(["?"] * 10)}" total="{b}" '
            f'caption="{b} cut into ten equal parts — 10% is one part"]]'
            f'[[step eq="10% of {b} = {b // 10}"]]'
            f'[[step eq="{a}% is {a // 10} tens"]]'
            f'[[step eq="{a}% of {b} = ?"]]')


def _pcn_worked(p):
    a, b = p["a"], p["b"]
    n, part, ans = a // 10, b // 10, a * b // 100
    return (f"Look what you did: ten percent of {b} is {part} — one of the ten parts. "
            f"{a} percent is {n} of those parts: {n} times {part} equals {ans}.",
            _ten_tape(b, caption=f"ten parts of {part} — 10% each")
            + f'[[tape parts="{ans} | {b - ans}" total="{b}" caption="{n} parts: {a}% of {b} = {ans}"]]')


def _asp_board(p):
    a, b = p["a"], p["b"]
    pic = (f'[[tape parts="{a} | {b - a}" total="{b}" caption="{a} out of {b}"]]'
           f'[[hundredgrid shaded="0" ask="1" unit="percent" '
           f'caption="the same share out of 100 — how many?"]]'
           f'[[step eq="{a}/{b} = ?/100"]]')
    if 100 % b == 0:
        k = 100 // b
        return pic + f'[[step eq="{b} × {k} = 100"]][[step eq="{a} × {k} = ?"]]'
    return pic + f'[[step eq="{a} × 100 ÷ {b} = ?"]]'


def _asp_worked(p):
    a, b = p["a"], p["b"]
    ans = a * 100 // b
    pic = (f'[[tape parts="{a} | {b - a}" total="{b}" caption="{a} out of {b}"]]'
           f'[[hundredgrid shaded="{ans}" unit="percent" '
           f'caption="{ans} out of 100 — the same share"]]')
    if 100 % b == 0:
        k = 100 // b
        return (f"Look what you did: the bottom went from {b} to 100 — timesed by {k} — so "
                f"the top is timesed by {k} too: {a} times {k} equals {ans}. {a} out of {b} "
                f"is {ans} percent.", pic)
    return (f"Look what you did: 100 is not a whole number of {b}s, so go through 1 — {a} "
            f"times 100 equals {a * 100}, and {a * 100} divided by {b} equals {ans}. {a} out "
            f"of {b} is {ans} percent.", pic)


def _pwh_board(p):
    a, b = p["a"], p["b"]
    n, part = a // 10, b // (a // 10)
    return (f'[[tape parts="{b} | ?" total="?" caption="{b} is {a}% — the whole is the question"]]'
            f'[[step eq="10% = {b} ÷ {n} = {part}"]]'
            f'[[step eq="{b} is {a}% of ?"]]')


def _pwh_worked(p):
    a, b = p["a"], p["b"]
    n, part, whole = a // 10, b // (a // 10), b * 100 // a
    return (f"Look what you did: {a} percent is {n} tens, so ten percent is {b} divided by "
            f"{n}, which equals {part}. The whole is ten of those: {part} times 10 equals "
            f"{whole}. And {whole} is bigger than {b}, as the whole has to be.",
            _ten_tape(whole, caption=f"ten parts of {part} — {n} of them are the {b}, all ten are {whole}")
            + f'[[tape parts="{b} | {whole - b}" total="{whole}" caption="{a}% of {whole} = {b}"]]')


def _pup_board(p):
    a, b, up = p["a"], p["b"], bool(p.get("c"))
    ch = a * b // 100
    pic = (f'[[tape parts="{b} | {ch}" total="?" caption="the price and the change put on"]]' if up
           else f'[[tape parts="? | {ch}" total="{b}" caption="the price with the change taken off"]]')
    return (pic + f'[[step eq="10% of {b} = {b // 10}"]]'
            + (f'[[step eq="{a}% = {ch}"]]' if a != 10 else "")
            + f'[[step eq="{b} {"+" if up else "−"} {ch} = ?"]]')


def _pup_worked(p):
    a, b, up = p["a"], p["b"], bool(p.get("c"))
    ch = a * b // 100
    new = b + ch if up else b - ch
    if up:
        return (f"Look what you did: {a} percent of {b} is {ch} dollars — that is the change, "
                f"not {a}. The price goes up, so put it on: {b} plus {ch} equals {new} dollars.",
                f'[[tape parts="{b} | {ch}" total="{new}" caption="{b} + {ch} = {new} dollars"]]')
    return (f"Look what you did: {a} percent of {b} is {ch} dollars — that is the change, "
            f"not {a}. The price goes down, so take it off: {b} take away {ch} equals {new} "
            f"dollars.",
            f'[[tape parts="{new} | {ch}" total="{b}" caption="{b} − {ch} = {new} dollars"]]')


_CNV_UNITS = {10: ("centimetre", "1 cm = 10 mm", "centimetres", "millimetres"),
              100: ("metre", "1 m = 100 cm", "metres", "centimetres"),
              1000: ("kilogram", "1 kg = 1000 g", "kilograms", "grams")}


def _cnv_board(p):
    a, b = p["a"], p["b"]
    big, fact, bigs, smalls = _CNV_UNITS[b]
    return (f'[[tape parts="{" | ".join([str(b)] * a)}" total="?" '
            f'caption="{a} {bigs} — {b} {smalls} in each"]]'
            f'[[step eq="{fact}"]][[step eq="{a} × {b} = ?"]]')


def _cnv_worked(p):
    a, b = p["a"], p["b"]
    big, fact, bigs, smalls = _CNV_UNITS[b]
    return (f"Look what you did: one {big} is {b} {smalls}, so {a} {bigs} are {a} lots of "
            f"{b}. {a} times {b} equals {a * b} {smalls}.",
            f'[[tape parts="{" | ".join([str(b)] * a)}" total="{a * b}" '
            f'caption="{a} × {b} = {a * b} {smalls}"]]')


def _tri_board(p):
    a, b = p["a"], p["b"]
    return (f'[[rectangle w="{a}" h="{b}" half="1" ask="1" '
            f'caption="base {a}, height {b} — the triangle is half the rectangle round it"]]'
            f'[[step eq="the rectangle round it: {a} × {b} = {a * b}"]]'
            f'[[step eq="the triangle is half: {a} × {b} ÷ 2 = ?"]]')


def _tri_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: the rectangle round the triangle is {a} times {b}, which "
            f"equals {a * b} squares. The triangle is half of it — the diagonal cuts the "
            f"rectangle into two of them — and half of {a * b} is {a * b // 2}.",
            f'[[rectangle w="{a}" h="{b}" half="1" caption="{a} × {b} = {a * b} · half is {a * b // 2}"]]')


def _sla_board(p):
    a = p["a"]
    return (f'[[angle deg="180" split="{a}" caption="a straight line — {a}° and the rest"]]'
            f'[[step eq="180° − {a}° = ?"]]')


def _sla_worked(p):
    a = p["a"]
    return (f"Look what you did: the two angles together fill the straight line, and a "
            f"straight line is 180 degrees. 180 take away {a} equals {180 - a}, and {a} "
            f"plus {180 - a} puts the 180 back.",
            f'[[angle deg="180" split="{a},{180 - a}" caption="{a}° + {180 - a}° = 180°"]]')


def _tri3_board(p):
    a, b = p["a"], p["b"]
    right = ' right="A"' if a == 90 else ' right="B"' if b == 90 else ""
    return (f'[[triangle v="A,B,C"{right} angles="{a},{b}," '
            f'caption="angles {a}° and {b}° — the third is forced"]]'
            f'[[step eq="{a}° + {b}° = {a + b}°"]]'
            f'[[step eq="180° − ({a}° + {b}°) = ?"]]')


def _tri3_worked(p):
    a, b = p["a"], p["b"]
    c = 180 - a - b
    right = ' right="A"' if a == 90 else ' right="B"' if b == 90 else ' right="C"' if c == 90 else ""
    return (f"Look what you did: the two you were given come to {a} plus {b}, which equals "
            f"{a + b}. The three angles of any triangle come to 180, so the third is 180 take "
            f"away {a + b}, which equals {c}.",
            f'[[triangle v="A,B,C"{right} angles="{a},{b},{c}" '
            f'caption="{a}° + {b}° + {c}° = 180°"]]')


def _evx_board(p):
    a, b = p["a"], p["b"]
    return (f'[[step eq="x = {a}"]]'
            f'[[tape parts="x | {b}" total="?" caption="x + {b}, with x holding {a}"]]'
            f'[[step eq="x + {b} = {a} + {b} = ?"]]')


def _evx_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: x is holding {a}, so swap the letter for its number. x plus "
            f"{b} becomes {a} plus {b}, which equals {a + b} — a sum, not two digits side "
            f"by side.",
            f'[[tape parts="{a} | {b}" total="{a + b}" caption="x + {b} = {a} + {b} = {a + b}"]]')


def _mlx_board(p):
    a, b = p["a"], p["b"]
    return (f'[[step eq="x = {a}"]]'
            f'[[tape parts="{" | ".join(["x"] * b)}" total="?" caption="{b}x — {b} copies of x"]]'
            f'[[step eq="{b}x = {b} × {a} = ?"]]')


def _mlx_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: {b} x means {b} times x — {b} copies of it, not {b} beside "
            f"it. With x holding {a}, that is {b} times {a}, which equals {a * b}.",
            f'[[tape parts="{" | ".join([str(a)] * b)}" total="{a * b}" '
            f'caption="{b}x = {b} × {a} = {a * b}"]]')


def _clt_tape(a, b, total):
    """ax + bx as one bar: an x per part while it fits ten parts, else the two
    counts as two proportional parts."""
    if a + b <= 10:
        return f'[[tape parts="{" | ".join(["x"] * (a + b))}" total="{total}" '
    return f'[[tape parts="{a}x | {b}x" total="{total}" '


def _clt_board(p):
    a, b = p["a"], p["b"]
    xs = "x's"
    return (_clt_tape(a, b, "?") + f'caption="{a} {xs} and {b} more {xs} — how many {xs}?"]]'
            f'[[step eq="{a}x + {b}x"]]'
            f'[[step eq="{a} of them + {b} of them = ? of them"]]')


def _clt_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: {a} of them and {b} more of them — count them, do not times "
            f"them. {a} plus {b} equals {a + b}, so {a} x plus {b} x equals {a + b} x, "
            f"whatever x is holding.",
            _clt_tape(a, b, f"{a + b}x") + f'caption="{a}x + {b}x = {a + b}x"]]')


def _dst_board(p):
    a, b = p["a"], p["b"]
    return (f'[[areamodel rows="{a}" cols="x,{b}" ask="1" '
            f'caption="{a} tall, x + {b} wide — read the two rooms"]]'
            f'[[step eq="{a}(x + {b}) = {a}x + ?"]]')


def _dst_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: the {a} reaches both rooms. One room is {a} times x — {a} x. "
            f"The other is {a} times {b}, which equals {a * b}. Both rooms together: {a} x "
            f"plus {a * b}.",
            f'[[areamodel rows="{a}" cols="x,{b}" caption="{a}(x + {b}) = {a}x + {a * b}"]]')



# ---- (tf, 2026-09-06) ALGEBRA 1 UNITS 1-3: letters as bars, the balance, the machine.
# Every ask draws its question with the answer withheld; every walk-back draws the
# same picture filled in.
def _ev2_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[step eq="x = {a}"]]'
            f'[[tape parts="{" | ".join(["x"] * b)} | {c}" total="?" '
            f'caption="{b}x + {c} — {b} copies of x, then {c}"]]'
            f'[[step eq="{b}x + {c} = {b} × {a} + {c} = ?"]]')


def _ev2_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: times first — {b} x is {b} copies of {a}, and {b} times {a} "
            f"equals {a * b}. Then the add: {a * b} plus {c} equals {a * b + c}. The plus "
            f"waited its turn.",
            f'[[tape parts="{" | ".join([str(a)] * b)} | {c}" total="{a * b + c}" '
            f'caption="{b}x + {c} = {a * b} + {c} = {a * b + c}"]]')


def _evxy_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[step eq="x = {a} · y = {b}"]]'
            f'[[tape parts="x | {" | ".join(["y"] * c)}" total="?" '
            f'caption="x + {c}y — one x, then {c} copies of y"]]'
            f'[[step eq="x + {c}y = {a} + {c} × {b} = ?"]]')


def _evxy_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: each letter kept its own number. {c} y is {c} copies of "
            f"{b}, which is {b * c}. Then x plus that: {a} plus {b * c} equals {a + b * c}. "
            f"The {c} belonged to the y and never touched the x.",
            f'[[tape parts="{a} | {" | ".join([str(b)] * c)}" total="{a + b * c}" '
            f'caption="x + {c}y = {a} + {b * c} = {a + b * c}"]]')


def _cl2_tape(a, b, c, total):
    """ax + by + cx as one bar in the order written: an x per part while it fits
    ten parts, else the three counts as three proportional parts."""
    if a + b + c <= 10:
        parts = ["x"] * a + ["y"] * b + ["x"] * c
        return f'[[tape parts="{" | ".join(parts)}" total="{total}" '
    return f'[[tape parts="{a}x | {b}y | {c}x" total="{total}" '


def _cl2_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (_cl2_tape(a, b, c, "?") + f'caption="{a}x + {b}y + {c}x — count only the x parts"]]'
            f'[[step eq="{a}x + {b}y + {c}x"]]'
            f'[[step eq="the x\'s: {a} + {c} = ? · the y walks past"]]')


def _cl2_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: only the same letter collects. The x parts are {a} and "
            f"{c}, and {a} plus {c} equals {a + c} — so {a + c} x. The {b} y is a different "
            f"thing; it walked past and stayed as it was. {a + c} x plus {b} y.",
            f'[[tape parts="{a + c}x | {b}y" caption="the x\'s collected: {a + c}x + {b}y"]]')


def _dstm_board(p):
    a, b = p["a"], p["b"]
    return (f'[[areamodel rows="{a}" cols="x,-{b}" ask="1" '
            f'caption="{a} tall, x − {b} wide — the second room is taken away"]]'
            f'[[step eq="{a}(x − {b}) = {a}x − ?"]]')


def _dstm_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: the {a} reaches both rooms, minus and all. One room is {a} "
            f"times x — {a} x. The other is {a} times {b}, which equals {a * b}, and that "
            f"room is taken away. So it is {a} x take away {a * b} — not {b}.",
            f'[[areamodel rows="{a}" cols="x,-{b}" caption="{a}(x − {b}) = {a}x − {a * b}"]]')


def _un1_board(p):
    a, b = p["a"], p["b"]
    return (f'[[balance left="x + {a}" right="{b}" caption="take {a} off BOTH sides"]]'
            f'[[step eq="x = {b} − {a} = ?"]]')


def _un1_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: {a} came off both sides, so the scale stayed level. {b} "
            f"take away {a} equals {b - a}, and x is holding {b - a}. Put it back to check: "
            f"{b - a} plus {a} equals {b}. Level.",
            f'[[balance left="x" right="{b - a}" caption="{a} off both sides: x = {b - a}"]]'
            f'[[step eq="{b - a} + {a} = {b} ✓"]]')


def _un2_board(p):
    a, b = p["a"], p["b"]
    return (f'[[balance left="{a}x" right="{b}" caption="share BOTH sides between {a}"]]'
            f'[[tape parts="{" | ".join(["x"] * a)}" total="{b}" '
            f'caption="{a} copies of x weigh {b} — how much is one?"]]'
            f'[[step eq="x = {b} ÷ {a} = ?"]]')


def _un2_worked(p):
    a, b = p["a"], p["b"]
    q = b // a
    return (f"Look what you did: {a} copies of x weigh {b}, so one x is {b} shared between "
            f"{a}, which equals {q}. Nothing was added, so nothing was taken away — the undo "
            f"of a times is a share. Check: {a} times {q} equals {b}. Level.",
            f'[[balance left="x" right="{q}" caption="shared between {a}: x = {q}"]]'
            f'[[tape parts="{" | ".join([str(q)] * a)}" total="{b}" caption="{a} × {q} = {b} ✓"]]')


def _un3_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[balance left="{a}x + {b}" right="{c}" caption="the {b} went on last — it comes off first"]]'
            f'[[step eq="take {b} off both sides: {a}x = {c - b}"]]'
            f'[[step eq="x = {c - b} ÷ {a} = ?"]]')


def _un3_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    m = c - b
    q = m // a
    return (f"Look what you did: two undos, last on first off. The {b} came off both sides: "
            f"{a} x equals {m}. Then the share: {m} shared between {a} equals {q}. Check: "
            f"{a} times {q} is {a * q}, plus {b} is {c}. Level.",
            f'[[balance left="{a}x" right="{m}" caption="{b} off both sides"]]'
            f'[[balance left="x" right="{q}" caption="shared between {a}: x = {q}"]]')


def _ineq_board(p):
    a, b = p["a"], p["b"]
    n = b - a
    return (f'[[step eq="x + {a} < {b}"]]'
            f'[[step eq="x < {b} − {a}"]]'
            f'[[numberline min="0" max="{n + 2}" ineq="x<{n}" '
            f'caption="everything to the left of {n} — the circle is open, {n} is shut out"]]')


def _ineq_worked(p):
    a, b = p["a"], p["b"]
    n = b - a
    return (f"Look what you did: take {a} off both sides and x is less than {n}. Less than "
            f"shuts the door on {n} itself — {n} plus {a} is {b}, not under {b}. The biggest "
            f"whole number under {n} is {n - 1}: {n - 1} plus {a} equals {n - 1 + a}, and "
            f"that is under {b}.",
            f'[[numberline min="0" max="{n + 2}" ineq="x<{n}" points="{n - 1}" '
            f'caption="x < {n} — the biggest whole number is {n - 1}"]]'
            f'[[step eq="{n - 1} + {a} = {n - 1 + a} < {b} ✓"]]')


def _fm1_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[machine input="{c}" rule="{a}x + {b}" output="?" '
            f'caption="in {c} — times by {a}, then add {b} — out ?"]]')


def _fm1_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: {c} went in and the rule ran in order. Times by {a} first: "
            f"{a} times {c} equals {a * c}. Then add {b}: {a * c} plus {b} equals "
            f"{a * c + b}. Out came {a * c + b}.",
            f'[[machine input="{c}" rule="{a}x + {b}" output="{a * c + b}" '
            f'caption="in {c}, out {a * c + b}"]]'
            f'[[step eq="{a} × {c} = {a * c}"]][[step eq="{a * c} + {b} = {a * c + b}"]]')


def _fnot_board(p):
    a, b = p["a"], p["b"]
    return (f'[[machine input="{b}" rule="x + {a}" output="?" fname="f" '
            f'caption="f of {b} — feed machine f the number {b}"]]'
            f'[[step eq="f({b}) = {b} + {a} = ?"]]')


def _fnot_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: f of {b} means feed the machine {b} — nothing is timesed. "
            f"{b} plus {a} equals {a + b}, so f of {b} equals {a + b}.",
            f'[[machine input="{b}" rule="x + {a}" output="{a + b}" fname="f" '
            f'caption="f({b}) = {b} + {a} = {a + b}"]]')


def _fm2_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[machine input="{c}" rule="x + {a}" output="{c + a}" '
            f'caption="machine one: in {c}, out {c + a}"]]'
            f'[[machine input="{c + a}" rule="{b}x" output="?" fname="g" '
            f'caption="machine two: in {c + a} — times by {b} — out ?"]]')


def _fm2_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    m = c + a
    return (f"Look what you did: first machine first. {c} plus {a} equals {m}, and that {m} "
            f"went straight into machine two: {m} times {b} equals {m * b}. Add first, then "
            f"times — because that is the order the machines stand in.",
            f'[[machine input="{c}" rule="x + {a}" output="{m}" caption="in {c}, out {m}"]]'
            f'[[machine input="{m}" rule="{b}x" output="{m * b}" fname="g" '
            f'caption="in {m}, out {m * b}"]]')


def _fback_board(p):
    a, b = p["a"], p["b"]
    return (f'[[machine input="?" rule="x + {a}" output="{b}" fname="f" '
            f'caption="in ?, out {b} — run it backwards"]]'
            f'[[step eq="? + {a} = {b}"]]')


def _fback_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: the machine added {a} and put out {b}, so undo the add — "
            f"{b} take away {a} equals {b - a}. The input was {b - a}. Run it forwards to "
            f"check: {b - a} plus {a} equals {b}. It fits.",
            f'[[machine input="{b - a}" rule="x + {a}" output="{b}" fname="f" '
            f'caption="f({b - a}) = {b} ✓"]]')



# ---- (tg, 2026-09-06) ALGEBRA 1 UNITS 4-6: the line on the grid, two rules as bars
# and two lines, powers as counted copies, the place-value chart, the doubling bars.
# Every ask draws its question with the answer withheld; every walk-back draws the
# same picture filled in.
def _line_spec(m, b):
    """y = mx + b written the way the grapher reads it: y=2x-1, y=2x, y=x+3."""
    mm = "" if m == 1 else str(m)
    if b == 0:
        return f"y={mm}x"
    return f"y={mm}x{'+' if b > 0 else '-'}{abs(b)}"


def _lny_board(p):
    a, b = p["a"], p["b"]
    return (f'[[graph lines="y=x+{a}; x={b}" range="0..{b + a + 2}" '
            f'caption="y = x + {a} — climb from x = {b} up to the line: how high?"]]'
            f'[[step eq="x = {b}"]][[step eq="y = {b} + {a} = ?"]]')


def _lny_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: find {b} along the bottom, climb straight up to the line, and "
            f"read the height — {b} plus {a} equals {b + a}. The point is {b} comma {b + a}: the "
            f"x you were given, standing under the y you found.",
            f'[[graph lines="y=x+{a}" points="({b},{b + a})" range="0..{b + a + 2}" '
            f'caption="y = x + {a} — the point ({b}, {b + a}): x = {b}, y = {b + a}"]]')


def _slp_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[graph points="({b},{c}),({b + 1},{c + a})" range="0..{b + 3}" '
            f'caption="from ({b}, {c}) to ({b + 1}, {c + a}) — one step right: how far up?"]]'
            f'[[step eq="climb = {c + a} − {c} = ?"]]')


def _slp_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: x stepped once, from {b} to {b + 1}, and y climbed from {c} "
            f"to {c + a} — a climb of {a}, because {c + a} take away {c} equals {a}. That "
            f"climb per step is the slope, and it is {a} all the way along the line.",
            f'[[graph lines="{_line_spec(a, c - a * b)}" points="({b},{c}),({b + 1},{c + a})" '
            f'range="0..{b + 3}" caption="one step right, {a} up — slope {a}"]]'
            f'[[step eq="slope = {c + a} − {c} = {a}"]]')


def _yint_board(p):
    a, b = p["a"], p["b"]
    return (f'[[graph lines="y={a}x+{b}" range="0..5" '
            f'caption="y = {a}x + {b} — where does it stand at the left wall, x = 0?"]]'
            f'[[step eq="x = 0"]][[step eq="y = {a} × 0 + {b} = ?"]]')


def _yint_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: at x equals zero, {a} times zero is zero — the whole times "
            f"part vanishes — and all that is left is the plus {b}. The line starts at height "
            f"{b} and does its climbing from there.",
            f'[[graph lines="y={a}x+{b}" points="(0,{b})" range="0..5" '
            f'caption="at x = 0 the line stands at {b}"]]'
            f'[[step eq="y = {a} × 0 + {b} = {b}"]]')


def _lin2_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[graph lines="y={a}x+{b}; x={c}" range="0..{c + 2}" '
            f'caption="y = {a}x + {b} — climb from x = {c} up to the line: how high?"]]'
            f'[[step eq="y = {a} × {c} + {b} = ?"]]')


def _lin2_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: start at {b}, then climb {a} for each of the {c} steps — {a} "
            f"times {c} equals {a * c} of climbing. {a * c} plus {b} equals {a * c + b}. The "
            f"line stands at height {a * c + b} over x equals {c}.",
            f'[[graph lines="y={a}x+{b}" points="({c},{a * c + b})" range="0..{c + 2}" '
            f'caption="the point ({c}, {a * c + b}) — start {b}, climb {a} × {c}"]]'
            f'[[step eq="y = {a} × {c} + {b} = {a * c + b}"]]')


def _sys1_board(p):
    a, b = p["a"], p["b"]
    x0 = a // (b - 1)
    return (f'[[graph lines="y=x+{a}; y={b}x" cross="ask" range="0..{x0 + 3}" '
            f'caption="two rules on one grid — they cross once: at which x?"]]'
            f'[[step eq="x + {a} = {b}x"]]')


def _sys1_worked(p):
    a, b = p["a"], p["b"]
    x0 = a // (b - 1)
    y0 = b * x0
    return (f"Look what you did: the lines cross once, and at the crossing both rules give the "
            f"same y. At x equals {x0}, the first rule says {x0} plus {a}, which is {y0}, and "
            f"the second says {b} times {x0}, which is {y0}. They agree — and the x asked for "
            f"is {x0}, not the height {y0}.",
            f'[[graph lines="y=x+{a}; y={b}x" range="0..{x0 + 3}" '
            f'caption="they cross at ({x0}, {y0}) — the x is {x0}"]]'
            f'[[step eq="x + {a} = {b}x at x = {x0}"]]')


def _sys2_board(p):
    a, b = p["a"], p["b"]
    return (f'[[tape parts="x | x | {a}" total="{b}" '
            f'caption="x + y = {b}, and y is x + {a} — two x\'s and the {a}"]]'
            f'[[step eq="x + y = {b}"]]'
            f'[[step eq="swap y in: x + (x + {a}) = {b}"]]'
            f'[[step eq="2x + {a} = {b}"]][[step eq="x = ?"]]')


def _sys2_worked(p):
    a, b = p["a"], p["b"]
    x0 = (b - a) // 2
    return (f"Look what you did: swap y for what it equals and the bar holds two x's and a {a}. "
            f"Take the {a} off: two x's are {b - a}, so one x is {x0}. And y is {x0} plus {a}, "
            f"which is {x0 + a} — the OTHER letter. Check: {x0} plus {x0 + a} equals {b}.",
            f'[[tape parts="{x0} | {x0} | {a}" total="{b}" caption="x = {x0} · y = {x0 + a} · {x0} + {x0 + a} = {b}"]]')


def _sumd_board(p):
    a, b = p["a"], p["b"]
    return (f'[[tape parts="bigger | smaller" total="{a}" caption="together {a}"]]'
            f'[[tape parts="smaller | {b}" caption="the bigger is the smaller and {b} more"]]'
            f'[[step eq="bigger + smaller = {a}"]]'
            f'[[step eq="bigger − smaller = {b}"]]'
            f'[[step eq="bigger = ({a} + {b}) ÷ 2 = ?"]]')


def _sumd_worked(p):
    a, b = p["a"], p["b"]
    big = (a + b) // 2
    small = (a - b) // 2
    return (f"Look what you did: add the two clues and the smaller cancels itself away — two "
            f"bigs equal {a} plus {b}, which is {a + b}, so the bigger is {big}. The smaller "
            f"is what is left: {small}. Check both: {big} plus {small} is {a}, and {big} take "
            f"away {small} is {b}.",
            f'[[tape parts="{big} | {small}" total="{a}" caption="{big} + {small} = {a} · {big} − {small} = {b}"]]')


def _elim_board(p):
    a, b = p["a"], p["b"]
    return (f'[[tape parts="pencil | pencil | eraser" total="{a}" caption="trip one: {a} cents"]]'
            f'[[tape parts="pencil | eraser" total="{b}" caption="trip two: {b} cents — the difference is one pencil"]]'
            f'[[step eq="2 pencils + eraser = {a}"]]'
            f'[[step eq="1 pencil + eraser = {b}"]]'
            f'[[step eq="take the second away: 1 pencil = {a} − {b} = ?"]]')


def _elim_worked(p):
    a, b = p["a"], p["b"]
    pen = a - b
    er = b - pen
    return (f"Look what you did: take trip two away from trip one. The eraser is in both, so "
            f"it vanishes, and one pencil is left over against {a} take away {b} — {pen} "
            f"cents. The eraser is {b} take away {pen}, which is {er} — the other unknown, "
            f"not yours.",
            f'[[tape parts="{pen} | {pen} | {er}" total="{a}" caption="pencil {pen} · pencil {pen} · eraser {er} = {a}"]]'
            f'[[tape parts="{pen} | {er}" total="{b}" caption="{pen} + {er} = {b}"]]')


def _exadd_board(p):
    a, b = p["a"], p["b"]
    return (f'[[tape parts="{" | ".join(["x"] * (a + b))}" '
            f'caption="x{_sup(a)} · x{_sup(b)} written out — {a} x\'s, then {b} more: count them"]]'
            f'[[step eq="x{_sup(a)} · x{_sup(b)}"]]'
            f'[[step eq="({" · ".join(["x"] * a)}) · ({" · ".join(["x"] * b)})"]]'
            f'[[step eq="{a} + {b} = ? x\'s"]]')


def _exadd_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: {a} x's joined by {b} more x's — count them on the page, and "
            f"there are {a + b}. Two piles joined, so the counts ADD: x to the power {a + b}.",
            f'[[tape parts="{" | ".join(["x"] * (a + b))}" total="x{_sup(a + b)}" '
            f'caption="{a} + {b} = {a + b} x\'s — x{_sup(a + b)}"]]')


def _exmul_board(p):
    a, b = p["a"], p["b"]
    return (f'[[tape parts="{" | ".join(["x" + _sup(a)] * b)}" '
            f'caption="{b} copies of x{_sup(a)} — {b} groups of {a} x\'s"]]'
            f'[[step eq="(x{_sup(a)}){_sup(b)}"]]'
            f'[[step eq="{b} copies of {a} x\'s"]]'
            f'[[step eq="{a} × {b} = ? x\'s"]]')


def _exmul_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: {b} copies of the whole thing, and each copy is {a} x's — "
            f"{b} groups of {a} is {a} times {b}, which equals {a * b} x's. Copies of copies "
            f"TIMES: x to the power {a * b}.",
            f'[[tape parts="{" | ".join(["x" + _sup(a)] * b)}" total="x{_sup(a * b)}" '
            f'caption="{b} × {a} = {a * b} x\'s — x{_sup(a * b)}"]]')


def _sci_board(p):
    a, b = p["a"], p["b"]
    return (f'[[placevalue n="{b}" caption="{b} — now move it {a} places up the chart"]]'
            f'[[step eq="{b} × 10{_sup(a)}"]]'
            f'[[step eq="{b} × {" × ".join(["10"] * a)} = ?"]]')


def _sci_worked(p):
    a, b = p["a"], p["b"]
    n = b * 10 ** a
    return (f"Look what you did: 10 to the power {a} is a 1 with {a} zeros, so {b} times it "
            f"moves the {b} up {a} places — {n}, the {b} with {a} zeros marching behind it. "
            f"The power counts the zeros; it is not a number to times by.",
            f'[[placevalue n="{n}" caption="{b} × 10{_sup(a)} = {n}"]]')


def _dbl_board(p):
    a, b = p["a"], p["b"]
    known = " | ".join(f"day {d}:{b * 2 ** d}" for d in range(a))
    return (f'[[bars data="{known}" caption="{b} pads, doubling — day {a} is the question"]]'
            f'[[step eq="start: {b}"]]'
            f'[[step eq="{" → ".join(str(b * 2 ** d) for d in range(a))} → ?"]]'
            f'[[step eq="{b} × {" × ".join(["2"] * a)} = ?"]]')


def _dbl_worked(p):
    a, b = p["a"], p["b"]
    n = b * 2 ** a
    alld = " | ".join(f"day {d}:{b * 2 ** d}" for d in range(a + 1))
    seq = ", then ".join(str(b * 2 ** d) for d in range(1, a + 1))
    return (f"Look what you did: doubling {a} times — {seq}. After {a} days the pond holds "
            f"{n} pads, because {b} times 2 to the power {a} is {n}. Each day doubled "
            f"everything there was, not just the start — look how the bars pull away.",
            f'[[bars data="{alld}" caption="{b} × 2{_sup(a)} = {n} pads after {a} days"]]')



# ---- (th, 2026-09-06) ALGEBRA 1 UNITS 7-9: the four rooms and their reverse, curves
# on the grid, the three middles. Every ask draws its question with the answer
# withheld; every walk-back draws the same picture filled in.
def _foil_board(p):
    a, b = p["a"], p["b"]
    return (f'[[areamodel rows="x,{a}" cols="x,{b}" ask="x" '
            f'caption="(x + {a}) by (x + {b}) — four rooms: the middle two are the question"]]'
            f'[[step eq="(x + {a})(x + {b})"]]'
            f'[[step eq="x rooms: {a}x + {b}x"]]'
            f'[[step eq="x² + ?x + {a * b}"]]')


def _foil_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: the two middle rooms are {b} x and {a} x, and middles ADD — "
            f"{a} plus {b} equals {a + b}, so {a + b} x. The corner times: {a} times {b} is "
            f"{a * b}. x squared, plus {a + b} x, plus {a * b}.",
            f'[[areamodel rows="x,{a}" cols="x,{b}" caption="(x + {a})(x + {b}) = x² + {a + b}x + {a * b}"]]')


def _fnum_board(p):
    a, b = p["a"], p["b"]
    return (f'[[areamodel rows="x,{a}" cols="x,{b}" ask="side" '
            f'caption="the rooms add up to x² + {a + b}x + {a * b} — one side is x + {a}: what is the other?"]]'
            f'[[step eq="x² + {a + b}x + {a * b}"]]'
            f'[[step eq="= (x + {a})(x + ?)"]]'
            f'[[step eq="{a} + ? = {a + b} · {a} × ? = {a * b}"]]')


def _fnum_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: the hidden number has to fit both clues. {a} plus {b} equals "
            f"{a + b} — the x count. {a} times {b} equals {a * b} — the corner. {b} fits both, "
            f"so the other side is x plus {b}. Multiply the sides back out and the sum comes "
            f"back.",
            f'[[areamodel rows="x,{a}" cols="x,{b}" caption="(x + {a})(x + {b}) = x² + {a + b}x + {a * b} ✓"]]')


def _gcfx_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[areamodel rows="{c}" cols="{a}x,{b}" ask="side" '
            f'caption="{c} tall — the rooms are {c * a}x and {c * b}: what is the second width?"]]'
            f'[[step eq="{c * a}x + {c * b}"]]'
            f'[[step eq="= {c}({a}x + ?)"]]'
            f'[[step eq="{c} × ? = {c * b}"]]')


def _gcfx_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: the {c} came out of BOTH rooms. {c * a} x is {c} times {a} x, "
            f"and {c * b} is {c} times {b} — so inside the parentheses is {a} x plus {b}. Check "
            f"it forwards: {c} times {a} x is {c * a} x, and {c} times {b} is {c * b}.",
            f'[[areamodel rows="{c}" cols="{a}x,{b}" caption="{c * a}x + {c * b} = {c}({a}x + {b}) ✓"]]')


def _dsq_board(p):
    a = p["a"]
    return (f'[[areamodel rows="x,{a}" cols="x,-{a}" ask="1" '
            f'caption="(x + {a}) by (x − {a}) — the middle rooms cancel; the corner is the question"]]'
            f'[[step eq="(x + {a})(x − {a})"]]'
            f'[[step eq="middles: +{a}x − {a}x cancel"]]'
            f'[[step eq="x² − ?"]]')


def _dsq_worked(p):
    a = p["a"]
    return (f"Look what you did: the middle rooms are plus {a} x and take away {a} x — they "
            f"cancel to nothing. The corner is {a} times {a}, which is {a * a}, taken away. "
            f"x squared take away {a * a}: the square of {a}, not {a} and not {2 * a}.",
            f'[[areamodel rows="x,{a}" cols="x,-{a}" caption="(x + {a})(x − {a}) = x² − {a * a}"]]')


def _sqy_board(p):
    a, b = p["a"], p["b"]
    return (f'[[graph func="x^2+{b}" lines="x={a}" range="-{a + 1}..{a + 1}" '
            f'caption="y = x² + {b} — climb from x = {a} up to the curve: how high?"]]'
            f'[[step eq="y = {a}² + {b} = ?"]]')


def _sqy_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: {a} squared is {a} times itself — {a * a}, not {2 * a}. Then "
            f"plus {b}: {a * a} plus {b} equals {a * a + b}. The curve stands at height "
            f"{a * a + b} over x equals {a}.",
            f'[[graph func="x^2+{b}" points="({a},{a * a + b})" range="-{a + 1}..{a + 1}" '
            f'caption="the point ({a}, {a * a + b}) — {a}² + {b}"]]'
            f'[[step eq="y = {a}² + {b} = {a * a} + {b} = {a * a + b}"]]')


def _roots_board(p):
    a, b = p["a"], p["b"]
    hi = max(a, b) + 2
    return (f'[[graph func="(x-{a})*(x-{b})" points="({a},0)" range="0..{hi}" '
            f'caption="the curve touches the ground at x = {a} — and once more: where?"]]'
            f'[[step eq="(x − {a})(x − {b}) = 0"]]'
            f'[[step eq="zero times anything is zero"]]'
            f'[[step eq="x = {a}, or x = ?"]]')


def _roots_worked(p):
    a, b = p["a"], p["b"]
    hi = max(a, b) + 2
    return (f"Look what you did: a product is zero only when a factor is zero. x equals {a} "
            f"turns the first bracket to zero, and x equals {b} turns the second to zero — "
            f"so the curve touches the ground at {a} and at {b}. Two answers, one per bracket, "
            f"and nobody added or timesed them.",
            f'[[graph func="(x-{a})*(x-{b})" points="({a},0),({b},0)" range="0..{hi}" '
            f'caption="the ground at x = {a} and x = {b}"]]'
            f'[[step eq="x = {a} or x = {b}"]]')


def _vtx_board(p):
    a, b = p["a"], p["b"]
    return (f'[[graph func="(x-{a})^2+{b}" range="{a - 3}..{a + 3}" '
            f'caption="y = (x − {a})² + {b} — how low does the curve go?"]]'
            f'[[step eq="y = (x − {a})² + {b}"]]'
            f'[[step eq="the squared part bottoms out at 0"]]'
            f'[[step eq="lowest y = ?"]]')


def _vtx_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: a square is never below zero, so the squared part bottoms "
            f"out at 0 — right at x equals {a}. There y is 0 plus {b}, which is {b}. The {a} "
            f"says where the low point sits; the {b} says how low it goes.",
            f'[[graph func="(x-{a})^2+{b}" points="({a},{b})" range="{a - 3}..{a + 3}" '
            f'caption="the lowest point ({a}, {b}) — lowest y = {b}"]]'
            f'[[step eq="lowest y = 0 + {b} = {b}"]]')


def _hitg_board(p):
    a = p["a"]
    return (f'[[graph func="{a * a}-x^2" range="0..{a + 1}" '
            f'caption="y = {a * a} − x² — where does the curve reach the ground?"]]'
            f'[[step eq="{a * a} − x² = 0"]]'
            f'[[step eq="x² = {a * a}"]]')


def _hitg_worked(p):
    a = p["a"]
    return (f"Look what you did: the height is zero when x squared equals {a * a}, and the "
            f"number that squares to {a * a} is {a} — {a} times {a}. The ball lands at x "
            f"equals {a}. {a} is the square root of {a * a}; it is not half of {a * a}.",
            f'[[graph func="{a * a}-x^2" points="(0,{a * a}),({a},0)" range="0..{a + 1}" '
            f'caption="from height {a * a} down to the ground at x = {a}"]]'
            f'[[step eq="x² = {a * a}, so x = {a}"]]')


def _mean_board(p):
    a, b = p["a"], p["b"]
    return (f'[[tape parts="{" | ".join(["?"] * a)}" total="{a * b}" '
            f'caption="{a * b} in all, shared equally between {a} — how much each?"]]'
            f'[[step eq="{a} numbers · {a * b} in all"]]'
            f'[[step eq="{a * b} ÷ {a} = ?"]]')


def _mean_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: pile everything together — {a * b} in all — then share it "
            f"equally between the {a}. {a * b} shared between {a} is {b} each. The mean is "
            f"{b}: what everybody would have if it were shared out evenly.",
            f'[[tape parts="{" | ".join([str(b)] * a)}" total="{a * b}" '
            f'caption="{a * b} ÷ {a} = {b} each — the mean is {b}"]]')


def _medn_board(p):
    a = p["a"]
    return (f'[[dotplot values="{_medlist(p)}" '
            f'caption="{2 * a + 1} numbers in order — walk in from both ends"]]'
            f'[[step eq="{2 * a + 1} numbers · {a} on each side of the middle"]]')


def _medn_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: {2 * a + 1} numbers, already in order. Walk in from both "
            f"ends at once and you meet at {b}, with {a} below it and {a} above it. The median "
            f"is {b} — the middle number, not the middle of the ends.",
            f'[[dotplot values="{_medlist(p)}" caption="{a} below · {b} · {a} above — the median is {b}"]]'
            f'[[step eq="median = {b}"]]')


def _rnge_board(p):
    a, b = p["a"], p["b"]
    return (f'[[bars data="smallest:{a} | biggest:{b}" '
            f'caption="smallest {a}, biggest {b} — how far does the data stretch?"]]'
            f'[[step eq="{b} − {a} = ?"]]')


def _rnge_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: the range is how far the data stretches, from the smallest "
            f"to the biggest. {b} take away {a} equals {b - a}. Not {a + b} — the ends are "
            f"not added, the gap between them is measured.",
            f'[[numberline min="0" max="{b + 2}" points="{a},{b}" '
            f'caption="from {a} to {b} — a stretch of {b - a}"]]'
            f'[[step eq="range = {b} − {a} = {b - a}"]]')


def _outl_board(p):
    b, c = p["b"], p["c"]
    m = (4 * b + c) // 5
    return (f'[[dotplot values="{b},{b},{b},{b},{c}" '
            f'caption="four with {b}, one with {c} — where is the middle child?"]]'
            f'[[step eq="mean = {m}"]][[step eq="median = ?"]]')


def _outl_worked(p):
    b, c = p["b"], p["c"]
    m = (4 * b + c) // 5
    return (f"Look what you did: line them up and walk in from both ends — the middle child "
            f"still has {b}, so the median is {b}. The mean was dragged to {m} by the one "
            f"with {c}, and nobody in the room has {m}. One unusual number moves the mean and "
            f"leaves the median standing.",
            f'[[dotplot values="{b},{b},{b},{b},{c}" caption="median {b} — the room · mean {m} — nobody"]]'
            f'[[step eq="median = {b} · mean = {m}"]]')



# ---- (ti, 2026-09-06) GEOMETRY UNITS 1-3: angles split, lines crossed, the circle, the
# midpoint, the three moves on the grid, the triangle's letters and angles. Every ask
# draws its question with the answer withheld; every walk-back draws it filled in.
def _comp_board(p):
    a = p["a"]
    return (f'[[angle deg="90" split="{a}" caption="a square corner split — {a}° and the rest"]]'
            f'[[step eq="90° − {a}° = ?"]]')


def _comp_worked(p):
    a = p["a"]
    return (f"Look what you did: the two angles fill a square corner, and a square corner is "
            f"90 degrees — not 180. 90 take away {a} equals {90 - a}, and {a} plus {90 - a} "
            f"puts the corner back together.",
            f'[[angle deg="90" split="{a},{90 - a}" caption="{a}° + {90 - a}° = 90°"]]')


def _vert_board(p):
    a = p["a"]
    return (f'[[angle deg="{a}" cross="{a}" caption="two lines cross — the {a}° angle and its twin opposite; the angle NEXT to it is the question"]]'
            f'[[step eq="the two sit on one straight line"]]'
            f'[[step eq="180° − {a}° = ?"]]')


def _vert_worked(p):
    a = p["a"]
    return (f"Look what you did: the angle next to {a} sits with it on one straight line, "
            f"and a straight line is 180. 180 take away {a} equals {180 - a}. The angle "
            f"opposite is {a} again — the twin — but next to was what was asked.",
            f'[[angle deg="180" split="{a},{180 - a}" caption="on one straight line: {a}° + {180 - a}° = 180°"]]')


def _circ_board(p):
    a = p["a"]
    return (f'[[circle center="O" r="{a}" caption="middle to edge: the radius is {a} — how far all the way across?"]]'
            f'[[step eq="diameter = 2 × {a} = ?"]]')


def _circ_worked(p):
    a = p["a"]
    return (f"Look what you did: the diameter goes all the way across through the middle — "
            f"two radiuses laid end to end. 2 times {a} equals {2 * a}. Doubling goes radius "
            f"to diameter; halving would have gone the wrong way.",
            f'[[circle center="O" r="{a}" d="{2 * a}" caption="two radiuses end to end: 2 × {a} = {2 * a}"]]')


def _mid_board(p):
    a, b = p["a"], p["b"]
    return (f'[[numberline min="{a - 1}" max="{b + 1}" points="{a},{b}" '
            f'caption="the ends, {a} and {b} — where is the middle?"]]'
            f'[[step eq="({a} + {b}) ÷ 2 = ?"]]')


def _mid_worked(p):
    a, b = p["a"], p["b"]
    m = (a + b) // 2
    return (f"Look what you did: both ends go in. {a} plus {b} equals {a + b}, shared by two "
            f"is {m}. Check it: {m} is {m - a} away from {a} and {b - m} away from {b} — the "
            f"same both ways, so {m} is the midpoint.",
            f'[[numberline min="{a - 1}" max="{b + 1}" points="{a},{m},{b}" mid="{m}" '
            f'caption="ends {a} and {b}, middle {m} — {m - a} each way"]]')


def _tran_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[graph points="({a},{b})" range="0..14" yrange="0..10" '
            f'caption="the point ({a}, {b}) — slide it {c} to the right"]]'
            f'[[step eq="slide right {c}: {a} + {c} = ?"]]')


def _tran_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: a slide to the right touches only x. {a} plus {c} equals "
            f"{a + c}, and y stayed at {b} — it never heard about the move. The point landed "
            f"at {a + c} across, {b} up.",
            f'[[graph points="({a},{b}),({a + c},{b})" range="0..14" yrange="0..10" '
            f'caption="from ({a}, {b}) to ({a + c}, {b}) — right {c}"]]')


def _refl_board(p):
    a, b = p["a"], p["b"]
    return (f'[[graph lines="x=0" points="({a},{b})" range="-9..9" yrange="0..10" '
            f'caption="the mirror stands on x = 0 — the point ({a}, {b}) flips across it"]]'
            f'[[step eq="x was {a} — new x = ?"]]')


def _refl_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: across the y line the point keeps its height and its "
            f"distance from the mirror — only the side changes. x goes from {a} to negative "
            f"{a}, and y stays {b}.",
            f'[[graph lines="x=0" points="({a},{b}),(-{a},{b})" range="-9..9" yrange="0..10" '
            f'caption="from ({a}, {b}) to (−{a}, {b}) — the same height, the other side"]]')


def _htrn_board(p):
    a, b = p["a"], p["b"]
    return (f'[[graph points="({a},{b})" range="-9..9" yrange="-9..9" '
            f'caption="the point ({a}, {b}) — turn it half way around (0, 0)"]]'
            f'[[step eq="y was {b} — new y = ?"]]')


def _htrn_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: a half turn around the middle carries the point to the "
            f"exact opposite spot — both signs change. x goes from {a} to negative {a}, and "
            f"y goes from {b} to negative {b}. One sign alone would have been a flip.",
            f'[[graph points="({a},{b}),(-{a},-{b})" range="-9..9" yrange="-9..9" '
            f'caption="from ({a}, {b}) to (−{a}, −{b}) — the opposite spot"]]')


def _rota_board(p):
    a = p["a"]
    pic = (f'[[pie parts="{a}" caption="a wheel cut into {a} equal parts — the smallest turn that lands it on itself?"]]'
           if a <= 12 else "")
    return (pic + f'[[step eq="{a} equal parts share one full turn"]]'
            f'[[step eq="360° ÷ {a} = ?"]]')


def _rota_worked(p):
    a = p["a"]
    d = 360 // a
    pic = (f'[[pie parts="{a}" caption="{a} equal parts — each is {d}° of the full turn"]]'
           if a <= 12 else
           f'[[write lines="one full turn = 360° | {a} equal parts | 360° ÷ {a} = {d}°"]]')
    return (f"Look what you did: one full turn is 360 degrees, and {a} equal parts share it "
            f"— 360 divided by {a} equals {d}. Turn the wheel {d} degrees and every part lands "
            f"on the next one; the wheel looks untouched.",
            pic + f'[[step eq="360° ÷ {a} = {d}°"]]')


def _cong_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[triangle v="A,B,C" sides="{a},{b},{c}" caption="ABC — sides {a}, {b}, {c}; DEF is its copy"]]'
            f'[[step eq="match the letters in order: A↔D · B↔E · C↔F"]]')


def _cong_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: the letters name the matching parts. F matches C and D "
            f"matches A, so side FD matches side CA — {c}. Not the side that looks right on "
            f"the page; the copy may be turned.",
            f'[[triangle v="A,B,C" sides="{a},{b},{c}" caption="ABC — CA is {c}"]]'
            f'[[triangle v="D,E,F" sides="{a},{b},{c}" caption="DEF — the same three sides: FD is {c}"]]')


def _isos_board(p):
    a = p["a"]
    return (f'[[triangle v="A,B,C" ticks="BC,CA" angles="{a},{a}," '
            f'caption="two equal sides — base angles {a}° and {a}°; the top is the question"]]'
            f'[[step eq="{a}° + {a}° + ? = 180°"]]')


def _isos_worked(p):
    a = p["a"]
    return (f"Look what you did: both base angles go in before the top comes out. {a} and "
            f"{a} use {2 * a} of the 180, so the top is 180 take away {2 * a}, which is "
            f"{180 - 2 * a}. Take away only one and the twin is still sitting inside.",
            f'[[triangle v="A,B,C" ticks="BC,CA" angles="{a},{a},{180 - 2 * a}" '
            f'caption="{a}° + {a}° + {180 - 2 * a}° = 180°"]]')


def _extr_board(p):
    a, b = p["a"], p["b"]
    return (f'[[triangle v="A,B,C" angles="{a},{b}," '
            f'caption="angles {a}° and {b}° — the third corner is opened out: how big is the outside angle?"]]'
            f'[[step eq="inside corner + exterior = 180°"]]'
            f'[[step eq="exterior = {a}° + {b}° = ?"]]')


def _extr_worked(p):
    a, b = p["a"], p["b"]
    c = 180 - a - b
    return (f"Look what you did: the inside corner is 180 take away {a} and {b}, which is "
            f"{c}. The exterior angle sits with it on a straight line, so it is 180 take away "
            f"{c} — {a + b}. And {a + b} is exactly the two far angles put together.",
            f'[[triangle v="A,B,C" angles="{a},{b},{c}" '
            f'caption="inside corner {c}° — exterior 180° − {c}° = {a + b}° = {a}° + {b}°"]]')


def _chas_board(p):
    a = p["a"]
    return (f'[[triangle v="A,B,C" ticks="BC,CA" angles=",,{a}" '
            f'caption="apex {a}° — the two equal base angles share the rest"]]'
            f'[[step eq="(180° − {a}°) ÷ 2 = ?"]]')


def _chas_worked(p):
    a = p["a"]
    r = 180 - a
    e = r // 2
    return (f"Look what you did: take the apex out first — 180 take away {a} leaves {r} for "
            f"the two base angles. They are equal, so they share it evenly: {r} divided by 2 "
            f"equals {e} each.",
            f'[[triangle v="A,B,C" ticks="BC,CA" angles="{e},{e},{a}" '
            f'caption="{e}° + {e}° + {a}° = 180°"]]')



# ---- (tj, 2026-09-06) GEOMETRY UNITS 4-6: the small shape beside its enlarged copy,
# the right triangle with its sides, the circle cut by its arcs. Every ask draws its
# question with the answer withheld; every walk-back draws it filled in.
def _scal_board(p):
    a, b = p["a"], p["b"]
    return (f'[[triangle v="A,B,C" sides="{a},," caption="the small triangle — one side is {a}; scale factor {b}"]]'
            f'[[step eq="scale factor {b}: {a} × {b} = ?"]]')


def _scal_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: a scale factor is a times, never an add. {a} times {b} "
            f"equals {a * b}, and every other side of the copy is timesed by {b} too — that is "
            f"why the copy keeps its shape.",
            f'[[triangle v="A,B,C" sides="{a},," caption="small: {a}"]]'
            f'[[triangle v="D,E,F" sides="{a * b},," caption="enlarged × {b}: {a * b}"]]')


def _sfac_board(p):
    a, b = p["a"], p["b"]
    return (f'[[bars data="small:{a} | big:{b}" caption="matching sides: {a} in the small shape, {b} in the big one"]]'
            f'[[step eq="{b} ÷ {a} = ?"]]')


def _sfac_worked(p):
    a, b = p["a"], p["b"]
    k = b // a
    return (f"Look what you did: the factor is the big side divided by the side it matches — "
            f"{b} divided by {a} equals {k}. Check it backwards: {a} times {k} equals {b}. Not "
            f"the difference, {b - a}; similar shapes share a times.",
            f'[[bars data="small:{a} | big:{b}" caption="{b} ÷ {a} = {k} — the big side is {k} times the small"]]'
            f'[[step eq="{b} ÷ {a} = {k} · {a} × {k} = {b} ✓"]]')


def _mside_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[triangle v="A,B,C" sides="{a},{b}," caption="the small triangle — {a} matches {a * c} in the big one; what matches {b}?"]]'
            f'[[step eq="{a} → {a * c} · {b} → ?"]]')


def _mside_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: divide to find the factor — {a * c} divided by {a} is {c} — "
            f"then times to cross over: {b} times {c} equals {b * c}. Not {b} plus "
            f"{a * c - a}; adding the same difference bends the shape.",
            f'[[triangle v="A,B,C" sides="{a},{b}," caption="small: {a} and {b}"]]'
            f'[[triangle v="D,E,F" sides="{a * c},{b * c}," caption="big × {c}: {a * c} and {b * c}"]]')


def _sare_board(p):
    a, b = p["a"], p["b"]
    return (f'[[rectangle w="{b}" h="{b}" caption="scale factor {b} strikes both directions — {b} by {b} boxes for every one"]]'
            f'[[step eq="area {a} · scale factor {b}"]]'
            f'[[step eq="{a} × {b} × {b} = ?"]]')


def _sare_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: area lives in two directions, and the factor strikes both. "
            f"Every one square becomes {b} by {b} — {b * b} squares — so {a} times {b} times "
            f"{b} equals {a * b * b}. Length pays the factor once; area pays it twice.",
            f'[[rectangle w="{b}" h="{b}" caption="one square scaled by {b}: {b * b} squares"]]'
            f'[[step eq="{a} × {b} × {b} = {a * b * b}"]]')


def _pyth_board(p):
    a, b = p["a"], p["b"]
    return (f'[[triangle v="A,B,C" right="B" sides="{a},{b}," caption="legs {a} and {b} — the hypotenuse is across from the square corner"]]'
            f'[[step eq="{a}² + {b}² = ?²"]]')


def _pyth_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: {a} squared is {a * a} and {b} squared is {b * b}; put "
            f"together, {a * a + b * b}. Which number times itself is {a * a + b * b}? {c} — "
            f"so the hypotenuse is {c}. Not {a + b}, the walk around the corner, and not "
            f"{a * a + b * b}, the square of the side.",
            f'[[righttriangle adj="{b}" opp="{a}" hyp="{c}" caption="legs {a} and {b}, hypotenuse {c}"]]'
            f'[[step eq="{a}² + {b}² = {a * a + b * b} = {c}²"]]')


def _leg_board(p):
    a, c = p["a"], p["c"]
    return (f'[[triangle v="A,B,C" right="B" sides="{a},,{c}" caption="hypotenuse {c}, one leg {a} — the other leg is the question"]]'
            f'[[step eq="{a}² + ?² = {c}²"]]')


def _leg_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: the rule speaks in squares. {c} squared is {c * c}, take "
            f"away {a} squared, {a * a}, leaves {c * c - a * a} — and {b} times {b} is "
            f"{b * b}, so the other leg is {b}. Not {c - a}: the lengths are never taken "
            f"away, the squares are.",
            f'[[righttriangle adj="{a}" opp="{b}" hyp="{c}" caption="legs {a} and {b}, hypotenuse {c}"]]'
            f'[[step eq="{c}² − {a}² = {c * c - a * a} = {b}²"]]')


def _tang_board(p):
    a, b = p["a"], p["b"]
    return (f'[[righttriangle adj="{a}" opp="{b}" caption="adjacent {a}, opposite {b} — how steep is the marked angle?"]]'
            f'[[step eq="tan = {b} ÷ {a} = ?"]]')


def _tang_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: the tangent is opposite divided by adjacent — {b} divided "
            f"by {a} equals {b // a}. For every 1 across, the angle climbs {b // a}. A pure "
            f"number, no length: not {b}, and not {b - a}.",
            f'[[righttriangle adj="{a}" opp="{b}" caption="tan = {b} ÷ {a} = {b // a} — climbs {b // a} for every 1 across"]]'
            f'[[step eq="tan = {b} ÷ {a} = {b // a}"]]')


def _topp_board(p):
    a, b = p["a"], p["b"]
    return (f'[[triangle v="A,B,C" right="B" sides="{a},," caption="adjacent {a}, tangent {b} — the opposite side is the question"]]'
            f'[[step eq="tan = {b} · opposite = {a} × {b} = ?"]]')


def _topp_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: a tangent of {b} climbs {b} for every one across. Walk {a} "
            f"across and it climbs {b}, {a} times over: {a} times {b} equals {a * b}. The "
            f"tangent is a times, not an add — and never the answer itself.",
            f'[[righttriangle adj="{a}" opp="{a * b}" caption="adjacent {a}, tangent {b} — opposite {a * b}"]]'
            f'[[step eq="opposite = {a} × {b} = {a * b}"]]')


def _cent_board(p):
    a = p["a"]
    return (f'[[circle center="O" caption="two radiuses cut the circle — the small arc opens at {a}°; how much is the rest?"]]'
            f'[[step eq="360° − {a}° = ?"]]')


def _cent_worked(p):
    a = p["a"]
    return (f"Look what you did: a circle is a full turn, and a full turn is 360 — not a "
            f"line\'s 180. 360 take away {a} equals {360 - a}, and {a} plus {360 - a} puts "
            f"the whole circle back.",
            f'[[pie data="the arc {a}°:{a} | the rest {360 - a}°:{360 - a}" caption="{a}° + {360 - a}° = 360°"]]'
            f'[[step eq="360° − {a}° = {360 - a}°"]]')


def _insc_board(p):
    a = p["a"]
    return (f'[[circle center="O" caption="an arc of {a}° — an angle on the rim opens onto it; how big is that angle?"]]'
            f'[[step eq="inscribed = {a}° ÷ 2 = ?"]]')


def _insc_worked(p):
    a = p["a"]
    return (f"Look what you did: from the rim the arc looks half. {a} divided by 2 equals "
            f"{a // 2} degrees. From the middle the same arc would be {a}; the rim is farther "
            f"away, and from farther away it looks exactly half.",
            f'[[circle center="O" inscribed="{a}" caption="arc {a}° — from the rim it looks {a // 2}°"]]'
            f'[[step eq="{a}° ÷ 2 = {a // 2}°"]]')


def _iarc_board(p):
    a = p["a"]
    return (f'[[circle center="O" inscribed="{2 * a}" caption="an angle of {a}° standing on the rim — how big is the arc it opens onto?"]]'
            f'[[step eq="arc = 2 × {a}° = ?"]]')


def _iarc_worked(p):
    a = p["a"]
    return (f"Look what you did: from angle to arc you double. 2 times {a} equals {2 * a} "
            f"degrees — and check it forwards: half of {2 * a} is {a}. The arc is the bigger "
            f"one; halving would have gone the wrong way.",
            f'[[circle center="O" inscribed="{2 * a}" caption="angle {a}° on the rim — arc 2 × {a}° = {2 * a}°"]]'
            f'[[step eq="arc = 2 × {a}° = {2 * a}°"]]')


def _alen_board(p):
    a, b = p["a"], p["b"]
    n = 360 // a
    return (f'[[pie parts="{n}" shaded="1" caption="a central angle of {a}° cuts the circle into {n} equal parts — the arc is one of them"]]'
            f'[[step eq="360° ÷ {a}° = {n} parts"]]'
            f'[[step eq="{b} ÷ {n} = ?"]]')


def _alen_worked(p):
    a, b = p["a"], p["b"]
    n = 360 // a
    return (f"Look what you did: {a} degrees goes into 360 {n} times, so the circle is {n} "
            f"equal parts and the arc is one of them. The whole distance around is {b}, so "
            f"the arc is {b} divided by {n} — {b // n}. Degrees say how far it turns; the "
            f"length says how far it runs.",
            f'[[pie parts="{n}" shaded="1" caption="{n} equal parts of {b} — the arc is {b // n}"]]'
            f'[[step eq="{b} ÷ {n} = {b // n}"]]')



# ---- (tk, 2026-09-06) GEOMETRY UNITS 7-9: the grid with the segment and the right
# triangle under the slant, the parallelogram with its true height, the two rooms,
# the six faces, the box that grows three ways, the bag as a pie, the outfits as an
# array, the table read at the crossing. Every ask draws its question with the answer
# withheld; every walk-back draws it filled in.
def _vseg_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[graph points="({a},{b}),({a},{c})" range="0..10" yrange="0..10" caption="from ({a}, {b}) straight up to ({a}, {c}) — how many steps?"]]'
            f'[[step eq="{c} − {b} = ?"]]')


def _vseg_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: the length is the gap between the heights, {c} take away "
            f"{b}, which equals {c - b}. Count the steps, never the dots — a fence with "
            f"{c - b + 1} posts has {c - b} rails.",
            f'[[graph points="({a},{b}),({a},{c})" range="0..10" yrange="0..10" caption="{c} − {b} = {c - b} steps"]]'
            f'[[step eq="{c} − {b} = {c - b}"]]')


def _dist_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[graph points="({a},{b}),({a + 3 * c},{b + 4 * c})" range="0..14" yrange="0..14" caption="from ({a}, {b}) to ({a + 3 * c}, {b + 4 * c}) — across {3 * c}, up {4 * c}; how far straight?"]]'
            f'[[step eq="across {3 * c} · up {4 * c}"]]'
            f'[[step eq="{3 * c}² + {4 * c}² = ?²"]]')


def _dist_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: a right triangle sits under the slant — across {3 * c}, up "
            f"{4 * c}. {9 * c * c} plus {16 * c * c} is {25 * c * c}, and {5 * c} times "
            f"{5 * c} squares back to it: the straight path is {5 * c}. Walking the grid "
            f"would cost {7 * c}.",
            f'[[graph points="({a},{b}),({a + 3 * c},{b}),({a + 3 * c},{b + 4 * c})" range="0..14" yrange="0..14" caption="the right triangle under the slant — across {3 * c}, up {4 * c}, straight {5 * c}"]]'
            f'[[righttriangle adj="{3 * c}" opp="{4 * c}" hyp="{5 * c}" caption="{3 * c}² + {4 * c}² = {25 * c * c} = {5 * c}²"]]')


def _mid2_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[graph points="({a},{b}),({c},{b + 4})" range="0..14" yrange="0..14" caption="from ({a}, {b}) to ({c}, {b + 4}) — where is the middle\'s x?"]]'
            f'[[step eq="x: ({a} + {c}) ÷ 2 = ?"]]')


def _mid2_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    m = (a + c) // 2
    return (f"Look what you did: the x\'s are {a} and {c} — put together {a + c}, shared by "
            f"two is {m}. The middle sits halfway across, at x equals {m}; its y is its own "
            f"little average, {b + 2}.",
            f'[[graph points="({a},{b}),({m},{b + 2}),({c},{b + 4})" range="0..14" yrange="0..14" caption="the midpoint ({m}, {b + 2}) — x: ({a} + {c}) ÷ 2 = {m}"]]'
            f'[[step eq="x: ({a} + {c}) ÷ 2 = {m}"]]')


def _corn_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[graph points="({a},{b}),({c},{b}),({a},{b + 3})" range="0..14" yrange="0..14" caption="three corners of a rectangle — the fourth closes the box; what is its x?"]]'
            f'[[step eq="the fourth corner closes the rectangle"]]')


def _corn_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: the fourth corner sits straight above ({c}, {b}), so it "
            f"shares that x — {c}. It sits level with ({a}, {b + 3}), so its y is {b + 3}: the "
            f"corner is ({c}, {b + 3}), and the box is closed.",
            f'[[graph points="({a},{b}),({c},{b}),({a},{b + 3}),({c},{b + 3})" range="0..14" yrange="0..14" caption="the four corners — the fourth is ({c}, {b + 3})"]]'
            f'[[step eq="above ({c}, {b}) → x = {c}"]]')


def _para_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[polygon kind="parallelogram" base="{a}" slant="{c}" height="{b}" caption="base {a}, leaning side {c}, height {b} — which two make the area?"]]'
            f'[[step eq="area = base × height = ?"]]')


def _para_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: base times height — {a} times {b} equals {a * b}. Push the "
            f"leaning stack straight and it is a rectangle {a} long and {b} tall; the slanted "
            f"{c} was never how tall it stood.",
            f'[[rectangle w="{a}" h="{b}" caption="pushed straight: {a} by {b} — area {a * b}"]]'
            f'[[step eq="{a} × {b} = {a * b}"]]')


def _lshp_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[rectangle w="{a}" h="{b}" caption="one room: {a} by {b}"]]'
            f'[[rectangle w="{c}" h="{b}" caption="the other room: {c} by {b} — the floor in all?"]]'
            f'[[step eq="{a} × {b} + {c} × {b} = ?"]]')


def _lshp_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: cut, measure, put together. One room is {a} times {b}, "
            f"{a * b}; the other is {c} times {b}, {c * b}. {a * b} plus {c * b} equals "
            f"{b * (a + c)} — areas add to areas; lengths never do.",
            f'[[rectangle w="{a}" h="{b}" caption="{a} × {b} = {a * b}"]]'
            f'[[rectangle w="{c}" h="{b}" caption="{c} × {b} = {c * b}"]]'
            f'[[step eq="{a * b} + {c * b} = {b * (a + c)}"]]')


def _surf_board(p):
    a = p["a"]
    return (f'[[solid kind="cube" caption="a cube — one face has an area of {a}; six faces in all"]]'
            f'[[step eq="6 × {a} = ?"]]')


def _surf_worked(p):
    a = p["a"]
    return (f"Look what you did: six faces, all alike — top, bottom, and four around the "
            f"sides. 6 times {a} equals {6 * a} square units. Four walls alone would be "
            f"{4 * a}, an open box; the floor and the ceiling are faces too.",
            f'[[bars data="top:{a} | bottom:{a} | front:{a} | back:{a} | left:{a} | right:{a}" caption="six faces of {a} — 6 × {a} = {6 * a}"]]'
            f'[[step eq="6 × {a} = {6 * a}"]]')


def _svol_board(p):
    a, b = p["a"], p["b"]
    return (f'[[solid kind="prism" caption="a box of {a} cubic units — every edge enlarged by {b}"]]'
            f'[[step eq="volume grows in three directions"]]'
            f'[[step eq="{a} × {b} × {b} × {b} = ?"]]')


def _svol_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: the box grows {b} times as long, {b} times as wide and {b} "
            f"times as tall — {b} times {b} times {b} is {b ** 3} times the room. {a} times "
            f"{b ** 3} equals {a * b ** 3} cubic units. Length pays once, area twice, volume "
            f"three times.",
            f'[[solid kind="prism" w="×{b}" d="×{b}" h="×{b}" caption="every edge × {b}: {b} × {b} × {b} = {b ** 3} times the room"]]'
            f'[[step eq="{a} × {b ** 3} = {a * b ** 3}"]]')


def _poft_board(p):
    a, b = p["a"], p["b"]
    return (f'[[bars data="red:{a} | blue:{b}" caption="{a} red and {b} blue — red is {a} out of the whole bag"]]'
            f'[[step eq="out of ALL the marbles: {a} + {b} = ?"]]')


def _poft_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: the pick lands on one of ALL the marbles. {a} reds plus "
            f"{b} blues is {a + b} in the bag, so red is {a} out of {a + b} — not out of "
            f"{b}; the blues are not the whole bag.",
            f'[[pie data="red:{a} | blue:{b}" caption="the whole bag: {a} + {b} = {a + b} — red is {a} out of {a + b}"]]'
            f'[[step eq="{a} + {b} = {a + b}"]]')


def _notp_board(p):
    a, b = p["a"], p["b"]
    return (f'[[bars data="rain:{a} | all the chances:{b}" caption="rain takes {a} of the {b} chances — no rain gets the rest"]]'
            f'[[step eq="{b} − {a} = ?"]]')


def _notp_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: every chance belongs to somebody. {b} take away {a} leaves "
            f"{b - a} out of {b} for no rain — and {a} plus {b - a} puts the whole {b} back.",
            f'[[bars data="rain:{a} | no rain:{b - a}" caption="{a} + {b - a} = {b} — every chance spoken for"]]'
            f'[[step eq="{b} − {a} = {b - a}"]]')


def _outc_board(p):
    a, b = p["a"], p["b"]
    return (f'[[array rows="{a}" cols="{b}" caption="a row for each of the {a} shirts, a column for each of the {b} hats — every box is one outfit"]]'
            f'[[step eq="{a} × {b} = ?"]]')


def _outc_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: for every shirt, every one of the hats is still open — "
            f"choices times up. {a} rows of {b} boxes is {a} times {b}, which equals "
            f"{a * b} outfits. Adding gives {a + b} things, not outfits.",
            f'[[array rows="{a}" cols="{b}" caption="{a} × {b} = {a * b} outfits"]]'
            f'[[step eq="{a} × {b} = {a * b}"]]')


def _twop_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[twoway rowlabels="boys,girls" collabels="soccer,art" data="{a},{b}|{c},{c + 2}" caption="rows and columns of counts — find the girls row, then the art column"]]'
            f'[[step eq="find the girls row, then the art column"]]')


def _twop_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: the girls row is the second row; slide along to the art "
            f"column, and the box where they cross holds {c + 2}. The next-door boxes were "
            f"the traps — {b} is the boys with art, {c} is the girls with soccer.",
            f'[[twoway rowlabels="boys,girls" collabels="soccer,art" data="{a},{b}|{c},{c + 2}" caption="girls row, art column — the crossing holds {c + 2}"]]'
            f'[[step eq="girls row → art column → {c + 2}"]]')



# ---- (tl, 2026-09-06) ALGEBRA 2 UNITS 1-3: the distance on the number line, the
# count as bars, the trips as tapes, the clues as bars, the curve on the grid with its
# turn marked and its crossings marked, the test number as two bars, the square as an
# array, the degrees as bars, the machine with its door blank. Every ask draws its
# question with the answer withheld; every walk-back draws it filled in.
def _absv_board(p):
    a, b = p["a"], p["b"]
    return (f'[[numberline min="{a - 2}" max="{b + 2}" points="{a},{b}" caption="{a} and {b} on the line — how far apart?"]]'
            f'[[step eq="|{a} − {b}| = how far apart = ?"]]')


def _absv_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: {a} take away {b} lands on negative {b - a} — but the bars "
            f"ask how FAR, and a distance is a plain count of steps. From {a} to {b} is "
            f"{b - a} steps: keep the size, drop the sign.",
            f'[[numberline min="{a - 2}" max="{b + 2}" points="{a},{b}" hops="{a},{b}" caption="from {a} to {b}: {b - a} steps — |{a} − {b}| = {b - a}"]]'
            f'[[step eq="|{a} − {b}| = {b - a}"]]')


def _absc_dots(a):
    """(uq) every integer strictly inside the fence, as dots -- all of them up to a
    fence of 10; a wider fence shows its innermost, zero and its outermost dot."""
    if a <= 10:
        return ",".join(str(k) for k in range(-(a - 1), a))
    return f"{-(a - 1)},-1,0,1,{a - 1}"


def _absc_board(p):
    a = p["a"]
    return (f'[[numberline min="{-a}" max="{a}" points="{_absc_dots(a)}" caption="the fence at −{a} and {a} — count every integer strictly inside it"]]'
            f'[[step eq="|x| < {a} · integers inside the fence = ?"]]')


def _absc_worked(p):
    a = p["a"]
    return (f"Look what you did: count the dots one side at a time. Left of zero, negative "
            f"{a - 1} up to negative 1: {a - 1} dots. Right of zero, 1 up to {a - 1}: {a - 1} "
            f"more. And zero in the middle. {a - 1} plus {a - 1} plus 1 is {2 * a - 1} "
            f"integers. The fence posts stay out — {a} is not less than {a}.",
            f'[[numberline min="{-a}" max="{a}" points="{_absc_dots(a)}" caption="{a - 1} left + {a - 1} right + zero = {2 * a - 1}"]]'
            f'[[step eq="{a - 1} + {a - 1} + 1 = {2 * a - 1}"]]')


def _el2_board(p):
    a, b = p["a"], p["b"]
    return (f'[[tape parts="apple | apple | apple | banana | banana" total="{a}" caption="the big trip: 3 apples and 2 bananas, {a} cents"]]'
            f'[[tape parts="apple | banana | banana" total="{b}" caption="the small trip: 1 apple and the same 2 bananas, {b} cents — one apple costs?"]]'
            f'[[step eq="3 apples + 2 bananas = {a} · 1 apple + 2 bananas = {b}"]]'
            f'[[step eq="the bananas cancel: 2 apples = ?"]]')


def _el2_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: take the small trip away from the big one and the bananas "
            f"vanish. 3 apples take away 1 apple leaves 2 apples, costing {a} take away "
            f"{b} — {a - b}. Two apples for {a - b}: share, and one apple is "
            f"{(a - b) // 2} cents. Vanish, then share.",
            f'[[tape parts="apple | apple" total="{a - b}" caption="what is left standing: 2 apples = {a} − {b} = {a - b}"]]'
            f'[[step eq="2 apples = {a - b} · 1 apple = {(a - b) // 2}"]]')


def _sys3_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[bars data="x + y:{a} | y + z:{b} | x + z:{c}" caption="three clues, each about a pair — every friend stands in two of them"]]'
            f'[[step eq="x + y = {a} · y + z = {b} · x + z = {c}"]]'
            f'[[step eq="every friend is in exactly two clues"]]'
            f'[[step eq="x + y + z = ?"]]')


def _sys3_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    t = a + b + c
    return (f"Look what you did: put the three clues together — {t} — but every friend "
            f"stood on the scale twice, so {t} counts everybody two times. Halve it: all "
            f"three together weigh {t // 2}. Not {t}, and not a pair\'s typical weight.",
            f'[[bars data="all three clues:{t} | everyone once:{t // 2}" caption="{a} + {b} + {c} = {t} — everyone twice — so all three weigh {t // 2}"]]'
            f'[[step eq="{t} ÷ 2 = {t // 2}"]]')


def _vtx2_board(p):
    a, b = p["a"], p["b"]
    return (f'[[graph func="(x-{a})^2+{b}" range="{a - 4}..{a + 4}" caption="y = (x − {a})² + {b} — at which x does it turn?"]]'
            f'[[step eq="y = (x − {a})² + {b}"]]'
            f'[[step eq="the squared part is zero when x = ?"]]')


def _vtx2_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: the squared part bottoms out where x take away {a} is "
            f"zero — at x equals {a}, positive {a}. The minus points opposite. And the "
            f"plus {b} is a different fact: how high the turn floats, not where.",
            f'[[graph func="(x-{a})^2+{b}" points="({a},{b})" range="{a - 4}..{a + 4}" caption="the turn at x = {a} — the vertex ({a}, {b})"]]'
            f'[[step eq="x − {a} = 0"]][[step eq="x = {a}"]]')


def _rsum_board(p):
    a, b = p["a"], p["b"]
    return (f'[[graph func="(x-{a})*(x-{b})" range="-1..{a + b}" caption="y = (x − {a})(x − {b}) — two crossings; put together they equal?"]]'
            f'[[step eq="(x − {a})(x − {b}) = 0"]]'
            f'[[step eq="the two crossings, put together = ?"]]')


def _rsum_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: each factor donates one answer — x equals {a} and x "
            f"equals {b}, the two crossings. Put together, {a} plus {b} equals {a + b}. "
            f"Not the product, and not one answer of two.",
            f'[[graph func="(x-{a})*(x-{b})" points="({a},0),({b},0)" range="-1..{a + b}" caption="crossings at {a} and {b} — {a} + {b} = {a + b}"]]'
            f'[[step eq="{a} + {b} = {a + b}"]]')


def _disc_worked(p):
    a, b = p["a"], p["b"]
    sq, fb = a * a, 4 * b
    verdict = ("positive — the curve cuts the x line twice" if sq > fb else
               "exactly zero — the curve touches the x line once" if sq == fb else
               "below zero — the curve never reaches the x line")
    n = 2 if sq > fb else 1 if sq == fb else 0
    return (f"Look what you did: {a} squared is {sq}, and 4 times {b} is {fb}. The test "
            f"number is {verdict}. You never report the test number, only its sign: "
            f"{n} crossings.",
            f'[[bars data="{a}²:{sq} | 4 · {b}:{fb}" caption="{sq} against {fb} — the test number is {verdict.split(" — ")[0]}"]]'
            f'[[graph func="x^2+{a}*x+{b}" range="{-a - 3}..{3}" caption="y = x² + {a}x + {b} — {n} crossings"]]')


def _imag_board(p):
    a = p["a"]
    return (f'[[step eq="x² = −{a}"]]'
            f'[[step eq="i² = −1"]]'
            f'[[step eq="x = ? · i"]]')


def _imag_worked(p):
    a = p["a"]
    k = round(a ** 0.5)
    return (f"Look what you did: the i carries the minus, so the number in front of it is "
            f"what SQUARED gives {a} — {k}, because {k} times {k} is {a}. Check: {k} i "
            f"times {k} i is {a} times i squared, negative {a}. So x is {k} i.",
            (f'[[array rows="{k}" cols="{k}" caption="{k} × {k} = {a} — so x = {k}i"]]' if k <= 10 else
             f'[[rectangle w="{k}" h="{k}" caption="{k} × {k} = {a} — so x = {k}i"]]')
            + f'[[step eq="({k}i)² = {a} · i² = −{a} ✓"]]')


def _pdeg_board(p):
    a, b = p["a"], p["b"]
    return (f'[[bars data="x{_sup(a)}:{a} | x{_sup(b)}:{b}" caption="two piles of x\'s — {a} in one, {b} in the other; join them"]]'
            f'[[step eq="x{_sup(a)} · x{_sup(b)} = x to the?"]]')


def _pdeg_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: the top powers join, and joining piles of x\'s ADDS the "
            f"counts — x to the {a} times x to the {b} is x to the {a + b}. Degree {a} "
            f"times degree {b} lands on degree {a + b}. Not {a * b}: degrees do not times.",
            f'[[bars data="x{_sup(a)}:{a} | x{_sup(b)}:{b} | joined x{_sup(a + b)}:{a + b}" caption="{a} + {b} = {a + b}"]]'
            f'[[step eq="x{_sup(a)} · x{_sup(b)} = x{_sup(a + b)}"]]')


def _turnc_worked(p):
    a = p["a"]
    return (f"Look what you did: every turn spends a climb or a fall, and the last stretch "
            f"runs off to the horizon without turning back — so a degree {a} curve turns "
            f"at most {a - 1} times, one fewer than its degree. A ceiling, not a schedule.",
            f'[[bars data="degree:{a} | turns, at most:{a - 1}" caption="degree {a} → at most {a - 1} turns"]]'
            f'[[step eq="degree {a} → at most {a - 1} turns"]]')


def _rsum3_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[graph func="(x-{a})*(x-{b})*(x-{c})" range="-1..{c + 2}" caption="y = (x − {a})(x − {b})(x − {c}) — three crossings; put together they equal?"]]'
            f'[[step eq="three crossings, put together = ?"]]')


def _rsum3_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: three factors, three crossings — {a}, {b} and {c}. Put "
            f"together, {a} plus {b} plus {c} equals {a + b + c}. Not the product, and not "
            f"two of three: a cubic has three answers.",
            f'[[graph func="(x-{a})*(x-{b})*(x-{c})" points="({a},0),({b},0),({c},0)" range="-1..{c + 2}" caption="crossings at {a}, {b} and {c} — {a} + {b} + {c} = {a + b + c}"]]'
            f'[[step eq="{a} + {b} + {c} = {a + b + c}"]]')


def _pval_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[machine input="{c}" rule="x³ − {a}x + {b}" output="?" caption="feed the machine x = {c} — every x gets the same meal; what comes out?"]]'
            f'[[step eq="y = x³ − {a}x + {b}"]]'
            f'[[step eq="x = {c}: {c}³ − {a}·{c} + {b} = ?"]]')


def _pval_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    cube = c ** 3
    y = cube - a * c + b
    return (f"Look what you did: {c} CUBED is {cube} — not 3 times {c}. Take away {a} "
            f"times {c}, {a * c}, leaves {cube - a * c}; plus {b} equals {y}. Read the "
            f"power, keep the sign.",
            f'[[machine input="{c}" rule="x³ − {a}x + {b}" output="{y}" caption="{c}³ − {a}·{c} + {b} = {y}"]]'
            f'[[step eq="{c}³ = {cube}"]][[step eq="{cube} − {a * c} + {b} = {y}"]]')



# ---- (tm, 2026-09-06) ALGEBRA 2 UNITS 4-6: the sharing curve with its point marked,
# the machine run backwards (its input blank), the jammed machine and the curve that
# flies off, the level line the curve settles toward, the square that two roots make,
# the root beside the half, the machine that undoes a root, the number between two
# squares on the line, the sample fading on the bars, the layers stacked as bars, the
# logs added, the number between two powers. Every ask draws its question with the
# answer withheld; every walk-back draws it filled in.
def _rdiv_board(p):
    a, b = p["a"], p["b"]
    return (f'[[graph func="{a}/x" range="0..{a + 2}" caption="y = {a} ÷ x — the sharing curve; read it at x = {b}"]]'
            f'[[step eq="y = {a} ÷ x"]]'
            f'[[step eq="x = {b}: {a} ÷ {b} = ?"]]')


def _rdiv_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: {a} shared among {b} is {a} divided by {b}, which equals "
            f"{a // b}. The word is DIVIDED — not take away, not times. The bigger the "
            f"crowd, the smaller each share.",
            f'[[graph func="{a}/x" points="({b},{a // b})" range="0..{a + 2}" caption="at x = {b}, y = {a} ÷ {b} = {a // b}"]]'
            f'[[step eq="{a} ÷ {b} = {a // b}"]]')


def _rsol_board(p):
    a, b = p["a"], p["b"]
    return (f'[[machine input="?" rule="{a} ÷ x" output="{b}" caption="the machine ran backwards — which x went in to give {b}?"]]'
            f'[[step eq="{a} ÷ x = {b}"]]'
            f'[[step eq="x · {b} = {a}"]]'
            f'[[step eq="x = ?"]]')


def _rsol_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: x times {b} must rebuild {a}, so x is {a} divided by {b} — "
            f"{a // b}. Check it forward: {a} divided by {a // b} is {b}. Rebuild, then "
            f"divide; times is not this undo.",
            f'[[machine input="{a // b}" rule="{a} ÷ x" output="{b}" caption="x = {a} ÷ {b} = {a // b} — check: {a} ÷ {a // b} = {b}"]]'
            f'[[step eq="x = {a} ÷ {b} = {a // b}"]]')


def _excl_board(p):
    a, b = p["a"], p["b"]
    return (f'[[machine input="?" rule="{b} ÷ (x − {a})" output="jammed" caption="one x jams the machine — the bottom turns to zero; which x?"]]'
            f'[[step eq="y = {b} ÷ (x − {a})"]]'
            f'[[step eq="the bottom hits zero when x = ?"]]')


def _excl_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: the bottom, x take away {a}, is zero exactly at x equals "
            f"{a} — and dividing by zero is the one thing mathematics never allows. Look at "
            f"the curve: it flies off at x equals {a} and never lands. Every other x is "
            f"welcome.",
            f'[[graph func="{b}/(x-{a})" range="{a - 4}..{a + 4}" yrange="-12..12" caption="y = {b} ÷ (x − {a}) — the curve flies off at x = {a}: the forbidden x"]]'
            f'[[step eq="x − {a} = 0"]][[step eq="x = {a} forbidden"]]')


def _rasy_board(p):
    a, b = p["a"], p["b"]
    return (f'[[graph func="({a}*x+{b})/x" range="0..20" caption="y = ({a}x + {b}) ÷ x — as x grows huge, the curve flattens toward what?"]]'
            f'[[step eq="y = ({a}x + {b}) ÷ x"]]'
            f'[[step eq="split it: the fading part dies · y settles at ?"]]')


def _rasy_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: split the top — {a} x over x is just {a}, and {b} over x "
            f"is the fading part. As x grows huge the {b} share dies toward zero and the "
            f"{a} stands untouched: y settles toward {a}, the level line.",
            f'[[graph func="({a}*x+{b})/x" lines="y={a}" range="0..20" caption="y = {a} + {b} ÷ x — the fading part dies, y settles toward the line y = {a}"]]'
            f'[[step eq="y = {a} + {b} ÷ x"]][[step eq="settles at {a}"]]')


def _sq_figure(k, total, cap):
    """The square k by k: an array up to 10, a rectangle up to 20, bars beyond."""
    if k <= 10:
        return f'[[array rows="{k}" cols="{k}" caption="{cap}"]]'
    if k <= 20:
        return f'[[rectangle w="{k}" h="{k}" caption="{cap}"]]'
    return f'[[bars data="{k} × {k}:{total}" caption="{cap}"]]'


def _rmul_worked(p):
    a, b = p["a"], p["b"]
    k = round((a * b) ** 0.5)
    return (f"Look what you did: under one roof, {a} times {b} is {a * b} — and {a * b} is "
            f"a perfect square: {k} times {k}. Two ragged roots, one clean answer, {k}. "
            f"Not {a * b}, still under the roof; and roots never add.",
            _sq_figure(k, a * b, f"√{a} · √{b} = √{a * b} — and {a * b} is {k} × {k}")
            + f'[[step eq="√{a} · √{b} = √{a * b} = {k}"]]')


def _rpow_worked(p):
    a = p["a"]
    k = round(a ** 0.5)
    return (f"Look what you did: a one-half power is a square root, never a halving. The "
            f"root of {a} is {k}, because {k} times {k} is {a}. Half of {a} would be "
            f"{a // 2} — and {a // 2} times itself is nowhere near {a}.",
            f'[[bars data="√{a} = {k}:{k} | half of {a}:{a // 2}" caption="the root, {k}, beside the halving trap, {a // 2}"]]'
            f'[[step eq="{a}^½ = √{a} = {k}"]]')


def _rsq_board(p):
    a = p["a"]
    return (f'[[machine input="?" rule="√x" output="{a}" caption="something, rooted, gave {a} — which x went in?"]]'
            f'[[step eq="√x = {a}"]]'
            f'[[step eq="undo the root: x = ?"]]')


def _rsq_worked(p):
    a = p["a"]
    return (f"Look what you did: the root\'s undo is the square. {a} times {a} equals "
            f"{a * a}, so x is {a * a}. Check it forward: the square root of {a * a} is "
            f"{a}. Not double — doubling undoes halving, not rooting.",
            f'[[machine input="{a * a}" rule="√x" output="{a}" caption="x = {a}² = {a * a} — check: √{a * a} = {a}"]]'
            + _sq_figure(a, a * a, f"{a} × {a} = {a * a}")
            + f'[[step eq="x = {a}² = {a * a}"]]')


def _rbet_board(p):
    a = p["a"]
    lo = int(a ** 0.5)
    hi = lo + 1
    return (f'[[numberline min="{lo * lo}" max="{hi * hi}" points="{a}" caption="{a} between the squares {lo * lo} and {hi * hi} — nearer which one?"]]'
            f'[[step eq="{lo}² = {lo * lo} · {hi}² = {hi * hi}"]]'
            f'[[step eq="{a} sits between — closest to?"]]')


def _rbet_worked(p):
    a = p["a"]
    lo = int(a ** 0.5)
    hi = lo + 1
    near = lo if a - lo * lo < hi * hi - a else hi
    return (f"Look what you did: {a} sits {a - lo * lo} past {lo * lo} and {hi * hi - a} "
            f"short of {hi * hi}, so it leans toward {near * near} — the root of {a} is "
            f"closest to {near}. Square the neighbours, then see who is nearer; never "
            f"halve.",
            f'[[numberline min="{lo * lo}" max="{hi * hi}" points="{a}" hops="{near * near},{a}" caption="{a} − {lo * lo} = {a - lo * lo} · {hi * hi} − {a} = {hi * hi - a} — nearer {near * near}, so √{a} → {near}"]]'
            f'[[step eq="√{a} → closest to {near}"]]')


def _hlfl_board(p):
    a, b = p["a"], p["b"]
    return (f'[[bars data="day 0:{a}" caption="{a} grams to start — it halves every day for {b} days"]]'
            f'[[step eq="{a}' + " ÷ 2" * b + ' = ?"]]')


def _hlfl_worked(p):
    a, b = p["a"], p["b"]
    days = " | ".join(f"day {d}:{a // 2 ** d}" for d in range(b + 1))
    chain = " → ".join(str(a // 2 ** d) for d in range(b + 1))
    return (f"Look what you did: a divide each day, never a take away. {chain} — halving "
            f"{b} times divides by {2 ** b}, and {a} divided by {2 ** b} equals "
            f"{a // 2 ** b} grams. Big numbers fall fast when the fall is a times.",
            f'[[bars data="{days}" caption="{chain}"]]'
            f'[[step eq="{a} ÷ {2 ** b} = {a // 2 ** b}"]]')


def _logb_board(p):
    a, b = p["a"], p["b"]
    return (f'[[machine input="?" rule="{b} to the power x" output="{a}" caption="how many {b}\'s stack up to {a}? — the hidden exponent"]]'
            f'[[step eq="{b}^? = {a}"]]')


def _logb_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    layers = " | ".join(f"{b}{_sup(i)}:{b ** i}" for i in range(1, c + 1))
    return (f"Look what you did: count the layers — {b} stacks {c} times to build {a}. "
            f"The logarithm is the hidden exponent, {c}: the count of the layers, not one "
            f"divide, and not the base itself.",
            f'[[bars data="{layers}" caption="{c} layers of {b} reach {a} — the logarithm is {c}"]]'
            f'[[step eq="{b}^{c} = {a} · log = {c}"]]')


def _logm_board(p):
    a, b = p["a"], p["b"]
    la, lb = a.bit_length() - 1, b.bit_length() - 1
    return (f'[[bars data="log {a}:{la} | log {b}:{lb}" caption="two stacks of doublings — {la} and {lb}; join them"]]'
            f'[[step eq="log {a} = {la} · log {b} = {lb}"]]'
            f'[[step eq="{a} × {b} = {a * b}"]]'
            f'[[step eq="log {a * b} = ?"]]')


def _logm_worked(p):
    a, b = p["a"], p["b"]
    la, lb = a.bit_length() - 1, b.bit_length() - 1
    return (f"Look what you did: when values times, their logs add. {la} doublings joined "
            f"with {lb} doublings is {la + lb} doublings — the log of {a * b} is {la} plus "
            f"{lb}, which equals {la + lb}. Values times; logs add.",
            f'[[bars data="log {a}:{la} | log {b}:{lb} | log {a * b}:{la + lb}" caption="{la} + {lb} = {la + lb}"]]'
            f'[[step eq="log {a * b} = {la} + {lb} = {la + lb}"]]')


def _lbet_board(p):
    a = p["a"]
    lo = a.bit_length() - 1
    return (f'[[bars data="2{_sup(lo)}:{2 ** lo} | {a}:{a} | 2{_sup(lo + 1)}:{2 ** (lo + 1)}" caption="{a} between the powers {2 ** lo} and {2 ** (lo + 1)} — nearer which one?"]]'
            f'[[step eq="2^{lo} = {2 ** lo} · 2^{lo + 1} = {2 ** (lo + 1)}"]]'
            f'[[step eq="{a} sits between — closest to?"]]')


def _lbet_worked(p):
    a = p["a"]
    lo = a.bit_length() - 1
    hi = lo + 1
    near = lo if a - 2 ** lo < 2 ** hi - a else hi
    return (f"Look what you did: {a} sits {a - 2 ** lo} past {2 ** lo} and {2 ** hi - a} "
            f"short of {2 ** hi}, so it leans toward {2 ** near} — the logarithm of {a} is "
            f"closest to {near}. Power the neighbours, then see who is nearer; never halve.",
            f'[[bars data="2{_sup(lo)}:{2 ** lo} | {a}:{a} | 2{_sup(hi)}:{2 ** hi}" caption="{a} − {2 ** lo} = {a - 2 ** lo} · {2 ** hi} − {a} = {2 ** hi - a} — nearer {2 ** near}, so log {a} → {near}"]]'
            f'[[step eq="log {a} → closest to {near}"]]')



# ---- (tn, 2026-09-06) ALGEBRA 2 UNITS 7-9: the pattern's first terms as bars and the
# ride to the asked term, the leaps as bars, the ends paired on the number line and
# the staircase rectangle, the rule walked through the machine twice, the arrow on the
# unit circle (the height and across asks stay picture-free: the pointed arrow IS the
# answer once the spins are stripped), the same arrow after a full turn, the wave with
# its crest line, the five scores as bars, the shirts-by-pants array, the plays as a
# pie, the sample beside the school. Every ask draws its question with the answer
# withheld; every walk-back draws it filled in.
def _anth_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[bars data="term 1:{a} | term 2:{a + b} | term 3:{a + 2 * b}" caption="start {a}, step {b} — the first three terms; ride on to term {c}"]]'
            f'[[step eq="{a}, {a + b}, {a + 2 * b}, …"]]'
            f'[[step eq="term {c} = ?"]]')


def _anth_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    terms = " | ".join(f"term {i}:{a + (i - 1) * b}" for i in range(1, c + 1))
    return (f"Look what you did: term 1 is already standing at the start, so term {c} is "
            f"{c - 1} steps away — not {c}. {a} plus {c - 1} steps of {b} is {a} plus "
            f"{(c - 1) * b}, which equals {a + (c - 1) * b}.",
            f'[[bars data="{terms}" caption="{c - 1} steps of {b} from {a} — term {c} is {a + (c - 1) * b}"]]'
            f'[[step eq="{a} + {c - 1} × {b} = {a + (c - 1) * b}"]]')


def _gnth_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[bars data="term 1:{a} | term 2:{a * b} | term 3:{a * b * b}" caption="start {a}, each term {b} times the one before — leap on to term {c}"]]'
            f'[[step eq="{a}, {a * b}, {a * b * b}, …"]]'
            f'[[step eq="term {c} = ?"]]')


def _gnth_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    terms = " | ".join(f"term {i}:{a * b ** (i - 1)}" for i in range(1, c + 1))
    return (f"Look what you did: a ratio is a times, never an add. Term {c} is {c - 1} "
            f"leaps of times {b} from {a} — {a} times {b ** (c - 1)}, which equals "
            f"{a * b ** (c - 1)}. Adding {b} each time would only have strolled to "
            f"{a + b * (c - 1)}.",
            f'[[bars data="{terms}" caption="{c - 1} leaps of × {b} from {a} — term {c} is {a * b ** (c - 1)}"]]'
            f'[[step eq="{a} × {b ** (c - 1)} = {a * b ** (c - 1)}"]]')


def _gaus_board(p):
    a = p["a"]
    return (f'[[numberline min="1" max="{a}" points="1,{a}" caption="every counting number from 1 up to {a} — pair the ends"]]'
            f'[[step eq="1 + 2 + 3 + … + {a} = ?"]]')


def _gaus_worked(p):
    a = p["a"]
    total = a * (a + 1) // 2
    fig = (f'[[rectangle w="{a + 1}" h="{a}" half="1" caption="{a} rows of {a + 1} — half of {a * (a + 1)} is {total}"]]'
           if a + 1 <= 20 else
           f'[[bars data="{a} × {a + 1}:{a * (a + 1)} | halved:{total}" caption="{a} × {a + 1} = {a * (a + 1)}, halved: {total}"]]')
    return (f"Look what you did: pair the ends — 1 with {a}, 2 with {a - 1}, and on — and "
            f"every pair is {a + 1}. That is {a} times {a + 1}, halved: {total}. Not "
            f"{a * a}, which overshoots, and not {a}, the last footstep only.",
            fig + f'[[step eq="{a} × {a + 1} ÷ 2 = {total}"]]')


def _reca_board(p):
    a, b = p["a"], p["b"]
    return (f'[[machine input="{a}" rule="2x − {b}" output="?" caption="term 1 goes in, term 2 comes out — then term 2 goes back in for term 3"]]'
            f'[[step eq="{a} → ×2 − {b} → ? → ×2 − {b} → ?"]]')


def _reca_worked(p):
    a, b = p["a"], p["b"]
    t2 = 2 * a - b
    t3 = 2 * t2 - b
    return (f"Look what you did: walk the whole rule, every term. Term 2: 2 times {a} take "
            f"away {b} is {t2}. Term 3: 2 times {t2} take away {b} is {t3}. Not {t2}, "
            f"stopping early; and the take away happens every time.",
            f'[[machine input="{a}" rule="2x − {b}" output="{t2}" caption="term 2: 2 × {a} − {b} = {t2}"]]'
            f'[[machine input="{t2}" rule="2x − {b}" output="{t3}" caption="term 3: 2 × {t2} − {b} = {t3}"]]'
            f'[[step eq="{a} → {t2} → {t3}"]]')


_COMPASS = {0: "flat to the right", 90: "straight up", 180: "flat to the left", 270: "straight down"}


def _sinp_board(p):
    a = p["a"]
    return (f'[[step eq="{a}° · strip the full turns, point the arrow"]]'
            f'[[step eq="sine = the height of its tip = ?"]]')


def _sinp_worked(p):
    a = p["a"]
    spins, base = a // 360, a % 360
    h = {0: 0, 90: 1, 180: 0, 270: -1}[base]
    hs = {1: "1", 0: "0", -1: "negative 1"}[h]
    strip = (f"{a} is {spins} full spin{'s' if spins > 1 else ''} plus {base}, so " if spins else "")
    return (f"Look what you did: {strip}the arrow points {_COMPASS[base]}. The sine is the "
            f"height of its tip — {hs}. Strip away the full turns, point the arrow, read "
            f"the height.",
            f'[[unitcircle angle="{a}" caption="{a}° — the arrow points {_COMPASS[base]}: height {hs.replace("negative ", "−")}"]]'
            f'[[step eq="{a}° → {_COMPASS[base]} → sine {hs.replace("negative ", "−")}"]]')


def _cosp_board(p):
    a = p["a"]
    return (f'[[step eq="{a}° · strip the full turns, point the arrow"]]'
            f'[[step eq="cosine = the across of its tip = ?"]]')


def _cosp_worked(p):
    a = p["a"]
    spins, base = a // 360, a % 360
    c = {0: 1, 90: 0, 180: -1, 270: 0}[base]
    cs = {1: "1", 0: "0", -1: "negative 1"}[c]
    strip = (f"{a} is {spins} full spin{'s' if spins > 1 else ''} plus {base}, so " if spins else "")
    return (f"Look what you did: {strip}the arrow points {_COMPASS[base]}. The cosine is "
            f"the across of its tip — {cs}. Same arrow as the sine; read across, not up.",
            f'[[unitcircle angle="{a}" caption="{a}° — the arrow points {_COMPASS[base]}: across {cs.replace("negative ", "−")}"]]'
            f'[[step eq="{a}° → {_COMPASS[base]} → cosine {cs.replace("negative ", "−")}"]]')


def _spin_board(p):
    a = p["a"]
    return (f'[[unitcircle angle="{a}" values="0" caption="the arrow at {a}° — spin it one more full turn; where does it land?"]]'
            f'[[step eq="{a}° + one full turn = ?"]]')


def _spin_worked(p):
    a = p["a"]
    return (f"Look what you did: a full turn is 360, so {a} plus 360 equals {a + 360} — and "
            f"the arrow points exactly where it began: same direction, same sine, same "
            f"cosine. A half turn would land opposite; 360 take away {a} is a mirror.",
            f'[[unitcircle angle="{a + 360}" values="0" caption="{a + 360}° — the same arrow as {a}°"]]'
            f'[[step eq="{a}° + 360° = {a + 360}°"]]')


def _ampl_board(p):
    a = p["a"]
    return (f'[[graph func="{a}*sin(x)" range="-7..7" caption="y = {a} · sin x — how high does the wave reach?"]]'
            f'[[step eq="the top of the wave = ?"]]')


def _ampl_worked(p):
    a = p["a"]
    return (f"Look what you did: the plain sine tops out at 1, and the {a} out front "
            f"stretches every height by {a} — the wave crests at {a} and dips to negative "
            f"{a}. The amplitude is {a}: not {2 * a}, crest to trough, and not 1.",
            f'[[graph func="{a}*sin(x)" lines="y={a}" range="-7..7" caption="the crest line y = {a} — amplitude {a}"]]'
            f'[[step eq="crest = {a} · trough = −{a}"]]')


def _wavg_board(p):
    a, b = p["a"], p["b"]
    return (f'[[bars data="quiz 1:{a} | quiz 2:{a} | quiz 3:{a} | quiz 4:{b} | quiz 5:{b}" caption="five quizzes — three scored {a}, two scored {b}; the mean of all five?"]]'
            f'[[step eq="{a}, {a}, {a}, {b}, {b}"]]'
            f'[[step eq="mean of the five = ?"]]')


def _wavg_worked(p):
    a, b = p["a"], p["b"]
    m = (3 * a + 2 * b) // 5
    return (f"Look what you did: all five scores go in. Three {a}s are {3 * a}; two {b}s "
            f"are {2 * b}; put together, {3 * a + 2 * b}, shared by 5 — the mean is {m}. "
            f"It sits nearer the {a}s, because they count three times.",
            f'[[bars data="quiz 1:{a} | quiz 2:{a} | quiz 3:{a} | quiz 4:{b} | quiz 5:{b} | mean:{m}" caption="({3 * a} + {2 * b}) ÷ 5 = {m} — nearer the three {a}s"]]'
            f'[[step eq="({3 * a} + {2 * b}) ÷ 5 = {m}"]]')


def _cnt3_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[array rows="{a}" cols="{b}" caption="{a} shirts by {b} pants — every box is one pair; each pair then takes any of {c} hats"]]'
            f'[[step eq="{a} shirts · {b} pants · {c} hats"]]'
            f'[[step eq="outfits = ?"]]')


def _cnt3_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: slot by slot, the times keeps rolling. {a} times {b} is "
            f"{a * b} shirt-and-pants pairs, and each pair takes any of {c} hats: {a * b} "
            f"times {c} is {a * b * c} outfits. Not added, and not stopped at two slots.",
            f'[[array rows="{a}" cols="{b}" caption="{a} × {b} = {a * b} pairs — each with {c} hats: {a * b * c}"]]'
            f'[[step eq="{a} × {b} = {a * b} · {a * b} × {c} = {a * b * c}"]]')


def _expv_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[pie parts="{b}" shaded="{a}" caption="{b} plays — about {a} of them pay {c} tokens; how many tokens to expect?"]]'
            f'[[step eq="{b} plays · win {c} tokens, {a} times"]]'
            f'[[step eq="expected in all = ?"]]')


def _expv_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: count the paying plays first — about {a} of the {b} — "
            f"then times by the prize: {a} wins of {c} tokens is {a * c} tokens. Not "
            f"{b * c}, as if every play paid; and not {c}, one win only.",
            f'[[array rows="{a}" cols="{c}" caption="{a} wins of {c} tokens — {a} × {c} = {a * c}"]]'
            f'[[step eq="{a} × {c} = {a * c}"]]')


def _samp_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[bars data="sample asked:{a} | said yes:{b} | the school:{a * c}" caption="{b} of {a} said yes — the school is {a * c}; about how many say yes there?"]]'
            f'[[step eq="sample: {b} of {a}"]]'
            f'[[step eq="the school: {a * c} · like pizza: about ?"]]')


def _samp_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: the school is {c} samples wide — {a * c} is {c} times "
            f"{a}. If each sample behaves like the one we asked, each holds about {b}: "
            f"{b} times {c} is about {b * c}. Scale the sample, and keep the word about.",
            f'[[bars data="one sample:{b} | the school, {c} samples wide:{b * c}" caption="{b} × {c} = about {b * c}"]]'
            f'[[step eq="{a * c} = {c} × {a} · {b} × {c} = about {b * c}"]]')



# ---- (to, 2026-09-06) PRECALC UNITS 1-3: two machines in a row, the point that
# slides on the grid, the root's doorway, the border on the number line, the minus
# parade paired on the array, the plug-in machine, the four rooms with the end number
# blank, the bottom that flies off twice, the exponent brought down as bars, the log
# machine run backwards, the tank halving and the pile doubling on the bars. Every ask
# draws its question with the answer withheld; every walk-back draws it filled in.
def _fcmp_board(p):
    # (uq) Jim's flag 21:57: "show the two functions first, then ask the question, then
    # use the graphic to solve". The rules lead, the machines follow, the question last.
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[step eq="f(x) = x + {a} · g(x) = {b}x"]]'
            f'[[machine input="{c}" rule="{b}x" output="?" fname="g" caption="g runs first: {c} goes in"]]'
            f'[[machine input="?" rule="x + {a}" output="?" fname="f" caption="then f eats what g made — what comes out?"]]'
            f'[[step eq="f(g({c})) = ?"]]')


def _fcmp_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: inside first — g of {c} is {b} times {c}, {b * c}. Then the "
            f"outer machine: f of {b * c} is {b * c} plus {a}, which equals {b * c + a}. The "
            f"inner machine runs before the outer; run f first and the number is different.",
            f'[[machine input="{c}" rule="{b}x" output="{b * c}" fname="g" caption="g({c}) = {b * c}"]]'
            f'[[step eq="g({c}) = {b} × {c} = {b * c}"]]'
            f'[[machine input="{b * c}" rule="x + {a}" output="{b * c + a}" fname="f" caption="f({b * c}) = {b * c + a}"]]'
            f'[[step eq="f({b * c}) = {b * c} + {a} = {b * c + a}"]]'
            f'[[step eq="f(g({c})) = {b * c + a}"]]')


def _fshf_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    hi = b + a + 2
    return (f'[[graph points="({b},{c})" range="0..{hi}" yrange="0..{max(c + 2, 4)}" caption="the point ({b}, {c}) on the old graph — under f(x − {a}), where does it land?"]]'
            f'[[step eq="y = f(x − {a}) · old point ({b}, {c})"]]'
            f'[[step eq="new x = ?"]]')


def _fshf_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    hi = b + a + 2
    return (f"Look what you did: the minus inside points opposite — take away {a} inside "
            f"slides the whole graph RIGHT by {a}. The point keeps its height, {c}, and "
            f"lands at x equals {b} plus {a}, which is {b + a}. Not {b - a}: that is the "
            f"literal minus.",
            f'[[graph points="({b},{c}),({b + a},{c})" range="0..{hi}" yrange="0..{max(c + 2, 4)}" caption="({b}, {c}) slides right {a} to ({b + a}, {c})"]]'
            f'[[step eq="({b}, {c}) → ({b + a}, {c})"]]')


def _fdom_worked(p):
    a = p["a"]
    return (f"Look what you did: below {a}, x take away {a} goes negative and the root "
            f"refuses. At x equals {a} the inside is exactly zero — and zero under a root "
            f"is welcome. The doorway is {a}, and the curve starts right there. Not "
            f"negative {a}: that is the flip.",
            f'[[graph func="sqrt(x-{a})" points="({a},0)" range="{a - 3}..{a + 9}" yrange="0..4" caption="y = √(x − {a}) — the curve starts at the doorway, x = {a}"]]'
            f'[[step eq="x − {a} ≥ 0 → x ≥ {a}"]]')


def _fpie_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[numberline min="0" max="10" points="5,{c}" caption="the border at 5 — which side does x = {c} live on?"]]'
            f'[[step eq="x < 5 → x + {a} · x ≥ 5 → {b}x"]]'
            f'[[step eq="x = {c} · y = ?"]]')


def _fpie_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    if c < 5:
        return (f"Look what you did: {c} lives below 5, so the FIRST rule runs and no other — "
                f"{c} plus {a}, which equals {c + a}. The other rule sleeps; check the "
                f"neighborhood, then compute.",
                f'[[numberline min="0" max="10" points="5,{c}" caption="{c} is below 5 — the first rule runs: {c} + {a} = {c + a}"]]'
                f'[[step eq="{c} < 5 → {c} + {a} = {c + a}"]]')
    return (f"Look what you did: {c} is 5 or more, so the SECOND rule runs and no other — "
            f"{b} times {c}, which equals {b * c}. The other rule sleeps; check the "
            f"neighborhood, then compute.",
            f'[[numberline min="0" max="10" points="5,{c}" caption="{c} is 5 or more — the second rule runs: {b} × {c} = {b * c}"]]'
            f'[[step eq="{c} ≥ 5 → {b} × {c} = {b * c}"]]')


def _negp_worked(p):
    a = p["a"]
    pairs, left = a // 2, a % 2
    extra = f' extra="{left}"' if left else ""
    if left:
        return (f"Look what you did: {a} minus signs pair up — {pairs} pairs, and one lone "
                f"minus sign left over at the end of the parade. The pairs cancel; the "
                f"survivor stays. Odd power, answer negative 1.",
                f'[[array rows="2" cols="{pairs}"{extra} caption="{a} minus signs — {pairs} pairs cancel, one survives: −1"]]'
                f'[[step eq="(−1)^{a} = −1"]]')
    return (f"Look what you did: {a} minus signs pair up — {pairs} pairs, none left over — "
            f"and every pair cancels. Even power, answer 1: the minus is wiped away "
            f"completely.",
            f'[[array rows="2" cols="{pairs}" caption="{a} minus signs — {pairs} pairs, all cancel: 1"]]'
            f'[[step eq="(−1)^{a} = 1"]]')


def _remt_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[machine input="{a}" rule="x² + {b}x + {c}" output="?" caption="plug {a} into the top — what comes out is the number left over"]]'
            f'[[step eq="(x² + {b}x + {c}) ÷ (x − {a})"]]'
            f'[[step eq="left over = ?"]]')


def _remt_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    r = a * a + a * b + c
    return (f"Look what you did: plug in {a} — {a} squared is {a * a}, plus {b} times {a} is "
            f"{a * b}, plus {c}: in all, {r}. That is exactly what long division would have "
            f"left over, and you never divided. Plug in the {a} from x take away {a}.",
            f'[[machine input="{a}" rule="x² + {b}x + {c}" output="{r}" caption="{a}² + {b}·{a} + {c} = {r} — the leftover"]]'
            f'[[step eq="{a}² + {b}·{a} + {c} = {r}"]]')


def _vprd_board(p):
    a, b = p["a"], p["b"]
    return (f'[[areamodel rows="x,-{a}" cols="x,-{b}" ask="1" caption="(x − {a}) by (x − {b}) — four rooms; the corner room is the end number"]]'
            f'[[step eq="(x − {a})(x − {b})"]]'
            f'[[step eq="end number = ?"]]')


def _vprd_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: the corner room is negative {a} times negative {b} — "
            f"{a * b}. The end number is the product of the roots. The middle number is "
            f"their sum, {a + b}, worn with a minus: sum sits in the middle, product at the "
            f"end.",
            f'[[areamodel rows="x,-{a}" cols="x,-{b}" caption="x² − {a + b}x + {a * b} — the end number is {a} × {b}"]]'
            f'[[step eq="(x − {a})(x − {b}) = x² − {a + b}x + {a * b}"]]')


def _vasy_worked(p):
    a, b = p["a"], p["b"]
    if a != b:
        lo, hi = min(a, b), max(a, b)
        return (f"Look what you did: each factor dies at its own x — {a} zeroes the first, "
                f"{b} the second — and either one alone flattens the whole bottom. Look at "
                f"the curve: it flies off twice. Two different zeros — the count is 2.",
                f'[[graph func="1/((x-{a})*(x-{b}))" range="{lo - 2}..{hi + 2}" yrange="-6..6" caption="y = 1 ÷ (x − {a})(x − {b}) — flies off at {a} and at {b}: two forbidden x\'s"]]'
                f'[[step eq="x = {a} ✗ · x = {b} ✗ — count 2"]]')
    return (f"Look what you did: two factors, but both die at the SAME x — only {a} zeroes "
            f"the bottom. Look at the curve: it flies off once. Count the different zeros, "
            f"never the factors: the count is 1.",
            f'[[graph func="1/((x-{a})*(x-{a}))" range="{a - 3}..{a + 3}" yrange="-6..6" caption="y = 1 ÷ (x − {a})(x − {a}) — flies off once, at {a}: one forbidden x"]]'
            f'[[step eq="(x − {a})(x − {a}): both die at {a} — count 1"]]')


def _logp_worked(p):
    a, b = p["a"], p["b"]
    j = a.bit_length() - 1
    return (f"Look what you did: log base 2 of {a} is {j} — {j} layers. The power rule "
            f"brings the exponent {b} down front: {b} times {j}, which equals {b * j}. "
            f"Not {j ** b}, the log raised to the power — that is the wrong kind of growth.",
            f'[[bars data="log {a}:{j} | log {a}^{b}:{b * j}" caption="the exponent {b} comes down front: {b} × {j} = {b * j}"]]'
            f'[[step eq="log {a}^{b} = {b} × {j} = {b * j}"]]')


def _lsol_board(p):
    a, b = p["a"], p["b"]
    return (f'[[machine input="?" rule="log base {a} of x" output="{b}" caption="the log counted {b} layers — which number went in?"]]'
            f'[[step eq="log ? = {b} · base {a}"]]')


def _lsol_worked(p):
    a, b = p["a"], p["b"]
    layers = " | ".join(f"{a}{_sup(i)}:{a ** i}" for i in range(1, b + 1))
    return (f"Look what you did: the log counted {b} layers of {a}, so rebuild the number by "
            f"stacking them again — {a} multiplied out {b} times is {a ** b}. Not {a * b}: "
            f"a single times cannot reach {b} whole layers.",
            f'[[bars data="{layers}" caption="{b} layers of {a} — the mystery number is {a ** b}"]]'
            f'[[machine input="{a ** b}" rule="log base {a} of x" output="{b}" caption="log {a ** b} = {b} ✓"]]')


def _hcnt_board(p):
    a, b = p["a"], p["b"]
    return (f'[[bars data="start:{a} | now:{b}" caption="{a} liters down to {b}, halving each day — how many halvings?"]]'
            f'[[step eq="{a} → half each day → {b}"]]'
            f'[[step eq="days = ?"]]')


def _hcnt_worked(p):
    a, b = p["a"], p["b"]
    k = (a // b).bit_length() - 1
    days = " | ".join(f"day {i}:{a >> i}" for i in range(k + 1))
    chain = " → ".join(str(a >> i) for i in range(k + 1))
    return (f"Look what you did: halve and count — {chain}. That is {k} halvings, {k} days. "
            f"The ratio, {a // b}, says how many times bigger {a} is — never how many "
            f"days; ask how many 2s multiply up to it.",
            f'[[bars data="{days}" caption="{chain} — {k} halvings"]]'
            f'[[step eq="{chain} · {k} days"]]')


def _cmpd_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[bars data="start:{c}" caption="{c} dollars, doubling every {a} years — after {a * b} years?"]]'
            f'[[step eq="${c} · doubles every {a} years"]]'
            f'[[step eq="after {a * b} years → $?"]]')


def _cmpd_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    years = " | ".join(f"year {a * i}:{c * 2 ** i}" for i in range(b + 1))
    chain = " → ".join(str(c * 2 ** i) for i in range(b + 1))
    return (f"Look what you did: count the doublings first — {a * b} divided by {a} is {b}. "
            f"Then double {b} times: {chain}. {c * 2 ** b} dollars. Steady adding would "
            f"have stalled at {c * (1 + b)}; doubling pulls away.",
            f'[[bars data="{years}" caption="{b} doublings: {chain}"]]'
            f'[[step eq="{a * b} ÷ {a} = {b} doublings"]][[step eq="{chain}"]]')



# ---- (tp, 2026-09-06) PRECALC UNITS 4-6: the half turn beside the angle, the arrow
# wound backwards, the flat line with the arrow hugging it, the plain wave beside the
# fast one, the hundred square split between sine and cosine, the right triangle's two
# sharp corners, the mirror on the circle, the wave crossing its level line, the honest
# SAS triangle, the ramp, the compass, the arrow and its two steps. Every ask draws its
# question with the answer withheld; every walk-back draws it filled in.
def _rad1_board(p):
    a = p["a"]; deg = 180 * a
    return (f'[[bars data="a half turn:180 | {deg}°:{deg}" caption="a half turn of 180 beside {deg}° — how many half turns fit?"]]'
            f'[[step eq="{deg}° = ? π rad"]]')


def _rad1_worked(p):
    a = p["a"]; deg = 180 * a
    if a <= 10:
        fig = (f'[[tape parts="{"|".join(["180"] * a)}" total="{deg}°" '
               f'caption="{deg}° = {a} half turns = {a}π rad"]]')
    else:
        fig = (f'[[numberline min="0" max="{deg}" hops="{",".join(str(180 * i) for i in range(a + 1))}" '
               f'caption="{a} hops of 180 — {deg}° = {a}π rad"]]')
    return (f"Look what you did: 180 degrees is one half turn, one pi. Count how many fit in "
            f"{deg}: {deg} divided by 180 equals {a} — {a} pi radians. Quarter turns would "
            f"say {2 * a}, and the degrees themselves were never the answer.",
            fig + f'[[step eq="{deg} ÷ 180 = {a}"]][[step eq="{deg}° = {a}π rad"]]')


def _nspn_board(p):
    a = p["a"]
    return (f'[[unitcircle angle="-{a}" values="0" caption="the arrow wound {a}° backwards — the same arrow, named forwards?"]]'
            f'[[step eq="−{a}° + one full turn = ?"]]')


def _nspn_worked(p):
    a = p["a"]
    return (f"Look what you did: a full turn is 360, so negative {a} plus 360 equals "
            f"{360 - a}. The same arrow, named forwards — it hangs {a} below flat right "
            f"either way. Dropping the minus would say {a}, the mirror image above the line.",
            f'[[unitcircle angle="{360 - a}" values="0" caption="the same arrow: −{a}° is {360 - a}° forwards"]]'
            f'[[step eq="−{a} + 360 = {360 - a}"]]')


def _refq_board(p):
    a = p["a"]
    return (f'[[angle deg="180" split="{a}" caption="the flat line is 180° — the arrow at {a}°; the gap to flat left is the reference"]]'
            f'[[step eq="{a}° · reference angle = ?"]]')


def _refq_worked(p):
    a = p["a"]
    return (f"Look what you did: flat left is 180 and the arrow sits at {a}, so the gap is "
            f"180 take away {a} — {180 - a} degrees. Measured from straight up it would be "
            f"{a - 90}, but the reference angle hugs the FLAT line, always.",
            f'[[angle deg="180" split="{a},{180 - a}" caption="180 − {a} = {180 - a}° — the gap to flat left"]]'
            f'[[step eq="180 − {a} = {180 - a}°"]]')


def _wper_board(p):
    a = p["a"]
    return (f'[[graph func="sin(x*pi/180); sin({a}*x*pi/180)" names="sin x; sin {a}x" range="0..360" yrange="-1.5..1.5" '
            f'caption="the plain sine tells its story once in 360° — the sine of {a}x, beside it"]]'
            f'[[step eq="y = sin({a}x)"]]'
            f'[[step eq="repeats every ? degrees"]]')


def _wper_worked(p):
    a = p["a"]; per = 360 // a
    return (f"Look what you did: divide — 360 divided by {a} equals {per}. This wave tells "
            f"its whole story in {per} degrees, then starts again. Faster means SOONER: "
            f"stretching to {360 * a} points the wrong way.",
            f'[[graph func="sin({a}*x*pi/180)" names="sin {a}x" lines="x={per}" range="0..360" yrange="-1.5..1.5" '
            f'caption="one full story by x = {per}°, then it repeats"]]'
            f'[[step eq="360 ÷ {a} = {per}°"]]')


def _pyid_board(p):
    a = p["a"]
    return (f'[[hundredgrid shaded="{a}" eq="sin² = {a} of 100" caption="one whole is 100 hundredths — sine squared shaded; cosine squared is the rest"]]'
            f'[[step eq="sin² = {a}/100"]]'
            f'[[step eq="cos² = ?/100"]]')


def _pyid_worked(p):
    a = p["a"]
    return (f"Look what you did: sine squared plus cosine squared equals 1 — the whole "
            f"hundred. 100 take away {a} equals {100 - a}: cosine squared is {100 - a} "
            f"hundredths. The pair always splits one whole between them.",
            f'[[hundredgrid shaded="{a}" eq="{a} + {100 - a} = 100" caption="sin² {a} shaded, cos² {100 - a} left — one whole between them"]]'
            f'[[step eq="100 − {a} = {100 - a}"]][[step eq="cos² = {100 - a}/100"]]')


def _cofn_board(p):
    a = p["a"]
    return (f'[[triangle v="A,B,C" right="B" angles="{a},90,?" caption="one right triangle — its two sharp corners finish 90 together"]]'
            f'[[step eq="sin {a}° = cos ?°"]]')


def _cofn_worked(p):
    a = p["a"]
    return (f"Look what you did: {a} plus {90 - a} equals 90, so the sine of {a} equals the "
            f"cosine of {90 - a}. One triangle, two sharp corners — what one corner calls "
            f"height, the other calls across.",
            f'[[triangle v="A,B,C" right="B" angles="{a},90,{90 - a}" caption="{a} + {90 - a} = 90 — partners across ninety"]]'
            f'[[step eq="sin {a}° = cos {90 - a}°"]]')


def _negf_worked(p):
    a, c = p["a"], p["c"]
    base = (-a) % 360
    spins = a // 360
    # base is where the arrow POINTS after winding a degrees backwards, so the plain
    # across/height tables read off it (the OP_EXT ans reads sin(-a) off +a instead).
    v = ({0: 1, 90: 0, 180: -1, 270: 0} if c == 0 else {0: 0, 90: 1, 180: 0, 270: -1})[base]
    vs = {1: "1", 0: "0", -1: "negative 1"}[v]
    vb = vs.replace("negative ", "−")
    strip = (f"{a} back is {spins} full spin{'s' if spins > 1 else ''} and {a - 360 * spins} more, so the arrow"
             if spins else "The arrow")
    if c == 0:
        spoken = (f"Look what you did: the mirror flips height, never across. {strip} "
                  f"points {_COMPASS[base]}, and its across is {vs}. The cosine of negative "
                  f"{a} equals the cosine of {a} — even: the minus vanishes.")
        tail = f"cosine = across = {vb}"
    else:
        spoken = (f"Look what you did: the mirror flips the height. {strip} points "
                  f"{_COMPASS[base]}, and its height is {vs}. The sine of negative {a} is the "
                  f"opposite of the sine of {a} — odd: one minus survives.")
        tail = f"sine = height = {vb}"
    return (spoken,
            f'[[unitcircle angle="-{a}" caption="−{a}° — the arrow points {_COMPASS[base]}: {tail}"]]'
            f'[[step eq="−{a}° → {_COMPASS[base]}"]][[step eq="{tail}"]]')


def _sols_pts(p):
    a, b, c = p["a"], p["b"], p["c"]
    f = ({0: 1, 90: 0, 180: -1, 270: 0} if c == 1 else {0: 0, 90: 1, 180: 0, 270: -1})
    return [x for x in range(90, 360 * b + 1, 90) if f[x % 360] == a]


def _sols_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    fn, word = ("cos", "cosine") if c == 1 else ("sin", "sine")
    tv = "−1" if a == -1 else str(a)
    turns = f"{b} turn{'s' if b > 1 else ''}"
    return (f'[[graph func="{fn}(x*pi/180)" names="{word}" lines="y={a}" range="0..{360 * b}" yrange="-1.5..1.5" '
            f'caption="the {word} through {turns} and the line y = {tv} — count the touches after the start"]]'
            f'[[step eq="{turns} · {fn} = {tv} · count = ?"]]')


def _sols_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    fn, word = ("cos", "cosine") if c == 1 else ("sin", "sine")
    tv = "−1" if a == -1 else str(a)
    tw = "negative 1" if a == -1 else str(a)
    base = 2 if a == 0 else 1
    ans = base * b
    place = {(0, 0): "at flat left and at the finish", (0, 1): "at straight up",
             (0, -1): "at straight down", (1, 0): "at straight up and at straight down",
             (1, 1): "at the finish", (1, -1): "at flat left"}[(c, a)]
    xs = _sols_pts(p)
    pts = ",".join(f"({x},{a})" for x in xs)
    turns = f"{b} turn{'s' if b > 1 else ''}"
    tail = (f"{b} turns, {base} each: {ans}." if b > 1 else f"One turn, so the count is {base}.")
    return (f"Look what you did: each turn, the {word} equals {tw} "
            f"{'twice' if base == 2 else 'once'} — {place}. {tail} Skip the start, keep the "
            f"finish, and never say 4 just because there are four quarters.",
            f'[[graph func="{fn}(x*pi/180)" names="{word}" lines="y={a}" points="{pts}" range="0..{360 * b}" yrange="-1.5..1.5" '
            f'caption="{ans} touch{"es" if ans > 1 else ""} after the start — {place}"]]'
            f'[[step eq="{turns} · {base} each turn = {ans}"]]')


def _arsn_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[triangle v="A,B,C" sas="{a},{b},{c}" sides="{a},,{b}" angles="{c},," caption="sides {a} and {b} with {c}° between them — drawn true"]]'
            f'[[step eq="sides {a} and {b} · angle {c}° between them"]]'
            f'[[step eq="area = ?"]]')


def _arsn_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    prod = a * b
    if c == 90:
        ans = prod // 2
        spoken = (f"Look what you did: the sine of 90 degrees is 1, so the area is half of "
                  f"{a} times {b} — half of {prod}, {ans}. The whole {prod} is the rectangle "
                  f"around it, and a triangle takes half.")
        steps = f'[[step eq="sin 90° = 1"]][[step eq="½ · {a} · {b} · 1 = {ans}"]]'
    else:
        ans = prod // 4
        spoken = (f"Look what you did: the sine of {c} degrees is one half, so half the "
                  f"product is halved again — a quarter of {a} times {b}, a quarter of {prod}, "
                  f"which is {ans}."
                  + (" And 150 shares its sine with 30: the wide triangle covers what the "
                     "sharp one covers." if c == 150 else ""))
        steps = f'[[step eq="sin {c}° = ½"]][[step eq="½ · {a} · {b} · ½ = {ans}"]]'
    return (spoken,
            f'[[triangle v="A,B,C" sas="{a},{b},{c}" sides="{a},,{b}" angles="{c},," caption="area = ½ · {a} · {b} · sin {c}° = {ans}"]]'
            + steps)


def _ramp_board(p):
    a = p["a"]
    return (f'[[triangle v="A,B,C" right="B" sides=",?,{a}" angles="30,," caption="a {a}-foot ramp at 30° — how high is its top end?"]]'
            f'[[step eq="height = ?"]]')


def _ramp_worked(p):
    a = p["a"]; h = a // 2
    return (f"Look what you did: the sine of 30 degrees is one half, so the ramp climbs half "
            f"its length — half of {a} is {h} feet. The {a} is how far you walk up the slope, "
            f"and doubling would say {2 * a}, taller than the ramp is long.",
            f'[[triangle v="A,B,C" right="B" sides=",{h},{a}" angles="30,," caption="half of {a} — the top end sits {h} feet up"]]'
            f'[[step eq="½ · {a} = {h} ft"]]')


def _brng_board(p):
    a, b = p["a"], p["b"]
    return (f'[[unitcircle bearing="{a}" turn="{b}" caption="the ship on bearing {a}° — now a {b}° turn clockwise"]]'
            f'[[step eq="{a}° · turn {b}° clockwise · new bearing = ?"]]')


def _brng_worked(p):
    a, b = p["a"], p["b"]; tot = a + b; ans = tot - 360
    return (f"Look what you did: {a} plus {b} equals {tot} — past a full turn, so take away "
            f"360: the new bearing is {ans} degrees. The ship swung around through north. "
            f"{tot} names no bearing, and {a - b} is where the backwards turn would point.",
            f'[[unitcircle bearing="{ans}" caption="{a} + {b} = {tot}, past 360 — the new bearing is {ans}°"]]'
            f'[[step eq="{a} + {b} = {tot}"]][[step eq="{tot} − 360 = {ans}"]]')


def _vmag_board(p):
    a, b = p["a"], p["b"]
    return (f'[[triangle v="A,B,C" right="B" sides="{a},{b},?" caption="right {a}, up {b} — the arrow is the slanted side"]]'
            f'[[step eq="the arrow = ?"]]')


def _vmag_worked(p):
    a, b, c = p["a"], p["b"], p["c"]; sq = a * a + b * b
    return (f"Look what you did: right {a} and up {b} meet at a right angle, so the arrow is "
            f"the hypotenuse. {a} squared is {a * a}, {b} squared is {b * b}, put together "
            f"{sq} — and {c} times {c} squares back to it. The arrow is {c}: longer than "
            f"either step, shorter than walking both, {a + b}.",
            f'[[vector v="{a},{b}" caption="right {a}, up {b} — the arrow is {c} long"]]'
            f'[[step eq="{a}² + {b}² = {sq}"]][[step eq="√{sq} = {c}"]]')



# ---- (tq, 2026-09-06) PRECALC UNITS 7-9: the circle with its radius marked "?", the
# circle with its middle unnamed, the two reaches of an ellipse as a tape, the ball's
# path at t = 1, the doubling machine, the sigma recipe machine, the crowd as an
# array, the bounces as bars, the line that never breaks, the machine that jams at
# the hole, the step with its two heights, the window on the curve. Every ask draws
# its question with the answer withheld; every walk-back draws it filled in.
def _crad_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[circle center="O" r="?" caption="the circle — how far from its middle to its edge? the equation says {c * c}, and {c * c} is not it"]]'
            f'[[step eq="(x − {a})² + (y − {b})² = {c * c}"]]'
            f'[[step eq="radius = ?"]]')


def _crad_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: the number on the right is the radius SQUARED. Un-square "
            f"{c * c} and the radius is {c} — the circle reaches {c} in every direction "
            f"from its middle. The {a} and the {b} say where it sits, never how big it is.",
            f'[[conic type="circle" r="{c}" cx="{a}" cy="{b}" caption="middle ({a}, {b}) — the circle reaches {c} every way: radius {c}"]]'
            f'[[step eq="un-square {c * c} = {c}"]][[step eq="radius = {c}"]]')


def _cctr_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[circle center="?" caption="the circle — where does its middle sit? the take-aways know, with the sign flipped"]]'
            f'[[step eq="(x − {a})² + (y − {b})² = {c * c}"]]'
            f'[[step eq="center x = ?"]]')


def _cctr_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: x take away {a} is zero exactly at x equals {a}, and the "
            f"middle sits where the squared pieces go quiet — the center's x is {a}. The "
            f"minus points opposite: take away {a} means positive {a}. The {b} is the y.",
            f'[[conic type="circle" r="{c}" cx="{a}" cy="{b}" caption="the middle sits at ({a}, {b}) — center x = {a}"]]'
            f'[[step eq="x − {a} = 0 at x = {a}"]][[step eq="center x = {a}"]]')


def _elax_board(p):
    a, b = p["a"], p["b"]
    return (f'[[tape parts="?|?" total="left edge to right edge = ?" caption="the middle splits the width into two equal reaches — un-square {a * a} for one of them"]]'
            f'[[step eq="x²/{a * a} + y²/{b * b} = 1"]]'
            f'[[step eq="left edge to right edge = ?"]]')


def _elax_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: the number under x squared is the half-width SQUARED. "
            f"Un-square {a * a} and the ellipse reaches {a} each way from the middle; edge "
            f"to edge is double that — {2 * a}. The {b * b} does the same work upward: "
            f"{b} each way.",
            f'[[conic type="ellipse" a="{a}" b="{b}" caption="{a} each way across, {b} each way up"]]'
            f'[[tape parts="{a}|{a}" total="{2 * a}" caption="two reaches of {a} — {2 * a} across"]]'
            f'[[step eq="un-square {a * a} = {a} each way"]][[step eq="{a} + {a} = {2 * a} across"]]')


def _parm_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    slope = b / a
    sl = f"{slope:g}"
    return (f'[[graph lines="y={sl}x" names="the path" points="({a},{b})" range="0..{max(a, b) + 2}" caption="the path — at t = 1 the ball sits at ({a}, {b}); at t = {c} it is farther along the same line"]]'
            f'[[step eq="x = {a}t · y = {b}t"]]'
            f'[[step eq="at t = {c} · distance from the start = ?"]]')


def _parm_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    h = round((a * a + b * b) ** 0.5)
    return (f"Look what you did: at {c} seconds x is {a * c} and y is {b * c} — the two legs. "
            f"The straight distance is the hypotenuse: {h * c}. Each second covers {h}, so "
            f"{h} alone is one second's worth, and {(a + b) * c} walks the corner.",
            f'[[vector v="{a * c},{b * c}" caption="at t = {c}: ({a * c}, {b * c}) — {h * c} from the start"]]'
            f'[[step eq="t = {c}: x = {a * c} · y = {b * c}"]][[step eq="√({a * c}² + {b * c}²) = {h * c}"]]')


def _gsum_terms(p):
    a, b, c = p["a"], p["b"], p["c"]
    return [a * b ** i for i in range(c)]


def _gsum_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[machine input="{a}" rule="× {b}" output="?" caption="the pattern\'s machine: each term goes in, {b} times it comes out — {c} terms, then add them all"]]'
            f'[[step eq="start {a} · times {b} each step · {c} terms"]]'
            f'[[step eq="sum = ?"]]')


def _gsum_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    t = _gsum_terms(p); tot = sum(t)
    bars = " | ".join(f"term {i + 1}:{v}" for i, v in enumerate(t))
    return (f"Look what you did: the terms are {', '.join(str(v) for v in t)} — put together, "
            f"{tot}. The last term alone is only {t[-1]}, and a pattern that never grew "
            f"would have stopped at {a * c}.",
            f'[[bars data="{bars}" caption="{" + ".join(str(v) for v in t)} = {tot}"]]'
            f'[[step eq="{" + ".join(str(v) for v in t)} = {tot}"]]')


def _sigm_board(p):
    a, b = p["a"], p["b"]
    return (f'[[machine input="k" rule="{a}k" output="?" caption="the recipe: k goes in, {a} times k comes out — run k from 1 to {b}, then put every result together"]]'
            f'[[step eq="Σ (k from 1 to {b}) of {a}k = ?"]]')


def _sigm_worked(p):
    a, b = p["a"], p["b"]
    bare = b * (b + 1) // 2; tot = a * bare
    bars = " | ".join(f"k={k}:{a * k}" for k in range(1, b + 1))
    return (f"Look what you did: every term carries the {a}, so pull it out front. 1 up to "
            f"{b} sums to {bare}, and {a} times {bare} equals {tot}. The bare sum {bare} "
            f"forgot the {a}, and {a * b} is only the last term.",
            f'[[bars data="{bars}" caption="{b} terms, each {a} times its k — {a} × {bare} = {tot}"]]'
            f'[[step eq="1 + 2 + … + {b} = {bare}"]][[step eq="{a} × {bare} = {tot}"]]')


def _pasc_board(p):
    a, b = p["a"], p["b"]
    return (f'[[array rows="1" cols="{a}" caption="{a} people in a row — choose {b}; the order they are picked in does not matter"]]'
            f'[[step eq="choose {b} from {a} · order does not matter"]]'
            f'[[step eq="teams = ?"]]')


def _pasc_worked(p):
    a, b = p["a"], p["b"]
    npr, f, ncr = _npr(a, b), _fact(b), _ncr(a, b)
    return (f"Look what you did: picking in order would give {npr} line-ups, but every "
            f"team of {b} shows up {f} times in that list — once per order. Divide: {npr} "
            f"divided by {f} equals {ncr} teams.",
            f'[[bars data="line-ups:{npr} | teams:{ncr}" caption="{npr} line-ups ÷ {f} orders = {ncr} teams"]]'
            f'[[step eq="{npr} ÷ {f} = {ncr} teams"]]')


def _gser_board(p):
    a = p["a"]
    return (f'[[bars data="1st bounce:{a} | 2nd:{a // 2} | 3rd:{a // 4}" caption="the bounces halve forever — how far in all?"]]'
            f'[[step eq="{a} + {a // 2} + {a // 4} + … forever"]]'
            f'[[step eq="in all = ?"]]')


def _gser_worked(p):
    a = p["a"]
    hops = ",".join(f"{v:g}" for v in (0, a, a * 1.5, a * 1.75, a * 1.875))
    return (f"Look what you did: add forever and it still settles. {a} plus {a // 2} plus "
            f"{a // 4}, on and on, closes in on {2 * a} — twice the first bounce, and never "
            f"a foot more. Each hop covers half of what is left.",
            f'[[numberline min="0" max="{2 * a}" hops="{hops}" points="{2 * a}" caption="each hop covers half of what is left — in all, {2 * a}"]]'
            f'[[step eq="{a} + {a // 2} + {a // 4} + … → {2 * a}"]]')


def _lsub_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[graph lines="y={b}x+{c}" range="0..{a + 3}" caption="y = {b}x + {c} — a line that never breaks; creep toward x = {a}"]]'
            f'[[step eq="y = {b}x + {c}"]]'
            f'[[step eq="x → {a} · y → ?"]]')


def _lsub_worked(p):
    a, b, c = p["a"], p["b"], p["c"]; v = a * b + c
    return (f"Look what you did: nothing breaks at x equals {a}, so the value walks in with "
            f"x — {b} times {a} is {a * b}, plus {c} is {v}. For a line, the limit is "
            f"simply where the line already is.",
            f'[[graph lines="y={b}x+{c}" points="({a},{v})" range="0..{a + 3}" caption="walk x in to {a} — y walks in to {v}"]]'
            f'[[step eq="{b} × {a} + {c} = {v}"]]')


def _lhol_board(p):
    a = p["a"]
    return (f'[[machine input="{a}" rule="(x² − {a * a}) ÷ (x − {a})" output="jammed" caption="at x = {a} the bottom is zero — the machine jams; where was y headed?"]]'
            f'[[step eq="y = (x² − {a * a}) ÷ (x − {a})"]]'
            f'[[step eq="x → {a} · y → ?"]]')


def _lhol_worked(p):
    a = p["a"]
    return (f"Look what you did: everywhere except {a}, that fraction quietly equals x plus "
            f"{a} — a straight line with one hole. As x creeps toward {a}, y creeps toward "
            f"{2 * a}. The function never reaches it; the limit says where it was headed.",
            f'[[graph func="(x^2-{a * a})/(x-{a})" hole="{a}" range="{a - 3}..{a + 3}" yrange="{2 * a - 6}..{2 * a + 6}" caption="a straight line with a hole at x = {a} — headed for {2 * a}"]]'
            f'[[step eq="(x − {a})(x + {a}) ÷ (x − {a}) = x + {a}"]][[step eq="x → {a} · y → {2 * a}"]]')


def _lsid_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    side = "left" if c == 0 else "right"
    return (f'[[graph func="{a} for x<6; {b} for x>=6" range="0..12" yrange="0..{max(a, b) + 4}" caption="a step at 6 — come in from the {side}"]]'
            f'[[step eq="x < 6: y = {a} · x ≥ 6: y = {b}"]]'
            f'[[step eq="from the {side} · y → ?"]]')


def _lsid_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    if c == 0:
        spoken = (f"Look what you did: from the left, every x you pass is below 6, so y "
                  f"reads {a} the whole way in — the limit from that side is {a}. The other "
                  f"side would say {b}, and the two do not have to agree.")
        pts, v, side = f"(3,{a}),(4,{a}),(5,{a})", a, "left"
    else:
        spoken = (f"Look what you did: from the right, every x you pass is 6 or more, so y "
                  f"reads {b} the whole way in — the limit from that side is {b}. The other "
                  f"side would say {a}, and the two do not have to agree.")
        pts, v, side = f"(9,{b}),(8,{b}),(7,{b})", b, "right"
    return (spoken,
            f'[[graph func="{a} for x<6; {b} for x>=6" points="{pts}" range="0..12" yrange="0..{max(a, b) + 4}" caption="coming in from the {side}, y reads {v} all the way"]]'
            f'[[step eq="from the {side} → {v}"]]')


def _avgr_board(p):
    a, b = p["a"], p["b"]
    return (f'[[graph func="x^2" lines="x={a}; x={b}" range="0..{b + 1}" yrange="0..{b * b + 10}" caption="y = x² — the window from x = {a} to x = {b}"]]'
            f'[[step eq="y = x² · x from {a} to {b}"]]'
            f'[[step eq="rise per step of x = ?"]]')


def _avgr_worked(p):
    a, b = p["a"], p["b"]
    rise, run, r = b * b - a * a, b - a, a + b
    return (f"Look what you did: y climbs from {a * a} to {b * b} — a rise of {rise} — while "
            f"x moves {run}. Divide: {r} per step, which is simply {a} plus {b}. The rise "
            f"alone and the run alone are only halves of the story.",
            f'[[graph func="x^2" lines="y={r}x-{a * b}" points="({a},{a * a}),({b},{b * b})" range="0..{b + 1}" yrange="0..{b * b + 10}" caption="the straight line through the two points climbs {r} per step"]]'
            f'[[step eq="rise {rise} ÷ run {run} = {r}"]][[step eq="{a} + {b} = {r}"]]')



# ---- (tr, 2026-09-06) PROBSTAT UNITS 1-3: the dot plot with its stacks, the line
# and the dots past it, the histogram's bars, the stray dot, the even list with its
# two middles, the box, the four distances as bars, the hundred square for a
# percentile, the scatter cloud, the rate machine, predicted beside actual, the
# dots split by the line. Every ask draws its question with the answer withheld;
# every walk-back draws it filled in.
def _dotm_board(p):
    return (f'[[dotplot values="{_dotmode(p)}" caption="one dot per value — find the tallest stack and read the number under it"]]'
            f'[[step eq="the mode = ?"]]')


def _dotm_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: the tallest stack sits over {a}, {b} dots high — so {b} "
            f"students read {a} books each. The mode is the value UNDER the stack, {a}. "
            f"Read down to the number line, never across to how many.",
            f'[[dotplot values="{_dotmode(p)}" caption="the tallest stack, {b} dots, stands over {a} — the mode is {a}"]]'
            f'[[step eq="tallest stack over {a}"]][[step eq="mode = {a}"]]')


def _dcnt_board(p):
    a = p["a"]
    return (f'[[dotplot values="{_dotcut(p)}" caption="one dot per player — count only the dots to the RIGHT of {a}; the dot standing on {a} stays out"]]'
            f'[[step eq="more than {a} · count = ?"]]')


def _dcnt_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: count only the dots to the right of {a} — there are {b}. "
            f"The dot standing exactly on {a} does not join them, because {a} is not more "
            f"than {a}, and the {c} dots below answer the opposite question.",
            f'[[dotplot values="{_dotcut(p)}" caption="{b} dots past {a}; the one on {a} stays out"]]'
            f'[[step eq="more than {a} = {b}"]]')


def _htot_board(p):
    return (f'[[histogram values="{_histvals(p)}" caption="each bar carries its count — add the counts for how many in all"]]'
            f'[[step eq="in all = ?"]]')


def _htot_worked(p):
    a, b, c = p["a"], p["b"], p["c"]; t = a + b + c
    return (f"Look what you did: add the bars — {a} plus {b} plus {c} equals {t} scores in "
            f"all. The tallest bar alone holds only {max(a, b, c)}, and the number of "
            f"bars is not the number of scores.",
            f'[[histogram values="{_histvals(p)}" caption="{a} + {b} + {c} = {t} in all"]]'
            f'[[step eq="{a} + {b} + {c} = {t}"]]')


def _farv_board(p):
    return (f'[[dotplot values="{_farlist(p)}" caption="one dot per student — one dot sits far from the crowd; read the number under it"]]'
            f'[[step eq="the outlier = ?"]]')


def _farv_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: nearly every dot crowds around {a}, and one sits alone out "
            f"at {b} — that stray is the outlier. {a} is where the crowd is, and {b - a} is "
            f"only how far the stray sits from it.",
            f'[[dotplot values="{_farlist(p)}" caption="the crowd near {a}; the stray at {b} — the outlier is {b}"]]'
            f'[[step eq="outlier = {b}"]]')


def _medv_board(p):
    n = 2 * p["a"]
    return (f'[[dotplot values="{",".join(str(v) for v in _evenlist(p))}" caption="{n} numbers — count in from both ends and two middles face each other"]]'
            f'[[step eq="{n} numbers · no single middle · median = ?"]]')


def _medv_worked(p):
    a, b = p["a"], p["b"]; lo, hi, m = b, b + 2, b + 1
    vals = _evenlist(p)
    return (f"Look what you did: {2 * a} numbers, so {a} sit either side and the middles "
            f"are {lo} and {hi}. The median is halfway between them: {lo} plus {hi} is "
            f"{lo + hi}, halved is {m}. Neither middle on its own will do.",
            f'[[numberline min="{vals[0] - 1}" max="{vals[-1] + 1}" points="{lo},{hi}" mid="{m}" caption="the two middles, {lo} and {hi} — halfway between them is {m}"]]'
            f'[[step eq="({lo} + {hi}) ÷ 2 = {m}"]]')


def _iqrw_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[boxplot five="{a - c},{a},{(a + b) // 2},{b},{b + c}" caption="the box is the middle half — one edge at {a}, the other at {b}; the whiskers reach the extremes"]]'
            f'[[step eq="box width = ?"]]')


def _iqrw_worked(p):
    a, b, c = p["a"], p["b"], p["c"]; w = b - a
    return (f"Look what you did: the box holds the middle half, from {a} to {b} — {b} take "
            f"away {a} equals {w}. Whisker tip to whisker tip is {b + c - (a - c)}, the "
            f"whole stretch, a different measurement; and {b} alone is just the right edge.",
            f'[[boxplot five="{a - c},{a},{(a + b) // 2},{b},{b + c}" caption="the box runs {a} to {b} — {w} wide"]]'
            f'[[step eq="{b} − {a} = {w}"]]')


def _madv_board(p):
    a = p["a"]
    return (f'[[dotplot values="{",".join(str(v) for v in _madlist(p))}" caption="four numbers with their mean at {a} — how far does each sit from it?"]]'
            f'[[step eq="mean {a} · average distance = ?"]]')


def _madv_worked(p):
    a, b = p["a"], p["b"]
    vals = _madlist(p)
    bars = " | ".join(f"{v}:{abs(v - a)}" for v in vals)
    return (f"Look what you did: the four distances from {a} are {3 * b}, {b}, {b} and "
            f"{3 * b} — put together {8 * b}, shared between 4: {2 * b}. The farthest sits "
            f"{3 * b} away and the nearest {b}, so the average distance lies between them.",
            f'[[bars data="{bars}" caption="each number\'s distance from the mean — {8 * b} in all, shared four ways: {2 * b}"]]'
            f'[[step eq="{3 * b} + {b} + {b} + {3 * b} = {8 * b}"]][[step eq="{8 * b} ÷ 4 = {2 * b}"]]')


def _pctl_board(p):
    a, b = p["a"], p["b"]
    return (f'[[hundredgrid shaded="{b}" unit="percent" eq="{b}th percentile: {b}%" caption="a percentile is a percent of the group — {b} of every 100; the group here is {a}"]]'
            f'[[step eq="{a} others · {b}th percentile"]]'
            f'[[step eq="beaten = ?"]]')


def _pctl_worked(p):
    a, b = p["a"], p["b"]; n = a * b // 100
    return (f"Look what you did: {b} percent of {a} is {n}, so she beat {n} of them. The "
            f"{b} is a PERCENT, never a headcount — and the other {a - n} finished ahead of her.",
            f'[[bars data="beaten:{n} | ahead of her:{a - n}" caption="{b}% of {a} = {n} beaten, {a - n} ahead"]]'
            f'[[step eq="{b}% of {a} = {n}"]]')


def _spnt_board(p):
    a = p["a"]
    return (f'[[scatter points="{_scat_points(p)}" caption="each dot is one student — find {a} along the bottom, go up to the dot, then across"]]'
            f'[[step eq="at {a} hours · points = ?"]]')


def _spnt_worked(p):
    a = p["a"]; y = _scat_at(p); nxt = _scat_next(p)
    return (f"Look what you did: find {a} along the bottom, go straight up to the dot, then "
            f"straight across — {y} points. The {a} is how long the student practiced, "
            f"across, not up; and {nxt} belongs to the neighbouring dot.",
            f'[[scatter points="{_scat_points(p)}" caption="the dot at {a} hours sits level with {y} points"]]'
            f'[[step eq="{a} hours · up · across = {y} points"]]')


def _sslp_board(p):
    a, b = p["a"], p["b"]
    return (f'[[machine input="{b}" rule="× {a}" output="?" caption="the slope as a rate: {b} extra hours go in, {a} points for each of them"]]'
            f'[[step eq="{a} points per extra hour · {b} extra hours"]]'
            f'[[step eq="extra points = ?"]]')


def _sslp_worked(p):
    a, b = p["a"], p["b"]; t = a * b
    return (f"Look what you did: the slope is a rate — {a} points EACH hour, so {b} hours "
            f"brings {b} times {a}, {t} points. {a} alone is one hour's worth, and adding "
            f"the two numbers treats a rate like a total.",
            f'[[graph lines="y={a}x" names="{a} points per hour" points="({b},{t})" range="0..{b + 2}" yrange="0..{t + 10}" caption="the line climbs {a} every hour — {b} hours up is {t} points"]]'
            f'[[step eq="{a} × {b} = {t}"]]')


def _resd_board(p):
    a, b = p["a"], p["b"]
    return (f'[[bars data="predicted:{a} | actual:{b}" caption="the line said {a}, the student scored {b} — the gap between the bars is the residual"]]'
            f'[[step eq="predicted {a} · actual {b}"]]'
            f'[[step eq="how far off = ?"]]')


def _resd_worked(p):
    a, b = p["a"], p["b"]; g = abs(b - a)
    lo, hi = min(a, b), max(a, b)
    way = "low" if b > a else "high"
    return (f"Look what you did: the gap between {a} and {b} is {g} — the line guessed "
            f"{g} points {way}. That gap is the residual, and every dot has one. {b} is "
            f"what the student scored, not how far the line missed by.",
            f'[[numberline min="{max(0, lo - 5)}" max="{hi + 5}" hops="{a},{b}" caption="from predicted {a} to actual {b} — a gap of {g}"]]'
            f'[[step eq="{hi} − {lo} = {g}"]]')


def _sblw_board(p):
    a, b = p["a"], p["b"]
    return (f'[[tape parts="{b} above|?" total="{a} dots" caption="{a} dots, none on the line — {b} above it, the rest below"]]'
            f'[[step eq="{a} dots · {b} above the line"]]'
            f'[[step eq="below the line = ?"]]')


def _sblw_worked(p):
    a, b = p["a"], p["b"]; n = a - b
    return (f"Look what you did: the line runs THROUGH the cloud, so every dot is on one "
            f"side or the other — {a} take away {b} leaves {n} below. {b} is the side you "
            f"were told about, and {a} is every dot on the plot.",
            f'[[tape parts="{b} above|{n} below" total="{a} dots" caption="{a} − {b} = {n} below the line"]]'
            f'[[step eq="{a} − {b} = {n}"]]')



# ---- (tt, 2026-09-06) PROBSTAT UNITS 4-6: the school as bars and the sample as a
# tape cut the same way, the surveys back and silent as a tape, the asked and the
# never-asked, the people machine that quadruples, the bag as bars and the chance
# on the hundred square, the three piles joined, two pies for two chances and the
# array of days by buses, the spinner as a pie and the tree of paths, the four
# groups as bars and the two-way table, the girls' share on the hundred square, the
# school beside the group, the bag before and after a marble is kept. Every ask
# draws its question with the answer withheld; every walk-back draws it filled in.
def _strf_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[bars data="girls:{a} | boys:{b}" caption="the school — {a} girls and {b} boys; the sample keeps this mix"]]'
            f'[[tape parts="? girls|? boys" total="sample of {c}" caption="the sample of {c}, cut the way the school is"]]'
            f'[[step eq="school: {a} girls · {b} boys"]]'
            f'[[step eq="sample of {c} · girls = ?"]]')


def _strf_worked(p):
    a, b, c = p["a"], p["b"], p["c"]; g = c * a // (a + b)
    return (f"Look what you did: girls are {a} of the {a + b} in the school, so the sample "
            f"keeps that share — {c} times {a}, divided by {a + b}, is {g} girls, leaving "
            f"{c - g} boys. Half and half would give {c // 2}, which matches only a school "
            f"that is half and half, and {a} copies the school's own count into the sample.",
            f'[[tape parts="{g} girls|{c - g} boys" total="sample of {c}" caption="{g} girls and {c - g} boys — the school\'s mix, {a} to {b}, inside {c}"]]'
            f'[[step eq="{c} × {a} ÷ {a + b} = {g} girls"]]')


def _resp_board(p):
    a, b = p["a"], p["b"]
    return (f'[[tape parts="{b} back|{a - b} silent" total="{a} sent" caption="{a} surveys went out — {b} came back and the rest stayed silent"]]'
            f'[[step eq="{b} back out of {a} sent"]]'
            f'[[step eq="percent returned = ?"]]')


def _resp_worked(p):
    a, b = p["a"], p["b"]; r = 100 * b // a
    return (f"Look what you did: {b} out of {a} is {r} percent — the response rate. {b} is "
            f"a count of surveys and {a - b} is how many never came back; the rate is the "
            f"percent, and a low one warns that the silent may not think like the answerers.",
            f'[[hundredgrid shaded="{r}" unit="percent" eq="{b} of {a} → {r}%" caption="{r} of every 100 surveys came back"]]'
            f'[[step eq="{b} ÷ {a} = {r}%"]]')


def _bias_board(p):
    a, b = p["a"], p["b"]
    return (f'[[tape parts="{a} asked|?" total="school of {b}" caption="the {a} in the cafeteria were handed the survey — the rest of the school never was"]]'
            f'[[step eq="asked: {a} in the cafeteria · school: {b}"]]'
            f'[[step eq="never had a chance = ?"]]')


def _bias_worked(p):
    a, b = p["a"], p["b"]; n = b - a
    return (f"Look what you did: {b} take away {a} leaves {n} who never had a chance — not "
            f"{n} who said no, {n} who were never asked at all. {a} is the crowd that WAS "
            f"asked and {b} is everyone; the gap between them is the survey's blind spot.",
            f'[[tape parts="{a} asked|{n} never asked" total="school of {b}" caption="{b} − {a} = {n} never had a chance"]]'
            f'[[step eq="{b} − {a} = {n}"]]')


def _merr_board(p):
    a, b = p["a"], p["b"]
    return (f'[[machine input="{a}" rule="× 4" output="?" caption="four times the people halves the margin — {a} people go in, the new headcount comes out"]]'
            f'[[step eq="{a} people · margin {b} points"]]'
            f'[[step eq="half the margin · people = ?"]]')


def _merr_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: four times {a} is {4 * a} people. Doubling to {2 * a} does "
            f"not halve the margin — it only shaves it — and {b} is the margin itself, not a "
            f"headcount. Every extra bit of certainty costs far more people than the last.",
            f'[[bars data="now:{a} | four times:{4 * a}" caption="{a} people to {4 * a} — and the margin of {b} points halves"]]'
            f'[[step eq="{a} × 4 = {4 * a}"]]')


def _ppct_board(p):
    a, b = p["a"], p["b"]
    return (f'[[bars data="red:{a} | not red:{b - a}" caption="{b} marbles in the bag, {a} of them red — the chance of red, as a percent"]]'
            f'[[step eq="{a} red out of {b} marbles"]]'
            f'[[step eq="percent chance of red = ?"]]')


def _ppct_worked(p):
    a, b = p["a"], p["b"]; r = 100 * a // b
    return (f"Look what you did: {a} out of {b} is {r} percent — a chance on the scale from "
            f"0, never, to 100, always. {a} is a count of marbles and {b - a} is how many are "
            f"not red; the question asked for the percent.",
            f'[[hundredgrid shaded="{r}" unit="percent" eq="{a} of {b} → {r}%" caption="{r} of every 100 picks would be red"]]'
            f'[[step eq="{a} ÷ {b} = {r}%"]]')


def _por_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[bars data="red:{a} | blue:{b} | green:{c}" caption="three piles — red OR blue wins, and a marble cannot be two colours at once"]]'
            f'[[step eq="red OR blue wins · winners = ?"]]')


def _por_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: a marble cannot be red and blue at once, so the two piles "
            f"join — {a} plus {b} is {a + b} winners out of {a + b + c}. Timesing gives "
            f"{a * b}, which counts pairs of marbles, and {a + b + c} counts the green losers in.",
            f'[[tape parts="{a} red|{b} blue|{c} green" total="{a + b + c} marbles" caption="the red and blue parts side by side — {a + b} winners"]]'
            f'[[step eq="{a} + {b} = {a + b}"]]')


def _pand_board(p):
    a, b = p["a"], p["b"]
    return (f'[[pie parts="{a}" shaded="1" caption="one day in {a} is rainy"]]'
            f'[[pie parts="{b}" shaded="1" caption="one bus in {b} is late — neither cares what the other does"]]'
            f'[[step eq="rain: 1 in {a} · late bus: 1 in {b}"]]'
            f'[[step eq="both = 1 in ?"]]')


def _pand_worked(p):
    a, b = p["a"], p["b"]; t = a * b
    return (f"Look what you did: one day in {a} is rainy, and on that day one bus in {b} is "
            f"late. So both together turn up one time in {a} times {b} — one in {t}. Wanting "
            f"both is rarer, never one in {a + b}, and never one in {max(a, b)} on its own.",
            f'[[array rows="{min(a, b)}" cols="{max(a, b)}" caption="{a} kinds of day by {b} kinds of bus — {t} squares, and only one is rainy AND late"]]'
            f'[[step eq="{a} × {b} = {t}"]]')


def _ptre_board(p):
    a, b = p["a"], p["b"]
    return (f'[[pie parts="{a}" shaded="{b}" caption="{a} equal parts, {b} of them winners — spun twice"]]'
            f'[[step eq="{b} winners of {a} parts · spun twice"]]'
            f'[[step eq="paths that win twice = ?"]]')


def _ptre_worked(p):
    a, b = p["a"], p["b"]; t = b * b
    return (f"Look what you did: each of the {b} winning first spins can be followed by each "
            f"of the {b} winning second spins. So {b} times {b} is {t} paths that win both "
            f"times, out of {a * a}. {b * a} leaves the second spin free, and {2 * b} adds "
            f"two spins together.",
            f'[[tree stage1="W:{b},L:{a - b}" stage2="W:{b},L:{a - b}" caption="every path, stage by stage — the win-then-win path counts {b} × {b}"]]'
            f'[[step eq="{b} × {b} = {t}"]]')


def _cbse_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[bars data="girls soccer:{a} | girls art:{b} | boys soccer:{c} | boys art:{c + 3}" caption="four groups — the question asks about the girls only"]]'
            f'[[step eq="girls: {a} soccer, {b} art · boys: {c} soccer, {c + 3} art"]]'
            f'[[step eq="among the girls · out of ?"]]')


def _cbse_worked(p):
    a, b, c = p["a"], p["b"], p["c"]; g = a + b; t = 2 * c + 3 + a + b
    return (f"Look what you did: asking about the girls only sends the boys away — {a} plus "
            f"{b} is {g} girls, so every chance from here is out of {g}. The whole class of "
            f"{t} answers a different question, and {a} alone is the soccer girls.",
            f'[[twoway rowlabels="girls,boys" collabels="soccer,art" data="{a},{b}|{c},{c + 3}" caption="the girls\' row adds to {g} — that is the whole now"]]'
            f'[[step eq="{a} + {b} = {g}"]]')


def _ccnt_board(p):
    a, b = p["a"], p["b"]
    return (f'[[bars data="soccer:{a} | art:{b}" caption="every girl chose one club — {a} soccer, {b} art; the soccer share of the girls, as a percent"]]'
            f'[[step eq="girls: {a} soccer · {b} art"]]'
            f'[[step eq="percent of the girls in soccer = ?"]]')


def _ccnt_worked(p):
    a, b = p["a"], p["b"]; g = a + b; r = 100 * a // g
    return (f"Look what you did: the girls are the whole world now — {a} plus {b} is {g} — "
            f"and {a} of them chose soccer: {r} percent. The other {100 - r} percent is the "
            f"art share, and {a} is a headcount, not a percent.",
            f'[[hundredgrid shaded="{r}" unit="percent" eq="{a} of {g} → {r}%" caption="{r} of every 100 girls chose soccer"]]'
            f'[[step eq="{a} + {b} = {g}"]][[step eq="{a} ÷ {g} = {r}%"]]')


def _indp_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[bars data="whole school:{a} | the {b} left-handers:{c}" caption="percent who like maths — the whole school, and the left-handers as measured"]]'
            f'[[step eq="whole school: {a}% · left-handers: {c}%"]]'
            f'[[step eq="if independent, left-handers = ?%"]]')


def _indp_worked(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f"Look what you did: independent means the left-handers would look just like the "
            f"school — {a} percent, whether there are {b} of them or 200. They came in at "
            f"{c}, so the two are not independent, and {b} is a headcount, not a rate.",
            f'[[bars data="school:{a} | if independent:{a} | measured:{c}" caption="independence predicts {a}% — the measured {c}% breaks the promise"]]'
            f'[[step eq="if independent: {a}%"]]')


def _wout_board(p):
    a, b = p["a"], p["b"]
    return (f'[[tape parts="{a} red|{b - a} other" total="{b} marbles" caption="one red is taken and KEPT — the next pick faces a smaller bag"]]'
            f'[[step eq="{b} marbles · {a} red · one red taken and kept"]]'
            f'[[step eq="next pick · out of ?"]]')


def _wout_worked(p):
    a, b = p["a"], p["b"]
    return (f"Look what you did: the marble did not go back, so the bag is smaller — {b} take "
            f"away 1 leaves {b - 1}. The reds shrank too, to {a - 1}, but that is the top of "
            f"the chance, not the bottom; answering {b} forgets that anything was taken at all.",
            f'[[tape parts="{a - 1} red|{b - a} other" total="{b - 1} marbles" caption="{b} − 1 = {b - 1} marbles left for the next pick"]]'
            f'[[step eq="{b} − 1 = {b - 1}"]]')



# ---- (ty, 2026-09-07) PROBSTAT UNITS 7-9: the chances on the hundred square and the
# three prizes as bars; the paying plays on the hundred square and the two piles of
# tokens as bars; the wins on the hundred square and the pot shared by a machine; what
# you pay beside what comes back as bars, the gap as a tape; the middle band of the
# bell and the 68 on the hundred square; the mean and the value on a number line with
# no hops on the ask and the hops of one deviation on the walk-back; one hop shown and
# two walked; the top sliver of the bell and the three parts of the group as a tape;
# the estimate on a number line and the step down as a hop; the two halves of the doubt
# as a tape; the estimate, the ceiling and the claim on one line and the gap as a hop;
# the low end as bars and the people machine. Every ask draws its question with the
# answer withheld; every walk-back draws it filled in.
def _pdis_board(p):
    a, b = p["a"], p["b"]
    return (f'[[hundredgrid shaded="{a}" plus="{b}" unit="percent" caption="small takes {a} of the hundred and medium {b} more — large is every cell still white"]]'
            f'[[step eq="small {a}% · medium {b}%"]]'
            f'[[step eq="large = ?%"]]')


def _pdis_worked(p):
    a, b = p["a"], p["b"]; c = 100 - a - b
    return (f"Look what you did: {a} and {b} together fill {a + b} of the hundred, so large "
            f"takes the {c} that are left. Something happens every single play, and these "
            f"three are the only doors. {a + b} is the two you were given, not the one "
            f"asked for, and 100 is all three together.",
            f'[[bars data="small:{a} | medium:{b} | large:{c}" caption="three prizes that fill the hundred between them — {a}, {b} and {c}"]]'
            f'[[step eq="100 − {a} − {b} = {c}%"]]')


def _evwa_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[hundredgrid shaded="{c}" unit="percent" caption="of every 100 plays, the {c} shaded pay {a} tokens and the white ones pay {b}"]]'
            f'[[step eq="{a} tokens on {c} plays · {b} tokens on {100 - c}"]]'
            f'[[step eq="one play is worth ? on average"]]')


def _evwa_worked(p):
    a, b, c = p["a"], p["b"], p["c"]; big = a * c; small = b * (100 - c); v = (big + small) // 100
    return (f"Look what you did: {c} plays at {a} tokens is {big}, and {100 - c} plays at "
            f"{b} is {small}. Together that is {big + small} tokens across 100 plays, so one "
            f"play is worth {v}. The plain average, {(a + b) // 2}, would need both prizes "
            f"to come up equally often.",
            f'[[bars data="{c} plays × {a}:{big} | {100 - c} plays × {b}:{small}" caption="two piles of tokens — {big} from the big prize, {small} from the small — {big + small} in all"]]'
            f'[[step eq="{big} + {small} = {big + small}"]]'
            f'[[step eq="{big + small} ÷ 100 = {v} a play"]]')


def _fair_board(p):
    a, b = p["a"], p["b"]
    return (f'[[hundredgrid shaded="{b}" unit="percent" caption="{b} of every 100 plays win — and all 100 of them pay {a} tokens"]]'
            f'[[step eq="{a} tokens a play · win {b} of 100"]]'
            f'[[step eq="fair prize = ?"]]')


def _fair_worked(p):
    a, b = p["a"], p["b"]; pot = 100 * a; prize = pot // b
    return (f"Look what you did: 100 plays at {a} tokens each is {pot} tokens paid in, and "
            f"only {b} of those plays win. Fair means the whole {pot} comes back across "
            f"those {b} wins — {pot} shared by {b} is {prize} a prize. Just your stake "
            f"back, {a}, still loses you every play you do not win.",
            f'[[machine input="{pot}" rule="÷ {b}" output="{prize}" caption="the pot of {pot} shared over {b} wins — {prize} tokens a prize"]]'
            f'[[step eq="{pot} ÷ {b} = {prize}"]]')


def _hedg_board(p):
    a, b = p["a"], p["b"]
    return (f'[[bars data="you pay:{a} | comes back:{b}" caption="every play: {a} tokens out, {b} back on average — the gap between the bars is the real cost"]]'
            f'[[step eq="pay {a} · get back {b} on average"]]'
            f'[[step eq="real cost per play = ?"]]')


def _hedg_worked(p):
    a, b = p["a"], p["b"]; g = a - b
    return (f"Look what you did: {a} out and {b} back leaves {g} tokens gone on every play. "
            f"That gap hides inside any single play and shows up with perfect reliability "
            f"over hundreds — it is how the machine stays open. {b} is what comes back, "
            f"and adding the two is nothing a play ever costs.",
            f'[[tape parts="{b} back|{g} gone" total="{a} paid" caption="of the {a} you pay, {b} comes back and {g} is gone for good"]]'
            f'[[step eq="{a} − {b} = {g}"]]')


def _n68_board(p):
    a = p["a"]
    return (f'[[normal mean="100" sd="10" lo="90" hi="110" caption="the middle band, one deviation each way — about 68 of every 100 sit inside it"]]'
            f'[[step eq="{a} in the group · about 68% in the middle band"]]'
            f'[[step eq="the middle band holds ?"]]')


def _n68_worked(p):
    a = p["a"]; n = 68 * a // 100
    return (f"Look what you did: 68 percent of {a} is {n} — that is how many of the group "
            f"sit no further than one deviation from the middle. The 68 is a percent and "
            f"never a headcount, and {a} is everybody, middle and ends together.",
            f'[[hundredgrid shaded="68" unit="percent" eq="68% of {a} → {n}" caption="68 of every 100 — and 68 percent of {a} is {n}"]]'
            f'[[step eq="68% of {a} = {n}"]]')


def _zsco_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[numberline min="{a - b}" max="{c + b}" points="{a},{c}" caption="the mean at {a} and the value at {c} — the gap between them, measured in steps of {b}"]]'
            f'[[step eq="mean {a} · one deviation {b} · value {c}"]]'
            f'[[step eq="deviations above the mean = ?"]]')


def _zsco_worked(p):
    a, b, c = p["a"], p["b"], p["c"]; k = (c - a) // b
    hops = ",".join(str(a + i * b) for i in range(k + 1))
    return (f"Look what you did: {c} sits {c - a} above the mean, and each deviation is a "
            f"step of {b} — so that gap holds {k} of them. Counting steps instead of raw "
            f"units is what lets a height and a test score be compared at all. {c - a} is "
            f"the raw gap, and {b} is one step.",
            f'[[numberline min="{a - b}" max="{c + b}" points="{a},{c}" hops="{hops}" caption="{k} hops of {b} carry the mean at {a} up to {c}"]]'
            f'[[step eq="({c} − {a}) ÷ {b} = {k} deviations"]]')


def _zval_board(p):
    a, b = p["a"], p["b"]
    return (f'[[numberline min="{a - b}" max="{a + 3 * b}" points="{a}" hops="{a},{a + b}" caption="one deviation is one hop of {b} from the mean at {a} — two deviations is two hops"]]'
            f'[[step eq="mean {a} · one deviation {b}"]]'
            f'[[step eq="two deviations above the mean = ?"]]')


def _zval_worked(p):
    a, b = p["a"], p["b"]; v = a + 2 * b
    return (f"Look what you did: two deviations is {b} twice — {2 * b} — and the distance "
            f"starts from the mean, so {a} plus {2 * b} is {v}. {a + b} is one hop only, "
            f"and {2 * b} is the distance with nowhere to start from.",
            f'[[numberline min="{a - b}" max="{a + 3 * b}" points="{a},{v}" hops="{a},{a + b},{v}" caption="two hops of {b} from {a} land on {v}"]]'
            f'[[step eq="{a} + 2 × {b} = {v}"]]')


def _ntal_board(p):
    a = p["a"]
    return (f'[[normal mean="100" sd="10" lo="120" hi="140" caption="the top end — the sliver beyond two deviations, about 2 or 3 of every 100"]]'
            f'[[step eq="{a} in the group · 95% no further than two deviations"]]'
            f'[[step eq="the top end holds ?"]]')


def _ntal_worked(p):
    a = p["a"]; ends = a // 20; top = a // 40
    return (f"Look what you did: 5 percent of {a} is {ends} out at the ends, and the bell "
            f"is symmetric, so they split evenly — {top} above two deviations and {top} "
            f"below. {ends} counts both ends when the question asked for one.",
            f'[[tape parts="{top} bottom end|{a - ends} middle|{top} top end" total="{a} in all" caption="the two ends hold {ends} between them — {top} at each"]]'
            f'[[step eq="{a} ÷ 40 = {top}"]]')


def _cint_board(p):
    a, b = p["a"], p["b"]
    return (f'[[numberline min="{a - 2 * b}" max="{a + 2 * b}" points="{a}" caption="the estimate at {a} — the margin of {b} reaches the same distance each way"]]'
            f'[[step eq="{a}% · give or take {b}"]]'
            f'[[step eq="lowest possible = ?"]]')


def _cint_worked(p):
    a, b = p["a"], p["b"]; lo = a - b
    return (f"Look what you did: give or take {b} means {b} either way, so the low end is "
            f"{a} take away {b} — {lo} percent. {a + b} is the high end, the same step in "
            f"the other direction, and {b} on its own is only the size of the step.",
            f'[[numberline min="{a - 2 * b}" max="{a + 2 * b}" points="{lo},{a},{a + b}" hops="{a},{lo}" caption="one step of {b} down from {a} lands on {lo}"]]'
            f'[[step eq="{a} − {b} = {lo}"]]')


def _cwid_board(p):
    a, b = p["a"], p["b"]
    return (f'[[tape parts="{b} down|{b} up" total="?" caption="the doubt reaches {b} below {a} and {b} above it — the whole range is both parts together"]]'
            f'[[step eq="{a}% · give or take {b}"]]'
            f'[[step eq="lowest to highest = ? points"]]')


def _cwid_worked(p):
    a, b = p["a"], p["b"]; w = 2 * b
    return (f"Look what you did: the range runs {b} below and {b} above, so it is {b} twice "
            f"— {w} points wide, from {a - b} to {a + b}. The margin {b} is one side of the "
            f"middle, and {a} is the middle itself.",
            f'[[tape parts="{b} down|{b} up" total="{w} points wide" caption="{b} and {b} — the whole range from {a - b} to {a + b} is {w} points across"]]'
            f'[[step eq="{b} × 2 = {w}"]]')


def _inci_board(p):
    a, b, c = p["a"], p["b"], p["c"]; top = a + b
    return (f'[[numberline min="{a - b - 2}" max="{c + 2}" points="{a},{top},{c}" caption="your estimate at {a}, your ceiling at {top}, their claim at {c} — measure from the ceiling"]]'
            f'[[step eq="your range tops out at {top}%"]]'
            f'[[step eq="their claim {c}% · points past the ceiling = ?"]]')


def _inci_worked(p):
    a, b, c = p["a"], p["b"], p["c"]; top = a + b; g = c - top
    return (f"Look what you did: your range reaches {top} at the very most, and they claim "
            f"{c} — that is {g} points past anything your poll can support. Measuring from "
            f"{a} instead gives {c - a} and pretends your estimate is exact, and {b} is the "
            f"size of your doubt, not the size of the disagreement.",
            f'[[numberline min="{a - b - 2}" max="{c + 2}" points="{a},{top},{c}" hops="{top},{c}" caption="one hop of {g} from the ceiling at {top} reaches their claim at {c}"]]'
            f'[[step eq="{c} − {top} = {g}"]]')


def _npop_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[bars data="low end:{a - b} | estimate:{a} | high end:{a + b}" caption="three percents — the low end {a - b}, the estimate {a}, the high end {a + b} — of a school of {c}"]]'
            f'[[step eq="{a}% of {c} · give or take {b}"]]'
            f'[[step eq="the low end, in people = ?"]]')


def _npop_worked(p):
    a, b, c = p["a"], p["b"], p["c"]; lo = a - b; n = lo * c // 100
    return (f"Look what you did: the low end of the range is {lo} percent, and {lo} percent "
            f"of {c} is {n}. Using {a} percent gives {a * c // 100} and quietly drops the "
            f"give-or-take — a sample that does not know exactly should never be reported "
            f"as though it did.",
            f'[[machine input="{c}" rule="× {lo}%" output="{n}" caption="the whole school of {c} goes in, the low end\'s {lo} percent comes out — {n}"]]'
            f'[[step eq="{lo}% of {c} = {n}"]]')




# ---- (tz, 2026-09-07) CALCULUS UNITS 1-3: two curves closing on their limits at x = 4
# and the product curve closing on theirs; the fraction flattening toward a number as x
# grows, the asymptote drawn only on the walk-back; two shelves with the open and the
# closed dot at the border, the leap measured on the walk-back; the sloping piece and the
# flat piece that do not meet, and the mended curve; the parabola with its point, the
# tangent drawn only on the walk-back; the exponent as the input of a MACHINE that meets
# the front number; the line with its one slope, the step-and-climb on the walk-back; the
# curve with its point and the tangent at it; the product curve and its tangent; the
# power and the inside as a machine; the composed curve at zero and its tangent; the
# front number through the doubling-and-dividing machine. Every ask draws its question
# with the answer withheld; every walk-back draws it filled in.
def _llaw_board(p):
    a, b = p["a"], p["b"]; top = max(a, b) + 3
    return (f'[[graph func="{a} + (x-4)^2/8; {b} - (x-4)^2/8" hole="4" lines="x=4" names="f; g" range="0..8" yrange="0..{top}" caption="f closes on {a} at x = 4 and g closes on {b} — their product closes on a number too"]]'
            f'[[step eq="f → {a} · g → {b}"]]'
            f'[[step eq="f × g → ?"]]')


def _llaw_worked(p):
    a, b = p["a"], p["b"]; t = a * b
    return (f"Look what you did: f is heading for {a} and g for {b}, and the limit passes "
            f"straight through the times sign — {a} times {b} is {t}, so f times g heads "
            f"for {t}. Adding would give {a + b}, which answers a different question, and "
            f"{max(a, b)} is only the bigger of the two.",
            f'[[graph func="({a} + (x-4)^2/8)*({b} - (x-4)^2/8)" hole="4" lines="x=4" names="f × g" range="0..8" yrange="0..{t + 6}" caption="the product curve closes on {t} at x = 4 — {a} times {b}"]]'
            f'[[step eq="{a} × {b} = {t}"]]')


def _linf_board(p):
    a, b = p["a"], p["b"]; c = a // b
    return (f'[[graph func="({a}*x^2)/({b}*x^2 + {b})" names="y = {a}x² / ({b}x² + {b})" range="0..12" yrange="0..{c + 2}" caption="{a} x squared over {b} x squared — as x grows the curve flattens toward one number"]]'
            f'[[step eq="y = {a}x² ÷ {b}x²"]]'
            f'[[step eq="x grows huge · y → ?"]]')


def _linf_worked(p):
    a, b = p["a"], p["b"]; c = a // b
    return (f"Look what you did: the x squareds grow at the very same speed and cancel "
            f"exactly, whatever x is — so {a} over {b} is what survives, and that is {c}. "
            f"The curve flattens onto {c} and stays there. {a - b} takes one from the "
            f"other and {a * b} times them, and neither describes what the fraction does.",
            f'[[graph func="({a}*x^2)/({b}*x^2 + {b})" names="y = {a}x² / ({b}x² + {b})" lines="y={c}" range="0..12" yrange="0..{c + 2}" caption="the curve settles onto the line y = {c} — {a} over {b}"]]'
            f'[[step eq="{a} ÷ {b} = {c}"]]')


def _jump_board(p):
    a, b = p["a"], p["b"]
    return (f'[[graph func="{a} for x<6; {b} for x>=6" range="0..12" yrange="0..{b + 4}" caption="two shelves at the border x = 6 — the open dot at {a}, the closed dot at {b}, and a leap between them"]]'
            f'[[step eq="x < 6: y = {a} · x ≥ 6: y = {b}"]]'
            f'[[step eq="the jump measures ?"]]')


def _jump_worked(p):
    a, b = p["a"], p["b"]; j = b - a
    return (f"Look what you did: from the left the curve heads for {a} and from the right "
            f"for {b}, so it leaps {j} in no distance at all — a jump of {j}. {b} is only "
            f"where it lands, and {a + b} adds two heights that the curve never adds.",
            f'[[graph func="{a} for x<6; {b} for x>=6" lines="x=6" points="(6,{a}),(6,{b})" range="0..12" yrange="0..{b + 4}" caption="the leap at x = 6 — from {a} up to {b} is {j}"]]'
            f'[[step eq="{b} − {a} = {j}"]]')


def _cfix_board(p):
    a, b, c = p["a"], p["b"], p["c"]; top = max(b, c + a) + 4
    return (f'[[graph func="x+{a} for x<{c}; {b} for x>={c}" range="0..{c + 4}" yrange="0..{top}" caption="the sloping piece climbs to the border at x = {c} and the flat piece sits at {b} — walk the slope to the border and see where it arrives"]]'
            f'[[step eq="x < {c}: y = x + {a} · x ≥ {c}: y = {b}"]]'
            f'[[step eq="join up smoothly · flat value = ?"]]')


def _cfix_worked(p):
    a, b, c = p["a"], p["b"], p["c"]; v = c + a; top = max(b, v) + 4
    return (f"Look what you did: walk the sloping piece right up to {c} and it arrives at "
            f"{c} plus {a}, which is {v}. Set the flat piece to {v} and the two ends meet — "
            f"no jump, no hole, nothing to lift the pencil for. {b} is the value that does "
            f"not fit, and {a} is only the slope\'s own number.",
            f'[[graph func="x+{a} for x<{c}; {v} for x>={c}" points="({c},{v})" range="0..{c + 4}" yrange="0..{top}" caption="the flat piece raised to {v} — the two ends meet at x = {c}"]]'
            f'[[step eq="{c} + {a} = {v}"]]')


def _derv_board(p):
    a = p["a"]; r = a + 2
    return (f'[[graph func="x^2" names="y = x²" points="({a},{a * a})" range="0..{r}" yrange="0..{r * r}" caption="y = x squared with the point at x = {a} — the slope right there, at that one point, is the derivative"]]'
            f'[[step eq="y = x² · window shrinking onto x = {a}"]]'
            f'[[step eq="the rate closes in on ?"]]')


def _derv_worked(p):
    a = p["a"]; m = 2 * a; r = a + 2
    return (f"Look what you did: the average rate is the two x\'s put together, so sliding "
            f"both onto {a} gives {m} — the derivative at {a}, the slope of the curve at "
            f"that single point. {a * a} is how high the curve sits there, not how steep.",
            f'[[graph func="x^2" names="y = x²" lines="y={m}x-{a * a}" points="({a},{a * a})" range="0..{r}" yrange="0..{r * r}" caption="the tangent at x = {a} climbs {m} for every step across"]]'
            f'[[step eq="slope at {a} = {m}"]]')


def _pwrc_board(p):
    a, b = p["a"], p["b"]
    return (f'[[write text="y = {b}x^{a}"]]'
            f'[[machine input="{a}" rule="× {b}" output="?" caption="the exponent {a} comes down and meets the {b} already standing there — the front number of the derivative comes out"]]'
            f'[[step eq="derivative front number = ?"]]')


def _pwrc_worked(p):
    a, b = p["a"], p["b"]; t = a * b
    return (f"Look what you did: the {a} comes down and meets the {b} standing there — {a} "
            f"times {b} is {t} — and the power drops to {a - 1}. So the derivative is {t} x "
            f"to the {a - 1}. {a + b} adds the two, which no rule does, and {b} left the "
            f"exponent up where it was.",
            f'[[machine input="{a}" rule="× {b}" output="{t}" caption="the {a} comes down onto the {b} — {t}"]]'
            f'[[write text="{t}x^{a - 1}"]]'
            f'[[step eq="{a} × {b} = {t}"]]')


def _cnst_board(p):
    a, b = p["a"], p["b"]; top = 4 * a + b + 2
    return (f'[[graph lines="y={a}x+{b}" range="0..4" yrange="0..{top}" caption="the line y = {a}x + {b} — the same steepness at every point on it"]]'
            f'[[step eq="y = {a}x + {b}"]]'
            f'[[step eq="slope anywhere = ?"]]')


def _cnst_worked(p):
    a, b = p["a"], p["b"]; top = 4 * a + b + 2
    return (f"Look what you did: the line climbs {a} for every step across, at every point "
            f"on it, so its derivative is {a} — one number, true everywhere. The {b} only "
            f"lifts the whole line up the page and never tilts it, and {a + b} adds a height "
            f"to a slope.",
            f'[[graph lines="y={a}x+{b}" points="(1,{a + b}),(2,{2 * a + b})" range="0..4" yrange="0..{top}" caption="one step right, {a} up — the slope is {a} wherever you stand"]]'
            f'[[step eq="slope = {a}"]]')


def _evat_board(p):
    a, c = p["a"], p["c"]; r = c + 2
    return (f'[[graph func="{a}*x^2" names="y = {a}x²" points="({c},{a * c * c})" range="0..{r}" yrange="0..{a * r * r}" caption="y = {a} x squared with the point at x = {c} — the slope right there is what the derivative hands back"]]'
            f'[[step eq="y = {a}x² · slope = {2 * a}x"]]'
            f'[[step eq="at x = {c} · slope = ?"]]')


def _evat_worked(p):
    a, c = p["a"], p["c"]; m = 2 * a * c; h = a * c * c; r = c + 2
    return (f"Look what you did: the derivative is a machine of its own — feed it {c} and "
            f"it hands back {2 * a} times {c}, which is {m}. That is the slope right at that "
            f"point. {h} is how high the curve sits there, and {2 * a} is the machine\'s "
            f"front number before any x went in.",
            f'[[graph func="{a}*x^2" names="y = {a}x²" lines="y={m}x-{h}" points="({c},{h})" range="0..{r}" yrange="0..{a * r * r}" caption="the tangent at x = {c} climbs {m} for every step across"]]'
            f'[[step eq="{2 * a} × {c} = {m}"]]')


def _prod_board(p):
    a, c = p["a"], p["c"]; r = c + 2
    return (f'[[graph func="x*(x+{a})" names="y = x(x + {a})" points="({c},{c * (c + a)})" range="0..{r}" yrange="0..{r * (r + a)}" caption="y = x times (x + {a}) with the point at x = {c} — the slope right there"]]'
            f'[[step eq="y = x(x + {a}) = x² + {a}x"]]'
            f'[[step eq="slope = 2x + {a}"]]'
            f'[[step eq="at x = {c} · slope = ?"]]')


def _prod_worked(p):
    a, c = p["a"], p["c"]; m = 2 * c + a; h = c * (c + a); r = c + 2
    return (f"Look what you did: feed {c} into 2 x plus {a} — {2 * c} plus {a} is {m}, the "
            f"slope at that point. The product rule gives the same without expanding first. "
            f"{h} is the curve\'s height there, and {2 * c} is half the derivative with the "
            f"second piece forgotten.",
            f'[[graph func="x*(x+{a})" names="y = x(x + {a})" lines="y={m}x-{c * c}" points="({c},{h})" range="0..{r}" yrange="0..{r * (r + a)}" caption="the tangent at x = {c} climbs {m} for every step across"]]'
            f'[[step eq="2({c}) + {a} = {m}"]]')


def _chan_board(p):
    a, b = p["a"], p["b"]
    return (f'[[write text="y = ({a}x + 3)^{b}"]]'
            f'[[machine input="{b}" rule="× {a}" output="?" caption="the power {b} comes down, and the inside\'s own derivative {a} comes out to meet it"]]'
            f'[[step eq="front number of the derivative = ?"]]')


def _chan_worked(p):
    a, b = p["a"], p["b"]; t = a * b
    return (f"Look what you did: two things come down — the power {b}, and the inside\'s "
            f"derivative {a} — and {b} times {a} is {t}. Forgetting the inside leaves {b}, "
            f"the commonest mistake in Calculus, and {a + b} adds what should be timesed.",
            f'[[machine input="{b}" rule="× {a}" output="{t}" caption="the power {b} meets the inside\'s {a} — {t}"]]'
            f'[[step eq="{b} × {a} = {t}"]]')


def _chev_board(p):
    a, b = p["a"], p["b"]; top = (2 * a + b) ** 2
    return (f'[[graph func="({a}*x+{b})^2" names="y = ({a}x + {b})²" points="(0,{b * b})" range="-1..2" yrange="0..{top}" caption="y = ({a}x + {b}) squared with the point at x = 0 — the slope right there"]]'
            f'[[step eq="y = ({a}x + {b})²"]]'
            f'[[step eq="slope = 2({a}x + {b})·{a}"]]'
            f'[[step eq="at x = 0 · slope = ?"]]')


def _chev_worked(p):
    a, b = p["a"], p["b"]; m = 2 * a * b; h = b * b; top = (2 * a + b) ** 2
    return (f"Look what you did: at x equals zero the inside is just {b}, so the slope is 2 "
            f"times {b} times {a} — {m}. {h} is the curve\'s height there, the inside "
            f"squared, and {2 * b} drops the inside\'s derivative, which is the whole point "
            f"of the chain rule.",
            f'[[graph func="({a}*x+{b})^2" names="y = ({a}x + {b})²" lines="y={m}x+{h}" points="(0,{h})" range="-1..2" yrange="0..{top}" caption="the tangent at x = 0 climbs {m} for every step across"]]'
            f'[[step eq="2 × {b} × {a} = {m}"]]')


def _quot_board(p):
    a, b = p["a"], p["b"]
    return (f'[[write text="y = {a}x² ÷ {b}"]]'
            f'[[machine input="{a}" rule="× 2, then ÷ {b}" output="?" caption="the front number goes in — the power rule doubles it, and the {b} underneath divides it"]]'
            f'[[step eq="derivative front number = ?"]]')


def _quot_worked(p):
    a, b = p["a"], p["b"]; d = 2 * a; t = d // b
    return (f"Look what you did: the power rule doubles the {a} to {d}, and the {b} "
            f"underneath divides it — {d} over {b} is {t}. A plain number on the bottom "
            f"needs no quotient rule; it just comes along for the ride. {a // b} forgot the "
            f"doubling, and {a * b} timesed what should be divided.",
            f'[[machine input="{a}" rule="× 2, then ÷ {b}" output="{t}" caption="{a} doubled is {d}, and {d} over {b} is {t}"]]'
            f'[[step eq="{d} ÷ {b} = {t}"]]')




# ---- (ua, 2026-09-07) CALCULUS UNITS 4-6: the speed line alone, then the height it
# reaches and the crossing; area against side with the point, then the tangent there;
# the valley alone, then its flat bottom; the speed line, then one step up it; the fence
# shared four ways as a tape with every part blank, then the square walked round; the
# square on a metre grid asked, then counted; the hump of every split, then its peak;
# the curve whose bend changes, then the place it changes; the power rule run backwards
# as a machine that halves, then divides by the new power; two parallel curves with the
# lower one's point, then both points; one member of the family with its start, then
# its height further on. Every ask draws its question with the answer withheld; every
# walk-back draws it filled in.
def _vsol_board(p):
    a, b = p["a"], p["b"]; m = 2 * a; t = b // m; r = t + 2
    return (f'[[graph lines="y={m}x" names="speed = {m}t" range="0..{r}" yrange="0..{m * r}" caption="the speed line — {m} metres a second faster every second; somewhere along it the speed reaches {b}"]]'
            f'[[step eq="speed = {m}t"]]'
            f'[[step eq="speed = {b} at t = ?"]]')


def _vsol_worked(p):
    a, b = p["a"], p["b"]; m = 2 * a; t = b // m; r = t + 2
    return (f"Look what you did: the speed is {m} t, so set it equal to {b} — {m} t equals "
            f"{b}, and t is {b} over {m}, which is {t} seconds. That is the moment the line "
            f"reaches the height {b}. {b} is the speed itself, not a time, and {b // a} "
            f"divides by the distance's number instead of the speed's.",
            f'[[graph lines="y={m}x; y={b}" names="speed = {m}t; speed = {b}" points="({t},{b})" range="0..{r}" yrange="0..{m * r}" caption="the speed line meets the height {b} at t = {t}"]]'
            f'[[step eq="{m}t = {b}"]]'
            f'[[step eq="t = {t} seconds"]]')


def _mrat_board(p):
    a, b = p["a"], p["b"]; r = a + 3
    return (f'[[graph func="x^2" names="area = side²" points="({a},{a * a})" range="0..{r}" yrange="0..{r * r}" caption="area against side — at a side of {a} the curve is already steep, and the side is still growing {b} a second"]]'
            f'[[step eq="side {a} cm · growing {b} cm/s"]]'
            f'[[step eq="area growing at ? cm²/s"]]')


def _mrat_worked(p):
    a, b = p["a"], p["b"]; r = a + 3; m = 2 * a; g = 2 * a * b
    return (f"Look what you did: area is side squared, so its rate is 2 times the side times "
            f"the side's rate — 2 times {a} times {b} is {g} square centimetres a second. "
            f"The tangent at {a} climbs {m} a centimetre, and the side adds {b} of those a "
            f"second. {b} is the side's rate alone, and {a * a} is the area itself, not "
            f"its rate.",
            f'[[graph func="x^2" names="area = side²" lines="y={m}x-{a * a}" points="({a},{a * a})" range="0..{r}" yrange="0..{r * r}" caption="the tangent at a side of {a} climbs {m} for every centimetre — times the side\'s rate {b}, that is {g} a second"]]'
            f'[[step eq="2 × {a} × {b} = {g} cm²/s"]]')


def _crit_board(p):
    a = p["a"]; h = a // 2; pad = max(2, h * h // 4)
    return (f'[[graph func="x^2-{a}*x" names="y = x² − {a}x" range="0..{a}" yrange="{-h * h - pad}..{pad}" caption="the valley — somewhere along the bottom the curve is flat for an instant"]]'
            f'[[step eq="slope = 2x − {a}"]]'
            f'[[step eq="slope = 0 at x = ?"]]')


def _crit_worked(p):
    a = p["a"]; h = a // 2; pad = max(2, h * h // 4)
    return (f"Look what you did: set the slope to zero — 2 x take away {a} equals zero, so "
            f"2 x is {a} and x is {h}. There the curve is flat for an instant, the bottom of "
            f"its valley, {h * h} below the axis. {a} is the number in the slope, not the x "
            f"that solves it, and {2 * a} doubles when the equation halves.",
            f'[[graph func="x^2-{a}*x" names="y = x² − {a}x; the flat tangent" lines="y=-{h * h}" points="({h},{-h * h})" range="0..{a}" yrange="{-h * h - pad}..{pad}" caption="flat at x = {h} — the bottom of the valley"]]'
            f'[[step eq="2x = {a}"]]'
            f'[[step eq="x = {h}"]]')


def _acce_board(p):
    a = p["a"]; m = 2 * a
    return (f'[[graph lines="y={m}x" names="speed = {m}t" range="0..5" yrange="0..{m * 5}" caption="the speed line — it climbs the same amount every second, and that steady climb is the acceleration"]]'
            f'[[step eq="fallen {a}t² · speed {m}t"]]'
            f'[[step eq="acceleration = ?"]]')


def _acce_worked(p):
    a = p["a"]; m = 2 * a
    return (f"Look what you did: the speed {m} t is a line, and a line's derivative is its "
            f"front number — {m}. So the acceleration is {m}, the same at every moment: one "
            f"second on, the speed is {m} higher. {a} is the distance's number, one "
            f"differentiation short, and {4 * a} doubles once too often.",
            f'[[graph lines="y={m}x" names="speed = {m}t" points="(1,{m}),(2,{2 * m})" range="0..5" yrange="0..{m * 5}" caption="one second on, {m} faster — the acceleration is {m}"]]'
            f'[[step eq="{a}t² → {m}t → {m}"]]')


def _optr_board(p):
    a = p["a"]
    return (f'[[tape parts="?|?|?|?" total="{a} m of fence" caption="the fence shared four ways — the best rectangle is a square, so every side takes an equal share"]]'
            f'[[step eq="fence all round = {a} m"]]'
            f'[[step eq="biggest area · each side = ?"]]')


def _optr_worked(p):
    a = p["a"]; q = a // 4
    return (f"Look what you did: the area is biggest when the rectangle is a square, so the "
            f"{a} metres of fence are shared four ways — {a} over 4 is {q} metres a side. "
            f"Walk round it: {q} plus {q} plus {q} plus {q} uses the fence exactly. "
            f"{a // 2} is half the fence, two sides at once, and {a} is the whole fence "
            f"read as one side.",
            f'[[rectangle w="{q}" h="{q}" show="perimeter" caption="a square of side {q} — the walk round it is the whole {a}"]]'
            f'[[step eq="{a} ÷ 4 = {q}"]]')


def _maxa_board(p):
    a = p["a"]; q = a // 4
    return (f'[[rectangle w="{q}" h="{q}" show="area" ask="1" caption="the square of side {q} on a metre grid — the ground inside is the area"]]'
            f'[[step eq="square of side {q} m"]]'
            f'[[step eq="area = ? m²"]]')


def _maxa_worked(p):
    a = p["a"]; q = a // 4; A = q * q
    return (f"Look what you did: a square of side {q} encloses {q} times {q} — {A} square "
            f"metres, every unit square on the grid counted. No other rectangle with {a} "
            f"metres of fence can beat it. {q} is the side, not the ground, and {a} is the "
            f"fence you started with.",
            f'[[rectangle w="{q}" h="{q}" show="area" caption="{q} by {q} — {A} square metres of ground"]]'
            f'[[step eq="{q} × {q} = {A} m²"]]')


def _sumx_board(p):
    a = p["a"]; h = a // 2; P = h * h; top = P + max(4, P // 5)
    return (f'[[graph func="x*({a}-x)" names="product = x({a} − x)" range="0..{a}" yrange="0..{top}" caption="the product for every way of splitting {a} into two numbers — it rises, peaks, and falls"]]'
            f'[[step eq="two numbers adding to {a}"]]'
            f'[[step eq="biggest product = ?"]]')


def _sumx_worked(p):
    a = p["a"]; h = a // 2; P = h * h; top = P + max(4, P // 5)
    return (f"Look what you did: equal halves win — {h} and {h} give {P}, the top of the "
            f"hump. Pull the pair apart and the product falls away on both sides: 1 and "
            f"{a - 1} give only {a - 1}. {h} is one of the halves, not their product, and "
            f"{a} is the sum you started with.",
            f'[[graph func="x*({a}-x)" names="product = x({a} − x); the peak" lines="y={P}" points="({h},{P})" range="0..{a}" yrange="0..{top}" caption="the peak sits at {h} and {h} — a product of {P}"]]'
            f'[[step eq="{h} × {h} = {P}"]]')


def _infl_board(p):
    a = p["a"]; x0 = a // 3; lo = -(4 * a * a * a) // 27; lo = lo - max(4, (-lo) // 8); top = max(4, (-lo) // 6)
    return (f'[[graph func="x^3-{a}*x^2" names="y = x³ − {a}x²" range="0..{a}" yrange="{lo}..{top}" caption="the curve bends like a dome at first and like a cup later — somewhere between, the bend changes sides"]]'
            f'[[step eq="second derivative = 6x − {2 * a}"]]'
            f'[[step eq="second derivative = 0 at x = ?"]]')


def _infl_worked(p):
    a = p["a"]; x0 = a // 3; lo = -(4 * a * a * a) // 27; lo = lo - max(4, (-lo) // 8); top = max(4, (-lo) // 6)
    return (f"Look what you did: set the second derivative to zero — 6 x take away {2 * a} "
            f"equals zero, so 6 x is {2 * a} and x is {x0}. There the curve stops bending "
            f"like a dome and starts bending like a cup: the inflection point. {a // 2} "
            f"halves out of the first-derivative habit, and {a} is the equation's own "
            f"number.",
            f'[[graph func="x^3-{a}*x^2" names="y = x³ − {a}x²; x = {x0}" lines="x={x0}" range="0..{a}" yrange="{lo}..{top}" caption="dome on the left of x = {x0}, cup on the right — the bend changes there"]]'
            f'[[step eq="6x = {2 * a}"]]'
            f'[[step eq="x = {x0}"]]')


def _anti_board(p):
    a = p["a"]
    return (f'[[write text="derivative = {a}x"]]'
            f'[[machine input="{a}" rule="÷ 2" output="?" caption="the power rule run backwards — the front number goes in and is halved, because differentiating had doubled it"]]'
            f'[[step eq="? x² came from it"]]')


def _anti_worked(p):
    a = p["a"]; h = a // 2
    return (f"Look what you did: forwards, {h} x squared drops its 2 down the front and gives "
            f"{a} x; so backwards from {a} x you halve — {a} over 2 is {h}, and the power "
            f"climbs back up to squared. {a} copies the number straight over, and {2 * a} "
            f"runs the forward rule the wrong way.",
            f'[[machine input="{a}" rule="÷ 2" output="{h}" caption="{a} halved is {h} — the front number of the function it came from"]]'
            f'[[write text="{h}x²"]]'
            f'[[step eq="{a} ÷ 2 = {h}"]]')


def _antp_board(p):
    a, b = p["a"], p["b"]; n = a + 1
    return (f'[[write text="derivative = {b}x^{a}"]]'
            f'[[machine input="{b}" rule="÷ {n}" output="?" caption="the power climbs from {a} to {n}, and the front number is divided by that new exponent"]]'
            f'[[step eq="? x^{n} came from it"]]')


def _antp_worked(p):
    a, b = p["a"], p["b"]; n = a + 1; k = b // n
    return (f"Look what you did: the power {a} climbs to {n}, and the front number is divided "
            f"by it — {b} over {n} is {k}. So {k} x to the {n} is the answer; check it "
            f"forwards, and the {n} comes down onto the {k} to give {b} back. {b} hands the "
            f"front number back undivided, and {n} is the exponent, not the front number.",
            f'[[machine input="{b}" rule="÷ {n}" output="{k}" caption="{b} over the new exponent {n} is {k}"]]'
            f'[[write text="{k}x^{n}"]]'
            f'[[step eq="{b} ÷ {n} = {k}"]]')


def _plusc_board(p):
    a, b = p["a"], p["b"]; k = a - 16; kk = k + b
    lo = f"x^2+{k}" if k >= 0 else f"x^2-{-k}"; hi = f"x^2+{kk}" if kk >= 0 else f"x^2-{-kk}"
    ymin = min(0, k) - 2; top = 36 + kk + 4
    return (f'[[graph func="{lo}; {hi}" names="lower; higher" points="(4,{a})" range="0..6" yrange="{ymin}..{top}" caption="two curves with the same derivative — the same shape, {b} apart at every x; the lower one passes {a} at x = 4"]]'
            f'[[step eq="same derivative · {b} apart everywhere"]]'
            f'[[step eq="lower is {a} · higher = ?"]]')


def _plusc_worked(p):
    a, b = p["a"], p["b"]; k = a - 16; kk = k + b
    lo = f"x^2+{k}" if k >= 0 else f"x^2-{-k}"; hi = f"x^2+{kk}" if kk >= 0 else f"x^2-{-kk}"
    ymin = min(0, k) - 2; top = 36 + kk + 4
    return (f"Look what you did: the two curves run parallel, {b} apart at every single x, "
            f"so above the lower one's {a} the higher one reads {a} plus {b} — {a + b}. "
            f"That gap is the plus C: an antiderivative is a whole family, stacked up the "
            f"page. {a - b} takes the gap away and lands below the curve you were given, "
            f"and {b} is the gap alone, not a height.",
            f'[[graph func="{lo}; {hi}" names="lower; higher" points="(4,{a}),(4,{a + b})" range="0..6" yrange="{ymin}..{top}" caption="at x = 4 the lower reads {a} and the higher {a + b} — {b} apart, like everywhere"]]'
            f'[[step eq="{a} + {b} = {a + b}"]]')


def _init_board(p):
    a, c = p["a"], p["c"]; r = c + 1
    return (f'[[graph func="x^2+{a}" names="y = x² + {a}" points="(0,{a})" range="0..{r}" yrange="0..{r * r + a + 2}" caption="slope 2x through the height {a} at x = 0 — one curve out of the family, and it keeps climbing"]]'
            f'[[step eq="slope 2x → y = x² + C"]]'
            f'[[step eq="y = {a} at x = 0 · at x = {c} · y = ?"]]')


def _init_worked(p):
    a, c = p["a"], p["c"]; r = c + 1; q = c * c; ans = q + a
    return (f"Look what you did: slope 2 x comes from x squared plus a constant, and at x "
            f"equals zero the x squared is nothing, so the constant is the starting height, "
            f"{a}. Then at x equals {c}: {c} squared is {q}, plus {a} — {ans}. {q} forgets "
            f"the constant the point gave you, and {a} pretends the curve never climbed.",
            f'[[graph func="x^2+{a}" names="y = x² + {a}" points="(0,{a}),({c},{ans})" range="0..{r}" yrange="0..{r * r + a + 2}" caption="from {a} at x = 0 up to {ans} at x = {c}"]]'
            f'[[step eq="{c}² + {a} = {ans}"]]')



# ---- (ub, 2026-09-07) CALCULUS UNITS 7-9: the area under the graph, SHADED
# ([[graph shade="lo..hi" label="?"]]) with its label "?" on the ask and the area on the
# walk-back -- the rectangle under a steady speed, the triangle under a ramp, the strip
# under 2x between two ends, the hump whose area is given and the flat line it flattens
# to, the strip caught between two curves (between="1"), the trapezium under a climbing
# speed and the halfway line, the flow rectangle and then the amount line; the cylinder
# a rectangle sweeps out; the amount line falling from the start, the two rates as bars
# and the net line, the rate line against the amount, the rate line crossing zero.
# Every ask draws its question with the answer withheld; every walk-back draws it in.
def _defi_board(p):
    a, b = p["a"], p["b"]
    return (f'[[graph lines="y={a}" names="a steady {a} metres a second" shade="0..{b}" label="?" range="0..{b + 2}" yrange="0..{a + 2}" caption="a steady {a} metres a second for {b} seconds — the shaded rectangle under the speed line is the distance"]]'
            f'[[step eq="speed {a} m/s · for {b} s"]]'
            f'[[step eq="area under the graph = ? metres"]]')


def _defi_worked(p):
    a, b = p["a"], p["b"]; d = a * b
    return (f"Look what you did: the speed line sits at {a} for {b} seconds, so the shape under "
            f"it is a rectangle {a} tall and {b} wide — {a} times {b} is {d}, and {d} metres "
            f"is how far the car went. The area MEANS the distance. {a + b} adds metres to "
            f"seconds, and {b} is the time you were told.",
            f'[[graph lines="y={a}" names="a steady {a} metres a second" shade="0..{b}" label="{d}" range="0..{b + 2}" yrange="0..{a + 2}" caption="{a} tall, {b} wide — an area of {d}, and {d} metres travelled"]]'
            f'[[step eq="{a} × {b} = {d} m"]]')


def _triz_board(p):
    a = p["a"]
    return (f'[[graph lines="y=x" names="speed = t" shade="0..{a}" label="?" range="0..{a + 2}" yrange="0..{a + 2}" caption="the speed ramps up from nothing — the shaded triangle under it is the distance after {a} seconds"]]'
            f'[[step eq="speed = t · from 0 to {a} s"]]'
            f'[[step eq="triangle area = ? metres"]]')


def _triz_worked(p):
    a = p["a"]; d = a * a // 2
    return (f"Look what you did: after {a} seconds the triangle is {a} wide and {a} tall, and "
            f"a triangle takes half the rectangle round it — {a} times {a} halved is {d} "
            f"metres. {a * a} forgets the half and claims the whole rectangle, as if the car "
            f"had gone flat out from the first second, and {a} is the time, not a distance.",
            f'[[graph lines="y=x" names="speed = t" shade="0..{a}" label="{d}" range="0..{a + 2}" yrange="0..{a + 2}" caption="{a} by {a}, halved — {d} metres"]]'
            f'[[step eq="{a} × {a} ÷ 2 = {d} m"]]')


def _ftc_board(p):
    a, b = p["a"], p["b"]
    return (f'[[graph lines="y=2x" names="y = 2x" shade="{a}..{b}" label="?" range="0..{b + 2}" yrange="0..{2 * b + 4}" caption="the strip under y = 2x from x = {a} to x = {b} — its area is what the theorem finds"]]'
            f'[[step eq="area under 2x from {a} to {b}"]]'
            f'[[step eq="{b}² − {a}² = ?"]]')


def _ftc_worked(p):
    a, b = p["a"], p["b"]; d = b * b - a * a
    return (f"Look what you did: 2 x comes from x squared, so work x squared out at both ends "
            f"and take one from the other — {b} squared is {b * b}, {a} squared is {a * a}, "
            f"and {b * b} take away {a * a} is {d}. That is the shaded strip's area, end "
            f"take away start. {(b - a) * (b - a)} squares the gap instead, and {b - a} is "
            f"only the gap.",
            f'[[graph lines="y=2x" names="y = 2x" shade="{a}..{b}" label="{d}" range="0..{b + 2}" yrange="0..{2 * b + 4}" caption="{b}² take away {a}² — the strip holds {d}"]]'
            f'[[step eq="{b}² − {a}² = {d}"]]')


def _avgv_board(p):
    a, b = p["a"], p["b"]; h = a // b; amp = h / 2; top = int(h * 1.6) + 2
    return (f'[[graph func="{h} + {amp:g}*sin(2*pi*x/{b})" names="the curve" shade="0..{b}" label="{a}" range="0..{b}" yrange="0..{top}" caption="the area under the curve from 0 to {b} is {a} — push the hump down into the dip until the top is flat"]]'
            f'[[step eq="area {a} · width {b}"]]'
            f'[[step eq="flattened height = ?"]]')


def _avgv_worked(p):
    a, b = p["a"], p["b"]; h = a // b; amp = h / 2; top = int(h * 1.6) + 2
    return (f"Look what you did: spread {a} of area evenly across a width of {b} and it stands "
            f"{a} over {b} high — {h}. That flat line is the curve's average height: the hump "
            f"above it and the dip below it trade places exactly. {a} is the area, not a "
            f"height, and {b} is only the width.",
            f'[[graph func="{h} + {amp:g}*sin(2*pi*x/{b})" names="the curve; flattened to {h}" lines="y={h}" shade="0..{b}" label="{a}" range="0..{b}" yrange="0..{top}" caption="the same {a} of area as a flat rectangle {b} wide — it stands {h} high"]]'
            f'[[step eq="{a} ÷ {b} = {h}"]]')


def _btwn_board(p):
    a, b = p["a"], p["b"]; ta = a / 10; tb = b / 10; top = int(ta * 1.5) + 3
    return (f'[[graph func="{ta:g} + {ta / 2:g}*sin(2*pi*x/10); {tb:g} + {tb / 2:g}*sin(2*pi*x/10)" names="top; bottom" shade="0..10" between="1" label="?" range="0..10" yrange="0..{top}" caption="two curves over the same stretch — {a} under the top one, {b} under the bottom one, and the shaded strip caught between them"]]'
            f'[[step eq="top area {a} · bottom area {b}"]]'
            f'[[step eq="area between = ?"]]')


def _btwn_worked(p):
    a, b = p["a"], p["b"]; ta = a / 10; tb = b / 10; top = int(ta * 1.5) + 3; d = a - b
    return (f"Look what you did: the {b} under the bottom curve is already counted inside the "
            f"{a} under the top one, so take it away — {a} take away {b} is {d}, the strip "
            f"between them. Top take away bottom, always in that order. {a + b} counts the "
            f"lower region twice over, and {a} is the whole slab, not the gap.",
            f'[[graph func="{ta:g} + {ta / 2:g}*sin(2*pi*x/10); {tb:g} + {tb / 2:g}*sin(2*pi*x/10)" names="top; bottom" shade="0..10" between="1" label="{d}" range="0..10" yrange="0..{top}" caption="{a} take away {b} — the strip between holds {d}"]]'
            f'[[step eq="{a} − {b} = {d}"]]')


def _trap_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[graph func="{a} + {b - a}*x/{c}" names="speed" shade="0..{c}" label="?" range="0..{c + 2}" yrange="0..{b + 4}" caption="the speed climbs steadily from {a} to {b} over {c} seconds — the shaded trapezium under it is the distance"]]'
            f'[[step eq="{a} m/s → {b} m/s · over {c} s"]]'
            f'[[step eq="area under the graph = ? metres"]]')


def _trap_worked(p):
    a, b, c = p["a"], p["b"], p["c"]; d = (a + b) * c // 2; mid = (a + b) / 2
    return (f"Look what you did: the speed climbs steadily, so its average is halfway between "
            f"{a} and {b} — {mid:g} — and {mid:g} metres a second for {c} seconds is {d} "
            f"metres. The halfway line cuts the trapezium into a rectangle of the same area. "
            f"{(a + b) * c} forgets the halving and holds both speeds at once, and {b * c} "
            f"holds the top speed for the whole journey.",
            f'[[graph func="{a} + {b - a}*x/{c}" names="speed; the halfway speed, {mid:g}" lines="y={mid:g}" shade="0..{c}" label="{d}" range="0..{c + 2}" yrange="0..{b + 4}" caption="halfway between {a} and {b} is {mid:g}, held for {c} seconds — {d} metres"]]'
            f'[[step eq="({a} + {b}) × {c} ÷ 2 = {d}"]]')


def _accu_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[graph lines="y={a}" names="{a} litres a minute running in" shade="0..{b}" label="?" range="0..{b + 2}" yrange="0..{a + 2}" caption="water runs in at {a} litres a minute for {b} minutes — the shaded rectangle is what ARRIVES, on top of the {c} already there"]]'
            f'[[step eq="starts with {c} L"]]'
            f'[[step eq="{a} L/min · {b} min · total = ?"]]')


def _accu_worked(p):
    a, b, c = p["a"], p["b"], p["c"]; g = a * b; t = c + g
    return (f"Look what you did: {a} litres a minute for {b} minutes is {g} litres — the area "
            f"under the flow graph. But the tank was not empty, so those {g} land on top of the "
            f"{c} already there: {c} plus {g} is {t}. The amount line starts at {c} and climbs "
            f"to {t}. {g} forgets the water that was there, and {c + a + b} adds three numbers "
            f"that measure nothing together.",
            f'[[graph lines="y={a}x+{c}" names="litres in the tank" points="(0,{c}),({b},{t})" range="0..{b + 1}" yrange="0..{t + 10}" caption="from {c} litres at the start up to {t} after {b} minutes"]]'
            f'[[step eq="{a} × {b} = {g}"]]'
            f'[[step eq="{c} + {g} = {t}"]]')


def _revo_board(p):
    a, b = p["a"], p["b"]
    return (f'[[solid kind="cylinder" r="{a}" h="{b}" caption="the rectangle {a} tall and {b} long, spun about the line beneath it — a cylinder of radius {a} and length {b}"]]'
            f'[[step eq="radius {a} · length {b}"]]'
            f'[[step eq="volume = ? × π"]]')


def _revo_worked(p):
    a, b = p["a"], p["b"]; q = a * a; v = q * b
    return (f"Look what you did: every slice through the cylinder is a circle of radius {a}, "
            f"and its area is pi times {a} squared — {q} pi. Stack {b} lengths of that and "
            f"the volume is {v} pi. Squaring the radius is what turns a flat area into a "
            f"solid: {a * b} leaves the squaring out, and {2 * a * b} doubles the radius "
            f"where it should be squared.",
            f'[[solid kind="cylinder" r="{a}" h="{b}" caption="a circle of area {q}π, stacked {b} long — {v}π"]]'
            f'[[step eq="{a}² = {q}"]]'
            f'[[step eq="{q} × {b} = {v}"]]')


def _dfeq_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[graph lines="y=-{b}x+{a}" names="litres in the tank" points="(0,{a})" range="0..{c + 2}" yrange="0..{a + 10}" caption="the tank starts at {a} litres and the line falls {b} every minute — the equation only says how fast it drops"]]'
            f'[[step eq="dV/dt = −{b} · starts at {a} L"]]'
            f'[[step eq="after {c} min · ? litres"]]')


def _dfeq_worked(p):
    a, b, c = p["a"], p["b"], p["c"]; g = b * c; left = a - g
    return (f"Look what you did: the rate has to meet the clock — {b} litres a minute for {c} "
            f"minutes is {g} gone, and {a} take away {g} leaves {left}. The line drops from "
            f"{a} to {left} over the {c} minutes. {a - b} takes away only one minute's worth, "
            f"and {g} is what drained, not what is left in the tank.",
            f'[[graph lines="y=-{b}x+{a}" names="litres in the tank" points="(0,{a}),({c},{left})" range="0..{c + 2}" yrange="0..{a + 10}" caption="from {a} down to {left} after {c} minutes — {g} gone"]]'
            f'[[step eq="{b} × {c} = {g}"]]'
            f'[[step eq="{a} − {g} = {left}"]]')


def _mixr_board(p):
    a, b, c = p["a"], p["b"], p["c"]
    return (f'[[bars data="in:{a} | out:{b}" caption="two rates pulling against each other — {a} litres a minute running in, {b} draining out"]]'
            f'[[step eq="in {a} L/min · out {b} L/min"]]'
            f'[[step eq="after {c} min · ? litres"]]')


def _mixr_worked(p):
    a, b, c = p["a"], p["b"], p["c"]; n = a - b; t = n * c
    return (f"Look what you did: settle the fight first — {a} in and {b} out means the tank "
            f"truly gains {n} litres a minute, the net rate. Then let the clock work on that "
            f"one number: {n} times {c} is {t} litres. {(a + b) * c} adds the two rates as if "
            f"the drain were helping, and {a * c} counts the inflow alone.",
            f'[[graph lines="y={n}x" names="litres in the tank" points="({c},{t})" range="0..{c + 3}" yrange="0..{t + 20}" caption="the tank climbs {n} a minute — {t} litres after {c} minutes"]]'
            f'[[step eq="{a} − {b} = {n}"]]'
            f'[[step eq="{n} × {c} = {t}"]]')


def _pgrw_board(p):
    a, b = p["a"], p["b"]; r = a + 4
    return (f'[[graph lines="y={b}x" names="rate = {b}P" range="0..{r}" yrange="0..{b * r}" caption="the rate against the amount — the bigger the colony, the faster it grows; read the line at P = {a}"]]'
            f'[[step eq="dP/dt = {b}P"]]'
            f'[[step eq="P = {a} · rate = ?"]]')


def _pgrw_worked(p):
    a, b = p["a"], p["b"]; r = a + 4; g = a * b
    return (f"Look what you did: every one of the {a} bacteria contributes {b} a minute, so the "
            f"rate right now is {a} times {b} — {g} a minute, the height of the line at P "
            f"equals {a}. And it will not stay there: the growing feeds the growing. {a + b} "
            f"adds where it should multiply, and {b} pretends the colony's size does not "
            f"matter.",
            f'[[graph lines="y={b}x" names="rate = {b}P" points="({a},{g})" range="0..{r}" yrange="0..{b * r}" caption="at P = {a} the line stands {g} high — {g} new bacteria a minute"]]'
            f'[[step eq="{a} × {b} = {g}"]]')


def _eqbm_board(p):
    a, b = p["a"], p["b"]; q = a // b
    return (f'[[graph lines="y=-{b}x+{a}" names="rate = {a} − {b}P" range="0..{q + 2}" yrange="{-2 * b}..{a + b}" caption="the rate against the population — it falls as P grows, and somewhere it reaches zero"]]'
            f'[[step eq="dP/dt = {a} − {b}P"]]'
            f'[[step eq="rate = 0 when P = ?"]]')


def _eqbm_worked(p):
    a, b = p["a"], p["b"]; q = a // b
    return (f"Look what you did: set the rate to zero — {b} P has to equal {a}, so P is {a} "
            f"over {b}, which is {q}. That is where the line crosses the axis: sit the "
            f"population there and nothing moves. Above it the rate is negative and pulls "
            f"down; below it the rate pushes up. {a - b} takes away instead of dividing, and "
            f"{a} is the equation's own number.",
            f'[[graph lines="y=-{b}x+{a}" names="rate = {a} − {b}P" points="({q},0)" range="0..{q + 5}" yrange="{-4 * b}..{a + b}" caption="the rate crosses zero at P = {q} — equilibrium"]]'
            f'[[step eq="{b}P = {a}"]]'
            f'[[step eq="P = {q}"]]')



# The base ops have no OP_EXT entry; their walk-back pictures live here.
BASE_WORKED = {
    "+": lambda p: _col_add(p["a"], p["b"]),
    "-": lambda p: _col_sub(p["a"], p["b"]),
    "t": _tens_ones_worked,
}


def _r10_walkback(a):
    lo = a // 10 * 10
    hi = lo + 10
    d = a % 10
    near = (a + 5) // 10 * 10
    where = ("below halfway" if d < 5 else
             "right at halfway" if d == 5 else "past halfway")
    way = "down" if d < 5 else "up"
    return (f"Look what you did: {a} sits between {lo} and {hi}. The ones digit "
            f"is {d} — {where} — so it hops {way} to {near}.")


OP_EXT = {
    # ============ (ph, 2026-08-28) THE LAST EIGHT -- THE COURSE IS WHOLE ==========
    # Basic was short seven lessons and Pre-Algebra one. With these, every one of the
    # ten courses is nine units of four and nothing anywhere falls to the live lane.
    "mtz": {   # a times ten or a hundred -- the place-shift, not a times table
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: f"What is {p['a']} times {p['b']}?",
        # (sr) the chart shows the number BEFORE the move; the walk-back shows it after
        "board": lambda p: (f'[[placevalue n="{p["a"]}" caption="{p["a"]} — now move every '
                            f'digit up"]][[step eq="{p["a"]} × {p["b"]} = ?"]]'),
        "worked": _mtz_worked,
        "praise": lambda p: (f"{p['a']} times {p['b']} is {p['a'] * p['b']} — every "
                             f"digit moved up, and the gap was filled with zeros."),
        "key": lambda p: p["a"] * p["b"],
        "check": lambda p: (2 <= p["a"] <= 99 and p["b"] in (10, 100)
                            and p["a"] % 10 != 0,
                            "a two-digit number that does not already end in zero, "
                            "times ten or a hundred"),
        # the one real slip is losing a zero (or adding one too many)
        "choices": lambda p: [p["a"] * p["b"] // 10, p["a"] * p["b"],
                              p["a"] * p["b"] * 10],
    },
    "fpr": {   # a is b times WHAT? -- the partner in a factor pair
        "ans": lambda p: p["a"] // p["b"],
        "spoken": lambda p: f"{p['a']} is {p['b']} times what number?",
        "board": _fpr_board,          # (st) the sharing picture while small
        "worked": _fpr_worked,        # (st) the groups, or the rectangle with its sides
        "praise": lambda p: (f"{p['b']} times {p['a'] // p['b']} is {p['a']}, so "
                             f"{p['b']} and {p['a'] // p['b']} are a factor pair."),
        "key": lambda p: p["a"],
        "check": lambda p: (12 <= p["a"] <= 100 and 2 <= p["b"] < p["a"]
                            and p["a"] % p["b"] == 0 and p["a"] // p["b"] >= 2
                            and p["b"] != p["a"] // p["b"],
                            "a real factor pair of two different numbers"),
    },
    "simp": {  # a out of b in simplest form -- what is the new TOP number?
        "ans": lambda p: p["a"] // _gcd(p["a"], p["b"]),
        "spoken": lambda p: (f"Write {p['a']} out of {p['b']} in its simplest form. "
                             f"What is the new top number?"),
        "board": _simp_board,         # (su) the pie as given (when it has 12 parts or fewer)
        "worked": _simp_worked,       # (su) the same amount, cut two ways
        "praise": lambda p: (f"Both numbers share {_gcd(p['a'], p['b'])}, so "
                             f"{p['a']} out of {p['b']} is "
                             f"{p['a'] // _gcd(p['a'], p['b'])} out of "
                             f"{p['b'] // _gcd(p['a'], p['b'])}."),
        "key": lambda p: p["b"],
        "check": lambda p: (2 <= p["a"] < p["b"] <= 24
                            and _gcd(p["a"], p["b"]) > 1,
                            "a fraction that really can be made simpler"),
    },
    "fus": {   # one b-th TAKE AWAY a c-ths, answered in c-ths (fu's mirror)
        # ⚠️ the first cut said "take away ONE c-th" and had a pool of six -- below
        # the battery's seven-problem floor before a single ask was set aside. Letting
        # the number taken away vary is the same lesson and gives 24 problems.
        "ans": lambda p: p["c"] // p["b"] - p["a"],
        "spoken": lambda p: (f"How many {_FRACWORD[p['c']][1]} is one "
                             f"{_FRACWORD[p['b']][0]} take away "
                             f"{_plural(p['a'], _FRACWORD[p['c']][0])}?"),
        "board": _fus_board,          # (sv) the finer line, the first fraction found on it
        "worked": _fus_worked,
        "praise": lambda p: (f"One {_FRACWORD[p['b']][0]} is "
                             f"{p['c'] // p['b']} {_FRACWORD[p['c']][1]}, so taking "
                             f"{_plural(p['a'], _FRACWORD[p['c']][0])} away leaves "
                             f"{p['c'] // p['b'] - p['a']}."),
        "key": lambda p: p["c"],
        "check": lambda p: (p["b"] in _FRACWORD and p["c"] in _FRACWORD
                            and p["c"] % p["b"] == 0 and p["c"] // p["b"] >= 2
                            and 1 <= p["a"] < p["c"] // p["b"],
                            "the bottoms must match up and leave something behind"),
        "speaks": lambda p, sp: True,   # the bottoms are spoken as words, not digits
    },
    "t2h": {   # a tenths + b hundredths -- answered in hundredths
        "ans": lambda p: 10 * p["a"] + p["b"],
        "spoken": lambda p: (f"How many hundredths is "
                             f"{_plural(p['a'], 'tenth')} plus "
                             f"{_plural(p['b'], 'hundredth')}?"),
        "board": _t2h_board,          # (sw) the hundredths square: tenths are full rows
        "worked": _t2h_worked,
        "praise": lambda p: (f"{_plural(p['a'], 'tenth')} is "
                             f"{_plural(10 * p['a'], 'hundredth')}, and {p['b']} "
                             f"more equals {10 * p['a'] + p['b']}."),
        "key": lambda p: 10 * p["a"] + p["b"],
        "check": lambda p: (1 <= p["a"] <= 9 and 1 <= p["b"] <= 9,
                            "single-digit tenths and hundredths, so the answer "
                            "stays under one whole"),
        # the slip is adding the two digits as though a tenth and a hundredth
        # were the same size
        "choices": lambda p: [p["a"] + p["b"], 10 * p["a"] + p["b"],
                              10 * p["a"] + 10 * p["b"]],
    },
    "wpc": {   # a out of b, said as a percent
        "ans": lambda p: 100 * p["a"] // p["b"],
        "spoken": lambda p: f"What is {p['a']} out of {p['b']} as a percent?",
        "board": _wpc_board,          # (sx) the part as a pie or a bar; the square on the walk-back
        "worked": _wpc_worked,
        "praise": lambda p: (f"{p['a']} out of {p['b']} is "
                             f"{100 * p['a'] // p['b']} percent."),
        "key": lambda p: 100 * p["a"] // p["b"],
        "check": lambda p: (p["b"] in (4, 5, 10, 20, 25, 50, 100)
                            and 1 <= p["a"] < p["b"]
                            and (100 * p["a"]) % p["b"] == 0,
                            "a bottom that divides a hundred, and a whole percent"),
    },
    "poff": {  # b percent off a price of a -- what do you PAY?
        "ans": lambda p: p["a"] - p["a"] * p["b"] // 100,
        "spoken": lambda p: (f"A coat costs {p['a']} dollars, and there is "
                             f"{p['b']} percent off. What do you pay?"),
        "board": _poff_board,         # (sx) the tape: the discount and what you pay
        "worked": _poff_worked,
        "praise": lambda p: (f"{p['b']} percent of {p['a']} is "
                             f"{p['a'] * p['b'] // 100}, so you pay "
                             f"{p['a'] - p['a'] * p['b'] // 100}."),
        "key": lambda p: p["a"] - p["a"] * p["b"] // 100,
        "check": lambda p: (10 <= p["a"] <= 200 and p["b"] in (10, 20, 25)
                            and (p["a"] * p["b"]) % 100 == 0,
                            "a whole-dollar discount off a whole-dollar price -- and "
                            "never 50 percent, where the saving and the price you pay "
                            "are the same number and the lesson's own trap vanishes"),
        # THE trap of the whole lesson: answering the discount instead of the price
        "choices": lambda p: [p["a"] * p["b"] // 100,
                              p["a"] - p["a"] * p["b"] // 100, p["a"]],
    },
    "bfac": {  # the BIGGEST factor of a that is not a itself
        "ans": lambda p: p["a"] // _spf(p["a"]),
        "spoken": lambda p: (f"What is the biggest number that divides {p['a']} "
                             f"exactly, apart from {p['a']} itself?"),
        "board": lambda p: f'[[step eq="{p["a"]} → biggest factor below it = ?"]]',
        "worked": _bfac_worked,       # (tc) the pair drawn: smallest with biggest
        "praise": lambda p: (f"Dividing {p['a']} by its smallest factor "
                             f"{_spf(p['a'])} gives {p['a'] // _spf(p['a'])} — the "
                             f"biggest one there is."),
        "key": lambda p: p["a"] // _spf(p["a"]),
        "check": lambda p: (4 <= p["a"] <= 99 and _spf(p["a"]) != p["a"],
                            "a number with a factor to find -- never a prime"),
        "speaks": lambda p, sp: str(p["a"]) in sp,
    },
    # ================= (pg, 2026-08-27) THE ENTRY COURSE FILLS ITS UNITS =========
    # Jim: "go and create the authored lessons as well." Entry had 20 lessons where
    # nine units of four is 36, so 16 topics fell straight through to the slow live
    # lane -- for the YOUNGEST children, who are least able to wait 8 seconds for a
    # sentence. These are their ops. Two of the sixteen needed no new op at all:
    # place value reuses "pv" and dimes reuse "m", both already proved in Basic.
    "big": {   # which of two numbers is bigger
        "ans": lambda p: max(p["a"], p["b"]),
        "spoken": lambda p: f"Which number is bigger, {p['a']} or {p['b']}?",
        # (tb) the ask draws the two numbers on the line -- the picture IS the
        # comparing method (reach it later = bigger), the way the array is the
        # equal-groups method; the caption names neither as bigger
        "board": lambda p: (f'[[numberline min="1" max="{10 if max(p["a"], p["b"]) <= 10 else 20}" '
                            f'points="{min(p["a"], p["b"])},{max(p["a"], p["b"])}" '
                            f'caption="{p["a"]} or {p["b"]} — which do you reach later?"]]'),
        "praise": lambda p: (f"{max(p['a'], p['b'])} is bigger than "
                             f"{min(p['a'], p['b'])}."),
        "key": lambda p: 100 * p["a"] + p["b"],
        "check": lambda p: (1 <= p["a"] <= 20 and 1 <= p["b"] <= 20
                            and p["a"] != p["b"],
                            "two different numbers inside the counting range"),
        # +-1 would give the answer away: the options must be the two numbers
        # themselves, plus the one slip a child actually makes -- adding them.
        "choices": lambda p: [min(p["a"], p["b"]), max(p["a"], p["b"]),
                              p["a"] + p["b"]],
    },
    "c20": {   # count a group that runs past ten (the picture IS the problem)
        "ans": lambda p: p["a"],
        "spoken": lambda p: "Count the stars. How many stars are there?",
        "board": lambda p: (f'[[objects emoji="⭐" groups="{p["a"]}" '
                            f'caption="ten first, then count on"]]'),
        "praise": lambda p: f"{_plural(p['a'], 'star')} — you counted past ten.",
        "key": lambda p: p["a"],
        "check": lambda p: (11 <= p["a"] <= 20,
                            "past ten, and still countable on one screen"),
        # same reasoning as "cnt": saying the number would answer the question.
        "speaks": lambda p, sp: True,
    },
    "dbe": {   # a double: a and a again
        "ans": lambda p: 2 * p["a"],
        "spoken": lambda p: f"What is {p['a']} plus {p['a']}?",
        "board": lambda p: f'[[step eq="{p["a"]} + {p["a"]} = ?"]]',
        "praise": lambda p: (f"{p['a']} plus {p['a']} equals {2 * p['a']} — "
                             f"that is a double."),
        "key": lambda p: p["a"],
        "check": lambda p: (1 <= p["a"] <= 10, "the double stays inside twenty"),
        "speaks": lambda p, sp: str(p["a"]) in sp,
    },
    "add3": {  # three single digits in one go
        "ans": lambda p: p["a"] + p["b"] + p["c"],
        "spoken": lambda p: (f"What is {p['a']} plus {p['b']} plus {p['c']}?"),
        "board": lambda p: (f'[[step eq="{p["a"]} + {p["b"]} + {p["c"]} = ?"]]'),
        "praise": lambda p: (f"{p['a']} plus {p['b']} plus {p['c']} equals "
                             f"{p['a'] + p['b'] + p['c']}."),
        "key": lambda p: p["a"] + p["b"] + p["c"],
        "check": lambda p: (1 <= p["a"] <= 9 and 1 <= p["b"] <= 9
                            and 1 <= p.get("c", 0) <= 9
                            and p["a"] + p["b"] + p["c"] <= 20,
                            "three single digits whose total stays inside twenty"),
    },
    "msp": {   # the missing part: a and how many more make b
        "ans": lambda p: p["b"] - p["a"],
        "spoken": lambda p: f"{p['a']} and how many more make {p['b']}?",
        "board": lambda p: f'[[step eq="{p["a"]} + ? = {p["b"]}"]]',
        "praise": lambda p: (f"{p['a']} and {p['b'] - p['a']} more make {p['b']}."),
        "key": lambda p: p["b"] - p["a"],
        "check": lambda p: (1 <= p["a"] < p["b"] <= 20,
                            "the whole is under twenty and the part is smaller"),
    },
    "t10": {   # ten more than a
        "ans": lambda p: p["a"] + 10,
        "spoken": lambda p: f"What is ten more than {p['a']}?",
        "board": lambda p: f'[[step eq="{p["a"]} + 10 = ?"]]',
        "praise": lambda p: (f"Ten more than {p['a']} is {p['a'] + 10} — only the "
                             f"tens digit changed."),
        "key": lambda p: p["a"],
        "check": lambda p: (10 <= p["a"] <= 89, "the answer stays under a hundred"),
        "speaks": lambda p, sp: str(p["a"]) in sp,
    },
    "wor": {   # what the TENS digit of a three-digit number is worth
        "ans": lambda p: 10 * p["b"],
        "spoken": lambda p: (f"In the number {100 * p['a'] + 10 * p['b'] + p['c']}, "
                             f"what is the {p['b']} worth?"),
        "board": lambda p: (f'[[step eq="{100 * p["a"] + 10 * p["b"] + p["c"]} → '
                            f'the {p["b"]} is worth ?"]]'),
        "praise": lambda p: (f"The {p['b']} sits in the tens place, so it is worth "
                             f"{10 * p['b']}."),
        "key": lambda p: p["b"],
        "check": lambda p: (1 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and 1 <= p.get("c", 0) <= 9
                            and p["b"] != p["a"] and p["b"] != p["c"],
                            "the tens digit appears once, so the question has one "
                            "possible reading"),
        # the whole lesson is WHICH PLACE it sits in, so the distractors are the
        # same digit read in the other two places.
        "choices": lambda p: [p["b"], 10 * p["b"], 100 * p["b"]],
    },
    "a3d": {   # three-digit plus three-digit, no column carrying
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: f"What is {p['a']} plus {p['b']}?",
        "board": lambda p: f'[[step eq="{p["a"]} + {p["b"]} = ?"]]',
        "praise": lambda p: f"{p['a']} plus {p['b']} equals {p['a'] + p['b']}.",
        "key": lambda p: p["a"] + p["b"],
        "check": lambda p: (100 <= p["a"] <= 899 and 100 <= p["b"] <= 899
                            and p["a"] % 10 + p["b"] % 10 <= 9
                            and (p["a"] // 10) % 10 + (p["b"] // 10) % 10 <= 9
                            and p["a"] + p["b"] <= 999,
                            "three digits each, and not one column carries"),
    },
    "c2h": {   # two-digit plus two-digit that crosses one hundred
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: f"What is {p['a']} plus {p['b']}?",
        "board": lambda p: f'[[step eq="{p["a"]} + {p["b"]} = ?"]]',
        "praise": lambda p: (f"{p['a']} plus {p['b']} equals {p['a'] + p['b']} — "
                             f"it went past one hundred."),
        "key": lambda p: p["a"] + p["b"],
        "check": lambda p: (10 <= p["a"] <= 99 and 10 <= p["b"] <= 99
                            and 100 <= p["a"] + p["b"] <= 199,
                            "both two-digit, and the answer crosses one hundred"),
    },
    "s2d": {   # two-digit take away, no column regrouping
        "ans": lambda p: p["a"] - p["b"],
        "spoken": lambda p: f"What is {p['a']} take away {p['b']}?",
        "board": lambda p: f'[[step eq="{p["a"]} − {p["b"]} = ?"]]',
        "praise": lambda p: (f"{p['a']} take away {p['b']} equals "
                             f"{p['a'] - p['b']}."),
        "key": lambda p: p["a"] - p["b"],
        "check": lambda p: (20 <= p["a"] <= 99 and 10 <= p["b"] < p["a"]
                            and p["a"] % 10 >= p["b"] % 10
                            and p["a"] // 10 > p["b"] // 10,
                            "two digits each, and no column needs regrouping"),
    },
    "s3d": {   # three-digit take away, no column regrouping
        "ans": lambda p: p["a"] - p["b"],
        "spoken": lambda p: f"What is {p['a']} take away {p['b']}?",
        "board": lambda p: f'[[step eq="{p["a"]} − {p["b"]} = ?"]]',
        "praise": lambda p: (f"{p['a']} take away {p['b']} equals "
                             f"{p['a'] - p['b']}."),
        "key": lambda p: p["a"] - p["b"],
        "check": lambda p: (200 <= p["a"] <= 999 and 100 <= p["b"] < p["a"]
                            and p["a"] % 10 >= p["b"] % 10
                            and (p["a"] // 10) % 10 >= (p["b"] // 10) % 10,
                            "three digits each, and no column needs regrouping"),
    },
    "chk": {   # check a take away by adding the answer back
        "ans": lambda p: p["a"],
        "spoken": lambda p: (f"Someone worked out {p['a']} take away {p['b']} and "
                             f"got {p['a'] - p['b']}. Add {p['a'] - p['b']} and "
                             f"{p['b']} to check. What do you get?"),
        "board": lambda p: f'[[step eq="{p["a"] - p["b"]} + {p["b"]} = ?"]]',
        "praise": lambda p: (f"{p['a'] - p['b']} plus {p['b']} equals {p['a']}, the "
                             f"number they started with, so the take away was right."),
        "key": lambda p: p["a"],
        "check": lambda p: (20 <= p["a"] <= 99 and 10 <= p["b"] < p["a"],
                            "a two-digit take away with something left to check"),
    },
    "qtr": {   # a quarters + b pennies = ? cents
        "ans": lambda p: 25 * p["a"] + p["b"],
        "spoken": lambda p: (f"How many cents is {_plural(p['a'], 'quarter')} and "
                             f"{_irr(p['b'], 'penny', 'pennies')}?"),
        "board": lambda p: (f'[[step eq="{p["a"]} quarters + {p["b"]} pennies '
                            f'= ? cents"]]'),
        "praise": lambda p: (f"{_plural(p['a'], 'quarter')} and "
                             f"{_irr(p['b'], 'penny', 'pennies')} equals "
                             f"{25 * p['a'] + p['b']} cents."),
        "key": lambda p: 25 * p["a"] + p["b"],
        "check": lambda p: (1 <= p["a"] <= 4 and 1 <= p["b"] <= 9,
                            "up to a dollar in quarters, and loose pennies"),
    },
    "chg": {   # pay a cents for something costing b cents -- the change
        "ans": lambda p: p["a"] - p["b"],
        "spoken": lambda p: (f"A toy costs {p['b']} cents. You pay {p['a']} cents. "
                             f"How much change do you get?"),
        "board": lambda p: (f'[[step eq="{p["a"]} − {p["b"]} = ? cents change"]]'),
        "praise": lambda p: (f"{p['a']} take away {p['b']} equals "
                             f"{_plural(p['a'] - p['b'], 'cent')} change."),
        "key": lambda p: p["a"] - p["b"],
        "check": lambda p: (p["a"] in (25, 50, 100) and 5 <= p["b"] < p["a"],
                            "you pay with one real coin and there is change to give"),
    },
    "*": {
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: f"What is {p['a']} times {p['b']}?",
        "board": _mul_board,          # (sr) the array while the lesson is about meaning
        "worked": _mul_worked,        # (sr) array, or the area model split into tens and ones
        "choices": _mul_choices,      # (sz) the neighbouring FACTS, not the neighbouring numbers
        "praise": lambda p: f"{p['a']} times {p['b']} equals {p['a'] * p['b']}.",
        "key": lambda p: p["a"] * p["b"],
        "check": lambda p: (p["a"] >= 1 and p["b"] >= 1, "factors must be at least 1"),
    },
    "/": {
        "ans": lambda p: p["a"] // p["b"],
        "spoken": lambda p: f"What is {p['a']} divided by {p['b']}?",
        "board": _div_board,          # (ss) the sharing question as a picture, when small
        "worked": _div_worked,        # (ss) the groups filled, or the area model backwards
        "praise": lambda p: f"{p['a']} divided by {p['b']} equals {p['a'] // p['b']}.",
        "key": lambda p: p["a"],
        "check": lambda p: (p["a"] % p["b"] == 0 and p["b"] >= 2,
                            "a division lesson must divide EXACTLY"),
    },
    "rem": {
        "ans": lambda p: p["a"] % p["b"],
        "spoken": lambda p: (f"What is left over when {p['a']} is shared into "
                             f"groups of {p['b']}?"),
        "board": _rem_board,          # (ss) the dots to share and the full-group boxes
        "worked": _rem_worked,        # (ss) the full groups and the red left-overs
        "praise": lambda p: (f"Sharing {p['a']} into groups of {p['b']} leaves "
                             f"{p['a'] % p['b']} left over."),
        "key": lambda p: p["a"],
        "check": lambda p: (1 <= p["a"] % p["b"] < p["b"],
                            "the left-over must be at least 1 (tap options start "
                            "at 1) and smaller than the group"),
    },
    "mf": {   # missing factor: b × ? = a
        "ans": lambda p: p["a"] // p["b"],
        "spoken": lambda p: f"{p['b']} times what equals {p['a']}?",
        "board": _mf_board,           # (st) b boxes, a dots: b groups of WHAT reach a?
        "worked": _mf_worked,
        "praise": lambda p: f"{p['b']} times {p['a'] // p['b']} equals {p['a']}.",
        "key": lambda p: p["a"],
        "check": lambda p: (p["a"] % p["b"] == 0 and p["b"] >= 2,
                            "the missing factor must be exact"),
    },
    "gcf": {
        "ans": lambda p: _gcd(p["a"], p["b"]),
        "spoken": lambda p: (f"What is the greatest common factor of {p['a']} "
                             f"and {p['b']}?"),
        "board": lambda p: f'[[step eq="GCF of {p["a"]} and {p["b"]} = ?"]]',
        "worked": _gcf_worked,        # (st) the two factor lists on a Venn
        "praise": lambda p: (f"The greatest common factor of {p['a']} and "
                             f"{p['b']} equals {_gcd(p['a'], p['b'])}."),
        "key": lambda p: max(p["a"], p["b"]),
        "check": lambda p: (_gcd(p["a"], p["b"]) >= 2,
                            "a GCF of 1 makes a dull tap question"),
    },
    "of": {   # one unit-fraction of a group: 1/b of a
        "ans": lambda p: p["a"] // p["b"],
        "spoken": lambda p: (f"What is one {_FRACWORD[p['b']][0]} of {p['a']}?"),
        "board": _of_board,           # (su) the array shared into b equal parts
        "worked": _of_worked,
        "praise": lambda p: (f"One {_FRACWORD[p['b']][0]} of {p['a']} equals "
                             f"{p['a'] // p['b']}."),
        "key": lambda p: p["a"],
        "check": lambda p: (p["a"] % p["b"] == 0 and p["b"] in _FRACWORD,
                            "the share must be exact and the fraction sayable"),
        "speaks": lambda p, sp: str(p["a"]) in sp and _FRACWORD[p["b"]][0] in sp,
    },
    "eqf": {   # 1/b = ?/c
        "ans": lambda p: p["c"] // p["b"],
        "spoken": lambda p: (f"One {_FRACWORD[p['b']][0]} equals how many "
                             f"{_FRACWORD[p['c']][1]}?"),
        "board": _eqf_board,          # (su) two pies: one shaded, the other cut finer and empty
        "worked": _eqf_worked,
        "praise": lambda p: (f"One {_FRACWORD[p['b']][0]} equals "
                             f"{_NUMWORD[p['c'] // p['b']]} {_FRACWORD[p['c']][1]}."),
        "key": lambda p: p["c"],
        "check": lambda p: (p["c"] % p["b"] == 0 and p["b"] in _FRACWORD
                            and p["c"] in _FRACWORD and p["c"] > p["b"]
                            and p["c"] // p["b"] in _NUMWORD,
                            "the equivalence must be exact and sayable"),
        "speaks": lambda p, sp: (_FRACWORD[p["b"]][0] in sp
                                 and _FRACWORD[p["c"]][1] in sp),
    },
    "fa": {   # a/c + b/c, answered in c-ths
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"How many {_FRACWORD[p['c']][1]} is "
                             f"{_fw(p['a'], p['c'])} plus {_fw(p['b'], p['c'])}?"),
        "board": _fa_board,           # (sv) the fraction line, start marked, hop withheld
        "worked": _fa_worked,
        "praise": lambda p: (f"{_fw(p['a'], p['c'])} plus {_fw(p['b'], p['c'])} "
                             f"equals {_fw(p['a'] + p['b'], p['c'])}."),
        "key": lambda p: p["a"] + p["b"],
        "check": lambda p: (p["a"] + p["b"] < p["c"] and p["c"] in _FRACWORD,
                            "same-bottom adding stays a proper fraction"),
    },
    "fs": {   # a/c - b/c
        "ans": lambda p: p["a"] - p["b"],
        "spoken": lambda p: (f"How many {_FRACWORD[p['c']][1]} is "
                             f"{_fw(p['a'], p['c'])} take away "
                             f"{_fw(p['b'], p['c'])}?"),
        "board": _fs_board,           # (sv) the fraction line, start marked, hop withheld
        "worked": _fs_worked,
        "praise": lambda p: (f"{_fw(p['a'], p['c'])} take away "
                             f"{_fw(p['b'], p['c'])} equals "
                             f"{_fw(p['a'] - p['b'], p['c'])}."),
        "key": lambda p: p["a"],
        "check": lambda p: (1 <= p["a"] - p["b"] and p["a"] < p["c"]
                            and p["c"] in _FRACWORD,
                            "same-bottom take-away stays proper and positive"),
    },
    "dt": {   # tenths: 0.a + 0.b, answered in tenths
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"How many tenths is {_fw(p['a'], 10)} plus "
                             f"{_fw(p['b'], 10)}?"),
        "board": _dt_board,           # (sw) the tenths line, start marked, hop withheld
        "worked": _dt_worked,
        "praise": lambda p: (f"{_fw(p['a'], 10)} plus {_fw(p['b'], 10)} equals "
                             f"{_fw(p['a'] + p['b'], 10)}."),
        "key": lambda p: p["a"] + p["b"],
        "check": lambda p: (p["a"] + p["b"] <= 9,
                            "the tenths must not spill into a whole (that is the "
                            "NEXT lesson's idea)"),
    },
    "m": {    # money: a dimes + b pennies = ? cents
        "ans": lambda p: 10 * p["a"] + p["b"],
        "spoken": lambda p: (f"How many cents is {_plural(p['a'], 'dime')} and "
                             f"{_irr(p['b'], 'penny', 'pennies')}?"),
        "board": _m_board,            # (sw) the place-value chart: dimes are tens
        "worked": _m_worked,
        "praise": lambda p: (f"{_plural(p['a'], 'dime')} and "
                             f"{_irr(p['b'], 'penny', 'pennies')} equals "
                             f"{10 * p['a'] + p['b']} cents."),
        "key": lambda p: 10 * p["a"] + p["b"],
        "check": lambda p: (1 <= p["a"] <= 9 and 1 <= p["b"] <= 9,
                            "dimes and pennies each stay single-digit"),
    },
    "pc": {   # a% of b
        "ans": lambda p: p["a"] * p["b"] // 100,
        "spoken": lambda p: f"What is {p['a']} percent of {p['b']}?",
        "board": _pc_board,           # (sx) the sharing picture: a percent is one of the parts
        "worked": _pc_worked,
        "praise": lambda p: (f"{p['a']} percent of {p['b']} equals "
                             f"{p['a'] * p['b'] // 100}."),
        "key": lambda p: p["b"],
        "check": lambda p: ((p["a"] * p["b"]) % 100 == 0
                            and p["a"] * p["b"] // 100 >= 1,
                            "the percent must come out whole, and at least 1"),
    },
    "rate": {  # b things cost a dollars; one costs?
        "ans": lambda p: p["a"] // p["b"],
        "spoken": lambda p: (f"{p['b']} apples cost {p['a']} dollars. What does "
                             f"one apple cost, in dollars?"),
        "board": _rate_board,         # (sx) the dollars shared over the apples
        "worked": _rate_worked,
        "praise": lambda p: (f"{p['a']} divided by {p['b']} equals "
                             f"{p['a'] // p['b']} — one costs "
                             f"{p['a'] // p['b']} dollars."),
        "key": lambda p: p["a"],
        "check": lambda p: (p["a"] % p["b"] == 0 and p["b"] >= 2,
                            "a unit price must come out exact"),
    },
    "pv": {   # a hundreds, b tens, c ones
        "ans": lambda p: 100 * p["a"] + 10 * p["b"] + p["c"],
        "spoken": lambda p: (f"What number is {_plural(p['a'], 'hundred')}, "
                             f"{_plural(p['b'], 'ten')} and "
                             f"{_plural(p['c'], 'one')}?"),
        # (sq, 2026-09-05) the place-value chart, digits hidden: the student reads
        # the blocks. The walk-back shows the same chart with the digits and the sum.
        "board": lambda p: (f'[[placevalue h="{p["a"]}" t="{p["b"]}" o="{p["c"]}" ask="1" '
                            f'caption="count the blocks in each place"]]'
                            f'[[step eq="{p["a"]} hundreds + {p["b"]} tens + '
                            f'{p["c"]} ones = ?"]]'),
        "worked": lambda p: (f"Look what you did: {_plural(p['a'], 'hundred')} is "
                             f"{100 * p['a']}, {_plural(p['b'], 'ten')} is {10 * p['b']}, "
                             f"and {_plural(p['c'], 'one')} is {p['c']}. Put together: "
                             f"{100 * p['a'] + 10 * p['b'] + p['c']}.",
                             f'[[placevalue h="{p["a"]}" t="{p["b"]}" o="{p["c"]}" '
                             f'caption="{100 * p["a"]} + {10 * p["b"]} + {p["c"]} = '
                             f'{100 * p["a"] + 10 * p["b"] + p["c"]}"]]'),
        "praise": lambda p: (f"{_plural(p['a'], 'hundred')}, "
                             f"{_plural(p['b'], 'ten')} and {_plural(p['c'], 'one')}"
                             f" — that is {100 * p['a'] + 10 * p['b'] + p['c']}."),
        "key": lambda p: 100 * p["a"] + 10 * p["b"] + p["c"],
        "check": lambda p: (1 <= p["a"] <= 9 and 1 <= p["b"] <= 9
                            and 1 <= p["c"] <= 9,
                            "each place stays 1-9 in this first lesson"),
    },
    "r10": {   # round a to the nearest ten
        "ans": lambda p: (p["a"] + 5) // 10 * 10,
        "spoken": lambda p: f"Round {p['a']} to the nearest ten.",
        # (sp, 2026-09-05) Jim: "we should have a number line anytime we talk about
        # rounding." The ask draws the number between its two tens with the halfway
        # mark -- the point and no hop, so the picture is the TOOL, not the answer.
        "board": lambda p: (_r10_line(p["a"], hop=False)
                            + f'[[step eq="{p["a"]} → nearest ten = ?"]]'),
        "praise": lambda p: (f"{p['a']} rounds to {(p['a'] + 5) // 10 * 10}."),
        # (sp) THE WALK-BACK, ruling ⑤: after a right answer the board shows what the
        # student just did -- the hop on the number line -- and the words read it off.
        "worked": lambda p: (_r10_walkback(p["a"]), _r10_line(p["a"], hop=True)),
        "key": lambda p: p["a"],
        "check": lambda p: (10 <= p["a"] <= 99 and p["a"] % 10 != 0,
                            "a multiple of ten leaves nothing to round"),
        "speaks": lambda p, sp: str(p["a"]) in sp,
        # +-1 distractors would make rounding guessable by eye; the real confusion
        # is WHICH ten, so the distractors are the neighbouring tens.
        # near the bottom of the range the lower ten would be 0 -- shift the
        # window up instead (tap options must stay >= 1, validator-enforced)
        "choices": lambda p: ([(p["a"] + 5) // 10 * 10 - 10,
                               (p["a"] + 5) // 10 * 10,
                               (p["a"] + 5) // 10 * 10 + 10]
                              if (p["a"] + 5) // 10 * 10 >= 20 else
                              [(p["a"] + 5) // 10 * 10,
                               (p["a"] + 5) // 10 * 10 + 10,
                               (p["a"] + 5) // 10 * 10 + 20]),
    },
    "r100": {  # round a to the nearest hundred
        "ans": lambda p: (p["a"] + 50) // 100 * 100,
        "spoken": lambda p: f"Round {p['a']} to the nearest hundred.",
        # (sq) the number line between the two hundreds, halfway marked, no hop
        "board": lambda p: (_r100_line(p["a"], hop=False)
                            + f'[[step eq="{p["a"]} → nearest hundred = ?"]]'),
        "worked": lambda p: (_r100_walkback(p["a"]), _r100_line(p["a"], hop=True)),
        "praise": lambda p: (f"{p['a']} rounds to {(p['a'] + 50) // 100 * 100}."),
        "key": lambda p: p["a"],
        "check": lambda p: (100 <= p["a"] <= 999 and p["a"] % 100 != 0,
                            "a multiple of one hundred leaves nothing to round"),
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "choices": lambda p: ([(p["a"] + 50) // 100 * 100 - 100,
                               (p["a"] + 50) // 100 * 100,
                               (p["a"] + 50) // 100 * 100 + 100]
                              if (p["a"] + 50) // 100 * 100 >= 200 else
                              [(p["a"] + 50) // 100 * 100,
                               (p["a"] + 50) // 100 * 100 + 100,
                               (p["a"] + 50) // 100 * 100 + 200]),
    },
    "nl": {    # hops from 0 to a/b on a 0-to-1 number line cut into b hops
        "ans": lambda p: p["a"],
        "spoken": lambda p: (f"A number line from 0 to 1 is cut into {p['b']} "
                             f"equal hops. How many hops from 0 reach {p['a']} "
                             f"out of {p['b']}?"),
        "board": _nl_board,           # (su) the fraction line, hops withheld
        "worked": _nl_worked,
        "praise": lambda p: (f"{_plural(p['a'], 'hop')} — {p['a']} out of "
                             f"{p['b']} lives {_plural(p['a'], 'hop')} from 0."),
        "key": lambda p: p["b"],
        "check": lambda p: (1 <= p["a"] < p["b"] <= 12,
                            "the fraction stays proper and the hops countable"),
    },
    "nlw": {   # hops from 0 to reach 1 whole
        "ans": lambda p: p["b"],
        "spoken": lambda p: (f"A number line from 0 to 1 is cut into {p['b']} "
                             f"equal hops. How many hops from 0 reach 1 whole?"),
        "board": _nlw_board,          # (su) the fraction line, hops withheld
        "worked": _nlw_worked,
        "praise": lambda p: (f"{p['b']} hops — all {p['b']} hops together equal "
                             f"1 whole."),
        "key": lambda p: p["b"],
        "check": lambda p: (2 <= p["b"] <= 12 and p.get("a", 1) == 1,
                            "the whole-line question fixes a=1"),
    },
    "cnt": {   # count the stars (concrete-only; the picture IS the problem)
        "ans": lambda p: p["a"],
        "spoken": lambda p: "Count the stars. How many stars are there?",
        "board": lambda p: (f'[[objects emoji="⭐" groups="{p["a"]}" '
                            f'caption="count them one at a time"]]'),
        "praise": lambda p: f"{_plural(p['a'], 'star')} — you counted every one.",
        "key": lambda p: p["a"],
        "check": lambda p: (1 <= p["a"] <= 10, "countable on one screen"),
        # rule 44's PURPOSE is "the child heard the whole problem" -- here the whole
        # problem is the picture, and SAYING the number would answer it.
        "speaks": lambda p, sp: True,
    },
    "aft": {
        "ans": lambda p: p["a"] + 1,
        "spoken": lambda p: f"What number comes right after {p['a']}?",
        "board": lambda p: f'[[step eq="{p["a"]}, ?"]]',
        "praise": lambda p: f"{p['a'] + 1} comes right after {p['a']}.",
        "key": lambda p: p["a"],
        "check": lambda p: (1 <= p["a"] <= 19, "stays in the counting range"),
        # the problem has ONE number; b is a placeholder 0 (like r10/r100)
        "speaks": lambda p, sp: str(p["a"]) in sp,
    },
    "bef": {
        "ans": lambda p: p["a"] - 1,
        "spoken": lambda p: f"What number comes right before {p['a']}?",
        "board": lambda p: f'[[step eq="?, {p["a"]}"]]',
        "praise": lambda p: f"{p['a'] - 1} comes right before {p['a']}.",
        "key": lambda p: p["a"],
        "check": lambda p: (2 <= p["a"] <= 20, "the answer must stay at least 1"),
        "speaks": lambda p, sp: str(p["a"]) in sp,
    },
    "nick": {  # a nickels + b pennies = ? cents
        "ans": lambda p: 5 * p["a"] + p["b"],
        "spoken": lambda p: (f"How many cents is {_plural(p['a'], 'nickel')} and "
                             f"{_irr(p['b'], 'penny', 'pennies')}?"),
        "board": lambda p: f'[[step eq="{p["a"]} nickels + {p["b"]} pennies = ? cents"]]',
        "praise": lambda p: (f"{_plural(p['a'], 'nickel')} and "
                             f"{_irr(p['b'], 'penny', 'pennies')} equals "
                             f"{5 * p['a'] + p['b']} cents."),
        "key": lambda p: 5 * p["a"] + p["b"],
        "check": lambda p: (1 <= p["a"] <= 9 and 1 <= p["b"] <= 4,
                            "pennies stay under a nickel"),
    },
    # ---- (mp) ENTRY-LEVEL UNIT 9: SHAPES, PATTERNS & GROUPS --------------------
    # The LAST unscripted unit in the curriculum. Same rule as Unit 8: nothing here
    # is a new KIND of arithmetic. sid/cor are counting. pat is counting on by a
    # fixed step -- the skip counting U7 and U8 already built. grp and eqs are the
    # honest precursors to multiplying and dividing, taught as REPEATED ADDITION and
    # FAIR SHARING and never with the word "times", because Basic Math Unit 2 is
    # where multiplying is taught and a child should meet the IDEA before the word.
    "sid": {   # how many sides does a <shape> have?
        "ans": lambda p: p["a"],
        "spoken": lambda p: f"How many sides does a {_SHAPE[p['a']]} have?",
        "board": lambda p: f'[[step eq="{_SHAPE[p["a"]]} → ? sides"]]',
        "praise": lambda p: f"A {_SHAPE[p['a']]} has {p['a']} sides.",
        "key": lambda p: p["a"],
        "check": lambda p: (p["a"] in _SHAPE and p.get("b", 0) == 0,
                            "it has to be a shape the lesson can name"),
        # rule 44's PURPOSE is "the child heard the whole problem". The NAME is the
        # whole problem here, and saying the number would answer it -- the same
        # reasoning cnt's override documents.
        "speaks": lambda p, sp: _SHAPE[p["a"]] in sp,
    },
    "cor": {   # how many corners does a <shape> have? -- the SAME number, and that
               # is the lesson: a child who notices never has to count twice
        "ans": lambda p: p["a"],
        "spoken": lambda p: f"How many corners does a {_SHAPE[p['a']]} have?",
        "board": lambda p: f'[[step eq="{_SHAPE[p["a"]]} → ? corners"]]',
        "praise": lambda p: (f"A {_SHAPE[p['a']]} has {p['a']} corners — the same "
                             f"as its sides."),
        "key": lambda p: p["a"],
        "check": lambda p: (p["a"] in _SHAPE and p.get("b", 0) == 0,
                            "it has to be a shape the lesson can name"),
        "speaks": lambda p, sp: _SHAPE[p["a"]] in sp,
    },
    "pat": {   # a, a+b, a+2b, a+3b -- what comes next?
        "ans": lambda p: p["a"] + 4 * p["b"],
        "spoken": lambda p: (f"The pattern is {p['a']}, {p['a'] + p['b']}, "
                             f"{p['a'] + 2 * p['b']}, {p['a'] + 3 * p['b']}. "
                             f"What comes next?"),
        "board": lambda p: (f'[[step eq="{p["a"]}, {p["a"] + p["b"]}, '
                            f'{p["a"] + 2 * p["b"]}, {p["a"] + 3 * p["b"]}, ?"]]'),
        "praise": lambda p: (f"{p['a'] + 4 * p['b']} — the pattern goes up by "
                             f"{p['b']} every time."),
        "key": lambda p: p["b"],
        "check": lambda p: (1 <= p["a"] <= 10 and 1 <= p["b"] <= 5,
                            "the step is countable and the pattern starts small"),
        # THE STEP IS NEVER SPOKEN -- finding it is the whole question.
        "speaks": lambda p, sp: str(p["a"]) in sp,
    },
    "grp": {   # a groups of b -- how many in all? (repeated addition, NOT "times")
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: (f"There are {p['a']} groups with {p['b']} stars in "
                             f"each group. How many stars are there in all?"),
        "board": lambda p: f'[[step eq="{p["a"]} groups of {p["b"]} = ?"]]',
        "praise": lambda p: (f"{p['a']} groups of {p['b']} is {p['a'] * p['b']} "
                             f"stars in all."),
        "key": lambda p: p["a"] * p["b"],
        "check": lambda p: (2 <= p["a"] <= 5 and 2 <= p["b"] <= 5,
                            "few enough groups to count, and none of them empty"),
    },
    "eqs": {   # a stars shared into b equal groups -- how many in each?
        "ans": lambda p: p["a"] // p["b"],
        "spoken": lambda p: (f"{p['a']} stars are shared fairly into {p['b']} "
                             f"equal groups. How many stars are in each group?"),
        "board": lambda p: (f'[[step eq="{p["a"]} shared into {p["b"]} equal '
                            f'groups = ? each"]]'),
        "praise": lambda p: (f"{p['a']} shared into {p['b']} equal groups is "
                             f"{p['a'] // p['b']} in each group."),
        "key": lambda p: p["a"],
        "check": lambda p: (2 <= p["b"] <= 5 and p["a"] % p["b"] == 0
                            and 2 <= p["a"] // p["b"] <= 6,
                            "fair sharing leaves nothing over -- remainders are "
                            "Basic Math's lesson, not this one"),
    },
    # ---- (mo) ENTRY-LEVEL UNIT 8: TIME, CALENDAR & MEASUREMENT -----------------
    # Four ops for the first unit of the curriculum that had no scripted lessons at
    # all. Each is deliberately shaped like something the child has ALREADY met:
    # hrl counts on (U2/U3), min5 counts by five exactly as nick does for coins
    # (U7), dwd is nick's shape with sevens instead of fives, and cube is taking
    # away (U3) with a ruler under it.
    "hrl": {   # it is a o'clock; what time b hours later?
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"It is {p['a']} o'clock. What time will it be "
                             f"{_plural(p['b'], 'hour')} later?"),
        "board": lambda p: (f'[[numberline min="1" max="12" points="{p["a"]}"]]'
                            f'[[step eq="{p["a"]} o\'clock, {p["b"]} hours later = ?"]]'),
        "praise": lambda p: (f"{_plural(p['b'], 'hour')} after {p['a']} o'clock "
                             f"is {p['a'] + p['b']} o'clock."),
        "key": lambda p: p["a"] + p["b"],
        # The clock face a child reads goes to 12 and no further. Wrapping past it
        # ("11 o'clock plus 3 is 2 o'clock") is a real idea and NOT this lesson's --
        # it needs the twelve-hour circle taught first, which Unit 8 does not do.
        "check": lambda p: (1 <= p["a"] <= 11 and 1 <= p["b"] <= 6
                            and p["a"] + p["b"] <= 12,
                            "the hand stays on the clock face, 1 through 12"),
    },
    "min5": {  # the minute hand points at a; how many minutes past?
        "ans": lambda p: 5 * p["a"],
        "spoken": lambda p: (f"The minute hand points to {p['a']}. How many "
                             f"minutes past the hour is that?"),
        "board": lambda p: (f'[[step eq="{p["a"]} numbers past 12, five minutes '
                            f'each = ? minutes"]]'),
        "praise": lambda p: (f"{p['a']} times five equals {5 * p['a']} minutes."),
        "key": lambda p: p["a"],
        "check": lambda p: (1 <= p["a"] <= 11 and p.get("b", 0) == 0,
                            "the minute hand points at a clock number, and this "
                            "problem has only one"),
        # b is a placeholder 0 -- the same shape r10/aft/bef use.
        "speaks": lambda p, sp: str(p["a"]) in sp,
        # ⚠️ THE NEIGHBOURS CANNOT BE +-1 HERE. Every answer is a multiple of five,
        # so 19 | 20 | 21 hands the answer to a child who has merely noticed that.
        # The honest distractors are the neighbouring five-minute marks.
        "choices": lambda p: ([5 * p["a"] - 5, 5 * p["a"], 5 * p["a"] + 5]
                              if p["a"] >= 2 else
                              [5, 10, 15]),
    },
    "min5q": {  # the reverse: a minutes past -> which clock number?
        # ⚠️ WHY THE REVERSE FORM EXISTS. min5 alone has ELEVEN distinct problems --
        # the minute hand points at 1 through 11 and there is no twelfth -- which is
        # not enough for a bank of twelve plus two worked pairs. ang/angq hit exactly
        # this wall in build kd and solved it the same way. It also happens to be
        # better teaching: a child who can only go one direction has memorised a
        # list, not learned to read a clock.
        "ans": lambda p: p["a"] // 5,
        "spoken": lambda p: (f"The minute hand is {p['a']} minutes past the hour. "
                             f"Which clock number is it pointing to?"),
        "board": lambda p: (f'[[step eq="{p["a"]} minutes, five minutes each '
                            f'= ? on the clock"]]'),
        "praise": lambda p: (f"{p['a']} minutes is the {p['a'] // 5} on the "
                             f"clock — five minutes for each number."),
        "key": lambda p: p["a"] // 5,
        "check": lambda p: (5 <= p["a"] <= 55 and p["a"] % 5 == 0
                            and p.get("b", 0) == 0,
                            "the minute hand lands ON a clock number, so the "
                            "minutes are a count of fives"),
        "speaks": lambda p, sp: str(p["a"]) in sp,
    },
    "dwd": {   # a weeks and b days = ? days   (nick's shape, with sevens)
        "ans": lambda p: 7 * p["a"] + p["b"],
        "spoken": lambda p: (f"How many days are in {p['a']} "
                             f"{'week' if p['a'] == 1 else 'weeks'} and "
                             f"{p['b']} {'day' if p['b'] == 1 else 'days'}?"),
        "board": lambda p: (f'[[step eq="{p["a"]} weeks and {p["b"]} days '
                            f'= ? days"]]'),
        "praise": lambda p: (f"{_plural(p['a'], 'week')} and "
                             f"{_plural(p['b'], 'day')} equals "
                             f"{7 * p['a'] + p['b']} days."),
        "key": lambda p: 7 * p["a"] + p["b"],
        "check": lambda p: (1 <= p["a"] <= 4 and 1 <= p["b"] <= 6,
                            "the loose days stay under a week, or they are "
                            "another week"),
    },
    "cube": {  # a cubes long against b cubes long: how many cubes longer?
        "ans": lambda p: p["a"] - p["b"],
        "spoken": lambda p: (f"The pencil is {_plural(p['a'], 'cube')} long. The "
                             f"crayon is {_plural(p['b'], 'cube')} long. How many "
                             f"cubes longer is the pencil?"),
        "board": lambda p: (f'[[bars data="pencil:{p["a"]} | crayon:{p["b"]}"]]'
                            f'[[step eq="{p["a"]} cubes − {p["b"]} cubes = ?"]]'),
        "praise": lambda p: (f"{_plural(p['a'], 'cube')} take away "
                             f"{_plural(p['b'], 'cube')} — the pencil is "
                             f"{_plural(p['a'] - p['b'], 'cube')} longer."),
        "key": lambda p: p["a"],
        "check": lambda p: (2 <= p["a"] <= 20 and 1 <= p["b"] < p["a"],
                            "the pencil is the longer one, and both are "
                            "measurable in cubes"),
    },
    "dh": {    # hundredths: 0.ab + 0.cd, answered in hundredths
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"How many hundredths is {p['a']} hundredths plus "
                             f"{p['b']} hundredths?"),
        "board": _dh_board,           # (sw) the hundredths square, total withheld
        "worked": _dh_worked,
        "praise": lambda p: (f"{p['a']} hundredths plus {p['b']} hundredths "
                             f"equals {p['a'] + p['b']} hundredths."),
        "key": lambda p: p["a"] + p["b"],
        "check": lambda p: (10 <= p["a"] <= 89 and 10 <= p["b"] <= 89
                            and p["a"] + p["b"] <= 99,
                            "two-digit hundredths, no spill into a whole"),
    },
    "fu": {    # one 1/b plus a/c, same-family bottoms (b divides c)
        "ans": lambda p: p["c"] // p["b"] + p["a"],
        "spoken": lambda p: (f"How many {_FRACWORD[p['c']][1]} is one "
                             f"{_FRACWORD[p['b']][0]} plus "
                             f"{_fw(p['a'], p['c'])}?"),
        "board": _fu_board,           # (sv) the finer line, the first fraction found on it
        "worked": _fu_worked,
        "praise": lambda p: (f"One {_FRACWORD[p['b']][0]} is "
                             f"{_fw(p['c'] // p['b'], p['c'])} — plus "
                             f"{p['a']} more equals "
                             f"{_fw(p['c'] // p['b'] + p['a'], p['c'])}."),
        "key": lambda p: p["c"],
        "check": lambda p: (p["c"] % p["b"] == 0 and p["c"] > p["b"]
                            and p["b"] in _FRACWORD and p["c"] in _FRACWORD
                            and p["c"] // p["b"] + p["a"] < p["c"],
                            "the bottoms must be family (b divides c) and the sum "
                            "stays a proper fraction"),
        "speaks": lambda p, sp: (str(p["a"]) in sp
                                 and _FRACWORD[p["b"]][0] in sp
                                 and _FRACWORD[p["c"]][1] in sp),
    },
    "lcm": {
        "ans": lambda p: p["a"] * p["b"] // _gcd(p["a"], p["b"]),
        "spoken": lambda p: (f"What is the least common multiple of {p['a']} "
                             f"and {p['b']}?"),
        "board": _lcm_board,          # (st) two count-by number lines, no hops yet
        "worked": _lcm_worked,        # (st) the hops drawn, the first shared landing marked
        "praise": lambda p: (f"The least common multiple of {p['a']} and "
                             f"{p['b']} equals "
                             f"{p['a'] * p['b'] // _gcd(p['a'], p['b'])}."),
        "key": lambda p: p["a"] * p["b"] // _gcd(p["a"], p["b"]),
        "check": lambda p: (2 <= p["a"] and 2 <= p["b"]
                            and p["a"] * p["b"] // _gcd(p["a"], p["b"]) <= 60,
                            "the LCM stays countable"),
    },
    "ang": {   # quarter turns
        "ans": lambda p: 90 * p["a"],
        "spoken": lambda p: (f"A quarter turn is 90 degrees. How many degrees "
                             f"is {p['a']} quarter "
                             f"turn{'' if p['a'] == 1 else 's'}?"),
        "board": _ang_board,          # (sy) the circle cut into four, the turned quarters shaded
        "worked": _ang_worked,
        "praise": lambda p: (f"{p['a']} quarter "
                             f"turn{'' if p['a'] == 1 else 's'} equals "
                             f"{90 * p['a']} degrees."),
        "key": lambda p: p["a"],
        "check": lambda p: (1 <= p["a"] <= 4, "a full turn is the ceiling"),
        # +-1 would be absurd next to 180; the confusion is WHICH multiple of 90
        "choices": lambda p: ([90 * p["a"] - 90, 90 * p["a"], 90 * p["a"] + 90]
                              if p["a"] >= 2 else [90, 180, 270]),
        "speaks": lambda p, sp: str(p["a"]) in sp,
    },
    "angq": {  # the reverse of ang: how many quarter turns is a degrees?
        "ans": lambda p: p["a"] // 90,
        "spoken": lambda p: f"How many quarter turns is {p['a']} degrees?",
        "board": _angq_board,         # (sy) the empty quarters -- how many make the degrees?
        "worked": _angq_worked,
        "praise": lambda p: (f"{p['a']} degrees equals {p['a'] // 90} quarter "
                             f"turn{'' if p['a'] // 90 == 1 else 's'}."),
        "key": lambda p: p["a"] // 90,
        "check": lambda p: (p["a"] in (90, 180, 270, 360),
                            "only whole quarter turns have an answer here"),
        "speaks": lambda p, sp: str(p["a"]) in sp,
    },
    "vol": {   # a x b x c cubes
        "ans": lambda p: p["a"] * p["b"] * p["c"],
        "spoken": lambda p: (f"A box is {_plural(p['a'], 'cube')} long, "
                             f"{_plural(p['b'], 'cube')} wide and "
                             f"{_plural(p['c'], 'cube')} tall. How many cubes "
                             f"fill it?"),
        "board": _vol_board,          # (sy) the box with its three sides
        "worked": _vol_worked,        # (sy) one layer as an array, times the layers
        "praise": lambda p: (f"{p['a']} times {p['b']} times {p['c']} equals "
                             f"{_plural(p['a'] * p['b'] * p['c'], 'cube')}."),
        "key": lambda p: p["a"] * p["b"] * p["c"],
        "check": lambda p: (p["a"] * p["b"] * p["c"] <= 96
                            and min(p["a"], p["b"], p["c"]) >= 1,
                            "countable cubes"),
    },
    "peri": {
        "ans": lambda p: 2 * (p["a"] + p["b"]),
        "spoken": lambda p: (f"A rectangle is {p['a']} long and {p['b']} wide. "
                             f"What is its perimeter?"),
        "board": _peri_board,         # (sy) the rectangle, the walk traced, the sum withheld
        "worked": _peri_worked,
        "praise": lambda p: (f"{p['a']} plus {p['b']} plus {p['a']} plus "
                             f"{p['b']} equals {2 * (p['a'] + p['b'])}."),
        "key": lambda p: p["a"] + p["b"],
        "check": lambda p: (p["a"] > p["b"] >= 1,
                            "long means longer: a must beat b"),
    },
    "area": {
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: (f"A rectangle is {p['a']} long and {p['b']} wide. "
                             f"What is its area?"),
        "board": _area_board,         # (sy) the rectangle on its grid, the count withheld
        "worked": _area_worked,
        "praise": lambda p: (f"{p['a']} times {p['b']} equals "
                             f"{p['a'] * p['b']} squares."),
        "key": lambda p: p["a"] * p["b"],
        "check": lambda p: (p["a"] > p["b"] >= 1, "long means longer"),
    },

    # ---- PREALGEBRA UNIT 1 (build kk) -- ORDER OF OPERATIONS ------------------
    # Each of these declares its own `choices`, and the wrong option on offer is
    # THE MISCONCEPTION ITSELF -- the answer a child gets by working left to right,
    # or by ignoring the parentheses, or by reading an exponent as a times. A
    # distractor that is merely "the answer plus one" tests arithmetic; a distractor
    # that is the actual error tests whether the RULE landed, and when the child taps
    # it the intervention knows exactly which wrong idea to unpick.
    "tba": {   # a + b x c -- times before add
        "ans": lambda p: p["a"] + p["b"] * p["c"],
        "spoken": lambda p: f"What is {p['a']} plus {p['b']} times {p['c']}?",
        "board": lambda p: f'[[step eq="{p["a"]} + {p["b"]} × {p["c"]} = ?"]]',
        "worked": _tba_worked,        # (tc) the order marches down the board
        "praise": lambda p: (f"{p['b']} times {p['c']} equals {p['b'] * p['c']}, "
                             f"and {p['a']} plus {p['b'] * p['c']} equals "
                             f"{p['a'] + p['b'] * p['c']}."),
        "key": lambda p: p["b"] * p["c"],
        "choices": lambda p: [p["a"] + p["b"] * p["c"] - p["c"],
                              p["a"] + p["b"] * p["c"],
                              (p["a"] + p["b"]) * p["c"]],
        "check": lambda p: (1 <= p["a"] <= 9 and 2 <= p["b"] <= 9 and 2 <= p["c"] <= 9,
                            "a is 1-9 and both times numbers are 2-9, so the "
                            "left-to-right answer is always a DIFFERENT number"),
    },
    "parf": {  # (a + b) x c -- parentheses first
        "ans": lambda p: (p["a"] + p["b"]) * p["c"],
        "spoken": lambda p: (f"What is {p['a']} plus {p['b']}, in parentheses, "
                             f"times {p['c']}?"),
        "board": lambda p: f'[[step eq="({p["a"]} + {p["b"]}) × {p["c"]} = ?"]]',
        "worked": _parf_worked,       # (tc) inside first, then the times, marching down
        "praise": lambda p: (f"Inside first: {p['a']} plus {p['b']} equals "
                             f"{p['a'] + p['b']}. Then {p['a'] + p['b']} times "
                             f"{p['c']} equals {(p['a'] + p['b']) * p['c']}."),
        "key": lambda p: (p["a"] + p["b"]) * p["c"],
        "choices": lambda p: [(p["a"] + p["b"]) * p["c"],
                              p["a"] + p["b"] * p["c"],
                              (p["a"] + p["b"]) * p["c"] + p["c"]],
        "check": lambda p: (1 <= p["a"] <= 9 and 1 <= p["b"] <= 9 and 2 <= p["c"] <= 9,
                            "c is 2-9 so ignoring the parentheses always gives a "
                            "different number"),
    },
    "expn": {  # a to the power b, b in (2, 3) -- an exponent is repeated times
        "ans": lambda p: p["a"] ** p["b"],
        # The spoken line must contain BOTH numbers -- the validator checks it, and it
        # is right to: "3 squared" hides the 2, and a child who only ever hears the word
        # never connects it to the small digit on the board.
        "spoken": lambda p: (f"What is {p['a']} to the power 3? That means three "
                             f"{p['a']}s multiplied."
                             if p["b"] == 3 else
                             f"What is {p['a']} squared — {p['a']} to the power 2?"),
        # THE PICTURE THE METHODOLOGY ASKS FOR (build kj gave us the renderer): a
        # square number IS a square. Cubes have no honest 2-D picture, so they get
        # the written repeat instead of a drawing that would lie about the shape.
        "board": lambda p: (f'[[areamodel rows="{p["a"]}" cols="{p["a"]}" '
                            f'caption="{p["a"]} rows of {p["a"]}"]]'
                            f'[[step eq="{p["a"]}² = ?"]]'
                            if p["b"] == 2 else
                            f'[[step eq="{p["a"]}³ = {p["a"]} × {p["a"]} × '
                            f'{p["a"]} = ?"]]'),
        "worked": _expn_worked,       # (tc) a square is a square; a cube is a cube
        "praise": lambda p: (f"{p['a']} to the power {p['b']} equals "
                             f"{p['a'] ** p['b']} — that is {p['b']} {p['a']}s "
                             f"multiplied."),
        "key": lambda p: p["a"] ** p["b"],
        "choices": lambda p: [p["a"] ** p["b"], p["a"] * p["b"],
                              p["a"] ** p["b"] + p["a"]],
        "check": lambda p: (2 <= p["a"] <= 9 and p["b"] in (2, 3)
                            and p["a"] ** p["b"] != p["a"] * p["b"],
                            "a is 2-9 and the power is 2 or 3, and the power answer "
                            "never equals the times answer (which rules out 2²)"),
    },
    "exo": {   # a squared + b x c -- power first, then times, then add
        "ans": lambda p: p["a"] * p["a"] + p["b"] * p["c"],
        "spoken": lambda p: (f"What is {p['a']} squared plus {p['b']} times "
                             f"{p['c']}?"),
        "board": lambda p: f'[[step eq="{p["a"]}² + {p["b"]} × {p["c"]} = ?"]]',
        "worked": _exo_worked,        # (tc) power, times, add -- three rungs down
        "praise": lambda p: (f"{p['a']} squared equals {p['a'] * p['a']}, "
                             f"{p['b']} times {p['c']} equals {p['b'] * p['c']}, "
                             f"and those put together equal "
                             f"{p['a'] * p['a'] + p['b'] * p['c']}."),
        "key": lambda p: p["a"] * p["a"] + p["b"] * p["c"],
        # The two wrong options are the two real errors: adding before the times, and
        # reading the little 2 as "times 2". a >= 3 is what keeps all three distinct --
        # at a = 2 the power and the doubling give the same number, and the child would
        # be offered the same answer twice. (The validator caught exactly that.)
        "choices": lambda p: [p["a"] * p["a"] + p["b"] * p["c"],
                              (p["a"] * p["a"] + p["b"]) * p["c"],
                              2 * p["a"] + p["b"] * p["c"]],
        "check": lambda p: (3 <= p["a"] <= 9 and 2 <= p["b"] <= 9 and 2 <= p["c"] <= 9,
                            "a is 3-9 (at 2, squaring and doubling agree and two "
                            "options would collide); b and c are 2-9"),
    },

    # ---- PREALGEBRA UNIT 2 (build km) -- FACTORS, MULTIPLES & PRIMES ----------
    # Basic Math already teaches GCF and LCM by listing. These go underneath that:
    # what a factor IS, which numbers have only two, and how to break a number all
    # the way down. `a` is the number; `b` carries the authored answer for reference
    # only -- ans() recomputes it, because ans() is the ONLY place answers are made.
    "nfac": {  # how many different numbers divide a exactly
        "ans": lambda p: sum(1 for d in range(1, p["a"] + 1) if p["a"] % d == 0),
        "spoken": lambda p: (f"How many different numbers divide {p['a']} exactly, "
                             f"with nothing left over?"),
        "board": lambda p: f'[[step eq="factors of {p["a"]} = ?"]]',
        "worked": _nfac_worked,       # (tc) the factor pairs written, one drawn
        "praise": lambda p: (f"{p['a']} has "
                             f"{sum(1 for d in range(1, p['a'] + 1) if p['a'] % d == 0)}"
                             f" factors."),
        "key": lambda p: p["a"],
        "speaks": lambda p, sp: str(p["a"]) in sp,   # `b` is a reference, never spoken
        "check": lambda p: (4 <= p["a"] <= 60,
                            "the number stays small enough to check every divisor by "
                            "hand"),
    },
    "spf": {   # the smallest number above 1 that divides a
        "ans": lambda p: next(d for d in range(2, p["a"] + 1) if p["a"] % d == 0),
        "spoken": lambda p: (f"What is the smallest number, bigger than 1, that "
                             f"divides {p['a']} exactly?"),
        "board": lambda p: f'[[step eq="{p["a"]} ÷ ? leaves nothing over"]]',
        "worked": _spf_worked,        # (tc) the tries in order, the first fit ticked and drawn
        "praise": lambda p: (f"{next(d for d in range(2, p['a'] + 1) if p['a'] % d == 0)}"
                             f" is the smallest one that divides {p['a']}."),
        "key": lambda p: p["a"],
        "speaks": lambda p, sp: str(p["a"]) in sp,   # `b` is a reference, never spoken
        "check": lambda p: (9 <= p["a"] <= 99 and
                            next(d for d in range(2, p["a"] + 1) if p["a"] % d == 0)
                            != p["a"],
                            "the number is 9-99 and is NOT itself prime, so there is a "
                            "smaller factor to find"),
    },
    "npf": {   # how many primes multiplied make a (repeats counted)
        "ans": lambda p: len(_prime_factors(p["a"])),
        "spoken": lambda p: (f"Break {p['a']} down into primes multiplied. How many "
                             f"primes does it take?"),
        "board": lambda p: f'[[step eq="{p["a"]} = ? primes multiplied"]]',
        "worked": _npf_worked,        # (tc) the ladder down to primes
        "praise": lambda p: (f"{p['a']} equals "
                             f"{' × '.join(str(x) for x in _prime_factors(p['a']))} — "
                             f"{len(_prime_factors(p['a']))} primes."),
        "key": lambda p: p["a"],
        "speaks": lambda p, sp: str(p["a"]) in sp,   # `b` is a reference, never spoken
        "check": lambda p: (4 <= p["a"] <= 99 and len(_prime_factors(p["a"])) >= 2,
                            "the number is 4-99 and is not prime itself, so there is "
                            "something to break down"),
    },

    # ---- PREALGEBRA UNIT 3 (build km) -- INTEGERS & NEGATIVE NUMBERS ---------
    # THE FIRST LESSONS IN THE APP WHOSE ANSWERS GO BELOW ZERO. The validator used to
    # assume every answer was 1 or more -- true of every counting lesson through Basic
    # Math, and false the moment integers arrive -- so a lesson now declares its own
    # min_value and the guard stays on. The PROBLEM DATA stays positive: `a` and `b`
    # are the numbers a child reads, and the sign lives in the question and the answer.
    # Each wrong option is the sign error itself.
    "cbz": {   # start at a, count back b, land below zero
        "ans": lambda p: p["a"] - p["b"],
        "spoken": lambda p: (f"Start at {p['a']} and count back {p['b']}. What number "
                             f"do you land on?"),
        # THE PICTURE THIS UNIT EXISTS FOR (build kj gave us the renderer): below zero
        # is a PLACE, and a child who sees it on the line stops thinking of a negative
        # as a broken sum.
        # (tc) the ask marks the START; the old board marked the landing point,
        # which is the answer drawn on the question. The walk-back hops.
        "board": _cbz_board,
        "worked": _cbz_worked,
        "praise": lambda p: (f"You land on negative {p['b'] - p['a']} — "
                             f"{p['b'] - p['a']} steps to the left of zero."),
        "key": lambda p: p["b"] - p["a"],
        "choices": lambda p: [p["a"] - p["b"], p["b"] - p["a"], p["a"] - p["b"] - 1],
        "check": lambda p: (1 <= p["a"] <= 9 and p["a"] < p["b"] <= 21,
                            "counting back always passes zero, which is the lesson"),
    },
    "addneg": {  # a + (-b)
        "ans": lambda p: p["a"] - p["b"],
        "spoken": lambda p: (f"What is {p['a']} plus negative {p['b']}?"),
        "board": _addneg_board,       # (tc) the start marked, the hop withheld
        "worked": _addneg_worked,     # (tc) the hop left, past zero
        "praise": lambda p: (f"Adding negative {p['b']} moves {p['b']} to the left, "
                             f"so you land on negative {p['b'] - p['a']}."),
        "key": lambda p: p["b"] - p["a"],
        "choices": lambda p: [p["a"] - p["b"], p["a"] + p["b"], p["a"] - p["b"] - 1],
        "check": lambda p: (1 <= p["a"] <= 9 and p["a"] < p["b"] <= 21,
                            "the answer lands below zero, which is the lesson"),
    },
    "subneg": {  # a - (-b) -- the surprise: it goes UP
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"What is {p['a']} take away negative {p['b']}?"),
        "board": _subneg_board,       # (tc) the start marked on the line
        "worked": _subneg_worked,     # (tc) the hop RIGHT
        "praise": lambda p: (f"Taking away negative {p['b']} moves {p['b']} to the "
                             f"RIGHT, so {p['a']} take away negative {p['b']} equals "
                             f"{p['a'] + p['b']}."),
        "key": lambda p: p["a"] + p["b"],
        "choices": lambda p: [p["a"] + p["b"], p["a"] - p["b"], p["a"] + p["b"] + 1],
        "check": lambda p: (1 <= p["a"] <= 9 and 1 <= p["b"] <= 15 and p["a"] != p["b"],
                            "a and b differ, so the right answer and the take-away "
                            "error are never the same number"),
    },
    "mulneg": {  # (-a) x b
        "ans": lambda p: -(p["a"] * p["b"]),
        "spoken": lambda p: f"What is negative {p['a']} times {p['b']}?",
        "board": lambda p: f'[[step eq="(−{p["a"]}) × {p["b"]} = ?"]]',
        "worked": _mulneg_worked,     # (tc) b hops of a to the left, from zero
        "praise": lambda p: (f"{p['a']} times {p['b']} equals {p['a'] * p['b']}, and "
                             f"one negative turns the answer negative — negative "
                             f"{p['a'] * p['b']}."),
        "key": lambda p: p["a"] * p["b"],
        "choices": lambda p: [-(p["a"] * p["b"]), p["a"] * p["b"],
                              -(p["a"] * p["b"]) - p["a"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9,
                            "both numbers are 2-9, so the answer and the "
                            "forgot-the-sign error are always different"),
    },

    # ---- PREALGEBRA UNIT 4 (build kn) -- FRACTIONS BEYOND BASIC ---------------
    # Basic Math takes fractions as far as adding and taking them away, and its
    # "fraction of a group" only ever asks for a UNIT fraction -- "one half of 4".
    # These four go past that: a non-unit fraction of a number, how many parts fit
    # inside a whole, dividing BY a fraction, and reading an improper fraction.
    # Every answer is a whole number, because a tap answer has to be one.
    "nuf": {   # a/b of c -- a NON-unit fraction of a whole number
        "ans": lambda p: p["c"] // p["b"] * p["a"],
        "spoken": lambda p: (f"What is {_frac_words(p['a'], p['b'])} of {p['c']}?"),
        "board": _nuf_board,       # (td) the picture, the answer withheld
        "worked": _nuf_worked,     # (td) the picture filled in
        "praise": lambda p: (f"One {_FRAC_BOTTOM.get(p['b'], 'part')} of {p['c']} is "
                             f"{p['c'] // p['b']}, and {p['a']} of those equal "
                             f"{p['c'] // p['b'] * p['a']}."),
        "key": lambda p: p["c"] // p["b"] * p["a"],
        # The wrong option is the child who stops after the divide -- they found ONE
        # part and forgot to take a of them, which is the whole difference between
        # this lesson and Basic's unit-fraction one.
        "choices": lambda p: [p["c"] // p["b"] * p["a"], p["c"] // p["b"],
                              p["c"] // p["b"] * p["a"] + p["c"] // p["b"]],
        "speaks": lambda p, sp: str(p["c"]) in sp,   # a and b are said as WORDS
        "check": lambda p: (2 <= p["a"] < p["b"] <= 10 and p["c"] % p["b"] == 0
                            and p["c"] <= 30 and p["a"] != 1,
                            "a proper NON-unit fraction, and c divides exactly so the "
                            "answer is a whole number a child can tap"),
    },
    "uic": {   # how many 1/a fit inside b wholes
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: (f"How many {_FRAC_BOTTOM.get(p['a'], 'parts')}s are "
                             f"there in {p['b']} wholes?"),
        "board": _uic_board,       # (td) the picture, the answer withheld
        "worked": _uic_worked,     # (td) the picture filled in
        "praise": lambda p: (f"Each whole holds {p['a']}, so {p['b']} wholes hold "
                             f"{p['a'] * p['b']}."),
        "key": lambda p: p["a"] * p["b"],
        "choices": lambda p: [p["a"] * p["b"], p["a"] + p["b"], p["a"] * p["b"] - p["a"]],
        "speaks": lambda p, sp: str(p["b"]) in sp,   # the bottom is said as a WORD
        "check": lambda p: (2 <= p["a"] <= 10 and 2 <= p["b"] <= 8
                            and p["a"] * p["b"] != p["a"] + p["b"],
                            "the parts are 2-10 and the wholes 2-8, and a×b never "
                            "equals a+b -- at 2 and 2 they both give 4 and the child "
                            "would be offered the answer twice"),
    },
    "dbf": {   # c divided by a/b -- flip and times
        "ans": lambda p: p["c"] * p["b"] // p["a"],
        "spoken": lambda p: (f"What is {p['c']} divided by "
                             f"{_frac_words(p['a'], p['b'])}?"),
        "board": _dbf_board,       # (td) the picture, the answer withheld
        "worked": _dbf_worked,     # (td) the picture filled in
        "praise": lambda p: (f"Flip the fraction and times: {p['c']} times "
                             f"{p['b']} over {p['a']} equals "
                             f"{p['c'] * p['b'] // p['a']}."),
        "key": lambda p: p["c"] * p["b"] // p["a"],
        # The error worth offering is dividing instead of flipping -- the child who
        # trusts that dividing always makes things smaller.
        "choices": lambda p: [p["c"] * p["b"] // p["a"], p["c"] * p["a"] // p["b"] or 1,
                              p["c"] * p["b"] // p["a"] + p["b"]],
        "speaks": lambda p, sp: str(p["c"]) in sp,
        "check": lambda p: (2 <= p["a"] < p["b"] <= 9 and 2 <= p["c"] <= 12
                            and (p["c"] * p["b"]) % p["a"] == 0
                            and p["c"] * p["b"] // p["a"] != p["c"] * p["a"] // p["b"],
                            "the answer is a whole number, and flipping the wrong way "
                            "always gives a different one"),
    },
    "imp": {   # a/b -- how many WHOLE ones are inside it
        "ans": lambda p: p["a"] // p["b"],
        "spoken": lambda p: (f"How many whole ones are inside {p['a']} "
                             f"{_FRAC_BOTTOM.get(p['b'], 'part')}s?"),
        # A fraction bigger than 1 is a PLACE past the whole numbers, and the line
        # says that better than any sentence (build kj gave us the renderer).
        "board": _imp_board,       # (td) the picture, the answer withheld
        "worked": _imp_worked,     # (td) the picture filled in
        "praise": lambda p: (f"{p['b']} of them fill one whole, so {p['a']} of them "
                             f"fill {p['a'] // p['b']} whole ones with "
                             f"{p['a'] % p['b']} left over."),
        "key": lambda p: p["a"] // p["b"],
        "choices": lambda p: [p["a"] // p["b"], p["a"] % p["b"], p["a"] // p["b"] + 1],
        "speaks": lambda p, sp: str(p["a"]) in sp,   # the bottom is said as a WORD
        "check": lambda p: (7 <= p["a"] <= 40 and 3 <= p["b"] <= 9
                            and p["a"] % p["b"] != 0
                            and p["a"] // p["b"] != p["a"] % p["b"],
                            "the fraction is bigger than 1 and does not land exactly "
                            "on a whole, and the whole count and the left-over are "
                            "never the same number"),
    },

    # ---- PREALGEBRA UNIT 5 (build ko) -- DECIMALS BEYOND BASIC ----------------
    # Basic Math names tenths and hundredths and counts dimes and pennies. These four
    # go past naming: converting to a common unit (which is what comparing decimals
    # REALLY is), scaling by ten, and timesing and sharing them.
    # Every answer is a COUNT OF PARTS -- "how many hundredths", "how many tenths" --
    # which is both the honest way to think about a decimal and the only way a tap
    # answer can carry one.
    "hun": {   # 0.ab -- how many hundredths is that?
        "ans": lambda p: 10 * p["a"] + p["b"],
        "spoken": lambda p: (f"How many hundredths are there in "
                             f"0 point {p['a']}{p['b']}?"),
        "board": _hun_board,       # (td) the picture, the answer withheld
        "worked": _hun_worked,     # (td) the picture filled in
        "praise": lambda p: (f"0 point {p['a']}{p['b']} is "
                             f"{10 * p['a'] + p['b']} hundredths."),
        "key": lambda p: 10 * p["a"] + p["b"],
        # The wrong option is the child reading the digits as a whole number and
        # ignoring the place -- the same habit that makes 0.45 look bigger than 0.5.
        "choices": lambda p: [10 * p["a"] + p["b"], p["a"] + p["b"],
                              10 * p["a"] + p["b"] + 10],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (1 <= p["a"] <= 9 and 0 <= p["b"] <= 9
                            and 10 * p["a"] + p["b"] != p["a"] + p["b"],
                            "a is 1-9 so the place-value answer and the "
                            "digits-added error are never the same number"),
    },
    "x10": {   # a.b times 10
        "ans": lambda p: 10 * p["a"] + p["b"],
        "spoken": lambda p: f"What is {p['a']} point {p['b']} times 10?",
        "board": _x10_board,       # (td) the picture, the answer withheld
        "worked": _x10_worked,     # (td) the picture filled in
        "praise": lambda p: (f"Timesing by 10 moves every digit one place to the "
                             f"left, so {p['a']} point {p['b']} becomes "
                             f"{10 * p['a'] + p['b']}."),
        "key": lambda p: 10 * p["a"] + p["b"],
        # The error worth offering is timesing only the whole part and leaving the
        # tenths where they were.
        "choices": lambda p: [10 * p["a"] + p["b"], 10 * p["a"],
                              10 * p["a"] + p["b"] + 1],
        "check": lambda p: (1 <= p["a"] <= 9 and 0 <= p["b"] <= 9 and p["b"] != 0,
                            "there is a tenths digit to move, so leaving it behind "
                            "gives a different number"),
    },
    "dth": {   # 0.a times b -- answered in TENTHS
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: (f"0 point {p['a']} times {p['b']} — how many tenths "
                             f"is that?"),
        "board": _dth_board,       # (td) the picture, the answer withheld
        "worked": _dth_worked,     # (td) the picture filled in
        "praise": lambda p: (f"{p['a']} tenths taken {p['b']} times equal "
                             f"{p['a'] * p['b']} tenths."),
        "key": lambda p: p["a"] * p["b"],
        "choices": lambda p: [p["a"] * p["b"], p["a"] + p["b"], p["a"] * p["b"] + p["a"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and p["a"] * p["b"] != p["a"] + p["b"],
                            "both are 2-9 and the times never equals the add, so the "
                            "three options are three different numbers"),
    },
    "dsh": {   # a.b shared between c -- answered in TENTHS
        "ans": lambda p: (10 * p["a"] + p["b"]) // p["c"],
        "spoken": lambda p: (f"{p['a']} point {p['b']} shared between {p['c']} — "
                             f"how many tenths each?"),
        "board": _dsh_board,       # (td) the picture, the answer withheld
        "worked": _dsh_worked,     # (td) the picture filled in
        "praise": lambda p: (f"{p['a']} point {p['b']} is "
                             f"{10 * p['a'] + p['b']} tenths, and shared between "
                             f"{p['c']} that is "
                             f"{(10 * p['a'] + p['b']) // p['c']} tenths each."),
        "key": lambda p: (10 * p["a"] + p["b"]) // p["c"],
        "choices": lambda p: [(10 * p["a"] + p["b"]) // p["c"],
                              (10 * p["a"] + p["b"]) // p["c"] + p["c"],
                              (10 * p["a"] + p["b"]) // p["c"] + 1],
        "check": lambda p: (1 <= p["a"] <= 9 and 0 <= p["b"] <= 9 and 2 <= p["c"] <= 9
                            and (10 * p["a"] + p["b"]) % p["c"] == 0,
                            "it shares out exactly, so the answer is a whole number "
                            "of tenths a child can tap"),
    },

    # ---- PREALGEBRA UNIT 6 (build kp) -- RATIOS, RATES & PROPORTIONS ----------
    # Basic Math's "one costs" already does unit PRICE. These four are the family of
    # ideas around it: keeping a ratio's shape when both sides grow, scaling a rate
    # over time, the same move written as an equation with a hole in it, and splitting
    # an amount in a ratio -- the one that is genuinely different, because the total is
    # given and the parts have to be found.
    "rat": {   # ratio a:b -- given c of the first, how many of the second
        "ans": lambda p: p["c"] // p["a"] * p["b"],
        "spoken": lambda p: (f"A recipe uses {p['a']} cups of flour for every "
                             f"{p['b']} cups of milk. With {p['c']} cups of flour, "
                             f"how many cups of milk?"),
        "board": _rat_board,       # (td) the picture, the answer withheld
        "worked": _rat_worked,     # (td) the picture filled in
        "praise": lambda p: (f"{p['c']} cups of flour is {p['c'] // p['a']} batches, "
                             f"so it takes {p['c'] // p['a'] * p['b']} cups of milk."),
        "key": lambda p: p["c"] // p["a"] * p["b"],
        # The error worth offering is ADDING the difference instead of scaling -- the
        # child who thinks 2:3 growing to 4 means "4:5", because 3 is one more than 2.
        "choices": lambda p: [p["c"] // p["a"] * p["b"], p["c"] + (p["b"] - p["a"]),
                              p["c"] // p["a"] * p["b"] + p["b"]],
        "speaks": lambda p, sp: str(p["a"]) in sp and str(p["c"]) in sp,
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9 and p["a"] != p["b"]
                            and p["c"] % p["a"] == 0 and p["c"] // p["a"] >= 2
                            and len({p["c"] // p["a"] * p["b"],
                                     p["c"] + (p["b"] - p["a"]),
                                     p["c"] // p["a"] * p["b"] + p["b"]}) == 3,
                            "the ratio really scales (at least two batches) and the "
                            "three tap options are three different numbers"),
    },
    "rte": {   # c things in b hours -- how many in a hours
        "ans": lambda p: p["c"] // p["b"] * p["a"],
        # "makes" is banned speech (canon is "equals"), so the machine FILLS.
        "spoken": lambda p: (f"A machine fills {p['c']} bottles in {p['b']} hours. "
                             f"How many does it fill in {p['a']} hours?"),
        "board": _rte_board,       # (td) the picture, the answer withheld
        "worked": _rte_worked,     # (td) the picture filled in
        "praise": lambda p: (f"That is {p['c'] // p['b']} an hour, so in {p['a']} "
                             f"hours it fills {p['c'] // p['b'] * p['a']}."),
        "key": lambda p: p["c"] // p["b"] * p["a"],
        "choices": lambda p: [p["c"] // p["b"] * p["a"], p["c"] // p["b"],
                              p["c"] // p["b"] * p["a"] + p["c"] // p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and p["c"] % p["b"] == 0 and p["a"] != 1
                            and p["c"] // p["b"] * p["a"] != p["c"] // p["b"],
                            "it divides exactly and the target time is not one hour, "
                            "so finding the rate is only HALF the job"),
    },
    "prop": {  # a/b = ?/c
        "ans": lambda p: p["a"] * p["c"] // p["b"],
        "spoken": lambda p: (f"{p['a']} over {p['b']} equals what over {p['c']}?"),
        "board": _prop_board,       # (td) the picture, the answer withheld
        "worked": _prop_worked,     # (td) the picture filled in
        "praise": lambda p: (f"{p['a']} over {p['b']} equals "
                             f"{p['a'] * p['c'] // p['b']} over {p['c']}."),
        "key": lambda p: p["a"] * p["c"] // p["b"],
        # The classic error: adding the same amount to both instead of timesing.
        "choices": lambda p: [p["a"] * p["c"] // p["b"], p["a"] + (p["c"] - p["b"]),
                              p["a"] * p["c"] // p["b"] + p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9 and p["c"] <= 30
                            and (p["a"] * p["c"]) % p["b"] == 0 and p["c"] != p["b"]
                            and len({p["a"] * p["c"] // p["b"],
                                     p["a"] + (p["c"] - p["b"]),
                                     p["a"] * p["c"] // p["b"] + p["b"]}) == 3,
                            "the missing number is whole, the bottom really changes, "
                            "and all THREE options are different numbers (the first "
                            "try had the add-the-same error landing on the same value "
                            "as the neighbour)"),
    },
    "shr": {   # share c in the ratio a:b -- the FIRST share
        "ans": lambda p: p["c"] // (p["a"] + p["b"]) * p["a"],
        "spoken": lambda p: (f"Share {p['c']} sweets between two children in the "
                             f"ratio {p['a']} to {p['b']}. How many does the first "
                             f"child get?"),
        "board": _shr_board,       # (td) the picture, the answer withheld
        "worked": _shr_worked,     # (td) the picture filled in
        "praise": lambda p: (f"{p['a'] + p['b']} parts in all, so each part is "
                             f"{p['c'] // (p['a'] + p['b'])}, and the first child gets "
                             f"{p['a']} of them — "
                             f"{p['c'] // (p['a'] + p['b']) * p['a']}."),
        "key": lambda p: p["c"] // (p["a"] + p["b"]) * p["a"],
        # The error worth offering is sharing the amount by the FIRST number only,
        # forgetting that the parts have to be counted together first.
        "choices": lambda p: [p["c"] // (p["a"] + p["b"]) * p["a"],
                              p["c"] // (p["a"] + p["b"]) * p["b"],
                              p["c"] // (p["a"] + p["b"])],
        "speaks": lambda p, sp: str(p["c"]) in sp and str(p["a"]) in sp,
        # A one-part share IS the size of one part, so a = 1 (or b = 1) makes two
        # of the three options the same number. Requiring three different options
        # says that out loud instead of hiding it in a bound on a.
        "check": lambda p: (1 <= p["a"] <= 9 and 1 <= p["b"] <= 9 and p["a"] != p["b"]
                            and p["c"] % (p["a"] + p["b"]) == 0
                            and p["c"] // (p["a"] + p["b"]) != 1
                            and len({p["c"] // (p["a"] + p["b"]) * p["a"],
                                     p["c"] // (p["a"] + p["b"]) * p["b"],
                                     p["c"] // (p["a"] + p["b"])}) == 3,
                            "each part is more than one and the three tap options "
                            "are three different numbers"),
    },

    # ---- PREALGEBRA UNIT 7 (build kr) -- PERCENTS -----------------------------
    # Basic Math's "pc" only ever asks for 10, 25 or 50 percent, and it answers them
    # with a fraction shortcut (half, a fourth, a tenth). That shortcut runs out the
    # moment the percent is 30 or 70. These four replace it with ONE method that keeps
    # working -- find ten percent, then count how many tens you need -- and then run
    # that method in every direction: forwards, as a reading of one number against
    # another, backwards from a part to the whole, and finally up and down.
    "pcn": {   # a percent of b, both multiples of ten
        "ans": lambda p: p["a"] * p["b"] // 100,
        "spoken": lambda p: f"What is {p['a']} percent of {p['b']}?",
        "board": _pcn_board,          # (te) the bar cut into ten -- 10% is one part
        "worked": _pcn_worked,        # (te) the parts filled, the taken parts marked
        "praise": lambda p: (f"10 percent of {p['b']} is {p['b'] // 10}, and "
                             f"{p['a']} percent is {p['a'] // 10} of those — "
                             f"{p['a'] * p['b'] // 100}."),
        "key": lambda p: p["a"] * p["b"] // 100,
        # The error worth offering is STOPPING AT TEN PERCENT -- the same shape as the
        # rate error in Unit 6, where the child divides to reach one and taps that.
        "choices": lambda p: [p["a"] * p["b"] // 100, p["b"] // 10,
                              p["a"] * p["b"] // 100 + p["b"] // 10],
        "check": lambda p: (p["a"] % 10 == 0 and 20 <= p["a"] <= 90 and p["a"] != 50
                            and p["b"] % 10 == 0 and 10 <= p["b"] <= 90
                            and len({p["a"] * p["b"] // 100, p["b"] // 10,
                                     p["a"] * p["b"] // 100 + p["b"] // 10}) == 3,
                            "both are tens so ten percent is whole, the percent is one "
                            "Basic never taught, and the three options differ"),
    },
    "asp": {   # a out of b -- what percent?
        "ans": lambda p: p["a"] * 100 // p["b"],
        "spoken": lambda p: f"{p['a']} out of {p['b']} — what percent is that?",
        "board": _asp_board,          # (te) the share as a bar, the empty hundred grid
        "worked": _asp_worked,        # (te) the same share shaded out of 100
        "praise": lambda p: (f"{p['a']} out of {p['b']} is "
                             f"{p['a'] * 100 // p['b']} percent."),
        "key": lambda p: p["a"] * 100 // p["b"],
        # The classic slip is reading the percent of what is NOT there, so the second
        # option is the leftover percent. The third is tapping the part itself.
        "choices": lambda p: [p["a"] * 100 // p["b"],
                              100 - p["a"] * 100 // p["b"], p["a"]],
        "check": lambda p: (1 <= p["a"] < p["b"] <= 100
                            and (p["a"] * 100) % p["b"] == 0
                            and len({p["a"] * 100 // p["b"],
                                     100 - p["a"] * 100 // p["b"], p["a"]}) == 3,
                            "the percent is whole, the part is smaller than the whole, "
                            "and the three options differ (which rules out 50 percent, "
                            "where the answer and its leftover are one number)"),
    },
    "pwh": {   # b is a percent of WHAT? -- the reverse, and the hard direction
        "ans": lambda p: p["b"] * 100 // p["a"],
        "spoken": lambda p: f"{p['b']} is {p['a']} percent of what number?",
        "board": _pwh_board,          # (te) the part as a bar, the whole the question
        "worked": _pwh_worked,        # (te) the ten parts, the whole bracketed
        "praise": lambda p: (f"10 percent is {p['b'] // (p['a'] // 10)}, so the whole "
                             f"is ten of those — {p['b'] * 100 // p['a']}."),
        "key": lambda p: p["b"] * 100 // p["a"],
        # THE reversal error: doing the forward sum instead -- finding a percent OF the
        # part, when the part is what you were given.
        "choices": lambda p: [p["b"] * 100 // p["a"], p["a"] * p["b"] // 100,
                              p["b"] * 100 // p["a"] - p["b"]],
        "check": lambda p: (p["a"] % 10 == 0 and 10 <= p["a"] <= 90
                            and (p["b"] * 100) % p["a"] == 0
                            and p["b"] % (p["a"] // 10) == 0
                            and 1 <= p["b"] * 100 // p["a"] <= 100
                            # >= 2, not >= 1: at 20 percent of 6 the forward error
                            # rounds down to 1, and "1" is not an answer any child
                            # arrives at -- it is a stub, and a stub is not a choice.
                            and min(p["b"] * 100 // p["a"], p["a"] * p["b"] // 100,
                                    p["b"] * 100 // p["a"] - p["b"]) >= 2
                            and len({p["b"] * 100 // p["a"], p["a"] * p["b"] // 100,
                                     p["b"] * 100 // p["a"] - p["b"]}) == 3,
                            "the ten-percent step is whole, the whole is a real "
                            "number a child can tap, and every wrong option is a real "
                            "wrong answer rather than a rounded-down stub"),
    },
    "pup": {   # c=1 a percent MORE, c=0 a percent LESS
        "ans": lambda p: (p["b"] + p["a"] * p["b"] // 100 if p.get("c")
                          else p["b"] - p["a"] * p["b"] // 100),
        "spoken": lambda p: (f"A coat costs {p['b']} dollars. The price goes "
                             f"{'up' if p.get('c') else 'down'} by {p['a']} percent. "
                             f"What does it cost now?"),
        # The ten-percent step and the "a percent" step are the SAME LINE when the
        # percent is ten, and a board that says "10% of 40 = 4" and then "10% = 4"
        # teaches a child that the second step is empty. Show it only when it says
        # something new.
        "board": _pup_board,          # (te) the price and the change, the new price withheld
        "worked": _pup_worked,        # (te) the bar with the change put on or taken off
        "praise": lambda p: (f"{p['a']} percent of {p['b']} is "
                             f"{p['a'] * p['b'] // 100}, so the new price is "
                             f"{p['b'] + p['a'] * p['b'] // 100 if p.get('c') else p['b'] - p['a'] * p['b'] // 100} dollars."),
        "key": lambda p: (p["b"] + p["a"] * p["b"] // 100 if p.get("c")
                          else p["b"] - p["a"] * p["b"] // 100),
        # THE error this lesson exists for: moving the price by the PERCENT NUMBER
        # instead of by that percent OF the price -- 40 dollars up 10 percent read as
        # 50 dollars. The third option is the change on its own, mistaken for the price.
        "choices": lambda p: [(p["b"] + p["a"] * p["b"] // 100 if p.get("c")
                               else p["b"] - p["a"] * p["b"] // 100),
                              (p["b"] + p["a"] if p.get("c") else p["b"] - p["a"]),
                              p["a"] * p["b"] // 100],
        "speaks": lambda p, sp: str(p["a"]) in sp and str(p["b"]) in sp,
        "check": lambda p: (p["a"] % 10 == 0 and 10 <= p["a"] <= 50
                            and p["b"] % 10 == 0 and 10 <= p["b"] <= 90
                            and (p["a"] * p["b"]) % 100 == 0
                            and len({(p["b"] + p["a"] * p["b"] // 100 if p.get("c")
                                      else p["b"] - p["a"] * p["b"] // 100),
                                     (p["b"] + p["a"] if p.get("c")
                                      else p["b"] - p["a"]),
                                     p["a"] * p["b"] // 100}) == 3,
                            "the change is a whole number of dollars and the three "
                            "options are three different prices"),
    },

    # ---- PREALGEBRA UNIT 8 (build ks) -- MEASUREMENT & GEOMETRY BASICS -------
    # Basic Math's geometry unit (perimeter, area, quarter turns, volume) draws NO
    # PICTURES -- every one of its boards is a [[step]] line. That is the wrong medium
    # for the one subject where the picture IS the argument, and geo-figures.js has had
    # [[triangle]] and [[angle]] the whole time. Three of these four ops put a real
    # figure on the board, and the straight-line lesson uses [[angle deg="180"
    # split="130"]] -- a tag built in July for exactly this and never once used by a
    # scripted lesson.
    "cnv": {   # a of the bigger unit -- how many of the smaller? b is the factor
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: (
            f"How many millimetres are there in {p['a']} centimetres?" if p["b"] == 10
            else f"How many centimetres are there in {p['a']} metres?" if p["b"] == 100
            else f"How many grams are there in {p['a']} kilograms?"),
        "board": _cnv_board,          # (te) one bar part per big unit, the small units in each
        "worked": _cnv_worked,        # (te) the total bracketed
        "praise": lambda p: (f"Each one is {p['b']}, so {p['a']} of them are "
                             f"{p['a'] * p['b']}."),
        "key": lambda p: p["a"] * p["b"],
        # THE unit-conversion error is the wrong power of ten -- one place short, or one
        # place too far. Neither is a careless slip; both are a child who knows a zero
        # goes on and does not know how many.
        "choices": lambda p: [p["a"] * p["b"], p["a"] * p["b"] // 10,
                              p["a"] * p["b"] * 10],
        # The factor is not spoken -- the UNIT NAMES carry it, which is the whole point
        # of the lesson. Rule 44 is satisfied by the number the child has to use.
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (1 <= p["a"] <= 9 and p["b"] in (10, 100, 1000)
                            and p["a"] * p["b"] <= 9000
                            and len({p["a"] * p["b"], p["a"] * p["b"] // 10,
                                     p["a"] * p["b"] * 10}) == 3,
                            "a single-digit count of a real unit, and the three options "
                            "are three different places"),
    },
    "tri": {   # area of a right triangle, base a and height b
        "ans": lambda p: p["a"] * p["b"] // 2,
        "spoken": lambda p: (f"A triangle has a base of {p['a']} and a height of "
                             f"{p['b']}. What is its area?"),
        "board": _tri_board,          # (te) the rectangle round it, the diagonal drawn, half asked
        "worked": _tri_worked,        # (te) the same, the half counted
        "praise": lambda p: (f"The rectangle round it is {p['a'] * p['b']}, and the "
                             f"triangle is half of that — {p['a'] * p['b'] // 2}."),
        "key": lambda p: p["a"] * p["b"] // 2,
        # The error worth offering is FORGETTING TO HALVE -- answering with the
        # rectangle. It is the single most common wrong answer there is here.
        "choices": lambda p: [p["a"] * p["b"] // 2, p["a"] * p["b"], p["a"] + p["b"]],
        "check": lambda p: (2 <= p["a"] <= 20 and 2 <= p["b"] <= 20
                            and (p["a"] * p["b"]) % 2 == 0
                            and len({p["a"] * p["b"] // 2, p["a"] * p["b"],
                                     p["a"] + p["b"]}) == 3,
                            "the half is a whole number of squares and the three "
                            "options are three different numbers"),
    },
    "sla": {   # two angles on a straight line: one is a, how big is the other?
        "ans": lambda p: 180 - p["a"],
        "spoken": lambda p: (f"Two angles sit together on a straight line. One of them "
                             f"is {p['a']} degrees. How big is the other one?"),
        # geo-figures' split= was built in July for exactly this sentence and no
        # scripted lesson had ever used it: the straight line IS the 180, drawn.
        "board": _sla_board,          # (te) the straight line split, the rest asked
        "worked": _sla_worked,        # (te) both pieces labelled, put back to 180
        "praise": lambda p: (f"A straight line is 180 degrees, and 180 take away "
                             f"{p['a']} equals {180 - p['a']}."),
        "key": lambda p: 180 - p["a"],
        # The two real errors: using a RIGHT ANGLE'S 90 or a FULL TURN'S 360 in place of
        # the straight line's 180, and simply tapping the angle you were handed.
        "choices": lambda p: [180 - p["a"], 360 - p["a"], p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (10 <= p["a"] <= 170 and p["a"] != 90
                            and len({180 - p["a"], 360 - p["a"], p["a"]}) == 3,
                            "the angle is not the right angle (where the answer and the "
                            "angle are one number) and the three options differ"),
    },
    "tri3": {  # two angles of a triangle are a and b -- the third?
        "ans": lambda p: 180 - p["a"] - p["b"],
        "spoken": lambda p: (f"Two angles of a triangle are {p['a']} degrees and "
                             f"{p['b']} degrees. How big is the third one?"),
        # When one of the given angles IS 90, say so in the figure. The renderer's
        # header calls these figures schematic, and they are -- but a right angle drawn
        # as a lazy corner with "90°" written beside it is schematic in the one way
        # that teaches the wrong thing.
        "board": _tri3_board,         # (te) the triangle with two angles, the third blank
        "worked": _tri3_worked,       # (te) all three, put back to 180
        "praise": lambda p: (f"The two you were given are {p['a'] + p['b']} together, "
                             f"and 180 take away {p['a'] + p['b']} equals "
                             f"{180 - p['a'] - p['b']}."),
        "key": lambda p: 180 - p["a"] - p["b"],
        # The error worth offering is answering with the two you were GIVEN added up --
        # the child who does the first step and taps it.
        "choices": lambda p: [180 - p["a"] - p["b"], p["a"] + p["b"],
                              180 - p["a"]],
        "check": lambda p: (10 <= p["a"] <= 150 and 10 <= p["b"] <= 150
                            and 180 - p["a"] - p["b"] >= 10
                            and len({180 - p["a"] - p["b"], p["a"] + p["b"],
                                     180 - p["a"]}) == 3,
                            "all three angles are real ones a child can see, and the "
                            "three options are three different numbers"),
    },

    # ---- PREALGEBRA UNIT 9 (build kt) -- VARIABLES & EXPRESSIONS --------------
    # The last prealgebra unit, and the doorway to algebra. Everything before this
    # asked about numbers; these four ask about a LETTER that stands for one. The
    # order is the order the idea actually grows: a letter holds a number (evx), a
    # number written against a letter means times (mlx), like terms collect by
    # counting (clt), and a times distributes over a parenthesis (dst) -- drawn with
    # [[areamodel]], the algebra-tile renderer that has been in the registry since
    # July and, exactly like [[angle split=]] before build ks, has never once been
    # used by a scripted lesson.
    "evx": {   # x holds a -- what is x + b?
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"The letter x is holding the number {p['a']}. "
                             f"What is x plus {p['b']}?"),
        "board": _evx_board,          # (te) x and the number as a bar, the total asked
        "worked": _evx_worked,        # (te) the letter swapped for its number
        "praise": lambda p: (f"x is {p['a']}, so x plus {p['b']} is {p['a']} plus "
                             f"{p['b']}, which equals {p['a'] + p['b']}."),
        "key": lambda p: p["a"] + p["b"],
        # THE first-variable error is CONCATENATION: x holds 5, so "x + 3" is read as
        # writing 5 next to 3 -- the child taps 53. It looks bizarre to an adult and it
        # is the documented, universal first misreading of substitution.
        "choices": lambda p: [p["a"] + p["b"], 10 * p["a"] + p["b"], p["a"] * p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and p["a"] * p["b"] != p["a"] + p["b"],
                            "single digits so the glued-together error is a real tap, "
                            "and the times never equals the add"),
    },
    "mlx": {   # x holds a -- what is bx?
        "ans": lambda p: p["a"] * p["b"],
        # The ask does NOT re-explain the shorthand -- the teach beats own that.
        # A scaffold repeated in every one of twelve asks is a scaffold that never
        # fades, and fading it is what practice is for.
        "spoken": lambda p: (f"The letter x is holding the number {p['a']}. "
                             f"What is {p['b']} x?"),
        "board": _mlx_board,          # (te) b copies of x as a bar
        "worked": _mlx_worked,        # (te) every copy is a, the total bracketed
        "praise": lambda p: (f"{p['b']} x means {p['b']} times x, and {p['b']} times "
                             f"{p['a']} equals {p['a'] * p['b']}."),
        "key": lambda p: p["a"] * p["b"],
        # The error is reading the written-together 3x as 3 PLUS x -- adding where the
        # notation quietly means times.
        "choices": lambda p: [p["a"] * p["b"], p["a"] + p["b"],
                              p["a"] * p["b"] + p["a"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and p["a"] * p["b"] != p["a"] + p["b"],
                            "both single digits and never the 2-and-2 case, so the "
                            "times-versus-add error is a different number"),
    },
    "clt": {   # ax + bx -- how many x in all?
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"{p['a']} x plus {p['b']} x — how many x is that "
                             f"in all?"),
        "board": _clt_board,          # (te) the x's as one bar, counted
        "worked": _clt_worked,        # (te) the same bar with the count
        "praise": lambda p: (f"{p['a']} x's and {p['b']} more x's are "
                             f"{p['a'] + p['b']} x's in all — {p['a'] + p['b']} x."),
        "key": lambda p: p["a"] + p["b"],
        # The error is TIMESING the counts -- the child who has just learned that
        # letters mean times and now applies it to everything in sight.
        "choices": lambda p: [p["a"] + p["b"], p["a"] * p["b"], p["a"] + p["b"] + 1],
        # Three DISTINCT options, said outright: at 2x + 3x the neighbour distractor
        # (6) lands exactly on the times-them distractor (6), so requiring the pair
        # to differ is not enough -- the whole set has to.
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and len({p["a"] + p["b"], p["a"] * p["b"],
                                     p["a"] + p["b"] + 1}) == 3,
                            "the counts add like apples add, and the three tap "
                            "options are three different numbers"),
    },
    "dst": {   # a(x + b) = ax + ? -- the distributive property, drawn as area
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: (f"Times the whole of x plus {p['b']} by {p['a']}. "
                             f"That comes to {p['a']} x plus what number?"),
        # ⭐ [[areamodel]] draws a rectangle a tall and (x + b) wide, cut into an ax
        # piece and an ab piece, with the expanded sum printed under it. The child is
        # not told the rule -- the child is shown the two rooms of the rectangle.
        "board": _dst_board,          # (te) the two rooms, the number room asked
        "worked": _dst_worked,        # (te) the rooms read
        "praise": lambda p: (f"The {p['a']} reaches BOTH rooms: {p['a']} times x, and "
                             f"{p['a']} times {p['b']}, which equals "
                             f"{p['a'] * p['b']}. So it is {p['a']} x plus "
                             f"{p['a'] * p['b']}."),
        "key": lambda p: p["a"] * p["b"],
        # THE distributive error: the times reaches the x and never the number --
        # 4(x + 3) read as 4x + 3. The wrong tap is the untouched 3.
        "choices": lambda p: [p["a"] * p["b"], p["b"], p["a"] + p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and len({p["a"] * p["b"], p["b"],
                                     p["a"] + p["b"]}) == 3,
                            "the multiplier is at least 2 so the untouched-number "
                            "error is a real different tap, and all three options "
                            "differ"),
    },

    # ---- ALGEBRA I UNIT 1 (build ku) -- FOUNDATIONS & EXPRESSIONS -------------
    # The first Algebra I unit, sitting directly on Prealgebra U9. That unit taught
    # the four seeds one at a time: a letter holds a number, a number against a letter
    # means times, like terms count, a times distributes. These four make the seeds
    # WORK TOGETHER: evaluate a two-step expression (where order of operations meets a
    # letter), read TWO letters at once, collect the x's when y's are standing in the
    # way, and distribute over a take away -- the first time the invisible times has
    # to carry a minus sign with it.
    "ev2": {   # x holds a -- what is bx + c?
        "ans": lambda p: p["a"] * p["b"] + p["c"],
        "spoken": lambda p: (f"The letter x is holding the number {p['a']}. "
                             f"What is {p['b']} x plus {p['c']}?"),
        "board": _ev2_board,          # (tf) b copies of x and the c, the whole withheld
        "worked": _ev2_worked,        # (tf) every copy the number, the whole bracketed
        "praise": lambda p: (f"{p['b']} x is {p['b']} times {p['a']}, which equals "
                             f"{p['a'] * p['b']}, and {p['a'] * p['b']} plus "
                             f"{p['c']} equals {p['a'] * p['b'] + p['c']}."),
        "key": lambda p: p["a"] * p["b"] + p["c"],
        # Prealgebra U1's own rule, now with a letter in it: times before add. The
        # error worth offering is ADDING FIRST -- b times (a plus c). The third option
        # is ignoring the invisible times altogether and adding everything in sight.
        "choices": lambda p: [p["a"] * p["b"] + p["c"],
                              p["b"] * (p["a"] + p["c"]),
                              p["a"] + p["b"] + p["c"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9 and 2 <= p["c"] <= 9
                            and len({p["a"] * p["b"] + p["c"],
                                     p["b"] * (p["a"] + p["c"]),
                                     p["a"] + p["b"] + p["c"]}) == 3,
                            "single digits and three distinct options -- which rules "
                            "out x holding 2 with a coefficient of 2, where timesing "
                            "and adding agree"),
    },
    "evxy": {  # x holds a, y holds b -- what is x + cy?
        "ans": lambda p: p["a"] + p["c"] * p["b"],
        # No "two letters now" preamble in the ask -- the same scaffold-never-fades
        # defect mlx had in build kt. The teach beats introduce y; the ask just asks.
        "spoken": lambda p: (f"x is holding {p['a']}, and y is holding {p['b']}. "
                             f"What is x plus {p['c']} y?"),
        "board": _evxy_board,         # (tf) one x and c copies of y
        "worked": _evxy_worked,       # (tf) each letter its own number
        "praise": lambda p: (f"{p['c']} y is {p['c']} times {p['b']}, which equals "
                             f"{p['c'] * p['b']}, and {p['a']} plus that equals "
                             f"{p['a'] + p['c'] * p['b']}."),
        "key": lambda p: p["a"] + p["c"] * p["b"],
        # Each letter keeps its own number. The errors: adding a to c first and then
        # timesing (the same add-first slip as ev2, wearing a y), and treating "c y"
        # as c plus y.
        "choices": lambda p: [p["a"] + p["c"] * p["b"],
                              (p["a"] + p["c"]) * p["b"],
                              p["a"] + p["c"] + p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9 and 2 <= p["c"] <= 9
                            and len({p["a"] + p["c"] * p["b"],
                                     (p["a"] + p["c"]) * p["b"],
                                     p["a"] + p["c"] + p["b"]}) == 3,
                            "single digits and three distinct options"),
    },
    "cl2": {   # ax + by + cx -- how many x?
        "ans": lambda p: p["a"] + p["c"],
        "spoken": lambda p: (f"{p['a']} x plus {p['b']} y plus {p['c']} x — "
                             f"how many x is that in all?"),
        "board": _cl2_board,          # (tf) the bar in the order written, x parts and y parts
        "worked": _cl2_worked,        # (tf) the x's collected, the y beside them
        "praise": lambda p: (f"Only the x's collect: {p['a']} and {p['c']} make "
                             f"{p['a'] + p['c']} x. The {p['b']} y is a different "
                             f"thing and stays as it is."),
        "key": lambda p: p["a"] + p["c"],
        # The error is GRABBING EVERYTHING -- apples and oranges into one pile. A y is
        # not an x, and 3x + 2y + 4x is 7x plus 2y, not 9 of anything.
        "choices": lambda p: [p["a"] + p["c"], p["a"] + p["b"] + p["c"],
                              p["a"] + p["c"] + 1],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9 and 2 <= p["c"] <= 9
                            and len({p["a"] + p["c"], p["a"] + p["b"] + p["c"],
                                     p["a"] + p["c"] + 1}) == 3,
                            "the y really is in the way (b at least 2, so grabbing it "
                            "is visibly different from the neighbour distractor)"),
    },
    "dstm": {  # a(x - b) = ax - ?
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: (f"Times the whole of x take away {p['b']} by {p['a']}. "
                             f"That comes to {p['a']} x take away what number?"),
        # The area model again, with a NEGATIVE room: [[areamodel]] parses "-b" and
        # prints the expanded sum with the minus carried through ("= ax - ab").
        "board": _dstm_board,         # (tf) the area model with the taken-away room blank
        "worked": _dstm_worked,       # (tf) the rooms read, the minus carried
        "praise": lambda p: (f"The {p['a']} reaches both rooms, minus and all: "
                             f"{p['a']} times x, and {p['a']} times {p['b']}, which "
                             f"equals {p['a'] * p['b']} — taken away. So it is "
                             f"{p['a']} x take away {p['a'] * p['b']}."),
        "key": lambda p: p["a"] * p["b"],
        # Same family as dst: the times never reaches the number (tap b), or the
        # numbers get added instead of timesed.
        "choices": lambda p: [p["a"] * p["b"], p["b"], p["a"] + p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and len({p["a"] * p["b"], p["b"],
                                     p["a"] + p["b"]}) == 3,
                            "the multiplier is at least 2 and the three options are "
                            "three different numbers"),
    },

    # ---- ALGEBRA I UNIT 2 (build kv) -- LINEAR EQUATIONS & INEQUALITIES -------
    # SOLVING BEGINS. Until now every x was handed to the child ("x is holding 5");
    # from here the equation holds it and the child gets it back by UNDOING -- the
    # same move off both sides. The board is ⭐ [[balance]], the balance-scale
    # renderer that (like [[areamodel]] and [[angle split=]] before it) has been in
    # the codebase since July and never once used by a scripted lesson. An equation
    # IS a balance; the figure is the argument.
    "un1": {   # x + a = b -- undo the plus
        "ans": lambda p: p["b"] - p["a"],
        "spoken": lambda p: (f"x plus {p['a']} equals {p['b']}. "
                             f"What number is x holding?"),
        "board": _un1_board,          # (tf) the balance as given
        "worked": _un1_worked,        # (tf) the balance with the a off both sides, checked
        "praise": lambda p: (f"Take {p['a']} off both sides and the scale stays "
                             f"level: x is {p['b']} take away {p['a']}, which "
                             f"equals {p['b'] - p['a']}."),
        "key": lambda p: p["b"] - p["a"],
        # The error is pushing the same way instead of undoing: x + 4 = 11 answered
        # with 15. The third option is tapping the right-hand side untouched.
        "choices": lambda p: [p["b"] - p["a"], p["b"] + p["a"], p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and p["a"] < p["b"] <= 30
                            and p["b"] - p["a"] >= 2,
                            "the hidden number is at least 2 and every number stays "
                            "small enough to check by counting"),
    },
    "un2": {   # ax = b -- undo the times
        "ans": lambda p: p["b"] // p["a"],
        "spoken": lambda p: (f"{p['a']} x equals {p['b']}. "
                             f"What number is x holding?"),
        "board": _un2_board,          # (tf) the balance and the a copies of x as a bar
        "worked": _un2_worked,        # (tf) one x on the pan, the bar shared
        "praise": lambda p: (f"{p['a']} x's weigh {p['b']}, so one x weighs "
                             f"{p['b']} shared between {p['a']} — "
                             f"{p['b'] // p['a']}."),
        "key": lambda p: p["b"] // p["a"],
        # The error is UNDOING THE WRONG OPERATION: taking the 3 away instead of
        # sharing between 3 -- 3x = 12 answered with 9.
        "choices": lambda p: [p["b"] // p["a"], p["b"] - p["a"],
                              p["b"] // p["a"] + 1],
        "check": lambda p: (2 <= p["a"] <= 9 and p["b"] % p["a"] == 0
                            and p["b"] // p["a"] >= 2
                            and len({p["b"] // p["a"], p["b"] - p["a"],
                                     p["b"] // p["a"] + 1}) == 3,
                            "it shares exactly, x is at least 2, and the take-away "
                            "error is visibly a different number"),
    },
    "un3": {   # ax + b = c -- two steps back, in reverse order
        "ans": lambda p: (p["c"] - p["b"]) // p["a"],
        "spoken": lambda p: (f"{p['a']} x plus {p['b']} equals {p['c']}. "
                             f"What number is x holding?"),
        "board": _un3_board,          # (tf) the balance as given
        "worked": _un3_worked,        # (tf) the balance after each undo
        "praise": lambda p: (f"The {p['b']} went on last, so it comes off first: "
                             f"{p['a']} x equals {p['c'] - p['b']}. Then share: "
                             f"x equals {(p['c'] - p['b']) // p['a']}."),
        "key": lambda p: (p["c"] - p["b"]) // p["a"],
        # The stop-at-step-one error again (rte, pcn, tri3 -- it is everywhere):
        # taking the b off, seeing ax = c-b, and tapping THAT number as x.
        "choices": lambda p: [(p["c"] - p["b"]) // p["a"], p["c"] - p["b"],
                              (p["c"] - p["b"]) // p["a"] + 1],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and (p["c"] - p["b"]) % p["a"] == 0
                            and (p["c"] - p["b"]) // p["a"] >= 2
                            and len({(p["c"] - p["b"]) // p["a"], p["c"] - p["b"],
                                     (p["c"] - p["b"]) // p["a"] + 1}) == 3,
                            "both undo steps land on whole numbers and the "
                            "stopped-halfway error is a different number"),
    },
    "ineq": {  # x + a < b -- the BIGGEST whole number x can hold
        "ans": lambda p: p["b"] - p["a"] - 1,
        "spoken": lambda p: (f"x plus {p['a']} is less than {p['b']}. "
                             f"What is the biggest whole number x can hold?"),
        "board": _ineq_board,         # (tf) the open circle and the shaded ray, the answer withheld
        "worked": _ineq_worked,       # (tf) the biggest whole number marked, checked
        "praise": lambda p: (f"x has to stay under {p['b'] - p['a']} — it can be "
                             f"anything less, and the biggest whole number under "
                             f"{p['b'] - p['a']} is {p['b'] - p['a'] - 1}."),
        "key": lambda p: p["b"] - p["a"] - 1,
        # THE inequality error: forgetting that "less than" shuts the door on the
        # number itself. x + 3 < 10 means x < 7, and 7 is NOT allowed.
        "choices": lambda p: [p["b"] - p["a"] - 1, p["b"] - p["a"],
                              p["b"] + p["a"]],
        "check": lambda p: (2 <= p["a"] <= 9 and p["a"] < p["b"] <= 30
                            and p["b"] - p["a"] >= 3,
                            "the boundary is at least 3, so the answer is a real "
                            "number and the door-shut error sits right beside it"),
    },

    # ---- ALGEBRA I UNIT 3 (build kw) -- FUNCTIONS & NOTATION ------------------
    # A function is a MACHINE: a number goes in, a rule happens to it, a number comes
    # out. The board is ⭐ [[machine]], the function-machine renderer -- the last of
    # July's figure shelf to get its first scripted use (areamodel kt, angle-split ks,
    # balance kv). It draws input -> rule box -> output AND prints "f(4) = 9"
    # underneath, so the notation lesson can point at a line the child has already
    # been looking at for a whole lesson.
    "fm1": {   # rule ax + b, input c -- what comes out?
        "ans": lambda p: p["a"] * p["c"] + p["b"],
        "spoken": lambda p: (f"A machine's rule is: times the input by {p['a']}, "
                             f"then add {p['b']}. Feed it {p['c']}. "
                             f"What number comes out?"),
        "board": _fm1_board,          # (tf) the machine with its output blank
        "worked": _fm1_worked,        # (tf) the machine filled, the rule's two steps
        "praise": lambda p: (f"{p['c']} goes in, the rule runs: {p['a']} times "
                             f"{p['c']} equals {p['a'] * p['c']}, plus {p['b']} — "
                             f"out comes {p['a'] * p['c'] + p['b']}."),
        "key": lambda p: p["a"] * p["c"] + p["b"],
        # The rule says its steps IN ORDER, so the wrong tap is running them the other
        # way: adding first. The third is ignoring the times altogether.
        "choices": lambda p: [p["a"] * p["c"] + p["b"],
                              p["a"] * (p["c"] + p["b"]),
                              p["a"] + p["b"] + p["c"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9 and 2 <= p["c"] <= 9
                            and len({p["a"] * p["c"] + p["b"],
                                     p["a"] * (p["c"] + p["b"]),
                                     p["a"] + p["b"] + p["c"]}) == 3,
                            "single digits and three distinct outputs -- which rules "
                            "out the inputs where timesing and adding agree"),
    },
    "fnot": {  # f(x) = x + a -- what is f(b)?
        "ans": lambda p: p["b"] + p["a"],
        "spoken": lambda p: (f"A new machine, still called f. f of x equals x plus {p['a']}. "
                             f"What is f of {p['b']}?"),   # (up) the name retired out loud, every problem
        "board": _fnot_board,         # (tf) machine f with its output blank
        "worked": _fnot_worked,       # (tf) f(b) filled
        "praise": lambda p: (f"f of {p['b']} means: feed the machine {p['b']}. "
                             f"{p['b']} plus {p['a']} equals {p['b'] + p['a']}."),
        "key": lambda p: p["b"] + p["a"],
        # THE notation error: reading f(3) as f TIMES 3 -- the parentheses have meant
        # "times" since the distributive lesson, and here they suddenly do not. The
        # wrong tap is the times reading; the third is handing back the input.
        "choices": lambda p: [p["b"] + p["a"], p["a"] * p["b"], p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and p["a"] * p["b"] != p["a"] + p["b"],
                            "single digits, never the 2-and-2 case, so the "
                            "f-times-b misreading is visibly a different number"),
    },
    "fm2": {   # machine one adds a, machine two times by b, input c -- IN ORDER
        "ans": lambda p: (p["c"] + p["a"]) * p["b"],
        "spoken": lambda p: (f"Two new machines in a row. The first adds {p['a']}. "   # (up) new, every problem
                             f"The second times by {p['b']}. Feed {p['c']} through "
                             f"both, first then second. What comes out?"),
        "board": _fm2_board,          # (tf) two machines, the second's output blank
        "worked": _fm2_worked,        # (tf) both filled, in order
        "praise": lambda p: (f"Machine one: {p['c']} plus {p['a']} equals "
                             f"{p['c'] + p['a']}. That goes straight into machine "
                             f"two: {p['c'] + p['a']} times {p['b']} equals "
                             f"{(p['c'] + p['a']) * p['b']}."),
        "key": lambda p: (p["c"] + p["a"]) * p["b"],
        # The error is running the machines in the WRONG ORDER -- timesing first,
        # then adding. Order mattering is the entire lesson.
        "choices": lambda p: [(p["c"] + p["a"]) * p["b"],
                              p["c"] * p["b"] + p["a"],
                              p["c"] + p["a"] + p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9 and 2 <= p["c"] <= 9
                            and len({(p["c"] + p["a"]) * p["b"],
                                     p["c"] * p["b"] + p["a"],
                                     p["c"] + p["a"] + p["b"]}) == 3,
                            "three distinct outputs, so the wrong-order error is a "
                            "real different tap"),
    },
    "fback": { # f(x) = x + a and f(?) = b -- which input was it?
        "ans": lambda p: p["b"] - p["a"],
        "spoken": lambda p: (f"A new machine, still called f. f of x equals x plus {p['a']}. "
                             f"f of WHAT equals {p['b']}? Which number went in?"),   # (up)
        "board": _fback_board,        # (tf) the machine with its input blank
        "worked": _fback_worked,      # (tf) the input found, run forwards
        "praise": lambda p: (f"The machine put out {p['b']} after adding {p['a']}, "
                             f"so {p['b']} take away {p['a']} went in — "
                             f"{p['b'] - p['a']}."),
        "key": lambda p: p["b"] - p["a"],
        # Running the machine FORWARDS with the output as input -- b + a -- is the
        # error; the third is tapping the output itself.
        "choices": lambda p: [p["b"] - p["a"], p["b"] + p["a"], p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and p["a"] < p["b"] <= 30
                            and p["b"] - p["a"] >= 2,
                            "the input is at least 2 and the numbers stay small "
                            "enough to check by running the machine forwards"),
    },

    # ---- ALGEBRA I UNIT 4 (build kx) -- LINEAR FUNCTIONS & GRAPHS -------------
    # The machine met the coordinate plane. A line IS the machine's whole table of
    # answers drawn at once -- every point is an input standing under its output. The
    # board is ⭐ [[graph]], the real function grapher (lines=, points=, range=) that
    # no scripted lesson has ever used. The ladder: read one point off a line, SLOPE
    # as how much y climbs when x steps once, the starting height where x is zero,
    # and finally slope and start working together to answer for any x.
    "lny": {   # y = x + a -- what is y when x = b?
        "ans": lambda p: p["b"] + p["a"],
        "spoken": lambda p: (f"The line is y equals x plus {p['a']}. "
                             f"What is y when x is {p['b']}?"),
        "board": _lny_board,          # (tg) the line and the climb from x = b, the height withheld
        "worked": _lny_worked,        # (tg) the point marked
        "praise": lambda p: (f"At x equals {p['b']}, the line stands at {p['b']} "
                             f"plus {p['a']} — y equals {p['b'] + p['a']}."),
        "key": lambda p: p["b"] + p["a"],
        # The graph error is SWAPPING THE PARTNERS: asked for y, tapping the x you
        # were given. The third option is the line's own added number.
        "choices": lambda p: [p["b"] + p["a"], p["b"], p["a"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9 and p["a"] != p["b"],
                            "a and b differ, so the swapped-partner tap and the "
                            "added-number tap are three different numbers"),
    },
    "slp": {   # through (b, c) and (b+1, c+a) -- how much does y go up?
        "ans": lambda p: p["a"],
        "spoken": lambda p: (f"A line passes through the point {p['b']} comma "
                             f"{p['c']}, and the point {p['b'] + 1} comma "
                             f"{p['c'] + p['a']}. When x goes up by 1, how much "
                             f"does y go up?"),
        "board": _slp_board,          # (tg) the two points, the climb asked
        "worked": _slp_worked,        # (tg) the line through them, the climb named
        "praise": lambda p: (f"x stepped once and y climbed from {p['c']} to "
                             f"{p['c'] + p['a']} — a climb of {p['a']}. That climb "
                             f"is called the slope."),
        "key": lambda p: p["a"],
        # The errors are reading a HEIGHT as the climb: tapping where y landed, or
        # where it started, instead of how far it moved.
        "choices": lambda p: [p["a"], p["c"] + p["a"], p["c"]],
        # The rise is the ANSWER, so it is deliberately never spoken; the two
        # heights and the x-step carry the problem.
        "speaks": lambda p, sp: (str(p["b"]) in sp and str(p["c"]) in sp
                                 and str(p["c"] + p["a"]) in sp),
        "check": lambda p: (2 <= p["a"] <= 9 and 1 <= p["b"] <= 4 and 2 <= p["c"] <= 9
                            and p["a"] != p["c"],
                            "the climb differs from both heights, so all three taps "
                            "are different numbers, and the points sit near the "
                            "origin where the graph can show them"),
    },
    "yint": {  # y = ax + b -- what is y when x is ZERO?
        "ans": lambda p: p["b"],
        "spoken": lambda p: (f"The line is y equals {p['a']} x plus {p['b']}. "
                             f"What is y when x is zero?"),
        "board": _yint_board,         # (tg) the line, the left wall asked
        "worked": _yint_worked,       # (tg) the start marked at x = 0
        "praise": lambda p: (f"{p['a']} times zero is zero — the times part "
                             f"vanishes, and y is just {p['b']}. That is where the "
                             f"line starts."),
        "key": lambda p: p["b"],
        # The error is tapping the SLOPE -- the other number in the rule -- or adding
        # the two as if x being zero changed nothing.
        "choices": lambda p: [p["b"], p["a"], p["a"] + p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9 and p["a"] != p["b"],
                            "slope and start differ, so the three taps are three "
                            "different numbers"),
    },
    "lin2": {  # y = ax + b -- what is y when x = c?
        "ans": lambda p: p["a"] * p["c"] + p["b"],
        "spoken": lambda p: (f"The line is y equals {p['a']} x plus {p['b']}. "
                             f"What is y when x is {p['c']}?"),
        "board": _lin2_board,         # (tg) the line and the climb from x = c
        "worked": _lin2_worked,       # (tg) the point marked, start and climb named
        "praise": lambda p: (f"Start at {p['b']}, climb {p['a']} for each of the "
                             f"{p['c']} steps: {p['a']} times {p['c']} equals "
                             f"{p['a'] * p['c']}, plus {p['b']} equals "
                             f"{p['a'] * p['c'] + p['b']}."),
        "key": lambda p: p["a"] * p["c"] + p["b"],
        # Off-by-one-step is the graph-reading error: the height one x to the LEFT.
        # The third is tapping the x itself.
        "choices": lambda p: [p["a"] * p["c"] + p["b"],
                              p["a"] * (p["c"] - 1) + p["b"], p["c"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 1 <= p["b"] <= 9 and 2 <= p["c"] <= 9
                            and len({p["a"] * p["c"] + p["b"],
                                     p["a"] * (p["c"] - 1) + p["b"],
                                     p["c"]}) == 3,
                            "three distinct heights, so the one-step-left error is a "
                            "real different tap"),
    },

    # ---- ALGEBRA I UNIT 5 (build ky) -- SYSTEMS OF EQUATIONS ------------------
    # Two rules true at once. The unit's one big picture is TWO LINES CROSSING --
    # [[graph]] takes lines="y=x+2; y=3x" and draws them both, and the crossing
    # point is the answer standing on the board. The ladder: see the crossing (sys1),
    # SWAP a letter for what it equals (sys2, substitution), the oldest system there
    # is -- a sum and a difference (sumd), and taking one equation away from another
    # so a whole unknown vanishes (elim, elimination in story clothes).
    "sys1": {  # y = x + a and y = bx -- which x makes both agree?
        "ans": lambda p: p["a"] // (p["b"] - 1),
        "spoken": lambda p: (f"One rule says y equals x plus {p['a']}. Another rule "
                             f"says y equals {p['b']} times x. For which x do both "
                             f"rules say the SAME y?"),
        "board": _sys1_board,         # (tg) two lines, the crossing ringed and asked
        "worked": _sys1_worked,       # (tg) the crossing labelled
        "praise": lambda p: (f"At x equals {p['a'] // (p['b'] - 1)}, both rules say "
                             f"y equals {p['b'] * (p['a'] // (p['b'] - 1))} — the "
                             f"lines cross there, and that crossing is the answer."),
        "key": lambda p: p["a"] // (p["b"] - 1),
        # U4's swapped-partner error comes back: tapping the Y where the lines meet
        # instead of the x that was asked for. The third is the rule's own plus number.
        "choices": lambda p: [p["a"] // (p["b"] - 1),
                              p["b"] * (p["a"] // (p["b"] - 1)), p["a"]],
        # a runs to 14, not 9: with b in 3..6 and the crossing forced whole and >= 2,
        # single-digit a yields only SIX distinct problems -- fewer than one bank.
        # The constraint surface here is genuinely small, and the wider a is what
        # buys a 10-problem ramp.
        "check": lambda p: (2 <= p["a"] <= 14 and 3 <= p["b"] <= 6
                            and p["a"] % (p["b"] - 1) == 0
                            and p["a"] // (p["b"] - 1) >= 2
                            and len({p["a"] // (p["b"] - 1),
                                     p["b"] * (p["a"] // (p["b"] - 1)),
                                     p["a"]}) == 3,
                            "the crossing lands on a whole x of at least 2, b is at "
                            "least 3 so the x never equals the plus number, and the "
                            "three taps differ"),
    },
    "sys2": {  # y = x + a and x + y = b -- what is x?
        "ans": lambda p: (p["b"] - p["a"]) // 2,
        "spoken": lambda p: (f"y equals x plus {p['a']}. Also, x plus y equals "
                             f"{p['b']}. What is x?"),
        "board": _sys2_board,         # (tg) the bar: two x's and the a, against b
        "worked": _sys2_worked,       # (tg) the bar with x found, y beside it
        "praise": lambda p: (f"Swap y for what it equals and there are two x's: "
                             f"2 x plus {p['a']} equals {p['b']}, so 2 x equals "
                             f"{p['b'] - p['a']}, and x equals "
                             f"{(p['b'] - p['a']) // 2}."),
        "key": lambda p: (p["b"] - p["a"]) // 2,
        # The middle option IS the other unknown -- y. Tapping the wrong letter's
        # value is the system error. The third is stopping at 2x.
        "choices": lambda p: [(p["b"] - p["a"]) // 2, (p["b"] + p["a"]) // 2,
                              p["b"] - p["a"]],
        "check": lambda p: (2 <= p["a"] <= 9 and p["a"] < p["b"] <= 30
                            and (p["b"] - p["a"]) % 2 == 0
                            and (p["b"] - p["a"]) // 2 >= 2
                            and p["b"] != 3 * p["a"],
                            "the swap lands on whole numbers, x is at least 2, and "
                            "b is never 3a (where stopping-at-2x collides with y)"),
    },
    "sumd": {  # together a, apart b -- the BIGGER of the two
        "ans": lambda p: (p["a"] + p["b"]) // 2,
        "spoken": lambda p: (f"Two secret numbers. Put together they equal {p['a']}. "
                             f"The bigger take away the smaller equals {p['b']}. "
                             f"What is the bigger number?"),
        "board": _sumd_board,         # (tg) the two bars: together, and the bigger as smaller-and-more
        "worked": _sumd_worked,       # (tg) the two numbers on the bar, both clues checked
        "praise": lambda p: (f"The bigger is {(p['a'] + p['b']) // 2} and the "
                             f"smaller is {(p['a'] - p['b']) // 2} — together "
                             f"{p['a']}, apart {p['b']}. Both rules happy at once."),
        "key": lambda p: (p["a"] + p["b"]) // 2,
        # The error is HALVING THE TOTAL -- splitting evenly as if the difference
        # rule were not there. One rule satisfied, the other ignored.
        "choices": lambda p: [(p["a"] + p["b"]) // 2, p["a"] // 2, p["b"]],
        "check": lambda p: (p["a"] % 2 == 0 and p["b"] % 2 == 0
                            and 2 <= p["b"] < p["a"] <= 30 and p["a"] != 2 * p["b"]
                            and (p["a"] - p["b"]) // 2 >= 1
                            and len({(p["a"] + p["b"]) // 2, p["a"] // 2,
                                     p["b"]}) == 3,
                            "both secret numbers are whole, the smaller is at least "
                            "1, and the split-evenly error is a different tap"),
    },
    "elim": {  # 2 pencils + eraser = a; 1 pencil + eraser = b -- the pencil?
        "ans": lambda p: p["a"] - p["b"],
        "spoken": lambda p: (f"Two pencils and an eraser cost {p['a']} cents. One "
                             f"pencil and the same eraser cost {p['b']} cents. "
                             f"What does one pencil cost?"),
        "board": _elim_board,         # (tg) the two trips as bars, the difference one pencil
        "worked": _elim_worked,       # (tg) the prices filled in
        "praise": lambda p: (f"Take the second buy away from the first: the eraser "
                             f"vanishes, one pencil is left, and it costs "
                             f"{p['a'] - p['b']} cents."),
        "key": lambda p: p["a"] - p["b"],
        # The middle option is the ERASER's price -- the other unknown again. The
        # third is halving the first buy as if it were two pencils and nothing else.
        "choices": lambda p: [p["a"] - p["b"], 2 * p["b"] - p["a"], p["a"] // 2],
        "check": lambda p: (p["b"] < p["a"] < 2 * p["b"] and p["a"] % 2 == 0
                            and p["a"] <= 30 and p["a"] - p["b"] >= 2
                            and 2 * p["b"] - p["a"] >= 1
                            and len({p["a"] - p["b"], 2 * p["b"] - p["a"],
                                     p["a"] // 2}) == 3,
                            "both prices are real (pencil and eraser at least 1), a "
                            "is even so the halving error is a whole tap, and the "
                            "three taps differ"),
    },

    # ---- ALGEBRA I UNIT 6 (build kz) -- EXPONENTS & EXPONENTIAL FUNCTIONS -----
    # Prealgebra U1 taught what a power IS (expn: "three 2s multiplied"). This unit
    # teaches how powers BEHAVE: the product rule as counting copies (x³ · x² is five
    # x's, not six), a power of a power as copies of copies, powers of ten carrying a
    # digit (scientific notation in child clothes), and finally DOUBLING -- the first
    # exponential growth, where the wrong tap is the linear thinker's answer.
    # _sup() writes the exponents as real superscripts on the board, the way expn
    # already wrote ² and ³ by hand.
    "exadd": { # x^a · x^b -- how many x's multiplied in all?
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"x to the power {p['a']}, times x to the power "
                             f"{p['b']}. Write out all the x's multiplied — "
                             f"how many x's are there?"),
        "board": _exadd_board,        # (tg) the x's written out as a bar, counted
        "worked": _exadd_worked,      # (tg) the bar with its count
        "praise": lambda p: (f"{p['a']} x's joined by {p['b']} more x's — "
                             f"{p['a'] + p['b']} x's multiplied, which is x to the "
                             f"power {p['a'] + p['b']}. The powers ADD."),
        "key": lambda p: p["a"] + p["b"],
        # THE exponent error: timesing the powers. x³ · x² read as x to the 6.
        "choices": lambda p: [p["a"] + p["b"], p["a"] * p["b"],
                              p["a"] + p["b"] + 1],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and len({p["a"] + p["b"], p["a"] * p["b"],
                                     p["a"] + p["b"] + 1}) == 3,
                            "three distinct counts -- which rules out 2·2 (where "
                            "adding and timesing agree) and 2·3 (where timesing "
                            "lands on the neighbour)"),
    },
    "exmul": { # (x^a)^b -- how many x's is that?
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: (f"Take x to the power {p['a']}, and raise all of it "
                             f"to the power {p['b']}. How many x's multiplied "
                             f"is that?"),
        "board": _exmul_board,        # (tg) b copies of x^a as a bar
        "worked": _exmul_worked,      # (tg) the copies counted
        "praise": lambda p: (f"{p['b']} copies of {p['a']} x's each: {p['a']} times "
                             f"{p['b']} equals {p['a'] * p['b']} x's. Copies of "
                             f"copies TIMES."),
        "key": lambda p: p["a"] * p["b"],
        # The mirror of exadd's error: ADDING here, where copies of copies times.
        # Taught back-to-back with exadd deliberately, because telling the two
        # situations apart IS the skill.
        "choices": lambda p: [p["a"] * p["b"], p["a"] + p["b"],
                              p["a"] * p["b"] + 1],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and len({p["a"] * p["b"], p["a"] + p["b"],
                                     p["a"] * p["b"] + 1}) == 3,
                            "three distinct counts, ruling out the cases where "
                            "adding collides with timesing or its neighbour"),
    },
    "sci": {   # b × 10^a
        "ans": lambda p: p["b"] * 10 ** p["a"],
        "spoken": lambda p: (f"What is {p['b']} times 10 to the power {p['a']}?"),
        "board": _sci_board,          # (tg) the digit on the chart before the move
        "worked": _sci_worked,        # (tg) the digit moved up a places
        "praise": lambda p: (f"10 to the {p['a']} is a 1 with {p['a']} zeros, so "
                             f"{p['b']} times it is {p['b']} with {p['a']} zeros — "
                             f"{p['b'] * 10 ** p['a']}."),
        "key": lambda p: p["b"] * 10 ** p["a"],
        # The times-not-power error, at ten: b × 10 × a instead of b × 10^a --
        # 3 times 10 to the 2 read as 3 × 10 × 2 = 60. The third option is one
        # power short, the place-value slip from Unit 8's changing-units lesson.
        "choices": lambda p: [p["b"] * 10 ** p["a"], p["b"] * 10 * p["a"],
                              p["b"] * 10 ** (p["a"] - 1)],
        "check": lambda p: (2 <= p["a"] <= 3 and 2 <= p["b"] <= 9,
                            "the exponent is at least 2 (at 1, times-ten and "
                            "ten-to-the agree and the error cannot be shown)"),
    },
    "dbl": {   # b pads, doubling every day, for a days
        "ans": lambda p: p["b"] * 2 ** p["a"],
        "spoken": lambda p: (f"A pond has {p['b']} lily pads, and the pads double "
                             f"every day. How many pads after {p['a']} days?"),
        # The sequence stops ONE DAY SHORT and ends on "?" -- drawn to the end it
        # hands the child the answer, and a board that answers its own ask teaches
        # tapping, not doubling.
        "board": _dbl_board,          # (tg) the bars one day short
        "worked": _dbl_worked,        # (tg) the bars to the end
        "praise": lambda p: (f"Doubling {p['a']} times: "
                             f"{' , then '.join(str(p['b'] * 2 ** d) for d in range(1, p['a'] + 1))}"
                             f" — {p['b'] * 2 ** p['a']} pads. Each day doubles "
                             f"EVERYTHING there is, not just the start."),
        "key": lambda p: p["b"] * 2 ** p["a"],
        # THE growth error is LINEAR THINKING: up by 2 a day (b + 2a), or "double"
        # read as times-2-times-days (b × 2 × a). Exponential beats both, visibly.
        "choices": lambda p: [p["b"] * 2 ** p["a"], p["b"] + 2 * p["a"],
                              p["b"] * 2 * p["a"]],
        "check": lambda p: (3 <= p["a"] <= 5 and 2 <= p["b"] <= 6
                            and p["b"] * 2 ** p["a"] <= 100
                            and len({p["b"] * 2 ** p["a"], p["b"] + 2 * p["a"],
                                     p["b"] * 2 * p["a"]}) == 3,
                            "at least 3 days (below that, doubling and times-2-"
                            "times-days agree), and the pond stays countable"),
    },

    # ---- ALGEBRA I UNIT 7 (build la) -- POLYNOMIALS & FACTORING ---------------
    # The area model comes back and then RUNS BACKWARDS. kt drew a(x + b); now the
    # rectangle is (x + a)(x + b) -- four rooms -- and factoring is the same picture
    # read the other way: given the rooms, find the sides. The unit ends on the
    # vanishing middle, the first identity a child meets that feels like a magic
    # trick and is just the rooms cancelling.
    "foil": {  # (x + a)(x + b) = x² + ?x + ab -- the x count
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"x plus {p['a']}, times x plus {p['b']}. That comes "
                            f"to x squared, plus how many x, plus "
                            f"{p['a'] * p['b']}?"),
        "board": _foil_board,         # (th) the four rooms, the middle two asked
        "worked": _foil_worked,       # (th) the rooms read
        "praise": lambda p: (f"The two x rooms hold {p['a']} x and {p['b']} x — "
                             f"{p['a'] + p['b']} x in all. x squared, plus "
                             f"{p['a'] + p['b']} x, plus {p['a'] * p['b']}."),
        "key": lambda p: p["a"] + p["b"],
        # The classic: forgetting the middle rooms entirely, or filling them with
        # the corner's product. The middle ADDS the two numbers; the corner times.
        "choices": lambda p: [p["a"] + p["b"], p["a"] * p["b"],
                              p["a"] + p["b"] + 1],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and len({p["a"] + p["b"], p["a"] * p["b"],
                                     p["a"] + p["b"] + 1}) == 3,
                            "three distinct counts (ruling out 2·2 and 2·3, where "
                            "the times collides with the add or its neighbour)"),
    },
    "fnum": {  # x² + (a+b)x + ab = (x + a)(x + ?)
        "ans": lambda p: p["b"],
        "spoken": lambda p: (f"x squared, plus {p['a'] + p['b']} x, plus "
                             f"{p['a'] * p['b']}, equals: x plus {p['a']}, times, "
                             f"x plus what?"),
        "board": _fnum_board,         # (th) the rooms with one side hidden
        "worked": _fnum_worked,       # (th) the side found, the sum back
        "praise": lambda p: (f"{p['a']} plus {p['b']} equals {p['a'] + p['b']}, and "
                             f"{p['a']} times {p['b']} equals {p['a'] * p['b']} — "
                             f"{p['b']} fits BOTH clues, and a factor has to fit "
                             f"both."),
        "key": lambda p: p["b"],
        # The wrong taps: the number that fits only ONE clue -- what is left after
        # subtracting from the product -- and the x count itself.
        "choices": lambda p: [p["b"], p["a"] * p["b"] - p["a"], p["a"] + p["b"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["a"] + p["b"]) in sp
                                 and str(p["a"] * p["b"]) in sp),
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and len({p["b"], p["a"] * p["b"] - p["a"],
                                     p["a"] + p["b"]}) == 3,
                            "three distinct taps -- which quietly excludes the "
                            "handful of pairs where the leftover collides"),
    },
    "gcfx": {  # (c·a)x + (c·b) = c(ax + ?)
        "ans": lambda p: p["b"],
        "spoken": lambda p: (f"{p['c'] * p['a']} x plus {p['c'] * p['b']} equals: "
                             f"{p['c']} times, {p['a']} x plus what?"),
        "board": _gcfx_board,         # (th) c tall, the second width hidden
        "worked": _gcfx_worked,       # (th) the width found, checked forwards
        "praise": lambda p: (f"The {p['c']} was pulled out of BOTH parts: "
                             f"{p['c'] * p['a']} x became {p['a']} x, so "
                             f"{p['c'] * p['b']} becomes {p['b']}. Both parts "
                             f"share, or it is not a common factor."),
        "key": lambda p: p["c"] * p["a"],
        # THE factoring-out error: pulling the factor from the x part only and
        # leaving the constant untouched -- 6x + 9 = 3(2x + 9).
        "choices": lambda p: [p["b"], p["c"] * p["b"], p["c"]],
        "speaks": lambda p, sp: (str(p["c"] * p["a"]) in sp
                                 and str(p["c"] * p["b"]) in sp
                                 and str(p["c"]) in sp),
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and 2 <= p["c"] <= 9 and p["b"] != p["c"]
                            and _gcd(p["a"], p["b"]) == 1,
                            "a and b share no factor (so c really is the WHOLE "
                            "common factor -- a half-factored answer would be a "
                            "lie), and b differs from c so the taps differ"),
    },
    "dsq": {   # (x + a)(x - a) = x² - ?
        "ans": lambda p: p["a"] * p["a"],
        "spoken": lambda p: (f"x plus {p['a']}, times x take away {p['a']}. That "
                             f"comes to x squared take away what number?"),
        "board": _dsq_board,          # (th) the four rooms, the corner asked
        "worked": _dsq_worked,        # (th) the middles cancelled, the corner read
        "praise": lambda p: (f"The middle rooms cancel — plus {p['a']} x and take "
                             f"away {p['a']} x land on nothing — leaving x squared "
                             f"take away {p['a'] * p['a']}."),
        "key": lambda p: p["a"] * p["a"],
        # The errors: tapping the number itself (x² − 3 for x² − 9), or doubling it
        # (the ghost of the middle terms that SHOULD have cancelled).
        "choices": lambda p: [p["a"] * p["a"], p["a"], 2 * p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (3 <= p["a"] <= 14,
                            "a is at least 3 (at 2, the square equals the double "
                            "and two taps collide)"),
    },

    # ---- ALGEBRA I UNIT 8 (build la) -- QUADRATIC FUNCTIONS -------------------
    # The curve arrives. y = x² is the first rule where the graph BENDS, and the
    # unit is built on the three things a child must feel about it: squaring is not
    # doubling, a product of zero means one of the factors is zero, and a square is
    # never negative (which is why the curve has a lowest point). The last lesson
    # throws a ball: height c take away x squared, and finding where it lands is
    # asking what number squared equals c.
    "sqy": {   # y = x² + b at x = a
        "ans": lambda p: p["a"] * p["a"] + p["b"],
        "spoken": lambda p: (f"The curve is y equals x squared plus {p['b']}. "
                             f"What is y when x is {p['a']}?"),
        "board": _sqy_board,          # (th) the curve and the climb from x = a
        "worked": _sqy_worked,        # (th) the point marked
        "praise": lambda p: (f"{p['a']} squared is {p['a']} times {p['a']} — "
                             f"{p['a'] * p['a']} — plus {p['b']} equals "
                             f"{p['a'] * p['a'] + p['b']}."),
        "key": lambda p: p["a"] * p["a"] + p["b"],
        # THE squaring error: x² read as 2x. The third tap drops the square entirely.
        "choices": lambda p: [p["a"] * p["a"] + p["b"], 2 * p["a"] + p["b"],
                              p["a"] + p["b"]],
        "check": lambda p: (3 <= p["a"] <= 9 and 1 <= p["b"] <= 9,
                            "x is at least 3 (at 2, squaring and doubling agree "
                            "and the error cannot be shown)"),
    },
    "roots": { # (x - a)(x - b) = 0 -- the other answer
        "ans": lambda p: p["b"],
        "spoken": lambda p: (f"x take away {p['a']}, times x take away {p['b']}, "
                             f"equals zero. One answer is x equals {p['a']}. "
                             f"What is the other answer?"),
        "board": _roots_board,        # (th) the curve with one ground point, the other asked
        "worked": _roots_worked,      # (th) both ground points
        "praise": lambda p: (f"If either bracket lands on zero, the whole thing is "
                             f"zero. x equals {p['a']} kills the first bracket, and "
                             f"x equals {p['b']} kills the second."),
        "key": lambda p: p["b"],
        # The wrong taps ADD or TIMES the two numbers -- treating the equation like
        # an arithmetic problem instead of reading which x kills a bracket.
        "choices": lambda p: [p["b"], p["a"] + p["b"], p["a"] * p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and p["a"] != p["b"]
                            and p["a"] + p["b"] != p["a"] * p["b"],
                            "two different roots, and the add and times taps are "
                            "different numbers"),
    },
    "vtx": {   # y = (x - a)² + b -- the lowest y
        "ans": lambda p: p["b"],
        "spoken": lambda p: (f"y equals: x take away {p['a']}, squared, plus "
                             f"{p['b']}. What is the LOWEST y this curve can ever "
                             f"reach?"),
        # The board shows the RULE and the square's floor -- never "0 + b = ?",
        # which is the answer wearing a hat (the pond taught this in kz).
        "board": _vtx_board,          # (th) the curve, how low asked
        "worked": _vtx_worked,        # (th) the lowest point marked
        "praise": lambda p: (f"A square can never be below zero — the smallest the "
                             f"squared part gets is 0, right at x equals {p['a']} — "
                             f"so the lowest y is 0 plus {p['b']}: {p['b']}."),
        "key": lambda p: p["b"],
        # The wrong taps: the OTHER number in the rule (where the low point sits
        # left-and-right, not how low it goes), and the two added.
        "choices": lambda p: [p["b"], p["a"], p["a"] + p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and p["a"] != p["b"],
                            "the across number and the up number differ, so the "
                            "three taps are three different numbers"),
    },
    "hitg": {  # y = a² - x² -- where does the height reach zero?
        "ans": lambda p: p["a"],
        "spoken": lambda p: (f"A ball's height is y equals {p['a'] * p['a']} take "
                             f"away x squared. At what x does the height reach "
                             f"zero?"),
        "board": _hitg_board,         # (th) the falling curve, the ground asked
        "worked": _hitg_worked,       # (th) the launch and the landing marked
        "praise": lambda p: (f"The height is zero when x squared equals "
                             f"{p['a'] * p['a']} — and {p['a']} squared is exactly "
                             f"that. {p['a']} is called the square root of "
                             f"{p['a'] * p['a']}."),
        "key": lambda p: p["a"],
        # The wrong taps: the height itself, and its half -- the child who reaches
        # for halving because halving undoes doubling, when what is needed is the
        # number that SQUARES to it.
        "choices": lambda p: [p["a"], p["a"] * p["a"], 2 * p["a"]],
        "speaks": lambda p, sp: str(p["a"] * p["a"]) in sp,
        "check": lambda p: (3 <= p["a"] <= 14,
                            "a is at least 3 (at 2, the double collides with the "
                            "square... with 2a = a² -- same wall as dsq)"),
    },

    # ---- ALGEBRA I UNIT 9 (build lc) -- DATA & STATISTICS ---------------------
    # The course's last statistics gap, and the last renderers on the shelf:
    # [[dotplot]], [[bars]] and [[boxplot]] have all been in math-figures.js since
    # July and none has ever been drawn by a scripted lesson. Every lesson here puts
    # the DATA on the board and asks a question the picture can answer -- which is
    # the whole argument for teaching statistics with a plot rather than a formula.
    "mean": {  # a values averaging b -- the mean
        "ans": lambda p: p["b"],
        "spoken": lambda p: (f"{p['a']} numbers add up to {p['a'] * p['b']}. "
                             f"What is their mean?"),
        # "in all", not "total" -- the spoken canon, kept on the board too so the
        # child reads the same word they hear (the validator only polices speech).
        "board": _mean_board,         # (th) the pile as a bar, shared into a hidden parts
        "worked": _mean_worked,       # (th) every part the mean
        "praise": lambda p: (f"Sharing {p['a'] * p['b']} equally between {p['a']} "
                             f"gives {p['b']} each — the mean is {p['b']}."),
        "key": lambda p: p["b"],
        # The error is dividing by the wrong thing -- by the total instead of by the
        # count -- or answering with the total itself.
        "choices": lambda p: [p["b"], p["a"] * p["b"], p["a"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["a"] * p["b"]) in sp),
        "check": lambda p: (3 <= p["a"] <= 9 and 2 <= p["b"] <= 20
                            and len({p["b"], p["a"] * p["b"], p["a"]}) == 3,
                            "at least three numbers to average, and the mean, the "
                            "total and the count are three different numbers"),
    },
    "medn": {  # the middle value of an odd list
        "ans": lambda p: p["b"],
        "spoken": lambda p: (f"Here are {2 * p['a'] + 1} numbers, smallest first: "
                             f"{_medlist_words(p)}. What is the median — the one in "
                             f"the middle?"),
        "board": _medn_board,         # (th) the dots in order, captioned
        "worked": _medn_worked,       # (th) the middle named
        "praise": lambda p: (f"With {2 * p['a'] + 1} numbers there are {p['a']} below "
                             f"and {p['a']} above, so the middle one is {p['b']} — "
                             f"that is the median."),
        "key": lambda p: p["b"],
        # The errors: the smallest, and the largest. A child who has not counted in
        # from both ends grabs an end.
        "choices": lambda p: [p["b"], p["b"] - p["a"], p["b"] + p["a"]],
        "speaks": lambda p, sp: str(p["b"] - p["a"]) in sp,
        "check": lambda p: (2 <= p["a"] <= 4 and p["a"] + 2 <= p["b"] <= 20,
                            "an odd-length list with a real middle, and every number "
                            "in it stays positive"),
    },
    "rnge": {  # biggest take away smallest
        "ans": lambda p: p["b"] - p["a"],
        "spoken": lambda p: (f"In a set of numbers the smallest is {p['a']} and the "
                             f"biggest is {p['b']}. What is the range?"),
        "board": _rnge_board,         # (th) the two ends as bars
        "worked": _rnge_worked,       # (th) the stretch on the number line
        "praise": lambda p: (f"The range is how far the data STRETCHES: {p['b']} "
                             f"take away {p['a']} equals {p['b'] - p['a']}."),
        "key": lambda p: p["b"] - p["a"],
        # The error is adding the two ends, or answering with an end itself.
        "choices": lambda p: [p["b"] - p["a"], p["a"] + p["b"], p["b"]],
        "check": lambda p: (2 <= p["a"] < p["b"] <= 40 and p["b"] - p["a"] >= 2,
                            "the two ends really differ and the range is a number "
                            "worth naming"),
    },
    "outl": {  # the mean MOVES when one value is huge -- the median does not
        "ans": lambda p: p["b"],
        "spoken": lambda p: (f"Four children have {p['b']} pencils each. A fifth "
                             f"child walks in with {p['c']}. What is the MEDIAN "
                             f"number of pencils now?"),
        "board": _outl_board,         # (th) the dots, the newcomer far out
        "worked": _outl_worked,       # (th) the median standing, the mean dragged
        "praise": lambda p: (f"The median is still {p['b']} — the middle child did "
                             f"not move. But the mean jumped to "
                             f"{(4 * p['b'] + p['c']) // 5}, dragged up by one "
                             f"unusual number."),
        "key": lambda p: p["b"],
        # The whole lesson: the wrong tap is the MEAN, which the outlier drags away.
        "choices": lambda p: [p["b"], (4 * p["b"] + p["c"]) // 5, p["c"]],
        "speaks": lambda p, sp: (str(p["b"]) in sp and str(p["c"]) in sp),
        "check": lambda p: ((4 * p["b"] + p["c"]) % 5 == 0
                            and 2 <= p["b"] <= 9 and p["c"] >= p["b"] + 15
                            and p["c"] <= 60
                            and len({p["b"], (4 * p["b"] + p["c"]) // 5,
                                     p["c"]}) == 3,
                            "the mean lands on a whole number, the newcomer is far "
                            "enough out to drag it visibly, and the three taps "
                            "differ"),
    },

    # ---- GEOMETRY UNIT 1 (build lc) -- FOUNDATIONS & CONSTRUCTIONS ------------
    # Geometry opens. Basic Math measured shapes and Prealgebra U8 met the straight
    # line and the triangle sum; this unit lays the vocabulary those facts stand on
    # -- the point, the line, the angle pair -- and it does it with the FIGURES, not
    # with definitions to memorise. [[angle split=]] and [[circle]] carry it.
    "comp": {  # two angles making a right angle
        "ans": lambda p: 90 - p["a"],
        "spoken": lambda p: (f"Two angles together make a right angle. One of them "
                             f"is {p['a']} degrees. How big is the other?"),
        "board": _comp_board,         # (ti) the square corner split, captioned
        "worked": _comp_worked,       # (ti) both pieces labelled
        "praise": lambda p: (f"A right angle is 90 degrees, so the other is 90 take "
                             f"away {p['a']} — {90 - p['a']} degrees. The two are "
                             f"called complementary."),
        "key": lambda p: 90 - p["a"],
        # The error is using the STRAIGHT LINE's 180 in place of the right angle's
        # 90 -- U8 taught 180 first, and it sticks.
        "choices": lambda p: [90 - p["a"], 180 - p["a"], p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (10 <= p["a"] <= 80 and p["a"] != 45,
                            "not the 45 case, where an angle and its partner are one "
                            "number and two taps collide"),
    },
    "vert": {  # X crossing: the angle opposite is equal, the one beside is 180-a
        "ans": lambda p: 180 - p["a"],
        "spoken": lambda p: (f"Two straight lines cross. One of the four angles is "
                             f"{p['a']} degrees. How big is the angle NEXT to it?"),
        "board": _vert_board,         # (ti) the X with the twin labelled, the neighbour asked
        "worked": _vert_worked,       # (ti) the straight line the two share
        "praise": lambda p: (f"The angle next to it shares a straight line with it, "
                             f"so the two make 180: the answer is "
                             f"{180 - p['a']} degrees. (The angle OPPOSITE is "
                             f"{p['a']} again — those are the equal pair.)"),
        "key": lambda p: 180 - p["a"],
        # The error is giving the OPPOSITE angle -- which really is a equal, but is
        # not the one asked for. Telling neighbour from opposite is the lesson.
        "choices": lambda p: [180 - p["a"], p["a"], 90 - p["a"]
                              if p["a"] < 90 else 360 - p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (20 <= p["a"] <= 70
                            and len({180 - p["a"], p["a"], 90 - p["a"]}) == 3,
                            "the angle is acute so all three taps are positive and "
                            "different"),
    },
    "circ": {  # radius a -- what is the diameter?
        "ans": lambda p: 2 * p["a"],
        "spoken": lambda p: (f"A circle has a radius of {p['a']}. "
                             f"What is its diameter?"),
        "board": _circ_board,         # (ti) the radius drawn, the diameter asked
        "worked": _circ_worked,       # (ti) the diameter drawn edge to edge
        "praise": lambda p: (f"The diameter crosses the whole circle, so it is two "
                             f"radiuses: 2 times {p['a']} equals {2 * p['a']}."),
        "key": lambda p: 2 * p["a"],
        # The error is halving instead of doubling -- the child who remembers the
        # two words are related and not which way round.
        "choices": lambda p: [2 * p["a"], p["a"] // 2 if p["a"] % 2 == 0 else p["a"],
                              p["a"] + 2],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (p["a"] % 2 == 0 and 4 <= p["a"] <= 40
                            and len({2 * p["a"], p["a"] // 2, p["a"] + 2}) == 3,
                            "an even radius so the halving error is a whole number a "
                            "child could really tap, and three distinct options"),
    },
    "mid": {   # midpoint of a segment from a to b on a number line
        "ans": lambda p: (p["a"] + p["b"]) // 2,
        "spoken": lambda p: (f"A line runs from {p['a']} to {p['b']}. "
                             f"What number is exactly halfway along it?"),
        "board": _mid_board,          # (ti) the two ends, captioned
        "worked": _mid_worked,        # (ti) the middle marked with the halfway line
        "praise": lambda p: (f"Halfway between {p['a']} and {p['b']} is "
                             f"{(p['a'] + p['b']) // 2} — the same distance from "
                             f"each end. That point is called the midpoint."),
        "key": lambda p: (p["a"] + p["b"]) // 2,
        # The errors: halving the far end alone (forgetting the line does not start
        # at zero), and the LENGTH of the line rather than its middle.
        "choices": lambda p: [(p["a"] + p["b"]) // 2, p["b"] // 2, p["b"] - p["a"]],
        "check": lambda p: ((p["a"] + p["b"]) % 2 == 0 and 2 <= p["a"] < p["b"] <= 40
                            and p["b"] % 2 == 0
                            and len({(p["a"] + p["b"]) // 2, p["b"] // 2,
                                     p["b"] - p["a"]}) == 3,
                            "the midpoint is whole, the start is off zero so the "
                            "halve-the-end error is real, and the taps differ"),
    },

    # ---- GEOMETRY UNIT 2 (build ld) -- TRANSFORMATIONS & SYMMETRY -------------
    # The three moves -- slide, flip, turn -- each own ONE coordinate rule, and every
    # wrong tap in the unit applies the right rule to the WRONG coordinate, the wrong
    # direction, or the wrong number of signs. [[graph points=]] puts the moving
    # point on the real grid; the image point is never drawn on an ask board.
    "tran": {  # slide right c: only x changes, by adding
        "ans": lambda p: p["a"] + p["c"],
        "spoken": lambda p: (f"The point ({p['a']}, {p['b']}) slides {p['c']} to the "
                             f"right. What is the new x coordinate?"),
        "board": _tran_board,         # (ti) the point, captioned
        "worked": _tran_worked,       # (ti) the point and where it landed
        "praise": lambda p: (f"Sliding right {p['c']} moves x from {p['a']} to "
                             f"{p['a'] + p['c']} — and y stayed at {p['b']}."),
        "key": lambda p: p["a"] + p["c"],
        # The errors: sliding the WRONG coordinate (the slide lands on y's number),
        # and sliding the wrong WAY (right taken as left).
        "choices": lambda p: [p["a"] + p["c"], p["b"] + p["c"], p["a"] - p["c"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["c"]) in sp),
        "check": lambda p: (2 <= p["a"] <= 9 and 1 <= p["b"] <= 9
                            and 2 <= p["c"] <= 5 and p["a"] != p["b"]
                            and p["a"] - p["c"] >= 1
                            and len({p["a"] + p["c"], p["b"] + p["c"],
                                     p["a"] - p["c"]}) == 3,
                            "the point stays on the small grid, the wrong-way slide "
                            "stays right of zero, and the three taps differ"),
    },
    "refl": {  # flip across the y line: x changes sign, y stays
        "ans": lambda p: -p["a"],
        "spoken": lambda p: (f"The point ({p['a']}, {p['b']}) flips across the "
                             f"y line. What is the new x coordinate?"),
        "board": _refl_board,         # (ti) the mirror and the point
        "worked": _refl_worked,       # (ti) both sides of the mirror
        "praise": lambda p: (f"Across the y line the point keeps its height and its "
                             f"distance — it only crosses over: x goes from "
                             f"{p['a']} to negative {p['a']}, and y stays "
                             f"{p['b']}."),
        "key": lambda p: p["a"],
        # The errors: leaving x alone (no flip happened), and flipping the WRONG
        # coordinate (the mirror does not change heights).
        "choices": lambda p: [-p["a"], p["a"], -p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 1 <= p["b"] <= 9
                            and p["a"] != p["b"]
                            and len({-p["a"], p["a"], -p["b"]}) == 3,
                            "the two coordinates differ, so flipping the wrong one "
                            "is a visible mistake, and the three taps differ"),
    },
    "htrn": {  # half turn about (0,0): BOTH signs change; asked for the new y
        "ans": lambda p: -p["b"],
        "spoken": lambda p: (f"The point ({p['a']}, {p['b']}) turns half way around "
                             f"the point (0, 0). What is the new y coordinate?"),
        "board": _htrn_board,         # (ti) the point, captioned
        "worked": _htrn_worked,       # (ti) the opposite spot
        "praise": lambda p: (f"A half turn around (0, 0) carries the point to the "
                             f"exact opposite spot — both signs change, and y goes "
                             f"from {p['b']} to negative {p['b']}."),
        "key": lambda p: p["b"],
        # The errors: forgetting the turn reaches y at all, and flipping signs but
        # answering with the x number -- the wrong coordinate again.
        "choices": lambda p: [-p["b"], p["b"], -p["a"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and p["a"] != p["b"]
                            and len({-p["b"], p["b"], -p["a"]}) == 3,
                            "the two coordinates differ, so the wrong-coordinate "
                            "tap is visible, and the three taps differ"),
    },
    "rota": {  # turn symmetry of a wheel with a equal parts: 360 / a degrees
        "ans": lambda p: 360 // p["a"],
        "spoken": lambda p: (f"A wheel is cut into {p['a']} equal parts, all alike. "
                             f"Turn the wheel about its middle. After how many "
                             f"degrees does it first land exactly on itself?"),
        # The pie renderer counts wedges only up to 12; past that the steps carry
        # the picture's job (a 15-part wheel drawn tiny teaches nothing anyway).
        "board": _rota_board,         # (ti) the wheel, captioned
        "worked": _rota_worked,       # (ti) the parts as degrees
        "praise": lambda p: (f"One full turn is 360 degrees, and {p['a']} equal "
                             f"parts share it: 360 divided by {p['a']} equals "
                             f"{360 // p['a']} degrees — the first turn that lands "
                             f"the wheel on itself."),
        "key": lambda p: p["a"],
        # The errors: the half-turn habit (180 brings SOME shapes back, not all),
        # and answering with the COUNT of parts as if it were an angle.
        "choices": lambda p: [360 // p["a"], 180, p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        # ky's lesson (enumerate before promising a ramp): only the divisors of 360
        # qualify, and between 3 and 24 there are exactly twelve -- 3, 4, 5, 6, 8,
        # 9, 10, 12, 15, 18, 20, 24 -- which is precisely two pair-asks plus a
        # ten-problem bank. The cap is 24 BECAUSE the surface needs all twelve.
        "check": lambda p: (3 <= p["a"] <= 24 and 360 % p["a"] == 0
                            and len({360 // p["a"], 180, p["a"]}) == 3,
                            "the parts share 360 exactly (divisors of 360 only -- "
                            "the whole surface is twelve problems), and the three "
                            "taps differ"),
    },

    # ---- GEOMETRY UNIT 3 (build ld) -- CONGRUENCE & TRIANGLE PROOFS -----------
    # Congruent means every matching part is equal, and the letters -- not the
    # picture -- say which parts match. Then the first proofs: the isosceles pair
    # read both directions, and the exterior angle built from two owned facts.
    # [[triangle ticks=]] draws the equal-side marks it was built for.
    "cong": {  # ABC ≅ DEF with all three sides given -- which one does FD match?
        "ans": lambda p: p["c"],
        "spoken": lambda p: (f"Triangle ABC and triangle DEF are congruent. Side AB "
                             f"is {p['a']}, side BC is {p['b']}, and side CA is "
                             f"{p['c']}. How long is side FD?"),
        "board": _cong_board,         # (ti) ABC with its sides, captioned
        "worked": _cong_worked,       # (ti) ABC beside its copy DEF
        "praise": lambda p: (f"F matches C and D matches A, so side FD matches "
                             f"side CA — {p['c']}."),
        "key": lambda p: p["c"],
        # The errors: the other two sides -- matched by eye or by position on the
        # page instead of by the letters. Both are on the figure, both are wrong.
        "choices": lambda p: [p["c"], p["a"], p["b"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["c"]) in sp),
        "check": lambda p: (2 <= p["a"] <= 20 and 2 <= p["b"] <= 20
                            and 2 <= p["c"] <= 20
                            and len({p["a"], p["b"], p["c"]}) == 3
                            and p["a"] < p["b"] + p["c"]
                            and p["b"] < p["a"] + p["c"]
                            and p["c"] < p["a"] + p["b"],
                            "three different side lengths that really form a "
                            "triangle (each side under the other two put "
                            "together)"),
    },
    "isos": {  # two equal sides -> equal base angles; apex from one base angle
        "ans": lambda p: 180 - 2 * p["a"],
        # The ask states GIVENS only ("each base angle is 40") -- saying "the base
        # angles are equal too" in every problem would re-teach the rule forever
        # (kw's scaffold-never-fades distinction).
        "spoken": lambda p: (f"A triangle has two equal sides, marked with ticks. "
                             f"Each base angle is {p['a']} degrees. How big is the "
                             f"angle at the top?"),
        "board": _isos_board,         # (ti) the base angles, the top blank
        "worked": _isos_worked,       # (ti) all three
        "praise": lambda p: (f"The three angles put together are 180: {p['a']} and "
                             f"{p['a']} use {2 * p['a']}, so the top angle is 180 "
                             f"take away {2 * p['a']} — {180 - 2 * p['a']} "
                             f"degrees."),
        "key": lambda p: p["a"],
        # The errors: taking away only ONE base angle (the twin is still inside),
        # and answering with the base angle itself -- true of its twin, not the top.
        "choices": lambda p: [180 - 2 * p["a"], 180 - p["a"], p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (20 <= p["a"] <= 80 and p["a"] != 60
                            and len({180 - 2 * p["a"], 180 - p["a"],
                                     p["a"]}) == 3,
                            "not the 60 case, where the triangle is equilateral "
                            "and all three taps become one number"),
    },
    "extr": {  # the exterior angle equals the two far interior angles together
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"In a triangle, two of the angles are {p['a']} "
                             f"degrees and {p['b']} degrees. One side of the third "
                             f"corner is stretched out, and that opens an exterior "
                             f"angle. How big is the exterior angle?"),
        "board": _extr_board,         # (ti) two angles, the third corner opened
        "worked": _extr_worked,       # (ti) the inside corner and the exterior
        "praise": lambda p: (f"The exterior angle equals the two far inside angles "
                             f"put together: {p['a']} plus {p['b']} equals "
                             f"{p['a'] + p['b']} degrees."),
        "key": lambda p: p["a"] + p["b"],
        # The errors: the third INSIDE angle offered as if it were the exterior
        # (right computation, wrong angle), and the straight-line rule applied to
        # one given angle alone.
        "choices": lambda p: [p["a"] + p["b"], 180 - p["a"] - p["b"],
                              180 - p["b"]],
        "check": lambda p: (20 <= p["a"] <= 90 and 20 <= p["b"] <= 90
                            and p["a"] + p["b"] <= 150
                            and len({p["a"] + p["b"], 180 - p["a"] - p["b"],
                                     180 - p["b"]}) == 3,
                            "a real third corner is left over, and the exterior, "
                            "the inside corner and the one-angle slip are three "
                            "different numbers"),
    },
    "chas": {  # the reverse of isos: apex given, each base angle = (180 - a) / 2
        "ans": lambda p: (180 - p["a"]) // 2,
        # Scene-setting only: no "the base angles are equal" re-teach, and no
        # per-ask gloss of apex -- the teach beats own the vocabulary.
        "spoken": lambda p: (f"An isosceles triangle has its apex at {p['a']} "
                             f"degrees. How big is each base angle?"),
        "board": _chas_board,         # (ti) the apex, the base angles blank
        "worked": _chas_worked,       # (ti) all three
        "praise": lambda p: (f"180 take away {p['a']} leaves {180 - p['a']} for the "
                             f"two base angles — shared equally, each one is "
                             f"{(180 - p['a']) // 2} degrees."),
        "key": lambda p: p["a"],
        # The errors: stopping at 180 - a (the PAIR's share, still owned by two
        # corners), and halving 180 FIRST then taking the apex away -- the order
        # slip, 90 - a.
        "choices": lambda p: [(180 - p["a"]) // 2, 180 - p["a"], 90 - p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (20 <= p["a"] <= 88 and p["a"] % 2 == 0
                            and p["a"] != 60
                            and len({(180 - p["a"]) // 2, 180 - p["a"],
                                     90 - p["a"]}) == 3,
                            "an even apex under 90 so each base angle is whole and "
                            "the order-slip tap stays positive; not 60, where the "
                            "answer equals the apex"),
    },

    # ---- GEOMETRY UNIT 4 (build le) -- SIMILARITY & DILATIONS -----------------
    # ONE THREAD: a scale factor is a TIMES, never an ADD. The additive error --
    # "from 3 to 6 is 3 more, so 5 becomes 8" -- is the best-documented
    # misconception in all of similarity, and it is a distractor in every lesson
    # here. The closer is the k-squared area surprise.
    "scal": {  # one side under a scale factor: a times b
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: (f"A triangle is enlarged by a scale factor of "
                             f"{p['b']}. One of its sides is {p['a']}. How long is "
                             f"that side in the enlarged copy?"),
        "board": _scal_board,         # (tj) the small triangle, captioned
        "worked": _scal_worked,       # (tj) the small beside the enlarged copy
        "praise": lambda p: (f"Scale factor {p['b']} is a times: {p['a']} times "
                             f"{p['b']} equals {p['a'] * p['b']}."),
        "key": lambda p: p["a"] * p["b"],
        # The errors: ADDING the factor (the unit's one great misconception), and
        # dividing by it -- the shrink direction, remembered the wrong way round.
        "choices": lambda p: [p["a"] * p["b"], p["a"] + p["b"], p["a"] // p["b"]],
        "check": lambda p: (2 <= p["b"] <= 5 and 4 <= p["a"] <= 20
                            and p["a"] % p["b"] == 0
                            and len({p["a"] * p["b"], p["a"] + p["b"],
                                     p["a"] // p["b"]}) == 3,
                            "the divide-error tap is a whole number a child could "
                            "really reach, and the three taps differ"),
    },
    "sfac": {  # find the scale factor from one matching pair: b divided by a
        "ans": lambda p: p["b"] // p["a"],
        # Givens only -- no per-ask gloss of "similar" (kw's scaffold rule; the
        # teach beats own the vocabulary).
        "spoken": lambda p: (f"Two shapes are similar. A side of {p['a']} in the "
                             f"small one matches a side of {p['b']} in the big "
                             f"one. What is the scale factor?"),
        "board": _sfac_board,         # (tj) the matching sides as bars
        "worked": _sfac_worked,       # (tj) the factor named, checked backwards
        "praise": lambda p: (f"{p['b']} divided by {p['a']} equals "
                             f"{p['b'] // p['a']} — and check it backwards: "
                             f"{p['a']} times {p['b'] // p['a']} equals "
                             f"{p['b']}."),
        "key": lambda p: p["b"],
        # The errors: the DIFFERENCE between the sides (additive thinking), and
        # the big side itself -- a side is not a factor.
        "choices": lambda p: [p["b"] // p["a"], p["b"] - p["a"], p["b"]],
        "check": lambda p: (2 <= p["a"] <= 12 and p["a"] < p["b"] <= 24
                            and p["b"] % p["a"] == 0
                            and 2 <= p["b"] // p["a"] <= 5
                            and len({p["b"] // p["a"], p["b"] - p["a"],
                                     p["b"]}) == 3,
                            "a whole factor between 2 and 5, and the factor, the "
                            "difference and the big side are three different "
                            "numbers"),
    },
    "mside": {  # missing side of a similar triangle: factor from a's pair, times b
        "ans": lambda p: p["b"] * p["c"],
        "spoken": lambda p: (f"Two triangles are similar. The side of {p['a']} "
                             f"matches the side of {p['a'] * p['c']} in the big "
                             f"one. Another side of the small triangle is "
                             f"{p['b']}. How long is its matching side?"),
        "board": _mside_board,        # (tj) the small triangle, the match asked
        "worked": _mside_worked,      # (tj) the small beside the big
        "praise": lambda p: (f"{p['a'] * p['c']} divided by {p['a']} says the "
                             f"factor is {p['c']} — and {p['b']} times {p['c']} "
                             f"equals {p['b'] * p['c']}."),
        "key": lambda p: p["b"] * p["c"],
        # The errors: adding the same DIFFERENCE instead of scaling (the classic
        # similarity mistake, in its natural habitat), and leaving the side alone.
        "choices": lambda p: [p["b"] * p["c"],
                              p["b"] + p["a"] * (p["c"] - 1), p["b"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["a"] * p["c"]) in sp),
        "check": lambda p: (2 <= p["c"] <= 4 and 2 <= p["a"] <= 10
                            and 2 <= p["b"] <= 10 and p["a"] != p["b"]
                            and len({p["b"] * p["c"],
                                     p["b"] + p["a"] * (p["c"] - 1),
                                     p["b"]}) == 3,
                            "the two small sides differ (so the additive trap is "
                            "a different number than the answer), and the three "
                            "taps differ"),
    },
    "sare": {  # area under a scale factor: the factor strikes BOTH directions
        "ans": lambda p: p["a"] * p["b"] * p["b"],
        "spoken": lambda p: (f"A shape has an area of {p['a']} square units. It "
                             f"is enlarged by a scale factor of {p['b']}. What is "
                             f"the area of the enlarged copy?"),
        "board": _sare_board,         # (tj) b by b boxes for every one
        "worked": _sare_worked,       # (tj) the boxes counted
        "praise": lambda p: (f"Area lives in two directions, and the factor "
                             f"strikes both: {p['a']} times {p['b']} times "
                             f"{p['b']} equals {p['a'] * p['b'] * p['b']}."),
        "key": lambda p: p["a"] * p["b"] * p["b"],
        # The errors: scaling the area like a LENGTH (times k once -- everyone's
        # first answer), and adding the factor.
        "choices": lambda p: [p["a"] * p["b"] * p["b"], p["a"] * p["b"],
                              p["a"] + p["b"]],
        "check": lambda p: (2 <= p["b"] <= 4 and 2 <= p["a"] <= 10
                            and len({p["a"] * p["b"] * p["b"],
                                     p["a"] * p["b"],
                                     p["a"] + p["b"]}) == 3,
                            "the squared answer, the once-scaled slip and the "
                            "added slip are three different numbers"),
    },

    # ---- GEOMETRY UNIT 5 (build le) -- RIGHT TRIANGLES & TRIGONOMETRY ---------
    # Pythagoras forward and backwards on the named triples, then the tangent met
    # as U4's ratio living inside one triangle (and alg1-u4's climb, renamed).
    # ⭐ [[righttriangle]] -- July's shelf -- draws its first scripted lessons.
    # RENDERER RULE learned reading it: the figure ALWAYS labels the hypotenuse
    # (computed if not given), so it may appear on teach/worked boards and on
    # TANGENT asks (where hyp is not the question) but NEVER on a Pythagorean ask
    # board -- there it would print the answer. Those asks use [[triangle
    # right=]], whose sides= labels only what the author lists.
    "pyth": {  # legs a, b -> hypotenuse c (Pythagorean triples only)
        "ans": lambda p: p["c"],
        "spoken": lambda p: (f"A right triangle has legs of {p['a']} and "
                             f"{p['b']}. How long is the hypotenuse?"),
        "board": _pyth_board,         # (tj) the legs, the hypotenuse blank
        "worked": _pyth_worked,       # (tj) all three sides
        "praise": lambda p: (f"{p['a']} squared is {p['a'] * p['a']} and "
                             f"{p['b']} squared is {p['b'] * p['b']}; put "
                             f"together that is {p['a'] * p['a'] + p['b'] * p['b']} "
                             f"— and {p['c']} times {p['c']} equals "
                             f"{p['c'] * p['c']}, so the hypotenuse is {p['c']}."),
        "key": lambda p: p["c"],
        # The errors: ADDING the legs (walking around the corner), and stopping at
        # the SQUARE of the answer.
        "choices": lambda p: [p["c"], p["a"] + p["b"],
                              p["a"] * p["a"] + p["b"] * p["b"]],
        "check": lambda p: (p["a"] * p["a"] + p["b"] * p["b"]
                            == p["c"] * p["c"]
                            and 3 <= p["a"] <= 32 and 3 <= p["b"] <= 32
                            and 5 <= p["c"] <= 40
                            and len({p["c"], p["a"] + p["b"],
                                     p["a"] * p["a"] + p["b"] * p["b"]}) == 3,
                            "a true Pythagorean triple with whole sides (the "
                            "answer must square back exactly)"),
    },
    "leg": {   # hypotenuse c and one leg a -> the other leg b
        "ans": lambda p: p["b"],
        "spoken": lambda p: (f"A right triangle's hypotenuse is {p['c']}, and one "
                             f"leg is {p['a']}. How long is the other leg?"),
        "board": _leg_board,          # (tj) the hypotenuse and one leg
        "worked": _leg_worked,        # (tj) all three sides
        "praise": lambda p: (f"{p['c']} squared is {p['c'] * p['c']}, take away "
                             f"{p['a']} squared, {p['a'] * p['a']}, leaves "
                             f"{p['c'] * p['c'] - p['a'] * p['a']} — and "
                             f"{p['b']} times {p['b']} equals "
                             f"{p['b'] * p['b']}, so the other leg is {p['b']}."),
        "key": lambda p: p["c"],
        # The errors: taking away the LENGTHS instead of the squares, and stopping
        # at the square of the answer (pyth's second trap, mirrored).
        "choices": lambda p: [p["b"], p["c"] - p["a"],
                              p["c"] * p["c"] - p["a"] * p["a"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["c"]) in sp),
        "check": lambda p: (p["a"] * p["a"] + p["b"] * p["b"]
                            == p["c"] * p["c"]
                            and 3 <= p["a"] <= 32 and 3 <= p["b"] <= 32
                            and 5 <= p["c"] <= 40
                            and len({p["b"], p["c"] - p["a"],
                                     p["c"] * p["c"] - p["a"] * p["a"]}) == 3,
                            "a true triple, and the leg, the length-difference "
                            "slip and the unsquared slip are three different "
                            "numbers"),
    },
    "tang": {  # adjacent a, opposite b -> the tangent b/a (whole ratios only)
        "ans": lambda p: p["b"] // p["a"],
        "spoken": lambda p: (f"The marked angle has an adjacent side of {p['a']} "
                             f"and an opposite side of {p['b']}. What is the "
                             f"tangent of the angle?"),
        # righttriangle is SAFE here: it labels the two givens and the (decimal)
        # hypotenuse -- none of which is the ratio being asked for.
        "board": _tang_board,         # (tj) the marked angle, captioned
        "worked": _tang_worked,       # (tj) the climb named
        "praise": lambda p: (f"Tangent is the climb for every one across: "
                             f"{p['b']} divided by {p['a']} equals "
                             f"{p['b'] // p['a']}."),
        "key": lambda p: p["b"],
        # The errors: the DIFFERENCE of the sides (a length, not a ratio), and the
        # opposite side copied -- a side is not a ratio.
        "choices": lambda p: [p["b"] // p["a"], p["b"] - p["a"], p["b"]],
        "check": lambda p: (2 <= p["a"] <= 6 and p["b"] % p["a"] == 0
                            and 2 <= p["b"] // p["a"] <= 5 and p["b"] <= 24
                            and len({p["b"] // p["a"], p["b"] - p["a"],
                                     p["b"]}) == 3,
                            "a whole tangent between 2 and 5, and the ratio, the "
                            "difference and the side are three different numbers"),
    },
    "topp": {  # tangent b and adjacent a -> opposite side a times b
        "ans": lambda p: p["a"] * p["b"],
        # NOT "the marked angle": this op's ask board is [[triangle]], which draws
        # no angle mark -- speech may never claim a mark the figure lacks (Jim's
        # 2026-08-01 live catch, the split-ray lesson). tang's ask says "marked"
        # because righttriangle really draws the θ arc.
        "spoken": lambda p: (f"An angle in a right triangle has a tangent of "
                             f"{p['b']}. Its adjacent side is {p['a']}. How long "
                             f"is its opposite side?"),
        # NOT righttriangle here: drawing it would need opp= -- the answer, printed.
        "board": _topp_board,         # (tj) the adjacent side, the opposite blank
        "worked": _topp_worked,       # (tj) both legs
        "praise": lambda p: (f"A tangent of {p['b']} climbs {p['b']} for every "
                             f"one across: {p['a']} across times {p['b']} equals "
                             f"{p['a'] * p['b']}."),
        "key": lambda p: p["a"] * p["b"],
        # The errors: U4's additive habit (adding the tangent to the side), and
        # the tangent itself -- a steepness, not a side.
        "choices": lambda p: [p["a"] * p["b"], p["a"] + p["b"], p["b"]],
        "check": lambda p: (3 <= p["a"] <= 10 and 2 <= p["b"] <= 4
                            and len({p["a"] * p["b"], p["a"] + p["b"],
                                     p["b"]}) == 3,
                            "the scaled side, the added slip and the bare tangent "
                            "are three different numbers"),
    },

    # ---- GEOMETRY UNIT 6 (build lf) -- CIRCLES --------------------------------
    # The whole is 360 (not 180 -- the straight-line habit is the standing wrong
    # tap), the inscribed angle is HALF its arc read in both directions, and arc
    # length as one equal part of the distance around. RENDERER RULE (read before
    # designing, like righttriangle's): [[circle inscribed=X]] labels the vertex
    # angle as X/2 -- so it may carry teach/worked boards and ANGLE-TO-ARC asks
    # (where the label is the given), but never an arc-to-angle ask (where the
    # label would be the answer).
    "cent": {  # a central angle a -- how big is the REST of the circle?
        "ans": lambda p: 360 - p["a"],
        "spoken": lambda p: (f"Two radiuses cut a circle into two arcs. The small "
                             f"arc's angle at the middle is {p['a']} degrees. How "
                             f"many degrees is the rest of the circle?"),
        "board": _cent_board,         # (tj) the circle, captioned
        "worked": _cent_worked,       # (tj) the two arcs as a pie
        "praise": lambda p: (f"The whole circle is 360 degrees, and this arc uses "
                             f"{p['a']} — the rest is {360 - p['a']} degrees."),
        "key": lambda p: p["a"],
        # The errors: the straight LINE's share (180, three units of triangle work
        # make it leap to mind first), and the arc copied.
        "choices": lambda p: [360 - p["a"], 180 - p["a"], p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (20 <= p["a"] <= 160 and p["a"] != 90
                            and len({360 - p["a"], 180 - p["a"],
                                     p["a"]}) == 3,
                            "not 90, where the line's-share slip equals the arc "
                            "itself, and the three taps differ"),
    },
    "insc": {  # arc a -> the inscribed angle a/2 (NO inscribed= figure: giveaway)
        "ans": lambda p: p["a"] // 2,
        "spoken": lambda p: (f"An arc of a circle measures {p['a']} degrees. An "
                             f"inscribed angle on the rim opens onto that arc. "
                             f"How big is the inscribed angle?"),
        # [[circle inscribed=]] is BANNED here: the renderer labels the vertex
        # angle at half the arc -- exactly this ask's answer, printed. Plain
        # circle plus the computation instead.
        "board": _insc_board,         # (tj) the plain circle, captioned (no inscribed= -- giveaway)
        "worked": _insc_worked,       # (tj) the angle on the rim, labelled
        "praise": lambda p: (f"From the rim the arc looks half: {p['a']} divided "
                             f"by 2 equals {p['a'] // 2} degrees."),
        "key": lambda p: p["a"],
        # The errors: treating middle and rim as twins (the arc copied), and
        # doubling in the wrong direction.
        "choices": lambda p: [p["a"] // 2, p["a"], 2 * p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (p["a"] % 2 == 0 and 30 <= p["a"] <= 160
                            and len({p["a"] // 2, p["a"], 2 * p["a"]}) == 3,
                            "an even arc so the inscribed angle is whole, and "
                            "the three taps differ"),
    },
    "iarc": {  # inscribed angle a -> its arc 2a (the figure IS legal here)
        "ans": lambda p: 2 * p["a"],
        "spoken": lambda p: (f"An inscribed angle on a circle's rim measures "
                             f"{p['a']} degrees. How many degrees is the arc it "
                             f"opens onto?"),
        # inscribed="2a" labels the vertex as a -- the GIVEN. The arc's measure
        # is never printed by the renderer, so the figure teaches without telling.
        "board": _iarc_board,         # (tj) the angle on the rim, captioned
        "worked": _iarc_worked,       # (tj) the arc named
        "praise": lambda p: (f"From angle to arc you double: 2 times {p['a']} "
                             f"equals {2 * p['a']} degrees."),
        "key": lambda p: p["a"],
        # The errors: the angle copied, and halving out of habit -- yesterday's
        # rule aimed the wrong direction.
        "choices": lambda p: [2 * p["a"], p["a"], p["a"] // 2],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (p["a"] % 2 == 0 and 10 <= p["a"] <= 80
                            and len({2 * p["a"], p["a"], p["a"] // 2}) == 3,
                            "an even angle so the wrong-way halving is a whole "
                            "number, and the three taps differ"),
    },
    "alen": {  # arc length: central angle a divides 360 evenly; rim length b
        "ans": lambda p: p["b"] * p["a"] // 360,
        "spoken": lambda p: (f"The distance around a whole circle is {p['b']}. An "
                             f"arc of that circle sits under a central angle of "
                             f"{p['a']} degrees. How long is the arc?"),
        "board": _alen_board,         # (tj) the equal parts, one shaded, captioned
        "worked": _alen_worked,       # (tj) the part measured
        "praise": lambda p: (f"{p['a']} degrees is one of {360 // p['a']} equal "
                             f"parts of the turn, so the arc is {p['b']} divided "
                             f"by {360 // p['a']} — {p['b'] * p['a'] // 360}."),
        "key": lambda p: p["b"] * p["a"] // 360,
        # The errors: degrees answered as LENGTH, and half-the-circle out of
        # habit regardless of the angle.
        "choices": lambda p: [p["b"] * p["a"] // 360, p["a"], p["b"] // 2],
        "check": lambda p: (p["a"] in (30, 40, 45, 60, 72, 90, 120)
                            and p["b"] % (360 // p["a"]) == 0
                            and p["b"] % 2 == 0 and 4 <= p["b"] <= 96
                            and len({p["b"] * p["a"] // 360, p["a"],
                                     p["b"] // 2}) == 3,
                            "the angle divides 360 into at most 12 equal parts "
                            "(the pie renderer's cap), the rim length shares "
                            "evenly, and the three taps differ"),
    },

    # ---- GEOMETRY UNIT 7 (build lf) -- COORDINATE GEOMETRY --------------------
    # Geometry moves onto the grid for good: lengths along a grid line (the
    # fencepost trap), the straight distance as U5's Pythagoras under a slant
    # (the taxicab walk as the standing wrong tap), U1's midpoint grown into two
    # dimensions, and the rectangle's fourth corner. The wrong-coordinate error
    # -- answering an x question with a y -- runs through the whole unit, just as
    # it ran through U2.
    "vseg": {  # vertical segment (a,b)-(a,c): length c - b, never the dot count
        "ans": lambda p: p["c"] - p["b"],
        "spoken": lambda p: (f"Two points sit at ({p['a']}, {p['b']}) and "
                             f"({p['a']}, {p['c']}). How long is the segment "
                             f"between them?"),
        "board": _vseg_board,         # (tk) the two points, captioned
        "worked": _vseg_worked,       # (tk) the steps counted
        "praise": lambda p: (f"From {p['b']} up to {p['c']} is "
                             f"{p['c'] - p['b']} steps — count steps, never "
                             f"dots."),
        "key": lambda p: p["c"] - p["b"],
        # The errors: the FENCEPOST count (dots instead of steps, one too many),
        # and the top height copied.
        "choices": lambda p: [p["c"] - p["b"], p["c"] - p["b"] + 1, p["c"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["c"]) in sp),
        "check": lambda p: (1 <= p["a"] <= 9 and 2 <= p["b"] < p["c"] <= 9
                            and len({p["c"] - p["b"], p["c"] - p["b"] + 1,
                                     p["c"]}) == 3,
                            "the lower point sits at 2 or higher (at 1 the "
                            "fencepost tap collides with the top), and the "
                            "three taps differ"),
    },
    "dist": {  # straight distance: (a,b) to (a+3c, b+4c) -- a 3-4-5 under a slant
        "ans": lambda p: 5 * p["c"],
        "spoken": lambda p: (f"How far is it straight from ({p['a']}, {p['b']}) "
                             f"to ({p['a'] + 3 * p['c']}, "
                             f"{p['b'] + 4 * p['c']})?"),
        "board": _dist_board,         # (tk) the two points, the across and up named
        "worked": _dist_worked,       # (tk) the right triangle under the slant
        "praise": lambda p: (f"Across {3 * p['c']} and up {4 * p['c']}: "
                             f"{9 * p['c'] * p['c']} plus "
                             f"{16 * p['c'] * p['c']} is "
                             f"{25 * p['c'] * p['c']}, and {5 * p['c']} times "
                             f"{5 * p['c']} squares back to it — the straight "
                             f"distance is {5 * p['c']}."),
        "key": lambda p: 5 * p["c"],
        # The errors: the TAXICAB walk (across plus up -- walking the grid
        # instead of cutting straight), and the up alone.
        "choices": lambda p: [5 * p["c"], 7 * p["c"], 4 * p["c"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["a"] + 3 * p["c"]) in sp
                                 and str(p["b"] + 4 * p["c"]) in sp),
        "check": lambda p: (1 <= p["c"] <= 3 and 1 <= p["a"] and 1 <= p["b"]
                            and p["a"] + 3 * p["c"] <= 13
                            and p["b"] + 4 * p["c"] <= 13
                            and len({5 * p["c"], 7 * p["c"],
                                     4 * p["c"]}) == 3,
                            "the slant fits the grid window, and the three taps "
                            "differ"),
    },
    "mid2": {  # midpoint on the grid: (a,b) to (c,b+4), asked for the x
        "ans": lambda p: (p["a"] + p["c"]) // 2,
        "spoken": lambda p: (f"A line runs from ({p['a']}, {p['b']}) up to "
                             f"({p['c']}, {p['b'] + 4}). What is the x "
                             f"coordinate of its midpoint?"),
        "board": _mid2_board,         # (tk) the two ends, captioned
        "worked": _mid2_worked,       # (tk) the midpoint marked
        "praise": lambda p: (f"The x's are {p['a']} and {p['c']}: put together "
                             f"{p['a'] + p['c']}, shared by two is "
                             f"{(p['a'] + p['c']) // 2}."),
        "key": lambda p: (p["a"] + p["c"]) // 2,
        # The errors: the midpoint's Y handed back for an x (the grid's oldest
        # mix-up, U2's wrong-coordinate again), and the RUN -- a length, not a
        # place.
        "choices": lambda p: [(p["a"] + p["c"]) // 2, p["b"] + 2,
                              p["c"] - p["a"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["c"]) in sp
                                 and str(p["b"] + 4) in sp),
        "check": lambda p: ((p["a"] + p["c"]) % 2 == 0
                            and 1 <= p["a"] < p["c"] <= 13
                            and 1 <= p["b"] <= 9
                            and len({(p["a"] + p["c"]) // 2, p["b"] + 2,
                                     p["c"] - p["a"]}) == 3,
                            "the midpoint's x is whole, and it differs from the "
                            "midpoint's y and from the run"),
    },
    "corn": {  # rectangle corners (a,b), (c,b), (a,b+3) -- the fourth's x
        "ans": lambda p: p["c"],
        "spoken": lambda p: (f"Three corners of a rectangle sit at ({p['a']}, "
                             f"{p['b']}), ({p['c']}, {p['b']}), and ({p['a']}, "
                             f"{p['b'] + 3}). What is the x coordinate of the "
                             f"fourth corner?"),
        # The fourth point is NEVER drawn -- the child closes the box.
        "board": _corn_board,         # (tk) three corners, captioned (the fourth never drawn)
        "worked": _corn_worked,       # (tk) the box closed
        "praise": lambda p: (f"The fourth corner sits straight above "
                             f"({p['c']}, {p['b']}), so its x is {p['c']} — the "
                             f"corner is ({p['c']}, {p['b'] + 3})."),
        "key": lambda p: p["c"],
        # The errors: the x of the DIAGONAL corner (grabbed from the wrong
        # corner), and a y answered for an x -- the unit's running mix-up.
        "choices": lambda p: [p["c"], p["a"], p["b"] + 3],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["c"]) in sp
                                 and str(p["b"] + 3) in sp),
        "check": lambda p: (1 <= p["a"] < p["c"] <= 12 and 1 <= p["b"] <= 9
                            and p["c"] != p["b"] + 3 and p["a"] != p["b"] + 3
                            and len({p["c"], p["a"], p["b"] + 3}) == 3,
                            "the fourth corner's x differs from the diagonal "
                            "corner's x and from its own y"),
    },

    # ---- GEOMETRY UNIT 8 (build lg) -- AREA, SURFACE AREA & VOLUME ------------
    # Past Basic U9's rectangle counting and pre-u8's triangle: the height that
    # is NOT the slant, composite floors, the cube's six faces, and the capstone
    # -- U4's scaling story finished: length pays the factor once, area twice,
    # VOLUME THREE TIMES. No new renderer needed; steps carry these boards (there
    # is no parallelogram/L-shape figure -- checked the shelf first).
    "para": {  # parallelogram: area = base x height, and the slant is a decoy
        "ans": lambda p: p["a"] * p["b"],
        # Givens named plainly, no "straight up" re-gloss (kw's scaffold rule) --
        # and the board states the FORMULA, never the picked numbers: choosing
        # the height over the slant IS this lesson's skill, so "a × b = ?" on
        # the board would do the whole job for the child.
        "spoken": lambda p: (f"A parallelogram leans: its base is {p['a']}, its "
                             f"slanted side is {p['c']}, and its height is "
                             f"{p['b']}. What is its area?"),
        "board": _para_board,         # (tk) the parallelogram with its true height drawn
        "worked": _para_worked,       # (tk) pushed straight into a rectangle
        "praise": lambda p: (f"Base times height: {p['a']} times {p['b']} equals "
                             f"{p['a'] * p['b']} — the slanted {p['c']} was never "
                             f"how tall it stood."),
        "key": lambda p: p["a"] * p["b"],
        # The errors: grabbing the SLANT as the height (the classic), and the
        # perimeter reflex.
        "choices": lambda p: [p["a"] * p["b"], p["a"] * p["c"],
                              2 * (p["a"] + p["c"])],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["c"]) in sp),
        "check": lambda p: (3 <= p["a"] <= 12 and 2 <= p["b"] <= 9
                            and p["b"] < p["c"] <= 12
                            and len({p["a"] * p["b"], p["a"] * p["c"],
                                     2 * (p["a"] + p["c"])}) == 3,
                            "the slant is longer than the height (leaning always "
                            "wastes length), and the three taps differ"),
    },
    "lshp": {  # L-shaped floor: rooms a-by-b and c-by-b -- areas add, lengths don't
        "ans": lambda p: p["b"] * (p["a"] + p["c"]),
        "spoken": lambda p: (f"A floor is made of two rectangles: one {p['a']} "
                             f"long and {p['b']} wide, and one {p['c']} long and "
                             f"{p['b']} wide. What is the floor's area in all?"),
        "board": _lshp_board,         # (tk) the two rooms, captioned
        "worked": _lshp_worked,       # (tk) each room measured
        "praise": lambda p: (f"Cut, measure, put together: {p['a'] * p['b']} plus "
                             f"{p['c'] * p['b']} equals "
                             f"{p['b'] * (p['a'] + p['c'])}."),
        "key": lambda p: p["b"] * (p["a"] + p["c"]),
        # The errors: stopping after ONE room, and adding the lengths -- lengths
        # added give edges, never area.
        "choices": lambda p: [p["b"] * (p["a"] + p["c"]), p["a"] * p["b"],
                              p["a"] + p["b"] + p["c"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["c"]) in sp),
        "check": lambda p: (3 <= p["a"] <= 10 and 2 <= p["b"] <= 6
                            and 2 <= p["c"] <= 10
                            and len({p["b"] * (p["a"] + p["c"]),
                                     p["a"] * p["b"],
                                     p["a"] + p["b"] + p["c"]}) == 3,
                            "the whole floor, the one-room stop and the "
                            "added-lengths slip are three different numbers"),
    },
    "surf": {  # cube surface area from ONE face's area: six faces, always six
        "ans": lambda p: 6 * p["a"],
        "spoken": lambda p: (f"One face of a cube has an area of {p['a']} square "
                             f"units. What is the cube's surface area?"),
        "board": _surf_board,         # (tk) the cube, captioned
        "worked": _surf_worked,       # (tk) the six faces as bars
        "praise": lambda p: (f"Six faces, all alike: 6 times {p['a']} equals "
                             f"{6 * p['a']} square units."),
        "key": lambda p: p["a"],
        # The errors: counting only the four WALLS (the open-box slip), and the
        # one face copied.
        "choices": lambda p: [6 * p["a"], 4 * p["a"], p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (2 <= p["a"] <= 25
                            and len({6 * p["a"], 4 * p["a"], p["a"]}) == 3,
                            "three different taps (automatic for a positive "
                            "face)"),
    },
    "svol": {  # volume under scaling: the k-cubed capstone of U4's k-squared
        "ans": lambda p: p["a"] * p["b"] ** 3,
        "spoken": lambda p: (f"A box holds {p['a']} cubic units. Every edge is "
                             f"enlarged by a scale factor of {p['b']}. How many "
                             f"cubic units does the new box hold?"),
        "board": _svol_board,         # (tk) the box, captioned
        "worked": _svol_worked,       # (tk) every edge timesed
        "praise": lambda p: (f"Length pays the factor once, area twice — volume "
                             f"pays it three times: {p['a']} times "
                             f"{p['b'] ** 3} equals {p['a'] * p['b'] ** 3} cubic "
                             f"units."),
        "key": lambda p: p["a"] * p["b"] ** 3,
        # The errors are the course's own history: the LENGTH habit (times k
        # once) and the AREA habit from U4 (times k twice).
        "choices": lambda p: [p["a"] * p["b"] ** 3, p["a"] * p["b"] ** 2,
                              p["a"] * p["b"]],
        "check": lambda p: (2 <= p["b"] <= 3 and 2 <= p["a"] <= 10
                            and len({p["a"] * p["b"] ** 3,
                                     p["a"] * p["b"] ** 2,
                                     p["a"] * p["b"]}) == 3,
                            "the three scaling habits land on three different "
                            "numbers (automatic for factor 2 or more)"),
    },

    # ---- GEOMETRY UNIT 9 (build lg) -- PROBABILITY -- GEOMETRY FINISHES -------
    # Chance in CHILD numbers: counts out of a whole, never fractions. The whole
    # bag is the out-of (odds-vs-probability is the standing wrong tap), the
    # complement shares the whole, choices TIMES up (not add), and the closer is
    # the two-way table. RENDERER RULINGS (read first, as always): [[tree]]
    # prints every leaf product and [[areamodel]] prints its expanded total --
    # both are giveaway machines on asks, so tree stays unused and areamodel is
    # teach-only. [[twoway]] auto-computes row/column/grand totals, so the table
    # lesson asks for a CELL -- a reading skill, like cong's matching side.
    "poft": {  # the chance of red is a out of -- the WHOLE bag, a + b
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"A bag holds {p['a']} red marbles and {p['b']} "
                             f"blue marbles. One marble is picked without "
                             f"looking. The chance of red is {p['a']} out of "
                             f"how many?"),
        "board": _poft_board,         # (tk) the two colours as bars, captioned
        "worked": _poft_worked,       # (tk) the whole bag as a pie
        "praise": lambda p: (f"The pick lands on one of ALL the marbles: "
                             f"{p['a']} plus {p['b']} equals "
                             f"{p['a'] + p['b']}, so red is {p['a']} out of "
                             f"{p['a'] + p['b']}."),
        "key": lambda p: p["a"] + p["b"],
        # The errors: "out of the blues" (odds against, not chance out of all --
        # the lesson's whole point), and the reds copied.
        "choices": lambda p: [p["a"] + p["b"], p["b"], p["a"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and p["a"] != p["b"]
                            and len({p["a"] + p["b"], p["b"],
                                     p["a"]}) == 3,
                            "the two colors differ in count, so the odds slip "
                            "and the copy are visible mistakes"),
    },
    "notp": {  # the complement: chance a out of b -> no-chance is b - a out of b
        "ans": lambda p: p["b"] - p["a"],
        "spoken": lambda p: (f"The chance of rain today is {p['a']} out of "
                             f"{p['b']}. What is the chance of no rain, out of "
                             f"{p['b']}?"),
        "board": _notp_board,         # (tk) rain against all the chances
        "worked": _notp_worked,       # (tk) rain beside no rain
        "praise": lambda p: (f"Every chance belongs to somebody: {p['b']} take "
                             f"away {p['a']} leaves {p['b'] - p['a']} out of "
                             f"{p['b']} for no rain — and {p['a']} plus "
                             f"{p['b'] - p['a']} puts the whole {p['b']} back."),
        "key": lambda p: p["b"] - p["a"],
        # The errors: the same chance copied (the complement ignored), and the
        # whole -- as if no-rain were certain.
        "choices": lambda p: [p["b"] - p["a"], p["a"], p["b"]],
        "check": lambda p: (2 <= p["a"] < p["b"] <= 20 and p["b"] != 2 * p["a"]
                            and len({p["b"] - p["a"], p["a"],
                                     p["b"]}) == 3,
                            "not the even split, where the other chance equals "
                            "the chance itself and the copy-tap is right"),
    },
    "outc": {  # the counting principle: choices TIMES up, never add
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: (f"You own {p['a']} shirts and {p['b']} hats, all "
                             f"different. How many different shirt-and-hat "
                             f"outfits can you choose?"),
        # [[areamodel]] would draw the outfit grid beautifully -- and prints its
        # expanded product at the bottom, the answer. Teach boards use it; ask
        # boards get steps.
        "board": _outc_board,         # (tk) the outfit grid as an array, captioned
        "worked": _outc_worked,       # (tk) the boxes counted
        "praise": lambda p: (f"Choices times up: {p['a']} times {p['b']} equals "
                             f"{p['a'] * p['b']} different outfits."),
        "key": lambda p: p["a"] * p["b"],
        # The errors: ADDING the choices (the canonical slip), and stopping at
        # the shirts.
        "choices": lambda p: [p["a"] * p["b"], p["a"] + p["b"], p["a"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and len({p["a"] * p["b"], p["a"] + p["b"],
                                     p["a"]}) == 3,
                            "the product, the sum and the first count are three "
                            "different numbers (excludes the 2-and-2 case)"),
    },
    "twop": {  # the two-way table: read the cell where the right row meets the
        # right column. Cells: boys soccer a, boys art b, girls soccer c, girls
        # art c + 2 (derived, so _problem_key still covers the whole problem).
        "ans": lambda p: p["c"] + 2,
        # The numbers live ON THE TABLE, not in the voice -- the cnt precedent:
        # speaks is always satisfied, because reading the board IS the skill.
        "spoken": lambda p: ("The table shows a class and the sport each child "
                             "chose. How many girls chose art?"),
        "board": _twop_board,         # (tk) the table, captioned
        "worked": _twop_worked,       # (tk) the crossing named
        "praise": lambda p: (f"Girls row, art column — the box where they cross "
                             f"holds {p['c'] + 2}."),
        "key": lambda p: p["c"],
        # The errors: the next-door boxes -- right column wrong row (boys art),
        # and right row wrong column (girls soccer).
        "choices": lambda p: [p["c"] + 2, p["b"], p["c"]],
        "speaks": lambda p, sp: True,
        "check": lambda p: (2 <= p["a"] <= 12 and 2 <= p["b"] <= 12
                            and 2 <= p["c"] <= 12 and p["b"] != p["c"]
                            and p["c"] + 2 != p["b"]
                            and len({p["c"] + 2, p["b"], p["c"]}) == 3,
                            "the asked cell and its two next-door boxes hold "
                            "three different numbers"),
    },

    # ---- ALGEBRA II UNIT 1 (build lh) -- FOUNDATIONS & SYSTEMS ----------------
    # The seventh course opens by SHARPENING TOOLS: absolute value as distance
    # (read both directions -- the value, then counting inside it), and systems
    # grown past Algebra I's U5: elimination where a shared piece cancels and one
    # more divide remains, then THREE unknowns weighed two at a time.
    "absv": {  # |a - b| with a < b: distance is never negative
        "ans": lambda p: p["b"] - p["a"],
        "spoken": lambda p: (f"What is the absolute value of {p['a']} take away "
                             f"{p['b']}?"),
        "board": _absv_board,         # (tl) the two spots on the line, captioned
        "worked": _absv_worked,       # (tl) the steps between them hopped
        # Spoken negatives as WORDS (the pre-u3 convention) -- never print "-4".
        "praise": lambda p: (f"{p['a']} take away {p['b']} lands on negative "
                             f"{p['b'] - p['a']} — but the absolute value asks "
                             f"how FAR, and distance is never negative: "
                             f"{p['b'] - p['a']}."),
        "key": lambda p: p["b"] - p["a"],
        # The errors: keeping the minus (the whole lesson), and adding the two
        # positions instead of measuring between them.
        "choices": lambda p: [p["b"] - p["a"], p["a"] - p["b"],
                              p["a"] + p["b"]],
        "check": lambda p: (2 <= p["a"] < p["b"] <= 20
                            and len({p["b"] - p["a"], p["a"] - p["b"],
                                     p["a"] + p["b"]}) == 3,
                            "two different spots on the line (automatic once "
                            "a is below b)"),
    },
    "absc": {  # how many INTEGERS have |x| < a: the zero counts too (uq: "whole numbers" was wrong)
        "ans": lambda p: 2 * p["a"] - 1,
        "spoken": lambda p: (f"How many integers x have an absolute value less than "
                             f"{p['a']}? Count every dot inside the fence."),
        "board": _absc_board,         # (tl) the ends on the line, captioned
        "worked": _absc_worked,       # (tl) negatives, zero, positives as bars
        # "{n} on each side" stays grammatical at n = 1 ("1 negatives" would
        # not -- caught reading ask1's praise aloud).
        "praise": lambda p: (f"From negative {p['a'] - 1} up to "
                             f"{p['a'] - 1}: {p['a'] - 1} on each side, and "
                             f"zero in the middle — {2 * p['a'] - 1} integers."),
        "key": lambda p: p["a"],
        # The errors: forgetting ZERO (one short of everything), and counting
        # the positive side only.
        "choices": lambda p: [2 * p["a"] - 1, 2 * p["a"] - 2, p["a"] - 1],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (2 <= p["a"] <= 15
                            and len({2 * p["a"] - 1, 2 * p["a"] - 2,
                                     p["a"] - 1}) == 3,
                            "a distance of at least 2, so all three taps "
                            "differ"),
    },
    "el2": {   # 3 apples + 2 bananas = a; 1 apple + 2 bananas = b -> one apple
        "ans": lambda p: (p["a"] - p["b"]) // 2,
        "spoken": lambda p: (f"Three apples and two bananas cost {p['a']} "
                             f"cents. One apple and the same two bananas cost "
                             f"{p['b']} cents. What does one apple cost, in "
                             f"cents?"),
        # The board names the cancellation but computes NOTHING -- the child
        # subtracts the trips AND shares between the two apples (el2's whole
        # step past alg1's elim, where one subtraction finished the job).
        "board": _el2_board,          # (tl) the two trips as tapes, captioned
        "worked": _el2_worked,        # (tl) the pair of apples left standing
        "praise": lambda p: (f"Take the small trip away from the big one and "
                             f"the bananas vanish: 2 apples cost "
                             f"{p['a'] - p['b']}, so one apple is "
                             f"{(p['a'] - p['b']) // 2} cents."),
        "key": lambda p: (p["a"] - p["b"]) // 2,
        # The errors: stopping at the PAIR of apples, and averaging the two
        # trips -- the wrong operation grabbed at the start.
        "choices": lambda p: [(p["a"] - p["b"]) // 2, p["a"] - p["b"],
                              (p["a"] + p["b"]) // 2],
        "check": lambda p: (4 <= p["b"] < p["a"] <= 40
                            and (p["a"] - p["b"]) % 2 == 0
                            and (p["a"] - p["b"]) // 2 >= 2
                            and (p["a"] - p["b"]) // 2 < p["b"]
                            and p["a"] != 3 * p["b"]
                            and len({(p["a"] - p["b"]) // 2,
                                     p["a"] - p["b"],
                                     (p["a"] + p["b"]) // 2}) == 3,
                            "one apple costs a whole positive amount, the "
                            "bananas cost something too, and the three taps "
                            "differ"),
    },
    "sys3": {  # x+y=a, y+z=b, x+z=c: everyone is in exactly two clues
        "ans": lambda p: (p["a"] + p["b"] + p["c"]) // 2,
        "spoken": lambda p: (f"Three friends step on a scale two at a time: "
                             f"the first pair weighs {p['a']}, the second pair "
                             f"{p['b']}, and the third pair {p['c']}. Put "
                             f"together, how much do all three weigh?"),
        "board": _sys3_board,         # (tl) the three clues as bars, captioned
        "worked": _sys3_worked,       # (tl) all three clues beside everyone once
        "praise": lambda p: (f"Put the three clues together: "
                             f"{p['a'] + p['b'] + p['c']} — but every friend "
                             f"was weighed twice, so all three together weigh "
                             f"{(p['a'] + p['b'] + p['c']) // 2}."),
        "key": lambda p: (p["a"] + p["b"] + p["c"]) // 2,
        # The errors: forgetting everyone was counted TWICE (no halving), and
        # averaging the three weighings.
        "choices": lambda p: [(p["a"] + p["b"] + p["c"]) // 2,
                              p["a"] + p["b"] + p["c"],
                              (p["a"] + p["b"] + p["c"]) // 3],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["c"]) in sp),
        # Each friend's own weight must be a real positive number -- the three
        # pair-sums cannot be arbitrary. Divisibility by 6 keeps BOTH wrong
        # taps whole (the un-halved sum and the averaged third).
        "check": lambda p: ((p["a"] + p["b"] + p["c"]) % 6 == 0
                            and p["a"] - p["b"] + p["c"] > 0
                            and p["a"] + p["b"] - p["c"] > 0
                            and -p["a"] + p["b"] + p["c"] > 0
                            and p["a"] <= 40 and p["b"] <= 40
                            and p["c"] <= 40
                            and len({(p["a"] + p["b"] + p["c"]) // 2,
                                     p["a"] + p["b"] + p["c"],
                                     (p["a"] + p["b"] + p["c"]) // 3}) == 3,
                            "three real friends with positive weights, and "
                            "the three taps land on three different numbers"),
    },

    # ---- ALGEBRA II UNIT 2 (build lh) -- QUADRATIC FUNCTIONS & COMPLEX NUMBERS
    # THE QUADRATIC TELLS ITS SECRETS WITHOUT BEING SOLVED: vertex form says
    # WHERE it turns (the sign points opposite -- alg1's vtx asked how LOW, this
    # asks WHERE), factored form says what the two answers share, the
    # discriminant says HOW MANY crossings -- and when the test number falls
    # below zero, a new number arrives to catch the answers: i.
    "vtx2": {  # y = (x-a)^2 + b: at which x does it turn? The sign points opposite.
        "ans": lambda p: p["a"],
        "spoken": lambda p: (f"y equals: x take away {p['a']}, squared, plus "
                             f"{p['b']}. At which x does this curve reach its "
                             f"lowest point?"),
        "board": _vtx2_board,         # (tl) the curve, captioned
        "worked": _vtx2_worked,       # (tl) the vertex marked
        "praise": lambda p: (f"x take away {p['a']} is zero exactly at x equals "
                             f"{p['a']} — and there the square bottoms out. The "
                             f"minus points OPPOSITE: take away {p['a']} means "
                             f"the turn sits at positive {p['a']}."),
        "key": lambda p: p["a"],
        # The errors: reading (x - a) as "at negative a" (the sign flip -- the
        # classic), and answering with the OTHER number -- the height, alg1-vtx's
        # answer to a different question.
        "choices": lambda p: [p["a"], -p["a"], p["b"]],
        "check": lambda p: (2 <= p["a"] <= 12 and 1 <= p["b"] <= 12
                            and p["a"] != p["b"]
                            and len({p["a"], -p["a"], p["b"]}) == 3,
                            "the x of the turn and the height are different "
                            "numbers, so the wrong-question tap is visible"),
    },
    "rsum": {  # (x-a)(x-b) = 0: BOTH answers count -- what do they total? (No:
        # "put together". The wrong taps are Vieta's other number and stopping
        # at one root.)
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"x take away {p['a']}, times x take away "
                             f"{p['b']}, equals zero. There are two answers. "
                             f"Put together, what do the two answers equal?"),
        # The graph SHOWS the two crossings -- reading a picture is allowed;
        # adding its two crossings is still the child's job.
        "board": _rsum_board,         # (tl) the curve, captioned
        "worked": _rsum_worked,       # (tl) both crossings marked
        "praise": lambda p: (f"The answers are x equals {p['a']} and x equals "
                             f"{p['b']} — put together, {p['a'] + p['b']}."),
        "key": lambda p: p["a"] + p["b"],
        # The errors: the PRODUCT (the other number the roots secretly share --
        # met properly later as Vieta), and stopping at one answer.
        "choices": lambda p: [p["a"] + p["b"], p["a"] * p["b"], p["a"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and p["a"] != p["b"]
                            and len({p["a"] + p["b"], p["a"] * p["b"],
                                     p["a"]}) == 3,
                            "two different roots whose sum, product and first "
                            "value are three different numbers"),
    },
    "disc": {  # x^2 + ax + b: the test number a^2 - 4b counts the crossings
        "ans": lambda p: (2 if p["a"] * p["a"] > 4 * p["b"]
                          else 1 if p["a"] * p["a"] == 4 * p["b"] else 0),
        "spoken": lambda p: (f"y equals x squared plus {p['a']} x plus "
                             f"{p['b']}. How many times does this curve meet "
                             f"the x line — 2, 1, or 0?"),
        # The board carries the test number's FORMULA and the fact that its
        # sign decides -- computing it and judging the sign stay with the child.
        "board": lambda p: (f'[[step eq="test number: {p["a"]}² − '
                            f'4 · {p["b"]}"]]'
                            f'[[step eq="its SIGN answers the question"]]'),
        "worked": _disc_worked,       # (tl) the two numbers as bars, then the curve (a picture on the ask would count the crossings)
        # Praise never PRINTS a negative test number -- it speaks the judgment.
        "praise": lambda p: (f"{p['a']} squared is {p['a'] * p['a']}, and 4 "
                             f"times {p['b']} is {4 * p['b']}. "
                             + ("The test number is positive — the curve cuts "
                                "the x line twice."
                                if p["a"] * p["a"] > 4 * p["b"] else
                                "The test number is exactly zero — the curve "
                                "touches the x line once."
                                if p["a"] * p["a"] == 4 * p["b"] else
                                "The test number falls below zero — the curve "
                                "never comes down to the x line: zero "
                                "crossings.")),
        "key": lambda p: p["a"],
        # All three counts are always on offer -- the judgment IS the lesson.
        "choices": lambda p: [2, 1, 0],
        "check": lambda p: (2 <= p["a"] <= 9 and 1 <= p["b"] <= 20,
                            "small clean coefficients (the answer set 2/1/0 is "
                            "distinct by construction)"),
    },
    "imag": {  # x^2 = -a (a a perfect square): a new number catches the answer
        "ans": lambda p: round(p["a"] ** 0.5),
        "spoken": lambda p: (f"x squared equals negative {p['a']}. Written "
                             f"with i, x is a number times i. What is that "
                             f"number?"),
        "board": _imag_board,         # (tl) the question, i's one job, and the blank on its own line (rule 44)
        "worked": _imag_worked,       # (tl) the square as an array, past 10 a rectangle (its side is the answer -- walk-back only)
        "praise": lambda p: (f"The i carries the minus: {round(p['a'] ** 0.5)} "
                             f"i times {round(p['a'] ** 0.5)} i equals "
                             f"{p['a']} times i squared — negative {p['a']}. "
                             f"So x is {round(p['a'] ** 0.5)} i."),
        "key": lambda p: round(p["a"] ** 0.5),
        # The errors: forgetting the ROOT entirely, and dragging the minus onto
        # the answer -- the minus lives inside i squared, not in front.
        "choices": lambda p: [round(p["a"] ** 0.5), p["a"],
                              -round(p["a"] ** 0.5)],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        # Problems run k = 4..15; the canonical x² = −9 belongs to the TEACH
        # beats (collision rule: teach numbers never reappear as problems).
        "check": lambda p: (round(p["a"] ** 0.5) ** 2 == p["a"]
                            and 4 <= round(p["a"] ** 0.5) <= 15
                            and len({round(p["a"] ** 0.5), p["a"],
                                     -round(p["a"] ** 0.5)}) == 3,
                            "a perfect square with a whole root between 4 "
                            "and 15"),
    },

    # ---- ALGEBRA II UNIT 3 (build li) -- POLYNOMIAL FUNCTIONS -----------------
    # What the DEGREE promises: it adds under times (kz's power rule, grown up),
    # it caps the wiggles at one fewer, a cubic's three roots answer together
    # (rsum's ladder extended), and evaluating means reading x-cubed as a CUBE --
    # the 3-times-x misconception from pre-u1/kz, returned taller.
    "pdeg": {  # degree a polynomial times degree b polynomial -> degree a + b
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"One polynomial has degree {p['a']}; another has "
                             f"degree {p['b']}. Multiply the two together. "
                             f"What is the degree of the answer?"),
        "board": _pdeg_board,         # (tl) the two piles as bars, captioned
        "worked": _pdeg_worked,       # (tl) the piles joined
        "praise": lambda p: (f"The top powers join: x to the {p['a']} times x "
                             f"to the {p['b']} is x to the "
                             f"{p['a'] + p['b']} — degree {p['a'] + p['b']}."),
        "key": lambda p: p["a"] + p["b"],
        # The errors: MULTIPLYING the degrees, and keeping the bigger one --
        # which is ADDITION's rule for polynomials, used on the wrong operation.
        "choices": lambda p: [p["a"] + p["b"], p["a"] * p["b"],
                              max(p["a"], p["b"])],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and len({p["a"] + p["b"], p["a"] * p["b"],
                                     max(p["a"], p["b"])}) == 3,
                            "the sum, the product and the bigger degree are "
                            "three different numbers (excludes 2-and-2)"),
    },
    "turnc": {  # a degree-a curve turns at most a - 1 times
        "ans": lambda p: p["a"] - 1,
        "spoken": lambda p: (f"y is a polynomial of degree {p['a']}. At most, "
                             f"how many times can its curve turn?"),
        "board": lambda p: (f'[[step eq="degree {p["a"]} · at most ? '
                            f'turns"]]'),
        "worked": _turnc_worked,      # (tl) the degree beside the turns (a curve of degree a would show its turns)
        "praise": lambda p: (f"A degree {p['a']} polynomial turns at most "
                             f"{p['a'] - 1} times — always one fewer than its "
                             f"degree."),
        "key": lambda p: p["a"],
        # The errors: the degree copied, and the parabola habit -- "curves turn
        # once".
        "choices": lambda p: [p["a"] - 1, p["a"], 1],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (3 <= p["a"] <= 16
                            and len({p["a"] - 1, p["a"], 1}) == 3,
                            "degree 3 or more, so one-fewer and the parabola "
                            "habit are different taps"),
    },
    "rsum3": {  # (x-a)(x-b)(x-c) = 0: all three answers, put together
        "ans": lambda p: p["a"] + p["b"] + p["c"],
        "spoken": lambda p: (f"x take away {p['a']}, times x take away "
                             f"{p['b']}, times x take away {p['c']}, equals "
                             f"zero. There are three answers. Put together, "
                             f"what do they equal?"),
        "board": _rsum3_board,        # (tl) the cubic, captioned
        "worked": _rsum3_worked,      # (tl) all three crossings marked
        "praise": lambda p: (f"The answers are {p['a']}, {p['b']} and "
                             f"{p['c']} — put together, "
                             f"{p['a'] + p['b'] + p['c']}."),
        "key": lambda p: p["a"] + p["b"] + p["c"],
        # The errors: the PRODUCT (the roots' other secret), and stopping after
        # two -- a cubic has three answers.
        "choices": lambda p: [p["a"] + p["b"] + p["c"],
                              p["a"] * p["b"] * p["c"], p["a"] + p["b"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["c"]) in sp),
        "check": lambda p: (1 <= p["a"] < p["b"] < p["c"] <= 7
                            and p["a"] + p["b"] + p["c"]
                            != p["a"] * p["b"] * p["c"]
                            and len({p["a"] + p["b"] + p["c"],
                                     p["a"] * p["b"] * p["c"],
                                     p["a"] + p["b"]}) == 3,
                            "three different roots whose sum is not their "
                            "product (1-2-3 is excluded)"),
    },
    "pval": {  # y = x^3 - a x + b at x = c: the cube read as a CUBE, sign kept
        "ans": lambda p: p["c"] ** 3 - p["a"] * p["c"] + p["b"],
        "spoken": lambda p: (f"y equals: x cubed, take away {p['a']} x, plus "
                             f"{p['b']}. What is y when x equals {p['c']}?"),
        "board": _pval_board,         # (tl) the machine with its door blank, captioned
        "worked": _pval_worked,       # (tl) the machine answered
        "praise": lambda p: (f"{p['c']} cubed is {p['c'] ** 3}; take away "
                             f"{p['a']} times {p['c']} — "
                             f"{p['a'] * p['c']} — leaves "
                             f"{p['c'] ** 3 - p['a'] * p['c']}; plus {p['b']} "
                             f"equals "
                             f"{p['c'] ** 3 - p['a'] * p['c'] + p['b']}."),
        "key": lambda p: p["c"] ** 3 - p["a"] * p["c"] + p["b"],
        # The errors: the minus dropped, and x-cubed read as 3-times-x -- the
        # pre-u1/kz exponent misconception, returned taller.
        "choices": lambda p: [p["c"] ** 3 - p["a"] * p["c"] + p["b"],
                              p["c"] ** 3 + p["a"] * p["c"] + p["b"],
                              3 * p["c"] - p["a"] * p["c"] + p["b"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["c"]) in sp),
        "check": lambda p: (2 <= p["c"] <= 4 and 1 <= p["a"] < p["c"] ** 2
                            and 1 <= p["b"] <= 10
                            and 3 * p["c"] - p["a"] * p["c"] + p["b"] >= 1
                            and len({p["c"] ** 3 - p["a"] * p["c"] + p["b"],
                                     p["c"] ** 3 + p["a"] * p["c"] + p["b"],
                                     3 * p["c"] - p["a"] * p["c"]
                                     + p["b"]}) == 3,
                            "the cube stays ahead of the take-away, the "
                            "3-times-x slip stays a positive tap, and the "
                            "three taps differ"),
    },

    # ---- ALGEBRA II UNIT 4 (build li) -- RATIONAL EXPRESSIONS & FUNCTIONS -----
    # DIVISION BECOMES A FUNCTION: y = a/x met and read backwards (the rdiv/rsol
    # pair), the one FORBIDDEN x (where the bottom dies -- with vtx2's sign flip
    # and the x=0 habit as the taps), and the far horizon -- (ax+b)/x hides a
    # survivor, and yesterday's answer (zero) is today's trap.
    "rdiv": {  # y = a / x at x = b: sharing shrinks
        "ans": lambda p: p["a"] // p["b"],
        "spoken": lambda p: (f"y equals {p['a']} divided by x. What is y when "
                             f"x equals {p['b']}?"),
        "board": _rdiv_board,         # (tm) the sharing curve, captioned; the divide on its own line
        "worked": _rdiv_worked,       # (tm) the point marked
        "praise": lambda p: (f"{p['a']} divided by {p['b']} equals "
                             f"{p['a'] // p['b']} — the bigger the x, the "
                             f"smaller the share."),
        "key": lambda p: p["a"],
        # The errors: the other operations wearing masks -- take away, and
        # times.
        "choices": lambda p: [p["a"] // p["b"], p["a"] - p["b"],
                              p["a"] * p["b"]],
        "check": lambda p: (2 <= p["b"] <= 9 and p["a"] % p["b"] == 0
                            and p["a"] // p["b"] >= 2 and p["a"] <= 36
                            and len({p["a"] // p["b"], p["a"] - p["b"],
                                     p["a"] * p["b"]}) == 3,
                            "a whole share of at least 2, and the divide, the "
                            "take-away and the times land on three different "
                            "numbers"),
    },
    "rsol": {  # a / x = b: which x was fed? Rebuild, then divide.
        "ans": lambda p: p["a"] // p["b"],
        "spoken": lambda p: (f"{p['a']} divided by x equals {p['b']}. What "
                             f"is x?"),
        "board": _rsol_board,         # (tm) the machine run backwards, its input blank
        "worked": _rsol_worked,       # (tm) the input found and checked
        "praise": lambda p: (f"x times {p['b']} must rebuild {p['a']}, so x "
                             f"is {p['a']} divided by {p['b']} — "
                             f"{p['a'] // p['b']}. Check: "
                             f"{p['a'] // p['b']} times {p['b']} equals "
                             f"{p['a']}."),
        "key": lambda p: p["a"],
        # The errors: grabbing TIMES as the undo (a times b), and take away.
        "choices": lambda p: [p["a"] // p["b"], p["a"] * p["b"],
                              p["a"] - p["b"]],
        "check": lambda p: (2 <= p["b"] <= 10 and p["a"] % p["b"] == 0
                            and p["a"] // p["b"] >= 2 and p["a"] <= 36
                            and len({p["a"] // p["b"], p["a"] * p["b"],
                                     p["a"] - p["b"]}) == 3,
                            "a whole answer of at least 2, and the three taps "
                            "differ"),
    },
    "excl": {  # y = b / (x - a): the one forbidden x is where the BOTTOM dies
        "ans": lambda p: p["a"],
        "spoken": lambda p: (f"y equals {p['b']} divided by: x take away "
                             f"{p['a']}. Which x is FORBIDDEN?"),
        # No graph here: the vertical asymptote would sit AT the answer, read
        # straight off the picture. The formula reasoning is the skill.
        "board": _excl_board,         # (tm) the jammed machine, captioned (no curve: the pole sits at the answer)
        "worked": _excl_worked,       # (tm) the curve flying off at the forbidden x
        "praise": lambda p: (f"x take away {p['a']} is zero exactly at x "
                             f"equals {p['a']} — and dividing by zero is the "
                             f"one thing mathematics never allows. Every "
                             f"other x is welcome."),
        "key": lambda p: p["a"],
        # The errors: the sign flip (vtx2's cousin, by design), and "zero is
        # always the danger" -- the y = a/x habit.
        "choices": lambda p: [p["a"], -p["a"], 0],
        "check": lambda p: (2 <= p["a"] <= 12 and 1 <= p["b"] <= 12
                            and len({p["a"], -p["a"], 0}) == 3,
                            "a nonzero shift, so the flip and the zero habit "
                            "are visible mistakes"),
    },
    "rasy": {  # y = (a x + b) / x: split it -- b/x dies, the survivor is a
        "ans": lambda p: p["a"],
        "spoken": lambda p: (f"y equals: {p['a']} x plus {p['b']}, all "
                             f"divided by x. As x grows huge, what number "
                             f"does y settle toward?"),
        # The board shows the UNSPLIT form -- splitting it is the skill (the
        # para/lg rule: never do the child's job on the board). The graph's
        # flattening is fair to read, like sys1's crossing.
        "board": _rasy_board,         # (tm) the curve, captioned
        "worked": _rasy_worked,       # (tm) the level line drawn
        "praise": lambda p: (f"Split it: {p['a']} plus {p['b']} divided by x. "
                             f"The {p['b']} share dies away as x grows; the "
                             f"{p['a']} stays — y settles toward {p['a']}."),
        "key": lambda p: p["a"],
        # The errors: ZERO -- the previous page's answer (plain b/x dies, but
        # today's function keeps a survivor) -- and the fading part's number.
        "choices": lambda p: [p["a"], 0, p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 1 <= p["b"] <= 9
                            and p["a"] != p["b"]
                            and len({p["a"], 0, p["b"]}) == 3,
                            "the survivor and the fading part differ, and "
                            "neither is zero"),
    },

    # ---- ALGEBRA II UNIT 5 (build lj) -- RADICALS & RATIONAL EXPONENTS --------
    # THE ROOT IS A POWER IN DISGUISE, AND NEVER A HALVING. Roots times under
    # one roof, the one-half power unmasked, the radical equation undone, and
    # estimation between the squares. The halving misconception is the unit's
    # standing wrong tap -- it appears in three of the four lessons.
    "rmul": {  # sqrt(a) * sqrt(b) = sqrt(ab), with ab a perfect square
        "ans": lambda p: round((p["a"] * p["b"]) ** 0.5),
        "spoken": lambda p: (f"The square root of {p['a']}, times the square "
                             f"root of {p['b']}. What single whole number is "
                             f"that?"),
        # RAW givens only (the para/rasy rule): combining under one roof is the
        # skill, so the board must not do it.
        "board": lambda p: (f'[[step eq="√{p["a"]} · √{p["b"]} = ?"]]'),
        "worked": _rmul_worked,       # (tm) the square the two roots make (walk-back only: its side is the answer)
        "praise": lambda p: (f"Under one roof: {p['a']} times {p['b']} is "
                             f"{p['a'] * p['b']}, and "
                             f"{round((p['a'] * p['b']) ** 0.5)} times itself "
                             f"equals {p['a'] * p['b']} — the answer is "
                             f"{round((p['a'] * p['b']) ** 0.5)}."),
        "key": lambda p: round((p["a"] * p["b"]) ** 0.5),
        # The errors: stopping at the product under the roof (forgot the
        # root), and ADDING under the roots -- the famous illegal move.
        "choices": lambda p: [round((p["a"] * p["b"]) ** 0.5),
                              p["a"] * p["b"], p["a"] + p["b"]],
        "check": lambda p: (2 <= p["a"] < p["b"] <= 54
                            and round((p["a"] * p["b"]) ** 0.5) ** 2
                            == p["a"] * p["b"]
                            and round(p["a"] ** 0.5) ** 2 != p["a"]
                            and round(p["b"] ** 0.5) ** 2 != p["b"]
                            and p["a"] * p["b"] <= 400
                            and len({round((p["a"] * p["b"]) ** 0.5),
                                     p["a"] * p["b"],
                                     p["a"] + p["b"]}) == 3,
                            "neither root is whole alone, but together they "
                            "square out exactly, and the three taps differ"),
    },
    "rpow": {  # a^(1/2), a = k^2 with k even: the fraction power unmasked
        "ans": lambda p: round(p["a"] ** 0.5),
        "spoken": lambda p: (f"What is {p['a']} to the one-half power?"),
        # RAW givens only: translating the fraction power into a root IS the
        # skill -- the board must not translate it.
        "board": lambda p: (f'[[step eq="{p["a"]} to the ½ power = ?"]]'),
        "worked": _rpow_worked,       # (tm) the root beside the halving trap, as bars
        "praise": lambda p: (f"A one-half power is a square root, never a "
                             f"halving: the root of {p['a']} is "
                             f"{round(p['a'] ** 0.5)}."),
        "key": lambda p: round(p["a"] ** 0.5),
        # The errors: HALF of a ("one-half power means half" -- the unit's
        # standing trap), and the power-did-nothing tap.
        "choices": lambda p: [round(p["a"] ** 0.5), p["a"] // 2, p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        # k is even so the halving tap is a whole number a child could really
        # reach; k = 2 is excluded (there the root equals the half).
        "check": lambda p: (round(p["a"] ** 0.5) ** 2 == p["a"]
                            and round(p["a"] ** 0.5) % 2 == 0
                            and 4 <= round(p["a"] ** 0.5) <= 26
                            and len({round(p["a"] ** 0.5), p["a"] // 2,
                                     p["a"]}) == 3,
                            "a perfect square with an even root of at least "
                            "4, so root and half are different whole taps"),
    },
    "rsq": {   # sqrt(x) = a -> x = a^2: the radical equation undone
        "ans": lambda p: p["a"] * p["a"],
        "spoken": lambda p: (f"The square root of x equals {p['a']}. What "
                             f"is x?"),
        # The board does NOT name the undo -- choosing the square over the
        # double IS the skill (the para/rasy rule).
        "board": _rsq_board,          # (tm) the machine that roots, its input blank
        "worked": _rsq_worked,        # (tm) the input found, the square drawn
        "praise": lambda p: (f"The root's undo is the square: {p['a']} times "
                             f"{p['a']} equals {p['a'] * p['a']}. Check: the "
                             f"square root of {p['a'] * p['a']} is "
                             f"{p['a']}."),
        "key": lambda p: p["a"],
        # The errors: DOUBLING (the root-means-half mirror), and handing x
        # back unchanged.
        "choices": lambda p: [p["a"] * p["a"], 2 * p["a"], p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (3 <= p["a"] <= 14
                            and len({p["a"] * p["a"], 2 * p["a"],
                                     p["a"]}) == 3,
                            "a root of at least 3, so the square and the "
                            "double are different taps"),
    },
    "rbet": {  # sqrt(a) for non-square a: closest whole number, by the squares
        "ans": lambda p: (lambda lo: lo if p["a"] - lo * lo
                          < (lo + 1) * (lo + 1) - p["a"] else lo + 1)
                         (int(p["a"] ** 0.5)),
        "spoken": lambda p: (f"The square root of {p['a']} is not a whole "
                             f"number — it sits between two. Which whole "
                             f"number is it CLOSEST to?"),
        "board": _rbet_board,         # (tm) the number between the two squares on the line
        "worked": _rbet_worked,       # (tm) the nearer square hopped to
        "praise": lambda p: (lambda lo, hi:
                             f"{p['a']} sits {p['a'] - lo * lo} past "
                             f"{lo * lo} and {hi * hi - p['a']} short of "
                             f"{hi * hi} — the root is closest to "
                             f"{lo if p['a'] - lo * lo < hi * hi - p['a'] else hi}.")
                            (int(p["a"] ** 0.5), int(p["a"] ** 0.5) + 1),
        "key": lambda p: p["a"],
        # The errors: the other neighbour, and the halving habit again.
        "choices": lambda p: (lambda lo, hi, ans:
                              [ans, hi if ans == lo else lo, p["a"] // 2])
                             (int(p["a"] ** 0.5), int(p["a"] ** 0.5) + 1,
                              (lambda lo: lo if p["a"] - lo * lo
                               < (lo + 1) * (lo + 1) - p["a"] else lo + 1)
                              (int(p["a"] ** 0.5))),
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (lambda lo, hi:
                            (lo * lo < p["a"] < hi * hi
                             and 12 <= p["a"] <= 150
                             and p["a"] - lo * lo != hi * hi - p["a"]
                             and p["a"] // 2 > hi,
                             "not a perfect square, not equidistant between "
                             "the neighbouring squares, and the half-tap "
                             "clears both neighbours"))
                           (int(p["a"] ** 0.5), int(p["a"] ** 0.5) + 1),
    },

    # ---- ALGEBRA II UNIT 6 (build lj) -- EXPONENTIAL & LOGARITHMIC FUNCTIONS --
    # Decay mirrors alg1-u6's doubling pond (the linear faller is the wrong tap,
    # exactly as the linear thinker was); then the LOGARITHM, met as a question
    # -- "the base raised to WHAT equals this?" -- read straight, with its
    # product rule (logs ADD when values times, the exadd/pdeg family), and by
    # estimation between the powers.
    "hlfl": {  # exponential decay: a grams halving for b days
        "ans": lambda p: p["a"] // (2 ** p["b"]),
        "spoken": lambda p: (f"A sample of {p['a']} grams halves every day. "
                             f"How many grams are left after {p['b']} days?"),
        "board": _hlfl_board,         # (tm) the sample to start, captioned
        "worked": _hlfl_worked,       # (tm) the sample fading day by day on the bars
        "praise": lambda p: (f"Halving {p['b']} times divides by "
                             f"{2 ** p['b']}: {p['a']} divided by "
                             f"{2 ** p['b']} equals "
                             f"{p['a'] // 2 ** p['b']} grams."),
        "key": lambda p: p["a"],
        # The errors: the LINEAR faller (down by 2 a day -- dbl's linear
        # thinker, falling instead of climbing), and halving only once.
        "choices": lambda p: [p["a"] // (2 ** p["b"]), p["a"] - 2 * p["b"],
                              p["a"] // 2],
        "check": lambda p: (2 <= p["b"] <= 4
                            and p["a"] % (2 ** p["b"]) == 0
                            and p["a"] // (2 ** p["b"]) >= 2
                            and p["a"] <= 96 and p["a"] - 2 * p["b"] >= 1
                            and len({p["a"] // (2 ** p["b"]),
                                     p["a"] - 2 * p["b"],
                                     p["a"] // 2}) == 3,
                            "the halvings come out whole, at least two days "
                            "pass, and the three taps differ"),
    },
    "logb": {  # the logarithm as a question: b^c = a, asked for c
        "ans": lambda p: p["c"],
        "spoken": lambda p: (f"{p['b']} raised to what power equals "
                             f"{p['a']}?"),
        "board": _logb_board,         # (tm) the power machine, its exponent blank
        "worked": _logb_worked,       # (tm) the layers stacked as bars
        "praise": lambda p: (f"{p['b']} multiplied out {p['c']} times builds "
                             f"{p['a']} — the hidden exponent, the logarithm, "
                             f"is {p['c']}."),
        "key": lambda p: p["a"],
        # The errors: dividing by the base ("log means divide"), and the base
        # copied.
        "choices": lambda p: [p["c"], p["a"] // p["b"], p["b"]],
        "check": lambda p: (p["b"] in (2, 3, 10)
                            and 3 <= p["c"] <= 10 and p["c"] != p["b"]
                            and p["a"] == p["b"] ** p["c"]
                            and p["a"] <= 1024
                            and len({p["c"], p["a"] // p["b"],
                                     p["b"]}) == 3,
                            "a true power of the base, exponent at least 3 "
                            "and not equal to the base, three distinct taps"),
    },
    "logm": {  # log2(a*b) = log2(a) + log2(b): logs ADD when values times
        "ans": lambda p: (p["a"].bit_length() - 1) + (p["b"].bit_length() - 1),
        "spoken": lambda p: (f"The logarithm base 2 of {p['a']} is "
                             f"{p['a'].bit_length() - 1}, and the logarithm "
                             f"base 2 of {p['b']} is "
                             f"{p['b'].bit_length() - 1}. What is the "
                             f"logarithm base 2 of {p['a'] * p['b']}?"),
        "board": _logm_board,         # (tm) the two stacks as bars, captioned; the product and the blank on two lines
        "worked": _logm_worked,       # (tm) the stacks joined
        "praise": lambda p: (f"When values times, their logarithms put "
                             f"together: {p['a'].bit_length() - 1} plus "
                             f"{p['b'].bit_length() - 1} equals "
                             f"{(p['a'].bit_length() - 1) + (p['b'].bit_length() - 1)}."),
        "key": lambda p: (p["a"].bit_length() - 1) + (p["b"].bit_length() - 1),
        # The errors: MULTIPLYING the logs (pdeg's cousin), and adding the
        # VALUES instead of the logs.
        "choices": lambda p: [(p["a"].bit_length() - 1)
                              + (p["b"].bit_length() - 1),
                              (p["a"].bit_length() - 1)
                              * (p["b"].bit_length() - 1),
                              p["a"] + p["b"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["a"] * p["b"]) in sp),
        "check": lambda p: (p["a"] == 2 ** (p["a"].bit_length() - 1)
                            and p["b"] == 2 ** (p["b"].bit_length() - 1)
                            and 4 <= p["a"] < p["b"] <= 128
                            and len({(p["a"].bit_length() - 1)
                                     + (p["b"].bit_length() - 1),
                                     (p["a"].bit_length() - 1)
                                     * (p["b"].bit_length() - 1),
                                     p["a"] + p["b"]}) == 3,
                            "both values are true powers of 2 (at least 4, so "
                            "sum and product of the logs differ)"),
    },
    "lbet": {  # log2(a) for a not a power of 2: closest whole, by the powers
        "ans": lambda p: (lambda lo: lo if p["a"] - 2 ** lo
                          < 2 ** (lo + 1) - p["a"] else lo + 1)
                         (p["a"].bit_length() - 1),
        "spoken": lambda p: (f"The logarithm base 2 of {p['a']} is not a "
                             f"whole number — it sits between two. Which "
                             f"whole number is it CLOSEST to?"),
        "board": _lbet_board,         # (tm) the number between the two powers, as bars
        "worked": _lbet_worked,       # (tm) the distances named
        "praise": lambda p: (lambda lo:
                             f"{p['a']} sits {p['a'] - 2 ** lo} past "
                             f"{2 ** lo} and {2 ** (lo + 1) - p['a']} short "
                             f"of {2 ** (lo + 1)} — the logarithm is closest "
                             f"to "
                             f"{lo if p['a'] - 2 ** lo < 2 ** (lo + 1) - p['a'] else lo + 1}.")
                            (p["a"].bit_length() - 1),
        "key": lambda p: p["a"],
        # The errors: the other neighbour, and the halving habit -- log read
        # as divide-by-2.
        "choices": lambda p: (lambda lo, ans:
                              [ans, lo + 1 if ans == lo else lo,
                               p["a"] // 2])
                             (p["a"].bit_length() - 1,
                              (lambda lo: lo if p["a"] - 2 ** lo
                               < 2 ** (lo + 1) - p["a"] else lo + 1)
                              (p["a"].bit_length() - 1)),
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (lambda lo:
                            (p["a"] & (p["a"] - 1) != 0
                             and 12 <= p["a"] <= 120
                             and p["a"] - 2 ** lo != 2 ** (lo + 1) - p["a"]
                             and p["a"] // 2 > lo + 1,
                             "not a power of 2, not equidistant between the "
                             "neighbouring powers, and the half-tap clears "
                             "both neighbours"))
                           (p["a"].bit_length() - 1),
    },

    # ---- ALGEBRA II UNIT 7 (build lk) -- SEQUENCES & SERIES -------------------
    # A PATTERN IS A RULE YOU CAN RIDE to any term without walking every step:
    # the arithmetic closed form (the off-by-one is THE trap -- term c is c-1
    # steps from the start), the geometric one (the adding habit is the trap,
    # the U4-similarity thread again), Gauss's pairing trick, and then walking
    # WITH a rule -- recursion -- as the contrast that shows what the closed
    # forms bought.
    "anth": {  # arithmetic sequence: start a, step b, term number c
        "ans": lambda p: p["a"] + (p["c"] - 1) * p["b"],
        "spoken": lambda p: (f"A pattern starts at {p['a']} and grows by "
                             f"{p['b']} each step. What is term number "
                             f"{p['c']}?"),
        # First three terms shown (the child could write them); the step COUNT
        # -- c or c-1 -- is the skill, so the board never says it.
        "board": _anth_board,         # (tn) the first three terms as bars, captioned
        "worked": _anth_worked,       # (tn) every term to the asked one
        "praise": lambda p: (f"From term 1 to term {p['c']} is "
                             f"{p['c'] - 1} steps — not {p['c']}: {p['a']} "
                             f"plus {p['c'] - 1} steps of {p['b']} equals "
                             f"{p['a'] + (p['c'] - 1) * p['b']}."),
        "key": lambda p: p["a"] + (p["c"] - 1) * p["b"],
        # The errors: the OFF-BY-ONE (took c steps -- term 1 is already
        # standing at the start), and forgetting the start entirely.
        "choices": lambda p: [p["a"] + (p["c"] - 1) * p["b"],
                              p["a"] + p["c"] * p["b"],
                              p["c"] * p["b"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["c"]) in sp),
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and p["a"] != p["b"] and 4 <= p["c"] <= 9
                            and p["a"] + (p["c"] - 1) * p["b"] <= 80
                            and len({p["a"] + (p["c"] - 1) * p["b"],
                                     p["a"] + p["c"] * p["b"],
                                     p["c"] * p["b"]}) == 3,
                            "start and step differ (so the forgot-the-start "
                            "tap is visible), and the three taps differ"),
    },
    "gnth": {  # geometric sequence: start a, ratio b, term number c
        "ans": lambda p: p["a"] * p["b"] ** (p["c"] - 1),
        "spoken": lambda p: (f"A pattern starts at {p['a']}, and each term is "
                             f"{p['b']} times the one before. What is term "
                             f"number {p['c']}?"),
        "board": _gnth_board,         # (tn) the first three terms as bars, captioned
        "worked": _gnth_worked,       # (tn) every leap to the asked term
        "praise": lambda p: (f"Times {p['b']} again and again — "
                             f"{p['c'] - 1} times in all: term {p['c']} is "
                             f"{p['a'] * p['b'] ** (p['c'] - 1)}."),
        "key": lambda p: p["a"] * p["b"] ** (p["c"] - 1),
        # The errors: the ARITHMETIC habit (grew by adding the ratio), and
        # stopping at term 2.
        "choices": lambda p: [p["a"] * p["b"] ** (p["c"] - 1),
                              p["a"] + p["b"] * (p["c"] - 1),
                              p["a"] * p["b"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["c"]) in sp),
        "check": lambda p: (2 <= p["a"] <= 5 and p["b"] in (2, 3)
                            and 3 <= p["c"] <= 6
                            and p["a"] * p["b"] ** (p["c"] - 1) <= 96
                            and len({p["a"] * p["b"] ** (p["c"] - 1),
                                     p["a"] + p["b"] * (p["c"] - 1),
                                     p["a"] * p["b"]}) == 3,
                            "the answer stays under 96 and the three taps "
                            "differ (excludes the collisions at 3-3-3 and "
                            "4-2-3)"),
    },
    "gaus": {  # the sum 1 + 2 + ... + n, by pairing the ends
        "ans": lambda p: p["a"] * (p["a"] + 1) // 2,
        "spoken": lambda p: (f"Put together every counting number from 1 up "
                             f"to {p['a']}. What is the sum?"),
        "board": _gaus_board,         # (tn) 1 up to n on the number line, captioned
        "worked": _gaus_worked,       # (tn) the staircase rectangle, half of it the sum (bars past 19)
        "praise": lambda p: (f"{p['a']} numbers, paired end to end, each pair "
                             f"{p['a'] + 1}: the sum is {p['a']} times "
                             f"{p['a'] + 1}, halved — "
                             f"{p['a'] * (p['a'] + 1) // 2}."),
        "key": lambda p: p["a"],
        # The errors: squaring ("n numbers, about n each"), and the last
        # number alone.
        "choices": lambda p: [p["a"] * (p["a"] + 1) // 2,
                              p["a"] * p["a"], p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (4 <= p["a"] <= 100
                            and len({p["a"] * (p["a"] + 1) // 2,
                                     p["a"] * p["a"], p["a"]}) == 3,
                            "at least 1-to-4, and the sum, the square and "
                            "the last number are three different taps"),
    },
    "reca": {  # walk a recursive rule twice: x2 then minus b, from a
        "ans": lambda p: 4 * p["a"] - 3 * p["b"],
        "spoken": lambda p: (f"A pattern's rule: each term is 2 times the one "
                             f"before, take away {p['b']}. The first term is "
                             f"{p['a']}. What is the third term?"),
        "board": _reca_board,         # (tn) the rule as a machine, its output blank
        "worked": _reca_worked,       # (tn) the machine run twice
        "praise": lambda p: (f"Term 2: 2 times {p['a']} take away {p['b']} is "
                             f"{2 * p['a'] - p['b']}. Term 3: 2 times "
                             f"{2 * p['a'] - p['b']} take away {p['b']} — "
                             f"{4 * p['a'] - 3 * p['b']}."),
        "key": lambda p: 4 * p["a"] - 3 * p["b"],
        # The errors: stopping at term 2, and forgetting the SECOND take away.
        "choices": lambda p: [4 * p["a"] - 3 * p["b"],
                              2 * p["a"] - p["b"],
                              4 * p["a"] - 2 * p["b"]],
        "check": lambda p: (2 <= p["a"] <= 12 and 1 <= p["b"] <= 9
                            and p["a"] != p["b"]
                            and 2 * p["a"] - p["b"] >= 2
                            and 4 * p["a"] - 3 * p["b"] >= 2
                            and len({4 * p["a"] - 3 * p["b"],
                                     2 * p["a"] - p["b"],
                                     4 * p["a"] - 2 * p["b"]}) == 3,
                            "both walked terms stay positive and the three "
                            "taps differ"),
    },

    # ---- ALGEBRA II UNIT 8 (build lk) -- TRIGONOMETRIC FUNCTIONS --------------
    # THE CIRCLE OF SIZE ONE: sine is the HEIGHT of the arrow's tip, cosine the
    # ACROSS -- read at the compass points, where both are exactly 1, 0 or -1
    # (the whole-number surface; the four base angles are the entire world, so
    # the teach necessarily shows them -- the turnc precedent -- and the spun
    # angles past 360 are the fresh practice). Then the spin that changes
    # nothing (coterminal angles) and the stretched wave (amplitude).
    # RENDERER RULE: [[unitcircle]] PRINTS "cos = ... sin = ..." at the bottom
    # -- teach and worked boards only, never a value ask.
    "sinp": {  # sine at the compass points, with full spins allowed
        "ans": lambda p: {0: 0, 90: 1, 180: 0, 270: -1}[p["a"] % 360],
        "spoken": lambda p: (f"What is the sine of {p['a']} degrees — 1, 0, "
                             f"or negative 1?"),
        "board": _sinp_board,         # (tn) statement lines only -- no question inside a step, no picture (the pointed arrow is the answer)
        "worked": _sinp_worked,       # (tn) the arrow pointed
        # The no-spin branch must start with a CAPITAL (the praise prefix ends
        # in "!", so a lowercase opener reads broken -- caught out loud).
        "praise": lambda p: (lambda spins, base:
                             ((("After " + ("a full spin, "
                                            if spins == 1 else
                                            f"{spins} full spins, "))
                               + "the arrow points ")
                              if spins else "The arrow points ")
                             + {0: "flat to the right — height 0",
                                90: "straight up — height 1",
                                180: "flat to the left — height 0",
                                270: "straight down — height negative 1"}
                             [base] + ".")
                            (p["a"] // 360, p["a"] % 360),
        "key": lambda p: p["a"],
        # All three values are always on offer -- the judgment IS the lesson.
        "choices": lambda p: [1, 0, -1],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (p["a"] % 90 == 0 and p["a"] % 360 in
                            (0, 90, 180, 270) and 0 <= p["a"] <= 1170,
                            "a compass point, possibly after full spins"),
    },
    "cosp": {  # cosine at the compass points -- the ACROSS, the deliberate pair
        "ans": lambda p: {0: 1, 90: 0, 180: -1, 270: 0}[p["a"] % 360],
        "spoken": lambda p: (f"What is the cosine of {p['a']} degrees — 1, 0, "
                             f"or negative 1?"),
        "board": _cosp_board,         # (tn) statement lines only -- no question inside a step, no picture (the pointed arrow is the answer)
        "worked": _cosp_worked,       # (tn) the arrow pointed
        "praise": lambda p: (lambda spins, base:
                             ((("After " + ("a full spin, "
                                            if spins == 1 else
                                            f"{spins} full spins, "))
                               + "the arrow points ")
                              if spins else "The arrow points ")
                             + {0: "flat to the right — across 1",
                                90: "straight up — across 0",
                                180: "flat to the left — across negative 1",
                                270: "straight down — across 0"}
                             [base] + ".")
                            (p["a"] // 360, p["a"] % 360),
        "key": lambda p: p["a"],
        "choices": lambda p: [1, 0, -1],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (p["a"] % 90 == 0 and p["a"] % 360 in
                            (0, 90, 180, 270) and 0 <= p["a"] <= 1170,
                            "a compass point, possibly after full spins"),
    },
    "spin": {  # coterminal: a degrees plus one full turn
        "ans": lambda p: p["a"] + 360,
        "spoken": lambda p: (f"Start at {p['a']} degrees and spin one more "
                             f"full turn around the circle. What angle do "
                             f"you land on?"),
        "board": _spin_board,         # (tn) the arrow at the angle, coordinates hidden (values="0")
        "worked": _spin_worked,       # (tn) the same arrow after a full turn
        "praise": lambda p: (f"A full turn is 360: {p['a']} plus 360 equals "
                             f"{p['a'] + 360} — same direction, same sine, "
                             f"same cosine."),
        "key": lambda p: p["a"],
        # The errors: the HALF turn, and spinning backwards to the mirror.
        "choices": lambda p: [p["a"] + 360, p["a"] + 180, 360 - p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (10 <= p["a"] <= 80
                            and len({p["a"] + 360, p["a"] + 180,
                                     360 - p["a"]}) == 3,
                            "a first-quarter angle, so all three taps "
                            "differ"),
    },
    "ampl": {  # amplitude: y = a sin x crests at a
        "ans": lambda p: p["a"],
        "spoken": lambda p: (f"The wave y equals {p['a']} times the sine of "
                             f"x rises and falls forever. What is the "
                             f"HIGHEST value it ever reaches?"),
        # The wave itself is on the board -- reading its crest IS understanding
        # amplitude (the sys1-crossing precedent).
        "board": _ampl_board,         # (tn) the wave, captioned
        "worked": _ampl_worked,       # (tn) the crest line drawn
        "praise": lambda p: (f"The plain sine tops out at 1; times {p['a']} "
                             f"stretches it — the wave crests at {p['a']} "
                             f"and dips to negative {p['a']}."),
        "key": lambda p: p["a"],
        # The errors: the full top-to-bottom swing, and the unstretched
        # sine's habit.
        "choices": lambda p: [p["a"], 2 * p["a"], 1],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (2 <= p["a"] <= 15
                            and len({p["a"], 2 * p["a"], 1}) == 3,
                            "a stretch of at least 2, so the crest, the "
                            "swing and the plain sine differ"),
    },

    # ---- ALGEBRA II UNIT 9 (build ll) -- STATISTICS & PROBABILITY -------------
    # ⭐ THE UNIT THAT COMPLETES ALGEBRA II. Past alg1-u9 (mean/median/range/
    # outlier) and geo-u9 (chance counts, the counting principle, tables):
    # statistics answers questions about what you have NOT seen yet -- the mean
    # when scores repeat, counting with three slots, what to expect from chance,
    # and scaling a sample up to the whole school.
    "wavg": {  # weighted mean: three quizzes at a, two at b
        "ans": lambda p: (3 * p["a"] + 2 * p["b"]) // 5,
        "spoken": lambda p: (f"Three quizzes each scored {p['a']} points, and "
                             f"two quizzes each scored {p['b']}. What is the "
                             f"mean of all five scores?"),
        # RAW givens: the five scores listed -- weighting them is the skill.
        "board": _wavg_board,         # (tn) the five scores as bars, captioned
        "worked": _wavg_worked,       # (tn) the mean beside them
        "praise": lambda p: (f"All five go in: three {p['a']}s and two "
                             f"{p['b']}s put together are "
                             f"{3 * p['a'] + 2 * p['b']}, shared by 5 — "
                             f"{(3 * p['a'] + 2 * p['b']) // 5}. The "
                             f"{p['a']}s count three times."),
        "key": lambda p: (3 * p["a"] + 2 * p["b"]) // 5,
        # The errors: the UNWEIGHTED mean of the two numbers (ignoring how
        # often each appears -- the classic), and the majority score alone.
        "choices": lambda p: [(3 * p["a"] + 2 * p["b"]) // 5,
                              (p["a"] + p["b"]) // 2, p["a"]],
        "check": lambda p: ((3 * p["a"] + 2 * p["b"]) % 5 == 0
                            and (p["a"] + p["b"]) % 2 == 0
                            and 2 <= p["a"] <= 20 and 2 <= p["b"] <= 20
                            and p["a"] != p["b"]
                            and len({(3 * p["a"] + 2 * p["b"]) // 5,
                                     (p["a"] + p["b"]) // 2,
                                     p["a"]}) == 3,
                            "both means come out whole, the two scores "
                            "differ, and the three taps differ"),
    },
    "cnt3": {  # the counting principle grows a slot: a * b * c
        "ans": lambda p: p["a"] * p["b"] * p["c"],
        "spoken": lambda p: (f"You own {p['a']} shirts, {p['b']} pairs of "
                             f"pants, and {p['c']} hats, all different. How "
                             f"many different outfits can you choose?"),
        "board": _cnt3_board,         # (tn) shirts by pants as an array, captioned
        "worked": _cnt3_worked,       # (tn) the pairs counted, then the hats
        "praise": lambda p: (f"Choices times up, slot by slot: {p['a']} times "
                             f"{p['b']} is {p['a'] * p['b']}, times "
                             f"{p['c']} — {p['a'] * p['b'] * p['c']}."),
        "key": lambda p: p["a"] * p["b"] * p["c"],
        # The errors: ADDING the three counts, and stopping after two slots.
        "choices": lambda p: [p["a"] * p["b"] * p["c"],
                              p["a"] + p["b"] + p["c"],
                              p["a"] * p["b"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["c"]) in sp),
        "check": lambda p: (2 <= p["a"] <= 5 and 2 <= p["b"] <= 5
                            and 2 <= p["c"] <= 5
                            and len({p["a"] * p["b"] * p["c"],
                                     p["a"] + p["b"] + p["c"],
                                     p["a"] * p["b"]}) == 3,
                            "small closets, and the product, the sum and the "
                            "two-slot stop are three different numbers"),
    },
    "expv": {  # expected value in child clothes: a wins of c tokens per b plays
        "ans": lambda p: p["a"] * p["c"],
        "spoken": lambda p: (f"In a game, you win {p['c']} tokens exactly "
                             f"{p['a']} times out of every {p['b']} plays. "
                             f"You play {p['b']} times. How many tokens "
                             f"should you EXPECT to win in all?"),
        "board": _expv_board,         # (tn) the plays as a pie, the paying ones shaded
        "worked": _expv_worked,       # (tn) the wins of tokens as an array
        "praise": lambda p: (f"About {p['a']} of the {p['b']} plays pay out: "
                             f"{p['a']} wins of {p['c']} tokens equals "
                             f"{p['a'] * p['c']} tokens."),
        "key": lambda p: p["a"] * p["c"],
        # The errors: paying out EVERY play, and paying out only once.
        "choices": lambda p: [p["a"] * p["c"], p["b"] * p["c"], p["c"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["c"]) in sp),
        "check": lambda p: (2 <= p["a"] < p["b"] <= 10 and 2 <= p["c"] <= 9
                            and len({p["a"] * p["c"], p["b"] * p["c"],
                                     p["c"]}) == 3,
                            "wins are fewer than plays, and the three taps "
                            "differ"),
    },
    "samp": {  # scale a sample to the school: b liked, school is c samples wide
        "ans": lambda p: p["b"] * p["c"],
        "spoken": lambda p: (f"A sample of {p['a']} students found {p['b']} "
                             f"of them like pizza. The whole school has "
                             f"{p['a'] * p['c']} students. About how many of the "
                             f"whole school like pizza?"),
        "board": _samp_board,         # (tn) the sample beside the school, as bars
        "worked": _samp_worked,       # (tn) the sample scaled
        "praise": lambda p: (f"The school is {p['c']} samples wide: "
                             f"{p['b']} liked it per sample, times "
                             f"{p['c']} — about {p['b'] * p['c']}."),
        "key": lambda p: p["b"] * p["c"],
        # The errors: the sample count copied ("the survey already said"),
        # and the about-half guess.
        "choices": lambda p: [p["b"] * p["c"], p["b"],
                              (p["a"] * p["c"]) // 2],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["a"] * p["c"]) in sp),
        "check": lambda p: (2 <= p["b"] < p["a"] <= 30 and 2 <= p["c"] <= 10
                            and (p["a"] * p["c"]) % 2 == 0
                            and p["a"] * p["c"] <= 400
                            and len({p["b"] * p["c"], p["b"],
                                     (p["a"] * p["c"]) // 2}) == 3,
                            "the sample is bigger than the yes-count, the "
                            "school halves evenly, and the three taps "
                            "differ"),
    },

    # ---- PRE-CALC UNIT 1 (build ll) -- FUNCTIONS & THEIR GRAPHS ---------------
    # ⭐ THE NINTH COURSE OPENS. Algebra I's machines grow up: composition in
    # f(g(x)) notation (inside first -- the order flip is THE trap), the graph
    # that slides opposite its sign (vtx2's lesson, generalized), the domain as
    # a doorway (the root's edge is WELCOME, unlike division's forbidden x --
    # the contrast is taught), and a function in pieces.
    "fcmp": {  # f(x) = x + a, g(x) = b x: evaluate f(g(c)) -- inside first
        "ans": lambda p: p["b"] * p["c"] + p["a"],
        "spoken": lambda p: (f"Two new machines, still called f and g. f of x equals x plus "
                             f"{p['a']}. g of x equals {p['b']} times x. "
                             f"What is f of g of {p['c']}?"),   # (up) the names retired out loud
        "board": _fcmp_board,         # (to) two machines in a row, g first, both outputs blank
        "worked": _fcmp_worked,       # (to) both machines answered
        "praise": lambda p: (f"Inside first: g of {p['c']} is "
                             f"{p['b'] * p['c']}. Then f: {p['b'] * p['c']} "
                             f"plus {p['a']} equals "
                             f"{p['b'] * p['c'] + p['a']}. The inner machine "
                             f"runs before the outer."),
        "key": lambda p: p["b"] * p["c"] + p["a"],
        # The errors: running f FIRST (the order flip -- THE composition
        # misconception), and forgetting the outer machine.
        "choices": lambda p: [p["b"] * p["c"] + p["a"],
                              p["b"] * (p["c"] + p["a"]),
                              p["b"] * p["c"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["c"]) in sp),
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 4
                            and 2 <= p["c"] <= 9
                            and len({p["b"] * p["c"] + p["a"],
                                     p["b"] * (p["c"] + p["a"]),
                                     p["b"] * p["c"]}) == 3,
                            "small machines, and the right order, the "
                            "flipped order and the unfinished run are three "
                            "different numbers"),
    },
    "fshf": {  # y = f(x - a): the point (b, c) slides RIGHT -- new x = b + a
        "ans": lambda p: p["b"] + p["a"],
        "spoken": lambda p: (f"The graph of y equals f of x becomes y equals "
                             f"f of: x take away {p['a']}. The point "
                             f"({p['b']}, {p['c']}) on the old graph slides "
                             f"to a new spot. What is its new x?"),
        "board": _fshf_board,         # (to) the old point on the grid, captioned
        "worked": _fshf_worked,       # (to) the point and where it landed
        "praise": lambda p: (f"The minus points OPPOSITE, exactly as the "
                             f"vertex lesson said: take away {p['a']} inside "
                             f"slides the graph RIGHT — the point lands at x "
                             f"equals {p['b'] + p['a']}."),
        "key": lambda p: p["b"] + p["a"],
        # The errors: reading the minus literally (slid left), and not
        # sliding at all.
        "choices": lambda p: [p["b"] + p["a"], p["b"] - p["a"], p["b"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["c"]) in sp),
        "check": lambda p: (2 <= p["a"] <= 9 and p["a"] < p["b"] <= 12
                            and 1 <= p["c"] <= 9
                            and len({p["b"] + p["a"], p["b"] - p["a"],
                                     p["b"]}) == 3,
                            "the literal-minus slip stays on the grid, and "
                            "the three taps differ"),
    },
    "fdom": {  # domain of sqrt(x - a): the doorway is a, and it is WELCOME
        "ans": lambda p: p["a"],
        "spoken": lambda p: (f"y equals the square root of: x take away "
                             f"{p['a']}. Roots refuse negatives. What is the "
                             f"SMALLEST x allowed in?"),
        "board": lambda p: (f'[[step eq="y = √(x − {p["a"]})"]]'
                            f'[[step eq="under the root must not go negative '
                            f'· smallest x = ?"]]'),
        "worked": _fdom_worked,       # (to) the curve starting at the doorway (no picture on the ask: the curve starts at the answer)
        "praise": lambda p: (f"Below {p['a']}, x take away {p['a']} goes "
                             f"negative and the root refuses. At x equals "
                             f"{p['a']} it is exactly zero — and zero under "
                             f"a root is welcome. The doorway is {p['a']}."),
        "key": lambda p: p["a"],
        # The errors: the sign flip (excl's cousin, by design), and "zero is
        # always the edge".
        "choices": lambda p: [p["a"], -p["a"], 0],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (2 <= p["a"] <= 14
                            and len({p["a"], -p["a"], 0}) == 3,
                            "a nonzero doorway, so the flip and the zero "
                            "habit are visible mistakes"),
    },
    "fpie": {  # piecewise: x + a below 5, b x at 5 or more -- run the RIGHT rule
        "ans": lambda p: (p["c"] + p["a"] if p["c"] < 5
                          else p["b"] * p["c"]),
        "spoken": lambda p: (f"A function in pieces: y equals x plus {p['a']} "
                             f"when x is below 5, and y equals {p['b']} times "
                             f"x when x is 5 or more. What is y when x "
                             f"equals {p['c']}?"),
        "board": _fpie_board,         # (to) the border and x on the number line
        "worked": _fpie_worked,       # (to) the side named, the rule run
        "praise": lambda p: ((f"x equals {p['c']} is below 5, so the FIRST "
                              f"rule runs: {p['c']} plus {p['a']} equals "
                              f"{p['c'] + p['a']}. The other rule sleeps.")
                             if p["c"] < 5 else
                             (f"x equals {p['c']} is 5 or more, so the "
                              f"SECOND rule runs: {p['b']} times {p['c']} "
                              f"equals {p['b'] * p['c']}. The other rule "
                              f"sleeps.")),
        "key": lambda p: (p["c"] + p["a"] if p["c"] < 5
                          else p["b"] * p["c"]),
        # The errors: running the WRONG piece, and handing x back untouched.
        "choices": lambda p: [(p["c"] + p["a"] if p["c"] < 5
                               else p["b"] * p["c"]),
                              (p["b"] * p["c"] if p["c"] < 5
                               else p["c"] + p["a"]),
                              p["c"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["c"]) in sp),
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 4
                            and 2 <= p["c"] <= 9
                            and p["c"] + p["a"] != p["b"] * p["c"]
                            and len({(p["c"] + p["a"] if p["c"] < 5
                                      else p["b"] * p["c"]),
                                     (p["b"] * p["c"] if p["c"] < 5
                                      else p["c"] + p["a"]),
                                     p["c"]}) == 3,
                            "the two rules land on different values at this "
                            "x, and the three taps differ"),
    },
    # ---- build lm: Pre-Calc U2 Polynomial & Rational Functions ------------
    "negp": {  # (-1)^a: even wipes the minus, odd leaves one
        "ans": lambda p: 1 if p["a"] % 2 == 0 else -1,
        "spoken": lambda p: (f"What is negative 1, raised to the power "
                             f"{p['a']}?"),
        "board": lambda p: f'[[step eq="(−1)^{p["a"]} = ?"]]',
        "worked": _negp_worked,       # (to) the minus signs paired on the array (the pairing is the answer -- walk-back only)
        "praise": lambda p: ((f"The power {p['a']} is even: the minus signs "
                              f"cancel two at a time, none survive, and the "
                              f"answer is 1.")
                             if p["a"] % 2 == 0 else
                             (f"The power {p['a']} is odd: the minus signs "
                              f"cancel two at a time, and one lone minus "
                              f"sign survives. The answer is negative 1.")),
        "key": lambda p: p["a"],
        # The errors: the other parity, and "the minus signs all vanish to 0".
        "choices": lambda p: [1, -1, 0],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (2 <= p["a"] <= 15 and p["b"] == 0,
                            "a real parade: power between 2 and 15, and no "
                            "second number"),
    },
    "remt": {  # remainder theorem: plug a into x^2 + bx + c -- no dividing
        "ans": lambda p: p["a"] * p["a"] + p["a"] * p["b"] + p["c"],
        "spoken": lambda p: (f"Take x squared plus {p['b']} x plus {p['c']}, "
                             f"divided by x take away {p['a']}. Do NOT "
                             f"divide — plug {p['a']} into the top instead. "
                             f"What number is left over?"),
        "board": _remt_board,         # (to) the plug-in machine, its output blank
        "worked": _remt_worked,       # (to) the machine answered
        "praise": lambda p: (f"Plug in {p['a']}: {p['a']} squared equals "
                             f"{p['a'] * p['a']}, plus {p['b']} times "
                             f"{p['a']} equals {p['a'] * p['b']}, plus "
                             f"{p['c']} — in all, "
                             f"{p['a'] * p['a'] + p['a'] * p['b'] + p['c']}. "
                             f"Long division would have ended exactly "
                             f"there, and you never divided."),
        "key": lambda p: p["a"] * p["a"] + p["a"] * p["b"] + p["c"],
        # The errors: plugging in zero (the end number), and the root itself.
        "choices": lambda p: [p["a"] * p["a"] + p["a"] * p["b"] + p["c"],
                              p["c"], p["a"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["c"]) in sp),
        "check": lambda p: (2 <= p["a"] <= 5 and 1 <= p["b"] <= 6
                            and 1 <= p["c"] <= 9 and p["c"] != p["a"]
                            and p["a"] * p["a"] + p["a"] * p["b"] + p["c"]
                            <= 40,
                            "small quadratic, the leftover stays under 40, "
                            "and the zero-plug tap differs from the root "
                            "tap"),
    },
    "vprd": {  # Vieta: roots a and b -- the end number is their product
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: (f"A puzzle's roots are {p['a']} and {p['b']}, "
                             f"so it equals x take away {p['a']}, times x "
                             f"take away {p['b']}. Multiplied out, it ends "
                             f"in a plain number. What is that END number?"),
        "board": _vprd_board,         # (to) the four rooms with the corner blank
        "worked": _vprd_worked,       # (to) the four rooms filled
        "praise": lambda p: (f"The end number is the product of the roots: "
                             f"{p['a']} times {p['b']} equals "
                             f"{p['a'] * p['b']}. The middle number is "
                             f"their sum, {p['a'] + p['b']}, worn with a "
                             f"minus — the roots write the whole puzzle."),
        "key": lambda p: p["a"] * p["b"],
        # The errors: the SUM (that is the middle number -- lh's promise,
        # paid), and the first root copied.
        "choices": lambda p: [p["a"] * p["b"], p["a"] + p["b"], p["a"]],
        "check": lambda p: (2 <= p["a"] < p["b"] <= 8
                            and p["a"] * p["b"] <= 40
                            and len({p["a"] * p["b"], p["a"] + p["b"],
                                     p["a"]}) == 3,
                            "two different roots, product under 40, and the "
                            "sum tap is a visible mistake"),
    },
    "vasy": {  # how many forbidden x's in 1 / ((x-a)(x-b)): count the ZEROS
        "ans": lambda p: 2 if p["a"] != p["b"] else 1,
        "spoken": lambda p: (f"y equals 1 divided by: x take away {p['a']}, "
                             f"times x take away {p['b']}. Division forbids "
                             f"any x that turns the bottom into zero. How "
                             f"many x's are forbidden?"),
        "board": lambda p: (f'[[step eq="y = 1 ÷ (x − {p["a"]})'
                            f'(x − {p["b"]})"]]'
                            f'[[step eq="forbidden x count = ?"]]'),
        "worked": _vasy_worked,       # (to) the curve flying off (its poles are the answer -- walk-back only)
        "praise": lambda p: ((f"Two factors, two different zeros: x equals "
                              f"{p['a']} zeroes the first, and x equals "
                              f"{p['b']} zeroes the second. The count is 2 "
                              f"— division forbids them both.")
                             if p["a"] != p["b"] else
                             (f"Both factors die at the same x: only x "
                              f"equals {p['a']} zeroes the bottom. The "
                              f"count is 1 — one x, counted once, however "
                              f"many factors say its name.")),
        "key": lambda p: p["a"] + p["b"],
        # The errors: the repeated case answered 2 (or the distinct case 1),
        # and "nothing is forbidden".
        "choices": lambda p: [2, 1, 0],
        "check": lambda p: (2 <= p["a"] <= p["b"] <= 8,
                            "factors in order, zeros between 2 and 8"),
    },
    # ---- build lm: Pre-Calc U3 Exponential & Logarithmic Functions --------
    "logp": {  # log2(a^b) by the power rule: the exponent comes down front
        "ans": lambda p: p["b"] * (p["a"].bit_length() - 1),
        "spoken": lambda p: (f"What is the logarithm, base 2, of {p['a']} "
                             f"raised to the power {p['b']}?"),
        "board": lambda p: f'[[step eq="log {p["a"]}^{p["b"]} = ? · base 2"]]',
        "worked": _logp_worked,       # (to) the log beside the log of the power, as bars
        "praise": lambda p: (lambda j:
                             f"The power rule: the exponent {p['b']} comes "
                             f"down front. Log base 2 of {p['a']} is {j}, "
                             f"so the logarithm equals {p['b']} times {j} — "
                             f"{p['b'] * j}. Powering the log instead lands "
                             f"on {j ** p['b']}, the wrong kind of growth.")
                            (p["a"].bit_length() - 1),
        "key": lambda p: p["b"] * (p["a"].bit_length() - 1),
        # The errors: the log RAISED to the exponent, and the bare log with
        # the power ignored.
        "choices": lambda p: (lambda j: [p["b"] * j, j ** p["b"], j])
                             (p["a"].bit_length() - 1),
        "check": lambda p: (lambda j:
                            (p["a"] == 2 ** j and j >= 3
                             and p["b"] in (2, 3) and p["a"] <= 512
                             and len({p["b"] * j, j ** p["b"], j}) == 3,
                             "a true power of 2 with at least three layers, "
                             "exponent 2 or 3, three distinct taps"))
                           (p["a"].bit_length() - 1),
    },
    "lsol": {  # solve log_a(?) = b: rebuild the number by stacking the base
        "ans": lambda p: p["a"] ** p["b"],
        "spoken": lambda p: (f"The logarithm, base {p['a']}, of a mystery "
                             f"number equals {p['b']}. What is the mystery "
                             f"number?"),
        "board": _lsol_board,         # (to) the log machine run backwards, its input blank
        "worked": _lsol_worked,       # (to) the layers stacked and the machine answered
        "praise": lambda p: (f"Stack the base: {p['a']} multiplied out "
                             f"{p['b']} times equals {p['a'] ** p['b']} — "
                             f"the power un-does the log. The tap "
                             f"{p['a'] * p['b']} came from {p['a']} times "
                             f"{p['b']}, a single times when the log "
                             f"promised {p['b']} whole layers."),
        "key": lambda p: p["a"] ** p["b"],
        # The errors: base TIMES log (the single-times trap), and base PLUS
        # log.
        "choices": lambda p: [p["a"] ** p["b"], p["a"] * p["b"],
                              p["a"] + p["b"]],
        "check": lambda p: (p["a"] in (2, 3, 10) and 2 <= p["b"] <= 8
                            and not (p["a"] == 2 and p["b"] == 2)
                            and p["a"] ** p["b"] <= 1000
                            and len({p["a"] ** p["b"], p["a"] * p["b"],
                                     p["a"] + p["b"]}) == 3,
                            "a friendly base, the rebuilt number stays at "
                            "1000 or under, and the three taps differ"),
    },
    "hcnt": {  # halvings counted BACKWARDS: a -> b, how many days -- a log
        "ans": lambda p: (p["a"] // p["b"]).bit_length() - 1,
        "spoken": lambda p: (f"A tank starts at {p['a']} liters, and each "
                             f"day it drops to HALF. Now it holds {p['b']} "
                             f"liters. How many days went by?"),
        "board": _hcnt_board,         # (to) start beside now, as bars
        "worked": _hcnt_worked,       # (to) the tank halving day by day
        "praise": lambda p: (lambda k:
                             "Halve and count: "
                             + ", then ".join(str(p["a"] >> i)
                                              for i in range(k + 1))
                             + f". That is {k} halvings — {k} days. The "
                             f"ratio {p['a'] // p['b']} says how many times "
                             f"bigger {p['a']} is, never how many days it "
                             f"took.")
                            ((p["a"] // p["b"]).bit_length() - 1),
        "key": lambda p: (p["a"] // p["b"]).bit_length() - 1,
        # The errors: the RATIO handed back as the count (hlfl's mirror
        # trap), and the end amount copied.
        "choices": lambda p: [(p["a"] // p["b"]).bit_length() - 1,
                              p["a"] // p["b"], p["b"]],
        "check": lambda p: (lambda k:
                            (p["b"] >= 2 and p["a"] <= 96
                             and 2 <= k <= 5
                             and p["a"] == p["b"] * 2 ** k
                             and k != p["b"]
                             and p["a"] // p["b"] != p["b"],
                             "the halvings come out exact, two to five "
                             "days, and the three taps differ"))
                           ((p["a"] // p["b"]).bit_length() - 1),
    },
    "cmpd": {  # money doubling every a years for a*b years: count, then power
        "ans": lambda p: p["c"] * 2 ** p["b"],
        "spoken": lambda p: (f"You save {p['c']} dollars, and it DOUBLES "
                             f"every {p['a']} years. After "
                             f"{p['a'] * p['b']} years, how many dollars do "
                             f"you have?"),
        "board": _cmpd_board,         # (to) the pile to start, as a bar
        "worked": _cmpd_worked,       # (to) the pile doubling year by year
        "praise": lambda p: ("Count the doublings first: "
                             f"{p['a'] * p['b']} divided by {p['a']} equals "
                             f"{p['b']}. Now double: "
                             + ", then ".join(str(p["c"] * 2 ** i)
                                              for i in range(p["b"] + 1))
                             + f". Steady adding would stall at "
                             f"{p['c'] * (1 + p['b'])} dollars — doubling "
                             f"pulls away."),
        "key": lambda p: p["c"] * 2 ** p["b"],
        # The errors: SIMPLE growth (up by c each doubling period), and
        # doubling exactly once.
        "choices": lambda p: [p["c"] * 2 ** p["b"],
                              p["c"] * (1 + p["b"]), 2 * p["c"]],
        "speaks": lambda p, sp: (str(p["c"]) in sp and str(p["a"]) in sp
                                 and str(p["a"] * p["b"]) in sp),
        "check": lambda p: (2 <= p["a"] <= 10 and 2 <= p["b"] <= 4
                            and 2 <= p["c"] <= 6
                            and p["c"] * 2 ** p["b"] <= 96
                            and len({p["c"] * 2 ** p["b"],
                                     p["c"] * (1 + p["b"]),
                                     2 * p["c"]}) == 3,
                            "two to four doublings, the pile stays at 96 "
                            "dollars or under, and the three taps differ"),
    },
    # ---- build ln: Pre-Calc U4 Trigonometric Functions --------------------
    "rad1": {  # degrees -> pi radians: count the HALF TURNS
        "ans": lambda p: p["a"],
        "spoken": lambda p: (f"How many pi radians is {180 * p['a']} "
                             f"degrees?"),
        "board": _rad1_board,         # (tp) a half turn beside the angle, as bars
        "worked": _rad1_worked,       # (tp) the half turns laid end to end
        "praise": lambda p: (f"180 degrees is one pi, so count the half "
                             f"turns: {180 * p['a']} divided by 180 equals "
                             f"{p['a']} — {p['a']} pi radians. Counting "
                             f"quarter turns would double it, and the "
                             f"degrees themselves were never the answer."),
        "key": lambda p: p["a"],
        # The errors: quarter turns counted (90-per-pi), and the degrees
        # handed straight back.
        "choices": lambda p: [p["a"], 2 * p["a"], 180 * p["a"]],
        "speaks": lambda p, sp: str(180 * p["a"]) in sp,
        "check": lambda p: (1 <= p["a"] <= 13 and p["b"] == 0,
                            "a whole count of half turns, and no second "
                            "number"),
    },
    "nspn": {  # negative angle -> its positive coterminal name: add 360
        "ans": lambda p: 360 - p["a"],
        "spoken": lambda p: (f"Start at negative {p['a']} degrees — a "
                             f"backwards spin. Add one full turn. What "
                             f"positive angle names the same direction?"),
        "board": _nspn_board,         # (tp) the arrow wound backwards, coordinates hidden
        "worked": _nspn_worked,       # (tp) the same arrow, named forwards
        "praise": lambda p: (f"A full turn is 360: negative {p['a']} plus "
                             f"360 equals {360 - p['a']} — the same arrow, "
                             f"named forwards. Dropping the minus would say "
                             f"{p['a']} — the mirror image, on the wrong "
                             f"side of the flat line."),
        "key": lambda p: p["a"],
        # The errors: the minus dropped (the mirror), and only a half turn
        # added.
        "choices": lambda p: [360 - p["a"], p["a"], 180 - p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (10 <= p["a"] <= 170 and p["a"] != 90
                            and p["b"] == 0
                            and len({360 - p["a"], p["a"],
                                     180 - p["a"]}) == 3,
                            "a backwards angle under half a turn, not 90, "
                            "and the three taps differ"),
    },
    "refq": {  # reference angle in the second quarter: the gap to 180
        "ans": lambda p: 180 - p["a"],
        "spoken": lambda p: (f"The arrow rests at {p['a']} degrees — past "
                             f"straight up, short of flat left. Its "
                             f"reference angle is the small gap between the "
                             f"arrow and the flat line. How many degrees is "
                             f"that gap?"),
        "board": _refq_board,         # (tp) the flat line split at the arrow, the gap blank
        "worked": _refq_worked,       # (tp) both pieces labelled
        "praise": lambda p: (f"Flat left is 180, and the arrow sits at "
                             f"{p['a']}: the gap is 180 take away {p['a']} "
                             f"— {180 - p['a']} degrees. Measured from "
                             f"straight up it would be {p['a'] - 90}, but "
                             f"reference angles hug the FLAT line, always."),
        "key": lambda p: p["a"],
        # The errors: measured from straight up, and the angle itself.
        "choices": lambda p: [180 - p["a"], p["a"] - 90, p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (100 <= p["a"] <= 170 and p["a"] % 5 == 0
                            and p["a"] != 135 and p["b"] == 0,
                            "a second-quarter angle, not 135 (where the "
                            "top-measure tap would collide)"),
    },
    "wper": {  # period of sin(a x): divide 360 by the multiplier
        "ans": lambda p: 360 // p["a"],
        "spoken": lambda p: (f"y equals the sine of {p['a']} x. The plain "
                             f"sine repeats every 360 degrees. How many "
                             f"degrees until THIS wave repeats?"),
        "board": _wper_board,         # (tp) the plain sine beside the fast one, the axis in degrees
        "worked": _wper_worked,       # (tp) the fast wave with its first repeat marked
        "praise": lambda p: (f"Divide: 360 divided by {p['a']} equals "
                             f"{360 // p['a']} — this wave tells its whole "
                             f"story in {360 // p['a']} degrees. Stretching "
                             f"to {360 * p['a']} points the wrong way: "
                             f"faster waves repeat SOONER, never later."),
        "key": lambda p: p["a"],
        # The errors: multiplied instead (faster read as longer), and the
        # plain sine's 360 kept.
        "choices": lambda p: [360 // p["a"], 360 * p["a"], 360],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (p["a"] in (3, 4, 5, 6, 8, 9, 10, 12, 15, 18,
                                       20, 24)
                            and 360 % p["a"] == 0 and p["b"] == 0,
                            "a clean divisor of 360, at least 3"),
    },
    # ---- build ln: Pre-Calc U5 Analytic Trigonometry ----------------------
    "pyid": {  # sin^2 + cos^2 = 1, split into hundredths
        "ans": lambda p: 100 - p["a"],
        "spoken": lambda p: (f"For a certain angle, sine squared equals "
                             f"{p['a']} hundredths — {p['a']} of the 100. How "
                             f"many of the 100 hundredths is cosine squared?"),
        "board": _pyid_board,         # (tp) the hundred square, sine squared shaded
        "worked": _pyid_worked,       # (tp) the split named
        "praise": lambda p: (f"Sine squared plus cosine squared equals 1 — "
                             f"the whole hundred: 100 take away {p['a']} "
                             f"equals {100 - p['a']}. The pair always "
                             f"splits one whole between them."),
        "key": lambda p: p["a"],
        # The errors: sine's share copied, and the whole 100 handed back.
        "choices": lambda p: [100 - p["a"], p["a"], 100],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (1 <= p["a"] <= 99 and p["a"] != 50
                            and p["b"] == 0,
                            "a real share of the whole, not the 50-50 "
                            "split where the copy tap would collide"),
    },
    "cofn": {  # cofunction: sin(a) = cos(90 - a)
        "ans": lambda p: 90 - p["a"],
        "spoken": lambda p: (f"The sine of {p['a']} degrees equals the "
                             f"cosine of one special angle. Which angle?"),
        "board": _cofn_board,         # (tp) the right triangle, its second sharp corner blank
        "worked": _cofn_worked,       # (tp) both sharp corners labelled
        "praise": lambda p: (f"Sine and cosine are partners across 90: "
                             f"{p['a']} plus {90 - p['a']} equals 90, so "
                             f"the sine of {p['a']} equals the cosine of "
                             f"{90 - p['a']} — a right angle's two sharp "
                             f"corners, finishing 90 together."),
        "key": lambda p: p["a"],
        # The errors: the same angle kept, and 90 ADDED instead of shared.
        "choices": lambda p: [90 - p["a"], p["a"], 90 + p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (10 <= p["a"] <= 80 and p["a"] % 5 == 0
                            and p["a"] != 45 and p["b"] == 0,
                            "a sharp angle, not 45 (its own partner), in "
                            "clean fives"),
    },
    "negf": {  # even/odd: cos(-a) = cos(a), sin(-a) = -sin(a), compass points
        "ans": lambda p: ({0: 1, 90: 0, 180: -1, 270: 0}[p["a"] % 360]
                          if p["c"] == 0 else
                          {0: 0, 90: -1, 180: 0, 270: 1}[p["a"] % 360]),
        "spoken": lambda p: (f"What is the "
                             f"{'cosine' if p['c'] == 0 else 'sine'} of "
                             f"negative {p['a']} degrees — 1, 0, or "
                             f"negative 1?"),
        "board": lambda p: (f'[[step eq="−{p["a"]}° · a backwards spin"]]'
                            + ('[[step eq="cosine = the across of its '
                               'tip"]]' if p["c"] == 0 else
                               '[[step eq="sine = the height of its '
                               'tip"]]')),
        "worked": _negf_worked,       # (tp) the arrow wound backwards with its values (the pointed arrow is the answer -- walk-back only)
        "praise": lambda p: (lambda v, w:
                             ((f"Backwards or forwards, the across is the "
                               f"same — the mirror flips height, never "
                               f"across. The cosine of negative {p['a']} "
                               f"equals the cosine of {p['a']}: {w}.")
                              if p["c"] == 0 else
                              (f"The mirror flips the height: the sine of "
                               f"negative {p['a']} is the opposite of the "
                               f"sine of {p['a']} — {w}.")))
                            (0, ("negative 1" if
                                 ({0: 1, 90: 0, 180: -1, 270: 0}
                                  [p["a"] % 360] if p["c"] == 0 else
                                  {0: 0, 90: -1, 180: 0, 270: 1}
                                  [p["a"] % 360]) == -1 else
                                 str({0: 1, 90: 0, 180: -1, 270: 0}
                                     [p["a"] % 360] if p["c"] == 0 else
                                     {0: 0, 90: -1, 180: 0, 270: 1}
                                     [p["a"] % 360]))),
        "key": lambda p: p["a"],
        # All three values always on offer -- the judgment IS the lesson
        # (sinp's precedent).
        "choices": lambda p: [1, 0, -1],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (p["a"] % 360 in (0, 90, 180, 270)
                            and 90 <= p["a"] <= 810 and p["b"] == 0
                            and p["c"] in (0, 1),
                            "a compass point fed in backwards, cosine or "
                            "sine"),
    },
    "sols": {  # count the solutions per sweep: skip the start, keep the finish
        "ans": lambda p: (2 if p["a"] == 0 else 1) * p["b"],
        "spoken": lambda p: (f"The arrow sweeps {p['b']} full "
                             f"turn{'s' if p['b'] > 1 else ''}. Not "
                             f"counting the start, how many times along "
                             f"the way does the "
                             f"{'sine' if p['c'] == 0 else 'cosine'} equal "
                             + ("0" if p["a"] == 0 else
                                ("1" if p["a"] == 1 else "negative 1"))
                             + "?"),
        "board": _sols_board,         # (tp) the wave through the turns with its level line; no question inside a step (the old "how many times?" was one)
        "worked": _sols_worked,       # (tp) the touches marked
        "praise": lambda p: (lambda base, word, place:
                             (f"Each turn, the {word} equals "
                              + ("0" if p["a"] == 0 else
                                 ("1" if p["a"] == 1 else "negative 1"))
                              + f" {'twice' if base == 2 else 'once'} — "
                              f"{place}. "
                              + (f"{p['b']} turns, {base} each: "
                                 f"{base * p['b']}."
                                 if p["b"] > 1 else
                                 f"One turn, so the count is {base}.")))
                            (2 if p["a"] == 0 else 1,
                             "sine" if p["c"] == 0 else "cosine",
                             {(0, 0): "at flat left and at the finish",
                              (0, 1): "at straight up",
                              (0, -1): "at straight down",
                              (1, 0): "at straight up and at straight down",
                              (1, 1): "at the finish",
                              (1, -1): "at flat left"}[(p["c"], p["a"])]),
        "key": lambda p: (2 if p["a"] == 0 else 1) * p["b"],
        # The errors: the miscounts, and 4 -- "one per quarter, always".
        "choices": lambda p: [2, 1, 4],
        "speaks": lambda p, sp: str(p["b"]) in sp,
        "check": lambda p: (p["a"] in (-1, 0, 1) and p["b"] in (1, 2)
                            and p["c"] in (0, 1),
                            "a reachable target, one or two sweeps, sine "
                            "or cosine"),
    },
    # ---- build lo: Pre-Calc U6 Applications of Trigonometry ---------------
    "arsn": {  # area from two sides and the angle between: half a b sin C
        "ans": lambda p: (p["a"] * p["b"] // 2 if p["c"] == 90
                          else p["a"] * p["b"] // 4),
        "spoken": lambda p: (f"A triangle has two sides of {p['a']} and "
                             f"{p['b']}, and the angle between them is "
                             f"{p['c']} degrees. What is its area?"),
        # Raw givens, in WORDS not a figure: the triangle renderer is
        # schematic, so a 150-degree angle would be drawn looking sharp --
        # and the praise calls that triangle wide. A picture that argues
        # with the speech is the le/topp defect; the teach keeps the figure
        # for the 90-degree case, where the drawing is honest.
        "board": _arsn_board,         # (tp) the honest SAS triangle (sas=); the schematic layout drew 150 looking sharp
        "worked": _arsn_worked,       # (tp) the same triangle with its area
        "praise": lambda p: ((f"The sine of 90 degrees is 1, so the area is "
                              f"half of {p['a']} times {p['b']} — "
                              f"{p['a'] * p['b'] // 2}. The whole "
                              f"{p['a'] * p['b']} is the rectangle around "
                              f"it, and a triangle takes half.")
                             if p["c"] == 90 else
                             (f"The sine of {p['c']} degrees is one half, "
                              f"so half the product is halved again — a "
                              f"quarter of {p['a']} times {p['b']}, which "
                              f"is {p['a'] * p['b'] // 4}."
                              + (" And 150 shares its sine with 30, so this "
                                 "wide triangle covers what the sharp one "
                                 "covers." if p["c"] == 150 else ""))),
        "key": lambda p: (p["a"] * p["b"] // 2 if p["c"] == 90
                          else p["a"] * p["b"] // 4),
        # The errors: the half forgotten (the whole rectangle), and the
        # WRONG sine used (1 where it is a half, or a half where it is 1).
        "choices": lambda p: [(p["a"] * p["b"] // 2 if p["c"] == 90
                               else p["a"] * p["b"] // 4),
                              p["a"] * p["b"],
                              (p["a"] * p["b"] // 4 if p["c"] == 90
                               else p["a"] * p["b"] // 2)],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["c"]) in sp),
        "check": lambda p: (p["c"] in (30, 90, 150)
                            and 2 <= p["a"] <= 12 and 2 <= p["b"] <= 12
                            and p["a"] * p["b"] % 4 == 0
                            and p["a"] * p["b"] <= 80
                            and len({p["a"] * p["b"] // 2,
                                     p["a"] * p["b"],
                                     p["a"] * p["b"] // 4}) == 3,
                            "a special angle, sides whose product quarters "
                            "cleanly, and three distinct taps"),
    },
    "ramp": {  # the 30-degree rise: height is HALF the ramp's length
        "ans": lambda p: p["a"] // 2,
        "spoken": lambda p: (f"A ramp {p['a']} feet long rises at 30 "
                             f"degrees above flat ground. How high is its "
                             f"top end?"),
        # The figure carries the givens; the height is a question mark.
        "board": _ramp_board,         # (tp) the ramp triangle, captioned (it had no caption -- rule 41)
        "worked": _ramp_worked,       # (tp) the height filled in
        "praise": lambda p: (f"The sine of 30 degrees is one half, so the "
                             f"ramp climbs half its length: half of "
                             f"{p['a']} equals {p['a'] // 2} feet. The "
                             f"{p['a']} is how far you walk up the slope, "
                             f"never how high you rise — and doubling "
                             f"instead would say {2 * p['a']}, higher than "
                             f"the ramp is long."),
        "key": lambda p: p["a"],
        # The errors: the length handed back as the height, and doubling
        # where the half belongs.
        "choices": lambda p: [p["a"] // 2, p["a"], 2 * p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (p["a"] % 2 == 0 and 6 <= p["a"] <= 40
                            and p["b"] == 0,
                            "an even length, so the half lands whole, and "
                            "no second number"),
    },
    "brng": {  # bearings: turn clockwise and wrap past the full turn
        "ans": lambda p: p["a"] + p["b"] - 360,
        "spoken": lambda p: (f"A ship sails on a bearing of {p['a']} "
                             f"degrees, then turns {p['b']} degrees "
                             f"clockwise. What is its new bearing?"),
        "board": _brng_board,         # (tp) the compass: the ship's arrow and the turn arc, its far end unnamed
        "worked": _brng_worked,       # (tp) the compass at the new bearing
        "praise": lambda p: (f"{p['a']} plus {p['b']} equals "
                             f"{p['a'] + p['b']} — past a full turn, so "
                             f"take away 360: the new bearing is "
                             f"{p['a'] + p['b'] - 360} degrees. "
                             f"{p['a'] + p['b']} names no bearing at all, "
                             f"and {p['a'] - p['b']} is where a backwards "
                             f"turn would have pointed."),
        "key": lambda p: p["a"] + p["b"],
        # The errors: the wrap forgotten (a bearing past 360), and the turn
        # taken the wrong way round.
        "choices": lambda p: [p["a"] + p["b"] - 360, p["a"] + p["b"],
                              p["a"] - p["b"]],
        "check": lambda p: (180 <= p["a"] <= 350 and 20 <= p["b"] <= 170
                            and p["a"] % 5 == 0 and p["b"] % 5 == 0
                            and p["a"] + p["b"] > 360 and p["a"] > p["b"]
                            and len({p["a"] + p["b"] - 360, p["a"] + p["b"],
                                     p["a"] - p["b"]}) == 3,
                            "the turn really does pass 360, the backwards "
                            "turn stays positive, and the taps differ"),
    },
    "vmag": {  # an arrow's length from its two steps (Pythagoras, vectors)
        "ans": lambda p: p["c"],
        "spoken": lambda p: (f"An arrow starts at the corner and goes "
                             f"{p['a']} steps to the right and {p['b']} "
                             f"steps up. How long is the arrow itself?"),
        # NOT [[vector]] on the ask -- that renderer PRINTS the magnitude.
        "board": _vmag_board,         # (tp) the two steps and the slanted side, captioned (it had no caption -- rule 41)
        "worked": _vmag_worked,       # (tp) the arrow drawn with its length
        "praise": lambda p: (f"Right {p['a']} and up {p['b']} meet at a "
                             f"right angle, so the arrow is the "
                             f"hypotenuse: {p['a']} squared is "
                             f"{p['a'] * p['a']}, {p['b']} squared is "
                             f"{p['b'] * p['b']}, put together "
                             f"{p['a'] * p['a'] + p['b'] * p['b']} — and "
                             f"{p['c']} times {p['c']} squares back to it. "
                             f"The arrow is {p['c']}: longer than either "
                             f"step, shorter than walking both."),
        "key": lambda p: p["c"],
        # The errors: the two steps added (walking the corner), and the
        # bigger step alone ("it is mostly up").
        "choices": lambda p: [p["c"], p["a"] + p["b"], max(p["a"], p["b"])],
        "check": lambda p: (p["a"] * p["a"] + p["b"] * p["b"]
                            == p["c"] * p["c"]
                            and 3 <= p["a"] <= 36 and 3 <= p["b"] <= 36
                            and 5 <= p["c"] <= 40
                            and len({p["c"], p["a"] + p["b"],
                                     max(p["a"], p["b"])}) == 3,
                            "a true triple with whole steps, and three "
                            "distinct taps"),
    },
    # ---- build lo: Pre-Calc U7 Conic Sections & Parametric Equations ------
    "crad": {  # circle equation -> radius: un-square the right-hand number
        "ans": lambda p: p["c"],
        "spoken": lambda p: (f"A circle is written: x take away {p['a']}, "
                             f"squared, plus y take away {p['b']}, "
                             f"squared, equals {p['c'] * p['c']}. What is "
                             f"the circle's radius?"),
        "board": _crad_board,         # (tq) the circle with its radius marked "?"
        "worked": _crad_worked,       # (tq) the circle on the grid, reaching its radius
        "praise": lambda p: (f"The number on the right is the radius "
                             f"SQUARED: un-square {p['c'] * p['c']} and "
                             f"the radius is {p['c']}. The {p['a']} and "
                             f"the {p['b']} name where the circle sits, "
                             f"never how big it is."),
        "key": lambda p: p["c"],
        # The errors: the squared number kept, and a center number grabbed.
        "choices": lambda p: [p["c"], p["c"] * p["c"], p["a"]],
        "check": lambda p: (2 <= p["c"] <= 12 and 1 <= p["a"] <= 12
                            and 1 <= p["b"] <= 12
                            and len({p["c"], p["c"] * p["c"],
                                     p["a"]}) == 3,
                            "a whole radius of at least 2, and three "
                            "distinct taps"),
    },
    "cctr": {  # circle equation -> the center's x: the minus points opposite
        "ans": lambda p: p["a"],
        "spoken": lambda p: (f"A circle is written: x take away {p['a']}, "
                             f"squared, plus y take away {p['b']}, "
                             f"squared, equals {p['c'] * p['c']}. What is "
                             f"the x of its center?"),
        "board": _cctr_board,         # (tq) the circle with its middle unnamed
        "worked": _cctr_worked,       # (tq) the circle on the grid at its middle
        "praise": lambda p: (f"x take away {p['a']} is zero exactly at x "
                             f"equals {p['a']}, and that is where the "
                             f"middle sits: the center's x is {p['a']}. "
                             f"The minus points opposite — take away "
                             f"{p['a']} means positive {p['a']}, never "
                             f"negative {p['a']}."),
        "key": lambda p: p["a"],
        # The errors: the sign flip (vtx2's and fdom's classic), and the
        # y-number answered instead.
        "choices": lambda p: [p["a"], -p["a"], p["b"]],
        "check": lambda p: (2 <= p["a"] <= 12 and 1 <= p["b"] <= 12
                            and 2 <= p["c"] <= 9 and p["a"] != p["b"]
                            and len({p["a"], -p["a"], p["b"]}) == 3,
                            "the two center numbers differ, so the "
                            "wrong-coordinate tap is visible"),
    },
    "elax": {  # ellipse: the number under x^2 un-squares to the HALF width
        "ans": lambda p: 2 * p["a"],
        "spoken": lambda p: (f"An ellipse is written: x squared over "
                             f"{p['a'] * p['a']}, plus y squared over "
                             f"{p['b'] * p['b']}, equals 1. How wide is it "
                             f"from its left edge to its right edge?"),
        "board": _elax_board,         # (tq) the two reaches as a tape, both blank
        "worked": _elax_worked,       # (tq) the ellipse on the grid and the tape filled
        "praise": lambda p: (f"The number under x squared is the "
                             f"half-width SQUARED: un-square "
                             f"{p['a'] * p['a']} and the ellipse reaches "
                             f"{p['a']} each way from the middle. Edge to "
                             f"edge is double that — {2 * p['a']}."),
        "key": lambda p: p["a"],
        # The errors: the half-width answered (the reach one way), and the
        # printed number handed back un-squared.
        "choices": lambda p: [2 * p["a"], p["a"], p["a"] * p["a"]],
        "speaks": lambda p, sp: (str(p["a"] * p["a"]) in sp
                                 and str(p["b"] * p["b"]) in sp),
        "check": lambda p: (3 <= p["a"] <= 10 and 2 <= p["b"] <= 10
                            and p["a"] != p["b"]
                            and len({2 * p["a"], p["a"],
                                     p["a"] * p["a"]}) == 3,
                            "a real ellipse whose half-width, width and "
                            "printed number are three different numbers"),
    },
    "parm": {  # parametric motion: plug the time, then the straight distance
        "ans": lambda p: p["c"] * round((p["a"] * p["a"]
                                         + p["b"] * p["b"]) ** 0.5),
        "spoken": lambda p: (f"A ball's path: x equals {p['a']} times t, "
                             f"and y equals {p['b']} times t, with t in "
                             f"seconds. At t equals {p['c']} seconds, how "
                             f"far is the ball from its start?"),
        "board": _parm_board,         # (tq) the path with the t = 1 point
        "worked": _parm_worked,       # (tq) the vector at time t (it prints the length)
        "praise": lambda p: (lambda h:
                             f"At {p['c']} seconds x is {p['a'] * p['c']} "
                             f"and y is {p['b'] * p['c']} — those two are "
                             f"the legs, and the straight distance is "
                             f"{h * p['c']}. Each second covers {h}, so "
                             f"{h} alone is one second's worth, not the "
                             f"whole {p['c']} seconds. Adding the two legs "
                             f"walks the corner: "
                             f"{(p['a'] + p['b']) * p['c']}.")
                            (round((p["a"] * p["a"]
                                    + p["b"] * p["b"]) ** 0.5)),
        "key": lambda p: p["c"] * round((p["a"] * p["a"]
                                         + p["b"] * p["b"]) ** 0.5),
        # The errors: the corner walked (legs added), and the ONE-SECOND
        # distance handed back -- speed mistaken for distance.
        "choices": lambda p: (lambda h: [p["c"] * h,
                                         (p["a"] + p["b"]) * p["c"], h])
                             (round((p["a"] * p["a"]
                                     + p["b"] * p["b"]) ** 0.5)),
        "check": lambda p: (lambda h:
                            (h * h == p["a"] * p["a"] + p["b"] * p["b"]
                             and 3 <= p["a"] <= 20 and 3 <= p["b"] <= 20
                             and 2 <= p["c"] <= 5 and h * p["c"] <= 40,
                             "a whole one-second distance, at least two "
                             "seconds gone, and the trip stays under 40"))
                           (round((p["a"] * p["a"]
                                   + p["b"] * p["b"]) ** 0.5)),
    },
    # ---- build lp: Pre-Calc U8 Sequences, Series & the Binomial Theorem ---
    "gsum": {  # a FINITE geometric sum: the run of terms, added up
        "ans": lambda p: (p["a"] * (p["b"] ** p["c"] - 1) // (p["b"] - 1)),
        "spoken": lambda p: (f"A pattern starts at {p['a']}, and each term "
                             f"is {p['b']} times the one before. Put the "
                             f"first {p['c']} terms together. What is the "
                             f"sum?"),
        # Raw givens: start, ratio, how many. Writing the terms out would do
        # the adding for them.
        "board": _gsum_board,         # (tq) the pattern's machine (writing the terms would do the adding)
        "worked": _gsum_worked,       # (tq) the terms as bars, added
        "praise": lambda p: (f"The terms are "
                             + ", ".join(str(p["a"] * p["b"] ** i)
                                         for i in range(p["c"]))
                             + f" — put together, "
                             f"{p['a'] * (p['b'] ** p['c'] - 1) // (p['b'] - 1)}. "
                             f"The last term alone is only "
                             f"{p['a'] * p['b'] ** (p['c'] - 1)}, and a "
                             f"pattern that never grew would have stopped "
                             f"at {p['a'] * p['c']}."),
        "key": lambda p: (p["a"] * (p["b"] ** p["c"] - 1) // (p["b"] - 1)),
        # The errors: the LAST TERM handed back as the sum, and the
        # arithmetic habit -- the start counted c times.
        "choices": lambda p: [(p["a"] * (p["b"] ** p["c"] - 1)
                               // (p["b"] - 1)),
                              p["a"] * p["b"] ** (p["c"] - 1),
                              p["a"] * p["c"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["c"]) in sp),
        "check": lambda p: (p["b"] in (2, 3) and 2 <= p["a"] <= 6
                            and 3 <= p["c"] <= 5
                            and (p["a"] * (p["b"] ** p["c"] - 1)
                                 // (p["b"] - 1)) <= 100
                            and len({(p["a"] * (p["b"] ** p["c"] - 1)
                                      // (p["b"] - 1)),
                                     p["a"] * p["b"] ** (p["c"] - 1),
                                     p["a"] * p["c"]}) == 3,
                            "a friendly ratio, at least three terms, a sum "
                            "at 100 or under, and three distinct taps"),
    },
    "sigm": {  # sigma notation read as an instruction: sum of a*k, k = 1..b
        "ans": lambda p: p["a"] * p["b"] * (p["b"] + 1) // 2,
        "spoken": lambda p: (f"Read this instruction: the sum, for k going "
                             f"from 1 up to {p['b']}, of {p['a']} times k. "
                             f"What is the sum?"),
        "board": _sigm_board,         # (tq) the recipe machine
        "worked": _sigm_worked,       # (tq) the terms as bars
        "praise": lambda p: (f"Every term carries the {p['a']}, so pull it "
                             f"out front: 1 up to {p['b']} sums to "
                             f"{p['b'] * (p['b'] + 1) // 2}, and {p['a']} "
                             f"times that is "
                             f"{p['a'] * p['b'] * (p['b'] + 1) // 2}. The "
                             f"bare sum {p['b'] * (p['b'] + 1) // 2} forgot "
                             f"the {p['a']}, and {p['a'] * p['b']} is only "
                             f"the last term."),
        "key": lambda p: p["a"] * p["b"] * (p["b"] + 1) // 2,
        # The errors: the multiplier dropped (Gauss's bare sum), and the
        # LAST TERM answered instead of the sum.
        "choices": lambda p: [p["a"] * p["b"] * (p["b"] + 1) // 2,
                              p["b"] * (p["b"] + 1) // 2,
                              p["a"] * p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 3 <= p["b"] <= 12
                            and p["a"] * p["b"] * (p["b"] + 1) // 2 <= 200
                            and len({p["a"] * p["b"] * (p["b"] + 1) // 2,
                                     p["b"] * (p["b"] + 1) // 2,
                                     p["a"] * p["b"]}) == 3,
                            "the sum stays at 200 or under, and the full "
                            "sum, the bare sum and the last term differ"),
    },
    "pasc": {  # n choose k: the count when ORDER does not matter
        "ans": lambda p: (_ncr(p["a"], p["b"])),
        "spoken": lambda p: (f"A team of {p['b']} is chosen from {p['a']} "
                             f"people, and the order they are picked in "
                             f"does not matter. How many different teams "
                             f"are possible?"),
        "board": _pasc_board,         # (tq) the crowd as an array
        "worked": _pasc_worked,       # (tq) line-ups beside teams
        "praise": lambda p: (f"Picking in order would give "
                             f"{_npr(p['a'], p['b'])} line-ups, but every "
                             f"team of {p['b']} shows up "
                             f"{_fact(p['b'])} times in that list — once "
                             f"per order. Divide: "
                             f"{_npr(p['a'], p['b'])} divided by "
                             f"{_fact(p['b'])} equals "
                             f"{_ncr(p['a'], p['b'])} teams."),
        "key": lambda p: _ncr(p["a"], p["b"]),
        # The errors: ORDER counted (the line-up count), and the crowd size
        # handed back.
        "choices": lambda p: [_ncr(p["a"], p["b"]), _npr(p["a"], p["b"]),
                              p["a"]],
        "check": lambda p: (4 <= p["a"] <= 10 and p["b"] in (2, 3)
                            and _ncr(p["a"], p["b"]) <= 100
                            and len({_ncr(p["a"], p["b"]),
                                     _npr(p["a"], p["b"]), p["a"]}) == 3,
                            "a small crowd, teams of two or three, and the "
                            "team count, the line-up count and the crowd "
                            "are three different numbers"),
    },
    "gser": {  # the INFINITE halving series: it settles on twice the first
        "ans": lambda p: 2 * p["a"],
        "spoken": lambda p: (f"A ball's first bounce carries it {p['a']} "
                             f"feet, and every bounce after that carries it "
                             f"half as far — forever. How far does it "
                             f"travel in all?"),
        "board": _gser_board,         # (tq) the first three bounces as bars
        "worked": _gser_worked,       # (tq) the hops that each cover half of what is left
        "praise": lambda p: (f"Add forever and it still settles: {p['a']} "
                             f"plus {p['a'] // 2} plus {p['a'] // 4}, on "
                             f"and on, closes in on {2 * p['a']} — twice "
                             f"the first bounce, and never a foot more. "
                             f"{p['a']} is the first bounce alone, and "
                             f"{p['a'] // 2} is only the second."),
        "key": lambda p: p["a"],
        # The errors: the first bounce alone, and the second one.
        "choices": lambda p: [2 * p["a"], p["a"], p["a"] // 2],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (p["a"] % 4 == 0 and 8 <= p["a"] <= 60
                            and p["b"] == 0,
                            "a first bounce that halves twice cleanly, so "
                            "the written-out sum stays whole"),
    },
    # ---- build lp: Pre-Calc U9 Introduction to Limits ---------------------
    "lsub": {  # the friendly limit: walk x in, and the value walks in too
        "ans": lambda p: p["a"] * p["b"] + p["c"],
        "spoken": lambda p: (f"As x creeps closer and closer to {p['a']}, "
                             f"what number does {p['b']} x plus {p['c']} "
                             f"creep toward?"),
        "board": _lsub_board,         # (tq) the line that never breaks
        "worked": _lsub_worked,       # (tq) the point walked in
        "praise": lambda p: (f"Nothing breaks at x equals {p['a']}, so the "
                             f"value walks in with x: {p['b']} times "
                             f"{p['a']} is {p['a'] * p['b']}, plus "
                             f"{p['c']} — {p['a'] * p['b'] + p['c']}. For a "
                             f"line, the limit is simply where the line "
                             f"already is."),
        "key": lambda p: p["a"] * p["b"] + p["c"],
        # The errors: x itself handed back, and the times read as a plus.
        "choices": lambda p: [p["a"] * p["b"] + p["c"], p["a"],
                              p["b"] + p["c"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["c"]) in sp),
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and 1 <= p["c"] <= 9
                            and p["a"] * p["b"] + p["c"] <= 90
                            and len({p["a"] * p["b"] + p["c"], p["a"],
                                     p["b"] + p["c"]}) == 3,
                            "small whole numbers, and the value, the x and "
                            "the added pair are three different taps"),
    },
    "lhol": {  # the hole: undefined AT the point, perfectly clear around it
        "ans": lambda p: 2 * p["a"],
        "spoken": lambda p: (f"y equals: x squared take away "
                             f"{p['a'] * p['a']}, all divided by x take "
                             f"away {p['a']}. At x equals {p['a']} it is "
                             f"undefined. As x creeps toward {p['a']}, what "
                             f"number does y creep toward?"),
        "board": _lhol_board,         # (tq) the machine that jams at the hole (the curve's hole sits at the answer -- walk-back only)
        "worked": _lhol_worked,       # (tq) the line with its hole
        "praise": lambda p: (f"Everywhere except {p['a']}, that fraction "
                             f"quietly equals x plus {p['a']} — so as x "
                             f"creeps toward {p['a']}, y creeps toward "
                             f"{2 * p['a']}. The function has a hole there "
                             f"and never reaches the value; the limit says "
                             f"where it was headed."),
        "key": lambda p: p["a"],
        # The errors: the forbidden x itself, and "undefined must mean
        # zero".
        "choices": lambda p: [2 * p["a"], p["a"], 0],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (2 <= p["a"] <= 20 and p["b"] == 0,
                            "a whole hole between 2 and 20, and no second "
                            "number"),
    },
    "lsid": {  # one-sided limits: the two sides can disagree
        "ans": lambda p: (p["a"] if p["c"] == 0 else p["b"]),
        "spoken": lambda p: (f"y is {p['a']} when x is below 6, and "
                             f"{p['b']} when x is 6 or more. Creeping up on "
                             f"6 from the "
                             + ("LEFT" if p["c"] == 0 else "RIGHT")
                             + ", what value does y creep toward?"),
        "board": _lsid_board,         # (tq) the step with its two heights
        "worked": _lsid_worked,       # (tq) the approach marked
        "praise": lambda p: ((f"From the left, every x is below 6, so y is "
                              f"{p['a']} the whole way in — the limit from "
                              f"that side is {p['a']}. The other side would "
                              f"say {p['b']}, and the two do not have to "
                              f"agree.")
                             if p["c"] == 0 else
                             (f"From the right, every x is 6 or more, so y "
                              f"is {p['b']} the whole way in — the limit "
                              f"from that side is {p['b']}. The other side "
                              f"would say {p['a']}, and the two do not have "
                              f"to agree.")),
        "key": lambda p: p["a"] + p["b"],
        # The errors: the OTHER side's value, and splitting the difference
        # -- a limit is not an average.
        "choices": lambda p: [(p["a"] if p["c"] == 0 else p["b"]),
                              (p["b"] if p["c"] == 0 else p["a"]),
                              (p["a"] + p["b"]) // 2],
        "check": lambda p: (2 <= p["a"] <= 30 and 2 <= p["b"] <= 30
                            and (p["a"] + p["b"]) % 2 == 0
                            and abs(p["a"] - p["b"]) >= 4
                            and 6 not in (p["a"], p["b"])
                            and p["c"] in (0, 1),
                            "two clearly different heights whose midpoint "
                            "lands whole, neither of them 6 -- that is the "
                            "border's own number -- so all three taps are "
                            "visible and nothing reads twice"),
    },
    "avgr": {  # average rate of change of x^2 -- the derivative, previewed
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"On the curve y equals x squared, x moves "
                             f"from {p['a']} to {p['b']}. For each step of "
                             f"x, how much does y rise on average?"),
        "board": _avgr_board,         # (tq) the window on the curve
        "worked": _avgr_worked,       # (tq) the line through the two points
        "praise": lambda p: (f"y climbs from {p['a'] * p['a']} to "
                             f"{p['b'] * p['b']} — a rise of "
                             f"{p['b'] * p['b'] - p['a'] * p['a']} — while "
                             f"x moves {p['b'] - p['a']}. Divide: "
                             f"{p['a'] + p['b']} per step, which is simply "
                             f"{p['a']} plus {p['b']}. The rise alone and "
                             f"the run alone are only halves of the "
                             f"story."),
        "key": lambda p: p["a"] + p["b"],
        # The errors: the RUN alone, and the RISE alone -- the two halves of
        # a slope, each mistaken for the whole.
        "choices": lambda p: [p["a"] + p["b"], p["b"] - p["a"],
                              p["b"] * p["b"] - p["a"] * p["a"]],
        "check": lambda p: (1 <= p["a"] and p["a"] + 2 <= p["b"] <= 12
                            and len({p["a"] + p["b"], p["b"] - p["a"],
                                     p["b"] * p["b"]
                                     - p["a"] * p["a"]}) == 3,
                            "a window at least two wide, so the slope, the "
                            "run and the rise are three different numbers"),
    },
    # ---- build lq: Probability & Statistics U1 Exploring Data -------------
    "dotm": {  # the MODE off a dot plot: the value under the stack, not the count
        "ans": lambda p: p["a"],
        "spoken": lambda p: ("This dot plot shows how many books each reader "
                             "read last month. Which number of books is the "
                             "MODE — the number that happened most often?"),
        "board": _dotm_board,         # (tr) the dot plot, captioned (it had no caption -- rule 41)
        "worked": _dotm_worked,       # (tr) the tallest stack named
        "praise": lambda p: (f"The tallest stack sits over {p['a']}, and it "
                             f"holds {p['b']} dots — so {p['b']} readers "
                             f"read {p['a']} books each. The mode is the "
                             f"value UNDER the stack, {p['a']}, never the "
                             f"{p['b']} readers standing on it."),
        "key": lambda p: p["a"],
        # The errors: the COUNT answered instead of the value (the classic),
        # and the biggest value on the line.
        "choices": lambda p: [p["a"], p["b"], p["a"] + 2],
        # Every number lives on the board; the question names none of them.
        "speaks": lambda p, sp: True,
        "check": lambda p: (5 <= p["a"] <= 20 and 3 <= p["b"] <= 6
                            and len({p["a"], p["b"], p["a"] + 2}) == 3,
                            "a clear tallest stack, and the value, the count "
                            "and the top of the line are three different "
                            "taps"),
    },
    "dcnt": {  # counting a SLICE of a dot plot, with a dot on the line itself
        "ans": lambda p: p["b"],
        "spoken": lambda p: (f"This dot plot shows the goals each player "
                             f"scored. How many players scored MORE than "
                             f"{p['a']} goals?"),
        "board": _dcnt_board,         # (tr) the dot plot captioned; the pending line a statement (the old "how many players?" was a question inside a step)
        "worked": _dcnt_worked,       # (tr) the dots past the line counted
        "praise": lambda p: (f"Count only the dots to the RIGHT of {p['a']}: "
                             f"there are {p['b']}. The dot standing exactly "
                             f"on {p['a']} does not join them — {p['a']} is "
                             f"not more than {p['a']} — and the {p['c']} "
                             f"dots below answer the opposite question."),
        "key": lambda p: p["b"],
        # The errors: the dot ON the line counted too, and the other side
        # counted.
        "choices": lambda p: [p["b"], p["b"] + 1, p["c"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (5 <= p["a"] <= 20 and 4 <= p["b"] <= 8
                            and 3 <= p["c"] <= 9
                            and len({p["b"], p["b"] + 1, p["c"]}) == 3,
                            "dots on both sides and one on the line, and "
                            "three distinct taps"),
    },
    "htot": {  # how many in all, from a histogram: add the printed bars
        "ans": lambda p: p["a"] + p["b"] + p["c"],
        "spoken": lambda p: ("This histogram sorts the scores into groups, "
                             "and each bar carries its count printed on "
                             "top. How many scores are shown in all?"),
        "board": _htot_board,         # (tr) the histogram captioned; the pending line a statement (the old "how many scores in all?" was a question inside a step)
        "worked": _htot_worked,       # (tr) the bars added
        "praise": lambda p: (f"Add the bars: {p['a']} plus {p['b']} plus "
                             f"{p['c']} equals {p['a'] + p['b'] + p['c']}. "
                             f"The tallest bar alone holds only "
                             f"{max(p['a'], p['b'], p['c'])}, and the "
                             f"number of bars is not the number of "
                             f"scores."),
        "key": lambda p: p["a"] + p["b"] + p["c"],
        # The errors: the tallest bar answered, and the BARS counted instead
        # of what stands in them.
        "choices": lambda p: [p["a"] + p["b"] + p["c"],
                              max(p["a"], p["b"], p["c"]), 3],
        "speaks": lambda p, sp: True,
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and 2 <= p["c"] <= 9
                            and p["a"] + p["b"] + p["c"] <= 27
                            and len({p["a"] + p["b"] + p["c"],
                                     max(p["a"], p["b"], p["c"]), 3}) == 3,
                            "three readable bars whose sum, tallest bar and "
                            "bar count are three different numbers"),
    },
    "farv": {  # SPOTTING the outlier -- alg1's outl showed what one does
        "ans": lambda p: p["b"],
        "spoken": lambda p: ("This dot plot shows how many minutes each "
                             "child took. One value sits far away from all "
                             "the others — the outlier. What is that "
                             "value?"),
        "board": _farv_board,         # (tr) the dot plot, captioned (it had no caption -- rule 41)
        "worked": _farv_worked,       # (tr) the stray named
        "praise": lambda p: (f"Nearly every dot crowds around {p['a']}, and "
                             f"one sits alone out at {p['b']} — that stray "
                             f"is the outlier. {p['a']} is where the crowd "
                             f"is, and {p['b'] - p['a']} is only how far "
                             f"the stray sits from it."),
        "key": lambda p: p["b"],
        # The errors: the CROWD's value, and the GAP between them.
        "choices": lambda p: [p["b"], p["a"], p["b"] - p["a"]],
        "speaks": lambda p, sp: True,
        "check": lambda p: (5 <= p["a"] <= 15 and p["a"] + 12 <= p["b"] <= 40
                            and len({p["b"], p["a"],
                                     p["b"] - p["a"]}) == 3,
                            "a stray far enough out to be unmistakable, and "
                            "three distinct taps"),
    },
    # ---- build lq: Probability & Statistics U2 Describing Distributions ---
    "medv": {  # the median of an EVEN list: halfway between the two middles
        "ans": lambda p: p["b"] + 1,
        "spoken": lambda p: (f"Here are {2 * p['a']} numbers, smallest "
                             f"first: {_evenlist_words(p)}. What is the "
                             f"median?"),
        "board": _medv_board,         # (tr) the even list as a dot plot, captioned
        "worked": _medv_worked,       # (tr) the two middles on the number line with the halfway mark
        "praise": lambda p: (f"An even count has no one middle: {p['b']} "
                             f"and {p['b'] + 2} both sit there, with the "
                             f"rest split evenly either side of the pair. "
                             f"The median is halfway between them — "
                             f"{p['b'] + 1} — and neither middle on its own "
                             f"is the answer."),
        "key": lambda p: p["b"],
        # The errors: the lower middle, and the upper one.
        "choices": lambda p: [p["b"] + 1, p["b"], p["b"] + 2],
        "speaks": lambda p, sp: str(p["b"]) in sp,
        "check": lambda p: (2 <= p["a"] <= 4
                            and p["b"] - 2 * (p["a"] - 1) >= 2
                            and p["b"] <= 24,
                            "an even list that stays positive, with two "
                            "middles two apart"),
    },
    "iqrw": {  # the BOX's width: the middle half, not the whole stretch
        "ans": lambda p: p["b"] - p["a"],
        "spoken": lambda p: (f"On this box plot the box runs from {p['a']} "
                             f"to {p['b']}, and the whiskers reach out to "
                             f"{p['a'] - p['c']} and {p['b'] + p['c']}. How "
                             f"wide is the BOX — the middle half of the "
                             f"data?"),
        "board": _iqrw_board,         # (tr) the box plot, captioned (it had no caption -- rule 41)
        "worked": _iqrw_worked,       # (tr) the box measured
        "praise": lambda p: (f"The box holds the middle half, from {p['a']} "
                             f"to {p['b']}: {p['b']} take away {p['a']} "
                             f"equals {p['b'] - p['a']}. Whisker tip to "
                             f"whisker tip is {p['b'] + p['c'] - p['a'] + p['c']} "
                             f"— that is the whole stretch, a different "
                             f"measurement, and {p['b']} alone is just the "
                             f"box's right edge."),
        "key": lambda p: p["b"] - p["a"],
        # The errors: the WHOLE range (whisker to whisker), and the box's
        # right edge read as its width.
        "choices": lambda p: [p["b"] - p["a"],
                              (p["b"] + p["c"]) - (p["a"] - p["c"]),
                              p["b"]],
        "check": lambda p: (5 <= p["a"] and p["a"] + 4 <= p["b"]
                            and p["b"] <= p["a"] + 20
                            and 2 <= p["c"] <= 6
                            and (p["a"] + p["b"]) % 2 == 0
                            and p["b"] + p["c"] <= 60
                            and len({p["b"] - p["a"],
                                     (p["b"] + p["c"]) - (p["a"] - p["c"]),
                                     p["b"]}) == 3,
                            "a real box with whiskers either side, a whole "
                            "median to print, and three distinct taps"),
    },
    "madv": {  # the average distance from the mean -- deviation, in child form
        "ans": lambda p: 2 * p["b"],
        "spoken": lambda p: (f"Four numbers — {_madlist_words(p)} — have a "
                             f"mean of {p['a']}. On average, how far from "
                             f"that mean does a number sit?"),
        "board": _madv_board,         # (tr) the four numbers as a dot plot, captioned
        "worked": _madv_worked,       # (tr) the four distances as bars
        "praise": lambda p: (f"The four distances are {3 * p['b']}, "
                             f"{p['b']}, {p['b']} and {3 * p['b']} — put "
                             f"together {8 * p['b']}, shared between 4: "
                             f"{2 * p['b']}. The farthest number sits "
                             f"{3 * p['b']} away and the nearest {p['b']}, "
                             f"so the average distance lies between them."),
        "key": lambda p: 2 * p["b"],
        # The errors: the FARTHEST distance, and the nearest -- the typical
        # distance mistaken for one of the extremes.
        "choices": lambda p: [2 * p["b"], 3 * p["b"], p["b"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (2 <= p["b"] <= 6 and p["a"] - 3 * p["b"] >= 2
                            and p["a"] <= 30,
                            "four numbers spread evenly either side of the "
                            "mean, all of them positive"),
    },
    "pctl": {  # a percentile is a PERCENT of the class, not a headcount
        "ans": lambda p: p["a"] * p["b"] // 100,
        "spoken": lambda p: (f"A swimmer raced against {p['a']} others and "
                             f"finished at the {p['b']}th percentile — faster "
                             f"than {p['b']} percent of them. How many of the "
                             f"{p['a']} did she beat?"),
        "board": _pctl_board,         # (tr) the hundred square as a percent; the pending line a statement (the old "how many beaten = ?" was a question inside a step)
        "worked": _pctl_worked,       # (tr) beaten beside above
        "praise": lambda p: (f"{p['b']} percent of {p['a']} is "
                             f"{p['a'] * p['b'] // 100}, so she beat "
                             f"{p['a'] * p['b'] // 100} of them. The "
                             f"{p['b']} is a PERCENT, never a headcount — "
                             f"and the other "
                             f"{p['a'] - p['a'] * p['b'] // 100} finished "
                             f"ahead of her."),
        "key": lambda p: p["a"] * p["b"] // 100,
        # The errors: the percentile read as a count of people, and the
        # OTHER side of the class counted.
        "choices": lambda p: [p["a"] * p["b"] // 100, p["b"],
                              p["a"] - p["a"] * p["b"] // 100],
        "check": lambda p: (20 <= p["a"] <= 60 and 10 <= p["b"] <= 90
                            and p["b"] % 5 == 0
                            and p["a"] * p["b"] % 100 == 0
                            and len({p["a"] * p["b"] // 100, p["b"],
                                     p["a"] - p["a"] * p["b"] // 100}) == 3,
                            "a percentile that lands on a whole classmate, "
                            "and three distinct taps"),
    },
    # ---- build lr: Prob & Stats U3 Scatterplots & Correlation ------------
    "spnt": {  # read ONE dot off a scatterplot -- the axes are the trap
        "ans": lambda p: _scat_at(p),
        "spoken": lambda p: (f"On this scatterplot each dot is one child: "
                             f"hours practiced across the bottom, points "
                             f"scored up the side. One child practiced "
                             f"{p['a']} hours. How many points did that "
                             f"child score?"),
        "board": _spnt_board,         # (tr) the scatter cloud, captioned (it had no caption -- rule 41)
        "worked": _spnt_worked,       # (tr) the dot read
        "praise": lambda p: (f"Find {p['a']} along the bottom, go straight "
                             f"up to the dot, then straight across: "
                             f"{_scat_at(p)} points. The {p['a']} is how "
                             f"long the child practiced — across, not up — "
                             f"and {_scat_next(p)} belongs to the "
                             f"neighbouring dot."),
        "key": lambda p: p["a"],
        # The errors: the x answered instead of the y (the axis mix-up), and
        # the dot next door read by mistake.
        "choices": lambda p: [_scat_at(p), p["a"], _scat_next(p)],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (p["a"] in _SCAT_X and 2 <= p["c"] <= 4
                            and p["b"] == 0
                            and min(_scat_ys(p)) >= 1
                            and len({_scat_at(p), p["a"],
                                     _scat_next(p)}) == 3,
                            "a dot really on the plot, a cloud that stays "
                            "positive, and three distinct taps"),
    },
    "sslp": {  # the fit line's slope USED -- a rate, over several steps
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: (f"A scatterplot's best-fit line climbs "
                             f"{p['a']} points for every extra hour of "
                             f"practice. Nadia practices {p['b']} hours "
                             f"more than Omar. How many more points would "
                             f"you predict for Nadia?"),
        "board": _sslp_board,         # (tr) the rate machine
        "worked": _sslp_worked,       # (tr) the line climbing, the point marked
        "praise": lambda p: (f"The slope is a rate: {p['a']} points EACH "
                             f"hour, so {p['b']} hours brings {p['b']} "
                             f"times {p['a']} — {p['a'] * p['b']} points. "
                             f"{p['a']} alone is one hour's worth, and "
                             f"adding the two numbers treats a rate like a "
                             f"total."),
        "key": lambda p: p["a"] * p["b"],
        # The errors: one hour's worth handed back, and the rate ADDED to
        # the hours instead of timesed by them.
        "choices": lambda p: [p["a"] * p["b"], p["a"], p["a"] + p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and p["a"] * p["b"] <= 81
                            and len({p["a"] * p["b"], p["a"],
                                     p["a"] + p["b"]}) == 3,
                            "a real rate over real steps, and the total, "
                            "the rate and their sum all differ"),
    },
    "resd": {  # the residual: how far the truth sits from the prediction
        "ans": lambda p: abs(p["b"] - p["a"]),
        "spoken": lambda p: (f"A best-fit line predicted {p['a']} points "
                             f"for Sam. Sam actually scored {p['b']}. How "
                             f"far off was the prediction?"),
        "board": _resd_board,         # (tr) predicted beside actual as bars
        "worked": _resd_worked,       # (tr) the gap as a hop on the number line
        "praise": lambda p: (f"The gap between {p['a']} and {p['b']} is "
                             f"{abs(p['b'] - p['a'])} — that gap has a "
                             f"name, the residual, and every dot has one. "
                             f"{p['b']} is what Sam scored, not how far the "
                             f"line missed by, and putting the two numbers "
                             f"together answers nothing at all."),
        "key": lambda p: abs(p["b"] - p["a"]),
        # The errors: the actual score handed back, and the two numbers
        # added.
        "choices": lambda p: [abs(p["b"] - p["a"]), p["b"], p["a"] + p["b"]],
        "check": lambda p: (5 <= p["a"] <= 60 and 5 <= p["b"] <= 60
                            and abs(p["b"] - p["a"]) >= 2
                            and len({abs(p["b"] - p["a"]), p["b"],
                                     p["a"] + p["b"]}) == 3,
                            "a real miss of at least 2, and three distinct "
                            "taps"),
    },
    "sblw": {  # the fit line runs THROUGH the cloud, so both sides are full
        "ans": lambda p: p["a"] - p["b"],
        "spoken": lambda p: (f"A best-fit line is drawn through a "
                             f"scatterplot's {p['a']} dots, and no dot "
                             f"lands exactly on it. {p['b']} of the dots "
                             f"sit above the line. How many sit below it?"),
        "board": _sblw_board,         # (tr) the dots as a tape, the below part blank
        "worked": _sblw_worked,       # (tr) both parts of the tape
        "praise": lambda p: (f"The line runs THROUGH the cloud, so every "
                             f"dot is on one side or the other: {p['a']} "
                             f"take away {p['b']} leaves "
                             f"{p['a'] - p['b']} below. {p['b']} is the "
                             f"side you were told about, and {p['a']} is "
                             f"every dot on the plot."),
        "key": lambda p: p["a"],
        # The errors: the given side echoed back, and the whole cloud.
        "choices": lambda p: [p["a"] - p["b"], p["b"], p["a"]],
        "check": lambda p: (8 <= p["a"] <= 20 and 2 <= p["b"] <= p["a"] - 2
                            and p["a"] - p["b"] != p["b"],
                            "dots on both sides, and the two sides do not "
                            "hold the same number"),
    },
    # ---- build lr: Prob & Stats U4 Collecting Data ------------------------
    "strf": {  # a sample that keeps the school's own mix
        "ans": lambda p: p["c"] * p["a"] // (p["a"] + p["b"]),
        "spoken": lambda p: (f"A school has {p['a']} girls and {p['b']} "
                             f"boys. A sample of {p['c']} students is built "
                             f"to keep the same mix. How many girls should "
                             f"it include?"),
        "board": _strf_board,         # (tt) the school as bars, the sample as a tape cut the same way
        "worked": _strf_worked,       # (tt) the tape filled in
        "praise": lambda p: (f"Girls are {p['a']} of {p['a'] + p['b']} in "
                             f"the school, so the sample keeps that share: "
                             f"{p['c']} times {p['a']} divided by "
                             f"{p['a'] + p['b']} equals "
                             f"{p['c'] * p['a'] // (p['a'] + p['b'])} "
                             f"girls. Splitting the sample down the middle "
                             f"would say {p['c'] // 2}, which only matches "
                             f"a school that is half and half."),
        "key": lambda p: p["c"] * p["a"] // (p["a"] + p["b"]),
        # The errors: half and half whatever the school looks like, and the
        # school's own girl count copied into the sample.
        "choices": lambda p: [p["c"] * p["a"] // (p["a"] + p["b"]),
                              p["c"] // 2, p["a"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["c"]) in sp),
        "check": lambda p: (20 <= p["a"] <= 90 and 20 <= p["b"] <= 90
                            and p["a"] != p["b"]
                            and 10 <= p["c"] <= 40
                            and p["c"] < p["a"] + p["b"]
                            and (p["c"] * p["a"]) % (p["a"] + p["b"]) == 0
                            and p["c"] % 2 == 0
                            and len({p["c"] * p["a"] // (p["a"] + p["b"]),
                                     p["c"] // 2, p["a"]}) == 3,
                            "a school that is not half and half, a sample "
                            "share that lands on whole children, and three "
                            "distinct taps"),
    },
    "resp": {  # the response rate: what percent actually came back
        "ans": lambda p: 100 * p["b"] // p["a"],
        "spoken": lambda p: (f"{p['a']} surveys went out and {p['b']} came "
                             f"back. What percent of them came back?"),
        "board": _resp_board,         # (tt) back and silent as a tape
        "worked": _resp_worked,       # (tt) the rate on the hundred square
        "praise": lambda p: (f"{p['b']} out of {p['a']} is "
                             f"{100 * p['b'] // p['a']} percent — that is "
                             f"the response rate, and a low one is a "
                             f"warning: the people who never answer may not "
                             f"think like the people who did. {p['b']} is a "
                             f"count of surveys, and "
                             f"{p['a'] - p['b']} is how many stayed out "
                             f"there."),
        "key": lambda p: 100 * p["b"] // p["a"],
        # The errors: the COUNT returned given as a percent, and the count
        # that never came back.
        "choices": lambda p: [100 * p["b"] // p["a"], p["b"],
                              p["a"] - p["b"]],
        "check": lambda p: (20 <= p["a"] <= 200 and 2 <= p["b"] < p["a"]
                            and (100 * p["b"]) % p["a"] == 0
                            and 100 * p["b"] // p["a"] >= 10
                            and len({100 * p["b"] // p["a"], p["b"],
                                     p["a"] - p["b"]}) == 3,
                            "a rate that lands on a whole percent, and "
                            "three distinct taps"),
    },
    "bias": {  # undercoverage: who never had a chance of being asked at all
        "ans": lambda p: p["b"] - p["a"],
        "spoken": lambda p: (f"A lunch survey is handed only to the "
                             f"{p['a']} in the cafeteria, in a school of "
                             f"{p['b']}. How many of the whole school never "
                             f"had a chance to be asked?"),
        "board": _bias_board,         # (tt) the asked and the never-asked as a tape, the second part blank
        "worked": _bias_worked,       # (tt) both parts
        "praise": lambda p: (f"{p['b']} take away {p['a']} leaves "
                             f"{p['b'] - p['a']} it could never reach — and "
                             f"the ones who bring lunch from home are just "
                             f"the ones it misses. A sample that cannot reach "
                             f"everyone is biased."),
        "key": lambda p: p["b"] - p["a"],
        # The errors: the asked group, and the whole school.
        "choices": lambda p: [p["b"] - p["a"], p["a"], p["b"]],
        "check": lambda p: (20 <= p["a"] <= 200 and p["a"] + 20 <= p["b"]
                            and p["b"] <= 400
                            and p["b"] - p["a"] != p["a"]
                            and len({p["b"] - p["a"], p["a"],
                                     p["b"]}) == 3,
                            "a school clearly bigger than the group asked, "
                            "and three distinct taps"),
    },
    "merr": {  # four times the people to halve the margin -- not twice
        "ans": lambda p: 4 * p["a"],
        "spoken": lambda p: (f"A sample of {p['a']} people gives a margin "
                             f"of error of about {p['b']} points. To cut "
                             f"that margin in HALF you need four times as "
                             f"many people. How many people is that?"),
        "board": _merr_board,         # (tt) the people machine, its output blank; the pending line a statement
        "worked": _merr_worked,       # (tt) now beside four times, as bars
        "praise": lambda p: (f"Four times {p['a']} is {4 * p['a']} people. "
                             f"Accuracy comes slowly: doubling to "
                             f"{2 * p['a']} does NOT halve the margin, it "
                             f"only shaves it a little. Every extra digit "
                             f"of certainty costs far more people than the "
                             f"last one did."),
        "key": lambda p: p["a"],
        # The errors: DOUBLING (the linear guess, and the whole lesson), and
        # the margin itself answered instead of a headcount.
        "choices": lambda p: [4 * p["a"], 2 * p["a"], p["b"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp),
        "check": lambda p: (25 <= p["a"] <= 250 and 2 <= p["b"] <= 9
                            and 4 * p["a"] <= 1000
                            and len({4 * p["a"], 2 * p["a"], p["b"]}) == 3,
                            "a sample that can afford to quadruple, and "
                            "three distinct taps"),
    },
    # ---- build ls: Prob & Stats U5 Probability Basics --------------------
    "ppct": {  # chance on the 0-to-100 scale -- geo-u9 counted, this measures
        "ans": lambda p: 100 * p["a"] // p["b"],
        "spoken": lambda p: (f"A bag holds {p['b']} marbles and {p['a']} of "
                             f"them are red. One is picked without looking. "
                             f"What percent chance is it red?"),
        "board": _ppct_board,         # (tt) the bag as bars, red beside not red
        "worked": _ppct_worked,       # (tt) the chance on the hundred square
        "praise": lambda p: (f"{p['a']} out of {p['b']} is "
                             f"{100 * p['a'] // p['b']} percent — chance "
                             f"lives on a scale from 0 to 100, where 0 never "
                             f"happens and 100 always does. {p['a']} is a "
                             f"count of marbles, and {p['b'] - p['a']} is "
                             f"how many are not red."),
        "key": lambda p: 100 * p["a"] // p["b"],
        # The errors: the COUNT of red handed back as a percent, and the
        # count of everything else.
        "choices": lambda p: [100 * p["a"] // p["b"], p["a"],
                              p["b"] - p["a"]],
        "check": lambda p: (2 <= p["a"] < p["b"] <= 50
                            and (100 * p["a"]) % p["b"] == 0
                            and 10 <= 100 * p["a"] // p["b"] <= 90
                            and len({100 * p["a"] // p["b"], p["a"],
                                     p["b"] - p["a"]}) == 3,
                            "a chance that lands on a whole percent, well "
                            "inside 0 and 100, with three distinct taps"),
    },
    "por": {  # OR, when the two cannot happen together: ADD the ways
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"A bag holds {p['a']} red, {p['b']} blue and "
                             f"{p['c']} green marbles. One is picked. Red OR "
                             f"blue wins. How many of the marbles are "
                             f"winners?"),
        "board": _por_board,          # (tt) the bars captioned (they had none -- rule 41); the pending line a statement (the old "how many winners?" was a question inside a step)
        "worked": _por_worked,        # (tt) the piles joined on a tape
        "praise": lambda p: (f"A marble cannot be red AND blue at once, so "
                             f"the two piles just join: {p['a']} plus "
                             f"{p['b']} equals {p['a'] + p['b']} winners out "
                             f"of {p['a'] + p['b'] + p['c']}. Timesing them "
                             f"would say {p['a'] * p['b']}, which counts "
                             f"PAIRS of marbles rather than marbles — and "
                             f"timesing is what AND does, not OR."),
        "key": lambda p: p["a"] + p["b"],
        # The errors: TIMESING (the and/or mix-up -- pand is the other half
        # of this pair), and counting the whole bag.
        "choices": lambda p: [p["a"] + p["b"], p["a"] * p["b"],
                              p["a"] + p["b"] + p["c"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and 2 <= p["c"] <= 9
                            and len({p["a"] + p["b"], p["a"] * p["b"],
                                     p["a"] + p["b"] + p["c"]}) == 3,
                            "three real piles, and the sum, the product and "
                            "the whole bag are three different numbers"),
    },
    "pand": {  # AND, when neither touches the other: TIMES the chances
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: (f"The chance of rain tomorrow is one in "
                             f"{p['a']}. The chance your bus is late is one "
                             f"in {p['b']}. Neither has anything to do with "
                             f"the other. The chance of BOTH happening is "
                             f"one in what?"),
        "board": _pand_board,         # (tt) two pies, one slice each
        "worked": _pand_worked,       # (tt) days by buses as an array
        "praise": lambda p: (f"One day in {p['a']} is rainy, and one bus "
                             f"in {p['b']} is late, so both together turn up "
                             f"one time in {p['a']} times {p['b']} — one in "
                             f"{p['a'] * p['b']}. Wanting BOTH is always "
                             f"rarer, never one in "
                             f"{p['a'] + p['b']}."),
        "key": lambda p: p["a"] * p["b"],
        # The errors: ADDING (por's rule, borrowed wrongly), and the rarer
        # of the two chances kept as if the other did nothing.
        "choices": lambda p: [p["a"] * p["b"], p["a"] + p["b"],
                              max(p["a"], p["b"])],
        "check": lambda p: (2 <= p["a"] <= 12 and 2 <= p["b"] <= 12
                            and p["a"] != p["b"] and p["a"] * p["b"] <= 100
                            and len({p["a"] * p["b"], p["a"] + p["b"],
                                     max(p["a"], p["b"])}) == 3,
                            "two different chances whose product stays "
                            "under 100, and three distinct taps"),
    },
    "ptre": {  # count the winning PATHS of a two-stage spin
        "ans": lambda p: p["b"] * p["b"],
        "spoken": lambda p: (f"A spinner has {p['a']} equal parts, and "
                             f"{p['b']} of them are winners. You spin it "
                             f"twice, giving {p['a'] * p['a']} "
                             f"different paths in all. How many of those "
                             f"paths win BOTH times?"),
        # NOT [[tree]] on the ask -- that renderer prints every leaf's
        # product, which is the answer. The teach beats show it instead.
        "board": _ptre_board,         # (tt) the spinner as a pie with its winners shaded
        "worked": _ptre_worked,       # (tt) the tree of paths (it prints the products -- walk-back only)
        "praise": lambda p: (f"Each winning first spin can be followed by "
                             f"each winning second spin: {p['b']} times "
                             f"{p['b']} equals {p['b'] * p['b']} winning "
                             f"paths out of {p['a'] * p['a']}. "
                             f"{p['b'] * p['a']} would count the paths that "
                             f"win the FIRST spin and then do anything at "
                             f"all."),
        "key": lambda p: p["b"],
        # The errors: win-then-anything (the second spin left free), and the
        # two spins added instead of paired.
        "choices": lambda p: [p["b"] * p["b"], p["b"] * p["a"], 2 * p["b"]],
        "check": lambda p: (3 <= p["a"] <= 12 and 2 <= p["b"] <= p["a"] - 1
                            and p["b"] * p["b"] <= 64
                            and len({p["b"] * p["b"], p["b"] * p["a"],
                                     2 * p["b"]}) == 3,
                            "a spinner with real losers on it, a winning-"
                            "path count under 64, and three distinct taps"),
    },
    # ---- build ls: Prob & Stats U6 Conditional Probability & Independence -
    "cbse": {  # conditioning changes WHAT YOU DIVIDE BY
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"In a class, {p['a']} girls chose soccer and "
                             f"{p['b']} girls chose art, while {p['c']} boys "
                             f"chose soccer and {p['c'] + 3} boys chose art. "
                             f"Picking from the GIRLS only, the chance of "
                             f"soccer is out of how many?"),
        "board": _cbse_board,         # (tt) the four groups as bars
        "worked": _cbse_worked,       # (tt) the two-way table with its row totals
        "praise": lambda p: (f"Asking about the girls only shrinks the "
                             f"world to the girls: {p['a']} plus "
                             f"{p['b']} equals {p['a'] + p['b']}. The whole "
                             f"class of "
                             f"{2 * p['c'] + 3 + p['a'] + p['b']} answers a "
                             f"different question, and {p['a']} alone is "
                             f"the soccer girls."),
        "key": lambda p: p["a"] + p["b"],
        # The errors: the WHOLE class (conditioning ignored -- the heart of
        # the unit), and the cell itself.
        "choices": lambda p: [p["a"] + p["b"],
                              2 * p["c"] + 3 + p["a"] + p["b"], p["a"]],
        "check": lambda p: (2 <= p["a"] <= 20 and 2 <= p["b"] <= 20
                            and 2 <= p["c"] <= 15
                            and len({p["a"] + p["b"],
                                     2 * p["c"] + 3 + p["a"] + p["b"],
                                     p["a"]}) == 3,
                            "a class with all four boxes filled, and three "
                            "distinct taps"),
    },
    "ccnt": {  # the conditional rate itself, once the world has shrunk
        "ans": lambda p: 100 * p["a"] // (p["a"] + p["b"]),
        "spoken": lambda p: (f"Every girl in a class chose one club: "
                             f"{p['a']} chose soccer and {p['b']} chose art. "
                             f"Picking a girl at random, what percent chose "
                             f"soccer?"),
        "board": _ccnt_board,         # (tt) the girls' two clubs as bars
        "worked": _ccnt_worked,       # (tt) the share on the hundred square
        "praise": lambda p: (f"The girls are the whole world now — "
                             f"{p['a']} plus {p['b']} equals "
                             f"{p['a'] + p['b']} of them — and {p['a']} of "
                             f"those chose soccer: "
                             f"{100 * p['a'] // (p['a'] + p['b'])} percent. "
                             f"The other "
                             f"{100 - 100 * p['a'] // (p['a'] + p['b'])} "
                             f"percent chose art, and {p['a']} is a "
                             f"headcount, not a percent."),
        "key": lambda p: 100 * p["a"] // (p["a"] + p["b"]),
        # The errors: the count answered as a percent, and the OTHER club's
        # share.
        "choices": lambda p: [100 * p["a"] // (p["a"] + p["b"]), p["a"],
                              100 - 100 * p["a"] // (p["a"] + p["b"])],
        "check": lambda p: (2 <= p["a"] <= 30 and 2 <= p["b"] <= 30
                            and (100 * p["a"]) % (p["a"] + p["b"]) == 0
                            and 20 <= 100 * p["a"] // (p["a"] + p["b"]) <= 80
                            and 100 * p["a"] // (p["a"] + p["b"]) != 50
                            and len({100 * p["a"] // (p["a"] + p["b"]),
                                     p["a"],
                                     100 - 100 * p["a"]
                                     // (p["a"] + p["b"])}) == 3,
                            "a whole percent away from the 50-50 split, so "
                            "the share and its complement are different "
                            "taps"),
    },
    "indp": {  # independent means the group's rate IS the overall rate
        "ans": lambda p: p["a"],
        "spoken": lambda p: (f"In a school, {p['a']} percent of students "
                             f"like maths, and among the {p['b']} "
                             f"left-handers {p['c']} percent do. If "
                             f"left-handedness had nothing to do with liking "
                             f"maths, what percent of the left-handers would "
                             f"like it?"),
        "board": _indp_board,         # (tt) the school beside the group as bars
        "worked": _indp_worked,       # (tt) predicted beside measured
        "praise": lambda p: (f"Independent means the left-handers would "
                             f"look just like the school: {p['a']} percent. "
                             f"They came in at {p['c']}, so the two are NOT "
                             f"independent — and {p['b']} is a headcount, "
                             f"not a rate."),
        "key": lambda p: p["a"],
        # The errors: the MEASURED rate (the question asked what it would be
        # IF independent), and the size of the group.
        "choices": lambda p: [p["a"], p["c"], p["b"]],
        "check": lambda p: (10 <= p["a"] <= 90 and p["a"] % 5 == 0
                            and 10 <= p["c"] <= 90 and p["c"] % 5 == 0
                            and abs(p["a"] - p["c"]) >= 10
                            and 10 <= p["b"] <= 60
                            and (p["b"] * p["c"]) % 100 == 0
                            and len({p["a"], p["c"], p["b"]}) == 3,
                            "two rates far enough apart to argue about, and "
                            "a group whose measured percent lands on whole "
                            "students -- no fraction of a child"),
    },
    "wout": {  # without replacement: the second draw lives in a smaller world
        "ans": lambda p: p["b"] - 1,
        "spoken": lambda p: (f"A bag holds {p['b']} marbles and {p['a']} of "
                             f"them are red. You take one red out and keep "
                             f"it. For the NEXT pick, the chance of red is "
                             f"out of how many marbles now?"),
        "board": _wout_board,         # (tt) the bag as a tape before the marble is kept
        "worked": _wout_worked,       # (tt) the smaller bag
        "praise": lambda p: (f"The marble did not go back, so the bag is "
                             f"smaller: {p['b']} take away 1 leaves "
                             f"{p['b'] - 1}. The reds shrank too, to "
                             f"{p['a'] - 1} — but that is the top of the "
                             f"chance, not the bottom. Answering {p['b']} "
                             f"forgets that anything was taken at all."),
        "key": lambda p: p["b"],
        # The errors: the bag unchanged (the whole lesson), and the count of
        # reds left -- the other number that shrank.
        "choices": lambda p: [p["b"] - 1, p["b"], p["a"] - 1],
        "check": lambda p: (3 <= p["a"] < p["b"] <= 40
                            and p["b"] - p["a"] >= 2
                            and len({p["b"] - 1, p["b"], p["a"] - 1}) == 3,
                            "a bag with other colours left in it, and three "
                            "distinct taps"),
    },
    # ---- build lt: Prob & Stats U7 Random Variables & Expected Value ------
    "pdis": {  # every chance in a distribution, added up, is the whole 100
        "ans": lambda p: 100 - p["a"] - p["b"],
        "spoken": lambda p: (f"A prize machine gives a small, medium or "
                             f"large prize. Small comes up {p['a']} percent "
                             f"of the time and medium {p['b']} percent. "
                             f"What percent of the time is it large?"),
        "board": _pdis_board,         # (ty) the ask picture, answer withheld
        "worked": _pdis_worked,       # (ty) the walk-back, filled in
        "praise": lambda p: (f"All the chances of one machine add to the "
                             f"whole 100: {p['a']} plus {p['b']} is "
                             f"{p['a'] + p['b']}, so large takes what is "
                             f"left — {100 - p['a'] - p['b']} percent. "
                             f"Something has to happen every time, and "
                             f"these three are the only choices."),
        "key": lambda p: 100 - p["a"] - p["b"],
        # The errors: the two given chances added (the leftover forgotten),
        # and the whole 100 handed back.
        "choices": lambda p: [100 - p["a"] - p["b"], p["a"] + p["b"], 100],
        "check": lambda p: (10 <= p["a"] <= 60 and 10 <= p["b"] <= 60
                            and p["a"] % 5 == 0 and p["b"] % 5 == 0
                            and 10 <= 100 - p["a"] - p["b"] <= 70
                            and len({100 - p["a"] - p["b"],
                                     p["a"] + p["b"], 100}) == 3,
                            "three real chances that add to 100, and three "
                            "distinct taps"),
    },
    "evwa": {  # expected value: the payoffs WEIGHTED by how often they come
        "ans": lambda p: (p["a"] * p["c"] + p["b"] * (100 - p["c"])) // 100,
        "spoken": lambda p: (f"A game pays {p['a']} tokens {p['c']} percent "
                             f"of the time, and {p['b']} tokens the rest of "
                             f"the time. Over many plays, how many tokens "
                             f"is a single play worth on average?"),
        "board": _evwa_board,         # (ty) the ask picture, answer withheld
        "worked": _evwa_worked,       # (ty) the walk-back, filled in
        "praise": lambda p: (f"Weighed by how often each turns up, "
                             f"{p['a']} tokens {p['c']} percent of the time "
                             f"and {p['b']} the rest averages "
                             f"{(p['a'] * p['c'] + p['b'] * (100 - p['c'])) // 100} "
                             f"a play. The plain average "
                             f"{(p['a'] + p['b']) // 2} would need both to "
                             f"come up equally often."),
        "key": lambda p: (p["a"] * p["c"] + p["b"] * (100 - p["c"])) // 100,
        # The errors: the PLAIN average of the two prizes (the classic --
        # weights ignored), and the big prize taken as the value.
        "choices": lambda p: [(p["a"] * p["c"]
                               + p["b"] * (100 - p["c"])) // 100,
                              (p["a"] + p["b"]) // 2, p["a"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["c"]) in sp),
        "check": lambda p: (2 <= p["b"] < p["a"] <= 40
                            and 10 <= p["c"] <= 90 and p["c"] % 5 == 0
                            and (p["a"] * p["c"]
                                 + p["b"] * (100 - p["c"])) % 100 == 0
                            and (p["a"] + p["b"]) % 2 == 0
                            and len({(p["a"] * p["c"]
                                      + p["b"] * (100 - p["c"])) // 100,
                                     (p["a"] + p["b"]) // 2, p["a"]}) == 3,
                            "an average that lands whole, a whole plain "
                            "average to argue with, and three distinct "
                            "taps"),
    },
    "fair": {  # run expected value BACKWARDS: what prize makes it even?
        "ans": lambda p: 100 * p["a"] // p["b"],
        "spoken": lambda p: (f"A game costs {p['a']} tokens to play, and "
                             f"you win {p['b']} percent of the time. What "
                             f"prize would make the game exactly fair — "
                             f"worth just what it costs?"),
        "board": _fair_board,         # (ty) the ask picture, answer withheld
        "worked": _fair_worked,       # (ty) the walk-back, filled in
        "praise": lambda p: (f"You pay on all hundred plays but collect "
                             f"on {p['b']}: {100 * p['a']} tokens in, "
                             f"shared over {p['b']} wins — "
                             f"{100 * p['a'] // p['b']} tokens a prize. "
                             f"Just your stake back, {p['a']}, still loses "
                             f"you every play you do not win."),
        "key": lambda p: 100 * p["a"] // p["b"],
        # The errors: the stake handed back as the prize (a fair-looking
        # trade that ignores the losses), and the percent read as tokens.
        "choices": lambda p: [100 * p["a"] // p["b"], p["a"], p["b"]],
        "check": lambda p: (2 <= p["a"] <= 20 and 10 <= p["b"] <= 50
                            and p["b"] % 5 == 0
                            and (100 * p["a"]) % p["b"] == 0
                            and 100 * p["a"] // p["b"] <= 200
                            and len({100 * p["a"] // p["b"], p["a"],
                                     p["b"]}) == 3,
                            "a fair prize that lands on whole tokens, and "
                            "three distinct taps"),
    },
    "hedg": {  # what a play really costs once the winnings are counted in
        "ans": lambda p: p["a"] - p["b"],
        "spoken": lambda p: (f"A game costs {p['a']} tokens a play, and "
                             f"over many plays it pays back {p['b']} tokens "
                             f"a play on average. In the long run, how many "
                             f"tokens does each play really cost you?"),
        "board": _hedg_board,         # (ty) the ask picture, answer withheld
        "worked": _hedg_worked,       # (ty) the walk-back, filled in
        "praise": lambda p: (f"Money out, money back: {p['a']} take away "
                             f"{p['b']} leaves {p['a'] - p['b']} tokens "
                             f"gone a play. That gap never shows in one "
                             f"play, only over hundreds — and it is how "
                             f"the machine stays open."),
        "key": lambda p: p["a"],
        # The errors: the two amounts added, and the winnings read as the
        # cost.
        "choices": lambda p: [p["a"] - p["b"], p["a"] + p["b"], p["b"]],
        "check": lambda p: (3 <= p["b"] < p["a"] <= 60
                            and p["a"] - p["b"] >= 2
                            and len({p["a"] - p["b"], p["a"] + p["b"],
                                     p["b"]}) == 3,
                            "a real gap between paying and winning, and "
                            "three distinct taps"),
    },
    # ---- build lt: Prob & Stats U8 The Normal Distribution ----------------
    "n68": {  # the middle of the bell: 68 percent, turned into children
        "ans": lambda p: 68 * p["a"] // 100,
        "spoken": lambda p: (f"The heights of a group of {p['a']} follow a "
                             f"bell curve. About 68 percent of the group sit "
                             f"no further than one standard deviation "
                             f"from the mean. "
                             f"About how many of the whole group is that?"),
        "board": _n68_board,         # (ty) the ask picture, answer withheld
        "worked": _n68_worked,       # (ty) the walk-back, filled in
        "praise": lambda p: (f"68 percent of {p['a']} is "
                             f"{68 * p['a'] // 100} — most of a "
                             f"bell curve crowds close to the middle, and "
                             f"that is what gives it the shape. The 68 is a "
                             f"percent, never a headcount, and {p['a']} is "
                             f"everybody."),
        "key": lambda p: p["a"],
        # The errors: the 68 answered as if it were people, and the whole
        # group.
        "choices": lambda p: [68 * p["a"] // 100, 68, p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (p["a"] % 25 == 0 and 50 <= p["a"] <= 800
                            and p["b"] == 0
                            and len({68 * p["a"] // 100, 68, p["a"]}) == 3,
                            "a group whose 68 percent lands on whole "
                            "students, and three distinct taps"),
    },
    "zsco": {  # how many standard deviations out a value sits
        "ans": lambda p: (p["c"] - p["a"]) // p["b"],
        "spoken": lambda p: (f"On a bell curve the mean is {p['a']} and one "
                             f"standard deviation is {p['b']}. A value of "
                             f"{p['c']} sits how many standard deviations "
                             f"ABOVE the mean?"),
        # NOT [[normal]] on the ask -- that renderer labels the axis at
        # every standard deviation, so the picture counts them for you.
        "board": _zsco_board,         # (ty) the ask picture, answer withheld
        "worked": _zsco_worked,       # (ty) the walk-back, filled in
        "praise": lambda p: (f"{p['c']} sits {p['c'] - p['a']} above the "
                             f"mean, and each standard deviation is "
                             f"{p['b']} — so that gap holds "
                             f"{(p['c'] - p['a']) // p['b']} of them. "
                             f"Counting deviations instead of raw units is "
                             f"what lets two different measurements be "
                             f"compared at all."),
        "key": lambda p: p["a"],
        # The errors: the RAW gap (deviations never counted), and the
        # standard deviation itself.
        "choices": lambda p: [(p["c"] - p["a"]) // p["b"],
                              p["c"] - p["a"], p["b"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["c"]) in sp),
        "check": lambda p: (10 <= p["a"] <= 100 and 2 <= p["b"] <= 15
                            and p["c"] > p["a"]
                            and (p["c"] - p["a"]) % p["b"] == 0
                            and 1 <= (p["c"] - p["a"]) // p["b"] <= 3
                            and len({(p["c"] - p["a"]) // p["b"],
                                     p["c"] - p["a"], p["b"]}) == 3,
                            "a value a whole number of deviations out, no "
                            "more than three, and three distinct taps"),
    },
    "zval": {  # the same rule run the other way: which value sits out there
        "ans": lambda p: p["a"] + 2 * p["b"],
        "spoken": lambda p: (f"On a bell curve the mean is {p['a']} and one "
                             f"standard deviation is {p['b']}. What value "
                             f"sits exactly two standard deviations ABOVE "
                             f"the mean?"),
        "board": _zval_board,         # (ty) the ask picture, answer withheld
        "worked": _zval_worked,       # (ty) the walk-back, filled in
        "praise": lambda p: (f"Two deviations is {p['b']} twice — "
                             f"{2 * p['b']} — laid on top of the mean: "
                             f"{p['a']} plus {2 * p['b']} equals "
                             f"{p['a'] + 2 * p['b']}. Only about 2 students "
                             f"in a hundred ever get out that far. "
                             f"{p['a'] + p['b']} is one deviation, and "
                             f"{2 * p['b']} forgot to start from the mean."),
        "key": lambda p: p["a"],
        # The errors: ONE deviation counted, and the distance answered
        # without ever leaving from the mean.
        "choices": lambda p: [p["a"] + 2 * p["b"], p["a"] + p["b"],
                              2 * p["b"]],
        "check": lambda p: (10 <= p["a"] <= 100 and 2 <= p["b"] <= 20
                            and len({p["a"] + 2 * p["b"], p["a"] + p["b"],
                                     2 * p["b"]}) == 3,
                            "a mean and a deviation whose one-step, "
                            "two-step and bare distance all differ"),
    },
    "ntal": {  # the far tail: how few people really live out there
        "ans": lambda p: p["a"] // 40,
        "spoken": lambda p: (f"In a group of {p['a']}, about 95 percent sit "
                             f"no further than two standard deviations "
                             f"from the mean. "
                             f"The 5 percent left over splits evenly "
                             f"between the two ends. About how many sit "
                             f"more than two standard deviations ABOVE the "
                             f"mean?"),
        "board": _ntal_board,         # (ty) the ask picture, answer withheld
        "worked": _ntal_worked,       # (ty) the walk-back, filled in
        "praise": lambda p: (f"5 percent of {p['a']} is {p['a'] // 20} "
                             f"people out at the ends, and they split "
                             f"evenly: {p['a'] // 40} above and "
                             f"{p['a'] // 40} below. That is why a value "
                             f"two deviations out is worth remarking on — "
                             f"almost nobody is there."),
        "key": lambda p: p["a"],
        # The errors: BOTH ends counted (the split forgotten), and half the
        # group -- the bell read as though its ends were huge.
        "choices": lambda p: [p["a"] // 40, p["a"] // 20, p["a"] // 2],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (p["a"] % 40 == 0 and 80 <= p["a"] <= 800
                            and p["b"] == 0
                            and len({p["a"] // 40, p["a"] // 20,
                                     p["a"] // 2}) == 3,
                            "a group whose ends land on whole people, and "
                            "three distinct taps"),
    },
    # ---- build lu: Prob & Stats U9 Sampling & Inference -------------------
    "cint": {  # an estimate is a RANGE: this is its low end
        "ans": lambda p: p["a"] - p["b"],
        "spoken": lambda p: (f"A poll estimates {p['a']} percent, give or "
                             f"take {p['b']} points. What is the LOWEST "
                             f"percent the true answer might be?"),
        "board": _cint_board,         # (ty) the ask picture, answer withheld
        "worked": _cint_worked,       # (ty) the walk-back, filled in
        "praise": lambda p: (f"Give or take {p['b']} means {p['b']} either "
                             f"way, so the low end is {p['a']} take away "
                             f"{p['b']} — {p['a'] - p['b']} percent. "
                             f"{p['a'] + p['b']} is the HIGH end, the same "
                             f"step in the other direction."),
        "key": lambda p: p["a"] - p["b"],
        # The errors: the high end, and the margin on its own.
        "choices": lambda p: [p["a"] - p["b"], p["a"] + p["b"], p["b"]],
        "check": lambda p: (20 <= p["a"] <= 80 and 2 <= p["b"] <= 12
                            and p["a"] - p["b"] >= 5
                            and len({p["a"] - p["b"], p["a"] + p["b"],
                                     p["b"]}) == 3,
                            "a real range that stays inside the percents, "
                            "and three distinct taps"),
    },
    "cwid": {  # the whole range is the margin BOTH ways
        "ans": lambda p: 2 * p["b"],
        "spoken": lambda p: (f"A poll estimates {p['a']} percent, give or "
                             f"take {p['b']} points. From its lowest to its "
                             f"highest, how many points wide is that whole "
                             f"range?"),
        "board": _cwid_board,         # (ty) the ask picture, answer withheld
        "worked": _cwid_worked,       # (ty) the walk-back, filled in
        "praise": lambda p: (f"The range runs {p['b']} below and {p['b']} "
                             f"above, so it is {p['b']} twice — "
                             f"{2 * p['b']} points wide, from "
                             f"{p['a'] - p['b']} to {p['a'] + p['b']}. The "
                             f"margin {p['b']} is only half the story, one "
                             f"side of the middle."),
        "key": lambda p: p["b"],
        # The errors: the margin answered as the width (one side only), and
        # the estimate itself.
        "choices": lambda p: [2 * p["b"], p["b"], p["a"]],
        "check": lambda p: (20 <= p["a"] <= 80 and 2 <= p["b"] <= 15
                            and p["a"] - p["b"] >= 5
                            and len({2 * p["b"], p["b"], p["a"]}) == 3,
                            "a margin whose double is still not the "
                            "estimate, and three distinct taps"),
    },
    "inci": {  # is a claim inside the range -- and if not, by how much?
        "ans": lambda p: p["c"] - (p["a"] + p["b"]),
        "spoken": lambda p: (f"Your poll says {p['a']} percent, give or "
                             f"take {p['b']}, so anything up to "
                             f"{p['a'] + p['b']} is possible. A company "
                             f"claims {p['c']} percent. How many points "
                             f"ABOVE your highest possible value is their "
                             f"claim?"),
        "board": _inci_board,         # (ty) the ask picture, answer withheld
        "worked": _inci_worked,       # (ty) the walk-back, filled in
        "praise": lambda p: (f"Your range reaches {p['a'] + p['b']} at the "
                             f"very most, and they claim {p['c']}: that is "
                             f"{p['c'] - (p['a'] + p['b'])} points past "
                             f"anything your poll can support. Measuring "
                             f"from {p['a']} instead gives "
                             f"{p['c'] - p['a']} and forgets that your own "
                             f"estimate has room in it."),
        "key": lambda p: p["c"] - (p["a"] + p["b"]),
        # The errors: measured from the ESTIMATE (the margin ignored), and
        # the margin itself.
        "choices": lambda p: [p["c"] - (p["a"] + p["b"]), p["c"] - p["a"],
                              p["b"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["c"]) in sp),
        "check": lambda p: (20 <= p["a"] <= 70 and 2 <= p["b"] <= 10
                            and p["c"] <= 95
                            and p["c"] - (p["a"] + p["b"]) >= 2
                            and len({p["c"] - (p["a"] + p["b"]),
                                     p["c"] - p["a"], p["b"]}) == 3,
                            "a claim clearly outside the range, and three "
                            "distinct taps"),
    },
    "npop": {  # carry the range down onto real people
        "ans": lambda p: (p["a"] - p["b"]) * p["c"] // 100,
        "spoken": lambda p: (f"A sample says {p['a']} percent of a school of "
                             f"{p['c']} walk to school, give or "
                             f"take {p['b']} points. At the LOW end of that "
                             f"range, how many of the whole school is that?"),
        "board": _npop_board,         # (ty) the ask picture, answer withheld
        "worked": _npop_worked,       # (ty) the walk-back, filled in
        "praise": lambda p: (f"The low end of the range is "
                             f"{p['a'] - p['b']} percent, and "
                             f"{p['a'] - p['b']} percent of {p['c']} is "
                             f"{(p['a'] - p['b']) * p['c'] // 100}. "
                             f"Using {p['a']} percent gives "
                             f"{p['a'] * p['c'] // 100} and quietly drops "
                             f"the give-or-take — the whole point of a "
                             f"sample is that it does not know exactly."),
        "key": lambda p: (p["a"] - p["b"]) * p["c"] // 100,
        # The errors: the estimate used with the margin forgotten, and the
        # HIGH end taken instead of the low.
        "choices": lambda p: [(p["a"] - p["b"]) * p["c"] // 100,
                              p["a"] * p["c"] // 100,
                              (p["a"] + p["b"]) * p["c"] // 100],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["c"]) in sp),
        "check": lambda p: (20 <= p["a"] <= 70 and 5 <= p["b"] <= 20
                            and p["c"] % 100 == 0 and 200 <= p["c"] <= 1000
                            and p["a"] - p["b"] >= 10
                            and p["a"] + p["b"] <= 90
                            and len({(p["a"] - p["b"]) * p["c"] // 100,
                                     p["a"] * p["c"] // 100,
                                     (p["a"] + p["b"]) * p["c"] // 100}) == 3,
                            "a school size that turns every percent into "
                            "whole students, and three distinct taps"),
    },
    # ---- build lu: Calculus U1 Limits & Continuity ------------------------
    "llaw": {  # limits pass straight through arithmetic
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: (f"As x creeps toward 4, f creeps toward "
                             f"{p['a']} and g creeps toward {p['b']}. What "
                             f"does f times g creep toward?"),
        "board": _llaw_board,         # (tz) the ask picture, answer withheld
        "worked": _llaw_worked,       # (tz) the walk-back, filled in
        "praise": lambda p: (f"Limits pass straight through the arithmetic: "
                             f"if f is heading for {p['a']} and g for "
                             f"{p['b']}, their product heads for {p['a']} "
                             f"times {p['b']} — {p['a'] * p['b']}. Adding "
                             f"would answer a different question, and "
                             f"{max(p['a'], p['b'])} is just the bigger of "
                             f"the two."),
        "key": lambda p: p["a"] * p["b"],
        # The errors: the limits ADDED, and the bigger limit kept.
        "choices": lambda p: [p["a"] * p["b"], p["a"] + p["b"],
                              max(p["a"], p["b"])],
        "check": lambda p: (2 <= p["a"] <= 12 and 2 <= p["b"] <= 12
                            and p["a"] != p["b"] and p["a"] * p["b"] <= 100
                            and len({p["a"] * p["b"], p["a"] + p["b"],
                                     max(p["a"], p["b"])}) == 3,
                            "two different limits whose product stays under "
                            "100, and three distinct taps"),
    },
    "linf": {  # far out, only the leading terms matter
        "ans": lambda p: p["a"] // p["b"],
        "spoken": lambda p: (f"As x grows huge, what number does {p['a']} x "
                             f"squared, divided by {p['b']} x squared, "
                             f"settle toward?"),
        "board": _linf_board,         # (tz) the ask picture, answer withheld
        "worked": _linf_worked,       # (tz) the walk-back, filled in
        "praise": lambda p: (f"The x squareds cancel however big x gets, "
                             f"leaving {p['a']} over {p['b']} — "
                             f"{p['a'] // p['b']}. Algebra Two's asymptote "
                             f"lesson split a fraction to find its "
                             f"survivor; here both parts grow at the same "
                             f"speed, so the ratio is what survives."),
        "key": lambda p: p["a"] // p["b"],
        # The errors: the coefficients subtracted, and timesed.
        "choices": lambda p: [p["a"] // p["b"], p["a"] - p["b"],
                              p["a"] * p["b"]],
        "check": lambda p: (2 <= p["b"] <= 12 and p["a"] <= 96
                            and p["a"] % p["b"] == 0
                            and p["a"] // p["b"] >= 2
                            and len({p["a"] // p["b"], p["a"] - p["b"],
                                     p["a"] * p["b"]}) == 3,
                            "a ratio that lands whole and is at least 2, "
                            "with three distinct taps"),
    },
    "jump": {  # a break has a SIZE, and that size has a name
        "ans": lambda p: p["b"] - p["a"],
        "spoken": lambda p: (f"y is {p['a']} while x is below 6, and jumps "
                             f"to {p['b']} the moment x reaches 6. How big "
                             f"is the jump?"),
        "board": _jump_board,         # (tz) the ask picture, answer withheld
        "worked": _jump_worked,       # (tz) the walk-back, filled in
        "praise": lambda p: (f"The two sides head for {p['a']} and "
                             f"{p['b']}, so the curve leaps "
                             f"{p['b'] - p['a']} in no distance at all — "
                             f"that is a jump discontinuity, and its size "
                             f"is the gap between the one-sided limits. "
                             f"{p['b']} is only where it lands."),
        "key": lambda p: p["b"] - p["a"],
        # The errors: where it lands, and the two heights added.
        "choices": lambda p: [p["b"] - p["a"], p["b"], p["a"] + p["b"]],
        "check": lambda p: (2 <= p["a"] < p["b"] <= 40
                            and p["b"] - p["a"] >= 2
                            and 6 not in (p["a"], p["b"])
                            and p["a"] + p["b"] != 6
                            and len({p["b"] - p["a"], p["b"],
                                     p["a"] + p["b"]}) == 3,
                            "a real gap, no height and no tap equal to the "
                            "border 6 the question names, and three "
                            "distinct taps"),
    },
    "cfix": {  # mend the break: the flat piece must MEET the sloping one
        "ans": lambda p: p["c"] + p["a"],
        "spoken": lambda p: (f"y equals x plus {p['a']} while x is below "
                             f"{p['c']}, and a flat {p['b']} once x reaches "
                             f"{p['c']}. Right now it jumps. What would "
                             f"that flat value have to be for the curve to "
                             f"join up smoothly?"),
        "board": _cfix_board,         # (tz) the ask picture, answer withheld
        "worked": _cfix_worked,       # (tz) the walk-back, filled in
        "praise": lambda p: (f"Walk the sloping piece right up to "
                             f"{p['c']}: it arrives at {p['c']} plus "
                             f"{p['a']}, which is {p['c'] + p['a']}. Set "
                             f"the flat piece to {p['c'] + p['a']} and the "
                             f"two ends meet — no jump, no hole, and the "
                             f"curve is continuous. {p['b']} is the value "
                             f"that does not fit."),
        "key": lambda p: p["c"] + p["a"],
        # The errors: the broken value kept, and the slope's own number.
        "choices": lambda p: [p["c"] + p["a"], p["b"], p["a"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["b"]) in sp
                                 and str(p["c"]) in sp),
        "check": lambda p: (2 <= p["a"] <= 12 and 3 <= p["c"] <= 15
                            and 2 <= p["b"] <= 30
                            and p["b"] != p["c"] + p["a"]
                            and p["b"] != p["c"]
                            and len({p["c"] + p["a"], p["b"], p["a"]}) == 3,
                            "a flat piece that really does not meet the "
                            "slope and does not echo the border, and three "
                            "distinct taps"),
    },
    # ---- build lv: Calculus U2 The Derivative -----------------------------
    "derv": {  # the shrinking window's limit -- pc-u9's avgr, finished
        "ans": lambda p: 2 * p["a"],
        "spoken": lambda p: (f"On y equals x squared, shrink the window "
                             f"onto x equals {p['a']}. What number does the "
                             f"average rate close in on?"),
        "board": _derv_board,         # (tz) the ask picture, answer withheld
        "worked": _derv_worked,       # (tz) the walk-back, filled in
        "praise": lambda p: (f"The average rate is the two x's put "
                             f"together, so sliding both onto {p['a']} "
                             f"gives {2 * p['a']} — the DERIVATIVE there, "
                             f"the slope at a single point. "
                             f"{p['a'] * p['a']} is how HIGH the curve is, "
                             f"not how steep."),
        "key": lambda p: p["a"],
        # The errors: the curve's HEIGHT at that x, and the x itself.
        "choices": lambda p: [2 * p["a"], p["a"] * p["a"], p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (3 <= p["a"] <= 24 and p["b"] == 0
                            and len({2 * p["a"], p["a"] * p["a"],
                                     p["a"]}) == 3,
                            "an x where the slope, the height and the x "
                            "itself are three different numbers"),
    },
    "pwrc": {  # the power rule: the exponent comes DOWN and times the front
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: (f"The power rule says the exponent comes down "
                             f"in front and the power drops by one. For y "
                             f"equals {p['b']} x to the power {p['a']}, "
                             f"what is the derivative's front number?"),
        "board": _pwrc_board,         # (tz) the ask picture, answer withheld
        "worked": _pwrc_worked,       # (tz) the walk-back, filled in
        "praise": lambda p: (f"The {p['a']} comes down and meets the "
                             f"{p['b']} already standing there: {p['a']} "
                             f"times {p['b']} equals {p['a'] * p['b']}, and "
                             f"the power drops to {p['a'] - 1}. So the "
                             f"derivative is {p['a'] * p['b']} x to the "
                             f"{p['a'] - 1}. Adding the two numbers is not "
                             f"a rule anything obeys."),
        "key": lambda p: p["a"] * p["b"],
        # The errors: the two numbers ADDED, and the front number left
        # alone (the exponent never brought down).
        "choices": lambda p: [p["a"] * p["b"], p["a"] + p["b"], p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 12
                            and p["a"] != p["b"] and p["a"] * p["b"] <= 96
                            and len({p["a"] * p["b"], p["a"] + p["b"],
                                     p["b"]}) == 3,
                            "an exponent and a front number that differ, "
                            "with three distinct taps"),
    },
    "cnst": {  # a straight line has ONE slope, everywhere
        "ans": lambda p: p["a"],
        "spoken": lambda p: (f"A straight line is y equals {p['a']} x plus "
                             f"{p['b']}. Its steepness never changes. What "
                             f"is its derivative — the slope, anywhere "
                             f"along it?"),
        "board": _cnst_board,         # (tz) the ask picture, answer withheld
        "worked": _cnst_worked,       # (tz) the walk-back, filled in
        "praise": lambda p: (f"A line climbs {p['a']} for every step "
                             f"across, at every point on it, so its "
                             f"derivative is just {p['a']} — a constant. "
                             f"The {p['b']} only says where the line starts "
                             f"and never changes its steepness; a plain "
                             f"number has a derivative of zero."),
        "key": lambda p: p["a"],
        # The errors: the starting height read as the slope, and the two
        # numbers added.
        "choices": lambda p: [p["a"], p["b"], p["a"] + p["b"]],
        "check": lambda p: (2 <= p["a"] <= 20 and 2 <= p["b"] <= 20
                            and p["a"] != p["b"]
                            and len({p["a"], p["b"],
                                     p["a"] + p["b"]}) == 3,
                            "a slope and a starting height that differ, "
                            "with three distinct taps"),
    },
    "evat": {  # a derivative is a FUNCTION -- feed it an x
        "ans": lambda p: 2 * p["a"] * p["c"],
        "spoken": lambda p: (f"For y equals {p['a']} x squared, the "
                             f"derivative is {2 * p['a']} x. What is the "
                             f"slope of the curve at x equals {p['c']}?"),
        "board": _evat_board,         # (tz) the ask picture, answer withheld
        "worked": _evat_worked,       # (tz) the walk-back, filled in
        "praise": lambda p: (f"The derivative is a machine of its own: feed "
                             f"it {p['c']} and it gives {2 * p['a']} times "
                             f"{p['c']} — {2 * p['a'] * p['c']}. That is "
                             f"the slope right at that point. "
                             f"{p['a'] * p['c'] * p['c']} is how high the "
                             f"curve sits there, and {2 * p['a']} is the "
                             f"derivative's own front number, before any x "
                             f"went in."),
        "key": lambda p: 2 * p["a"] * p["c"],
        # The errors: the HEIGHT of the curve, and the derivative's front
        # number handed back un-fed.
        "choices": lambda p: [2 * p["a"] * p["c"],
                              p["a"] * p["c"] * p["c"], 2 * p["a"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["c"]) in sp),
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["c"] <= 9
                            and p["b"] == 0
                            and 2 * p["a"] * p["c"] <= 96
                            and len({2 * p["a"] * p["c"],
                                     p["a"] * p["c"] * p["c"],
                                     2 * p["a"]}) == 3,
                            "a point where the slope, the height and the "
                            "bare front number are three different taps"),
    },
    # ---- build lv: Calculus U3 Product, Quotient & Chain Rules ------------
    "prod": {  # the product rule agrees with multiplying out first
        "ans": lambda p: 2 * p["c"] + p["a"],
        "spoken": lambda p: (f"y equals x times the quantity x plus "
                             f"{p['a']}. Multiplied out that is x squared "
                             f"plus {p['a']} x, so its derivative is 2 x "
                             f"plus {p['a']}. What is the slope at x equals "
                             f"{p['c']}?"),
        "board": _prod_board,         # (tz) the ask picture, answer withheld
        "worked": _prod_worked,       # (tz) the walk-back, filled in
        "praise": lambda p: (f"Feed {p['c']} into 2 x plus {p['a']}: "
                             f"{2 * p['c']} plus {p['a']} is "
                             f"{2 * p['c'] + p['a']}. The product rule "
                             f"gives this without expanding first. "
                             f"{p['c'] * (p['c'] + p['a'])} is the curve's "
                             f"height there, not its slope."),
        "key": lambda p: 2 * p["c"] + p["a"],
        # The errors: the curve's height at that x, and the 2x term with
        # the second piece's derivative forgotten.
        "choices": lambda p: [2 * p["c"] + p["a"],
                              p["c"] * (p["c"] + p["a"]), 2 * p["c"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["c"]) in sp),
        "check": lambda p: (2 <= p["a"] <= 12 and 2 <= p["c"] <= 12
                            and p["b"] == 0
                            and len({2 * p["c"] + p["a"],
                                     p["c"] * (p["c"] + p["a"]),
                                     2 * p["c"]}) == 3,
                            "a point where the slope, the height and the "
                            "half-answer are three different taps"),
    },
    "chan": {  # the chain rule: the INSIDE's derivative comes out too
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: (f"y equals the quantity {p['a']} x plus 3, "
                             f"raised to the power {p['b']}. The chain rule "
                             f"brings the power down front AND times by the "
                             f"inside's own derivative. What number ends up "
                             f"in front?"),
        "board": _chan_board,         # (tz) the ask picture, answer withheld
        "worked": _chan_worked,       # (tz) the walk-back, filled in
        "praise": lambda p: (f"Two things come down: the power {p['b']} "
                             f"and the inside's derivative {p['a']} — "
                             f"{p['b']} times {p['a']} is "
                             f"{p['a'] * p['b']}. Forgetting the inside "
                             f"leaves {p['b']}, the commonest mistake in "
                             f"Calculus."),
        "key": lambda p: p["a"] * p["b"],
        # The errors: the INSIDE forgotten (the classic), and the two
        # numbers added.
        "choices": lambda p: [p["a"] * p["b"], p["b"], p["a"] + p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and p["a"] != p["b"] and p["a"] * p["b"] <= 81
                            and len({p["a"] * p["b"], p["b"],
                                     p["a"] + p["b"]}) == 3,
                            "an inside and a power that differ, with three "
                            "distinct taps"),
    },
    "chev": {  # the chain rule, then fed a number
        "ans": lambda p: 2 * p["a"] * p["b"],
        "spoken": lambda p: (f"y equals the quantity {p['a']} x plus "
                             f"{p['b']}, squared. The chain rule gives a "
                             f"slope of 2, times that quantity, times "
                             f"{p['a']}. What is the slope at x equals "
                             f"zero?"),
        "board": _chev_board,         # (tz) the ask picture, answer withheld
        "worked": _chev_worked,       # (tz) the walk-back, filled in
        "praise": lambda p: (f"At x equals zero the inside is just "
                             f"{p['b']}, so the slope is 2 times {p['b']} "
                             f"times {p['a']} — {2 * p['a'] * p['b']}. "
                             f"{p['b'] * p['b']} is the curve's height "
                             f"there, and {2 * p['b']} drops the inside's "
                             f"derivative — the chain rule's whole point."),
        "key": lambda p: 2 * p["a"] * p["b"],
        # The errors: the HEIGHT at zero, and the chain factor dropped.
        "choices": lambda p: [2 * p["a"] * p["b"], p["b"] * p["b"],
                              2 * p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 12
                            and p["a"] != p["b"]
                            and 2 * p["a"] * p["b"] <= 96
                            and len({2 * p["a"] * p["b"], p["b"] * p["b"],
                                     2 * p["b"]}) == 3,
                            "an inside and a multiplier that differ, with "
                            "three distinct taps"),
    },
    "quot": {  # a constant on the bottom just divides -- no quotient rule
        "ans": lambda p: 2 * p["a"] // p["b"],
        "spoken": lambda p: (f"y equals {p['a']} x squared, all divided by "
                             f"{p['b']}. A plain number on the bottom just "
                             f"divides everything. What is the derivative's "
                             f"front number?"),
        "board": _quot_board,         # (tz) the ask picture, answer withheld
        "worked": _quot_worked,       # (tz) the walk-back, filled in
        "praise": lambda p: (f"The power rule doubles the {p['a']} to "
                             f"{2 * p['a']}, and the {p['b']} underneath "
                             f"divides it: {2 * p['a']} over {p['b']} is "
                             f"{2 * p['a'] // p['b']}. A constant on the "
                             f"bottom needs no quotient rule at all — it "
                             f"just comes along for the ride."),
        "key": lambda p: 2 * p["a"] // p["b"],
        # The errors: the 2 from the power rule forgotten, and the two
        # numbers timesed instead of divided.
        "choices": lambda p: [2 * p["a"] // p["b"], p["a"] // p["b"],
                              p["a"] * p["b"]],
        "check": lambda p: ((2 * p["a"]) % p["b"] == 0
                            and p["a"] % p["b"] == 0
                            and 2 <= p["b"] <= 12 and p["a"] <= 60
                            and 2 * p["a"] // p["b"] >= 2
                            and len({2 * p["a"] // p["b"],
                                     p["a"] // p["b"],
                                     p["a"] * p["b"]}) == 3,
                            "both the doubled and the plain division land "
                            "whole, so the forgotten-2 tap is a real "
                            "number, and three distinct taps"),
    },
    # ---- build lw: Calculus U4 Applications of Derivatives ----------------
    "vsol": {  # run a derivative BACKWARDS: when is the speed this?
        "ans": lambda p: p["b"] // (2 * p["a"]),
        "spoken": lambda p: (f"A ball has fallen {p['a']} t squared metres "
                             f"after t seconds, so its speed is "
                             f"{2 * p['a']} t metres a second. At what time "
                             f"is it falling at {p['b']} metres a second?"),
        "board": _vsol_board,         # (ua) the ask picture, answer withheld
        "worked": _vsol_worked,       # (ua) the walk-back, filled in
        "praise": lambda p: (f"Set the speed equal to {p['b']}: "
                             f"{2 * p['a']} t equals {p['b']}, so t is "
                             f"{p['b']} over {2 * p['a']} — "
                             f"{p['b'] // (2 * p['a'])} seconds. A "
                             f"derivative can be solved like any other "
                             f"equation once you know what it says."),
        "key": lambda p: p["b"] // (2 * p["a"]),
        # The errors: the speed handed back as a time, and dividing by the
        # front number without doubling it.
        "choices": lambda p: [p["b"] // (2 * p["a"]), p["b"],
                              p["b"] // p["a"]],
        "check": lambda p: (2 <= p["a"] <= 9
                            and p["b"] % (2 * p["a"]) == 0
                            and p["b"] % p["a"] == 0
                            and 2 <= p["b"] // (2 * p["a"]) <= 15
                            and len({p["b"] // (2 * p["a"]), p["b"],
                                     p["b"] // p["a"]}) == 3,
                            "a time that lands whole, with the halved-and-"
                            "unhalved divisions both real, and three "
                            "distinct taps"),
    },
    "mrat": {  # related rates: how fast the AREA grows as the side grows
        "ans": lambda p: 2 * p["a"] * p["b"],
        "spoken": lambda p: (f"A square's side is growing {p['b']} "
                             f"centimetres a second. At the moment the side "
                             f"is {p['a']} centimetres, how fast is its "
                             f"AREA growing, in square centimetres a "
                             f"second?"),
        "board": _mrat_board,         # (ua) the ask picture, answer withheld
        "worked": _mrat_worked,       # (ua) the walk-back, filled in
        "praise": lambda p: (f"2 times {p['a']} times {p['b']} — "
                             f"{2 * p['a'] * p['b']} square centimetres a "
                             f"second. The area speeds up as the square "
                             f"grows, even though the side keeps a steady "
                             f"{p['b']}."),
        "key": lambda p: 2 * p["a"] * p["b"],
        # The errors: the SIDE's rate answered, and the area itself.
        "choices": lambda p: [2 * p["a"] * p["b"], p["b"],
                              p["a"] * p["a"]],
        "check": lambda p: (3 <= p["a"] <= 20 and 2 <= p["b"] <= 9
                            and 2 * p["a"] * p["b"] <= 96
                            and len({2 * p["a"] * p["b"], p["b"],
                                     p["a"] * p["a"]}) == 3,
                            "a growing square whose rate, side-rate and "
                            "area are three different numbers"),
    },
    "crit": {  # where the curve levels off: the slope hits zero
        "ans": lambda p: p["a"] // 2,
        "spoken": lambda p: (f"For y equals x squared take away {p['a']} x, "
                             f"the slope is 2 x take away {p['a']}. At "
                             f"which x is the slope exactly zero?"),
        "board": _crit_board,         # (ua) the ask picture, answer withheld
        "worked": _crit_worked,       # (ua) the walk-back, filled in
        "praise": lambda p: (f"Set the slope to zero: 2 x equals {p['a']}, "
                             f"so x is {p['a'] // 2}. There the curve is "
                             f"flat for an instant — the bottom of its "
                             f"valley, and the only place a smooth curve "
                             f"can turn around. {p['a']} is the number in "
                             f"the slope, not the x that answers it."),
        "key": lambda p: p["a"] // 2,
        # The errors: the slope's own number, and doubling instead of
        # halving.
        "choices": lambda p: [p["a"] // 2, p["a"], 2 * p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (p["a"] % 2 == 0 and 4 <= p["a"] <= 40
                            and len({p["a"] // 2, p["a"],
                                     2 * p["a"]}) == 3,
                            "an even number so the flat point lands whole, "
                            "and three distinct taps"),
    },
    "acce": {  # the derivative OF the derivative
        "ans": lambda p: 2 * p["a"],
        "spoken": lambda p: (f"A stone falls {p['a']} t squared metres in t "
                             f"seconds. Its speed is {2 * p['a']} t. "
                             f"Differentiate once more: what is its "
                             f"acceleration?"),
        "board": _acce_board,         # (ua) the ask picture, answer withheld
        "worked": _acce_worked,       # (ua) the walk-back, filled in
        "praise": lambda p: (f"The speed {2 * p['a']} t is a line, and a "
                             f"line's derivative is its front number: "
                             f"{2 * p['a']}. That is the acceleration — the "
                             f"rate the SPEED changes — and it never varies "
                             f"here, which is exactly what falling under "
                             f"gravity does. {p['a']} is the distance's "
                             f"number, one step back."),
        "key": lambda p: p["a"],
        # The errors: the distance's front number (one differentiation
        # short), and doubling once too often.
        "choices": lambda p: [2 * p["a"], p["a"], 4 * p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (2 <= p["a"] <= 24 and p["b"] == 0
                            and len({2 * p["a"], p["a"], 4 * p["a"]}) == 3,
                            "a fall whose speed, distance and double-"
                            "doubled numbers all differ"),
    },
    # ---- build lw: Calculus U5 Curve Sketching & Optimization -------------
    "optr": {  # the best rectangle for a fixed fence is a SQUARE
        "ans": lambda p: p["a"] // 4,
        "spoken": lambda p: (f"A rectangle is to be built with {p['a']} "
                             f"metres of fence all the way round. To make "
                             f"its area as big as possible, how long should "
                             f"each side be?"),
        "board": _optr_board,         # (ua) the ask picture, answer withheld
        "worked": _optr_worked,       # (ua) the walk-back, filled in
        "praise": lambda p: (f"The area is biggest when the rectangle is a "
                             f"SQUARE, and four equal sides share the "
                             f"{p['a']} metres: {p['a'] // 4} metres each. "
                             f"{p['a'] // 2} would be half the fence — two "
                             f"sides, not one — and a shape stretched long "
                             f"and thin has almost no area at all."),
        "key": lambda p: p["a"] // 4,
        # The errors: half the fence (two sides at once), and the whole
        # fence read as a side.
        "choices": lambda p: [p["a"] // 4, p["a"] // 2, p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (p["a"] % 4 == 0 and 16 <= p["a"] <= 80
                            and len({p["a"] // 4, p["a"] // 2,
                                     p["a"]}) == 3,
                            "a fence that shares four ways exactly, and "
                            "three distinct taps"),
    },
    "maxa": {  # ...and how much area that actually wins you
        "ans": lambda p: (p["a"] // 4) * (p["a"] // 4),
        "spoken": lambda p: (f"With {p['a']} metres of fence all the way "
                             f"round, the best rectangle is a square of "
                             f"side {p['a'] // 4}. What is its area, in "
                             f"square metres?"),
        "board": _maxa_board,         # (ua) the ask picture, answer withheld
        "worked": _maxa_worked,       # (ua) the walk-back, filled in
        "praise": lambda p: (f"A square of side {p['a'] // 4} has area "
                             f"{p['a'] // 4} times {p['a'] // 4} — "
                             f"{(p['a'] // 4) * (p['a'] // 4)} square "
                             f"metres. That is the most any rectangle can "
                             f"get from {p['a']} metres of fence; every "
                             f"other shape with the same fence encloses "
                             f"less."),
        "key": lambda p: (p["a"] // 4) * (p["a"] // 4),
        # The errors: the SIDE answered instead of the area, and the fence.
        "choices": lambda p: [(p["a"] // 4) * (p["a"] // 4), p["a"] // 4,
                              p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (p["a"] % 4 == 0 and 16 <= p["a"] <= 80
                            and p["b"] == 0
                            and len({(p["a"] // 4) * (p["a"] // 4),
                                     p["a"] // 4, p["a"]}) == 3,
                            "a square whose area, side and fence are three "
                            "different numbers, and a side the grid can draw "
                            "(20 at most -- build ua)"),
    },
    "sumx": {  # two numbers with a fixed sum: equal halves win
        "ans": lambda p: (p["a"] // 2) * (p["a"] // 2),
        "spoken": lambda p: (f"Two numbers add to {p['a']}. Choosing them "
                             f"to make their product as big as possible, "
                             f"what is that biggest product?"),
        "board": _sumx_board,         # (ua) the ask picture, answer withheld
        "worked": _sumx_worked,       # (ua) the walk-back, filled in
        "praise": lambda p: (f"Equal halves always win: {p['a'] // 2} and "
                             f"{p['a'] // 2} give {(p['a'] // 2) * (p['a'] // 2)}. "
                             f"Pull them apart and the product falls away — "
                             f"1 and {p['a'] - 1} give only {p['a'] - 1}. "
                             f"It is the fence problem again, wearing plain "
                             f"numbers."),
        "key": lambda p: (p["a"] // 2) * (p["a"] // 2),
        # The errors: the half answered instead of the product, and the sum.
        "choices": lambda p: [(p["a"] // 2) * (p["a"] // 2), p["a"] // 2,
                              p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (p["a"] % 2 == 0 and 6 <= p["a"] <= 32
                            and p["b"] == 0
                            and len({(p["a"] // 2) * (p["a"] // 2),
                                     p["a"] // 2, p["a"]}) == 3,
                            "an even sum whose product, half and total are "
                            "three different numbers"),
    },
    "infl": {  # where the bend itself changes sides
        "ans": lambda p: p["a"] // 3,
        "spoken": lambda p: (f"For y equals x cubed take away {p['a']} x "
                             f"squared, the second derivative is 6 x take "
                             f"away {2 * p['a']}. At which x is the SECOND "
                             f"derivative zero?"),
        "board": _infl_board,         # (ua) the ask picture, answer withheld
        "worked": _infl_worked,       # (ua) the walk-back, filled in
        "praise": lambda p: (f"6 x equals {2 * p['a']}, so x is "
                             f"{p['a'] // 3}. There the curve stops bending "
                             f"one way and starts bending the other — an "
                             f"inflection point. The slope is not zero "
                             f"there; it is the BEND that changes, which is "
                             f"a different thing entirely."),
        "key": lambda p: p["a"] // 3,
        # The errors: halving (the first-derivative habit), and the number
        # from the equation.
        "choices": lambda p: [p["a"] // 3, p["a"] // 2, p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (p["a"] % 6 == 0 and 6 <= p["a"] <= 90
                            and len({p["a"] // 3, p["a"] // 2,
                                     p["a"]}) == 3,
                            "a number that thirds AND halves cleanly, so "
                            "the halving tap is a real number, and three "
                            "distinct taps"),
    },
    # ---- build lx: Calculus U6 Antiderivatives ----------------------------
    "anti": {  # the power rule run BACKWARDS
        "ans": lambda p: p["a"] // 2,
        "spoken": lambda p: (f"Which function has a derivative of {p['a']} "
                             f"x? It looks like something times x squared — "
                             f"what is that something?"),
        "board": _anti_board,         # (ua) the ask picture, answer withheld
        "worked": _anti_worked,       # (ua) the walk-back, filled in
        "praise": lambda p: (f"Differentiating {p['a'] // 2} x squared "
                             f"doubles the {p['a'] // 2} and drops the "
                             f"power: {p['a']} x, exactly what we wanted. "
                             f"Going backwards you HALVE instead of "
                             f"doubling, so {p['a']} x squared would "
                             f"differentiate to {2 * p['a']} x — far too "
                             f"much."),
        "key": lambda p: p["a"] // 2,
        # The errors: the number copied straight over (no halving), and
        # doubling -- the forward rule run the wrong way.
        "choices": lambda p: [p["a"] // 2, p["a"], 2 * p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (p["a"] % 2 == 0 and 4 <= p["a"] <= 60
                            and p["b"] == 0
                            and len({p["a"] // 2, p["a"],
                                     2 * p["a"]}) == 3,
                            "an even front number so the halving lands "
                            "whole, and three distinct taps"),
    },
    "antp": {  # backwards through a higher power: raise, then divide
        "ans": lambda p: p["b"] // (p["a"] + 1),
        "spoken": lambda p: (f"Which function has a derivative of {p['b']} "
                             f"x to the power {p['a']}? Its power is one "
                             f"higher — {p['a'] + 1} — and its front number "
                             f"is what?"),
        "board": _antp_board,         # (ua) the ask picture, answer withheld
        "worked": _antp_worked,       # (ua) the walk-back, filled in
        "praise": lambda p: (f"Raise the power to {p['a'] + 1}, then divide "
                             f"by it: {p['b']} over {p['a'] + 1} is "
                             f"{p['b'] // (p['a'] + 1)}. Check it forwards "
                             f"— the {p['a'] + 1} comes down onto "
                             f"{p['b'] // (p['a'] + 1)} and gives {p['b']} "
                             f"back. Handing {p['b']} straight back leaves "
                             f"the dividing undone."),
        "key": lambda p: p["b"] // (p["a"] + 1),
        # The errors: the front number handed back undivided, and the new
        # power itself.
        "choices": lambda p: [p["b"] // (p["a"] + 1),
                              p["b"], p["a"] + 1],
        "check": lambda p: (2 <= p["a"] <= 8
                            and p["b"] % (p["a"] + 1) == 0
                            and 2 <= p["b"] // (p["a"] + 1) <= 12
                            and len({p["b"] // (p["a"] + 1),
                                     p["b"], p["a"] + 1}) == 3,
                            "a front number that divides by the new power "
                            "exactly, and three distinct taps"),
    },
    "plusc": {  # antiderivatives come in FAMILIES, a constant apart
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"Two functions have exactly the same "
                             f"derivative, so they sit a constant {p['b']} "
                             f"apart at every x. At x equals 4 the lower "
                             f"one is {p['a']}. What is the higher one "
                             f"there?"),
        "board": _plusc_board,         # (ua) the ask picture, answer withheld
        "worked": _plusc_worked,       # (ua) the walk-back, filled in
        "praise": lambda p: (f"They run parallel, {p['b']} apart at every "
                             f"single x, so the higher one is {p['a']} plus "
                             f"{p['b']} — {p['a'] + p['b']}. That gap is "
                             f"the plus C: an antiderivative is never one "
                             f"function but a whole family of them, stacked "
                             f"up the page."),
        "key": lambda p: p["a"] + p["b"],
        # The errors: the gap taken away instead of added, and the gap
        # itself answered.
        "choices": lambda p: [p["a"] + p["b"], p["a"] - p["b"], p["b"]],
        "check": lambda p: (5 <= p["a"] <= 60 and 2 <= p["b"] <= 30
                            and p["a"] - p["b"] >= 2
                            and len({p["a"] + p["b"], p["a"] - p["b"],
                                     p["b"]}) == 3,
                            "a real gap that still leaves the lower curve "
                            "positive, and three distinct taps"),
    },
    "init": {  # one known point picks ONE member of the family
        "ans": lambda p: p["c"] * p["c"] + p["a"],
        "spoken": lambda p: (f"A curve has slope 2 x everywhere, and passes "
                             f"through the height {p['a']} when x is zero. "
                             f"What is its height at x equals {p['c']}?"),
        "board": _init_board,         # (ua) the ask picture, answer withheld
        "worked": _init_worked,       # (ua) the walk-back, filled in
        "praise": lambda p: (f"Slope 2 x comes from x squared, plus some "
                             f"constant. At x equals zero the x squared is "
                             f"nothing, so the constant is {p['a']} itself. "
                             f"Then at {p['c']}: {p['c']} squared is "
                             f"{p['c'] * p['c']}, plus {p['a']} — "
                             f"{p['c'] * p['c'] + p['a']}. One known point "
                             f"picks one curve out of the whole family."),
        "key": lambda p: p["c"] * p["c"] + p["a"],
        # The errors: the constant forgotten, and the starting height kept
        # as though the curve never moved.
        "choices": lambda p: [p["c"] * p["c"] + p["a"],
                              p["c"] * p["c"], p["a"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["c"]) in sp),
        "check": lambda p: (2 <= p["a"] <= 30 and 2 <= p["c"] <= 9
                            and p["b"] == 0
                            and p["c"] * p["c"] != p["a"]
                            and len({p["c"] * p["c"] + p["a"],
                                     p["c"] * p["c"], p["a"]}) == 3,
                            "a height and a square that differ, with three "
                            "distinct taps"),
    },
    # ---- build lx: Calculus U7 The Definite Integral & the FTC ------------
    "defi": {  # the simplest integral of all: a rectangle
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: (f"A car holds a steady {p['a']} metres a "
                             f"second for {p['b']} seconds. On a speed "
                             f"graph that is a rectangle, and its area is "
                             f"the distance travelled. How far did it go?"),
        "board": _defi_board,         # (ub) the ask picture, answer withheld
        "worked": _defi_worked,       # (ub) the walk-back, filled in
        "praise": lambda p: (f"{p['a']} metres every second for {p['b']} "
                             f"seconds is {p['a'] * p['b']} metres — the "
                             f"rectangle's area, height times width, read "
                             f"as a distance."),
        "key": lambda p: p["a"] * p["b"],
        # The errors: the two numbers added, and the time alone.
        "choices": lambda p: [p["a"] * p["b"], p["a"] + p["b"], p["b"]],
        "check": lambda p: (2 <= p["a"] <= 20 and 2 <= p["b"] <= 12
                            and p["a"] != p["b"]
                            and p["a"] * p["b"] <= 200
                            and len({p["a"] * p["b"], p["a"] + p["b"],
                                     p["b"]}) == 3,
                            "a steady speed and a time that differ, with "
                            "three distinct taps"),
    },
    "triz": {  # a straight ramp: the area is a triangle
        "ans": lambda p: p["a"] * p["a"] // 2,
        "spoken": lambda p: (f"A car speeds up steadily so that after t "
                             f"seconds it is going t metres a second. After "
                             f"{p['a']} seconds, the area under that speed "
                             f"graph is a triangle. How far has it gone?"),
        "board": _triz_board,         # (ub) the ask picture, answer withheld
        "worked": _triz_worked,       # (ub) the walk-back, filled in
        "praise": lambda p: (f"The triangle is {p['a']} wide and {p['a']} "
                             f"tall, and a triangle takes half the "
                             f"rectangle: {p['a']} times {p['a']} halved is "
                             f"{p['a'] * p['a'] // 2} metres. Forgetting "
                             f"the half claims {p['a'] * p['a']} — the "
                             f"whole rectangle, as if the car had gone flat "
                             f"out the entire time."),
        "key": lambda p: p["a"],
        # The errors: the half forgotten (the full rectangle), and the time.
        "choices": lambda p: [p["a"] * p["a"] // 2, p["a"] * p["a"],
                              p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (p["a"] % 2 == 0 and 4 <= p["a"] <= 30
                            and p["b"] == 0
                            and len({p["a"] * p["a"] // 2, p["a"] * p["a"],
                                     p["a"]}) == 3,
                            "an even time so the half lands whole, and "
                            "three distinct taps"),
    },
    "ftc": {  # the fundamental theorem: end value take away start value
        "ans": lambda p: p["b"] * p["b"] - p["a"] * p["a"],
        "spoken": lambda p: (f"The area under y equals 2 x, from x equals "
                             f"{p['a']} to x equals {p['b']}, is found by "
                             f"working out x squared at both ends and "
                             f"taking one from the other. What is it?"),
        "board": _ftc_board,         # (ub) the ask picture, answer withheld
        "worked": _ftc_worked,       # (ub) the walk-back, filled in
        "praise": lambda p: (f"{p['b']} squared is {p['b'] * p['b']}, "
                             f"{p['a']} squared is {p['a'] * p['a']}, so "
                             f"the area is "
                             f"{p['b'] * p['b'] - p['a'] * p['a']}. That is "
                             f"the Fundamental Theorem: areas come from "
                             f"ANTIDIFFERENTIATING and taking end from "
                             f"start — the two halves of Calculus, one "
                             f"idea."),
        "key": lambda p: p["b"] * p["b"] - p["a"] * p["a"],
        # The errors: the difference SQUARED, and the plain width.
        "choices": lambda p: [p["b"] * p["b"] - p["a"] * p["a"],
                              (p["b"] - p["a"]) * (p["b"] - p["a"]),
                              p["b"] - p["a"]],
        "check": lambda p: (1 <= p["a"] and p["a"] + 2 <= p["b"] <= 14
                            and len({p["b"] * p["b"] - p["a"] * p["a"],
                                     (p["b"] - p["a"]) * (p["b"] - p["a"]),
                                     p["b"] - p["a"]}) == 3,
                            "ends far enough apart that the squared "
                            "difference is a visibly different number"),
    },
    "avgv": {  # spread the area back out: the average height
        "ans": lambda p: p["a"] // p["b"],
        "spoken": lambda p: (f"The area under a curve from x equals zero to "
                             f"x equals {p['b']} is {p['a']}. If that same "
                             f"area were a flat rectangle of the same "
                             f"width, how tall would it be?"),
        "board": _avgv_board,         # (ub) the ask picture, answer withheld
        "worked": _avgv_worked,       # (ub) the walk-back, filled in
        "praise": lambda p: (f"Spread {p['a']} of area evenly across a "
                             f"width of {p['b']} and it stands "
                             f"{p['a'] // p['b']} high — the curve's "
                             f"AVERAGE height. Some of it towers above that "
                             f"line and some falls below, and the two "
                             f"exactly trade places."),
        "key": lambda p: p["a"] // p["b"],
        # The errors: the area answered as a height, and the width.
        "choices": lambda p: [p["a"] // p["b"], p["a"], p["b"]],
        "check": lambda p: (2 <= p["b"] <= 12 and p["a"] % p["b"] == 0
                            and 2 <= p["a"] // p["b"] <= 20
                            and p["a"] <= 200
                            and len({p["a"] // p["b"], p["a"],
                                     p["b"]}) == 3,
                            "an area that flattens to a whole height, and "
                            "three distinct taps"),
    },
    # ---- build ly: Calculus U8 Applications of Integration ----------------
    "btwn": {  # two areas, one sitting inside the other
        "ans": lambda p: p["a"] - p["b"],
        "spoken": lambda p: (f"Two curves run across the same stretch. The "
                             f"area under the top one is {p['a']}, and the "
                             f"area under the bottom one is {p['b']}. How "
                             f"much area sits between them?"),
        "board": _btwn_board,         # (ub) the ask picture, answer withheld
        "worked": _btwn_worked,       # (ub) the walk-back, filled in
        "praise": lambda p: (f"The bottom curve's {p['b']} is counted inside "
                             f"the top curve's {p['a']}, so take it away and "
                             f"{p['a'] - p['b']} is what is left in the gap. "
                             f"Top take away bottom, every time — adding "
                             f"them counts the lower strip twice over."),
        "key": lambda p: p["a"] - p["b"],
        # The errors: the two areas added, and the top area answered alone.
        "choices": lambda p: [p["a"] - p["b"], p["a"] + p["b"], p["a"]],
        "check": lambda p: (2 <= p["b"] and p["b"] + 2 <= p["a"] <= 190
                            and len({p["a"] - p["b"], p["a"] + p["b"],
                                     p["a"]}) == 3,
                            "a top area comfortably above the bottom one, "
                            "and three distinct taps"),
    },
    "trap": {  # a speed that climbs: the shape under it is a trapezium
        "ans": lambda p: (p["a"] + p["b"]) * p["c"] // 2,
        "spoken": lambda p: (f"A train speeds up steadily from {p['a']} "
                             f"metres a second to {p['b']} metres a second "
                             f"over {p['c']} seconds. How far does it "
                             f"travel in that time?"),
        "board": _trap_board,         # (ub) the ask picture, answer withheld
        "worked": _trap_worked,       # (ub) the walk-back, filled in
        "praise": lambda p: (f"Its average speed is halfway between "
                             f"{p['a']} and {p['b']}, and it holds that for "
                             f"{p['c']} seconds: "
                             f"{(p['a'] + p['b']) * p['c'] // 2} metres. "
                             f"That is the trapezium under the graph — a "
                             f"rectangle and a triangle stacked, which is "
                             f"why the halving turns up again."),
        "key": lambda p: (p["a"] + p["b"]) * p["c"] // 2,
        # The errors: the half forgotten, and the top speed held throughout.
        "choices": lambda p: [(p["a"] + p["b"]) * p["c"] // 2,
                              (p["a"] + p["b"]) * p["c"], p["b"] * p["c"]],
        "check": lambda p: (2 <= p["a"] and p["a"] + 2 <= p["b"] <= 22
                            and 2 <= p["c"] <= 12
                            and (p["a"] + p["b"]) * p["c"] % 2 == 0
                            and (p["a"] + p["b"]) * p["c"] // 2 <= 190
                            and len({(p["a"] + p["b"]) * p["c"] // 2,
                                     (p["a"] + p["b"]) * p["c"],
                                     p["b"] * p["c"]}) == 3,
                            "a climb that halves to a whole distance, and "
                            "three distinct taps"),
    },
    "accu": {  # the integral ADDS ON to what was already there
        "ans": lambda p: p["c"] + p["a"] * p["b"],
        "spoken": lambda p: (f"A tank already holds {p['c']} litres. Water "
                             f"runs in at {p['a']} litres a minute for "
                             f"{p['b']} minutes. How much is in it then?"),
        "board": _accu_board,         # (ub) the ask picture, answer withheld
        "worked": _accu_worked,       # (ub) the walk-back, filled in
        "praise": lambda p: (f"{p['a']} litres a minute for {p['b']} "
                             f"minutes runs in {p['a'] * p['b']}, and that "
                             f"lands on top of the {p['c']} already there — "
                             f"{p['c'] + p['a'] * p['b']}. An integral "
                             f"measures the CHANGE, so whatever was there "
                             f"at the start still has to be counted."),
        "key": lambda p: p["c"] + p["a"] * p["b"],
        # The errors: the starting amount forgotten, and all three numbers
        # simply added.
        "choices": lambda p: [p["c"] + p["a"] * p["b"], p["a"] * p["b"],
                              p["c"] + p["a"] + p["b"]],
        "check": lambda p: (2 <= p["a"] <= 12 and 2 <= p["b"] <= 12
                            and 2 <= p["c"] <= 40 and p["a"] != p["b"]
                            and p["c"] + p["a"] * p["b"] <= 190
                            and len({p["c"] + p["a"] * p["b"],
                                     p["a"] * p["b"],
                                     p["c"] + p["a"] + p["b"]}) == 3,
                            "a start and a flow that stay in range, with "
                            "three distinct taps"),
    },
    "revo": {  # spin the area and it sweeps out a solid
        "ans": lambda p: p["a"] * p["a"] * p["b"],
        "spoken": lambda p: (f"Spin a rectangle {p['a']} tall and {p['b']} "
                             f"long about the line beneath it and it sweeps "
                             f"out a cylinder. Its volume is pi times the "
                             f"radius squared, times the length. What "
                             f"number does the pi multiply?"),
        "board": _revo_board,         # (ub) the ask picture, answer withheld
        "worked": _revo_worked,       # (ub) the walk-back, filled in
        "praise": lambda p: (f"The radius {p['a']} squares to "
                             f"{p['a'] * p['a']}, and {p['b']} lengths of "
                             f"that stack up to {p['a'] * p['a'] * p['b']} "
                             f"pi. Squaring the radius is what turns a flat "
                             f"area into a solid."),
        "key": lambda p: p["a"] * p["a"] * p["b"],
        # The errors: the squaring left out, and the radius doubled instead
        # of squared.
        "choices": lambda p: [p["a"] * p["a"] * p["b"], p["a"] * p["b"],
                              2 * p["a"] * p["b"]],
        "check": lambda p: (2 <= p["a"] <= 7 and 2 <= p["b"] <= 12
                            and p["a"] != p["b"]
                            and p["a"] * p["a"] * p["b"] <= 300
                            and len({p["a"] * p["a"] * p["b"],
                                     p["a"] * p["b"],
                                     2 * p["a"] * p["b"]}) == 3,
                            "a radius above 2 so squaring beats doubling, "
                            "and three distinct taps"),
    },
    # ---- build ly: Calculus U9 Introduction to Differential Equations -----
    "dfeq": {  # an equation that describes a RATE, not an amount
        "ans": lambda p: p["a"] - p["b"] * p["c"],
        "spoken": lambda p: (f"A differential equation says how fast "
                             f"something changes. This one says the tank "
                             f"loses {p['b']} litres every minute. It "
                             f"starts with {p['a']} litres. How many are "
                             f"left after {p['c']} minutes?"),
        "board": _dfeq_board,         # (ub) the ask picture, answer withheld
        "worked": _dfeq_worked,       # (ub) the walk-back, filled in
        "praise": lambda p: (f"{p['b']} litres a minute for {p['c']} "
                             f"minutes is {p['b'] * p['c']} gone, and "
                             f"{p['a']} take away that is "
                             f"{p['a'] - p['b'] * p['c']}. The equation "
                             f"only told you the RATE — integrating it is "
                             f"what turned the rate back into litres."),
        "key": lambda p: p["a"] - p["b"] * p["c"],
        # The errors: one minute's loss taken away, and the amount that
        # drained answered instead of the amount left.
        "choices": lambda p: [p["a"] - p["b"] * p["c"], p["a"] - p["b"],
                              p["b"] * p["c"]],
        "check": lambda p: (2 <= p["b"] <= 9 and 2 <= p["c"] <= 12
                            and p["b"] * p["c"] + 2 <= p["a"] <= 190
                            and len({p["a"] - p["b"] * p["c"],
                                     p["a"] - p["b"],
                                     p["b"] * p["c"]}) == 3,
                            "a tank that never runs dry, and three distinct "
                            "taps"),
    },
    "mixr": {  # two rates pulling against each other
        "ans": lambda p: (p["a"] - p["b"]) * p["c"],
        "spoken": lambda p: (f"Water runs into an empty tank at {p['a']} "
                             f"litres a minute and drains out at {p['b']} "
                             f"litres a minute at the same time. After "
                             f"{p['c']} minutes, how much is in it?"),
        "board": _mixr_board,         # (ub) the ask picture, answer withheld
        "worked": _mixr_worked,       # (ub) the walk-back, filled in
        "praise": lambda p: (f"The two rates pull against each other, so "
                             f"the tank really gains {p['a'] - p['b']} "
                             f"litres a minute — and over {p['c']} minutes "
                             f"that is {(p['a'] - p['b']) * p['c']}. Find "
                             f"the NET rate first, then let the time work "
                             f"on that one number."),
        "key": lambda p: (p["a"] - p["b"]) * p["c"],
        # The errors: the two rates added, and the inflow counted alone.
        "choices": lambda p: [(p["a"] - p["b"]) * p["c"],
                              (p["a"] + p["b"]) * p["c"], p["a"] * p["c"]],
        "check": lambda p: (2 <= p["b"] <= 12 and p["b"] + 2 <= p["a"] <= 22
                            and 2 <= p["c"] <= 12
                            and (p["a"] - p["b"]) * p["c"] <= 190
                            and len({(p["a"] - p["b"]) * p["c"],
                                     (p["a"] + p["b"]) * p["c"],
                                     p["a"] * p["c"]}) == 3,
                            "an inflow that beats the drain, and three "
                            "distinct taps"),
    },
    "pgrw": {  # the rate depends on how much is already there
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: (f"In this one the rate depends on the amount: "
                             f"the colony gains {p['b']} bacteria a minute "
                             f"for every single bacterium already there. "
                             f"Right now there are {p['a']}. How fast is it "
                             f"growing at this moment?"),
        "board": _pgrw_board,         # (ub) the ask picture, answer withheld
        "worked": _pgrw_worked,       # (ub) the walk-back, filled in
        "praise": lambda p: (f"Every one of the {p['a']} contributes "
                             f"{p['b']} a minute, so the rate right now is "
                             f"{p['a'] * p['b']} — and it grows as the "
                             f"colony grows."),
        "key": lambda p: p["a"] * p["b"],
        # The errors: the two numbers added, and the constant answered as
        # though the amount did not matter.
        "choices": lambda p: [p["a"] * p["b"], p["a"] + p["b"], p["b"]],
        "check": lambda p: (2 <= p["a"] <= 30 and 2 <= p["b"] <= 9
                            and p["a"] != p["b"] and p["a"] * p["b"] <= 190
                            and len({p["a"] * p["b"], p["a"] + p["b"],
                                     p["b"]}) == 3,
                            "a colony and a growth constant that differ, "
                            "and three distinct taps"),
    },
    "eqbm": {  # the amount at which the change stops
        "ans": lambda p: p["a"] // p["b"],
        "spoken": lambda p: (f"A population changes at a rate of {p['a']} "
                             f"take away {p['b']} P, where P is the "
                             f"population. Equilibrium is the P that "
                             f"drives that rate to zero. What is it?"),
        "board": _eqbm_board,         # (ub) the ask picture, answer withheld
        "worked": _eqbm_worked,       # (ub) the walk-back, filled in
        "praise": lambda p: (f"Set the rate to zero and {p['b']} P has to "
                             f"equal {p['a']}, so P is "
                             f"{p['a'] // p['b']}. Sit the population "
                             f"exactly there and nothing moves — above it "
                             f"the rate turns negative and pulls back "
                             f"down, below it the rate pushes up."),
        "key": lambda p: p["a"] // p["b"],
        # The errors: the two numbers taken away from each other, and the
        # constant answered as though it were the population itself.
        "choices": lambda p: [p["a"] // p["b"], p["a"] - p["b"], p["a"]],
        "check": lambda p: (2 <= p["b"] <= 9 and p["a"] % p["b"] == 0
                            and 2 <= p["a"] // p["b"] <= 30
                            and p["a"] <= 190
                            and len({p["a"] // p["b"], p["a"] - p["b"],
                                     p["a"]}) == 3,
                            "a rate law that balances at a whole "
                            "population, and three distinct taps"),
    },
    # ---- build lz: DiffEq U1 Introduction, Classification & Slope Fields ---
    "slpf": {  # the equation draws a dash at every point on the plane
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"A slope field draws a tiny dash at every "
                             f"point, and the equation says how steep each "
                             f"one leans. This one says d y d x equals x "
                             f"plus y. At the point where x is {p['a']} and "
                             f"y is {p['b']}, how steep is the dash?"),
        "board": lambda p: (f'[[step eq="dy/dx = x + y"]]'
                            f'[[step eq="at ({p["a"]}, {p["b"]}) · slope = '
                            f'?"]]'),
        "praise": lambda p: (f"Feed the point straight into the equation: "
                             f"{p['a']} plus {p['b']} is "
                             f"{p['a'] + p['b']}, so the dash there leans at "
                             f"a slope of {p['a'] + p['b']}. Do that at "
                             f"every point and the whole field appears — "
                             f"and the field is the equation, drawn."),
        "key": lambda p: p["a"] + p["b"],
        # The errors: the two taken away instead of added, and only the x
        # read -- half the point used, half ignored. (Timesing was the first
        # draft's third tap and reached 2,750 against an answer of 105; a
        # tap nobody would touch is a wasted tap -- lx and ly both.)
        "choices": lambda p: [p["a"] + p["b"], p["a"] - p["b"], p["a"]],
        "check": lambda p: (2 <= p["b"] and p["b"] + 2 <= p["a"] <= 60
                            and len({p["a"] + p["b"], p["a"] - p["b"],
                                     p["a"]}) == 3,
                            "a point whose two coordinates differ enough to "
                            "keep three distinct taps"),
    },
    "slpq": {  # change the law and the whole field changes with it
        "ans": lambda p: p["a"] * p["a"] - p["b"],
        "spoken": lambda p: (f"Here is a different equation over the same "
                             f"plane: d y d x equals x squared, take away "
                             f"y. At the point where x is {p['a']} and y is "
                             f"{p['b']}, how steep is the dash?"),
        "board": lambda p: (f'[[step eq="dy/dx = x² − y"]]'
                            f'[[step eq="at ({p["a"]}, {p["b"]}) · slope = '
                            f'?"]]'),
        "praise": lambda p: (f"Square the x first: {p['a']} squared is "
                             f"{p['a'] * p['a']}, and taking away the "
                             f"{p['b']} leaves {p['a'] * p['a'] - p['b']}. "
                             f"Same plane, same points, a completely "
                             f"different field — the law is what shapes it."),
        "key": lambda p: p["a"] * p["a"] - p["b"],
        # The errors: the y added instead of taken away, and the y left off
        # the end so only the bare square comes back.
        "choices": lambda p: [p["a"] * p["a"] - p["b"],
                              p["a"] * p["a"] + p["b"], p["a"] * p["a"]],
        "check": lambda p: (3 <= p["a"] <= 13 and 2 <= p["b"] <= 60
                            and p["a"] + 2 <= p["a"] * p["a"] - p["b"]
                            and len({p["a"] * p["a"] - p["b"],
                                     p["a"] * p["a"] + p["b"],
                                     p["a"] * p["a"]}) == 3,
                            "a square comfortably above the y, and three "
                            "distinct taps"),
    },
    "isoc": {  # the field read BACKWARDS: where do the equal dashes live?
        "ans": lambda p: p["a"] - p["b"],
        "spoken": lambda p: (f"Now read the field backwards. In d y d x "
                             f"equals x plus y, every dash leaning at a "
                             f"slope of {p['a']} lies along one straight "
                             f"line. Where that line crosses x equals "
                             f"{p['b']}, what is y?"),
        "board": lambda p: (f'[[step eq="dy/dx = x + y = {p["a"]}"]]'
                            f'[[step eq="at x = {p["b"]} · y = ?"]]'),
        "praise": lambda p: (f"x plus y has to come to {p['a']}, and x is "
                             f"already {p['b']}, so y is "
                             f"{p['a'] - p['b']}. That line is called an "
                             f"isocline — every dash along it leans exactly "
                             f"the same way, and drawing whole lines at a "
                             f"time is how a field gets built by hand."),
        "key": lambda p: p["a"] - p["b"],
        # The errors: the two added, and the x handed back as the y.
        "choices": lambda p: [p["a"] - p["b"], p["a"] + p["b"], p["b"]],
        "check": lambda p: (2 <= p["b"] and p["b"] + 2 <= p["a"] <= 60
                            and len({p["a"] - p["b"], p["a"] + p["b"],
                                     p["b"]}) == 3,
                            "a slope above the x it is read at, and three "
                            "distinct taps"),
    },
    "fldc": {  # join the dashes and a solution curve appears
        "ans": lambda p: p["a"] + p["b"] * p["c"],
        "spoken": lambda p: (f"A solution is what you get by joining the "
                             f"dashes. Start on the field at height "
                             f"{p['a']}, and suppose every dash along the "
                             f"way leans at a slope of {p['b']}. Follow "
                             f"them for {p['c']} across. What height do you "
                             f"land at?"),
        "board": lambda p: (f'[[step eq="start at y = {p["a"]}"]]'
                            f'[[step eq="slope {p["b"]} · for {p["c"]} '
                            f'across · y = ?"]]'),
        "praise": lambda p: (f"A slope of {p['b']} climbs {p['b']} for "
                             f"every 1 across, so {p['c']} across is "
                             f"{p['b'] * p['c']} of climb — landing at "
                             f"{p['a'] + p['b'] * p['c']}. The dashes were "
                             f"never a picture of the answer; joining them "
                             f"IS the answer."),
        "key": lambda p: p["a"] + p["b"] * p["c"],
        # The errors: the climb handed back with no starting height, and a
        # single step's worth of it.
        "choices": lambda p: [p["a"] + p["b"] * p["c"], p["b"] * p["c"],
                              p["a"] + p["b"]],
        "check": lambda p: (2 <= p["a"] <= 40 and 2 <= p["b"] <= 12
                            and 2 <= p["c"] <= 12
                            and p["a"] + p["b"] * p["c"] <= 190
                            and len({p["a"] + p["b"] * p["c"],
                                     p["b"] * p["c"],
                                     p["a"] + p["b"]}) == 3,
                            "a start and a climb that stay in range, with "
                            "three distinct taps"),
    },
    # ---- build lz: DiffEq U2 First-Order: Separable & Linear --------------
    "sepv": {  # split the letters apart, integrate, pin the constant
        "ans": lambda p: 9 * (p["a"] // 2) + p["b"],
        "spoken": lambda p: (f"The equation d y d x equals {p['a']} x "
                             f"separates and integrates to y equals half of "
                             f"{p['a']}, times x squared, plus C. The curve "
                             f"sits at height {p['b']} when x is zero. What "
                             f"is its height at x equals 3?"),
        "board": lambda p: (f'[[step eq="dy/dx = {p["a"]}x → y = '
                            f'{p["a"] // 2}x² + C"]]'
                            f'[[step eq="C = {p["b"]} · y at x = 3 = ?"]]'),
        "praise": lambda p: (f"Half of {p['a']} is {p['a'] // 2}, and 3 "
                             f"squared is 9, so the x part is "
                             f"{9 * (p['a'] // 2)} — then the C of "
                             f"{p['b']} lands on top: "
                             f"{9 * (p['a'] // 2) + p['b']}. Separating and "
                             f"integrating is the whole method; the point "
                             f"is only there to pin the C."),
        "key": lambda p: 9 * (p["a"] // 2) + p["b"],
        # The errors: the C dropped, and the halving skipped.
        "choices": lambda p: [9 * (p["a"] // 2) + p["b"], 9 * (p["a"] // 2),
                              9 * p["a"] + p["b"]],
        "check": lambda p: (p["a"] % 2 == 0 and 4 <= p["a"] <= 20
                            and 2 <= p["b"] <= 40
                            and 9 * p["a"] + p["b"] <= 190
                            and len({9 * (p["a"] // 2) + p["b"],
                                     9 * (p["a"] // 2),
                                     9 * p["a"] + p["b"]}) == 3,
                            "an even front number so the halving lands "
                            "whole, and three distinct taps"),
    },
    "sepr": {  # separating when the y will not stay on one side quietly
        "ans": lambda p: _isqrt(2 * p["a"] * p["c"] + p["b"] * p["b"]),
        "spoken": lambda p: (f"This one has y underneath: d y d x equals "
                             f"{p['a']} over y. Separating gives y d y "
                             f"equals {p['a']} d x, so y squared equals 2 "
                             f"times {p['a']} times x, plus C. The height "
                             f"is {p['b']} when x is zero. What is the "
                             f"height at x equals {p['c']}?"),
        "board": lambda p: (f'[[step eq="y² = 2·{p["a"]}x + C · C = '
                            f'{p["b"] * p["b"]}"]]'
                            f'[[step eq="at x = {p["c"]} · y = ?"]]'),
        "praise": lambda p: (f"y squared climbs to "
                             f"{2 * p['a'] * p['c'] + p['b'] * p['b']}, and "
                             f"the height is the square root of that — "
                             f"{_isqrt(2 * p['a'] * p['c'] + p['b'] * p['b'])}. "
                             f"Notice it did NOT climb in a straight line: "
                             f"separating tells you the truth about a curve "
                             f"that guessing cannot."),
        "key": lambda p: _isqrt(2 * p["a"] * p["c"] + p["b"] * p["b"]),
        # The errors: y squared answered instead of y, and a straight-line
        # guess -- the very guess the lesson exists to break.
        "choices": lambda p: [_isqrt(2 * p["a"] * p["c"] + p["b"] * p["b"]),
                              2 * p["a"] * p["c"] + p["b"] * p["b"],
                              p["b"] + p["a"] * p["c"]],
        "check": lambda p: (2 <= p["a"] <= 13 and 2 <= p["b"] <= 13
                            and 2 <= p["c"] <= 13
                            and _isqrt(2 * p["a"] * p["c"]
                                       + p["b"] * p["b"]) > p["b"]
                            and 2 * p["a"] * p["c"] + p["b"] * p["b"] <= 250
                            and len({_isqrt(2 * p["a"] * p["c"]
                                            + p["b"] * p["b"]),
                                     2 * p["a"] * p["c"] + p["b"] * p["b"],
                                     p["b"] + p["a"] * p["c"]}) == 3,
                            "a y squared that comes out a perfect square, "
                            "and three distinct taps"),
    },
    "newt": {  # the first-order LINEAR equation everybody meets first
        # NOTE (lz): the first draft read "loses {c} degrees a minute for
        # every degree of gap", which made a 30-degree gap cool at 60 degrees
        # a minute -- the coffee would reach room temperature in half a
        # minute. Real cooling constants are fractions, which integer taps
        # cannot carry, so the constant was INVERTED: one degree a minute for
        # every c degrees of gap. Same law, honest numbers.
        "ans": lambda p: (p["a"] - p["b"]) // p["c"],
        "spoken": lambda p: (f"Coffee at {p['a']} degrees stands in a room "
                             f"at {p['b']} degrees. Newton's law of cooling "
                             f"says it drops 1 degree a minute for every "
                             f"{p['c']} degrees it stands above the room. "
                             f"How fast is it cooling right now?"),
        "board": lambda p: (f'[[step eq="coffee {p["a"]}° · room '
                            f'{p["b"]}°"]]'
                            f'[[step eq="1°/min per {p["c"]}° of gap · '
                            f'rate = ?"]]'),
        "praise": lambda p: (f"The gap is {p['a'] - p['b']} degrees, and "
                             f"every {p['c']} of those is worth 1 degree a "
                             f"minute — so {(p['a'] - p['b']) // p['c']} a "
                             f"minute. The gap shrinks as it cools, so the "
                             f"cooling slows, which is why coffee never "
                             f"quite gets cold."),
        "key": lambda p: (p["a"] - p["b"]) // p["c"],
        # The errors: the gap handed back as though it were a rate, and the
        # cooling constant answered on its own.
        "choices": lambda p: [(p["a"] - p["b"]) // p["c"], p["a"] - p["b"],
                              p["c"]],
        "check": lambda p: (10 <= p["b"] <= 30
                            and 40 <= p["a"] <= 95
                            and p["b"] + 10 <= p["a"]
                            and 2 <= p["c"] <= 8
                            and (p["a"] - p["b"]) % p["c"] == 0
                            and 2 <= (p["a"] - p["b"]) // p["c"] <= 40
                            and len({(p["a"] - p["b"]) // p["c"],
                                     p["a"] - p["b"], p["c"]}) == 3,
                            "coffee comfortably hotter than the room, a gap "
                            "that shares out whole, and three distinct "
                            "taps"),
    },
    "conc": {  # the number every mixing problem is really about
        "ans": lambda p: p["a"] // p["b"],
        "spoken": lambda p: (f"A mixing problem always turns on one number. "
                             f"{p['a']} grams of salt are stirred evenly "
                             f"into {p['b']} litres of water. How many "
                             f"grams sit in each single litre?"),
        "board": lambda p: (f'[[step eq="{p["a"]} g in {p["b"]} L"]]'
                            f'[[step eq="grams per litre = ?"]]'),
        "praise": lambda p: (f"Share the {p['a']} grams out over {p['b']} "
                             f"litres and each one carries "
                             f"{p['a'] // p['b']}. That is the "
                             f"concentration — what the outflow pipe takes "
                             f"away, and why a mixing equation has the salt "
                             f"divided by the volume inside it."),
        "key": lambda p: p["a"] // p["b"],
        # The errors: the litres taken off the grams, muddling the units,
        # and the litres handed back as the concentration.
        "choices": lambda p: [p["a"] // p["b"], p["a"] - p["b"], p["b"]],
        "check": lambda p: (2 <= p["b"] <= 14 and p["a"] % p["b"] == 0
                            and 2 <= p["a"] // p["b"] <= 20
                            and p["a"] <= 190
                            and len({p["a"] // p["b"], p["a"] - p["b"],
                                     p["b"]}) == 3,
                            "a share that comes out whole, and three "
                            "distinct taps"),
    },
    # ---- build ma: DiffEq U3 Qualitative Analysis: Equilibria & Stability --
    "logi": {  # the rate law whose whole shape is the lesson
        "ans": lambda p: p["b"] * (p["a"] - p["b"]) // p["c"],
        "spoken": lambda p: (f"A pond holds at most {p['a']} fish. Logistic "
                             f"growth says the rate is the number of fish "
                             f"times the room still left, divided by "
                             f"{p['c']}. With {p['b']} fish in it now, how "
                             f"fast is the population growing?"),
        "board": lambda p: (f'[[step eq="ceiling {p["a"]} · now '
                            f'{p["b"]}"]]'
                            f'[[step eq="P × room ÷ {p["c"]} = ?"]]'),
        "praise": lambda p: (f"The room still left is {p['a']} take away "
                             f"{p['b']}, which is {p['a'] - p['b']}, so the "
                             f"rate is {p['b']} times that over {p['c']} — "
                             f"{p['b'] * (p['a'] - p['b']) // p['c']}. "
                             f"Notice both ends: almost no fish and almost "
                             f"no room BOTH give almost no growth."),
        "key": lambda p: p["b"] * (p["a"] - p["b"]) // p["c"],
        # The errors: the room left handed back as a rate, and the whole
        # ceiling used where only the room left belongs.
        "choices": lambda p: [p["b"] * (p["a"] - p["b"]) // p["c"],
                              p["a"] - p["b"],
                              p["b"] * p["a"] // p["c"]],
        "check": lambda p: (2 <= p["c"] <= 12
                            and 20 <= p["a"] <= 200
                            and 4 <= p["b"] <= p["a"] - 4
                            and p["b"] * (p["a"] - p["b"]) % p["c"] == 0
                            and p["b"] * p["a"] % p["c"] == 0
                            and 2 <= p["b"] * (p["a"] - p["b"]) // p["c"] <= 60
                            and p["b"] * p["a"] // p["c"] <= 190
                            and len({p["b"] * (p["a"] - p["b"]) // p["c"],
                                     p["a"] - p["b"],
                                     p["b"] * p["a"] // p["c"]}) == 3,
                            "a pond with room at both ends and three "
                            "distinct taps"),
    },
    "carr": {  # the non-obvious fact: growth peaks HALFWAY, not at the top
        "ans": lambda p: p["a"] // 2 - p["b"],
        "spoken": lambda p: (f"Logistic growth is fastest exactly halfway "
                             f"to the ceiling — not near the top, where "
                             f"everyone guesses. The pond's ceiling is "
                             f"{p['a']} and it holds {p['b']} fish today. "
                             f"How many more fish would take it to its "
                             f"fastest-growing size?"),
        "board": lambda p: (f'[[step eq="ceiling {p["a"]} · fastest at '
                            f'half"]]'
                            f'[[step eq="now {p["b"]} · how many more?"]]'),
        "praise": lambda p: (f"Half of {p['a']} is {p['a'] // 2}, and it is "
                             f"already at {p['b']}, so {p['a'] // 2 - p['b']} "
                             f"more fish reach the fastest-growing size. "
                             f"Past that point the pond keeps filling but "
                             f"the FILLING slows — the crowd starts getting "
                             f"in its own way."),
        "key": lambda p: p["a"] // 2 - p["b"],
        # The errors: the distance to the CEILING rather than to the halfway
        # point -- the guess the lesson exists to break -- and the halfway
        # point itself answered instead of the distance to it.
        "choices": lambda p: [p["a"] // 2 - p["b"], p["a"] - p["b"],
                              p["a"] // 2],
        "check": lambda p: (p["a"] % 2 == 0 and 20 <= p["a"] <= 190
                            and 4 <= p["b"]
                            and p["b"] + 2 <= p["a"] // 2
                            and len({p["a"] // 2 - p["b"], p["a"] - p["b"],
                                     p["a"] // 2}) == 3,
                            "a pond still short of its halfway mark, and "
                            "three distinct taps"),
    },
    "fast": {  # and how big that peak actually is
        "ans": lambda p: p["a"] * p["b"] // 4,
        "spoken": lambda p: (f"A pond grows fastest at its halfway point, "
                             f"and the size of that peak is the ceiling "
                             f"times the growth constant, divided by 4. "
                             f"With a ceiling of {p['a']} and a growth "
                             f"constant of {p['b']}, what is the fastest "
                             f"rate?"),
        "board": lambda p: (f'[[step eq="ceiling {p["a"]} · constant '
                            f'{p["b"]}"]]'
                            f'[[step eq="peak rate = {p["a"]} × {p["b"]} ÷ '
                            f'4 = ?"]]'),
        "praise": lambda p: (f"{p['a']} times {p['b']} is "
                             f"{p['a'] * p['b']}, and a quarter of that is "
                             f"{p['a'] * p['b'] // 4}. The quarter is where "
                             f"the halving shows up twice — half the fish "
                             f"and half the room, at the same moment."),
        "key": lambda p: p["a"] * p["b"] // 4,
        # The errors: the quarter never taken, and halved once instead of
        # twice.
        "choices": lambda p: [p["a"] * p["b"] // 4, p["a"] * p["b"],
                              p["a"] * p["b"] // 2],
        "check": lambda p: (p["a"] % 4 == 0 and 20 <= p["a"] <= 100
                            and 2 <= p["b"] <= p["a"] // 4 and p["b"] <= 12
                            and p["a"] * p["b"] <= 300
                            and 2 <= p["a"] * p["b"] // 4
                            and len({p["a"] * p["b"] // 4, p["a"] * p["b"],
                                     p["a"] * p["b"] // 2}) == 3,
                            "a ceiling that quarters whole, and three "
                            "distinct taps"),
    },
    "away": {  # the other kind of equilibrium: one that PUSHES
        "ans": lambda p: p["c"] * (p["b"] - p["a"]),
        "spoken": lambda p: (f"Not every equilibrium pulls things in. This "
                             f"one sits at {p['a']} and pushes away: "
                             f"anything off it moves at {p['c']} for every "
                             f"1 of distance. A population of {p['b']} is "
                             f"sitting above it. How fast is it moving "
                             f"away?"),
        "board": lambda p: (f'[[step eq="unstable at {p["a"]} · now '
                            f'{p["b"]}"]]'
                            f'[[step eq="{p["c"]} per 1 of distance · rate '
                            f'= ?"]]'),
        "praise": lambda p: (f"It stands {p['b'] - p['a']} above the "
                             f"equilibrium, and {p['c']} for each of those "
                             f"is {p['c'] * (p['b'] - p['a'])}. And it only "
                             f"gets worse — the further it goes the harder "
                             f"it is pushed. That is what UNSTABLE means."),
        "key": lambda p: p["c"] * (p["b"] - p["a"]),
        # The errors: the distance handed back as a rate, and the
        # population itself answered as though it were the speed.
        "choices": lambda p: [p["c"] * (p["b"] - p["a"]),
                              p["b"] - p["a"], p["b"]],
        "check": lambda p: (4 <= p["a"] and p["a"] + 3 <= p["b"] <= 90
                            and 2 <= p["c"] <= 9
                            and p["c"] * (p["b"] - p["a"]) <= 190
                            and len({p["c"] * (p["b"] - p["a"]),
                                     p["b"] - p["a"], p["b"]}) == 3,
                            "a population clear of the equilibrium, and "
                            "three distinct taps"),
    },
    # ---- build ma: DiffEq U4 Numerical Methods: Euler & Runge-Kutta -------
    "eulr": {  # Euler reads the slope at the START of the step and commits
        "ans": lambda p: p["a"] + 2 * p["b"] * p["b"],
        "spoken": lambda p: (f"Euler's method walks in straight steps, "
                             f"using the slope at the START of each one. "
                             f"For d y d x equals 2 x, starting at height "
                             f"{p['a']} when x is zero, take two steps of "
                             f"{p['b']}. Where does Euler land?"),
        "board": lambda p: (f'[[step eq="dy/dx = 2x · start {p["a"]} · two '
                            f'steps of {p["b"]}"]]'
                            f'[[step eq="0 climb, then 2×{p["b"]}×{p["b"]} '
                            f'· lands?"]]'),
        "praise": lambda p: (f"The first step starts where the slope is "
                             f"nothing, so it climbs nothing. The second "
                             f"starts at {p['b']}, slope {2 * p['b']}, held "
                             f"across {p['b']} — a climb of "
                             f"{2 * p['b'] * p['b']}, landing at "
                             f"{p['a'] + 2 * p['b'] * p['b']}. Euler lands "
                             f"low: it committed to an old slope."),
        "key": lambda p: p["a"] + 2 * p["b"] * p["b"],
        # The errors: the TRUE value, which Euler does not reach -- the
        # whole point of the unit -- and the climb with no starting height.
        "choices": lambda p: [p["a"] + 2 * p["b"] * p["b"],
                              p["a"] + 4 * p["b"] * p["b"],
                              2 * p["b"] * p["b"]],
        "check": lambda p: (2 <= p["a"] <= 40 and 2 <= p["b"] <= 9
                            and p["a"] + 4 * p["b"] * p["b"] <= 190
                            and len({p["a"] + 2 * p["b"] * p["b"],
                                     p["a"] + 4 * p["b"] * p["b"],
                                     2 * p["b"] * p["b"]}) == 3,
                            "a start and a step whose true landing stays in "
                            "range, and three distinct taps"),
    },
    "estp": {  # what "first order" actually buys you
        "ans": lambda p: p["a"] * p["c"] // p["b"],
        "spoken": lambda p: (f"Euler is called first order because its "
                             f"error is proportional to the step size — "
                             f"shrink the step and the error shrinks by the "
                             f"very same factor. A step of {p['b']} left an "
                             f"error of {p['a']}. What error does a step of "
                             f"{p['c']} leave?"),
        "board": lambda p: (f'[[step eq="step {p["b"]} → error '
                            f'{p["a"]}"]]'
                            f'[[step eq="step {p["c"]} → error ?"]]'),
        "praise": lambda p: (f"The step shrank from {p['b']} to {p['c']}, "
                             f"and the error follows it exactly: {p['a']} "
                             f"becomes {p['a'] * p['c'] // p['b']}. That is "
                             f"the deal Euler offers — the error only ever "
                             f"shrinks in step with the step itself, never "
                             f"faster."),
        "key": lambda p: p["a"] * p["c"] // p["b"],
        # The errors: the error left unchanged, and the error halved out of
        # habit no matter what the step actually did.
        "choices": lambda p: [p["a"] * p["c"] // p["b"], p["a"],
                              p["a"] // 2],
        "check": lambda p: (2 <= p["b"] <= 12 and 2 <= p["c"] <= 12
                            and p["c"] < p["b"] and 2 * p["c"] != p["b"]
                            and 20 <= p["a"] <= 190 and p["a"] % 2 == 0
                            and p["a"] * p["c"] % p["b"] == 0
                            and 2 <= p["a"] * p["c"] // p["b"]
                            and len({p["a"] * p["c"] // p["b"], p["a"],
                                     p["a"] // 2}) == 3,
                            "a smaller step that scales the error whole, "
                            "and three distinct taps"),
    },
    "rk4": {  # fourth order, and what that is worth
        "ans": lambda p: p["a"] // 16,
        "spoken": lambda p: (f"Runge-Kutta of fourth order is the method "
                             f"everybody actually uses. Halve the step and "
                             f"Euler's error halves — but this one's error "
                             f"divides by 16. Starting from an error of "
                             f"{p['a']}, what is left after halving the "
                             f"step once?"),
        "board": lambda p: (f'[[step eq="RK4 error {p["a"]} · halve the '
                            f'step"]]'
                            f'[[step eq="÷ 16 = ?"]]'),
        "praise": lambda p: (f"{p['a']} divided by 16 is {p['a'] // 16}. "
                             f"Halving the step twice would divide by 16 "
                             f"again — which is why a fourth-order method "
                             f"reaches an accuracy Euler could not buy with "
                             f"a thousand times the steps."),
        "key": lambda p: p["a"] // 16,
        # The errors: halving like Euler, and quartering like a second-order
        # method -- the three taps are the three convergence orders.
        "choices": lambda p: [p["a"] // 16, p["a"] // 2, p["a"] // 4],
        # ⚠️ THE b=0 TRAP AGAIN (lw bit three ops at once, and every handoff
        # since has named it). The default rule-44 check demands the digit
        # "0" in speech that never says zero -- so a=80 passed by accident
        # and a=32 failed. Every b=0 op needs its own speaks override.
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (p["a"] % 16 == 0 and 32 <= p["a"] <= 320
                            and len({p["a"] // 16, p["a"] // 2,
                                     p["a"] // 4}) == 3,
                            "an error that divides by 16 whole, and three "
                            "distinct taps"),
    },
    "evls": {  # accuracy is not free: count the slope evaluations
        "ans": lambda p: p["a"] - 4 * p["b"],
        "spoken": lambda p: (f"Accuracy is never free. Euler needs {p['a']} "
                             f"steps to reach the accuracy you want, at one "
                             f"slope evaluation each. Runge-Kutta reaches "
                             f"it in {p['b']} steps, but every step costs 4 "
                             f"evaluations. How many evaluations does "
                             f"Runge-Kutta save?"),
        "board": lambda p: (f'[[step eq="Euler {p["a"]} × 1"]]'
                            f'[[step eq="RK4 {p["b"]} × 4 · saving = ?"]]'),
        "praise": lambda p: (f"Runge-Kutta spends 4 times {p['b']}, which "
                             f"is {4 * p['b']}, against Euler's {p['a']} — "
                             f"a saving of {p['a'] - 4 * p['b']}. Four "
                             f"times the cost per step and it still wins "
                             f"easily, because it needs so very many fewer "
                             f"of them."),
        "key": lambda p: p["a"] - 4 * p["b"],
        # The errors: the step counts compared as though a step cost the
        # same in both, and RK4's bill answered as the saving.
        "choices": lambda p: [p["a"] - 4 * p["b"], p["a"] - p["b"],
                              4 * p["b"]],
        "check": lambda p: (2 <= p["b"] <= 30
                            and 4 * p["b"] + 4 <= p["a"] <= 190
                            and len({p["a"] - 4 * p["b"], p["a"] - p["b"],
                                     4 * p["b"]}) == 3,
                            "a Runge-Kutta bill comfortably under Euler's, "
                            "and three distinct taps"),
    },
    # ---- build mb: DiffEq U5 Second-Order Linear: Homogeneous -------------
    "char": {  # the discriminant again -- but now it decides a PHYSICS case
        "ans": lambda p: p["a"] * p["a"] - 4 * p["b"],
        "spoken": lambda p: (f"A damped spring obeys y double-prime, plus "
                             f"{p['a']} y prime, plus {p['b']} y, equals "
                             f"zero. Its characteristic equation is r "
                             f"squared plus {p['a']} r plus {p['b']}. What "
                             f"is {p['a']} squared, take away 4 times "
                             f"{p['b']}?"),
        "board": lambda p: (f'[[step eq="r² + {p["a"]}r + {p["b"]} = 0"]]'
                            f'[[step eq="{p["a"]}² − 4×{p["b"]} = ?"]]'),
        "praise": lambda p: (f"{p['a']} squared is {p['a'] * p['a']}, and 4 "
                             f"times {p['b']} is {4 * p['b']}, leaving "
                             f"{p['a'] * p['a'] - 4 * p['b']}. Above zero "
                             f"means two real roots and no wobble at all — "
                             f"the door closes slowly and stops. That one "
                             f"number decides how the whole spring behaves."),
        "key": lambda p: p["a"] * p["a"] - 4 * p["b"],
        # The errors: the 4 forgotten, and the two added instead of taken
        # away.
        "choices": lambda p: [p["a"] * p["a"] - 4 * p["b"],
                              p["a"] * p["a"] - p["b"],
                              p["a"] * p["a"] + 4 * p["b"]],
        "check": lambda p: (4 <= p["a"] <= 20 and 2 <= p["b"]
                            and 4 * p["b"] + 4 <= p["a"] * p["a"]
                            and p["a"] * p["a"] + 4 * p["b"] <= 300
                            and len({p["a"] * p["a"] - 4 * p["b"],
                                     p["a"] * p["a"] - p["b"],
                                     p["a"] * p["a"] + 4 * p["b"]}) == 3,
                            "a damping strong enough to keep the test "
                            "number above zero, and three distinct taps"),
    },
    "cdmp": {  # the knife-edge: the discriminant exactly zero
        "ans": lambda p: p["a"] * p["a"] // 4,
        "spoken": lambda p: (f"A door closer is critically damped when that "
                             f"test number is exactly zero — the fastest "
                             f"close with no bounce at all. With {p['a']} "
                             f"on the y prime term, what must the plain y "
                             f"term be to land exactly there?"),
        "board": lambda p: (f'[[step eq="{p["a"]}² − 4c = 0"]]'
                            f'[[step eq="c = ?"]]'),
        "praise": lambda p: (f"{p['a']} squared is {p['a'] * p['a']}, and a "
                             f"quarter of that is "
                             f"{p['a'] * p['a'] // 4} — set the plain term "
                             f"there and the test number is exactly zero. A "
                             f"hair less and the door bounces; a hair more "
                             f"and it crawls."),
        "key": lambda p: p["a"] * p["a"] // 4,
        # The errors: the square itself, and halved rather than quartered.
        "choices": lambda p: [p["a"] * p["a"] // 4, p["a"] * p["a"],
                              p["a"] * p["a"] // 2],
        # ⚠️ b=0 op. THIS BUILD WROTE TWO OF THEM AND ONLY REMEMBERED ONE --
        # natf got its override at authoring, cdmp did not, and the bank
        # half-passed because a=10 and a=20 carry a "0" of their own. Every
        # b=0 op needs this line. No exceptions, no memory required.
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (p["a"] % 2 == 0 and 4 <= p["a"] <= 30
                            and p["a"] * p["a"] <= 900
                            and len({p["a"] * p["a"] // 4, p["a"] * p["a"],
                                     p["a"] * p["a"] // 2}) == 3,
                            "an even damping so the quarter lands whole, "
                            "and three distinct taps"),
    },
    "natf": {  # strip the damping away and it never stops
        "ans": lambda p: _isqrt(p["a"]),
        "spoken": lambda p: (f"Take the damping away completely and the "
                             f"spring never stops: y double-prime plus "
                             f"{p['a']} y equals zero. It rocks at its "
                             f"natural frequency, which is the square root "
                             f"of {p['a']}. What is that?"),
        "board": lambda p: (f'[[step eq="y″ + {p["a"]}y = 0"]]'
                            f'[[step eq="natural frequency = √{p["a"]} = '
                            f'?"]]'),
        "praise": lambda p: (f"The square root of {p['a']} is "
                             f"{_isqrt(p['a'])}, so it rocks at "
                             f"{_isqrt(p['a'])} radians a second and keeps "
                             f"rocking for ever. Every object has a "
                             f"frequency like this one, and the next unit "
                             f"is about what happens when something else "
                             f"finds it."),
        "key": lambda p: _isqrt(p["a"]),
        # The errors: the number itself un-rooted, and the root doubled --
        # reaching for the other operation that undoes a square.
        "choices": lambda p: [_isqrt(p["a"]), p["a"], 2 * _isqrt(p["a"])],
        # ⚠️ b=0 op -- the default rule-44 check would demand the digit "0"
        # in speech that never says zero. (lw bit three at once; ma's rk4
        # half-passed because some of its numbers happened to contain a 0.)
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (p["b"] == 0 and _isqrt(p["a"]) >= 3
                            and p["a"] <= 300
                            and len({_isqrt(p["a"]), p["a"],
                                     2 * _isqrt(p["a"])}) == 3,
                            "a perfect square whose root is 3 or more, and "
                            "three distinct taps"),
    },
    "oscf": {  # put a little damping back and the rocking SLOWS
        "ans": lambda p: _isqrt(4 * p["b"] - p["a"] * p["a"]) // 2,
        "spoken": lambda p: (f"Now put a little damping back: y "
                             f"double-prime, plus {p['a']} y prime, plus "
                             f"{p['b']} y, equals zero. It still rocks, but "
                             f"slower — at the square root of 4 times "
                             f"{p['b']} take away {p['a']} squared, all "
                             f"halved. What is that?"),
        "board": lambda p: (f'[[step eq="4×{p["b"]} − {p["a"]}² = '
                            f'{4 * p["b"] - p["a"] * p["a"]}"]]'
                            f'[[step eq="√ then ÷ 2 = ?"]]'),
        "praise": lambda p: (f"4 times {p['b']} take away {p['a']} squared "
                             f"is {4 * p['b'] - p['a'] * p['a']}, whose "
                             f"root is "
                             f"{_isqrt(4 * p['b'] - p['a'] * p['a'])}, and "
                             f"half of that is "
                             f"{_isqrt(4 * p['b'] - p['a'] * p['a']) // 2}. "
                             f"Damping does not only shrink the swing — it "
                             f"slows the rocking down as well."),
        "key": lambda p: _isqrt(4 * p["b"] - p["a"] * p["a"]) // 2,
        # The errors: the halving skipped, and the DAMPING halved instead
        # of the root -- a over 2 is a real number in this solution, just
        # not the frequency.
        "choices": lambda p: [_isqrt(4 * p["b"] - p["a"] * p["a"]) // 2,
                              _isqrt(4 * p["b"] - p["a"] * p["a"]),
                              p["a"] // 2],
        "check": lambda p: (p["a"] % 2 == 0 and 4 <= p["a"] <= 20
                            and 2 <= p["b"] <= 240
                            and 4 * p["b"] - p["a"] * p["a"] > 0
                            and _isqrt(4 * p["b"] - p["a"] * p["a"]) % 2 == 0
                            and _isqrt(4 * p["b"]
                                       - p["a"] * p["a"]) // 2 >= 2
                            and 4 * p["b"] - p["a"] * p["a"] <= 900
                            and len({_isqrt(4 * p["b"] - p["a"] * p["a"]) // 2,
                                     _isqrt(4 * p["b"] - p["a"] * p["a"]),
                                     p["a"] // 2}) == 3,
                            "a wobble whose root halves whole, and three "
                            "distinct taps"),
    },
    # ---- build mb: DiffEq U6 Nonhomogeneous, Vibrations & Resonance -------
    "part": {  # a steady push produces a steady offset
        "ans": lambda p: p["b"] // p["a"],
        "spoken": lambda p: (f"Until now the right-hand side was zero — "
                             f"nobody pushing. Now someone leans on the "
                             f"spring with a steady force: y double-prime "
                             f"plus {p['a']} y equals {p['b']}. A steady "
                             f"push settles at a steady height. What "
                             f"height?"),
        "board": lambda p: (f'[[step eq="y″ + {p["a"]}y = {p["b"]}"]]'
                            f'[[step eq="steady y · {p["a"]}y = {p["b"]} · '
                            f'y = ?"]]'),
        "praise": lambda p: (f"A steady answer has no curvature, so the y "
                             f"double-prime is nothing and {p['a']} y has "
                             f"to equal {p['b']} on its own, so y is "
                             f"{p['b'] // p['a']}. That is a particular "
                             f"solution: guess the SHAPE of the push, then "
                             f"let the equation fix the size."),
        "key": lambda p: p["b"] // p["a"],
        # The errors: the force timesed instead of shared out, and the force
        # handed straight back as a height.
        "choices": lambda p: [p["b"] // p["a"], p["a"] * p["b"], p["b"]],
        "check": lambda p: (2 <= p["a"] <= 12 and p["b"] % p["a"] == 0
                            and 2 <= p["b"] // p["a"] <= 20
                            and p["a"] * p["b"] <= 300
                            and len({p["b"] // p["a"], p["a"] * p["b"],
                                     p["b"]}) == 3,
                            "a push that shares out whole, and three "
                            "distinct taps"),
    },
    "trns": {  # the part that fades, and how the start pins it
        "ans": lambda p: p["a"] - p["b"],
        "spoken": lambda p: (f"A pushed spring does two things at once. It "
                             f"settles toward a steady height of {p['b']}, "
                             f"and it carries a transient that fades away. "
                             f"At the very start it is at {p['a']}. How big "
                             f"is the transient part?"),
        "board": lambda p: (f'[[step eq="starts at {p["a"]} · settles at '
                            f'{p["b"]}"]]'
                            f'[[step eq="transient = ?"]]'),
        "praise": lambda p: (f"The transient is whatever the start is NOT "
                             f"explained by the steady part: {p['a']} take "
                             f"away {p['b']} is {p['a'] - p['b']}. Wait a "
                             f"while and that piece is gone, leaving only "
                             f"{p['b']} — which is why a spring forgets how "
                             f"it was let go."),
        "key": lambda p: p["a"] - p["b"],
        # The errors: the two added, and the steady height answered as
        # though the transient were the whole story.
        "choices": lambda p: [p["a"] - p["b"], p["a"] + p["b"], p["b"]],
        "check": lambda p: (2 <= p["b"] and p["b"] + 2 <= p["a"] <= 190
                            and len({p["a"] - p["b"], p["a"] + p["b"],
                                     p["b"]}) == 3,
                            "a start clear of the steady height, and three "
                            "distinct taps"),
    },
    "reso": {  # the closer the frequencies, the wilder the answer
        "ans": lambda p: p["c"] // (p["a"] - p["b"]),
        "spoken": lambda p: (f"Here is why soldiers break step on a bridge. "
                             f"The spring's natural frequency squared is "
                             f"{p['a']}, and something is shaking it at a "
                             f"frequency squared of {p['b']}. The swing it "
                             f"builds is {p['c']} divided by the gap "
                             f"between those two. How big is the swing?"),
        "board": lambda p: (f'[[step eq="natural² {p["a"]} · driver² '
                            f'{p["b"]}"]]'
                            f'[[step eq="{p["c"]} ÷ gap = ?"]]'),
        "praise": lambda p: (f"The gap is {p['a'] - p['b']}, so the swing "
                             f"is {p['c']} over that — "
                             f"{p['c'] // (p['a'] - p['b'])}. Shrink the "
                             f"gap and the swing grows; close it entirely "
                             f"and there is nothing left to divide by — it "
                             f"just grows. That is resonance."),
        "key": lambda p: p["c"] // (p["a"] - p["b"]),
        # The errors: divided by the DRIVER instead of by the gap, and the
        # force handed back undivided. (The gap itself was the first
        # draft's second tap and sat at 3 beside an answer of 47 -- the
        # small-end wasted tap, for the fifth build running.)
        "choices": lambda p: [p["c"] // (p["a"] - p["b"]),
                              p["c"] // p["b"], p["c"]],
        "check": lambda p: (2 <= p["b"] and p["b"] + 2 <= p["a"] <= 190
                            and 4 <= p["c"] <= 190
                            and p["c"] % (p["a"] - p["b"]) == 0
                            and p["c"] % p["b"] == 0
                            and p["a"] - p["b"] != p["b"]
                            and 2 <= p["c"] // (p["a"] - p["b"]) <= 60
                            and len({p["c"] // (p["a"] - p["b"]),
                                     p["c"] // p["b"], p["c"]}) == 3,
                            "a force that divides by both the gap and the "
                            "driver, and three distinct taps"),
    },
    "damp": {  # the only thing standing between resonance and ruin
        "ans": lambda p: p["a"] // (p["b"] * p["c"]),
        "spoken": lambda p: (f"At exact resonance the swing would be "
                             f"endless — except that real things have "
                             f"damping. Then the swing is the force "
                             f"{p['a']}, divided by the damping {p['b']} "
                             f"times the frequency {p['c']}. How big does "
                             f"it actually get?"),
        "board": lambda p: (f'[[step eq="force {p["a"]} · damping '
                            f'{p["b"]} · frequency {p["c"]}"]]'
                            f'[[step eq="{p["a"]} ÷ ({p["b"]}×{p["c"]}) = '
                            f'?"]]'),
        "praise": lambda p: (f"{p['b']} times {p['c']} is "
                             f"{p['b'] * p['c']}, and {p['a']} shared over "
                             f"that is {p['a'] // (p['b'] * p['c'])}. So "
                             f"damping is the only thing standing between "
                             f"resonance and ruin — and the smaller it "
                             f"gets, the bigger that swing grows."),
        "key": lambda p: p["a"] // (p["b"] * p["c"]),
        # The errors: only one of the two divisions done, and the force
        # answered undivided.
        "choices": lambda p: [p["a"] // (p["b"] * p["c"]),
                              p["a"] // p["b"], p["a"]],
        "check": lambda p: (2 <= p["b"] <= 12 and 2 <= p["c"] <= 12
                            and p["b"] != p["c"]
                            and p["a"] % (p["b"] * p["c"]) == 0
                            and 2 <= p["a"] // (p["b"] * p["c"]) <= 40
                            and p["a"] <= 190
                            and len({p["a"] // (p["b"] * p["c"]),
                                     p["a"] // p["b"], p["a"]}) == 3,
                            "a force that divides by both whole, and three "
                            "distinct taps"),
    },
    # ---- build mc: DiffEq U7 Laplace Transforms ---------------------------
    "lder": {  # the rule that turns calculus into algebra
        "ans": lambda p: p["b"] * p["c"] - p["a"],
        "spoken": lambda p: (f"The Laplace transform turns a derivative into "
                             f"a multiplication: y prime becomes s times Y, "
                             f"take away the starting height. The curve "
                             f"starts at {p['a']}. With s equal to {p['b']} "
                             f"and Y equal to {p['c']}, what does y prime "
                             f"become?"),
        "board": lambda p: (f'[[step eq="L{{y′}} = sY − y(0)"]]'
                            f'[[step eq="s={p["b"]} · Y={p["c"]} · y(0)='
                            f'{p["a"]} · = ?"]]'),
        "praise": lambda p: (f"{p['b']} times {p['c']} is "
                             f"{p['b'] * p['c']}, take away the starting "
                             f"{p['a']} — {p['b'] * p['c'] - p['a']}. That "
                             f"one rule is the whole trick: differentiating "
                             f"becomes timesing by s, so a differential "
                             f"equation turns into ordinary algebra."),
        "key": lambda p: p["b"] * p["c"] - p["a"],
        # The errors: the starting height added instead of taken away, and
        # the product handed back with the start ignored.
        "choices": lambda p: [p["b"] * p["c"] - p["a"],
                              p["b"] * p["c"] + p["a"], p["b"] * p["c"]],
        "check": lambda p: (2 <= p["b"] <= 14 and 2 <= p["c"] <= 14
                            and p["b"] != p["c"]
                            and 2 <= p["a"]
                            and p["a"] + 2 <= p["b"] * p["c"]
                            and p["b"] * p["c"] + p["a"] <= 250
                            and len({p["b"] * p["c"] - p["a"],
                                     p["b"] * p["c"] + p["a"],
                                     p["b"] * p["c"]}) == 3,
                            "a product comfortably above the starting "
                            "height, and three distinct taps"),
    },
    "lalg": {  # and now it IS algebra: solve for Y, then read it off
        "ans": lambda p: p["b"] // (p["a"] + p["c"]),
        "spoken": lambda p: (f"Transforming leaves plain algebra: s plus "
                             f"{p['a']}, all times Y, equals {p['b']}. So Y "
                             f"is {p['b']} over s plus {p['a']}. What is Y "
                             f"when s is {p['c']}?"),
        "board": lambda p: (f'[[step eq="(s + {p["a"]})Y = {p["b"]}"]]'
                            f'[[step eq="Y = {p["b"]}/(s + {p["a"]}) · at s '
                            f'= {p["c"]} · = ?"]]'),
        "praise": lambda p: (f"The bottom is {p['c']} plus {p['a']}, which "
                             f"is {p['c'] + p['a']}, and {p['b']} over that "
                             f"is {p['b'] // (p['a'] + p['c'])}. Notice "
                             f"what just happened: no calculus was done at "
                             f"all. The derivative left the problem the "
                             f"moment we transformed it."),
        "key": lambda p: p["b"] // (p["a"] + p["c"]),
        # The errors: the two bottom numbers taken away instead of added,
        # and the top handed back undivided.
        "choices": lambda p: [p["b"] // (p["a"] + p["c"]),
                              p["b"] // abs(p["c"] - p["a"])
                              if p["c"] != p["a"] else p["b"],
                              p["b"]],
        "check": lambda p: (2 <= p["a"] <= 12 and 2 <= p["c"] <= 12
                            and p["a"] != p["c"]
                            and p["b"] % (p["a"] + p["c"]) == 0
                            and p["b"] % abs(p["c"] - p["a"]) == 0
                            and 2 <= p["b"] // (p["a"] + p["c"]) <= 40
                            and p["b"] <= 240
                            and len({p["b"] // (p["a"] + p["c"]),
                                     p["b"] // abs(p["c"] - p["a"]),
                                     p["b"]}) == 3,
                            "a top that divides by both the sum and the "
                            "difference, and three distinct taps"),
    },
    "lshf": {  # the most-used line in the whole table
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"Here is the shift rule, the line of the "
                             f"table everybody uses most. A transform blows "
                             f"up at s equals {p['a']} — that is its pole. "
                             f"Multiply the original by e to the {p['b']} "
                             f"t, and every s becomes s take away "
                             f"{p['b']}. Where is the pole now?"),
        "board": lambda p: (f'[[step eq="pole at s = {p["a"]}"]]'
                            f'[[step eq="× e^({p["b"]}t) · new pole = ?"]]'),
        "praise": lambda p: (f"The whole picture slides {p['b']} to the "
                             f"right, so the pole moves from {p['a']} to "
                             f"{p['a'] + p['b']}. And the pole is not "
                             f"bookkeeping: a pole to the right of zero "
                             f"means the answer grows, one to the left "
                             f"means it dies away."),
        "key": lambda p: p["a"] + p["b"],
        # The errors: shifted the wrong way, and the original pole left
        # where it was.
        "choices": lambda p: [p["a"] + p["b"], p["a"] - p["b"], p["a"]],
        "check": lambda p: (2 <= p["b"] and p["b"] + 2 <= p["a"] <= 150
                            and len({p["a"] + p["b"], p["a"] - p["b"],
                                     p["a"]}) == 3,
                            "a pole clear of the shift, and three distinct "
                            "taps"),
    },
    "lfin": {  # read the ending without ever transforming back
        "ans": lambda p: p["b"] // p["a"],
        "spoken": lambda p: (f"Best of all, you can read where a solution "
                             f"ENDS without ever transforming back. Y is "
                             f"{p['b']}, with two things underneath it: a "
                             f"lone s, and s plus {p['a']}. Multiply by s "
                             f"and let s fall to zero: what is the final "
                             f"value?"),
        "board": lambda p: (f'[[step eq="Y = {p["b"]}/(s(s + {p["a"]}))"]]'
                            f'[[step eq="s·Y as s → 0 · = ?"]]'),
        "praise": lambda p: (f"Multiplying by s clears the lone s "
                             f"underneath, and letting s fall to zero "
                             f"leaves {p['b']} over {p['a']} — "
                             f"{p['b'] // p['a']}. The final-value theorem: "
                             f"where a thing settles, read straight off the "
                             f"transform, with no inverting at all."),
        "key": lambda p: p["b"] // p["a"],
        # The errors: the top handed back whole, and the two taken away
        # rather than shared.
        "choices": lambda p: [p["b"] // p["a"], p["b"], p["b"] - p["a"]],
        "check": lambda p: (2 <= p["a"] <= 12 and p["b"] % p["a"] == 0
                            and 2 <= p["b"] // p["a"] <= 40
                            and p["b"] <= 190
                            and len({p["b"] // p["a"], p["b"],
                                     p["b"] - p["a"]}) == 3,
                            "a top that shares out whole, and three "
                            "distinct taps"),
    },
    # ---- build mc: DiffEq U8 Linear Systems & the Phase Plane -------------
    "sysx": {  # Unit 1's slope field, one dimension up
        "ans": lambda p: p["a"] * p["b"] - p["c"],
        "spoken": lambda p: (f"Two things now change together, each one "
                             f"watching the other. Say x grows by {p['a']} "
                             f"for every x it already has, and loses 1 for "
                             f"every y. At the point where x is {p['b']} "
                             f"and y is {p['c']}, how fast is x changing?"),
        "board": lambda p: (f'[[step eq="x′ = {p["a"]}x − y"]]'
                            f'[[step eq="at ({p["b"]}, {p["c"]}) · x′ = '
                            f'?"]]'),
        "praise": lambda p: (f"{p['a']} times {p['b']} is "
                             f"{p['a'] * p['b']}, and the {p['c']} of y "
                             f"pulls it back to "
                             f"{p['a'] * p['b'] - p['c']}. Do that for y as "
                             f"well and you have an arrow at that point — "
                             f"a slope field with two directions instead of "
                             f"one."),
        "key": lambda p: p["a"] * p["b"] - p["c"],
        # The errors: the y added instead of taken away, and the x part
        # answered with the y ignored.
        "choices": lambda p: [p["a"] * p["b"] - p["c"],
                              p["a"] * p["b"] + p["c"], p["a"] * p["b"]],
        "check": lambda p: (2 <= p["a"] <= 12 and 2 <= p["b"] <= 16
                            and 2 <= p["c"]
                            and p["c"] + 2 <= p["a"] * p["b"]
                            and p["a"] * p["b"] + p["c"] <= 250
                            and len({p["a"] * p["b"] - p["c"],
                                     p["a"] * p["b"] + p["c"],
                                     p["a"] * p["b"]}) == 3,
                            "an x part comfortably above the y, and three "
                            "distinct taps"),
    },
    "nucl": {  # the lines where one of the two arrows goes flat
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: (f"Some points are special: x stops changing "
                             f"entirely where {p['a']} x equals y. That "
                             f"line is called the x-nullcline. Where x is "
                             f"{p['b']}, what is y on it?"),
        "board": lambda p: (f'[[step eq="x′ = 0 where y = {p["a"]}x"]]'
                            f'[[step eq="at x = {p["b"]} · y = ?"]]'),
        "praise": lambda p: (f"{p['a']} times {p['b']} is "
                             f"{p['a'] * p['b']}, so the nullcline passes "
                             f"through there. Along that whole line the "
                             f"arrows point straight up or straight down — "
                             f"and where the two nullclines cross, nothing "
                             f"moves at all. That crossing is an "
                             f"equilibrium."),
        "key": lambda p: p["a"] * p["b"],
        # The errors: the two added -- the honest wrong operation, and
        # small here only because that is what addition IS next to a product
        # -- and the slope used for the x as well.
        "choices": lambda p: [p["a"] * p["b"], p["a"] + p["b"],
                              p["a"] * p["a"]],
        "check": lambda p: (2 <= p["a"] <= 14 and 2 <= p["b"] <= 16
                            and p["a"] != p["b"]
                            and p["a"] * p["b"] <= 190
                            and len({p["a"] * p["b"], p["a"] + p["b"],
                                     p["a"] * p["a"]}) == 3,
                            "a slope and an x that differ, and three "
                            "distinct taps"),
    },
    "detm": {  # one number that classifies the whole picture
        "ans": lambda p: p["a"] * p["c"] - p["b"] * p["b"],
        "spoken": lambda p: (f"A system like this is carried by four "
                             f"numbers in a square: {p['a']} and {p['c']} "
                             f"down the diagonal, {p['b']} in both corners. "
                             f"Its determinant is {p['a']} times {p['c']}, "
                             f"take away {p['b']} squared. What is it?"),
        "board": lambda p: (f'[[step eq="[{p["a"]} {p["b"]}; {p["b"]} '
                            f'{p["c"]}]"]]'
                            f'[[step eq="{p["a"]}×{p["c"]} − {p["b"]}² = '
                            f'?"]]'),
        "praise": lambda p: (f"{p['a']} times {p['c']} is "
                             f"{p['a'] * p['c']}, and {p['b']} squared is "
                             f"{p['b'] * p['b']}, leaving "
                             f"{p['a'] * p['c'] - p['b'] * p['b']}. The "
                             f"determinant is the two eigenvalues "
                             f"multiplied together — so if it ever falls "
                             f"below zero, one of them is positive and you "
                             f"have a saddle."),
        "key": lambda p: p["a"] * p["c"] - p["b"] * p["b"],
        # The errors: the corners added on instead of taken off, and the
        # squaring skipped.
        "choices": lambda p: [p["a"] * p["c"] - p["b"] * p["b"],
                              p["a"] * p["c"] + p["b"] * p["b"],
                              p["a"] * p["c"] - p["b"]],
        "check": lambda p: (2 <= p["a"] <= 16 and 2 <= p["c"] <= 16
                            and 2 <= p["b"] <= 12
                            and p["b"] * p["b"] + 2 <= p["a"] * p["c"]
                            and p["a"] * p["c"] + p["b"] * p["b"] <= 300
                            and len({p["a"] * p["c"] - p["b"] * p["b"],
                                     p["a"] * p["c"] + p["b"] * p["b"],
                                     p["a"] * p["c"] - p["b"]}) == 3,
                            "a diagonal product comfortably above the "
                            "corner squared, and three distinct taps"),
    },
    "eign": {  # the two numbers that decide everything
        "ans": lambda p: p["a"] - p["b"],
        "spoken": lambda p: (f"The two eigenvalues add up to the trace — "
                             f"the sum down the diagonal. This system's "
                             f"trace is {p['a']}, and one eigenvalue has "
                             f"turned out to be {p['b']}. What is the "
                             f"other?"),
        "board": lambda p: (f'[[step eq="trace {p["a"]} = λ₁ + λ₂"]]'
                            f'[[step eq="λ₁ = {p["b"]} · λ₂ = ?"]]'),
        "praise": lambda p: (f"They have to add to {p['a']}, and one is "
                             f"{p['b']}, so the other is "
                             f"{p['a'] - p['b']}. Both above zero and "
                             f"everything races away from the origin; both "
                             f"below and it spirals in; one of each is a "
                             f"saddle. Two numbers decide the picture."),
        "key": lambda p: p["a"] - p["b"],
        # The errors: the two added, and the known eigenvalue handed back.
        "choices": lambda p: [p["a"] - p["b"], p["a"] + p["b"], p["b"]],
        "check": lambda p: (2 <= p["b"] and p["b"] + 2 <= p["a"] <= 190
                            and len({p["a"] - p["b"], p["a"] + p["b"],
                                     p["b"]}) == 3,
                            "a trace clear of the known eigenvalue, and "
                            "three distinct taps"),
    },
    # ---- build md: DiffEq U9 Nonlinear Systems & Stability ----------------
    # ⭐ THE LAST FOUR OPS IN THE COURSE.
    "lnrz": {  # up close, a curve is a line -- which is why Unit 8 mattered
        "ans": lambda p: 2 * p["b"] * p["c"],
        "spoken": lambda p: (f"A nonlinear rate law is a curve, but up "
                             f"close it is very nearly a straight line. The "
                             f"law {p['a']} take away P squared has slope 2 "
                             f"P, so at the equilibrium P equals {p['b']} "
                             f"it pulls back at 2 times {p['b']} for every "
                             f"1 of distance. You are {p['c']} away. How "
                             f"fast are you pulled back?"),
        "board": lambda p: (f'[[step eq="rate = {p["a"]} − P² · '
                            f'equilibrium P = {p["b"]}"]]'
                            f'[[step eq="2×{p["b"]} per 1 · {p["c"]} away · '
                            f'= ?"]]'),
        "praise": lambda p: (f"2 times {p['b']} is {2 * p['b']} for every 1 "
                             f"of distance, and you are {p['c']} out — "
                             f"{2 * p['b'] * p['c']}. That is "
                             f"linearisation: close to an equilibrium, "
                             f"every curved law behaves like a straight "
                             f"one."),
        "key": lambda p: 2 * p["b"] * p["c"],
        # The errors: the doubling forgotten, and the two numbers added.
        "choices": lambda p: [2 * p["b"] * p["c"], p["b"] * p["c"],
                              p["b"] + p["c"]],
        # ⚠️ The story has to be TRUE, not merely arithmetical: the rate law
        # is a take away P squared, so its equilibrium is the square root of
        # a. The first draft let a and b float free and cheerfully said "the
        # law 6 take away P squared has its equilibrium at P equals 6".
        "check": lambda p: (p["a"] == p["b"] * p["b"] and p["a"] <= 190
                            and 2 <= p["b"] <= 12
                            and 2 <= p["c"] <= 12 and p["b"] != p["c"]
                            and 2 * p["b"] * p["c"] <= 190
                            and len({2 * p["b"] * p["c"], p["b"] * p["c"],
                                     p["b"] + p["c"]}) == 3,
                            "a distance and a pull that differ, and three "
                            "distinct taps"),
    },
    "prey": {  # the most famous nonlinear system there is
        "ans": lambda p: p["a"] * p["c"] // p["b"],
        "spoken": lambda p: (f"Rabbits and foxes. Each rabbit adds {p['a']} "
                             f"new rabbits a year, and each fox eats "
                             f"{p['b']} rabbits a year. With {p['c']} "
                             f"rabbits in the wood, how many foxes hold "
                             f"that number exactly steady?"),
        "board": lambda p: (f'[[step eq="{p["c"]} rabbits × {p["a"]} born '
                            f'each"]]'
                            f'[[step eq="÷ {p["b"]} eaten per fox · foxes = '
                            f'?"]]'),
        "praise": lambda p: (f"{p['c']} rabbits breeding at {p['a']} each "
                             f"is {p['a'] * p['c']} new rabbits a year, and "
                             f"at {p['b']} eaten per fox that takes "
                             f"{p['a'] * p['c'] // p['b']} foxes to hold "
                             f"level. Neither number is steady on its own — "
                             f"each one is held in place by the other."),
        "key": lambda p: p["a"] * p["c"] // p["b"],
        # The errors: the births counted with nothing eating them, and the
        # rabbits handed back as a fox count.
        "choices": lambda p: [p["a"] * p["c"] // p["b"], p["a"] * p["c"],
                              p["c"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 12
                            and 4 <= p["c"] <= 90
                            and p["a"] * p["c"] % p["b"] == 0
                            and 2 <= p["a"] * p["c"] // p["b"] <= 60
                            and p["a"] * p["c"] <= 190
                            and len({p["a"] * p["c"] // p["b"],
                                     p["a"] * p["c"], p["c"]}) == 3,
                            "a wood whose births share out whole among the "
                            "foxes, and three distinct taps"),
    },
    "cycl": {  # what a nonlinear system does that a linear one cannot
        "ans": lambda p: p["a"] // 4,
        "spoken": lambda p: (f"Rabbits and foxes never settle — they go "
                             f"round and round, and the foxes always peak a "
                             f"quarter of a cycle after the rabbits do. If "
                             f"the whole cycle takes {p['a']} months, how "
                             f"long after the rabbits do the foxes peak?"),
        "board": lambda p: (f'[[step eq="cycle {p["a"]} months"]]'
                            f'[[step eq="foxes lag ¼ of it · = ?"]]'),
        "praise": lambda p: (f"A quarter of {p['a']} is "
                             f"{p['a'] // 4} months. That lag is what keeps "
                             f"the loop turning — each one chasing the "
                             f"other round, for ever."),
        "key": lambda p: p["a"] // 4,
        # The errors: halved rather than quartered, and the whole cycle
        # handed back as the lag.
        "choices": lambda p: [p["a"] // 4, p["a"] // 2, p["a"]],
        # ⚠️ b=0 op -- the default rule-44 check would demand the digit "0"
        # in speech that never says zero. Written FIRST, before the rest of
        # the op, exactly as the handoff insists.
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (p["b"] == 0 and p["a"] % 4 == 0
                            and 8 <= p["a"] <= 190
                            and len({p["a"] // 4, p["a"] // 2,
                                     p["a"]}) == 3,
                            "a cycle that quarters whole, and three "
                            "distinct taps"),
    },
    "chao": {  # ⭐ THE LAST OP IN THE COURSE
        "ans": lambda p: p["a"] * p["b"] ** p["c"],
        "spoken": lambda p: (f"Two weather forecasts start {p['a']} apart — "
                             f"almost the same, but not quite. In this "
                             f"system every day multiplies whatever gap "
                             f"there is by {p['b']}. After {p['c']} days, "
                             f"how far apart are they?"),
        "board": lambda p: (f'[[step eq="gap {p["a"]} · ×{p["b"]} each '
                            f'day"]]'
                            f'[[step eq="after {p["c"]} days · = ?"]]'),
        "praise": lambda p: (f"{p['b']} to the power {p['c']} is "
                             f"{p['b'] ** p['c']}, and {p['a']} of those is "
                             f"{p['a'] * p['b'] ** p['c']}. Nothing was "
                             f"random and nothing was unknown — the gap "
                             f"just multiplied its way out of sight. A "
                             f"perfectly known equation, and still no "
                             f"forecast."),
        "key": lambda p: p["a"] * p["b"] ** p["c"],
        # The errors: the days timesed instead of powered -- the guess that
        # growth is a walk -- and the starting gap forgotten.
        "choices": lambda p: [p["a"] * p["b"] ** p["c"],
                              p["a"] * p["b"] * p["c"], p["b"] ** p["c"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 6
                            and 2 <= p["c"] <= 6
                            and p["a"] * p["b"] ** p["c"] <= 190
                            and len({p["a"] * p["b"] ** p["c"],
                                     p["a"] * p["b"] * p["c"],
                                     p["b"] ** p["c"]}) == 3,
                            "a gap that stays readable after all that "
                            "doubling, and three distinct taps"),
    },
}











# =============================================================================
# RENDERERS -- problem data -> what the child sees and hears, per level.
# One function per surface, so vocabulary consistency is BY CONSTRUCTION.
# =============================================================================
def spoken_for(p, level):
    a, b = p["a"], p["b"]
    # kd: a problem may carry its own story sentence -- word problems are authored
    # per problem, and every closure/vocabulary/digits check applies to the story.
    if p.get("story"):
        return p["story"]
    if p.get("op") in OP_EXT:
        return OP_EXT[p["op"]]["spoken"](p)
    if p.get("op") == "t":
        if level == "abstract":
            return (f"What number is {_plural(a, 'ten')} and "
                    f"{_plural(b, 'one')}?")
        if level == "pictorial":
            return (f"Count if you need to. What number is "
                    f"{_plural(a, 'ten')} and {_plural(b, 'one')}?")
        return (f"Let's count together. {_plural(a, 'ten')}, and {b} more "
                f"{'one' if b == 1 else 'ones'}. What number is that?")
    if p.get("op") == "-":
        if level == "abstract":
            return f"What is {a} minus {b}?"
        if level == "pictorial":
            return f"Count the stars if you need them. What is {a} minus {b}?"
        return (f"Let's count together. {_plural(a, 'star')}, take {b} away. "
                f"How many are left?")
    if level == "abstract":
        return f"What is {a} plus {b}?"
    if level == "pictorial":
        return f"Count the stars if you need them. What is {a} plus {b}?"
    return (f"Let's count together. {_plural(a, 'star')}, then {b} more "
            f"{'star' if b == 1 else 'stars'}. How many in all?")


def board_for(p, level):
    a, b = p["a"], p["b"]
    if p.get("op") in OP_EXT:
        return OP_EXT[p["op"]]["board"](p)
    if p.get("op") == "t":
        step = f'[[step eq="{a} ten and {b} ones = ?"]]'
        if level == "abstract":
            return step
        stars = (f'[[objects emoji="⭐" groups="10" add="{b}" '
                 f'caption="one ten and {b} ones"]]')
        return stars + step
    # (sq, 2026-09-05) TWO-DIGIT NUMBERS ARE ASKED ON THE COLUMN. Jim's flags
    # 22:35/22:36: carrying and regrouping were taught over a flat line. A problem
    # with two two-digit numbers now draws [[column]] at every level -- sixty stars
    # was never a picture of 38 + 24, and the column is exactly how it is worked.
    if p.get("op") in ("+", "-") and a >= 10 and b >= 10:
        sym = "−" if p.get("op") == "-" else "+"
        return (f'[[column terms="{a}|{b}" op="{sym}" caption="line up the ones"]]'
                f'[[step eq="{a} {sym} {b} = ?"]]')
    if p.get("op") == "-":
        step = f'[[step eq="{a} − {b} = ?"]]'
        if level == "abstract":
            return step
        # (my) ⚠️ AND HERE IS WHERE THE ASYMMETRY LIVED. One line below, ADDING gets
        # add="{b}" and the child watches it happen. Taking away got a caption that
        # SAID "take 2 away" over a picture where nothing was ever taken -- so the
        # words did the teaching and the board just sat there. take="{b}" strikes
        # the ones being removed, which is how a teacher does it with counters.
        # It does NOT give the answer away: the child still has to count what is
        # left, which is the whole method this level exists to support.
        stars = (f'[[objects emoji="⭐" groups="{a}" take="{b}" '
                 f'caption="start with {a} — take {b} away, count what is left"]]')
        return stars + step
    step = f'[[step eq="{a} + {b} = ?"]]'
    if level == "abstract":
        return step
    stars = f'[[objects emoji="⭐" groups="{a}" add="{b}" caption="count every star"]]'
    return stars + step


# =============================================================================
# READING A CHILD'S OWN WORDS  (build ou, 2026-08-27)
# -----------------------------------------------------------------------------
# Jim: "I like to be able to raise my hand and ask a question... go ahead and
# preload it." The fast lane was TAP-ONLY, which is fine for a six-year-old and
# insulting to everyone else -- and a lane a child cannot answer in their own
# words is not a classroom either.
#
# ⭐ CODE READS THE ANSWER. NOT THE MODEL. EVER. The whole latency case for this
# lane is that no model sits between the child and the next sentence. Sending a
# typed answer to an LLM to be "understood" would hand back the five to ten
# seconds the lane exists to delete, and would put a guesser in charge of
# grading. So this function is a parser: pure, deterministic, and importable by
# the battery, which drives it over hundreds of real utterances.
#
# ⭐ IT REFUSES RATHER THAN GUESSES. Every answer this engine grades is a whole
# number (see ans()). When the words do not yield one, the honest outcomes are
# "ask again" or "that wants a whole number" -- never a rounded guess. Reading
# "three point five" as 3 would mark a wrong answer CORRECT, which is the one
# failure a grader must never have. int() is not used anywhere below.
#
# Returns a dict, always, one of:
#   {"kind": "value",   "value": int}   a whole number was said
#   {"kind": "notwhole","said": str}    a number, but not a whole one
#   {"kind": "unsure"}                  "I don't know" -- a real answer, not silence
#   {"kind": "none"}                    nothing usable; treat exactly like unheard
# =============================================================================
_RA_MAXLEN = 200                      # a child's answer; anything longer is noise
_RA_UNSURE = re.compile(
    r"\b(?:i\s*(?:do\s*n[o']?t|dont|don t)\s*know"
    r"|no\s*idea|not\s*sure|unsure|dunno|no\s*clue"
    r"|i\s*am\s*stuck|i'?m\s*stuck|stuck|help(?:\s*me)?"
    r"|i\s*(?:ca|can)n(?:no|')?t\b)", re.I)
# a numeral, with an optional sign and an optional decimal part
# ⚠️ (pv) A HYPHEN GLUED TO A WORD IS NOT A MINUS SIGN. Jim spoke "sixty-one
# degrees" into a Geometry angle question; the transcript came back "Si-61
# degrees" -- a stutter the recogniser hyphenated -- and this pattern read the
# "-" as a sign and returned NEGATIVE 61. The child was RIGHT (90 - 29 = 61),
# was told "Not quite", and was dropped into an AI intervention that then taught
# adding zero in a geometry lesson. One character, three visible failures.
# The sign now requires that the character before it is not a LETTER. Digits are
# deliberately still allowed ("3-5" keeps its old reading) -- the defect is a
# word prefix, and a narrow fix is the one that cannot break something else.
_RA_NUMERAL = re.compile(r"((?<![A-Za-z])-|(?<![A-Za-z])\u2212|minus\s+|negative\s+)?(\d+(?:\.\d+)?)", re.I)
_RA_WORDNUM = re.compile(
    r"(minus\s+|negative\s+)?(" + _numw.NUMWORD_PATTERN + r")", re.I)
# ⚠️ THE SPOKEN FORMS OF "NOT A WHOLE NUMBER", found by driving the parser over
# real utterances before it shipped: "1/2" was read as 2, "three point five" as 5,
# and "one half" as 1 -- each one a wrong answer that would have been graded
# CORRECT if the number happened to match. A voice lane produces exactly these
# shapes, so they are detected FIRST, before any digit is extracted.
_RA_FRACTION = re.compile(
    r"\b\d+\s*/\s*\d+\b"                                   # 1/2, 3 / 4
    r"|\b(?:point|decimal)\s+(?:\d|" + _numw.NUMWORD_PATTERN + r")"   # three point five
    r"|\b(?:half|halves|thirds?|quarters?|fourths?|fifths?"    # one half, two thirds
    r"|sixths?|sevenths?|eighths?|ninths?|tenths?)\b", re.I)


def read_answer(said):
    """Turn what the child typed or said into an answer. Pure; never raises."""
    try:
        # ⚠️ ONLY A STRING IS AN ANSWER. str(some_object) yields
        # "<object object at 0x7f3c...0>" -- whose hex address is full of digits,
        # which the numeral scan below duly read as an answer. Caught by the
        # battery's own never-raises pin, and it is the "never guess" law in
        # miniature: garbage in must be a refusal, not a number.
        if not isinstance(said, str):
            return {"kind": "none"}
        text = said.strip()[:_RA_MAXLEN]
        if not text:
            return {"kind": "none"}
        low = text.lower()

        # A fraction is a number the engine cannot be answered with. Say so
        # BEFORE the numeral scan, which would otherwise read "1/2" as 2.
        if _RA_FRACTION.search(low):
            return {"kind": "notwhole", "said": text}

        # ⚠️ THE LAST NUMBER WINS, on purpose. A child talks their way to it --
        # "3 plus 4 is 7", "12, no wait, 15" -- and the number they land on is
        # the answer they mean. Taking the first would grade their working.
        best = None
        for m in _RA_NUMERAL.finditer(low):
            sign = -1 if (m.group(1) or "").strip() in ("-", "\u2212", "minus", "negative") else 1
            raw = m.group(2)
            if "." in raw:
                whole = raw.split(".", 1)[1].strip("0") == ""
                if not whole:
                    best = ("notwhole", None)
                    continue
                raw = raw.split(".", 1)[0]
            if len(raw) > 7:
                continue          # not an answer to a lesson problem; ignore it
            try:
                best = ("value", sign * int(raw))
            except ValueError:
                continue
        if best is None:
            for m in _RA_WORDNUM.finditer(low):
                v = _numw.word_value(m.group(2))
                if v is None:
                    continue
                sign = -1 if (m.group(1) or "").strip() in ("minus", "negative") else 1
                best = ("value", sign * v)

        # "I don't know" is checked only AFTER the numbers, so "I don't know,
        # maybe seven?" is read as the guess it is rather than as a shrug.
        if best is None:
            if _RA_UNSURE.search(low):
                return {"kind": "unsure"}
            return {"kind": "none"}
        if best[0] == "notwhole":
            return {"kind": "notwhole", "said": text}
        return {"kind": "value", "value": best[1]}
    except Exception:
        return {"kind": "none"}


def choices_for(p):
    """Three tap options: the answer and its two neighbours (floor 1), shuffled by a
    FIXED per-problem rotation -- deterministic, so replays render identically.
    kc: an op may declare its OWN distractors (rounding needs the neighbouring tens,
    not +-1, or the answer is guessable by eye)."""
    v = ans(p)
    ext = OP_EXT.get(p.get("op", "+"), {})
    if "choices" in ext:
        opts = list(ext["choices"](p))
    else:
        opts = [v - 1, v, v + 1] if v > 1 else [v, v + 1, v + 2]
    k = (p["a"] * 3 + p["b"] + p.get("c", 0)) % 3
    opts = opts[k:] + opts[:k]
    return "[[choices options=\"" + " | ".join(str(o) for o in opts) + "\"]]"


def praise_for(p, index):
    a, b = p["a"], p["b"]
    if p.get("op") in OP_EXT:
        return (PRAISE_PREFIXES[index % len(PRAISE_PREFIXES)] + " "
                + OP_EXT[p["op"]]["praise"](p))
    if p.get("op") == "t":
        return (PRAISE_PREFIXES[index % len(PRAISE_PREFIXES)]
                + f" {_plural(a, 'ten')} and {_plural(b, 'one')}"
                + f" — that is {ans(p)}.")
    word = "minus" if p.get("op") == "-" else "plus"
    return (PRAISE_PREFIXES[index % len(PRAISE_PREFIXES)]
            + f" {a} {word} {b} equals {ans(p)}.")


# =============================================================================
# THE ENGINE -- a pure state machine.  step(lesson, state, event) -> (out, state)
# -----------------------------------------------------------------------------
# Events:   ("begin",)            start the lesson
#           ("answer", value)     the child answered (tap or typed int)
#           ("unheard",)          voice input could not be recognized
#           ("resume",)           the AI intervention finished; give the retest
# Outputs (dicts), by kind:
#   say        {spoken, board}                       -- narration beat, no input
#   ask        {spoken, board, choices, expected, guided, problem} -- wait for child
#   intervene  {reason, problem, expected, got, vocabulary, retest} -- AI takes over;
#              the ONLY step the model ever authors, and the engine has already chosen
#              the retest problem, so the RETURN to script is code's decision.
#   end        {spoken, graceful, mastered, problems_done}
# =============================================================================
def start(lesson, seed=None):
    """The opening state. `seed` (sz) is the ONE place chance enters the engine: it
    shuffles a times-table pass so two students do not meet the facts in the same
    order. main.py draws it; the battery passes a fixed one, so every walk replays
    byte for byte. A lesson without a table never reads it."""
    return {"phase": "teach", "i": 0,
            "level": lesson.get("levels", LEVELS)[0],
            "bank_i": 0, "done": 0, "streak": 0,
            "interventions": 0, "unheard": 0, "pending": None,
            "retest": None, "finished": False,
            # (sp) the reason question: how many times it has been missed
            "reason_tries": 0,
            # (sz) the times-table pass: the shuffle seed, which pass this is, the
            # dealt order, the fact the student is on, and the sitting's slips
            "table_seed": int(seed or 0), "table_pass": 0, "table_order": [],
            "table_i": 0, "table_misses": 0}


# =============================================================================
# (sp, 2026-09-05) THE SHAPE'S HELPERS. Each reads an OPTIONAL lesson field and
# returns nothing for a lesson that does not carry it, so the 359 lessons authored
# before the shape play exactly as they did.
# =============================================================================
def _spoken_name(text):
    """A curriculum name the way it is SAID: "&" is "and", a slash is "and"."""
    return " ".join(str(text or "").replace("&", "and").replace("/", "and").split())


def lesson_intro(lesson):
    """(ts, 2026-09-06) THE LESSON INTRODUCES ITSELF. Jim, back after a day away:
    "Welcome back -- let's pick up where you left off" and then the why beat of a
    Pre-Algebra lesson, mid-sentence into the course -- "I have no idea what it is
    referring to." The old teach beats opened by naming the unit ("Unit Seven reads
    shapes...", "Today we count past ten"); the shape's why beat opens on the WHY,
    and that orientation was lost -- the 22:16 "no introduction" flag, back in a
    new costume. This is the engine's answer, for every lesson in every course, on a
    fresh start and on a return alike: one spoken line and one board card that say
    where the student is -- the course, the unit and its name, which lesson of the
    unit this is, and what it teaches -- BEFORE the why. Returns (spoken, board).
    Pure: reads the lesson and the curriculum's titles; the walk-back and closure
    machinery carry the line like any other."""
    import curriculum as _cur
    course, unit = lesson["course"], lesson["unit"]
    title = _cur.course_title(course)
    uname = dict(_cur.units_for(course)).get(unit, "")
    sibs = [l for l in LESSONS if l["course"] == course and l["unit"] == unit]
    order = {lid: i for i, lid in enumerate(COURSE_ORDER)}
    sibs.sort(key=lambda l: order.get(l["id"], 10 ** 6))
    n = len(sibs)
    i = next((k + 1 for k, l in enumerate(sibs) if l["id"] == lesson["id"]), 1)
    topic = str(lesson.get("topic") or "").strip()
    spoken = (f"{_spoken_name(title)}, Unit {unit}: {_spoken_name(uname)}. "
              f"Lesson {i} of {n}: {_spoken_name(topic)}.")
    board = (f'[[write lines="{title} · Unit {unit} | {uname} | '
             f'Lesson {i} of {n} · {topic}"]]')
    return spoken, board


def _beats(lesson, field):
    """The `say` beats of an authored section (why / picture / recap), or []."""
    return [{"kind": "say", "spoken": spoken, "board": board}
            for spoken, board in (lesson.get(field) or [])]


def _worked_for(p):
    """The walk-back for a solved problem: (spoken, board), or None if the op has
    no worked picture yet. The board is the same picture the worked examples use,
    filled in for THIS problem."""
    op = p.get("op", "+")
    ext = OP_EXT.get(op, {})
    fn = ext.get("worked") or BASE_WORKED.get(op)   # (sq) base ops draw too
    if fn is None:
        return None
    spoken, board = fn(p)
    return (spoken, board)


def _correct_beats(lesson, p, idx):
    """What a right answer earns: the praise line, then -- ruling ⑤, in a lesson that
    says so -- the walk-back: "Look what you did..." over the worked board."""
    out = [{"kind": "say", "spoken": praise_for(p, idx), "board": ""}]
    if lesson.get("show_work_on_correct"):
        w = _worked_for(p)
        if w:
            out.append({"kind": "say", "spoken": w[0], "board": w[1]})
    return out


def _reason_options(lesson):
    """The reason question's options in the order the buttons show them: rotated by
    a FIXED per-lesson turn (like choices_for), so the right reason is not always
    first and a replay renders identically."""
    ex = lesson.get("explain") or {}
    opts = [o.strip() for o in str(ex.get("choices", "")).split("|") if o.strip()]
    if not opts:
        return []
    k = len(str(ex.get("spoken", ""))) % len(opts)
    return opts[k:] + opts[:k]


def reason_choices_for(lesson):
    """The [[choices]] tag for the reason question -- text options, same tag, same
    buttons on every page."""
    return "[[choices options=\"" + " | ".join(_reason_options(lesson)) + "\"]]"


def _reason_norm(s):
    return re.sub(r"\s+", " ", str(s or "").strip().lower()).rstrip(".!?")


def reason_right(lesson, said):
    """Is this tapped (or typed) label the authored reason? Pure; never raises."""
    try:
        ex = lesson.get("explain") or {}
        return _reason_norm(said) == _reason_norm(ex.get("answer", "")) and \
            bool(_reason_norm(said))
    except Exception:  # noqa: BLE001
        return False


def reason_option_for(lesson, said):
    """Which option a free-typed answer names, if any (exact label, case-blind), so a
    student who types the reason instead of tapping it is graded the same. Returns
    the option text or ""."""
    try:
        want = _reason_norm(said)
        for o in _reason_options(lesson):
            if _reason_norm(o) == want:
                return o
    except Exception:  # noqa: BLE001
        pass
    return ""


def _ask_reason(state, lesson, spoken=None):
    """Beat six. An `ask` with reason=True: no problem, text choices, tap only."""
    ex = lesson["explain"]
    out = {"kind": "ask", "spoken": (spoken if spoken is not None else ex["spoken"]),
           "board": ex.get("board", ""), "choices": reason_choices_for(lesson),
           "expected": ex["answer"], "guided": False, "problem": None,
           "reason": True, "tap_only": True}
    state["pending"] = {"problem": None, "guided": False, "reason": True,
                        "expected": ex["answer"]}
    return out


def _end(lesson, state, spoken, mastered):
    """Beat seven's first half: the recap, then the end line. EVERY end of a lesson
    passes through here, so a lesson that carries a recap says it whether the student
    mastered the idea or is still learning it -- the still-learning student needs to
    hear the rule again more, not less."""
    state["finished"] = True
    return _beats(lesson, "recap") + [
        {"kind": "end", "spoken": spoken, "graceful": True, "mastered": mastered,
         "problems_done": state["done"]}]


def _problem_key(p):
    return (p.get("op", "+"), p["a"], p["b"], p.get("c", 0))


def _next_bank_problem(lesson, state):
    """The next unused bank problem; the bank wraps if the retest path consumed it."""
    bank = lesson["bank"]
    p = bank[state["bank_i"] % len(bank)]
    state["bank_i"] += 1
    return p


# =============================================================================
# (sz, 2026-09-05) THE TIMES-TABLE PASS. Rulings ⑥ ⑦ (see the settings above).
# The pass is dealt from a seeded shuffle and STORED in the state, so a replay of
# the same seed is the same pass and the engine stays a pure function of its state.
# Nothing in the pass reaches the model: a slip draws the fact's own picture (the
# array, count-by spoken down the rows), says the restart line, and deals a fresh
# shuffle. The pass counter rides the ask's board as the step's caption -- "fact 12
# of 81" -- so every page that draws a [[step]] shows it with no page change.
# =============================================================================
_BY_WORDS = {1: "ones", 2: "twos", 3: "threes", 4: "fours", 5: "fives",
             6: "sixes", 7: "sevens", 8: "eights", 9: "nines"}


def table_facts():
    """The 81 facts, in table order (1 × 1 first, 9 × 9 last). Public: the battery
    and the validator enumerate the pass from here, never from a copy."""
    return [{"a": a, "b": b, "op": "*"}
            for a in range(1, TABLE_MAX + 1) for b in range(1, TABLE_MAX + 1)]


def _table_order(seed, pass_n):
    """One pass's order: the 81 facts shuffled by the seed AND the pass number, so a
    restart deals a different order from the same seed."""
    import random
    facts = table_facts()
    random.Random(int(seed) * 1009 + int(pass_n)).shuffle(facts)
    return facts


def _table_praise_index(p):
    """One praise line per fact (not five): the pass is 81 facts long, and five
    variants of each would put 405 lines in the closure for the same warmth."""
    return (p["a"] * 3 + p["b"]) % len(PRAISE_PREFIXES)


def _table_board(p, pass_n, n):
    cap = (f"fact {n} of {TABLE_SIZE}" if pass_n <= 1
           else f"try {pass_n} · fact {n} of {TABLE_SIZE}")
    return f'[[step eq="{p["a"]} × {p["b"]} = ?" caption="{cap}"]]'


def _table_miss(p):
    """What a slipped fact earns: its picture, counted down the rows, and the fact
    said whole. Never "Look what you did" -- the student did not."""
    a, b = p["a"], p["b"]
    counts = ", ".join(str(b * i) for i in range(1, a + 1))
    return (f"Not that one. {_plural(a, 'row')} of {b} — count by {_BY_WORDS[b]}: "
            f"{counts}. {a} times {b} equals {a * b}.",
            f'[[array rows="{a}" cols="{b}" caption="{a} × {b} = {a * b}"]]')


def _table_begin(state):
    """Deal a pass: the first, or a fresh shuffle after a slip."""
    state["table_pass"] = state.get("table_pass", 0) + 1
    state["table_order"] = _table_order(state.get("table_seed", 0), state["table_pass"])
    state["table_i"] = 0


def _table_ask(state):
    p = state["table_order"][state["table_i"]]
    return _ask(state, p, board=_table_board(p, state["table_pass"], state["table_i"] + 1))


def _ask(state, p, guided=False, board=None):
    """An ask. `board` (sz) overrides board_for -- the table pass writes its counter
    on the step -- and the board is REMEMBERED in pending so a re-ask after an
    unheard answer draws the same one."""
    out = {"kind": "ask", "spoken": spoken_for(p, state["level"]),
           "board": (board if board is not None else board_for(p, state["level"])),
           "choices": choices_for(p),
           "expected": ans(p), "guided": guided, "problem": p,
           "tap_only": state["unheard"] >= 2}
    state["pending"] = {"problem": p, "guided": guided, "board": out["board"]}
    return out


def step(lesson, state, event):
    """One engine transition. Returns (list_of_output_steps, state). Pure."""
    kind = event[0]
    out = []

    if state["finished"]:
        return ([{"kind": "end", "spoken": "", "graceful": True,
                  "mastered": False, "problems_done": state["done"]}], state)

    if kind == "begin":
        # (ts) the lesson introduces itself -- course, unit, lesson, topic -- first
        _isp, _ibd = lesson_intro(lesson)
        out.append({"kind": "say", "spoken": _isp, "board": _ibd})
        # (sp) the shape: WHY the skill exists, then the PICTURE, then the rule --
        # in that order, so the rule summarises what the picture already showed.
        # A lesson without the two new fields opens on its teach beats as before.
        out.extend(_beats(lesson, "why"))
        out.extend(_beats(lesson, "picture"))
        for spoken, board in lesson["teach"]:
            out.append({"kind": "say", "spoken": spoken, "board": board})
        pair = lesson["pairs"][0]
        out.append({"kind": "say", "spoken": pair["worked"][0],
                    "board": pair["worked"][1]})
        out.append(_ask(state, pair["ask"], guided=True))
        state["phase"] = "pair-0"
        return (out, state)

    if kind == "unheard":
        state["unheard"] += 1
        # (sp) the reason question re-asks itself the same two ways a problem does
        if (state["pending"] or {}).get("reason"):
            re_spoken = LINE_TAP if state["unheard"] >= 2 else (
                LINE_REASK + " " + lesson["explain"]["spoken"])
            return ([_ask_reason(state, lesson, spoken=re_spoken)], state)
        p = state["pending"]["problem"]
        guided = state["pending"]["guided"]
        re_spoken = LINE_TAP if state["unheard"] >= 2 else (
            LINE_REASK + " " + spoken_for(p, state["level"]))
        # (sz) the same board as the first ask (the pass counter survives a re-ask)
        asked = _ask(state, p, guided=guided, board=state["pending"].get("board"))
        asked["spoken"] = re_spoken
        return ([asked], state)

    if kind == "resume":
        # The AI intervention is over. The engine -- not the model -- decides what
        # happens next: the retest problem it already chose, or (at the cap) the
        # warm close. The model never picks where the child lands.
        p = state["retest"]
        state["retest"] = None
        if p is None:
            return (_end(lesson, state, LINE_END_GRACEFUL, mastered=False), state)
        return ([_ask(state, p, guided=False)], state)

    if kind != "answer":
        return ([], state)

    state["unheard"] = 0
    pend = state["pending"]

    # ---- (sp) beat six: THE REASON QUESTION, graded in code ----------------------
    # Right: the lesson is mastered -- the student can say WHY, not only what. A miss
    # replays the PICTURE (never a lecture, never the model) and asks once more; a
    # second miss ends warmly as still-learning, where the warm choice (sn) lets the
    # student review or go on. The star moves on the tap exactly as on a problem
    # (main.py grades the label against the same answer before calling here).
    if (pend or {}).get("reason"):
        if reason_right(lesson, event[1]):
            out.append({"kind": "say", "spoken": LINE_REASON_RIGHT, "board": ""})
            out.extend(_end(lesson, state, lesson["advance_line"], mastered=True))
            return (out, state)
        state["reason_tries"] = state.get("reason_tries", 0) + 1
        out.append({"kind": "say", "spoken": LINE_REASON_WRONG, "board": ""})
        out.extend(_beats(lesson, "picture"))
        if state["reason_tries"] < REASON_TRIES:
            out.append(_ask_reason(state, lesson))
            return (out, state)
        out.extend(_end(lesson, state, LINE_END_GRACEFUL, mastered=False))
        return (out, state)

    p, guided = pend["problem"], pend["guided"]
    correct = (event[1] == ans(p))

    if correct:
        idx = state["done"]
        if state["phase"] == "table":
            # (sz) inside the pass a right answer earns the praise and the next fact --
            # no walk-back: the pass is recall, and 81 pictures would make it an hour
            out.append({"kind": "say", "spoken": praise_for(p, _table_praise_index(p)),
                        "board": ""})
        else:
            out.extend(_correct_beats(lesson, p, idx))  # (sp) praise, then the walk-back
        if not guided:
            state["done"] += 1
            state["streak"] += 1
        # ---- where next? ----
        if state["phase"] == "pair-0":
            pair = lesson["pairs"][1]
            out.append({"kind": "say", "spoken": pair["worked"][0],
                        "board": pair["worked"][1]})
            out.append(_ask(state, pair["ask"], guided=True))
            state["phase"] = "pair-1"
            return (out, state)
        if state["phase"] == "pair-1":
            out.append({"kind": "say", "spoken": lesson["practice_intro"],   # (uq) a card, never a blank board
                        "board": PRACTICE_INTRO_BOARD})
            if lesson.get("mastery") == "table":
                # (sz) the table lesson practices as a PASS, not a streak
                state["phase"] = "table"
                _table_begin(state)
                out.append(_table_ask(state))
                return (out, state)
            state["phase"] = "practice"
            out.append(_ask(state, _next_bank_problem(lesson, state)))
            return (out, state)
        if state["phase"] == "table":
            # (sz) THE PASS. The next fact, or -- all 81 right in one go -- the reason
            # question and the mastered end, exactly as a streak earns them.
            state["table_i"] += 1
            if state["table_i"] < TABLE_SIZE:
                out.append(_table_ask(state))
                return (out, state)
            if lesson.get("explain"):
                state["phase"] = "explain"
                out.append(_ask_reason(state, lesson))
                return (out, state)
            out.extend(_end(lesson, state, lesson["advance_line"], mastered=True))
            return (out, state)
        # practice
        # (ri, 2026-09-01) the gate is the PROMISE: "Three right answers in a row
        # and we're done." Jim's ruling -- no fourth problem for a perfect child.
        if state["streak"] >= ADVANCE_STREAK:
            # (sp) a lesson that carries a reason question asks it HERE, between the
            # streak and the end line: three right answers earn the question, and the
            # reason earns the lesson.
            if lesson.get("explain"):
                state["phase"] = "explain"
                out.append(_ask_reason(state, lesson))
                return (out, state)
            out.extend(_end(lesson, state, lesson["advance_line"], mastered=True))
            return (out, state)
        if state["done"] >= MAX_PROBLEMS:
            out.extend(_end(lesson, state, LINE_END_GRACEFUL, mastered=False))
            return (out, state)
        out.append(_ask(state, _next_bank_problem(lesson, state)))
        return (out, state)

    # ---- (sz) a slip inside the times-table pass: NOT a doorway to the AI ----
    # Ruling ⑦: the fact's working is shown, then the pass restarts on a fresh
    # shuffle. The picture is authored per fact (_table_miss), so nothing here needs
    # the model, and the level never drops -- a table is recall, asked bare. After
    # TABLE_MAX_MISSES slips in one sitting the student is released warmly.
    if state["phase"] == "table":
        state["streak"] = 0
        state["done"] += 1
        state["table_misses"] = state.get("table_misses", 0) + 1
        spoken, board = _table_miss(p)
        out.append({"kind": "say", "spoken": spoken, "board": board})
        if state["table_misses"] >= TABLE_MAX_MISSES:
            out.append({"kind": "say", "spoken": LINE_TABLE_REST, "board": ""})
            out.extend(_end(lesson, state, LINE_END_GRACEFUL, mastered=False))
            return (out, state)
        out.append({"kind": "say", "spoken": LINE_TABLE_RESTART, "board": ""})
        _table_begin(state)
        out.append(_table_ask(state))
        return (out, state)

    # ---- wrong answer: the ONE doorway to the AI ----
    state["streak"] = 0
    if not guided:
        state["done"] += 1
    state["interventions"] += 1
    if state["interventions"] >= DROP_AFTER_INTERVENTIONS:
        lv = lesson.get("levels", LEVELS)
        li = lv.index(state["level"])
        if li + 1 < len(lv):
            state["level"] = lv[li + 1]
            state["interventions"] = 0
        else:
            # already at concrete and still failing: end warmly, mark "learning"
            out.append({"kind": "say", "spoken": LINE_WRONG, "board": ""})
            out.extend(_end(lesson, state, LINE_END_GRACEFUL, mastered=False))
            return (out, state)
    # AT THE CAP, THE ERROR IS STILL CORRECTED BUT NO RETEST FOLLOWS: the AI's
    # Model-Lead-Test runs (never leave a child with an uncorrected error), and
    # "resume" then ends the practice gracefully instead of asking an eleventh
    # problem. Found by the alternating right/wrong scenario in build js's own
    # dry run -- the cap only guarded the CORRECT path, and `done` reached 11.
    retest = None
    if state["done"] < MAX_PROBLEMS:
        retest = _next_bank_problem(lesson, state)
    state["retest"] = retest
    out.append({"kind": "say", "spoken": LINE_WRONG, "board": ""})
    out.append({"kind": "intervene", "reason": "wrong_answer", "problem": p,
                "expected": ans(p), "got": event[1],
                "vocabulary": {k: k for k in VOCABULARY},
                "level": state["level"], "retest": retest,
                # (ta) the board the student is looking at -- the ask's own, as drawn
                "board": (pend or {}).get("board") or board_for(p, state["level"])})
    return (out, state)


# =============================================================================
# THE TOPIC QUIZ  (build ov, 2026-08-27)
# -----------------------------------------------------------------------------
# Jim's flip order made this lane the main road, and a child on the main road
# hits the end of a topic and needs a QUIZ -- until this build they hit a wall
# and had to cross to the slow lane to be assessed.
#
# ⭐ A QUIZ IS NOT A LESSON, SO IT IS NOT THE LESSON'S STATE MACHINE. step() is
# a teaching machine: it re-levels, it fetches the AI on a wrong answer, it
# praises by name. Every one of those is exactly wrong in a quiz, and bending
# step() to suppress them would put the assessment and the teaching in one
# tangle where a change to either could quietly corrupt the other. So the quiz
# is its own tiny linear machine, right here, and NOTHING in it can reach the
# model.
#
# ⭐ THE QUESTION SET IS FIXED AND PURE. quiz_problems() (drillpool.py, which
# owns "more problems from this lesson") is a deterministic function of the
# lesson alone -- never of what this child happened to be asked -- so
# audio_lines() can enumerate every sentence a quiz will ever speak, and the
# closure property holds: rendered once, free forever. A quiz that picked its
# questions at runtime would be a live TTS call per child per question.
#
# ⭐ THE SCORE IS BOARD WORK, NOT SPEECH. See the note on the lines above.
# =============================================================================
def quiz_start(lesson, problems):
    """Open a quiz over an ALREADY-CHOSEN question list. Returns (steps, state)."""
    ps = list(problems or [])[:QUIZ_LEN]
    if len(ps) < QUIZ_MIN:
        return ([], None)                     # this lesson cannot field a quiz
    level = lesson.get("levels", LEVELS)[-1]  # a quiz asks at the lesson's own top level
    state = {"i": 0, "correct": 0, "problems": ps, "level": level,
             "total": len(ps), "finished": False}
    out = [{"kind": "say", "spoken": LINE_QUIZ_INTRO[len(ps)], "board": ""}]
    out.append(_quiz_ask(state))
    return (out, state)


def _quiz_ask(state):
    p = state["problems"][state["i"]]
    return {"kind": "qask", "spoken": spoken_for(p, state["level"]),
            "board": board_for(p, state["level"]), "choices": choices_for(p),
            "n": state["i"] + 1, "total": state["total"]}


def quiz_answer(lesson, state, value):
    """Grade ONE quiz answer in code. Returns (steps, state). Never teaches, never
    re-asks, never reaches a model -- the next question follows immediately."""
    if not state or state.get("finished"):
        return ([], state)
    p = state["problems"][state["i"]]
    right = (value == ans(p))
    if right:
        state["correct"] += 1
    out = [{"kind": "say", "spoken": (LINE_QUIZ_RIGHT if right else LINE_QUIZ_WRONG),
            "board": ""}]
    state["i"] += 1
    if state["i"] < state["total"]:
        out.append(_quiz_ask(state))
        return (out, state)
    state["finished"] = True
    pct = (state["correct"] * 100) // state["total"]
    passed = pct >= QUIZ_PASS_PCT
    out.append({"kind": "qend", "spoken": (LINE_QUIZ_PASS if passed else LINE_QUIZ_FAIL),
                "board": "", "correct": state["correct"], "total": state["total"],
                "pct": pct, "passed": passed})
    return (out, state)


def quiz_audio_lines(lesson, problems):
    """Every sentence a quiz on THIS lesson can speak (the closure's quiz half)."""
    lines = set(LINE_QUIZ_INTRO.values())
    lines.update([LINE_QUIZ_RIGHT, LINE_QUIZ_WRONG, LINE_QUIZ_PASS, LINE_QUIZ_FAIL])
    level = lesson.get("levels", LEVELS)[-1]
    for p in list(problems or [])[:QUIZ_LEN]:
        lines.add(spoken_for(p, level))
    return lines


# =============================================================================
# THE AUDIO CLOSURE -- every spoken string a lesson can ever emit.
# =============================================================================
def audio_lines(lesson):
    lines = set()
    lines.add(lesson_intro(lesson)[0])   # (ts) the lesson's own introduction
    for spoken, _board in lesson["teach"]:
        lines.add(spoken)
    # (sp) the shape's authored beats: why, picture, recap
    for field in ("why", "picture", "recap"):
        for spoken, _board in (lesson.get(field) or []):
            lines.add(spoken)
    for pair in lesson["pairs"]:
        lines.add(pair["worked"][0])
    lines.add(lesson["practice_intro"])
    problems = list(lesson["bank"]) + [pair["ask"] for pair in lesson["pairs"]]
    for p in problems:
        for level in lesson.get("levels", LEVELS):
            lines.add(spoken_for(p, level))
            lines.add(LINE_REASK + " " + spoken_for(p, level))
        for i in range(len(PRAISE_PREFIXES)):
            lines.add(praise_for(p, i))
        # (sp) the walk-back after a right answer, one per problem
        if lesson.get("show_work_on_correct"):
            w = _worked_for(p)
            if w:
                lines.add(w[0])
    lines.update([LINE_WRONG, LINE_TAP, LINE_END_GRACEFUL,
                  lesson["advance_line"]])
    # (sz) the times-table pass: every one of the 81 facts asked and re-asked, its one
    # praise line, its slip picture's words, and the pass's two standing lines
    if lesson.get("mastery") == "table":
        for p in table_facts():
            for level in lesson.get("levels", LEVELS):
                lines.add(spoken_for(p, level))
                lines.add(LINE_REASK + " " + spoken_for(p, level))
            lines.add(praise_for(p, _table_praise_index(p)))
            lines.add(_table_miss(p)[0])
        lines.update([LINE_TABLE_RESTART, LINE_TABLE_REST])
    # (sp) the reason question: asked, re-asked, and its two verdicts
    if lesson.get("explain"):
        lines.add(lesson["explain"]["spoken"])
        lines.add(LINE_REASK + " " + lesson["explain"]["spoken"])
        lines.update([LINE_REASON_RIGHT, LINE_REASON_WRONG])
    # build ov: the TOPIC QUIZ's own sentences.
    # ⚠️ READ THE PINNED TABLE, NEVER drillpool. The first draft called
    # drillpool.quiz_problems() here, and the profiler caught what that meant:
    # validate() calls audio_lines(), pool_for() calls validate() thousands of
    # times per lesson, and quiz_problems() falls back to a pool scan for any
    # lesson id it does not recognise -- which every SYNTHETIC candidate lesson
    # the pool builder makes is. One line put a minutes-long scan inside the
    # validator's inner loop (13,729 recursive calls in a single 20-second
    # profile). It also pointed a dependency backwards: drillpool imports THIS
    # module. quizsets.py is pure data and is the very set the audio is rendered
    # against, so it is both the fast answer and the correct one. Guarded,
    # because a missing table must cost the app its quizzes, never its lessons.
    try:
        import quizsets as _qs
        lines.update(quiz_audio_lines(lesson, _qs.QUIZ_SETS.get(lesson.get("id")) or []))
    except Exception:
        pass
    return sorted(lines)


# =============================================================================
# LINES THAT BELONG TO NO SINGLE LESSON  (build mk, 2026-08-23)
# -----------------------------------------------------------------------------
# THE CLOSURE PROPERTY, restated: every line the app can ever speak in Mr. Cadabra's
# voice must be enumerable in advance, so it is rendered once and free forever. Until
# now every such line lived inside a lesson and audio_lines(lesson) found it. Abrabot's
# introduction is the first that belongs to the COURSE rather than to any lesson --
# Mr. Cadabra says it once, on a page that is not a lesson at all.
#
# ⚠️ SO IT HAS TO BE ENUMERATED HERE, NOT WHEREVER IT IS SPOKEN. main.py had SIX
# separate places building the closure as {s for les in LESSONS for s in
# audio_lines(les)} -- the prewarm, the dry-run, the clip audit, the model split, the
# eviction guard and the byte estimator. A line these six disagree about is a line that
# is rendered but not protected, or protected but never rendered, or billed twice.
# course_audio_lines() is now the ONE answer and all six ask it.
#
# ⚠️ AND THESE LINES ARE NOT VALIDATED BY validate(), because validate() takes a
# LESSON. They are held to the same speech rules by the battery instead (PART 3di):
# the VOCABULARY canon, the beat word cap, and no notation. A line outside the
# validator's reach is exactly the kind of line that quietly acquires "subtract".
ABRABOT_INTRO = (
    "I would like you to meet somebody. This is Abrabot. He is my practice helper, "
    "and he is very good at his job.",

    "When you have finished a lesson with me, Abrabot has more problems for you. "
    "As many as you want, on the very same idea.",

    "He will tell you when you are right, and he will show you the answer when you "
    "are not. He keeps count, and nothing you do with him changes what you have "
    "already learned.",

    "And if a problem is tricky, Abrabot will come and get me. I will teach it again, "
    "and then I will hand you back to him. Have fun!",
)

# (mn) THE HANDOFF'S OWN TWO LINES -- what Mr. Cadabra says around the re-teach when
# Abrabot fetches him. mj left these out of the closure and Jim heard the seam on
# 2026-08-24: the fly-in opened in the BROWSER voice, then his real voice "came back"
# one beat later. They are as authored and as invariant as the introduction above, so
# they belong in the closure for the same reasons: rendered once by the prewarm,
# protected by the evictor, priced by the estimator, admitted by the drill gate.
# main.py's _CAD_HELLO/_CAD_BYE are ALIASES of these -- never a second copy.
CADABRA_HANDOFF_HELLO = "Let's look at this one together."
CADABRA_HANDOFF_BYE = "You have got this. Back to you, Abrabot."

# (rj, 2026-09-01) THE SEAM LINE. Jim watched a mastered lesson hand the class to the
# live tutor with no warning ("acted as if we had been working on subtraction. This is
# strange") and ruled: announce it, then continue. session.html speaks this AFTER the
# advance line on a MASTERED end, before the live tutor takes over; the live tutor is
# separately told (main.py's __script_done__ note) to NAME the new topic in its first
# sentence and put the name on the board. The page carries this string byte-for-byte
# (the voice cache is keyed by exact text) -- the battery pins the two copies equal.
LINE_NEW_TOPIC = ("That lesson is finished — well done! Something new is coming "
                  "next. Watch the board.")

# (sn, 2026-09-04) THE WARM CHOICE. Jim's ruling ③: a still-learning lesson end does
# not block and does not silently repeat -- the student PICKS. His words, verbatim.
# Standalone for the same reason as LINE_NEW_TOPIC: it belongs to the course, not to
# any lesson, and the page speaks it byte-for-byte so the pre-rendered clip is a
# cache hit, never browser voice (the battery pins the two copies equal).
LINE_STILL_LEARNING_CHOICE = ("You're doing great — would you like to go on to the "
                              "next lesson, or review this a bit more to get it solid?")

# Everything above, plus anything else that is spoken outside a lesson later.
STANDALONE_LINES = (tuple(ABRABOT_INTRO)
                    + (CADABRA_HANDOFF_HELLO, CADABRA_HANDOFF_BYE)
                    # (rj) the seam line belongs to the course, not to any lesson
                    + (LINE_NEW_TOPIC,)
                    # (sn) and so does the still-learning choice
                    + (LINE_STILL_LEARNING_CHOICE,)
                    # build ou: the free-answer lines belong to no lesson
                    + (LINE_WHOLE, LINE_UNSURE))


def course_audio_lines(lessons=None):
    """EVERY line the app can speak in Mr. Cadabra's voice, deduped and sorted.

    `lessons` narrows to a subset (the admin tools render one lesson at a time). The
    standalone lines belong to the COURSE, so they come along only when nobody has
    narrowed the request -- rendering "just lesson 12" should not quietly re-price
    Abrabot's introduction."""
    src = LESSONS if lessons is None else list(lessons)
    out = {s for les in src for s in audio_lines(les)}
    if lessons is None:
        out.update(STANDALONE_LINES)
    return sorted(out)


def audio_cost_estimate(lesson, usd_per_1k_chars=0.22):
    chars = sum(len(s) for s in audio_lines(lesson))
    return {"lines": len(audio_lines(lesson)), "chars": chars,
            "usd": round(chars / 1000.0 * usd_per_1k_chars, 2)}


# =============================================================================
# THE VALIDATOR -- the checks that make "verified once" true. Pure; returns a list
# of (ok, label, detail). The battery fails the build on any not-ok.
# =============================================================================
_TAG_RE = re.compile(r"\[\[\s*([\w-]+)")


def _difficulty_key(p):
    """The ramp is measured on what makes the problem HARD: the sum for adding,
    the starting number for taking away (you count back from it), the ones count
    for tens-and-ones."""
    op = p.get("op", "+")
    if op in OP_EXT:
        return OP_EXT[op]["key"](p)
    if op == "-":
        return p["a"]
    if op == "t":
        return p["b"]
    return p["a"] + p["b"]


# (mo) THE PUBLIC NAME FOR IT. drillpool.py has to sort a candidate bank by exactly
# the measure validate() ramps on, and it was computing its own -- one key function
# taken from the LESSON'S op and applied to every problem in the bank. That is right
# only while a lesson has a single op, and silently wrong the moment it does not:
# min5q problems were ranked with min5's key, the sort came out unramped, and
# validate() then rejected every candidate. Both mixed-op lessons in the course
# (basic-u9-quarter-turns and entry-u8-minutes-past-the-hour) had EMPTY drill pools
# because of it. One owner, publicly named, so no caller has to guess again.
difficulty_key = _difficulty_key


def validate(lesson, board_tag_names=None):
    checks = []

    def ck(ok, label, detail=""):
        checks.append((bool(ok), label, detail))

    lid = lesson["id"]
    bound = lesson.get("max_value", 10)

    # 1. every answer is COMPUTED -- and inside the lesson's own stated bound
    problems = list(lesson["bank"]) + [pr["ask"] for pr in lesson["pairs"]]
    # build km: the floor is DECLARED, not assumed. Every lesson through Basic Math
    # answers with a count, so "answers are 1 or more" was a true invariant and a
    # useful one -- it catches an op whose arithmetic has gone backwards. Prealgebra
    # Unit 3 teaches integers, where landing below zero IS the lesson, so a lesson may
    # now state its own floor. Default 1, so all 45 earlier lessons are unchanged and
    # still guarded; a lesson that wants negatives has to say so out loud.
    floor = lesson.get("min_value", 1)
    ck(all(floor <= ans(p) <= bound for p in problems),
       f"{lid}: every answer stays within {floor} to {bound}",
       str([p for p in problems if not floor <= ans(p) <= bound]))
    ck(all(p["a"] <= bound and p["b"] <= bound for p in problems),
       f"{lid}: every number a child sees stays within {bound}", "")
    # jx: the lesson's NAME is a promise about its INPUTS (Jim's second wording
    # ruling) -- a_max/b_max make the bank provably match the name.
    a_cap = lesson.get("a_max")
    b_cap = lesson.get("b_max")
    if a_cap is not None:
        ck(all(p["a"] <= a_cap for p in problems),
           f"{lid}: every first number honors the name (a <= {a_cap})",
           str([p for p in problems if p["a"] > a_cap]))
    if b_cap is not None:
        ck(all(p["b"] <= b_cap for p in problems),
           f"{lid}: every second number honors the name (b <= {b_cap})",
           str([p for p in problems if p["b"] > b_cap]))
    for p in problems:
        _ext = OP_EXT.get(p.get("op", "+"))
        if _ext:
            okc, why = _ext["check"](p)
            ck(okc, f"{lid}: {p} satisfies its op's constraint", why)
    if lesson.get("regroup"):
        ck(all(p["a"] % 10 < p["b"] % 10 and p["a"] > p["b"] and
               p["a"] // 10 - 1 >= p["b"] // 10 for p in problems),
           f"{lid}: EVERY problem regroups (ones too small) and never goes "
           f"negative in the tens",
           str([p for p in problems if not (p["a"] % 10 < p["b"] % 10
                and p["a"] > p["b"] and p["a"] // 10 - 1 >= p["b"] // 10)]))
    if lesson.get("carry"):
        ck(all(p["a"] % 10 + p["b"] % 10 > 9 for p in problems),
           f"{lid}: EVERY problem carries -- a carrying lesson that practices on "
           f"no-carry problems teaches its idea on examples that never use it",
           str([p for p in problems if p["a"] % 10 + p["b"] % 10 <= 9]))
        ck(all(p["a"] // 10 + p["b"] // 10 + 1 <= 9 for p in problems),
           f"{lid}: no problem overflows the tens (answers stay two-digit)",
           str([p for p in problems if p["a"] // 10 + p["b"] // 10 + 1 > 9]))
    if lesson.get("no_carry"):
        ck(all(p["a"] % 10 + p["b"] % 10 <= 9
               and p["a"] // 10 + p["b"] // 10 <= 9 for p in problems),
           f"{lid}: NO problem carries -- the lesson that promises no carrying "
           f"cannot quietly require it",
           str([p for p in problems
                if p["a"] % 10 + p["b"] % 10 > 9
                or p["a"] // 10 + p["b"] // 10 > 9]))
    ck(len({_problem_key(p) for p in problems}) == len(problems),
       f"{lid}: no duplicate problems", "")

    # 2. choices: the right answer appears exactly once, every option in range.
    # build km: the pattern was r"\d+", which cannot see a minus sign -- it read the
    # option "-6" as "6", so a Prealgebra U3 lesson looked like it was offering the
    # answer twice when it was offering -6 and +6, which is the whole point of the
    # question. The floor moved with it: "every option is at least 1" was the same
    # assumption as min_value, and it is now the lesson's declared floor (default 1,
    # so the other 45 lessons are guarded exactly as before).
    for p in problems:
        opts = re.findall(r"-?\d+", choices_for(p))
        ck(opts.count(str(ans(p))) == 1,
           f"{lid}: choices for {p['a']}{p.get('op', '+')}{p['b']} contain the "
           f"answer exactly once", str(opts))
        # THE FLOOR ONLY, deliberately. An upper bound here was tried in km and was
        # WRONG: the default distractor set is the answer's neighbours, so a lesson
        # whose top answer equals its max_value legitimately offers max_value + 1 --
        # Counting to 10 shows 9 | 10 | 11, times tables show 72 | 81 | 90 (sz: the
        # neighbouring facts; before sz it was 80 | 81 | 82). Six shipped
        # lessons said so at once, and they were right. max_value describes the
        # PROBLEMS; a neighbour one step past it is a normal wrong answer, not a defect.
        ck(all(int(o) >= floor for o in opts),
           f"{lid}: choices for {p['a']}{p.get('op', '+')}{p['b']} are all at "
           f"least {floor}", str(opts))

    # 3. the difficulty ramp: the key never falls by more than 1 across the bank.
    # kc: a lesson may declare mixed_review=True -- INTERLEAVED practice across ops
    # is the evidence-based design for review (the ramp is a teaching-lesson rule).
    if not lesson.get("mixed_review"):
        keys = [_difficulty_key(p) for p in lesson["bank"]]
        ck(all(keys[i + 1] >= keys[i] - 1 for i in range(len(keys) - 1)),
           f"{lid}: the bank is a ramp (difficulty never falls by more than 1)",
           str(keys))

    # (sp, 2026-09-05) THE SHAPE'S BEATS ARE HELD TO EVERY RULE THE OLD BEATS ARE.
    # A why, a picture or a recap line is spoken exactly like a teach line, so it
    # takes the word caps, the punctuation rule and the tag registry below.
    _shape_beats = [(s, b) for f in ("why", "picture", "recap")
                    for s, b in (lesson.get(f) or [])]
    _explain = lesson.get("explain") or {}

    # 4. every beat respects the spoken cap
    for spoken in [s for s, _b in lesson["teach"]] + \
                  [pr["worked"][0] for pr in lesson["pairs"]] + \
                  [lesson["practice_intro"]] + \
                  [s for s, _b in _shape_beats] + \
                  ([_explain["spoken"]] if _explain else []):
        ck(len(spoken.split()) <= BEAT_WORD_CAP,
           f"{lid}: beat under {BEAT_WORD_CAP} words: \"{spoken[:36]}...\"",
           f"{len(spoken.split())} words")

    # 5. rule 14 by construction: the lesson's symbols are READ ALOUD in teach
    # ⚠️ (pe, 2026-08-27) THIS CHECK USED TO DEMAND LITERAL SPACES -- f" {sym} " --
    # and that quietly shaped the prose for months. To satisfy it, a line that ended a
    # clause on the symbol had to be written "are called terms , and terms of x
    # collect", with a SPACE BEFORE THE COMMA, because "terms," has no trailing space.
    # 171 of those stray spaces were sitting in the authored lines; they read as
    # sloppy on screen and make the voice stumble. When pe closed them, 70 lessons
    # failed rule 14 at once -- which is how the dependency was found. The prose was
    # never the problem: a word followed by a comma is still the word. The check now
    # matches on WORD BOUNDARIES, so "terms," "terms." and "terms" all count, and an
    # author never has to bend a sentence around a test again.
    # (sp) a name may be introduced on the why or the picture beat -- they come first
    teach_text = " ".join(s for s, _b in lesson["teach"]).lower() + " " + \
        " ".join(s for s, _b in _shape_beats).lower()
    for sym in lesson["symbols"]:
        _sym_re = re.compile(r"(?<![a-z])" + re.escape(sym.lower()) + r"(?![a-z])")
        ck(bool(_sym_re.search(teach_text)),
           f"{lid}: the {sym} sign is introduced by name (rule 14)", "")

    # 5b. (pe, 2026-08-27) THE SENTENCES HAVE TO MAKE SENSE OUT LOUD. Jim, on a live
    # Algebra II lesson: "the text itself is as if someone is teaching math in a
    # non-native language ... when you put it in the whole context of those sentences,
    # it just didn't make sense." Most of what was wrong there is a judgement call and
    # NO TEST CAN CATCH IT -- a first pass at detectors flagged 390 lines for "stacked
    # dashes and colons" and nearly all of them were fine ("Eight plus three: eight —
    # nine, ten, eleven." is exactly right). The canon sweep threw that pattern out,
    # the same way build ox's "first...then...then" arm was cut for hitting 11 good
    # cards. What survived the sweep are the two defects that are MECHANICAL, that a
    # reader can verify without taste, and that had zero false positives across all
    # 1,989 authored cards:
    #   (a) a stray space before punctuation -- "terms , and". 171 of them; they read
    #       as sloppy in the bubble and make the voice stumble.
    #   (b) a spoken sentence over 34 words. 22 of them. This lane is heard, not read;
    #       a listener cannot re-scan a 44-word sentence, and every one of the 22 got
    #       clearer when it was split.
    # Everything else about the writing is reviewed by a person, on purpose.
    for _line in [s for s, _b in lesson["teach"]] + \
                 [pr["worked"][0] for pr in lesson["pairs"]] + \
                 [lesson.get("advance_line") or "", lesson.get("practice_intro") or ""] + \
                 [s for s, _b in _shape_beats] + \
                 [_explain.get("spoken", "")]:
        if not _line:
            continue
        ck(not re.search(r"\s+[,.;:?!]", _line),
           f"{lid}: no stray space before punctuation: \"{_line[:34]}...\"",
           "a word followed by a comma is still the word -- do not pad it to please a test")
        for _sent in re.split(r"(?<=[.?!])\s+", _line):
            ck(len(_sent.split()) <= SPOKEN_SENTENCE_CAP,
               f"{lid}: spoken sentence under {SPOKEN_SENTENCE_CAP} words: "
               f"\"{_sent[:34]}...\"",
               f"{len(_sent.split())} words -- a listener cannot re-scan a long sentence")

    # 6. rule 44 by construction: every ask SPEAKS its numbers
    for p in problems:
        for level in lesson.get("levels", LEVELS):
            sp = spoken_for(p, level)
            _speaks = OP_EXT.get(p.get("op", "+"), {}).get("speaks")
            ok44 = _speaks(p, sp) if _speaks else (str(p["a"]) in sp
                                                  and str(p["b"]) in sp)
            ck(ok44,
               f"{lid}: ask speaks its numbers "
               f"({p['a']}{p.get('op', '+')}{p['b']}, {level})", sp)

    # 7. build jr's lesson, enforced at authoring time: canon vocabulary only
    # (ts) the introduction quotes the curriculum's own names verbatim -- "Unit 3:
    # Subtraction within 20", "The remainder theorem" -- the names the student sees
    # on the course map. A name is said as written; the canon sweep reads every
    # other line the lesson speaks, exactly as before.
    _intro_line = lesson_intro(lesson)[0]
    all_speech = " ".join(x for x in audio_lines(lesson) if x != _intro_line).lower()
    for canon, banned in VOCABULARY.items():
        for term in banned:
            ck(term not in all_speech,
               f"{lid}: '{term}' never appears (canon is '{canon}')", "")

    # 8. every board tag is a real tag (against tags.py when provided)
    if board_tag_names:
        boards = [b for _s, b in lesson["teach"]] + \
                 [pr["worked"][1] for pr in lesson["pairs"]] + \
                 [board_for(p, lv) for p in problems
                  for lv in lesson.get("levels", LEVELS)] + \
                 [choices_for(p) for p in problems] + \
                 [b for _s, b in _shape_beats] + \
                 [_explain.get("board", "")] + \
                 [(_worked_for(p) or ("", ""))[1] for p in problems
                  if lesson.get("show_work_on_correct")]
        if lesson.get("mastery") == "table":
            # (sz) the pass's boards: the counter on the step, and every slip picture
            boards += [_table_board(table_facts()[0], 1, 1),
                       _table_board(table_facts()[-1], 2, TABLE_SIZE)]
            boards += [_table_miss(p)[1] for p in table_facts()]
        for b in boards:
            for name in _TAG_RE.findall(b):
                ck(name in board_tag_names,
                   f"{lid}: board tag [[{name}]] exists in the registry", b[:60])

    # 9. praise pool sanity
    ck(len(PRAISE_PREFIXES) >= 3, "at least 3 praise variants", "")

    # 10. (sp, 2026-09-05) THE SHAPE'S OWN PROMISES.
    # (a) show_work_on_correct is a promise the engine has to be able to keep: every
    #     problem's op needs a worked picture, or the walk-back silently never comes.
    if lesson.get("show_work_on_correct"):
        _no_work = [p for p in problems if _worked_for(p) is None]
        ck(not _no_work,
           f"{lid}: every problem's op has a worked picture (show_work_on_correct)",
           str(_no_work[:3]))
        for p in problems:
            w = _worked_for(p)
            if w:
                # (tc) a negative answer is SAID "negative 4" -- the digits alone would
                # be read as a hyphen by the voice -- so either form names it
                ck(str(ans(p)) in w[0] or (ans(p) < 0 and f"negative {-ans(p)}" in w[0]),
                   f"{lid}: the walk-back for {p['a']} names the answer", w[0])
    # (b) the reason question: 2-4 options, the answer among them exactly once, and
    #     no option that the page would read as a QUESTION (session.html routes a
    #     message ending in "?" or opening "what/why/how/can you" to the raised-hand
    #     door, not the answer door -- an option shaped like that could never be
    #     graded). A wrong reason is a real reason a student might give, so the
    #     options are held to the same word cap as a spoken sentence.
    if _explain:
        _opts = _reason_options(lesson)
        ck(2 <= len(_opts) <= 4,
           f"{lid}: the reason question offers two to four reasons", str(_opts))
        ck(sum(1 for o in _opts if _reason_norm(o) == _reason_norm(_explain.get("answer", ""))) == 1,
           f"{lid}: the authored reason is among the options exactly once",
           str(_opts))
        for o in _opts:
            ck(not re.search(r"\?\s*$", o)
               and not re.match(r"^(what|why|how|can you|i don'?t (get|understand))\b", o, re.I),
               f"{lid}: reason option is not shaped like a question: \"{o[:30]}\"",
               "the page would send it to the raised-hand door")
            ck(len(o.split()) <= 12,
               f"{lid}: reason option is short enough for a button: \"{o[:30]}\"",
               f"{len(o.split())} words")
        ck(bool(_explain.get("spoken")) and bool(_explain.get("answer")),
           f"{lid}: the reason question has a spoken line and an answer", "")
    # (c) a lesson that teaches the shape teaches it whole: why, picture and recap come
    #     together (a why without a recap is "taught once" again), and a reason question
    #     needs a picture to replay on a miss. The reason question itself is optional --
    #     a counting or comparing lesson has nothing to walk back (the design page).
    if lesson.get("why") or lesson.get("picture") or lesson.get("recap"):
        ck(bool(lesson.get("why")) and bool(lesson.get("picture"))
           and bool(lesson.get("recap")),
           f"{lid}: the shape is whole -- why, picture and recap together",
           str({f: bool(lesson.get(f)) for f in ("why", "picture", "recap")}))
    if _explain:
        ck(bool(lesson.get("picture")),
           f"{lid}: a reason question has a picture to replay on a miss", "")

    # 11. (sz, 2026-09-05) A TABLE LESSON'S PROMISES. "mastery": "table" hands the
    # practice to the 81-fact pass, so the pass is held to the same rules the bank is:
    # every fact inside the bound, every fact's options honest, every fact spoken with
    # its numbers, every slip picture naming the fact -- and the WORDS match the gate.
    # A table lesson that still said "three right answers in a row" would promise a
    # gate the engine no longer keeps (ri's lesson, the other way round).
    if lesson.get("mastery") is not None:
        ck(lesson.get("mastery") == "table",
           f"{lid}: mastery names a mode the engine has (table)",
           str(lesson.get("mastery")))
    if lesson.get("mastery") == "table":
        _facts = table_facts()
        ck(lesson.get("op") == "*" and all(p["op"] == "*" for p in problems),
           f"{lid}: a table lesson multiplies, bank and pairs alike", "")
        ck(tuple(lesson.get("levels", LEVELS)) == ("abstract",),
           f"{lid}: a table is recall, asked bare -- no level to drop to inside a pass",
           str(lesson.get("levels")))
        ck(all(floor <= ans(p) <= bound for p in _facts),
           f"{lid}: every fact of the table stays within {floor} to {bound}",
           str([p for p in _facts if not floor <= ans(p) <= bound][:3]))
        _bad_opts = []
        for p in _facts:
            _o = re.findall(r"-?\d+", choices_for(p))
            if _o.count(str(ans(p))) != 1 or not all(int(x) >= floor for x in _o):
                _bad_opts.append((p["a"], p["b"], _o))
        ck(not _bad_opts,
           f"{lid}: every fact's options hold the answer once, all at least {floor}",
           str(_bad_opts[:3]))
        _unspoken = [p for p in _facts for lv in lesson.get("levels", LEVELS)
                     if not (str(p["a"]) in spoken_for(p, lv) and str(p["b"]) in spoken_for(p, lv))]
        ck(not _unspoken, f"{lid}: every fact's ask speaks its numbers (rule 44)",
           str(_unspoken[:3]))
        _unnamed = [p for p in _facts if str(ans(p)) not in _table_miss(p)[0]
                    or f'rows="{p["a"]}" cols="{p["b"]}"' not in _table_miss(p)[1]]
        ck(not _unnamed,
           f"{lid}: every slip picture draws the fact's array and names its answer",
           str(_unnamed[:3]))
        _words = (lesson.get("practice_intro", "") + " " + lesson.get("advance_line", "")).lower()
        ck(not re.search(r"\bthree\b|\bin a row\b", _words),
           f"{lid}: the words never promise three in a row -- the gate is the clean pass",
           _words[:80])
        ck(str(TABLE_SIZE) in lesson.get("practice_intro", ""),
           f"{lid}: the practice intro tells the student the pass is {TABLE_SIZE} facts", "")
        ck(len(LINE_TABLE_RESTART.split()) <= BEAT_WORD_CAP
           and len(LINE_TABLE_REST.split()) <= BEAT_WORD_CAP
           and str(TABLE_MAX_MISSES) in LINE_TABLE_REST,
           f"{lid}: the pass's standing lines fit a beat and the rest line names "
           f"{TABLE_MAX_MISSES}", "")
    return checks


# I did no harm and this file is not truncated.
