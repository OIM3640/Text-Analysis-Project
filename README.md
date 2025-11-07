# Text-Analysis-Project

Please read the [instructions](instructions.md).


# Project Overview

For this project, I used "Oliver Twist" by Charles Dickens from Project Gutenberg. I learned how to download, clean, and analyze text using Python. I removed stop words, calculated word frequencies, and created visualizations like bar charts and word clouds. I also explored sentiment analysis using NLTK's VADER tool to understand emotional tone in the story. This helped me learn how Python can be used to process and analyze natural language.

# Implementation

I organized my project using Jupyter Notebook. The first part of the code downloads the text using `urllib`, and saves it to a file. Then I cleaned the text by removing special characters, lowercasing the words, and filtering out common stop words using the NLTK stopword list.

After preprocessing, I used Python’s `collections.Counter` to count word frequencies and used `matplotlib` to plot the top 10 words. I also used the `wordcloud` library to create a visual representation of the most frequent words. For my optional feature, I used NLTK's VADER sentiment analyzer to test the emotional tone of various sentences from the book. I had to choose between different libraries (like TextBlob vs VADER), and I chose VADER because it was easier to use with NLTK and well-documented.

# Results

After removing stop words, the most frequent words in "Oliver Twist" included “oliver”, “mr”, “said”, and “one”. This makes sense, as they are common character references and dialogue indicators.

The bar chart showed that “oliver” was by far the most mentioned word, with “mr” and “said” close behind. The word cloud gave a nice visual overview of these results.

The sentiment analysis results showed that many sentences had neutral or slightly negative tones, which makes sense given the book’s serious themes. Some sentences involving hope or friendship had more positive scores.

# Reflection

This was my first time working with text analysis and Python, so everything was new to me. One challenge was figuring out how to clean the text properly — there were a lot of characters and symbols I didn’t expect! I also had never used libraries like `nltk` or `matplotlib` before, but following examples helped me understand them.

AI tools like ChatGPT helped me step through the assignment when I got stuck. I learned how to ask questions, test small chunks of code, and build up the project piece by piece. In the future, I’d like to try text generation or compare multiple books.

