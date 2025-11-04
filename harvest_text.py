"""
Part 1 Harvesting Text from the Internet
Author: Sophia Pak
"""

import urllib.request
import os
import pickle


def download_gutenberg_text(url: str) -> str:
    """Download plain text from Project Gutenberg."""
    try:
        with urllib.request.urlopen(url) as f:
            text = f.read().decode("utf-8")
        print("Successfully downloaded text from Project Gutenberg.")
        return text
    except Exception as e:
        print("Error downloading Gutenberg text:", e)
        return ""


def save_text(text: str, filename: str):
    """Save text locally as a pickle file."""
    with open(filename, "wb") as f:
        pickle.dump(text, f)
    print(f"Text saved to {filename}")


def load_text(filename: str) -> str:
    """Load text from a pickle file."""
    with open(filename, "rb") as f:
        text = pickle.load(f)
    print(f"Loaded text from {filename}")
    return text


def main():
    # *A Perfect Gentleman* by Ralph Hale Mottram (public domain)
    gutenberg_url = "https://www.gutenberg.org/cache/epub/72949/pg72949.txt"
    filename = "a_perfect_gentleman.pkl"

    # Download and save if not already downloaded
    if not os.path.exists(filename):
        text = download_gutenberg_text(gutenberg_url)
        if text:
            save_text(text, filename)
    else:
        text = load_text(filename)


if __name__ == "__main__":
    main()
