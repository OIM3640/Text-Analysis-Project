
################################################### TEST PROGRAM #################################################################################

###### RUNNING PROGRAM

    
import datapull_newspaper3k as newspaper
import datapull_reddit as reddit
import config

# INTEGRATING ALL TEXTS INTO LIST FOR ANALYSIS 

all_texts = []

for article in newspaper.news_contents:
    all_texts.append(article)

for comment in reddit.reddit_comments:
    all_texts.append(comment)

    # print(all_texts)

def text_analysis(aLL_texts: list):
    """
    This function prints and shows the visualiations created for the analysis of a company. Function takes parameter: all_texts; This parameter is a list.

    The function prints the frequency of each word on the texts in a tabular form and shows a bar graph for Sentiment Analyzer average scores.
    """

    ########### CHARACTERIZING BY WORD FREQUENCIES #######################
    # Creating a dictionary of words that appear in these data pulls and their frequencies

    stop_words = ['the', 'and', 'a', 'to', 'for', 'what', 'it', 'this']

    frequent_words = {}

    for item in all_texts:
        words = item.split(" ")
        for word in words:
            if word.lower() not in stop_words:
                if word not in frequent_words:
                    frequent_words[word] = 1
                else: 
                    frequent_words[word] += 1

    sorted_frequent = dict(sorted(frequent_words.items(), key = lambda item: item[1], reverse=True))

    print(sorted_frequent)

    ############################  NATURAL LANGUAGE PROCESSING #############################
    # coded based on example in instructions at first, added some of my own elements to it, and finally modified it to accomodate for visualizations 
    # https://chat.openai.com/share/0ce2d5c9-1fa0-4674-a3d5-b672516bfe4c

    from nltk.sentiment.vader import SentimentIntensityAnalyzer

    overall_sscores = {}

    for item in all_texts:
        sentence = item
        score = SentimentIntensityAnalyzer().polarity_scores(sentence)
        overall_sscores[item] = score


    categories = ['neg', 'pos', 'neu', 'compound']
    category_totals = {category: 0 for category in categories}
    category_counts = {category: 0 for category in categories}

    for text, score in overall_sscores.items():
        for category in categories:
            category_totals[category] += score[category]
            category_counts[category] += 1

    category_averages = {category: category_totals[category]/category_counts[category] for category in categories}

    #################################### VISUALIZATION ###########################################################

    # Asked ChatGPT for toolkits I could use to create a visualization of results: https://chat.openai.com/share/f991f59b-4ada-4a1c-8a03-43f36b4930d6

    # Word frequency visualization

    from tabulate import tabulate

    sorted_frequent_list = [[word, frequency] for word, frequency in sorted_frequent.items()]

    table = tabulate(sorted_frequent_list, headers=["Word", "Frequency"], tablefmt="grid")



    # Sentiment Analyzer results

    import matplotlib.pyplot as plt
    import numpy as np


    average_scores = [category_averages[category] for category in categories]

    x = np.arange(len(categories))

    plt.bar(x, average_scores)
    plt.xlabel("sentiment Categories")
    plt.ylabel("Average Scores")
    plt.title(f"Bar Chart of Sentiment levels and Average Total Scores for {config.company_query} news")
    plt.xticks(x, categories)


    print(f'The list of all texts extracted from newspaper3k and reddit APIs, based on the search of {config.company_query} news is: {all_texts}')
    print("The following words were the most frequent...")
    # print(table)
    print("The sentiment analysis scores for these texts averaged:")
    plt.show()



if __name__ == "__main__":
    text_analysis(all_texts)


