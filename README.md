# Text-Analysis-Project
 
Please read the [instructions](instructions.md).

---

#1. Project Overview

The data source used for sentiment analysis was a text document obtained from Project Gutenberg, specifically the eBook with the identifier '42671'. The sentiment analysis was conducted using the VADER (Valence Aware Dictionary and sEntiment Reasoner) tool, a part of the NLTK (Natural Language Toolkit) libraryThe project aimed to perform sentiment analysis on the text retrieved from Project Gutenberg. To extract sentiment scores related to the text data, such as the polarity of the sentiment (positive, negative, neutral), and the intensity of these sentiments.By utilizing sentiment analysis techniques, the project sought to gain insights into the overall emotional tone or sentiment expressed within the document sourced from Project Gutenberg.

---

#2. Implementation

For the components, the system starts by fetching text data from Project Gutenberg using the urllib library to access a specific eBook identified by a URL. The retrieved text is then decoded from UTF-8 and stored for further analysis. The NLTK library with VADER is utilized for sentiment analysis of the text data, generating sentiment scores (positive, negative, neutral, and compound scores) to gauge the sentiment expressed in the text. For the Algorithms & Data Structures, the system reads and decodes the text data, operating primarily with strings and encoding/decoding methods in Python. The VADER algorithm relies on a lexicon-based approach, considering the valence of words in a given text, their order, and their context to generate sentiment scores. It uses a predefined lexicon of words with associated sentiment scores.

One major decision in sentiment analysis was the choice of the sentiment analysis tool. While VADER within NLTK is powerful and well-suited for social media text, it may not perform optimally for all text types, especially if the text structure is complex or includes domain-specific language. An alternative could be employing machine learning-based models like recurrent neural networks (RNNs) or long short-term memory networks (LSTMs). However, these models often require extensive training on specific datasets, which might not be readily available or practical for smaller-scale projects like this. Therefore, VADER's lexicon-based approach was chosen due to its ease of use and relatively good performance in general text sentiment analysis tasks.

---

#3. Results

The results indicate that the analyzed text is predominantly neutral (0.754), with a moderate positive sentiment (0.164) and a minimal negative sentiment (0.082). The compound score of 1.0 signifies a highly positive overall sentiment.

---

#4. Reflection

The initial stages of the project, including data retrieval and sentiment analysis implementation, went well. However, a more detailed testing plan could have been beneficial, including segmenting the text for a more granular analysis and better visualization. The project scope could have been enhanced by considering different sections or chapters within the text for a more in-depth sentiment evaluation.

From a learning standpoint, this project provided a hands-on opportunity to implement sentiment analysis using VADER within NLTK. ChatGPT significantly supported by providing guidance on sentiment analysis methodologies, tools, and their strengths and limitations.

