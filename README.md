# Text-Analysis-Project Write Up


## Project Overview

For this project I used Wikipedia and News API as data sources. 

For the Wikipadia data, I copared the mast frequent words in two country articles. I chose US and Canada but the user can input any countries they would like. First I removed stop words for each article, then I used a dictionary to record the frequency of each distinct word, and then I used a list to sort the words in descending order by frequency, and then used a loop to print the first k words. I chose 20 for my K Value. My hope was to find some common frequently used words in the two articles. I believe that the more common words there are in the Wikipedia articles for two countries, the more similar those countries operate.

For the News API data, I gathered the descriptions of the first 100 news articles from the past 2 days appearing on the US google search for SVB. The user can input the topic of their choosing. I chose to complete a sentiment analysis of the descriptions to determine how the media is communicating the banking crisis started by SVB. 



## Implementation 

When analyzing the Wikipedia articles, I first collected the content of the two articles, and removed all the stop words. I have to convert the text back into a string because removing the stop words turned the data into a list. I used a dictionary to record the frequency of each distinct word. Each word was a key and the value was the frequency. I used a dict.get function here. If word was already in my dictionary, it simply added 1 to the current value of that key. If the word was not yet in my dictionary, then the value of the new key was 1. Then I used a simple while loop to create a list with the most common words with their frequencies for each article. After that I used an in range function to add all the words found in both lists to a new list. I had to decide whether to use a while loop or an in range loop. Typically, I would use a while loop and have a variable that increases by 1 with every cycle. However, recently, you made a comment on an assignment of mine telling me that an in range loop would be more efficient, and I think that was the case here. I was able to calculate the rate of commonality between the frequent word lists for each article. However, the rate is very dependent on the k value.


When analyzing the news articles, I collected the descriptions for the 100 recent articles relating to SVB into a list. I then removed all the stop words, and combined the list into a string. I was then able to pass the string through the sentiment analysis NLTK and evaluate whether the sentiment was positive or negative. I oddly got neutral answer for the sentiment of the recent SVB news, so I decided to use ChatGPT to summarize all the descriptions. I thought that ChatGPT would be able to pick up on and highlight trends in the descriptions as a whole, rather than focus on each word independently. You can see my output from ChatGPT on [google docs] (https://docs.google.com/document/d/1NKFyGInZ3YY3053OW3aIVDLWDZ8VK9Wb76tVw0rh5Fc/edit?usp=sharing). 


## Results

The two Wikipedia articles for the largest North American countries had 60% similarity when I used 20 as my k value. I wanted to see whether the commonality would increase or decrease when I increased by k value. When I used a k value of 30, the commonality was about 53%, and when I used a k value of 60, the commonality decreased to 48%. It seems as though when the k value increases, the commonality decreases. In any case it seems as though the United States have many similar words in their respective Wikipedia articles. Some of these words are national, population, north, and federal. I decided to try my code with China and the United States, and the commonality value was much lower. With a k value of 20, the value was about 40%. 

The sentiment analysis of the full set of article descriptions with stop words removed had a neutral result.  {'neg': 0.13, 'neu': 0.74, 'pos': 0.13, 'compound': 0.2263}. This didn’t seem right to me. After recalculating using ChatGPT summarized data, I got a clearly negative result {'neg': 0.11, 'neu': 0.854, 'pos': 0.036, 'compound': -0.9648}. 

## Reflection

My coding process needs improvement. I'm not sure why, but whenever I have to learn a new concept by myself, it takes me hours to get it to work properly. I tend to use a lot of online resources, however they usually leave something out that is critical to know for my code to work properly. I am however, getting better at debugging and understanding what the errors in the terminal mean. I believe my project was appropriately scoped and I think I used the appropriate analysis methods for the data I chose. Once I figured out how to get the data, I didn’t have much trouble finishing the assignment. It took me a while because I had to keep going back to add things, but I was able to get the code to do what I wanted. I didn’t use ChatGPT at all until this project and I am still trying to figure out how I can use it with my other classes. Personally, I haven’t found ChatGPT to be more helpful when writing code compared to the internet. It will show me how to do something but it doesn’t help me understand it. The online forums are better at helping me understand things. I definitely like the summarization tool. I also tried to ask it to put something in its own words to avoid plagiarism on another project and that worked really well. Before starting this assignment I wish I understood more about how to download modules using the command center. I had a hard time getting media wiki to work and I kept thinking it was a problem with the download. I honestly don’t know how it ended up working.