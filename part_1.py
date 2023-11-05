### This is a Product Management Teardown of the Game Pokemon Go ###

# import urllib.request
# import json

###   PART 1   ###
import pprint
from thefuzz import fuzz


from mediawiki import MediaWiki

wikipedia = MediaWiki()
poke = wikipedia.page("Pokémon Go")
# print(poke.title)
# print(poke.content)

from newspaper import Article

url = 'https://bulbapedia.bulbagarden.net/wiki/List_of_glitches_(GO)'
article = Article(url)
article.download()
article.parse()
article_text = article.text
# print(article_text) 

###   PART 2   ###


from nltk.sentiment.vader import SentimentIntensityAnalyzer
sentence = poke.content
score = SentimentIntensityAnalyzer().polarity_scores(sentence)
print(score)



import pickle

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

# The purpose of the following lines are to effectively sift through the Bulbapedia website to put just the names of all the Pokemon Go glitches in a dictionary.
# WHY are we doing this, you may ask? Well, later, I plan to check each glitch name w/ wikipedia to see if a certain glitch also appears on a broad website like Wiki.
    # If so, that will tell me that the glitch must be one of extra importance, and that I should focus specficially on those types of glitches in my analysis. 
list_store = []
list_divide = []
list_glitch = {}
f1 = open('poke_glitch.pickle')
for line in f1:
    list_store = line.split(' ')
    # list_divide.append(line.split(' '))
    if 'list of glitch' in line.lower():
            continue
    elif len(list_store) < 10:
        for i in range(len(list_store)):
            if 'glitch' in list_store[i] or 'bug' in list_store[i]:
                # if 'glitch' in list_divide[len(list_divide)-1] or 'bug' in list_divide[len(list_divide)-1]:
                list_glitch[line.strip('\n')] = 0
    list_store.clear()
    # list_divide.clear()
pprint.pprint(list_glitch)

print()
print()
print()


list_header = {}
f2 = open('poke_wiki.pickle')
for line1 in f2:
    if '==' in line1 and ' ' in line1:
        list_header[line1.strip(' ==\n')] = ''
# pprint.pprint(list_header)


print()
print()
print()


check_var = False
f3 = open('poke_wiki.pickle')
for line2 in f3:
    if '=' in line2 and ('Criticism and incidents' in line2 or 'Technical issues' in line2):
        check_var = True
    elif check_var == True:
        if '=' in line2:
            check_var = False
        else:
            for k in list_glitch:
                list_glitch[k] += fuzz.ratio(k, line2)
# pprint.pprint(list_glitch)

#Now, to order in the similarity #'s in anew dictionary, in ascending order:
max = 0
glitch_dict = {}
list_sort = []
for m in list_glitch:
    list_sort.append(list_glitch[m])
list_sort.sort()
# print(list_sort)

for a in range(len(list_sort)):
    for z in list_glitch:
        if list_glitch[z] == list_sort[a]:
            glitch_dict[list_glitch[z]] = z
pprint.pprint(glitch_dict)

# I would then go on to look more into the top x-amount (x is subjective) of glitches, and do deeper research into those.




