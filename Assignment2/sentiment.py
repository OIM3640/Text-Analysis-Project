from newsapi import NewsApiClient
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download("vader_lexicon")

# Init
newsapi = NewsApiClient(api_key="02c327faf5fe45cf982405221d456274")

sid = SentimentIntensityAnalyzer() 

# /v2/top-headlines for Babson College
# top_headlines = newsapi.get_top_headlines(q='Babson College',
#                                           category='business',
#                                           language='en',)

keywords = [''] #do a for loop for keywords, also search in multiple days
# /v2/everything
all_articles = newsapi.get_everything(
    q="Venture capital",
    from_param="2023-10-30",
    to="2023-11-30",
    language="en",
    sort_by="relevancy",
    page=2,
)

# /v2/top-headlines/sources
sources = newsapi.get_sources()

# Printing the results
# print(top_headlines)
print(sources)
print(all_articles)

for article in all_articles["articles"]:
    source_name = article["source"]["name"]
    title = article["title"]
    author = article["author"]
    url = article["url"]
    published_at = article["publishedAt"]
    description = article["description"]

#wrapped into function
def get_sentiment(description):
    if (description and description.strip()):  # Check if the description exists and is not empty
        score = sid.polarity_scores(
            description
        )  # Compute the sentiment score for the article's description
        sentiment = f"Sentiment: {score}"
    else:
        sentiment = "Sentiment: No description available"


    print(f"Source: {source_name}")
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"URL: {url}")
    print(f"Published At: {published_at}")
    print(f"Description: {description}")
    print(sentiment)
    print("-" * 50)  # creates a line to separate the different news

# Understand sentiment score in VC world per article description. Understand what are the top trends being talked about in the world of venture capital
# do word frequency
# run through multiple dates, expand range