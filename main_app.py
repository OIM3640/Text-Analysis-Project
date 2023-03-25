def main():
    """
    Run this file to generate summary results for all text analysis techniques in this repository.

    Note:
    - Some output may take longer to load or load in another location. Details commented next to functions.
    - Additional statistics and graph output code located in each file.
    """
    # Imports / Data Processing
    from data_processing import import_file, spam_ham_lists, spam_ham_string, histogram
    from common_words import most_common_words, top_unique_words, bar_chart_word_freq, word_cloud
    from sentiment_analysis import sentiment_analysis, sentiment_analysis_averages, combined_bar_chart
    from markov_analysis import markov_analysis

    spam_dict = import_file()
    spam_list, ham_list = spam_ham_lists(spam_dict)
    spam_paragraph = spam_ham_string(spam_list)
    ham_paragraph = spam_ham_string(ham_list)
    spam_hist = histogram(spam_paragraph, paragraph=True)
    ham_hist = histogram(ham_paragraph, paragraph=True)


    # 1. Summary Statistics (common words in spam and ham)
    spam_common_words = most_common_words(spam_hist)
    ham_common_words = most_common_words(ham_hist)

    top_spam_words = top_unique_words(spam_common_words, ham_common_words)
    top_ham_words = top_unique_words(ham_common_words, spam_common_words) # loads after spam bar chart is x-ed out

    bar_chart_word_freq(top_spam_words, n=10, stat_name="Top Spam Words")
    bar_chart_word_freq(top_ham_words, n=10, stat_name="Top Ham (Non-Spam) Words")

    word_cloud(top_spam_words, n=30, cloud_name="spam_cloud.png") # generated in Explorer tab (page icon on upper left of screen)
    word_cloud(top_ham_words, n=30, cloud_name="ham_cloud.png") # generated in Explorer tab (page icon on upper left of screen)


    # 2. Sentiment Analysis
    spam_sentiment = sentiment_analysis(spam_list)
    ham_sentiment = sentiment_analysis(ham_list)

    spam_stats = sentiment_analysis_averages(spam_sentiment)
    ham_stats = sentiment_analysis_averages(ham_sentiment)

    combined_bar_chart(spam_stats, ham_stats) # takes a few seconds to load after ham bar chart is x-ed out

    # 3. Markov Analysis
    markov_analysis(spam_paragraph) # loads after combined bar chart is x-ed out
    markov_analysis(ham_paragraph)

if __name__ == '__main__':
    main()