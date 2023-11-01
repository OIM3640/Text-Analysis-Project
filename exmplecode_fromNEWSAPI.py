from newsapi import NewsApiClient

from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='95b99711861949b2afde929a0debf89f')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          category='business',
                                          language='en',
                                          country='us')


# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2023-03-22',
                                      to='2023-02-21',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/top-headlines/sources
sources = newsapi.get_sources()

#print(top_headlines)
print(all_articles)