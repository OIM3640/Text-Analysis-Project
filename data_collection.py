from mediawiki import MediaWiki

def fetch_wikipedia_content(article_title):
    wikipedia = MediaWiki()
    page = wikipedia.page(article_title)
    return page.content

if __name__ == "__main__":
    text = fetch_wikipedia_content("Babson College")
    print(text)

# Clean the data

import re

def clean_text(text):
    text = re.sub(r'\[.*?\]', '', text)  # Remove citations like [1], [2]
    text = re.sub(r'\n+', ' ', text)     # Replace newlines with spaces
    return text.strip()


import pickle

def save_data(data, filename='wikipedia_article.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def load_data(filename='wikipedia_article.pkl'):
    with open(filename, 'rb') as f:
        return pickle.load(f)

