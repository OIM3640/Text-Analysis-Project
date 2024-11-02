from text import fetch_text
from frequency import calculate_word_frequencies
from statistics import print_gatsby_count, print_top_words

"""
This will fetch the text of "The Great Gatsby" and count the frequency of each word, print the number of times "Gatsby" appears,
and display the top 10 most common words.
"""


def main():
    url = "https://www.gutenberg.org/cache/epub/64317/pg64317.txt"
    text = fetch_text(url)

    word_counts, gatsby_count = calculate_word_frequencies(text)

    print_gatsby_count(gatsby_count)  # Print how many "gatsbys"
    print_top_words(word_counts)  # Print the 10 most common words and their frequency


if __name__ == "__main__":
    main()
