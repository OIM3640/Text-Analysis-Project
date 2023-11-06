import part1

CF = part1.Cuba_freedon
HC = part1.history_Cuba

def word_frequency(text, target):
    """This counts the amount of times a specific word appears in the chosen text. Please make the target word all lowercase, even if it is a proper noun
    """
    # Splits text into words by whitespace and punctuation
    # given from https://www.w3schools.com/python/ref_string_split.asp
    words = text.split()
    # Dictionary for storage
    word_count = {}
    nonzero = False
    for word in words:
        # Converts the word to all lowercase to account for proper nouns and sentence capitalizations
        word = word.lower()
        # Remove any non-alphabetic characters from the word
        #Given from https://stackoverflow.com/questions/22520932/python-remove-all-non-alphabet-chars-from-string
        word = ''.join(filter(str.isalpha, word))
        # Update the word count dictionary if 'word' is the desired word
        if word==target:
            word_count[word] = word_count.get(word, 0) + 1
            nonzero = True
    #if the word is not in the text at all, then it will return 0 instead of an empty dictionary
    if nonzero:
        return word_count
    else:
        word_count[target] = 0
        return word_count


def compare_word_count(t1, t2):
    """Prompts the user to say how many words they would like to compare, and then asks for each word individually. Each word is stored in a list. Then, word_frequency is called for the 'word' in t1. The result is added to a list. Then, the same is done for the second text. Then the program moves onto the next word and it repeats until it has iterated the entire list. The result is a chart showing the word count for each text, side-by-side. (I recommend the words cuba, sandy, and troop)
    """
    print('Welcome! How many words would you like to compare')
    amount = int(input('Type: ')) 
    comparables = [] #stores list of words being compared
    text_1_count = [] #stores the word count for text 1
    text_2_count = [] #stores the word count for text 2
    for i in range(amount):
        x = input('What word would you like to compare? Type: ')
        comparables.append(x)
    for i in range(amount):
        text_1_count.append(word_frequency(t1, comparables[i]))
        text_2_count.append(word_frequency(t2, comparables[i]))
    print()
    print('Below are the results')
    for i in range(amount):
        print(f'Text 1: {text_1_count[i]}      Text 2: {text_2_count[i]}')




compare_word_count(CF, HC)
