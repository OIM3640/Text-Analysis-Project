import urllib.request
import string

def download_data(url, filename = 'pg1513.txt'):
    """Downloads a file from the Project Gutenberg site and saves it to the """
    try:
        with urllib.request.urlopen(url) as f:
            text = f.read().decode('utf-8')
            print(text)  # for testing
        with open(filename, 'w', encoding='utf-8') as out:
            out.write(text)
        print(f"File downloaded and saved as {filename}")
        return filename
    except Exception as e:
        print("An error occurred:", e)
        return None 
    

def is_special_line(line): 
    """Text Cleaning and Processing"""
    return line.strip().startswith('*** ')


def clean_file(input_file, output_file):
    """Removing headers and footers"""
    with open(input_file, encoding='utf-8', errors= 'ignore') as reader,\
        open(output_file, 'w', encoding='utf-8') as writer: 
        for line in reader: 
            if is_special_line(line):
                break 
        for line in reader: 
            if is_special_line(line): 
                break 
            writer.write(line)
        
    print(f"Cleaned file save as {output_file}")
    

def final_clean_version(filename, output_file = 'final_cleaned.txt'):
    """Removes punctuation and makes entire text in lower caps"""
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        text= f.read()

    no_punct = ''.join(ch for ch in text if ch not in string.punctuation).lower()
    cleaned_lines = [''.join(line.split()) for line in no_punct.splitlines()]
    cleaned_text = '\n'.join(cleaned_lines)

    with open(output_file, 'w', encoding='utf-8') as f: 
        f.write(cleaned_text)
    print (f"Final cleaned text saved as {output_file}")
    return output_file




def remove_stopwords(filename):
    stopwords = ["a", "of", "to", "in", "it", "is", "i", "that","was", "he", 
        "you", "for", "on", "with", "as", "his", "they", "be", "at", "one", "have", "this", "from", 
        "or", "had", "by", "not", "but", "what", "all", "were", "we", "her", "can", "an"]
        
    with open( filename, 'r', encoding='utf-8', errors='ignore') as f:
        lines= f.readlines()
    new_lines= []
    for line in lines: 
        words = [w for w in line.split() if w.lower() not in stopwords]
        new_lines.append(''.join(words))
    
    with open(filename, 'w', encoding='utf-8') as f: 
        f.write('\n'.join(new_lines))
    
    print(f"Stopwords removed from the text")


if __name__ == "__main__":
    url = 'https://www.gutenberg.org/cache/epub/1513/pg1513.txt'
    raw = download_data(url)

    if raw: 
        clean_file(raw, 'cleaned_text.txt')
        final_clean_version('cleaned_text.txt')
        remove_stopwords('final_cleaned.txt')