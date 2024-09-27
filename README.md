# Text-Analysis-Project
 
Please read the [instructions](instructions.md).


Project overview:
I chose the project gutenberg data set for my project. I started by characterizing the words with the word frequencies and got the top ten reoccouring words. These words were "a", "an", "the", "but", etc. So, next, I removed the stop words. Then I tried to look at the text similarity between two paragraphs in the data set to see how words may be similar when stories proceed. Lastly, I focused on the Markov text analysis to see if machine learning can generate a sententce, given the data set, that makes sense. I believe my hope from this was to see if machines understand how texts are written and have the ability to complete a text. The entire process is extremely mathematical and hence looking at the similarities within data would be of great help to see if the machine can finally respond with a sensible answer. 

Implementation:
In the first part, I cleaned up the code by removing punctuation, converting all text to lowercase, and splitting it into individual words using the 're' library. I also counted the frequency of each word and sorted it using the 'sorted' function. Then I used the 'nltk' library to remove the stop words and then the resulting text is joined back into a single string. Then I calculated the similarity between two different passages within the text using the 'fuzz' library. I calculated the "toen sort ratio" which is a measure of how similar the words are in these two passages. This was to return a score between 0 and 100. Finally, I performed text clustering using the sklearn library. I used the TF-IDF vectorization method to represent each document in the corpus as a vector of numbers. Then I used K-means clustering to group similar documents together. The resulting clustering is displayed as a binary matrix using matplotlib.

Results:
There were a lot of issues with my code, which I could not fix, resulting it in not working. 

Reflection: 
I believe that Chat GPT aided in my learning in terms of helping me understand what I could do with a data set in python and how to excute a given code. There are still a lot of doubts but I understood the gist of carrying out a text analysis and the power that python holds when it come to the analysis of any data set. 