def create_word_frequency_chart(top_words):
    """Create a simple ASCII bar chart of word frequencies"""
    print("\n" + "="*60)
    print("Word Frequency Visualization")
    print("="*60)
    
    if not top_words:
        print("No data to visualize")
        return
    
    # Find max count for scaling
    max_count = top_words[0][1]
    max_bar_length = 50
    
    for word, count in top_words:
        # Scale bar length
        bar_length = int((count / max_count) * max_bar_length)
        bar = '█' * bar_length
        print(f"{word:15} | {bar} {count}")
    
    print("="*60)
    