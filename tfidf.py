import math
from collections import Counter, defaultdict

def compute_tf(tokens): # AI/Chat helped me perform the calculations for TF and IDF, which was taught to me in my machine learning class
    """Compute term frequency for one document."""
    tf = Counter(tokens)
    total = sum(tf.values())    
    return {term: freq / total for term, freq in tf.items()}

def compute_idf(all_docs):
    """Compute inverse document frequency from multiple docs."""
    N = len(all_docs)
    idf = defaultdict(int)

    # count in how many docs each term appears
    for doc in all_docs:
        for term in set(doc):
            idf[term] += 1

    # compute IDF
    return {term: math.log((N + 1) / (df + 1)) + 1 for term, df in idf.items()}

def compute_tfidf(tokens, idf):
    """Compute TF-IDF for one document given its IDF dictionary."""
    tf = compute_tf(tokens)
    return {term: tf_val * idf.get(term, 0) for term, tf_val in tf.items()}
