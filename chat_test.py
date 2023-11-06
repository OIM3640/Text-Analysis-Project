def word_frequency(text):
    # Split the text into words by whitespace and punctuation
    words = text.split()
    
    # Initialize an empty dictionary to store word frequencies
    word_count = {}

    # Iterate through the words and count their frequencies
    for word in words:
        # Convert the word to lowercase to ensure case-insensitive counting
        word = word.lower()
        
        # Remove any non-alphabetic characters from the word
        word = ''.join(filter(str.isalpha, word))
        
        # Update the word count dictionary
        if word:
            word_count[word] = word_count.get(word, 0) + 1

    return word_count

# Example usage
text = "This is a simple example. This is another example."
word_counts = word_frequency(text)
for word, count in word_counts.items():
    print(f"{word}: {count}")
