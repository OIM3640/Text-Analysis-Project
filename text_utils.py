# text_utils.py
# Basic cleaning, tokenizing, stopwords, and small helpers.
#
# AI Assistance (ChatGPT, November 2025):
# - Used for generating stopword list (tedious task of compiling common stopwords)
# - Used for documentation: Writing docstrings and comments explaining preprocessing steps
# - Used for troubleshooting: "How to remove HTML tags and decode HTML entities in Python text"

import re
from collections import Counter
from typing import List, Dict, Tuple
import html

DEFAULT_STOPWORDS = {
    "the","and","a","of","to","in","it","is","i","was","for","on","that","this",
    "with","but","movie","film","you","they","he","she","we","are","as","an","be",
    "by","or","at","from","so","if","not","have","has","had","its","my","me","your",
    "their","our","them","his","her","which","who","what","when","where","how",
    "can","could","should","would","did","do","does","than","then","there","here",
    "about","into","out","up","down","over","again","more","also","just"
}

def clean_text(s: str) -> str:
    s = (s or "").lower()
    # Decode HTML entities (e.g., &amp; -> &)
    s = html.unescape(s)
    # Remove HTML tags (e.g., <br />, <p>)
    s = re.sub(r"<[^>]+>", " ", s)
    # keep alphanumerics and spaces; strip punctuation; flatten whitespace
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def tokenize(s: str) -> List[str]:
    return s.split()

def remove_stopwords(tokens: List[str], stopwords=DEFAULT_STOPWORDS) -> List[str]:
    return [t for t in tokens if t not in stopwords and len(t) > 1]

def word_frequencies(tokens: List[str]) -> Counter:
    return Counter(tokens)

def summary_stats(tokens: List[str]) -> Dict[str, float]:
    if not tokens:
        return {"num_tokens": 0, "vocab_size": 0, "avg_word_len": 0.0, "type_token_ratio": 0.0}
    vocab = set(tokens)
    avg_len = sum(len(t) for t in tokens) / len(tokens)
    return {
        "num_tokens": len(tokens),
        "vocab_size": len(vocab),
        "avg_word_len": round(avg_len, 3),
        "type_token_ratio": round(len(vocab)/len(tokens), 4)
    }

def ascii_bar_chart(items: List[Tuple[str, int]], width: int = 48) -> str:
    if not items:
        return "(no data)"
    maxv = max(c for _, c in items)
    maxlab = max(len(w) for w, _ in items)
    lines = []
    for w, c in items:
        bar = "#" * int(width * (c / maxv)) if maxv else ""
        lines.append(f"{w.rjust(maxlab)} | {bar} {c}")
    return "\n".join(lines)

