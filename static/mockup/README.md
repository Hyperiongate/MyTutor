# mockup/

Concept pages for review. **Nothing here is production.**

Last updated 1 September 2026 (build rq: the playground is superseded by `/static/cadabra-lab.html`; the pencil itself is no longer a mockup — it ships in cadabra.js on every lesson page and the demo).

| File | What it is |
|---|---|
| `cadabra-pencil.html` | **Mr. Cadabra, Sharpened** — Mr. Cadabra redrawn as a No.2 yellow pencil. Full character, size tests in the face orb, five expressions, a talking mouth (press "Say a line"), and the trade-offs behind each decision. |
| `cadabra-playground.html` | **The Cadabra Motion Lab** *(added 31 Aug 2026; superseded 1 Sep by the permanent bench, `/static/cadabra-lab.html`, which drives the REAL shipped layer — this file keeps its own older copy of the pencil and is kept only as the design record)* — the same character, but free of the box: he floats over a stand-in entry-level math lesson and the dark console on the right fires every behaviour live. Point, underline, three celebration tiers, a page tour, an opening joke, three hand styles, and sliders for size, bob, drift and flight speed. |
| `landing-cadabra.html` | **The Front Door, Hosted** *(added 1 Sep 2026)* — the simpler home page, with the pencil as the hero picture, and a product demonstration **he gives himself**: press "Let him show you around" and he flies into a stand-in classroom, points at the board, the streak bubbles and the sidebar tab (which he closes, to show what it does), writes the answer line, and hands over. No video, no narrator, no per-view cost. Supersedes `landing-quiet.html`. |
| `landing-quiet.html` | **The Quiet Front Door** *(superseded 1 Sep)* — a calmer home page. Three doors above the fold, everything we sell with below it. Press **Show design notes** in the top bar for the reasoning inline. |

## For marketing

Open any file in a browser — double-click works, no server needed. Once pushed they
are also live at:

- `/static/mockup/cadabra-pencil.html`
- `/static/mockup/cadabra-playground.html`
- `/static/mockup/landing-cadabra.html`
- `/static/mockup/landing-quiet.html`

All three are `noindex`, so they cannot show up in search or compete with the real pages.

## Three decisions already made in these files

- **He is No.2 yellow.** `#F2BC1B`. The company stays purple — site, logo, buttons — and
  the purple rides on his hat band so the two read as related. **Yellow is the character's
  and nothing else's:** no button, badge or highlight on the site should use it.
- **He has no legs.** He balances on his own sharpened point over a soft shadow. Writing
  is a lean, not a walk.
- **He moves when the child is not working.** The playground enforces this in code: he
  parks and goes still the moment the answer box takes focus. Movement is a reward or a
  transition, never company for a child mid-problem.

## The human avatar comes out

Jim's ruling, 1 September 2026: **if the pencil is Mr. Cadabra, a photoreal man in the
orb is a different character** — and children notice that before adults do. Nothing in
`landing-cadabra.html` mounts the presence layer or plays a moments clip.

What that means for the real pages, none of it done yet:

- `static/videos/cadabra/presence.json` exists today, so silent loops of a real man play
  inside the round orb on **six pages** — session, topic, practice, challenge, landing and
  demo. Only `drill.html` opts out, using the `presence:false` flag `tutor-face.js` has
  supported since build mi.
- `moments.json` adds two **talking** clips: `site_welcome` on the landing page and
  `demo_welcome` on the demo.
- Closing the path is three reversible moves: pass `presence:false` at the five remaining
  `TutorFace.draw` call sites; stop calling `TutorMoments.play` for those two clips; and
  leave both manifests and every `.mp4` exactly where they are. Nothing is deleted and
  each step is a one-line revert.

## Still open

- The colour values are concept values. They must be matched against the real palette in
  `static/tutor-face.js` before any production work, and the pixel-regression checks that
  currently assert Mr. Cadabra is purple will need repointing.
- Hand style is undecided. The playground ships three — thin mitts as first drawn,
  gloves, and detached gloves with no arms — so the call can be made by looking.
- The playground's mouth runs on a synthetic loudness envelope. In production it reads the
  real amplitude of the playing ElevenLabs clip from a Web Audio `AnalyserNode` on the
  existing `<audio>` element — no new audio, no per-word work.
- The jokes are eight stand-ins. Production needs 50+ with no repeat inside a session.

## Safety

Self-contained, linked from nowhere, imported by nothing. No API calls. The only external
request is Google Fonts, which falls back cleanly if blocked. Adding or deleting this
folder cannot affect the live app.

I did no harm and this file is not truncated.
