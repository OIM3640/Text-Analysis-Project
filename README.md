# Text-Analysis-Project
 
Please read the [instructions](instructions.md).

1. **Project Overview**
    The data source I used is Wikipedia. I characterized my datas by Word Frequencies, removed stop words in my data, and summarized statistics of my data.Through this project I learned how to process text datas. I hope to process the original messy text data into a clear structured data with useful statistic informations. 

2. **Implementation**
    I uploaded the data source of wikipedia, and then extracted the search content for "Babson College" in the wikipedia page as my text data. I want to characterize the data by word frequency. So I need to make these text data clean first. I learned to use `.replace` to remove unnecessary symbols and spaces by asking ChatGPT how to remove spaces from text (see detailed conversation:https://chat.openai.com/share/4949941e-4239-413f-9bfb-7d5ab82f6b3a). I created an empty dictionary `hist = {} `at the beginning to store each word and its frequency, then I wrote these codes to calculate the frequency of each word:
   ```
   `if word in hist:
        hist[word] += 1
   else:
        hist[word] = 1`
   ```
However, I shortened these codes to: `hist[word] = hist.get(word,0) + 1` based on the example of the analyze_book exercise in session 15. Not only does this make my code look cleaner, it also becomes easier to understand.
    I wanted to find the top ten most occurring words. So I need to remove the stop words in the text first, because stop words are meaningless words and may affect my data. I turned to ChatGPT to give me a good list of stop words to be removed from text in python (see detailed conversation: https://chat.openai.com/share/e3c76a99-8f45-4913-ae7f-6e69b8e1122b) ChatGPT initially gave me the NLTK method. This method is simple and fast, and the entire code looks cleaner, but I still let ChatGPT generate a list of stop words without using NLTK, because this way I can see more clearly and intuitively which stop words have been removed, and it is also easier for me to understand the code later. Later, by studying the examples of session 15 anayze_book exercise, I changed the hist data into descending order list of (frequency, word). This makes it easier to process the top ten data. Later, I tried the fuzz library and nltk through the examples on the instructions, and asked ChatGPT to explain each line of code to facilitate my understanding (see detailed conversation: https://chat.openai.com/share/a7249e2b-d61a-4c9e-91a3-9f35db18a5a5 ). I added these two functions to my code to obtain more data about the text.

4. **Results**
    I collected two data sources in Wikipedia: the search result content of "Babson College" and "Olin College", and I get the top ten most frequently occurring words from two different data sources (see examples). You can see that the words that appear more frequently in the content of the search results for "Babson College" are words that characterizes Babson: such as "business" and "ceo" ; And the content that appears more often in the search results for "Olin College" is: "enginerring". I think this result can be used to prove the success and significance of my project. By analyzing more words that appear in a paragraph of text, we can get a rough summary of the text and quickly understand the important elements in the text data.
    ```
    "Babson College" Example： 
        The most common words are:
        babson   24
        mba      20
        business         19
        college          17
        former   16
        students         8
        new      8
        ranked   7
        president        7
        ceo      7`
    
    "Olin College" Example:
        The most common words are:
        olin     53
        students         27
        college          25
        student          16
        engineering      13
        first    11
        projects         9
        academic         9
        school   7
        also     7
    ```
   
    There is another very interesting point in my data analysis. I compared the fuzz similarity between Babson and Brandeis text data and etween Babson and Olin text data. I originally thought that Babson and Brandeis would be more similar because they are both business schools, but then I found that Babson and Olin would be closer. Fuzz uses Levenshtein distance to analyze the similarity of two data. In fact, it is reasonable to think about it carefully. For example, if Babson and Olin have the same geographical location, then the Levenshtein distance of their text data may be closer.

    ```
    Example Babson vs. Olin:
    `text = babson_content
    reference_text = olin_content
    fuzztext(text, reference_text)`
    Output: 
    Ratio Similarity: 40
    Partial Similarity: 40
    Token similarity: 62

    Example Babson vs. Brandeis:
    `text = babson_content
    reference_text = brandeis_content
    fuzztext(text, reference_text)`
    Output: 
    Ratio Similarity: 29
    Partial Similarity: 40
    Token similarity: 57
    ```
   
5. **Reflection**
    There are still many areas for improvement in my code. For example, when I clean up the text data, I use a lot of repeated code `.replace`, which can be coded to be cleaner.  Since I was constantly updating my data and wanted to use the code I learned in class as much as possible in this assignment, I chose to continue using .replace. I feel that the data analyzed by my code is not very relevant, but they are all useful analysis methods. Whether it is the word with most frequncy or the similarity between the two sets of text data, some interesting findings can be analyzed very well.
    Reasonable use of ChatGPT can develop more coding ideas. For example, it can tell you multiple ways to solve a problem, so you can compare them and choose the most suitable code. Through ChatGPT, we can realize more problem-solving ideas and learn more codes.
