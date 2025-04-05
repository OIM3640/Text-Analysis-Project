import urllib.request
from thefuzz import fuzz

def fetch_text(url):
    """Fetches text from the given URL using urllib."""
    try:
        with urllib.request.urlopen(url) as f:
            return f.read().decode('utf-8')
    except Exception as e:
        print("An error occurred:", e)
        return ""

def compute_text_similarity(text1, text2):
    """Computes similarity between two texts using Levenshtein distance."""
    text1 = text1.lower().strip()
    text2 = text2.lower().strip()
    return fuzz.ratio(text1, text2)

def main():
    url1 = "https://www.gutenberg.org/cache/epub/11/pg11.txt" # Alice in Wonderland
    url2 = "https://www.gutenberg.org/cache/epub/730/pg730.txt" # Oliver Twist

    text1 = fetch_text(url1)
    text2 = fetch_text(url2)

    if not text1:
        print ("Error: Could not fetch 'Alice's Adventures in Wonderland'.")
        return
    if not text2:
        print("Error: Could not fetch 'Oliver Twist'.")
        return
    
    similarity_score = compute_text_similarity(text1, text2)
    
    print("\nText Similarity:")
    print(f"Similarity between 'Alice's Adventures in Wonderland' and 'Oliver Twist': {similarity_score}%")

if __name__== "__main__":
    main()


# Suggestion from ChatGPT for final version:

# Prompt: "I just finished my Python assingment, can you help me go through every file and
# make any suggestions for improvement in terms of overall functionality, organization, and style?"

# ✍️ Text cleanup	Maybe lowercase + strip spaces before comparing	Minor boost to accuracy (because raw downloads can have weird whitespace)