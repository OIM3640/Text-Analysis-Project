import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
import string  # Import the string module

from mediawiki import MediaWiki
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
from googletrans import Translator
from rake_nltk import Rake


def get_panama_wikipedia_content():
    wikipedia = MediaWiki()
    Panama = wikipedia.page("Panama")
    text = Panama.content
    summary = Panama.summary
    return text, summary

def filter_words(text):
    words = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    special_characters = string.punctuation
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words and not any(char.isdigit() for char in word) and word.lower() != "de" and all(char not in special_characters for char in word)]
    return filtered_words

def translate_to_spanish(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='es')
    return translation.text

def find_top_words(filtered_words, n=10):
    word_counts = Counter(filtered_words)
    top_words = word_counts.most_common(n)
    return top_words

def find_top_keywords(text, n=10):
    text = text.replace("(", "").replace(")", "").replace("==", "")
    r = Rake()
    r.extract_keywords_from_text(text)
    keywords = r.get_ranked_phrases()[:n]
    keywords_score = r.get_ranked_phrases_with_scores()[:n]
    top_keywords = [(round(rating, 2), keyword) for rating, keyword in keywords_score if rating > 30]
    return top_keywords

def main():
    nltk.download('stopwords')
    nltk.download('punkt')

    stop_words = set(stopwords.words("english"))
    content, summary = get_panama_wikipedia_content()
    filtered_words = filter_words(content)

    # Translate the summary to Spanish
    translated_summary = translate_to_spanish(summary)
    print('Here is the summary of Panama in Spanish:')
    print(translated_summary)
    
    # Top 10 words
    top_words = find_top_words(filtered_words, n=10)
    print("Top 10 words:")
    for word, count in top_words:
        percentage = (count / len(filtered_words) * 100)
        print(f"{word}: {count} times ({percentage:.2f}%)")
    
    # Top 10 keywords
    top_keywords = find_top_keywords(content, n=10)
    print("Top 10 keywords:")
    for rating, keyword in top_keywords:
        print(f"{keyword} ({rating})")

if __name__ == "__main__":
    main()
