import re 
import urllib.request
import pickle
import os
import nltk
from nltk.corpus import stopwords  


def download_book(gutenberg_url, file_name):
    """
    Downloads a book from a given Gutenberg URL, saves it to disk if it hasn't been saved before, 
    and returns the text. This helps avoid repeated downloads by saving the file locally.
    
    Args:
        gutenberg_url (str): The URL to download the book from.
        file_name (str): The local file name to save the downloaded text.
    
    Returns:
        str: The content of the book as a string.
    """
    if os.path.exists(file_name):
        with open(file_name, 'rb') as f:
            reloaded_copy_of_texts = pickle.load(f)
            return reloaded_copy_of_texts
    else:
        with urllib.request.urlopen(gutenberg_url) as f:
            text = f.read().decode('utf-8')
        with open(file_name, 'wb') as f:
            pickle.dump(text, f)
            return text


# Download NLTK stopwords 
nltk.download('stopwords')
STOP_WORDS = set(stopwords.words('english'))
MORE_STOP_WORDS = {"so", "im", "from", "he", "she", "but", "my", "his", "him", "me", "you", "at", "her", "had", 
                   "we", "i", "and", "the", "a", "an", "in", "to", "of", "that", "it", "is", "for", "with", "as", 
                   "on", "this", "by", "was", "be", "or", "are"}
STOP_WORDS.update(MORE_STOP_WORDS)

def clean_text(text):
    """
    Cleans the text by converting it to lowercase, removing punctuation, and filtering out 
    common stop words. Returns the cleaned text as a single string.
    
    Args:
        text (str): The raw text to clean.
    
    Returns:
        str: The cleaned text.
    """
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    filtered_words = [word for word in words if word not in STOP_WORDS]
    cleaned_text = " ".join(filtered_words)
    return cleaned_text