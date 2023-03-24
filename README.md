# Text-Analysis-Project

Project Write-Up

Project Overview
In this project, I used the NewsAPI to extract news articles about Credit Suisse and identified the most frequent words in the titles of these articles. I then used the identified words to search for more news articles that contained these words. I extract data from the NewsAPI and the collections module to count the word frequency. The goal of the project was to investigate  about the coverage of Credit Suisse in the news due to it current situation, learn how to anlysis the core of article effciently by counting the frequency of words within its title and contents, and how to identify the cluster between two similar text by using python built-in function.


Implementation 
The implementation of this project was done in several steps. The first step was to extract the articles using the NewsAPI, which was done using the requests and json modules. After extracting the articles, I analyzed the text to find out the word frequency in the titles of these articles. This was done using the Counter module from collections. After checking the word frequency, I identified the words "UBS" and "takeover" as being frequently mentioned and decided to search for articles that contained these words. I used the NewsAPI again to search for articles containing these words. I used the NewsApiClient module to access the NewsAPI and made a request to the endpoint with the appropriate query parameters. I printed the headlines and URLs of the articles for both the initial search and the second search. In addition,  I extracted two articles from the website and did further text analysis about two articles: I first removed the stopword and the punctuation from article, then I count the frequency for words in the article and print out 10 most commoly used word in the article. Lastly, I identify the cluster between two similar text by Metric Multi-dimensional Scaling (MDS) to visualize the texts in a 2-dimensional spaceI 

One design decision I made was to use the Counter module to count the word frequency. I chose this module because it is a built-in module in Python and makes it easy to count the frequency of each word. I also chose to use the NewsAPI because I'm interested in the news report related to credit suisse.

Chapgpt assist and teach me a lot to finish this project.
First I use chatgpt to analyze the example code from NEWSAPI website to understand the parameters used when I define the URL.(see pt1 under image folder)Second, I use Chatgpt to help me debug my code when I try to access the article title from NEWSAPI, it help me to figure out which parameter I should keep or delete.(see pt2 under image folder)I also learn what are the benefits of computing the cosine similarity of two texts from Chatgpt. (see pt3 under image folder)Last, I learn what scikit-learn and how to use it in python to helo me do my text clustering analsyis.(see pt4 under image folder)



Results
The results shown meet my expectation. First, it's showed that Credit Suisse was frequently mentioned in the news with other financial institutions such as UBS because of the current undergoing takeover, which help me identify there is relationship betwwen two financial instituion by the word frequency analysis showed that UBS and takeover were frequently mentioned in the titles of these articles. However, it's suprisingly found that two articles have weak realtionship after conducting the text clusting analysis.(see text_clustering under images folder)



Reflection 
Overall, this project went well. The scope of the project was appropriately sized for the time allotted and the testing plan was good. However, I could have improved the testing plan by including more edge cases. The articles extracted from NEWS API are not easily readable. I plan to learn more text analysis tools in the future to help me organize articles and make it more readable.

From a learning perspective, I learned more about how to use APIs to extract data and how to process text data using Python. ChatGPT was very helpful in providing guidance on which modules to use and how to use them. If I had known more about the NewsAPI before starting the project, such as its required parameter, daily usage limitation, it would have helped me to succeed more quickly.