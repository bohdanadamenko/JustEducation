my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
for item in my_list:
    if item.isdigit():
        new_list.extend(['"', f'{int(item):02}', '"'])
    elif item[0] == '+':
        new_list.extend(['"', f'{item[0]}{int(item):02}', '"'])
    else:
        new_list.append(item)
my_str = ' '.join(new_list)

a = 0
for idx, letter in enumerate(my_str):
    if letter == '"':
        if a % 2 == 0:
            my_str = my_str[:idx + 1 - a] + my_str[idx + 2 - a:]
            a += 1
        else:
            my_str = my_str[:idx - 1 - a] + my_str[idx - a:]
            a += 1
print(my_str)
