from data_processing import import_file, spam_ham_lists, spam_ham_string, histogram
import matplotlib.pyplot as plt
from pytagcloud import create_tag_image, make_tags
from IPython.display import Image

def most_common_words(hist):
    """Finds the common words in spam/ham messages and corresponding frequencies.

    hist: histogram (dictionary)

    returns: list of (frequency, word) pairs
    """
    res = []
    stopwords = histogram("data/stopwords.txt", paragraph=False)

    for word in hist:
        if word in stopwords:
            continue
        freq = hist[word]
        res.append((freq, word))
    
    res.sort(reverse=True)
    return res


def top_unique_words(word_freq_1, word_freq_2):
    """Returns the top words found in message type 1 (e.g. spam) but not in message type 2 (e.g. ham).

    word_freq_1: list of (frequency, word) pairs, represents message type 1
    word_freq_2: list of (frequency, word) pairs, represents message type 2

    returns: list of (word, frequency) pairs
    """
    d1, d2 = dict(word_freq_1), dict(word_freq_2)
    res = []

    for freq, word in d1.items():
        if word not in d2.values(): # d2, like d1, has freq:word pairs
            word = d1[freq]
            res.append((word, freq))

    return res


def bar_chart_word_freq(word_freq, n, stat_name):
    """Bar chart that includes each word and corresponding frequency.

    word_freq: list of (word, frequency) pairs
    n: integer, number of words to include
    stat_name: string, name of statistic displayed on bar chart (e.g. "Top Spam Words")

    shows: bar chart
    """
    # Code source: ChatGPT
    # x is a list of n words, y is a list of n frequencies
    x, y = zip(*word_freq[0:n]) 

    plt.bar(x, y)
    plt.xlabel("Words")
    plt.ylabel("Frequencies")
    plt.title(f"Word Frequency Bar Chart: {stat_name}")

    plt.show()


def word_cloud(word_freq, n, cloud_name):
    """Generates a word cloud with n words.
    
    word_freq: list of (word, frequency) pairs
    n: integer, number of words to include
    cloud_name: string, word cloud image file name. Include .png (e.g. "word_cloud.png")

    shows: word cloud
    """
    # Code source: ChatGPT
    tags = make_tags(word_freq[0:n], maxsize=80)
    create_tag_image(tags, cloud_name, size=(900, 800), fontname="Nobile",)

    Image(filename=cloud_name)

def main():
    spam_dict = import_file()
    spam_list, ham_list = spam_ham_lists(spam_dict)
    spam_paragraph = spam_ham_string(spam_list)
    ham_paragraph = spam_ham_string(ham_list)
    spam_hist = histogram(spam_paragraph, paragraph=True)
    ham_hist = histogram(ham_paragraph, paragraph=True)

    spam_common_words = most_common_words(spam_hist)
    print('The most common words in spam messages are:')
    for freq, word in spam_common_words[0:20]:
        print(word, '\t', freq)

    ham_common_words = most_common_words(ham_hist)
    print('The most common words in ham (non-spam) messages are:')
    for freq, word in ham_common_words[0:20]:
        print(word, '\t', freq)

    top_spam_words = top_unique_words(spam_common_words, ham_common_words)
    print('The most common words in spam messages that are not in ham messages are:')
    for word, freq in top_spam_words[0:10]:
        print(word, '\t', freq)

    top_ham_words = top_unique_words(ham_common_words, spam_common_words)
    print('The most common words in ham messages that are not in spam messages are:')
    for word, freq in top_ham_words[0:10]:
        print(word, '\t', freq)

    bar_chart_word_freq(top_spam_words, n=10, stat_name="Top Spam Words")
    bar_chart_word_freq(top_ham_words, n=10, stat_name="Top Ham (Non-Spam) Words")

    word_cloud(top_spam_words, n=30, cloud_name="spam_cloud.png")
    word_cloud(top_ham_words, n=30, cloud_name="ham_cloud.png")

if __name__ == '__main__':
    main()