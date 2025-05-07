from data_collection import fetch_wikipedia_content, clean_text
from text_analysis import (
    word_frequency,
    summary_statistics,
    analyze_sentiment,
    compute_text_similarity,
    find_specific_word_frequencies,
    unique_frequent_words,
)


def main():
    # Fetch and Clean Wikipedia Articles
    babson_text = fetch_wikipedia_content("Babson College")
    babson_text = clean_text(babson_text)

    related_text = fetch_wikipedia_content("Entrepreneurship")
    related_text = clean_text(related_text)

    # Compute Word Frequency
    babson_frequency = word_frequency(babson_text)
    top_words = sorted(babson_frequency.items(), key=lambda x: x[1], reverse=True)[:10]
    print("Top 10 Words in 'Babson College':", top_words)

    related_frequency = word_frequency(related_text)
    top_words = sorted(related_frequency.items(), key=lambda x: x[1], reverse=True)[:10]
    print("Top 10 Words in 'Entrepreneurship':", top_words)

    target_words = ["entrepreneurship", "entrepreneur", "entrepreneurial"]
    specific_frequencies = find_specific_word_frequencies(
        babson_frequency, target_words
    )
    print("\nFrequencies of Specific Words in 'Babson College':", specific_frequencies)

    # Summary Statistics
    babson_summary = summary_statistics(babson_frequency)
    related_summary = summary_statistics(related_frequency)

    print("\nSummary Statistics for 'Babson College':", babson_summary)
    print("Summary Statistics for 'Entrepreneurship':", related_summary)

    unique_words = unique_frequent_words(babson_frequency, related_frequency)
    print(
        "\nWords Frequent in 'Babson College' but Not in 'Entrepreneurship':",
        unique_words,
    )

    # Sentiment Analysis
    babson_sentiment = analyze_sentiment(babson_text)
    related_sentiment = analyze_sentiment(related_text)
    print("\nSentiment Analysis for 'Babson College':", babson_sentiment)
    print("Sentiment Analysis for 'Entrepreneurship':", related_sentiment)

    # Text Similarity
    similarity_scores = compute_text_similarity(babson_text, related_text)
    print(
        "\nSimilarity between 'Babson College' and 'Entrepreneurship':",
        similarity_scores,
    )


if __name__ == "__main__":
    main()
