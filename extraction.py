from imdb import Cinemagoer
from datetime import datetime

ia = Cinemagoer()

# Initialize the list to store animated movies
drama_movies = []

try:
    # Fetch the top 250 movies
    top_movies = ia.get_top250_movies()
    print(f"Fetched {len(top_movies)} movies")

    if not top_movies:
        print("No movies fetched. Please check the API call or your internet connection.")
    else:
        # Loop through the fetched movies and filter by genre 'Animation'
        for movie in top_movies:
            try:
                movie_id = movie.movieID  # Get IMDb movie ID
                full_movie = ia.get_movie(movie_id)  # Fetch full movie details

                # Debugging: Print movie title and genres
                print(f"Processing movie: {full_movie.get('title')}, Genres: {full_movie.get('genres', [])}")

                # Check if the movie belongs to the 'Animation' genre
                if 'Drama' in full_movie.get('genres', []) and full_movie.get('kind') == 'movie':
                    release_date = full_movie.get('original air date') or full_movie.get('year')
                    parsed_date = None

                    if isinstance(release_date, str):
                        try:
                            parsed_date = datetime.strptime(release_date, "%d %B %Y").date()
                        except ValueError:
                            try:
                                parsed_date = datetime.strptime(release_date, "%Y-%m-%d").date()
                            except ValueError:
                                pass

                    # Append the animated movie to the list
                    drama_movies.append({
                        'title': full_movie.get('title'),
                        'movieID': full_movie.movieID,
                        'genres': full_movie.get('genres', []),
                        'year': full_movie.get('year'),
                        'release_date': parsed_date,
                    })
                    print(f"Added {full_movie.get('title')} to drama_movies list")
            except Exception as e:
                print(f"Error processing movie {movie_id}: {e}")
except Exception as e:
    print(f"Error fetching top movies: {e}")

# Display first 10 animated movies with reviews
for movie in drama_movies[:10]:
    print(f"\n🎬 {movie['title']} ({movie['year']})")
    print(f"📅 Release Date: {movie['release_date']}")
    print(f"🎭 Genres: {', '.join(movie['genres'])}")

    try:
        reviews = ia.get_movie_reviews(movie['movieID'])
        review_list = reviews.get('data', {}).get('reviews', [])
        if review_list:
            print(f"📝 Review: {review_list[0].get('content', '')[:300]}...\n")
        else:
            print("📝 Review: No reviews available.\n")
    except Exception as e:
        print(f"Could not get reviews for {movie['title']}: {e}")

