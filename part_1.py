import urllib.request
import re
import matplotlib.pyplot as plt
import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('vader_lexicon')
#process text1
url = 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt'
with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')
   

text= text.lower()
text= text.strip()


#remove punctuation from the text 
text = re.sub(r'[^\w\s]', '', text)


#compile stop words and other unnecessary words into a list
unnecessary_stop_words = ['said','came', 'and', 'all','who','would','im','them','their','the', 'to', 'of', 'a', 'in', 'that', 'is', 'it', 'for', 'on','ebook','gutenberg','ii','iii','iv','v','vi','vii','viii','this','i','he','was','you','his','at','her','had','she','me','as','from','my','but','we','us','an','him','were','there','if','or','by','with','into','they','so', 'be', 'when', 'what', 'not','like','are','have','had', 'about', 'then', 'do', 'dont', 'its', 'your', 'no']

def freq(text):
    '''calculate the frequency of words that appear in the text'''
    d={}
    text=text.split()
    for word in text:
        d[word] = d.get(word,0)+1
    return d

word_frequency_1=freq(text)

#remove stop words from frequency dictionary
for stop_word in unnecessary_stop_words:
    if stop_word in word_frequency_1:
        del word_frequency_1[stop_word]



#process text2
url2='https://www.gutenberg.org/cache/epub/805/pg805.txt'
with urllib.request.urlopen(url2) as f2:
    text2 = f2.read().decode('utf-8')

text2=text2.lower()
text2=text2.strip()

#remove punctuations
text2 = re.sub(r'[^\w\s]', '', text2)

word_frequency_2 = freq(text2)

#remove stop words
for stop_word in unnecessary_stop_words:
    if stop_word in word_frequency_2:
        del word_frequency_2[stop_word]




#basic summary statistics and surface level analysis of lexicon

def most_frequent_words(s):
    '''prints the 10 most frequently used words in a text'''
    rank= sorted(s.items(), key=lambda item: item[1], reverse=True)
    top_ten = rank[:10]
    for word, freq in top_ten:
        print(f'{word}: {freq}')

def diversity(s):
    '''takes the ratio of unique words to total words to quantify the lexical diversity of a text'''
    unique_words= len(s)
    total_words = sum(s.values())
    return round(unique_words/total_words,3)


#using nltk to analyze text
from nltk import pos_tag

def pos(s):
    """frequency of parts of speech(nouns, verbs, and adjectives)"""
    tagged_words = pos_tag(s)
    pos_frequencies = {'Noun': 0, 'Verb':0, 'Adjective': 0}
    #take the output abbreviations and categorize into noun verb or adjective
    noun_tags = ('NN', 'NNS', 'NNP', 'NNPS')
    verb_tags = ('VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ')
    adjective_tags = ('JJ', 'JJR', 'JJS')
    for word, tag in tagged_words:
        if tag.startswith(noun_tags):
            pos_frequencies['Noun'] += 1
        elif tag.startswith(verb_tags):
            pos_frequencies['Verb'] += 1
        elif tag.startswith(adjective_tags):
            pos_frequencies['Adjective'] += 1
    
    return pos_frequencies


from fuzzywuzzy import process
from fuzzywuzzy import fuzz

def word_similarity(frequency_dictionary_1, frequency_dictionary_2, scorer=fuzz.WRatio):
    '''
    Compares word frequencies of two texts and computes a similarity score producing a metric to be used in analysis.
    Using fuzzywuzzy to find best matches and similarity scores for individual words, the function then produces an overall score
    by multiplying the scores to give them weightings.
    '''
    total_similarity = 0
    weight_count = 0
    for word, freq in frequency_dictionary_1.items():
        best_match_data = process.extractOne(word, frequency_dictionary_2.keys(), scorer=scorer)
        if best_match_data:
            _, score = best_match_data  # Only the score is needed for the calculation
            total_similarity += score * freq
            weight_count += freq
    if weight_count == 0:
        return 0
    similarity = total_similarity / weight_count
    return similarity



def main():
    print(f'The top 10 words in order of frequency for The Great Gatsby are:')
    most_frequent_words(word_frequency_1)
    print(f'The top 10 words in order of frequency for This Side of Paradise are:')
    most_frequent_words(word_frequency_2)
    print(f'Among the most common words in the two books respectively we see many commonalities, out, up, one, been, and over.')
    gatsby_diversity=diversity(word_frequency_1)
    paradise_diversity=diversity(word_frequency_2)
    print(f'The ratio of unique words to total words in The Great Gatsby is:{gatsby_diversity}')
    print(f'The ratio of unique words to total words in This Side of Paradise is:{paradise_diversity}')
    print(f'These results are similar. It is that is no surprise that the lexical diversity is similar given that they are by the same author')
    gatsby_pos = pos(word_frequency_1.keys())
    paradise_pos = pos(word_frequency_2.keys())
    print(f'The parts of speech analysis for The Great Gatsby yielded the following results:{gatsby_pos}')
    print(f'The parts of speech analysis for This Side of Paradise yielded the following results:{paradise_pos}')
    print(f'In both novels we see a greater amount of nouns relative to adjectives and verbs.')
    similarity = word_similarity(word_frequency_1,word_frequency_2,scorer=fuzz.W)
    




if __name__ == '__main__':
    main()




