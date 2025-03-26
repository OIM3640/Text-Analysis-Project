"""Module for analyzing news article text data.

This module provides comprehensive text analysis functionality including:
1. Word Frequency Analysis
   - Word frequencies with stop word removal
   - TF-IDF scoring
   - Election-themed word cloud generation

2. N-gram Analysis
   - Bigram and trigram extraction
   - Phrase frequency analysis

3. Topic Modeling
   - Latent Dirichlet Allocation (LDA)
   - Topic importance visualization
   - Interactive topic exploration

4. Sentiment Analysis
   - Polarity and subjectivity scoring
   - Sentiment distribution visualization

5. Text Similarity
   - Pairwise similarity computation
   - Text clustering using MDS
   - Cluster visualization

6. Statistical Analysis
   - Document statistics
   - Word frequencies
   - Common phrases
   - Comprehensive visualizations
"""

import numpy as np
import pandas as pd
from collections import Counter
from pathlib import Path
from typing import Dict, List, Tuple, Union

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.manifold import MDS
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from nltk import ngrams
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
import pyLDAvis


class TextAnalyzer:
    """Class to handle text analysis operations."""

    def __init__(self):
        """Initialize the TextAnalyzer with required NLTK data."""
        # Ensure NLTK data is downloaded
        import nltk

        try:
            nltk.data.find("tokenizers/punkt")
        except LookupError:
            nltk.download("punkt")
        try:
            nltk.data.find("corpora/stopwords")
        except LookupError:
            nltk.download("stopwords")
        try:
            nltk.data.find("tokenizers/punkt_tab")
        except LookupError:
            nltk.download("punkt_tab")

        self.stop_words = set(stopwords.words("english"))

    def preprocess_text(self, text: str) -> List[str]:
        """Preprocess text by tokenizing and removing stop words.

        Args:
            text: Raw text string

        Returns:
            List of processed tokens
        """
        # Simple word tokenization using split()
        tokens = text.lower().split()
        # Remove stop words and non-alphabetic tokens
        tokens = [
            token
            for token in tokens
            if token not in self.stop_words and token.isalpha()
        ]
        return tokens

    def get_word_frequencies(self, text: str, top_n: int = None) -> Dict[str, int]:
        """Calculate word frequencies for a text.

        Args:
            text: Input text
            top_n: Number of top frequencies to return (optional)

        Returns:
            Dictionary of word frequencies
        """
        tokens = self.preprocess_text(text)
        frequencies = Counter(tokens)
        if top_n:
            return dict(frequencies.most_common(top_n))
        return dict(frequencies)

    def compute_tfidf(self, texts: List[str]) -> pd.DataFrame:
        """Compute TF-IDF scores for a collection of texts.

        Args:
            texts: List of text documents

        Returns:
            DataFrame with TF-IDF scores
        """
        vectorizer = TfidfVectorizer(
            preprocessor=lambda x: " ".join(self.preprocess_text(x))
        )
        tfidf_matrix = vectorizer.fit_transform(texts)
        return pd.DataFrame(
            tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out()
        )

    def get_summary_statistics(self, texts: List[str]) -> Dict[str, Union[float, Dict]]:
        """Compute summary statistics for a collection of texts.

        Args:
            texts: List of text documents

        Returns:
            Dictionary containing various summary statistics
        """
        stats = {
            "num_documents": len(texts),
            "avg_length": np.mean([len(text.split()) for text in texts]),
            "total_unique_words": len(
                set(word for text in texts for word in self.preprocess_text(text))
            ),
            "common_words": Counter(
                word for text in texts for word in self.preprocess_text(text)
            ).most_common(10),
            "all_text": texts,  # Add full text for n-gram analysis
        }
        return stats

    def analyze_sentiment(self, texts: List[str]) -> List[Dict]:
        """Perform sentiment analysis on texts using TextBlob.

        Args:
            texts: List of text documents

        Returns:
            List of sentiment analysis results
        """
        sentiments = []
        for text in texts:
            blob = TextBlob(text)
            sentiments.append(
                {
                    "polarity": blob.sentiment.polarity,
                    "subjectivity": blob.sentiment.subjectivity,
                }
            )
        return sentiments

    def compute_similarity_matrix(self, texts: List[str]) -> np.ndarray:
        """Compute pairwise similarity matrix for texts using TF-IDF.

        Args:
            texts: List of text documents

        Returns:
            Numpy array of pairwise similarities
        """
        tfidf = TfidfVectorizer().fit_transform(texts)
        return (tfidf * tfidf.T).toarray()

    def cluster_texts(
        self, texts: List[str], labels: List[str] = None
    ) -> Tuple[np.ndarray, plt.Figure]:
        """Perform text clustering using MDS.

        Args:
            texts: List of text documents
            labels: Optional list of labels for the texts

        Returns:
            Tuple of (coordinates array, matplotlib figure)
        """
        # Compute similarity matrix
        similarities = self.compute_similarity_matrix(texts)

        # Convert to dissimilarity
        dissimilarities = 1 - similarities

        # Apply MDS
        mds = MDS(dissimilarity="precomputed", random_state=42)
        coords = mds.fit_transform(dissimilarities)

        # Create visualization
        fig, ax = plt.subplots(figsize=(10, 8))
        scatter = ax.scatter(coords[:, 0], coords[:, 1])

        if labels:
            for i, label in enumerate(labels):
                ax.annotate(label, (coords[i, 0], coords[i, 1]))

        ax.set_title("Text Clustering Visualization")
        plt.tight_layout()

        return coords, fig

    def plot_sentiment_distribution(self, sentiments: List[Dict]) -> plt.Figure:
        """Create visualization of sentiment distribution.

        Args:
            sentiments: List of sentiment dictionaries

        Returns:
            Matplotlib figure
        """
        df = pd.DataFrame(sentiments)

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(data=df, x="polarity", y="subjectivity", ax=ax)
        ax.set_title("Sentiment Distribution")
        ax.set_xlabel("Polarity (Negative -> Positive)")
        ax.set_ylabel("Subjectivity (Objective -> Subjective)")

        plt.tight_layout()
        return fig

    def generate_wordcloud(
        self, text: str, width: int = 800, height: int = 400
    ) -> Tuple[WordCloud, plt.Figure]:
        """Generate word cloud visualization from text."""
        # Get word frequencies (with stop words already removed)
        frequencies = self.get_word_frequencies(text)

        # Define election color function
        def election_color_func(
            word, font_size, position, orientation, random_state=None, **kwargs
        ):
            """Return red or white color based on position."""
            # Use just red and white with adjusted brightness
            colors = ["#FF3030", "#FFFFFF"]  # Bright red and white

            # Use both x and y position for more varied distribution
            x_pos = position[0] / width
            y_pos = position[1] / height
            position_value = (x_pos + y_pos) / 2

            # Simple 50/50 split for red and white
            return colors[1] if position_value > 0.5 else colors[0]

        # Generate word cloud
        wordcloud = WordCloud(
            width=width,
            height=height,
            background_color="navy",  # Dark blue background
            max_words=100,
            relative_scaling=1.0,  # Scale word size based on frequency
            normalize_plurals=True,
            color_func=election_color_func,
            prefer_horizontal=0.6,  # Allow more vertical words
            min_font_size=8,  # Ensure smaller words are still readable
            max_font_size=80,  # Limit maximum font size
        ).generate_from_frequencies(frequencies)

        # Create figure
        fig, ax = plt.subplots(figsize=(width / 100, height / 100))
        ax.imshow(wordcloud, interpolation="bilinear")
        ax.axis("off")
        plt.tight_layout(pad=0)

        return wordcloud, fig

    def get_ngrams(
        self, text: str, n: int, top_k: int = 15
    ) -> List[Tuple[Tuple[str, ...], int]]:
        """Extract most common n-grams from text.

        Args:
            text: Input text
            n: Length of n-gram (2 for bigrams, 3 for trigrams, etc.)
            top_k: Number of top n-grams to return

        Returns:
            List of tuples (n-gram, frequency)
        """
        # Tokenize and convert to lowercase
        tokens = word_tokenize(text.lower())

        # Remove stop words and non-alphabetic tokens
        tokens = [
            token
            for token in tokens
            if token not in self.stop_words and token.isalpha()
        ]

        # Generate n-grams
        n_grams = list(ngrams(tokens, n))

        # Count frequencies
        freq_dist = Counter(n_grams)

        # Return top k most common
        return freq_dist.most_common(top_k)

    def plot_ngrams(
        self, text: str, n: int, top_k: int = 15, title: str = None
    ) -> plt.Figure:
        """Create bar plot of most common n-grams.

        Args:
            text: Input text
            n: Length of n-gram
            top_k: Number of top n-grams to show
            title: Optional title for the plot

        Returns:
            Matplotlib figure
        """
        # Get n-gram frequencies
        ngram_freq = self.get_ngrams(text, n, top_k)

        # Prepare data for plotting
        phrases = [" ".join(gram[0]) for gram in ngram_freq]
        frequencies = [freq for _, freq in ngram_freq]

        # Create figure
        fig, ax = plt.subplots(figsize=(12, 6))

        # Create bar plot
        bars = ax.barh(phrases, frequencies)

        # Customize plot
        ax.set_title(title or f"Top {top_k} {n}-grams")
        ax.set_xlabel("Frequency")

        # Add value labels on bars
        for bar in bars:
            width = bar.get_width()
            ax.text(
                width,
                bar.get_y() + bar.get_height() / 2,
                f"{int(width)}",
                ha="left",
                va="center",
                fontsize=10,
            )

        plt.tight_layout()
        return fig

    def perform_topic_modeling(
        self, texts: List[str], n_topics: int = 5, n_words: int = 10
    ) -> Tuple[Dict, plt.Figure]:
        """Perform topic modeling using LDA."""
        # Create document-term matrix
        vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words="english")
        doc_term_matrix = vectorizer.fit_transform(texts)

        # Create and fit LDA model
        lda_model = LatentDirichletAllocation(
            n_components=n_topics, random_state=42, learning_method="batch"
        )
        doc_topics = lda_model.fit_transform(doc_term_matrix)

        # Get feature names (words)
        feature_names = vectorizer.get_feature_names_out()

        # Calculate topic importance scores
        topic_importance = doc_topics.sum(axis=0)
        topic_importance = (
            topic_importance / topic_importance.sum()
        )  # Normalize to percentages

        # Sort topics by importance
        sorted_topic_idx = topic_importance.argsort()[::-1]

        # Define topic labels based on top words
        topic_labels = []
        topics = {}

        # Store sorted topics for consistent ordering
        sorted_topics = []

        for idx, topic_idx in enumerate(sorted_topic_idx):
            topic = lda_model.components_[topic_idx]
            top_words_idx = topic.argsort()[: -n_words - 1 : -1]
            top_words = [feature_names[i] for i in top_words_idx]
            topic_weight = topic[top_words_idx]

            # Create descriptive label from top 3 words
            label = f"Topic {idx + 1}: {', '.join(top_words[:3])}"
            topic_labels.append(label)

            topic_info = {
                "words": list(zip(top_words, topic_weight)),
                "importance": topic_importance[topic_idx],
                "dominant_docs": sum(doc_topics.argmax(axis=1) == topic_idx),
                "label": label,
            }
            topics[label] = topic_info
            sorted_topics.append((label, topic_info))

        # Create visualization with adjusted layout
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 16), height_ratios=[1, 3])

        # Plot 1: Topic Importance
        importance_values = [info["importance"] for _, info in sorted_topics]
        doc_counts = [info["dominant_docs"] for _, info in sorted_topics]
        labels = [info["label"] for _, info in sorted_topics]

        ax1.bar(labels, importance_values, alpha=0.8)
        ax1.set_title("Topic Importance in Corpus")
        ax1.set_ylabel("Proportion of Corpus")
        plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha="right")

        # Add document count annotations
        for i, (v, c) in enumerate(zip(importance_values, doc_counts)):
            ax1.text(i, v, f"{c} docs\n({v:.1%})", ha="center", va="bottom")

        # Plot 2: Words in Topics
        colors = plt.cm.Set3(np.linspace(0, 1, len(topics)))
        current_pos = 0
        y_ticks = []
        y_labels = []

        # Process topics in original order but reverse word order within each topic
        for (label, topic_info), color in zip(sorted_topics, colors):
            # Sort words by weight within each topic (descending order)
            words_weights = sorted(
                topic_info["words"], key=lambda x: x[1], reverse=True
            )
            words, weights = zip(*words_weights)

            # Reverse the positions for this topic's words
            positions = np.arange(len(words))[::-1] + current_pos

            # Plot bars for this topic
            ax2.barh(positions, weights, height=0.8, color=color, label=label)

            # Add word labels (in reversed order)
            y_ticks.extend(positions)
            y_labels.extend(words)

            # Add topic separator
            if current_pos > 0:
                ax2.axhline(
                    y=current_pos - 0.5, color="gray", linestyle="--", alpha=0.3
                )

            current_pos += len(words) + 1

        # Customize word plot
        ax2.set_yticks(y_ticks)
        ax2.set_yticklabels(y_labels)
        ax2.set_title("Top Words in Each Topic")
        ax2.set_xlabel("Word Weight in Topic")

        # Invert the y-axis to match the topic order in the importance plot
        ax2.invert_yaxis()

        plt.tight_layout()

        # Try to create interactive visualization if possible
        try:
            # Prepare data for pyLDAvis
            # Get term frequencies
            term_frequency = np.asarray(doc_term_matrix.sum(axis=0)).ravel()

            # Prepare document-topic distribution
            doc_topic_dist = doc_topics

            # Prepare topic-term distribution
            topic_term_dist = (
                lda_model.components_ / lda_model.components_.sum(axis=1)[:, np.newaxis]
            )

            # Create the prepared data
            prepared_data = pyLDAvis.prepare(
                topic_term_dist,  # Topic-term distribution
                doc_topic_dist,  # Document-topic distribution
                doc_lengths=np.sum(doc_term_matrix, axis=1).A1,  # Document lengths
                vocab=feature_names,  # Vocabulary
                term_frequency=term_frequency,  # Term frequencies
                start_index=0,  # pyLDAvis uses 0-based indexing
            )

            # Save the visualization
            pyLDAvis.save_html(prepared_data, "analysis_output/topic_model_vis.html")
        except Exception as e:
            print(f"Warning: Could not create interactive visualization: {str(e)}")
            print("Continuing with static visualization only...")

        return topics, fig

    def plot_summary_statistics(self, stats: Dict) -> plt.Figure:
        """Create visualization of summary statistics.

        Args:
            stats: Dictionary containing summary statistics

        Returns:
            Matplotlib figure with summary visualizations
        """
        # Create figure with subplots
        fig = plt.figure(figsize=(20, 10))
        gs = plt.GridSpec(2, 2, figure=fig)

        # Plot 1: Document Statistics (top left)
        ax1 = fig.add_subplot(gs[0, 0])
        doc_stats = [
            stats["num_documents"],
            stats["avg_length"],
            stats["total_unique_words"],
        ]
        labels = [
            "Number of\nDocuments",
            "Average\nDocument Length",
            "Total\nUnique Words",
        ]
        ax1.bar(labels, doc_stats)
        ax1.set_title("Document Statistics")
        # Add value labels on bars
        for i, v in enumerate(doc_stats):
            ax1.text(i, v, f"{int(v)}", ha="center", va="bottom")

        # Plot 2: Common Words (top right)
        ax2 = fig.add_subplot(gs[0, 1])
        words, counts = zip(*stats["common_words"])
        ax2.barh(words, counts)
        ax2.set_title("Most Common Words")
        ax2.set_xlabel("Frequency")
        # Add value labels on bars
        for i, v in enumerate(counts):
            ax2.text(v, i, f"{v}", ha="left", va="center")

        # Plot 3: Common Bigrams (bottom left)
        ax3 = fig.add_subplot(gs[1, 0])
        bigrams = self.get_ngrams(
            text=" ".join(stats.get("all_text", [])), n=2, top_k=10
        )
        bigram_labels = [" ".join(gram[0]) for gram in bigrams]
        bigram_counts = [count for _, count in bigrams]
        ax3.barh(bigram_labels, bigram_counts)
        ax3.set_title("Most Common Bigrams")
        ax3.set_xlabel("Frequency")
        # Add value labels
        for i, v in enumerate(bigram_counts):
            ax3.text(v, i, f"{v}", ha="left", va="center")

        # Plot 4: Common Trigrams (bottom right)
        ax4 = fig.add_subplot(gs[1, 1])
        trigrams = self.get_ngrams(
            text=" ".join(stats.get("all_text", [])), n=3, top_k=10
        )
        trigram_labels = [" ".join(gram[0]) for gram in trigrams]
        trigram_counts = [count for _, count in trigrams]
        ax4.barh(trigram_labels, trigram_counts)
        ax4.set_title("Most Common Trigrams")
        ax4.set_xlabel("Frequency")
        # Add value labels
        for i, v in enumerate(trigram_counts):
            ax4.text(v, i, f"{v}", ha="left", va="center")

        plt.tight_layout()
        return fig
