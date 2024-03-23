# Text-Analysis-Project
 
Please read the [instructions](instructions.md).

**1. Project Overview** (~1 paragraph)

What data source(s) did you use? What technique(s) did you use to process or analyze them? What did you hope to create or learn through this project?

The text analysis project uses data from Wikipedia, which was extracted using the mediawiki library, a python wrapper and parser for the MediaWiki API. A function was created to process the data in which it first splits the content into lines then into words that are appended to a histogram. The histogram is a dictionary. To analyze them, I created functions to get basic summary statistics such as total number of words, the total unique number of words, and the frequencies of each word. Sentimental analysis was also conducted on random sentences pulled from the content of the Wikipedia page and text comparision was also conducted on random sentences pulled from the content. Through this project, I hope to better understand the concept of natural language processing so that in the future I could use it well.

**2. Implementation** (~1-2 paragraphs)

Describe your implementation at a system architecture level. You should NOT walk through your code line by line, or explain every function (we can get that from your docstrings). Instead, talk about the major components, algorithms, data structures and how they fit together. You should also discuss at least one design decision where you had to choose between multiple alternatives, and explain why you made the choice. Use shared links and/or screenshots to describe how you used ChatGPT to help you or learn new things.

**3. Results** (~1-3 paragraphs + figures/examples)

Present what you accomplished in your project:

If you did some text analysis, what interesting things did you find? Graphs or other visualizations may be very useful here for showing your results.
If you created a program that does something interesting (e.g. a Markov text synthesizer), be sure to provide a few interesting examples of the program's output.

**4. Reflection** (~1-2 paragraphs)

From a process point of view, what went well? What could you improve? Was your project appropriately scoped? Did you have a good testing plan?

From a learning perspective, mention what you learned through this project, how ChatGPT helped you, and how you'll use what you learned going forward. What do you wish you knew beforehand that would have helped you succeed?