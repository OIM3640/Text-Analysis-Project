import urllib.request
import sys
from unicodedata import category



def preprocess(text):
    """
    Removes the non crucial parts of the book like release dates and terms and conditions of use
    Converts words to lowercase
    Creates word frequency dictionary

    Returns:
    Word frequency dictionary after preprocessing

    This function is a modified version of our analyze_book.py assignment
    """
    hist = dict() # Creates dictionary 
    start = text.find("START OF THE PROJECT GUTENBERG EBOOK")
    end = text.find("END OF THE PROJECT GUTENBERG EBOOK")
    text = text[start:end] # Creates a list of all words between start and end indexes

    text = text.lower().split() # Makes everything lowercase for uniformity and splits text into words

    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")] # Identifies punctuation and stores it in variable
    )

    for line in text:
        line = line.replace('-', ' ') # Gets ride of em dashes
        line = line.replace(
            chr(8212), ' '
        )  # Unicode 8212 is the HTML decimal entity for em dash

        for word in line.split():
            word = word.strip(strippables) # Gets rid of punctuation
            # update the dictionary
            hist[word] = hist.get(word, 0) + 1 # adds words to dictionary

    return hist

def totalwords(hist):
    """
    Returns total number of words counted in histogram
    Borrowed from analyze_books.py
    """
    return sum(hist.values())

def differentwords(hist):
    """
    Returns number of different words in histogram
    Borrowed from analyze_books.py
    """
    return len(hist)

def remove_stopwords(hist):
    """
    Removes words in stopwords.txt file that also appear in histogram
    """
    with open('assignment2/stopwords.txt', 'r') as f:
        stopwords = f.read().splitlines()
    
    for word in stopwords:
        hist.pop(word, None)

    return hist


def main():
    global ptext, mtext # Making these global so I can easily access them both throughout the project
    p_url = 'http://www.gutenberg.org/ebooks/1497.txt.utf-8'
    with urllib.request.urlopen(p_url) as p: # p for Plato
        ptext = p.read().decode('utf-8')

    m_url = 'http://www.gutenberg.org/ebooks/2680.txt.utf-8'
    with urllib.request.urlopen(m_url) as m: # m for Marcus
        mtext = m.read().decode('utf-8')

    ptext = preprocess(ptext)
    mtext = preprocess(mtext)

    print(f"Plato's 'The Republic' has {totalwords(ptext)} words and Marucs Aurelius's Meditations has {totalwords(mtext)}")
    print(f"Plato's 'The Republic' has {differentwords(ptext)} different words and Marcus Aurelius's Meditations has {differentwords(mtext)} different words")

    ptext = remove_stopwords(ptext)
    mtext = remove_stopwords(mtext)

    print(f"Without stopwords, Plato's 'The Republic' has {totalwords(ptext)} and Marcus Aurelius's Meditations has {totalwords(mtext)}")
    print(f"Without stopwords, Plato's 'The Republic' has {differentwords(ptext)} different words and Marcus Aurelius's Meditations has {differentwords(mtext)} different words")

if __name__ == '__main__':
    main()