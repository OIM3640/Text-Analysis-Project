import requests

def query_wikipedia(search_term):
    base_url = 'https://en.wikipedia.org/w/api.php'
    
    params = {
        'action': 'query',
        'format': 'json',
        'list': 'search',
        'utf8': 1,
        'srsearch': search_term,
        'srprop': 'snippet',
        'srlimit': 1,
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        page_id = data['query']['search'][0]['pageid']
        return page_id
    else:
        return None

def get_page_content(page_id):
    base_url = 'https://en.wikipedia.org/w/api.php'
    
    params = {
        'action': 'query',
        'format': 'json',
        'prop': 'extracts',
        'pageids': page_id,
        'explaintext': 1,
        'exsectionformat': 'wiki',
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        content = data['query']['pages'][str(page_id)]['extract']
        return content
    else:
        return None

search_term = 'Consumer Price Index'
page_id = query_wikipedia(search_term)

if page_id:
    content = get_page_content(page_id)
    print(content)
else:
    print(f"No Wikipedia page found for '{search_term}'")

