from imdb import Cinemagoer
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from fuzzywuzzy import fuzz
from nltk.corpus import stopwords
from collections import Counter

# Create an instance of the Cinemagoer class
ia = Cinemagoer()

# Download the VADER lexicon (if not already downloaded)
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('punkt')

# Create a SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Define a list of the top 10 movies of all time (you can add more)
top_10_movies = [
    "The Shawshank Redemption",
]

x = input("Enter the name of a movie: ")

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = nltk.word_tokenize(text)
    filtered_words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]
    return filtered_words

def movie_sentiment(movie_title):
    
    '''
    Analyzes sentiment and word frequency of reviews for a given movie.

    Parameters:
    - input: Title of the movie entered by the user.

    Functionality:
    1. Searches for the movie.
    2. Calculates sentiment polarity for each review.
    3. Computes average sentiment rating based on reviews and converts it to a 0-5 star rating. 
    4. Performs word frequency analysis on reviews.
    5. Displays the top 10 most common words and their frequencies.
    
    Prints:
    - 0-5 star rating, based on reviews alone. 
    - Top 10 most common words, with stopwords removed. 
    '''
    
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
    all_reviews_text = ""

    for review in reviews:
        review_content = review['content']
        all_reviews_text += review_content + " "
        sentiment = analyzer.polarity_scores(review_content)
        sentiment_polarity = sentiment['compound']
        total_sentiment += sentiment_polarity
        num_reviews += 1

    if num_reviews > 0:
        average_sentiment = total_sentiment / num_reviews

        # Convert sentiment from -1 to 1 to a 0 to 5 star scale
        average_sentiment_0_to_5 = (average_sentiment + 1) * 2.5

        # Round the average sentiment to two decimal places for star rating purposes. 
        average_sentiment_0_to_5 = round(average_sentiment_0_to_5, 2)

        print(f'Based on the written reviews, {best_match} is rated {average_sentiment_0_to_5} stars')

        # Word frequency analysis
        words = remove_stopwords(all_reviews_text)
        word_frequencies = Counter(words)

        # Display only the top 10 most common words
        top_words = word_frequencies.most_common(10)
        print("\nTop 10 Most Common Words:")
        for word, frequency in top_words:
            print(f"{word}: {frequency}")

    else:
        print(f'No reviews found for {movie_title}')


if __name__ == '__main__':
    movie_sentiment(x)
