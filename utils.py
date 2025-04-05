import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download these once
nltk.download('punkt')
nltk.download('stopwords')

def clean_text(text):
    # Make lowercase
    text = text.lower()
    
    # Split into words
    words = word_tokenize(text)
    
    # Get English stop words (like "the", "and")
    stop_words = set(stopwords.words('english'))
    
    # Keep only real words (not punctuation or stop words)
    cleaned_words = []
    for word in words:
        if word.isalpha() and word not in stop_words:
            cleaned_words.append(word)
    
    # Join cleaned words back into one string
    return ' '.join(cleaned_words)
