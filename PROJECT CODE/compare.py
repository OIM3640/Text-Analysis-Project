"""I found that it would be interesting to compare the movie script , with the book, to see if they had many
similarities or not"""

"For this, I prompted CHATGPT with my idea to see where I could start"

import urllib.request
import string
from collections import defaultdict
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

book_url = 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt'
movie_script = 'data/The Great Gatsby Movie Script.txt'

def collect_text_url(url, skip_header = True, end_marker = "*** END OF THE PROJECT GUTENBERG EBOOK THE GREAT GATSBY ***"):
    with urllib.request.urlopen(url) as f:
        text = f.read().decode("utf-8")

    """This makes sure that the header is skipped as well as 
stopping before the credits/copyright"""

    if skip_header:
        start_index = text.lower().find("*** START OF THE PROJECT GUTENBERG EBOOK THE GREAT GATSBY ***")
        if start_index != -1:
            text = text[start_index:]
    if end_marker in text:
            end_index = text.lower().find(end_marker.lower())
            text = text[:end_index]
    return text

" This defines for the movie script to be read"

def collect_text_data(filepath='data/The Great Gatsby Movie Script.txt'):
    with open (filepath, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

"This cleans the text"

def clean_text(text):
    text = text.lower().translate(str.maketrans('','', string.punctuation)) # removes punctuation and makes all texts lower
    words = [word for word in text.split() if word not in stop_words] # removes stop words
    return " ".join(words) # keeps spaces between words

# cleans both texts, movie and book

book_text = clean_text(collect_text_url(book_url))
movie_script_text = clean_text(collect_text_data(movie_script))

# calculates the cosine similarity to see how similar they are

vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform([book_text,movie_script_text])

cosine_sim= cosine_similarity(vectors[0:1],vectors[1:2])
print(f"The Cosine Similarity between the book and the movie script is : {cosine_sim[0][0]}")


