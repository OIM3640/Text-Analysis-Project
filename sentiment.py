import os
""" Used to make sure I had the Correct Directory, used google an AI to understand the os package,
and how to properly switch the directory my file was in"""
def Testing_Code():
    print("Running script...")
    print("Current directory:", os.getcwd())
    os.chdir(r"C:\Users\drodriguez1\Documents\GitHub\Text-Analysis-Project")
    print("Changed directory to:", os.getcwd())

def Pos_or_Neg(folder: str):
    """Load positive and negative word lists from a folder."""
    pos_words = set() # Creates a blank positive word set
    neg_words = set() # Creates a blank negative word set

    if not os.path.isdir(folder): # Checks if my (Text_Words) folder exist
        print(f"[!] Folder '{folder}' not found.")
        return pos_words, neg_words

    for i in os.listdir(folder): # For each file in my folder(text) goes through and reads them
        if i.lower().endswith(".txt"): # Converts file names into lowercase (Removing the case errors around capitalization)
            path = os.path.join(folder, i) # Creates a valid path to each txt (Easier Access to the file)
            try: # Reads files expecting utf-8 format 
                with open(path, "r", encoding="utf-8") as f: 
                    words = set(f.read().split()) # reads the text, splits it into a list, and lastly stores as a set of unique words
            except UnicodeDecodeError: # allows the opportunity to skip the first error and try to read in a different encoding
                with open(path, "r", encoding="latin-1") as f:
                    words = set(f.read().split())

            if "pos" in i.lower(): # Checks what file it came from
                pos_words.update(words) # will place the words into the blank positive set 
            elif "neg" in i.lower():
                neg_words.update(words)

    print(f"Loaded {len(pos_words)} positive and {len(neg_words)} negative words.")
    return pos_words, neg_words # Returns 2 sets that can be used in the future


def sentiment_score(text: str, pos_set, neg_set) -> float:
    """Simple sentiment score between -1 and +1."""
    words = text.split()
    pos = 0
    neg = 0
    for w in words:
        if w in pos_set:
            pos += 1
    for w in words:
        if w in neg_set: 
            neg+= 1    
    total = pos + neg
    if total == 0:
        return 0.0
    return (pos - neg) / total
