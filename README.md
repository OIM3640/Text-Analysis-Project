# Text-Analysis-Project
 
Please read the [instructions](instructions.md).

1.
    I used the IMDB website for this project. My goal was to explore the career of Matt Damon, and see if there were any common threads between his highest rated books. I wanted to take this from the perspective of a producer, who already has Matt Damon signed, and wants to create the best film possible. I used natural language processing to create a positivity score for the reviews of all his movies. I hoped to use this to find commonalities between the movies that were rated higher.
2.
    The first step in this project was to find what Matt Damon's ID number is. This could then be used throughout the rest of the code. From there, I was able to create a dictionary of all the films he took part in. I only needed the ID numbers at this point. I then used these ID numbers to match with the reviews for each film. This was the start of the more challenging part of this project. I realized that the easiest way to continue this project was to combine the reviews for each movie into one mega-review. I used natural language processing to get the polarity scores for each movie. I had to make sure to include code to get rid of 0 scores as that meant there were no reviews. Lastly, I made a dictionary out of the movie ids and positivity scores (I felt the positivity score was the best measure to pick as it had the most variation) to transfer over to a histogram.

    I used ChatGPT mainly for a few things. I was struggling with dealing with the fact that there were often many reviews for each movie, with each one having a different number. ChatGPT helped me combine all the reviews for each movie into one. This way each movie would only represent one data plot. Seperately, I used it to help me ignore the movies with no reviews and how to focus on only the positivity scores. Lastly, I used it to debug and pull everything all together to create the histogram.
    https://chat.openai.com/share/a3e5a1d5-ae7a-453b-9bb2-c499144bdc0c
    https://chat.openai.com/share/45da1479-05c8-4cfa-80d2-20dfdad6f795
3.
    The main results I were able to extract were the polarity scores for the reviews and the histogram.
    [def]: image.png 
    What I saw is that overall, Matt Damon's reviews are very good. This was to be expected with an actor of his caliber and fame. Even the movies that are not rated as well, still had fairly positive polarity scores. The histogram shows that the distribution is fairly uniform, following almost a bell curve with a single peak in the middle. This peak occured at about 0.18. This means that, on average, 18% of words in the reviews were seen as positive. Although this may not seem super high, it is as most words will be seen as neutral.

    The great thing about this program is that it would be very easy to adjust. I can plug in any actor's ID and get their movie's polarity scores. I can also very easily change which statistic to look for (negative). In this case, I would be interested in digging into the extremes on the chart more. What made one film had a positivity score of 0.3? Can learn from this film and apply it to a new one?
4.
    To start, my project was not appropriately scoped. My initial idea would have been way too intensive. And I do think my final project may have been on the simplier side, as I feel I didn't have much to write in the results section. I think all in all with this, I struggled to solve problems. I often hit roadblocks that I felt I couldn't get through. I am happy that I think I did something unique and something that I could build upon. I would really enjoy to finish my initial plan of connecting the dots between films to find commonalities among the good and bad movies. 

    I learned the most from the back half of the project. Once I got past the initial issues (with your guidance), I was able to have more fun with getting to the analysis tools. This is where I relied on ChatGPT more, and the example code from you and the repository less. I really tried to take the time during this project to work on asking the ai better questions and found this a lot more efficient to getting accurate responses. That, I believe, will be my biggest takeaway from the project. I wish going into this that I understoon a better way to describe my problems.
