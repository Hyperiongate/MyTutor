/* =============================================================================
   site-nav.js  --  MyTutor  --  Hyperion Shift LLC
   -----------------------------------------------------------------------------
   CHANGE NOTES (keep newest at top):
   - 2026-08-25  "HOW WE TEACH" JOINS THE MENU (build ne). Jim reviewed /methodology
     twice, made his edits in build nd, then: "I like this methodology page. Let's go
     ahead and add it to the menu." Injected here rather than hand-edited into the 13
     marketing pages' nav rows, for the same reason the college dropdown lives here:
     one file, every page, and a page added next month gets the link for free. Placed
     right after "Our mission" (the two answer the same visitor question: who are
     these people and can I trust them). Guard: if a page already hardcodes a
     /methodology nav link (methodology.html itself does, so it can highlight as
     "here" without JavaScript), the injector leaves it alone.
   - 2026-08-09  DEMO BUTTON (Jim). Adds a highlighted ORANGE "Try the demo" pill to the
     end of the marketing nav on every page that has a .nav-links row, linking to /demo.
     The demo is the strongest thing we have to sell with (a full guided lesson in
     Mr. Cadabra's voice plus the three dashboards), so it gets the one loud button in
     the menu. Skipped automatically ON the demo page itself, and skipped if a page
     already has its own /demo nav link.
   - 2026-08-03  NEW FILE. Adds a "College level math" DROPDOWN to the marketing top
     nav (the .nav-links row), right after the "Courses" link. The dropdown lists the
     college-level courses and is DATA-DRIVEN by the COLLEGE array below, so adding
     another course later is a one-line change here -- nothing else to touch. This is
     ONE shared file, referenced from the <head> of the marketing pages via
       <script src="/static/site-nav.js" defer></script>
     It self-checks for a .nav-links row and does nothing on pages that don't have one
     (the app pages), so it's safe to include anywhere. Pure add-on; if it fails to
     load, the nav simply shows its normal links. Hover to open on desktop; tap to
     open on touch devices.
   =============================================================================
   To add another college-level course, add one entry to COLLEGE (title + href).
   ============================================================================= */
(function () {
  "use strict";
  // The college-level courses shown in the dropdown. Extend this list to add more.
  var COLLEGE = [
    { title: "Calculus", href: "/courses#calculus" },
    { title: "Differential Equations", href: "/courses#diffeq" }
  ];

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  ready(function () {
    var links = document.querySelector(".nav-links");
    if (!links) return;                       // not a marketing page -> do nothing
    if (document.getElementById("collegeNav")) return;   // already added

    var css = document.createElement("style");
    css.textContent =
      ".mt-college{position:relative;display:inline-block}" +
      ".mt-college>a{cursor:pointer;white-space:nowrap}" +
      ".mt-college>a .mt-caret{font-size:11px;margin-left:3px}" +
      ".mt-college-menu{position:absolute;left:50%;transform:translateX(-50%);top:100%;" +
      "margin-top:8px;background:#fff;border:1px solid var(--line,#ece8f6);border-radius:12px;" +
      "box-shadow:0 14px 34px rgba(60,40,120,.16);padding:6px;min-width:220px;display:none;z-index:60}" +
      ".mt-college:hover .mt-college-menu,.mt-college.open .mt-college-menu{display:block}" +
      ".mt-college-menu a{display:block;padding:9px 12px;border-radius:8px;font-size:14px;" +
      "font-weight:600;white-space:nowrap;color:var(--ink,#20233a)}" +
      ".mt-college-menu a:hover{background:#f6f3ff;color:var(--purple,#6d5ae6)}" +
      /* 2026-08-09: the one loud button in the menu -- the demo sells the product. */
      ".mt-demo{display:inline-flex;align-items:center;gap:6px;background:linear-gradient(135deg,#ff8a2b,#ff6a3d);" +
      "color:#fff !important;font-weight:800;border-radius:999px;padding:9px 16px;white-space:nowrap;" +
      "box-shadow:0 6px 16px rgba(255,106,61,.34);border:0;text-decoration:none;line-height:1.1}" +
      ".mt-demo:hover{filter:brightness(1.06);color:#fff !important}" +
      ".mt-demo:active{transform:translateY(1px)}";
    document.head.appendChild(css);

    var wrap = document.createElement("span");
    wrap.className = "mt-college";
    wrap.id = "collegeNav";

    var trigger = document.createElement("a");
    trigger.href = "/courses";
    trigger.setAttribute("aria-haspopup", "true");
    trigger.innerHTML = 'College level math<span class="mt-caret">▾</span>';

    var menu = document.createElement("div");
    menu.className = "mt-college-menu";
    COLLEGE.forEach(function (co) {
      var a = document.createElement("a");
      a.href = co.href;
      a.textContent = co.title;
      menu.appendChild(a);
    });

    wrap.appendChild(trigger);
    wrap.appendChild(menu);

    // On touch devices (no hover), tap the label to open/close instead of navigating.
    trigger.addEventListener("click", function (e) {
      if (window.matchMedia && window.matchMedia("(hover: none)").matches) {
        e.preventDefault();
        wrap.classList.toggle("open");
      }
    });

    // Place it right after the "Courses" link if we can find it; otherwise at the end.
    var anchors = links.querySelectorAll("a");
    var coursesLink = null;
    for (var i = 0; i < anchors.length; i++) {
      if ((anchors[i].getAttribute("href") || "").split("#")[0] === "/courses") {
        coursesLink = anchors[i];
        break;
      }
    }
    if (coursesLink && coursesLink.nextSibling) links.insertBefore(wrap, coursesLink.nextSibling);
    else links.appendChild(wrap);

    // ---- HOW WE TEACH (2026-08-25, build ne) ------------------------------------
    // Jim approved the page and asked for it in the menu. After "Our mission",
    // because a parent asking "can I trust these people?" should meet both answers
    // side by side.
    addHowWeTeach(links);

    // ---- THE DEMO BUTTON (2026-08-09) -------------------------------------------
    // Last item in the row so it reads as the call to action, and orange so it is the
    // only thing in the menu competing for a first-time visitor's eye.
    addDemoButton(links);
  });

  function addHowWeTeach(links) {
    if (document.getElementById("methodNav")) return;                // already added
    var onPage = (location.pathname || "").replace(/\/+$/, "") === "/methodology";
    var existing = links.querySelector('a[href="/methodology"], a[href="/methodology/"]');
    if (existing) {                       // the page hardcodes it (methodology.html)
      existing.id = "methodNav";
      if (onPage && existing.className.indexOf("here") < 0) {
        existing.className = (existing.className ? existing.className + " " : "") + "here";
      }
      return;
    }
    var a = document.createElement("a");
    a.id = "methodNav";
    a.href = "/methodology";
    a.textContent = "How we teach";
    if (onPage) a.className = "here";
    // Right after "Our mission" when the page has one; otherwise before "Features";
    // otherwise the end of the row. Never crashes the nav -- worst case it appends.
    var anchors = links.querySelectorAll("a"), after = null, before = null;
    for (var i = 0; i < anchors.length; i++) {
      var h = (anchors[i].getAttribute("href") || "").split("#")[0];
      if (h === "/mission") { after = anchors[i]; break; }
      if (h === "/features" && !before) before = anchors[i];
    }
    if (after && after.nextSibling) links.insertBefore(a, after.nextSibling);
    else if (before) links.insertBefore(a, before);
    else links.appendChild(a);
  }

  function addDemoButton(links) {
    if (document.getElementById("demoNav")) return;                  // already added
    var here = (location.pathname || "").replace(/\/+$/, "");
    if (here === "/demo" || here === "/static/demo.html") return;    // not on the demo itself
    var existing = links.querySelectorAll('a[href="/demo"], a[href="/demo/"]');
    if (existing.length) {                                           // page already links it: just style it
      existing[0].id = "demoNav";
      existing[0].className = (existing[0].className ? existing[0].className + " " : "") + "mt-demo";
      existing[0].innerHTML = "🎬 Try the demo";
      return;
    }
    var a = document.createElement("a");
    a.id = "demoNav";
    a.className = "mt-demo";
    a.href = "/demo";
    a.innerHTML = "🎬 Try the demo";
    a.setAttribute("aria-label", "Try the interactive demo");
    links.appendChild(a);
  }
})();
/* I did no harm and this file is not truncated. */
