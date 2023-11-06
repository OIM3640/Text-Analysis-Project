"""retrieve graduate schools info from Wikipedia and news articles to do text analysis on by copying the results from the terminal into each sources individual text file by hardcoding the text"""

import requests
from mediawiki import MediaWiki

# Initialize the Wikipedia API
wikipedia = MediaWiki()

# Title of page to grab info from
wikipedia_page_title = "List of United States graduate business school rankings"

# Fetch the content of the Wikipedia page
page_content = wikipedia.page(wikipedia_page_title).content

# Display the content
print(page_content)


# Initialize the Wikipedia API
wikipedia = MediaWiki()

# Title of page to grab info from
wikipedia_page_title = "Higher education in the United States"

# Fetch the content of the Wikipedia page
page_content = wikipedia.page(wikipedia_page_title).content

# Display the content
print(page_content)


from newspaper import Article

url_1 = 'https://www.insidehighered.com/news/government/student-aid-policy/2023/10/03/biden-administration-puts-grad-schools-hot-seat'
url_2 = 'https://fortune.com/education/business/best-mba-programs/'
article_1 = Article(url_1)
article_2 = Article(url_2)
article_1.download()
article_2.download()
article_1.parse()
article_2.parse()
article_1_text = article_1.text
article_2_text = article_2.text
print(article_1_text)
print(article_2_text) 

