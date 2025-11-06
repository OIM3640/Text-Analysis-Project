# Within my Macbook Terminal, I have already downloaded "conda install -c conda-forge pymediawiki"

from mediawiki import MediaWiki
w = MediaWiki()
p = w.page("James Harden")
print(p.title, " — chars:", len(p.content))  

#"re" for (remove [1] style citations + newlines) (Chatgpt suggested)
import re

# "json" to write our results to a .jsonl file (one JSON object per line)(Chatgpt suggested)
import json


from typing import Dict, List

# _CIT will find anything inside square brackets (prompted by chatgpt)
#_NL will find one or more newline characters (prompted by chatgpt)
_CIT = re.compile(r"\[.*?\]")
_NL  = re.compile(r"\n+")

#The following function cleans the text by removing citations and replacing newlines with spaces.
def clean_text(text: str) -> str:
    if not text:
        return ""
    text = _CIT.sub("", text) #Remoove bracketed citations
    text = _NL.sub(" ", text) # Turn multiple newlines into one single space
    return text.strip()

#The following funtion searches for a Wikipedia page by its title and returns the page object.
#Page.Title is the title of the page and the page.content is the full text of the article
#Fetch is also suggested by Chatg
def fetch_page(title: str):
    wikipedia = MediaWiki()
    page = wikipedia.page(title)
    return page

#From what we learned in class, I will be using a dictionary to store the titles and their corresponding cleaned text.
#Multiple pages will be downloaded at a time in a loop and stored in a dictionary.
#The output should be {"title" : "cleaned article text"}
def harvest_titles(titles: List[str], preview_chars: int = 600) -> Dict[str, str]:
    """Returns dict[title -> cleaned_text] and prints title + preview (per the doc)."""
    docs: Dict[str, str] = {}
    for t in titles:
        page = fetch_page(t)
        print(page.title)
        print(page.content[:preview_chars], "...\n")
        #Following line of code stores the cleaned text in the dictionary
        docs[page.title] = clean_text(page.content)
    return docs

#Save the documents to a JSONL file, where each line is a JSON object with "title" and "content" fields.
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
