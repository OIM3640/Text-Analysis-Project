import requests

def fetch_wikipedia_article(title):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "explaintext": True,
        "titles": title
    }
    response = requests.get(url, params=params)
    data = response.json()
    page = next(iter(data["query"]["pages"].values()))
    return page["extract"]