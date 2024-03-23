import re
import nltk
import random
import numpy as np
from thefuzz import fuzz
import matplotlib.pyplot as plt
from mediawiki import MediaWiki
from sklearn.manifold import MDS
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

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


# Using NLTK's built-in stopwords library
# nltk.download("stopwords")
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


def wiki_page_to_sentences(page):
    """Returns a randomly chosed sentences from a Wikipedia page."""
    sentences = nltk.sent_tokenize(page.content)
    random_sentence = random.choice(sentences)
    return random_sentence


def sentiment_analysis(text):
    """Returns the sentiment score of a text."""
    score = SentimentIntensityAnalyzer().polarity_scores(text)
    print(score)


# Compute the similarity matrix for clustering
n = len(pages_content)
similarity_matrix = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        # Using fuzz.token_sort_ratio for more robustness against word order
        similarity_matrix[i, j] = (
            fuzz.token_sort_ratio(pages_content[i], pages_content[j]) / 100.0
        )  # Normalizing to [0, 1]


def main():
    hist = create_histogram(NVDA_page.content)
    print("Total number of words:", total_words(hist))
    print("Number of different words:", different_words(hist))

    t = most_common(hist, excluding_stopwords=True)
    print()
    print("The most common words are:")
    for freq, word in t[0:20]:
        print(word, "\t", freq)
    print()

    # Compute Text Similarity Using TheFuzz Library
    print(
        f"The Wekipdia page of Nvidia and AMD has a {fuzz.ratio(NVDA_page.content, AMD_page.content)}% similarity ratio."
    )
    print()

    print(
        f"The Wekipdia page of Nvidia and AMD has a {fuzz.token_sort_ratio(NVDA_page.content, AMD_page.content)}% sorted similarity ratio. (Persoanlly I believe in this score since the two companies are in the same industry field.)"  # This method is particularly useful when the order of words might vary but the words themselves are the same or very similar.
    )

    print()
    print("The sentiment analysis of the Nvidia Wikipedia page is:")
    sentiment_analysis(NVDA_page.content)
    print()

    print("The sentiment analysis of the AMD Wikipedia page is:")
    sentiment_analysis(AMD_page.content)
    print()

    print("The random sentence of the Nvidia Wikipedia page is:")
    random_sentence_nvidia = wiki_page_to_sentences(NVDA_page)
    print(f"{random_sentence_nvidia}\n")
    print("The sentiment analysis of the random Nvidia Wikipedia sentence is:")
    sentiment_analysis(random_sentence_nvidia)
    print()

    print("The random sentence of the AMD Wikipedia page is:")
    random_sentence_amd = wiki_page_to_sentences(AMD_page)
    print(f"{random_sentence_amd}\n")
    print("The sentiment analysis of the random AMD Wikipedia sentence is:")
    sentiment_analysis(random_sentence_amd)

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
    titles = [
        "Nvidia",
        "AMD",
        "Intel",
        "Graphics Processing Unit",
        "Central Processing Unit",
    ]

    for i in range(len(titles)):
        plt.scatter(coords[i, 0], coords[i, 1], label=titles[i])

    for i in range(coords.shape[0]):
        plt.annotate(str(i), (coords[i, 0], coords[i, 1]))
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
