import urllib.request

# Save data to a file (will be part of your data fetching script)

#with open('dickens_texts.pickle','w') as f:
    #pickle.dump(charles_dickens_texts,f)


# Load data from a file (will be part of your data processing script)
#with open('dickens_texts.pickle','r') as f:
    #reloaded_copy_of_texts = pickle.load(f)

#Project Guttenberg
url1 = 'https://www.gutenberg.org/cache/epub/4210/pg4210.txt'
with urllib.request.urlopen(url1) as f:
    CF_original = f.read().decode('utf-8')
    #I found the character count by copying what I wanted removed into Word
    #Our War with Spain for Cuba's Freedom is the name of url1
    #print(Cuba_freedom) # for testing

def word_frequency(text, target):
    # Split the text into words by whitespace and punctuation
    words = text.split()
    # Initialize an empty dictionary to store word frequencies
    word_count = dict
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

#print(word_frequency(Cuba_freedom, 'cuba'))

def remove_preamble(text):
    count = 0
    checker = 0
    words = text
    key = build_key()
    key_tooth = key[0]

    for word in words:
        count= count+1
        if word == key_tooth:
            key_tooth = key[checker+1]
            checker = checker+1
        if checker == 12:
            break
    print(text[count:])
            
    

def build_key():
    print('Type the unique heading of the section immediately following the preamble EXACTLY as it appears. Everything before this heading will be removed.')
    chosen = input('Type here: ')
    key = []
    for i in range(len(chosen)):
        key.append(chosen[i])
    return key


remove_preamble(CF_original)
#print(len(CF_original))


