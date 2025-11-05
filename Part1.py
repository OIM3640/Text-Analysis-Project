from pathlib import Path
from imdb import Cinemagoer
import json, pickle

def save_jsonl(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

def save_pickle(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as f:
        pickle.dump(obj, f)

def fetch_imdb_reviews(title: str, max_reviews: int = 200):
    ia = Cinemagoer()
    movie = ia.search_movie(title)[0]
    movie = ia.get_movie(movie.movieID, info=['reviews'])
    reviews = movie.get('reviews', [])[:max_reviews]
    rows = []
    for i, r in enumerate(reviews):
        rows.append({
            "source": "imdb",
            "movie_title": title,
            "movie_id": movie.movieID,
            "idx": i,
            "rating": r.get("rating"),
            "author": r.get("author"),
            "date": r.get("date"),
            "text": r.get("content", "")
        })
    return rows

if __name__ == "__main__":
    out_jsonl = Path("data/raw/imdb_dark_knight_reviews.jsonl")
    out_pkl   = Path("data/raw/imdb_dark_knight_reviews.pkl")
    rows = fetch_imdb_reviews("The Dark Knight", max_reviews=300)
    save_jsonl(out_jsonl, rows); save_pickle(out_pkl, rows)
    print(f"IMDB: saved {len(rows)} rows -> {out_jsonl}")