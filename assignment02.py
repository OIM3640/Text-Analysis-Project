import urllib.request
import random
import string
import sys
from collections import Counter
from unicodedata import category


# Load the text from Project Gutenberg
url = "https://www.gutenberg.org/cache/epub/5200/pg5200-images.html"
try:
    with urllib.request.urlopen(url) as f:
        metamorphosis = f.read().decode("utf-8")
except Exception as e:
    print("An error occurred:", e)
    sys.exit(1)  

def remove_gutenberg_header(text):
    """Removes the Project Gutenberg header and returns the processed text.

    text: string (entire content of the book)

    returns: string without the header.
    """
    start_marker = "START OF THE PROJECT"
    lines = text.splitlines()

    for i, line in enumerate(lines):
        if start_marker.lower() in line.lower():  # Case-insensitive search
            return "\n".join(lines[i+1:])  

    raise ValueError(f"Header marker '{start_marker}' not found in text.")

# REMOVING STOPWORDS

def loading_stopwords():
    import nltk
    # nltk.download('stopwords')
    from nltk.corpus import stopwords

    import nltk
    # nltk.download('punkt')

    stop_words = list(stopwords.words('english'))
    return stop_words
 
def removing_stop_words(text):
    stop_words = loading_stopwords()
    
    from nltk.tokenize import word_tokenize
    word_tokens = word_tokenize(text)
 
    filtered_sentence = []
    filtered_sentence = [w for w in word_tokens if w.lower() not in stop_words]
    
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    return filtered_sentence


# PART 2 - Analyzing the tezt
def total_words(text):
    """Finds the total words in the text"""
    total = 0
    for line in text:
        total += 1
    return total 

def creates_histogram(text):
    """Creates a histogram of all the words the in the text"""

    # strippables = string.punctuation + string.whitespace
    strippables = "".join(
        chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")
    )

    histogram = {}
    if isinstance(text, list):
        text = " ".join(text)

    for line in text.splitlines():
        line = line.replace("-", " ")
        line = line.replace(chr(8212), " ")  # Replace em dash

        for word in line.split():
            word = word.strip(strippables).lower()
            histogram[word] = histogram.get(word, 0) + 1  # Increment count

    return histogram

def percentage_tf(text, total):
    """Calculates the term frequency in percentage - percentage of the text that the word makes up."""
    percentages = {}
    for word in text:
        value = text[word]  # Retrieve the count of the word
        percentages[word] = value / total
    return percentages

def top_ten_perc(percentages):
    """Sorts the percentage frequencies of all the words and prints the top 10"""
    sorted_perc = sorted(percentages.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_perc[3:13]: # excluding the top three which are spaces and characters
        print(f"{word}: {count}")

def computing_summary(histogram):
    """This prints the top 10 terms by frequency in a nice formats"""
    sorted_histogram = sorted(histogram.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_histogram[3:13]: # excluding the top three which are spaces and characters
        print(f"{word}: {count}")

## SENTIMENT ANALYSIS ##
from textblob import TextBlob

def analyze_sentiment(text):
    """Analyzes sentiment using TextBlob and returns average polarity. Positive sentences are
    cloesr to 1 and negative sentences are closer to -1. The output is the average sentiment of the entire text.
    It splits every sentence up and computes the sentiment analysis and returns the average."""
    sentences = text.split(".")  # Split into sentences
    polarities = [TextBlob(sentence).sentiment.polarity for sentence in sentences if sentence.strip()]

    avg_polarity = sum(polarities) / len(polarities) if polarities else 0
    return avg_polarity

def main():
    # Process the text and remove the header and stopwords
    processed_text = remove_gutenberg_header(metamorphosis)
    final_text = removing_stop_words(processed_text)

    ############# Part 2 ###############

    # # TOTAL WORDS IN THE TEXT W AND WITHOUT STOPWORDS
    # number_words = total_words(processed_text)
    # print(f"The total amount of words in this text are {number_words}.")
    total_without = total_words(final_text)
    # print(f"Without stopwords, the number of words in this text are {total_without}.")

    # # CREATES A HISTOGRAM OF FREQUENCIES
    histogram = creates_histogram(final_text)
    # print(histogram)

    # Calculate the percentage of frequency of words
    percentage = percentage_tf(histogram, total_without)
    # print(percentage)

    # Top 10 percentages 
    # top_ten_perc(percentage)

    # HISTOGRAM OF THE TOP 10 MOST COMMON WORDS
    # computing_summary(histogram) # must make sure that the histogram variable is not commented out

    # Sentiment analysis
    sentiment_score = analyze_sentiment(processed_text)
    print(f"Sentiment Score: {sentiment_score:.2f}") # output = 0.03. This means that the text is fairly neutral.


if __name__ == "__main__":
    main()

