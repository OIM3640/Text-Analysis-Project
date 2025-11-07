# Text-Analysis-Project

Please read the [instructions](instructions.md).

Project Overview:

For this project, I did my best to apply the TF-IDF methods I learned in my Machine Learning class. However, although I had a solid idea of tokenization and such, I had issues performing those methods in Python rather than R Studio, which is something that AI helped me tremendously.
For this project I collected wikipedia articles as my main data source through the MediaWiki API from the mediawiki Python library. I collected data particularly from Apple, Microsoft and Samsung to compare the most frequently used terms in each article and identify the top TF-IDF keywords unique to each company since I wanted to find the differences of focus between companies within the same industry.

Implementation:
I used multiple Python files:
    - fetch.py (Uses MediaWiki to fetch article text for each topic.)
    - clean.py (Cleans and tokenizes text by removing punctuation, converting to lowercase, and removing stop words)
    - tfidf.py (Calculates TF, IDF, and TF-IDF scores using dictionaries and counters)
    - visualize.py (Generates bar charts of the top keywords and word clouds to visualize the most important terms)
    - main.py (Integrates all of the files above mentioned and also saves the output graphs in a figures/ folder)![alt text](image-1.png)

I applied the term frequency–inverse document frequency (TF–IDF) method to identify which words were most unique to each company’s article. Term frequency (TF) captured how often a word appeared in one document, while inverse document frequency (IDF) measured how rare it was across all three documents. The multiplication of the two gave each term a weight that emphasized words distinctive to a specific company. I then visualized the results with matplotlib bar charts and word clouds, saving each plot to a /figures/ directory.

A key design decision I faced was whether to analyze the text using TF-IDF or a sentiment analysis approach with libraries like NLTK. I chose TF-IDF because I was more familiar with it than NLTK.

Some issues I had, which made me glad that I kept on checking my results was this (![alt text](image.png)) since I had to make sure that I got rid of the Samsung('s) or else the TF-IDF will simply yield another result that doesn't matter that much.
Throughout the development of this project, I used ChatGPT to help debug TF-IDF weighting logic, manage file paths, and structure my functions cleanly.


Results:
Apple Top 10 TF-IDF![alt text](image-2.png)
Microsoft Top 10 TF-IDF ![alt text](../figures/Microsoft_top10.png)
Samsung Top 10 TF-IDF ![alt text](../figures/Samsung_Electronics_top10.png)
 
Apple WordCloud ![alt text](image-3.png)
Microsoft WordCloud ![alt text](../figures/Microsoft_wordcloud.png)
Samsung WordCloud ![alt text](../figures/Samsung_Electronics_wordcloud.png)

For Apple, top keywords like apple, jobs, macintosh, and iphone highlight the company’s focus on product design and its strong link to co-founders Steve Jobs and Steve Wozniak.
Microsoft stood out with terms like windows, azure, xbox, and gates, showing its history in software, gaming, and cloud computing.
For Samsung, words such as galaxy, semiconductor, and design reflect its strength in hardware, electronics, and large-scale production.

Overall, the graphs and word clouds show that each company’s Wikipedia article reflects its core identity — Apple with innovation and products, Microsoft with software and cloud systems, and Samsung with manufacturing and technology.

Reflection:

When starting this project, I knew I'll use AI alot, but I know the code might not always work whenever I asked it to do something. So before I started, I decided to be very direct and specific with what I wanted to do and created a step by step process to achieve it. Fetching first, then cleaning...., which made the procress much smoother. Initially I wanted to conduct sentiment analysis on Amazon products since it would help users find the most loved producted. I wish I was better at organizing multiple files and functions across different modules since it felt confusing at first. 
My biggest takeaways is that I should have a step by step plan when writing code. Just like how we need a docstring for functions, we need a plan for a project.
Overall, this project taught me not only about text analytics, but also about writing cleaner, modular Python code that’s easy to maintain and scale.


