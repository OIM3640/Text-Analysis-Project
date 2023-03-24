import nltk
from newsapi import NewsApiClient
from newspaper import Article
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def get_article_sentiment(query, source, api_key):
    # initialize NLTK's Vader module
    nltk.download('vader_lexicon')

    # initialize NewsApiClient with your API key
    newsapi = NewsApiClient(api_key=api_key)

    # set query parameters
    language = 'en'

    # get the latest article related to the query from the source
    articles = newsapi.get_everything(q=query, sources=source, language=language)

    # retrieve the URL of the first article in the response
    url = articles['articles'][0]['url']

    # create an Article object and download the article content
    article = Article(url)
    article.download()

    # parse the article content and extract the main text
    article.parse()
    text = article.text

    # perform sentiment analysis on the article text
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)

    # return the sentiment scores as a dictionary
    return score


api_key = 'a81a2f3a42104f77aa29a2cdd60a0623'
query = 'CPI'
source = 'bbc-news,the-verge'

score = get_article_sentiment(query, source, api_key)

print(score)
