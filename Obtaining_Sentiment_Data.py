print("Running script...")
import os
import requests
from datetime import datetime
from urllib.parse import urlparse
import re

def _normalize_url(u: str) -> str:
    if not u:
        return ""
    # strip query/fragment, lowercase host, remove trailing slash
    p = urlparse(u)
    path = p.path.rstrip("/")
    return f"{p.scheme.lower()}://{p.netloc.lower()}{path}"

def _normalize_text(t: str) -> str:
    if not t:
        return ""
    t = t.lower().strip()
    # collapse whitespace and remove punctuation that often varies
    t = re.sub(r"\s+", " ", t)
    t = re.sub(r"[^\w\s]", "", t)  # drop punctuation
    return t

def _dedupe_key(article: dict) -> str:
    url = _normalize_url(article.get("url", ""))
    title = _normalize_text(article.get("title", ""))
    desc = _normalize_text(article.get("description", ""))[:120]  # short fingerprint
    source = _normalize_text(article.get("source") or article.get("author") or "")
    date = (article.get("published_at") or "")[:10]  # YYYY-MM-DD
    # Preference order: clean URL, else composite fingerprint
    return url or f"{title}|{desc}|{source}|{date}"

def Data_Gathering(key, keywords="artificial intelligence", want=5, per_page=20):
    url = "http://api.mediastack.com/v1/news"
    seen = set()
    results = []
    offset = 0

    while len(results) < want:
        params = {
            "access_key": key,
            "languages": "en",
            "keywords": keywords,
            "sort": "published_desc",
            "limit": per_page,
            "offset": offset,
            # Optional helpful filters to reduce dupes:
            # "countries": "us,gb,ca",
            # "search_in": "title",   # reduces same-story variants
        }
        resp = requests.get(url, params=params, timeout=15)
        try:
            payload = resp.json()
        except Exception:
            print(f"Bad JSON (status {resp.status_code}): {resp.text[:200]}")
            break

        if isinstance(payload, dict) and "error" in payload:
            err = payload["error"]
            print(f"API error {err.get('code')}: {err.get('message')}")
            break

        batch = payload.get("data", [])
        if not batch:
            break

        for a in batch:
            k = _dedupe_key(a)
            if not k or k in seen:
                continue
            seen.add(k)
            results.append(a)
            if len(results) == want:
                break

        offset += per_page

    if not results:
        print("No unique articles returned.")
        return

    for a in results:
        title = a.get("title", "<no title>")
        desc = a.get("description", "") or ""
        source = a.get("source", a.get("author", ""))
        pub = a.get("published_at", "")
        try:
            pub = datetime.fromisoformat(pub.replace("Z", "+00:00")).strftime("%Y-%m-%d %H:%M")
        except Exception:
            pass
        print(title)
        meta = "  ".join(x for x in [source or "", pub or ""] if x).strip()
        if meta:
            print(meta)
        if desc:
            print(desc)
        print()
