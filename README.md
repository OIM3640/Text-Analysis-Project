# Text-Analysis-Project
 
## Project Writeup and Reflection

### 1. Project Overview (~1 paragraph)
#### What data source(s) did you use? What technique(s) did you use to process or analyze them? What did you hope to create or learn through this project?

For the data sources of the project, I downloaded two books from Gutenberg. One is "The Great Gatsby" by F. Scott Fitzgerald, and the other one is the "The Age of Innocence" by Edith Wharton. I chose these two books because they share the similar themes of exploration of social change, the American dream, etc. The primary techniques I used to process and analyze the data are basic word statistics analysis, word cloud analysis, sentiment score analysis, and text similarity analysis. In this project, I hoped to dive into comparing and contrasting between texts, "The Great Gatsby" and "The Age of Innocence", while using and studying different technique of data analysis and visualization using python. 

### 2. Implementation (~1-2 paragraphs)

#### Describe your implementation at a system architecture level. You should NOT walk through your code line by line, or explain every function (we can get that from your docstrings). Instead, talk about the major components, algorithms, data structures and how they fit together. You should also discuss at least one design decision where you had to choose between multiple alternatives, and explain why you made the choice. Use shared links and/or screenshots to describe how you used ChatGPT to help you or learn new things.

The data sources of this project is retrieved through downloading two books from Gutenberg using urllib, which allows people to download contents from online website and save them in local files using json.To make the analyzation process easier, I first preprocessed the text data to conduct simple data cleaning, including stripping unneeded characters like puctuation and whitespace, identifying when the text processing should start and end, seperating hyphenated words, and splitting each line into formatted words. 

The major component of this project are functions to calculate words statitics in the two books. For example, number of total words, number of different words, and common words' frequencies. To better visualize the common words' frequencies of the two books, I also generated a word cloud usng the WordCloud library, which vividly present the frequencies using different colors and font size. In addition, I utilized natural language processing, using the NLTK library, to get the sentiment analysis score of the books. This helps to identify the negative, neutral, and positive sentiment in the text. After that, I used the fuzz library to learn about the text similarity ratio between the text. To better manage my program, I used the 'main' function to put various programs in one execution. 

# Design decision: no partial ratio, word cloud
# Links, screenshot, gpt



### 3. Results (~2-3 paragraphs + figures/examples)

Present what you accomplished in your project:

If you did some text analysis, what interesting things did you find? Graphs or other visualizations may be very useful here for showing your results.
If you created a program that does something interesting (e.g. a Markov text synthesizer), be sure to provide a few interesting examples of the program's output.

### 4. Reflection (~1-2 paragraphs)

From a process point of view, what went well? What could you improve? Was your project appropriately scoped? Did you have a good testing plan?

From a learning perspective, mention what you learned through this project, how ChatGPT helped you, and how you'll use what you learned going forward. What do you wish you knew beforehand that would have helped you succeed?