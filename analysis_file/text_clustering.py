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

#De Profundis, by Oscar Wilde
url3 = 'https://www.gutenberg.org/cache/epub/921/pg921.txt'
with urllib.request.urlopen(url3) as h:
    text3 = h.read().decode('utf-8')

#The Importance of Being Earnest, by Oscar Wilde
url4 = 'https://www.gutenberg.org/files/844/844-0.txt'
with urllib.request.urlopen(url4) as i:
    text4 = i.read().decode('utf-8')

#The Gentle Art of Making Enemies, by James McNeill Whistler
url5 = 'https://www.gutenberg.org/cache/epub/24650/pg24650.txt'
with urllib.request.urlopen(url5) as j:
    text5 = j.read().decode('utf-8')

#The Story of Venus and Tannhäuser, by Aubrey Beardsley
url6 = 'https://www.gutenberg.org/cache/epub/50210/pg50210.txt'
with urllib.request.urlopen(url6) as k:
    text6 = k.read().decode('utf-8')

texts = [text1, text2, text3, text4, text5, text6]
vocabulary = set()
similarity_scores = np.zeros((len(texts), len(texts)))
for i in range(len(texts)):
    words_i = set(texts[i].split())
    vocabulary |= words_i
    for j in range(i+1, len(texts)):
        words_j = set(texts[j].split())
        vocabulary |= words_j
        score = len(words_i & words_j) / len(words_i | words_j)
        similarity_scores[i, j] = score
        similarity_scores[j, i] = score

# Calculate dissimilarities
dissimilarities = 1 - similarity_scores

# Calculate MDS coordinates
coord = MDS(dissimilarity='precomputed').fit_transform(dissimilarities)

# Plot scatter plot with annotations
plt.scatter(coord[:, 0], coord[:, 1])

for i in range(coord.shape[0]):
    plt.annotate(str(i), (coord[i, :]))

plt.show()
