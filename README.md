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

        Output:
        Top 10 words in Alice: [('the', 1629), ('and', 818), ('to', 719), ('a', 626), ('she', 536), ('of', 500), ('said', 461), ('it', 452), ('alice', 384), ('in', 358)]
        Top 10 words in Peter: [('the', 2313), ('and', 1365), ('to', 1180), ('he', 1033), ('was', 922), ('a', 921), ('of', 846), ('it', 718), ('in', 672), ('that', 584)]
        Top 20 words (without stopwords) in Alice: [('said', 461), ('alice', 384), ('little', 127), ('“i', 124), ('one', 92), ('went', 83), ('like', 78), ('thought', 74), ('know', 66), ('queen', 65), ('time', 63), ('see', 63), ('', 61), ('king', 60), ('began', 58), ('mock', 57), ('“and', 56), ('way', 56), ('quite', 55), ('turtle', 55)]
        Top 20 words (without stopwords) in Peter: [('said', 358), ('peter', 321), ('wendy', 283), ('one', 205), ('“i', 161), ('now', 141), ('cried', 136), ('hook', 136), ('time', 115), ('darling', 108), ('john', 107), ('little', 100), ('see', 98), ('like', 92), ('michael', 91), ('boys', 89), ('children', 87), ('will', 83), ('night', 82), ('know', 80)]
        NLTK Alice: {'neg': 0.083, 'neu': 0.823, 'pos': 0.094, 'compound': 0.9999}
        NLTK Peter: {'neg': 0.094, 'neu': 0.788, 'pos': 0.117, 'compound': 1.0}
        Text Similarity between Alice and Peter (Out of 100): 45

- Based on the information, I found that it was very interesting to me that, when comparing the NLTKs,  Peter Pan was slightly more positive but also more negative but for the most part both books shared the similarity of having the majority of their language being very neutral. One thing when researching NLTKs was the compound value which it could be from -1 to 1 depending on its sentiment positivity Peter scored a perfect 1 for some reason while Alice and Wonderland scored just slightly lower at .9999. In the future I would probably look at more books to see how the compound value was generated and whether this was just a fluke or if is it affected by its negative neutral and positive values. One really surprising thing that I found was that the text similarity between Alice and Peter was only 45 out of 100 and because they were both children's books I expected them to be a lot higher in value. From analyzing the books I found that it was very interesting that, when looking at the frequencies, the names Peter and Wendy were the most frequent and the other boys in the crew appeared less in general.

## 4. Reflection (~1-2 paragraphs)
### From a process point of view, what went well? What was the biggest challenge? How did you solve it? What could you improve? Was your project appropriately scoped? Did you have a good testing plan?
### From a learning perspective, what was your biggest takeaway from this project? How did GenAI tools help yo? How will you use what you learned going forward? What do you wish you knew beforehand that would have helped you succeed?

- In this assignment, I found that the biggest challenge was looking at the new functions as well as importing and learning about what they could do as well as their limitations. I also learned a lot about formatting and through a lot of trial and error I gained a better understanding of some of the functions used and the outputs such as the process file function where the text (fp) at the end is not returned as listing of words but instead as a “<_io.TextIOWrapper” type which I thought was interesting. One main issue that I found when writing my code was how my terminal when running new code tended to just output as if I did not revise the code but it fixes itself once I close the application and reopen it. Overall I thought that this was a very useful tool and I found that for the most part once I understood the functions they were relatively intuitive in terms of use. Furthermore, after doing an analysis comparing these two texts, I would want to compare Peter Pan, the original story, with Peter and Starcatchers, a book series that I read in middle school or high school which was heavily inspired by Peter Pan but took place in a more modern society and I would like to both compare the words used as well as compare the similarities of the text with other books in the series as well. Finally, I think that the use of Chatgpt helped me understand the code that I was initially looking at since it was able to provide very simple code along with an explanation so that I could have a more holistic understanding of functions like the Sentiment Intensity Analyzer.

        What the varaible, fp, is after the process file function:
        <_io.TextIOWrapper name='data/Alice.txt' mode='r' encoding='utf-8'>
        <_io.TextIOWrapper name='data/Peter.txt' mode='r' encoding='utf-8'>

