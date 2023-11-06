# Text-Analysis-Project
 
Please read the [instructions](instructions.md).

## Project Overview 
The aim of this project is to determine the overall sentiments—positive, negative, or neutral—in news article descriptions and to identify the most common words within these descriptions in relation to Venture Capital. To accomplish this, I extracted news data from the News API, which was provided in a dictionary format. I used two methods for my analysis: sentiment analysis through the NLTK library, and a frequency count of the most recurring words to analyze hot trends in the VC space.

A key lesson learned was the value of a review of the project's entire instructions before starting. This strategic planning was crucial in topic selection, because it made me ensure that the topic was compatible for later stages of the project. Understanding the API documentation was equally important, as it showed the specific limitations and features of the News API for example, understanding that the description was limited to 200 words and the max date to search for news.

The process also highlighted the importance of agile testing. With each code alteration, running the code was essential to ensure the changes produced the intended results. 


## Implementation 
The system consists of three main components: a news fetching module, a sentiment analysis module, and a word frequency counter. The News API fetches articles relevant to venture capital within a specified date range. Each article's description undergoes sentiment analysis using NLTK's SentimentIntensityAnalyzer, which creates a compound score to indicate the overall sentiment. To count word frequency, the system counts each word's occurrence while filtering out common English stopwords and specific terms to provide better results.

A notable design decision was made regarding the output format—whether to display sentiment as numerical scores or as labels (positive, negative, or neutral). As a viewer, I found it more straightforward to use the terms positive, negative, or neutral, so I wouldn't have to explain the numerical threshold meanings to the users.

### Graphs
Sentiment Graph: https://drive.google.com/file/d/1xn1PEL-iLxjY6g4p4PSow7OMlfklJlNY/view?usp=sharing 

Common Words: https://drive.google.com/file/d/1ATwvV2WN8b1ShKz5cq1-1YHLw4BhuUmu/view?usp=sharing 


## Results 

Out of 100 news articles analyzed, the majority (63 articles) conveyed a positive sentiment. This indicates that the current news coverage related to venture capital and associated topics is largely positive.There were 20 articles with negative sentiments, suggesting that while there is some critical or unfavorable news in the space. A smaller portion, 17 articles, had a neutral sentiment, indicating a balanced or factual reporting style without a strong positive or negative. Every article had a description available for analysis, so there were no gaps in the data due to missing descriptions.

The word "new" was the most frequent across the articles, appearing 17 times. This could imply a focus on innovation, new developments, or new players in the venture capital field.
The terms "company," "crypto," and "business" were also among the most common, which aligns with typical discussions in venture capital news, highlighting companies, cryptocurrency-related news, and general business topics. Other common words like "investment," "technology," and "startups" reflect the core interests and topics of venture capital, such as investing in emerging technologies and startup companies.
The presence of words like "pleased" and "said" suggests reporting on company statements and official announcements, which are common in business news articles.
These findings offer a snapshot of the current narrative in the venture capital and business news space, emphasizing positive developments and a keen interest in new ventures, with a particular spotlight on the cryptocurrency segment.


## Reflection 

The process of fetching data and performing sentiment analysis went smoothly, with the News API and nltk libraries facilitating most of the difficult parts. This was a very valuable project because it gave me the flexibility to explore my interests and get relevant insights. I used GPT to debug if something my code didnt run or somethign was working when adding new code from the websites either the sentiment or the API. I also asked gpt to give me feedback on my project overall and made changes accordingly. ChatGPT was instrumental in providing guidance on structuring the code and debugging. I also used GPT for one part to where it explained and guided me through crafting an effective if statement to exclude stopwords in the word frequency analysis that I wasn't sure how to do.

Something that I wish I knew beforehand that would have helped me succeed was just having a better practice on reading documentation from websites, for example, finding out that the descriptions were only limited to 200 words to fully understand my results. 

I actually wanted to start with news on babson college, then I realised that there wasn't news about Babson College and it probably had to do with the API and the news sources it was choosing. I asked different topics until I got the good results and relevant news articles, this is one of the reasons of why I chose VC, another main reason is because I work at a VC firm, so this is data that I can use and has immediate value to what I am currently doing.

I also learned things while going to office hours and getting feedback on my intital plan and code. I learned to wrap code into functions and playing with more concepts, this is why I decided to add the "count words function". I also realized that knowing the importance of total articles being analyzed is important so I added a counter to see the percentages of sentiments and see an overal landscape of the current VC ecosystem The professor told me that doing sentiment with shorter words was better thats why I decided to stick with doing a sentiment analysis for descriptions 

I created three different files during the entire process. The first, news.py, was used to test out the API. I initiated a second file rather than altering the original code, which would have made it challenging to track any errors. Upon integrating the sentiment NLTK library, I established a new file named sentiment.py. The final file, finalversion.py, consolidates all the features. This approach was beneficial as it kept me organized and ensured that my code functioned correctly in each stage. If an error occurred in the latest file, I had a previous working version to revert to.

Moving forward, I will leverage these skills to conduct more sophisticated text analysis, and be more meaningful and more specific about the sources I and APIs I use, I will do research and look at reviews from APIs before I use them. For example, understanding API alimitations before starting a project wil be important for my future project.

GPT Usage = https://drive.google.com/drive/folders/13sFMSH8_VoO3HFBw4hnQaFSMecD0jGV9?usp=drive_link 

