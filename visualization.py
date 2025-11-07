import matplotlib.pyplot as plt
from collections import Counter
#import plotext as plt
print("Matplotlib is ready!")
def plot_sentiment(scores: dict):
    """
    Visualize sentiment scores for each text as a bar chart.
    scores: dictionary { 'filename': sentiment_score }
    """
    names = list(scores.keys())
    values = list(scores.values())

    plt.figure(figsize=(10, 6))
    bars = plt.bar(names, values)

    # color bars by sentiment
    for bar, val in zip(bars, values):
        if val > 0:
            bar.set_color("green")
        elif val < 0:
            bar.set_color("red")
        else:
            bar.set_color("gray")

    plt.axhline(0, color="black", linewidth=1)
    plt.title("Sentiment Scores of Project Gutenberg Texts")
    plt.ylabel("Sentiment Score (-1 to +1)")
    plt.xlabel("Book Title")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.show()

def top_n_counts_per_file(files, n=15, cleaner=None):
    result = {}
    for name, raw in files:
        text = cleaner(raw) if cleaner else raw
        counts = Counter(text.split())
        result[name] = counts.most_common(n)
    return result