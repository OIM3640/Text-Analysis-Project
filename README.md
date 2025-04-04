# Text-Analysis-Project

Please read the [instructions](instructions.md).

##Project Overview

I used a data source from Project Gutenberg, a book called "Little Women" by Luisa May Alcott. I chose this book because it was the first novel that I read completely and it touched me to the soul.To analyze the text I converted **individual words into tokens** by splitting lines and stripping punctuation, **frequency analysis** counting how often words appear, **filtered stopwords** and **data cleaninf**. Then I used NLTK to **analyze the sentiment** of the book as a whole and chapter by chapter. And finally I tried to compare the book to a Charles Dickens novel from the same year to see if there are any similarities in language. From this project I was hoping to reate a simple but helfull analysis of the novel and to learn more on how to strip down text data.

##Implementation 
There are various components that help the code function as a whole, but I would say that the key algorithims are:
- Text cleaning ans tokenization: Stripping punctuation using Unicode character properties, splitting lines into words and converting lower case
- Word Frequency Analysis: Using a dictionaly to count ocurrences and sorting to rank words by frequency.
- Sentiment Analysis: Uses VADER for nltk and scores each chapter as positive, neutral or negative
- Chapter splitting: Detects roman numeral in heading and split chapters

So at the end the book is downloaded (read_book()) and cleaned (skip_gutenberg_header()).The text is processed (process_text()) into a word frequency dictionary (hist). Statistical analysis is performed to find the most common words. The text is split into chapters (split_into_chapters()). Sentiment analysis is applied to the whole book and each chapter (analyze_book_sentiment()).Results are printed and could be visualized (not implemented yet).

##Results
What I implemented in my code is a pipeline to: download and clean the text, count word occurences and analyze the most common words and perform a sentiment analysis on the book and its chapters. 
###Key Findings:
- The most common words (excluding stopwords) were: "jo", "said", "meg", "little", "Laurie". This result highlights the main characters in the book, it is evident that Jo is the protagonist.The histogram of word frequencies shows a steep drop after most common words.
- The overall sentiment analysis of the booked reached the conclusion that the book was: neutral - positive. Which was a surprice for me since I cried several times while reading it. But it makes sence since it has a fairly happy ending. Per chapter analysis revealed that the chapters with high positive sentiment where chapters that contained moments of family bonding and seccesses and chapters with negative sentiments are chapters that contain loss and struggles.
- The most positive chapter is 65 and most negative is Chapter 87, this showa hw the book starts with some optistics and positive scenarios where the sisters are kind and hopefull about the future. But as the book goes on, hearts are broken and the plot twists. There is a happy ending, but not the one the book made us thought we would get.
- The text similarity and clusterin compares the Little Women book with a book by Charles Dickens called Edwin, the scatter plot shows that the two books, even though they were made in the same year, show little similarities. This shows how even though both texts where published in 1868 they do not present too much similarities in their language. 

#Reflection
##Process Reflection
The overalll process of analyzing the book went well in terms of breaking down the steps in each function logically( reading, cleaning, counting words, sentiment analysis and comparison). I used python built in libraries as 'nltk' and 'collections'. My biggest challenge was dealing with the text processinf function and cealing the text properlY. I couldn't get the code to split the chapters at first which made my sentiment analysis less meaningfull. I solved it by using AI and regular expressions to improve the detection of the chapters. GenAI helped me understand re.split() and point out errors.

I think that the chapter detection could be imporved, it currently rely on patterns and that does not always work perfectly. Perhaps using NLP could help. Also I thing that a more robust sentiment analysis could be done. A analysis where one could determine the characters and see it they are more positive or negative.

I did not have a goo testing plan at first, and mostly relied on printing outputs or manualy checking if the results made sense. I notice how complicated and hard coding can get, I got lost several times and had to ask GenAI to explain functions constanlty. GenAI helped me understand regular expresions for chapter splitting, it suggested debugging strategies when functions were not workinf and it provided clear explanations of Python libraries I was not familiar with like NLTK and Fuzz.

###GEN AI links:
Explained the fuzz function:
https://claude.ai/share/b0b92e2e-da0f-42a7-ae2d-f0f61b38d2ac

Ideas for the sentiment Analysis:
https://claude.ai/chat/52fd4194-63b8-4cf3-a334-0342ede9b71e

Fixing the chapter split:
https://chatgpt.com/share/67ef40a4-7340-800e-88d9-2ffe23cd0b5f


