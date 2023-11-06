# Text Analysis Project

## Project Overview
I used the Wikipedia page on Panama as my text data source. I extracted the page content using the MediaWiki API and then analyzed the text by computing word frequencies, keywords and translating the summary to Panama's main language. My goal was to explore different techniques for analyzinga and manipulating text from a web page. 

## Implementation
In this project, three major components played pivotal roles. Firstly, the utilization of the MediaWiki API to access Wikipedia's "Panama" page content provided an efficient alternative to direct webpage scraping. Additionally, the Natural Language Toolkit (NLTK) was instrumental in various natural language processing tasks, including text tokenization, stopwords removal, and keyword extraction using the Rake algorithm. Lastly, the Google Translate API, facilitated by the googletrans package, seamlessly translated the summary to Spanish, eliminating the need for building a translation system from scratch.

Several key algorithms were applied for text analysis. Word Frequency Analysis involved tokenization, filtering of stopwords, numbers, and punctuation, and the use of the Counter to identify the top 10 most frequent words, shedding light on the primary topics covered. The Rake Keyword Extraction algorithm efficiently extracted keywords and key phrases based on word frequency and co-occurrence, generating the top 10 ranked keywords from the page. Various data structures, such as a Set for Stopwords, Counter for Word Frequencies, and List for Clean Tokens, were employed to streamline data handling and analysis.

The decision to leverage the MediaWiki and Google Translate APIs rather than developing scraping and translation systems from scratch simplified the code by utilizing robust existing packages. However, it necessitates reliance on external service availability and usage limits. Throughout the project, ChatGPT proved invaluable in providing coding assistance, helping to troubleshoot issues, and offering guidance on how to tackle various tasks, enhancing the overall development process.

## Results

## Reflection