from imdb import Cinemagoer  # Importing the Cinemagoer class to interact with IMDb data
from datetime import datetime  # Used for parsing and formatting release dates

ia = Cinemagoer()  # Creating an instance of the IMDb API client

results = ia.search_movie('Animation')  # Searching IMDb for movies with the keyword "Animation"

animated_movies = []  # List to store filtered animated movie data

# Loop through each search result to find animated movies
for movie in results:
    try:
        movie_id = movie.movieID  # Extracting the unique movie ID from the result
        full_movie = ia.get_movie(movie_id)  # Fetching full movie details using the movie ID

        # Filtering for movies that are actually categorized as "Animation" and of type "movie"
        if 'Animation' in full_movie.get('genres', []) and full_movie.get('kind') == 'movie':
            # Attempt to get the release date; fallback to year if detailed date is not available
            release_date = full_movie.get('original air date') or full_movie.get('year')

            parsed_date = None  # Initialize parsed date variable
            if isinstance(release_date, str):  # If the release date is a string (e.g., "12 June 2021")
                try:
                    # Parse the string into a date object using the expected format
                    parsed_date = datetime.strptime(release_date, "%d %B %Y").date()
                except ValueError:
                    pass  # If parsing fails, keep parsed_date as None

            # Append the relevant movie info to the animated_movies list
            animated_movies.append({
                'title': full_movie.get('title'),  # Movie title
                'movieID': full_movie.movieID,  # IMDb movie ID
                'genres': full_movie.get('genres', []),  # List of genres
                'year': full_movie.get('year'),  # Release year
                'release_date': parsed_date,  # Parsed release date
            })
    except Exception as e:
        # Print any errors that occur while fetching or parsing a movie
        print(f"Error fetching movie: {e}")

# Loop through the first 10 animated movies in the list to display info and fetch reviews
for movie in animated_movies[:]:
    print(f"\n🎬 {movie['title']} ({movie['year']})")  # Display movie title and year
    print(f"📅 Release Date: {movie['release_date']}")  # Display parsed release date
    print(f"🎭 Genres: {', '.join(movie['genres'])}")  # Display genres as a comma-separated list

    try:
        # Fetch reviews for the current movie using its IMDb ID
        reviews = ia.get_movie_reviews(movie['movieID'])
        review_list = reviews.get('data', {}).get('reviews', [])  # Safely get the list of reviews

        # If reviews are available, print the first one (up to 300 characters)
        if review_list:
            print(f"📝 Review: {review_list[0].get('content', '')[:300]}...\n")
        else:
            print("📝 Review: No reviews available.\n")  # Message if no reviews found
    except Exception as e:
        # Handle any errors that occur while fetching reviews
        print(f"Could not get reviews for {movie['title']}: {e}")





