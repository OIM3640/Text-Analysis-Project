import os
import urllib.request
import unicodedata
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# —————————————————————————————————————————————————————
# Download and Import Texts
def import_text(url, filename):
    """
    Use text from Project Gutenberg.
    
    If the file exists in the folder, read it from disk.
    Otherwise, download it from the URL, save it to the file, and return the text as a string.
    """
    # If file already exists, read from disk
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    
    # Otherwise, download from the link
    try:
        with urllib.request.urlopen(url) as f:
            text = f.read().decode("utf-8")
            # Save a copy locally for next time
            with open(filename, "w", encoding="utf-8") as out:
                out.write(text)
            return text
        
    # Print an error message if download fails
    except Exception as e:
        print(f"An error occurred while downloading {url}:", e)
        return ""


# —————————————————————————————————————————————————————
# Text Cleaning and Preprocessing
def extract_text_between_markers(text, start_marker, end_marker):
    """Return only the lines between the given start and end markers, which are the first and last line of the novel, excluding the title page and any transcriber's notes."""
    lines = []
    copy = False
    for line in text.splitlines():
        
        # After finding and appending the first line, start copying
        if start_marker in line:
            lines.append(line)
            copy = True
            continue
        
        # After finding the last line, append it and stop reading lines
        if end_marker in line:    
            lines.append(line)
            break

        # If copy is True, append the line
        if copy:
            lines.append(line)
    return lines


def get_punctuation(lines):
    """Return a string of all unique punctuation marks in the given text."""
    punc_marks = {}
    for line in lines:
        for char in line:
            if unicodedata.category(char).startswith("P"):
                punc_marks[char] = 1
    return "".join(punc_marks)


def split_line(line):
    """
    Replace em, en, and double dashes with spaces to avoid joining words together when they should not be.
    
    Returns a list of words.
    """
    return line.replace("—", " ").replace("–", " ").replace("--", " ").split()


def clean_word(word, punctuation):
    """Strip punctuation from the beginning and end of each word and convert to lowercase.
    
    Returns the cleaned word.
    """
    word = word.strip(punctuation).lower()
    return word


def clean_text(lines, punctuation):
    """Returns a cleaned list of words."""
    cleaned = []
    for line in lines:
        for word in split_line(line):
            word = clean_word(word, punctuation)

            # Don't append empty strings
            if word != "":
                cleaned.append(word)
    return cleaned


def preprocess_text(text, start_marker, end_marker):
    """Extracts, cleans, and returns a list of sentences and a cleaned list of words."""
    lines = extract_text_between_markers(text, start_marker, end_marker)
    punctuation = get_punctuation(lines)
    cleaned = clean_text(lines, punctuation)
    return lines, cleaned


# —————————————————————————————————————————————————————
# Removing Stop Words
import os
import urllib.request

def load_stopwords(file_path="stopwords.txt", url=None):
    """
    Loads stopwords.txt locally if it exists.
    Otherwise, downloads it from the provided URL and saves it.
    """
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return set(f.read().split())

    if url:
        try:
            with urllib.request.urlopen(url) as f:
                text = f.read().decode("utf-8")
            with open(file_path, "w", encoding="utf-8") as out:
                out.write(text)
            return set(text.split())
        
        # Print an error message if download fails
        except Exception as e:
            print(f"Error downloading stopwords: {e}")
            return set()
        
    # Print a message if no URL is provided
    else:
        print("Stopwords file missing and no URL provided.")
        return set()


def remove_stopwords(cleaned, stopwords):
    """
    Return a list of words with stop words removed.
    """

    # For each word in cleaned, include it only if it's not in stopwords
    filtered = []
    for word in cleaned:
        if word not in stopwords:
            filtered.append(word)
    return filtered


# —————————————————————————————————————————————————————
# Word Frequency Analysis
def frequencies(word_list):
    """
    Return a dictionary with the words as keys and their frequencies as values.
    """
    count = {}
    for word in word_list:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    # print(count) # Long output, commented out for convenience
    return count


# —————————————————————————————————————————————————————
# Summary Statistics

# -----------------------------------------------------
# Top X Most Frequent Words
def second_element(item):
    """
    Return the second element in a list.
    Will be used to sort words by frequency.
    """
    return item[1]


def print_most_common(word_counter, x, title=""):
    """
    Print the x most frequent words and their counts for a text.
    """
    # Sort the items in word_counter (word-frequency pairs) by frequency (second element) in descending order
    items = sorted(word_counter.items(), key=second_element, reverse=True)
    print(f"\nTop {x} most common words in {title}")
    
    # For the top x items, print the word and its frequency
    for word, freq in items[:x]:

        # Add a tab between the word and its freq for clarity
        print(word, freq, sep="\t")

# -----------------------------------------------------
# Words that Appear Frequently in One Text but Not the Other (Not Within the Top X Words)
def print_unique_high_freq(source, compare, top_x_compare, top_x_display, source_title, compare_title):
    """
    Print the most frequent words in one text (source) that are not among the top x words in another text (compare).
    """
    # Sort the compared text's words by frequency
    sorted_compare = sorted(compare.items(), key=second_element, reverse=True)

    # Take only the word part of the top x word-frequency pairs in the compared text, since frequency will not be needed any further
    top_compare_set = set()
    for pair in sorted_compare[:top_x_compare]:
        top_compare_set.add(pair[0])

    # If the word is not in the compared text, add it to a new dictionary that has the words as keys and frequencies as values
    source_unique = {}
    for word, freq in source.items():
        if word not in top_compare_set:
            source_unique[word] = freq
    
    # Sort the source text's words by frequency
    sorted_unique = sorted(source_unique.items(), key=second_element, reverse=True)

    # Print the results
    print(f"\nTop {top_x_display} words frequent in {source_title} but not in {compare_title}'s top {top_x_compare}:")
    for word, freq in sorted_unique[:top_x_display]:
        print(word, freq, sep="\t")

# -----------------------------------------------------
# Average Word Length and Words per Sentence
def average_word_length(word_list):
    """
    Return the average number of characters per word in the text.
    """
    # Divide the total number of characters by the number of words
    total_length = 0
    for word in word_list:
        total_length += len(word)
    return total_length / len(word_list)


def average_sentence_length(text):
    """
    Return the average number of words per sentence.
    """
    sentences = []

    # For this program, sentences will be considered the text between two periods also how doe sthe follllwoing code work
    for s in text.split("."):

        # Clean the sentences and store them in a list
        if s.strip():
            sentences.append(s.strip())

    # Divide the total number of words by the total number of sentences
    # len(text.split()) gives the total number of words, len(sentences) gives the total number of sentences
    return len(text.split()) / len(sentences)


# -----------------------------------------------------
# Vocabulary Richness (TTR)
def type_token_ratio(word_list):
    """
    Return the type-token ratio (TTR) for the text.

    The TTR is a measure of vocabulary richness.
    It is calculated by dividing the number of unique words
    by the total number of words in the text.
    """
    # If the list is empty, return 0 to avoid division by zero
    if len(word_list) == 0:
        return 0

    # Find the number of unique words by converting the list to a set
    unique_words = set(word_list)

    # Divide the number of unique words by the total number of words
    return len(unique_words) / len(word_list)


# —————————————————————————————————————————————————————
# Visualization (I had a lot of AI help for this section)
def plot_barchart(word_counter, n=10, title=""):
    """
    Plot a vertical bar chart showing the most frequent words in a text using matplotlib.

    word_counter: A dictionary where each key is a word and each value is its frequency count.
    """
    sorted_items = sorted(word_counter.items(), key=lambda x: x[1], reverse=True)[:n]
    words, freqs = zip(*sorted_items)
    plt.bar(words, freqs, color="Blue")
    plt.title(f"Top {n} Most Frequent Words in {title}")
    plt.xlabel("Word")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()


def plot_wordcloud(word_counter, title="", color=""):
    """
    Display a word cloud visualization for a given word frequency dictionary.
    """
    wc = WordCloud(width=800, height=400, background_color="white", colormap=color, max_words=150)
    wc.generate_from_frequencies(word_counter)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title(f"Word Cloud for {title}")


# Add parameters to increase reusability
def plot_dashboard(count_frank, count_drac, save_path="images/dashboard.png"):
    """Create and display a two-by-two dashboard comparing Frankenstein and Dracula word frequencies.

    Combines plot_barchart and plot_wordcloud, then saves the figure to the images folder.
    """
    # Create a two-by-two plot dashboard
    fig, subplots = plt.subplots(2, 2, figsize=(14, 10))

    # Frankenstein Top Words
    plt.sca(subplots[0, 0])
    plot_barchart(count_frank, n=10, title="Frankenstein")

    # Frankenstein Word Cloud
    plt.sca(subplots[1, 0])
    plot_wordcloud(count_frank, "Frankenstein", color="Greens")

    # Dracula Top Words
    plt.sca(subplots[0, 1])
    plot_barchart(count_drac, n=10, title="Dracula")

    # Dracula Word Cloud
    plt.sca(subplots[1, 1])
    plot_wordcloud(count_drac, "Dracula", color="Reds")

    # Adjust layout to prevent overlap
    plt.tight_layout(pad=3.0)
    plt.subplots_adjust(hspace=0.4)

    # Ensure the directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Save the figure if it doesn't exist yet
    plt.savefig(save_path, dpi=300, bbox_inches="tight")

    # Display the full dashboard for testing
    # plt.show()


# —————————————————————————————————————————————————————
# Natural Language Processing
def ending_sentiment(text_raw, title, sia):
    """
    Conduct sentiment analysis for the text's ending, defined as the last 10 sentences.
    """
    # Split the full text into individual sentences by periods, removing any empty strings or extra spaces
    sentences = [s.strip() for s in text_raw.split(".") if s.strip()]

    # Only use the last 10 sentences for the analysis
    # The sentiment analyzer performs better on shorter text samples
    ending_sentences = sentences[-10:]

    # Get the sentiment scores for each of the last 10 sentences
    scores = [sia.polarity_scores(s) for s in ending_sentences]

    # Calculate the average sentiment for each category across the 10 sentences
    avg_scores = {
        k: round(sum(score[k] for score in scores) / len(scores), 4)
        for k in scores[0]
    }

    # Print the average sentiment results for the text's ending
    print(f"\nAverage sentiment for the ending of {title}:")
    print(avg_scores)


# —————————————————————————————————————————————————————
# Main Function
def main():
    # *Frankenstein*
    text_frank = import_text("https://www.gutenberg.org/cache/epub/42324/pg42324.txt", "pg42324.txt")

    # *Dracula*
    text_drac = import_text("https://www.gutenberg.org/cache/epub/45839/pg45839.txt", "pg45839.txt")

    # —————————————————————————————————————————————————————
    # Text Cleaning and Preprocessing
    # Frankenstein
    lines_frank, cleaned_frank = preprocess_text(text_frank, "INTRODUCTION.", "THE END.")
    
    # Dracula
    lines_drac, cleaned_drac = preprocess_text(text_drac, "How these papers", "/Jonathan Harker./")

    # —————————————————————————————————————————————————————
    # Removing Stop Words
    # Load stopwords (downloads if missing)
    stopwords = load_stopwords(
        "stopwords.txt",
        url="https://raw.githubusercontent.com/OIM3640/resources/main/code/data/stopwords.txt"
    )

    # Add custom stopwords
    custom_stopwords = {
        "one", "now", "upon", "every",
        "must", "might", "shall", "us",
        "yet", "will", "can"
    }
    stopwords.update(custom_stopwords)


    # Frankenstein
    final_frank = remove_stopwords(cleaned_frank, stopwords)
    print(len(final_frank))

    # Dracula
    final_drac = remove_stopwords(cleaned_drac, stopwords)
    print(len(final_drac))

    # —————————————————————————————————————————————————————
    # Word Frequency Analysis
    count_frank = frequencies(final_frank)
    count_drac = frequencies(final_drac)

    # —————————————————————————————————————————————————————
    # Computing Summary Statistics

    # ***Top n Most Frequent Words***
    print_most_common(count_frank, 10, "Frankenstein")
    print_most_common(count_drac, 10, "Dracula")

    # ***Words that Appear Frequently in One Text but Not the Other***
    print_unique_high_freq(count_frank, count_drac, 20, 10, "Frankenstein", "Dracula")
    print_unique_high_freq(count_drac, count_frank, 20, 10, "Dracula", "Frankenstein")

    # ***Average Word and Sentence Length***
    text_frank_raw = "\n".join(lines_frank)
    text_drac_raw = "\n".join(lines_drac)

    # Frankenstein
    avg_word_len_frank = average_word_length(final_frank)
    avg_sent_len_frank = average_sentence_length(text_frank_raw)

    print("Average word length - Frankenstein:", round(avg_word_len_frank, 2))
    print("Average words per sentence length - Frankenstein:", round(avg_sent_len_frank, 2))

    # Dracula
    avg_word_len_drac = average_word_length(final_drac)
    avg_sent_len_drac = average_sentence_length(text_drac_raw)
    
    print("Average word length - Dracula:", round(avg_word_len_drac, 2))
    print("Average words per sentence length - Dracula:", round(avg_sent_len_drac, 2))

    # ***Vocabulary Richness***
    # Frankenstein
    ttr_frank = type_token_ratio(final_frank)
    print("TTR - Frankenstein:", round(ttr_frank, 2))

    # Dracula
    ttr_drac = type_token_ratio(final_drac)
    print("TTR - Dracula:", round(ttr_drac, 2))

    # —————————————————————————————————————————————————————
    # Visualization Dashboard
    plot_dashboard(count_frank, count_drac)

    # —————————————————————————————————————————————————————
    # Sentiment Analysis
    sia = SentimentIntensityAnalyzer()

    # Frankenstein
    ending_sentiment(text_frank_raw, "Frankenstein", sia)

    # Dracula
    ending_sentiment(text_drac_raw, "Dracula", sia)


if __name__ == "__main__":
    main()