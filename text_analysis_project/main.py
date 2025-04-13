from wikiapi import get_wiki_page
from analysis import process_page, print_most_common, total_words, different_words

"""
we will now find how many times "Ronaldo" is written in the "Real Madrid CF" page, as well as the top 10 most common words used in the article, and find how many times "Messi" is written in the "FC Barcelona" page, as well as the top 10 most common words used in that article
"""


def main():
    word = "Ronaldo"
    page = "Real Madrid CF"
    page_text = get_wiki_page(page)
    processed_page = process_page(page_text)
    count = processed_page[word.lower()]
    print("on " + page + " we find " + word + " " + str(count) + " times")
    print("most common words on " + str(page))
    processed_page = process_page(page_text)
    print_most_common(processed_page)
    print("total words on " + str(page))
    print(total_words(processed_page))
    print("unique words on " + str(page))
    print(different_words(processed_page))

    word = "Messi"
    page = "FC Barcelona"
    page_text = get_wiki_page(page)
    processed_page = process_page(page_text)
    count = processed_page[word.lower()]
    print("on " + page + " we find " + word + " " + str(count) + " times")
    print("most common words on " + str(page))
    processed_page = process_page(page_text)
    print_most_common(processed_page)
    print("total words on " + str(page))
    print(total_words(processed_page))
    print("unique words on " + str(page))
    print(different_words(processed_page))


if __name__ == "__main__":
    main()
