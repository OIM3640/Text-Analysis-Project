import os
import nltk

nltk.download("vader_lexicon")
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# Define a function to process a text file and generate a word frequency histogram
def process_text_file(filename):
    hist = {}
    with open(filename, encoding="UTF8") as fp:
        for line in fp:
            for word in line.split():
                word = word.lower()
                # add counter if word appears
                hist[word] = hist.get(word, 0) + 1
    return hist


def most_common(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    # sort the words by frequency in descending order
    sort_words = sorted(hist.items(), key=lambda item: item[1], reverse=True)
    if excluding_stopwords:
        stopwords = set(
            [
                "a",
                "an",
                "the",
                "and",
                "it",
                "for",
                "or",
                "but",
                "in",
                "my",
                "your",
                "our",
                "their",
                "of",
                "by",
                "in",
                "with",
                "is",
            ]
        )
        sort_words = [
            (frequency, word) for frequency, word in sort_words if word not in stopwords
        ]
    return sort_words


# Define a function to print the most common words in a histogram
def print_most_common(hist, num = 10):
    common_words = most_common(hist)
    count = 1
    for frequency, word in common_words[:num]:
        print(f"{count}. {word}: {frequency}")
        count += 1


# Define a function to compare word frequencies between two histograms
def compare_word_frequencies(hist1, hist2):
    # Calculate the set of common words in both histograms
    common_words = set(hist1.keys()) & set(hist2.keys())

    # Calculate the differences in word frequencies for common words
    word_diff = {word: hist1[word] - hist2[word] for word in common_words}

    return word_diff


# Define the main analysis function
def main():
    # List of text files to process
    text_files = [
        "data/Fortune.txt",
        "data/Inside_highered.txt",
        "data/Higher_education.txt",
        "data/List_of_US_Grad.txt",
    ]

    # Process each text file and store the word frequency histograms
    histograms = {}
    for filename in text_files:
        base_filename = os.path.basename(filename)
        histograms[base_filename] = process_text_file(filename)

    # Print the most common words in each text file
    for filename, hist in histograms.items():
        print(f"Word frequency analysis for {filename}:")
        print_most_common(hist, num=10)
        print()

    # Compare word frequencies between text files
    for filename1, hist1 in histograms.items():
        for filename2, hist2 in histograms.items():
            if filename1 != filename2:
                print(f"Comparing {filename1} and {filename2}:")
                word_diff = compare_word_frequencies(hist1, hist2)
                print(f"Common words with frequency differences:")
                for word, diff in word_diff.items():
                    print(f"{word}: {diff}")
                print()


if __name__ == "__main__":
    main()

# analyzes the sentiment of the four texts"
def analyze_sentiment(texts):
    # Initialize the sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()

    sentiment_results = []

    for text in texts:
        # Get sentiment scores for the text
        sentiment_scores = analyzer.polarity_scores(text)

        # Interpret the sentiment based on the compound score
        compound_score = sentiment_scores["compound"]
        if compound_score >= 0.05:
            sentiment = "Positive"
        elif compound_score <= -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        sentiment_results.append(
            {"text": text, "sentiment_scores": sentiment_scores, "sentiment": sentiment}
        )

    return sentiment_results


# List of texts
texts = [
    "data/Fortune.txt",
    "data/Inside_highered.txt",
    "data/Higher_education.txt",
    "data/List_of_US_Grad.txt",
]

# Analyze sentiment for all texts
results = analyze_sentiment(texts)

# Print sentiment analysis results
for i, result in enumerate(results, 1):
    print(f"Text {i} - Sentiment: {result['sentiment']}")
    print(f"Sentiment Scores: {result['sentiment_scores']}")
    print("-" * 50)

