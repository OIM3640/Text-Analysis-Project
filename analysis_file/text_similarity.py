from fuzzywuzzy import fuzz
import urllib.request

# The Picture of Dorian Gray, by Oscar Wilde
url = 'http://www.gutenberg.org/ebooks/174.txt.utf-8'
with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')


# Text Similarity
# The Happy Prince and Other Tales, by Oscar Wilde
url2 = 'https://www.gutenberg.org/cache/epub/30120/pg30120.txt'
with urllib.request.urlopen(url2) as g:
    text2 = g.read().decode('utf-8')
    # print(text_aih) # for testing


# Example
print(fuzz.ratio("this is a test", "this is a test!"))  # 97
print(fuzz.partial_ratio("this is a test", "this is a test!"))  # 100
print(fuzz.ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear"))  # 91
print(fuzz.token_sort_ratio("fuzzy wuzzy was a bear",
      "wuzzy fuzzy was a bear"))  # 100

# For the two text by Oscar Wilde, determine the similarity in using similar words (author's habits)

score = fuzz.ratio(text, text2)
print("Text similarity score:", score)

words1 = set(text.split())  # create a set of words from first text
words2 = set(text2.split())  # create another set of words from second text
# fuzz.token_set_radio usage from https://medium.com/nlpgurukool/fuzzy-matching-1baac719aa25
similarity_scores = [(w, fuzz.token_set_ratio(w, words2)) for w in words1]
most_similar = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[:10]
