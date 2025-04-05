# Wikipedia/ MediaWiki

from mediawiki import MediaWiki
import json
import nltk

nltk.download("stopwords")
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))
from thefuzz import fuzz

wikipedia = MediaWiki(user_agent="sguti")
# wikipedia = MediaWiki()
asoiaf = MediaWiki(url="http://awoiaf.westeros.org/api.php")

# create the artist list that we want to explore
artist_names = ["Jhene Aiko", "Tyler the Creator", "Nessa Barrett"]


def get_summary(artist_names):
    """Get the summary of the 3 artist and return it in a dict. Do the summaries because the full pages are too long and do not fully load"""
    artist_content = {}  # turn this into a dict instead
    for name in artist_names:
        page = wikipedia.page(name)
        content_summary = page.summary
        # summary = page.summarize(chars = 2000)
        artist_content[name] = content_summary

    return artist_content


# print(artist1.title)
# print(artist1.content)

# notes for later part below
# json.dumps() -- converts the string into a nicely formatted string
# ensure_ascii=False -- ensures special characters like accents are kept
# print(json.dumps(artist_content, indent = 4, ensure_ascii=False))


def count_word_freq(artist_content, stop_words):
    """Creates a dict of the words that are in the summaries, excluding common stop words, sorts them from greatest to least."""
    word_freq = {}
    words = artist_content.lower().split()

    for word in words:
        word = word.strip('.,!?()[]""\'')
        if word and word not in stop_words:
            word_freq[word] = word_freq.get(word, 0) + 1
    # return word_freq
    # return sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

    sorted_word_freq = {
        k: v
        for k, v in sorted(word_freq.items(), key=lambda item: item[1], reverse=True)
    }
    return sorted_word_freq


def word_freq_per_artist(artist_content, stop_words):
    """Create a dict that has the frequency of each word for EACH artist."""
    freq_per_artist = {}

    for artist, summary in artist_content.items():
        freq_per_artist[artist] = count_word_freq(summary, stop_words)

    return freq_per_artist


def top_words_per_artist(freq_per_artist, top_n=10):
    """Returns the top 10 words that are most common for each artist"""
    top_words = {}

    for artist, freqs in freq_per_artist.items():
        top_words[artist] = dict(list(freqs.items())[:top_n])

    return top_words


def compute_fuzz_similarity(artist_content):
    """Checks for the similarity of text between the 3 artists -- seeing how similar or different the artists are"""
    artists = list(artist_content.keys())
    summaries = list(artist_content.values())
    fuzz_results = {}

    for i in range(len(artists)):
        artist1 = artists[i]
        fuzz_results[artist1] = {}

        for j in range(len(artists)):
            if i != j:
                artist2 = artists[j]
                score = fuzz.token_sort_ratio(summaries[i], summaries[j])
                fuzz_results[artist1][artist2] = score

    return fuzz_results


def main():
    if __name__ == "__main__":

        artist_content = get_summary(artist_names)

        # pretty print summaries
        print(json.dumps(artist_content, indent=4, ensure_ascii=False))

        # print word frequencies in each summary
        freqs = word_freq_per_artist(artist_content, stop_words)
        total_word_counts = {}
        for artist, freq_dict in freqs.items():
            total_count = sum(
                freq_dict.values()
            )  # freq_dict is a dict of {word: count}
            total_word_counts[artist] = total_count

        print("\n Total Word Count (excluding stopwords):")
        print(json.dumps(total_word_counts, indent=4, ensure_ascii=False))

        # # Print word frequencies per artist
        print("\n Word Frequencies:")
        print(
            json.dumps(
                word_freq_per_artist(artist_content, stop_words),
                indent=4,
                ensure_ascii=False,
            )
        )

        # Remove stopwords, count frequencies, and analyze
        freqs = word_freq_per_artist(artist_content, stop_words)
        top_words = top_words_per_artist(freqs)

        print("\n Top 10 Words per Artist:")
        print(json.dumps(top_words, indent=4, ensure_ascii=False))

        # fuzz score - test for similarity
        fuzz_scores = compute_fuzz_similarity(artist_content)

        print("\n Fuzz Similarity Between Artist Summaries:")
        print(json.dumps(fuzz_scores, indent=4, ensure_ascii=False))


main()
