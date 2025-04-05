import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
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
    return fuzz.ratio(text1, text2) / 100.0

def main():
    urls = {
        "Alice's Adventures in Wonderland": "https://www.gutenberg.org/files/11/11-0.txt",
        "Oliver Twist": "https://www.gutenberg.org/files/730/730-0.txt"
    }

    texts = []
    labels = []

    for label, url in urls.items():
        text = fetch_text(url)
        if text:
            texts.append(text)
            labels.append(label)

    if len(texts) < 2:
        print("Not all texts were fetched successfully")
        return
    
    num_texts = len(texts)
    similarities = np.zeros((num_texts, num_texts))

    for i in range(num_texts):
        for j in range(i, num_texts):
            similarity = compute_text_similarity(texts[i], texts[j])
            similarities[i, j] = similarity
            similarities[j, i] = similarity

    dissimilarities = 1 - similarities

    mds = MDS(dissimilarity='precomputed', random_state=42)
    coordinates = mds.fit_transform(dissimilarities)

    plt.figure(figsize=(8,6))
    plt.scatter(coordinates[:, 0], coordinates[:, 1])

    for i in range(coordinates.shape[0]):
        plt.annotate(f'Text {i+1}', (coordinates[i, 0], coordinates[i, 1]))

    plt.title('Text Clustering using MDS')
    plt.xlabel('MDS Dimension 1')
    plt.ylabel('MDS Dimension 2')
    plt.show()

if __name__ == "__main__":
    main()

# Suggestion from ChatGPT for final version:

# Prompt: "I just finished my Python assingment, can you help me go through every file and
# make any suggestions for improvement in terms of overall functionality, organization, and style?"

# Issue	What to fix	Why
#⚡ Error handling	Should check if text1 and text2 actually loaded successfully before proceeding	
# 🎯 Label texts better	Instead of "Text 1", "Text 2" ➔ Label them as "Alice" and "Oliver Twist" for clarity	
# 📈 (Optional) Plot aesthetics	Slightly improve the plot — bigger font size, grid lines, etc.	Just for a more polished final look