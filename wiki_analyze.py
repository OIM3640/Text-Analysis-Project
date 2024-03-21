from mediawiki import MediaWiki
import re
import nltk
from nltk.corpus import stopwords

wikipedia = MediaWiki()
NVDA = wikipedia.page("Nvidia")
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


def main():
    hist = create_histogram(NVDA.content)
    print("Total number of words:", total_words(hist))
    print("Number of different words:", different_words(hist))


if __name__ == "__main__":
    main()
