"""Recently, The shutdown of Credit Suisse, one of the nine biggest investment banking, has been arouse people's attention.
As an finance student, I would like to know more about this event. Therefore, I use NewAPI key to help me trace the articless realted to credit suisse
and have done several anaysis to give me an foresight about what's going on with credit suisse """

#Step 1. Using NewsAPI key to find all the news that have "Credit Suisse" in their headline from credible financial news source.

import requests
import json

api_key = '95b99711861949b2afde929a0debf89f'

# Define the URL for the NewsAPI endpoint
url = ('https://newsapi.org/v2/everything?'
       'q=Credit%20Suisse&inTitle=true'
       'sortBy=publishedAt&'
       f'apiKey={api_key}')

# Make a GET request to the NewsAPI endpoint
response = requests.get(url)

# Parse the response JSON data
try:
    data = json.loads(response.text)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON response: {e}")
    exit()

# Check if the API response contains any articles
if 'articles' not in data:
    print("No articles found in API response.")
    exit()

#Print the headlines and URLs of the articles
# for article in data['articles']:
#     print(article['title'])
#     print(article['url'])
#     print()

#Step 2: Analyze the text extracted: find out the word frequency in these title
from collections import Counter

words_frequency = []
for article in data['articles']:
    words_frequency.extend(article['title'].split())

# Count the frequency of each word
word_counts = Counter(words_frequency)

# Print the word frequencies in descending order
for word, count in word_counts.most_common():
   # print(f"{word}: {count}")

 """
After checking the word frequency, it is found words "UBS" "takeover" have appeared frequently in the title
Therefore, I intended to find out the aritles that have "UBS" "Credit suisse" "takeover" in the text.
 """

# step 3:

 from newsapi import NewsApiClient

# Initialize NewsApiClient with your API key
api_key = '95b99711861949b2afde929a0debf89f'
newsapi = NewsApiClient(api_key=api_key)

# Define the search query
query = 'UBS AND "Credit Suisse" AND takeover'

# Make a request to the NewsAPI endpoint
response = newsapi.get_everything(q=query, language='en')

# Check if the API response contains any articles
if response['totalResults'] == 0:
    print("No articles found in API response.")
    exit()

# Print the headlines and URLs of the articles
for article in response['articles']:
    print(article['title'])
    print(article['url'])
    print()


