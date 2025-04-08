import json
import string
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

def preprocess_text(text):
    """
    cleans and tokenizes the text. makes it lowercase, removes the punctuation and whitespace.
    """
    words = text.split()
    cleaned_words = []
    for word in words:
        cleaned_word = word.strip(string.punctuation + string.whitespace).lower()

        extra_cleaned_word = '' # cleans the word further. used this in one of the text analysis excercises.

        for char in cleaned_word:
            if char.isalpha():
                extra_cleaned_word += char
            
        extra_cleaned_word = extra_cleaned_word.lower()
        
        if extra_cleaned_word:
            cleaned_words.append(extra_cleaned_word)
    return cleaned_words

def extract_histograms_from_file(filepath):
    """
    loads JSON file and builds a sorted histogram for each article.
    returns a list of dictionaries sorted by descending frequency.
    """
    with open(filepath, "r", encoding="utf-8") as file:
        articles = json.load(file)

    histograms = []

    for article in articles[8:]: # the first 8 articles downloaded as descriptions of news categories so I'm removing them
        text = article.get("text", "")
        words = preprocess_text(text)
        histogram = {}

        for word in words:
            histogram[word] = histogram.get(word, 0) + 1

        sorted_histogram = dict(sorted(histogram.items(), key=lambda item: item[1], reverse=True)) # sort by value descending, and rebuild the dictionary in sorted order
        histograms.append(sorted_histogram)

    return histograms

def remove_stopwords_from_histogram(histogram, stop_words):
    """
    removes stop words from all histograms. the stop word list in __name__ was 
    created mannually by looking through outputs of the function and finding stop
    words and adding them to the list. 
    """
    
    filtered_histogram = {} # create an empty dictionary to store the filtered words

    for word, count in histogram.items(): # loop through each word and its count in the original histogram
        if word not in stop_words: # check if the word is NOT in the stop word list
            filtered_histogram[word] = count # add it to the new dictionary

    # Return the cleaned dictionary
    return filtered_histogram

def extract_top_words_from_histograms(histograms):
    """
    for each article's histogram, finds the highest word count,
    then collects all words with at least (max_count - 10) frequency.
    returns one combined list of selected words.
    """
    selected_words = []

    for histogram in histograms:

        max_freq = max(histogram.values())
        threshold = max_freq - 10

        for word, count in histogram.items():
            if count >= threshold:
                selected_words.append(word)

    return selected_words

if __name__ == "__main__":
    stop_words = set(stopwords.words("english"))
    stop_words.update(["advertisement", "said", "mr", "us", "—", "“i", "didnt", "youll", "loadingerror", "use", "well", "time", 
                       "also", "one", "like", "would", "many", "new", "including", "adfree", "way", "could", "youve", "cant", "adfree"])

    histograms = extract_histograms_from_file("project/data/theepochtimes_articles.json") # load histograms from file

    clean_histograms = [] # apply stopword removal to each histogram and store in a list

    for h in histograms:
        cleaned = remove_stopwords_from_histogram(h, stop_words)
        clean_histograms.append(cleaned)

    top_words = extract_top_words_from_histograms(clean_histograms)

    with open("project/data/theepochtimes_cleaned4.json", "w", encoding = "utf-8") as file:
        json.dump(top_words, file, indent = 2, ensure_ascii = False)

    # print(json.dumps(top_words, indent=2))
    # print(len(top_words))