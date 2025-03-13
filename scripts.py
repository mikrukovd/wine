import pandas

from collections import defaultdict


def get_year(year):
    if year % 100 in range(11, 21):
        return f'Уже {year} лет с вами'
    elif year % 10 == 1:
        return f'Уже {year} год с вами'
    elif year % 10 in range(2, 5):
        return f'Уже {year} года с вами'
    else:
        return f'Уже {year} лет с вами'


def get_sorted_drinks(excel_file):
    '''Возвращает словарь отсортированный по категориям напитков'''
    excel_data = pandas.read_excel(
        excel_file,
        sheet_name='Лист1',
        keep_default_na=False
    )

    sorted_drinks = defaultdict(list)
    for i, row in enumerate(excel_data.itertuples(index=False)):

        text = {
            'Название': row[1],
            'Сорт': row[2],
            'Цена': row[3],
            'Картинка': row[4],
            'Категория': row[0],
            'Акция': row[5]
        }

        sorted_drinks[text['Категория']].append(text)
    return sorted_drinks
