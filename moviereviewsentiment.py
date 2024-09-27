from imdb import Cinemagoer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

"""
get ratings from movie reviews
"""


def paragraph_sentiment(par):
    """
    returns the average sentiment compound of each sentence in a paragraph
    """
    scores_list = []
    # split paragraph by sentence
    punctuation = '.?!'
    for i in punctuation:
        par = par.replace()
    print(par)

    for sentence in par:
        if len(sentence) > 2:
            score = SentimentIntensityAnalyzer().polarity_scores(sentence)
            print(score)
            scores_list.append(score['compound'])
    print(scores_list)

    sum_scores = 0
    for sentence in scores_list:
        sum_scores += sentence
    
    average_score = sum_scores/len(scores_list)
    return average_score
    pass

print(paragraph_sentiment('I am very happy with your work. It came out great. Looking forward to the next one!'))


