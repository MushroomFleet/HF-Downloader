@echo off
cd /d "%~dp0"

if not exist "venv" (
    echo Run install.bat first!
    pause
    exit /b 1
)

if "%~1"=="" (
    set /p REPO_ID="Enter repository ID (e.g. username/repo-name): "
) else (
    set REPO_ID=%~1
)

if "%~2"=="" (
    set /p SAVE_DIR="Enter save directory path: "
) else (
    set SAVE_DIR=%~2
)

call venv\Scripts\activate

python main.py "%REPO_ID%" "%SAVE_DIR%" %3 %4

call deactivate
pause