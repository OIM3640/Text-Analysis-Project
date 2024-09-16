import csv 


def true_word_list():
    '''Returns a complete list of valid English words'''
    true_words_set = open("words.txt")
    true_words = list()
    for line in true_words_set:
        true_words.append(line.strip())
    return true_words

# https://docs.python.org/3/library/csv.html
def read_data(dataset):
    '''Reads email set from CSV and returns list of emails'''
    emails = list()
    spamct = 0
    hamct = 0
    header = 0
    with open(dataset, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        try:
            for text in reader:
                flag = text[-1]
                emails.append(text)
                # print(text[-1], type(text[-1]))
                if text[-1] == "0":
                    hamct += 1
                elif text[-1] == "1":
                    spamct += 1
                else:
                    header += 1
        except:
            print("Error here")
    print(f'spam: {spamct}, ham: {hamct}, header: {header}')
    return emails




def partition_emails(dataset):
    '''Partitions emails into spam or ham and returns 2 lists that contain all the words used in each'''
    emails = read_data(dataset)
    spamwords = list()
    hamwords = list()
    for email, flag in emails:
        words = email.split(" ")
        for i in range(len(words) - 1):
            if flag == "0":
                hamwords.append(words[i])
            elif flag == "1":
                spamwords.append(words[i])
    print("Partitioning Complete")
    print(f"hamwords: {len(hamwords)}, spamwords: {len(spamwords)}")
    return hamwords, spamwords


def validate_words(dataset):
    '''Returns 2 lists that only include the valid english words in spamwords and hamwords'''
    hamwords, spamwords = partition_emails(dataset)
    true_words = true_word_list()
    true_ham = list()
    true_spam = list()
    for item in hamwords:
        if item in true_words:
            true_ham.append(item)
    for item in spamwords:
        if item in true_words:
            true_spam.append(item)
    print("Validation Complete")
    print(f"true spam: {len(true_spam)}, true ham: {len(true_ham)}")
    return true_ham, true_spam


def create_dicts(dataset):
    '''Returns a dictionary of unique words and their frequencies'''
    true_ham, true_spam = validate_words(dataset)
    spamdict = dict()
    hamdict = dict()
    for word in true_spam:
        spamdict[word] = spamdict.get(word, 0) + 1
    for word in true_ham:
        hamdict[word] = hamdict.get(word, 0) + 1
    print("Dictionaries Complete")
    print(f"hamdict: {len(hamdict)}, spamdict: {len(spamdict)}")
    return hamdict, spamdict


def sort_dicts(dataset):
    '''Turns dictionaries into list of tuples and sorts them by word frequency'''
    sorted_ham = list()
    sorted_spam = list()
    hamdict, spamdict = create_dicts(dataset)
    for k, v in hamdict.items():
        sorted_ham.append((v, k))
    sorted_ham.sort(reverse=True)
    for k, v in spamdict.items():
        sorted_spam.append((v, k))
    sorted_spam.sort(reverse=True)
    print("done sorting")
    print(f"ham: {len(sorted_ham)}, spam: {len(sorted_spam)}")
    return sorted_ham, sorted_spam


"""
Running this program understandably took a while (~ 5 min per run) so I decided it would be best to clean all the data and write it into a readable csv file. 
"""


def write_cleaned_data(dataset):
    '''Writes the 2 sorted lists into CSVs'''
    sorted_ham, sorted_spam = sort_dicts(dataset)
    fields = ["frq", "word"]
    with open("cleaned_true_ham.csv", "w", newline="") as f:
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(sorted_ham)
    with open("cleaned_true_spam.csv", "w", newline="") as f:
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(sorted_spam)
    print("done writing")


def main():
    '''Writes raw email CSV data into 2 lists of sorted word-frequency tuples sorted by frequency'''
    dataset = "spamdata.csv"
    write_cleaned_data(dataset)


if __name__ == "__main__":
    main()
