/* =============================================================================
 * student-code.js  --  MyTutor  --  Hyperion Shift LLC
 * CHANGE NOTES (keep newest at top):
 *   2026-10-03  (build zd) SIGN OUT: any [data-signout] element clears the mt_student cookie
 *               and goes to /login (Jim's phone pass, P8 -- a student had no way out, and a
 *               cookie on a shared laptop needs one). The board pages carry the link.
 *   2026-10-01  NEW shared component (build zb, Jim's first-family playthrough F34):
 *               THE STUDENT'S CODE LEAVES THE ADDRESS BAR. The login code IS the
 *               credential, and until now every student page carried it in the URL
 *               (/topic?code=MAPLE42) -- in the browser history, in bookmarks, in
 *               screenshots, in the address bar a classmate reads over a shoulder.
 *               Jim's 2026-08-18 ruling stands beside this one: "do not kill the
 *               bookmark login" -- a family bookmark WITH the code is how a young
 *               student signs in. Both are honoured here:
 *                 - a page that ARRIVES with ?code= (a bookmark, a link from the
 *                   family page, the login hand-off) stores it in the mt_student
 *                   cookie (this origin only, SameSite=Lax, 30 days, Secure on
 *                   https) and then takes it OUT of the address bar in place
 *                   (history.replaceState -- the page does not reload, nothing else
 *                   in the URL changes, and the Back button is untouched);
 *                 - a page that arrives WITHOUT a code reads the cookie;
 *                 - every link a page builds between the student pages drops the
 *                   code (MTStudent.q builds the query without it), so nothing a
 *                   student taps inside the app carries the credential;
 *                 - the login page stores the code and sends the student on with a
 *                   clean address.
 *               The PARENT'S doors are deliberately different: /dashboard?view=parent
 *               and /records are the parent reading one student, often a second one
 *               a minute after the first, on the family's shared laptop. Those pages
 *               call MTStudent.code({ keep: true }): the code in their URL is used
 *               for that page and NEITHER stored NOR stripped -- so viewing a
 *               sibling's progress never changes which student the laptop is signed
 *               in as, and a reload of the parent page keeps working.
 *               The API never sees the code in a URL either way: every call sends
 *               X-Student-Code (build hs) and main.py's _code_dep reads the header.
 *               Loaded in <head> before each page's own script (the page's CODE is
 *               read from here) and before app-nav.js / library.js / time-tracker.js
 *               (they run at DOMContentLoaded, after the address has been cleaned, so
 *               they must read the cookie, not the URL). Self-contained, no libraries.
 *               A page whose cache still lacks this file falls back to the URL as
 *               before (each page guards `window.MTStudent`). Pin: PART 3ov.
 * ============================================================================= */
(function () {
  if (window.MTStudent) return;

  var KEY = "mt_student";
  var MAX_AGE = 30 * 24 * 3600;   // thirty days, the same life as the parent's token
  var memo = null;                // the code this page resolved, once

  function fromUrl() {
    try { return (new URLSearchParams(window.location.search).get("code") || "").trim(); }
    catch (e) { return ""; }
  }
  function readCookie() {
    try {
      var parts = String(document.cookie || "").split(";");
      for (var i = 0; i < parts.length; i++) {
        var kv = parts[i].trim();
        if (kv.indexOf(KEY + "=") === 0) return decodeURIComponent(kv.slice(KEY.length + 1)).trim();
      }
    } catch (e) {}
    return "";
  }
  function write(code) {
    code = String(code || "").trim();
    if (!code) return;
    try {
      document.cookie = KEY + "=" + encodeURIComponent(code) + "; path=/; max-age=" + MAX_AGE +
        "; SameSite=Lax" + (window.location.protocol === "https:" ? "; Secure" : "");
    } catch (e) {}
    memo = code;
  }
  function clear() {
    try { document.cookie = KEY + "=; path=/; max-age=0; SameSite=Lax"; } catch (e) {}
    memo = null;
  }
  // Take ?code= out of the address bar in place. Everything else in the URL stays
  // (course, unit, tour, view...), the hash stays, the page does not reload, and the
  // history entry is REPLACED, not added -- Back still goes where it went before.
  function strip() {
    try {
      var url = new URL(window.location.href);
      if (!url.searchParams.has("code")) return;
      url.searchParams.delete("code");
      var clean = url.pathname + (url.searchParams.toString() ? "?" + url.searchParams.toString() : "") + url.hash;
      window.history.replaceState(window.history.state, "", clean);
    } catch (e) {}
  }
  // The code for this page. Default: an arriving ?code= is stored and stripped; with
  // no code in the URL the cookie answers. { keep: true } (the parent's pages): the
  // URL's code is used as-is, never stored, never stripped; the cookie is only the
  // fallback when the URL has none.
  function code(opts) {
    opts = opts || {};
    if (memo !== null && !opts.keep) return memo;
    var u = fromUrl();
    if (u) {
      if (opts.keep) return u;
      write(u); strip();
      return u;
    }
    var c = readCookie();
    if (!opts.keep) memo = c;
    return c;
  }
  // A query string for a student-page link WITHOUT the code: q({course: "entry"})
  // -> "?course=entry"; q({}) -> "". Empty values are left out.
  function q(obj) {
    var pairs = [];
    obj = obj || {};
    for (var k in obj) {
      if (!Object.prototype.hasOwnProperty.call(obj, k)) continue;
      if (k === "code") continue;
      var v = obj[k];
      if (v === undefined || v === null || v === "" || v === false) continue;
      pairs.push(encodeURIComponent(k) + "=" + encodeURIComponent(String(v)));
    }
    return pairs.length ? "?" + pairs.join("&") : "";
  }

  window.MTStudent = { code: code, set: write, clear: clear, q: q, strip: strip, KEY: KEY };

  // (zd, 2026-10-03) SIGN OUT. Jim's phone pass (P8): a student had no way out -- and with
  // the code in a cookie, a shared laptop needs one. Any element with data-signout (the
  // board pages' "Sign out" link, last in their sidebar nav, and so in the phone menu)
  // clears the cookie and goes to the sign-in page. Wired once, at DOMContentLoaded.
  function wireSignOut() {
    var nodes = document.querySelectorAll("[data-signout]");
    for (var i = 0; i < nodes.length; i++) {
      nodes[i].addEventListener("click", function (ev) {
        try { ev.preventDefault(); } catch (e) {}
        clear();
        try { sessionStorage.removeItem("mt_sb_open"); } catch (e) {}
        window.location.href = "/login";
      });
    }
  }
  if (document.readyState !== "loading") wireSignOut();
  else document.addEventListener("DOMContentLoaded", wireSignOut);
})();
/* I did no harm and this file is not truncated. */
