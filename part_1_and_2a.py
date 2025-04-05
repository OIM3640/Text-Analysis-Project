#Part 1: Harvesting A Text From The Internet:

#Datasource selected: Project Gutenberg.
#eBook selected: The Great Gatsby By: F. Scott Fitzgerald

#Downloading the text into Python:

import urllib.request
url = 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt'
#URL of The Great Gatsby eBook from Gutenberg. 
try:
    with urllib.request.urlopen(url) as f:
        text = f.read().decode('utf-8')
        print(text)  # for testing
except Exception as e:
    print("An error occurred:", e)

#First we need to process the text and clean the text effectively. 
#The below code is taken from the analyze_book example, where we experimented
#with Pride and Prejudice by Jane Austen. 

import random
import string
import sys
from unicodedata import category

def process_file(filename, skip_header):
    """Makes a histogram that counts the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding="utf-8")

    if skip_header:
        skip_gutenberg_header(fp)

    # strippables = string.punctuation + string.whitespace
    strippables = "".join(
        chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")
    )  # Unicode punctuation characters. Ref: https://stackoverflow.com/a/60983895

#Now start reading the text line by line:
    for line in fp:
        if line.startswith("*** END OF THE PROJECT"):
            break
#Stop processing the text once the end of the text is reached,
#in this case, being the Project Gutenberg end marker ("*** END OF THE PROJECT")
        line = line.replace("-", " ")
        line = line.replace(chr(8212), " ")  # Em dash replacement

        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()

            hist[word] = hist.get(word, 0) + 1 #Tokenization

    fp.close()
    return hist

#Now after the text is cleaned and processed, to ensure efficient reading of the book,
#we want to skip the header and get to the starting point of the book:
def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
 #Indicates where the content of the book begins:    
    start_marker = "START OF THE PROJECT"

#Goes through the lines in the text until the start_marker
#or the starting position of the book is found. 
    for line in fp:
        if start_marker.lower() in line.lower():  # Case-insensitive search
            return
#Once the start_marker is found, then the book is ready to be read
#by the reader. 

    # If the loop completes without finding the start marker
    raise ValueError(f"Header end marker '{start_marker}' not found in file.")

#Part 2: Analyzing The Text

#Part 2a) Required Step 1: Characterizing By Word Frequencies:
import string

def count_word_frequency(text):
    """
    Count word frequencies in a given text. 
    Return a dictionary where keys are words and values are their frequencies. 
    """
    d = {} #initalize the dictionary to store word frequencies. 

    #Split the text into individual words: 
    words = text.split()
    
    #Clean each word, remove trailing characters (string.punctuation) 
    #and convert each word to lowercase (.lower). Used GenAI for debugging in the line below (line 102). 
    cleaned_words = [word.strip(string.punctuation).lower() for word in words]

    #After cleaning each word, count the frequency of each word: 
    for word in cleaned_words: 
        if word not in d: 
            d[word] = 1 
    #if the word is not in the dictionary, add it to the dictionary
    #with a designated count of 1.
        else: 
            d[word] += 1
    #If the word is in the dictionary, increment the word's count by 1. 
    #For the above for loop, can also do: d[word] = d.get(word, 0) + 1

    return d #Return the dictionary containing word frequencies. 

#Testing the above function for analysis: 
if __name__ == "__main__":

#Here is a chosen sentence from the book: 
    text = ("In my younger and more vulnerable years my father gave me some advice " 
"that I've been turning over in my mind ever since") 

    result = count_word_frequency(text)  
    #Calling the count_word_frequency function to analyze the chosen sentence (text). 

    total_words = sum(result.values())
    #Use sum to add all frequency values in regards to words
    #in the dictionary, including words that were repeated.
    unique_words = len(result)
    #Use len to calculate the number of unique words in the text. 

#Print results:
    print(f"Total words: {total_words}")
    print(f"Unique words: {unique_words}")
    #Show total and unique word counts!

    print("\nWord Frequencies:") 
#prints a new header in the terminal: Word Frequencies, for better organization. 

    for word, freq in sorted(result.items(), key=lambda x:
x[1], reverse=True):
#Used GenAI for assistance in the above line (line 141), was having an issue in the code. 
#The functionality is explained below: 

#result.items() creates a list of these key-value pairs [("word1, freq1"), ("word2, freq2")] 
#and stores them as tuples.

#sorted() function sorts these lists by their frequency: 
#The key=lambda x: --> x signals to sorted() to sort by
#the second element of each key-value pair (the frequency),
#in descending order (reverse=True)

#The for loop goes over each sorted key-value pair (word, freq).

        print(f"{word}: {freq}")
        #As a result, each word is printed with its frequency. 

