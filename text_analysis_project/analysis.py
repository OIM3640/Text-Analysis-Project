import sys
from unicodedata import category


def process_page(text):
    """
    updated function to take text instead of file (from analyze_book.py)
    so we can find the top 10 most common words used in both the "Real Madrid CF" and "FC Barcelona" page
    """
    hist = {}

    # strippables = string.punctuation + string.whitespace
    strippables = "".join(
        chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")
    )  # Unicode punctuation characters. Ref: https://stackoverflow.com/a/60983895

    text = text.replace("-", " ")
    text = text.replace(chr(8212), " ")  # Em dash replacement

    for word in text.split():
        word = word.strip(strippables)
        word = word.lower()

        hist[word] = hist.get(word, 0) + 1

    return hist


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)


def most_common(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    freq_word_tuples = []  # a list of tuples ((freq, word))
    for word, freq in hist.items():
        freq_word_tuples.append((freq, word))

    freq_word_tuples.sort(reverse=True)
    return freq_word_tuples


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.

    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    common_words = most_common(hist)
    for freq, word in common_words[:num]:
        print(f"{word} : {freq}")
