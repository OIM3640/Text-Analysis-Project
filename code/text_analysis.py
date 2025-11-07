import unicodedata


def read_data(filename): 
    """Read all lines from a text file"""
    with open(filename, "r", encoding="utf-8") as file: #r是只读file，
        data = file.readlines()
        print("Number of lines:", len(data))
        print("Type:", type(data))
        print("\nFirst 5 lines preview:\n", data[:5])
    return data

def clean_text(lines): 
    """docstring"""
    clean = []
    for line in lines: 
        new_line = ""
        for character in line: 
            if unicodedata.category(character).startswith('C'):
                # if character is c, meaning its controled character""" 
                continue
            if character.isalpha() or character.isspace(): 
                new_line += character.lower()
                # "if character is character, add it lowercase to new line"
            else: 
                new_line += ' '
                "if character is puncation, replace with space"
        new_line = new_line.strip()   
        if new_line != "":            #GENERATE BY GHATGPT 
            clean.append(new_line)
    
    text = ""
    for line in clean:
        text += line + " "
    return text

stopword = {
    "a","about","above","after","again","against","all","am","an","and","any",
    "are","aren't","as","at","be","because","been","before","being","below",
    "between","both","but","by","can't","cannot","could","couldn't","did",
    "didn't","do","does","doesn't","doing","don't","down","during","each",
    "few","for","from","further","had","hadn't","has","hasn't","have","haven't",
    "having","he","he'd","he'll","he's","her","here","here's","hers","herself",
    "him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in",
    "into","is","isn't","it","it's","its","itself","let's","me","more","most",
    "mustn't","my","myself","no","nor","not","of","off","on","once","only","or",
    "other","ought","our","ours","ourselves","out","over","own","same","shan't",
    "she","she'd","she'll","she's","should","shouldn't","so","some","such",
    "than","that","that's","the","their","theirs","them","themselves","then",
    "there","there's","these","they","they'd","they'll","they're","they've",
    "this","those","through","to","too","under","until","up","very","was",
    "wasn't","we","we'd","we'll","we're","we've","were","weren't","what",
    "what's","when","when's","where","where's","which","while","who","who's",
    "whom","why","why's","with","won't","would","wouldn't","you","you'd",
    "you'll","you're","you've","your","yours","yourself","yourselves" }
#use Professor's stop words file, create text file###

def stopwords(words): 
    """remove stopwords """
    result = [] 
    for w in words: 
        if w not in stopword: 
            result.append(w)
    return result

def dictonary(words2): 
    dictionary = {}
    for word in words2: 
        if word not in dictionary: 
            dictionary[word] = 1
        else: 
            dictionary[word] += 1
    return dictionary

def most_common(dictionary):
    """Convert dictionary to list of tuples.不能改了，方便排序"""
    t = []
    for word, freq in dictionary.items():
        t.append((freq, word))
    t.sort(reverse=True)
    """sort is ranking the frequency"""
    return t

def main(): 
    filename = "jane_eyre.txt"
    lines = read_data(filename)
    cleaned = clean_text(lines)
    words = cleaned.split()
    filtered_words = stopwords(words)
    word_dict = dictonary(filtered_words)
    common = most_common(word_dict)

    cleaned = clean_text(lines)
    print("\n=== Clean Text Check ===")
    print("Length of cleaned text:", len(cleaned))
    print("First 3000 characters:\n", cleaned[:3000])
###chat给的检查code

    print("\nTop 10 most common words:")
    for freq, word in common[:10]:
        print(word, freq)

    # Computatig Summary Statistics 
    print("\nSummary Statistics:")
    total_words = len(filtered_words)
    unique_words = len(word_dict)
    average_freq = sum(word_dict.values()) / len(word_dict)
    richness = unique_words / total_words 
    

    print("Total words:", total_words)
    print("Unique words:", unique_words)
    print("Average frequency:", average_freq)
    print("Vocabulary richness:", richness)
    print("Most common word:", common[0])

    total_chars = 0 
    """generate evertge word length"""
    for w in filtered_words: 
        total_chars += len(w)
    avg_word_length = total_chars / total_words
    print("\nAverage word length:", avg_word_length)
###还有其他要用的方法吗

    common = most_common(word_dict)
    print("\nTop 20 Word Frequency Bar Chart (ASCII)")
    max_freq = common[0][0]
    for freq, word in common[:20]:
        bar = "#" * int(freq / max_freq * 40)
        print(f"{word:15} | {bar} ({freq})")
### 用gpt写的可以吗



if __name__ == "__main__": 
    main()

