from text_processing import Load_Txt, clean_and_filter
from sentiment import Pos_or_Neg, sentiment_score
from visualization import plot_sentiment

def main():
    text_folder = "text"
    files = Load_Txt(text_folder)
    if not files:
        return

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

if __name__ == "__main__":
    main()
