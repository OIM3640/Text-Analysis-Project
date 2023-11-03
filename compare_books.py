# Take three books (Frankenstein, The great Gatsby, and Little Women)
# Compare these three books by text similarity and by sentiment analysis to see which is more positive or negative

import book_analysis
import urllib.request
from nltk.sentiment.vader import SentimentIntensityAnalyzer

frankurl = 'https://www.gutenberg.org/files/84/84-0.txt'
with urllib.request.urlopen(frankurl) as f:
    franktext = f.read().decode('utf-8')[985:] # This is the index for the actual beginning of the book because the URL text is being read as a str.
# print(franktext)

gatsby = 'https://www.gutenberg.org/files/64317/64317-0.txt'
with urllib.request.urlopen(gatsby) as g:
    gatsbytext = g.read().decode('utf-8')[945:] # This is the index for the actual beginning of the book because the URL text is being read as a str.
# print(gatsbytext)

def sentiment_score(wordtuple):
    '''
    This function returns the average positive and negative sentiment score of a wordlist
    '''
    words = []
    for tuple in wordtuple:
        words.append(tuple[1])
    total_pos_score = 0
    total_neg_score = 0
    for word in words:
        score = SentimentIntensityAnalyzer().polarity_scores(word)
        pos_value = score['pos']
        total_pos_score += pos_value
        neg_value = score['neg']
        total_neg_score += neg_value
    avg_pos_score = total_pos_score/len(words)
    avg_neg_score = total_neg_score/len(words)
    return avg_pos_score, avg_neg_score

def compareresult(book1, book2, value1, value2, sentiment):
    '''
    This function prints the result for a comparison between sentiment scores for two books
    '''
    if value1 > value2:
        print(f"The book {book1} is more {sentiment} than {book2} by {value1 - value2}.")
    else:
        print(f"The book {book2} is more {sentiment} than {book1} by {value2 - value1}.")

def compare(tuple1, tuple2):
    '''
    This function separates values in tuples to specific variables and calls another function for comparison results.
    '''
    frank_pos = tuple1[0]
    frank_neg = tuple1[1]
    gatsby_pos = tuple2[0]
    gatsby_neg = tuple2[1]
    compareresult("Frankenstein", "The Great Gatsby", frank_pos, gatsby_pos, "positive")
    compareresult("Frankenstein", "The Great Gatsby", frank_neg, gatsby_neg, "negative")


def main():
    '''
    The following code is dedicated to the Frankenstein text.
    '''
    frank_wordlist = book_analysis.processtext(franktext)
    frank_hist = book_analysis.wordfreq(frank_wordlist)
    print(frank_hist)

    frank_common_list = book_analysis.common_words(frank_hist, num=100)
    print(frank_common_list)

    frank_scores = sentiment_score(frank_common_list)
    print(frank_scores)

    '''
    Ths following code is dedicated to the Gatsby text.
    '''
    gatsby_wordlist = book_analysis.processtext(gatsbytext)
    gatsby_hist = book_analysis.wordfreq(gatsby_wordlist)
    print(gatsby)

    gatsby_common_list = book_analysis.common_words(gatsby_hist, num=100)
    print(gatsby_common_list)

    gatsby_scores = sentiment_score(gatsby_common_list)
    print(gatsby_scores)

    '''
    The following code is used for comparison between the two books' sentiment scores. 
    '''
    compare(frank_scores, gatsby_scores)


if __name__ == "__main__":
    main()
