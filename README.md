# Text-Analysis-Project

# Project Overview

The main data source I used was Wikipedia, specifically, I looked at the Wikipedia articles of Babson College and Bentley University. I wanted to compare two articles of groups that are direct competitors of each other to see if their articles are similar. Since I chose two colleges, I wanted to see if the verbiage used in both was similar or different. The program that I created analyzes both texts in 4 ways: 
- 1) Text Similarity
    - Uses the 'thefuzz' library to compare the similarity of both text strings as a ratio and returns that ratio.
- 2) Sentiment Analysis
    - Uses the 'nltk' library to conduct a sentiment analysis for both articles and then compares the values.
- 3) Word Frequency
    - Creates a dictionary that stores the most common words in descending order for each value. It then prints a bar chart using mathplotlib if requested by the user.
- 4) A Word Checker
    - Has the user input a word and then checks both articles to see if that word is present.

# Implementation

The project is structured in a question/answer format where the program prompts the user what type of analysis they would like to conduct. They can choose between each of the four analysis methods and depending on their answer, it runs the corresponding function. This function is recursive, so it continuously runs until the user tells the program to stop running analysis. I chose to have the program run this way because I wanted it to be as interactive as possible. Originally, I had the program set up where it would automatically run every function but after further testing, I found the project to be one-dimensional. When creating the new function, I wanted to implement a way for the user to continue asking questions without feeling like they exhausted the program – this was why I created the Word Checker. Since there is an infinite number of words that the user can check, the user could continue checking different words to see if they are in both articles. This made the program much more useful, especially since the Word Frequency function only visualizes the top words in each article.

I used ChatGPT in 3 instances: twice to idea generate when I was stuck and once to troubleshoot a broken function.
1.	Reversing a Dictionary (https://chat.openai.com/share/dcca8c2a-3cfd-4c37-84c6-1c63ad7d8474)
    - ![Screenshot of ChatGPT responding to the question "how do i sort a dictionary in descending order in python?" With python code that uses the function sorted() to reverse a dictionary.](/images/reversedictionary.png)
    - While writing the function wordFrequency(), I already knew how to create a dictionary with a list of words & how many times they appeared in a text but I did not know how to sort it in descending order. I tried using sorted(), but I forgot that I needed to next that function under dict(). Additionally, it didn't sort it from highest to lowest, but from lowest to highest. After consulting ChatGPT, I learned that I needed to use this function: dict(sorted(babo_frequency.items(), key=lambda item: item[1], reverse=True)). I didn't know that the sorted() function had parameters that you could use to sort it in a reverse order, but after using ChatGPT I was able to use it to reverse the sort of the dictionary to optimize my wordFrequency() function.
1. Creating a Bar Chart (https://chat.openai.com/share/289e130d-16f4-4ef8-ad07-5ec183ce124f)
    - ![Screenshot of ChatGPT responding to the question "how to make a bar chart from a dictionary that lists the most common words in a piece of text in descending order?" ChatGPT responds with step by step instructions on how to do so with attached code.](/images/barcharttext.png)
    - ![Screenshot of ChatGPT responding with code to the question "how to make a bar chart from a dictionary that lists the most common words in a piece of text in descending order?".](/images/barchartcode.png)
    - After I finished the function wordFrequency(), which displayed via text the most frequent words, I wanted to display this visually but I did not know how. After consulting ChatGPT, I learned that you could use mathplotlib to plot a bar chart using the dictionaries that I created in the function. I used the base function that ChatGPT provided and then customized it to change the size of the bar chart based on how many words the user wanted to analyze.
1. Troubleshooting wordChecker() (https://chat.openai.com/share/d97f9f09-c71e-48ae-ae6e-f15883560c57)
    - ![Screenshot of ChatGPT responding to an input of code with the request to check and correct the error. ChatGPT responds with step by step instructions on how to fix the code along with a fixed version of the function.](/images/wordchecker1.png)
    - ![Screenshot of ChatGPT responding to an input of code with the request to check and correct the error. ChatGPT responds with step by step instructions on how to fix the code along with a fixed version of the function.](/images/wordchecker2.png)
    - While creating the wordChecker() function, I ran into the issue where I inputted a word that was present in the article but it printed that it was not present. After trying to troubleshoot where my error was, I couldn't find what line caused the issue so I consulted ChatGPT. After consulting, I realized that I forgot to make the list of both dictionaries (after using split()) lowercase which caused issues when comparing the parameter with the overall text.


# Results

## Text Similarity

The similarity between Babson's and Bentley's Wikipedia articles is 63%. How the function works is it sorts the entire article based on word (via a list) and then compares the similarity between each text using the Levenshtein distance. 

## Sentiment Analysis

- There is more negative verbiage in Bentley's Wikipedia page than Babson's. The value of neg for Babson is 0.0 whereas the value for Bentley is 0.008.
- There is more neutral verbiage in Babson's Wikipedia page than Bentley's. The value of neu for Babson is 0.931 whereas the value for Bentley is 0.91.
- There is more positive verbiage in Bentley's Wikipedia page than Babson's. The value of pos for Babson is 0.069 whereas the value for Bentley is 0.082.
- The compound valuein Bentley's Wikipedia page is higher than Babson's. The value of compound for Babson is 0.9977 whereas the value for Bentley is 0.9981.

This means that the Bentley University article has more emotionally charged language than Babson (hence the higher negative and positive verbiage values). This is important to keep in mind when reading wikipedia articles because they are supposed to be as impartial as possible since they are supposed to be articles based on facts. That being said, even though the value is higher than Babson's, it is still relatively low, which means that it is not heavily biased.

## Word Frequency
![Screenshot of Bar Chart showing the top 5 words in the Babson Wikipedia Article](/images/top5babson.png)
![Screenshot of Bar Chart showing the top 5 words in the Bentley Wikipedia Article](/images/top5bentley.png)

It makes sense that the most common word for both schools would be the name of their school; however, I found it intriguing that Bentley was present in their article twice as many times as Babson (50 and 23 times, respectively). This is most likely due to a difference in authors and writing style.

Additonaly, looking at the second most common word, it was interesting that for Babson it was "mba" and for Bentley it was "men's". Babson isn't well known for its MBA program, so it is interesting that it was mentioned as much as it was. Looking deeper into the article, you can see that under "Alumni" some are listed as MBA graduates, which would attribute to this count. As for Bentley, I was surprised that a gendered term, "men's" was the second highest count with 20. When I looked deeper into the content of the article, the reason why it showed up so much was because of Bentley's athletics program, where their men's program is strong & has plenty of notable alumni. These two words show the difference between the student body of both colleges: Babson students are more well known for their business studies whereas Bentley is more well known for their athletics.

# Reflection

After concluding this project, I felt like it went very well overall. I was able to compare the similarities and differences between Babson and Bentley's articles and I found interesting data that stemmed from the most common words. I found it really interesting that Babson's second most common word was "mba" whereas Bentley's was "men's", but after doing further research it made more sense since it reflected the overall student body of each college. 

That being said, I found it difficult at the beginning to figure out how I should compare the two texts. After starting out by measuring the similarity between each text, I felt like my ideas were snowballing and I continued to create different ways to analyze the text. I'm the most proud of my wordFrequency() function since it combines iteration, dictionaries, and using mathplotlib all in one function. Since I struggled with dictionaries, I was proud of myself that I was able to create a function that iterates through a dictionary.

I felt my testing plan was strong - after I completed each function, I tested, and if a result appeared that I didn't expect, I would troubleshoot by myself for 10 minutes and if I was unable to figure it out I used ChatGPT. I felt that ChatGPT was a tool that I could use to get over "writer's block". When I got stuck, whether that be because I didn't know a function or I didn't know where the error in my code was, I was able to consult ChatGPT to be able to get beyond my block. I only used it as reference, never copying the entire program it generated - only select parts. I wish I knew how to prompt better because there was one instance where I didn't get my desired result and I had to ask it again. 