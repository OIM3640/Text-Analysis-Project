# Election News Analysis Project

A comprehensive text analysis tool for analyzing news coverage of the 2024 US Presidential Election using the News API. This project performs various text analysis techniques including sentiment analysis, topic modeling, word frequency analysis, and text clustering.

## Project Overview

This project analyzes election news coverage by:
1. Fetching recent election-related articles from News API
2. Downloading and processing full article content
3. Performing comprehensive text analysis
4. Generating interactive and static visualizations
5. Providing detailed statistical analysis

The project write up can be found [here](write_up.md).

## Project Structure

```
project/
├── data/
│   ├── json/          # Cached API responses
│   └── processed/     # Processed article data
├── analysis_output/   # Generated visualizations
│   ├── wordcloud.png              # Election-themed word cloud
│   ├── sentiment_distribution.png # Article sentiment analysis
│   ├── text_clusters.png         # Article similarity clusters
│   ├── topic_model.png           # Topic modeling results
│   ├── summary_statistics.png    # Statistical overview
│   └── topic_model_vis.html      # Interactive topic visualization
├── data_harvesting.py # News API interaction
├── data_processing.py # Data preparation
├── text_analysis.py   # Text analysis tools
├── main.py           # Main entry point
├── requirements.txt   # Project dependencies
└── .env              # API credentials
```

## Features

### 1. Data Collection & Processing
- Fetches election news from News API's everything endpoint
- Downloads full article content using newspaper3k
- Implements smart caching with JSON storage
- Filters out invalid or removed articles
- Processes up to 50 successfully downloaded articles
- Handles rate limiting and error recovery

### 2. Text Analysis Capabilities
- **Word Frequency Analysis**
  - Word frequencies with stop word removal
  - TF-IDF scoring
  - Red, white, and blue themed word cloud

- **N-gram Analysis**
  - Common bigrams (two-word phrases)
  - Common trigrams (three-word phrases)
  - Frequency visualizations

- **Topic Modeling**
  - Latent Dirichlet Allocation (LDA)
  - Topic importance visualization
  - Word weights within topics
  - Interactive topic exploration
  - Document distribution across topics

- **Sentiment Analysis**
  - Polarity (positive/negative)
  - Subjectivity analysis
  - Sentiment distribution visualization

- **Text Similarity**
  - Pairwise similarity matrix
  - Text clustering visualization
  - Multi-dimensional scaling (MDS)

### 3. Statistical Analysis
- Document Statistics
  - Number of articles
  - Average article length
  - Total unique words
  - Most common words

- Phrase Analysis
  - Common two-word phrases
  - Common three-word phrases
  - Phrase frequency visualization

## Installation

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in project root
2. Add your News API key:
```
NEWS_API_KEY=your_api_key_here
```

## Usage

Run the analysis pipeline:
```bash
python main.py
```

This will:
1. Fetch recent election news articles
2. Download and process full content
3. Perform comprehensive analysis
4. Generate visualizations
5. Print analysis results

## Output

### Visualizations
- `wordcloud.png`: Election-themed word cloud
- `sentiment_distribution.png`: Article sentiment analysis
- `text_clusters.png`: Article similarity visualization
- `topic_model.png`: Topic modeling results
- `summary_statistics.png`: Statistical overview
- `topic_model_vis.html`: Interactive topic exploration

### Console Output
- Processing progress
- Word frequencies
- TF-IDF analysis
- Summary statistics
- Sentiment analysis
- Topic modeling results
- N-gram analysis

## Best Practices

1. Use cached responses when possible
2. Check analysis_output/ for visualizations
3. Review console output for insights
4. Monitor API rate limits
5. Use the virtual environment

## Error Handling

Comprehensive error handling for:
- Missing API credentials
- Failed API requests
- Article download failures
- Data processing errors
- Analysis failures
- Invalid content

## Dependencies

Key dependencies include:
- newsapi-python: API interaction
- newspaper3k: Article downloading
- nltk: Text processing
- scikit-learn: Topic modeling
- textblob: Sentiment analysis
- matplotlib/seaborn: Visualization
- pyLDAvis: Interactive topic visualization

See `requirements.txt` for complete list and versions.

## License

This project is licensed under the MIT License - see the LICENSE file for details.