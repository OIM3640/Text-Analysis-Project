# Text-Analysis-Project

# 1. Project Overview

For this project, I used the text of *Oliver Twist* by Charles Dickens, which I accessed from Project Gutenberg. My main goal was to explore how to harvest a real book from the internet and then analyze its contents using basic text processing techniques. I wanted to identify the most frequently used words and also evaluate the overall tone or sentiment of the text. I used Python to clean the text, filter out common "stop words," count word frequencies, and perform sentiment analysis. Through this process, I hoped to improve my skills in working with text data and learn how to apply natural language processing techniques in a real-world context.

# 2. Implementation

I structured the project into three main Python files:  
- `harvest_text.py`: handles downloading the text from a URL  
- `analyze.py`: contains all the text processing and analysis functions  
- `main.py`: serves as the entry point that ties everything together and prints results

In `harvest_text.py`, I used `urllib.request` to download the raw text from the provided Project Gutenberg link. This part was fairly straightforward, and I followed the structure given in the instructions.

In `analyze.py`, I wrote functions for word cleaning, stop word removal, word frequency counting, and sentiment analysis. I originally planned to just use `.split()` to tokenize words, but that included punctuation and other symbols. After getting stuck, I asked ChatGPT to help me understand a regular expression that would return only clean words, which led to using `re.findall(r'\b[a-z]+\b', text)`. I also used the `nltk` library for stopword filtering and sentiment analysis. I had to install and download the necessary NLTK resources (`stopwords` and `vader_lexicon`), and I used the `SentimentIntensityAnalyzer` to get sentiment scores. GPT helped me understand how to interpret the output from this tool and what each score meant.

In `main.py`, I called all the functions in a logical sequence: download the text, extract words, filter stopwords, count word frequencies, and run sentiment analysis. The final result prints out the top 10 most common words and the sentiment scores for the entire book.

# 3. Results

After processing *Oliver Twist*, I was able to identify the most frequently used non-stopwords. Most of them are key characters or common narrative terms, which makes sense in the context of a novel. Here’s the output of the top 10 words:

Top 10 words (after removing stopwords):
said: 1233
mr: 1080
oliver: 880
upon: 481
one: 466
replied: 464
old: 450
would: 413
man: 398
bumble: 397

For sentiment analysis, I used `nltk`’s built-in VADER tool. This gave me a breakdown of how positive, neutral, or negative the overall tone of the book was. Given the darker themes in *Oliver Twist*, I expected it to lean more negative or neutral. Here’s what the sentiment scores looked like:

Running sentiment analysis...
Sentiment scores:
neg: 0.092
neu: 0.784
pos: 0.124
compound: 1.0

The scores suggest that while the text contains some negativity(0.092), it’s overall fairly neutral in tone with a score of 0.784. The compound score is close to 1.0, which might reflect the presence of both light and dark moments in the story.

# 4. Reflection

Overall, I’m really happy with how the project turned out. I was able to write most of the code myself and organize the project in a clean and modular way. The hardest part for me was working with regular expressions — I wasn’t sure how to extract only the real words from the text at first. I also wasn’t confident in how sentiment analysis worked, but ChatGPT helped explain both of these parts clearly. It didn’t write everything for me, but it made it easier to understand tricky concepts that I probably would’ve struggled with on my own.

From a learning perspective, I now feel more confident using libraries like `nltk` and working with large text datasets. I also learned how important it is to clean and structure text properly before trying to analyze it. If I were to continue the project, I’d probably add a second book for comparison or try visualizing the word frequencies with a bar chart. I feel like the scope was very appropriate for my level and I was able to test my code frequently to make sure each step was working correctly.

