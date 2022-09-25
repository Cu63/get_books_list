import pandas as pd
import os


def get_table(cat):
    book_dict = []
    lit_data = open('./tables/%s' % cat, 'r', encoding='utf8')
    text = lit_data.read()
    lit_data.close()
    prom = text.split('\n')
    prom = prom[1:]
    for c in prom:
        s = c.split(';')
        book_dict.append(s)
    return book_dict


def sercher(table, keyword):
    result = []
    for c in table:
        if keyword in c:
            result.append(c)
    return result


def main():
    catigories = os.listdir('./tables/')
    print('Поиск в категории по ключевому слову:')
    for i in range(len(catigories)):
        print(i+1, catigories[i][0:-4])
    catigorie = (int(input('Выбери номер категории: ')) - 1)
    keyword = input('Введи ключевое слово: ')
    print(sercher(get_table(catigories[catigorie]), keyword))


if __name__ == '__main__':
    main()