import urllib.request
import string
import random

from nltk.tokenize import sent_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def process_text(text):
    """
    Processes the text and returns a histogram of the words used in the book. 
    """
    hist = {}
    for line in text.split('\n'):
        line = line.strip().lower()
        for word in line.split():
            # remove punctuations from the word
            word = word.translate(str.maketrans('', '', string.punctuation))
            hist[word] = hist.get(word, 0) + 1
    return hist

def total_words(hist):
    """
    Returns the total number of words in the histogram: word count of the book
    """
    return sum(hist.values())

def different_words(hist):
    """
    Returns the number of different words in the books: word variety.
    """
    return len(hist)

def load_stopwords():
    """Loads a list of stopwords."""
    with open('stopwords.txt') as f:
        stopwords = f.read().split()
    return stopwords

def most_common(hist, excluding_stopwords=False):
    """
    Returns a list of the most common words in the book.
    """
    t = []
    stopwords = load_stopwords()
    for word, freq in hist.items():
        if excluding_stopwords and word in stopwords:
            continue
        t.append((freq, word))
    t.sort(reverse=True)
    return t

def subtract(hist1, hist2):
    """Subtracts two histograms and returns the result."""
    diff = {}
    for word in hist1:
        if word not in hist2:
            diff[word] = hist1[word]
    return diff

def number_not_in_the_list(hist):
    """
    Returns the total number of words in the book that aren't in the stopword list.
    """
    stopwords = load_stopwords()
    words = {word for word in stopwords if word in hist}
    diff = subtract(hist, words)
    return sum(diff.values())

def main():
    
    url = 'http://www.gutenberg.org/ebooks/174.txt.utf-8'
    with urllib.request.urlopen(url) as f:
        text = f.read().decode('utf-8')
    
    # Process the book text
    hist = process_text(text)
    
    # Print out the total and different number of words in the book
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))
    
    # Print out the most common words in the book
    print('The most common words are:')
    for freq, word in most_common(hist, excluding_stopwords=True)[0:20]:
        print(word, '\t', freq)
    
    # Load the stopwords
    stopwords = load_stopwords()
    
    # Subtract the book words from the stopwords
    words = {word for word in stopwords if word in hist}
    diff = subtract(hist, words)
    
    # Print out the words in the book that aren't in the stopword list
    print("The words in the book that aren't in the word list are:")
    for word in diff.keys():
        print(word, end=' ')
    
    print("\nTotal number of words not in the word list:", number_not_in_the_list(hist))
        
if __name__ == '__main__':
    main()



### Another Way I appraoch word Frequency in the beginning (both with and without stopwords considered) 
### which I do not prefer
url = 'http://www.gutenberg.org/ebooks/174.txt.utf-8'
with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')

words = text.split()

word_freq = {}
for word in words:
    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] += 1

# Computing Summary Statistics
sorted_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
# word_freq.items is tuple, and lambda returns the second value of the tuple which is the frequency
for word, count in sorted_freq[:10]:  # return the first 10 tuples
    print(f'{word}: {count}')

words = text.split()
stop_words = {'the', 'and', 'a', 'an', 'or', 'but', 'not',
              'at', 'in', 'on', 'to', 'of'}  # self-defined stop words
words_without_stop_words = [
    word for word in words if word.lower() not in stop_words]

filtered_words = [word for word in words if word.lower() not in stop_words]

word_freq = {}
for word in words_without_stop_words:
    if word not in word_freq:
        word_freq[word] = 0
    word_freq[word] += 1

sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_word_freq[:10]:
    print(f'{word}: {count}')
