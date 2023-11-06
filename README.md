# Text-Analysis-Project
 
**1. Project Overview** (~1 paragraph)
I used two articles from Wikipedia, an article from insidehighered, and one last article from Fortune. The reason why I chose separate sources to pull information from was to diversify the data and make sure it was not all biased from one source type. These sources were all related to news about grad school in terms of which business schools are best to attend and analysis on the pros and cons of grad school. From this project, I was hoping to do a sentiment analysis and see which grad schools seem to be the ones that every source is ranking as top tier, what is being said about them, and if any of the sources were gravitating any schools in particular. 

**2. Implementation** (~1-2 paragraphs)
The way that I approached this assignment was to first parse text from the four websites that I wanted to analyze. Then, after parsing the texts into the terminal, I copied and pasted it into four separate text files to hard code the texts. The reason why I chose to hard code it was to prevent issues with internet connection and the websites putting up paywalls later on that would prevent me from being able to pull the texts. After successfully gathering the information that I needed to conduct text analysis, I started my text analysis by first performing a word frequency analysis on the text files. It includes functions for processing text files, generating word frequency histograms, finding the most common words, and comparing word frequencies. The major components that I used here are process_text_file function (takes filename as input, reads the contents, tokenizes it into words, and generates a word frequency histogram), most_common function (takes word frequency hstogram and a flag to exclude common stopwords and then sorts the word-frequency pairs in descending order of frequency to return a list of pairs), print_most_common function (calls on most_common function to get sorted listed of word-frequency pairs), and the compare_word_frequencies function (calculates the frequency differences between common words in both histograms). 

A design decision that I made was to exclude common English stopwords in my most_common function because I felt that these stopwords would not provide meaningful insights and would rather clutter my text analysis. 

After performing a word frequency analysis, I decided to do a sentiment analysis on the four texts to make a more in-depth analyzation of the sources. I used the VADER sentiment analysis tool to process the list of text files and determine the sentiment (positive, negative, or neutral) of each text. The analyze_sentiment function takes a list of text strings as input and initializes the VADER sentiment analyzer to calculate a sentiment score. If the compound score is greater than or equal to 0.05, it's considered positive, and if it is less than or equal to -0.05, it is considered negative. 

Throughout my assignment, I used ChatGPT to help with writing my code and providing me with ideas on what I can do with the topic that I have chosen. The link to my chat conversation is https://chat.openai.com/c/2b4dacd2-cab6-4ce4-8358-b67678cf2de0. 

**3. Results** (~2-3 paragraphs + figures/examples)
In my project, I found that between the Higher Education article and the List of US Grad School article, there were significant word frequency differences on global, research, professional, universities, students, institutions, and higher. Between the List of US Grad School article and the Fortune article, there were significant word frequency differences on full time, business, and schools. Between the List of US Grad School article and the Inside_HigherEd article, there were significant word frequency differences on new, programs, education, and graudate students. Between the List of US Grad Schools article and the Higher Education article, there were significant word frequency differences on research, professional, university, elite, national, universities, and ranking. This is interesting to see that the pattern here is mostly regarding whether or not the grad school is about research, professional, and the ranking of the schools. I presented these findings in the terminal with the usage of a histogram formatting. 

Another thing that I found was that across all four texts, upon conducting a sentiment analysis, all the texts came out with a neutral sentiment score. This is an interesting finding because I was expecting some articles to be biased towards some particular grad school programs and push the reader to consider those more than others. It is good to know that these articles are written monotonously and that they can be trusted and relied on for advice regarding grad schools. 

**4. Reflection** (~1-2 paragraphs) 
From a process point of view, I found it easy to analyze the word frequencies of each text because I referenced the previous hw on analyzing the Pride and Prejudice book. However, it was extremely difficult for me to pull the information from the web because NewsAPI was not working for me, and I ran into many articles that had paywalls on them, making it hard to extract information from. The process became easier after I made the decision to hard code the texts and pull data from files stored in Visual Studio. I feel that my project was appropriately scoped to a certain extent. I believe I had the right idea behind wanting to analyze articles on grad schools, however, I feel that my approach was not the best. After implementing a sentimental analysis and getting neutral sentiment scores for every article, I wasn't sure if I should have chose sentimental analysis for my texts because I don't think it added significant value. Also for testing, I wish I was able to figure out a better format to present my results as. I attempted to create a visual bar chart with x and y axes, but I couldn't get the code to run.

From a learning perspective, I definitely got more comfortable with creating dictionaires and storing keys to process and store the text files. I also learned to do a lot more searching on the web for how tos on python stuff that we did not learn in class and reading stackoverflow to see if some users ran into the same errors that I did, in order to try and break my error with NewsAPI. From ChatGPT, this assignment taught me how to ask the right questions to ChatGPT through trial and error in order to get the responses that I want out of it. I also learned to tell it to micmic code that I've previously written so ChatGPT is not creating brand new code for me and introducing new topics that I have yet to learn in class. Going forward, I can use ChatGPT more efficiently to help me with assignments, now that I know the structure and style I should be framing my questions to it. 