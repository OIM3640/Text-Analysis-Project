# Count word frequencies without stopwords
from nltk.corpus import stopwords
import string
def count_word_frequencies(text):
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator).lower()
    words = clean_text.split()
    stop_words = set(stopwords.words('english'))
    frequency_dict = {}
    for word in words:
        if word not in stop_words:
            frequency_dict[word] = frequency_dict.get(word, 0) + 1
    return frequency_dict

# Use main 
def main():
    # Get text from Wikipedia for Jeddah
    from mediawiki import MediaWiki
    wikipedia = MediaWiki()
    jeddah = wikipedia.page("Jeddah")
    print(jeddah.title)
    print(jeddah.summary)
    print()  # Line breaker

    # Count word frequencies
    combined_text = jeddah.title + " " + jeddah.summary
    word_frequencies = count_word_frequencies(combined_text)

    for word, freq in word_frequencies.items():
        print(f"{word}: {freq}")
    print()  # Line breaker

    #Top 5 frequent words
    from collections import Counter
    print('These are the top 5 most frequent words.')
    counter = Counter(word_frequencies)
    top_five = counter.most_common(5)
    for word, freq in top_five:
        print(f"{word}: {freq}")
    print()  # Line breaker

    # Translate top 5 words - With the help of Reddit and github
    from googletrans import Translator, LANGUAGES
    print("Most frequent words translated to Arabic:")
    translator = Translator()
    for word, freq in top_five:
        translation = translator.translate(word, dest='ar')
        print(f"Original: {word} - Translated: {translation.text}")
    print()  # Line breaker

    # Top 10 words in a bar graph - With the help of ChatGPT
    import plotly.graph_objects as go

    counter = Counter(word_frequencies)
    top_ten = counter.most_common(10)

    words, frequencies = zip(*top_ten)

    # The bar chart
    fig = go.Figure(data=[go.Bar(
                x=words,
                y=frequencies,
                text=frequencies,
                textposition='auto',  
                marker_color='rgba(68, 51, 50, 1)', 
                marker_line_color='rgb(68, 51, 50, 1)',
                opacity=1 )])

    # Customize the layout
    fig.update_layout(
        title='Top 10 Most Frequent Words in Jeddahs Wikipedia Summary',
        xaxis_title='Words',
        yaxis_title='Frequency',
        template='plotly_white', 
        plot_bgcolor='rgba(0,0,0,0)')

    fig.show()


if __name__ == "__main__":
    main()

