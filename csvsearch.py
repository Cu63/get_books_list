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
    for v in book_dict:
        print(v)



def main():
    catigories = os.listdir('./tables/')
    print('Поиск в категории по ключевому слову:')
    for i in range(len(catigories)):
        print(i+1, catigories[i][0:-4])
    catigorie = (int(input('Выбери номер категории: ')) - 1)
    keyword = input('Введи ключевое слово: ')
    get_table(catigories[catigorie])


if __name__ == '__main__':
    main()