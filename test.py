# This is a test file just to test to individual cases, not part of the main codes.

import urllib.request
# Lady Windermere’s Fan, by Oscar Wilde
url2 = 'https://www.gutenberg.org/cache/epub/30120/pg30120.txt'
with urllib.request.urlopen(url2) as g:
    text_aih = g.read().decode('utf-8')
    print(text_aih)  # for testingF
