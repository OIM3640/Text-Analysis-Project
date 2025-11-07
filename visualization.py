import matplotlib.pyplot as plt
import plotext as plt
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

def terminal_plot(scores: dict):
    """
    Plots sentiment scores as bars directly in the terminal.
    Green bars for positive, red for negative, gray for neutral.
    """
    names = list(scores.keys())
    values = list(scores.values())

    colors = []
    for v in values:
        if v > 0:
            colors.append("green")
        elif v < 0:
            colors.append("red")
        else:
            colors.append("white")

    plt.clear_plot()
    plt.bar(names, values, color=colors)
    plt.title("Sentiment Scores of Project Gutenberg Texts")
    plt.xlabel("Book Title")
    plt.ylabel("Sentiment (-1 to +1)")
    plt.plotsize(100, 25)  # width, height in terminal cells
    plt.show()

