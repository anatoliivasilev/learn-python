import copy as c
# Исправить 5 фрагментов с aliasing/shared rows.

# 1 Две переменные указывают на один список
original = [1, 2, 3]
# copy = original
copy = original.copy()
copy.append(4)
print(original)
print(copy)

# 2 Shared rows в матрице
rows = 3
columns = 4
# matrix = [[0] * columns] * rows
matrix = [[0] * columns for i in range(rows)]
matrix[0][1] = 7
print(matrix)

# 3 Вложенный список и поверхностная копия
original = [
    ["Python", "Java"],
    ["AWS", "Docker"]
]
#copy = original.copy()
copy = c.deepcopy(original)
copy[0].append("JavaScript")
print(original)
print(copy)

# 4 Один список используется для нескольких пользователей
default_skills = []
# users = {
#     "Alice": default_skills,
#     "Bob": default_skills
# }
users = {
    "Alice": default_skills.copy(),
    "Bob": default_skills.copy()
}
users["Alice"].append("Python")
print(users)

# 5. Повторение одного изменяемого объекта
default_user = {
    "name": "",
    "skills": []
}
# users = [default_user] * 3
users = [c.deepcopy(default_user) for i in range(3)]
users[0]["name"] = "Alice"
users[0]["skills"].append("Python")
print(users)

# Написать `append_item(item, items=None)` и тесты
def append_item(item, items=None):
    if items == None:
        items = []
    items.append(item)
    return items

assert append_item(1) == [1]
assert append_item(2) == [2]
assert append_item(3) == [3]

# Создать корректную матрицу 3x3 и доказать отсутствие shared rows
a = [[0] * 3 for i in range(3)]
a[0][0] = 1
a[1][1] = 2
a[2][2] = 3
print(f'a = {a}')
