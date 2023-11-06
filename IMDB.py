from imdb import Cinemagoer
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# * Objective: Compare popular movie series's based on overall movie sentiment to find the most
# * family friendly option for movie night

ia = Cinemagoer()  # open the movie database

# Gathering Harry Potter Movie Data for IMDB reviews and ratings
hp1 = ia.get_movie("0241527", info=["reviews"])
hp2 = ia.get_movie("0295297", info=["reviews"])
hp3 = ia.get_movie("0304141", info=["reviews"])
hp4 = ia.get_movie("0330373", info=["reviews"])
hp5 = ia.get_movie("0373889", info=["reviews"])
hp6 = ia.get_movie("0417741", info=["reviews"])
hp7 = ia.get_movie("0926084", info=["reviews"])
hp8 = ia.get_movie("1201607", info=["reviews"])

hp1r = ia.get_movie("0241527")
hp2r = ia.get_movie("0295297")
hp3r = ia.get_movie("0304141")
hp4r = ia.get_movie("0330373")
hp5r = ia.get_movie("0373889")
hp6r = ia.get_movie("0417741")
hp7r = ia.get_movie("0926084")
hp8r = ia.get_movie("1201607")

"""
I tried using ChatGPT to find a way to pull the harry potter movie info into a dictionary containing
the movie title as the key and movie ID as the value to make this data aggregation scalable. It
recommended using the (re) library but it caused errors when I tried it so I just entered the info
manually :P
"""


def get_info(movie, info="reviews"):
    """
    collects movie info (default = reviews)
    """
    return movie.get(info, [])


def get_review_content(movie):
    """
    Returns the reviews for a specified movie
    """
    for review in movie:
        return review["content"]


hp1r = get_info(hp1r, "rating")
hp2r = get_info(hp2r, "rating")
hp3r = get_info(hp3r, "rating")
hp4r = get_info(hp4r, "rating")
hp5r = get_info(hp5r, "rating")
hp6r = get_info(hp6r, "rating")
hp7r = get_info(hp7r, "rating")
hp8r = get_info(hp8r, "rating")

hp1 = get_info(hp1)
hp2 = get_info(hp2)
hp3 = get_info(hp3)
hp4 = get_info(hp4)
hp5 = get_info(hp5)
hp6 = get_info(hp6)
hp7 = get_info(hp7)
hp8 = get_info(hp8)

# First rank all the Harry Potter Movies based on their actual IMDB Ratings
harry_potter_ranking = [
    (hp1r, "Harry Potter #1"),
    (hp2r, "Harry Potter #2"),
    (hp3r, "Harry Potter #3"),
    (hp4r, "Harry Potter #4"),
    (hp5r, "Harry Potter #5"),
    (hp6r, "Harry Potter #6"),
    (hp7r, "Harry Potter #7"),
    (hp8r, "Harry Potter #8"),
]
harry_potter_ranking = sorted(harry_potter_ranking, key=lambda a: a[0], reverse=True)

# Next execute sentiment analysis for the IMDB reviews for each Harry Potter Movie
hp1_score = SentimentIntensityAnalyzer().polarity_scores(get_review_content(hp1))
hp2_score = SentimentIntensityAnalyzer().polarity_scores(get_review_content(hp2))
hp3_score = SentimentIntensityAnalyzer().polarity_scores(get_review_content(hp3))
hp4_score = SentimentIntensityAnalyzer().polarity_scores(get_review_content(hp4))
hp5_score = SentimentIntensityAnalyzer().polarity_scores(get_review_content(hp5))
hp6_score = SentimentIntensityAnalyzer().polarity_scores(get_review_content(hp6))
hp7_score = SentimentIntensityAnalyzer().polarity_scores(get_review_content(hp7))
hp8_score = SentimentIntensityAnalyzer().polarity_scores(get_review_content(hp8))


# Delete unnecessary dict item
def del_dict_item(dict, item="compound"):
    """
    Removes the "compound" key from a dictionary
    """
    del dict["compound"]
    return dict


hp1_score = del_dict_item(hp1_score)
hp2_score = del_dict_item(hp2_score)
hp3_score = del_dict_item(hp3_score)
hp4_score = del_dict_item(hp4_score)
hp5_score = del_dict_item(hp5_score)
hp6_score = del_dict_item(hp6_score)
hp7_score = del_dict_item(hp7_score)
hp8_score = del_dict_item(hp8_score)

# Add titles
hp1_score["title"] = "Harry Potter #1"
hp2_score["title"] = "Harry Potter #2"
hp3_score["title"] = "Harry Potter #3"
hp4_score["title"] = "Harry Potter #4"
hp5_score["title"] = "Harry Potter #5"
hp6_score["title"] = "Harry Potter #6"
hp7_score["title"] = "Harry Potter #7"
hp8_score["title"] = "Harry Potter #8"

harry_potter = [
    hp1_score,
    hp2_score,
    hp3_score,
    hp4_score,
    hp5_score,
    hp6_score,
    hp7_score,
    hp8_score,
]

# Sort movies in decending order based on each sentiment score
harry_potter = sorted(harry_potter, key=lambda a: a["neg"])

hp_reviews_neg = {}
hp_reviews_neg["Rank 1"] = harry_potter[0]["title"]
hp_reviews_neg["Rank 2"] = harry_potter[1]["title"]
hp_reviews_neg["Rank 3"] = harry_potter[2]["title"]
hp_reviews_neg["Rank 4"] = harry_potter[3]["title"]
hp_reviews_neg["Rank 5"] = harry_potter[4]["title"]
hp_reviews_neg["Rank 6"] = harry_potter[-3]["title"]
hp_reviews_neg["Rank 7"] = harry_potter[-2]["title"]
hp_reviews_neg["Rank 8"] = harry_potter[-1]["title"]

harry_potter = sorted(harry_potter, key=lambda a: a["neu"], reverse=True)

hp_reviews_neu = {}
hp_reviews_neu["Rank 1"] = harry_potter[0]["title"]
hp_reviews_neu["Rank 2"] = harry_potter[1]["title"]
hp_reviews_neu["Rank 3"] = harry_potter[2]["title"]
hp_reviews_neu["Rank 4"] = harry_potter[3]["title"]
hp_reviews_neu["Rank 5"] = harry_potter[4]["title"]
hp_reviews_neu["Rank 6"] = harry_potter[-3]["title"]
hp_reviews_neu["Rank 7"] = harry_potter[-2]["title"]
hp_reviews_neu["Rank 8"] = harry_potter[-1]["title"]

harry_potter = sorted(harry_potter, key=lambda a: a["pos"], reverse=True)

hp_reviews_pos = {}
hp_reviews_pos["Rank 1"] = harry_potter[0]["title"]
hp_reviews_pos["Rank 2"] = harry_potter[1]["title"]
hp_reviews_pos["Rank 3"] = harry_potter[2]["title"]
hp_reviews_pos["Rank 4"] = harry_potter[3]["title"]
hp_reviews_pos["Rank 5"] = harry_potter[4]["title"]
hp_reviews_pos["Rank 6"] = harry_potter[-3]["title"]
hp_reviews_pos["Rank 7"] = harry_potter[-2]["title"]
hp_reviews_pos["Rank 8"] = harry_potter[-1]["title"]


# Print Comparison Report
def main():
    print(
        "\nHarry Potter Movies Actual Rankings vs Natural Language Processing Rankings of Review Sentiments:\n"
        "\nActual IMDB Ranking:        Positive Review Sentiment Ranking:        Negative Review Sentiment Ranking (least):\n"
        f"  {harry_potter_ranking[0][1]}                     {hp_reviews_pos['Rank 1']}                             {hp_reviews_neg['Rank 1']}\n"
        f"  {harry_potter_ranking[1][1]}                     {hp_reviews_pos['Rank 2']}                             {hp_reviews_neg['Rank 2']}\n"
        f"  {harry_potter_ranking[2][1]}                     {hp_reviews_pos['Rank 3']}                             {hp_reviews_neg['Rank 3']}\n"
        f"  {harry_potter_ranking[3][1]}                     {hp_reviews_pos['Rank 4']}                             {hp_reviews_neg['Rank 4']}\n"
        f"  {harry_potter_ranking[4][1]}                     {hp_reviews_pos['Rank 5']}                             {hp_reviews_neg['Rank 5']}\n"
        f"  {harry_potter_ranking[-3][1]}                     {hp_reviews_pos['Rank 6']}                             {hp_reviews_neg['Rank 6']}\n"
        f"  {harry_potter_ranking[-2][1]}                     {hp_reviews_pos['Rank 7']}                             {hp_reviews_neg['Rank 7']}\n"
        f"  {harry_potter_ranking[-1][1]}                     {hp_reviews_pos['Rank 8']}                             {hp_reviews_neg['Rank 8']}\n"
    )


if __name__ == "__main__":
    main()
