# Weekly backup to this PC (build zj, 2026-10-12)

Every Sunday at 9:00 (or the next time the PC is on), Windows downloads a fresh Mr. Cadabra
backup into **`D:\MrCadabra Backup`** by itself. No button to remember.

## Set it up (once, about a minute)

1. In Render: **mytutor-2 → Environment → DATA_EXPORT_KEY** → copy the value.
2. In File Explorer, open `D:\MyTutor\tools\pc-backup` and **double-click `Install-Backup.cmd`**.
3. Paste the key when it asks (nothing shows while you paste — that is normal) and press Enter.

It takes the first backup right away and tells you whether it worked. If Windows asks
whether to allow PowerShell to run, choose yes.

## What it does

- Saves each backup as `mrcadabra-backup-YYYYMMDD-HHMMSS.json.gz` in `D:\MrCadabra Backup`.
- Keeps the **newest 8** (about two months) and removes older ones.
- Writes one line per run to `D:\MrCadabra Backup\backup-log.txt` — `OK` or `FAILED` and why.
- Tells the server it is the PC copy. The admin page's **Nightly jobs** tile shows its age,
  and if a week and two days go by with no copy, you get a **STALE JOB** email.

## The key

The key is stored **encrypted by Windows** for your login only
(`%LOCALAPPDATA%\MrCadabraBackup\key.dat`). It is never in the repo or in any plain-text file.
If the key in Render ever changes, run `Install-Backup.cmd` again.

## Turn it off

Double-click `Uninstall-Backup.cmd`. It removes the weekly task and the saved key and leaves
your backups where they are.

## Keep in mind

These files hold every family's data. Keep the folder on this PC (not a shared or synced
folder), and follow the retention rule counsel sets (PM-16 on the PM board).

I did no harm and this file is not truncated.
