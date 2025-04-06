import urllib.request
import ssl
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

# URL of the text file from Project Gutenberg
url = 'https://www.gutenberg.org/cache/epub/37106/pg37106.txt'

# Headers to seem like a browser request. Otherwise, I was encountering issues with the output.
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Ensure the stopwords corpus is downloaded
try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords')

# Create a request object with the specified URL and headers
req = urllib.request.Request(url, headers = headers)

# Create an unverified SSL context. Code wouldn't run otherwise
context = ssl._create_unverified_context()

def strip_headers(text):
    """Remove header and footer from the text"""

    # Find the start
    start = re.search(r"\*\*\* START OF.*PROJECT GUTENBERG EBOOK .* \*\*\*", text, re.IGNORECASE)
    if start:
        text = text[start.end():]

    # Find the end 
    end = re.search (r"\[Illustration\]", text, re.IGNORECASE)
    if end:
        text = text[:end.start()]

    return text.strip()

def word_frequencies(text):
    """Calculate the frequency of each word in the text, excluding stopwords."""

    # Convert text to lowercase
    text = text.lower()
    
    # Replace punctuation with space
    for char in '.,!?;:()[]{}"\'-_':
        text = text.replace(char, ' ')
    
    # Split text into words
    words = text.split()

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    # Count word frequencies
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

try:
    # Open the URL and read the raw text
    with urllib.request.urlopen(req, context=context) as f:
        raw_text = f.read().decode('utf-8')
        # Remove headers and footers from the text
        clean_text = strip_headers(raw_text) 
        print(clean_text)

        # Calculate word frequencies
        frequencies = word_frequencies(clean_text)

        # Print word frequencies
        print(frequencies)

# Print any errors that occur
except Exception as e:

    print("An error occurred:", e)

