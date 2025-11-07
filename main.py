from fetch import fetch_articles
from mediawiki import MediaWiki
from clean import clean_then_strip_punct_and_lower, remove_stopwords
from tfidf import compute_tf, compute_idf, compute_tfidf
from visualize import plot_top_keywords, generate_wordcloud
from collections import Counter
from visualize import plot_top_keywords, generate_wordcloud
import os

def compute_word_frequency(tokens):
    """Count raw word frequencies for a document."""
    return Counter(tokens)

def main():
    topics = [ "Apple Inc.", "Microsoft", "Samsung Electronics"]
    articles = fetch_articles(topics)

    cleaned_docs = {}

    # Step 1: Clean & preprocess
    for title, content in articles.items():
        tokens = clean_then_strip_punct_and_lower(content)
        tokens_no_stop = remove_stopwords(tokens)
        cleaned_docs[title] = tokens_no_stop

    # Step 2a: Word frequency (raw counts) BEFORE TF-IDF
    for title, tokens in cleaned_docs.items():
        word_freq = compute_word_frequency(tokens)     # Counter
        top_words = word_freq.most_common(10)
        print(f"\n--- {title}: Top 10 Frequent Words ---")
        for word, freq in top_words:
            print(f"{word:<15} {freq}")

    # Step 2b: Compute IDF across all documents
    idf = compute_idf(cleaned_docs.values())

    outdir = "figures"
    os.makedirs(outdir, exist_ok=True)

    # Step 3: Compute TF-IDF for each document
    for title, tokens in cleaned_docs.items():
        tfidf_scores = compute_tfidf(tokens, idf)

        # get top 10 keywords by TF-IDF score
        top_keywords = sorted(tfidf_scores.items(), key=lambda x: x[1], reverse=True)[:10]

        print(f"{title}: TF-IDF terms count =", len(tfidf_scores))
        print(f"\n--- {title} ---")
        
        for word, score in top_keywords:
            print(f"{word:<20} {score:.4f}")
        print("-" * 60)

            # Visualize
        plot_top_keywords(
            tfidf_scores, title, n=10,
            save_path=f"{outdir}/{title.replace(' ', '_')}_top10.png"
        )
        generate_wordcloud(
            tfidf_scores, title,
            save_path=f"{outdir}/{title.replace(' ', '_')}_wordcloud.png"
        )

if __name__ == "__main__":
    main()