# Text-Analysis-Project
 
Please read the [instructions](instructions.md).

# IDEA:
### CREATE A PROGRAM THAT DOES SOCIAL MEDIA LISTENING (USING GOOGLE/NEWS SEARCH, YELP, AND REDDIT) & ANALYZES GENERAL SENTIMENT AND KEY WORDS ASSOCIATED WITH A COMPANY; THE PROGRAM PROMPT USER TO INPUT THE COMPANY THEY WANT TO RESEARCH AND WILL GIVE AN OUTPUT OF SNIPPETS FROM EACH CHANNEL, AN ANALYSIS OF THOSE SNIPPETS, AND AN SUMMARIZED ANALYSIS OF BRAND PERCEPTION ACCORDING TO THOSE CHANNELS.

## EXECUTION PLAN (subject to change):
### 1. Datapull with news headlines & google cse api (in progress @ datapull_newsheadlines.py) 
### 2. Datapull with reddit (datapull_reddit.py)
### 3. Datapull with yelp (dataoull_yelp.py)
### *Decision point: Decide which pieces of data are valuable and how they are relevant amongst each other; Decide text analysis that is relevant for each
### 4. Data analysis for headlines, reddit, and yelp
### 5. User interface creation and testing (create function that requests the company name input and returns all analyses); will need to edit data pulls to accomodate and do some back and forth; MAKE SURE TO USE TRICKS TO AVOID ERRORS WE TRED IN SESSION 15
### *Decision point: If everything works, what can I add? Do I have time to attempt more? etc.
### 6. Attempt program, make final edits, and edit readme to reflect application of finalized program