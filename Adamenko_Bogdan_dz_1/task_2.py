list_1 = []
for number in range(1, 1001, 2):
    list_1.append(number ** 3)
sum_1 = 0
sum_17 = 0
for idx in range(len(list_1)):
    sum_1_1 = 0
    sum_17_1 = 0
    for idx_2 in range(1, 10):
        sum_1_1 += list_1[idx] % 10 ** idx_2 // 10 ** (idx_2 - 1)
        sum_17_1 += (list_1[idx]+17) % 10 ** idx_2 // 10 ** (idx_2 - 1)
    if sum_1_1 % 7 == 0:
        sum_1 += sum_1_1
    if sum_17_1 % 7 == 0:
        sum_17 += sum_17_1
print(sum_1)
print(sum_17)

