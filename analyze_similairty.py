import os
from utils import clean_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_all_reviews(folder='reviews'):
    all_texts = []
    movie_names = []

    for file in sorted(os.listdir(folder)):
        if file.endswith('.txt'):
            with open(os.path.join(folder, file), 'r', encoding='utf-8') as f:
                text = f.read()
                cleaned = clean_text(text)
                all_texts.append(cleaned)
                movie_names.append(file.replace('.txt', '').replace('_', ' ').title())
    
    return all_texts, movie_names

def compare_reviews(texts, movie_names):
    # Turn all text into TF-IDF word vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)

    # Compute similarity between each pair
    similarity_matrix = cosine_similarity(tfidf_matrix)

    print("\nMovie Review Similarity Scores (0 = not similar, 1 = very similar):\n")
    for i in range(len(movie_names)):
        for j in range(i + 1, len(movie_names)):
            movie_1 = movie_names[i]
            movie_2 = movie_names[j]
            score = similarity_matrix[i][j]
            print(f"{movie_1} ↔ {movie_2}: {score:.2f}")

def main():
    texts, names = load_all_reviews()
    compare_reviews(texts, names)

if __name__ == "__main__":
    main()
