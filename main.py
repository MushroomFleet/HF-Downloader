"""
Command line interface for HuggingFace repository downloads.
Provides user-friendly command line options for downloading HuggingFace repositories.
"""

import argparse
import os
from pathlib import Path
from src.downloader import HuggingFaceDownloader

def validate_path(path: str) -> str:
    """Validate and normalize directory path."""
    try:
        path = os.path.abspath(os.path.expanduser(path))
        os.makedirs(path, exist_ok=True)
        return path
    except Exception as e:
        raise argparse.ArgumentTypeError(f"Invalid directory path: {e}")

def validate_repo_id(repo_id: str) -> str:
    """Validate repository ID format."""
    if '/' not in repo_id:
        raise argparse.ArgumentTypeError(
            "Repository ID must be in format 'username/repo-name'"
        )
    return repo_id

def main():
    parser = argparse.ArgumentParser(
        description="Download complete HuggingFace repositories",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s facebook/opt-350m ./models
  %(prog)s bert-base-uncased ./models --revision main
"""
    )
    
    parser.add_argument(
        "repo_id",
        type=validate_repo_id,
        help="Repository ID (e.g. 'username/repo-name')"
    )
    
    parser.add_argument(
        "save_dir",
        type=validate_path,
        help="Directory to save repository"
    )
    
    parser.add_argument(
        "--revision",
        help="Branch or tag name (default: main branch)",
        default="main"
    )

    args = parser.parse_args()

    try:
        downloader = HuggingFaceDownloader(args.save_dir)
        saved_path = downloader(args.repo_id, args.revision)
        print(f"\nRepository successfully downloaded to: {saved_path}")
        return 0
        
    except Exception as e:
        print(f"\nError: {e}")
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(main())