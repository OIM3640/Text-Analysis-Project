#Retrieve the first review for the movie "Dead Poets Society"
from imdb import Cinemagoer

ia = Cinemagoer()

movie = ia.search_movie("Dead Poets Society")[0]
print(movie.movieID)
#0097165

movie = ia.get_movie('0097165', info=['reviews']) # Make sure to add the second argument
reviews = movie.get('reviews', [])

#Creates a list of words for the first review
moviereview = []
for review in reviews:
    print(review['content'])
    print()
    moviereview.append(review["content"])

# Start Pickling Data
import pickle

with open('moviereview.pkl','wb') as f:
    pickle.dump(moviereview,f)
    
with open('moviereview.pkl','rb') as f:
    reloaded_copy_of_texts = pickle.load(f)
    
# print(reloaded_copy_of_texts)

# Part 2:
# Characterizing by Word Frequencies

