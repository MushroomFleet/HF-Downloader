# HuggingFace Repository Downloader

A tool to download complete repositories from HuggingFace Hub, featuring both Web UI and command-line interfaces.

## Web Interface Usage

1. **Install Dependencies**
   - Run `install.bat` to set up the virtual environment
   - Wait for the installation to complete

2. **Launch Web Interface**
   - Run `run-web.bat` to start the web server
   - Open `http://localhost:7860` in your browser

3. **Download Repositories**
   - Enter repository IDs (comma-separated): `username/repo-name,username/repo-name2`
   - Specify save directory path
   - Optional: Set revision/branch (default: main)
   - Click "Download Repositories"
   - Monitor download progress and results in the status area

## Command Line Usage

### Windows Quick Start
```bash
run-downloader.bat "username/repo-name,username/repo-name2" ./save/path
```

### Manual Command
```bash
python main.py "username/repo-name,username/repo-name2" ./save/path [--revision branch-or-tag]
```

### Examples
```bash
# Download multiple repositories
python main.py "THUDM/CogVideoX-5b-I2V,THUDM/CogVideoX1.5-5B" ./models

# Download with specific revision
python main.py "bert-base-uncased,gpt2-medium" ./models --revision v1.0
```

## Features
- Download entire HuggingFace repositories
- Batch download multiple repositories
- Support for specific branches and tags
- Progress tracking
- Status reporting for each repository
- Web and command-line interfaces

## Requirements
- Python 3.7+
- huggingface_hub>=0.20.3
- tqdm>=4.66.2
- requests>=2.31.0
- gradio==4.44.1

## Installation

### Windows Setup
1. Ensure Python 3.7+ is installed
2. Run `install.bat`
3. Use either `run-web.bat` or `run-downloader.bat`

### Manual Setup
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## License
MIT

## Contributing
Pull requests welcome. For major changes, please open an issue first.
