def main(title):
    """
    Predict movie rating from 0 to 10 stars
    """
    from imdb import Cinemagoer
    # create an instance of the Cinemagoer class
    ia = Cinemagoer()

    # search movie
    movie = ia.search_movie(title)[0]

    # Get reviews
    movie = ia.get_movie(movie.movieID, info=['reviews']) # Make sure to add the second argument
    reviews = movie.get('reviews', [])

    polarity = polarity_scores(reviews)

    avg_polarity = average_polarity_score(polarity)

    plot_points(avg_polarity, title)

    score = weighted_avg(avg_polarity)

    final_score = 5 + (score * 5)
    return f'I predict that {title} has {round(final_score, 1)} stars on IMDB.'


def polarity_scores(reviews):
    """
    Calculate sentiment polarity scores for reviews
    """
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    from nltk.tokenize import sent_tokenize
    score_storage = {}
    rev_count = 0

    for review in reviews:
        sent_count = 0
        rev_count += 1
        rev_key = f'Review_{rev_count}'
        review_scores = {}
        content = review.get('content', '')
        sentences = sent_tokenize(content)

        for sentence in sentences:
            sent_count += 1
            sent_key = f'Sentence_{sent_count}'
            score = SentimentIntensityAnalyzer().polarity_scores(sentence)
            sentiment = score['compound']
            if sentiment == 0:
                continue    # Restarts the for loop (ChatGPT)
            review_scores[sent_key] = sentiment
        score_storage[rev_key] = review_scores
    return score_storage


def average_polarity_score(polarity):
    """
    Calculate the average polarity score for each review
    """
    count = 0
    avg_score_storage = {}

    for review in polarity.values():    # Iterate out the embedded dictionaries (ChatGPT)
        count += 1
        key = f'Review_{count}'
        scores = list(review.values())
        avg_score = sum(scores) / len(scores)
        avg_score_storage[key] = avg_score
    return avg_score_storage


def plot_points(dictionary, title):
    """
    Create and display a plot of polarity scores for each review
    """
    import matplotlib.pyplot as plt     # Used matplotlib for code and info
    review_num = list(dictionary.keys())
    polarity = list(dictionary.values())
    header = f'{title} Reviews'

    plt.stem(review_num, polarity)
    plt.title(header)
    plt.xlabel('Reviews')
    plt.ylabel('Polarity')
    plt.xticks(rotation=90)     # Rotate x-axis tick labels vertically (ChatGPT)
    plt.show()


def weighted_avg(dictionary):
    """
    Calculate the weighted average of polarity scores
    """
    weighted_scores = []
    scores = list(dictionary.values())
    total = sum(scores)
    for number in scores:
        weight = number * (abs(number) / total)
        weighted_scores.append(weight)
    return sum(weighted_scores)


if __name__ == "__main__":
    print(main('La La Land'))
    print(main('Whiplash'))
    print(main('Foodfight!'))