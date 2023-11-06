from mediawiki import MediaWiki
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import string
from googletrans import Translator
from rake_nltk import Rake
""" We are going to be analyzing the Wikipedia page "Panama".
    1. We are going to be using the library nltk to remove the stopwords and find what are the 10 most common words that appear in Panama's page. (We won't take into account numbers, special characters, and the word "de").
    2. Then we are going to be using Rake nltk to find the top 10 keywords in Panama's Website.
    3. We are going to be translating Panama's summary to Spanish; Panama's first language.
    """

def panama_content():
    wikipedia = MediaWiki()
    Panama = wikipedia.page("Panama")
    return Panama.content

def filter_words(text):
    words = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    special_characters = string.punctuation
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words and not any(char.isdigit() for char in word) and word.lower() != "de" and word.lower() != "percent" and word.lower() !="us" and word.lower() != "also" and all(char not in special_characters for char in word)]
    return filter_words

def translate_spanish(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='es')
    return translation.text

def find_top_words(filtered_words, n=10):
    word_counts = Counter(filtered_words)
    top_words = word_count.most_common(n)
    return top_words

def find_top_keywords(text, n=10):
    text = text.replace("(", "").replace(")", "").replace("==", "")
    r = Rake(stopwords=stop_words, include_repeated_phrases=False)
    r.extract_keywords_from_text(text)
    keywords = r.get_ranked_phrases()[:n]
    keywords_score = r.get_ranked_phrases_with_scores()[:n] 
    top_keywords = [(round(rating,2), keyword) for rating, keyword in keywords_score if rating >30]   
    return top_keywords

def main():
    content = panama_content()
    filtered_words = filter_words(content)
    
    # Top 10 words
    top_words = find_top_words(filtered_words, n=10)
    print("Top 10 words:")
    for word, count in top_words:
        percentage = (count / len(filtered_words) * 100)
        print(f"{word}: {count} times ({percentage:.2f}%)")
    
    # Translate the summary to Spanish
    translated_summary = translate_to_spanish(content)
    print('Here is the summary of Panama in Spanish:')
    print(translated_summary)
    
    # Top 10 keywords
    top_keywords = find_top_keywords(content, n=10)
    print("Top 10 keywords:")
    for rating, keyword in top_keywords:
        print(f"{keyword} ({rating})")

if __name__ == '__main__':
    main()

#    # Find the word that appears the most and its count. Top 10 words
#     print("Top 10 words:")
#     for word, count in word_counts.most_common(10):
#         percentage = (count / len(filtered_words) * 100)
#         print(f"{word}: {count} times ({percentage:.2f}%)")

#     """ Translate the summary for Panama to Spanish """


#     print('Here is the summary of Panama in Spanish.')
#     print(translate_to_spanish(Panama.summary))

#     """ Top 10 keywords """


#     # r = Rake(stopwords=stop_words, include_repeated_phrases=False, min_length=1, max_length=2)

#     for rating, keyword in keywords_score:
#         if rating > 30:
#             # print(round(rating, 2), keyword)
#             pass

#     print(set([keyword for keyword in keywords if len(keyword.split()) > 1]))
#     print(keyword)
#     print(keywords_score)

# if __name__ == "__main__":
#     analyze_panama_wikipedia()
