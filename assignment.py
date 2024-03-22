from mediawiki import MediaWiki

import sys
from unicodedata import category
import nltk
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import random
from thefuzz import fuzz
import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt


def process_file(content):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    hist = {}
    
    strippables = "".join(
        chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")
    )

    for line in content.split():
        line.split()
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

    return hist


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram"""
    return len(hist.keys())


def most_common(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    sorted_items = sorted(hist.items(), key=lambda item: item[1], reverse=True)

    if excluding_stopwords:
        stop_words = set(stopwords.words('english'))
        sorted_items = [
            (freq, word) for word, freq in sorted_items if word not in stop_words
        ]
        sorted_items = [
            (freq, word) for freq, word in sorted_items if word.isalpha()
        ]

    return sorted_items


def print_most_common(hist, num):
    """Prints the most commons words in a histgram and their frequencies.

    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    common_words = most_common(hist)[:num]

    common_words = common_words[:num]

    print(common_words)


def random_word(hist):
    """Chooses a random word from a histogram.

    The probability of each word is proportional to its frequency.
    """
    total_freq = sum(hist.values())

    rand_val = random.randint(0, total_freq - 1)

    cumulative_freq = 0
    for word, freq in hist.items():
        cumulative_freq += freq
        if rand_val < cumulative_freq:
            return word


def random_sentence(wiki_page):
    sentences = nltk.sent_tokenize(wiki_page)
    random_sentence = random.choice(sentences)

    return random_sentence


def sentiment_analysis(sentence):
    score = SentimentIntensityAnalyzer().polarity_scores(sentence)
    return score


def text_similarity(sentence1, sentence2):
    ratio = fuzz.ratio(sentence1, sentence2)
    partial_ratio = fuzz.partial_ratio(sentence1, sentence2)
    token_sort_ratio = fuzz.token_sort_ratio(sentence1, sentence2)

    return ratio, partial_ratio, token_sort_ratio

        
def main():
    wikipedia = MediaWiki()
    tate_mcrae = wikipedia.page("Tate McRae")
    hist = process_file(tate_mcrae.content)

    print(hist)
    print("Total number of words:", total_words(hist))
    print("Number of different words:", different_words(hist))

    t = most_common(hist, excluding_stopwords=True)
    print("The most common words are:")
    for freq, word in t[0:20]:
        print(word, freq)
    
    print_most_common(hist, num=20)

    print("\n\nHere are some random words from the Wikipedia page:")
    for i in range(100):
        print(random_word(hist), end=' ')

    wiki_page = tate_mcrae.content
    sentence = random_sentence(wiki_page)
    print(f"\n\nThis is the random sentence:\n{sentence}")
    print(f"This is the sentiment score of the sentence:\n{sentiment_analysis(sentence)}")

    sentence1 = random_sentence(wiki_page)
    sentence2 = random_sentence(wiki_page)
    print(f"This is sentence 1:\n{sentence1}")
    print(f"This is sentence 2:\n{sentence2}")
    print(f"The text similarity score between the two sentence are: {text_similarity(sentence1, sentence2)}")


if __name__ == "__main__":
    main()