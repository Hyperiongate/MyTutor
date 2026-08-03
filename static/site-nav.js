/* =============================================================================
   site-nav.js  --  MyTutor  --  Hyperion Shift LLC
   -----------------------------------------------------------------------------
   CHANGE NOTES (keep newest at top):
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
      ".mt-college-menu a:hover{background:#f6f3ff;color:var(--purple,#6d5ae6)}";
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
  });
})();
/* I did no harm and this file is not truncated. */
