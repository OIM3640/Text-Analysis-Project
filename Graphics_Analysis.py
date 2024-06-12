from wordcloud import WordCloud
import matplotlib.pyplot as plt
import urllib.request

# URL for "The Importance of Being Earnest" by Oscar Wilde
url = "http://www.gutenberg.org/ebooks/844.txt.utf-8"

with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')

# Generate word cloud using wordcloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()