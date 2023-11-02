import csv

emails = list() 
spamct = 0
hamct = 0
header = 0

with open('spamdata.csv', newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    try:
        for text in reader:
            flag = text[-1]
            emails.append(text)
            # print(text[-1], type(text[-1]))
            if text[-1] == "0":
                hamct += 1
            elif text[-1] == "1":
                spamct +=1
            else: header += 1
    except:
        print("Error here")

# print(f'spam: {spamct}, ham: {hamct}, header: {header}')

# print(s)

spamwords = list()
hamwords = list()
for email, flag in emails:
    words = email.split(" ")
    for i in range(len(words)-1):
        if flag == "0":
            hamwords.append(words[i])
        elif flag == "1":
            spamwords.append(words[i])


print(f'hamwords: {len(hamwords)}, spamwords: {len(spamwords)}')

spamdict = dict()
hamdict = dict()

for word in spamwords:
    spamdict[word] = spamdict.get(word, 0) + 1

for word in hamwords:
    hamdict[word] = spamdict.get(word, 0) + 1

for k,v in spamdict.items():
    spamdict[k] = v/len(spamwords)
    
for k,v in hamdict.items():
    hamdict[k] = v/len(hamwords)



print(f'hamdict: {len(hamdict)}, spamdict: {len(spamdict)}')

sorted_ham = list()
sorted_spam = list()

for k,v in hamdict.items():
    sorted_ham.append((v,k))
    sorted_ham.sort(reverse=True)

for k,v in spamdict.items():
    sorted_spam.append((v,k))
    sorted_spam.sort(reverse=True)

print(sorted_spam)
print("done sorting")

fields = ["word", "frq"]

with open('cleaned_ham', "w") as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(sorted_ham)

with open('cleaned_spam', "w") as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(sorted_spam)

print('done writing')




