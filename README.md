# HuggingFace Repository Downloader

A simple command-line tool to download complete repositories from HuggingFace Hub.

## Features
- Download entire HuggingFace repositories with a single command
- Support for specific branches and tags
- Progress tracking during downloads
- Windows batch scripts for easy setup and execution

## Installation

### Windows
1. Ensure Python 3.7+ is installed
2. Run `install.bat` to set up the virtual environment and dependencies
3. Start downloading with `run-downloader.bat`

### Manual Installation
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

### Command Line
```bash
python main.py username/repo-name ./save/path [--revision branch-or-tag]
```

### Windows Batch Script
```bash
run-downloader.bat username/repo-name ./save/path
```

### Examples
```bash
# Download default branch
python main.py facebook/opt-350m ./models

# Download specific revision
python main.py bert-base-uncased ./models --revision v1.0
```

## Requirements
- Python 3.7+
- huggingface_hub>=0.20.3
- tqdm>=4.66.2
- requests>=2.31.0

## License
MIT

## Contributing
Pull requests welcome. For major changes, please open an issue first.
