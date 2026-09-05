/* =============================================================================
   client-log.js -- the browser stops being a black box -- Hyperion Shift LLC
   -----------------------------------------------------------------------------
   CHANGE NOTES (keep newest at top):
     2026-09-04  BUILD so -- window.MyTutorReport(kind, message): a NAMED client
                 event through the same beacon, so voice.js can file a
                 voice_fallback the night watch can count. Own cap (10/page), own
                 dedupe; the server whitelists kinds. Errors are untouched.
     2026-08-17  NEW FILE (build ha -- EYES, Phase 1 of the full-app review). The
                 review found ~70 empty catch blocks across the pages and ZERO
                 client->server error reporting -- so two JavaScript defects
                 (undeclared variables that killed every spoken answer on /topic and
                 /practice) fired on every single use and were invisible until a
                 human read the source. This file is the blanket fix: window.onerror
                 and unhandledrejection beacon a tiny, capped report to
                 /api/client-error, where it lands in the system_events table and on
                 the /admin telemetry card. Design rules, in order of importance:
                   1. NEVER interfere with the page. Everything is wrapped; this
                      file has no dependencies and throws nothing.
                   2. NEVER flood. At most MAX_REPORTS per page load, duplicates
                      (same message+line) sent once, server rate-limits per IP too.
                   3. NEVER leak content. Error message, source file, line, and a
                      short stack only -- no conversation text, no student input.
   ============================================================================= */
(function () {
  "use strict";
  var MAX_REPORTS = 5;                    // per page load -- a loop can't flood
  var sent = 0;
  var seen = {};                          // message+line -> true (dedupe repeats)

  function beacon(payload) {
    try {
      var body = JSON.stringify(payload);
      // sendBeacon survives page unload and never blocks; fetch is the fallback.
      if (navigator.sendBeacon) {
        navigator.sendBeacon("/api/client-error",
                             new Blob([body], { type: "application/json" }));
      } else if (window.fetch) {
        fetch("/api/client-error", { method: "POST", body: body, keepalive: true,
                                     headers: { "Content-Type": "application/json" } })
          .catch(function () {});
      }
    } catch (e) { /* an error reporter must never error the page */ }
  }

  function report(message, source, line, stack) {
    try {
      if (sent >= MAX_REPORTS) return;
      var key = String(message).slice(0, 120) + "@" + String(line || "");
      if (seen[key]) return;
      seen[key] = true;
      sent++;
      beacon({
        page: (location.pathname || "").slice(0, 80),
        message: String(message || "").slice(0, 300),
        stack: String(stack || "").slice(0, 400),
        url: (String(source || "") + (line ? (":" + line) : "")).slice(0, 120)
      });
    } catch (e) { /* never throw */ }
  }

  // (so, 2026-09-04) A NAMED EVENT, NOT AN ERROR. voice.js falls back to the browser
  // voice when a clip will not start -- and until now said so on the console only, so
  // the night watch could not count how often a student heard the mechanical voice
  // instead of Mr. Cadabra. Same beacon, same route, one extra field (kind); the
  // server whitelists the kinds it will file. Its own cap and its own dedupe, so a
  // bad voice night can never crowd out a real error report.
  var MAX_EVENTS = 10, sentEvents = 0, seenEvents = {};
  window.MyTutorReport = function (kind, message) {
    try {
      if (sentEvents >= MAX_EVENTS) return;
      var key = String(kind) + "|" + String(message).slice(0, 120);
      if (seenEvents[key]) return;
      seenEvents[key] = true;
      sentEvents++;
      beacon({ kind: String(kind || "").slice(0, 24),
               page: (location.pathname || "").slice(0, 80),
               message: String(message || "").slice(0, 300) });
    } catch (e) { /* never throw */ }
  };

  window.addEventListener("error", function (ev) {
    try {
      report(ev.message || (ev.error && ev.error.message) || "script error",
             ev.filename, ev.lineno,
             ev.error && ev.error.stack ? ev.error.stack : "");
    } catch (e) { /* never throw */ }
  });

  window.addEventListener("unhandledrejection", function (ev) {
    try {
      var r = ev.reason || {};
      report("unhandledrejection: " + (r.message || String(r)).slice(0, 200),
             "", "", r.stack || "");
    } catch (e) { /* never throw */ }
  });
})();
/* I did no harm and this file is not truncated. */
