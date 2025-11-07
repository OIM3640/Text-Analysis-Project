# Text-Analysis-Project

Please read the [instructions](instructions.md).

# Part 4: Project Writeup and Reflection  

## 1. Project Overview  
For my text analysis project, I used **Jane Eyre** by Charlotte Brontë from **Project Gutenberg** as the main dataset. I explored the text using several computational techniques including text cleaning, stop-word removal, word-frequency analysis, ASCII visualization, Markov analysis to generate new text based on learned word transitions，and sentiment analysis to analyze sentiment of a text. 
The purpose of this project was to learn how to handle and analyze large text data step by step using fundamental Python logic from Think Python. I wanted to see how coding techniques like loops, conditionals, and dictionaries could reveal patterns in word use and emotional tone in literature. Through this process, I hoped to gain a deeper understanding of both text analysis and the emotional structure of Jane Eyre using only my own code and logic.

---

## 2. Implementation  
The project was divided into several parts that work together.
First part, the text file (jane_eyre.txt) was downloaded directly from the site and saved locally. I used Python’s built-in open() function with UTF-8 encoding to read the file line by line.
This part is to clean the data part, the `read_data()` and `clean_text()` functions prepare the text by reading lines, removing control characters, punctuation, and converting everything to lowercase to better prepare with text analysis.Then, the cleaned text is tokenized into words, and stop words are removed using a manually built stop-word list and simple list loops. This is what we learned in class and in thinkpython.  

The next part is to build analysis part. I first creates a **word-frequency dictionary** that counts how often each word appears and displays the top results through an **ASCII bar chart**. The frequency data was used to calculate summary statistics like total words, unique words, and vocabulary richness. For advanced analysis, i chose **Markov text synthesis** which is bigram model. it helps building a mapping from prefix (tuple of two words) to build list of possible next words; generate by repeatedly sampling and shifting the prefix window. For the optional exploration, I implemented a **sentiment analysis** module using a small manually defined sentiment lexicon (`SENT_LEX`) and a **rolling mean function** to observe trends in emotional tone throughout the novel.  

A key design decision was choosing between using external libraries like `nltk` or writing my own functions with only built-in tools. I decided to code all parts manually (loops, regex, dictionaries) to deepen my understanding of the logic behind text analysis instead of relying on pre-built sentiment models.  

Throughout the project, I used ChatGPT to clarify Python logic and debug problems and also learn how to write some code. I pasted code errors into ChatGPT to ask why my functions didn’t print results, how to normalize ASCII chart lengths, and how to handle negations in sentiment analysis. The chats helped me break large problems into smaller steps and understand each part before testing.   (see more in part3 ai_write up)
#https://chatgpt.com/share/690e2452-6088-8013-81c5-a30cefefaab2
#https://chatgpt.com/share/690cf8a6-2e18-8013-a696-76f9fb747bf6


---

## 3. Results  
For words summary staistic after cleaning and process the data, I found out that 12,635 words were unique, resulting in a vocabulary richness of 0.1378, meaning roughly one in seven words in the text is unique. The average word length was approximately 5.77 characters, which reflects the novel’s formal Victorian writing style and tendency toward longer words.

For analysis part i found out most frequent words are " now, will, one, said, s, mr, like, rochester, jane, well" , this make sense because "said,” “Mr.,” “Jane,” and “Rochester” reflect frequent dialogue and direct address between the novel’s two main characters, while words like “now,” “will,” and “well” indicate a focus on reflection and emotion, which aligns with the novel’s introspective tone. The **ASCII word-frequency bar chart** successfully helped tp  the top 20 most common words in the novel, showing that emotional words appeared repeatedly. 
The **sentiment analysis** found a **total sentiment score of 1353** with an **average of 0.122 per sentence**, meaning the novel had a slightly positive tone overall.  and i learned that the relative sentiment distribution captured the general balance between emotionally charged and neutral passages. Sentences expressing affection, admiration, or gratitude tended to receive the highest scores. For instance, "My Edward and I, then, are happy.”,  while sentences involving conflict or despair scored lowest, like “A cankering evil sat at my heart and drained my happiness.”
In addition, using a bigram-based Markov model, I generated new sentences that mimicked Jane Eyre’s writing style by predicting each word based on its preceding pair. The output captured common transitions such as “Mr. Rochester” and “said Jane,” reflecting the novel’s dialogue-heavy and emotional tone.This shows that Markov analysis can reproduce the surface rhythm and vocabulary patterns of a literary text without requiring deep linguistic understanding. 

##. Reflection 
From a process point of view, one of the biggest challenges was figuring out how to get started and designing each function from scratch. In the beginning, I found it hard to understand how to clean text data properly and connect all the functions together,  from reading and cleaning the text to building dictionaries and calculating word frequencies. To overcome this, I brainstormed each function’s role with the help of ChatGPT, breaking the large project into smaller parts such as read_data(), clean_text(), stopwords(), and dictionary(). Like i ask chatgpt to breakdown each projects to small steps. 

Another challenge was debugging. Sometimes my output looked empty, or the ASCII bar chart didn’t display correctly. By testing each function step by step and checking small text samples, I learned how to verify data at every stage before combining them into the full pipeline. The sentiment analysis part was also complex at first; I had to learn how negations worked. Then i will ask ai to explain each code in simple words and if it write a complex one, i will tell him to code concept from thinkpython. 

What went well was that once I had the core data cleaning and counting logic working, I could expand easily. It has same logic, both using for loop and add some tweaks.  In addition, i learned adding Markov analysis and sentiment scoring as new modules. I ask chatgpt to explain those two advanced analysis concepts and learned from start how to do it, ask chat to explain each code. If I could improve one thing, I would expand the sentiment analysis by adding a more detailed lexicon and visualizing emotional trends across chapters to make results clearer. I would also refine my Markov model to generate longer, more coherent sentences that better reflect the novel’s tone.

From a learning perspective, this project helped me connect everything I’ve learned from Think Python into a real applied task, like using loops, conditionals, dictionaries, and string operations to analyze a full-length novel. My biggest takeaway is to actually practice the code we learned in class in real life. Another key takeaway was learning how basic functions I wrote for cleaning, counting, and filtering words could later be reused to build more advanced analyses like sentiment scoring and Markov text generation. Also project was appropriately scoped because it focused on one large text and applied progressively more advanced analysis methods without relying on external datasets or libraries. I kept the workflow simple enough to test each function separately, first checking text cleaning, then word counts, and finally sentiment and Markov generation. My testing plan involved printing intermediate outputs to verify each step worked correctly before moving to the next stage.

AI tools like ChatGPT played a major role in helping me clarify difficult logic and learn new methods. I asked questions such as how to remove control characters with unicodedata.category(), how to handle punctuation, and how to build my own sentiment lexicon. ChatGPT also helped me rewrite and simplify my code, making it more readable while explaining the reasoning behind each step. It also explain code pretty well, which help me understand what each code does. 

Going forward, I will use what I learned to build more advanced text-analysis projects and perhaps incorporating visualization libraries or real world datasets. I now feel confident that I can design full analysis pipelines from raw text to summary statistics, and I better understand how AI assistance can guide learning without replacing critical thinking or testing.