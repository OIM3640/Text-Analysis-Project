import urllib.request
import sys
from unicodedata import category
import re
import markovify



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

    text = text.lower() # Makes everything lowercase for uniformity 

    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")] # Identifies punctuation and stores it in variable
    )
    additional_strippables = ''.join([chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith(("P","Z"))]) # P is punctional & Z is seperator

    words = re.findall(r'\b\w+\b', text) # \b is word boundary that makes sure only complete words are used
    
    for word in words:
        word = word.strip(strippables) # Gets rid of punctuation
        hist[word] = hist.get(word, 0) + 1 # adds words to dictionary

    return hist

def totalwords(hist):
    """
    Returns total number of words counted in histogram
    Borrowed from analyze_books.py
    """
    return sum(hist.values()) # Sum frequencies of each value

def differentwords(hist):
    """
    Returns number of different words in histogram
    Borrowed from analyze_books.py
    """
    return len(hist) # Number of unique keys in histogram

def remove_stopwords(hist):
    """
    Removes words in stopwords.txt file that also appear in histogram
    """
    with open('assignment2/stopwords.txt', 'r') as f:
        stopwords = f.read().splitlines() # Read stopwords as each line
    
    for word in stopwords: # Removes each stopword from frequency dictionary
        hist.pop(word, None) 

    return hist

def longest_word(hist):
    """
    Finds and returns longest non-stopword in histogram
    """
    words = list(hist.keys()) # Creates a list of key values in the hist dictionary aka every unique word in the text
    longest_word = max(words, key=len) # Finds word with the most characters
    return longest_word

def shortest_word(hist):
    """
    Finds and returns shortest non-stopword in histogram
    """
    words = [word for word in hist.keys() if word.strip()] # Excludes empty strings which is important because we're looking for shortest
    shortest_word = min(words, key=len) # Finds shortest word that has at least 1 char
    return shortest_word

def most_common(hist):
    """
    Makes a list of word-freq pairs(tuples) in descending order of frequency.
    MODIFIED FROM OIM3640/SESSION15/ANALYZE_BOOKS_SOL.PY
    """
    t = [] # Empty list to store word-freq pairs
    for word, freq in hist.items():
        t.append((freq, word)) # Add each pair as a tuple to the list t

    t.sort(reverse=True) # Sort list is desc order based on frequency
    return t

def top_10(hist, n=10):
    """
    Prints the most commons words in a histgram and their frequencies.
    TAKEN FROM OIM3640/SESSION15/ANALYZE_BOOKS_SOL.PY
    """
    common_words = most_common(hist)[:n] # Get the top N most common words based on frequency using most_common() function

    for frequency, word in common_words: # Print words and their frequency
        print(f'{word}: {frequency}')

def dict_to_text(hist):
    """
    Converts frequency dictionary into text
    Necessary function to perform later analysis
    """
    text = ' '.join(hist.keys()) # Joins words with a space
    return text

def jaccard_similarity(text1, text2):
    """
    Jaccard Similarity Coefficient: https://en.wikipedia.org/wiki/Jaccard_index
    Measures the similarity between 2 sets by dividing the size of their intersection by the size of their union
    """
    set1 = set(text1.split()) # Converts to set data structure which is an unordered collect of unique elements
    set2 = set(text2.split())

    intersection = set1.intersection(set2) # Find intersection of 2 sets (common words)
    union = set1.union(set2) # Find union of the 2 sets (All unique words)
    similarity = len(intersection)/len(union) # Calculate Jaccard Similarity Coefficent using the formula: Jaccard Similarity = (Size of Intersection) / (Size of Union) 

    return similarity

def markov_paragraph(text1, text2, sentence=8):
    combined = text1 + text2 # Combine the 2 texts for training
    model = markovify.Text(combined, state_size=2) # Create a training model that checks every 2 words to determine generation of n+1

    paragraph = "" # Creates string
    for _ in range(sentence): # Uses _ to loop 8 times (sentences=8) to create 8 sentence paragraph
        sentence = model.make_short_sentence(max_chars=200) # Maxes sentence length at 200 characters
        paragraph += sentence + ' ' # Adds space betwene sentences

    return paragraph

def main():
    global ptext, mtext # Making these global so I can easily access them both throughout the project
    p_url = 'http://www.gutenberg.org/ebooks/1497.txt.utf-8'
    with urllib.request.urlopen(p_url) as p: # p for Plato
        ptext = p.read().decode('utf-8')

    m_url = 'http://www.gutenberg.org/ebooks/2680.txt.utf-8'
    with urllib.request.urlopen(m_url) as m: # m for Marcus
        mtext = m.read().decode('utf-8')

    paragraph = markov_paragraph(ptext, mtext)

    ptext = preprocess(ptext)
    mtext = preprocess(mtext)

    print(f"Plato's 'The Republic' has {totalwords(ptext)} words and Marucs Aurelius's Meditations has {totalwords(mtext)}")
    print(f"Plato's 'The Republic' has {totalwords(ptext) - totalwords(mtext)} more words than Marcus Aurelius's Mediations\n")
    print(f"Plato's 'The Republic' has {differentwords(ptext)} different words and Marcus Aurelius's Meditations has {differentwords(mtext)} different words")
    print(f"Plato's 'The Republic' has {differentwords(ptext) - differentwords(mtext)} more different words than Marcus Aurelius's Mediations\n")

    ptext = remove_stopwords(ptext)
    mtext = remove_stopwords(mtext)

    print(f"Without stopwords, Plato's 'The Republic' has {totalwords(ptext)} and Marcus Aurelius's Meditations has {totalwords(mtext)}")
    print(f"Without stopwords, Plato's 'The Republic' has {totalwords(ptext)-totalwords(mtext)} more words than Marcus Aurelius's Meditations\n")
    print(f"Without stopwords, Plato's 'The Republic' has {differentwords(ptext)} different words and Marcus Aurelius's Meditations has {differentwords(mtext)} different words")
    print(f"Without stopwords, Plato's 'The Republic' has {differentwords(ptext)-differentwords(mtext)} more different words than Marcus Aurelius's Meditations\n")

    print(f"Without stopwords, the lexical difference of 'The Republic' is {differentwords(ptext)/totalwords(ptext)*100:.2f}%")
    print(f"Without stopwords, the lexical difference of 'Meditations' is {differentwords(mtext)/totalwords(mtext)*100:.2f}%\n")

    print(f"The longest word in The Republic is {longest_word(ptext)}")
    print(f"The longest word in Meditations is {longest_word(mtext)}\n")

    print(f"The shortest word in The Republic is {shortest_word(ptext)}")
    print(f"The shortest word in Meditations is {shortest_word(mtext)}\n")

    p = most_common(ptext)
    print('The most common words in The Republic are:')
    for freq, word in p[0:10]:
        print(word, '\t', freq)
    
    m = most_common(mtext)
    print('The most common words in Meditations are:')
    for freq, word in m[0:10]:
        print(word, '\t', freq)
    print()

    ptext_text = dict_to_text(ptext)
    mtext_text = dict_to_text(mtext)
    jaccard_similarity(ptext_text, mtext_text)

    print(f"The Jaccard Similarity between 'The Republic' and 'Meditations' is {jaccard_similarity(ptext_text, mtext_text):.4f}\n")

    print("Markov Text Synthesis generated the following paragraph using 'The Republic' and 'Meditations'\n")
    print(paragraph)
    

    
if __name__ == '__main__':
    main()