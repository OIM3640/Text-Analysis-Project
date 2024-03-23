# Author: Adrien Schaal
# Date: 2024-03-22
# Description: This script fetches top headlines in the business and technology categories from the News API,

# Import the necessary libraries to fetch news articles url and theiur content
from newsapi import NewsApiClient
from newspaper import Article

# Import the necessary libraries for text processing
import nltk
from collections import Counter

# Download the list of stop words from NLTK
# Stop words are words which are filtered out before or after processing of text.
# Stop words might be words that are too common or not relevant like 'and', 'the', 'a', etc.
nltk.download('stopwords')
from nltk.corpus import stopwords

# Download the English tokenizer from Spacy for named entity recognition
# Named entity recognition (NER) is a subtask of information extraction that
# seeks to locate and classify named entities in text into pre-defined categories 
# such as the names of persons, organizations, locations, expressions of times, quantities, monetary values, percentages, etc.

import spacy
# Load Spacy's English tokenizer, tagger, parser, NER, and word vectors
# This model needs to be downloaded using the following command:
# python -m spacy download en_core_web_sm
# Source: https://stackoverflow.com/questions/54334304/spacy-cant-find-model-en-core-web-sm-on-windows-10-and-python-3-5-3-anacon
nlp = spacy.load("en_core_web_sm")

def perform_ner(text):
    """
    Perform named entity recognition (NER) on the input text using Spacy's NLP pipeline.
    """
    
    # Process the combined text through Spacy's NLP pipeline
    doc = nlp(text)
    
    # Initialize a dictionary to hold entities. People, Organizations, and Geopolitical Entities
    entities = {"PERSON": [], "ORG": [], "GPE": []}
    
    # Iterate over the entities in the document
    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].append(ent.text)
    
    # Removing duplicates
    for entity_type in entities:
        entities[entity_type] = list(set(entities[entity_type]))
    
    return entities


def main():
    # Init
    newsapi = NewsApiClient(api_key='f02d4005830c43fbbd6ff20629c3cdc1')

    # Fetch business news
    top_headlines_business = newsapi.get_top_headlines(category='business',
                                                       language='en',
                                                       country='us')

    # Fetch technology news
    top_headlines_technology = newsapi.get_top_headlines(category='technology',
                                                         language='en',
                                                         country='us')

    # Merge business and technology articles
    all_articles = top_headlines_business['articles'] + top_headlines_technology['articles']

    # Initialize an array to hold all articles' content
    articles_content = []
    number_articles_not_found = 0
    # Iterate over merged articles
    for article in all_articles:
        try:
            # Create Article object
            article_obj = Article(article['url'])
            
            # Download and parse the article
            article_obj.download()
            article_obj.parse()
            
            # Append the article's text to the articles_content array
            articles_content.append(article_obj.text)
        except Exception as e:
            number_articles_not_found += 1

    if articles_content:
        print()
        print("Total number of articles found in both business and technology (top headlines):", len(articles_content))
        print()
        print("Number of articles not found using newspaper API:", number_articles_not_found)

        # Combine all articles into a single text for analysis
        combined_text = " ".join(articles_content).lower()

        # Get the list of stopwords for a particular language, e.g., English
        stop_words = list(stopwords.words('english'))

        # Define additional stopwords that do not add to the analysis
        new_stop_words = ['like', 'also', 'would', 'see']

        # Extend the original list with your new stopwords
        stop_words.extend(new_stop_words)

        # Tokenize the combined text and filter out stop words and non-alphabetic words
        words = combined_text.split()
        words_filtered = [word for word in words if word.isalpha() and word not in stop_words]

        # Count the frequency of each word
        word_frequencies = Counter(words_filtered)

        # Compute summary statistics
        print("\nTop 10 most frequent words in the combined set of articles:")
        for word, frequency in word_frequencies.most_common(10):
            print(f"{word}: {frequency}")

        # Perform named entity recognition (NER) on the combined text
        entities = perform_ner(combined_text)

        # Add a newline for better readability between entity types
        print()  

        # Print extracted entities
        for entity_type, entity_list in entities.items():
            print(f"{entity_type}: {len(entity_list)} entities")
            for entity in entity_list[:10]:  # Print only the first 10 for brevity
                print(f" - {entity}")
            print()  # Add a newline for better readability between entity types
    else:
        print("No articles were processed.")

if __name__ == "__main__":
    main()