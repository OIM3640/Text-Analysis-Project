from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer

urls = ['https://www.bbc.co.uk/news/world-us-canada-67067565',
        'https://www.bbc.co.uk/news/world-middle-east-67219256',
        'https://www.jpost.com/middle-east/article-768704',
        'https://www.jpost.com/middle-east/iran-news/article-765307'
    ]


urls2 = ['https://www.aljazeera.com/program/inside-story/2023/10/10/israel-palestine-conflict-and-the-gaza-war',
         'https://www.aljazeera.com/news/2023/10/10/israel-and-hamas-war-what-to-know-on-day-4-after-surprise-attack',
         'https://www.aljazeera.com/news/2023/10/14/israel-hamas-war-list-of-key-events-day-8',
         'https://www.aljazeera.com/news/2023/10/8/israel-hamas-conflict-list-of-key-events-day-2-after-surprise-attack',
         ]


############################################

import nltk
nltk.download('vader_lexicon') 

def full_article_parser_sentiment(url):
    ' this is a modified verison of the parsing function found news_parser.py. It gets the text of each article which is passed through the sentiment analysis'
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    article_text = soup.get_text(separator=' ', strip=True)
    driver.quit()  # Close the browser
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(article_text)

    return sentiment_score

sentiment_scores_west = [full_article_parser_sentiment(url) for url in urls]
sentiment_scores_palestine = [full_article_parser_sentiment(url) for url in urls2]


#print(sentiment_scores_west)
#print(sentiment_scores_palestine)

result_west = [{'neg': 0.155, 'neu': 0.765, 'pos': 0.08, 'compound': -0.9987}, 
{'neg': 0.15, 'neu': 0.783, 'pos': 0.067, 'compound': -0.9998}, 
{'neg': 0.117, 'neu': 0.787, 'pos': 0.096, 'compound': -0.989}, 
{'neg': 0.077, 'neu': 0.851, 'pos': 0.073, 'compound': -0.8567}]

result_palestine = [{'neg': 0.126, 'neu': 0.831, 'pos': 0.043, 'compound': -0.9942},
{'neg': 0.085, 'neu': 0.823, 'pos': 0.091, 'compound': -0.7416}, 
{'neg': 0.074, 'neu': 0.856, 'pos': 0.07, 'compound': -0.9678}, 
{'neg': 0.111, 'neu': 0.823, 'pos': 0.066, 'compound': -0.9955}]

def main(): 
    sentiment_scores_west = [full_article_parser_sentiment(url) for url in urls]
    sentiment_scores_palestine = [full_article_parser_sentiment(url) for url in urls2]
    print(sentiment_scores_west)
    print(sentiment_scores_palestine)


if __name__ == '__main__':
    main()