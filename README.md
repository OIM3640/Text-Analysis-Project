### Text-Analysis-Project
 
Please read the [instructions](instructions.md).

## Project Overview

- This was the first Assignment we have done which I thoroughly enjoyed and put in more hours that I needed to complete. The data source that I used for this project was Project-Gutenberg. I initially was going to try to use an API - but realized that this might prove too complicated for me at this stage. In middle school, I read the play "The Importance of Being Earnest" by Oscar Wilde in my English Literature class. I wanted to analyze this text as it brought me back to my middle school days where I remember enjoying reading the play. 

- I used a wide variety of techniques to analyze the text. I used multiple libraries, including NLTK, WordCloud, urlib, and textstat.

- Through this project, I hoped to learn how to apply the python code and libraries to analyze something in the real world. This is why this project was so exciting for me and I have started to enjoy the programming process. I would also say I got a lot strong at using ChatGPT, which I will go further in depth later on.

## Implementation

- The implementation for text analysis involved numerous components including data retrieval, preprocessing, analysis, and visualization components. The selection of libraries, including NLTK, wordcloud, urlib, and texstat helped perform a myriad of functions including character extraction, word freqeuency analysis, and readability. The textstat module was especially helpful for that. For the visual representation of word frequencies, the wordcloud library created visually appealing representations. The system integrated these stages, transforming raw text into structured data and interesting visual insights. Wordcloud was definetely my favorite tool to play around with as the size and colors could be adjusted. It was also extremely interesting to see the program generate multiple formats of the same text representation.

- During the implementation process, I came across "Topic Modelling" Which involves using LDA (Latent Dirichlet Allocation) to extract underlying themes in a text. I wanted to use this to highlight the important themes of the play (including marriage, class, societal expections), but could not do so because the ChatGPT proposed code kept trying to use the frequently recurring words as input. Most of the frequently recurring words involved the names of the characters, and so the output of themes was consistently just names. I had to pivot from this process as I realized this would not work, and found the applications of wordcloud instead.

-  ChatGPT-generated code samples significantly contributed to learning and problem-solving, aiding in the understanding of more advanced NLP techniques and refining the implementation approach. These shared insights and code snippets from ChatGPT enhanced the overall understanding and implementation of the text analysis system. I was very impressed by the details and granularity that the AI-Model could generate, and I really pushed it to it's limits as seen below:

![ChatGPT Example1](ChatGPT_Example_1.PNG)
![ChatGPT Example2](ChatGPT_2.PNG)

## Results

- While embarking on the text analysis project, several intriguing findings emerged from the analysis of "The Importance of Being Earnest." The application of various tools yielded fascinating insights into the text. The word frequency analysis showcased that words like "love," "man," "life," and "time" were recurrent throughout the play. Interestingly, the WordCloud visualization vividly highlighted the prominence of these terms, visually showcasing their frequency in a captivating display. Moreover, the Flesch Reading Ease score (77.03) affirmed the play's readability at a level suitable for a broad audience, offering an engaging narrative accessible to a wide spectrum of readers.

- The colorful word clouds and character interaction analyses didn't just show the main themes in the text; they also created cool pictures of how characters are connected and how the story works. This approach helped us find the main ideas in the play and see how the characters relate, giving us a full picture of what the play is all about.

- The sentiment analysis was also very interesting. I initilly wanted to do an analysis based on page numbers (1-50, 50-100), but quickly realized this would not be possible due to the UTF formatting. Instead, with the help of ChatGPT, I broke down text into 4 parts based on character count. I then used NLTK to gauge the sentiment of the four parts, and found that all four parts were "relatively positive". This makes sense as the play is supposed to encapsulate a comedic satire, poking fun at old traditions and societal expectations in Victorian England.

![WordCloud Result](Wordcloud.PNG)
![Readability Analysis Result](Readability_analysis.PNG)
![Sentiment Analysis Result](Sentiment_analysis.PNG)

## Reflection

- Through delving into text analysis with "The Importance of Being Earnest," this project unveiled an array of interesting discoveries. Shifting away from certain analysis approaches that didn't quite match the play's essence taught the valuable lesson of aligning techniques with the text's context for more meaningful interpretations. Adapting my strategy when they didn't sync with the play's themes highlighted the iterative nature of analysis. ChatGPT's guidance proved crucial in not only recognizing mistakes but also sparking better ideas, steering the project in a more promising direction. 

- For future projects, clearer scoping and a more organized testing plan could refine the analysis process. I went into the process blind and tried to figure things out along the way. While many of the libraries and tools were new to me, I should have used my understanding of the play to pick and choose better analysis methods, which in turn would have saved me a lot of time. 

- ChatGPT was crucial in the construction of this project. As mentioned previously, this project was a steep learning curve, diving into various NLP tools and their practical uses. ChatGPT's ability to offer code samples, explanations, and alternative methods not only fixed errors but also expanded the range of viable analysis techniques which I eventually simplified down to "Compute summary", "frequency counter", "graphics analysis", "readibility analysis", and "sentiment analysis". 

- Overall, this was a wonderful experience that showed me the power of both Python and ChatGPT. I plan on using what I learned today in my final project, where I can consistenyl refine the methods that I use to extract and build. 


