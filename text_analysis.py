

def news_article_headlines():

    from newsapi import NewsApiClient

    import requests
    url = ('https://newsapi.org/v2/top-headlines?'
        'country=us&'
        'apiKey=12bcd741cfe7426ea4df9c970e781394')
    response = requests.get(url)
    #Code is from NewsAPI website
    #https://newsapi.org/docs/get-started#top-headlines

    a = response.json()
    #print(a)

    headlines = []

    for i in a["articles"]:
        headlines.append(i["title"])

    print(headlines)

def headlines_sentiment():
    
    from nltk.sentiment.vader import SentimentIntensityAnalyzer

def main():
    print(news_article_headlines())
    
if __name__ == "__main__":
    main()