# I got this code directly from the instructions.md
import urllib.request

def harvest_gutenberg_text(url):
    try:
        with urllib.request.urlopen(url) as f:
            text = f.read().decode('utf-8')
            return text
    except Exception as e:
        print("An error occurred:", e)
        return ""
