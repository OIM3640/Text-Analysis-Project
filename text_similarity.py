from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import movie_reviews


def similarity(movie_name):
    """ """
    # Get list of first 5 reviews
    review_list = movie_reviews.get_reviews(movie_name)

    # Create a TF-IDF vectorizer object
    vectorizer = TfidfVectorizer()

    # Vectorize the texts
    vectors = vectorizer.fit_transform(review_list)

    # Compute the cosine similarity between all pairs of texts
    cosine_sim = cosine_similarity(vectors)

    # Print the similarity matrix
    print(np.round(cosine_sim, 2))


def main():
    """
    This will be the entry function. All the test code goes here
    """
    movie = "Creed 3"
    similarity(movie)


if __name__ == "__main__":
    main()
