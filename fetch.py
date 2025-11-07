# fetch.py
# Fetch multiple Wikipedia articles by title and return {title: content}

from mediawiki import MediaWiki
from mediawiki.exceptions import DisambiguationError, PageError

def fetch_articles(titles: list[str]) -> dict[str, str]:
    wikipedia = MediaWiki()
    articles: dict[str, str] = {}

    for title in titles:
        try:
            # normal fetch
            page = wikipedia.page(title)
            articles[title] = page.content

        except DisambiguationError as e:
            # if ambiguous, try the first suggested option
            try:
                alt = e.options[0]
                page = wikipedia.page(alt)
                articles[title] = page.content
                print(f"⚠️  '{title}' was ambiguous; used '{alt}'.")
            except Exception as e2:
                print(f"⚠️ Could not fetch {title} (disambiguation): {e2}")

        except PageError as e:
            print(f"⚠️ Could not fetch {title}: {e}")

        except Exception as e:
            print(f"⚠️ Could not fetch {title}: {e}")

    return articles

if __name__ == "__main__":
    # tiny self-test
    data = fetch_articles(["Tesla"])
    for k in data:
        print("Fetched:", k, "chars:", len(data[k]))
