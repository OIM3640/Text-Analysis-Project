# Importing standard Python libraries
import urllib.request # Used to download the book text from the internet
import pickle  # Used to save and load text locally (for efficiency and avoiding repeated downloads)
import re # Regular expressions module used for text cleaning
import os  # Helps access environment variables and file paths
import string  # Helps access environment variables and file paths
from collections import Counter # For counting word frequencies
import nltk # Natural Language Toolkit for language processing utilities
from nltk.corpus import stopwords
import openai # External libraries for AI interaction and environment variable management
import requests # Not directly used but often useful for HTTP requests
from openai import OpenAI
from dotenv import load_dotenv # Loads environment variables from a .env file (like API keys)

# Download stopwords if needed
nltk.download('stopwords')

# URL and pickle file path
url = 'https://www.gutenberg.org/cache/epub/730/pg730.txt'
pickle_file = "book_text.pkl"

# OpenAI API Key
load_dotenv()
APIKEY = os.getenv("OPENAI_API_KEY")

# Code used from Session about OpenAI API
def get_openai_response(user_prompt):
    client = OpenAI() 

    system_prompt = " You are a helpful assistant for learning Python programming" 
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[{
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_prompt
        }]
    )
    return completion.choices[0].message.content

# === Function to download raw book text from the internet ===
def download_text(url):
    try:
        with urllib.request.urlopen(url) as f:
            text = f.read().decode('utf-8')
        return text
    except Exception as e:
        print("Error downloading file:", e)
        return None

# === Function to clean and prepare the downloaded text ===
def clean_text(text):
    # Project Gutenberg texts have boilerplate info at the beginning and end — this trims it
    start_marker = "*** START OF THIS PROJECT GUTENBERG EBOOK"
    end_marker = "*** END OF THIS PROJECT GUTENBERG EBOOK"
    
    start_idx = text.find(start_marker)
    end_idx = text.find(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        text = text[start_idx + len(start_marker):end_idx].strip()
    
    # Remove punctuation and numbers, make everything lowercase
    text = re.sub(r'[^a-zA-Z\s]', '', text).lower()

    # Preview of cleaned text (useful for debugging or confirmation)
    print("\n=== Preview of cleaned text ===\n")
    print(text[:500])
    print("\n=== End preview ===\n")
        
    return text

# === Save cleaned text to a local file using pickle ===
def save_text(text, filename=pickle_file):
    with open(filename, "wb") as f:
        pickle.dump(text, f)

# === Load previously saved text from local pickle file ===
def load_text(filename=pickle_file):
    with open(filename, "rb") as f:
        return pickle.load(f)

# === Generate word frequencies from text (minus stopwords) ===
def word_frequencies(text, top_n=20):
    words = text.split()
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    freq_dict = Counter(filtered_words)

    # Print top 50 frequent words for context
    print("\n=== Full Word Frequencies ===")
    for word, count in freq_dict.most_common(50):
        print(f"{word}: {count}")
    print("=== End of Frequencies ===\n")

    return freq_dict

# === Display top N frequent words ===
def display_top_words(freq_dict, n=10):
    top_words = freq_dict.most_common(n)
    print(f"\nTop {n} words in the text:")
    for word, freq in top_words:
        print(f"{word}: {freq}")

# === Show additional statistics about the text ===
def show_additional_stats(freq_dict):
    unique_words = len(freq_dict)
    avg_len = sum(len(w)*f for w,f in freq_dict.items()) / sum(freq_dict.values())
    longest = max(freq_dict, key=len)
    print(f"\n--- Additional Stats ---")
    print(f"Unique Words: {unique_words}")
    print(f"Average Word Length: {avg_len:.2f}")
    print(f"Longest Word: {longest}")
    print(f"Words Occurring Only Once: {sum(1 for w in freq_dict.values() if w == 1)}")

# === Generate a dad joke based on the book ===
# AI-generated feature (suggested by ChatGPT) that adds humor using the book content
def generate_book_joke(book_text):
    joke_prompt = f"Create a dad joke based on the story of Oliver Twist. It should reference a character or event from the story. Here is an excerpt from the text: {book_text[:200]}"

    joke_response = get_openai_response(joke_prompt)
    # Uses ChatGPT for joke generation
    return joke_response

# === Stylized rewrite of the text ===
# Another AI-enhanced optional feature — not required in the original instructions but added creatively
def rewrite_in_neuromancer_style(text):
    print("\n=== Neuromancer Style Rewrite Preview ===")
    neuromancer_prompt = f"Rewrite the following text in the style of Neuromancer by William Gibson. Keep the language cyberpunk and futuristic. Text: {text[:300]}"
    neuromancer_response = get_openai_response(neuromancer_prompt)
    print(neuromancer_response)
    print("\n=== End of Rewrite ===")

# === Main program logic ===
def main():
    # Check if we already saved a cleaned version of the book to avoid re-downloading
    if not os.path.exists(pickle_file):
        print("Downloading and cleaning text...")
        raw_text = download_text(url)
        if raw_text:
            cleaned_text = clean_text(raw_text)
            save_text(cleaned_text)
            print("Text saved successfully.\n")
    else:
        print("Using existing cleaned text...\n")

    # Load text from pickle file
    text = load_text()
    # Get frequency of words and show top 10
    freq_dict = word_frequencies(text) 
    display_top_words(freq_dict, n=10)

    # Show additional statistics about the text
    show_additional_stats(freq_dict)

    # Generate and print a dad joke related to the book - AI suggested
    joke = generate_book_joke(text)
    print(f"\n=== Bonus Book-Related Dad Joke ===\n{joke}\n=== End Joke ===")

    # Neuromancer style rewrite 
    rewrite_in_neuromancer_style(text)

if __name__ == "__main__":
    main()
