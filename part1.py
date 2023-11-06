import urllib.request
import pickle

# Save data to a file (will be part of your data fetching script)

#with open('dickens_texts.pickle','w') as f:
    #pickle.dump(charles_dickens_texts,f)


# Load data from a file (will be part of your data processing script)
#with open('dickens_texts.pickle','r') as f:
    #reloaded_copy_of_texts = pickle.load(f)

#Project Guttenberg
url1 = 'https://www.gutenberg.org/cache/epub/4210/pg4210.txt'
with urllib.request.urlopen(url1) as f:
    Cuba_freedom = f.read().decode('utf-8')
    #Our War with Spain for Cuba's Freedom is the name of url1
    print(Cuba_freedom) # for testing

def word_frequency(text, target):
    # Split the text into words by whitespace and punctuation
    words = text.split()
    
    # Initialize an empty dictionary to store word frequencies
    word_count = {}

    # Iterate through the words and count their frequencies
    for word in words:
        # Convert the word to lowercase to ensure case-insensitive counting
        word = word.lower()
        
        # Remove any non-alphabetic characters from the word
        word = ''.join(filter(str.isalpha, word))
        
        # Update the word count dictionary
        if word==target:
            word_count[word] = word_count.get(word, 0) + 1

    return word_count

print(word_frequency(Cuba_freedom, 'cuba'))

