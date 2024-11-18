"""
Queue management for HuggingFace repository downloads.
Handles sequential processing of multiple repository downloads.
"""

from typing import Dict, Union, Optional
from pathlib import Path
import time
from tqdm import tqdm

class DownloadQueue:
    def __init__(self, downloader):
        """Initialize download queue."""
        self.downloader = downloader
        self.queue = []
        self.results = {}

    def add(self, repo_id: str, revision: Optional[str] = None) -> None:
        """Add repository to download queue."""
        self.queue.append((repo_id, revision))

    def process(self) -> Dict[str, Union[str, Exception]]:
        """
        Process all queued downloads sequentially.
        Returns dict mapping repo_ids to either success paths or exceptions.
        """
        with tqdm(total=len(self.queue), desc="Processing Queue") as pbar:
            for repo_id, revision in self.queue:
                try:
                    pbar.set_description(f"Downloading {repo_id}")
                    result = self.downloader(repo_id, revision)
                    self.results[repo_id] = result
                except Exception as e:
                    self.results[repo_id] = e
                finally:
                    pbar.update(1)
                    time.sleep(0.1)  # Prevent potential rate limiting

        return self.results