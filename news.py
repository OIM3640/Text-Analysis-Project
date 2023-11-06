import pprint
from newsapi import NewsApiClient
from config import NEWSAPI_KEY
newsapi = NewsApiClient(api_key = NEWSAPI_KEY)

pprint.pprint(newsapi.get_top_headlines())