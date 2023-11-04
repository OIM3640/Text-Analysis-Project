from data_processing import import_file, spam_ham_lists
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt


def sentiment_analysis(messages):
    """Perform sentiment analysis on list messages.

    messages: list of messages

    returns: list of sentiment values (sentiment values are in dictionaries)
    """
    # code source: https://github.com/OIM3640/Text-Analysis-Project/blob/main/instructions.md 
    sentiment_list = []

    for sentence in messages:
        score = SentimentIntensityAnalyzer().polarity_scores(sentence) 
        sentiment_list.append(score)
    
    return sentiment_list


def sentiment_analysis_averages(sentiment_list):
    """Calculates average sentiment of messages overall and positive/negative messages.
    
    sentiment_list: list of sentiment values (sentiment values are in dictionaries)
    
    returns: list of (stat name, stat value) pairs
    """
    res_stats = []
    compound_list = []
    pos_compound_list = []
    neg_compound_list = []

    for sentiment in sentiment_list:
        compound_score = sentiment["compound"] # compound score represents overall sentiment score.
        if compound_score > 0: # Positive compound score equates to a positive sentiment (and vice verse).
            pos_compound_list.append(compound_score)
        elif compound_score < 0: # Takes negative sentiments, excluding any neutral sentiments.
            neg_compound_list.append(compound_score)
        compound_list.append(compound_score)

    average_compound = round((sum(compound_list) / len(compound_list)), 2) # source: https://www.geeksforgeeks.org/find-average-list-python/ 
    average_pos_compound = round((sum(pos_compound_list) / len(pos_compound_list)), 2)
    average_neg_compound = round((sum(neg_compound_list) / len(neg_compound_list)), 2)

    res_stats = [("Avg. Sentiment", average_compound), 
                  ("Avg. Pos. Sentiment", average_pos_compound), 
                  ("Avg. Neg. Sentiment", average_neg_compound)]
    
    return res_stats


def bar_graph_sentiment_analysis(stat_value, message_type):
    """Bar chart with average sentiment of messages overall and positive/negative messages.

    stat_value: list of (stat name, stat value) pairs
    message_type: string, type of message displayed on bar chart (e.g. "Spam Messages")

    shows: bar chart
    """
    # Code source: ChatGPT
    # x is a list of stat names, y is a list of stat values
    x, y = zip(*stat_value) 

    plt.bar(x, y)
    plt.xlabel("Sentiment Analysis Statistics")
    plt.ylabel("Values")
    plt.title(f"Sentiment Analysis Bar Chart: {message_type}")

    plt.show()


def combined_bar_chart(spam_stats, ham_stats):
    """Combines statistics from different message types into one bar chart

    spam_stats, ham_stats: list of (stat name, stat value) pairs

    shows: bar chart
    """
    # x_spam and x_ham are lists of stat names, y_spam and y_ham are lists of stat values
    x_spam, y_spam = zip(*spam_stats)
    x_ham, y_ham = zip(*ham_stats)
    
    # Edit stat names: shorten and add message type
    x_spam = ["S Avg.", "S Avg. Pos.", "S Avg. Neg."]
    x_ham = ["H Avg.", "H Avg. Pos.", "H Avg. Neg."]

    # Combine stat names and stat values
    combined_stat_names = []
    combined_stat_values = []
    combined_stat_names = x_spam + x_ham
    combined_stat_values = y_spam + y_ham

    # Convert into list of (stat name, stat value) pairs
    combined_stats = list(zip(combined_stat_names, combined_stat_values))

    bar_graph_sentiment_analysis(combined_stats, message_type="Spam and Ham Messages")


def main():
    spam_dict = import_file()
    spam_list, ham_list = spam_ham_lists(spam_dict)
    spam_sentiment = sentiment_analysis(spam_list)
    ham_sentiment = sentiment_analysis(ham_list)
    spam_stats = sentiment_analysis_averages(spam_sentiment)
    ham_stats = sentiment_analysis_averages(ham_sentiment)

    bar_graph_sentiment_analysis(spam_stats, message_type="Spam Messages")
    bar_graph_sentiment_analysis(ham_stats, message_type="Ham (Non-Spam) Messages")
    combined_bar_chart(spam_stats, ham_stats)
    

if __name__ == '__main__':
    main()