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

Describe your implementation at a system architecture level. You should NOT walk through your code line by line, or explain every function (we can get that from your docstrings). Instead, talk about the major components, algorithms, data structures and how they fit together. You should also discuss at least one design decision where you had to choose between multiple alternatives, and explain why you made the choice. Use shared links and/or screenshots to describe how you used ChatGPT to help you or learn new things.

My system begins at the ***config.py*** file, where the user should change the *company_query* variable to the company that is being researched. The ***num_results*** and ***limitcomments*** variables can also be edited to increase the amount of content being processed. 

In **datapull_newspaper3k.py**, googleapiclient tool is used to generate URLs and a for loop is then used to gather the article's text with newspaper and parse it. The text (str) of each URL article is stored on a list called: ***news_contents***. 

In **datapull_reddit.py**,  reddit API and praw are used to gather each submission in the list called: ***reddit_comments***.

* I had originally intended to use **"newsapi"** and **Yelp API** as additional sources of text for the analysis, but I sturggle to get these APIs to work. 

In the process of writing this programs, I used the help of ChatGPT to understand the functions related to each API and how to set the correct parameters. On the other hand, I had to make a decision between writing my program as functions or just writing the program as code. I decided not to write functions given that they didn't serve an additional purpose that couldn't be achieves with loops. However, if I intended to generalize the program's purpose and/or use some of the sub-components of the program, I would edit to define as functions.

In **text_analysis.py**, I begin by creating a list called ***all_texts***, where the texts from both sources are put together for a joint analysis. 

**3. Results** (~2-3 paragraphs + figures/examples)

Present what you accomplished in your project:

- If you did some text analysis, what interesting things did you find? Graphs or other visualizations may be very useful here for showing your results.
- If you created a program that does something interesting (e.g. a Markov text synthesizer), be sure to provide a few interesting examples of the program's output.

**4. Reflection** (~1-2 paragraphs)

From a process point of view, what went well? What could you improve? Was your project appropriately scoped? Did you have a good testing plan?
From a learning perspective, mention what you learned through this project, how ChatGPT helped you, and how you'll use what you learned going forward. What do you wish you knew beforehand that would have helped you succeed?


As I advance the data pulls for this assignment, I have struggled to access the YELP data using its API and determining ways to combine Google's CSE and Newspaper3k. As a result, for efficient learning purposes I have tweaked my project's objective to be more related to company news as opposed to brand perception online. In an effort to add more information to my analysis, I tried configuring NewsAPI as well, but it wasnt working well.

