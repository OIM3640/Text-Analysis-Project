# src/clean.py
import re
from typing import List, Iterable

# A compact default stopword list (you can add more if you want)
STOPWORDS = {
    "the","a","an","and","or","but","if","then","else","for","to","in","of","on","at",
    "by","with","from","as","is","are","was","were","be","been","being",
    "that","this","these","those","it","its","i","you","he","she","we","they",
    "me","him","her","them","my","your","his","their","our","yours","ours","theirs",
    "not","no","so","too","very","can","could","should","would","may","might","will",
    "do","does","did","done","have","has","had","having","about","into","over","under",
    "up","down","out","off","than","such"
}

WORD_RE = re.compile(r"[a-z']+")         # keep words & simple contractions
SENT_RE = re.compile(r"[.!?]+")

def to_lower(text: str) -> str:
    return text.lower()

def tokenize_words(text: str) -> List[str]:
    return WORD_RE.findall(text)

def remove_stopwords(tokens: Iterable[str]) -> List[str]:
    return [t for t in tokens if t not in STOPWORDS and len(t) > 1]

def split_sentences(text: str) -> List[str]:
    # crude sentence split—good enough for summary stats
    return [s.strip() for s in SENT_RE.split(text) if s.strip()]
