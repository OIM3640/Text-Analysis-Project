# Text-Analysis-Project

Please read the [instructions](instructions.md).

*1. Project Overview** (~1 paragraph)

This project explores the texts of The Iliad and The Odyssey, using Project Gutenberg as the data source. The goal is to analyze word frequencies, identify key themes, and compare linguistic patterns between the two texts. Techniques include word frequency analysis, stop-word removal, and relative frequency comparison. The project aims to highlight similarities and differences between these two classic works through computational text analysis.

**2. Implementation** (~1-2 paragraphs)

First, text data is retrieved from Project Gutenberg using Python’s urllib.request, as was shown in class, allowing for automated access to these sources. The raw content is then cleaned through a  function that removes introductory and closing boilerplate text, retaining only the main body for analysis, starting from a given string of text and ending for another given text, this was done because of the unlikely probability of select words being in the same sentence, while words can be repeated much more easily. Next, data cleaning is performed through tokenization, stop word removal, and lowercasing, with NLTK’s RegexpTokenizer removing punctuation and irrelevant content, making sure that only significant terms remain for analysis.

Word frequency analysis is conducted using dictionary-based structures, where each word’s count is recorded to calculate both total and unique words in each text. Comparative analysis between the two texts is accomplished through relative frequency calculations, identifying common words that hold thematic significance within each text. 
When trying to calculate the relative word that was most frequent in both textes (weighted relatively) ChatGPT was essential in understanding how to build said function. From there I tweaked and changed the code in order to better fit in my overall file. Additionalyl ChatGpt was useful when trying to clear examples or theories or ways to use code for my goal without directly impacting it but rather my understanding of it

Photos Below of the Conversation:

![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)


**3. Results** (~1-3 paragraphs + figures/examples)

The analysis revealed significant differences in vocabulary between The Iliad and The Odyssey, reflecting on the two different texts. The Iliad contained a total of 100,710 words, with 11,536 unique words, while The Odyssey had 52,468 words and 6,725 unique words. This variance highlights The Iliad's more extensive use of diverse vocabulary, likely due to its interpreation and wider emphasis on the breadth of topics and stories that it tackles

The most common words in The Iliad include "thy," "thus," and "shall," as well as names such as "Achilles" and "Hector," along with terms related to conflict like "war" and "arms." This vocabulary aligns with The Iliad's themes of warfare, heroism and its central heroes. Conversely, The Odyssey features "Ulysses" and "house" among its most frequent words, , as well as conversational terms like "said" and "went," which reflecting on the protagonist's interactions and his quest to go home.

To gain a deeper understanding of shared themes, I calculated the combined relative frequency of words common to both texts, identifying terms that are significant across both works. Words like "one" and "said" rank highly, underscoring universal themes of identity and dialogue. In The Odyssey, the prominence of "house" aligns with the narrative’s emphasis on homecoming, while The Iliad’s frequent use of words like "thy" and "shall" supports its formal and honor-driven focus.This comparison between high-frequency words in both texts underscores each work’s distinctive tone and thematic focus, with The Odyssey favoring journey and dialogue, and The Iliad emphasizing conflict and epic heroism.



**4. Reflection** (~1-2 paragraphs)

The project proved more challenging than expected, requiring substantial re-coding and restructuring, particularly in the data cleaning phase. A significant amount of time went into removing boilerplate text and refining the handling of stop words to ensure relevant data was retained for analysis. Managing these complexities involved rewriting functions multiple times to achieve accurate results, which highlighted the importance of thorough data preparation in text analysis. Despite the added difficulty, the iterative process improved the final outcome and deepened my understanding of effective data cleaning techniques.

GenAI tools were instrumental in refining my approach, particularly in structuring comparative analysis and learning efficient tokenization techniques, which helped streamline the code and optimize the frequency calculations. Knowing more about handling text length discrepancies in comparative analysis beforehand would have been helpful.