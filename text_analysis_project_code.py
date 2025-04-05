import urllib.request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk


def download_text(url):
    """Download text from a URL and return it as a string."""
    with urllib.request.urlopen(url) as f:
        text = f.read().decode("utf-8")
    return text


def clean_text(text):
    """Clean the text by removing unnecessary parts."""
    start_markers = ["*** START OF THE PROJECT GUTENBERG EBOOK THE SCARLET LETTER ***"]
    end_markers = ["*** END OF THE PROJECT GUTENBERG EBOOK THE SCARLET LETTER ***"]
    start_position = len(text)
    for marker in start_markers:
        position = text.find(marker)
        if position != -1:
            end_of_line = text.find("\n", position)
        if end_of_line != -1 and end_of_line < start_position:
            start_position = end_of_line

    end_position = 0
    for marker in end_markers:
        position = text.find(marker)
        if position != -1 and position > end_position:
            end_position = position

    if start_position < len(text) and end_position > 0:
        cleaned_text = text[start_position:end_position].strip()
    else:
        cleaned_text = text

    return cleaned_text


def word_frequency(cleaned_text):
    """Calculates the frequency of each word in the story"""
    words = cleaned_text.lower().split()
    punctuation = ",!?[].{}:();'-"
    clean_words = []
    for word in words:
        for char in punctuation:
            word = word.replace(char, "")
        if word:
            clean_words.append(word)

    word_freq = {}
    for word in clean_words:
        if word:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
    return word_freq


def sort_by_frequency_decending(word_freq):
    """Sorts the word frequency dictionary in descending order"""
    sorted_word_freq = dict(
        sorted(word_freq.items(), key=lambda item: item[1], reverse=True)
    )

    return sorted_word_freq


def create_summary_statistics(sorted_word_freq):
    """Generates summary statistics for the word frequency"""
    total_words = sum(sorted_word_freq.values())
    unique_words = len(sorted_word_freq)
    average_frequency = total_words / unique_words if unique_words > 0 else 0
    word_items = list(sorted_word_freq.items())
    most_common_word = word_items[0:4] if word_items else None
    least_common_word = word_items[-1] if word_items else None

    statistics = {
        "total_words": total_words,
        "unique_words": unique_words,
        "average_frequency": average_frequency,
        "most_common_words": most_common_word,
        "least_common_word": least_common_word,
    }

    return statistics


def remove_stop_words(sorted_word_freq):
    """Removes common stop words from the word frequency dictionary"""
    stop_words = set(
        [
            "i",
            "me",
            "my",
            "a",
            "an",
            "the",
            "and",
            "is",
            "to",
            "in",
            "that",
            "of",
            "for",
            "on",
            "with",
            "as",
            "by",
            "at",
            "this",
            "it",
            "are",
            "was",
            "were",
            "be",
            "been",
            "he",
            "she",
            "they",
            "them",
            "we",
            "us",
            "you",
            "her",
            "him",
            "his",
            "had",
            "which",
            "not",
            
        ]
    )
    filtered_word_freq = {
        word: freq for word, freq in sorted_word_freq.items() if word not in stop_words
    }
    return filtered_word_freq


def sentiment_analysis(text):
    """Perform a sentiment analysis using vader"""
    try:
        nltk.data.find("sentiment/vader_lexicon.zip")
    except LookupError:
        nltk.download("vader_lexicon")

    vader_analyzer = SentimentIntensityAnalyzer()
    vader_scores = vader_analyzer.polarity_scores(text)

    return vader_scores


def analysis_of_the_text(text):
    """This function prints out all of the analysis form above"""
    cleaned_text = clean_text(text)
    word_freq = word_frequency(cleaned_text)
    sorted_decending = sort_by_frequency_decending(word_freq)
    statistics = create_summary_statistics(sorted_decending)

    print("Word Frequency analysis - Entire Text: ")
    print(f"Total Words: {statistics['total_words']}")
    print(f"Unique Words: {statistics['unique_words']}")
    print(f"Average Word Frequency: {statistics['average_frequency']} ")
    print(f"5 Most Common Words: {statistics['most_common_words']}")

    word_freq_filtered = remove_stop_words(sorted_decending)
    statistics_with_filter = create_summary_statistics(word_freq_filtered)

    print("Word Frequency analysis - Removing Stop Words:")
    print(f"Total Words: {statistics_with_filter['total_words']}")
    print(f"Unique Words: {statistics_with_filter['unique_words']}")
    print(f"Average Word Frequency: {statistics_with_filter['average_frequency']} ")
    print(f" 5 Most Common Words: {statistics_with_filter['most_common_words']}")

    sentiment_scores = sentiment_analysis(cleaned_text)
    print("Sentiment Score using VADER:")
    print(sentiment_scores)


def main():
    url = "https://www.gutenberg.org/cache/epub/25344/pg25344.txt"
    try:
        text = download_text(url)
        analysis_of_the_text(text)
    except Exception as e:
        print(
            "Error: Make sure you have the required packages installed (pip install nltk textblob) and make sure your URL is correct"
        )


if __name__ == "__main__":
    main()

main()
