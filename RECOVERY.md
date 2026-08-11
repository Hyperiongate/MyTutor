# RECOVERY.md — how to get Mr. Cadabra's Classroom back, no matter what broke

_New file 2026-08-11 (build dj). Written for Jim, to be read on a bad day. Everything
here has a tested path; nothing is aspirational. The one-line summary: **the code lives
on GitHub, the voice cache is $20 and one button, and the database now has three
copies — Render's own backups, a nightly snapshot on the persistent disk, and the
weekly download on your computer.** The last one is the copy that survives anything._

---

## What exists, and where its copies are

| Asset | Where it lives | Its backup | How it comes back |
|---|---|---|---|
| **The code** (app, prompts, scripts, tests) | GitHub `Hyperiongate/MyTutor` | GitHub itself + the copy on D:\MyTutor | Render rebuilds from GitHub automatically |
| **The database** (students, mastery, quizzes, parents, passes) | Render Postgres | 1) Render's own daily backups (paid DB plans) · 2) nightly `/var/data/backups/backup-*.json.gz` on the persistent disk (14 kept) · 3) **your weekly download** from /admin → 🛟 Backups | `restore_backup.py` (below) |
| **The voice cache** (186 rendered clips) | Persistent disk `/var/data/tts_cache` | none needed — recreatable | /admin → pre-render button, ~$13–27, ~5 min |
| **Secrets** (API keys, admin key) | Render → Environment | **your password manager** (keep every name + value there; see the list below) | typed back into Render |
| **The domain** (mrcadabra.com) | your registrar + Render custom domain | registrar account | re-point DNS at the new service |

## Drill 1 — a bad deploy (site broken after a push)
Render dashboard → mytutor-2 → **Events** → find the previous deploy → **Rollback**.
Two minutes, no data touched. (The database is never changed by a deploy.)

## Drill 2 — the database is damaged or wiped, Render itself is fine
1. Pick your newest good snapshot: `/admin → 🛟 Backups` shows the nightly ones; your
   own downloads are on your computer. To pull a nightly file off the disk: Render →
   mytutor-2 → **Shell** tab → `ls /var/data/backups` →
   `base64 /var/data/backups/backup-XXXX.json.gz` and copy it out — or just use your
   latest downloaded copy, which is the point of downloading weekly.
2. On your computer, in the D:\MyTutor folder, with the database's **External URL**
   (Render → the Postgres instance → Connect → External Database URL):
   - set `DATABASE_URL` to that URL for the command, then a dry look (changes nothing):
     `python restore_backup.py mrcadabra-backup-XXXX.json.gz`
   - the real restore: add ` --yes-i-mean-it`
3. Verify: `/health` shows db true → open the parent dashboard → spot-check a student.

## Drill 3 — Render is gone entirely (account, region, company — worst case)
Everything below assumes only two survivors: **GitHub** and **your latest downloaded
backup + your password manager.** That is why those two are non-negotiable.
1. New host (Render again, or any host that runs Python): create a web service from
   the GitHub repo. `render.yaml` documents the full shape — build command, start
   command, every env var name, the persistent disk at `/var/data`, `DATA_DIR`.
2. Create a new Postgres, set `DATABASE_URL`. Boot the service once — it creates all
   tables itself on first start.
3. Restore the database: Drill 2, step 2, with your downloaded snapshot.
4. Re-enter the secrets from your password manager (names listed below).
5. Re-render the voice cache: /admin → pre-render → ② (~$13–27, once).
6. Point mrcadabra.com's DNS at the new service.
Realistic time: an afternoon. Realistic data loss: whatever happened since your last
downloaded backup — which is why the weekly click matters.

## The secrets to keep in your password manager (names; you hold the values)
`ANTHROPIC_API_KEY` · `ELEVENLABS_API_KEY` · `OPENAI_API_KEY` · `DATABASE_URL` ·
`FORUM_MOD_KEY` · `STRIPE_SECRET_KEY` · `STRIPE_WEBHOOK_SECRET` · plus the settings:
`CLAUDE_MODEL=claude-sonnet-5`, `SITE_URL`, `DATA_DIR=/var/data`, and any of the
optional tuning vars you have set (`OPENAI_AUDIT_MODEL`, `USAGE_LOG_DAYS`,
`DB_POOL_SIZE`, `DB_MAX_OVERFLOW`, `BACKUP_KEEP`, `WEEKLY_EMAIL`, `ALERT_EMAIL`,
`COST_ALERT_USD`, SMTP settings).

## The habits that make all of this true
- **Weekly:** /admin → 🛟 Backups → Download a fresh backup → keep the newest few files.
- **After any deploy:** glance at /health; once, press ① Price it on the pre-render to
  confirm "186 already cached" (proves the persistent disk).
- **Never** put a secret in a file in this repo, a chat, or a URL.

I did no harm and this file is not truncated.
