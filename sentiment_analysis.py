import urllib.request
from textblob import TextBlob

"""Because we do not have th page numbers from the UTF format, I decided to ask ChatGPT to breakdown the text into 4 parts based on character count"""

# URL for "The Importance of Being Earnest" by Oscar Wilde
url = "http://www.gutenberg.org/ebooks/844.txt.utf-8"
with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')

    # Splitting the text into four parts
    total_words = len(text.split())
    segment_size = total_words // 4
    segments = []
    start = 0
    for i in range(3):
        segment = text.split()[start:start+segment_size]
        segments.append(' '.join(segment))
        start += segment_size

    # The last segment includes the remaining words
    segments.append(' '.join(text.split()[start:]))

    # sentiment analysis being perfomrd for each segment
    for i, segment in enumerate(segments):
        blob = TextBlob(segment)
        sentiment = blob.sentiment

        print(f"Sentiment analysis for segment {i+1}:")
        print(f"Overall sentiment polarity: {sentiment.polarity}")
        if sentiment.polarity > 0:
            print("The segment is generally positive.")
        elif sentiment.polarity < 0:
            print("The segment is generally negative.")
        else:
            print("The segment is neutral.")
        print()