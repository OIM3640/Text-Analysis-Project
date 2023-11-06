from mediawiki import MediaWiki


wikipedia = MediaWiki()
Jean_Michel_Basquiat = wikipedia.page("Jean-Michel Basquiat")
print(Jean_Michel_Basquiat.title)
print(Jean_Michel_Basquiat.content)


import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#Asked ChatGPT how to preform a sentiment analysis for the whole wikipedia page of Basquiat rather than just a sentence 
#Here we are downloading Vader lexicon, it is designed to analyze emotional tone of text
nltk.download('vader_lexicon')

#Start the SentimentAnalyzerIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

#Here we are extracting the text from The artist's wikipedia page 
text = Jean_Michel_Basquiat.content

#Preform the analysis 
sentiment_scores = sia.polarity_scores(text)

#Analyze Sentiment scores

compound_score = sentiment_scores['compound']

if compound_score >= 0.05: 
    sentiment = "Positive"
elif compound_score <= 0.05: 
    sentiment = "Negative"
else: 
    sentiment = "Neutral"
    
print("Sentiment Analysis:")
print("Sentiment Score(Compound):", compound_score) 
print("Sentiment", sentiment)

#Now we are going to get the raw text from the wikipedia page and then tokenize it,
#at first I did it in two parts and I asked chat gpt how to call my defined function (raw_text) to tokenize it

import wikipediaapi
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Create a Wikipedia API object with a custom user agent
wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='YourUserAgent/1.0'  # Replace 'YourUserAgent/1.0' with your user agent string
)

# Page title for Jean-Michel Basquiat
page_title = "Jean-Michel_Basquiat"

# Get the page
page = wiki_wiki.page(page_title)

# Get the raw text
raw_text = page.text

# Print the raw text
print(raw_text)

# Download NLTK resources
nltk.download('stopwords')
nltk.download('punkt')

# Tokenize the text into words
tokens = word_tokenize(raw_text)

# Convert tokens to lowercase
tokens = [token.lower() for token in tokens]

# Remove punctuation and numbers
tokens = [token for token in tokens if token.isalpha()]

# Remove stopwords
stop_words = set(stopwords.words('english'))
tokens = [token for token in tokens if token not in stop_words]

# Join the cleaned tokens back into a single string
cleaned_text = ' '.join(tokens)

print("cleaned_text:")
print(cleaned_text)

#asked chat GPT how to build a bar chart for my top ten frequencies of the most important words used in the article 
import matplotlib.pyplot as plt
from collections import Counter

# Count the word frequencies
word_freq = Counter(tokens)

# Displaying the top ten most frequent words
top_words = word_freq.most_common(10)

# Extract words and frequencies
words = [word for word, freq in top_words]
frequencies = [freq for word, freq in top_words]

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.barh(words, frequencies, color='skyblue')
plt.xlabel('Frequency')
plt.title('Top 10 Most Frequent Words')
plt.gca().invert_yaxis()  # Invert the y-axis to show the most common word at the top

# Save the chart as an image file
plt.savefig('C:/Users/nguillamon1/Desktop/word_frequency_chart.png')

#displaying the chart
plt.show()


    