"""Module for processing news data from News API responses.

This module handles:
1. Converting API responses to pandas DataFrames
2. Downloading full article content using newspaper3k
3. Filtering out invalid or removed articles
4. Processing up to 50 successfully downloaded articles
5. Caching processed articles in JSON format
6. Stop word removal and text preprocessing
7. Error handling and progress tracking
"""

import pandas as pd
from typing import Dict, List, Optional
import requests
from newspaper import Article
from urllib.parse import urlparse
import time
from pathlib import Path


class NewsDataProcessor:
    """Class to handle processing of news data."""

    def __init__(self):
        """Initialize the NewsDataProcessor."""
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def get_full_article_content(self, url: str) -> Optional[Dict[str, str]]:
        """Fetch and extract full article content from URL.

        Args:
            url: URL of the article

        Returns:
            Dictionary containing article text and metadata or None if failed
        """
        try:
            # Create Article object
            article = Article(url)
            
            # Download and parse article
            article.download()
            article.parse()
            
            # Return article content and metadata
            return {
                'full_text': article.text,
                'authors': article.authors,
                'publish_date': article.publish_date,
                'top_image': article.top_image,
                'movies': article.movies,
                'keywords': article.keywords,
            }
        except Exception as e:
            print(f"Error fetching article from {url}: {str(e)}")
            return None

    def articles_to_dataframe(self, articles_data: Dict, save_path: str = "data/processed/articles.json") -> pd.DataFrame:
        """Convert News API response to pandas DataFrame with full content."""
        # Check if we have saved processed data
        save_path = Path(save_path)
        if save_path.exists():
            print("Loading previously processed articles...")
            return pd.read_json(save_path)

        if not articles_data or 'articles' not in articles_data:
            raise ValueError("Invalid articles data format")

        # Extract articles list from the response
        articles_list = articles_data['articles']
        
        if not articles_list:
            raise ValueError("No articles found in the data")

        # Filter out removed articles
        valid_articles = [
            article for article in articles_list
            if article.get('title') != '[Removed]' 
            and article.get('description') != '[Removed]'
            and article.get('content') != '[Removed]'
        ]

        if not valid_articles:
            raise ValueError("No valid articles found after filtering removed content")

        # Create DataFrame from filtered articles
        df = pd.DataFrame(valid_articles)
        
        # Handle source information
        if 'source' in df.columns:
            df['source_id'] = df['source'].apply(lambda x: x.get('id') if x else None)
            df['source_name'] = df['source'].apply(
                lambda x: x.get('name') if x and x.get('name') != '[Removed]' else None
            )
            df = df.drop('source', axis=1)

        # Initialize new columns for full content
        df['full_text'] = None
        df['article_authors'] = None
        df['article_publish_date'] = None
        df['article_image'] = None
        df['article_movies'] = None
        df['article_keywords'] = None

        # Create a new DataFrame for successful articles
        successful_articles = pd.DataFrame(columns=df.columns)
        successful_count = 0
        target_count = 50  # Changed from 10 to 50

        # Fetch full content for articles until we get 50 successful ones
        print("\nFetching full article content...")
        for idx, row in df.iterrows():
            print(f"Processing article {idx + 1}/{len(df)}...")
            if row['url']:
                content = self.get_full_article_content(row['url'])
                if content and content['full_text']:  # Only count articles with actual content
                    new_row = row.copy()
                    new_row['full_text'] = content['full_text']
                    new_row['article_authors'] = str(content['authors'])
                    new_row['article_publish_date'] = content['publish_date']
                    new_row['article_image'] = content['top_image']
                    new_row['article_movies'] = str(content['movies'])
                    new_row['article_keywords'] = str(content['keywords'])
                    
                    successful_articles.loc[successful_count] = new_row
                    successful_count += 1
                    print(f"Successfully processed article {successful_count}/{target_count}")
                    
                    if successful_count >= target_count:
                        print(f"Reached {target_count} successful articles, stopping processing.")
                        break
                else:
                    print("Failed to get full content, skipping to next article...")

            time.sleep(1)  # Be nice to the servers

        if successful_count == 0:
            raise ValueError("No articles were successfully processed")

        print(f"\nSuccessfully processed {successful_count} articles")
        
        # Save the processed DataFrame as JSON
        save_path.parent.mkdir(parents=True, exist_ok=True)
        successful_articles.to_json(save_path, orient='records', indent=4)
        print(f"Saved processed articles to {save_path}")
        
        return successful_articles

    def get_text_content(
        self, 
        articles_data: Dict,
        remove_stopwords: bool = True
    ) -> List[str]:
        """Extract text content from articles.

        Args:
            articles_data: Dictionary containing News API response
            remove_stopwords: Whether to remove stop words from texts

        Returns:
            List of article text content strings
        """
        df = self.articles_to_dataframe(articles_data)
        
        # Download NLTK stop words if needed
        if remove_stopwords:
            import nltk
            try:
                nltk.data.find('corpora/stopwords')
            except LookupError:
                nltk.download('stopwords')
            from nltk.corpus import stopwords
            stop_words = set(stopwords.words('english'))
        
        texts = []
        for _, row in df.iterrows():
            content_parts = []
            
            # Use full text if available, otherwise fall back to summary
            if row.get('full_text'):
                content_parts.append(row['full_text'])
            else:
                if row.get('title'):
                    content_parts.append(row['title'])
                if row.get('description'):
                    content_parts.append(row['description'])
                if row.get('content'):
                    content_parts.append(row['content'])
            
            text = ' '.join(content_parts)
            
            # Remove stop words if requested
            if remove_stopwords:
                words = text.lower().split()
                words = [word for word in words if word not in stop_words]
                text = ' '.join(words)
            
            texts.append(text)

        return texts