# Text-Analysis-Project

1. Project Overview (~1 paragraph)


The data source that I used is the book, The Metamorphosis, from the Gutenberg website. In addition to the full text of the book, it includes a header and footer outlining technical information about the licensing that Gutenberg needs. Because of the additional information that the text contains, I did not want to include it in the analysis of the text, thus the first step was to ensure that the text did not include either the header or footer. To analyze the text, I found frequencies (in amount and percentage of the text) to find what words are the most common within the text. This was reported in histogram form. Because stopwords like "the","a", etc. are the most likely to show up in these sort of analysis, I also created a function and loaded a library that would remove the stopwords from the text. For the frequency analysis, I output two versions - one with and one without the stopwords. 

At the beginning of the project, I was hoping to learn the basics and a little more about how text analysis works in python. In a previous class I took at Babson, we had learned text mining in R Studio and one of the tedious aspects of text analysis was listing out all of the words that I did not want to include in the final product. For example, we were looking at job descriptions and the objective was to find the skills prominent within them, but all of them included the equal employment opportunity statement. Amongst other words, we had to make sure that this did not show up in the word cloud and I feel as though this process was made simpler with the use of the natural language processing package.

2. Implementation (~1-2 paragraphs)

Describe your implementation at a system architecture level. You should NOT walk through your code line by line, or explain every function (we can get that from your docstrings). Instead, talk about the major components, algorithms, data structures and how they fit together. You should also discuss at least one design decision where you had to choose between multiple alternatives, and explain why you made the choice. Use shared links and/or screenshots to describe how you used GenAI tools to help you or learn new things.

All of the steps of the project and the various analysis steps were made into functions. This is with the exception of the code that brings in the text using the URL and unpacking it. It remains a variable outside of any functions and I do this to make it easier to call throughout the various functions that were used to clean the text. In doing this, it remained a global variable without having to explicitly label it as one within in a function which made is simpler to use the text whenever I needed to do so. 
To center all of the outputs, I created a "main" function that would call any or all of the functions that I wanted. This helped in using the the output of a previous function as the input of another function. For example, the output of the preproccessing steps were often used and in one function it was used to count how many words the text contained. Or in another case, one of the functions produced a histogram and the histogram was then sorted to find the top 10 most common words. Overall, the main function allowed me to elaborate on processes to further analyze the output of another.

3. Results (~1-3 paragraphs + figures/examples)

Present what you accomplished in your project:

If you did some text analysis, what interesting things did you find? Graphs or other visualizations may be very useful here for showing your results.
If you created a program that does something interesting (e.g. a Markov text synthesizer), be sure to provide a few interesting examples of the program's output.

![alt text](image.png)
The results of the project include common words that are included the most within the story and through the results, there is a subtle summary of what the story is about. For example, some of the top words include, "room", "father", "sister", "mother" and "door". Although it doesn't give quite the full picture, some of the prominent themes in the book are isolation and family. After turning into a huge insect, Gregor Samsa isolates himself in the room and the door being closed is a recurring symbol for him shutting himself out from his family. 
Another thing that I found interesting was the sentiment score of 0.03 using the TextBlob package. TextBlob provides a sentiment polarity score ranging from -1 (very negative) to 1 (very positive). The average sentiment for all of the sentences was 0.03, implying that the book is fairly natural and many people know the book, The Metamorphosis, as somewhat bleak and saddening because of the themes of alienation, transformation, and the fragility of relationships, so this came as a surprise to me to see that the package would analyze it as a 0.03 meaning that the words that the book contains are mostly positive. 


4. Reflection (~1-2 paragraphs)

From a process point of view, what went well? What was the biggest challenge? How did you solve it? What could you improve? Was your project appropriately scoped? Did you have a good testing plan?

From a learning perspective, what was your biggest takeaway from this project? How did GenAI tools help you? How will you use what you learned going forward? What do you wish you knew beforehand that would have helped you succeed?

One thing that went well was figuring out how to clean the text without relying on external libraries. It was a culminition of many of the python tools that we have learned for string modificaation, like .split, .lower, and