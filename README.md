# Text-Analysis-Project

Please read the [instructions](instructions.md).


**1. Project Overview** (~1 paragraph)
In Assignment #2, the data source I chose was Project Gutenberg. In order to perform accurate text analysis, I first downloaded the eBook of The Great Gatsby By: F. Scott Fitzgerald and then later on, when choosing Text Similarity analysis as an additional step that intrigued me, I downloaded a second eBook of The Adventures of Tom Sawyer By: Mark Twain, both from the Project Gutenberg website. Prior to the Text Similarity analysis, I conducted Characterizing By Word Frequencies - where I focused on creating a code that could easily identify the number of times (frequency) a particular word appears in a given section of The Great Gatsby text: The user for example could input one sentence or a couple of lines from the text, and the result given would be the designated words and its frequency of occurrence. Additionally, in terms of Computing Summary Statistics analysis, I focused on figuring out the Top 10 Words that appeared the most frequently in The Great Gatsby text, and in the process I aimed to remove some stopwords for more niched results. Lastly, for Text Similarity analysis, I wanted to understand if both texts had a similarly high word count for a particular word, thus, using the cosine similarity method, once both eBooks were examined with the corresponding code, a cosine similarity decimal value was created to display textual similarity. Through this project, I was interested in learning to dive deeper into numeric textual analysis, and I found that by applying the above methods, to write code for successful implementation of the chosen methods to be very fascinating! Especially amongst two books that are up there as my favourites!

**2. Implementation** (~1-2 paragraphs)
Amongst all chosen methodologies, a common major component for code functionalities was ensuring that the eBook texts were appropriately downloaded to Python, and that it was cleaned and processed to ensure more efficient reading for the reader - skipping the Gutenberg headers, finding the starting marker point of the books as well as the end point, and the premables: table of contents & more. This sole component helped to set up the accuracy of organization of the analytical results when starting implementation of chosen methods. After this preliminary step, within Characterizing By Word Frequencies, Computing Summary Statistics, and Text Similarity techniques, new functions and empty dictionaries were created to store corresponding datapoints, these datapoints were sorted in descending order, and helped to present data that was required efficiently and effectively. After the codes for the techniques were complete, the code was always then tested to ensure its accuracy, starting with the: if__name__ = "__main__": the functions were always called back and the results were then printed. In the Text Similarity technique, I needed help with conducting Cosine Similarity to display the textual similarity between both chosen eBook texts, therefore I used GenAI for help in the final part of the code, my comments in the code clearly explain its funcionalities. Stemming from the Cosine Similarity equation, where to get the result the dot product of two vectors would need to be divided by the product of their magnitudes (lengths), I knew how to calculate it, but needed guidance in writing the code, below is the prompt I wrote (after 24 hours, the page reloaded so I couldn't get a screenshot, but I remember the prompt given below). This was only the big use of GenAI for this assignment:

"Hi! You are an expert in Python. I have downloaded two eBook texts: The Great Gatsby and The Adventures of Tom Sawyer. I am currently conducting Text Analysis and need guidance in completing Cosine Similarity to conduct it. Using basic Python fundamentals, can you help with the corresponding code? 
Here is the code I have so far: (gave it the code I wrote which was up until removing the stopwords before conducting Cosine Similarity) - use it as reference, don't change it please! (as the code I was using had the same aspects of the successful code from the previous two techniques, therefore I knew it was working).

From here, I got the resulting code written in the part_2b_and_2c.py file. 

One design decision in regards to all the methods that I chose to do, was utilize tuples for the results (words, frequency) instead of lists, as I wanted the results to be concrete, final and immutable. This helped to store and present data better!

**3. Results** (~1-3 paragraphs + figures/examples)

***Characterizing By Word Frequencies***
Inputted text (quote from the book): In my younger and more vulnerable years my father gave me some advice " 
that I've been turning over in my mind ever since.

Total words: 23
Unique words: 20

Word Frequencies:
my: 3
in: 2
younger: 1
and: 1
more: 1
vulnerable: 1
years: 1
father: 1
gave: 1
me: 1
some: 1
advice: 1
that: 1
i've: 1
been: 1
turning: 1
over: 1
mind: 1
ever: 1
since: 1

It was great to see the code functioning well! By adding two sentences, I was able to get the corresponding words and its frequencies, thus allowing it to work potentially for larger sections! However using the Computing Summary Statistics code could be much better for larger sections, to see the Top 10 Most Frequent words used in the section, instead of getting all individual words and their frequencies! For small data, the code for Characterizing By Word Frequencies would work for baseline understanding of Word Frequency! 

***Computing Summary Statistics***
Top 10 Most Frequent Words In The Great Gatsby
the: 2544
and: 1566
a: 1442
of: 1224
to: 1198
i: 1000
in: 850
he: 771
was: 762
that: 566

Even though I had tried to remove some common stopwords, the majority of the Top 10 Most Frequent Words In The Great Gatsby are to an extent, stopwords. 
Maybe next time, an additional method used could be Natural Language Processing, to understand the sentiment behind the words, and their affiliations in sentences, were these words used majorly positively or negatively? That could have been another consideration! However, to get the Top 10 Most Frequent Words, this code runs and garners results effectively! 

***Text Similarity***
Cosine Similarity between The Great Gatsby and Tom Sawyer: 0.4108

From this Cosine Similarity metric, it can be stated that there is a moderate similarity between the two novels. The score of 0.41 potentially suggests that both novels have some similar thematic or stylistic elements, such as overlapping messages (societal critique - The Great Gatsby and adventure/individualism - Tom Sawyer), however are completely distinct in narrative focus, cultural context, setting and tone. Thus, Text Similarity Analysis can be a great metric for building similar genred book lists or recommendations, and can be useful for creating personalized reading schedules!

**4. Reflection** (~1-2 paragraphs)
From a process point of view, I am quite happy that I was able to step by step, picture the approach to take to effectively conduct text analysis methodologies. I felt that I was able to accurately take knowledge and examples from class and apply it to my own forms of data, to curate new exciting results. There were fewer times where I ran into issues, which I see personally as a good improvement, as my understanding of coding is increasing in proficiency! In the times where I already applied personal debugging strategies and still needed guidance, GenAI was a great tool for assistance, which I used as a reference to modify my code for better funcionality. When I prompt AI to help with a task, (ex: debugging), I talk to it as if it is a learning buddy, as a mentor for me. By practicing my skills in Python in after-class exercises and assignments such as #1 and now #2, I feel that my interactive skills with AI has also improved, where I can follow and talk to AI with a better understanding, using it as a good resource for learning when required, stretching my knowledge. I had tried to attempt Text Clustering analysis between both my eBook texts, however was running into lots of issues. If I had slightly more time, I would have looked into it! Maybe outside of class I can come back to this and try it once again to learn further, or even ask GenAI and analyze its process when approaching this type of text analysis. Overall, I felt my project was well thought out and scoped, moving forward, in terms of learnings and takeaways from this project, I can apply the same methodologies to do my own forms of data analysis and textual analysis to identify patterns and draw my own conclusions from real world events (ex: in finance & more). Thus, this project has allowed me to merge my skills and interest in technology (coding) with my interest in business! 
