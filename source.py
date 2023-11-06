from imdb import Cinemagoer
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from fuzzywuzzy import fuzz

# Create an instance of the Cinemagoer class
ia = Cinemagoer()

# Download the VADER lexicon (if not already downloaded)
nltk.download('vader_lexicon')

# Create a SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Define a list of the top 10 movies of all time (you can add more)
top_10_movies = [
    "The Shawshank Redemption",
]

x = input("Enter the name of a movie: ")

def movie_sentiment(movie_title):
    
    
    
    # Search for the movie
    movie_search_result = ia.search_movie(movie_title)

    # Check if any movie was found
    if not movie_search_result:
        print(f"Movie '{movie_title}' does not exist.")
        return

    # Calculate the similarity between the user's input and the titles in the search result
    similarity_threshold = 60
    best_match = max(movie_search_result, key=lambda movie: fuzz.partial_ratio(movie_title, movie['title']))

    if fuzz.partial_ratio(movie_title, best_match['title']) < similarity_threshold:
        print(f"Movie '{movie_title}' does not exist.")
        return

    # Use the best match found
    movie_id = best_match.movieID

    # Get reviews
    movie = ia.get_movie(movie_id, info=['reviews'])
    reviews = movie.get('reviews', [])

    total_sentiment = 0
    num_reviews = 0

    for review in reviews:
        review_content = review['content']
        sentiment = analyzer.polarity_scores(review_content)
        sentiment_polarity = sentiment['compound']
        total_sentiment += sentiment_polarity
        num_reviews += 1

    if num_reviews > 0:
        average_sentiment = total_sentiment / num_reviews

        # Convert sentiment from -1 to 1 to a 0 to 5 scale
        average_sentiment_0_to_5 = (average_sentiment + 1) * 2.5

        # Round the average sentiment to two decimal places
        average_sentiment_0_to_5 = round(average_sentiment_0_to_5, 2)

        print(f'Based on the written reviews, {best_match} is rated {average_sentiment_0_to_5} stars')
    else:
        print(f'No reviews found for {movie_title}')


if __name__ == '__main__':
    movie_sentiment(x)


