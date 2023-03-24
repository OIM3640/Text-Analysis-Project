# Text-Analysis-Project
 
Please read the [instructions](instructions.md).

##1. Project Overview 

What data source(s) did you use? What technique(s) did you use to process or analyze them? What did you hope to create or learn through this project?

I tested out multiple data sources but ended up going with the IMDB one. Being a movie fanatic, I thoroughly enjoyed going through the different types of data and seeing what I could analyze. I extracted both characters and integers from my data set. I analyzed "positive" and "negative" words found in reviews (chracterizing by word frequencies) and found an average of groups of numerical ratings. I also learned how to plot my findings using matplotlib.

##2. Implementation 

When creating my word frequency code, I decided to make a list of my own self created word and then reference this list as I looked at each review. My count_words_frequency takes a string as an input and counts the frequency of positive and negative words in it. It does this by splitting the string into words and thus using a list to count the number of positive and negative words that are there. My analyze revies counts the frequency and sums up all the counts. I am actually taking a Quantitative Methods of Machine Learning Course and can see many design decisions being pivoted to use deep learning models for sentiment analysis that can learn to extract features from the text automatically, without the need for any of my hand crafted lists. I made the choice I did because I was unsure of how to code it in Python and apply it to run in Visual Code, but given more research I definitely see myself using the feature in the future. 

I utilized a mix of ChatGPT and a youtube video to learn how to use matplotlib. I will like the video I watched below; I found it extremely helpful and easy to follow. I used a bar chart but there are so many different ones you could have done based on what type of data you are analzying and how you want to showcase. 

https://www.youtube.com/watch?v=QYLCXLQo1Sc

##3. Results 

When finding the positive and negative words, I was suprised as I had given such a small list and it still output a lot of data from the movie Frozen. The code performs a sentiment analysis on a set of movie reviews by counting a handmade list of positive and negative words. The results are then summed up across all reviews. I then created a graph that would visualize the positive and negative words after looking at x number of reviews. 

When running the graph function (as can be seen when running visual_table.py). The functions starts by defining two lists, 'labels' and 'data' and uses the bar method to create a bar chart. This is important because visualizing the results of sentiment analysis can make it easier to understand and interpret data. A bar plot is especially effective when looking at frequency. It can also help you identify trends and patterns in the data. It was interesting that despite the high numerical reviews, there were many negative sentiments.


##4. Reflection 

This is the first solo code I have written from scratch for a project by myself so it was really exciting to just see it all come together. Being able to correctly utilize the library and use matplotlib was also a huge step as I had never touched that before. As I mentioned, the code uses a pre-defined list of positive and negative words to perform sentiment analysis. This isn't as accurate or comprehensive enough for all types of reviews so a more robust approach in the future would be to use machine learning algorithms. Starting out, I didn't really have a plan but as I experimented with the API the more creative I got with how I tested what I was doing.

I learned how to solve problems by myself and take a step back when getting stuck. I also utilized chatGPT to help me with debugging and more of the KeyErrors when initially using the API. Going forward, I can use matplotlib for so many other things and now I know how to access a database and analyze data from it. I wish I knew beforehand some of the different analysis and how to use them; just a little example in class would have been extremely useful. 



