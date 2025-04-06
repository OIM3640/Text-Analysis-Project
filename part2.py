import random
import string
import sys
from unicodedata import category



def process_file(filename, skip_header):
    """Makes a histogram that counts the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding="utf-8")

    if skip_header:
        skip_gutenberg_header(fp)

    # strippables = string.punctuation + string.whitespace
    strippables = "".join(
        chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")
    )  # Unicode punctuation characters. Ref: https://stackoverflow.com/a/60983895

    for line in fp:
        if line.startswith("*** END OF THE PROJECT"):
            break

        line = line.replace("-", " ")
        line = line.replace(chr(8212), " ")  # Em dash replacement

        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()

            hist[word] = hist.get(word, 0) + 1

    fp.close()
    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    start_marker = "START OF THE PROJECT"

    for line in fp:
        if start_marker.lower() in line.lower():  # Case-insensitive search
            return
    # If the loop completes without finding the start marker
    raise ValueError(f"Header end marker '{start_marker}' not found in file.")


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
    stopwords = set()
    if excluding_stopwords:
        stopwords = {
            "a",
            "and",
            "at", "as",
            "be",
            "but",
            "by",
            "for",
            "had",
            "he",
            "her",
            "his",
            "i",
            "in",
            "is", 
            "it",
            "so",
            "that",
            "the",
            "them",
            "to",
            "with",
            "which",
        }
    # i searched up some stop words
    t = []
    for word, freq in hist.items():
        if excluding_stopwords and word in stopwords:
            continue
        t.append((freq, word))

    t.sort(reverse=True)
    return t


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.

    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    common = most_common(hist)
    for freq, word in common[:num]:
        print(word, "\t", freq)


def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.

    d1, d2: dictionaries
    """
    result = {}
    for key in d1:
        if key not in d2:
            result[key] = d1[key]
    return result


def random_word(hist):
    """Chooses a random word from a histogram.

    The probability of each word is proportional to its frequency.
    """
    words = []
    for word, freq in hist.items():
        words.extend([word] * freq)
    return random.choice(words)


def main():
    # This text file is downloaded from gutenberg.org (https://www.gutenberg.org/cache/epub/1342/pg1342.txt)
    hist = process_file("Parts/East of Eden.txt", skip_header=True)
    words = process_file("Parts/words.txt", skip_header=False)  # Ensure correct filename and path

    print(hist)
    print(f"Total number of words: {total_words(hist)}")
    print(f"Number of different words: {different_words(hist)}")

    t = most_common(hist, excluding_stopwords=True)
    print("The most common words are:")
    for freq, word in t[0:20]:
        print(word, "\t", freq)

    diff = subtract(hist, words)
    print("The words in the book that aren't in the word list are:")
    for word in diff.keys():
        print(word, end=" ")

    print("\n\nHere are some random words from the book")
    for i in range(100):
        print(random_word(hist), end=" ")


if __name__ == "__main__":
    main()


# Putting them on a list to pickle
def main():
    book_files = [
        "Parts/East of Eden.txt",
        "Parts/The Great Gatsby.txt"
    ]

    histograms = []
    for book in book_files:
        hist = process_file(book, skip_header=True)
        histograms.append(hist)
        print(f"Processed '{book}':")
        print(f"  Total words: {total_words(hist)}")
        print(f"  Unique words: {different_words(hist)}\n")

    # Example: most common words in each book
    for i, hist in enumerate(histograms):
        print(f"Most common words in Book {i+1}:")
        top_words = most_common(hist, excluding_stopwords=True)
        for freq, word in top_words[:10]:
            print(f"{word}\t{freq}")
        print("\n")

# Pickle
import pickle

# Assuming you already read the texts from files
with open('Parts/East of Eden.txt', 'r', encoding='utf-8') as f1:
    east_of_eden_text = f1.read()

with open('Parts/The Great Gatsby.txt', 'r', encoding='utf-8') as f2:
    great_gatsby_text = f2.read()

# Combine both into a dictionary
books = {
    "East of Eden": east_of_eden_text,
    "The Great Gatsby": great_gatsby_text
}

# Save data to a pickle file
with open('books_texts.pkl', 'wb') as f:
    pickle.dump(books, f)

# Load data from the pickle file later
with open('books_texts.pkl', 'rb') as f:
    reloaded_books = pickle.load(f)
