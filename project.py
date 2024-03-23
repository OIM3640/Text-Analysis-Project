from imdb import Cinemagoer
import markovify
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from openai import OpenAI

client = OpenAI()

# The goal is to analyze existing reviews of Avengers: Endgame and generate similar reviews using Markov generation and openai API. Followed by using nltk sentiment analysis to check the similarity of the generated review sentiments to the original reviews.


def markov_review_generator(
    text,
):  # function to generate 6 sentence reviews using Markov chains
    """This function takes input text and uses the markovify library to generate similar text with a length of 6 sentences. It returns the 6 sentences as a block of text. This function is used to generate reviews."""
    generator = markovify.Text(text)

    sentences = ""
    for i in range(6):
        sentence = str(generator.make_sentence())
        sentences += sentence

    return sentences


def openai_review_generator(prompt):
    """This function uses the openai API to generate text. It takes a text input as a prompt and it returns the resulting generated block of text. This function is used to generate reviews."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content


def average_sentiment_scorer(
    scores,
):  # Used Gemini to figure out how to calculate average sentiment scores
    """This function takes a list of sentiment scores as an input and calculates the average positive, negative, neutral and compound sentiment scores. It returns those four values."""

    total_pos_score = 0
    total_neu_score = 0
    total_neg_score = 0
    total_comp_score = 0
    num_scores = len(scores)  # Denominator to calculate average
    for score in scores:
        total_pos_score += score["pos"]
        total_neu_score += score["neu"]
        total_neg_score += score["neg"]
        total_comp_score += score["compound"]

    avg_pos = total_pos_score / num_scores
    avg_neu = total_neu_score / num_scores
    avg_neg = total_neg_score / num_scores
    avg_comp = total_comp_score / num_scores

    return f"The average sentiment score of the reviews is a{avg_pos: .3f} positive score, a{avg_neu: .3f} neutral score, a{avg_neg: .3f} negative score and a{avg_comp: .3f} compound score."  # Summarized average scores


def markov_reviews(text):
    """This function generates 25 movie reviews using Markov chains and calculates the average sentiment score of the reviews. It prints a summary of the reviews as well as the average sentiment score. It takes a text as an input to use as a corpus."""
    generated_reviews = []
    for i in range(25):
        new_review = markov_review_generator(text)
        generated_reviews.append(
            new_review
        )  # Generates 25 reviews and adds them to the list

    markov_sentiment_scores = []
    for review in generated_reviews:
        score2 = SentimentIntensityAnalyzer().polarity_scores(review)
        markov_sentiment_scores.append(score2)  # Scores each review individually

    markov_sentiment = average_sentiment_scorer(
        markov_sentiment_scores
    )  # Calculates the average sentiment score of the reviews

    print(
        "The Markov generated reviews are as follows: "
    )  # Outputting reviews and scores
    for item in generated_reviews:
        print(item + "\n\n")

    print(
        f"There are {len(generated_reviews)} Markov generated reviews in the list. {markov_sentiment}"
    )


def gpt_reviews():
    """This function generates 25 movie reviews using the openai API and calculates the average sentiment score of the reviews. It prints a summary of the reviews as well as the average sentiment score."""
    gpt_reviews = []
    for i in range(25):
        new_gpt_review = openai_review_generator("Write a review for Avengers: Endgame")
        gpt_reviews.append(
            new_gpt_review
        )  # Generates 25 reviews and adds them to the list

    gpt_sentiment_scores = []
    for review in gpt_reviews:
        score3 = SentimentIntensityAnalyzer().polarity_scores(review)
        gpt_sentiment_scores.append(score3)  # Scores each review individually

    gpt_sentiment = average_sentiment_scorer(
        gpt_sentiment_scores
    )  # Calculates the average sentiment score of the reviews

    print("The GPT generated reviews are as follows: ")  # Outputting reviews and scores
    for item in gpt_reviews:
        print(item + "\n\n")

    print(
        f"There are {len(gpt_reviews)} GPT generated reviews in the list. {gpt_sentiment}"
    )


def main():
    """Main function of the project - this function sources and stores reviews from IMDB and calculates the sentiment scores before calling helper functions to generate new reviews and score them."""
    ia = Cinemagoer()

    id = ia.search_movie("Avengers: Endgame")[0]
    movie = ia.get_movie(id.movieID, info=["reviews"])
    reviews = movie.get("reviews", [])

    review_text = []
    for review in reviews:
        review_text.append(
            review["content"]
        )  # Sourcing and separating reviews, storing them in a list

    sentiment_scores = []
    for review in review_text:
        score1 = SentimentIntensityAnalyzer().polarity_scores(review)
        sentiment_scores.append(score1)  # Calculating sentiment score of each review

    review_sentiment = average_sentiment_scorer(
        sentiment_scores
    )  # Calculate average sentiment score

    print(f"There are {len(review_text)} reviews in the list. {review_sentiment}")

    print("The reviews are as follows: ")  # Outputting reviews and scores
    for item in review_text:
        print(item + "\n\n")

    markov_reviews(review_text)

    gpt_reviews()


if __name__ == "__main__":
    main()
