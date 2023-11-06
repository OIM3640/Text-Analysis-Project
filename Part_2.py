import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import gensim
from gensim import corpora
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim import corpora, models
nltk.download('punkt')
nltk.download('stopwords')
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

""" In this file I will be performing three types of analysis: Sentiment, Topic Modeling with LDA and Text Clustering using MDS"""

# Sentiment Analysis 

# Downloading the VADER lexicon
nltk.download('vader_lexicon')

# Function to read text from a file
def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to perform sentiment analysis
def perform_sentiment_analysis(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)
    return sentiment_score

# List of filenames
filenames = ['Fox.txt', 'MSNBC.txt']  

# Loop through each file and perform sentiment analysis
for file_name in filenames:
    file_path = file_name  # or specify the path if the files are in a different directory
    article_text = read_text_from_file(file_path)
    sentiment_result = perform_sentiment_analysis(article_text)
    print(f"Sentiment results for {file_name}: {sentiment_result}\n")

# Topic Modeling LDA 

# Assuming you have two text files: 'Fox.txt' and 'MSNBC.txt'
file_paths = ['Fox.txt', 'MSNBC.txt']

documents = []
for path in file_paths:
    with open(path, 'r', encoding='utf-8') as file:
        documents.append(file.read())

# Tokenize documents
stop_words = set(stopwords.words('english'))
# You don't need to tokenize twice; this will tokenize and remove stop words
texts = [
    [word for word in word_tokenize(document.lower()) if word not in stop_words]
    for document in documents
]

# Build a dictionary and a corpus for LDA preparation
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

# Train the LDA model
lda_model = models.LdaModel(corpus, num_topics=2, id2word=dictionary, passes=15)

# Get the topics from the model
topics = lda_model.print_topics(num_words=4)
for topic in topics:
    print(topic)

# Seeing which topic is most dominant in each article 
for doc_bow in corpus:
    print(lda_model.get_document_topics(doc_bow))


# Text Clustering using MDS

# Inserting topic distributions obtained from LDA model
topic_distributions = [
    np.array([0, 0.99793404]), 
    np.array([1, 0.9991887])    
]

# Calculate the similarity matrix
S = cosine_similarity(topic_distributions)

# Dissimilarity is 1 minus similarity
dissimilarities = 1 - S

# Compute the embedding
embedding = MDS(dissimilarity='precomputed').fit_transform(dissimilarities)

# Visualize with Matplotlib
plt.scatter(embedding[:, 0], embedding[:, 1])

# Label the points
for i in range(embedding.shape[0]):
    plt.annotate(f'Doc {i+1}', (embedding[i, 0], embedding[i, 1]))

plt.title('Text Clustering using MDS')
plt.xlabel('MDS Dimension 1')
plt.ylabel('MDS Dimension 2')
plt.show()

