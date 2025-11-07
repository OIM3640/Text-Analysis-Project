#######################################################################################################
#starting code for text assignment
#importing library 
from mediawiki import MediaWiki

#making the pull of text a function so i can reuse later with less lines of code 
def get_text(topic):
    wikipedia = MediaWiki()
    page = wikipedia.page(topic)
    return page.content

if __name__ == "__main__":
    text = get_text("The Neighbourhood (band)") #one of my fav bands 
    print(text[:1000])
    #making sure package works by printing first 1000 characters of the text

#pickling the text for later use
import pickle

#https://wiki.python.org/moin/UsingPickle (used this to help)
with open("the_neighbourhood_band.pkl", "wb") as f:
    pickle.dump(text, f)
#######################################################################################################
#text cleaning and preprocessing
import re
import string

def clean_text(text):
    """cleans and preprocesses text for analysis"""
    # lowercase the text
    text = text.lower()

    # remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # remove numbers and other symbols using regex
    text = re.sub(r'\d+', '', text)

    # remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    # split into words (tokenization, learned from machine learning class for easier data manipulation of text)
    words = text.split()

    return words

# testing the function
words = clean_text(text)
print(words[:30])  # first 30 cleaned words
#######################################################################################################
#removing stop words 
#importing nltk package (used https://www.nltk.org/book/ch01.html as reference)

import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def remove_stopwords(words):
    """removes common stop words from a list of words"""
    stop_words = set(stopwords.words('english'))
    filtered = [w for w in words if w not in stop_words]
    return filtered

# testing the function
words = clean_text(text)
print("Before stopword removal:", len(words), "words")

filtered_words = remove_stopwords(words)
print("After stopword removal:", len(filtered_words), "words")
print(filtered_words[:30])
#######################################################################################################
#word frequency analysis
#using a dictionary function to do this
def word_frequency(words):
    """count word frequencies using a dictionary"""
    freq = {}  # empty dictionary

    for word in words:
        if word in freq:
            freq[word] += 1   # if word exists, increment count
        else:
            freq[word] = 1    # if new word, set count to 1

    return freq

freq = word_frequency(filtered_words)

#print all word freqs
for word, count in freq.items():
    print(f"{word}: {count}")

######################################################################################################
#summary statistics 

def summary_statistics(text, words, freq):
    """compute and print key summary statistics for the text"""
    
    # document length (in words)
    total_words = len(words)

    # unique words
    unique_words = len(set(words))

    # vocabulary richness (unique / total)
    vocab_richness = unique_words / total_words if total_words > 0 else 0

    # average word length
    avg_word_length = sum(len(word) for word in words) / total_words if total_words > 0 else 0

    # sentence stats (split text by punctuation)
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip() != ""]
    total_sentences = len(sentences)
    avg_sentence_length = total_words / total_sentences if total_sentences > 0 else 0

    # top 10 frequent words
    sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
    top_10 = list(sorted_freq.items())[:10]

    #printing all results 
    print("\nthe neighbourhood text stats:")
    print(f"Total words (after cleaning): {total_words}")
    print(f"Unique words: {unique_words}")
    print(f"Vocabulary richness: {vocab_richness:.3f}")
    print(f"Average word length: {avg_word_length:.2f}")
    print(f"Total sentences: {total_sentences}")
    print(f"Average sentence length (words): {avg_sentence_length:.2f}")
    print("\nTop 10 most frequent words:")
    for word, count in top_10:
        print(f"  {word}: {count}")

#calling function to print summary stats
summary_statistics(text, filtered_words, freq) 
######################################################################################################
#data visualization

import matplotlib.pyplot as plt
from wordcloud import WordCloud

def plot_top_words(freq, n=10):
    """
    visualize the top 10 most frequent words as a bar chart.

    learned from:
    https://matplotlib.org/stable/tutorials/introductory/pyplot.html
    and https://www.w3schools.com/python/matplotlib_intro.asp
    and used ai agent help to format code properly
    """
    # sort the frequency dictionary by value (descending order)
    sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
    top_items = list(sorted_freq.items())[:n]
    words, counts = zip(*top_items)

    # create bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(words, counts, color='skyblue')
    plt.title(f"Top {n} Most Frequent Words")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def make_wordcloud(freq):
    """
    Generate and display a word cloud from word frequencies.

    Technique inspired by:
    https://amueller.github.io/word_cloud/
    and https://www.geeksforgeeks.org/generating-word-cloud-python/
    """
    wc = WordCloud(
        width=800,
        height=400,
        background_color='white',
        max_words=200
    ).generate_from_frequencies(freq)

    plt.figure(figsize=(10, 6))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.title("Word Cloud of Most Frequent Words", fontsize=16)
    plt.show()

#calling functions to show chart outputs
plot_top_words(freq, n=10)
make_wordcloud(freq)
#######################################################################################################
#advanced technique - vader from nltk and markov

#used these sources to help with vader sentiment analysis
#https://www.nltk.org/_modules/nltk/sentiment/vader.html
#https://www.geeksforgeeks.org/python-sentiment-analysis-using-vader/

#technique 1 : sentiment analysis with vader
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    """analyze sentiment of the text using NLTK's VADER."""
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(text)

    print("\nsentiment analysis results:")
    for k, v in scores.items():
        print(f"{k}: {v}")
    
    # basic interpretation
    if scores["compound"] >= 0.05:
        print("\nOverall Sentiment: 😊 Positive")
    elif scores["compound"] <= -0.05:
        print("\nOverall Sentiment: 😠 Negative")
    else:
        print("\nOverall Sentiment: 😐 Neutral")

#calling the function to analyze sentiment
analyze_sentiment(text)

#technique 2 : markov text generation

# sources used
# "Think Python" by Allen B. Downey (Markov example)
# Real Python Markov Tutorial: https://realpython.com/markov-chains/
# used chatgpt to explain and help with this one


import random

def build_markov_chain(words, n=2):
    """
    build a Markov chain as a dictionary mapping tuples of 'n' words to possible next words
    """
    markov_chain = {}
    for i in range(len(words) - n):
        key = tuple(words[i:i + n])
        next_word = words[i + n]
        if key not in markov_chain:
            markov_chain[key] = []
        markov_chain[key].append(next_word)
    return markov_chain


def generate_markov_text(chain, num_words=100):
    """
    generate new text using the Markov chain. 
    randomly starts from one of the keys and keeps selecting next words based on the learned transitions.
    """

    start_key = random.choice(list(chain.keys()))
    result = list(start_key)

    for _ in range(num_words - len(start_key)):
        next_words = chain.get(tuple(result[-len(start_key):]), None)
        if not next_words:
            break
        next_word = random.choice(next_words)
        result.append(next_word)

    return ' '.join(result)

#printing output 
print("\n generating markov text \n")
chain = build_markov_chain(filtered_words, n=2)
generated_text = generate_markov_text(chain, num_words=100)
print(generated_text)
#######################################################################################################
#main function to run all parts of the project
def main():
    # get Wikipedia text
    text = get_text("The Neighbourhood (band)")  # one of my fav bands
    print(text[:1000])  # sanity check

    # pickle text for later use
    with open("the_neighbourhood_band.pkl", "wb") as f:
        pickle.dump(text, f)

    # clean and preprocess
    words = clean_text(text)
    print(words[:30])

    # remove stopwords
    print("Before stopword removal:", len(words))
    filtered_words = remove_stopwords(words)
    print("After stopword removal:", len(filtered_words))
    print(filtered_words[:30])

    # word frequency + summary stats
    freq = word_frequency(filtered_words)
    summary_statistics(text, filtered_words, freq)

    # visualizations
    plot_top_words(freq, n=10)
    make_wordcloud(freq)

    # sentiment analysis
    analyze_sentiment(text)

    # markov text synthesis
    print("\n--- Generating Markov Text ---\n")
    chain = build_markov_chain(filtered_words, n=2)
    generated_text = generate_markov_text(chain, num_words=100)
    print(generated_text)

# run the project
if __name__ == "__main__":
    main()
