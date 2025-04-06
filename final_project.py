"""The following code aims to solve part 2 where in counter is used to measure the frequency of reviews with the keyword "drama" under the genre for imdb reviews. """

import matplotlib.pyplot as plt # Required for frequency diagram. donwloaded via terminal
from collections import Counter 
from extraction import drama_movies # extract list from extracted.py for frequency diagram
def main():

    year = [movie['year'] for movie in drama_movies if movie['year'] is not None]
    """ Following code created to count and sort the frequency of drama films in the top 250 films of all time """
    count_years = Counter(year)
    sorted = sorted(count_years)
    sorted_counts = [count_years[year] for year in sorted]

    """ The following code is used to calculate the frequency mentioned above and created a frequency diagram of the number of 250 drama films released every year """
    plt.figure(figsize=(12, 6))
    plt.bar(sorted, sorted_counts, color='teal')
    plt.title('Top Movies under Drama Genre every year')
    plt.xlabel('Year')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()







