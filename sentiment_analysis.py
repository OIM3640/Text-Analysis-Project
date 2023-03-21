from nltk.sentiment.vader import SentimentIntensityAnalyzer
import movie_reviews
import numpy as np


def movie_sentiment(movie_name):
    """
    Generates the sentiment scores for the reviews extracted in file 'movie_reviews', creates a list with all the sentiment scores, and returns the average score for each category.
    """
    # Generate sentiment analysis for the reviews
    movie_review_content = movie_reviews.process_reviews(
        movie_name, exclude_stopwords=True
    )
    score_data = []
    for i in range(len(movie_review_content)):
        sentence = movie_review_content[i]
        score = SentimentIntensityAnalyzer().polarity_scores(sentence)
        score_list = list(score.values())
        score_data.append(score_list)

    # Convert the score_data to array
    score_array = np.array(score_data)

    # Calculate average
    average_score = np.mean(score_array, axis=0) # axis=0 will compute the average of the columns

    return average_score


def main():
    """
    This will be the entry function. All the test code goes here
    """
    # Creed 1
    creed1 = "Creed (2015)"
    creed1_scores = movie_sentiment(creed1)
    print(
        f"The average sentimental score for Creed 1 is: \nNegative: {creed1_scores[0]:.4f}, Neutral:{creed1_scores[1]:.4f}, Positive: {creed1_scores[2]:.4f}, Compound: {creed1_scores[3]:.4f}"
    )

    # Creed 2
    creed2 = "Creed 2"
    creed2_scores = movie_sentiment(creed2)
    print(
        f"The average sentimental score for Creed 2 is: \nNegative: {creed2_scores[0]:.4f}, Neutral:{creed2_scores[1]:.4f}, Positive: {creed2_scores[2]:.4f}, Compound: {creed2_scores[3]:.4f}"
    )

    # Creed 3
    creed3 = "Creed 3"
    creed3_scores = movie_sentiment(creed3)
    print(
        f"The average sentimental score for Creed 3 is: \nNegative: {creed3_scores[0]:.4f}, Neutral:{creed3_scores[1]:.4f}, Positive: {creed3_scores[2]:.4f}, Compound: {creed3_scores[3]:.4f}"
    )


if __name__ == "__main__":
    main()
