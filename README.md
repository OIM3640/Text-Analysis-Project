# Text-Analysis-Project

Please read the [instructions](instructions.md).

## Part 4 of Text Analysis Project

For this project assignment, I used a classical literary work from Project Gutenberg, specifically the ebook, or we can say, the plain text version of Frankenstein by Mary Shelley. Using this public domain text allowed me to analyze a literary work freely. My primary techniques employed in this project involved characterizing by word frequencies, computing summary statistics, and removing stop words. The goal of this project was to explore word frequency analysis within this classical and historial literary text to uncover patterns and underlying themes by removing the repetitive, low-meaning stop words. I aim to deepen my familiarity with the foundational text processing techniques that we learned in class by building a reusable tool that can be applied to the future text-based datasets. 

I think there are three major components or we can say, functions for my project. The first one is the file processing and data cleaning and transformation function. This component reads in the text file, skipping the header and footer, allowing us to focus solely on the main content. I used the tokenization and punctuation stripping to create a consistent format across all words, preparing them for accurate frequency analysis. Furthermore, the stopword removal allows me to filter out common words from the histogram that do not contribute significant meaning to the analysis. The last component, frequency analysis, is to generate a list of the top 20 most commonly used words and its frequencies that offered insight into the unique vocabulary and recurrent themes within the text. 

One of the key design decision in this project was the functions of stopword removal. As we all know, Stopwords are common words that generally do not contribute significant meaning in text analysis and can skew frequency results if left in the plain data. Initially, I was indecisive between using a list-based or set-based approach for the Stopword function. After consulting GenAI tools, I was advised to implement the set-based approach stating that using a set would reduce the check time and allow for rapid identification of stopwords. This choice was particularly beneficial for larger texts. 

Also，I encountered a problem while working on the code of the stopword removal. 

I wrote:
```
def remove_stopwords(hist):
    """ 
    It creates the new dictionary after removing the stopwords. 
    """
    if word not in STOPWORDS:
        filtered_hist = {word, count in hist.items()}
    
    return filtered_hist
```
Then, I received the following message: 

> Traceback (most recent call last):
  File "/Users/yinxiaohe/Documents/GitHub/Text-Analysis-Project-YinxiaoHe/textanalysisproject.py", line 113, in <module>
    main()
  File "/Users/yinxiaohe/Documents/GitHub/Text-Analysis-Project-YinxiaoHe/textanalysisproject.py", line 106, in main
    t = most_common(hist, excluding_stopwords=True)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/yinxiaohe/Documents/GitHub/Text-Analysis-Project-YinxiaoHe/textanalysisproject.py", line 85, in most_common
    hist = remove_stopwords(hist)
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/yinxiaohe/Documents/GitHub/Text-Analysis-Project-YinxiaoHe/textanalysisproject.py", line 69, in remove_stopwords
    if word not in STOPWORDS:
       ^^^^
NameError: name 'word' is not defined. Did you mean: 'ord'?

Then, I asked ChatGPT to make revisions on my current existing code. It provides me with the following:
```
def remove_stopwords(hist):

    filtered_hist = {word: count for word, count in hist.items() if word not in STOPWORDS}

    return filtered_hist

```
By letting the ChatGPT to break down into each part, I restructured the code to use a dictionary comprehension. The modified one allows me to check if the word is in STOPWORDS for each word and its count in hist.items(), ensuring that only words not in STOPWORDS are added to the new dictionary with their respective counts.

Through this project, I was able to visualize the frequency distribution of words within Frankenstein, providing insights into the central themes and character in the text. Notably, the words like "death", "creature", "monster", and "creation" were among the most frequent terms, reflecting the key idea of identity, humanity, and scientific ambition from this book. This frequency analysis by visualizing the top words offer a quantitative perspective on a traditionally qualitative subject.

From a process standpoint, the modular design approach worked very well, enabling a clear separation of responsibility within each function and easy debugging and testing. The most challenging aspect was to develop the efficient way to handle stopwords without sacrificing performance. To address this, I used the set-based approach for stopword filtering, which provided a significant speed advantage over list-based methods for larger text. For the testing section, I believe it was quite straightforward, as each module could be independently verified to ensure accuracy. 

The biggest takeaway from this project was understanding the value of clean, modular, and straighforward code when processing complex datasets. Working with ChatGPT, this GenAI tool, enhanced my approach to problem-solving and implement best practices effectively. Moving forward, I am quite interested in applying these similar text analysis techniques to sentiment analysis, by analyzing the emotional tone of texts. 

One thing I wish I would know earlier was the variety of the libraries for text processing. Before, I thought because of the problems of patent, we wouldn't have the opportunities to have the access of these ebooks not only for reading but also for text processing. Now, I believe I would definitely utilize these analysis techniques in the future to some books that I haven't read about to find out the key characters and main themes. 




