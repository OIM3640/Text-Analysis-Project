# Import text
import urllib.request

def import_text(url):
    """Download text from a Project Gutenberg URL and return it as a string."""
    try:
        with urllib.request.urlopen(url) as f:
            text = f.read().decode('utf-8')
            return text
    except Exception as e:
        print(f"An error occurred while downloading {url}:", e)
        return ""

# *Frankenstein*
text_frank = import_text("https://www.gutenberg.org/cache/epub/42324/pg42324.txt")


# *Dracula*
text_drac = import_text("https://www.gutenberg.org/cache/epub/45839/pg45839.txt")

# —————————————————————————————————————————————————————
# Text Cleaning and Preprocessing
import unicodedata

# Remove the Project Gutenberg header and footer
def extract_text_between_markers(text, start_marker, end_marker):
    """Return only the lines between the given start and end markers."""
    lines = []
    copy = False

    for line in text.splitlines():
        if start_marker in line:
            lines.append(line)
            copy = True
            continue
        if end_marker in line:
            lines.append(line)
            break
        if copy:
            lines.append(line)

    return lines

# Manage punctuation: taken from Chapter 12 Notebook
def get_punctuation(lines):
    """Return a string of all unique punctuation marks in the given text."""
    punc_marks = {}
    for line in lines:
        for char in line:
            category = unicodedata.category(char)
            if category.startswith('P'):
                punc_marks[char] = 1
    return ''.join(punc_marks)

def split_line(line):
    """Replace different dashes with spaces to avoid joining words together inaccurately."""
    return line.replace('—', ' ').replace('–', ' ').replace('--', ' ').split()

def clean_word(word, punctuation):
    """Strip punctuation from the beginning and end of each word, convert to lowercase, and remove numbers."""
    word = word.strip(punctuation).lower()
    if any(ch.isdigit() for ch in word):
        return ""
    return word

def clean_text(lines, punctuation):
    """UseReturn a cleaned list of words from a list of lines."""
    cleaned = []
    for line in lines:
        for word in split_line(line):
            word = clean_word(word, punctuation)
            if word != "":
                cleaned.append(word)
    return cleaned

# *Frankenstein*
# Get the main content of Frankenstein
lines_frank = extract_text_between_markers(text_frank, "INTRODUCTION.", "THE END.")

# Get punctuation marks from the text
punctuation = get_punctuation(lines_frank)

# Generate cleaned list of words
cleaned_frank = clean_text(lines_frank, punctuation)

# Check: there are 77935 words total after cleaning
print(len(cleaned_frank))


# *Dracula*
# Similar cleaning process for Dracula
# Get the main content of Frankenstein
lines_drac = extract_text_between_markers(text_drac, "How these papers", "/Jonathan Harker./")

# Get punctuation marks from the text
punctuation = get_punctuation(lines_drac)

# Generate cleaned list of words
cleaned_drac = clean_text(lines_drac, punctuation)

# Check total word count
print(len(cleaned_drac))


# —————————————————————————————————————————————————————
# Removing Stop Words

# Create a set containing the stop words from stopwords.txt
with open("stopwords.txt", "r", encoding="utf-8") as f:
    stopwords = set(f.read().split())

def remove_stopwords(cleaned):
    """Return a list of words with stop words removed."""
    filtered = []
    for word in cleaned:
        if word not in stopwords:   # uses global variable directly
            filtered.append(word)
    return filtered

# *Frankenstein*
# Remove stop words
final_frank = remove_stopwords(cleaned_frank)

# Check: there are 36015 words total after removing stop words
print(len(final_frank))


# *Dracula*
# Remove stop words
final_drac = remove_stopwords(cleaned_drac)

# Check total word count after removing stop words
print(len(final_drac))


# —————————————————————————————————————————————————————
# Word Frequency Analysis
def frequencies(word_list):
    """Return a dictionary mapping each word to its frequency."""
    count = {}
    for word in word_list:
        count[word] = count.get(word, 0) + 1
    return count


# *Frankenstein*
# Use the word list with no stop words to find word frequencies
count_frank = frequencies(final_frank)

# Too long, so commented out for convenience
# print(count_frank)


# *Dracula*
# Use the word list with no stop words to find word frequencies
count_drac = frequencies(final_drac)

# Too long, so commented out for convenience
# print(word_counter_drac)


# —————————————————————————————————————————————————————
# Computing Summary Statistics

# ------------------------------------------------------
# ***Top n Most Frequent Words***
def second_element(t):
    """Return the second element of the word, freq tuple, which is the frequency."""
    return t[1]

def print_most_common(word_counter, x, title=""):
    """Print the n most frequent words and their counts for any text."""
    # Sort the dictionary by frequency (highest first)
    items = sorted(word_counter.items(), key=second_element, reverse=True)
    
    # Print the top x words
    print(f"\nTop {x} most common words in {title}")
    for word, freq in items[:x]:
        print(word, freq, sep='\t')

# *Frankenstein*
print_most_common(count_frank, 10, "Frankenstein")

# *Dracula*
print_most_common(count_drac, 10, "Dracula")


# ***Words that Appear Frequently in One Text but Not the Other***
def print_unique_high_freq(source, compare, top_x_compare=20, top_x_display=10, source_title="", compare_title=""):
    """Print the most frequent words in one text that are not among the top x words in another text."""
    # Sort the comparison dictionary by frequency
    sorted_compare = sorted(compare.items(), key=second_element, reverse=True)

    # Take only the top x words from the comparison
    words_compare = sorted_compare[:top_x_compare]

    # Save just the words into a set, since frequency for the comparison words is not needed anymore
    top_compare_set = {pair[0] for pair in words_compare}

    # Build a dictionary of words from the source text that aren’t in the comparison text’s top x words
    source_unique = {}
    for word, freq in source.items():
        if word not in top_compare_set:
            source_unique[word] = freq

    # Sort the new dictionary by frequency
    sorted_unique = sorted(source_unique.items(), key=second_element, reverse=True)

    # Print the results
    print(f"\nTop {top_x_display} words frequent in {source_title} but not in {compare_title}'s top {top_x_compare}:")
    for word, freq in sorted_unique[:top_x_display]:
        print(word, freq, sep='\t')


# Words in Frankenstein but not in Dracula (not within the top 20 words)
print_unique_high_freq(count_frank, count_drac, 20, 10, "Frankenstein", "Dracula")

# Words in Dracula but not in Frankenstein (not within the top 20 words)
print_unique_high_freq(count_drac, count_frank, 20, 10, "Dracula", "Frankenstein")

# ------------------------------------------------------
# ***Average Word Length and Sentence Length***
def average_word_length(word_list):
    """Return the average number of characters per word in a list of words."""
    total_len = sum(len(w) for w in word_list)
    return total_len / len(word_list)

def average_sentence_length(text):
    """Return the average number of words per sentence using periods as separator."""
    sentences = text.split('.')
    sentences = [s.strip() for s in sentences if s.strip() != ""]
    sentence_count = len(sentences)
    word_count = len(text.split())
    return word_count / sentence_count

# *Frankenstein*
avg_word_len_frank = average_word_length(final_frank)

# Use lines_frank as the base, since it contains the original sentences
text_frank_raw = "\n".join(lines_frank)   # new line for each sentence
avg_sent_len_frank = average_sentence_length(text_frank_raw)

print("Average word length - Frankenstein:", round(avg_word_len_frank, 2))
print("Average words per sentence length - Frankenstein:", round(avg_sent_len_frank, 2))

# *Dracula*
avg_word_len_drac = average_word_length(final_drac)

# Use lines_drac as the bse, since it contains the original sentences
text_drac_raw = "\n".join(lines_drac)   # new line for each sentence
avg_sent_len_drac = average_sentence_length(text_drac_raw)

print("Average word length - Dracula:", round(avg_word_len_drac, 2))
print("Average words per sentence length - Dracula:", round(avg_sent_len_drac, 2))

# ------------------------------------------------------
# ***Vocabulary Richness in Frankenstein vs Dracula***
def type_token_ratio(word_list):
    """Return the type-token ratio of a list of words (unique words / total words)."""
    if len(word_list) == 0:
        return 0
    return len(set(word_list)) / len(word_list)

# *Frankenstein*
ttr_frank = type_token_ratio(final_frank)
print("TTR - Frankenstein:", round(ttr_frank, 2))

# *Dracula*
ttr_drac = type_token_ratio(final_drac)
print("TTR - Dracula:", round(ttr_drac, 2))


# —————————————————————————————————————————————————————
# Data Visualization (I got AI help for many parts of this section)
import matplotlib.pyplot as plt
import wordcloud
from wordcloud import WordCloud

# Barchart
def plot_barchart(word_counter, n=10, title=""):
    """Plot a bar chart of the top N most frequent words."""
    sorted_items = sorted(word_counter.items(), key=lambda x: x[1], reverse=True)[:n]
    # Zip separates the words and frequencies into two lists so we can plot them
    words, freqs = zip(*sorted_items)

    # Barchart with words on the x-axis and frequencies on the y-axis
    plt.bar(words, freqs, color="skyblue")

    # Add the labels and make sure the labels don't overlap
    plt.title(f"Top {n} Most Frequent Words in {title}")
    plt.xlabel("Word")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45, ha="right")

    # Make sure everything fits properly
    plt.tight_layout()

# Word Cloud
def plot_wordcloud(word_counter, title="", color=""):
    """Display a word cloud for a word frequency dictionary."""
    wc = WordCloud(
        width=800,
        height=400,
        background_color="white",
        colormap=color,
        max_words=150
    )
    
    # Generate the word cloud from frequencies
    wc.generate_from_frequencies(word_counter)

    # Clean up the display by smoothening the edges of the words, hiding the axes, and creating a title
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.title(f"Word Cloud for {title}")

# Create a two-by-two plot dashboard
# plt.subplots() builds the entire figure and its grid of subplots together, returning both "fig" (the full canvas) and "subplots" (the individual plot areas)
fig, subplots = plt.subplots(2, 2, figsize=(14, 10))

# Plot each of the four visualizations in a specific subplot area
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

# Adjust layout to prevent overlap by adding padding
plt.tight_layout(pad=3.0)
plt.subplots_adjust(hspace=0.4)

# Display the final dashboard
plt.show()


# —————————————————————————————————————————————————————
# Natural Language Processing

# ——————————————————————————————————————————————
# Natural Language Processing (NLP) — Sentiment Analysis using NLTK
# ——————————————————————————————————————————————

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Download VADER sentiment model (only needs to run once)
nltk.download('vader_lexicon')

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Combine cleaned text lines into full strings
text_frank_full = "\n".join(lines_frank)
text_drac_full  = "\n".join(lines_drac)

# Get sentiment scores for each novel
sent_frank = sia.polarity_scores(text_frank_full)
sent_drac  = sia.polarity_scores(text_drac_full)

# Print sentiment scores
print("Frankenstein sentiment scores:", sent_frank)
print("Dracula sentiment scores:", sent_drac)

# ——————————————————————————————————————————————
# Visualization: Compare Sentiment Scores
# ——————————————————————————————————————————————

labels = ["Negative", "Neutral", "Positive", "Compound"]
frank_values = [sent_frank["neg"], sent_frank["neu"], sent_frank["pos"], sent_frank["compound"]]
drac_values  = [sent_drac["neg"], sent_drac["neu"], sent_drac["pos"], sent_drac["compound"]]

x = range(len(labels))
width = 0.35

plt.figure(figsize=(8, 5))
plt.bar([i - width/2 for i in x], frank_values, width, label="Frankenstein", color="green")
plt.bar([i + width/2 for i in x], drac_values, width, label="Dracula", color="darkred")

plt.xticks(x, labels)
plt.ylabel("Sentiment Score")
plt.title("Sentiment Comparison: Frankenstein vs Dracula (VADER Analysis)")
plt.legend()
plt.tight_layout()
plt.show()

