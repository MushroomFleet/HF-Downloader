"""
HuggingFace Repository Downloader 
Simple downloader for complete HuggingFace repositories.
"""

from huggingface_hub import snapshot_download

def download_repo(repo_id: str, local_dir: str) -> str:
    """
    Download complete repository from HuggingFace.
    
    Args:
        repo_id: Repository ID (e.g. 'username/repo-name')
        local_dir: Local directory to save files
        
    Returns:
        str: Path where repository was saved
    """
    return snapshot_download(repo_id=repo_id, local_dir=local_dir)

__version__ = "1.0.0"
