# Создать список, применить append, extend, insert, pop, remove;
# после каждой операции вывести список.

l = [1, 7, 5, 8, 10]
print(f'List: {l}')

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
