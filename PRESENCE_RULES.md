# Mr. Cadabra — the presence rules

Companion to `RULES.md`. That file governs what he **says**. This one governs when he
**appears**, what he **does**, and when he must do nothing at all.

Written 31 August 2026, from the character study in `static/mockup/cadabra-pencil.html`
and the motion rig in `static/mockup/cadabra-playground.html`. Deployed since build rh
(1 September); section G added 2 September (build rr) for Jim's behaviour list. The
bench for trying any of it on the real layer is `/static/cadabra-lab.html`.

The whole document exists to protect one thing: **a child in the middle of a problem.**
Every rule below is downstream of that.

---

## A. WHO HE IS, AND WHO HE IS NOT

### 1. HE IS A PERSON. ABRABOT IS A MACHINE.
Mr. Cadabra teaches. Abrabot drills and proctors. That difference must be visible in one
glance, before a single word is read.

### 2. THE DIFFERENCE IS FREEDOM, NOT COLOUR.
Mr. Cadabra floats and can go anywhere on the page. Abrabot stays in his box. A child
learns who is who from behaviour faster than from a palette, and behaviour survives bad
lighting and colour-blindness. Yellow versus cyan is the second signal, not the first.

### 3. THEY ARE NEVER BOTH LOOSE ON THE SAME SCREEN.
If Abrabot is present and boxed, Mr. Cadabra either is not there or is parked and silent.
Two floating characters is a cartoon; one floating and one boxed is a classroom.

### 4. HE OWNS NO WAND AND PERFORMS NO MAGIC.
The hat is a hat. Nothing appears in a puff. The only trick he ever performs is that the
child suddenly understands. This survives from the 28 August study and does not reopen.

---

## B. WHEN HE APPEARS

### 5. HE MOVES WHEN THE CHILD IS NOT WORKING.
The governing rule. While an answer field has focus, or a timed question is running, he
parks and goes still — blink only. Movement is a reward or a transition. It is never
company for a child mid-problem.

### 6. HE TALKS STILL, AND MOVES SILENT.
Motion and speech at the same time makes children track the motion and lose the words.
He may drift while idle and gesture while still, but a line that matters is delivered
from a stationary character.

### 7. HE ARRIVES ONCE PER PAGE, NOT ONCE PER SECTION.
One entrance. After that he is furniture that occasionally acts. A character who
re-introduces himself is a pop-up.

### 8. HE OPENS A LESSON, NOT A PAGE LOAD.
The joke, the greeting and the tour belong to the start of a *lesson*. Navigating back to
a page the child was already on does not re-trigger any of them.

### 9. HE NEVER BLOCKS THE START.
The opening joke plays *while* the lesson loads and any click skips it. If the lesson is
ready and he is not finished, he stops talking. The child's time is not his.

### 10. THE TOUR IS ONCE, ON THE FIRST LESSON, AND SKIPPABLE.
After that it is available on request and never volunteered. An on-demand "where do I
click?" is worth more than an unprompted tour, and costs less goodwill.

---

## C. WHAT HE DOES

### 11. CELEBRATION IS TIERED, AND THE TOP TIER IS RARE.
Three levels, and they do not drift upward:

| Tier | Fires on | What he does |
|---|---|---|
| 1 | any correct answer | a blink and a small bob, under one second |
| 2 | a streak of three | arms up, a couple of bounces, a few sparkles |
| 3 | the hard one, or a first-time-got-it | he flies over and underlines it in his own graphite |

If every right answer gets a performance, by the sixth problem it is wallpaper and by the
twelfth it is irritating. Reserve the big one and it stays big.

### 12. THE UNDERLINE IS THE ONE THAT MEANS SOMETHING.
It says *this is the part that mattered*, in his handwriting, drawn with his own point.
It is the only behaviour that carries information rather than mood. Spend it accordingly:
at most once per lesson unless the child earns another.

### 13. HE POINTS AT THE NEAR EDGE OF A THING, STANDING BESIDE IT.
Pointing at the middle of a wide panel from across the page reads as a vague wave. He
comes close, and the finger lands on the edge nearest him.

### 14. HE WRITES WITH HIMSELF. HE NEVER HOLDS A TOOL.
No pen, no pointer, no chalk. He leans and his own tip leaves the line. This is the best
thing the pencil idea gave us and it is not to be traded away for convenience.

### 15. HIS MARKS ARE CLEARED WHEN THE PROBLEM IS.
An underline belongs to the line underneath it. When that problem leaves the board, the
mark leaves with it. Rule 26 of `RULES.md` applies to his graphite exactly as it applies
to the tutor's.

### 16. A WRONG ANSWER GETS CURIOSITY, NEVER DISAPPOINTMENT.
He goes *thinking*, not sad. No slumping, no frowning, no sighing. He asks the child to
look at something specific. He has no expression that a child could read as being let
down by them, and we will not draw one.

### 17. HE ANSWERS NOTHING.
He points, marks, reacts and jokes. Every mathematical sentence still comes from the
tutor under `RULES.md`. He is presence, not a second teacher with different rules.

---

## D. WHEN HE MUST NOT

### 18. NOT DURING A QUIZ, A TEST, OR A TIMED CHALLENGE.
Assessment belongs to Abrabot, boxed. Mr. Cadabra is absent — not parked, absent.

### 19. NOT OVER ANYTHING THE CHILD IS READING OR TYPING.
He never covers live text, an input, or a control. If the only route to a target crosses
one, he goes around or he stays put.

**And a target that is covered is not a target.** Found the first time the layer ran on
the real `session.html`: the welcome card was up and he underlined the board straight
through it. A thing can be perfectly present in the page and still be *underneath*
something — a modal, a sprint overlay, the keyboard tray. If the point at the middle of a
target does not belong to that target, he does not act on it at all. Enforced generically
in `cadabra.js`, so it covers every overlay on every page without naming any of them.

### 20. NOT WHEN THE DEVICE ASKS FOR CALM.
`prefers-reduced-motion` reduces him to a still character in a fixed spot with a blink.
Every behaviour still *happens* — the underline still appears, the celebration still
registers — it simply arrives without travel.

### 21. NOT ON THE PARENT, TEACHER, ADMIN, PRICING, PRIVACY OR TERMS PAGES.
Adults doing paperwork are not the audience. Marketing pages are a separate decision,
made by marketing, and not covered here.

### 22. NOT AFTER A HARD SESSION.
If the previous session ended in repeated failure or an early exit, the next one opens
quietly: no joke, no tour, tier-1 celebrations only, until the child gets two right.

### 23. HE NEVER EATS A CLICK.
The layer he lives in is transparent to the pointer, always. If a child can tap him and
something happens that they did not intend, the rule has been broken.

---

## E. HOW MUCH, AND FOR WHOM

### 24. PRESENCE BUDGET SHRINKS AS THE STUDENT GROWS.
One dial, applied everywhere:

| Stage | Entrance | Joke | Tour | Idle drift | Tier 3 |
|---|---|---|---|---|---|
| Early elementary | full | yes | yes | full | freely |
| Upper elementary | full | yes | on request | reduced | earned |
| Middle school | brief | occasional | on request | slight | rare |
| High school and up | corner only | no | no | none | never |

A fourteen-year-old being cheered at by a cartoon pencil is being told the software
thinks they are small.

### 25. HE GETS QUIETER AS THE LESSON GOES ON.
The first five minutes may carry an entrance and a tour. Minute thirty carries a blink.
Attention is spent, not renewed.

### 26. NO BEHAVIOUR REPEATS INSIDE A SESSION.
Not a joke, not a celebration line, not a gesture sequence. The library must be large
enough that it does not have to: fifty jokes minimum before this ships.

### 27. THE CHILD CAN TURN HIM DOWN.
A setting with three positions — full, quiet, off — that persists per child. "Off" leaves
the lesson completely intact, because nothing he does is load-bearing. If turning him off
breaks anything, that thing was built wrong.

---

## F. HOW IT IS BUILT

### 28. HE IS A LAYER, NOT A CHANGE TO THE PAGE.
One overlay above everything, transparent to the pointer, positioned in page pixels. He
adds no element to the lesson's own DOM and takes nothing out of it.

### 29. TRANSFORM ONLY. NOTHING HE DOES CAUSES LAYOUT.
Translate, rotate, scale, opacity. No width, height, top, left, margin or padding is ever
animated. The board must not reflow because a mascot moved, on any device.

### 30. HE FINDS HIS TARGETS BY NAME, NEVER BY COORDINATE.
Elements he may act on carry a `data-cad="..."` attribute and he reads their boxes at
runtime. No hardcoded positions anywhere, so a page can be redesigned without touching
him.

### 31. THE MENU IS DATA, NOT CODE.
What he does and when lives in one JSON script — page, moment, behaviour, stage limits.
Changing his behaviour is editing that file. Adding a behaviour is code; scheduling one
is not.

### 32. HE SHIPS DARK.
No script file present means every page behaves exactly as it does today, with no flag to
set and no caller to change — the same pattern `tutor-moments.js` already uses. The day
the manifest lands, he appears. Any page can opt out by not carrying the attributes.

### 33. HE IS NOT THE PRESENCE LAYER.
The video presence layer is footage of a real person and no drawn character may wear it.
Whatever happens to the orb, the floating layer and the presence layer are never the same
character at the same time.

## G. HOW HE FEELS ABOUT THE WORK (added 2 September 2026, build rr — Jim's list)

### 34. HE MARKS A WORD BY ASKING THE PAGE WHERE IT IS.
A circle, an underline or an exclamation mark lands on a word, a number or a label
because the page measured that text (a DOM Range; SVG labels by their box), newest
board block first, forgiving of the board's own spacing and operator glyphs. He never
estimates a position. Rule 19 applies inside the finder: a covered or off-screen
occurrence is skipped, and if no visible one exists he draws nothing. Proof standard: a
mark encloses its word and its centre sits within a few pixels of the word's centre —
measured, not eyeballed (fifty words, 2026-09-02).

### 35. INK BELONGS TO THE THING IT WAS DRAWN ON.
A mark remembers its element and moves with it — a scrolling board carries its circles,
an element that leaves the page takes its mark along (rule 15 by construction), and ink
drawn on the board is clipped to the board's box so it can never sit over the page's
header. A mark he was interrupted in the middle of drawing is wiped, never left half
invisible. The tutor asks for a mark with `[[ink circle="…"]]`, `underline=` or `bang=`
— at most one per reply, most replies none, never while correcting.

### 36. THE GLANCE IS A REWARD, NEVER COMPANY.
When the board grows he may drift over and point at the newest thing — only after the
voice has stopped, only if nobody is typing, not more often than the menu allows, and
on a dice roll. It never interrupts something he is already doing. In quiet mode it does
not happen at all.

### 37. STUCK GETS COMPANY, NOT CORRECTION.
Two misses in a row, or a long silence after he actually asked something, and he comes
close to the answer box, listens, says one short warm line, and stays beside the child
until the next answer. No disappointed face exists to make (rule 16); the words in the
empathy bag never begin with "no", "wrong" or "not".

### 38. A MILESTONE GETS THE BIGGEST PARTY HE HAS, AND A NAMED ONE.
Three in a row, a mastered lesson, a passed quiz, a mastered unit, the Course Champion
medal: stars, arms up, an exclamation mark on the newest board line, and a line written
for that kind of milestone. Ordinary right answers keep the tiered celebration of rule 11
— a party that happens every turn is not a party.

### 39. HE STOPS TALKING WHEN THE VOICE DOES.
His mouth and his stillness follow the real voice: `mt:speaking` starts them,
`mt:silent` (voice.js, and the demo's own player) ends them, and two watchdogs — a quiet
analyser, a 25-second ceiling — cover a page whose voice never announces. Waving hello at
the start of a lesson is silent; the real voice owns the opening.

---

## Open, and owned by Jim

1. **Does the orb become the pencil, or does the orb keep the robot while the pencil
   floats?** Everything in section F works either way. This is the only decision that
   forces `tutor-face.js` open and repoints the pixel pins.
2. **Does the video presence path close?** Still the question everything else follows
   from, unchanged since 28 August.
3. **The stage table in rule 24 is a first draft.** The boundaries are guesses and should
   be argued with.

I did no harm and this file is not truncated.
