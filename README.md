# Text-Analysis-Project
 
Please read the [instructions](instructions.md).

1. Project Overview (~1 paragraph)

What data source(s) did you use? What technique(s) did you use to process or analyze them? What did you hope to create or learn through this project?

I used Project Gutenberg for my data source, and downloaded the texts of my choice from there. I used techniques such as filtering stop words with my custom stop word list to create a filtered version and tokenizes the text into words. I selected 3 targets words to conduct the frequency test (bokhara, silk and trade). I then also identified and printed the top 10 words in the text, as well as various unique words. Afterwards, I imported the nltk library to perform natural language processing & sentiment analysis and the text similarity test selection with fuzz. In addition, as part of text clustering, I performed cosine similarity calculation and the MDS visualization with tools such as sklearn, numpy and matplotlib. Lastly, I experimented with the Markov Analysis model and discovered different interesting combinations that can be generated from the texts. Because I am a big history and archaeology enthuasiast, I selected texts on the Central Asia region that is known for its silk road trade and cultural interaction in history, from the Project Gutenberg website. I was excited to integrate my love for history with python, and I wanted to conduct a text analysis to extract information from the selected books on Central Asia and learn about the similarities between two texts that are on a similar topic, for instance ("Sketches of Central Asia" by Ármin Vámbéry and "Travels into Bokhara" by Sir Alexander Burnes)

2. Implementation (~1-2 paragraphs)

Describe your implementation at a system architecture level. You should NOT walk through your code line by line, or explain every function (we can get that from your docstrings). Instead, talk about the major components, algorithms, data structures and how they fit together. You should also discuss at least one design decision where you had to choose between multiple alternatives, and explain why you made the choice. Use shared links and/or screenshots to describe how you used ChatGPT to help you or learn new things.

In this text analysis project, several major components and algorithms are involved. The process begins with data retrieval from external sources, specifically Project Gutenberg, followed by text preprocessing, including the removal of custom-defined stop words. Frequency analysis is conducted for specific words to understand their significance within the text. The text is then tokenized using regular expressions, and word counts are calculated to identify the top 10 words. Additionally, sentiment analysis is performed using the VADER tool to gauge the emotional tone of sentences within the text. Comparing text similarity through the FuzzyWuzzy library enables the assessment of textual resemblance. Furthermore, Multi-dimensional Scaling (MDS) is utilized to cluster and visualize texts in 2D space, aiding in the identification of text clusters.

A key design decision centers on the use of TF-IDF vectorization for text similarity analysis, combined with cosine similarity for measuring the likeness between texts. This choice aligns with standard Natural Language Processing practices. For the project, I used ChatGPT as a valuable resource and tool for insights, debugging, explanations to clarify complex code, and alternative approaches. ChatGPT was very helpful with structuring and debugging the cosine similarity functions, the MDS visualization and the Markov Analysis Model. 

3. Results (~2-3 paragraphs + figures/examples)

Present what you accomplished in your project:

If you did some text analysis, what interesting things did you find? Graphs or other visualizations may be very useful here for showing your results.
If you created a program that does something interesting (e.g. a Markov text synthesizer), be sure to provide a few interesting examples of the program's output.

I found some cool things from the text analysis, such as the frequency of words like bokhara, silk and trade. I also was able to identify the top 10 words and find a variety of unique words from the text, as well as similarity ratio between strings. When conducting a test on the two different texts on a similar topic, I was able to find their Pairwise Cosine Similarities and visualized it through MDS (in code). The Markov test seemed very fascinating, and some examples from the output are: 

4. Reflection (~1-2 paragraphs)

From a process point of view, what went well? What could you improve? Was your project appropriately scoped? Did you have a good testing plan?

From a learning perspective, mention what you learned through this project, how ChatGPT helped you, and how you'll use what you learned going forward. What do you wish you knew beforehand that would have helped you succeed?

This text analysis project has been a rewarding journey from both a process and learning perspective. From a process point of view, the data retrieval and preprocessing steps seemed to have worked well. The integration of various libraries and tools to extract and clean the text, remove stop words, and conduct frequency and sentiment analysis was challenging, but successful at the end. The decision to use TF-IDF vectorization for text similarity analysis, as suggested by ChatGPT, turned out to be a suitable choice, and the project's scope was reasonable for the objectives outlined.

In terms of learning, this project has deepened my understanding of natural language processing and text analysis. ChatGPT played a valuable role by providing ideas, organization, alternative approaches, and debugging assistance that helped me overcome obstacles. The project's interactive nature has been a practical way to apply NLP concepts in a real-world scenario and to a topic of my interest. Looking forward, I'll utilize this knowledge in more complex text analysis projects and explore advanced techniques. 