# This file stores the program to data pull from google and articles
# news_contents is the list with news search results

import config
from newspaper import Article
import json
from googleapiclient.discovery import build

service = build("customsearch", "v1", developerKey="AIzaSyCIcwVXbwNW62pyT-N-311y8OYntRtSOtw") #API created from Google search engine: AIzaSyCIcwVXbwNW62pyT-N-311y8OYntRtSOtw
response = service.cse().list(q=f'{config.company_query} news', cx="75973179b5d8045f3", num=config.num_results).execute()

# articles_count = 0

news_contents = []

if 'items' in response:
    # print(response)
    results = response['items']
    for result in results:
        # articles_count += 1
        individual_url = result['link']
    
        try:
            article = Article(individual_url)
            article.download()
            article.parse()
            article_text = article.text
            news_contents.append(article_text)
            #print(f" ARTICLE #{articles_count} states: {article_text}")
        except Exception as e:
            config.num_results += 1

############################### PICKLING DATA #####################################################################
# decided not to pickle data

# import pickle

# with open('news_contents.pickle','wb') as f:
#     pickle.dump(news_contents, f)

# with open('news_contents.pickle', 'r') as f:
#     reload_copy = pickle.load(f)
# TO CALL COPY: datapull_newspaper3k.reload_copy
