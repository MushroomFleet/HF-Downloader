"""
Core download functionality for HuggingFace repositories.
Uses huggingface_hub for direct repository downloads.
"""

from huggingface_hub import snapshot_download
from pathlib import Path
from typing import Optional

class HuggingFaceDownloader:
    def __init__(self, save_dir: str):
        """Initialize downloader with save directory."""
        self.save_dir = Path(save_dir)
        self.save_dir.mkdir(parents=True, exist_ok=True)

    def download_repository(self, repo_id: str, revision: Optional[str] = None) -> str:
        """
        Download complete repository from HuggingFace.
        
        Args:
            repo_id: Repository ID (e.g. 'username/repo-name')
            revision: Optional branch/tag name
            
        Returns:
            str: Path where repository was saved
        """
        local_dir = self.save_dir / repo_id.split('/')[-1]
        local_dir.mkdir(parents=True, exist_ok=True)
        
        return snapshot_download(
            repo_id=repo_id,
            revision=revision,
            local_dir=local_dir
        )

    def __call__(self, repo_id: str, revision: Optional[str] = None) -> str:
        """Shorthand for download_repository."""
        return self.download_repository(repo_id, revision)
