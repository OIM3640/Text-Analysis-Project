import string

def calculate_word_frequencies(text):
    """
    This counts the frequency of each word in the text and returns
    a dictionary.
    """
    words = text.lower().split() # Converts the text into lowercase and splits it into individual words

    word_counts = {}  # Dictionary to store the frequency of each word
    gatsby_count = 0  # This counts the number of times the word "Gatsby" is used

    for word in words:
        word = word.strip(string.punctuation)
        if word == "gatsby":  # Check if the word is "gatsby"
            gatsby_count += 1  # Increment the count for "gatsby"
        word_counts[word] = (word_counts.get(word, 0) + 1)  # This updates the word frequency count in the dictionary
    return word_counts, gatsby_count
