def remove_stop_words(text):
    """Remove common stop words from text"""
    stop_words = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 
        'of', 'with', 'is', 'was', 'are', 'were', 'been', 'be', 'have', 'has', 
        'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 
        'might', 'must', 'can', 'this', 'that', 'these', 'those', 'i', 'you', 
        'he', 'she', 'it', 'we', 'they', 'what', 'which', 'who', 'when', 'where', 
        'why', 'how', 'all', 'each', 'every', 'both', 'few', 'more', 'most', 
        'other', 'some', 'such', 'no', 'not', 'only', 'own', 'same', 'so', 
        'than', 'too', 'very', 'as', 'from', 'by', 'his', 'her', 'its', 'their',
        'them', 'there', 'here', 'then', 'now', 'if', 'into', 'out', 'up', 'down',
        'about', 'said', 'upon'
    }
    
    words = text.split()
    filtered_words = []
    
    for word in words:
        if word.lower() not in stop_words:
            filtered_words.append(word)
    
    return filtered_words

def word_frequency(words):
    """Count frequency of each word"""
    freq = {}
    for word in words:
        if word in freq:
            freq[word] = freq[word] + 1
        else:
            freq[word] = 1
    return freq

def get_top_words(freq_dict, n=20):
    """Get top N most frequent words"""
    # Convert dictionary to list of tuples
    word_list = []
    for word, count in freq_dict.items():
        word_list.append((word, count))
    
    # Sort by count (highest first)
    for i in range(len(word_list)):
        for j in range(len(word_list) - 1):
            if word_list[j][1] < word_list[j + 1][1]:
                # Swap
                temp = word_list[j]
                word_list[j] = word_list[j + 1]
                word_list[j + 1] = temp
    
    # Return top n words
    return word_list[:n]

def calculate_average_word_length(words):
    """Calculate average length of words"""
    if not words:
        return 0
    total_length = 0
    for word in words:
        total_length += len(word)
    return total_length / len(words)

def calculate_vocabulary_richness(words):
    """Calculate unique words / total words ratio"""
    if not words:
        return 0
    unique_words = set(words)
    return len(unique_words) / len(words)

def get_longest_words(words, n=10):
    """Get the n longest words"""
    # Create list of (word, length) tuples
    word_lengths = []
    unique_words = set(words)  # Remove duplicates
    
    for word in unique_words:
        word_lengths.append((word, len(word)))
    
    # Sort by length (longest first)
    for i in range(len(word_lengths)):
        for j in range(len(word_lengths) - 1):
            if word_lengths[j][1] < word_lengths[j + 1][1]:
                temp = word_lengths[j]
                word_lengths[j] = word_lengths[j + 1]
                word_lengths[j + 1] = temp
    
    return word_lengths[:n]

def text_similarity(text1, text2):
    """Compare similarity between two texts using Levenshtein Distance"""
    try:
        from thefuzz import fuzz
        
        # Only use the fastest method
        token_sort_ratio = fuzz.token_sort_ratio(text1, text2)
        
        return {
            'token_sort_ratio': token_sort_ratio
        }
    except ImportError:
        print("thefuzz not installed. Run: pip install thefuzz")
        return None

def compare_book_sections(text, section_length=500):
    """Compare different sections of the same book"""
    # Splits text into sections
    words = text.split()
    total_words = len(words)
    
    # Create 3 sections: beginning, middle, end (SMALLER SIZE)
    section_size = min(section_length, total_words // 3)
    
    beginning = ' '.join(words[:section_size])
    middle_start = (total_words // 2) - (section_size // 2)
    middle = ' '.join(words[middle_start:middle_start + section_size])
    end = ' '.join(words[-section_size:])
    
    return beginning, middle, end