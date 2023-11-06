# Text-Analysis-Project
 
Please read the [instructions](instructions.md).

# IDEA:
CREATE A PROGRAM THAT DOES SOCIAL MEDIA LISTENING (USING GOOGLE/NEWS SEARCH AND REDDIT) & ANALYZES GENERAL SENTIMENT AND KEY WORDS ASSOCIATED WITH A COMPANY; THE PROGRAM PROMPT USER TO INPUT THE COMPANY THEY WANT TO RESEARCH AND WILL GIVE AN OUTPUT OF SNIPPETS FROM EACH CHANNEL, AN ANALYSIS OF THOSE SNIPPETS, AND A SUMMARIZED ANALYSIS OF BRAND PERCEPTION ACCORDING TO THOSE CHANNELS.

## EXECUTION PLAN (subject to change):
1. Datapull with news headlines & google cse api (in progress @ datapull_newsheadlines.py) 
2. Datapull with reddit (datapull_reddit.py)
3. Datapull with yelp (dataoull_yelp.py)
 *Decision point: Decide which pieces of data are valuable and how they are relevant amongst each other; Decide text analysis that is relevant for each
4. Data analysis for headlines, reddit, and yelp
5. User interface creation and testing (create function that requests the company name input and returns all analyses); will need to edit data pulls to accomodate and do some back and forth; MAKE SURE TO USE TRICKS TO AVOID ERRORS WE TRED IN SESSION 15
*Decision point: If everything works, what can I add? Do I have time to attempt more? etc.
6. Attempt program, make final edits, and edit readme to reflect application of finalized program


#**Project Overview** 

For this project, I used **Google Custom Search API**, **Newspaper3k API**, and **Reddit's API**. I used google CSE to generate URLs of news related to the company being investigated. This output was then used in combination with Newspaper3k article parsing to extract the text and store it into a list. I also used Reddit's API to gather some data on public opinion (which Reddit is the perfect forum for, however it has higher risk for not returning the specificed amount of comments if the company query doesn't show return enough results on Reddit). I compiled the text output from both sources into a single list and analyzed them using **Word Frequency Analysis** and **natural language processing** using the ***SentimentIntensityAnalyzer*** tool. To enhance the user experience with this analysis, I used ***tabulate***, ***matplotlib***, and ***numpy*** toolkits to create visualizations. ***Tabulate*** is used to summarize results of frequent words and their count; ***matplotlib*** and ***numpy*** were used to create a bar chart that summarized the average scores of each category in ***SentimentIntensityAnalyzer*** (neg, pos, neu, compound).

Through this project, I hope to learn how to use API's and access new tools by creating an analysis of brand perception / PR performance for a company based on news about it.

#**Implementation** 

My system begins at the ***config.py*** file, where the user should change the *company_query* variable to the company that is being researched. The ***num_results*** and ***limitcomments*** variables can also be edited to increase the amount of content being processed. 

In **datapull_newspaper3k.py**, googleapiclient tool is used to generate URLs and a for loop is then used to gather the article's text with newspaper and parse it. The text (str) of each URL article is stored on a list called: ***news_contents***. 

In **datapull_reddit.py**,  reddit API and praw are used to gather each submission in the list called: ***reddit_comments***.

* I had originally intended to use **"newsapi"** and **Yelp API** as additional sources of text for the analysis, but I sturggle to get these APIs to work. 

In the process of writing this programs, I used the help of ChatGPT to understand the functions related to each API and how to set the correct parameters. On the other hand, I had to make a decision between writing my program as functions or just writing the program as code. I decided to write only the text analysis as functions, given that datapull's programs didn't serve an additional purpose that couldn't be achieves with loops. However, if I intended to generalize the program's purpose and/or use some of the sub-components of the program, I would edit to define as functions. 

In **text_analysis.py**, I begin by creating a list called ***all_texts***, where the texts from both sources are put together for a joint analysis. The program then defines the function ***text_analysis***, which analyzes all texts together by creating a word frequency dictionary and creating a dicitionary the stores the average Sentiment Analyzer scores for each category and they are presented in a bar chart form. 

If __name___ = "__main__" idiom is used with function so that full program will run without being called


#**Results** 

This program allows the user to make configurations based on which company they want to research and how thouroughly for each source. The output for the text_analysis function gives a summarized, more self-explanatory version of average sentiment across the texts and words with their respective frequencies. A program like this would be particularly helpful internally for a company and using additional APIs to monitor social media and public perception of the company. The results are the right balance of qualitative and quantitative information since they allow for numerical and descriptive analysis of results. 

### When researching Fenty beauty (set in config.company_query):

Some of the words and frequencies that were relevant:
'brand': 55,  'Rihanna': 37, 'Kylie': 30, 'love': 29,  'Rare': 19 
C:\Users\mdominguezgonzalez1\Documents\GitHub\Text-Analysis-Project\image.png


the bar chart:
![Alt text](image-2.png)

This analysis would reveal that most comments are neutral, with more average positive than average negative texts.  Some of the frequent words include competitor brands and reference to the brand founder, Rihanna, which would reaffirm that the public associates the brand with her. For a company like Fenty beauty, conversations about the brand online can presumably affect sales much more than it would for a company selling standarized products. As a result, knowing the tone and sentiment expressed online is a must, with the next step being how to strategically improve the brand perception (and therefore tone of those conversations)


#**Reflection** 

From a process point of view, what went well? What could you improve? Was your project appropriately scoped? Did you have a good testing plan?
From a learning perspective, mention what you learned through this project, how ChatGPT helped you, and how you'll use what you learned going forward. What do you wish you knew beforehand that would have helped you succeed?


As I advance the data pulls for this assignment, I have struggled to access the YELP data using its API and determining ways to combine Google's CSE and Newspaper3k. As a result, for efficient learning purposes I have tweaked my project's objective to be more related to company news as opposed to brand perception online. In an effort to add more information to my analysis, I tried configuring NewsAPI as well, but it wasnt working well. 

In the process of writing the program, the hardest part was managing functions from the tools for which I didn't necessarily understand the parameters. ChatGPT was really helpful whenever I encountered this issue, as it explained options and outcomes of different parameters. As a result, ChatGPT was a great source of inspiration to explore tools that I wasn't familiar with and asking it to explain alternatives prompted more ideas of features I wanted to add to my program. 

I think I had a good testing plan, since I divided the program into smaller sub-programs and didn't proceed coding until a section was working perfectly. I wish I had understood beforehand how I could automate different parts of the program, since I could have written functions in a way that is more applicable to future programs. Additionally, I think that the way I wrote my program could be more efficient and there are ways I that I could edit the code so that results load faster. Specially for the word frequency component of the analysis, I wish I had created a bigger list of stop words so that more relevant results were shown.



