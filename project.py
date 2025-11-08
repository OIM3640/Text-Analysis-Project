import urllib.request
import string

from api import STOPWORDS, extract_entities_with_openai, tally_entities

# source texts
ILIAD_URL = "https://www.gutenberg.org/cache/epub/6130/pg6130.txt"
ODYSSEY_URL = "https://www.gutenberg.org/cache/epub/1727/pg1727.txt"

# chunk settings for OpenAI API
CHUNK_SIZE = 1200
MAX_API_CHUNKS = 2

# download the texts from project gutenberg
def download_text(url):
    try:
        with urllib.request.urlopen(url) as f:
            text = f.read().decode('utf-8')
            return text
    except Exception as e:
        print("An error occurred:", e)

# strip texts of headers
def strip_gutenberg(text):
    start_token = "*** START OF"
    end_token = "*** END OF"
    s = text.find(start_token)
    e = text.find(end_token)
    if s != -1 and e != -1:
        return text[s:e]
    return text

def clean_and_split(text):
    # convert to lowercase
    text = text.lower()
    # remove basic punctuation
    for p in string.punctuation:
        text = text.replace(p, " ")
    # split to words
    words = text.split()
    return words

# filter text to remove stopwords
def remove_stopwords(words):
    new_words = []
    for w in words:
        if w not in STOPWORDS:
            new_words.append(w)
    return new_words

def count_words(words):
    counts = {}
    for w in words:
        if w in counts:
            counts[w] = counts[w] + 1
        else:
            counts[w] = 1
    return counts

def top_words(counts, n=15):
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    return items[:n]

def ascii_bar_chart(pairs, title):
    """
    pairs: list of (word, count)
    prints a simple bar chart
    """
    print("\n" + title)
    if not pairs:
        print("no data")
        return
    max_val = pairs[0][1]
    for word, count in pairs:
        # scale bar to 30 chars
        bar_len = int(count / max_val * 30)
        bar = "#" * bar_len
        print(f"{word:15} | {bar}")

def chunks_from_words(words, chunk_size):
    for i in range(0, len(words), chunk_size):
        yield words[i:i + chunk_size]

def analyze_work(name, url):
    print(f"--- downloading {name} ---")
    text = download_text(url)
    text = strip_gutenberg(text)

    # 1. basic text analysis
    words = clean_and_split(text)
    filtered_words = remove_stopwords(words)
    counts = count_words(filtered_words)
    top15 = top_words(counts, 15)

    # visualization requirement: show a bar chart of top words
    ascii_bar_chart(top15, f"Top words in {name}")

    # 2. advanced: OpenAI entity extraction
    print(f"\nExtracting entities from {name} with OpenAI (up to {MAX_API_CHUNKS} chunks)...")
    all_entities = []
    original_words = text.split()

    chunk_number = 0
    for chunk_words in chunks_from_words(original_words, CHUNK_SIZE):
        if chunk_number >= MAX_API_CHUNKS:
            break
        passage = " ".join(chunk_words)
        try:
            data = extract_entities_with_openai(passage)
            all_entities.append(data)
        except Exception as e:
            print("OpenAI error:", e)
            break
        chunk_number = chunk_number + 1

    if all_entities:
        char_counts, place_counts, god_counts = tally_entities(all_entities)
    else:
        char_counts, place_counts, god_counts = {}, {}, {}

    print(f"\n(Partial) most mentioned characters in {name}:")
    for word, cnt in sorted(char_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(word, cnt)

    print(f"\n(Partial) most mentioned places in {name}:")
    for word, cnt in sorted(place_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(word, cnt)

    print(f"\n(Partial) most mentioned gods in {name}:")
    for word, cnt in sorted(god_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(word, cnt)

    return {
        "word_counts": counts,
        "entities": {
            "characters": char_counts,
            "places": place_counts,
            "gods": god_counts
        }
    }


def main():
    iliad_result = analyze_work("Iliad", ILIAD_URL)
    odyssey_result = analyze_work("Odyssey", ODYSSEY_URL)

    # compare if we got entities
    print("\n=== Comparison (partial) ===")
    if iliad_result["entities"]["characters"] and odyssey_result["entities"]["characters"]:
        print("\nCharacters mentioned more in Iliad than Odyssey:")
        for name, cnt in iliad_result["entities"]["characters"].items():
            other = odyssey_result["entities"]["characters"].get(name, 0)
            if cnt > other:
                print(f"{name}: Iliad {cnt}, Odyssey {other}")
    else:
        print("Skipped comparison because no entities were extracted.")


if __name__ == "__main__":
    main()