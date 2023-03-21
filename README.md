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
 ### [Word Usage Frequency Analysis](frequency_analysis.py)
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

Also, I initially wrote the codes without define any function.

```
url = 'http://www.gutenberg.org/ebooks/174.txt.utf-8'
with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')

words = text.split()

word_freq = {}
for word in words:
    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] += 1

# Computing Summary Statistics
sorted_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
# word_freq.items is tuple, and lambda returns the second value of the tuple which is the frequency
for word, count in sorted_freq[:10]:  # return the first 10 tuples
    print(f'{word}: {count}')

words = text.split()
stop_words = {'the', 'and', 'a', 'an', 'or', 'but', 'not',
              'at', 'in', 'on', 'to', 'of'}  # self-defined stop words
words_without_stop_words = [
    word for word in words if word.lower() not in stop_words]

filtered_words = [word for word in words if word.lower() not in stop_words]

word_freq = {}
for word in words_without_stop_words:
    if word not in word_freq:
        word_freq[word] = 0
    word_freq[word] += 1

sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_word_freq[:10]:
    print(f'{word}: {count}')
```

However, when I want to do analysis again for another book *The Happy Prince and Other Tales*, I found that I have to copy and paste the whole codes again and change every input name to differentiate. Function with a def main which allows variable input is more convenient. 
 
The process_text function generates a dictionary to store the word frequencies, while the load_stopwords function generates a set to store the stop words. The most_common function generates a list of tuples, where the first element is the frequency and the second element is the word. The subtract function generates a dictionary of the difference between two histograms.

### [Book Analysis with NLK and NTLK](book_analysis.py)/ [Text Similarity](text_similarity.py)/[Text Clustering](text_clustering.py)

The data structures in these codes includes multiple lists and tuples. "sentences" is a list of sentences gathered and split through using "sent_tokenize" to process the input text. "score" is the output in form of tuples of of each sentence and its sentiment score. 

In understanding the sentiment analysis, ChatGPT helps on the choice of VADER (Valence Aware Dictionary and Sentiment Reasoner) which is a rule-based approach and machine-learning-based approach. 