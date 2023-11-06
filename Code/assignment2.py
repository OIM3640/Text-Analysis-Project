import urllib.request
import random
import string
import sys
import nltk
from unicodedata import category
from thefuzz import fuzz
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("stopwords")
nltk.download("stopwords")
nltk.download("vader_lexicon")


url = "https://www.gutenberg.org/cache/epub/64317/pg64317.txt"
with urllib.request.urlopen(url) as f:
    text = f.read().decode("utf-8")


def process_file(text, skip_header=True):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    hist = {}

    if skip_header:
        skip_gutenberg_header(text)

    strippables = "".join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )

    for line in text.splitlines():
        if line.startswith("*** END OF THIS PROJECT"):
            break

        line = line.replace("-", " ")
        line = line.replace(chr(8212), " ")

        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()
            hist[word] = hist.get(word, 0) + 1

    return hist


def skip_gutenberg_header(text):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    lines = text.splitlines()
    for i in range(len(lines)):
        if lines[i].startswith("*** START OF THIS PROJECT"):
            return "\n".join(lines[i + 1 :])


def remove_stop_words(text):
    """
    Remove common English stop words from the text
    """
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words]
    return " ".join(filtered_words)


# I asked chatGPT on how to remove stopwords in text analysis. Here's the link: https://chat.openai.com/share/a3f9671d-fbb7-4860-baed-5ba0b48b4437


def word_frequencies(text):
    """
    Calculate word frequencies in The Great Gatsby

    This function tokenizes the input text, strips punctuation and converts words to lowercase,
    and then counts the frequency of each word in the text.
    """
    words = text.split()
    word_frequencies = {}
    for word in words:
        word = word.strip(string.punctuation).lower()
        word_frequencies[word] = word_frequencies.get(word, 0) + 1
    return word_frequencies


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)


def most_common(hist, excluding_stopwords=True):
    """Makes a list of word-freq pairs(tuples) in descending order of frequency.

    hist: map from word to frequency
    excluding_stopwords: a boolean value. If it is True, do not include any stopwords in the list.

    returns: list of (frequency, word) pairs
    """
    t = []

    stop_words = set(stopwords.words("english"))

    for word, freq in hist.items():
        if not word.strip():
            continue

        if excluding_stopwords:
            if word in stop_words:
                continue

        t.append((freq, word))

    t.sort(reverse=True)
    return t


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.

    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist)
    max_word_length = max(len(word) for _, word in t)
    for freq, word in t[:num]:
        formatted_word = f"{word:>{max_word_length}}"


def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.

    d1, d2: dictionaries
    """
    res = {}
    for key in d1:
        if key not in d2:
            res[key] = None
    return res


def random_word(hist):
    """Chooses a random word from a histogram.

    The probability of each word is proportional to its frequency.
    """
    t = []
    for word, freq in hist.items():
        t.extend([word] * freq)

    return random.choice(t)


# Split chapters for sentiment analysis
def split_text_into_chapters(text):
    """
    text is raw text, like 'CHAPTER 1, dffsafds... .CHAPTER 2.....'
    """
    chapters = text.split("CHAPTER")[1:]
    return chapters


def analyze_chapters(chapters):
    """
    Perform sentiment analysis
    """
    sia = SentimentIntensityAnalyzer()
    chapter_sentiments = []

    for chapter in chapters[1:]:
        sentiment = ""
        sentiment_scores = sia.polarity_scores(chapter)
        chapter_sentiments.append(sentiment)
    return chapter_sentiments


# I asked ChatGPT about educating me on sentiment analysis, and show me examples. Here's the link: https://chat.openai.com/share/3c8e9e06-e3c4-4b37-991f-bf75b94ccc49


def compute_similarity(book1_text, book2_text):
    """
    Compare the Great Gatsby to another book by the same author, check the similarity between two books
    """
    similarity_ratio = fuzz.ratio(book1_text, book2_text)
    return similarity_ratio


# text clustering
import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

# These are the similarities computed from the previous section
S = np.asarray(
    [
        [1.0, 0.90850572, 0.96451312, 0.97905034, 0.78340575],
        [0.90850572, 1.0, 0.95769915, 0.95030073, 0.87322494],
        [0.96451312, 0.95769915, 1.0, 0.98230284, 0.83381607],
        [0.97905034, 0.95030073, 0.98230284, 1.0, 0.82953109],
        [0.78340575, 0.87322494, 0.83381607, 0.82953109, 1.0],
    ]
)


# Dissimilarity is 1 minus similarity
dissimilarities = 1 - S

# Compute the embedding using multidimensional scaling (MDS)
coord = MDS(dissimilarity="precomputed").fit_transform(dissimilarities)

# Scatter plot of the MDS coordinates
plt.scatter(coord[:, 0], coord[:, 1])

# Label the points with their indices
for i in range(coord.shape[0]):
    plt.annotate(
        str(i), (coord[i, 0], coord[i, 1])
    )  # Corrected placement of parentheses

# Show the plot
plt.show()

# I asked ChatGPT to explain the sample code provided in the instruction for me. Here's the link: https://chat.openai.com/share/5cf7a57f-e0ce-4648-aa17-8b3f6e9c1fcd


# Markov Text Synthesis
class MarkovTextGenerator:
    def __init__(self):
        self.model = {}

    def train(self, text):
        words = text.split()
        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]
            if current_word in self.model:
                self.model[current_word].append(next_word)
            else:
                self.model[current_word] = [next_word]

    def generate_text(self, length=100):
        current_word = random.choice(list(self.model.keys()))
        generated_text = [current_word.capitalize()]
        for _ in range(length - 1):
            if current_word in self.model:
                next_word = random.choice(self.model[current_word])
                generated_text.append(next_word)
                current_word = next_word
            else:
                break
        return " ".join(generated_text)


# I asked ChatGPT to educate me on what is Markov Text Synthesis and show me sample code. Here's the link: https://chat.openai.com/share/eda06a43-6ab9-4fe4-ae5e-3bb9c8df7f61


def main():
    """
    Main function for text analysis and processing
    """
    url_great_gatsby = "https://www.gutenberg.org/cache/epub/64317/pg64317.txt"
    url_other_book = "https://www.gutenberg.org/cache/epub/805/pg805.txt"

    with urllib.request.urlopen(url_great_gatsby) as f:
        text_great_gatsby = f.read().decode("utf-8")

    with urllib.request.urlopen(url_other_book) as f:
        text_other_book = f.read().decode("utf-8")

    # Process and analyze "The Great Gatsby" and its similarity to another book
    hist_other_book = process_file(text_other_book, skip_header=True)
    similarity = compute_similarity(text, text_other_book)
    print("Similarity to Another Book by the Same Author:", similarity)

    hist = process_file(text, skip_header=True)
    print("Total number of words:", total_words(hist))
    print("Number of different words:", different_words(hist))

    # Print the top 20 words in the book
    print("Top 20 Words in 'The Great Gatsby':")
    top_20_great_gatsby = most_common(hist, excluding_stopwords=True)[:20]
    for freq, word in top_20_great_gatsby:
        print(f"{word}: {freq}")

    chapters = split_text_into_chapters(text)
    chapters_other_book = split_text_into_chapters(text_other_book)
    chapters_great_gatsby = split_text_into_chapters(text_great_gatsby)

    chapter_sentiments = analyze_chapters(chapters)
    chapter_sentiments_other_book = analyze_chapters(chapters_other_book)

    # Perform sentiment analysis on the entire text
    t = most_common(hist, excluding_stopwords=True)
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    # Print sentiment analysis results
    print("Sentiment Analysis: ")
    print("Positive:", sentiment["pos"])
    print("Neutral:", sentiment["neu"])
    print("Negative:", sentiment["neg"])
    print("Compound:", sentiment["compound"])

    # Generate and print random words from the book
    words = process_file("data/words.txt", skip_header=False)
    print("\nHere are some random words from the book:")
    for i in range(100):
        print(random_word(hist), end=" ")

    # Markov Text Synthesis
    markov_generator = MarkovTextGenerator()
    markov_generator.train(text)
    generated_text = markov_generator.generate_text(length=200)
    print("\nGenerated Text:")
    print(generated_text)


if __name__ == "__main__":
    main()
