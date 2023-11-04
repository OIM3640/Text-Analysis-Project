import urllib.request
import json
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
import string
from collections import Counter

APIKEY = '34686ac4ab5866863e5cd49de96ce446'

def make_api_request(url):
    try:
        with urllib.request.urlopen(url) as f:
            response_text = f.read().decode('utf-8')
            response_data = json.loads(response_text)
            return response_data
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_movie_overviews(APIKEY, num_pages=1):
    overviews = []
    base_url = 'https://api.themoviedb.org/3/movie/popular'
    
    for page in range(1, num_pages + 1):
        url = f'{base_url}?api_key={APIKEY}&language=en-US&page={page}'
        response_data = make_api_request(url)
        if response_data and 'results' in response_data:
            overviews.extend(movie['overview'] for movie in response_data['results'] if 'overview' in movie)
            
    return overviews

def get_movie_details(APIKEY, movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={APIKEY}&language=en-US'
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        movie_details = json.loads(response_text)
        return movie_details

def preprocess_text(text):
    stopwords_ = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    processed_text = [w for w in words if w not in string.punctuation and w not in stopwords_ and len(w) > 1 and w != "the"]
    return processed_text


def get_counts(texts):
    return Counter(texts)

def print_highest_count(counts, k):
    highest_counts = counts.most_common(k)
    for word, count in highest_counts:
        print(f"{word:10} was found {count:5} times")
    return highest_counts

def get_pos_tags(words):
    return nltk.pos_tag(words)

def main():
    overviews = get_movie_overviews(APIKEY)
    print(overviews)
    
    if overviews:
        processed_overviews = preprocess_text(' '.join(overviews))
        pos_tags = get_pos_tags(processed_overviews)
        

        print("\nPOS Tags:")
        print(pos_tags[:10])
        
        word_counts = get_counts(processed_overviews)
        print("\nTop 10 most common words:")
        print_highest_count(word_counts, 10)
        
        movie_details = get_movie_details(APIKEY, 700)
        if movie_details:
            print("\nMovie Details:")
            print(json.dumps(movie_details, indent=4))

if __name__ == "__main__":
    main()
