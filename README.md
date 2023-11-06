# Text-Analysis-Project
 Please read the [instructions](instructions.md).

# Project Overview

 For my text analysis project, I used two novels sourced from **Project Gutenberg** as my primary dataset. Both by F. Scott Fitzgerald. Employing **Natural Language Processing (NLP)** techniques provided by the **NLTK library**, I focused on **part-of-speech tagging** and **sentiment analysis** to delve into the linguistic structure and emotional undertones of the texts. Additionally, I experimented with the **FuzzyWuzzy** library to conduct similarity analysis, which allowed me to quantitatively compare the texts. The goal of this project was to combine these methodologies to produce metrics that reveal insights about the author's use of language, the emotional arcs conveyed through F. Scott Fitzgerald's writing, and the stylistic similarities across his writing. By harnessing these computational techniques, I not only automated the process of literary analysis but also uncovered patterns and correlations within my favorite author's writing that might have remained undiscovered without an automated analysis.



 # Implementation

 The text analysis system I designed is structured to utilize Python's **urllib** for data retrieval and **NLTK for linguistic processing**, and uses **FuzzyWuzzy** for string matching and quantifying qualitative results. Initially, the two texts are **fetched** and then **preprocessed**, involving **case normalization**, **whitespace trimming**, and **punctuation removal**, using Python's regular expressions. A **list** of predefined stop words is employed to filter out any unimportant words from the analysis. Subsequently, the preprocessed texts undergo a **frequency analysis** through a custom function that constructs a word-to-frequency mapping. This word frequency data then serves as the basis for further linguistic exploration, such as **POS tagging** performed by NLTK, categorizing words into grammatical types. One pivotal design decision in the development was choosing FuzzyWuzzy's **WRatio** for similarity assessment between texts. While vector-based models like cosine similarity are common, I chose **WRatio** for simplicity.

 **Chat GPT** played a key role in my decision making process as well as in the structuring of my code. First, I used it as a brainstorming tool of how I could incorporate a few different python libraries into my analysis. I also used it as a learning tool to inform me on how to get certain python libraries to work and how to manipulate them to build a simple and efficient program. My decision to use **WRatio** and **FuzzyWuzzy** was heavily influenced by my questions to Chat GPT as it briefed me on the limitations of each library suggested in the assignment instructions.
 chat GPT url: https://chat.openai.com/c/536853a4-23c7-41df-9ca7-c3d7535fb4df


 # Results

 Through the use of python programming in my text analysis I found that F. Scott Fitzgerald's texts have striking similarities in their lexical structure through the metrics produced in my program. I found that the unique word usage in both texts was very similar as the word uniqueness ratios, **0.234 and 0.227** were nearly identical. This suggests that F. Scott Fitzgerald uses a very similar lexicon variety across his texts. These findings were extremely unexpected for me as I thought these texts would be much more varied in the number of unique words used. The difference between the two metrics grew as I added more and more stop words however, on a base level this similarity was striking. I also found that of the most common 10 words in each text respectively, half of them were the same for both. These words are out, up, been, one, and over. Out of the **10 most common words in each text 5 of them were the same and 2 of those words were names of different main characters in the novels.** From this I extracted the hypothesis that F. Scott Fitzgerald uses action words and descriptive prepositions most often across his texts echoing the diary like nature of his novels, desciribing events and scenes with vivid imagery. The heavy use of different character names was not out of the ordinary, it simply re-affirmed my thinking after I wrote the program. 

 The pos analysis resulted in interesting results as well. Seeing the frequency of nouns, verbs, and adjectives in each text was pretty surprising. I thought that the distribution of frequencies would be relatively even and very different for each text given their situational differences. However, the results of my text analysis program show that nouns were clearly the most common in both texts with 2766 words and 4970 words respectively. There was no difference in the order of most common to least common parts of speech either, with the most common in both texts being nouns and the least common being adjectives. 

 The similarity analysis also produced an interesting metric that was quite surprising yet in line with the results from my unique words analysis 0.18. Thus further alluding to the previous findings in that F. Scott Fitzgerald has a consistent writing style regardless of different scenarios.

 # Reflection
 
 From a process standpoint, the project to analyze literary texts from Project Gutenberg and compute similarities was largely successful. The scope was well-defined, allowing for focused analysis utilizing natural language processing techniques and fuzzy string matching. The preprocessing of text and the word frequency analysis went smoothly, laying a solid foundation for further examination. However, I could have done better in testing and error handling, particularly in ensuring that functions like word_similarity operate as intended when executed. A more rigorous testing plan could have identified issues with function calls and input types earlier in the process. Over the course of the project, I gained knowledge of the complexities of text processing, the value of cleaning and preparing data for analysis, and the different ways in which NLP tools may be used to extract insightful information from text. With its advice on debugging, code optimization, and introduction to alternate techniques for text comparison, such as cosine similarity, ChatGPT proved to be an essential resource. Moving ahead, this experience has emphasized the value of thorough testing and the advantages of creating code in a modular fashion. It would have sped up the development process if I had known more about the subtleties of NLTK and FuzzyWuzzy in advance.









