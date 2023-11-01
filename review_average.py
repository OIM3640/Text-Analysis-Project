from imdb import Cinemagoer
import matplotlib.pyplot as plt

'''
This code searches for a movie, and retrieves the reviews for the movie and checks if they have ratings.
if they do it finds the average out of all the ratings.
'''

# create an instance of the Cinemagoer class
ia = Cinemagoer()
# search movie
movie = ia.search_movie("Frozen")[0]

#get the first # of reviews
reviews = ia.get_movie_reviews(movie.movieID)['data']['reviews']
reviews = reviews[:11]

#empty list to store the ratings
ratings = [] 

#loop through each review and if it has a rating, append it to the list
for review in reviews: 
    rating = review.get('rating')
    if rating:
        ratings.append(rating)      

#calculate the average rating 
if len(reviews) >0:
    average_rating = sum(ratings)/ len(ratings)
    print(f"The average rating of the first {len(ratings)} reviews is {average_rating:.2f}.")

#if there are no reviews then print no reviews were found
else:
    print(f"No reviews found")


