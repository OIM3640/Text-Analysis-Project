from mediawiki import MediaWiki

wikipedia = MediaWiki()
babson = wikipedia.page("Babson College")
babson_content = babson.content
olin = wikipedia.page("Olin College")
olin_content = olin.content
brandeis = wikipedia.page("Brandeis College")
brandeis_content = brandeis.content
# print(babson.title)
# print(babson.content)

# Characterizing by Word Frequencies
def process_file ():
    '''
    Use a dictionary where the keys are words that appear and the 
    values are frequencies of words in the text.
    '''
    words = babson_content.split()
    # words = olin_content.split()

    hist = {}
    for word in words:
        word = word.lower()
        # I asked ChatGPT about How to remove spaces in a given text in python? 
        # See detailed conversation: https://chat.openai.com/share/4949941e-4239-413f-9bfb-7d5ab82f6b3a 
        word = word.replace(' ', '')
        word = word.replace('-', '') 
        word = word.replace('—', '') 
        word = word.replace('.', '')
        word = word.replace('=','')
        word = word.replace('(','')
        word = word.replace(')','')

        if word:
            # I learned it from session 15-analyze_book
            hist[word] = hist.get(word,0) + 1
        
        # if word in hist:
        #     hist[word] += 1
        # else:
        #     hist[word] = 1

    return hist


# I asked ChatGPT to give me a good list of stop words to be removed from text in python
# See detailed conversation: https://chat.openai.com/share/e3c76a99-8f45-4913-ae7f-6e69b8e1122b 

# ChatGPT at first inspires me to use NLTK to get a list of common English stop words:
# import nltk
# nltk.download('stopwords')
# from nltk.corpus import stopwords

# stop_words = set(stopwords.words('english'))
# print(stop_words)

stopwords =  [
     "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
    "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers",
    "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves",
    "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are",
    "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does",
    "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until",
    "while", "of", "at", "by", "for", "with", "about", "against", "between", "into",
    "through", "during", "before", "after", "above", "below", "to", "from", "up", "down",
    "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here",
    "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more",
    "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so",
    "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"
    ]
# print(stopwords)


# Removing Stop Words
def remove_stop(hist, excluding_stopwords=True):
    ## I copied this docstring from session 15-analyze_book exercise
    '''
    Removing stop words can help to reduce the size of the text data and 
    improve the accuracy of analysis

    Makes a list of word-freq pairs(tuples) in descending order of frequency.

    hist: map from word to frequency
    excluding_stopwords: a boolean value. If it is True, do not include any stopwords in the list.

    returns: list of (frequency, word) pairs
    '''
    t = []

    # I learned it from session 15-analyze_book
    for word, freq in hist.items():
        if excluding_stopwords:
            if word in stopwords:
                continue

        t.append((freq,word))
    
    t.sort(reverse=True)
    return t

# Computing Summary Statistics
def most_common(hist, num=10):
    '''
    Prints the most commons words in a histgram and their frequencies.

    hist: histogram (map from word to frequency)
    num: number of words to print
    '''
    t = remove_stop(hist)
    print('The most common words are:')
    for freq, word in t[:num]:
        # I learned it from session 15-analyze_book
        print(word, '\t', freq)

# Natural Language Processing
def nltktest():
    '''
    This function perform sentiment analysis on given text using NLTK
    '''
    # Following code were inspired from the assigment instruction, so I asked ChatGPT to explain each line of codes and NLTK for me:
    # See below conversation: https://chat.openai.com/share/a7249e2b-d61a-4c9e-91a3-9f35db18a5a5 
    from nltk.sentiment.vader import SentimentIntensityAnalyzer

    sentence = babson_content
    score = SentimentIntensityAnalyzer().polarity_scores(sentence)
    print(score)

# Text Similarity
def fuzztext(text, reference_text):
    '''
    Fuzzy string matching like a boss. It uses Levenshtein Distance to calculate 
    the differences between sequences in a simple-to-use package.
    This function calculate different types of text similarity scores between
    the given text and reference_text
    '''
    # I leanred it from the instruction linked: https://github.com/seatgeek/thefuzz
    from thefuzz import fuzz 

    similarity = fuzz.ratio(text,reference_text)
    partial_similarity = fuzz.partial_ratio(text, reference_text)
    token_similarity = fuzz.token_set_ratio(text, reference_text)

    print('Ratio Similarity:', similarity)
    print('Partial Similarity:', partial_similarity) 
    print('Token similarity:', token_similarity) 



if __name__ == "__main__":
    print(process_file())

    hist = process_file()
    t = remove_stop(hist,excluding_stopwords=True)
    print('Removed stop_words data:')
    print(t)

    most_common(hist, 10)

    print(f'The polarity scores are: {nltktest()}')

    text = babson_content
    reference_text = brandeis_content
    fuzztext(text, reference_text)