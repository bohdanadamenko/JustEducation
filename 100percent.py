for i in list(range(1,101)):
    if i % 10 == 0 or i % 10 in range(5,10) or i % 100 == i in range(11,20):
        print(i, 'процентов')
    elif i % 10 == 1 and i % 100 != 11:
        print(i, 'процент')
    elif i % 10 in range(2,5):
        print(i, 'процента')
