import requests
from bs4 import BeautifulSoup
import openpyxl

# Отправляем GET-запрос на сайт и получаем HTML-код страницы
url = 'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&foot_min=45&is_by_homeowner=1&kitchen_stove=gas&min_balconies=1&minsu_r=1&offer_type=flat&only_foot=2&region=1&repair%5B0%5D=3&room1=1&room2=1'
response = requests.get(url)
html = response.text

# Создаем объект BeautifulSoup для парсинга HTML-кода
soup = BeautifulSoup(html, 'html.parser')

# Находим все объявления на странице
adverts = soup.find_all('div', {'class': '_93444fe79c--card--_yguQ'})

# Создаем новый файл Excel и добавляем в него заголовки столбцов
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.append(['Адрес', 'Площадь', 'Цена'])

# Добавляем информацию о каждой квартире в файл Excel
for advert in adverts:
    address = advert.find('div', {'class': '_93444fe79c--address-links--1tfGW'}).text.strip()
    area = advert.find('div', {'class': '_93444fe79c--header--1fV2A'}).text.strip()
    price = advert.find('span', {'class': '_93444fe79c--header--2JyvH'}).text.strip()
    worksheet.append([address, area, price])

# Сохраняем файл Excel
workbook.save('cian.xlsx')
