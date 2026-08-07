/* =============================================================================
 * library.js  --  Math Tutor MVP  --  Hyperion Shift LLC
 * CHANGE NOTES (keep newest at top):
 *   2026-08-07  CONTEXT CHOICES FIRST (build aw, Jim: "students often don't know exactly
 *               what they're looking up"). Opening the overlay now shows CHIP CHOICES drawn
 *               from what's being taught RIGHT NOW on this page -- the red key terms Mr.
 *               Cadabra has bolded (.kterm, newest first), the unit bar's topic ladder,
 *               today's goal, and the practice problem / explored topic -- plus a
 *               "✏️ Something else…" chip that reveals the type-your-own search box. Tap a
 *               chip and the article opens straight away. No page changes needed: the
 *               chips read state the pages already render. If the page has no context yet,
 *               the type-in box shows directly, as before.
 *   2026-08-07  NEW shared component -- the 📖 LOOK IT UP reference library (Jim: a
 *               searchable database of every course's topics; the student reads a
 *               bubble -- the tutor's voice and the chat conversation are NEVER
 *               involved). Included on session.html, practice.html, topic.html.
 *               What it does:
 *                 - Adds a "📖 Look it up" button to the page's left nav (.leftnav).
 *                 - Opens a full-screen overlay: search box -> GET /api/library
 *                   (?q&course&code from the page URL) -> renders the article in a
 *                   big readable bubble. Curated/saved articles return instantly; a
 *                   brand-new topic takes a few seconds while the library writes
 *                   its page once (then it's saved for everyone, forever).
 *                 - The server scrubs article HTML to a safe subset; this file
 *                   renders it inside the bubble only.
 *               Self-contained: injects its own CSS; guarded so a page without
 *               .leftnav is simply skipped. Purely additive -- do no harm.
 * ============================================================================= */
(function () {
  if (window.__mtLibrary) return;
  window.__mtLibrary = true;

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  ready(function () {
    var nav = document.querySelector(".leftnav");
    if (!nav) return;
    var params = new URLSearchParams(window.location.search);
    var CODE = (params.get("code") || "").trim();
    var COURSE = (params.get("course") || "algebra1").trim();
    if (!CODE) return;

    // ---- styles ----
    var css = document.createElement("style");
    css.textContent =
      ".lib-overlay{position:fixed;inset:0;z-index:80;display:none;align-items:flex-start;justify-content:center;" +
      "padding:26px 14px;overflow-y:auto;background:rgba(24,20,50,.55);backdrop-filter:blur(3px)}" +
      ".lib-overlay.show{display:flex}" +
      ".lib-card{background:#fffdf9;border-radius:20px;max-width:720px;width:100%;padding:22px 26px 26px;" +
      "box-shadow:0 30px 80px rgba(20,15,60,.35);font-family:inherit;margin:auto 0}" +
      ".lib-top{display:flex;align-items:center;gap:10px}" +
      ".lib-top .lib-ic{font-size:26px}" +
      ".lib-top h2{margin:0;font-size:20px;color:#2a2450;flex:1}" +
      ".lib-x{border:1px solid #e3def3;background:#fff;color:#5b6079;font-weight:800;border-radius:10px;" +
      "padding:8px 12px;cursor:pointer;font-size:14px}" +
      ".lib-bar{display:flex;gap:8px;margin:14px 0 4px;flex-wrap:wrap}" +
      ".lib-bar input{flex:1 1 220px;min-width:0;font-size:16px;padding:11px 13px;border:1.5px solid #d8d3ec;" +
      "border-radius:12px;outline:none}" +
      ".lib-bar input:focus{border-color:#6d5ae6;box-shadow:0 0 0 3px rgba(109,90,230,.15)}" +
      ".lib-bar button{font-size:15px;font-weight:800;padding:11px 18px;border:none;border-radius:12px;cursor:pointer;" +
      "background:linear-gradient(135deg,#6d5ae6,#1fb6b0);color:#fff;flex:0 0 auto}" +
      ".lib-chips{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 4px}" +
      ".lib-chip{border:1.5px solid #d8d3ec;background:#fff;border-radius:20px;padding:10px 16px;font-size:14.5px;" +
      "font-weight:700;color:#2a2450;cursor:pointer}" +
      ".lib-chip:hover{border-color:#6d5ae6;background:#f6f3ff}" +
      ".lib-chip.alt{color:#5b6079;border-style:dashed}" +
      ".lib-bar.hidden{display:none}" +
      ".lib-hint{font-size:12.5px;color:#7a7694;margin:2px 2px 0}" +
      ".lib-art{display:none;margin-top:14px;border-top:1.5px solid #eee9dc;padding-top:14px}" +
      ".lib-art.show{display:block}" +
      ".lib-art h1{font-size:24px;color:#2a2450;margin:0 0 10px;font-family:Georgia,serif}" +
      ".lib-art h3{font-size:16px;color:#4a3fa0;margin:16px 0 6px}" +
      ".lib-art p{font-size:15.5px;line-height:1.65;color:#33304d;margin:8px 0}" +
      ".lib-art ul,.lib-art ol{font-size:15.5px;line-height:1.6;color:#33304d;margin:8px 0;padding-left:24px}" +
      ".lib-art li{margin:5px 0}" +
      ".lib-art div.ex,.lib-art > div{background:#f6f3ff;border:1px solid #e3def3;border-radius:12px;" +
      "padding:12px 15px;margin:10px 0;font-size:15.5px;line-height:1.7;color:#2a2450}" +
      ".lib-art b{color:#2a2450}" +
      ".lib-status{display:none;margin-top:16px;font-size:15px;color:#5b6079;text-align:center;padding:18px 8px}" +
      ".lib-status.show{display:block}" +
      "@media (max-width:600px){.lib-card{padding:16px}}";
    document.head.appendChild(css);

    // ---- the overlay ----
    var ov = document.createElement("div");
    ov.className = "lib-overlay";
    ov.innerHTML =
      '<div class="lib-card">' +
      '  <div class="lib-top"><span class="lib-ic">📖</span><h2>Look it up</h2>' +
      '    <button type="button" class="lib-x" id="libClose">✕ Close</button></div>' +
      '  <div class="lib-chips" id="libChips"></div>' +
      '  <div class="lib-bar">' +
      '    <input id="libQ" placeholder="What do you want to read about? e.g. the binomial theorem, adding money…" maxlength="160" autocomplete="off" />' +
      '    <button type="button" id="libGo">Look it up</button>' +
      '  </div>' +
      '  <div class="lib-hint">A short reading page opens right here — your lesson stays exactly where you left it.</div>' +
      '  <div class="lib-status" id="libStatus"></div>' +
      '  <div class="lib-art" id="libArt"></div>' +
      "</div>";
    document.body.appendChild(ov);

    var q = document.getElementById("libQ"), art = document.getElementById("libArt"),
        status = document.getElementById("libStatus");

    // What is this page teaching RIGHT NOW? Chips are drawn from state the page already
    // renders: the tutor's bolded key terms (newest first), the unit bar's topic ladder,
    // today's goal, and the practice problem / explored topic. Deduped, capped at 6.
    function currentTopics() {
      var out = [], seen = {};
      function push(t) {
        t = String(t || "").replace(/\s+/g, " ").trim().replace(/[.,;:!?]+$/, "");
        if (t.length < 3 || t.length > 60) return;
        var k = t.toLowerCase();
        if (seen[k] || out.length >= 6) return;
        seen[k] = 1; out.push(t);
      }
      var kt = Array.prototype.slice.call(document.querySelectorAll(".kterm"));
      kt.reverse().forEach(function (e) { push(e.textContent); });          // newest terms first
      document.querySelectorAll("#unitTrack .pbseg").forEach(function (e) { push(e.title); });
      var g = document.getElementById("goalText"); if (g) push(g.textContent);
      var pb = document.getElementById("probText"); if (pb) push(pb.textContent);
      var tb = document.getElementById("topicText"); if (tb) push(tb.textContent);
      return out;
    }
    var chips = document.getElementById("libChips");
    var bar = ov.querySelector(".lib-bar");
    function open() {
      ov.classList.add("show");
      art.classList.remove("show"); art.innerHTML = "";
      status.classList.remove("show");
      chips.innerHTML = "";
      var topics = currentTopics();
      if (topics.length) {
        bar.classList.add("hidden");                       // type-in waits behind "Something else…"
        topics.forEach(function (t) {
          var b = document.createElement("button");
          b.type = "button"; b.className = "lib-chip"; b.textContent = t;
          b.addEventListener("click", function () { q.value = t; lookup(); });
          chips.appendChild(b);
        });
        var other = document.createElement("button");
        other.type = "button"; other.className = "lib-chip alt"; other.textContent = "✏️ Something else…";
        other.addEventListener("click", function () {
          bar.classList.remove("hidden"); q.value = ""; q.focus();
        });
        chips.appendChild(other);
      } else {
        bar.classList.remove("hidden");                    // no context yet — type-in as before
        setTimeout(function () { q.focus(); }, 60);
      }
    }
    function close() { ov.classList.remove("show"); }
    document.getElementById("libClose").addEventListener("click", close);
    ov.addEventListener("click", function (e) { if (e.target === ov) close(); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && ov.classList.contains("show")) close();
    });

    var busy = false;
    // A brand-new topic takes a few seconds while the library writes its page (once,
    // ever) -- keep the student company so the wait reads as work, not a hang.
    var waitLines = ["Checking the library…", "Pulling the right book off the shelf…",
                     "Writing this page for you — first time anyone's asked! One moment…"];
    async function lookup() {
      var query = (q.value || "").trim();
      if (!query || busy) return;
      busy = true;
      art.classList.remove("show"); art.innerHTML = "";
      status.textContent = waitLines[0]; status.classList.add("show");
      var t1 = setTimeout(function () { status.textContent = waitLines[1]; }, 1600);
      var t2 = setTimeout(function () { status.textContent = waitLines[2]; }, 4000);
      try {
        var res = await fetch("/api/library?q=" + encodeURIComponent(query) +
                              "&course=" + encodeURIComponent(COURSE) +
                              "&code=" + encodeURIComponent(CODE));
        var data = await res.json();
        clearTimeout(t1); clearTimeout(t2);
        status.classList.remove("show");
        if (!res.ok) {
          status.textContent = (data && data.detail) || "The library is busy — try again in a moment.";
          status.classList.add("show");
        } else if (!data.body) {
          status.textContent = (data && data.detail) || "I couldn't find that — try different words.";
          status.classList.add("show");
        } else {
          // The server scrubs article HTML to a safe subset before serving.
          art.innerHTML = "<h1>" + String(data.title || "").replace(/&/g, "&amp;").replace(/</g, "&lt;") + "</h1>" + data.body;
          art.classList.add("show");
          art.scrollIntoView({ block: "nearest" });
        }
      } catch (e) {
        clearTimeout(t1); clearTimeout(t2);
        status.textContent = "I couldn't reach the library — check your connection and try again.";
        status.classList.add("show");
      }
      busy = false;
    }
    document.getElementById("libGo").addEventListener("click", lookup);
    q.addEventListener("keydown", function (e) { if (e.key === "Enter") lookup(); });

    // ---- the nav button ----
    var btn = document.createElement("a");
    btn.className = "navbtn"; btn.href = "#"; btn.id = "libraryLink";
    btn.textContent = "📖 Look it up";
    btn.addEventListener("click", function (e) { e.preventDefault(); open(); });
    nav.appendChild(btn);
  });
})();
/* I did no harm and this file is not truncated. */
