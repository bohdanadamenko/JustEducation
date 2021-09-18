for idx in range(1, 101):
    if idx % 10 == 1 and idx != 11:
        print(idx, 'процент')
    elif 1 < idx % 10 < 5 and idx != 12 and idx != 13 and idx != 14:
        print(idx, 'процента')
    else:
        print(idx, 'процентов')
