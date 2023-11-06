Text Analysis Assignment

1. Project Overview

For this project, I want to compare two different news sources' perspectives on the Israel and Palestine war. I gathered an article from Fox News, a typically right-leaning news source, and from MSNBC, a left-leaning news source. I made sure both news sources represented two different political parties so that I could analyze their reports on the conflict. Does one side use more harmful verbiage? Can you tell which party supports Palestine and which supports Israel? What are the most frequent words used in both of these articles? What is the tone of voice, positive, negative, soft, or aggressive?

My script for part 1 uses the News API to fetch articles, then BeautifulSoup to scrape the content, and the Textblob library to perform a sentiment analysis on key words found in the title of the articles. In Part 2 I perform a sentimental analysis on both articles, an LDA analysis, and a Text clustering analysis using sklearn.manifold and matplotlib.

2. Implementation

In part_1 of my code, I am fetching my articles, analyzing the content, and then saving them in two different text files: Fox.txt and MSNBC.txt. I began by making a function that constructs a URL for a GET request to the NEWSAPI using certain parameters related to the Israel-Palestine conflict, then processed the response. My get_word_frequencies function takes a list of titles, then tokenizes the titles into words, removes stops words, and calculates the frequency of each word. I did this to analyze the most frequent words used in the title of the articles. I wanted to see the differences in keywords that both Fox News and MSNBC use in their title. Titles capture the attention of readers, therefore it was interesting to see if these words were biased or shed light on the tone of the article.

The Part_2 of my code I am performing a sentiment analysis with VADER, and Topic Modeling analysis with LDA and a Text clustering analysis with MDS.

I used ChatGPT to analyze the example code from the News API website to understand the parameters I should use for my topic. At first, my parameters were too broad and ChatGPT helped me narrow it down to include this: ‘q=("Israel Palestine war" OR "Hamas" OR "Gaza") AND (conflict OR war OR bombings OR airstrikes)&'.

I also used ChatGPT to help me debug my code when I was accessing the full text from my news articles using the News API.

I decided to use the News API because it had a broad array of different news sources and It was easy to use. Initially, I tried to used ChatGPT and YouTube videos to extract a New York Times article but they seem to have more protections around web scraping and extractions. After spending hours on it, I was unable to do it and moved to the News API. I also chose to use the counter module to count the word frequencies within the titles. I chose to do this simply because it is a built-in function in Python therefore making it easier to use.

3. Results
Sentimental analysis
(VSCODE Output Terminal)

Sentiment results for Fox.txt: {'neg': 0.166, 'neu': 0.8, 'pos': 0.034, 'compound': -0.995}

Sentiment results for MSNBC.txt: {'neg': 0.191, 'neu': 0.71, 'pos': 0.098, 'compound': -0.999}

I performed a sentimental analysis on the text files that I extracted from Fox News and MSNBC. The article on Fox News resulted in a compound score of –0.995, suggesting a strong negative sentiment in the text. Similarly, MSNBC received a compound score of –0.999 also indicating negative sentiment (even more than Fox News). Both newspaper articles had a very high neutrality score. This surprises me as some of these article's tone and storytelling are indicative that they are in favor of one party in this war. The neutrality suggests that these were both factual-based pieces.

LDA Analysis
Fox News:

(0, '0.056"," + 0.042"." + 0.013*"israel" + 0.013*"hamas"')

[(0, 0.99780357)]

MSNBC:

(1, '0.056"," + 0.047"." + 0.022*"gaza" + 0.020*"civilians"')

[(1, 0.9991627)]

The Fox News results suggest that the article is characterized by mentions of Israel and Hamas. There were also high frequencies of periods and commas, which makes sense considering this is a professional news reporting source. The second output suggests that the content of the article is 99.78% associated with the terms Israel and Hamas.

The MSNBC news results suggest that the article is characterized by mentions of Gaza and civilians. There were also high frequencies of commas and periods. The analysis found that this article focused more on the civilian experience in Gaza. This is more so of what I predicted before I did this analysis. MSNBC given that they are more liberal, tends to report more information on Palestinian citizens of Gaza, their experience and the hardships they are going through. Fox News likes to focus on the American republican party and their assistance and loyalty to Israel. Its more political while MSNBC is more humane. The second output for MSNBC suggests that the content of the article is 99.92% associated with the terms Gaza and civilians.

This LDA analysis reflects the different angles and perspectives taken by Fox news and MSNBC on the Israel versus Palestine war.

Metric Multi-dimensional Scaling Analysis
I used ChatGPT to help me analyze the results of this plot. From ChatGPT, I was able to learn that this type of analysis is not the most fitting or appropriate for my project. Any MDS analysis usually expects more documentation for a more comprehensive interpretation of the results. However, because I only used two articles, the results and clusters are not very meaningful.

The positioning of the clusters suggests that the MDS algorithm found the two articles to be different in terms of the topics they covered. The axes are labeled with 1e-9 and 1e-7, which indicates that the scale is quite small. The distances you're seeing on the graph are in the order of 10^-9 for Fox News and 10^-7 for MSNBC. This means that even though the points seem separated on the graph, the actual difference in topic distribution is still very small.

4. Reflection
From a process point of view, what went well? What did you learn? What could you improve upon if you had more time?

Overall, I think the project was successful in terms of achieving the basic functionality of fetching, processing, analyzing, and visualizing data from different news sources regarding a sensitive topic. One of the key lessons from this project was understanding the importance of precise parameters while fetching data from an API. Incorrect or vague parameters can lead to a vast and unmanageable dataset, or not enough data at all.

Additionally, I learned that different sources have different levels of protection against web scraping, which can make it difficult to obtain information. As a result, choosing the right tool or API for data extraction is crucial.

If I had more time, I would like to refine the sentimental analysis to better capture the nuances of the language used in the articles. I could also explore more news sources to get a broader range of perspectives and implement a more robust MDS analysis with additional data. Furthermore, integrating an automatic way of identifying biases and measuring the extent of their influence on the reporting could also enhance the project.