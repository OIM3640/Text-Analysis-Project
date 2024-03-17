### Theme analysis for Metamorphosis ###


## Download the book from gutenberg ##

import urllib.request
import pickle
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Metamorphosis txt (main part)
url = "https://www.gutenberg.org/cache/epub/5200/pg5200.txt"
with urllib.request.urlopen(url) as f:
    metamorphosis = f.read().decode("utf-8")
    # print(metamorphosis)


# The Trail txt of the second book used for vector space representation
url2 = "https://www.gutenberg.org/cache/epub/7849/pg7849.txt"
with urllib.request.urlopen(url2) as f:
    trail = f.read().decode("utf-8")


## Pickling Data ##

# Metamorphosis
with open("metamorphosis.pkl", "wb") as f:
    pickle.dump(metamorphosis, f)
# wb => writes data without changing it
# saving in binary format

# Load data from the file
with open("metamorphosis.pkl", "rb") as f:
    book = pickle.load(f)
# rb => reads data without changing it

# The Trail
with open("trail.pkl", "wb") as f:
    pickle.dump(trail, f)

# Load data from the file
with open("trail.pkl", "rb") as f:
    book2 = pickle.load(f)


# Start cleaning the text (Code modified from class materials)
import sys
from unicodedata import category


def process_file(bookname):
    """
    Reads the Metamorphosis book already read

    Clean the text by excluding special characters and converting to lower cases

    Exluding the header and the footer

    Excluding stop words

    Returns a dictionary with each unique words and thier counts
    """
    hist = {}
    fp = bookname
    in_project = False  # Initialize in_project to False

    # if skip_header:
    #     skip_gutenberg_header(fp)
    # For some reason this line did not work so I changed to another way

    strippables = "".join(
        chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")
    )  # https://stackoverflow.com/questions/60983836/complete-set-of-punctuation-marks-for-python-not-just-ascii

    # split the book by line
    # in_project is defined so we only access text in between start and end of the project
    # when encountering start of the project => in_project is TRUE and
    # we continue to read the lines until we reaches end of the project
    for line in fp.split("\n"):
        if "*** START OF THE PROJECT" in line:
            in_project = True
            continue
        elif "*** END OF THE PROJECT" in line:
            break

        if in_project:
            line = line.replace("-", " ")
            line = line.replace(
                chr(8212), " "
            )  # Unicode 8212 is the HTML decimal entity for em dash

            for word in line.split():
                # word could be 'Sussex.'
                word = word.strip(strippables)
                word = word.lower()

                # update the dictionary
                hist[word] = hist.get(word, 0) + 1

    stop = open("stopwords.txt")

    for line in stop:
        stopwords = line.strip()
        if stopwords in hist:
            del hist[stopwords]

    return hist


def most_common(hist):
    """
    Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    """

    sort = sorted(hist.items(), key=lambda x: x[1], reverse=True)

    return sort


# Originally, the code I copied from class material on textual analysis did not work
# as it only gives me a dictionary consist of letters as key instead of words
# I asked help from ChatGPT where I asked it how to get words instead of letters
# Below are some modifications on the original code:
# 1. changed the argument filename direcly to the already loaded file
# 2. changing the ways to delet header and footer using for loop


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)


def cleantext(text):
    """
    Cleans the text by excluding special characters and converting to lower case

    Returns a list of all the words in the book

    This is similar to process_file function but instead of a dictionary

    The output is a list of words only
    """
    hist = []

    in_project = False

    strippables = "".join(
        chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")
    )

    for line in text.split("\n"):
        if "*** START OF THE PROJECT" in line:
            in_project = True
            continue
        elif "*** END OF THE PROJECT" in line:
            break

        if in_project:
            line = line.replace("-", " ")
            line = line.replace(chr(8212), " ")
            for word in line.split():
                word = word.strip(strippables)
                word = word.lower()

                hist.append(word)

    stop = open("stopwords.txt")
    remove_words = []

    for line in stop:
        stopwords = line.strip()
        if stopwords in hist:
            remove_words.append(stopwords)

    hist = [word for word in hist if word not in remove_words]
    # This line is coded with help of ChatGPT:https://chat.openai.com/c/56bf14ac-01c2-4376-9d81-15ad9ad7ba57
    # iterate through each word in hist (list of cleaned words in the text)
    # only keep words that are not in the words to remove (stop words)

    return hist


## Natrual Language Processing ##
import nltk

nltk.download("vader_lexicon")

from nltk.sentiment.vader import SentimentIntensityAnalyzer


## calculate the sentiment score for the top 50 most popular words in a text ##
def sentiment_of_context(bookname):
    """
    Returns a dictionary of top 50 most frequently appearing words as key and thier context sentiment scores are value

    Context sentiment score is generated by analysing the nearest 5 words before and after the words

    The analysis is for the book Metamorphosis
    """
    dict = {}

    text = cleantext(bookname)
    hist = process_file(bookname)

    commonwords = most_common(hist)
    commonwords50 = commonwords[:50]
    # this is a list of tuple in form of word and frequency

    for word, freq in commonwords50:
        if word in text:
            # Goal => find the 5 words before and after the most common word
            # to understand the context of the word
            # and access the sentiment using NLP
            # Note => avoide going over the lenght of the text

            start_index = max(0, text.index(word) - 5)
            end_index = min(len(text), text.index(word) + 6)
            # Add 6 => X include the top

            # Knit all the nearby words together
            context = text[start_index:end_index]  # note that this is list

            sentence = " ".join(context)
            # join list to a str by blank space => make up a sentence

            # get the sentiment score for the context
            score = SentimentIntensityAnalyzer().polarity_scores(sentence)

            dict[word] = score
    return dict


## calculate the sentiment score for the whole book ##
def sentiment_of_book(bookname):
    text = " ".join(cleantext(bookname))
    score = SentimentIntensityAnalyzer().polarity_scores(text)
    return score


## wordcloud ##
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def wordcloud(bookname):
    """
    Displays the wordcloud of the book Metamorphosis

    Most frequently appearing words would show up bigger
    """
    text = bookname
    wordcloud = WordCloud(
        width=800, height=400, background_color="white", random_state=88
    ).generate(text)
    # random_state => similar to set.seed which ensure same results for wordcloud

    # Display the generated word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


## Side by Side Bar Charts for 2 Books ##
# chat history: https://chat.openai.com/c/56bf14ac-01c2-4376-9d81-15ad9ad7ba57

import matplotlib.pyplot as plt
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer


def sbs_barchart():
    """
    Plot 2 bar charts side by side showing the top 50 most common words in each book
    """
    # clean both text and convert list into str
    # each book is a document
    metamorphosis = " ".join(cleantext(book))
    trail = " ".join(cleantext(book2))

    # creat the corpus
    documents = [metamorphosis, trail]

    # CountVectorizer
    vectorizer = CountVectorizer()
    # this is similar to material covered in machine learning class
    # where texts are tokenized into segments of individual words
    # each unigrams (individual words) in the document inthe corpus is counted
    # a final matrix is contructed:
    # row = document (metamorphosis or trail) note that both text together is refered as a corpus
    # column = unigrams from the vocabulary (set of unique terms underlying a corpus)
    # this is somewhat similar to the process_file function defined before

    # fitting the corpus into the matrix
    # fit_transform => analyse the corpus following the logic above (analyse each documents)
    bow_matrix = vectorizer.fit_transform(documents)
    # bow means Bag of Words => basic terms in NLP of Text
    # essentially similar to process_file function where each unique word is stored with the frequency

    # get the unique words
    vocabulary = vectorizer.get_feature_names_out()
    # get_feature_names_out => get all the unique unigrams in the vocab list (x freq)
    # print(vocabulary) # for testing and learning

    # convert the document-term matrix to a dense array
    bow_matrix_dense = bow_matrix.toarray()
    # dense array => shows zero values
    # bow_matrix => only show non-zero values

    # Get top 50 most frequent terms for each document
    top50words_book = np.argsort(bow_matrix_dense[0])[::-1][:50]
    top50words_book2 = np.argsort(bow_matrix_dense[1])[::-1][:50]
    # np.argsort(...) => sort the matrix by frequency (bow_matrix_dense[0] or [1]) in ascending order
    # note that the output is only words
    # [::-1] => slicing where the search start from bottom (most frequent) to top
    # [:50] => search till the 50th most common term (inclusive of the 50th term)

    # # another way (using existing function)
    # hist1 = process_file(book)
    # top50words_book = []
    # top50words_book_orig = most_common(hist1)[:50]
    # for words, freq in top50words_book_orig:
    #     top50words_book.append(words)

    # hist2 = process_file(book2)
    # top50words_book2 = []
    # top50words_book_orig2 = most_common(hist2)[:50]
    # for words, freq in top50words_book_orig2:
    #     top50words_book2.append(words)

    # # Get the top 50 terms and their frequencies for each document
    # top_terms_book = [word for word in top50words_book if word in vocabulary]
    # top_frequencies_book = [bow_matrix_dense[0][top50words_book.index(word)] for word in top_terms_book]

    # top_terms_book2 = [word for word in top50words_book2 if word in vocabulary]
    # top_frequencies_book2 = [bow_matrix_dense[1][top50words_book2.index(word)] for word in top_terms_book2]

    ## why #? The code provided above does not plot in descending order from the most frequent words to the least frequnt ##

    # Get the top 50 terms and their frequencies for each document
    top_terms_book = [vocabulary[i] for i in top50words_book]
    # iterate through the array vocabulary only for words that appears in top_indice_book (top 50 most common words)
    top_frequencies_book = [bow_matrix_dense[0][i] for i in top50words_book]
    # retrives the frequency of each popular words from the vocab ([0] and [1] is to specify which document to iterate)
    # the i correseponds the each most common words

    top_terms_book2 = [vocabulary[i] for i in top50words_book2]
    top_frequencies_book2 = [bow_matrix_dense[1][i] for i in top50words_book2]

    # Plot the top 50 most frequent terms separately for each book
    plt.figure(figsize=(18, 10))
    # set the dimention of the plot => base 18, height 10

    # This part is for bar chars of Metamorphosis

    plt.subplot(1, 2, 1)
    # divide into 2 barchats
    # (1 row of block with 2 columns of blocks and the last 1 means the below code affects the plot on the left)

    # Settings for bar
    plt.barh(np.arange(len(top_terms_book)), top_frequencies_book, color="skyblue")
    # np.arange(len(top_terms_book)) => general number of bars that equals to number of words in top_term_book
    # each bar is a most common words and length of bars represents frequencies
    # bar is colored as skyblue

    # Setting for lables
    plt.yticks(np.arange(len(top_terms_book)), top_terms_book)
    # np.arange(len(top_terms_book)) => ensure the lable corresponds to the bar
    # bar is derived from top_terms_book
    # this is pobably why an array is important as the index is essential to make sure the label matches

    # adding title and x bar
    plt.xlabel("Frequency")
    plt.title("Top 50 Most Commonly Appearing Words in Metamorphosis by Kafka")
    plt.gca().invert_yaxis()  # Invert y-axis to have the highest frequency at the top

    # This part is for bar chart of The Trail

    plt.subplot(1, 2, 2)  # change subject
    plt.barh(np.arange(len(top_terms_book2)), top_frequencies_book2, color="lightgreen")
    plt.yticks(np.arange(len(top_terms_book2)), top_terms_book2)

    # adding title and x bar
    plt.xlabel("Frequency")
    plt.title("Top 50 Most Commonly Appearing Words in The Trail by Kafka")

    # sort bars from longest to the shortest
    # sort yaxies
    plt.gca().invert_yaxis()

    plt.subplots_adjust(wspace=200)  # moves the two subplots alittle apart

    plt.tight_layout()  # make sure the plots fits the given space
    plt.show()


## Vector Space Representation ##
# This is a concept I learned in Machine learning were IDF (Inverse Document Frequency)
# is calculated to count the number of times a term appears in a document relative to the total
# number of time the term appears in the document
# it evaluates the relative frequency and measure the prevalence of a term across the entire corpus
# the formulat is idf(t,D) = ln(# doc in the corpus / # docs contains the term)
# Using IDF we can visualize relatively how similar and different the two books are in terms of the material inside
# chat history: https://chat.openai.com/c/56bf14ac-01c2-4376-9d81-15ad9ad7ba57

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer


def vsr(text1, text2, title1, title2):
    """
    Plots the visual space representation of text1 and text2 based on IDF

    The function takes 4 arguments:
    text1, text2 and there corresponding titles in str title1 and title2

    The distance between the two point represents how similar the 2 texts are:
    the further apart they are the more they are not similar

    x axies => how content of text1 relates to text2
    y axies => how content of text2 relates to text1
    """
    # Join the cleaned text from the input objects
    metamorphosis = " ".join(cleantext(text1))
    trail = " ".join(cleantext(text2))

    # Initialize TfidfVectorizer object with IDF weighting
    # this is similar tot he vector before but instead of counting frequencies it calculates IDF
    vectorizer = TfidfVectorizer()

    # fit each book into the vector above
    vsm_matrix = vectorizer.fit_transform([metamorphosis, trail])

    # Perform PCA for dimensionality reduction
    pca = PCA(n_components=2)  # similar to pruning in a sense
    # reduce the dimentions of the text to 2 (since we only have 2 books)
    vsm_matrix_reduced = pca.fit_transform(vsm_matrix.toarray())

    # plotting the final graph

    # setting initial dimention
    plt.figure(figsize=(8, 6))

    plt.scatter(vsm_matrix_reduced[:, 0], vsm_matrix_reduced[:, 1])
    # in simple terms:
    # x component or axies = book1, y component or axies = book2 (this is a scatter plot)

    # labeling the two points
    labels = [title1, title2]

    for i, label in enumerate(labels):
        plt.annotate(label, (vsm_matrix_reduced[i, 0], vsm_matrix_reduced[i, 1]))
    # i corresponds the which point we are refering to
    # 1 = text1, 2 = text2
    # while the 0 and 1 on the right size specified the x and y axies

    # another way
    # plt.annotate(title1, (vsm_matrix_reduced[0, 0], vsm_matrix_reduced[0, 1]))
    # plt.annotate(title2, (vsm_matrix_reduced[1, 0], vsm_matrix_reduced[1, 1]))

    plt.title(f"Vector Space Representation by IDF for {title1} and {title2}")
    plt.xlabel("Dimention 1")
    plt.ylabel("Dimention 2")
    plt.show()


def main():
    hist = process_file(book)  # This text file is downloaded from gutenberg.org
    # print(hist)
    print("Simple Text Cleaning and Analysis for Metamorphosis:")
    print("\nTotal number of words excluding stop words:", total_words(hist))
    print("Number of different words:", different_words(hist))

    t = most_common(hist)
    print("\nThe most common 20 words are:")
    for freq, word in t[0:20]:
        print(word, "\t", freq)
    print("This means that the book circumspect around these topics.")

    hist1 = process_file(book2)  # This text file is downloaded from gutenberg.org
    print("\nSimple Text Cleaning and Analysis for The Trail:")
    print("\nTotal number of words excluding stop words:", total_words(hist1))
    print("Number of different words:", different_words(hist1))

    t1 = most_common(hist1)
    print("\nThe most common 20 words are:")
    for freq, word in t1[0:20]:
        print(word, "\t", freq)
    print("This means that the book circumspect around these topics.")

    print("\nTextual Analysis:")

    ## NLP Sentiment of Context ##
    sentiments = sentiment_of_context(book)

    # Prints the top 10 most common words and thier correseponding context sentiment scores
    print(
        "\nThe context sentiment scores for the 10 most commonly appearing words in Metamorphosis are:"
    )
    for key, value in list(sentiments.items())[:10]:
        # converts dictionary into list and only loop for top 10 keys
        print(f"{key}: {value}")

    print("\nThe overall sentiment score for Metamorphosis by Kafka is:")
    overallscore1 = sentiment_of_book(book)
    print(overallscore1)

    sentiments1 = sentiment_of_context(book2)

    # Prints the top 10 most common words and thier correseponding context sentiment scores
    print(
        "\nThe context sentiment scores for the 10 most commonly appearing words in The Trail are:"
    )
    for key, value in list(sentiments1.items())[:10]:
        # converts dictionary into list and only loop for top 10 keys
        print(f"{key}: {value}")

    print("\nThe overall sentiment score for The Trail by Kafka is:")
    overallscore2 = sentiment_of_book(book2)
    print(overallscore2)

    print(
        "\nDeciphering sentiment scores: compound score (0 extremely negative, 1 extremely positive)"
    )

    wordcloud(book)
    wordcloud(book2)

    sbs_barchart()

    vsr(book, book2, "Metamorphosis", "The Trail")


if __name__ == "__main__":
    main()


# ChatGPT Chat History
# https://chat.openai.com/c/c96b6bac-e943-40b9-98c4-9b9a0b355131
# Wordcloud chat link: https://chat.openai.com/c/56bf14ac-01c2-4376-9d81-15ad9ad7ba57
# reading multiple files: https://stackoverflow.com/questions/208120/how-to-read-and-write-multiple-files
