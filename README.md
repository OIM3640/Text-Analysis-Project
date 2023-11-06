# Text-Analysis-Project
 
Please read the [instructions](instructions.md).

Patterns within Words
There is a vast amount of text that is waiting to be decoded on the internet. With that in mind, my project centers around techniques that could help analyze hidden information within the texts. In order to do so, I sourced the text data from the online database of Project Gutenburg to find information related to information regarding a research project of mine focused on the implementation of asian joinery techniques with modern manufacturing. The aim of this specific project aimed to extract and process texts from Project Gutenburg to discover patterns and trends related to the topic. 

Implementation
My project begins with automatically downloading texts from Project Gutenburg through HTTP requests and then parsing the text data recieved. 

After the download, lists were used to store data and dictionaries were used to count and categorize key terms as well as wanting to count the occurences of each term. I also wanted to be able to easily know if the texts were of use to me relating to the field of my interest so I created target words to be able to find if my focus was in the text. 

In order to analyze the text, I also used the NLTK library for text processing which allowed me to find specific information related to my interests. 

Results
The text analysis allowed for me to be able to see which joinery techniques were most often mentioned as well as the similarities between two strings that were grabbed from the text. I also created visualizations using Matplotlib to show the patterns. 

Reflection
The project was very difficult but was fruitful in being able to better understand potential utilizations that I could have in the real world in my own utilizations as I had to use the assignment in my own context. By making the project relating to something similar to what I could potentially need myself to make my quality of life improved, I was able to better understand how data sources and the utilization of python can help analyze texts more effectively. 

I also learned how I could use Chat GPT effectively as I was able to ask questions such as why markovify was not being properly installed as install was apparently an invalid syntax, reccomending that I exit Command Prompt to retry.  When also encountering bugs that I did not know where, it was also able to point out potential areas of errors. 

I was able to learn a lot about text analysis and was also able to find information relating to my own external research. I am intending to find ways to perhaps find a better way to also be able to use other books to analyze more information to find what I need. This project has made me more sure to also plan things more in advance to best present the results in a more consumable and understandable way. 