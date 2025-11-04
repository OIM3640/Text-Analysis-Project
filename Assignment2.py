import urllib.request
import unicodedata
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# —————————————————————————————————————————————————————
# Download and Import Texts
import os
import urllib.request

def import_text(url, filename):
    """Download text from a Project Gutenberg URL if not already saved locally.
    
    Combines a local file check and URL download to return the text as a string.
    
    - If the file exists in the current folder, read it from disk.
    - Otherwise, download it from the URL, save it to the file, and return the text.
    """
    # If file already exists, read from disk
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    
    # Otherwise, download from the web
    try:
        with urllib.request.urlopen(url) as f:
            text = f.read().decode("utf-8")
            # Save a copy locally for next time
            with open(filename, "w", encoding="utf-8") as out:
                out.write(text)
            return text
    except Exception as e:
        print(f"An error occurred while downloading {url}:", e)
        return ""


# —————————————————————————————————————————————————————
# Text Cleaning and Preprocessing
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


def get_punctuation(lines):
    """Return a string of all unique punctuation marks in the given text."""
    punc_marks = {}
    for line in lines:
        for char in line:
            if unicodedata.category(char).startswith("P"):
                punc_marks[char] = 1
    return "".join(punc_marks)


def split_line(line):
    """Replace different dashes with spaces to avoid joining words together inaccurately."""
    return line.replace("—", " ").replace("–", " ").replace("--", " ").split()


def clean_word(word, punctuation):
    """Strip punctuation from the beginning and end of each word, convert to lowercase, and remove numbers."""
    word = word.strip(punctuation).lower()
    if any(ch.isdigit() for ch in word):
        return ""
    return word


def clean_text(lines, punctuation):
    """Return a cleaned list of words from a list of lines."""
    cleaned = []
    for line in lines:
        for word in split_line(line):
            word = clean_word(word, punctuation)
            if word != "":
                cleaned.append(word)
    return cleaned


def preprocess_text(text, start_marker, end_marker):
    """Extracts, cleans, and returns (lines, cleaned_words) using existing helper functions."""
    lines = extract_text_between_markers(text, start_marker, end_marker)
    punctuation = get_punctuation(lines)
    cleaned = clean_text(lines, punctuation)
    return lines, cleaned


# —————————————————————————————————————————————————————
# Stopword Removal
import os
import urllib.request

def load_stopwords(file_path="stopwords.txt", url=None):
    """Combines local check and URL download to return a set of stopwords.

    - Loads stopwords.txt locally if it exists.
    - Otherwise, downloads from the provided GitHub raw URL and saves it for future use.
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
        except Exception as e:
            print(f"Error downloading stopwords: {e}")
            return set()
    else:
        print("Stopwords file missing and no URL provided.")
        return set()


def remove_stopwords(cleaned, stopwords):
    """Return a list of words with stop words removed."""
    return [w for w in cleaned if w not in stopwords]


# —————————————————————————————————————————————————————
# Word Frequency Analysis
def frequencies(word_list):
    """Return a dictionary mapping each word to its frequency."""
    count = {}
    for word in word_list:
        count[word] = count.get(word, 0) + 1
    return count


def second_element(t):
    return t[1]


def print_most_common(word_counter, x, title=""):
    """Print the n most frequent words and their counts for any text."""
    items = sorted(word_counter.items(), key=second_element, reverse=True)
    print(f"\nTop {x} most common words in {title}")
    for word, freq in items[:x]:
        print(word, freq, sep="\t")


def print_unique_high_freq(source, compare, top_x_compare, top_x_display, source_title, compare_title):
    """Print the most frequent words in one text that are not among the top x words in another text."""
    sorted_compare = sorted(compare.items(), key=second_element, reverse=True)
    top_compare_set = {pair[0] for pair in sorted_compare[:top_x_compare]}
    source_unique = {w: f for w, f in source.items() if w not in top_compare_set}
    sorted_unique = sorted(source_unique.items(), key=second_element, reverse=True)

    print(f"\nTop {top_x_display} words frequent in {source_title} but not in {compare_title}'s top {top_x_compare}:")
    for word, freq in sorted_unique[:top_x_display]:
        print(word, freq, sep="\t")


# —————————————————————————————————————————————————————
# Summary Statistics
def average_word_length(word_list):
    return sum(len(w) for w in word_list) / len(word_list)


def average_sentence_length(text):
    sentences = [s.strip() for s in text.split(".") if s.strip()]
    return len(text.split()) / len(sentences)


def type_token_ratio(word_list):
    return len(set(word_list)) / len(word_list) if word_list else 0


# —————————————————————————————————————————————————————
# Visualization
def plot_barchart(word_counter, n=10, title=""):
    sorted_items = sorted(word_counter.items(), key=lambda x: x[1], reverse=True)[:n]
    words, freqs = zip(*sorted_items)
    plt.bar(words, freqs, color="Blue")
    plt.title(f"Top {n} Most Frequent Words in {title}")
    plt.xlabel("Word")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()


def plot_wordcloud(word_counter, title="", color=""):
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

    # Display it for testing
    # plt.show()


# —————————————————————————————————————————————————————
# Natural Language Processing
# Sentiment Analysis of Novel Endings
def ending_sentiment(text_raw, title, sia):
    sentences = [s.strip() for s in text_raw.split(".") if s.strip()]
    ending_sentences = sentences[-10:]
    scores = [sia.polarity_scores(s) for s in ending_sentences]
    avg_scores = {
        k: round(sum(score[k] for score in scores) / len(scores), 4)
        for k in scores[0]
    }
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
    
    # Too long, commented out for convenience
    # print(len(cleaned_frank))
    
    # Dracula
    lines_drac, cleaned_drac = preprocess_text(text_drac, "How these papers", "/Jonathan Harker./")

    # Too long, co mmented out for convenience
    # print(len(cleaned_drac))

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