from newsapi import NewsApiClient
import pprint


# Connect API
newsapi = NewsApiClient(api_key="841898ac60834037bd25b9f134b163c6")

# fetch Apple-related top-headlines
all_articles = newsapi.get_everything(
    q="Apple Growth",
    sort_by="relevancy",
    language="en",
    from_param="2023-11-01",
    to="2023-11-07",
)
# print (all_articles)


# Create article content list with title, desciption and url link
def article_content_list():
    """
    get articles from NEWS API
    return article content list with title, desciption and url link
    
    """
    articles = all_articles.get("articles", [])
    article_content = {"title": [], "description": []}

    for article in articles:
        title = article.get("title", "")
        description = article.get("description", "")
        url = article.get("url", "")
        article_content["title"].append(title + url)
        article_content["description"].append(description + url)

    return article_content


content = article_content_list()
# pprint.pprint(content)


# text processing
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

nltk.download("stopwords")
nltk.download("punkt")
nltk.download("vader_lexicon")


# 1: text cleanning
# https://chat.openai.com/share/af7aa015-d1be-4263-9b36-84213e1ac6e5
def process_text(text):
    """
    processes text by removing uncessary characters and stopwords 
    tokening processed words and return them to a list 
    
    """
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\d+", "", text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words("english"))

    filtered_tokens = []
    for word in tokens:
        if word.lower not in stop_words:
            filtered_tokens.append(word)
    return filtered_tokens


# 2. process the article content
def processed_content():
    """
    the function uses the process_text function to process the title and description
    in the content and return the processed content 
    
    """
    processed_content = []
    for title, description in zip(content["title"], content["description"]):
        processed_title = process_text(title)
        processed_description = process_text(description)
        processed_content.append(
            {"title": processed_title, "description": processed_description}
        )

    return processed_content


processed = processed_content()
print(processed)


# Sentiment Analysis
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()


def analyze_sentiment(text):
    """
    analyzes sentiment of the text and return the score 
    """
    scores = sid.polarity_scores("".join(text))
    return scores


for title, description in processed:
    overall_sentiment = analyze_sentiment(title+description)
    # description_sentiment = analyze_sentiment(content["description"])
    print(f"Overall Sentiment: {overall_sentiment}")
    # print(f"Description Sentiment: {description_sentiment}")

#reference: https://chat.openai.com/share/53c5063b-c550-43aa-97e7-aa7eef98071d