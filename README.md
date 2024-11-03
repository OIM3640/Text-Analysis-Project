# Text Analysis Project

## 1. Project Overview

This project focuses on analyzing text data from Wikipedia to understand content and sentiment patterns about Babson College. The main data sources used were Wikipedia articles on "Babson College" and "Entrepreneurship." The project involved processing text data through word frequency analysis, summary statistics, sentiment analysis, and text similarity calculations. Through this project, I aimed to learn more about natural language processing techniques and gain hands-on experience with sentiment analysis and text similarity using Python libraries such as NLTK and TheFuzz.

## 2. Implementation
The project is organized into three main files: data_collection.py, text_analysis.py, and main.py. The data_collection.py file fetches and cleans article content from Wikipedia, while text_analysis.py includes functions for word frequency calculation, summary statistics, sentiment analysis, and text similarity analysis. The main.py file orchestrates the execution, combining these components to perform the overall analysis.

A fourth file, part3.py, demonstrates how ChatGPT assisted in consolidating the separate components (data_collection, text_analysis, and main execution) into a single, more concise script for efficiency. This process involved restructuring the code and ensuring that each function was self-contained and reusable. ChatGPT also provided guidance on checking errors and optimizing the code, especially for stop word removal and sentiment analysis setup.

## 3. Results

The text analysis provided interesting insights into each article. For example, the word frequency analysis highlighted the key topics in each article, with terms like "babson" and "business" ranking high in frequency for Babson College and "entrepreneurship" and "business" for Entrepreneur article. However, words related to "entrepreneurship" only exist once in the Babson text, which is surprising for Babson since it is known for its entrepreneurship. The sentiment analysis for both texts showed a largely neutral tone, with a slight positive inclination, reflecting the informative and factual nature of Wikipedia articles.

The similarity scores calculated between "Babson College" and "Entrepreneurship" articles revealed a moderately high similarity, as expected due to the shared themes for business. The `fuzz.ratio`, `fuzz.partial_ratio`, and `fuzz.token_sort_ratio` metrics offered a nuanced understanding of how similar these articles are at different levels of text comparison.


## 4. Reflection

Overall, the project went smoothly. It was difficult in the beginning since there was too much data and materials need to be handled. To solve this issue, I started by setting up with separate files, which allowed for better organization and modularity. The most challenging part was managing the stop word removal effectively to ensure clean word frequency analysis. I resolved this by using NLTK’s built-in stop word list. In retrospect, I could further explore other similarity measures or analyze more articles for broader insights.

The project was a valuable learning experience, especially in using GenAI tools for quick troubleshooting and exploring library functionalities. Moving forward, I would consider expanding my use of these tools for more advanced natural language processing techniques. A prior understanding of text similarity methods could have helped me scope the project more efficiently from the start.