import csv
from wordcloud import WordCloud  # https://amueller.github.io/word_cloud/references.html
import random

# ChatGPT prompt: https://chat.openai.com/c/f2ad0805-b705-42f2-8ec8-16fad925e006

# https://docs.python.org/3/library/csv.html


def read_data():
    """Reads cleaned and processed data and returns a list of word, frequency, and frq as a %"""
    ham = list()
    spam = list()
    with open("processed_ham.csv", newline="") as file:
        reader = csv.reader(file, delimiter=",")
        next(reader, None)  # ignore header
        for row in reader:
            ham.append(row)
    with open("processed_spam.csv", newline="") as file:
        reader = csv.reader(file, delimiter=",")
        next(reader, None)  # ignore header
        for row in reader:
            spam.append(row)
    print("Done Reading Data")
    # print(len(ham), len(spam))
    return ham, spam


def frq_dicts():
    """Returns dictionaries for word:frq for use in later functions"""
    ham, spam = read_data()
    ham_dict = dict()
    spam_dict = dict()
    for i in range(len(ham) - 1):
        frq = ham[i][0]
        word = ham[i][1]
        ham_dict[word] = int(frq)
    for i in range(len(spam) - 1):
        frq = spam[i][0]
        word = spam[i][1]
        spam_dict[word] = int(frq)
    return ham_dict, spam_dict


def pct_dicts():
    """Returns dictionaries for word:pct for use in later functions"""
    ham, spam = read_data()
    ham_dict_pct = dict()
    spam_dict_pct = dict()
    for i in range(len(ham) - 1):
        pct = ham[i][2]
        word = ham[i][1]
        ham_dict_pct[word] = pct
    for i in range(len(spam) - 1):
        pct = spam[i][2]
        word = spam[i][1]
        spam_dict_pct[word] = pct
    return ham_dict_pct, spam_dict_pct

# From ChatGPT
def word_clouds():
    """Creates a word cloud from ham and spam data using the wordcloud module"""
    ham_dict, spam_dict = frq_dicts()
    ham_cloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(ham_dict)
    print("Ham Cloud Done")
    spam_cloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(spam_dict)
    print("Spam Cloud Done")
    return ham_cloud, spam_cloud


def top_words_table(n):
    """From each of ham and spam lists, prints the top n words in terms of frequency"""
    ham, spam = read_data()
    print("_____________SPAM__________________________HAM___________")
    for i in range(n):
        print(
            f'{"| " + str(spam[i][1] + ", " + str(spam[i][0])) + ", " + str(spam[i][2]) + "%":<29}|  {"| " + str(ham[i][1] + ", " + str(ham[i][0])) + ", " + str(ham[i][2]) + "%":<25}|')


# top_words_table(20)


def spam_words_match(n):
    '''For the top n words in spam, returns the corresponding frequency % in a non-spam email. 
    If the frequency is higher in spam emails than it is in ham emails, 
    stars will be appended to the end of the row'''
    counter = 0
    ham_dict, spam_dict = pct_dicts()
    print('______WORD_________SPAM FRQ %_______HAM FRQ %______')
    for k, v in spam_dict.items():
        hampct = ham_dict[k]
        spampct = spam_dict[k]
        if spampct > hampct:
            print(f'{k:<15} |   {spampct:<10}|{hampct:>20}   ***')
        else:
            print(f'{k:<15} |   {spampct:<10}|{hampct:>20}')
        counter += 1
        if counter > n-1:
            break


# spam_words_match(10)


def main():
    ham_cloud, spam_cloud = word_clouds()
    ham_cloud.to_file("ham_cloud.png") # no need to keep overwriting the image once it's been done
    spam_cloud.to_file("spam_cloud.png") # ^^^
    n = 20
    top_words_table(n)
    spam_words_match(n)


if __name__ == "__main__":
    main()
