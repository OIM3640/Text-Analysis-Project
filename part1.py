# ### Part 1: Harvesting text from internet ###

# ## Gutenberg ##
# # download text (oliver twist)
# import urllib.request

# url = "https://www.gutenberg.org/cache/epub/730/pg730.txt"
# with urllib.request.urlopen(url) as f:
#     text = f.read().decode("utf-8")
#     # print(text)  # for testing


# ## Wikipedia ##
# from mediawiki import MediaWiki

# wikipedia = MediaWiki()
# babson = wikipedia.page("Babson College")
# print(babson.title)
# print(babson.content)


# ## Twitter ##
# import tweepy

# # I don't have twitter so I will pass the testing for twitter #

# # TOKEN = 'Your TOKEN'
# # TOKEN_SECRET = 'Your TOKEN_SECRET'
# # CONSUMER_KEY = 'Your CONSUMER_KEY'
# # CONSUMER_SECRET = 'Your CONSUMER_SECRET'

# # # Authenticate to Twitter
# # auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# # auth.set_access_token(TOKEN,TOKEN_SECRET)

# # api = tweepy.API(auth)

# # for tweet in api.search_tweets(q="babson college", lang="en", count=10):
# #     print(f"{tweet.user.name}: {tweet.text}")


# ## Reddit ##
# import praw

# # import config

# # reddit = praw.Reddit(client_id=config.client_id,
# #                      client_secret=config.client_secret,
# #                      username=config.username,
# #                      password=config.password,
# #                      user_agent=config.user_agent)

# # sub = 'learnpython'
# # submissions = reddit.subreddit(sub).top('day', limit=5)
# # for submission in submissions:
# #     print(submission.title)
# #     print(submission.selftext)

# ## News API ##
# from newsapi import NewsApiClient

# # # Init
# # newsapi = NewsApiClient(api_key="733687fa26774696a08acddb45d7e8cb")

# # # /v2/top-headlines
# # top_headlines = newsapi.get_top_headlines(
# #     q="bitcoin",
# #     sources="bbc-news,the-verge",
# #     category="business",
# #     language="en",
# #     country="us",
# # )

# # # /v2/everything
# # all_articles = newsapi.get_everything(
# #     q="bitcoin",
# #     sources="bbc-news,the-verge",
# #     domains="bbc.co.uk,techcrunch.com",
# #     from_param="2017-12-01",
# #     to="2017-12-12",
# #     language="en",
# #     sort_by="relevancy",
# #     page=2,
# # )

# # # /v2/top-headlines/sources
# # sources = newsapi.get_sources()


# ## Newspaper Articles ##
# from newspaper import Article

# url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
# article = Article(url)
# article.download()
# article.parse()
# article_text = article.text
# print(article_text) # Output: Washington (CNN) -- Not everyone subscribes to a New Year's resolution...


# ## IMDB Movie Reviews ##
# from imdb import Cinemagoer

# # create an instance of the Cinemagoer class
# ia = Cinemagoer()

# # search movie
# movie = ia.search_movie("The Dark Knight")[0]
# print(movie.movieID)
# # '0468569'

# # Get reviews
# movie = ia.get_movie('0468569', info=['reviews']) # Make sure to add the second argument
# reviews = movie.get('reviews', [])

# for review in reviews:
#     print(review['content'])
#     print()


# # Get actor
# matt_damon = ia.get_person_filmography('0000354')

# # Get Matt Damon's movies
# data = matt_damon['data']
# filmography = data['filmography']
# films_as_actor = filmography['actor']
# print(films_as_actor)


## Pickling Data ##
import pickle

# Save data to a file (will be part of your data fetching script)

with open("dickens_texts.pkl", "w") as f:
    pickle.dump(charles_dickens_texts, f)


# Load data from a file (will be part of your data processing script)
with open("dickens_texts.pkl", "r") as f:
    reloaded_copy_of_texts = pickle.load(f)

# X pickle and then unpickle in the same Python script
