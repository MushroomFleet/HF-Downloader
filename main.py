"""
Command line interface for HuggingFace repository downloads.
Provides user-friendly command line options for downloading multiple HuggingFace repositories.
"""

import argparse
import os
from pathlib import Path
from src.downloader import HuggingFaceDownloader
from src.queue_manager import DownloadQueue

def validate_path(path: str) -> str:
    """Validate and normalize directory path."""
    try:
        path = os.path.abspath(os.path.expanduser(path))
        os.makedirs(path, exist_ok=True)
        return path
    except Exception as e:
        raise argparse.ArgumentTypeError(f"Invalid directory path: {e}")

def validate_repo_ids(repo_ids: str) -> list:
    """Validate repository IDs format."""
    repos = [repo.strip() for repo in repo_ids.split(',')]
    for repo in repos:
        if '/' not in repo:
            raise argparse.ArgumentTypeError(
                f"Invalid repository ID '{repo}'. Must be in format 'username/repo-name'"
            )
    return repos

def main():
    parser = argparse.ArgumentParser(
        description="Download complete HuggingFace repositories",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "facebook/opt-350m,bert-base-uncased" ./models
  %(prog)s "THUDM/CogVideoX-5b-I2V,THUDM/CogVideoX1.5-5B" ./models --revision main
"""
    )
    
    parser.add_argument(
        "repo_ids",
        type=validate_repo_ids,
        help="Comma-separated repository IDs (e.g. 'username/repo-name,username2/repo-name2')"
    )
    
    parser.add_argument(
        "save_dir",
        type=validate_path,
        help="Directory to save repositories"
    )
    
    parser.add_argument(
        "--revision",
        help="Branch or tag name (default: main branch)",
        default="main"
    )

    args = parser.parse_args()

    try:
        downloader = HuggingFaceDownloader(args.save_dir)
        queue = DownloadQueue(downloader)
        
        # Add all repositories to queue
        for repo_id in args.repo_ids:
            queue.add(repo_id, args.revision)
        
        # Process queue
        results = queue.process()
        
        # Print results
        print("\nDownload Results:")
        for repo_id, result in results.items():
            if isinstance(result, Exception):
                print(f"❌ {repo_id}: {result}")
            else:
                print(f"✓ {repo_id}: {result}")
        
        return 0 if all(not isinstance(r, Exception) for r in results.values()) else 1
        
    except Exception as e:
        print(f"\nError: {e}")
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(main())