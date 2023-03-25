# Text-Analysis-Project
 
Please read the [instructions](instructions.md).

**1. Project Overview** (~1 paragraph)

The data sources I used included the newsapi API in order to get the top headlines of the day,
along with the nltk package in order to perform sentiment analysis. The techniques I used to
analyze the data was sentiment analysis using nltk and also with my own personal ranking dictionary,
and I averaged each rating to get an overall market sentiment. Through this project, I hoped to learn
more about how to use dictionaries, APIs, packages, lists, and more, and I am happy with the result.

**2. Implementation** (~1-2 paragraphs + screenshots)

The first step in the process was to figure out which text I wanted to analyze.
At first, I was interested in tweets by famous individuals, such as Elon Musk,
However, I soon realized how complicated it was to actually use Twitter API
Paywalls and developer approval prevented me from using twitter (shame, it was a recent update).

Thus, I looked into news articles.
My curiosity led me to see if I can code a way to see the market sentiment from news articles.
The way I wanted to do this was to use NewsAPI to get the overall market sentiment from 
multiple news articles. I wanted to do this through article headlines. 
So, I created def news_article_headlines() that put various top news article headlines
of any given day into a list.

Once I created that function, the next step was to conduct sentiment analysis. To do this,
I created a new function called headline_sentiment. In this function, I used the nltk package
in order to conduct sentiment analysis on each headline. I then averaged the ratings of each
headline to get an overall "market sentiment value".

Even though I had a value, it would still be confusing for others to understand the value.
So, I created the sentiment_result() function that interprets it.

At this point in the project, I was proud of what I accomplished, but I wasn't satisfied.
I wondered if there was any way I could have done the project myself rather than having
to rely on the sentiment analysis of nltk. I also wondered how it worked. After doing some
research on sentiment analysis on wikipedia along with how nltk did it, I wanted to try it
myself. So, I created a function that had a custom dictionary. I asked ChatGPT to list out
many positive and negative words, and raking their sentiment from -100 to 100. Then, I asked
ChatGPT to format it into a dictionary and added it into the function. More details are 
commented in the custom_words_ranking() function.

Using chatGPT:
https://drive.google.com/file/d/1WLlrQbVglvG7cB2NqlujKWSrzkOOrBuO/view?usp=sharing

Now that the dictionary has been created, the hard part was analyzing it. It was a lot more
steps than just using one line of code to tell nltk to analyze a sentence. However,
I was able to figure it out in the custom_sentiment_analysis() function. 

One design choice I had to think of was with the sentiment_result function. At first,
I was going to make 2 functions, one for the nltk result, and one for the custom result.
Then, I realized, why not just add an input to the function: sentiment_result(n).
In this case, "n" would be the number result from each one, so in my main method,
I simply had to put:
    print(sentiment_result(headlines_sentiment)) 
    print(sentiment_result(custom_sentiment_analysis))

**3. Results** (~2-3 paragraphs + figures/examples)

What was interesting
was the difference in numbers between the nltk sentiment number and my custom number. One
reason was becasue I told chatGPT to give each word a rating between -100 to 100 while
nltk probably did -1 to 1. However, as of writing this, both nltk and my custom algorithm
provided a positive sentiment number, meaning that there is a positive sentiment in the market,
and there may be a correlation/similarity between the 2 datasets of words and their rankings.
Granted, the NLTK package probably has a more in-depth dictionary with a lot more words
and more accurate rankings that aren't AI-generated.

**4. Reflection** (~1-2 paragraphs)

While a lot of things went well (I already knew how to make dictionaries, lists, add APIs),
there were a lot of new things that I learned, and a lot of struggles along the way that
made the project very meaningful. For example, I learned how to implement a package (nltk).
What was great was that the website had a section on how to use the package, and what
services it offered. After going to the sentiment analysis section and reading up on it,
I realized it was something I wanted to utilize. However, the hard part was implementing it
in my very own project. It took a lot of time and thinking, as well as problem solving various
errors, but I was able to make it work.

The hard part about doing a custom project is that a lot of the times when you get an error,
you don't know what made the error. This is because a project can be very complicated in nature.
You don't know where the error stems from, since there are many parts of the code, and there
may even be multiple errors. However, by using various troubleshooting techniques like print()
in order to see if something is running properly, I was able to address the problems and fix them.
A lot of these print commands are still embedded in the code, but commented out because I was
able to solve them.

Moving forward, there's a lot I can do to improve the project. For example, in my custom analysis
the words I used were mostly adjectives, so maybe the result would be neutral (0.0), because
none of the words in the dictionary matched the words in the news headline. Another thing
is that some words are capitalized and some words are not, which may be affecting the result.
This is something I would change if I had time.

However, overall, I am very happy with the project as I was able to learn a lot and there was 
a lot of satisfaction with getting the code to work properly after many hours of going through
it looking for errors.
