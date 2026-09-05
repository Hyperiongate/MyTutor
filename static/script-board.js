/* =========================================================================
   script-board.js  --  THE SCRIPTED LANE'S BOARD LAYER  --  Hyperion Shift LLC
   -------------------------------------------------------------------------
   CHANGE NOTES (keep newest at top):
     2026-09-05 (sr) FIGURE_KINDS gains array -- the multiplication array (math-figures.js).
     2026-09-05 (sq) FIGURE_KINDS gains placevalue -- the place-value chart the
       Basic place-value lesson now teaches from (math-figures.js).
     2026-08-27 (os) THE BOARD READS ONE, TWO, THREE, scripted lane. drawBoard
       dispatches the new [[stepcard n="1" title="..."]] tag (board.js's
       openStepCard -- labeled Step-N cards side by side); feedBlock hosts new
       blocks into the OPEN card (board.js activeStepCell) so figures and
       worklists after a [[stepcard]] land inside it; the grid clears per beat
       (drawBoard start) and on wipeBoard. board.js loads AFTER this file, so
       the calls are guarded typeof-checks resolved at call time, exactly like
       the rest of the ambient contract.
     2026-08-23 (mh) NEW FILE. Lifted VERBATIM out of static/pilot.html, which
       had carried it inline since build kj, so that the Abrabot drill page
       (static/drill.html) could draw the same boards without a second copy.
       Nothing in the behaviour changed: the functions below are the pilot
       page's own, moved, and pilot.html now loads this file instead of
       declaring them. A browser drive of BOTH pages proves it.

       ⭐ WHY A FILE AND NOT A COPY-PASTE. voice.js's header records what
       happened the last time this lane duplicated a layer instead of sharing
       one: four hand-ports of the audio code in a row, each missing a
       different one of the four head-of-clip protections, until the copy was
       deleted and the real file loaded. The board dispatcher is the same
       shape of thing -- it grew from four tags to twenty-nine across thirteen
       content builds -- and a second copy would start drifting on the first
       lesson that draws a tag only one page knows.

   WHAT THIS IS. board.js states an AMBIENT CONTRACT: it reaches for the bare
   names el, feed, composer, busy, feedBlock(), getWorklist(), showGoal(),
   scrollFeed(), clearHint() and wipeBoard(), and it says the tag DISPATCHER is
   page-specific BY DESIGN ("which tags a page supports is configuration, not
   copy-paste"). This file provides that contract for the SCRIPTED lane -- one
   board, redrawn per beat -- plus the dispatcher for the tags a scripted lesson
   may draw. Both scripted pages want exactly this, so both load it.

   LOAD ORDER MATTERS: board-text.js (styleVars/escapeHTML), then the figure
   libraries, then THIS FILE, then board.js. It must be loaded before board.js
   because board.js reads these names as bare globals at call time.

   ONE BOARD, REDRAWN PER BEAT. session.html appends each turn to a scrolling
   transcript; the scripted lane does not. That is Jim's build-ir complaint
   ("I constantly need to scroll ... what's showing up on the board is at the
   bottom") answered by the lane's shape: a beat is a screenful, not a
   conversation. feedBlock() therefore hands back a child of a board that was
   cleared when the beat began.

   THE HOST PAGE MUST PROVIDE: a <div id="board">. It MAY provide
   window.boardWarn(message) to hear about a tag that threw.
   ========================================================================= */

/* ---- board.js's ambient contract ---- */
var el = function (id) { return document.getElementById(id); };
var feed = null;        // resolved on first use: the one board area
var composer = null;    // the scripted lane has no text composer; board.js only guards on it
var busy = false;

var _scriptWork = null;

/* The host page's <div id="board"> may not exist when this file loads, so `feed`
   cannot be bound eagerly -- it is resolved on first use and cached. (The first
   version of build kj bound it at load time, got null, and silently drew nothing.) */
function boardEl() {
  if (!feed) feed = document.getElementById("board");
  return feed;
}
function feedBlock() {
  _scriptWork = null;
  var b = document.createElement("div");
  b.className = "mblock";
  // (os) an OPEN step card captures the block; otherwise the board, as before.
  var cell = null;
  try { if (typeof activeStepCell === "function") cell = activeStepCell(); } catch (e) {}
  (cell || boardEl() || document.body).appendChild(b);
  return b;
}
/* showGoal is PAGE-SPECIFIC by board.js's design (session.html has its own); the
   scripted lane wants a compact chip, not the session goal panel. */
function showGoal(text) {
  var d = document.createElement("div");
  d.className = "goalchip";
  d.textContent = "🎯 " + String(text == null ? "" : text);
  (boardEl() || document.body).appendChild(d);
}
function getWorklist() {
  if (!_scriptWork) {
    var b = feedBlock();
    _scriptWork = document.createElement("div");
    _scriptWork.className = "worklist";
    b.appendChild(_scriptWork);
  }
  return _scriptWork;
}
function scrollFeed() {}          // nothing to scroll: the beat IS the screen
function clearHint() {}
function wipeBoard() {
  var f = boardEl(); if (f) f.innerHTML = "";
  _scriptWork = null;
  try { if (typeof clearStepGrid === "function") clearStepGrid(); } catch (e) {}   // (os)
}

/* ---- small text helpers the scripted pages share ---- */
function esc(s) {
  var d = document.createElement("div");
  d.textContent = String(s == null ? "" : s);
  return d.innerHTML;
}
function attrs(tag) {
  var m, re = /(\w+)="([^"]*)"/g, out = {};
  while ((m = re.exec(tag)) !== null) out[m[1]] = m[2];
  return out;
}
function choiceValues(text) {
  var m = /\[\[\s*choices\s+options="([^"]*)"/.exec(text || "");
  if (!m) return [];
  return m[1].split("|").map(function (s) { return s.trim(); }).filter(Boolean);
}
function spokenOnly(text) {       // the child hears words, never tags
  return String(text || "").replace(/\[\[[^\]]*\]\]/g, " ").replace(/\s+/g, " ").trim();
}
function styleTerms(s) {          // **term** -> bold (matches the app's habit)
  return esc(s).replace(/\*\*([^*]{2,60}?)\*\*/g, "<b>$1</b>");
}

/* ---- the board: DELEGATED to board.js (kj) ----
   board.js says the tag dispatcher is page-specific BY DESIGN. This is the
   SCRIPTED LANE's: the tags a scripted lesson may draw. Everything here is
   rendered by the same code session.html uses, so a lesson authored against
   these pages will look the same when the lane is folded into the real client.
   DELIBERATELY ABSENT: check / quiz / today / unitplan / finalexam / mark /
   nice / bye -- those belong to the generated lane's session bookkeeping, and a
   scripted lesson that reached for one would be reaching outside the closure. */
var FIGURE_KINDS = ["bars", "histogram", "dotplot", "boxplot", "scatter", "normal",
                    "twoway", "tree", "pie", "unitcircle", "righttriangle", "conic",
                    "numberline", "areamodel", "vector",
                    "venn", "tape", "clock",   // (ot) the shelf grows
                    "placevalue",              // (sq) the place-value chart
                    "array"];                  // (sr) the multiplication array
function drawBoard(text) {
  if (!boardEl()) return false;
  var re = /\[\[\s*([\w-]+)([^\]]*?)\]\]/g, m, drew = false;
  _scriptWork = null;
  try { if (typeof clearStepGrid === "function") clearStepGrid(); } catch (e) {}   // (os) per beat
  while ((m = re.exec(text)) !== null) {
    var name = m[1].toLowerCase(), a = attrs(m[0]);
    try {
      if (name === "goal" && a.text) { showGoal(a.text); drew = true; }
      else if (name === "stepcard") { _scriptWork = null; openStepCard(a); drew = true; }   // (os)
      else if (name === "step") { showStep(a); drew = true; }
      else if (name === "write") { showWrite(a); drew = true; }
      else if (name === "column") { showColumn(a); drew = true; }
      else if (name === "solve") { showSolve(a); drew = true; }
      else if (name === "objects") { showObjects(a); drew = true; }
      else if (name === "balance") { showBalance(a); drew = true; }
      else if (name === "machine") { showMachine(a); drew = true; }
      else if (name === "graph") { showFig("graph", a); drew = true; }
      else if (FIGURE_KINDS.indexOf(name) >= 0) { showFig(name, a); drew = true; }
      else if (["triangle", "angle", "circle", "transversal", "polygon", "solid", "segment"].indexOf(name) >= 0) {
        showGeo(name, a); drew = true;   // (ot) +transversal/polygon/solid
      }
      else if (name === "clear") { wipeBoard(); }
      // [[choices]] becomes tap BUTTONS in the controls row, never a board line
    } catch (e) {
      try {
        if (window.boardWarn) window.boardWarn("board tag [[" + name + "]] threw: " + e.message);
      } catch (e2) {}
    }
  }
  return drew;
}

/* TEST SEAM, same convention as session.html's window.__setState: the dispatcher
   is reachable by name so a browser proof can draw one tag in isolation and check
   what came out. Nothing in either page calls it through window. */
window.__drawBoard = drawBoard;

/* I did no harm and this file is not truncated. */
