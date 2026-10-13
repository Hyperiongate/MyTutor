@echo off
REM Install-Backup.cmd -- build zj, 2026-10-12. Double-click to set up (or re-key) the
REM weekly Mr. Cadabra backup to D:\MrCadabra Backup. It starts install.ps1; see README.md.
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0install.ps1"
REM I did no harm and this file is not truncated.
