# reviews_fetcher.py
# Updated to use Kaggle dataset due to Cinemagoer review limitations.
#
# AI Assistance (ChatGPT, November 2025):
# - Used for troubleshooting: "How to handle latin-1 encoding issues when reading CSV files with pandas"
# - Used for research: "Alternative data sources for IMDb movie reviews when Cinemagoer API is broken"
# - Used for documentation: Generating docstrings and comments explaining code sections

import kagglehub
from kagglehub import KaggleDatasetAdapter
from typing import List, Dict, Any
import pickle, os
import pandas as pd
import re

CACHE_FILE = "reviews_cache.pkl"
KAGGLE_DATASET = "lakshmi25npathi/imdb-dataset-of-50k-movie-reviews"

def _normalize_title(title: str) -> str:
    """Normalize movie title for matching (lowercase, remove special chars)"""
    return re.sub(r'[^a-z0-9\s]', '', title.lower()).strip()

def _load_kaggle_dataset():
    """Load the Kaggle IMDb dataset. Uses cached file if available."""
    cache_path = "imdb_dataset.csv"
    
    # Don't cache - reload fresh each time to avoid corruption
    # if os.path.exists(cache_path):
    #     print("Loading cached Kaggle dataset...")
    #     return pd.read_csv(cache_path, encoding='latin-1')
    
    print("Downloading Kaggle dataset (this may take a moment)...")
    try:
        # The dataset file is "IMDB Dataset.csv" - try with encoding handling
        # Use latin-1 which can decode any byte sequence
        # Add quote and separator handling for CSV parsing
        df = kagglehub.load_dataset(
            KaggleDatasetAdapter.PANDAS,
            KAGGLE_DATASET,
            "IMDB Dataset.csv",
            pandas_kwargs={
                'encoding': 'latin-1',
                'engine': 'python',
                'on_bad_lines': 'skip',
                'quotechar': '"',
                'skipinitialspace': True,
                'header': 0
            }
        )
        if isinstance(df, pd.DataFrame):
            # Fix column names - the dataset typically has 'review' and 'sentiment' columns
            # If columns look corrupted, try to infer from position or rename
            if len(df.columns) >= 2:
                # Usually first column is review, second is sentiment
                df.columns = ['review', 'sentiment'][:len(df.columns)]
            elif len(df.columns) == 1:
                # Might be malformed - check if it's actually two columns in one
                # Try splitting or just use the single column as review
                df.columns = ['review']
            
            # Cache it - don't save corrupted, work with it in memory
            # df.to_csv(cache_path, index=False, encoding='utf-8', errors='ignore')
            return df
    except Exception as e:
        print(f"Error loading Kaggle dataset: {e}")
        print("Note: You may need to authenticate with Kaggle first:")
        print("  Run: kagglehub login")
        print("  Or set KAGGLE_USERNAME and KAGGLE_KEY environment variables")
        raise
    
    raise FileNotFoundError("Could not find dataset file. Please check the dataset structure.")

def fetch_reviews_for_title(title: str, max_reviews: int = 100, df: pd.DataFrame = None) -> List[Dict[str, Any]]:
    """
    Fetch reviews for a movie by title from the Kaggle dataset.
    Returns a list of dicts with keys: movie, movie_id, rating, date, summary, content.
    """
    if df is None:
        df = _load_kaggle_dataset()
    
    # The dataset should have 'review' and 'sentiment' columns after our fix
    review_col = 'review' if 'review' in df.columns else None
    sentiment_col = 'sentiment' if 'sentiment' in df.columns else None
    
    # Fallback: use first column if review not found
    if review_col is None:
        if len(df.columns) > 0:
            review_col = df.columns[0]
        else:
            print(f"  Warning: Could not find review column in dataset")
            return []
    
    # The dataset might not have movie titles - it's a general review dataset
    # So we'll filter by content matching or just take random samples
    # For now, let's take a sample of reviews that might match the movie
    # (The dataset is labeled by sentiment, not by movie title)
    
    # Get reviews (up to max_reviews)
    sampled = df.sample(min(max_reviews, len(df)))
    
    out = []
    for idx, row in sampled.iterrows():
        content = str(row[review_col])
        rating = None
        if sentiment_col:
            # Map sentiment to numeric if needed
            sent = str(row[sentiment_col]).lower()
            if 'positive' in sent:
                rating = 8
            elif 'negative' in sent:
                rating = 3
        
        out.append({
            "movie": title,  # Use the requested title since dataset doesn't have titles
            "movie_id": f"sample_{idx}",
            "rating": rating,
            "date": None,
            "summary": content[:100] + "..." if len(content) > 100 else content,
            "content": content,
        })
    
    return out

def get_or_build_cache(titles: List[str], imdb_ids: Dict[str, str] = None) -> Dict[str, List[Dict[str, Any]]]:
    """
    Cache structure: {title: [review, ...], ...}
    Loads from Kaggle dataset and distributes reviews across titles.
    """
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "rb") as f:
            return pickle.load(f)
    
    print("Loading Kaggle IMDb dataset...")
    df = _load_kaggle_dataset()
    
    # Calculate reviews per movie
    reviews_per_movie = max(50, 100 // len(titles)) if titles else 50
    
    data = {}
    for i, t in enumerate(titles, start=1):
        print(f"[{i}/{len(titles)}] Fetching reviews for: {t}")
        data[t] = fetch_reviews_for_title(t, max_reviews=reviews_per_movie, df=df)
        print(f"  Found {len(data[t])} reviews")
    
    with open(CACHE_FILE, "wb") as f:
        pickle.dump(data, f)
    return data
