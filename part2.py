import urllib.request
import random
import string
import sys
from unicodedata import category
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from thefuzz import fuzz


def word_freq(filename, skip_header): # Original from analyze_book.py
    """
    Creates a dictionary where the keys are words that appear and the values are frequencies of words in the text
    """
    word_freq = {}
    fp = open(filename, encoding="utf-8")

    if skip_header:
        skip_gutenberg_header(fp)

    strippables = string.punctuation + string.whitespace

    for line in fp:
        if line.startswith("*** END OF THE PROJECT"):
            break

        line = line.replace("-", " ")
        line = line.replace(chr(8212), " ")

        for word in line.split():
            word = word.strip(strippables).lower()
            
            word_freq[word] = word_freq.get(word, 0) + 1

    fp.close()
    return word_freq

def skip_gutenberg_header(fp): # Original from analyze_book.py
    """
    Skips the Gutenberg header
    """
    start_marker = "START OF THE PROJECT"

    for line in fp:
        if start_marker.lower() in line.lower():
            return
    raise ValueError(f"Header end marker '{start_marker}' not found in file.")

def top_x(word_freq, x=10): 
    """
    Gets the top 10 words from a word frequency dictionary.
    """
    top_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:x]
    return top_words

def remove_stop_words(word_freq):
    """
    Removes stop words from a given word frequency dictionary.
    """
    with open('data/stopwords.txt', 'r') as f:
        stop_words = f.read().splitlines()  # Read stopwords from the file

    for word in list(word_freq.keys()):
        if word in stop_words:
            del word_freq[word]
    return word_freq

def nltk_analyze_sentiment(text):
    """
    Does a Sentiment analysis on the given text using NLTK.
    """
    score = SentimentIntensityAnalyzer().polarity_scores(text)
    return score

def compute_text_similarity(text1, text2):
    """
    Computes the similarity between two texts, Returns A score from 0 to 100 
    """
    return fuzz.ratio(text1, text2) 



def main():
    ## Characterizing by Word Frequencies
    # Finds word frequencies in Alice and Peter
    Alice_word_freq = word_freq("data/Alice.txt", skip_header=True) 
    Peter_word_freq = word_freq("data/Peter.txt", skip_header=True)

    # Print the top 10 words from each text
    top_alice_words = top_x(Alice_word_freq)
    top_peter_words = top_x(Peter_word_freq)
    print(f"Top 10 words in Alice: {top_alice_words}")
    print(f"Top 10 words in Peter: {top_peter_words}")


    ## Removing Stop words
    Alice_word_freq = remove_stop_words(Alice_word_freq)
    Peter_word_freq = remove_stop_words(Peter_word_freq)


    ## Computing Summary Statistics
    # Print the top 10 words from each text
    x = 20
    top_alice_words = top_x(Alice_word_freq,x)
    top_peter_words = top_x(Peter_word_freq,x)
    print(f"Top {x} words (without stopwords) in Alice: {top_alice_words}")
    print(f"Top {x} words (without stopwords) in Peter: {top_peter_words}")

    ## Natural Language Processing 
    with urllib.request.urlopen("https://www.gutenberg.org/cache/epub/11/pg11.txt") as f:
        Alice_word_text = f.read().decode('utf-8')

    with urllib.request.urlopen("https://www.gutenberg.org/cache/epub/16/pg16.txt") as f:
        Peter_word_text = f.read().decode('utf-8')
    
    nltk_alice = nltk_analyze_sentiment(Alice_word_text)
    nltk_peter = nltk_analyze_sentiment(Peter_word_text)

    print(f"NLTK Alice: {nltk_alice}")
    print(f"NLTK Peter: {nltk_peter}")

    ## Text Similarity
    similarity = compute_text_similarity(Alice_word_text, Peter_word_text)
    print(f"Text Similarity between Alice and Peter (Out of 100): {similarity}")


if __name__ == "__main__":
    main()