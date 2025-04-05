import urllib.request
import string
from collections import Counter

# GenAI-assisted: Prompt "Can you give me a basic stopword list to filter common English words."
stopwords = {
    "the",
    "and",
    "to",
    "of",
    "a",
    "i",
    "it",
    "in",
    "that",
    "was",
    "he",
    "you",
    "as",
    "had",
    "with",
    "her",
    "for",
    "on",
    "at",
    "is",
    "his",
    "but",
    "be",
    "she",
    "they",
    "not",
    "by",
    "this",
    "or",
    "which",
    "have",
    "from",
    "all",
    "were",
    "my",
    "me",
    "so",
    "an",
    "one",
    "if",
}


def get_text(url):
    """Gets the text from the url using urllib"""
    try:
        with urllib.request.urlopen(url) as f:
            return f.read().decode("utf-8")
    except Exception as e:
        print("An error occurred:", e)
        return ""


def clean_text(text):
    """Cleans the text"""
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text


def remove_stopwords(words):
    """Removes common stopwords from the list of words."""
    return [word for word in words if word not in stopwords]


def count_word_frequencies(text):
    """Count word frequencies in the text"""
    words = text.split()
    words = remove_stopwords(words)
    return Counter(words)


def main():
    url = "https://www.gutenberg.org/cache/epub/11/pg11.txt"
    text = get_text(url)
    if not text:
        return
    text = clean_text(text)
    word_frequencies = count_word_frequencies(text)

    # Display the 10 most common words
    print("Top 10 most common words:")
    for word, freq in word_frequencies.most_common(10):
        print(f"{word}: {freq}")


if __name__ == "__main__":
    main()
