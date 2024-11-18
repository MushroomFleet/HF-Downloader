# HuggingFace Repository Downloader

A command-line tool to download complete repositories from HuggingFace Hub, with support for batch downloading multiple repositories.

## Features
- Download entire HuggingFace repositories with a single command
- Batch download multiple repositories via queue system
- Support for specific branches and tags
- Progress tracking during downloads
- Windows batch scripts for easy setup and execution
- Download status reporting for each repository

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
python main.py "username/repo-name,username/repo-name2" ./save/path [--revision branch-or-tag]
```

### Windows Batch Script
```bash
run-downloader.bat "username/repo-name,username/repo-name2" ./save/path
```

### Examples
```bash
# Download multiple repositories
python main.py "THUDM/CogVideoX-5b-I2V,THUDM/CogVideoX1.5-5B" ./models

# Download multiple repos with specific revision
python main.py "bert-base-uncased,gpt2-medium" ./models --revision v1.0

# Interactive mode (Windows)
run-downloader.bat
```

### Queue Operation
1. Enter repositories as comma-separated list without spaces between entries:
   ```
   username/repo1,username/repo2,username/repo3
   ```
2. Downloads will process sequentially with progress tracking
3. Final status report shows success/failure for each repository

## Requirements
- Python 3.7+
- huggingface_hub>=0.20.3
- tqdm>=4.66.2
- requests>=2.31.0

## License
MIT

## Contributing
Pull requests welcome. For major changes, please open an issue first.
