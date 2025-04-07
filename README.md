# Text-Analysis-Project

Please read the [instructions](instructions.md).
#URL: https://www.gutenberg.org/cache/epub/730/pg730.txt

Oliver Twist Text Analysis with a Side of Humor and Cyberpunk
1. Project Overview
For this project, I used the full-text version of Oliver Twist by Charles Dickens, sourced from Project Gutenberg. I processed the text using Python and several NLP tools to clean it, analyze word frequency, and enhance the experience with AI-generated content. My goal was to explore basic text analysis techniques while adding creative AI features that make the output more engaging, like generating dad jokes and cyberpunk rewrites. The project blends traditional language processing with GenAI elements to create a tool that’s both analytical and entertaining.
2. Implementation
The program is structured into modular components, starting with data acquisition from a URL, followed by text cleaning using regex and string manipulation. I removed boilerplate content and filtered out punctuation and stopwords to prepare the text for analysis. The cleaned data is saved locally using pickle to avoid redundant downloads and processing. Word frequencies were computed using collections.Counter, and stopwords were filtered out using NLTK.
A key design decision involved using OpenAI's API to generate dynamic content based on the book. Instead of building a custom text generation model or rule-based system, I used GPT-4o to generate a dad joke and rewrite part of the novel in the style of Neuromancer. I considered writing static jokes or summaries, but opted for real-time generation for creativity and variety. To learn how to interact with the API and troubleshoot formatting issues, I used ChatGPT as a tutor, especially while debugging prompt engineering and confirming expected response structures. A screenshot of my OpenAI prompt history is here: https://imgur.com/a/BtAA3K1.
3. Results
The program outputs a cleaned and filtered list of the most frequent words in Oliver Twist. Unsurprisingly, high-frequency words included emotionally and thematically loaded terms like "mr," "oliver," and "man", which reflect the book’s focus on poverty and identity.
Top 10 words in the text:
said: 1231
mr: 1078
oliver: 770
upon: 481
replied: 464
one: 454
old: 448
would: 410
man: 366
bumble: 365
As a fun, AI-enhanced bonus, the script generates a dad joke using the book text. For example:
    Dad Joke: Why did Oliver Twist bring a ladder to the workhouse?      
    Because he heard they wouldn't give him more, so he decided to "climb the social ladder" himself!
    Finally, the “Neuromancer-style rewrite” repurposes an excerpt of Dickens’ prose into a gritty cyberpunk aesthetic, adding a whole new layer to how we could experience classic literature. It gives a taste of what Oliver Twist might look like in a dystopian techno-thriller.
    For users who want to dig deeper, the app also includes a "Show Additional Data" button that reveals extra insights like word frequency tables and analysis summaries.
4. Reflection
The pipeline worked well once I got the data loaded and cleaned, and the AI integration added an unexpectedly enjoyable layer. The biggest challenge was formatting prompts and handling long text segments when interacting with the OpenAI API, especially keeping the prompts concise but contextually rich. I solved this by chunking the text and testing different prompt lengths. I also had to get comfortable with pickle and environment variable loading, which I hadn’t used much before.
From a learning perspective, my biggest takeaway was seeing how fast GenAI tools can accelerate creative and analytical projects. It was also a good reminder that APIs don’t just “work”, you have to think through how to integrate them meaningfully. In future projects, I want to explore more visualization tools or integrate the analysis into a web app. I wish I’d known more about prompt engineering from the start. It would have saved me time with formatting and consistency. Still, I’m proud of how it came together and how I was able to personalize a classic text with both humor and a futuristic twist.

