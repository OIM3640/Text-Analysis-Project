'''
## Submitting your Project

1. Push all the code and updated `README.md` to the GitGub repository.
2. Create a pull request to the upstream repository. Please learn how to create a pull request by following [this instruction](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/working-with-your-remote-repository-on-github-or-github-enterprise/creating-an-issue-or-pull-request#creating-a-pull-request).
3. Submit your project's GitHub repository URL to Canvas.

---
*updated: 3/08/2023*
'''

import urllib.request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

def open_book():
    """
    This function opens the book. In this case it is the Great Gatsby
    """
    # url = 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt'

    # with urllib.request.urlopen(url) as f:
    #     text = f.read().decode('utf-8')
    # for line in text:
    #     if line.startswith('*** START OF THE PROJECT GUTENBERG EBOOK THE GREAT GATSBY ***'):
    #         break
    # print(text)  # for testing

    """
    Different Approach With ChatGPT below:
    """
    url = 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt'
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode('utf-8')

    start_str = "*** START OF THE PROJECT GUTENBERG EBOOK THE GREAT GATSBY ***"
    end_str = "*** END OF THE PROJECT GUTENBERG EBOOK THE GREAT GATSBY ***"

    start_index = text.find(start_str)
    end_index = text.find(end_str)

    if start_index != -1 and end_index != -1:
        return text[start_index:end_index]
    return text
    # print(text) #this is a test
    

def word_list():
    """
    This function makes the text into an actual list
    """
    text = open_book()
    for word in text:
        if ".,!?'-" in word or '"' in word:
            for letter in word:
                if letter == "." or letter == "," or letter == "!" or letter == "?" or letter == "'" or letter == '"' or letter == "-":
                    letter = ""
    word_list = text.split()
    return word_list

# Characterizing by Word Frequencies
def characterize_word_frequencies():
    """
    This function records in a dictionary how often each word is used in the book
    """
    freq = {}
    list = word_list()
    for word in list:
        freq[word] = freq.get(word, 0) + 1
    return sorted(freq)

# Computing Summary Statistics
def word_frequency_without_stop_words():
    """
    This function shows the frequencies of words without the stop words
    """
    new_list = removing_stop_words()
    return sorted(new_list)

# Removing Stop words
def removing_stop_words():
    """
    This function removes the following stop words: a, an, the, and, it, for, or, but, in, my, your, their 
    """
    sample = characterize_word_frequencies()
    del sample['a']
    del sample['an']
    del sample['the']
    del sample['and']
    del sample['it']
    del sample['for']
    del sample['or']
    del sample['but']
    del sample['in']
    del sample['my']
    del sample['your']
    del sample['their']
    return sample

# Natural Language Processing
def natural_language_processing():
    """
    This function checks the natural language processing of a line in the book
    """
    text = open_book()
    for line in text:
        score = SentimentIntensityAnalyzer().polarity_scores(line)
        print(score)

# Text Clustering
def text_clustering():
    """
    This function allows for text clustering.
    """
    pass

def main():
    """"""
    # open_book()
    # print(characterize_word_frequencies())
    # print(word_frequency_without_stop_words())
    # natural_language_processing()
    # text_clustering()


if __name__ == "__main__":
    main()