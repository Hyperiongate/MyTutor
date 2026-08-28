/* =============================================================================
   board.js  --  THE WHITEBOARD, ONE COPY  --  Hyperion Shift LLC
   -----------------------------------------------------------------------------
   CHANGE NOTES (keep newest at top):
   2026-08-28  BUILD pw -- A DIFFERENT PROBLEM IS NOT A STALE SNAPSHOT. Jim's
               order-of-operations screenshot: the worked "6 + 4 x 2 = 14" and the
               earlier "3 + 2 x 5 = 13" both hidden behind "show the 5 earlier steps"
               on a board around 90% empty. supersedePrevious()'s own comment says a
               block folds when this turn opens with the SAME first line -- but the
               code computed _firstLine(self), tested it only for emptiness, and NEVER
               CALLED _firstLine(k). Every earlier written block folded, whatever
               problem it belonged to. One missing `if`. Build oz's fold survives
               untouched for real re-statements (rule 35 restates every turn), and a
               folding block now takes its own chip with it -- the drive caught it
               reading "1 earlier step" while two were folded. tools/pwdrive.py,
               both directions, in a real browser.
   2026-08-28  BUILD pu -- SHRINK THE PICTURE UNTIL THE TURN FITS. Jim: "whatever
               he's saying needs to be visible on the whiteboard without the student
               moving anything." MEASURED in a real browser (tools/puedrive.py): the
               SCRIPTED lane is clean at 1280x800 and 1280x600; the LIVE lane is not
               -- one reply is 406px of content in a 335px board, 90px above the
               fold, while the words say "look back at the number line". Cause is
               build ns's own follow-the-pen: once a turn outgrows the window the
               anchor pins its END, so the top of the SAME turn scrolls away.
               fitTurnToBoard() now shrinks that turn's figures (aspect kept, floor
               340px, restored when the window grows back) before the anchor runs.
               ⚠️ IT DOES NOT CLOSE THIS CASE: text alone is 396px of that turn, so
               the next build is turn LENGTH. Both numbers are in the code.
     2026-08-27  BUILD os -- THE BOARD READS ONE, TWO, THREE. Jim: "I want ...
                 Cadabra to talk and then puts up the problem as he's explaining
                 it. And it says step one... right next to it, it says step two,
                 and there's the drawing. And next to that is step three... if
                 there are several steps to a process he's teaching that we use a
                 whole board, and it clearly says this is one, then two, then
                 three, then four, and the student doesn't have to scroll around
                 to find it." NEW [[stepcard n="1" title="..."]] tag: opens a
                 labeled "Step N" CARD in a flex row (.steprow) that fills the
                 board's width; EVERY board block that follows (worklists,
                 figures, columns, objects -- anything that walks through
                 mountBlock, or the scripted lane's feedBlock) lands INSIDE that
                 card until the next [[stepcard]] or the end of the turn. Cards
                 sit shoulder to shoulder, wrap on narrow screens, and fold into
                 a finished problem like everything else. Machinery here
                 (openStepCard / clearStepGrid / activeStepCell / _stepCellLive /
                 ensureStepGridCSS; mountBlock now hosts into the open card and
                 the [[beside]] join works inside a card too); the pages'
                 handleTags dispatch [[stepcard]] (resetting their own worklist
                 pointer) and clearStepGrid() at turn start; script-board.js
                 dispatches it for the scripted lane. A [[stepcard]] whose card
                 was folded away (or cleared) simply starts a fresh row -- it
                 can never draw into a closed problem.
     2026-08-26  BUILD oj -- SIDE BY SIDE ON PURPOSE. Jim: "the whiteboard is
                 underutilized... they can move to the side. Say, alright, we're
                 gonna put the other equation right next to this one so you could
                 see it better." NEW [[beside]] tag: the NEXT board block (a
                 worklist or a figure) joins the PREVIOUS one in a flex row
                 (.mrow) instead of starting a new line -- so two equations, or
                 an equation and its picture, sit shoulder to shoulder and the
                 board's width finally works. Machinery here (armBeside /
                 clearBeside / mountBlock -- the ONE door every new .mblock now
                 walks through); the pages' getWorklist/feedBlock call
                 mountBlock, their handleTags dispatch [[beside]], and their CSS
                 adds .mrow (flex-wrap: wrap, so a phone stacks the columns --
                 which is why prose must keep naming work by CONTENT, never by
                 left/right; referee 40's law already says so). A block moved
                 into a row is re-fitted (fitRow) on the next frame, folded
                 problems are never joined, and a [[beside]] with nothing before
                 it renders exactly as if the tag were absent.
     2026-08-25  BUILD nt -- THE FLAG SHOWS ITSELF. Jim, first look for his new
                 flag: "I don't see a flag." The server was current (checked live);
                 the button was also drawn at 25%% opacity -- discretion that serves
                 nobody, since the ONLY person who can ever see it is the owner who
                 asked for it. Now 55%%, full on hover. Nothing else changed.
     2026-08-25  BUILD ns -- FOLLOW THE PEN. Jim, next lesson after nr: "same
                 problem with the sizing of the keyboard." He was right and nr was
                 INCOMPLETE: the ResizeObserver only repairs the moment the board
                 CHANGES size. In his lesson the keyboard was ALREADY open, the
                 board was already short, and a tall turn simply OUTGREW it -- the
                 ir top-anchor held the turn's start on screen while the question
                 at its end landed below the fold. No resize, no repair.
                 THE REAL FIX is one line in scrollFeed's anchored mode: the scroll
                 target is now max(turnTop, contentEnd - windowHeight) -- the turn
                 still STARTS at the top (ir's ruling intact for turns that fit),
                 but once the board work outgrows the window the view advances with
                 the writing, like eyes following a teacher's pen, so the newest
                 line -- and the question always lands last -- is ALWAYS visible.
                 History stays one scroll-up away; a student who scrolled away is
                 still never touched (stickBottom rules, build ay's latch intact).
                 feedResized() collapses to a thin guard + scrollFeed() call, since
                 scrollFeed itself now handles a shrunken board correctly.
                 ⚠️ LESSON, PINNED: a repair that only fires on the EVENT (resize)
                 misses the STATE (already small). Fix the invariant, not the moment.
     2026-08-25  BUILD nr -- THE BOARD ANSWERS FOR ITS OWN SIZE. Jim, live in
                 Pre-Algebra with the new symbol strip: "it says what do you get?
                 and I have to scroll down to see it... the keyboard is now taking
                 up space the whiteboard used to extend into, and I don't know that
                 the app understands the whiteboard is as shallow as it used to
                 be... we have to scroll so the student doesn't have to."
                 ROOT CAUSE: #feed is flex:1 under a fixed-height column, so when
                 the composer (and its math-keyboard strip) appears, the feed
                 SHRINKS -- but scrollFeed() only ran when CONTENT changed, never
                 when the CONTAINER did, so the turn's tail (where the question
                 lives) slid below the fold and stayed there. FIX: a ResizeObserver
                 on the feed (armed lazily from addBubble -- `feed` is a page
                 global that does not exist yet when this file parses). On any
                 size change: student scrolled away -> leave them alone (stickBottom
                 still rules); the anchored turn still fits -> re-run scrollFeed
                 (build ir's top anchor, recomputed); the feed SHRANK and the turn
                 no longer fits -> show the END of the content, because the newest
                 thing -- the question and the answer buttons -- lives at the end.
                 Every programmatic scroll is marked autoScroll so build ay's
                 latch never reads our own fix as the student scrolling away.
                 One copy here = session, practice, topic, drill, demo all fixed.
     2026-08-25  BUILD nq -- THE OWNER'S FLAG. Jim, live in geometry, caught the
                 tutor saying "piece" for "angle": "It would be great if I could
                 point this out while in the app." Ruling: "I only want it when I'm
                 online. I don't want the parents or teachers to see it." So: a tiny
                 flag button rides every TUTOR bubble, but ONLY when this device
                 holds the owner key (localStorage "mt_owner_key", set from /admin's
                 "Enable flag on this device"). Tap -> type what's wrong -> POST
                 /api/flag with the key in the X-Admin-Key header; the server
                 re-checks the key, so a forged localStorage value gets a 403 and
                 writes nothing. Students/parents/teachers never hold the key, so
                 for them this build changes NOTHING -- ownerFlagAttach() returns on
                 the first line. The quote is read from a CLONE of the bubble with
                 the button removed, so the flag never quotes itself, and it is read
                 at TAP time so streamed-in board work is included. addBubble is the
                 one shared door every tutor bubble passes through (session, topic,
                 practice, drill, demo alike), so one hook covers every page.
     2026-08-19  BUILD jc -- THE COLUMN REDRAWS ITSELF, NEW MARKS IN RED (Jim, live on
                 a five-digit addition: "as you complete steps, what you just did
                 disappears off the top of the screen... it would be better if they
                 restated what it looked like... the three underneath the eight and
                 five in red, and the one carried above the tens column in red").
                 [[column]] gains carries="1_" and partial="43" -- both RIGHT-ALIGNED
                 to the ones column, "_" for a blank -- so the tutor re-emits the same
                 problem each step and the board redraws it whole. The page DIFFS the
                 new state against the last render of that same problem and reds only
                 what changed, so the model states the state and cannot get the
                 highlighting wrong. result= (the green final answer) and align="last"
                 (build di's deliberately-wrong lineup) are untouched.
     2026-08-19  EVERY TUTOR TURN STARTS AT THE TOP OF THE BOARD (build ir, Jim:
                 "I constantly need to scroll ... what's showing up on the board is
                 at the bottom. Every time Mr. Cadabra speaks, he starts speaking in
                 a bubble that is placed at the top of the visible board -- if I want
                 what came before, I scroll UP"). Build ax anchored a turn's start at
                 the top ONLY when the turn was taller than the window; short turns
                 still pinned to the bottom, which is exactly the eyes-down hunt Jim
                 described. Now a NEW TUTOR BUBBLE is ALWAYS placed at the visible
                 top of the feed: history is above (scroll up), and the turn's board
                 work fills in below it as it arrives. The mechanics: a short turn
                 near the end of the transcript physically CANNOT sit at the top
                 (scrollTop clamps at scrollHeight - clientHeight), so a zero-height
                 spacer (#feedPad) rides as the feed's LAST child and grows just
                 enough blank to let the turn reach the top -- shrinking again as
                 real board work replaces it, and collapsing to zero whenever the
                 view pins to the bottom (student/system bubbles). The spacer is
                 re-appended only when something landed after it, so the childList
                 MutationObserver never loops. Student-scrolled-away behavior is
                 untouched (stickBottom still rules). Applies to session, topic and
                 practice alike -- one copy, all three boards.
     2026-08-17  NEW FILE (build he -- Phase 2 of the full-app review). All 34
                 top-level board-display functions -- every [[step]]/[[write]]/
                 [[solve]] row, the graph, the figures, the balance, the machine,
                 the objects and choice rows (choiceBtn lives nested inside
                 showChoices, as it does on every page), the bubble feed, the
                 spotlight -- were hand-synced copies across session.html,
                 topic.html and practice.html, measured byte-identical after
                 comment normalisation. Zero divergence -- which after build gz's
                 two live defects is luck, not safety. One copy now.
                 MOVED WITH THEM: the pure state they own (lastTurnEl, spotTimer,
                 choicesRow, autoScroll, stickBottom) and their constants
                 (GRAPH_COLORS, SPOT_MS). NOT moved: DOM references (feed, composer
                 -- this file loads in <head>, before the DOM exists) and the truly
                 page-specific dispatchers (handleTags, wipeBoard, feedBlock,
                 getWorklist, clearStage), which differ per page BY DESIGN: which
                 tags a page supports is configuration, not copy-paste.
                 AMBIENT CONTRACT (verified on all three pages before the move):
                 el, feed, composer, busy, feedBlock(), getWorklist(), plus
                 styleVars/escapeHTML from board-text.js, which loads before this
                 file. EXTRACTED VERBATIM from session.html, comments included.
                 PROVED: the full-tag corpus rendered before and after in a real
                 browser -- bubble and board HTML byte-identical on every page.
   ============================================================================= */
// ---------- THE BOARD'S OWN STATE + CONSTANTS (moved from the pages, build he) ----------
const GRAPH_COLORS = ["#5b5bd6", "#14b8a6", "#ff7a59", "#9333ea"];

// ---------- BOARD SPOTLIGHT (build ee, rule 60 / signaling) ----------
// [[highlight id="line"]] glows the newest line of board work; [[highlight
// id="board"]] glows the whole board. Returns true when it HANDLED a board key
// (so the dispatcher doesn't also run the page tour), false when the id belongs
// to the tour (highlightEl's territory, unchanged). The glow is a CUE, not a
// state: it self-clears after SPOT_MS, a new spotlight replaces the old one, and
// clearHighlight (start of every tutor turn) clears it too.
const SPOT_MS = 6000;

// 2026-08-07 (build ax, Jim: "the whiteboard disappears below and I have to scroll
// constantly"): FOLLOW THE TURN, not just the bottom. Every new tutor turn re-engages
// following (even if the student had scrolled up to read history).
// 2026-08-19 (build ir): the turn's START now sits at the visible top for EVERY tutor
// turn, not just window-tall ones -- see scrollFeed and feedPadEl below.
let lastTurnEl = null;   // the bubble that starts the current tutor turn (null = pin bottom)

let spotTimer = null;

// ---------- TAP-TO-ANSWER CHOICES (2026-08-03, for the elementary courses) ----------
// The tutor offers answer buttons with [[choices options="12 | 14 | 16"]]. A tap sends
// that answer exactly like typing it, so young children who can't type (or read well)
// can still answer. A friendly "I'm not sure" button is ALWAYS added so a stuck child
// can say so without writing a word. The typed answer bar stays available as a backup.
// Choices clear at the start of every tutor turn (stale buttons never linger).
let choicesRow = null;

// 2026-08-07 (build ay, Jim's Basic-Math cookies: the follow fix latched OFF by
// accident). Our OWN programmatic scrolls fire scroll events too -- the old listener
// read an anchored (non-bottom) position as "the student scrolled away" and disabled
// following, so when the tap-to-answer row shrank the transcript a beat later, the
// re-anchor was skipped and the board work slid below the fold. autoScroll marks our
// scrolls so only a REAL student scroll releases following.
let autoScroll = false;

// Keep the newest content visible. We pin to the bottom on any new content -- UNLESS the
// student has deliberately scrolled up to read history (then we leave them alone until
// they return to the bottom). requestAnimationFrame lets the new content lay out FIRST, so
// we measure the true height (fixes the "new line hides below the fold" scrolling).
let stickBottom = true;

// ---------- SIDE BY SIDE ON PURPOSE (build oj) ----------
// [[beside]] arms this flag; the NEXT board block joins the previous one in a
// .mrow instead of starting its own line. Consumed by mountBlock, cleared at the
// start of every tutor turn (a dangling [[beside]] with no block after it must
// never leak into the next turn).
let besidePending = false;

function armBeside() { besidePending = true; }
function clearBeside() { besidePending = false; }

// ---------- THE BOARD READS ONE, TWO, THREE (build os) ----------
// [[stepcard n="1" title="..."]] opens a labeled Step-N card; every block that
// follows mounts INSIDE it until the next [[stepcard]] or the end of the turn.
// Cleared at the start of every tutor turn (pages call clearStepGrid() next to
// clearBeside()) and per beat in the scripted lane.
let curStepRow = null;    // the .steprow flex container (one per demonstration)
let curStepCell = null;   // the OPEN card's body -- where new blocks land

// A cell (or row) is only a live target while it is on the board and NOT folded
// into a finished problem (.probdone) -- drawing into a closed problem is the
// one thing this machinery must never do.
function _stepCellLive(node) {
  return !!(node && node.isConnected && !(node.closest && node.closest(".probdone")));
}
function activeStepCell() { return _stepCellLive(curStepCell) ? curStepCell : null; }
function clearStepGrid() { curStepRow = null; curStepCell = null; }

function ensureStepGridCSS() {
  if (document.getElementById("mtStepGridCSS")) return;
  const st = document.createElement("style"); st.id = "mtStepGridCSS";
  st.textContent =
    ".steprow{display:flex;flex-wrap:wrap;gap:12px;width:100%;align-self:stretch;" +
    "align-items:stretch;padding:4px 0}" +
    ".stepcell{flex:1 1 280px;min-width:250px;max-width:100%;border:2px solid #d9d7ee;" +
    "border-radius:16px;background:#fcfcff;padding:10px 12px 12px;" +
    "box-shadow:0 4px 14px rgba(60,40,120,.06)}" +
    ".stephead{display:flex;align-items:center;gap:8px;margin-bottom:6px}" +
    ".stepnum{background:linear-gradient(90deg,#5b5bd6,#14b8a6);color:#fff;font-weight:800;" +
    "font-size:13px;border-radius:999px;padding:4px 12px;flex:0 0 auto;white-space:nowrap}" +
    ".steptitle{font-weight:700;font-size:14px;color:#26263a;line-height:1.25}" +
    ".stepbody{display:flex;flex-direction:column;gap:8px;align-items:center}" +
    ".stepbody .mblock{width:100%;padding:2px 0}" +
    "@media (max-width:560px){.stepcell{min-width:100%}}";
  document.head.appendChild(st);
}

// [[stepcard n="2" title="Multiply the tops"]] -> a "Step 2" card joins the row.
// n missing -> numbered by position; a fresh row starts when there is no live row
// (first card of a turn, after a [[clear]], or after the problem folded).
function openStepCard(a) {
  ensureStepGridCSS();
  // the host board: the scripted lane's #board (boardEl) or the transcript feed
  let host = null;
  try { if (typeof boardEl === "function") host = boardEl(); } catch (e) {}
  if (!host) host = feed;
  if (!host) return;
  // the pages' fold hooks, exactly as their feedBlock() runs them (a stepcard
  // STARTS teaching just as a figure does); absent on the scripted lane.
  try { if (typeof foldIfProblemClosed === "function") foldIfProblemClosed(); } catch (e) {}
  try { if (typeof foldOpenerOnce === "function") foldOpenerOnce(); } catch (e) {}
  try { clearHint(); } catch (e) {}
  if (!_stepCellLive(curStepRow)) {
    curStepRow = document.createElement("div");
    curStepRow.className = "steprow";
    host.appendChild(curStepRow);
  }
  const cell = document.createElement("div"); cell.className = "stepcell pop";
  const head = document.createElement("div"); head.className = "stephead";
  const badge = document.createElement("span"); badge.className = "stepnum";
  const nRaw = String(a && (a.n || a.num || a.number) || "").trim();
  badge.textContent = "Step " + (nRaw || (curStepRow.children.length + 1));
  head.appendChild(badge);
  const title = String(a && (a.title || a.label) || "").trim();
  if (title) {
    const t = document.createElement("span"); t.className = "steptitle";
    t.textContent = title; head.appendChild(t);
  }
  cell.appendChild(head);
  const bodyEl = document.createElement("div"); bodyEl.className = "stepbody";
  cell.appendChild(bodyEl);
  curStepRow.appendChild(cell);
  curStepCell = bodyEl;
  scrollFeed();
}

// THE ONE DOOR every new .mblock walks through (pages' getWorklist + feedBlock).
// Plain case: append to the host, exactly as before. [[beside]] case: find the
// previous board block -- never inside a folded problem (.probdone), and give up
// at nothing found -- then wrap it (or join its existing row) and re-fit its rows
// once the new, narrower width has laid out.
// build os: the HOST is the open step card when one is live ([[stepcard]] captured
// this turn's blocks), the feed otherwise -- and [[beside]] joins within whichever
// host the block lands in.
function _joinBeside(host, b) {
  let prev = null;
  const kids = host.children;
  for (let i = kids.length - 1; i >= 0; i--) {
    const k = kids[i];
    if (!k.classList) continue;
    if (k.classList.contains("probdone")) break;   // a folded problem is finished
    if (k.classList.contains("mrow") || k.classList.contains("mblock")) { prev = k; break; }
  }
  if (!prev) return false;
  let row = prev;
  if (!prev.classList.contains("mrow")) {
    row = document.createElement("div"); row.className = "mrow";
    host.insertBefore(row, prev); row.appendChild(prev);
  }
  row.appendChild(b);
  // rows sized for the full board are too wide for half of it -- re-fit after layout
  requestAnimationFrame(() => { try { row.querySelectorAll(".wrow, .worow").forEach(fitRow); } catch (e) {} });
  scrollFeed();
  return true;
}

function mountBlock(b) {
  const cell = activeStepCell();
  const host = cell || feed;
  if (besidePending) {
    besidePending = false;
    if (_joinBeside(host, b)) return b;
  }
  host.appendChild(b);
  // a block landing in a narrow card gets its rows re-fit once layout settles
  if (cell) requestAnimationFrame(() => { try { cell.querySelectorAll(".wrow, .worow").forEach(fitRow); } catch (e) {} });
  return b;
}

// ---------- THE DISPLAY FUNCTIONS ----------

// Created once, appended to <body>; centered over the whiteboard (#feed) at show
// time and re-centered on resize. Fixed positioning, so feed scrolling never moves it.
function thinkFlagEl() {
  let f = document.getElementById("thinkFlag");
  if (!f) {
    f = document.createElement("div"); f.id = "thinkFlag"; f.className = "thinkflag";
    f.innerHTML = '<span class="tdot"></span><span class="ttxt"></span>';
    document.body.appendChild(f);
  }
  return f;
}

function placeThinkFlag() {
  const f = document.getElementById("thinkFlag");
  if (!f || !f.classList.contains("show")) return;
  const feed = document.getElementById("feed");
  const r = feed ? feed.getBoundingClientRect() : null;
  f.style.left = (r ? r.left + r.width / 2 : window.innerWidth / 2) + "px";
  f.style.top = (r ? r.top + r.height * 0.45 : window.innerHeight * 0.45) + "px";
}

// ---------- Control tags ----------
function parseAttrs(s) {
  const attrs = {}; const re = /(\w+)\s*=\s*("([^"]*)"|'([^']*)'|(\S+))/g; let m;
  while ((m = re.exec(s)) !== null) attrs[m[1].toLowerCase()] = (m[3] !== undefined ? m[3] : m[4] !== undefined ? m[4] : m[5]);
  return attrs;
}

function clearSpot() {
  if (spotTimer) { clearTimeout(spotTimer); spotTimer = null; }
  document.querySelectorAll(".stepglow").forEach(n => n.classList.remove("stepglow"));
}

function spotlightBoard(id) {
  const key = String(id || "").toLowerCase();
  let target = null;
  if (key === "line" || key === "step" || key === "last") {
    // the newest piece of board WORK this problem: equation rows, check rows,
    // captions -- whichever was appended last. An empty board falls back to the
    // board itself so the cue never silently vanishes.
    const rows = feed.querySelectorAll(".worklist .wrow, .worklist .wcheck, .worklist .wcap");
    target = rows.length ? rows[rows.length - 1] : feed;
  } else if (key === "board") {
    target = feed;
  } else {
    return false;                      // not a board key -- the page tour owns it
  }
  clearSpot();
  target.classList.add("stepglow");
  try { target.scrollIntoView({ behavior: "smooth", block: "nearest" }); } catch (e) {}
  spotTimer = setTimeout(clearSpot, SPOT_MS);
  return true;
}

// ---------- Geometry figures (triangle / angle / circle) -- see /static/geo-figures.js ----------
// Shared math figures (grapher + stats + trig) -- see /static/math-figures.js
function showFig(kind, a) {
  const stage = feedBlock();
  const wrap = document.createElement("div"); wrap.className = "mfig pop";
  wrap.innerHTML = (window.MathFigures ? window.MathFigures.svg(kind, a) : "");
  stage.appendChild(wrap);
  if (a.caption) { const c = document.createElement("div"); c.className = "cap"; c.textContent = a.caption; wrap.appendChild(c); }
}

function showGeo(kind, a) {
  const stage = feedBlock();
  const wrap = document.createElement("div"); wrap.className = "mfig pop";
  wrap.innerHTML = (window.GeoFigures ? window.GeoFigures.svg(kind, a) : "");
  stage.appendChild(wrap);
  if (a.caption) { const c = document.createElement("div"); c.className = "cap"; c.textContent = a.caption; wrap.appendChild(c); }
}

function ensureChoicesCSS() {
  if (document.getElementById("mtChoicesCSS")) return;
  const st = document.createElement("style"); st.id = "mtChoicesCSS";
  st.textContent =
    ".choicerow{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin:10px 0 4px}" +
    ".choicebtn{font-size:20px;font-weight:800;padding:14px 24px;min-width:64px;min-height:52px;border-radius:16px;" +
    "border:2.5px solid #c9beff;background:#fff;color:#20233a;cursor:pointer;box-shadow:0 4px 12px rgba(60,40,120,.10);" +
    "transition:transform .1s ease;font-family:inherit}" +
    ".choicebtn:hover{transform:translateY(-2px);border-color:#6d5ae6;color:#6d5ae6}" +
    ".choicebtn:disabled{opacity:.45;cursor:default;transform:none}" +
    ".choicebtn.notsure{font-size:15px;border-style:dashed;color:#5b6079}";
  document.head.appendChild(st);
}

function clearChoices() { if (choicesRow) { choicesRow.remove(); choicesRow = null; scrollFeed(); } }

function showChoices(a) {
  const opts = String(a.options || "").split("|").map(s => s.trim()).filter(Boolean).slice(0, 6);
  if (!opts.length) return;
  ensureChoicesCSS(); clearChoices();
  const row = document.createElement("div"); row.className = "choicerow"; choicesRow = row;
  function choiceBtn(label, message, extra) {
    const b = document.createElement("button"); b.type = "button";
    b.className = "choicebtn" + (extra ? " " + extra : ""); b.textContent = label;
    b.addEventListener("click", () => {
      if (busy) return;
      Array.prototype.forEach.call(row.querySelectorAll("button"), (x) => { x.disabled = true; });
      ensureAudioGraph(); clearChoices(); sendToTutor(message);
    });
    row.appendChild(b);
  }
  for (const o of opts) choiceBtn(o, o);
  choiceBtn("🤔 I'm not sure", "I'm not sure", "notsure");
  composer.parentNode.insertBefore(row, composer);
  // Re-pin the transcript (NOT the page): the buttons take vertical space below it,
  // so without this the tutor's newest words could slip out of view.
  scrollFeed();
}

// ---------- COUNTABLE OBJECTS ON THE BOARD (2026-08-03, for the elementary courses) ----------
// [[objects emoji="⭐" groups="5"]] draws five big stars on the board; groups="5 | 3" draws two
// rows so the child can COMPARE. The tutor uses it so young children SEE the things they're
// counting instead of imagining them. The count is never printed -- counting is the child's job.
//
// add="1"  draws "⭐⭐⭐⭐⭐ + ⭐"  -- the child SEES the addition happen.
// take="2" draws the LAST TWO struck through and greyed -- the child SEES the taking away.
//
// ⚠️ (my) take= EXISTS BECAUSE ADDITION HAD A VERB AND SUBTRACTION DID NOT. Jim drilled a
// take-away lesson on 2026-08-24 and said of the re-teach: "it could have shown four stars
// and crossed out one of the stars or something, but instead he just kind of laid out a
// problem about stars and solved it and did no teaching." He was exactly right, and the
// cause was here: for two years this tag could show things being ADDED and had no way at
// all to show things being TAKEN. 63 boards said "take two away" over a picture in which
// nothing was ever taken. The caption did the work the picture was supposed to do.
function ensureObjectsCSS() {
  if (document.getElementById("mtObjectsCSS")) return;
  const st = document.createElement("style"); st.id = "mtObjectsCSS";
  st.textContent =
    ".objwrap{padding:10px 6px;text-align:center}" +
    ".objline{font-size:36px;letter-spacing:9px;line-height:1.5}" +
    // (my) the taken ones: struck through AND faded, so it reads as "gone" at a
    // glance and still reads as "gone" to a child who cannot tell the colours apart.
    ".objgone{position:relative;display:inline-block}" +
    ".objgoneimg{opacity:.30;filter:grayscale(1)}" +
    ".objgone::after{content:'';position:absolute;left:-3px;width:40px;top:46%;" +
    "height:5px;border-radius:3px;background:#c0392b;" +
    "transform:rotate(-20deg);transform-origin:center;pointer-events:none}" +
    ".objcap{font-size:13px;color:#5b6079;margin-top:4px;font-weight:600}";
  document.head.appendChild(st);
}

function showObjects(a) {
  const groups = String(a.groups || a.n || "").split("|").map(s => parseInt(s, 10))
    .filter(x => x > 0).slice(0, 3);
  if (!groups.length) return;
  ensureObjectsCSS();
  const emoji = (a.emoji || "⭐").trim() || "⭐";
  const addN = Math.min(Math.max(parseInt(a.add, 10) || 0, 0), 10);
  // (my) take="2" -- how many of the FIRST row are being taken away. Clamped to the
  // row itself: you cannot take four stars from three, and a board that tried would
  // be teaching a child something false.
  const takeN = Math.min(Math.max(parseInt(a.take, 10) || 0, 0), groups[0] || 0);
  const stage = feedBlock();
  const box = document.createElement("div"); box.className = "objwrap pop";
  groups.forEach((g, gi) => {
    const row = document.createElement("div"); row.className = "objline";
    if (gi === 0 && takeN) {
      // THE ONES THAT STAY, then THE ONES BEING TAKEN, struck through. Two spans
      // rather than one string, because the strike has to land on some of the
      // stars and not the others -- which is the entire point of the picture.
      const keep = document.createElement("span");
      keep.textContent = emoji.repeat(Math.min(g - takeN, 20));
      row.appendChild(keep);
      // ⚠️ ONE STRIKE PER STAR, not one line across the group. The first draft wrapped
      // all the taken ones in a single span and drew one long diagonal, which reads as
      // a slash through a picture rather than "each of these is gone" -- checked on a
      // render before it shipped.
      for (let k = 0; k < Math.min(takeN, 20); k++) {
        // ⚠️ TWO NESTED SPANS, and the nesting is the point: the FADE belongs to the
        // star and the STRIKE must not fade with it. One span carrying both put
        // opacity on the pseudo-element too, and the cross came out as a ghost --
        // caught on a render, not in review.
        const gone = document.createElement("span");
        gone.className = "objgone";
        const img = document.createElement("span");
        img.className = "objgoneimg";
        img.textContent = emoji;
        gone.appendChild(img);
        row.appendChild(gone);
      }
    } else {
      row.textContent = emoji.repeat(Math.min(g, 20))
        // add="1" on the FIRST row draws "⭐⭐⭐⭐⭐ + ⭐" so the child SEES the addition happen.
        + (gi === 0 && addN ? "  +  " + emoji.repeat(addN) : "");
    }
    box.appendChild(row);
  });
  if (a.caption) { const c = document.createElement("div"); c.className = "objcap"; c.textContent = a.caption; box.appendChild(c); }
  stage.appendChild(box);
}

// The summary line's equation, read from the FIRST board row of the folded problem.
function problemLabel(body) {
  let eq = "";
  try {
    const row = body.querySelector(".worklist .wrow");
    if (row) {
      const l = row.querySelector(".wl"), r = row.querySelector(".wr");
      const lt = l ? l.textContent.trim() : "";
      const rt = r ? r.textContent.trim() : "";
      eq = rt ? (lt + " = " + rt) : lt;
    }
  } catch (e) {}
  eq = eq.replace(/\s+/g, " ").trim();
  if (eq.length > 44) eq = eq.slice(0, 43) + "…";
  return eq;
}

function iconsFor(expr) {
  const wrap = document.createElement("div"); wrap.className = "tray";
  const tokens = String(expr).split("+").map(x => x.trim()).filter(Boolean); let rendered = false;
  for (const tok of tokens) {
    if (/^\d+$/.test(tok)) { const n = Math.min(parseInt(tok, 10), 12);
      for (let i = 0; i < n; i++) wrap.appendChild(document.createTextNode("🐵")); rendered = true; }
    else if (/[a-zA-Z?]/.test(tok)) { const b = document.createElement("span"); b.className = "box"; b.textContent = tok; wrap.appendChild(b); rendered = true; }
    else { const s = document.createElement("span"); s.style.fontSize = "16px"; s.textContent = tok; wrap.appendChild(s); rendered = true; }
  }
  if (!rendered) wrap.textContent = String(expr); return wrap;
}

function pan(side, expr) {
  const p = document.createElement("div"); p.className = "pan " + side;
  const rope = document.createElement("div"); rope.className = "rope";
  const label = document.createElement("div"); label.className = "label"; label.textContent = expr;
  p.appendChild(rope); p.appendChild(iconsFor(expr)); p.appendChild(label); return p;
}

function showBalance(a) {
  const left = a.left || "", right = a.right || "", st = (a.state || "level").toLowerCase();
  let deg = 0; if (st.includes("left")) deg = -9; else if (st.includes("right")) deg = 9;
  else if (st === "tip" || st === "unbalanced") deg = -9;
  const stage = feedBlock(); const scale = document.createElement("div"); scale.className = "scale pop";
  const bw = document.createElement("div"); bw.className = "beamwrap";
  const beam = document.createElement("div"); beam.className = "beam"; beam.style.transform = "rotate(" + deg + "deg)";
  const pivot = document.createElement("div"); pivot.className = "pivot";
  bw.appendChild(beam); bw.appendChild(pan("left", left)); bw.appendChild(pan("right", right)); bw.appendChild(pivot);
  scale.appendChild(bw);
  const eq = document.createElement("div"); eq.className = "eq"; eq.textContent = left + "  =  " + right; scale.appendChild(eq);
  if (a.caption) { const c = document.createElement("div"); c.className = "cap"; c.textContent = a.caption; scale.appendChild(c); }
  stage.appendChild(scale);
  requestAnimationFrame(() => { beam.style.transform = "rotate(" + deg + "deg)"; });
}

// ---------- Coordinate grapher (lines, parabolas, points) ----------
// Driven by [[graph lines="y=2x+1; y=-x+3" parabola="y=x^2-4x+1" points="(1,3),(0,5)"
//            caption="..." range="-10..10"]]. Draws an SVG coordinate plane.
function parseLinear(expr) {
  let s = String(expr).replace(/\s+/g, "").toLowerCase();
  let vm = s.match(/^x=(-?\d*\.?\d+)$/);
  if (vm) return { vertical: true, x: parseFloat(vm[1]) };
  s = s.replace(/^y=/, "");
  let m = 0, b = 0, hasX = false;
  let xm = s.match(/([+-]?\d*\.?\d*)x/);
  if (xm) { hasX = true; let c = xm[1];
    m = (c === "" || c === "+") ? 1 : (c === "-" ? -1 : parseFloat(c)); s = s.replace(xm[0], ""); }
  s = s.replace(/^\+/, "");
  if (s !== "") { let bv = parseFloat(s); if (!isNaN(bv)) b = bv; }
  if (!hasX && s === "") return null;
  return { vertical: false, m, b };
}

function parseQuadratic(expr) {
  let s = String(expr).replace(/\s+/g, "").toLowerCase().replace(/²/g, "^2").replace(/^y=/, "");
  let am = s.match(/([+-]?\d*\.?\d*)x\^2/); if (!am) return null;
  let cc = am[1]; let a = (cc === "" || cc === "+") ? 1 : (cc === "-" ? -1 : parseFloat(cc));
  s = s.replace(am[0], ""); let lin = parseLinear("y=" + (s || "0"));
  return { a, b: lin ? lin.m : 0, c: lin ? lin.b : 0 };
}

function parsePts(str) {
  const pts = []; const re = /\(\s*(-?\d*\.?\d+)\s*,\s*(-?\d*\.?\d+)\s*\)/g; let m;
  while ((m = re.exec(String(str))) !== null) pts.push([parseFloat(m[1]), parseFloat(m[2])]);
  return pts;
}

function showGraph(a) {
  const S = 440, PAD = 28;
  let xmin = -10, xmax = 10, ymin = -10, ymax = 10;
  const rng = String(a.range || "").match(/(-?\d+)\.\.(-?\d+)/);
  if (rng) { xmin = ymin = parseInt(rng[1], 10); xmax = ymax = parseInt(rng[2], 10); }
  const plot = S - 2 * PAD;
  const mapX = (x) => PAD + (x - xmin) / (xmax - xmin) * plot;
  const mapY = (y) => PAD + (ymax - y) / (ymax - ymin) * plot;
  const esc = (t) => String(t).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  let svg = '<svg viewBox="0 0 ' + S + ' ' + S + '" class="grapher" xmlns="http://www.w3.org/2000/svg">';
  svg += '<defs><clipPath id="gclip"><rect x="' + PAD + '" y="' + PAD + '" width="' + plot + '" height="' + plot + '"/></clipPath></defs>';
  svg += '<rect x="' + PAD + '" y="' + PAD + '" width="' + plot + '" height="' + plot + '" fill="#fbfbff" stroke="#e7e6f2"/>';
  // grid + tick labels
  for (let x = xmin; x <= xmax; x++) {
    const px = mapX(x);
    svg += '<line x1="' + px + '" y1="' + PAD + '" x2="' + px + '" y2="' + (S - PAD) + '" stroke="' + (x === 0 ? "#9aa7b6" : "#eef0f7") + '" stroke-width="' + (x === 0 ? 1.5 : 1) + '"/>';
    if (x !== 0 && x % 2 === 0) svg += '<text x="' + px + '" y="' + (mapY(0) + 13) + '" font-size="10" fill="#8890a0" text-anchor="middle">' + x + '</text>';
  }
  for (let y = ymin; y <= ymax; y++) {
    const py = mapY(y);
    svg += '<line x1="' + PAD + '" y1="' + py + '" x2="' + (S - PAD) + '" y2="' + py + '" stroke="' + (y === 0 ? "#9aa7b6" : "#eef0f7") + '" stroke-width="' + (y === 0 ? 1.5 : 1) + '"/>';
    if (y !== 0 && y % 2 === 0) svg += '<text x="' + (mapX(0) - 6) + '" y="' + (py + 3) + '" font-size="10" fill="#8890a0" text-anchor="end">' + y + '</text>';
  }
  svg += '<text x="' + (S - PAD + 2) + '" y="' + (mapY(0) + 3) + '" font-size="11" fill="#6b6f82">x</text>';
  svg += '<text x="' + (mapX(0) + 4) + '" y="' + (PAD - 2) + '" font-size="11" fill="#6b6f82">y</text>';
  // lines
  const lines = String(a.lines || "").split(/[;|]/).map(s => s.trim()).filter(Boolean);
  const parsedLines = [];
  svg += '<g clip-path="url(#gclip)">';
  lines.forEach((expr, i) => {
    const L = parseLinear(expr); if (!L) return; parsedLines.push(L);
    const col = GRAPH_COLORS[i % GRAPH_COLORS.length];
    if (L.vertical) {
      svg += '<line x1="' + mapX(L.x) + '" y1="' + mapY(ymin) + '" x2="' + mapX(L.x) + '" y2="' + mapY(ymax) + '" stroke="' + col + '" stroke-width="2.5"/>';
    } else {
      svg += '<line x1="' + mapX(xmin) + '" y1="' + mapY(L.m * xmin + L.b) + '" x2="' + mapX(xmax) + '" y2="' + mapY(L.m * xmax + L.b) + '" stroke="' + col + '" stroke-width="2.5"/>';
    }
  });
  // parabolas
  const paras = String(a.parabola || a.parabolas || "").split(/[;|]/).map(s => s.trim()).filter(Boolean);
  paras.forEach((expr, i) => {
    const Q = parseQuadratic(expr); if (!Q) return;
    const col = GRAPH_COLORS[(lines.length + i) % GRAPH_COLORS.length];
    let pts = [];
    for (let x = xmin; x <= xmax + 0.001; x += 0.2) pts.push(mapX(x) + "," + mapY(Q.a * x * x + Q.b * x + Q.c));
    svg += '<polyline points="' + pts.join(" ") + '" fill="none" stroke="' + col + '" stroke-width="2.5"/>';
  });
  // intersection of the first two straight lines
  if (parsedLines.length >= 2 && !parsedLines[0].vertical && !parsedLines[1].vertical && parsedLines[0].m !== parsedLines[1].m) {
    const ix = (parsedLines[1].b - parsedLines[0].b) / (parsedLines[0].m - parsedLines[1].m);
    const iy = parsedLines[0].m * ix + parsedLines[0].b;
    if (ix >= xmin && ix <= xmax && iy >= ymin && iy <= ymax) {
      svg += '<circle cx="' + mapX(ix) + '" cy="' + mapY(iy) + '" r="5.5" fill="#fff" stroke="#e0392b" stroke-width="2.5"/>';
      svg += '<text x="' + (mapX(ix) + 9) + '" y="' + (mapY(iy) - 7) + '" font-size="11" font-weight="700" fill="#c0392b">(' + (+ix.toFixed(2)) + ", " + (+iy.toFixed(2)) + ')</text>';
    }
  }
  // points
  parsePts(a.points).forEach(([x, y]) => {
    svg += '<circle cx="' + mapX(x) + '" cy="' + mapY(y) + '" r="4.5" fill="#5b5bd6"/>';
    svg += '<text x="' + (mapX(x) + 8) + '" y="' + (mapY(y) - 6) + '" font-size="10.5" fill="#26263a">(' + x + ", " + y + ')</text>';
  });
  svg += '</g></svg>';
  // legend of the equations shown
  const legend = lines.concat(paras).map((e, i) =>
    '<span class="glg" style="color:' + GRAPH_COLORS[i % GRAPH_COLORS.length] + '">&#9644; ' + esc(e) + '</span>').join("");
  feedBlock().innerHTML = '<div class="graphwrap pop">' + svg
    + (legend ? '<div class="glegend">' + legend + '</div>' : "")
    + (a.caption ? '<div class="cap">' + esc(a.caption) + '</div>' : "") + '</div>';
}

// [[machine input="3" rule="2x+1" output="7" fname="f" caption="..."]]
function showMachine(a) {
  const input  = String(a.input  == null ? "" : a.input ).trim();
  const rule   = String(a.rule   == null ? "" : a.rule  ).trim();
  const output = String(a.output == null ? "" : a.output).trim();
  const fname  = String(a.fname || "f").trim();
  const stage = feedBlock();
  const wrap = document.createElement("div"); wrap.className = "machine pop";
  let html = '<div class="mflow">';
  html += '<div class="mnode min"><div class="mcap">input</div><div class="mval">' + escapeHTML(input) + '</div></div>';
  html += '<div class="marrow">&#10230;</div>';
  html += '<div class="mbox"><div class="mboxlabel">' + styleVars(fname + "(x)") + '</div><div class="mrule">' + styleVars(rule) + '</div></div>';
  html += '<div class="marrow">&#10230;</div>';
  html += '<div class="mnode mout"><div class="mcap">output</div><div class="mval">' + escapeHTML(output) + '</div></div>';
  html += '</div>';
  if (input !== "" && rule !== "") {
    html += '<div class="mwork">' + escapeHTML(machineSub(rule, input)) + (output !== "" ? " = " + escapeHTML(output) : "") + '</div>';
  }
  if (fname && input !== "" && output !== "") {
    html += '<div class="mfx">' + escapeHTML(fname) + '(' + escapeHTML(input) + ') = ' + escapeHTML(output) + '</div>';
  }
  if (a.caption) html += '<div class="cap">' + escapeHTML(a.caption) + '</div>';
  wrap.innerHTML = html;
  stage.appendChild(wrap);
}

// One equation/expression row. If it has an "=", split into left | = | right so
// columns line up down the board; otherwise render it centered on its own.
// Shrink a just-appended board row until its content fits on ONE line (see the
// .wrow nowrap note in the CSS). Runs after layout; a no-op for normal short lines.
function fitRow(row) {
  try {
    let size = parseFloat(getComputedStyle(row).fontSize) || 33;
    let guard = 0;
    while (row.scrollWidth > row.clientWidth + 1 && size > 14 && guard++ < 20) {
      size -= 2; row.style.fontSize = size + "px";
    }
  } catch (e) {}
  return row;
}

function eqRow(eqText) {
  const s = String(eqText == null ? "" : eqText).trim();
  const row = document.createElement("div"); row.className = "wrow";
  const i = s.indexOf("=");
  if (i >= 0) {
    const left = s.slice(0, i).trim(), right = s.slice(i + 1).trim();
    row.innerHTML = '<span class="wl">' + styleVars(left) + '</span>'
      + '<span class="we">=</span><span class="wr">' + styleVars(right) + '</span>';
  } else {
    row.classList.add("solo");
    row.innerHTML = '<span class="wl">' + styleVars(s) + '</span>';
  }
  return row;
}

// The operation applied to BOTH sides, shown under each side (e.g. "- 1" under the
// left and "- 1" under the right), so the student SEES it done to both sides.
function opRow(opText) {
  const op = styleVars(String(opText == null ? "" : opText).trim());
  const row = document.createElement("div"); row.className = "worow";
  row.innerHTML = '<span class="ol">' + op + '</span><span class="oe"></span><span class="orr">' + op + '</span>';
  return row;
}

// ---------- build oz: THE RE-STATED SNAPSHOT SUPERSEDES THE OLD ONE ----------
// Jim: "nothing has changed. We're just marching straight down." The measurement
// says why, and it is NOT that the tutor is doing anything wrong: rule 35 makes
// him RE-STATE the whole equation every turn (build jg, from Jim's own earlier
// complaint that the original scrolled out of sight). So each turn draws a fresh
// block whose first line repeats the last block's first line, and six turns of one
// problem stack six near-identical snapshots down the board.
//
// When this turn's board opens with the SAME line the previous block opened with,
// that previous block is a superseded snapshot. It COLLAPSES to a single quiet row
// -- one click brings it back, nothing is deleted -- so the board shows the CURRENT
// state of the working plus the history, folded, instead of a column of ghosts.
let _supCssDone = false;
function supersedeCss() {
  if (_supCssDone) return; _supCssDone = true;
  const st = document.createElement("style");
  // ⚠️ ONE QUIET CHIP, NOT A STACK OF BARS. The first version gave every superseded
  // snapshot its own full-width summary row, and a six-turn problem then showed five
  // grey bars filling the board -- I replaced a column of ghosts with a column of
  // labels, which is not better. Superseded blocks are simply hidden; the live block
  // carries ONE small chip that brings them all back.
  st.textContent =
    ".mblock.superseded{display:none}" +
    ".feed.show-earlier .mblock.superseded{display:flex}" +
    ".supchip{align-self:center;background:#f4f5fb;border:1px solid #e7e6f2;" +
    "border-radius:999px;padding:3px 12px;font:inherit;font-size:12px;font-weight:700;" +
    "color:#8288a0;cursor:pointer;margin-bottom:6px}" +
    ".supchip:hover{background:#eceefa;color:#5b5bd6}";
  document.head.appendChild(st);
}

// ONE chip on the live block: "5 earlier steps", click to show them all again.
function supChip(liveBlock) {
  try {
    const n = feed.querySelectorAll(".mblock.superseded").length;
    let c = liveBlock.querySelector(".supchip");
    if (!c) {
      c = document.createElement("button");
      c.type = "button"; c.className = "supchip";
      c.addEventListener("click", function () {
        feed.classList.toggle("show-earlier");
        paintChip(c);
      });
      liveBlock.insertBefore(c, liveBlock.firstChild);
    }
    paintChip(c);
  } catch (e) {}
}
function paintChip(c) {
  const n = feed.querySelectorAll(".mblock.superseded").length;
  const open = feed.classList.contains("show-earlier");
  c.textContent = (open ? "\u25be hide" : "\u25b8 show") + " the " + n
    + " earlier step" + (n === 1 ? "" : "s");
}

// The first equation of a block, as plain text -- the identity of the snapshot.
function _firstLine(block) {
  try {
    const r = block.querySelector(".worklist .wrow");
    if (!r) return "";
    return (r.textContent || "").replace(/\s+/g, " ").trim();
  } catch (e) { return ""; }
}

function supersedePrevious(wl) {
  try {
    const self = wl.closest(".mblock") || wl.parentElement;
    // ⚠️ (pw) THE COMPARISON THIS FUNCTION IS NAMED FOR WAS NEVER MADE. The comment
    // above says a block folds when THIS turn's board "opens with the SAME line the
    // previous block opened with" -- that is what makes it a superseded SNAPSHOT of
    // one problem. _firstLine(self) was computed and then only tested for emptiness;
    // _firstLine(k) was never called at all, so EVERY earlier written block folded,
    // whatever problem it belonged to.
    // Jim's order-of-operations screenshot is what that looks like: "3 + 2 x 5" and
    // the worked "6 + 4 x 2" both hidden behind "show the 5 earlier steps" while the
    // board sits 90% empty and the tutor talks about work the child cannot see. It
    // is his standing rule broken by a missing `if`: whatever he is saying has to be
    // visible without the student moving anything.
    const mine = _firstLine(self);
    if (!mine) return;
    const kids = feed.children;
    let seenSelf = false;
    for (let i = kids.length - 1; i >= 0; i--) {
      const k = kids[i];
      if (!k.classList) continue;
      // Stop at the last FOLDED problem: everything before it is already history,
      // and everything after it belongs to the problem being worked now.
      if (k.classList.contains("probdone")) return;
      if (!k.classList.contains("mblock")) continue;
      if (!seenSelf) { seenSelf = true; continue; }      // this turn's own block
      if (k.classList.contains("superseded")) continue;  // already folded; keep walking
      // ⚠️ ONLY WRITTEN WORK IS SUPERSEDED. A block carrying a FIGURE -- a graph, a
      // triangle, a number line -- is not a re-statement of anything and must stay
      // on the board; the whole point of drawing it was that the child can look at
      // it while they work. First draft collapsed those too, which would have
      // deleted the picture out from under the question about it.
      if (!k.querySelector(".worklist") || k.querySelector(".mfig, .graphwrap, "
          + ".colmath, .objwrap, .scale, .machine, .solveboard, .steprow")) continue;
      // (pw) A DIFFERENT PROBLEM IS NOT A STALE SNAPSHOT OF THIS ONE. Only a block
      // that opens with the same first line is a re-statement, and only that folds.
      if (_firstLine(k) !== mine) continue;
      supersedeCss();
      k.classList.add("superseded");
      // (pw) A BLOCK THAT FOLDS TAKES ITS OWN CHIP WITH IT. Caught by this build's
      // drive: the live chip read "show the 1 earlier step" while TWO were folded,
      // because an older block had been given a chip and was then superseded itself,
      // carrying a stale count into the hidden pile. One chip, on the live block.
      const stale = k.querySelector(".supchip");
      if (stale) stale.remove();
      supChip(self);
      // keep walking: EVERY earlier snapshot of this problem folds, so the board
      // shows the current state of the work and its history, folded -- not a column
      // of ghosts. (Jim: "we're just marching straight down.")
    }
  } catch (e) {}
}

// ---------- build oz: THE WORKLIST FLOWS ACROSS, NOT DOWN ----------
// Measured on Jim's own algebra2 session: a 1,732px board with the work in a
// 560px column down the middle, and 1,593px of scrolling for one problem. Rows
// now fill a column and then continue in the NEXT column to the right, so a long
// solve uses the width it has. A short turn produces one column and looks exactly
// as it always did -- which is why every existing board pin still holds.
const WCOL_ROWS = 4;          // equation rows per column before it moves right

function workCol(wl) {
  let col = wl.lastElementChild;
  if (!col || !col.classList || !col.classList.contains("wcol")
      || col.querySelectorAll(".wrow").length >= WCOL_ROWS) {
    col = document.createElement("div");
    col.className = "wcol";
    wl.appendChild(col);
  }
  return col;
}

// The check line and the caption belong to the whole solve, so they sit in the
// WORKLIST itself (full width, under the columns), never inside a column.
function setWorkCap(wl, capText) {
  const old = wl.querySelector(".wcap"); if (old) old.remove();
  if (capText) { const cap = document.createElement("div"); cap.className = "wcap"; cap.textContent = capText; wl.appendChild(cap); }
}

// [[step eq="2X + 1 = 25"]]            -> add one equation line
// [[step op="- 1" eq="2X = 24"]]       -> show "- 1" under both sides, then the result
// [[step op="/ 2" eq="X = 12"]]        -> next step
// [[step check="2(12) + 1 = 25 ✓"]]    -> a substitution-check line at the end
function showStep(a) {
  const wl = getWorklist();
  const oldCap = wl.querySelector(".wcap"); if (oldCap) oldCap.remove();   // keep any caption last
  const eq = a.eq || a.result || a.line || a.text || "";
  // build oz: an operation and the line it produces are ONE move -- they must not
  // be split across a column break, or the "- 1" ends up orphaned at the bottom of
  // one column with its result at the top of the next.
  let col = workCol(wl);
  if (a.op && eq && col.querySelectorAll(".wrow").length >= WCOL_ROWS - 1) {
    col = workCol(wl);   // (the current one is full enough that the pair would split)
  }
  const wasEmpty = !wl.querySelector(".wrow");
  if (a.op) fitRow(col.appendChild(opRow(a.op)));
  if (eq) fitRow(col.appendChild(eqRow(eq)));
  // build oz: the moment this turn's first line exists, fold away the previous
  // snapshot if it was the same problem re-stated.
  if (wasEmpty && wl.querySelector(".wrow")) supersedePrevious(wl);
  if (a.check) { const c = document.createElement("div"); c.className = "wcheck"; c.innerHTML = checkHTML(a.check); wl.appendChild(c); }
  if (a.cap || a.caption) setWorkCap(wl, a.cap || a.caption);
  scrollFeed();
}

// build oz -- Jim: "why don't they just create a space or something instead of
// having this vertical bar separating it, which is confusing." A check that
// compares two sides is written "left | right"; the bar used to be rendered
// literally, in a green line of maths, where it reads as notation. Now each side
// becomes its own cell with real space between them.
function checkHTML(text) {
  const parts = String(text == null ? "" : text).split("|")
    .map(s => s.trim()).filter(Boolean);
  if (parts.length < 2) return styleVars(String(text || ""));
  // ⚠️ THE SPACING IS INLINE, DELIBERATELY. session.html does NOT load board.css --
  // it carries its own inline copy of the board styles -- so a rule added to the
  // stylesheet reached the pilot page and nothing else. The first version of this
  // shipped exactly that way and rendered "2(5 - 1) + 3 = 115 + 6 = 11", which is
  // worse than the bar Jim complained about. Inline styles cannot be missed by a
  // page that never loaded the sheet.
  return parts.map(function (p, i) {
    return '<span style="display:inline-block;margin:0 18px;'
      + (i ? "padding-left:34px;border-left:2px dashed #b6e0c9;" : "")
      + '">' + styleVars(p) + "</span>";
  }).join("");
}

// ---- Column arithmetic (place-value aligned add/subtract) ----
// [[column op="+" terms="2.40 | 1.35" result="3.75" caption="line up the points"]]
// Stacks the numbers so every decimal point lines up, draws the operator + a rule line,
// and (only when the tutor supplies it) the result below. result is OPTIONAL so the board
// never runs ahead of the student -- omit it until they've found the answer.
function splitNum(t) {
  const s = String(t == null ? "" : t).trim();
  const dot = s.indexOf(".");
  if (dot < 0) return { ip: s, fp: "" };
  return { ip: s.slice(0, dot), fp: s.slice(dot) };   // fp keeps the leading "."
}

function colOp(op) {
  const o = String(op == null ? "" : op).trim().toLowerCase();
  if (o === "-" || o === "−" || o === "minus" || o === "subtract") return "−";
  if (o === "x" || o === "*" || o === "×" || o === "times") return "×";
  if (o === "/" || o === "÷" || o === "divide" || o === "divided") return "÷";
  return "+";
}

// build jc (2026-08-19, Jim watching a live column-addition lesson): THE COLUMN
// REDRAWS ITSELF, AND THE NEW MARKS ARE RED. "As you complete steps, what you just
// did disappears off the top of the screen... it would be better if they restated
// what it looked like -- the three underneath the eight and five in red, and the one
// carried above the tens column in red -- so we could see the original problem with
// the progress we made." Before this, a demonstration emitted one [[step]] line per
// stage ("ones: 4 + 7 = 11", "write 1, carry 1") and the PROBLEM scrolled away, so the
// student was reading a transcript of arithmetic instead of watching a sum being
// worked. Now the tutor re-emits the SAME [[column]] each step with the marks made so
// far -- carries="1_" (right-aligned above the columns) and partial="43" (the answer
// digits written so far) -- and the board redraws the whole problem in place.
// WHAT IS NEW IS RED, and the page works that out ITSELF by diffing against the last
// render of this same problem, so the model only has to state the current state and
// cannot get the highlighting wrong. Blanks are "_", "." or a space; both strings are
// RIGHT-ALIGNED to the ones column, so a carry above the tens is just "1_".
let _colState = {};

function _colDigits(s) {
  return String(s == null ? "" : s).split("")
    .map(function (c) { return (c === "_" || c === "." || c === " ") ? "" : c; });
}

function showColumn(a) {
  const terms = String(a.terms || a.nums || a.lines || "").split(/\s*\|\s*/).map(s => s.trim()).filter(Boolean);
  if (!terms.length) return;
  const op = colOp(a.op);
  // BUILD di (audit finding S-9): align="last" deliberately stacks the numbers by
  // their LAST DIGIT -- the wrong way -- so the tutor can SHOW a student why the
  // last-digit rule fails instead of describing it in words (the audit's student
  // asked to SEE it twice and got prose labels). Amber "wrong way" styling plus a
  // built-in badge so it can never be mistaken for the taught method; the whole
  // number goes into the integer cell, so every row right-aligns on its final
  // digit. A result row is REFUSED in this mode -- the wrong layout is never
  // completed on our board (rules 13 and 26).
  const wrongAlign = String(a.align || "").trim().toLowerCase() === "last";
  const stage = feedBlock();
  const box = document.createElement("div"); box.className = "colmath pop" + (wrongAlign ? " colwrong" : "");

  // build jc: the carry row and the partial-answer row, with new marks in red.
  const carries = String(a.carries || a.carry || "");
  const partial = String(a.partial || a.sofar || "");
  const key = op + "||" + terms.join("|");
  const prev = (!wrongAlign && _colState[key]) ? _colState[key] : { carries: "", partial: "" };
  const addDigitRow = (rowCls, nowStr, wasStr) => {
    const now = _colDigits(nowStr), was = _colDigits(wasStr);
    const cop = document.createElement("div"); cop.className = "cop";
    const mid = document.createElement("div"); mid.className = "cip " + rowCls;
    const offset = now.length - was.length;          // both rows are right-aligned
    now.forEach((d, i2) => {
      const sp = document.createElement("span"); sp.className = "dig";
      if (d) {
        const k = i2 - offset;
        const before = (k >= 0 && k < was.length) ? was[k] : "";
        if (before !== d) sp.classList.add("cnew");  // THIS is what turns it red
        const inner = document.createElement("i"); inner.textContent = d;
        sp.appendChild(inner);
      }
      mid.appendChild(sp);
    });
    const cfp = document.createElement("div"); cfp.className = "cfp";
    box.appendChild(cop); box.appendChild(mid); box.appendChild(cfp);
  };

  if (carries && !wrongAlign) addDigitRow("ccarry", carries, prev.carries);

  const addRow = (num, showOp, resClass) => {
    const rc = resClass ? " cres" : "";
    const parts = wrongAlign ? { ip: String(num), fp: "" } : splitNum(num);
    const cop = document.createElement("div"); cop.className = "cop" + rc; cop.textContent = showOp ? op : "";
    const cip = document.createElement("div"); cip.className = "cip" + rc; cip.textContent = parts.ip;
    const cfp = document.createElement("div"); cfp.className = "cfp" + rc; cfp.textContent = parts.fp;
    box.appendChild(cop); box.appendChild(cip); box.appendChild(cfp);
  };
  // Operator sits on the LAST addend (like on paper). One addend => no operator shown.
  terms.forEach((t, i) => addRow(t, terms.length > 1 && i === terms.length - 1, false));
  const rule = document.createElement("div"); rule.className = "crule"; box.appendChild(rule);
  const res = String(a.result || a.sum || a.answer || a.total || "").trim();
  if (res && !wrongAlign) addRow(res, false, true);   // never complete the wrong layout
  else if (partial && !wrongAlign) addDigitRow("cpart", partial, prev.partial);
  if (wrongAlign) { const w = document.createElement("div"); w.className = "cwarn"; w.textContent = "\u26a0 lined up by the LAST digit \u2014 the wrong way"; box.appendChild(w); }
  if (a.caption || a.cap) { const c = document.createElement("div"); c.className = "ccap"; c.textContent = (a.caption || a.cap); box.appendChild(c); }
  if (!wrongAlign && (carries || partial)) {
    if (Object.keys(_colState).length > 24) _colState = {};   // never grows without bound
    _colState[key] = { carries: carries, partial: partial };
  }
  stage.appendChild(box); scrollFeed();
}
// [[write lines="2X + 1 = 15 | X = 7" caption="..."]] -- legacy catch-all. It now
// APPENDS its line(s) to the same persistent worklist (so it STACKS instead of
// replacing the board). Prefer [[step]]; this is kept so older behavior still works.
function showWrite(a) {
  const wl = getWorklist();
  const lines = String(a.lines || a.text || "").split(/\s*\|\s*/).map(s => s.trim()).filter(Boolean);
  for (const ln of lines) fitRow(workCol(wl).appendChild(eqRow(ln)));   // build oz: flows across
  if (a.caption || a.cap) setWorkCap(wl, a.caption || a.cap);
  scrollFeed();
}

// [[solve start="2x + 1 = 11" steps="subtract 1 from both sides : 2x = 10 | divide both sides by 2 : x = 5" caption="..."]]
// A worked solution that MARCHES DOWN the board: the starting equation on top, then
// each operation (the note before ":") and the resulting equation below it. Each row
// cascades in, so re-sending it with one more step makes the board grow line by line.
function showSolve(a) {
  const start = String(a.start || a.top || "").trim();
  const steps = String(a.steps || "").split(/\s*\|\s*/).map(s => s.trim()).filter(Boolean);
  const rows = [];
  if (start) rows.push('<div class="sline start">' + styleVars(start) + '</div>');
  for (const st of steps) {
    const i = st.indexOf(":"); let op = "", eq = st;
    if (i >= 0) { op = st.slice(0, i).trim(); eq = st.slice(i + 1).trim(); }
    if (op) rows.push('<div class="sop"><span class="sarrow">↓</span> ' + escapeHTML(op) + '</div>');
    rows.push('<div class="sline">' + styleVars(eq) + '</div>');
  }
  let html = rows.map((r, i) => r.replace(/^<div /, '<div style="animation-delay:' + (i * 0.14).toFixed(2) + 's" ')).join("");
  if (a.caption) html += '<div class="scap">' + escapeHTML(a.caption) + '</div>';
  const stage = feedBlock();
  const wrap = document.createElement("div"); wrap.className = "solveboard"; wrap.innerHTML = html;
  stage.appendChild(wrap);
}

// ---------- The transcript feed (tutor chat + student chat + worked math) ----------
// Everything appends to #feed and is RETAINED (scroll up/down). addBubble adds a chat
// bubble; the worked-math blocks append right after the tutor's words on that turn.
function clearHint() { const h = feed.querySelector(".stage-hint"); if (h) h.remove(); }

// build ir (2026-08-19): the blank that lets a SHORT new turn sit at the visible top.
// Lives as the feed's LAST child (re-appended only when content landed after it, so
// the childList observer can't loop on our own housekeeping); height is set by
// scrollFeed each pass and is zero whenever the view pins to the bottom.
function feedPadEl() {
  let p = document.getElementById("feedPad");
  if (!p) {
    p = document.createElement("div"); p.id = "feedPad";
    p.style.flex = "0 0 auto"; p.style.height = "0px";
    p.setAttribute("aria-hidden", "true");
    feed.appendChild(p);
  }
  if (p.nextSibling) feed.appendChild(p);   // keep the blank BELOW the newest work
  return p;
}


// =============================================================================
// BUILD pu (2026-08-28) -- SHRINK THE PICTURE UNTIL THE TURN FITS THE BOARD.
// -----------------------------------------------------------------------------
// Jim: "we're still having Mr. Cadabra talking about a problem that is not
// immediately visible on the whiteboard, so the student either has to scroll up to
// what are you talking about or scroll down to where is it at. Whatever he's saying
// needs to be visible on the whiteboard without the student moving anything."
//
// MEASURED FIRST, in a real browser (tools/puedrive.py), and the scripted lane came
// back CLEAN -- every authored beat's own board work is on screen at 1280x800 and
// 1280x600. The LIVE lane is where it breaks: one reply (a number line, three worked
// steps, then the question) is 406px of content, and on a 1280x600 window the board
// is 335px, so 90px sits ABOVE THE FOLD. The reply says "look back at the number
// line" while the number line is off the top of the screen.
//
// ⚠️ THE CAUSE IS BUILD ns's OWN FIX. Follow-the-pen anchors to
// max(turnTop - 6, natural - clientHeight); once a turn outgrows the window the
// second term wins, so the END of the turn is pinned to the bottom and the TOP of
// the SAME turn scrolls away. ns guaranteed the newest line is never below the fold.
// It never guaranteed the picture that line refers to is still on screen.
//
// 406px will not fit in 335px, so something has to give, and Jim chose the picture.
// Build pc raised the figure caps so pictures could be BIG (je 660, nw 1100, ox 1500);
// this is the reciprocal rule it never had -- never so big that the turn stops
// fitting. A figure's <svg> is sized "width:100%;max-width:Npx;height:auto", so its
// height follows its width: shrinking max-width shrinks the picture and keeps its
// aspect exactly.
//
// DO NO HARM: the original max-width is stashed on the node and RESTORED before every
// measurement, so a window that grows back gets its full-size picture back, and a turn
// that already fits is never touched at all.
//
// ⚠️⚠️ NECESSARY BUT NOT SUFFICIENT, AND THE MEASUREMENT SAYS SO PLAINLY. With the
// fitter running, that same live turn at 1280x600 breaks down as:
//        bubble (five sentences of prose)   190px
//        the number line                    143px  ->  35px at the 190 floor
//        four [[step]] rows                 206px
//        ------------------------------------------
//        TEXT ALONE                         396px   in a 335px board
// The picture was never the problem. Crushing it to nothing recovered 108px and the
// turn STILL did not fit, because five prose sentences plus four board rows cannot fit
// a short window whatever the picture does. This fitter is the right guard for a turn
// a big FIGURE dominates (build pc lets a figure reach 1500px, and one of those really
// can own the board on its own). It is not the fix for a turn the WORDS dominate.
// That one is turn length, and it is the next build. Recorded here rather than
// quietly hoped away.
// ⚠️ THE FLOOR IS HIGH ON PURPOSE, and the drive is why. At 190 the fitter crushed a
// number line from 787px wide to 190px -- it recovered 108px of height and left the
// child squinting at the very thing the tutor was pointing to, which is a worse
// failure than scrolling. 340px still reads. See the measured composition below.
var FIG_FIT_MIN = 340;      // legibility floor -- never shrink a figure below this

function fitTurnToBoard(turnTop) {
  try {
    if (!lastTurnEl || !lastTurnEl.isConnected) return;
    var vh = feed.clientHeight;
    if (!vh) return;
    // collect this turn's figures: lastTurnEl and every sibling after it
    var svgs = [], n = lastTurnEl;
    while (n) {
      if (n.nodeType === 1 && n.id !== "feedPad") {
        var here = n.querySelectorAll ? n.querySelectorAll(".mfig svg") : [];
        for (var i = 0; i < here.length; i++) svgs.push(here[i]);
      }
      n = n.nextSibling;
    }
    // ALWAYS restore first -- this is what lets the picture grow back
    var touched = false;
    for (var j = 0; j < svgs.length; j++) {
      var o = svgs[j].getAttribute("data-pu-maxw");
      if (o !== null) { svgs[j].style.maxWidth = o; touched = true; }
    }
    if (!svgs.length) return;
    if (touched) void feed.offsetHeight;            // reflow at full size before measuring

    var pad = feedPadEl();
    var natural = feed.scrollHeight - pad.offsetHeight;
    var over = (natural - turnTop) - vh;
    if (over <= 1) return;                          // it fits: nothing to do

    var figH = 0;
    for (var k = 0; k < svgs.length; k++) figH += svgs[k].offsetHeight;
    if (figH <= 0) return;                          // no picture to give: leave it alone

    // ⚠️ ONE PASS IS NOT ENOUGH, and the drive proved it: shrinking a figure reflows
    // everything under it, so the first factor is only an estimate (the first cut
    // closed 0 of a measured 90px overage). Iterate until it fits or the floor stops
    // us -- three passes is plenty and is bounded work.
    for (var pass = 0; pass < 3 && over > 1; pass++) {
      figH = 0;
      for (var k2 = 0; k2 < svgs.length; k2++) figH += svgs[k2].offsetHeight;
      if (figH <= 0) break;
      var factor = (figH - over) / figH;
      if (!(factor > 0)) factor = 0.35;             // take as much as the floor allows
      var moved = false;
      for (var m = 0; m < svgs.length; m++) {
        var el = svgs[m];
        if (el.getAttribute("data-pu-maxw") === null) {
          el.setAttribute("data-pu-maxw", el.style.maxWidth || "");
        }
        var w = el.getBoundingClientRect().width;
        if (!w) continue;
        var want = Math.max(FIG_FIT_MIN, Math.round(w * factor));
        if (Math.abs(want - w) > 2) { el.style.maxWidth = want + "px"; moved = true; }
      }
      if (!moved) break;                            // every figure is at the floor
      void feed.offsetHeight;                       // reflow, then measure again
      natural = feed.scrollHeight - pad.offsetHeight;
      over = (natural - turnTop) - vh;
    }
  } catch (e) {}
}

function scrollFeed() {
  requestAnimationFrame(() => {
    if (!stickBottom) return;
    if (lastTurnEl && lastTurnEl.isConnected) {
      // build ir (2026-08-19, Jim's ruling): a tutor turn ALWAYS starts at the top of
      // the visible board -- history above (scroll up), his board work filling in
      // below. (Build ax did this only for turns taller than the window; short turns
      // pinned bottom, and Jim's eyes had to hunt the bottom edge every time.)
      const pad = feedPadEl();
      let turnTop = lastTurnEl.getBoundingClientRect().top - feed.getBoundingClientRect().top + feed.scrollTop;
      // (pu) BEFORE anchoring, make the turn FIT. Jim's rule: whatever he is saying
      // must be visible without the student moving anything. Anchoring can only
      // choose WHICH part of an over-tall turn to hide; this stops it being over-tall.
      fitTurnToBoard(turnTop);
      turnTop = lastTurnEl.getBoundingClientRect().top - feed.getBoundingClientRect().top + feed.scrollTop;
      const natural = feed.scrollHeight - pad.offsetHeight;    // real content, without the blank
      const extra = Math.max(0, Math.round(turnTop + feed.clientHeight - natural));
      if (Math.abs(pad.offsetHeight - extra) > 1) pad.style.height = extra + "px";
      // build ns (2026-08-25): FOLLOW THE PEN. The turn starts at the top (ir) --
      // but once its board work has outgrown the window (a keyboard-shortened
      // board, a long worked example), the newest line used to land BELOW the fold
      // and the child had to scroll (Jim, twice). The anchor now advances just far
      // enough to keep the END of the content visible: top-anchored while the turn
      // fits, following the writing once it does not. The question lands last, so
      // the question is always on screen when it is asked.
      const target = Math.max(0, turnTop - 6, natural - feed.clientHeight);
      if (Math.abs(feed.scrollTop - target) > 1) { autoScroll = true; feed.scrollTop = target; }
      return;
    }
    const pad = document.getElementById("feedPad");
    if (pad && pad.offsetHeight) pad.style.height = "0px";     // pin-bottom mode: no blank
    const target = feed.scrollHeight;
    if (Math.abs(feed.scrollTop - target) > 1) { autoScroll = true; feed.scrollTop = target; }
  });
}

// build nr (2026-08-25): THE BOARD ANSWERS FOR ITS OWN SIZE. When the typed-answer
// bar (with its symbol strip) opens, the feed SHRINKS -- and until now nothing
// noticed, so the tutor's question slid below the fold and the CHILD had to scroll
// (Jim: "we have to scroll so the student doesn't have to"). A ResizeObserver on
// the feed re-runs the anchoring on ANY size change: grow, shrink, strip wrapping
// to a second row, a tablet rotating. Armed lazily from addBubble because `feed`
// is a page global that does not exist when this file parses.
let _feedRO = null;
function feedResized() {
  // build ns: scrollFeed's anchored mode now follows the pen on its own, so a
  // resize only needs to RE-RUN the placement -- no special shrink branch. (nr's
  // branch repaired the resize MOMENT and missed the already-small STATE; the
  // invariant now lives in one place, scrollFeed.)
  if (!feed.clientHeight) return;       // hidden/collapsed layout: nothing to place
  if (!stickBottom) return;             // the student scrolled away -- their board
  scrollFeed();
}
function armFeedWatch() {
  if (_feedRO || typeof ResizeObserver === "undefined" || typeof feed === "undefined" || !feed) return;
  _feedRO = new ResizeObserver(() => feedResized());
  _feedRO.observe(feed);
}

/* ---- THE OWNER'S FLAG (build nq, 2026-08-25) ----------------------------------
   Owner-only: the button exists only when localStorage holds the admin key this
   device was blessed with on /admin. The key gates BOTH sides -- no key means no
   button here, and the server 403s /api/flag without it -- so no student, parent,
   or teacher can ever see or use this. */
function ownerFlagKey() {
  try { return (localStorage.getItem("mt_owner_key") || "").trim(); }
  catch (e) { return ""; }
}
let _flagCssDone = false;
function ownerFlagCss() {
  if (_flagCssDone) return; _flagCssDone = true;
  const st = document.createElement("style");
  st.textContent =
    ".mtflag{position:absolute;top:2px;right:4px;border:0;background:transparent;" +
    "cursor:pointer;font-size:15px;line-height:1;opacity:.55;padding:2px;}" +
    ".mtflag:hover{opacity:1;}" +
    ".mtflag.sent{opacity:1;cursor:default;}";
  document.head.appendChild(st);
}
function ownerFlagAttach(div) {
  const key = ownerFlagKey();
  if (!key) return;                       // everyone but the owner exits here
  ownerFlagCss();
  div.style.position = "relative";
  const btn = document.createElement("button");
  btn.type = "button"; btn.className = "mtflag"; btn.textContent = "\u{1F6A9}";
  btn.title = "Flag this for correction (owner)";
  btn.addEventListener("click", function () {
    if (btn.classList.contains("sent")) return;
    // Quote from a CLONE with the button stripped, AT TAP TIME, so streamed-in
    // board work is included and the flag never quotes its own button.
    const clone = div.cloneNode(true);
    clone.querySelectorAll(".mtflag").forEach(function (b) { b.remove(); });
    const quote = (clone.textContent || "").replace(/\s+/g, " ").trim().slice(0, 600);
    const note = prompt("What's wrong with this line? (what SHOULD it say?)");
    if (note === null) return;            // owner changed his mind -- write nothing
    const body = {
      page: (location.pathname.split("/").pop() || "").replace(".html", "") || "board",
      course: (typeof COURSE !== "undefined" ? COURSE : ""),
      code: (typeof CODE !== "undefined" ? CODE : ""),
      quote: quote,
      note: (note || "").trim().slice(0, 400)
    };
    fetch("/api/flag", {
      method: "POST",
      headers: { "Content-Type": "application/json", "X-Admin-Key": key },
      body: JSON.stringify(body)
    }).then(function (r) {
      if (r.ok) { btn.textContent = "\u2705"; btn.classList.add("sent"); btn.title = "Flagged -- it's in your queue on /admin"; }
      else { alert("Flag not saved (" + r.status + "). Is the owner key on this device still current? Re-enable it from /admin."); }
    }).catch(function () {
      alert("Flag not saved -- network error. It is safe to try again.");
    });
  });
  div.appendChild(btn);
}

function addBubble(role, text) {
  clearHint();
  const div = document.createElement("div"); div.className = "bubble " + role; div.innerHTML = styleVars(text);
  // 2026-08-07 (build ax): a new bubble re-engages following. A TUTOR bubble anchors
  // the view to the start of his turn; a student/system bubble pins to the bottom.
  lastTurnEl = (role === "tutor") ? div : null;
  stickBottom = true;
  armFeedWatch();                               // build nr: the feed reports its own size from now on
  feed.appendChild(div); scrollFeed();
  if (role === "tutor") ownerFlagAttach(div);   // build nq: owner-only, no-op without the key
  return div;
}
/* I did no harm and this file is not truncated. */
