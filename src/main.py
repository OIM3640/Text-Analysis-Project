from pathlib import Path

from utils import load_text, strip_gutenberg_boilerplate
from clean import to_lower, tokenize_words, remove_stopwords, split_sentences
from analyze import word_frequencies, top_n, summary_stats
from viz import ascii_bar_chart

RAW_FILE = Path("data/raw/oliver_twist.txt")   # change name if your file differs
PROC_DIR = Path("data/processed")
RES_DIR  = Path("data/results")

def main():
    # 1) Load + strip boilerplate
    raw = load_text(RAW_FILE)
    body = strip_gutenberg_boilerplate(raw)
    print("Loaded characters:", len(raw))

    # 2) Clean
    lowered = to_lower(body)
    tokens = tokenize_words(lowered)
    tokens_nostop = remove_stopwords(tokens)
    sents = split_sentences(body)

    # 3) Analysis
    freqs = word_frequencies(tokens_nostop)
    top20 = top_n(freqs, 20)
    stats = summary_stats(body, tokens_nostop)
    stats["num_sentences"] = len(sents)
    stats["avg_sentence_len_words"] = round(len(tokens_nostop) / len(sents), 3) if sents else 0

    # 4) Save processed + results
    PROC_DIR.mkdir(parents=True, exist_ok=True)
    RES_DIR.mkdir(parents=True, exist_ok=True)

    (PROC_DIR / "oliver_tokens_nostop.txt").write_text(" ".join(tokens_nostop), encoding="utf-8")
    # CSV of word frequencies
    (RES_DIR / "top_words.csv").write_text(
        "word,count\n" + "\n".join(f"{w},{c}" for w,c in top20),
        encoding="utf-8"
    )
    # Stats as plain text
    (RES_DIR / "stats.txt").write_text(
        "\n".join(f"{k}: {v}" for k,v in stats.items()),
        encoding="utf-8"
    )

    # 5) Visualization (ASCII bars)
    print("\nTop 20 words (ASCII chart):")
    print(ascii_bar_chart(top20, width=40))

    # OPTIONAL (sentiment) – module-level import/flag
try:
    from optional_sentiment import split_paragraphs, vader_scores, top_pos_neg
    HAVE_SENTIMENT = True
except Exception as e:
    print("[Sentiment] Import failed:", e)
    HAVE_SENTIMENT = False

if __name__ == "__main__":
    main()

