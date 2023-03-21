import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
import urllib.request
from fuzzywuzzy import fuzz

# The Picture of Dorian Gray, by Oscar Wilde
url1 = 'http://www.gutenberg.org/ebooks/174.txt.utf-8'
with urllib.request.urlopen(url1) as f:
    text1 = f.read().decode('utf-8')

# The Happy Prince and Other Tales, by Oscar Wilde
url2 = 'https://www.gutenberg.org/cache/epub/30120/pg30120.txt'
with urllib.request.urlopen(url2) as g:
    text2 = g.read().decode('utf-8')

# Compute similarities between The Picture of Dorian Gray and The Happy Prince and other Tales
words1 = set(text1.split())
words2 = set(text2.split())
similarity_scores = [[fuzz.token_set_ratio(
    w, w2) for w2 in words2] for w in words1]

# I get this line of code from CHATGPT.
dissimilarities = 100 - np.asarray(similarity_scores)


coord = MDS(dissimilarity='precomputed').fit_transform(dissimilarities)

plt.scatter(coord[:, 0], coord[:, 1])

for i in range(coord.shape[0]):
    plt.annotate(str(i), (coord[i, :]))

plt.show()
