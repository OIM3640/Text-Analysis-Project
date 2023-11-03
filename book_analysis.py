import urllib.request
import sys
from unicodedata import category
import nltk
from nltk.stem import PorterStemmer



url = 'https://www.gutenberg.org/files/514/514-0.txt'
with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')[780:]
strippables = [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]

def processtext(text):
    """
    This function returns a list of words from the text without punctuations
    """
    text = " ".join(text.split())
    wordlist = text.split(" ")
    wordlist = [word for word in wordlist if word not in strippables]
    return wordlist


def wordfreq(wordlist):
    '''
    This function returns a dictionary that maps the word to the frequency of the word.
    '''
    hist = {}
    for word in wordlist:
        word = word.replace('-', '')
        word = word.replace(chr(8212), '')

        word = "".join(letter for letter in word if letter not in strippables)
        if word == "END":
            break
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1
    return hist

def total_words(hist):
    '''
    This function returns the total number of words in the file
    '''
    return sum(hist.values())

def num_of_unique_words(hist):
    '''
    This function returns the number of unique words in the text.
    
    The result is essentiatlly the number of keys in the result dictionary from the processfile function.
    '''
    return len(hist)

def stopwords():
    '''
    This function will return the stopwords txt file as a list.
    '''
    stopwords_list = []
    f = open('data/stopwords.txt')# This txt file of stopwords are provided by Github user larsyencken.
    for line in f:
        word = line.strip()
        stopwords_list.append(word)
    return stopwords_list

def common_words(hist, stopwords=stopwords(), num=10):
    '''
    This function creates a list that shows the top common words from the text depending on the parameter num without the stop words
    '''
    wordfreq = []

    for word in hist:
        if word in stopwords:
            continue
        freq = hist[word]
        wordfreq.append((freq, word))
    wordfreq.sort(reverse=True)
    most_common = [wordfreq[i] for i in range(num)]
    return most_common

def pos_tags(wordlist, num):
    '''
    This function returns the most common part of speech used in the text
    '''
    pos_freq = {}
    pos_common = []
    pos_tags = nltk.pos_tag(wordlist)
    for element in pos_tags:
        pos_freq[element[1]] = pos_freq.get(element[1], 0) + 1
    for k in pos_freq:
        freq = pos_freq[k]
        pos_common.append((freq, k))
    pos_common.sort(reverse = True)
    most_common = [pos_common[i] for i in range(num)]
    return most_common

def stemming(hist, num):
    '''
    This function returns the top common stemmed words from the a list of unique words.
    It will combine words with similar roots and return its frequency.
    '''
    stemmed_words = {}
    ps = PorterStemmer()
    for k in hist:
        k = ps.stem(k)
        stemmed_words[k] = stemmed_words.get(k, 0) + 1
    stemmed_list = [(stemmed_words[k], k) for k in stemmed_words]
    stemmed_list.sort(reverse = True)
    common_stemmed = [stemmed_list[i] for i in range(num)]
    return common_stemmed

def stemm(wordlist, num):
    '''
    This function returns the most common stem words from the orginal text's wordlist.
    '''
    lis = []
    ps = PorterStemmer()
    for word in wordlist:
        word = ps.stem(word)
        lis.append(word)
    hist = wordfreq(lis)
    most_common = common_words(hist)
    return most_common


def main():
    wordlist = processtext(text)
    hist = wordfreq(wordlist)
    print(hist)

    print(f"The total number of words is {total_words(hist)}")

    num = 10
    stopwords_list = stopwords()
    common_words_list = common_words(hist, stopwords_list, num)
    print(f'The top {num} most common words are {common_words_list}.')

    common_pos_list = pos_tags(wordlist, num)
    print(f'The top {num} most common part of speech tags are {common_pos_list}.')

    print(stemming(hist, num))

    print(stemm(wordlist, num))

if __name__ == "__main__":
    main()