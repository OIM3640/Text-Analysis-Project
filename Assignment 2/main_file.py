import urllib.request
import random
import string
import sys
from unicodedata import category


#url = 'https://gutenberg.org/cache/epub/11/pg11.txt'
# with urllib.request.urlopen(url) as f:
#     text = f.read().decode('utf-8')
#     print(text) 

def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.
    """
    hist = {}
    fp = open(filename, encoding='UTF8')

    if skip_header:
        skip_gutenberg_header(fp)

    strippables = string.punctuation + string.whitespace

    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break

        line = line.replace('-', ' ')
        line = line.replace(
            chr(8212), ' '
        )  
        line = line.replace("'", " ").replace('"', ' ')

        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1
    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break


def word_frequencies(hist):
    """This function finds the frequency of each word in the text."""
    word_frequencies = {}
    for word in hist:
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1
    print(word_frequencies)



def remove_stopwords(hist, stopwords):
    """This function removes stop words, such as those listed below, from the text to gather a better analysis."""
    stop_words = ["a", "an", "the", "in", "on", "at", "to", "and", "is", "it", "with", "as"]
    # Create a copy of the histogram without stop words
    hist_without_stopwords = {word: freq for word, freq in hist.items() if word not in stopwords}
    print(hist_without_stopwords)


def top_10_words(hist):
    """This function provides output for the top 10 most used words in the text."""
    sorted_hist = sorted(hist.items(), key=lambda x: x[1], reverse=True) # Sorts the histogram by word frequency in descending order
    top_10 = sorted_hist[:10] # Get the top 10 words or less if there are fewer than 10 unique words
    return top_10

def remove_quotation_marks(hist):
    """This function removes quotation marks from the text. *I asked ChatGPT how to do this and it still didn't work."""
    cleaned_text = hist.replace("'", "").replace('"', '') # Remove both single and double quotation marks
    return cleaned_text


import nltk 
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer #Asked ChatGPT how to run this function

def analyze_sentiment(hist):
    """This function run the sentiment analysis on the texts."""
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(hist)
    return score
# result = analyze_sentiment(hist)
# print(result)

from thefuzz import fuzz 

print(fuzz.ratio('https://gutenberg.org/cache/epub/11/pg11.txt', 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt')) # 86
print(fuzz.partial_ratio('https://gutenberg.org/cache/epub/11/pg11.txt', 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt')) # 82
print(fuzz.ratio('https://gutenberg.org/cache/epub/11/pg11.txt', 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt')) # 86
print(fuzz.token_sort_ratio('https://gutenberg.org/cache/epub/11/pg11.txt', 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt')) # 85



import string
import sys
import urllib.request

stop_words = ["a", "an", "the", "in", "on", "at", "to", "and", "is", "it", "with", "as"] # Defines a list of stop words

def main():
    #url = 'https://gutenberg.org/cache/epub/11/pg11.txt'
    url = 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt'
    text = fetch_text_from_url(url)

    text = remove_quotation_marks(text)
    
    hist = process_text(text, skip_header=True) # Process the text and create a histogram without stop words
    

    hist_without_stopwords = remove_stopwords(hist, stop_words) # Remove stop words from the histogram
    
    word_frequencies(hist_without_stopwords) # Calculate and print word frequencies
    
    top_words = top_10_words(hist_without_stopwords) # Calculate and print the top 10 words
    print("\nTop 10 words:")
    for word, frequency in top_words:
        print(f"{word}: {frequency}")


def fetch_text_from_url(url):
    with urllib.request.urlopen(url) as f:
        text = f.read().decode('utf-8')
    return text

def process_text(text, skip_header):
    hist = {}
    lines = text.split('\n')

    if skip_header:
        lines = skip_gutenberg_header(lines)

    strippables = string.punctuation + string.whitespace

    for line in lines:
        for char in strippables:
            line = line.replace(char, ' ')

        for word in line.split():
            word = word.strip()
            word = word.lower()

            # Update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist

def skip_gutenberg_header(lines):
    for i, line in enumerate(lines): # Identify the line that ends the header
        if line.startswith('*** START OF THIS PROJECT'):
            return lines[i+1:]  # Skip the lines after the header ends
    return lines

def remove_stopwords(hist, stopwords):
    hist_without_stopwords = {word: freq for word, freq in hist.items() if word not in stopwords}  # Create a copy of the histogram without stop words
    return hist_without_stopwords

def top_10_words(hist):
    sorted_hist = sorted(hist.items(), key=lambda x: x[1], reverse=True) # Sort the histogram by word frequency in descending order
    top_10 = sorted_hist[:10] # Get the top 10 words or less if there are fewer than 10 unique words
    return top_10


def remove_quotation_marks(hist):
    cleaned_text = hist.replace("'", "").replace('"', '') # Remove both single and double quotation marks
    return cleaned_text

def analyze_sentiment(hist):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(hist)
    return score
    # result = analyze_sentiment(hist)
    # print(result)


if __name__ == '__main__':
    main()
