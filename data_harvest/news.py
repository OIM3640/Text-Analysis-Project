# # 1c96463708304daeb5f74385c1327bd1


from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key= '1c96463708304daeb5f74385c1327bd1')
api_key = '1c96463708304daeb5f74385c1327bd1'

def find_top_relevant_articles():
    '''this function looks for the top 5 most relevant articles about the Israel Palestine conflict across all articles'''
    top_articles = newsapi.get_everything(
        q='Israel Palestine conflict',
        language='en',
        sort_by='relevancy',
        page=1)
    
    for i, article in enumerate(top_articles['articles'][:10], start= 1):
        print(f"Article {i}:")
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}")
        print('-' * 100)


# creates a function that takes list of top articles. I will use this to get top five articles from the top news sources of a vareity of countries
def top_articles_by_country(source):
    'finds the top articles with a given set of sources. it thne sorts by relevancy and enumarates top 5 results'
    # Join the list of sources with commas if it's not already a string
    if isinstance(source, list):
        source = ','.join(source)
    
    articles_by_news_source = newsapi.get_everything(q='Israel Palestine conflict',
                                                     language='en',
                                                     sources= source,
                                                     sort_by='relevancy',
                                                     page=1)
    for i, article in enumerate(articles_by_news_source['articles'][:5], start=1):
        print(f"Article {i}:")
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}")
        print('-' * 100)

import requests
def get_top_english_israel_sources(api_key):
    'looks for english sources uisng the API key'
    url = "https://newsapi.org/v2/sources"
    params = {
        
        'country': 'eg',  
        'apiKey': api_key
    }
    response = requests.get(url, params=params)
    data = response.json()

    for i, source in enumerate(data['sources'][:3]):
        print(f"Source {i}:")
        print(f"ID: {source['id']}")
        print(f"Name: {source['name']}")
        print(f"Description: {source['description']}")
        print(f"URL: {source['url']}")
        print('-' * 100)
    else:
        print('no surce')



def main():
    'prefroms functions'
    print(find_top_relevant_articles)
    #top_articles_by_country('cnn', 'bbc')
    top_articles_by_country(['jerusalem post'])

    
    top_articles_by_country(['cnn', 'the-new-york-times', 'the-washington-post'])
    get_top_english_israel_sources(api_key)





if __name__ == '__main__':
    main()









