# Import libraries
from mediawiki import MediaWiki  # Library accessing MediaWiki API
import nltk  # NLTK library
from nltk.sentiment.vader import SentimentIntensityAnalyzer  # Sentiment analysis tool
from collections import Counter  # Counter for word frequency counting
import matplotlib.pyplot as plt  # Matplotlib library for plotting. I learned this from geek for geeks, and inserted the link to the article i used in part 3 (the other .py)

# Download NLTK data (VADER Lexicon used for sentiment analysis)
nltk.download('vader_lexicon')

def remove_stopwords(text):
    """
    this function removes stopowords from the text
    """
    tokens = nltk.word_tokenize(text)  # Tokenize the text
    stop_words = set(nltk.corpus.stopwords.words('english'))  # Get English stopwords
    # Filter out stopwords and non-alphabetic words
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words and word.isalpha()]
    return filtered_tokens


def word_frequencies(text):
    """"
    this function calculates word frequencies
    """
    word_list = remove_stopwords(text)  # Remove stopwords from text
    word_freq = Counter(word_list)  # Count word frequencies
    return word_freq

def lookup_words(word_freq, words_to_lookup):
    """
    this function looks up for specific words in the word frquency dictionary
    """
    results = {}
    for word in words_to_lookup:
        results[word] = word_freq.get(word, 0)  # Get frequency of each word in words_to_lookup
    return results

def plot_top_words(word_freq, n=10):
    """
    this function plots the top 10 most frequent words. I used an article on Geeks for Geeks as a guide to develop this code, I out the link of the article in part 3. 
    """
    top_words = dict(word_freq.most_common(n))  # Get the top most frequent words
    plt.figure(figsize=(10, 6)) #Create a new figure for the plot with this size
    plt.bar(top_words.keys(), top_words.values())  #Plot a bar chart with words on the x-axis and their frequencies on the y-axis
    plt.xlabel('Words') #label for the x-axis
    plt.ylabel('Frequency') #label for the y-axis
    plt.title('Top 10 Most Frequent Words') #title of the plot
    plt.xticks(rotation=45) #Rotate the x-axis labels 
    plt.show() #show the plot


def main():
    # link Wikipedia article about "Babson College"
    wiki = MediaWiki()
    article = wiki.page("Babson College")
    article_text = article.content  # Get the content of the article

    cleaned_text = ' '.join(remove_stopwords(article_text))  # Remove stopwords from text
    sid = SentimentIntensityAnalyzer()  # Initialize SentimentIntensityAnalyzer
    sentiment_scores = sid.polarity_scores(cleaned_text)  # Perform sentiment analysis 
    word_freq = word_frequencies(article_text)  # Calculate word frequencies in the article text

    # Words to lookup in the word frequency dictionary
    words_to_lookup = ['Babson', 'Entrepreneurship', 'Wellesley', 'business', 'MBA', 'students', 
                       'undergraduates', 'Babson', 'CEO', 'Roger', 'banker', 'success']
    lookup_results = lookup_words(word_freq, words_to_lookup)  # Lookup specified words in word frequency dictionary

    # Plot the top 10 most frequent words
    plot_top_words(word_freq, 10)

    # Print word frequencies
    print("Word frequencies:")
    print(word_freq)

    # Print lookup results
    print("\nLookup results:")
    for word, frequency in lookup_results.items():
        print(f"{word}: {frequency}")

    # Print sentiment analysis results
    print("\nSentiment Analysis:")
    print(f"Negative: {sentiment_scores['neg']}")
    print(f"Neutral: {sentiment_scores['neu']}")
    print(f"Positive: {sentiment_scores['pos']}")
    print(f"Compound: {sentiment_scores['compound']}")

# Check if the script is being run directly
if __name__ == "__main__":
    main()  # Call the main function if the script is run directly
