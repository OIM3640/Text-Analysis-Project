from imdb import Cinemagoer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

"""
get ratings from movie reviews
"""

ia = Cinemagoer()

movie = ia.search_movie('The Dark Knight')[0]
# print(movie.movieID)

movie_reviews = ia.get_movie_reviews(movie.movieID)
review = movie_reviews['data']['reviews'][0]['content']
score = SentimentIntensityAnalyzer().polarity_scores(review)
print(score)