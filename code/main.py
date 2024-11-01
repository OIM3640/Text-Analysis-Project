import string
import nltk
import os
import unicodedata
import urllib.request
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

# Download Packages for Text and Data clean-up:
# nltk.download('stopwords')


def main():
    # Load text from URLs
    url1 = "https://www.gutenberg.org/cache/epub/6130/pg6130.txt"  # The Iliad
    url2 = "https://www.gutenberg.org/cache/epub/1727/pg1727.txt"  # The Odyssey

    with urllib.request.urlopen(url1) as f:
        text_iliad = f.read().decode("utf-8")
    with urllib.request.urlopen(url2) as f:
        text_odyssey = f.read().decode("utf-8")

    """Remove unnecessary text, resulting in a text without the boilerplate intro.
     The two sentences are the start and end of both actual texts """
    text_iliad = remove_unnecessary_text(
        text_iliad, "Scepticism is as much the result of knowledge", "March 25, 1720"
    )
    text_odyssey = remove_unnecessary_text(
        text_odyssey, "Tell me, O Muse,", "between the two contending parties"
    )

    """Print the first 500 characters for testing"""
    # print("\nThe Iliad (First 500 characters after removing unnecessary text):")
    # print(text_iliad[:500])
    # print("\nThe Odyssey (First 500 characters after removing unnecessary text):")
    # print(text_odyssey[:500])

    """Cleaning Text after unnecessary text removal"""
    cleaned_words_iliad = clean_data(text_iliad)
    cleaned_words_odyssey = clean_data(text_odyssey)

    """Print the first 50 cleaned words for testing"""
    # print("\nCleaned Words from The Iliad (First 50 words):")
    # print(cleaned_words_iliad[:50])
    # print("\nCleaned Words from The Odyssey (First 50 words):")
    # print(cleaned_words_odyssey[:50])

    # Create histograms (word frequency dictionaries)
    hist_iliad = count_word_frequencies(cleaned_words_iliad)
    hist_odyssey = count_word_frequencies(cleaned_words_odyssey)

    # Calculate total words for each text
    total_words_iliad = total_words(hist_iliad)
    total_words_odyssey = total_words(hist_odyssey)

    # Print total and different words
    print(f"The Iliad - Total words: {total_words(hist_iliad)}")
    print(f"The Iliad - Different words: {different_words(hist_iliad)}")

    print(f"\nThe Odyssey - Total words: {total_words(hist_odyssey)}")
    print(f"The Odyssey - Different words: {different_words(hist_odyssey)}")

    # Print the 10 most common words in each text
    print("\nThe Iliad - Most Common Words:")
    print_most_common(hist_iliad, num=10)

    print("\nThe Odyssey - Most Common Words:")
    print_most_common(hist_odyssey, num=10)

    top_10_relative_words = top_relative_words(
        hist_iliad, total_words_iliad, hist_odyssey, total_words_odyssey, num=10
    )

    print("\nTop 10 words with the highest relative frequency in both texts:")
    for word, combined_rel_freq in top_10_relative_words:
        print(f"'{word}' with combined relative frequency of {combined_rel_freq:.6f}")


def remove_unnecessary_text(text, start_marker, end_marker):
    """
    Function removes unnecessary text from the provided text, focusing on
    introductory content, and anything after the end marker.
    The start and end markers are included in the returned text.
    """
    s = []
    started = False

    for line in text.split("\n"):
        if start_marker in line:
            started = True
            s.append(line)  # Includes the start marker in the text
            continue
        if end_marker in line:
            s.append(line)  # Includes the end marker in the text
            break
        if started:
            s.append(line)

    return "\n".join(s)


def clean_data(text):
    """
    Function utilizes NLTK to clean up the data/words/characters in the text.
    """
    text = (
        unicodedata.normalize("NFKD", text)
        .encode("ascii", "ignore")
        .decode("utf-8", "ignore")
    )

    # Tokenize text using RegexpTokenizer to remove punctuation
    tokenizer = RegexpTokenizer(r"\w+")
    words = tokenizer.tokenize(text)

    words = [word.lower() for word in words]

    # Remove English stop words
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]

    return words


############################
############################
# ANALYSIS OF THE CODE
############################
############################


def count_word_frequencies(words):
    """ """
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)


def most_common(hist, excluding_stopwords=True):
    """Makes a list of word-freq pairs (tuples) in descending order of frequency.
    hist: map from word to frequency
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
    """Prints the most common words in a histogram and their frequencies.
    """
    t = most_common(hist)
    max_word_length = max(len(word) for _, word in t)
    for freq, word in t[:num]:
        formatted_word = f"{word:>{max_word_length}}"
        print(f"{formatted_word} : {freq}")

### For this function I had in mind to find the frequency of certain words within both texts.
# The goal is to calculate how common certain words are relative to the size of each text.
# However I was not sure and I utilised ChatGPT to explain it in a much clearer way.

def top_relative_words(hist1, total_words1, hist2, total_words2, num=10):
    common_words = set(hist1) & set(hist2)

    relative_word_list = []
    for word in common_words:
        combined_relative_frequency = (hist1[word] / total_words1) + (
            hist2[word] / total_words2
        )
        relative_word_list.append((word, combined_relative_frequency))

    # Sort the list by combined relative frequency in descending order
    relative_word_list.sort(key=lambda x: x[1], reverse=True)

    return relative_word_list[:num]


if __name__ == "__main__":
    main()
