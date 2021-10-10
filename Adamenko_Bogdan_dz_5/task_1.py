def odd_nums(n):
    for i in range(1, n + 1, 2):
        yield i


gen = odd_nums(10)
print(next(gen))
print(next(gen))
print(next(gen))




