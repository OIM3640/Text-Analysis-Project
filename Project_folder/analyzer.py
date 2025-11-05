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

    word_list = []
    for word, count in freq_dict.items():
        word_list.append((word, count))
    

    for i in range(len(word_list)):
        for j in range(len(word_list) - 1):
            if word_list[j][1] < word_list[j + 1][1]:
                # Swap
                temp = word_list[j]
                word_list[j] = word_list[j + 1]
                word_list[j + 1] = temp
    
   
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

    word_lengths = []
    unique_words = set(words)  #gets rid of duplicates
    
    for word in unique_words:
        word_lengths.append((word, len(word)))
    
    # Sorted by length
    for i in range(len(word_lengths)):
        for j in range(len(word_lengths) - 1):
            if word_lengths[j][1] < word_lengths[j + 1][1]:
                temp = word_lengths[j]
                word_lengths[j] = word_lengths[j + 1]
                word_lengths[j + 1] = temp
    
    return word_lengths[:n]

def sentiment_analysis(text):
    """Analyze sentiment of text using VADER"""
    try:
        import nltk
        from nltk.sentiment.vader import SentimentIntensityAnalyzer
        
        # Download required data
        try:
            nltk.data.find('vader_lexicon')
        except:
            print("Downloading VADER lexicon...")
            nltk.download('vader_lexicon', quiet=True)
        
        sia = SentimentIntensityAnalyzer()
        
        sentences = text.split('.')
       
        overall_score = sia.polarity_scores(text)
        
        # Find most positive and negative sentences
        sentence_scores = []
        for sentence in sentences[:100]:  # Analyze first 100 sentences
            if len(sentence.strip()) > 10:  # Skip very short sentences
                score = sia.polarity_scores(sentence)
                sentence_scores.append((sentence.strip()[:80], score['compound']))
        
        #  sentiment technique(ADDED)
        sentence_scores.sort(key=lambda x: x[1])
        most_negative = sentence_scores[:3]
        most_positive = sentence_scores[-3:]
        most_positive.reverse()
        
        return {
            'overall': overall_score,
            'most_positive': most_positive,
            'most_negative': most_negative
        }
    except ImportError:
        print("NLTK not installed. Run: pip install nltk")
        return None

def text_similarity(text1, text2):
    """Compare similarity between two texts using Levenshtein Distance"""
    try:
        from thefuzz import fuzz
        
      
        token_sort_ratio = fuzz.token_sort_ratio(text1, text2)
        
        return {
            'token_sort_ratio': token_sort_ratio
        }
    except ImportError:
        print("thefuzz not installed. Run: pip install thefuzz")
        return None

def compare_book_sections(text, section_length=500):
    """Compare different sections of the same book"""
    # Split text into sections
    words = text.split()
    total_words = len(words)
    
    
    section_size = min(section_length, total_words // 3)
    
    beginning = ' '.join(words[:section_size])
    middle_start = (total_words // 2) - (section_size // 2)
    middle = ' '.join(words[middle_start:middle_start + section_size])
    end = ' '.join(words[-section_size:])
    
    return beginning, middle, end