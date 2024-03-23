# Text-Analysis-Project
**1. Project Overview**

I mainly used Wikipedia as my data source. I chose it because I believe it is a balanced source with proofreading facts and data. I used MediaWiki API to fetch and analyze content from Wiki pages of Nvidia, AMD, GPU and CPU. I used sklearn for Multidimensional Scaling (MDS), matplotlib for visualization, and nltk for natural language processing; the goal was to explore similarities and differences in the content of these pages as well as provide a summary. I learned a comprehensive way to analyze a piece of text, providing insights not only including a basic summary of words but also advanced analysis like the overall sentiment.  

**2. Implementation**

The project's architecture involves fetching data from Wikipedia pages and processing this textual content to perform various analyses. The MediaWiki library was used to fetch content. The analysis starts with some basic word analysis, such as counting the word frequencies, and preparation work, such as removing all the stop words (I, am, the, they, them, etc.). Then the fuzz library from thefuzz package provided functionality to compute textual similarities, enhancing robustness against variations in word order. The nltk library was used to remove stopwords and conduct sentiment analysis.

One of my design decisions was to choose `fuzz.token_sort_ratio` over the normal fuzz.ratio approach. The reason behind the decision is that the `fuzz.token_sort_ratio` method is particularly useful when the order of words might vary, but the words themselves are the same or very similar. In my case, Wikipedia is indeed a source that needs robustness. 

ChatGPT also helped me debug and learn new libraries. For instance, it explains to me how to apply Metric Multidimensional Scaling (MDS) for text clustering. 
![alt text](<Screenshot 2024-03-22 at 23.07.48.png>)


**3. Results**
The analysis revealed intriguing relationships between the analyzed tech companies and concepts. For example, the similarity scores indicated closer textual relationships between company pages (Nvidia, AMD). 
```
The Wekipdia page of Nvidia and AMD has a 38% similarity ratio.

The Wekipdia page of Nvidia and AMD has a 62% sorted similarity ratio. (Persoanlly I believe in this score since the two companies are in the same industry field.)
```

The companies and concepts (CPU, GPU) have a distinct separation between these two clusters in the MDS plot. The plot layout clearly delineates how Wikipedia content is structured around company profiles versus technology concepts.
![alt text](Figure_1.png)

The sentiment analysis's orientation is mostly neutral, with slightly positive means in the identified Wikipedia text. This trait aligns with the articles' academic and objective orientation. Nonetheless, the small differences in the sentiment scores perhaps indicate changes in how the public perceives institutions or their different periods of development and functioning.
```
The sentiment analysis of the Nvidia Wikipedia page is:
{'neg': 0.027, 'neu': 0.902, 'pos': 0.071, 'compound': 0.9997}

The sentiment analysis of the AMD Wikipedia page is:
{'neg': 0.026, 'neu': 0.899, 'pos': 0.075, 'compound': 0.9999}

The random sentence of the Nvidia Wikipedia page is:
The investigation is set to end on March 15, 2022.

The sentiment analysis of the random Nvidia Wikipedia sentence is:
{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}

The random sentence of the AMD Wikipedia page is:
Throughout 2007 and into 2008, AMD has continued to add both single-core Mobile AMD Sempron and AMD Athlon processors and dual-core AMD Athlon X2 and AMD Turion processors to its embedded product line and now offers embedded 64-bit solutions starting with 8 W TDP Mobile AMD Sempron and AMD Athlon processors for fan-less designs up to multi-processor systems leveraging multi-core AMD Opteron processors all supporting longer than standard availability.The ATI acquisition in 2006 included the Imageon and Xilleon product lines.

The sentiment analysis of the random AMD Wikipedia sentence is:
{'neg': 0.0, 'neu': 0.943, 'pos': 0.057, 'compound': 0.5574}
```

**4. Reflection**

In conclusion, this project was a productive journey of exploring how NLP techniques can help us understand relationships in textual data. Everything from fetching the data to pre-processing the text to applying the analysis techniques was smooth, mainly because of the variety of powerful libraries and easy-to-use APIs. To improve this project, I believe I could work on the pre-processing process by trying more sophisticated methods of handling synonyms and technical jargon, which are abundant in tech-related news and articles. I believe this project can be a good bedrock for future projects, like fetching news and generating sentiment scores for users to reference. 

As for learning, this project solidified the basics of NLP for me and showed me the actual use cases of text similarity and sentiment analysis. Using ChatGPT as a roadmap genuinely helped me navigate the research and coding process, easily getting to the bottom of the library documentation or finding and eliminating the bug. In the future, I plan to dive deeper into machine learning models for more sophisticated text analysis and look forward to implementing more advanced data visualization techniques to visualize results more interpretably. I wish I knew how to efficiently use the different Python libraries like Numpy or re, as these two libraries are often used in bigger projects. 

The ChatGPT conversation link:
1. https://chat.openai.com/share/693dc5f1-0cb5-49c1-9579-bc61291ae0c6
2. https://chat.openai.com/share/582df36a-9fb0-4067-82b7-69125e39a364
