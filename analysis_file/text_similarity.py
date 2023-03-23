from fuzzywuzzy import fuzz
import urllib.request



def compare_texts(url1, url2):
    with urllib.request.urlopen(url1) as f:
        text1 = f.read().decode('utf-8')
    with urllib.request.urlopen(url2) as g:
        text2 = g.read().decode('utf-8')
        
    similarity_score = fuzz.ratio(text1, text2)
    print("Text similarity score:", similarity_score)
    
    words1 = set(text1.split())
    words2 = set(text2.split())
    
    similarity_scores = [(w, fuzz.token_set_ratio(w, words2)) for w in words1]
    most_similar = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[:10]
    
    print("Top 10 most similar words:")
    for word, score in most_similar:
        print(f"{word}: {score}")

# Example usage:
url1 = 'https://www.gutenberg.org/cache/epub/174/pg174.txt' 
url2 = 'https://www.gutenberg.org/cache/epub/50210/pg50210.txt' 

compare_texts(url1, url2)
