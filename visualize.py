# visualize.py
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def plot_top_keywords(tfidf_scores, title, n=10, save_path=None):
    """Bar chart of top n TF-IDF terms. If save_path is given, saves PNG instead of showing.
        My experience wtih TF-IDF was with R so I needed alot of help from Ai to be able to perform this task"""
    
    top_items = sorted(tfidf_scores.items(), key=lambda x: x[1], reverse=True)[:n]
    if not top_items:
        return
    words, scores = zip(*top_items)

    plt.figure(figsize=(8, 4))
    plt.barh(words, scores)
    plt.gca().invert_yaxis()
    plt.title(f"Top {n} TF-IDF Keywords – {title}")
    plt.xlabel("TF-IDF Score")
    plt.tight_layout()

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=150)
        plt.close()
    else:
        plt.show()


def generate_wordcloud(tfidf_scores, title, save_path=None): 
    """Word cloud based on TF-IDF weights. If save_path is given, saves PNG instead of showing.
    I am familiar with how word clouds work and their functionality, 
    but still, since it was new to me in python, I heavily needed help from AI"""
    if not tfidf_scores:
        return

    wc = WordCloud(width=800, height=400, background_color='white')
    wc.generate_from_frequencies(tfidf_scores)

    plt.figure(figsize=(8, 4))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title(f"Word Cloud – {title}")
    plt.tight_layout()

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=150)
        plt.close()
    else:
        plt.show()
