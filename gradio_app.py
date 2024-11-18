"""
Gradio web interface for HuggingFace Repository Downloader.
Provides a user-friendly GUI for downloading repositories.
"""

import gradio as gr
from pathlib import Path
from typing import Tuple
import json
from src.downloader import HuggingFaceDownloader
from src.queue_manager import DownloadQueue

class GradioDownloader:
    def __init__(self):
        self.download_history = []
        
    def process_download(self, repo_ids: str, save_dir: str, revision: str = "main") -> Tuple[str, str]:
        """Process repository downloads and return results."""
        try:
            # Validate inputs
            if not repo_ids or not save_dir:
                return "Error", "Repository IDs and save directory are required."
                
            # Clean and validate repo IDs
            repos = [repo.strip() for repo in repo_ids.split(',')]
            if not all('/' in repo for repo in repos):
                return "Error", "Invalid repository format. Use 'username/repo-name' format."
                
            # Initialize downloader and queue
            save_path = Path(save_dir)
            save_path.mkdir(parents=True, exist_ok=True)
            
            downloader = HuggingFaceDownloader(save_dir)
            queue = DownloadQueue(downloader)
            
            # Add repositories to queue
            for repo_id in repos:
                queue.add(repo_id, revision)
            
            # Process downloads
            results = queue.process()
            
            # Format results
            success_count = sum(1 for r in results.values() if not isinstance(r, Exception))
            failed_count = len(results) - success_count
            
            result_details = []
            for repo_id, result in results.items():
                status = "✓" if not isinstance(result, Exception) else "❌"
                message = str(result) if isinstance(result, Exception) else "Successfully downloaded"
                result_details.append(f"{status} {repo_id}: {message}")
            
            # Update history
            self.download_history.append({
                "repo_ids": repos,
                "save_dir": save_dir,
                "revision": revision,
                "results": result_details
            })
            
            summary = f"Completed: {success_count} successful, {failed_count} failed"
            details = "\n".join(result_details)
            
            return summary, details
        except Exception as e:
            return "Error", f"An unexpected error occurred: {str(e)}"
            
    def launch_interface(self):
        """Create and launch the Gradio interface."""
        with gr.Blocks(title="HuggingFace Repository Downloader") as interface:
            gr.Markdown("# HuggingFace Repository Downloader")
            gr.Markdown("Download complete repositories from HuggingFace Hub")
            
            with gr.Row():
                with gr.Column():
                    repo_ids = gr.Textbox(
                        label="Repository IDs",
                        placeholder="username/repo-name,username/repo-name2",
                        info="Comma-separated list of repository IDs"
                    )
                    save_dir = gr.Textbox(
                        label="Save Directory",
                        placeholder="Path to save repositories",
                        info="Local directory path where repositories will be saved"
                    )
                    revision = gr.Textbox(
                        label="Revision (Optional)",
                        value="main",
                        info="Branch or tag name"
                    )
                    download_btn = gr.Button("Download Repositories", variant="primary")
                
                with gr.Column():
                    status_output = gr.Textbox(label="Status", interactive=False)
                    details_output = gr.Textbox(
                        label="Details",
                        interactive=False,
                        max_lines=10
                    )
            
            download_btn.click(
                fn=self.process_download,
                inputs=[repo_ids, save_dir, revision],
                outputs=[status_output, details_output]
            )
            
        return interface

def main():
    """Launch the Gradio interface."""
    app = GradioDownloader()
    interface = app.launch_interface()
    interface.launch(
        server_name="localhost",
        server_port=7860,
        share=False
    )

if __name__ == "__main__":
    main()