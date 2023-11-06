from mediawiki import MediaWiki
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import string

""" We are going to be analyzing the Wikipedia page "Panama". 
1. We are going to be using the library nltk to remove the stopwords and find what are the 10 most common words that appear in Panama's page. (We wont take into account numbers, special characters, and the word "de"
2. Then we are going to be using Rake nltk to find the top 10 keywords in Panama's Website).
3. We are going to be translating Panama's summary to Spanish; Panama's first language.
"""


#download stopwords
# nltk.download('stopwords')
# nltk.download('punkt')

#get content from wikipedia
wikipedia = MediaWiki()
Panama = wikipedia.page("Panama")
text = Panama.content
# print(Panama.logos)
# print(Panama.summary)
#print(Panama.images)

""" Top 10 words"""
#convert the text into words
words = word_tokenize(text)

#Define a list of English stopwords and string of special characters
stop_words = set(stopwords.words("english"))
special_characters = string.punctuation

#Filter out the stopwords, words that contain numbers, the word "de" and special characters and convert words to lowercase
filtered_words = [word.lower() for word in words if word.lower() not in stop_words and not any(char.isdigit() for char in word) and word.lower() != "de" and all(char not in special_characters for char in word)]

#Count the frequency of each word
word_counts = Counter(filtered_words)

#Find the word that appears the most and its count.top 10 words
# print("Top 10 words:")
# for word, count in word_counts.most_common(10):
#     percentage = (count / len(filtered_words) * 100)
#     print(f"{word}: {count} times ({percentage:.2f}%)")


""" translate the summary for panama to spanish"""

from googletrans import Translator
def translate_to_spanish(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='es')
    return translation.text

print('Here is the summary of Panama in Spanish.')
print(translate_to_spanish(Panama.summary))


""" top 10 keywords"""

from rake_nltk import Rake

text = text.replace("(","").replace(")", "").replace("==","")

# r = Rake(stopwords=stop_words, include_repeated_phrases=False, min_length=1, max_length=2)
r = Rake(stopwords=stop_words, include_repeated_phrases=False)
r.extract_keywords_from_text(text)
keywords = r.get_ranked_phrases()[:10]
keywords_score = r.get_ranked_phrases_with_scores()[:10]
for rating, keyword in keywords_score:
    if rating > 30:
        print(round(rating,2), keyword)
        
    

# print(set([keyword for keyword in keywords if len(keyword.split()) > 1]))
# print(keyword)

# print(keywords_score)

"""find flag of pty"""

# page = Panama."Flag of Panama"
if page.exists():
    images = page.images
    flag_image = None

    for image in images:
        if 'flag of panama' in image.lower():
            flag_image = image
            break

    if flag_image:
        print(f"URL of the flag of Panama: {flag_image}")
    else:
        print("Flag image not found on the Wikipedia page.")
else:
    print("Wikipedia page not found for 'Flag_of_Panama'.")