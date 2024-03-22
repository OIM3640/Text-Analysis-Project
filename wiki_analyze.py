from mediawiki import MediaWiki
import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
from thefuzz import fuzz
import re
import nltk
from nltk.corpus import stopwords

wikipedia = MediaWiki()
NVDA_page = wikipedia.page("Nvidia")
AMD_page = wikipedia.page("AMD")
# Add more pages to calculate clustering
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


nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

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
    # dissimilarity is 1 minus similarity
    dissimilarities = 1 - similarity_matrix

    # compute the embedding
    coord = MDS(dissimilarity="precomputed", random_state=42).fit_transform(
        dissimilarities
    )

    plt.scatter(coord[:, 0], coord[:, 1])

    # Label the points
    for i in range(coord.shape[0]):
        plt.annotate(str(i), (coord[i, :]))

    plt.show()
    # In this plot, "0" represents to "Nvidia", "1" represents to "AMD", "2" represents to "Intel", "3" represents to "Graphics Processing Unit", and "4" represents to "Central Processing Unit".


if __name__ == "__main__":
    main()
