import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import sys
from unicodedata import category


def process_file():
    """
    Reads the Metamorphosis book already read

    Clean the text by excluding special characters and converting to lower cases

    Excluding the header and the footer

    Excluding stop words

    Returns a dictionary with each unique words and their counts
    """
    hist = {}
    fp = open("metamorphosis.txt", encoding="utf-8")
    in_project = False  # Initialize in_project to False

    strippables = "".join(
        chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")
    )

    for line in fp:
        if "*** START OF THE PROJECT" in line:
            in_project = True
            continue
        elif "*** END OF THE PROJECT" in line:
            break

        if in_project:
            line = line.replace("-", " ")
            line = line.replace(
                chr(8212), " "
            )  # Unicode 8212 is the HTML decimal entity for em dash

            for word in line.split():
                word = word.strip(strippables)
                word = word.lower()

                # update the dictionary
                hist[word] = hist.get(word, 0) + 1

    stop = open("stopwords.txt")

    for line in stop:
        stopwords = line.strip()
        if stopwords in hist:
            del hist[stopwords]

    return hist


def most_common(hist):
    """
    Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    """

    sort = sorted(hist.items(), key=lambda x: x[1], reverse=True)

    return sort


def cleantext():
    """
    Cleans the text by excluding special characters and converting to lower case.
    Assigns each word to its corresponding chapter in the book.

    Returns: a dictionary where keys are chapter numbers and values are sets of words.
    """
    book = open("metamorphosis.txt", encoding="utf-8")
    chapters = {1: set(), 2: set(), 3: set()}

    in_project = False
    in_part1 = True
    in_part2 = False
    in_part3 = False

    strippables = "".join(
        chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")
    )

    for line in book:
        if "*** START OF THE PROJECT" in line:
            in_project = True
            continue
        elif "*** END OF THE PROJECT" in line:
            break
        elif line.startswith("II"):
            in_part1 = False
            in_part2 = True
            continue
        elif line.startswith("III"):
            in_part2 = False
            in_part3 = True
            continue

        if in_project:
            line = line.replace("-", " ")
            line = line.replace(chr(8212), " ")
            for word in line.split():
                word = word.strip(strippables)
                word = word.lower()

                if in_part1:
                    chapters[1].add(word)
                elif in_part2:
                    chapters[2].add(word)
                elif in_part3:
                    chapters[3].add(word)

    return chapters


def main():
    hist = process_file()  # This text file is downloaded from gutenberg.org
    print("Simple Text Cleaning:")
   
    t = most_common(hist)
    print("The most common 30 words are:")
    for freq, word in t[0:30]:
        print(word, "\t", freq)

    ## Natural Language Processing ##

    nltk.download("vader_lexicon")

    for freq, word in t[0:30]:
        score = SentimentIntensityAnalyzer().polarity_scores(freq)
        print(score)

    text = open("metamorphosis.txt")
    print(text)


if __name__ == "__main__":
    main()
