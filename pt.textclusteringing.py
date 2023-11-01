from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

# load the documents
with open("extract/article1.txt", "r", encoding="utf-8") as file:
    document1 = file.read()
    
with open("extract/article2.txt", "r", encoding="utf-8") as file:
    document2 = file.read()
    


# create a list of documents
documents = [document1, document2]

# create a TfidfVectorizer to convert the documents into a matrix of TF-IDF features
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(documents)

# calculate pairwise cosine similarities
pairwise_similarities = cosine_similarity(tfidf_matrix)

# apply MDS to the pairwise similarities
mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
pos = mds.fit_transform(pairwise_similarities)

# plot the MDS result
xs, ys = pos[:, 0], pos[:, 1]
names = ['document1', 'document2', 'document3']
for x, y, name in zip(xs, ys, names):
    plt.scatter(x, y)
    plt.text(x, y, name)

plt.show()
