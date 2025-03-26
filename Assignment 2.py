import urllib.request
import string 
import json
import requests
import os
from pprint import pprint
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from thefuzz import fuzz
load_dotenv()

def access_api():
    """ Retrieves articles from News API and Project Gutenberg. It fetches an article regarding Diwali and eBook section. Returns list of dictionaries with titles and content."""
    api_key = os.getenv('API_KEY')
    if not api_key:
        print("Error: API key not found. Check your .env file")
        return []
    
    print("API key successfully retrieved.")
    url1= f"https://newsapi.org/v2/everything?q=Millions+of+Indians+celebrate+Diwali,+the+festival+of+lights&apiKey={api_key}"
    url2="https://www.gutenberg.org/cache/epub/14360/pg14360-images.html"
    articles =[]

    try:
        response =requests.get(url1)
        response.raise_for_status()
        data = response.json()

        for article in data.get('articles',[]):
            if article.get('title')=="Millions of Indians celebrate Diwali, the festival of lights":
                full_content = fetch_full_article(article['url'])
                articles.append({'title': article['title'],'content': full_content})
                break
    except requests.exceptions.RequestException as e:
        print(e)
    
    try: 
        with urllib.request.urlopen(url2) as f:
            gt_html= f.read().decode('utf-8')
            soup = BeautifulSoup(gt_html,"html.parser")
            intro = soup.find(string=lambda text: text and 'introduction.' in text.lower().strip())
           
            if intro:
                intro_sec = intro.find_parent()
                gt_txt = []

                for sibling in intro_sec.find_next_siblings():
                    if sibling.name and sibling.name.startswith('h'):
                        break
                    gt_txt.append(sibling.get_text(separator=' ', strip=True))
                gt_txt = ' '.join(gt_txt)
            else:
                gt_txt = "No intro found"
            articles.append({'title':'The Project Gutenberg eBook of The Dawn and the Day; Or, The Buddha and the Christ, Part I',
                             'content':gt_txt })
    except Exception as e:
        print(e)
    
    return articles

def fetch_full_article(article_url):
    """Retrieves full text given url. Extracts via paragraphs and applies debugging error codes."""
    try:
        response = requests.get(article_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        paragraphs = soup.find_all('p')
        full_text = ' '.join([para.get_text() for para in paragraphs])
        return full_text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching article: {e}")
        return "Unable to retrieve full content."
    

    
def compare_articles(articles):
    """Compares article similarity. Uses fuzzy matching to return ratios and similarity scores"""
    comparisons = []
    for i in range(len(articles)):
        for j in range(i+1, len(articles)):
            content1 = articles[i].get('content','').lower().strip()
            content2 = articles[j].get('content','').lower().strip()
            if not content1 or not content2:
                continue
            sim_ratio = fuzz.ratio(content1, content2)
            partial_ratio = fuzz.partial_ratio(content1,content2)
            token_sort_ratio = fuzz.token_sort_ratio(content1,content2)
            comparisons.append({
                'article1': articles[i].get('title', 'No title'),
                'article2': articles[j].get('title', 'No title'),
                'similarity_ratio': sim_ratio,
                'partial_ratio': partial_ratio,
                'token_sort_ratio': token_sort_ratio
            })
            return comparisons

    
def get_word_freq(texts):
        """Finds 13 most common words in provided texts, excluding stop words."""
        stop_words = {
   "p","the", "and", "to", "of", "a", "in", "that", "it", "is","its", "was", "he", "for", "with", "as", "his", "on", 
    "be", "at", "by", "i", "you", "this", "we", "but", "had", "she", "or", "which", "from", "an", "were", 
    "not", "are", "they", "have", "has", "her", "him", "all", "their", "been", "will", "who", "would", "when","while","through","so","where","no","now", "my", "then","every",
    "one", "there", "can", "some", "those", "whose", "if","like", "lovebr", "such", "lightbr"}
        word_freq = {}
        for text in texts:
            
            text = text.translate(str.maketrans("","", string.punctuation)).lower()
            words = text.split()
   
            for word in words:
                if word not in stop_words:
                    word_freq[word]=word_freq.get(word,0)+1

        top_words = sorted(word_freq.items(), key= lambda item: item[1], reverse=True)[:13]
        print(top_words)
        return top_words



def main():
    """Main that calls all other functions to perform text analysis"""
    articles = access_api()
    
    if articles:
        print("**Project Overview**")
        print("The articles are analyzed for similarity using techniques like fuzzy matching and word frequency analysis.\n")
        print("**Implementation")
        print("**Results**")
        comparisons=compare_articles(articles)
        for comp in comparisons:
            print(f"Comparing '{comp['article1']}' and '{comp['article2']}':")
            print(f"  Similarity Ratio: {comp['similarity_ratio']}")
            print(f"  Partial Ratio: {comp['partial_ratio']}")
            print(f"  Token Sort Ratio: {comp['token_sort_ratio']}")
            
        for article in articles:
            top_words = get_word_freq([article.get('content')])
            print(f"Top words for article '{article.get('title', 'No title')}': {top_words}")

    else:
        print("No articles found")
    
if __name__ == "__main__":
    main()