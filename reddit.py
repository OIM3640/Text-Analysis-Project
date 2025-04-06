import os
import re
import nltk
import praw
import numpy as np
import matplotlib.pyplot as plt

from dotenv import load_dotenv
from collections import Counter
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.manifold import MDS

nltk.download('stopwords')
nltk.download('vader_lexicon')

def load_reddit_instance():
    """
    Loads Reddit credentials from .env and returns an authenticated Reddit instance.
    """
    load_dotenv()
    return praw.Reddit(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD"),
        user_agent=os.getenv("USER_AGENT")
    )


def fetch_titles(subreddit_name="marvelstudios", limit=500, time_filter="month"):
    """
    Fetches post titles from the specified subreddit
    """
    reddit = load_reddit_instance()
    subreddit = reddit.subreddit(subreddit_name)
    posts = subreddit.top(time_filter=time_filter, limit=limit)
    return [post.title for post in posts]


def analyze_mentions(titles, keywords):
    """
    Counts how many times each Marvel-related keyword appears in the collected titles
    """
    combined_text = " ".join(titles).lower() #Text combination assisted by ChatGPT
    counts = Counter()
    for keyword in keywords:
        if keyword in combined_text:
            counts[keyword] = combined_text.count(keyword)
    return counts


def get_word_frequencies(titles):
    """
    Extracts non-stop words from titles and returns a frequency count
    """
    stop_words = set(stopwords.words('english'))
    words = []

    for title in titles:
        cleaned = re.sub(r"[^\w\s]", "", title.lower()) #Cleaning process assisted by ChatGPT
        for word in cleaned.split():
            if word not in stop_words:
                words.append(word)

    return Counter(words)


def analyze_sentiments(titles):
    """
    Performs sentiment analysis on Reddit titles using VADER.

    This section was developed with assistance from ChatGPT.
    """
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = {
        "positive": 0,
        "neutral": 0,
        "negative": 0
    }

    for title in titles:
        score = sia.polarity_scores(title)
        if score["compound"] >= 0.05:
            sentiment_scores["positive"] += 1
        elif score["compound"] <= -0.05:
            sentiment_scores["negative"] += 1
        else:
            sentiment_scores["neutral"] += 1

    total = len(titles)
    print("\nSentiment analysis of Reddit post titles:\n")
    for label, count in sentiment_scores.items():
        pct = round(100 * count / total, 2)
        print(f"{label.title()}: {count} posts ({pct}%)")


def cluster_titles(titles, keywords):
    """
    Uses cosine similarity and MDS to cluster Reddit post titles in 2D space.

    The clustering and color-coded visualization were built with assistance from ChatGPT
    """
    stop_words = set(stopwords.words('english'))
    cleaned_titles = []
    labels = []

    # Clean titles and assign labels based on Marvel keyword matches
    for title in titles:
        lower_title = title.lower()
        words = re.sub(r"[^\w\s]", "", lower_title).split()
        filtered = [w for w in words if w not in stop_words]
        cleaned_titles.append(" ".join(filtered))

        movie_label = "None"
        for keyword in keywords:
            if keyword in lower_title:
                movie_label = keyword.title()
                break
        labels.append(movie_label)

    # Vectorize text and compute cosine similarity
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(cleaned_titles)
    sim_matrix = cosine_similarity(X)

    # Use Multi-Dimensional Scaling (MDS) for dimensionality reduction
    coords = MDS(dissimilarity='precomputed', random_state=42).fit_transform(1 - sim_matrix)

    # Assign colors per movie label
    unique_labels = list(sorted(set(labels)))
    cmap = plt.cm.get_cmap("tab20", len(unique_labels))
    label_to_color = {label: cmap(i) for i, label in enumerate(unique_labels)}
    colors = [label_to_color[label] for label in labels]

    # Plot the clustered points
    plt.figure(figsize=(12, 8))
    plt.scatter(coords[:, 0], coords[:, 1], c=colors, alpha=0.7, edgecolor='k', linewidth=0.2)

    # Legend for colored labels (skip "None")
    handles = [plt.Line2D([0], [0], marker='o', color='w', label=label,
                          markerfacecolor=color, markersize=8)
               for label, color in label_to_color.items() if label != "None"]

    plt.legend(handles=handles, title="Movie Mentions", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.title("Clustering of r/marvelstudios Post Titles (Color-Coded by Movie Mention)")
    plt.xlabel("MDS Dimension 1")
    plt.ylabel("MDS Dimension 2")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    """
    Main section compiled with the aid of ChatGPT
    """
    movie_keywords = [ #Generated by ChatGPT
        "endgame", "infinity war", "iron man", "black panther", "captain marvel",
        "ant-man", "quantumania", "no way home", "multiverse of madness",
        "shang-chi", "eternals", "thor", "love and thunder", "wakanda forever",
        "guardians", "avengers", "deadpool", "spider-man", "loki", "wandavision",
        "daredevil", "thunderbolts", "secret invasion", "kang", "doomsday"
    ]

    print("Fetching Reddit post titles")
    titles = fetch_titles()

    print("\nTop Marvel mentions in r/marvelstudios this month:\n")
    mentions = analyze_mentions(titles, movie_keywords)
    for movie, count in mentions.most_common():
        print(f"{movie.title()}: {count}") #Listing aided by ChatGPT

    print("\nTop individual non-stop words in post titles:\n")
    word_freqs = get_word_frequencies(titles)
    for word, count in word_freqs.most_common(15):
        print(f"{word}: {count}") #Listing aided by ChatGPT

    print("\nAnalyzing sentiment of post titles")
    analyze_sentiments(titles)

    print("\nClustering post titles (color-coded by movie mentions)\n")
    cluster_titles(titles, movie_keywords)


if __name__ == "__main__":
    main()

#Overall structure and debugging done using the help of ChatGPT