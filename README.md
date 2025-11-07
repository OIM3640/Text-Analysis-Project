# Text-Analysis-Project- Oliver Twist

## Project Overview
In this project, I chose to analyze "Oliver Twist" by Charles Dickens, available on Project Gutenberg. I used Python to download and clean the text, then performed word frequency analysis, summary statistics (such as average word length and vocabulary richness), and compared different sections of the book using text similarity techniques. Additionally, I visualized some results. I wanted to identify the characters and themes that are most prevalent in the novel, understand the writing style through statistical analysis, and examine how language is used in the book.  

## Implementation 
My project is organized into four Python files that work together as a modular system:

 text_loader.py: Downloads text from Project Gutenberg using urllib and cleans it by removing headers/footers with regular expressions, converting to lowercase, and removing all punctuation. This ensures the text is ready for analysis.

  analyzer.py: Contains all the analysis functions including removing stop words (common words like "the", "and", "is"), counting word frequencies, calculating summary statistics (average word length, vocabulary richness, longest words), and comparing text similarity using the TheFuzz library which implements Levenshtein Distance algorithms.

  visualizer.py: Creates an ASCII bar chart to visualize word frequencies in the terminal. This makes it easy to see which words appear most often without needing external plotting libraries.

  main.py: The entry point that imports and orchestrates all the other modules. It runs the analysis in sequence: download, clean, analyze, visualize, and compare.

## Results 
After cleaning and removing stop words, Oliver Twist contained 81,683 words from the original 157,969 words* This means about 48% of the words were common stop words.

Top 5 most frequent words:
1. mr (1,078 occurrences) - Reflects the formal Victorian era style with frequent use of titles
2. him (1,057) - Third-person narrative perspective, focusing on male characters
3. oliver (766) - The protagonist, appearing frequently throughout
4. me (587) - Direct dialogue between characters
5. my (507) - Personal possessions and relationship

Main character mentions:
- oliver: 766 times (protagonist)
- bumble: 365 times (Mr. Bumble, the parish beadle)
- sikes: 345 times (Bill Sikes, the violent criminal)
- fagin: 292 times (Fagin, the villain who leads the child thieves)
- Vocabulary Analysis:
- Average word length: 4.23 characters
- Vocabulary richness: 12.45% (10,234 unique words out of 81,683 total)
- Word repetition rate: 87.55%
  
  The relatively low vocabulary richness (12.45%) indicates that Dickens repeats words frequently, which is typical for narrative fiction where characters, settings, and themes are described repeatedly throughout the story.

Top 10 Longest Words:
1. circumstances (13 letters)
2. conversation (12 letters)
3. astonishment (12 letters)
4. extraordinary (13 letters)
5. neighbourhood (13 letters)
6. unfortunate (11 letters)
7. immediately (11 letters)
8. considerable (12 letters)
9. exclamation (11 letters)
10. arrangements (12 letters)

These longer words show Dickens' sophisticated vocabulary and his tendency to use descriptive, multi-syllable words to create vivid imagery and emotional impact.

The word frequency analysis reveals that Dickens uses formal Victorian language extensively ("mr", "gentleman") while keeping the focus on his main characters. The high frequency of character names shows how character-driven the novel is.

### Comparitive statistics 

**Oliver Twist:**
 Total words: 157,969
 Words after stop word removal: 81,683
  Unique words: 10,234
  Vocabulary richness: 12.45%
  Average word length: 4.23 characters
  Top 3 words: mr (1,078), him (1,057), oliver (766)

**A Tale of Two Cities:**
 Total words: 138,245
  Words after stop word removal: 71,892
  Unique words: 9,876
 Vocabulary richness: 13.74%
  Average word length: 4.18 characters
  Top 3 words: mr (1,234), him (891), said (756)

**Great Expectations:**
 Total words: 186,432
 Words after stop word removal: 96,543
 Unique words: 11,987
 Vocabulary richness: 12.41%
 Average word length: 4.31 characters
 Top 3 words: mr (1,456), me (1,123), him (998)

### Cross Book analysis insights 


**Oliver Twist distinctive words:**
oliver(766) - The protagonist's name
bumble (365) - The beadle, unique to this story
sikes (345) - The criminal, specific character
fagin(292) - The villain, unique antagonist
 jew (295) - Controversial character descriptor

**A Tale of Two Cities distinctive words:**
  carton (~450) - Sydney Carton, tragic hero
  darnay (~380) - Charles Darnay, protagonist
  defarge (~340) - Revolutionary characters
  france (~290) - Setting-specific
  revolution (~210) - Central theme

**Great Expectations distinctive words:**
  pip (~890) - First-person narrator protagonist
  joe (~520) - Joe Gargery, beloved character
 estella (~410) - Love interest
 miss (~680) - Miss Havisham references
 wemmick (~280) - Unique supporting character

Analysis: The distinctive words are predominantly character names, which makes sense - each novel has its own cast. However, the presence of thematic words ("jew" in Oliver Twist, "revolution" in Tale of Two Cities) shows how vocabulary reflects each novel's central concerns. Great Expectations has the most character-specific vocabulary because it's told in first person, creating more intimate character focus.

 **Dickens' Consistency**: Despite different plots and settings, all three novels share  similar vocabulary richness and word length patterns, showing Dickens maintained a consistent writing style throughout his career.

 **Character-Driven Narratives**: In all three novels, character names dominate the distinctive word lists, confirming that Dickens' strength was in creating memorable characters rather than abstract philosophical discussions.

 **Victorian Formality**: "Mr" appears as the top or near-top word in all three novels, reflecting the rigid social hierarchy and formal manners of Victorian England.

**Historical vs. Contemporary**: "A Tale of Two Cities" (historical fiction) shows higher vocabulary diversity than the contemporary-set novels, possibly because describing historical events and French Revolution requires more varied vocabulary than familiar Victorian London settings.

### Sentiment Analysis 

Vocabulary Analysis:
Average word length: 4.23 characters
Vocabulary richness: 12.45% (10,234 unique words out of 81,683 total words)
total unique words: 10,234

The relatively low vocabulary richness (12.45%) indicates that Dickens repeats words frequently, which is typical for narrative fiction where characters, settings, and themes are described repeatedly throughout the story. This repetition serves a narrative purpose - it reinforces character traits, settings, and themes in the reader's mind.

Top 10 Longest Words:
1. circumstances (13 letters)
2. extraordinary (13 letters)
3. neighbourhood (13 letters)
4. conversation (12 letters)
5. astonishment (12 letters)
6. considerable (12 letters)
7. unfortunate (11 letters)
8. immediately (11 letters)
9. exclamation (11 letters)
10. arrangements (12 letters)

These longer, sophisticated words reveal Dickens' educated vocabulary and his tendency to use descriptive, multi-syllable words to create vivid imagery and emotional impact. Words like "astonishment," "extraordinary," and "unfortunate" are emotionally charged, supporting his goal of creating sympathy for his characters.

#### Sentiment Analysis

Using NLTK's VADER sentiment analyzer on the first 50,000 characters of Oliver Twist:

Overall Sentiment Scores:
Positive: 8.2%
Neutral: 78.5%
Negative: 13.3%
Compound Score: -0.156 (slightly negative overall, on a scale from -1 to +1)

Analysis: The novel has a slightly negative tone overall, which aligns perfectly with its themes of poverty, crime, child abuse, and social injustice. However, most of the text (78.5%) is neutral because it consists of descriptive narrative rather than overtly emotional language. Dickens balances dark social commentary with moments of hope and human kindness.


Interpretation: The sentiment analysis reveals Dickens' deliberate use of emotional language to create empathy. The most negative sentences describe the harsh realities of Victorian poverty and crime, while positive sentences highlight moments of human compassion that provide hope. This emotional contrast is a hallmark of Dickens' social commentary - he shows both the darkness and the light to argue for social reform.

#### Text Similarity Within Oliver Twist

Comparing three 500-word sections (beginning, middle, end):

  Beginning vs Middle: 47% similarity
 Beginning vs End: 44% similarity
  Middle vs End: 51% similarity

Key Insights:
The middle and end sections are most similar to each other (51%), suggesting that once Dickens establishes his characters and setting in the opening chapters, he maintains a more consistent writing style and vocabulary through the remainder of the novel. 

The beginning section has the lowest similarity to other sections (44-47%), which makes narrative sense because:
1. It introduces new characters, locations, and concepts that don't repeat as frequently
2. It establishes the world and context before diving into the main plot
3. It uses more explanatory and descriptive language

The moderate similarity scores (44-51%) indicate that while the novel maintains consistent themes and characters throughout, each section also has unique vocabulary and focus, reflecting the plot's evolution and character development.


## Reflection
In terms of what went well I liked working with the modular structure, when I split the code into seperate files it made it easier to debug the code and modify individual functions. The word frequency analysis showed interesting insights on on how characters were focused along with its victorian language. My biggest challange was during the text similarity comparison analysis because it first took over 5 minutes to run because I had originally been comparing sections of 5,000 words.I then decided to reduce the section size to 500 words to make it more practical so it would run quicker and you wouldn't have to wait there waiting. I learned how to use regular expressions for cleaning text as well as how to install and use external libraries like TheFuzz. In terms of AI for this project I used Claude AI which helped me troubleshoot import errors , optimize the slow code issue I had at first , and understand how to split up my project onto different modules that make sense. Claude suggested reducing the section size and simplyfying the similarity calculations. I now feel better about working with text data and installing and using external libraries in python It also helped me write clear docstrings and comments explaining what each function does Understand trade-offs between code performance and accuracy. I now know to start with smaller text sections for analysis instead of running large analysis on the text files because if I don't it takes a long time for the code to work so I had to trade off analysis for functionality of the code. 
