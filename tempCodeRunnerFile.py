def word_freq(artist_content):
    total_word_count = 0

    for freq in artist_content:
        total_word_count += artist_content[freq]
    
    print(total_word_count)


print(word_freq(artist_content))