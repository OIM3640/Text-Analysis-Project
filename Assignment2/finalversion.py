import nltk
from newsapi import NewsApiClient
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from collections import Counter

def main():
    nltk.download("vader_lexicon")  # Used for sentiment analysis

    # Init
    newsapi = NewsApiClient(api_key="02c327faf5fe45cf982405221d456274")
    sid = SentimentIntensityAnalyzer()


    def get_sentiment(description):  
        """
        Evaluate the sentiment of each article description and chck whether its positive,
        negative, neutral and state if there is no description available
        """
        if (
            description and description.strip()
        ):  # Check if the description exists and is not empty
            score = sid.polarity_scores(
                description
            )  # Compute the sentiment score for the article's description
            compound_score = score["compound"]
            if compound_score >= 0.05:  # categorizing sentiment based on score
                sentiment = "THIS DESCRIPTION HAS A POSITIVE SENTIMENT"
            elif compound_score <= -0.05:
                sentiment = "THIS DESCRIPTION HAS A NEGATIVE SENTIMENT"
            else:
                sentiment = "THIS DESCRIPTION HAS A NEUTRAL SENTIMENT"
        else:
            sentiment = "No description available"
        return sentiment


    def most_common(word_count, excluding_stopwords=False):
        """
        Stopwords and additional terms to be skipped when we are counting words
        """
        stopwords = set(
            [
                "a",
                "about",
                "above",
                "after",
                "again",
                "against",
                "ain",
                "all",
                "am",
                "an",
                "and",
                "any",
                "are",
                "aren",
                "aren't",
                "as",
                "at",
                "be",
                "because",
                "been",
                "before",
                "being",
                "below",
                "between",
                "both",
                "but",
                "by",
                "can",
                "couldn",
                "couldn't",
                "d",
                "did",
                "didn",
                "didn't",
                "do",
                "does",
                "doesn",
                "doesn't",
                "doing",
                "don",
                "don't",
                "down",
                "during",
                "each",
                "few",
                "for",
                "from",
                "further",
                "had",
                "hadn",
                "hadn't",
                "has",
                "hasn",
                "hasn't",
                "have",
                "haven",
                "haven't",
                "having",
                "he",
                "her",
                "here",
                "hers",
                "herself",
                "him",
                "himself",
                "his",
                "how",
                "i",
                "if",
                "in",
                "into",
                "is",
                "isn",
                "isn't",
                "it",
                "it's",
                "its",
                "itself",
                "just",
                "ll",
                "m",
                "ma",
                "me",
                "mightn",
                "mightn't",
                "more",
                "most",
                "mustn",
                "mustn't",
                "my",
                "myself",
                "needn",
                "needn't",
                "no",
                "nor",
                "not",
                "now",
                "o",
                "of",
                "off",
                "on",
                "once",
                "only",
                "or",
                "other",
                "our",
                "ours",
                "ourselves",
                "out",
                "over",
                "own",
                "re",
                "s",
                "same",
                "shan",
                "shan't",
                "she",
                "she's",
                "should",
                "should've",
                "shouldn",
                "shouldn't",
                "so",
                "some",
                "such",
                "t",
                "than",
                "that",
                "that'll",
                "the",
                "their",
                "theirs",
                "them",
                "themselves",
                "then",
                "there",
                "these",
                "they",
                "this",
                "those",
                "through",
                "to",
                "too",
                "under",
                "until",
                "up",
                "ve",
                "very",
                "was",
                "wasn",
                "wasn't",
                "we",
                "were",
                "weren",
                "weren't",
                "what",
                "when",
                "where",
                "which",
                "while",
                "who",
                "whom",
                "why",
                "will",
                "with",
                "won",
                "won't",
                "wouldn",
                "wouldn't",
                "y",
                "you",
                "you'd",
                "you'll",
                "you're",
                "you've",
                "your",
                "yours",
                "yourself",
                "yourselves",
                "venture",
                "capital",
                "(marketscreener.com)",
            ]
        )
        # I asked GPT to come up with a list of common stopwords and I also added words that were appearing in the output that were not relevant

        if excluding_stopwords: #This condition will filter out stopwords, digits, and single-character words from the word_count dictionary
            word_count = {
                word: freq
                for word, freq in word_count.items()
                if word not in stopwords and not word.isdigit() and len(word) > 1
            }
        return sorted([(freq, word) for word, freq in word_count.items()], reverse=True) # The return statement sorts the words by their frequency in descending order, giving a list of tuples (frequency, word).

    # I asked GPT help to create an if statement to exclude the stopwords

    word_frequencies = Counter()
    sentiment_counts = Counter()

    # /v2/everything #get everything is the one i started initially using, now i will use Keywords for loop
    all_articles = newsapi.get_everything(
        q="Venture Capital",
        from_param="2023-10-30",  # you can only get news until october 4th and on, thats why I chose one month from october 10th to november 10th
        to="2023-11-30",
        language="en",
        sort_by="relevancy",
        page=2,
    )

    # Uncomment the following if you want to search for multiple keywords and comment the part above tat only shows "Venture Capital"
    # keywords = ['Venture Capital', 'Startup Funding', 'Investment Trends']
    # for keyword in keywords:
    #     all_articles = newsapi.get_everything(
    #         q=keyword,
    #         from_param="2023-10-30",
    #         to="2023-11-30",
    #         language="en",
    #         sort_by="relevancy",
    #         page=2,
    #     )

    # /v2/top-headlines/sources
    sources = newsapi.get_sources()

    # Printing the results to understand components of what the API is fetching
    # print(sources)
    # print(all_articles)

    for article in all_articles["articles"]:
        source_name = article["source"]["name"]
        title = article["title"]
        author = article["author"]
        url = article["url"]
        published_at = article["publishedAt"]
        description = article["description"]
        sentiment = get_sentiment(description)  # Call the function inside the loop
        sentiment_counts[
            sentiment
        ] += 1  # Increment the counter for the respective sentiment

        print(f"Source: {source_name}")
        print(f"Title: {title}")
        print(f"Author: {author}")
        print(f"URL: {url}")
        print(f"Published At: {published_at}")
        print(f"Description: {description}")
        print(sentiment)
        print("-" * 50)  # creates a line to separate the different news

        if description:
            """if there is anything of anykind this if function will start executing (set to true)"""
            description_lower = (
                description.lower()
            )  # Convert the description to lowercase to ensure uniformity
            words_split = (
                description_lower.split()
            )  # Split the description into individual words based on whitespace
            words = []  # Initialize an empty list to hold the filtered words
            for word in words_split:  # Iterate over each word in the split description
                if (
                    len(word) > 1 and not word.isdigit()
                ):  # Check if the word is more than one character long and not a digit
                    words.append(
                        word
                    )  # If the word passes the checks, add it to the list of words
            word_frequencies.update(words)  # to get word frequency

    total_articles = len(all_articles["articles"])  # counts how many articles
    print(f"SENTIMENT ANALYSIS")
    print(f"Total number of article descriptions: {total_articles}")
    print(
        f"Article descriptions with a POSITIVE sentiment: {sentiment_counts['THIS DESCRIPTION HAS A POSITIVE SENTIMENT']}"
    )
    print(
        f"Article descriptions with a NEGATIVE sentiment: {sentiment_counts['THIS DESCRIPTION HAS A NEGATIVE SENTIMENT']}"
    )
    print(
        f"Article descriptions with a NEUTRAL sentiment: {sentiment_counts['THIS DESCRIPTION HAS A NEUTRAL SENTIMENT']}"
    )
    print(
        f"Number of articles without description: {sentiment_counts['No description available']}"
    )

    common_words = most_common(word_frequencies, excluding_stopwords=True)
    print("-" * 50)
    print(f"WORD COUNT")
    print("These are the most common words found in the 100 news article descriptions:")
    print(common_words[:10])  # gets the top 10 most common words


if __name__ == "__main__":
    main()