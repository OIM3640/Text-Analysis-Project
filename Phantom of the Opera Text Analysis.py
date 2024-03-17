import urllib.request
import string
import sys
from unicodedata import category
import pprint
import pandas as pd
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

"""
This following Project will analyze the text "Phantom of the Opera" by Gaston Leroux. It will do a sentiment Analysis of the Three Main Characters: Christine, The Phantom, and Raoul. 
"""
#Text Exploration
###Text Analysis Begins

def skipgutenbergheader(filename):
    """
    This function skips the Project Gutenberg Header.
    """
    for line in filename:
        if line.startswith("*** START OF THE PROJECT GUTENBERG EBOOK THE PHANTOM OF THE OPERA ***"):
            break

def count_words(filename):
    """ This function counts the amount of words that are in the text.
    filename = str() <-- Enter a text file with the name and extension.
    """
    text = open(filename,encoding='utf-8')

    skipgutenbergheader(text)

    word_count = 0
    for line in text:
        if line.startswith("End of Project Gutenberg's The Phantom of the Opera, by Gaston Leroux"):
            break
        length =len(line.split())
        word_count += length
        #   endgutenberg
    return word_count

#The following function will now create a dictionary that contains all the words from the book. 
#The code for this section comes from Professor Zhi Li's analyze book.py: https://github.com/OIM3640/resources/blob/main/code/analyze_book.py
###Beginning of Zhi Li Code:
def process_file(filename):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    hist = {}
    text = open(filename, encoding='UTF8')

    skipgutenbergheader(text)

    # strippables = string.punctuation + string.whitespace
    # via: https://stackoverflow.com/questions/60983836/complete-set-of-punctuation-marks-for-python-not-just-ascii

    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )

    for line in text:
        if line.startswith("End of Project"):
            break

        line = line.replace('-', ' ')
        line = line.replace(
            chr(8212), ' '
        )  # Unicode 8212 is the HTML decimal entity for em dash

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist
###End of Zhi Li edited code sample. 

#Testing If Histogram Worked:
#Take the histogram, search for a key named "ebook" or "guttenberg" as a quick test of histogram effectiveness.
def histogram_test(hist):
    """
    Takes a dicitonary as an argument.
    Looks through dictionary for the keyword ebook, which should not be in the dictionary. 
    Returns a True, if keyword found in dictionary, or False if not. 
    """
    if "ebook" in hist.keys(): #we choose getunberg because we know that ebooks did not exist in the 19th century. 
        return True #means that the keyword was found in our histogram dictionary; therefore our histogram dictionary is not working.
    else:
        return False #means that the keyword was not found in our histogram dictionary; the dictionary is functioning as intended. 
    
#Number of Unique Words in Histogram:
def unique_words(dictionary):
    """
    Counts the number of keys in a dictionary. 
    returns count of words. 
    """
    unique_word_count = len(dictionary)
    return unique_word_count

#Removal of Stop Words. Source:
def stop_words():
    """
    This function returns a list of stop_words based off the file terrier.txt.
    This function takes no arguments. 
    """
    stop = open('stop_words.txt', encoding= 'utf-8')
    stoplist = list()
    for line in stop:
        word = line.strip()
        stoplist.append(word)
    return stoplist
            
#Most Common Words found after removing stop words:
def most_common(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    frequency_first_list = [] #empty dictionary to store reverse mapped hist dictionary.
    stop_list = stop_words()
    for key in hist.keys():
        if key not in stop_list:
            frequency_first_list.append((hist[key],key))
    frequency_first_list.remove((866,''))#because space is not an important "word"
    frequency_first_list.sort(key = lambda v: v[0],reverse= True) #code based off example from this website: https://learnpython.com/blog/sort-tuples-in-python/
    return frequency_first_list[0:10]
            
#Sentiment Analysis
"""
Here, I want to find the sentiment (positive or negative) towards our three main characters: The Phantom (aka Erik or ghost), Christine Dae, and Raoul de Chagny. How does the novel depict these characters? What is the general sentiment from it? And if we cna find this general sentiment, can we compare it to other sources? How do other media sources see the phantom? 
"""
#For every sentence containing the "Ghost", "Phantom", and "Erik" I want to get a sentiment reading. 
#For this purpose I might want to split the whole book into sentences, then add the ones that contain my words to a list or string for later use.
def extract_sentences(filename):
    file = open(filename, encoding='utf-8')
    skipgutenbergheader(file)  
    text = file.read()

    #Contains list of all stop words
    stop_list = stop_words()

    # Remove ellipses and split the text into words
    words = text.replace('...', ' ').split()
    
    sentences = []
    current_sentence = []

    for word in words:
        word = word.lower()

        if word in stop_list:
            continue #also got this code from the internet, did not know continue was a thing!
        current_sentence.append(word)
        if word.endswith(('.', '!', '?')):
            sentences.append(' '.join(current_sentence))
            current_sentence = []
        #come back to this and remove stop words and gutenberg ender.
    return sentences
##Sentiment Analysis Begins: code borrowed from https://www.datacamp.com/tutorial/text-analytics-beginners-nltk and edited for Project Purposes.
# initialize NLTK sentiment analyzer

analyzer = SentimentIntensityAnalyzer()
# create get_sentiment function

def get_sentiment_phantom(filename):

    sentences = extract_sentences(filename)
    #phantom_occurence
    phantom_occurences = list()
    for phrase in sentences:
        if 'phantom'in phrase or 'erik' in phrase or 'ghost' in phrase:
            phantom_occurences.append(phrase)
    #count the number of sentences = > to divide score 
    total_score = 0 #contains the number of positive occurences of the character in the function
    total_no_occurences = len(phantom_occurences)
    for phrase in phantom_occurences:

        scores = analyzer.polarity_scores(phrase)

        sentiment = 1 if scores['pos'] > 0 else 0
        total_score += sentiment
    return (total_score / total_no_occurences)*100 #This returns a percentage of overall sentiment. T

def get_sentiment_christine(filename):

    sentences = extract_sentences(filename)
    #phantom_occurence
    christine_occurences = list()
    for phrase in sentences:
        if 'christine'in phrase or 'daae' in phrase:
            christine_occurences.append(phrase)
    #count the number of sentences = > to divide score 
    total_score = 0
    total_no_occurences = len(christine_occurences)
    for phrase in christine_occurences:

        scores = analyzer.polarity_scores(phrase)

        sentiment = 1 if scores['pos'] > 0 else 0
        total_score += sentiment
    return (total_score / total_no_occurences)*100

def get_sentiment_raoul(filename):

    sentences = extract_sentences(filename)
    #phantom_occurence
    raoul_occurences = list()
    for phrase in sentences:
        if 'raoul'in phrase or 'de chagny' in phrase or 'chagny' in phrase:
            raoul_occurences.append(phrase)
    #count the number of sentences = > to divide score 
    total_score = 0
    total_no_occurences = len(raoul_occurences)
    for phrase in raoul_occurences:

        scores = analyzer.polarity_scores(phrase)

        sentiment = 1 if scores['pos'] > 0 else 0
        total_score += sentiment
    return (total_score / total_no_occurences)*100  


def main():
    filename = 'Phantom of the Opera.txt'
    print(f"This is the total count of words within this file: {count_words(filename)}")
    hist = process_file(filename)
    #print(process_file(filename))
    #print(histogram_test(hist))
    print(f"The top ten words in this book are (in (freq,word) order are:\n{most_common(hist)}")
    #print(extract_sentences(filename))
    print(f"\nThe Phantom of the Opera, or Erik,  got a total sentiment score of: {get_sentiment_phantom(filename)}, which is mostly neutral, but leans negtive.") #neutral
    print(f"\nChristine Daae has a sentiment score of:{get_sentiment_christine(filename)}, which is mostly neutral and leans positive. ") #neutral
    print(f"\nRoul has a sentiment score of: {get_sentiment_raoul(filename)} which is mostly neutral, but leans negative") #neutral


if __name__ == '__main__':
    main()