# This lets us use regular expressions, which help us extract just the words from a big chunk of text.
import re
# Counter is a really useful tool that helps count how many times each word shows up.
from collections import Counter
# nltk is a popular Python library that helps us work with natural language (text data).
import nltk
# This gives us a list of very common English words like "the", "and", "is" that we usually want to ignore.
from nltk.corpus import stopwords
# This tool helps us measure the "mood" or sentiment of the text — whether it sounds positive, negative, or neutral.
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# These two lines download some tools from nltk the first time we run the code.
nltk.download('stopwords')        # downloads the list of stopwords
nltk.download('vader_lexicon')    # downloads the sentiment scoring tool

# This function breaks a big string of text into a list of individual words.
def get_words(text): 
    text = text.lower()
    # This line uses a regular expression to grab only actual words made of letters.
    # I wasn’t totally sure how this worked, so I used GPT to help me understand what \b[a-z]+\b means
    # At first I was thinking of using split to break the text into words, but that would have included punctuation
    words = re.findall(r'\b[a-z]+\b', text)
    return words

# This function removes stop words 
def remove_stopwords(words):
    # Get the default list of stopwords from nltk.
    stop_words = set(stopwords.words('english'))
    # Keep only the words that are NOT in the stopwords list.
    filtered = [word for word in words if word not in stop_words]
    return filtered

# This function counts how many times each word appears.
def count_words(words):
    # This uses Python’s Counter class to count things. Very useful for word counts.
    return Counter(words)

# This function checks how positive, negative, or neutral the overall text is.
def analyze_sentiment(text):
    # Create a sentiment analyzer (provided by nltk).
    sid = SentimentIntensityAnalyzer()
    # Get a dictionary of sentiment scores for the text.
    # It returns values like: {'neg': 0.1, 'neu': 0.6, 'pos': 0.3, 'compound': 0.4}
    # I used GPT to learn how to interpret these scores and what they mean.
    return sid.polarity_scores(text)
