from mediawiki import MediaWiki
import re

def fetch_wikipedia_content(article_title):
    """Fetch content of a Wikipedia article by title."""
    wikipedia = MediaWiki()
    page = wikipedia.page(article_title)
    return page.content

def clean_text(text):
    """Clean the text by removing citations and newlines."""
    text = re.sub(r'\[.*?\]', '', text)  
    text = re.sub(r'\n+', ' ', text)     
    return text.strip()


import pickle

def save_data(data, filename="wikipedia_article.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(data, f)


def load_data(filename="wikipedia_article.pkl"):
    with open(filename, "rb") as f:
        return pickle.load(f)
