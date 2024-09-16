import urllib.request


url = 'https://www.gutenberg.org/cache/epub/16/pg16.txt'
with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')
    print(text)

url = 'https://www.gutenberg.org/cache/epub/67098/pg67098.txt'
with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')
    print(text) 