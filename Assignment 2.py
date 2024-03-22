#Retrieve the first review for the movie "Dead Poets Society"
from imdb import Cinemagoer
import string
import sys
from unicodedata import category
import nltk
from nltk.corpus import stopwords
# nltk.download('vader_lexicon')

ia = Cinemagoer()

movie = ia.search_movie("Dead Poets Society")[0]
print(movie.movieID)
#0097165

movie = ia.get_movie('0097165', info=['reviews'])
reviews = movie.get('reviews', [])

#Creates a list of words for the first review
moviereview = []
for review in reviews:
    print(review['content'])
    print()
    moviereview.append(review["content"])

# Start Pickling Data
import pickle

with open('moviereview.pkl','wb') as f:
    pickle.dump(moviereview,f)


with open('moviereview.pkl','rb') as f:
    reloaded_copy_of_texts = pickle.load(f)
#used "wb" and "rb" to specify binary write mode    

# print(reloaded_copy_of_texts)

# Part 2:
# Characterizing by Word Frequencies

def word_freq(texts):
    """
    removes punctuation and stop words
    use a **dictionary** where the keys are words that 
    appear and the values are frequencies of words in the text
    """
    d = {}
    strippables = string.punctuation + string.whitespace

    strippables = "".join(
        chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")
    )  # https://stackoverflow.com/questions/60983836/complete-set-of-punctuation-marks-for-python-not-just-ascii

    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    
    for line in reloaded_copy_of_texts:
        if line.startswith("*** END OF THE PROJECT"):
            break

        line = line.replace("-", " ").replace("/", " ").replace("(", " ").replace(")", " ").replace("'", " ").replace(".", " ").replace("?", " ").replace(":", " ")
        line = line.replace(
            chr(8212), " "
        )  # Unicode 8212 is the HTML decimal entity for em dash

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()
            if word and word not in stop_words: #created the dictionary without stop words
                d[word] = d.get(word, 0) + 1
    return d

word_frequencies = word_freq(reloaded_copy_of_texts)
print(word_frequencies)

# Computing Summary Statistics
def top_ten(d):
    """
        Identifies the top ten words that appeared in the review
    """
    top_ten = sorted(d.items(),key=lambda x: x[1], reverse = True)[:10]
    for word, frequency in top_ten:
        print(word, ":", frequency)

top_ten(word_frequencies)

# Removing stop words is already done when generating the word frequency dictionary

# Natural Language Processing
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentimental_analysis():
    """
    takes the sentiment scores and draws interesting arguments from the review
    """
    max_pos_score = -1
    max_neg_score = -1
    most_positive_line = ""
    most_negative_line = ""
    for line in reloaded_copy_of_texts:
        score = SentimentIntensityAnalyzer().polarity_scores(line)
        pos_score = score["pos"]
        neg_score = score["neg"]
        print("Text:", line)
        print("Sentiment Score:", score)
        if pos_score > max_pos_score: 
            #compares with the -1 at first and stores the previous score
            #because positive score is between 0 to 1, it can never be smaller than -1
            max_pos_score = pos_score
            most_positive_line = line
        if neg_score > max_neg_score:
            max_neg_score = neg_score
            most_negative_line = line
    print(f"The most positive line: {most_positive_line} ")
    print(f"The most negative line: {most_negative_line}")

sentimental_analysis()

#Part 3
