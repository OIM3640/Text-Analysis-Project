# import urllib.request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import sys
from mediawiki import MediaWiki
from thefuzz import fuzz
from unicodedata import category
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt


def process_file(filename, skip_header):
    """Helps process the file containing Percy jackson and adds the words to a dictionary."""
    fp = open(filename, encoding='UTF8')
    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")])
    if skip_header:
        skip_gutenberg_header(fp)
    word_freq = {}
    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break
        line = line.replace('-', ' ')
        line = line.replace(
            chr(8212), ' '
        )  # Unicode 8212 is the HTML decimal entity for em dash

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            if word not in word_freq:
                word_freq[word] = 1
            elif word in word_freq:
                word_freq[word] += 1
    return word_freq


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break


def removestopwords(fp):
    """This function helps delete all the stop words from the dictionary. For example, of, the, who, etc."""
    stopwords = []
    word_file = open("data/stopwords.txt", encoding='UTF8')
    for word in word_file:
        stopwords.append(word.strip())
    for word in stopwords:
        if word in fp:
            del fp[word]
    return fp


def mostcommon(hist):
    """This function is used to calculate the 10 most common words occuring in the Percy Jackson text."""
    common = []
    for word, val in hist.items():
        common.append((val, word))
    common.sort(reverse=True)
    for freq, word in common[0:10]:
        print(word, '\t', freq)


def compare_texts(filename, filename2):
    """This function is used to analyse the text similarity between Charles Dickens and Percy Jackson
    by comparing their similarity line by line and then returning their average similarity."""
    fp = open(filename, encoding='UTF8')
    Dickens = open(filename2, encoding='UTF8')
    strippables = ''.join([chr(i) for i in range(
        sys.maxunicode) if category(chr(i)).startswith("P")])

    total = 0
    similarity_sum = 0
    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break
        for d_line in Dickens:
            if d_line.startswith('***END OF THE PROJECT'):
                break
            ratio = fuzz.ratio(line, d_line)
            similarity_sum += ratio
            total += 1

    average_similarity = similarity_sum / total
    print(
        f'The average ratio between the two texts is {average_similarity:.2f}')


def get_average_polarity(filename):
    """This function calculates the average polarity score for a given text."""
    with open(filename, encoding='UTF8') as f:
        text = f.read()
    sid = SentimentIntensityAnalyzer()
    sentences = nltk.tokenize.sent_tokenize(text)
    fp = open(filename, encoding='UTF8')
    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")])
    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break
    polarity_sum = 0
    for sentence in sentences:
        polarity = sid.polarity_scores(sentence)['compound']
        polarity_sum += polarity
    average_polarity = polarity_sum / len(sentences)
    return round(average_polarity, 2)


def check_patterns():
    """This function helps check the cosine similarity between Babson college and Bentley University"""
    wikipedia = MediaWiki()
    babson = wikipedia.page("Babson College").content
    bentley = wikipedia.page("Bentley University").content
    doc = [babson, bentley]
    vector = CountVectorizer()
    matrix = vector.fit_transform(doc)
    similarity = cosine_similarity(matrix)
    return similarity


def plot_matrix():
    """This function will help plot the cosine similarity between Babson college and Bentley university using MDS"""
    s = np.asarray(check_patterns())
    dissimilarities = 1 - s
    coord = MDS(dissimilarity='precomputed').fit_transform(dissimilarities)
    plt.scatter(coord[:, 0], coord[:, 1])
    for i in range(coord.shape[0]):
        plt.annotate(str(i), (coord[i, :]))

    plt.show()


def main():
    hist = {}
    hist = process_file("data/percy_jackson.txt", skip_header=True)
    hist = removestopwords(hist)
    mostcommon(hist)
    compare_texts("data/percy_jackson.txt", "data/Dickens.txt")
    print(get_average_polarity("data/percy_jackson.txt"))
    check_patterns()
    plot_matrix()


if __name__ == '__main__':
    main()
