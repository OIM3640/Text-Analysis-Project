# **Text-Analysis-Project by Charlotte**

## **Project Overview**
 I used an eBook written by my favorite author, Oscar Wilde, called The Picture of Dorian Gray from the Project Gutenberg. Another source that I use especially in finding text similarity part is The Happy Prince and Other Tales by Oscar Wilde too. The texts are pre-organized into pretty txt file so all I did is retrieve the url through urllib.request and decode it according to “utf-8”. In analyzing them, I did word frequency test, frequency test after deleting stopping words, sentiment score of each sentence, text similarity score, and text clustering. These tools help me generate a general writing habit of Oscar Wilde and linguistic patterns of that era through individual analyzing and comparison between two texts. What is the difference in tone and syntax between serious literature, like *The Picture of Dorian Gray* and Fairy Tale, like *The Happy Prince and Other Tales*. 
 
 ### **Data Source**
 1. [*The Picture of Dorian Gray* by Oscar Wilde](http://www.gutenberg.org/ebooks/174.txt.utf-8)
 2. [*The Happy Prince and Other Tales* by Oscar Wilde](https://www.gutenberg.org/cache/epub/30120/pg30120.txt)
 3. [A stopword list](stopwords.txt)
 4. [A word list of most frequently used words](wiki-100k.txt) 
    <sub>This is a [wordlist](https://gist.github.com/h3xx/1976236) downloaded from Github.</sub>

## **Implementation**
 ### [Frequency Analysis](frequency_analysis.py)
 For the **first** part, I did some basic processing with the text so that it becomes histogram (words with frequency instead of a simple list of word itself). It is better as in finding the word variety. Before, I did list which is like below (Which will also lead to changes in the other functions, but for clarity, I will just show the first function)
```
 def process_text(text):
    """
    Processes the text and returns a list of the words used in the book. 
    """
    words = []
    for line in text.split('\n'):
        line = line.strip().lower()
        for word in line.split():
            # remove punctuations from the word
            word = word.translate(str.maketrans('', '', string.punctuation))
            words.append(word)
    return words
```

However it turns out that histogram is better to analyze the "rare" words in the book and frequency of those which is better in calculating the lanaguge usage patterns like does Oscar Wilde has certain rare words that he likes to use a lot? (after excluding the stopwords from Professor Li's source). Using a dictionary to store the histogram leads to easier lookup of the word frequencies. 

Also, I initially wrote the codes without define any function (written in the end part of [Frequency Analysis](frequency_analysis.py)); however, when I want to did analysis again for another book *The Happy Prince and Other Tales*, I found that I have to copy and paste the whole codes again and change every input name to differentiate. Function with a def main which allows variable input is more convenient. 
 
The process_text function generates a dictionary to store the word frequencies, while the load_stopwords function generates a set to store the stop words. The most_common function generates a list of tuples, where the first element is the frequency and the second element is the word. The subtract function generates a dictionary of the difference between two histograms.

### [Book Analysis with NLK and NTLK](book_analysis.py)
