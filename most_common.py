from collections import Counter 
import re 
from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ia = Cinemagoer()
# search movie
movie = ia.search_movie("Frozen")[0]
movie_reviews = ia.get_movie_reviews(movie.movieID)['data']['reviews'][:10]

def count_words_frequency(text):

    positive_words = ['good', 'great', 'showstopping', 'excellent', 'breathtaking', 'fantastic', 'must watch']
    negative_words = ['lacking', 'poor', 'awful', 'worst', 'not recommend', 'bad', 'terrible']
    words = text.split()

    positive_count = sum( 1 for word in words if word in positive_words)
    negative_count = sum( 1 for word in words if word in negative_words)
    return positive_count, negative_count 

def analyze_reviews(movie_id, number_of_reviews):
    reviews = ia.get_movie_reviews(movie_id)['data']['reviews']
    reviews = reviews[:number_of_reviews]

    counts = [count_words_frequency(review['content']) for review in reviews]

    total_positive_count = sum(count[0] for count in counts)
    total_negative_count= sum(count[1] for count in counts)

    return total_positive_count, total_negative_count


movie_id = '0468569'
number_of_reviews = 10 
positive_count, negative_count = analyze_reviews(movie_id, number_of_reviews)

print(f'Total positive words: {positive_count}')
print(f'Total positive words: {negative_count}')


import matplotlib.pyplot as plt 


def plot_of_frequency(positive_count, negative_count):

    labels = ['Positive', 'Negative']
    data = [positive_count, negative_count]

    plt.bar(labels,data) 

    plt.title('Word Frequency in IMDB Reviews')
    plt.xlabel('Type of Review')
    plt.ylabel('Frequency')

    plt.show()

plot_of_frequency(positive_count, negative_count)