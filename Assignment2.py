# Import text
# *Frankenstein*
import urllib.request

url = 'https://www.gutenberg.org/cache/epub/42324/pg42324.txt'
try:
    with urllib.request.urlopen(url) as f:
        text = f.read().decode('utf-8')
        # print(text)  # For testing
except Exception as e:
    print("An error occurred:", e)


# *Wikipedia*
from mediawiki import MediaWiki

wikipedia = MediaWiki()
fiction = wikipedia.page("Gothic fiction")
print(fiction.title)
print(fiction.content)


# —————————————————————————————————————————————————————
# Text Cleaning and Preprocessing

# *Frankenstein*
import unicodedata

# Remove the Project Gutenberg header and footer
lines = []
copy = False

for line in text.splitlines():
    # Between the official start marker and the novel text, there is unneeded information like the novel's title page, translator's notes, publication information, etc. Keep reading lines until the last line of the description, then start storing the text. The novel starts with "INTRODUCTION."
    if "INTRODUCTION." in line:
        lines.append(line)
        copy = True
        continue
    # Stop reading lines at the end of the novel, which ends with "THE END."
    if "THE END." in line:
        lines.append(line)
        break

    if copy:
        lines.append(line)


# Manage punctuation: taken from Chapter 12 Notebook
punc_marks = {}

for line in lines:
    for char in line:
        category = unicodedata.category(char)
        if category.startswith('P'):
            punc_marks[char] = 1

# Turn dictionary keys into one string of punctuation symbols
punctuation = ''.join(punc_marks)

# Removed dashes
def split_line(line):
    return line.replace('--', ' ').split()

# Remove punctuation and standardize case
def clean_word(word):
    return word.strip(punctuation).lower()

# Generate cleaned list of words
cleaned_frank = []

for line in lines:
    for word in split_line(line):   # split each line into words
        word = clean_word(word)
        if word != "":              # ignore empty strings
            cleaned_frank.append(word)

# Check: there are 77935 words total after cleaning
print(len(cleaned_frank))


# *Wikipedia*
# Similar cleaning process for Wikipedia article on Gothic fiction
text = fiction.content
lines = text.splitlines()

# Manage punctuation
punc_marks = {}

for line in lines:
    for char in line:
        category = unicodedata.category(char)
        if category.startswith('P'):
            punc_marks[char] = 1

# Turn dictionary keys into one string of punctuation symbols
punctuation = ''.join(punc_marks)

# Remove dashes
def split_line(line):
    return line.replace('—', ' ').replace('–', ' ').split()

# Remove punctuation, standardize case, and remove numbers
def clean_word(word):
    word = word.strip(punctuation).lower()
    if word.isdigit():        # skip pure numbers
        return ""
    return word

# Generate cleaned list of words
cleaned_wiki = []

for line in lines:
    for word in split_line(line):
        word = clean_word(word)
        if word != "":
            cleaned_wiki.append(word)

# Check total word count
print(len(cleaned_wiki))


# —————————————————————————————————————————————————————
# Removing Stop Words

# *Frankenstein*
# Create a set containing the stop words from stopwords.txt
with open("stopwords.txt", "r", encoding="utf-8") as f:
    stopwords = set(f.read().split())

# 2. Create a new list with no stop words
final_frank = []

for word in cleaned_frank:
    if word not in stopwords:
        final_frank.append(word)

# Check: there are 36015 words total after removing stop words
print(len(final_frank))


# *Wikipedia*
final_wiki = []

for word in cleaned_wiki:
    if word not in stopwords:
        final_wiki.append(word)

# Check total word count after removing stop words
print(len(final_wiki))


# —————————————————————————————————————————————————————
# Word Frequency Analysis

# *Frankenstein*
# Use the word list with no stop words to find word frequencies
unique_frank = set(final_frank)
print(len(unique_frank))

# Create a dictionary that maps each word to its frequency
word_counter = {}
for word in final_frank:
    word_counter[word] = word_counter.get(word, 0) + 1

# print(word_counter)


# *Wikipedia*
unique_wiki = set(final_wiki)
print(len(unique_wiki))

word_counter2 = {}
for word in final_wiki:
    word_counter2[word] = word_counter2.get(word, 0) + 1

# print(word_counter2)


# —————————————————————————————————————————————————————
# Computing Summary Statistics

# ***Top n Most Frequent Words***
# Sort the (word, count) pairs by frequency, highest first
def second_element(t):
    return t[1]

# *Frankenstein*
items_frank = sorted(word_counter.items(), key=second_element, reverse=True)

# Print the n most frequent words and their counts
def print_most_common(word_counter, n):
    items_frank = sorted(word_counter.items(), key=second_element, reverse=True)
    for word, freq in items_frank[:n]:
        print(word, freq, sep='\t')

print_most_common(word_counter, 10)

# *Wikipedia*
items_wiki = sorted(word_counter2.items(), key=second_element, reverse=True)

# Print the 10 most frequent words and their counts
def print_most_common(word_counter2, n):
    items_wiki = sorted(word_counter2.items(), key=second_element, reverse=True)
    for word, freq in items_wiki[:n]:
        print(word, freq, sep='\t')

print_most_common(word_counter, 10)


# —————————————————————————————————————————————————————
# Data Visualization

# —————————————————————————————————————————————————————
# Natural Language Processing
