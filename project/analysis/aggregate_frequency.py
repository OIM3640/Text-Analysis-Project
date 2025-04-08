import json
from collections import Counter

# Load word lists
with open("project/data/huffpost__cleaned4.json", encoding="utf-8") as file:
    huffpost_words = json.load(file)
    huffpost_unique = set(huffpost_words) # turn them into sets for later

with open("project/data/theepochtimes_cleaned4.json", encoding="utf-8") as file:
    epochtimes_words = json.load(file)
    epochtimes_unique = set(epochtimes_words)

huffpost_counts = Counter(huffpost_words) #count frequency
epochtimes_counts = Counter(epochtimes_words)

print("\nHuffPost Top 20 Words:") # top 20 most common words from each source
for word, count in huffpost_counts.most_common(20):
    print(f"{word}: {count}")

print("\nEpoch Times Top 20 Words:")
for word, count in epochtimes_counts.most_common(20):
    print(f"{word}: {count}")

shared_words = huffpost_unique & epochtimes_unique
only_huffpost = huffpost_unique - epochtimes_unique
only_epochtimes = epochtimes_unique - huffpost_unique

print(f"\nShared words: {len(shared_words)}")
print(f"Words only in HuffPost: {len(only_huffpost)}")
print(f"Words only in Epoch Times: {len(only_epochtimes)}\n")