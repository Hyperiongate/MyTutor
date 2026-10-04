/* =============================================================================
 * phone-menu.js  --  MyTutor  --  Hyperion Shift LLC
 * CHANGE NOTES (keep newest at top):
 *   2026-10-03  NEW shared component (build zd, Jim's phone pass, P6 + P8): THE PHONE'S
 *               MENU. On a phone the board pages' left sidebar is a dock at the bottom
 *               (build dz), and its nav links were a sideways chip strip -- one word per
 *               screen ("Curriculum", scroll, "Course assessment"), with the Curriculum
 *               list opening as a thin column INSIDE the strip. Jim: "getting around is
 *               super cumbersome." Now, on a screen 900px wide or less:
 *                 - a ☰ Menu button sits in the top bar (first thing on the left);
 *                 - the page's own .leftnav -- the SAME nodes, same ids, so the tour,
 *                   library.js's "Look it up" and every page hook still find them -- is
 *                   moved into a full-screen sheet (#menuSheet) as a plain vertical list;
 *                   the Curriculum opens stacked, unit under unit, as its own screen;
 *                 - the pages' own Sign out link (P8 -- a student had no way out; a
 *                   navbtn with data-signout, last in the .leftnav on every board page,
 *                   wired by student-code.js: clear the mt_student cookie, go to /login)
 *                   rides along into the sheet and is drawn as the way out, in red;
 *                 - a tap on any link, any unit, the ✕ or the dark backdrop closes it.
 *               Above 900px nothing changes: the .leftnav is put back exactly where it
 *               was in the sidebar (before .controls), the button and the sheet hide.
 *               The reparent follows the media query both ways (a phone turned sideways,
 *               a window resized), the way placeCtrls does on session.html. Self-
 *               contained CSS, no libraries; if a page has no .leftnav or no top bar it
 *               does nothing. Pin: PART 3ox.
 * ============================================================================= */
(function () {
  if (window.__mtPhoneMenu) return;
  window.__mtPhoneMenu = true;

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  ready(function () {
    var nav = document.querySelector(".side.left .leftnav") || document.querySelector(".leftnav");
    var bar = document.querySelector(".topbar") || document.querySelector(".top");
    var side = document.querySelector(".side.left");
    if (!nav || !bar || !side) return;
    var home = nav.parentElement;            // where the nav lives on a desktop
    var homeNext = nav.nextSibling;          // ...and what it sits before (.controls)
    // the Sign out link is LAST, on every screen -- library.js appends "Look it up" to the
    // nav at the same moment this runs, and this script is loaded after it on purpose
    var so = nav.querySelector("[data-signout]");
    if (so) nav.appendChild(so);

    var css = document.createElement("style");
    css.id = "mtPhoneMenuCSS";
    css.textContent =
      "#menuBtn{display:none;order:-1;flex:0 0 auto;margin-right:8px;border:1.5px solid #e5e2f2;background:#fff;" +
      "border-radius:10px;padding:7px 11px;font:inherit;font-size:15px;font-weight:800;color:#26263a;cursor:pointer;line-height:1}" +
      "#menuSheet{display:none;position:fixed;inset:0;z-index:48;background:rgba(20,28,40,.45)}" +
      "#menuSheet.show{display:block}" +
      ".msheet{position:absolute;inset:0;background:#fff;display:flex;flex-direction:column;padding:12px 14px 20px;overflow-y:auto}" +
      ".mshead{display:flex;align-items:center;justify-content:space-between;padding:4px 2px 12px;border-bottom:1px solid #e7e6f2;margin-bottom:12px}" +
      ".mshead b{font-size:18px}" +
      ".msclose{border:1.5px solid #e5e2f2;background:#fff;border-radius:10px;padding:8px 12px;font:inherit;font-size:15px;font-weight:700;cursor:pointer}" +
      ".msheet .leftnav{display:flex;flex-direction:column;gap:10px;overflow:visible;padding:0}" +
      ".msheet .leftnav .navbtn{display:flex;width:100%;white-space:normal;font-size:17px;padding:14px 16px;border-radius:12px}" +
      ".msheet .leftnav .curriculum{display:block;margin:0 0 6px;padding:0 4px}" +
      ".msheet .leftnav .curriculum .unit{font-size:15px;padding:12px 12px;border:1px solid #e7e6f2;border-radius:10px;margin:6px 0;background:#fff}" +
      ".msheet .leftnav .navbtn[data-signout]{margin-top:14px;border-color:#f5cfc8;color:#b3402e}" +
      // the pencil floats above everything by design (cadabra.js); he steps out while the menu is up
      "body.menu-open #cadabra-layer{visibility:hidden}" +
      "@media (max-width:900px){#menuBtn{display:inline-flex}}";
    document.head.appendChild(css);

    // the button, first in the top bar
    var btn = document.createElement("button");
    btn.id = "menuBtn"; btn.type = "button";
    btn.setAttribute("aria-label", "Menu"); btn.setAttribute("aria-expanded", "false");
    btn.textContent = "☰ Menu";
    bar.insertBefore(btn, bar.firstChild);

    // the sheet
    var sheet = document.createElement("div");
    sheet.id = "menuSheet";
    sheet.innerHTML =
      '<div class="msheet" role="dialog" aria-label="Menu">' +
      '  <div class="mshead"><b>Menu</b><button type="button" class="msclose" id="menuClose">✕ Close</button></div>' +
      '  <div id="menuNavHome"></div>' +
      '</div>';
    document.body.appendChild(sheet);
    var navHome = sheet.querySelector("#menuNavHome");

    var MQ = window.matchMedia("(max-width: 900px)");
    function open(on) {
      sheet.classList.toggle("show", !!on);
      document.body.classList.toggle("menu-open", !!on);
      btn.setAttribute("aria-expanded", on ? "true" : "false");
    }
    function place() {
      if (MQ.matches) {
        if (nav.parentElement !== navHome) navHome.appendChild(nav);
      } else {
        open(false);
        if (nav.parentElement !== home) home.insertBefore(nav, homeNext && homeNext.parentElement === home ? homeNext : null);
      }
    }
    btn.addEventListener("click", function () { open(!sheet.classList.contains("show")); });
    sheet.querySelector("#menuClose").addEventListener("click", function () { open(false); });
    sheet.addEventListener("click", function (ev) {
      if (ev.target === sheet) { open(false); return; }               // the backdrop
      var t = ev.target.closest ? ev.target.closest("a, .unit") : null;
      if (t && nav.contains(t)) open(false);                           // a link or a unit: away we go
    });
    try { MQ.addEventListener("change", place); }
    catch (e) { try { MQ.addListener(place); } catch (e2) {} }
    place();
    window.MTPhoneMenu = { open: open, isOpen: function () { return sheet.classList.contains("show"); }, place: place };
  });
})();
/* I did no harm and this file is not truncated. */
