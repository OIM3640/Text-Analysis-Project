import urllib.request

url = 'https://www.gutenberg.org/cache/epub/37106/pg37106.txt'
try:
    with urllib.request.urlopen(url) as f:
        text = f.read().decode('utf-8')
        print(text)  # for testing
except Exception as e:
    print("An error occurred:", e)