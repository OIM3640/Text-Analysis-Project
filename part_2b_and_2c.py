#Part 2: Analyzing The Text

#Part 2b) Required Step 2: Computing Summary Statistics:
#Specifically I will be analyzing The Great Gatsby to find the
#top 10 words that appear the most frequently, and will aim to
#exclude some stopwords as there are 20,000+ stop words in the text!

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

#Starting Code To Get The Top 10 Words That Appear Most Frequently
#In The Great Gatsby:

def get_top_words(text, n=10):
    """
    Get the top 10 most frequent words from The Great Gatsby.

    n: number of words to return.
    returning numbers should be in a list of tuples (word, frequency) sorted
    by frequency in descending order - same as what I did in part_1and_2a.py
    """

    #To ensure more accurate analysis, stop words should be removed:

    #List of some common stop words:
    stopwords = {"the", "and", "to", "a", "of", "in", "it", "is",
                 "i", "that", "on", "was", "he", "she", "you", "for",
                 "with", "as", "at", "by", "an", "be", "this", "which",
                 "or", "from", "but", "not", "are", "we", "his", "her", 
                 "they", "them", "my", "me", "their", "our", "but", "have",
                 "what", "were", "when", "your", "all", "can"}
    
    #Now onto writing the code to get the Top 10 most frequent words from the text.
    #Utilizing code from the Part 2a) required technique and modifying it:

    #Create a dictionary to store word frequencies:
    word_frequencies = {}

    #Split the text into individual words:
    words = text.split()

    #Clean each word, remove trailing characters (string.punctuation) 
    #and convert to lowercase (.lower):
    cleaned_words = [word.strip(string.punctuation).lower() for word in words]

    #After cleaning each word, count the frequency of each word: 
    for word in cleaned_words: 
        if word not in word_frequencies: 
            word_frequencies[word] = 1 
        #if the word is not in the dictionary, add it to the dictionary
        #with a designated count of 1.
        else: 
            word_frequencies[word] += 1
    #If the word is in the dictionary, increment the word's count by 1. 
    #For the above for loop, can also do: d[word] = d.get(word, 0) + 1

    #Sort the dictionary by frequency in descending order, similar to 2a):
    sorted_words = sorted(word_frequencies.items(), key=lambda x:
x[1], reverse=True)
    
    #Return the all the most frequent words:
    return sorted_words[:n] #Slice to get all sorted N number of words that are most frequent.
    
#Testing the above function for analysis: 
if __name__ == "__main__":

    f = open("data\The Great Gatsby.txt")
    #Open the stored, The Great Gatsby text file.

    #Call the function to get the top 10 most frequent words:
    top_words = get_top_words(text, n=10)

    #Print the resulting words:
    print("Top 10 Most Frequent Words In The Great Gatsby")
    for word, freq in top_words:
        print(f"{word}: {freq}")

#Part 2c) Additional Step - Text Similarity:

#To perform this analysis, I selected and downloaded 
#a second eBook: The Adventures of Tom Sawyer, Complete By: Mark Twain.

#In order to test for Text Similarity, I am going to choose the Cosine Similarity method.
#Utilizing similar aspects of the code in 2a and 2b. 

import math
import string

def process_book(text):
    """
    Process the books to clean them and return a dictionary of
    word frequencies.
    Return a dictionary where keys are words and values are their frequencies. 
    """

#Create a dictionary to store word frequencies:
    word_frequencies = {}

    #Split the text into individual words:
    words = text.split()

    #Clean each word, remove trailing characters (string.punctuation) 
    #and convert to lowercase (.lower):
    cleaned_words = [word.strip(string.punctuation).lower() for word in words]

    #After cleaning each word, count the frequency of each word: 
    for word in cleaned_words: 
        if word != "": #Ignore empty strings. 
            if word not in word_frequencies: 
                word_frequencies[word] = 1 
        #if the word is not in the dictionary, add it to the dictionary
        #with a designated count of 1.
    else: 
            word_frequencies[word] += 1
    #If the word is in the dictionary, increment the word's count by 1. 
    #For the above for loop, can also do: d[word] = d.get(word, 0) + 1

    return word_frequencies

#To find the cosine similarity I used GenAI tools for assistance, 
#I will write the corresponding pseudo codse & comments 
#to explain the methodologies and process below:
def cosine_similarity(freq1, freq2):
    """
    Compute the cosine similarity between two dictionaries 
    of word frequencies. 

    freq1: dictionary of word frequencies for text 1.
    freq2: dictionary of word frequencies for text 2.

    Returns the cosine similarity score (float).
    """
    
    #Get the set of all unique words in both texts. 
    #Combine the keys from both frequency dictionaries to create
    #one set of vocabulary from both books. 
    unique_words = set(freq1.keys()).union(set(freq2.keys()))

    #Create vectors for both books.
    #Generate parallel vectors where each position corresponds to
    #the same word. 
    #In both texts, we use 0 if a specific word doesn't exist in 
    #a particular text. 
    vector1 = [freq1.get(word, 0) for word in unique_words]
    vector2 = [freq2.get(word, 0) for word in unique_words]

    #Calculate the dot product of the two vectors.
    #Using the sum function for element multiplication - for
    #measuring alignment between the vectors. 
    dot_product = sum(v1 * v2 for v1, v2 in zip(vector1, vector2))

    #Calculate the magnitudes of each vector, by calculating
    #the Euclidean norm: square root of the sum of squared elements. 
    magnitude1 = math.sqrt(sum(v1 ** 2 for v1 in vector1))
    magnitude2 = math.sqrt(sum(v2 ** 2 for v2 in vector2))

    #Ensure division by 0 is avoided, to ensure results are not undefined.
    #If either one of the texts has no meaningful content (empty vector - no words),
    #return 0.0 as the similarity score. 
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    
    #Calculate Cosine Similarity:
    #By taking the ratio of dot product to the product of magnitdues:
    return dot_product / (magnitude1 * magnitude2)

#Testing the function:
if __name__ == "__main__":
    f = open("data\The Great Gatsby.txt",encoding = "utf-8" )
    #Open the stored, The Great Gatsby text file.

    text1 = f.read() #Read the contents of the book.
    freq1 = process_book(text1) #Process the book text (count frequencies).
    f.close() #Close the file after reading.

    f2 = open("data\Tom Sawyer.txt",encoding = "utf-8" )
    #Open the stored, Tom Sawyer text file. 
    text2 = f2.read() #Read the contents of the book.
    freq2 = process_book(text2)  #Process the book text (count frequencies).
    f2.close() #Close the file after reading.

    #Call the function to calculate cosine similarity between both texts.
    #Compare the word frequencies of both books:
    similarity_score = cosine_similarity(freq1, freq2)

    #Print the cosine similarity score between both texts:
    print(f"Cosine Similarity between The Great Gatsby and Tom Sawyer: {similarity_score:.4f}")
    #Round the result to 4 decimal places. 



    