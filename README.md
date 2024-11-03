# Text Analysis Project Reflection

## 1. Project Overview

In this project, I used text data from Wikipedia, specifically the page for "Babson College". The goal was to perform text analysis using various computational codes, including word frequency analysis, sentiment analysis, text similarity, and clustering. I aimed to understand how computational methods can reveal insights about text content and relationships between texts. Through this project, I hoped to deepen my understanding of text processing, visualization, and the use of Python libraries for precssing texts.

## 2. Implementation

The project was implemented with several major components:
- **Data Retrieval**: I used the `mediawiki` library to fetch text content from Wikipedia, specifically the page for "Babson College".
- **Text Processing**: After retrieving text, I applied word frequency analysis, sentiment analysis using NLTK's VADER tool.
- **Similarity and Clustering**: I computed a similarity matrix with cosine similarity and visualized relationships between texts using a heatmap and MDS for clustering. Dendrograms were also used for hierarchical clustering.
  
One important design decision involved choosing between using pre-processing to remove stop words initially or filtering them out from the frequency dictionary afterward. I chose to filter them out the frequency dictionary afterwards to maintain flexibility in handling raw and filtered data separately. ChatGPT was helpful for troubleshooting errors and learning about techniques like MDS, which I was unfamiliar with.

## 3. Results

The project successfully demonstrated text analysis techniques:
- **Word Frequency Analysis**: After removing common stop words, I identified the most frequent words in the text. The analysis highlighted key themes, such as the business part and president of school. 
- **Sentiment Analysis**: Using VADER, I found that the text was largely neutral with slight positive tones. This was expected for an informational Wikipedia page.
- **Text Similarity and Clustering**: Visualizing similarity using MDS and heatmaps revealed clusters among texts from different universities, with closer proximity for those in similar contexts, like those located in Massachusetts. The dendrogram further showed relationships. 

### Figures
- **Heatmap of Similarity**: ![similarity_heatmap.png](similarity_heatmap.png)
- **MDS Plot**: ![mds_plot.png](mds_plot.png)

## 4. Reflection

This project taught me a lot about the nuances of text analysis. One of the most challenging aspects was setting up accurate similarity measures and finding effective ways to visualize the relationships. Using MDS turned out to be an effective approach. GenAI tools helped clarify complex concepts, making it easier to apply clustering and MDS, and provided quick solutions to errors that would have taken longer to troubleshoot independently.

If I were to improve this project, I would consider adding more complex NLP techniques, such as topic modeling, for deeper content analysis. Going forward, I’ll apply what I learned here to future text processing tasks, especially regarding visualization. In hindsight, having a clearer understanding of MDS and clustering beforehand would have helped streamline my workflow.
