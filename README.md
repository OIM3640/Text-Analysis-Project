# Text-Analysis-Project

Please read the [instructions](instructions.md).

1. Project Overview (1 paragraph)

As an avid reader and literature lover, I decided to choose Project Gutenberg as my source. While browsing throught the titles, I settled on the following books:
    - A Tale of Two Cities by Charles Dickens
    - The Great Gatsby by F. Scott Fitzgerald
    - The Hound of the Baskervilles by Arthur Conan Doyle
    - Little Women by Louisa May Alcott
    - Peter Pan by J.M. Barrie

My goal was to create a short text by combining words from each piece of literature, which I accomplished in the "combining-texts" file. 
In addition to implementing Markov Text Synthesis, I analysed the frequency of words for each text in the "word-frequences" file. And lastly, I summarised the statistics of the top ten words that appeared in each book.

2. Implementation (1-2 paragraphs)

The implementation aspec that I struggled with the most was for the Markov Text section because I had very little idea about how to implement it. However, since I knew what my end goal was (to create short texts from multiple stories), I created a basic coding outline and asked GenAI for more intricate details. In the "images" folder I have attached photos of my interactions with tools like ChatGPT, Claude, or Microsoft Copilot. 

There were several times where I had to reevaluate my code and thought processes because I would think "I'm making it more complicated than it needs to be." An instance of this is when I attempted to introduce punctuation in the "combining-texts" file, which made the output texts expremely confusing and unappealing. Throughout the project, I also consulted with resources from our class (ex: recordings), GitHub, and platforms like Stack Overflow.

3. Results (1-3 paragraphs + figures and examples)

I loved the results for Homework 2 because they were creative and analytical. For example, I loved reading the different, twenty-five word texts generated by Markov's Text Synthesis. What made them unique is that they were composed by characters, plots, and verbs of each book, which made them incredibly unique. Here are a few examples:

"your whole morning for nothing thought jo as she rang the bell half an hour later than usual and stood hot tired and dispirited surveying"

"cigarette was trembling suddenly she threw the cigarette and the burning match on the carpet “oh you want too much ” she cried to gatsby"

"of this and there s no reason you should all die of a surfeit because i ve been a fool cried amy wiping her eyes"

What is really interesting about these examples is that they read as normal stories. It is true that there are some grammatical errors, but their storyline is consistent. I also find it amusing when different eras interact. For example, A Tale of Two Cities is written with an older version of english, while The Great Gatsby is more modern, so the outputs are sometimes a mix of both versions. 

Meanwhile, for the Word Frequencies Analysis, it helped me realised how some words can have such a great impact and be used scarcely, and vice versa. For instance,the word "dust" is only used six times in the story, but it is a crucial aspect of the plot because it is what allows them to fly.

Regarding the Summary Statistics, the Top 10 words tended to be modal verbs (ex: could and would), character names, and the verb "said."


4. Reflection (1-2 paragraphs)

Overall, I really enjoyed this project because it allowed me to see how Python can be used for Data Analysis. Throughout the process I ran into a few issues, especially when coding the Summary Statistics and Combining Texts (Markov Test). I kept running into issues because I would not get the output that I wanted. In the case of the Summary Statistics, I would get a list of the whole ranking with every word included. It wasn't until I submitted it to Claude that the reason for this was because I hadn't deleted "print frequencies" from the Word Frequencies section. Meanwhile, for the Markov Test, I didn't have a clear understanding as to how to code it, but because I had a vision I wanted to implement, I was able to ask Microsoft Copilot for help. I provided the code I had developed, my request, and any special comments (ex: "please keep the coding language simple so I can understand it"). Thanks to consulting with AI I have a deeper understanding as to how Text Analysis works and how to interpret code that makes it possible.

Overall, I also experienced issues with the NLTK library because every time I attempted to download it, I kept getting a warning. Eventually, thanks to asking ChatGPT multiple times and rewatching class recordings, I got it to work. Although I struggled with certain concepts and invested a lot of time in debugging, my biggest takeaway from this project is that Python is really cool and versatile. Thanks to my project scope, my creative goal was never negatively influenced.