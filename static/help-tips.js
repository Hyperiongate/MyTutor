/* =============================================================================
 * help-tips.js  --  MyTutor  --  Hyperion Shift LLC
 * CHANGE NOTES (keep newest at top):
 *   2026-08-07  VOICE-FIRST CLASSROOM (Jim): tips updated to match the restored voice input
 *               and the retired controls. REMOVED the 🧮 Math Keyboard tip (.mtk-open no
 *               longer exists) and the quick-replies tip (the Yes/No/I'm confused row is
 *               gone -- students SAY it now). ADDED a tip on the 🎙️ Tap-to-talk button.
 *               REWORDED the answer-bar tip: talk first, typing as the fallback. The 📈
 *               graph, trophy, and time-tile tips are unchanged.
 *   2026-07-30  NEW shared component (Jim: "scatter little ?-in-a-circle helpers anywhere
 *               someone could get confused"). Plants a small ? button next to known
 *               confusion points and shows a friendly popup bubble on click:
 *                 - the answer bar (how do I answer?)          [session/practice/topic]
 *                 - the 🧮 Math Keyboard button (incl. the correct exponent order)
 *                 - the 📈 Graph button (plot -> line -> send)
 *                 - the quick-reply row (Yes/No/I'm confused/Hint)
 *                 - the 🏆 Trophy case header (what a "check" is; how badges are earned)
 *                 - the "Time this week" tile (why idle time doesn't count)
 *               One bubble at a time; closes on X, outside click, or Escape. Targets are
 *               matched by selector (or label text for generated tiles) with a short RETRY
 *               loop, because several targets are injected asynchronously by other scripts
 *               (math-keyboard.js, graph-input.js, the dashboard's fetch renders). Fully
 *               self-contained: injects its own CSS, no libraries, no storage; a missing
 *               target simply gets no tip. Purely additive -- do no harm.
 * ============================================================================= */
(function () {
  if (window.__mtHelpTips) return;
  window.__mtHelpTips = true;

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  ready(function () {
    // ---- styles ----
    var css = document.createElement("style");
    css.textContent =
      ".hlp-q{display:inline-flex;align-items:center;justify-content:center;width:17px;height:17px;flex:0 0 auto;" +
      "border-radius:50%;border:none;background:#e6e1f8;color:#6d5ae6;font-weight:900;font-size:11.5px;cursor:pointer;" +
      "margin-left:6px;vertical-align:middle;line-height:1;padding:0}" +
      ".hlp-q:hover{background:#6d5ae6;color:#fff}" +
      ".hlp-pop{position:fixed;z-index:99999;max-width:270px;background:#fff;border:1px solid #e5dff7;border-radius:14px;" +
      "box-shadow:0 18px 48px rgba(60,40,120,.25);padding:13px 15px 13px;font-family:inherit}" +
      ".hlp-pop .hlp-t{font-weight:800;font-size:13.5px;color:#20233a;margin:0 22px 5px 0}" +
      ".hlp-pop .hlp-b{font-size:12.5px;color:#5b6079;line-height:1.5;margin:0}" +
      ".hlp-pop .hlp-x{position:absolute;top:7px;right:9px;border:none;background:transparent;color:#9aa0b5;" +
      "font-size:15px;font-weight:800;cursor:pointer;padding:2px;line-height:1}" +
      ".hlp-pop .hlp-x:hover{color:#6d5ae6}";
    document.head.appendChild(css);

    // ---- one popup at a time ----
    var pop = null;
    function closePop() { if (pop) { pop.remove(); pop = null; } }
    document.addEventListener("click", function (e) {
      if (pop && !pop.contains(e.target) && !e.target.classList.contains("hlp-q")) closePop();
    }, true);
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") closePop(); });

    function openPop(btn, tip) {
      closePop();
      pop = document.createElement("div");
      pop.className = "hlp-pop";
      pop.innerHTML = '<button type="button" class="hlp-x" aria-label="Close">✕</button>' +
        '<p class="hlp-t">' + tip.title + '</p><p class="hlp-b">' + tip.body + "</p>";
      document.body.appendChild(pop);
      pop.querySelector(".hlp-x").addEventListener("click", closePop);
      var r = btn.getBoundingClientRect(), pw = pop.offsetWidth, ph = pop.offsetHeight;
      var x = Math.min(Math.max(8, r.left - 20), window.innerWidth - pw - 8);
      var y = r.bottom + 8;
      if (y + ph > window.innerHeight - 8) y = Math.max(8, r.top - ph - 8);
      pop.style.left = x + "px"; pop.style.top = y + "px";
    }

    function attach(el, tip) {
      if (!el || el.dataset.hlpDone) return;
      el.dataset.hlpDone = "1";
      var q = document.createElement("button");
      q.type = "button"; q.className = "hlp-q"; q.textContent = "?";
      q.setAttribute("aria-label", "What's this?");
      q.title = "What's this?";
      q.addEventListener("click", function (e) { e.stopPropagation(); openPop(q, tip); });
      if (tip.inside) el.appendChild(q);
      else el.insertAdjacentElement("afterend", q);
    }

    // ---- the tips (title + body are innerHTML; keep them short and warm) ----
    var TIPS = [
      { sel: "#talkBtn", visibleOnly: true,   // pages hide the mic when recording isn't supported
        title: "Talk with Mr. Cadabra",
        body: "When it's your turn, <b>tap the mic and say your answer out loud</b> — then tap again when you're done. Stuck? Just say <b>\"I'm confused\"</b> or ask for a hint — that tells him to slow down and try a different way. Rather not talk? You can always type instead." },
      { sel: ".gpi-open",
        title: "Graph paper",
        body: "Opens a coordinate grid. <b>Tap</b> to plot a point (tap again to remove it), draw a line through your points if you want one, then <b>Send to tutor</b> — Mr. Cadabra reads your points and checks them with you." },
      { sel: "#chatInput, #input", after: "bar",
        title: "How do I answer?",
        body: "Type your answer and press <b>Enter ⏎</b> — or tap the 🎙️ mic and just say it. Stuck? Tell him <b>\"I'm confused\"</b> or ask for a hint — Mr. Cadabra never minds, and a hint is a nudge, never the whole answer. You can also just ask him how anything on this screen works." },
      { sel: "#trophyWrap .section-h", inside: true,
        title: "Badges, medals & checks",
        body: "A <b>check</b> is a short scored quiz — no hints — you take when you feel ready. Score 80%+ and the unit turns gold and you earn its <b>merit badge</b>. Medals reward the work itself: streaks, real minutes, comebacks. Everything here is earned." },
      { label: "Time this week",
        title: "Real work only",
        body: "The clock runs only while this tab is open <b>and</b> you're actually doing something. Walk away or switch tabs and it stops — so these hours are real enough for a homeschool log." },
    ];

    // ---- placement, with retries (several targets render asynchronously) ----
    var tries = 0;
    function place() {
      tries++;
      TIPS.forEach(function (tip) {
        if (tip.label) {                     // generated dashboard tiles: match by label text
          document.querySelectorAll(".tile .lbl").forEach(function (l) {
            if (l.textContent.trim() === tip.label) attach(l, { title: tip.title, body: tip.body, inside: true });
          });
          return;
        }
        document.querySelectorAll(tip.sel).forEach(function (el) {
          // visibleOnly (2026-08-07): don't plant a "?" next to a hidden target (e.g. the mic
          // button on a browser that can't record) -- a floating orphan ? just confuses.
          if (tip.visibleOnly && el.offsetParent === null) return;
          if (tip.after === "bar") {          // the answer bar: put the ? at the end of the row
            var bar = el.parentNode;
            if (bar && !bar.dataset.hlpDone) { bar.dataset.hlpDone = "1"; attach(bar, { title: tip.title, body: tip.body, inside: true }); }
            return;
          }
          attach(el, tip);
        });
      });
      if (tries < 12) setTimeout(place, 500);   // catch late-rendered targets, then stop
    }
    place();
  });
})();
/* I did no harm and this file is not truncated. */
