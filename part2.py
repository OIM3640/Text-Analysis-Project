### Part 2 Analyzing Text ###

## Natrual Language Processing ##
import nltk

nltk.download("vader_lexicon")

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentence = "Software Design is my favorite class because learning Python is so cool!"
score = SentimentIntensityAnalyzer().polarity_scores(sentence)
print(score)
# Output
# {'neg': 0.0, 'neu': 0.614, 'pos': 0.386, 'compound': 0.7417}


## Text Similarity ##

from thefuzz import fuzz

print(fuzz.ratio("this is a test", "this is a test!"))  # 97
print(fuzz.partial_ratio("this is a test", "this is a test!"))  # 100
print(fuzz.ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear"))  # 91
print(fuzz.token_sort_ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear"))  # 100


## Text Clustering ##
import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

# these are the similarities computed from the previous section
S = np.asarray(
    [
        [1.0, 0.90850572, 0.96451312, 0.97905034, 0.78340575],
        [0.90850572, 1.0, 0.95769915, 0.95030073, 0.87322494],
        [0.96451312, 0.95769915, 1.0, 0.98230284, 0.83381607],
        [0.97905034, 0.95030073, 0.98230284, 1.0, 0.82953109],
        [0.78340575, 0.87322494, 0.83381607, 0.82953109, 1.0],
    ]
)

# dissimilarity is 1 minus similarity
dissimilarities = 1 - S

# compute the embedding
coord = MDS(dissimilarity="precomputed").fit_transform(dissimilarities)

plt.scatter(coord[:, 0], coord[:, 1])

# Label the points
for i in range(coord.shape[0]):
    plt.annotate(str(i), (coord[i, :]))

plt.show()
