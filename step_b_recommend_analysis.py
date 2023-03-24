# Analysis 1: this part assess whether the TV show is recommended based on the scraped film reviews
"""
This module contains utility functions for processing text data.
"""
# install: pip install spacy
import sys
from unicodedata import category
import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import MDS
from fuzzywuzzy import fuzz
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
nltk.download('stopwords')  # download stopwords from NLTK library


def process_file(filename, excluding_stopwords=True):
    """
    Makes a histogram that contains the words from a file, in which stopwords are excluded

    Args:
    - filename: string, the name of the file to process
    - excluding_stopwords: boolean, whether to exclude stop words from the histogram

    Returns:
    - hist: dictionary, a map from each word to the number of times it appears in the file
    """
    hist = {}  # create an empty dictionary to store the word frequency
    open_file = open(filename, encoding='UTF8')  # open the file
    # define the set of characters to remove from each word
    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode)
         if category(chr(i)).startswith("P") and not category(chr(i)).startswith("Pc")])

    # Get the list of English stop words
    stop_words = set(nltk.corpus.stopwords.words('english'))
    for line in open_file:
        if line.startswith('*** END OF THIS PROJECT'):
            break
        line = line.replace('-', ' ')
        line = line.replace(
            chr(8212), ' '
        )  # Unicode 8212 is the HTML decimal entity for em dash
        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()
            # Ignore stop words if excluding_stopwords is True
            if excluding_stopwords and word in stop_words:
                continue
            # update the dictionary
            hist[word] = hist.get(word, 0) + 1
    # Create a new dictionary without stop words
    if excluding_stopwords:
        hist_without_stopwords = {word: count for word,
                                  count in hist.items() if word not in stop_words}
        return hist_without_stopwords
    else:
        return hist


def most_common(hist):
    """
    Returns a list of word-frequency pairs in descending order of frequency.

    Args:
    hist: a dictionary that contains the words and their frequencies.

    Returns:
    a list of tuples, where each tuple contains a word and its frequency, 
    sorted in descending order of frequency.
    """
    res = []  # Create an empty list
    for word in hist:
        freq = hist[word]  # extract the frequency from the hist dictionary
        res.append((freq, word))  # append tuples to res
    res.sort(reverse=True)  # descending orders
    return res


def analyze_sentiment(hist):
    """
    This function takes a histogram of words and their frequency as input 
    and uses the VADER sentiment analyzer to compute the average sentiment 
    score for the words. 
    The function then prints a recommendation for the film based on the
    average sentiment score.

    Args:
    - hist (dict): A histogram of words and their frequency.

    Result:
    - prints a recommendation for the film based on the average sentiment score.

    """
    nltk.data.path.append('/path/to/custom/nltk_data')
    # define an empty word list
    word_list = []
    # loop through each item in the dictionary and append words * frequency
    for key, value in hist.items():
        # use "extend" to add multiple copies of a word to the list
        word_list.extend([key]*value)
    analyzer = SentimentIntensityAnalyzer()
    # loop through each word in the word_list to calculate the score
    total_score = 0
    for word in word_list:
        scores = analyzer.polarity_scores(word)
        total_score += scores['compound']
    avg_score = total_score / len(word_list)
    if avg_score >= 0:
        print(f"The film is recommended, with avg_score of {avg_score}")
    else:
        print(f"The film is not recommended, with avg_score of {avg_score}")


def is_show_recommended(text_file):
    """
    This function reads a file containing reviews of a TV show, uses the VADER sentiment analyzer to
    determine the sentiment of each review, and prints a recommendation for the TV show based on 
    the majority sentiment of the reviews.

    Args:
    - text_file (str): the name of the text file containing the reviews

    Result:
    - prints a recommendation for the TV show based on the majority sentiment of the reviews.
    """

    nltk.download('vader_lexicon')
    sid = SentimentIntensityAnalyzer()

    with open(text_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    # set two variables for counting purposes
    num_positive_reviews = 0
    num_negative_reviews = 0
    # loop through each line to calculate sentimental score
    # and classify the words into positive and negative ones
    for line in lines:
        sentiment_scores = sid.polarity_scores(line)
        if sentiment_scores['compound'] >= 0.05:
            num_positive_reviews += 1
        elif sentiment_scores['compound'] <= -0.05:
            num_negative_reviews += 1

    if num_positive_reviews > num_negative_reviews:
        print(f"The TV show is recommended, with {num_positive_reviews} positive reviews and "
              f"{num_negative_reviews} negative reviews")
    elif num_positive_reviews < num_negative_reviews:
        print(f"The TV show is not recommended, with {num_positive_reviews} positive reviews"
              f" and {num_negative_reviews} negative reviews")
    else:
        print(f"Mixed reviews, with {num_positive_reviews} positive reviews and"
              f"{num_negative_reviews} negative reviews. Watch at your own discretion.")


def get_similarity_matrix(list1, list2):
    """
    Compute a similarity matrix between two lists of strings using fuzzy string matching.

    Args:
        list1 (list): A list of strings.
        list2 (list): A list of strings.

    Returns:
        An array representing the similarity scores between every pair of strings 
        in the two lists.
    """
    similarity_matrix = np.zeros((len(list1), len(list2)))
    for i, review1 in enumerate(list1):
        for j, review2 in enumerate(list2):
            score = fuzz.token_sort_ratio(review1, review2)
            similarity_matrix[i][j] = score
            similarity_matrix[j][i] = score  # enforce symmetry
    return similarity_matrix


def main():
    """
    Runs the main program, which processes reviews for the 
    TV shows 'Stranger Things' and 'Vampire Diaries'.

    This function reads review files for each TV show, 
    creates a dictionary of word frequencies for each show,
    finds the 20 most common words for each show and their corresponding frequencies, 
    analyzes the sentiment of each show's reviews using VADER, 
    and prints a recommendation for each show based on its average sentiment score.
    """
    # Stranger Things
    # Read stranger_things_reviews.txt and creates a dictionary:
    # values are words, keys are the frequencies of words
    stranger_things = process_file('stranger_things_reviews.txt',
                                   excluding_stopwords=True)
    print(stranger_things)

    # Find the 20 most common words in the review and the corresponding occurences
    st_20_common_words = most_common(stranger_things)
    print('The most common words are:')
    for freq, word in st_20_common_words[0:20]:
        print(word, '\\st_20_common_words', freq)

    # Analyze sentiment of the review
    analyze_sentiment(stranger_things)
    is_show_recommended('stranger_things_reviews.txt')

    # Vampire Diaries
    # Read vampire_diaries_reviews.txt and creates a dictionary:
    # values are words, keys are the frequencies of words
    vampire = process_file('vampire_diaries_reviews.txt',
                           excluding_stopwords=True)
    print(vampire)

    # Find the 20 most common words in the review and the corresponding occurences
    vp_20_common_words = most_common(vampire)
    print('The most common words are:')
    for freq, word in vp_20_common_words[0:20]:
        print(word, '\vp_20_common_words', freq)

    # Analyze sentiment
    analyze_sentiment(vampire)
    is_show_recommended('vampire_diaries_reviews.txt')

    # Read the first 50 lines from each file
    filename1 = "stranger_things_reviews.txt"
    with open(filename1, "r", encoding="utf-8") as file:
        list1 = [next(file).strip() for x in range(50)]

    filename2 = "vampire_diaries_reviews.txt"
    with open(filename2, "r", encoding="utf-8") as file:
        list2 = [next(file).strip() for x in range(50)]

    # Compute similarity matrix and apply MDS
    similarity_matrix = get_similarity_matrix(list1, list2)
    mds = MDS(n_components=2, dissimilarity='precomputed')
    results = mds.fit(similarity_matrix)

    # Print the positions of the reviews in the 2D space
    print(results.embedding_)

    # Visualize the 2D space
    x = [d[0] for d in results.embedding_]
    y = [d[1] for d in results.embedding_]

    plt.scatter(x, y)
    plt.show()


if __name__ == '__main__':
    main()
