from text_loader import load_text
from analyzer import (remove_stop_words, word_frequency, get_top_words, 
                      calculate_average_word_length, calculate_vocabulary_richness, 
                      get_longest_words, text_similarity, compare_book_sections)
from visualizer import create_word_frequency_chart

def main():
    url = "https://www.gutenberg.org/cache/epub/730/pg730.txt"
    

    print("Downloading and cleaning text...")
    text = load_text(url)
    
    # Display sample
    print("\nFirst 500 characters:")
    print(text[:500])
    
    # Word count
    total_words = len(text.split())
    print(f"\n\nTotal word count: {total_words}")
    
    # Remove stop words
    filtered_words = remove_stop_words(text)
    print(f"Word count after removing stop words: {len(filtered_words)}")
    
    # Word frequency analysis
    freq = word_frequency(filtered_words)
    
    # Get top 10 words
    top_words = get_top_words(freq, 10)
    
    print("\nTop 10 most frequent words:")
    for word, count in top_words:
        print(f"{word}: {count}")
    
    # SUMMARY STATISTICS 
    print("\n" + "="*60)
    print("Summary Statistics")
    print("="*60)
    
    avg_word_length = calculate_average_word_length(filtered_words)
    print(f"Average word length: {avg_word_length:.2f} characters")
    
    vocab_richness = calculate_vocabulary_richness(filtered_words)
    print(f"Vocabulary richness: {vocab_richness:.2%}")
    print("  (Higher % = more diverse vocabulary)")
    
    longest_words = get_longest_words(filtered_words, 10)
    print("\nTop 10 longest words:")
    for word, length in longest_words:
        print(f"  {word} ({length} letters)")
    
    unique_word_count = len(set(filtered_words))
    print(f"\nTotal unique words: {unique_word_count}")
    print(f"Word repetition rate: {1 - vocab_richness:.2%}")
    print("="*60)
    
    # VISUALIZATION
    create_word_frequency_chart(top_words)
    
    # TEXT SIMILARITY 
    print("\n" + "="*60)
    print("Text Similarity Analysis")
    print("="*60)
    print("Comparing different sections of Oliver Twist...")
    
    beginning, middle, end = compare_book_sections(text)
    
    print("\nComparing Beginning vs Middle:")
    similarity1 = text_similarity(beginning, middle)
    if similarity1:
        print(f"  Similarity Score: {similarity1['token_sort_ratio']}%")
    
    print("\nComparing Beginning vs End:")
    similarity2 = text_similarity(beginning, end)
    if similarity2:
        print(f"  Similarity Score: {similarity2['token_sort_ratio']}%")
    
    print("\nComparing Middle vs End:")
    similarity3 = text_similarity(middle, end)
    if similarity3:
        print(f"  Similarity Score: {similarity3['token_sort_ratio']}%")
    
    print("\nInterpretation:")
    print("- Higher percentages mean more similar text")
    print("- This shows how writing style/vocabulary changes throughout the book")
    print("="*60)

if __name__ == "__main__":
    main()