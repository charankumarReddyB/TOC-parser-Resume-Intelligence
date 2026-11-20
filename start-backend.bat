@echo off
title SyntaxHire - Backend Server (FastAPI)
echo ===================================================
echo   Starting SyntaxHire Backend (FastAPI + Uvicorn)
echo ===================================================
cd backend

set PYTHON_CMD=python
where python >nul 2>nul
if %errorlevel% neq 0 (
    if exist "%LOCALAPPDATA%\Python\bin\python.exe" (
        set "PYTHON_CMD=%LOCALAPPDATA%\Python\bin\python.exe"
    ) else if exist "%LOCALAPPDATA%\Python\pythoncore-3.14-64\python.exe" (
        set "PYTHON_CMD=%LOCALAPPDATA%\Python\pythoncore-3.14-64\python.exe"
    )
)

echo Using Python: %PYTHON_CMD%
"%PYTHON_CMD%" -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
pause
