# THE FILE IS DEDICATED TO TESTING CODE FROM CHATGPT

import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer



text = "This is a sample text."
words = word_tokenize(text)
pos_tags = nltk.pos_tag(words)

print(pos_tags)



text = "Steve Jobs was the co-founder of Apple Inc."
words = word_tokenize(text)
ne_tags = nltk.ne_chunk(nltk.pos_tag(words))

print(ne_tags)



from nltk.sentiment import SentimentIntensityAnalyzer

def sentiment_score(wordlist):
    total_pos_score = 0
    for word in wordlist:
        score = SentimentIntensityAnalyzer().polarity_scores(word)
        pos_value = score['pos']
        if pos_value > 0:
            total_pos_score += pos_value

    return total_pos_score

wordlist = ['good', 'great', 'excellent']
result = sentiment_score(wordlist)
print(result)
