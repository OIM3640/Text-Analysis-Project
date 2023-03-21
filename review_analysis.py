import movie_reviews


def review_dict(movie_name):
    """
    Counts the frequency of words in the movie review list, and returns a dictionary with words and its corresponding frequency count.
    """
    # Create dictionary of reviews and extract movie reviews from the function above.
    hist = {}
    review_list = movie_reviews.process_reviews(movie_name, exclude_stopwords=True)

    for review in review_list:
        words = review.split()  # Split reviews into words
        for word in words:
            hist[word] = hist.get(word, 0) + 1  # Update dictionary word frequency
    return hist


def most_frequent(hist, num=10):
    """
    Makes a list of the most frequent words in the movie dictionary.
    Prints the most frequent words in the reviews and its fequency. (tnum = the number of words printed)
    """
    res = []
    for word in hist:
        freq = hist[word]
        res.append((freq, word))
    res.sort(reverse=True)

    for freq, word in res[0:num]:
        print(word, "\t", freq)


def main():
    """
    This will be the entry function. All the test code goes here.
    """
    # Creed 1
    hist_creed = review_dict("Creed (2015)")
    # print(hist_creed) # Prints movie word frequency dictionary
    print("The top 10 most frequent words for Creed 1 are: ")
    most_frequent(hist_creed)

    # Creed 2
    hist_creed2 = review_dict("Creed 2")
    # print(hist_creed2) # Prints movie word frequency dictionary
    print("The top 10 most frequent words for Creed 2 are: ")
    most_frequent(hist_creed2)

    # Creed 3
    hist_creed3 = review_dict("Creed 3")
    # print(hist_creed3) # Prints movie word frequency dictionary
    print("The top 10 most frequent words for Creed 3 are: ")
    most_frequent(hist_creed3)


if __name__ == "__main__":
    main()
