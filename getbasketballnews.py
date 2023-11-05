import pprint
from newsapi import NewsApiClient
from config import NEWSAPI_KEY
newsapi = NewsApiClient(api_key = NEWSAPI_KEY)

"""
get US basketball news related to certain player, team, or keywords 
"""

# filter out all non-US news
us_sources = newsapi.get_sources(country = 'us')
# print(sources)

def get_category_sources(category):
    """
    helper function that returns a string of ids for all sources in a certain category
    """
    categorized_sources = []
    for s in us_sources['sources']:
        if s['category'] == category:
            categorized_sources.append(s['id'])
    categorized_sources = ','.join(categorized_sources)
    return categorized_sources
# print(get_category_sources('sports'))

# articles = newsapi.get_everything(sources = get_category_sources('sports'))
# pprint.pprint(articles)

def get_sports_news(keyword=' '):
    """
    get sports news on a certain string keyword (i.e. team, player, league, etc.), assumes proper punctuation
    """
    news_list = []
    keywords = keyword.split()
    articles_dict = newsapi.get_everything(sources = get_category_sources('sports'))
    articles_list = articles_dict['articles']

    # pprint.pprint(articles_list)
    for key in keywords:
        for article in articles_list:
            text = article['content'] + article['description'] + article['title']
            if key in text and article not in news_list:
                news_list.append(article)
    return news_list




def main():
    player = 'Lebron'
    news = get_sports_news(player)
    pprint.pprint(news)


if __name__ == "__main__":
    main()