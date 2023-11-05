import urllib.request
import json
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import string
from collections import Counter
import datetime
import random

APIKEY = '34686ac4ab5866863e5cd49de96ce446'

api_cache = {}  # Cache for API responses; added by Chat GPT

def make_api_request(url):
    try:
        with urllib.request.urlopen(url) as f:
            response_text = f.read().decode('utf-8')
            response_data = json.loads(response_text)
            return response_data
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_api_data(url, movie_id=None):
    if movie_id and movie_id in api_cache:
        return api_cache[movie_id]
    response_data = make_api_request(url)
    if movie_id:
        api_cache[movie_id] = response_data
    return response_data

def preprocess_text(text):
    # edited by Chat GPT
    stopwords_ = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    processed_text = [w for w in words if w not in string.punctuation and w not in stopwords_ and len(w) > 1 and w != "the"]
    return processed_text

def print_movie_details(movie_details):
    print("\nMovie Details:")
    print(f"Title: {movie_details.get('title', 'N/A')}")
    print(f"Overview: {movie_details.get('overview', 'N/A')}")
    print(f"Genres: {', '.join(genre['name'] for genre in movie_details.get('genres', []))}")
    print(f"Production Companies: {', '.join(company['name'] for company in movie_details.get('production_companies', []))}")
    print(f"Average Rating: {movie_details.get('vote_average', 'N/A')}")
    print(f"Number of Votes: {movie_details.get('vote_count', 'N/A')}")

def get_processed_movie_counter(): 
    # added by Chat GPT 
    try:
        with open('processed_movie_counter.txt', 'r') as file:
            return int(file.read().strip())
    except:
        return 0
    
def update_processed_movie_counter(counter):
     # added by Chat GPT 
    with open('processed_movie_counter.txt', 'w') as file:
        file.write(str(counter))


def get_most_popular_movie(APIKEY):
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={APIKEY}&language=en-US&page=1'
    popular_movies = get_api_data(url)
    if popular_movies and 'results' in popular_movies and popular_movies['results']:
        most_popular_movie = popular_movies['results'][0] 
        return most_popular_movie.get('id')
    return None


def main():
    most_popular_movie_id = get_most_popular_movie(APIKEY)
    
    if most_popular_movie_id:
        movie_details = get_api_data(f'https://api.themoviedb.org/3/movie/{most_popular_movie_id}?api_key={APIKEY}&language=en-US', most_popular_movie_id)
        if movie_details:
            print("Most Popular Movie:")
            print_movie_details(movie_details)
            
            processed_overview = preprocess_text(movie_details.get('overview', ''))
            pos_tags = pos_tag(processed_overview)
            
            print("\nPOS Tags:")
            print(pos_tags[:10])
            
            word_counts = Counter(processed_overview)
            print("\nTop 10 most common words:")
            print(word_counts.most_common(10))
        else:
            print("Error fetching movie details.")
    else:
        print("Error fetching most popular movie.")
    
    current_minute = datetime.datetime.now().minute  # added by Chat GPT 
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={APIKEY}&language=en-US&page={current_minute}'
    
    movies = get_api_data(url)
    if not movies or 'results' not in movies:
        print("No movies found for the current minute.")
        return
    
    movie_ids = [movie['id'] for movie in movies['results'] if 'id' in movie]
    
    movie_id_to_process = random.choice(movie_ids)
    
    movie_details = get_api_data(f'https://api.themoviedb.org/3/movie/{movie_id_to_process}?api_key={APIKEY}&language=en-US', movie_id_to_process)
    if movie_details:
        print("\nRandom Movie:")
        print_movie_details(movie_details)
        
        processed_overview = preprocess_text(movie_details.get('overview', ''))
        pos_tags = pos_tag(processed_overview)
        
        print("\nPOS Tags:")
        print(pos_tags[:10])
        
        word_counts = Counter(processed_overview)
        print("\nTop 10 most common words:")
        print(word_counts.most_common(10))

if __name__ == "__main__":
    main()
