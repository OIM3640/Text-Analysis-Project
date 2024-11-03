from nltk.sentiment.vader import SentimentIntensityAnalyzer
from thefuzz import fuzz
import nltk

nltk.download('vader_lexicon')

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the text using the VADER sentiment analyzer and returns sentiment scores.
    """
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(text)
    return sentiment_scores

def compare_texts(text1, text2):
    """
    Compares two texts and provides a similarity score using TheFuzz.
    """
    return fuzz.ratio(text1, text2)

if __name__ == "__main__":
    from data_collection import wikipedia_content

    content1 = wikipedia_content("FC Barcelona")
    content2 = wikipedia_content("Real Madrid")

    if content1:
        sentiment_score = analyze_sentiment(content1)
        print("\nSentiment Analysis of FC Barcelona's Wikipedia page:")
        print(sentiment_score)

    if content1 and content2:
        similarity_score = compare_texts(content1, content2)
        print("\nSimilarity Score between FC Barcelona's & Real Madrid's Wikipedia pages:")
        print(similarity_score)

