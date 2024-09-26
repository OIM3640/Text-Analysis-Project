# Text-Analysis-Project
# **Text-Analysis-Project**

Please read the [instructions](instructions.md).
## Comparing IMDB Rankings for each Harry Potter Movie to Natural Language Processing's Rankings of each Harry Potter Movie based on Review Sentiments


### **Project Overview**
I utilized IMDB's API (aka Cinemagoer) to access movie review and rating information. I used NLTK (Natural Language Tool Kit) to use Natural Language Processing (NLP) to analyze the IMDB movie data. I compared IMDB ratings with their reviews to test how accurate/consistent their ratings are with their reviews. I chose the Harry Potter series as my test subject as it is my favorite movie series of all time. I am happy with my results as I automated the creation of a model displaying each Harry Potter movie ranked from 1-8 based on their original ratings, positive review percent, and negative review percent.

### **Implementation**
I first researched the basics of the "Cinemagoer" library and API to import the Harry Potter Movie Rating and Review data. I then used NLTK's SentimentIntensityAnalyzer to gather the Polarity scores (or sentiments: positive, neutral, and negative) from each movie's IMDB reviews. I finally ranked each movie's original ratings, positive sentiment score, and negative sentiment score in descending order to analyze how accurate/consistent IMDB's flagship rankings are with their own reviews. I used the sorted() function with Lamda as the key parameter to carry this out. Finally, I printed each row of rankings (from 1-8) for each of the original ratings, positive review percent, and negative review percent so users can view the differences between them.

ChatGPT helped me out on a few occasions throughout this project.
It helped me effectively sort my lists of nested data types:
![image](https://github.com/OIM3640/Text-Analysis-Project/assets/143458194/492c2b0f-a07b-49dc-8c5d-be6e43691e3c)
It helped me learn how to use the "Cinemagoer" API:
![image](https://github.com/OIM3640/Text-Analysis-Project/assets/143458194/109ca773-60fa-4f82-a91b-5f22cfd1b3e5)
And finally, it helped me recall the past lessons I learned about dictionaries:
![image](https://github.com/OIM3640/Text-Analysis-Project/assets/143458194/7908e821-dc69-4378-89e3-aa971522ad85)

### **Results**

I successfully compared each Harry Potter movie's original ratings, positive sentiment score, and negative sentiment score and analyzed how accurate/consistent IMDB's flagship rankings are with their own reviews. My findings indicate the IMDB standard ratings aligned well with the sentiment rankings from the reviews. I generated sentiment reports that analyzed each word in the reviews of each movie and returned a corresponding score, then ranked each movie based on those scores. It is interesting to look at these scores as someone who has seen each movie many times and have my own set of ratings.

I worked heavily with lists, tuples, and dictionaries throughout this project. I learned a lot about how and when to use each data type. I also learned about the intricacies of working with APIs (specifically Cinemagoer) and the NLTK library. Please take a look at the results chart showing the rankings below.
**CLICK HERE FOR RESULTS IMAGE >>>**([https://github.com/OIM3640/Text-Analysis-Project/assets/143458194/040dfcf8-f7a3-426c-8ef6-28e4f822f6a6](https://github.com/OIM3640/Text-Analysis-Project/assets/143458194/040dfcf8-f7a3-426c-8ef6-28e4f822f6a6)

### **Reflection**
This was the most challenging project I have ever worked on at Babson. My knowledge of dictionaries and APIs was very limited going into this, which is what my entire program was centered around. I did this to force myself to improve with these Python topics, which is exactly what I achieved. ChatGPT helped me when I encountered small roadblocks, especially regarding the library and API-specific functions and capabilities I needed to learn. But it also explained to me line by line what my code did to ensure that even when this worked as planned, I understood precisely **why** they worked that way.

I did achieve what I set out to achieve, but my code is far from perfect, and I plan to revisit it to make improvements. It takes 24 seconds to execute fully, which is partially out of my control as it is pulling a lot of information from the API and also depends on my hardware. Still, it could be improved by limiting the number of times I recall movie data into separate variables for different purposes. Additionally, I manually repeated each step 8 times for each movie when I knew this could be automated to a degree. Lastly, I would love to generate additional visual reports/comparisons of the differences between the rankings and dive deeper into the NLTK library.

Overall, I am happy with the result and look forward to hearing your feedback.
