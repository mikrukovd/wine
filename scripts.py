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

    sorted_drinks = []
    for data in enumerate(excel_data):

        text = {
            'Название': excel_data['Название'].to_list()[data[0]],
            'Сорт': excel_data['Сорт'].to_list()[data[0]],
            'Цена': excel_data['Цена'].to_list()[data[0]],
            'Картинка': excel_data['Картинка'].to_list()[data[0]],
            'Категория': excel_data['Категория'].to_list()[data[0]],
            'Акция': excel_data['Акция'].to_list()[data[0]]
        }

        sorted_drinks.append(text)

    drinks = defaultdict(list)
    for info in sorted_drinks:
        drinks[info['Категория']].append(info)
    return drinks
