# Text-Analysis-Project

1. Project Overview 

For this project, I analyzed text from the Wikipedia article "The Neighbourhood (band)" which is a band I listen to regualry but did not know much about its origins nor much about the members of the band. I used the MediaWiki API to fetch the article content, then cleaned and processed the text to study word frequencies, summary statistics, and visual patterns. I also used NLKT Vader sentiment analyzer to see the overall consensus on what the wikipedia page views the band to be as I did see there was some controversy with this band. I also implemented a Markov text generator to create new, band-style text based on the original article. My goal was to practice accessing data programmatically, working with text data structures, and experimenting with basic language models while working with data that truly fascinated and resonated with me

2. Implementation .

For this project, I used Python to analyze text from the Wikipedia article “The Neighbourhood (band)”. I started by using the MediaWiki library to access the article and then saved the data locally using the pickle module so I wouldn’t have to redownload it each time. Once I had the text, I cleaned it by converting everything to lowercase, removing punctuation, numbers, and extra spaces. I also removed common stop words like “the” and “and” using NLTK, which helped me focus on more meaningful words that described the band. After that, I created a dictionary-based word frequency counter to see which words appeared most often, and I wrote a summary function to calculate things like total words, unique words, and average word length.

To make the results easier to understand, I created visualizations using matplotlib and the wordcloud library, which clearly showed that the article focused on the band’s albums, songs, and members. I also used NLTK’s VADER sentiment analyzer to check if the article described the band in a positive, negative, or neutral way. As a final step, I built a Markov chain text generator that created new sentences based on the band’s Wikipedia page. The generated text wasn’t perfect, but it was fun to see how the model imitated the article’s tone and vocabulary. Throughout the project, I learned a lot about working with APIs, cleaning data, and experimenting with text-based models, all while exploring a topic that genuinely interested me.

3. Results 

After cleaning and analyzing the text from The Neighbourhood (band) Wikipedia article, several interesting patterns appeared. The most frequent words were band, released, album, lead, love, single, imagine, and music, which makes sense given how much of the article focuses on the band’s discography and musical style. The bar chart clearly highlighted these recurring terms, while the word cloud visually emphasized the same ideas, showing that the Wikipedia page revolves heavily around their albums, releases, and artistic identity.

The sentiment analysis using NLTK’s VADER tool produced the following results:

neg: 0.019  
neu: 0.911  
pos: 0.071  
compound: 0.9959  
Overall Sentiment: 😊 Positive  

These scores indicate that the overall tone of the article is highly positive, with very little negativity. This suggests that the band is presented favorably on Wikipedia, focusing more on their creative output and achievements rather than the  it has faced.

For the Markov text synthesis, I generated new text based on the cleaned article. The results were often jumbled but still recognizable, repeating words like “album,” “released,” and “imagine” in random but musically themed combinations. For example, one output read: “Revenge serious august premiered music video released march included tracks previous extended plays including lead single scary love...” Another example produced: “Band april neighbourhood announced summer tour called love collection tour along lovelife jmsn well planning release mixtape december released new ep called hard imagine...” While some of the generated sentences don’t follow clear grammar or structure, they reflect how the Markov model mimics the repetitive phrasing and musical terminology from the original article. This shows how text generation models can capture patterns of language without fully understanding context, producing interesting and sometimes chaotic outputs that still sound like something a band’s Wikipedia might say.

4. Reflection 

Overall, this project went really well and helped me gain a deeper understanding of how to work with text data in Python. I was proud of how I broke the project into smaller functions, which made it easier to test and fix errors along the way. The biggest challenge was cleaning and preprocessing the text correctly — especially when I was first getting random outputs or symbols that didn’t make sense. Another challenge was using a .py file as it is a bit different than the juypter files I usually use. I had to understand the terminal section more as I was downloading libraries and especially learning the difference between running commands in the Python terminal, PowerShell, and my computer’s regular terminal. At first, I kept getting errors like “module not found,” and I didn’t realize that I was entering commands in the wrong place. Once I learned to use pip install correctly inside the right environment, everything started running smoothly. If I were to improve the project, I’d try to generate text from multiple band articles and compare how their styles differ. This would allow me to do comparison visualization  models as well. 

From a learning perspective, my biggest takeaway was realizing how much potential text analysis has for exploring culture, music, and media through data. Before this project, I had never used APIs or performed text-based sentiment analysis, so learning how to fetch, clean, and visualize data felt like a big step forward. Using AI tools helped me understand new libraries like MediaWiki, NLTK, and wordcloud faster and guided me when I got stuck. Going forward, I feel more confident about applying Python to real-world datasets, especially when combining data science and creativity. I also learned that debugging patiently and documenting my process through comments and doc strings made the work much smoother because I was able to recall my steps faster. This assignment definitely tested my patience with the bugs I had to fix or modifying the code so it runs how I inteded it to and this is something I’ll definitely carry into future projects.
