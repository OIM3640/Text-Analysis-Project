# Text-Analysis-Project
 
Please read the [instructions](instructions.md).

# Project Overview

This project involved developing a Python script to fetch top headlines in the business and technology categories from the News API. The primary goal was to perform text analysis on these articles, aiming to identify the most frequent words and themes emerging in current news. By using techniques such as text parsing, stopwords removal, and frequency analysis, the project's goal was to provide insights into the dominant topics in business and technology news, thereby reflecting the current trends and interests in these fields.

# Implementation

The system architecture of this project is built around several major components. Firstly, the `NewsApiClient` from the `newsapi` Python package was utilized to fetch news articles. Secondly, the `Article` class from the `newspaper` package enabled downloading the content from the found articles from the url that was provided. For the text analysis part, the Natural Language Toolkit (NLTK) was used for stopwords removal and the `Counter` class from Python's collections module facilitated frequency analysis of the words.

A significant design decision was the choice between using a pre-defined list of stopwords versus dynamically generating this list based on the corpus. I opted for a mix of both, leveraging NLTK's comprehensive list of stopwords, as it offers a balance between simplicity and effectiveness, allowing for more focus on the unique content of the articles. And at the same time adding words that I believed were not effecient for the text analysis

Throughout the development, ChatGPT served as a valuable resource for troubleshooting and learning about the best practices in text analysis and data fetching techniques.

# Results

The text analysis of business and technology news headlines revealed several recurring themes and keywords. Specifically, on March 22nd, 2024, our analysis found:

- A total of 37 top headlines in both business and technology categories, with 3 articles not found using newspaper API.
- The top 10 most frequent words in the combined set of articles were: new (76), surface (46), said (43), pro (40), one (34), warzone (34), mobile (33), company (31), business (31), and duty (25).
- Identified entities included 67 PERSON entities, with notable mentions such as Jack Dorsey and Donald Trump; 70 ORG entities, including CNBC and Apple; and 25 GPE entities, highlighting locations such as Florida, UK, and South Korea.

# Reflection

From a process perspective, the project was a great learning experience. The scope was well-defined, and the implementation went smoothly, with effective testing strategies in place. However, there is room for improvement in expanding the analysis to include graphs and categorization for a more nuanced understanding of the news landscape.

ChatGPT played a crucial role in overcoming challenges related to API usage and text processing (here is my chatGPT history: https://chat.openai.com/share/d4aa9b35-1285-43c5-8b82-b2545a35a31d). This project not only enhanced my skills in Python programming and text analysis but also emphasized the importance of clear project scoping and iterative testing. Going forward, I will leverage these learnings to tackle more complex data analysis projects, incorporating advanced natural language processing techniques.

What I wish I knew beforehand was more about the limitations and challenges of working with different data sources and APIs, which would have streamlined the data fetching process. Some APIs are limited in their fetching capability so combining them is a great idea to overcome those struggles.
