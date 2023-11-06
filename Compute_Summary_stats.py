import urllib.request
from collections import Counter
import nltk
from nltk.corpus import stopwords

# Download the NLTK stopwords
nltk.download('stopwords')

""" Apart from the english stopwords, I also decided to include the character list to remove because these names are highly repetitive across the play"""

# URL for "The Importance of Being Earnest" by Oscar Wilde
url = "http://www.gutenberg.org/ebooks/844.txt.utf-8"
with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')

    text_lower = text.lower()

    # List of characters from the play
    play_characters = ['jack', 'algernon', 'lady bracknell', 'gwendolen', 'cecily', 'miss prism', 'lane']
    words = text_lower.split()
    # Remove common English stopwords and character names
    stop_words = set(stopwords.words('english'))
    stop_words.update(play_characters)
    words = [word for word in words if word not in stop_words]
    word_counter = Counter(words)

    # Most frequent word calculation
    most_common_word = word_counter.most_common(1)[0]
    print(f"The most frequent word is '{most_common_word[0]}' appearing {most_common_word[1]} times.")

    # Least frequent word calculation
    least_common_word = word_counter.most_common()[:-2:-1][0]
    print(f"The least frequent word is '{least_common_word[0]}' appearing {least_common_word[1]} time.")

    # Top 10 words calculation
    top_10_words = word_counter.most_common(10)
    print("\nTop 10 words:")
    for word, count in top_10_words:
        print(f"'{word}' appears {count} times.")