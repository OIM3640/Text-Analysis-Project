# Text-Analysis-Project
 
Please read the [instructions](instructions.md).


#PROJECT OVERVIEW
#For my project, I chose Wikipedia as the source of data, focusing specifically on the Babson College page. Using natural language processing techniques, I processed the text by removing stopwords and characterizing word frequencies using NLTK. Moreover, I added sentiment analysis using NLTK's VADER tool to see what the overall sentiment of the article was (hoping it was mostly positive!). I also plotted the 10 most frequent words in the article using Matplot. I wanted to complete the text analysis project not only to see my progress in Python programming and NLP libraries but also to explore the practical application of these techniques in understanding textual data. Through this project, I gained hands-on experience in accessing and analyzing text data programmatically, as well as developing a deeper understanding of sentiment analysis.

#IMPLEMENTATION
#This text analysis project had three major components: inserting the data into Python, text processing, and then analysis of the text. First, the data retrieval part brought the Wikipedia article on Babson College using the `MediaWiki` library. Once the text data was obtained, I removed the stopwords and tokenized the text using NLTK. Then, the processed text was used for further analysis, such as word frequency characterization and sentiment analysis (using NLTK's VADER tool).

#Choosing the 'right sentiment analysis tool' was a crucial decision in the design of this project. While I chose NLTK's VADER tool, I considered alternatives such as training a custom sentiment analysis model or using other sentiment analysis libraries like TextBlob. However, after the research, I realized that the beginner-friendly nature of VADER made it the most suitable choice for this project. It aligned well with my learning objectives, as a beginner, in text analysis. Then, I decided to plot the most frequent words, in a bar chart, to visually see the most seen words in the article and the amount of times each one appeared. Also, I used ChatGPT to learn different techniques for the analysis of the text. It provided me with suggestions and explanations on various algorithms and libraries. Through shared links and screenshots, I documented ChatGPT's assistance, incorporating it into the learning process.

#RESULTS
#For my project, I analyzed the Wikipedia article on Babson College. My goal was to identify the frequently used words associated with Babson and determine the sentiment of the article. The analysis revealed that words such as "entrepreneurship," "business," "MBA," and "CEO" were frequently used in the article, indicating the college's focus on these areas. Additionally, using word frequency analysis, I identified the most commonly used words in the article, which further demonstrated the significance of these terms. The sentiment analysis indicated a largely positive sentiment associated with the text, which suggested a positive portrayal of Babson College in the article.

#To make the word frequencies easier to understand, I created a bar chart displaying the top 10 most frequent words in the article after removing the stopwords. The chart made it clear that "Babson" and "MBA" were the most prominent terms in the article. Moreover, I generated a sentiment analysis score that indicated the overall sentiment of the text, which further supported the positive tone of the article. These findings helped me gain a better understanding of the sentiments expressed in the article.

#REFLECTION
#During this project, I faced challenges that turned to be rewarding. As I worked in the text analysis, I found myself captivated by the procedures employed to extract information from Wikipedia. I gained knowledge of Python libraries and utilized resources such as NLTK and MediaWiki to facilitate my work. Despite running into limitations during the process, I used AI and the Google engine to overcome obstacles.

#Throughout this project, I not only learned practical skills in text analysis but also increased my understanding of natural language processing concepts. As I reflect on the project's conclusion, I feel a sense of accomplishment for the learning experience. Equipped with new knowledge, I am eager to apply this to future works, looking forward to taking on even more ambitious tasks that lie ahead.

