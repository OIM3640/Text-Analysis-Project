### This is a version of using ChatGPT to check any error and help organize all the files into a more concise and organized one.

from mediawiki import MediaWiki
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from thefuzz import fuzz
import nltk
import re

# Ensure required NLTK resources are downloaded
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')

# Initialize tools
wikipedia = MediaWiki()
stop_words = set(stopwords.words('english'))
sia = SentimentIntensityAnalyzer()

# Fetch and clean text from Wikipedia
def fetch_and_clean_text(title):
    page = wikipedia.page(title)
    text = re.sub(r'\[.*?\]|\n+', ' ', page.content)  # Remove citations and newlines
    return text.lower().strip()

# Compute word frequencies excluding stop words
def word_frequency(text):
    words = [word.strip('.,!?"()') for word in text.split() if word.isalnum() and word not in stop_words]
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

# Summary statistics for word frequencies
def compute_summary(frequency):
    total_words = sum(frequency.values())
    unique_words = len(frequency)
    top_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:10]
    return {"total_words": total_words, "unique_words": unique_words, "top_words": top_words}

# Find words frequent in one text but not in another
def unique_frequent_words(frequency1, frequency2, threshold=5):
    return {word: count for word, count in frequency1.items() if count >= threshold and frequency2.get(word, 0) < threshold}

# Sentiment analysis
def analyze_sentiment(text):
    return sia.polarity_scores(text)

# Compute text similarity using TheFuzz
def compute_text_similarity(text1, text2):
    return {
        "fuzz_ratio": fuzz.ratio(text1, text2),
        "partial_ratio": fuzz.partial_ratio(text1, text2),
        "token_sort_ratio": fuzz.token_sort_ratio(text1, text2)
    }

# Main execution
def main():
    # Fetch and clean text
    babson_text = fetch_and_clean_text("Babson College")
    entrepreneurship_text = fetch_and_clean_text("Entrepreneurship")

    # Word frequency and summary
    babson_frequency = word_frequency(babson_text)
    entrepreneurship_frequency = word_frequency(entrepreneurship_text)
    print("Summary for 'Babson College':", compute_summary(babson_frequency))
    print("Summary for 'Entrepreneurship':", compute_summary(entrepreneurship_frequency))

    # Specific words' frequencies
    target_words = ["entrepreneurship", "entrepreneur", "entrepreneurial"]
    specific_frequencies = {word: babson_frequency.get(word, 0) for word in target_words}
    print("\nFrequencies of Specific Words in 'Babson College':", specific_frequencies)

    # Unique frequent words
    unique_words = unique_frequent_words(babson_frequency, entrepreneurship_frequency)
    print("\nWords Frequent in 'Babson College' but Not in 'Entrepreneurship':", unique_words)

    # Sentiment analysis
    print("\nSentiment Analysis for 'Babson College':", analyze_sentiment(babson_text))
    print("Sentiment Analysis for 'Entrepreneurship':", analyze_sentiment(entrepreneurship_text))

    # Text similarity
    print("\nSimilarity between 'Babson College' and 'Entrepreneurship':", compute_text_similarity(babson_text, entrepreneurship_text))

if __name__ == "__main__":
    main()
