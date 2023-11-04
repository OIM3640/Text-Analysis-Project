import urllib.request
import json

# Download the text, "The Great Gatsby" inside Python.
url = 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt'
with urllib.request.urlopen(url) as f:
    the_great_gatsby_texts = f.read().decode('utf-8')
    print(the_great_gatsby_texts) # for testing

# Save data to a file.
with open('gatsby_texts','w') as f:
    json.dump(the_great_gatsby_texts,f)

# Load data from a file.
with open('gatsby_texts','r') as f:
    reloaded_copy_of_texts = json.load(f)

