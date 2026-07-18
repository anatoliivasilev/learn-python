import copy
# Показать aliasing: `b=a`; изменить b; проверить a.

a = 1
b = a
print(f'a = {a}, b = {b}')
b = 2
print(f'a = {a}, b = {b}')

# Сравнить `a[:]`, `list(a)`, `copy.copy`, `copy.deepcopy` на вложенном списке.

a = [[0] * 4 for i in range(2)]
print(f'a = {a}')
print(f'a[:] = {a[:]}')
b = copy.copy(a)
c = copy.deepcopy(a)
a[0][0] = 1
print(f'copy.copy(a) = {b}')
print(f'copy.deepcopy(a) = {c}')

# Проверить `is` и `==` на двух списках с одинаковым содержимым.
a = [1, 2, 3]
b = [1, 2, 3]
print(f'{a} is {b} = {a is b}')
print(f'{a} == {b} = {a == b}')

# Воспроизвести mutable default argument; исправить через `None`.
def add_value(value, list=[]):
    list.append(value)
    return list

print(f'add_value(1) = {add_value(1)}')
print(f'add_value(2) = {add_value(2)}')

def add_value_fixed(value, list=None):
    if list == None:
        list = []
    list.append(value)
    return list

print(f'add_value_fixed(1) = {add_value_fixed(1)}')
print(f'add_value_fixed(2) = {add_value_fixed(2)}')
