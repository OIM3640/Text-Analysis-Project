# README

## Project Overview:
To give some general context about my project: Two of my favorite works of literature I read in high school were
The Odyssey and Iliad, both by Homer. As I was scrolling through Project Gutenberg, looking for texts to analyze, they were amongst the most popular downloaded on the site. Thus, I thought it would be fun to compare the two pieces of work. What drew me to the works initially was the vast world Homer details within the texts, the gods, the heroes, battles, places, etc. The "world-building" was very appealing to me, and that same draw became the foundation of my project. I wanted to see what kinds of words show up most often in each work, and then go a step further and try to automatically pull out the characters, places, and gods mentioned in different passages. To do that, I cleaned the text (lowercasing, removing punctuation, removing stopwords) and ran word-frequency analysis. Then I used the OpenAI API to label small chunks of the text with entities. The goal was to build a basic text-analysis pipeline and to practice using API's and an external AI service inside a Python script.


## 2. Implementation

Before I started writing any code, I outlined my system architecture and project requirements to make sure I tackled every part of it.

My requirements were:
- Download the texts
- Clean and filter the texts
- Analyze the text through word frequency and chart the findings
- Use the OpenAI API to show the most mentioned characters, places, and gods
- Use the API to compare the two texts and see what/if characters, places, and gods appear in both texts
- Return the API findings in json format

I split the project into two files: `api.py` and `project.py`. `api.py` is responsible for anything “external”: loading my OpenAI API key from a `.env` file, and providing the function that calls the model to extract entities. `project.py` is the main function. It downloads the two texts from Gutenberg, strips out the header/footer, cleans the text, removes stopwords (I ended up making my own stopwords list, albeit to varying success due to the nature of the texts), counts word frequencies, and then makes repeated calls to the API on fixed-size text chunks. The API results are combined into dictionaries that count how many times each character/place/god was mentioned.

One design decision was how to do the visualization. The instructions said I needed at least one visualization, so I decided to print a simple ASCII bar chart of the top 15 words for each text, showcasing the relative frequencies. Another design decision was chunk size vs. number of API calls: sending the whole epic in one request isn’t practical (and as I discovered a very easy way to get yourself rate limited by OpenAI), so I picked a chunk size (~1200 words) and a max number of chunks per run to avoid hammering the API and to keep the cost of calling the API down. ChatGPT was extremely helpful, especially in implementing the OpenAI API to do what I sought out to do, and diagnosing the numerous errors I encountered along the way.


## 3. Results

After cleaning and removing stopwords, the top words for each text started looking more meaningful (fewer “the/and/my/thou”) as I iterated the stopwords list. The ASCII bar chart shows the most common content words in the *Iliad* and in the *Odyssey* separately.

I explored using other people's stopping words lists for the texts, like [https://github.com/aurelberra/stopwords/blob/master/stopwords_greek_odyssey.txt] - but I didn't really find what I was looking for (for example, that person made stopping words for the ancient greek version of the text, obviously I was not using the ancient greek version of the text...) From there, I considered using the NLTK library for default stopping words, but I thought it could be more fun to try to do it myself.

On the “advanced” side, I used the OpenAI API to return structured JSON for passages like:

```json
{
  "characters": ["Achilles"],
  "places": ["Troy"],
  "gods": ["Athena"]
}
```

I ran this over multiple chunks and then tallied the results, so I could print “most mentioned characters (partial)” for each work. Because API rate limits can slow things down, I limited how many chunks to send in one run, but the structure is there to process the whole text. This means the program doesn’t just count plain words,  it can also name the important figures in the epic, which is something basic frequency analysis can’t do on its own.

## 4. Reflection

I personally found this project to definitely be a learning curve, but I had a lot of fun completing it. What went well was the basic text pipeline of downloading the text -> cleaning it -> filtering stopwords -> counting the words -> plotting with the ASCII chart. That part I had a good idea of how to do, and ChatGPT helped answer some questions along the way. The hardest part by far was getting the OpenAI API to work smoothly; that took a lot of work, and a lot of prompting ChatGPT to return what I wanted it to do. My biggest takeaway (and how I solved the implementing the OpenAI API issue) was that it's very important to be very clear in what you're trying to do, how you're currently doing it, and what is wrong when asking ChatGPT for help. I found that a lot of the code it was giving me I didn't really understand, and that felt detrimental to my learning and to the project, so I only wanted to use code I felt like I at least had some understanding of what it was doing.

# A note on the OpenAI API:
Before this project I always wanted to experiment with the API, so this felt like a good time to do so. I had to consider some trade-offs in using it, like which model I was using to perform my analysis and it's price per 1M tokens. I opted to use the cheapest model, gpt-5-nano, as I felt it was good enough for the scope of this project. The current rates for each model are [https://platform.openai.com/docs/pricing]. I know you offered to cover the cost of the tokens, but I didn't mind paying for it myself as I plan on exploring other uses for the API in my free time. For transparency, I ended up running 122 total requests, using 167,886 tokens at a cost of 26 cents.

Ultimately, I learned how to combine simple local text analysis with a cloud model that can understand entities.  The local part is fast and free; the API part is flexible and “smarter,” but you have to be careful about cost and rate limits. AI tools helped me implement my vision for the project, and bring it to life while making sure I understood what each line was doing. If I were to do this project again, I would try to find ways to optimize it, as during my testing it took a long time for the API to return what I wanted from it, even after limiting the input through breaking the texts into chunks.
