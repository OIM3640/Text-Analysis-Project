# Text-Analysis-Project

Please read the [instructions](instructions.md).


## 1. Project Overview (~1 paragraph): 
### What data source(s) did you use? What technique(s) did you use to process or analyze them? What did you hope to create or learn through this project?

- I was initially interested in pursuing the Grimm tales which I learned about in middle school which was the inspiration for a lot of the Tales movies and books that are out there but after looking more into the Gutenberg project I only found the original as well as very little other fairy tales. While researching I have found that Peter Pan and Alice in the Wonderland were both writings inside the project and I thought I'd be interesting to compare the two in terms of similarities as they both target kids with their writing. I found the similarity technique to be very intuitive as well as just looking at the word frequencies after removing the stop words because they both tended to use the word “said” a lot which indicated how both books are filled with conversations rather than events that might have happened.

## 2. Implementation (~1-2 paragraphs):
### Describe your implementation at a system architecture level. You should NOT walk through your code line by line, or explain every function (we can get that from your docstrings). Instead, talk about the major components, algorithms, data structures and how they fit together. You should also discuss at least one design decision where you had to choose between multiple alternatives, and explain why you made the choice. Use shared links and/or screenshots to describe how you used GenAI tools to help you or learn new things.

- I first created a function that read the text files and generated a dictionary representing the work frequencies for both texts. After that, I removed the stop words because the most common words in both texts were very similar as they were used in all sentences. After removing it I found that the main characters for both texts were the second most common word. Looking at the tools afterward that I could use, I focused on text similarity because it looked intuitive and was very simple to both implement and interpret. Lastly, I tried using the sentiment intensity analyzer which was a lot more complicated and I had to ask for a check-up to try to explain the values that I got and their importance. On top of this, I found the formatting for the commands themselves to be somewhat challenging because I was trying to tinker with the process file function to create an output that was not an error but I eventually used the sample code in the instructions which worked. Initially, I tried asking for ways to alter the files that were in the data folder to try to format it correctly for the NLTK to work but it only produced error messages. 

## 3.Results (~1-3 paragraphs + figures/examples):
### Present what you accomplished in your project:
#### If you did some text analysis, what interesting things did you find? Graphs or other visualizations may be very useful here for showing your results.
#### If you created a program that does something interesting (e.g. a Markov text synthesizer), be sure to provide a few interesting examples of the program's output.

![alt text](image.png)
- 

## 4. Reflection (~1-2 paragraphs)
### From a process point of view, what went well? What was the biggest challenge? How did you solve it? What could you improve? Was your project appropriately scoped? Did you have a good testing plan?
### From a learning perspective, what was your biggest takeaway from this project? How did GenAI tools help yo? How will you use what you learned going forward? What do you wish you knew beforehand that would have helped you succeed?

- 

