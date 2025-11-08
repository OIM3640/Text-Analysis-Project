import string

def create_dictionary(filename):
    """Creates a list from a file to a python dictionary"""
    dict_conversion ={}
    with open(filename, 'r', encoding= 'utf-8', errors = 'ignore') as f: 
        for line in f: 

            parts = line.strip().lower().split('-')
            if len(parts) == 2:
                dict_conversion[parts[0].strip()]= parts[1].strip()

    print (f"{len(dict_conversion)} translation words.")
    return dict_conversion

def translate_words(word, dictionary):
    """Translate the words from the original text with the new created dictionary"""
    cleaned = word.strip(string.punctuation).lower()
    return dictionary.get(cleaned, word)
 

def translate_text_file(input_file, output_file, dictionary):
    """Translate the entire text file, creating an new entire translated text file"""
    with open (input_file, 'r', encoding = 'utf-8', errors = 'ignore') as f:
        lines = f.readlines()

    translated_words =[]
    for line in lines: 
        words = line.split()
        translated_line= ' '.join(translate_words(w, dictionary)for w in words)
        translated_words.append(translated_line)

    with open(output_file, 'w', encoding= 'utf-8') as f: 
        f.write ('\n'.join(translated_words))
    
    print (f"Translation saved to {output_file}")


if __name__ == "__main__":
    dictionary = create_dictionary("development/Dictionary.txt")
    translate_text_file("final_cleaned.txt", "translated_text.txt", dictionary)
    


