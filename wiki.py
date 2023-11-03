from mediawiki import MediaWiki
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords


# used for nltk stopwords resource! https://pythonspot.com/nltk-stop-words/
def remove_stop_words(data):
    """takes stop words out of the data set and returns all other words"""
    filtered_words = []
    stopWords = set(stopwords.words('english'))
    words = word_tokenize(data)

    for w in words:
        if w not in stopWords and w not in ",()==.''":
            filtered_words.append(w)
    return filtered_words


def word_frequencies(words):
    """prints the frequency of each word in the text, excluding stop words"""
    frequency = nltk.FreqDist(words)
    # asked chatgpt to help me sort the frequencies in line 24
    sorted_freq = frequency.most_common()
    for word, freq in sorted_freq:
        print(f'{word}: {freq}')

# used chatgpt to help me clarify what goes in main


def main():
    wikipedia = MediaWiki()
    # print(capybara.title)
    # print(capybara.content)
    capybara = wikipedia.page("Capybara")
    guinea_pig = wikipedia.page("Guinea Pig")
    capybara_text = capybara.content
    guinea_pig_text = guinea_pig.content

    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('vader_lexicon')

    non_stop_words = remove_stop_words(capybara_text)
    print(remove_stop_words(capybara_text))
    print(word_frequencies(non_stop_words))

    # Sentiment test example test
    from nltk.sentiment.vader import SentimentIntensityAnalyzer

    # sentence = 'Software Design is my favorite class because learning Python is so cool!'
    # score = SentimentIntensityAnalyzer().polarity_scores(sentence)
    data = capybara_text
    score = SentimentIntensityAnalyzer().polarity_scores(data)
    print(score)

    # from github.com/seatgeek/thefuzz example
    from thefuzz import fuzz
    from thefuzz import process
    print(fuzz.ratio(guinea_pig_text, capybara_text))
    print(fuzz.ratio(guinea_pig_text, guinea_pig_text))


if __name__ == "__main__":
    main()
