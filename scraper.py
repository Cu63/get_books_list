from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
#asdkhfakjldsfhkljah

def get_page(url):
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
    return bs


def create_books_list(bs):
    prefix = 'https://www.piter.com'
    for book in bs.find_all('div', {'class': re.compile(
        '(grid-3 prod-block book-block )+(clear-class[0-9].)*')}):
        title = book.find('span', {'class': 'title'})
        if title != None:
            title = title.text
        author = book.find('span', {'class': 'author'})
        if author != None:
            author = author.text
        price = book.find('span', {'class': 'price'})
        if price != None:
            price = price.text
        url = prefix + book.find('a')['href']

        print('Title: %s' % title)
        print('Author: %s' % author)
        print('Price: %s' % price)
        print('Url: %s' % url)


def main():
    prefix = 'https://www.piter.com/collection/'
    suffix = '?page_size=100&order=&q=&only_available=true'
    categories = ['biznes-literatura', 'nauka-i-obrazovanie',
                  'kompyutery-i-internet', 'publitsistika-i-istoriya',
                  'meditsinskaya-literatura', 'psihologicheskaya-literatura',
                  'dom-byt-dosug', 'detskaya-literatura-igry',
                  'iskusstvo-i-kultura', 'prochee']
    for cat in categories:
        print('*' * 50)
        url = '%s%s%s' % (prefix, cat, suffix)
        print(url)
        bs = get_page(url)
        books_list = create_books_list(bs)


if __name__ == '__main__':
    main()
