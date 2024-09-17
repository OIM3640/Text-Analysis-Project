# Text-Analysis-Project
 
Please read the [instructions](instructions.md).

**1. Project Overview** (~1 paragraph)

What data source(s) did you use? What technique(s) did you use to process or analyze them? What did you hope to create or learn through this project?

The text analysis project uses data from Wikipedia, which was extracted using the mediawiki library, a python wrapper and parser for the MediaWiki API. A function was created to process the data in which it first splits the content into lines then into words that are appended to a histogram. During this process, stopwords were also removed. The histogram is a dictionary. To analyze them, I created functions to get basic summary statistics such as total number of words, the total unique number of words, and the frequencies of each word. Sentimental analysis was also conducted on random sentences pulled from the content of the Wikipedia page and text comparision was also conducted on random sentences pulled from the content. Through this project, I hope to better understand the concept of natural language processing so that in the future I could use it well.

**2. Implementation** (~1-2 paragraphs)

Describe your implementation at a system architecture level. You should NOT walk through your code line by line, or explain every function (we can get that from your docstrings). Instead, talk about the major components, algorithms, data structures and how they fit together. You should also discuss at least one design decision where you had to choose between multiple alternatives, and explain why you made the choice. Use shared links and/or screenshots to describe how you used ChatGPT to help you or learn new things.

The data structure used for basic summary statistic of the content is a dictionary. A dictionary was created to store each unique words with their corresponding frequencies. This allows for the ease of computing total number of words, which is the sum of the keys in the dictionary, and computing the total number of words, which is the sum of the values in the dictionary. The second data structure used for sentiment analysis and text comparision is each sentence is a string stored in a list. This allows me to pull easily pick a random sentence by picking a random element in the string.

When creating the sentiment analysis function and the text similarity function, I originally had each function include a part where it would first create the list of sentences and pick a random sentence first. But, I realized that I could just create a separate function for to create the list of sentences and pick a random sentence so that the random sentence can be consistent for both the sentiment and text similarity function. This means that sentiment and similarity analysis is conducted on the same sentence rather than a different sentence for both functions.

![alt text](image.png)

This image is a screenshot of ChatGPT helping me with how to call the function so that it displays the same sentence the sentiment analysis was conducted on. It also was an inspiration to my decision to develop a separate function to create a list of sentences.

![alt text](image-1.png)

I also used ChatGPT to explain lines of code for me. I originally asked ChatGPT to help me with extracting sentences from a paragraph, in which it recommended me to use "sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', paragraph)". I later Googled if the nltk package has the ability to do that and found the current line of code I am using. Because I didn't completely understand the syntax of the line of code, I had ChatGPT explain it to me and break it down for me so I can better understand the use of the line of code as well as nltk.

**3. Results** (~1-3 paragraphs + figures/examples)

Present what you accomplished in your project:

If you did some text analysis, what interesting things did you find? Graphs or other visualizations may be very useful here for showing your results.
If you created a program that does something interesting (e.g. a Markov text synthesizer), be sure to provide a few interesting examples of the program's output.

I focused on conducting sentiment analysis because I was interested in if a Wikipedia page could have potential perspective biases for singers. Based on conducting sentiment analysis on many random sentences pulled from the Wikipedia page, I believe it is fair to say that articles on Wikipedia are fair. This is because neutral sentiments was always the highest, averaging around 0.8 and positive sentiment avergaging around 0.15. Because the article page would also talk about the achievement of the singer, it made sense that there is some positive sentiment in the article. However, because the overall article is objectively talking about the singer, such as their background, their genre of music, and their past music releases and shows, neutral sentiment makes sense. I did find a few exceptions for negative sentiments, and reading the sentence, the analysis was reasonable because it was talking about the main topics of her music, in which some were about sadness and heartbreaks.

Example Outputs:
This is the random sentence: performing "Slower", and received two Juno Award nominations.On April 16, 2021, McRae released the track "You" alongside Regard and Troye Sivan.

This is the sentiment score of the sentence: {'neg': 0.0, 'neu': 0.851, 'pos': 0.149, 'compound': 0.5423}

This is the random sentence: and Ariana Grande’s influences on the project, stating that in terms of the latter, Think Later "represented a career-defining shift for McRae as she pulled herself from the rubble of grief, heartbreak, and internal turmoil.

This is the sentiment score of the sentence: {'neg': 0.233, 'neu': 0.767, 'pos': 0.0, 'compound': -0.8555}

This is the random sentence: In May 2021, McRae was nominated for the Social Star Award at the IHeartRadio Music Awards, and performed "You" with Regard and Troye Sivan on The Tonight Show Starring Jimmy Fallon.

This is the sentiment score of the sentence: {'neg': 0.0, 'neu': 0.817, 'pos': 0.183, 'compound': 0.7579}

**4. Reflection** (~1-2 paragraphs)

From a process point of view, what went well? What could you improve? Was your project appropriately scoped? Did you have a good testing plan?

From a learning perspective, mention what you learned through this project, how ChatGPT helped you, and how you'll use what you learned going forward. What do you wish you knew beforehand that would have helped you succeed?

From a process point of view, I believe that the basic summary statistics went really well. Especially after taking a look at my data set, in which is was paragraphs of words. I could improve by conducting more analysis such as the overall content sentiment as well as comparing Wikipedia text to text from another source to illustrate in numbers how each source differ in the way their writing style. There was also a challenge that I found, which is there is empty space key in my histogram that I could not remove. I would need more time to look into it to understand why it is in my histogram. I have asked ChatGPT for help, and have tried many different codes, and for some reason it is still not removed. I think it could be because of the original data structrue, and I did not understand it well enough. I believed that my project was appropriately scoped because I covered all the basic summary statistics and analyzed the sentiment of the article, which is what people do to better understand if a string of text is positive, negative, or neutral. It actually reminds of an internship I had in which I assisted with sentiment analysis by using a platform the company has created. My testing plan was to cover the basic summary statistics first and then figure out what I want to do from there. 

From a learning perspective, I learned to better understand different data structures. I had dictionary and also a list of strings that I derived from paragraphs of text. I also learned about new packages such as ntlk, which I find super helpful in natural language processing. Additionally, ChatGPT was extremely helpful in explaining new lines of code to me. ChatGPT is like my 24/7 personal tutor that I can go to for help. It does very well at breaking down the code part by part to better help me understand each line of code. I think having more examples of text analysis would help because I am a visual learner, so have a demonstration is always super helpful to my learning and understanding. I tend to find myself learning quicker and better when a demonstration is given and I follow along.
