#For this project, I decided to use Data Source: Project Gutenberg to download /
# and analyze The Great Gatsby


import urllib.request
import string
from string import punctuation
from unicodedata import category
from collections import defaultdict
import nltk
from nltk.corpus import stopwords

url = 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt'
with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')
    #print(text) # for testing

    """"
    I looked up a way to use the NLTK tool to remove stopwords easier"""
#   https://pythonspot.com/nltk-stop-words/

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def analyze_text(url,skip_header=True):
    """This downloads the text from the URL, and creates the function to skip the header of the book so it isn't counted"""
    word_freq = defaultdict(int)
    # hist = defaultdict(int)

    with urllib.request.urlopen(url) as f:
        text = f.read().decode("utf-8")

    if skip_header:
        text= skip_gatsby_header(text)

    for line in text.splitlines():
        """This makes the count of the words end when it reachers the end of the book"""
        
        if line.startswith("*** END OF THE PROJECT GUTENBERG EBOOK THE GREAT GATSBY ***"):
            break

        line = line.lower().translate(str.maketrans('','', string.punctuation)) # This makes all words lowercase

        for word in line.split():
            if word not in stop_words:
                word_freq[word] += 1
                print (f"{word}: {word_freq[word]}") # This will print the every word in the book with the frequency
    return word_freq

def skip_gatsby_header(text):
    """This defines the function in order to skip the header and go straight into the book"""
    start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK THE GREAT GATSBY ***"
    start_index = text.lower().find(start_marker.lower()) 
    return text [start_index:] if start_index != -1 else text

# def total_words(hist):
#     "This gives me a summary of the amount of total words used in the book"
#     return sum (hist.values())

def most_common(word_freq, num=10):
    "This defines the top 10 words used in the book"
    freq_word_top10 = [(freq, word) for word, freq in word_freq.items()]
    freq_word_top10.sort(reverse=True)
    return freq_word_top10[:num]

def main():
    word_freq = analyze_text(url,skip_header=True)
    
    "This gives me the total amount of words in the book"
    total_words = sum(word_freq.values())
    print(f" Total number of words(exluding stop words): {total_words}")

    print("The 10 frequent words are:")
    for freq, word in most_common(word_freq):
        print(f"{word}\t{freq}")
    
    """Because I am a big fan of the book and movie, I wanted to test how many times the word 'party' and 'parties'
    were used, since the parties are a huge component of the film/book, to my surprise, it was said less times than I thought"""
    
    my_word = "party"
    my_word2 = "parties"
    print( f" The word I chose, '{my_word}', is mentioned {word_freq.get(my_word,0)} times in the book.")
    print( f" The word I chose, '{my_word2}', is mentioned {word_freq.get(my_word2,0)} times in the book.")


if __name__ == "__main__":
    main()


