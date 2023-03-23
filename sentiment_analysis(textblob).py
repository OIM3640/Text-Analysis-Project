from textblob import TextBlob
import movie_reviews
import numpy as np
import matplotlib.pyplot as plt


def movie_sentiment_textblob(movie_name):
    """"""
    # Generate sentiment analysis for the reviews
    movie_review_content = movie_reviews.process_reviews(
        movie_name, exclude_stopwords=True
    )
    score_data = []
    for i in range(len(movie_review_content)):
        sentence = movie_review_content[i]
        sentiment = TextBlob(sentence).sentiment
        score_list = [sentiment.polarity, sentiment.subjectivity]
        score_data.append(score_list)

    # Convert the score_data to array
    score_array = np.array(score_data)

    # Calculate average
    average_score = np.mean(
        score_array, axis=0
    )  # axis=0 will compute the average of the columns

    return average_score


def sentiment_plot():
    """
    Plots the average sentiment scores of the three movies on a scatterplot.
    """
    creed1 = movie_sentiment_textblob("Creed (2015)").tolist()
    creed2 = movie_sentiment_textblob("Creed 2").tolist()
    creed3 = movie_sentiment_textblob("Creed 3").tolist()
    data = [creed1, creed2, creed3]

    # Extract values from data
    pol, sub = zip(*data)
    # Create plot
    plt.scatter(pol, sub)

    # Add labels and title to plot
    plt.xlabel("Polarity")
    plt.ylabel("Subjectivity")
    plt.title("Sentiment Analysis of Movies (Textblob)")

    # Lable the points
    for i, (pol, sub) in enumerate(data):
        plt.text(pol, sub, f"Creed {i+1}")

    # Show the plot
    plt.show()


def main():
    """
    This will be the entry function. All the test code goes here
    """
    # Creed 1
    creed1 = "Creed (2015)"
    creed1_scores = movie_sentiment_textblob(creed1)
    print(type(creed1_scores))
    print(
        f"The average sentiment score for Creed 1 is: \nPolarity: {creed1_scores[0]:.4f}, Subjectivity:{creed1_scores[1]:.4f}"
    )

    # Creed 2
    creed2 = "Creed 2"
    creed2_scores = movie_sentiment_textblob(creed2)
    print(
        f"The average sentiment score for Creed 2 is: \nPolarity: {creed2_scores[0]:.4f}, Subjectivity:{creed2_scores[1]:.4f}"
    )

    # Creed 3
    creed3 = "Creed 3"
    creed3_scores = movie_sentiment_textblob(creed3)
    print(
        f"The average sentiment score for Creed 3 is: \nPolarity: {creed3_scores[0]:.4f}, Subjectivity:{creed3_scores[1]:.4f}"
    )

    # Generate Scatterplot
    sentiment_plot()


if __name__ == "__main__":
    main()
