### Theme analysis for Metamorphosis ###


## Download the book from gutenberg ##

import urllib.request
import pickle
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

url = "https://www.gutenberg.org/cache/epub/5200/pg5200.txt"
with urllib.request.urlopen(url) as f:
    metamorphosis = f.read().decode("utf-8")
    # print(metamorphosis)


## Pickling Data ##

with open("metamorphosis.pkl", "wb") as f:
    pickle.dump(metamorphosis, f)
# wb => writes data without changing it
# saving in binary format

# Load data from the file
with open("metamorphosis.pkl", "rb") as f:
    book = pickle.load(f)
# rb => reads data without changing it


# Start cleaning the text (Code modified from class materials)
import sys
from unicodedata import category


def process_file():
    """
    Reads the Metamorphosis book already read

    Clean the text by excluding special characters and converting to lower cases

    Exluding the header and the footer

    Excluding stop words

    Returns a dictionary with each unique words and thier counts
    """
    hist = {}
    fp = book
    in_project = False  # Initialize in_project to False

    # if skip_header:
    #     skip_gutenberg_header(fp)
    # For some reason this line did not work so I changed to another way

    strippables = "".join(
        chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")
    )  # https://stackoverflow.com/questions/60983836/complete-set-of-punctuation-marks-for-python-not-just-ascii

    # split the book by line
    # in_project is defined so we only access text in between start and end of the project
    # when encountering start of the project => in_project is TRUE and
    # we continue to read the lines until we reaches end of the project
    for line in fp.split("\n"):
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
                # word could be 'Sussex.'
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


# Originally, the code I copied from class material on textual analysis did not work
# as it only gives me a dictionary consist of letters as key instead of words
# I asked help from ChatGPT where I asked it how to get words instead of letters
# Below are some modifications on the original code:
# 1. changed the argument filename direcly to the already loaded file
# 2. changing the ways to delet header and footer using for loop


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)


def cleantext():
    """
    Reads the Metamorphosis book already read

    Clean the text by excluding special characters and converting to lower cases

    Exluding the header and the footer

    Excluding stop words

    Returns a dictionary with each unique words and thier corresponding chapters in the book
    """
    hist = {}
    fp = book

    in_project = False
    in_part1 = True
    in_part2 = False
    in_part3 = False

    strippables = "".join(
        chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")
    )  # https://stackoverflow.com/questions/60983836/complete-set-of-punctuation-marks-for-python-not-just-ascii

    for line in fp.split("\n"):
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
                    hist[word] = 1
                elif in_part2:
                    hist[word] = 2
                elif in_part3:
                    hist[word] = 3

    stop = open("stopwords.txt")

    for line in stop:
        stopwords = line.strip()
        if stopwords in hist:
            del hist[stopwords]

    return hist


def cleantext():
    """
    Cleans the text by excluding special characters and converting to lower case.
    Assigns each word to its corresponding chapter in the book.

    Returns: a dictionary where keys are chapter numbers and values are sets of words.
    """
    hist = []

    in_project = False

    strippables = "".join(
        chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")
    )

    for line in book.split("\n"):
        if "*** START OF THE PROJECT" in line:
            in_project = True
            continue
        elif "*** END OF THE PROJECT" in line:
            break

        if in_project:
            line = line.replace("-", " ")
            line = line.replace(chr(8212), " ")
            for word in line.split():
                word = word.strip(strippables)
                word = word.lower()

                hist.append(word)

    return hist


## Natrual Language Processing ##
import nltk

nltk.download("vader_lexicon")

from nltk.sentiment.vader import SentimentIntensityAnalyzer


def sentiment_of_context():
    dict = {}

    text = cleantext()
    hist = process_file()

    commonwords = most_common(hist)
    commonwords50 = commonwords[:51]
    # this is a list of tuple in form of word and frequency

    for word, freq in commonwords50:
        if word in text:
            # Goal => find the 5 words before and after the most common word
            # to understand the context of the word
            # and access the sentiment using NLP
            # Note => avoide going over the lenght of the text

            start_index = max(0, text.index(word) - 5)
            end_index = min(len(text), text.index(word) + 6)
            # Add 6 => X include the top

            # Knit all the nearby words together
            context = text[start_index:end_index]  # note that this is list

            sentence = " ".join(context)
            # join list to a str by blank space => make up a sentence

            # get the sentiment score for the context
            score = SentimentIntensityAnalyzer().polarity_scores(sentence)

            dict[word] = score
    return dict


def main():
    hist = process_file()  # This text file is downloaded from gutenberg.org
    # print(hist)
    print("Simple Text Cleaning:")
    print("Total number of words excluding stop words:", total_words(hist))
    print("Number of different words:", different_words(hist))

    t = most_common(hist)
    print("The most common 30 words are:")
    for freq, word in t[0:30]:
        print(word, "\t", freq)

    ## NLP Sentiment of Context ##
    sentiments = sentiment_of_context()

    # Prints the top 10 most common words and thier correseponding context sentiment scores
    print("The context sentiment scores for the 10 most commonly appearing words are:")
    for key, value in list(sentiments.items())[:10]:
        # converts dictionary into list and only loop for top 10 keys
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()


# ChatGPT Chat History
# https://chat.openai.com/c/c96b6bac-e943-40b9-98c4-9b9a0b355131
