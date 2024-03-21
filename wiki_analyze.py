from mediawiki import MediaWiki
import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
from thefuzz import fuzz
import re

# import nltk
# from nltk.corpus import stopwords

wikipedia = MediaWiki()
NVDA_page = wikipedia.page("Nvidia")
AMD_page = wikipedia.page("AMD")
# add more pages to calculate clustering
pages_titles = [
    "Nvidia",
    "AMD",
    "Intel",
    "Graphics Processing Unit",
    "Central Processing Unit",
]
pages_content = []

for title in pages_titles:
    page = wikipedia.page(title)
    pages_content.append(page.content)

# Compute the similarity matrix
n = len(pages_content)
similarity_matrix = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        # Using fuzz.token_sort_ratio for more robustness against word order
        similarity_matrix[i, j] = (
            fuzz.token_sort_ratio(pages_content[i], pages_content[j]) / 100.0
        )  # Normalizing to [0, 1]

stop_words = set(
    [
        "i",
        "me",
        "my",
        "myself",
        "we",
        "our",
        "ours",
        "ourselves",
        "you",
        "your",
        "yours",
        "yourself",
        "yourselves",
        "he",
        "him",
        "his",
        "himself",
        "she",
        "her",
        "hers",
        "herself",
        "it",
        "its",
        "itself",
        "they",
        "them",
        "their",
        "theirs",
        "themselves",
        "what",
        "which",
        "who",
        "whom",
        "this",
        "that",
        "these",
        "those",
        "am",
        "is",
        "are",
        "was",
        "were",
        "be",
        "been",
        "being",
        "have",
        "has",
        "had",
        "having",
        "do",
        "does",
        "did",
        "doing",
        "a",
        "an",
        "the",
        "and",
        "but",
        "if",
        "or",
        "because",
        "as",
        "until",
        "while",
        "of",
        "at",
        "by",
        "for",
        "with",
        "about",
        "against",
        "between",
        "into",
        "through",
        "during",
        "before",
        "after",
        "above",
        "below",
        "to",
        "from",
        "up",
        "down",
        "in",
        "out",
        "on",
        "off",
        "over",
        "under",
        "again",
        "further",
        "then",
        "once",
        "here",
        "there",
        "when",
        "where",
        "why",
        "how",
        "all",
        "any",
        "both",
        "each",
        "few",
        "more",
        "most",
        "other",
        "some",
        "such",
        "no",
        "nor",
        "not",
        "only",
        "own",
        "same",
        "so",
        "than",
        "too",
        "very",
        "s",
        "t",
        "can",
        "will",
        "just",
        "don",
        "should",
        "now",
    ]
)

# nltk.download("stopwords")
# stop_words = set(stopwords.words("english"))

# print(NVDA.title)
# print(NVDA.content)


def create_histogram(text):
    hist = {}
    # Remove non-alphabetic characters and convert to lowercase
    words = re.findall(r"\b[a-z]+\b", text.lower())
    for word in words:
        if word not in stop_words:  # remove stopwords
            hist[word] = hist.get(word, 0) + 1
    return hist


# Characterizing by Word Frequencies
def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)


def most_common(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    if excluding_stopwords:
        return sorted(hist.items(), key=lambda x: x[1], reverse=True)
    else:
        return sorted(hist.items(), key=lambda x: x[1], reverse=True)


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.

    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist, excluding_stopwords=True)
    print("The most common words are:")
    for freq, word in t[0:num]:
        print(freq, "\t", word)


def main():
    hist = create_histogram(NVDA_page.content)
    print("Total number of words:", total_words(hist))
    print("Number of different words:", different_words(hist))

    t = most_common(hist, excluding_stopwords=True)
    print("The most common words are:")
    for freq, word in t[0:20]:
        print(word, "\t", freq)
    # Compute Text Similarity Using TheFuzz Library
    print(
        f"The Wekipdia page of Nvidia and AMD has a {fuzz.ratio(NVDA_page.content, AMD_page.content)}% similarity ratio."
    )
    print(
        f"The Wekipdia page of Nvidia and AMD has a {fuzz.token_sort_ratio(NVDA_page.content, AMD_page.content)}% sorted similarity ratio. (Persoanlly I believe in this score since the two companies are in the same industry field.)"  # This method is particularly useful when the order of words might vary but the words themselves are the same or very similar.
    )

    # Convert similarity to dissimilarity
    dissimilarities = 1 - similarity_matrix

    # Apply MDS
    mds = MDS(dissimilarity="precomputed", random_state=42)
    coords = mds.fit_transform(dissimilarities)

    # Plot the results
    plt.figure(figsize=(10, 8))
    plt.scatter(coords[:, 0], coords[:, 1], marker="o")
    for i, title in enumerate(pages_titles):
        plt.annotate(title, (coords[i, 0], coords[i, 1]))
    plt.title("Text Clustering with MDS")
    plt.xlabel("MDS Dimension 1")
    plt.ylabel("MDS Dimension 2")
    plt.show()


if __name__ == "__main__":
    main()
