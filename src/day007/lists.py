# Создать список, применить append, extend, insert, pop, remove;
# после каждой операции вывести список.

l = [1, 7, 5, 8, 10]
print(f'List: {l}')

a = 5
b = [1] * a
print(f'[1] * {a} = {b}')

l.append(12)
print(f'Append 12: {l}')

l.extend([13, 15])
print(f'Extend [13, 15]: {l}')

l.insert(1, 4)
print(f'Insert 4 at index 1: {l}')

p = l.pop()
print(f'L pop() with {p}: {l}')

l.remove(4)
print(f'Removed value 4: {l}')

print(f'l[-1] = {l[-1]}')

a, b, c = [1, 2, 3]

print(f'a = {a}, b = {b}, c = {c}')

# Обойти список по значениям и индексам; затем через `enumerate` после изучения его примера

for i in l:
    print(f'Value {i}')

for i in range(0, len(l)):
    print(f'Index {i}: Value {l[i]}')

for i, v in enumerate(l):
    print(f'Index {i}: Value {v}')

# Скопировать список через slicing; изменить копию и проверить оригинал.

sliced = l[:]
sliced[1] = 2
print(f"""Original: {l}
Mutated: {sliced}""")

# Отсортировать числа через `sorted` и `list.sort`; записать разницу return value.
print(f"""Sorted: {sorted(l)}
Original: {l}""")

l.sort()
print(f"Original Sorted: {l}")

a = [1, 3, 5]
b = [2, 4, 6]
for i, j in zip(a, b):
    print(i, j)

l.reverse()
print(f"Reversed: {l}")

l.sort(key=lambda x: x)
print(f"Sorted: {l}")

# comprehension
arr = [i for i in range(5)]
print(f'Comprehension: {arr}')

# init correct
a1 = [[0] * 4 for i in range(4)]
print(f'correct = {a1}')

# init wrong (same object 4 times)
a1 = [[0] * 4] * 4
a1[0][0] = 1
print(f'wrong = {a1}')
