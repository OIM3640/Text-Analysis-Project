import os
def Testing_Code():
    print("Running script...")
    print("Current directory:", os.getcwd())
    os.chdir(r"C:\Users\drodriguez1\Documents\GitHub\Text-Analysis-Project")
    print("Changed directory to:", os.getcwd())

def Pos_or_Neg(folder: str):
    """Load positive and negative word lists from a folder."""
    pos_words = set()
    neg_words = set()

    if not os.path.isdir(folder):
        print(f"[!] Folder '{folder}' not found.")
        return pos_words, neg_words

    for fn in os.listdir(folder):
        if fn.lower().endswith(".txt"):
            path = os.path.join(folder, fn)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    words = set(f.read().split())
            except UnicodeDecodeError:
                with open(path, "r", encoding="latin-1") as f:
                    words = set(f.read().split())

            if "pos" in fn.lower():
                pos_words.update(words)
            elif "neg" in fn.lower():
                neg_words.update(words)

    print(f"Loaded {len(pos_words)} positive and {len(neg_words)} negative words.")
    return pos_words, neg_words


def sentiment_score(text: str, pos_set, neg_set) -> float:
    """Simple sentiment score between -1 and +1."""
    words = text.split()
    pos = sum(1 for w in words if w in pos_set)
    neg = sum(1 for w in words if w in neg_set)
    total = pos + neg
    if total == 0:
        return 0.0
    return (pos - neg) / total