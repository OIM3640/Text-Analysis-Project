"""Module for harvesting news data from News API.

This module provides functionality to:
1. Fetch election-related articles from News API
2. Cache API responses in JSON format
3. Handle API authentication and requests
4. Support multiple API endpoints (everything, top-headlines)
5. Implement rate limiting and error handling
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Union

from dotenv import load_dotenv
from newsapi import NewsApiClient
from newsapi.newsapi_exception import NewsAPIException


class NewsDataHarvester:
    """Class to handle news data harvesting operations.

    This class provides methods to fetch top headlines, all articles,
    and news sources using the News API service. It includes caching
    functionality to store API responses locally.
    """

    def __init__(self):
        """Initialize the NewsDataHarvester with API credentials.

        Raises:
            ValueError: If NEWS_API_KEY environment variable is not found.
        """
        load_dotenv()
        self._api_key = os.getenv("NEWS_API_KEY")
        if not self._api_key:
            raise ValueError("NEWS_API_KEY not found in environment variables")
        self._client = NewsApiClient(api_key=self._api_key)
        self._json_dir = Path("data/json")
        self._json_dir.mkdir(parents=True, exist_ok=True)

    def _save_to_json(self, data: Dict, filename: str) -> None:
        """Save data to a JSON file.

        Args:
            data: The data to save
            filename: Name for the JSON file (without extension)

        Note:
            Files are saved in the data/json directory with .json extension
        """
        filepath = self._json_dir / f"{filename}.json"
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def _load_from_json(self, filename: str) -> Optional[Dict]:
        """Load data from a JSON file.

        Args:
            filename: Name of the JSON file to load (without extension)

        Returns:
            The loaded data or None if file doesn't exist

        Note:
            Looks for files in the data/json directory
        """
        filepath = self._json_dir / f"{filename}.json"
        if filepath.exists():
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        return None

    def get_top_headlines(
        self,
        query: Optional[str] = None,
        sources: Optional[str] = None,
        category: Optional[str] = None,
        language: str = "en",
        country: Optional[str] = None,
        page_size: int = 20,
        use_cache: bool = True,
    ) -> Dict:
        """Fetch top headlines based on specified parameters.

        Args:
            query: Keywords or phrases to search for
            sources: Comma-separated string of news sources or blogs
            category: Category of news to fetch (e.g., business, technology)
            language: 2-letter ISO-639-1 code of the language (default: "en")
            country: 2-letter ISO 3166-1 code of the country
            page_size: Number of results to return per page (max 100)
            use_cache: Whether to use cached data if available

        Returns:
            Dict containing the API response with headlines

        Raises:
            NewsAPIException: If the API request fails
        """
        # Create a unique cache key based on parameters
        cache_key = f"headlines_{query}_{sources}_{category}_{language}_{country}"
        
        if use_cache:
            cached_data = self._load_from_json(cache_key)
            if cached_data:
                return cached_data

        try:
            data = self._client.get_top_headlines(
                q=query,
                sources=sources,
                category=category,
                language=language,
                country=country,
                page_size=page_size,
            )
            self._save_to_json(data, cache_key)
            return data
        except NewsAPIException as e:
            raise NewsAPIException(f"Failed to fetch top headlines: {str(e)}") from e

    def get_all_articles(
        self,
        query: str,
        from_date: Optional[Union[str, datetime]] = None,
        to_date: Optional[Union[str, datetime]] = None,
        language: str = "en",
        sort_by: str = "publishedAt",
        page: int = 1,
        use_cache: bool = True,
    ) -> Dict:
        """Fetch all articles based on specified parameters.

        Args:
            query: Keywords or phrases to search for
            from_date: Start date for article search (YYYY-MM-DD)
            to_date: End date for article search (YYYY-MM-DD)
            language: 2-letter ISO-639-1 code (default: "en")
            sort_by: Order to sort articles (relevancy,popularity,publishedAt)
            page: Page number for pagination (default: 1)
            use_cache: Whether to use cached data if available

        Returns:
            Dict containing the API response with articles

        Raises:
            NewsAPIException: If the API request fails
        """
        # Create a unique cache key based on parameters
        cache_key = (
            f"articles_{query}_{from_date}_{to_date}_"
            f"{language}_{sort_by}_{page}"
        )
        
        if use_cache:
            cached_data = self._load_from_json(cache_key)
            if cached_data:
                return cached_data

        try:
            data = self._client.get_everything(
                q=query,
                from_param=from_date,
                to=to_date,
                language=language,
                sort_by=sort_by,
                page=page
            )
            self._save_to_json(data, cache_key)
            return data
        except NewsAPIException as e:
            raise NewsAPIException(f"Failed to fetch articles: {str(e)}") from e

    def get_news_sources(
        self,
        category: Optional[str] = None,
        language: Optional[str] = None,
        country: Optional[str] = None,
        use_cache: bool = True,
    ) -> Dict:
        """Fetch available news sources.

        Args:
            category: Category to filter sources by (e.g., business, technology)
            language: 2-letter ISO-639-1 code of the language
            country: 2-letter ISO 3166-1 code of the country
            use_cache: Whether to use cached data if available

        Returns:
            Dict containing the API response with news sources

        Raises:
            NewsAPIException: If the API request fails

        Note:
            This endpoint returns a list of all available sources that can
            be used with the /top-headlines endpoint.
        """
        cache_key = f"sources_{category}_{language}_{country}"
        
        if use_cache:
            cached_data = self._load_from_json(cache_key)
            if cached_data:
                return cached_data

        try:
            data = self._client.get_sources(
                category=category,
                language=language,
                country=country,
            )
            self._save_to_json(data, cache_key)
            return data
        except NewsAPIException as e:
            raise NewsAPIException(f"Failed to fetch news sources: {str(e)}") from e
