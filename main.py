# Text Analysis Project

# Part 1: Harvesting Text from the internet with differcent sources

# source 1: Project Gutenberg
import urllib.request

url = "https://www.gutenberg.org/cache/epub/11/pg11.txt"

with urllib.request.urlopen(url) as f:
    book_text = f.read().decode("utf-8")
    # print(book_text) # for testing

# Source 2: Wikipedia

from mediawiki import MediaWiki

wikipedia = MediaWiki()
babson = wikipedia.page("Babson College")  # Stores the wiki page into variable babson
print(babson.title)  # Display the title of the wiki page
print(babson.content)  # Display the content of the page

harvard = wikipedia.page("Harvard University")

# Source 3: Newspaper Articles

from newspaper import Article

url = "https://www.fox13now.com/news/fox-13-investigates/epa-seeking-to-regulate-fumes-from-local-medical-facilities"
article = Article(url)  # Stores the article in article variables
article.download()  # Download the content from the url
article.parse()  # Extract the informations from the article, stuch as text, author, etc
article_text = article.text  # Stores the text in a variable
article_author = article.authors  # Stores the author inside a variable
# print(article_author) # For test
# print(article_text) # For test

# Part 2: Analyzing your text

from gensim.parsing.preprocessing import remove_stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from thefuzz import fuzz
import networkx as nx
from nltk.tokenize import word_tokenize
from collections import Counter
from matplotlib import pyplot as plt
from pytagcloud import create_tag_image, make_tags


def remove_punctuations(text):
    """
    This function removes the punctuations from a given text and returns an output text. Source: ChatGDP
    """
    import string  # Gain access to all the string punctuations

    # str.maketrains maps each punctuations to a space
    translator = str.maketrans(string.punctuation, " " * len(string.punctuation))

    # The translate method then replacing each punctuation with a space.
    text = text.translate(translator)

    # Remove extra spaces
    text = " ".join(text.split())

    # returns text
    return text


def remove_stop_words(text):
    """
    This function removes all the stop words using remove_stopwords from gensim.parsing.preprocessing
    """
    # remove stopword is a built in function from gensim that removes stop words from a text.
    text = remove_stopwords(text)

    # returns text
    return text


def text_cleaning(text):
    """
    This function cleans the text by removing the stop words and the punctuations
    """
    # Make the text lower case
    text = text.lower()
    # First remove the puncuations
    text = remove_punctuations(text)

    # Then remove the stop words
    clean_text = remove_stop_words(text)

    # return a string of clean text
    return clean_text


def word_frequency(text):
    """
    This function returns a dictory with words as key and its frequency as values.
    """

    words = text.split()  # Splits the word into a list
    frequency = {}  # Creates an empty dictionary to store the word and its frequency

    for word in words:  # For every word in the words list
        # if the word is not already in frequency dict.
        if word not in frequency:
            # it will create a new key with value 0
            frequency[word] = 0
        # else it will increase the value of the word by 1
        frequency[word] += 1
    # return as a dictionary
    return frequency


def most_frequent(frequency):
    """
    This function prints the word with the highest frequency and its frequency given a dictionary.
    """
    # The max function takes the given dictionary and uses frequency.get to obtain values of each key
    max_word = max(frequency, key=frequency.get)

    # printing the most frequent words
    print(
        f"the word with highest frequency is {max_word} and its frequency is {frequency[max_word]}"
    )


def top_10_frequency(frequency):
    """
    This function outputs the top 10 words with its frequency
    """
    words_sorted = sorted(
        frequency, key=frequency.get, reverse=True
    )  # Sort the words in his by descending order.
    num = 10

    # the top 10 words will be added to the dictionary with word as key and frequency as value.
    for i in range(num):
        # If the length of the dictionary is less than the top 'x' numbers, the loop will break and print result
        if i >= len(words_sorted):
            break
        word = words_sorted[i]
        freq = frequency[word]

        # print word and its frequency
        print(f"{word}: {freq}")


def natural_lang(clean_text):
    """
    This function prints a polarity scores of a given text.
    """
    # The function takes the clean text and calculates a polarity score of the text
    score = SentimentIntensityAnalyzer().polarity_scores(clean_text)

    print(score)


def text_similarity(clean_text, clean_text_2):
    """
    This function output the similarity ratio between two given text
    """
    print(f"The ratio is {fuzz.ratio(clean_text, clean_text_2)}%")

    print(f"The partical ratio is {fuzz.partial_ratio(clean_text, clean_text_2)}%")

    print(f"The token sort ratio is {fuzz.token_sort_ratio(clean_text, clean_text_2)}%")


def word_network(clean_text):
    """
    This function takes the clean text and outputs a word network graph
    """
    # Tokenize the text and count the frequency of each word
    tokens = word_tokenize(clean_text.lower())
    word_counts = Counter(tokens)

    # Create an empty graph, and I chose the Digraph model
    G = nx.DiGraph()

    # Add nodes to the graph, every node is a unique word
    for word, count in word_counts.items():
        G.add_node(word, size=count)

    # Add edges to the graph
    for i in range(len(tokens) - 1):
        word1 = tokens[i]
        word2 = tokens[i + 1]

    # If there are no edge between two words, then there adds a edge with a weight of 1. If there is an edge, then increase it by 1.
    if not G.has_edge(word1, word2):
        G.add_edge(word1, word2, weight=1)
    else:
        G[word1][word2]["weight"] += 1

    # Draw the graph using the pyplot backend and using prebuilt function in nx and matplot
    pos = nx.spring_layout(G, k=0.5)
    # The spring_layout algorithm to position the nodes, the size of the nodes based degree, and the  width of the edges based on their weight
    nx.draw_networkx_nodes(
        G, pos, node_size=[d["size"] * 100 for (n, d) in G.nodes(data=True)]
    )
    nx.draw_networkx_edges(
        G, pos, width=[d["weight"] * 0.1 for (u, v, d) in G.edges(data=True)]
    )
    nx.draw_networkx_labels(G, pos)

    # turns off the axis and display the graph
    plt.axis("off")
    plt.show()


def wordCloud(clean_text):
    """
    This function takes the clean text and outputs a word cloud of the 50 words with most frequency.
    """
    # The counter function counds the frequency of each unique word in clean text. A tuple with word and frequency
    word_counts = Counter(clean_text.split())

    # The function takes the 50 most common words from the tuple and make a list
    top_words = word_counts.most_common(50)

    # The function makes_tag then create a list of tags from the top 50 words
    top_50 = make_tags(top_words)

    # Create a tag cloud image
    create_tag_image(top_50, "wordcloud.png", size=(800, 800), fontname="Lobster")

    # Display the tag cloud image using plt from matplot
    plt.figure(figsize=(8, 8))
    plt.imshow(plt.imread("wordcloud.png"))

    # Turns off the axis and display the graph
    plt.axis("off")
    plt.show()


def main():
    # Extract the two text
    text = (
        babson.content
    )  # Recalling from part 1, stored wiki content for babson into variable text for analysis

    text_2 = harvard.content

    # For the code belwo clean text is Babson content and clean text 2 is Harvard content

    # Clean the two text
    clean_text = text_cleaning(text)
    clean_text_2 = text_cleaning(text_2)

    # Create a dictionary with key and value
    frequency_1 = word_frequency(clean_text)
    frequency_2 = word_frequency(clean_text_2)

    # Display most frequent used word from both texts
    most_frequent(frequency_1)
    most_frequent(frequency_2)

    # Display a dictionary with top 10 words based on frequency, word as key and frequency as value
    top_10_frequency(frequency_1)
    top_10_frequency(frequency_2)

    # Display sentimental analysis for both text using natural lang
    natural_lang(clean_text)
    natural_lang(clean_text_2)

    # Display similiarity between both text
    text_similarity(clean_text, clean_text_2)

    # Create a word network diagram for both text
    word_network(clean_text)
    word_network(clean_text_2)

    # Create a word cloud for both text based on frequency
    wordCloud(clean_text)
    wordCloud(clean_text_2)


if __name__ == "__main__":
    main()
