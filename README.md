# Text-Analysis-Project

Please read the [instructions](instructions.md).

# Text Analysis Project: Wikipedia Page Analysis

## Part 3: Using GenAI

### Overview of Using GenAI Tools
Throughout this project, I utilised ChatGPT to enhance my learning and problem-solving skills.

- **Debugging Assistance**: When I encountered issues with the 'nltk' resources or other library imports, I consulted ChatGPT to quickly identify and resolve these errors.
- **Learning New Techniques**: ChatGPT introduced me to 'TheFuzz' library for easy comparison of text similarities.

### Examples of GenAI Help:
- **Debugging**: When I had an error with 'nltk' not finding the 'punkt_tab' resource, ChatGPT suggested downloading specific NLTK packages, which resolved the issue.
- **Learning**: ChatGPT explained how to use the 'SentimentIntensityAnalyzer' from 'nltk''s 'VADER' library to conduct the sentiment analysis, enhancing my understanding of how sentiment scoring works.
- **Optimization**: For analyzing word frequencies, ChatGPT advised using 'collections.Counter' for better performance.

---

## Part 4: Project Writeup and Reflection

### Project Overview
In this project, I analyzed the **FC Barcelona** Wikipedia page using Python to extract, process, and analyze text data. The project aimed to:
- Fetch and preprocess Wikipedia content.
- Analyze word frequencies and sentiment.
- Compare the similarity between the **FC Barcelona** and **Real Madrid** pages.

### Implementation
The project consisted of two main Python scripts:
1. **'data_collection.py'**: This script used 'pymediawiki' to fetch and clean the text data. Preprocessing included tokenization and stop word removal using 'nltk'.
2. **'text_analysis.py'**: This script analyzed text using 'nltk' for sentiment analysis and 'TheFuzz' for text similarity.

### Results
**Word Frequency Anlysis**:
The most common words in the **FC Barcelona** Wikipedia page were:
- 'barcelona': 216 occurrences 
- 'club': 179 occurrences    
- 'madrid': 72 occurrences

**Sentiment Analysis**:
- **Compound Score**: 1.0
- **Positive Score**: 0.136
- **Neutral Score**: 0.821
- **Negative Score**: 0.043

**Similarity Score**:
The similarity between the **FC Barcelona** and **Real Madrid** pages was '47', indicating significant overlap in topics related to football.

### Reflection
**What Went Well**:
- Successfully integrated Python libraries to fetch and process large text data.
- Word frequency and sentiment analysis provided insightful information about the content.

**Challenges**:
- Encountered issues with missing NLTK resources and Unicode characters during text processing.
- Initially struggled with efficient text tokenization and stop word removal.

**Solutions**:
- Used ChatGPT to help troubleshoot errors and improve my understanding of text processing functions.

### Future Improvements
- Explore topic modeling.
- Use more sophisticated visualizations to present data insights.