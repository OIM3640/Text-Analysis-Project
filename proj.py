from imdb import Cinemagoer
import nltk
nltk.download('vader_lexicon'), nltk.download('popular')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize

# create an instance of the Cinemagoer class
ia = Cinemagoer()
# search movie
movie = ia.search_movie("interstellar")[0]
print(movie.movieID)
# '0816692'
movie_reviews = ia.get_movie_reviews('0816692')

def summarize_text(text):
    """Corpus
Corpus means a collection of text. It could be data sets of anything containing texts be it poems by a certain poet, bodies of work by a certain author, etc. In this case, we are going to use a data set of pre-determined stop words.
Tokenizers
it divides a text into a series of tokens. There are three main tokenizers – word, sentence, and regex tokenizer. We will only use the word and sentence tokenizer"""    
    # Initialize a set of English stop words
    stopWords = set(stopwords.words("english"))

    # Tokenize the text into words and sentences
    words = word_tokenize(text)
    sentences = sent_tokenize(text)

    # Initialize dictionaries for word frequencies and sentence scores
    freqTable = dict()
    sentenceValue = dict()

    # Count the frequency of each non-stop word in the text
    for word in words:
        word = word.lower()
        if word not in stopWords:
            freqTable[word] = freqTable.get(word, 0) + 1

    # Score sentences based on word frequencies
    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                sentenceValue[sentence] = sentenceValue.get(sentence, 0) + freq

    # Calculate the average score for sentences
    sumValues = sum(sentenceValue.values())
    average = int(sumValues / len(sentenceValue)) if sentenceValue else 0

    # Generate summary: sentences with a score above 1.2 times the average score
    summary = ''
    for sentence in sentences:
        if sentence in sentenceValue and sentenceValue[sentence] > (1.2 * average):
            summary += " " + sentence

    return summary.strip()  # Return the summary without leading/trailing spaces
def summarize_reviews(movie_title):
    ia = Cinemagoer()
    movies = ia.search_movie(movie_title)

    if not movies:
        print(f"No results found for '{movie_title}'")
        return

    movie = movies[0]
    movie_id = movie.movieID
    movie_reviews = ia.get_movie_reviews(movie_id)

    for review in movie_reviews['data']['reviews']:
        content = review['content']
        summary = summarize_text(content)
        #print("Original Review:", content)
        print("------------------------------------------Summary:", summary)
        print("__________________------------___________________________________________")
def count_good_in_reviews(movie_title):
    """
    Count how many times the word 'good' is mentioned in the reviews of a specific movie.
    movie_title: Title of the movie to search for.
    return: Number of occurrences of the word 'good'.
    """
    # search for the movie return 0 if the movie title is not found
    movies = ia.search_movie(movie_title)
    if not movies:
        print(f"No results found for '{movie_title}'")
        return 0
    
    # select the first match we take the first result 
    # (which is the most likely to be the one we're looking for)
    # and retrieve its movieID
    movie = movies[0]
    movie_id = movie.movieID

    # get movie reviews
    movie_reviews = ia.get_movie_reviews(movie_id)

    # initialize a counter made from a dictionary for occurrences of the word
    word_counts = {'good': 0, 'great': 0, 'awesome': 0, 'amazing': 0, 'perfect': 0}
    total_reviews = 0
    # iterate through each review
    for review in movie_reviews['data']['reviews']:
        # and ensuring 'good' is a whole word
        total_reviews += 1
        content = review['content'].lower() #lower it so that all matches are without uppercase boundaries
        #Get the text content of the review
        for word in word_counts: # loop that iterates over the keys of the word_counts dictionary. On each iteration, the variable word will hold one of the keys from the dictionary.
            # Split the content into words and count how many times word appears
            #content.split(): This method splits the content string into a list of words based on whitespace. 
            word_counts[word] += content.split().count(word)
            #.count(word): The count method is called on the list of words obtained from the split operation.
            # It returns the number of times the specified word appears in that list.
    print("-----------------------------------------") 
    print(f"In the movie {movie_title} reviews:")
    for word, count in word_counts.items():
        if count == 0:
            print(f"The word '{word}' is mentioned 0 times")
        else:
            print(f"The word '{word}' is mentioned {count} times")
    print(f"Total number of reviews analyzed: {total_reviews}")
    print("===========================================================")
def sentiment_in_reviews(movie_title):
 """
    Print each review for the specified movie and its sentiment (negative, neutral, or positive).

    movie_title: Title of the movie to search for."""
 movies = ia.search_movie(movie_title)
 sentiment_counts = {"Positive": 0, "Neutral": 0, "Negative": 0} #list for negative pozitive neut counter

 if not movies:
        print(f"No results found for '{movie_title}'")
        return
 movie = movies[0]
 movie_id = movie.movieID
 # select the first match we take the first result 
    # (which is the most likely to be the one we're looking for)
    # and retrieve its movieID
 movie_reviews = ia.get_movie_reviews(movie_id) #get the movie reviews
 sid = SentimentIntensityAnalyzer() #an instance of the SentimentIntensityAnalyzer

 for review in movie_reviews['data']['reviews']:
        content = review['content'] #the text content of the review
        
        sentiment_scores = sid.polarity_scores(content) # calculate sentiment scores
        compound_score = sentiment_scores['compound'] #determine the overall sentiment based on compound score
        
        if compound_score >= 0.05:
            sentiment = "Positive"
            sentiment_counts["Positive"] += 1
        elif compound_score <= -0.05:
            sentiment = "Negative"
            sentiment_counts["Negative"] += 1
        else:
            sentiment = "Neutral"
            sentiment_counts["Neutral"] += 1
        
        print("Review:", content)
        print("------------------------------------------------------------>")
        print("Sentiment:", sentiment)
        print("_____________________________________________________________")
        
        print("Review:", content)
        print("------------------------------------------------------------>")
        print("Sentiment:", sentiment)
        print("_____________________________________________________________")
    
 print(f"Total Positive: {sentiment_counts['Positive']}")
 print(f"Total Neutral: {sentiment_counts['Neutral']}")
 print(f"Total Negative: {sentiment_counts['Negative']}")

sentiment_in_reviews("Interstellar")
summarize_reviews("Interstellar")
count_good_in_reviews('Interstellar')