import urllib.request

# URL for "The Great Gatsby" from Project Gutenberg:
url = "https://www.gutenberg.org/cache/epub/64317/pg64317.txt"


def fetch_text(url):
    """
    This fetches the text from the URL that is Project Gutenberg
    and returns it as a string.
    """
    with urllib.request.urlopen(url) as f:  # Open URL connection
        text = f.read().decode("utf-8")  # Read and decode the content
    return text
