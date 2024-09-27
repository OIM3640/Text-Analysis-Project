# Text-Analysis-Project
 
## 1. Project Overview

For this assignment I decided to analyze the Odyssey by Homer which is very popular and usually read by high schoolers in America. To process and analyze this text I removed the header and ending that the Gutenberg Project adds to its text. The text is split into lines and analyzed in a few ways. Frequencies of words, unique words, and the 10 most used words and their frequencies excluding stop words. As someone who has read this book, I hoped that the 10 most used words would give the user of this code an overview of what it was about and align with what I know about it.

## 2. Implementation

### Design Decisions 

The main things that I have done in this code are importing the text from an online source, processing it so that I could extract useful information, and creating a histogram without stopwords to store the words and their frequencies. There is then a main function that enables all of the components of the code to be used, if asked. For stopwords, I decided to pull them from a file and then add them to a list. An alternative would have been to create a list with all words that I wanted removed. Using a ready made file is much simpler than creating a list with every word I want removed. I did add the word 'us' to the list though because it was appearing as one of the top 10 words and I did not think it added anything to the users understanding of what the book was about. The external list can also be updated easily.

### ChatGPT

ChatGPT was extremely helpful when writing this program. For instance, I learned about the use of .splitlines() for text processing. I was having trouble looking at lines of the text vs. words in the text. I asked how I would fix my problem and was showed .splitlines(). It helped me fix my code and gave me a detailed description of what it was and how it was used. 

#### ChatGPT Output
![Alt text](image.png)

## 3. Results

In this project I found out how many different words are in the Odyssey by finding the length of the histogram, the result is showed below.
![Alt text](image-1.png)

Although I was able to create a histogram with the frequency of every word, I did not think that was particularly useful in terms of analysis of the data. But finding and printing the top 10 most used words was. The output of this is also shown below. 
![Alt text](image-2.png)

These two actions show me that this is an extremely long book that uses many different words. The 10 most common words give me a little insight on what the book is about. For instance, Ulysses is the latin name for Odysseus who is the main character. As someone who read the book, this is a fact that I was already aware of. But someone who has not read it, could use this output and infer that Ulysses, whoever he is, is the main character. 

There are also a lot of action words, 'will', 'now', 'went', and 'come'. These tell someone that the book is probably about some sort of adventure or journey and the future. Another interesting result is that 'men' and 'man' are in the top 10 most common words. This book is dominated by men and the output would tell the reader this before ever opening the book. 

## 4. Reflection

When writing this program, I did not immediately know where I was going with it. I first just started with processing the file as I knew that was something that would have to be done regardless. A lot of the code and practice we did in class helped with this part and gave me an understanding of what the code was actually doing. However, not knowing where I was going led to me having to change and add parts in later when I knew what I was doing. This was a little frustrating as there was a lot of scrolling up and done to see what went wrng and what I was missing. I encountered many errors as I tried to adapt code to this new data with a different outcome.

This is where ChatGPT came in handy. It gave suggestions for things I could do and explained what the errors I was getting meant. Not all of them were self explanatory and I had trouble understanding how to fix my code when I did not even know what the problem was. ChatGPT explained what the error meant and some common ways to fix the problem. Going forward, I will remeber understanding the problem is integral to finding the solution. I also would not start to code without knowing where I want to end up and what I want to get out of the code. I will start writing a plan first so I have a clear picture of what I want to happen.

Overall, even with the strugles I had, I learned a lot about crafting a program and how I could improve the process for myself in the future. 
