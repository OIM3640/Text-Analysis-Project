# Text-Analysis-Project

Please read the [instructions](instructions.md).

# Project Overview
 In this project, I worked with data from the text "The Great Gatsby" by F. Scott Fitzgerald, retrieved from Project Gutenberg's online repository. My goal was to analyze the text by calculating the word frequency of the word "Gatsby" to see how often the main character's name appeared on the text. By studying the word patterns, I wanted to gain insights into the text's language, observe common words that shape the novel's themes, and see how frequently certain terms contribute to the story's plot. Using an online text source allowed me to practice accesing and processing large text files, while focusing on basic text analysis helped me improve my Python skills in handling real world data.

 # Implementation
 The project structure is divided into four main files, each with a distinct purpose that contributes to the overall project. The first file, 'text.py', includes a function that fetches the text from a URL using Python's urllib library. This function connects to Project Gutenberg, downloads "The Great Gatsby" and converts it into a text format suitable for processing. Using an online source provided a dynamic way to access data and made it possible to replace the text file with other texts in the future, which makes the structure flexible and scalable for future projects. 
 
 The second file 'frequency.py' is dedicated to analyzing the text's word frequencies. This file includes a function that reads through the fetched text, splits it into individual words, and counts each word's occurrence. An additional counter tracks how often "Gatsby" appeaars separately from other words, allowing for targeted analysis of the main character's mention frequence. A key choice I made was to limit the results to the top 10 most frequent words to keep the output manageable by highlighting only the 10 most important. 
 
 The third file, 'statistics.py', contains functions responsible for outputting key statistics from the analysis. Specifically, print_gatsby_count outputs the total number of times “Gatsby” appears in the text, while print_top_words displays the top 10 most frequently occurring words and their counts. This approach kept the data processing separate from the data presentation, ensuring that each file handled a unique part of the analysis workflow. 

Finally, main.py acts as the central folder for coordinating these functions. It calls the functions from text.py, frequency.py, and statistics.py in sequence, gathering the text, processing the word frequencies, and outputting the results. By consolidating everything into main.py, I kept the structure organized and could easily make adjustments in one place without changing each individual file.

 # Results

Running the program provided several meaningful insights into the language and style of *The Great Gatsby*. The word “Gatsby” appeared 176 times throughout the text, reflecting the main character’s significance and giving a glimpse into his role within the story’s narrative. Counting “Gatsby” helped underscore his presence and influence, showing just how central he is to the novel’s plot and themes. In addition to this specific analysis, I was able to identify the top 10 most common words in the text. Expectedly, many of these were function words or conjunctions.

Top 10 words and their frequencies:
the : 2544
and : 1566
a : 1442
of : 1224
to : 1198
i : 1000
in : 850
he : 771
was : 762
that : 566

This word frequency analysis offered a new perspective on the novel's language by isolating the key terms that shape its tone and style. If time permitted, I would have liked to represent these word frequencies visually, using either a word cloud or bar chart to make the patterns more engaging and clear. Visual representations would add an additional layer to the analysis, showing the frequency distribution and giving a fuller picture of Fitzgerald's language style. Despite the lack of visuals, the text analysis alone revealed meaningful patterns and reinforced some thematic elements of the story, aligning with what I expected given the novel’s subject matter.

## Reflection

Looking back on this project, I feel that it was a valuable experience, especially as it taught me about working with external text data in Python. One challenge I had was managing the text file’s size and ensuring the analysis was efficient, as processing an entire book can be intensive. To address this, I structured the program to handle only necessary functions and limited the output to the top 10 words, which kept the program efficient and results-focused.

From a learning perspective, this project helped me gain confidence in text processing and data retrieval, particularly by showing how to clean, split, and count words effectively. Using GenAI tools provided additional support, especially in finding examples of how to handle large text files and manage online data sources, and correcting my code when it wasn't working. This guidance was helpful in implementing a structured approach to the project. This project was a strong foundation, and I feel more prepared to handle similar tasks and data challenges in future projects.