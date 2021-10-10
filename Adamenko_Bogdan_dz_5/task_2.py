n = int(input('числа до: '))
gen = (i for i in range(1, n + 1, 2))
print([i for i in gen])