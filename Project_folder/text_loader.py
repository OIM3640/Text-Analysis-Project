import urllib.request
import re

def load_text(url):
    try:
        with urllib.request.urlopen(url) as f:
            text = f.read().decode('utf-8')
    except Exception as e:
        print("Error downloading text:", e)
        return ""

    # Remove Project Gutenberg header/footer
    start_match = re.search(r"\*\*\* START OF.*?\*\*\*", text)
    end_match = re.search(r"\*\*\* END OF.*?\*\*\*", text)

    if start_match and end_match:
        start = start_match.end()
        end = end_match.start()
        text = text[start:end]

    # Lowercase and remove punctuation
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)

    return text