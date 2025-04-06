import urllib.request
import ssl
import re
import nltk
from nltk.corpus import stopwords
from collections import Counter

# URL of the text file from Project Gutenberg
url = 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt'

# Headers to seem like a browser request  
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Ensure stopword corpus is downloaded
try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords')

# Create request object with specified URL and headers
req = urllib.request.Request(url, headers = headers)

# Create an unverified SSL context
context = ssl._create_unverified_context()

def strip_headers(text):
    """Remove the Project Gutenberg header and footer from the text."""

    # Find the start of the main content
    start = re.search(r"\*\*\* START OF.*PROJECT GUTENBERG EBOOK .* \*\*\*", text, re.IGNORECASE)
    if start:
        text = text[start.end():]

    # Find the end of the main content
    end = re.search (r"\*\*\* END OF.*PROJECT GUTENBERG EBOOK.* \*\*\*", text, re.IGNORECASE)
    if end:
        text = text[:end.start()]

    return text.strip()

def word_frequencies(text):
    """Calculate the frequency of each word in the text, excluding stopwords."""
    # Convert text to lowercase
    text = text.lower()

    # Replace punctuation with spaces
    for char in '.,!?;:()[]{}"\'-_':
        text = text.replace(char, ' ')
    
    # Split text into words
    words = text.split()

    # Remove stopwords and single-character words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words and len(word) > 1]

    return Counter(words)
    
def main():
    try:
        # Open the URL and read the raw text
        with urllib.request.urlopen(req, context=context) as f:
            raw_text = f.read().decode('utf-8')

            # Remove headers and footers from the text
            clean_text = strip_headers(raw_text)

            # Calculate word frequencies
            frequencies = word_frequencies(clean_text)

            # Get the top 10 most frequent words
            top_10 = frequencies.most_common(10)
            print(f"Length of top_10: {len(top_10)}")
            print("Top 10 most frequent words:")
            for word, count in top_10:
                print(f"{word}: {count}")

    except Exception as e:
        # Print any errors that occur
        print("An error occurred:", e)

if __name__ == "__main__":
    main()