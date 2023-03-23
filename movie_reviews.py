from imdb import Cinemagoer
import nltk
import string
from nltk.corpus import stopwords

nltk.download("stopwords")

# create an instance of the Cinemagoer class
ia = Cinemagoer()


def get_reviews(movie_name):
    """
    Search for movie id for the given movie and returns the list of movie reviews.
    """
    # Search for movie ids
    movie = ia.search_movie(movie_name)[0]
    movie_id = movie.movieID

    # Get movie reviews
    movie_reviews = ia.get_movie_reviews(movie_id)
    movie_reviews_list = []

    for i in range(len(movie_reviews["data"]["reviews"])):
        movie_content = movie_reviews["data"]["reviews"][i]["content"]
        movie_reviews_list.append(movie_content)
    return movie_reviews_list


def process_reviews(movie_name, exclude_stopwords=False):
    """
    Process the extracted reviews from the function above by removing stopwords and unnecessary characters.
    Returns the cleaned review list for the given movie.
    """
    # Add stopwords from nltk library
    stop_words = set(stopwords.words("english"))

    # Add punctuation and whitespaces
    strippables = string.punctuation + string.whitespace

    # Create a list of cleaned reviews without stopwords and strippables.
    review_list = get_reviews(movie_name)
    cleaned_reviews = []

    # Split reviews into words
    for review in review_list:
        words = review.split()

        cleaned_sentence = []
        for word in words:
            word = word.strip(strippables)
            word = word.lower()
            if exclude_stopwords:
                if word in stop_words:
                    continue
            cleaned_sentence.append(word)

        cleaned_reviews.append(" ".join(cleaned_sentence))
    return cleaned_reviews


def main():
    """
    This will be the entry function. All the test code goes here.
    """
    # Creed 1
    creed1 = "Creed (2015)"
    creed_list = process_reviews(creed1, exclude_stopwords=True)
    print(creed_list)

    # Creed 2
    creed2 = "Creed 2"
    creed2_list = process_reviews(creed2, exclude_stopwords=True)
    print(creed2_list)

    # Creed 3
    creed3 = "Creed 3"
    creed3_list = process_reviews(creed3, exclude_stopwords=True)
    print(creed3_list)

    
if __name__ == "__main__":
    main()
