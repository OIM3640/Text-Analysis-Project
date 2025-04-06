import urllib.request
import ssl
import re
import nltk
from nltk.corpus import stopwords
from collections import defaultdict, Counter
import random

# List of URLs of text files from Project Gutenberg
gutenberg_urls = [
    'https://www.gutenberg.org/cache/epub/98/pg98.txt',
    'https://www.gutenberg.org/cache/epub/64317/pg64317.txt',
    'https://www.gutenberg.org/cache/epub/2852/pg2852.txt',
    'https://www.gutenberg.org/cache/epub/37106/pg37106.txt',
    'https://www.gutenberg.org/cache/epub/16/pg16.txt'
]

# Headers to seem like a browser request
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Ensure the stopwords corpus is downloaded
try: 
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords')

# Create an unverified SSL context
context = ssl._create_unverified_context()

def strip_headers(text):
    """Remove the Project Gutenberg header and footer from the text."""

    # Find the start of the main content
    start = re.search(r"\*\*\* START OF.*PROJECT GUTENBERG EBOOK .* \*\*\*", text, re.IGNORECASE)
    if start:
        text = text[start.end():]

    # Find the end of the main content
    end = re.search(r"\*\*\* END OF.*PROJECT GUTENBERG EBOOK.* \*\*\*|\[Illustration\]", text, re.IGNORECASE)
    if end:
        text = text[:end.start()]

    return text.strip()

def find_words(text):
    """Convert text to lowercase, remove punctuation, and split into words."""
    # Convert text to lowercase
    text = text.lower()

    # Replace punctuation with spaces
    for char in '.,!?;:()[]{}""\'-_':
        text = text.replace(char, ' ')  

    # Remove Roman numerals
    text = re.sub(r'\b(?:[IVXLCDM]+)\b', '', text)   

    return text.split()

def create_markov_model(tokens, n=1):
    """Create a Markov model. AI helped a lot with this section because I did not know what to do"""

    model = defaultdict(Counter)
    for i in range(len(tokens) - n):
        state = tuple(tokens[i:i+n])
        next_state = tokens [i+n]
        model[state] [next_state] += 1
    return model

def generate_text(model, length=100, n=1):
    """Generate text using the Markov model."""

    # Random starting state
    state = random.choice(list(model.keys()))
    output = list(state)
    
    for _ in range(length - n):
        # If the state is not in the model or has no next states, choose a new random state
        if state not in model or not model [state]:
            state = random.choice(list(model.keys()))

        # Choose the next state based on the probabilities in the model
        next_state = random.choices(list(model[state].keys()), list(model[state].values()))[0]
        output.append(next_state)
        state = tuple(output[-n:])

    return ' '.join(output)

def main():
    all_tokens = []

    # Process each URL in the list, clean it, and print any errors if necessary
    for url in gutenberg_urls:
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, context=context) as f:
                raw_text = f.read().decode('utf-8')
                clean_text = strip_headers(raw_text)
                tokens = find_words(clean_text)
                all_tokens.extend(tokens)
        except Exception as e:
            print(f"An error occurred with {url}: {e}")

    # Create a Markov model and generate text
    markov_model = create_markov_model(all_tokens, n=5)
    generated_text = generate_text(markov_model, length=25, n=5)
    print(generated_text)

if __name__ == "__main__":
    main()