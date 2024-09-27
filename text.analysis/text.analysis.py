#Text Analysis Assignment

#Importing Great Gatsby through Project Gutenberg API
import urllib.request
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import re
from collections import Counter
from nltk.sentiment import SentimentIntensityAnalyzer
import spacy
import openai


def downlaod_book():
    """
    function downloads book, The Great Gatsby, from Project Gutenberg
    """
    url = 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt'
    with urllib.request.urlopen(url) as f:
        text = f.read().decode('utf-8')
        return text


#Removing the unnecessary text from book 
def remove_unnecessary_text(text):
    """
    Function removes unnecessary text from the text 
    sets a start and end point of the text to analyze
    """
    start_of_book= "*** START OF THE PROJECT GUTENBERG EBOOK THE GREAT GATSBY ***"
    end_of_book= "*** END OF THE PROJECT GUTENBERG EBOOK THE GREAT GATSBY ***"

    start_point= text.find(start_of_book)
    end_point= text.find(end_of_book)

    #need this to confirm the start and end points have been found in text
    if start_point != -1 and end_point != -1:
        book= text[start_point + len(start_of_book):end_point].strip()
        return book
    else:
        return text



#Text Analysis 
#Text Preprocessing


def preprocess_text(book):
    """
    Function cleans text so it can be analyzed 

    Uses NLTK package to:
    Tokenize text into words
    Removes punctuation and makes words lowercase
    Removs common stop words
    Lemmatizes words to their base form
    Removes hyphens and replaces special characters with spaces
    Joins the cleaned words into a single string
    """
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')

    words= nltk.word_tokenize(book)

    words = [word for word in words if word not in string.punctuation]

    words = [word.lower() for word in words]

    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]


    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]

    book = " ".join(words)

    #FROM CHATGPT, supposed to remove " or ' but it is not working
    # cleaned_book = re.sub(r'-+', ' ', book)
    # cleaned_book = re.sub(r'[“”’]', ' ', cleaned_book)

    lines = book.splitlines()

    cleaned_lines = []
    for line in lines:
        line = line.replace('-', ' ')
        line = line.replace(chr(8212), ' ')
        cleaned_lines.append(line)

    cleaned_book = '\n'.join(cleaned_lines)

    return cleaned_book




def total_words(cleaned_text):
    """
    Returns the total word count in the cleaned text. 
    """
    words = cleaned_text.split()  
    return len(words)  



def word_frequency(cleaned_text, custom_stopwords=[]):
    """
    Returns a dictionary of word frequencies in the text
    """
    words = cleaned_text.split()
    stop_words = set(stopwords.words('english') + custom_stopwords)
    words = [word for word in words if word.lower() not in stop_words]

    word_freq = Counter(words)
    return word_freq




def perform_sentiment_analysis(text):
    """
    Function uses NLTK package to perform a sentiment analysis of the book
    recieves a sentiment score, above 0.05 is positive, under -0.05 is negative
    anything in the middle is neutral
    """
    nltk.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()

    sentiment_scores = sia.polarity_scores(text)

    compound_score = sentiment_scores['compound']
    if compound_score >= 0.05:
        sentiment_label = "Positive"
    elif compound_score <= -0.05:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"
    return sentiment_scores, sentiment_label


def perform_ner_analysis(text):
    """
    Function performs Named Entity Recognition (NER) analysis on the text
    classifies named entities as person, place, date, etc.
    stores in dictionary with keys
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    named_entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    return named_entities


def find_people(text):
    """
    Find and extract all people from the NER dictionary
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    people = [ent.text for ent in doc.ents if ent.label_ == 'PERSON']
    
    return people



def generate_text(prompt, max_tokens= 100):
    """
    Function uses the OpenAI API key to have ChatGPT perform a text creation 
    Prompt, max tokens are taken in 
    prompt is the guide for ChatGPT 
    Max Tokens is number of words generated
    """
    api_key= "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"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=max_tokens,
        api_key=api_key,
    )

    generated_text= response.choices[0].text
    return generated_text



def main():
    text= downlaod_book()

    book= remove_unnecessary_text(text)

    cleaned_book= preprocess_text(book)

    word_count = total_words(cleaned_book)
    print(f"Total words in the text: {word_count}")


    word_frequencies = word_frequency(cleaned_book)
    most_common_words = word_frequencies.most_common(30)
    print("30 most common words and their frequencies:")
    for word, frequency in most_common_words:
        print(f"{word}: {frequency}")

    
    sentiment_scores, sentiment_label = perform_sentiment_analysis(cleaned_book)
    print("Sentiment Scores:", sentiment_scores)
    print("Sentiment Label:", sentiment_label)


    ner_results = perform_ner_analysis(cleaned_book)
    print("Named Entities:", ner_results)


    people_found = find_people(cleaned_book)
    print("People in the text:", people_found)

    #last line of The Great Gatsby, wanted a continuation of the text
    prompt = "So we beat on, boats against the current, borne back ceaselessly into the past."
    generated_text = generate_text(prompt)
    print("Generated Text:")
    print(generated_text)


if __name__ == "__main__":
    main()


