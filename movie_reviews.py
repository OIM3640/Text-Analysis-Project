from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ia = Cinemagoer()

# search movie IDs 
# Creed I movie id: 3076658
movie = ia.search_movie("Creed (2015)")[0]
print(movie.movieID)
# Creed II movie id: 6343314
movie = ia.search_movie("Creed 2")[0]
print(movie.movieID)
# Creed III movie id: 11145118
movie = ia.search_movie("Creed 3")[0]
print(movie.movieID)

# movie_reviews = ia.get_movie_reviews('3076658')
# print(movie_reviews['data']['reviews'][0]['content'])
