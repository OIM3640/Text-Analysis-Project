import newspaper
from newspaper import Article

article = newspaper.article('https://www.nytimes.com/2025/04/01/business/economy/trump-tariffs-fed-economy.html')

article.download()
article.parse()

print(article.authors)
print(article.publish_date)
print(article.text)
