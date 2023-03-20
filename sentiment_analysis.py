from nltk.sentiment.vader import SentimentIntensityAnalyzer
import movie_reviews


def movie_sentiment(movie_name):
    """ """
    # Headers
    print(f"{'Negative':<10} {'Neutral':<10} {'Positive':<10} {'Compound':<10}")
    print(f"{'-'*45}")

    # Generate sentiment analysis for the first 5 reviews
    movie_review_content = movie_reviews.get_reviews(movie_name)
    for i in range(5):
        sentence = movie_review_content[i]
        score = SentimentIntensityAnalyzer().polarity_scores(sentence)
        print(
            f"{score['neg']:<10} {score['neu']:<10} {score['pos']:<10} {score['compound']:<10}"
        )


def main():
    """
    This will be the entry function. All the test code goes here
    """
    # Creed 1
    creed1 = 'Creed (2015)'
    print('The sentimental analysis for Creed 1 is: ')
    movie_sentiment(creed1)

    #Creed 2
    creed2 = 'Creed 2'
    print('The sentimental analysis for Creed 2 is: ')
    movie_sentiment(creed2)

    # Creed 3
    creed3 = 'Creed 3'
    print('The sentimental analysis for Creed 3 is: ')
    movie_sentiment(creed3)


if __name__ == "__main__":
    main()
