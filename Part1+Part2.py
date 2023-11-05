import urllib.request
import json
import string
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from thefuzz import fuzz
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# Download the text 1, "The Great Gatsby" inside Python.
url = 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt'
with urllib.request.urlopen(url) as f:
    downloaded_the_great_gatsby = f.read().decode('utf-8')
    print(downloaded_the_great_gatsby) # for testing
# Save data to a file.
with open('the_great_gatsby_texts','w') as f:
    json.dump(downloaded_the_great_gatsby,f)
# Load data from a file.
with open('the_great_gatsby_texts','r') as f:
    great_gatsby = json.load(f)


# Download the text 2, "The Age of Innocence" inside Python.
url = 'https://www.gutenberg.org/cache/epub/541/pg541.txt'
with urllib.request.urlopen(url) as f:
    downloaded_the_age_of_innocence = f.read().decode('utf-8')
    print(downloaded_the_age_of_innocence) # for testing
# Save data to a file.
with open('the_age_of_innocence_texts','w') as f:
    json.dump(downloaded_the_age_of_innocence,f)
# Load data from a file.
with open('the_age_of_innocence_texts','r') as f:
    age_of_innocence = json.load(f)


# Process the gatsby_texts and showing the word frequencies.
def process_file(text_file):
    """
    Create a histogram that contains the words in gatsby_texts, and return a map from each word to the number of times it appears in the gatsby_texts.
    """
    hist = {}

    strippables = string.punctuation + string.whitespace

    after_header = False

    for line in text_file.split('\n'):
        if line.startswith('*** START OF THE PROJECT'):
            after_header = True
            continue
        if not after_header:
            continue
        if line.lstrip().startswith('*** END OF THE PROJECT'):
            break

        line = line.replace('-', ' ')
        line = line.replace(
            chr(8212), ' '
        )  # Unicode 8212 is the HTML decimal entity for em dash

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist

# Total words
def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    sum = 0 
    for i in hist:
        sum += hist[i]
    return sum

# Number of different words
def different_words(hist):
    """Returns the number of different words in a histogram."""
    num_of_diff_words = 0
    for i in hist:
        if hist[i] == 1:
            num_of_diff_words += 1
    return num_of_diff_words

# Print the most common words with their frequencies. 
def most_common(hist, excluding_stopwords=True):
    """
    Make a list of word-frequency pairs in descending order of frequency.
    """
    frequency_list = []
    stop_words_list = []
    stop_words = open('data/stopwords.txt')
    for line in stop_words:
        word = line.strip()
        stop_words_list.append(word)
        
    for word, frequency in hist.items():
        if excluding_stopwords:
            if word in stop_words_list:
                continue
        frequency_list.append((frequency, word))
    frequency_list.sort(reverse=True)
    return frequency_list

# Find the top 15 overlapping most common words between the two books.
def find_overlapping_words(d1, d2):
    """Returns a dictionary with all keys that appear in both d1 and d2.

    d1, d2: dictionaries
    """
    d = []
    counter = 0
    for word in d1:
        if word in d2:
           d.append(word)
           counter +=1
           if counter == 15:
               break
    return d

# Word Cloud
def generate_word_cloud(text_file):
    wordcloud = WordCloud(width=800, height=400).generate(text_file)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation = "bilinear")
    plt.axis("off")
    plt.show()

# Natural Language Processing
def nltk_score(text_file):
    """
    Return the results of sentiment analysis using VADER library in NLTK.
    """
    score = SentimentIntensityAnalyzer().polarity_scores(text_file)
    return score

# Text Similarity
def similarity_ratios(text_file_1, text_file2):
    simple_ratio = fuzz.ratio(text_file_1, text_file2)
    print(f"The simple ratio using fuzz is: {simple_ratio} ")

    token_sort_ratio = fuzz.token_sort_ratio(text_file_1, text_file2)
    print(f"The token sort ratio using fuzz is: {token_sort_ratio} ")

    token_set_ratio = fuzz.token_set_ratio(text_file_1, text_file2)
    print(f"The token set ratio using fuzz is: {token_set_ratio} ")



def main():
    great_gatsby_hist = process_file(great_gatsby)
    age_of_innocence_hist = process_file(age_of_innocence)

    print('Total number of words in "The Great Gatsby":', total_words(great_gatsby_hist))
    print('Number of different words in "The Great Gatsby":', different_words(great_gatsby_hist))

    print('Total number of words in "The Age Of Innocence":', total_words(age_of_innocence_hist))
    print('Number of different words in "The Age Of Innocence":', different_words(age_of_innocence_hist))

    gatsby_frequency_list = most_common(great_gatsby_hist,  excluding_stopwords=True)
    print('The most common 20 words in "The Great Gatsby" are:')
    for freq, word in gatsby_frequency_list[0:20]:
        print(word, '\t', freq)
    
    innocence_frequency_list = most_common(age_of_innocence_hist,  excluding_stopwords=True)
    print('The most common 20 words in "The Age of Innocence" are:')
    for freq, word in innocence_frequency_list[0:20]:
        print(word, '\t', freq)

    print("See the graph for the word cloud of the Great Gatsby:")
    generate_word_cloud(great_gatsby)
    print("See the graph for the word cloud of the Age of Innocence:")
    generate_word_cloud(age_of_innocence)

    overlapping_words = find_overlapping_words(gatsby_frequency_list, innocence_frequency_list)    
    print("The top 15 overlapping common words between the two books are:")
    for word in overlapping_words:
        print(word, '\t')

    great_gatsby_nltk_score = nltk_score(great_gatsby)
    print(f"The sentiment analysis score for The great Gastby is:\n{great_gatsby_nltk_score}")

    age_of_innocence_nltk_score = nltk_score(age_of_innocence)
    print(f"The sentiment analysis score for The Age of Innocence is:\n{age_of_innocence_nltk_score}")

    similarity_ratios(great_gatsby, age_of_innocence)

if __name__ == '__main__':
    main()
