import sys

args = sys.argv[1:]
with open('bakery.csv', encoding='utf-8') as b:
    if len(args) == 1:
        start = int(args[0])
        stop = sum(1 for line in b)
        b.seek(0)
    elif len(args) > 1:
        start = int(args[0])
        stop = int(args[1])
    else:
        start = 0
        stop = sum(1 for line in b)
        b.seek(0)

    for idx, item in enumerate(b):
        if start <= idx + 1 <= stop:
            print(item.strip())