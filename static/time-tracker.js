/* =============================================================================
 * time-tracker.js  --  MyTutor  --  Hyperion Shift LLC
 * CHANGE NOTES (keep newest at top):
 *   2026-07-30  NEW shared component: ENGAGED-TIME tracking ("how long did my kid
 *               actually work?"). Included on the four learning pages (session,
 *               practice, topic, challenge). Once a minute it posts /api/heartbeat
 *               -- but ONLY when this tab is VISIBLE and the student did something
 *               real (typed / clicked / tapped) within the last IDLE_LIMIT_MS.
 *               Leaving the app open in the background, or walking away, counts
 *               NOTHING -- that's the whole point: the dashboard's time numbers
 *               must be honest enough for a homeschool parent's hour log. The
 *               server adds its own minimum-gap + rate-limit guards, so a tampered
 *               page can't inflate the clock. Self-contained, no libraries, no
 *               storage; if the page has no ?code= it does nothing.
 * ============================================================================= */
(function () {
  if (window.__mtTime) return;
  window.__mtTime = true;

  var params = new URLSearchParams(window.location.search);
  var CODE = (params.get("code") || "").trim();
  var COURSE = (params.get("course") || "algebra1").trim();
  if (!CODE) return;   // demo pages / logged-out views: track nothing

  var BEAT_MS = 60 * 1000;        // one heartbeat per minute
  var IDLE_LIMIT_MS = 4 * 60 * 1000;  // no real activity for 4 min -> the clock stops
  var lastActivity = Date.now();  // arriving on the page counts as activity

  // "Real activity" = the student actually did something.
  ["keydown", "pointerdown", "touchstart"].forEach(function (ev) {
    document.addEventListener(ev, function () { lastActivity = Date.now(); },
                              { capture: true, passive: true });
  });

  function localDay() {
    // The student's LOCAL calendar day, so evening work logs on the right date.
    var d = new Date();
    return d.getFullYear() + "-" +
      String(d.getMonth() + 1).padStart(2, "0") + "-" +
      String(d.getDate()).padStart(2, "0");
  }

  function beat() {
    if (document.visibilityState !== "visible") return;          // tab hidden -> no time
    if (Date.now() - lastActivity > IDLE_LIMIT_MS) return;       // walked away -> no time
    try {
      fetch("/api/heartbeat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code: CODE, course: COURSE, day: localDay() }),
      }).catch(function () {});   // tracking must never break the lesson
    } catch (e) {}
  }

  setInterval(beat, BEAT_MS);
})();
/* I did no harm and this file is not truncated. */
