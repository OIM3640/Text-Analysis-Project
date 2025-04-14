# Retrieve the first review for the movie "Dead Poets Society"
from imdb import Cinemagoer
import string
import sys
from unicodedata import category
import nltk
from nltk.corpus import stopwords

# nltk.download('vader_lexicon')

ia = Cinemagoer()

movie = ia.search_movie("Dead Poets Society")[0]
print(movie.movieID)
# 0097165

movie = ia.get_movie("0097165", info=["reviews"])
reviews = movie.get("reviews", [])

# Creates a list of words for the first review
moviereview = []
for review in reviews:
    print(review["content"])
    print()
    moviereview.append(review["content"])

# Start Pickling Data
import pickle

with open("moviereview.pkl", "wb") as f:
    pickle.dump(moviereview, f)


with open("moviereview.pkl", "rb") as f:
    reloaded_copy_of_texts = pickle.load(f)
# used "wb" and "rb" to specify binary write mode

# print(reloaded_copy_of_texts)

# Part 2:
# Characterizing by Word Frequencies


def word_freq(texts):
    """
    removes punctuation and stop words
    use a **dictionary** where the keys are words that
    appear and the values are frequencies of words in the text
    """
    d = {}
    strippables = string.punctuation + string.whitespace

    strippables = "".join(
        chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")
    )  # https://stackoverflow.com/questions/60983836/complete-set-of-punctuation-marks-for-python-not-just-ascii

    nltk.download("stopwords")
    stop_words = set(stopwords.words("english"))

    for line in reloaded_copy_of_texts:
        if line.startswith("*** END OF THE PROJECT"):
            break

        line = (
            line.replace("-", " ")
            .replace("/", " ")
            .replace("(", " ")
            .replace(")", " ")
            .replace("'", " ")
            .replace(".", " ")
            .replace("?", " ")
            .replace(":", " ")
        )
        line = line.replace(
            chr(8212), " "
        )  # Unicode 8212 is the HTML decimal entity for em dash

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()
            if (
                word and word not in stop_words
            ):  # created the dictionary without stop words
                d[word] = d.get(word, 0) + 1
    return d


word_frequencies = word_freq(reloaded_copy_of_texts)
print(word_frequencies)


# Computing Summary Statistics
def top_ten(d):
    """
    Identifies the top ten words that appeared in the review
    """
    top_ten = sorted(d.items(), key=lambda x: x[1], reverse=True)[:10]
    for word, frequency in top_ten:
        print(word, ":", frequency)


top_ten(word_frequencies)

# Removing stop words is already done when generating the word frequency dictionary

# Natural Language Processing
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def sentimental_analysis():
    """
    takes the sentiment scores and draws interesting arguments from the review
    """
    max_pos_score = -1
    max_neg_score = -1
    most_positive_line = ""
    most_negative_line = ""
    for line in reloaded_copy_of_texts:
        score = SentimentIntensityAnalyzer().polarity_scores(line)
        pos_score = score["pos"]
        neg_score = score["neg"]
        print("Text:", line)
        print("Sentiment Score:", score)
        if pos_score > max_pos_score:
            # compares with the -1 at first and stores the previous score
            # because positive score is between 0 to 1, it can never be smaller than -1
            max_pos_score = pos_score
            most_positive_line = line
        if neg_score > max_neg_score:
            max_neg_score = neg_score
            most_negative_line = line
    print(f"The most positive line: {most_positive_line} \n {max_pos_score}")
    print(f"The most negative line: {most_negative_line} \n {max_neg_score}")


sentimental_analysis()

# Text Similarity
from thefuzz import fuzz

# get another review from similar type of movie (no longer using because no similarity):
# ia = Cinemagoer()

# movie2 = ia.search_movie("The Holdovers")[0]
# print(movie2.movieID)
# # 14849194

# movie2 = ia.get_movie("14849194", info=["reviews"])
# reviews2 = movie2.get("reviews", [])

# # Creates a list of words for the first review
# moviereview2 = []
# for review in reviews2:
#     print(review["content"])
#     print()
#     moviereview2.append(review["content"])

# # Start Pickling Data
# import pickle

# with open("moviereview.pkl", "wb") as f2:
#     pickle.dump(moviereview2, f2)


# with open("moviereview.pkl", "rb") as f2:
#     reloaded_copy_of_texts2 = pickle.load(f2)

# Test:
print(fuzz.ratio("this is a test", "this is a test!"))  # 97, correct

# print(fuzz.ratio(reloaded_copy_of_texts2, reloaded_copy_of_texts))  # 0, no similarity
# print(fuzz.partial_ratio(reloaded_copy_of_texts2, reloaded_copy_of_texts)) # 0

def similarity():
    """
    generate similarity ratios from each passages from the review text
    """
    l = []
    reference = reloaded_copy_of_texts[0]
    for paragraph in reloaded_copy_of_texts:
        l.append(fuzz.ratio(paragraph, reference ))
    return l
    
print(similarity())
#[100, 42, 40, 43, 38, 43, 40, 44, 30, 41, 43, 37, 42, 27, 42, 43, 42, 38, 27, 35, 35, 40, 34, 43, 32]

# Text Clustering 
import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

# these are the similarities computed from the previous section
S = np.asarray([[100, 42, 40, 43, 38, 43, 40, 44, 30, 41, 43, 37, 42, 27, 42, 43, 42, 38, 27, 35, 35, 40, 34, 43, 32]])

# dissimilarity is 1 minus similarity
n = S.shape[1]
dissimilarities = np.zeros((n, n))
for i in range(n):
    for j in range(i, n):  # Iterate over the upper triangular part of the matrix
        dissimilarities[i, j] = 1 - S[0, j] / 100
        dissimilarities[j, i] = dissimilarities[i, j]
# I encounter aa valueerror : ValueError: array must be 2-dimensional and square. shape = (1, 25)
# And the above code is the solution provided by chatgpt
# It converts the ratios into a square matrix

# compute the embedding
coord = MDS(n_components=2, dissimilarity='precomputed').fit_transform(dissimilarities)

plt.scatter(coord[:, 0], coord[:, 1])

# Label the points
for i in range(coord.shape[0]):
    plt.annotate(str(i), (coord[i, 0], coord[i, 1]))

plt.show()