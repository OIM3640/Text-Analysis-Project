import urllib.request

url = 'https://www.gutenberg.org/cache/epub/43795/pg43795.txt'
with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')
    print(text) 
#downloads the text of my choice, "Sketches of Central Asia", from Project Gutenberg

#Remove stop words from the text

custom_stop_words = ["one", "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his","himself", 
"she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who","whom", "this", "that", "these", 
"those", "am", "is", "are", "was", "were","be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", 
"if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", 
"above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", 
"why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", 
"very", "s", "t", "can", "will", "just", "don", "should", "now", "d", "ll", "m", "o", "re", "ve", "y", "ain", "aren", "couldn", "didn", "doesn", "hadn", "hasn", 
"haven", "isn", "ma", "mightn", "mustn", "needn", "shan", "shouldn", "wasn", "weren", "won", "wouldn", "many", "even", "would", "may", "among", "great", "much", "first", "upon", "long", "yet", 
"people", "far", "also", "two", "part", "must", "still", "every", "could", "whole", "well", "without", "made", "like", "often", "man", "place", "however"]

#This is my custom list of stop words

words = text.split()
#Tokenize the text into words

filtered_words = [word for word in words if word.lower() not in custom_stop_words]
#This removes stop words from the list of words
filtered_text = " ".join(filtered_words)
#This creates a version of the text without stop words

print(filtered_text)
#Print the new version of text without stop words


import re

words = re.findall(r'\b\w+\b', text.lower())
# This function tokenizes the text into words using regular expressions and convert to lowercase

target1_word = "bokhara"  #This is my selected word for frequency test

target1_word_count = 0
# Initialize a counter for the target word

# Count the frequency of the target word
for word in words:
    if word == target1_word:
        target1_word_count += 1

# Print the frequency of the target word
print(f'The word "{target1_word}" appears {target1_word_count} times in the text.')

target2_word = "silk"  #This is my selected word for frequency test

target2_word_count = 0
# Initialize a counter for the target word

# Count the frequency of the target word
for word in words:
    if word == target2_word:
        target2_word_count += 1

print(f'The word "{target2_word}" appears {target2_word_count} times in the text.')
# Print the frequency of the target word

target3_word = "trade"  #This is my selected word for frequency test

target3_word_count = 0
# Initialize a counter for the target word

# Count the frequency of the target word
for word in words:
    if word == target3_word:
        target3_word_count += 1

print(f'The word "{target3_word}" appears {target3_word_count} times in the text.')
# Print the frequency of the target word


text = [filtered_text]
#Using the text that has filtered out the stop words

# Function to tokenize text
def preprocess(text):
    words = text.split()
    words = [word.strip('.,!?()[]') for word in words]
    words = [word.lower() for word in words if word.isalpha()]
    return words

# This function processes texts and count word frequencies
word_counts = []

for text in text:
    words = preprocess(text)
    
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    word_counts.append(word_count)

# this function captures the top N words from a word count dictionary
def get_top_words(word_count, n=10):
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_words[:n])

# this function identifies the top 10 words in each text
top_words_per_text = [get_top_words(word_count, 10) for word_count in word_counts]

# Print the top 10 words for each text
for i, top_words in enumerate(top_words_per_text):
    print(f"Text {i + 1} - Top 10 words: {top_words}")

# Find unique words in each text
unique_words_per_text = [set(word_count.keys()) for word_count in word_counts]

# Print unique words for each text
for i, unique_words in enumerate(unique_words_per_text):
    print(f"Text {i + 1} - Unique words: {unique_words}")

#Natural Language Processing & Sentiment Analysis
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sentence = 'insuperable barrier Kuen-Lun mountains renders progress towards Kashmir impossible; Russian diversion good Central-Asiatic trade. moment, however, put aside discussion question, preferring glance Central Asia inclines westward Khokand'
score = SentimentIntensityAnalyzer().polarity_scores(sentence)
print(score)

sentence = 'Moreover, Bokhara, Khiva Karshi, Russian traders found who, secure energy government, course advance interests better foreign mercantile agents. vain seek better apostle, better pioneer civilisation, trade; vain, better teacher turn men ways thinking, silent bales goods carried Europe; England, apart commercial interests, bound, ends humanity also, help forward trade Central Asia.'
score = SentimentIntensityAnalyzer().polarity_scores(sentence)
print(score)

#Text Similarity Test Selection
from thefuzz import fuzz 

string1 = "insuperable barrier Kuen-Lun mountains renders progress towards Kashmir impossible"
string2 = "Moreover, Bokhara, Khiva Karshi, Russian traders found who, secure energy government, course advance interests better foreign mercantile agents."

similarity = fuzz.ratio(string1, string2)
print(f"Similarity ratio: {similarity}")

#Text Clustering 

import urllib.request
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.manifold import MDS
import numpy as np
import matplotlib.pyplot as plt

# Read text content from the Project Gutenberg URL
url = 'https://www.gutenberg.org/cache/epub/58074/pg58074.txt'
with urllib.request.urlopen(url) as f:
    text_2 = f.read().decode('utf-8')

texts = [text, text_2]
#List of texts to analyze
#text = "Sketches of Central Asia" by Ármin Vámbéry 
#text_2 = "Travels into Bokhara" by Sir Alexander Burnes

# Text vectorization and cosine similarity calculation
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Calculate cosine similarities
similarity_matrix = cosine_similarity(X)

# Display the similarity matrix
print("Pairwise Cosine Similarities:")
print(similarity_matrix)

# MDS for visualization
mds = MDS(n_components=2, dissimilarity="precomputed")

# Calculate the dissimilarity matrix (1 - similarity_matrix)
dissimilarity_matrix = 1 - similarity_matrix

embedding = mds.fit_transform(dissimilarity_matrix)

# Visualize the texts in 2D space
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
#Create a Markov model

new_text = generate_text(markov_model)
#Generate new text with the model

print(new_text)
#Various possible combinations, so cool!
















