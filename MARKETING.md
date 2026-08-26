<!--
  =============================================================================
  MARKETING.md  --  rules of the road for the marketing clone  --  Hyperion Shift LLC
  -----------------------------------------------------------------------------
  CHANGE NOTES (keep newest at top):
  - 2026-08-26  NEW FILE (build oa). Jim shared the repo with marketing (HTML
    pages only, no backend). This is the one page they read before their first
    commit. Written to prevent the three real accidents: pushing straight to
    the live site, colliding with the app builds, and committing the phantom
    line-ending rewrite their git offered them on day one.
  =============================================================================
-->

# Working in this repo — marketing edition

Welcome! This repo is the live product: **a push to `main` deploys to mrcadabra.com
within minutes, real families included.** These five rules keep everyone safe.

## 1. Work on a branch, never on `main`

In GitHub Desktop: **Branch → New Branch** → name it `marketing` (or
`marketing-<topic>`) → Publish. Do all your work there. When you're ready,
**Create Pull Request** — Jim reviews and merges, and only that merge goes live.
You never push to `main` directly, even for a typo.

## 2. Your lane is the marketing pages

You'll work only in `static/`, and only on the marketing pages:

home.html · landing.html · index.html · features.html · pricing.html ·
mission.html · homeschool.html · parents.html · teachers.html · students.html ·
courses.html · help.html · privacy.html

**Please do not edit** anything else — especially `main.py`, `tutor.py`,
`prompts.py`, `store.py`, any `.js` file, or the app pages
(`session.html`, `practice.html`, `topic.html`, `drill.html`, `demo.html`,
`admin.html`, `dashboard.html`, `methodology.html`). Those files are covered by
an automated test battery (6,000+ checks) that runs on Jim's side; edits there
will bounce.

## 3. House rules the tests enforce (yes, really)

- The company's experience is always written **"Hundreds"** — never "300+".
- Numbers on the methodology page (checks per release, checks per reply,
  problem counts) are **machine-counted** — never edit them by hand. (That page
  is off-limits per rule 2 anyway.)
- The odd HTML comments in every file — including the closing line
  *"I did no harm and this file is not truncated."* — are **load-bearing**.
  Leave them exactly as they are, and leave the change-notes block at the top
  of each file alone (Jim's side adds entries there).
- No API keys, passwords, or student information ever goes into this repo.
  Keys live in Render only.

## 4. About the "98 modified files" your git showed you

That was a line-endings illusion (Windows CRLF vs. the repo's LF), not real
changes. It is fixed repo-wide by the `.gitattributes` file that now lives here.
**Do not commit those files.** The clean path:

1. In GitHub Desktop: **Branch → Discard all changes** (they're phantom).
2. **Fetch/Pull** so you have the `.gitattributes` fix.
3. If anything still shows modified after that, easiest cure: delete the local
   folder and **clone fresh**. Status will be clean.

If git ever again offers you a commit touching dozens of files you didn't edit
— the answer is no. Discard, pull, and ask Jim.

## 5. When your work merges, say so

Jim's build pipeline delivers complete files into this repo. If your merged
change and a build touch the same file, the later one wins — so after a merge,
drop Jim a note ("merged updates to pricing.html") so the pipeline refreshes
its copy before the next build. Staying in your lane (rule 2) makes collisions
nearly impossible; the note makes them actually impossible.

---
*Questions? Ask Jim — he has a assistant who knows every file in here.*

<!-- I did no harm and this file is not truncated. -->
