"""
Part 2 Analyzing Your Text with Optional NLP + AI Summary
Author: Sophia Pak
"""

import re
import pickle
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize

# Importing transformers; fallback if unavailable
try:
    from transformers import pipeline
    HAS_TRANSFORMERS = True
except ImportError:
    HAS_TRANSFORMERS = False
    print("'transformers' not found. Using lightweight built-in summarizer instead.")

# NLTK setup
nltk.download('stopwords')
nltk.download('vader_lexicon')
nltk.download('punkt')


# 1. Text Cleaning and Preprocessing
def clean_text(text: str) -> str:
    """Clean and preprocess text."""
    start = re.search(r'\*\*\* START OF .* \*\*\*', text)
    end = re.search(r'\*\*\* END OF .* \*\*\*', text)
    if start and end:
        text = text[start.end():end.start()]
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


# 2. Removing Stop Words
def remove_stopwords(text: str) -> list:
    stop_words = set(stopwords.words('english'))
    words = text.split()
    return [word for word in words if word not in stop_words]


# 3. Word Frequency Analysis
def get_word_frequencies(words: list) -> Counter:
    return Counter(words)


# 4. Summary Statistics
def summary_statistics(words: list, word_freq: Counter):
    total_words = len(words)
    unique_words = len(set(words))
    avg_word_length = sum(len(word) for word in words) / total_words
    top_20_words = word_freq.most_common(20)

    print(f"\nText Summary Statistics:")
    print(f"Total words: {total_words}")
    print(f"Unique words: {unique_words}")
    print(f"Average word length: {avg_word_length:.2f}")
    print("\nTop 20 most frequent words:")
    for word, freq in top_20_words:
        print(f"{word}: {freq}")
    return top_20_words


# 5. Text-Based Bar Chart
def visualize_bar_chart(top_words: list, scale: int = 2):
    print("\nWord Frequency Chart:")
    for word, freq in top_words:
        bar = "#" * (freq // scale)
        print(f"{word.ljust(15)} | {bar} ({freq})")


# 6. Sentiment Analysis
def analyze_sentiment(text: str, preview_sentences: int = 5, max_words: int = 20):
    sentences = sent_tokenize(text)
    sia = SentimentIntensityAnalyzer()
    compound_scores = [sia.polarity_scores(s)['compound'] for s in sentences]
    overall_score = sum(compound_scores) / len(compound_scores)

    print("\nExample sentence sentiment scores:")
    for s in sentences[:preview_sentences]:
        snippet = " ".join(s.split()[:max_words])
        print(f"→ {snippet}...")
        print(f"   Sentiment: {sia.polarity_scores(s)}\n")

    print(f"Overall compound sentiment score: {overall_score:.3f}")
    return overall_score


# 7. AI Text Summarization (with fallback)
def ai_summary(text: str, max_words: int = 300):
    print("\nGenerating AI summary...")

    if HAS_TRANSFORMERS:
        summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

        words = text.split()
        chunk_size = 900  # safe margin below token limit
        chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

        summaries = []
        for i, chunk in enumerate(chunks[:5]):
            print(f"  Summarizing chunk {i + 1}/{min(len(chunks),5)}...")
            try:
                summary = summarizer(chunk, max_length=150, min_length=50, do_sample=False)
                summaries.append(summary[0]['summary_text'])
            except Exception as e:
                print(f"Skipping chunk {i+1}: {e}")

        combined_summary = " ".join(summaries)
        print("\nAI-Generated Summary:\n")
        print(combined_summary)
        print("-" * 80)
        return combined_summary

    else:
        sentences = re.split(r'(?<=[.!?]) +', text)
        words = re.findall(r'\w+', text.lower())
        freq = Counter(words)
        scores = {s: sum(freq[w] for w in re.findall(r'\w+', s.lower())) for s in sentences}
        top = sorted(scores, key=scores.get, reverse=True)[:5]

        print("\nKeyword-Based Summary (no transformers):\n")
        for s in top:
            print("-", s.strip())
        print("-" * 80)
        return " ".join(top)


# 8. Main Analysis Workflow
def main_analysis(filename="a_perfect_gentleman.pkl"):
    with open(filename, "rb") as f:
        text = pickle.load(f)

    clean = clean_text(text)
    words_filtered = remove_stopwords(clean)
    word_freq = get_word_frequencies(words_filtered)
    top_words = summary_statistics(words_filtered, word_freq)
    visualize_bar_chart(top_words)
    analyze_sentiment(clean, preview_sentences=5, max_words=20)
    ai_summary(clean)


if __name__ == "__main__":
    main_analysis()
