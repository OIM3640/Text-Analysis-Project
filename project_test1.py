from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='a81a2f3a42104f77aa29a2cdd60a0623')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          language='en')

print("Top Headlines:")
for i, article in enumerate(top_headlines['articles']):
    print(f"{i + 1}. {article['title']} - {article['source']['name']}")

# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

print("\nAll Articles:")
for i, article in enumerate(all_articles['articles']):
    print(f"{i + 1}. {article['title']} - {article['source']['name']}")

# /v2/top-headlines/sources
sources = newsapi.get_sources

print(all_articles)