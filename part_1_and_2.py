### This is a Semi Game Teardown of the Game Pokemon Go ###

    ## Goal: To find the top x prevalent glitch/bugs in the game: Pokemon Go.
    ## Methodology: 
        # Generating list of the various glitches & bugs encounter by users, throughout the history of the game's existence. 
        # Then browse select sections of the broad Pokemon Go Wikipedia Page, to gather which are the most noticeable glitch/bugs, based on the fuzz score.


###  IMPORT Statements  ###
import pprint
from thefuzz import fuzz


from mediawiki import MediaWiki
from newspaper import Article
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pickle

import praw
import config 


###   PART 1   ###

def part1():
    """The purpose of this part is to create a .pickle file for the wikipedia page for 
    Pokemon Go, and the Bulbapedia page containing the list and history of in-game glitches"""

    wikipedia = MediaWiki()
    poke = wikipedia.page("Pokémon Go")
    # print(poke.title)
    # print(poke.content)

    url = 'https://bulbapedia.bulbagarden.net/wiki/List_of_glitches_(GO)'
    article = Article(url)
    article.download()
    article.parse()
    article_text = article.text
    # print(article_text) 


    # Note BELOW: originally was: open('poke_wiki.pickle','w') as f:, but given the following error: "TypeError: write() argument must be str, not bytes," ChatGPT suggested putting 'wb' instead of 'w,' which worked!

    # Save data to a file (will be part of your data fetching script)
    with open('poke_wiki.pickle','wb') as f:
        pickle.dump(poke.content,f)

    # Load data from a file (will be part of your data processing script)
    with open('poke_wiki.pickle','rb') as f:
        reloaded_copy_of_texts = pickle.load(f)

    with open('poke_glitch.pickle', 'wb') as g:
        pickle.dump(article_text,g)
    
    with open('poke_glitch.pickle','rb') as g:
        reloaded_copy_of_texts1 = pickle.load(g)

###   END OF PART 1   ###


###   PART 2   ###

def part2():
    """The following code will analyze & process the text in 'poke_glitch.pickle,' and 'poke_wiki.pickle' 

    Processing:
    1. 'poke_glitch.pickle' will be used to create a dictionary of the various glitch/bugs in Pokemon Go
    2. 'poke_wiki.pickle' will be used to organize a dictionary of the headers of the Pokemon Go Wikipedia page.

    Analysis:
    1. Will scan the each glitch/bug stored as a key, against the specific Wiki sections related to issues with the Pokemon Go game, to see for what degree, is the glitch important enough to be present in a broad source, such as wikipedia.
        
        Importance will be measure by the overal fuzz score of each glitch term [higher fuzz = higher importance]
    """

    # The purpose of the following lines are to effectively sift through the Bulbapedia website to put just the names of all the Pokemon Go glitches into a dictionary, as the keys.
    # WHY are we doing this, you may ask? Well, later, I plan to check each glitch name w/ wikipedia to see if a certain glitch also appears on a broad website like Wiki.
        # If so, that will tell me that the glitch must be one of extra importance, and that I should focus specficially on those types of glitches in my analysis. 
    
    list_store = [] # list_store is for spliting a line, word by word, into a list
    list_glitch = {} # this is for storing the name of each glitch/bug, as a key.
    f1 = open('poke_glitch.pickle')
    for line in f1:
        list_store = line.split(' ')
        # Eliminate the header 
        if 'list of glitch' in line.lower():
                continue
        #name of glitch/bug header, on avg., should be less than 10 words --- so we check for this
        elif len(list_store) < 10:
            for i in range(len(list_store)):
                #checks to see if less-than-10-word-phrase has glitch or bug as a word
                if 'glitch' in list_store[i] or 'bug' in list_store[i]:
                    # only adds as key, if glitch or bug is the last word --> for consistency purposes
                    if 'glitch' in list_store[len(list_store)-1] or 'bug' in list_store[len(list_store)-1]:
                        list_glitch[line.strip('\n')] = 0
        # clears before analyzing next line of the text.
        list_store.clear()
    pprint.pprint(list_glitch)

    ###     SPACER     ###
    print()
    print()
    print()
    ###     SPACER     ###

    list_header = {} # this is for storeing the wikipedia headers as keys
    f2 = open('poke_wiki.pickle')
    for line1 in f2:
        # on avg, each wiki header has '==' and ' ' within it, so we check for those
        if '==' in line1 and ' ' in line1:
            # we strip the '==' and the '\n', to clean up the data.
            list_header[line1.strip(' ==\n')] = ''
    pprint.pprint(list_header)

    ###     SPACER     ###
    print()
    print()
    print()
    ###     SPACER     ###

    check_var = False # this is a reference variable to see if we hit the headers we are looking for.
    f3 = open('poke_wiki.pickle')
    for line2 in f3:
        # we go line by line to see if we get to the selectively chosen headers for our analysis
        if '=' in line2 and ('Criticism and incidents' in line2 or 'Technical issues' in line2):
            # set this true if so
            check_var = True
        elif check_var == True:
            # if true, we then look through the description under the header. 
            #We know the description under a certain section is over when the line has an '=' in it.
            if '=' in line2:
                # reset back to false as we look for next header
                check_var = False
            else:
                # for the description under the select wiki headers, we do fuzz analysis for each glitch/bug name to find general relevance.
                # why '+='? Well, we are looking through 2 sets of descriptions here, so we much consolidate the fuzz score for each, following the iteration through the first header description, through the other header description.
                for k in list_glitch:
                    list_glitch[k] += fuzz.ratio(k, line2)
    pprint.pprint(list_glitch)

    ###     SPACER     ###
    print()
    print()
    print()
    ###     SPACER     ###

    #Now, to order in the similarity #'s in anew dictionary, in ascending order:
  
    list_sort = [] # this list is for storing the fuzz scores, from lowest to highest
    for m in list_glitch:
        # first, we just add all the fuzz scores into the list
        list_sort.append(list_glitch[m])
    # we sort it afterwards
    list_sort.sort()
    print(list_sort)
    
    ###     SPACER     ###
    print()
    print()
    print()
    print('*** The BELOW will print out the dictionary with the ascending fuzz values ***')
    print()
    ###     SPACER     ###

    glitch_dict = {} # this is for storing the fuzz scores as keys (in ascending order), and the glitch/bug name, as the output
    for a in range(len(list_sort)):
        # refers to previous dictionary from before
        for z in list_glitch:
            if list_glitch[z] == list_sort[a]:
                #adds fuzz value from list as key if they match, which it eventually will.
                glitch_dict[list_glitch[z]] = z
    pprint.pprint(glitch_dict)

    # I would then go on to look more into the top x-amount (x is subjective) of glitches (has the highest total fuzz score/key-value), and do deeper research into those.

###   END OF PART 2   ###
def part3():
    # reddit = praw.Reddit(client_id=config.client_id,
    #                     client_secret=config.client_secret,
    #                     username=config.username,
    #                     password=config.password,
    #                     user_agent=config.user_agent)
    # sub = 'learnpython'
    # submissions = reddit.subreddit(sub).top('day', limit=5)
    # top5 = [(submission.title, submission.selftext) for submission in submissions]
    # print(top5)
    reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     username=config.username,
                     password=config.password,
                     user_agent=config.user_agent)

    sub = 'pokemongo'
    submissions = reddit.subreddit(sub)
    reddit.read_only = True
    # print(reddit.read_only)
    # print(submissions.description)
    for submission in submissions.controversial(limit=20):
        print(submission.title, submission.url)



def main():
    # part1()
    # part2()
    part3()



if __name__ == "__main__":
    main()


