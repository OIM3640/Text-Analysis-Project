# Note: All evidence has been added to the repository with the naming convention (Image_#).

# Text-Analysis-Project
1. Project Overview: 

My goal that I aimed to achieve via the implementation of the "Text-Analysis Project" was to find out the frequency of drama films that are the top-rated films of all time. This prompt was derived from my hobby of watching films throughout my childhood and deciphering that films under the 'drama' genre tend to be rated very highly. Thus, using the .get function as well as the "counter" function, not only was I able to find the number of drama films in the top 250 films of all time, but I was also able to create a frequency diagram for their respective release dates. As suggested by the repository's instructions, I performed this via the API "Cinemagoer." 

2. Implementation:

In order to first decipher this trend, the first objective of my code was to create an API key that could create a list of the top 250 films of all time. In this list, not only was I able to find the names of these films, but their basic information such as release dates, genres, and titles were all found and filtered into a list for future references. This list was called "top_movies". 

After this list was created, I created filters using the a for loop and if functions to find all the movies that were under the 'drama' genre. If a movie was to fall under the 'drama' genre in the top 250 movies of all time, a sublist called "drama_movies" was created with all the basic information stated above. This my curated list was not only curated but also extarcted for frequency analysis (found in the analysis.py file). Furthermore, AI advised me to create error handeling code that would output a print statement if mistakes were made during the code creation process. This small step signficantly aided me during this project as these print statement essentially created breaks in my code for debugging.

AI was further able to showcase its importance during my prelimary research phase as it was able to point out that Cinemagoer did not allow users to filter movies by just the genre alone. Instead, a list must be created by an alternate deciding factor and thus my decision was to undertake the top 250 movies and filter them accordingly. This can be seen via Image_1 (added to the same repository) which showcases the prompt provided by ChatGPT. Furthermore, AI was able to effectively conlude that my methodlogy for Cinemagoer was the most efficient without the use of JSON (Image_2, Image_3, Image_4). As seen from Image_6, the best methodology was found using the table where in the most efficient yet detailed method was found. 

3. Results (Note: Image_5 is the final frequency diagram derived from both .py files): 

Overall, via the use of my aforementioned methodology, not only did I gain insight into the frequency of dramas that were on the top 250 movies of all time. But I was able to gauge the years in which these movies released. From Image_4, it is evident that most of widely-acclaimed films of all time tended to be released pre-2000. Furthermore, most of these films tended to revolve around major historical events such as Schindler's list or 12 Angry men. Overall, it was certain that archaic form of filmography combined with the use of historical plot progression were common recipes to create popular films. 

Lastly, it was also observed that almost none of the films in drama_movies were created in the past decade. This could hint that the modern style of filmaking was popular (i.e box office revenue) but it was not widley acclaimed in terms of Imdb ratings. This could hint that current directors aim to cater to modern audiences' tendencies such as shorter duration films with less plot progression. 

4. Reflection:
Overall, it is certain that one of the decisions that I made at the start of the project ensured that not only was my methodolgy efficient, but the prompt could be answered using the tools taught during the course. More specifically, my decision to first curate the top 250 movies of all time and then filter the subsequent data aided not only my code creation but also trouble shooting during the process. 

Additionally, I believe that using AI for troubleshooting greatly aided my work flow as it ensured that not only was I able to fix minute mistakes, but errors such as an outdated version of Cinemagoer was averted. This in turn ensured that I was able to constant develop and create an efficient code that could run for different genres without major modifications. 

Overall, after the completion of the "Text-Analysis Project" there were some major takeaways that can be implemented for the future of this course. One key takeaway was how to use AI for trouble shooting. Before, it was observed that I tended to use AI for code development and creation when I was unable to develop the code individually. However, via this project, I came to the conlusion that GenAI tools such as copilot and chatgpt were very good and finding minute mistakes and fixing formatting issues. This features not only ensured that my code could be translated to different softwares (for example using both copilot and chatgpt), but it allowed me to coherently identifying the minute mistakes that would be repeatedly used during my codes. Not only was I unaware of these mistakes in the past, but I would keep using them throughout the course which would further hinder my progress. It can be concluded that my methodologies used in this project have aided me in create a concrete procedure whenever I use python to solve my problems or address prompts during the rest of the course. 

# Note: 
extraction.py aims to curate the all the movies in the top 250 movies of all time that fall under the genre of drama. final_project.py aims to use extraction.py to create a frequency diagram of these films in relation to their release date. 
