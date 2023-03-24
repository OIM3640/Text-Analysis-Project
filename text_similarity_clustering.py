from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
import numpy as np
import movie_reviews


def similarity(movie_name):
    """
    Generates the cosine similarity between the reviews.
    Returns the cosine similairty matrix between the reviews.
    """
    # Get list of  reviews
    review_list = movie_reviews.process_reviews(movie_name, exclude_stopwords=True)

    # Convert reviews to vectors
    vectors = TfidfVectorizer().fit_transform(review_list)

    # Compute the cosine similarity between all pairs of reviews
    cosine_sim = cosine_similarity(vectors)

    # Return the similarity matrix
    similarity_matrix = np.round(cosine_sim, 2)
    return similarity_matrix


def clustering_kmeans(movie_name):
    """
    Perform KMeans Clustering algorithm with similarity matrix for the given movie from the above function.
    Clusters the data into 3 clusters, and plotted on a graph.
    """

    # Get similarity matrix
    similarity_matrix = similarity(movie_name)

    # Compute dissimilarity
    dissimilarities = 1 - similarity_matrix

    # Multi-dimensional Scaling (MDS) embedding on the dissimilarity matrix
    coord = MDS(dissimilarity="precomputed").fit_transform(dissimilarities)

    # Compute kmean model with dissimilarity matrix
    clusters = 3
    kmeans = KMeans(n_clusters=clusters).fit(dissimilarities)

    # Get labels
    labels = kmeans.labels_

    # Plot clusters
    plt.scatter(coord[:, 0], coord[:, 1], c=labels)

    # Lable the points
    for i in range(coord.shape[0]):
        plt.annotate(str(i), (coord[i, :]))

    plt.title(movie_name)
    plt.show()


def main():
    """
    This will be the entry function. All the test code goes here
    """
    # Creed 1
    creed1 = "Creed (2015)"
    clustering_kmeans(creed1)

    # Creed 2
    creed2 = "Creed 2"
    clustering_kmeans(creed2)

    # Creed 3
    creed3 = "Creed 3"
    clustering_kmeans(creed3)


if __name__ == "__main__":
    main()
