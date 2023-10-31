# This file stores the program to data pull from google and articles

#API created from Google search engine: AIzaSyCIcwVXbwNW62pyT-N-311y8OYntRtSOtw

from newspaper import Article
import json
from googleapiclient.discovery import build

#created Customized Search Engine and API using Google's programmable search engine
# api_key = "AIzaSyCIcwVXbwNW62pyT-N-311y8OYntRtSOtw"
# cse_id = "75973179b5d8045f3"

company_query = "Fenty beauty" #NEXT STEP: WILL MAKE INTO AN INPUT IN A SEPARATE FILE TO PROGRAM FOR ALL SEARCHES (i want to be able to ask user to input what company they want to research and this step will be iput of company to be queried)

# url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse_id}&q={company_query}"

def search(company_query, num_results=5):
    service = build("customsearch", "v1", developerKey="AIzaSyCIcwVXbwNW62pyT-N-311y8OYntRtSOtw")
    response = service.cse().list(q=company_query, cx="75973179b5d8045f3", num=num_results).execute()

    # print(response)

    # if 'items' in response:
    #     results = response["items"]
    #     urls = [result["link"] for result in results]
    #     return urls

    articles_count = 0

    if 'items' in response:
        results = response['items']
        for result in results:
            articles_count += 1
            individual_url = result['link']
            article = Article(individual_url)
            article.download()
            article.parse()
            article_text = article.text
            print(f" ARTICLE #{articles_count} states: {article_text}")
        
print(search(company_query))

#     data = response.json()

#     for item in data.get("items", []):
#         individual_url = item.get("link")
#         article = Article(individual_url)
#         article.download()
#         article.parse()
#         article_text = article.text
#         print(f"ARTICLE {article_text}") 
    
#     else:
#         print("Error: Unable to retrieve search results")




# # asked ChatGPT how I could use google engine; The code below gives me this only gives me official sites that use the company name (doesnt help much)
# response = requests.get(url)

# if response.status_code == 200: # what does this mean??????
#     data = response.json()

#     for item in data.get("items", []):
#         title = item.get("title")
#         link = item.get("link")
#         print(f"Title: {title}")
#         print(f"Link: {link}")
    
#     else:
#         print("Error: Unable to retrieve search results")
