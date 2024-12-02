# Part 3
I'm having problem on cleaning strings. I used methods such as 'replace' but it didn't achieve the expected effect. I don't know if it's because the string is too long or some other reason. So I asked Chatgpt for help on how to clean up long text.

prompt: 
I want to delete all non-English letters and spaces in a long string of str (including newlines)

anwser:

You can remove all non-English letters and spaces, including newlines, from a string by using regular expressions. The re module in Python is a powerful tool for working with regular expressions. Here's how you can do it:
```
import re


def remove_non_english_characters(input_str):
    # Define a regular expression pattern to match English letters and spaces
    pattern = r'[^a-zA-Z\s]'
    
    # Use re.sub to replace non-matching characters with an empty string
    cleaned_str = re.sub(pattern, '', input_str)
    
    return cleaned_str

# Example usage
input_str = "This is a test string with\nnon-English characters like 你好 and こんにちは."
cleaned_str = remove_non_english_characters(input_str)

print(cleaned_str)
```

In this code:

We import the re module for working with regular expressions.

The remove_non_english_characters function takes an input string as its argument.

We define a regular expression pattern r'[^a-zA-Z\s]' that matches any character that is not an English letter (both lowercase and uppercase) or a space.

We use re.sub to replace all the characters that match the pattern with an empty string '', effectively removing them from the input string.

The cleaned string is then returned.

When you run the example, it will remove all non-English letters and spaces, including newlines, from the input string, leaving only the English letters and spaces. You can apply this function to your long string as needed.

I def the learning from gpt as 'processing' fuction in my code.
However, there still many '\r' and '\n' in the str after I check. Therefore, I create a fuction 'processing2' by myself to further clean the str.


# Part 4
## 1. Project Overview
What data source(s) did you use? What technique(s) did you use to process or analyze them? What did you hope to create or learn through this project?

The data source is the text fetched from the Project Gutenberg. Data Processing and Analysis Techniques: Several text cleaning functions are defined (`processing`, `processing2`) to remove non-English characters, convert text to lowercase, and handle spaces for str Cleaning; using the list and dictionary we learned on course to do some Word Frequency Analysis; removes Stopword from the text, and doing Sentiment Analysis using the `SentimentIntensityAnalyzer` from the Natural Language Toolkit.
The Project is aiming for learning data Cleaning and preprocessing methods, and to gain insights into the content of the text, identify frequently used words, and analyze the overall sentiment, specifically analyze the Sentiment of lauguage for different way of its present (with punctuation & symbols and without; with stopword and without).

## 2. Implementation 
Describe your implementation at a system architecture level. You should NOT walk through your code line by line, or explain every function (we can get that from your docstrings). Instead, talk about the major components, algorithms, data structures and how they fit together. You should also discuss at least one design decision where you had to choose between multiple alternatives, and explain why you made the choice. Use shared links and/or screenshots to describe how you used ChatGPT to help you or learn new things.

Data Retrieval Component: The initial step is to fetch text data from an external source (a URL) using the `urllib.request` module. 
Text Cleaning and Preprocessing Component: After obtaining the text data, it goes through a series of cleaning and preprocessing steps. The `processing` and `processing2` functions handle text cleaning. They remove non-English characters, convert text to lowercase, and eliminate extra spaces.
Word Frequency Analysis Component: The `cintext` function processes the cleaned text and creates a dictionary that stores the frequency of each word in the text. The `nonStopwords` function extends the previous component by removing common English stopwords from the word frequency analysis. 
Sentiment Analysis Component: Sentiment analysis is performed using the `SentimentIntensityAnalyzer` from the NLTK library. This component calculates sentiment scores, including 'neg' (negative), 'neu' (neutral), 'pos' (positive), and 'compound'. The `pat` function calculates average sentiment scores for words in the text. 
The major data structure used in the code is dictionaries, which are used to store word frequencies and sentiment scores. Additionally, lists and strings are employed for various text processing and manipulation tasks.

## 3. Results 
Present what you accomplished in your project: 
If you did some text analysis, what interesting things did you find? Graphs or other visualizations may be very useful here for showing your results. If you created a program that does something interesting (e.g. a Markov text synthesizer), be sure to provide a few interesting examples of the program's output.
```
print (top(cintext(text), 20))
print (top(nonStopwords(text), 20))
#output:
['the', 'and', 'of', 'to', 'a', 'in', 'he', 'his', 'that', 'was', 'it', 'you', 'i', 'with', 'as', 'said', 'had', 'for', 'mr', 'him']
['he', 'his', 'you', 'i', 'said', 'had', 'mr', 'him', 'which', 'her', 'oliver', 'have', 'from', 'all', 'me', 'so', 'were', 'she', 'who', 'my']
```
It shows that when we not remove the stopwords, ths top high-frequency words in a book are most stopwords.
After we clean all stopwords, many of the high-frequency words become personal pronouns.
```
print (at(processing2(text)), at(text))
# output:
{'neg': 0.1, 'neu': 0.766, 'pos': 0.134, 'compound': 1.0} {'neg': 0.092, 'neu': 0.784, 'pos': 0.124, 'compound': 1.0}
```
The text after cleaning (without punctuation & symbols and all lowercase) are more negative but less neutral and positive.
```
print (pat(cintext(text)), pat(nonStopwords(text)))
# output: 
{'neg': 0.0349980118296138, 'neu': 0.889637904468413, 'pos': 0.0413974352602018, 'compound': 0.003287388786719019} {'neg': 0.04581088814803375, 'neu': 0.8783826748907643, 'pos': 0.060527056857098735, 'compound': 0.0063929198877210784}
```
The average Sentiment score include stopwords are less negative and positive but more neutral. It do match the fact that stopwords actually means nothing.

## 4. Reflection
From a process point of view, what went well? What could you improve? Was your project appropriately scoped? Did you have a good testing plan?
From a learning perspective, mention what you learned through this project, how ChatGPT helped you, and how you'll use what you learned going forward. What do you wish you knew beforehand that would have helped you succeed?

What Went Well: The code effectively retrieves, cleans, and analyzes text data; it is modular and organized with distinct functions, making it easy to change and debugging; the sentiment analysis achieve the expectation.
What Could Be Improved: The data cleaning and processing part defiantly coud be smarter (for example, the method gpt used), however, I haven't learned those stuff. Could include the compare anaylsis between two text.
Project Scope appears to be appropriately set for basic text analysis, including word frequency and sentiment analysis. 
Testing Plan: The code includes some print statements for testing, but a more structured testing plan, including unit tests. 
Learning a new way of str cleaning from gpt, and sentiment analysis using the VADER sentiment analysis tool from NLTK. I will further develop my own data cleaning&processing method which are best fit for myself's logic that combine all methods and logic I learned. I wish I know more library and keywords on not only text analysis but data analysis.