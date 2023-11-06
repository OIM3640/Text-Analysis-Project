import urllib.request

url = 'http://www.gutenberg.org/ebooks/730.txt.utf-8'
with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')
    print(text)

import re
# to remove punctuations and convert to lowercase 
text = re.sub(r'[^\w\s]', '', text)
text = text.lower()

#splitting the text into individual words 
words = text.split()

# counting the frequency of each word 
word_count = {}
for word in words: 
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

#sort the words by frequency 
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# print out the top ten most frequent words
for word, count in sorted_words[:20]:
    print(word, count)

# REMOVING STOP WORDS 
import nltk
nltk.download('stopwords')
words1 = nltk.word_tokenize(text)

from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words1 if word.casefold() not in stop_words]
filtered_data = ' '.join(filtered_words)
print(filtered_data)

# finding text similarity 
from thefuzz import fuzz 
text1 = "The court was paved, from floor to roof, with human faces. Inquisitive and eager eyes peered from every inch of space. From the rail before the dock, away into the sharpest angle of the smallest corner in the galleries, all looks were fixed upon one man—Fagin. Before him and behind: above, below, on the right and on the left: he seemed to stand surrounded by a firmament, all bright with gleaming eyes."
text2 = "He stood there, in all this glare of living light, with one hand resting on the wooden slab before him, the other held to his ear, and his head thrust forward to enable him to catch with greater distinctness every word that fell from the presiding judge, who was delivering his charge to the jury. At times, he turned his eyes sharply upon them to observe the effect of the slightest featherweight in his favour; and when the points against him were stated with terrible distinctness, looked towards his counsel, in mute appeal that he would, even then, urge something in his behalf. Beyond these manifestations of anxiety, he stirred not hand or foot. He had scarcely moved since the trial began; and now that the judge ceased to speak, he still remained in the same strained attitude of close attention, with his gaze bent on him, as though he listened still."

fuzz_similarity = fuzz.token_sort_ratio(text1, text2)
print("Fuzz similarity between text1 and text2: ", fuzz_similarity)

# TEXT CLUSTERING 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

n_texts = len(text)
X = np.empty((n_texts, n_texts))

tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf = tfidf_vectorizer.fit_transform(text)

kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(tfidf)

for i in range(n_texts):
    for j in range(n_texts):
        if kmeans.labels_[i] == kmeans.labels_[j]:
            X[i,j] = 1

plt.imshow(X, camp='viridis')
plt.colorbar()
plt.show()

# Markov text analisys 

import markovify 
text_model = markovify.Text(text)
sentence = text_model.make_sentence()
print(sentence)
