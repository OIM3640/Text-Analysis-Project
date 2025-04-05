1. Project Overview
In this project I analyzed "The Scarlett Letter" by Nathaniel Hawthorne using the Gutenberg digital library as my data source. The goal of the project better understand the text by counting how often each word appeared, removing common words for example “the” or “and,” and analyzing the emotional tone of the book using sentiment analysis.Overall creating a Python program that does all of this automatically for any text as long as URL is provided.

2. Implementation
The program first downloads the book from a given URL using the urllib library. It then cleans the text by removing extra headers, footers, and punctuation. Once cleaned, the program counts how often each word appears using a dictionary. Words are sorted in descending order based on how frequently they appear. I also created summary statistics, like total and unique word counts, and the average frequency.

To focus on more meaningful words, I removed common stop words such as "the", "and", and "is". This gave a clearer picture of important terms in the story. Finally, I used the VADER sentiment analyzer to evaluate the emotional tone of the book, returning a score that shows how positive, negative, or neutral the text is overall.

3. Results
Word Frequency Analysis - The entire book
Total Words: 83826
Unique Words: 10150
Average Word Frequency: 8.25871921182266
5 Most Common Words: 
the: 5239
of: 3247
and: 2716
a: 2058

Word Frequency Analysis - Removing Stop Words:
Total Words: 51608
Average Word Frequency: 5.149312765747058
 5 Most Common Words:
 not: 467
 but: 454
 so', 452
 'have', 419
 'or', 403
Sentiment Score using VADER:
negative: 0.1
neutral: 0.77
positive 0.129
compound: 1.0

The intitial word frequency for the story is 83826 and after removing some common words it drops down to 51608. What I found interesting from the results was the amount of unique words. The number is higher than what I expected but speaks towards the writers style  The results from the sentiment analysis show that this story follows a more neutral tone. 

4. Reflection
This project helped me learn how to analyze large pieces of texts in python better. The biggest challenge that I had was cleaning up the text so the frequency analysis would work properly. For example if there was punctuation at the end of the word would count it as something different. I built on my skils with python particularly with dictionaries. I utilized AI during this project to enchance my understanding. I primarly used AI for debugging assitance for when I had issues with my code. I also used AI to learn about the new library I was loading in or thought about using such as nltk. Future improvements I could make on my code is adding more stop words. I still had basic english words as most common after removing the stop words I chose. Also I could continue to build on this code. Such as adding in a funtcion to compare different text using fuzzy. 