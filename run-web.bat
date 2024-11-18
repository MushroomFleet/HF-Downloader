@echo off
cd /d "%~dp0"

if not exist "venv" (
    echo Run install.bat first!
    pause
    exit /b 1
)

call venv\Scripts\activate

python gradio_app.py

call deactivate
pause