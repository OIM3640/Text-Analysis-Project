import urllib.request
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer


url = 'http://www.gutenberg.org/ebooks/730.txt.utf-8'
with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')
    # print(text) # for testing

stopwords = ['a', 'an', 'and', 'are', 'as', 'at', 'be', 'but', 'by', 'for', 'if', 'in', 'into', 'is', 'it', 'no', 'not', 'of', 'on', 'or', 'such', 'that', 'the', 'their', 'then', 'there', 'these', 'they', 'this', 'to', 'was', 'will','with']

def processing(input_str):
    # Define a regular expression pattern to match English letters and spaces
    pattern = r'[^a-zA-Z\s]'
    # Use re.sub to replace non-matching characters with an empty string
    cleaned_str = re.sub(pattern, '', input_str)
    return cleaned_str

def processing2(s):
    '''
    clean the str
    '''
    text = processing(s)
    text = text.replace('\r', ' ')
    text = text.replace('\n', ' ')
    text = text.lower()
    while '  ' in text:
        text = text.replace('  ', ' ')
    return text

def cintext(s):
    '''
    sort str in to a dictionary with the frequency of each word
    '''
    s = processing2(s)
    l = s.split(" ")
    d = {}
    for word in l:
        d[word]=d.get(word,0)+1
    return d

def total_words(d):
    '''
    Calculate the total number of words in the text
    '''
    total = 0
    for v in d.values():
        total += v
    return total

# print (total_words(text))

def top(d, num):
    '''
    return a list of the (num) most frequent words
    '''
    l = []
    value = sorted(list(set(d.values())), reverse=True)
    for i in range(num):
        for k in d.keys():
            if d[k] == value[i]:
                l.append(k)
    return l

def nonStopwords(s):
    '''
    clean all stopwords
    '''
    d = cintext(s)
    for word in stopwords:
        del d[word]
    return d

print (top(cintext(text), 20))
print (top(nonStopwords(text), 20))

def at(s):
    '''
    calculate Sentiment score for str
    '''
    score = SentimentIntensityAnalyzer().polarity_scores(s)
    return score

#print (at(processing2(text)), at(text))

def pat(dic):
    '''
    calculate the average Sentiment score for keys in a dic
    '''
    d = {'neg':0, 'neu':0, 'pos':0, 'compound':0}
    ave = {}
    for word in dic.keys():
        temp = at(word)
        for k in d.keys():
            d[k] += temp[k]*dic[word]
    for k in d.keys():
        ave[k] = d[k]/total_words(dic)
    return ave

# print (pat(cintext(text)), pat(nonStopwords(text)))






