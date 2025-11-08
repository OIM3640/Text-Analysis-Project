import urllib.request, urllib.error, re, os, sys, json
from collections import Counter
from typing import List, Tuple, Dict

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('vader_lexicon')

STOPWORDS = {
    "a","an","the","and","or","but","if","then","else","when","while","of","to","in","on","for","from","by",
    "with","as","at","is","are","was","were","be","been","being","that","this","it","its","they","them","their",
    "she","her","he","his","you","your","i","we","us","our","not","no","do","does","did","so","such","than","too",
    "very","can","could","should","would","may","might","will","just","my","me","him","her","his","hers","ours","theirs","our","your","yours",
    "which","who","whom","whose","what","this","that","these","those","am","is","are","was","were","be","been","being","have","has","had","do","does","did"
}

def fetch_text(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "TextAnalysisProject/1.0"})
    with urllib.request.urlopen(req, timeout=40) as f:
        return f.read().decode("utf-8", errors="ignore")

def strip_gutenberg(text: str) -> str:
    lines = text.splitlines()
    start, end = 0, len(lines)
    for i, line in enumerate(lines):
        if "start of the project gutenberg" in line.lower():
            start = i + 1
            break
    for j in range(len(lines)-1, -1, -1):
        if "end of the project gutenberg" in lines[j].lower():
            end = j
            break
    return "\n".join(lines[start:end])

def clean_text(text: str) -> str:
    text = re.sub(r"\[[^\]]*\]", " ", text)
    text = re.sub(r"[^A-Za-z\s'\-]", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = text.lower().strip()
    text = re.sub(r"\b[a-zA-Z]\b", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenize(text: str) -> List[str]:
    return [t for t in re.split(r"\s+", text) if t]

def remove_stopwords(tokens: List[str]) -> List[str]:
    return [t for t in tokens if t not in STOPWORDS]

def word_frequencies(tokens: List[str]) -> Counter:
    return Counter(tokens)

def ascii_bar_chart(pairs: List[Tuple[str, int]], width: int = 50) -> str:
    maxcount = max(c for _, c in pairs) or 1
    return "\n".join(f"{w:>15} | {'#' * int((c / maxcount) * width)} {c}" for w, c in pairs)

def summary_stats(tokens: List[str]) -> Dict[str, float]:
    if not tokens:
        return {"num_tokens": 0, "vocab_size": 0, "avg_word_len": 0.0}
    lengths = [len(t) for t in tokens]
    return {
        "num_tokens": len(tokens),
        "vocab_size": len(set(tokens)),
        "avg_word_len": sum(lengths) / len(lengths),
    }

def sentiment_sample(text: str, take: int = 10):
    sia = SentimentIntensityAnalyzer()
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [(s.strip(), sia.polarity_scores(s.strip())["compound"]) for s in sentences[:take] if s.strip()]

def tfidf_similarity(text1: str, text2: str) -> float:
    vec = TfidfVectorizer(
        stop_words='english',
        token_pattern=r'(?u)\b[a-zA-Z]{2,}\b',  # ignore 1-letter tokens
        min_df=1,                               
        max_df=1.0                               # allow terms that appear in both documents
    )
    X = vec.fit_transform([text1, text2])
    S = cosine_similarity(X)
    return float(S[0, 1])

def main():
    url = "https://www.gutenberg.org/cache/epub/11/pg11.txt"  # Alice in Wonderland
    compare_url = "https://www.gutenberg.org/cache/epub/84/pg84.txt"  # Frankenstein

    raw = fetch_text(url)
    text = clean_text(strip_gutenberg(raw))
    tokens = remove_stopwords(tokenize(text))
    freqs = word_frequencies(tokens)
    top_words = freqs.most_common(20)
    stats = summary_stats(tokens)

    print("\n=== Top Words ===")
    print(ascii_bar_chart(top_words))
    print("\n=== Summary Stats ===")
    for k, v in stats.items():
        print(f"{k}: {v}")

    comp_text = clean_text(strip_gutenberg(fetch_text(compare_url)))
    comp_tokens = remove_stopwords(tokenize(comp_text))
    comp_freqs = word_frequencies(comp_tokens)
    comp_top = comp_freqs.most_common(20)

    print("\n=== Top Words (Comparison Book) ===")
    print(ascii_bar_chart(comp_top))

    similarity = tfidf_similarity(text, comp_text)
    print(f"\nCosine Similarity with comparison text: {similarity:.3f}")

    sentiment = sentiment_sample(text)

    os.makedirs("data", exist_ok=True)
    with open("data/top_words.txt", "w", encoding="utf-8") as f:
        f.write(ascii_bar_chart(top_words))
    with open("data/summary.json", "w", encoding="utf-8") as f:
        json.dump({"top_words": top_words, "stats": stats, "similarity": similarity, "sentiment": sentiment}, f, indent=2)

if __name__ == "__main__":
    main()


# AI Useage : 
# I used chatGPT to help me structure the functions for text cleaning, and frequency analysis. 
# I provided prompts describing the desired functionality, and ChatGPT generated code snippets which I then reviewed, tested, and modified as needed to fit the overall program. 
# I also used ChatGPT to help debug some syntax errors and optimize certain parts of the code. However, I ensured that I understood all the code and made final decisions on implementing the code.