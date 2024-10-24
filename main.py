
import urllib.request
import pickle
url = 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt'
with urllib.request.urlopen(url) as f:
    gatsby_text = f.read().decode('utf-8')
   
# Save data to a file (will be part of your data fetching script)

with open('gatsby_text.pkl','w') as f:
    
    pickle.dump(gatsby_text,f)


# Load data from a file (will be part of your data processing script)
##with open('dickens_texts.pkl','r') as f:
    ##reloaded_copy_of_texts = pickle.load(f)