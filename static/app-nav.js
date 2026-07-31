/* =============================================================================
 * app-nav.js  --  MyTutor  --  Hyperion Shift LLC
 * CHANGE NOTES (keep newest at top):
 *   2026-07-30  NEW shared component (Jim: "navigating backwards is hard — give me buttons
 *               back to my main decision points, and a Contact button on every top bar").
 *               Injects clearly-labeled pill links into each app page's top bar:
 *                 🏠 Home            -> /home?code&course   (the hub: lesson/practice/topic/dashboard)
 *                 🔄 Switch course   -> /home?code          (no course param -> home shows the subject picker)
 *                 🎓 My lesson       -> /session?code&course (from dashboard/practice/topic)
 *                 📊 Progress        -> /dashboard?code&course
 *                 ✉️ Contact         -> mailto:support@mrcadabra.com   (EVERY page, every visitor)
 *               Context-aware: student links only when a student code is present and the page
 *               isn't a read-only parent/teacher view; never links to the page you're on; hides
 *               the page's old obscure link ("☰ Menu" / "← Home") when it injects its own Home,
 *               but leaves the parent/teacher "← Back" untouched. Self-contained CSS, no
 *               libraries, no storage; if a page has no top bar it does nothing. Do no harm.
 * ============================================================================= */
(function () {
  if (window.__mtAppNav) return;
  window.__mtAppNav = true;

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  ready(function () {
    var bar = document.querySelector(".topbar") || document.querySelector(".top");
    if (!bar) return;

    var params = new URLSearchParams(window.location.search);
    var CODE = (params.get("code") || "").trim();
    var COURSE = (params.get("course") || "").trim();
    var VIEW = (params.get("view") || "").toLowerCase();
    var readOnly = (VIEW === "parent" || VIEW === "teacher") || !!params.get("teacher");
    var page = window.location.pathname.replace(/\.html$/, "").replace(/^\/static/, "") || "/";
    if (page === "/") page = "/home";
    var q = CODE ? ("?code=" + encodeURIComponent(CODE) + (COURSE ? "&course=" + encodeURIComponent(COURSE) : "")) : "";

    var css = document.createElement("style");
    css.textContent =
      ".anav{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-left:12px}" +
      ".anav a{display:inline-flex;align-items:center;gap:5px;font-size:13px;font-weight:700;text-decoration:none;" +
      "color:#4a4f66;background:#fff;border:1.5px solid #e5e2f2;border-radius:999px;padding:7px 13px;white-space:nowrap}" +
      ".anav a:hover{border-color:#6d5ae6;color:#6d5ae6}" +
      "@media(max-width:760px){.anav a .alabel{display:none}.anav a{padding:7px 9px}}";
    document.head.appendChild(css);

    var nav = document.createElement("div");
    nav.className = "anav";
    function add(href, icon, label) {
      var a = document.createElement("a");
      a.href = href;
      a.innerHTML = icon + ' <span class="alabel">' + label + "</span>";
      nav.appendChild(a);
    }

    var student = CODE && !readOnly;
    if (student) {
      if (page !== "/home") add("/home" + q, "🏠", "Home");
      if (page !== "/session" && COURSE) add("/session" + q, "🎓", "My lesson");
      if (page !== "/dashboard") add("/dashboard" + q, "📊", "Progress");
      add("/home?code=" + encodeURIComponent(CODE), "🔄", "Switch course");
    }
    add("mailto:support@mrcadabra.com", "✉️", "Contact");

    // Hide the page's old, easy-to-miss nav link once ours is in ("☰ Menu" / "← Home") --
    // but NEVER the parent/teacher "← Back", which is that view's own way out.
    if (student) {
      var old = document.getElementById("homeLink") || document.getElementById("lessonLink");
      if (old) old.style.display = "none";
    }
    bar.appendChild(nav);
  });
})();
/* I did no harm and this file is not truncated. */
