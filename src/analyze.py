# src/analyze.py
from collections import Counter
from typing import Dict, List, Tuple

def word_frequencies(tokens: List[str]) -> Counter:
    return Counter(tokens)

def top_n(freqs: Counter, n: int = 20) -> List[Tuple[str, int]]:
    return freqs.most_common(n)

def summary_stats(raw_text: str, tokens: List[str]) -> Dict[str, float]:
    total_chars = len(raw_text)
    total_words = len(tokens)
    unique_words = len(set(tokens))
    avg_word_len = sum(len(t) for t in tokens) / total_words if total_words else 0
    # sentence-level stats: do outside (we’ll pass counts in main)
    return {
        "total_chars": total_chars,
        "total_words": total_words,
        "unique_words": unique_words,
        "avg_word_len": round(avg_word_len, 3),
        "type_token_ratio": round(unique_words / total_words, 4) if total_words else 0,
    }
