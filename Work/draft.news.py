from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='966d42a19bf042c68e6bec614e7e74c4')

# # /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='bitcoin',
#                                           sources='bbc-news,the-verge',
#                                           category='business',
#                                           language='en',
#                                           country='us')

# /v2/everything
all_articles = newsapi.get_everything(q='SVB',
                                      from_param='2023-03-23',
                                      to='2023-03-24',
                                      language='en',
                                      sort_by='relevancy',
                                      page=1)

# # /v2/top-headlines/sources
# sources = newsapi.get_sources()

data = all_articles

# print(data.keys())

print(data['status'])
print(data['totalResults'])
# print(len(data['articles']))
# print(data['articles'][1])

data = data['articles']

# print(data)
print(len(data))

d = []
for i in data:
    x = i.get('description')
    d.append(x)

d = ' '.join(d)
print(d)





# print(summary)

# def remove_stopwords(text):
#     from nltk.corpus import stopwords
#     from nltk.tokenize import word_tokenize
#     stopwords_ = set(stopwords.words('english'))
#     words= word_tokenize(text)
#     texts = []
#     punctuation = "!()-[]{};:'\"\ , <> . /?@#$%^&*_~ `` 's⟩ ⟨===\'\'\'"

#     for w in words:
#         x = 0
#         w = w.lower()
#         characters = []
#         characters[:] = w
#         for i in characters:
#             if i in punctuation:
#                 x += 1
#         if w in stopwords_:
#             x += 1
#         if len(w) == 1:
#             x += 1
#         if w == "the":
#             x += 1
#         if x == 0:
#             texts.append(w)
    
#     return texts
  
# text = remove_stopwords(summary)
# text = ' '.join(text)

# # print(text)


# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# score = SentimentIntensityAnalyzer().polarity_scores(text)
# print(score)

