from imdb import Cinemagoer
from textblob import TextBlob
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


# Download NLTK stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Function to preprocess a review
def preprocess_review(review):
    # Convert to lowercase
    review = review.lower()
    # Tokenize the text
    words = word_tokenize(review)
    # Remove stopwords and punctuation
    words = [word for word in words if word.isalnum() and word not in stop_words]
    return ' '.join(words)

# Function to perform sentiment analysis
def analyze_sentiment(review):
    analysis = TextBlob(review)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Main function to fetch movie reviews and perform sentiment analysis
def analyze_movie_reviews(movie_name):
    # Create an instance of the Cinemagoer class
    ia = Cinemagoer()

    # Search for the movie by name
    movies = ia.search_movie(movie_name)

    if not movies:
        print("Movie not found.")
        return

    movie = movies[0]

    # Get the Cinemagoer movie ID
    movie_id = movie.movieID

    # Get reviews for the movie
    movie = ia.get_movie(movie_id, info=['reviews'])
    reviews = movie.get('reviews', [])

    if not reviews:
        print("No reviews found for this movie.")
        return

    # Initialize counters for sentiment analysis
    positive_reviews_count = 0
    negative_reviews_count = 0
    total_reviews_count = 0

    for review in reviews:
        content = review['content']
        preprocessed_review = preprocess_review(content)
        sentiment = analyze_sentiment(preprocessed_review)

        if sentiment == 'Positive':
            positive_reviews_count += 1
        elif sentiment == 'Negative':
            negative_reviews_count += 1

        total_reviews_count += 1

        print("Review:")
        print(content)
        print("Sentiment:", sentiment)
        print()

    # Display sentiment statistics
    print("Positive Reviews:", positive_reviews_count)
    print("Negative Reviews:", negative_reviews_count)
    print("Total Reviews:", total_reviews_count)

# User input for the movie name
movie_name = input("Enter the name of a movie: ")
analyze_movie_reviews(movie_name)

