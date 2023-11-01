import urllib.request
import json

APIKEY = '34686ac4ab5866863e5cd49de96ce446'
url = f'https://api.themoviedb.org/3/movie/popular?api_key={APIKEY}&language=en-US&page=1'

def get_movie_overviews(APIKEY, num_pages=1):
    """
    gathers movie overviews from the TMDb API and returns list of movie overviews
    """
    overviews = []
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={APIKEY}&language=en-US&page={{}}'
    
    for page in range(1, num_pages + 1):
        url_page = url.format(page)
        with urllib.request.urlopen(url) as f:
            response_text = f.read().decode('utf-8')
            response_data = json.loads(response_text)
            overviews.extend(movie['overview'] for movie in response_data['results'] if 'overview' in movie)
            
    return overviews