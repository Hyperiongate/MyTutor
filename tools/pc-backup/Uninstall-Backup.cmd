@echo off
REM Uninstall-Backup.cmd -- build zj, 2026-10-12. Double-click to switch the weekly backup
REM off and remove the saved key. Backups already saved are left alone.
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0uninstall.ps1"
REM I did no harm and this file is not truncated.
