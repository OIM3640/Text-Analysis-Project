#PART 3 AND 4
For thir project I worked with text data from Project Gutenberg, using Oliver Twist by Charles Dickens as my main source. My goal was to practice text cleaning, processing, and basic analysis (as required by the homework assignment), and see what kind of insights I could pull from a long public-domain novel. I als learnt how to structure a Python project that feels real, with separate files for different tasks, instead of one big messy notebook. 
I organized everythiing into small, modular scripts because when I was coding everything in the main.py file, whenever I got an error I wasnt able to track what part of my code was not working. The division of scripts is as follows:
    fetch.py- downloads the text from Project Gutenberg. 
    clean.py-handles the cleaning, removing extra spaces, headers, and stop words. 
    analyze.py-calculates word frequencies, top words, and basic stats like average sentence length. 
    viz.py prints a simple ASCII bar chart right in the terminal so I can actually see the most common words.
Main.py ties it all together and run the full pipeline from start to finish. 

I had to make one design choice about whether to include the optional sentiment analysis step with NLTK. 
It caused environment issues and even ChatGPT wasn't able to help me with my errors, plus as professor mentioned it was optional, and it wasnt essential to the end project goal, so I left it out. 

ChatGPT was helpful in some places, and unhelpful in some. When I was confused with how to rearrange my main.py and divide it into different python files, I used chat to tell me exactly how to divide it and what would be the purpose of each file. However, when I wanted to know how to why my optional_sentiment wasn't working, I hated ChatGPT because not only did it not tell me what was wrong, it told me errors in my main.py and viz.py that did not exist. I had to go back and redo all my code. 

After cleaning the text, my program processed over 930k characaters from Olier Twist. The analysis printed the Top 20 most frequent words, where "said," "mr," and "which" dominated the list, which did not surprise me for a dialogue heavy book. The ASCII bar chart in the terminal made it easy to see frequency patterns visually. AI also helped me store my data neatly in the data/processed, and data/results folder. 

The hardest part was getting everything to connect smoothl, imports between files, directory paths, and figuring out why 'fetch' would not load at first. 
Once I fixed those, running the whole thing and seeing atctual results felt AMAZING. The most frustating part was redoing the code over and over again till it worked. I feel like I know the book Oliver Twist in and out without having read it. 

From a learning perspective, I'm walking away much more confident with text analysis and file handling in Python. The AI part was like a patient tutor who explained what my errors meant. If I had to redo this project then I would ask all students to submit a list of the texts that we were analyzing so that no two students clean the same text. That way, we can get access to different clean texts for further projects. 