@echo off
REM ============================================
REM CaesarGuard - Windows Build Script
REM ============================================
REM Run this file ON A WINDOWS COMPUTER (double-click it)
REM Make sure caesarguard.py, caesarguard_logo.png, and
REM caesarguard_logo.ico are all in this same folder.

echo Installing required tools (only needed once)...
pip install pyinstaller pillow

echo Building CaesarGuard.exe with logo...
pyinstaller --onefile --windowed --name CaesarGuard --icon=caesarguard_logo.ico --add-data "caesarguard_logo.png;." --add-data "caesarguard_logo.ico;." caesarguard.py

echo.
echo Done! Your app is in the "dist" folder as CaesarGuard.exe
pause
