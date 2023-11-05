import urllib.request
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

url = 'https://www.gutenberg.org/ebooks/42671.txt.utf-8'

with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')

nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()

scores = sid.polarity_scores(text)

print("Sentiment Scores:")
for score_name, score_value in scores.items():
    print(f"{score_name}: {score_value}")






