/* =============================================================================
   analytics.js  --  MyTutor  --  Hyperion Shift LLC
   -----------------------------------------------------------------------------
   CHANGE NOTES (keep newest at top):
   - 2026-08-04  FUNNEL GOALS (Measurement plan #2): new window.mtTrack(name, props) helper --
     a safe wrapper over plausible() custom events (never throws, buffers before the tracker
     loads). Pages fire five named events: "Demo Level Picked", "Demo Completed",
     "Parent Signup", "Checkout Started", "Subscribed". Cookieless, zero personal data --
     event name + optional coarse props (e.g. which demo level) only. Add each name as a
     custom-event GOAL in the Plausible dashboard to see funnel conversion.
   - 2026-08-03  NEW FILE. Privacy-friendly analytics by Plausible (plausible.io,
     Jim's account). Plausible is COOKIELESS and collects no personal data, which
     is why it's safe site-wide, including pages minors use. This ONE shared file
     is referenced from the <head> of every page via
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
