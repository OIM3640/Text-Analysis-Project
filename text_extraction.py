import urllib.request

url = 'https://www.gutenberg.org/ebooks/42671.txt.utf-8'
with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')


