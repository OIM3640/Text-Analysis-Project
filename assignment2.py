from newspaper import Article
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from operator import itemgetter
import nltk 
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('punkt')


stop_words = set(nltk.corpus.stopwords.words('english')) # Got this through ChatGPT as the function below wasn't running without this
def removing_stopwords(article_text): 
    """
    This function removes any stopwords using the NLTK library, to help improve analysis and outputs a clean text
    """
    # I used a mix spotintelligence and geeksforgeeks to understand the NLTK library to remove stopwords, instead of doing it manually
    tokens = article_text.split()
    filtered_text = [word for word in tokens if word.lower() not in stop_words]
    return ' '.join(filtered_text)

def word_frequency(clean_text):
    """
    This function counts the frequency of every word throughout the article and removes any 'words' it detects that have numbers (eg. 15) and any special characters (eg. %)
    """
    tokens = clean_text.split()
    word_freq = {}
    for word in tokens:
        word = word.lower()
        special_char = False
        for char in word:
            if not char.isalpha():
                special_char = True
        if special_char == False:
            if word not in word_freq:
                word_freq[word] = 1
            else:
                word_freq[word] += 1
    return word_freq

def top_ten_words(word_freq):
    """
    This function outputs the top 10 words that are seen in the text. There are 3 methods here below: 2 are mine and 1 is from ChatGPT. This was due to lot of complications and time spent on the error
    """
# My method 1
    n = 10
    top_words = []
    unique_words = 0
    sorted_words = sorted(word_freq.items(), key=itemgetter(1), reverse=True) # Used geeksforgeeks: python n largest values - as a reference
    for word,count in sorted_words:
        if word not in top_words:
            top_words.append(word, count)
            unique_words += 1
        if unique_words == n:
            break
    return top_words

# My method 2
    # top_words = {}
    # for word,count in word_freq:
    #     if word_freq[count] > word_freq[count - 1]:
    #         top_words.append(word,count)
    #     if len(top_words) == 10:
    #         break
    # return top_words

# ChatGPT's method
    # sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    # top_words = sorted_word_freq[:10]
    # return top_words

def sentiment_analyser(clean_text):
    """
    This function further uses NLTK libraries to conduct sentiment analysis on the text to observe how positive/negative it may be
    """
    score = SentimentIntensityAnalyzer().polarity_scores(clean_text)
    return score

def main():
    """
    This is the main function
    """
    url = 'https://www.usatoday.com/story/money/2024/03/20/march-federal-reserve-meeting-live-updates/73027664007/'
    article = Article(url)
    article.download()
    article.parse()
    article_text = article.text
    #print(article_text)

    clean_text = removing_stopwords(article_text)
    #print(clean_text)

    word_freq = word_frequency(clean_text)
    print("The Word Frequency is as follows:")
    word_freq_output = " ".join([f"{word}: {count}" for word, count in word_freq.items()]) # Used GPT to help format 
    print(word_freq_output)

    sentiment_score = sentiment_analyser(clean_text)
    print(sentiment_score)

    top = top_ten_words(word_freq)
    print("The top 10 words:")
    top1 = " ".join([f"{word}: {count}" for word, count in top.items()])
    print(top1)

if __name__ == "__main__":
    main()