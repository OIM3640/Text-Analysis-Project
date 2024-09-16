import csv

def stopwords_list():
    '''Returns list of stopwords according to NLTK'''
    stopwords_file = open("stopwords.txt")  # from https://gist.github.com/sebleier/554280#file-nltk-s-list-of-english-stopwords
    stopwords = list()
    for line in stopwords_file:
        word = line.strip()
        stopwords.append(word)
    return stopwords


# https://docs.python.org/3/library/csv.html
def subset_data():
    '''Subsets cleaned so that included words are not stopwords and have a frequency count > 10'''
    hams = list()
    spams = list()
    stopwords = stopwords_list()
    with open('cleaned_true_spam.csv', newline="") as file:
        reader = csv.reader(file, delimiter= ",")
        next(reader, None) #skipping the header https://stackoverflow.com/questions/14257373/how-to-skip-the-headers-when-processing-a-csv-file-using-python
        spam_word_ct = 0
        for frq, word in reader:
            spam_word_ct += int(frq)
            if int(frq) > 10 and word not in stopwords: # subset to non-stopwords with frq > 10
                spams.append([int(frq), word])
    with open('cleaned_true_ham.csv', newline="") as file:
        reader = csv.reader(file, delimiter= ",")
        next(reader, None) # skipping the header https://stackoverflow.com/questions/14257373/how-to-skip-the-headers-when-processing-a-csv-file-using-python
        ham_word_ct = 0
        for frq, word in reader:
            ham_word_ct += int(frq)
            if int(frq) > 10 and word not in stopwords: # subset to non-stopwords with frq > 10
                hams.append([int(frq), word])
    print('Done Subsetting')
    print(f'spams: {len(spams), spam_word_ct}, hams: {len(hams), ham_word_ct}')
    return hams, spams, ham_word_ct, spam_word_ct


def add_pct():
    '''adds frequency as a percentage of total word occurrences (rounded to 5 decimal places after % conversion)'''
    hams, spams, ham_word_ct, spam_word_ct = subset_data()
    for i in range(len(spams)-1):
        item = spams[i]
        item.append(round(item[0]/spam_word_ct*100, 5))
    for i in range(len(hams)-1):
        item = hams[i]
        item.append(round(item[0]/ham_word_ct*100, 5))
    print("Done Adding %")
    return hams, spams

def write_processed_data():
    '''Writes cleaned and processed data into new CSV files to be analyzed'''
    hams, spams = add_pct()
    fields = ["frq", "word", "pct"]
    with open('processed_ham.csv', 'w', newline="") as file:
        write = csv.writer(file)
        write.writerow(fields)
        write.writerows(hams)
    with open('processed_spam.csv', "w", newline="") as file:
        write = csv.writer(file)
        write.writerow(fields)
        write.writerows(spams)
    print('Done Writing')

def main():
    write_processed_data()

if __name__ == "__main__":
    main()