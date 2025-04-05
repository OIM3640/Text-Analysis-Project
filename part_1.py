import urllib.request


def download_text(url):
    try:
        with urllib.request.urlopen(url) as f:
            return f.read().decode("utf-8")
    except Exception as e:
        print("An error occurred:", e)
        return None


def main():
    url = "https://www.gutenberg.org/cache/epub/11/pg11.txt"
    text = download_text(url)
    if text:
        print(text[:1000])  # ChatGPT suggested to only print out the first 1000 words for testing.


if __name__ == "__main__":
    main()
