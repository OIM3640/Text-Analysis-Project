import string
from unicodedata import category

STOPWORDS = {
    "the", "and", "is", "in", "it", "you", "of", "to", "a", "that", 
    "with", "for", "on", "this", "by", "an", "as", "at", "i", "my", "was",
    "me", "but", "had", "he", "she", "it", "which", "him", "his", "her",
    "be", "your", "from", "not", "have", "had", "were", "when", "so", "they",
    "one", "could", "will", "would", "can", "could", "these", "those", "no", "should",
    "all", "been", "if", "their", "or", "are", "we", "who", "more", "now", "yet", "some",
    "before", "myself", "man", "upon", "what", "our", "them", "am", "into", "its", "only",
    "did", "do", "does", "than", "shall", "may", "being", "towards", "first", "might", "then",
    "even", "most", "such", "any", "whom", "there", "ever"
}

def process_file(filename, skip_header):
    """
    It reads the text file to create a histogram of word frequencies.
    """
    hist = {}
    fp = open(filename, encoding="utf-8")

    if skip_header:
        skip_gutenberg_header(fp)

    strippables = string.punctuation + string.whitespace

    for line in fp:
        if line.startswith("*** END OF THE PROJECT"):
            break

        line = line.replace("-", " ")
        line = line.replace(chr(8212), " ")

        for word in line.split():
            word = word.strip(strippables).lower()
            hist[word] = hist.get(word, 0) + 1

    fp.close()
    return hist

def skip_gutenberg_header(fp):
    """
    It skips the Project Gutenberg header in the text file.
    """
    start_marker = "START OF THE PROJECT"

    for line in fp:
        if start_marker.lower() in line.lower():
            return
    raise ValueError(f"Header end marker '{start_marker}' not found in file.")

def total_words(hist):
    """
    It calculates the total number of words in the histogram.
    """
    return sum(hist.values())

def different_words(hist):
    """
    It calculates the number of unique words in the histogram.
    """
    return len(hist)

def remove_stopwords(hist):
    """ 
    It creates the new dictionary after removing the stopwords. 
    """

    filtered_hist = {word: count for word, count in hist.items() if word not in STOPWORDS}
    # For each word and its count in hist.items(), it checks if the word is not in STOPWORDS.
    # If the word is not in STOPWORDS, it is added to the new dictionary with its count.

    return filtered_hist

def most_common(hist, excluding_stopwords=False):
    """
    It returns a list of word-frequencies pairs in the descending order of frequency.
    """
    if excluding_stopwords:
        hist = remove_stopwords(hist)
    t = list(hist.items())
    t.sort(key=lambda x: x[1], reverse=True)
    return t

def print_most_common(hist, num=20):
    """
    It prints the top 10 most common words after removing the stopwords.
    """
    t = most_common(hist, excluding_stopwords=True)
    for i in range (num):
        t = most_common(hist)
        print(t[i])

def main():
    # This text file is downloaded from gutenberg.org: https://www.gutenberg.org/cache/epub/84/pg84.txt.
    # The ebook name is Frankenstein, written by Mary Wollstonecraft Shelley. 
    hist = process_file("data/Frankenstein.txt", skip_header=True)
    print(f"Total number of words: {total_words(hist)}")
    print(f"Number of different words: {different_words(hist)}")

    t = most_common(hist, excluding_stopwords=True)
    print("The most common words are:")
    for freq, word in t[0:20]:
        print(word, "\t", freq)
    print(hist)

if __name__ == "__main__":
    main()




