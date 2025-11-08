# Text-Analysis-Project
Please read the [instructions](instructions.md).

#Project Write Up and Reflection 

#1. Project Overview 

This project focuses on doing an overview of the play 'Romeo and Juliet' written  by William Shakespear. The functions of the code focused on removing the data set from the API 'Project Gutenber'. The overall project focused on cleaning and polishing all of the dataset, this includes removing all of the punctuations, stopwords, make all the characters be in lower case and remove any uncessary information from the data set. All of this was done using computational methods to also then run an analysis, such like a sentiment analysis, to analyze different information from the datas set. After running those analysis methods, I then introduced a document containing all of the translations of Old English words to New English words and translated the original file to an updated version with modern english words. Throughout the entire process I used several functions such as tex cleaning, stopword removal, word frequency analysis, text summary, visualisation and sentiment analysis, using the NLTK and TheFuzz package. My goal through this project was to identify different ways in which texts can be analyzed and identify if there was a potential way to introduce another data set to make the book easier for people to understand. 


#2.Implementation 

I started the project using an .ipynb file where I tested all of the data and went through the creation process of the code. This allowed me to check where functions could be improved or if there was any error that needed to be fixed. This made it easier for me to then pass the code to a .py file and run the final version of the project. After finishing drafting the code, I created several python modules to organize the data more clearly. 

For data structures I focused on mainly using dictionaries to then be able to store the word frequencies of the data sets and run the translation for the text. This approach made it easier because it allowed me to keep adding information whilst still running all of the regressions. I also chose to separate all of the data into multiple .py modules as it kept the code cleaner and allows for independent testing of each section before merging it all up. I also used the help from Chat GPT in various stages of this process to help me draft functions that I wasnt fully aware how they worked (my reasoning on how they work are on the comments in the .ipynb file) and it also helped me with debugging issues. The use of a virtual assistant allowed me to restructure my code more clearly and making sure it ran all of the functions. 

#3. Results 

As mentioned, I runned several .py methods that produced different analysis and results. I created five python modules: download.py which focuses on downloading, cleaning and processing the file; analysis.py which focuses on running all of the analysis formulas such as a bar chart visualisation, sentiment analysis etc. ; translation.py which focuses on reading the external dictionary file to then translate the old english words in the data files to the new english word file; similarity.py focuses on running a text similarity between both texts, old and new; and finally the main.py document which combines all of the formulas into one main document and process all of the text and runs all of the analysis in one file. 

These allowed me to identify the following results: 
 
Top 10 most common words:

and : 733
the : 688
my : 355
romeo : 298
thou : 277
me : 263
juliet : 178
thy : 170
o : 149
will : 148

 Text Summary Statistics:

Total words: 19309
Unique words: 3819
Average word length: 4.76
Average sentence length (in words): 0
Vocabulary richness: 0.198

    SENTIMENT ANALYSIS RESULTS    
Negative: 0.137
Neutral:  0.7
Positive: 0.163
Overall Compound Score: 1.0

→ The overall sentiment of the text is Positive. (this was a very surprising result given the tragic connotation of Romeo and Juliet)

TEXT SIMILARITY ANALYSIS    
Basic Ratio: 98
Partial Ratio: 98
Token Sort Ratio: 96
Token Set Ratio: 99

→ The two texts are very similar.

The bar graph helped plot the frequency of the most common words, I just cannot add an image to the text.

#4. Reflection 

The process of this porject managed to work very well as I managed to get the dictionary to translate the words and run all of the analysis functions on the text. Also separating the function on an individual python module made it easier to manage the data and work step by step. I believe that my biggest challenge in this assignment was to ensure that the transaltion worked correctly specific with all of the punctuation and spacing. The most complicated words to translate where the ones that had an apostrophe such as 'they'd' because when I removed all of the punctuation from the text it made it challenging for the dictionary to translate these words. Thats why I had to go back again to the code and make sure that only certain punctuation symbols were removed and not all of them. Another challenge was performance when comparing long texts using TheFuzz; I learned to limit the text sample size for efficiency as it was taking a lot of minutes to compare both texts together. 

My biggest takeaway from this project was that I realized how important it is to cleand and process data such as real-world text before running analysis regressions because if not the results given by the functions won't provide an accurate measurement. I also learned (and was surprised) that natural laguage processing tools such the NLTK package can help analyze the emotional tone of a novel and focus on the emotional perspective of a dataset rather than just doing statistical analysis. For this entire process, using a virtual assistant such as Chat GPT was very helpful to complete certain functions and uderstand the reasoning behind different approaches, like dictionaries for word frequency or splitting the project into modules, to get the results I wanted to obtain. The help from the virtual assistant also helped me debug the code and fix errors that my function had, making the overall creation process more effective. 

If I were to think of a recommendation to improve this project, I would like to expand the dictionary for a more comprehensive translation for all of Shakespear's plays. At the same time I believe it would be really interesting to create a proper python dictionary that can be implemented for multiple files. I would also recommend implementing the Markov text synthesis to generate sentences that use the same english style as William Shakespear does, that way new texts could also be generated with old english words to make more formal texts. Overall, I believe this project was really interesting to implement and it provided useful findings that taught me the importance of data cleaning, data processing and modular design. 

