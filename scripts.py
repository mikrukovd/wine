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


def get_drinks_info(excel_file):
    '''Возвращает словарь отсортированный по категориям напитков'''
    excel_data = pandas.read_excel(
        excel_file,
        sheet_name='Лист1',
        keep_default_na=False
    )

    drinks_info = []
    for i in range(len(excel_data['Название'].to_list())):

        text = {
            'Название': excel_data['Название'].to_list()[i],
            'Сорт': excel_data['Сорт'].to_list()[i],
            'Цена': excel_data['Цена'].to_list()[i],
            'Картинка': excel_data['Картинка'].to_list()[i],
            'Категория': excel_data['Категория'].to_list()[i],
            'Акция': excel_data['Акция'].to_list()[i]
        }

        drinks_info.append(text)

    drinks = defaultdict(list)
    for info in drinks_info:
        drinks[info['Категория']].append(info)
    return drinks
