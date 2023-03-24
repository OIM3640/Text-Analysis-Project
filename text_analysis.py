# Referenced the following source to learn how to import both the pyplot module and matplotlib library:
# https://www.geeksforgeeks.org/create-a-stacked-bar-plot-in-matplotlib/
import matplotlib.pyplot as plt # install command: python -m pip install -U matplotlib

# Referenced the assignment instructions to learn how to import these helper tools and how to initialize the MediaWiki API to an object:
# https://github.com/OIM3640/Text-Analysis-Project/blob/main/instructions.md
import pickle # ^
from nltk.sentiment.vader import SentimentIntensityAnalyzer # install command: python -m pip install nltk
from mediawiki import MediaWiki # install command: python -m pip install pymediawiki
wikipedia = MediaWiki()

# Referenced the following source to learn how to create a text file as an object and create a list variable without newlines from that object: 
# https://stackoverflow.com/questions/17569679/python-attributeerror-io-textiowrapper-object-has-no-attribute-split
with open('data/countries_of_the_world.txt') as database:
    countries = [line.rstrip('\n') for line in database]


def scan_wiki_countries():
    """
    This function performs sentiment analyses on the content of the English Wikipedia pages for every country in the world to detect for bias.

    Stores the sentiment variable within a pickle file.
    """
    """
    Psuedo Code:
    1.  Initialize sentiment as a list
    2.  Print a message informing the user of long wait times
    3.  Create a counter set to 1
    4.  Create an end_point set to the length of all the countries
    5.  Create a for loop for each country in the database
        1.  Load the Wiki for that country
        2.  Calculate the sentiment analysis for the Wikipedia page of the country
        3.  Append the previous value to the sentiment list
        4.  Tell the user that the sentiment analysis has been performed for a country
        5.  Increase the counter by 1
    6.  Store the computed sentiment analyses list to a pickle file
    """
    sentiment = []
    print(f'Please allow the program some time to scan through the Wikipedia pages.')
    counter = 1
    end_point = len(countries)
    for country in countries:
        country_wiki = wikipedia.page(country)
        # Referenced the assignment instructions to learn how to perform a sentiment analysis using the vader sub-module of the sentiment module of the nltk library:
        # https://github.com/OIM3640/Text-Analysis-Project/blob/main/instructions.md
        scores = [country, SentimentIntensityAnalyzer().polarity_scores(country_wiki.content)]
        sentiment.append(scores)
        print(f'Loaded {counter} of {end_point}')
        counter += 1
    # Referenced the following source to learn how to create a pickle file and write to its contents:
    # https://pythonnumericalmethods.berkeley.edu/notebooks/chapter11.03-Pickle-Files.html
    pickle.dump(sentiment, open('text_analysis.pkl', 'wb'))


# Referenced this source to learn about matplotlib: https://www.geeksforgeeks.org/create-a-stacked-bar-plot-in-matplotlib/
def bar_chart(sentiment, label = False):
    """
    This function charts the sentiment analysis per country on a stacked bar chart to visualize bias among English Wikipedia entries.

    Parameters: accepts the sentiment list and a boolean label for displaying the x axis

    Shows a stacked bar chart of the sentiment analysis.
    """
    """
    Psuedo Code:
    1.  Initialize countries as a list
    2.  Initialize pos_sentiment as a list
    3.  Initialize neg_sentiment as a list
    4.  Create a for loop that traverses every country within the sentiment analysis
        1.  Append each country to the countries list
        2.  Append each positive value to the pos_sentiment list
        3.  Append each negative value to the neg_sentiment list
    5.  If the label is False:
        1.  Hide the x axis
    6.  Set the title of the graph
    7.  Chart the positive sentiment of each country in green
    8.  Chart the negative sentiment of each country in red
    9.  Display the chart
    """
    countries = []
    pos_sentiment = []
    neg_sentiment = []
    for country in sentiment:
        countries.append(country[0])
        pos_sentiment.append(country[1]['pos'])
        neg_sentiment.append(country[1]['neg'])
    if label == False:
        # Referenced the following source to learn how to hide the x axis values of a chart:
        # https://stackoverflow.com/questions/37039685/hide-tick-label-values-but-keep-axis-labels
        plt.xticks([])
    # Referenced the following source to learn how to create and show a stacked bar shart using colors:
    # https://www.geeksforgeeks.org/create-a-stacked-bar-plot-in-matplotlib/
    plt.title("English Wikipedia Bias About Each Country")
    plt.bar(countries, pos_sentiment, color='g')
    plt.bar(countries, neg_sentiment, color='r')
    plt.show()


def chosen_bar_chart(sentiment, number = 6):
    """
    This function charts the sentiment analysis per country on a stacked bar chart for user specified countries

    Parameters: accepts the sentiment list and an integer number of countries

    Calls the bar_chart function after selecting the specified number of countries

    Returns: None in the instance that a user inputs 0 for the amount of countries they wish to see.
    """
    """
    Psuedo Code:
    1.  Converts the number to an integer. This disallows a user to input a float
    2.  If the user input number equals 0:
        1.  Tell the user 0 is not acceptable
        2.  Return nothing to terminate the code
    3.  If the number is negative:
        1.  Tell the user that negative numbers are not acceptable
        2.  Convert the negative integer into a positive integer
    4.  Initialize a list to chosen_sentiment variable
    5.  Initialize a list to countries variable
    6.  Initialize a counter set to 0
    7.  Initialize a boolean variable set to False
    8.  Tell the user to choose a country from the list of countries
    9.  Creates a for loop for every country in the sentiment list
        1.  Append only the country to the countries list
    10. Print the countries list for the user
    11. While the counter is less than the number of countries a user wishes to see
        1.  Ask the user to input a country
        2.  Create a for loop for each country in the sentiment list
            1.  If the user input name matches a country in the list:
                1.  Append that country and its sentiment analysis to the chosen_sentiment list
                2.  Set the checker to True
                3.  Increase the counter by 1
        3.  If the checker is False:
            1.  Tell the user to spell the country name correctly
        4.  Otherwise:
            1.  Set the checker back to False.
    12. If the user selected number of countries will crowd the x axis:
        1.  Call the bar_chart using the selected countries
    13. Else:
        1.  Call the bar_chart using the selected countries and tell it to display the x axis.
    """
    number = int(number)
    if number == 0:
        print('Please select a number of countries that you wish to see greater than 0.\n')
        return
    if number < 0:
        print('Negative numbers are not allowed. Converting to absolute value.\n')
        number *= -1
    chosen_sentiment = []
    countries = []
    counter = 0
    checker = False
    print("Choose a country from the following list:")
    for country in sentiment:
        countries.append(country[0])
    print(countries, '\n')
    while counter < number:
        name = input("Enter a country name from the list >>> ")
        for country in sentiment:
            if name == country[0]:
                chosen_sentiment.append(country)
                checker = True
                counter += 1
        if checker == False:
            print(f'The country you entered was not detected. Please refer to the list above and try again.\n')
        else:
            checker = False
    if number > 6:
        bar_chart(chosen_sentiment)
    else:
        bar_chart(chosen_sentiment, True)


def main():
    scan_wiki_countries() # Note: takes a long time to load.

    # Referenced the following source to learn how to load the contents of a pickle file:
    # https://pythonnumericalmethods.berkeley.edu/notebooks/chapter11.03-Pickle-Files.html
    sentiment = pickle.load(open('./text_analysis.pkl', 'rb'))

    bar_chart(sentiment)

    chosen_bar_chart(sentiment, 0)
    chosen_bar_chart(sentiment, -4)
    chosen_bar_chart(sentiment, 2.5)


if __name__ == "__main__":
    main()