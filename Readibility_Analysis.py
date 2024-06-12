import urllib.request
from textstat import flesch_reading_ease

"""I was initially trying to perform a topic model using LDA and specifically Gensim, but this could not work (will be explained further in essay)."""
""" Instead, I used the Flesch Reading Ease Score to calculate how complex/simple the play is to comprehend"""
# URL for "The Importance of Being Earnest" by Oscar Wilde
url = "http://www.gutenberg.org/ebooks/844.txt.utf-8"

with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')

# Calculate Flesch Reading Ease score
reading_ease = flesch_reading_ease(text)

print(f"The Flesch Reading Ease score for 'The Importance of Being Earnest' is {reading_ease}.")

"""I am printing a table for the users reference for them to gauage how easy or complex a book is"""

print("Please use the following table to comprehend the score of The Importance of Being Earnest")

# Table showing readability levels for Flesch Reading Ease Score
readability_table = """
Flesch Reading Ease Score   | Readability Level
-------------------------------------------------
90-100                      | Very Easy (5th grade level)
80-89                       | Easy (6th grade level)
70-79                       | Fairly Easy (7th-8th grade level)
60-69                       | Standard (9th-10th grade level)
50-59                       | Fairly Difficult (11th-12th grade level)
30-49                       | Difficult (College level)
0-29                        | Very Confusing (College Graduate level and above)
"""

print(readability_table)