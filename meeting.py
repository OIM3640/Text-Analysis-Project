from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ia = Cinemagoer()


def get_actor(name):
    """get actor id by name"""
    people = ia.search_person('Matt Damon')
    for person in people:
        print(person.personID, person['name'])

# print(get_actor('matt damon'))

def get_films_by_actor(actor_id):
    """return a list of movie ids"""

    person = ia.get_person(actor_id)
    # Actor's name
    print(person)

    actor_work = ia.get_person_filmography(actor_id)
    film_ids = []
    for movie in actor_work["data"]["filmography"]["actor"]:
        try:
            # print(movie.movieID, movie["title"], movie.currentRole, movie["year"])
            film_ids.append(movie.movieID)
        except KeyError:
            print("No Year for the movie")
            print(movie.movieID, movie["title"], movie.currentRole)
    return film_ids


def get_review(movie_id):
    """get reviews of movies with Matt Damon"""
    movie = ia.get_movie(movie_id, info=['reviews'])
    reviews = movie.get('reviews', [])
    # print(type(reviews), len(reviews))
    master_review = ""
    for review in reviews:
        master_review ++ "review['content']"
    
    return master_review
        


# movie_id = '3659388'
# get_review(movie_id)


movie_ids= ['5079448', '24169886', '11152168', '19356262', '15398776', '16419074', '10648342', '4244994', '10696896', '11525644', '6521876', '1950186', '9881938', '0072562', '5463162', '7153766', '14279324', '3501632', '0491175', '1389072', '2034800', '4196776', '5364898', '3659388', '5520670', '5520656', '0320037', '0816692', '2177771', '2333804', '1535108', '14786186', '1291580', '1797404', '2091473', '1389137', '1402488', '0466893', '1598778', '1385826', '0496424', '1403865', '1212419', '0947810', '1792654', '1057500', '0387199', '1130080', '0876563', '0374569', '18304820', '0481797', '0169414', '0440963', '0496806', '0343737', '0407887', '0365737', '0401623', '0355295', '0275140', '0349903', '0372183', '0300051', '0356150', '0338466', '0270288', '0285341', '0258463', '0202623', '0166813', '0157246', '0302674', '0268995', '0240772', '0261392', '27658541', '0149624', '0181536', '0146984', '0120913', '0134119', '0120655', '0128442', '0120815', '0119217', '0119978', '0118842', '0115956', '0116422', '0113196', '0107004', '0105327', '0100497', '0097351', '0095238', '0095690']

from nltk.sentiment.vader import *


def get_review_sentiment(review):
    """creates a polarity score of the reviews"""
    score = SentimentIntensityAnalyzer().polarity_scores(review)
    print(score)

def get_avg_sentiment(movie):
    """"""


def main():
    """"""
    # matt = get_actor('Matt Damon')
    # print(matt)
    # matt = "0000354"
    # film_list = get_films_by_actor(matt)
    # print(film_list)
    review_sentiment_scores = {}

    for review in movie_ids:
        review_sentiment_scores[review] = get_review_sentiment(get_review(review))


if __name__ == "__main__":
    main()
