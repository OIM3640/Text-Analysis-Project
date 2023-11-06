import urllib.request


def remove_preamble(text, cutoff):
    """Takes two parameters. The first is the text and the second is a word whose first time appearing is either in the heading of the main body of the book or the first word of the first sentence. First the text is broken up into a list of individual words. Then a loop iterates until the cutoff word is reached. The condition cutoff_reached will then become true, activating the second conditional. The loop then adds that word and every subsequent word into a new list. The new list is then joined back together to become a string and it is returned."""
    words = text.split()  # string is broken up into individual words
    new_list = []
    cutoff_reached = (
        False  # starts off as false so everything preceding the cutoff is not added
    )
    for word in words:
        word = word.lower()  # words become lowercase to avoid confusion with the cutoff
        if cutoff == word:
            cutoff_reached = True  # remains true for the rest of the loop.
        if cutoff_reached:
            new_list.append(word)
    new_text = " ".join(new_list)
    return new_text


def only_alpha(word):
    """A bunch of other functions give wrong outputs if the word is attatched to a punctuation mark. I looked online and found this method called isalpha() that can determine if a character is a letter or not. The code runs through the word and removed all non-letter characters by creating a new string and only adding valid letters."""
    result = ""  # empty string waiting to be filled
    for letter in word:  # iterates through each letter
        if letter.isalpha():
            result = (
                result + letter
            )  # if the character is a valid letter then it is added to the new string
    return result


# Project Guttenberg

# Our War with Spain for Cuba's Freedom
url_1 = "https://www.gutenberg.org/cache/epub/4210/pg4210.txt"
with urllib.request.urlopen(url_1) as f:
    CF_original = f.read().decode("utf-8")
Cuba_freedom = remove_preamble(CF_original, "introduction.")
# print(Cuba_freedom) # for testing

# The History of Cuba, vol. 2
url_2 = "https://www.gutenberg.org/cache/epub/37676/pg37676.txt"
with urllib.request.urlopen(url_2) as f:
    HC_original = f.read().decode("utf-8")
history_Cuba = remove_preamble(HC_original, "when")
# print(history_Cuba) # for testing

# Thrilling Narratives of Mutiny, Murder and Piracy
url_3 = "https://www.gutenberg.org/cache/epub/25982/pg25982.txt"
with urllib.request.urlopen(url_3) as f:
    MMP_original = f.read().decode("utf-8")
murder_piracy = remove_preamble(MMP_original, "book")
# print(murder_piracy) # for testing
