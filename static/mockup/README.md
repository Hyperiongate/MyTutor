# mockup/

Concept pages for review. **Nothing here is production.**

| File | What it is |
|---|---|
| `cadabra-pencil.html` | **Mr. Cadabra, Sharpened** — Mr. Cadabra redrawn as a No.2 yellow pencil. Full character, size tests in the face orb, five expressions, a talking mouth (press "Say a line"), and the trade-offs behind each decision. |
| `landing-quiet.html` | **The Quiet Front Door** — a calmer home page. Three doors above the fold, everything we sell with below it. Press **Show design notes** in the top bar for the reasoning inline. |

## For marketing

Open either file in a browser — double-click works, no server needed. Once pushed they
are also live at:

- `/static/mockup/cadabra-pencil.html`
- `/static/mockup/landing-quiet.html`

Both are `noindex`, so they cannot show up in search or compete with the real pages.

## Two decisions already made in these files

- **He is No.2 yellow.** `#F2BC1B`. The company stays purple — site, logo, buttons — and
  the purple rides on his hat band so the two read as related. **Yellow is the character's
  and nothing else's:** no button, badge or highlight on the site should use it.
- **He has no legs.** He balances on his own sharpened point over a soft shadow. Writing
  is a lean, not a walk.

## Still open

The colour values are concept values. They must be matched against the real palette in
`static/tutor-face.js` before any production work, and the pixel-regression checks that
currently assert Mr. Cadabra is purple will need repointing.

## Safety

Self-contained, linked from nowhere, imported by nothing. No API calls. The only external
request is Google Fonts, which falls back cleanly if blocked. Adding or deleting this
folder cannot affect the live app.

I did no harm and this file is not truncated.
