"""Main entry point for election news analysis.

This script orchestrates the complete analysis pipeline:
1. Fetches recent election news using NewsDataHarvester
2. Processes articles using NewsDataProcessor
3. Performs comprehensive text analysis using TextAnalyzer
4. Generates visualizations and statistics including:
   - Word frequencies and word cloud
   - Topic modeling and clustering
   - Sentiment analysis
   - N-gram analysis
   - Summary statistics
5. Saves results to analysis_output directory
6. Provides detailed console output of findings

The analysis focuses on the 2024 US Presidential Election coverage,
processing 50 successfully downloaded articles in this example.
"""

import os
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from data_harvesting import NewsDataHarvester
from data_processing import NewsDataProcessor
from text_analysis import TextAnalyzer


def fetch_election_news(harvester: NewsDataHarvester, days_back: int = 3) -> dict:
    """Fetch recent election-related news articles.

    Args:
        harvester: Initialized NewsDataHarvester instance
        days_back: Number of days to look back for articles (default: 3)

    Returns:
        Dictionary containing the API response with articles
    """
    # Calculate date range
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days_back)

    # Format dates as YYYY-MM-DD
    from_date = start_date.strftime("%Y-%m-%d")
    to_date = end_date.strftime("%Y-%m-%d")

    # Fetch articles about the election using /v2/everything endpoint
    articles = harvester.get_all_articles(
        query="election",
        from_date=from_date,
        to_date=to_date,
        language="en",
        sort_by="popularity",
        page=1,
    )

    # Debug print to check the response
    print(f"\nFound {articles.get('totalResults', 0)} articles")
    if not articles.get("articles"):
        print("No articles returned from the API")
        print("API Response:", articles)

    return articles


def prepare_texts(
    articles: dict, 
    processor: NewsDataProcessor,
    save_path: str = "data/processed/articles.json"
) -> list:
    """Extract and prepare article texts for analysis."""
    # Convert to DataFrame for easier handling
    df = processor.articles_to_dataframe(articles, save_path=save_path)
    
    # Print number of articles before and after filtering
    total_articles = len(articles.get("articles", []))
    valid_articles = len(df)
    print(f"\nTotal articles: {total_articles}")
    print(f"Valid articles after filtering: {valid_articles}")

    # Get text content with stop words removed
    texts = processor.get_text_content(articles, remove_stopwords=True)

    # Print statistics about content sources
    full_text_count = sum(1 for row in df.itertuples() 
                         if hasattr(row, 'full_text') and row.full_text)
    print(f"\nArticles with full text content: {full_text_count}")
    print(f"Articles using fallback content: {len(texts) - full_text_count}")

    return texts


def analyze_election_coverage(texts: list, analyzer: TextAnalyzer) -> None:
    """Perform comprehensive analysis of election news texts."""
    # Create output directory for plots
    output_dir = Path("analysis_output")
    output_dir.mkdir(exist_ok=True)

    # 1. Word Frequencies and Word Cloud
    print("\nTop words across all articles:")
    all_text = " ".join(texts)
    top_words = analyzer.get_word_frequencies(all_text, top_n=15)
    print("\nMost frequent words:")
    for word, freq in top_words.items():
        print(f"{word}: {freq}")

    # Generate and save word cloud
    _, wordcloud_fig = analyzer.generate_wordcloud(all_text)
    wordcloud_fig.savefig(
        output_dir / "wordcloud.png",
        dpi=300,
        bbox_inches='tight',
        pad_inches=0
    )

    # 2. TF-IDF Analysis
    tfidf_df = analyzer.compute_tfidf(texts)
    print("\nTop TF-IDF terms for each article:")
    for i, text in enumerate(texts, 1):
        top_terms = tfidf_df.iloc[i - 1].nlargest(5)
        print(f"\nArticle {i} top terms:")
        print(top_terms)

    # 3. Summary Statistics (including n-grams)
    stats = analyzer.get_summary_statistics(texts)
    print("\nSummary Statistics:")
    print(f"Number of articles: {stats['num_documents']}")
    print(f"Average article length: {stats['avg_length']:.2f} words")
    print(f"Total unique words: {stats['total_unique_words']}")
    print("\nMost common words across all articles:")
    for word, count in stats["common_words"]:
        print(f"{word}: {count}")

    # Generate and save summary statistics visualization
    stats_fig = analyzer.plot_summary_statistics(stats)
    stats_fig.savefig(
        output_dir / "summary_statistics.png",
        dpi=300,
        bbox_inches='tight'
    )

    # 4. Sentiment Analysis
    sentiments = analyzer.analyze_sentiment(texts)
    sentiment_fig = analyzer.plot_sentiment_distribution(sentiments)
    sentiment_fig.savefig(output_dir / "sentiment_distribution.png")

    print("\nSentiment Analysis Summary:")
    avg_polarity = sum(s["polarity"] for s in sentiments) / len(sentiments)
    avg_subjectivity = sum(s["subjectivity"] for s in sentiments) / len(sentiments)
    print(f"Average Polarity: {avg_polarity:.2f}")
    print(f"Average Subjectivity: {avg_subjectivity:.2f}")

    # 5. Text Clustering
    labels = [f"Article {i+1}" for i in range(len(texts))]
    coords, cluster_fig = analyzer.cluster_texts(texts, labels)
    cluster_fig.savefig(output_dir / "text_clusters.png")

    # 6. Text Similarity
    similarity_matrix = analyzer.compute_similarity_matrix(texts)
    print("\nText Similarity Matrix:")
    print(similarity_matrix)

    # 7. Topic Modeling
    print("\nPerforming topic modeling...")
    topics, topic_fig = analyzer.perform_topic_modeling(texts)
    
    # Print topics
    print("\nDiscovered Topics:")
    for topic_name, topic_info in topics.items():
        print(f"\n{topic_name}:")
        for word, weight in topic_info['words']:
            print(f"  {word}: {weight:.4f}")
        print(f"  Documents: {topic_info['dominant_docs']}")
        print(f"  Importance: {topic_info['importance']:.1%}")
    
    # Save topic visualization
    topic_fig.savefig(
        output_dir / "topic_model.png",
        dpi=300,
        bbox_inches='tight'
    )

    print("\nTopic model visualizations saved:")
    print("- Static visualization: analysis_output/topic_model.png")
    print("- Interactive visualization: analysis_output/topic_model_vis.html")

    plt.close("all")


def main():
    """Main function to orchestrate the election news analysis."""
    print("Starting Election News Analysis...")

    # Initialize our modules
    harvester = NewsDataHarvester()
    processor = NewsDataProcessor()
    analyzer = TextAnalyzer()

    # Fetch the news
    print("Fetching election news articles...")
    articles = fetch_election_news(harvester)

    # Prepare texts for analysis
    print("Preparing texts for analysis...")
    texts = prepare_texts(articles, processor)

    # Perform analysis
    print("Analyzing election coverage...")
    analyze_election_coverage(texts, analyzer)

    print(
        "\nAnalysis complete! Check the 'analysis_output' directory for visualizations."
    )


if __name__ == "__main__":
    main()
