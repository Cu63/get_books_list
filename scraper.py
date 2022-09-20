# -Добавить обработку страниц (Кир)+
# -Сохранение в файл(Мур)
# -Поиск по файлу(Мур)
# -Обработка ошибок(Kir)
#

from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
import pandas as pd
from urllib.error import HTTPError, URLError


def get_page(url):
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
    return bs


def create_books_list(bs, table):
    prefix = 'https://www.piter.com'
    for book in bs.find_all('div', {'class': re.compile(
        '(grid-3 prod-block).*')}):
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

#        print('Title: %s' % title)
#        print('Author: %s' % author)
#        print('Price: %s' % price)
#        print('Url: %s' % url)
        table['Title'].append(title)
        table['Author'].append(author)
        table['Price'].append(price)
        table['Url'].append(price)



def main():
    prefix = 'https://www.piter.com/collection/'
    suffix = '?page_size=100&order=&q=&only_available=true'
    categories = ['biznes-literatura', 'nauka-i-obrazovanie',
                  'kompyutery-i-internet', 'publitsistika-i-istoriya',
                  'meditsinskaya-literatura', 'psihologicheskaya-literatura',
                  'dom-byt-dosug', 'detskaya-literatura-igry',
                  'iskusstvo-i-kultura', 'prochee']
    for cat in categories:
        table = {'Title': [], 'Author': [], 'Price': [], 'Url': []}

# start page
        page_num = 1
        print('*' * 50)
        url = '%s%s?page=%d%s' % (prefix, cat, page_num, suffix)
        print('page %d' % page_num)
        print(url)

# get html page
        bs = get_page(url)
        while True:
            create_books_list(bs, table)
            # increase page num
            page_num += 1
            print('page %d' % page_num)
            # url of next
            url = '%s%s?page=%d%s' % (prefix, cat, page_num, suffix)
            bs = get_page(url)
            # check last page
            if bs.find('a', {'class': 'nav'}, text='Следующая')['href'] == '':
                frame = pd.DataFrame(table)
                print(frame)
                break



if __name__ == '__main__':
    main()
