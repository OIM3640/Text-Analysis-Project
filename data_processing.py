import csv
import sys
from unicodedata import category
import random


def import_file():
    """Transforms SMS Spam CVS file into a dictionary.

    returns: dictionary with "message" as the keys and "status" as the values
    """
    # Code source: ChatGPT
    # sms_file is a cvs file composed of two columns: status (spam or ham/non-spam) and message
    with open("data/spam.csv", mode="r") as sms_file:
        csv_reader = csv.DictReader(sms_file)
        sms_dict = {}
        for row in csv_reader:
            sms_dict[row["message"]] = row["status"]

    return sms_dict


def spam_ham_lists(sms_dict):
    """Separates spam and ham in dictionary into two corresponding lists.

    sms_dict: dictionary of sms messages (message:status pairs)

    returns: list of spam messages, list of ham messages
    """
    spam_list = []
    ham_list = []

    for k, v, in sms_dict.items():
        if v == "spam":
            spam_list.append(k)
        else:
            ham_list.append(k)

    return spam_list, ham_list


def spam_ham_string(messages):
    """Transforms spam or ham list into a string.

    messages: list of spam or ham messages

    returns: string containing paragraph of spam or ham messages.
    """
    paragraph = " ".join(messages)
    return paragraph


def histogram(data, paragraph):
    """Creates a histogram with words and corresponding frequencies.

    data: string (paragraph of messages or file path)
    paragraph: boolean, whether data is a paragraph

    returns histogram
    """
    hist = {}
    strippables = ''.join([chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")])
    
    # if data is a string with a paragraph of messages
    if paragraph:
        data = data.replace('-', ' ')
        data = data.replace(chr(8212), ' ')
        for word in data.split():
            word = word.strip(strippables)
            word = word.lower()
            if word == "": # if word is an empty string, do not add to histogram
                continue
            # Issue with dataset: lt;#&gt represents a number (e.g. "lt;#&gt mins"). This code replaces it with a random 2 digit integer
            if word == "lt;#&gt":
                word = str(random.randint(10, 99))
            hist[word] = hist.get(word, 0) + 1
    # if data is a text document (one word per line, no punctuation, all lowercase)
    else:
        data = open(data)
        for line in data:
            for word in line.split():
                hist[word] = hist.get(word, 0) + 1

    return hist


def main():
    sms_dict = import_file()
    spam_list, ham_list = spam_ham_lists(sms_dict)
    spam_paragraph = spam_ham_string(spam_list)
    ham_paragraph = spam_ham_string(ham_list)
    
    print(histogram(spam_paragraph, paragraph=True))
    print(histogram(ham_paragraph, paragraph=True))
    print(histogram("data/stopwords.txt", paragraph=False))

if __name__ == '__main__':
    main()