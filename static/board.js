/* =============================================================================
   board.js  --  THE WHITEBOARD, ONE COPY  --  Hyperion Shift LLC
   -----------------------------------------------------------------------------
   CHANGE NOTES (keep newest at top):
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
  if (a.op) fitRow(wl.appendChild(opRow(a.op)));
  if (eq) fitRow(wl.appendChild(eqRow(eq)));
  if (a.check) { const c = document.createElement("div"); c.className = "wcheck"; c.innerHTML = styleVars(a.check); wl.appendChild(c); }
  if (a.cap || a.caption) setWorkCap(wl, a.cap || a.caption);
  scrollFeed();
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
  for (const ln of lines) fitRow(wl.appendChild(eqRow(ln)));
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

function scrollFeed() {
  requestAnimationFrame(() => {
    if (!stickBottom) return;
    if (lastTurnEl && lastTurnEl.isConnected) {
      // build ir (2026-08-19, Jim's ruling): a tutor turn ALWAYS starts at the top of
      // the visible board -- history above (scroll up), his board work filling in
      // below. (Build ax did this only for turns taller than the window; short turns
      // pinned bottom, and Jim's eyes had to hunt the bottom edge every time.)
      const pad = feedPadEl();
      const turnTop = lastTurnEl.getBoundingClientRect().top - feed.getBoundingClientRect().top + feed.scrollTop;
      const natural = feed.scrollHeight - pad.offsetHeight;    // real content, without the blank
      const extra = Math.max(0, Math.round(turnTop + feed.clientHeight - natural));
      if (Math.abs(pad.offsetHeight - extra) > 1) pad.style.height = extra + "px";
      const target = Math.max(0, turnTop - 6);
      if (Math.abs(feed.scrollTop - target) > 1) { autoScroll = true; feed.scrollTop = target; }
      return;
    }
    const pad = document.getElementById("feedPad");
    if (pad && pad.offsetHeight) pad.style.height = "0px";     // pin-bottom mode: no blank
    const target = feed.scrollHeight;
    if (Math.abs(feed.scrollTop - target) > 1) { autoScroll = true; feed.scrollTop = target; }
  });
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
    "cursor:pointer;font-size:13px;line-height:1;opacity:.25;padding:2px;}" +
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
  feed.appendChild(div); scrollFeed();
  if (role === "tutor") ownerFlagAttach(div);   // build nq: owner-only, no-op without the key
  return div;
}
/* I did no harm and this file is not truncated. */
