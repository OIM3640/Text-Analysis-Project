# Text-Analysis-Project

Please read the [instructions](instructions.md).

***1. Project Overview*** 

What data source(s) did you use? What technique(s) did you use to process or analyze them? What did you hope to create or learn through this project?

For Assignment 2, I used the Data Source, Project Gutenberg. I specifically chose the ebook file of 
The Great Gatsby. I analyzed the whole book text individually, however, I also used the movie script
from the movie in order to create a Cosine Similarity to compare texts from the movie and the book.
I used the string.punctuation from the nltk library to make it easier for me to remove stop words, as well as printing the top 10 more frequent words , all words and their frequency in the book. Also, to make the analyzing and breaking down easier, I removed punctuation as well as making all words lowercase. With this project, I wanted to analyze and break down the text into detail, as well as see how the movie and book script compare to eachother. 


***2. Implementation ***

Describe your implementation at a system architecture level. You should NOT walk through your code line by line, or explain every function (we can get that from your docstrings). Instead, talk about the major components, algorithms, data structures and how they fit together. You should also discuss at least one design decision where you had to choose between multiple alternatives, and explain why you made the choice. Use shared links and/or screenshots to describe how you used GenAI tools to help you or learn new things.

We had worked on a similar exercise in class, so to start the project, I used the analyze_book.py code, where we analzyed Pride and Prejudice to give me a base on where I should begin. This really helped me in starting off with the right foot and showing me how my code should look like give or less. I modified it to fit what I wanted to do specifically. 

Because analyzing a book has a lot of text, it is not easy. Therefore, breaking it down was a very important component. I started off by removing stopwords like I mentioned before. In class, we had learned a different way of avoiding stopwords, but because you introduced the nltk library in the instructions, I decided to take a look to see what it had to offer. I found, throughout this link : "https://pythonspot.com/nltk-stop-words/" that you could install a tool that did it almost automatically. I retrieved the text using the urllib.request tool. Because the book was formatted well using a url, I decided to just use the url for the book part. However, the movie script was not formatted the best way, so I copy pasted the text and added it into my data folder. "https://transcripts.foreverdreaming.org/viewtopic.php?t=36773", this is where I got the movie script from. I removed the header as well as the text after the end marker to ensure only the text from the book was included in the word count. This is the reason why I also removed punctuation and stop words, and changed all text to lowercase, to only have important words/characters in the analysis, and make sure the format was the same for all text. 

When seeing the possibilities of the tools I could use to analyze the text, and read about the text similairty, I realized that comparing the book with the movie script would be very interesting. This way I could see how much directors/producers/writers modified the book to create the movie. However, I did not know how to go about this, so I presented ChatGpt with the prompt "If I wanted to compare the words used in the movie script with those in the book, how would I go about it?" It gave me a step by step guide on how to do this, explaining what vectorization was, as well as explaining the cosine similarity tool. 

I also encountered a problem when analyzing the book. I wanted the code to give me a list of every word in the book with its frequency, but also giving me the top 10 words used in the book. However, when I ran the code, it just gave me the lists of all words, not the 10 most frequent ones. I explained chatgpt that I was having this problem, and told me that instead of using hist, I should use the defaultdict tool. I modified my code based on AIs suggestion, and my code was able to run with no problems. 

3. Results (~1-3 paragraphs + figures/examples)

Present what you accomplished in your project:

If you did some text analysis, what interesting things did you find? Graphs or other visualizations may be very useful here for showing your results.
If you created a program that does something interesting (e.g. a Markov text synthesizer), be sure to provide a few interesting examples of the program's output.

I am a huge fan of the movie and the book, so this was a very exciting project for me. If you are a fan of the film/book, you know that Gatsbys parties are one of the huge components of the movie and book. This is why I decided to write a code that told me how many times the word party or parties was used. To my surprise, the number was lower than expected. Party was used 17 times, and party was only used 10 times. I was wrong and found it interesting how this word was very low, and other words were much higher than this. 

Also, I compared the movie script with the book. I expected to find great similarities in words. To my surprise, the cosine similarity resulted in a 0.0, meaning that it is nothing similar. I do not know if the format of the text of the movie script affected this result. but I did expect a way higher similarity. This was very interetsing to do, and I learned a lot by using new tools like the cosine_similarity function. Maybe you have some suggestions about what I did wrong in this code that would explain the 0.0 similarity, or maybe this is just the real result.


4. Reflection (~1-2 paragraphs)

From a process point of view, what went well? What was the biggest challenge? How did you solve it? What could you improve? Was your project appropriately scoped? Did you have a good testing plan?

From a learning perspective, what was your biggest takeaway from this project? How did GenAI tools help yo? How will you use what you learned going forward? What do you wish you knew beforehand that would have helped you succeed?


I think that the project went well. I feel like I felt more prepared than when I completed the first assignment. I feel like I have more knowledge with Python, and write code easier than before. Also, the analyze_book exercise we worked in class really helped me have a background on how this code should work, and helped me inmensely in having a base on where/how to start. I thnk the way I went about this project was very useful. I used the analyze_book file as a guide, modified to what I wanted to analyze. I then ran the code, and if it showed an error, then I would try to solve it myself. If I was still unsucessful, then I would provide ChatGpt with my detailed problem and ask how to fix it. AI was able to explain step by step what I was doing wrong, and what I should do to modify it. 

Overall, I felt way more confident completing this assignment. I used AI solely to explain and help if I had an issue, and felt more confident in my code and when I wrote it. I feel like each time with more practice I am able to identify what is needed to complete the output, and your lessons as well as the code really helps guides me in the right direction. Although doing a completely new process, which was compare the book with the movie was something challenging, I took the time to learn about the cosine and vectorization process, which made it easier for me to understand what I was doing. It was a very interesting learning experience for me. 


