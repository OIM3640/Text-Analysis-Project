from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ia = Cinemagoer()

# get a movie
movie = ia.get_movie('0119217')

 # print the names of the directors of the movie
print('Actors:')
for actors in movie['actors']:
     print(actors['name'])

# # print the genres of the movie
# print('Genres:')
# for genre in movie['genres']:
#     print(genre)

 # search for a person name
people = ia.search_person('Mel Gibson')
for person in people:
    print(person.personID, person['name'])

movie = ia.get_movie('0119217', info=['reviews'])

reviews = movie.get('reviews', [])
print(type(reviews), len(reviews))

for review in reviews:
    print(review['content'])
    print()


