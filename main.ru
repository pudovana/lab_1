from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
page = 1

wb = Workbook()
ws = wb.active
ws.append(['Адрес', 'Площадь', 'Цена'])
url = 'https://www.cian.ru/kupit-4-komnatnuyu-kvartiru/'


response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
adverts = soup.find_all('div', {'class': '_93444fe79c--card--_yguQ'})

for advert in adverts:
    address = advert.find('div', {'class': '_93444fe79c--address-links--1tfGW'}).text.strip()
    area = advert.find('div', {'class': '_93444fe79c--header--1fV2A'}).text.strip()
    price = advert.find('span', {'class': '_93444fe79c--header--dC7Xh'}).text.strip()
    print(address, area, price)
    ws.append([address, area, price])
wb.save('cian.xlsx')
wb.close()
