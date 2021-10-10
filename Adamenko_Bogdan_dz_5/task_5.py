import time
start = time.time()
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
resoult = [i for i in src if src.count(i) == 1]
print(resoult)
end = time.time()
print(end - start)

start = time.time()
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique = set()
tmp = set()
for num in src:
    if num not in tmp:
        unique.add(num)
    else:
        unique.discard(num)
    tmp.add(num)
""" Получаем множество не повторяющихся чисел, теперь вернем такой же порядок как в списке src"""
unique_ord = [num for num in src if num in unique]
print(unique_ord)
end = time.time()
print(end - start)
