# analyze_reviews.py
# Required steps: clean -> stopwords -> freqs -> stats -> ASCII chart.
# Optional: VADER sentiment (toggle with USE_SENTIMENT = True)
#
# AI Assistance (ChatGPT, November 2025):
# - Used for documentation: Writing docstrings and comments explaining what each code section does
# - Used for reference: "How to use VADER sentiment analyzer from NLTK in Python" (looked up API usage)

from typing import List, Dict
from collections import Counter
from text_utils import clean_text, tokenize, remove_stopwords, word_frequencies, summary_stats, ascii_bar_chart

# Optional sentiment block (safe if nltk isn't installed as long as USE_SENTIMENT=False)
USE_SENTIMENT = False
_sia = None

def _init_sentiment():
    global _sia
    if _sia is None:
        import nltk
        nltk.download('vader_lexicon', quiet=True)
        from nltk.sentiment.vader import SentimentIntensityAnalyzer
        _sia = SentimentIntensityAnalyzer()

def analyze_title_reviews(title: str, reviews: List[Dict], top_n: int = 20):
    """
    reviews: list of dicts with 'content'
    Prints stats & top words, returns a dict of results you can save if needed.
    """
    tokens = []
    sentiments = []

    for r in reviews:
        text = clean_text(r.get("content", ""))
        toks = tokenize(text)
        toks = remove_stopwords(toks)
        tokens.extend(toks)

        if USE_SENTIMENT:
            if _sia is None:
                _init_sentiment()
            score = _sia.polarity_scores(text)["compound"]
            sentiments.append(score)

    freqs: Counter = word_frequencies(tokens)
    stats = summary_stats(tokens)
    top = freqs.most_common(top_n)

    print(f"\n=== {title} ===")
    for k, v in stats.items():
        print(f"{k}: {v}")
    print(f"\nTop {top_n} words:")
    print(ascii_bar_chart(top))

    if USE_SENTIMENT and sentiments:
        avg = sum(sentiments)/len(sentiments)
        print(f"\nApprox. average VADER compound sentiment: {avg:.3f}")

    return {
        "title": title,
        "stats": stats,
        "top_words": top,
        "num_reviews": len(reviews),
        "avg_sentiment": (sum(sentiments)/len(sentiments)) if (USE_SENTIMENT and sentiments) else None
    }

