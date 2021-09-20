duration = int(input('Введите число: '))
d = duration // 86400
h = duration % 86400 // 3600
m = duration % 3600 // 60
s = duration % 60
list_1 = [d, h, m, s]
list_2 = [str(d) + ' дн ', str(h) + ' час ', str(m) + ' мин ', str(s) + ' сек']
list_3 = str()
for idx in range(4):
    if list_1[idx] > 0:
        list_3 += list_2[idx]
print(list_3)