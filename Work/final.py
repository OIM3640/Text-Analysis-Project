# _______________________________________________ Wikipedia Article Text Analysis
from mediawiki import MediaWiki

wikipedia = MediaWiki()


def remove_stopwords(text):
    """remove all the stopwords in the article content includeing punctuation, returns list of remaining words"""
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize

    stopwords_ = set(stopwords.words("english"))
    words = word_tokenize(text)
    texts = []
    punctuation = "!()-[]{};:'\"\ , <> . /?@#$%^&*_~ `` 's⟩ ⟨==='''"

    for w in words:
        x = 0
        w = w.lower()
        characters = []
        characters[:] = w
        for i in characters:
            if i in punctuation:
                x += 1
        if w in stopwords_:
            x += 1
        if len(w) == 1:
            x += 1
        if w == "the":
            x += 1
        if x == 0:
            texts.append(w)

    return texts


def gives_counts(texts: list):
    """counts frequency of all words in article content, returns dict with keys as words and values as frequency"""

    counts = dict()
    for i in texts:
        counts[i] = counts.get(i, 0) + 1
    return counts


def list_highest_count(counts: dict, k):
    """lists top k words by frequency and their corresponing frequencies, returns nothing"""

    counts_list = list(counts.items())
    ordered_counts = sorted(counts_list, key=lambda x: x[1], reverse=True)

    highest_counts = []

    included = 0
    print()
    while included < k:
        word = ordered_counts[included][0]
        count = ordered_counts[included][1]
        print(f"{word:10} was found {count:5} times")

        highest_counts.append(ordered_counts[included])
        included += 1
    print()
    return highest_counts

def comparison(a,b,k):
    """returns the common words in the k most frequent words of each list of words"""

    common = []
    common_count = 0

    for n in range(k):
        word = a[n][0]

        for item in b:
            if word == item[0]:
                common.append(word)
                common_count +=1

    perc = common_count/k
    response = ( 
        f"""Matching Words are {common}, 


        {common_count} out of the {k} most frequent words match. ({perc:.2}%)""")
            
    return response




# _______________________________________________ Current Event News Sentiment Analysis

from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key="966d42a19bf042c68e6bec614e7e74c4")


def remove_stopwords(text):
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize

    stopwords_ = set(stopwords.words("english"))
    words = word_tokenize(text)
    texts = []
    punctuation = "!()-[]{};:'\"\ , <> . /?@#$%^&*_~ `` 's⟩ ⟨==='''"

    for w in words:
        x = 0
        w = w.lower()
        characters = []
        characters[:] = w
        for i in characters:
            if i in punctuation:
                x += 1
        if w in stopwords_:
            x += 1
        if len(w) == 1:
            x += 1
        if w == "the":
            x += 1
        if x == 0:
            texts.append(w)

    return texts


def text_for_sentiment(topic):
    """prepares descriptions of the top 100 news articles in the US from the
    past two days on topic of choosing for sentiment analysis"""

    data = newsapi.get_everything(
        q=topic,
        from_param="2023-03-23",
        to="2023-03-24",
        language="en",
        sort_by="relevancy",
        page=1,
    )

    data = data["articles"]

    d = []
    for i in data:
        x = i.get("description")
        d.append(x)

    d = " ".join(d)
    d = remove_stopwords(d)
    d = " ".join(d)

    return d



def sentiment_(text,topic):
    """ provides and interprets sentiment analysis results given text"""

    from nltk.sentiment.vader import SentimentIntensityAnalyzer

    score = SentimentIntensityAnalyzer().polarity_scores(text)

    neg = score.get("neg")
    pos = score.get('pos')

    if neg == pos:
        sentiment  = "neutral"
    elif neg > pos:
        sentiment  = "negative"
    else:
        sentiment  = "positive"

    print(f'The NLTK Sentiment Analysis of "{topic}" in the US media from the past two days seems to be {sentiment}.')
    print(f'Numerical Results: {score}')
    


def main():
    """

    FIRTST
    compares two wiki articles by top most frequent words,
    more specifically, compares the most popular words in wiki
    articles for the two largest countries in north america
    prints results


    SECOND
    prints sentiment analysis of a popular current event
    using descriptions of the top 100 news articles in the US from the
    past two days


    """

    #  _______WIKI Inputs

    # article 1
    country_a = "The United States of America"
    # article 2
    country_b = "China"

    # top x most frequent words in each article to compare
    compare = 60


    #  _______News Inputs

    topic = "SVB"

    ChatGPT_Summary = """There have been recent bank collapses and runs on deposits in the US, causing concern about the stability of the banking system. The CEOs of Silicon Valley Bank and Signature Bank have been called to testify before the US Senate panel. Federal Reserve Chair Jerome Powell admits that the regulator was blindsided by the sudden collapse of Silicon Valley Bank, which sparked a panic in the financial markets. However, Powell declares that the banking system is sound and resilient. There are concerns about the risk of further bank failures, and the House Republicans are demanding detailed information from the Biden Administration. Some blame the failures on the rollback of Dodd-Frank, but others point to the poorly designed regulatory framework and government backing as the ultimate culprit.
                    Silicon Valley Bank's collapse is causing instability in the global banking system, prompting investors to adjust to more challenging economic and lending conditions. The sudden fall of SVB left regulators stumped, and a paper analyzing more than 4,800 U.S. banks was conducted to determine their exposure to the risks that led to the failure of SVB. Billions of dollars in deposits poured into the nation's banking giants, and the government protected depositors. Startups are having a hard time finding funding in the private equity markets, but fortunately, non-dilutive capital is available from the government and Google. Some banks are considered "unsafe" in the crypto market, and banking shares slipped in Europe on Thursday. The Federal Reserve is weighing the risks of continued high inflation, and JPMorgan Chase & Co analysts estimate that the "most vulnerable" U.S. banks are likely to have lost a total of about $1 trillion in deposits since last year. Citigroup CEO Jane Fraser said that banking crises have happened before, but this may be the first one accelerated by mobile banking and social media."""

    #  no need to touch below
    # ________________________________________________________________
    a = wikipedia.page(country_a)
    name_a = a.title
    text_a = a.content

    b = wikipedia.page(country_b)
    name_b = b.title
    text_b = b.content

    print()
    print(name_a)
    x = remove_stopwords(text_a)
    # print(x)
    y = gives_counts(x)
    f = list_highest_count(y, compare)

    print(name_b)
    x = remove_stopwords(text_b)
    y = gives_counts(x)
    g = list_highest_count(y, compare)
    print()

    print(comparison(f,g,compare))

    print()

    d = text_for_sentiment(topic)
    sentiment_(d,topic)
    print()

    topic = (f"{topic}_chatgpt")

    print("Using Chat GPT Summarized Articles")
    sentiment_(ChatGPT_Summary,topic)



if __name__ == "__main__":
    main()
