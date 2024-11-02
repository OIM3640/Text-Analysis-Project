import urllib.request

url = 'https://www.gutenberg.org/cache/epub/2591/pg2591.txt'
with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')
    print(text) # for testing