from mediawiki import MediaWiki

wikipedia = MediaWiki()
babson = wikipedia.page("Babson College")
print(babson.title)
print(babson.content)


dunkin = wikipedia.page("Dunkin Donut")
print(dunkin.title)
print(dunkin.content)
print(dunkin.references)
print(dunkin.categories)