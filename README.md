# Text-Analysis-Project

Please read the [instructions](instructions.md).

## 1. Project Overview

    I decided to use this project to analyze the languages of two ideologically radically opposite news sources: 
HuffPost (left-leaning) and The Epoch Times (right-leaning). I did so by extracting 40-50 latest news articles
from each source using the 'newspaper' Python library and processing them using a variety of programmatic tools
from simple code to 'collections', '.json', 'nltk' libraries. The research question is: **How does the language used
by political media sources and the sentiment conveyed by them differ based on their ideology?** I hoped to not
only extract and clean the data, but also uncover meaningful patterns in their political narratives through
comparing their word frequencies, vocabularies and sentiments. 

## 2. Implementation

    I can separate my project into three main steps: **data extraction/acquisition**, **data processing** (cleaning,
sorting), and analysis. First I looked at multiple political news sources to find the most fitting ones, not only
in terms of content and ideology, but also in terms of use of accessibility of their API and how easily they could 
be used and implemented into my code. ChatGPT was a big help here as it quickly identified matching news sources in
both criterias, and helped deal with (403 errors). I tested different sources, and rotated user-agent headers before
settling on HuffPost and The Epoch Times. I scraped 50 articles from both website using the 'newspaper' library and
stored tham as '.json' files containing a list of dictionaries containing their titles, URLs, and body texts.
    In the processing phase, I used various NLP techniques to clean the data nd organize it. I used 'string' library
and 'isalpha()' to remove punctuation, non-alphabetic characters, and lowercased everything. I was planning to use
'nltk' for analysis, but also used it to remove stop words, although had to mannually add some because my cleaning
technique wasn't as perfect. I then build histograms of word frequencies for each article, which helped me later
with analysis, but also helped me single out the **top words** from each article: instead of arbitrarily selecting
the most common one, I gathered all words that had at least (max_frequency - 10) appearances. This way I created
the richer vocabularies of most representative political terms for both sources. I then played around with the code
and ended up creating multiple '.json' files - with unique words, unique top words (3320 HuffSpot vs 3420 The Epoch
Times), top words(5617 HuffSpot vs 6104 The Epoch Times). 
    I then used these findings to conduct **aggregate frequency analyses** and **sentiment analysis**. I merged all
unique top words per source, counted their frequencies, and compared shared and exclusive vocabularies. I applied
VADER from 'nltk.sentiment' analysis package to access overall emotional tone of each article, and average those
scores to compare outlets. I used GenAI tools to debug unfamiliar errors, understand library documentation, 
brainstorm NLP strategies, compare newssources and bypass website restrictions. For a while I considered a different
approach to the entire project where I would extract the political vocabulary and sort articles based on that, 
which involved using a different documentation ('mediaWiki'), which OpenAI was also helpful with. 

## Results

    The frequency and vocabulary analyses showed clear patterns. As mentioned above, HuffPost produced a total of 5617
top words with 3320 of them being unique. The Epoch Times had 6104 words with unique being 3423. Out of those, only 
1193 were shared by both sources, leabing 2207 unique to HuffPost and 2230 to The Epoch Times. This suggests a strong
difference in languages used by the two sources, confirming that each of them uses a distinctive terminology to 
construct their political narratives. As for top words, they also reflect different vocabularies. Here's the ouput 
example:

    HuffPost Top 20 Words:                                                           Epoch Times Top 20 Words:
    back: 24                                                                         china: 16
    first: 23                                                                        united: 15
    huffpost: 22                                                                     states: 15
    help: 22                                                                         trump: 14
    free: 21                                                                         april: 14
    moment: 21                                                                       tariffs: 13
    without: 21                                                                      need: 13
    experience: 21                                                                   president: 12
    support: 20                                                                      house: 12
    fair: 20                                                                         make: 12
    news: 19                                                                         chinese: 11
    supported: 19                                                                    first: 11
    honest: 19                                                                       something: 11
    wont: 19                                                                         times: 11
    mission: 19                                                                      last: 11
    providing: 19                                                                    percent: 10
    critical: 19                                                                     effect: 10
    offering: 19                                                                     people: 10
    qualifying: 19                                                                   going: 10
    contributors: 19                                                                 years: 10

HuffPost's words include "support", "free", "fair", "contributors", "experience", suggesting it appeals to values like 
fairness and reader engagement. The Epoch Times includes "china", "tariffs", "president", "communist", and "freedom" - 
more menacing, serious words indicating a focus on national politics and foreign relations. Of course, it is tough to 
judge when analyzing just two little-known artiles. 
    Sentiment analysis provided a very strong contrast too. THe average sentiment score for HuffPost was 0.7757,
suggesting a positive tone, while a score of 0.2723 for The Epoch Times suggest a more neutral tone. This could reflect
outlets' differing rhetorical priorities. HuffPost's language aims to uplift it's audience, especially around topics 
like social justice, rights, and activism. While TET engages in ideological critique, geopolitical conflicts, etc., 
skewing towards neutral and cautious language. HuffPost's stories are more personal and value-driven, while TET frames
stories around systemic challenges and national concerns, which lend themselves to more emotionally restrained language.

## 4. Reflection

    From a process point of view, I believe once I was able to extract the files, it was smooth sailing from there. The
main roadblocks for me personally were in file extraction as I wasn't sure how to deal with 403 Errors and wasn't as
comfortable with APIs. Also, after extracting everything and organizing and cleaning data, I got a little lost as in what
I should do next, but was able to figure it out. I believe the results yilded through the project are not the best reflection
of differing languages, and there is always room for improvement. I need to learn more NLP techniques to allow for better 
ideation of what I can do with the data, and have a clear plan ahead of how I should process it. For example, after separating
top words into lists, I wasn't sure how to use those lists for sentiment or similarity analyses - it's just a wrong type of
data for that, so I need to work on my look ahead. Another big takeaway is how powerful NLP tools like frequency counts and 
VADER sentiment can be when used systematically. I was also initially intimidated by the modular design of the project, e.g. 
how I would organize everything, but learned it's value and realized how important it is to keep codes and project parts separate
as it makes it much easier. If I could start over, I would build a clearer testing pipeline earlier to work with intermidiate
outputs. Going forward, I will apply what I learned in other projects and experiments involving language processing. 