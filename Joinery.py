import urllib.request
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from thefuzz import fuzz
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
import markovify
import nltk
url = 'https://www.gutenberg.org/cache/epub/60369/pg60369.txt'
with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')
    #print(text) # for testing
#downloads the text from Project Gutenberg

#Removes stop words

custom_stop_words = ["our", "by", "which", "she", "were", "there", "what", "his", "is", "few", "here", "yourself", 
    "while", "myself", "below", "from", "of", "about", "them", "above", "how", "should", "or", 
    "those", "any", "yourselves", "was", "as", "have", "its", "the", "my", "against", "having", 
    "further", "down", "we", "do", "been", "because", "does", "can", "had", "a", "will", "hadn", 
    "through", "both", "each", "most", "herself", "then", "aren", "they", "on", "who", "to", 
    "own", "in", "himself", "and", "hasn", "he", "that", "not", "off", "after", "shouldn", "than", 
    "itself", "whom", "these", "being", "are", "ourselves", "at", "wouldn", "over", "this", "their", 
    "hers", "so", "under", "has", "me", "an", "same", "mightn", "before", "theirs", "him", "you", 
    "doing", "am", "where", "very", "couldn", "for", "weren", "be", "now", "other", "once", 
    "only", "your", "too", "i", "her", "ours", "until", "more", "some", "with", "during", "didn", 
    "when", "nor", "such", "it"
    , "all", "why", "if", "into", "just", "up", "re", "don", 
    "out", "wasn", "but", "ll", "again", "no", "him", "refer", "museums", "please", "either", 
    "permission", "illustrations", "convey", "character", "disposition", "periods", "chronological", 
    "descriptions", "accompany", "historical", "social", "manners", "customs", "directly", "indirectly", 
    "affected", "nations", "endeavour", "acceptable", "wishing", "study", "respect", "generally", "feel", 
    "particular", "interest", "obvious", "limits", "single", "volume", "dimensions", "impossible", 
    "outline", "sketch", "deserve", "consideration", "asked", "accept", "refers", "introductory", 
    "serious", "attempt", "examine", "deals", "trustworthy", "accessible", "probable", "english", 
    "readers", "greater", "french", "luxe", "treated", "manifested", "cabinet", "maker's", "mounter's", 
    "past", "years", "evidence", "appreciation", "enormous", "prices", "realised", "notable", "auction", 
    "sales", "offered", "competition", "connoisseurs", "correct", "idea", "necessary", "notice", 
    "alterations", "architectural", "styles", "influenced"]

#A list of stop words

words = text.split()
#Tokenize the text into words

filtered_words = [word for word in words if word.lower() not in custom_stop_words]
#Removes stop words from the list of words
filtered_text = " ".join(filtered_words)
#This creates a version of the text without stop words

#print(filtered_text)
#Print the new version of text without stop words


import re

words = re.findall(r'\b\w+\b', text.lower())
# This function tokenizes the text into words using regular expressions and convert to lowercase

target1_word = "chinese"  #This is my selected word for frequency test

target1_word_count = 0
# Initialize a counter for the target word

# Count the frequency of the target word
for word in words:
    if word == target1_word:
        target1_word_count += 1

# Print the frequency of the target word
print(f'The word "{target1_word}" appears {target1_word_count} times in the text.')

target2_word = "roman"  #This is my selected word for frequency test

target2_word_count = 0
# Initialize a counter for the target word

# Count the frequency of the target word
for word in words:
    if word == target2_word:
        target2_word_count += 1

print(f'The word "{target2_word}" appears {target2_word_count} times in the text.')
# Print the frequency of the target word


text = [filtered_text]

# Function to preprocess and tokenize text
def preprocess(text):
    words = text.split()
    words = [word.strip('.,!?()[]') for word in words]
    words = [word.lower() for word in words if word.isalpha()]
    return words

# Process texts and count word frequencies
word_counts = []

for text in text:
    words = preprocess(text)
    
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    word_counts.append(word_count)

# Function to get the top N words from a word count dictionary
def get_top_words(word_count, n=10):
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_words[:n])

# Identify the top 10 words in each text
top_words = [get_top_words(word_count, 10) for word_count in word_counts]

# Print the top 10 words for each text
for i, top_words in enumerate(top_words):
    print(f"Text {i + 1} - Top 10 words: {top_words}")

# Find unique words in each text
unique_words_per_text = [set(word_count.keys()) for word_count in word_counts]

# Print unique words for each text
for i, unique_words in enumerate(unique_words_per_text):
    print(f"Text {i + 1} - Unique words: {unique_words}")

#Natural Language Processing & Sentiment Analysis
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sentence = " One noticeable feature modern design furniture, revival marquetry"
score = SentimentIntensityAnalyzer().polarity_scores(sentence)
print(score)

sentence = "cases veneers cut thickness 1/16 inch"
score = SentimentIntensityAnalyzer().polarity_scores(sentence)
print(score)

#Text Similarity Test Selection
from thefuzz import fuzz 

string1 = " One noticeable feature modern design furniture, revival marquetry"
string2 = "cases veneers cut thickness 1/16 inch"

similarity = fuzz.ratio(string1, string2)
print(f"Similarity ratio: {similarity}")

#Text Clustering 

import urllib.request
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.manifold import MDS
import numpy as np
import matplotlib.pyplot as plt

#Read text content from the Project Gutenberg URL
url = 'https://www.gutenberg.org/cache/epub/47917/pg47917.txt'
with urllib.request.urlopen(url) as f:
    text_2 = f.read().decode('utf-8')

texts = [text, text_2]
#List of texts to analyze
#text = "Illustrated History of Furniture
#text_2 = "The Old Furniture Book, with a Sketch of Past Days and Ways

#Text vectorization and cosine similarity calculation
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

#Calculate cosine similarities
similarity_matrix = cosine_similarity(X)

#Display the similarity matrix
print("Pairwise Cosine Similarities:")
print(similarity_matrix)

#MDS for visualization
mds = MDS(n_components=2, dissimilarity="precomputed")

#Calculate the dissimilarity matrix (1 - similarity_matrix)
dissimilarity_matrix = 1 - similarity_matrix

embedding = mds.fit_transform(dissimilarity_matrix)

#Visualize the texts in 2D space
plt.scatter(embedding[:, 0], embedding[:, 1])
plt.title("MDS Visualization of Texts")
for i, txt in enumerate(texts):
    plt.annotate(f'Text {i + 1}', (embedding[i, 0], embedding[i, 1]))
plt.show()

#Markov Analysis Experimentation

import markovify
def build_markov_model(text):
    return markovify.Text(text)

def generate_text(markov_model, num_sentences=3):
    return markov_model.make_short_sentence(max_chars=200, min_chars=50, tries=100)

text = filtered_text

markov_model = build_markov_model(text)
#Creates a Markov model

new_text = generate_text(markov_model)
#Generate new text with the model

print(new_text)
#Various possible combinations, so awesome!