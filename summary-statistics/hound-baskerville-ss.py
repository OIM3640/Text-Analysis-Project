import urllib.request
import ssl
import re
import nltk
from nltk.corpus import stopwords
from collections import Counter

nltk.download('stopwords')

url = 'https://www.gutenberg.org/cache/epub/2852/pg2852.txt'

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords')

req = urllib.request.Request(url, headers = headers)

context = ssl._create_unverified_context()

def strip_headers(text):
    start = re.search(r"\*\*\* START OF.*PROJECT GUTENBERG EBOOK .* \*\*\*", text, re.IGNORECASE)
    if start:
        text = text[start.end():]

    end = re.search (r"\*\*\* END OF.*PROJECT GUTENBERG EBOOK.* \*\*\*", text, re.IGNORECASE)
    if end:
        text = text[:end.start()]

    return text.strip()

def word_frequencies(text):
    text = text.lower()
    for char in '.,!?;:()[]{}"\'-_':
        text = text.replace(char, ' ')
    
    words = text.split()

    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words and len(word) > 1]

    return Counter(words)
    
try:
    with urllib.request.urlopen(req, context=context) as f:
        raw_text = f.read().decode('utf-8')
        clean_text = strip_headers(raw_text)

        frequencies = word_frequencies(clean_text)

        top_10 = frequencies.most_common(10)
        print(f"Length of top_10: {len(top_10)}")
        print("Top 10 most frequent words:")
        for word, count in top_10:
            print(f"{word}: {count}")

except Exception as e:
    print("An error occurred:", e)