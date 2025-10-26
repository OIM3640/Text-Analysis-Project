"""
THEEPOCHTIMES ARTICLES SCRAPE
"""
import newspaper
import json

def build_the_epoch_times_source():

    the_epoch_times_paper = newspaper.build(
    'https://www.theepochtimes.com/us/us-politics',
    memoize_articles=False, # false so that it cache new data every time, that way it will analyze the most relevant data only 
    browser_user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) "
        "Version/16.0 Safari/605.1.15"
)
    
    print(f"Found {len(the_epoch_times_paper.articles)} articles.")

    articles_collected = []

    i = 1
    for article in the_epoch_times_paper.articles[:50]:
        try:
            article.download()
            article.parse()

            print(f"{i}. {article.title}.")
            print(article.url)
            i += 1

            articles_collected.append({"title": article.title, "url": article.url, "text": article.text})
        
        except Exception as e:
            print(f"Skipped article {i} due to error: {e}")
    

    return articles_collected

def save_to_json(data):
    with open("project/data/the_epoch_times_articles.json", "w", encoding = "utf-8") as file:
        json.dump(data, file, indent = 2, ensure_ascii = False) # ensure ensure_ascii = False is something chatgpt helped me with so that special characters are handled correctly
    print(f"Saved {len(data)} articles to data/the_epoch_times_articles.json")

if __name__ == "__main__":
    articles = build_the_epoch_times_source()
    save_to_json(articles)