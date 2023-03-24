# Text-Analysis-Project

## Project Overview

Within this project, I sought to identify bias among writers on the English Wikipedia country pages. I selected the country description pages because they summarize the political history of groups of people and, therefore, should contain abundant material to discuss without bias. The existence of skewed negative or positive sentiment would suggest that the English Wikipedia page contains significant bias, which will invariably affect the global perception of particular countries. To discover this bias, I created a [text file](images/countries_of_the_world.txt) that contains all the countries of the world based on a [Wikipedia article](https://simple.wikipedia.org/wiki/List_of_countries). Then, I imported the [MediaWiki library](https://github.com/barrust/mediawiki) to use the `MediaWiki API` to temporarily store the content of every country page worldwide. I performed sentiment analysis on the temporarily stored data using the [natural language toolkit library](https://www.nltk.org/), specifically the [vader submodule](https://www.nltk.org/_modules/nltk/sentiment/vader.html). Then, I visually represented the results using the [pyplot module](https://matplotlib.org/stable/tutorials/introductory/pyplot.html) of the [Matplot library](https://matplotlib.org/). Finally, I used `pickle` to create a pickle file that contains the sentiment analyses as a list to save loading times.

## Implementation

Fundamentally, my code imports and formats the necessary helper tools, retrieves my countries list as a imagesbase variable, performs sentiment analyses for countries in the imagesbase using the `MediaWiki API`, dumps the sentiment analyses into a `pickle` file for later retrieval, visualizes the sentiment analyses from the pickle file using `Matplot Pyplot` graphs, and additionally prompts the user to compare countries by selecting specific information from the sentiment analyses. Per instructions, I used ChatGPT to provide recommendations on the best manner to visualize the data computed from the sentiment analyses, as seen in `Exhibit 1` and `Exhibit 2`.

**Exhibit 1**
<img src="images/ChatGPT - Chart Recommendation.png" width="500" alt="ChatGPT: Chart Recommendation" style="display:block; margin:10px auto" allign = "left"/>

**Exhibit 2**
<img src="images/ChatGPT - Stacked Bar Chart.png" width="500" alt="ChatGPT: Stacked Bar Chart" style="display:block; margin:10px auto"/>

Interestingly, ChatGPT provided code to visualize positive, negative, and neutral sentiment, though I did not ask it to do so. This is likely due to my previous question. Per the recommendation, I researched the `Matplot Pyplot` library and module on [geeksforgeeks](https://www.geeksforgeeks.org/create-a-stacked-bar-plot-in-matplotlib/) and sicovered a more simplistic method of generating the chart. I later elected to exclude netural sentiment to better demonstrate the prevalence of bias.

The most significant design choice surrounded creating my own [text file](images/countries_of_the_world.txt) rather than relying upon several pre-existing GitHub text files that contain all the countries in the world. I successfully loaded text files from GitHub for sentiment analysis, however, particular naming conventions applied to the countries caused the `WikiMedia API` to behave in an unintended manner. For instance, "Georgia" does not immediately direct to the country of Georgia, but instead to another page which asks asks whether the state of Georgia or the country of Georgia was intended. Because this issue affected a handful of countries, I manually created a list of countries named in a manner that does not result in any re-directs, like naming "Georgia" to "Republic of Georgia" among others.


## Results
The following charts seen in `Exhibit 3`, `Exhibit 4`, and `Exhibit 5` demonstrate incidences of bias across the world. `Exhibit 3` enables the user to hover over each line to understand specific images points of interest, for instance, that the United States country page has the most bias or that Mauritania has the most negative sentiment. `Exhibit 4` and `Exhibit 5` demonstrate geographical comparisons which shed significant insight into English Wikipedia bias.

**Exhibit 3**
<img src="images/Output - Bias Across the World.png" width="1000" alt="Bias Across the World" style="display:block; margin:10px auto" allign = "left"/>

**Exhibit 4**
<img src="images/Output - Notable Bias.png" width="1000" alt="Notable Biases" style="display:block; margin:10px auto" allign = "left"/>

**Exhibit 5**
<img src="images/Output - Geographical Bias.png" width="1000" alt="Geographical Bias" style="display:block; margin:10px auto" allign = "left"/>

The sentiment analyses reveal that English Wikipedia country pages often equally represent negative and positive sentiment for predominantly English first-language speaking countries. `Exhibit 4` reveals a degree of bias against particular countries like Afghanistan or Mauritania likely due to publicized geopolitical scandals like war and coup d'etats. `Exhibit 5` demonstrates an application of the program to analyze a particular geographical area. Ultimately, this program enables users to answer simple questions regarding how particular countries in the world are percieved. This program would work well to corroborate research surrounding cultural and geographic biases, insofar as the `natural language toolkit library` effectively performs sentiment analyses.


## Reflection
Originally, I intended to identify instances of repeated lines in certain religious texts like the Bible. However, due to the size of those texts, this was not possible easily. Consequently, I elected to focus on something more dynamic, given that the sentiment analyzes will change whenever the Wikipedia pages are altered. I tested the code iteratively with no particular issues after I determined precisely what I intended to do. The process of performing sentiment analyses on the 208 recognized and unrecognized countries of the world does take a significant amount of time, so I originally tested the code with a temporary variable that stored the output. Once I finalized the visualization component of my program, I learned how to use `pickle` which has seemingly worked well. For finishing touches, I added text to inform the user of the sentiment analyses progress, some failsafe logic for user input, and graph visualization features.

This project better familiarized me with APIs and particular libraries such as `pickle`, `natural language toolkit library`, and `Matplot library`. Within this project, I experimented with ChatGPT per instructions to gain an awareness of the `Matplot library` and the `pyplot` module. I subsequently researched the library and module until I found a method of achieving my desired outcome. In hindsight, I wish I knew how much memory would be required to parse through large texts. Hilariously, when I attempted to parse through the Bible, I received an error message indicating that my cache could not exceed 5 gigabytes. I did ask ChatGPT to debug, but the provided suggestions did not help; I anticipate more efficient code or excessive usage of `pickle` may have resolved the problem, but I moved on to the sentiment analyses of Wikipedia articles, which I considered more interesting due to their dynamic nature.