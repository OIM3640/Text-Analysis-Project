# Text-Analysis-Project
Please read the [instructions](instructions.md).


#Part 4: Project Write-Up and Reflection
## 1. For this project I actually used several data sources and then finally chose the wikipedia one. I originally wanted to use the IMDB one to compare reviews, but couldn't find any reviews for the movies I was searching up. I then tried to do NEWSAPI, but I learned that you cannot access full text articles with the free version. Ultimately this led me to choose Wikipedia because I had access to a lot of content and was able to use their summary function to condense it. This helped me learn how to use 3 different APIs and access their specific commands. I thought that was fun and interesting because they were all so different, but once I understood them I realized how intuitive they were. Ultimately, I just wanted to learn more about APIs in this assignment and I feel like I did. I did not fully understand APIs before, but now I feel less afraid of an API.

## 2. In terms of implementation I started off by skimming through the whole assignment. Once I got a bit of an understanding to what I had to do, I started by going through each question individually, keeping in mind of the analysis to do. That is why I struggled a little at first because I did not know how to access reviews or the full text of NEWSAPI, so I pivoted and chose a different API. After that I decided I wanted to do an analysis on music artists because I love music, so I chose 3 different artists. I came into some issues because the pages of some of the artists were long, so the full text did not fit into a dictionary, so I decided to use their built in function of summaries for each artist. 

## After doing so the rest was easier because it was similar to the text analysis we did in class. However, I did come into some printing issues and this is when I would ask ChatGPT for help. I was unsure how to make my results print nicely and GPT showed me how to use json for that, which was very helpful. Aside from that issue I started off by creating a global variable for the artist and then I created every other function that had to do with the question from the assignment. They fit together because some functions help others do another step that breaks down to the essence of the question. 

## 3. I decided to do a text similarity using the Fuzz library. I wanted to do this to see how similar  or different the artists would be based on their summaries. I found that the Fuzz did pretty well at detecting the scores. For example, Jhene Aiko and Tyler the Creator were the most similar at 54. Although it is not very high it is much higher than the comparison to Nessa Barrrett which was lower for both of the artists. I thought that the Fuzz score met up to my thoughts on each artist. I would definitley rate Tyler the Creator and Jhene Aiko much similar compared to Nessa Barrett. I would not rate Jhene and Tyler higher than a 60 though because they make music differently. 

## 4. Overall, I think getting started was the most challenging part for me because I was struggling to find text. However, with trail and error I got over that obstacle and I was able to break down the next questions into digestable steps and move on. I think I could improve on researching the API beforehand and see what is available on their free versions so that I did not have to waste time figuring it out on my own. I think my porject was appropriatley scoped, however I think I should have started working on this earlier because I had a lot of other assignments at the same time which cut into my coding time. I believe I did have a good testing plan because after I created a function I would run and test it to see if my desired results printed

## From a learning presepective I think I learned a lot. I was not confident before with APIs and nested dictionaries, but with this assignment I feel more powerful. I do believe ,though, that I need more practice because I kept finding myself having to ask GPT to remind me how to do certain things because I feel like I haven't practiced it enough to understand. This was the biggest area where GenAI helped me because it helped me remember things that I forget as well as teaching me new skills like how to print a sorted dictionary from greatest to least. The code seems complicated, but it is very intuitive. Going forward I will use json more because I think it has a lot to offer, especially with printing. I will also use GenAi to help me break complex matters into simple tasks. Beforehand, I wish I had known that some of the APIs required a paid subscription for access to full texts, like the one for NEWSAPI. 