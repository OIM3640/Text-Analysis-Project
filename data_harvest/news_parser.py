
import sys
from unicodedata import category

#########################################################################################
# Issue: websites were blocking scrapping through use of the two parsing libraries 
# solution: I asked chatgbt to find a work around this protections. It showed me the code using a new library called selenium which is meant to simulate human interaction 
# with the website allowing to fully parse it and get access to the text
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords


def full_article_parser(url):
    # Initialize headless Chrome browser
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Open the URL and get the page content
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Here you may want to adjust the method of finding the text if necessary
    # For now, let's assume you're taking all the text
    article_text = soup.get_text(separator=' ', strip=True)
    
    # Close the browser
    driver.quit()
    
    stop_words = set(stopwords.words('english'))
    # Create a histogram of word frequencies
    hist = {}
    strippables = ''.join([chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")])

    # Replace hyphens and em dashes with spaces
    article_text = article_text.replace('-', ' ')
    article_text = article_text.replace(chr(8212), ' ')  

    # Split the text into words and count them
    for word in article_text.split():
        word = word.strip(strippables)
        word = word.lower()
        if word not in stop_words:
            hist[word] = hist.get(word, 0) + 1
        
    

    return hist

def process_urls(urls):
    'goes through the lost of urls and inputs them into the parsing function'
    all_word_counts = {}
    for url in urls:
        word_counts = full_article_parser(url)
        for word, count in word_counts.items():
            if word in all_word_counts:
                all_word_counts[word] += count
            else:
                all_word_counts[word] = count
    return all_word_counts

# Two set of articles that will be analayzed:
urls = ['https://www.bbc.co.uk/news/world-us-canada-67067565',
        'https://www.bbc.co.uk/news/world-middle-east-67219256',
        'https://www.jpost.com/middle-east/article-768704',
        'https://www.jpost.com/middle-east/iran-news/article-765307'
    ]

combined_word_counts_west = process_urls(urls)
print(combined_word_counts_west)

urls2 = ['https://www.aljazeera.com/program/inside-story/2023/10/10/israel-palestine-conflict-and-the-gaza-war',
         'https://www.aljazeera.com/news/2023/10/10/israel-and-hamas-war-what-to-know-on-day-4-after-surprise-attack',
         'https://www.aljazeera.com/news/2023/10/14/israel-hamas-war-list-of-key-events-day-8',
         'https://www.aljazeera.com/news/2023/10/8/israel-hamas-conflict-list-of-key-events-day-2-after-surprise-attack',
         ]


combined_word_counts_palestine = process_urls(urls2)
print(combined_word_counts_palestine)

# use pickle to speed analysis process. Currently it is taking too long to pasrse through the urls and do analysis. 

import pickle
with open('combined_word_counts_west.pkl', 'wb') as f:
    pickle.dump(combined_word_counts_west, f)

with open('combined_word_counts_palestine.pkl', 'wb') as f:
    pickle.dump(combined_word_counts_palestine, f)
