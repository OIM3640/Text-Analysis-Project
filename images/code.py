from mediawiki import MediaWiki

# Initialize
wikipedia = MediaWiki()
babson = wikipedia.page("Babson College")
print(babson.title)
print(babson.content)

# Get the title and content
title = babson.title
content = babson.content

# Split the content into words by whitespace
words = content.split()

# Count word frequencies using a dictionary
word_frequencies = {}
for word in words:
    if word in word_frequencies:
        word_frequencies[word] += 1
    else:
        word_frequencies[word] = 1

# Sort the top 10 most common words
most_common_words = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)[:10]

# Results
print(f"Title: {title}")
print("Most common words:", most_common_words)

# Remove Stop Words
stop_words = {
    "the", "and", "a", "an", "in", "of", "to", "is", "it", "that", "on",
    "for", "with", "as", "by", "this", "at", "from", "or", "be", "are", 
    "was", "were", "but", "not", "have", "has", "had", "they", "their", 
    "which", "you", "we", "his", "her", "him", "she", "he", "them", "its",
    "my", "our", "your", "i", "me", "us", "do", "does", "did"
}

# Remove stop word if it exists in dictionary
for stop_word in stop_words:
    word_frequencies.pop(stop_word, None) 

# Summary Statistics
total_words = sum(word_frequencies.values())
unique_words = len(word_frequencies)
average_frequency = total_words / unique_words
most_common_words = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)[:10]
least_common_words = [word for word, count in word_frequencies.items() if count == 1]

# Display Summary Statistics
print(f"Title: {title}")
print(f"Total Words (after stop word removal): {total_words}")
print(f"Number of Words Appearing Once): {len(least_common_words)}")

for word, freq in most_common_words:
    print(f"  {word}: {freq} occurrences")

# Natural Language Processing
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize Wikipedia API
wikipedia = MediaWiki()
page = wikipedia.page("Babson College")
content = page.content

# Initialize Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Analyze the sentiment of the entire Wikipedia page content
sentiment_score = analyzer.polarity_scores(content)

# Display the sentiment scores
print("Sentiment Analysis for 'Babson College' Wikipedia Page:")
print(f"Negative Score: {sentiment_score['neg']}")
print(f"Neutral Score: {sentiment_score['neu']}")
print(f"Positive Score: {sentiment_score['pos']}")
print(f"Compound Score: {sentiment_score['compound']}")

# Text Similarity with TheFuzz
from thefuzz import fuzz

# Sample texts
text1 = "Babson College is a private business school in Wellesley, Massachusetts."
text2 = "Harvard University is a private Ivy League school in Cambridge, Massachusetts."

# Compute similarity ratios
ratio = fuzz.ratio(text1, text2)
partial_ratio = fuzz.partial_ratio(text1, text2)
token_sort_ratio = fuzz.token_sort_ratio(text1, text2)

# Display results
print("Levenshtein Similarity Ratio:", ratio)
print("Partial Similarity Ratio:", partial_ratio)
print("Token Sort Similarity Ratio:", token_sort_ratio)

# visualize similarity between multiple texts using Python?
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Example run (Ai Generated prompts)
texts = [
    "Babson College is a private business school in Massachusetts.",
    "Harvard University is an Ivy League university in Cambridge.",
    "MIT is a research university in Cambridge, Massachusetts.",
    "Stanford University is a prestigious school in California.",
    "Berkeley is known for its research programs in California."
]

# Vectorize the texts
vectorizer = CountVectorizer()
text_vectors = vectorizer.fit_transform(texts)

# Compute pairwise cosine similarity
similarity_matrix = cosine_similarity(text_vectors)

import seaborn as sns
import matplotlib.pyplot as plt

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(similarity_matrix, annot=True, cmap="YlGnBu", xticklabels=[f'Text {i+1}' for i in range(len(texts))], yticklabels=[f'Text {i+1}' for i in range(len(texts))])
plt.title("Cosine Similarity Heatmap between Texts")
plt.show()