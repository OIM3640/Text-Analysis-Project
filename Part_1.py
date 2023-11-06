import requests
from bs4 import BeautifulSoup
import json
from collections import Counter
import re
from textblob import TextBlob

""" The objective of this analysis, is two extract news articles from two different news sources. I will be extracting from
a right leaning party, Fox News, and a left leaning part, MSNBC, to compare their take on the Israel and Palestine crisis.
I want to analyze these tets to see what type of tone and language is used when talking about this topic. I want to see the verbiage 
used to decide if one news source is more humane and focused on the lives that are being lost, or if one side is more politicl and 
only reporting political and economic implications about the event.  """

def fetch_articles(api_key):
    # Definining the URL for the NewsAPI endpoint with specific parameters. Endpoint was foud on NewsAPI website 
    url = ('https://newsapi.org/v2/everything?'
           'q=("Israel Palestine war" OR "Hamas" OR "Gaza") AND (conflict OR war OR bombings OR airstrikes)&' 
           'domains=foxnews.com,msnbc.com&'     # Only include articles from these domains
           'from=2023-10-03&'                 # Start date for articles
           'to=2023-11-03&'                   # End date for articles
           'sortBy=relevancy&'                # Sort by relevancy
           'language=en&'                     # Articles in English
           f'apiKey={api_key}')              

    # GET request to the NewsAPI endpoint
    response = requests.get(url)

    # Checking if the request was successful
    if response.status_code == 200:
        # Process the response if the request was successful
        return response.json()
    else:
        # Print an error message if the request failed
        print(f"Error: {response.status_code}")
        return None

def get_word_frequencies(titles):
    # Combine all titles into one large string
    all_titles = ' '.join(titles)
    
    # Tokenize the string into words
    words = re.findall(r'\w+', all_titles.lower())  # This uses regular expressions to find words
    
    # Remove stop words
    stop_words = set(['for', 'a', 'the', 'and', 'to', 'in', 'of', 'on', 'with', 'as', 'at', 'by', 'from', 'is', 'it', 'that', 'this', 'was', 'will', 'be', 'or', 'are', 'an']) 
    words = [word for word in words if word not in stop_words]
    
    # Count the words
    word_freq = Counter(words)
    
    return word_freq

def get_full_article_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        article_body = None
        if 'foxnews.com' in url:
            article_body = soup.find('div', class_='article-content-wrap sticky-columns')
        elif 'msnbc.com' in url:
            article_body = soup.find('div', class_='article-body')
        
        # If article_body is None, the selector did not find the content
        if article_body is None:
            print(f"Could not find the article body for URL: {url}")
            return None

        paragraphs = article_body.find_all('p')
        article_text = ' '.join(paragraph.text for paragraph in paragraphs)
        return article_text

    except requests.RequestException as e:
        print(f"Error fetching article from {url}: {e}")
        return None

def save_article_to_file(filename, article_text):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(article_text)

def perform_sentiment_analysis(text):
    # Creating a TextBlob object
    analysis = TextBlob(text)
    # Return sentiment
    return analysis.sentiment

def main():
    api_key = '05179757eaf84491931d350951a86161' 
    articles_data = fetch_articles(api_key)

    # Define the URL or title for the articles you'd like to fetch
    specific_articles = [
        'SEAN HANNITY: If Hamas laid down their arms today, nobody would die',
        'https://www.msnbc.com/opinion/msnbc-opinion/israel-hamas-gaza-war-crimes-evacuation-humanitarian-rcna120345'
    ]

    if articles_data:
        # Extract titles for word frequency analysis
        titles = [article['title'] for article in articles_data['articles']]
        word_freq = get_word_frequencies(titles)
        
        # Print the most common words in titles
        for word, freq in word_freq.most_common(20):
            print(f"{word}: {freq}")

        #  Scraping the full text of fox news and MSNBC articles 
        for article in articles_data['articles']:
            if article['url'] in specific_articles or article['title'] in specific_articles:
                print(f"Fetching full text for: {article['title']}")
                full_text = get_full_article_text(article['url'])
                
                if full_text:
                    #Sentiment Analysis on key words in the title 
                    sentiment_result = perform_sentiment_analysis(full_text)
                    print(f"Sentiment analysis result for {article['title']}:")
                    print(f"Polarity: {sentiment_result.polarity}, Subjectivity: {sentiment_result.subjectivity}")
                    
                    filename = f"{article['title'].replace(':', '').replace(' ', '_')}.txt"
                    save_article_to_file(filename, full_text)
                    print(f"Successfully saved full text to {filename}")
                else:
                    print(f"Failed to fetch full text for: {article['title']}")
                print()
            else:
                print(f"Skipping article: {article['title']}")

if __name__ == "__main__":
    main()