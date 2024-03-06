from imdb import Cinemagoer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Create an instance of the Cinemagoer class
ia = Cinemagoer()

def get_actor(name):
    """Get actor id by name"""
    people = ia.search_person(name)
    for person in people:
        return person.personID

def get_films_by_actor(actor_id):
    """Return a list of movie ids"""
    person = ia.get_person(actor_id)
    actor_work = ia.get_person_filmography(actor_id)
    film_ids = []
    return film_ids

def get_combined_review(movie_id):
    """Get a combined review for a movie"""
    movie = ia.get_movie(movie_id, info=['reviews'])
    reviews = movie.get('reviews', [])
    combined_review = ""
    for review in reviews:
        combined_review += review['content'] + ' '  # Combine reviews with space in between
    return combined_review

def get_review_sentiment(review):
    """Create a polarity score of the reviews"""
    score = SentimentIntensityAnalyzer().polarity_scores(review)
    return score

def get_avg_sentiment(movie_id):
    """Get the average sentiment score for a movie"""
    combined_review = get_combined_review(movie_id)
    sentiment_score = get_review_sentiment(combined_review)
    return sentiment_score

import matplotlib.pyplot as plt

def main():
    actor_name = 'Matt Damon'
    actor_id = get_actor(actor_name)
    film_ids = get_films_by_actor(actor_id)
    
    movie_sentiments = {}
    
    for movie_id in film_ids:
        print(f"Processing movie ID: {movie_id}")
        sentiment_score = get_avg_sentiment(movie_id)
        movie_sentiments[movie_id] = sentiment_score
        print(f"Movie ID: {movie_id}, Sentiment Score: {sentiment_score}")

   
    movie_sentiments = {movie_id: sentiment_scores for movie_id, sentiment_scores in movie_sentiments.items() if sentiment_scores.get('pos', 0) > 0} #did this as movies with no reviews were skewing it with positivity scores of 0

    # Create a histogram with 0.01 intervals
    sentiment_values = [sentiment_scores.get('pos', 0) for sentiment_scores in movie_sentiments.values()]
    bins = [i/100 for i in range(101)]  

    plt.hist(sentiment_values, bins=bins, edgecolor='k')
    plt.xlabel('Positive Sentiment Score')
    plt.ylabel('Number of Movies')
    plt.title('Histogram of Positive Sentiment Scores')
    plt.show()

if __name__ == "__main__":
    main()


#Chat GPT Links
#https://chat.openai.com/share/a3e5a1d5-ae7a-453b-9bb2-c499144bdc0c
#https://chat.openai.com/share/45da1479-05c8-4cfa-80d2-20dfdad6f795