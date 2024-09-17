# Text Analysis Project
 
## Introduction

In this project, you will learn how to use computational techniques to analyze text. You will access text from a variety of sources, including websites and APIs, and run computational analyses to create some sort of deliverable, such as interesting results from a text analysis, a visualization, or even a Python program that manipulates language in some interesting way. As part of the project, you are encouraged to use ChatGPT to explore how to talk to APIs and how to use Python libraries that have not been covered in class yet. This assignment is an **individual project**. 

**Skills Emphasized**:

- Accessing data programmatically from various sources on the Internet
- Parsing text and storing it in appropriate data structures
- Selecting the most suitable data structures for a specific task (e.g. dictionaries versus lists)
- Applying computational methods to analyze, characterize, and compare text
- Experimenting with ChatGPT, an AI assistant, to enhance the learning process and explore new tools and techniques.

---
## How to Proceed

To get started on the assignment, you should **fork** this base repository. Once you've forked the repository, **clone** the **forked** repository (the one under your GitHub profile) to your computer. You need to create one or multiple `.py` files in the **forked** repository.

You should read this document in a somewhat non-linear/spiral fashion:

1. Scan through Part 1 to get a sense of what data sources are available. You can select a source that interests you and try to retrieve text from it. Note that you do not need to try all the data sources.
2. Scan through Part 2 to see a bunch of cool examples for what you can do with your text. You can also ask ChatGPT what else you can do with Python to process, analyze or visulize text.
3. Choose (at least) one data source from Part 1 and apply techniques from Part 2 or elsewhere to analyze, manipulate or transform the text. 
4. Use the `if __name__ == "__main__"` idiom in the `.py` file (or the entry `.py` file if you create multiple `.py` files). In other words, your code should be executed when the entry Python file is run.
    ```python
    if __name__ == "__main__":
        main()
    ```
5. You are ~~encouraged~~ required to experiment with learning from ChatGPT (see more in Part 3).
6. Write a brief document (Part 4) describing what you did.
7. If you use any code that is not written by you (or that you learned from other places such as StackOverFlow/GitHub), please add Python comments (before the block of code) describing where you got/learned it from.
8. Overall, I don't recommend using `numpy`, `pandas`, `sklearn` or `matplotlib` in this project, unless there is no other alternative way of processing and analyazing your data.

---

## Part 1: Harvesting text from the Internet

The goal for Part 1 is to collect some text from the Internet that you can later use for text analysis.  Before diving deep into any particular method of text acquisition, it is recommended that you explore the different APIs and Python libraries available to extract text from the web. However, before spending too much time going down a particular path on the text acquisition component, you should look ahead to Part 2 to understand some of the things you can do with text you are harvesting. The key to a successful project is combining a relevant source of text with an appropriate technique for analysis (see Part 2).

### Data Source: Project Gutenberg

Project Gutenberg (http://www.gutenberg.org/) is a website that provides over 55,000 e-books that are freely available to the public. Unlike some sites, all of the texts on Project Gutenberg are in the public domain, which means they are no longer protected by copyright. For example, the site offers 171 works by Charles Dickens. The best thing about these texts is that they are available in plain text format, which makes them easy to analyze using Python.

To download a book from Project Gutenberg, first use the search engine on the Project Gutenberg website to find a book you are interested in downloading. For example, if you want to download O*liver Twist* by Charles Dickens, search for it on the website. Once you have found the book you want to download, go to its page on the Project Gutenberg website. Find the "Plain Text UTF-8" link on the book's page. Copy the link to the plain text version of the book. In the case of *Oliver Twist*, the link to the plain text version is `"https://www.gutenberg.org/cache/epub/730/pg730.txt"`.

To download the text inside Python, you can use the following code:

```python
import urllib.request

url = 'https://www.gutenberg.org/cache/epub/730/pg730.txt'
with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')
    print(text) # for testing
```

Note that there is a preamble (boilerplate on Project Gutenberg, table of contents, etc.) that has been added to the text that you might want to strip out using Python code when you do your analysis. There is similar material at the end of the file.

One limitation of using Project Gutenberg is that they impose a limit on how many texts you can download in a 24-hour period. If you are analyzing many texts, it may be more efficient to download them once and load them off disk, rather than fetching them from Project Gutenberg's servers every time you run your program. See the **Pickling Data** section below on how to save data to files and load it back into your program. Additionally, there are many mirrors of the Project Gutenberg site available if you want to get around the download restriction.

### Data Source: Wikipedia

Wikipedia is another valuable source of data that can be easily accessed and parsed using the [mediawiki library](https://github.com/barrust/mediawiki) which is a python wrapper and parser for the **MediaWiki API**. To install the library, you can use the following command in the Command Prompt or Terminal:

```shell
# For Windows users
> python -m pip install pymediawiki

# For macOS users
> python3 -m pip install pymediawiki
```

Once you have installed the library, you can use it to search Wikipedia, get article summaries, and extract data like links and images from a page. To fetch a particular article and print out its sections, you can use the following Python code:

```python
from mediawiki import MediaWiki

wikipedia = MediaWiki()
babson = wikipedia.page("Babson College")
print(babson.title)
print(babson.content)
```

This code will fetch the article with the given title and print its title and content. The output will look like this:

```txt
Babson College (Babson) is a private business school in Wellesley, Massachusetts. Established in 1919, Babson's central focus is on entrepreneurship education and its use in creating economic and social value. The college was founded by Roger W. Babson as an all-male business institute and became coeducational in 1970.
...
```

You can also access other properties of a page, such as its categories, sections, and links. See the mediawiki package [documentation](https://pymediawiki.readthedocs.io/en/latest/quickstart.html#other-properties) for more information on available properties and methods.

### Data Source: Twitter

(**Note**: I have not tested this API since the announcment of shutting down free Twitter API. The free version of Twitter API has been deprecated and replaced with a new version that requires application approval and authentication with a paid subscription. To use the Twitter API, you need to apply to Twitter for a developer account and explain the purpose of what you are doing with the data, which Twitter will manually review.) 

(**Update**: You'll need at least the Basic access tier to search recent tweets, which isn't free. You can subscribe to it in your [Dashboard](https://developer.twitter.com/en/portal/dashboard) in the Developer Portal.)

If you have access to a Twitter developer account and the necessary API keys and tokens, you can use the `tweepy` library to search for tweets.

To install tweepy, run the following command in Command Prompt or Terminal:

```shell
# For Windows users
> python -m pip install tweepy

# For macOS users
> python3 -m pip install tweepy
```

Here is a simple example for searching tweets containing `Babson College`:

```python
import tweepy

# Replace the following strings with your own keys and secrets
TOKEN = 'Your TOKEN'
TOKEN_SECRET = 'Your TOKEN_SECRET'
CONSUMER_KEY = 'Your CONSUMER_KEY'
CONSUMER_SECRET = 'Your CONSUMER_SECRET'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(TOKEN,TOKEN_SECRET)

api = tweepy.API(auth)

for tweet in api.search_tweets(q="babson college", lang="en", count=10):
    print(f"{tweet.user.name}: {tweet.text}")
```

### Data Source: Reddit

Note: Reddit also requires users to register and create an application in order to obtain API credentials. After creating an application, you can obtain the necessary credentials such as `client_id`, `client_secret`, `username`, `password`, and `user_agent`. You can learn more about this process on the [Reddit API documentation](https://www.reddit.com/dev/api/). 

To get reddit data, you need to install the [PRAW library](https://github.com/praw-dev/praw) by running the following command in Command Prompt or Terminal:

```shell
# For Windows users
> python -m pip install praw

# For macOS users
> python3 -m pip install praw
```

Here's an example from the [PRAW docs page](https://praw.readthedocs.io/en/stable/getting_started/quick_start.html):

```python
import praw
import config


reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     username=config.username,
                     password=config.password,
                     user_agent=config.user_agent)

sub = 'learnpython'
submissions = reddit.subreddit(sub).top('day', limit=5)
for submission in submissions:
    print(submission.title)
    print(submission.selftext)
```

### Data Source: News API

You can use `newsapi-python` library to fetch news articles from [News API](https://newsapi.org/docs/). You need to install the [newsapi-python library](https://github.com/mattlisiv/newsapi-python) by running the following command in Command Prompt or Terminal:

```shell
# For Windows users
> python -m pip install newsapi-python

# For macOS users
> python3 -m pip install newsapi-python
```

Here's an example from the [Python client library page](https://newsapi.org/docs/client-libraries/python) in News API Documentation:

```python
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='12bcd741cfe7426ea4df9c970e781394')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')

# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/top-headlines/sources
sources = newsapi.get_sources()
```

### Data Source: Newspaper Articles

You can also use `Newspaper4k` package to scrape and curate news articles. You need to install the [Newspaper4k library](https://github.com/AndyTheFactory/newspaper4k) by running the following command in Command Prompt or Terminal:

```shell
# For Windows users
> python -m pip install newspaper4k

# For macOS users
> python3 -m pip install newspaper4k
```

Here's an example from the [Newspaper4k Docs page](https://newspaper4k.readthedocs.io/en/latest/):

```python
import newspaper

article = newspaper.article('https://edition.cnn.com/2023/10/29/sport/nfl-week-8-how-to-watch-spt-intl/index.html')

print(article.authors)
# ['Hannah Brewitt', 'Minute Read', 'Published', 'Am Edt', 'Sun October']

print(article.publish_date)
# 2023-10-29 09:00:15.717000+00:00

print(article.text)
# New England Patriots head coach Bill Belichick, right, embraces Buffalo Bills head coach Sean McDermott ...
```


### Data Source: IMDB Movie Reviews

To get the IMDB data, you need to install [`cinemagoer` library ](https://github.com/cinemagoer/cinemagoer) by running the following command in Command Prompt or Terminal:

```shell
# For Windows users
> python -m pip install cinemagoer

# For macOS users
> python3 -m pip install cinemagoer
```

Here's an example to print the first review of the movie "The Dark Knight":
```python
from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ia = Cinemagoer()

# search movie
movie = ia.search_movie("The Dark Knight")[0]
print(movie.movieID)
# '0468569'

# Get reviews
movie = ia.get_movie('0468569', info=['reviews']) # Make sure to add the second argument
reviews = movie.get('reviews', [])

for review in reviews:
    print(review['content'])
    print()


# Get actor
matt_damon = ia.get_person_filmography('0000354')

# Get Matt Damon's movies
data = matt_damon['data']
filmography = data['filmography']
films_as_actor = filmography['actor']
print(films_as_actor)
``` 

### Data Source: More Data Sources

There are many other data sources that you can utilize in your project:

- [SMS Spam Collection](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset) is composed by 5,574 English, real and non-enconded messages, tagged according being legitimate (ham) or spam.
- [Enron email dataset](https://www.cs.cmu.edu/~./enron/)
- [Yelp dataset](https://www.yelp.com/dataset)
- [News articles](https://archive.ics.uci.edu/dataset/137/reuters+21578+text+categorization+collection) in UCI Machine Learning Repository
- [Awesome Public Datasets](https://github.com/awesomedata/awesome-public-datasets)
- [Kaggle datasets](https://www.kaggle.com/datasets), which includes a variety of text datasets, such as news articles and movie reviews.
- [Amazon AWS Registry of Open Data](https://registry.opendata.aws/), which includes several text datasets, such as Wikipedia and Common Crawl.
- ...

Feel free to explore and choose the data source that fits your project's needs.

### Pickling Data

For several of these data sources you might find that the API calls take a pretty long time to return, or that you run into various API limits. To deal with this, you will want to save the data that you collect from these services so that the data can be loaded back at a later point in time. 

Suppose you have a bunch of Project Gutenberg texts in a list called `charles_dickens_texts`. You can save this list to a file and reload it later using the `pickle` module in Python. Here's how:

```python
import pickle

# Save data to a file (will be part of your data fetching script)

with open('dickens_texts.pkl','w') as f:
    pickle.dump(charles_dickens_texts,f)


# Load data from a file (will be part of your data processing script)
with open('dickens_texts.pkl','r') as f:
    reloaded_copy_of_texts = pickle.load(f)
```

The result of running this code is that all of the texts in the list variable `charles_dickens_texts` will now be in the list variable `reloaded_copy_of_texts`. It's important to note that you shouldn't pickle and then unpickle in the same Python script. Instead, you might want to have one script that pulls data from the web and then pickles it to a file, and another script for processing the data that will read the pickle file to get the data loaded into Python for analysis.

In addition to pickling, you can also save files using JSON format. To explore more about the built-in `json` library, feel free to ask ChatGPT or visit the official Python documentation website.

---

## Part 2: Analyzing Your Text

### Characterizing by Word Frequencies

One way to begin to process your text is to take each unit of text (for instance, books from Project Gutenberg, or perhaps a collection of movie reviews) and summarize it by counting the number of times a particular word appears in the text. A natural way to approach this in Python would be to use a **dictionary** where the keys are words that appear and the values are frequencies of words in the text. If you want to do something fancier, you can use [TF-IDF features](https://en.wikipedia.org/wiki/Tf%E2%80%93idf).

### Computing Summary Statistics


(**Note**: This step is required.)

Apart from word frequencies, there are other ways to summarize text. For example, you may want to identify the top 10 words in each text, or find the words that appear most frequently in each text, but not in other texts. Before this step, you may want to remove stop words first. 

### Removing Stop words

Stop words are words that occur frequently in text but do not provide any useful information for analysis. Examples of stop words include "the", "and", "a", etc. Removing stop words can help to reduce the size of the text data and improve the accuracy of analysis. 

### Natural Language Processing

[NLTK](https://www.nltk.org/) - the Natural Language Toolkit - is a powerful tool for processing human language data. It provides a wide range of capabilities, such as part-of-speech tagging, sentiment analysis, and full sentence parsing. 

To use NLTK, you need to install `nltk` by running the following command in in Command Prompt or Terminal:

```shell
# For Windows users
> python -m pip install nltk

# For macOS users
> python3 -m pip install nltk
```

Here is an example of doing [sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) using the `VADER` library in NLTK::

```python
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentence = 'Software Design is my favorite class because learning Python is so cool!'
score = SentimentIntensityAnalyzer().polarity_scores(sentence)
print(score)
# Output
# {'neg': 0.0, 'neu': 0.614, 'pos': 0.386, 'compound': 0.7417}
```

Notice: If you receive `Resource vader_lexicon not found` error when using `nltk`, you need to enter `python` in **Command Prompt** (or `python3` in **Terminal** on macOS), then enter `import nltk` and `nltk.download('vader_lexicon')` in Python interactive shell.

You can also use [TextBlob](https://github.com/sloria/TextBlob) library, which is built on top of NLTK, for almost everything that NLTK does. Below is the brief introduction of TextBlob from its GitHub page:

> TextBlob is a Python library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, and more.

If you perform natural language processing, you can draw interesting insights from text data collected from the web. For instance, if you monitor a specific subreddit related to a political topic, you can gauge the sentiment of the community by analyzing the text of each post and comment. Similarly, you can analyze discussions on subreddits dedicated to movies to identify which recent movies have received the most negative reviews. There are tons of cool options here!




### Text Similarity

It is potentially quite useful to be able to compute the similarity of two texts. Suppose that we have characterized some texts from Project Gutenberg using word frequency analysis. One way to compute the similarity of two texts is to test to what extent when one text has a high count for a particular word the other text also a high count for a particular word. Specifically, we can compute the cosine similarity between the two texts. This strategy involves thinking of the word counts for each text as being high-dimensional vectors where the number of dimensions is equal to the total number of unique words in your text dataset and the entry in a particular element of the vector is the count of how frequently the corresponding word appears in a specific document.  If you find this approach unclear and wish to try it, you can either reach out to the professor, or ask ChatGPT for assistance.

For a simple text similarity task, you can use external libraries, like [`TheFuzz` library](https://github.com/seatgeek/thefuzz), which uses [Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance) to calculate the differences between sequences.

```python
from thefuzz import fuzz

print(fuzz.ratio("this is a test", "this is a test!")) # 97
print(fuzz.partial_ratio("this is a test", "this is a test!")) # 100
print(fuzz.ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear")) # 91
print(fuzz.token_sort_ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear")) # 100
```

### Text Clustering 

If you can generate pairwise similarities (say using the technique above), you can Metric Multi-dimensional Scaling (MDS) to visualize the texts in a 2-dimensional space. This can help identify clusters of similar texts. 

In order to apply MDS to your data, you can use the machine learning toolkit `scikit-learn`. Here is some code that uses the similarity matrix defined in the previous section to create a 2-dimensional embedding of the four *Charles Dickens* and 1 *Charles Darwin* texts.

```python
import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

# these are the similarities computed from the previous section
S = np.asarray([[1., 0.90850572, 0.96451312, 0.97905034, 0.78340575],
    [0.90850572, 1., 0.95769915, 0.95030073, 0.87322494],
    [0.96451312, 0.95769915, 1., 0.98230284, 0.83381607],
    [0.97905034, 0.95030073, 0.98230284, 1., 0.82953109],
    [0.78340575, 0.87322494, 0.83381607, 0.82953109, 1.]])

# dissimilarity is 1 minus similarity
dissimilarities = 1 - S

# compute the embedding
coord = MDS(dissimilarity='precomputed').fit_transform(dissimilarities)

plt.scatter(coord[:, 0], coord[:, 1])

# Label the points
for i in range(coord.shape[0]):
    plt.annotate(str(i), (coord[i, :]))

plt.show()
```

This will generate the following plot. The coordinates don't have any special meaning, but the embedding tries to maintain the similarity relationships that we computed via comparing word frequencies. Keep in mind that the point labeled 4 is the work by *Charles Darwin* and the other are by *Charles Dickens*.
<!-- ![text clustering](images/text_clustering.png) -->
<img src="images/text_clustering.png" width="400" alt="text clustering" style="display:block; margin:10px auto;"/>

### Markov Text Synthesis

You can use Markov analysis to learn a generative model of the text that you collect from the web and use it to generate new texts. You can even use it to create mashups of multiple texts. One of possibilities in this space would be to create literary mashups automatically. Again, let professor know if you go this route and we can provide more guidance.

### More 

You can explore further possibilities by using the [OpenAI API](https://platform.openai.com/docs/introduction).

---

## Part 3: Learning with ChatGPT

As you work through this project and experiment with different libraries in Python, you may encounter roadblocks or have questions about your code. That's when you can use ChatGPT to clear out any issues. You are also encouraged to learn other approaches, besides the techniques mentioned above, to process, analyze and visualize your own text dataset in Python from ChatGPT, who will serve as your assistant, providing helpful suggestions, aiding your learning process.

Here's how to make the most out of ChatGPT:

- Start by taking detailed, comprehensive notes about where you're stuck or what you're trying to accomplish.
- Ask ChatGPT by providing your question or issue. Make sure to prompt it thoroughly so it may better understand your problem.
- Once ChatGPT responds, make sure to read their message carefully and consider their suggestions. Remember, responses from ChatGPT could be wrong, so it's essential to test and look for additional official documentation.
- Include ChatGPT Shared Links in comments or in a separate document, and/or **take screenshots** during your ChatGPT session to document your learning progress, which you will use in your write-up. For example: you can add "I asked ChatGPT about the best practices of writing comments. See detailed conversation: [ChatGPT Shared Link](https://chat.openai.com/share/d4445b1e-f99a-413f-a588-e4447dc73cc)"

---

## Part 4: Project Writeup and Reflection

Write a summary of your project and your reflections on it in [`README.md`](README.md), using [Markdown format](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax). There is no need to use fancy words or ChatGPT. The [`README.md`](README.md) file should consist of the following sections:

**1. Project Overview** (~1 paragraph)

What data source(s) did you use? What technique(s) did you use to process or analyze them? What did you hope to create or learn through this project?

**2. Implementation** (~1-2 paragraphs)

Describe your implementation at a system architecture level. You should NOT walk through your code line by line, or explain every function (we can get that from your docstrings). Instead, talk about the major components, algorithms, data structures and how they fit together. You should also discuss at least one design decision where you had to choose between multiple alternatives, and explain why you made the choice. Use shared links and/or screenshots to describe how you used ChatGPT to help you or learn new things.

**3. Results** (~1-3 paragraphs + figures/examples)

Present what you accomplished in your project:

- If you did some text analysis, what interesting things did you find? Graphs or other visualizations may be very useful here for showing your results.
- If you created a program that does something interesting (e.g. a Markov text synthesizer), be sure to provide a few interesting examples of the program's output.

**4. Reflection** (~1-2 paragraphs)

From a process point of view, what went well? What could you improve? Was your project appropriately scoped? Did you have a good testing plan?

From a learning perspective, mention what you learned through this project, how ChatGPT helped you, and how you'll use what you learned going forward. What do you wish you knew beforehand that would have helped you succeed?

---

## Submitting your Project

1. Push all the code and updated `README.md` to the GitGub repository.
2. Create a pull request to the upstream repository. Please learn how to create a pull request by following [this instruction](https://docs.github.com/en/desktop/working-with-your-remote-repository-on-github-or-github-enterprise/creating-an-issue-or-pull-request-from-github-desktop#creating-a-pull-request).
3. Submit your project's GitHub repository URL to Canvas.

---
*updated: 3/06/2024*