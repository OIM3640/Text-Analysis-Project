from nltk.sentiment.vader import SentimentIntensityAnalyzer
import part1 as p


def analyze_sentiment(sentence):
    """Used the given code. Returns the sentiment score for the phrase."""
    score = SentimentIntensityAnalyzer().polarity_scores(sentence)
    return score


def compare_sentiments(sentence_list):
    """Iterates analyze_sentiment() over a list of phrases. Creates and returns a dictionary where each phrase is numbered, based on the order of the original list, along with its sentiment score"""
    score_dict = {}
    for i in range(len(sentence_list)):
        score = analyze_sentiment(sentence_list[i])
        k = "Phrase " + str(i + 1)
        v = score
        score_dict[k] = v
    return score_dict


def find_most_pos(sentence_list):
    """This uses the dictionary created in compare_sentiments to find the phrase with the highest 'pos' score. I built on this a lot more for the next method so please look at that one."""
    phrases_analyzed = compare_sentiments(sentence_list)
    current_best = 0
    phrase_number = 0
    for i in range(len(phrases_analyzed.keys())):
        if current_best < phrases_analyzed["Phrase " + str(i + 1)]["pos"]:
            current_best = phrases_analyzed["Phrase " + str(i + 1)]["pos"]
            phrase_number = i + 1
    print(
        f"The most positive phrase out of this list was Phrase {phrase_number} with a score of {current_best}"
    )


def find_most_sentiment(sentence_list):
    """I'm pretty proud of this. First the user is asked which sentiment category it wants to know about. Then it checks to make sure that it is a valid input. If so, then it takes a list of phrases and, using the above methods, turns that list into a dicitonary where each phrase is coupled with its sentiment score. It then iterates over the phrases and compares the desired score with the next item's score. If the score is higher, it gets replaced. If not then it continues unchanged. Finally, after it has iterated over the entire dictionary, it prints the phrase number, the score category the user requested, and the actual score."""
    print("Which sentiment do you want know is the highest?")
    answer = input("Enter pos, neg, neu, or compound: ")
    # I used a website to refresh my memory on the error code
    # https://www.w3schools.com/python/python_try_except.asp
    if answer == "pos" or answer == "neu" or answer == "neg" or answer == "compound":
        phrases_analyzed = compare_sentiments(sentence_list)
        current_best = 0
        phrase_number = 0
        for i in range(len(phrases_analyzed.keys())):
            if current_best < phrases_analyzed["Phrase " + str(i + 1)][answer]:
                current_best = phrases_analyzed["Phrase " + str(i + 1)][answer]
                phrase_number = (
                    i + 1
                )  # Phrase numbers begin at 1 so they are 1 higher than their index
        if answer == "compound":
            print(
                f"The phrase with the highest compound score is Phrase {phrase_number} with a score of {current_best}"
            )
        else:
            print(
                f"The most {answer} phrase is Phrase {phrase_number} with a score of {current_best}"
            )
    else:
        raise Exception("That is an invalid sentiment category")


if __name__ == "__main__":
    from imdb import Cinemagoer

    a = "My roomate keeps eating my snacks!"
    b = "I love Professor Zhi"
    c = "I am so tired"
    sentence_list = [a, b, c]
    # find_most_pos(sentence_list)

    # create an instance of the Cinemagoer class
    ia = Cinemagoer()
    # search movie
    movie = ia.search_movie("The Wolf of Wall Street")[0]
    wolf_id = movie.movieID
    # '0993846'

    movie_reviews = ia.get_movie_reviews(wolf_id)
    review = movie_reviews["data"]["reviews"][0]["content"]
    # print(movie_reviews['data']['reviews'][2]['content'])

    wolf_list = []
    for i in range(7):
        wolf_list.append(movie_reviews["data"]["reviews"][i]["content"])
        # print(wolf_list[i])        # this is if you want to read the review
    find_most_sentiment(wolf_list)
