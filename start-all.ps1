# SyntaxHire Launcher for PowerShell
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host "   Starting SyntaxHire Full Stack Application      " -ForegroundColor Cyan
Write-Host "===================================================" -ForegroundColor Cyan

$py = (Get-Command python -ErrorAction SilentlyContinue).Source
if (-not $py -or $py -like "*WindowsApps*") {
    $candidates = @(
        "$env:LOCALAPPDATA\Python\bin\python.exe",
        "$env:LOCALAPPDATA\Python\pythoncore-3.14-64\python.exe",
        "$env:LOCALAPPDATA\Programs\Python\Python*\python.exe"
    )
    foreach ($c in $candidates) {
        $found = Get-Item $c -ErrorAction SilentlyContinue | Select-Object -First 1
        if ($found) { $py = $found.FullName; break }
    }
}

if (-not $py) {
    Write-Host "Could not automatically locate python.exe. Please ensure Python is installed." -ForegroundColor Red
    exit 1
}

$backendScript = "cd '$PSScriptRoot\backend'; & '$py' -m uvicorn main:app --reload --host 0.0.0.0 --port 8000"
$frontendScript = "cd '$PSScriptRoot\frontend'; npm.cmd run dev"

Start-Process powershell -ArgumentList "-NoExit", "-Command", $backendScript
Start-Process powershell -ArgumentList "-NoExit", "-Command", $frontendScript

Write-Host "Launched both processes in separate PowerShell windows:" -ForegroundColor Green
Write-Host " - Backend API: http://localhost:8000/docs" -ForegroundColor Yellow
Write-Host " - Frontend UI: http://localhost:5173" -ForegroundColor Yellow
Write-Host " - Admin Credentials: admin / admin" -ForegroundColor Yellow
