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

## Reflection
In terms of what went well I liked working with the modular structure, when I split the code into seperate files it made it easier to debug the code and modify individual functions. The word frequency analysis showed interesting insights on on how characters were focused along with its victorian language. My biggest challange was during the text similarity comparison analysis because it first took over 5 minutes to run because I had originally been comparing sections of 5,000 words.I then decided to reduce the section size to 500 words to make it more practical so it would run quicker and you wouldn't have to wait there waiting. I learned how to use regular expressions for cleaning text as well as how to install and use external libraries like TheFuzz. In terms of AI for this project I used Claude AI which helped me troubleshoot import errors , optimize the slow code issue I had at first , and understand how to split up my project onto different modules that make sense. Claude suggested reducing the section size and simplyfying the similarity calculations. I now feel better about working with text data and installing and using external libraries in python. I now know to start with smaller text sections for analysis instead of running large analysis on the text files because if I don't it takes a long time for the code to work so I had to trade off analysis for functionality of the code. 
