import urllib.request

#Project Guttenberg

url_1 = 'https://www.gutenberg.org/cache/epub/4210/pg4210.txt'
#Our War with Spain for Cuba's Freedom
with urllib.request.urlopen(url_1) as f:
    CF_original = f.read().decode('utf-8')
    #I found the character count by copying what I wanted removed into Word
    Cuba_freedon = CF_original
    #print(Cuba_freedom) # for testing



url_2 = 'https://www.gutenberg.org/cache/epub/37676/pg37676.txt'
#The History of Cuba, vol. 2
with urllib.request.urlopen(url_2) as f:
    HC_original = f.read().decode('utf-8')
    #I found the character count by copying what I wanted removed into Word
    history_Cuba = HC_original
    #print(history_Cuba) # for testing


#print(word_frequency(Cuba_freedom, 'cuba'))

def remove_preamble(text):
    count = 0
    checker = 0
    key = build_key()
    key_tooth = key[0]

    for letter in text:
        count = count+1
        if letter == key_tooth:
            if checker < len(key)-1:
                #print(key_tooth)
                key_tooth = key[checker+1]
            checker = checker+1
        if checker == len(key)-1:
            #print(key_tooth)
            print('checker')
            break
    return text[count:]
            
        
    print('done!')
            
    

def build_key():
    print('Type the unique heading of the section immediately following the preamble EXACTLY as it appears. Everything before this heading will be removed.')
    chosen = input('Type here: ')
    key = []
    for i in range(len(chosen)):
        key.append(chosen[i])
    return key





