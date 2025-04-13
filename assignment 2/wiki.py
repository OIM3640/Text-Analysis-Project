from mediawiki import MediaWiki
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

nltk.download("stopwords")
nltk.download("punkt")

import matplotlib.pyplot as plt

wikipedia = MediaWiki()


def full_length(page):
    """
    Returns the length (total number of words) of a given Wikipedia page.
    """
    search = wikipedia.page(page).content
    return len(search)


def stop_words(page):
    """
    Parses through the given Wikipedia page, removing all of the stop words ("the," "a," "and," etc.)
    """
    search = wikipedia.page(page).content
    words = word_tokenize(search)
    stops = set(stopwords.words("english"))
    filtered_words = []
    for word in words:
        if word.lower() not in stops:
            filtered_words.append(word)
    filtered_text = " ".join(filtered_words)
    return filtered_text


def top_chars_frequency(page):
    """
    Find the top 10 most common characters of a given Wikipedia page.
    """
    search = wikipedia.page(page).content
    words = word_tokenize(search)
    frequency = FreqDist(words)
    top = frequency.most_common(10)
    return top


def top_chars_freq_no_stop(page):
    """
    Find the top 10 most common characters of a given Wikipedia page after removing all stop words.
    """
    search = wikipedia.page(page).content
    words = word_tokenize(search)
    stops = set(stopwords.words("english"))
    filtered_char = []
    for char in words:
        if char.lower() not in stops:
            filtered_char.append(char)
    frequency = FreqDist(filtered_char)
    top = frequency.most_common(10)
    return top


def bar_chart_full(top_chars_frequency):
    """
    Creates a bar chart that shows the top ten characters from the full text.
    """
    chars, freq = zip(*top_chars_frequency)
    plt.bar(chars, freq)
    plt.xlabel("Characters")
    plt.ylabel("Frequency")
    plt.title("Top 10 Most Frequent Characters")
    plt.show()


def bar_chart_no_stop(top_chars_freq_no_stop):
    """
    Creates a bar chart that shows the top ten characters from the full text after removing all of the stop words.
    """
    chars, freq = zip(*top_chars_freq_no_stop)
    plt.bar(chars, freq)
    plt.xlabel("Characters")
    plt.ylabel("Frequency")
    plt.title("Top 10 Most Frequent Characters Without Stop Words")
    plt.show()


def main():
    page = "Lionel Messi"

    # print(full_length(page))

    # print(stop_words(page))
    # print(len(stop_words(page)))

    # print(f"The top 10 most characters words in the Wikipedia page for '{page}': ")
    # for char, frequency in top_chars_frequency(page):
    #     print(f"{char}: {frequency}")

    # print(
    #     f"The top 10 most characters words in the Wikipedia page for '{page}' after removing all stop words: "
    # )
    # for char, frequency in top_chars_freq_no_stop(page):
    #     print(f"{char}: {frequency}")

    # top_chars_full = top_chars_frequency(page)
    # bar_chart_no_stop(top_chars_full)

    # top_chars_no_stop = top_chars_freq_no_stop(page)
    # bar_chart_no_stop(top_chars_no_stop)


if __name__ == "__main__":
    main()
