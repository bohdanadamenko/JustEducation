from random import uniform
numbers = []
idx = 0
while idx < 10:
    numbers.append(uniform(1, 1000))
    idx += 1
print(numbers)
for number in numbers:
    grn = int(number)
    kk = (number - grn) * 100
    print(f'{grn} грн {kk:02.0f} коп')
print(id(numbers))
numbers.sort()
print(id(numbers))
print([f'{int(number)} грн {(number - int(number)) * 100:02.0f} коп' for number in numbers[::-1][:5]])



