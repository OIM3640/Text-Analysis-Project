Part 3: Learning with AI 
I will talk about two problems I ran into while doing this assignment. The first problem I ran into was how to install nltk. The second problem was learning how to compare two pieces of text from the Gutenburg project. 

Problem one: While I was able to run my code before I forked the repository, 
I was not able to rerun the same code after I forked the repositoty. The code 
keep saying that no module named nltk was found. 

Crafted prompts 1: It took me three prompts to get to the solution. 
I first sent a screenshot of the error message I was getting which says
"no module nltk found", and asked copilot how to fix it. Copilot suggested that I install nltk using pip. I followed the 
the suggestion, and piped install nltk in the terminal. However, when 
I installed the package, I got a message that said "Requirement already satisfied".
I was very confused, so I sent another prompt asking "what could be wrong?"
if nltk was already installed. Copilot suggested that I checked my python
environment, and make sure that I was using the same environment where nltk was located. 
Copilot gave me an option to check my nltk installation by running "pip show nltk" 
in the terminal and check the location of the package in jupyter notebook by running 
import sysprint(sys.executable) and !{sys.executable} -m pip install nltk. The locations 
did not match. I decided to run the "python -m pip install nltk" in the console
instead of the terminal and that fixed the problem. 

Review and verify(1): Copilot gave me different options and 
I usually started with the simplest one first, usually the first or 
second suggestion. In this case, it takes three prompts to get to the solution. 

The process: Even though installing nltk does not seem hard, 
because it only takes one command to install it, not being able to get 
it to work was very confusing. Thankfully, copilot was able to guide me, giving 
me a different suggestions based on how I responded to the previous suggestions. 

Problem two: When comparing two pieces of texts from the Gutenburg prohect, 
I felt like my code was very repetitive and long. I somewhat have an idea on how 
to work with one text, but did not know how to extend the code to work with 
more than two texts or more without repeating the same code over and over again. 

Crafted prompts #2: 
1) I started by sending copilot my existing code that works with one text, 
and asked "how do I clean and process two texts at the same time?" 
2) While I was normalizing the unicode, I got an error message 
saying "an error occurred: invalid normalization form". I did not 
understand what I did wrong, so I asked chat how to fix the problem
including the screenshot of the error message. 
3) I asked copilot to help me choose a data visualization library 
so I compare the two texts visually using bar charts, but without using 
matplotlib. 
4) After choosing to visualize my data using ASCII bar charts, I also ask 
copilot interesting features I could add to my bar chart such as 
colors and titles. 
5) Another step I was interested in was sentiment analysis,
so I asked copilot how to do a sentiment analysis on Romeo and Juliet in addition to 
your guidance on how to install the necessary packages. 

Review and verify(2): 
1) Copilot suggested that I could create a function that takes in a text as 
input and returns the cleaned and processed text. I know we covered this in
class, so I incorporated the function into my code. It made my code so much more 
concise and easier to read. 
2) Copilot pointed out that I made a type in the normalization 
form, and suggested that I change "NFDK" to "NFKD. After this step, my code works fine.
3) Copilot suggested that I could use seaborn, plotly, or ASCCI bar chart terminal. Looking at the options with the sample code for each one, I decided to go with 
ASCII bar chart, since I do not have to install any additional packages and the visualization seems interesting and simple.
4) Copilot suggested I printed the title of the chart above 
my bar chart, which I thought was a good idea and it made my visualization look more complete. 
5) With the code ChatGPT provided, I tweaked it a little bit by not using the dictionary to store the sentiment scores, but printing them directly. 
