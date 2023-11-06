# Text-Analysis-Project
 
Please read the [instructions](instructions.md).
extra code line used w explanations from gpt:https://www.nltk.org/data.html
https://chat.openai.com/share/d0c052d3-525f-46ff-8a44-ea2ceb35ad55
https://chat.openai.com/share/9143bb30-37a1-4c06-a5cb-d8a6c39e943b


I realized that the IMDb API reviews were lengthy, and instead of using a common words function for each review, I decided on a logical summary function. I discovered the necessary code online but needed help understanding it, so I turned to GPT for a line-by-line explanation. This was also the case for sentiment analysis. The Natural Language Toolkit (NLTK) was utilized for these tasks.

My project comprises four main functions, with two nested, resulting in three distinct functions serving the user. The first step was to import all the necessary packages, followed by creating instances for the IMDb API. Next, I developed a function for text summarization, which processes input text using corpus and tokenizers. It retrieves stopwords from NLTK, tokenizes the text excluding those stopwords, and constructs a frequency table. This function calculates scores based on the frequency of the tokenized words and generates a summary of the input text for those with a score >=1.2 times the average, producing a concise summary.

The subsequent function retrieves all reviews from the IMDb API and then utilizes the previously created summarizer to condense each review iteratively. Another function counts the occurrences of predefined positive-connotation words in each review and presents a numerical summary of these instances. The final function conducts sentiment analysis on each review using SentimentIntensityAnalyzer. It processes each review in a loop and returns the sentiment type—neutral, negative, or positive—along with a total count of each sentiment type.

Interestingly, during the project, I learned to tokenize and utilize the summarizer, altering a code I found online that rates every word to create a brief summary of the reviews. Additionally, with the help of NLTK packages and guidance provided in the instructions and on Reddit, I was able to implement a sentiment analysis function.

Moreover, I managed to search for a list of words within the text obtained from the API and summarized the frequency of these words across all reviews for a specified movie. The data gathering from the API went smoothly, and the loops used in each function were similar, requiring only minor adjustments. Adapting code from the internet for my needs proved to be fairly straightforward.

One potential improvement for the code could be to extract not only the input but also the predominant negative connotations from each comment, which could then provide a percentage score indicating the movie's worthiness to watch.

GPT and Reddit were incredibly helpful throughout my coding process, especially regarding sentiment analysis and the development of the summary maker. GPT greatly assisted in constructing the logic flows of the functions and also provided excellent recommendations. I definitely plan to utilize the knowledge and packages acquired in this project and had a solid testing plan in place.