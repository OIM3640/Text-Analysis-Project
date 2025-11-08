#%%md 1. Harvest the Text
import urllib.request # To open and read URLs
import re # To match regular expressions
import unicodedata # To normalize texts

url = 'https://www.gutenberg.org/cache/epub/1513/pg1513.txt'
try:
    with urllib.request.urlopen(url) as f:
        text = f.read().decode('utf-8')
        print(text)  # for testing
except Exception as e:
    print("An error occurred:", e)
#%%md 2. Analyzing the text
#%%md Step 1: Text Cleaning and Processing 
try:
    # Remove text before and after the main content 
    start = re.search(r"\*\*\* START OF THE PROJECT GUTENBERG EBOOK .* \*\*\*", text)
    end = re.search(r"\*\*\* END OF THE PROJECT GUTENBERG EBOOK .* \*\*\*", text)
    if start and end:
        text = text[start.end():end.start()]
    else:
        print("Warning: Could not find Gutenberg delimiters; cleaning entire text")

    # Step 3: Normalize unicode
    text = unicodedata.normalize("NFKD", text)

    # Step 4: Remove HTML tags and special characters
    text = re.sub(r"<.*?>", " ", text)  
    text = re.sub(r"[^a-zA-Z0-9\s.,;:'\"!?-]", " ", text)

    # Step 5: Convert to lowercase
    text = text.lower()

    # Step 6: Replace multiple spaces/newlines with one space
    text = re.sub(r"\s+", " ", text).strip()

    # Step 7: Tokenize into words
    tokens = re.findall(r"\b\w+\b", text)

    # Step 8: Print short preview
    #print("Cleaned text preview:\n", text[:])
    #print("\nTotal words:", len(tokens))
except Exception as e:
    print("An error occurred:", e)
#%%md Step 2: Removing Stop Words 
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
# Define the stop words set
stop_words = set(stopwords.words('english'))
# Filter out stop words
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
#print("Filtered tokens:", filtered_tokens)
print("\nTotal Filtered:", len(filtered_tokens))
print("\nTotal Original:", len(tokens))

# Step 7: (Optional) Rejoin filtered words into cleaned text
cleaned_text = " ".join(filtered_tokens)
# Step 8: Print results
print("Original text:\n", text[:50])
print("\nCleaned text:\n", cleaned_text[:50])
print("\nTokens before stopword removal:\n", tokens[:50])
print("\nTokens after stopword removal:\n", filtered_tokens[:50])

# %%md Step 3: Frequency Analysis
# Step 9: Count word frequencies
word_freq = {}
for word in filtered_tokens:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
#%%md Step 4: Computing Summary Statistics 
#Print the top 50 words
top_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:50]
print("\nTop 50 most frequent words:\n" ,  top_words)

#Calculate average word length
total_length = sum(len(word) * count for word, count in word_freq.items())
total_words = sum(word_freq.values())
average_word_length = total_length / total_words if total_words > 0 else 0
print(f"\nAverage word length: {average_word_length:.2f}")

#Calculate vocabulary size
vocabulary_size = len(word_freq)
print(f"\nVocabulary size: {vocabulary_size}")

#Calculate vocabulary richness
vocabulary_richness = vocabulary_size / total_words if total_words > 0 else 0
print(f"\nVocabulary richness: {vocabulary_richness:.4f}")

#%%md Part 3: Learning with AI 
# I will talk about two problems I ran into while doing this 
#assignment. The first problem I had was how to install the nltk. 
# The Problem: One problem that I had that took me 1.5 hours to 
# figure out even with the use of AI was how to install the nltk even if the environment
# I used stated that I had already installed it. 

