from rake_nltk import Rake

from mediawiki import MediaWiki


wikipedia = MediaWiki()
Panama = wikipedia.page("Panama")
text = Panama.content

r = Rake(filtered_words)
mytext = text

r.extract_keywords_from_text(mytext)
keywords = r.get_ranked_phrases()

for keyword in keywords[:10]:
    print(keywords)
# print(r.get_ranked_phrases_with_scores())