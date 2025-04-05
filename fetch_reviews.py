from imdb import Cinemagoer
import os

def get_reviews(movie_name, max_reviews=20):
    ia = Cinemagoer()
    search_results = ia.search_movie(movie_name)
    movie = search_results[0]
    movie_id = movie.movieID

    movie_info = ia.get_movie(movie_id, info=['reviews'])
    reviews = movie_info.get('reviews', [])
    
    texts = []
    for review in reviews[:max_reviews]:
        texts.append(review['content'])
    
    return texts

def save_reviews(movie_name, reviews):
    folder = 'reviews'
    os.makedirs(folder, exist_ok=True)
    file_name = movie_name.lower().replace(' ', '_') + '.txt'
    
    with open(os.path.join(folder, file_name), 'w', encoding='utf-8') as f:
        for review in reviews:
            f.write(review + '\n\n')

def main():
    movie_list = ["The Dark Knight", "Inception", "Interstellar", "Avengers: Endgame"]
    
    for movie in movie_list:
        print(f"Getting reviews for {movie}...")
        reviews = get_reviews(movie)
        save_reviews(movie, reviews)

if __name__ == "__main__":
    main()
