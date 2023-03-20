from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ia = Cinemagoer()


def get_reviews(movie_name):
    """
    Search for movie id for the given movie and returns the first five reviews.
    """
    # Search for movie ids
    movie = ia.search_movie(movie_name)[0]
    movie_id = movie.movieID

    # Get First 5 movie reviews
    movie_reviews = ia.get_movie_reviews(movie_id)
    movie_reviews5 = []

    for i in range(5):
        movie_content = movie_reviews["data"]["reviews"][i]["content"]
        movie_reviews5.append(movie_content)
    return movie_reviews5


def process_reviews(movie_name):
    """
    Makes a dictionary that contains the frequency of words in the first five reviews.
    """
    hist = {}
    review_list = get_reviews(movie_name)

    # Split reviews into words
    for review in review_list:
        words = review.split()

        # Update words in dictionary
        for word in words:
            word = word.lower()
            hist[word] = hist.get(word, 0) + 1
    return hist


def main():
    """
    This will be the entry function. All the test code goes here.
    """
    # # Creed 1 
    # creed1 = "Creed (2015)"
    # hist_creed = process_reviews(creed1)
    # print(hist_creed)

    # # Creed 2
    # creed2 = "Creed 2"
    # hist_creed2 = process_reviews(creed2)
    # print(hist_creed2)

    # # Creed 3
    # creed3 = "Creed 3"
    # hist_creed3 = process_reviews(creed3)
    # print(hist_creed3)

if __name__ == "__main__":
    main()
