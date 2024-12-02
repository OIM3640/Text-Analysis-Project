from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from thefuzz import fuzz
import nltk

nltk.download("stopwords")

stop_words = set(stopwords.words("english"))


def word_frequency(text):
    """Compute word frequency, filtering out stop words."""
    words = text.lower().split()
    frequency = {}
    for word in words:
        word = word.strip('.,!?"()')
        if word.isalnum() and word not in stop_words:
            frequency[word] = frequency.get(word, 0) + 1
    return frequency


def find_specific_word_frequencies(frequency, target_words):
    """Find the frequency of specific words in the frequency dictionary."""
    specific_frequencies = {word: frequency.get(word, 0) for word in target_words}
    return specific_frequencies


def summary_statistics(frequency):
    """Compute summary statistics from word frequencies."""
    total_words = sum(frequency.values())
    unique_words = len(frequency)
    top_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:10]
    return {
        "total_words": total_words,
        "unique_words": unique_words,
        "top_words": top_words
    }


def unique_frequent_words(frequency1, frequency2, threshold=5):
    """Identify words that appear frequently in one text but not in another.
    """
    unique_words = {}
    for word, count in frequency1.items():
        if count >= threshold and frequency2.get(word, 0) < threshold:
            unique_words[word] = count
    return unique_words


def analyze_sentiment(text):
    """Perform sentiment analysis using NLTK's VADER."""
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)


def compute_text_similarity(text1, text2):
    """Compute similarity between two texts using TheFuzz."""
    return {
        "fuzz_ratio": fuzz.ratio(text1, text2),
        "partial_ratio": fuzz.partial_ratio(text1, text2),
        "token_sort_ratio": fuzz.token_sort_ratio(text1, text2),
    }
