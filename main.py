# These functions are the ones we defined in analyzer.py
from analyze import get_words, remove_stopwords, count_words, analyze_sentiment
from harvest_text import harvest_gutenberg_text

def main():
    # This is the Project Gutenberg link to Oliver Twist by Charles Dickens
    url = "https://www.gutenberg.org/cache/epub/730/pg730.txt"
    print("Downloading text from Project Gutenberg...")

    # Fetch the book text from the web
    raw_text = harvest_gutenberg_text(url)

    # Break the text into a list of words (all lowercase, no punctuation)
    words = get_words(raw_text)

    # Remove common words like "the", "and", "is", etc.
    filtered_words = remove_stopwords(words)

    # Count how often each word appears
    word_counts = count_words(filtered_words)

    # Print the 10 most common words and their counts
    print("\nTop 10 words (after removing stopwords):")
    for word, count in word_counts.most_common(10):
        print(f"{word}: {count}")

    # Use sentiment analysis to see if the overall tone is positive/negative/neutral
    print("\nRunning sentiment analysis...")
    sentiment_scores = analyze_sentiment(raw_text)
    print("Sentiment scores:")
    for category, score in sentiment_scores.items():
        print(f"{category}: {score}")

if __name__ == "__main__":
    main()
