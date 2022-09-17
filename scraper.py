from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from urllib.error import HTTPError, URLError


def get_page(url):
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
    return bs


def create_books_list(bs):
    for book in bs.find_all('div', {'class': re.compile(
        '(grid-3 prod-block book-block )+(clear-class2 )*(clear-class4)*')}):
        print(book)
        return


def main():
    prefix = 'https://www.piter.com/collection/'
    suffix = '?page_size=100&order=&q=&only_available=true'
    categories = ['biznes-literatura', 'nauka-i-obrazovanie',
                  'kompyutery-i-internet', 'publitsistika-i-istoriya',
                  'meditsinskaya-literatura']
    for cat in categories:
        print('*' * 50)
        url = '%s%s%s' % (prefix, cat, suffix)
        print(url)
        bs = get_page(url)
        books_list = create_books_list(bs)


if __name__ == '__main__':
    main()
