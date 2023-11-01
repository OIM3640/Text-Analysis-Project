import matplotlib.pyplot as plt 
import most_common
most_common.analyze_reviews
most_common.count_words_frequency

'''
This code allows you to visualize the frequency of positive
and negative words from the most_common py file.
'''

def plot_of_frequency(positive_count, negative_count):

    labels = ['Positive', 'Negative']
    data = [positive_count, negative_count]

    plt.bar(labels,data) 

    plt.title('Word Frequency in IMDB Reviews')
    plt.xlabel('Type of Review')
    plt.ylabel('Frequency')

    plt.show()

    plot_of_frequency(positive_count, negative_count)


