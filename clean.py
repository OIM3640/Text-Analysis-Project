# clean the feteched data 

import unicodedata 
import re
import nltk 
from nltk.corpus import stopwords


def split_line(line:str): # Finds split lines so tokenization is easier 
    return line.replace('-', ' ').replace('–', ' ').replace('—', ' ').split()

def find_punctuation(text:str):  # Finds punctuation in text to remove 
    punc_marks = {}
    for char in text:
        category = unicodedata.category(char)
        if category.startswith("P"):
            punc_marks[char] = 1
    return "".join(punc_marks)

def clean_word(word: str, punctuation: str):
    return word.strip(punctuation).lower()

POSSESSIVE_RE    = re.compile(r"[’']s\b")    # samsung's -> samsung
TRAILING_APOS_RE = re.compile(r"s[’']\b")    # companies' -> companies
URL_RE        = re.compile(r'(https?://\S+|www\.[^\s]+)', re.IGNORECASE)
DIGITS_RE     = re.compile(r'\d+')
MULTISPACE_RE = re.compile(r'\s+')


def clean_basic(text: str) -> str:
    """Remove URLs, possessives, digits/numbers, and collapse whitespace.
    I am familiar with the reason we needed to preprocess and clean the data, and AI
    helped suggest a way to do it"""
    # remove URLs
    text = URL_RE.sub(' ', text)
    # normalize curly and straight apostrophes first (to make regex consistent)
    text = text.replace("’", "'").replace("‘", "'")
    # remove possessive endings (e.g., samsung's → samsung)
    text = re.sub(r"\b(\w+)'s\b", r"\1", text)
    # remove plural possessives (e.g., companies' → companies)
    text = re.sub(r"\b(\w+)'\b", r"\1", text)
    # remove digits and numbers (e.g., 2024, 10,000)
    text = DIGITS_RE.sub(' ', text)
    # collapse multiple spaces/newlines/tabs
    text = MULTISPACE_RE.sub(' ', text).strip()
    return text

def clean_then_strip_punct_and_lower(text: str) -> list[str]:  # Tokenizes Words 
    cleaned = clean_basic(text)
    punctuation = find_punctuation(cleaned)
    words = []
    for line in cleaned.splitlines():
        for w in split_line(line):
            w = clean_word(w, punctuation)
            if w:
                words.append(w)
    return words
# download once (safe to leave here)
nltk.download('stopwords', quiet=True)

# base English stopwords
STOP = set(stopwords.words('english'))

# optional: domain-specific stopwords for Wikipedia/company pages (AI helped generate this idea to me since it made sense to get rid of generic words)
EXTRA_STOP = {
    'inc', 'ltd', 'co', 'corp', 'corporation', 'company',
    'electronics', 'technology', 'software', 'services',
    'usa', 'us', 'u', 's', '===','==','=', # sometimes appear after punctuation removal and AI helped me get rid of these words by suggesting this method
}
STOP |= EXTRA_STOP

def remove_stopwords(tokens: list[str]) -> list[str]:
    """Filter out stop words and very short leftovers."""
    return [t for t in tokens if t not in STOP and len(t) > 2]
