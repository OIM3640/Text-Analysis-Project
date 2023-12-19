# Text-Analysis-Project
 
## Project Overview:
    For this project, I used wikipedia and an article as data sources. To process and analyze both sources, I used techniques, including filtering by word or symbol and checking for text similarity. Through this project, I hoped to create a process that would allow me to easily analyze information, in way by which I can prioritize the important aspects to cover. In terms of what I hoped to learn through this project: I would hope to effectively utilize python to sift through large sets of data and text to only take out the most important insights.

## Implementation:
    At a basic level, here are my steps:
    1. import wiki and bulbapedia sources 
    2. Convert them into .pickle text sources to draw from later.
    3. Utilized a nuanced for-loop to fill a dictionary with the names of the game glitch/bugs ---> as keys, with the output automatically set to 0 --> will see why soon
    4. Utilized a nuanced for-loop to organize all the headers in the Pokemon Go Wikipedia Page --> into dictionary keys.
    5. Selectively choose two headers related to game glitch/bugs, and ran fuzz tests on the glitch names we found on bulbapedia, vs the broad wikipedia text of those specific sections.
       1. The scores would then replace the original pre-set value of 0 in the dictionary w/ the glitch names
    6. I would then create a list that would store all the scores, in ascending order
    7. Finally, I would create a dictionary w/ the score as the key, going in ascending order, and the glitch/bug name as the output for each key.

    In terms of other alternative strategies:

    I was considering using the following strtagey from the json example:

    with urllib.request.urlopen(url) as f:
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)

    I just wanted to store the whole text, but I stuck to the pickle method, as the json method wouldn't be condusive, as there's nothing to decode in Wikipedia or Bulbapedia, and I also can't go line by line to analyze the text.

ChatGPT:

    The error message you're seeing, "TypeError: write() argument must be str, not bytes," is occurring because you're trying to open the file 'poke_glitch.pickle' in text mode ('r' for read), but it appears that the file was written in binary mode. In Python, when you open a file in text mode ('r'), the data read from the file is expected to be in string format, but if the file was written in binary mode, you should open it in binary mode ('rb') to correctly read the data.

Here's how you can modify your code to open the file in binary mode and load the data using the 'rb' mode:

```python
import pickle

with open('poke_glitch.pickle', 'rb') as g:
    reloaded_copy_of_texts1 = pickle.load(g)
```

By using 'rb' mode, you will be able to correctly read the binary data from the file and deserialize it using `pickle.load()`.
    ![Alt text](image.png)

## Results:
    Through my text analysis, I was able to find the most prevalent glitches/bugs in Pokemon Go. 

    Ex Outputs [Similarity#: 'Name of glitch']:
    49: 'Ditto background glitch',
    50: 'Too far PokÃ©mon glitch',
    51: 'Special Attack usage bug',
    53: 'Disappearing PokÃ©mon glitch',
    58: 'PokÃ©mon model merging glitch',
    63: 'Shadow PokÃ©mon purifying glitch',
    67: 'Raid Boss last Premier Ball glitch',
    79: 'No internet connection message glitch'

Purpose:
    I've always loved playing games of all kinds, and given this fact, I saw this project as a great opportunity to conduct a semi-game teardown, through utilizing code to collect prevalent glitches/bugs in the game of choice: Pokemon Go.

    But how do I select the most prevalent bugs?

    That's where my code comes in, and that's what makes it so cool! My code takes all specific glitches from an article from Bulbapedia, and checks those through a broad website like Wikipedia, to see out of all the glitches noted, which one does Wikipedia highlight the most (measured by fuzz score). 
    The top x amount, in terms of fuzz scores, are the most 'prevalent,' --- and are the glitches I would analyze in depth, if I were to do a full-on game 'teardown' of Pokemon Go.

## Reflection:
    From a process point of view, what went well, was me being able to choose data sources, which had noticeable patterns in how the information was delivered. Whether it be Wikipedia having '==' before and after each header, or bulbapedia having glitch/bug at the end of each issue --- that made it very convenient for me to effectively extract information from the pages to do my analysis. In terms of what I could've improved, I wish I would've been able to find a way to use reddit to conduct a more proper sentiment analysis. On another note, I truly believed that my project was approprietely scoped & planned, as I was able to use pprint.pprint statements to shpw my outputs as I go, and I was able to clearly progress in my data analysis from stage to stage.

    From a learning perspective, ChatGPT helped me in being able to solve a minor inconvenience that would've otherwise costed me hours of my time. When trying to put the data source into the .pickle, I got the following error: 
    
    typeerror: write() argument must be str, not bytes
    ChatGPT was able to find the simple, yet subtle solution to my issue, through giving the solution that infact worked.

    Pre ChatGPT:
        with open('poke_glitch.pickle','r') as g:

    After ChatGPT:
        with open('poke_glitch.pickle','rb') as g:
    
    What I really learned from this assignment was being able to effectively phrase my question in a way that gives ChatGPT enough info to give the best answer. I wish I knew of these learning techniques beforehand, as given my previous experience in Java, through taking AP Computer Science in high school, I essentially utilized my familiraity w/ Java to propel my Python learning. Obviously it's best to give your full effort to actually learn, but it's also best to be time-efficient, especially in the face of small, relatively minor coding issues.