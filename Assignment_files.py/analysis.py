import matplotlib.pyplot as plt
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def word_frequency_analysis(filename):
    """Creates a dictionary counting how many times a words appears"""
    word_counter = {}
    with open (filename, 'r', encoding='utf-8', errors='ignore') as f: 
        for line in f:
            for word in line.split(): 
                word_counter[word] = word_counter.get(word,0)+1
        return word_counter
    


def text_summary_statistics(filename):
    """Run a statistical test on the text of the document."""
    word_counter = word_frequency_analysis(filename)
    total_words = sum(word_counter.values())
    total_characters = sum(len(w)*c for w, c in word_counter.items())
    unique_words = len(word_counter)

    avg_word_length = total_characters/total_words if total_words else 0
    vocab = unique_words/ total_words if total_words else 0

    print("\n Text Summary Statistics:\n")
    print("Total words:", total_words)
    print("Unique words:", unique_words)
    print("Average word length:", round(avg_word_length, 2))
    print("Vocabulary richness:", round(vocab, 3))

    return word_counter


def common_words_chart(filename, top_n= 10):
    """Creates a bar chart on the top 10 most used words in a text"""
    word_counter = word_frequency_analysis(filename)
    sorted_words = sorted(word_counter.items(), key= lambda x: x[1], reverse = True)[:top_n]

    words = [w for w, _ in sorted_words]   
    count = [c for _, c in sorted_words]  

    plt.figure(figsize=(15,5))  
    plt.bar (words, count) 
    plt.title(f"Top {top_n} Most Frequent Words")
    plt.xlabel("Words") 
    plt.ylabel("Count") 
    plt.xticks(rotation=45) 
    plt.show() 


def sentiment_analysis(filename):
    """Runs a Sentiment Analysis for the text """
    nltk.download('vader_lexicon', quiet=True)
    sia = SentimentIntensityAnalyzer()
    with open (filename, 'r', encoding='utf-8', errors='ignore') as f: 
        text = f.read()

    sentiment_words = sia.polarity_scores(text)

    print("   SENTIMENT ANALYSIS RESULTS    ")
    print(sentiment_words)


if __name__ == "__main__":
    text_summary_statistics('final_cleaned.txt')
    common_words_chart('final_cleaned.txt')
    sentiment_analysis('final_cleaned.txt')