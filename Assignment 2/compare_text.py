import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_text_similarity(url_1, url_2):
    "Comparing text similarity between 2 different books."
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([url_1 , url_2])
    cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
    return cosine_sim[0][0]

import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

similarity_score = 0.55
new_S = np.full((5, 5), similarity_score, dtype=float)
np.fill_diagonal(new_S, 1.0)

# dissimilarity is 1 minus similarity
dissimilarities = 1 - new_S

# compute the embedding
coord = MDS(dissimilarity='precomputed').fit_transform(dissimilarities)

plt.scatter(coord[:, 0], coord[:, 1])

# Label the points
for i in range(coord.shape[0]):
    plt.annotate(str(i), (coord[i, :]))

plt.show()

def main():
    url_1 = 'https://gutenberg.org/cache/epub/11/pg11.txt' #'Alice in Wonderland' 
    url_2 = 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt' #'The Great Gatsby'

    similarity_score = calculate_text_similarity(url_1, url_2)
    print(similarity_score) #55%

if __name__ == '__main__':
    main()