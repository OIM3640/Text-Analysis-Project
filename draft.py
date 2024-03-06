from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ia = Cinemagoer()

# search for a person name
people = ia.search_person('Matt Damon')
for person in people:
   print(person.personID, person['name'])


movie = ia.get_movie('0119217')
movie = ia.get_movie('0119217', info=['reviews'])

reviews = movie.get('reviews', [])
print(type(reviews), len(reviews))

for review in reviews:
    print(review['content'])
    print()

# Create an IMDb object
moviesDB = imdb.IMDb()

# Search for the movie "The Martian"
movie_title = "The Martian"
search_results = moviesDB.search_movie(movie_title)

# Extract the IMDb ID of the first search result (assuming it's the movie you're looking for)
if search_results:
    imdb_id = search_results[0].movieID
    print(f"IMDb ID for 'The Martian': {imdb_id}")
else:
    print("Movie not found.")


# Search for movies featuring Matt Damon (IMDb ID: 0000354)
matt_damon_id = "0000354"
movies_with_matt_damon = Cinemagoer.search_movies_by_actor_id(matt_damon_id)

# Print the list of movies
for movie in movies_with_matt_damon:
    print(movie['title'])


moviesDB = imdb.IMDb()

#PeterDinklage IMDB ID
ActorId = "0000354"
person = moviesDB.get_person(ActorId)
#Actor's name
print (person)
actor_work = moviesDB.get_person_filmography(ActorId)
for movie in actor_work['data']['filmography']['actor'] :
    try:
        print (movie.movieID, movie['title'], movie.currentRole, movie['year'])
    except KeyError:
        #print("No Year for the movie")
        print (movie.movieID, movie['title'], movie.currentRole)

