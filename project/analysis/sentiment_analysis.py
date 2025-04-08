from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json

analyzer = SentimentIntensityAnalyzer()

def sentiment_huffpost():
    with open("project/data/huffpost_articles.json", encoding="utf-8") as file: 
        articles = json.load(file)

        scores = []

        for article in articles[8:]:  # skip category descriptions
            text = article.get("text", "")
            if text.strip():  # ignore empty
                score = analyzer.polarity_scores(text)
                scores.append(score["compound"])

        avg_score = sum(scores) / len(scores) # average sentiment score
        print("Average HuffPost sentiment:", round(avg_score, 4))

def sentiment_epochtimes():
    with open("project/data/theepochtimes_articles.json", encoding="utf-8") as file: 
        articles = json.load(file)

        scores = []

        for article in articles:
            text = article.get("text", "")
            if text.strip():  # ignore empty
                score = analyzer.polarity_scores(text)
                scores.append(score["compound"])

        avg_score = sum(scores) / len(scores) # average sentiment score
        print("Average The Epoch Times sentiment:", round(avg_score, 4))

sentiment_huffpost()
sentiment_epochtimes()