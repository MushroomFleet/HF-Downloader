# HuggingFace Repository Downloader Project Manifest

## Project Structure
```
/
├── src/
│   ├── __init__.py
│   └── downloader.py
├── install.bat
├── main.py
├── requirements.txt
└── run-downloader.bat
```

## File Descriptions

### Core Files
- `main.py` - Command line interface and entry point
- `requirements.txt` - Python package dependencies

### Source Directory
- `src/__init__.py` - Package initialization and basic download functionality
- `src/downloader.py` - Core downloader implementation class

### Batch Scripts
- `install.bat` - Windows setup script (creates venv and installs dependencies)
- `run-downloader.bat` - Windows execution wrapper script

## Dependencies
- huggingface_hub (>=0.20.3)
- tqdm (>=4.66.2)
- requests (>=2.31.0)

## Entry Points
- Command line: `python main.py`
- Windows: `run-downloader.bat`

## Installation
Run `install.bat` to set up virtual environment and install dependencies
