import urllib.request
import string
import gensim 
from gensim import corpora
import random
import nltk
import matplotlib.pyplot as plt
import spacy
import requests


#Download Packages for Text and Data clean-up:
# nltk.download('stopwords')
# nltk.download('vader_lexicon')
# nltk.download('punkt')

from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import WordCloud

#Welcome to my code for the Text Analysis Project
"""
I asked ChatGPT after reading through some of the different
examples of anaylzing the text, if it could come up with any
different suggestions. 
https://chat.openai.com/share/60f01db4-398b-4d92-934e-4816b6b64228

"""
#Part 1
#Data Source: Project Gutenberg, opens Frankenstein and Great Gatsby
import urllib.request

url = 'https://www.gutenberg.org/cache/epub/84/pg84.txt'
with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')
    # print(text) # for testing

url2 = 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt'
with urllib.request.urlopen(url2) as f:
    text2 = f.read().decode('utf-8')

#Cleaning the data set

def clean_data(text):
    """
    Function utilzies NLTK (Natural Language Toolkit to clean up the data/ words/ characters in the text)
    """
    #Part of code cleans up the text by removing spacing & punctuation
    text = text.translate(str.maketrans("","",string.punctuation))

    #Converts the text into lowercase characters
    text=text.lower()

    #Removes English stop words as defined by NLK (such as "the", "a", "an", "in", "i", "be", "what", "as") https://pythonspot.com/nltk-stop-words/
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    words = [word for word in words if word not in stop_words]

    return words

#Finds the total number of words in the text after cleaning it up after removing the Stop Words 
cleaned_words = clean_data(text)
total_words = len(cleaned_words)

print(f'Total number of words after cleaning the text for Frankenstein: {total_words}')

def find_most_common_words(url, num_words=50):
    """
    Function finds the 50 most common words utilized in the text
    """
    with urllib.request.urlopen(url) as f:
        text = f.read().decode('utf-8')
        

    #Cleans the text with function made before
    words = clean_data(text)

    #creates a distibution of the remaining words
    frequency_dist = FreqDist(words)

    #finds the most common words listing the number of times utilized
    common_words = frequency_dist.most_common(num_words)

    #Finds the the sentiment scores of the text: output should give the percentage of "neg" = negative, "neu" = neutral, "pos" = positive and the total of scores = 1.0
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    print(score)

    return common_words


def create_markov_text(text, order = 2, length=200):
    """
    Asked ChatGPT to help me add a Markov Text Synthesis into my current code. Markov Text Synthesis creates a mashup of the text

    https://chat.openai.com/share/1be2f0f2-e29b-417f-90e6-c95bedfa3bc1

    Had issues with the url2 not being defined orginally and asked ChatGPT for troublesooting help. Since the urls before were not defined seperately. 

    https://chat.openai.com/share/24597441-7192-4b14-9a00-b4c8d4b71ef1
    
    """
    words = text.split()

    #Creates a dictonary to store words
    transitions = {}
    for i in range(len(words) - order):
        context = tuple(words[i:i + order])
        next_word = words[i + order]
        if context not in transitions:
            transitions[context] = []
        transitions[context].append(next_word)

    #Starts the Markov text synthesis
    current_context = random.choice(list(transitions.keys()))
    generated_text = list (current_context)
    for _ in range(length):
        if current_context in transitions:
            next_word = random.choice(transitions[current_context])
            generated_text.append(next_word)
            current_context = tuple(generated_text[-order:])
        else:
            break

    return ' '.join(generated_text)

#Generates the Markov Text for the two text sources
url1_markov_text = create_markov_text(text, order = 2, length = 200)
url2_markov_text = create_markov_text(text2, order=2, length=200)

#Print the Markov Text from the respective source
print("Markov Text from the first source:")
print(url1_markov_text)

print("Markov Text from the second source:")
print(url2_markov_text)


def get_topics(url, num_topics=10, num_words = 10):
    """
    """
    words= clean_data(text)

    dictionary = corpora.Dictionary([words])

    corpus = [dictionary.doc2bow([words])]

    lda = gensim.models.ldamodel.LdaModel(corpus = corpus, id2word=dictionary, num_topics=num_topics, random_state=42)

    topics = lda.print_topic(num_words=num_words)

    print("Top {} topics from the text: \n".format(num_topics))
    for i, topic in enumerate(topics):
        topic_num = i + 1
        words = topic[1].split("+")
        words = [words.split("*")[1].replace('"','').strip() for word in words]
        print("Topic {}: {}\n".format(topic_num,",".join(words)))

def entity_recog():
    """
    Tried out one of ChatGPTs recommendations for a new way
    to anaylze the text.

    Link to ChatGPT questions to making the code: 

    https://chat.openai.com/share/60f01db4-398b-4d92-934e-4816b6b64228

    """
    source = 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt'
    response = requests.get(source)

    if response.status_code == 200:
        text = response.text
    else:
        print("Failed to retrieve text from the URL")
        return

    #Load the English NEW model
    nlp = spacy.load("en_core_web_sm")

    doc = nlp(text)

    person_entities = set()

    for entity in doc.ents:
        if entity.label_=="PERSON":
            person_entities.add(entity.text)
    if person_entities:
        print("List of unique Person entities:")
        for entity in person_entities:
            print(f"Entity: {entity}, Label: PERSON")
        else:
            print("No person entities found in the text")

#Runs the function labeling the entities:
entity_recog()

def visualization_cloud():
    """
    Asked ChatGPT for some visual methods to showcase
    the text analysis:
    https://chat.openai.com/share/144be43e-c2b8-40af-b414-4a1db53ed88f

    One of the methods recommended was a word cloud.
    Visualize the most frequent words in a text.

    Had a few issues after running the base code and adjusting and asked ChatGPT 
    for some guidance to resolve it:
    
    https://chat.openai.com/share/144be43e-c2b8-40af-b414-4a1db53ed88f

    """
    web_source = 'https://www.gutenberg.org/cache/epub/84/pg84.txt'
    response = requests.get(web_source)

    if response.status_code == 200:
        text = response.text

        #Convers the text into lowercase
        text = text.lower()


        wordcloud = WordCloud(width=800, height = 400, background_color="white")
        wordcloud.generate(text)

        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
    else:
        print("Failed to get data from the URL")
    
#Runs the function
visualization_cloud()

def plot_scatter(url):
    """
    Creates a scatter plot of four words in Frankenstien
    These words have literally meaning that the words have a deeper 
    meaning in terms of the context of the novel
    The words I picked were the words I used in my High School
    AP Lit class essay
    """
    #Takes the text from the url provided
    with urllib.request.urlopen(url)as f:
        text = f.read().decode('utf-8')

    words = word_tokenize(text.lower())

    #The words we are looking for
    target_words = ["evil", "light", "love", "life"]

    words_freqs = {word: 0 for word in target_words}

    #Counts the number of times the desired words are used
    for word in words:
        if word in target_words:
            words_freqs[word] += 1

    #Builds scatter plot
    x_vals = list(range(len(target_words)))
    y_vals = [words_freqs[word]for word in target_words]

    fig, ax = plt.subplots()
    ax.scatter(x_vals, y_vals)

    #Adds labels to the x-axis
    ax.set_xticks(x_vals)
    ax.set_xticklabels(target_words)

    #Adds labels to the y-axis
    ax.set_ylabel("Frequency")
    ax.set_title("Occurences of words with textual meanings")

    plt.show()

#URLs used in this homework:

url = 'https://www.gutenberg.org/cache/epub/84/pg84.txt'
common_words = find_most_common_words(url, num_words=50)
print(common_words)


url2 = 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt'
with urllib.request.urlopen(url2) as f:
    text2 = f.read().decode('utf-8')
    # print(text)


url2 = 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt'
common_words2 = find_most_common_words(url2, num_words=50)
print(common_words2)


url = 'https://www.gutenberg.org/cache/epub/84/pg84.txt'
plot_scatter(url)

topics = get_topics(url, num_topics =8, num_words =10)
for topic in topics:
    print(topic)

if __name__ == "__main__":
    visualization_cloud()
    entity_recog()
