@echo off
title HF Repo Downloader Setup

REM Change to project root directory
cd /d "%~dp0"

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo Python not found!
    pause
    exit /b 1
)

REM Remove existing venv if present
if exist "venv" rmdir /s /q "venv"

REM Create fresh venv
python -m venv venv
call venv\Scripts\activate

REM Upgrade pip and install requirements
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Verify installation
python -c "from huggingface_hub import snapshot_download" >nul 2>&1
if errorlevel 1 (
    echo Package verification failed!
    pause
    exit /b 1
)

echo Setup complete!
pause
