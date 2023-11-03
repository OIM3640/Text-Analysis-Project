import random
import urllib.request
import string
import sys
from thefuzz import fuzz
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from unicodedata import category
import nltk
import numpy as np

nltk.download('vader_lexicon')
nltk.download('stopwords')


# Part 1: Harvesting and Reading the Data

def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    name = {}
    fp = open(filename, encoding='UTF8')

    if skip_header:
        skip_gutenberg_header(fp)

    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break

        line = line.replace('-', ' ')
        line = line.replace(chr(8212), ' ')

        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()
            name[word] = name.get(word, 0) + 1

    return name

def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line
    that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break

# Part 2: Analyze the Text

def total_words(name):
    """
    This function returns the 
    total of the frequencies in a histogram.
    """
    return sum(name.values())

def eliminate_stop(name, stopwords_file_path):
    """
    This function eliminates the 
    stop words in the text files
    """
    with open(stopwords_file_path, 'r', encoding='UTF8') as stopwords_file:
        stopwords = set(word.strip() for word in stopwords_file)

    words = name.keys()
    filtered_words = [word for word in words if word.lower() not in stopwords]
    
    # This is to reconstruct the text without stopwords
    text_without_stopwords = ' '.join(filtered_words)
    return text_without_stopwords

def specific_words(name, word):
    """
    This function finds how many 
    times the word appears in the text file
    """
    try:
        with open(name, 'r', encoding='UTF8') as file:
            text = file.read()
            words = text.split()
            count = words.count(word.lower())
            return count
    except FileNotFoundError:
        return 0
    
word_to_count = 'the'
count_1 = specific_words('data/Peter Pan.txt', word_to_count)
count_2 = specific_words('data/Winnie the Pooh.txt', word_to_count)

print(f'The word "{word_to_count}" appears {count_1} times in the text.')
print(f'The word "{word_to_count}" appears {count_2} times in the text.')

def most_common(name, excluding_stopwords=False):
    """
    Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    stopwords = set(nltk.corpus.stopwords.words('english'))
    name = process_file(name, skip_header=True)  # Process the provided text
    res = []
    for word in name:
        if excluding_stopwords and word in stopwords:
            continue
        freq = name[word]
        res.append((freq, word))

    res.sort(reverse=True)
    return res


def top_10(name):
    """
    This function finds the top 
    10 words in each text
    """
    t = most_common(name,excluding_stopwords=True)
    result = {}
    for freq, word in t[:10]:
        result[word] = freq
    return result

def unique_words(name):
    '''
    This function returns the number of unique words in the text.
    The result is the number of keys in the result dictfrom the processfile function.
    '''
    return len(name)

# Part 3: Natural Language Processing

def sentiment_analysis(filename):
    """
    This function returns the polarity score for the book.
    """
    analyzer = SentimentIntensityAnalyzer()
    with open(filename, 'r', encoding='UTF8') as file:
        text = file.read()
    score = analyzer.polarity_scores(text)
    return score

# Part 4: Text Similarity

def similarity(filename, filename_1):
    """
    This function calculates the similarity 
    between Peter Pan and Winnie the Pooh
    """
    return fuzz.ratio(filename, filename_1)

def main():
    name = {}
    # Load text data
    text1 = 'data/Peter Pan.txt'
    text2 = 'data/Winnie the Pooh.txt'

    # Process the text files to create histograms
    Peter = process_file('data/Peter Pan.txt', skip_header=True)
    Winnie = process_file('data/Winnie the Pooh.txt', skip_header=True)

    # Total Words
    print(f'The total number of words in Peter Pan is: {total_words(Peter)}')
    print(f'The total number of words in Winnie the Pooh is: {total_words(Winnie)}')

    #Eliminate stop words
    stopwords_file_path = 'data/stopwords.txt'
    text_without_stopwords = eliminate_stop(process_file(text1, skip_header=True), stopwords_file_path)
    text_without_stopwords_1 = eliminate_stop(process_file(text2, skip_header=True), stopwords_file_path)

    # Most Common
    print(f'The most common words in Peter Pan are:{most_common(text1)}')
    print(f'The most common words in Winnie the Pooh are:{most_common(text2)}')

    # Top 50
    print(f'The top 10 words in Peter Pan are: {top_10(text1)}')
    print(f'The top 10 words in Winnie the Pooh are: {top_10(text2)}')

    # Unique Words
    print(f'The number of unique words in Peter Pan are: {unique_words(text1)} ')
    print(f'The number of unique words in Winnie the Pooh are: {unique_words(text2)} ')

    # Sentiment Analysis
    score_1 = sentiment_analysis(text1)
    score_2 = sentiment_analysis(text2)

    print(f'The sentiment score for Peter Pan is {score_1}')
    print(f'The sentiment score for Winnie the Pooh is {score_2}')

    # Calculate text similarity
    similarity_score = similarity(text1, text2)
    print(f'Text similarity score between Peter Pan and Winnie the Pooh: {similarity_score}')

if __name__ == '__main__':
    main()