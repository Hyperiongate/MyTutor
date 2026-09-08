# =============================================================================
# lessons/probstat.py  --  PROBABILITY & STATISTICS: THE AUTHORED LESSONS  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
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

# =============================================================================
# PROB & STATS UNIT 1 -- Exploring Data (build lq) -- ⭐ THE TENTH COURSE OPENS
# The thread: BEFORE you compute anything, LOOK. Algebra One computed the mean,
# median and range from lists of numbers; this unit reads a picture instead --
# the mode under the tallest stack, a slice of the dots counted with an edge
# case standing on the line, a histogram's bars added up, and the one value
# that does not belong.
# =============================================================================
_PROBSTAT_U1 = [
    {
        "id": "ps-u1-under-the-tallest-stack",
        "course": "probstat", "unit": 1,
        "topic": "The mode from a picture",
        "op": "dotm", "max_value": 20,
        "levels": ("abstract",),
        "symbols": ("mode", "stack"),
        "advance_line": "Three in a row, and you can say why — you've got it! The mode is the value under the stack.",
        "why": [
            ("Why look before you count? Welcome to Probability and Statistics, where "
             "the first move is always to LOOK. A dot plot puts one dot above a number "
             "for every time that number happened. The shape of the data stands up off "
             "the page — tall where values repeat, flat where they do not.",
             '[[goal text="Under the tallest stack"]][[dotplot values="12,13,13,14,14,14,14,15,15,16" caption="one dot per value — the shape stands up off the page"]]'),
        ],
        "picture": [
            ("Here is a dot plot of books read: one dot per reader, stacked over the "
             "number of books. Look at the stacks — one of them stands taller than "
             "all the others. That tall stack is where the data piles up, and the "
             "number underneath it is the one that happened most.",
             '[[dotplot values="12,13,13,14,14,14,14,15,15,16" caption="one dot per reader — the tallest stack stands over one number"]]'),
        ],
        "teach": [
            ("That is the method: the mode is the value that happened most often, so "
             "find the tallest stack and read the number UNDERNEATH it. Here four dots "
             "stand over 14, more than any other number, so the mode is 14.",
             '[[dotplot values="12,13,13,14,14,14,14,15,15,16" caption="four dots over 14 — the mode is 14"]][[step eq="tallest stack over 14"]][[step eq="mode = 14"]]'),
            ("Here is the slip worth naming. Four dots stand on that stack, and 4 is "
             "not the answer — the mode is the value they stand on, 14, not the count "
             "of them. Read down to the number line, never across to how many.",
             '[[step eq="14 ✓ the value"]][[step eq="4 ✗ that is the count of dots"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. The tallest stack here sits over "
                        "16 — so the mode is 16, however many dots are stacked on it.",
                        '[[dotplot values="14,15,15,16,16,16,17,17,18" caption="the tallest stack stands over 16 — the mode is 16"]][[step eq="mode = 16"]]'),
             "ask": {'a': 18, 'b': 5, 'op': 'dotm'}},
            {"worked": ("One more together. The tallest stack here sits over 20, so the "
                        "mode is 20.",
                        '[[dotplot values="18,19,19,20,20,20,20,20,21,21,22" caption="five dots over 20 — the mode is 20"]][[step eq="mode = 20"]]'),
             "ask": {'a': 17, 'b': 6, 'op': 'dotm'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. On the plot with four "
                       "dots over 14, the mode is 14. Tap the reason why."),
            "choices": ("because the mode is the value under the tallest stack | because "
                        "the mode is how many dots stand on the stack | because the mode "
                        "is the biggest number on the line"),
            "answer": "because the mode is the value under the tallest stack",
            "board": '[[dotplot values="12,13,13,14,14,14,14,15,15,16" caption="the value under the tallest stack"]]',
        },
        "recap": [
            ("So, here it is again. A dot plot stacks one dot per value, and the mode "
             "is the value under the tallest stack — the number that happened most "
             "often. Read down to the number line, never across to the count of dots, "
             "and never grab the biggest number on the line.",
             '[[dotplot values="12,13,13,14,14,14,14,15,15,16" caption="under the tallest stack"]]'),
            ("And that is the first thing a picture of data can tell you.",
             '[[step eq="tallest stack over 14 · mode = 14"]]'),
        ],
        "bank": [
            {"a": 5, "b": 3, "op": "dotm"},
            {"a": 6, "b": 5, "op": "dotm"},
            {"a": 7, "b": 4, "op": "dotm"},
            {"a": 8, "b": 6, "op": "dotm"},
            {"a": 9, "b": 3, "op": "dotm"},
            {"a": 10, "b": 3, "op": "dotm"},
            {"a": 11, "b": 4, "op": "dotm"},
            {"a": 12, "b": 6, "op": "dotm"},
            {"a": 13, "b": 5, "op": "dotm"},
            {"a": 15, "b": 4, "op": "dotm"},
        ],
    },
    {
        "id": "ps-u1-count-the-ones-above",
        "course": "probstat", "unit": 1,
        "topic": "Counting part of a plot",
        "op": "dcnt", "max_value": 20,
        "levels": ("abstract",),
        "symbols": ("count", "line"),
        "advance_line": "Three in a row, and you can say why — you've got it! Count only past the line, and never the dot standing on it.",
        "why": [
            ("Why count part of a plot? A dot plot answers more than one question. "
             "Beyond what is most common, you can count how many values sit past some "
             "mark — how many players scored more than 8, how many days ran over an "
             "hour. Draw a line, then count one side of it.",
             '[[goal text="Count the ones above"]]'),
        ],
        "picture": [
            ("Here is a dot plot of goals, one dot per player, with a line to draw in "
             "your mind at 8. Look at the three kinds of dot: the ones to the left of "
             "8, the one standing exactly ON 8, and the ones to the right. More than 8 "
             "means the right-hand kind only.",
             '[[dotplot values="6,7,7,8,9,9,10,11" caption="one dot per player — left of 8, ON 8, and right of 8"]]'),
        ],
        "teach": [
            ("That is the method. Count how many are MORE than 8 here: 9, 9, 10 and "
             "11 — four dots to the right of 8. Work left to right and touch each dot "
             "once; a count you cannot repeat exactly is a count you should do again.",
             '[[dotplot values="6,7,7,8,9,9,10,11" caption="four dots to the right of 8"]][[step eq="more than 8 → 9, 9, 10, 11 → 4"]]'),
            ("The dot standing exactly ON 8 is the whole trap. More than 8 does not "
             "include 8 itself, so that dot stays out and the answer is 4, not 5. And "
             "counting the other side answers a question nobody asked. Read the word, "
             "then count.",
             '[[step eq="4 ✓"]][[step eq="5 ✗ counted the dot on the line"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. More than 14: five dots sit to "
                        "the right, and the one resting on 14 stays out.",
                        '[[dotplot values="11,12,13,13,14,15,15,16,17,17" caption="five dots past 14 — the one on 14 stays out"]][[step eq="more than 14 → 5"]]'),
             "ask": {'a': 13, 'b': 8, 'c': 7, 'op': 'dcnt'}},
            {"worked": ("One more together. More than 9, with seven dots past the line: "
                        "the answer is 7.",
                        '[[dotplot values="7,8,8,9,10,10,10,11,11,12,12" caption="seven dots past 9"]][[step eq="more than 9 → 7"]]'),
             "ask": {'a': 18, 'b': 7, 'c': 6, 'op': 'dcnt'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. On the plot with a "
                       "dot on 8, more than 8 counts 4 dots, not 5. Tap the reason why."),
            "choices": ("because the dot standing on 8 is not more than 8 | because the "
                        "dot on the line counts for both sides | because more than 8 "
                        "means 8 and everything past it"),
            "answer": "because the dot standing on 8 is not more than 8",
            "board": '[[dotplot values="6,7,7,8,9,9,10,11" caption="the dot on 8 stays out"]]',
        },
        "recap": [
            ("So, here it is again. To count part of a dot plot, draw the line, read "
             "the word, and count one side of it — touching each dot once. More than "
             "the line leaves the dot ON the line out, and never count the side that "
             "was not asked for.",
             '[[dotplot values="6,7,7,8,9,9,10,11" caption="count only past the line"]]'),
            ("And that is a plot answering a second question.",
             '[[step eq="more than 8 → 4"]]'),
        ],
        "bank": [
            {"a": 5, "b": 4, "c": 3, "op": "dcnt"},
            {"a": 10, "b": 4, "c": 8, "op": "dcnt"},
            {"a": 16, "b": 4, "c": 6, "op": "dcnt"},
            {"a": 5, "b": 5, "c": 9, "op": "dcnt"},
            {"a": 11, "b": 5, "c": 7, "op": "dcnt"},
            {"a": 17, "b": 5, "c": 3, "op": "dcnt"},
            {"a": 6, "b": 6, "c": 8, "op": "dcnt"},
            {"a": 12, "b": 6, "c": 4, "op": "dcnt"},
            {"a": 17, "b": 6, "c": 9, "op": "dcnt"},
            {"a": 7, "b": 7, "c": 5, "op": "dcnt"},
        ],
    },
    {
        "id": "ps-u1-add-the-bars",
        "course": "probstat", "unit": 1,
        "topic": "Reading a histogram",
        "op": "htot", "max_value": 27,
        "levels": ("abstract",),
        "symbols": ("histogram", "bars"),
        "advance_line": "Three in a row, and you can say why — you've got it! Add every bar to find how many there are in all.",
        "why": [
            ("Why bars instead of dots? When there are too many values for one dot "
             "each, a histogram sorts them into groups and draws a bar for each group. "
             "The bar's height is how many landed in that group — and on this board, "
             "each bar carries its count printed above it.",
             '[[goal text="Add the bars"]][[histogram values="5,5,5,15,15,15,15,25,25" caption="a bar for each group, its count printed on top"]]'),
        ],
        "picture": [
            ("Here is a histogram with three bars, and a count printed on each: 3, 4 "
             "and 2. Look at what the bars hide — you never see the values themselves, "
             "only how many landed in each group. The whole is every group put "
             "together.",
             '[[histogram values="5,5,5,15,15,15,15,25,25" caption="three groups — 3, 4 and 2 landed in them"]]'),
        ],
        "teach": [
            ("That is the method: to find how many values there are in all, add the "
             "bars. 3 plus 4 plus 2 equals 9 values. A histogram never shows you the "
             "values themselves — adding the counts brings them all back.",
             '[[histogram values="5,5,5,15,15,15,15,25,25" caption="3 + 4 + 2 = 9 in all"]][[step eq="3 + 4 + 2 = 9 values in all"]]'),
            ("Two easy misreads. The tallest bar, 4, is only the biggest group — it "
             "is not the whole. And counting the bars themselves gives 3, which is how "
             "many GROUPS there are, not how many values. Add the heights, always.",
             '[[step eq="9 ✓"]][[step eq="4 ✗ tallest group · 3 ✗ number of groups"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Bars of 4, 4 and 4: adding them "
                        "gives 12 values in all.",
                        '[[histogram values="5,5,5,5,15,15,15,15,25,25,25,25" caption="4 + 4 + 4 = 12"]][[step eq="4 + 4 + 4 = 12"]]'),
             "ask": {'a': 9, 'b': 8, 'c': 5, 'op': 'htot'}},
            {"worked": ("One more together. Bars of 5, 5 and 5 add up to 15 values.",
                        '[[histogram values="5,5,5,5,5,15,15,15,15,15,25,25,25,25,25" caption="5 + 5 + 5 = 15"]][[step eq="5 + 5 + 5 = 15"]]'),
             "ask": {'a': 7, 'b': 6, 'c': 8, 'op': 'htot'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Bars of 3, 4 and 2 "
                       "show 9 values in all. Tap the reason why."),
            "choices": ("because the groups add up to the whole | because the tallest bar "
                        "is the whole | because the number of bars is the number of "
                        "values"),
            "answer": "because the groups add up to the whole",
            "board": '[[histogram values="5,5,5,15,15,15,15,25,25" caption="3 + 4 + 2 = 9"]]',
        },
        "recap": [
            ("So, here it is again. A histogram sorts values into groups and prints "
             "each group's count on its bar; how many in all is every bar added. The "
             "tallest bar is only the biggest group, and the number of bars is only the "
             "number of groups.",
             '[[histogram values="5,5,5,15,15,15,15,25,25" caption="add every bar"]]'),
            ("And that is the values, brought back from their groups.",
             '[[step eq="3 + 4 + 2 = 9"]]'),
        ],
        "bank": [
            {"a": 2, "b": 4, "c": 3, "op": "htot"},
            {"a": 3, "b": 4, "c": 4, "op": "htot"},
            {"a": 6, "b": 3, "c": 3, "op": "htot"},
            {"a": 7, "b": 3, "c": 3, "op": "htot"},
            {"a": 6, "b": 5, "c": 3, "op": "htot"},
            {"a": 5, "b": 6, "c": 4, "op": "htot"},
            {"a": 4, "b": 7, "c": 5, "op": "htot"},
            {"a": 2, "b": 9, "c": 6, "op": "htot"},
            {"a": 8, "b": 4, "c": 5, "op": "htot"},
            {"a": 7, "b": 4, "c": 7, "op": "htot"},
        ],
    },
    {
        "id": "ps-u1-the-one-that-sits-alone",
        "course": "probstat", "unit": 1,
        "topic": "Spotting an outlier",
        "op": "farv", "max_value": 40,
        "levels": ("abstract",),
        "symbols": ("outlier", "cluster"),
        "advance_line": "Three in a row, and you can say why — you've got it! The outlier is the value sitting alone, far from the crowd.",
        "why": [
            ("Why hunt for the stray? Algebra One showed what one unusual value does "
             "to a mean — it drags it. Before you can watch for that, you have to SPOT "
             "the stray. On a dot plot it is obvious: nearly every dot huddles in one "
             "cluster, and one sits out on its own with a gap between.",
             '[[goal text="The one that sits alone"]]'),
        ],
        "picture": [
            ("Here is a dot plot of minutes taken, one dot per student. Look at the "
             "crowd huddled between 6 and 9 — and then look at the empty stretch to "
             "the right of it, and the single dot out at 26 with nobody near it. That "
             "lonely dot is the one we want.",
             '[[dotplot values="6,7,7,8,8,9,26" caption="a crowd from 6 to 9, a gap, and one dot alone at 26"]]'),
        ],
        "teach": [
            ("That is the method. That lonely dot is called an outlier, and here it "
             "sits at 26 while the crowd huddles between 6 and 9. The outlier is the "
             "VALUE it sits above — 26 — the same way the mode was the value under its "
             "stack.",
             '[[dotplot values="6,7,7,8,8,9,26" caption="the stray sits above 26 — the outlier is 26"]][[step eq="crowd 6 to 9 · stray at 26"]][[step eq="outlier = 26"]]'),
            ("Two things not to hand back. 7, where the crowd is thickest, is the "
             "mode — a different question. And 20, the size of the gap, tells you how "
             "far out the stray is, not what it is. Point at the lonely dot and read "
             "the number below it.",
             '[[step eq="26 ✓"]][[step eq="7 ✗ the crowd · 20 ✗ the gap"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. The crowd sits near 10 and one "
                        "dot is stranded at 30 — the outlier is 30.",
                        '[[dotplot values="9,10,10,11,11,12,30" caption="the crowd near 10; the stray at 30"]][[step eq="outlier = 30"]]'),
             "ask": {'a': 15, 'b': 38, 'op': 'farv'}},
            {"worked": ("One more together. A crowd around 13 with one stray far out at "
                        "35: the outlier is 35.",
                        '[[dotplot values="12,13,13,14,14,15,35" caption="the crowd near 13; the stray at 35"]][[step eq="outlier = 35"]]'),
             "ask": {'a': 12, 'b': 37, 'op': 'farv'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. On the plot with a "
                       "crowd from 6 to 9, the outlier is 26. Tap the reason why."),
            "choices": ("because 26 sits under the dot far from the crowd | because the "
                        "outlier is the value where the crowd is thickest | because the "
                        "outlier is the size of the gap"),
            "answer": "because 26 sits under the dot far from the crowd",
            "board": '[[dotplot values="6,7,7,8,8,9,26" caption="the one that sits alone"]]',
        },
        "recap": [
            ("So, here it is again. An outlier is the value sitting alone, far from "
             "the crowd, with a gap between — read the number under that lonely dot. "
             "Never hand back the crowd's value, and never hand back the size of the "
             "gap.",
             '[[dotplot values="6,7,7,8,8,9,26" caption="the value under the lonely dot"]]'),
            ("And that is the stray, spotted before it drags anything.",
             '[[step eq="crowd 6 to 9 · outlier = 26"]]'),
        ],
        "bank": [
            {"a": 5, "b": 17, "op": "farv"},
            {"a": 9, "b": 21, "op": "farv"},
            {"a": 5, "b": 24, "op": "farv"},
            {"a": 12, "b": 25, "op": "farv"},
            {"a": 8, "b": 27, "op": "farv"},
            {"a": 11, "b": 28, "op": "farv"},
            {"a": 15, "b": 29, "op": "farv"},
            {"a": 8, "b": 31, "op": "farv"},
            {"a": 11, "b": 32, "op": "farv"},
            {"a": 14, "b": 33, "op": "farv"},
        ],
    },
]
LESSONS.extend(_PROBSTAT_U1)

# =============================================================================
# PROB & STATS UNIT 2 -- Describing Distributions (build lq)
# The thread: now put NUMBERS on the shape. The median when there is no single
# middle, the box plot's box as the middle half, the average distance from the
# mean (standard deviation in child clothes), and a percentile read as a
# percent of the class rather than a headcount.
# =============================================================================
_PROBSTAT_U2 = [
    {
        "id": "ps-u2-no-single-middle",
        "course": "probstat", "unit": 2,
        "topic": "The median of an even list",
        "op": "medv", "max_value": 30,
        "levels": ("abstract",),
        "symbols": ("median", "middles"),
        "advance_line": "Three in a row, and you can say why — you've got it! Two middles — the median sits halfway between them.",
        "why": [
            ("Why is there no single middle? Algebra One found the median of an odd "
             "list: count in from both ends and one number is left standing. Unit Two "
             "starts with the case that has no single middle at all — an even count, "
             "where counting in from both ends leaves TWO numbers facing each other.",
             '[[goal text="No single middle"]][[step eq="2, 4, | 6, 8 | , 10, 12"]]'),
        ],
        "picture": [
            ("Here are six numbers on a dot plot: 2, 4, 6, 8, 10, 12. Count in from "
             "both ends — two from the left, two from the right. Look at what is left: "
             "6 and 8, two dots facing each other across a gap with nothing standing "
             "in it. The median lives in that gap.",
             '[[dotplot values="2,4,6,8,10,12" caption="six numbers — count in from both ends and two middles face each other"]]'),
        ],
        "teach": [
            ("That is the method: find both middles, then go halfway. Take 2, 4, 6, 8, "
             "10, 12 — six numbers, so three sit either side and the middles are 6 and "
             "8. Add and halve: 6 plus 8 is 14, halved is 7. The median of an even "
             "list often is not in the list at all.",
             '[[numberline min="1" max="13" points="6,8" mid="7" caption="the two middles, 6 and 8 — halfway between them is 7"]][[step eq="middles 6 and 8"]][[step eq="(6 + 8) ÷ 2 = 7"]]'),
            ("Neither middle on its own will do. Answering 6 takes the lower one and 8 "
             "takes the upper, and both leave half the data unbalanced — 7 is the only "
             "number with three below it and three above. Find both middles, then go "
             "halfway.",
             '[[step eq="7 ✓"]][[step eq="6 ✗ lower middle · 8 ✗ upper middle"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 9, 11, 13, 15, 17, 19: the "
                        "middles are 13 and 15, so the median is 14.",
                        '[[numberline min="8" max="20" points="13,15" mid="14" caption="middles 13 and 15 — halfway is 14"]][[step eq="(13 + 15) ÷ 2 = 14"]]'),
             "ask": {'a': 3, 'b': 23, 'op': 'medv'}},
            {"worked": ("One more together. With middles of 9 and 11: 9 plus 11 is 20, "
                        "halved — the median is 10.",
                        '[[numberline min="4" max="16" points="9,11" mid="10" caption="middles 9 and 11 — halfway is 10"]][[step eq="(9 + 11) ÷ 2 = 10"]]'),
             "ask": {'a': 2, 'b': 22, 'op': 'medv'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The median of 2, 4, "
                       "6, 8, 10, 12 is 7. Tap the reason why."),
            "choices": ("because 7 is halfway between the two middles, 6 and 8 | because "
                        "the median is the lower of the two middles | because the median "
                        "is the upper of the two middles"),
            "answer": "because 7 is halfway between the two middles, 6 and 8",
            "board": '[[numberline min="1" max="13" points="6,8" mid="7" caption="halfway between the two middles"]]',
        },
        "recap": [
            ("So, here it is again. An even list has no single middle: count in from "
             "both ends, find the two middles facing each other, and the median is "
             "halfway between them — add and halve. Never take the lower middle "
             "alone, and never the upper.",
             '[[dotplot values="2,4,6,8,10,12" caption="two middles — the median sits halfway between them"]]'),
            ("And that is a median that is not in the list.",
             '[[step eq="(6 + 8) ÷ 2 = 7"]]'),
        ],
        "bank": [
            {"a": 2, "b": 4, "op": "medv"},
            {"a": 2, "b": 7, "op": "medv"},
            {"a": 4, "b": 8, "op": "medv"},
            {"a": 2, "b": 10, "op": "medv"},
            {"a": 3, "b": 11, "op": "medv"},
            {"a": 4, "b": 12, "op": "medv"},
            {"a": 2, "b": 14, "op": "medv"},
            {"a": 3, "b": 15, "op": "medv"},
            {"a": 4, "b": 16, "op": "medv"},
            {"a": 2, "b": 18, "op": "medv"},
        ],
    },
    {
        "id": "ps-u2-the-middle-half",
        "course": "probstat", "unit": 2,
        "topic": "The box plot's box",
        "op": "iqrw", "max_value": 60,
        "levels": ("abstract",),
        "symbols": ("box", "whiskers"),
        "advance_line": "Three in a row, and you can say why — you've got it! The box is the middle half — take one edge away from the other.",
        "why": [
            ("Why a box? A box plot draws five numbers: the smallest, the biggest, "
             "the median in the middle, and two more that cut the data into quarters. "
             "The box spans the middle two quarters — the middle HALF of everything — "
             "and the whiskers reach out to the extremes.",
             '[[goal text="The middle half"]]'),
        ],
        "picture": [
            ("Here is a box plot. Look at its three parts: a whisker reaching out "
             "left to 4, the box in the middle from 10 to 20 with the median line "
             "inside it, and a whisker reaching right to 26. The box is the calm "
             "middle half; the whiskers are the wild ends.",
             '[[boxplot five="4,10,15,20,26" caption="five numbers drawn as a box — the box runs 10 to 20"]]'),
        ],
        "teach": [
            ("That is the method: two edges, one take-away. This box runs from 10 to "
             "20, so the middle half of the data lies between them: its width is 20 "
             "take away 10 — 10. Statisticians lean on that width because the wild "
             "extremes cannot touch it.",
             '[[boxplot five="4,10,15,20,26" caption="the box runs 10 to 20 — 10 wide"]][[step eq="box: 10 to 20"]][[step eq="20 − 10 = 10"]]'),
            ("Do not measure the whiskers by mistake. Tip to tip is 4 out to 26 — a "
             "stretch of 22, the whole range, which one strange value can blow wide "
             "open. And 20 alone is just the box\'s right edge. Two edges, one "
             "take-away.",
             '[[step eq="10 ✓ the box"]][[step eq="22 ✗ whisker to whisker · 20 ✗ one edge"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. A box from 12 to 24: the middle "
                        "half is 24 take away 12 — 12 wide.",
                        '[[boxplot five="8,12,18,24,28" caption="the box runs 12 to 24 — 12 wide"]][[step eq="24 − 12 = 12"]]'),
             "ask": {'a': 14, 'b': 34, 'c': 6, 'op': 'iqrw'}},
            {"worked": ("One more together. This box runs 15 to 27: 27 take away 15 — 12 "
                        "wide as well, however far its whiskers reach.",
                        '[[boxplot five="9,15,21,27,33" caption="the box runs 15 to 27 — 12 wide"]][[step eq="27 − 15 = 12"]]'),
             "ask": {'a': 23, 'b': 41, 'c': 6, 'op': 'iqrw'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. On the box plot whose "
                       "box runs 10 to 20, the middle half is 10 wide. Tap the reason "
                       "why."),
            "choices": ("because the box is the middle half, edge to edge | because the "
                        "middle half runs from whisker to whisker | because the width of "
                        "the box is its right edge"),
            "answer": "because the box is the middle half, edge to edge",
            "board": '[[boxplot five="4,10,15,20,26" caption="20 − 10 = 10"]]',
        },
        "recap": [
            ("So, here it is again. The box of a box plot is the middle half of the "
             "data, and its width is one edge taken away from the other. Never "
             "measure whisker to whisker — that is the whole range — and never hand "
             "back one edge as the width.",
             '[[boxplot five="4,10,15,20,26" caption="the box is the middle half"]]'),
            ("And that is the calm middle, measured.",
             '[[step eq="20 − 10 = 10"]]'),
        ],
        "bank": [
            {"a": 5, "b": 9, "c": 2, "op": "iqrw"},
            {"a": 22, "b": 26, "c": 2, "op": "iqrw"},
            {"a": 13, "b": 19, "c": 2, "op": "iqrw"},
            {"a": 29, "b": 35, "c": 3, "op": "iqrw"},
            {"a": 20, "b": 28, "c": 3, "op": "iqrw"},
            {"a": 11, "b": 21, "c": 2, "op": "iqrw"},
            {"a": 27, "b": 37, "c": 4, "op": "iqrw"},
            {"a": 18, "b": 30, "c": 4, "op": "iqrw"},
            {"a": 9, "b": 23, "c": 2, "op": "iqrw"},
            {"a": 25, "b": 39, "c": 5, "op": "iqrw"},
        ],
    },
    {
        "id": "ps-u2-how-far-from-the-middle",
        "course": "probstat", "unit": 2,
        "topic": "Average distance from the mean",
        "op": "madv", "max_value": 30,
        "levels": ("abstract",),
        "symbols": ("distance", "spread"),
        "advance_line": "Three in a row, and you can say why — you've got it! Add the four distances, then share them out.",
        "why": [
            ("Why measure spread? Two sets can share a mean and look nothing alike: "
             "19, 20, 21 huddles, while 5, 20, 35 sprawls. To describe that difference "
             "you measure spread — and the plainest measure asks how far a number "
             "sits from the mean, on average.",
             '[[goal text="How far from the middle"]][[dotplot values="19,20,21" caption="a huddle around 20"]][[dotplot values="5,20,35" caption="a sprawl around the same 20"]]'),
        ],
        "picture": [
            ("Here are four numbers on a dot plot — 11, 17, 23, 29 — with their mean "
             "at 20 in the middle. Look at how far each dot sits from 20: the outer "
             "two far, the inner two close. Those four distances are what we average.",
             '[[dotplot values="11,17,23,29" caption="four numbers, their mean at 20 — how far does each sit from it?"]]'),
        ],
        "teach": [
            ("That is the method. The distances from 20 are 9, 3, 3 and 9 — never "
             "mind which side, distance has no sign. Put them together for 24, then "
             "share between the four numbers: each sits 6 from the mean, on average.",
             '[[bars data="11:9 | 17:3 | 23:3 | 29:9" caption="the four distances — 24 in all, shared four ways: 6"]][[step eq="9 + 3 + 3 + 9 = 24"]] [[step eq="24 ÷ 4 = 6"]]'),
            ("The two temptations are the extremes. The farthest number is 9 away and "
             "the nearest only 3, so an average distance of 6 sits between them — as "
             "an average must. Square these distances instead and you get variance, "
             "which is another unit\'s business.",
             '[[step eq="6 ✓"]][[step eq="9 ✗ the farthest · 3 ✗ the nearest"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 2, 12, 22, 32 have a mean of 17 "
                        "and distances of 15, 5, 5, 15 — put together 40, shared four "
                        "ways: 10.",
                        '[[bars data="2:15 | 12:5 | 22:5 | 32:15" caption="40 in all, shared four ways: 10"]][[step eq="40 ÷ 4 = 10"]]'),
             "ask": {'a': 24, 'b': 6, 'op': 'madv'}},
            {"worked": ("One more together. 10, 18, 26, 34: mean 22, distances 12, 4, 4, "
                        "12 — put together 32, shared four ways: 8.",
                        '[[bars data="10:12 | 18:4 | 26:4 | 34:12" caption="32 in all, shared four ways: 8"]][[step eq="(12 + 4 + 4 + 12) ÷ 4 = 8"]]'),
             "ask": {'a': 29, 'b': 5, 'op': 'madv'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. For 11, 17, 23, 29 "
                       "with a mean of 20, the average distance is 6. Tap the reason "
                       "why."),
            "choices": ("because the four distances add to 24, shared four ways | because "
                        "the average distance is the farthest one | because the average "
                        "distance is the nearest one"),
            "answer": "because the four distances add to 24, shared four ways",
            "board": '[[bars data="11:9 | 17:3 | 23:3 | 29:9" caption="24 ÷ 4 = 6"]]',
        },
        "recap": [
            ("So, here it is again. Spread is how far the numbers sit from the mean, "
             "on average: measure each distance without a sign, add them, then share "
             "them out. The answer sits between the nearest and the farthest — never "
             "one of those extremes.",
             '[[dotplot values="11,17,23,29" caption="add the four distances, then share them out"]]'),
            ("And that is spread, in plain clothes.",
             '[[step eq="(9 + 3 + 3 + 9) ÷ 4 = 6"]]'),
        ],
        "bank": [
            {"a": 8, "b": 2, "op": "madv"},
            {"a": 14, "b": 2, "op": "madv"},
            {"a": 20, "b": 2, "op": "madv"},
            {"a": 26, "b": 2, "op": "madv"},
            {"a": 12, "b": 3, "op": "madv"},
            {"a": 18, "b": 3, "op": "madv"},
            {"a": 24, "b": 3, "op": "madv"},
            {"a": 30, "b": 3, "op": "madv"},
            {"a": 19, "b": 4, "op": "madv"},
            {"a": 25, "b": 4, "op": "madv"},
        ],
    },
    {
        "id": "ps-u2-a-percent-not-a-person",
        "course": "probstat", "unit": 2,
        "topic": "Percentiles",
        "op": "pctl", "max_value": 90,
        "levels": ("abstract",),
        "symbols": ("percentile", "percent"),
        "advance_line": "Three in a row, and you can say why — you've got it! A percentile is a percent of the group, not a count of people.",
        "why": [
            ("Why a percent, not a person? A last way to place one value inside a "
             "distribution: say what percent of the others it beat. That is a "
             "percentile. Finishing at the 80th percentile means faster than 80 "
             "percent of the racers you were measured against — nothing more, "
             "nothing less.",
             '[[goal text="A percent, not a person"]][[step eq="80th percentile → faster than 80% of them"]]'),
        ],
        "picture": [
            ("Here is the 80th percentile as a hundred square: 80 of every 100 "
             "shaded. Look at what the square does NOT say — it never says how many "
             "racers there were. The percentile is the shading; the headcount comes "
             "only when you know the size of the group.",
             '[[hundredgrid shaded="80" unit="percent" eq="80th percentile: 80%" caption="80 of every 100 — the group\'s size is a separate fact"]]'),
        ],
        "teach": [
            ("That is the method: turn it into people by taking that percent of the "
             "group. A runner races 20 others and finishes at the 80th percentile: 80 "
             "percent of 20 is 16, so she beat 16 of them and 4 finished ahead. The "
             "percentile never changes, but the headcount depends on the group.",
             '[[bars data="beaten:16 | ahead of her:4" caption="80% of 20 = 16 beaten, 4 ahead"]][[step eq="80% of 20 = 16 beaten · 4 ahead"]]'),
            ("Two mix-ups to dodge. The 80 is a percent, not 80 people — among 20 "
             "racers there are not 80 anybody. And 4 answers the opposite question, "
             "how many finished ahead. Take the percent of the group, and read which "
             "side was asked for.",
             '[[step eq="16 ✓"]][[step eq="80 ✗ that is the percent · 4 ✗ the other side"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. A swimmer against 60 others at "
                        "the 25th percentile: a quarter of 60 is 15 of them beaten.",
                        '[[bars data="beaten:15 | ahead:45" caption="25% of 60 = 15"]][[step eq="25% of 60 = 15"]]'),
             "ask": {'a': 40, 'b': 85, 'op': 'pctl'}},
            {"worked": ("One more together. Against 30 others at the 90th percentile: 90 "
                        "percent of 30 is 27.",
                        '[[bars data="beaten:27 | ahead:3" caption="90% of 30 = 27"]][[step eq="90% of 30 = 27"]]'),
             "ask": {'a': 40, 'b': 75, 'op': 'pctl'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. At the 80th "
                       "percentile among 20 others, a runner beat 16 of them. Tap the "
                       "reason why."),
            "choices": ("because a percentile is a percent of the group | because the "
                        "80th percentile means 80 racers were beaten | because the "
                        "percentile counts the racers ahead"),
            "answer": "because a percentile is a percent of the group",
            "board": '[[bars data="beaten:16 | ahead of her:4" caption="a percent of the group"]]',
        },
        "recap": [
            ("So, here it is again. A percentile is a percent of the group, not a "
             "count of people: take that percent of the group\'s size for the "
             "headcount, and read which side was asked for. Never hand back the "
             "percent as people, and never the other side.",
             '[[hundredgrid shaded="80" unit="percent" eq="80th percentile: 80%" caption="a percent, not a person"]]'),
            ("And that is one value, placed inside its distribution.",
             '[[step eq="80% of 20 = 16"]]'),
        ],
        "bank": [
            {"a": 20, "b": 10, "op": "pctl"},
            {"a": 50, "b": 10, "op": "pctl"},
            {"a": 20, "b": 35, "op": "pctl"},
            {"a": 20, "b": 45, "op": "pctl"},
            {"a": 40, "b": 25, "op": "pctl"},
            {"a": 30, "b": 40, "op": "pctl"},
            {"a": 20, "b": 70, "op": "pctl"},
            {"a": 50, "b": 30, "op": "pctl"},
            {"a": 24, "b": 75, "op": "pctl"},
            {"a": 50, "b": 40, "op": "pctl"},
        ],
    },
]
LESSONS.extend(_PROBSTAT_U2)
# =============================================================================
# PROB & STATS UNIT 3 -- Scatterplots & Correlation (build lr)
# The thread: TWO measurements at once. Each dot carries a pair, so the cloud
# shows how one thing moves with another -- read a single dot without mixing
# the axes, use the fit line's slope as a RATE, measure how far a dot sits
# from the line it predicted (the residual), and see that the line runs
# THROUGH the cloud rather than over or under it.
# ⭐ [[scatter]] walked here for the first time. It prints the fit equation
# when fit="true", so any lesson whose answer IS the line stays teach-only.
# =============================================================================
_PROBSTAT_U3 = [
    {
        "id": "ps-u3-one-dot-two-numbers",
        "course": "probstat", "unit": 3,
        "topic": "Reading a scatterplot",
        "op": "spnt", "max_value": 50,
        "levels": ("abstract",),
        "symbols": ("scatterplot", "dot"),
        "advance_line": "Three in a row, and you can say why — you've got it! Across for the hours, up for the points.",
        "why": [
            ("Why two numbers on one dot? Every plot so far showed ONE measurement. A "
             "scatterplot shows two at once: each dot is one student, placed across "
             "by hours practiced and up by points scored. That pairing is what lets "
             "you see whether practice and points travel together.",
             '[[goal text="One dot, two numbers"]]'),
        ],
        "picture": [
            ("Here is a scatterplot of six students. Look at any one dot: slide "
             "straight down from it and you land on the hours along the bottom; slide "
             "straight across from it and you land on the points up the side. One "
             "dot, two numbers — and the cloud rises from left to right.",
             '[[scatter points="(2,12),(4,22),(6,31),(8,41),(10,50),(12,62)" caption="each dot is one student — hours across, points up"]]'),
        ],
        "teach": [
            ("That is the method: across first, then up, then across again. To read "
             "a student, find their hours along the bottom, go straight up until you "
             "meet their dot, then straight across to the side. The student at 8 hours "
             "sits level with 41 — so 41 points.",
             '[[scatter points="(2,12),(4,22),(6,31),(8,41),(10,50),(12,62)" caption="8 along the bottom, up to the dot, across to 41"]][[step eq="8 hours → up to the dot → across → 41 points"]]'),
            ("The mix-up to avoid is answering with the number you were GIVEN. 8 is "
             "the hours, and hours live across the bottom; the points live up the "
             "side. And it is easy to land on the dot next door — 50 belongs to the "
             "student who practiced 10 hours, not 8.",
             '[[step eq="41 ✓"]][[step eq="8 ✗ that is the hours · 50 ✗ the next dot"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. This student practiced 8 hours: "
                        "go up to the dot, across to the side — 35 points.",
                        '[[scatter points="(2,10),(4,20),(6,25),(8,35),(10,40),(12,50)" caption="the dot at 8 hours sits level with 35"]][[step eq="8 hours · up · across = 35 points"]]'),
             "ask": {'a': 12, 'b': 0, 'c': 2, 'op': 'spnt'}},
            {"worked": ("One more together. On a gentler plot, the student at 6 hours "
                        "sits level with 13 points.",
                        '[[scatter points="(2,6),(4,12),(6,13),(8,19),(10,20),(12,26)" caption="the dot at 6 hours sits level with 13"]][[step eq="6 hours · up · across = 13 points"]]'),
             "ask": {'a': 10, 'b': 0, 'c': 3, 'op': 'spnt'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. On the plot, the "
                       "student at 8 hours scored 41 points. Tap the reason why."),
            "choices": ("because the dot above 8 sits level with 41 on the side | because "
                        "the hours are the points | because the nearest dot to the right "
                        "gives the points"),
            "answer": "because the dot above 8 sits level with 41 on the side",
            "board": '[[scatter points="(2,12),(4,22),(6,31),(8,41),(10,50),(12,62)" caption="across, up, across"]]',
        },
        "recap": [
            ("So, here it is again. Each dot on a scatterplot carries two numbers: "
             "find the given one along the bottom, go straight up to the dot, then "
             "straight across to the side for the other. Never hand back the number "
             "you were given, and never read the dot next door.",
             '[[scatter points="(2,12),(4,22),(6,31),(8,41),(10,50),(12,62)" caption="one dot, two numbers"]]'),
            ("And that is two measurements, seen together.",
             '[[step eq="8 hours → up → across → 41 points"]]'),
        ],
        "bank": [
            {"a": 2, "b": 0, "c": 2, "op": "spnt"},
            {"a": 2, "b": 0, "c": 3, "op": "spnt"},
            {"a": 4, "b": 0, "c": 2, "op": "spnt"},
            {"a": 4, "b": 0, "c": 4, "op": "spnt"},
            {"a": 6, "b": 0, "c": 3, "op": "spnt"},
            {"a": 6, "b": 0, "c": 4, "op": "spnt"},
            {"a": 8, "b": 0, "c": 2, "op": "spnt"},
            {"a": 8, "b": 0, "c": 3, "op": "spnt"},
            {"a": 10, "b": 0, "c": 2, "op": "spnt"},
            {"a": 10, "b": 0, "c": 4, "op": "spnt"},
        ],
    },
    {
        "id": "ps-u3-the-slope-is-a-rate",
        "course": "probstat", "unit": 3,
        "topic": "Using the best-fit line's slope",
        "op": "sslp", "max_value": 81,
        "levels": ("abstract",),
        "symbols": ("slope", "per"),
        "advance_line": "Three in a row, and you can say why — you've got it! The slope is points per hour — times the hours.",
        "why": [
            ("Why is a slope a rate? Draw the single straight line that runs best "
             "through a scatter cloud and you have a best-fit line. Algebra One "
             "measured a line\'s slope as its climb per step. Here that climb MEANS "
             "something: points per extra hour of practice.",
             '[[goal text="The slope is a rate"]]'),
        ],
        "picture": [
            ("Here is a scatter cloud with its best-fit line drawn through it. Look "
             "at the line, not the dots: for every hour you move to the right, the "
             "line climbs the same number of points. That steady climb per hour is "
             "the slope — a rate, ready to be timesed by however many hours.",
             '[[scatter points="(2,11),(4,17),(6,26),(8,34),(10,41),(12,51)" fit="true" caption="the best-fit line climbs 4 for every extra hour"]]'),
        ],
        "teach": [
            ("That is the method: times the rate by the steps. Say the slope is 4 — "
             "four more points for each extra hour. Then two extra hours are worth 4 "
             "twice: 8 points. Ten extra hours would be worth 40. A slope is a rate, "
             "so it multiplies by however many steps you take.",
             '[[graph lines="y=4x" names="4 points per hour" points="(2,8),(10,40)" range="0..12" yrange="0..50" caption="4 per hour — 2 hours up is 8, 10 hours up is 40"]][[step eq="4 points per hour × 2 hours = 8 points"]]'),
            ("Two slips. Answering 4 gives ONE hour\'s worth when the question asked "
             "about two. And adding — 4 plus 2 — treats a rate as though it were a "
             "total. Times the rate by the steps, every time.",
             '[[step eq="8 ✓"]][[step eq="4 ✗ one hour only · 6 ✗ added"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. A slope of 7 points per hour, over "
                        "5 extra hours: 7 times 5 — 35 more points.",
                        '[[graph lines="y=7x" names="7 points per hour" points="(5,35)" range="0..7" yrange="0..45" caption="7 × 5 = 35"]][[step eq="7 × 5 = 35"]]'),
             "ask": {'a': 7, 'b': 7, 'op': 'sslp'}},
            {"worked": ("One more together. 5 points per hour over 8 hours: 5 times 8 — 40 "
                        "more points.",
                        '[[machine input="8" rule="× 5" output="40" caption="8 hours in, 5 points each — 40"]][[step eq="5 × 8 = 40"]]'),
             "ask": {'a': 5, 'b': 9, 'op': 'sslp'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A slope of 4 points "
                       "per hour is worth 8 points over two extra hours. Tap the reason "
                       "why."),
            "choices": ("because a rate multiplies by however many steps you take | "
                        "because the slope is the total, whatever the hours | because a "
                        "rate is added to the hours"),
            "answer": "because a rate multiplies by however many steps you take",
            "board": '[[graph lines="y=4x" names="4 points per hour" points="(2,8)" range="0..12" yrange="0..50" caption="4 × 2 = 8"]]',
        },
        "recap": [
            ("So, here it is again. The slope of a best-fit line is a rate — points "
             "per extra hour — so times it by the hours to predict the extra points. "
             "Never hand back one hour\'s worth, and never add the rate to the hours.",
             '[[scatter points="(2,11),(4,17),(6,26),(8,34),(10,41),(12,51)" fit="true" caption="the slope is a rate"]]'),
            ("And that is a line that predicts.",
             '[[step eq="4 × 2 = 8"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "op": "sslp"},
            {"a": 3, "b": 3, "op": "sslp"},
            {"a": 3, "b": 4, "op": "sslp"},
            {"a": 7, "b": 2, "op": "sslp"},
            {"a": 4, "b": 4, "op": "sslp"},
            {"a": 6, "b": 3, "op": "sslp"},
            {"a": 3, "b": 7, "op": "sslp"},
            {"a": 6, "b": 4, "op": "sslp"},
            {"a": 9, "b": 3, "op": "sslp"},
            {"a": 6, "b": 5, "op": "sslp"},
        ],
    },
    {
        "id": "ps-u3-how-far-off-the-line",
        "course": "probstat", "unit": 3,
        "topic": "Residuals",
        "op": "resd", "max_value": 60,
        "levels": ("abstract",),
        "symbols": ("residual", "predicted"),
        "advance_line": "Three in a row, and you can say why — you've got it! The residual is the gap between predicted and actual.",
        "why": [
            ("Why does a prediction miss? A best-fit line predicts, and predictions "
             "miss. Read the line at some student\'s hours and it names a score; look "
             "at that student\'s real dot and you see what they actually got. The gap "
             "between those two is the interesting part.",
             '[[goal text="How far off the line"]]'),
        ],
        "picture": [
            ("Here are two bars: what the line predicted, 30, and what the student "
             "actually scored, 36. Look at the gap between the tops of the bars — the "
             "line guessed a little low. That gap is the whole lesson.",
             '[[bars data="predicted:30 | actual:36" caption="the line said 30, the student scored 36 — the gap is the residual"]]'),
        ],
        "teach": [
            ("That is the method: the gap has a name, the residual. If the line "
             "predicted 30 and the student scored 36, the residual is 6 — the line "
             "was 6 points low. A dot above the line has the line guessing low; a dot "
             "below has it guessing high.",
             '[[numberline min="25" max="41" hops="30,36" caption="from predicted 30 to actual 36 — a gap of 6"]][[step eq="36 − 30 = 6"]] [[step eq="residual = 6"]]'),
            ("The best-fit line is chosen to keep these gaps as small as they can be "
             "across every dot at once — that is what BEST fit means. So do not hand "
             "back 36, which is what the student scored, or 66, which puts two "
             "unrelated numbers together.",
             '[[step eq="6 ✓"]][[step eq="36 ✗ the actual score · 66 ✗ added"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Predicted 29, actual 56: the line "
                        "was 27 points low.",
                        '[[numberline min="24" max="61" hops="29,56" caption="from 29 to 56 — a gap of 27"]][[step eq="56 − 29 = 27"]]'),
             "ask": {'a': 5, 'b': 47, 'op': 'resd'}},
            {"worked": ("One more together. Predicted 44, actual 14: 44 take away 14 — the "
                        "line guessed 30 points high.",
                        '[[bars data="predicted:44 | actual:14" caption="the line said 44, the score was 14 — 30 high"]][[step eq="44 − 14 = 30"]]'),
             "ask": {'a': 11, 'b': 47, 'op': 'resd'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The line predicted 30, "
                       "the student scored 36, and the residual is 6. Tap the reason "
                       "why."),
            "choices": ("because the residual is the gap between predicted and actual | "
                        "because the residual is the score the student got | because the "
                        "residual is predicted and actual put together"),
            "answer": "because the residual is the gap between predicted and actual",
            "board": '[[bars data="predicted:30 | actual:36" caption="the gap between them"]]',
        },
        "recap": [
            ("So, here it is again. A best-fit line predicts and the residual is how "
             "far the truth sits from the prediction — the gap between predicted and "
             "actual, low when the dot is above the line, high when below. Never hand "
             "back the score, and never add the two.",
             '[[bars data="predicted:30 | actual:36" caption="how far off the line"]]'),
            ("And that is what best fit keeps small.",
             '[[step eq="36 − 30 = 6"]]'),
        ],
        "bank": [
            {"a": 5, "b": 8, "op": "resd"},
            {"a": 41, "b": 44, "op": "resd"},
            {"a": 26, "b": 20, "op": "resd"},
            {"a": 11, "b": 20, "op": "resd"},
            {"a": 47, "b": 56, "op": "resd"},
            {"a": 38, "b": 26, "op": "resd"},
            {"a": 29, "b": 44, "op": "resd"},
            {"a": 26, "b": 8, "op": "resd"},
            {"a": 23, "b": 44, "op": "resd"},
            {"a": 23, "b": 47, "op": "resd"},
        ],
    },
    {
        "id": "ps-u3-through-the-middle-of-the-cloud",
        "course": "probstat", "unit": 3,
        "topic": "The line splits the cloud",
        "op": "sblw", "max_value": 20,
        "levels": ("abstract",),
        "symbols": ("above", "below"),
        "advance_line": "Three in a row, and you can say why — you've got it! Every dot is on one side or the other.",
        "why": [
            ("Why does the line run through the cloud? Here is a fact about the "
             "best-fit line that catches people out: it does not sit on top of the "
             "cloud, or underneath it. It runs THROUGH the middle, so dots end up on "
             "both sides — some above it, some below.",
             '[[goal text="Through the middle of the cloud"]]'),
        ],
        "picture": [
            ("Here is a scatter cloud with its best-fit line. Look at where the dots "
             "sit: some float above the line, some hang below it, and the line "
             "threads between them. Count the dots on one side, and the rest must be "
             "on the other.",
             '[[scatter points="(2,12),(4,22),(6,31),(8,41),(10,50),(12,62)" fit="true" caption="the line threads through the cloud — dots above it and dots below"]]'),
        ],
        "teach": [
            ("That is the method: take the side you know away from the whole. If 14 "
             "dots are plotted and none lands exactly on the line, every dot is "
             "either above or below. With 6 above, the other 8 must be below: 14 "
             "take away 6.",
             '[[tape parts="6 above|8 below" total="14 dots" caption="14 dots: 6 above the line, 8 below"]][[step eq="14 dots · 6 above"]][[step eq="14 − 6 = 8 below"]]'),
            ("Two answers to resist. 6 is the side you were already told about — the "
             "question asked for the other one. And 14 is every dot on the plot, both "
             "sides at once. Take the side you know away from the whole.",
             '[[step eq="8 ✓"]][[step eq="6 ✗ the side you were given · 14 ✗ all of them"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 18 dots with 16 above the line "
                        "leaves just 2 below.",
                        '[[tape parts="16 above|2 below" total="18 dots" caption="18 − 16 = 2 below"]][[step eq="18 − 16 = 2"]]'),
             "ask": {'a': 19, 'b': 4, 'op': 'sblw'}},
            {"worked": ("One more together. 18 dots, 6 above: 18 take away 6 — 12 sit "
                        "below.",
                        '[[tape parts="6 above|12 below" total="18 dots" caption="18 − 6 = 12 below"]][[step eq="18 − 6 = 12"]]'),
             "ask": {'a': 19, 'b': 13, 'op': 'sblw'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. With 14 dots and 6 "
                       "above the line, 8 sit below. Tap the reason why."),
            "choices": ("because every dot is on one side or the other | because the "
                        "same number sits on each side | because every dot on the plot "
                        "sits below the line"),
            "answer": "because every dot is on one side or the other",
            "board": '[[tape parts="6 above|8 below" total="14 dots" caption="one side or the other"]]',
        },
        "recap": [
            ("So, here it is again. The best-fit line runs through the middle of the "
             "cloud, so every dot is on one side or the other. Take the side you know "
             "away from the whole for the side you do not. Never hand back the side "
             "you were given, and never the whole cloud.",
             '[[scatter points="(2,12),(4,22),(6,31),(8,41),(10,50),(12,62)" fit="true" caption="through the middle of the cloud"]]'),
            ("And that is a line that splits the crowd.",
             '[[step eq="14 − 6 = 8"]]'),
        ],
        "bank": [
            {"a": 8, "b": 6, "op": "sblw"},
            {"a": 9, "b": 2, "op": "sblw"},
            {"a": 11, "b": 7, "op": "sblw"},
            {"a": 12, "b": 7, "op": "sblw"},
            {"a": 13, "b": 7, "op": "sblw"},
            {"a": 14, "b": 9, "op": "sblw"},
            {"a": 15, "b": 11, "op": "sblw"},
            {"a": 15, "b": 2, "op": "sblw"},
            {"a": 16, "b": 5, "op": "sblw"},
            {"a": 17, "b": 10, "op": "sblw"},
        ],
    },
]
LESSONS.extend(_PROBSTAT_U3)

# =============================================================================
# PROB & STATS UNIT 4 -- Collecting Data (build lr)
# The thread: THE ANSWER IS ONLY AS GOOD AS THE ASKING. Algebra II's samp
# scaled a sample up to a school; this unit asks whether the sample deserved
# to be scaled at all -- a sample built to match the group's own mix, the
# response rate as a warning light, the people a survey could never reach,
# and the price of accuracy: four times the people to halve the margin.
# =============================================================================
_PROBSTAT_U4 = [
    {
        "id": "ps-u4-a-sample-that-matches",
        "course": "probstat", "unit": 4,
        "topic": "Stratified samples",
        "op": "strf", "max_value": 90,
        "levels": ("abstract",),
        "symbols": ("mix", "share"),
        "advance_line": "Three in a row, and you can say why — you've got it! Keep the group's own mix inside the sample.",
        "why": [
            ("Why build the sample first? Algebra Two took a sample\'s answer and "
             "scaled it up to a whole school. That only works if the sample looks "
             "like the school. So this unit builds the sample before it asks anything "
             "— and the plainest way is to keep the same mix of people inside it.",
             '[[goal text="A sample that matches"]]'),
        ],
        "picture": [
            ("Here is a school as two bars, 40 girls and 60 boys, and under it a "
             "sample of 20 cut as a tape. Look at the cut: the tape is split the way "
             "the bars are, two-fifths girls and three-fifths boys. The sample is a "
             "small copy of the school.",
             '[[bars data="girls:40 | boys:60" caption="the school — 40 girls, 60 boys"]][[tape parts="8 girls|12 boys" total="sample of 20" caption="the sample of 20, cut the way the school is"]]'),
        ],
        "teach": [
            ("That is the method: take the share the group has and give the sample "
             "that same share. Girls are 40 of the 100, so a sample of 20 keeps two "
             "fifths girls — 20 times 40, divided by 100, is 8 girls, and the other 12 "
             "are boys.",
             '[[tape parts="8 girls|12 boys" total="sample of 20" caption="20 × 40 ÷ 100 = 8 girls"]][[step eq="20 × 40 ÷ 100 = 8 girls"]]'),
            ("The lazy move is splitting the sample down the middle — 10 and 10 — "
             "which only matches a school that really is half and half. And copying "
             "40 straight across asks for more girls than the sample holds. Work out "
             "the share, then take it.",
             '[[step eq="8 ✓"]][[step eq="10 ✗ half and half · 40 ✗ the school\'s own count"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 60 girls and 30 boys, a sample "
                        "of 24: girls are two-thirds of the school, so 24 times 60, "
                        "divided by 90 — 16 girls.",
                        '[[bars data="girls:60 | boys:30" caption="two-thirds girls"]][[tape parts="16 girls|8 boys" total="sample of 24" caption="24 × 60 ÷ 90 = 16 girls"]][[step eq="24 × 60 ÷ 90 = 16 girls"]]'),
             "ask": {'a': 60, 'b': 35, 'c': 38, 'op': 'strf'}},
            {"worked": ("One more together. 45 girls and 40 boys, a sample of 34: girls "
                        "are 45 of the 85, and 34 times 45 divided by 85 is 18 girls.",
                        '[[tape parts="18 girls|16 boys" total="sample of 34" caption="34 × 45 ÷ 85 = 18 girls"]][[step eq="34 × 45 ÷ 85 = 18 girls"]]'),
             "ask": {'a': 75, 'b': 30, 'c': 28, 'op': 'strf'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A school of 40 girls "
                       "and 60 boys gets a sample of 20 with 8 girls in it. Tap the reason "
                       "why."),
            "choices": ("because the sample keeps the school\'s own share of girls | "
                        "because every sample is split half and half | because the sample "
                        "copies the school\'s girl count"),
            "answer": "because the sample keeps the school\'s own share of girls",
            "board": '[[tape parts="8 girls|12 boys" total="sample of 20" caption="the school\'s mix, inside the sample"]]',
        },
        "recap": [
            ("So, here it is again. A sample should look like the group it comes "
             "from, so take the share the group has and give the sample that same "
             "share. Never split it half and half by habit, and never copy the "
             "group\'s own count into the sample.",
             '[[bars data="girls:40 | boys:60" caption="the school"]][[tape parts="8 girls|12 boys" total="sample of 20" caption="a sample that matches"]]'),
            ("And that is a sample you can trust.",
             '[[step eq="20 × 40 ÷ 100 = 8"]]'),
        ],
        "bank": [
            {"a": 20, "b": 80, "c": 10, "op": "strf"},
            {"a": 20, "b": 60, "c": 20, "op": "strf"},
            {"a": 45, "b": 30, "c": 10, "op": "strf"},
            {"a": 20, "b": 45, "c": 26, "op": "strf"},
            {"a": 60, "b": 30, "c": 12, "op": "strf"},
            {"a": 90, "b": 70, "c": 16, "op": "strf"},
            {"a": 50, "b": 90, "c": 28, "op": "strf"},
            {"a": 35, "b": 70, "c": 36, "op": "strf"},
            {"a": 90, "b": 75, "c": 22, "op": "strf"},
            {"a": 30, "b": 50, "c": 40, "op": "strf"},
        ],
    },
    {
        "id": "ps-u4-who-actually-answered",
        "course": "probstat", "unit": 4,
        "topic": "Response rate",
        "op": "resp", "max_value": 200,
        "levels": ("abstract",),
        "symbols": ("response rate", "percent"),
        "advance_line": "Three in a row, and you can say why — you've got it! Returned out of sent, as a percent.",
        "why": [
            ("Why count the answers? Sending a survey is not the same as getting "
             "answers. Of everyone you ask, only some reply — and the percent who do "
             "is called the response rate. It is the first number a statistician "
             "looks for, before believing a word of the results.",
             '[[goal text="Who actually answered"]]'),
        ],
        "picture": [
            ("Here are 60 surveys as a tape: 15 came back, and 45 stayed silent. "
             "Look at the two parts — the answers are the short piece, and the "
             "silence is three times as long. A survey that reports only the short "
             "piece is reporting a quarter of the story.",
             '[[tape parts="15 back|45 silent" total="60 sent" caption="60 went out — 15 came back, 45 stayed silent"]]'),
        ],
        "teach": [
            ("That is the method: work the rate out as any percent — returned out of "
             "sent. 15 back out of 60 sent is a quarter, so 25 percent. On the hundred "
             "square that is 25 cells filled: 25 of every 100 surveys came back, and "
             "75 did not.",
             '[[hundredgrid shaded="25" unit="percent" eq="15 of 60 → 25%" caption="25 of every 100 came back"]][[step eq="15 ÷ 60 = 25%"]]'),
            ("Why it matters: the silent ones may differ from the answerers. People "
             "with strong feelings reply; the contented shrug and bin it. So do not "
             "hand back 15, which is a count of surveys, or 45, which is how many "
             "stayed silent. The rate is the percent.",
             '[[step eq="25 ✓"]][[step eq="15 ✗ a count · 45 ✗ the silent ones"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 55 sent and 33 back: 33 out of "
                        "55 is 60 percent.",
                        '[[tape parts="33 back|22 silent" total="55 sent" caption="33 of 55 came back"]][[hundredgrid shaded="60" unit="percent" eq="33 of 55 → 60%" caption="60 of every 100"]][[step eq="33 ÷ 55 = 60%"]]'),
             "ask": {'a': 90, 'b': 72, 'op': 'resp'}},
            {"worked": ("One more together. 150 sent with 96 back: 96 out of 150 — 64 "
                        "percent.",
                        '[[hundredgrid shaded="64" unit="percent" eq="96 of 150 → 64%" caption="64 of every 100 came back"]][[step eq="96 ÷ 150 = 64%"]]'),
             "ask": {'a': 75, 'b': 54, 'op': 'resp'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 60 surveys went out, "
                       "15 came back, and the response rate is 25 percent. Tap the reason "
                       "why."),
            "choices": ("because the rate is the returned surveys out of the sent ones | "
                        "because the rate is the count that came back | because the rate "
                        "counts the surveys that stayed silent"),
            "answer": "because the rate is the returned surveys out of the sent ones",
            "board": '[[hundredgrid shaded="25" unit="percent" eq="15 of 60 → 25%" caption="returned out of sent"]]',
        },
        "recap": [
            ("So, here it is again. The response rate is the surveys that came back "
             "out of the surveys that went out, as a percent. A low one is a "
             "warning, because the silent may not think like the answerers. Never "
             "hand back a count, and never the silent ones.",
             '[[tape parts="15 back|45 silent" total="60 sent" caption="who actually answered"]]'),
            ("And that is the first number to check.",
             '[[step eq="15 ÷ 60 = 25%"]]'),
        ],
        "bank": [
            {"a": 20, "b": 2, "op": "resp"},
            {"a": 50, "b": 7, "op": "resp"},
            {"a": 40, "b": 8, "op": "resp"},
            {"a": 180, "b": 36, "op": "resp"},
            {"a": 150, "b": 39, "op": "resp"},
            {"a": 190, "b": 57, "op": "resp"},
            {"a": 150, "b": 54, "op": "resp"},
            {"a": 120, "b": 48, "op": "resp"},
            {"a": 175, "b": 77, "op": "resp"},
            {"a": 150, "b": 78, "op": "resp"},
        ],
    },
    {
        "id": "ps-u4-the-ones-you-never-asked",
        "course": "probstat", "unit": 4,
        "topic": "Bias and undercoverage",
        "op": "bias", "max_value": 400,
        "levels": ("abstract",),
        "symbols": ("biased", "chance"),
        "advance_line": "Three in a row, and you can say why — you've got it! Count everyone the survey could never reach.",
        "why": [
            ("Why can a well-run survey still be wrong? Because it asked the wrong "
             "crowd. Hand a lunch survey only to those eating in the cafeteria, and "
             "everyone who brings lunch from home is invisible — and they are the "
             "ones with the strongest opinions about school lunches.",
             '[[goal text="The ones you never asked"]]'),
        ],
        "picture": [
            ("Here is a school of 300 as a tape. The 120 in the cafeteria were handed "
             "the survey — that is the first part. Look at the rest of the tape: it "
             "is blank, because nobody there was ever asked. The blank part is the "
             "survey\'s blind spot.",
             '[[tape parts="120 asked|?" total="school of 300" caption="120 were handed the survey — the rest of the school never was"]]'),
        ],
        "teach": [
            ("That is the method: take the ones asked away from the whole school. 300 "
             "take away 120 leaves 180 who never had a chance of being handed the "
             "survey. Not 180 who said no — 180 who were never asked at all. A sample "
             "like that is called biased.",
             '[[tape parts="120 asked|180 never asked" total="school of 300" caption="300 − 120 = 180 never had a chance"]][[step eq="300 − 120 = 180"]]'),
            ("The cure is giving everyone a chance of being picked, usually at random. "
             "And notice which numbers do not answer the question: 120 is the crowd "
             "that WAS asked, and 300 is everybody, asked or not. The gap between them "
             "is the blind spot.",
             '[[step eq="180 ✓"]][[step eq="120 ✗ those asked · 300 ✗ everyone"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 90 asked at the school gate, out "
                        "of 250: 250 take away 90 — 160 never had a chance.",
                        '[[tape parts="90 asked|160 never asked" total="school of 250" caption="250 − 90 = 160"]][[step eq="250 − 90 = 160"]]'),
             "ask": {'a': 120, 'b': 320, 'op': 'bias'}},
            {"worked": ("One more together. 140 asked in a school of 360: 360 take away "
                        "140 — 220 never had a chance.",
                        '[[tape parts="140 asked|220 never asked" total="school of 360" caption="360 − 140 = 220"]][[step eq="360 − 140 = 220"]]'),
             "ask": {'a': 160, 'b': 400, 'op': 'bias'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A school of 300, a "
                       "survey handed to 120 in the cafeteria, and 180 never had a "
                       "chance. Tap the reason why."),
            "choices": ("because everyone outside the crowd asked was never reached | "
                        "because 180 of them refused to answer | because the whole "
                        "school was handed the survey"),
            "answer": "because everyone outside the crowd asked was never reached",
            "board": '[[tape parts="120 asked|180 never asked" total="school of 300" caption="the blind spot"]]',
        },
        "recap": [
            ("So, here it is again. A survey handed to one crowd can never hear from "
             "the rest, so take the ones asked away from the whole for the ones it "
             "could never reach — that sample is biased. Never hand back the crowd "
             "asked, and never everybody.",
             '[[tape parts="120 asked|180 never asked" total="school of 300" caption="the ones you never asked"]]'),
            ("And that is why everyone needs a chance.",
             '[[step eq="300 − 120 = 180"]]'),
        ],
        "bank": [
            {"a": 30, "b": 50, "op": "bias"},
            {"a": 40, "b": 70, "op": "bias"},
            {"a": 60, "b": 100, "op": "bias"},
            {"a": 50, "b": 105, "op": "bias"},
            {"a": 80, "b": 140, "op": "bias"},
            {"a": 75, "b": 145, "op": "bias"},
            {"a": 100, "b": 180, "op": "bias"},
            {"a": 95, "b": 185, "op": "bias"},
            {"a": 120, "b": 220, "op": "bias"},
            {"a": 110, "b": 230, "op": "bias"},
        ],
    },
    {
        "id": "ps-u4-the-price-of-accuracy",
        "course": "probstat", "unit": 4,
        "topic": "Sample size and margin of error",
        "op": "merr", "max_value": 1000,
        "levels": ("abstract",),
        "symbols": ("margin", "four times"),
        "advance_line": "Three in a row, and you can say why — you've got it! Four times the people for half the margin.",
        "why": [
            ("Why does accuracy cost so much? Every sample carries a margin of error "
             "— a give-or-take around its answer. Ask 60 people and you might report "
             "55 percent, give or take 12. Bigger samples give smaller margins, but "
             "not in the way most people expect.",
             '[[goal text="The price of accuracy"]]'),
        ],
        "picture": [
            ("Here is a machine that takes a headcount in and hands the bigger sample "
             "out. Look at its rule: times 4. That is what halving the margin costs — "
             "60 people go in, and four times as many come out. Not twice: four "
             "times.",
             '[[machine input="60" rule="× 4" output="240" caption="halving the margin — 60 people in, four times as many out"]]'),
        ],
        "teach": [
            ("That is the method: doubling the sample does NOT halve the margin. To "
             "halve it you need four times as many people, so 60 becomes 240. Want "
             "the margin halved again? Four times more still — 960 people to go from "
             "12 points to 3.",
             '[[bars data="sample:60 | halved once:240 | halved twice:960" caption="each halving of the margin needs four times the people"]][[step eq="60 × 4 = 240 halves it"]][[step eq="240 × 4 = 960 halves it again"]]'),
            ("That is why national surveys stop around a thousand people. Going "
             "further costs a fortune and buys very little. So the tap that says "
             "double — 120 — is the honest-looking wrong answer, and the margin itself "
             "is not a headcount at all.",
             '[[step eq="240 ✓"]][[step eq="120 ✗ doubling · 12 ✗ that is the margin"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. A sample of 45 needs four times "
                        "as many — 180 people — to halve its margin.",
                        '[[machine input="45" rule="× 4" output="180" caption="45 people × 4 = 180 people"]][[step eq="45 × 4 = 180"]]'),
             "ask": {'a': 110, 'b': 5, 'op': 'merr'}},
            {"worked": ("One more together. 250 people need four times as many — 1000 — "
                        "to halve the margin.",
                        '[[bars data="now:250 | four times:1000" caption="250 to 1000 — the margin halves"]][[step eq="250 × 4 = 1000"]]'),
             "ask": {'a': 190, 'b': 3, 'op': 'merr'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A sample of 60 "
                       "needs 240 people to halve its margin of error. Tap the reason "
                       "why."),
            "choices": ("because halving the margin takes four times the people | "
                        "because doubling the sample halves the margin | because the "
                        "margin itself is the number of people needed"),
            "answer": "because halving the margin takes four times the people",
            "board": '[[machine input="60" rule="× 4" output="240" caption="the price of half the margin — 60 people to 240"]]',
        },
        "recap": [
            ("So, here it is again. A sample\'s margin of error shrinks slowly: "
             "halving it costs four times the people, and halving it again costs four "
             "times more. Never double and expect half, and never hand back the "
             "margin as a headcount.",
             '[[machine input="60" rule="× 4" output="240" caption="the price of accuracy — 60 people to 240"]]'),
            ("And that is why a thousand is usually enough.",
             '[[step eq="60 × 4 = 240"]]'),
        ],
        "bank": [
            {"a": 25, "b": 3, "op": "merr"},
            {"a": 50, "b": 4, "op": "merr"},
            {"a": 75, "b": 6, "op": "merr"},
            {"a": 100, "b": 3, "op": "merr"},
            {"a": 125, "b": 5, "op": "merr"},
            {"a": 150, "b": 7, "op": "merr"},
            {"a": 175, "b": 4, "op": "merr"},
            {"a": 200, "b": 6, "op": "merr"},
            {"a": 225, "b": 3, "op": "merr"},
            {"a": 240, "b": 8, "op": "merr"},
        ],
    },
]
LESSONS.extend(_PROBSTAT_U4)
# =============================================================================
# PROB & STATS UNIT 5 -- Probability Basics (build ls)
# The thread: PUT A NUMBER ON A CHANCE. Geometry U9 counted chances ("a out of
# b"); this unit measures them on the 0-to-100 scale, then meets the two rules
# that combine them -- OR adds, AND times -- taught as a deliberate PAIR, each
# one the other's trap, and finishes by counting winning PATHS through two
# stages.
# ⭐ [[tree]] walked here. It prints every leaf's product, so it appears in
# teach beats only; ask boards carry the givens in words.
# =============================================================================
_PROBSTAT_U5 = [
    {
        "id": "ps-u5-chance-on-a-scale",
        "course": "probstat", "unit": 5,
        "topic": "Chance as a percent",
        "op": "ppct", "max_value": 90,
        "levels": ("abstract",),
        "symbols": ("percent", "chance"),
        "advance_line": "Three in a row, and you can say why — you've got it! A chance is a percent of the whole.",
        "why": [
            ("Why put chance on a scale? Geometry counted a chance: 3 red marbles out "
             "of 10 is 3 out of 10. That is true, but two chances counted out of "
             "different wholes cannot be compared. So probability puts every chance "
             "on ONE scale, from 0 to 100.",
             '[[goal text="Chance on a scale"]][[step eq="0 = never · 100 = always"]]'),
        ],
        "picture": [
            ("Here is the bag as two bars: 3 red marbles and 7 that are not red. "
             "Look at the red bar against the whole bag of 10 — it is a bit less than "
             "a third. The hundred square underneath turns that share into a number "
             "on the scale: 30 of every 100 picks would be red.",
             '[[bars data="red:3 | not red:7" caption="the bag — 3 red out of 10"]][[hundredgrid shaded="30" unit="percent" eq="3 of 10 → 30%" caption="30 of every 100 picks would be red"]]'),
        ],
        "teach": [
            ("That is the method: turn the count into a percent the ordinary way. 3 "
             "red out of 10 marbles is 3 divided by 10, then out of a hundred — 30 "
             "percent. Now it can sit beside any other chance in the world: a 30 "
             "percent chance of red, a 40 percent chance of rain.",
             '[[hundredgrid shaded="30" unit="percent" eq="3 of 10 → 30%" caption="3 divided by 10, out of a hundred"]][[step eq="3 ÷ 10 = 30%"]]'),
            ("The two ends anchor the scale: 0 percent never happens, 100 percent "
             "always does, and everything real lives between. So do not hand back 3, "
             "the count of red marbles, or 7, the count that is not red. The question "
             "asks for the percent.",
             '[[step eq="30 ✓"]][[step eq="3 ✗ a count · 7 ✗ the others"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 9 red out of 12 marbles: 9 "
                        "divided by 12 is 75 percent.",
                        '[[bars data="red:9 | not red:3" caption="9 red out of 12"]][[hundredgrid shaded="75" unit="percent" eq="9 of 12 → 75%" caption="75 of every 100"]][[step eq="9 ÷ 12 = 75%"]]'),
             "ask": {'a': 17, 'b': 20, 'op': 'ppct'}},
            {"worked": ("One more together. 7 out of 35 marbles: 7 divided by 35 — 20 "
                        "percent.",
                        '[[hundredgrid shaded="20" unit="percent" eq="7 of 35 → 20%" caption="20 of every 100 picks"]][[step eq="7 ÷ 35 = 20%"]]'),
             "ask": {'a': 16, 'b': 20, 'op': 'ppct'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A bag of 10 marbles "
                       "with 3 red gives a 30 percent chance of red. Tap the reason why."),
            "choices": ("because a chance is the red share, out of a hundred | because "
                        "the chance is the count of red marbles | because the chance is "
                        "the count that is not red"),
            "answer": "because a chance is the red share, out of a hundred",
            "board": '[[hundredgrid shaded="30" unit="percent" eq="3 of 10 → 30%" caption="chance on a scale"]]',
        },
        "recap": [
            ("So, here it is again. A chance is a percent of the whole, on one scale "
             "from 0, never, to 100, always — divide the count by the whole, then out "
             "of a hundred. Never hand back the count of red, and never the count "
             "that is not.",
             '[[hundredgrid shaded="30" unit="percent" eq="3 of 10 → 30%" caption="chance on a scale"]]'),
            ("And that is a chance you can compare with any other.",
             '[[step eq="3 ÷ 10 = 30%"]]'),
        ],
        "bank": [
            {"a": 2, "b": 20, "op": "ppct"},
            {"a": 8, "b": 50, "op": "ppct"},
            {"a": 11, "b": 50, "op": "ppct"},
            {"a": 9, "b": 36, "op": "ppct"},
            {"a": 12, "b": 40, "op": "ppct"},
            {"a": 2, "b": 5, "op": "ppct"},
            {"a": 21, "b": 50, "op": "ppct"},
            {"a": 27, "b": 50, "op": "ppct"},
            {"a": 15, "b": 25, "op": "ppct"},
            {"a": 26, "b": 40, "op": "ppct"},
        ],
    },
    {
        "id": "ps-u5-either-one-wins",
        "course": "probstat", "unit": 5,
        "topic": "The OR rule",
        "op": "por", "max_value": 27,
        "levels": ("abstract",),
        "symbols": ("or", "winners"),
        "advance_line": "Three in a row, and you can say why — you've got it! Two piles that cannot overlap simply join.",
        "why": [
            ("Why do chances join up? Because there are exactly two ways to want two "
             "things, and this is the first: either one will do. A bag of red, blue "
             "and green, where red OR blue wins — a marble cannot be both colours at "
             "once, so the winners are two piles side by side.",
             '[[goal text="Either one wins"]]'),
        ],
        "picture": [
            ("Here is the bag as three bars: 4 red, 3 blue and 5 green. Look at the "
             "red bar and the blue bar standing next to each other — those are the "
             "winners, and no marble is counted in both. The green bar is the losers.",
             '[[bars data="red:4 | blue:3 | green:5" caption="red 4, blue 3, green 5 — red OR blue wins"]]'),
        ],
        "teach": [
            ("That is the method: put the two piles together. 4 plus 3 is 7 winners "
             "out of the 12 marbles. That is the OR rule, and it works whenever the "
             "two things cannot happen together — one marble, one colour.",
             '[[tape parts="4 red|3 blue|5 green" total="12 marbles" caption="the red and blue parts side by side — 7 winners"]][[step eq="4 + 3 = 7 winners out of 12"]]'),
            ("Do not times them. 4 times 3 is 12, which would say every marble in the "
             "bag is a winner — and timesing belongs to the OTHER rule, the one for "
             "two separate events. Adding the green in as well counts marbles that "
             "lose.",
             '[[step eq="7 ✓"]][[step eq="12 ✗ timesed · 12 ✗ the whole bag"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 3 red, 6 blue and 2 green, with "
                        "red or blue winning: 3 plus 6 — 9 winners.",
                        '[[tape parts="3 red|6 blue|2 green" total="11 marbles" caption="red and blue together — 9 winners"]][[step eq="3 + 6 = 9 winners"]]'),
             "ask": {'a': 7, 'b': 9, 'c': 8, 'op': 'por'}},
            {"worked": ("One more together. 5 red and 2 blue among 4 green: 5 plus 2 — 7 "
                        "winners.",
                        '[[bars data="red:5 | blue:2 | green:4" caption="5 red and 2 blue — 7 winners"]][[step eq="5 + 2 = 7 winners"]]'),
             "ask": {'a': 6, 'b': 9, 'c': 6, 'op': 'por'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. With 4 red and 3 blue "
                       "in the bag and either colour winning, there are 7 winners. Tap the "
                       "reason why."),
            "choices": ("because a marble cannot be two colours, so the piles just join | "
                        "because either-or means timesing the two piles | because every "
                        "marble in the bag is a winner"),
            "answer": "because a marble cannot be two colours, so the piles just join",
            "board": '[[tape parts="4 red|3 blue|5 green" total="12 marbles" caption="either one wins"]]',
        },
        "recap": [
            ("So, here it is again. When either of two things will do and they cannot "
             "happen together, the winners are the two piles put together — the OR "
             "rule adds. Never times them, and never count the losers in.",
             '[[bars data="red:4 | blue:3 | green:5" caption="either one wins"]]'),
            ("And that is the first way chances join.",
             '[[step eq="4 + 3 = 7"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "c": 2, "op": "por"},
            {"a": 4, "b": 2, "c": 7, "op": "por"},
            {"a": 2, "b": 6, "c": 6, "op": "por"},
            {"a": 2, "b": 7, "c": 4, "op": "por"},
            {"a": 6, "b": 3, "c": 8, "op": "por"},
            {"a": 5, "b": 5, "c": 5, "op": "por"},
            {"a": 2, "b": 9, "c": 9, "op": "por"},
            {"a": 7, "b": 4, "c": 3, "op": "por"},
            {"a": 4, "b": 8, "c": 6, "op": "por"},
            {"a": 8, "b": 4, "c": 8, "op": "por"},
        ],
    },
    {
        "id": "ps-u5-both-at-once",
        "course": "probstat", "unit": 5,
        "topic": "The AND rule",
        "op": "pand", "max_value": 100,
        "levels": ("abstract",),
        "symbols": ("and", "rarer"),
        "advance_line": "Three in a row, and you can say why — you've got it! Wanting both leaves a chance rarer — times the two.",
        "why": [
            ("Why is wanting both so different? It is the second way chances join up: "
             "you want BOTH, and the two have nothing to do with each other. Rain "
             "tomorrow is one day in 5. A late bus is one bus in 3. Neither cares "
             "what the other does.",
             '[[goal text="Both at once"]]'),
        ],
        "picture": [
            ("Here are the two chances as two pies. The first is cut into 5, with one "
             "rainy slice; the second into 3, with one late slice. Look at how small "
             "each slice is on its own — and a rainy day WITH a late bus needs both "
             "slices to come up together.",
             '[[pie parts="5" shaded="1" caption="one day in 5 is rainy"]][[pie parts="3" shaded="1" caption="one bus in 3 is late"]]'),
        ],
        "teach": [
            ("That is the method: times the two chances. Of every 5 days one is "
             "rainy, and on that rainy day only one bus in 3 runs late. Lay the days "
             "against the buses as an array — 5 by 3 is 15 squares, and only one is "
             "rainy AND late. Both together turn up one time in 15.",
             '[[array rows="3" cols="5" caption="5 kinds of day by 3 kinds of bus — 15 squares, one of them rainy AND late"]][[step eq="1 in 5 × 1 in 3 → 1 in 15"]]'),
            ("Notice the direction: asking for both always leaves a chance rarer, so "
             "the answer must be a bigger one-in number than either you started with. "
             "One in 8 — adding them — is more common than rain alone, which cannot "
             "be right.",
             '[[step eq="1 in 15 ✓ rarer"]][[step eq="1 in 8 ✗ added · 1 in 5 ✗ the bus ignored"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. One in 5 and one in 6, with "
                        "nothing between them: 5 times 6 — one in 30.",
                        '[[array rows="5" cols="6" caption="5 by 6 — 30 squares, one of them both"]][[step eq="5 × 6 = 30"]]'),
             "ask": {'a': 10, 'b': 8, 'op': 'pand'}},
            {"worked": ("One more together. One in 7 and one in 11: 7 times 11 — one in "
                        "77.",
                        '[[array rows="7" cols="11" caption="7 by 11 — 77 squares, one of them both"]][[step eq="7 × 11 = 77"]]'),
             "ask": {'a': 6, 'b': 12, 'op': 'pand'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Rain is one day in 5, "
                       "a late bus is one in 3, and both at once is one in 15. Tap the "
                       "reason why."),
            "choices": ("because wanting both is rarer, so the two chances times together "
                        "| because wanting both adds the two chances | because the rarer "
                        "chance alone decides it"),
            "answer": "because wanting both is rarer, so the two chances times together",
            "board": '[[array rows="3" cols="5" caption="one square in 15"]]',
        },
        "recap": [
            ("So, here it is again. When you want both of two things that have nothing "
             "to do with each other, times the two chances — the answer is rarer than "
             "either. Never add them, and never ignore one of the two.",
             '[[pie parts="5" shaded="1" caption="one in 5"]][[pie parts="3" shaded="1" caption="one in 3 — both at once is one in 15"]]'),
            ("And that is the second way chances join.",
             '[[step eq="5 × 3 = 15"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "op": "pand"},
            {"a": 3, "b": 4, "op": "pand"},
            {"a": 2, "b": 8, "op": "pand"},
            {"a": 4, "b": 5, "op": "pand"},
            {"a": 2, "b": 12, "op": "pand"},
            {"a": 9, "b": 3, "op": "pand"},
            {"a": 4, "b": 8, "op": "pand"},
            {"a": 4, "b": 9, "op": "pand"},
            {"a": 6, "b": 7, "op": "pand"},
            {"a": 6, "b": 8, "op": "pand"},
        ],
    },
    {
        "id": "ps-u5-count-the-winning-paths",
        "course": "probstat", "unit": 5,
        "topic": "Two-stage outcomes",
        "op": "ptre", "max_value": 64,
        "levels": ("abstract",),
        "symbols": ("paths", "both"),
        "advance_line": "Three in a row, and you can say why — you've got it! Winners on the first spin, times winners on the second.",
        "why": [
            ("Why draw the paths? Draw the two rules as a picture and you get a tree: "
             "every first outcome branches into every second one, and each finished "
             "branch is one path through the whole experiment. A spinner spun twice "
             "is exactly that kind of picture.",
             '[[goal text="Count the winning paths"]]'),
        ],
        "picture": [
            ("Here is a spinner cut into 4 equal parts, 2 of them winners, and under "
             "it the tree for spinning it twice. Look at the branches: the first spin "
             "wins or loses, and each of those splits again for the second spin. Four "
             "finished paths, and every one is win-then-something or lose-then-something.",
             '[[pie parts="4" shaded="2" caption="4 equal parts, 2 winners"]][[tree stage1="W:2,L:2" stage2="W:2,L:2" caption="every path, stage by stage"]]'),
        ],
        "teach": [
            ("That is the method: count the paths that win BOTH times. Each of the 2 "
             "winning first spins can be followed by each of the 2 winning second "
             "spins. So 2 times 2 — four paths win twice, out of the 4 times 4, "
             "sixteen paths in all. That is the AND rule again, counted on a picture.",
             '[[tree stage1="W:2,L:2" stage2="W:2,L:2" caption="the win-then-win path counts 2 × 2"]][[step eq="2 × 2 = 4 winning paths of 16"]]'),
            ("Two miscounts. 2 times 4 is 8 — that counts winning FIRST and then "
             "anything at all, which is a different question. And 2 plus 2 treats two "
             "spins as though they were one longer spin. Winners times winners, "
             "always.",
             '[[step eq="4 ✓"]][[step eq="8 ✗ second spin left free · 4 ✗ added"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. A 12-part spinner with 9 "
                        "winners, spun twice: 9 times 9 — 81 paths win both times.",
                        '[[tree stage1="W:9,L:3" stage2="W:9,L:3" caption="win-then-win counts 9 × 9"]][[step eq="9 × 9 = 81 winning paths"]]'),
             "ask": {'a': 9, 'b': 8, 'op': 'ptre'}},
            {"worked": ("One more together. 11 parts with 10 winners: 10 times 10 — 100 "
                        "paths win twice.",
                        '[[pie parts="11" shaded="10" caption="11 parts, 10 winners"]][[tree stage1="W:10,L:1" stage2="W:10,L:1" caption="win-then-win counts 10 × 10"]][[step eq="10 × 10 = 100"]]'),
             "ask": {'a': 7, 'b': 4, 'op': 'ptre'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A 4-part spinner with "
                       "2 winners, spun twice, has 4 paths that win both times. Tap the "
                       "reason why."),
            "choices": ("because every winning first spin pairs with every winning second "
                        "| because the second spin can land anywhere | because two spins "
                        "add their winners together"),
            "answer": "because every winning first spin pairs with every winning second",
            "board": '[[tree stage1="W:2,L:2" stage2="W:2,L:2" caption="the winning paths"]]',
        },
        "recap": [
            ("So, here it is again. A two-stage experiment is a tree, and the paths "
             "that win both times are the winners of the first spin times the winners "
             "of the second. Never leave the second spin free, and never add the two "
             "spins.",
             '[[pie parts="4" shaded="2" caption="count the winning paths"]]'),
            ("And that is the AND rule, drawn.",
             '[[step eq="2 × 2 = 4"]]'),
        ],
        "bank": [
            {"a": 4, "b": 3, "op": "ptre"},
            {"a": 5, "b": 3, "op": "ptre"},
            {"a": 5, "b": 4, "op": "ptre"},
            {"a": 6, "b": 4, "op": "ptre"},
            {"a": 6, "b": 5, "op": "ptre"},
            {"a": 7, "b": 5, "op": "ptre"},
            {"a": 7, "b": 6, "op": "ptre"},
            {"a": 8, "b": 6, "op": "ptre"},
            {"a": 8, "b": 7, "op": "ptre"},
            {"a": 9, "b": 7, "op": "ptre"},
        ],
    },
]
LESSONS.extend(_PROBSTAT_U5)

# =============================================================================
# PROB & STATS UNIT 6 -- Conditional Probability & Independence (build ls)
# The thread: THE WORD "GIVEN" SHRINKS THE WORLD. First what you divide BY
# (conditioning changes the denominator), then the rate inside that smaller
# world, then what INDEPENDENT actually claims -- that the group's rate is the
# overall rate -- and finally the draw that changes the bag behind it.
# =============================================================================
_PROBSTAT_U6 = [
    {
        "id": "ps-u6-out-of-how-many-now",
        "course": "probstat", "unit": 6,
        "topic": "Conditioning changes the whole",
        "op": "cbse", "max_value": 40,
        "levels": ("abstract",),
        "symbols": ("among", "world"),
        "advance_line": "Three in a row, and you can say why — you've got it! Asking about one group shrinks the whole to that group.",
        "why": [
            ("Why does one small word change the whole? Unit Six turns on the word "
             "GIVEN. Ask \"what is the chance a student plays soccer?\" and the whole "
             "is the whole class. Ask it about the girls only, and the boys have just "
             "left the room — the whole is a different number.",
             '[[goal text="Out of how many now?"]]'),
        ],
        "picture": [
            ("Here is a class as four bars: 7 girls in soccer, 5 girls in art, 5 boys "
             "in soccer and 8 boys in art — 25 students. Look at the two girls\' "
             "bars standing on the left. Ask about the girls only and those two bars "
             "are the entire world; the boys\' bars do not count any more.",
             '[[bars data="girls soccer:7 | girls art:5 | boys soccer:5 | boys art:8" caption="four groups — asking about the girls keeps only the first two bars"]]'),
        ],
        "teach": [
            ("That is the method: the word GIVEN throws away everyone it does not "
             "mention. Among the girls only, the world has shrunk to 7 plus 5 — 12 "
             "girls — and every chance from here on is out of 12, not 25. The two-way "
             "table shows it: the girls\' row adds to 12.",
             '[[twoway rowlabels="girls,boys" collabels="soccer,art" data="7,5|5,8" caption="the girls\' row adds to 12 — that is the whole now"]][[step eq="among the girls: 7 + 5 = 12"]]'),
            ("Answering 25 keeps the boys who were just sent away. And 7 is the soccer "
             "girls themselves — the group you are counting, not the group you are "
             "counting out of. Read which group the question names, and add up that "
             "group.",
             '[[step eq="12 ✓"]][[step eq="25 ✗ everyone · 7 ✗ the cell"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 9 girls in soccer and 7 in art: "
                        "among the girls, everything is out of 9 plus 7 — 16.",
                        '[[twoway rowlabels="girls,boys" collabels="soccer,art" data="9,7|6,9" caption="the girls\' row adds to 16"]][[step eq="9 + 7 = 16 girls"]]'),
             "ask": {'a': 16, 'b': 18, 'c': 5, 'op': 'cbse'}},
            {"worked": ("One more together. 5 girls in soccer and 15 in art: 5 plus 15 — a "
                        "world of 20 girls.",
                        '[[bars data="girls soccer:5 | girls art:15" caption="the two girls\' bars — 20 girls"]][[step eq="5 + 15 = 20 girls"]]'),
             "ask": {'a': 14, 'b': 17, 'c': 8, 'op': 'cbse'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. In a class of 25 with "
                       "7 girls in soccer and 5 in art, a chance about the girls is out of "
                       "12. Tap the reason why."),
            "choices": ("because asking about the girls shrinks the whole to the girls | "
                        "because a chance is always out of the whole class | because the "
                        "whole is the soccer girls alone"),
            "answer": "because asking about the girls shrinks the whole to the girls",
            "board": '[[twoway rowlabels="girls,boys" collabels="soccer,art" data="7,5|5,8" caption="out of how many now?"]]',
        },
        "recap": [
            ("So, here it is again. A conditional chance names a group, and that group "
             "becomes the whole — add up the group named, and everyone else has left "
             "the room. Never keep the whole class, and never hand back the one cell "
             "you were counting.",
             '[[twoway rowlabels="girls,boys" collabels="soccer,art" data="7,5|5,8" caption="the girls\' row is the whole now"]]'),
            ("And that is what GIVEN does.",
             '[[step eq="7 + 5 = 12"]]'),
        ],
        "bank": [
            {"a": 2, "b": 2, "c": 2, "op": "cbse"},
            {"a": 6, "b": 4, "c": 13, "op": "cbse"},
            {"a": 8, "b": 5, "c": 10, "op": "cbse"},
            {"a": 13, "b": 2, "c": 7, "op": "cbse"},
            {"a": 14, "b": 3, "c": 4, "op": "cbse"},
            {"a": 10, "b": 9, "c": 15, "op": "cbse"},
            {"a": 3, "b": 18, "c": 12, "op": "cbse"},
            {"a": 11, "b": 11, "c": 9, "op": "cbse"},
            {"a": 19, "b": 4, "c": 6, "op": "cbse"},
            {"a": 12, "b": 13, "c": 3, "op": "cbse"},
        ],
    },
    {
        "id": "ps-u6-inside-the-smaller-world",
        "course": "probstat", "unit": 6,
        "topic": "The conditional rate",
        "op": "ccnt", "max_value": 80,
        "levels": ("abstract",),
        "symbols": ("among", "percent"),
        "advance_line": "Three in a row, and you can say why — you've got it! Divide inside the smaller world, not the big one.",
        "why": [
            ("Why work inside the smaller world? Once GIVEN has shrunk the whole, the "
             "chance is worked out the ordinary way — just inside the smaller group. "
             "Every girl in a class chose one club, and the question is asked among "
             "the girls, so the boys never enter the arithmetic at all.",
             '[[goal text="Inside the smaller world"]]'),
        ],
        "picture": [
            ("Here are the girls as two bars: 9 chose soccer and 6 chose art. Look at "
             "the soccer bar against both bars together — it is a bit more than half. "
             "The hundred square underneath turns that share into a percent: 60 of "
             "every 100 girls chose soccer.",
             '[[bars data="soccer:9 | art:6" caption="the girls — 9 soccer, 6 art"]][[hundredgrid shaded="60" unit="percent" eq="9 of 15 → 60%" caption="60 of every 100 girls chose soccer"]]'),
        ],
        "teach": [
            ("That is the method: add up the group, then divide inside it. 9 plus 6 is "
             "15 girls, and 9 of those chose soccer — 9 out of 15 is 60 percent. "
             "However many boys there are, they never enter the arithmetic, because "
             "the question already sent them away.",
             '[[hundredgrid shaded="60" unit="percent" eq="9 of 15 → 60%" caption="9 out of the 15 girls"]][[step eq="9 + 6 = 15"]][[step eq="9 ÷ 15 = 60%"]]'),
            ("Two answers not to give: 9 is a headcount, not a percent, and 40 percent "
             "is the art share — the rest of the girls. Read which group is being "
             "asked about, count that group, and divide inside it.",
             '[[step eq="60 ✓"]][[step eq="9 ✗ a count · 40 ✗ the other club"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 8 girls in soccer and 32 in art: "
                        "8 out of 40 is 20 percent.",
                        '[[bars data="soccer:8 | art:32" caption="8 of the 40 girls"]][[hundredgrid shaded="20" unit="percent" eq="8 of 40 → 20%" caption="20 of every 100"]][[step eq="8 ÷ 40 = 20%"]]'),
             "ask": {'a': 30, 'b': 10, 'op': 'ccnt'}},
            {"worked": ("One more together. 21 in soccer and 14 in art: 21 out of 35 — 60 "
                        "percent.",
                        '[[hundredgrid shaded="60" unit="percent" eq="21 of 35 → 60%" caption="60 of every 100 girls"]][[step eq="21 ÷ 35 = 60%"]]'),
             "ask": {'a': 14, 'b': 6, 'op': 'ccnt'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 9 girls chose soccer "
                       "and 6 chose art, so 60 percent of the girls chose soccer. Tap the "
                       "reason why."),
            "choices": ("because you divide by all the girls, not the class | because "
                        "the percent is the count of soccer girls | because the boys are "
                        "divided into the girls"),
            "answer": "because you divide by all the girls, not the class",
            "board": '[[hundredgrid shaded="60" unit="percent" eq="9 of 15 → 60%" caption="inside the smaller world"]]',
        },
        "recap": [
            ("So, here it is again. Inside the smaller world, a chance is worked out "
             "the ordinary way — the count you want, divided by the whole of the group "
             "named, as a percent. Never hand back the headcount, and never the other "
             "club\'s share.",
             '[[bars data="soccer:9 | art:6" caption="inside the smaller world"]]'),
            ("And that is a conditional rate.",
             '[[step eq="9 ÷ 15 = 60%"]]'),
        ],
        "bank": [
            {"a": 2, "b": 8, "op": "ccnt"},
            {"a": 6, "b": 19, "op": "ccnt"},
            {"a": 7, "b": 21, "op": "ccnt"},
            {"a": 6, "b": 14, "op": "ccnt"},
            {"a": 9, "b": 16, "op": "ccnt"},
            {"a": 12, "b": 18, "op": "ccnt"},
            {"a": 11, "b": 14, "op": "ccnt"},
            {"a": 24, "b": 26, "op": "ccnt"},
            {"a": 14, "b": 11, "op": "ccnt"},
            {"a": 12, "b": 8, "op": "ccnt"},
        ],
    },
    {
        "id": "ps-u6-what-independent-claims",
        "course": "probstat", "unit": 6,
        "topic": "Independence",
        "op": "indp", "max_value": 90,
        "levels": ("abstract",),
        "symbols": ("independent", "rate"),
        "advance_line": "Three in a row, and you can say why — you've got it! Independent means the group looks just like everyone.",
        "why": [
            ("Why is independence a claim? Two things are independent when knowing "
             "one tells you nothing about the other. That is a claim you can TEST, "
             "because it carries a promise: the group\'s rate should match the "
             "overall rate, exactly.",
             '[[goal text="What independent claims"]]'),
        ],
        "picture": [
            ("Here are two bars: the whole school, where 45 percent like maths, and "
             "beside it the left-handers. Look at the second bar — if left-handedness "
             "had nothing to do with liking maths, it would stand exactly as tall as "
             "the first. Independence promises a matching bar.",
             '[[bars data="whole school:45 | left-handers if independent:45" caption="percent who like maths — independence promises the same height"]]'),
        ],
        "teach": [
            ("That is the method: independence predicts the overall rate for every "
             "group. Say 45 percent of a school likes maths. If left-handedness were "
             "independent of liking maths, then 45 percent of the left-handers would "
             "like maths too — the same 45, whether there are 20 left-handers or 200.",
             '[[bars data="school:45 | if independent:45" caption="the group would look just like the school"]][[step eq="school 45% · if independent, left-handers 45%"]]'),
            ("Then you look. If the left-handers actually come in at 60 percent, the "
             "promise is broken and the two are NOT independent — something links "
             "them. The question asks what independence WOULD predict, so the "
             "measured 60 is not the answer, and the number of left-handers is not a "
             "rate at all.",
             '[[bars data="school:45 | if independent:45 | measured:60" caption="the measured bar breaks the promise"]][[step eq="45 ✓ what independence predicts"]][[step eq="60 ✗ what was measured"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 40 percent of a school walks to "
                        "school. If independence held, 40 percent of the bus-pass holders "
                        "would walk too.",
                        '[[bars data="school:40 | bus-pass holders if independent:40" caption="the same 40"]][[step eq="school 40% · any independent group 40%"]]'),
             "ask": {'a': 75, 'b': 55, 'c': 20, 'op': 'indp'}},
            {"worked": ("One more together. A school at 60 percent predicts 60 percent "
                        "inside any independent group.",
                        '[[bars data="school:60 | if independent:60" caption="school 60, group 60"]][[step eq="school 60% · group 60%"]]'),
             "ask": {'a': 85, 'b': 20, 'c': 65, 'op': 'indp'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 45 percent of a school "
                       "likes maths, so independence would put the left-handers at 45 "
                       "percent too. Tap the reason why."),
            "choices": ("because an independent group looks just like everyone | because "
                        "an independent group always scores higher | because the group\'s "
                        "headcount sets its rate"),
            "answer": "because an independent group looks just like everyone",
            "board": '[[bars data="school:45 | if independent:45" caption="what independent claims"]]',
        },
        "recap": [
            ("So, here it is again. Independent means the group\'s rate matches the "
             "overall rate, so independence predicts the school\'s own percent for "
             "any group — and a measured rate that differs breaks the claim. Never "
             "hand back the measured rate, and never a headcount.",
             '[[bars data="school:45 | if independent:45 | measured:60" caption="what independent claims"]]'),
            ("And that is a promise you can check.",
             '[[step eq="if independent: 45%"]]'),
        ],
        "bank": [
            {"a": 10, "b": 20, "c": 90, "op": "indp"},
            {"a": 15, "b": 40, "c": 85, "op": "indp"},
            {"a": 20, "b": 10, "c": 80, "op": "indp"},
            {"a": 25, "b": 60, "c": 75, "op": "indp"},
            {"a": 30, "b": 50, "c": 70, "op": "indp"},
            {"a": 40, "b": 30, "c": 90, "op": "indp"},
            {"a": 45, "b": 15, "c": 80, "op": "indp"},
            {"a": 50, "b": 25, "c": 20, "op": "indp"},
            {"a": 55, "b": 35, "c": 20, "op": "indp"},
            {"a": 65, "b": 45, "c": 20, "op": "indp"},
        ],
    },
    {
        "id": "ps-u6-the-bag-remembers",
        "course": "probstat", "unit": 6,
        "topic": "Without replacement",
        "op": "wout", "max_value": 40,
        "levels": ("abstract",),
        "symbols": ("kept", "smaller"),
        "advance_line": "Three in a row, and you can say why — you've got it! A marble kept out leaves a smaller bag behind.",
        "why": [
            ("Why does the bag remember? The last conditional idea is the most "
             "physical. Take a marble from a bag and put it back, and the second pick "
             "faces exactly the bag the first one did. Keep it instead, and the bag "
             "has changed — the second pick lives in a smaller world.",
             '[[goal text="The bag remembers"]]'),
        ],
        "picture": [
            ("Here is a bag of 10 as a tape, 4 red and 6 other. Now take one red out "
             "and keep it. Look at the second tape: the red part is shorter by one, "
             "and the whole tape is shorter too — 9 marbles, not 10. Both numbers "
             "moved.",
             '[[tape parts="4 red|6 other" total="10 marbles" caption="before — 4 red in a bag of 10"]][[tape parts="3 red|6 other" total="9 marbles" caption="after one red is kept — 3 red in a bag of 9"]]'),
        ],
        "teach": [
            ("That is the method: take the kept marble off the whole. 10 take away 1 "
             "leaves 9, so the next pick is out of 9. The reds moved too, 4 down to "
             "3, so the next chance of red is 3 out of 9 rather than 4 out of 10. The "
             "bottom number is what the question asks for.",
             '[[tape parts="3 red|6 other" total="9 marbles" caption="10 − 1 = 9 marbles for the next pick"]][[step eq="10 − 1 = 9"]][[step eq="4 of 10 → 3 of 9"]]'),
            ("Answering 10 is the slip worth naming — it treats the bag as though the "
             "marble went back. And 3 is the reds left over, the TOP of the new "
             "chance, not the bottom. One marble kept out, one smaller bag.",
             '[[step eq="9 ✓"]][[step eq="10 ✗ nothing taken · 3 ✗ that is the reds"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 25 marbles, one kept out: 25 take "
                        "away 1 — the next pick is out of 24.",
                        '[[tape parts="8 red|16 other" total="24 marbles" caption="25 − 1 = 24 left for the next pick"]][[step eq="25 − 1 = 24"]]'),
             "ask": {'a': 19, 'b': 39, 'op': 'wout'}},
            {"worked": ("One more together. A bag of 16 with one marble kept: 16 take away "
                        "1 leaves 15 for the next pick.",
                        '[[tape parts="4 red|11 other" total="15 marbles" caption="16 − 1 = 15"]][[step eq="16 − 1 = 15"]]'),
             "ask": {'a': 6, 'b': 38, 'op': 'wout'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A bag of 10 with 4 "
                       "red, one red taken and kept, and the next pick is out of 9. Tap "
                       "the reason why."),
            "choices": ("because a marble kept out leaves a smaller bag behind | because "
                        "the bag is the same until every red is gone | because the next "
                        "pick is out of the reds left"),
            "answer": "because a marble kept out leaves a smaller bag behind",
            "board": '[[tape parts="3 red|6 other" total="9 marbles" caption="the bag remembers"]]',
        },
        "recap": [
            ("So, here it is again. Without replacement, the bag remembers: a marble "
             "kept out leaves one fewer in the bag, so the next pick is out of a "
             "smaller whole, and the top of the chance shrinks too. Never keep the "
             "old bag, and never hand back the reds left as the whole.",
             '[[tape parts="3 red|6 other" total="9 marbles" caption="the bag remembers"]]'),
            ("And that is the second pick\'s world.",
             '[[step eq="10 − 1 = 9"]]'),
        ],
        "bank": [
            {"a": 3, "b": 5, "op": "wout"},
            {"a": 5, "b": 14, "op": "wout"},
            {"a": 6, "b": 18, "op": "wout"},
            {"a": 8, "b": 21, "op": "wout"},
            {"a": 20, "b": 23, "op": "wout"},
            {"a": 7, "b": 26, "op": "wout"},
            {"a": 9, "b": 28, "op": "wout"},
            {"a": 7, "b": 30, "op": "wout"},
            {"a": 28, "b": 31, "op": "wout"},
            {"a": 20, "b": 33, "op": "wout"},
        ],
    },
]
LESSONS.extend(_PROBSTAT_U6)
# =============================================================================
# PROB & STATS UNIT 7 -- Random Variables & Expected Value (build lt)
# The thread: WHAT IS ONE PLAY WORTH? alg2-u9's expv counted the payout of a
# run of plays; this unit builds the idea properly -- a distribution's chances
# must fill the hundred, a value is the payoffs WEIGHTED by how often they
# come, fairness is that idea run backwards, and the gap between what you pay
# and what comes back is why the machine is still standing there.
# =============================================================================
_PROBSTAT_U7 = [
    {
        "id": "ps-u7-the-chances-fill-the-hundred",
        "course": "probstat", "unit": 7,
        "topic": "A distribution adds to one whole",
        "op": "pdis", "max_value": 100,
        "levels": ("abstract",),
        "symbols": ("chances", "hundred"),
        "advance_line": "Three in a row, and you can say why — you've got it! The chances fill the hundred, and what is left is the last one.",
        "why": [
            ("Why should the chances add up to anything? Because something happens every "
             "single play. A prize machine gives small, medium or large, and there is no "
             "fourth door. So the chances of the three together have to fill the whole "
             "hundred — that is what a distribution is.",
             '[[goal text="The chances fill the hundred"]]'),
        ],
        "picture": [
            ("Here is the hundred square. Small comes up 25 times in every hundred plays, "
             "so 25 cells. Medium comes up 40 times — 40 more cells. Look at what is still "
             "white: every one of those cells is a play that must have been large.",
             '[[hundredgrid shaded="25" plus="40" unit="percent" caption="25 for small, 40 more for medium — the white cells are every play that was large"]]'),
        ],
        "teach": [
            ("That is the method: add the chances you know, and take them from 100. 25 plus "
             "40 is 65 accounted for, so large takes the 35 that are left. There is nowhere "
             "else for those plays to go.",
             '[[bars data="small:25 | medium:40 | large:35" caption="three prizes that fill the hundred — 25, 40 and 35"]][[step eq="100 − 25 − 40 = 35%"]]'),
            ("Answering 65 hands back the two you were given and forgets the very prize you "
             "were asked about. And 100 is all three together. The leftover is the answer.",
             '[[step eq="35 ✓"]][[step eq="65 ✗ the two given · 100 ✗ all of them"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 40 percent and 15 percent are spoken "
                        "for, so the third takes 45.",
                        '[[hundredgrid shaded="40" plus="15" unit="percent" caption="40 and 15 shaded — 45 cells still white"]][[step eq="100 − 40 − 15 = 45%"]]'),
             "ask": {"a": 10, "b": 30, "op": "pdis"}},
            {"worked": ("One more together. 20 and 25 make 45, so 100 take away 45 — 55 "
                        "percent for the last one.",
                        '[[bars data="small:20 | medium:25 | large:55" caption="20, 25 and the 55 left over"]][[step eq="100 − 20 − 25 = 55%"]]'),
             "ask": {"a": 10, "b": 35, "op": "pdis"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Small is 25 percent and "
                       "medium 40, so large is 35. Tap the reason why."),
            "choices": ("because the three chances have to fill the whole hundred | "
                        "because large is always the rarest prize | "
                        "because 25 and 40 average out to 35"),
            "answer": "because the three chances have to fill the whole hundred",
            "board": '[[hundredgrid shaded="25" plus="40" unit="percent" caption="why is the white part 35?"]]',
        },
        "recap": [
            ("So, here it is again. A distribution lists every outcome and its chance, and "
             "the chances fill the hundred because something happens every time. Add the "
             "ones you know, take them from 100, and the leftover is the missing one.",
             '[[hundredgrid shaded="25" plus="40" unit="percent" caption="the chances fill the hundred"]]'),
            ("And that is why a missing chance can always be found.",
             '[[step eq="100 − 25 − 40 = 35"]]'),
        ],
        "bank": [
            {"a": 30, "b": 60, "op": "pdis"},
            {"a": 60, "b": 30, "op": "pdis"},
            {"a": 50, "b": 35, "op": "pdis"},
            {"a": 35, "b": 45, "op": "pdis"},
            {"a": 15, "b": 60, "op": "pdis"},
            {"a": 45, "b": 30, "op": "pdis"},
            {"a": 20, "b": 50, "op": "pdis"},
            {"a": 50, "b": 20, "op": "pdis"},
            {"a": 20, "b": 45, "op": "pdis"},
            {"a": 55, "b": 10, "op": "pdis"},
        ],
    },
    {
        "id": "ps-u7-what-one-play-is-worth",
        "course": "probstat", "unit": 7,
        "topic": "Expected value",
        "op": "evwa", "max_value": 40,
        "levels": ("abstract",),
        "symbols": ("average", "often"),
        "advance_line": "Three in a row, and you can say why — you've got it! Weigh each payout by how often it comes.",
        "why": [
            ("Why would anyone want to know what one play is worth? Because the best prize "
             "is not what you usually get, and the worst is not either. A machine that pays "
             "20 tokens sometimes and 5 tokens most of the time is worth something in "
             "between — pulled toward whichever turns up more often.",
             '[[goal text="What one play is worth"]]'),
        ],
        "picture": [
            ("Here are a hundred plays on the hundred square. The 40 shaded cells are the "
             "plays that paid 20 tokens. The 60 white cells paid 5. Look how much more of "
             "the square is white — that is why the true value sits closer to 5 than to 20.",
             '[[hundredgrid shaded="40" unit="percent" caption="40 plays paid 20 tokens, 60 plays paid 5 — the small prize covers more of the square"]]'),
        ],
        "teach": [
            ("That is the method: count the tokens over a hundred plays, then share them "
             "out. 40 plays at 20 is 800, and 60 plays at 5 is 300 — 1100 tokens in all. "
             "Share 1100 across 100 plays and one play is worth 11. That is a weighted "
             "average: each prize weighed by how often it comes.",
             '[[bars data="40 plays × 20:800 | 60 plays × 5:300" caption="two piles of tokens — 800 and 300, 1100 together"]][[step eq="800 + 300 = 1100"]][[step eq="1100 ÷ 100 = 11 a play"]]'),
            ("The trap is averaging the two prizes and stopping. 20 and 5 average to 12 "
             "and a half, which is only right if both come up equally often — and they do "
             "not. And 20 alone is the big prize, not what a play is worth.",
             '[[step eq="11 ✓"]][[step eq="12 or 13 ✗ the prizes averaged · 20 ✗ the big prize"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 30 tokens 20 percent of the time and "
                        "5 tokens otherwise: 600 plus 400 over a hundred plays — 10 a play.",
                        '[[bars data="20 plays × 30:600 | 80 plays × 5:400" caption="600 and 400 — 1000 tokens across 100 plays"]][[step eq="600 + 400 = 1000"]][[step eq="1000 ÷ 100 = 10 a play"]]'),
             "ask": {"a": 22, "b": 12, "c": 10, "op": "evwa"}},
            {"worked": ("One more together. 25 tokens 40 percent of the time and 10 the rest: "
                        "1000 plus 600 over a hundred plays — 16 tokens a play.",
                        '[[bars data="40 plays × 25:1000 | 60 plays × 10:600" caption="1000 and 600 — 1600 tokens across 100 plays"]][[step eq="1000 + 600 = 1600"]][[step eq="1600 ÷ 100 = 16 a play"]]'),
             "ask": {"a": 22, "b": 12, "c": 20, "op": "evwa"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 20 tokens 40 percent of "
                       "the time and 5 the rest is worth 11 a play, not 12 and a half. Tap "
                       "the reason why."),
            "choices": ("because the small prize comes up more and pulls the value down | "
                        "because the big prize is what a play is worth | "
                        "because a machine never pays its average"),
            "answer": "because the small prize comes up more and pulls the value down",
            "board": '[[hundredgrid shaded="40" unit="percent" caption="why 11 and not 12 and a half?"]]',
        },
        "recap": [
            ("So, here it is again. What one play is worth is a weighted average: count the "
             "tokens over a hundred plays, then share them across the hundred. Each prize "
             "counts as often as it comes, so the one that comes up more pulls the value "
             "its way. Never average the prizes alone, and never take the big one.",
             '[[bars data="40 plays × 20:800 | 60 plays × 5:300" caption="weighed by how often each comes"]]'),
            ("And that is expected value.",
             '[[step eq="1100 ÷ 100 = 11"]]'),
        ],
        "bank": [
            {"a": 12, "b": 2, "c": 10, "op": "evwa"},
            {"a": 12, "b": 2, "c": 20, "op": "evwa"},
            {"a": 22, "b": 2, "c": 15, "op": "evwa"},
            {"a": 9, "b": 5, "c": 25, "op": "evwa"},
            {"a": 14, "b": 4, "c": 30, "op": "evwa"},
            {"a": 17, "b": 7, "c": 10, "op": "evwa"},
            {"a": 17, "b": 7, "c": 20, "op": "evwa"},
            {"a": 27, "b": 7, "c": 15, "op": "evwa"},
            {"a": 14, "b": 10, "c": 25, "op": "evwa"},
            {"a": 19, "b": 9, "c": 30, "op": "evwa"},
        ],
    },
    {
        "id": "ps-u7-what-would-be-fair",
        "course": "probstat", "unit": 7,
        "topic": "Fair games",
        "op": "fair", "max_value": 200,
        "levels": ("abstract",),
        "symbols": ("fair", "prize"),
        "advance_line": "Three in a row, and you can say why — you've got it! Spread the whole stake over the wins.",
        "why": [
            ("Why would you run expected value backwards? To design a game. A fair game is "
             "worth exactly what it costs — play it a thousand times and you end up level, "
             "neither up nor down. So the question turns around: what prize would make this "
             "game fair?",
             '[[goal text="What would be fair"]]'),
        ],
        "picture": [
            ("Here are a hundred plays. Every one of them costs 5 tokens, so that is 500 "
             "tokens paid in. Only the 20 shaded cells are wins. Look at those 20 cells: "
             "between them they have to hand the whole 500 back.",
             '[[hundredgrid shaded="20" unit="percent" caption="all 100 plays pay 5 tokens — only the 20 shaded ones win, and they must return the whole 500"]]'),
        ],
        "teach": [
            ("That is the method: work out the pot, then share it over the wins. 100 plays "
             "at 5 tokens is 500 in the pot. Shared over 20 wins, that is 25 tokens a "
             "prize. The rarer the win, the bigger the prize has to be.",
             '[[machine input="500" rule="÷ 20" output="25" caption="the pot of 500 shared over 20 wins — 25 tokens a prize"]][[step eq="500 ÷ 20 = 25"]]'),
            ("A prize of 5 — your money back — sounds fair and is not: you only collect it "
             "one play in five, and the other four are gone. And 20 is the percent of wins, "
             "not tokens at all.",
             '[[step eq="25 ✓"]][[step eq="5 ✗ just your stake · 20 ✗ that is the percent"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 6 tokens a play, winning a quarter "
                        "of the time: 600 over 25 wins — a fair prize of 24.",
                        '[[machine input="600" rule="÷ 25" output="24" caption="600 in the pot, 25 wins — 24 a prize"]][[step eq="600 ÷ 25 = 24"]]'),
             "ask": {"a": 12, "b": 15, "op": "fair"}},
            {"worked": ("One more together. 8 tokens a play, winning 40 percent of the time: "
                        "800 over 40 — 20 tokens.",
                        '[[machine input="800" rule="÷ 40" output="20" caption="800 in the pot, 40 wins — 20 a prize"]][[step eq="800 ÷ 40 = 20"]]'),
             "ask": {"a": 7, "b": 10, "op": "fair"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. At 5 tokens a play and a "
                       "win one time in five, the fair prize is 25, not 5. Tap the reason why."),
            "choices": ("because every play pays in but only the wins pay out | "
                        "because a prize is always five times the stake | "
                        "because 5 tokens is too small to be a prize"),
            "answer": "because every play pays in but only the wins pay out",
            "board": '[[hundredgrid shaded="20" unit="percent" caption="why 25 and not 5?"]]',
        },
        "recap": [
            ("So, here it is again. A fair game returns exactly what it takes in. Every "
             "play pays into the pot, only the wins pay out of it, so the fair prize is the "
             "whole pot shared over the wins. Your stake back is not fair, and the percent "
             "is not a prize.",
             '[[machine input="500" rule="÷ 20" output="25" caption="the pot shared over the wins"]]'),
            ("And that is how a game is designed.",
             '[[step eq="500 ÷ 20 = 25"]]'),
        ],
        "bank": [
            {"a": 2, "b": 50, "op": "fair"},
            {"a": 3, "b": 30, "op": "fair"},
            {"a": 3, "b": 20, "op": "fair"},
            {"a": 3, "b": 15, "op": "fair"},
            {"a": 10, "b": 50, "op": "fair"},
            {"a": 13, "b": 50, "op": "fair"},
            {"a": 15, "b": 50, "op": "fair"},
            {"a": 9, "b": 25, "op": "fair"},
            {"a": 10, "b": 25, "op": "fair"},
            {"a": 9, "b": 20, "op": "fair"},
        ],
    },
    {
        "id": "ps-u7-why-the-machine-stays-open",
        "course": "probstat", "unit": 7,
        "topic": "The long-run cost",
        "op": "hedg", "max_value": 60,
        "levels": ("abstract",),
        "symbols": ("long run", "back"),
        "advance_line": "Three in a row, and you can say why — you've got it! Paid out take away paid back — that is the real cost.",
        "why": [
            ("Why is the machine still standing there? Because real games are not fair, "
             "and the gap is the whole business. You pay a fixed price each play, and "
             "expected value says what comes back on average. The difference is what a "
             "play really costs you in the long run, and it is small on purpose.",
             '[[goal text="Why the machine stays open"]]'),
        ],
        "picture": [
            ("Here are the two numbers as bars. The tall one is what you pay: 10 tokens, "
             "every play. The shorter one is what comes back on average: 7. Look at the "
             "gap between the tops of the bars — that gap is the real cost of a play.",
             '[[bars data="you pay:10 | comes back:7" caption="10 out, 7 back on average — the gap between the bars is what a play really costs"]]'),
        ],
        "teach": [
            ("That is the method: take what comes back away from what you pay. 10 take "
             "away 7 is 3 — each play quietly costs 3 tokens. Play once and you might walk "
             "away up; play four hundred times and the 3 arrives with perfect reliability.",
             '[[tape parts="7 back|3 gone" total="10 paid" caption="of the 10 you pay, 7 comes back and 3 is gone for good"]][[step eq="10 − 7 = 3 a play"]]'),
            ("Keep the two numbers apart. 7 is what comes back, not what it costs. And "
             "adding them is nothing at all — no play ever costs you 17.",
             '[[step eq="3 ✓"]][[step eq="7 ✗ what comes back · 17 ✗ added"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Pay 20, get 13 back on average: 7 "
                        "tokens a play, gone.",
                        '[[tape parts="13 back|7 gone" total="20 paid" caption="13 back, 7 gone"]][[step eq="20 − 13 = 7"]]'),
             "ask": {"a": 15, "b": 9, "op": "hedg"}},
            {"worked": ("One more together. Pay 30 and get 22 back: 30 take away 22 — each "
                        "play costs 8.",
                        '[[bars data="you pay:30 | comes back:22" caption="30 out, 22 back — a gap of 8"]][[step eq="30 − 22 = 8"]]'),
             "ask": {"a": 16, "b": 14, "op": "hedg"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Pay 10 and get 7 back on "
                       "average, and a play really costs 3. Tap the reason why."),
            "choices": ("because what comes back is taken away from what you pay | "
                        "because the machine keeps every token you put in | "
                        "because 10 and 7 are added together"),
            "answer": "because what comes back is taken away from what you pay",
            "board": '[[bars data="you pay:10 | comes back:7" caption="why does a play cost 3?"]]',
        },
        "recap": [
            ("So, here it is again. A play costs what you pay take away what comes back on "
             "average. The gap hides in any single play and shows up over hundreds — that "
             "is the business model. What comes back is not the cost, and adding the two "
             "means nothing.",
             '[[bars data="you pay:10 | comes back:7" caption="the gap is the real cost"]]'),
            ("And that is why the machine stays open.",
             '[[step eq="10 − 7 = 3"]]'),
        ],
        "bank": [
            {"a": 5, "b": 3, "op": "hedg"},
            {"a": 6, "b": 4, "op": "hedg"},
            {"a": 7, "b": 4, "op": "hedg"},
            {"a": 8, "b": 3, "op": "hedg"},
            {"a": 9, "b": 5, "op": "hedg"},
            {"a": 10, "b": 4, "op": "hedg"},
            {"a": 11, "b": 9, "op": "hedg"},
            {"a": 12, "b": 9, "op": "hedg"},
            {"a": 13, "b": 8, "op": "hedg"},
            {"a": 14, "b": 10, "op": "hedg"},
        ],
    },
]
LESSONS.extend(_PROBSTAT_U7)

# =============================================================================
# PROB & STATS UNIT 8 -- The Normal Distribution (build lt)
# The thread: ONE CURVE FITS SO MUCH OF THE WORLD, and it comes with a ruler.
# How many sit in the crowded middle, how far out a value really is once you
# count in standard deviations, which value sits that far out, and how few
# people live in the tails.
# ⭐ [[normal]] walked here -- the LAST unused renderer. It labels the axis at
# every standard deviation, so it is teach-only throughout.
# =============================================================================
_PROBSTAT_U8 = [
    {
        "id": "ps-u8-the-crowded-middle",
        "course": "probstat", "unit": 8,
        "topic": "The 68 percent rule",
        "op": "n68", "max_value": 800,
        "levels": ("abstract",),
        "symbols": ("bell curve", "standard deviation"),
        "advance_line": "Three in a row, and you can say why — you've got it! About 68 in every hundred sit in the middle band.",
        "why": [
            ("Why does one curve matter so much? Measure almost anything about a big group "
             "— heights, test scores, how long the walk to school takes — and the picture "
             "comes out the same shape every time. Crowded in the middle, thin at both "
             "ends. Once you know the shape, you know how a group is spread out before you "
             "count it.",
             '[[goal text="The crowded middle"]]'),
        ],
        "picture": [
            ("Here is the bell curve, with the middle at 100 and a spread of 10. The shaded "
             "band runs from 90 to 110 — one standard deviation each way. Look how much of "
             "the curve sits under that band: about 68 of every hundred.",
             '[[normal mean="100" sd="10" lo="90" hi="110" caption="the middle band, one deviation each way — about 68 of every 100 sit inside it"]]'),
        ],
        "teach": [
            ("That is the method: the bell always shares itself out the same way, so 68 "
             "percent of any group sits in the middle band. In a school of 200, 68 percent "
             "is 136 — that many sit no further than one deviation from the average height.",
             '[[hundredgrid shaded="68" unit="percent" eq="68% of 200 → 136" caption="68 of every 100 — and 68 percent of 200 is 136"]][[step eq="68% of 200 = 136"]]'),
            ("The 68 is a percent and never a headcount, so answering 68 counts nobody. "
             "And 200 is everybody — middle and ends together. Take the percent of the "
             "group, and that is the middle band.",
             '[[step eq="136 ✓"]][[step eq="68 ✗ a percent · 200 ✗ everyone"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. In a group of 300, 68 percent is 204 "
                        "in the middle band.",
                        '[[hundredgrid shaded="68" unit="percent" eq="68% of 300 → 204" caption="68 percent of 300 is 204"]][[step eq="68% of 300 = 204"]]'),
             "ask": {"a": 725, "b": 0, "op": "n68"}},
            {"worked": ("One more together. Out of 900: 68 percent of 900 is 612, sitting no "
                        "further than one standard deviation out.",
                        '[[normal mean="100" sd="10" lo="90" hi="110" caption="the middle band of 900 holds 612"]][[step eq="68% of 900 = 612"]]'),
             "ask": {"a": 675, "b": 0, "op": "n68"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. In a group of 200, "
                       "about 136 sit in the middle band. Tap the reason why."),
            "choices": ("because the bell always keeps about 68 percent inside one deviation | "
                        "because 136 people is the size of the middle band everywhere | "
                        "because the ends of the bell hold the most people"),
            "answer": "because the bell always keeps about 68 percent inside one deviation",
            "board": '[[normal mean="100" sd="10" lo="90" hi="110" caption="why 136 of 200?"]]',
        },
        "recap": [
            ("So, here it is again. A bell curve is crowded in the middle, and it always "
             "shares itself out the same way: about 68 percent sit inside one standard "
             "deviation of the mean. Take 68 percent of the group and that is the middle "
             "band — the 68 is never a headcount, and the whole group is never the answer.",
             '[[normal mean="100" sd="10" lo="90" hi="110" caption="68 of every 100, in the middle band"]]'),
            ("And that is the 68 percent rule.",
             '[[step eq="68% of 200 = 136"]]'),
        ],
        "bank": [
            {"a": 50, "b": 0, "op": "n68"},
            {"a": 125, "b": 0, "op": "n68"},
            {"a": 175, "b": 0, "op": "n68"},
            {"a": 225, "b": 0, "op": "n68"},
            {"a": 275, "b": 0, "op": "n68"},
            {"a": 325, "b": 0, "op": "n68"},
            {"a": 375, "b": 0, "op": "n68"},
            {"a": 425, "b": 0, "op": "n68"},
            {"a": 475, "b": 0, "op": "n68"},
            {"a": 525, "b": 0, "op": "n68"},
        ],
    },
    {
        "id": "ps-u8-how-far-out-is-that",
        "course": "probstat", "unit": 8,
        "topic": "Counting standard deviations",
        "op": "zsco", "max_value": 100,
        "levels": ("abstract",),
        "symbols": ("deviations", "above"),
        "advance_line": "Three in a row, and you can say why — you've got it! Measure the gap in deviations, not in raw units.",
        "why": [
            ("Why is a score of 82 impressive, or not? You cannot say until you know the "
             "middle and the spread. 82 in a class averaging 70 is one thing; 82 in a "
             "class averaging 80 is another. So the bell curve measures every distance in "
             "its own unit: standard deviations from the mean.",
             '[[goal text="How far out is that?"]]'),
        ],
        "picture": [
            ("Here is a number line with the mean at 70 and the score at 82. One standard "
             "deviation is 6, so a step of 6 is the ruler. Look at the gap between the two "
             "dots — it holds two steps of 6, one after the other.",
             '[[numberline min="64" max="88" points="70,82" hops="70,76,82" caption="from the mean at 70 to 82 is two hops of 6"]]'),
        ],
        "teach": [
            ("That is the method: find the raw gap, then count how many deviations fit in "
             "it. 82 take away 70 is 12, and 12 holds two sixes — so 82 sits two deviations "
             "above the mean. Roughly 2 people in a hundred beat that, which is why it is "
             "impressive.",
             '[[numberline min="64" max="88" points="70,82" hops="70,76,82" caption="12 holds two sixes"]][[step eq="82 − 70 = 12"]][[step eq="12 ÷ 6 = 2 deviations"]]'),
            ("Answering 12 stops at the raw gap and never asks how big a step is — 12 "
             "points might be enormous or nothing at all, depending on the spread. And 6 "
             "is one step, not the count of them.",
             '[[step eq="2 ✓"]][[step eq="12 ✗ the raw gap · 6 ✗ one step"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Mean 80, deviation 7, value 94: the "
                        "gap is 14, which holds two sevens — 2 deviations.",
                        '[[numberline min="73" max="101" points="80,94" hops="80,87,94" caption="two hops of 7 from 80 reach 94"]][[step eq="14 ÷ 7 = 2 deviations"]]'),
             "ask": {"a": 60, "b": 2, "c": 66, "op": "zsco"}},
            {"worked": ("One more together. Mean 90, deviation 8, value 114: a gap of 24 — 3 "
                        "deviations out.",
                        '[[numberline min="82" max="122" points="90,114" hops="90,98,106,114" caption="three hops of 8 from 90 reach 114"]][[step eq="24 ÷ 8 = 3 deviations"]]'),
             "ask": {"a": 65, "b": 3, "c": 71, "op": "zsco"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. With a mean of 70 and a "
                       "deviation of 6, a score of 82 sits two deviations out, not 12. Tap "
                       "the reason why."),
            "choices": ("because the gap is measured in steps of the deviation | "
                        "because 12 is too big a number to be a distance | "
                        "because every score sits exactly two deviations out"),
            "answer": "because the gap is measured in steps of the deviation",
            "board": '[[numberline min="64" max="88" points="70,82" caption="why two, and not 12?"]]',
        },
        "recap": [
            ("So, here it is again. To say how far out a value is, find the raw gap from "
             "the mean and count how many standard deviations fit inside it. The raw gap "
             "alone says nothing, and one deviation is the ruler, not the answer. Counting "
             "steps is what lets a height and a test score be compared at all.",
             '[[numberline min="64" max="88" points="70,82" hops="70,76,82" caption="count the steps, not the units"]]'),
            ("And that is a standard score.",
             '[[step eq="12 ÷ 6 = 2"]]'),
        ],
        "bank": [
            {"a": 10, "b": 2, "c": 16, "op": "zsco"},
            {"a": 15, "b": 3, "c": 21, "op": "zsco"},
            {"a": 20, "b": 4, "c": 28, "op": "zsco"},
            {"a": 25, "b": 4, "c": 37, "op": "zsco"},
            {"a": 30, "b": 5, "c": 40, "op": "zsco"},
            {"a": 35, "b": 2, "c": 41, "op": "zsco"},
            {"a": 40, "b": 3, "c": 46, "op": "zsco"},
            {"a": 45, "b": 4, "c": 53, "op": "zsco"},
            {"a": 50, "b": 4, "c": 62, "op": "zsco"},
            {"a": 55, "b": 5, "c": 65, "op": "zsco"},
        ],
    },
    {
        "id": "ps-u8-which-value-sits-out-there",
        "course": "probstat", "unit": 8,
        "topic": "Reading the curve backwards",
        "op": "zval", "max_value": 140,
        "levels": ("abstract",),
        "symbols": ("mean", "two"),
        "advance_line": "Three in a row, and you can say why — you've got it! Two steps of the deviation, starting from the mean.",
        "why": [
            ("Why run the ruler the other way? Because sometimes the question is not how "
             "far out a value is, but which value sits at a named distance. Two standard "
             "deviations above the mean, say — the line that only about 2 people in a "
             "hundred ever reach. Name that value and you have named the rare ones.",
             '[[goal text="Which value sits out there?"]]'),
        ],
        "picture": [
            ("Here is the number line with the mean at 50 and a deviation of 8. Watch the "
             "hops: one hop of 8 lands on 58, and a second hop of 8 lands on 66. Look where "
             "the second hop ends — that is the value two deviations out.",
             '[[numberline min="42" max="74" points="50,66" hops="50,58,66" caption="two hops of 8 from the mean at 50 land on 66"]]'),
        ],
        "teach": [
            ("That is the method: two deviations is the deviation twice, and the distance "
             "starts from the mean. 8 twice is 16, and 50 plus 16 is 66. Everything above "
             "66 is the rare top sliver of the curve.",
             '[[numberline min="42" max="74" points="50,66" hops="50,58,66" caption="8 twice is 16, and 50 plus 16 is 66"]][[step eq="50 + 2 × 8 = 66"]]'),
            ("Two slips. Adding one 8 gives 58, which is only one deviation out. And "
             "answering 16 gives the distance while forgetting to start from 50 — a "
             "distance is not a value. Two steps, always beginning at the mean.",
             '[[step eq="66 ✓"]][[step eq="58 ✗ one deviation · 16 ✗ the distance alone"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Mean 70, deviation 9: two deviations "
                        "is 18, so the value is 88.",
                        '[[numberline min="61" max="97" points="70,88" hops="70,79,88" caption="two hops of 9 from 70 land on 88"]][[step eq="70 + 18 = 88"]]'),
             "ask": {"a": 60, "b": 2, "op": "zval"}},
            {"worked": ("One more together. Mean 80, deviation 7: two deviations is 14, so "
                        "the value is 80 plus 14 — 94.",
                        '[[numberline min="73" max="101" points="80,94" hops="80,87,94" caption="two hops of 7 from 80 land on 94"]][[step eq="80 + 14 = 94"]]'),
             "ask": {"a": 65, "b": 3, "op": "zval"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Mean 50, deviation 8, "
                       "and the value two deviations up is 66, not 58. Tap the reason why."),
            "choices": ("because two deviations means two hops of 8 from the mean | "
                        "because 58 is below the mean | "
                        "because the deviation is always added twice to itself"),
            "answer": "because two deviations means two hops of 8 from the mean",
            "board": '[[numberline min="42" max="74" points="50" hops="50,58" caption="why 66, and not 58?"]]',
        },
        "recap": [
            ("So, here it is again. To find the value a named distance out, take that many "
             "hops of the deviation, always starting from the mean. One hop is one "
             "deviation, and the distance alone is not a value until it leaves from the "
             "middle.",
             '[[numberline min="42" max="74" points="50,66" hops="50,58,66" caption="two hops from the mean"]]'),
            ("And that is reading the curve backwards.",
             '[[step eq="50 + 2 × 8 = 66"]]'),
        ],
        "bank": [
            {"a": 10, "b": 2, "op": "zval"},
            {"a": 15, "b": 3, "op": "zval"},
            {"a": 20, "b": 4, "op": "zval"},
            {"a": 25, "b": 5, "op": "zval"},
            {"a": 30, "b": 6, "op": "zval"},
            {"a": 35, "b": 2, "op": "zval"},
            {"a": 40, "b": 3, "op": "zval"},
            {"a": 45, "b": 4, "op": "zval"},
            {"a": 50, "b": 5, "op": "zval"},
            {"a": 55, "b": 6, "op": "zval"},
        ],
    },
    {
        "id": "ps-u8-almost-nobody-out-there",
        "course": "probstat", "unit": 8,
        "topic": "The tails",
        "op": "ntal", "max_value": 800,
        "levels": ("abstract",),
        "symbols": ("ends", "outside"),
        "advance_line": "Three in a row, and you can say why — you've got it! Half of the leftover five percent lives at each end.",
        "why": [
            ("Why does rare really mean rare? Because the bell keeps sharing itself out the "
             "same way. About 68 percent sit inside one deviation, about 95 inside two — "
             "which leaves just 5 percent outside two deviations, in all. And that 5 is "
             "split between the two ends.",
             '[[goal text="Almost nobody out there"]]'),
        ],
        "picture": [
            ("Here is the bell with the middle at 100 and a spread of 10. The shaded part "
             "is the top end — everything beyond two deviations, past 120. Look how thin "
             "that sliver is. The same sliver sits at the bottom end, below 80.",
             '[[normal mean="100" sd="10" lo="120" hi="140" caption="the top end — the sliver beyond two deviations, about 2 or 3 of every 100"]]'),
        ],
        "teach": [
            ("That is the method: take 5 percent of the group for both ends, then halve it "
             "for one. In a group of 800, 5 percent is 40 out at the ends — so 20 sit above "
             "two deviations and 20 below. The bell is symmetric, so the split is even.",
             '[[tape parts="20 bottom end|760 middle|20 top end" total="800 in all" caption="the two ends hold 40 between them — 20 at each"]][[step eq="5% of 800 = 40 · half at each end = 20"]]'),
            ("Forgetting the split is the slip — 40 counts both ends when the question "
             "asked for one. And a bell never has half its people out at the edges; that is "
             "what the shape is telling you.",
             '[[step eq="20 ✓"]][[step eq="40 ✗ both ends · 400 ✗ half the group"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Out of 1000, 5 percent is 50 at the "
                        "ends — so 25 sit above two deviations.",
                        '[[tape parts="25 bottom end|950 middle|25 top end" total="1000 in all" caption="50 at the ends — 25 at each"]][[step eq="50 ÷ 2 = 25 above"]]'),
             "ask": {"a": 600, "b": 0, "op": "ntal"}},
            {"worked": ("One more together. In a group of 2000: 5 percent is 100 at the ends, "
                        "so 50 sit beyond two deviations at the top.",
                        '[[tape parts="50 bottom end|1900 middle|50 top end" total="2000 in all" caption="100 at the ends — 50 at each"]][[step eq="2000 ÷ 40 = 50"]]'),
             "ask": {"a": 560, "b": 0, "op": "ntal"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. In a group of 800, "
                       "about 20 sit beyond two deviations at the top, not 40. Tap the "
                       "reason why."),
            "choices": ("because the 5 percent outside is shared between two ends | "
                        "because the top end is always exactly 20 people | "
                        "because 40 is more than 5 percent of the group"),
            "answer": "because the 5 percent outside is shared between two ends",
            "board": '[[normal mean="100" sd="10" lo="120" hi="140" caption="why 20, and not 40?"]]',
        },
        "recap": [
            ("So, here it is again. Beyond two deviations lives just 5 percent of a bell "
             "curve, and the two ends share it evenly. Take 5 percent of the group, then "
             "halve it for one end. Both ends together is not one end, and the edges are "
             "never half the group.",
             '[[normal mean="100" sd="10" lo="120" hi="140" caption="the thin top sliver"]]'),
            ("And that is why a value two deviations out is worth remarking on.",
             '[[step eq="800 ÷ 40 = 20"]]'),
        ],
        "bank": [
            {"a": 80, "b": 0, "op": "ntal"},
            {"a": 120, "b": 0, "op": "ntal"},
            {"a": 160, "b": 0, "op": "ntal"},
            {"a": 200, "b": 0, "op": "ntal"},
            {"a": 240, "b": 0, "op": "ntal"},
            {"a": 280, "b": 0, "op": "ntal"},
            {"a": 320, "b": 0, "op": "ntal"},
            {"a": 360, "b": 0, "op": "ntal"},
            {"a": 400, "b": 0, "op": "ntal"},
            {"a": 440, "b": 0, "op": "ntal"},
        ],
    },
]
LESSONS.extend(_PROBSTAT_U8)
# =============================================================================
# PROB & STATS UNIT 9 -- Sampling & Inference (build lu) -- ⭐ COURSE COMPLETE
# The thread: A SAMPLE ANSWERS WITH A RANGE, NEVER A POINT. Unit 4 built the
# sample; this one reports it honestly -- the low end, the width of the whole
# range, whether somebody else's claim can survive inside it, and what the
# range means once it is carried back onto real people.
# =============================================================================
_PROBSTAT_U9 = [
    {
        "id": "ps-u9-give-or-take",
        "course": "probstat", "unit": 9,
        "topic": "The low end of an estimate",
        "op": "cint", "max_value": 100,
        "levels": ("abstract",),
        "symbols": ("poll", "give or take"),
        "advance_line": "Three in a row, and you can say why — you've got it! The margin steps down as well as up.",
        "why": [
            ("A poll says give or take because a sample never knows the exact answer. An "
             "honest poll reports a range instead: 46 percent, give or take 5. That "
             "give-or-take is the margin of error from Unit Four, and it turns one number "
             "into a band the truth could be hiding in.",
             '[[goal text="Give or take"]]'),
        ],
        "picture": [
            ("Here is the estimate, 46, on a number line. Watch the hop: 5 down from 46 "
             "lands on 41. The same hop up would land on 51. Look at the two ends — the "
             "band reaches the same distance each way, and 41 is its floor.",
             '[[numberline min="36" max="56" points="41,46,51" hops="46,41" caption="one step of 5 down from 46 lands on 41 — the low end of the band"]]'),
        ],
        "teach": [
            ("That is the method: asked for the lowest the truth might be, take the margin "
             "off the estimate. 46 take away 5 is 41. So this poll is really saying: "
             "somewhere between 41 and 51, and we cannot narrow it with the people we "
             "asked.",
             '[[numberline min="36" max="56" points="41,46,51" hops="46,41" caption="46 take away 5 is 41 — the floor of the band"]][[step eq="46 − 5 = 41"]][[step eq="46 + 5 = 51"]]'),
            ("Answering 51 gives the highest — the same step in the other direction. And 5 "
             "on its own is just the size of the step, not a percent anybody claimed.",
             '[[step eq="41 ✓"]][[step eq="51 ✗ the high end · 5 ✗ the step"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 62 percent give or take 9: the low "
                        "end is 62 take away 9 — 53.",
                        '[[numberline min="44" max="80" points="53,62,71" hops="62,53" caption="a step of 9 down from 62 lands on 53"]][[step eq="62 − 9 = 53"]]'),
             "ask": {"a": 20, "b": 2, "op": "cint"}},
            {"worked": ("One more together. 75 percent give or take 6: 75 take away 6 — it "
                        "reaches down to 69.",
                        '[[numberline min="63" max="87" points="69,75,81" hops="75,69" caption="a step of 6 down from 75 lands on 69"]][[step eq="75 − 6 = 69"]]'),
             "ask": {"a": 22, "b": 3, "op": "cint"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 46 percent give or take "
                       "5 reaches down to 41. Tap the reason why."),
            "choices": ("because the margin steps the same distance down as up | "
                        "because a poll always rounds its answer down | "
                        "because 41 is the smallest percent a poll can report"),
            "answer": "because the margin steps the same distance down as up",
            "board": '[[numberline min="36" max="56" points="46" caption="why 41?"]]',
        },
        "recap": [
            ("So, here it is again. A poll reports a range, not a point, and the margin "
             "reaches the same distance each way from the estimate. The low end is the "
             "estimate take away the margin; the high end is the same step up. The margin "
             "alone is only the size of the step.",
             '[[numberline min="36" max="56" points="41,46,51" hops="46,41" caption="the margin steps down as well as up"]]'),
            ("And that is what give or take means.",
             '[[step eq="46 − 5 = 41"]]'),
        ],
        "bank": [
            {"a": 20, "b": 12, "op": "cint"},
            {"a": 21, "b": 12, "op": "cint"},
            {"a": 22, "b": 12, "op": "cint"},
            {"a": 23, "b": 12, "op": "cint"},
            {"a": 20, "b": 8, "op": "cint"},
            {"a": 24, "b": 11, "op": "cint"},
            {"a": 25, "b": 11, "op": "cint"},
            {"a": 27, "b": 12, "op": "cint"},
            {"a": 28, "b": 12, "op": "cint"},
            {"a": 21, "b": 4, "op": "cint"},
        ],
    },
    {
        "id": "ps-u9-how-wide-is-the-doubt",
        "course": "probstat", "unit": 9,
        "topic": "The width of the range",
        "op": "cwid", "max_value": 100,
        "levels": ("abstract",),
        "symbols": ("range", "doubt"),
        "advance_line": "Three in a row, and you can say why — you've got it! The margin counts twice — once each way.",
        "why": [
            ("Why is a margin of 4 not as tight as it sounds? Because the margin points "
             "both ways at once. It is only the trip from the middle to one edge, so the "
             "range a poll really covers is wider than its margin — twice as wide.",
             '[[goal text="How wide is the doubt"]]'),
        ],
        "picture": [
            ("Here is the doubt as a tape. 50 percent give or take 4: one part reaches 4 "
             "down, to 46, and the other reaches 4 up, to 54. Look at the whole tape from "
             "end to end — it is the two parts together, 8 points across.",
             '[[tape parts="4 down|4 up" total="8 points wide" caption="4 down to 46 and 4 up to 54 — the whole range is 8 points across"]]'),
        ],
        "teach": [
            ("That is the method: the whole range is the margin counted twice, once each "
             "way. 4 down plus 4 up is 8 points wide, from 46 to 54 — exactly the way an "
             "ellipse's width was double its reach.",
             '[[numberline min="42" max="58" points="46,50,54" caption="from 46 to 54 — 8 points, with 50 in the middle"]][[step eq="4 + 4 = 8 points wide"]]'),
            ("Answering 4 gives one side only. And 50 is the middle of the range, not its "
             "size. Edge to edge, it is the margin doubled.",
             '[[step eq="8 ✓"]][[step eq="4 ✗ one side · 50 ✗ the middle"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 40 percent give or take 12 covers 24 "
                        "points, from 28 up to 52.",
                        '[[tape parts="12 down|12 up" total="24 points wide" caption="12 and 12 — from 28 to 52 is 24 across"]][[step eq="12 × 2 = 24 points wide"]]'),
             "ask": {"a": 21, "b": 12, "op": "cwid"}},
            {"worked": ("One more together. A margin of 15, doubled, opens a range 30 points "
                        "wide.",
                        '[[tape parts="15 down|15 up" total="30 points wide" caption="15 and 15 — 30 across"]][[step eq="15 × 2 = 30"]]'),
             "ask": {"a": 22, "b": 13, "op": "cwid"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 50 percent give or take "
                       "4 covers a range 8 points wide, not 4. Tap the reason why."),
            "choices": ("because the margin reaches both down and up from the middle | "
                        "because a range is always twice the estimate | "
                        "because 4 points is too narrow for any poll"),
            "answer": "because the margin reaches both down and up from the middle",
            "board": '[[tape parts="4 down|4 up" total="?" caption="why 8, and not 4?"]]',
        },
        "recap": [
            ("So, here it is again. A margin is the trip from the middle to one edge, and "
             "the doubt reaches both ways, so the whole range is the margin doubled. One "
             "side is not the width, and the middle is not the size.",
             '[[tape parts="4 down|4 up" total="8 points wide" caption="the margin counts twice"]]'),
            ("And that is how wide the doubt is.",
             '[[step eq="4 × 2 = 8"]]'),
        ],
        "bank": [
            {"a": 21, "b": 2, "op": "cwid"},
            {"a": 22, "b": 3, "op": "cwid"},
            {"a": 23, "b": 4, "op": "cwid"},
            {"a": 24, "b": 5, "op": "cwid"},
            {"a": 25, "b": 6, "op": "cwid"},
            {"a": 21, "b": 7, "op": "cwid"},
            {"a": 22, "b": 8, "op": "cwid"},
            {"a": 23, "b": 9, "op": "cwid"},
            {"a": 24, "b": 10, "op": "cwid"},
            {"a": 25, "b": 11, "op": "cwid"},
        ],
    },
    {
        "id": "ps-u9-can-that-claim-survive",
        "course": "probstat", "unit": 9,
        "topic": "Testing a claim",
        "op": "inci", "max_value": 95,
        "levels": ("abstract",),
        "symbols": ("claim", "range"),
        "advance_line": "Three in a row, and you can say why — you've got it! Measure from the edge of your range, not its middle.",
        "why": [
            ("Why build a range at all? Here is what it is for. Somebody claims a number; "
             "your sample disagrees. Whether that is a real disagreement depends on one "
             "thing — can their claim fit inside your range at all?",
             '[[goal text="Can that claim survive?"]]'),
        ],
        "picture": [
            ("Here are three dots on one line. Your estimate, 40. Your ceiling, 46 — the "
             "very most your range allows, 40 plus 6. And a company's claim, 55. Look at "
             "the gap between the ceiling and the claim: that is the disagreement.",
             '[[numberline min="32" max="58" points="40,46,55" hops="46,55" caption="from your ceiling at 46 to their claim at 55 is a gap of 9"]]'),
        ],
        "teach": [
            ("That is the method. Measure from the EDGE, not the middle. Your range tops out "
             "at 46, and 55 take away 46 is 9 — the claim sits 9 points past the very best "
             "your data can support. Your sample flatly contradicts it.",
             '[[numberline min="32" max="58" points="40,46,55" hops="46,55" caption="from the ceiling at 46 to the claim at 55 is 9"]][[step eq="46 is your ceiling"]][[step eq="55 − 46 = 9 points past"]]'),
            ("Measuring from 40 gives 15 and pretends your estimate is exact, when the "
             "whole point of a range is that it is not. And the margin 6 is the size of "
             "your doubt, not the size of the disagreement.",
             '[[step eq="9 ✓"]][[step eq="15 ✗ measured from the middle · 6 ✗ the margin"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 30 percent give or take 4 tops out at "
                        "34, and a claim of 45 sits 11 points past it.",
                        '[[numberline min="24" max="48" points="30,34,45" hops="34,45" caption="from the ceiling at 34 to the claim at 45 is 11"]][[step eq="45 − 34 = 11 points past"]]'),
             "ask": {"a": 20, "b": 2, "c": 34, "op": "inci"}},
            {"worked": ("One more together. A ceiling of 50 with a claim of 58: 58 take away "
                        "50 — 8 points outside.",
                        '[[numberline min="44" max="62" points="50,58" hops="50,58" caption="from 50 to 58 is 8"]][[step eq="58 − 50 = 8"]]'),
             "ask": {"a": 21, "b": 2, "c": 36, "op": "inci"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. With a ceiling of 46 "
                       "and a claim of 55, the disagreement is 9 points, not 15. Tap the "
                       "reason why."),
            "choices": ("because the gap starts at the edge of the range | "
                        "because a claim is always measured from zero | "
                        "because 15 is bigger than the margin"),
            "answer": "because the gap starts at the edge of the range",
            "board": '[[numberline min="32" max="58" points="40,46,55" caption="why 9, and not 15?"]]',
        },
        "recap": [
            ("So, here it is again. A range is for testing claims: find your ceiling — the "
             "estimate plus the margin — and measure from there, not from the middle. A "
             "claim past the ceiling is a claim your data cannot support, and the margin "
             "is the size of your doubt, not the size of the disagreement.",
             '[[numberline min="32" max="58" points="40,46,55" hops="46,55" caption="measure from the edge"]]'),
            ("And that is how a claim gets tested.",
             '[[step eq="55 − 46 = 9"]]'),
        ],
        "bank": [
            {"a": 24, "b": 3, "c": 29, "op": "inci"},
            {"a": 25, "b": 2, "c": 30, "op": "inci"},
            {"a": 26, "b": 2, "c": 32, "op": "inci"},
            {"a": 27, "b": 2, "c": 34, "op": "inci"},
            {"a": 20, "b": 2, "c": 28, "op": "inci"},
            {"a": 21, "b": 2, "c": 30, "op": "inci"},
            {"a": 24, "b": 2, "c": 34, "op": "inci"},
            {"a": 25, "b": 2, "c": 36, "op": "inci"},
            {"a": 26, "b": 2, "c": 38, "op": "inci"},
            {"a": 27, "b": 2, "c": 40, "op": "inci"},
        ],
    },
    {
        "id": "ps-u9-the-range-in-real-people",
        "course": "probstat", "unit": 9,
        "topic": "Carrying a range to the population",
        "op": "npop", "max_value": 1000,
        "levels": ("abstract",),
        "symbols": ("low end", "students"),
        "advance_line": "Three in a row, and you can say why — you've got it! Take the low end FIRST, then count the people.",
        "why": [
            ("Why carry the doubt along? Algebra Two scaled a sample's answer up to a whole "
             "school. Now do it honestly: a sample's range becomes a range of people, and "
             "a sample that does not know exactly should never be reported as though it "
             "did.",
             '[[goal text="The range in real people"]]'),
        ],
        "picture": [
            ("Here are three percents as bars: the low end 20, the estimate 30, the high "
             "end 40 — a sample of the 400 students in a school, give or take 10. Look at the shortest "
             "bar. That is the one to carry onto the people first.",
             '[[bars data="low end:20 | estimate:30 | high end:40" caption="20, 30 and 40 percent — the low end is the bar to take first, of a school of 400"]]'),
        ],
        "teach": [
            ("That is the method: take the low end of the percents first, then count the "
             "people. The low end is 20 percent, and 20 percent of 400 is 80. The high end, "
             "40 percent, gives 160 — so somewhere between 80 and 160 walk.",
             '[[machine input="400" rule="× 20%" output="80" caption="the whole school of 400 goes in, the low end\'s 20 percent comes out — 80"]][[step eq="20% of 400 = 80"]]'),
            ("The order matters. Using 30 percent gives 120 and quietly drops the doubt. "
             "And 160 is the high end, the other edge of the range.",
             '[[step eq="80 ✓"]][[step eq="120 ✗ the margin dropped · 160 ✗ the high end"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 45 percent of 600 give or take 5: "
                        "the low end is 40 percent — 240.",
                        '[[machine input="600" rule="× 40%" output="240" caption="600 in, the low end\'s 40 percent out — 240"]][[step eq="40% of 600 = 240"]]'),
             "ask": {"a": 30, "b": 5, "c": 400, "op": "npop"}},
            {"worked": ("One more together. 55 percent of 800 give or take 15 reaches down to "
                        "40 percent — 320.",
                        '[[bars data="low end:40 | estimate:55 | high end:70" caption="40, 55 and 70 percent of 800 — the low end first"]][[step eq="40% of 800 = 320"]]'),
             "ask": {"a": 20, "b": 5, "c": 700, "op": "npop"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 30 percent of 400, give "
                       "or take 10, is at least 80, not 120. Tap the reason why."),
            "choices": ("because the low end of the percents is taken before counting people | "
                        "because 80 is the smallest number a sample can give | "
                        "because a school of 400 always has 80 walkers"),
            "answer": "because the low end of the percents is taken before counting people",
            "board": '[[bars data="low end:20 | estimate:30 | high end:40" caption="why 80, and not 120?"]]',
        },
        "recap": [
            ("So, here it is again. A sample's range becomes a range of people: take the "
             "low end of the percents first, then count. Using the estimate alone drops "
             "the doubt, and the high end is the other edge.",
             '[[bars data="low end:20 | estimate:30 | high end:40" caption="the low end first, then the people"]]'),
            ("And that is a range carried onto real people.",
             '[[step eq="20% of 400 = 80"]]'),
        ],
        "bank": [
            {"a": 20, "b": 10, "c": 200, "op": "npop"},
            {"a": 20, "b": 5, "c": 200, "op": "npop"},
            {"a": 20, "b": 10, "c": 400, "op": "npop"},
            {"a": 20, "b": 5, "c": 300, "op": "npop"},
            {"a": 20, "b": 10, "c": 500, "op": "npop"},
            {"a": 20, "b": 5, "c": 400, "op": "npop"},
            {"a": 40, "b": 5, "c": 200, "op": "npop"},
            {"a": 20, "b": 5, "c": 500, "op": "npop"},
            {"a": 50, "b": 10, "c": 200, "op": "npop"},
            {"a": 35, "b": 5, "c": 300, "op": "npop"},
        ],
    },
]
LESSONS.extend(_PROBSTAT_U9)

# ---- this course's slice of COURSE_ORDER: the teaching order (lessons/__init__.py joins the ten) ----
ORDER = [

    # ---- PROBABILITY & STATISTICS (build lq) -- ⭐ THE TENTH COURSE OPENS ----
    # Unit 1: Exploring Data
    "ps-u1-under-the-tallest-stack", "ps-u1-count-the-ones-above",
    "ps-u1-add-the-bars", "ps-u1-the-one-that-sits-alone",
    # Unit 2: Describing Distributions
    "ps-u2-no-single-middle", "ps-u2-the-middle-half",
    "ps-u2-how-far-from-the-middle", "ps-u2-a-percent-not-a-person",
    # Unit 3: Scatterplots & Correlation (build lr)
    "ps-u3-one-dot-two-numbers", "ps-u3-the-slope-is-a-rate",
    "ps-u3-how-far-off-the-line", "ps-u3-through-the-middle-of-the-cloud",
    # Unit 4: Collecting Data (build lr)
    "ps-u4-a-sample-that-matches", "ps-u4-who-actually-answered",
    "ps-u4-the-ones-you-never-asked", "ps-u4-the-price-of-accuracy",
    # Unit 5: Probability Basics (build ls)
    "ps-u5-chance-on-a-scale", "ps-u5-either-one-wins",
    "ps-u5-both-at-once", "ps-u5-count-the-winning-paths",
    # Unit 6: Conditional Probability & Independence (build ls)
    "ps-u6-out-of-how-many-now", "ps-u6-inside-the-smaller-world",
    "ps-u6-what-independent-claims", "ps-u6-the-bag-remembers",
    # Unit 7: Random Variables & Expected Value (build lt)
    "ps-u7-the-chances-fill-the-hundred", "ps-u7-what-one-play-is-worth",
    "ps-u7-what-would-be-fair", "ps-u7-why-the-machine-stays-open",
    # Unit 8: The Normal Distribution (build lt)
    "ps-u8-the-crowded-middle", "ps-u8-how-far-out-is-that",
    "ps-u8-which-value-sits-out-there", "ps-u8-almost-nobody-out-there",
    # Unit 9: Sampling & Inference (build lu) -- ⭐ PROB & STATS COMPLETE
    "ps-u9-give-or-take", "ps-u9-how-wide-is-the-doubt",
    "ps-u9-can-that-claim-survive", "ps-u9-the-range-in-real-people",
]

# I did no harm and this file is not truncated.
