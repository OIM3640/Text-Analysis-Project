# Text-Analysis-Project
Project Title: Text Analysis Project – Alice in Wonderland and Frankenstein

# Project Overview

For this project, I used two books from Project Gutenberg — Alice’s Adventures in Wonderland by Lewis Carroll and Frankenstein by Mary Shelley. The goal was to explore how Python can be used to analyze, compare, and visualize text data. I applied techniques such as text cleaning, stopword removal, word frequency analysis, and summary statistics. Through this I aimed to learn how language, tone and theme differ between these 2 distinct genres and allowed me to explore the deeper qualitative insights such as emotional tone.

# Implementation

The system is built with Python and Utilizes several libraries for different analysis techniques: 

Text Cleaning: Unnecessary characters, punctuation, stopwords and headers were removed, and text was converted to lowercase.

Word Frequency: The remaining words were counted with a Python Counter dictionary to identify the most common ones and its frequency and then I used the ACII bar chart to visualize the top 20 words. 

Sentiment Analysis: NLTK’s SentimentIntensityAnalyzer determined emotional tone per text.

Cosine Similarity: Scikit-learn’s TF-IDF vectorizer calculated how similar the two books were in vocabulary and themes.

Design Decision: Instead of heavy plotting libraries, I used an ASCII bar chart for visualization.

GenAI (chatgpt) has helped and guided me in optimizing the code 

# Results
The project acheived the following results:

Word Frequency:
Alice in Wonderland – Common words included said, Alice, little, Queen, and thought, reflecting a story driven by character dialogue and whimsical interactions.

Frankenstein – Frequent words such as life, father, eyes, shall, and man indicate a more reflective and emotional tone centered on human experience and morality.

Cosine Similarity:
The similarity score between the two texts was 0.25, meaning limited overlap in vocabulary and subject matter which makes sense as they are in completely different genres.

Sentiment Analysis:
Alice in Wonderland had generally neutral to positive sentiment whereas,Frankenstein showed more negative or somber sentiment with words suggesting conflict, guilt or emotional struggle.

Visualization:
The ASCII bar chart clearly highlighted differences — Alice is dominated by character dialogue, while Frankenstein emphasizes abstract and emotional words.
![alt text](image.png)

# Reflection
This project was both challenging and insightful. From a learning perspective, I realized the versatility of text analysis in understanding themes, sentiment, and content generation. Alice in Wonderland used simple, lively language with lots of dialogue, while Frankenstein had a heavier tone and more emotional depth. The low similarity score proved how different their writing styles really are. Cleaning the text, removing stopwords, and looking at word frequencies made me see how much detail is hidden in plain text. I also learned how sentiment analysis can capture the overall mood of a story without needing to read every line.
