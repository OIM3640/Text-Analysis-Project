from newspaper import Article
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentiment_analyzer = SentimentIntensityAnalyzer()


def article_function():

    """
    This function uses the newspaper3k abilities to essentially open up the article and
    present it in the output in a digestible way. I did this by creating an empty list and then
    reading each word and organizing the list by each word. However, I probably need to remove
    punctuation, whitespace, and turn everything into lowercase.

    """

    url = "https://apnews.com/article/lionel-messi-argentina-win-world-cup-final-against-france-e13fc1886725a0fe4f9e053e16a061bc"
    article = Article(url)
    article.download()
    article.parse()
    article_text = article.text

    messi_article_words = []
    for word in article_text.split():
        messi_article_words.append(word)

    return messi_article_words


def text_cleaning_dict():
    """
    This function removes dashes, spaces, and turns the words into lower case so that
    its easier to analyze the text because it is constant throughout. Then it creates a dictionary
    with the key and the value for each word. Got some of the code and formatting suggestions from chatGPT.

    """

    messi_article_words = article_function()
    dict = {}

    for word in messi_article_words:
        word = word.replace("-", " ")

        for i in word.split():
            word = word.lower()

            dict[word] = dict.get(word, 0) + 1

    return dict


def remove_stopwords():
    """
    This function uses the stopwords.txt to remove the words that are not neccesary so that
    our dictionary contains words that have meaning. Got some of the code and formatting suggestions from chatGPT.

    """

    best_list = []
    dict = text_cleaning_dict()

    with open("stopwords.txt", "r") as f:
        stopwords = f.read().splitlines()

    for word, frequency in dict.items():
        if word not in stopwords and word.isalnum():
            best_list.append((word, frequency))

    best_list = sorted(best_list)

    return best_list


def sentiment_analysis():
    """
    This function uses the NLP vaderSentiment package to output a polarity score analysis
    for the words in the article. I used this sentiment analysis to determine whether there was some sort of bias in the author. Got some of the code and formatting suggestions from chatGPT.
    """

    messi_article_words = remove_stopwords()

    pos_scores = []
    neg_scores = []
    neu_scores = []

    for word in messi_article_words:
        scores = sentiment_analyzer.polarity_scores(word[0])
        pos_scores.append(scores["pos"])
        neg_scores.append(scores["neg"])
        neu_scores.append(scores["neu"])

    avg_pos = sum(pos_scores) / len(pos_scores)
    avg_neg = sum(neg_scores) / len(neg_scores)
    avg_neu = sum(neu_scores) / len(neu_scores)

    print(
        f"The current sentiment in the Messi article is {round(avg_pos*100)}% positive, {round(avg_neg*100)}% negative, and {round(avg_neu*100)}% neutral"
    )


def main():

    sentiment_analysis()


if __name__ == "__main__":
    main()
