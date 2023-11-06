import remove_stop_words as rsw

def most_common_words():
    """This counts the amount of times a specific word appears in the chosen text."""
    # Splits text into words by whitespace and punctuation
    # Given from https://www.w3schools.com/python/ref_string_split.asp
    words = text.split()
    # Dictionary for storage
    word_count = {}
    nonzero = False
    for word in words:
        # Converts the word to all lowercase to account for proper nouns and sentence capitalizations
        # I realize that remove_preamble already turns all words lowercase, but I added it again to work regardless of the input string. IE: we decide to run the original text with the preamble
        word = part1.only_alpha(word)
        word = word.lower()
        # Remove any non-alphabetic characters from the word
        # Given from https://stackoverflow.com/questions/22520932/python-remove-all-non-alphabet-chars-from-string
        word = "".join(filter(str.isalpha, word))
        # Update the word count dictionary if 'word' is the desired word
        if word == target:
            word_count[word] = word_count.get(word, 0) + 1
            nonzero = True