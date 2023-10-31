"""

Have you ever thought of reading philosophy? Have you been too afraid to start one of these hefty books because you're afraid you might end up losing your mind and becoming a doomer? 

This tool will help bring clarity on the rumors stating Russian philosophy is extra dark, or scary, or whatever word you want to use.

We will look at 19th century novelist Fyodor Dostoevsky's top 5 works and do a sentiment analysis of each text. The tool will give each book a score of how negative 'neg', neutral 'neu', and postive 'pos' the text in each book is.

After doing so, you can then make an informed decision if you want to continue down this path of enlightenment via Dostoevsky's works.

Let us begin.   |
                |
                V

"""


"""
STAGE 0 - COLLECT DATA
"""

# Here is where all the book txt files are pulled into the file:
notes_from_underground_raw = open('data/notesfromunderground.txt', encoding='UTF8')
crime_and_puinishment_raw = open('data/crimeandpunishment.txt', encoding='UTF8')
brothers_karamazov_raw = open('data/thebrotherskaramazov.txt', encoding='UTF8')
the_idiot_raw = open('data/theidiot.txt', encoding='UTF8')
the_possessed_raw = open('data/thepossessed.txt', encoding='UTF8')


"""
STAGE 1 - CLEAN THE DATA
"""

# Here we will import the string library for precreated lists of punctuation to strip from the text
import string

def clean_book(book_raw):

    """
    This function takes in a book's raw text and punctuation and cleans it to be text without punctuation or quotes, etc., and makes all words lower case.
    """

    # Read the content within the txt files
    content = book_raw.read()

    # Replace line breaks with spaces in content
    content = content.replace('\n', ' ')

    # Remove punctuation, double quotes, apostrophies from content
    for char in string.punctuation + '“”‘’':
        content = content.replace(char, '')

    # Convert all words to lowercase in content
    content = content.lower()

    # Splits the text content into individual words and joins those words with a single space between each word
    return ' '.join(content.split())


# Now we will store all cleaned books here:
notes_clean = clean_book(notes_from_underground_raw)
crime_clean = clean_book(crime_and_puinishment_raw)
brothers_clean = clean_book(brothers_karamazov_raw)
idiot_clean = clean_book(the_idiot_raw)
possessed_clean = clean_book(the_possessed_raw)


# Here we will import nltk or 'Natural Language Tool Kit' stopwords to do NLP analysis:
from nltk.corpus import stopwords


# Stores the set of stopwords
stop_words = set(stopwords.words('english'))


# We will use stopwords in this library to clean the text of all non-meaningful words here:
def remove_stop_words(text):

    """
    This function takes in the cleaned texts from above and then cleans them further of stop words that will impact our analysis, it returns the text in it's final format.
    """

    words = text.split()
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)


# Storing all books/text after removing stop words.
notes = remove_stop_words(notes_clean)
crime = remove_stop_words(crime_clean)
brothers = remove_stop_words(brothers_clean)
idiot = remove_stop_words(idiot_clean)
possessed = remove_stop_words(possessed_clean)


# Store all cleaned books in a list of tuples with titles:
books = [('Notes from the Underground', notes), ('Crime and Punishment', crime), ('The Brothers Karamazov', brothers), ('The Idiot', idiot), ('The Possessed', possessed)]


"""
STAGE 2 - ANALYZE THE DATA
"""


# DO SOME NLP!!!!!
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# Here we will analyze the sentiment of each book:
def do_nlp(books):

    """
    This function takes in the list of books and their titles and then performs NLP on each book, it prints the sentiment score of each book and its title when ran.
    """

    for title, book in books:
        text = book
        score = SentimentIntensityAnalyzer().polarity_scores(text)
        print(f'The Sentiment Score of "{title}" is: {score}')

    
def main():
    print("Let's analyze the sentiment of Russian novelist Fyodor Dostoevsky's 5 greatest works: ")
    do_nlp(books)

if __name__ == '__main__':
    main()