# Wikipedia_Download.py
# Part 1: Fetch Harden season vs playoff pages from Wikipedia and save to JSONL.

from mediawiki import MediaWiki          # <-- you accidentally removed this import
import re, json
from typing import Dict, List

# --- cleaner ---
_CIT = re.compile(r"\[.*?\]")
_NL  = re.compile(r"\n+")

def clean_text(text: str) -> str:
    if not text:
        return ""
    text = _CIT.sub("", text)
    text = _NL.sub(" ", text)
    return text.strip()

# --- fetchers ---
def fetch_page(title: str):
    wikipedia = MediaWiki()
    return wikipedia.page(title)

def harvest_titles(titles: List[str], preview_chars: int = 600) -> Dict[str, str]:
    """Returns dict[title -> cleaned_text] and prints title + preview (per the doc)."""
    docs: Dict[str, str] = {}
    for t in titles:
        page = fetch_page(t)
        # EXACT behavior from the course example:
        print(page.title)
        print(page.content[:preview_chars], "...\n")
        docs[page.title] = clean_text(page.content)
    return docs

def save_jsonl(docs: Dict[str, str], path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        for title, content in docs.items():
            f.write(json.dumps({"title": title, "content": content}, ensure_ascii=False) + "\n")

# --- tiny runner so the file actually does something when executed ---
if __name__ == "__main__":
    TITLES = [
        "James Harden",
        "2017–18 Houston Rockets season",
        "2018 Western Conference Finals"
    ]
    docs = harvest_titles(TITLES, preview_chars=800)
    save_jsonl(docs, "harden_2018_season_vs_playoff.jsonl")
    print("\nSaved harden_2018_season_vs_playoff.jsonl with", len(docs), "docs.")
