Write a summary of your project and your reflections on it in README.md, using Markdown format. There is no need to use fancy words or ChatGPT. The README.md file should consist of the following sections:

1. Project Overview (~1 paragraph)

Honestly, I found this project to be quite difficult, as I was working with outside data rather than just information stored in the python code itself. However, I thought it was a great way to understand how Python can be applied to real-world situation. For this project, I used the newspaper3k functions. The article that I chose, not surprisingly, was about soccer. It was an article about Messi winning the world cup. In order to process the data source, I used the newspaper3k functions which included the "article." functions as well as the "article.text" function. These functions allowed me to import the data from the article into the python file. I used the "characterizing by word frequencies" technique, "removing stop words" function, and the "NLP" function to view sentiment analysis. With this project, I hoped to analyze the sentiment of the article to see whether the article was simply a neutral article about Messi winning the world cup, or whether there was slight bias by the writer.

2. Implementation (~1-2 paragraphs + screenshots)

I knew that I needed to gather the data and clean the data in the best way possible so that the NLP sentiment analysis that I generated had the most meaning. Therefore, I needed to collect the data using the newspaper3k function, clean the data by removing dashes, spaces, and making the words into lowercase, and then used the stopwords.txt file to remove words that had 0 meaning to a sentiment analysis. Doing all of this hard work allowed for the best possible sentiment analysis.It was really important to know when to use lists, dictionaries, tuples, etc. Storing the data in a dictionary with keys and values was the best way to organize my data for sentiment analysis, as the sentiment analysis uses the frequencies of each word and calculates a percentage of positive, neutral, and negative. It was also important to use to the proper word functions such as "word.split, word.lower, word.replace" when cleaning the data.

A time where I needed to choose between multiple alternatives was when I was working with the sentiment analysis. I was considering the best way to store the data. And in the end, with feedback from chatGPT, I decided to create three different lists to store positive scores, negative scores, and neutral scores. This helped with the math behind the average scores and made it way easier to do the division to solve for the average sentiment scores. I don't have screenshots from when I used chatGPT but I worked with it a lot for this project. I've been struggling with the lists, dictionaries, and tuples section, and chatGPT acted as a tutor. I essentially would ask chatGPT to give me suggestions on my code and ask if there were any mistakes. ChatGPT would provide me with suggestions and sometimes I would take those suggestions and other times I would reject them.

3. Results (~2-3 paragraphs + figures/examples)

The main finding comes from the sentiment analysis that I conducted. However, I did do a decent amount of text analysis, such as text cleaning and removing stopwords. I thought it was interesting how many stop words there were; words such as "a, and, but," etc. Once these words were taken out, there was much more meaning in the potential sentiment anaylsis.

As stated in the project overview, I wanted to see whether there was any bias in the way the author wrote this article. Of course this article is going to be positive, because it will be about winning the world cup, however, if there is mostly neutral sentiment then we can infer that there probably wasn't much bias. After running the code, taking into account the removal of spaces and dashes, and removing the stopwords, we can see that "The current sentiment in the Messi article is 9% positive, 4% negative, and 86% neutral". I think this allows us to determine that there wasn't much bias from the writer, and that most of the words/sentiment in the article is mainly neutral/factual.

However, what I find to be interesting is the fact that there is 4% negative sentiment. This could be because there is mention of a team losing or maybe some of the mistakes that players on the other team made. 


4. Reflection (~1-2 paragraphs)

As stated before, I thought that this project was pretty difficult. I struggled a decent amount with the cleaning of the data. There were times where I wasn't sure when to use lists or dictionaries, and that's where chatGPT played a helpful role in the process. I would ask which data storage function to use when storing data or generating frequencies for data and it really helped out.

I thought that the first and last functions were the easiest for me, mainly because the calling and the format made the most sense to me. It was really cool to use newspaper3k function. I had no clue that you were able to source information and words from an article into python. 

Overall, I was happy that this project really challenged me. I think it did a good job solidifying my understanding of text analysis and it was awesome to see how I could conduct sentiment analysis through python.