@echo off
title SyntaxHire - Master Launcher
echo ===================================================
echo   Starting SyntaxHire Full Stack Application
echo ===================================================
echo Starting Backend API on http://localhost:8000 ...
start "SyntaxHire Backend (Port 8000)" cmd /k "%~dp0start-backend.bat"

echo Starting Frontend on http://localhost:5173 ...
start "SyntaxHire Frontend (Port 5173)" cmd /k "%~dp0start-frontend.bat"

echo.
echo Both servers are launching in separate windows!
echo - Frontend: http://localhost:5173
echo - Backend API Docs: http://localhost:8000/docs
echo - Default Admin Login: username: admin / password: admin
echo ===================================================
pause
