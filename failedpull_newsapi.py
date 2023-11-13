import config
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key = config.apikey_newsapi)

top_headlines = newsapi.get_top_headlines(
    q=f'{config.company_query} news',
    category = 'business',
)

all_articles = newsapi.get_everything(
    q=f'{config.company_query} news',
    sort_by='relevancy'
)

print(top_headlines, all_articles)