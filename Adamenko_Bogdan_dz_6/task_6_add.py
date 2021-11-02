import sys

sale = sys.argv[1]

with open('bakery.csv', 'a', encoding='utf-8') as bakery:
    bakery.write(f'{sale} \n')
print(f'== Добавлено: {sale} ===')