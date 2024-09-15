"""Next, I intend to access one of the articles that has "credit suisse" "UBS"and "takeover" to do the further analysis """
import requests
import json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

api_key = '95b99711861949b2afde929a0debf89f'

# Define the URL for the NewsAPI endpoint
url = ('https://newsapi.org/v2/everything?'
       'q=UBS%20Credit%20Suisse%20takeover&'
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
if 'articles' not in data or len(data['articles']) == 0:
    print("No articles found in API response.")
    exit()

# Get one article from the response
article = data['articles'][6]

# Store the content of the article in a variable
article_content = requests.get(article['url']).text

# Save the content of the article to a file
with open('article2.txt', 'w', encoding='utf-8') as f:
     f.write(article_content)


#Text analysis 

# Open the file and read its contents
with open('extract/article1.txt', 'rb') as file:
    bytes_text = file.read()
    text = bytes_text.decode('utf-8')


# Tokenize the text
tokens = word_tokenize(text)

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in tokens if not token in stop_words]

# Write the filtered tokens to a new file
with open('filtered_article.txt', 'w') as file:
    file.write(' '.join(filtered_tokens))




import nltk
from collections import Counter

#Identify the 10 most common words
nltk.download('punkt')
nltk.download('stopwords')

# Load stop words
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Open file
with open('extract/filtered_article1.txt', 'r', encoding='ISO-8859-1') as file:
    text = file.read()


# Filter out punctuation and stopwords
words = [token for token in tokens if token.isalpha() and token not in stop_words]

# Get the frequency distribution of the words
freq_dist = nltk.FreqDist(words)

# Print the 10 most common words
print(freq_dist.most_common(10))