from mediawiki import MediaWiki
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import string

""" We are going to be analyzing the Wikipedia page "Panama". 
1. We are going to be using the library nltk to remove the stopwords and find what are the 10 most common words that appear in Panama's page. (We wont take into account numbers, special characters, and the word "de")"""


#download stopwords
nltk.download('stopwords')
nltk.download('punkt')

#get content from wikipedia
wikipedia = MediaWiki()
Panama = wikipedia.page("Panama")
text = Panama.content
# print(Panama.summary)
#print(Panama.images)

#convert the text into words
words = word_tokenize(text)

#Define a list of English stopwords and string of special characters
stop_words = set(stopwords.words("english"))
special_characters = string.punctuation

#Filter out the stopwords, words that contain numbers, the word "de" and special characters and convert words to lowercase
filtered_words = [word.lower() for word in words if word.lower() not in stop_words and not any(char.isdigit() for char in word) and word.lower() != "de" and all(char not in special_characters for char in word)]

#Count the frequency of each word
word_counts = Counter(filtered_words)

#Find the word that appears the most and its count.top 10 words
print("Top 10 words:")
for word, count in word_counts.most_common(10):
    percentage = (count / len(filtered_words) * 100)
    print(f"{word}: {count} times ({percentage:.2f}%)")


