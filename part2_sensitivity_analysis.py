import urllib.request
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')

def fetch_text(url):
    """Fetch text from the given URL using urllib."""
    try:
        with urllib.request.urlopen(url) as f:
            return f.read().decode('utf-8')
    except Exception as e:
        print("An error occurred while fetching the text:", e)
        return ""
    
def analyze_sentiment(text):
    """Performs sentiment analysis on the text."""
    analyzer = SentimentIntensityAnalyzer()
    return  analyzer.polarity_scores(text)

def main():
    url = "https://www.gutenberg.org/cache/epub/11/pg11.txt"
    text = fetch_text(url)
    if not text:
        return
    
    sentiment = analyze_sentiment(text)
    
    # Display sentiment analysis results
    print("Sentiment Analysis:")
    print(f"Positive: {sentiment['pos']:.3f}, Neutral: {sentiment['neu']:.3f}, Negative: {sentiment['neg']:.3f}, Compound: {sentiment['compound']:.3f}")

if __name__ == "__main__":
    main()


# Suggestions for improvement by ChatGPT:

# Prompt: "I just finished my Python assingment, can you help me go through every file and
# make any suggestions for improvement in terms of overall functionality, organization, and style?"

# Small things to fix:
    # 🎯 NLP Best Practice	Ideally nltk.download('vader_lexicon') should be inside a try/except, or placed under a setup script, not inside the main script	Just cleaner: avoids re-downloading every time
    # 📜 Extra Tip	Sentiment works better when broken into paragraphs or sentences	Right now, you're analyzing the whole book at once
# Notes:
    # nltk.data.find() avoids re-downloading vader_lexicon every time you run the script.
    # Added a little formatting to make your output look cleaner (3 decimal places).