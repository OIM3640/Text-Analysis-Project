## 1. Project Overview (~1 paragraph)

I used movie reviews from IMDB movie reviews, and I used the NLTK library to perform natural language processing on said data. I pursued this path because I knew that I wanted to use the NLTK library in order to gather analytics regarding subjecting metrics. In my case, I focused on sentiment, or the measure of how positive, neutral, or negative a piece of text was. My main goal was figuring out how different the general population viewed a movie, versus how I did, without looking just at the star reviews. Sometimes, the star reviews aren't detailed enough, and reviews that point out the flaws of a movie still receive a 5 star. I wanted to figure out, what movies would rank on a 5 star scale, based solely on what people had to say about the movie in reviews. I used the VADER module offered on NLTK, then averaged the resulting sentiment for each movie, to find an average sentiment score for each review. I then scaled the -1 to 1 sentiment score to a 0-5 scale to assign it a number of stars. 

## 2. Implementation (~1-2 paragraphs)

First and foremost, I import data from the IMDB API, which allows me to go through every review for a given movie. I also import NLTK, a natural language processing toolkit, which allows me to perform different natural language processes for a given piece of text. The module that I focused on using in this application was the VADER module, which is an amazing module that provides sentiment analysis for texts. For my sentiment analysis, a negative number correlates to a negative review, a 0 is neutral, and a positive number correlates to a positive review. My script allows for users to enter a movie name, and uses a distance formula that detects movie titles most similar to the one that the user enters (for people that don't know the exactly accurate name of the movie), and returns their sentiment analysis for each review given on IMDB. Then, I implemented an averaging component, which takes the average of every single review in order to get an average sentiment per review. Then, I scaled the sentient score (given -1 to 1), to a 0-5 star scale. 


This all comes together in this manner:
a. Import NLTK library
b. Import IMDB movie review data
c. Ask for user input for a movie title
d. Find the movie title that is the most similar to the entered text
e. Pull data about the reviews of said movie from IMDB
f. Using VADER, give a sentiment rating for each review on the site
g. Average all the sentiment scores together
h. Convert to number of stars. 
i. Print results


One design decision that I made was choosing to use IMDB movie reviews, rather than Tweets under a certain hashtag. I had originally wanted to use the Twitter API, but I didn't have the access that I needed. So, I pivoted to another text source with opinionated messages. Another design choice that I made was choosing to allow users to input movies they liked, instead of needing the user to include a str argument in the function call. I figured this would make the script feel more like a user-facing application. 

I used Chat GPT to help me create a function that helps the app find movies that are most similar to the inputted movie title. I decided to do this because when I was testing out the code and playing around with the script, I found that sometimes I would misspell a word or forget the exact movie title, and the app would return "no reviews found for __". I also implemented a component of the app that prints "no movie ___ found". I've put screenshots of Chat GPT's solution in the folder similar_title under images. 

## 3. Results (~2-3 paragraphs + figures/examples)

After my implementation of my script, I uncovered a very interesting finding. 

The main conclusion I found was that the reviews given on a movie do not necessarily correlate with how well-recieved the movie is. For example, I conducted a sentiment analysis of the top 10 movies of all time, according to IMDB's site. The screenshot of the output is in "findings", under the images folder. One of the biggest things that I found out after performing a sentiment review, is that people often have much more negative things to say about a movie than its IMDB ranking denotes. For example, Pulp Fiction is one of my favorite movies of all time, and ranked a top 10 movie all time by IMDB. However, it was only given a sentiment rating of 0.60. This means that the reviews written about Pulp Fiction are far more critial than expected. This could lead to a deduction that Pulp Fiction was controversial, and there were moments in the movie that people didn't like, but people still enjoyed the movie overall. This offers a pretty stark contrast compared to Shawshank Redemption, which received a sentiment rating of 0.93. This shows that the average review on Shawshank Redemption was very positive, and people struggled to find flaws in the movie. 

These two points are very interesting, because they show that controversy can sometimes lead to a better received movie, whereas "perfection" sometimes is punished. For example, I think that Pulp Fiction is definitely a bit flawed. However, it sits higher on movie ranking lists than movies that had higher sentiment reviews. This goes to show that the reviews that a movie receives sometimes doesn't represent how good of a movie it really is. This also serves as interesting evidence that sometimes movies benefit from being controversial, and also from evoking negative emotion. 

## 4. Reflection (~1-2 paragraphs)

From a process point of view, I think that the overall project went very well. I learned that with a proper plan in place and knowing the outcome that I wanted, there are ample tools online that can help me fulfill my goal. I was able to learn about the necessary steps that go into creating an app with API calling, as well as how to interact with ChatGPT to provide optimal assistance with the NLTK. A hurdle that I faced when doing this project was actually a minor mistake that became a big bottleneck. I had accidently been using the wrong Python interpreter, which was stopping me from importing the necessary libraries and functions. I could improve on this by paying better attention in class when the professor goes over such things. I believe that my project was overscoped. I had planned on using the Twitter API, and sorting through posts with the # Steph Curry, to find out what people thought about my favorite basketball player and how that had changed over the years. I was in over my head, however, because what I didn't know was that the Twitter API now costs $100/month, which is a lot more than I was willing to pay. I wasted a lot of time doing research on how to execute this without knowing that I wasn't going to even get access. 

As for my testing plan, I ran the script over and over, making sure it outputted exactly what I wanted it to. I also roped in my friend George to help me test the script and play around with it. We also tested the movie title recognition function multiple times in order to find the very best similarity cutoff for the movie title recognition function, and ended up sticking with 0.6, the originally suggested cutoff. 

Chat GPT was a huge help for this project, and helped me create code for functions that I would otherwise have no clue how to write. Going forward, I now know that I can use ChatGPT, along with my own knowledge of API calling, to analyze a large variety of text that I find online. I also learned how to use NLTK, as well as some very common modules that they offer. I feel like this project was a huge value add for me, because scraping data that I find on the internet, and performing fun analytics on it was the main reason I took this class. Now, with knowledge of cool natural language processing libraries, along with practice calling and using API's, I can do these things on my own. 

