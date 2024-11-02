def print_gatsby_count(count):
    """
    Prints the # of times "gatsby" appeaars in the text.
    """
    print(f"The word 'gatsby' appears {count} times in the text.")


def print_top_words(word_counts, top=10):
    """
    Print the top most common words and their frequencies.
    """

    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)  # Sorts the word counts by frequencies
    print(f"Top {top} words and their frequencies:")
    for word, freq in sorted_word_counts[:top]:  # Loop through top words
        print(f"{word} : {freq}")
