numbers3 = []

for number in range(1, 1000, 2):
    number3 = number ** 3
    numbers3.append(number3)

total_summ = 0
total_summ17 = 0

for i in numbers3:
    isumm = sum(map(int, str(i)))
    if isumm % 7 == 0:
        total_summ += isumm
    isumm_17 = sum(map(int, str(i + 17)))
    if isumm_17 % 7 == 0:
        total_summ17 += isumm_17

print(total_summ)
print(total_summ17)