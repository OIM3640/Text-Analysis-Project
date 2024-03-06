# Import library
import re
import sys
import urllib.request
from collections import Counter
from unicodedata import category

import pandas as pd
import pyLDAvis.gensim_models as gensimvis
import matplotlib.pyplot as plt
from gensim import corpora
from gensim.models import LdaModel
from nltk.corpus import (
    stopwords,
)  # Have to download stopwords list: python -m nltk.downloader stopwords
from nltk.stem import PorterStemmer
from gensim.models.coherencemodel import CoherenceModel


# Download file from url
def read_url(url):
    """
    Take a url downloadable

    url: string
    return: list of lines of downloaded text
    """
    with urllib.request.urlopen(url) as f:
        text = f.read().decode("utf-8")
    return text.splitlines()


def read_file(filepath):
    """
    Take a downloaded file

    filepath: string
    return: list of lines of downloaded text
    """
    with open(filepath, "r", encoding="utf-8") as df:
        text = df.read()
    return text.splitlines()


# Process data
def process_file(
    file,
    skip_header=True,
    punct=True,
    number=True,
    lowercase=True,
    roman_numerals=True,
    special_chars=True,
    single_chars=True,
    suppress_blanks=True,
):
    """Clean the data to obtain a dictionary with paragraph number and the text in paragraph

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    punct: boolean, strip punctuation if true
    number: boolean, remove isolated numbers and numbers followed by a single letter if true
    lowercase: boolean, convert all characters to lowercase
    roman_numerals: boolean, remove all roman_numerals if true
    special_chars: boolean, remove all special_chars if true
    single_chars: boolean, remove all single_chars if true
    suppress_blanks: boolean, compress extra blanks if true

    returns: a dictionary based on the parameters
    """
    paragraphs = {}
    paragraph_num = 1
    reading_content = False  # Flag to start recording lines after the header

    # Define characters to strip if punct is True
    strippables = "".join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )

    for line in file:
        # Start reading after the start marker
        if skip_header and "*** START OF THE PROJECT" in line:
            reading_content = True
            continue

        # Stop reading when the end marker is reached
        if "*** END OF THE PROJECT" in line:
            break

        if reading_content:
            # Replace hyphens with spaces to separate words
            line = line.replace("-", " ").replace(chr(8212), " ")

            # Cleaning operations based on parameters
            if number:
                line = re.sub(r"\b\d+\b|\b\d+[a-zA-Z]{1}\b", "", line)
            if roman_numerals:
                line = re.sub(r"\b[i,v,x,l,c,d,m]+\b", "", line, flags=re.IGNORECASE)
            if special_chars:
                line = re.sub(r"[^a-zA-Z0-9\s]", "", line)

            words_list = line.split()

            if punct:
                words_list = [word.strip(strippables) for word in words_list]
            if lowercase:
                words_list = [word.lower() for word in words_list]
            if single_chars:
                words_list = [word for word in words_list if len(word) > 1]
            if suppress_blanks:
                words_list = [word for word in words_list if word.strip()]

            # If the line is not empty, add the words to the current paragraph
            if words_list:
                paragraphs.setdefault(paragraph_num, []).extend(words_list)
            else:
                # If the line is empty, it is a new paragraph
                if paragraphs.get(
                    paragraph_num
                ):  # If the current paragraph has content
                    paragraph_num += 1  # Increase paragraph number

    return paragraphs


def stem_file(corpus: dict):
    """
    Apply stemming and stopword removal to the words in the dictionary.

    corpus: dict, a dictionary with paragraph number as key, text as value

    Return: stemmed dictionary
    """
    stop_words = set(
        stopwords.words("english")
    )  # Change to other langauge's stopwords if needed
    stemmer = PorterStemmer()

    stemmed_corpus = {}
    for paragraph_num, paragraph_text in corpus.items():
        filtered_words = [
            word for word in paragraph_text if word not in stop_words
        ]  # Remove stop words
        stemmed_words = [
            stemmer.stem(word) for word in filtered_words
        ]  # Stemmed the passed words
        stemmed_corpus[paragraph_num] = stemmed_words  # Add to the dictionary

    return stemmed_corpus


# Topic Modeling
def compute_coherence_values(
    dictionary, corpus, texts, limit, start=2, step=1, passes=10
):
    """
    Compute coherence values for different numbers of topics.

    dictionary: dict, the Gensim dictionary based on stemmed dictionary
    corpus: List, list of token for corpus
    texts: List, input texts from stemmed corpus
    limit: int, Maximum number of topics to test
    start: int, Starting number of topics
    step: int, Step size to iterate through number of topics
    passes: int, Number of passes through the corpus during training

    Returns:
    model_list: List of LDA topic models
    coherence_values: Coherence values corresponding to the LDA model with respective number of topics
    """
    coherence_values = []
    model_list = []
    for num_topics in range(start, limit, step):
        model = LdaModel(
            corpus=corpus, id2word=dictionary, num_topics=num_topics, passes=passes
        )
        model_list.append(model)
        coherencemodel = CoherenceModel(
            model=model, texts=texts, dictionary=dictionary, coherence="c_v"
        )
        coherence_values.append(coherencemodel.get_coherence())
    return model_list, coherence_values


def coherence_value_display(start, limit, step, coherence_values):
    '''
    Plot the coherence value based on number of topic.

    start: int, how much topics to start with
    limit: int, how much topics it limits to
    step: int, how large a step is to find the value
    coherence_value: float, the cv value calculated using compute_coherence_values()

    returns: a line plot that display the change of cv based on number of topics
    '''
    x = range(start, limit, step)
    plt.plot(x, coherence_values)
    plt.xlabel("Num Topics")
    plt.ylabel("Coherence score")
    plt.legend(("coherence_values"), loc="best")
    plt.show() #It seems that for default if I show a graph, code won't continue until I close it. Didn't find a solution

    for m, cv in zip(x, coherence_values):
        print("Num Topics =", m, " has Coherence Value of", round(cv, 4))


def best_num_topic(model_list, coherence_values, start, limit, step, topn):
    """
    Perform topic modeling using LDA on the provided corpus.

    dictionary: gensim.corpora.Dictionary
        The dictionary created from the processed corpus.
    corpus: list of list of (int, int)
        The corpus in Bag-of-Words format.
    num_topics: int
        The number of topics to model.
    passes: int
        The number of passes through the corpus during training.
    topn: int
        How many words for each topics you want to see

    Returns:
    lda_model: Gensim LDA model
    """
    topic_count = list(range(start, limit, step))
    best_model_index = coherence_values.index(max(coherence_values))
    best_lda_model = model_list[best_model_index]
    
    print(f"The best model has {topic_count[best_model_index]} topics.")
    print('\n')

    # Get word distribution for each topic
    for i in range(topic_count[best_model_index]):
        print(f"Topic {i}: ")
        print(best_lda_model.show_topic(i, topn))
    
    print('\n')

    return best_lda_model, topic_count[best_model_index]


def analyze_paragraph(lda_model, dictionary, paragraph, topn=10):
    """
    Analyze a specific preprocessed paragraph for topic distribution using a trained LDA model.
    Output the most relevant topic and a barchart showing the distribution of words in that topic

    Parameters:
    lda_model: Gensim LDA model
        The best LDA model.
    dictionary: gensim.corpora.Dictionary
        The dictionary created from the processed corpus.
    paragraph: list of str
        The preprocessed paragraph represented as a list of words.
    topn: int
        The number of top words to display for each topic.

    Returns:
    None
    """
    # Convert paragraph into bag-of-words format using the dictionary
    bow_vector = dictionary.doc2bow(paragraph)

    # Get the topic distribution for the paragraph
    topic_distribution = lda_model.get_document_topics(bow_vector)

    # Find the topic with the highest probability
    highest_topic, highest_prob = max(topic_distribution, key=lambda x: x[1]) # lamba using x[1] which is the second value in the tuple as key

    # Print the highest probability topic
    print(f"Highest Probability Topic {highest_topic}: {highest_prob:.3f}")

    # Print words associated with the highest probability topic
    words_in_topic = lda_model.show_topic(highest_topic, topn)
    print(f"Words in Highest Probability Topic {highest_topic}:")
    for word, prob in words_in_topic:
        print(f"  {word}: {prob:.3f}")

    # Create a bar chart for the word distribution in the highest probability topic
    words, probabilities = zip(*words_in_topic)
    plt.figure(figsize=(10,5))
    plt.bar(words, probabilities, color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Probabilities')
    plt.title(f'Distribution of Words in Topic {highest_topic}')
    plt.xticks(rotation=30, ha='right')
    plt.show() 

# Main function
def main():
    # Read data
    filepath = "data/Metamorphosis.txt"
    lines = read_file(filepath)
    # url = https://www.gutenberg.org/cache/epub/5200/pg5200.txt # Uncomment if input data is from url
    # lines = read_url(url)
    processed_corpus = process_file(lines)
    stemmed_corpus = stem_file(processed_corpus)

    # Use the stemmed data to come up with the three main parameter input for Gensim package
    dictionary = corpora.Dictionary(stemmed_corpus.values())
    corpus = [dictionary.doc2bow(text) for text in stemmed_corpus.values()]
    texts = list(stemmed_corpus.values())

    # Compute models based on different number of topics and the coherence values associate with it
    model_list, coherence_vals = compute_coherence_values(
        dictionary, corpus, texts, 20
    )

    # Display coherence values
    coherence_value_display(2, 20, 1, coherence_vals) # I think I should add a section for parameter definition of start, limit and step to avoid inconsistency, but I don't have time to do it...

    # Find the best number of topics based on coherence values; Use best number of topics to build the best topic model
    best_model, best_num_topics = best_num_topic(model_list, coherence_vals, 2, 20, 1, 3)

    # View the topic distribution for a given paragraph based on the best model
    paragraph = stemmed_corpus[32]  # Change the number to what ever paragraph you want to view
    analyze_paragraph(best_model, dictionary, paragraph)

if __name__ == "__main__":
    main()
