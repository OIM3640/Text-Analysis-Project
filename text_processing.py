# yfiance API (to obtain live market Data
import os
import re
from collections import Counter
from math import floor
def Testing_Code():
    print("Running script...")
    print("Current directory:", os.getcwd())
    os.chdir(r"C:\Users\drodriguez1\Documents\GitHub\Text-Analysis-Project")
    print("Changed directory to:", os.getcwd())

#def api_access(api_key: str):

    #url = [('https://newsapi.org/v2/everything?q=NFL&sortBy=popularity&apiKey=fd772e4022f1491994dc98392a019790')]
    #response = requests.get(url)
    #print(response)
import os

def read_gutenberg(path: str, skip_header: bool = True, encoding_primary="utf-8", encoding_fallback="latin-1") -> str:
    """
    Read a Project Gutenberg .txt file, optionally skipping the boilerplate
    header and footer. Returns the file's main content as a single string.
    """
    def read_with_encoding(enc: str) -> str:
        lines = []
        with open(path, "r", encoding=enc, errors="strict") as f:
            # --- Skip the header (until we hit the START marker) ---
            if skip_header:
                for line in f:
                    up = line.upper()
                    if up.startswith("*** START OF") or "START OF THE PROJECT" in up:
                        break
            # --- Read main content; stop at END marker if skipping header ---
            for line in f:
                up = line.upper()
                if skip_header and (up.startswith("*** END OF") or "END OF THE PROJECT" in up):
                    break
                lines.append(line)
        return "".join(lines)

    # Try primary encoding, then fallback if needed
    try:
        return read_with_encoding(encoding_primary)
    except UnicodeDecodeError:
        return read_with_encoding(encoding_fallback)

def Load_Txt(folder: str, skip_header: bool = True):
    """
    Load all .txt files in a folder.
    Returns: list of (filename, text) with Gutenberg boilerplate removed if requested.
    """
    out = []
    if not os.path.isdir(folder):
        print(f"[!] Folder '{folder}' not found.")
        return out

    for fn in os.listdir(folder):
        if fn.lower().endswith(".txt"):
            path = os.path.join(folder, fn)
            try:
                text = read_gutenberg(path, skip_header=skip_header, encoding_primary="utf-8", encoding_fallback="latin-1")
                out.append((fn, text))
            except Exception as e:
                print(f"[!] Could not read '{fn}': {e}")

    print(f"You have loaded {len(out)} Text files into the Processor")
    return out


def clean_and_filter(text: str) -> str:
    """Lowercase, keep only letters, and remove stopwords/pronouns."""
    Filter_Words = {# --- Stopwords ---
    'the','and','a','to','of','in','is','it','for','on','was','as','at',
    'with','be','by','an','are','were','from','this','which',

    # --- Pronouns ---
    'i','you','he','she','it','we','they','me','him','her','us','them',
    'my','your','his','its','our','their','mine','yours','hers','ours','theirs',
    'myself','yourself','himself','herself','itself','ourselves','yourselves','themselves',
    'this','that','these','those',
    'who','whom','whose','which','what',
    'all','another','any','anybody','anyone','anything','both','each','either',
    'everybody','everyone','everything','few','many','most','neither','nobody',
    'none','no','one','no one','other','others','several','some','somebody',
    'someone','something','such'}
    text = text.lower()
    cleaned = ""
    filtered= []
    for i in text:
        if i.isalpha() or i.isspace():
            cleaned += i
    words = cleaned.split()
    for i in words:
        if i not in Filter_Words:
            filtered.append(i)
    return " ".join(filtered)

def count_words(text: str) -> dict:
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts 

def summary_stats(text: str) -> dict:
    words = text.split()
    unique = set(words)
    total= 0
    for i in words:
        total+= len(i)
    Longest_lenght = max
    avg_word_len = total / max(len(words), 1) # 
    print("This is an overview of the files!")
    return{"words": len(words),
        "unique_words": len(unique),
        "type_token_ratio": len(unique)/max(len(words),1),
        "avg_word_len": avg_word_len,}       

def main():
    folder = "text"
    files = Load_Txt(folder)
    if not files:
        return

    all_counts = {}

    for name, text in files:
        cleaned = clean_and_filter(text)
        counts = count_words(cleaned)

        print(f"\nTop words in {name}:")
        top = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]
        for w, c in top:
            print(f"  {w:<12} {c}")

        # combine into overall counts
        for w, c in counts.items():
            all_counts[w] = all_counts.get(w, 0) + c

    print("\nOverall most common words:")
    top_all = sorted(all_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    for w, c in top_all:
        print(f"  {w:<12} {c}")
    stats = summary_stats(cleaned)
    print(f"  words={stats['words']}  unique={stats['unique_words']}  Avg Word Length={stats['avg_word_len']:.3f}")

if __name__ == "__main__":
    main()
