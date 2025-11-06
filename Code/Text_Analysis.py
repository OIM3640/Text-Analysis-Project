#This code is a text anlysis of 2017-2018 James Harden Wikipedia Article and also the 2018 Western Conference Finals.

#Counter is recommended by chatgpt for word counting
from collections import Counter
from math import sqrt
import json, os

#This explains which WCF it is and the JSONL and the Season
JSONL = "harden_2018_season_vs_playoff.jsonl"
SEASON = "2017–18 Houston Rockets season"
WCF    = "2018 Western Conference Finals"

# This is a stop list provided by chatgpt to remove common words from analysis
STOP = {
    "the","and","a","an","of","for","to","in","on","at","as","by","from","with","it",
    "its","is","are","was","were","be","been","being","that","this","these","those",
    "or","not","no","but","so","if","into","than","then","their","his","her","they",
    "them","he","she","we","you","your","our","i","over","after","before","during",
    "within","without","between","about","also","such","there","here","up","down"
}

#Loads JSON lines from a file and returns a dictionary of titles and their corresponding content
#Using UTF-8 to read special characters from the documents
def load_jsonl(path=JSONL):
    docs = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            title = obj.get("title", "").strip()
            if title:
                docs[title] = obj.get("content", "")
    return docs

# The following are very basic NPL functions for tokenization, which creates a list of words
def tokens(text):
    out = []
    for w in text.split():
        #This code here will strip punctuation and also convert the words to lowercase
        w = w.strip(".,!?;:\"()[]{}<>''``“”’").lower()
        #This code will filter out stop words and single character words
        if w and w not in STOP and len(w) > 1:
            out.append(w)
    return out


#This will build a bag of words from a string of text
def bow(text):
    return Counter(tokens(text))

#This function will return the top 15 most common words
def top_n(c, n=15):
    return c.most_common(n)

#Suggested by Chatgpt, this function will find words that are frequent in one document but not in another
#Words in A but not freqeuent in B
#Return will be a list of tuples (word, count)
def unique_freq(a, b, thr=5):
    items = [(w, ca) for w, ca in a.items() if ca >= thr and b.get(w, 0) < thr]
    items.sort(key=lambda x: x[1], reverse=True)
    return items

#Suggested by Chatgpt
#Compute dot(a, b) / (||a|| * ||b||)
#dot(a, b) = sum over shared words of a[w] * b[w]
#  ||a||     = sqrt( sum of (a[w]^2) for all w in a )
#  ||b||     = likewise for b
def cosine(a, b):
    if not a or not b: return 0.0
    dot = sum(a[w]*b.get(w,0) for w in a)
    na  = sqrt(sum(v*v for v in a.values()))
    nb  = sqrt(sum(v*v for v in b.values()))
    return 0.0 if na==0 or nb==0 else dot/(na*nb)

def proper_names(text, k=15):
    c = Counter()
    for w in text.split():
        w = w.strip(".,!?;:\"()[]{}<>''``“”’")
        if w.istitle() and len(w) >= 3:
            c[w] += 1
    return c.most_common(k)

def bar(x, scale=20):
    return "█" * int(round(x*scale))


# This part will be the main anaylsis 
# 1. Build bag of words for each document 
# 2. Print two words from each document 
# 3. Print words that are freqeunt in Season but not in the WCF

def analyze(docs):
    bows = {t: bow(txt) for t, txt in docs.items()}

    print("\n=== Top Words per Document ===")
    for t, c in bows.items():
        print(f"\n{t}")
        for w, n in top_n(c, 15):
            print(f"  {w:<18} {n}")

    if SEASON in bows and WCF in bows:
        print("\n=== Frequent in SEASON but not WCF (thr=5) ===")
        for w, n in unique_freq(bows[SEASON], bows[WCF], 5)[:20]:
            print(f"  {w:<18} {n}")

        print("\n=== Frequent in WCF but not SEASON (thr=5) ===")
        for w, n in unique_freq(bows[WCF], bows[SEASON], 5)[:20]:
            print(f"  {w:<18} {n}")

    print("\n=== Cosine Similarity ===")
    pairs = [("James Harden", SEASON), ("James Harden", WCF), (SEASON, WCF)]
    for a, b in pairs:
        if a in bows and b in bows:
            s = cosine(bows[a], bows[b])
            print(f"  {a} ↔ {b}\n    {s:.3f} {bar(s)}")

    print("\n=== Proper Names (top 15) ===")
    for t, txt in docs.items():
        print(f"\n{t}")
        for name, n in proper_names(txt, 15):
            print(f"  {name:<18} {n}")

# ---------- run directly ----------
def main():
    if not os.path.exists(JSONL):
        print("[error] JSONL not found. Run Part 1 first.")
        return
    docs = load_jsonl(JSONL)
    if not docs:
        print("[error] Loaded 0 documents.")
        return
    analyze(docs)

if __name__ == "__main__":
    main()
