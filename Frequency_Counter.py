import urllib.request

""" In the frequency counter, I chose a specific set of words as I quickly re-skimmed the play to analyse. Additionally, I wanted to see which character was the most popular and included that in the count list"""

# URL for "The Importance of Being Earnest" by Oscar Wilde
url = "http://www.gutenberg.org/ebooks/844.txt.utf-8"
with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')

    # Convert text to lowercase to ensure case-insensitive word count
    text_lower = text.lower()

    # Split the text into words
    words = text_lower.split()

    # List of words to count
    words_to_count = ['earnest', 'skeptic', 'obliged', 'boring', 'truth']

    # Count the occurrences of the specified words
    word_counts = {word: words.count(word) for word in words_to_count}

    # Character names to count
    characters_to_count = ['jack', 'algernon', 'lady bracknell', 'gwendolen', 'cecily', 'miss prism', 'lane']

    # Count the occurrences of the specified characters
    character_counts = {character: text_lower.count(character) for character in characters_to_count}

    # Display the counts for chosen words
    for word, count in word_counts.items():
        print(f"The word '{word}' appears {count} times in the text.")

     # Display the counts for characters
    for character, count in character_counts.items():
        print(f"The character '{character.capitalize()}' appears {count} times in the text.")