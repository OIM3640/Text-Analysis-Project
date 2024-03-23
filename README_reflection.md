**1. Project Overview** (~1 paragraph)

    I used the reviews for the move "Dead Poets Society" from IMDB's database. I first summarized the statistics and found out that exclusing the stopwords, the top ten dictions appeared in the reviews are  "film" (74), "one" (64), "movie" (63), "school"(42), "keating"(42), "williams"(41), "teacher(34), "life" (33), "society"(32), "dead"(29). Most of the top appearing words are associated with the genre or the theme of the movie. Next, I conducted a sentimental analysis to conclude the two paragraphs with the most negative and positive sentiments. I also used text similarity and clustering analysis to compare each paragraphs of review with the first paragraph as reference. Thourgh this project, I learned about how sentiments and similarities could be quantified as ratios and further help us as users of the program to make implications more efficiently. 


**2. Implementation** (~1-2 paragraphs)

Describe your implementation at a system architecture level. You should NOT walk through your code line by line, or explain every function (we can get that from your docstrings). Instead, talk about the major components, algorithms, data structures and how they fit together. You should also discuss at least one design decision where you had to choose between multiple alternatives, and explain why you made the choice. Use shared links and/or screenshots to describe how you used ChatGPT to help you or learn new things.



**3. Results** (~1-3 paragraphs + figures/examples)

Present what you accomplished in your project:

- If you did some text analysis, what interesting things did you find? Graphs or other visualizations may be very useful here for showing your results.
- If you created a program that does something interesting (e.g. a Markov text synthesizer), be sure to provide a few interesting examples of the program's output.

    While conducting the sentimental analysis, the result shows the most positive line had a score of 0.295, and negative line a score of 0.155. A lot could be implied from this result. First, the maximum negative score is lower than the positive score. This indicates that the movie, although sad, presents a healing/positive atmosphere to the audience that teaches them something about life. Second, the dictions in the most positive line are "good", "love", "enjoy", etc. that bring positve energy to the readers. However, the negative paragraph uses words like "hopeless", "die", and etc. that contribute to the relatively high negative score. 

Sentimental analysis results:
## The most positive line: There's so much good about this movie. The first time I saw it I watched it solely for plot and I loved it. Now I've seen it again and watched Peter Weir's filming and timing which is also great. Robin Williams is a terrific actor when he's serious. He proved it in Good Will Hunting but he proved it first here. If you liked that movie and your liking it had something to do with Williams than you will like this one. The plot is about a number of students who are taught by Williams about life. They are taught how to enjoy themselves. This ends up causing great controversy among the heads of the school. The students are terrific and even the dialogue is great. This is a movie that I can't imagine anyone not liking. It is good in every way.


## The most negative line: At the end of the movie, Neil's dream of pursuing drama is hopeless and his life is hopeless. In the white night, Neil chose to die brilliantly.Neil's parents went to the school to press charges. The university blamed Keating entirely and put pressure on students to sign documents proving that Keating had "misled students" and "abused teacher influence" . Eventually, Keating got kicked out of the school.Before he left, Keating went back to the classroom to get something. He was replaced by President Nolan, who had expelled him.At the last moment before Keating leaves the classroom, Todd, who has always been shy and timid, stands up from his seat, blushes, jumps onto the desk and intones:O Captain! My Captain! Oh, captain! My captain!President Nolan angrily warned "Sit down!"Overstreet also stood at the desk.O Captain! My Captain!Pitts stood at the desk. Meeks stands at the desk. One by one, one by one.Let the headmaster shout "How dare you! "Out of this school! "Sit Down!"One by one, one by one.Standing one by one, it is clear that a bottle of torch, flourish.Keating tears, these once hesitated confused face, now are showing perseverance, courage, fearlessness. Burst out the light of life.Keating whispered "thank you."May you shine forever. Do not extinguish, do not dim, always holding the torch, efforts to shine, efforts to do the rain in the sun.  

    Another analysis that I found interesting was the text similarity and clustering program. 
    

**4. Reflection** (~1-2 paragraphs)

From a process point of view, what went well? What could you improve? Was your project appropriately scoped? Did you have a good testing plan?

From a learning perspective, mention what you learned through this project, how ChatGPT helped you, and how you'll use what you learned going forward. What do you wish you knew beforehand that would have helped you succeed?

