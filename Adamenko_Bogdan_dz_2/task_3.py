list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for item in list:
    if item.isdigit():
        idx = list.index(item)
        list[idx] = f'"{int(item):02d}"'
    elif item.startswith('+') or item.startswith('-') and item[1:].isdigit():
        idx = list.index(item)
        list[idx] = f'"{int(item):+03d}"'
my_str = ' '.join(list)
print(my_str)