from imdb import Cinemagoer
import random

# ChatGPT told me how to download stopwords
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# ChatGPT told me about word frequency counter
from collections import Counter

nltk.download("punkt")
nltk.download("stopwords")
ia = Cinemagoer()


def random_movies():
    '''This function simply returns a list of 5 random numbers from 0-99'''
    random_ints = []
    while len(set(random_ints)) != 5:
        random_ints.append(random.randint(0, 99))
    # uncomment to see which ints it is choosing
    # print(set(random_ints))
    return set(random_ints)


# Thanks for teaching us about set! Super useful.

# I inputted the docs to Cinemagoer to ChatGPT and it told me there was a top_250 movies, so I went to experiment on VSC and when I type get_ it allowed me to choose from an entire list of categories.
def movie_choice_b100():
    '''This function takes the list of integers from random_movies() and converts them into movie_ids using the list of the 100 bottom movies'''
    movies = ia.get_bottom100_movies()
    movie_ids = []
    for movie_num in random_movies():
        movie_ids.append(movies[movie_num].movieID)
    return movie_ids


def movie_reviews():
    '''This function takes the movie IDs from movie_choice_b100() and makes a dictionary with the titles of movies as keys and the movie review as value'''
    # This block of code was heavily inspired by your example in the instructions
    movies_and_reviews = {}
    for id in movie_choice_b100():
        movie = ia.get_movie(id)
        title = movie["title"]
        movie_reviews = ia.get_movie_reviews(id)
        movies_and_reviews[title] = movie_reviews["data"]["reviews"][0]["content"]
    return movies_and_reviews


# https://www.w3schools.com/python/python_dictionaries_add.asp


def review_stripper():
    '''This function takes the dictionary from movie_reviews() and strips the reviews of most punctuation and stop words (words like a, and, the). The function then creates a new dictionary with the titles of movies as keys and filtered reviews as values '''
    current_reviews = movie_reviews()
    altered_reviews = {}
    stop_words = stopwords.words("english")
    punctuation = string.punctuation
    for movie in current_reviews:
        review = current_reviews[movie]
        tokenizer = word_tokenize(review)
        filtered_review = []
        # https://www.geeksforgeeks.org/string-punctuation-in-python/
        for word in tokenizer:
            if word.lower() not in stop_words and word not in punctuation:
                filtered_review.append(word)
        altered_reviews[movie] = filtered_review
    return altered_reviews


def review_word_frequency():
    '''This function takes the dictionary from review_stripper() and makes a new frequency with the movie titles as keys and frequency of words in each review as values'''
    current_reviews = review_stripper()
    word_frequency = {}
    for review in current_reviews:
        word_count = Counter(current_reviews[review])
        word_frequency[review] = word_count
    print(word_frequency)
    return word_frequency


if __name__ == "__main__":
    review_word_frequency()

# https://cinemagoer.readthedocs.io/en/latest/usage/data-interface.html#composite-data
# https://github.com/cinemagoer/cinemagoer
