# The part includes the NLP, Sentivity Analysis
import urllib.request
from nltk.tokenize import sent_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# The Picture of Dorian Gray, by Oscar Wilde
url = 'https://www.gutenberg.org/cache/epub/30120/pg30120.txt'
with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')
    # print(text) # for testing

# Natural Language Processor

nltk.download('vader_lexicon')

# Example

sentence = 'Software Design is my favorite class because learning Python is so cool!'
score = SentimentIntensityAnalyzer().polarity_scores(sentence)
print(score)

# Sentivity Analysis
# this is because when I run without this line, the output is always error, saying no punkt.
nltk.download('punkt')

sentences = nltk.sent_tokenize(text)
# From internet, I understand that sentiment analysis can only be applied to sentences.
# Tokenize is to make the text split into tokens of sentences.

if text:
    scores = []
    for sentence in sentences:
        score = SentimentIntensityAnalyzer().polarity_scores(sentence)
        scores.append((sentence, score['compound']))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    highest_score_sentence = sorted_scores[0][0]
    lowest_score_sentence = sorted_scores[-1][0]
    print("Sentence with the highest sentiment score:")
    print(highest_score_sentence)
    print("\nSentence with the lowest sentiment score:")
    # The first half of the book's score runs out, however, it output urllib.error.HTTPError: HTTP Error 404: Not Found
    print(lowest_score_sentence)
    for sentence, score in sorted_scores:
        print(sentence, score)  # print all the sentences with a score
