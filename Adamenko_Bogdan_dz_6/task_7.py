import sys
idx, price = sys.argv[1:]

with open('bakery.csv', 'r+', encoding='utf-8') as b:
    tmp = open('bakery.tmp', 'w+', encoding='utf-8')
    lines = sum(1 for i in enumerate(b, 1)) + 1
    b.seek(0)

    for i, v in enumerate(b, 1):
        if i == int(idx):
            tmp.write(f'{price}\n')
        elif int(idx) in range(lines):
            tmp.write(v)
        else:
            exit('Нет такого значения')

    b.truncate(0)
    tmp.seek(0)
    b.seek(0)
    for line in tmp:
        print(line)
        b.write(line)
    tmp.close()
    b.close()