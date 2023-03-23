# install: pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup


def scrape_stranger_things_reviews():
    """
    Scrape the reviews for Stranger Things from the IMDb website and write them to a text file.
    """
    # set the URL of the Stranger Things reviews page on IMDb
    url = 'https://www.imdb.com/title/tt4574334/reviews'

    # create an empty list to store the reviews
    reviews = []

    # loop through the first 100 pages of reviews (each page has 25 reviews)
    for page in range(1, 101):
        # construct the URL for the current page
        page_url = f'{url}?start={25*(page-1)}'

        # send a request to the URL and get the HTML content
        response = requests.get(page_url)
        html_content = response.content

        # use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')

        # find all the review elements on the page
        review_elements = soup.find_all(
            'div', {'class': 'lister-item-content'})

        # extract the text of each review and add it to the list
        for element in review_elements:
            review_text = element.find('div', {'class': 'text'}).text.strip()
            if review_text:
                reviews.append(review_text)

        # print progress notification
        print(f'Finished scraping page {page} of Stranger Things reviews')

    # write the reviews to a text file using UTF-8 encoding
    with open('stranger_things_reviews.txt', 'w', encoding='utf-8') as f:
        for review in reviews:
            f.write(review + '\n')


def scrape_vampire_diaries_reviews():
    """
    Scrape the reviews for Vampire Diaries from the IMDb website and write them to a text file.
    """
    # set the URL of the Vampire Diaries reviews page on IMDb
    url = 'https://www.imdb.com/title/tt1405406/reviews'

    # create an empty list to store the reviews
    reviews = []

    # loop through the first 100 pages of reviews (each page has 25 reviews)
    for page in range(1, 101):
        # construct the URL for the current page
        page_url = f'{url}?start={10*(page-1)}'

        # send a request to the URL and get the HTML content
        response = requests.get(page_url)
        html_content = response.content

        # use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')

        # find all the review elements on the page
        review_elements = soup.find_all(
            'div', {'class': 'text show-more__control'})

        # extract the text of each review and add it to the list
        for element in review_elements:
            review_text = element.text.strip()
            if review_text:
                reviews.append(review_text)

        # print progress notification
        print(f'Finished scraping page {page} of Vampire Diaries reviews')

    # write the reviews to a text file using UTF-8 encoding
    with open('vampire_diaries_reviews.txt', 'w', encoding='utf-8') as f:
        for review in reviews:
            f.write(review + '\n')


def main():
    # call the function to scrape reviews and write them to a file
    scrape_stranger_things_reviews()
    scrape_vampire_diaries_reviews()


if __name__ == '__main__':
    main()
