from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key="02c327faf5fe45cf982405221d456274")

# /v2/top-headlines for Babson College
# top_headlines = newsapi.get_top_headlines(q='Babson College',
#                                           category='business',
#                                           language='en',)

# /v2/everything
all_articles = newsapi.get_everything(
    q="Venture capital",
    from_param="2023-10-30",
    to="2023-10-30",
    language="en",
    sort_by="relevancy",
)

# /v2/top-headlines/sources
sources = newsapi.get_sources()

# Printing the results
# print(top_headlines)
# print(sources)
print(len(all_articles))
first_article = all_articles["articles"][0]
print(type(first_article))
print(first_article.keys())
first_content = first_article["content"]
print(type(first_content), len(first_content))

# for article in all_articles['articles']:
#     source_name = article['source']['name']
#     title = article['title']
#     author = article['author']
#     url = article['url']
#     published_at = article['publishedAt']
#     description = article['description']


#     print(f"Source: {source_name}")
#     print(f"Title: {title}")
#     print(f"Author: {author}")
#     print(f"URL: {url}")
#     print(f"Published At: {published_at}")
#     print(f"Description: {description}")
#     print("-" * 50)  # creates a line to separate the different news


# sentiment of vc description news or understand what are the top trends being talked about in the world of venture capital
