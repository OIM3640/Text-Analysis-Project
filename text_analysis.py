import string
import random
from collections import Counter
import sys
from unicodedata import category
import urllib.request

# ######################################## READ BOOK #####################################################################
def read_book(url):
    """
    Downloadds and reads over Little Women book
    """
    try:
        with urllib.request.urlopen(url) as f:
            text = f.read().decode('utf-8')
            
            return text
    except Exception as e:
        print("An error occurred:", e)

def skip_gutenberg_header(text):
    """
    Removes Gutenberg header from text
    """
    lines = text.splitlines()
    start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK LITTLE WOMEN; OR, MEG, JO, BETH, AND AMY ***"

    for i, line in enumerate(lines):
        if start_marker in line: 
            return "\n".join(lines[i + 1:])
   
    raise ValueError(f"Header end marker '{start_marker}' not found in file.")

# ###################################### WORD FREQUENCY AND SUMMARY STATISTICS ###############################################

def process_text(text, skip_header):
    """
    Process the text and returns a histogram of the words
    """
    if skip_header:
        text = skip_gutenberg_header(text)

    hist = {}

    strippables = "".join(
        chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")
    )  

    for line in text.splitlines():
        if line.startswith("*** END OF THE PROJECT"):
            break

        line = line.replace("-", " ") #Removes unwanted symbols
        line = line.replace(chr(8212), " ")  # Em dash replacement

        for word in line.split():
            word = word.strip(strippables).lower() #determine words in text
            if word:
                hist[word] = hist.get(word, 0) + 1
    
    return hist

def most_common(hist, excluding_stopwords=False):
    """
    returns a sorted list of word-freq pairs, optionally filtering stopwords
    """
    stopwords = set(["the","and","to","of","a","in","that","it","is","was","he","for","on","with","her","i","she","you","as","but","his","so","at","him","had","be","not","if","all","my","one","me","they","when","do","up","by","have","which","like"])
    
    #Remove stopwords
    if excluding_stopwords:
        hist = {word: freq for word, freq in hist.items() if word not in stopwords}
    
    return sorted(hist.items(), key=lambda x: x[1], reverse=True)

def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.

    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    common_words = most_common(hist)[:num]
    for word, freq in common_words:
        print(f"{word}: {freq}")

# ######################################### NATURAL LANGUAGE PROCESSING #########################################################
# #Used the help of AI for most of this section, the code I wrote for spliting the chapters needed a lot of work and Claude AI helped me explaining how to use rh Sentiment Analysis tool
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import re

def split_into_chapters(text):
    """
    Splits book into chapters based on chapter heading
    """
    if not isinstance(text, str):
        print("warning: Input text is not a string. Converting to str")
        text = str(text)

    #Split chaper by the roman numbers
    pattern = r'(?:CHAPTER\s+)?([IVXLCDM]+)\.'
    
    try:
        split_text = re.split(pattern, text)
        if len(split_text)> 1:
            preface = split_text[0].strip()

            chapters = []
            if preface:
                chapters.append(preface)
            
            for i in range(2, len(split_text), 2):
                chapter_text = split_text[i].strip()
                if chapter_text:
                    chapters.append(chapter_text)
            print(f"Found {len(chapters)} chapters")
            return chapters

        #If roman number not found, try by looking for Chapter
        else:
            print("No chapters found with Roman numeral pattern.")
            alt_pattern = r'CHAPTER\s+\d+'
            split_text = re.split(alt_pattern, text)

            if len(split_text) > 1:
                chapters = [chunk.strip() for chunk in split_text if chunk.strip()]
                print(f"Found {len(chapters)} chapters using numerical pattern")
                return chapters
            else:
                print("Warning: Could not identify chapters")
                return [text]
    except Exception as e:
        print(f"Error splitting chapters: {e}")
        print("Treating the whole book as a single unit.")
        return [text]
    

def sentiment_analysis(text):
    """
    Performs sentiment analysis on text and returns polarity scores
    """
    try:
        nltk.data.find('sentiment/vader_lexicon.zip')
    except LookupError:
        nltk.download('vader_lexicon')
    
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    return score

def analyze_book_sentiment(url, chapter_level=True):
    """
    Analyzes sentiment throughout the book
    """
    raw_text = read_book(url)
    if not raw_text:
        return None
    
    text = skip_gutenberg_header(raw_text)

    #Overall sentiment of the book
    overall_sentiment = sentiment_analysis(text)
    print(f"Overall book sentiment: {overall_sentiment}")

    results = {
        'overall': overall_sentiment,
        'chapters': []
    }

    #Chapter by chapter analysis
    if chapter_level:
        chapters = split_into_chapters(text)
        print(f"Found {len(chapters)} chapters")

        chapter_sentiments = []
        for i, chapter in enumerate(chapters):
            sentiment = sentiment_analysis(chapter)
            chapter_sentiments.append(sentiment)
            results ['chapters'].append({
                'chapter': i+1,
                'sentiment': sentiment
            })
            print(f"Chapter {i+1} sentiment: {sentiment}")

    return results

def main():
    Little_Women_url = 'https://www.gutenberg.org/cache/epub/37106/pg37106.txt'
    Little_Women_Book = read_book(Little_Women_url)

    hist = process_text(Little_Women_Book, skip_header=True)
    print(hist)

    print("The most common words are:")
    t = most_common(hist, excluding_stopwords=True)

    for word, freq in t[0:10]:
        print(word, "\t", freq)
    
    results = analyze_book_sentiment(Little_Women_url)

    print("\nSentiment Analysis Summary:")
    print(f"Overall sentiment: {results['overall']['compound']}")

    if results['chapters']:
        chapter_compounds = [(ch['chapter'], ch['sentiment']['compound']) for ch in results['chapters']]
        most_positive = max(chapter_compounds, key=lambda x: x[1])
        most_negative = min(chapter_compounds, key=lambda x: x[1])
        
        print(f"Most positive chapter: Chapter {most_positive[0]} (score: {most_positive[1]:.2f})")
        print(f"Most negative chapter: Chapter {most_negative[0]} (score: {most_negative[1]:.2f})")

if __name__ == "__main__":
    main()



############################################### TEXT SIMILARITY & CLUSTERING ##################################################################
import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as pls
from thefuzz import fuzz

def fetch_text(url):
    """Gets text from the given URL"""
    try:
        with urllib.request.urlopen(url) as f:
            return f.read().decode('utf-8') #downloads the given urls
    except Exception as e:
        print("An error ocurred:", e)
        return ""
    
def compute_text_similarity(text1, text2):
    """Computes similarity between 2 texts"""
    return fuzz.ratio(text1, text2)

little_women_url = 'https://www.gutenberg.org/cache/epub/37106/pg37106.txt'
edwin_drood_url = 'https://www.gutenberg.org/cache/epub/564/pg564.txt'

little_women = fetch_text(little_women_url)
edwin_drood = fetch_text(edwin_drood_url)

texts = [little_women, edwin_drood]

num_texts = len(texts)
similarities = np.zeros((num_texts, num_texts))

# Calculate pairwise similarities
for i in range(num_texts):
    for j in range(i, num_texts):
        similarity = compute_text_similarity(texts[i], texts[j])
        similarities[i, j] = similarity
        similarities[j, i] = similarity

#Calculate dissimilarity (1 - similarity)
dissimilarities = 1 - similarities

#MDS
mds = MDS(dissimilarity='precomputed', random_state=42)
coordinates = mds.fit_transform(dissimilarities)

#Plot
plt.scatter(coordinates[:, 0], coordinates[:, 1])

#Label the points
for i in range(coordinates.shape[0]):
    plt.annotate(f"Text {i+1}", (coordinates[i, 0], coordinates[i, 1]))

plt.title('Text Clustering')
plt.xlabel('MDS Dimension 1')
plt.ylabel('MDS Dimension 2')
plt.show()


