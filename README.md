# Text-Analysis-Project
Please read the [instructions](instructions.md).
###########    Project Overview ##############
I have designed this project to provide a simple Sentiment Analysis on literary text especialized from Project Gutenberg. It has been seperated into four parts as it made tracking all the different parts much easier. The first part was designed to Clean and proccess the txt files; removing punctuation, "stopwords" and pronouns. In the same file it calculates word counts, summarized statistics(words, Unique Words, and Average Word Length), lastly it prints the most used 5 words in each article. 

###########        Data Used          ###############
I utilized two types of files while testing the project
Type 1: Text Analysis Files, these were the trial points for understanding the positive and negative junctions of my project
Type 2: Positive and Negative Identifying Files, these 2 Files were brought in too create a wide scope of what counts as a positive or negative sentiment word and these were obtained from Kaggle as a Sentiment Analysis Database
###########   Methods and Processing   ##############
Step 1: Text Loading - essential step to read and remove Project Gutenberg's header and footer
Step 2: Clean and Filter - coverts all text into lowercase; removing case seperation caused by Capitalization. In additon to removing punctuation, and filtering out stopwords and pronouns; because it would be noise to the analysis, since needer words should hold a polarity
Step 3: Counting - provides counts of simple summarized stats (total words, unique words, and avg word length) for the simple reason of understanding more from the text
Step 4: Sentiment Analysis - My personal favorite part of the project as it allowed me to explore the method of understanding a simple sentiment analysis, while also giving me ideas of developing my own version of understanding (There's much room for improvement). Ultimately this step required the loading of two files to identify positive or negative and using a simple count for each, we can calculate a score in the range of -1 or +1 
Step 5: Visualization - This step was much more complicated for me, struggled with packages and python versions left me using with the intent of creating 2 types of charts. A plotted version of the Sentiment Analysis of all books, and a histogram plot of the top 15 words from each text (I failed to accomplish this one).


###########    Output Description   #############
The analysis found that *Little Women* and *Laugh and Live* had the most positive sentiment scores,
while *The Iron Heel* and *Studies in Pessimism* leaned more negative. 
The text leviathan showed minimal polarity which can be expected from a book covering concepts of a bad present needing change for a better future
The visualization highlights the contrast between texts with uplifting themes and darker philosophies.

Some possible outputs include:
Laugh and Live.txt: +0.264
Leviathan.txt: +0.070
Little Women; Or, Meg, Jo, Beth, and Amy.txt: +0.207
Optimism An Essay by Helen Keller.txt: +0.106
The Essays of Arthur Schopenhauer; Studies in Pessimism.txt: -0.093
The Great Gatsby.txt: -0.095
The Iron Heel.txt: -0.153
We.txt: -0.009

#######################################################                     Section 3
#######################################################
During the Course of the project the usage of AI was primaraly used to understand the different segments within the Instuctions, as a formating tool that provided a checklist of all necessary components, as a debugging tool, and lastly as a learning tool when it came to understanding the Viusalization library that was completely new to me. (In addition to helping fix my directories and library downloads)

################        Sources        ################
## References
- Project Gutenberg (https://www.gutenberg.org/)
- Kaggle-Prajwal Kanade- Sentiment Analysis Word Lists Dataset(2023) (https://www.kaggle.com/datasets/prajwalkanade/sentiment-analysis-word-lists-dataset? esource=download&select=positive-words.txt)
- Babson OIM3640 Text Analysis Project Instructions
