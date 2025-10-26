# Text-Analysis-Project

Please read the [instructions](instructions.md).

Project Overview
    I decided to use the histograms and Project Gutenburg to analyze and reak down two books. The books being East of Eden and The Great Gatsby. I also decided to look into movie reviews for the same books. I was hoping to learn more about API and data mining. I was also curios on looking into two of my favorite books

Implementation
    The first part of my code loads and downloads the books into text and creates a list of stop words which I will use for data mininig. I then created historgrams and see which words appear the most (excluding stop words). This all fits togeher as i can compare the books and furhter analyze them such as which words are used in each book I also pickled my data by trying to add the texts to one list. This allowed my to have the two texts in one code.

    The next part of my code was the movie reviews but I could not get it to work. I have used AI to fix my code and ask for inut, howver, AI beleives it is a library error. I also experimented with the OPen AI API but faced challenges with API authentication. I asked AI to see where the issue was and since it was my key. It asked me to implement my key to a .emv dile on gitignore. Then import the libraries. After importing these, my key was working.

Results
    Some of my results are the top twenty words from each book
The top 20 words in East of Eden are:

eva: 463  
us: 203   
“i: 193   
over: 192 
might: 188
did: 187  
know: 169 
like: 163 
see: 163  
van: 162  
your: 154
must: 154
eyes: 147
never: 143
nicholas: 142
because: 142
work: 139
down: 139
say: 138

The top 20 words in The Great Gatsby are:
gatsby: 189
“i: 175
tom: 173
daisy: 143
over: 141
like: 118
down: 118
came: 108
back: 108
man: 105
any: 102
little: 102
know: 96
just: 94
house: 92
before: 91
now: 91
went: 91
after: 86

I also have a MDS scatterplot that shows the correlation of 5 chunchs for the two books. I used fuzzy to show the similarities from 0 to 1where 0 is no correlatoin and 1 is exactly the same. This is the graph
![alt text](image.png)
![alt text](image-4.png)
For the pickling, I was able to see the two books into one code Howver, I orginilnally did not have the list, so i asked AI to walk me thorugh the list. Then, fix my errors. Here is some inputs
![alt text](image-1.png)
![alt text](image-2.png)

I also used Claude AI for making sure my code is correct since I did try to implement extra steps. However this was more complicated. Here, i asked Claude to help me with the movie reviews before messaging proffesor
![alt text](image-3.png)

Reflection
    From my point of view, there were a lot of things that went well, such as extracting and getting the books into a histogram, however, some things did not go the way I expected. My first issue was trying to remove the punctuations and spaces and special characters. I asked Ai for this but got something complicated, So i decedd to look for a simpler solution. I also asked my brother to assit me and looking over my code and giving me suggestions. Howeverm his feedback was outside my knowledge learned in OIM 3640
    Another big challenge was understanding the structure of the Cinemagoer. I orignially did not want to look into movies as I was already having problems in Part 1. However, I wanted to challenge myself and get a sense of accomplishment by going over the movies of the two books. One thing I learned was properly using the .get function with default values to prevent crashes when keys were not present. I also wanted to try the NPL with the charts. This was very sucessful after I learned how to merge a list into a dictionary and then pickle.  I do beleive my project was scoped to a small extent as it was simple and effective. I did not feel too comfortable doing something complex. My testing plan was commenting out parts of my code and then running what I had. 
    My biggest Takeaway was learning how to process and analyze text data into NPL. I also learned how to tokenize and extract specific data such as stop words. I also learned how to organize text to create dictionaries andreveal patterns such as similar words. The biggest thing however, was learning about each external resrouces and how to handle such as Reddit and Cinemagoer libraries. Going forward, I will use more NPL techniques and try to get developer accounts for reddit and twitter. I will also try to compare the book and movies to each otehr rather than the two books to each other. I wish I studied more and looked over the JSOn files and started earlier