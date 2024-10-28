
from collections import Counter
import re 
import urllib.request
import pickle
import os

def download_book(gutenberg_url,file_name):
    """
    
    """
    #if we have already downloaded book to disk, just read book from disk to avoid api request
    if os.path.exists(file_name):
        with open(file_name,'rb') as f:
            reloaded_copy_of_texts = pickle.load(f)
            return reloaded_copy_of_texts
    
    #if we don't have copy of book already, save to disk for future references
    else:
        with urllib.request.urlopen(gutenberg_url) as f:
            text = f.read().decode('utf-8')
        with open(file_name,'wb') as f:
            pickle.dump(text,f)
            return text

def analyze_text(text):
    words=text.split()
    counts=dict()
    for word in words:
        if word in counts:
            counts[word]=counts[word]+1
        else:
            counts[word]=1
    return counts

def top_words(text):
    counts=Counter(text.split())
    print(counts.most_common(10))

STOP_WORDS = {"so","he","she","but", "my","his","him","my","me","you","at","her","had", "we", "i", "and", "the", "a", "an", "in", "to", "of", "that", "it", "is", "for", "with", "as", "on", "this", "by", "was", "be", "or", "are"}
def clean_text(text):
    """
    TO DO: Set up function to clean text
    periods, question marks, quotes, :, 
    Remove stop words (So, we, I, and, the)
    """
    #Make sure all words are lowercase
    text=text.lower() 
    #Make sure punctuation is removed from words in text
    text = re.sub(r'[^\w\s]', '', text)
    
    # Remove stop words
    words = text.split()
    filtered_words = [word for word in words if word not in STOP_WORDS]
    
    # Join filtered words back into a single string
    cleaned_text = " ".join(filtered_words)
    
    return cleaned_text
    #Make every word lowercase
    ##text=text.lower() 
    ##return text


def main():
    gatsby_url = 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt'
    file_name="gatsby_text.pkl"
    text=download_book(gatsby_url,file_name)
    cleaned_text=clean_text(text)
    print(analyze_text(cleaned_text))
    top_words(cleaned_text)


#run program by running main
if __name__ == "__main__":
    main()