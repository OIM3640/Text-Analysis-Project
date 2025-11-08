from text_processing import Load_Txt, clean_and_filter,count_words,summary_stats
from sentiment import Pos_or_Neg, sentiment_score
from visualization import plot_sentiment #, top_n_counts_per_file

def main():
    # Folder and Text Loader
    text_folder = "text"
    files = Load_Txt(text_folder, skip_header=True)
    if not files:
        return
    for name, raw in files:
        cleaned = clean_and_filter(raw)         # clean the text
        counts  = count_words(cleaned)          # dict: word -> freq
        stats   = summary_stats(cleaned)        # your words/unique/TTR/avg len stats
        items = counts.items()
        sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
        top5 = sorted_items[:5] # top 5 words for a quick glance
        for word, count in top5:
            print(f"{word}: {count}")
        print(f"\n{name}")
        print(f"  words: {stats['words']}")
        print(f"  unique_words: {stats['unique_words']}")
        print(f"  type_token_ratio: {stats['type_token_ratio']:.3f}")
        print(f"  avg_word_len: {stats['avg_word_len']:.2f}")
        print("  top5:", ", ".join(f"{w}({c})" for w, c in top5))

    # (simple) Sentiment Analysis
    lexicon_folder = "Text_Words"
    POS, NEG = Pos_or_Neg(lexicon_folder)

    scores = {}
    for name, text in files:
        cleaned = clean_and_filter(text)
        score = sentiment_score(cleaned, POS, NEG)
        scores[name] = score
        print(f"{name}: {score:+.3f}")

    # Visualization
    plot_sentiment(scores)
    # top_n_counts_per_file(files, n=15, cleaner=None)

if __name__ == "__main__":
    main()
