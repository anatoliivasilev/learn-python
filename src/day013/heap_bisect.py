# Создать min-heap через `heapify`; выполнить push/pop.
from heapq import heapify, heappop, heappush, heapreplace, heappushpop, merge
from bisect import bisect_left, bisect_right, insort

nums = [4, 5, 2, 3, 9, 12]
print(f'nums = {nums}')

heapify(nums)
print(f'heapify(nums), nums = {nums}')

elm = heappop(nums)
print(f'heappop(nums), elm = {elm}, nums = {nums}')

heappush(nums, 6)
print(f'heappush(nums), nums = {nums}')

# Смоделировать max-heap через отрицательные числа
max_nums = [-4, -5, -2, -3, -9, -12]
heapify(max_nums)
print(f'heapify(max_nums), max_nums = {max_nums}')

elm = heappop(max_nums)
print(f'heappop(max_nums), elm = {elm}, nums = {max_nums}')

heappush(nums, -6)
print(f'heappush(max_nums), max_nums = {max_nums}')

# Применить `bisect_left`, `bisect_right`, `insort`;
# записать результаты на массиве с дубликатами.

array = [1, 2, 5, 8, 13]
print(f'array = {array}')

idx = bisect_left(array, 2)
print(f'bisect_left 2 idx = {idx}')

idx = bisect_right(array, 2)
print(f'bisect_right 2 idx = {idx}')

insort(array, 4)
print(f'insort array = {array}')

# Найти 3 наименьших элемента потока через heap размера 3

stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
heap = []

for s in stream:
    if len(heap) < 3:
        heappush(heap, -s)
    else:
        heappushpop(heap, -s)
print([-x for x in heap])

# Объединить два маленьких sorted списка вручную и сравнить с `heapq.merge`
a = [1, 2, 4]
b = [3, 5, 7]

l = []
i, j = 0, 0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        l.append(a[i])
        i += 1
    else:
        l.append(b[j])
        j += 1
while i < len(a):
    l.append(a[i])
    i += 1
while j < len(b):
    l.append(b[j])
    j += 1

print(f'l = {l}')
print(f'l = {list(merge(a, b))}')

# Найти insertion position через bisect и через собственный linear scan.
print(f'a = {a}, bisect_left 2 = {bisect_left(a, 2)}')

candidate = 0
target = 3
for i, n in enumerate(a):
    if n <= target:
        candidate = i

print(f'candidate {target} = {candidate}')



