# part 3 exploration with AI, this part i use chatgpt to help me learn new approach sentiment text analysis


import unicodedata
import re


def read_data(filename): 
    """Read all lines from a text file"""
    with open(filename, "r", encoding="utf-8") as file: #r是只读file，
        data = file.readlines()
        print("Number of lines:", len(data))
        print("Type:", type(data))
        print("\nFirst 5 lines preview:\n", data[:5])
    return data

def clean_text(lines): 
    """"Cleaning part: clean the text by removing punctuation, symbols, and special characters.
    It keeps only letters and spaces, makes all letters lowercase, 
    and removes any empty lines. This helps prepare the text for analysis. """
    clean = []
    for line in lines: 
        new_line = ""
        for character in line: 
            if unicodedata.category(character).startswith('C'):
                # if character is c, meaning its controled character 
                continue
            if character.isalpha() or character.isspace(): 
                new_line += character.lower()
                # if character is character, add it lowercase to new line
            else: 
                new_line += ' '
                "if character is puncation, replace with space"
        new_line = new_line.strip()   
        if new_line != "":            #with help in gpt  checks if the cleaned line is not empty before appending.
            clean.append(new_line)
    
    text = ""
    for line in clean:
        text += line + " "
    return text


# Sentiment helpers (Think Python style) ####with help from chatgpt
SENT_LEX = {
    "love": 3, "loved": 3, "lovely": 3, "like": 2, "happy": 3, "joy": 3, "delight": 3,
    "good": 2, "great": 3, "excellent": 4, "fortunate": 2, "kind": 2, "brave": 2,
    "bad": -2, "worse": -3, "worst": -4, "hate": -3, "hated": -3, "angry": -3,
    "sad": -2, "cry": -2, "cried": -2, "fear": -2, "terrible": -3, "horrible": -3,
    "dead": -2, "death": -2, "poor": -2, "ugly": -2, "evil": -3, "wicked": -3
}  #define sentiment metrics

NEGATIONS = {"not","no","never","none","hardly","barely","scarcely"}

def split_sentences(text):
    """Very simple rule-based splitter using punctuation boundaries."""
    # Think Python approach: simple regex and list filtering
    sents = re.split(r'[.!?]+\s*', text.strip())  # “Split the text at any sequence of whitespace that follows a sentence-ending punctuation mark.
    result = [s.strip() for s in sents if s.strip() != ""]
    return result

def tokenize_words(text):
    """Lowercase alphabetic tokens only, returns a list of words."""
    return re.findall(r"[a-z]+", text.lower())

def sentiment_score(tokens, lexicon, negations, window=3):
    """
    Sum lexicon scores; if a negation appears, flip the sign of the
    next few scored tokens (simple window-based negation).
    """
    score = 0
    flip = 0
    for t in tokens:
        if t in negations:
            flip = window
            continue
        s = lexicon.get(t, 0)
        if flip > 0 and s != 0:
            s = -s
        score += s
        if flip > 0:
            flip -= 1
    return score

def rolling_mean(values, k):
    """
    Smooth the sequence with a simple moving average of window k.
    No numpy: just accumulate in a list (Think Python style).
    """
    out = []
    window_sum = 0.0
    q = []
    for v in values:
        q.append(v)
        window_sum += v
        if len(q) > k:
            window_sum -= q.pop(0)
        out.append(window_sum / len(q))
    return out


def main(): 
    filename = "jane_eyre.txt"
    lines = read_data(filename)

    # keep a raw version (with punctuation) for sentence splitting
    raw_text = "".join(lines)

    cleaned = clean_text(lines)

    print("\n=== Clean Text Check ===")
    print("Length of cleaned text:", len(cleaned))
    print("First 3000 characters:\n", cleaned[:3000])
    ### with chatgpt's help, used to check if the cleaned text looks correct.

    # --- Sentiment Analysis (Think Python style) ---
    lexicon = dict(SENT_LEX)  # copy so you can extend safely

    # split sentences from the raw text (still has . ! ?)
    sentences = split_sentences(raw_text)

    # score each sentence
    sent_scores = []
    for s in sentences:
        toks = tokenize_words(s)
        sent_scores.append( sentiment_score(toks, lexicon, NEGATIONS, window=3) )

    # overall/average
    total_sent = sum(sent_scores)
    avg_sent = total_sent / max(1, len(sentences))
    print(f"\n[Sentiment] Total score = {total_sent:.2f}, Average per sentence = {avg_sent:.3f}")

    # top positive/negative sentences (like Think Python’s “most frequent words” pattern)
    # build a list of (score, sentence), then sort
    scored_pairs = []
    i = 0
    while i < len(sentences):
        scored_pairs.append( (sent_scores[i], sentences[i]) )
        i += 1
    scored_pairs.sort(key=lambda p: p[0], reverse=True)
    print("\n[Sentiment] Top 5 positive sentences:")
    j = 0
    while j < 5 and j < len(scored_pairs):
        sc, s = scored_pairs[j]
        print(f"  (+{sc:.1f}) {s[:180]}")
        j += 1

    scored_pairs.sort(key=lambda p: p[0])  # ascending for negative
    print("\n[Sentiment] Top 5 negative sentences:")
    j = 0
    while j < 5 and j < len(scored_pairs):
        sc, s = scored_pairs[j]
        print(f"  ({sc:.1f}) {s[:180]}")
        j += 1

    # rolling trend (window=50 sentences)
    trend = rolling_mean(sent_scores, k=50)
    print("\n[Sentiment] First 20 values of rolling mean (k=50):")
    preview = []
    t = 0
    while t < 20 and t < len(trend):
        preview.append(round(trend[t], 3))
        t += 1
    print(preview)


if __name__ == "__main__":
    main()


# --- AI Assistance Acknowledgment ---
# Parts of this code (sentiment analysis and tokenization explanations)
# were developed with the help of ChatGPT (OpenAI, 2025).
# ChatGPT conversation link:
# https://chatgpt.com/share/690e2452-6088-8013-81c5-a30cefefaab2

