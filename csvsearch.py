import pandas as pd
import os

def get_table(cat, key_word):
    lit_data = pd.read_csv('tables/%s' % cat)

    print(lit_data)


def main():
    catigories = os.listdir('./tables/')
    print('Поиск в категории по ключевому слову:')
    for i in range(len(catigories)):
        print(i+1, catigories[i][0:-4])
    catigorie = (int(input('Выбери номер категории: ')) - 1)
    keyword = input('Введи ключевое слово: ')
    get_table(catigories[catigorie], keyword)


if __name__ == '__main__':
    main()