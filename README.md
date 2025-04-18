# Text-Analysis-Project

## 1. Project Overview 

In this project, I analyzed the word usage patterns in two well-known novels by Jane Austen, Pride and Prejudice and Emma, both sourced from Project Gutenberg. I used basic Python techniques to download and process the texts, focusing on counting how often each word appears and comparing the word choices in both books. By doing this, I hoped to learn which words were most common in each text (excluding common "stop words" such as "the" and "and") and to see how similar the books are in terms of vocabulary.

## 2. Implementation

The code for this project is organized into three main parts: loading and cleaning the text, counting word frequencies, and calculating how similar the books are. First, I used urllib to load each text and then removed extra text at the start and end (like headers) by adapting the code we used during session 15 as well as punctuation and common words (or “stop words”) using the process_text function. This function created a dictionary of each word’s count, called a “histogram.” The next part identified the 20 most frequently used words in each book with the most_common function. Finally, I calculated the similarity between the books using a method called “cosine similarity,” which compares the frequency counts of words in both texts.

One choice I made was to use cosine similarity over other methods that could have been used to compare the similarity between the texts, such as comparing the total unique words or using external libraries. I chose cosine similarity because it considers both the specific words used and how often they appear, giving a better picture of how the books are alike or different. I also used a code suggestion from a GenAI tool to help build the cosine similarity function, which was helpful since this was my first time working with this kind of similarity measure.

## 3. Results 

The results showed some interesting patterns. In Pride and Prejudice, the most frequent words (after filtering out stop words) included names like "Elizabeth," and "Darcy," while in Emma, words like "Emma" and "Harriet" appeared often. This reflects each book's focus on its main characters. The cosine similarity score I calculated (around 0.8790) indicates a moderate similarity, meaning the books have some overlap in word choices but still stand apart. These findings suggest that while both novels are by the same author, they emphasize different characters and themes. Showing these word counts in a graph might make it easier to see the differences at a glance.

## 4. Reflection

Overall, the project went well, and I learned a lot about working with text data in Python. My biggest challenge was figuring out the proper syntax for removing stop words in both texts and adapting code that I already had to make it suitable for this project -- the code I had would take a file as an input and I needed to adapt it to take in text. The project felt well-sized, but I think it would have been even better if I had included some graphs or visual aids. The GenAI tools I used helped me build the cosine similarity function, which was new for me, and also suggested a better way to remove punctuation. Additonally, GenAI proved to be helpful when it came to debugging and figuring out where I had written incorrect syntax in my code, This project taught me more about text processing in Python, and going forward, I’d like to experiment with other ways to compare texts.
