### PART 1: importing data sources - 2 most popular jane austen texts
import urllib.request

url1 = 'https://www.gutenberg.org/cache/epub/1342/pg1342.txt' #pride and prejudice
url2 = 'https://www.gutenberg.org/cache/epub/158/pg158.txt' #emma
with urllib.request.urlopen(url1) as f:
    pride_and_prejudice_text = f.read().decode('utf-8')
    # print(text) # for testing
with urllib.request.urlopen(url2) as f:
    emma_text = f.read().decode('utf-8')
    # print(text) # for testing


# processes text to remove irrelevant headers by using code from in class exercise form session 15 - adapted to accept text a opposed to file from data folder 

import random
import string
import sys
from unicodedata import category

def process_file(text, skip_header):
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
            word = word.strip(strippables)
            word = word.lower()

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


### characterizing by word frequencies 

#pride and prejudice

#emma 


def main():
    # This text file is downloaded from gutenberg.org (https://www.gutenberg.org/cache/epub/1342/pg1342.txt)
      # Process the downloaded text of Pride and Prejudice
    hist1 = process_file(pride_and_prejudice_text, skip_header=True)
    print(f"Total number of words in Pride and Prejudice: {total_words(hist1)}")
    
    # Process the downloaded text of Emma
    hist2 = process_file(emma_text, skip_header=True)
    print(f"Total number of words in Emma: {total_words(hist2)}")


if __name__ == "__main__":
    main()