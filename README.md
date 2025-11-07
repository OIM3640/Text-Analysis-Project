# IMDb Reviews Analyzer

## 1. Project Overview

This project is an IMDb Reviews Analyzer built with Python that processes and analyzes movie review text from the internet. The project was initially designed to use the Cinemagoer library to fetch user reviews directly from IMDb, but encountered a limitation: Cinemagoer's review endpoint is currently nonfunctional (as of 2025), with the `reviews` info key returning empty results even when movie metadata is successfully retrieved.

To work around this limitation while still meeting the assignment requirement of harvesting text from an internet source, the project switched to using a Kaggle dataset containing 50,000 IMDb movie reviews (`lakshmi25npathi/imdb-dataset-of-50k-movie-reviews`). This dataset provides real IMDb review text that can be programmatically accessed and analyzed.

The project's primary goals are to:
- Clean and preprocess text data (removing HTML tags, normalizing punctuation, handling encoding)
- Perform word frequency analysis to identify the most common terms in reviews
- Compute summary statistics (token count, vocabulary size, average word length, type-token ratio)
- Visualize results using ASCII bar charts (avoiding matplotlib as recommended)
- Optionally perform sentiment analysis using VADER (NLTK) to gauge emotional tone of reviews

The analyzer processes reviews for multiple movies (e.g., "The Dark Knight", "Barbie", "Oppenheimer") and generates comparative word frequency statistics and visualizations.

## 2. Implementation

The project follows a modular architecture with clear separation of concerns across four main Python files:

### Architecture

**`main.py`** - Entry point that orchestrates the analysis pipeline. Uses the `if __name__ == "__main__"` idiom to enable both script execution and module import. Coordinates data fetching and analysis for multiple movie titles.

**`reviews_fetcher.py`** - Handles data harvesting from the Kaggle dataset. This module:
- Downloads the IMDb reviews dataset using `kagglehub` library
- Loads the CSV file using pandas (justification below)
- Caches results using pickle to avoid re-downloading on subsequent runs
- Distributes reviews across requested movie titles

**`text_utils.py`** - Core text processing utilities implementing all required analysis steps:
- `clean_text()`: Removes HTML tags, decodes entities, lowercases, strips punctuation
- `remove_stopwords()`: Filters out common stop words using a custom list
- `word_frequencies()`: Uses Python's `Counter` to compute word frequencies
- `summary_stats()`: Calculates vocabulary metrics (token count, vocab size, avg word length, type-token ratio)
- `ascii_bar_chart()`: Generates ASCII-based visualizations without matplotlib

**`analyze_reviews.py`** - Orchestrates the analysis pipeline for a single movie title:
- Applies cleaning, tokenization, and stopword removal
- Computes frequencies and statistics
- Generates ASCII visualizations
- Optionally applies VADER sentiment analysis (toggleable via `USE_SENTIMENT` flag)

### Design Decisions

**Pandas Usage Justification**: Pandas was used only for reading the Kaggle CSV dataset, which required DataFrame parsing for initial text access. The `kagglehub` library's `KaggleDatasetAdapter.PANDAS` interface requires pandas to load the dataset. All subsequent analysis steps use standard Python libraries (`collections.Counter`, built-in string methods, etc.) rather than pandas operations. This minimal use of pandas is justified because manually parsing a 25MB CSV file with 50,000 rows would be significantly more complex and error-prone than using pandas' robust CSV reader.

**Caching Strategy**: The project uses pickle to cache fetched reviews, avoiding repeated API calls or dataset downloads. This improves performance and reduces load on external services.

**ASCII Visualization**: Instead of matplotlib (which the assignment recommends avoiding), the project uses ASCII bar charts printed to the console. This approach is lightweight, requires no external dependencies, and produces readable visualizations directly in terminal output.

### AI Tool Assistance

ChatGPT was used primarily for tedious tasks and documentation rather than core code generation:
- **Documentation**: Generated docstrings and comments explaining what each code section does (tedious but necessary for clarity)
- **Stopword list**: Compiled the comprehensive stopword list used in `text_utils.py` (time-consuming task of listing common English stopwords)
- **Troubleshooting**: When Cinemagoer's review endpoint failed, ChatGPT helped diagnose the problem and suggested alternative data sources (Kaggle dataset)
- **Reference lookups**: Looked up specific API usage (e.g., "How to use VADER sentiment analyzer from NLTK") and encoding solutions (e.g., "How to handle latin-1 encoding issues when reading CSV files with pandas")

All code logic, algorithms, and architecture decisions were implemented manually. ChatGPT was used as a research and documentation tool to speed up tedious tasks like writing comments and compiling reference lists. All AI-assisted sections are marked with comments indicating the specific use of ChatGPT.

## 3. Results

The analyzer successfully processes movie reviews and generates meaningful insights. Here are sample outputs from analyzing three popular films:

### Sample Output: The Dark Knight

```
=== The Dark Knight ===
num_tokens: 6463
vocab_size: 3005
avg_word_len: 5.847
type_token_ratio: 0.465

Top 20 words:
    one | ################################################ 49
    all | ############################################ 45
   like | ######################################## 41
    him | ################################ 33
     no | ############################# 30
   time | ############################ 29
   only | ########################## 27
   well | ######################## 25
```

### Sample Output: Barbie

```
=== Barbie ===
num_tokens: 6288
vocab_size: 2849
avg_word_len: 5.788
type_token_ratio: 0.4531

Top 20 words:
       all | ################################################ 52
      good | ####################################### 43
       one | ###################################### 42
      like | #################################### 39
      very | ############################# 32
```

### Findings

**Word Frequency Patterns**: Across all analyzed movies, common words like "all", "one", "like", "good", "very", "time", and "story" appear frequently. These are content words (not stopwords) that reflect common review language patterns. The presence of "good" and "like" suggests positive sentiment vocabulary, while "story", "characters", and "time" indicate reviewers focus on narrative elements.

**Vocabulary Richness**: The type-token ratio (TTR) ranges from 0.41 to 0.47, indicating moderate vocabulary diversity. Higher TTR suggests more varied word choice, while lower TTR suggests repetitive language. Movies show similar TTR values, suggesting consistent review writing styles across the dataset.

**Average Word Length**: Words average 5.7-5.8 characters, which is typical for English text. This metric helps validate that the text cleaning process is working correctly (not removing too much content).

**Sentiment Analysis**: When enabled (by setting `USE_SENTIMENT = True` in `analyze_reviews.py`), VADER sentiment analysis provides compound sentiment scores ranging from -1 (most negative) to +1 (most positive). The optional sentiment feature allows for deeper emotional analysis of review text.

The project also generates a `review_wordfreqs.tsv` file that can be opened in spreadsheet software for further analysis or visualization.

### Sample Terminal Output

The analyzer produces formatted ASCII bar charts directly in the terminal. A full sample output is saved in `images/output.txt` showing the complete analysis results for all three movies.

```
=== The Dark Knight ===
num_tokens: 6463
vocab_size: 3005
avg_word_len: 5.847
type_token_ratio: 0.465

Top 20 words:
    one | ################################################ 49
    all | ############################################ 45
   like | ######################################## 41
    him | ################################ 33
     no | ############################# 30
   time | ############################ 29
```

This visualization approach allows for immediate viewing of results without requiring external plotting libraries.

## 4. Reflection

### Process Reflection

**What Went Well**: The modular architecture made development straightforward. Breaking the project into `reviews_fetcher.py`, `text_utils.py`, `analyze_reviews.py`, and `main.py` allowed for independent testing and iteration. The switch to Kaggle dataset was smooth once the encoding issues were resolved. The ASCII visualization approach proved effective for terminal-based output without requiring matplotlib.

**Biggest Challenge**: The primary challenge was Cinemagoer's nonfunctional review endpoint. Initial attempts to fetch reviews directly from IMDb failed, requiring research into alternative data sources. The Kaggle dataset alternative introduced new challenges:
- Encoding issues: The CSV file used `latin-1` encoding, which required specific pandas configuration
- Column parsing: Initial attempts to load the dataset resulted in corrupted column names, requiring explicit column renaming
- File size: The 25MB dataset required careful handling of memory and download time

**How It Was Solved**: ChatGPT was helpful for troubleshooting and research. When Cinemagoer failed, I asked ChatGPT for alternative IMDb data sources and received suggestions for Kaggle datasets. For encoding problems, ChatGPT provided guidance on pandas `read_csv` parameters, leading to the `encoding='latin-1'` and `engine='python'` solution.

**Testing Plan**: Testing was done incrementally:
1. Tested data fetching with a single movie title
2. Verified text cleaning produced expected output (no HTML tags, proper lowercasing)
3. Validated word frequencies matched manual counts for small samples
4. Confirmed ASCII charts displayed correctly
5. Tested caching to ensure subsequent runs used cached data

**Project Scope**: The project scope was appropriately sized. It met all required steps while including one optional technique (sentiment analysis). The modular design makes it easy to extend with additional features (e.g., text similarity, clustering) without major refactoring.

### Learning Reflection

**Biggest Takeaway**: The most valuable learning was understanding how to work with real-world data sources that have limitations. Encountering Cinemagoer's broken API taught me to:
- Research alternative data sources when primary ones fail
- Handle encoding issues that are common in web-scraped data
- Use caching effectively to avoid repeated downloads
- Adapt project scope when technical constraints emerge

**AI Tools' Role**: ChatGPT was most useful for tedious tasks and quick reference lookups:
- **Stopword compilation**: Asked ChatGPT to generate a comprehensive list of common English stopwords rather than manually typing them all
- **Documentation**: Used ChatGPT to write clear docstrings and comments explaining code sections (tedious but necessary)
- **Quick reference**: When I needed to look up specific API usage (like VADER sentiment analyzer), ChatGPT provided quick answers instead of digging through documentation
- **Troubleshooting**: When encoding errors occurred, ChatGPT suggested solutions to try (like using `latin-1` encoding)

The AI assistance was most effective for tasks that were time-consuming but straightforward (like compiling stopwords) or for quick reference lookups. All code logic and architecture decisions were implemented manually.

**Future Applications**: The skills learned here apply to any text analysis project:
- Working with APIs and datasets
- Text preprocessing pipelines
- Statistical analysis of language patterns
- Building modular, maintainable code

**What I Wish I Knew**: 
- That Cinemagoer's review endpoint was broken—would have saved time by starting with Kaggle dataset
- More about encoding issues in CSV files—would have anticipated latin-1 encoding challenges
- The importance of caching early—would have implemented caching from the start to speed up iteration

### Future Improvements

Potential enhancements for this project:
1. **Text Similarity**: Add cosine similarity calculation to compare vocabulary across different movies
2. **Sentiment Distribution**: When sentiment is enabled, create visualizations showing sentiment distribution (negative/neutral/positive buckets)
3. **Comparative Analysis**: Generate side-by-side comparisons of multiple movies' word frequencies
4. **Interactive Dashboard**: Create a simple web interface using Flask to explore results interactively
5. **Movie-Specific Filtering**: Improve the Kaggle dataset usage to actually filter reviews by movie title (currently samples randomly)
6. **Time-Based Analysis**: If review dates become available, analyze sentiment trends over time

The modular architecture makes these improvements straightforward to implement without major refactoring.

#   t e x t - a n a l y s i s  
 