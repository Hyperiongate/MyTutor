# =============================================================================
# lessons/basic.py  --  BASIC MATH: THE AUTHORED LESSONS  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-09-11  BUILD vj -- FOUR OF JIM'S SIX FLAGS FROM A LIVE BASIC LESSON.
#               (1) basic-u1-place-value-to-1000: the TOPIC "Place value to 1,000" ->
#               "Place value: hundreds, tens and ones". The lesson never shows a
#               thousand (every number is three digits; the bank tops out at 929), so
#               the next lesson's "Before this came Place value to 1,000, and you
#               finished it" was the record telling the truth about the wrong name --
#               Jim: "we never did place value to 1,000". The id and the order are
#               untouched. Its [[goal]] card carries the new name.
#               (2) the same lesson's why beat and second recap beat no longer speak
#               of "three hundred and forty-two tally marks" -- Jim: "a child does not
#               know what a tally mark is" / "sort of a nonsense statement". The why
#               now ends "and three digits say it all"; the recap says "places save
#               the counting: three digits tell you three hundred and forty-two
#               without counting one by one".
#               (3) basic-u1-rounding-tens why beat: "more than you need" -> "more
#               ACCURATE than you need" (Jim's own wording).
#               Four spoken lines change, so four clips re-render on the next prewarm;
#               speechmap.py regenerated the same build.
#   2026-09-08  BUILD uj -- ONE FILE PER COURSE. Split out of lessonscripts.py (Jim's
#               housekeeping, second half). Every lesson below is the text that sat in
#               lessonscripts.py, moved whole -- the unit lists keep their names, and
#               the build notes above each unit came with them. ORDER at the bottom is
#               this course's slice of COURSE_ORDER (the teaching order). PURE DATA: no
#               imports, no functions -- the engine (lessonscripts.py) reads
#               lessons.LESSONS and lessons.COURSE_ORDER through lessons/__init__.py.
#               ADDING A LESSON: put it in its unit's list AND in ORDER; the battery's
#               validator, the closure prewarm and the demo pick it up from there.
# =============================================================================
LESSONS = []

_BASIC_MORE = [
    {
        # (sr, 2026-09-05) TO THE SHAPE on the PLACE-VALUE CHART: the digits are
        # SEEN moving up a column (the chart grew a Thousands column for it).
        "id": "basic-u2-times-by-ten", "course": "basic", "unit": 2,
        "topic": "Times by ten and a hundred", "op": "mtz", "max_value": 9900,
        "levels": ("abstract",), "symbols": ("times", "place"),
        "advance_line": "Three in a row, and you can say why — you've got it! Times by ten moves every digit up one place.",
        "why": [
            ("Why is times ten special? Because our whole number system is built "
             "on ten — ten ones are a ten, ten tens are a hundred. So timesing by "
             # (ta) "once you see the move" read as pointing at a chart the goal
             # line does not draw; the chart comes on the next beat. "know" is truer.
             "ten is not a fact to memorize. It is a move on the place-value "
             "chart, and once you know the move you can do it for any number.",
             '[[goal text="Times by ten and a hundred"]]'),
        ],
        "picture": [
            ("Here is 46 on the chart: 4 tens, 6 ones. Now times it by ten. Every "
             "digit slides up one column — the 4 tens become 4 hundreds, the 6 "
             "ones become 6 tens — and the ones column is empty, so a zero holds "
             "it open. 460.",
             '[[placevalue n="460" caption="46 × 10 = 460: every digit up one place"]]'),
        ],
        "teach": [
            ("That is the move: times ten, every digit up one place, a zero in the "
             "ones. Times a hundred is the same move twice — every digit up two "
             "places, and two zeros hold the tens and the ones. 46 times 100 is "
             "4,600.",
             '[[placevalue n="4600" caption="46 × 100 = 4600: every digit up two places"]]'),
            ("Here is the trap. Count your zeros against the number you timesed "
             "by. Ten has one zero, so one zero is added. A hundred has two zeros, "
             "so two are added. An extra zero leaves the answer ten times too big.",
             '[[step eq="46 × 100 = 4600 ✓ two zeros"]]'
             '[[step eq="46000 ✗ three zeros — that is times a thousand"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 38 times 10. The 3 tens "
                        "become 3 hundreds, the 8 ones become 8 tens, and a zero "
                        "fills the ones. 380.",
                        '[[placevalue n="380" caption="38 × 10 = 380: every digit up one place"]]'),
             "ask": {"a": 27, "b": 10, "op": "mtz"}},
            {"worked": ("One more together. 53 times 100. Two places this time: 5 "
                        "tens become 5 thousands, 3 ones become 3 hundreds, and two "
                        "zeros hold the tens and the ones. 5,300.",
                        '[[placevalue n="5300" caption="53 × 100 = 5300: every digit up two places"]]'),
             "ask": {"a": 64, "b": 100, "op": "mtz"}},
        ],
        "practice_intro": "Now it's your turn. Watch the digits move on the chart. Three right answers in a row and we're done — here comes the first one.",
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 46 times 10 is "
                       "460, and it ends in a zero. Tap the reason why."),
            "choices": ("because every digit moved up a place and left the ones "
                        "empty | because ten ends in a zero, so you copy it | "
                        "because 460 is a round number"),
            "answer": "because every digit moved up a place and left the ones empty",
            "board": '[[placevalue n="460" caption="the ones column is empty — a zero holds it"]]',
        },
        "recap": [
            ("So, here it is again. Times ten: every digit up one place, a zero in "
             "the ones. Times a hundred: up two places, two zeros. Count your "
             "zeros against the number you timesed by.",
             '[[placevalue n="4600" caption="46 × 100 = 4600"]]'),
            ("And it works for every number, because the whole system is built on "
             "ten.",
             '[[step eq="46 × 10 = 460 · 46 × 100 = 4600"]]'),
        ],
        "bank": [{"a": 2, "b": 10, "op": "mtz"}, {"a": 23, "b": 10, "op": "mtz"}, {"a": 42, "b": 10, "op": "mtz"}, {"a": 62, "b": 10, "op": "mtz"}, {"a": 82, "b": 10, "op": "mtz"}, {"a": 12, "b": 100, "op": "mtz"}, {"a": 34, "b": 100, "op": "mtz"}, {"a": 56, "b": 100, "op": "mtz"}, {"a": 77, "b": 100, "op": "mtz"}, {"a": 99, "b": 100, "op": "mtz"}],
    },
    {
        # (st, 2026-09-05) TO THE SHAPE: a factor pair is a RECTANGLE -- the number
        # laid out as rows, its two sides the pair. Small ones are groups of dots; big
        # ones are the area model's one cell with its sides labelled.
        "id": "basic-u4-factor-pairs", "course": "basic", "unit": 4,
        "topic": "Factor pairs", "op": "fpr", "max_value": 100,
        "levels": ("abstract",), "symbols": ("factor", "pair"),
        "advance_line": "Three in a row, and you can say why — you've got it! Factors come in pairs.",
        "why": [
            ("Factors never arrive alone. Every time you find one factor of a "
             "number, you have found a second one for free, because the two of "
             "them times each other make the number. That is why it is worth "
             "seeing what a pair looks like — you will use pairs to simplify "
             "fractions and to share things out for years.",
             '[[goal text="Factor pairs"]]'),
        ],
        "picture": [
            ("Here is 18 laid out in 2 rows: 9 in each. A rectangle, 2 by 9, "
             "holding 18. The two sides of the rectangle are a factor pair — 2 and "
             "9 — and every factor pair of 18 is a rectangle like this one.",
             '[[array rows="2" cols="9" view="groups" eq="2 × 9 = 18" caption="a 2 by 9 rectangle holds 18"]]'),
        ],
        "teach": [
            ("So: 18 is 2 times what? Share 18 into 2 rows — 9 in each. 2 and 9 "
             "are a factor pair of 18, and finding one handed me the other.",
             '[[array rows="2" cols="9" view="groups" eq="18 ÷ 2 = 9" caption="2 and 9 are a pair"]]'),
            ("Here is the trap. The partner is what you DIVIDE by to get there, "
             "not what you take away. For 18 and 2 the partner is 9, not 16. "
             "Check yourself every time: your answer times the factor should come "
             "straight back to the number you started with.",
             '[[step eq="2 × 9 = 18 ✓"]]'
             '[[step eq="16 ✗ that is 18 − 2, and 2 × 16 is nowhere near 18"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 30 is 5 times what? 30 laid "
                        "out in 5 rows is 6 in each. So 5 and 6 are a pair — and 5 "
                        "times 6 comes straight back to 30.",
                        '[[array rows="5" cols="6" view="groups" eq="5 × 6 = 30" caption="5 and 6 are a factor pair of 30"]]'),
             "ask": {"a": 40, "b": 8, "op": "fpr"}},
            {"worked": ("One more together. 63 is 7 times what? 63 in 7 rows is 9 in "
                        "each, so 7 and 9 are a pair. Check: 7 times 9 equals 63.",
                        '[[array rows="7" cols="9" view="groups" eq="7 × 9 = 63" caption="7 and 9 are a factor pair of 63"]]'),
             "ask": {"a": 54, "b": 6, "op": "fpr"}},
        ],
        "practice_intro": "Now it's your turn. Divide to find the partner, then check with times. Three right answers in a row and we're done — here comes the first one.",
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. For 18 and 2, "
                       "the partner is 9 and not 16. Tap the reason why."),
            "choices": ("because 2 times 9 comes straight back to 18 | because 16 "
                        "is too big to be a factor | because 9 is half of 18"),
            "answer": "because 2 times 9 comes straight back to 18",
            "board": '[[array rows="2" cols="9" view="groups" eq="2 × 9 = 18" caption="2 and 9 are a pair"]]',
        },
        "recap": [
            ("So, here it is again. A factor pair is two numbers that times each "
             "other make the number — the two sides of a rectangle that holds it. "
             "Divide to find the partner, and check with times.",
             '[[array rows="2" cols="9" view="groups" eq="2 × 9 = 18" caption="the sides of the rectangle are the pair"]]'),
            ("And pairs are what you will reach for to simplify fractions and share "
             "things out.",
             '[[step eq="18 = 2 × 9 = 3 × 6 = 1 × 18"]]'),
        ],
        "bank": [{"a": 12, "b": 2, "op": "fpr"}, {"a": 27, "b": 3, "op": "fpr"}, {"a": 38, "b": 19, "op": "fpr"}, {"a": 48, "b": 12, "op": "fpr"}, {"a": 58, "b": 29, "op": "fpr"}, {"a": 68, "b": 2, "op": "fpr"}, {"a": 76, "b": 19, "op": "fpr"}, {"a": 84, "b": 28, "op": "fpr"}, {"a": 92, "b": 46, "op": "fpr"}, {"a": 100, "b": 50, "op": "fpr"}],
    },
    {
        # (su, 2026-09-05) TO THE SHAPE on TWO PIES: the fraction as given and its
        # shortest name, the same amount. The trap line kept.
        "id": "basic-u5-simplest-form", "course": "basic", "unit": 5,
        "topic": "Simplest form", "op": "simp", "max_value": 24,
        "levels": ("abstract",), "symbols": ("simplest", "share"),
        "advance_line": "Three in a row, and you can say why — you've got it! You can put a fraction in its simplest form.",
        "why": [
            ("Different fractions can name the same amount — 4 out of 8, 2 out of "
             "4, 1 out of 2. Of all the names for one amount, one is the shortest. "
             "That one is its simplest form, and it is the one we write, because "
             "it is the easiest to read, compare and say.",
             '[[goal text="Simplest form"]]'),
        ],
        "picture": [
            ("Here is 9 out of 12, and next to it the same pie cut into just 4 "
             "pieces — 3 out of 4 shaded. Look: the shaded amount is the same. 3 "
             "out of 4 is the shortest name for it.",
             '[[pie parts="12" shaded="9" caption="9 out of 12"]][[pie parts="4" shaded="3" caption="3 out of 4 — the same amount"]]'),
        ],
        "teach": [
            ("Here is how to find the shortest name. 9 and 12 both share 3, so "
             "divide both by 3: 9 becomes 3 and 12 becomes 4. Nothing divides 3 "
             "and 4 together, so 3 out of 4 is as short as it goes.",
             '[[pie parts="12" shaded="9" caption="9/12"]][[pie parts="4" shaded="3" caption="÷ 3 top and bottom → 3/4"]]'),
            ("Here is the trap. Whatever you do to the top, do to the bottom. "
             "Halving only the top turns the fraction into a different amount "
             "entirely. Simplest form renames the fraction. It never changes how "
             "much it is worth.",
             '[[step eq="9/12 = 3/4 ✓ both divided by 3"]]'
             '[[step eq="only the top divided ✗ that is a different fraction"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 8 out of 12. Both share 4, "
                        "so divide both by 4. That is 2 out of 3 — the same amount.",
                        '[[pie parts="12" shaded="8" caption="8/12"]][[pie parts="3" shaded="2" caption="2/3 — the same amount"]]'),
             "ask": {"a": 3, "b": 9, "op": "simp"}},
            {"worked": ("One more together. 10 out of 16. Both share 2, so divide "
                        "both by 2. That is 5 out of 8.",
                        '[[step eq="10/16 ÷ 2 → 5/8"]][[pie parts="8" shaded="5" caption="5/8 — the same amount, simplest form"]]'),
             "ask": {"a": 14, "b": 21, "op": "simp"}},
        ],
        "practice_intro": "Now it's your turn. Find what the top and bottom share, and divide both. Three right answers in a row and we're done — here comes the first one.",
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 9 out of 12 and "
                       "3 out of 4 are the same amount. Tap the reason why."),
            "choices": ("because both top and bottom were divided by the same 3 | "
                        "because 9 take away 6 is 3 | because 3 out of 4 sounds "
                        "smaller"),
            "answer": "because both top and bottom were divided by the same 3",
            "board": '[[pie parts="12" shaded="9" caption="9/12"]][[pie parts="4" shaded="3" caption="3/4"]]',
        },
        "recap": [
            ("So, here it is again. Find what the top and the bottom share, divide "
             "both by it, and you have the shortest name for the same amount. Do "
             "it to both, never to one.",
             '[[pie parts="12" shaded="9" caption="9/12"]][[pie parts="4" shaded="3" caption="3/4 — the same amount"]]'),
            ("And the shortest name is the one we write, because it is the easiest "
             "to read and compare.",
             '[[step eq="9/12 = 3/4"]]'),
        ],
        "bank": [{"a": 2, "b": 4, "op": "simp"}, {"a": 5, "b": 10, "op": "simp"}, {"a": 2, "b": 14, "op": "simp"}, {"a": 10, "b": 15, "op": "simp"}, {"a": 4, "b": 18, "op": "simp"}, {"a": 4, "b": 20, "op": "simp"}, {"a": 6, "b": 21, "op": "simp"}, {"a": 10, "b": 22, "op": "simp"}, {"a": 6, "b": 24, "op": "simp"}, {"a": 22, "b": 24, "op": "simp"}],
    },
    {
        # (sv, 2026-09-05) TO THE SHAPE on the FRACTION LINE cut the finer way, hopping
        # back. The trap line kept.
        "id": "basic-u6-take-away-unlike-bottoms", "course": "basic", "unit": 6,
        "topic": "Taking away fractions with different bottoms", "op": "fus",
        "max_value": 12,
        "levels": ("abstract",), "symbols": ("bottom", "take away"),
        "advance_line": "Three in a row, and you can say why — you've got it! Match the bottoms, then take away.",
        "why": [
            ("Adding fractions with different bottoms meant renaming one of them "
             "first. Taking away works the very same way. You cannot take eighths "
             "from a half until the half is written in eighths — and once it is, "
             "it is just counting back.",
             '[[goal text="Different bottoms, take away"]]'),
        ],
        "picture": [
            ("Here is a line cut into eighths. One half sits at four eighths — "
             "same spot, new name. Now hop back one eighth. Three eighths.",
             '[[numberline min="0" max="1" denom="8" hops="0.5,0.375" points="0.375" caption="1/2 = 4/8, then − 1/8 = 3/8"]]'),
        ],
        "teach": [
            ("Watch me. One half take away one eighth. A half is 4 eighths, because "
             "8 divided by 2 is 4. Now both are eighths: 4 eighths take away 1 "
             "eighth leaves 3 eighths.",
             '[[step eq="1/2 = 4/8"]][[numberline min="0" max="1" denom="8" hops="0.5,0.375" points="0.375" caption="4/8 − 1/8 = 3/8"]]'),
            ("Here is the trap. Once both bottoms MATCH, the bottom stops "
             "changing: eighths take away eighths leaves eighths, and only the top "
             "numbers do the taking away. That holds only after they match, which "
             "is why renaming comes first.",
             '[[step eq="4/8 − 1/8 = 3/8 ✓"]]'
             '[[step eq="3/7 ✗ the bottoms were taken away from as well"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. One half take away 2 sixths. "
                        "On a line of sixths, a half sits at 3 sixths. Hop back 2: 1 "
                        "sixth.",
                        '[[numberline min="0" max="1" denom="6" hops="0.5,0.1667" points="0.1667" caption="1/2 = 3/6, then − 2/6 = 1/6"]]'),
             "ask": {"a": 1, "b": 2, "c": 6, "op": "fus"}},
            {"worked": ("One more together. One fourth take away 1 eighth. On a line "
                        "of eighths, a fourth sits at 2 eighths. Hop back 1: 1 eighth.",
                        '[[numberline min="0" max="1" denom="8" hops="0.25,0.125" points="0.125" caption="1/4 = 2/8, then − 1/8 = 1/8"]]'),
             "ask": {"a": 3, "b": 2, "c": 8, "op": "fus"}},
        ],
        "practice_intro": "Now it's your turn. Find the first fraction on the finer line, then hop back. Three right answers in a row and we're done — here comes the first one.",
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Four eighths "
                       "take away one eighth is three eighths, not three sevenths. "
                       "Tap the reason why."),
            "choices": ("because once the bottoms match, only the tops are taken away "
                        "| because 8 take away 1 is 7 | because sevenths do not exist"),
            "answer": "because once the bottoms match, only the tops are taken away",
            "board": '[[numberline min="0" max="1" denom="8" hops="0.5,0.375" points="0.375" caption="the bottom stays 8"]]',
        },
        "recap": [
            ("So, here it is again. Rename one fraction until the bottoms match, "
             "then take away the tops and keep the bottom. On the line: find the "
             "first fraction on the finer line, then hop back.",
             '[[numberline min="0" max="1" denom="8" hops="0.5,0.375" points="0.375" caption="1/2 − 1/8 = 3/8"]]'),
            ("And it is the same move adding used — match first, then count.",
             '[[step eq="1/2 − 1/8 = 4/8 − 1/8 = 3/8"]]'),
        ],
        "bank": [{"a": 1, "b": 2, "c": 4, "op": "fus"}, {"a": 1, "b": 3, "c": 6, "op": "fus"}, {"a": 2, "b": 2, "c": 8, "op": "fus"}, {"a": 1, "b": 2, "c": 10, "op": "fus"}, {"a": 3, "b": 2, "c": 10, "op": "fus"}, {"a": 1, "b": 2, "c": 12, "op": "fus"}, {"a": 3, "b": 2, "c": 12, "op": "fus"}, {"a": 1, "b": 3, "c": 12, "op": "fus"}, {"a": 3, "b": 3, "c": 12, "op": "fus"}, {"a": 1, "b": 6, "c": 12, "op": "fus"}],
    },
    {
        # (sw, 2026-09-05) TO THE SHAPE on the HUNDREDTHS SQUARE: a tenth is a full row.
        # The trap line kept.
        "id": "basic-u7-tenths-and-hundredths", "course": "basic", "unit": 7,
        "topic": "Tenths and hundredths together", "op": "t2h", "max_value": 99,
        "levels": ("abstract",), "symbols": ("tenths", "hundredths"),
        "advance_line": "Three in a row, and you can say why — you've got it! A tenth is ten hundredths.",
        "why": [
            ("You have met tenths, and you have met hundredths. Today they meet "
             "each other — because real numbers mix them: 0.43 is 4 tenths and 3 "
             "hundredths. The rule that joins them is small and it is the whole "
             "lesson: one tenth is ten hundredths.",
             '[[goal text="Tenths and hundredths"]]'),
        ],
        "picture": [
            ("Here is the hundredths square. One full row is ten cells — ten "
             "hundredths — and that is exactly one tenth. So 4 tenths is 4 full "
             "rows, 40 cells. Add 3 more cells in red: 43 hundredths.",
             '[[hundredgrid shaded="40" plus="3" caption="4 tenths = 4 rows = 40, + 3 = 43 hundredths"]]'),
        ],
        "teach": [
            ("Watch me. 4 tenths plus 3 hundredths. You cannot add them as they "
             "stand, so change the tenths first: 4 tenths is 40 hundredths. Now "
             "both are hundredths. 40 plus 3 is 43 hundredths.",
             '[[step eq="4 tenths = 40 hundredths"]][[hundredgrid shaded="40" plus="3" caption="40 + 3 = 43 hundredths"]]'),
            ("Here is the trap, and it is the same one place value always sets. Do "
             "not add the digits as though they were the same size. 4 tenths plus "
             "3 hundredths is not 7 of anything. A tenth is ten times the bigger "
             "coin.",
             '[[step eq="4 tenths + 3 hundredths = 43 hundredths ✓"]]'
             '[[step eq="7 ✗ the two digits added as if they matched"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 2 tenths plus 5 hundredths. "
                        "2 tenths is 2 full rows — 20 hundredths — and 20 plus 5 is "
                        "25 hundredths.",
                        '[[hundredgrid shaded="20" plus="5" caption="2 tenths = 20, + 5 = 25 hundredths"]]'),
             "ask": {"a": 3, "b": 4, "op": "t2h"}},
            {"worked": ("One more together. 7 tenths plus 6 hundredths. 7 full rows is "
                        "70 hundredths, plus 6 is 76 hundredths.",
                        '[[hundredgrid shaded="70" plus="6" caption="7 tenths = 70, + 6 = 76 hundredths"]]'),
             "ask": {"a": 8, "b": 2, "op": "t2h"}},
        ],
        "practice_intro": "Now it's your turn. Tenths are full rows; count the rows, then the cells. Three right answers in a row and we're done — here comes the first one.",
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 4 tenths plus 3 "
                       "hundredths is 43 hundredths, not 7. Tap the reason why."),
            "choices": ("because a tenth is a whole row of ten cells, not one | "
                        "because 43 is the bigger answer | because you always put "
                        "the digits side by side"),
            "answer": "because a tenth is a whole row of ten cells, not one",
            "board": '[[hundredgrid shaded="40" plus="3" caption="a tenth is a whole row"]]',
        },
        "recap": [
            ("So, here it is again. One tenth is ten hundredths — a whole row of "
             "the square. To add tenths and hundredths, turn the tenths into "
             "hundredths first, then count.",
             '[[hundredgrid shaded="40" plus="3" caption="4 tenths + 3 hundredths = 43 hundredths"]]'),
            ("And that is how a number like 0.43 is built — tenths and hundredths, "
             "each in its own place.",
             '[[step eq="4 tenths + 3 hundredths = 43 hundredths"]]'),
        ],
        "bank": [{"a": 1, "b": 1, "op": "t2h"}, {"a": 2, "b": 1, "op": "t2h"}, {"a": 3, "b": 1, "op": "t2h"}, {"a": 4, "b": 1, "op": "t2h"}, {"a": 5, "b": 1, "op": "t2h"}, {"a": 5, "b": 9, "op": "t2h"}, {"a": 6, "b": 9, "op": "t2h"}, {"a": 7, "b": 9, "op": "t2h"}, {"a": 8, "b": 9, "op": "t2h"}, {"a": 9, "b": 9, "op": "t2h"}],
    },
    {
        # (sx, 2026-09-05) TO THE SHAPE on the HUNDREDTHS SQUARE in percent mode: the
        # part as a pie, then the same part out of a hundred. The trap line kept.
        "id": "basic-u8-what-percent-is-it", "course": "basic", "unit": 8,
        "topic": "What percent is it", "op": "wpc", "max_value": 100,
        "levels": ("abstract",), "symbols": ("percent", "out of"),
        "advance_line": "Three in a row, and you can say why — you've got it! You can say any part as a percent.",
        "why": [
            ("Percent means out of a hundred, and the world talks in it: 75 percent "
             "on a test, 20 percent off, a phone at 40 percent. It is one way to "
             "say any part so that every part can be compared. Turning a part into "
             "a percent is one job only: rewrite it as something out of a hundred.",
             '[[goal text="What percent is it"]]'),
        ],
        "picture": [
            ("Here is 3 out of 4 as a pie — three of four pieces. And here is the "
             "same amount on the hundred square: 75 of the 100 cells. 3 out of 4 "
             "is 75 out of 100 — 75 percent.",
             '[[pie parts="4" shaded="3" caption="3 out of 4"]][[hundredgrid shaded="75" unit="percent" caption="the same amount: 75 out of 100"]]'),
        ],
        "teach": [
            ("Here is the quick way. Ask what turns the bottom into 100: 4 times 25. "
             "Do the same to the top: 3 times 25 is 75. So 3 out of 4 is 75 "
             "percent.",
             '[[step eq="4 × 25 = 100"]][[step eq="3 × 25 = 75, so 75 percent"]]'
             '[[hundredgrid shaded="75" unit="percent" caption="75 out of 100"]]'),
            ("Here is the trap. Do not read the top number as the percent. 3 out "
             "of 4 is not 3 percent — 3 percent would be almost nothing, and 3 out "
             "of 4 is most of it. Change the bottom to a hundred first, every "
             "time.",
             '[[step eq="3 out of 4 = 75 percent ✓"]]'
             '[[step eq="3 percent ✗ the top copied without changing the bottom"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 2 out of 5. Five times 20 "
                        "is a hundred, so 2 times 20 is 40. That is 40 percent — 40 "
                        "of the hundred cells.",
                        '[[hundredgrid shaded="40" unit="percent" caption="2 out of 5 = 40 out of 100 = 40%"]]'),
             "ask": {"a": 7, "b": 10, "op": "wpc"}},
            {"worked": ("One more together. 13 out of 20. Twenty times 5 is a "
                        "hundred, so 13 times 5 is 65. 65 percent.",
                        '[[hundredgrid shaded="65" unit="percent" caption="13 out of 20 = 65 out of 100 = 65%"]]'),
             "ask": {"a": 9, "b": 25, "op": "wpc"}},
        ],
        "practice_intro": "Now it's your turn. Turn the bottom into a hundred, and do the same to the top. Three right answers in a row and we're done — here comes the first one.",
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 3 out of 4 is 75 "
                       "percent, not 3 percent. Tap the reason why."),
            "choices": ("because out of a hundred, 3 out of 4 is 75 | because 75 "
                        "is a bigger number | because 3 percent is a small number"),
            "answer": "because out of a hundred, 3 out of 4 is 75",
            "board": '[[hundredgrid shaded="75" unit="percent" caption="3 out of 4 = 75 out of 100"]]',
        },
        "recap": [
            ("So, here it is again. Percent means out of a hundred. To say a part "
             "as a percent, turn the bottom into 100 and do the same to the top — "
             "that top is your percent.",
             '[[hundredgrid shaded="75" unit="percent" caption="3 out of 4 = 75%"]]'),
            ("And percent is how the world compares parts — scores, sales, "
             "batteries.",
             '[[step eq="3 out of 4 = 75 percent"]]'),
        ],
        "bank": [{"a": 1, "b": 100, "op": "wpc"}, {"a": 12, "b": 100, "op": "wpc"}, {"a": 6, "b": 25, "op": "wpc"}, {"a": 34, "b": 100, "op": "wpc"}, {"a": 9, "b": 20, "op": "wpc"}, {"a": 55, "b": 100, "op": "wpc"}, {"a": 33, "b": 50, "op": "wpc"}, {"a": 76, "b": 100, "op": "wpc"}, {"a": 22, "b": 25, "op": "wpc"}, {"a": 99, "b": 100, "op": "wpc"}],
    },
    {
        # (sx, 2026-09-05) TO THE SHAPE on the TAPE: the price as a bar, the discount
        # and what you pay as its two parts. The trap line kept.
        "id": "basic-u8-percent-off", "course": "basic", "unit": 8,
        "topic": "Percent off a price", "op": "poff", "max_value": 200,
        "levels": ("abstract",), "symbols": ("percent off", "pay"),
        "advance_line": "Three in a row, and you can say why — you've got it! Work out the discount, then take it away.",
        "why": [
            ("A sign in a shop window says 25 percent off. That is a percent of "
             "the price, and it is the part you do NOT pay. Knowing what you "
             "actually pay — not what you save — is the difference between a "
             "bargain and a surprise at the till.",
             '[[goal text="Percent off a price"]]'),
        ],
        "picture": [
            ("Here is the price as a bar: 60 dollars. 25 percent off cuts it into "
             "two parts — the discount, 15, and what you pay, 45. The discount is "
             "the small piece that comes off; you pay the rest.",
             '[[tape parts="15 | 45" total="60" caption="60 dollars: discount 15, you pay 45"]]'),
        ],
        "teach": [
            ("So it is two steps: find the discount, then take it away from the "
             "price. A coat costs 60 dollars with 25 percent off. 25 percent of 60 "
             "is 15. 60 take away 15 is 45. You pay 45 dollars.",
             '[[step eq="25% of 60 = 15"]][[step eq="60 − 15 = 45"]][[tape parts="15 | 45" total="60" caption="discount 15 — you pay 45"]]'),
            ("Here is the trap, and shops rely on it. The discount is not the "
             "answer. 15 is what you SAVE. The question asks what you pay, so the "
             "second step is the one that matters, and your answer is always "
             "smaller than the price but bigger than the discount.",
             '[[step eq="you pay 45 ✓"]]'
             '[[step eq="15 ✗ that is the saving, not the price"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 40 dollars with 10 percent "
                        "off. The discount is 10 percent of 40 — 4 dollars. 40 take "
                        "away 4 is 36. You pay 36.",
                        '[[tape parts="4 | 36" total="40" caption="discount 4 — you pay 36"]]'),
             "ask": {"a": 80, "b": 25, "op": "poff"}},
            {"worked": ("One more together. 50 dollars with 20 percent off. The "
                        "discount is 20 percent of 50 — 10. 50 take away 10 is 40. "
                        "You pay 40.",
                        '[[tape parts="10 | 40" total="50" caption="discount 10 — you pay 40"]]'),
             "ask": {"a": 140, "b": 25, "op": "poff"}},
        ],
        "practice_intro": "Now it's your turn. Discount first, then take it off the price. Three right answers in a row and we're done — here comes the first one.",
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 60 dollars with "
                       "25 percent off: you pay 45, not 15. Tap the reason why."),
            "choices": ("because 15 comes off, and you pay the rest | because 45 is "
                        "the bigger number | because shops never give 15 dollars off"),
            "answer": "because 15 comes off, and you pay the rest",
            "board": '[[tape parts="15 | 45" total="60" caption="15 comes off — 45 is what you pay"]]',
        },
        "recap": [
            ("So, here it is again. Percent off is two steps: find the discount — a "
             "percent of the price — then take it away. The bar shows both parts; "
             "you pay the big one.",
             '[[tape parts="15 | 45" total="60" caption="price 60 = discount 15 + you pay 45"]]'),
            ("And knowing what you pay, not what you save, is what keeps the till "
             "from surprising you.",
             '[[step eq="60 − 15 = 45"]]'),
        ],
        "bank": [{"a": 10, "b": 20, "op": "poff"}, {"a": 30, "b": 20, "op": "poff"}, {"a": 55, "b": 20, "op": "poff"}, {"a": 70, "b": 10, "op": "poff"}, {"a": 104, "b": 25, "op": "poff"}, {"a": 120, "b": 20, "op": "poff"}, {"a": 148, "b": 25, "op": "poff"}, {"a": 168, "b": 25, "op": "poff"}, {"a": 180, "b": 20, "op": "poff"}, {"a": 200, "b": 10, "op": "poff"}],
    },
    {
        # (sr, 2026-09-05) TO THE SHAPE on the ARRAY ([[array view="groups"]]): equal
        # groups drawn as rows of dots, the times sign as the short way to write them.
        "id": 'basic-u2-what-multiplying-means',
        "course": "basic", "unit": 2,
        "topic": 'What multiplying means',
        "op": '*', "max_value": 30,
        "levels": ("abstract",),
        "symbols": ('times', 'equals'),
        "advance_line": "Three in a row, and you can say why — you've got it! You know what multiplying means.",
        "why": [
            ("Why multiply? Because adding the same number again and again is slow. "
             "Three packs of four pencils: 4 plus 4 plus 4. Fine for three packs — "
             "but for twenty packs you would be adding all day. Multiplying is the "
             "short way to add equal groups.",
             '[[goal text="What multiplying means"]]'),
        ],
        "picture": [
            ("Here are three groups of four. Three rows, four dots in each row. "
             "Count them: 4, 8, 12. Three groups of four is twelve.",
             '[[array rows="3" cols="4" view="groups" caption="3 groups of 4 = 12"]]'),
        ],
        "teach": [
            ("That is what multiplying means: putting together equal groups. We "
             "write it with the times sign. Three times four means three groups of "
             "four, and it equals 12 — the same 12 as 4 plus 4 plus 4, written the "
             "short way.",
             '[[array rows="3" cols="4" caption="3 × 4 = 12"]][[step eq="4 + 4 + 4 = 12"]]'),
            ("One more, watch. Two times five is two groups of five: 5 plus 5 equals "
             "10. Two times five equals ten.",
             '[[array rows="2" cols="5" view="groups" caption="2 groups of 5 = 10"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Four times two is four groups "
                        "of two: 2 plus 2 plus 2 plus 2 equals 8. Four times two equals "
                        "eight.",
                        '[[array rows="4" cols="2" view="groups" caption="4 groups of 2 = 8"]]'),
             "ask": {'a': 3, 'b': 2, 'op': '*'}},
            {"worked": ("One more together. Five times three is five groups of three. "
                        "Count the rows: 3, 6, 9, 12, 15. Five times three equals "
                        "fifteen.",
                        '[[array rows="5" cols="3" view="groups" caption="5 groups of 3 = 15"]]'),
             "ask": {'a': 4, 'b': 3, 'op': '*'}},
        ],
        "practice_intro": ("Now it's your turn. Count the groups if you need to. Three "
                           "right answers in a row and we're done — here comes the "
                           "first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 3 times 4 equals "
                       "12. Tap the reason why."),
            # the second wrong reason is the classic confusion -- adding instead
            "choices": ("because it is 3 groups of 4 put together | because 3 and 4 "
                        "add up to 12 | because 12 is the biggest number"),
            "answer": "because it is 3 groups of 4 put together",
            "board": '[[array rows="3" cols="4" view="groups" caption="3 groups of 4 = 12"]]',
        },
        "recap": [
            ("So, here it is again. Multiplying means putting together equal groups. "
             "Three times four is three groups of four — 4 plus 4 plus 4 — and that "
             "equals 12.",
             '[[array rows="3" cols="4" caption="3 × 4 = 12"]]'),
            ("And it is the short way to add the same number many times — the more "
             "groups, the more it saves.",
             '[[step eq="4 + 4 + 4 = 3 × 4 = 12"]]'),
        ],
        "bank": [{'a': 2, 'b': 2, 'op': '*'}, {'a': 2, 'b': 3, 'op': '*'}, {'a': 3, 'b': 3, 'op': '*'}, {'a': 2, 'b': 5, 'op': '*'}, {'a': 4, 'b': 4, 'op': '*'}, {'a': 3, 'b': 5, 'op': '*'}, {'a': 4, 'b': 5, 'op': '*'}, {'a': 5, 'b': 5, 'op': '*'}],
    },
    {
        # (sr, 2026-09-05) TO THE SHAPE on the ARRAY. The ask is bare on purpose (a
        # times table is recall); every worked beat and every walk-back draws the array.
        # (sz, 2026-09-05) MASTERED BY A PASS, NOT A STREAK -- rulings ⑥ ⑦: after the
        # two worked pairs the student runs all 81 facts (1-9 times 1-9) in a shuffled
        # order; a slip draws that fact's array and restarts the pass; one clean pass
        # earns the reason question and the lesson. The bank below still feeds the
        # topic quiz and Abrabot's drill; the pass does not read it.
        "id": 'basic-u2-times-tables',
        "course": "basic", "unit": 2,
        "topic": 'Times tables',
        "op": '*', "max_value": 81,
        "mastery": "table",
        "levels": ("abstract",),
        "symbols": ('times', 'equals'),
        "advance_line": "Every fact right in one pass, and you can say why — the times tables are yours!",
        "why": [
            ("Why learn the times tables by heart? Because you use them constantly "
             "— sharing out, working out a bill, every bigger sum you will ever do. "
             "Knowing 6 times 7 the way you know your own name means the hard part "
             "of a problem never has to wait for the easy part.",
             '[[goal text="Times tables"]]'),
        ],
        "picture": [
            ("Every times table fact is a picture. Six times seven: six rows, seven "
             "dots in each. Count by sevens down the rows — 7, 14, 21, 28, 35, 42. "
             "Forty-two dots.",
             '[[array rows="6" cols="7" caption="6 rows of 7 = 42"]]'),
        ],
        "teach": [
            ("So six times seven equals 42. The times tables are these pictures, "
             "learned so well you no longer need to count them — up to nine times "
             "nine.",
             '[[array rows="6" cols="7" caption="6 × 7 = 42"]]'),
            ("A helpful trick: turn the picture on its side. Seven rows of six is "
             "the same dots, so seven times six is the same 42. The order does not "
             "change the answer — one fact learned is two facts known.",
             '[[array rows="7" cols="6" caption="7 × 6 = 42, the same dots"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Eight times six. Eight rows of "
                        "six — count by sixes: 6, 12, 18, 24, 30, 36, 42, 48. Eight "
                        "times six equals 48.",
                        '[[array rows="8" cols="6" caption="8 × 6 = 48"]]'),
             "ask": {'a': 8, 'b': 5, 'op': '*'}},
            {"worked": ("One more together. Nine times seven. Nine rows of seven is "
                        "63. Nine times seven equals 63.",
                        '[[array rows="9" cols="7" caption="9 × 7 = 63"]]'),
             "ask": {'a': 9, 'b': 6, 'op': '*'}},
        ],
        "practice_intro": ("Now the whole table — all 81 facts, one after another, in "
                           "any order. Get every one right and the table is yours. If "
                           "one slips, we look at its picture together, then start "
                           "again from the beginning. Here comes the first fact."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 6 times 7 and 7 "
                       "times 6 both equal 42. Tap the reason why."),
            "choices": ("because turning the rows on their side keeps the same dots | "
                        "because 6 and 7 are next to each other | because 42 is an "
                        "even number"),
            "answer": "because turning the rows on their side keeps the same dots",
            "board": '[[array rows="7" cols="6" caption="7 × 6 = 42, the same dots as 6 × 7"]]',
        },
        "recap": [
            ("So, here it is again. Every times table fact is rows of dots, and "
             "turning the rows on their side gives the same answer — one fact "
             "learned is two facts known.",
             '[[array rows="6" cols="7" caption="6 × 7 = 42"]]'),
            ("And knowing them by heart is what lets every bigger sum go quickly.",
             '[[step eq="6 × 7 = 42 · 7 × 6 = 42"]]'),
        ],
        "bank": [{'a': 3, 'b': 6, 'op': '*'}, {'a': 4, 'b': 6, 'op': '*'}, {'a': 5, 'b': 6, 'op': '*'}, {'a': 6, 'b': 6, 'op': '*'}, {'a': 6, 'b': 7, 'op': '*'}, {'a': 7, 'b': 7, 'op': '*'}, {'a': 8, 'b': 7, 'op': '*'}, {'a': 8, 'b': 8, 'op': '*'}, {'a': 9, 'b': 8, 'op': '*'}, {'a': 9, 'b': 9, 'op': '*'}],
    },
    {
        # (ss, 2026-09-05) TO THE SHAPE on the ARRAY read the other way: the dots to
        # share and the empty boxes, then the boxes filled.
        "id": 'basic-u3-what-dividing-means',
        "course": "basic", "unit": 3,
        "topic": 'What dividing means',
        "op": '/', "max_value": 45,
        "levels": ("abstract",),
        "symbols": ('divided', 'equals'),
        "advance_line": "Three in a row, and you can say why — you've got it! You know what dividing means.",
        "why": [
            ("Why divide? Because sharing fairly is one of the first things anyone "
             "needs to do with numbers. Twelve cookies, three friends — how many "
             "each? You could deal them out one at a time. Dividing is the quick "
             "way to know the answer before you start dealing.",
             '[[goal text="What dividing means"]]'),
        ],
        "picture": [
            ("Here are 12 dots to share, and 3 empty boxes. Deal them out: one to "
             "each box, then another, then another, until they are gone. Every box "
             "ends up with 4.",
             '[[array total="12" rows="3" ask="1" caption="12 to share, 3 equal groups"]]'),
        ],
        "teach": [
            ("That is what dividing means: sharing into equal groups. Twelve "
             "divided by three asks: share 12 into 3 equal groups — how many in "
             "each? Four. Twelve divided by three equals four.",
             '[[array rows="3" cols="4" view="groups" eq="12 ÷ 3 = 4" caption="12 shared into 3 groups: 4 in each"]]'),
            ("And look — it is the multiplying picture turned around. Three groups "
             "of four is 12, so twelve divided by three is four. Dividing undoes "
             "multiplying.",
             '[[array rows="3" cols="4" caption="3 × 4 = 12, so 12 ÷ 3 = 4"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Ten divided by two. Share 10 "
                        "into 2 equal groups: each gets 5. Ten divided by two equals "
                        "five.",
                        '[[array rows="2" cols="5" view="groups" eq="10 ÷ 2 = 5" caption="10 shared into 2 groups: 5 in each"]]'),
             "ask": {'a': 8, 'b': 2, 'op': '/'}},
            {"worked": ("One more together. Fifteen divided by five. Share 15 into 5 "
                        "equal groups — each gets 3. Fifteen divided by five equals "
                        "three.",
                        '[[array rows="5" cols="3" view="groups" eq="15 ÷ 5 = 3" caption="15 shared into 5 groups: 3 in each"]]'),
             "ask": {'a': 20, 'b': 5, 'op': '/'}},
        ],
        "practice_intro": ("Now it's your turn. Share the dots into the boxes if you "
                           "need to. Three right answers in a row and we're done — "
                           "here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 12 divided by 3 "
                       "equals 4. Tap the reason why."),
            "choices": ("because 12 shared into 3 equal groups puts 4 in each | "
                        "because 12 take away 3 leaves 9 | because 4 is smaller "
                        "than 12"),
            "answer": "because 12 shared into 3 equal groups puts 4 in each",
            "board": '[[array rows="3" cols="4" view="groups" eq="12 ÷ 3 = 4" caption="12 shared into 3 groups: 4 in each"]]',
        },
        "recap": [
            ("So, here it is again. Dividing means sharing into equal groups — "
             "twelve divided by three is 12 shared into 3 groups, 4 in each. And "
             "it is multiplying turned around: 3 groups of 4 is 12.",
             '[[array rows="3" cols="4" view="groups" eq="12 ÷ 3 = 4" caption="12 ÷ 3 = 4 · 3 × 4 = 12"]]'),
            ("And it is for sharing fairly — knowing the answer before you deal a "
             "single cookie.",
             '[[step eq="12 ÷ 3 = 4"]]'),
        ],
        "bank": [{'a': 6, 'b': 2, 'op': '/'}, {'a': 9, 'b': 3, 'op': '/'}, {'a': 12, 'b': 4, 'op': '/'}, {'a': 16, 'b': 4, 'op': '/'}, {'a': 18, 'b': 3, 'op': '/'}, {'a': 24, 'b': 6, 'op': '/'}, {'a': 28, 'b': 4, 'op': '/'}, {'a': 35, 'b': 7, 'op': '/'}, {'a': 36, 'b': 6, 'op': '/'}, {'a': 45, 'b': 9, 'op': '/'}],
    },
    {
        # (ss, 2026-09-05) TO THE SHAPE on the ARRAY with extra= -- the full groups and
        # the red dots that did not fit.
        "id": 'basic-u3-left-overs',
        "course": "basic", "unit": 3,
        "topic": 'Dividing with left-overs',
        "op": 'rem', "max_value": 50,
        "levels": ("abstract",),
        "symbols": ('shared', 'left'),
        "advance_line": "Three in a row, and you can say why — you've got it! You can handle the left-overs.",
        "why": [
            ("Sharing does not always come out even. Thirteen stickers, packs of "
             "four: you can fill three packs, and one sticker has no pack. Real "
             "life is full of left-overs — the last slice, the odd sock — so we "
             "need a way to say exactly how many are left.",
             '[[goal text="Dividing with left-overs"]]'),
        ],
        "picture": [
            ("Here are 13 dots shared into groups of 4. Three full groups — that "
             "is 12 dots — and one dot, in red, that did not fit. That one is the "
             "left-over.",
             '[[array rows="3" cols="4" extra="1" eq="13 ÷ 4 = 3 left over 1" caption="3 groups of 4, 1 left over"]]'),
        ],
        "teach": [
            ("Here is how to find it without drawing. 13 shared into groups of 4: "
             "three groups of four equals 12 — as many as fit — and 13 take away "
             "12 equals 1. So 1 is left over.",
             '[[array rows="3" cols="4" extra="1" eq="13 ÷ 4 = 3 left over 1" caption="3 × 4 = 12, 13 − 12 = 1"]]'),
            ("One more, watch. 17 shared into groups of 5. Three groups of five "
             "equals 15, and 17 take away 15 equals 2. So 2 are left over.",
             '[[array rows="3" cols="5" extra="2" eq="17 ÷ 5 = 3 left over 2" caption="3 groups of 5, 2 left over"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 11 shared into groups of 3. "
                        "Three groups of three equals 9, and 11 take away 9 equals "
                        "2. So 2 are left over.",
                        '[[array rows="3" cols="3" extra="2" eq="11 ÷ 3 = 3 left over 2" caption="3 groups of 3, 2 left over"]]'),
             "ask": {'a': 10, 'b': 3, 'op': 'rem'}},
            {"worked": ("One more together. 14 shared into groups of 4. Three groups "
                        "of four equals 12, and 14 take away 12 equals 2. So 2 are "
                        "left over.",
                        '[[array rows="3" cols="4" extra="2" eq="14 ÷ 4 = 3 left over 2" caption="3 groups of 4, 2 left over"]]'),
             "ask": {'a': 13, 'b': 5, 'op': 'rem'}},
        ],
        "practice_intro": ("Now it's your turn. Fill the groups, then count what did "
                           "not fit. Three right answers in a row and we're done — "
                           "here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 13 shared into "
                       "groups of 4 leaves 1 over. Tap the reason why."),
            "choices": ("because 3 groups of 4 is 12 and 13 is one more | because "
                        "13 is an odd number | because 4 does not go into 13"),
            "answer": "because 3 groups of 4 is 12 and 13 is one more",
            "board": '[[array rows="3" cols="4" extra="1" eq="13 ÷ 4 = 3 left over 1" caption="3 groups of 4, 1 left over"]]',
        },
        "recap": [
            ("So, here it is again. Fill as many equal groups as you can, then take "
             "that away from what you started with. What is left is the "
             "left-over — always smaller than a group.",
             '[[array rows="3" cols="4" extra="1" eq="13 ÷ 4 = 3 left over 1" caption="the red dot is the left-over"]]'),
            ("And it is for real life, where sharing rarely comes out even.",
             '[[step eq="13 ÷ 4 = 3 left over 1"]]'),
        ],
        "bank": [{'a': 7, 'b': 2, 'op': 'rem'}, {'a': 9, 'b': 4, 'op': 'rem'}, {'a': 11, 'b': 4, 'op': 'rem'}, {'a': 14, 'b': 3, 'op': 'rem'}, {'a': 17, 'b': 4, 'op': 'rem'}, {'a': 19, 'b': 5, 'op': 'rem'}, {'a': 23, 'b': 5, 'op': 'rem'}, {'a': 26, 'b': 6, 'op': 'rem'}, {'a': 31, 'b': 7, 'op': 'rem'}, {'a': 38, 'b': 8, 'op': 'rem'}],
    },
    {
        # (st, 2026-09-05) TO THE SHAPE on the ARRAY: a missing factor is the sharing
        # question -- b boxes, a dots, how many in each? -- and the answer is the boxes
        # filled.
        "id": 'basic-u4-missing-factors',
        "course": "basic", "unit": 4,
        "topic": 'Missing factors',
        "op": 'mf', "max_value": 72,
        "levels": ("abstract",),
        "symbols": ('times', 'factor'),
        "advance_line": "Three in a row, and you can say why — you've got it! You can find the missing factor.",
        "why": [
            ("A factor is a number you multiply: in 3 times 4 equals 12, the factors "
             "are 3 and 4. Real questions often hand you the answer and hide a "
             "factor — twelve cookies, three bags, how many in each? Finding the "
             "hidden factor is what today is for.",
             '[[goal text="Missing factors"]]'),
        ],
        "picture": [
            ("Here is 3 times what equals 12, as a picture: 12 dots and 3 empty "
             "boxes. Three groups of WHAT reach 12? Share the dots out — every box "
             "gets 4. The hidden factor is 4.",
             '[[array total="12" rows="3" ask="1" eq="3 × ? = 12" caption="3 groups of what reach 12?"]]'),
        ],
        "teach": [
            ("So a missing factor is a sharing question in disguise. 3 times what "
             "equals 12 asks: 12 shared into 3 groups, how many in each? Four. "
             "Three times four equals 12 — and that times fact is the check.",
             '[[array rows="3" cols="4" view="groups" eq="3 × 4 = 12" caption="3 groups of 4 reach 12"]]'),
            ("One more, watch. 5 times what equals 30? Share 30 into 5 groups — 6 "
             "in each. Five times six equals 30. The missing factor is 6.",
             '[[array rows="5" cols="6" view="groups" eq="5 × 6 = 30" caption="5 groups of 6 reach 30"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 4 times what equals 20? Share "
                        "20 into 4 groups — 5 in each. Four times five equals 20. The "
                        "missing factor is 5.",
                        '[[array rows="4" cols="5" view="groups" eq="4 × 5 = 20" caption="4 groups of 5 reach 20"]]'),
             "ask": {'a': 16, 'b': 4, 'op': 'mf'}},
            {"worked": ("One more together. 6 times what equals 42? Share 42 into 6 "
                        "groups — 7 in each. Six times seven equals 42.",
                        '[[array rows="6" cols="7" view="groups" eq="6 × 7 = 42" caption="6 groups of 7 reach 42"]]'),
             "ask": {'a': 36, 'b': 6, 'op': 'mf'}},
        ],
        "practice_intro": ("Now it's your turn. Share the dots into the boxes if you "
                           "need to. Three right answers in a row and we're done — "
                           "here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. In 3 times what "
                       "equals 12, the missing factor is 4. Tap the reason why."),
            "choices": ("because 12 shared into 3 groups puts 4 in each | because "
                        "12 take away 3 leaves 9 | because 4 comes after 3"),
            "answer": "because 12 shared into 3 groups puts 4 in each",
            "board": '[[array rows="3" cols="4" view="groups" eq="3 × 4 = 12" caption="3 groups of 4 reach 12"]]',
        },
        "recap": [
            ("So, here it is again. A missing factor is a sharing question: share "
             "the answer into the groups you know, and what each group gets is the "
             "hidden factor. Then the times fact checks it.",
             '[[array rows="3" cols="4" view="groups" eq="3 × 4 = 12" caption="3 groups of 4 reach 12"]]'),
            ("And it is for the questions that hand you the answer and hide a "
             "factor — which is most of them.",
             '[[step eq="3 × ? = 12"]][[step eq="12 ÷ 3 = 4"]]'),
        ],
        "bank": [{'a': 6, 'b': 2, 'op': 'mf'}, {'a': 12, 'b': 3, 'op': 'mf'}, {'a': 15, 'b': 3, 'op': 'mf'}, {'a': 24, 'b': 4, 'op': 'mf'}, {'a': 30, 'b': 5, 'op': 'mf'}, {'a': 35, 'b': 5, 'op': 'mf'}, {'a': 48, 'b': 6, 'op': 'mf'}, {'a': 56, 'b': 7, 'op': 'mf'}, {'a': 63, 'b': 9, 'op': 'mf'}, {'a': 72, 'b': 8, 'op': 'mf'}],
    },
    {
        # (st, 2026-09-05) TO THE SHAPE on the VENN: the two factor lists, the
        # overlap holding what they share, the greatest of the overlap circled by
        # the caption.
        "id": 'basic-u4-greatest-common-factor',
        "course": "basic", "unit": 4,
        "topic": 'The greatest common factor',
        "op": 'gcf', "max_value": 48,
        "levels": ("abstract",),
        "symbols": ('factor', 'greatest'),
        "advance_line": "Three in a row, and you can say why — you've got it! You can find the greatest common factor.",
        "why": [
            ("Two numbers can share factors. 12 and 18 are both made of 2s and 3s. "
             "Knowing the biggest thing two numbers share is how you cut a "
             "fraction down to its simplest form, and how you split two piles "
             "into the biggest equal groups possible. Today we find it.",
             '[[goal text="The greatest common factor"]]'),
        ],
        "picture": [
            ("Here are the factors of 12 and the factors of 18 in two circles. "
             "Where the circles overlap sit the factors they share: 1, 2, 3 and "
             "6. The greatest one in the overlap is 6.",
             '[[venn left="Factors of 12" right="Factors of 18" a="4, 12" both="1, 2, 3, 6" b="9, 18" caption="they share 1, 2, 3, 6 — the greatest is 6"]]'),
        ],
        "teach": [
            ("So a common factor divides both numbers evenly, and the greatest "
             "common factor is the biggest one in the overlap. List the factors "
             "of each, find what they share, take the greatest. For 12 and 18, "
             "that is 6.",
             '[[step eq="12: 1, 2, 3, 4, 6, 12"]][[step eq="18: 1, 2, 3, 6, 9, 18"]][[step eq="GCF of 12 and 18 = 6"]]'),
            ("One more, watch. 8 and 20. Factors of 8: 1, 2, 4, 8. Factors of 20: "
             "1, 2, 4, 5, 10, 20. The overlap is 1, 2 and 4 — the greatest common "
             "factor equals 4.",
             '[[venn left="Factors of 8" right="Factors of 20" a="8" both="1, 2, 4" b="5, 10, 20" caption="they share 1, 2, 4 — the greatest is 4"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 6 and 9. Factors of 6: 1, 2, "
                        "3, 6. Factors of 9: 1, 3, 9. The overlap is 1 and 3 — the "
                        "greatest common factor equals 3.",
                        '[[venn left="Factors of 6" right="Factors of 9" a="2, 6" both="1, 3" b="9" caption="they share 1, 3 — the greatest is 3"]]'),
             "ask": {'a': 6, 'b': 8, 'op': 'gcf'}},
            {"worked": ("One more together. 10 and 15. Factors of 10: 1, 2, 5, 10. "
                        "Factors of 15: 1, 3, 5, 15. The overlap is 1 and 5 — the "
                        "greatest one they share equals 5.",
                        '[[venn left="Factors of 10" right="Factors of 15" a="2, 10" both="1, 5" b="3, 15" caption="they share 1, 5 — the greatest is 5"]]'),
             "ask": {'a': 12, 'b': 16, 'op': 'gcf'}},
        ],
        "practice_intro": ("Now it's your turn. List the factors, find the overlap, "
                           "take the greatest. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The greatest "
                       "common factor of 12 and 18 is 6, not 12. Tap the reason why."),
            "choices": ("because 12 is not a factor of 18 | because 6 is half of 12 "
                        "| because 18 take away 12 is 6"),
            "answer": "because 12 is not a factor of 18",
            "board": '[[venn left="Factors of 12" right="Factors of 18" a="4, 12" both="1, 2, 3, 6" b="9, 18" caption="12 sits outside the overlap"]]',
        },
        "recap": [
            ("So, here it is again. List the factors of each number, look at what "
             "they share, and take the greatest — the biggest number in the "
             "overlap.",
             '[[venn left="Factors of 12" right="Factors of 18" a="4, 12" both="1, 2, 3, 6" b="9, 18" caption="the greatest in the overlap is 6"]]'),
            ("And it is the number you will use to simplify fractions and to make "
             "the biggest equal groups.",
             '[[step eq="GCF of 12 and 18 = 6"]]'),
        ],
        "bank": [{'a': 4, 'b': 6, 'op': 'gcf'}, {'a': 6, 'b': 10, 'op': 'gcf'}, {'a': 8, 'b': 12, 'op': 'gcf'}, {'a': 9, 'b': 12, 'op': 'gcf'}, {'a': 14, 'b': 21, 'op': 'gcf'}, {'a': 18, 'b': 24, 'op': 'gcf'}, {'a': 10, 'b': 25, 'op': 'gcf'}, {'a': 20, 'b': 30, 'op': 'gcf'}, {'a': 24, 'b': 36, 'op': 'gcf'}, {'a': 32, 'b': 48, 'op': 'gcf'}],
    },
    {
        # (su, 2026-09-05) TO THE SHAPE on the ARRAY shared into equal parts: one part
        # is the fraction.
        "id": 'basic-u5-fraction-of-a-group',
        "course": "basic", "unit": 5,
        "topic": 'A fraction of a group',
        "op": 'of', "max_value": 24,
        "levels": ("abstract",),
        "symbols": ('share', 'equal'),
        "advance_line": "Three in a row, and you can say why — you've got it! You can find a fraction of a group.",
        "why": [
            ("A fraction names equal shares — one half is one of two equal shares, "
             "one fourth is one of four. But shares of WHAT? Usually a group of "
             "things: half the class, a third of the cookies. Taking a fraction of "
             "a group is how fractions show up in real life.",
             '[[goal text="A fraction of a group"]]'),
        ],
        "picture": [
            ("Here are 8 dots and 2 boxes. One half of 8 means: share 8 into 2 "
             "equal parts and take one part. Each part gets 4. One half of 8 is "
             "4.",
             '[[array rows="2" cols="4" view="groups" eq="1/2 of 8 = 4" caption="8 shared into 2 equal parts — one part is 4"]]'),
        ],
        "teach": [
            ("So the bottom of the fraction says how many equal parts to share the "
             "group into, and one part is the answer. One half of 8: share into 2, "
             "one part is 4. One half of 8 equals 4.",
             '[[array rows="2" cols="4" view="groups" eq="1/2 of 8 = 4" caption="the bottom says how many parts"]]'),
            ("One more, watch. One third of 12. Share 12 into 3 equal parts — each "
             "gets 4. One part is one third. One third of 12 equals 4.",
             '[[array rows="3" cols="4" view="groups" eq="1/3 of 12 = 4" caption="12 shared into 3 equal parts — one part is 4"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. One fourth of 12. Share 12 "
                        "into 4 equal parts — each gets 3. One fourth of 12 equals 3.",
                        '[[array rows="4" cols="3" view="groups" eq="1/4 of 12 = 3" caption="12 shared into 4 equal parts — one part is 3"]]'),
             "ask": {'a': 8, 'b': 4, 'op': 'of'}},
            {"worked": ("One more together. One fifth of 10. Share 10 into 5 equal "
                        "parts — each gets 2. One fifth of 10 equals 2.",
                        '[[array rows="5" cols="2" view="groups" eq="1/5 of 10 = 2" caption="10 shared into 5 equal parts — one part is 2"]]'),
             "ask": {'a': 15, 'b': 5, 'op': 'of'}},
        ],
        "practice_intro": ("Now it's your turn. Share the dots into the parts if you "
                           "need to. Three right answers in a row and we're done — "
                           "here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. One third of 12 "
                       "is 4. Tap the reason why."),
            # the wrong reasons: the classic slip (a fraction as taking away), and noise
            "choices": ("because 12 shared into 3 equal parts gives 4 in each part | "
                        "because one third means take 3 away | because 4 is bigger "
                        "than 3"),
            "answer": "because 12 shared into 3 equal parts gives 4 in each part",
            "board": '[[array rows="3" cols="4" view="groups" eq="1/3 of 12 = 4" caption="one of the 3 equal parts"]]',
        },
        "recap": [
            ("So, here it is again. A fraction of a group: the bottom says how "
             "many equal parts to share into, and one part is the answer. One "
             "third of 12 is 4.",
             '[[array rows="3" cols="4" view="groups" eq="1/3 of 12 = 4" caption="share into 3, take one part"]]'),
            ("And that is how fractions show up in real life — a fraction of a "
             "group of things.",
             '[[step eq="1/3 of 12 = 12 ÷ 3 = 4"]]'),
        ],
        "bank": [{'a': 4, 'b': 2, 'op': 'of'}, {'a': 6, 'b': 2, 'op': 'of'}, {'a': 6, 'b': 3, 'op': 'of'}, {'a': 10, 'b': 2, 'op': 'of'}, {'a': 9, 'b': 3, 'op': 'of'}, {'a': 12, 'b': 2, 'op': 'of'}, {'a': 12, 'b': 3, 'op': 'of'}, {'a': 16, 'b': 4, 'op': 'of'}, {'a': 20, 'b': 5, 'op': 'of'}, {'a': 24, 'b': 6, 'op': 'of'}],
    },
    {
        # (su, 2026-09-05) TO THE SHAPE on TWO PIES: the same amount, cut two ways.
        "id": 'basic-u5-equivalent-fractions',
        "course": "basic", "unit": 5,
        "topic": 'Equivalent fractions',
        "op": 'eqf', "max_value": 12,
        "levels": ("abstract",),
        "symbols": ('equal', 'same'),
        "advance_line": "Three in a row, and you can say why — you've got it! You can spot equal fractions.",
        "why": [
            ("Two fractions can name the SAME amount. Half a pizza and two fourths "
             "of a pizza are the same pizza — one is just cut smaller. Knowing "
             "which fractions are secretly equal is what lets you compare them and "
             "add them later.",
             '[[goal text="Equivalent fractions"]]'),
        ],
        "picture": [
            ("Here are two pies. The first is cut into 2, and one half is shaded. "
             "The second is the same pie cut into 4 — every half cut in two — and "
             "two fourths are shaded. Look: the shaded amount is exactly the same.",
             '[[pie parts="2" shaded="1" caption="one half"]][[pie parts="4" shaded="2" caption="two fourths — the same amount"]]'),
        ],
        "teach": [
            ("So: one half equals how many fourths? Cut every half into two — two "
             "halves become four fourths, and ONE half becomes TWO fourths. One "
             "half equals two fourths. Same amount, smaller pieces.",
             '[[pie parts="2" shaded="1" caption="1/2"]][[pie parts="4" shaded="2" caption="2/4 — equal fractions"]]'),
            ("One more, watch. One third equals how many sixths? Cut every third in "
             "two — one third becomes two sixths.",
             '[[pie parts="3" shaded="1" caption="one third"]][[pie parts="6" shaded="2" caption="two sixths — the same amount"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. One half equals how many "
                        "sixths? Cut every half into three — one half equals three "
                        "sixths.",
                        '[[pie parts="2" shaded="1" caption="one half"]][[pie parts="6" shaded="3" caption="three sixths — the same amount"]]'),
             "ask": {'a': 1, 'b': 2, 'c': 8, 'op': 'eqf'}},
            {"worked": ("One more together. One fourth equals how many eighths? Cut "
                        "every fourth in two — one fourth equals two eighths.",
                        '[[pie parts="4" shaded="1" caption="one fourth"]][[pie parts="8" shaded="2" caption="two eighths — the same amount"]]'),
             "ask": {'a': 1, 'b': 2, 'c': 10, 'op': 'eqf'}},
        ],
        "practice_intro": ("Now it's your turn. Look at the two pies. Three right "
                           "answers in a row and we're done — here comes the first "
                           "one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. One half equals "
                       "two fourths. Tap the reason why."),
            "choices": ("because cutting each half in two keeps the same amount | "
                        "because 2 plus 2 makes 4 | because fourths are bigger than "
                        "halves"),
            "answer": "because cutting each half in two keeps the same amount",
            "board": '[[pie parts="2" shaded="1" caption="1/2"]][[pie parts="4" shaded="2" caption="2/4 — the same amount"]]',
        },
        "recap": [
            ("So, here it is again. Equal fractions name the same amount cut into "
             "different pieces. Cut every piece the same way and the shaded amount "
             "never changes — one half is two fourths is three sixths.",
             '[[pie parts="2" shaded="1" caption="1/2"]][[pie parts="4" shaded="2" caption="2/4"]][[pie parts="6" shaded="3" caption="3/6"]]'),
            ("And spotting equal fractions is what lets you compare and add them "
             "later.",
             '[[step eq="1/2 = 2/4 = 3/6"]]'),
        ],
        "bank": [{'a': 1, 'b': 2, 'c': 4, 'op': 'eqf'}, {'a': 1, 'b': 3, 'c': 6, 'op': 'eqf'}, {'a': 1, 'b': 2, 'c': 6, 'op': 'eqf'}, {'a': 1, 'b': 4, 'c': 8, 'op': 'eqf'}, {'a': 1, 'b': 5, 'c': 10, 'op': 'eqf'}, {'a': 1, 'b': 6, 'c': 12, 'op': 'eqf'}, {'a': 1, 'b': 4, 'c': 12, 'op': 'eqf'}, {'a': 1, 'b': 3, 'c': 12, 'op': 'eqf'}, {'a': 1, 'b': 2, 'c': 12, 'op': 'eqf'}],
    },
    {
        # (sv, 2026-09-05) TO THE SHAPE on the FRACTION LINE: start at the first
        # fraction, hop by the second, read where you land.
        "id": 'basic-u6-add-fractions-same-bottom',
        "course": "basic", "unit": 6,
        "topic": 'Adding fractions',
        "op": 'fa', "max_value": 12,
        "levels": ("abstract",),
        "symbols": ('bottom', 'plus'),
        "advance_line": "Three in a row, and you can say why — you've got it! You can add fractions with the same bottom.",
        "why": [
            ("Fractions get added all the time — two eighths of a pizza now and three "
             "eighths later, how much did you eat? When the two fractions have the "
             "SAME bottom, the pieces are the same size, and adding is just "
             "counting pieces.",
             '[[goal text="Adding fractions"]]'),
        ],
        "picture": [
            ("Here is a line from 0 to 1 cut into eighths. Start at two eighths. "
             "Hop three more eighths — one, two, three. You land on five eighths.",
             '[[numberline min="0" max="1" denom="8" hops="0,0.25,0.625" points="0.625" caption="2/8 + 3/8 = 5/8"]]'),
        ],
        "teach": [
            ("So when the bottoms are the same, count the pieces: 2 plus 3 equals 5. "
             "Two eighths plus three eighths equals five eighths. The bottom stays "
             "the same — only the count changes.",
             '[[numberline min="0" max="1" denom="8" hops="0,0.25,0.625" points="0.625" caption="count the pieces: 2 + 3 = 5 eighths"]]'),
            ("One more, watch. One fourth plus two fourths. Start at one fourth, hop "
             "two more. Three fourths.",
             '[[numberline min="0" max="1" denom="4" hops="0,0.25,0.75" points="0.75" caption="1/4 + 2/4 = 3/4"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Two sixths plus three sixths. "
                        "Start at two sixths, hop three more: 2 plus 3 equals 5. Five "
                        "sixths.",
                        '[[numberline min="0" max="1" denom="6" hops="0,0.3333,0.8333" points="0.8333" caption="2/6 + 3/6 = 5/6"]]'),
             "ask": {'a': 1, 'b': 3, 'c': 6, 'op': 'fa'}},
            {"worked": ("One more together. Three tenths plus four tenths. Start at "
                        "three tenths, hop four more: 3 plus 4 equals 7. Seven tenths.",
                        '[[numberline min="0" max="1" denom="10" hops="0,0.3,0.7" points="0.7" caption="3/10 + 4/10 = 7/10"]]'),
             "ask": {'a': 2, 'b': 5, 'c': 10, 'op': 'fa'}},
        ],
        "practice_intro": ("Now it's your turn. Start at the first fraction and hop. "
                           "Three right answers in a row and we're done — here comes "
                           "the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Two eighths plus "
                       "three eighths is five eighths, not five sixteenths. Tap the "
                       "reason why."),
            "choices": ("because the pieces stay eighths — only the count changes | "
                        "because 8 plus 8 is 16 | because sixteenths are too small"),
            "answer": "because the pieces stay eighths — only the count changes",
            "board": '[[numberline min="0" max="1" denom="8" hops="0,0.25,0.625" points="0.625" caption="the bottom stays 8"]]',
        },
        "recap": [
            ("So, here it is again. Same bottom means same-size pieces: add the "
             "tops, keep the bottom. On the line, start at the first fraction and "
             "hop by the second.",
             '[[numberline min="0" max="1" denom="8" hops="0,0.25,0.625" points="0.625" caption="2/8 + 3/8 = 5/8"]]'),
            ("And it is for adding up pieces of the same whole — pizza, an hour, a "
             "mile.",
             '[[step eq="2/8 + 3/8 = 5/8"]]'),
        ],
        "bank": [{'a': 1, 'b': 1, 'c': 4, 'op': 'fa'}, {'a': 1, 'b': 2, 'c': 5, 'op': 'fa'}, {'a': 2, 'b': 2, 'c': 6, 'op': 'fa'}, {'a': 1, 'b': 4, 'c': 6, 'op': 'fa'}, {'a': 2, 'b': 3, 'c': 8, 'op': 'fa'}, {'a': 3, 'b': 3, 'c': 8, 'op': 'fa'}, {'a': 2, 'b': 5, 'c': 8, 'op': 'fa'}, {'a': 4, 'b': 3, 'c': 10, 'op': 'fa'}, {'a': 3, 'b': 5, 'c': 10, 'op': 'fa'}, {'a': 5, 'b': 4, 'c': 12, 'op': 'fa'}],
    },
    {
        # (sv, 2026-09-05) TO THE SHAPE on the FRACTION LINE: start at the first
        # fraction, hop BACK by the second.
        "id": 'basic-u6-take-away-fractions-same-bottom',
        "course": "basic", "unit": 6,
        "topic": 'Taking away fractions',
        "op": 'fs', "max_value": 12,
        "levels": ("abstract",),
        "symbols": ('bottom', 'take'),
        "advance_line": "Three in a row, and you can say why — you've got it! You can take away fractions with the same bottom.",
        "why": [
            ("Five eighths of a pizza is left and someone eats two eighths — how "
             "much is left now? Taking away fractions with the same bottom works "
             "like adding did: the pieces are the same size, so you just count "
             "what is left.",
             '[[goal text="Taking away fractions"]]'),
        ],
        "picture": [
            ("Here is the line cut into eighths. Start at five eighths. Hop back "
             "two eighths — one, two. You land on three eighths.",
             '[[numberline min="0" max="1" denom="8" hops="0.625,0.375" points="0.375" caption="5/8 − 2/8 = 3/8"]]'),
        ],
        "teach": [
            ("So when the bottoms are the same, count what is left: 5 take away 2 "
             "equals 3. Five eighths take away two eighths equals three eighths. The "
             "bottom stays the same.",
             '[[numberline min="0" max="1" denom="8" hops="0.625,0.375" points="0.375" caption="count back: 5 − 2 = 3 eighths"]]'),
            ("One more, watch. Three fourths take away one fourth. Start at three "
             "fourths, hop back one. Two fourths.",
             '[[numberline min="0" max="1" denom="4" hops="0.75,0.5" points="0.5" caption="3/4 − 1/4 = 2/4"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Four sixths take away one "
                        "sixth. Start at four sixths, hop back one: 4 take away 1 "
                        "equals 3. Three sixths.",
                        '[[numberline min="0" max="1" denom="6" hops="0.6667,0.5" points="0.5" caption="4/6 − 1/6 = 3/6"]]'),
             "ask": {'a': 5, 'b': 2, 'c': 6, 'op': 'fs'}},
            {"worked": ("One more together. Seven tenths take away three tenths. "
                        "Start at seven tenths, hop back three: 7 take away 3 equals "
                        "4. Four tenths.",
                        '[[numberline min="0" max="1" denom="10" hops="0.7,0.4" points="0.4" caption="7/10 − 3/10 = 4/10"]]'),
             "ask": {'a': 8, 'b': 5, 'c': 10, 'op': 'fs'}},
        ],
        "practice_intro": ("Now it's your turn. Start at the first fraction and hop "
                           "back. Three right answers in a row and we're done — here "
                           "comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Five eighths take "
                       "away two eighths is three eighths, and the bottom stayed 8. "
                       "Tap the reason why."),
            "choices": ("because the pieces are still eighths — only the count "
                        "changed | because 8 take away 8 is 0 | because eighths "
                        "cannot change"),
            "answer": "because the pieces are still eighths — only the count changed",
            "board": '[[numberline min="0" max="1" denom="8" hops="0.625,0.375" points="0.375" caption="the bottom stays 8"]]',
        },
        "recap": [
            ("So, here it is again. Same bottom means same-size pieces: take away "
             "the tops, keep the bottom. On the line, start at the first fraction "
             "and hop back by the second.",
             '[[numberline min="0" max="1" denom="8" hops="0.625,0.375" points="0.375" caption="5/8 − 2/8 = 3/8"]]'),
            ("And it is for finding what is left of a whole — the pizza, the hour, "
             "the tank of gas.",
             '[[step eq="5/8 − 2/8 = 3/8"]]'),
        ],
        "bank": [{'a': 3, 'b': 1, 'c': 4, 'op': 'fs'}, {'a': 4, 'b': 2, 'c': 5, 'op': 'fs'}, {'a': 5, 'b': 1, 'c': 6, 'op': 'fs'}, {'a': 5, 'b': 3, 'c': 6, 'op': 'fs'}, {'a': 6, 'b': 2, 'c': 8, 'op': 'fs'}, {'a': 7, 'b': 3, 'c': 8, 'op': 'fs'}, {'a': 7, 'b': 5, 'c': 8, 'op': 'fs'}, {'a': 8, 'b': 3, 'c': 10, 'op': 'fs'}, {'a': 9, 'b': 4, 'c': 10, 'op': 'fs'}, {'a': 11, 'b': 5, 'c': 12, 'op': 'fs'}],
    },
    {
        # (sw, 2026-09-05) TO THE SHAPE on the 0-to-1 line, which speaks in tenths.
        "id": 'basic-u7-tenths',
        "course": "basic", "unit": 7,
        "topic": 'Tenths',
        "op": 'dt', "max_value": 9,
        "levels": ("abstract",),
        "symbols": ('tenth', 'point'),
        "advance_line": "Three in a row, and you can say why — you've got it! You know your tenths.",
        "why": [
            ("Today we meet decimals — the way money, rulers and race times write "
             "parts of a whole. Split one whole into ten equal parts and each part "
             "is one tenth. We write one tenth with a point: 0.1. It is a fraction "
             "in a new coat.",
             '[[goal text="Tenths"]]'),
        ],
        "picture": [
            ("Here is the line from 0 to 1 cut into ten equal hops: 0.1, 0.2, 0.3 "
             "and so on. Start at 0.3 — three tenths. Hop four more tenths. You "
             "land on 0.7.",
             '[[numberline min="0" max="1" hops="0,0.3,0.7" points="0.7" caption="0.3 + 0.4 = 0.7"]]'),
        ],
        "teach": [
            ("So 0.3 is three tenths and 0.4 is four tenths, and adding them is "
             "counting tenths: 3 plus 4 equals 7. Three tenths plus four tenths "
             "equals seven tenths — 0.7. The point stays put; only the count "
             "changes.",
             '[[numberline min="0" max="1" hops="0,0.3,0.7" points="0.7" caption="count the tenths: 3 + 4 = 7"]]'),
            ("The point keeps the tenths in their own place, just like tens and "
             "ones have places. One more: 0.2 plus 0.5. Start at 0.2, hop five. "
             "0.7.",
             '[[numberline min="0" max="1" hops="0,0.2,0.7" points="0.7" caption="0.2 + 0.5 = 0.7"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Two tenths plus six tenths. "
                        "Start at 0.2, hop six more: 2 plus 6 equals 8. Eight tenths "
                        "— 0.8.",
                        '[[numberline min="0" max="1" hops="0,0.2,0.8" points="0.8" caption="0.2 + 0.6 = 0.8"]]'),
             "ask": {'a': 1, 'b': 3, 'op': 'dt'}},
            {"worked": ("One more together. Five tenths plus four tenths. Start at "
                        "0.5, hop four more: 5 plus 4 equals 9. Nine tenths — 0.9.",
                        '[[numberline min="0" max="1" hops="0,0.5,0.9" points="0.9" caption="0.5 + 0.4 = 0.9"]]'),
             "ask": {'a': 2, 'b': 4, 'op': 'dt'}},
        ],
        "practice_intro": ("Now it's your turn. Start at the first number and hop. "
                           "Three right answers in a row and we're done — here comes "
                           "the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 0.3 plus 0.4 is "
                       "0.7, and the point did not move. Tap the reason why."),
            "choices": ("because we counted tenths, and tenths stay in the tenths "
                        "place | because the point is just decoration | because 3 "
                        "plus 4 is less than 10"),
            "answer": "because we counted tenths, and tenths stay in the tenths place",
            "board": '[[numberline min="0" max="1" hops="0,0.3,0.7" points="0.7" caption="the point stays put"]]',
        },
        "recap": [
            ("So, here it is again. A tenth is one of ten equal parts of a whole, "
             "written after the point. Adding tenths is counting tenths — hop along "
             "the line — and the point stays put.",
             '[[numberline min="0" max="1" hops="0,0.3,0.7" points="0.7" caption="0.3 + 0.4 = 0.7"]]'),
            ("And decimals are how money, rulers and race times write parts of a "
             "whole.",
             '[[step eq="0.3 + 0.4 = 0.7"]]'),
        ],
        "bank": [{'a': 1, 'b': 2, 'op': 'dt'}, {'a': 2, 'b': 2, 'op': 'dt'}, {'a': 1, 'b': 4, 'op': 'dt'}, {'a': 3, 'b': 3, 'op': 'dt'}, {'a': 2, 'b': 5, 'op': 'dt'}, {'a': 4, 'b': 4, 'op': 'dt'}, {'a': 3, 'b': 5, 'op': 'dt'}, {'a': 6, 'b': 3, 'op': 'dt'}, {'a': 4, 'b': 5, 'op': 'dt'}, {'a': 7, 'b': 2, 'op': 'dt'}],
    },
    {
        # (sw, 2026-09-05) TO THE SHAPE on the PLACE-VALUE CHART: dimes are tens,
        # pennies are ones -- rods and cubes.
        "id": 'basic-u7-dimes-and-pennies',
        "course": "basic", "unit": 7,
        "topic": 'Dimes and pennies',
        "op": 'm', "max_value": 99,
        "levels": ("abstract",),
        "symbols": ('dime', 'penny'),
        "advance_line": "Three in a row, and you can say why — you've got it! You can count money like a shopkeeper.",
        "why": [
            ("Money is the place-value chart you carry in your pocket. A dime is "
             "worth ten cents and a penny is worth one cent — so dimes are the "
             "tens and pennies are the ones. Count them the way you read a "
             "two-digit number, and you can count money like a shopkeeper.",
             '[[goal text="Dimes and pennies"]]'),
        ],
        "picture": [
            ("Here is the chart with 3 dimes in the tens column and 4 pennies in "
             "the ones column. Three rods — thirty. Four cubes — four. 34 cents.",
             '[[placevalue t="3" o="4" caption="3 dimes + 4 pennies = 34 cents"]]'),
        ],
        "teach": [
            ("So: the dimes bring the tens, the pennies bring the ones. 3 dimes "
             "bring 30 cents, 4 pennies bring 4 more. 30 plus 4 equals 34 cents.",
             '[[placevalue t="3" o="4" caption="30 + 4 = 34 cents"]]'),
            ("One more, watch. 5 dimes and 2 pennies. Five rods, two cubes. 50 plus "
             "2 equals 52 cents.",
             '[[placevalue t="5" o="2" caption="5 dimes + 2 pennies = 52 cents"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 2 dimes and 7 pennies. The "
                        "dimes bring 20 cents, the pennies bring 7 more. 20 plus 7 "
                        "equals 27 cents.",
                        '[[placevalue t="2" o="7" caption="2 dimes + 7 pennies = 27 cents"]]'),
             "ask": {'a': 2, 'b': 5, 'op': 'm'}},
            {"worked": ("One more together. 4 dimes and 6 pennies. The dimes bring 40 "
                        "cents, the pennies bring 6 more. 40 plus 6 equals 46 cents.",
                        '[[placevalue t="4" o="6" caption="4 dimes + 6 pennies = 46 cents"]]'),
             "ask": {'a': 4, 'b': 3, 'op': 'm'}},
        ],
        "practice_intro": ("Now it's your turn. Dimes in the tens column, pennies in "
                           "the ones. Three right answers in a row and we're done — "
                           "here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 3 dimes and 4 "
                       "pennies is 34 cents, not 7 cents. Tap the reason why."),
            "choices": ("because a dime is ten cents, so dimes are the tens column | "
                        "because dimes are bigger coins than pennies | because 34 is "
                        "bigger than 7"),
            "answer": "because a dime is ten cents, so dimes are the tens column",
            "board": '[[placevalue t="3" o="4" caption="dimes are tens, pennies are ones"]]',
        },
        "recap": [
            ("So, here it is again. Dimes are tens, pennies are ones. Read the "
             "coins like a two-digit number — dimes first, then pennies — and you "
             "have the cents.",
             '[[placevalue t="3" o="4" caption="3 dimes + 4 pennies = 34 cents"]]'),
            ("And it is the place-value chart in your pocket.",
             '[[step eq="3 dimes + 4 pennies = 34 cents"]]'),
        ],
        "bank": [{'a': 1, 'b': 2, 'op': 'm'}, {'a': 1, 'b': 5, 'op': 'm'}, {'a': 2, 'b': 3, 'op': 'm'}, {'a': 3, 'b': 1, 'op': 'm'}, {'a': 3, 'b': 6, 'op': 'm'}, {'a': 5, 'b': 4, 'op': 'm'}, {'a': 6, 'b': 2, 'op': 'm'}, {'a': 7, 'b': 5, 'op': 'm'}, {'a': 8, 'b': 8, 'op': 'm'}, {'a': 9, 'b': 9, 'op': 'm'}],
    },
    {
        # (sx, 2026-09-05) TO THE SHAPE: a percent of a number is the sharing picture
        # -- 50 percent is one of two equal parts, 25 one of four, 10 one of ten.
        "id": 'basic-u8-percent-of',
        "course": "basic", "unit": 8,
        "topic": 'Percent',
        "op": 'pc', "max_value": 100,
        "levels": ("abstract",),
        "symbols": ('percent', 'hundred'),
        "advance_line": "Three in a row, and you can say why — you've got it! You can take a percent of a number.",
        "why": [
            ("Percent means out of one hundred. Fifty percent is fifty out of a "
             "hundred — one half. Twenty-five percent is one fourth. Ten percent is "
             "one tenth. Taking a percent OF a number is how you work out a tip, a "
             "tax, or how much battery is left.",
             '[[goal text="Percent"]]'),
        ],
        "picture": [
            ("Here is 50 percent of 8. Fifty percent is one half — one of two equal "
             "parts. Share 8 into 2 parts, take one: 4. Fifty percent of 8 is 4.",
             '[[hundredgrid shaded="50" unit="percent" caption="50% is one half of the square"]]'
             '[[array rows="2" cols="4" view="groups" eq="50% of 8 = 4" caption="one of 2 equal parts of 8"]]'),
        ],
        "teach": [
            ("So a percent of a number is a share: turn the percent into its "
             "fraction, share into that many equal parts, take one. 50 percent is "
             "one half, and one half of 8 equals 4.",
             '[[array rows="2" cols="4" view="groups" eq="50% of 8 = 4" caption="50% = one half"]]'),
            ("One more, watch. 10 percent of 40. Ten percent is one tenth — one of "
             "ten equal parts. Share 40 into 10 parts, take one: 4. So 10 percent "
             "of 40 equals 4.",
             '[[array rows="10" cols="4" view="groups" eq="10% of 40 = 4" caption="10% = one tenth"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 25 percent of 8. Twenty-five "
                        "percent is one fourth. Share 8 into 4 parts, take one: 2.",
                        '[[array rows="4" cols="2" view="groups" eq="25% of 8 = 2" caption="25% = one fourth"]]'),
             "ask": {'a': 25, 'b': 12, 'op': 'pc'}},
            {"worked": ("One more together. 50 percent of 12. Fifty percent is one "
                        "half. Share 12 into 2 parts, take one: 6.",
                        '[[array rows="2" cols="6" view="groups" eq="50% of 12 = 6" caption="50% = one half"]]'),
             "ask": {'a': 50, 'b': 14, 'op': 'pc'}},
        ],
        "practice_intro": ("Now it's your turn. Turn the percent into its share. Three "
                           "right answers in a row and we're done — here comes the "
                           "first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 50 percent of 8 "
                       "is 4. Tap the reason why."),
            "choices": ("because 50 percent is one half, and half of 8 is 4 | because "
                        "50 take away 8 is 42 | because 4 is half of 50"),
            "answer": "because 50 percent is one half, and half of 8 is 4",
            "board": '[[array rows="2" cols="4" view="groups" eq="50% of 8 = 4" caption="50% = one half"]]',
        },
        "recap": [
            ("So, here it is again. Percent means out of a hundred: 50 percent is a "
             "half, 25 a fourth, 10 a tenth. A percent of a number is that share of "
             "it — split into equal parts and take one.",
             '[[hundredgrid shaded="25" unit="percent" caption="25% is one fourth of the square"]]'),
            ("And it is how you work out a tip, a tax, or the battery left.",
             '[[step eq="50% of 8 = 4 · 25% of 8 = 2 · 10% of 40 = 4"]]'),
        ],
        "bank": [{'a': 50, 'b': 2, 'op': 'pc'}, {'a': 50, 'b': 4, 'op': 'pc'}, {'a': 25, 'b': 4, 'op': 'pc'}, {'a': 50, 'b': 6, 'op': 'pc'}, {'a': 50, 'b': 10, 'op': 'pc'}, {'a': 25, 'b': 16, 'op': 'pc'}, {'a': 50, 'b': 18, 'op': 'pc'}, {'a': 10, 'b': 20, 'op': 'pc'}, {'a': 10, 'b': 30, 'op': 'pc'}, {'a': 10, 'b': 50, 'op': 'pc'}],
    },
    {
        # (sx, 2026-09-05) TO THE SHAPE on the ARRAY: the dollars shared over the apples.
        "id": 'basic-u8-one-costs',
        "course": "basic", "unit": 8,
        "topic": 'What one costs',
        "op": 'rate', "max_value": 40,
        "levels": ("abstract",),
        "symbols": ('cost', 'divided'),
        "advance_line": "Three in a row, and you can say why — you've got it! You can find what one costs.",
        "why": [
            ("Prices often come in bunches: six apples for twelve dollars, three "
             "pens for nine. To compare two prices, you need what ONE costs — and "
             "that is sharing the dollars over the things, which is dividing.",
             '[[goal text="What one costs"]]'),
        ],
        "picture": [
            ("Here are 12 dollars shared over 6 apples — one box for each apple. "
             "Deal the dollars out: every apple gets 2. One apple costs 2 dollars.",
             '[[array rows="6" cols="2" view="groups" eq="12 ÷ 6 = 2" caption="12 dollars over 6 apples: 2 each"]]'),
        ],
        "teach": [
            ("So what one costs is the whole price divided by how many. 6 apples cost 12 "
             "dollars: 12 divided by 6 equals 2 — one apple costs 2 dollars.",
             '[[array rows="6" cols="2" view="groups" eq="12 ÷ 6 = 2" caption="one apple costs 2 dollars"]]'),
            ("One more, watch. 4 apples cost 20 dollars. 20 divided by 4 equals 5 "
             "— one apple costs 5 dollars.",
             '[[array rows="4" cols="5" view="groups" eq="20 ÷ 4 = 5" caption="one apple costs 5 dollars"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 3 apples cost 9 dollars. 9 "
                        "divided by 3 equals 3 — one costs 3 dollars.",
                        '[[array rows="3" cols="3" view="groups" eq="9 ÷ 3 = 3" caption="one apple costs 3 dollars"]]'),
             "ask": {'a': 8, 'b': 4, 'op': 'rate'}},
            {"worked": ("One more together. 5 apples cost 15 dollars. 15 divided by 5 "
                        "equals 3 — one apple costs 3 dollars.",
                        '[[array rows="5" cols="3" view="groups" eq="15 ÷ 5 = 3" caption="one apple costs 3 dollars"]]'),
             "ask": {'a': 12, 'b': 3, 'op': 'rate'}},
        ],
        "practice_intro": ("Now it's your turn. Share the dollars over the apples. "
                           "Three right answers in a row and we're done — here comes "
                           "the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 6 apples for 12 "
                       "dollars means one apple costs 2. Tap the reason why."),
            "choices": ("because 12 dollars shared over 6 apples is 2 each | because "
                        "12 take away 6 is 6 | because apples usually cost 2 dollars"),
            "answer": "because 12 dollars shared over 6 apples is 2 each",
            "board": '[[array rows="6" cols="2" view="groups" eq="12 ÷ 6 = 2" caption="2 dollars each"]]',
        },
        "recap": [
            ("So, here it is again. What one costs is the whole price shared over "
             "how many — divide. Six apples for twelve dollars is two dollars each.",
             '[[array rows="6" cols="2" view="groups" eq="12 ÷ 6 = 2" caption="12 ÷ 6 = 2 dollars each"]]'),
            ("And it is how you compare two prices honestly.",
             '[[step eq="12 ÷ 6 = 2"]]'),
        ],
        "bank": [{'a': 6, 'b': 2, 'op': 'rate'}, {'a': 10, 'b': 2, 'op': 'rate'}, {'a': 12, 'b': 4, 'op': 'rate'}, {'a': 15, 'b': 3, 'op': 'rate'}, {'a': 16, 'b': 4, 'op': 'rate'}, {'a': 20, 'b': 5, 'op': 'rate'}, {'a': 24, 'b': 6, 'op': 'rate'}, {'a': 28, 'b': 7, 'op': 'rate'}, {'a': 32, 'b': 8, 'op': 'rate'}, {'a': 36, 'b': 9, 'op': 'rate'}],
    },
    {
        # (sy, 2026-09-05) TO THE SHAPE on the RECTANGLE ([[rectangle show="perimeter"]]):
        # the walk around the outside, traced.
        "id": 'basic-u9-perimeter',
        "course": "basic", "unit": 9,
        "topic": 'Perimeter',
        "op": 'peri', "max_value": 60,
        "levels": ("abstract",),
        "symbols": ('perimeter', 'around'),
        "advance_line": "Three in a row, and you can say why — you've got it! You can walk the whole way around.",
        "why": [
            ("How much fence goes around a garden? How much ribbon around a box? "
             "That is perimeter — the distance all the way around a shape — and "
             "it is one of the most-asked questions in building anything.",
             '[[goal text="Perimeter"]]'),
        ],
        "picture": [
            ("Here is a rectangle 5 long and 3 wide. Walk around it: along the top, "
             "5. Down the side, 3. Along the bottom, 5. Up the side, 3. The whole "
             "walk is 5 plus 3 plus 5 plus 3 — 16.",
             '[[rectangle w="5" h="3" show="perimeter" caption="5 + 3 + 5 + 3 = 16"]]'),
        ],
        "teach": [
            ("So for a rectangle, walk all four sides: long, wide, long, wide. Add "
             "them up and that is the perimeter. 5 plus 3 plus 5 plus 3 equals 16.",
             '[[rectangle w="5" h="3" show="perimeter" caption="long, wide, long, wide"]]'),
            ("One more, watch. 6 long and 2 wide: 6 plus 2 plus 6 plus 2 equals 16.",
             '[[rectangle w="6" h="2" show="perimeter" caption="6 + 2 + 6 + 2 = 16"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 4 long and 2 wide. Walk "
                        "around: 4 plus 2 plus 4 plus 2 equals 12.",
                        '[[rectangle w="4" h="2" show="perimeter" caption="4 + 2 + 4 + 2 = 12"]]'),
             "ask": {'a': 5, 'b': 2, 'op': 'peri'}},
            {"worked": ("One more together. 7 long and 3 wide. Walk around: 7 plus 3 "
                        "plus 7 plus 3 equals 20. The perimeter equals 20.",
                        '[[rectangle w="7" h="3" show="perimeter" caption="7 + 3 + 7 + 3 = 20"]]'),
             "ask": {'a': 6, 'b': 4, 'op': 'peri'}},
        ],
        "practice_intro": ("Now it's your turn. Walk the four sides. Three right "
                           "answers in a row and we're done — here comes the first "
                           "one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A rectangle 5 "
                       "long and 3 wide has a perimeter of 16, not 8. Tap the reason "
                       "why."),
            "choices": ("because the walk around has four sides, not two | because "
                        "16 is twice 8 | because 5 and 3 are odd numbers"),
            "answer": "because the walk around has four sides, not two",
            "board": '[[rectangle w="5" h="3" show="perimeter" caption="four sides: 5, 3, 5, 3"]]',
        },
        "recap": [
            ("So, here it is again. Perimeter is the distance all the way around. "
             "For a rectangle, add all four sides — long, wide, long, wide.",
             '[[rectangle w="5" h="3" show="perimeter" caption="5 + 3 + 5 + 3 = 16"]]'),
            ("And it is the fence around the garden, the ribbon around the box.",
             '[[step eq="5 + 3 + 5 + 3 = 16"]]'),
        ],
        "bank": [{'a': 3, 'b': 1, 'op': 'peri'}, {'a': 3, 'b': 2, 'op': 'peri'}, {'a': 4, 'b': 3, 'op': 'peri'}, {'a': 7, 'b': 1, 'op': 'peri'}, {'a': 6, 'b': 3, 'op': 'peri'}, {'a': 7, 'b': 4, 'op': 'peri'}, {'a': 8, 'b': 5, 'op': 'peri'}, {'a': 9, 'b': 6, 'op': 'peri'}, {'a': 10, 'b': 7, 'op': 'peri'}, {'a': 12, 'b': 8, 'op': 'peri'}],
    },
    {
        # (sy, 2026-09-05) TO THE SHAPE on the RECTANGLE ([[rectangle show="area"]]):
        # the squares inside, counted in rows.
        "id": 'basic-u9-area',
        "course": "basic", "unit": 9,
        "topic": 'Area',
        "op": 'area', "max_value": 96,
        "levels": ("abstract",),
        "symbols": ('area', 'inside'),
        "advance_line": "Three in a row, and you can say why — you've got it! You can count the space inside.",
        "why": [
            ("How much carpet covers a floor? How much paint covers a wall? That "
             "is area — the space INSIDE a shape — and we count it in squares, "
             "because squares tile a flat space with no gaps.",
             '[[goal text="Area"]]'),
        ],
        "picture": [
            ("Here is a rectangle 5 long and 3 wide, filled with unit squares. "
             "Count them by rows: 3 rows, 5 squares in each — 5, 10, 15. The area "
             "is 15 squares.",
             '[[rectangle w="5" h="3" show="area" caption="3 rows of 5 = 15 squares"]]'),
        ],
        "teach": [
            ("So for a rectangle, area is the long side times the wide side — the "
             "rows times the squares in a row. 5 times 3 equals 15. The area "
             "equals 15 squares.",
             '[[rectangle w="5" h="3" show="area" caption="5 × 3 = 15 squares"]]'),
            ("One more, watch. 4 long and 2 wide: 2 rows of 4. 4 times 2 equals 8 "
             "squares.",
             '[[rectangle w="4" h="2" show="area" caption="4 × 2 = 8 squares"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 6 long and 2 wide: 2 rows of "
                        "6. 6 times 2 equals 12 squares.",
                        '[[rectangle w="6" h="2" show="area" caption="6 × 2 = 12 squares"]]'),
             "ask": {'a': 3, 'b': 2, 'op': 'area'}},
            {"worked": ("One more together. 7 long and 4 wide. That is 4 rows of 7 "
                        "squares: 7 times 4 equals 28. The area equals 28 squares.",
                        '[[rectangle w="7" h="4" show="area" caption="7 × 4 = 28 squares"]]'),
             "ask": {'a': 5, 'b': 4, 'op': 'area'}},
        ],
        "practice_intro": ("Now it's your turn. Rows times squares in a row. Three "
                           "right answers in a row and we're done — here comes the "
                           "first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Area is long "
                       "times wide, not long plus wide. Tap the reason why."),
            "choices": ("because the inside is rows of squares, and times counts them "
                        "| because times gives a bigger answer | because plus is for "
                        "perimeter only"),
            "answer": "because the inside is rows of squares, and times counts them",
            "board": '[[rectangle w="5" h="3" show="area" caption="3 rows of 5 squares"]]',
        },
        "recap": [
            ("So, here it is again. Area is the space inside, counted in squares: "
             "for a rectangle, long times wide — the rows times the squares in "
             "each row.",
             '[[rectangle w="5" h="3" show="area" caption="5 × 3 = 15 squares"]]'),
            ("And it is the carpet on the floor, the paint on the wall.",
             '[[step eq="5 × 3 = 15 squares"]]'),
        ],
        "bank": [{'a': 5, 'b': 2, 'op': 'area'}, {'a': 4, 'b': 3, 'op': 'area'}, {'a': 6, 'b': 3, 'op': 'area'}, {'a': 7, 'b': 3, 'op': 'area'}, {'a': 6, 'b': 4, 'op': 'area'}, {'a': 8, 'b': 4, 'op': 'area'}, {'a': 9, 'b': 5, 'op': 'area'}, {'a': 8, 'b': 6, 'op': 'area'}, {'a': 9, 'b': 7, 'op': 'area'}, {'a': 12, 'b': 8, 'op': 'area'}],
    },
    {
        # (sq, 2026-09-05) TO THE SHAPE, with the place-value chart ([[placevalue]]):
        # why places exist, the chart before the rule, every example on the chart.
        "id": "basic-u1-place-value-to-1000", "course": "basic", "unit": 1,
        "topic": "Place value: hundreds, tens and ones",
        "op": "pv", "max_value": 999,
        "levels": ("abstract",),
        "symbols": ("hundreds", "ones"),
        "advance_line": ("Three in a row, and you can say why — you've got it! "
                         "You can read hundreds, tens and ones."),
        "why": [
            ("Why do we have places at all? Because counting one at a time stops "
             "working. If a school has 342 students, nobody counts them one by "
             "one. We count in hundreds, then tens, then ones — and three digits "
             "say it all.",
             '[[goal text="Place value: hundreds, tens and ones"]]'),
        ],
        "picture": [
            ("Here is the place-value chart. Three columns: hundreds, tens and "
             "ones. Each column holds its own kind of block. A flat is one "
             "hundred, a rod is one ten, a cube is one. This is 342: three "
             "flats, four rods, two cubes.",
             '[[placevalue n="342" caption="3 flats, 4 rods, 2 cubes — 342"]]'),
        ],
        "teach": [
            ("So a digit means different things in different columns. The 3 in "
             "the hundreds column is three hundred. The 4 in the tens column is "
             "forty. The 2 in the ones column is just two. Read the columns left "
             "to right and you have read the number.",
             '[[step eq="342 = 300 + 40 + 2"]]'),
            ("One more, watch. 5 hundreds, 1 ten and 7 ones. Five flats, one rod, "
             "seven cubes. Five hundred, ten, seven — 517.",
             '[[placevalue n="517" caption="5 hundreds + 1 ten + 7 ones = 517"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 2 hundreds, 6 tens and 3 "
                        "ones. Two flats, six rods, three cubes. Two hundred "
                        "sixty-three — 263.",
                        '[[placevalue n="263" caption="2 hundreds + 6 tens + 3 ones = 263"]]'),
             "ask": {"a": 2, "b": 3, "c": 4, "op": "pv"}},
            {"worked": ("One more together. 7 hundreds, 2 tens and 9 ones. Count "
                        "the blocks in each column — 729.",
                        '[[placevalue n="729" caption="7 hundreds + 2 tens + 9 ones = 729"]]'),
             "ask": {"a": 6, "b": 1, "c": 5, "op": "pv"}},
        ],
        "practice_intro": ("Now it's your turn. Read the blocks in each column. Three "
                           "right answers in a row and we're done — here comes the "
                           "first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. In 342, the 4 "
                       "means forty, not four. Tap the reason why."),
            "choices": ("because it sits in the tens column | because 4 is bigger "
                        "than 2 | because it comes second"),
            "answer": "because it sits in the tens column",
            "board": '[[placevalue n="342" caption="the 4 sits in the tens column"]]',
        },
        "recap": [
            ("So, here it is again. A three-digit number has three columns — "
             "hundreds, tens, ones — and a digit means what its column says: the "
             "3 is three hundred, the 4 is forty, the 2 is two.",
             '[[placevalue n="342" caption="300 + 40 + 2 = 342"]]'),
            ("And places save the counting: three digits tell you three hundred "
             "and forty-two without counting one by one.",
             '[[step eq="342 = 300 + 40 + 2"]]'),
        ],
        "bank": [
            {"a": 1, "b": 1, "c": 2, "op": "pv"}, {"a": 1, "b": 4, "c": 3, "op": "pv"},
            {"a": 2, "b": 2, "c": 5, "op": "pv"}, {"a": 3, "b": 1, "c": 6, "op": "pv"},
            {"a": 3, "b": 5, "c": 2, "op": "pv"}, {"a": 4, "b": 3, "c": 8, "op": "pv"},
            {"a": 5, "b": 6, "c": 1, "op": "pv"}, {"a": 6, "b": 4, "c": 7, "op": "pv"},
            {"a": 7, "b": 8, "c": 3, "op": "pv"}, {"a": 9, "b": 2, "c": 9, "op": "pv"},
        ],
    },
    {
        # (sp, 2026-09-05) THE PROTOTYPE OF THE SHAPE -- Jim's own example. Rebuilt
        # end to end to the seven beats (claude/Design_What_A_Lesson_Is): WHY before
        # any rule, the PICTURE (a number line, on every beat) before the rule, the
        # rule as a summary of what the picture showed, two worked examples drawn on
        # the picture, the walk-back after every right answer, the REASON question
        # after the streak, and the RECAP before the end line. He runs this one and
        # reacts; the rest of the course follows the shape he corrects.
        "id": "basic-u1-rounding-tens", "course": "basic", "unit": 1,
        "topic": "Rounding to the nearest ten",
        "op": "r10", "max_value": 110,
        "levels": ("abstract",),
        "symbols": ("round", "nearest"),
        "advance_line": ("Three in a row, and you can say why — you've got it! "
                         "You can round to the nearest ten."),
        # 1 · WHY -- what rounding is FOR, in the student's world
        "why": [
            ("Rounding is for when the exact number is more accurate than you need. If a "
             "jar has 47 marbles and a friend asks how many, saying about 50 is "
             "easier to say, easier to remember, and close enough.",
             '[[goal text="Rounding to the nearest ten"]]'),
            ("People round all day long. Shops, sports scores, how far away a "
             "place is — about is often all you need. Today we learn to round "
             "to the nearest ten.",
             '[[step eq="47 marbles → about 50"]]'),
        ],
        # 2 · PICTURE -- the number line, before the rule (replayed on a missed reason)
        "picture": [
            ("Here is 47 on a number line, between 40 and 50. Halfway between "
             "them is 45. Look where 47 sits — past the halfway mark, closer "
             "to 50.",
             '[[numberline min="40" max="50" mid="45" points="47" '
             'caption="47 sits past halfway, closer to 50"]]'),
        ],
        # 3 · TEACH -- the idea read off the picture, then the quick rule
        "teach": [
            ("Every number lives between two tens. Rounding just means: hop to "
             "the ten you are closer to. 47 is closer to 50, so 47 rounds to 50.",
             '[[numberline min="40" max="50" mid="45" points="47" hops="47,50" '
             'caption="47 rounds to 50"]]'),
            ("Here is the quick way to tell, in your head. Look at the ones "
             "digit. 4 or smaller, you are below halfway — hop down. 5 or "
             "bigger, you are at halfway or past it — hop up.",
             '[[step eq="ones 0–4 → hop down · ones 5–9 → hop up"]]'),
            # 4 · SHOW -- worked on the picture
            ("Watch me round 32. It sits between 30 and 40. The ones digit is "
             "2 — below halfway — so it hops down. 32 rounds to 30.",
             '[[numberline min="30" max="40" mid="35" points="32" hops="32,30" '
             'caption="32 rounds to 30"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Round 85. It sits "
                        "between 80 and 90, and the ones digit is 5 — right at "
                        "halfway. At halfway we hop up. 85 rounds to 90.",
                        '[[numberline min="80" max="90" mid="85" points="85" '
                        'hops="85,90" caption="85 rounds to 90"]]'),
             "ask": {"a": 74, "op": "r10", "b": 0}},
            {"worked": ("One more together. Round 61. It sits between 60 and 70, "
                        "and the ones digit is 1 — below halfway — so it hops "
                        "down. 61 rounds to 60.",
                        '[[numberline min="60" max="70" mid="65" points="61" '
                        'hops="61,60" caption="61 rounds to 60"]]'),
             "ask": {"a": 58, "op": "r10", "b": 0}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        # 5 · TRY -- after every right answer, the walk-back on the number line
        "show_work_on_correct": True,
        # 6 · SAY IT -- not the answer, the reason (graded in code, never the model)
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 58 rounded "
                       "up to 60. Tap the reason why."),
            "choices": ("because 8 is 5 or bigger | because 58 is a big number | "
                        "because 60 comes after 50"),
            "answer": "because 8 is 5 or bigger",
            "board": ('[[numberline min="50" max="60" mid="55" points="58" '
                      'hops="58,60" caption="58 rounds to 60"]]'),
        },
        # 7 · COME BACK -- the rule and the why, said again before the end line
        "recap": [
            ("So, here it is again. Every number sits between two tens, and "
             "rounding hops to the closer one. Ones digit 4 or smaller hops "
             "down; 5 or bigger hops up.",
             '[[step eq="ones 0–4 → hop down · ones 5–9 → hop up"]]'),
            ("And rounding is for when about is good enough — like about 50 "
             "marbles in the jar.",
             '[[numberline min="40" max="50" mid="45" points="47" hops="47,50" '
             'caption="47 → about 50"]]'),
        ],
        "bank": [
            {"a": 12, "op": "r10", "b": 0}, {"a": 17, "op": "r10", "b": 0},
            {"a": 23, "op": "r10", "b": 0}, {"a": 35, "op": "r10", "b": 0},
            {"a": 41, "op": "r10", "b": 0}, {"a": 49, "op": "r10", "b": 0},
            {"a": 56, "op": "r10", "b": 0}, {"a": 64, "op": "r10", "b": 0},
            {"a": 78, "op": "r10", "b": 0}, {"a": 93, "op": "r10", "b": 0},
        ],
    },
    {
        # (sq, 2026-09-05) TO THE SHAPE: the same number line as the tens lesson,
        # one place over. Every beat draws it.
        "id": "basic-u1-rounding-hundreds", "course": "basic", "unit": 1,
        "topic": "Rounding to the nearest hundred",
        "op": "r100", "max_value": 1000,
        "levels": ("abstract",),
        "symbols": ("round", "nearest"),
        "advance_line": ("Three in a row, and you can say why — you've got it! "
                         "You can round to the nearest hundred."),
        "why": [
            ("Last time we rounded to the nearest ten. Sometimes even that is more "
             "than you need. If a stadium holds 470 people, saying about 500 is "
             "quicker and close enough. Big numbers get rounded to the nearest "
             "hundred.",
             '[[goal text="Rounding to the nearest hundred"]]'),
        ],
        "picture": [
            ("Same number line, bigger steps. Here is 470, between 400 and 500. "
             "Halfway between them is 450. Look where 470 sits — past halfway, "
             "closer to 500.",
             '[[numberline min="400" max="500" mid="450" points="470" '
             'caption="470 sits past halfway, closer to 500"]]'),
        ],
        "teach": [
            ("Every number lives between two hundreds, and rounding hops to the "
             "closer one. 470 is closer to 500, so 470 rounds to 500.",
             '[[numberline min="400" max="500" mid="450" points="470" hops="470,500" '
             'caption="470 rounds to 500"]]'),
            ("The quick way to tell: now the tens digit decides. 4 or smaller, "
             "you are below halfway — hop down. 5 or bigger, at halfway or past "
             "it — hop up.",
             '[[step eq="tens 0–4 → hop down · tens 5–9 → hop up"]]'),
            ("Watch me round 320. It sits between 300 and 400. The tens digit is "
             "2 — below halfway — so it hops down. 320 rounds to 300.",
             '[[numberline min="300" max="400" mid="350" points="320" hops="320,300" '
             'caption="320 rounds to 300"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Round 149. Between 100 "
                        "and 200, and the tens digit is 4 — below halfway. It hops "
                        "down. 149 rounds to 100.",
                        '[[numberline min="100" max="200" mid="150" points="149" '
                        'hops="149,100" caption="149 rounds to 100"]]'),
             "ask": {"a": 253, "op": "r100", "b": 0}},
            {"worked": ("One more together. Round 662. Between 600 and 700; the "
                        "tens digit is 6 — past halfway — so it hops up. 662 rounds "
                        "to 700.",
                        '[[numberline min="600" max="700" mid="650" points="662" '
                        'hops="662,700" caption="662 rounds to 700"]]'),
             "ask": {"a": 578, "op": "r100", "b": 0}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 253 rounded "
                       "up to 300. Tap the reason why."),
            "choices": ("because the tens digit is 5 or bigger | because 253 is a "
                        "big number | because 300 comes after 200"),
            "answer": "because the tens digit is 5 or bigger",
            "board": ('[[numberline min="200" max="300" mid="250" points="253" '
                      'hops="253,300" caption="253 rounds to 300"]]'),
        },
        "recap": [
            ("So, here it is again. Every number sits between two hundreds, and "
             "rounding hops to the closer one. Tens digit 4 or smaller hops "
             "down; 5 or bigger hops up.",
             '[[step eq="tens 0–4 → hop down · tens 5–9 → hop up"]]'),
            ("And it is for when about is good enough — about 500 people in the "
             "stadium.",
             '[[numberline min="400" max="500" mid="450" points="470" hops="470,500" '
             'caption="470 → about 500"]]'),
        ],
        "bank": [
            {"a": 120, "op": "r100", "b": 0}, {"a": 180, "op": "r100", "b": 0},
            {"a": 240, "op": "r100", "b": 0}, {"a": 350, "op": "r100", "b": 0},
            {"a": 430, "op": "r100", "b": 0}, {"a": 490, "op": "r100", "b": 0},
            {"a": 560, "op": "r100", "b": 0}, {"a": 640, "op": "r100", "b": 0},
            {"a": 770, "op": "r100", "b": 0}, {"a": 910, "op": "r100", "b": 0},
        ],
    },
    {
        # (sq, 2026-09-05) TO THE SHAPE, on the COLUMN. Jim's flags 22:35/22:36: the
        # carry and the regrouping were described over a flat line; now every example
        # is a stacked column with the carry above (carries=) or the regrouped digits
        # written over the struck ones (borrows=, new in board.js). The "terrible"
        # teach line is gone; the rule is read off the two columns instead.
        "id": "basic-u1-multi-digit-review", "course": "basic", "unit": 1,
        "topic": "Adding and taking away — review",
        "op": "+", "max_value": 99, "mixed_review": True,
        "levels": ("abstract",),
        "symbols": ("carry", "regroup"),
        "advance_line": ("Three in a row, and you can say why — you've got it! "
                         "Your adding and taking away are ready for bigger things."),
        "why": [
            ("Before we multiply and divide, we warm up adding and taking away "
             "with two-digit numbers. Everything bigger is built on these two "
             "moves — a shop bill, a score, change from a twenty. Get them "
             "quick and the rest comes easy.",
             '[[goal text="Adding and taking away — review"]]'),
        ],
        "picture": [
            ("Here is how the work is set up: the numbers stacked, ones over "
             "ones, tens over tens. 38 plus 24. Ones first: 8 plus 4 equals 12 "
             "— over nine — so the 2 is written and the one ten is carried, up "
             "here, in red. Then the tens: 3 plus 2 plus that 1 equals 6. 62.",
             '[[column terms="38|24" op="+" carries="1_" result="62" '
             'caption="8 + 4 = 12: write 2, carry one ten"]]'),
        ],
        "teach": [
            ("Two moves, and the column shows both. Adding: when the ones add up "
             "to over nine, write the ones digit and carry one ten. Taking away: "
             "when the top ones digit is too small, regroup — one ten becomes ten "
             "ones.",
             '[[step eq="carry: ones over nine"]][[step eq="regroup: ones too small"]]'),
            ("Watch the regrouping. 53 take away 28. 3 is too small to take 8 "
             "away, so one ten comes across: the 5 becomes 4 and the 3 becomes "
             "13 — see them written above, in red. 13 take away 8 equals 5; 4 "
             "take away 2 equals 2. 25.",
             '[[column terms="53|28" op="−" borrows="4|13" result="25" '
             'caption="3 is too small: one ten becomes ten ones"]]'),
        ],
        "pairs": [
            {"worked": ("One more adding, done for you. 46 plus 37. Ones: 6 plus 7 "
                        "equals 13 — over nine — write 3, carry one ten. Tens: 4 "
                        "plus 3 plus 1 equals 8. 83.",
                        '[[column terms="46|37" op="+" carries="1_" result="83" '
                        'caption="6 + 7 = 13: write 3, carry one ten"]]'),
             "ask": {"a": 27, "b": 15, "op": "+"}},
            {"worked": ("And one taking away, together. 62 take away 35. 2 is too "
                        "small — regroup: 6 becomes 5, 2 becomes 12. 12 take away 5 "
                        "equals 7; 5 take away 3 equals 2. 27.",
                        '[[column terms="62|35" op="−" borrows="5|12" result="27" '
                        'caption="2 is too small: one ten becomes ten ones"]]'),
             "ask": {"a": 42, "b": 17, "op": "-"}},
        ],
        "practice_intro": ("Now it's your turn — adds and take-aways, mixed, each one "
                           "on the column. Three right answers in a row and we're "
                           "done."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. In 53 take "
                       "away 28, the 3 became 13. Tap the reason why."),
            # the third wrong reason is THE classic slip -- flipping the digits
            "choices": ("because one ten was regrouped into ten ones | because 13 "
                        "is bigger than 8 | because you take the smaller digit from "
                        "the bigger one"),
            "answer": "because one ten was regrouped into ten ones",
            "board": ('[[column terms="53|28" op="−" borrows="4|13" result="25" '
                      'caption="one ten became ten ones"]]'),
        },
        "recap": [
            ("So, here it is again. Stack the numbers, ones over ones. Adding: "
             "ones over nine, write the digit, carry one ten. Taking away: top "
             "ones too small, regroup one ten into ten ones. The column shows "
             "every move.",
             '[[column terms="38|24" op="+" carries="1_" result="62" '
             'caption="carry"]][[column terms="53|28" op="−" borrows="4|13" result="25" '
             'caption="regroup"]]'),
            ("And these two moves are what every bigger sum is built on.",
             '[[step eq="carry: ones over nine"]][[step eq="regroup: ones too small"]]'),
        ],
        "bank": [
            {"a": 26, "b": 15, "op": "+"}, {"a": 31, "b": 14, "op": "-"},
            {"a": 35, "b": 17, "op": "+"}, {"a": 44, "b": 26, "op": "-"},
            {"a": 46, "b": 18, "op": "+"}, {"a": 52, "b": 35, "op": "-"},
            {"a": 57, "b": 26, "op": "+"}, {"a": 63, "b": 47, "op": "-"},
            {"a": 65, "b": 28, "op": "+"}, {"a": 82, "b": 56, "op": "-"},
        ],
    },
    {
        # (sr, 2026-09-05) TO THE SHAPE on the AREA MODEL ([[areamodel]]): the two-digit
        # number split into tens and ones, each piece its own box, the boxes added.
        "id": "basic-u2-multiply-two-digit", "course": "basic", "unit": 2,
        "topic": "Multiplying bigger numbers",
        "op": "*", "max_value": 300,
        "levels": ("abstract",),
        "symbols": ("times", "tens"),
        "advance_line": ("Three in a row, and you can say why — you've got it! "
                         "You can multiply bigger numbers."),
        "why": [
            ("The times tables stop at nine. But the world does not: 34 tickets at "
             "2 dollars each, 23 rows of 3 chairs. Today we multiply a two-digit "
             "number — and the whole trick is that you already know how, in "
             "pieces.",
             '[[goal text="Multiplying bigger numbers"]]'),
        ],
        "picture": [
            ("Here is 34 times 2 as a picture: a box 34 wide and 2 tall. Cut the 34 "
             "into 30 and 4, and the box splits into two smaller boxes — one 30 by "
             "2, one 4 by 2. The big box is the two small ones put together.",
             '[[areamodel rows="2" cols="30,4" caption="34 × 2 = 30 × 2 + 4 × 2"]]'),
        ],
        "teach": [
            ("So the trick is: split the two-digit number into tens and ones, "
             "multiply each piece, then put the pieces together. 30 times 2 equals "
             "60. 4 times 2 equals 8. 60 plus 8 equals 68.",
             '[[areamodel rows="2" cols="30,4" caption="60 + 8 = 68"]]'
             '[[step eq="34 × 2 = 68"]]'),
            ("One more, watch. 23 times 3. Split 23 into 20 and 3. 20 times 3 "
             "equals 60; 3 times 3 equals 9. 60 plus 9 equals 69.",
             '[[areamodel rows="3" cols="20,3" caption="23 × 3 = 60 + 9 = 69"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 42 times 2. Split 42 into 40 "
                        "and 2. 40 times 2 equals 80; 2 times 2 equals 4. 80 plus 4 "
                        "equals 84.",
                        '[[areamodel rows="2" cols="40,2" caption="42 × 2 = 80 + 4 = 84"]]'),
             "ask": {"a": 43, "b": 2, "op": "*"}},
            {"worked": ("One more together. 31 times 3. Split 31 into 30 and 1. "
                        "30 times 3 equals 90; 1 times 3 equals 3. "
                        "90 plus 3 equals 93.",
                        '[[areamodel rows="3" cols="30,1" caption="31 × 3 = 90 + 3 = 93"]]'),
             "ask": {"a": 32, "b": 3, "op": "*"}},
        ],
        "practice_intro": ("Now it's your turn. Split it, multiply the pieces, put "
                           "them together. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. To find 34 "
                       "times 2, we split 34 into 30 and 4. Tap the reason why."),
            "choices": ("because we know how to multiply each piece | because 30 "
                        "is a rounder number | because 34 is too big to write"),
            "answer": "because we know how to multiply each piece",
            "board": '[[areamodel rows="2" cols="30,4" caption="34 × 2 = 60 + 8 = 68"]]',
        },
        "recap": [
            ("So, here it is again. A two-digit number times a digit: split it into "
             "tens and ones, multiply each piece — those are times table facts you "
             "know — then put the pieces together.",
             '[[areamodel rows="2" cols="30,4" caption="34 × 2 = 60 + 8 = 68"]]'),
            ("And that is how the times tables reach past nine — in pieces.",
             '[[step eq="34 × 2 = 30 × 2 + 4 × 2 = 68"]]'),
        ],
        "bank": [
            {"a": 12, "b": 2, "op": "*"}, {"a": 13, "b": 3, "op": "*"},
            {"a": 24, "b": 2, "op": "*"}, {"a": 21, "b": 3, "op": "*"},
            {"a": 23, "b": 4, "op": "*"}, {"a": 34, "b": 3, "op": "*"},
            {"a": 42, "b": 3, "op": "*"}, {"a": 33, "b": 5, "op": "*"},
            {"a": 45, "b": 4, "op": "*"}, {"a": 62, "b": 4, "op": "*"},
        ],
    },
    {
        # (ss, 2026-09-05) TO THE SHAPE on the AREA MODEL backwards: the two-digit
        # number split into tens and ones, each piece shared out.
        "id": "basic-u3-divide-two-digit", "course": "basic", "unit": 3,
        "topic": "Dividing bigger numbers",
        "op": "/", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("divided", "split"),
        "advance_line": ("Three in a row, and you can say why — you've got it! "
                         "You can divide bigger numbers."),
        "why": [
            ("Sharing 12 into 3 is a times table fact turned around. But 84 into 4? "
             "No times table goes that far. Today we divide a two-digit number — "
             "and the trick is the one multiplying used: you already know how, in "
             "pieces.",
             '[[goal text="Dividing bigger numbers"]]'),
        ],
        "picture": [
            ("Here is 84 divided by 4 as a picture. A box 4 tall holding 84. Cut "
             "the 84 into 80 and 4, and the box splits in two: 80 shared by 4 is "
             "20 across, and 4 shared by 4 is 1 across. Side by side, 21.",
             '[[areamodel rows="4" cols="20,1" caption="84 ÷ 4: 80 ÷ 4 = 20, 4 ÷ 4 = 1"]]'),
        ],
        "teach": [
            ("So the trick is: split the number into friendly pieces — tens and "
             "ones — divide each piece, then put the answers together. 80 divided "
             "by 4 equals 20. 4 divided by 4 equals 1. 20 plus 1 equals 21.",
             '[[areamodel rows="4" cols="20,1" caption="84 ÷ 4 = 20 + 1 = 21"]]'
             '[[step eq="84 ÷ 4 = 21"]]'),
            ("One more, watch. 69 divided by 3. Split 69 into 60 and 9. 60 divided "
             "by 3 equals 20; 9 divided by 3 equals 3. 20 plus 3 equals 23.",
             '[[areamodel rows="3" cols="20,3" caption="69 ÷ 3 = 20 + 3 = 23"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 48 divided by 2. Split 48 "
                        "into 40 and 8. 40 divided by 2 equals 20; 8 divided by 2 "
                        "equals 4. 20 plus 4 equals 24.",
                        '[[areamodel rows="2" cols="20,4" caption="48 ÷ 2 = 20 + 4 = 24"]]'),
             "ask": {"a": 46, "b": 2, "op": "/"}},
            {"worked": ("One more together. 96 divided by 3. Split 96 into 90 and 6. "
                        "90 divided by 3 equals 30; 6 divided by 3 equals 2. "
                        "30 plus 2 equals 32.",
                        '[[areamodel rows="3" cols="30,2" caption="96 ÷ 3 = 30 + 2 = 32"]]'),
             "ask": {"a": 93, "b": 3, "op": "/"}},
        ],
        "practice_intro": ("Now it's your turn. Split it, divide the pieces, put them "
                           "together. Three right answers in a row and we're done — "
                           "here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. To find 84 "
                       "divided by 4, we split 84 into 80 and 4. Tap the reason why."),
            "choices": ("because we know how to divide each piece | because 80 is "
                        "a rounder number | because 84 is too big to share"),
            "answer": "because we know how to divide each piece",
            "board": '[[areamodel rows="4" cols="20,1" caption="84 ÷ 4 = 20 + 1 = 21"]]',
        },
        "recap": [
            ("So, here it is again. A two-digit number divided by a digit: split it "
             "into tens and ones, divide each piece — those are facts you know — "
             "then put the answers together.",
             '[[areamodel rows="4" cols="20,1" caption="84 ÷ 4 = 20 + 1 = 21"]]'),
            ("And that is how dividing reaches past the times tables — in pieces, "
             "the same way multiplying did.",
             '[[step eq="84 ÷ 4 = 80 ÷ 4 + 4 ÷ 4 = 21"]]'),
        ],
        "bank": [
            {"a": 22, "b": 2, "op": "/"}, {"a": 26, "b": 2, "op": "/"},
            {"a": 33, "b": 3, "op": "/"}, {"a": 39, "b": 3, "op": "/"},
            {"a": 44, "b": 4, "op": "/"}, {"a": 48, "b": 4, "op": "/"},
            {"a": 55, "b": 5, "op": "/"}, {"a": 63, "b": 3, "op": "/"},
            {"a": 66, "b": 2, "op": "/"}, {"a": 88, "b": 4, "op": "/"},
        ],
    },
    {
        # (su, 2026-09-05) TO THE SHAPE on the FRACTION LINE ([[numberline denom=]]):
        # the line from 0 to 1 cut into equal hops, labelled in fourths, the hops drawn.
        "id": "basic-u5-fractions-on-the-number-line", "course": "basic", "unit": 5,
        "topic": "Fractions live on the number line",
        "op": "nl", "max_value": 12,
        "levels": ("abstract",),
        "symbols": ("hop", "line"),
        "advance_line": ("Three in a row, and you can say why — you've got it! "
                         "A fraction is a number with its own home on the line."),
        "why": [
            ("A fraction is not just a piece of pizza. A fraction is a NUMBER — it "
             "can be bigger or smaller than another, it has a place in order, and "
             "every number has a home on the number line. Once you can see where a "
             "fraction lives, comparing and adding fractions stop being a mystery.",
             '[[goal text="Fractions live on the number line"]]'),
        ],
        "picture": [
            ("Here is the line from 0 to 1, cut into 4 equal hops. Each hop is one "
             "fourth. Hop once from 0 and you stand on 1 out of 4. Hop three times "
             "and you stand on 3 out of 4 — there it is, with its own home.",
             '[[numberline min="0" max="1" denom="4" hops="0,0.25,0.5,0.75" points="0.75" caption="3 hops land on 3/4"]]'),
        ],
        "teach": [
            ("So the bottom number says how many equal hops the line from 0 to 1 "
             "is cut into, and the top number says how many hops to take. 3 out "
             "of 4: four hops to a whole, take three.",
             '[[numberline min="0" max="1" denom="4" hops="0,0.25,0.5,0.75" points="0.75" caption="bottom: 4 hops to 1 · top: take 3"]]'),
            ("And if you take ALL 4 hops, you reach 1 whole. Four fourths equals "
             "one — the top and bottom the same means the whole line.",
             '[[numberline min="0" max="1" denom="4" hops="0,0.25,0.5,0.75,1" points="1" caption="4 hops → 4/4 = 1"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Cut the line into 3 equal "
                        "hops. 2 hops from 0 land on 2 out of 3.",
                        '[[numberline min="0" max="1" denom="3" hops="0,0.3333,0.6667" points="0.6667" caption="2 hops land on 2/3"]]'),
             "ask": {"a": 2, "b": 5, "op": "nl"}},
            {"worked": ("One more together. Cut the line into 6 equal hops. Reaching "
                        "1 whole takes all 6 hops — six sixths equals one.",
                        '[[numberline min="0" max="1" denom="6" hops="0,0.1667,0.3333,0.5,0.6667,0.8333,1" points="1" caption="all 6 hops reach 1"]]'),
             "ask": {"a": 1, "b": 8, "op": "nlw"}},
        ],
        "practice_intro": ("Now it's your turn. Count the hops on the line. Three "
                           "right answers in a row and we're done — here comes the "
                           "first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 3 out of 4 "
                       "lives 3 hops from 0 on a line cut into 4. Tap the reason why."),
            "choices": ("because the bottom cuts the line into 4, the top takes 3 "
                        "| because 3 is smaller than 4 | because 3 out of 4 is nearly "
                        "a whole"),
            "answer": "because the bottom cuts the line into 4, the top takes 3",
            "board": '[[numberline min="0" max="1" denom="4" hops="0,0.25,0.5,0.75" points="0.75" caption="4 hops to 1, take 3"]]',
        },
        "recap": [
            ("So, here it is again. A fraction is a number on the line: the bottom "
             "cuts 0 to 1 into equal hops, the top says how many hops to take, and "
             "top equals bottom means the whole line.",
             '[[numberline min="0" max="1" denom="4" hops="0,0.25,0.5,0.75,1" points="0.75,1" caption="3/4 and 4/4 = 1"]]'),
            ("And once you can see where a fraction lives, comparing and adding "
             "fractions stop being a mystery.",
             '[[step eq="3/4 → 3 hops of 1/4"]]'),
        ],
        "bank": [
            {"a": 1, "b": 2, "op": "nl"}, {"a": 1, "b": 3, "op": "nl"},
            {"a": 2, "b": 3, "op": "nl"}, {"a": 1, "b": 3, "op": "nlw"},
            {"a": 3, "b": 4, "op": "nl"}, {"a": 1, "b": 5, "op": "nlw"},
            {"a": 4, "b": 5, "op": "nl"}, {"a": 5, "b": 6, "op": "nl"},
            {"a": 1, "b": 8, "op": "nl"}, {"a": 1, "b": 10, "op": "nlw"},
        ],
    },
    {
        # (ss, 2026-09-05) TO THE SHAPE: the two pictures side by side -- groups put
        # together (times) and a total shared out (divided by). The picture is how a
        # student tells which one the story is asking for.
        "id": "basic-u3-story-problems", "course": "basic", "unit": 3,
        "topic": "Story problems — multiplying and dividing",
        "op": "*", "max_value": 40, "mixed_review": True,
        "levels": ("abstract",),
        "symbols": ("times", "divided"),
        "advance_line": ("Three in a row, and you can say why — you've got it! "
                         "You can solve multiplying and dividing story problems."),
        "why": [
            ("Nobody hands you a times sign in real life. They hand you a story: "
             "three boxes of crayons, twelve cookies for three friends. The skill "
             "is hearing which picture the story is — groups put together, or a "
             "pile shared out — and that tells you whether it is times or "
             "divided by.",
             '[[goal text="Story problems — multiplying and dividing"]]'),
        ],
        "picture": [
            ("Here are the two pictures. Equal groups put together: 4 crayons in "
             "each of 3 boxes — that is times. A pile shared into equal groups: 12 "
             "cookies into 3 bags — that is divided by. Same dots; the story "
             "decides which way you read them.",
             '[[array rows="3" cols="4" view="groups" caption="3 boxes of 4 — times"]]'
             '[[array total="12" rows="3" ask="1" caption="12 shared into 3 bags — divided by"]]'),
        ],
        "teach": [
            ("Listen. Each box holds 4 crayons. There are 3 boxes. Equal boxes put "
             "together — that is times. Four times three equals twelve crayons in "
             "all.",
             '[[array rows="3" cols="4" view="groups" caption="3 boxes of 4 = 12 crayons"]]'),
            ("Listen. 12 cookies are shared into 3 equal bags. A pile shared out — "
             "that is divided by. Twelve divided by three equals four cookies in "
             "each bag.",
             '[[array rows="3" cols="4" view="groups" eq="12 ÷ 3 = 4" caption="12 cookies into 3 bags: 4 each"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Each pack holds 5 pencils. "
                        "There are 2 packs. Groups put together — times. Five times "
                        "two equals ten pencils in all.",
                        '[[array rows="2" cols="5" view="groups" caption="2 packs of 5 = 10 pencils"]]'),
             "ask": {"a": 2, "b": 5, "op": "*",
                     "story": ("Each jar holds 2 marbles. There are 5 jars. How "
                               "many marbles in all?")}},
            {"worked": ("One more together. 10 apples are shared into 2 equal "
                        "baskets. A pile shared out — divided by. Ten divided by two "
                        "equals five apples in each basket.",
                        '[[array rows="2" cols="5" view="groups" eq="10 ÷ 2 = 5" caption="10 apples into 2 baskets: 5 each"]]'),
             "ask": {"a": 12, "b": 4, "op": "/",
                     "story": ("12 grapes are shared into 4 equal bowls. How "
                               "many grapes go in each bowl?")}},
        ],
        "practice_intro": ("Now it's your turn. Ask yourself: groups put together, or "
                           "a pile shared out? Three right answers in a row and "
                           "we're done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Twelve cookies "
                       "shared into 3 bags is divided by, not times. Tap the reason "
                       "why."),
            "choices": ("because a pile is being shared out into equal groups | "
                        "because 12 is bigger than 3 | because cookies are always "
                        "divided"),
            "answer": "because a pile is being shared out into equal groups",
            "board": '[[array total="12" rows="3" ask="1" caption="a pile shared out — divided by"]]',
        },
        "recap": [
            ("So, here it is again. Equal groups put together — times. A pile "
             "shared into equal groups — divided by. Hear which picture the story "
             "is, and the sign follows.",
             '[[array rows="3" cols="4" view="groups" caption="groups put together — times"]]'
             '[[array total="12" rows="3" ask="1" caption="a pile shared out — divided by"]]'),
            ("And that is the skill real life actually asks for.",
             '[[step eq="4 × 3 = 12 · 12 ÷ 3 = 4"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "op": "*",
             "story": ("Each cup holds 2 straws. There are 3 cups. How many "
                       "straws in all?")},
            {"a": 6, "b": 2, "op": "/",
             "story": ("6 socks are shared into 2 equal drawers. How many socks "
                       "go in each drawer?")},
            {"a": 4, "b": 2, "op": "*",
             "story": ("Each bag holds 4 buns. There are 2 bags. How many buns "
                       "in all?")},
            {"a": 8, "b": 4, "op": "/",
             "story": ("8 fish are shared into 4 equal tanks. How many fish "
                       "swim in each tank?")},
            {"a": 5, "b": 3, "op": "*",
             "story": ("Each row has 5 chairs. There are 3 rows. How many "
                       "chairs in all?")},
            {"a": 15, "b": 3, "op": "/",
             "story": ("15 stickers are shared into 3 equal sheets. How many "
                       "stickers go on each sheet?")},
            {"a": 6, "b": 4, "op": "*",
             "story": ("Each tray holds 6 eggs. There are 4 trays. How many "
                       "eggs in all?")},
            {"a": 20, "b": 5, "op": "/",
             "story": ("20 beads are shared into 5 equal strings. How many "
                       "beads go on each string?")},
            {"a": 7, "b": 3, "op": "*",
             "story": ("Each shelf holds 7 books. There are 3 shelves. How many "
                       "books in all?")},
            {"a": 30, "b": 6, "op": "/",
             "story": ("30 seeds are shared into 6 equal pots. How many seeds "
                       "go in each pot?")},
        ],
    },
    {
        # (st, 2026-09-05) TO THE SHAPE on TWO NUMBER LINES: count-by hops on each,
        # the first landing they share marked.
        "id": "basic-u4-least-common-multiple", "course": "basic", "unit": 4,
        "topic": "Least common multiple",
        "op": "lcm", "max_value": 60,
        "levels": ("abstract",),
        "symbols": ("multiple", "least"),
        "advance_line": ("Three in a row, and you can say why — you've got it! "
                         "You can find the least common multiple."),
        "why": [
            ("A multiple of a number is what you land on when you count by it — "
             "the multiples of 3 are 3, 6, 9, 12, and so on. Two numbers sometimes "
             "land on the same spot. One bus every 2 minutes, another every 3: "
             "when do they arrive together? That question is today's lesson.",
             '[[goal text="Least common multiple"]]'),
        ],
        "picture": [
            ("Here are two number lines. On the top one, hop by 2: 2, 4, 6. On the "
             "bottom one, hop by 3: 3, 6. Look where both hops land on the same "
             "number for the first time — 6.",
             '[[numberline min="0" max="6" hops="0,2,4,6" points="6" caption="count by 2 — lands on 6"]]'
             '[[numberline min="0" max="6" hops="0,3,6" points="6" caption="count by 3 — lands on 6"]]'),
        ],
        "teach": [
            ("That is the least common multiple: the smallest number in BOTH "
             "count-by lists — the first spot both sets of hops land on. For 2 "
             "and 3, it is 6.",
             '[[step eq="2: 2, 4, 6"]][[step eq="3: 3, 6"]]'
             '[[step eq="LCM of 2 and 3 = 6"]]'),
            ("One more, watch. 4 and 6. Hop by 4: 4, 8, 12. Hop by 6: 6, 12. The "
             "first shared landing is 12. The least common multiple of 4 and 6 "
             "equals 12.",
             '[[numberline min="0" max="12" hops="0,4,8,12" points="12" caption="count by 4 — lands on 12"]]'
             '[[numberline min="0" max="12" hops="0,6,12" points="12" caption="count by 6 — lands on 12"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 3 and 6. Hop by 3: 3, 6. Hop "
                        "by 6: 6. The first shared landing is 6 — the least common "
                        "multiple of 3 and 6 equals 6.",
                        '[[numberline min="0" max="6" hops="0,3,6" points="6" caption="count by 3 — lands on 6"]]'
                        '[[numberline min="0" max="6" hops="0,6" points="6" caption="count by 6 — lands on 6"]]'),
             "ask": {"a": 2, "b": 6, "op": "lcm"}},
            {"worked": ("One more together. 2 and 5. Hop by 2: 2, 4, 6, 8, 10. Hop "
                        "by 5: 5, 10. The first shared landing is 10.",
                        '[[numberline min="0" max="10" hops="0,2,4,6,8,10" points="10" caption="count by 2 — lands on 10"]]'
                        '[[numberline min="0" max="10" hops="0,5,10" points="10" caption="count by 5 — lands on 10"]]'),
             "ask": {"a": 4, "b": 5, "op": "lcm"}},
        ],
        "practice_intro": ("Now it's your turn. Count by each number until they "
                           "meet. Three right answers in a row and we're done — "
                           "here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The least "
                       "common multiple of 2 and 3 is 6, not 12. Tap the reason why."),
            "choices": ("because 6 is the first number both counts land on | "
                        "because 12 is too big | because 2 and 3 and 1 add up to 6"),
            "answer": "because 6 is the first number both counts land on",
            "board": ('[[numberline min="0" max="12" hops="0,2,4,6,8,10,12" points="6,12" caption="count by 2 lands on 6 and on 12"]]'
                      '[[numberline min="0" max="12" hops="0,3,6,9,12" points="6,12" caption="count by 3 lands on 6 first"]]'),
        },
        "recap": [
            ("So, here it is again. Count by each number — hop along the line — "
             "and the least common multiple is the first spot both sets of hops "
             "land on.",
             '[[numberline min="0" max="6" hops="0,2,4,6" points="6" caption="count by 2"]]'
             '[[numberline min="0" max="6" hops="0,3,6" points="6" caption="count by 3 — they meet at 6"]]'),
            ("And it is for anything that repeats on two different beats — finding "
             "the moment they line up.",
             '[[step eq="LCM of 2 and 3 = 6"]]'),
        ],
        "bank": [
            {"a": 2, "b": 4, "op": "lcm"}, {"a": 3, "b": 2, "op": "lcm"},
            {"a": 6, "b": 6, "op": "lcm"}, {"a": 2, "b": 10, "op": "lcm"},
            {"a": 3, "b": 4, "op": "lcm"}, {"a": 4, "b": 3, "op": "lcm"},
            {"a": 2, "b": 7, "op": "lcm"}, {"a": 3, "b": 5, "op": "lcm"},
            {"a": 4, "b": 10, "op": "lcm"}, {"a": 3, "b": 8, "op": "lcm"},
            {"a": 5, "b": 6, "op": "lcm"},
        ],
    },
    {
        # (sv, 2026-09-05) TO THE SHAPE on the FRACTION LINE cut the FINER way: one
        # half found on a line of fourths, then the hop.
        "id": "basic-u6-add-fractions-different-bottoms", "course": "basic",
        "unit": 6,
        "topic": "Adding fractions with different bottoms",
        "op": "fu", "max_value": 12,
        "levels": ("abstract",),
        "symbols": ("bottoms", "plus"),
        "advance_line": ("Three in a row, and you can say why — you've got it! "
                         "You can add fractions with different bottoms."),
        "why": [
            ("Half a pizza plus a fourth of a pizza — how much pizza? You cannot "
             "count halves and fourths together; they are different-sized pieces. "
             "So first you rename one fraction until both bottoms match. Then it is "
             "the same counting as before.",
             '[[goal text="Adding fractions with different bottoms"]]'),
        ],
        "picture": [
            ("Here is a line cut into fourths. Where does one half sit on it? At "
             "two fourths — the same spot, with a new name. Now hop one more "
             "fourth. Three fourths.",
             '[[numberline min="0" max="1" denom="4" hops="0,0.5,0.75" points="0.75" caption="1/2 = 2/4, then + 1/4 = 3/4"]]'),
        ],
        "teach": [
            ("So the trick is: change one fraction so both bottoms match, then add "
             "the tops. One half equals two fourths. Two fourths plus one fourth "
             "equals three fourths.",
             '[[step eq="1/2 = 2/4"]][[numberline min="0" max="1" denom="4" hops="0,0.5,0.75" points="0.75" caption="2/4 + 1/4 = 3/4"]]'),
            ("One more, watch. One third plus two sixths. On a line of sixths, one "
             "third sits at two sixths. Hop two more: four sixths.",
             '[[numberline min="0" max="1" denom="6" hops="0,0.3333,0.6667" points="0.6667" caption="1/3 = 2/6, then + 2/6 = 4/6"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. One half plus one sixth. On "
                        "a line of sixths, one half sits at three sixths. Hop one "
                        "more: four sixths.",
                        '[[numberline min="0" max="1" denom="6" hops="0,0.5,0.6667" points="0.6667" caption="1/2 = 3/6, then + 1/6 = 4/6"]]'),
             "ask": {"a": 1, "b": 2, "c": 4, "op": "fu"}},
            {"worked": ("One more together. One fourth plus one eighth. On a line of "
                        "eighths, one fourth sits at two eighths. Hop one more: "
                        "three eighths.",
                        '[[numberline min="0" max="1" denom="8" hops="0,0.25,0.375" points="0.375" caption="1/4 = 2/8, then + 1/8 = 3/8"]]'),
             "ask": {"a": 1, "b": 3, "c": 6, "op": "fu"}},
        ],
        "practice_intro": ("Now it's your turn. Find the first fraction on the finer "
                           "line, then hop. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. To add one half "
                       "and one fourth, we first write one half as two fourths. Tap "
                       "the reason why."),
            "choices": ("because you can only count pieces that are the same size | "
                        "because fourths are smaller than halves | because 2 plus 4 "
                        "makes 6"),
            "answer": "because you can only count pieces that are the same size",
            "board": '[[numberline min="0" max="1" denom="4" hops="0,0.5,0.75" points="0.75" caption="both in fourths first"]]',
        },
        "recap": [
            ("So, here it is again. Different bottoms mean different-sized pieces: "
             "rename one fraction until the bottoms match, then add the tops. On "
             "the line, find the first fraction on the finer line, then hop.",
             '[[numberline min="0" max="1" denom="4" hops="0,0.5,0.75" points="0.75" caption="1/2 + 1/4 = 3/4"]]'),
            ("And it is for every time the pieces do not match — which is most of "
             "the time.",
             '[[step eq="1/2 + 1/4 = 2/4 + 1/4 = 3/4"]]'),
        ],
        "bank": [
            {"a": 1, "b": 2, "c": 6, "op": "fu"},
            {"a": 2, "b": 3, "c": 6, "op": "fu"},
            {"a": 1, "b": 2, "c": 8, "op": "fu"},
            {"a": 3, "b": 2, "c": 8, "op": "fu"},
            {"a": 1, "b": 4, "c": 8, "op": "fu"},
            {"a": 5, "b": 4, "c": 8, "op": "fu"},
            {"a": 2, "b": 2, "c": 10, "op": "fu"},
            {"a": 3, "b": 5, "c": 10, "op": "fu"},
            {"a": 4, "b": 2, "c": 12, "op": "fu"},
            {"a": 5, "b": 3, "c": 12, "op": "fu"},
            {"a": 2, "b": 4, "c": 12, "op": "fu"},
            {"a": 7, "b": 6, "c": 12, "op": "fu"},
        ],
    },
    {
        # (sw, 2026-09-05) TO THE SHAPE on the HUNDREDTHS SQUARE ([[hundredgrid]]).
        "id": "basic-u7-hundredths", "course": "basic", "unit": 7,
        "topic": "Hundredths",
        "op": "dh", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("hundredths", "plus"),
        "advance_line": ("Three in a row, and you can say why — you've got it! "
                         "You know your hundredths."),
        "why": [
            ("Tenths are not always fine enough. A price is 3 dollars and 25 cents "
             "— that 25 is hundredths of a dollar. A hundredth is one out of one "
             "hundred equal pieces, and we write hundredths after the point: 0.25 "
             "is 25 hundredths.",
             '[[goal text="Hundredths"]]'),
        ],
        "picture": [
            ("Here is a whole cut into a hundred equal cells — ten rows of ten. "
             "Shade 25 of them: two full rows and five more. That is 25 "
             "hundredths, 0.25.",
             '[[hundredgrid shaded="25" caption="25 hundredths = 0.25"]]'),
        ],
        "teach": [
            ("Adding hundredths is counting cells. 25 hundredths, then 13 more in "
             "red: 25 plus 13 equals 38. 25 hundredths plus 13 hundredths equals 38 "
             "hundredths — 0.38.",
             '[[hundredgrid shaded="25" plus="13" caption="0.25 + 0.13 = 0.38"]]'),
            ("One more, watch. 40 hundredths — four full rows — plus 22 hundredths. "
             "40 plus 22 equals 62. 0.62.",
             '[[hundredgrid shaded="40" plus="22" caption="0.40 + 0.22 = 0.62"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 31 hundredths plus 24 "
                        "hundredths. Count the cells: 31 plus 24 equals 55. 55 "
                        "hundredths — 0.55.",
                        '[[hundredgrid shaded="31" plus="24" caption="0.31 + 0.24 = 0.55"]]'),
             "ask": {"a": 11, "b": 12, "op": "dh"}},
            {"worked": ("One more together. 26 hundredths plus 32 hundredths. 26 plus "
                        "32 equals 58. 58 hundredths — 0.58.",
                        '[[hundredgrid shaded="26" plus="32" caption="0.26 + 0.32 = 0.58"]]'),
             "ask": {"a": 22, "b": 15, "op": "dh"}},
        ],
        "practice_intro": ("Now it's your turn. Count the cells if you need to. "
                           "Three right answers in a row and we're done — here comes "
                           "the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 0.25 plus 0.13 "
                       "is 0.38, added like whole numbers. Tap the reason why."),
            "choices": ("because both are counts of the same-sized cell, a hundredth "
                        "| because the point does not matter | because 25 and 13 "
                        "are both small"),
            "answer": "because both are counts of the same-sized cell, a hundredth",
            "board": '[[hundredgrid shaded="25" plus="13" caption="same-sized cells, so just count"]]',
        },
        "recap": [
            ("So, here it is again. A hundredth is one cell of a hundred, written "
             "two places after the point. Adding hundredths is counting cells — "
             "add the counts, and the point stays put.",
             '[[hundredgrid shaded="25" plus="13" caption="0.25 + 0.13 = 0.38"]]'),
            ("And hundredths are how money writes its cents.",
             '[[step eq="0.25 + 0.13 = 0.38"]]'),
        ],
        "bank": [
            {"a": 12, "b": 13, "op": "dh"}, {"a": 21, "b": 14, "op": "dh"},
            {"a": 23, "b": 22, "op": "dh"}, {"a": 30, "b": 25, "op": "dh"},
            {"a": 42, "b": 23, "op": "dh"}, {"a": 34, "b": 37, "op": "dh"},
            {"a": 44, "b": 31, "op": "dh"}, {"a": 52, "b": 33, "op": "dh"},
            {"a": 63, "b": 27, "op": "dh"}, {"a": 61, "b": 34, "op": "dh"},
        ],
    },
    {
        # (sy, 2026-09-05) TO THE SHAPE on the CIRCLE cut into four ([[pie parts="4"]]):
        # the turned quarters shaded, 90 degrees each.
        "id": "basic-u9-quarter-turns", "course": "basic", "unit": 9,
        "topic": "Quarter turns and degrees",
        "op": "ang", "max_value": 360,
        "levels": ("abstract",),
        "symbols": ("degrees", "turn"),
        "advance_line": ("Three in a row, and you can say why — you've got it! "
                         "You know your quarter turns."),
        "why": [
            ("Turn to face the door. Turn all the way around. How do you say how "
             "much you turned? We measure turning in degrees, and the whole idea "
             "rests on one picture: a circle cut into four quarters, 90 degrees "
             "each.",
             '[[goal text="Quarter turns and degrees"]]'),
        ],
        "picture": [
            ("Here is the circle cut into four quarters. One quarter turn is 90 "
             "degrees. Two quarters shaded — two quarter turns — is 180 degrees, "
             "half the way around. Four quarters is all the way round: 360.",
             '[[pie parts="4" shaded="2" caption="2 quarter turns = 180°"]]'),
        ],
        "teach": [
            ("So there are 90 degrees in one quarter turn, and you count by 90 for "
             "each quarter. 2 quarter turns: 2 times 90 equals 180 — so 2 quarter "
             "turns equals 180 degrees.",
             '[[pie parts="4" shaded="2" caption="2 × 90° = 180°"]]'),
            ("And backwards, watch. 270 degrees. How many quarter turns? Count by "
             "90: 90, 180, 270 — three counts. 270 degrees equals 3 quarter turns.",
             '[[pie parts="4" shaded="3" caption="270° = 3 quarter turns"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 3 quarter turns. Three "
                        "quarters of the circle: 3 times 90 equals 270 degrees.",
                        '[[pie parts="4" shaded="3" caption="3 × 90° = 270°"]]'),
             "ask": {"a": 4, "b": 0, "op": "ang"}},
            {"worked": ("One more together. 180 degrees. Count by 90: 90, 180 — two "
                        "counts. 180 degrees equals 2 quarter turns — half the "
                        "circle.",
                        '[[pie parts="4" shaded="2" caption="180° = 2 quarter turns"]]'),
             "ask": {"a": 360, "b": 0, "op": "angq"}},
        ],
        "practice_intro": ("Now it's your turn. Count the quarters, 90 each. Three "
                           "right answers in a row and we're done — here comes the "
                           "first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Two quarter "
                       "turns is 180 degrees. Tap the reason why."),
            "choices": ("because each quarter is 90 degrees, and two of them make 180 "
                        "| because 180 is half of 360 | because two turns is always 180"),
            "answer": "because each quarter is 90 degrees, and two of them make 180",
            "board": '[[pie parts="4" shaded="2" caption="90° + 90° = 180°"]]',
        },
        "recap": [
            ("So, here it is again. A circle is four quarter turns of 90 degrees "
             "each: count by 90 to go from turns to degrees, and count by 90 to go "
             "back.",
             '[[pie parts="4" shaded="4" caption="4 × 90° = 360° — all the way round"]]'),
            ("And it is how we say how far anything has turned — a door, a dial, "
             "you.",
             '[[step eq="1 quarter turn = 90°"]]'),
        ],
        "bank": [
            {"a": 1, "b": 0, "op": "ang"}, {"a": 90, "b": 0, "op": "angq"},
            {"a": 2, "b": 0, "op": "ang"}, {"a": 180, "b": 0, "op": "angq"},
            {"a": 3, "b": 0, "op": "ang"}, {"a": 270, "b": 0, "op": "angq"},
        ],
    },
    {
        # (sy, 2026-09-05) TO THE SHAPE: the box ([[solid kind="prism"]]) and one layer
        # of it as an array, times the layers.
        "id": "basic-u9-volume", "course": "basic", "unit": 9,
        "topic": "Volume — counting cubes",
        "op": "vol", "max_value": 96,
        "levels": ("abstract",),
        "symbols": ("times", "cubes"),
        "advance_line": ("Three in a row, and you can say why — you've got it! "
                         "You can count the cubes that fill a box."),
        "why": [
            ("How much fits in a box? How much water fills a tank? That is "
             "volume — the space inside something solid — and we count it in "
             "cubes, the way area was counted in squares.",
             '[[goal text="Volume — counting cubes"]]'),
        ],
        "picture": [
            ("Here is a box 3 cubes long, 2 cubes wide and 2 cubes tall. Look at "
             "the bottom layer on its own: 2 rows of 3 cubes — 6 cubes. The box "
             "holds 2 such layers. 6 and 6: 12 cubes.",
             '[[array rows="2" cols="3" caption="one layer: 3 × 2 = 6 cubes"]][[solid kind="prism" w="3" d="2" h="2" caption="2 layers: 6 × 2 = 12 cubes"]]'),
        ],
        "teach": [
            ("So volume is: count the cubes in one layer, then count the layers. "
             "One layer holds 3 times 2 equals 6 cubes. There are 2 layers. 6 "
             "times 2 equals 12 cubes.",
             '[[step eq="3 × 2 = 6"]][[step eq="6 × 2 = 12 cubes"]][[solid kind="prism" w="3" d="2" h="2" caption="3 × 2 × 2 = 12 cubes"]]'),
            ("One more, watch. 4 cubes long, 2 wide, 2 tall. 4 times 2 equals 8 in "
             "a layer. 8 times 2 equals 16 cubes.",
             '[[array rows="2" cols="4" caption="one layer: 4 × 2 = 8 cubes"]][[solid kind="prism" w="4" d="2" h="2" caption="2 layers: 8 × 2 = 16 cubes"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 2 long, 2 wide, 3 tall. One "
                        "layer: 2 times 2 equals 4. Three layers: 4 times 3 equals 12 "
                        "cubes.",
                        '[[array rows="2" cols="2" caption="one layer: 2 × 2 = 4 cubes"]][[solid kind="prism" w="2" d="2" h="3" caption="3 layers: 4 × 3 = 12 cubes"]]'),
             "ask": {"a": 3, "b": 3, "c": 1, "op": "vol"}},
            {"worked": ("One more together. 5 long, 2 wide, 2 tall. One layer: 5 "
                        "times 2 equals 10. Two layers: 10 times 2 equals 20 cubes.",
                        '[[array rows="2" cols="5" caption="one layer: 5 × 2 = 10 cubes"]][[solid kind="prism" w="5" d="2" h="2" caption="2 layers: 10 × 2 = 20 cubes"]]'),
             "ask": {"a": 2, "b": 3, "c": 1, "op": "vol"}},
        ],
        "practice_intro": ("Now it's your turn. One layer first, then count the "
                           "layers. Three right answers in a row and we're done — "
                           "here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. To find the "
                       "cubes in a box, we count one layer and then the layers. Tap "
                       "the reason why."),
            "choices": ("because every layer holds the same number of cubes | "
                        "because the top layer is the biggest | because boxes always "
                        "have two layers"),
            "answer": "because every layer holds the same number of cubes",
            "board": '[[solid kind="prism" w="3" d="2" h="2" caption="2 layers of 6 cubes"]]',
        },
        "recap": [
            ("So, here it is again. Volume is the cubes that fill a box: cubes in "
             "one layer — long times wide — then times the number of layers.",
             '[[solid kind="prism" w="3" d="2" h="2" caption="3 × 2 × 2 = 12 cubes"]]'),
            ("And it is how much fits in a box, or fills a tank — space counted in "
             "cubes, as area was counted in squares.",
             '[[step eq="3 × 2 × 2 = 12 cubes"]]'),
        ],
        "bank": [
            {"a": 2, "b": 2, "c": 1, "op": "vol"},
            {"a": 3, "b": 2, "c": 1, "op": "vol"},
            {"a": 2, "b": 2, "c": 2, "op": "vol"},
            {"a": 2, "b": 3, "c": 2, "op": "vol"},
            {"a": 4, "b": 1, "c": 4, "op": "vol"},
            {"a": 3, "b": 3, "c": 2, "op": "vol"},
            {"a": 4, "b": 3, "c": 2, "op": "vol"},
            {"a": 5, "b": 3, "c": 2, "op": "vol"},
            {"a": 4, "b": 4, "c": 2, "op": "vol"},
            {"a": 4, "b": 3, "c": 3, "op": "vol"},
            {"a": 4, "b": 4, "c": 3, "op": "vol"},
            {"a": 4, "b": 4, "c": 4, "op": "vol"},
        ],
    },
]
LESSONS.extend(_BASIC_MORE)

# ---- this course's slice of COURSE_ORDER: the teaching order (lessons/__init__.py joins the ten) ----
ORDER = [
    # ---- BASIC MATH (grades 3-5 band) ----
    "basic-u1-place-value-to-1000", "basic-u1-rounding-tens",
    "basic-u1-rounding-hundreds", "basic-u1-multi-digit-review",
    "basic-u2-what-multiplying-means", "basic-u2-times-tables",
    "basic-u2-multiply-two-digit", "basic-u2-times-by-ten",
    "basic-u3-what-dividing-means", "basic-u3-left-overs",
    "basic-u3-divide-two-digit", "basic-u3-story-problems",
    "basic-u4-missing-factors", "basic-u4-greatest-common-factor",
    "basic-u4-factor-pairs", "basic-u4-least-common-multiple",
    "basic-u5-fractions-on-the-number-line",
    "basic-u5-fraction-of-a-group", "basic-u5-equivalent-fractions",
    "basic-u5-simplest-form",
    "basic-u6-add-fractions-same-bottom", "basic-u6-take-away-fractions-same-bottom",
    "basic-u6-add-fractions-different-bottoms",
    "basic-u6-take-away-unlike-bottoms",
    "basic-u7-tenths", "basic-u7-dimes-and-pennies", "basic-u7-hundredths",
    "basic-u7-tenths-and-hundredths",
    "basic-u8-what-percent-is-it", "basic-u8-percent-of",
    "basic-u8-percent-off", "basic-u8-one-costs",
    "basic-u9-perimeter", "basic-u9-area",
    "basic-u9-quarter-turns", "basic-u9-volume",
]

# I did no harm and this file is not truncated.
