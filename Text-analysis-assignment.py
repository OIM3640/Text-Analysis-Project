import urllib.request
import string
import sys
from unicodedata import category


def process_file(text, skip_header):
    """
    Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}

    if skip_header:
        skip_gutenberg_header(text)

    strippables = string.punctuation + string.whitespace
    # via: https://stackoverflow.com/questions/60983836/complete-set-of-punctuation-marks-for-python-not-just-ascii

    strippables = "".join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )
    ##ChatGPT helped fix so that the end is skipped and makes sure header is skipped
    for line in text.splitlines():
        if line.startswith("*** END OF THIS PROJECT"):
            break
        
        line = line.replace("-", " ")
        line = line.replace(
            chr(8212), " "
        )  # Unicode 8212 is the HTML decimal entity for em dash

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update
            hist[word] = hist.get(word, 0) + 1

    return hist


def skip_gutenberg_header(text):
    """
    Reads from fp until it finds the line that ends the header.
    """
    lines = text.splitlines() #learned from ChatGPT
    for i, line in enumerate(lines):
        if line.startswith("*** START OF THIS PROJECT"):
            break
    return '\n'.join(lines[i + 1:])

def read_stopwords(file_path):
    """
    Reads stopwords from a file and returns a list of stopwords.
    """
    stopwords = []
    with open('data/stopwords.txt', 'r') as file:
        for line in file:
            word = line.strip()
            stopwords.append(word)
    stopwords.append('us')
    return stopwords


def most_common(hist, stopwords=None):
    """
    Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    t = []

    for word, freq in hist.items():
        if stopwords and word in stopwords:
            continue
        t.append((freq, word))

    t.sort(reverse=True)
    return t


def different_words(hist):
    """
    Returns the number of different words in a histogram.
    """
    return len(hist)


def main():
    url = 'https://www.gutenberg.org/cache/epub/1727/pg1727.txt'
    with urllib.request.urlopen(url) as f:
        text = f.read().decode('utf-8')
    
    stopwords = read_stopwords('stopwords.txt')

    hist = process_file(text, skip_header=True)
    print(hist) # for testing
    
    print('Number of different words:', different_words(hist))

    t = most_common(hist, stopwords=stopwords)
    print('The most common words are:')
    for freq, word in t[0:10]:
        print(word, '\t', freq)
    


if __name__ == "__main__":
    main()