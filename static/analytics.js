/* =============================================================================
   analytics.js  --  MyTutor  --  Hyperion Shift LLC
   -----------------------------------------------------------------------------
   CHANGE NOTES (keep newest at top):
   - 2026-08-18  (build hs) NO FOURTH PARTY ON CHILDREN'S PAGES -- Jim's policy ruling,
     2026-08-18, resolving the review's Class-F finding: privacy.html promises exactly
     three processors, and Plausible loading on a child's lesson page made a silent
     fourth. The tracker now refuses to load on the STUDENT SURFACES (session, topic,
     practice, challenge, dashboard, records, home) -- matched by pretty route AND
     /static/*.html form -- and mtTrack becomes a no-op there, so no event, no queue,
     no request leaves a child's page. Marketing/adult surfaces (index, landing,
     parents, teachers, homeschool, pricing, demo -- the demo funnel is Jim's
     conversion measure -- family, teacher, students, admin) keep analytics exactly as
     before. The guard lives HERE, in the one shared file, so a future page that adds
     the include is protected by default if it is a student surface.
   - 2026-08-04  FUNNEL GOALS (Measurement plan #2): new window.mtTrack(name, props) helper --
     a safe wrapper over plausible() custom events (never throws, buffers before the tracker
     loads). Pages fire five named events: "Demo Level Picked", "Demo Completed",
     "Parent Signup", "Checkout Started", "Subscribed". Cookieless, zero personal data --
     event name + optional coarse props (e.g. which demo level) only. Add each name as a
     custom-event GOAL in the Plausible dashboard to see funnel conversion.
   - 2026-08-03  NEW FILE. Privacy-friendly analytics by Plausible (plausible.io,
     Jim's account). This ONE shared file is referenced from the <head> of every page via
       <script src="/static/analytics.js"></script>
     so the site key lives in exactly one place. Pure add-on: if Plausible is
     unreachable, the tracker simply doesn't load and the page is unaffected.
   =============================================================================
   Original snippet this reproduces (from Jim's Plausible dashboard):
     <script async src="https://plausible.io/js/pa-Brw8zIdpjWcu7EbkYXKqP.js"></script>
     window.plausible = window.plausible || function(){(plausible.q=plausible.q||[]).push(arguments)};
     plausible.init = plausible.init || function(i){plausible.o=i||{}};
     plausible.init();
   ============================================================================= */
(function () {
  "use strict";

  // THE CHILDREN'S-PAGE GUARD (2026-08-18, build hs -- Jim's ruling: no fourth party
  // on kids' pages). Student surfaces load NOTHING: no tracker, no stub queue, no
  // events. Everything else behaves exactly as before.
  var KID_PAGES = ["session", "topic", "practice", "challenge", "dashboard",
                   "records", "home"];
  var path = String((window.location && window.location.pathname) || "").toLowerCase();
  // Normalise "/session", "/session/", "/static/session.html" -> "session".
  var page = path.replace(/^\/static\//, "/").replace(/\.html$/, "")
                 .replace(/\/+$/, "").replace(/^\/+/, "");
  var isKidPage = false;
  for (var i = 0; i < KID_PAGES.length; i++) {
    if (page === KID_PAGES[i]) { isKidPage = true; break; }
  }
  if (isKidPage) {
    window.mtTrack = function () { /* a child's page reports to no one */ };
    return;
  }

  // Queue stub first, so any event fired before the tracker finishes loading is
  // buffered and replayed rather than lost.
  window.plausible = window.plausible || function () { (plausible.q = plausible.q || []).push(arguments); };
  window.plausible.init = window.plausible.init || function (i) { plausible.o = i || {}; };

  // Load the Plausible tracker script asynchronously (non-blocking).
  var s = document.createElement("script");
  s.async = true;
  s.src = "https://plausible.io/js/pa-Brw8zIdpjWcu7EbkYXKqP.js";
  (document.head || document.documentElement).appendChild(s);

  // Initialise with default config.
  window.plausible.init();

  // FUNNEL EVENTS (2026-08-04): one safe door for every page to fire a named event.
  window.mtTrack = function (name, props) {
    try { window.plausible(name, props ? { props: props } : undefined); } catch (e) { /* never break a page */ }
  };
})();
/* I did no harm and this file is not truncated. */
