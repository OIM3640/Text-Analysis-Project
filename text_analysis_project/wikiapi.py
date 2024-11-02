from mediawiki import MediaWiki


def get_wiki_page(Real_Barcelona):
    """
    we are using the MediaWiki library to find the Wikipedia page titled "Real Madrid CF" and "FC Barcelona"
    """
    wikipedia = MediaWiki()
    page = wikipedia.page(Real_Barcelona)
    return page.content
