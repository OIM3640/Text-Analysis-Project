from mediawiki import MediaWiki
# need to install via command prompt with "python -m pip install pymediawiki" before using
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from nltk.corpus import stopwords
# nltk.download('vader_lexicon')
# Need to run the above (nltk.download('vader_lexicon')) in terminal once in order for compareSentimentScores() to run. After this is downloaded it can be commented out.
from thefuzz import fuzz
# need to install via command prompt with "python -m pip install thefuzz" before using
import matplotlib.pyplot as plt

wikipedia = MediaWiki()

babson = wikipedia.page("Babson College")
bentley = wikipedia.page("Bentley University")


""" THIS BLOCK REMOVES THE STOP WORDS FROM THE WIKIPEDIA CONTENT"""
# nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

babo = babson.content.split()
bent = bentley.content.split()

filtered_Babo_words = [word for word in babo if word.lower() not in stop_words]
babson = ' '.join(filtered_Babo_words)

filtered_Bent_words = [word for word in bent if word.lower() not in stop_words]
bentley = ' '.join(filtered_Bent_words)

babson = str(babson)
bentley = str(bentley)

""" THIS BLOCK REMOVES THE STOP WORDS FROM THE WIKIPEDIA CONTENT"""



def compareTextSimilarity():
    """This function compares the text similarity (as a ratio)"""
    
    ratio = fuzz.token_sort_ratio(babson, bentley)
    print(f"The similarity between Babson's and Bentley's Wikipedia articles is {ratio}%!")


def compareSentimentScores():
    """Function compares the sentiment scores of the content of two wikipedia articles
    
    neg --> negative verbiage
    neu --> neutral verbiage
    pos --> positive verbiage
    compound --> neu + pos - neg (overall sentiment score)
    """
    
    score = SentimentIntensityAnalyzer().polarity_scores(babson)  
    score2 = SentimentIntensityAnalyzer().polarity_scores(bentley)

    for key in score:
        if score[key] > score2[key]:
            print(f"There is more {key} in Babson's Wikipedia page than Bentley's. The value of {key} for Babson is {score[key]} whereas the value for Bentley is {score2[key]}")
        else:
            print(f"There is more {key} in Bentley's Wikipedia page than Babson's. The value of {key} for Babson is {score[key]} whereas the value for Bentley is {score2[key]}")


def wordFrequency(count):
    """function creates two dictionaries for each wiki article, counts how many times a word is present in the article,
    sorts the dictionary in descending order, and prints the top desired amount of words via the parameter 'counter'
    
    example: if i wanted to get the top 5 words, i would do:
    
    wordFrequency(5)
    
    # and it would return
    
    The most common words in the Babson article are: 
    babson: 23
    mba: 20
    business: 19
    ===: 18
    college: 17

    The most common words in the Bentley article are:
    bentley: 50
    men's: 20
    ==: 18
    former: 16
    university: 14

    The function then prompts the user if they would like to print a bar chart visualizing the data. If they say yes,
    bar charts are shown to the user based on the amount of words they wanted to analyze
    """

    babson1 = babson.split()
    bentley1 = bentley.split()

    babo_frequency = {}
    bent_frequency = {}


    for word in babson1:
        word = word.lower()
        if word in babo_frequency:
            babo_frequency[word] += 1
        else:
            babo_frequency[word] = 1
    
    for word in bentley1:
        word = word.lower()
        if word in bent_frequency:
            bent_frequency[word] += 1
        else:
            bent_frequency[word] = 1

    
    # I learned about how to reverse a dictionary via ChatGPT: https://chat.openai.com/share/dcca8c2a-3cfd-4c37-84c6-1c63ad7d8474
    babo_frequency = dict(sorted(babo_frequency.items(), key=lambda item: item[1], reverse=True))
    bent_frequency = dict(sorted(bent_frequency.items(), key=lambda item: item[1], reverse=True))

    print(f"The {count} most common words in the Babson article are: ")
    counter = 0
    for key in babo_frequency:
        if counter < count:
            print(f"{key}: {babo_frequency[key]}")
            counter += 1
        else:
            break
    
    print(" ")
    print(f"The {count} most common words in the Bentley article are: ")
    counter = 0
    for key in bent_frequency:
        if counter < count:
            print(f"{key}: {bent_frequency[key]}")
            counter += 1
        else:
            break

    # I learned how to create a barchart with mathplotlib via ChatGPT: https://chat.openai.com/share/289e130d-16f4-4ef8-ad07-5ec183ce124f
    # I edited the code to show a bar chart based on the parameter value inputted by the user
    barchart = input("Would you like to visualize this data via a bar chart?")
    barchart = barchart.lower()
    if barchart == "yes":
        babowords = list(babo_frequency.keys())
        topbabowords = babowords[:count]
        babofrequencies = list(babo_frequency.values())
        topbabofrequencies = babofrequencies[:count]

        plt.figure(figsize=(10, 6))
        plt.barh(topbabowords, topbabofrequencies, color='skyblue')
        plt.xlabel('Frequency')
        plt.ylabel('Words')
        plt.title(f'The {count} Most Common Words in the Babson Article')
        plt.gca().invert_yaxis()
        plt.show()

        # Repeat the same bar chart for Bentley

        bentwords = list(bent_frequency.keys())
        topbentwords = bentwords[:count]
        bentfrequencies = list(bent_frequency.values())
        topbentfrequencies = bentfrequencies[:count]

        plt.figure(figsize=(10, 6))
        plt.barh(topbentwords, topbentfrequencies, color='skyblue')
        plt.xlabel('Frequency')
        plt.ylabel('Words')
        plt.title(f'The {count} Most Common Words in the Bentley Article')
        plt.gca().invert_yaxis()
        plt.show()

# I used ChatGPT to troubleshoot the below function: https://chat.openai.com/share/d97f9f09-c71e-48ae-ae6e-f15883560c57
def wordchecker(word):
    word = word.lower()
    
    babson2 = babson.lower().split()
    bentley2 = bentley.lower().split()

    if word in babson2:
        print(f'Yes, your word "{word}" is in the Babson Article.')
    else:
        print(f'No, your word "{word}" is not in the Babson Article.')
    
    if word in bentley2:
        print(f'Yes, your word "{word}" is in the Bentley Article.')
    else:
        print(f'No, your word "{word}" is not in the Bentley Article.')

def userAnalysis():
    """This is the core analysis function. It prompts the user which analysis type they want to do and outputs the result.
    
    This function is recursive, it continues to run until the user tells it to stop."""

    print("Hello! Welcome to the Wikipedia Analyzer. This program analyzes the articles of Babson College and Bentley University.")
    print("[1] Text Similarity")
    print("[2] Sentiment Scores")
    print("[3] Word Frequency")
    print("[4] Word Checker")

    userinput = int(input("Which option would you like to analyze?"))
    if userinput == 1:
        compareTextSimilarity()
    elif userinput == 2:
        compareSentimentScores()
    elif userinput == 3:
        usercounter = int(input("How many of the top words would you like to analyze?"))
        wordFrequency(usercounter)
    elif userinput == 4:
        word = input("What word would you like to check for in each article?")
        wordchecker(word)
    usercontinue()

    

def usercontinue():
    """This function asks if the user would like to continue analyzing. It converts what the user says to lowercase,
    checks if it is 'yes' or 'no', if yes runs userAnalysis(), if no it ends the program.
     
    If the user did not input a proper value, it tells the user to type either 'yes' or 'no' and calls usercontinue() again."""
    usercont = input("Would you like to continue?")
    usercont = usercont.lower()
    if usercont == "yes":
        userAnalysis()
    elif usercont == "no":
        print("Ok! Have a nice day!")
    else:
        print('Please either type "yes" or "no".')
        usercontinue()

userAnalysis()