from mediawiki import MediaWiki
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

def wikipedia_content(title):
    """
    Retrieves the content of a Wikipedia page and returns the content.
    """
    wikipedia = MediaWiki()
    page = wikipedia.page(title)
    print(f"Title: {page.title}")
    return page.content

def preprocess_text(text):
    """
    Tokenizes and removes stop words to clean the text and returns filtered words.
    """
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalpha() and word not in stop_words]
    return filtered_words

def word_frequency_analysis(words):
    """
    Counts the frequency of words. Identifies and returns the most used words.
    """
    freq_dict = Counter(words)
    return freq_dict

if __name__ == "__main__":
    content = wikipedia_content("FC Barcelona")
    if content:
        processed_words = preprocess_text(content)
        word_freq = word_frequency_analysis(processed_words)

        print("Top 10 words by frequency:")
        for word, count in word_freq.most_common(10):
            print(f"{word}: {count}")
        