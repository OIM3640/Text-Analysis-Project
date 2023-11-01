from collections import Counter 
import re 
from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ia = Cinemagoer()
# search movie
movie = ia.search_movie("Frozen")[0]

def count_words_frequency(text):
    '''
    This function counts the positive and negative words in a text; based on a self created list.
    '''
    positive_words = ['good', 'great', 'showstopping', 'excellent', 'breathtaking', 'fantastic', 'must watch']
    negative_words = ['lacking', 'poor', 'awful', 'worst', 'not recommend', 'bad', 'terrible']
    words = text.split()
    #using the sum function to count the words 
    positive_count = sum( 1 for word in words if word in positive_words)
    negative_count = sum( 1 for word in words if word in negative_words)
    return positive_count, negative_count 

def analyze_reviews(movie_id, number_of_reviews):
    '''
    This function analyzes the reviews of a movie and uses the count_words_frequency 
    function to count the frequency of positive and negative words seen.
    '''
    reviews = ia.get_movie_reviews(movie_id)['data']['reviews']
    reviews = reviews[:number_of_reviews]

    counts = [count_words_frequency(review['content']) for review in reviews]
    #summing up the positive and negative words
    total_positive_count = sum(count[0] for count in counts)
    total_negative_count= sum(count[1] for count in counts)

    return total_positive_count, total_negative_count

movie_id = movie.movieID
number_of_reviews = 10 
positive_count, negative_count = analyze_reviews(movie_id, number_of_reviews)

print(f'Total positive words: {positive_count}')
print(f'Total negative words: {negative_count}')

