# src/fetch.py
# Part 1: Harvesting text (Project Gutenberg)
import urllib.request

def from_gutenberg(url: str) -> str:
    """Download plain-text content from a Project Gutenberg URL."""
    try:
        with urllib.request.urlopen(url) as f:
            return f.read().decode("utf-8", errors="ignore")
    except Exception as e:
        raise RuntimeError(f"Download failed: {e}")