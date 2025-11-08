from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

# Load English stopwords
stop_words = set(stopwords.words('english'))

def get_top_words(text, n=10):
    """Returns the top n most frequent non-stopwords in the text."""
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    counter = Counter(filtered_words)
    return counter.most_common(n)

def plot_word_frequencies(word_freqs):
    """Plots a bar chart of word frequencies."""
    words, counts = zip(*word_freqs)
    plt.figure(figsize=(10, 6))
    plt.bar(words, counts, color='skyblue')
    plt.title("Top 10 Most Frequent Words (Stopwords Removed)")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Ensure charts folder exists
    os.makedirs("charts", exist_ok=True)

    # Save the chart as a PNG file
    plt.savefig("charts/ebay_word_frequency.png")

    # Display the chart
    plt.show()
   