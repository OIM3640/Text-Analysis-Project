from collections import Counter
from nltk.corpus import stopwords  
from thefuzz import fuzz
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
import numpy as np
from utilities import clean_text,download_book

def compute_similarity_matrix(texts):
    """
    Computes a similarity matrix for a list of cleaned text strings using fuzz.ratio for pairwise comparison.
    
    Args:
        texts (list): A list of cleaned text strings.
        
    Returns:
        np.array: A similarity matrix (2D numpy array) where each entry [i, j] represents the similarity score
                  between text i and text j.
    """
    num_texts = len(texts)
    similarity_matrix = np.zeros((num_texts, num_texts))
    
    for i in range(num_texts):
        for j in range(num_texts):
            if i == j:
                similarity_matrix[i, j] = 100  # Perfect similarity with itself
            else:
                similarity_matrix[i, j] = fuzz.ratio(texts[i], texts[j])
    
    return similarity_matrix

def mds_visualization(similarity_matrix, labels):
    """
    Performs metric MDS on the similarity matrix and plots the results in 2D space.
    
    Args:
        similarity_matrix (np.array): The similarity matrix.
        labels (list): A list of labels for each text, used in plotting.
    """
    mds = MDS(n_components=2, dissimilarity='precomputed', random_state=42)
    distances = 100 - similarity_matrix  # Convert similarity to dissimilarity
    coords = mds.fit_transform(distances)
    
    plt.figure(figsize=(10, 8))
    plt.scatter(coords[:, 0], coords[:, 1], c='blue', marker='o')
    
    for i, label in enumerate(labels):
        plt.text(coords[i, 0], coords[i, 1], label, fontsize=12)
    
    plt.title("Metric MDS of Text Similarities")
    plt.xlabel("MDS Dimension 1")
    plt.ylabel("MDS Dimension 2")
    plt.show()

def compare_fitz_shakespeare():
    # URLs of texts to analyze
    texts_urls = {
        "The Great Gatsby": 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt',
        "Paradise Lost": 'https://www.gutenberg.org/cache/epub/805/pg805.txt',
        "Hamlet": 'https://www.gutenberg.org/files/1524/1524-0.txt',
        "Macbeth": 'https://www.gutenberg.org/files/1533/1533-0.txt'
    }
    
    cleaned_texts = []
    labels = []

    for title, url in texts_urls.items():
        file_name = f"{title.replace(' ', '_').lower()}_text.pkl"
        text = download_book(url, file_name)
        cleaned_text = clean_text(text)
        cleaned_texts.append(cleaned_text)
        labels.append(title)
    
    # Compute similarity matrix
    similarity_matrix = compute_similarity_matrix(cleaned_texts)
    
    # Perform MDS and visualize
    mds_visualization(similarity_matrix, labels)


