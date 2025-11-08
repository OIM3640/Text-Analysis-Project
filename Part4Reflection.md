1. Project Overview: The source that I mainly use is Project Gutenberg. Because the texts are already long enough, I choose to compare two long texts from the site Romeo and Juliet and The Comedy of Errors. Through this project, I hope to understand the vocabulary richness, the text's sentiment, and explore some of the most common words that appear in William Shakepeare's work. In order to get to these goals, I first have to clean the texts and process the texs. I use the package unicodedata to normalize the text and remove any unwanted characters such as HTML tags and special characters. Additionally, to remove stopwords so that I can get to the core meaning of the content, I use the package nltk.
2. Implementation:
Through the guidance of AI and what we learned in class in
the past few weeks, I begin to do my project by first, cleaning the text and and making sure that only the core content of the texts should be worth analyzing. Based on professor Li's instruction on how to download and open the url, I was able to pull out two of William Shakepear's texts and analyze them. Copilot provided me a step by step process on how to clean and process the data: for instance, how to normalize the text using unicodedata and how to remove unwanted characters such as HTML tags and special characters.

Additionally, VS code is very helpful in providing suggestions on what to do next the moment we started writing comments. For instance, after cleaning and processing the data, the analysis section seems very standardized with calculating the top 20 words, comparing common words between one text to the next and analyzing the average word's length in each document. Because I understand the concept of the dictionary, when to use length and set in the code, I mainly choose those codes rather than the alternatives since that is based on what I already learned rather than choosing something that is completely new. For instance, I did not use matplotlib nor seaborn mainly because I have not learned that yet. Even though AI gave good suggestions, I tried to tweak my code based on how long the texts are. Instead of printing the whole dictionary of all the words occured and how frequent they appear, I choose to work in a smaller set; for instance 500 words. If I were to work in another text like an instagram post, I would print the whole dictionary of all the words and their frequency. 

3. Results: Based on the text comparison between Romeo and Juliet and The Comedy of Errors, I find three very interesting insights. First, I look into the top ten words that appear in both texts. The chart below is a good demonstration of the top ten words. It is interesting to see that some of these top ten words are really ancient words that we don't usually use nowadays such as thou, thee, thy. 

Another interesting thing is that common words that appear in both texts. Based on the code, there are 1293 words that are common among the two texts that have the same author. 
The biggest surprise for me is the sentiment analysis. Considering that
Romeo and Juliet is a tragedy with two people die, the overall sentiment of the text is actually neutral rather than negative. Similarly, the sentiment 
in the text The Comedy of Errors are also neutral when I expect it to be more positive as a comedy implies that the text is funny and lighthighted. Both texts seem to be neutral and are approximately equally negative and positive. 

4. Reflection: 
From my point of view, the findings such as computing the average word length, sentiment analysis, finding common words, and the top ten words work very well and are very insightful. I like to see both texts alongside one another. Since, both texts use the same code, I can just copy and paste the first code I did from one text to another. I also enjoyed the data visualization; I got to learn how to use ASCII.

Something that did not work very well for me is installing the packages. For some reason, I keep getting errors and even if I have already installed it successfully before, if I rerun the code, sometimes it tells me that I do not have the package installed, so I have to reinstall it all over again. Another thing that froze my laptop for awhile is printing the dictionary where I count the frequency of the words in the text and print them one by one. I thought that I won't run into the problem, but since my text has around 25,000 words, printing 25,000 values freezes my laptop, so I had to force the code to stop running and instead only print about 50 words. 






