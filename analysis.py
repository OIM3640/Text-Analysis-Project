"""The following code aims to solve part 2 where in counter is used to measure the frequency of reviews with the keyword "animation" under the genre for imdb reviews. """

import matplotlib.pyplot as plt # Required for frequency diagram. donwloaded via terminal
from collections import Counter 
from extraction import animated_movies # extract list from extracted.py for frequency diagram

year = [movie['year'] for movie in animated_movies if movie['year'] is not None]

""" Following code is used to extract years from extraction.py and sort them into a table for a frequency diagram"""


count_years = Counter(year)
sorted = sorted(count_years)
sorted_counts = [count_years[year] for year in sorted]

# Following code used from matplotlib page for a frequency diagram

plt.figure(figsize=(12, 6))
plt.bar(sorted, sorted_counts, color='teal')
plt.title('Animated Movies Released Per Year')
plt.xlabel('Year')
plt.ylabel('Number of Movies')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()





