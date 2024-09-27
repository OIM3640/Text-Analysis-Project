from mediawiki import MediaWiki
wikipedia = MediaWiki()

example = "the man said hi to the other man and he said that he man"

def remove_stopwords(text):
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    stopwords_ = set(stopwords.words('english'))
    words= word_tokenize(text)
    texts = []
    punctuation = "!()-[]{};:'\"\ , <> . /?@#$%^&*_~ `` 's⟩ ⟨===\'\'\'"

    for w in words:
        x = 0
        w = w.lower()
        characters = []
        characters[:] = w
        for i in characters:
            if i in punctuation:
                x += 1
        if w in stopwords_:
            x += 1
        if len(w) == 1:
            x += 1
        if w == "the":
            x += 1
        if x == 0:
            texts.append(w)
    
    return texts
  


def gives_counts(texts:list):
    counts= dict()
    for i in texts:
        counts[i] = counts.get(i, 0) + 1
    return counts


def list_highest_count(counts:dict, k):

    counts_list = list(counts.items())
    ordered_counts = sorted(counts_list,key = lambda x: x[1],reverse = True)

    highest_counts = []

    included = 0
    print()
    while included < k:
        word = ordered_counts[included][0]
        count = ordered_counts[included][1]
        print(f"{word:10} was found {count:5} times")

        highest_counts.append(ordered_counts[included])
        included += 1
    print()
    return highest_counts



country_a = "The United States of America"
country_b = "Canada"
compare = 20

a = wikipedia.page(country_a)
name_a = a.title
text_a = a.content

b = wikipedia.page(country_b)
name_b = b.title
text_b = b.content

print()
print(name_a)
x = remove_stopwords(text_a)
# print(x)
y = gives_counts(x)
z = list_highest_count(y,compare)
print(z)
print()
print(name_b)
x = remove_stopwords(text_b)
y = gives_counts(x)
list_highest_count(y,compare)






    


