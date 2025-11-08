from thefuzz import fuzz

def text_similarity(file1, file2, sample_size=10000):
    """Compates how much similarity two texts have"""
    with open(file1, 'r', encoding='utf-8', errors='ignore') as f1: 
        text1 = f1.read(sample_size)
    
    with open(file2, 'r', encoding='utf-8', errors='ignore') as f2: 
        text2 = f2.read(sample_size)

    ratio = fuzz.ratio(text1, text2)

    print(f"Text similarity ratio {ratio}")
    return ratio

if __name__ == "__main__":
    text_similarity("final_cleaned.txt", "translated_text.txt")