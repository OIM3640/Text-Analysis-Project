# main.py
# Entry file for the project: runs fetch -> analysis for chosen titles.
#
# AI Assistance (ChatGPT, November 2025):
# - Used for documentation: Writing comments explaining the main entry point and code organization

from reviews_fetcher import get_or_build_cache
from analyze_reviews import analyze_title_reviews

def main():
    # Pick any films you like—franchise comparisons are fun!
    # Note: Using Kaggle dataset due to Cinemagoer review limitations
    titles = ["The Dark Knight", "Barbie", "Oppenheimer"]

    data = get_or_build_cache(titles)

    results = []
    for t in titles:
        results.append(analyze_title_reviews(t, data.get(t, []), top_n=20))

    # Optionally write TSV to inspect in Sheets without pandas
    with open("review_wordfreqs.tsv", "w", encoding="utf-8") as f:
        f.write("title\tword\tcount\n")
        for r in results:
            for w, c in r["top_words"]:
                f.write(f"{r['title']}\t{w}\t{c}\n")
    print("\n[✓] Wrote review_wordfreqs.tsv")

if __name__ == "__main__":
    main()

