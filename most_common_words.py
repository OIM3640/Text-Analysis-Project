import remove_stop_words as rsw
import part1


def word_counter(text):
    """Counts the amount of times each word appears in the text. Dictionaries have a method called get that takes a key and a default value. If the key appears in the dictionary, that means the word has already appeared in the text and its count is increased by one. If not, then that means this is a new word. It is added to the dictionary and its count value is set as 1"""
    d = {}
    words = text.split()
    for word in words:
        word = part1.only_alpha(word.lower())
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    return d


def most_common_words(text, word_amount):
    """First word counter is called to get the total amount of each unique word. That dictionary is then sorted in descending order by making a list of the keys. Each word is paired in a new dictionary with the amount of time it appears. That dictionary is filled with the top however many most common words, depending on word_amount, and returned."""
    d_text = word_counter(text)
    # the code for ranked I got from chat GPT. The way that it works is it uses items() which returns each dict pair in a tuple. Then lambda is used to create a small, anonymous function. This function creates a dictionary of the words ranked in descending order of usage in the text. Since sorted() returns in ascending order, reverse=True is needed.
    #  https://chat.openai.com/share/57454618-03e9-4a7f-942d-1fa3a354a5b9
    ranked = dict(sorted(d_text.items(), key=lambda item: item[1], reverse=True))
    result = {}
    for i in range(word_amount):
        k = list(ranked.keys())[i]
        v = list(ranked.values())[i]
        result[k] = v
    return result


def most_common_words_wo_stop(text, word_amount, stop_words):
    """Essentially the same as most_common_words(). However, this one has the extra parameter of the stop_words list. This means that before calculating the word count, the stop words will be removed."""
    # calls remove_words from the other file to remove stop words.
    text = rsw.remove_words(text, stop_words)
    d_text = word_counter(text)
    ranked = dict(sorted(d_text.items(), key=lambda item: item[1], reverse=True))
    result = {}
    for i in range(word_amount):
        k = list(ranked.keys())[i]
        v = list(ranked.values())[i]
        result[k] = v
    return result


if __name__ == "__main__":
    test = "hi My soldiers push forward hi hi hi hi. My hi soldiers scream out. My soldiers RAGE j j j j j j j j j j j j j j j j!"
    stop_words = ["j", "hi"]
    word_amount = 2
    # test print statements
    # print(f"Here are the {word_amount} most used words in the text")
    # print("Including stop words:", most_common_words(test, word_amount))
    # print("Without stop words:", most_common_words_wo_stop(test, word_amount, stop_words))

    # Top 10 most common words in Thrilling Narratives of Mutiny, Murder and Piracy with and without stop words
    mmp = part1.murder_piracy
    cf = part1.Cuba_freedom
    hc = part1.history_Cuba
    # print(most_common_words(mmp, 50))
    cuba_stop_words = [
        "the",
        "of",
        "and",
        "to",
        "a",
        "in",
        "was",
        "on",
        "had",
        "with",
        "that",
        "were",
        "he",
        "they",
        "it",
        "which",
        "his",
        "we",
        "at",
        "for",
        "by",
        "as",
        "their",
        "from",
        "but",
        "our",
        "this",
        "them",
        "be",
        "not",
        "all",
        "who",
        "us",
        "her",
        "him",
        "or",
        "i",
        "so",
        "some",
        "an",
        "could",
        "my",
        "being",
        "been",
        "into",
        "about",
        "is",
        "have",
        "would",
        "no",
        "very",
        "would",
        "",
        "are",
    ]
    word_count = 10
    print(
        f"MMP's {word_count} most common words are {most_common_words_wo_stop(mmp, word_count, cuba_stop_words)}"
    )
    print()
    print(
        f"CF's {word_count} most common words are {most_common_words_wo_stop(cf, word_count, cuba_stop_words)}"
    )
    print()
    print(
        f"HC's {word_count} most common words are {most_common_words_wo_stop(hc, word_count, cuba_stop_words)}"
    )
