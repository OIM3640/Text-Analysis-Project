from text_loader import load_text
from analyzer import (remove_stop_words, word_frequency, get_top_words, 
                      calculate_average_word_length, calculate_vocabulary_richness, 
                      get_longest_words, sentiment_analysis, text_similarity, 
                      compare_book_sections)
from visualizer import create_word_frequency_chart

def analyze_single_book(url, title):
    """Analyze a single book and return statistics"""
    print(f"\nAnalyzing {title}...")
    print("-" * 60)
    
    text = load_text(url)
    
    if not text:
        print(f"Failed to load {title}")
        return None
    
    # Remove stop words
    filtered_words = remove_stop_words(text)
    
    #  frequency analysis
    freq = word_frequency(filtered_words)
    
    
    stats = {
        'title': title,
        'text': text,
        'filtered_words': filtered_words,
        'frequency': freq,
        'total_words': len(text.split()),
        'filtered_word_count': len(filtered_words),
        'unique_words': len(set(filtered_words)),
        'avg_word_length': calculate_average_word_length(filtered_words),
        'vocab_richness': calculate_vocabulary_richness(filtered_words),
        'top_words': get_top_words(freq, 20)
    }
    
    return stats

def compare_multiple_books():
    """Compare multiple Charles Dickens books"""
    print("\n" + "="*60)
    print("COMPARING MULTIPLE CHARLES DICKENS NOVELS")
    print("="*60)
    
    books = {
        'Oliver Twist': 'https://www.gutenberg.org/cache/epub/730/pg730.txt',
        'A Tale of Two Cities': 'https://www.gutenberg.org/cache/epub/98/pg98.txt',
        'Great Expectations': 'https://www.gutenberg.org/cache/epub/1400/pg1400.txt'
    }
    
    book_stats = {}
    
    # Analyze each book
    for title, url in books.items():
        stats = analyze_single_book(url, title)
        if stats:
            book_stats[title] = stats
            print(f"✓ {title} analyzed successfully")
    
    # Comparison Summary
    print("\n" + "="*60)
    print("Cross-Book Comparison Summary")
    print("="*60)
    
    for title, stats in book_stats.items():
        print(f"\n{title}:")
        print(f"  Total words (original): {stats['total_words']:,}")
        print(f"  Words after stop word removal: {stats['filtered_word_count']:,}")
        print(f"  Unique words: {stats['unique_words']:,}")
        print(f"  Vocabulary richness: {stats['vocab_richness']:.2%}")
        print(f"  Average word length: {stats['avg_word_length']:.2f} characters")
        print(f"  Top 3 words: ", end="")
        for i, (word, count) in enumerate(stats['top_words'][:3]):
            print(f"{word} ({count})", end="")
            if i < 2:
                print(", ", end="")
        print()
    
    # Find unique words for each book
    print("\n" + "="*60)
    print("Distinctive Words Analysis")
    print("="*60)
    print("(Words that appear frequently in one book but not others)\n")
    
    #  top words from each book
    for title1, stats1 in book_stats.items():
        top_words1 = set([word for word, count in stats1['top_words'][:20]])
        
        # Compare with other books
        distinctive_words = []
        for word, count in stats1['top_words'][:20]:
            appears_in_others = False
            for title2, stats2 in book_stats.items():
                if title1 != title2:
                    top_words2 = set([w for w, c in stats2['top_words'][:20]])
                    if word in top_words2:
                        appears_in_others = True
                        break
            
            if not appears_in_others:
                distinctive_words.append((word, count))
        
        if distinctive_words:
            print(f"{title1} distinctive words:")
            for word, count in distinctive_words[:5]:
                print(f"  - {word} ({count} occurrences)")
            print()
    
    return book_stats

def main():
    # PART 1: DETAILED ANALYSIS OF OLIVER TWIST BOOK
    print("="*60)
    print("DETAILED ANALYSIS: OLIVER TWIST")
    print("="*60)
    
    url = "https://www.gutenberg.org/cache/epub/730/pg730.txt"
    
    # Load and clean text
    print("\nDownloading and cleaning text...")
    text = load_text(url)
    
    # Display sample
    print("\nFirst 500 characters:")
    print(text[:500])
    
  
    total_words = len(text.split())
    print(f"\n\nTotal word count: {total_words}")
    
    # Removing  stop words
    filtered_words = remove_stop_words(text)
    print(f"Word count after removing stop words: {len(filtered_words)}")
    
    # Word frequency analysis
    freq = word_frequency(filtered_words)
    
    # Get top 10 words
    top_words = get_top_words(freq, 10)
    
    print("\nTop 20 most frequent words:")
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
    
    
    print("\n" + "="*60)
    print("Sentiment Analysis")
    print("="*60)
    print("Analyzing the emotional tone of Oliver Twist...")
    
    sentiment = sentiment_analysis(text[:50000])  # Analyze first part of book
    if sentiment:
        overall = sentiment['overall']
        print(f"\nOverall Sentiment Scores:")
        print(f"  Positive: {overall['pos']:.1%}")
        print(f"  Neutral: {overall['neu']:.1%}")
        print(f"  Negative: {overall['neg']:.1%}")
        print(f"  Compound: {overall['compound']:.3f} (range: -1 to +1)")
        
        print(f"\nMost Positive Sentences:")
        for sentence, score in sentiment['most_positive']:
            print(f"  [{score:+.3f}] {sentence}...")
        
        print(f"\nMost Negative Sentences:")
        for sentence, score in sentiment['most_negative']:
            print(f"  [{score:+.3f}] {sentence}...")
        
        print("\nInterpretation:")
        if overall['compound'] > 0.05:
            print("  The novel has an overall POSITIVE tone")
        elif overall['compound'] < -0.05:
            print("  The novel has an overall NEGATIVE tone")
        else:
            print("  The novel has an overall NEUTRAL tone")
        print("="*60)
    
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
    
    # PART 2: COMPARE MULTIPLE BOOKS 
    book_stats = compare_multiple_books()
    
    print("\n" + "="*60)
    print("ANALYSIS COMPLETE!")
    print("="*60)
    print("\nThis project analyzed:")
    print("✓ Word frequencies and patterns")
    print("✓ Summary statistics (word length, vocabulary richness)")
    print("✓ Sentiment analysis (emotional tone)")
    print("✓ Text similarity (within Oliver Twist)")
    print("✓ Cross-book comparison (3 Dickens novels)")

if __name__ == "__main__":
    main()