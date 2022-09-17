# -Добавить обработку страниц (Кир)+
# -Сохранение в файл(Мур)
# -Поиск по файлу(Мур)
# -Обработка ошибок(Kir)
#
#
#
#

from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
#asdkhfakjldsfhkljah

def get_page(url):
    html = urlopen(url)
    print(html)
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
        page_num = 1
        print('*' * 50)
        url = '%s%s?page=%d%s' % (prefix, cat, page_num, suffix)
        print('page %d' % page_num)
        print(url)

        bs = get_page(url)
        while True:
            books_list = create_books_list(bs)
            page_num += 1
            print('page %d' % page_num)
            url = '%s%s?page=%d%s' % (prefix, cat, page_num, suffix)
            bs = get_page(url)
            if bs.find('a', {'class': 'nav'}, text='Следующая')['href'] == '':
                break



if __name__ == '__main__':
    main()
