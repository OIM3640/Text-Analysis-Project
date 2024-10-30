### PART 1: importing data sources - 2 most popular jane austen texts
import urllib.request
import math
from collections import Counter
from unicodedata import category
import sys

url1 = 'https://www.gutenberg.org/cache/epub/1342/pg1342.txt' #pride and prejudice
url2 = 'https://www.gutenberg.org/cache/epub/158/pg158.txt' #emma

with urllib.request.urlopen(url1) as f:
    pride_and_prejudice_text = f.read().decode('utf-8')
    # print(text) # for testing
with urllib.request.urlopen(url2) as f:
    emma_text = f.read().decode('utf-8')
    # print(text) # for testing

# Defines a set of words that we will use as "stop words" 
STOP_WORDS = {
    "the", "and", "a", "an", "in", "on", "at", "to", "of", "for", "with", "that", "this",
    "is", "it", "as", "by", "from", "or", "not", "be", "are", "was", "were", "he", "she",
    "they", "we", "you", "i", "his", "her", "their", "our", "my", "me", "him", "them", "do",
    "does", "did", "so", "if", "but", "about", "which", "there", "then", "out", "up", "down",
    "more", "such", "into", "no", "than", "too", "very", "can", "will", "just", "now", "over",
    "again", "only", "after", "before", "when", "where", "how", "why"
}

# processes text to remove irrelevant headers by using code from in class exercise form session 15 - adapted to accept text a opposed to file from data folder 

def process_text(text, skip_header, excluding_stopwords=False):
    """Makes a histogram that counts the words from a file.

    text: string, the text content to process
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    hist = {}
    lines = text.splitlines()

    if skip_header:
        lines = skip_gutenberg_header(lines)

    # strippables = string.punctuation + string.whitespace
    strippables = "".join(
        chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")
    )  # Unicode punctuation characters. Ref: https://stackoverflow.com/a/60983895

    for line in lines:
        if line.startswith("*** END OF THE PROJECT"):
            break

        line = line.replace("-", " ")
        line = line.replace(chr(8212), " ")  # Em dash replacement

        for word in line.split():
            word = word.strip(strippables).lower()

            if word and (not excluding_stopwords or word not in STOP_WORDS):
                hist[word] = hist.get(word, 0) + 1

    return hist


def skip_gutenberg_header(lines):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    start_marker = "START OF THE PROJECT"

    for index, line in enumerate(lines):
        if start_marker.lower() in line.lower():
            return lines[index + 1:]  # return lines after the header
    raise ValueError(f"Header end marker '{start_marker}' not found in text.")

def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


### characterizing by word frequencies - done under main fucntion

### shows top 20 most frequent words
def most_common(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    freq_word_tuples = []
    for word, freq in hist.items():
        if not excluding_stopwords or word not in STOP_WORDS:
            freq_word_tuples.append((freq, word))

    freq_word_tuples.sort(reverse=True)
    return freq_word_tuples

# Cosine Similarity Calculation  to calaculate similarity between the texts - used AI to generate 
def cosine_similarity(hist1, hist2):
    """Compute cosine similarity between two word frequency dictionaries."""
    all_words = set(hist1.keys()).union(set(hist2.keys()))
    
    # Calculate dot product and magnitudes
    dot_product = sum(hist1.get(word, 0) * hist2.get(word, 0) for word in all_words)
    mag1 = math.sqrt(sum(count ** 2 for count in hist1.values()))
    mag2 = math.sqrt(sum(count ** 2 for count in hist2.values()))

    # Handle division by zero in case of empty vectors
    if mag1 == 0 or mag2 == 0:
        return 0.0

    return dot_product / (mag1 * mag2)


def main():
# This text file is downloaded from gutenberg.org (https://www.gutenberg.org/cache/epub/1342/pg1342.txt)
    # Process the downloaded texts
    hist1 = process_text(pride_and_prejudice_text, skip_header=True, excluding_stopwords=True)
    hist2 = process_text(emma_text, skip_header=True, excluding_stopwords=True)

    # Displays total word counts
    print(f"Total number of words in Pride and Prejudice: {total_words(hist1)}")
    print(f"Total number of words in Emma: {total_words(hist2)}")

    # Display word frequencies for each text
    print("Word frequencies in Pride and Prejudice:")
    for word, count in hist1.items():
        print(f"{word}: {count}")
    
    print("\nWord frequencies in Emma:")
    for word, count in hist2.items():
        print(f"{word}: {count}")

    #most common words and frequencies - pride and prejudice
    t1 = most_common(hist1)
    print("The most common words in Pride & Prejudice are:")
    for freq, word in t1[0:20]:
        print(word, "\t", freq)

    #most common words and frequencies - emma
    t2 = most_common(hist2)
    print("The most common words in Emma are:")
    for freq, word in t2[0:20]:
        print(word, "\t", freq)

    # Compute cosine similarity between the texts
    cosine_sim = cosine_similarity(hist1, hist2)
    print(f"Cosine Similarity between Pride and Prejudice and Emma: {cosine_sim:.4f}")



if __name__ == "__main__":
    main()