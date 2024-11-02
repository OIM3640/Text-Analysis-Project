# Text Analysis Project

import urllib.request
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer 
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
import sys 
from unicodedata import category
from sklearn.feature_extraction.text import TfidfVectorizer

# Book of poems written by Emily Dickinson from www.gutenburg.org
emily_dickinson_poems=['https://www.gutenberg.org/cache/epub/2678/pg2678.txt','https://www.gutenberg.org/cache/epub/2679/pg2679.txt','https://www.gutenberg.org/cache/epub/12241/pg12241.txt']
# Imported links for series one, two, and three 

#File Download 

def downloadText(url_address):
    #Professor provided 
    #Ebook downloads from the url_address and returns it as a plain text file
    with urllib.request.urlopen(url_address) as f:
        text = f.read().decode('utf-8')
        return text 

def saveText(text, nfile):
    #Text content gets saved to the file named nfile
    f = open(nfile, "w")
    f.write(text)
    f.close()

def downloadBookList(booklist):
    #Download a list of ebooks (booklist) and save them each in a text file, file names -> book#.txt
    n = 1 
    for url in booklist: 
        t = downloadText(url)
        nfile = 'book'+str(n)+'.txt'
        saveText(t, nfile)
        n += 1

#Loading text from the files 

def loadText(filename): 
    #Return the text from the file 'name', or return None, meaning that the file does not exist
    text = ''
    fp = open(filename, encoding="utf-8")

    if True:
        skip_gutenberg_header(fp)
    for line in fp:
        if line.startswith("*** END OF THE PROJECT"):
            break     
        text += line
    fp.close()
    return text 

def skip_gutenberg_header(fp):
    start_marker = "START OF THE PROJECT"
    for line in fp: 
        if start_marker.lower() in line.lower():
            return
    raise ValueError(f"Header end marker '{start_marker}' not found in file.")

def cleanText(text):
    #Return a substring of 'text', substring return result removes header and footer
    #Specifying with strings, starting_mark and ending_mark, the ending of the header 
    #and the begining of the footer. 
    splittext = text.split('\n\n') #takes text body and splits it into a list
    poems = [] #List of poems of the text 
    poem = '' #Poem
    for i in range(len(splittext)): #Build a list of poem
        if splittext[i] == '' and len(poem)>0:
            poems.append(poem)
            poem = ''
        else:
            poem += splittext[i]
    return poems 

def loadAll(numfiles):      
    textslist = [] #list of texts containing list of poems 
    for i in range (1, numfiles+1):        
        t = loadText("book"+str(i)+".txt")
        if t is not None:
            textslist.append(cleanText(t))
    return textslist 

#Part 2
#Sentiment Analysis 

def sentimentNLTK(text):
    #Sentiment Analysis for text 
    #Return a disctionary 
    #neg: negative, neu: neurtral, pos: positive, compoung: general score, from negative (-1) to positive (1)
    result = SentimentIntensityAnalyzer().polarity_scores(text)
    return result

def sentimentNLTKforAll(books):
    #This method returns a 2Dimensional list with the sentiment analysis
    #of each poem for each book, using NLTK: result[book][poem]
    result = []
    for b in books: #for books 
        s = []
        for p in b: #for poems within books
            s.append(sentimentNLTK(p))
        result.append(s)
    return result 

def graphNLTKresults(s):
    n = 1 
    for i in s: 
        print(f"****** BOOK {n} ******")
        print(f"Total Poems: {len((s[n-1]))}")
        v = []
        for j in i: 
            #print (j)
            v.append(j["compound"])
        x = np.arange(len(v))
        y = np.array (v)
        if n == 1:
            plt.subplot(3,1,n).set_title("NLTK Result (average sentiment)")
        else: 
            plt.subplot (3,1,n)
        plt.plot(x,y)
        n += 1 
    plt.show()


#Metrics

def removeWords(text, list):
    #GenAi Method
    #Remove a list of words from text
    oldwords = text.split() #Converts text into a list of words
    newwords = [word for word in oldwords if word.lower()not in list] #Filtered words
    newtext = ' '.join(newwords) #Converts the list into text 
    return newtext

def wordsRelevanceTF_IDF(text):
    #Method adapted from GenAi GPT to analyze a list of texts
    #Creating the TF-IDF vectorizer 
    vectorizer = TfidfVectorizer()
    #Adjusting and transforming the documents 
    tfidf_matrix = vectorizer.fit_transform(text)
    #Getting the names of the word to measure 
    feature_names = vectorizer.get_feature_names_out()
    #Building the TF-IDF matrix in display format 
    dense = tfidf_matrix.todense()
    denselist = dense.tolist()
    #Showing the results 
    df = pd.DataFrame(denselist, columns=feature_names)
    print(df)

def wordsRelevanceTF_IDFforALL(lbooks, rwords):
    #Calculate the words relevance for each book
    n = 1 
    for b in lbooks:
        print(f"****** BOOK {n} ******")
        bb = []        
        for p in range(len(b)):
            bb.append(removeWords(b[p],rwords))
        wordsRelevanceTF_IDF(bb)
        n += 1

def convertToDic(book,rlist):
    #convert a list of text into a dictionary of word frequencies 
    hist = {}
    strippables = "".join(chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P"))
        #Unicode puntuation characters. Ref: https://stackoverflow.com/a/60983895
    for p in book:
        rp = removeWords(p,rlist)
        for word in rp.split():
            word = word.strip(strippables)
            word = word.lower()
            hist[word] = hist.get(word, 0) + 1
    return hist

def total_words(hist):
    """Returns the total of frequencies in a histogram"""
    # strippables = string.punctuation + string.whitespace
    return sum(hist.values())

def most_common(hist, excluding_stopwords=False):
    list = []
    for key, value in hist.items():
        list.append((key, value))
    return sorted(list, key=lambda x: x[1], reverse=True)

def metrics(lbooks,rlist):
    n = 1 
    for b in lbooks:
        histB = convertToDic(b,rlist)
        print(f"****** BOOK {n} ******")
        print(f"Total Words: {total_words(histB)}")
        print("Top Ten Most Common Words")
        h = most_common(histB)
        for i in range(0,10):
            print(h[i])
        n += 1 

#Main 

def main():
    #1. Downloads the book from the web ans saves them into hardrivel
    #downloadBookList(emily_dickinson_poems)
    #2. Read all books from their designated files and keep them in a list 
    tl = loadAll(len(emily_dickinson_poems))
    #3. Analize the sentiment of each poem with nltk 
    #nltk.download('vader_lexicon') #-> only the first time  
    s = sentimentNLTKforAll(tl)
    graphNLTKresults(s)
    #4. Words Frequency
    wordsRelevanceTF_IDFforALL(tl, ['a','an','and','the','all','as','10','15','1830','1886'])
    metrics(tl,['a','an','and','the','all','as'])



if __name__=='__main__': 
    main()

