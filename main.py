from collections import Counter
from nltk.corpus import stopwords  
from thefuzz import fuzz
from utilities import download_book, clean_text
from visualize_similarities import compare_fitz_shakespeare

def analyze_text(text):
    """
    Analyzes word frequency in the given text, returning a dictionary with words as keys and 
    their counts as values.
    
    Args:
        text (str): The text to analyze.
    
    Returns:
        dict: A dictionary where keys are words and values are the frequency of each word.
    """
    words = text.split()
    counts = dict()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def top_words(text):
    """
    Prints the top 10 most common words in the given text.
    
    Args:
        text (str): The text to analyze for top words.
    """
    counts = Counter(text.split())
    print(counts.most_common(10))



def analyze_book_text(cleaned_text):
    """
    Analyzes and prints word frequencies and top words in the cleaned text.
    
    Args:
        cleaned_text (str): The cleaned text to analyze.
    """
    top_words(cleaned_text)

def main():
    """
    Main function to download, clean, and analyze texts from two books and calculate text similarity.
    Downloads 'The Great Gatsby' and 'This Side of Paradise' from Project Gutenberg, cleans the text, 
    analyzes top words, and calculates the similarity ratio between the two books.
    """
    gatsby_url = 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt'
    gatsby_file_name = "gatsby_text.pkl"
    gatsby_text = download_book(gatsby_url, gatsby_file_name)
    gatsby_cleaned_text = clean_text(gatsby_text)
    analyze_book_text(gatsby_cleaned_text)
    
    paradise_url = 'https://www.gutenberg.org/cache/epub/805/pg805.txt'
    paradise_file_name = "paradise_text.pkl"
    paradise_text = download_book(paradise_url, paradise_file_name)
    paradise_cleaned_text = clean_text(paradise_text)
    analyze_book_text(paradise_cleaned_text)

    # Text Similarity
    print(fuzz.ratio(gatsby_cleaned_text, paradise_cleaned_text))  # Similarity ratio

    #Compare Fitzgerald and Shakespeare
    compare_fitz_shakespeare()

    
# Run program by running main
if __name__ == "__main__":
    main()
