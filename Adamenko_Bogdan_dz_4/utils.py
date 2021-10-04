import requests
from decimal import *
from datetime import datetime

link = "http://www.cbr.ru/scripts/XML_daily.asp"


def currency_rates(name):
    response = requests.get(link).text
    name = name.upper()
    if name not in response:
        return None

    rate_start = response.find('<Value>', response.find(name)) + len('<Value>')
    rate_end = response.find('</Value>', rate_start)
    rate = Decimal(response[rate_start:rate_end].replace(',', '.'))

    date_start = response.find('Date="') + len('Date="')
    date_end = response.find('"', date_start)
    date_list = response[date_start:date_end].split(".")
    d, m, y = map(int, date_list)

    return f'{datetime(day=d, month=m, year=y)} {name}/RUB: {rate}'


